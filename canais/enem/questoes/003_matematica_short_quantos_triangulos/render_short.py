"""Short de engajamento (não é aula): "Quantos triângulos tem?" em 3 níveis. Vertical 1080x1920, 30 fps.
Mesmo formato do Short 002 (quantos quadrados): visual das questões de matemática (_ferramentas/matematica.py) em pé,
cores com função: âmbar = peça sozinha / pequeno, ciano = 2 peças / médio, menta = inteiro / grande e certo, coral = erro.
Nível 1: leque com a base em 3 pedaços → 3 + 2 + 1 = 6 (D) · atalho: soma os pedaços da base
Nível 2: leque com 4 pedaços + uma linha no meio → 2 andares × (4 + 3 + 2 + 1) = 20 (B)
Chefão: triângulo de 4 fileiras → 16 pequenos (10 em pé + 6 de ponta-cabeça) + 7 médios + 3 grandes + 1 = 27 (C)
As contagens foram conferidas por força bruta em conferir_contagens.py.

Sem a voz: sai final/..._sem_audio.mp4 na linha do tempo do roteiro.md (backup em trabalho/).
Com a voz em audio/voz_original.wav + audio/palavras.json: preencher GAPS/ANCORAS/CORRIGE (como no Short 002) e rodar de
novo: as animações são deformadas para a voz e a legenda usa os tempos reais das palavras.
Uso: python3 render_short.py [--stills t1,t2,...]"""
import json
import os
import subprocess
import sys
from pathlib import Path

os.environ["VIDEO_FORMATO"] = "vertical"          # antes de importar o motor
HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
from matematica import *  # noqa
from motor import W, H, FPS

# ---------------------------------------------------------------- linha do tempo (s) = a do roteiro.md
FALAS = [
    (0.0, 3.0, "Quantos triângulos tem aqui? Parece fácil."),
    (3.0, 7.5, "3, 4, 5 ou 6? Comenta a sua antes de ver!"),
    (7.5, 12.5, "Pausa e conta. Valendo!"),
    (12.5, 15.5, "Quem disse 3 contou só os pequenos."),
    (15.5, 19.0, "Juntando 2 vizinhos: mais 2."),
    (19.0, 21.5, "E o triângulo inteiro: mais 1."),
    (21.5, 24.5, "3 + 2 + 1 = 6. Letra D!"),
    (24.5, 30.0, "O atalho: soma os pedaços da base. 3 + 2 + 1. Com 4 pedaços: 10!"),
    (30.0, 33.0, "Nível 2: e com uma linha no meio?"),
    (33.0, 36.5, "10, 20, 16 ou 12?"),
    (36.5, 39.5, "3 segundos!"),
    (39.5, 45.0, "O andar de cima tem 10. Os inteiros, mais 10."),
    (45.0, 47.5, "20! Letra B."),
    (47.5, 50.0, "Nível chefão: triângulo de triângulos!"),
    (50.0, 53.5, "16, 20, 27 ou 24?"),
    (53.5, 56.5, "Valendo!"),
    (56.5, 61.0, "16 pequenos, 7 médios, 3 grandes e o gigante."),
    (61.0, 64.0, "27! Letra C."),
    (64.0, 69.0, "Quantos você acertou: 0, 1, 2 ou 3? Comenta! No próximo: quantos retângulos?"),
]
DUR_ROTEIRO = 69.0
DESTAQUE = {"triângulos": AMB, "fácil.": RED, "3": AMB, "2": CYA, "1": MNT, "1.": MNT, "= 6.": MNT, "+ 2,": CYA, "+ 1,": MNT, "+ 2": CYA, "+ 1.": MNT, "D!": MNT,
            "atalho:": AMB, "10!": CYA, "meio?": AMB, "10.": AMB, "20!": MNT, "B.": MNT, "chefão:": RED,
            "triângulos!": AMB, "pequenos,": AMB, "médios,": CYA, "grandes": MNT, "gigante.": WHITE, "27!": MNT,
            "C.": MNT, "retângulos?": CYA, "Comenta!": CYA}

