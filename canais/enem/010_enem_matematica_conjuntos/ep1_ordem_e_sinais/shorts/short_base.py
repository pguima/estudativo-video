# Base dos Shorts do episódio: recorta o vídeo final (16:9) num quadro vertical 1080x1920, sem re-render.
# Topo: selo + pergunta-gancho fixa · meio: aula com bordas esfumadas · abaixo: legenda queimada ampliada · rodapé: aula completa.
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).resolve().parent
EP = AQUI.parent
SRC = EP / "final" / "enem_matematica_conjuntos_ep1_ordem_e_sinais.mp4"
FONTES = EP.parents[3] / "_ferramentas" / "fontes" / "inter" / "extras" / "ttf"

W, H = 1080, 1920
BG = (236, 236, 231)
TINTA, AZUL, VERDE, VERMELHO, CINZA = (28, 28, 30), (59, 108, 246), (22, 150, 90), (220, 60, 60), (110, 110, 115)
SELO = "MATEMÁTICA ENEM"
RODAPE = "Matemática ENEM do Zero · Episódio 1"

# recortes do vídeo 1920x1080 (x, y, w, h)
CONT = (130, 20, 1660, 810)   # conteúdo da aula
LEG = (260, 860, 1400, 140)   # legenda queimada
CONT_H = round(CONT[3] * W / CONT[2]) // 2 * 2
LEG_H = round(LEG[3] * W / LEG[2]) // 2 * 2
Y_SELO = 190
Y_CONT = 560
Y_LEG = Y_CONT + CONT_H + 10
Y_RODAPE = Y_LEG + LEG_H + 70


def fonte(tam, peso="extrabold"):
    nome = {"semibold": "Inter-SemiBold", "bold": "Inter-Bold", "extrabold": "Inter-ExtraBold", "black": "Inter-Black"}[peso]
    return ImageFont.truetype(str(FONTES / f"{nome}.ttf"), tam)


def centro(d, y, partes, tam, peso="extrabold"):
    """desenha [(texto, cor), ...] numa linha centralizada (reduz a fonte se passar da largura útil)"""
    f = fonte(tam, peso)
    larg = sum(d.textlength(t, font=f) for t, _ in partes)
    if larg > W - 100:
        tam = int(tam * (W - 100) / larg)
        y += (fonte(tam, peso).size - f.size) * -0.5
        f = fonte(tam, peso)
        larg = sum(d.textlength(t, font=f) for t, _ in partes)
    x = (W - larg) / 2
    for t, c in partes:
        d.text((x, y), t, font=f, fill=c)
        x += d.textlength(t, font=f)


def mascara(w, h, borda, caminho):
    """alfa com bordas esfumadas, para o recorte se fundir ao fundo"""
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rectangle((borda, borda, w - borda, h - borda), fill=255)
    m.filter(ImageFilter.GaussianBlur(borda / 2)).save(caminho)


def fundo(caminho, linha1, linha2):
    """linha1/linha2 = [(texto, cor), ...]: a pergunta-gancho fixa no topo"""
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    f = fonte(32, "extrabold")
    lw = d.textlength(SELO, font=f)
    d.rounded_rectangle(((W - lw) / 2 - 30, Y_SELO, (W + lw) / 2 + 30, Y_SELO + 60), 16, fill=(255, 255, 255))
    d.text(((W - lw) / 2, Y_SELO + 11), SELO, font=f, fill=AZUL)
    centro(d, Y_SELO + 95, linha1, 120, "black")
    centro(d, Y_SELO + 235, linha2, 92, "black")
    centro(d, Y_RODAPE, [("Aula completa no canal", TINTA)], 46, "extrabold")
    centro(d, Y_RODAPE + 66, [(RODAPE, CINZA)], 36, "semibold")
    im.save(caminho)


def gerar(nome, trechos, linha1, linha2):
    """nome = base dos arquivos (shorts/<nome>.mp4); trechos = [(início, fim), ...] em segundos do vídeo final"""
    out = AQUI / f"{nome}.mp4"
    prefixo = nome.split("_")[0]
    fundo_png = AQUI / f"{prefixo}_fundo.png"
    masc_c = AQUI / f"{prefixo}_mascara_conteudo.png"
    masc_l = AQUI / f"{prefixo}_mascara_legenda.png"
    fundo(fundo_png, linha1, linha2)
    mascara(W, CONT_H, 24, masc_c)
    mascara(W, LEG_H, 14, masc_l)

    filtros, rot = [], []
    for i, (a, b) in enumerate(trechos):
        filtros.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}]")
        filtros.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.04,afade=t=out:st={b - a - 0.06}:d=0.06[a{i}]")
        rot.append(f"[v{i}][a{i}]")
    cx, cy, cw, ch = CONT
    lx, ly, lw, lh = LEG
    filtros += [
        f"{''.join(rot)}concat=n={len(trechos)}:v=1:a=1[v][a]",
        "[v]split[va][vb]",
        f"[va]crop={cw}:{ch}:{cx}:{cy},scale={W}:{CONT_H}:flags=lanczos,format=rgba[c0]",
        f"[vb]crop={lw}:{lh}:{lx}:{ly},scale={W}:{LEG_H}:flags=lanczos,format=rgba[l0]",
        "[2:v]format=gray[mc]",
        "[3:v]format=gray[ml]",
        "[c0][mc]alphamerge[c]",
        "[l0][ml]alphamerge[l]",
        f"[1:v][c]overlay=0:{Y_CONT}[t1]",
        f"[t1][l]overlay=0:{Y_LEG},format=yuv420p[out]",
    ]
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(SRC),
           "-loop", "1", "-framerate", "30", "-i", str(fundo_png),
           "-loop", "1", "-framerate", "30", "-i", str(masc_c),
           "-loop", "1", "-framerate", "30", "-i", str(masc_l),
           "-filter_complex", ";".join(filtros), "-map", "[out]", "-map", "[a]", "-shortest",
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-r", "30",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    for p in (masc_c, masc_l):
        p.unlink()
    print(out)
