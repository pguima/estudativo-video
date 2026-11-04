"""Visual — Redação ENEM, Leitura da Proposta, Episódio 2: A frase temática bloco a bloco (tema claro).
Reaproveita do ep1 (como V1): folha de rascunho com letra manuscrita, etiqueta de encomenda, caixa, caminhão, selos.
Novo: PEÇAS DE QUEBRA-CABEÇA (um bloco da frase temática por peça, com "obriga a discutir"), FUNIL e CASA COM PORTAS.
Cores: azul = núcleo/tema · verde = delimitadores e método · âmbar = armadilha · vermelho = erro · roxo = regra oficial.
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

_p = Path(__file__).resolve().parents[2] / "ep1_o_que_a_prova_pede" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v_ep1", _p)
V1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V1)
motor.set_theme("claro")
# o marca-texto do ep1 lê os tempos do ep1: aponto para os tempos DESTE episódio
try:
    V1._SC = {s["id"]: s for s in json.load(open(Path(__file__).resolve().parent.parent / "audio" / "tempos.json",
                                                 encoding="utf-8"))["scenes"]}
except Exception:
    V1._SC = {}

paper, hand, hand_w, hwrap, hand_para = V1.paper, V1.hand, V1.hand_w, V1.hwrap, V1.hand_para
underline, etiqueta, caixa, truck = V1.underline, V1.etiqueta, V1.caixa, V1.truck
boxed, regra, selo, pause_timer, which, para, wrap = V1.boxed, V1.regra, V1.selo, V1.pause_timer, V1.which, V1.para, V1.wrap
frame, head_seq, xmark, phrase_span, wreveal = V1.frame, V1.head_seq, V1.xmark, V1.phrase_span, V1.wreveal
PEN = V1.PEN

MARCA = ""
ARQUIVO_FINAL = "enem_redacao_leitura_proposta_ep2_frase_tematica_blocos.mp4"
CARD_R = (140, 150, 1640, 690)
NUC, DEL = BLUE, GREEN

T23 = [("Desafios para o enfrentamento", DEL, "ORIENTAÇÃO", "obstáculos e saídas", "11.b"),
       ("da invisibilidade", DEL, "PROBLEMA", "um trabalho não reconhecido", "12.a"),
       ("do trabalho de cuidado", NUC, "NÚCLEO", "o assunto", "10.b"),
       ("realizado pela mulher", DEL, "GRUPO", "de quem se fala", "13.a"),
       ("no Brasil", DEL, "LUGAR", "onde", "13.b")]
T17 = [("Desafios para", DEL, "ORIENTAÇÃO", None, "30.b"), ("a formação educacional", NUC, "NÚCLEO", None, "30.a"),
       ("de surdos", DEL, "GRUPO", None, "30.c"), ("no Brasil", DEL, "LUGAR", None, "30.d")]
T16 = [("Caminhos para combater", DEL, "ORIENTAÇÃO", None, "36.d"), ("a intolerância religiosa", NUC, "NÚCLEO", None, "36.c"),
       ("no Brasil", DEL, "LUGAR", None, "36.e")]


# ======================================================================
# frase temática em blocos (texto corrido, manuscrito ou impresso, sublinhado por bloco)
# ======================================================================

def seg_layout(segs, x, y, size, maxw, lh, handw=True):
    meas = (lambda s: hand_w(s, size)) if handw else (lambda s: text_w(s, "black", size))
    sp = meas(" ")
    out, xx, yy = [], x, y
    for si, seg in enumerate(segs):
        for w in seg[0].split():
            ww = meas(w)
            if xx > x and xx + ww > x + maxw:
                xx, yy = x, yy + lh
            out.append((w, si, xx, yy, ww))
            xx += ww + sp
    return out


def draw_segs(c, t, C, segs, lay, size, a=1.0, handw=True, reveal=1.0, base=None, under=True):
    if a <= 0:
        return
    base = base or (PEN if handw else INK)
    n = len(lay)
    shown = reveal * n
    for k, (w, si, xx, yy, ww) in enumerate(lay):
        r = clamp(shown - k)
        if r <= 0:
            break
        col = segs[si][1]
        on_ = ep(t, C[segs[si][4]], 0.4) if under else 0
        if on_ > 0:
            rrect(c, xx - 4, yy - size * 0.95, ww + 12, size * 1.3, 6, col, a * on_ * 0.16)
            underline(c, xx - 2, xx + ww + 8, yy + 10, col, a * on_, prog(t, C[segs[si][4]], 0.5), 5)
        if handw:
            hand(c, w, xx, yy, size, mix(base, col, on_), a, r, pen=False)
        else:
            text(c, w, xx, yy, size, "black", mix(base, col, on_), a, align="left")


def piece(c, x, y, w, h, col, a, label=None, obriga=None, oa=1.0, knob=True, dy=0.0, rot=0.0):
    """peça de quebra-cabeça: retângulo com encaixe à direita; rótulo do tipo em cima, 'obriga a discutir' embaixo"""
    if a <= 0:
        return
    c.save()
    c.translate(x + w / 2, y + h / 2 + dy); c.rotate(rot); c.translate(-(x + w / 2), -(y + h / 2))
    rrect(c, x, y, w, h, 14, mix("#FFFFFF", col, 0.14), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), paint(col, a, stroke=4))
    if knob:
        c.drawCircle(x + w, y + h / 2, 16, paint(mix("#FFFFFF", col, 0.14), a))
        c.drawArc(skia.Rect.MakeLTRB(x + w - 16, y + h / 2 - 16, x + w + 16, y + h / 2 + 16), -90, 180, False, paint(col, a, stroke=4))
    if label:
        pill(c, label, x + w / 2, y - 24, col, size=18, a=a, anchor="center", bounds=(0, 1920))
    if obriga and oa > 0:
        text(c, "obriga a discutir:", x + w / 2, y + h + 34, 18, "bold", GRAY, a * oa)
        lines = wrap(obriga, "black", 22, w + 20)
        for j, ln in enumerate(lines):
            text(c, ln, x + w / 2, y + h + 64 + j * 28, 22, "black", col, a * oa)
    c.restore()


def puzzle(c, t, C, segs, y, a, size=26, show=None, gone=None, fall=0.0, obriga=True):
    """fila de peças centralizada; show[i] = alpha de cada peça; gone = índices que caem (fall 0..1)"""
    if a <= 0:
        return
    ws = [text_w(s[0], "black", size) + 46 for s in segs]
    gap = 26
    tot = sum(ws) + gap * (len(ws) - 1)
    x = W / 2 - tot / 2
    for i, (seg, w) in enumerate(zip(segs, ws)):
        al = a * (show[i] if show else 1)
        dy, rot, fa = 0.0, 0.0, 1.0
        if gone and i in gone:
            dy, rot, fa = 260 * fall * fall, 18 * fall, 1 - fall
        if al > 0:
            piece(c, x, y, w, 76, seg[1], al * fa, seg[2], seg[3] if obriga else None, 1.0, i < len(segs) - 1, dy, rot)
            text_mid(c, seg[0], x + w / 2, y + 38 + dy, size, "black", INK, al * fa)
        x += w + gap


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM", "A FRASE TEMÁTICA, BLOCO A BLOCO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 200, 1320, 150, PURPLE, aa, 0.08)
        text(c, "CARTILHA DO PARTICIPANTE", 340, 248, 20, "black", PURPLE, aa, align="left", tracking=2)
        text(c, "abordar TODOS os elementos da frase temática", W / 2, 312, 46, "black", INK, aa)
    show = [ep(t, C["01.a"] + 1.0 + 0.3 * i, 0.4) for i in range(5)]
    ab = ep(t, C["01.b"], 0.5)
    puzzle(c, t, C, T23, 520, aa, 26, show, gone=[1, 3], fall=ep(t, C["01.c"], 1.2), obriga=False)
    pill(c, "quase ninguém confere", 560, 780, AMBER, size=30, a=ab, anchor="center", bounds=(0, 1920))
    selo(c, 1360, 780, ep(t, C["01.c"] + 0.6, 0.4), "PERDE PONTOS", RED, -6, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "DESMONTAR a frase temática", "em blocos"), ("02.b", "saber o que cada bloco OBRIGA", "você a discutir"),
            ("02.c", "transformar o tema em PERGUNTA", "")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 290 + j * 160 + d
        check_icon(c, 330, y - 14, 34, a, GREEN)
        text(c, s, 400, y, 50, "black", INK, a, align="left")
        if sub:
            text(c, sub, 400, y + 52, 30, "bold", GRAY, a, align="left")


def pen_draw(c, x, y, col, a, ang=-35, s=1.0):
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.rotate(ang); c.scale(s, s)
    rrect(c, -18, -150, 36, 230, 12, col, a, shadow=True)
    rrect(c, -18, -150, 36, 46, 10, mix(col, "#000000", 0.25), a)
    p = skia.Path(); p.moveTo(-18, 80); p.lineTo(18, 80); p.lineTo(0, 120); p.close()
    c.drawPath(p, paint("#F2D3A8", a))
    c.drawCircle(0, 116, 5, paint(col, a))
    c.restore()


def b_caneta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COMEÇAR", "PAPEL E CANETA", GREEN)
    a0 = ep(t, C["03.t"], 0.5)
    paper(c, 360, 220, 700, 540, a0, lh=54, top=270)
    aa = ep(t, C["03.a"], 0.5)
    pen_draw(c, 1250, 470, BLUE, aa, -25)
    pen_draw(c, 1420, 470, GREEN, aa, 20)
    text(c, "2 cores", 1335, 720, 40, "black", INK, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        underline(c, 440, 980, 380, BLUE, ab, ep(t, C["03.b"], 0.8), 7)
        underline(c, 440, 820, 490, GREEN, ab, ep(t, C["03.b"] + 0.4, 0.8), 7)
        underline(c, 440, 900, 600, GREEN, ab, ep(t, C["03.b"] + 0.8, 0.8), 7)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRANDO O EPISÓDIO 1", "EM 30 SEGUNDOS", BLUE)
    aa = ep(t, C["04.a"], 0.5)
    caixa(c, 230, 450, 330, 260, aa, open_=ep(t, C["04.d"], 0.6), inner="TESE = a sua posição", inner_a=ep(t, C["04.d"] + 0.4, 0.6))
    rows = [("CIDADE", "envelhecimento", ep(t, C["04.b"], 0.4), BLUE, "ASSUNTO", ep(t, C["04.b"] + 0.3, 0.4)),
            ("ENDEREÇO COMPLETO", V1.TEMA25, ep(t, C["04.c"], 0.4), BLUE, "TEMA", ep(t, C["04.c"] + 0.3, 0.4))]
    etiqueta(c, 720, 210, 900, aa, rows)


# ======================================================================
# bloco A — núcleo e delimitadores
# ======================================================================

def b_etiqueta(c, t, C, B):
    head_seq(c, t, C, [("05", "POR QUE UM ENDEREÇO", "TEM TANTAS PARTES?", BLUE), ("06", "A FRASE TEMÁTICA", "TAMBÉM TEM BLOCOS", BLUE)])
    card(c, *CARD_R)
    a6 = ep(t, C["06"], 0.6)
    aa = ep(t, C["05.a"], 0.5) * (1 - a6)
    if aa > 0:
        rrect(c, 360, 200, 1200, 460, 20, "#FFFFFF", aa, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(372, 212, 1176, 436), 12, 12), paint(LIGHT, aa, stroke=2))
        text(c, "DESTINATÁRIO", 410, 262, 22, "black", GRAY, aa, align="left", tracking=2)
        parts = [("05.b", "CIDADE", "São Paulo", "a região"), ("05.c", "BAIRRO", "Vila Mariana", "aperta o cerco"),
                 ("05.d", "RUA", "Rua das Flores", "aperta mais"), ("05.e", "NÚMERO", "120", "a porta exata")]
        for k, (cue, lab, val, fn) in enumerate(parts):
            a, d = rise(t, C[cue])
            a *= aa
            y = 330 + k * 82 + d
            text(c, lab, 410, y, 20, "black", GRAY, a, align="left", tracking=1.5)
            text(c, val, 640, y + 4, 38, "black", INK, a, align="left")
            pill(c, fn, 1510, y - 8, GREEN, size=22, a=a, anchor="right", bounds=(0, 1920))
    af = ep(t, C["05.f"], 0.5) * (1 - a6)
    if af > 0:
        truck(c, 760, 700, af, RED, 0.7)
        selo(c, 1180, 740, af, "ESQUECEU UMA? A ENTREGA FALHA", RED, -4, 30)
    if a6 > 0:
        show = [ep(t, C["06.b"] + 0.25 * i, 0.4) for i in range(5)]
        text(c, "a frase temática é feita de", W / 2, 300, 40, "bold", INK2, ep(t, C["06.a"], 0.5))
        text(c, "BLOCOS", W / 2, 380, 70, "black", BLUE, ep(t, C["06.a"], 0.5))
        puzzle(c, t, C, T23, 520, a6, 26, show, obriga=False)
        text(c, "cada bloco = uma parte do endereço", W / 2, 720, 34, "black", GREEN, ep(t, C["06.b"] + 1.4, 0.5))


def b_nucleo(c, t, C, B):
    head_seq(c, t, C, [("07", "O BLOCO PRINCIPAL", "NÚCLEO", NUC), ("08", "O RESTO DA FRASE", "DELIMITADORES", DEL)])
    card(c, *CARD_R)
    a8 = ep(t, C["08"], 0.6)
    aa = ep(t, C["07.a"], 0.5)
    # cidade no centro (núcleo) e anéis que apertam (delimitadores)
    cx, cy = 560, 470
    if aa > 0:
        for k, r in enumerate((260, 200, 140)):
            ak = a8 * ep(t, C["08.b"] + 0.3 * k, 0.4)
            if ak > 0:
                c.drawCircle(cx, cy, r, paint(DEL, ak * 0.10))
                c.drawCircle(cx, cy, r, paint(DEL, ak, stroke=4))
        c.drawCircle(cx, cy, 80, paint(NUC, aa))
        text_mid(c, "NÚCLEO", cx, cy, 30, "black", "#FFFFFF", aa)
    text(c, "a palavra que NOMEIA O ASSUNTO", 1300, 300, 34, "black", NUC, aa * (1 - a8))
    ab = ep(t, C["07.b"], 0.5) * (1 - a8)
    for k, s in enumerate(("envelhecimento", "cinema", "registro civil")):
        pill(c, s, 1300, 390 + k * 80, NUC, size=32, a=ab * ep(t, C["07.b"] + 0.4 * k, 0.3), anchor="center", bounds=(0, 1920))
    ac = ep(t, C["07.c"], 0.5) * (1 - a8)
    pill(c, "nome de MÉTODO DE ESTUDO · não é termo da Cartilha", 1300, 700, AMBER, size=24, a=ac, anchor="center", bounds=(0, 1920))
    aa8 = ep(t, C["08.a"], 0.5)
    text(c, "DELIMITADORES", 1300, 320, 50, "black", DEL, aa8)
    text(c, "tudo o que RESTRINGE o núcleo", 1300, 390, 34, "bold", INK, aa8)
    ab8 = ep(t, C["08.b"], 0.5)
    text(c, "como bairro, rua e número", 1300, 470, 32, "bold", GRAY, ab8)
    text(c, "restringem a cidade", 1300, 515, 32, "bold", GRAY, ab8)
    pill(c, "também é nome de método", 1300, 700, AMBER, size=24, a=ep(t, C["08.c"], 0.5), anchor="center", bounds=(0, 1920))


def b_tipos(c, t, C, B):
    frame(c, t, B["start"], "DELIMITADORES", "QUATRO TIPOS", DEL)
    rows = [("09.a", "ASPECTO", ["estigma", "invisibilidade", "acesso"]), ("09.b", "GRUPO", ["surdos", "mulher", "povos tradicionais"]),
            ("09.c", "LUGAR", ["no Brasil"]), ("09.d", "ORIENTAÇÃO", ["desafios para", "caminhos para"])]
    for k, (cue, lab, ex) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 260 + k * 125 + d
        rrect(c, 230, y - 50, 1460, 100, 18, "#F7F7F5", a)
        badge_num(c, k + 1, 290, y, a, 26, bg=DEL)
        text(c, lab, 340, y + 14, 40, "black", DEL, a, align="left")
        x = 720
        for j, e in enumerate(ex):
            x0, x1 = pill(c, e, x, y, "#FFFFFF", INK, size=28, a=a * ep(t, C[cue] + 0.4 + 0.3 * j, 0.3), bounds=(0, 1920))
            x = x1 + 20


# ======================================================================
# bloco B — eu faço: 2023 no rascunho
# ======================================================================

def b_eufaco(c, t, C, B):
    sid = which(t, C, ["10", "11", "12", "13", "14"])
    head(c, t, B["start"], "EU FAÇO · ENEM 2023", "BLOCO A BLOCO NO RASCUNHO", GREEN)
    a14 = ep(t, C["14"], 0.6)
    paper(c, 160, 160, 1600, 700, 1.0, lh=60, top=210)
    lay = seg_layout(T23, 260, 270, 38, 1420, 66)
    sp = (C["10.q"], C["10.a"] - 0.4)
    draw_segs(c, t, C, T23, lay, 38, 1.0, True, wreveal(t, sp))
    # legenda das canetas
    pen_a = ep(t, C["10.b"], 0.4)
    pill(c, "azul = NÚCLEO", 1690, 780, NUC, size=20, a=pen_a, anchor="right", bounds=(0, 1920))
    pill(c, "verde = DELIMITADOR", 1690, 820, DEL, size=20, a=ep(t, C["11.a"], 0.4), anchor="right", bounds=(0, 1920))
    # peças aparecendo conforme cada bloco é analisado
    show = [ep(t, C[s[4]] + 0.6, 0.4) for s in T23]
    fall = ep(t, C["14.b"], 1.4)
    puzzle(c, t, C, T23, 470, 1.0, 22, show, gone=[1, 3, 4], fall=fall)
    if sid == "10":
        th = fw(t, C["10.a"], C["10.b"])
        text(c, "de que assunto essa frase fala?", W / 2, 720, 34, "black", GRAY, th)
    ac = ep(t, C["14.c"], 0.5)
    pill(c, "peças do recorte DE FORA", 700, 800, RED, size=28, a=ac, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        truck(c, 1150, 740, ad, RED, 0.6)
        text(c, "não chega", 1420, 800, 30, "black", RED, ad, align="left")
    pill(c, "5 blocos = 5 exigências", W / 2, 400, GREEN, size=30, a=ep(t, C["14.t"], 0.4) * (1 - ep(t, C["14.a"], 0.4)), anchor="center")


# ======================================================================
# bloco C — expressões de abertura
# ======================================================================

ABERT = [("15.a", "Desafios para…", "2017 · 2022 · 2023 · 2024", "apontar obstáculos concretos e discutir como superá-los"),
         ("15.b", "Caminhos para combater…", "2016", "reconhecer o problema e discutir formas de enfrentá-lo"),
         ("16.a", "Perspectivas acerca de…", "2025", "discutir modos de ver e de lidar com o fenômeno"),
         ("16.b", "A persistência de…", "2015", "explicar por que o problema continua existindo"),
         ("16.c", "Democratização do acesso a…", "2019", "discutir quem tem e quem não tem acesso, e por quê")]


def b_aberturas(c, t, C, B):
    head_seq(c, t, C, [("15", "O COMECINHO DA FRASE", "O QUE ELE COSTUMA PEDIR", DEL), ("17", "ATENÇÃO", "LEITURA DE ESTUDO", AMBER)])
    card(c, *CARD_R)
    text(c, "EXPRESSÃO", 220, 210, 20, "black", GRAY, ep(t, C["15.t"], 0.4), align="left", tracking=1.5)
    text(c, "PROVAS", 720, 210, 20, "black", GRAY, ep(t, C["15.t"], 0.4), align="left", tracking=1.5)
    text(c, "O QUE A DISCUSSÃO COSTUMA PRECISAR", 1080, 210, 20, "black", GRAY, ep(t, C["15.t"], 0.4), align="left", tracking=1.5)
    for k, (cue, ex, anos, pede) in enumerate(ABERT):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 280 + k * 104 + d
        pill(c, ex, 210, y, DEL, size=26, a=a, bounds=(0, 1920))
        text(c, anos, 720, y + 10, 22, "bold", GRAY, a, align="left")
        para(c, pede, 1080, y - 4, 26, "bold", INK, a, 600, 32)
        line(c, 200, y + 48, 1720, y + 48, LINE, a, 2)
    a17 = ep(t, C["17.t"], 0.5)
    if a17 > 0:
        boxed(c, 360, 730, 1200, 100, AMBER, a17, 0.14)
        text_mid(c, "NÃO é regra oficial · serve para não esquecer metade do recorte", W / 2, 780, 32, "black", INK, a17)


# ======================================================================
# bloco D — as duas canetas
# ======================================================================

T25 = [("Perspectivas acerca", DEL, "ORIENTAÇÃO", None, "18.b"), ("do envelhecimento", NUC, "NÚCLEO", None, "18.a"),
       ("na sociedade brasileira", DEL, "LUGAR", None, "18.b")]


def b_cores(c, t, C, B):
    frame(c, t, B["start"], "DICA PRÁTICA", "SUBLINHE COM DUAS CORES", DEL)
    aa = ep(t, C["18.t"], 0.5)
    rrect(c, 260, 220, 1400, 170, 16, "#FFFFFF", aa, shadow=True)
    text(c, "CADERNO DE QUESTÕES", 300, 262, 18, "black", GRAY, aa, align="left", tracking=2)
    lay = seg_layout(T25, 300, 340, 46, 1150, 60, handw=False)
    draw_segs(c, t, C, T25, lay, 46, aa, handw=False)
    pen_draw(c, 1560, 330, NUC, ep(t, C["18.a"], 0.4), -30, 0.6)
    pen_draw(c, 1630, 330, DEL, ep(t, C["18.b"], 0.4), 25, 0.6)
    ac = ep(t, C["18.c"], 0.5)
    if ac > 0:
        paper(c, 300, 470, 900, 330, ac, lh=48, top=500)
        text(c, "o SEU texto", 340, 520, 22, "black", GRAY, ac, align="left")
        for k, (s, col) in enumerate((("envelhecimento", NUC), ("perspectivas", DEL), ("sociedade brasileira", DEL))):
            a = ac * ep(t, C["18.c"] + 0.6 + 0.5 * k, 0.4)
            check_icon(c, 1280, 560 + k * 80, 22, a, GREEN)
            text(c, s, 1320, 572 + k * 80, 32, "black", col, a, align="left")
            hand(c, s + "...", 360 + k * 60, 590 + k * 70, 30, PEN, ac)
    pill(c, "mesmas palavras OU sinônimos precisos", 1440, 800, GREEN, size=24, a=ep(t, C["18.d"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco E — foco, porta, funil
# ======================================================================

def b_foco(c, t, C, B):
    head_seq(c, t, C, [("19", "TEMA IGUAL PARA TODOS", "TEXTOS IGUAIS?", BLUE), ("20", "O QUE A CARTILHA", "RECOMENDA", PURPLE)])
    card(c, *CARD_R)
    a20 = ep(t, C["20"], 0.6)
    a0 = ep(t, C["19.t"], 0.5) * (1 - a20)
    if a0 > 0:
        boxed(c, 560, 200, 800, 90, BLUE, a0, 0.10)
        text_mid(c, "MESMO TEMA", W / 2, 245, 40, "black", BLUE, a0)
        foci = ["as CAUSAS", "as CONSEQUÊNCIAS", "outros ASPECTOS"]
        for k, s in enumerate(foci):
            a = a0 * ep(t, C["19.b"] + 0.4 * k, 0.4)
            x = 420 + k * 540
            arrow(c, W / 2, 295, x, 400, LIGHT, a, 4, 14)
            paper(c, x - 200, 410, 400, 300, a, lh=40, top=440, margin=False)
            pill(c, "foco: " + s, x, 470, GREEN, size=24, a=a * ep(t, C["19.c"] + 0.3 * k, 0.3), anchor="center", bounds=(0, 1920))
        pill(c, "NÃO", W / 2, 360, RED, size=30, a=ep(t, C["19.a"], 0.3) * a0, anchor="center", bounds=(0, 1920))
        text(c, "FOCO = a parte do tema que VOCÊ decide desenvolver", W / 2, 790, 34, "black", GREEN, ep(t, C["19.c"], 0.5) * a0)
    if a20 > 0:
        aq = ep(t, C["20.a"], 0.5)
        boxed(c, 260, 260, 1400, 330, PURPLE, aq, 0.08)
        text(c, "CARTILHA DO PARTICIPANTE", 300, 310, 20, "black", PURPLE, aq, align="left", tracking=2)
        text(c, "refletir sobre o tema para decidir", 300, 380, 42, "black", INK, aq, align="left")
        for k, s in enumerate(("como abordá-lo,", "qual ponto de vista adotar", "e como defendê-lo.")):
            text(c, s, 340, 450 + k * 50, 40, "black", PURPLE, aq * ep(t, C["20.a"] + 1.5 + 0.7 * k, 0.4), align="left")


def casa(c, cx, by, a, col=BLUE, placa=None, doors=None):
    if a <= 0:
        return
    w, h = 560, 300
    x, y = cx - w / 2, by - h
    rrect(c, x, y, w, h, 10, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 10, 10), paint(col, a, stroke=4))
    p = skia.Path(); p.moveTo(x - 30, y + 4); p.lineTo(cx, y - 150); p.lineTo(x + w + 30, y + 4); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.25), a)); c.drawPath(p, paint(col, a, stroke=4))
    if placa:
        rrect(c, cx - 150, y - 70, 300, 50, 8, col, a)
        text_mid(c, placa, cx, y - 45, 22, "black", "#FFFFFF", a)
    for k, (lab, da) in enumerate(doors or []):
        dx = x + 70 + k * 170
        rrect(c, dx, by - 170, 110, 170, 8, mix("#FFFFFF", GREEN, 0.25 + 0.5 * da), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(dx, by - 170, 110, 170), 8, 8), paint(GREEN, a * (0.4 + 0.6 * da), stroke=3))
        c.drawCircle(dx + 90, by - 85, 6, paint(INK2, a))
        text(c, lab, dx + 55, by + 36, 24, "black", GREEN, a * da)


def b_porta(c, t, C, B):
    frame(c, t, B["start"], "O FOCO É", "ESCOLHER A PORTA", GREEN)
    aa = ep(t, C["21.a"], 0.5)
    ab = ep(t, C["21.b"], 0.5)
    doors = [(s, ab * ep(t, C["21.c"] + 0.5 * k, 0.4)) for k, s in enumerate(("frente", "fundos", "garagem"))]
    casa(c, 620, 700, aa, BLUE, "O TEMA", doors)
    text(c, "a casa certa, no endereço certo", 620, 790, 28, "bold", BLUE, aa)
    ad = ep(t, C["21.d"], 0.5)
    if ad > 0:
        c.save(); c.translate(1360, 560); c.scale(0.6, 0.6); c.translate(-1360, -560)
        casa(c, 1360, 760, ad, RED, "OUTRO ENDEREÇO")
        c.restore()
        xmark(c, 1360, 560, 110, ep(t, C["21.d"] + 0.4, 0.4), RED, 14)
        text(c, "não pode TROCAR DE ENDEREÇO", 1360, 790, 30, "black", RED, ad)


FUNIL = [("22.a", "ASSUNTO", "saúde mental", INK2), ("22.b", "TEMA", "o estigma das doenças mentais na sociedade brasileira", BLUE),
         ("23.a", "FOCO · 2 EIXOS", "afasta do tratamento · a mídia reforça estereótipos", GREEN), ("23.d", "TESE", "a posição que reúne os eixos", PURPLE)]


def b_funil(c, t, C, B):
    head(c, t, B["start"], "DO TEMA AO SEU TEXTO", "O FUNIL · ENEM 2020", BLUE)
    card(c, *CARD_R)
    cx = 820
    for k, (cue, lab, s, col) in enumerate(FUNIL):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        w = 1100 - k * 210
        y = 200 + k * 150
        p = skia.Path()
        p.moveTo(cx - w / 2, y); p.lineTo(cx + w / 2, y); p.lineTo(cx + (w - 210) / 2, y + 130); p.lineTo(cx - (w - 210) / 2, y + 130); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", col, 0.16), a))
        c.drawPath(p, paint(col, a, stroke=3))
        text(c, lab, cx, y + 48, 26, "black", col, a)
        sz = 26 if len(s) < 40 else 22
        para(c, s, cx, y + 88, sz, "bold", INK, a, w - 260, 28, align="center")
    ac = ep(t, C["22.c"], 0.5)
    if ac > 0:
        line(c, 1440, 210, 1440, 480, BLUE, ac, 5)
        text(c, "a prova", 1480, 330, 34, "black", BLUE, ac, align="left")
        text(c, "TE DÁ", 1480, 375, 34, "black", BLUE, ac, align="left")
    ae = ep(t, C["23.e"], 0.5)
    if ae > 0:
        line(c, 1440, 510, 1440, 780, GREEN, ae, 5)
        text(c, "VOCÊ", 1480, 630, 34, "black", GREEN, ae, align="left")
        text(c, "constrói", 1480, 675, 34, "black", GREEN, ae, align="left")
    pill(c, "EIXO = cada linha de argumento que você escolhe seguir", 820, 840, GREEN, size=22,
         a=ep(t, C["23.a"] + 0.8, 0.4) * (1 - ep(t, C["23.d"], 0.4)), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco F — foco não é corte
# ======================================================================

def b_corte(c, t, C, B):
    head_seq(c, t, C, [("24", "FOCO", "NÃO É CORTE DO TEMA", AMBER), ("25", "TANGENCIAR", "PASSAR RASPANDO PELO TEMA", RED)])
    card(c, *CARD_R)
    a25 = ep(t, C["25"], 0.6)
    for k, (cue, cue2, tt, s, res, col) in enumerate((("24.a", "24.a2", "ESTIGMA DAS DOENÇAS MENTAIS", "só DUAS causas do estigma", "FOCO LEGÍTIMO · escolheu a porta", GREEN),
                                                     ("24.b", "24.b2", "ESTIGMA DAS DOENÇAS MENTAIS", "saúde mental SEM falar de estigma", "ASSUNTO AMPLO · trocou de endereço", RED))):
        a, d = rise(t, C[cue])
        a *= (1 - 0.5 * a25)
        if a <= 0:
            continue
        x = 220 + k * 760
        rrect(c, x, 200 + d, 720, 330, 22, mix("#FFFFFF", col, 0.07), a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 200 + d, 720, 330), 22, 22), paint(col, a * ep(t, C[cue2], 0.4), stroke=5))
        text(c, "tema: " + tt.lower(), x + 40, 250 + d, 22, "bold", GRAY, a, align="left")
        para(c, s, x + 40, 320 + d, 42, "black", INK, a, 640, 50)
        ra = ep(t, C[cue2], 0.4)
        check_icon(c, x + 60, 470 + d, 22, a * ra, col, "check" if col == GREEN else "x")
        text(c, res, x + 96, 482 + d, 28, "black", col, a * ra, align="left")
    if a25 > 0:
        text(c, "TANGENCIAR = ficar só no assunto amplo", W / 2, 620, 40, "black", RED, ep(t, C["25.t"], 0.5))
        check_icon(c, 520, 700, 24, ep(t, C["25.a"], 0.4), GREEN)
        text(c, "escolher eixos: PERMITIDO", 560, 712, 34, "black", GREEN, ep(t, C["25.a"], 0.4), align="left")
        check_icon(c, 1060, 700, 24, ep(t, C["25.b"], 0.4), RED, "x")
        text(c, "tirar um bloco: NÃO", 1100, 712, 34, "black", RED, ep(t, C["25.b"], 0.4), align="left")
        pill(c, "escolher um foco NÃO é tangenciar", W / 2, 800, AMBER, size=30, a=ep(t, C["25.c"], 0.5), anchor="center")


# ======================================================================
# bloco G — a pergunta-problema
# ======================================================================

def b_pergunta(c, t, C, B):
    head_seq(c, t, C, [("26", "PRENDA O TEXTO NO ENDEREÇO", "A PERGUNTA-PROBLEMA", GREEN), ("27", "O TEXTO SAI", "DA PERGUNTA", GREEN)])
    card(c, *CARD_R)
    a27 = ep(t, C["27"], 0.6)
    aa = ep(t, C["26.a"], 0.5)
    y0 = lerp(260, 200, a27)
    if aa > 0:
        boxed(c, 260, y0 - 40, 1400, 80 if a27 > 0.5 else 90, BLUE, aa * (1 - a27), 0.08)
        text_mid(c, "frase temática  →  PERGUNTA", W / 2, y0, 40, "black", BLUE, aa * (1 - a27))
    ab = ep(t, C["26.b"], 0.5)
    if ab > 0:
        y = lerp(360, 200, a27)
        paper(c, 260, y, 1400, 150, ab, lh=52, top=y + 30, margin=False)
        sp = (C["26.b"] + 0.5, C["26.b"] + 6.0)
        hand_para(c, "Por que o estigma associado às doenças mentais persiste na sociedade brasileira, e como enfrentá-lo?",
                  300, y + 62, 32, PEN, ab, 1320, 52, wreveal(t, sp))
    if a27 > 0:
        rows = [("27.a", "TESE", "a RESPOSTA à pergunta", BLUE), ("27.b", "DESENVOLVIMENTO", "os parágrafos do meio: as RAZÕES", GREEN),
                ("28.a", "CONCLUSÃO", "o último parágrafo: a PROPOSTA", PURPLE)]
        for k, (cue, lab, s, col) in enumerate(rows):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 440 + k * 120 + d
            arrow(c, 300, 380, 300, y, LIGHT, a, 4, 12)
            rrect(c, 330, y - 40, 1300, 90, 16, mix("#FFFFFF", col, 0.08), a)
            text(c, lab, 370, y + 14, 34, "black", col, a, align="left")
            text(c, s, 820, y + 14, 32, "bold", INK, a, align="left")


# ======================================================================
# nós fazemos — 2017
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("29", "SUA VEZ · ENEM 2017", "BLOCOS E PERGUNTA", GREEN), ("30", "VAMOS CONFERIR", "BLOCOS E PERGUNTA", GREEN)])
    card(c, *CARD_R)
    ab = ep(t, C["29.b"], 0.5)
    rrect(c, 260, 200, 1400, 120, 16, "#FFFFFF", ab, shadow=True)
    lay = seg_layout(T17, 300, 275, 48, 1320, 60, handw=False)
    draw_segs(c, t, C, T17, lay, 48, ab, handw=False)
    pause_timer(c, t, C["29.end"] - 1.9, 1560, 520)
    show = [ep(t, C[s[4]] + 0.4, 0.4) for s in T17]
    puzzle(c, t, C, T17, 440, 1.0, 28, show, obriga=False)
    ac = ep(t, C["31.a"], 0.5)
    if ac > 0:
        paper(c, 260, 600, 1400, 200, ac, lh=52, top=630, margin=False)
        text(c, "PERGUNTA-PROBLEMA", 300, 640, 18, "black", GRAY, ac, align="left", tracking=2)
        hand_para(c, "Quais obstáculos dificultam a formação educacional de surdos no Brasil, e como superá-los?",
                  300, 700, 32, PEN, ac, 1320, 52, wreveal(t, (C["31.a"] + 0.3, C["31.b"] - 0.3)))
    pill(c, "todos os blocos dentro da pergunta", 1460, 840, GREEN, size=24, a=ep(t, C["31.b"], 0.5), anchor="center", bounds=(0, 1920))
    if t < C["30"]:
        ins = [("29.c", "1. divida em blocos (2 cores)"), ("29.d", "2. escreva a pergunta-problema")]
        for k, (cue, s) in enumerate(ins):
            a = ep(t, C[cue], 0.4)
            text(c, s, 300, 640 + k * 60, 38, "black", INK, a, align="left")


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Cada bloco é uma exigência.", "Escolha a porta, não troque de endereço.",
          "Transforme o tema em pergunta; a tese é a resposta."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["32", "44"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "32" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 48, "black", INK, a, align="left")


ERROS = [("33", "Ler só o NÚCLEO e esquecer os delimitadores", "o núcleo é a palavra mais forte da frase", "cada delimitador é parte do endereço: sublinhe todos"),
         ("34", "Achar que “no Brasil” é enfeite", "quase todo tema termina assim", "“no Brasil” é EXIGÊNCIA: fale da realidade daqui"),
         ("35", "Confundir escolher um foco com tangenciar", "nos dois casos você não fala de tudo", "o foco escolhe a porta e mantém todos os blocos")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS ERROS CLÁSSICOS", RED)
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
    para(c, fix, 360, 694, 40, "black", GREEN, ac, 1300)


# ======================================================================
# questões 5 e 7
# ======================================================================

def alts_panel(c, t, C, alts, x, y0, w, size, aok_cue, okL, d_line=6):
    aok = ep(t, C[aok_cue], 0.5)
    y = y0
    for L, s, cue_in, cx, why, col in alts:
        a, d = rise(t, C[cue_in])
        lines = wrap(s, "bold", size, w - 60)
        hh = len(lines) * (size + d_line) + 12 + (26 if cx else 0)
        ok = L == okL
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 20, y - size - 6 + d, w + 30, hh + 8, 12, GREEN, 0.15 * aok)
            badge_num(c, L, x + 6, y - size * 0.35 + d, a, 18, bg=GREEN if ok and aok > 0.5 else INK)
            ax = ep(t, C[cx], 0.4) if cx else 0
            for j, ln in enumerate(lines):
                yy = y + d + j * (size + d_line)
                text(c, ln, x + 40, yy, size, "bold", INK, a * (1 - 0.5 * ax), align="left")
                if ax > 0:
                    strike(c, x + 36, yy - size * 0.35, x + 44 + text_w(ln, "bold", size), yy - size * 0.35, ax, RED, ax)
            if ax > 0:
                pill(c, why, x + 40, y + d + len(lines) * (size + d_line) + 2, col, size=16, a=ax, bounds=(0, 1920))
        y += hh + 12


ALT5 = [("A", "introdução sobre a origem das grandes religiões; desenvolvimento descrevendo as crenças de cada uma; conclusão sobre a importância da fé.", "37.a", "39.xa", "sem intolerância e sem combater", RED),
        ("B", "introdução sobre a intolerância em geral; desenvolvimento sobre preconceito racial e polarização política; conclusão pedindo mais respeito entre as pessoas.", "37.b", "39.xb", "perdeu o “religiosa”", RED),
        ("C", "introdução com a garantia constitucional da liberdade de crença; desenvolvimento sobre a desinformação acerca das religiões de matriz africana e a impunidade dos ataques a templos no país; conclusão com ações de educação e de responsabilização.", "37.c", None, "", GREEN),
        ("D", "introdução sobre as guerras religiosas na Europa; desenvolvimento sobre conflitos religiosos no Oriente Médio; conclusão sobre a paz mundial.", "38.d", "39.xd", "tirou o Brasil", RED),
        ("E", "relato, do início ao fim, da história de uma família vítima de intolerância, sem defesa de ponto de vista.", "38.e", "39.xe", "não defende ponto de vista", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · ENEM 2016", "O PLANEJAMENTO QUE COBRE O RECORTE", BLUE)
    card(c, *CARD_R)
    alt_on = ep(t, C["37"], 0.7)
    a0 = ep(t, C["36.a"], 0.5)
    x = lerp(260, 170, alt_on)
    w = lerp(1400, 560, alt_on)
    sz = lerp(46, 28, alt_on)
    text(c, "Tema do Enem 2016:", x, lerp(240, 220, alt_on), 26, "bold", GRAY, a0, align="left")
    lay = seg_layout(T16, x, lerp(320, 270, alt_on), sz, w, sz * 1.3, handw=False)
    draw_segs(c, t, C, T16, lay, sz, ep(t, C["36.b"], 0.5), handw=False)
    if alt_on < 1:
        show = [ep(t, C[s[4]] + 0.3, 0.4) for s in T16]
        puzzle(c, t, C, T16, 460, 1 - alt_on, 28, show, obriga=False)
    enun = "O planejamento que atende ao recorte completo desse tema é:"
    if alt_on < 0.5:
        text(c, enun, x, 700, 32, "bold", INK, ep(t, C["36.f"], 0.5), align="left")
    else:
        para(c, enun, x, 420, 24, "bold", INK, ep(t, C["36.f"], 0.5), w, 30)
    text(c, "Questão do material de estudo (seção 12)", x, 820, 16, "medium", GRAY, a0 * alt_on, align="left")
    if alt_on > 0:
        alts_panel(c, t, C, ALT5, 790, 222, 950, 21, "39.ok", "C", 5)
        pause_timer(c, t, C["38.end"] - 1.9, 440, 640)
        result_box(c, "Letra C", 440, 700, 52, ep(t, C["39.ok"], 0.5), GREEN)


ALT7 = [("A", "tangencia o tema, pois deixa de fora outros aspectos possíveis do trabalho de cuidado.", "41.a", "42.xa", "confunde foco com corte", RED),
        ("B", "foge ao tema, pois creches e serviços de apoio a idosos são assuntos de outra área.", "41.b", "42.xb", "creche divide o cuidado", RED),
        ("C", "só atenderia ao tema se comentasse, um a um, todos os textos motivadores da proposta.", "41.c", "43.xc", "inventa uma exigência", RED),
        ("D", "tangencia o tema, pois a frase temática fala em “desafios”, e não em políticas públicas.", "41.d", "43.xd", "a falta de políticas É um desafio", RED),
        ("E", "é legítimo: escolher eixos dentro do recorte define o foco do texto, sem retirar nenhum bloco da frase temática.", "41.e", None, "", GREEN)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · ENEM 2023", "FOCO OU TANGENCIAMENTO?", BLUE)
    card(c, *CARD_R)
    alt_on = ep(t, C["41"], 0.7)
    x, w = 170, lerp(1400, 560, alt_on)
    sz = lerp(30, 21, alt_on)
    y = 220
    blocks = [("40.a", "Tema de 2023: o trabalho de cuidado realizado pela mulher no Brasil."),
              ("40.b", "Uma estudante planejou discutir só dois aspectos:"),
              ("40.c", "• a herança de uma divisão de tarefas que atribui o cuidado às mulheres;"),
              ("40.d", "• a falta de políticas públicas, como creches e serviços de apoio a idosos, que dividam esse trabalho."),
              ("40.e", "Sua tese menciona o trabalho de cuidado, a mulher, a invisibilidade e o Brasil."),
              ("40.f", "Sobre esse planejamento, é correto afirmar que")]
    for cue, s in blocks:
        a = ep(t, C[cue], 0.4)
        hl = s.startswith("•")
        y += para(c, s, x, y, sz, "black" if hl else "bold", GREEN if hl else INK, a, w, sz * 1.3) + sz * 0.5
    # conferência dos blocos na tese (cena 42)
    ks = [("42.k1", "trabalho de cuidado", NUC), ("42.k2", "mulher", DEL), ("42.k3", "invisibilidade", DEL), ("42.k4", "Brasil", DEL),
          ("42.k5", "desafios (falta de políticas)", DEL)]
    for k, (cue, s, col) in enumerate(ks):
        a = ep(t, C[cue], 0.3) * (1 - ep(t, C["42.xa"], 0.4))
        if a > 0:
            check_icon(c, 200, 640 + k * 42, 14, a, GREEN)
            text(c, s, 230, 650 + k * 42, 24, "black", col, a, align="left")
    if alt_on > 0:
        alts_panel(c, t, C, ALT7, 790, 222, 950, 22, "43.ok", "E", 6)
        pause_timer(c, t, C["41.end"] - 1.9, 440, 700)
        result_box(c, "Letra E", 440, 760, 52, ep(t, C["43.ok"], 0.5), GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "TEXTOS MOTIVADORES E A CÓPIA", PURPLE)
    aa = ep(t, C["45.a"], 0.5)
    for k in range(3):
        a = aa * ep(t, C["45.a"] + 0.3 * k, 0.4)
        x = 300 + k * 260
        rrect(c, x, 240, 220, 280, 12, "#FFFFFF", a, shadow=True)
        text(c, "TEXTO " + "I" * (k + 1), x + 110, 280, 18, "black", GRAY, a, tracking=1)
        for j in range(6):
            line(c, x + 24, 320 + j * 30, x + 196 - (j % 2) * 30, 320 + j * 30, LIGHT, a, 7)
    pill(c, "ajudam muito", 560, 580, GREEN, size=28, a=ep(t, C["45.b"], 0.5), anchor="center", bounds=(0, 1920))
    ac = ep(t, C["45.c"], 0.5)
    if ac > 0:
        paper(c, 1120, 240, 520, 360, ac, lh=48, top=280)
        gone = ep(t, C["45.c"] + 1.2, 1.0)
        for j in range(5):
            copied = j == 2
            col = RED if copied else PEN
            al = ac * (1 - gone if copied else 1)
            line(c, 1200, 300 + j * 48, 1580 - (j % 2) * 60, 300 + j * 48, col, al, 6)
        if gone > 0:
            text(c, "linha copiada = deixa de existir", 1380, 660, 26, "black", RED, gone)
    pill(c, "ep. 3 · textos motivadores e o risco da cópia", W / 2, 780, PURPLE, size=32, a=ep(t, C["45.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["46.like"], C["46.sub"], C["46.bell"], C["46.com"], C["46.bye"], "Qual foi a sua pergunta-problema para 2017?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, caneta=b_caneta, prereq=b_prereq, etiqueta=b_etiqueta, nucleo=b_nucleo,
              tipos=b_tipos, eufaco=b_eufaco, aberturas=b_aberturas, cores=b_cores, foco=b_foco, porta=b_porta, funil=b_funil,
              corte=b_corte, pergunta=b_pergunta, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q5=b_q5, q7=b_q7,
              ponte=b_ponte, cta=b_cta)
