"""Short de engajamento (não é aula): "Quantos quadrados tem?" em 3 níveis. Vertical 1080x1920, 30 fps.
Narração gravada pelo usuário a partir de roteiro.md (audio/voz_original.wav): as animações seguem escritas na linha do
tempo do roteiro e são deformadas para a voz (ANCORAS); a legenda usa os tempos reais das palavras (audio/palavras.json).
Visual = o mesmo dos vídeos de questões / aulas de matemática (_ferramentas/matematica.py), adaptado ao vertical:
selo no canto, título âmbar pequeno no alto (header), figura com traço neon, quadro translúcido com as contas e as
opções, faixa de legenda escura embaixo. Cores com função: âmbar = 1x1 / dado, ciano = 2x2, menta = 3x3 e certo,
coral = erro.
Nível 1: grade 3x4 → 12 + 6 + 2 = 20 (C) · atalho: 4×3 + 3×2 + 2×1
Nível 2: grade 4x4 → 16 + 9 + 4 + 1 = 30 (B) · Chefão: tabuleiro 8x8 → 64 + 49 + ... + 1 = 204 (D)
Uso: python3 render_short.py [--stills t1,t2,...]"""
import os, sys, subprocess
from pathlib import Path

os.environ["VIDEO_FORMATO"] = "vertical"          # antes de importar o motor
HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
from matematica import *  # noqa
from motor import W, H, FPS

# ---------------------------------------------------------------- linha do tempo (s) = a do roteiro.md
FALAS = [
    (0.0, 3.0, "Quantos quadrados tem aqui? A maioria erra."),
    (3.0, 7.5, "12, 17, 20 ou 24? Comenta a sua antes de ver!"),
    (7.5, 12.5, "Pausa e conta. Valendo!"),
    (12.5, 15.5, "Quem disse 12 contou só os pequenos."),
    (15.5, 20.0, "Mas tem quadrado de 2×2. Olha: 6 deles."),
    (20.0, 23.5, "E de 3×3, mais 2."),
    (23.5, 27.0, "12 + 6 + 2 = 20. Letra C!"),
    (27.0, 33.0, "Tem atalho: 4×3, mais 3×2, mais 2×1. 20!"),
    (33.0, 35.5, "Nível 2: e numa grade 4×4?"),
    (35.5, 39.0, "16, 30, 25 ou 36?"),
    (39.0, 42.0, "3 segundos!"),
    (42.0, 47.6, "16 pequenos, 9 de 2×2, 4 de 3×3 e 1 grandão."),
    (47.6, 50.0, "30! Letra B."),
    (50.0, 52.5, "Nível chefão: tabuleiro de xadrez!"),
    (52.5, 56.0, "64, 100, 128 ou 204?"),
    (56.0, 59.0, "Valendo!"),
    (59.0, 64.0, "Soma os quadrados de 8 até 1: 204! Letra D."),
    (64.0, 69.0, "Quantos você acertou: 0, 1, 2 ou 3? Comenta! No próximo: quantos triângulos?"),
]
DUR_ROTEIRO = 69.0

# ---------------------------------------------------------------- sincronia com a narração gravada (audio/voz_original.wav)
# A voz veio mais rápida que o roteiro e sem as pausas de contagem: abrimos silêncio depois de "Valendo!" / "3 segundos!"
# (GAPS, no tempo do áudio original) e a linha do tempo do roteiro é deformada por âncoras (roteiro -> áudio original).
VOZ = HERE / "audio" / "voz_original.wav"
NARRACAO = HERE / "audio" / "narracao.wav"
GAPS = [(10.80, 3.0), (39.60, 1.5), (55.55, 2.0)]           # (posição no áudio original, segundos de silêncio)
ANCORAS = [(0.0, 0.0), (3.0, 3.74), (7.5, 8.94), (12.5, 11.28), (15.5, 13.82), (20.0, 17.60), (23.5, 20.56),
           (27.0, 25.30), (33.0, 31.76), (35.5, 35.10), (39.0, 38.62), (42.0, 40.12), (47.6, 45.86), (50.0, 47.68),
           (52.5, 50.70), (56.0, 54.88), (59.0, 55.84), (62.6, 57.80), (64.0, 60.10), (69.0, 68.50)]


def com_gaps(x):
    """tempo no áudio original -> tempo no áudio com os silêncios inseridos"""
    return x + sum(d for g, d in GAPS if x >= g)


_A = [(r, com_gaps(a)) for r, a in ANCORAS]
DUR = _A[-1][1]