# ---------------------------------------------------------------- sincronia com a narração gravada (quando chegar)
VOZ = HERE / "audio" / "voz_original.wav"
NARRACAO = HERE / "audio" / "narracao.wav"
# a voz veio sem as pausas de contagem: silêncio aberto depois de "Valendo!", "3 segundos!" e do 2º "Valendo!"
GAPS = [(8.45, 3.2), (30.80, 1.7), (43.00, 2.1)]          # (posição no áudio original, segundos de silêncio)
ANCORAS = [(0.0, 0.0), (3.0, 2.78), (7.5, 6.88), (12.5, 8.76), (15.5, 11.20), (19.0, 13.52), (21.5, 15.68),
           (24.5, 18.52), (30.0, 24.54), (33.0, 27.14), (36.5, 29.60), (39.5, 31.17), (42.3, 32.50), (45.0, 34.14),
           (47.5, 35.88), (50.0, 39.02), (53.5, 42.24), (56.5, 43.18), (58.5, 44.42), (60.0, 45.40), (61.0, 47.04),
           (64.0, 49.32), (69.0, 56.90)]                   # (tempo do roteiro, tempo no áudio original)
CORRIGE = {4.64: "6?", 6.40: "ver!", 7.74: "Valendo!", 10.42: "pequenos.", 11.20: "Juntando", 12.00: "vizinhos:",
           14.14: "inteiro:", 16.92: "= 6.", 17.78: "D!", 18.66: "atalho:", 22.80: "pedaços:", 23.56: "10!",
           24.92: "2:", 25.20: "e", 26.44: "meio?", 28.96: "12?", 29.88: "segundos!", 34.14: "20!", 36.26: "chefão:",
           38.08: "triângulos!", 41.48: "24?", 42.24: "Valendo!", 47.04: "27!", 49.80: "acertou:", 51.94: "3?",
           52.50: "Comenta!", 53.38: "próximo:", 53.76: "quantos", 54.34: "retângulos?"}   # {início da palavra: texto}
SOMA = {15.92, 16.46, 21.22, 21.64}       # "mais" das contas: vira "+ 2" junto com o número seguinte
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
    out = [[CORRIGE.get(w["s"], w["w"]), w["s"], w["e"]] for w in ws if CORRIGE.get(w["s"], w["w"]) != ""]
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
N1 = dict(opc=[("A", "3"), ("B", "4"), ("C", "5"), ("D", "6")], certa="D",
          t_hook=0.0, t_opc=3.0, t_conta=7.5, dur_conta=5, t_rev=12.5, t_tot=21.5, t_fim=30.0)
N2 = dict(opc=[("A", "10"), ("B", "20"), ("C", "16"), ("D", "12")], certa="B",
          t_hook=30.0, t_opc=33.0, t_conta=36.5, dur_conta=3, t_rev=39.5, t_tot=45.0, t_fim=47.5)
N3 = dict(opc=[("A", "16"), ("B", "20"), ("C", "27"), ("D", "24")], certa="C",
          t_hook=47.5, t_opc=50.0, t_conta=53.5, dur_conta=3, t_rev=56.5, t_tot=61.0, t_fim=64.0)
T_1, T_2, T_3 = 12.5, 15.5, 19.0          # nível 1: sozinhos, de 2 peças, inteiro
T_ATALHO, T_CTA = 24.5, 64.0

# ---------------------------------------------------------------- geometria (px)
AP = (540.0, 330.0)                          # vértice de cima dos leques
BASE_Y, BASE_X0, BASE_X1 = 845.0, 170.0, 910.0


def leque(m):
    return [(BASE_X0 + (BASE_X1 - BASE_X0) * k / m, BASE_Y) for k in range(m + 1)]


