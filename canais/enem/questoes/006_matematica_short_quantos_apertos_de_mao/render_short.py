"""Short de engajamento (não é aula): "Quantos apertos de mão?" em 3 níveis. Vertical 1080x1920, 30 fps.
Mesmo formato dos Shorts 002–005: visual das questões de matemática (_ferramentas/matematica.py) em pé.
Amigos numa roda; cada um aperta a mão de todos os outros, uma vez. Um aperto = uma linha entre duas pessoas.
Cores com função: âmbar = 1º / contagem por pessoa, ciano = 2º, menta = 3º / certo, coral = erro.
Nível 1: 4 amigos → 3 + 2 + 1 = 6 (C) · o segredo: 4 × 3 = 12 conta cada aperto 2 vezes (2 mãos) → 12 ÷ 2 = 6
Nível 2: 5 amigos → 5 × 4 = 20, ÷ 2 = 10 (A) · as linhas formam a estrela
Chefão: 10 amigos → 10 × 9 = 90, ÷ 2 = 45 (D) · pegadinhas: 90 (sem dividir), 100 (10 × 10), 55 (conta a si mesmo)
As contagens foram conferidas por força bruta em conferir_contagens.py.

Sem a voz: sai final/..._sem_audio.mp4 na linha do tempo do roteiro.md.
Com a voz em audio/voz_original.wav + audio/palavras.json: preencher GAPS/ANCORAS/CORRIGE (como no Short 005) e rodar de
novo: as animações são deformadas para a voz e a legenda usa os tempos reais das palavras.
Uso: python3 render_short.py [--stills t1,t2,...]"""
import json
import os
import subprocess
import sys
from math import cos, sin, pi
from pathlib import Path

os.environ["VIDEO_FORMATO"] = "vertical"          # antes de importar o motor
HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
from matematica import *  # noqa
from motor import W, H, FPS

# ---------------------------------------------------------------- linha do tempo (s) = a do roteiro.md
FALAS = [
    (0.0, 4.0, "4 amigos. Todo mundo aperta a mão de todo mundo, uma vez."),
    (4.0, 7.5, "Quantos apertos de mão? 8, 12, 6 ou 4?"),
    (7.5, 9.5, "Comenta antes de ver!"),
    (9.5, 14.5, "Pausa e conta. Valendo!"),
    (14.5, 17.0, "O primeiro aperta a mão de 3."),
    (17.0, 19.0, "O segundo, de mais 2."),
    (19.0, 21.0, "O terceiro, de mais 1."),
    (21.0, 23.0, "E o quarto já apertou todas!"),
    (23.0, 26.0, "3 + 2 + 1 = 6. Letra C!"),
    (26.0, 30.5, "Quem disse 12 fez 4 vezes 3. Mas cada aperto tem 2 mãos!"),
    (30.5, 33.5, "Contou tudo 2 vezes: 12 dividido por 2, 6."),
    (33.5, 36.0, "Nível 2: e com 5 amigos?"),
    (36.0, 39.5, "10, 20, 15 ou 25?"),
    (39.5, 42.5, "3 segundos!"),
    (42.5, 46.5, "Cada um aperta 4: 5 vezes 4, 20."),
    (46.5, 49.5, "Dividido por 2: 10! Letra A."),
    (49.5, 52.0, "Nível chefão: 10 amigos!"),
    (52.0, 56.0, "90, 100, 55 ou 45?"),
    (56.0, 59.0, "Valendo!"),
    (59.0, 63.0, "10 vezes 9, 90. Dividido por 2..."),
    (63.0, 66.0, "45! Letra D. O 90 conta tudo 2 vezes!"),
    (66.0, 71.0, "Quantos você acertou: 0, 1, 2 ou 3? Comenta! No próximo: quantas diagonais?"),
]
DUR_ROTEIRO = 71.0
DESTAQUE = {"4": AMB, "amigos.": AMB, "mão": AMB, "uma": AMB, "vez.": AMB, "C!": MNT, "6.": MNT, "12": RED, "2": CYA,
            "mãos!": CYA, "vezes:": CYA, "amigos?": AMB, "10!": MNT, "A.": MNT, "chefão:": RED, "45!": MNT, "D.": MNT,
            "Comenta!": CYA, "diagonais?": CYA, "amigos!": AMB, "apertos": AMB, "= 6.": MNT, "45!": MNT}