def roteiro_t(t):
    """tempo real do vídeo -> tempo da linha do tempo do roteiro (todas as animações continuam escritas nela)"""
    for (r0, a0), (r1, a1) in zip(_A, _A[1:]):
        if t < a1 or (r1, a1) == _A[-1]:
            return r0 + (t - a0) * (r1 - r0) / (a1 - a0)


# palavras ditas (transcrição de audio/palavras.json, já corrigida e escrita como na tela), tempo do áudio original
def _palavras():
    import json
    ws = json.load(open(HERE / "audio" / "palavras.json", encoding="utf-8"))[0]["words"]
    fix = {13.82: "Mas", 17.60: "E", 32.92: "e", 40.64: "pequenos,", 44.68: "e", 49.60: "de", 49.84: "xadrez!", 8.28: "ver!", 10.16: "Valendo!",
           16.04: "Olha:", 23.58: "20.", 24.38: "C!", 25.62: "atalho:", 30.84: "20!", 32.18: "2:", 32.92: "e", 40.64: "pequenos,", 48.06: "chefão:",
           54.88: "Valendo!", 57.48: "1:", 57.70: "204!", 63.74: "Comenta!", 64.68: "próximo:", 65.50: "quantos",
           65.82: "triângulos?", 60.98: "acertou:", 3.74: "12,", 35.10: "16,", 35.78: "30,", 50.70: "64,", 51.80: "100,",
           38.94: "segundos!", 21.12: "+", 21.62: "6", 22.30: "+", 22.58: "2", 23.24: "= 20.", 19.22: "mais"}
    out = []
    for w in ws:
        txt = fix.get(w["s"], w["w"])
        if w["s"] == 49.60:          # "de chá 3." = "de xadrez!" (erro do reconhecimento)
            continue
        out.append([txt, w["s"], w["e"]])
    # "4 vezes 3" / "2 por 2" -> "4×3" / "2×2" (uma palavra só na legenda)
    i = 0
    while i < len(out) - 2:
        if out[i + 1][0] in ("por", "vezes") and out[i][0].isdigit():
            out[i] = [out[i][0] + "×" + out[i + 2][0], out[i][1], out[i + 2][2]]
            del out[i + 1:i + 3]
        i += 1
    i = 0
    while i < len(out) - 1:                              # "+ 6" numa palavra só: a conta cabe num bloco
        if out[i][0] == "+":
            out[i] = ["+ " + out[i + 1][0], out[i][1], out[i + 1][2]]
            del out[i + 1]
        i += 1
    pont = {17.98: "3×3,", 26.42: "4×3,", 28.00: "3×2,", 33.74: "4×4?", 42.14: "2×2,", 43.80: "3×3", 45.86: "30!"}
    for w in out:
        w[0] = pont.get(w[1], w[0])
        if w[0] == "Mais" and w[1] > 27:                # atalho: "mais" minúsculo no meio da conta
            w[0] = "mais"
    return [(w[0], com_gaps(w[1]), com_gaps(w[2])) for w in out]


PALAVRAS = _palavras()
DESTAQUE = {"quadrados": AMB, "erra.": RED, "12": AMB, "12,": AMB, "6": CYA, "6.": CYA, "2": MNT, "2.": MNT, "20.": MNT,
            "20!": MNT, "C!": MNT, "2×2.": CYA, "3×3,": MNT, "4×3,": AMB, "3×2,": CYA, "2×1.": MNT, "atalho:": AMB,
            "4×4?": AMB, "16": AMB, "9": CYA, "4": MNT, "1": WHITE, "30!": MNT, "B.": MNT, "chefão:": RED,
            "204!": MNT, "D.": MNT, "triângulos?": CYA, "Comenta!": CYA, "= 20.": MNT, "+ 6": CYA, "+ 2": MNT, "2×2,": CYA, "3×3": MNT,
            "4×4?": AMB, "xadrez!": AMB, "2×2.": CYA, "6": CYA, "2×1.": MNT}

QX0, QX1, QY0, QY1 = 70, W - 70, 965, 1445          # quadro
QCX = W / 2
CAP_Y_V = 1540
AREA = (300, 870)                                    # faixa vertical da figura

# níveis: grade, opções, certa e tempos (gancho, opções, contagem, revelação, total, fim)
N1 = dict(cols=4, rows=3, cel=190, opc=[("A", "12"), ("B", "17"), ("C", "20"), ("D", "24")], certa="C",
          t_hook=0.0, t_opc=3.0, t_conta=7.5, dur_conta=5, t_rev=12.5, t_tot=23.5, t_fim=33.0, header="DESAFIO")
