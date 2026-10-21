# Short-convite (1080x1920): "As aulas de Operações e Conjuntos Numéricos estão prontas"
# Narração: audio/narracao.wav (Gemini TTS local, voz Neno) · tempos: audio/palavras.json (faster-whisper)
# Trechos das aulas (sem som) tirados dos finais dos 5 episódios. Saída: convite_conjuntos.mp4
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).resolve().parent
SERIE = AQUI.parent
FONTES = SERIE.parents[2] / "_ferramentas" / "fontes" / "inter" / "extras" / "ttf"
W, H, FPS = 1080, 1920, 30
BG = (236, 236, 231)
TINTA, CINZA, BRANCO = (28, 28, 30), (110, 110, 115), (255, 255, 255)
AZUL, LARANJA, VERDE, VERMELHO, ROXO = (30, 111, 217), (255, 122, 26), (22, 150, 90), (220, 60, 60), (124, 77, 255)

# (início, fim, tipo, dados) em segundos da narração
EPS = [  # nº, título (2 linhas), cor, vídeo, início do trecho
    (1, ("Ordem das operações", "e regra de sinais"), AZUL, "ep1_ordem_e_sinais", 116.0),
    (2, ("Racional ou", "irracional?"), ROXO, "ep2_conjuntos_numericos", 19.0),
    (3, ("Intervalos reais:", "bolinha cheia ou vazia?"), VERDE, "ep3_intervalos", 118.0),
    (4, ("Diagrama de Venn:", "ponto garantido"), LARANJA, "ep4_venn", 118.0),
    (5, ("Revisão:", "as pegadinhas do ENEM"), VERMELHO, "ep5_revisao", 58.0),
]
CORTES = [0.0, 4.0, 11.2, 18.0, 22.3, 26.3, 29.65, 33.6]  # gancho, prontas, ep1..ep5, CTA
DUR = 42.6

# legenda: palavras do whisper com as correções do que foi dito
CORRIGE = {"enente": "ENEM", "Enem": "ENEM", "Enem.": "ENEM.", "bem,": "Venn,", "-se": None}


def palavras():
    ws = json.load(open(AQUI / "audio" / "palavras.json", encoding="utf-8"))[0]["words"]
    out = []
    for w in ws:
        t = CORRIGE.get(w["w"], w["w"])
        if t is None:
            out[-1]["w"] += w["w"]; out[-1]["e"] = w["e"]; continue
        out.append(dict(w=t, s=w["s"], e=w["e"]))
    return out


_F = {}
def fonte(tam, peso="extrabold"):
    k = (tam, peso)
    if k not in _F:
        nome = {"semibold": "Inter-SemiBold", "bold": "Inter-Bold", "extrabold": "Inter-ExtraBold", "black": "Inter-Black"}[peso]
        _F[k] = ImageFont.truetype(str(FONTES / f"{nome}.ttf"), tam)
    return _F[k]


