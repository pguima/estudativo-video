"""Visual — Redação ENEM, Leitura da Proposta, Episódio 4: Abordagem completa, tangenciamento e fuga ao tema (tema claro).
Reaproveita o ep3 (V3) e, por ele, o ep2 (V2: peças do quebra-cabeça, alternativas) e o ep1 (V1: etiqueta, caixa, caminhão).
Novo: MAPA com as três entregas (pino verde no endereço exato, âmbar no bairro sem número, vermelho em outra cidade);
PLACAR das 5 competências (C2, C3 e C5 batem no teto de 40 no tangenciamento; tudo zera na fuga);
teses conferidas AO VIVO contra as peças da frase temática (✓/✗ embaixo de cada bloco).
Cores: azul = definição · verde = abordagem completa/método · âmbar = tangenciamento/armadilha · vermelho = fuga/erro
· roxo = regra oficial.
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

_p = Path(__file__).resolve().parents[2] / "ep3_textos_motivadores" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v_ep3", _p)
V3 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V3)
V2, V1 = V3.V2, V3.V1
motor.set_theme("claro")
try:
    V1._SC = {s["id"]: s for s in json.load(open(Path(__file__).resolve().parent.parent / "audio" / "tempos.json",
                                                 encoding="utf-8"))["scenes"]}
except Exception:
    V1._SC = {}

etiqueta, caixa, truck = V1.etiqueta, V1.caixa, V1.truck
boxed, selo, pause_timer, which, para, wrap = V1.boxed, V1.selo, V1.pause_timer, V1.which, V1.para, V1.wrap
frame, head_seq, xmark = V1.frame, V1.head_seq, V1.xmark
alts_panel, puzzle = V2.alts_panel, V2.puzzle
NUC, DEL = V2.NUC, V2.DEL

MARCA = ""
ARQUIVO_FINAL = "enem_redacao_leitura_proposta_ep4_tangenciamento_fuga.mp4"
CARD_R = (140, 150, 1640, 690)

TEMA25 = V1.TEMA25
TEMA19 = "Democratização do acesso ao cinema no Brasil"
T25 = [("Perspectivas acerca", DEL, "ORIENTAÇÃO", None, "12.b"), ("do envelhecimento", NUC, "NÚCLEO", None, "12.b"),
       ("na sociedade brasileira", DEL, "LUGAR", None, "12.b")]
T19 = [("Democratização do acesso", DEL, "RECORTE", None, "22.a"), ("ao cinema", NUC, "NÚCLEO", None, "22.a"),
       ("no Brasil", DEL, "LUGAR", None, "22.a")]
TESE1 = "O envelhecimento é um processo biológico universal, marcado pela perda gradual de funções das células."
TESE2 = "O uso excessivo de celulares prejudica a concentração dos estudantes."
TESE3 = ("No Brasil, a velhice ainda é vista sobretudo como perda, visão que alimenta o etarismo e atrasa a adaptação "
         "das cidades e dos serviços a uma população que envelhece.")
EX = ["O cinema é uma arte capaz de emocionar e de registrar a cultura de um povo.",
      "No Brasil, ir ao cinema ainda é privilégio de poucos, e democratizar esse acesso exige levar exibições a bairros e cidades que não têm salas.",
      "As redes sociais mudaram a forma como os jovens se informam."]
SIT = {"ok": ("ABORDAGEM COMPLETA", GREEN), "tg": ("TANGENCIAMENTO", AMBER), "fg": ("FUGA AO TEMA", RED)}


# ======================================================================
# peças: pino, mapa das entregas, placar das competências
# ======================================================================

def pino(c, x, y, col, a, s=1.0, sym=None):
    """pino de mapa com a ponta em (x, y); cai do alto ao aparecer"""
    if a <= 0:
        return
    dy = -60 * (1 - ease_out(clamp(a)))
    c.save(); c.translate(x, y + dy); c.scale(s, s)
    c.drawOval(skia.Rect.MakeLTRB(-16, -6, 16, 6), paint("#000000", a * 0.18))
    p = skia.Path()
    p.moveTo(0, 0); p.lineTo(-24, -44); p.lineTo(24, -44); p.close()
    c.drawPath(p, paint(col, a))
    c.drawCircle(0, -56, 28, paint(col, a))
    if sym:
        text_mid(c, sym, 0, -56, 30, "black", "#FFFFFF", a)
    else:
        c.drawCircle(0, -56, 11, paint("#FFFFFF", a))
    c.restore()


def casinha(c, x, y, a, col=INK2, s=1.0):
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s, s)
    p = skia.Path(); p.moveTo(-26, -20); p.lineTo(0, -44); p.lineTo(26, -20); p.close()
    c.drawPath(p, paint(col, a))
    c.drawRect(skia.Rect.MakeLTRB(-20, -22, 20, 10), paint(col, a))
    c.drawRect(skia.Rect.MakeLTRB(-6, -6, 6, 10), paint("#FFFFFF", a))
    c.restore()


MAPA_W, MAPA_H = 1400, 540
# pontos no sistema do mapa (sem escala)
P_CASA, P_BAIRRO, P_OUTRA = (560, 222), (430, 300), (1190, 250)


def mapa(c, x, y, s, a, pins=(0, 0, 0), bairro=0.0, labels=0.0, nomes=0.0):
    """mapa estilizado: cidade certa (grade de quarteirões, bairro e casa) + estrada + outra cidade.
    pins = alfas dos pinos (exato, bairro, outra cidade)"""
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, 0, 0, MAPA_W, MAPA_H, 26, "#EEF3E8", a, shadow=True)
    # estrada entre as cidades
    pth = skia.Path(); pth.moveTo(820, 300); pth.cubicTo(900, 330, 960, 200, 1040, 240)
    c.drawPath(pth, paint("#D9D6CC", a, stroke=26, cap_round=True))
    pp = paint("#FFFFFF", a, stroke=3); pp.setPathEffect(skia.DashPathEffect.Make([16, 12], 0))
    c.drawPath(pth, pp)
    # cidade certa: 6 x 4 quarteirões
    rrect(c, 40, 50, 780, 450, 22, "#F8F7F2", a)
    for i in range(6):
        for j in range(4):
            bx, by = 64 + i * 124, 74 + j * 104
            hl = bairro > 0 and i in (2, 3, 4) and j in (1, 2)
            rrect(c, bx, by, 104, 84, 10, mix("#E6E3D8", AMBER, 0.35 * bairro) if hl else "#E6E3D8", a)
    if bairro > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(300, 168, 380, 204), 16, 16), paint(AMBER, a * bairro, stroke=5))
        text(c, "O BAIRRO", 490, 400, 22, "black", AMBER, a * bairro, tracking=2)
    casinha(c, P_CASA[0], P_CASA[1] - 10, a, INK2, 0.9)
    text(c, "A CIDADE CERTA", 430, 40 + 0, 22, "black", GRAY, a * labels, tracking=2)
    # outra cidade: 3 x 3
    rrect(c, 1040, 90, 320, 320, 22, "#F8F7F2", a)
    for i in range(3):
        for j in range(3):
            rrect(c, 1062 + i * 100, 112 + j * 100, 76, 76, 10, "#E6E3D8", a)
    text(c, "OUTRA CIDADE", 1200, 460, 22, "black", GRAY, a * labels, tracking=2)
    pino(c, *P_CASA, GREEN, a * pins[0], 1.0)
    pino(c, *P_BAIRRO, AMBER, a * pins[1], 1.0, "?")
    pino(c, *P_OUTRA, RED, a * pins[2], 1.0)
    if nomes > 0:
        for (px, py), (nm, col), dx in ((P_CASA, SIT["ok"], 120), (P_BAIRRO, SIT["tg"], -60), (P_OUTRA, SIT["fg"], 0)):
            pass
    c.restore()


def placar(c, x, y, w, a, cap=0.0, zero=0.0, total=True, teto=True):
    """5 competências de 0 a 200. cap: C2, C3 e C5 descem até 40 · zero: tudo vai a 0"""
    if a <= 0:
        return
    vals = []
    for k in range(5):
        v = 200.0
        if k in (1, 2, 4):
            v = lerp(200, 40, ease_out(clamp(cap)))
        v = v * (1 - ease_out(clamp(zero)))
        vals.append(v)
    for k, v in enumerate(vals):
        yy = y + k * 72
        text(c, f"C{k + 1}", x, yy + 12, 30, "black", INK2, a, align="left")
        rrect(c, x + 70, yy - 16, w, 36, 10, "#EDEDEA", a)
        capped = k in (1, 2, 4) and cap > 0.02
        col = RED if zero > 0.02 else (AMBER if capped else GREEN)
        if v > 1:
            rrect(c, x + 70, yy - 16, w * v / 200, 36, 10, col, a * 0.9)
        text(c, f"{round(v)}", x + 90 + w, yy + 12, 28, "black", col, a, align="left")
    if teto and cap > 0 and zero < 0.5:
        tx = x + 70 + w * 40 / 200
        line(c, tx, y - 40, tx, y + 4 * 72 + 36, RED, a * cap * (1 - zero), 3, dash=(10, 8))
        text(c, "TETO 40", tx, y - 52, 20, "black", RED, a * cap * (1 - zero))
    if total:
        tot = sum(vals)
        text(c, "máximo possível", x + 70, y + 5 * 72 + 22, 24, "bold", GRAY, a, align="left")
        text(c, f"{round(tot)}", x + 70 + w, y + 5 * 72 + 26, 44, "black",
             RED if zero > 0.5 else (AMBER if cap > 0.5 else GREEN), a, align="right")


def centros(segs, size=26):
    ws = [text_w(s[0], "black", size) + 46 for s in segs]
    gap = 26
    x = W / 2 - (sum(ws) + gap * (len(ws) - 1)) / 2
    out = []
    for w in ws:
        out.append(x + w / 2)
        x += w + gap
    return out


def marcas(c, segs, y, alphas, oks, size=26):
    """✓ ou ✗ embaixo de cada peça"""
    for cx, a, ok in zip(centros(segs, size), alphas, oks):
        check_icon(c, cx, y, 26, a, GREEN if ok else RED, "check" if ok else "x")


def veredito(c, x, y, sit, a, size=30):
    nm, col = SIT[sit]
    pill(c, nm, x, y, col, size=size, a=a, anchor="center", bounds=(0, 1920))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM", "O ERRO SILENCIOSO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    rrect(c, 220, 230, 700, 150, 20, mix("#FFFFFF", RED, 0.06), aa)
    text(c, "FUGIU AO TEMA", 260, 285, 26, "black", RED, aa, align="left", tracking=2)
    text(c, "geralmente percebe", 260, 345, 42, "black", INK, aa, align="left")
    ab = ep(t, C["01.b"], 0.5)
    rrect(c, 220, 420, 700, 150, 20, mix("#FFFFFF", AMBER, 0.08), ab)
    text(c, "TANGENCIOU", 260, 475, 26, "black", AMBER, ab, align="left", tracking=2)
    text(c, "quase NUNCA percebe", 260, 535, 42, "black", INK, ab, align="left")
    acc = ep(t, C["01.c"], 0.5)
    text(c, "até −480 pontos", 570, 680, 64, "black", RED, acc)
    text(c, "sem saber por quê", 570, 740, 30, "bold", GRAY, acc)
    ad = ep(t, C["01.d"], 0.5)
    placar(c, 1040, 300, 440, max(acc, ad) if ad <= 0 else 1.0, cap=ep(t, C["01.d"], 1.2), total=False)
    ae = ep(t, C["01.e"], 0.4)
    for k in (1, 2, 4):
        text(c, "−160", 1040 + 70 + 440 + 120, 300 + k * 72 + 12, 26, "black", RED, ae, align="left")
    text(c, "3 × (200 − 40) = 480", 1300, 700 + 40, 40, "black", RED, ep(t, C["01.f"], 0.4))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "a diferença entre as 3 situações"), ("02.b", "o que cada uma CUSTA"), ("02.c", "como se PROTEGER antes de escrever")]
    for j, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 150 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRANDO OS EPISÓDIOS 1 E 2", "EM 30 SEGUNDOS", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    ab = ep(t, C["03.b"], 0.5)
    rows = [("CIDADE = ASSUNTO", "envelhecimento", aa, INK2, None, 0), ("ENDEREÇO EXATO = TEMA", TEMA25, ab, BLUE, None, 0)]
    etiqueta(c, 360, 190, 1200, aa, rows)
    show = [ep(t, C["03.c"] + 0.3 * i, 0.4) for i in range(3)]
    puzzle(c, t, C, T25, 650, ep(t, C["03.c"], 0.5), 30, show, obriga=False)
    text(c, "cada bloco, uma exigência", W / 2, 800, 32, "black", GREEN, ep(t, C["03.d"], 0.5))


# ======================================================================
# as três entregas e o placar
# ======================================================================

def b_entregas(c, t, C, B):
    head_seq(c, t, C, [("04", "A MESMA ENCOMENDA", "TRÊS ENTREGAS", BLUE), ("05", "NA REDAÇÃO", "TRÊS NOMES OFICIAIS", PURPLE)])
    a0 = ep(t, C["04.t"], 0.5)
    s = 1.18
    x0, y0 = W / 2 - MAPA_W * s / 2, 160
    mapa(c, x0, y0, s, a0, (ep(t, C["04.a"], 0.5), ep(t, C["04.b"], 0.5), ep(t, C["04.c"], 0.5)),
         bairro=ep(t, C["04.b"], 0.6), labels=a0)
    P = lambda p: (x0 + p[0] * s, y0 + p[1] * s)
    a5 = ep(t, C["05"], 0.5)
    for (pt, cue, sub, nm_cue, sit) in ((P_CASA, "04.a", "entregue!", "05.b", "ok"),
                                         (P_BAIRRO, "04.b", "chegou perto... não chegou", "05.c", "tg"),
                                         (P_OUTRA, "04.c", "outra cidade", "05.d", "fg")):
        px, py = P(pt)
        a = ep(t, C[cue] + 0.4, 0.4)
        nm, col = SIT[sit]
        yy = py - 150 if sit == "ok" else py + 40
        pill(c, sub, px, yy, col, size=24, a=a * (1 - a5), anchor="center", bounds=(0, 1920))
        pill(c, nm, px, yy, col, size=26, a=ep(t, C[nm_cue], 0.4), anchor="center", bounds=(0, 1920))


def b_placar0(c, t, C, B):
    frame(c, t, B["start"], "COMO A NOTA É DADA", "AS 5 COMPETÊNCIAS", BLUE)
    aa = ep(t, C["06.a"], 0.5)
    placar(c, 300, 270, 620, aa, total=False)
    text(c, "COMPETÊNCIA", 1420, 300, 44, "black", BLUE, aa)
    para(c, "cada uma das 5 partes em que a nota é dividida", 1420, 360, 30, "bold", INK2, aa, 420, 38, align="center")
    text(c, "cada uma: até 200", 1420, 520, 36, "black", INK, ep(t, C["06.b"], 0.4))
    text(c, "5 × 200 = 1000", 1420, 600, 48, "black", GREEN, ep(t, C["06.c"], 0.4))
    pill(c, "guarde este placar", 1420, 720, PURPLE, size=28, a=ep(t, C["06.d"], 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# blocos A, B, C — completa, tangenciamento, fuga
# ======================================================================

def definicao(c, x, y, w, nome, col, txt, a, a_txt):
    rrect(c, x, y, w, 300, 22, mix("#FFFFFF", col, 0.07), a)
    text(c, nome, x + 40, y + 62, 40, "black", col, a, align="left")
    text(c, "CARTILHA DO PARTICIPANTE", x + 40, y + 112, 18, "black", PURPLE, a_txt, align="left", tracking=2)
    para(c, txt, x + 40, y + 160, 32, "black", INK, a_txt, w - 80, 40)


def b_completa(c, t, C, B):
    frame(c, t, B["start"], "ENDEREÇO EXATO", "ABORDAGEM COMPLETA", GREEN)
    a0 = ep(t, C["07.t"], 0.5)
    c.save(); c.translate(250, 210); c.scale(0.36, 0.36); c.translate(-250, -210)
    mapa(c, 250, 210, 1.0, a0, (1, 0, 0))
    c.restore()
    text(c, "pino no endereço exato", 500, 440, 24, "bold", GREEN, a0)
    definicao(c, 220, 480, 620, "", GREEN, "o texto discute o recorte da frase temática", ep(t, C["07.a"], 0.5), ep(t, C["07.b"], 0.5))
    text(c, "ABORDAGEM COMPLETA", 260, 542, 34, "black", GREEN, ep(t, C["07.a"], 0.5), align="left")
    ac = ep(t, C["07.c"], 0.5)
    placar(c, 1000, 280, 380, ac)
    pill(c, "avaliação NORMAL nas 5", 1270, 220, GREEN, size=26, a=ac, anchor="center", bounds=(0, 1920))
    pill(c, "nenhum teto", 1270, 790, GREEN, size=24, a=ep(t, C["07.d"], 0.4), anchor="center", bounds=(0, 1920))


def tangente(c, cx, cy, r, a, p):
    """círculo (o tema) e uma reta que só encosta nele"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(BLUE, a * 0.12))
    c.drawCircle(cx, cy, r, paint(BLUE, a, stroke=6))
    text_mid(c, "O TEMA", cx, cy, 34, "black", BLUE, a)
    y = cy - r
    line(c, cx - 380, y, cx + 380, y, AMBER, a, 7, progress=p)
    c.drawCircle(cx, y, 12 * clamp(p * 2 - 0.8), paint(AMBER, a))