B1, B2 = leque(3), leque(4)
P2 = [(AP[0] + 0.5 * (x - AP[0]), AP[1] + 0.5 * (y - AP[1])) for x, y in B2]    # linha do meio do nível 2

G_N, G_LADO, G_TOPO = 4, 660.0, 312.0                                           # chefão: 4 fileiras
G_S, G_H = G_LADO / G_N, G_LADO / G_N * 0.8660254


def V(r, c):
    return (W / 2 + (c - r / 2) * G_S, G_TOPO + r * G_H)


SOBE = {k: [(V(r, c), V(r + k, c), V(r + k, c + k)) for r in range(G_N - k + 1) for c in range(r + 1)]
        for k in range(1, G_N + 1)}
DESCE = {k: [(V(r, c), V(r, c + k), V(r + k, c + k)) for r in range(G_N + 1) for c in range(r + 1)
             if c + k <= r and r + k <= G_N] for k in range(1, G_N + 1)}
assert [len(SOBE[k]) + len(DESCE[k]) for k in (1, 2, 3, 4)] == [16, 7, 3, 1]


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


def neon(c, p, q, col, a, w=8, glow=0.5, u=1.0):
    if a <= 0 or u <= 0:
        return
    x1, y1 = p[0] + (q[0] - p[0]) * u, p[1] + (q[1] - p[1]) * u
    c.drawLine(p[0], p[1], x1, y1, blur_paint(col, glow * a, 10, stroke=w + 4))
    c.drawLine(p[0], p[1], x1, y1, paint(col, a, stroke=w, cap_round=True))


def triang(c, pts, col, a, encolhe=14, width=9, fill=0.18):
    """um triângulo destacado: encolhido em direção ao centro (para não sumir sob as linhas), brilho + contorno"""
    if a <= 0:
        return
    cx, cy = sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3
    path = skia.Path()
    for k, (x, y) in enumerate(pts):
        d = max(1.0, ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5)
        f = max(0.3, 1 - encolhe * 1.8 / d)
        q = (cx + (x - cx) * f, cy + (y - cy) * f)
        (path.moveTo if k == 0 else path.lineTo)(*q)
    path.close()
    c.drawPath(path, paint(col, fill * a))
    pb = blur_paint(col, 0.55 * a, 14, stroke=width + 6); pb.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pb)
    pl = paint(col, a, stroke=width); pl.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pl)


def figura_leque(c, base, t, t0, a, meio=None):
    """leque: lados e linhas que saem do vértice de cima, base; opcional: linha do meio"""
    if a <= 0:
        return
    u = ep(t, t0 + 0.15, 0.9)
    path = skia.Path(); path.moveTo(*AP); path.lineTo(*base[0]); path.lineTo(*base[-1]); path.close()
    c.drawPath(path, paint(CYA, 0.07 * a))
    for b in base:
        neon(c, AP, b, CYA, a, 8, 0.5, u)
    neon(c, base[0], base[-1], CYA, a, 8, 0.5, u)
    if meio:
        neon(c, meio[0], meio[-1], CYA, a, 8, 0.5, ep(t, t0 + 0.6, 0.6))


def figura_grade(c, t, t0, a):
    if a <= 0:
        return
    u = ep(t, t0 + 0.15, 0.9)
    path = skia.Path(); path.moveTo(*V(0, 0)); path.lineTo(*V(G_N, 0)); path.lineTo(*V(G_N, G_N)); path.close()
    c.drawPath(path, paint(CYA, 0.07 * a))
    for r in range(1, G_N + 1):
        neon(c, V(r, 0), V(r, r), CYA, a, 7, 0.5, u)                        # horizontais
    for k in range(G_N):
        neon(c, V(k, 0), V(G_N, G_N - k), CYA, a, 7, 0.5, u)                 # paralelas ao lado direito
        neon(c, V(k, k), V(G_N, k), CYA, a, 7, 0.5, u)                       # paralelas ao lado esquerdo


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


