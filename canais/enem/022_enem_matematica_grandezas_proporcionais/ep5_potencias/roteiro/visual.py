"""Visual — Grandezas Proporcionais, Episódio 5: quando dobrar não dobra (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências, alternativas, erro_cards, atalho...).
Peças deste episódio: azulejos() (piso n × n), cubo_iso() (caixa de n³ cubinhos em perspectiva), lanterna_lado()
(a lanterna vista de lado com o feixe se abrindo até a parede) e parede() (a mesma luz repartida em n × n quadrados).
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
_s = importlib.util.spec_from_file_location("comum022", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_grandezas_ep5_potencias.mp4"
CARD_R = K.CARD_R
AZULEJO = "#7FB5E8"
AZULEJO_BORDA = "#3E7BFA"
CUBO = ("#F2A541", "#D98B2B", "#B8701C")      # topo, esquerda, direita
LUZ = "#FFD54A"


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# peças do episódio
# ======================================================================

def azulejos(c, x, y, n, u, a, prog_=1.0, hl=None, rotulo=True):
    """piso quadrado n × n azulejos de lado u px; (x, y) = canto superior esquerdo; prog_ anima a entrada dos azulejos"""
    if a <= 0:
        return
    tot = n * n
    for k in range(tot):
        i, j = k % n, k // n
        ak = a * clamp(prog_ * tot - k, 0, 1)
        if ak <= 0:
            continue
        col = AZULEJO if hl is None or hl(i, j) else mix("#FFFFFF", AZULEJO, 0.35)
        rrect(c, x + i * u + 4, y + j * u + 4, u - 8, u - 8, 10, col, ak)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + i * u + 4, y + j * u + 4, u - 8, u - 8), 10, 10),
                    paint(AZULEJO_BORDA, ak, stroke=3))
    if rotulo:
        text(c, f"{n} m", x + n * u / 2, y + n * u + 46, 30, "black", INK2, a)
        text_mid(c, f"{n} m", x - 50, y + n * u / 2, 30, "black", INK2, a)


def _iso(ox, oy, s, x, y, z):
    return ox + (x - y) * s * 0.866, oy + (x + y) * s * 0.5 - z * s


def cubo_iso(c, ox, oy, n, s, a, prog_=1.0):
    """caixa de n × n × n cubinhos em perspectiva isométrica; (ox, oy) = canto da frente embaixo do primeiro cubinho"""
    if a <= 0:
        return
    cells = [(i, j, k) for k in range(n) for j in range(n) for i in range(n)]
    cells.sort(key=lambda p: (p[2], p[0] + p[1]))
    tot = len(cells)
    for idx, (i, j, k) in enumerate(cells):
        ak = a * clamp(prog_ * tot - idx, 0, 1)
        if ak <= 0:
            continue
        P = lambda dx, dy, dz: _iso(ox, oy, s, i + dx, j + dy, k + dz)
        faces = [([P(0, 0, 1), P(1, 0, 1), P(1, 1, 1), P(0, 1, 1)], CUBO[0]),
                 ([P(0, 1, 0), P(1, 1, 0), P(1, 1, 1), P(0, 1, 1)], CUBO[1]),
                 ([P(1, 0, 0), P(1, 1, 0), P(1, 1, 1), P(1, 0, 1)], CUBO[2])]
        for pts, col in faces:
            p = skia.Path(); p.moveTo(*pts[0])
            for q in pts[1:]:
                p.lineTo(*q)
            p.close()
            c.drawPath(p, paint(col, ak))
            c.drawPath(p, paint("#FFFFFF", ak * 0.9, stroke=2.5))


def lampada(c, cx, cy, r, a, brilho=1.0):
    if a <= 0:
        return
    for k in range(12):
        ang = k * math.pi / 6
        c.drawLine(cx + (r + 14) * math.cos(ang), cy + (r + 14) * math.sin(ang), cx + (r + 40) * math.cos(ang),
                   cy + (r + 40) * math.sin(ang), paint(AMBER, a * brilho, stroke=6, cap_round=True))
    c.drawCircle(cx, cy, r, paint(LUZ, a))
    c.drawCircle(cx, cy, r, paint(AMBER, a, stroke=5))
    rrect(c, cx - r * 0.45, cy + r * 0.8, r * 0.9, r * 0.6, 6, GRAY, a)


def lanterna_lado(c, x0, cy, u, d, a, mostrar=(1, 2, 3)):
    """lanterna vista de lado em (x0, cy); paredes nas distâncias 1, 2, 3 (u px por metro); feixe aberto até a distância d"""
    if a <= 0:
        return
    rrect(c, x0 - 110, cy - 26, 90, 52, 12, INK, a)
    p = skia.Path(); p.moveTo(x0 - 24, cy - 26); p.lineTo(x0, cy - 40); p.lineTo(x0, cy + 40); p.lineTo(x0 - 24, cy + 26); p.close()
    c.drawPath(p, paint(INK2, a))
    if d > 0:
        half = 50 * d
        p = skia.Path(); p.moveTo(x0, cy - 34); p.lineTo(x0 + d * u, cy - half); p.lineTo(x0 + d * u, cy + half)
        p.lineTo(x0, cy + 34); p.close()
        c.drawPath(p, paint(LUZ, a * 0.45))
    for m in mostrar:
        xm = x0 + m * u
        on = abs(m - d) < 0.05
        line(c, xm, cy - 175, xm, cy + 175, INK if on else "#D8D8D2", a, 8 if on else 4)
        text(c, f"{m} m", xm, cy + 225, 28, "black", INK if on else GRAY, a)
    arrow(c, x0, cy + 195, x0 + d * u - 6, cy + 195, GRAY, a * clamp(d, 0, 1), 3, 12)


def parede(c, cx, cy, n, q, a, lux=None, prog_=1.0):
    """a parede vista de frente: o feixe cobre n × n quadrados de lado q px; cada um fica 1/n² tão claro"""
    if a <= 0:
        return
    tot = n * n
    x0, y0 = cx - n * q / 2, cy - n * q / 2
    c.drawRect(skia.Rect.MakeXYWH(cx - 1.5 * q - 12, cy - 1.5 * q - 12, 3 * q + 24, 3 * q + 24), paint("#F1F1EC", a))
    for k in range(tot):
        i, j = k % n, k // n
        ak = a * clamp(prog_ * tot - k, 0, 1)
        if ak <= 0:
            continue
        rrect(c, x0 + i * q + 3, y0 + j * q + 3, q - 6, q - 6, 8, LUZ, ak * (0.25 + 0.75 / (n * n)))
        c.drawRect(skia.Rect.MakeXYWH(x0 + i * q + 3, y0 + j * q + 3, q - 6, q - 6), paint(AMBER, ak, stroke=2))
        if lux:
            text_mid(c, lux, x0 + i * q + q / 2, y0 + j * q + q / 2, 30 if n < 3 else 26, "black", INK, ak)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "QUANDO DOBRAR NÃO DOBRA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    lampada(c, 330, 420, 60, aa)
    if aa > 0:
        for k, (d, rot) in enumerate([(1, "d"), (2, "2d")]):
            xx = 330 + 280 * d
            a = aa * ep(t, C["01.a"] + 0.4 * k, 0.4)
            c.drawCircle(xx, 400, 26, paint(INK, a)); line(c, xx, 426, xx, 520, INK, a, 10)
            text(c, rot, xx, 600, 34, "black", INK2, a)
        arrow(c, 420, 660, 880, 660, GRAY, aa, 3, 12)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        text(c, "a luz cai pela metade?", 1310, 300, 40, "black", INK, ab)
        rrect(c, 1040, 350, 540, 70, 14, "#EEEEE8", ab)
        rrect(c, 1040, 350, 270, 70, 14, mix(RED, "#FFFFFF", 0.4), ab)
        text_mid(c, "1/2 ?", 1175, 385, 34, "black", "#FFFFFF", ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        check_icon(c, 1610, 385, 30, acc, RED, "x")
        rrect(c, 1040, 470, 540, 70, 14, "#EEEEE8", acc)
        rrect(c, 1040, 470, 135, 70, 14, GREEN, acc)
        text(c, "1/4", 1240, 520, 44, "black", GREEN, acc, align="left")
        text(c, "UM QUARTO", 1310, 620, 52, "black", GREEN, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        for k, s in enumerate(["LUZ", "SOM", "GRAVIDADE"]):
            chip(c, s, 1110 + k * 200 + (k == 2) * 30, 730, PURPLE, ad * ep(t, C["01.d"] + 0.25 * k, 0.4), 30)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "saber o que acontece quando algo DOBRA", "e não chutar \"dobra também\""),
            ("02.b", "…ou TRIPLICA", "× 3, × 9, × 27, ÷ 9…"),
            ("02.c", "em QUALQUER tipo de relação", "direta, quadrática, cúbica, inversa, inverso do quadrado")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "POTÊNCIA", 560, 250, GRAY, size=22, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "o número vezes ele mesmo", 560, 330, 34, "black", PURPLE, aa)
        for k, s in enumerate(["2^2 = 2·2 = 4", "3^2 = 3·3 = 9", "2^3 = 2·2·2 = 8"]):
            expr(c, s, 560, 440 + k * 110, 58, aa * ep(t, C["03.a"] + 0.8 * (k + 1), 0.4), cores={4: GREEN})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        pill(c, "EPISÓDIO 1", 1360, 250, GRAY, size=22, a=ab, anchor="center", bounds=(0, 1920))
        text(c, "o k: o número que não muda", 1360, 330, 34, "black", PURPLE, ab)
        text(c, "DIRETA", 1360, 430, 28, "black", GREEN, ab)
        expr(c, "y = k·x", 1360, 500, 60, ab, cores=mono("y = k·x", INK))
        text(c, "INVERSA", 1360, 610, 28, "black", BLUE, ab)
        expr(c, "y = k/x", 1360, 690, 60, ab, cores=mono("y = k/x", INK))
    line(c, 960, 230, 960, 800, "#E6E6E2", aa, 3)


def b_concreto(c, t, C, B):
    frame(c, t, B["start"], "TRÊS PERGUNTAS", "DA VIDA REAL", BLUE)
    itens = [("04.a", "PISO", "o dobro do lado →", "o dobro de azulejos?"),
             ("04.b", "CAIXA", "o dobro da aresta →", "o dobro de espaço?"),
             ("04.c", "LANTERNA", "o dobro da distância →", "metade da luz?")]
    for k, (cue, tit, l1, l2) in enumerate(itens):
        a, d = rise(t, C[cue])
        x = 200 + k * 520
        if a <= 0:
            continue
        rrect(c, x, 230 + d, 480, 520, 24, "#FFFFFF", a, shadow=True)
        text(c, tit, x + 240, 290 + d, 34, "black", BLUE, a)
        cx, cy = x + 240, 450 + d
        if k == 0:
            azulejos(c, cx - 90, cy - 90, 2, 90, a, rotulo=False)
        elif k == 1:
            cubo_iso(c, cx, cy, 2, 62, a)
        else:
            rrect(c, cx - 150, cy - 18, 70, 36, 8, INK, a)
            p = skia.Path(); p.moveTo(cx - 80, cy - 26); p.lineTo(cx + 150, cy - 110); p.lineTo(cx + 150, cy + 110)
            p.lineTo(cx - 80, cy + 26); p.close()
            c.drawPath(p, paint(LUZ, a * 0.5))
        text(c, l1, x + 240, 640 + d, 28, "bold", INK2, a)
        text(c, l2, x + 240, 690 + d, 32, "black", INK, a)
        ad = ep(t, C["04.d"] + 0.25 * k, 0.4)
        selo(c, x + 370, 560 + d, ad, "NÃO!", RED, -10, 34)


# ======================================================================
# A) direta — revisão
# ======================================================================

def b_direta(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RÁPIDA", "DIRETA", GREEN)
    aa = ep(t, C["05.a"], 0.5)
    expr(c, "y = k·x", 560, 330, 96, aa, cores=mono("y = k·x", PURPLE))
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        for k, (kg, rs) in enumerate([("1 kg", "R$ 5"), ("2 kg", "R$ 10")]):
            a = ab * ep(t, C["05.b"] + 0.6 * k, 0.4)
            y = 470 + k * 120
            rrect(c, 300, y, 520, 92, 14, "#FFFFFF", a, shadow=True)
            text(c, kg, 430, y + 60, 42, "black", INK, a)
            text(c, rs, 690, y + 60, 42, "black", GREEN, a)
        chip(c, "× 2", 250, 580, PURPLE, ab, 32)
        chip(c, "× 2", 870, 580, GREEN, ab, 32)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        boxed(c, 1080, 300, 560, 220, BLUE, acc, 0.08)
        text(c, "LINEAR", 1360, 380, 48, "black", BLUE, acc)
        text(c, "as duas crescem no mesmo ritmo", 1360, 450, 30, "bold", INK2, acc)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        text(c, "dobrou  →  DOBROU", 1360, 650, 52, "black", GREEN, ad)


# ======================================================================
# B) quadrática — os azulejos
# ======================================================================

def b_azulejos(c, t, C, B):
    sid = which(t, C, ["06", "07", "08"])
    head_seq(c, t, C, [("06", "O PISO", "O LADO DOBROU…", BLUE), ("07", "ÁREA = LADO × LADO", "QUADRÁTICA", PURPLE),
                       ("08", "TAMBÉM NA FÍSICA", "E O ATALHO", GREEN)])
    card(c, *CARD_R)
    U = 120
    if sid == "06":
        a1 = ep(t, C["06.a"], 0.5)
        n = 2 if t >= C["06.b"] else 1
        pr = ep(t, C["06.b"], 1.2) if n == 2 else 1.0
        azulejos(c, 330, 320 if n == 2 else 380, n, U, a1, pr)
        if n == 1:
            text(c, "1 azulejo", 390, 560, 34, "black", INK, a1)
        ac = ep(t, C["06.c"], 0.5)
        if ac > 0:
            arrow(c, 330, 290, 330 + 2 * U, 290, GREEN, ac, 4, 14)
            text(c, "2 de largura", 330 + U, 270, 30, "black", GREEN, ac)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            arrow(c, 330 + 2 * U + 30, 320, 330 + 2 * U + 30, 320 + 2 * U, PURPLE, ad, 4, 14)
            text(c, "2 de comprimento", 330 + 2 * U + 55, 330 + U, 30, "black", PURPLE, ad, align="left")
        ae = ep(t, C["06.e"], 0.5)
        if ae > 0:
            expr(c, "2 × 2 = 4", 1260, 380, 80, ae, cores={4: GREEN})
            text(c, "lado × 2  →  área × 4", 1260, 540, 46, "black", GREEN, ae)
            text(c, "QUADRUPLICOU", 1260, 640, 56, "black", GREEN, ae)
    elif sid == "07":
        a0 = ep(t, C["07"], 0.4)
        expr(c, "A = L^2", 1260, 320, 90, a0, cores=mono("A = L^2", PURPLE))
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            boxed(c, 1000, 400, 520, 190, PURPLE, ab, 0.08)
            text(c, "QUADRÁTICA", 1260, 460, 36, "black", PURPLE, ab)
            expr(c, "y = k·x^2", 1260, 535, 60, ab, cores=mono("y = k·x^2", INK))
        n = 3 if t >= C["07.c"] else 2
        pr = ep(t, C["07.c"], 1.4) if n == 3 else 1.0
        azulejos(c, 330, 260 if n == 3 else 320, n, U, a0, pr)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            expr(c, "3 × 3 = 9", 1260, 700, 64, ad, cores={4: GREEN})
            text(c, "lado × 3  →  área × 9", 1260, 790, 34, "black", GREEN, ad)
    else:
        aa = ep(t, C["08.a"], 0.5)
        if aa > 0:
            rrect(c, 220, 260, 700, 420, 24, "#FFFFFF", aa, shadow=True)
            text(c, "ENERGIA CINÉTICA", 570, 330, 36, "black", BLUE, aa)
            text(c, "= a energia do movimento", 570, 380, 30, "bold", INK2, aa)
            expr(c, "E = m·v^2/2", 570, 480, 64, aa, cores=mono("E = m·v^2/2", INK))
            text(c, "a velocidade vai AO QUADRADO", 570, 600, 30, "black", PURPLE, aa)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            ftext(c, "velocidade × 2  →  energia × 4", 570, 740, 38, "black", RED, ab)
        K.atalho(c, 1040, 280, 640, 440, "ATALHO", ["eleve o FATOR ao quadrado:", "dobrou  →  × 4", "triplicou  →  × 9",
                                                    "× 10  →  × 100"], ep(t, C["08.c"], 0.5), 38)


# ======================================================================
# C) cúbica — os cubinhos
# ======================================================================

def b_cubinhos(c, t, C, B):
    sid = which(t, C, ["09", "10"])
    head_seq(c, t, C, [("09", "A CAIXA", "A ARESTA DOBROU…", BLUE), ("10", "VOLUME = ARESTA × ARESTA × ARESTA", "CÚBICA", PURPLE)])
    card(c, *CARD_R)
    if sid == "09":
        a1 = ep(t, C["09.a"], 0.5)
        n = 2 if t >= C["09.b"] else 1
        pr = ep(t, C["09.b"], 1.6) if n == 2 else 1.0
        cubo_iso(c, 560, 520, n, 110 if n == 2 else 150, a1, pr)
        if n == 1:
            text(c, "1 cubinho", 560, 760, 34, "black", INK, a1)
        labs = [("09.c", "2 de largura", GREEN), ("09.c", "2 de comprimento", BLUE), ("09.d", "2 de altura", PURPLE)]
        for k, (cue, s, col) in enumerate(labs):
            a = ep(t, C[cue] + (0.5 if k == 1 else 0), 0.5)
            text(c, s, 1050, 340 + k * 70, 36, "black", col, a, align="left")
        ae = ep(t, C["09.e"], 0.5)
        if ae > 0:
            expr(c, "2 × 2 × 2 = 8", 1300, 610, 66, ae, cores={6: GREEN})
            text(c, "aresta × 2  →  volume × 8", 1300, 730, 40, "black", GREEN, ae)
    else:
        a0 = ep(t, C["10"], 0.4)
        n = 3 if t >= C["10.b"] else 2
        pr = ep(t, C["10.b"], 2.0) if n == 3 else 1.0
        cubo_iso(c, 540, 510, n, 90 if n == 3 else 120, a0, pr)
        expr(c, "V = a^3", 1300, 300, 80, a0, cores=mono("V = a^3", PURPLE))
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            boxed(c, 1050, 370, 500, 170, PURPLE, aa, 0.08)
            text(c, "CÚBICA", 1300, 425, 34, "black", PURPLE, aa)
            expr(c, "y = k·x^3", 1300, 495, 56, aa, cores=mono("y = k·x^3", INK))
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            expr(c, "3^3 = 27", 1300, 600, 56, ab, cores={2: GREEN})
        K.atalho(c, 1030, 650, 540, 170, "ATALHO", ["no cubo, eleve o fator ao cubo:", "× 2 → × 8   ·   × 3 → × 27"],
                 ep(t, C["10.c"], 0.5), 30)


# ======================================================================
# D) inversa — revisão
# ======================================================================

def b_inversa(c, t, C, B):
    frame(c, t, B["start"], "AS QUE DESCEM", "INVERSA", BLUE)
    aa = ep(t, C["11.a"], 0.5)
    expr(c, "y = k/x", 560, 380, 100, aa, cores=mono("y = k/x", PURPLE))
    text(c, "o x fica EMBAIXO", 560, 520, 34, "black", INK2, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        text(c, "VIAGEM DE 240 km", 1360, 290, 30, "black", INK2, ab)
        for k, (v, h, w) in enumerate([("60 km/h", "4 h", 480), ("120 km/h", "2 h", 240)]):
            a = ab * ep(t, C["11.b"] + 0.8 * k, 0.4)
            y = 360 + k * 170
            text(c, v, 1080, y + 50, 36, "black", INK, a, align="left")
            rrect(c, 1080, y + 70, w, 60, 14, mix(BLUE, "#FFFFFF", 0.2), a)
            text_mid(c, h, 1080 + w / 2, y + 100, 32, "black", "#FFFFFF", a)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        text(c, "dobrou  →  METADE", 1360, 760, 46, "black", BLUE, acc)


# ======================================================================
# E) inverso do quadrado — a lanterna
# ======================================================================

def b_lanterna(c, t, C, B):
    sid = which(t, C, ["12", "13", "14", "15"])
    head_seq(c, t, C, [("12", "A LANTERNA", "A 1 METRO", BLUE), ("13", "A MESMA LUZ", "A 2 METROS", BLUE),
                       ("14", "A MESMA LUZ", "A 3 METROS", PURPLE), ("15", "NÃO É SÓ A LUZ", "E O ATALHO", GREEN)])
    card(c, *CARD_R)
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        itens = [("15", "LUZ", "lanterna, lâmpada"), ("15.a", "SOM", "a caixa de som do show"),
                 ("15.b", "GRAVIDADE", "a força que puxa os planetas")]
        for k, (cue, s, sub) in enumerate(itens):
            a, d = rise(t, C[cue])
            y = 290 + k * 150 + d
            rrect(c, 230, y - 60, 700, 120, 18, "#FFFFFF", a, shadow=True)
            text(c, s, 290, y - 4, 40, "black", PURPLE, a, align="left")
            text(c, sub, 290, y + 40, 26, "bold", INK2, a, align="left")
        expr(c, "y = k/x^2", 580, 760, 56, aa, cores=mono("y = k/x^2", PURPLE))
        K.atalho(c, 1050, 300, 600, 380, "ATALHO", ["distância × 2  →  efeito ÷ 4", "distância × 3  →  efeito ÷ 9",
                                                    "(o fator ao quadrado, embaixo)"], ep(t, C["15.c"], 0.5), 34)
        return
    a0 = ep(t, C["12"], 0.4)
    if sid == "12":
        d = ep(t, C["12.a"], 1.0)
        n, lux, pr = 1, "36 lux" if t >= C["12.d"] else None, 1.0
    elif sid == "13":
        d = 1 + ep(t, C["13"], 1.2)
        n = 2 if t >= C["13.b"] else 1
        pr = ep(t, C["13.b"], 1.0) if n == 2 else 1.0
        lux = "9 lux" if t >= C["13.d"] else ("36 lux" if n == 1 else None)
    else:
        d = 2 + ep(t, C["14"], 1.2)
        n = 3 if t >= C["14.a"] else 2
        pr = ep(t, C["14.a"], 1.2) if n == 3 else 1.0
        lux = "4 lux" if t >= C["14.b"] else ("9 lux" if n == 2 else None)
    lanterna_lado(c, 320, 470, 190, d, a0)
    parede(c, 1330, 450, n, 100, a0, lux, pr)
    text(c, "a parede vista de frente", 1330, 260, 26, "black", GRAY, a0)
    if sid == "12":
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            boxed(c, 1000, 640, 660, 120, BLUE, ab, 0.08)
            text(c, "INTENSIDADE = luz em cada pedacinho", 1330, 692, 30, "black", BLUE, ab)
            text(c, "medida em LUX", 1330, 738, 28, "black", INK2, ep(t, C["12.c"], 0.5))
    elif sid == "13":
        ab = ep(t, C["13.b"], 0.5)
        text(c, "2 × 2 = 4 quadrados", 1330, 650, 36, "black", INK, ab)
        ac = ep(t, C["13.c"], 0.5)
        text(c, "a mesma luz, repartida em 4", 1330, 705, 30, "bold", INK2, ac)
        ad = ep(t, C["13.d"], 0.5)
        ftext(c, "36 ÷ 4 = 9 lux  →  1/4", 1330, 775, 38, "black", GREEN, ad)
    else:
        aa = ep(t, C["14.a"], 0.5)
        text(c, "3 × 3 = 9 quadrados", 1330, 650, 36, "black", INK, aa)
        ab = ep(t, C["14.b"], 0.5)
        ftext(c, "36 ÷ 9 = 4 lux  →  1/9", 1330, 715, 38, "black", GREEN, ab)
        ad = ep(t, C["14.d"], 0.5)
        if ad > 0:
            rrect(c, 380, 720, 620, 100, 18, "#FFFFFF", ad, shadow=True)
            expr(c, "y = k/x^2", 560, 770, 52, ad, cores=mono("y = k/x^2", PURPLE))
            text(c, "INVERSO DO QUADRADO", 830, 780, 22, "black", PURPLE, ad)


# ======================================================================
# F) a regra geral
# ======================================================================

TABELA = [("16.a", "Direta", "y = k·x", "dobra", "× 2", GREEN),
          ("16.b", "Quadrática", "y = k·x^2", "quadruplica", "× 4", GREEN),
          ("16.c", "Cúbica", "y = k·x^3", "fica 8 vezes maior", "× 8", GREEN),
          ("16.d", "Inversa", "y = k/x", "cai à metade", "÷ 2", BLUE),
          ("16.e", "Inverso do quadrado", "y = k/x^2", "cai a um quarto", "÷ 4", BLUE)]


def b_regra(c, t, C, B):
    frame(c, t, B["start"], "A TABELA COMPLETA", "SE x DOBRA, y…", PURPLE)
    a0 = ep(t, C["16"], 0.4)
    for k, s in enumerate(["RELAÇÃO", "FÓRMULA", "SE x DOBRA, y…"]):
        text(c, s, [360, 800, 1260][k], 230, 24, "black", GRAY, a0)
    for j, (cue, nome, f, efeito, fat, col) in enumerate(TABELA):
        a = ep(t, C[cue], 0.4)
        if a <= 0:
            continue
        y = 260 + j * 88
        rrect(c, 200, y, 1520, 76, 12, "#FFFFFF", a, shadow=True)
        text(c, nome, 380, y + 50, 28, "black", INK, a)
        expr(c, f, 800, y + 38, 40, a, cores=mono(f, PURPLE))
        text(c, efeito, 1260, y + 50, 32, "black", col, a)
        chip(c, fat, 1620, y + 38, col, a, 30)
    af = ep(t, C["16.f"], 0.5)
    if af > 0:
        boxed(c, 260, 712, 1400, 104, GREEN, af, 0.08)
        text(c, "o EXPOENTE diz quantas vezes o fator se multiplica", W / 2, 756, 34, "black", GREEN, af)
        text(c, "em cima: multiplica   ·   embaixo: divide", W / 2, 800, 28, "black", INK2, af)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E PENSE", GREEN), ("18", "VAMOS CONFERIR", "PAUSE E PENSE", GREEN)])
    card(c, *CARD_R)
    q = [("17.a", "LÂMPADA", "a distância TRIPLICA. E a luz?", "18.a", "3² = 9, embaixo  →  luz ÷ 9  (1/9)"),
         ("17.b", "CUBO", "o lado TRIPLICA. E o volume?", "18.b", "3³ = 27  →  volume × 27")]
    for j, (cue, tit, s, rc, r) in enumerate(q):
        a = ep(t, C[cue], 0.5)
        x = 200 + j * 780
        if a <= 0:
            continue
        rrect(c, x, 240, 740, 300, 24, "#FFFFFF", a, shadow=True)
        text(c, tit, x + 370, 300, 30, "black", BLUE, a)
        if j == 0:
            lampada(c, x + 370, 400, 40, a)
        else:
            cubo_iso(c, x + 370, 410, 1, 55, a)
        text(c, s, x + 370, 520, 32, "black", INK, a)
        if t >= C["18"]:
            ra = ep(t, C[rc], 0.5)
            ftext(c, r, x + 370, 620, 36, "black", GREEN, ra)
    if t >= C["18"]:
        acc = ep(t, C["18.c"], 0.5)
        if acc > 0:
            ftext(c, "confira: lado 1 → volume 1 · lado 3 → volume 27 ✓", W / 2, 740, 34, "black", AMBER, acc)
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 680)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Quadrado: dobrou, quadruplicou.", "Cubo: dobrou, oito vezes.",
          "Inverso do quadrado: dobrou a distância, um quarto do efeito."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 290 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 58)


ERROS = [("Dobrar o lado dobra a área", "o lado dobrou, e a gente pensa que tudo dobra junto",
          "a área cresce nas DUAS direções: 2 de largura × 2 de comprimento = × 4"),
         ("Dobrar a distância reduz a luz à metade", "\"mais longe, menos luz\" soa como inversa simples",
          "a luz se espalha em largura E em altura: cobre 4 quadrados → 1/4"),
         ("Ao triplicar, trocar o × 9 da área pelo × 27 do volume", "9 e 27 são as duas potências de 3",
          "área é ao quadrado: × 9 · volume é ao cubo: × 27 · é piso ou é caixa?")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


# ======================================================================
# Questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=32, w=680):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS8 = [("A", "3", "tratou como direta", RED), ("B", "6", "fez 3 × 2, não 3²", RED), ("C", "9", "", GREEN),
         ("D", "12", "não sai de conta certa", RED), ("E", "27", "é o fator do VOLUME", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EU FAÇO", "PROPORCIONALIDADE QUADRÁTICA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    _enunciado(c, [("Uma praça tem formato quadrado. Em um projeto de ampliação, a medida do lado será triplicada.", INK),
                   ("A área da praça ampliada, em relação à área atual, ficará multiplicada por", BLUE)], a0, 240, 30, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABDE"}
    if t >= C["23.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS8, 1000, 230, 680, 40, C["24.ok"], "C", cues_in, cues_x, gap=22)
    if t >= C["24"]:
        ra = ep(t, C["24"], 0.4)
        rrect(c, 170, 470, 740, 340, 18, "#FFFFFF", ra, shadow=True)
        text(c, "ÁREA = LADO²  →  QUADRÁTICA", 540, 525, 28, "black", PURPLE, ep(t, C["24.a"], 0.4))
        expr(c, "3^2 = 9", 540, 600, 56, ep(t, C["24.b"], 0.4), cores={2: GREEN})
        ac = ep(t, C["24.c"], 0.4)
        if ac > 0:
            azulejos(c, 230, 660, 2, 30, ac, rotulo=False)
            text(c, "lado 2 → área 4", 420, 700, 26, "black", INK, ac, align="left")
        ad = ep(t, C["24.d"], 0.4)
        if ad > 0:
            text(c, "lado 6 → área 36", 420, 745, 26, "black", INK, ad, align="left")
            ftext(c, "36 ÷ 4 = 9 ✓", 740, 790, 30, "black", AMBER, ad)


ALTS6 = [("A", "10 lux", "não sai de conta coerente", RED), ("B", "16 lux", "", GREEN),
         ("C", "20 lux", "fez 100 ÷ 5", RED), ("D", "40 lux", "inversa simples, sem o ²", RED),
         ("E", "250 lux", "a luz AUMENTOU? absurdo", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · VOCÊ FAZ", "INVERSO DO QUADRADO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    _enunciado(c, [("A iluminação produzida por uma lâmpada sobre uma superfície é inversamente proporcional ao quadrado da "
                    "distância entre elas. A 2 metros da lâmpada, a iluminação medida é de 100 lux.", INK),
                   ("A 5 metros, a iluminação será de", BLUE)], a0, 240, 30, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ACDE"}
    if t >= C["26.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS6, 1000, 230, 680, 40, C["27.ok"], "B", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["26.end"] - 2.4, 470, 690)
    if t >= C["27"]:
        ra = ep(t, C["27"], 0.4)
        rrect(c, 170, 490, 740, 320, 18, "#FFFFFF", ra, shadow=True)
        expr(c, "I = k/d^2", 540, 545, 44, ep(t, C["27.a"], 0.4), cores=mono("I = k/d^2", PURPLE))
        expr(c, "100 = k/4", 540, 625, 40, ep(t, C["27.b"], 0.4), cores=mono("100 = k/4", INK))
        ftext(c, "k = 400", 800, 630, 30, "black", PURPLE, ep(t, C["27.b"] + 1.2, 0.4))
        ftext(c, "400 ÷ 25 = 16 lux", 540, 705, 40, "black", GREEN, ep(t, C["27.c"], 0.4))
        ftext(c, "distância × 2,5 → luz ÷ 6,25 ✓", 540, 775, 28, "black", AMBER, ep(t, C["27.d"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    itens = [("30.a", "JUNTAMOS TUDO", "k · tabela · gráfico · fórmulas · potências", BLUE),
             ("30.b", "CAÇAMOS AS PEGADINHAS", "verdadeiro ou falso?", AMBER),
             ("30.c", "QUESTÕES NOVAS", "5 inéditas, estilo ENEM", GREEN)]
    for k, (cue, s, sub, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        y = 300 + k * 150 + d
        badge_num(c, k + 1, 420, y - 16, a, 34, bg=col)
        text(c, s, 480, y, 46, "black", col, a, align="left")
        text(c, sub, 480, y + 48, 28, "bold", INK2, a, align="left")
    pill(c, "ep. 6 · revisão e treino", W / 2, 790, PURPLE, size=32, a=ep(t, C["30.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"], "Você achava que a luz caía pela metade?",
        canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, direta=b_direta,
              azulejos=b_azulejos, cubinhos=b_cubinhos, inversa=b_inversa, lanterna=b_lanterna, regra=b_regra,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q8=b_q8, q6=b_q6, ponte=b_ponte, cta=b_cta)
