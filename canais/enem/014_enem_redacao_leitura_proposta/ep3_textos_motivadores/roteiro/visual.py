"""Visual — Redação ENEM, Leitura da Proposta, Episódio 3: Textos motivadores — como usar sem copiar (tema claro).
Reaproveita o ep2 (V2: peças, alternativas, rascunho) e, por ele, o ep1 (V1: folha manuscrita, etiqueta, caminhão).
Novo: FOLHA DE REDAÇÃO com linhas numeradas — linha copiada vira LINHA FANTASMA e o contador de linhas válidas cai;
GPS (celular com rota até o endereço); colunas cópia × uso autônomo com o acréscimo próprio em verde.
Cores: azul = definição · verde = dica/método · âmbar = armadilha · vermelho = erro/penalidade · roxo = regra oficial.
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

_p = Path(__file__).resolve().parents[2] / "ep2_frase_tematica_blocos" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v_ep2", _p)
V2 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V2)
V1 = V2.V1
motor.set_theme("claro")
try:
    V1._SC = {s["id"]: s for s in json.load(open(Path(__file__).resolve().parent.parent / "audio" / "tempos.json",
                                                 encoding="utf-8"))["scenes"]}
except Exception:
    V1._SC = {}

paper, hand, hand_w, hwrap, hand_para = V1.paper, V1.hand, V1.hand_w, V1.hwrap, V1.hand_para
underline, etiqueta, caixa, truck = V1.underline, V1.etiqueta, V1.caixa, V1.truck
boxed, regra, selo, pause_timer, which, para, wrap = V1.boxed, V1.regra, V1.selo, V1.pause_timer, V1.which, V1.para, V1.wrap
frame, head_seq, xmark, wreveal = V1.frame, V1.head_seq, V1.xmark, V1.wreveal
alts_panel, puzzle, piece = V2.alts_panel, V2.puzzle, V2.piece
PEN = V1.PEN

MARCA = ""
ARQUIVO_FINAL = "enem_redacao_leitura_proposta_ep3_textos_motivadores.mp4"
CARD_R = (140, 150, 1640, 690)

MOT = "Em muitas cidades brasileiras, centros culturais fecharam as portas por falta de público e de verba."
COPIA = MOT + " Isso é um problema muito grave para o país."
AUT_A = "O fechamento de espaços culturais por escassez de recursos, apontado na própria discussão sobre o tema, não é causa isolada:"
AUT_B = "ele resulta de políticas que concentram investimentos nas capitais e deixam o interior sem programação regular."
EXE = "Muitos trabalhadores das grandes cidades brasileiras passam horas no transporte público todos os dias."
EXE_A = "O longo tempo gasto no deslocamento diário, comum nas metrópoles do país, não acontece por acaso:"
EXE_B = "ele resulta de bairros afastados dos locais de trabalho."


# ======================================================================
# folha de redação com linhas fantasmas
# ======================================================================

def folha(c, x, y, w, n, a, t=0.0, ghosts=None, partial=None, counter=None, lh=44, rows_drawn=None, title="FOLHA DE REDAÇÃO"):
    """n linhas numeradas com 'escrita'; ghosts = {índice: 0..1} (linha some); partial = índices com trecho copiado
    destacado (âmbar no começo da linha); counter = (valor, cor) no topo."""
    if a <= 0:
        return
    h = 90 + n * lh + 30
    rrect(c, x, y, w, h, 12, "#FFFFFF", a, shadow=True)
    text(c, title, x + 30, y + 44, 18, "black", GRAY, a, align="left", tracking=2)
    ghosts = ghosts or {}
    partial = partial or ()
    rows = rows_drawn if rows_drawn is not None else n
    for i in range(n):
        yy = y + 90 + i * lh
        text(c, f"{i + 1:02d}", x + 40, yy + 6, 16, "bold", LIGHT, a, align="right")
        line(c, x + 54, yy + 14, x + w - 24, yy + 14, LINE, a, 1.5)
        if i >= rows:
            continue
        g = ghosts.get(i, 0.0)
        la = a * (1 - 0.82 * g)
        L = (w - 110) * (0.78 + 0.18 * math.sin(i * 1.7 + 0.4))
        if i in partial:
            cut = L * 0.45
            line(c, x + 64, yy + 2, x + 64 + cut, yy + 2, AMBER if g < 0.5 else LIGHT, la, 9)
            line(c, x + 64 + cut + 12, yy + 2, x + 64 + L, yy + 2, PEN, la, 6)
        else:
            line(c, x + 64, yy + 2, x + 64 + L, yy + 2, PEN, la, 6)
        if g > 0:
            p = paint(RED, a * g, stroke=2)
            p.setPathEffect(skia.DashPathEffect.Make([10, 7], 0))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 56, yy - 16, w - 76, 34), 8, 8), p)
    if counter:
        val, col = counter
        rrect(c, x + w - 230, y + 14, 210, 56, 12, mix("#FFFFFF", col, 0.12), a)
        text(c, "linhas válidas", x + w - 125, y + 36, 16, "bold", GRAY, a)
        text(c, str(val), x + w - 125, y + 64, 28, "black", col, a)
    return h


def ghost_label(c, x, y, a):
    pill(c, "LINHA FANTASMA", x, y, RED, size=20, a=a, bounds=(0, 1920))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM", "TEXTOS MOTIVADORES SEM CÓPIA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    gb = ep(t, C["01.b"], 0.8)
    gc = ep(t, C["01.c"], 0.8)
    ghosts = {2: gb, 4: gc, 6: gc, 7: gc}
    val = 10 - (1 if gb > 0.5 else 0) - (3 if gc > 0.5 else 0)
    col = RED if val <= 7 else (AMBER if val < 10 else GREEN)
    folha(c, 300, 190, 760, 10, aa, t, ghosts, partial=(2,), counter=(val, col))
    pill(c, "“só copiei uma frase...”", 1450, 300, AMBER, size=30, a=aa, anchor="center", bounds=(0, 1920))
    text(c, "some da contagem", 1450, 430, 40, "black", RED, gb)
    if gc > 0:
        selo(c, 1450, 600, gc, "TEXTO INSUFICIENTE", RED, -6, 40)
        text(c, "nota zero", 1450, 720, 48, "black", RED, ep(t, C["01.c"] + 1.0, 0.4))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "ler os textos motivadores", "como um CORRETOR"), ("02.b", "usar as ideias deles", "SEM COPIAR uma linha")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 190 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")
        text(c, sub, 400, y + 60, 40, "black", GREEN, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRANDO OS EPISÓDIOS 1 E 2", "EM 30 SEGUNDOS", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    rows = [("ENDEREÇO COMPLETO = TEMA", V1.TEMA25, aa, BLUE, None, 0)]
    etiqueta(c, 460, 200, 1000, aa, rows)
    show = [ep(t, C["03.b"] + 0.25 * i, 0.4) for i in range(5)]
    puzzle(c, t, C, V2.T23, 600, ep(t, C["03.b"], 0.5), 24, show, obriga=False)
    text(c, "cada bloco, uma exigência", W / 2, 790, 32, "black", GREEN, ep(t, C["03.b"] + 1.4, 0.5))


# ======================================================================
# bloco A — GPS e a Cartilha
# ======================================================================

def celular(c, x, y, a, t, prog_=1.0, pin_lbl="O TEMA"):
    if a <= 0:
        return
    w, h = 360, 620
    rrect(c, x, y, w, h, 46, "#1C1C1E", a, shadow=True)
    rrect(c, x + 18, y + 40, w - 36, h - 80, 30, "#EAF1E6", a)
    for k in range(5):
        line(c, x + 30, y + 120 + k * 100, x + w - 30, y + 90 + k * 100, "#FFFFFF", a, 14)
    for k in range(3):
        line(c, x + 80 + k * 100, y + 60, x + 60 + k * 110, y + h - 60, "#FFFFFF", a, 14)
    pth = skia.Path()
    pts = [(x + 70, y + h - 90), (x + 120, y + 420), (x + 230, y + 380), (x + 260, y + 220), (x + 290, y + 150)]
    pth.moveTo(*pts[0])
    for p in pts[1:]:
        pth.lineTo(*p)
    pm = skia.PathMeasure(pth, False)
    seg = skia.Path()
    pm.getSegment(0, pm.getLength() * clamp(prog_), seg, True)
    c.drawPath(seg, paint(BLUE, a, stroke=9, cap_round=True))
    px, py = pts[-1]
    c.drawCircle(px, py - 26, 22, paint(RED, a))
    c.drawCircle(px, py - 26, 8, paint("#FFFFFF", a))
    pill(c, pin_lbl, px, py - 74, BLUE, size=18, a=a, anchor="center", bounds=(0, 1920))


def b_gps(c, t, C, B):
    head_seq(c, t, C, [("04", "O QUE O GPS", "FAZ POR VOCÊ?", BLUE), ("05", "O GPS DA REDAÇÃO", "TEXTOS MOTIVADORES", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["04.t"], 0.5)
    celular(c, 300, 190, a0, t, ep(t, C["04.a"], 1.6))
    rows = [("04.a", "mostra o caminho", GREEN, True), ("04.b", "avisa onde virar", GREEN, True), ("04.c", "NÃO dirige por você", RED, False)]
    a5 = ep(t, C["05"], 0.5)
    for k, (cue, s, col, ok) in enumerate(rows):
        a = ep(t, C[cue], 0.4) * (1 - a5)
        check_icon(c, 800, 290 + k * 90, 24, a, col, "check" if ok else "x")
        text(c, s, 840, 304 + k * 90, 42, "black", col if not ok else INK, a, align="left")
    ad = ep(t, C["04.d"], 0.5) * (1 - a5)
    if ad > 0:
        truck(c, 820, 600, ad, BLUE, 0.9)
        text(c, "a entrega é SUA", 1120, 670, 44, "black", BLUE, ad, align="left")
    if a5 > 0:
        text(c, "TEXTOS MOTIVADORES", 1180, 330, 52, "black", BLUE, a5)
        text(c, "os textos que a prova traz junto com o tema", 1180, 400, 30, "bold", INK2, ep(t, C["05.a"], 0.4))
        pill(c, "mostram onde fica o endereço", 1180, 520, GREEN, size=30, a=ep(t, C["05.b"], 0.4), anchor="center", bounds=(0, 1920))
        pill(c, "a entrega é SUA", 1180, 610, BLUE, size=34, a=ep(t, C["05.c"], 0.4), anchor="center", bounds=(0, 1920))


GENEROS = [("07.b", "dados do Censo 2022 (IBGE)"), ("07.c", "pictogramas de pessoas idosas"), ("07.d", "artigo de opinião"),
           ("07.e", "infográfico"), ("07.f", "trecho de conto"), ("07.g", "resenha de documentário")]


def b_cartilha(c, t, C, B):
    head_seq(c, t, C, [("06", "O QUE DIZ A", "CARTILHA DO PARTICIPANTE", PURPLE), ("07", "A PROPOSTA DE 2025", "GÊNEROS DIFERENTES", BLUE)])
    card(c, *CARD_R)
    a7 = ep(t, C["07"], 0.6)
    a0 = ep(t, C["06.a"], 0.5) * (1 - a7)
    if a0 > 0:
        for k, (lab, sub) in enumerate((("VERBAL", "feito de palavras"), ("NÃO VERBAL", "imagens, gráficos, números"))):
            x = 560 + k * 800
            ak = a0 * ep(t, C["06.b"] + 0.4 * k, 0.4)
            rrect(c, x - 280, 210, 560, 250, 20, "#F7F7F5", ak)
            if k == 0:
                for j in range(4):
                    line(c, x - 200, 260 + j * 34, x + 200 - (j % 2) * 60, 260 + j * 34, LIGHT, ak, 9)
            else:
                for j, hh in enumerate((0.4, 0.7, 0.5, 0.9)):
                    rrect(c, x - 150 + j * 80, 380 - 130 * hh, 56, 130 * hh, 6, BLUE, ak * 0.8)
            text(c, lab, x, 420, 34, "black", INK, ak)
            text(c, sub, x, 500, 28, "bold", GRAY, ak)
        ac = ep(t, C["06.c"], 0.5) * (1 - a7)
        boxed(c, 360, 580, 1200, 140, PURPLE, ac, 0.08)
        text(c, "remetem ao tema", W / 2, 630, 30, "bold", INK2, ac)
        text(c, "“a fim de orientar sua reflexão”", W / 2, 690, 44, "black", PURPLE, ac)
    if a7 > 0:
        for k, (cue, s) in enumerate(GENEROS):
            a, d = rise(t, C[cue])
            a *= a7
            x = 260 + (k % 3) * 480
            y = 230 + (k // 3) * 200 + d
            rrect(c, x, y, 440, 160, 18, "#FFFFFF", a, shadow=True)
            para(c, s, x + 220, y + 70, 32, "black", INK, a, 380, 38, align="center")
        ah = ep(t, C["07.h"], 0.5)
        text(c, "gêneros diferentes iluminando O MESMO TEMA", W / 2, 700, 36, "black", BLUE, ah)
        pill(c, "o conjunto = COLETÂNEA", W / 2, 790, BLUE, size=30, a=ep(t, C["07.h"] + 2.0, 0.4), anchor="center")


# ======================================================================
# bloco B — os três passos
# ======================================================================

PASSOS = [("08.a", "08.b", "Observar a posição dos autores e a SITUAÇÃO-PROBLEMA", "sublinhe a frase que resume o problema", "sub"),
          ("09.a", "09.b", "Identificar o ponto de vista e os argumentos", "anote na margem o que cada texto defende", "mar"),
          ("10.a", "10.b", "Refletir, definir a SUA posição e juntar o que você sabe", "liste o que os textos NÃO dizem", "lis")]


def b_passos(c, t, C, B):
    head(c, t, B["start"], "LER COMO UM CORRETOR", "OS 3 PASSOS DA CARTILHA", PURPLE)
    card(c, *CARD_R)
    text(c, "SEGUNDO A CARTILHA", 300, 215, 20, "black", PURPLE, ep(t, C["08.t"], 0.4), align="left", tracking=2)
    text(c, "NA PRÁTICA", 1120, 215, 20, "black", GREEN, ep(t, C["08.t"], 0.4), align="left", tracking=2)
    for k, (ca, cb, s1, s2, ic) in enumerate(PASSOS):
        a, d = rise(t, C[ca])
        if a <= 0:
            continue
        y = 300 + k * 165 + d
        badge_num(c, k + 1, 250, y, a, 30, bg=PURPLE)
        para(c, s1, 300, y - 10, 30, "black", INK, a, 760, 36)
        b = ep(t, C[cb], 0.4)
        rrect(c, 1100, y - 50, 560, 120, 16, mix("#FFFFFF", GREEN, 0.08), b)
        para(c, s2, 1130, y - 2, 28, "black", GREEN, b, 500, 34)
        if ic == "sub" and b > 0:
            underline(c, 1130, 1600, y + 56, GREEN, b, ep(t, C[cb] + 0.4, 0.6), 5)
    ac = ep(t, C["10.c"], 0.4)
    for k, s in enumerate(("leis", "fatos", "obras", "conceitos")):
        pill(c, s, 1130 + k * 135, 830, GREEN, size=22, a=ac * ep(t, C["10.c"] + 0.3 * k, 0.3), bounds=(0, 1920))


# ======================================================================
# bloco C — ponto de partida
# ======================================================================

def b_partida(c, t, C, B):
    head_seq(c, t, C, [("11", "POSSO USAR AS IDEIAS?", "PONTO DE PARTIDA", GREEN), ("12", "SÓ REPETIR A COLETÂNEA?", "NÍVEIS MÉDIOS", AMBER)])
    card(c, *CARD_R)
    a12 = ep(t, C["12"], 0.6)
    aa = ep(t, C["11.a"], 0.5) * (1 - a12)
    if aa > 0:
        rrect(c, 260, 230, 620, 380, 22, mix("#FFFFFF", BLUE, 0.06), aa)
        text(c, "COLETÂNEA", 570, 290, 28, "black", BLUE, aa, tracking=2)
        for k in range(3):
            rrect(c, 300 + k * 190, 340, 160, 200, 10, "#FFFFFF", aa, shadow=True)
        check_icon(c, 330, 590, 18, ep(t, C["11.a"] + 0.6, 0.3), GREEN)
        text(c, "pode se apropriar das ideias", 360, 600, 26, "bold", GREEN, ep(t, C["11.a"] + 0.6, 0.3), align="left")
        ab = ep(t, C["11.b"], 0.5)
        pill(c, "mas não fique PRESO a elas", 570, 680, AMBER, size=26, a=ab, anchor="center", bounds=(0, 1920))
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            arrow(c, 1500, 420, 900, 420, GREEN, acc, 6, 22, progress=acc)
            text(c, "informações", 1340, 360, 40, "black", GREEN, acc)
            text(c, "DE FORA DA PROVA", 1340, 500, 44, "black", GREEN, acc)
        ad = ep(t, C["11.d"], 0.5)
        pill(c, "REPERTÓRIO = o que você sabe e leva para o texto", 1260, 680, BLUE, size=26, a=ad, anchor="center", bounds=(0, 1920))
        text(c, "(série própria)", 1260, 740, 24, "bold", GRAY, ad)
    if a12 > 0:
        aa2 = ep(t, C["12.a"], 0.5)
        x0, x1, y = 300, 1620, 360
        line(c, x0, y, x1, y, LIGHT, aa2, 8)
        for k, v in enumerate((0, 40, 80, 120, 160, 200)):
            x = lerp(x0, x1, v / 200)
            hl = v == 120
            col = AMBER if hl else INK2
            c.drawCircle(x, y, 22 if hl else 14, paint(col, aa2 * (ep(t, C["12.b"], 0.4) if hl else 1)))
            text(c, str(v), x, y + 60, 30, "black", col, aa2)
        text(c, "níveis de nota de cada competência", W / 2, 260, 30, "bold", GRAY, aa2)
        ab2 = ep(t, C["12.b"], 0.5)
        boxed(c, 360, 500, 1200, 140, PURPLE, ab2, 0.08)
        text(c, "C3 · NÍVEL 120", 400, 545, 20, "black", PURPLE, ab2, align="left", tracking=2)
        text(c, "informações “limitadas aos argumentos dos textos motivadores”", W / 2, 610, 34, "black", INK, ab2)
        pill(c, "só repete a coletânea → tende aos NÍVEIS MÉDIOS", W / 2, 740, AMBER, size=30, a=ep(t, C["12.c"], 0.5), anchor="center")


# ======================================================================
# bloco D — não verbal
# ======================================================================

def b_naoverbal(c, t, C, B):
    frame(c, t, B["start"], "NÃO VERBAL", "TAMBÉM É TEXTO", BLUE)
    a0 = ep(t, C["13.t"], 0.5)
    if a0 > 0:
        rrect(c, 260, 220, 640, 460, 18, "#FFFFFF", a0, shadow=True)
        text(c, "GRÁFICO", 300, 262, 18, "black", GRAY, a0, align="left", tracking=2)
        for k, hh in enumerate((0.35, 0.5, 0.62, 0.85)):
            rrect(c, 330 + k * 140, 640 - 320 * hh, 90, 320 * hh, 8, BLUE, a0 * ep(t, C["13.t"] + 0.2 * k, 0.4))
        line(c, 300, 642, 860, 642, INK2, a0, 3)
    ab = ep(t, C["13.b"], 0.5)
    for k, q in enumerate(("o que o dado mostra?", "qual é a comparação?", "que crítica a imagem faz?")):
        pill(c, q, 1000, 300 + k * 80, BLUE, size=28, a=ab * ep(t, C["13.b"] + 0.9 * k, 0.3), bounds=(0, 1920))
    ac = ep(t, C["13.c"], 0.5)
    check_icon(c, 1030, 590, 24, ac, RED, "x")
    text(c, "transcrever o número", 1070, 602, 38, "black", RED, ac, align="left")
    ad = ep(t, C["13.d"], 0.5)
    check_icon(c, 1030, 670, 24, ad, GREEN)
    text(c, "INTERPRETAR", 1070, 682, 44, "black", GREEN, ad, align="left")


# ======================================================================
# bloco E — a regra da cópia
# ======================================================================

def b_copia(c, t, C, B):
    head_seq(c, t, C, [("14", "O TRABALHO DA ESCOLA", "COPIADO DA INTERNET", AMBER), ("15", "O QUE DIZ O EDITAL", "LINHAS COPIADAS", PURPLE),
                       ("16", "O DETALHE", "INTEGRAL OU PARCIALMENTE", PURPLE), ("17", "E NÃO PARA POR AÍ", "A CÓPIA PESA NA NOTA", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15", "16", "17"])
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        paper(c, 300, 220, 600, 480, ep(t, C["14.t"], 0.5), lh=48, top=260)
        pill(c, "Ctrl + C · Ctrl + V", 600, 480, AMBER, size=34, a=ep(t, C["14.t"] + 0.8, 0.4), anchor="center", bounds=(0, 1920))
        xmark(c, 600, 460, 150, aa, RED, 14)
        text(c, "o professor percebia na hora", 600, 770, 30, "black", RED, aa)
        ab = ep(t, C["14.b"], 0.5)
        text(c, "CÓPIA", 1360, 360, 60, "black", BLUE, ab)
        para(c, "escrever trechos iguais aos da prova como se fossem seus", 1360, 450, 34, "bold", INK, ab, 560, 42, align="center")
        return
    a15 = ep(t, C["15.t"], 0.5)
    text(c, "EDITAL = o documento oficial com as regras do ENEM", W / 2, 215, 26, "bold", PURPLE, a15 * (1 - ep(t, C["16"], 0.4)))
    g16 = ep(t, C["16.b"], 0.8)
    ghosts = {1: ep(t, C["15.a"], 0.8), 4: g16}
    val = 12 - (1 if ghosts[1] > 0.5 else 0) - (1 if g16 > 0.5 else 0)
    folha(c, 260, 250, 820, 12, 1.0, t, ghosts, partial=(4,), counter=(val, AMBER if val < 12 else GREEN), lh=40)
    ghost_label(c, 860, 250 + 90 + 1 * 40, ep(t, C["15.a"] + 0.8, 0.4))
    pill(c, "contam só as linhas produzidas pelo participante", 1400, 330, PURPLE, size=22, a=ep(t, C["15.b"], 0.4), anchor="center", bounds=(0, 1920))
    if sid in ("16", "17"):
        aa = ep(t, C["16.a"], 0.5)
        text(c, "copiou só meia linha?", 1400, 450, 34, "black", AMBER, aa)
        text(c, "a linha INTEIRA some", 1400, 510, 40, "black", RED, ep(t, C["16.b"], 0.4))
        ghost_label(c, 860, 250 + 90 + 4 * 40, g16)
        ac = ep(t, C["16.c"], 0.5) * (1 - ep(t, C["17"], 0.4))
        if ac > 0:
            boxed(c, 1130, 580, 560, 150, RED, ac, 0.06)
            text(c, "LINHA FANTASMA", 1410, 640, 40, "black", RED, ac)
            text(c, "está no papel · não existe para o corretor", 1410, 690, 22, "bold", INK2, ac)
    if sid == "17":
        aa = ep(t, C["17.a"], 0.5)
        pill(c, "repetida: avaliada NEGATIVAMENTE", 1410, 600, RED, size=24, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "pode baixar a nota ou anular como cópia", 1410, 660, 24, "bold", INK2, aa)
        ab = ep(t, C["17.b"], 0.5)
        boxed(c, 1130, 700, 560, 130, PURPLE, ab, 0.08)
        text(c, "C2 · NÍVEL 80", 1160, 738, 18, "black", PURPLE, ab, align="left", tracking=2)
        para(c, "“recorrendo à cópia de trechos dos textos motivadores”", 1160, 778, 22, "black", INK, ab, 510, 28)


# ======================================================================
# bloco F — cópia × uso autônomo
# ======================================================================

def b_lado(c, t, C, B):
    head_seq(c, t, C, [("18", "UM TEXTO MOTIVADOR", "HIPOTÉTICO", BLUE), ("19", "LADO A LADO", "CÓPIA × USO AUTÔNOMO", BLUE)])
    card(c, *CARD_R)
    a19 = ep(t, C["19"], 0.6)
    ab = ep(t, C["18.b"], 0.5)
    y_m = lerp(330, 205, a19)
    sz = lerp(40, 24, a19)
    if ab > 0:
        rrect(c, 260, y_m - 50, 1400, lerp(170, 90, a19), 16, "#F4F5F7", ab)
        text(c, "TEXTO MOTIVADOR", 290, y_m - 18, 16, "black", GRAY, ab, align="left", tracking=2)
        para(c, "“" + MOT + "”", 290, y_m + 30, sz, "black", INK, ab, 1340, sz * 1.25)
    if a19 > 0:
        # coluna da cópia
        a1 = ep(t, C["19.a"], 0.5)
        g = ep(t, C["19.b"], 0.8)
        rrect(c, 200, 330, 720, 470, 20, mix("#FFFFFF", RED, 0.05), a1, shadow=True)
        pill(c, "CÓPIA", 240, 370, RED, size=24, a=a1, bounds=(0, 1920))
        para(c, MOT, 240, 440, 26, "bold", INK, a1 * (1 - 0.75 * g), 640, 34)
        para(c, "Isso é um problema muito grave para o país.", 240, 590, 26, "bold", INK, a1, 640, 34)
        if g > 0:
            p = paint(RED, g, stroke=2)
            p.setPathEffect(skia.DashPathEffect.Make([10, 7], 0))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(230, 405, 670, 120), 8, 8), p)
            ghost_label(c, 640, 545, g)
        check_icon(c, 250, 700, 18, ep(t, C["19.c"], 0.4), RED, "x")
        text(c, "nada é acrescentado", 280, 710, 26, "black", RED, ep(t, C["19.c"], 0.4), align="left")
        # coluna do uso autônomo
        a2 = ep(t, C["20.a"], 0.5)
        rrect(c, 1000, 330, 720, 470, 20, mix("#FFFFFF", GREEN, 0.05), a2, shadow=True)
        pill(c, "USO AUTÔNOMO", 1040, 370, GREEN, size=24, a=a2, bounds=(0, 1920))
        h1 = para(c, AUT_A, 1040, 440, 25, "bold", INK, a2, 640, 33)
        abb = ep(t, C["20.b"], 0.5)
        if abb > 0:
            rrect(c, 1030, 440 + h1 - 30, 670, 4 * 33 + 10, 10, GREEN, 0.14 * abb)
        para(c, AUT_B, 1040, 440 + h1, 25, "black", mix(INK, GREEN, abb), max(a2 * 0.3, abb), 640, 33)
        acc = ep(t, C["20.c"], 0.4)
        pill(c, "PARÁFRASE = a mesma ideia com outras palavras", 1360, 860 - 20, BLUE, size=20, a=acc * (1 - ep(t, C["20.d"], 0.4)),
             anchor="center", bounds=(0, 1920))
        pill(c, "+ uma CAUSA própria", 1360, 840, GREEN, size=26, a=ep(t, C["20.d"], 0.4), anchor="center", bounds=(0, 1920))
    text(c, "Texto motivador hipotético e trechos elaborados para fins didáticos.", 200, 868, 16, "medium", GRAY,
         ep(t, C["18.b"], 0.4), align="left")


# ======================================================================
# bloco G — texto insuficiente
# ======================================================================

def b_insuficiente(c, t, C, B):
    head(c, t, B["start"], "A CONSEQUÊNCIA MAIS GRAVE", "TEXTO INSUFICIENTE", RED)
    card(c, *CARD_R)
    aa = ep(t, C["21.a"], 0.5)
    gb = ep(t, C["21.b"], 1.2)
    ghosts = {1: gb, 3: gb, 4: gb}
    n_own = 10 - (3 if gb > 0.6 else 0)
    folha(c, 280, 190, 760, 10, aa, t, ghosts, partial=(1, 4), counter=(n_own, RED if n_own <= 7 else AMBER), lh=56)
    ab = ep(t, C["21.b"], 0.5)
    text(c, "7 linhas próprias", 1400, 330, 44, "black", RED, ab)
    text(c, "ou menos", 1400, 390, 44, "black", RED, ab)
    ac = ep(t, C["21.c"], 0.5)
    selo(c, 1400, 520, ac, "INSUFICIENTE", RED, -6, 46)
    text(c, "nota ZERO", 1400, 650, 52, "black", RED, ep(t, C["21.c"] + 0.8, 0.4))
    pill(c, "aprofundado em “Situações que zeram”", 1400, 770, PURPLE, size=22, a=ep(t, C["21.d"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco H — como retomar (eu faço)
# ======================================================================

def b_retomar(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO NO RASCUNHO", "COMO RETOMAR SEM COPIAR", GREEN)
    paper(c, 160, 160, 1600, 700, 1.0, lh=58, top=200)
    a0 = ep(t, C["22.t"], 0.4)
    text(c, "ORIGINAL:", 260, 250, 18, "black", GRAY, a0, align="left", tracking=2)
    para(c, "“" + MOT + "”", 400, 250, 24, "bold", GRAY, a0, 1280, 30)
    steps = [("22.a", "1 · TROQUE A ESTRUTURA", "22.a2", "O fechamento de espaços culturais por escassez de recursos,", PEN),
             ("23.b", "2 · RESUMA", "23.b2", "apontado na própria discussão sobre o tema, não é causa isolada:", PEN),
             ("23.c", "3 · ACRESCENTE ALGO SEU", "23.c2", AUT_B, GREEN)]
    y = 380
    for k, (cs, lab, cw, s, col) in enumerate(steps):
        a = ep(t, C[cs], 0.4)
        pill(c, lab, 260, y - 12, GREEN if k == 2 else BLUE, size=20, a=a, bounds=(0, 1920))
        sp = (C[cw], C[cw] + (4.5 if k == 2 else 3.0))
        n = hand_para(c, s, 600, y, 30, col, ep(t, C[cw], 0.2), 1100, 54, wreveal(t, sp), bold=(k == 2))
        y += max(1, n) * 54 + 34
    ad = ep(t, C["23.d"], 0.5)
    pill(c, "dado da coletânea? cite breve e INTERPRETE", 1460, 820, GREEN, size=22, a=ad, anchor="center", bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("24", "SUA VEZ", "REESCREVA + UMA CAUSA", GREEN), ("25", "UMA VERSÃO", "POSSÍVEL", GREEN)])
    card(c, *CARD_R)
    ab = ep(t, C["24.b"], 0.5)
    rrect(c, 260, 200, 1400, 150, 16, "#F4F5F7", ab)
    text(c, "TEXTO MOTIVADOR", 290, 236, 16, "black", GRAY, ab, align="left", tracking=2)
    para(c, "“" + EXE + "”", 290, 290, 32, "black", INK, ab, 1340, 40)
    text(c, "Frase elaborada para fins didáticos.", 260, 380, 18, "medium", GRAY, ab, align="left")
    acc = ep(t, C["24.c"], 0.4) * (1 - ep(t, C["25"], 0.4))
    text(c, "1. outras palavras e outra estrutura", 300, 500, 38, "black", INK, acc, align="left")
    text(c, "2. + UMA CAUSA sua", 300, 570, 38, "black", GREEN, ep(t, C["24.d"], 0.4) * (1 - ep(t, C["25"], 0.4)), align="left")
    pause_timer(c, t, C["24.end"] - 1.9, 1560, 560)
    if t >= C["25"] - 0.2:
        a = ep(t, C["25"], 0.4)
        paper(c, 260, 420, 1400, 360, a, lh=56, top=450)
        n = hand_para(c, EXE_A, 300, 500, 30, PEN, a, 1300, 56, wreveal(t, (C["25.a"], C["25.b"] - 0.2)))
        hand_para(c, EXE_B, 300, 500 + n * 56, 30, GREEN, a, 1300, 56, wreveal(t, (C["25.b"], C["25.c"] - 0.2)), bold=True)
        for k, (cue, s, col) in enumerate((("25.c", "estrutura nova", BLUE), ("25.c", "ideia curta", BLUE), ("25.d", "causa SUA", GREEN))):
            pill(c, s, 400 + k * 330, 820, col, size=24, a=ep(t, C[cue] + 0.5 * k, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["O motivador é GPS: ajuda a chegar, não faz a entrega.", "Linha copiada, mesmo em parte, é linha fantasma.",
          "Parafraseie e acrescente algo seu."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["26", "38"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "26" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 46, "black", INK, a, align="left")


ERROS = [("27", "Copiar “só um pedacinho” achando que a linha conta", "o resto da linha é seu", "a linha INTEIRA vira fantasma"),
         ("28", "Construir a redação toda com as ideias da coletânea", "são fontes oficiais da prova", "sem nada de fora, fica nos níveis médios"),
         ("29", "Transcrever o dado do gráfico sem interpretar", "número passa credibilidade", "diga o que o dado MOSTRA"),
         ("30", "Não ler os textos motivadores", "a frase temática já diz o tema", "são eles que mostram a situação-problema")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 4", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(4):
        badge_num(c, k + 1, 840 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
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
# questões 3 e 4
# ======================================================================

ALT3 = [("A", "apropriar-se das ideias dos textos motivadores para entender o problema, retomá-las por paráfrase quando necessário e acrescentar informações de fora da prova.", "31.b", None, "", GREEN),
        ("B", "reproduzir o primeiro parágrafo de um dos textos motivadores na introdução, já que ele apresenta o tema com precisão.", "31.c", "33.xb", "é cópia: linhas fantasmas", RED),
        ("C", "construir toda a argumentação com os dados dos textos motivadores, pois são fontes legítimas e dispensam outro repertório.", "32.d", "33.xc", "presa à coletânea (C3, nível 120)", RED),
        ("D", "deixar de ler os textos motivadores, pois a frase temática já contém todas as informações necessárias.", "32.e", "33.xd", "contraria ler com atenção", RED),
        ("E", "copiar trechos dos textos motivadores, desde que ocupem, ao todo, menos de sete linhas.", "32.f", "33.xe", "limite que NÃO existe", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3", "O PAPEL DOS MOTIVADORES", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["31.a"], 0.5)
    para(c, "Entre as estratégias abaixo, a que corresponde às recomendações da Cartilha do Participante para o uso dos textos motivadores é:",
         180, 240, 26, "bold", INK, a, 560, 34)
    c.save(); c.translate(300, 470); c.scale(0.55, 0.55); c.translate(-300, -470)
    celular(c, 300, 470, a * 0.9, t, 1.0)
    c.restore()
    alts_panel(c, t, C, ALT3, 790, 222, 950, 22, "33.ok", "A", 6)
    pause_timer(c, t, C["32.end"] - 1.9, 640, 540)
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


ALT4 = [("A", "como as quatro linhas são apenas parcialmente copiadas, todas as 20 linhas entram na contagem e a cópia não interfere na avaliação.", "35.a", "37.xa", "cópia parcial também tira a linha", RED),
        ("B", "a redação recebe nota zero por fuga ao tema, já que reproduziu a coletânea.", "35.b", "37.xb", "cópia não é fuga", RED),
        ("C", "as quatro linhas contam pela metade, totalizando 18 linhas válidas.", "35.c", "37.xc", "“meia linha” não existe", RED),
        ("D", "a redação é classificada como texto insuficiente, pois apresenta cópia.", "35.d", "37.xd", "16 > 7: não é insuficiente", RED),
        ("E", "as quatro linhas são desconsideradas na contagem, restando 16 linhas próprias; o texto não é insuficiente, mas a cópia é avaliada negativamente.", "35.e", None, "", GREEN)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4", "LINHAS COM CÓPIA", BLUE)
    card(c, *CARD_R)
    alt_on = ep(t, C["35"], 0.6)
    conta = ep(t, C["36"], 0.6)
    gh = ep(t, C["36.a"], 0.8)
    ghosts = {k: gh for k in (3, 7, 11, 15)}
    nval = 20 - (4 if gh > 0.5 else 0)
    sc = lerp(1.0, 0.62, max(alt_on, 0))
    c.save(); c.translate(180, 200); c.scale(sc, sc); c.translate(-180, -200)
    folha(c, 180, 200, 620, 20, ep(t, C["34.a"], 0.5), t, ghosts, partial=(3, 7, 11, 15),
          counter=(nval, GREEN if nval > 7 else RED), lh=26, rows_drawn=20)
    c.restore()
    if alt_on < 0.5:
        rows = [("34.a", "20 linhas escritas"), ("34.b", "4 linhas com um trecho copiado"), ("34.c", "o resto dessas 4 linhas é do participante"),
                ("34.d", "edital e Cartilha do Enem 2026:")]
        for k, (cue, s) in enumerate(rows):
            text(c, s, 900, 300 + k * 90, 38, "black", AMBER if k == 1 else INK, ep(t, C[cue], 0.4) * (1 - alt_on * 2), align="left")
    if alt_on > 0:
        alts_panel(c, t, C, ALT4, 790, 222, 950, 22, "37.ok", "E", 6)
        pause_timer(c, t, C["35.end"] - 1.9, 620, 520)
    if conta > 0:
        rrect(c, 170, 620, 580, 210, 18, "#FFFFFF", conta, shadow=True)
        text(c, "20 − 4 = 16", 460, 695, 54, "black", INK, ep(t, C["36.b"], 0.4))
        text(c, "16 > 7", 460, 765, 46, "black", GREEN, ep(t, C["36.c"], 0.4))
        text(c, "não é insuficiente · mas a cópia pesa", 460, 810, 22, "bold", AMBER, ep(t, C["36.d"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUANDO VOCÊ ERRA O ENDEREÇO", PURPLE)
    aa = ep(t, C["39.a"], 0.5)
    rows = [("CIDADE", "envelhecimento", aa, BLUE, None, 0), ("ENDEREÇO COMPLETO", V1.TEMA25, aa, BLUE, None, 0)]
    etiqueta(c, 230, 220, 720, aa, rows)
    ab = ep(t, C["39.b"], 0.5)
    ac = ep(t, C["39.c"], 0.5)
    if ab > 0:
        truck(c, 1100, 270, ab, AMBER, 0.8)
        text(c, "bairro errado", 1420, 330, 38, "black", AMBER, ab, align="left")
    if ac > 0:
        truck(c, 1100, 450, ac, RED, 0.8)
        text(c, "cidade errada", 1420, 510, 38, "black", RED, ac, align="left")
    pill(c, "ep. 4 · abordagem completa, tangenciamento e fuga ao tema", W / 2, 760, PURPLE, size=30, a=ep(t, C["39.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["40.like"], C["40.sub"], C["40.bell"], C["40.com"], C["40.bye"], "Como ficou a sua versão da frase do transporte?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, gps=b_gps, cartilha=b_cartilha, passos=b_passos, partida=b_partida,
              naoverbal=b_naoverbal, copia=b_copia, lado=b_lado, insuficiente=b_insuficiente, retomar=b_retomar,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q3=b_q3, q4=b_q4, ponte=b_ponte, cta=b_cta)