def ease(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def pop(x):  # ease-out com leve passada (escala de "pulo")
    x = max(0.0, min(1.0, x))
    return 1 + 2.2 * (x - 1) ** 3 + 1.2 * (x - 1) ** 2 if x < 1 else 1.0


def texto_c(d, y, partes, tam, peso="black", maxw=W - 120, alpha=255):
    f = fonte(tam, peso)
    larg = sum(d.textlength(t, font=f) for t, _ in partes)
    if larg > maxw:
        tam = int(tam * maxw / larg); f = fonte(tam, peso)
        larg = sum(d.textlength(t, font=f) for t, _ in partes)
    x = (W - larg) / 2
    for t, c in partes:
        d.text((x, y), t, font=f, fill=c + (alpha,))
        x += d.textlength(t, font=f)


def camada():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def cola(base, lay, a, dy=0):
    """cola a camada com opacidade a (0..1) e deslocamento vertical dy"""
    if a <= 0:
        return
    if a < 1:
        al = lay.getchannel("A").point(lambda v: int(v * a)); lay.putalpha(al)
    base.alpha_composite(lay, (0, int(dy)))


def cartao(lay, box, raio=36, cor=BRANCO, sombra=True):
    x0, y0, x1, y1 = box
    if sombra:
        s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(s).rounded_rectangle((x0, y0 + 14, x1, y1 + 14), raio, fill=(0, 0, 0, 40))
        lay.alpha_composite(s.filter(ImageFilter.GaussianBlur(18)))
    ImageDraw.Draw(lay).rounded_rectangle(box, raio, fill=cor + (255,))


def pilula(d, cx, y, texto, tam, cor_fundo, cor_texto=BRANCO, pad=30, alt=None):
    f = fonte(tam, "extrabold")
    lw = d.textlength(texto, font=f)
    alt = alt or int(tam * 1.9)
    d.rounded_rectangle((cx - lw / 2 - pad, y, cx + lw / 2 + pad, y + alt), alt // 2, fill=cor_fundo + (255,))
    d.text((cx - lw / 2, y + (alt - tam * 1.2) / 2), texto, font=f, fill=cor_texto + (255,))


# ---------- fundo fixo ----------
def fundo():
    im = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(im)
    for (cx, cy, r, c) in ((-80, 1820, 420, AZUL), (1160, 120, 380, LARANJA)):
        d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=c + (38,), width=34)
    return im


LOGO = Image.open(AQUI / "logo_estudativo.png").convert("RGBA").crop((90, 180, 1190, 1010))


def logo(lay, cx, cy, larg):
    lg = LOGO.resize((larg, int(larg * LOGO.height / LOGO.width)), Image.LANCZOS)
    box = (cx - larg // 2 - 30, cy - lg.height // 2 - 26, cx + larg // 2 + 30, cy + lg.height // 2 + 26)
    cartao(lay, box, 40)
    lay.alpha_composite(lg, (cx - lg.width // 2, cy - lg.height // 2))


# ---------- trechos das aulas ----------
CROP = (130, 20, 1660, 810)  # área do conteúdo no vídeo 1920x1080
CLIP_W = 1000
CLIP_H = round(CROP[3] * CLIP_W / CROP[2])


def ler_trecho(pasta, ini, dur):
    src = next((SERIE / pasta / "final").glob("*.mp4"))
    cx, cy, cw, ch = CROP
    cmd = ["ffmpeg", "-v", "error", "-ss", str(ini), "-t", str(dur + 0.2), "-i", str(src),
           "-vf", f"crop={cw}:{ch}:{cx}:{cy},scale={CLIP_W}:{CLIP_H}:flags=lanczos,fps={FPS}",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = CLIP_W * CLIP_H * 3
    return [Image.frombytes("RGB", (CLIP_W, CLIP_H), raw[i:i + n]) for i in range(0, len(raw) - n + 1, n)]


MASC = Image.new("L", (CLIP_W, CLIP_H), 0)
ImageDraw.Draw(MASC).rounded_rectangle((0, 0, CLIP_W - 1, CLIP_H - 1), 30, fill=255)


# ---------- cenas ----------
def selo(lay):
    d = ImageDraw.Draw(lay)
    pilula(d, W // 2, 150, "MATEMÁTICA ENEM", 34, BRANCO, AZUL)


def cena_gancho(base, t):
    lay = camada(); selo(lay); cola(base, lay, 1)
    for i, (y, partes, tam) in enumerate((
            (520, [("Matemática", TINTA)], 128),
            (680, [("no ", TINTA), ("ENEM", AZUL)], 128),
            (880, [("te dá um", TINTA)], 92),
            (1000, [("frio na barriga?", LARANJA)], 104))):
        a = ease((t - 0.35 * i) / 0.45)
        lay = camada(); texto_c(ImageDraw.Draw(lay), y, partes, tam)
        cola(base, lay, a, 30 * (1 - a))
    a = ease((t - 2.6) / 0.4)
    lay = camada(); pilula(ImageDraw.Draw(lay), W // 2, 1190, "Então presta atenção 👀".replace(" 👀", ""), 44, TINTA)
    cola(base, lay, a, 20 * (1 - a))


def cena_prontas(base, t):
    lay = camada(); selo(lay); cola(base, lay, 1)
    a = ease(t / 0.5)
    lay = camada(); texto_c(ImageDraw.Draw(lay), 300, [("As aulas estão", TINTA)], 84); cola(base, lay, a, 30 * (1 - a))
    # carimbo PRONTAS!
    s = pop((t - 0.4) / 0.5)
    if s > 0:
        st = Image.new("RGBA", (760, 190), (0, 0, 0, 0)); d = ImageDraw.Draw(st)
        d.rounded_rectangle((0, 0, 759, 189), 40, fill=VERDE + (255,))
        f = fonte(120, "black"); lw = d.textlength("PRONTAS!", font=f)
        d.text(((760 - lw) / 2, 22), "PRONTAS!", font=f, fill=BRANCO + (255,))
        st = st.rotate(-4, expand=True, resample=Image.BICUBIC)
        st = st.resize((max(1, int(st.width * s)), max(1, int(st.height * s))), Image.LANCZOS)
        base.alpha_composite(st, (W // 2 - st.width // 2, 520 - st.height // 2))
    a = ease((t - 1.0) / 0.5)
    lay = camada(); cartao(lay, (90, 700, 990, 1060), 40)
    d = ImageDraw.Draw(lay)
    texto_c(d, 750, [("SÉRIE", CINZA)], 36, "extrabold")
    texto_c(d, 810, [("Operações e", AZUL)], 84)
    texto_c(d, 915, [("Conjuntos Numéricos", AZUL)], 84, maxw=820)
    cola(base, lay, a, 40 * (1 - a))
    # 5 episódios aparecendo em sequência (narração: "São cinco episódios" ≈ 3,7 s)
    lay = camada(); d = ImageDraw.Draw(lay)
    for i, (n, _, cor, _, _) in enumerate(EPS):
        a = ease((t - 3.6 - 0.15 * i) / 0.35)
        if a <= 0: continue
        cx = W // 2 + (i - 2) * 170; cy = 1180 + 20 * (1 - a)
        r = 62 * (0.6 + 0.4 * a)
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=cor + (int(255 * a),))
        f = fonte(64, "black"); lw = d.textlength(str(n), font=f)
        d.text((cx - lw / 2, cy - 40), str(n), font=f, fill=BRANCO + (int(255 * a),))
    base.alpha_composite(lay)
    a = ease((t - 4.4) / 0.5)
    lay = camada(); texto_c(ImageDraw.Draw(lay), 1290, [("5 episódios · do zero", TINTA)], 58, "extrabold")
    cola(base, lay, a, 20 * (1 - a))


def cena_ep(base, t, k, frames):
    n, (l1, l2), cor, _, _ = EPS[k]
    lay = camada(); selo(lay); cola(base, lay, 1)
    a = ease(t / 0.4)
    lay = camada(); d = ImageDraw.Draw(lay)
    pilula(d, W // 2, 370, f"EPISÓDIO {n}", 40, cor)
    texto_c(d, 495, [(l1, TINTA)], 76)
    texto_c(d, 590, [(l2, cor)], 76)
    cola(base, lay, a, 24 * (1 - a))
    # trecho da aula num cartão
    a = ease((t - 0.1) / 0.45)
    fr = frames[min(int(t * FPS), len(frames) - 1)]
    lay = camada()
    y0 = 740
    cartao(lay, (W // 2 - CLIP_W // 2 - 14, y0 - 14, W // 2 + CLIP_W // 2 + 14, y0 + CLIP_H + 14), 40)
    lay.paste(fr, (W // 2 - CLIP_W // 2, y0), MASC)
    cola(base, lay, a, 50 * (1 - a))
    # trilha dos 5 episódios
    lay = camada(); d = ImageDraw.Draw(lay)
    for i, (m, _, c2, _, _) in enumerate(EPS):
        cx, cy = W // 2 + (i - 2) * 110, 740 + CLIP_H + 90
        if m == n:
            r = 40 * pop(t / 0.4)
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=c2 + (255,))
            f = fonte(44, "black"); lw = d.textlength(str(m), font=f)
            d.text((cx - lw / 2, cy - 28), str(m), font=f, fill=BRANCO + (255,))
        else:
            r = 28
            fill = c2 + (255,) if m < n else (210, 210, 205, 255)
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=fill)
            f = fonte(30, "black"); lw = d.textlength(str(m), font=f)
            d.text((cx - lw / 2, cy - 19), str(m), font=f, fill=BRANCO + (255,))
    base.alpha_composite(lay)


def cena_cta(base, t):
    lay = camada(); logo(lay, W // 2, 420, 640); a = ease(t / 0.5); cola(base, lay, a, 40 * (1 - a))
    # barra de busca do YouTube digitando "Estudativo"
    a = ease((t - 0.3) / 0.4)
    lay = camada(); d = ImageDraw.Draw(lay)
    cartao(lay, (110, 800, 970, 920), 60)
    alvo = "Estudativo"
    nlet = int(max(0, min(1, (t - 0.6) / 0.8)) * len(alvo))
    f = fonte(56, "bold")
    d.text((180, 828), alvo[:nlet], font=f, fill=TINTA + (255,))
    if int(t * 2) % 2 == 0:
        x = 180 + d.textlength(alvo[:nlet], font=f) + 4
        d.rectangle((x, 830, x + 4, 892), fill=AZUL + (255,))
    # lupa
    d.ellipse((868, 832, 912, 876), outline=CINZA + (255,), width=7)
    d.line((904, 868, 928, 892), fill=CINZA + (255,), width=8)
    cola(base, lay, a, 20 * (1 - a))
    # playlist
    a = ease((t - 2.4) / 0.5)
    lay = camada(); d = ImageDraw.Draw(lay)
    cartao(lay, (110, 980, 970, 1150), 36)
    d.rounded_rectangle((140, 1010, 290, 1120), 18, fill=AZUL + (255,))
    for i in range(3):
        d.rectangle((170, 1032 + i * 26, 260, 1042 + i * 26), fill=BRANCO + (255,))
    d.text((320, 1012), "PLAYLIST", font=fonte(30, "extrabold"), fill=CINZA + (255,))
    d.text((320, 1052), "Matemática ENEM do Zero", font=fonte(46, "black"), fill=TINTA + (255,))
    cola(base, lay, a, 30 * (1 - a))
    # inscreva-se + sininho (narração ≈ 5,1 s)
    a = ease((t - 4.9) / 0.4)
    lay = camada(); d = ImageDraw.Draw(lay)
    s = pop((t - 4.9) / 0.5)
    bw, bh = int(520 * s), int(130 * s)
    if bw > 2:
        d.rounded_rectangle((W // 2 - 90 - bw // 2, 1270 - bh // 2, W // 2 - 90 + bw // 2, 1270 + bh // 2), bh // 2, fill=VERMELHO + (255,))
        f = fonte(max(8, int(58 * s)), "black"); lw = d.textlength("INSCREVA-SE", font=f)
        d.text((W // 2 - 90 - lw / 2, 1270 - 36 * s), "INSCREVA-SE", font=f, fill=BRANCO + (255,))
    base.alpha_composite(lay)
    a = ease((t - 5.6) / 0.4)
    if a > 0:
        import math
        sino = Image.new("RGBA", (160, 160), (0, 0, 0, 0)); d = ImageDraw.Draw(sino)
        d.ellipse((0, 0, 159, 159), fill=LARANJA + (255,))
        d.pieslice((40, 30, 120, 120), 180, 360, fill=BRANCO + (255,))
        d.rectangle((40, 74, 120, 104), fill=BRANCO + (255,))
        d.rounded_rectangle((30, 100, 130, 114), 6, fill=BRANCO + (255,))
        d.ellipse((68, 112, 92, 134), fill=BRANCO + (255,))
        ang = 18 * math.sin((t - 5.6) * 14) * max(0, 1 - (t - 5.6) / 1.6)
        sino = sino.rotate(ang, resample=Image.BICUBIC)
        sino.putalpha(sino.getchannel("A").point(lambda v: int(v * a)))
        base.alpha_composite(sino, (W // 2 + 290 - 80, 1270 - 80))
    a = ease((t - 6.9) / 0.5)
    lay = camada(); texto_c(ImageDraw.Draw(lay), 1390, [("Bons estudos!", AZUL)], 92)
    cola(base, lay, a, 24 * (1 - a))


# ---------- legenda palavra a palavra ----------
def grupos(ws, maxc=22):
    gs, g = [], []
    for w in ws:
        if g and (sum(len(x["w"]) + 1 for x in g) + len(w["w"]) > maxc or g[-1]["w"][-1] in ".?!,"):
            gs.append(g); g = []
        g.append(w)
    gs.append(g)
    return gs


def legenda(base, t, gs):
    atual = None
    for g in gs:
        if g[0]["s"] - 0.05 <= t <= g[-1]["e"] + 0.35:
            atual = g
    if not atual:
        return
    lay = camada(); d = ImageDraw.Draw(lay)
    f = fonte(62, "black")
    txt = " ".join(w["w"] for w in atual)
    lw = d.textlength(txt, font=f)
    if lw > W - 120:
        f = fonte(int(62 * (W - 120) / lw), "black"); lw = d.textlength(txt, font=f)
    y = 1530
    d.rounded_rectangle(((W - lw) / 2 - 34, y - 18, (W + lw) / 2 + 34, y + 96), 30, fill=TINTA + (235,))
    x = (W - lw) / 2
    for w in atual:
        cor = LARANJA if w["s"] - 0.05 <= t else BRANCO
        d.text((x, y), w["w"], font=f, fill=cor + (255,))
        x += d.textlength(w["w"] + " ", font=f)
    base.alpha_composite(lay)


def main():
    so = float(sys.argv[1]) if len(sys.argv) > 1 else None  # prévia: um quadro no tempo t
    gs = grupos(palavras())
    FUNDO = fundo()
    clips = {}

    def frame(t):
        im = FUNDO.copy()
        i = max(j for j, c in enumerate(CORTES) if c <= t)
        lt = t - CORTES[i]
        if i == 0:
            cena_gancho(im, lt)
        elif i == 1:
            cena_prontas(im, lt)
        elif i <= 6:
            k = i - 2
            if k not in clips:
                fim = CORTES[i + 1]
                clips[k] = ler_trecho(EPS[k][3], EPS[k][4], fim - CORTES[i])
            cena_ep(im, lt, k, clips[k])
        else:
            cena_cta(im, lt)
        legenda(im, t, gs)
        return im.convert("RGB")

    if so is not None:
        out = AQUI / f"previa_{so:05.1f}.png"
        frame(so).save(out); print(out); return

    out = AQUI / "convite_conjuntos.mp4"
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", str(AQUI / "audio" / "narracao.wav"),
           "-af", "apad", "-t", str(DUR),
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for n in range(int(DUR * FPS)):
        p.stdin.write(frame(n / FPS).tobytes())
        if n % 150 == 0:
            print(f"{n / FPS:.0f}s", flush=True)
    p.stdin.close(); p.wait()
    print(out)


if __name__ == "__main__":
    main()
