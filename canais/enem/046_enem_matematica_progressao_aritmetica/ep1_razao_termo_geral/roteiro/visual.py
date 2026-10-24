"""Visual — Progressão Aritmética, Episódio 1: o que é PA, a razão e o "n − 1" (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, contador...).
Peças deste episódio: escadaria() (escada de degraus iguais com o bonequinho subindo), boneco(), cofrinho(),
palitos_quad() e palitos_tri() (figuras de palitos com o palito compartilhado piscando), termos() (fila de termos com os
saltos +r), plano() (os pontos da PA sobre a reta tracejada), linha().
Índices com caracteres subscritos (a₁, aₙ, a₁₂): a fonte desenha direto.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum046", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_pa_ep1_razao_termo_geral.mp4"
CARD_R = K.CARD_R
DEGRAU = K.DEGRAU
PAPEL = K.PAPEL
MADEIRA = "#D9A55B"
CABECA = "#D9483B"
ROSA = "#F4A7B9"
ROSA2 = "#E58AA0"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


def escadaria(c, x0, yb, n, sw, sh, a, acesos=None, rotulos=None, cor=PURPLE, rot_size=24, rot_col=None):
    """escada de n degraus iguais subindo para a direita; acesos = lista de alfas por degrau (barra colorida no topo);
    rotulos = textos dentro de cada degrau (ex.: 'a₁ · 50')"""
    if a <= 0:
        return
    for i in range(n):
        x, top = x0 + i * sw, yb - (i + 1) * sh
        c.drawRect(skia.Rect.MakeXYWH(x, top, sw + 1, yb - top), paint(DEGRAU, a))
        c.drawLine(x, top, x + sw, top, paint("#CFCBC0", a, stroke=3))
        c.drawLine(x, top, x, yb, paint("#DDD9CF", a, stroke=2))
        ai = a * (acesos[i] if acesos and i < len(acesos) else 0)
        if ai > 0:
            c.drawRect(skia.Rect.MakeXYWH(x, top, sw, 9), paint(cor, ai))
        if rotulos and i < len(rotulos) and rotulos[i]:
            ftext(c, rotulos[i], x + sw / 2, top + 6 + rot_size * 1.1, rot_size, "black", rot_col or INK2,
                  a * (acesos[i] if acesos and i < len(acesos) else 1))
    c.drawLine(x0 - 20, yb, x0 + n * sw + 20, yb, paint("#BDB8AC", a, stroke=4))


def degrau_xy(x0, yb, sw, sh, p):
    """posição dos pés do bonequinho na posição p (1 = 1º degrau), com pulo entre degraus"""
    p = max(1.0, p)
    i = int(math.floor(p))
    f = p - i
    xa, xb = x0 + (i - 0.5) * sw, x0 + (i + 0.5) * sw
    ya, yb_ = yb - i * sh, yb - (i + 1) * sh
    x = lerp(xa, xb, f)
    y = lerp(ya, yb_, f) - math.sin(math.pi * f) * sh * 1.3
    return x, y


def boneco(c, x, yf, s, a, col=BLUE):
    if a <= 0:
        return
    pp = paint(col, a, stroke=s * 0.16, cap_round=True)
    c.drawCircle(x, yf - s * 1.62, s * 0.26, paint(col, a))
    c.drawLine(x, yf - s * 1.34, x, yf - s * 0.62, pp)
    c.drawLine(x, yf - s * 0.62, x - s * 0.26, yf, pp)
    c.drawLine(x, yf - s * 0.62, x + s * 0.26, yf, pp)
    c.drawLine(x, yf - s * 1.18, x - s * 0.34, yf - s * 0.84, pp)
    c.drawLine(x, yf - s * 1.18, x + s * 0.36, yf - s * 1.36, pp)


def cofrinho(c, cx, cy, s, a):
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeLTRB(cx - s, cy - s * 0.72, cx + s, cy + s * 0.72), paint(ROSA, a))
    c.drawOval(skia.Rect.MakeLTRB(cx - s, cy - s * 0.72, cx + s, cy + s * 0.72), paint(ROSA2, a, stroke=4))
    for fx in (-0.55, 0.45):
        rrect(c, cx + fx * s, cy + s * 0.55, s * 0.22, s * 0.42, 6, ROSA2, a)
    c.drawOval(skia.Rect.MakeLTRB(cx + s * 0.8, cy - s * 0.18, cx + s * 1.18, cy + s * 0.2), paint(ROSA2, a))
    c.drawCircle(cx + s * 0.92, cy - s * 0.02, s * 0.04, paint(INK, a))
    c.drawCircle(cx + s * 1.05, cy - s * 0.02, s * 0.04, paint(INK, a))
    c.drawCircle(cx + s * 0.45, cy - s * 0.25, s * 0.07, paint(INK, a))
    rrect(c, cx - s * 0.3, cy - s * 0.74, s * 0.6, s * 0.1, 4, ROSA2, a)


def moeda(c, cx, cy, r, a, s="+15"):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#F5C542", a))
    c.drawCircle(cx, cy, r, paint("#C99A1C", a, stroke=4))
    text_mid(c, s, cx, cy, r * 0.7, "black", "#7A5A00", a)


def palito(c, x1, y1, x2, y2, a, col=None, w=9):
    if a <= 0:
        return
    c.drawLine(x1, y1, x2, y2, paint(col or MADEIRA, a, stroke=w, cap_round=True))
    c.drawCircle(x2, y2, w * 0.85, paint(CABECA, a))


def palitos_quad(c, x, y, n, L, a, novos=None, hl=0.0):
    """n quadrados em fila (canto superior esquerdo em x, y). novos = alfa do último quadrado (entrada);
    hl = alfa do destaque âmbar dos palitos compartilhados (pisca)"""
    if a <= 0:
        return
    for k in range(n):
        ak = a * (novos if (novos is not None and k == n - 1) else 1)
        xl, xr = x + k * L, x + (k + 1) * L
        if k == 0:
            palito(c, xl, y + L, xl, y, ak)
        palito(c, xl, y, xr, y, ak)
        palito(c, xl, y + L, xr, y + L, ak)
        shared = k < n - 1
        palito(c, xr, y + L, xr, y, ak, AMBER if (shared and hl > 0.5) else None)


def tri_pontos(x, yb, L, n):
    """vértices da faixa de triângulos alternados (para cima / para baixo)"""
    h = L * 0.866
    base = [(x + j * L, yb) for j in range(n + 2)]
    topo = [(x + L / 2 + j * L, yb - h) for j in range(n + 2)]
    return base, topo


def tri_arestas(n, x, yb, L):
    """arestas na ordem de montagem; cada triângulo novo acrescenta 2 e aproveita a última do anterior"""
    base, topo = tri_pontos(x, yb, L, n)
    ar = [(base[0], base[1]), (base[0], topo[0]), (topo[0], base[1])]
    for k in range(1, n):
        if k % 2 == 1:      # para baixo: topo[j] - topo[j+1] - base[j+1]
            j = (k - 1) // 2
            ar += [(topo[j], topo[j + 1]), (topo[j + 1], base[j + 1])]
        else:               # para cima: base[j] - base[j+1] - topo[j]
            j = k // 2
            ar += [(base[j], base[j + 1]), (base[j + 1], topo[j])]
    return ar


def palitos_tri(c, x, yb, n, L, a, novos=None, hl=0.0):
    """n triângulos em faixa; o palito compartilhado com o triângulo anterior pisca em âmbar (hl)"""
    if a <= 0:
        return
    ar = tri_arestas(n, x, yb, L)
    for i, (p1, p2) in enumerate(ar):
        k = 0 if i < 3 else 1 + (i - 3) // 2
        ak = a * (novos if (novos is not None and k == n - 1) else 1)
        compart = (k < n - 1) and (i == len(tri_arestas(k + 1, x, yb, L)) - 1)
        palito(c, p1[0], p1[1], p2[0], p2[1], ak, AMBER if (compart and hl > 0.5) else None)


def termos(c, vals, cx, cy, a, size=52, bw=150, gap=60, alfas=None, rotulos=None, saltos=None, salto_txt="+3",
           salto_col=None, cores=None, ret=False):
    """fila de termos em caixas; rotulos = textos acima (a₁, a₂...); saltos = alfa dos arcos +r entre as caixas"""
    if a <= 0:
        return []
    n = len(vals)
    alfas, cores = alfas or {}, cores or {}
    tw = n * bw + (n - 1) * gap
    x0 = cx - tw / 2
    xs = []
    for i, v in enumerate(vals):
        ai = a * alfas.get(i, 1.0)
        x = x0 + i * (bw + gap)
        xs.append(x + bw / 2)
        if ai <= 0:
            continue
        col = cores.get(i, BLUE)
        rrect(c, x, cy - 50, bw, 100, 18, mix("#FFFFFF", col, 0.12), ai)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, cy - 50, bw, 100), 18, 18), paint(col, ai, stroke=3))
        fmid(c, str(v), x + bw / 2, cy, size, "black", INK, ai)
        if rotulos and i < len(rotulos) and rotulos[i]:
            ftext(c, rotulos[i], x + bw / 2, cy - 66, 32, "black", col, ai)
    for i in range(n - 1):
        sa = a * (saltos.get(i, 0) if isinstance(saltos, dict) else (saltos or 0))
        if sa <= 0:
            continue
        x1, x2 = xs[i] + bw * 0.25, xs[i + 1] - bw * 0.25
        top = cy + 50 + 54
        p = skia.Path(); p.moveTo(x1, cy + 54); p.quadTo((x1 + x2) / 2, top + 30, x2, cy + 54)
        sc = salto_col or AMBER
        c.drawPath(p, paint(sc, sa, stroke=4, cap_round=True))
        txt = salto_txt[i] if isinstance(salto_txt, (list, tuple)) else salto_txt
        fmid(c, txt, (x1 + x2) / 2, top + 44, 30, "black", sc, sa)
    return xs


def plano(c, x0, y0, w, h, a, nmax=7, vmax=24, pts=None, pa=None, reta=0.0, reta_col=None):
    """eixos n (posição) × aₙ (termo); pts = [(n, v)] com alfas pa (lista); reta = alfa da reta tracejada y = 3n + 2"""
    if a <= 0:
        return None
    X = lambda n: x0 + n / nmax * w
    Y = lambda v: y0 + h - v / vmax * h
    line(c, x0, y0 + h, x0 + w + 20, y0 + h, INK2, a, 4)
    line(c, x0, y0 + h, x0, y0 - 20, INK2, a, 4)
    text(c, "posição n", x0 + w - 60, y0 + h + 60, 26, "black", GRAY, a)
    text(c, "termo", x0 - 10, y0 - 40, 26, "black", GRAY, a)
    for n in range(1, nmax):
        line(c, X(n), y0 + h - 8, X(n), y0 + h + 8, INK2, a, 3)
        text(c, str(n), X(n), y0 + h + 34, 24, "bold", INK2, a)
    for v in range(4, vmax + 1, 4):
        line(c, x0 - 8, Y(v), x0 + 8, Y(v), INK2, a, 3)
        text(c, str(v), x0 - 34, Y(v) + 8, 22, "bold", GRAY, a)
    if reta > 0:
        line(c, X(0.3), Y(3 * 0.3 + 2), X(6.6), Y(3 * 6.6 + 2), reta_col or PURPLE, a * reta, 4, dash=(16, 12))
    for i, (n, v) in enumerate(pts or []):
        ai = a * (pa[i] if pa else 1)
        if ai <= 0:
            continue
        c.drawCircle(X(n), Y(v), 13, paint(BLUE, ai))
        c.drawCircle(X(n), Y(v), 13, paint("#FFFFFF", ai, stroke=3))
    return X, Y


def poste(c, x, yb, h, a, col=INK2):
    if a <= 0:
        return
    line(c, x, yb, x, yb - h, col, a, 8)
    line(c, x, yb - h, x + 26, yb - h, col, a, 6)
    c.drawCircle(x + 28, yb - h + 10, 9, paint("#F5C542", a))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PROGRESSÃO ARITMÉTICA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        cofrinho(c, 380, 430, 140, aa)
        moeda(c, 380, 230 + 30 * (1 - ep(t, C["01.a"] + 0.4, 0.6)), 44, aa * ep(t, C["01.a"] + 0.4, 0.4), "50")
        linha(c, [("jan: ", INK), ("R$ 50", BLUE)], 380, 640, 42, aa)
        linha(c, [("cada mês: ", INK), ("+ R$ 15", GREEN)], 380, 700, 36, ep(t, C["01.a"] + 2.2, 0.4))
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        linha(c, [("dezembro = ", INK), ("R$ ?", AMBER)], 1150, 280, 64, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 760, 360, 820, 120, 24, "#FFFFFF", acc, shadow=True)
        linha(c, [("50 + 12 · 15 = ", INK), ("R$ 230", RED)], 1170, 420, 54, acc)
        sx = ep(t, C["01.c"] + 2.4, 0.4)
        if sx > 0:
            strike(c, 800, 420, 1540, 420, sx, RED, sx)
            selo(c, 1480, 500, sx, "ERROU", RED, -6, 34)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 760, 550, 820, 120, 24, mix("#FFFFFF", GREEN, 0.10), ad)
        linha(c, [("certo: ", INK), ("R$ 215", GREEN)], 1170, 610, 60, ad)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        escadaria(c, 800, 830, 12, 66, 10, ae, acesos=[1] * 12)
        pill(c, "o motivo cabe numa ESCADA", 1170, 760, PURPLE, size=28, a=ae, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "achar o termo 50, 100 ou 1 000 de qualquer PA", "a₅₀  ·  a₁₀₀  ·  a₁ ₀₀₀"),
            ("02.b", "sem listar os anteriores", "nada de escrever 49 termos antes")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        ftext(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 62, 36, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "EQUAÇÃO DO 1º GRAU", 560, 290, 32, "black", BLUE, aa)
        linha(c, [("6r = 24", INK)], 560, 430, 84, aa)
        a2 = ep(t, C["03.a"] + 2.4, 0.4)
        text(c, "÷ 6 dos dois lados", 560, 540, 30, "black", AMBER, a2)
        linha(c, [("r = ", INK), ("4", GREEN)], 560, 640, 84, ep(t, C["03.a"] + 3.4, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    line(c, 960, 240, 960, 780, "#E6E6E2", ab, 3)
    if ab > 0:
        text(c, "FUNÇÃO AFIM", 1370, 290, 32, "black", PURPLE, ab)
        linha(c, [("y = ", INK), ("a", PURPLE), ("x + b", INK)], 1370, 400, 72, ab)
        line(c, 1110, 720, 1640, 470, PURPLE, ab, 5)
        line(c, 1300, 631, 1420, 631, AMBER, ab, 4, dash=(10, 8))
        line(c, 1420, 631, 1420, 574, AMBER, ab, 4, dash=(10, 8))
        text(c, "+1", 1360, 670, 26, "black", AMBER, ab)
        text(c, "a", 1450, 612, 30, "black", PURPLE, ab, align="left")
        text(c, "a = quanto muda a cada unidade", 1370, 790, 30, "black", PURPLE, ep(t, C["03.b"] + 2.6, 0.4))


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS COISAS DO DIA A DIA", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    cols = ((220, "ESCADA", "degraus da mesma altura", "04.a"), (730, "COFRINHO", "+ R$ 15 a cada mês", "04.b"),
            (1240, "PALITOS", "4 · 7 · 10 palitos", "04.c"))
    for x, tit, sub, cue in cols:
        a1 = ep(t, C[cue], 0.5)
        if a1 <= 0:
            continue
        rrect(c, x, 230, 460, 430, 24, "#FFFFFF", a1, shadow=True)
        rrect(c, x, 230, 460, 60, 24, BLUE, a1 * 0.14)
        text(c, tit, x + 230, 272, 28, "black", BLUE, a1)
        text(c, sub, x + 230, 630, 28, "black", INK, a1)
    a1 = ep(t, C["04.a"], 0.5)
    escadaria(c, 270, 580, 5, 72, 50, a1, acesos=[1] * 5)
    a2 = ep(t, C["04.b"], 0.5)
    if a2 > 0:
        cofrinho(c, 940, 470, 100, a2)
        u = ep(t, C["04.b"] + 0.6, 0.8)
        moeda(c, 940, lerp(320, 380, u), 30, a2 * (1 - prog(t, C["04.b"] + 1.6, 0.3)))
    a3 = ep(t, C["04.c"], 0.5)
    if a3 > 0:
        palitos_quad(c, 1270, 340, 1, 46, a3)
        palitos_quad(c, 1360, 340, 2, 46, ep(t, C["04.c"] + 1.0, 0.4))
        palitos_quad(c, 1290, 450, 3, 46, ep(t, C["04.c"] + 1.8, 0.4))
        text(c, "4", 1293, 420, 26, "black", INK2, a3)
        text(c, "7", 1406, 420, 26, "black", INK2, ep(t, C["04.c"] + 1.0, 0.4))
        text(c, "10", 1359, 530, 26, "black", INK2, ep(t, C["04.c"] + 1.8, 0.4))
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "o próximo = o anterior + um valor FIXO", W / 2, 745, ad, 40, BLUE)


# ======================================================================
# bloco a, b — o que é PA, a razão
# ======================================================================

def b_definicao(c, t, C, B):
    head(c, t, B["start"], "TRÊS PALAVRAS SIMPLES", "SEQUÊNCIA · TERMO · POSIÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        pill(c, "SEQUÊNCIA = lista de números EM ORDEM", W / 2, 240, BLUE, size=30, a=aa, anchor="center")
    al = {i: ep(t, C["05.a"] + 0.5 + 0.4 * i, 0.4) for i in range(4)}
    rot = None
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        rot = ["a₁", "a₂", "a₃", "a₄"]
    termos(c, [5, 8, 11, 14], W / 2 - 110, 470, aa, size=60, bw=170, gap=70, alfas=al, rotulos=rot)
    if aa > 0:
        fmid(c, "…", W / 2 + 470, 470, 60, "black", GRAY, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        x = W / 2 - 110 - (4 * 170 + 3 * 70) / 2 + 170 + 70 + 85
        c.drawCircle(x, 470, 92, paint(BLUE, ab, stroke=5))
        pill(c, "TERMO: cada número da lista", x, 610, BLUE, size=26, a=ab, anchor="center")
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        x0 = W / 2 - 110 - (4 * 170 + 3 * 70) / 2
        for i in range(4):
            text(c, f"{i + 1}º", x0 + i * 240 + 85, 350 if ad <= 0 else 330, 30, "black", PURPLE, acc * (1 - ad))
        pill(c, "POSIÇÃO (ou ÍNDICE): o lugar na fila", W / 2 + 330, 680, PURPLE, size=26, a=acc, anchor="center")
    if ad > 0:
        rrect(c, 360, 720, 1200, 90, 20, mix("#FFFFFF", BLUE, 0.08), ad)
        ftext(c, "a₁ = primeiro termo   ·   aₙ = termo da posição n", W / 2, 778, 36, "black", BLUE, ad)


TAB = [("(5, 8, 11, 14, …)", "r = 3", "crescente", GREEN, "06"),
       ("(40, 34, 28, 22, …)", "r = −6", "decrescente", RED, "07.a"),
       ("(7, 7, 7, …)", "r = 0", "constante", GRAY, "07.b"),
       ("(1,5; 2; 2,5; 3; …)", "r = 0,5", "crescente: razão não inteira", GREEN, "07.c"),
       ("(2, 4, 8, 16, …)", "não é PA", "diferenças 2, 4, 8: é PG", RED, "07.d")]


def b_pa(c, t, C, B):
    head_seq(c, t, C, [("06", "PROGRESSÃO ARITMÉTICA", "A ESCADA DE DEGRAUS IGUAIS", BLUE),
                       ("07", "E SE O DEGRAU DESCER?", "OS TIPOS DE PA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 220, 1400, 110, 24, mix("#FFFFFF", BLUE, 0.08), aa)
            text(c, "PA: cada termo = o anterior + um número FIXO", W / 2, 292, 42, "black", BLUE, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            pill(c, "o número fixo = RAZÃO  r", W / 2, 390, PURPLE, size=30, a=ab, anchor="center")
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            sal = {i: ep(t, C["06.c"] + 0.8 + 0.5 * i, 0.4) for i in range(3)}
            termos(c, [5, 8, 11, 14], 640, 530, acc, size=48, bw=130, gap=50, saltos=sal, salto_txt="+3",
                   salto_col=GREEN)
            chip(c, "r = 3 · crescente", 640, 760, GREEN, ep(t, C["06.c"] + 2.6, 0.4), 34)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            escadaria(c, 1180, 800, 4, 110, 80, ad, acesos=[1] * 4)
            x = 1180 + 3 * 110 + 120
            line(c, x, 800 - 3 * 80, x, 800 - 4 * 80, AMBER, ad, 5)
            line(c, x - 14, 800 - 3 * 80, x + 14, 800 - 3 * 80, AMBER, ad, 5)
            line(c, x - 14, 800 - 4 * 80, x + 14, 800 - 4 * 80, AMBER, ad, 5)
            text(c, "r", x + 36, 800 - 3.5 * 80 + 12, 40, "black", AMBER, ad, align="left")
            text(c, "a razão é a ALTURA do degrau", 1400, 460, 30, "black", PURPLE, ad)
        return
    for k, (seq, r, tipo, col, cue) in enumerate(TAB):
        a1 = ep(t, C[cue] if cue != "06" else C["07"], 0.5)
        if a1 <= 0:
            continue
        y = 250 + k * 112
        rrect(c, 220, y, 1480, 92, 18, "#FFFFFF" if k % 2 else "#F7F7F5", a1)
        ftext(c, seq, 260, y + 60, 38, "black", INK, a1, align="left")
        ftext(c, r, 1000, y + 60, 38, "black", col, a1)
        ftext(c, tipo, 1240, y + 60, 32, "black", col, a1, align="left")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        pill(c, "PG: assunto da próxima série", 1700, 812, AMBER, size=22, a=ad, anchor="right")


def b_razao(c, t, C, B):
    head(c, t, B["start"], "A RAZÃO SEM ERRAR O SINAL", "SEGUNDO MENOS PRIMEIRO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        regra(c, "r = a₂ − a₁   (segundo − primeiro)", W / 2, 260, aa, 44)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        termos(c, [40, 34, 28], 620, 450, ab, size=56, bw=150, gap=60, rotulos=["a₁", "a₂", "a₃"],
               saltos=ep(t, C["08.b"] + 1.4, 0.4), salto_txt="−6", salto_col=GREEN)
        linha(c, [("34 − 40 = ", INK), ("−6", GREEN)], 620, 680, 54, ep(t, C["08.b"] + 1.0, 0.4))
        conferido(c, "certo", 480, 770, ep(t, C["08.b"] + 2.4, 0.4), True, 30)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 1080, 400, 560, 140, 22, mix("#FFFFFF", RED, 0.08), acc)
        linha(c, [("40 − 34 = ", INK), ("+6", RED)], 1360, 470, 52, acc)
        text(c, "o maior menos o menor", 1360, 580, 28, "black", RED, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        arrow(c, 1240, 760, 1300, 660, RED, ad, 6, 20)
        text(c, "sobe?", 1340, 720, 32, "black", RED, ad, align="left")
        arrow(c, 1460, 660, 1520, 760, GREEN, ad, 6, 20)
        text(c, "devia descer", 1560, 720, 32, "black", GREEN, ad, align="left")


# ======================================================================
# bloco c — termo geral
# ======================================================================

EX0, EYB, ESW, ESH = 230, 810, 98, 44     # a escada de 12 degraus


def b_saltos(c, t, C, B):
    head(c, t, B["start"], "O CORAÇÃO DA AULA", "CONTE OS SALTOS", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.5)
    aa = ep(t, C["09.a"], 0.5)
    rot = ["50", "65", "80"] + [""] * 8 + ["?"]
    acesos = [aa, aa, aa] + [0] * 8 + [ep(t, C["09.c"], 0.4)]
    escadaria(c, EX0, EYB, 12, ESW, ESH, a0, acesos=acesos, rotulos=rot, rot_size=30)
    for i, lb in ((0, "a₁"), (1, "a₂"), (2, "a₃"), (11, "a₁₂")):
        ftext(c, lb, EX0 + (i + 0.5) * ESW, EYB + 30, 26, "black", PURPLE, acesos[i] * a0)
    # o bonequinho: 1 → 2, volta, 1 → 3 (cue b) ; 1 → 12 (cue d)
    tb, td = C["09.b"], C["09.d"]
    if t < tb + 1.2:
        p, sal = 1.0 + ep(t, tb + 0.2, 0.8), round(ep(t, tb + 0.2, 0.8))
    elif t < tb + 3.6:
        p = 1.0 + 2 * ep(t, tb + 2.2, 1.2)
        sal = int(p - 1 + 1e-6) if p < 3 else 2
    elif t < td:
        p, sal = 3.0, 2
    else:
        u = ep(t, td, 4.0)
        p = 3.0 + 9 * u
        sal = int(p - 1 + 1e-6)
    if t >= C["09.c"] and t < td:
        p, sal = 1.0, 0
    x, y = degrau_xy(EX0, EYB, ESW, ESH, p)
    boneco(c, x, y, 46, a0)
    K.contador(c, 1600, 330, sal, a0, rotulo="saltos", col=AMBER, size=100)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0 and t < td + 4.2:
        pergunta(c, "do 1º ao 12º degrau: quantos saltos?", 760, 250, acc * (1 - ep(t, td, 0.4)), AMBER, 34)
    ad = ep(t, td + 4.0, 0.5)
    if ad > 0:
        regra(c, "do 1º ao 12º degrau você sobe 11 vezes", 760, 250, ad, 36)


def b_formula(c, t, C, B):
    head(c, t, B["start"], "O TERMO GERAL", "n − 1 SALTOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        linha(c, [("até a posição n:  ", INK), ("n − 1", AMBER), ("  saltos", INK)], W / 2, 260, 48, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        boxed(c, 360, 340, 1200, 170, PURPLE, ab, 0.08)
        linha(c, [("aₙ = a₁ + ", INK), ("(n − 1)", AMBER), (" · r", INK)], W / 2, 425, 84, ab)
        pill(c, "TERMO GERAL", 360, 340, PURPLE, size=24, a=ab, anchor="center")
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        linha(c, [("a₁₂ = 50 + ", INK), ("11", AMBER), (" · 15", INK)], W / 2, 600, 58, acc)
        linha(c, [("= 50 + 165 = ", INK), ("R$ 215", GREEN)], W / 2, 700, 58, ep(t, C["10.c"] + 2.6, 0.4))
        conferido(c, "dezembro", 1420, 720, ep(t, C["10.c"] + 4.0, 0.4), True, 30)


def b_teste(c, t, C, B):
    head(c, t, B["start"], "A FÓRMULA ESTÁ CERTA?", "TESTE COM n = 1", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    K.atalho(c, 360, 200, 1200, 150, "ATALHO", ["teste com n = 1: tem de devolver a₁"], aa, 40)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 220, 400, 700, 330, 24, mix("#FFFFFF", GREEN, 0.06), ab)
        text(c, "aₙ = a₁ + (n − 1) · r", 570, 460, 36, "black", PURPLE, ab)
        linha(c, [("50 + ", INK), ("(1 − 1)", AMBER), (" · 15", INK)], 570, 550, 44, ab)
        linha(c, [("= 50 + 0 = ", INK), ("50", GREEN)], 570, 630, 44, ep(t, C["11.b"] + 2.0, 0.4))
        conferido(c, "PASSOU", 470, 710, ep(t, C["11.b"] + 3.0, 0.4), True, 34)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 400, 700, 330, 24, mix("#FFFFFF", RED, 0.06), acc)
        text(c, "versão errada: a₁ + n · r", 1350, 460, 36, "black", RED, acc)
        linha(c, [("50 + ", INK), ("1", RED), (" · 15", INK)], 1350, 550, 44, acc)
        linha(c, [("= ", INK), ("65", RED)], 1350, 630, 44, ep(t, C["11.c"] + 2.0, 0.4))
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        selo(c, 1350, 700, ad, "JANEIRO = 65? REPROVADA", RED, -4, 30)


# ======================================================================
# bloco d — a partir de qualquer termo e a razão por dois termos
# ======================================================================

def faixa_pos(c, x0, cy, n, bw, gap, a, vals=None, cores=None, alfas=None):
    """faixa de caixas numeradas 1..n (posições) com valores opcionais"""
    vals, cores, alfas = vals or {}, cores or {}, alfas or {}
    xs = []
    for i in range(1, n + 1):
        x = x0 + (i - 1) * (bw + gap)
        xs.append(x + bw / 2)
        ai = a * alfas.get(i, 1.0)
        if ai <= 0:
            continue
        col = cores.get(i, LIGHT)
        rrect(c, x, cy - 46, bw, 92, 14, mix("#FFFFFF", col, 0.14) if col != LIGHT else "#FFFFFF", ai)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, cy - 46, bw, 92), 14, 14),
                    paint(col if col != LIGHT else "#D9D9D4", ai, stroke=3))
        ftext(c, f"a{''.join('₀₁₂₃₄₅₆₇₈₉'[int(d)] for d in str(i))}", x + bw / 2, cy - 60, 26, "black", GRAY, ai)
        if i in vals:
            fmid(c, str(vals[i]), x + bw / 2, cy, 40, "black", col if col != LIGHT else INK, ai)
    return xs


def arco(c, x1, x2, y, a, col, txt, alto=60, size=28):
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(x1, y); p.quadTo((x1 + x2) / 2, y + alto, x2, y)
    c.drawPath(p, paint(col, a, stroke=4, cap_round=True))
    fmid(c, txt, (x1 + x2) / 2, y + (alto * 0.5 + 34 if alto > 0 else alto - 16), size, "black", col, a)


def b_qualquer(c, t, C, B):
    head(c, t, B["start"], "SEM O PRIMEIRO TERMO?", "PARTA DE QUALQUER UM", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        boxed(c, 360, 230, 1200, 160, PURPLE, aa, 0.08)
        linha(c, [("aₙ = ", INK), ("aₖ", BLUE), (" + ", INK), ("(n − k)", AMBER), (" · r", INK)], W / 2, 310, 80, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        pill(c, "k = a posição de onde você PARTE", W / 2, 450, BLUE, size=30, a=ab, anchor="center")
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        x0, x1 = 300, 1620
        line(c, x0, 640, x1, 640, INK2, acc, 4)
        for i in range(1, 21):
            x = x0 + (i - 1) / 19 * (x1 - x0)
            on_ = 5 <= i
            line(c, x, 628, x, 652, INK2, acc, 3)
            if i in (1, 5, 10, 15, 20):
                text(c, f"{i}º", x, 700, 26, "black", BLUE if i in (5, 20) else GRAY, acc)
        u = ep(t, C["12.c"] + 0.8, 1.6)
        xa = x0 + 4 / 19 * (x1 - x0)
        xb = x0 + 19 / 19 * (x1 - x0)
        line(c, xa, 600, lerp(xa, xb, u), 600, AMBER, acc, 8)
        linha(c, [("20 − 5 = ", INK), ("15 saltos", AMBER)], W / 2, 780, 44, ep(t, C["12.c"] + 2.4, 0.4))


def b_dois(c, t, C, B):
    head_seq(c, t, C, [("13", "A RAZÃO POR DOIS TERMOS", "a₄ = 17 · a₁₀ = 41", PURPLE),
                       ("14", "O ATALHO", "DIFERENÇA ÷ DIFERENÇA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        add = ep(t, C["13.d"], 0.5)
        vals = {4: 17, 10: 41}
        cores = {4: BLUE, 10: BLUE}
        if add > 0:
            vals[1] = 5
            cores[1] = GREEN
        xs = faixa_pos(c, 230, 330, 10, 120, 26, aa, vals, cores)
        if aa > 0:
            for i in (2, 3, 5, 6, 7, 8, 9):
                fmid(c, "?", xs[i - 1], 330, 36, "black", LIGHT, aa)
            if add <= 0:
                fmid(c, "?", xs[0], 330, 36, "black", LIGHT, aa)
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            for k in range(6):
                arco(c, xs[3 + k] + 10, xs[4 + k] - 10, 390, ab * ep(t, C["13.b"] + 0.3 * k, 0.3), AMBER, "+r", 46, 24)
            linha(c, [("6 saltos  ·  subiu 41 − 17 = ", INK), ("24", BLUE)], W / 2, 560, 44, ep(t, C["13.b"] + 2.4, 0.4))
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            linha(c, [("6r = 24  →  ", INK), ("r = 4", GREEN)], W / 2, 660, 56, acc)
        if add > 0:
            for k in range(3):
                arco(c, xs[k] + 10, xs[k + 1] - 10, 252, add * ep(t, C["13.d"] + 0.3 * k, 0.3), GREEN, "−4", -46, 24)
            linha(c, [("a₁ = 17 − 3 · 4 = ", INK), ("5", GREEN)], W / 2, 770, 48, ep(t, C["13.d"] + 1.6, 0.4))
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 220, 1320, 230, GREEN, aa, 0.08)
        text(c, "ATALHO", W / 2, 264, 22, "black", GREEN, aa, tracking=2)
        fr(c, "diferença dos termos", "diferença das posições", 1040, 330, 50, INK, aa, num_col=BLUE, den_col=AMBER)
        text_mid(c, "r =", 700, 360, 60, "black", INK, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        fr(c, "41 − 17", "10 − 4", 660, 570, 64, INK, ab, num_col=BLUE, den_col=AMBER)
        text_mid(c, "=", 860, 600, 64, "black", INK, ab)
        fr(c, "24", "6", 980, 570, 64, INK, ep(t, C["14.b"] + 2.0, 0.4), num_col=BLUE, den_col=AMBER)
        linha(c, [("=  ", INK), ("4", GREEN)], 1180, 600, 72, ep(t, C["14.b"] + 3.4, 0.4))
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        chip(c, "sem montar equação", W / 2, 760, GREEN, acc, 34)


# ======================================================================
# bloco e — padrão de figuras (triângulos: exemplo nosso)
# ======================================================================

def b_figuras(c, t, C, B):
    head(c, t, B["start"], "PADRÃO DE FIGURAS", "TRIÂNGULOS DE PALITOS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    ab = ep(t, C["15.b"], 0.5)
    acc = ep(t, C["15.c"], 0.5)
    blink = 1.0 if (int((t - C["15.b"]) * 2.5) % 2 == 0) else 0.0
    hl = blink if C["15.b"] + 0.6 < t < C["15.c"] + 1.5 else 0.0
    if aa > 0:
        palitos_tri(c, 250, 470, 1, 130, aa)
        text(c, "figura 1", 315, 540, 28, "black", INK2, aa)
        linha(c, [("3", BLUE), (" palitos", INK)], 315, 600, 34, aa)
    if ab > 0:
        palitos_tri(c, 600, 470, 2, 130, ab, novos=ep(t, C["15.b"] + 0.3, 0.4), hl=hl)
        text(c, "figura 2", 730, 540, 28, "black", INK2, ab)
        linha(c, [("3 + ", INK), ("2", GREEN), (" = 5", INK)], 730, 600, 34, ab)
        pill(c, "aproveita um lado", 730, 290, AMBER, size=24, a=ab * (hl > 0 or t > C["15.c"]), anchor="center")
    if acc > 0:
        palitos_tri(c, 1060, 470, 3, 130, acc, novos=ep(t, C["15.c"] + 0.3, 0.4), hl=hl)
        text(c, "figura 3", 1255, 540, 28, "black", INK2, acc)
        linha(c, [("5 + ", INK), ("2", GREEN), (" = 7", INK)], 1255, 600, 34, acc)
        chip(c, "3, 5, 7 · r = 2", 1560, 330, GREEN, ep(t, C["15.c"] + 1.6, 0.4), 32)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        boxed(c, 260, 660, 1400, 150, PURPLE, ad, 0.08)
        linha(c, [("aₙ = 3 + ", INK), ("(n − 1)", AMBER), (" · 2 = ", INK), ("2n + 1", PURPLE)], W / 2, 715, 46, ad)
        linha(c, [("figura 20: 2 · 20 + 1 = ", INK), ("41 palitos", GREEN)], W / 2, 780, 38,
              ep(t, C["15.d"] + 3.0, 0.4))


# ======================================================================
# bloco f — PA é função afim
# ======================================================================

PTS = [(n, 3 * n + 2) for n in range(1, 7)]


def b_afim(c, t, C, B):
    head_seq(c, t, C, [("16", "POR QUE LEMBRA UMA RETA?", "PA E FUNÇÃO AFIM", PURPLE),
                       ("17", "OS PONTOS DA PA", "UMA RETA SÓ NOS INTEIROS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["16", "17"])
    if sid == "16":
        aa = ep(t, C["16.a"], 0.5)
        if aa > 0:
            text(c, "abra o termo geral", W / 2, 260, 30, "black", GRAY, aa)
            linha(c, [("aₙ = ", INK), ("r", PURPLE), (" · n + ", INK), ("(a₁ − r)", BLUE)], W / 2, 360, 76, aa)
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            linha(c, [("y = ", INK), ("a", PURPLE), ("x + ", INK), ("b", BLUE)], W / 2, 520, 76, ab)
            pill(c, "FUNÇÃO AFIM", W / 2, 610, PURPLE, size=26, a=ab, anchor="center")
        acc = ep(t, C["16.c"], 0.5)
        if acc > 0:
            regra(c, "razão r  =  coeficiente a  =  quanto muda a cada passo", W / 2, 740, acc, 36)
        return
    aa = ep(t, C["17.a"], 0.5)
    pa = [ep(t, C["17.a"] + 0.5 + 0.35 * i, 0.3) for i in range(6)]
    res = plano(c, 300, 230, 820, 540, aa, pts=PTS, pa=pa, reta=ep(t, C["17.b"], 0.8))
    if aa > 0:
        ftext(c, "(5, 8, 11, 14, 17, 20)", 1450, 260, 38, "black", BLUE, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        linha(c, [("y = ", INK), ("3", PURPLE), ("n + 2", INK)], 1450, 360, 56, ab)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0 and res:
        X, Y = res
        c.drawCircle(X(2.5), Y(9.5), 13, paint(RED, acc, stroke=4))
        check_icon(c, X(2.5) + 40, Y(9.5) - 40, 20, acc, RED, "x")
        text(c, "pontos SOLTOS: não existe n = 2,5", 1450, 480, 30, "black", RED, acc)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0 and res:
        X, Y = res
        line(c, X(4), Y(14), X(5), Y(14), AMBER, ad, 5)
        line(c, X(5), Y(14), X(5), Y(17), AMBER, ad, 5)
        text(c, "+1", (X(4) + X(5)) / 2, Y(14) + 36, 26, "black", AMBER, ad)
        text(c, "+3", X(5) + 34, (Y(14) + Y(17)) / 2 + 8, 26, "black", AMBER, ad)
        regra(c, "a razão é a INCLINAÇÃO", 1450, 620, ad, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "CONTE OS SALTOS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 120, 24, "#F7F7F5", aa)
        linha(c, [("PA ", INK), ("(7, 11, 15, …)", BLUE), ("  ·  ", INK), ("a₃₀ = ?", AMBER)], W / 2, 270, 58, aa)
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 560)
    if t < C["19"]:
        return
    ab0 = ep(t, C["19.a"], 0.5)
    if ab0 > 0:
        linha(c, [("r = 11 − 7 = ", INK), ("4", GREEN)], W / 2, 410, 52, ab0)
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0:
        linha(c, [("do 1º ao 30º: ", INK), ("29 saltos", AMBER)], W / 2, 510, 52, ab)
    acc = ep(t, C["19.c"], 0.5)
    if acc > 0:
        linha(c, [("a₃₀ = 7 + 29 · 4 = 7 + 116 = ", INK), ("123", GREEN)], W / 2, 620, 52, acc)
    ad = ep(t, C["19.d"], 0.5)
    if ad > 0:
        K.atalho(c, 460, 680, 1000, 130, "TESTE COM n = 1", ["7 + 0 · 4 = 7  ✓"], ad, 36)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Razão é segundo menos primeiro.",
          "Do 1º ao n-ésimo termo há n − 1 saltos.",
          "PA é uma reta vista só nos números inteiros."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("a₁₂ = a₁ + 12 · r  (um salto a mais)", "é o 12º termo, e o 12 está ali, pedindo para entrar",
          "o 1º degrau é a partida: do 1º ao 12º são 11 saltos → a₁ + 11r"),
         ("razão de (40, 34, 28) = 6", "a distância entre os números é mesmo 6, e o sinal some sem barulho",
          "segundo − primeiro: 34 − 40 = −6. Sequência que desce tem razão negativa"),
         ("figura n de triângulos = 3n palitos", "cada triângulo, sozinho, tem mesmo 3 lados",
          "os vizinhos DIVIDEM um lado: 3 no primeiro, +2 em cada novo → 2n + 1")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS2 = [("A", "R$ 165,00", "só o acréscimo", RED), ("B", "R$ 180,00", "12 · 15 sem os 50", RED),
         ("C", "R$ 215,00", "", GREEN), ("D", "R$ 230,00", "12 saltos", RED),
         ("E", "R$ 1 590,00", "a soma dos 12", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · EU FAÇO", "TERMO DISTANTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Para juntar dinheiro, Ana depositou R$ 50,00 em janeiro e decidiu que, a cada mês, "
                           "depositaria R$ 15,00 a mais do que no mês anterior. O valor que ela vai depositar em "
                           "dezembro, o 12º mês, é", INK)], a0, 240, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 44, C["25.ok"], "C", cues_in, cues_x, gap=34)
    if t >= C["25"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["25"], 0.4))
        ftext(c, "50 · 65 · 80 …  →  r = 15", 540, y0 + 50, 30, "black", BLUE, ep(t, C["25"], 0.4))
        linha(c, [("dezembro = a₁₂ → ", INK), ("11 saltos", AMBER)], 540, y0 + 110, 30, ep(t, C["25.a"], 0.4))
        linha(c, [("50 + 11 · 15 = ", INK), ("215", GREEN)], 540, y0 + 170, 36, ep(t, C["25.b"], 0.4))
        conferido(c, "perto de 200: razoável", 260, y0 + 240, ep(t, C["25.c"], 0.4), True, 26)


ALTS1 = [("A", "101", "+2 por quadrado", RED), ("B", "148", "49 quadrados", RED), ("C", "150", "sem o palito inicial", RED),
         ("D", "151", "", GREEN), ("E", "200", "4 por quadrado", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · VOCÊ FAZ", "PADRÃO DE PALITOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    yend = _enunciado(c, [("Uma criança monta, com palitos de fósforo, uma sequência de figuras. A figura 1 é um "
                           "quadrado (4 palitos); a figura 2 tem dois quadrados lado a lado, que compartilham um palito "
                           "(7 palitos); a figura 3 tem três quadrados em fila (10 palitos), e assim por diante. O número "
                           "de palitos necessários para montar a figura 50 é", INK)], a0, 230, 24, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["28"], 0.3)),
         align="left")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 44, C["28.ok"], "D", cues_in, cues_x, gap=34)
    if t < C["28"]:
        pause_timer(c, t, C["27.end"] - 1.9, 540, yend + 150)
        if t < C["27.p"]:
            palitos_quad(c, 300, yend + 60, 3, 50, ep(t, C["27.a"] + 4.0, 0.5))
    else:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["28"], 0.4))
        ftext(c, "4 · 7 · 10 …  →  r = 3", 540, y0 + 50, 30, "black", BLUE, ep(t, C["28"], 0.4))
        linha(c, [("figura 1 → 50: ", INK), ("49 saltos", AMBER)], 540, y0 + 110, 30, ep(t, C["28.a"], 0.4))
        linha(c, [("4 + 49 · 3 = 4 + 147 = ", INK), ("151", GREEN)], 540, y0 + 170, 32, ep(t, C["28.b"], 0.4))
        linha(c, [("reta: 3 · 50 + 1 = ", INK), ("151", GREEN)], 540, y0 + 230, 30, ep(t, C["28.c"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "CONTAR TERMOS E SALTOS", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        yb = 560
        line(c, 220, yb, 1700, yb, "#9A968C", aa, 14)
        line(c, 220, yb, 1700, yb, "#FFFFFF", aa, 2, dash=(30, 26))
        xa, xb = 300, 1620
        poste(c, xa, yb, 200, aa)
        poste(c, xb, yb, 200, aa)
        text(c, "km 3", xa, yb + 60, 34, "black", INK, aa)
        text(c, "km 27", xb, yb + 60, 34, "black", INK, aa)
        for k in range(1, 6):
            ak = aa * ep(t, C["31.a"] + 1.4 + 0.3 * k, 0.3)
            x = lerp(xa, xb, k / 6)
            poste(c, x, yb, 200, ak, GRAY)
            text(c, "?", x, yb + 60, 34, "black", AMBER, ak)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        linha(c, [("distância = 24 ÷ 5 ?", AMBER)], W / 2, 280, 56, ab)
    acc = ep(t, C["31.c"], 0.5)
    if acc > 0:
        selo(c, 1420, 300, acc, "NÃO", RED, -6, 48)
    pill(c, "ep. 2 · contar termos e saltos sem errar", W / 2, 760, PURPLE, size=30, a=ep(t, C["31.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você já tinha caído no salto a mais?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao, pa=b_pa,
              razao=b_razao, saltos=b_saltos, formula=b_formula, teste=b_teste, qualquer=b_qualquer, dois=b_dois,
              figuras=b_figuras, afim=b_afim, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, q1=b_q1,
              ponte=b_ponte, cta=b_cta)
