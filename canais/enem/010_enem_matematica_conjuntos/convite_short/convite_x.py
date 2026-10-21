# Convite HORIZONTAL (1920x1080) para o X: mesmo vídeo do convite.py (narração, cortes, legenda e trechos das aulas),
# com layout 16:9 em duas colunas. Saída: convite_conjuntos_horizontal.mp4
# Uso: python convite_x.py [t]  -> sem t renderiza o vídeo; com t salva um quadro de prévia.
import importlib.util, math, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw

AQUI = Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location("convite_v", AQUI / "convite.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)

W, H, FPS = 1920, 1080, V.FPS
V.W, V.H = W, H           # os ajudantes do vertical (camada, cola, texto_c, cartao...) passam a usar o quadro 16:9
fonte, ease, pop, camada, cola, cartao, pilula = V.fonte, V.ease, V.pop, V.camada, V.cola, V.cartao, V.pilula
TINTA, CINZA, BRANCO, BG = V.TINTA, V.CINZA, V.BRANCO, V.BG
AZUL, LARANJA, VERDE, VERMELHO, ROXO = V.AZUL, V.LARANJA, V.VERDE, V.VERMELHO, V.ROXO
EPS, CORTES, DUR = V.EPS, V.CORTES, V.DUR

# trechos das aulas: mesma área do vídeo original, maior no quadro horizontal
CLIP_W = 1040
CLIP_H = round(V.CROP[3] * CLIP_W / V.CROP[2])
V.CLIP_W, V.CLIP_H = CLIP_W, CLIP_H
MASC = Image.new("L", (CLIP_W, CLIP_H), 0)
ImageDraw.Draw(MASC).rounded_rectangle((0, 0, CLIP_W - 1, CLIP_H - 1), 30, fill=255)


def texto_x(d, cx, y, partes, tam, peso="black", maxw=800, alpha=255):
    """texto centralizado em cx (coluna), reduzindo a fonte se passar de maxw"""
    f = fonte(tam, peso)
    larg = sum(d.textlength(t, font=f) for t, _ in partes)
    if larg > maxw:
        tam = int(tam * maxw / larg); f = fonte(tam, peso)
        larg = sum(d.textlength(t, font=f) for t, _ in partes)
    x = cx - larg / 2
    for t, c in partes:
        d.text((x, y), t, font=f, fill=c + (alpha,))
        x += d.textlength(t, font=f)


def fundo():
    im = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(im)
    for (cx, cy, r, c) in ((-60, 1060, 380, AZUL), (1980, 60, 360, LARANJA)):
        d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=c + (38,), width=32)
    return im


def selo(lay):
    pilula(ImageDraw.Draw(lay), 230, 52, "MATEMÁTICA ENEM", 30, BRANCO, AZUL)