N2 = dict(cols=4, rows=4, cel=140, opc=[("A", "16"), ("B", "30"), ("C", "25"), ("D", "36")], certa="B",
          t_hook=33.0, t_opc=35.5, t_conta=39.0, dur_conta=3, t_rev=42.0, t_tot=47.6, t_fim=50.0, header="NÍVEL 2")
N3 = dict(cols=8, rows=8, cel=70, opc=[("A", "64"), ("B", "100"), ("C", "128"), ("D", "204")], certa="D",
          t_hook=50.0, t_opc=52.5, t_conta=56.0, dur_conta=3, t_rev=59.0, t_tot=62.6, t_fim=64.0, header="NÍVEL CHEFÃO",
          xadrez=True)
T_ATALHO, T_CTA = 27.0, 64.0
for N in (N1, N2, N3):
    N["x0"] = (W - N["cols"] * N["cel"]) / 2
    N["y0"] = AREA[0] + (AREA[1] - AREA[0] - N["rows"] * N["cel"]) / 2
CORES = {1: AMB, 2: CYA, 3: MNT, 4: WHITE}


# ---------------------------------------------------------------- peças no estilo das questões, em pé
def header_v(c, s, a):
    if a > 0:
        text_mid(c, s, W / 2, 175, 40, "black", AMB, a, tracking=2)


def quadro(c, a):
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(QX0, QY0, QX1, QY1), 26, 26)
    c.drawRRect(r, paint(BG2, 0.55 * a))
    c.drawRRect(r, paint(CYA, 0.18 * a, stroke=2))


def neon(c, x0, y0, x1, y1, col, a, w=8, glow=0.5):
    c.drawLine(x0, y0, x1, y1, blur_paint(col, glow * a, 10, stroke=w + 4))
    c.drawLine(x0, y0, x1, y1, paint(col, a, stroke=w, cap_round=True))


def grade(c, N, t, a=1.0):
    """figura no estilo das questões: traço neon colorido (ciano) com brilho e preenchimento bem leve"""
    if a <= 0:
        return
    u = ep(t, N["t_hook"] + 0.15, 0.9)
    X0, Y0, cel, cols, rows = N["x0"], N["y0"], N["cel"], N["cols"], N["rows"]
    if N.get("xadrez"):     # tabuleiro: casas "escuras" em ciano translúcido, borda neon
        for j in range(rows):
            for i in range(cols):
                ak = ep(t, N["t_hook"] + 0.1 + 0.025 * (i + j), 0.2) * a
                if (i + j) % 2 == 1 and ak > 0:
                    c.drawRect(skia.Rect.MakeXYWH(X0 + i * cel, Y0 + j * cel, cel, cel), paint(CYA, 0.30 * ak))
        r = skia.Rect.MakeXYWH(X0, Y0, cols * cel, rows * cel)
        c.drawRect(r, paint(CYA, 0.05 * a))
        c.drawRect(r, blur_paint(CYA, 0.5 * a * u, 10, stroke=14))
        c.drawRect(r, paint(CYA, a * u, stroke=8))
        return
    c.drawRect(skia.Rect.MakeXYWH(X0, Y0, cols * cel * u, rows * cel), paint(CYA, 0.07 * a))
    for k in range(cols + 1):
        x = X0 + k * cel
        neon(c, x, Y0, x, Y0 + rows * cel * u, CYA, a, 8, 0.5)
    for k in range(rows + 1):
        y = Y0 + k * cel
        neon(c, X0, y, X0 + cols * cel * u, y, CYA, a, 8, 0.5)


def quadrado(c, N, i, j, n, col, a, inset=10, width=10, fill=0.16):
    if a <= 0:
        return
    cel = N["cel"]
    rect = skia.Rect.MakeXYWH(N["x0"] + i * cel + inset, N["y0"] + j * cel + inset, n * cel - 2 * inset, n * cel - 2 * inset)
    r = skia.RRect.MakeRectXY(rect, 12, 12)
    c.drawRRect(r, paint(col, fill * a))
    c.drawRRect(r, blur_paint(col, 0.55 * a, 14, stroke=width + 6))
    c.drawRRect(r, paint(col, a, stroke=width))


def badge(c, s, cx, cy, a, bg=AMB, fg=None, r=30):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(bg, a))
    text_mid(c, s, cx, cy, r * 1.05, "black", fg or BG0, a)


