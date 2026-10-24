"""Visual — Conceito de Função, Episódio 1: a ideia de função, quando é e quando não é (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: maquina() (funil de entrada, caixa e bandeja de saída), bomba() (o visor da bomba de combustível),
diagrama() (conjuntos A e B com flechas; marca o defeito), tabela() (x → y com linhas destacadas), linha().
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
_s = importlib.util.spec_from_file_location("comum038", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcoes_ep1_ideia_funcao.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
METAL = "#5B6270"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def maquina(c, cx, cy, s, a, entra=None, sai=None, u=1.0, rotulo="FUNÇÃO", col=None):
    """máquina: funil em cima (entrada), caixa, bandeja embaixo (saída). u = 0..1: o número cai no funil (0–0.4),
    a máquina processa (0.4–0.6) e a saída aparece na bandeja (0.6–1)."""
    if a <= 0:
        return
    col = col or PURPLE
    w, h = s, s * 0.62
    x0, y0 = cx - w / 2, cy - h / 2
    # funil
    p = skia.Path()
    p.moveTo(cx - w * 0.30, y0 - h * 0.55); p.lineTo(cx + w * 0.30, y0 - h * 0.55)
    p.lineTo(cx + w * 0.08, y0); p.lineTo(cx - w * 0.08, y0); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.18), a))
    c.drawPath(p, paint(col, a, stroke=5))
    text(c, "ENTRADA", cx - w * 0.42, y0 - h * 0.40, s * 0.055, "black", BLUE, a, align="right")
    # corpo
    rrect(c, x0, y0, w, h, 26, col, a, shadow=True)
    rrect(c, x0 + w * 0.08, y0 + h * 0.16, w * 0.84, h * 0.40, 16, mix("#FFFFFF", col, 0.25), a)
    girar = clamp((u - 0.4) / 0.2)
    for k in range(3):
        gx = x0 + w * (0.28 + k * 0.22)
        gy = y0 + h * 0.36
        r = h * 0.11
        c.drawCircle(gx, gy, r, paint("#FFFFFF", a))
        ang = math.radians(girar * 360 * (1 if k % 2 else -1) + k * 30)
        line(c, gx, gy, gx + math.cos(ang) * r * 0.8, gy + math.sin(ang) * r * 0.8, col, a, 5)
    text(c, rotulo, cx, y0 + h * 0.84, s * 0.09, "black", "#FFFFFF", a)
    # bandeja
    by = y0 + h + h * 0.30
    rrect(c, cx - w * 0.30, by - 12, w * 0.60, 24, 12, METAL, a)
    line(c, cx, y0 + h, cx, by - 12, METAL, a, 8)
    text(c, "SAÍDA", cx + w * 0.42, by + 10, s * 0.055, "black", GREEN, a, align="left")
    # número entrando
    if entra is not None:
        ue = clamp(u / 0.4)
        if ue < 1:
            yy = lerp(y0 - h * 1.05, y0 - h * 0.15, ease_io(ue))
            fmid(c, entra, cx, yy, s * 0.12, "black", BLUE, a * (1 - clamp((ue - 0.85) / 0.15)))
    if sai is not None:
        us = clamp((u - 0.6) / 0.4)
        if us > 0:
            yy = lerp(y0 + h * 0.9, by - s * 0.09, ease_out(us))
            fmid(c, sai, cx, yy, s * 0.12, "black", GREEN, a * clamp(us * 3))


def bomba(c, cx, cy, w, a, litros="10 L", valor="R$ 60,00", col_valor=None):
    """visor da bomba de combustível"""
    if a <= 0:
        return
    h = w * 0.62
    rrect(c, cx - w / 2, cy - h / 2, w, h, 24, "#2B2F37", a, shadow=True)
    rrect(c, cx - w * 0.44, cy - h * 0.40, w * 0.88, h * 0.34, 12, "#10141A", a)
    rrect(c, cx - w * 0.44, cy + h * 0.04, w * 0.88, h * 0.34, 12, "#10141A", a)
    text(c, "LITROS", cx - w * 0.40, cy - h * 0.30, w * 0.05, "black", "#9AA3B2", a, align="left")
    text(c, "A PAGAR", cx - w * 0.40, cy + h * 0.14, w * 0.05, "black", "#9AA3B2", a, align="left")
    text(c, litros, cx + w * 0.40, cy - h * 0.10, w * 0.12, "black", "#7FD4FF", a, align="right")
    text(c, valor, cx + w * 0.40, cy + h * 0.33, w * 0.12, "black", col_valor or "#8CF09A", a, align="right")


A3 = ["1", "2", "3"]
B3 = ["a", "b", "c"]


def diagrama(c, cx, cy, a, setas, A=A3, B=B3, h=330, prog_=1.0, ruim_A=None, ruim_setas=(), cor_seta=None,
             nomes=("A", "B"), size=40, gapx=360, larg=170):
    """conjuntos A e B (elipses) com flechas setas = [(i, j)] (i em A, j em B). prog_ = 0..1 desenha as flechas em sequência.
    ruim_A = índice de A destacado em vermelho (sem flecha ou com duas); ruim_setas = flechas em vermelho."""
    if a <= 0:
        return
    xa, xb = cx - gapx / 2, cx + gapx / 2
    for x, nome, col in ((xa, nomes[0], BLUE), (xb, nomes[1], GREEN)):
        rect = skia.Rect.MakeXYWH(x - larg / 2, cy - h / 2, larg, h)
        c.drawOval(rect, paint(mix("#FFFFFF", col, 0.12), a))
        c.drawOval(rect, paint(col, a, stroke=5))
        text(c, nome, x, cy - h / 2 - 22, size * 0.9, "black", col, a)

    def ys(n, k):
        return cy + (k - (n - 1) / 2) * (h * 0.78 / max(n, 1))

    pos_a = [(xa, ys(len(A), k)) for k in range(len(A))]
    pos_b = [(xb, ys(len(B), k)) for k in range(len(B))]
    for k, (x, y) in enumerate(pos_a):
        if ruim_A == k:
            rw = max(size * 0.75, ftext_w(A[k], "black", size) / 2 + 12)
            rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - rw, y - size * 0.75, rw * 2, size * 1.5), size * 0.75,
                                       size * 0.75)
            c.drawRRect(rr, paint(mix("#FFFFFF", RED, 0.25), a))
            c.drawRRect(rr, paint(RED, a, stroke=4))
        fmid(c, A[k], x, y, size, "black", RED if ruim_A == k else INK, a)
    for k, (x, y) in enumerate(pos_b):
        fmid(c, B[k], x, y, size, "black", INK, a)
    n = len(setas)
    for k, (i, j) in enumerate(setas):
        pk = clamp(prog_ * n - k)
        if pk <= 0:
            continue
        (x0, y0), (x1, y1) = pos_a[i], pos_b[j]
        ra = max(size * 0.6, ftext_w(A[i], "black", size) / 2 + 14)
        rb = max(size * 0.6, ftext_w(B[j], "black", size) / 2 + 14)
        col = RED if (i, j) in ruim_setas else (cor_seta or INK2)
        arrow(c, x0 + ra, y0, x1 - rb, y1, col, a, 5, 18, pk)


def tabela(c, x, y, rows, a, w=360, rh=70, destaque=(), cor_dest=None, alfas=None, size=38):
    """tabela x | y. rows = [(x, y)]. destaque = índices das linhas em âmbar/vermelho."""
    if a <= 0:
        return
    rrect(c, x, y, w, rh, 14, PURPLE, a)
    text_mid(c, "x", x + w * 0.25, y + rh / 2, size, "black", "#FFFFFF", a)
    text_mid(c, "y", x + w * 0.75, y + rh / 2, size, "black", "#FFFFFF", a)
    for k, (vx, vy) in enumerate(rows):
        ak = a * (alfas[k] if alfas else 1.0)
        if ak <= 0:
            continue
        yy = y + rh * (k + 1)
        bg = mix("#FFFFFF", cor_dest or RED, 0.22) if k in destaque else ("#FFFFFF" if k % 2 else "#F4F4F1")
        rrect(c, x, yy, w, rh, 0, bg, ak)
        fmid(c, vx, x + w * 0.25, yy + rh / 2, size, "black", BLUE, ak)
        fmid(c, vy, x + w * 0.75, yy + rh / 2, size, "black", GREEN, ak)
    line(c, x + w / 2, y + rh, x + w / 2, y + rh * (len(rows) + 1), "#D6D6D0", a, 3)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÕES · EPISÓDIO 1", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        for k in range(3):
            ak = ep(t, C["01.a"] + 1.2 + k * 0.7, 0.4)
            if ak <= 0:
                continue
            bomba(c, 360 + k * 300, 450, 260, ak)
        linha(c, [("10 L", BLUE), ("  →  ", INK), ("R$ 60,00", GREEN)], 660, 660, 52, aa)
        text(c, "SEMPRE", 660, 740, 40, "black", GREEN, ep(t, C["01.a"] + 3.4, 0.4))
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        bomba(c, 1450, 450, 300, ab, valor="R$ 70,00", col_valor="#FF8A8A")
        selo(c, 1450, 650, ep(t, C["01.b"] + 1.0, 0.4), "OS MESMOS 10 L?", RED, -5, 34)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 560, 770, 800, 90, 30, BLUE, acc)
        text_mid(c, "ESSA REVOLTA = FUNÇÃO", W / 2, 815, 44, "black", "#FFFFFF", acc)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "BLOCO DE FUNÇÕES · EP. 1", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "1º episódio do bloco de FUNÇÕES", W / 2, 250, BLUE, size=32, a=a0, anchor="center")
    aa = ep(t, C["02.a"], 0.5)
    itens = [("TEXTO", "“cada aluno, sua data”"), ("TABELA", "x → y"), ("FLECHAS", "A → B")]
    for k, (tit, sub) in enumerate(itens):
        ak = aa * ep(t, C["02.a"] + 0.6 + k * 0.6, 0.4)
        if ak <= 0:
            continue
        x = 420 + k * 540
        rrect(c, x - 220, 330, 440, 210, 24, "#FFFFFF", ak, shadow=True)
        text(c, tit, x, 410, 44, "black", BLUE, ak)
        text(c, sub, x, 480, 32, "bold", INK2, ak)
    ab = ep(t, C["02.b"], 0.5)
    if ab > 0:
        chip(c, "É FUNÇÃO?", 720, 650, GREEN, ab, 46)
        chip(c, "NÃO É?", 1120, 650, RED, ab, 46)
    acc = ep(t, C["02.c"], 0.5)
    if acc > 0:
        regra(c, "e QUEM DEPENDE DE QUEM", W / 2, 780, acc, 38)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "CONJUNTO = lista entre chaves", 520, 290, 36, "black", BLUE, aa)
        linha(c, [("A = ", INK), ("{ 1, 2, 3 }", BLUE)], 520, 470, 80, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "SUBSTITUIR na fórmula", 1400, 290, 36, "black", BLUE, ab)
        text(c, "série de Expressões algébricas", 1400, 340, 26, "bold", GRAY, ab)
        linha(c, [("V = 6 · L", PURPLE)], 1400, 450, 64, ab)
        linha(c, [("L = 10  →  6 · 10 = ", INK), ("60", GREEN)], 1400, 560, 48, ep(t, C["03.b"] + 2.0, 0.4))
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS COISAS DO DIA A DIA", "ENTRA UMA, SAI OUTRA", BLUE)
    card(c, *CARD_R)
    cols = [("04.a", "BOMBA", "litros", "valor"), ("04.b", "TAXÍMETRO", "km rodados", "preço"),
            ("04.c", "CHAMADA", "número", "aluno")]
    for k, (cue, tit, ent, sai) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 450 + k * 510
        rrect(c, x - 230, 220, 460, 470, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x - 230, 220, 460, 60, 24, BLUE, a * 0.14)
        text(c, tit, x, 262, 30, "black", BLUE, a)
        if k == 0:
            bomba(c, x, 410, 300, a)
        elif k == 1:
            rrect(c, x - 150, 340, 300, 140, 18, "#2B2F37", a)
            text(c, "R$ 15,00", x, 432, 52, "black", "#FFD166", a)
            text(c, "4 km", x, 520, 36, "black", INK2, a)
        else:
            for j, (n_, nome) in enumerate((("1", "Ana"), ("2", "Bruno"), ("3", "Carla"))):
                yy = 350 + j * 62
                fmid(c, n_, x - 110, yy, 38, "black", BLUE, a)
                text_mid(c, "→", x - 40, yy, 36, "black", INK2, a)
                text_mid(c, nome, x + 20, yy, 36, "black", GREEN, a, align="left")
        linha(c, [("entra: ", INK2), (ent, BLUE)], x, 590, 30, a)
        linha(c, [("sai: ", INK2), (sai, GREEN)], x, 640, 30, a)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "uma coisa ENTRA, outra SAI", W / 2, 765, ad, 40, BLUE)


# ======================================================================
# bloco a — a máquina
# ======================================================================

def b_maquina(c, t, C, B):
    head(c, t, B["start"], "A MÁQUINA", "MESMA ENTRADA, MESMA SAÍDA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    t0 = C["05.b"]
    k = int(clamp((t - t0) / 1.8, 0, 2.999)) if t >= t0 else -1
    u = clamp((t - t0 - max(k, 0) * 1.8) / 1.6) if k >= 0 else 0
    maquina(c, 640, 500, 520, aa, "10" if k >= 0 else None, "60" if k >= 0 else None, u, "× 6")
    if aa > 0 and k < 0:
        text(c, "entra um número, sai um número", 640, 830, 30, "black", INK2, aa)
    # placar das três vezes
    for j in range(3):
        aj = ep(t, t0 + j * 1.8 + 1.4, 0.3)
        if aj <= 0:
            continue
        y = 330 + j * 120
        rrect(c, 1120, y - 45, 520, 90, 18, "#FFFFFF", aj, shadow=True)
        linha(c, [(f"{j + 1}ª vez:  ", INK2), ("10", BLUE), ("  →  ", INK), ("60", GREEN)], 1380, y, 40, aj)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        selo(c, 1380, 720, acc, "SEMPRE A MESMA SAÍDA", GREEN, -4, 34)
        pill(c, "isso é uma FUNÇÃO", 1380, 810, BLUE, size=30, a=ep(t, C["05.c"] + 1.6, 0.4), anchor="center")


def b_definicao(c, t, C, B):
    head(c, t, B["start"], "DEFINIÇÃO", "FUNÇÃO DE A EM B", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 220, 1460, 130, 24, mix("#FFFFFF", BLUE, 0.10), aa)
        para(c, "FUNÇÃO: regra que associa a CADA elemento de A um ÚNICO elemento de B", 270, 275, 38, "black", BLUE,
             aa, 1400, 46)
    ab = ep(t, C["06.b"], 0.5)
    diagrama(c, 700, 600, ab, [(0, 0), (1, 1), (2, 1)], h=300, prog_=ep(t, C["06.b"] + 0.5, 1.2), gapx=380)
    if ab > 0:
        pill(c, "conjunto de PARTIDA", 510, 800, BLUE, size=24, a=ab, anchor="center")
        pill(c, "conjunto de CHEGADA", 890, 800, GREEN, size=24, a=ep(t, C["06.b"] + 2.4, 0.4), anchor="center")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        linha(c, [("f", PURPLE), (" : ", INK), ("A", BLUE), (" → ", INK), ("B", GREEN)], 1380, 520, 96, acc)
        text(c, "“f, de A em B”", 1380, 620, 34, "bold", INK2, acc)
        selo(c, 1380, 740, ep(t, C["06.c"] + 1.8, 0.4), "ÚNICO", PURPLE, -5, 52)


# ======================================================================
# bloco b — variáveis
# ======================================================================

LEIS = [("táxi", "distância (km)", "preço (R$)", "P(d) = 5 + 2,5d"),
        ("quadrado", "lado", "área", "A(ℓ) = ℓ²"),
        ("combustível", "litros", "valor pago (R$)", "V(L) = 6L"),
        ("bola para cima", "tempo (s)", "altura (m)", "h(t) = 20t − 5t²")]


def b_variaveis(c, t, C, B):
    head(c, t, B["start"], "QUEM ESCOLHE? QUEM É CALCULADO?", "INDEPENDENTE × DEPENDENTE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 205, 700, 100, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        linha(c, [("x", BLUE), (" = variável INDEPENDENTE · você escolhe", INK)], 570, 255, 28, aa)
        ab0 = ep(t, C["07.a"] + 2.6, 0.4)
        rrect(c, 1000, 205, 700, 100, 20, mix("#FFFFFF", GREEN, 0.12), ab0)
        linha(c, [("y", GREEN), (" = variável DEPENDENTE · é calculada", INK)], 1350, 255, 28, ab0)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        pill(c, "LEI DA FUNÇÃO = a fórmula que liga x e y", W / 2, 350, PURPLE, size=26, a=ab, anchor="center")
    # tabela da seção 02
    x0, y0 = 220, 400
    cols = [(0, 330, "SITUAÇÃO", INK2), (330, 420, "ENTRA (x)", BLUE), (750, 420, "SAI (y)", GREEN),
            (1170, 310, "LEI", PURPLE)]
    ah = ep(t, C["07.c"], 0.4)
    if ah > 0:
        for dx, w_, tit, col in cols:
            rrect(c, x0 + dx, y0, w_ - 10, 54, 12, mix("#FFFFFF", col, 0.18), ah)
            text_mid(c, tit, x0 + dx + (w_ - 10) / 2, y0 + 27, 24, "black", col, ah)
    cues = [("07.c", 0), ("07.c", 2.2), ("07.c", 4.4), ("07.d", 0)]
    for k, (sit, ent, sai, lei) in enumerate(LEIS):
        ak = ep(t, C[cues[k][0]] + cues[k][1], 0.4)
        if ak <= 0:
            continue
        y = y0 + 70 + k * 84
        rrect(c, x0, y, 1470, 74, 14, "#FFFFFF" if k % 2 else "#F6F6F3", ak)
        text_mid(c, sit, x0 + 160, y + 37, 28, "black", INK, ak)
        text_mid(c, ent, x0 + 330 + 205, y + 37, 28, "black", BLUE, ak)
        text_mid(c, sai, x0 + 750 + 205, y + 37, 28, "black", GREEN, ak)
        K.mdraw(c, lei.replace("ℓ²", "ℓ^2").replace("5t²", "5t^2"), x0 + 1180, y + 37, 26, PURPLE, ak)


# ======================================================================
# bloco c — quem depende de quem
# ======================================================================

def _aluno(c, x, y, s, a, col, nome):
    c.drawCircle(x, y - s * 0.55, s * 0.18, paint(col, a))
    rrect(c, x - s * 0.22, y - s * 0.34, s * 0.44, s * 0.62, s * 0.14, col, a)
    text(c, nome, x, y + s * 0.55, s * 0.17, "black", INK2, a)


def b_depende(c, t, C, B):
    head(c, t, B["start"], "QUEM DEPENDE DE QUEM?", "A PERGUNTA CERTA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        text(c, "sei o LADO → sei a ÁREA?", 560, 250, 36, "black", INK, aa)
        rrect(c, 420, 320, 280, 280, 8, mix("#FFFFFF", BLUE, 0.2), aa)
        c.drawRect(skia.Rect.MakeXYWH(420, 320, 280, 280), paint(BLUE, aa, stroke=5))
        text(c, "lado 3", 560, 650, 36, "black", BLUE, aa)
        text_mid(c, "área 9", 560, 460, 48, "black", GREEN, ep(t, C["08.a"] + 1.6, 0.4))
        conferido(c, "SIM: área é função do lado", 340, 740, ep(t, C["08.a"] + 3.0, 0.4), True, 32)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        line(c, 960, 230, 960, 800, "#E6E6E2", ab, 3)
        text(c, "sei a ALTURA → sei o ALUNO?", 1380, 250, 36, "black", INK, ab)
        rrect(c, 1180, 300, 400, 70, 35, mix("#FFFFFF", AMBER, 0.3), ab)
        text_mid(c, "altura: 1,70 m", 1380, 335, 34, "black", AMBER, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        _aluno(c, 1260, 540, 200, acc, BLUE, "Ana")
        _aluno(c, 1500, 540, 200, acc, GREEN, "Bruno")
        text(c, "1,70 m", 1260, 680, 28, "black", AMBER, acc)
        text(c, "1,70 m", 1500, 680, 28, "black", AMBER, acc)
        conferido(c, "NÃO: aluno não é função da altura", 1080, 760, ep(t, C["08.c"] + 1.5, 0.4), False, 30)


def b_magica(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "A PERGUNTA MÁGICA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    K.atalho(c, 260, 250, 1400, 200, "A PERGUNTA MÁGICA", ["se eu souber ISTO,", "consigo dizer AQUILO sem dúvida?"], aa, 44)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 540, 600, 180, 28, mix("#FFFFFF", GREEN, 0.15), ab)
        text_mid(c, "SIM", 600, 600, 60, "black", GREEN, ab)
        text_mid(c, "é função", 600, 670, 40, "black", INK, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 540, 600, 180, 28, mix("#FFFFFF", RED, 0.12), acc)
        text_mid(c, "DUAS RESPOSTAS?", 1320, 600, 52, "black", RED, acc)
        text_mid(c, "não é", 1320, 670, 40, "black", INK, acc)


# ======================================================================
# bloco d — o diagrama de flechas
# ======================================================================

def b_flechas(c, t, C, B):
    head(c, t, B["start"], "O DIAGRAMA DE FLECHAS", "AS DUAS REGRAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    diagrama(c, 560, 520, aa, [(0, 0), (1, 2), (2, 1)], prog_=ep(t, C["10.a"] + 1.2, 1.5), h=380)
    ab = ep(t, C["10.b"], 0.5)
    regras = [("10.b", "1", "TODO elemento de A tem flecha saindo"), ("10.c", "2", "de cada elemento de A sai UMA SÓ flecha")]
    for k, (cue, n_, s_) in enumerate(regras):
        ak = ep(t, C[cue] + (1.0 if k == 0 else 0), 0.5)
        if ak <= 0:
            continue
        y = 300 + k * 170
        rrect(c, 960, y - 60, 700, 130, 22, mix("#FFFFFF", PURPLE, 0.10), ak)
        badge_num(c, n_, 1010, y + 5, ak, 30, bg=PURPLE)
        para(c, s_, 1060, y - 4, 34, "black", INK, ak, 580, 42)
    if ab > 0 and t < C["10.b"] + 1.0:
        text(c, "para ser FUNÇÃO:", 1310, 250, 34, "black", PURPLE, ab)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 960, 610, 700, 120, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        para(c, "em B: NENHUMA exigência (várias flechas ou nenhuma)", 1000, 660, 32, "black", GREEN, ad, 640, 40)


# ======================================================================
# bloco e — os três diagramas
# ======================================================================

D1 = [(0, 0), (1, 0), (2, 1)]
D2 = [(0, 0), (1, 1)]
D3 = [(0, 0), (1, 1), (1, 2), (2, 2)]


def b_diagramas(c, t, C, B):
    head_seq(c, t, C, [("11", "TESTE 1", "É FUNÇÃO?", PURPLE), ("12", "TESTES 2 E 3", "ONDE ESTÁ O DEFEITO?", PURPLE)])
    card(c, *CARD_R)
    xs = [420, 960, 1500]
    a1 = ep(t, C["11"], 0.4)
    diagrama(c, xs[0], 500, a1, D1, prog_=ep(t, C["11.a"], 3.0), h=330, gapx=260, larg=140, size=38)
    a1c = ep(t, C["11.c"], 0.4)
    if a1c > 0:
        selo(c, xs[0], 760, a1c, "É FUNÇÃO", GREEN, -4, 34)
        pill(c, "2 flechas chegam no a: pode", xs[0], 830, GREEN, size=20, a=a1c, anchor="center")
    if t < C["12"]:
        return
    a2 = ep(t, C["12"], 0.4)
    ruim2 = 2 if t >= C["12.a"] else None
    diagrama(c, xs[1], 500, a2, D2, prog_=ep(t, C["12"] + 0.3, 1.5), h=330, gapx=260, larg=140, size=38, ruim_A=ruim2)
    a2c = ep(t, C["12.a"], 0.4)
    if a2c > 0:
        selo(c, xs[1], 760, a2c, "NÃO É", RED, -4, 34)
        pill(c, "o 3 ficou sem flecha", xs[1], 830, RED, size=20, a=a2c, anchor="center")
    a3 = ep(t, C["12.b"], 0.4)
    diagrama(c, xs[2], 500, a3, D3, prog_=ep(t, C["12.b"] + 0.3, 2.0), h=330, gapx=260, larg=140, size=38,
             ruim_A=1 if t >= C["12.c"] else None, ruim_setas=((1, 1), (1, 2)) if t >= C["12.b"] + 1.5 else ())
    a3c = ep(t, C["12.c"], 0.4)
    if a3c > 0:
        selo(c, xs[2], 760, a3c, "NÃO É", RED, -4, 34)
        pill(c, "do 2 saem duas flechas", xs[2], 830, RED, size=20, a=a3c, anchor="center")


# ======================================================================
# bloco f — duas flechas chegando
# ======================================================================

def b_chegando(c, t, C, B):
    head(c, t, B["start"], "DUAS FLECHAS CHEGANDO", "ESTRAGA?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        K.mdraw(c, "x^2", 300, 270, 54, PURPLE, aa)
        text(c, "regra: x ao quadrado", 420, 282, 32, "black", PURPLE, aa, align="left")
    diagrama(c, 560, 540, aa, [(0, 0), (1, 0), (2, 1)], A=["2", "−2", "3"], B=["4", "9"], h=320, gapx=380,
             prog_=ep(t, C["13.a"] + 0.8, 2.4), size=42)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        conferido(c, "cada entrada: UMA saída", 260, 790, ab, True, 32)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 230, 680, 380, 26, "#FFFFFF", acc, shadow=True)
        text(c, "DATA DE NASCIMENTO", 1340, 290, 32, "black", BLUE, acc)
        for j, nome in enumerate(("Ana", "Bruno", "Carla")):
            fmid(c, nome, 1110, 380 + j * 80, 34, "black", INK, acc)
        rrect(c, 1450, 400, 200, 120, 18, mix("#FFFFFF", AMBER, 0.3), acc)
        text_mid(c, "12/03", 1550, 460, 44, "black", AMBER, acc)
        for j in range(3):
            arrow(c, 1190, 380 + j * 80, 1440, 460, INK2, acc, 4, 14, ep(t, C["13.c"] + 0.8 + j * 0.4, 0.5))
        text(c, "cada pessoa: UMA data", 1340, 580, 28, "black", INK2, acc)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        rrect(c, 1000, 650, 680, 150, 26, mix("#FFFFFF", PURPLE, 0.10), ad)
        conferido(c, "2 flechas CHEGANDO: pode", 1060, 710, ad, True, 32)
        conferido(c, "2 flechas SAINDO: não", 1060, 770, ad, False, 32)


# ======================================================================
# bloco g — na tabela
# ======================================================================

TAB_OK = [("1", "4"), ("2", "4"), ("3", "9")]


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "E NA TABELA?", "A MESMA REGRA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    tabela(c, 300, 260, [("1", "3"), ("2", "5"), ("2", "8")], aa, destaque=(1, 2) if t >= C["14.b"] else ())
    if aa > 0:
        text(c, "entradas", 390, 600, 26, "black", BLUE, aa)
        text(c, "saídas", 570, 600, 26, "black", GREEN, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        selo(c, 480, 700, ab, "MESMO x · y DIFERENTE", RED, -4, 30)
        text(c, "NÃO É", 480, 800, 40, "black", RED, ab)
    acc = ep(t, C["14.c"], 0.5)
    tabela(c, 1200, 260, TAB_OK, acc, destaque=(0, 1), cor_dest=GREEN)
    if acc > 0:
        selo(c, 1380, 700, acc, "MESMO y: TUDO BEM", GREEN, -4, 30)
        text(c, "flechas chegando", 1380, 800, 34, "black", GREEN, acc)


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CACE O x REPETIDO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    K.atalho(c, 220, 210, 820, 140, "ATALHO", ["olhe SÓ a coluna do x"], aa, 40)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        tabela(c, 340, 400, [("1", "2"), ("2", "4"), ("3", "6")], ab)
        # dedo descendo
        yy = lerp(470, 640, ep(t, C["15.b"] + 0.3, 1.4))
        c.drawCircle(310, yy, 16, paint(GREEN, ab))
        conferido(c, "nenhum repetido: É FUNÇÃO", 260, 740, ep(t, C["15.b"] + 1.8, 0.4), True, 30)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        tabela(c, 1220, 260, [("1", "2"), ("4", "7"), ("4", "9")], acc, destaque=(1, 2))
        text(c, "achou repetido?", 1400, 620, 34, "black", AMBER, acc)
        text(c, "olhe os dois y", 1400, 670, 34, "black", INK, acc)
        conferido(c, "diferentes: NÃO É", 1250, 760, ep(t, C["15.c"] + 1.8, 0.4), False, 32)


# ======================================================================
# nós fazemos
# ======================================================================

TAB_EX = [("1", "3"), ("2", "5"), ("2", "6"), ("3", "7")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "CACE O x REPETIDO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    alf = [ep(t, C["16.a"] + k * 1.5, 0.4) for k in range(4)]
    dest = (1, 2) if t >= C["17.a"] + 1.2 else ()
    tabela(c, 380, 230, TAB_EX, aa, destaque=dest, alfas=alf, rh=80, size=44)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0 and t < C["17"]:
        text(c, "é uma FUNÇÃO?", 1280, 360, 52, "black", INK, ab)
    pause_timer(c, t, C["16.end"] - 1.9, 1280, 540)
    if t < C["17"]:
        return
    a1 = ep(t, C["17.a"], 0.4)
    if a1 > 0:
        yy = lerp(350, 590, ep(t, C["17.a"], 1.4))
        c.drawCircle(350, yy, 16, paint(GREEN, a1))
        pill(c, "o 2 aparece DUAS vezes", 1280, 330, AMBER, size=32, a=ep(t, C["17.a"] + 1.2, 0.4), anchor="center")
    ab2 = ep(t, C["17.b"], 0.5)
    if ab2 > 0:
        diagrama(c, 1280, 560, ab2, [(0, 0), (0, 1)], A=["2"], B=["5", "6"], h=240, gapx=320, larg=130,
                 ruim_A=0, ruim_setas=((0, 0), (0, 1)), prog_=ep(t, C["17.b"] + 0.3, 1.0))
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        selo(c, 1280, 780, acc, "NÃO É FUNÇÃO", RED, -4, 38)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Função: a cada entrada, uma única saída.",
          "Duas flechas chegando pode; duas flechas saindo, não.",
          "Todo elemento do conjunto de partida precisa de flecha."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Achar que duas flechas CHEGANDO impedem a função", "a palavra “único” fica martelando",
          "o único é a saída de CADA entrada: duas entradas com a mesma saída PODE"),
         ("Achar que tudo bem um elemento de A ficar SEM flecha", "ninguém ficou com duas saídas",
          "TODO elemento do conjunto de partida precisa de flecha"),
         ("Inverter quem depende de quem: “o aluno é função da altura”", "cada aluno TEM uma altura",
          "isso diz que a ALTURA é função do aluno; o contrário, não")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


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


ALTS6 = [("A", "y é o aluno da turma cuja altura é x cm.", "", GREEN),
         ("B", "y é a área de um quadrado de lado x cm.", "lado → área (x²)", RED),
         ("C", "y é o preço pago por x quilogramas de arroz.", "massa → preço", RED),
         ("D", "y é a temperatura registrada no instante x.", "instante → temperatura", RED),
         ("E", "y é o perímetro de um quadrado de lado x cm.", "lado → perímetro (4x)", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · EU FAÇO", "QUANDO y NÃO É FUNÇÃO DE x", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("Em uma turma, há alunos com a mesma altura. Em qual das situações a seguir a grandeza y "
                           "NÃO é função da grandeza x?", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS6, 980, 230, 720, 26, C["23.ok"], "A", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["22.end"] - 1.9, 540, yend + 140)
    if C["23"] <= t < C["24"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["23"], 0.4))
        pill(c, "PERGUNTA MÁGICA: sei x → digo y sem dúvida?", 540, y0 + 50, GREEN, size=22, a=ep(t, C["23"], 0.4),
             anchor="center")
        aa = ep(t, C["23.a"], 0.4)
        if aa > 0:
            text(c, "A: sei a ALTURA → sei o ALUNO?", 540, y0 + 130, 28, "black", INK, aa)
        diagrama(c, 540, y0 + 290, ep(t, C["23.b"], 0.4), [(0, 0), (0, 1)], A=["1,70"], B=["Ana", "Bruno"],
                 h=200, gapx=300, larg=150, size=30, ruim_A=0, ruim_setas=((0, 0), (0, 1)),
                 prog_=ep(t, C["23.b"] + 0.2, 1.0), nomes=("altura", "aluno"))
    if t >= C["24"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["24"], 0.4))
        text(c, "nas outras, a entrada DETERMINA a saída", 540, y0 + 60, 26, "black", GREEN, ep(t, C["24"], 0.4))
        aa = ep(t, C["24.a"], 0.4)
        diagrama(c, 540, y0 + 260, aa, [(0, 0), (1, 0)], A=["8 h", "15 h"], B=["22 °C"], h=200, gapx=300,
                 larg=150, size=30, prog_=ep(t, C["24.a"] + 0.2, 1.0), nomes=("instante", "temperatura"),
                 cor_seta=GREEN)
        if aa > 0:
            text(c, "temperatura repetida = flechas CHEGANDO: pode", 540, y0 + 420, 22, "black", GREEN, aa)


ALTS1 = [("A", "apenas I.", "descarta a III sem motivo", RED), ("B", "apenas II.", "aceita a II: flechas saindo", RED),
         ("C", "I e III.", "", GREEN), ("D", "II e III.", "aceita a II: flechas saindo", RED),
         ("E", "I, II e III.", "ignora as duas disciplinas", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · VOCÊ FAZ", "RECONHECER UMA FUNÇÃO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("A secretaria de uma escola analisou três relações:", INK),
                          ("I. Cada aluno matriculado → sua data de nascimento.", BLUE),
                          ("II. Cada professor → as disciplinas que leciona (alguns lecionam duas).", BLUE),
                          ("III. Cada número da lista de chamada → o aluno com esse número.", BLUE),
                          ("Considerando o primeiro conjunto como domínio, são funções", INK)], a0, 236, 25, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
         align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 38, C["26.ok"], "C", cues_in, cues_x, gap=30)
    if t < C["26"]:
        pause_timer(c, t, C["25.end"] - 1.9, 1340, 760)
        return
    # resolução por cima do enunciado
    y0 = 236
    _painel(c, y0 - 30, ep(t, C["26"], 0.4))
    itens = [("26.a", "I", ["aluno"], ["data"], [(0, 0)], True, "cada aluno: UMA data"),
             ("26.b", "II", ["prof."], ["Mat.", "Fís."], [(0, 0), (0, 1)], False, "prof. com 2 disciplinas"),
             ("26.c", "III", ["nº 7"], ["Ana"], [(0, 0)], True, "cada número: UM aluno")]
    for k, (cue, rom, A_, B_, st, ok, leg) in enumerate(itens):
        ak = ep(t, C[cue], 0.4)
        if ak <= 0:
            continue
        y = y0 + 70 + k * 190
        text_mid(c, rom, 230, y + 10, 40, "black", PURPLE, ak)
        diagrama(c, 470, y + 10, ak, st, A=A_, B=B_, h=150, gapx=230, larg=120, size=26, nomes=("", ""),
                 ruim_A=None if ok else 0, ruim_setas=() if ok else tuple(st), prog_=ep(t, C[cue] + 0.3, 0.8))
        check_icon(c, 720, y + 10, 26, ak, GREEN if ok else RED, "check" if ok else "x")
        para(c, leg, 760, y, 22, "black", GREEN if ok else RED, ak, 140, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DOMÍNIO, CONTRADOMÍNIO E IMAGEM", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        K.mdraw(c, "x^2", 300, 280, 60, PURPLE, aa)
        text(c, "recebe só 1, 2 e 3", 420, 294, 34, "black", INK, aa, align="left")
    ab = ep(t, C["29.b"], 0.5)
    diagrama(c, 760, 560, aa, [(0, 0), (1, 1), (2, 3)], A=["1", "2", "3"], B=["1", "4", "7", "9"], h=380, gapx=420,
             prog_=ep(t, C["29.b"] + 0.6, 1.8), size=44)
    if ab > 0:
        rrect(c, 1260, 380, 420, 120, 24, mix("#FFFFFF", AMBER, 0.3), ab)
        text_mid(c, "o 7 sai alguma vez?", 1470, 440, 36, "black", AMBER, ab)
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        selo(c, 1470, 600, acc, "QUEM NUNCA SAI TEM NOME", PURPLE, -4, 30)
    pill(c, "ep. 2 · domínio, contradomínio e imagem", W / 2, 810, PURPLE, size=30, a=ep(t, C["29.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Que máquina do seu dia a dia é uma função?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, maquina=b_maquina,
              definicao=b_definicao, variaveis=b_variaveis, depende=b_depende, magica=b_magica, flechas=b_flechas,
              diagramas=b_diagramas, chegando=b_chegando, tabela=b_tabela, atalho=b_atalho, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q6=b_q6, q1=b_q1, ponte=b_ponte, cta=b_cta)