# ---------------------------------------------------------------- sincronia com a narração gravada (quando chegar)
VOZ = HERE / "audio" / "voz_original.wav"
NARRACAO = HERE / "audio" / "narracao.wav"
# a voz veio no ritmo de Short: silêncio aberto depois de "Valendo!", depois do "6" do segredo (respira antes do nível 2),
# de "3 segundos!" e do 2º "Valendo!"
GAPS = [(12.00, 3.2), (31.40, 0.6), (39.30, 1.4), (53.10, 2.2)]   # (posição no áudio original, segundos de silêncio)
ANCORAS = [(0.0, 0.0), (4.0, 4.14), (7.5, 8.72), (9.5, 10.08), (14.5, 12.36), (17.0, 14.40), (19.0, 16.22), (21.0, 17.72),
           (23.0, 19.66), (23.9, 21.80), (26.0, 23.00), (28.6, 25.70), (29.5, 26.66), (30.5, 29.20), (33.5, 31.84),
           (36.0, 34.60), (39.5, 38.08), (42.5, 39.96), (45.2, 41.36), (45.8, 42.42), (46.5, 42.98), (47.4, 44.76), (49.5, 45.97),
           (52.0, 48.64), (56.0, 52.24), (59.0, 53.51), (61.3, 54.54), (62.0, 55.18), (63.0, 56.22), (63.9, 56.98),
           (64.4, 58.26), (66.0, 60.72), (68.6, 65.30), (71.0, 67.60)]   # (tempo do roteiro, tempo no áudio original)
CORRIGE = {0.00: "4", 3.34: "uma", 4.42: "apertos", 8.72: "Comenta antes", 9.40: "ver!", 11.24: "Valendo!", 14.58: "segundo,",
           16.34: "terceiro,", 18.88: "todas!", 21.14: "= 6.", 22.16: "C!", 26.98: "mãos!", 28.52: "vezes:", 32.18: "2:", 38.38: "segundos!",
           33.34: "5", 33.74: "amigos?", 40.74: "4:", 44.12: "10!", 46.38: "chefão:", 47.50: "10", 47.88: "amigos!",
           51.22: "45?", 52.24: "Valendo!", 56.22: "45!", 59.88: "vezes!", 64.52: "Comenta!", 65.48: "próximo:",
           66.24: "quantas"}                   # {início da palavra: texto}
INICIO = {31.62: 31.84, 39.68: 39.96, 45.88: 45.97, 53.42: 53.51}   # palavra que a transcrição começou cedo: {início: início real}
SOMA = {19.96, 20.46}                      # "mais" das contas: vira "+ 2" junto com o número seguinte
COM_VOZ = VOZ.exists() and (HERE / "audio" / "palavras.json").exists() and len(ANCORAS) > 2


def com_gaps(x):
    return x + sum(d for g, d in GAPS if x >= g)


_A = [(r, com_gaps(a)) for r, a in ANCORAS]
DUR = _A[-1][1]


def roteiro_t(t):
    """tempo real do vídeo -> tempo da linha do tempo do roteiro (as animações são escritas nela)"""
    for (r0, a0), (r1, a1) in zip(_A, _A[1:]):
        if t < a1 or (r1, a1) == _A[-1]:
            return r0 + (t - a0) * (r1 - r0) / (a1 - a0)


def _palavras():
    """[(texto, início, fim)] no tempo real. Sem voz: ritmo de Short a partir do início de cada fala."""
    if not COM_VOZ:
        out = []
        for t0, t1, s in FALAS:
            ws = s.split()
            passo = min(0.36, (t1 - t0 - 0.3) / len(ws))
            out += [(w, t0 + 0.1 + passo * k, t0 + 0.1 + passo * (k + 1)) for k, w in enumerate(ws)]
        return out
    ws = json.load(open(HERE / "audio" / "palavras.json", encoding="utf-8"))[0]["words"]
    out = [[CORRIGE.get(w["s"], w["w"]), INICIO.get(w["s"], w["s"]), w["e"]] for w in ws if CORRIGE.get(w["s"], w["w"]) != ""]
    i = 0
    while i < len(out) - 1:
        if out[i][1] in SOMA:
            out[i] = ["+ " + out[i + 1][0].rstrip(","), out[i][1], out[i + 1][2]]
            del out[i + 1]
        i += 1
    return [(w, com_gaps(s), com_gaps(e)) for w, s, e in out]