def b_tangencia(c, t, C, B):
    head_seq(c, t, C, [("08", "CHEGOU PERTO, NÃO CHEGOU", "TANGENCIAR", AMBER), ("09", "A DEFINIÇÃO", "TANGENCIAMENTO", AMBER),
                       ("10", "QUANTO CUSTA?", "C2, C3 E C5 NO TETO", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09", "10"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        text(c, "TANGENCIAR", W / 2, 260, 60, "black", AMBER, aa)
        tangente(c, W / 2, 560, 170, ep(t, C["08.t"], 0.5), prog(t, C["08.b"], 1.6))
        text(c, "só encosta... e segue em frente", W / 2, 810, 32, "black", INK2, ep(t, C["08.b"] + 1.4, 0.4))
        return
    if sid == "09":
        aa = ep(t, C["09.t"], 0.5)
        definicao(c, 200, 200, 820, "TANGENCIAMENTO", AMBER,
                  "abordagem parcial, baseada somente no assunto mais amplo a que o tema está vinculado", aa, ep(t, C["09.a"], 0.5))
        ab = ep(t, C["09.b"], 0.5)
        boxed(c, 200, 560, 820, 200, BLUE, ab, 0.06)
        text(c, "ASSUNTO AMPLO", 240, 615, 22, "black", BLUE, ab, align="left", tracking=2)
        text(c, "a cidade inteira:", 240, 675, 36, "black", INK, ab, align="left")
        text(c, "o campo geral, sem o recorte", 240, 725, 32, "bold", INK2, ab, align="left")
        acc = ep(t, C["09.c"], 0.5)
        c.save(); c.translate(1080, 260); c.scale(0.4, 0.4); c.translate(-1080, -260)
        mapa(c, 1080, 260, 1.0, ep(t, C["09.t"], 0.5), (0, acc, 0), bairro=acc)
        c.restore()
        text(c, "bairro certo, sem rua e sem número", 1360, 520, 26, "black", AMBER, acc)
        return
    aa = ep(t, C["10.a"], 0.5)
    placar(c, 300, 300, 640, 1.0, cap=ep(t, C["10.a"], 1.4))
    ab = ep(t, C["10.b"], 0.5)
    pill(c, "C2, C3 e C5 batem no teto", 1450, 330, AMBER, size=30, a=ab, anchor="center", bounds=(0, 1920))
    text(c, "não passam de 40", 1450, 410, 40, "black", RED, ab)
    acc = ep(t, C["10.c"], 0.5)
    boxed(c, 1160, 500, 580, 200, GREEN, acc, 0.06)
    text(c, "C1 e C4", 1450, 565, 40, "black", GREEN, acc)
    para(c, "não são limitadas por essa regra: avaliadas normalmente", 1450, 620, 26, "bold", INK2, acc, 520, 32, align="center")


def b_fuga(c, t, C, B):
    frame(c, t, B["start"], "A CIDADE ERRADA", "FUGA AO TEMA", RED)
    aa = ep(t, C["11.a"], 0.5)
    definicao(c, 200, 200, 820, "FUGA AO TEMA", RED,
              "nem o tema específico nem o assunto mais geral são abordados", aa, ep(t, C["11.b"], 0.5))
    c.save(); c.translate(250, 540); c.scale(0.4, 0.4); c.translate(-250, -540)
    mapa(c, 250, 540, 1.0, aa, (0, 0, ep(t, C["11.a"] + 0.3, 0.5)))
    c.restore()
    ac = ep(t, C["11.c"], 0.5)
    placar(c, 1100, 300, 380, 1.0 if ac > 0 else 0, cap=0, zero=ep(t, C["11.c"], 1.0))
    selo(c, 1350, 230, ac, "NOTA ZERO", RED, -6, 40)
    ad = ep(t, C["11.d"], 0.5)
    pill(c, "não é avaliado em NENHUMA competência", 1100 + 200, 800, RED, size=24, a=ad, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco D — eu faço: três teses de 2025
# ======================================================================

def tese_card(c, n, s, a, y=430, size=34, col=INK):
    if a <= 0:
        return
    rrect(c, 220, y, 1480, 210, 20, "#FFFFFF", a, shadow=True)
    pill(c, f"TESE {n}", 260, y + 40, INK2, size=22, a=a, bounds=(0, 1920))
    para(c, s, 260, y + 110, size, "black", col, a, 1400, size * 1.3)


def b_eufaco(c, t, C, B):
    sid = which(t, C, ["12", "13", "14", "15", "16", "17"])
    head_seq(c, t, C, [("12", "EU FAÇO NA SUA FRENTE", "O TEMA DE 2025", GREEN), ("13", "TESE 1", "CONFERINDO OS BLOCOS", GREEN),
                       ("15", "TESE 2", "CONFERINDO OS BLOCOS", GREEN), ("16", "TESE 3", "CONFERINDO OS BLOCOS", GREEN)])
    card(c, *CARD_R)
    a0 = ep(t, C["12.a"], 0.5)
    if sid == "12":
        text(c, "ENEM 2025", W / 2, 260, 26, "black", GRAY, a0, tracking=2)
        text(c, "“" + TEMA25 + "”", W / 2, 340, 46, "black", BLUE, a0)
        show = [ep(t, C["12.b"] + 0.5 * i, 0.4) for i in range(3)]
        puzzle(c, t, C, T25, 500, ep(t, C["12.b"], 0.5), 34, show, obriga=False)
        text(c, "3 teses contra esses blocos", W / 2, 760, 36, "black", GREEN, ep(t, C["12.c"], 0.5))
        return
    puzzle(c, t, C, T25, 230, 1.0, 30, None, obriga=False)
    my = 360
    if sid in ("13", "14"):
        tese_card(c, 1, TESE1, ep(t, C["13.a"], 0.5), y=420)
        marcas(c, T25, my, [ep(t, C["13.c"], 0.4), ep(t, C["13.b"], 0.4), ep(t, C["13.d"], 0.4)], [False, True, False], 30)
        if sid == "14":
            veredito(c, W / 2, 690, "tg", ep(t, C["14.a"], 0.4), 30)
            ab = ep(t, C["14.b"], 0.5)
            boxed(c, 300, 730, 1320, 90, PURPLE, ab, 0.08, 16)
            text(c, "a Cartilha cita: envelhecimento só como processo biológico universal = TANGENCIAMENTO",
                 W / 2, 785, 26, "black", PURPLE, ab)
        return
    if sid == "15":
        tese_card(c, 2, TESE2, ep(t, C["15.a"], 0.5), y=420)
        ab = ep(t, C["15.b"], 0.4)
        marcas(c, T25, my, [ab, ab, ab], [False, False, False], 30)
        pill(c, "OUTRO ASSUNTO", W / 2, 700, RED, size=26, a=ep(t, C["15.c"], 0.4) * (1 - ep(t, C["15.d"], 0.3)), anchor="center")
        veredito(c, W / 2, 700, "fg", ep(t, C["15.d"], 0.4), 30)
        text(c, "um texto inteiro a partir dela fugiria ao tema", W / 2, 780, 28, "bold", INK2, ep(t, C["15.d"], 0.4))
        return
    # tese 3
    tese_card(c, 3, TESE3, ep(t, C["16.a"], 0.5), y=410, size=32)
    pill(c, "ETARISMO = preconceito contra as pessoas por causa da idade", W / 2, 690, BLUE, size=26,
         a=ep(t, C["16.b"], 0.4) * (1 - ep(t, C["17"], 0.3)), anchor="center")
    if sid == "17":
        marcas(c, T25, my, [ep(t, C["17.a"], 0.4), ep(t, C["17.b"], 0.4), ep(t, C["17.c"], 0.4)], [True, True, True], 30)
        ad = ep(t, C["17.d"], 0.4)
        text(c, "2 EIXOS:", 470, 705, 26, "black", GREEN, ad, align="left", tracking=2)
        pill(c, "etarismo", 640, 695, GREEN, size=26, a=ad, bounds=(0, 1920))
        pill(c, "adaptação das cidades e dos serviços", 820, 695, GREEN, size=26, a=ep(t, C["17.d"] + 0.8, 0.4), bounds=(0, 1920))
        veredito(c, W / 2, 790, "ok", ep(t, C["17.e"], 0.4), 30)
    text(c, "Teses elaboradas para fins didáticos (material de estudo).", 180, 860, 16, "medium", GRAY, 1.0, align="left")


# ======================================================================
# blocos E e F — silencioso e quando conferir
# ======================================================================

def b_silencio(c, t, C, B):
    head_seq(c, t, C, [("18", "POR QUE É PERIGOSO?", "TANGENCIAR É SILENCIOSO", AMBER), ("19", "BEM ESCRITO...", "NO ENDEREÇO ERRADO", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["18", "19"])
    if sid == "18":
        aa = ep(t, C["18.a"], 0.5)
        text(c, "SILENCIOSO", W / 2, 300, 72, "black", AMBER, aa)
        ab = ep(t, C["18.b"], 0.5)
        rrect(c, 280, 400, 620, 300, 22, mix("#FFFFFF", RED, 0.06), ab)
        text(c, "FUGA", 590, 470, 34, "black", RED, ab, tracking=2)
        text(c, "geralmente percebe", 590, 560, 40, "black", INK, ab)
        check_icon(c, 590, 640, 28, ab, RED, "check")
        rrect(c, 1020, 400, 620, 300, 22, mix("#FFFFFF", AMBER, 0.08), ab)
        text(c, "TANGENCIAMENTO", 1330, 470, 34, "black", AMBER, ab, tracking=2)
        text(c, "quase nunca", 1330, 560, 40, "black", INK, ab)
        check_icon(c, 1330, 640, 28, ab, AMBER, "x")
        return
    a0 = ep(t, C["19.a"], 0.4)
    caixa(c, 330, 420, 360, 260, a0, label=True, label_a=1.0)
    for k, (cue, s) in enumerate((("19.a", "boa norma"), ("19.b", "bons conectivos"), ("19.c", "repertório interessante"))):
        a = ep(t, C[cue], 0.4)
        check_icon(c, 860, 290 + k * 80, 24, a, GREEN)
        text(c, s, 900, 302 + k * 80, 38, "black", INK, a, align="left")
    ad = ep(t, C["19.d"], 0.5)
    boxed(c, 820, 540, 760, 120, AMBER, ad, 0.08)
    text(c, "sobre o ASSUNTO, não sobre o RECORTE", 1200, 612, 34, "black", AMBER, ad)
    ae = ep(t, C["19.e"], 0.5)
    text(c, "uma caixa linda... no endereço errado", W / 2, 790, 36, "black", RED, ae)


def b_conferir(c, t, C, B):
    frame(c, t, B["start"], "QUANDO CONFERIR?", "DUAS PARADAS NA ETIQUETA", GREEN)
    a0 = ep(t, C["20.t"], 0.5)
    xs = [380, 960, 1540]
    labs = ["TESE", "DESENVOLVIMENTO", "FIM DO RASCUNHO"]
    line(c, xs[0], 420, xs[2], 420, LIGHT, a0, 10)
    line(c, xs[0], 420, xs[2], 420, GREEN, a0, 10, progress=prog(t, C["20.a"], 3.5))
    for k, (x, lb) in enumerate(zip(xs, labs)):
        c.drawCircle(x, 420, 26, paint(INK2 if k == 1 else GREEN, a0))
        text(c, lb, x, 500, 32, "black", INK, a0)
    for cue, x, lbl in (("20.a", xs[0], "1ª conferência: antes de desenvolver"), ("20.b", xs[2], "2ª conferência")):
        a = ep(t, C[cue], 0.4)
        check_icon(c, x, 330, 36, a, GREEN)
        pill(c, lbl, x, 580, GREEN, size=24, a=a, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["20.c"], 0.5)
    rows = [("TEMA", TEMA25, ac, BLUE, None, 0)]
    c.save(); c.translate(W / 2, 650); c.scale(0.7, 0.7); c.translate(-W / 2, -650)
    etiqueta(c, W / 2 - 500, 650, 1000, ac, rows, "OLHE A ETIQUETA")
    c.restore()


# ======================================================================
# recap, exercício, erros
# ======================================================================

FRASES = [("Endereço exato: completa.", "Bairro certo, casa errada: tangencia.", "Outra cidade: fuga."),
          ("Tangenciar limita C2, C3 e C5 a 40; fugir zera.",),
          ("Confira o tema na tese, antes de desenvolver.",)]
COLS = [(GREEN, AMBER, RED), (INK,), (INK,)]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "35"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    y = 260
    for k, parts in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        badge_num(c, k + 1, 270, y + d - 14, a, 34, bg=PURPLE)
        for j, s in enumerate(parts):
            text(c, s, 340, y + d + j * 58, 44, "black", COLS[k][j], a, align="left")
        y += len(parts) * 58 + 70


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("22", "SUA VEZ", "PAUSE E CLASSIFIQUE", GREEN), ("23", "CONFERINDO", "TRÊS DESTINOS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["22.a"], 0.5)
    text(c, "ENEM 2019 · “" + TEMA19 + "”", W / 2, 215, 30, "black", BLUE, aa)
    puzzle(c, t, C, T19, 270, aa, 26, None, obriga=False)
    res = [("23.r1", "tg"), ("23.r2", "ok"), ("23.r3", "fg")]
    for k, s in enumerate(EX):
        a, d = rise(t, C[f"22.t{k + 1}"])
        y = 420 + k * 135 + d
        if a <= 0:
            continue
        badge_num(c, k + 1, 230, y + 6, a, 26, bg=INK2)
        para(c, s, 280, y, 28, "black", INK, a, 1060, 34)
        cue, sit = res[k]
        veredito(c, 1530, y + 8, sit, ep(t, C[cue], 0.4), 22)
    if C.get("22.p"):
        pause_timer(c, t, C["22.end"] - 1.9, 1530, 560)
    text(c, "Teses elaboradas para fins didáticos.", 180, 860, 16, "medium", GRAY, aa, align="left")


ERROS = [("24", "Achar que tangenciar ZERA a redação", "os dois são chamados de erro de tema", "quem zera é a FUGA; tangenciar limita 3 competências"),
         ("25", "Achar que o tangenciamento limita AS CINCO", "o texto inteiro errou o recorte", "o teto de 40 vale só para C2, C3 e C5"),
         ("26", "Chamar de fuga um texto fora do recorte de LUGAR", "falar de outro país parece fugir do Brasil", "está na cidade certa: é TANGENCIAMENTO")]


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
# questões 2 e 6
# ======================================================================

Q2 = ("Para o tema do Enem 2025, “Perspectivas acerca do envelhecimento na sociedade brasileira”, um participante dedicou "
      "todos os parágrafos a mostrar como o Japão se adaptou ao envelhecimento da população, sem relacionar essa experiência "
      "à realidade brasileira. Segundo a Cartilha do Participante, essa redação")
ALT2 = [("A", "fugiu ao tema e recebe nota zero, pois tratou de outro país.", "28.a", "30.xa", "confunde com fuga: trata do assunto", RED),
        ("B", "abordou o tema de forma completa, pois o envelhecimento é o núcleo da frase temática.", "28.b", "30.xb", "ignora o recorte de lugar", RED),
        ("C", "tangenciou o tema e fica limitada a 40 pontos nas cinco competências.", "28.c", "30.xc", "C1 e C4 não são limitadas", RED),
        ("D", "tangenciou o tema, pois tratou o envelhecimento só fora do contexto brasileiro; C2, C3 e C5 não passam de 40 pontos.", "28.d", None, "", GREEN),
        ("E", "será penalizada apenas na Competência 1, por não usar exemplos nacionais.", "28.e", "30.xe", "o tema é avaliado na C2", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2", "O BLOCO ESQUECIDO", BLUE)
    card(c, *CARD_R)
    sid = which(t, C, ["27", "28", "29", "30"])
    a = ep(t, C["27.a"], 0.5)
    expl = ep(t, C["29"], 0.5)
    para(c, Q2, 180, 240, 25, "bold", INK, a * (1 - expl), 560, 33)
    if expl > 0:
        segs = [("Perspectivas", "29.a", True), ("envelhecimento", "29.a", True), ("sociedade brasileira", "29.b", False)]
        for k, (s, cue, ok) in enumerate(segs):
            y = 270 + k * 100
            ak = ep(t, C[cue] + 0.3 * k, 0.4) * expl
            rrect(c, 190, y - 40, 470, 76, 14, mix("#FFFFFF", GREEN if ok else RED, 0.10), ak)
            text(c, s, 220, y + 10, 30, "black", INK, ak, align="left")
            check_icon(c, 620, y, 24, ak, GREEN if ok else RED, "check" if ok else "x")
        veredito(c, 425, 600, "tg", ep(t, C["29.b"] + 0.8, 0.4), 26)
        ac = ep(t, C["29.c"], 0.5)
        boxed(c, 180, 650, 500, 150, PURPLE, ac, 0.08, 16)
        para(c, "Cartilha 2026: envelhecimento só fora do contexto brasileiro = tangenciamento", 210, 700, 22, "black", PURPLE, ac, 450, 28)
    if t >= C["28"] - 0.2:
        alts_panel(c, t, C, ALT2, 790, 222, 950, 22, "30.ok", "D", 6)
        pause_timer(c, t, C["28.end"] - 1.9, 640, 700)
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


REDS = [("31.i", "I", "Discute apenas a história do cinema mundial e as escolas cinematográficas, sem tratar de acesso.", "só a história do cinema mundial", "33.r1", "tg"),
        ("31.ii", "II", "Discute a importância da leitura de livros na formação dos jovens, sem mencionar cinema.", "leitura de livros, sem cinema", "33.r2", "fg"),
        ("31.iii", "III", "Discute a concentração das salas de exibição nas capitais e o preço dos ingressos como barreiras de acesso no país.", "salas nas capitais + preço do ingresso", "33.r3", "ok")]
ALT6 = [("A", "tangenciamento, fuga ao tema e abordagem completa.", "32.a", None, "", GREEN),
        ("B", "fuga ao tema, tangenciamento e abordagem completa.", "32.b", "34.xb", "inverte I e II", RED),
        ("C", "abordagem completa, fuga ao tema e tangenciamento.", "32.c", "34.xc", "I ignora o acesso", RED),
        ("D", "tangenciamento, tangenciamento e abordagem completa.", "32.d", "34.xd", "II abandona até o assunto", RED),
        ("E", "fuga ao tema, fuga ao tema e tangenciamento.", "32.e", "34.xe", "I fala de cinema", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6", "TRÊS REDAÇÕES, TRÊS DESTINOS", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["31.a"], 0.5)
    alt_on = ep(t, C["32"], 0.6)
    text(c, "ENEM 2019 · “" + TEMA19 + "”", W / 2, 215, 30, "black", BLUE, a * (1 - alt_on))
    text(c, "ENEM 2019 · acesso ao cinema no Brasil", 460, 215, 24, "black", BLUE, a * alt_on)
    for k, (cue, n, full, short, rc, sit) in enumerate(REDS):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        if alt_on < 1:
            y = 300 + k * 150 + d
            badge_num(c, n, 250, y + 6, ak * (1 - alt_on), 28, bg=INK2)
            para(c, full, 310, y, 32, "black", INK, ak * (1 - alt_on), 1300, 40)
        if alt_on > 0:
            y = 300 + k * 150
            rrect(c, 180, y - 50, 560, 120, 16, "#F4F5F7", alt_on)
            badge_num(c, n, 220, y - 6, alt_on, 22, bg=INK2)
            para(c, short, 260, y, 24, "black", INK, alt_on, 460, 30)
            veredito(c, 460, y + 52, sit, ep(t, C[rc], 0.4), 20)
    if alt_on > 0:
        alts_panel(c, t, C, ALT6, 790, 262, 950, 26, "34.ok", "A", 8)
        pause_timer(c, t, C["32.end"] - 1.9, 1560, 760)
    pill(c, "Segundo a Cartilha: respectivamente...", W / 2, 790, PURPLE, size=24, a=ep(t, C["31.b"], 0.4) * (1 - alt_on), anchor="center")
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A LEITURA EM 6 PASSOS", PURPLE)
    aa = ep(t, C["36.a"], 0.5)
    text(c, "você tem todas as ferramentas", W / 2, 280, 50, "black", GREEN, aa)
    ab = ep(t, C["36.b"], 0.5)
    rrect(c, 260, 360, 520, 300, 18, "#FFFFFF", ab, shadow=True)
    text(c, "PROPOSTA REAL", 520, 410, 22, "black", GRAY, ab, tracking=2)
    for j in range(5):
        line(c, 300, 460 + j * 38, 740 - (j % 2) * 90, 460 + j * 38, LIGHT, ab, 9)
    for k in range(6):
        a = ep(t, C["36.b"] + 0.5 * k, 0.4)
        badge_num(c, k + 1, 900 + k * 120, 510, a, 40, bg=PURPLE)
        if k < 5:
            arrow(c, 900 + k * 120 + 44, 510, 900 + k * 120 + 76, 510, LIGHT, a, 4, 10)
    text(c, "do zero até a TESE, na sua frente", 1200, 650, 34, "black", PURPLE, ep(t, C["36.c"], 0.5))


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"], "Como você classificou as três teses do cinema?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, entregas=b_entregas, placar0=b_placar0, completa=b_completa,
              tangencia=b_tangencia, fuga=b_fuga, eufaco=b_eufaco, silencio=b_silencio, conferir=b_conferir, recap=b_recap,
              exercicio=b_exercicio, erros=b_erros, q2=b_q2, q6=b_q6, ponte=b_ponte, cta=b_cta)
