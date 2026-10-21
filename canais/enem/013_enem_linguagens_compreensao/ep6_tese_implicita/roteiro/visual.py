"""Visual — Compreensão Global e Tese, Episódio 6: A tese implícita (tema claro).
Analogia: o autor de um texto implícito é um FOTÓGRAFO (câmera + visor com cantoneiras): a opinião está na ESCOLHA
do que enquadrar, do que fica de fora e do que vai lado a lado.
Dona Lurdes: texto inteiro em cima; embaixo, tela dividida — à esquerda a TV anunciando "em segundos", à direita um
relógio que corre das 5h às 11h enquanto a voz lê.
Ironia: "Admiro" gira e vira do avesso para "Critico" (no esquema do bloco E e em cima das palavras da Questão 4).
Cores: azul = tese/definição · verde = pista/palavra-sinal · âmbar = armadilha · vermelho = erro · roxo = regra.
Peças reaproveitadas dos eps. 1 a 5 (V1…V5).
"""
import importlib.util
import json
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

HERE = Path(__file__).resolve().parent
SERIE = HERE.parent.parent


def _load(nome, path):
    spec = importlib.util.spec_from_file_location(nome, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


V5 = _load("visual_ep5", SERIE / "ep5_pistas" / "roteiro" / "visual.py")
V4, V3, V2, V1 = V5.V4, V5.V3, V5.V2, V5.V1
motor.set_theme("claro")
try:   # a leitura (classe do ep. 2) usa os tempos deste episódio
    V2._SC = {s["id"]: s for s in json.load(open(HERE.parent / "audio" / "tempos.json", encoding="utf-8"))["scenes"]}
except Exception:
    V2._SC = {}

MARCA = ""
ARQUIVO_FINAL = "enem_linguagens_compreensao_ep6_tese_implicita.mp4"
CARD_R = (140, 150, 1640, 690)

wrap, para, which, frame, head_seq, boxed, regra, selo, pause_timer = (
    V1.wrap, V1.para, V1.which, V1.frame, V1.head_seq, V1.boxed, V1.regra, V1.selo, V1.pause_timer)
notas, Leitura, caixa, alternativas = V2.notas, V2.Leitura, V4.caixa, V4.alternativas
_norm = V2._norm


# ======================================================================
# peças: câmera, visor, foto (prédio × favela), relógio, TV, balão, virada
# ======================================================================

def camera(c, cx, cy, s, a, col=INK):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    rrect(c, -60, -52, 44, 18, 6, col, a)
    rrect(c, -100, -38, 200, 120, 22, col, a, shadow=True)
    c.drawCircle(0, 22, 44, paint("#FFFFFF", a))
    c.drawCircle(0, 22, 34, paint(BLUE, a))
    c.drawCircle(0, 22, 18, paint("#1E3A8A", a))
    c.drawCircle(-8, 14, 6, paint("#FFFFFF", a * 0.8))
    rrect(c, 58, -24, 26, 14, 4, AMBER, a)
    c.restore()


def visor(c, x, y, w, h, a, col=INK, L=46, sw=7):
    """cantoneiras de enquadramento"""
    if a <= 0:
        return
    for (px, py, dx, dy) in ((x, y, 1, 1), (x + w, y, -1, 1), (x, y + h, 1, -1), (x + w, y + h, -1, -1)):
        line(c, px, py, px + dx * L, py, col, a, sw)
        line(c, px, py, px, py + dy * L, col, a, sw)


def predio(c, x, base, w, h, a):
    if a <= 0:
        return
    rrect(c, x, base - h, w, h, 6, "#5B7FA6", a)
    rrect(c, x + w * 0.3, base - h - 26, w * 0.4, 30, 4, "#4A6A8E", a)
    cols, rows = 4, int(h / 46)
    for i in range(cols):
        for j in range(rows):
            ww = (w - 30) / cols - 8
            rrect(c, x + 15 + i * (ww + 8), base - h + 20 + j * 46, ww, 28, 3, "#BFD7F0" if (i + j) % 3 else "#E8F1FB", a)


CASAS = [(0, 0, 70, 58, "#D97757"), (64, 0, 80, 70, "#E8B04B"), (138, 0, 66, 52, "#9CB380"), (0, 58, 60, 48, "#C9A27E"),
         (56, 70, 74, 50, "#8FA7C9"), (126, 52, 70, 56, "#E39B7B"), (20, 106, 66, 44, "#B5B08A"), (84, 120, 60, 42, "#D9A066")]


def favela(c, x, base, s, a):
    if a <= 0:
        return
    for dx, dy, w, h, col in CASAS:
        X, Y, Wd, Hd = x + dx * s, base - (dy + h) * s, w * s, h * s
        rrect(c, X, Y, Wd, Hd, 2, col, a)
        rrect(c, X + Wd * 0.2, Y + Hd * 0.3, Wd * 0.22, Hd * 0.3, 2, "#3F3A36", a * 0.8)
        rrect(c, X + Wd * 0.58, Y + Hd * 0.3, Wd * 0.22, Hd * 0.3, 2, "#3F3A36", a * 0.8)
        line(c, X - 2, Y, X + Wd + 2, Y, "#7A6A5A", a, 4)


def foto(c, x, y, w, h, a, a_predio=1.0, a_favela=1.0):
    """a foto sem legenda: prédio de luxo colado na favela"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 10, "#FFFFFF", a, shadow=True)
    rrect(c, x + 16, y + 16, w - 32, h - 32, 6, "#DCE9F5", a)
    base = y + h - 40
    rrect(c, x + 16, base, w - 32, 24, 0, "#A8B3A0", a)
    predio(c, x + w * 0.16, base, w * 0.28, h * 0.72, a * a_predio)
    favela(c, x + w * 0.48, base, w / 520, a * a_favela)


def relogio(c, cx, cy, r, hora, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r + 10, paint(INK, a))
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    for k in range(12):
        ang = math.radians(k * 30 - 90)
        r0 = r * (0.80 if k % 3 == 0 else 0.86)
        line(c, cx + r0 * math.cos(ang), cy + r0 * math.sin(ang), cx + r * 0.94 * math.cos(ang), cy + r * 0.94 * math.sin(ang),
             INK, a, 6 if k % 3 == 0 else 3)
    ah = math.radians((hora % 12) * 30 - 90)
    am = math.radians((hora % 1) * 360 - 90)
    line(c, cx, cy, cx + r * 0.5 * math.cos(ah), cy + r * 0.5 * math.sin(ah), INK, a, 12)
    line(c, cx, cy, cx + r * 0.76 * math.cos(am), cy + r * 0.76 * math.sin(am), RED, a, 6)
    c.drawCircle(cx, cy, 10, paint(INK, a))


def tv(c, cx, cy, w, h, a, a_txt=1.0):
    if a <= 0:
        return
    line(c, cx - w * 0.25, cy + h / 2, cx - w * 0.32, cy + h / 2 + 50, INK2, a, 8)
    line(c, cx + w * 0.25, cy + h / 2, cx + w * 0.32, cy + h / 2 + 50, INK2, a, 8)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 18, INK, a, shadow=True)
    rrect(c, cx - w / 2 + 16, cy - h / 2 + 16, w - 32, h - 32, 8, "#2E5BD8", a)
    # celular com o aplicativo
    rrect(c, cx - w / 2 + 50, cy - 70, 90, 150, 14, "#FFFFFF", a)
    for j in range(3):
        rrect(c, cx - w / 2 + 64, cy - 46 + j * 36, 62, 22, 5, mix("#2E5BD8", "#FFFFFF", 0.6), a)
    text(c, "marque consultas", cx + 60, cy - 18, 28, "bold", "#FFFFFF", a * a_txt)
    text(c, "“em segundos”", cx + 60, cy + 40, 46, "black", "#FFE58A", a * a_txt)


def balao(c, s, x, y, w, a, size=40, col="#FFFFFF", fg=None, cauda=True):
    if a <= 0:
        return
    h = size * 2.1
    rrect(c, x, y, w, h, 28, col, a, shadow=True)
    if cauda:
        p = skia.Path(); p.moveTo(x + 50, y + h - 2); p.lineTo(x + 30, y + h + 34); p.lineTo(x + 100, y + h - 2)
        c.drawPath(p, paint(col, a))
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg or INK, a)


def virada(c, s1, s2, x, cy, size, u, a, col1=GREEN, col2=RED, align="center", bg=None):
    """a palavra gira no eixo horizontal e volta do avesso: s1 → s2"""
    if a <= 0:
        return
    u = ease_io(clamp(u))
    k = math.cos(math.pi * u)
    s, col = (s1, col1) if k >= 0 else (s2, col2)
    w = text_w(s, "black", size)
    x0 = x - w / 2 if align == "center" else x
    c.save(); c.translate(x0 + w / 2, cy); c.scale(1, max(abs(k), 0.02))
    if bg:
        rrect(c, -w / 2 - 10, -size * 0.75, w + 20, size * 1.5, 8, bg, a)
    text_mid(c, s, 0, 0, size, "black", col, a)
    c.restore()


def virada_na_palavra(c, t, L, lay_args, si, palavra, u, a=1.0):
    """vira do avesso uma palavra que já está na leitura (Admiro → Critico)"""
    if u <= 0 or a <= 0:
        return
    x, y, maxw, size, lh = lay_args
    for w, s_i, wi, xx, yy, ww in L.layout(x, y, maxw, size, lh):
        if s_i == si and _norm(w) == _norm(palavra):
            rrect(c, xx - 6, yy - size * 0.9, ww + 12, size * 1.22, 6, "#FFFFFF", a)
            u2 = ease_io(clamp(u)); k = math.cos(math.pi * u2)
            s, col = (w, GREEN) if k >= 0 else ("Critico", RED)
            c.save(); c.translate(xx + ww / 2, yy - size * 0.34); c.scale(1, max(abs(k), 0.02))
            text_mid(c, s, 0, 0, size, "black", col, a)
            c.restore()
            return


def texto_fake(c, x, y, w, n, a, col=LINE, lh=30):
    for j in range(n):
        line(c, x, y + j * lh, x + w - (j % 3) * 40, y + j * lh, col, a, 10)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "LINGUAGENS ENEM", "A TESE IMPLÍCITA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    rrect(c, 300, 230, 520, 420, 18, "#FFFFFF", aa, shadow=True)
    texto_fake(c, 350, 290, 420, 10, aa)
    selo(c, 560, 600, aa * ep(t, C["01.a"] + 0.8, 0.4), "NENHUMA FRASE DE OPINIÃO", RED, -4, 24)
    ab = ep(t, C["01.b"], 0.5)
    arrow(c, 860, 440, 1010, 440, BLUE, ab, 6, 22)
    rrect(c, 1050, 330, 560, 220, 22, mix("#FFFFFF", BLUE, 0.10), ab)
    text(c, "e mesmo assim", 1330, 405, 32, "bold", INK2, ab)
    text(c, "DEFENDE UMA IDEIA", 1330, 470, 44, "black", BLUE, ab)
    for k, s in enumerate(("crônicas", "charges", "anúncios")):
        pill(c, s, 640 + k * 320, 760, GREEN, size=30, a=ep(t, C["01.c"] + 0.4 * k, 0.4), anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "reconstruir a TESE ESCONDIDA", "de um texto que não diz “eu defendo”"),
            ("02.b", "sem inventar nada", "só o que o texto AUTORIZA")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")
        text(c, sub, 400, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRANÇAS", "EPISÓDIOS 1, 3 E 4", BLUE)
    rows = [("03.a", "EP. 1", "TESE", "o que o texto afirma", BLUE),
            ("03.b", "EP. 4", "TESE IMPLÍCITA", "não está escrita em frase nenhuma", BLUE),
            ("03.c", "EP. 3", "CONTRADIÇÃO", "dizer o contrário do texto", RED),
            ("03.d", "EP. 3", "EXTRAPOLAÇÃO", "ir além do texto", AMBER)]
    for k, (cue, ep_, s, sub, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 250 + k * 130 + d
        if a <= 0:
            continue
        rrect(c, 300, y, 1320, 104, 16, mix("#FFFFFF", col, 0.07), a)
        c.drawRect(skia.Rect.MakeXYWH(300, y, 10, 104), paint(col, a))
        pill(c, ep_, 340, y + 52, INK2, size=22, a=a, bounds=(0, 1920))
        text(c, s, 470, y + 64, 40, "black", col, a, align="left")
        text(c, sub, 1580, y + 62, 30, "bold", INK2, a, align="right")


def b_amigo(c, t, C, B):
    frame(c, t, B["start"], "IMAGINE A CENA", "“NOSSA, QUE PONTUAL!”", BLUE)
    a0 = ep(t, C["04.a"], 0.5)
    hora = 8 + clamp(prog(t, C["04.a"], 1.6))
    relogio(c, 420, 400, 120, hora, a0)
    pill(c, "+1 HORA de atraso", 420, 590, RED, size=30, a=a0, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["04.b"], 0.5)
    balao(c, "Nossa, que pontual!", 700, 250, 620, ab, 46)
    ac = ep(t, C["04.c"], 0.4)
    text(c, "ele não disse: “você se atrasou”", 1010, 470, 32, "bold", INK2, ac)
    text(c, "mas você ENTENDEU", 1010, 520, 36, "black", GREEN, ac)
    caixa(c, 700, 600, 470, 150, BLUE, ep(t, C["04.d"], 0.4), "", 26)
    ad = ep(t, C["04.d"], 0.4)
    text(c, "EXPLÍCITO", 935, 660, 34, "black", BLUE, ad)
    text(c, "escrito com todas as letras", 935, 710, 24, "bold", INK2, ad)
    ae = ep(t, C["04.e"], 0.4)
    caixa(c, 1200, 600, 470, 150, BLUE, ae, "", 26, fill=0.2)
    text(c, "IMPLÍCITO", 1435, 660, 34, "black", BLUE, ae)
    text(c, "não escrito, mas dá para entender", 1435, 710, 24, "bold", INK2, ae)


def b_foto(c, t, C, B):
    frame(c, t, B["start"], "AGORA, UMA FOTO", "SEM NENHUMA PALAVRA", BLUE)
    a0 = ep(t, C["05.t"], 0.5)
    foto(c, 260, 210, 760, 540, a0, ep(t, C["05.a"], 0.5), ep(t, C["05.b"], 0.5))
    pill(c, "sem legenda", 640, 790, LIGHT, INK, size=26, a=ep(t, C["05.c"], 0.4), anchor="center", bounds=(0, 1920))
    ad = ep(t, C["05.d"], 0.4)
    text(c, "mesmo assim, ela diz algo", 1360, 280, 34, "black", INK, ad)
    text(c, "sobre DESIGUALDADE", 1360, 330, 34, "black", BLUE, ad)
    ae = ep(t, C["05.e"], 0.4)
    caixa(c, 1110, 390, 500, 130, BLUE, ae)
    text(c, "INFERIR", 1360, 440, 34, "black", BLUE, ae)
    text(c, "tirar uma conclusão a partir de pistas", 1360, 488, 22, "bold", INK2, ae)
    af = ep(t, C["05.f"], 0.5)
    camera(c, 1360, 640, 0.9, af)
    text(c, "quem falou? o FOTÓGRAFO", 1360, 790, 30, "black", INK, af)
    visor(c, 300, 250, 680, 460, af * 0.9, AMBER)


def b_fotografo(c, t, C, B):
    frame(c, t, B["start"], "A IMAGEM DA AULA", "O AUTOR É UM FOTÓGRAFO", PURPLE)
    aa = ep(t, C["06.a"], 0.5)
    camera(c, 420, 430, 1.4, aa)
    ab = ep(t, C["06.b"], 0.4)
    text(c, "não diz a opinião", 420, 640, 34, "black", RED, ab)
    rows = ["o que ENQUADRAR", "o que deixa DE FORA", "o que põe LADO A LADO"]
    for k, s in enumerate(rows):
        a, d = rise(t, C["06.c"] + 0.9 * k)
        y = 290 + k * 120 + d
        visor(c, 760, y - 44, 70, 70, a, GREEN, 20, 5)
        text(c, s, 870, y + 4, 40, "black", INK, a, align="left")
    regra(c, "A opinião está na ESCOLHA.", 740, ep(t, C["06.d"], 0.5), 48)


# ======================================================================
# bloco A — onde a opinião aparece
# ======================================================================

def b_generos(c, t, C, B):
    frame(c, t, B["start"], "QUEM ESCREVE", "ASSIM?", BLUE)
    data = [("07.a", "CRÔNICA", "texto curto que conta uma cena do dia a dia"),
            ("07.b", "CHARGE", "desenho de humor que comenta uma notícia"),
            ("07.c", "ANÚNCIO", "a propaganda")]
    for k, (cue, s, sub) in enumerate(data):
        a, d = rise(t, C[cue])
        x = 240 + k * 500
        if a <= 0:
            continue
        rrect(c, x, 220 + d, 440, 380, 20, "#FFFFFF", a, shadow=True)
        cx, cy = x + 220, 340 + d
        if k == 0:
            texto_fake(c, cx - 120, cy - 60, 240, 5, a, LIGHT, 26)
        elif k == 1:
            rrect(c, cx - 120, cy - 80, 240, 160, 8, mix("#FFFFFF", AMBER, 0.15), a)
            c.drawCircle(cx - 30, cy + 10, 34, paint(INK, a, stroke=5))
            c.drawCircle(cx - 42, cy + 2, 4, paint(INK, a)); c.drawCircle(cx - 18, cy + 2, 4, paint(INK, a))
            balao(c, "...", cx + 10, cy - 70, 100, a, 22, cauda=False)
        else:
            rrect(c, cx - 120, cy - 70, 240, 140, 14, RED, a)
            text_mid(c, "OFERTA!", cx, cy, 44, "black", "#FFFFFF", a)
        text(c, s, cx, 500 + d, 40, "black", BLUE, a)
        para(c, sub, cx, 548 + d, 24, "bold", INK2, a, 380, 30, align="center")
    ad = ep(t, C["07.d"], 0.4)
    text(c, "“eu defendo que...”", W / 2, 720, 44, "black", INK2, ad)
    strike(c, W / 2 - 220, 705, W / 2 + 220, 705, ad, RED, prog(t, C["07.d"] + 0.4, 0.5))
    pill(c, "então, onde está a opinião?", W / 2, 800, BLUE, size=28, a=ep(t, C["07.d"] + 2.4, 0.4), anchor="center")


ONDE = [("08", "SELEÇÃO", "o que o texto escolhe mostrar e o que deixa de fora", "o enquadramento"),
        ("09", "CONTRASTE", "pôr lado a lado duas coisas que brigam entre si", "luxo × favela"),
        ("10", "TOM", "o jeito de falar: sério, exagerado, debochado", "“que pontual!”")]


def b_onde(c, t, C, B):
    head_seq(c, t, C, [("08", "ONDE ESTÁ A OPINIÃO? 1", "NA SELEÇÃO", GREEN), ("09", "ONDE ESTÁ A OPINIÃO? 2", "NO CONTRASTE", GREEN),
                       ("10", "ONDE ESTÁ A OPINIÃO? 3", "NO TOM", GREEN)])
    card(c, *CARD_R)
    for k, (sid, s, defi, ex) in enumerate(ONDE):
        a, d = rise(t, C[f"{sid}.a"])
        x = 250 + k * 500
        cx = x + 210
        if a <= 0:
            continue
        cur = which(t, C, ["08", "09", "10"]) == sid
        rrect(c, x, 210 + d, 420, 560, 22, mix("#FFFFFF", GREEN, 0.10 if cur else 0.03), a, shadow=cur)
        cy = 340 + d
        if k == 0:
            visor(c, cx - 110, cy - 80, 220, 160, a, GREEN, 36, 7)
            foto(c, cx - 80, cy - 55, 160, 110, a * 0.9)
        elif k == 1:
            predio(c, cx - 110, cy + 70, 70, 140, a)
            text_mid(c, "×", cx, cy, 70, "black", GREEN, a)
            favela(c, cx + 30, cy + 70, 0.42, a)
        else:
            balao(c, "que pontual!", cx - 150, cy - 70, 300, a, 32)
        text(c, s, cx, 500 + d, 44, "black", GREEN, a)
        para(c, defi, cx, 550 + d, 26, "bold", INK2, a, 360, 34, align="center")
        ab = ep(t, C[f"{sid}.b"], 0.4)
        pill(c, ex, cx, 720 + d, BLUE, size=24, a=a * ab, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco B — eu faço: Dona Lurdes
# ======================================================================

LURDES = Leitura(
    [("11", "f1", "c1", "Na sala de espera do posto de saúde, a televisão anunciava um aplicativo para marcar consultas “em segundos”."),
     ("12", "f2", "c2", "Dona Lurdes, que chegara às cinco da manhã para pegar senha, assistiu ao anúncio inteiro."),
     ("12", "f3", "c3", "Às onze, foi chamada.")],
    [(0, "“em segundos”.", "box", GREEN, None),
     (1, "às cinco da manhã", "box", GREEN, None),
     (2, "Às onze,", "box", GREEN, None),
     (1, "assistiu ao anúncio inteiro.", "under", INK2, "12.c2")])
LARGS = (230, 260, 1460, 34, 50)


def b_lurdes(c, t, C, B):
    head_seq(c, t, C, [("11", "EU FAÇO", "O POSTO DE SAÚDE", BLUE), ("13", "EU FAÇO", "O CONTRASTE", GREEN),
                       ("14", "EU FAÇO", "A TESE IMPLÍCITA", BLUE)])
    card(c, *CARD_R)
    LURDES.draw(c, t, C, *LARGS, ep(t, C["11.f1"] - 0.3, 0.4))
    p14 = ep(t, C["14.a"], 0.6)
    sa = 1 - p14
    # tela dividida
    aL = ep(t, C["11.f1"] + 1.0, 0.5) * sa
    tv(c, 560, 560, 520, 290, aL, ep(t, C["11.c1"], 0.4))
    pill(c, "A PROMESSA", 560, 770, GREEN, size=26, a=aL * ep(t, C["13.b"], 0.4), anchor="center", bounds=(0, 1920))
    aR = ep(t, C["12.f2"], 0.5) * sa
    T = LURDES.times(C)
    t5, t11 = C["12.f3"] - 1.2, T[2][1] + 0.2   # segura em 5h no comentário e corre até o "onze"
    hora = 5 + 6 * ease_io(clamp((t - t5) / max(t11 - t5, 0.1)))
    relogio(c, 1280, 540, 140, hora, aR)
    hh = int(hora); mm = int(round((hora - hh) * 60 / 10) * 10) % 60
    text(c, f"{hh}h{mm:02d}" if mm else f"{hh}h", 1280, 740, 40, "black", RED if hora > 10.9 else INK, aR)
    ac3 = ep(t, C["12.c3"], 0.4) * sa
    pill(c, "6 HORAS de espera", 1530, 400, RED, size=28, a=ac3, anchor="center", bounds=(0, 1920))
    pill(c, "A REALIDADE", 1280, 800, RED, size=26, a=aR * ep(t, C["13.c"], 0.4), anchor="center", bounds=(0, 1920))
    a13 = ep(t, C["13.a"], 0.4) * sa
    selo(c, 920, 470, a13 * (1 - ep(t, C["13.b"], 0.3)), "NENHUMA FRASE OPINA", RED, -4, 26)
    text_mid(c, "×", 920, 560, 110, "black", GREEN, ep(t, C["13.c"], 0.4) * sa)
    visor(c, 250, 380, 1420, 440, ep(t, C["13.d"], 0.5) * sa, AMBER, 60, 8)
    camera(c, 920, 770, 0.45, ep(t, C["13.d"], 0.5) * sa)
    # a tese
    if p14 > 0:
        rrect(c, 260, 440, 1400, 220, 22, mix("#FFFFFF", BLUE, 0.10), p14, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(260, 440, 1400, 220), 22, 22), paint(BLUE, p14, stroke=4))
        pill(c, "TESE IMPLÍCITA", 300, 440, BLUE, size=24, a=p14, bounds=(0, 1920))
        para(c, "A modernização anunciada está longe da experiência de quem de fato usa o serviço.", W / 2, 530, 42, "black",
             INK, p14, 1300, 54, align="center")
        text(c, "MODERNIZAÇÃO = deixar o serviço mais moderno, com tecnologia", W / 2, 720, 26, "bold", BLUE, ep(t, C["14.b"], 0.4))
        text(c, "a promessa da TV não chegou à cadeira da Dona Lurdes", W / 2, 790, 30, "black", INK2, ep(t, C["14.c"], 0.4))


# ======================================================================
# bloco C — o limite
# ======================================================================

def b_limite(c, t, C, B):
    head_seq(c, t, C, [("15", "O LIMITE", "DÁ PARA IR MAIS LONGE?", AMBER), ("16", "O LIMITE", "SÓ O QUE ESTÁ NA FOTO", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["15.t"], 0.5)
    rrect(c, 300, 230, 620, 330, 16, mix("#FFFFFF", BLUE, 0.08), a0)
    visor(c, 280, 210, 660, 370, a0, BLUE, 50, 7)
    para(c, "A modernização anunciada está longe da experiência de quem de fato usa o serviço.", 610, 330, 32, "black", BLUE,
         a0, 540, 44, align="center")
    pill(c, "DENTRO DA FOTO", 610, 610, BLUE, size=24, a=a0, anchor="center", bounds=(0, 1920))
    rows = [("15", "“O texto defende o fim dos aplicativos.”", "o aplicativo saiu mal na história", "não pede o fim de nada"),
            ("16", "“O posto é mal administrado.”", "seis horas de espera é muito", "não diz por que a espera foi longa")]
    for k, (sid, s, parece, porque) in enumerate(rows):
        a, d = rise(t, C[f"{sid}.a"])
        y = 230 + k * 280 + d
        if a <= 0:
            continue
        line(c, 940, 395, 1010, y + 60, LIGHT, a, 3, dash=[10, 8])
        rrect(c, 1010, y, 640, 250, 18, "#FFFFFF", a, shadow=True)
        para(c, s, 1040, y + 50, 30, "black", INK, a, 580, 38)
        ab = ep(t, C[f"{sid}.b"], 0.4)
        text(c, "parece certo: " + parece, 1040, y + 140, 22, "bold", AMBER, ab, align="left")
        ac = ep(t, C[f"{sid}.c"], 0.4)
        text(c, "mas o texto " + porque, 1040, y + 180, 22, "bold", INK2, ac, align="left")
        if ac > 0:
            strike(c, 1030, y + 40, 1630, y + 40, ac, RED, prog(t, C[f"{sid}.c"], 0.5))
        selo(c, 1500, y + 222, ep(t, C[f"{sid}.d"], 0.4), "EXTRAPOLAÇÃO", AMBER, -4, 24)
    pill(c, "o fotógrafo só responde pelo que está DENTRO da foto", 610, 780, PURPLE, size=24, a=ep(t, C["16.e"], 0.4),
         anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco D — as três perguntas · nós fazemos
# ======================================================================

PERG = ["O que o texto escolheu mostrar, e o que deixou de fora?", "Há contraste ou exagero? Entre o quê e o quê?",
        "Quem ou o que sai criticado ou valorizado no fim?"]


def b_perguntas(c, t, C, B):
    frame(c, t, B["start"], "PARA NÃO PASSAR DO PONTO", "AS TRÊS PERGUNTAS", PURPLE)
    for k, s in enumerate(PERG):
        a, d = rise(t, C[f"17.{'abc'[k]}"])
        y = 260 + k * 170 + d
        if a <= 0:
            continue
        rrect(c, 260, y, 1400, 130, 20, mix("#FFFFFF", PURPLE, 0.08), a)
        badge_num(c, k + 1, 330, y + 65, a, 34, bg=PURPLE)
        text(c, s, 400, y + 78, 40, "black", INK, a, align="left")


def b_nosfazemos(c, t, C, B):
    frame(c, t, B["start"], "NÓS FAZEMOS", "O AMIGO DE VOLTA", GREEN)
    a0 = ep(t, C["18.t"], 0.5)
    balao(c, "Nossa, que pontual!", 230, 220, 560, a0, 42)
    relogio(c, 510, 520, 100, 9, a0)
    pill(c, "+1 HORA de atraso", 510, 670, RED, size=26, a=a0, anchor="center", bounds=(0, 1920))
    rows = [("18.a", "O QUE ESCOLHEU MOSTRAR?", "a pontualidade"),
            ("18.b", "HÁ CONTRASTE?", "o elogio × uma hora de atraso"),
            ("18.c", "QUEM SAI CRITICADO?", "quem chegou atrasado")]
    for k, (cue, q, r_) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 230 + k * 140 + d
        if a <= 0:
            continue
        rrect(c, 900, y, 760, 116, 16, "#F7F7F5", a)
        badge_num(c, k + 1, 950, y + 58, a, 22, bg=PURPLE)
        text(c, q, 990, y + 46, 24, "black", PURPLE, a, align="left")
        text(c, r_, 990, y + 92, 32, "black", RED if k == 2 else INK, a, align="left")
    ad = ep(t, C["18.d"], 0.4)
    pill(c, "as palavras ELOGIAM", 1080, 700, GREEN, size=28, a=ad, anchor="center", bounds=(0, 1920))
    pill(c, "a mensagem CRITICA", 1480, 700, RED, size=28, a=ep(t, C["18.d"] + 1.2, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco E — ironia ao pé da letra
# ======================================================================

def b_ironia(c, t, C, B):
    frame(c, t, B["start"], "ISSO TEM NOME", "IRONIA", RED)
    aa = ep(t, C["19.a"], 0.4)
    caixa(c, 360, 200, 1200, 70, BLUE, aa, "IRONIA = dizer uma coisa para significar outra", 30)
    ab = ep(t, C["19.b"], 0.4)
    u = prog(t, C["19.b"] + 1.0, 1.0)
    virada(c, "Admiro", "Critico", 660, 420, 110, u, ab, bg=None)
    arrow(c, 920, 420, 1040, 420, GRAY, ab, 5, 18)
    text(c, "elogia", 1180, 400, 40, "black", GREEN, ab, align="left")
    text(c, "para CRITICAR", 1180, 456, 40, "black", RED, ab, align="left")
    ac = ep(t, C["19.c"], 0.4)
    text(c, "AO PÉ DA LETRA = só o que as palavras dizem, sem o tom", W / 2, 580, 30, "black", INK2, ac)
    ad = ep(t, C["19.d"], 0.4)
    check_icon(c, 560, 660, 30, ad, RED, "x")
    text(c, "ironia ao pé da letra = CONTRADIÇÃO", 610, 676, 40, "black", RED, ad, align="left")
    pill(c, "ironia e humor: série própria", W / 2, 790, LIGHT, INK, size=22, a=ep(t, C["19.e"], 0.4), anchor="center",
         bounds=(0, 1920))


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["A opinião está na escolha: o que mostra, o que contrasta, o tom.", "Implícito não é livre: só vale o que o texto autoriza.",
          "Elogio irônico é crítica."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 230, y - 16, a, 36, bg=PURPLE)
        para(c, s, 300, y, 42, "black", INK, a, 1400, 54)


ERROS = [("21", "Achar que texto sem frase de opinião NÃO TEM TESE", "você não achou nenhum “eu acho”", "a opinião está na escolha: faça as 3 perguntas"),
         ("22", "Ler a ironia AO PÉ DA LETRA", "você repete o que o texto escreveu", "elogio irônico é crítica"),
         ("23", "Ir ALÉM do texto ao montar a tese", "a conclusão faz sentido no mundo", "só vale o que o texto autoriza")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(3):
        badge_num(c, k + 1, 880 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 330, 34, aa, RED, "x")
    para(c, err, 360, 345, 44, "black", RED, aa, 1300)
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 480, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 560, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 678, 34, ac, GREEN)
    text(c, fix, 360, 694, 42, "black", GREEN, ac, align="left")
    if sid == "22":
        virada(c, "Admiro", "Critico", 1450, 560, 60, prog(t, cue("c") + 0.6, 0.9), ac)
    if sid == "23":
        foto(c, 1400, 490, 180, 110, ac)
        visor(c, 1380, 470, 220, 150, ac, BLUE, 34, 6)


# ======================================================================
# questão 4 — você faz
# ======================================================================

Q4 = Leitura(
    [("24", "f1", "f2", "Admiro profundamente o motorista que para na vaga de idoso “só por um minutinho”."),
     ("24", "f2", "f3", "É um homem de fé: acredita que o tempo dele vale mais que o joelho alheio."),
     ("24", "f3", "f4", "Admiro também quem fura a fila do pão com um sorriso, convicto de que a pressa é um documento."),
     ("24", "f4", "g", "Gente assim nos ensina, todos os dias, que a regra é ótima — para os outros.")],
    [(0, "vaga de idoso", "under", GREEN, "26.a"),
     (2, "fura a fila do pão", "under", GREEN, "26.a"),
     (1, "homem de fé:", "under", AMBER, "28.d"),
     (3, "a regra é ótima — para os outros.", "fill", BLUE, "26.d")])
QARGS = (200, 300, 1060, 32, 50)

ALTS4 = [("A", "o elogio a pessoas que sabem aproveitar bem o próprio tempo.", "27.a", "28.a", "AO PÉ DA LETRA → CONTRADIÇÃO"),
         ("B", "a defesa de que o número de vagas para idosos seja ampliado.", "27.b", "28.b", "EXTRAPOLAÇÃO"),
         ("C", "a constatação de que as filas das padarias são desorganizadas.", "27.c", "28.c", "REDUÇÃO: o foco é quem fura"),
         ("D", "a ideia de que a fé leva as pessoas a agir com pressa.", "27.d", "28.d", "AO PÉ DA LETRA: “homem de fé”"),
         ("E", "a crítica a quem desrespeita regras de convivência por se julgar uma exceção a elas.", "27.e", None, "")]


def b_questao4(c, t, C, B):
    head_seq(c, t, C, [("24", "VOCÊ FAZ", "QUESTÃO 4 · A VAGA E A FILA", GREEN), ("25", "VOCÊ FAZ", "AS TRÊS PERGUNTAS", PURPLE),
                       ("26", "VOCÊ FAZ", "A TESE IMPLÍCITA", BLUE), ("27", "VOCÊ FAZ", "AS ALTERNATIVAS", AMBER)])
    card(c, *CARD_R)
    pill(c, "COMANDO: O texto, construído em tom irônico, tem como ideia central", 200, 200, BLUE, size=24,
         a=ep(t, C["24.a"], 0.4), bounds=(0, 1920))
    ph = ep(t, C["27"], 0.7)
    if ph < 1:
        a = 1 - ph
        Q4.draw(c, t, C, *QARGS, a * ep(t, C["24.f1"] - 0.3, 0.4))
        u = prog(t, C["26.c"], 1.0)
        for si, w in ((0, "Admiro"), (2, "Admiro")):
            virada_na_palavra(c, t, Q4, QARGS, si, w, u, a)
        pill(c, "tom IRÔNICO", 1330, 200, GREEN, size=24, a=a * ep(t, C["24.a"] + 2.4, 0.4), bounds=(0, 1920))
        notas(c, t, C, [("24.g", "ALHEIO · CONVICTO", "de outra pessoa · convencido", BLUE)], 1310, 300, 104, 430,
              a * (1 - ep(t, C["25"], 0.4)))
        # 25: as três perguntas → 26: as respostas
        a25 = ep(t, C["25"], 0.4) * a
        a26 = ep(t, C["26.a"], 0.4)
        if a25 > 0:
            for k, s in enumerate(("o que mostra?", "há contraste?", "quem sai criticado?")):
                y = 300 + k * 104
                al = a25 * (1 - a26)
                rrect(c, 1310, y - 20, 430, 84, 14, mix("#FFFFFF", PURPLE, 0.08), al)
                badge_num(c, k + 1, 1350, y + 22, al, 20, bg=PURPLE)
                text(c, s, 1385, y + 32, 28, "black", PURPLE, al, align="left")
            pause_timer(c, t, C["25.end"] - 1.7, 1525, 680, a)
        notas(c, t, C, [("26.a", "1 · MOSTRA", "vaga de idoso · fila do pão", GREEN),
                        ("26.b", "2 · CONTRASTE", "“admiro” × atitudes feias", GREEN),
                        ("26.c", "3 · VIRA DO AVESSO", "admiro = CRITICO", RED),
                        ("26.d", "A TESE", "a regra é ótima — para os outros", BLUE)], 1310, 300, 104, 430, a)
        pill(c, "se acham EXCEÇÃO às regras", 730, 790, BLUE, size=30, a=a * ep(t, C["26.e"], 0.4), anchor="center",
             bounds=(0, 1920))
    if ph > 0:
        Q4.draw(c, t, C, 190, 300, 600, 20, 30, ph * 0.9)
        for si, w in ((0, "Admiro"), (2, "Admiro")):
            virada_na_palavra(c, t, Q4, (190, 300, 600, 20, 30), si, w, 1.0, ph)
        pill(c, "crítica a quem se acha EXCEÇÃO", 190, 620, BLUE, size=20, a=ph, bounds=(0, 1920))
        aok = alternativas(c, t, C, ALTS4, "28.ok", 920, 290, 760, ph, 22)
        pause_timer(c, t, C["27.end"] - 1.7, 490, 760, ph)
        result_box(c, "Letra E", 490, 790, 50, aok, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

PECAS = ["tema e tese", "resumo", "armadilhas", "onde está", "as pistas", "implícita"]


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "JUNTANDO TUDO", PURPLE)
    a0 = ep(t, C["30.t"], 0.5)
    text(c, "você viu todas as peças da compreensão global", W / 2, 250, 36, "black", INK, a0)
    for k, s in enumerate(PECAS):
        a = a0 * ep(t, C["30.t"] + 0.3 * k, 0.3)
        x = 270 + k * 235
        rrect(c, x, 320, 210, 150, 18, mix("#FFFFFF", BLUE, 0.10), a, shadow=True)
        text(c, f"EP. {k + 1}", x + 105, 375, 24, "black", BLUE, a)
        text(c, s, x + 105, 425, 26, "black", INK, a)
    rows = [("30.a", "juntamos tudo"), ("30.b", "caçamos as pegadinhas"), ("30.c", "questões novas")]
    for k, (cue, s) in enumerate(rows):
        pill(c, s, 480 + k * 480, 590, [BLUE, AMBER, GREEN][k], INK if k == 1 else None, size=30, a=ep(t, C[cue], 0.4),
             anchor="center", bounds=(0, 1920))
    pill(c, "ep. 7 · estratégia e revisão", W / 2, 760, PURPLE, size=34, a=ep(t, C["30.a"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"], "Qual foi o elogio mais irônico que você já ouviu?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, amigo=b_amigo, foto=b_foto, fotografo=b_fotografo,
              generos=b_generos, onde=b_onde, lurdes=b_lurdes, limite=b_limite, perguntas=b_perguntas,
              nosfazemos=b_nosfazemos, ironia=b_ironia, recap=b_recap, erros=b_erros, questao4=b_questao4,
              ponte=b_ponte, cta=b_cta)