PALAVRAS = _palavras()

QX0, QX1, QY0, QY1 = 70, W - 70, 965, 1445          # quadro
QCX = W / 2
CAP_Y_V = 1540

# níveis: opções, certa e tempos (gancho, opções, contagem, revelação, total, fim)
N1 = dict(opc=[("A", "8"), ("B", "12"), ("C", "6"), ("D", "4")], certa="C",
          t_hook=0.0, t_opc=4.0, t_conta=9.5, dur_conta=5, t_rev=14.5, t_tot=23.0, t_fim=33.5)
N2 = dict(opc=[("A", "10"), ("B", "20"), ("C", "15"), ("D", "25")], certa="A",
          t_hook=33.5, t_opc=36.0, t_conta=39.5, dur_conta=3, t_rev=42.5, t_tot=46.5, t_fim=49.5)
N3 = dict(opc=[("A", "90"), ("B", "100"), ("C", "55"), ("D", "45")], certa="D",
          t_hook=49.5, t_opc=52.0, t_conta=56.0, dur_conta=3, t_rev=59.0, t_tot=63.0, t_fim=66.0)
T_P = [14.5, 17.0, 19.0, 21.0]                         # nível 1: a vez do 1º, 2º, 3º e 4º
T_SEG, T_MAOS, T_DIV, T_CTA = 26.0, 28.6, 30.5, 66.0   # o segredo: 4 × 3, as 2 mãos, ÷ 2

# ---------------------------------------------------------------- geometria (px): a roda de amigos
R1 = dict(n=4, cx=540.0, cy=600.0, R=240.0, r=52, a0=-135)
R2 = dict(n=5, cx=540.0, cy=610.0, R=255.0, r=46, a0=-90)
R3 = dict(n=10, cx=540.0, cy=590.0, R=265.0, r=34, a0=-90)


def pos(G, k):
    a = (G["a0"] + 360 * k / G["n"]) * pi / 180
    return G["cx"] + G["R"] * cos(a), G["cy"] + G["R"] * sin(a)


def pares(G):
    """todos os apertos (i, j), i < j, na ordem: os do 1º, depois os novos do 2º..."""
    return [(i, j) for i in range(G["n"]) for j in range(i + 1, G["n"])]


assert [len(pares(G)) for G in (R1, R2, R3)] == [6, 10, 45]


def header_v(c, s, a):
    if a > 0:
        text_mid(c, s, W / 2, 175, 40, "black", AMB, a, tracking=2)


def quadro(c, a):
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(QX0, QY0, QX1, QY1), 26, 26)
    c.drawRRect(r, paint(BG2, 0.55 * a))
    c.drawRRect(r, paint(CYA, 0.18 * a, stroke=2))


def neon(c, p, q, col, a, w=8, glow=0.5, u=1.0):
    if a <= 0 or u <= 0:
        return
    x1, y1 = p[0] + (q[0] - p[0]) * u, p[1] + (q[1] - p[1]) * u
    c.drawLine(p[0], p[1], x1, y1, blur_paint(col, glow * a, 10, stroke=w + 4))
    c.drawLine(p[0], p[1], x1, y1, paint(col, a, stroke=w, cap_round=True))


def badge(c, s, cx, cy, a, bg=AMB, fg=None, r=30):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(bg, a))
    text_mid(c, s, cx, cy, r * 1.05, "black", fg or BG0, a)


def _blocos():
    """legenda em blocos de até 4 palavras: quebra na pontuação ou numa pausa da voz"""
    blocos, cur = [], []
    for k, (w_, s0, e0) in enumerate(PALAVRAS):
        cur.append(k)
        prox = PALAVRAS[k + 1][1] if k + 1 < len(PALAVRAS) else DUR
        if k + 1 < len(PALAVRAS) and PALAVRAS[k + 1][0][:1] in "+=":       # a conta fica inteira num bloco
            continue
        if len(cur) >= 4 or (w_[-1] in ":," and len(cur) >= 2) or prox - e0 > 0.45 or w_[-1] in ".!?":
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
    """faixa escura curta (estilo matematica.CAPTION): a palavra que está sendo dita em âmbar"""
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