def _blocos():
    """legenda em blocos de até 4 palavras: quebra na pontuação ou numa pausa da voz; cada palavra no tempo em que é dita"""
    blocos, cur = [], []
    for k, (w_, s0, e0) in enumerate(PALAVRAS):
        cur.append(k)
        prox = PALAVRAS[k + 1][1] if k + 1 < len(PALAVRAS) else DUR
        if len(cur) >= 4 or (w_[-1] in ".!?:," and len(cur) >= 2) or prox - e0 > 0.45 or w_[-1] in "!?":
            blocos.append(cur); cur = []
    if cur:
        blocos.append(cur)
    out = []
    for n, b in enumerate(blocos):
        ini = PALAVRAS[b[0]][1] - 0.08
        fim = PALAVRAS[b[-1]][2] + 0.7
        if n + 1 < len(blocos):
            fim = min(fim, PALAVRAS[blocos[n + 1][0]][1] - 0.08)
        out.append((ini, fim, b))
    return out


BLOCOS = _blocos()


def legenda(c, t):
    """faixa escura curta (estilo matematica.CAPTION): a palavra que está sendo dita em âmbar (tempos reais da voz)"""
    for s0, e, ch in BLOCOS:
        if s0 <= t < e:
            break
    else:
        return
    size, sp = 54, 15
    ws = [PALAVRAS[k][0] for k in ch]
    tot = sum(text_w(w_, "extrabold", size) for w_ in ws) + sp * (len(ws) - 1)
    k_ = ease_out(clamp((t - s0) / 0.14)) * (1 - prog(t, e - 0.12, 0.12))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(W / 2 - tot / 2 - 28, CAP_Y_V - size * 0.9, tot + 56, size * 1.8), 18, 18)
    c.drawRRect(r, paint(BG0, 0.72 * k_))
    x = W / 2 - tot / 2
    f = font("extrabold", size)
    for k, w_ in zip(ch, ws):
        falando = PALAVRAS[k][1] - 0.05 <= t < PALAVRAS[k][2] + 0.05
        col = AMB if falando else (CYA if w_ in DESTAQUE else WHITE)
        c.drawString(w_, x, CAP_Y_V + size * 0.36, f, paint(col, k_))
        x += text_w(w_, "extrabold", size) + sp


# ---------------------------------------------------------------- blocos comuns aos níveis
def opcoes(c, N, t, y0=1300, t_out=None):
    ok = ep(t, N["t_tot"] + 0.9, 0.4)
    for k, (L, v) in enumerate(N["opc"]):
        a = ep(t, N["t_opc"] + 0.25 * k, 0.3) * (1 - prog(t, (t_out or N["t_fim"]) - 0.3, 0.3))
        if a <= 0:
            continue
        x = QX0 + 120 + (k % 2) * 460
        y = y0 + (k // 2) * 96 + (1 - ease_back(clamp(prog(t, N["t_opc"] + 0.25 * k, 0.4)))) * 20
        certo = L == N["certa"]
        dim = 1 - 0.55 * ok * (not certo)
        if certo and ok > 0:
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 46, y - 42, 340, 84), 18, 18)
            c.drawRRect(r, blur_paint(MNT, 0.3 * ok, 22))
            c.drawRRect(r, paint(BG1, 0.95 * ok))
            c.drawRRect(r, paint(MNT, ok, stroke=4))
        badge(c, L, x, y, a * dim, MNT if (certo and ok > 0.5) else AMB, r=28)
        text(c, v, x + 50, y + 23, 64, "black", MNT if (certo and ok > 0.5) else WHITE, a * dim, align="left")
        if ok > 0 and not certo:
            strike(c, x + 44, x + 50 + text_w(v, "black", 64) + 6, y, a, ok)
        if certo and ok > 0:
            check(c, x + 250, y, 24, ok)


def contagem(c, N, t):
    t0, d = N["t_conta"], N["dur_conta"]
    if not (t0 - 0.1 <= t < t0 + d + 0.3):
        return
    a = ep(t, t0, 0.3) * (1 - prog(t, t0 + d - 0.1, 0.3))
    u = clamp((t - t0) / d)
    n = max(1, d - int(t - t0))
    cx, cy, r = QCX, QY0 + 140, 80
    c.drawCircle(cx, cy, r, paint(INK2, 0.2 * a, stroke=12))
    arc = skia.Path(); arc.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, 360 * (1 - u))
    c.drawPath(arc, blur_paint(AMB, 0.5 * a, 10, stroke=16))
    c.drawPath(arc, paint(AMB, a, stroke=12, cap_round=True))
    k = 1 + 0.3 * (1 - ease_out(clamp(((t - t0) % 1.0) / 0.25)))
    text_mid(c, str(n), cx, cy, 80 * k, "black", WHITE, a)


