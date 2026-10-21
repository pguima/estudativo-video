# Base dos Shorts do canal Tecnologia: recorta o vídeo final (16:9) num quadro vertical 1080x1920, sem re-render.
# Visual escuro/neon do tech.py: topo com chip HUD + pergunta-gancho fixa · meio: painéis do vídeo com bordas esfumadas
# · abaixo: legenda queimada ampliada · rodapé: vídeo completo no canal.
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).resolve().parent
EP = AQUI.parent
SRC = EP / "final" / "tecnologia_001_rea_engenharia_reversa.mp4"
INTER = EP.parents[2] / "_ferramentas" / "fontes" / "inter" / "extras" / "ttf"
MONO = Path(r"C:\Windows\Fonts\consolab.ttf")

W, H = 1080, 1920
BG = (6, 12, 30)
BRANCO, CIANO, VIOLETA, MAGENTA = (234, 242, 255), (34, 211, 238), (167, 139, 250), (244, 114, 182)
VERDE, AMBAR, ROSA, CINZA = (74, 222, 128), (251, 191, 36), (251, 113, 133), (169, 184, 208)
SELO = "TECH//001 · REA"
RODAPE = "REA: engenharia reversa com IA"

# recortes do vídeo 1920x1080 (x, y, w, h)
CONT = (60, 50, 1800, 800)    # título + painéis (margem para a borda esfumada não comer o texto)
LEG = (200, 905, 1520, 100)   # legenda queimada
CONT_H = round(CONT[3] * W / CONT[2]) // 2 * 2
LEG_H = round(LEG[3] * W / LEG[2]) // 2 * 2
Y_SELO = 280
Y_CONT = 680
Y_LEG = Y_CONT + CONT_H + 10
Y_RODAPE = Y_LEG + LEG_H + 70


def fonte(tam, peso="black"):
    if peso == "mono":
        return ImageFont.truetype(str(MONO), tam)
    nome = {"semibold": "Inter-SemiBold", "bold": "Inter-Bold", "extrabold": "Inter-ExtraBold", "black": "Inter-Black"}[peso]
    return ImageFont.truetype(str(INTER / f"{nome}.ttf"), tam)


def linha(d, y, partes, tam, peso="black"):
    """[(texto, cor), ...] centralizado; reduz a fonte se passar da largura útil. Devolve [(x, y, texto, cor, fonte)]"""
    f = fonte(tam, peso)
    larg = sum(d.textlength(t, font=f) for t, _ in partes)
    if larg > W - 100:
        novo = int(tam * (W - 100) / larg)
        y += (tam - novo) * 0.5
        f = fonte(novo, peso)
        larg = sum(d.textlength(t, font=f) for t, _ in partes)
    x, out = (W - larg) / 2, []
    for t, c in partes:
        out.append((x, y, t, c, f))
        x += d.textlength(t, font=f)
    return out


def glow(im, itens, raio=14, forca=0.9):
    """texto com halo neon da própria cor por baixo"""
    hal = Image.new("RGBA", im.size, (0, 0, 0, 0))
    dh = ImageDraw.Draw(hal)
    for x, y, t, c, f in itens:
        dh.text((x, y), t, font=f, fill=c + (int(255 * forca),))
    im.alpha_composite(hal.filter(ImageFilter.GaussianBlur(raio)))
    d = ImageDraw.Draw(im)
    for x, y, t, c, f in itens:
        d.text((x, y), t, font=f, fill=c)


def chanfro(d, x0, y0, x1, y1, k, cor, larg=3, fill=None):
    pts = [(x0 + k, y0), (x1, y0), (x1, y1 - k), (x1 - k, y1), (x0, y1), (x0, y0 + k)]
    if fill:
        d.polygon(pts, fill=fill)
    d.line(pts + [pts[0]], fill=cor, width=larg)


def mascara(w, h, borda, caminho):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rectangle((borda, borda, w - borda, h - borda), fill=255)
    m.filter(ImageFilter.GaussianBlur(borda / 2)).save(caminho)


def fundo(caminho, linha1, linha2):
    """fundo espacial (órbitas ciano/violeta + grade em perspectiva + cantos HUD) e a pergunta-gancho fixa"""
    im = Image.new("RGBA", (W, H), BG + (255,))
    luz = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dl = ImageDraw.Draw(luz)
    dl.ellipse((-350, -250, 650, 750), fill=(20, 120, 150, 120))
    dl.ellipse((450, 1250, 1450, 2250), fill=(90, 70, 170, 110))
    im.alpha_composite(luz.filter(ImageFilter.GaussianBlur(220)))
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dg = ImageDraw.Draw(g)
    hz = 1500
    for i in range(-12, 13):
        dg.line((W / 2 + i * 30, hz, W / 2 + i * 260, H), fill=(34, 211, 238, 34), width=2)
    for k in range(10):
        yy = hz + (H - hz) * (k / 10) ** 1.8
        dg.line((0, yy, W, yy), fill=(34, 211, 238, 30), width=2)
    for yy in range(0, H, 4):
        dg.line((0, yy, W, yy), fill=(0, 0, 0, 28))
    im.alpha_composite(g)
    d = ImageDraw.Draw(im)
    for (x, y, dx, dy) in [(40, 40, 1, 1), (W - 40, 40, -1, 1), (40, H - 40, 1, -1), (W - 40, H - 40, -1, -1)]:
        d.line((x, y, x + 70 * dx, y), fill=CIANO, width=4)
        d.line((x, y, x, y + 70 * dy), fill=CIANO, width=4)
    # chip HUD com o ponto "ao vivo"
    f = fonte(34, "mono")
    lw = d.textlength(SELO, font=f)
    x0 = (W - lw) / 2 - 56
    chanfro(d, x0, Y_SELO, (W + lw) / 2 + 30, Y_SELO + 64, 14, CIANO, 3, fill=(8, 30, 48))
    d.ellipse((x0 + 22, Y_SELO + 25, x0 + 36, Y_SELO + 39), fill=ROSA)
    d.text(((W - lw) / 2 + 4, Y_SELO + 13), SELO, font=f, fill=CIANO)
    glow(im, linha(d, Y_SELO + 105, linha1, 112), 16, 0.55)
    glow(im, linha(d, Y_SELO + 235, linha2, 96), 18, 0.8)
    glow(im, linha(d, Y_RODAPE, [("Vídeo completo no canal", BRANCO)], 46, "extrabold"), 10, 0.35)
    glow(im, linha(d, Y_RODAPE + 70, [("// " + RODAPE, CIANO)], 32, "mono"), 8, 0.5)
    im.convert("RGB").save(caminho)


def gerar(nome, trechos, linha1, linha2):
    """nome = base dos arquivos (shorts/<nome>.mp4); trechos = [(início, fim), ...] em segundos do vídeo final"""
    out = AQUI / f"{nome}.mp4"
    prefixo = nome.split("_")[0]
    fundo_png = AQUI / f"{prefixo}_fundo.png"
    masc_c = AQUI / f"{prefixo}_mascara_conteudo.png"
    masc_l = AQUI / f"{prefixo}_mascara_legenda.png"
    fundo(fundo_png, linha1, linha2)
    mascara(W, CONT_H, 30, masc_c)
    mascara(W, LEG_H, 22, masc_l)

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