def placar(c, linhas, t, t_out, y0=QY0 + 66, dy=68, x_seta=320):
    """linhas: (rótulo, total, cor, t0, passo) — badge âmbar, rótulo, contador que corre, ✓ ao completar"""
    a_all = 1 - prog(t, t_out, 0.3)
    for k, (nome, tot, col, t0, passo) in enumerate(linhas):
        a = ep(t, t0, 0.25) * a_all
        if a <= 0:
            continue
        y = y0 + k * dy
        badge(c, str(k + 1), QX0 + 90, y, a, r=26)
        text_mid(c, nome, QX0 + 136, y, 46, "black", col, a, align="left")
        n = min(tot, int(max(0.0, t - t0) / passo) + 1)
        text_mid(c, "→", QX0 + x_seta, y, 42, "black", INK2, a)
        text_mid(c, str(n), QX0 + x_seta + 80, y, 54, "black", WHITE if n < tot else col, a)
        if t >= t0 + passo * tot:
            check(c, QX1 - 90, y, 24, ep(t, t0 + passo * tot, 0.3) * a_all)


def gancho(c, N, t, partes, sub=None):
    a = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3))
    if a <= 0:
        return
    eq(c, partes, QY0 + 95, a, size=64, cx=QCX, maxw=880)
    if sub:
        label(c, sub, QCX, QY0 + 175, ep(t, N["t_hook"] + 0.5, 0.3) * (1 - prog(t, N["t_opc"] + 1.0, 0.3)), 34, INK2)


def selo_torto(c, s, t, t0, t_out, x):
    k = pop(t, t0, 0.4) * (1 - prog(t, t_out, 0.3))
    if k > 0:
        c.save(); c.translate(x, QY0 + 2); c.rotate(-5); c.scale(k, k)
        pill(c, s, 0, 0, 30, RED, WHITE, 1)
        c.restore()



def pessoa(c, G, k, a, col=CYA, glow=0.0, num=True):
    """um amigo: bolinha com o bonequinho (cabeça + ombros) e o número dele por fora da roda"""
    if a <= 0:
        return
    x, y = pos(G, k)
    r = G["r"]
    if glow > 0:
        c.drawCircle(x, y, r + 14, blur_paint(col, 0.6 * glow * a, 18))
    c.drawCircle(x, y, r, paint(BG1, a))
    c.drawCircle(x, y, r, paint(col, a, stroke=5))
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x - r, y - r, 2 * r, 2 * r))
    c.drawCircle(x, y - 0.22 * r, 0.27 * r, paint(col, a))
    c.drawOval(skia.Rect.MakeXYWH(x - 0.55 * r, y + 0.16 * r, 1.1 * r, 0.9 * r), paint(col, a))
    c.restore()
    c.drawCircle(x, y, r, paint(BG0, 0.0))
    if num:
        dx, dy = x - G["cx"], y - G["cy"]
        n = (dx * dx + dy * dy) ** 0.5
        badge(c, str(k + 1), x + dx / n * (r + 26), y + dy / n * (r + 26), a, col, r=22)


def roda(c, G, a, cores=None, glows=None, num=True):
    for k in range(G["n"]):
        pessoa(c, G, k, a, (cores or {}).get(k, CYA), (glows or {}).get(k, 0.0), num)


def aperto(c, G, i, j, col, a, u=1.0, w=8, glow=0.6):
    """a linha do aperto, de borda a borda das bolinhas, desenhada de i para j até a fração u"""
    if a <= 0 or u <= 0:
        return
    (x0, y0), (x1, y1) = pos(G, i), pos(G, j)
    dx, dy = x1 - x0, y1 - y0
    n = (dx * dx + dy * dy) ** 0.5
    e = G["r"] + 4
    p, q = (x0 + dx / n * e, y0 + dy / n * e), (x1 - dx / n * e, y1 - dy / n * e)
    neon(c, p, q, col, a, w, glow, u)