def placar(c, linhas, t, t_out, y0=QY0 + 66, dy=68):
    """linhas: (rótulo, total, cor, t0, passo) — badge âmbar, tamanho, contador que corre, ✓ ao completar"""
    a_all = 1 - prog(t, t_out, 0.3)
    for k, (nome, tot, col, t0, passo) in enumerate(linhas):
        a = ep(t, t0, 0.25) * a_all
        if a <= 0:
            continue
        y = y0 + k * dy
        badge(c, str(k + 1), QX0 + 90, y, a, r=26)
        text_mid(c, nome, QX0 + 136, y, 46, "black", col, a, align="left")
        n = min(tot, int(max(0.0, t - t0) / passo) + 1)
        text_mid(c, "→", QX0 + 320, y, 42, "black", INK2, a)
        text_mid(c, str(n), QX0 + 400, y, 54, "black", WHITE if n < tot else col, a)
        tf = t0 + passo * tot
        if t >= tf:
            check(c, QX1 - 90, y, 24, ep(t, tf, 0.3) * a_all)


def gancho(c, N, t, partes, sub=None):
    a = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3))
    if a <= 0:
        return
    eq(c, partes, QY0 + 95, a, size=64, cx=QCX, maxw=880)
    if sub:
        label(c, sub, QCX, QY0 + 175, ep(t, N["t_hook"] + 0.5, 0.3) * (1 - prog(t, N["t_opc"] + 1.0, 0.3)), 34, INK2)


# ---------------------------------------------------------------- nível 1 (grade 3x4)
Q2 = [(i, j) for j in range(N1["rows"] - 1) for i in range(N1["cols"] - 1)]
Q3 = [(i, j) for j in range(N1["rows"] - 2) for i in range(N1["cols"] - 2)]
T_1, T_2, T_3 = 12.5, 15.5, 20.0