# ---------------- cenas ----------------
def cena_gancho(base, t):
    lay = camada(); selo(lay); cola(base, lay, 1)
    linhas = ((250, [("Matemática no ", TINTA), ("ENEM", AZUL)], 120),
              (420, [("te dá um ", TINTA), ("frio na barriga?", LARANJA)], 104))
    for i, (y, partes, tam) in enumerate(linhas):
        a = ease((t - 0.5 * i) / 0.45)
        lay = camada(); texto_x(ImageDraw.Draw(lay), W // 2, y, partes, tam, maxw=1700)
        cola(base, lay, a, 30 * (1 - a))
    a = ease((t - 2.6) / 0.4)
    lay = camada(); pilula(ImageDraw.Draw(lay), W // 2, 640, "Então presta atenção", 48, TINTA)
    cola(base, lay, a, 20 * (1 - a))


def cena_prontas(base, t):
    lay = camada(); selo(lay); cola(base, lay, 1)
    cx = 520
    a = ease(t / 0.5)
    lay = camada(); texto_x(ImageDraw.Draw(lay), cx, 210, [("As aulas estão", TINTA)], 84); cola(base, lay, a, 30 * (1 - a))
    s = pop((t - 0.4) / 0.5)
    if s > 0:
        st = Image.new("RGBA", (760, 190), (0, 0, 0, 0)); d = ImageDraw.Draw(st)
        d.rounded_rectangle((0, 0, 759, 189), 40, fill=VERDE + (255,))
        f = fonte(120, "black"); lw = d.textlength("PRONTAS!", font=f)
        d.text(((760 - lw) / 2, 22), "PRONTAS!", font=f, fill=BRANCO + (255,))
        st = st.rotate(-4, expand=True, resample=Image.BICUBIC)
        st = st.resize((max(1, int(st.width * s)), max(1, int(st.height * s))), Image.LANCZOS)
        base.alpha_composite(st, (cx - st.width // 2, 440 - st.height // 2))
    a = ease((t - 1.0) / 0.5)
    lay = camada(); cartao(lay, (1000, 170, 1820, 520), 40)
    d = ImageDraw.Draw(lay)
    texto_x(d, 1410, 215, [("SÉRIE", CINZA)], 36, "extrabold")
    texto_x(d, 1410, 280, [("Operações e", AZUL)], 80, maxw=740)
    texto_x(d, 1410, 385, [("Conjuntos Numéricos", AZUL)], 80, maxw=740)
    cola(base, lay, a, 40 * (1 - a))
    lay = camada(); d = ImageDraw.Draw(lay)
    for i, (n, _, cor, _, _) in enumerate(EPS):
        a = ease((t - 3.6 - 0.15 * i) / 0.35)
        if a <= 0:
            continue
        ccx = 1410 + (i - 2) * 150; cy = 640 + 20 * (1 - a)
        r = 56 * (0.6 + 0.4 * a)
        d.ellipse((ccx - r, cy - r, ccx + r, cy + r), fill=cor + (int(255 * a),))
        f = fonte(58, "black"); lw = d.textlength(str(n), font=f)
        d.text((ccx - lw / 2, cy - 36), str(n), font=f, fill=BRANCO + (int(255 * a),))
    base.alpha_composite(lay)
    a = ease((t - 4.4) / 0.5)
    lay = camada(); texto_x(ImageDraw.Draw(lay), 1410, 720, [("5 episódios · do zero", TINTA)], 54, "extrabold")
    cola(base, lay, a, 20 * (1 - a))


def cena_ep(base, t, k, frames):
    n, (l1, l2), cor, _, _ = EPS[k]
    lay = camada(); selo(lay); cola(base, lay, 1)
    cx = 400
    a = ease(t / 0.4)
    lay = camada(); d = ImageDraw.Draw(lay)
    pilula(d, cx, 230, f"EPISÓDIO {n}", 40, cor)
    texto_x(d, cx, 350, [(l1, TINTA)], 66, maxw=640)
    texto_x(d, cx, 440, [(l2, cor)], 66, maxw=640)
    cola(base, lay, a, 24 * (1 - a))
    # trilha dos 5 episódios, embaixo do título
    lay = camada(); d = ImageDraw.Draw(lay)
    for i, (m, _, c2, _, _) in enumerate(EPS):
        ccx, cy = cx + (i - 2) * 100, 640
        if m == n:
            r = 38 * pop(t / 0.4)
            d.ellipse((ccx - r, cy - r, ccx + r, cy + r), fill=c2 + (255,))
            f = fonte(42, "black"); lw = d.textlength(str(m), font=f)
            d.text((ccx - lw / 2, cy - 27), str(m), font=f, fill=BRANCO + (255,))
        else:
            r = 26
            fill = c2 + (255,) if m < n else (210, 210, 205, 255)
            d.ellipse((ccx - r, cy - r, ccx + r, cy + r), fill=fill)
            f = fonte(28, "black"); lw = d.textlength(str(m), font=f)
            d.text((ccx - lw / 2, cy - 18), str(m), font=f, fill=BRANCO + (255,))
    base.alpha_composite(lay)
    # trecho da aula num cartão, à direita
    a = ease((t - 0.1) / 0.45)
    fr = frames[min(int(t * FPS), len(frames) - 1)]
    lay = camada()
    x0, y0 = 820, 170
    cartao(lay, (x0 - 14, y0 - 14, x0 + CLIP_W + 14, y0 + CLIP_H + 14), 40)
    lay.paste(fr, (x0, y0), MASC)
    cola(base, lay, a, 40 * (1 - a))


def cena_cta(base, t):
    lay = camada(); V.logo(lay, 480, 400, 560); a = ease(t / 0.5); cola(base, lay, a, 40 * (1 - a))
    # busca no YouTube
    a = ease((t - 0.3) / 0.4)
    lay = camada(); d = ImageDraw.Draw(lay)
    cartao(lay, (1000, 150, 1820, 260), 55)
    alvo = "Estudativo"
    nlet = int(max(0, min(1, (t - 0.6) / 0.8)) * len(alvo))
    f = fonte(54, "bold")
    d.text((1060, 172), alvo[:nlet], font=f, fill=TINTA + (255,))
    if int(t * 2) % 2 == 0:
        x = 1060 + d.textlength(alvo[:nlet], font=f) + 4
        d.rectangle((x, 175, x + 4, 235), fill=AZUL + (255,))
    d.ellipse((1720, 178, 1764, 222), outline=CINZA + (255,), width=7)
    d.line((1756, 214, 1780, 238), fill=CINZA + (255,), width=8)
    cola(base, lay, a, 20 * (1 - a))
    # playlist
    a = ease((t - 2.4) / 0.5)
    lay = camada(); d = ImageDraw.Draw(lay)
    cartao(lay, (1000, 300, 1820, 460), 36)
    d.rounded_rectangle((1030, 325, 1170, 435), 18, fill=AZUL + (255,))
    for i in range(3):
        d.rectangle((1058, 348 + i * 26, 1142, 358 + i * 26), fill=BRANCO + (255,))
    d.text((1200, 325), "PLAYLIST", font=fonte(30, "extrabold"), fill=CINZA + (255,))
    d.text((1200, 365), "Matemática ENEM do Zero", font=fonte(46, "black"), fill=TINTA + (255,))
    cola(base, lay, a, 30 * (1 - a))
    # inscreva-se + sininho
    s = pop((t - 4.9) / 0.5)
    lay = camada(); d = ImageDraw.Draw(lay)
    bw, bh = int(500 * s), int(120 * s)
    bx, by = 1330, 570
    if bw > 2:
        d.rounded_rectangle((bx - bw // 2, by - bh // 2, bx + bw // 2, by + bh // 2), bh // 2, fill=VERMELHO + (255,))
        f = fonte(max(8, int(54 * s)), "black"); lw = d.textlength("INSCREVA-SE", font=f)
        d.text((bx - lw / 2, by - 34 * s), "INSCREVA-SE", font=f, fill=BRANCO + (255,))
    base.alpha_composite(lay)
    a = ease((t - 5.6) / 0.4)
    if a > 0:
        sino = Image.new("RGBA", (150, 150), (0, 0, 0, 0)); d = ImageDraw.Draw(sino)
        d.ellipse((0, 0, 149, 149), fill=LARANJA + (255,))
        d.pieslice((37, 28, 113, 112), 180, 360, fill=BRANCO + (255,))
        d.rectangle((37, 70, 113, 98), fill=BRANCO + (255,))
        d.rounded_rectangle((28, 94, 122, 107), 6, fill=BRANCO + (255,))
        d.ellipse((64, 105, 86, 126), fill=BRANCO + (255,))
        ang = 18 * math.sin((t - 5.6) * 14) * max(0, 1 - (t - 5.6) / 1.6)
        sino = sino.rotate(ang, resample=Image.BICUBIC)
        sino.putalpha(sino.getchannel("A").point(lambda v: int(v * a)))
        base.alpha_composite(sino, (1690 - 75, by - 75))
    a = ease((t - 6.9) / 0.5)
    lay = camada(); texto_x(ImageDraw.Draw(lay), 1410, 690, [("Bons estudos!", AZUL)], 84)
    cola(base, lay, a, 24 * (1 - a))


# ---------------- legenda ----------------
def legenda(base, t, gs):
    atual = None
    for g in gs:
        if g[0]["s"] - 0.05 <= t <= g[-1]["e"] + 0.35:
            atual = g
    if not atual:
        return
    lay = camada(); d = ImageDraw.Draw(lay)
    f = fonte(56, "black")
    txt = " ".join(w["w"] for w in atual)
    lw = d.textlength(txt, font=f)
    if lw > W - 300:
        f = fonte(int(56 * (W - 300) / lw), "black"); lw = d.textlength(txt, font=f)
    y = 900
    d.rounded_rectangle(((W - lw) / 2 - 34, y - 16, (W + lw) / 2 + 34, y + 88), 30, fill=TINTA + (235,))
    x = (W - lw) / 2
    for w in atual:
        cor = LARANJA if w["s"] - 0.05 <= t else BRANCO
        d.text((x, y), w["w"], font=f, fill=cor + (255,))
        x += d.textlength(w["w"] + " ", font=f)
    base.alpha_composite(lay)


def main():
    so = float(sys.argv[1]) if len(sys.argv) > 1 else None
    gs = V.grupos(V.palavras(), maxc=34)
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
                clips[k] = V.ler_trecho(EPS[k][3], EPS[k][4], CORTES[i + 1] - CORTES[i])
            cena_ep(im, lt, k, clips[k])
        else:
            cena_cta(im, lt)
        legenda(im, t, gs)
        return im.convert("RGB")

    if so is not None:
        out = AQUI / f"previa_x_{so:05.1f}.png"
        frame(so).save(out); print(out); return

    out = AQUI / "convite_conjuntos_horizontal.mp4"
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", str(AQUI / "audio" / "narracao.wav"),
           "-af", "apad", "-t", str(DUR),
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for n in range(int(DUR * FPS)):
        p.stdin.write(frame(n / FPS).tobytes())
        if n % 300 == 0:
            print(f"{n / FPS:.0f}s", flush=True)
    p.stdin.close(); p.wait()
    print(out)


if __name__ == "__main__":
    main()
