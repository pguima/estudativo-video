"""Visual — Compreensão Global e Tese, Episódio 5: As pistas que entregam a tese (tema claro).
Analogia: as palavras-sinal são PLACAS DE TRÂNSITO (verdes = pista): CURVA (losango), CHEGADA (retângulo com bandeira),
OPINIÃO (círculo com "!"). Na leitura, cada palavra-sinal vira uma plaquinha que surge quando é dita.
Questão 7: parágrafos separados, com etiqueta lateral que se escreve (apresenta o problema / explica por quê / propõe solução).
Cores: azul = tese/definição · verde = pista/palavra-sinal · âmbar = armadilha · vermelho = erro · roxo = regra.
Peças reaproveitadas dos eps. 1 a 4 (V1…V4).
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


V4 = _load("visual_ep4", SERIE / "ep4_onde_esta_a_tese" / "roteiro" / "visual.py")
V3, V2, V1 = V4.V3, V4.V2, V4.V1
motor.set_theme("claro")
try:   # a leitura (classe do ep. 2) usa os tempos deste episódio
    V2._SC = {s["id"]: s for s in json.load(open(HERE.parent / "audio" / "tempos.json", encoding="utf-8"))["scenes"]}
except Exception:
    V2._SC = {}

MARCA = ""
ARQUIVO_FINAL = "enem_linguagens_compreensao_ep5_pistas.mp4"
CARD_R = (140, 150, 1640, 690)

wrap, para, which, frame, head_seq, boxed, regra, selo, pause_timer = (
    V1.wrap, V1.para, V1.which, V1.frame, V1.head_seq, V1.boxed, V1.regra, V1.selo, V1.pause_timer)
wa_bubble, notas, Leitura, colored, caixa, alternativas = V2.wa_bubble, V2.notas, V2.Leitura, V2.colored, V4.caixa, V4.alternativas
_norm = V2._norm


# ======================================================================
# placas de trânsito
# ======================================================================

PLACAS = {"curva": ("CURVA", "mas · porém · no entanto · engano", "a direção vai mudar: vem a opinião do autor"),
          "chegada": ("CHEGADA", "portanto · assim · logo · em suma", "lá vem a conclusão"),
          "opiniao": ("OPINIÃO", "é preciso · deveria · é um erro · defendo", "o autor está avaliando")}


def placa(c, x, y, kind, a, s=1.0, label=True, poste=True):
    """placa verde; (x, y) = centro da placa"""
    if a <= 0:
        return
    sc = s * (0.7 + 0.3 * ease_back(clamp(a)))
    c.save(); c.translate(x, y); c.scale(sc, sc)
    if poste:
        rrect(c, -6, 40, 12, 90, 3, "#64748B", a)
    if kind == "curva":
        c.save(); c.rotate(45)
        rrect(c, -46, -46, 92, 92, 10, GREEN, a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-40, -40, 80, 80), 7, 7), paint("#FFFFFF", a, stroke=4))
        c.restore()
        p = skia.Path(); p.moveTo(-14, 30); p.lineTo(-14, 0); p.quadTo(-14, -16, 6, -16); p.lineTo(10, -16)
        c.drawPath(p, paint("#FFFFFF", a, stroke=8, cap_round=True))
        q = skia.Path(); q.moveTo(22, -16); q.lineTo(6, -30); q.lineTo(6, -2); q.close()
        c.drawPath(q, paint("#FFFFFF", a))
    elif kind == "chegada":
        rrect(c, -62, -44, 124, 88, 10, GREEN, a, shadow=True)
        line(c, -20, 30, -20, -26, "#FFFFFF", a, 5)
        for i in range(3):
            for j in range(2):
                if (i + j) % 2 == 0:
                    rrect(c, -18 + i * 14, -28 + j * 14, 14, 14, 1, "#FFFFFF", a)
        c.drawRect(skia.Rect.MakeXYWH(-18, -28, 42, 28), paint("#FFFFFF", a, stroke=2))
    else:
        c.drawCircle(0, 0, 48, paint(GREEN, a))
        c.drawCircle(0, 0, 41, paint("#FFFFFF", a, stroke=4))
        text_mid(c, "!", 0, 0, 60, "black", "#FFFFFF", a)
    c.restore()
    if label:
        text(c, PLACAS[kind][0], x, y + (170 if poste else 80) * s, int(26 * s) + 2, "black", GREEN, a)


def placa_na_palavra(c, t, C, L, frase_i, palavra, kind, lay_args, a=1.0, s=0.45):
    """plaquinha que surge sobre uma palavra da leitura no instante em que é dita"""
    x, y, maxw, size, lh = lay_args
    lay = L.layout(x, y, maxw, size, lh)
    T = L.times(C)
    alvo = _norm(palavra)
    for w, si, wi, xx, yy, ww in lay:
        if si == frase_i and _norm(w) == alvo:
            ap = ep(t, T[si][wi] - 0.05, 0.35) * a
            if ap <= 0:
                return
            sc = 0.75 + 0.25 * ease_back(clamp(ap))
            cx, cy = xx + ww / 2, yy - size * 0.33
            bw, bh = ww + 22, size * 1.45
            c.save(); c.translate(cx, cy); c.scale(sc, sc)
            rrect(c, -bw / 2, -bh / 2, bw, bh, 8, GREEN, ap, shadow=True)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-bw / 2 + 4, -bh / 2 + 4, bw - 8, bh - 8), 5, 5), paint("#FFFFFF", ap, stroke=2))
            text_mid(c, w, 0, 0, size, "black", "#FFFFFF", ap)
            c.restore()
            return


# ======================================================================
# abertura
# ======================================================================

def estrada(c, a, y=560):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(160, y + 150); p.cubicTo(700, y + 150, 900, y - 40, 1760, y - 30)
    c.drawPath(p, paint("#9CA3AF", a, stroke=110))
    pe = paint("#FFFFFF", a, stroke=6); pe.setPathEffect(skia.DashPathEffect.Make([40, 30], 0))
    c.drawPath(p, pe)


def b_hook(c, t, C, B):
    head(c, t, B["start"], "LINGUAGENS ENEM", "AS PISTAS QUE ENTREGAM A TESE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    estrada(c, aa, 690)
    for k, kind in enumerate(("curva", "chegada", "opiniao")):
        placa(c, 480 + k * 480, 380, kind, aa * ep(t, C["01.a"] + 0.5 * k, 0.4), 1.1)
    text(c, "o texto já avisou onde está a tese", W / 2, 250, 40, "black", INK, aa)
    pill(c, "quase ninguém repara nas placas", W / 2, 810, AMBER, INK, size=30, a=ep(t, C["01.b"], 0.4), anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "achar a tese MAIS RÁPIDO", "título · começo dos parágrafos · palavrinhas"),
            ("02.b", "responder FUNÇÃO DO PARÁGRAFO", "a questão de organização do texto")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")
        text(c, sub, 400, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DUAS LEMBRANÇAS", "EPISÓDIOS 1 E 4", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    pill(c, "EP. 1 · TESE = o que o texto afirma", 560, 280, BLUE, size=30, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["03.b"], 0.5)
    pill(c, "EP. 4 · ONDE ELA FICA", 1360, 280, PURPLE, size=30, a=ab, anchor="center", bounds=(0, 1920))
    for k, (s, pos) in enumerate((("começo", 0), ("fim", 5), ("nenhum lugar", -1))):
        x = 1130 + k * 230
        a = ab * ep(t, C["03.b"] + 0.4 * k, 0.3)
        rrect(c, x - 80, 340, 160, 240, 12, "#FFFFFF", a, shadow=True)
        for j in range(6):
            line(c, x - 55, 375 + j * 34, x + 55 - (j % 3) * 18, 375 + j * 34, BLUE if j == pos else LINE, a, 12 if j == pos else 8)
        if pos < 0:
            text_mid(c, "?", x, 460, 80, "black", PURPLE, a * 0.8)
        text(c, s, x, 620, 26, "black", INK2, a)
    text(c, "hoje: as PISTAS que mostram onde", W / 2, 760, 38, "black", GREEN, ep(t, C["03.c"], 0.4))


def b_estrada(c, t, C, B):
    frame(c, t, B["start"], "PENSE NUMA", "ESTRADA", GREEN)
    a0 = ep(t, C["04.t"], 0.5)
    estrada(c, a0, 620)
    placa(c, 520, 380, "curva", ep(t, C["04.a"], 0.5), 1.2)
    placa(c, 1300, 360, "chegada", ep(t, C["04.b"], 0.5), 1.2)
    acc = ep(t, C["04.c"], 0.4)
    text(c, "você ainda não viu a curva...", 900, 250, 34, "black", INK2, acc)
    text(c, "mas já sabe que ela vem", 900, 296, 34, "black", GREEN, acc)
    pill(c, "o texto também tem PLACAS", W / 2, 830, GREEN, size=32, a=ep(t, C["04.d"], 0.4), anchor="center")


# ======================================================================
# blocos A e B — o título
# ======================================================================

def titulo_card(c, x, y, w, s, a, sub="", col=INK):
    if a <= 0:
        return
    rrect(c, x, y, w, 230, 20, "#FFFFFF", a, shadow=True)
    text(c, s, x + w / 2, y + 110, 44, "black", col, a)
    for j in range(3):
        line(c, x + 50, y + 150 + j * 22, x + w - 50 - j * 50, y + 150 + j * 22, LINE, a, 8)
    if sub:
        text(c, sub, x + w / 2, y + 290, 26, "bold", GRAY, a)


def b_titulo(c, t, C, B):
    frame(c, t, B["start"], "A 1ª PLACA", "O TÍTULO", BLUE)
    aa = ep(t, C["05.a"], 0.4)
    caixa(c, 460, 190, 1000, 70, BLUE, aa, "TÍTULO = o nome que vem em cima do texto", 28)
    ab = ep(t, C["05.b"], 0.5)
    titulo_card(c, 260, 330, 640, "Feiras livres", ab)
    pill(c, "só o ASSUNTO", 580, 620, INK2, size=30, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["05.c"], 0.5)
    titulo_card(c, 1020, 330, 640, "O barato que sai caro", acc, col=BLUE)
    pill(c, "já entrega a TESE", 1340, 620, BLUE, size=30, a=acc, anchor="center", bounds=(0, 1920))
    text(c, "a melhor pista antes de ler uma linha", 1340, 720, 28, "black", GREEN, ep(t, C["05.d"], 0.4))


def b_efeito(c, t, C, B):
    head_seq(c, t, C, [("06", "TÍTULO DE EFEITO", "ENGANA", AMBER), ("07", "O TÍTULO É", "HIPÓTESE", PURPLE)])
    card(c, *CARD_R)
    p7 = ep(t, C["07"], 0.6)
    if p7 < 1:
        a = 1 - p7
        text(c, "título feito só para chamar atenção", W / 2, 250, 36, "black", INK, a * ep(t, C["06.a"], 0.4))
        cards = [("06.b", "IRÔNICO", "diz uma coisa querendo dizer outra"), ("06.c", "PERGUNTA", "“O fim do livro?”"),
                 ("06.d", "TROCADILHO", "jogo de palavras")]
        for k, (cue, s, sub) in enumerate(cards):
            al, d = rise(t, C[cue])
            al *= a
            x = 260 + k * 480
            rrect(c, x, 320 + d, 420, 220, 20, mix("#FFFFFF", AMBER, 0.08), al)
            text(c, s, x + 210, 400 + d, 40, "black", AMBER, al)
            text(c, sub, x + 210, 470 + d, 26, "bold", INK2, al)
        selo(c, W / 2, 680, a * ep(t, C["06.e"], 0.4), "PODE DIZER O CONTRÁRIO DO TEXTO", AMBER, -3, 30)
    if p7 > 0:
        a = p7
        caixa(c, 460, 230, 1000, 80, PURPLE, a * ep(t, C["07.a"], 0.4), "HIPÓTESE = um palpite que ainda precisa ser conferido", 28)
        steps = [("07.b", "1. leia o título"), ("07.b", "2. imagine a tese"), ("07.c", "3. CONFIRME no texto")]
        for k, (cue, s) in enumerate(steps):
            al = a * ep(t, C[cue] + (0.8 if k == 1 else 0), 0.4)
            x = 420 + k * 540
            rrect(c, x - 220, 420, 440, 140, 20, "#FFFFFF", al, shadow=True)
            text_mid(c, s, x, 490, 34, "black", GREEN if k == 2 else INK, al)
            if k < 2:
                arrow(c, x + 230, 490, x + 310, 490, GRAY, al, 4, 16)
        check_icon(c, 1500, 640, 34, a * ep(t, C["07.c"] + 0.8, 0.3), GREEN)


# ======================================================================
# blocos C e D — parágrafos e função
# ======================================================================

def doc(c, x, y, w, a, hl_first=0.0, labels=None, la=(0, 0, 0)):
    """documento com 3 parágrafos; hl_first destaca a 1ª linha de cada um (tópico frasal)"""
    if a <= 0:
        return
    rrect(c, x, y, w, 560, 18, "#FFFFFF", a, shadow=True)
    for k in range(3):
        y0 = y + 50 + k * 170
        for j in range(4):
            xx = x + (80 if j == 0 else 50)
            ww = w - 100 - (j % 2) * 60 - (40 if j == 0 else 0)
            line(c, xx, y0 + j * 32, xx + ww, y0 + j * 32, mix(LINE, BLUE, hl_first) if j == 0 else LINE, a, 12)
        if labels:
            pill(c, labels[k], x + w + 30, y0 + 46, [BLUE, INK2, PURPLE][k], size=26, a=a * la[k], bounds=(0, 1920))


def b_paragrafos(c, t, C, B):
    head_seq(c, t, C, [("08", "A 2ª PLACA", "OS PARÁGRAFOS", BLUE), ("09", "A 1ª FRASE DO PARÁGRAFO", "TÓPICO FRASAL", BLUE),
                       ("10", "NO TEXTO QUE DEFENDE OPINIÃO", "O PAPEL DE CADA PARÁGRAFO", PURPLE)])
    card(c, *CARD_R)
    a0 = ep(t, C["08.t"], 0.5)
    labels = ["1º · assunto e TESE", "meio · ARGUMENTOS", "último · retoma ou PROPÕE"]
    doc(c, 260, 220, 560, a0, ep(t, C["09.a"], 0.5), labels, (ep(t, C["10.a"], 0.4), ep(t, C["10.b"], 0.4), ep(t, C["10.c"], 0.4)))
    p10 = ep(t, C["10.t"], 0.4)
    a8 = 1 - p10
    rows = [("08.a", "PARÁGRAFO", "bloco de texto que começa numa linha nova"),
            ("08.b", "PARAGRAFAÇÃO", "o jeito como o texto se divide em parágrafos"),
            ("08.c", "UM tema por parágrafo", ""),
            ("09.b", "TÓPICO FRASAL", "a 1ª frase, que anuncia o parágrafo")]
    for k, (cue, s, sub) in enumerate(rows):
        al, d = rise(t, C[cue])
        al *= a8
        y = 280 + k * 130 + d
        if al > 0:
            rrect(c, 960, y - 40, 720, 104 if sub else 70, 14, "#F7F7F5", al)
            text(c, s, 990, y + (2 if sub else 6), 30, "black", BLUE, al, align="left")
            if sub:
                text(c, sub, 990, y + 42, 24, "bold", INK2, al, align="left")
    pill(c, "leia a 1ª frase de cada parágrafo = o esqueleto", 1320, 800, GREEN, size=24, a=a8 * ep(t, C["09.c"], 0.4), anchor="center", bounds=(0, 1920))


def b_pergunta(c, t, C, B):
    frame(c, t, B["start"], "COMO ISSO CAI", "NA PROVA", PURPLE)
    aa = ep(t, C["11.a"], 0.4)
    text(c, "“Qual a FUNÇÃO do segundo parágrafo?”", W / 2, 270, 44, "black", INK, aa)
    text(c, "função = o trabalho que ele faz no texto", W / 2, 340, 30, "bold", BLUE, ep(t, C["11.b"], 0.4))
    regra(c, "Para que serve este parágrafo?", 470, ep(t, C["11.c"], 0.5), 48)
    for k, s in enumerate(("apresentar o problema?", "explicar por quê?", "propor uma solução?")):
        pill(c, s, 480 + k * 480, 650, [BLUE, INK2, PURPLE][k], size=30, a=ep(t, C["11.d"] + 0.6 * k, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# blocos E e F — palavras-sinal e a palavra que volta
# ======================================================================

def b_sinais(c, t, C, B):
    head_seq(c, t, C, [("12", "A 3ª PLACA", "AS PALAVRAS-SINAL", GREEN), ("13", "PALAVRAS-SINAL", "CHEGADA", GREEN),
                       ("14", "PALAVRAS-SINAL", "OPINIÃO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.4)
    caixa(c, 330, 185, 1260, 64, GREEN, aa, "PALAVRA-SINAL = palavrinha que avisa o que vem depois", 26)
    text(c, "(muitos livros dizem: MARCA LINGUÍSTICA)", W / 2, 290, 24, "bold", GRAY, ep(t, C["12.b"], 0.4))
    data = [("curva", "12.c", "12.d"), ("chegada", "13.a", "13.b"), ("opiniao", "14.a", "14.b")]
    for k, (kind, c1, c2) in enumerate(data):
        x = 440 + k * 520
        a1 = ep(t, C[c1], 0.5)
        placa(c, x, 400, kind, a1, 1.0, label=False)
        text(c, PLACAS[kind][0], x, 600, 34, "black", GREEN, a1)
        para(c, PLACAS[kind][1], x, 650, 26, "black", INK, a1, 440, 34, align="center")
        para(c, PLACAS[kind][2], x, 720, 24, "bold", BLUE, ep(t, C[c2], 0.4), 440, 32, align="center")
    pill(c, "+ defendo · acredito: o autor falando por si", 1480, 798, GREEN, size=20, a=ep(t, C["14.c"], 0.4), anchor="center", bounds=(0, 1920))
    pill(c, "viu uma placa? a tese está POR PERTO", 600, 798, BLUE, size=22, a=ep(t, C["14.d"], 0.4), anchor="center", bounds=(0, 1920))


def b_volta(c, t, C, B):
    frame(c, t, B["start"], "A ÚLTIMA PISTA", "A PALAVRA QUE VOLTA", BLUE)
    aa = ep(t, C["15.a"], 0.5)
    rrect(c, 260, 200, 760, 600, 18, "#FFFFFF", aa, shadow=True)
    for k in range(3):
        y0 = 250 + k * 180
        for j in range(4):
            line(c, 300, y0 + j * 34, 960 - (j % 2) * 80, y0 + j * 34, LINE, aa, 12)
        xw = 340 + (k * 170) % 420
        hb = ep(t, C["15.a"] + 0.6 + 0.5 * k, 0.3)
        rrect(c, xw, y0 + 34 - 14, 120, 28, 6, AMBER, aa * hb)
        text_mid(c, "feira", xw + 60, y0 + 34, 22, "black", INK, aa * hb)
    ab = ep(t, C["15.b"], 0.4)
    pill(c, "ela indica o ASSUNTO", 1340, 340, INK2, size=32, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["15.c"], 0.4)
    placa(c, 965, 590, "curva", acc, 0.4, label=False, poste=False)
    rrect(c, 300, 620 - 14, 600, 28, 6, BLUE, aa * acc * 0.6)
    text(c, "o que se afirma com mais força,", 1340, 520, 30, "black", INK, acc)
    text(c, "perto de uma placa", 1340, 565, 30, "black", GREEN, acc)
    pill(c, "indica a TESE", 1340, 680, BLUE, size=36, a=ep(t, C["15.d"], 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

EXE = [("16.a", "17.a", "Portanto, a cidade precisa de mais ciclovias.", "chegada"),
       ("16.b", "17.b", "Muitos acham que o livro vai acabar, porém as bibliotecas estão cheias.", "curva"),
       ("16.c", "17.c", "É preciso investir no transporte público.", "opiniao"),
       ("16.d", "17.d", "Defendo que a escola comece mais tarde.", "opiniao")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "AGORA É COM VOCÊ", "QUAL PLACA É ESTA?", GREEN), ("17", "VAMOS CONFERIR", "QUAL PLACA É ESTA?", GREEN)])
    card(c, *CARD_R)
    for k, (cq, cr, s, kind) in enumerate(EXE):
        a, d = rise(t, C[cq])
        y = 220 + k * 150 + d
        if a > 0:
            rrect(c, 220, y, 1180, 120, 20, "#F7F7F5", a)
            badge_num(c, k + 1, 290, y + 60, a, 28, bg=INK)
            para(c, s, 350, y + (72 if len(s) < 50 else 52), 32, "black", INK, a, 1020, 40)
        ar = ep(t, C[cr], 0.4)
        placa(c, 1500, y + 60, kind, ar, 0.55, label=False, poste=False)
        text(c, PLACAS[kind][0], 1580, y + 72, 28, "black", GREEN, ar, align="left")
    pause_timer(c, t, C["16.end"] - 1.7, 1580, 500)


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["O título é hipótese; o texto confirma.", "Mas, porém, engano: lá vem a opinião do autor.", "Para que serve este parágrafo?"]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 230, y - 16, a, 36, bg=PURPLE)
        text(c, s, 300, y, 50, "black", INK, a, align="left")


ERROS = [("19", "Confiar num título IRÔNICO ou em PERGUNTA", "é a primeira coisa que o autor escreveu", "pode ser só efeito: confirme no texto"),
         ("20", "Tomar como do autor a ideia ANTES do mas", "ela está escrita, com todas as letras", "placa de curva: a opinião vem DEPOIS"),
         ("21", "Descrever a função de OUTRO parágrafo", "a alternativa descreve algo do texto", "qual parágrafo a questão pediu?")]


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
    if sid == "20":
        placa(c, 1560, 690, "curva", ac, 0.6, label=False, poste=False)


# ======================================================================
# questões 5 e 7
# ======================================================================

Q5 = Leitura(
    [("23", "f1", "c1", "Uma camiseta pelo preço de um lanche parece vitória do consumidor."),
     ("23", "f2", "c2", "Mas alguém pagou a diferença: o costureiro que recebe por peça, o rio que recebe o corante, o aterro que recebe a roupa descartada depois de três lavagens."),
     ("24", "f3", "c3", "O preço da etiqueta é só a parte da conta que chega ao caixa; o resto é dividido entre quem não estava na loja.")],
    [(0, "parece vitória do consumidor.", "under", AMBER, "23.c1"),
     (0, "parece vitória do consumidor.", "strike", RED, "23.c2"),
     (1, "Mas", "box", GREEN, None),
     (1, "o costureiro que recebe por peça,", "under", BLUE, "24.c3"),
     (1, "o rio que recebe o corante,", "under", BLUE, "24.c3"),
     (1, "o aterro que recebe a roupa descartada", "under", BLUE, "24.c3"),
     (2, "o resto é dividido entre quem não estava na loja.", "fill", BLUE, "24.c3")])

Q7P = [Leitura([("27", "f1", "c1", "Consertar um aparelho deveria ser mais simples do que comprar outro. Hoje, porém, o caminho costuma ser o inverso.")],
               [(0, "deveria", "box", GREEN, None), (0, "porém,", "box", GREEN, None)]),
       Leitura([("28", "f2", "c2", "Peças coladas em vez de parafusadas, baterias que não se removem, manuais técnicos que o fabricante não divulga: cada um desses detalhes de projeto encarece o reparo até o ponto em que ele deixa de compensar.")],
               [(0, "Peças coladas em vez de parafusadas,", "under", INK2, "29.b"),
                (0, "baterias que não se removem,", "under", INK2, "29.b"),
                (0, "manuais técnicos que o fabricante não divulga:", "under", INK2, "29.b")]),
       Leitura([("28", "f3", "f3", "Leis que obriguem a oferta de peças e de informações técnicas por um prazo mínimo não resolvem tudo, mas devolvem ao consumidor uma escolha que hoje lhe é tirada antes mesmo da compra.")],
               [(0, "mas", "box", GREEN, None)])]
FUNCOES = [("29.a", "apresenta o problema", BLUE), ("29.b", "explica por quê", INK2), ("29.c", "propõe solução", PURPLE)]

ALTS5 = [("A", "antecipa a tese de que o preço baixo esconde custos sociais e ambientais pagos por outros.", "25.a", None, ""),
         ("B", "contradiz o texto, que defende a compra de roupas baratas como vitória do consumidor.", "25.b", "26.b", "CONTRADIÇÃO: o que vem antes do mas"),
         ("C", "indica que o texto tratará do aumento recente no preço das roupas.", "25.c", "26.c", "NÃO ESTÁ NO TEXTO"),
         ("D", "refere-se apenas à baixa durabilidade das camisetas, descartadas após poucas lavagens.", "25.d", "26.d", "REDUÇÃO"),
         ("E", "sugere que o consumidor foi enganado pelo vendedor no momento da compra.", "25.e", "26.e", "EXTRAPOLAÇÃO")]
ALTS7 = [("A", "apresenta a tese, que é retomada no terceiro parágrafo.", "30.a", "31.a", "FUNÇÃO ERRADA"),
         ("B", "fundamenta a afirmação do primeiro parágrafo com exemplos de como o projeto dos aparelhos dificulta o conserto.", "30.b", None, ""),
         ("C", "introduz uma opinião contrária à do autor, que é refutada no terceiro parágrafo.", "30.c", "31.c", "NÃO ESTÁ NO TEXTO"),
         ("D", "propõe a solução defendida pelo autor para o problema apresentado.", "30.d", "31.d", "PARÁGRAFO ERRADO: é o 3º"),
         ("E", "abandona o assunto inicial para tratar do preço dos aparelhos novos.", "30.e", "31.e", "TROCA O ASSUNTO")]


def b_questao5(c, t, C, B):
    head_seq(c, t, C, [("22", "EU FAÇO", "QUESTÃO 5 · O TÍTULO COMO PISTA", BLUE), ("25", "EU FAÇO", "AS ALTERNATIVAS", AMBER)])
    card(c, *CARD_R)
    pill(c, "COMANDO: Em relação ao texto, o título", 200, 200, BLUE, size=24, a=ep(t, C["22.a"], 0.4), bounds=(0, 1920))
    ph = ep(t, C["25"], 0.7)
    if ph < 1:
        a = 1 - ph
        a0 = ep(t, C["22.f0"], 0.4) * a
        text(c, "O barato que sai caro", 200, 300, 48, "black", INK, a0, align="left")
        ac = ep(t, C["22.c0"], 0.4) * a
        adx = ep(t, C["24.d"], 0.4) * a
        pill(c, "HIPÓTESE: o barato acaba custando caro?", 1000, 286, PURPLE, size=24, a=ac * (1 - adx), bounds=(0, 1920))
        args = (200, 400, 1060, 34, 54)
        Q5.draw(c, t, C, *args, a * ep(t, C["23.f1"] - 0.3, 0.4))
        placa_na_palavra(c, t, C, Q5, 1, "Mas", "curva", args, a)
        notas(c, t, C, [("23.c1", "“PARECE”", "guarde essa palavra", AMBER),
                        ("23.c2", "MAS = PLACA DE CURVA", "o autor derruba a vitória", GREEN),
                        ("24.c3", "CONFIRMADO", "sai caro para OUTROS", BLUE)], 1310, 400, 110, 430, a)
        selo(c, 1240, 290, adx, "HIPÓTESE CONFIRMADA", GREEN, -4, 26)
    if ph > 0:
        text(c, "O barato que sai caro", 190, 300, 32, "black", INK, ph, align="left")
        pill(c, "o título antecipa a tese ✓", 190, 350, GREEN, size=20, a=ph, bounds=(0, 1920))
        Q5.draw(c, t, C, 190, 420, 600, 21, 31, ph * 0.9)
        aok = alternativas(c, t, C, ALTS5, "26.ok", 920, 290, 760, ph, 22)
        result_box(c, "Letra A", 490, 790, 50, aok, GREEN)


def typewriter(c, s, x, y, size, col, a, u):
    n = int(len(s) * clamp(u))
    if n > 0 and a > 0:
        pill(c, s[:n], x, y, col, size=size, a=a, bounds=(0, 1920))


def b_questao7(c, t, C, B):
    head_seq(c, t, C, [("27", "VOCÊ FAZ", "QUESTÃO 7 · OS PARÁGRAFOS", GREEN), ("29", "VOCÊ FAZ", "PARA QUE SERVE CADA UM?", PURPLE),
                       ("30", "VOCÊ FAZ", "O SEGUNDO PARÁGRAFO", AMBER)])
    card(c, *CARD_R)
    pill(c, "COMANDO: Na organização do texto, o segundo parágrafo", 200, 200, BLUE, size=24, a=ep(t, C["27.a"], 0.4), bounds=(0, 1920))
    ph = ep(t, C["30"], 0.7)
    ys = (300, 430, 640)
    if ph < 1:
        a = 1 - ph
        for k, L in enumerate(Q7P):
            sid, f = L.sents[0][0], L.sents[0][1]
            L.draw(c, t, C, 200, ys[k], 1060, 30, 44, a * ep(t, C[f"{sid}.{f}"] - 0.3, 0.4))
            badge_num(c, k + 1, 170, ys[k] - 10, a * ep(t, C[f"{sid}.{f}"] - 0.3, 0.4), 18, bg=INK2)
        placa_na_palavra(c, t, C, Q7P[0], 0, "deveria", "opiniao", (200, ys[0], 1060, 30, 44), a)
        placa_na_palavra(c, t, C, Q7P[0], 0, "porém,", "curva", (200, ys[0], 1060, 30, 44), a)
        placa_na_palavra(c, t, C, Q7P[2], 0, "mas", "curva", (200, ys[2], 1060, 30, 44), a)
        pill(c, "REPARO = conserto", 1560, 440, LIGHT, INK, size=22, a=a * ep(t, C["28.c2"], 0.4), anchor="center", bounds=(0, 1920))
        for k, (cue, s, col) in enumerate(FUNCOES):
            typewriter(c, s, 1300, ys[k] + (10, 70, 40)[k], 26, col, a, prog(t, C[cue], 1.0))
        pause_timer(c, t, C["29.a"] - 1.7, 1500, 330, a)
    if ph > 0:
        y = 300
        for k, L in enumerate(Q7P):
            L.draw(c, t, C, 210, y, 580, 18, 26, ph * 0.9)
            h = L.layout(210, y, 580, 18, 26)[-1][4] - y + 26
            pill(c, FUNCOES[k][1], 210, y + h + 10, FUNCOES[k][2], size=16, a=ph, bounds=(0, 1920))
            badge_num(c, k + 1, 180, y - 6, ph, 14, bg=INK2)
            y += h + 64
        aok = alternativas(c, t, C, ALTS7, "31.ok", 920, 290, 760, ph, 22)
        pause_timer(c, t, C["30.end"] - 1.7, 490, 790, ph)
        result_box(c, "Letra B", 490, 800, 50, aok, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A TESE IMPLÍCITA", PURPLE)
    a0 = ep(t, C["33.t"], 0.5)
    estrada(c, a0, 600)
    for k in range(3):
        x = 480 + k * 480
        a = a0 * ep(t, C["33.t"] + 0.4 * k, 0.3)
        rrect(c, x - 6, 410, 12, 90, 3, "#64748B", a)
        pe = paint(LIGHT, a, stroke=4); pe.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
        c.drawCircle(x, 370, 48, pe)
    text(c, "nenhuma placa, nenhuma opinião...", W / 2, 260, 36, "black", INK2, ep(t, C["33.a"], 0.4))
    text(c, "e mesmo assim defende algo?", W / 2, 310, 36, "black", BLUE, ep(t, C["33.b"], 0.4))
    pill(c, "ep. 6 · a tese implícita", W / 2, 820, PURPLE, size=34, a=ep(t, C["33.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Quantas das quatro placas você acertou?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, estrada=b_estrada, titulo=b_titulo, efeito=b_efeito,
              paragrafos=b_paragrafos, pergunta=b_pergunta, sinais=b_sinais, volta=b_volta, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, questao5=b_questao5, questao7=b_questao7, ponte=b_ponte, cta=b_cta)