def nivel1(c, t):
    N = N1
    if t >= N["t_fim"] + 0.3:
        return
    ga = 1 - prog(t, N["t_fim"] - 0.3, 0.3)
    grade(c, N, t, ga)
    if T_1 <= t < N["t_tot"] + 0.4:      # 1x1: as 12 casas acendem uma a uma
        out = 1 - prog(t, N["t_tot"], 0.4)
        for k in range(12):
            i, j = k % 4, k // 4
            a = ep(t, T_1 + 0.15 + 0.17 * k, 0.18)
            if a > 0:
                quadrado(c, N, i, j, 1, AMB, a * (1 - 0.7 * prog(t, T_2, 0.3)) * out, inset=14, width=6, fill=0.18)
                if t < T_2:
                    text_mid(c, str(k + 1), N["x0"] + (i + 0.5) * 190, N["y0"] + (j + 0.5) * 190, 58, "black", AMB, a)
    if T_2 <= t < T_3:                    # 2x2: um de cada vez
        for k, (i, j) in enumerate(Q2):
            t0 = T_2 + 0.15 + 0.62 * k
            fim = T_3 - 0.2 if k == len(Q2) - 1 else t0 + 0.55
            a = ep(t, t0, 0.15) * (1 - prog(t, fim, 0.15))
            if a > 0:
                quadrado(c, N, i, j, 2, CYA, a, inset=12, width=10)
                badge(c, str(k + 1), N["x0"] + (i + 1) * 190, N["y0"] + (j + 1) * 190, a, CYA, r=34)
    if T_3 <= t < N["t_tot"]:             # 3x3: os dois
        for k, (i, j) in enumerate(Q3):
            t0 = T_3 + 0.2 + 1.1 * k
            fim = N["t_tot"] - 0.2 if k == len(Q3) - 1 else t0 + 1.0
            a = ep(t, t0, 0.2) * (1 - prog(t, fim, 0.15))
            if a > 0:
                quadrado(c, N, i, j, 3, MNT, a, inset=12, width=12)
                badge(c, str(k + 1), N["x0"] + (i + 1.5) * 190, N["y0"] + (j + 1.5) * 190, a, MNT, r=38)
    gancho(c, N, t, [("Quantos ", WHITE), ("quadrados", AMB), (" tem?", WHITE)], "conte todos os tamanhos")
    k = pop(t, 1.3, 0.4) * (1 - prog(t, N["t_conta"] - 0.2, 0.3))
    if k > 0:
        c.save(); c.translate(QX1 - 170, QY0 + 2); c.rotate(-5); c.scale(k, k)
        pill(c, "A MAIORIA ERRA", 0, 0, 30, RED, WHITE, 1)
        c.restore()
    label(c, "comenta a sua antes de ver ↓", QCX, QY0 + 175, ep(t, N["t_opc"] + 1.4, 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3)),
          34, CYA, "black")
    contagem(c, N, t)
    placar(c, [("1×1", 12, AMB, T_1 + 0.15, 0.17), ("2×2", 6, CYA, T_2 + 0.15, 0.62), ("3×3", 2, MNT, T_3 + 0.2, 1.1)],
           t, N["t_tot"] - 0.2)
    a = ep(t, N["t_tot"], 0.3) * (1 - prog(t, T_ATALHO, 0.3))
    if a > 0:
        eq(c, [("12", AMB), (" + ", WHITE), ("6", CYA), (" + ", WHITE), ("2", MNT), (" = ", WHITE), ("20", MNT)],
           QY0 + 120, a, size=96, cx=QCX, box=MNT if t > N["t_tot"] + 1.2 else None, maxw=860)
    opcoes(c, N, t, t_out=T_ATALHO)
    # atalho: cada tamanho = (colunas que cabem) × (linhas que cabem)
    a = ep(t, T_ATALHO, 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if a > 0:
        label(c, "cada tamanho: colunas × linhas que cabem", QCX, QY0 + 60, a, 32, INK2)
        termos = [("4×3", AMB, "12"), ("3×2", CYA, "6"), ("2×1", MNT, "2")]
        for k, (s, col, v) in enumerate(termos):
            ak = ep(t, T_ATALHO + 0.4 + 1.2 * k, 0.3) * a
            if ak > 0:
                y = QY0 + 145 + k * 82
                badge(c, f"{k + 1}", QX0 + 110, y, ak, r=26)
                text_mid(c, f"{k + 1}×{k + 1}", QX0 + 160, y, 44, "black", col, ak, align="left")
                text_mid(c, "→", QX0 + 330, y, 42, "black", INK2, ak)
                text_mid(c, s, QX0 + 390, y, 56, "black", WHITE, ak, align="left")
                text_mid(c, "= " + v, QX0 + 560, y, 56, "black", col, ak, align="left")
                # na figura: um quadrado daquele tamanho no canto, como amostra
                quadrado(c, N, 0, 0, k + 1, col, ak * 0.9, inset=8 + 4 * k, width=8)
        eq(c, [("12 + 6 + 2 = ", WHITE), ("20", MNT)], QY0 + 410, ep(t, T_ATALHO + 4.2, 0.3) * a, size=64, cx=QCX,
           box=MNT)


# ---------------------------------------------------------------- nível 2 (grade 4x4)
def nivel2(c, t):
    N = N2
    if not (N["t_hook"] - 0.1 <= t < N["t_fim"] + 0.3):
        return
    ga = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    grade(c, N, t, ga)
    tr = N["t_rev"]
    passos = [(1, 16, 0.08), (2, 9, 0.15), (3, 4, 0.33), (4, 1, 1.0)]       # tamanho, quantos, passo (s)
    for k, (n, tot, passo) in enumerate(passos):
        t0, t1 = tr + 1.4 * k, tr + 1.4 * (k + 1)
        if not (t0 <= t < t1 + 0.1):
            continue
        lado = 4 - n + 1
        for q in range(tot):
            i, j = q % lado, q // lado
            tq = t0 + passo * q
            if n == 1:
                a = ep(t, tq, 0.12) * (1 - prog(t, t1 - 0.1, 0.15))
            else:
                a = ep(t, tq, 0.08) * (1 - prog(t, tq + passo * (0.9 if q < tot - 1 else 1.3), 0.08))
            quadrado(c, N, i, j, n, CORES[n], a, inset=8 + 2 * n, width=6 + 2 * n, fill=0.18 if n == 1 else 0.14)
    gancho(c, N, t, [("E numa grade ", WHITE), ("4×4", AMB), ("?", WHITE)], "mesma pergunta, grade maior")
    contagem(c, N, t)
    placar(c, [("1×1", 16, AMB, tr, 0.08), ("2×2", 9, CYA, tr + 1.4, 0.15), ("3×3", 4, MNT, tr + 2.8, 0.33),
               ("4×4", 1, WHITE, tr + 4.2, 1.0)], t, N["t_tot"] - 0.2, y0=QY0 + 58, dy=60)
    a = ep(t, N["t_tot"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if a > 0:
        eq(c, [("16", AMB), (" + ", WHITE), ("9", CYA), (" + ", WHITE), ("4", MNT), (" + ", WHITE), ("1", WHITE),
               (" = ", WHITE), ("30", MNT)], QY0 + 130, a, size=86, cx=QCX, box=MNT, maxw=880)
    opcoes(c, N, t)


# ---------------------------------------------------------------- chefão (tabuleiro 8x8)
def nivel3(c, t):
    N = N3
    if not (N["t_hook"] - 0.1 <= t < N["t_fim"] + 0.3):
        return
    ga = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    grade(c, N, t, ga)
    tr = N["t_rev"]
    termos = [(8 - k) ** 2 for k in range(8)]                       # 64, 49, ..., 1
    # na figura: um quadrado de cada tamanho, do maior ao menor, no canto, enquanto a soma cresce
    for k in range(8):
        n = 8 - k
        tk = tr + 0.4 * k
        a = ep(t, tk, 0.12) * (1 - prog(t, tk + 0.38, 0.1) if k < 7 else 1) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
        col = [AMB, CYA, MNT][k % 3]
        quadrado(c, N, 0, 0, n, col, a, inset=4, width=8, fill=0.25)
        if a > 0:
            pill(c, f"{n}×{n}", N["x0"] + n * 35, N["y0"] + n * 35, 22 + 3 * n, col, BG0, a)
    gancho(c, N, t, [("Tabuleiro de ", WHITE), ("xadrez", AMB), ("!", WHITE)], "8 × 8 casas")
    k = pop(t, N["t_hook"] + 0.5, 0.4) * (1 - prog(t, N["t_conta"] - 0.2, 0.3))
    if k > 0:
        c.save(); c.translate(QX1 - 150, QY0 + 2); c.rotate(-5); c.scale(k, k)
        pill(c, "NÍVEL DIFÍCIL", 0, 0, 30, RED, WHITE, 1)
        c.restore()
    contagem(c, N, t)
    # a soma cresce termo a termo (cores alternadas), depois o total
    out = 1 - prog(t, N["t_fim"] - 0.3, 0.3)
    n_on = sum(1 for k in range(8) if t >= tr + 0.4 * k)
    if n_on and t >= tr:
        partes = []
        for k in range(n_on):
            partes += [(str(termos[k]), [AMB, CYA, MNT][k % 3])] + ([(" + ", WHITE)] if k < n_on - 1 else [])
        eq(c, partes, QY0 + 75, out, size=54, cx=QCX, maxw=900)
        soma = sum(termos[:n_on])
        label(c, f"= {soma}", QCX, QY0 + 170, out * (1 - ep(t, N["t_tot"], 0.2)), 54, WHITE, "black")
    a = ep(t, N["t_tot"], 0.3) * out
    if a > 0:
        eq(c, [("= ", WHITE), ("204", MNT)], QY0 + 190, a, size=84, cx=QCX, box=MNT)
    opcoes(c, N, t)


# ---------------------------------------------------------------- final
def cta(c, t):
    a = ep(t, T_CTA, 0.35)
    if a <= 0:
        return
    eq(c, [("Quantos você ", WHITE), ("acertou", AMB), ("?", WHITE)], QY0 - 520, a, size=72, cx=QCX, maxw=900)
    # placar 0 · 1 · 2 · 3 para comentar
    for k in range(4):
        ak = ep(t, T_CTA + 0.4 + 0.2 * k, 0.3)
        x = QCX + (k - 1.5) * 200
        if ak > 0:
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 80, QY0 - 420, 160, 160), 28, 28)
            col = [RED, AMB, CYA, MNT][k]
            c.drawRRect(r, blur_paint(col, 0.3 * ak, 18))
            c.drawRRect(r, paint(BG1, 0.95 * ak))
            c.drawRRect(r, paint(col, ak, stroke=5))
            text_mid(c, str(k), x, QY0 - 340, 96, "black", col, ak)
    ab = ep(t, T_CTA + 1.4, 0.3)
    if ab > 0:
        y = QY0 + 110
        w1 = text_w("comenta o seu número", "black", 54)
        text_mid(c, "comenta o seu número", QCX - 40, y, 54, "black", WHITE, ab)
        check(c, QCX + w1 / 2 + 10, y, 28, ab, CYA)
    label(c, "1x1 · 2x2 · 3x3 ... sempre conte todos os tamanhos", QCX, QY0 + 210, ep(t, T_CTA + 2.0, 0.3), 30, INK2)
    popill(c, "PRÓXIMO: QUANTOS TRIÂNGULOS?", QCX, QY0 + 340, 34, CYA, BG0, 1.0, t, T_CTA + 2.6)


HEADERS = [(0.0, "DESAFIO"), (7.5, "PAUSE E CONTE"), (T_1, "1 × 1"), (T_2, "2 × 2"), (T_3, "3 × 3"), (23.5, "TOTAL"),
           (T_ATALHO, "O ATALHO"), (N2["t_hook"], "NÍVEL 2"), (N2["t_conta"], "NÍVEL 2 · CONTE"),
           (N2["t_rev"], "NÍVEL 2 · RESPOSTA"), (N3["t_hook"], "NÍVEL CHEFÃO"), (N3["t_conta"], "CHEFÃO · CONTE"),
           (N3["t_rev"], "CHEFÃO · RESPOSTA"), (T_CTA, "E AÍ?")]


def frame(c, t_real):
    t = roteiro_t(t_real)
    BACKGROUND(c, t_real)
    s_ = "QUESTÃO DE MATEMÁTICA · 002"          # selo do canto (o mesmo das questões), um pouco maior no celular
    pill(c, s_, 52 + (text_w(s_, "extrabold", 24) + 29) / 2, 80, 24, AMB, BG0, 0.95, "extrabold")
    for k, (t0, s) in enumerate(HEADERS):
        t1 = HEADERS[k + 1][0] if k + 1 < len(HEADERS) else DUR_ROTEIRO + 1
        if t0 <= t < t1:
            header_v(c, s, ep(t, t0, 0.25) * (1 - prog(t, t1 - 0.2, 0.2)))
    quadro(c, ep(t, 0.1, 0.4))
    nivel1(c, t)
    nivel2(c, t)
    nivel3(c, t)
    cta(c, t)
    legenda(c, t_real)


def narracao():
    """voz gravada + os silêncios de contagem (GAPS), 48 kHz, volume de Short (-14 LUFS), cauda de silêncio até DUR"""
    partes, ini, filt = [], 0.0, []
    for k, (g, d) in enumerate(GAPS + [(None, 0)]):
        fim = f":end={g}" if g is not None else ""
        filt.append(f"[0:a]atrim=start={ini}{fim},asetpts=PTS-STARTPTS[v{k}]")
        partes.append(f"[v{k}]")
        if d:
            filt.append(f"anullsrc=r=24000:cl=mono,atrim=duration={d}[s{k}]")
            partes.append(f"[s{k}]")
        ini = g
    filt.append("".join(partes) + f"concat=n={len(partes)}:v=0:a=1,loudnorm=I=-14:TP=-1.5:LRA=11,"
                f"aresample=48000,apad=whole_dur={DUR}[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(VOZ), "-filter_complex", ";".join(filt), "-map", "[a]",
                    "-ac", "1", str(NARRACAO)], check=True)


def render_frame(t):
    surf = skia.Surface(W, H)
    frame(surf.getCanvas(), t)
    return surf


if __name__ == "__main__":
    out = HERE / "final"
    out.mkdir(exist_ok=True)
    if "--stills" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--stills") + 1].split(",")]
        d = HERE / "trabalho" / "stills"; d.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*.png"):
            f.unlink()
        for t in ts:
            render_frame(t).makeImageSnapshot().save(str(d / f"t{t:06.2f}.png"), skia.kPNG)
        print("ok", d)
        sys.exit()
    narracao()
    mudo = HERE / "trabalho" / "video_mudo.mp4"
    mudo.parent.mkdir(exist_ok=True)
    # Surface.makeImageSnapshot().tobytes() sai em BGRA neste skia (vermelho puro = 0,0,255,255)
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                           "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(mudo)], stdin=subprocess.PIPE)
    for f in range(int(DUR * FPS)):
        ff.stdin.write(render_frame(f / FPS).makeImageSnapshot().tobytes())
    ff.stdin.close(); ff.wait()
    dst = out / "estudativo_short_002_quantos_quadrados.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mudo), "-i", str(NARRACAO), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart",
                    str(dst)], check=True)
    print(dst)