def mao(c, G, i, j, s, col, a):
    """selo na ponta do aperto, do lado de i (quem está contando)"""
    if a <= 0:
        return
    (x0, y0), (x1, y1) = pos(G, i), pos(G, j)
    dx, dy = x1 - x0, y1 - y0
    n = (dx * dx + dy * dy) ** 0.5
    e = G["r"] + 40
    badge(c, s, x0 + dx / n * e, y0 + dy / n * e, a, col, r=26)


def vez_de_cada(c, G, t, t0, passo, fim, col=AMB, w=6):
    """cada pessoa, na sua vez, acende os apertos dela (com todos os outros). Devolve quantas já contaram."""
    feitas = 0
    for k in range(G["n"]):
        tk = t0 + passo * k
        if t < tk:
            break
        feitas = k + 1
        a = ep(t, tk, 0.08) * (1 - prog(t, fim if k == G["n"] - 1 else tk + passo * 0.92, 0.08))
        for j in range(G["n"]):
            if j != k:
                aperto(c, G, k, j, col, a, ep(t, tk, passo * 0.5), w, 0.5)
    return feitas


def conta_vez(c, n, por, y, a, size=84):
    """no quadro: n × (n − 1) com o total que corre"""
    eq(c, [(str(n), AMB), (" × ", WHITE), (str(por), CYA), (" = ", WHITE), (str(n * por), WHITE)], y, a, size=size, cx=QCX, maxw=880)