def piscando(c, tris, t, t0, passo, col, fim, acumula=False, **kw):
    """destaca os triângulos um de cada vez (ou acumulando); o último fica até `fim`"""
    for q, pts in enumerate(tris):
        tq = t0 + passo * q
        if acumula:
            a = ep(t, tq, 0.12) * (1 - prog(t, fim, 0.2))
        else:
            a = ep(t, tq, 0.08) * (1 - prog(t, fim if q == len(tris) - 1 else tq + passo * 0.92, 0.08))
        triang(c, pts, col, a, **kw)


# ---------------------------------------------------------------- nível 1 (leque, base em 3 pedaços)
def nivel1(c, t):
    N = N1
    if t >= N["t_fim"] + 0.3:
        return
    ga = 1 - prog(t, N["t_fim"] - 0.3, 0.3)
    figura_leque(c, B1, t, N["t_hook"], ga)
    out = 1 - prog(t, N["t_tot"], 0.4)
    if T_1 <= t < N["t_tot"] + 0.4:            # sozinhos: acendem e ficam, numerados
        for k in range(3):
            a = ep(t, T_1 + 0.3 + 0.7 * k, 0.2) * (1 - 0.7 * prog(t, T_2, 0.3)) * out
            pts = (AP, B1[k], B1[k + 1])
            triang(c, pts, AMB, a, encolhe=16, width=7)
            if t < T_2 and a > 0:
                text_mid(c, str(k + 1), sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3 + 60, 64, "black", AMB, a)
    if T_2 <= t < T_3:                          # de 2 peças: um de cada vez
        for k in range(2):
            t0 = T_2 + 0.3 + 1.4 * k
            a = ep(t, t0, 0.15) * (1 - prog(t, T_3 - 0.2 if k == 1 else t0 + 1.3, 0.15))
            pts = (AP, B1[k], B1[k + 2])
            triang(c, pts, CYA, a, encolhe=12, width=10)
            badge(c, str(k + 1), sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3 + 70, a, CYA, r=34)
    if T_3 <= t < N["t_tot"]:                   # o inteiro
        a = ep(t, T_3 + 0.3, 0.2) * (1 - prog(t, N["t_tot"] - 0.2, 0.15))
        triang(c, (AP, B1[0], B1[3]), MNT, a, encolhe=10, width=12)
        badge(c, "1", AP[0], 700, a, MNT, r=38)
    gancho(c, N, t, [("Quantos ", WHITE), ("triângulos", AMB), (" tem?", WHITE)], "conte todos os tamanhos")
    selo_torto(c, "PARECE FÁCIL", t, 1.3, N["t_conta"] - 0.2, QX1 - 160)
    label(c, "comenta a sua antes de ver ↓", QCX, QY0 + 175, ep(t, N["t_opc"] + 1.4, 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3)),
          34, CYA, "black")
    contagem(c, N, t)
    placar(c, [("1 peça", 3, AMB, T_1 + 0.3, 0.7), ("2 peças", 2, CYA, T_2 + 0.3, 1.4), ("3 peças", 1, MNT, T_3 + 0.3, 1.0)],
           t, N["t_tot"] - 0.2, x_seta=370)
    a = ep(t, N["t_tot"], 0.3) * (1 - prog(t, T_ATALHO, 0.3))
    if a > 0:
        eq(c, [("3", AMB), (" + ", WHITE), ("2", CYA), (" + ", WHITE), ("1", MNT), (" = ", WHITE), ("6", MNT)],
           QY0 + 120, a, size=96, cx=QCX, box=MNT if t > N["t_tot"] + 1.2 else None, maxw=860)
    opcoes(c, N, t, t_out=T_ATALHO)
    # atalho: base com n pedaços → n + (n-1) + ... + 1
    a = ep(t, T_ATALHO, 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if a > 0:
        label(c, "soma os pedaços da base", QCX, QY0 + 60, a, 34, INK2)
        a1 = ep(t, T_ATALHO + 0.8, 0.3) * a
        badge(c, "3", QX0 + 110, QY0 + 165, a1, r=30)
        text_mid(c, "pedaços", QX0 + 160, QY0 + 165, 44, "black", AMB, a1, align="left")
        eq(c, [("3 + 2 + 1 = ", WHITE), ("6", MNT)], QY0 + 165, a1, size=56, cx=QX0 + 610, maxw=520)
        a2 = ep(t, T_ATALHO + 3.4, 0.3) * a
        badge(c, "4", QX0 + 110, QY0 + 275, a2, CYA, r=30)
        text_mid(c, "pedaços", QX0 + 160, QY0 + 275, 44, "black", CYA, a2, align="left")
        eq(c, [("4 + 3 + 2 + 1 = ", WHITE), ("10", CYA)], QY0 + 275, a2, size=56, cx=QX0 + 610, maxw=520)
        # na figura: os pedaços da base numerados
        for k in range(3):
            ak = ep(t, T_ATALHO + 0.8 + 0.3 * k, 0.2) * a
            x = (B1[k][0] + B1[k + 1][0]) / 2
            badge(c, str(k + 1), x, BASE_Y + 2, ak, AMB, r=24)


# ---------------------------------------------------------------- nível 2 (leque com 4 pedaços + linha no meio)
def nivel2(c, t):
    N = N2
    if not (N["t_hook"] - 0.1 <= t < N["t_fim"] + 0.3):
        return
    ga = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    figura_leque(c, B2, t, N["t_hook"], ga, meio=P2)
    tr = N["t_rev"]
    pares = [(i, j) for d in range(1, 5) for i in range(5 - d) for j in [i + d]]      # pequenos primeiro
    piscando(c, [(AP, P2[i], P2[j]) for i, j in pares], t, tr + 0.2, 0.25, AMB, tr + 2.75, encolhe=8, width=6)
    piscando(c, [(AP, B2[i], B2[j]) for i, j in pares], t, tr + 2.8, 0.22, CYA, N["t_tot"] - 0.2, encolhe=10, width=8)
    a = ep(t, tr + 0.2, 0.3) * (1 - prog(t, tr + 2.7, 0.2))                   # o "andar de cima" sombreado
    if a > 0:
        p = skia.Path(); p.moveTo(*AP); p.lineTo(*P2[0]); p.lineTo(*P2[-1]); p.close()
        c.drawPath(p, paint(AMB, 0.08 * a))
    gancho(c, N, t, [("E com uma ", WHITE), ("linha no meio", AMB), ("?", WHITE)], "base em 4 pedaços")
    contagem(c, N, t)
    placar(c, [("andar de cima", 10, AMB, tr + 0.2, 0.25), ("inteiros", 10, CYA, tr + 2.8, 0.22)], t, N["t_tot"] - 0.2,
           y0=QY0 + 80, dy=80, x_seta=530)
    a = ep(t, N["t_tot"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if a > 0:
        eq(c, [("10", AMB), (" + ", WHITE), ("10", CYA), (" = ", WHITE), ("20", MNT)], QY0 + 130, a, size=96, cx=QCX,
           box=MNT, maxw=880)
    opcoes(c, N, t)


# ---------------------------------------------------------------- chefão (triângulo de 4 fileiras)
def nivel3(c, t):
    N = N3
    if not (N["t_hook"] - 0.1 <= t < N["t_fim"] + 0.3):
        return
    ga = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    figura_grade(c, t, N["t_hook"], ga)
    tr = N["t_rev"]
    out = 1 - prog(t, N["t_fim"] - 0.3, 0.3)
    pequenos = SOBE[1] + DESCE[1]                                     # 10 em pé, depois 6 de ponta-cabeça
    piscando(c, pequenos, t, tr + 0.1, 0.1, AMB, tr + 1.9, acumula=True, encolhe=7, width=5, fill=0.22)
    piscando(c, SOBE[2] + DESCE[2], t, tr + 2.0, 0.2, CYA, tr + 3.45, encolhe=9, width=8)
    piscando(c, SOBE[3], t, tr + 3.5, 0.15, MNT, tr + 3.95, encolhe=10, width=9)
    triang(c, SOBE[4][0], WHITE, ep(t, tr + 4.0, 0.2) * (1 - prog(t, N["t_tot"] + 0.6, 0.3)) * out, encolhe=8, width=10, fill=0.1)
    gancho(c, N, t, [("Triângulo de ", WHITE), ("triângulos", AMB), ("!", WHITE)], "4 fileiras")
    selo_torto(c, "NÍVEL DIFÍCIL", t, N["t_hook"] + 0.5, N["t_conta"] - 0.2, QX1 - 150)
    contagem(c, N, t)
    placar(c, [("pequenos", 16, AMB, tr + 0.1, 0.1), ("médios", 7, CYA, tr + 2.0, 0.2), ("grandes", 3, MNT, tr + 3.5, 0.15),
               ("gigante", 1, WHITE, tr + 4.0, 0.5)], t, N["t_tot"] - 0.2, y0=QY0 + 58, dy=60, x_seta=440)
    a = ep(t, tr + 0.1, 0.2) * (1 - prog(t, tr + 1.95, 0.2))           # dica: os de ponta-cabeça também contam
    if a > 0 and t >= tr + 1.1:
        pill(c, "+ 6 DE PONTA-CABEÇA", QX0 + 330, QY0 + 125, 28, CYA, BG0, ep(t, tr + 1.1, 0.2) * a)
    a = ep(t, N["t_tot"], 0.3) * out
    if a > 0:
        eq(c, [("16", AMB), (" + ", WHITE), ("7", CYA), (" + ", WHITE), ("3", MNT), (" + ", WHITE), ("1", WHITE),
               (" = ", WHITE), ("27", MNT)], QY0 + 130, a, size=86, cx=QCX, box=MNT, maxw=880)
    opcoes(c, N, t)


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
    label(c, "sozinhos · juntos · de ponta-cabeça: conte todos", QCX, QY0 + 210, ep(t, T_CTA + 2.0, 0.3), 30, INK2)
    popill(c, "PRÓXIMO: QUANTOS RETÂNGULOS?", QCX, QY0 + 340, 34, CYA, BG0, 1.0, t, T_CTA + 2.6)


HEADERS = [(0.0, "DESAFIO"), (7.5, "PAUSE E CONTE"), (T_1, "1 PEÇA"), (T_2, "2 PEÇAS"), (T_3, "3 PEÇAS"), (21.5, "TOTAL"),
           (T_ATALHO, "O ATALHO"), (N2["t_hook"], "NÍVEL 2"), (N2["t_conta"], "NÍVEL 2 · CONTE"),
           (N2["t_rev"], "NÍVEL 2 · RESPOSTA"), (N3["t_hook"], "NÍVEL CHEFÃO"), (N3["t_conta"], "CHEFÃO · CONTE"),
           (N3["t_rev"], "CHEFÃO · RESPOSTA"), (T_CTA, "E AÍ?")]


def frame(c, t_real):
    t = roteiro_t(t_real)
    BACKGROUND(c, t_real)
    s_ = "QUESTÃO DE MATEMÁTICA · 003"          # selo do canto (o mesmo das questões)
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
        dst = out / "estudativo_short_003_quantos_triangulos_sem_audio.mp4"
        subprocess.run(["cp", str(mudo), str(dst)], check=True)
        print(dst)
        sys.exit()
    narracao()
    dst = out / "estudativo_short_003_quantos_triangulos.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mudo), "-i", str(NARRACAO), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart",
                    str(dst)], check=True)
    print(dst)