def divide(c, tot, y, a, box, size=84):
    eq(c, [(str(tot), WHITE), (" ÷ ", WHITE), ("2", CYA), (" = ", WHITE), (str(tot // 2), MNT)], y, a, size=size, cx=QCX,
       box=MNT if box else None, maxw=880)


# ---------------------------------------------------------------- nível 1 (4 amigos)
def nivel1(c, t):
    N, G = N1, R1
    if t >= N["t_fim"] + 0.3:
        return
    ga = ep(t, 0.2, 0.4) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    cor_vez = [AMB, CYA, MNT]
    # a vez de cada um: o 1º aperta 3, o 2º mais 2, o 3º mais 1, o 4º nenhum novo
    seg = ep(t, T_SEG, 0.3)
    if N["t_rev"] <= t < N["t_fim"]:
        k = 0
        for i in range(3):
            for j in range(i + 1, 4):
                tk = T_P[i] + 0.3 + (0.5 if i == 0 else 0.6) * (j - i - 1)
                a = ep(t, tk, 0.2) * (1 - 0.75 * seg) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
                aperto(c, G, i, j, cor_vez[i] if t < N["t_tot"] + 0.6 else MNT, a, ep(t, tk, 0.35), 9, 0.7)
                k += 1
    # o segredo: cada um conta os seus 3 (4 × 3 = 12)... e o aperto 1–2 aparece nas duas contas
    if T_SEG <= t < T_MAOS:
        vez_de_cada(c, G, t, T_SEG + 0.3, 0.55, T_MAOS - 0.1, AMB, 7)
    am = ep(t, T_MAOS, 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if am > 0:
        aperto(c, G, 0, 1, AMB, am, 1.0, 12, 0.9)
        mao(c, G, 0, 1, "+1", AMB, ep(t, T_MAOS + 0.3, 0.2) * am)
        mao(c, G, 1, 0, "+1", CYA, ep(t, T_MAOS + 0.9, 0.2) * am)
    vez = next((i for i in range(4) if T_P[i] <= t < (T_P[i + 1] if i < 3 else N["t_tot"])), None)
    cores = {i: cor_vez[i] for i in range(3) if N["t_rev"] <= t < N["t_tot"] + 0.6 and t >= T_P[i]}
    glows = {vez: 1.0} if vez is not None else {}
    if T_MAOS <= t:
        cores, glows = {0: AMB, 1: CYA}, {0: am, 1: am}
    roda(c, G, ga, cores, glows)
    if vez == 3:
        label(c, "já apertou todas", pos(G, 3)[0] + 40, pos(G, 3)[1] + 95, ep(t, T_P[3] + 0.3, 0.3) * (1 - prog(t, N["t_tot"] - 0.2, 0.2)),
              32, MNT, "black")
    gancho(c, N, t, [("Quantos ", WHITE), ("apertos de mão", AMB), ("?", WHITE)], "cada um aperta a mão de todos, 1 vez")
    selo_torto(c, "PARECE FÁCIL", t, 1.3, N["t_conta"] - 0.2, QX1 - 160)
    label(c, "comenta antes de ver ↓", QCX, QY0 + 250, ep(t, 7.5, 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3)), 34, CYA, "black")
    contagem(c, N, t)
    placar(c, [("o 1º", 3, AMB, T_P[0] + 0.3, 0.5), ("o 2º", 2, CYA, T_P[1] + 0.3, 0.6), ("o 3º", 1, MNT, T_P[2] + 0.3, 0.6),
               ("o 4º", 0, WHITE, T_P[3] + 0.3, 0.5)], t, N["t_tot"] - 0.2, y0=QY0 + 58, dy=60, x_seta=440)
    a = ep(t, N["t_tot"], 0.3) * (1 - prog(t, T_SEG, 0.3))
    if a > 0:
        eq(c, [("3", AMB), (" + ", WHITE), ("2", CYA), (" + ", WHITE), ("1", MNT), (" = ", WHITE), ("6", MNT)], QY0 + 120, a,
           size=90, cx=QCX, box=MNT if t > N["t_tot"] + 1.2 else None, maxw=880)
    opcoes(c, N, t, t_out=T_SEG)
    # quadro do segredo
    a = ep(t, T_SEG, 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if a <= 0:
        return
    n = min(4, int(max(0.0, t - T_SEG - 0.3) / 0.55) + 1)
    label(c, "quem disse 12 fez:", QCX, QY0 + 55, a, 34, INK2)
    eq(c, [("4", AMB), (" × ", WHITE), ("3", CYA), (" = ", WHITE), ("12", RED if t >= T_MAOS else WHITE)], QY0 + 135, a, size=80,
       cx=QCX, maxw=880)
    if t < T_MAOS:
        label(c, f"{n} {'pessoa' if n == 1 else 'pessoas'} × 3 = {3 * n}", QCX, QY0 + 235, ep(t, T_SEG + 0.3, 0.2) * a, 40, AMB, "black")
    a2 = ep(t, T_MAOS + 0.6, 0.3) * a
    label(c, "cada aperto tem 2 mãos → contou 2 vezes", QCX, QY0 + 235, a2, 36, CYA, "black")
    divide(c, 12, QY0 + 355, ep(t, T_DIV, 0.3) * a, t > T_DIV + 1.2, 80)


# ---------------------------------------------------------------- nível 2 e chefão: n × (n − 1) ÷ 2
def nivel(c, t, N, G, hook, sub, selo=None, passo=0.6, num=True):
    if not (N["t_hook"] - 0.1 <= t < N["t_fim"] + 0.3):
        return
    ga = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    n = G["n"]
    tr, tt = N["t_rev"], N["t_tot"]
    feitas = 0
    if tr <= t < tt:                                      # cada um acende os seus n − 1
        feitas = vez_de_cada(c, G, t, tr + 0.3, passo, tt - 0.1, AMB, 5 if n > 5 else 7)
    if t >= tt - 0.2:                                     # dividido por 2: cada aperto uma vez só, desenhados em sequência
        ps = pares(G)
        d = min(0.12, 1.6 / len(ps))
        for q, (i, j) in enumerate(ps):
            tq = tt + d * q
            aperto(c, G, i, j, MNT, ep(t, tq, 0.15) * ga, ep(t, tq, 0.25), 5 if n > 5 else 8, 0.5)
    vez = feitas - 1 if tr <= t < tt and feitas else None
    roda(c, G, ga, {vez: AMB} if vez is not None else {}, {vez: 1.0} if vez is not None else {}, num)
    gancho(c, N, t, hook, sub)
    if selo:
        selo_torto(c, selo, t, N["t_hook"] + 0.5, N["t_conta"] - 0.2, QX1 - 150)
    contagem(c, N, t)
    a = ep(t, tr, 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if a > 0:
        label(c, f"cada um aperta {n - 1}", QCX, QY0 + 50, a, 34, INK2)
        k = max(1, feitas) if t < tt else n
        eq(c, [(str(k), AMB), (" × ", WHITE), (str(n - 1), CYA), (" = ", WHITE), (str(k * (n - 1)), WHITE)], QY0 + 125, a,
           size=80, cx=QCX, maxw=880)
        divide(c, n * (n - 1), QY0 + 225, ep(t, tt, 0.3) * a, t > tt + 0.9, 80)
    opcoes(c, N, t)


def nivel2(c, t):
    nivel(c, t, N2, R2, [("E com ", WHITE), ("5 amigos", AMB), ("?", WHITE)], "todo mundo com todo mundo, 1 vez", passo=0.6)


def nivel3(c, t):
    nivel(c, t, N3, R3, [("Agora ", WHITE), ("10 amigos", AMB), ("!", WHITE)], "todo mundo com todo mundo, 1 vez",
          "NÍVEL DIFÍCIL", passo=0.2, num=False)
    popill(c, "90 CONTA TUDO 2 VEZES", QCX, 930, 30, CYA, BG0, 1 - prog(t, N3["t_fim"] - 0.3, 0.3), t, N3["t_tot"] + 1.4)


# ---------------------------------------------------------------- final
def cta(c, t):
    a = ep(t, T_CTA, 0.35)
    if a <= 0:
        return
    eq(c, [("Quantos você ", WHITE), ("acertou", AMB), ("?", WHITE)], QY0 - 520, a, size=72, cx=QCX, maxw=900)
    for k in range(4):                         # placar 0 · 1 · 2 · 3 para comentar
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
    label(c, "n × (n − 1) ÷ 2: cada aperto tem 2 mãos", QCX, QY0 + 210, ep(t, T_CTA + 2.0, 0.3), 30, INK2)
    popill(c, "PRÓXIMO: QUANTAS DIAGONAIS?", QCX, QY0 + 340, 34, CYA, BG0, 1.0, t, T_CTA + 2.6)


HEADERS = [(0.0, "DESAFIO"), (N1["t_conta"], "PAUSE E CONTE"), (T_P[0], "O 1º"), (T_P[1], "O 2º"), (T_P[2], "O 3º"),
           (T_P[3], "O 4º"), (N1["t_tot"], "TOTAL"), (T_SEG, "O SEGREDO"), (N2["t_hook"], "NÍVEL 2"),
           (N2["t_conta"], "NÍVEL 2 · CONTE"), (N2["t_rev"], "NÍVEL 2 · RESPOSTA"), (N3["t_hook"], "NÍVEL CHEFÃO"),
           (N3["t_conta"], "CHEFÃO · CONTE"), (N3["t_rev"], "CHEFÃO · RESPOSTA"), (T_CTA, "E AÍ?")]


def frame(c, t_real):
    t = roteiro_t(t_real)
    BACKGROUND(c, t_real)
    s_ = "QUESTÃO DE MATEMÁTICA · 006"          # selo do canto (o mesmo das questões)
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
    """voz gravada + os silêncios de contagem (GAPS), 48 kHz, -14 LUFS, cauda de silêncio até DUR"""
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
    mudo = HERE / "trabalho" / "video_mudo.mp4"
    mudo.parent.mkdir(exist_ok=True)
    # Surface.makeImageSnapshot().tobytes() sai em BGRA neste skia (vermelho puro = 0,0,255,255)
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                           "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(mudo)], stdin=subprocess.PIPE)
    for f in range(int(DUR * FPS)):
        ff.stdin.write(render_frame(f / FPS).makeImageSnapshot().tobytes())
    ff.stdin.close(); ff.wait()
    if not COM_VOZ:
        dst = out / "estudativo_short_006_quantos_apertos_de_mao_sem_audio.mp4"
        subprocess.run(["cp", str(mudo), str(dst)], check=True)
        print(dst)
        sys.exit()
    narracao()
    dst = out / "estudativo_short_006_quantos_apertos_de_mao.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mudo), "-i", str(NARRACAO), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart",
                    str(dst)], check=True)
    print(dst)
