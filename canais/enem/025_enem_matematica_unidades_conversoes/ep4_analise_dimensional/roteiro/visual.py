"""Visual — Unidades e conversões, Episódio 4: análise dimensional e as unidades de fora do sistema métrico (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, pause_timer...).
Peças deste episódio: cadeia() (cadeia de frações de conversão com as unidades riscadas uma a uma; as que não cancelam
acendem em vermelho), notas() (a troca de uma nota de 100 por dez de 10), tv() (diagonal em polegadas e cm), chuveiro(),
relogio_luz() (o medidor de energia com o disco girando), regua_pol() (polegada × centímetro), linha() (texto com cor por
trecho, mantém espaços de milhar).
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
_s = importlib.util.spec_from_file_location("comum025", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_unidades_ep4_analise_dimensional.mp4"
CARD_R = K.CARD_R
AGUA = "#4FA3E0"
NOTA = "#7FB77E"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)]"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def _parte_w(n, u, size):
    s = (n + " " if n else "") + u
    return text_w(s, "black", size) if s else 0


def cadeia_w(termos, size, gap=70):
    ws = [max(_parte_w(n, u, size), _parte_w(dn, du, size)) + 34 for n, u, dn, du in termos]
    return sum(ws) + gap * (len(termos) - 1), ws


def cadeia(c, cx, cy, termos, size=60, alfas=None, riscos=None, cores=None, gap=70, a=1.0):
    """cadeia de frações de conversão centrada em cx.
    termos = [(num_cima, unid_cima, num_baixo, unid_baixo)]; termo sem andar de baixo: num_baixo = unid_baixo = "".
    alfas[i] = opacidade do termo i · riscos[(i, "t"|"b")] = progresso do risco na unidade · cores[(i, "t"|"b")] = cor da
    unidade (padrão azul). Devolve a largura total."""
    alfas = alfas or [1.0] * len(termos)
    riscos = riscos or {}
    cores = cores or {}
    total, ws = cadeia_w(termos, size, gap)
    x = cx - total / 2
    for i, ((n, u, dn, du), w_) in enumerate(zip(termos, ws)):
        ai = alfas[i] * a
        if ai > 0:
            mx = x + w_ / 2
            tem_baixo = bool(dn or du)
            yt = cy - size * 0.28 if tem_baixo else cy + size * 0.36
            yb = cy + size * 0.98

            def andar(nn, uu, yy, key):
                if not (nn or uu):
                    return
                sn = (nn + " ") if nn else ""
                wn, wu = text_w(sn, "black", size), text_w(uu, "black", size)
                x0 = mx - (wn + wu) / 2
                if sn:
                    text(c, sn, x0, yy, size, "black", INK, ai, align="left")
                col = cores.get((i, key), BLUE)
                text(c, uu, x0 + wn, yy, size, "black", col, ai, align="left")
                pr = riscos.get((i, key), 0)
                if pr > 0:
                    ym = yy - size * 0.34
                    strike(c, x0 + wn - 6, ym + size * 0.32, x0 + wn + wu + 6, ym - size * 0.32, ai, RED, pr)

            andar(n, u, yt, "t")
            if tem_baixo:
                line(c, x, cy, x + w_, cy, INK, ai, max(3, size * 0.07))
                andar(dn, du, yb, "b")
        if i < len(termos) - 1:
            an = alfas[i + 1] * a
            if an > 0:
                text_mid(c, "×", x + w_ + gap / 2, cy, size * 0.8, "black", GRAY, an)
        x += w_ + gap
    return total


def notas(c, cx, cy, a, troca=0.0):
    """uma nota de 100 que vira dez notas de 10 (troca 0 → 1)"""
    if a <= 0:
        return
    a1 = a * (1 - troca)
    if a1 > 0:
        rrect(c, cx - 150, cy - 70, 300, 140, 14, NOTA, a1, shadow=True)
        rrect(c, cx - 130, cy - 50, 260, 100, 10, "#FFFFFF", a1 * 0.25)
        fmid(c, "R$ 100", cx, cy, 52, "black", "#1E5631", a1)
    if troca > 0:
        for k in range(10):
            col_, row = k % 5, k // 5
            x = cx - 270 + col_ * 110
            y = cy - 70 + row * 80
            ak = a * ep(troca, k * 0.06, 0.3)
            rrect(c, x, y, 100, 64, 8, "#B9D7A8", ak, shadow=True)
            fmid(c, "10", x + 50, y + 32, 30, "black", "#1E5631", ak)


def tv(c, cx, cy, w, h, a, rotulo=None, col=None):
    """TV com a diagonal marcada"""
    if a <= 0:
        return
    col = col or PURPLE
    rrect(c, cx - w / 2 - 14, cy - h / 2 - 14, w + 28, h + 28, 18, "#1F2430", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 8, "#3B4252", a)
    rrect(c, cx - 50, cy + h / 2 + 14, 100, 26, 6, "#1F2430", a)
    arrow(c, cx - w / 2 + 16, cy + h / 2 - 16, cx + w / 2 - 16, cy - h / 2 + 16, col, a, 6, 18)
    if rotulo:
        rrect(c, cx - 110, cy - 30, 220, 60, 14, "#FFFFFF", a * 0.92)
        fmid(c, rotulo, cx, cy, 34, "black", col, a)


def chuveiro(c, cx, cy, a, agua=1.0):
    """chuveiro com gotas"""
    if a <= 0:
        return
    rrect(c, cx - 12, cy - 160, 24, 110, 8, "#9AA3AE", a)
    rrect(c, cx - 110, cy - 60, 220, 40, 16, "#7D8792", a)
    if agua > 0:
        for k in range(9):
            x = cx - 90 + k * 22
            for j in range(3):
                y = cy - 5 + j * 45 + (k % 3) * 12
                c.drawCircle(x, y, 6, paint(AGUA, a * agua * 0.8))


def relogio_luz(c, cx, cy, a, giro=0.0, leitura="0"):
    """medidor de energia: caixa com visor e disco girando"""
    if a <= 0:
        return
    rrect(c, cx - 150, cy - 170, 300, 340, 26, "#E9ECEF", a, shadow=True)
    rrect(c, cx - 115, cy - 140, 230, 70, 10, "#1F2430", a)
    fmid(c, leitura, cx, cy - 105, 42, "black", AMBER, a)
    text(c, "kWh", cx, cy - 40, 26, "black", INK2, a)
    rx, ry = 100, 26
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, cy + 40 - ry, 2 * rx, 2 * ry), paint("#C9CED8", a))
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, cy + 40 - ry, 2 * rx, 2 * ry), paint(INK2, a, stroke=4))
    ang = giro * 2 * math.pi
    mx = cx + rx * 0.85 * math.cos(ang)
    my = cy + 40 + ry * 0.85 * math.sin(ang)
    c.drawLine(cx, cy + 40, mx, my, paint(RED, a, stroke=6, cap_round=True))


def regua_pol(c, x0, y, a, esc=150):
    """1 polegada ao lado de 1 centímetro, na mesma escala (esc = px por cm)"""
    if a <= 0:
        return
    rrect(c, x0, y - 40, 2.54 * esc, 50, 8, "#F4D27A", a)
    text(c, "1 polegada", x0 + 2.54 * esc / 2, y - 60, 30, "black", PURPLE, a)
    rrect(c, x0, y + 50, esc, 50, 8, "#BFD8F2", a)
    text(c, "1 cm", x0 + esc / 2, y + 140, 30, "black", BLUE, a)
    for k in range(3):
        line(c, x0 + k * esc, y + 10, x0 + k * esc, y + 30, INK2, a, 3)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


KMH = ("72", "km", "", "h")
KM_M = ("1 000", "m", "1", "km")
H_S = ("1", "h", "3 600", "s")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "UNIDADES E CONVERSÕES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    chip(c, "3,6 ?", 620, 300, AMBER, aa, 60)
    ab = ep(t, C["01.b"], 0.5)
    chip(c, "×  ou  ÷ ?", 1300, 300, AMBER, ab, 60)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        r1 = ep(t, C["01.c"] + 1.2, 0.5)
        r2 = ep(t, C["01.c"] + 2.0, 0.5)
        cadeia(c, W / 2, 500, [KMH, KM_M, H_S], 60, riscos={(0, "t"): r1, (1, "b"): r1, (0, "b"): r2, (2, "t"): r2},
               cores={(1, "t"): GREEN, (2, "b"): GREEN}, a=acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 760, ad, "E AINDA AVISA QUANDO VOCÊ ERROU", GREEN, -2, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "converter qualquer unidade composta", "deixando as unidades se cancelarem"),
            ("02.b", "usar qualquer fator do enunciado", "polegada, milha, libra, galão...")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 52, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EPISÓDIO 3 E A SÉRIE DE FRAÇÕES", GREEN)
    aa, da = rise(t, C["03.a"])
    badge_num(c, 1, 300, 330 + da - 14, aa, 30, bg=BLUE)
    text(c, "fração de dois andares", 360, 330 + da, 42, "black", INK, aa, align="left")
    text(c, "km/h  →  m/s:   ÷ 3,6", 1080, 330 + da, 46, "black", GREEN, aa, align="left")
    ab, db = rise(t, C["03.b"])
    badge_num(c, 2, 300, 560 + db - 14, ab, 30, bg=BLUE)
    text(c, "igual em cima e embaixo se cancela", 360, 560 + db, 42, "black", INK, ab, align="left")
    if ab > 0:
        expr(c, "6/6 = 1", 1300, 540 + db, 80, ab, cores={2: GREEN})
        r = ep(t, C["03.b"] + 2.0, 0.5)
        if r > 0:
            strike(c, 1180, 560, 1240, 470, ab, RED, r)
            strike(c, 1180, 650, 1240, 560, ab, RED, r)


def b_cotidiano(c, t, C, B):
    head(c, t, B["start"], "UMA TROCA DE DINHEIRO", "MUDA A FORMA, NÃO O VALOR", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    notas(c, 640, 380, aa, ep(t, C["04.a"] + 1.6, 1.0))
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        boxed(c, 1100, 300, 560, 160, GREEN, ab, 0.08)
        text(c, "mesmo valor", 1380, 370, 46, "black", GREEN, ab)
        text(c, "mudou só a forma", 1380, 425, 30, "bold", INK2, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        itens = [("TV", "polegadas"), ("avião", "pés"), ("chuveiro", "kW"), ("conta de luz", "kWh")]
        for k, (o, u) in enumerate(itens):
            ak = acc * ep(t, C["04.c"] + 0.9 * k, 0.4)
            x = 330 + k * 370
            rrect(c, x - 160, 600, 320, 150, 20, "#F7F7F5", ak)
            text(c, o, x, 655, 32, "bold", INK2, ak)
            text(c, u, x, 715, 42, "black", PURPLE, ak)


# ======================================================================
# blocos a, b, c — a fração que vale 1, a cadeia, a conferência
# ======================================================================

def b_vale1(c, t, C, B):
    head_seq(c, t, C, [("05", "A IDEIA", "UMA FRAÇÃO QUE VALE 1", BLUE), ("06", "AS UNIDADES", "SE CANCELAM", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        cadeia(c, 560, 400, [KM_M], 84, a=aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            text_mid(c, "= 1", 820, 400, 96, "black", GREEN, ab)
            text(c, "a mesma distância", 560, 600, 32, "bold", GRAY, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            boxed(c, 1040, 280, 640, 200, BLUE, acc, 0.08)
            text(c, "FRAÇÃO DE CONVERSÃO", 1360, 345, 40, "black", BLUE, acc)
            text(c, "vale 1, com unidades", 1360, 400, 30, "bold", INK2, acc)
            text(c, "diferentes em cima e embaixo", 1360, 442, 30, "bold", INK2, acc)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            regra(c, "× 1 não muda o valor (como trocar a nota)", W / 2, 720, ad, 34)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        cadeia(c, 560, 400, [("", "km", "", "km")], 100, riscos={(0, "t"): ep(t, C["06.a"] + 2.2, 0.5),
                                                                  (0, "b"): ep(t, C["06.a"] + 2.2, 0.5)}, a=aa)
        text(c, "como 6/6: risca", 560, 610, 34, "bold", GRAY, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        boxed(c, 1000, 300, 700, 230, PURPLE, ab, 0.08)
        text(c, "ANÁLISE DIMENSIONAL", 1350, 370, 42, "black", PURPLE, ab)
        text(c, "multiplicar por frações que valem 1", 1350, 430, 30, "bold", INK2, ab)
        text(c, "e deixar as unidades se riscarem", 1350, 475, 30, "bold", INK2, ab)


def b_cadeia(c, t, C, B):
    head_seq(c, t, C, [("07", "72 km/h EM m/s", "PRIMEIRO, O QUILÔMETRO", PURPLE),
                       ("08", "72 km/h EM m/s", "AGORA, A HORA", PURPLE)])
    card(c, *CARD_R)
    a0 = ep(t, C["07.a"], 0.5)
    a1 = ep(t, C["07.b"], 0.5)
    a2 = ep(t, C["08.a"], 0.5)
    r1 = ep(t, C["07.c"], 0.6)
    r2 = ep(t, C["08.b"], 0.6)
    ok = ep(t, C["08.c"], 0.4)
    cores = {(1, "t"): mix(BLUE, GREEN, ok), (2, "b"): mix(BLUE, GREEN, ok)}
    riscos = {(0, "t"): r1, (1, "b"): r1, (0, "b"): r2, (2, "t"): r2}
    cadeia(c, W / 2, 400, [KMH, KM_M, H_S], 72, alfas=[a0, a1, a2], riscos=riscos, cores=cores)
    if t < C["08"]:
        ab = ep(t, C["07.b"] + 1.4, 0.4)
        if ab > 0:
            text(c, "km em cima → fração com km EMBAIXO", W / 2, 640, 34, "black", AMBER, ab)
    else:
        if ab := ep(t, C["08.a"] + 0.6, 0.4) * (1 - ok):
            text(c, "h embaixo → fração com h EM CIMA", W / 2, 640, 34, "black", AMBER, ab)
        if ok > 0:
            text(c, "sobrou:  m / s", W / 2, 620, 36, "black", GREEN, ok)
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            linha(c, [("72 × 1 000 ÷ 3 600 = ", INK), ("20 m/s", GREEN)], W / 2, 730, 56, ad)


def b_confere(c, t, C, B):
    head_seq(c, t, C, [("09", "O MÉTODO", "SE CONFERE SOZINHO", AMBER), ("10", "ATALHO", "MONTE CERTO DE PRIMEIRA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        ab = ep(t, C["09.b"], 0.5)
        cores = {(0, "t"): mix(BLUE, RED, ab), (1, "t"): mix(BLUE, RED, ab), (1, "b"): mix(BLUE, RED, ab),
                 (0, "b"): mix(BLUE, RED, ab)}
        cadeia(c, W / 2, 360, [KMH, ("1", "km", "1 000", "m")], 80, alfas=[1, aa], cores=cores, a=ep(t, C["09"], 0.4))
        if ab > 0:
            check_icon(c, 790, 508, 26, ab, RED, "x")
            text(c, "nada se cancela", 830, 520, 34, "black", RED, ab, align="left")
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            linha(c, [("sobra:  km² / (m · h)", RED)], W / 2, 620, 44, acc)
            text(c, "sem sentido", W / 2, 690, 30, "bold", GRAY, acc)
        ad = ep(t, C["09.d"], 0.5)
        if ad > 0:
            selo(c, W / 2, 770, ad, "ALGUMA FRAÇÃO ESTÁ DE CABEÇA PARA BAIXO", RED, -2, 30)
        return
    cadeia(c, 560, 470, [KMH, KM_M, H_S], 56, riscos={(0, "t"): 1, (1, "b"): 1, (0, "b"): 1, (2, "t"): 1},
           a=ep(t, C["10"], 0.4) * 0.9)
    aa = ep(t, C["10.a"], 0.5)
    K.atalho(c, 1040, 300, 640, 180, "ATALHO", ["a unidade que você quer eliminar", "vai no ANDAR OPOSTO"], aa, 34)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        text(c, "km em cima  →  km embaixo", 1360, 580, 32, "black", INK, ab)
        text(c, "h embaixo  →  h em cima", 1360, 640, 32, "black", INK, ep(t, C["10.b"] + 1.6, 0.4))


# ======================================================================
# bloco d — várias unidades (densidade)
# ======================================================================

def b_densidade(c, t, C, B):
    head_seq(c, t, C, [("11", "VÁRIAS UNIDADES", "O MÉTODO VALE OURO", PURPLE), ("12", "RISCANDO", "O PORQUÊ DO × 1 000", PURPLE)])
    card(c, *CARD_R)
    ab = ep(t, C["11.b"], 0.5)
    acc = ep(t, C["11.c"], 0.5)
    ad = ep(t, C["11.d"], 0.5)
    r1 = ep(t, C["12"], 0.6)
    r2 = ep(t, C["12"] + 1.6, 0.6)
    ok = ep(t, C["12.a"], 0.4)
    termos = [("2,7", "g", "", "cm³"), ("1", "kg", "1 000", "g"), ("1 000 000", "cm³", "1", "m³")]
    cores = {(1, "t"): mix(BLUE, GREEN, ok), (2, "b"): mix(BLUE, GREEN, ok)}
    cadeia(c, W / 2, 380, termos, 58, alfas=[ab, acc, ad], riscos={(0, "t"): r1, (1, "b"): r1, (0, "b"): r2, (2, "t"): r2},
           cores=cores)
    aa = ep(t, C["11.a"], 0.5) * (1 - ab)
    if aa > 0:
        text(c, "a unidade mistura várias coisas", W / 2, 400, 44, "black", INK2, aa)
    if t < C["12"]:
        if ad > 0:
            text(c, "1 000 000 cm³ = 1 m³: o cubo de cubinhos do episódio 2", W / 2, 620, 30, "bold", GRAY, ad)
        return
    if ok > 0:
        text(c, "sobrou:  kg / m³", W / 2, 600, 36, "black", GREEN, ok)
    ab2 = ep(t, C["12.b"], 0.5)
    if ab2 > 0:
        linha(c, [("2,7 × 1 000 000 ÷ 1 000 = ", INK), ("2 700 kg/m³", GREEN)], W / 2, 690, 48, ab2)
    ac2 = ep(t, C["12.c"], 0.5)
    if ac2 > 0:
        pill(c, "o × 1 000 = 1 000 000 ÷ 1 000", W / 2, 790, PURPLE, size=30, a=ac2, anchor="center", bounds=(0, 1920))


# ======================================================================
# blocos e, f — unidades de fora e a conferência de sentido
# ======================================================================

TABELA = [("13.b", "polegada", "2,54 cm", "telas"), ("13.b", "pé", "≈ 30,5 cm", "aviação"),
          ("13.b", "milha", "≈ 1,6 km", "distâncias"), ("13.c", "libra", "≈ 0,45 kg", "peso"),
          ("13.c", "galão", "≈ 3,785 L", "combustível"), ("13.d", "caloria", "≈ 4,18 J", "energia")]


def b_fora(c, t, C, B):
    head_seq(c, t, C, [("13", "UNIDADES DE FORA", "DO SISTEMA MÉTRICO", BLUE), ("14", "A PROVA TE DÁ O FATOR", "USE-O", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        for k, (cue, u, eq, ctx) in enumerate(TABELA):
            a = ep(t, C[cue] + 0.9 * (k % 3 if cue == "13.b" else (k - 3) if cue == "13.c" else 0), 0.4)
            y = 270 + k * 88
            rrect(c, 320, y - 34, 1280, 72, 14, "#F7F7F5", a)
            text(c, u, 360, y + 14, 38, "black", PURPLE, a, align="left")
            text(c, "=", 760, y + 14, 38, "black", GRAY, a)
            text(c, eq, 820, y + 14, 38, "black", INK, a, align="left")
            text(c, ctx, 1560, y + 14, 30, "bold", GRAY, a, align="right")
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        selo(c, W / 2, 290, aa, "A PROVA SEMPRE TE DÁ O FATOR", GREEN, -2, 36)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        r = ep(t, C["14.b"] + 3.6, 0.6)
        cadeia(c, 820, 500, [("10", "mi", "", ""), ("1,6", "km", "1", "mi")], 72,
               alfas=[1, ep(t, C["14.b"] + 1.6, 0.4)], riscos={(0, "t"): r, (1, "b"): r}, a=ab)
        ok = ep(t, C["14.b"] + 4.6, 0.4)
        if ok > 0:
            linha(c, [("= ", INK), ("16 km", GREEN)], 1380, 530, 72, ok)


def b_sentido(c, t, C, B):
    head(c, t, B["start"], "MULTIPLICA OU DIVIDE?", "PENSE NO TAMANHO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    regua_pol(c, 300, 400, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("pol  →  cm:  o número ", INK), ("CRESCE", GREEN)], 1260, 360, 44, ab)
        linha(c, [("2 pol = ", INK), ("5,08 cm", GREEN)], 1260, 450, 44, ab)
    acc = ep(t, C["15.c"], 0.5)
    K.atalho(c, 940, 560, 640, 200, "ATALHO", ["de unidade GRANDE para PEQUENA,", "o número cresce",
                                               "diminuiu? você dividiu"], acc, 30)


# ======================================================================
# bloco g — o quilowatt-hora
# ======================================================================

def b_kwh(c, t, C, B):
    head_seq(c, t, C, [("16", "O QUILOWATT-HORA", "POTÊNCIA × ENERGIA", BLUE), ("17", "O CHUVEIRO", "5 kW POR 12 MINUTOS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["16", "17"])
    if sid == "16":
        aa = ep(t, C["16.a"], 0.5)
        if aa > 0:
            boxed(c, 220, 260, 680, 170, BLUE, aa, 0.08)
            text(c, "POTÊNCIA", 560, 320, 44, "black", BLUE, aa)
            text(c, "a rapidez do gasto · em kW", 560, 380, 30, "bold", INK2, aa)
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            boxed(c, 1020, 260, 680, 170, GREEN, ab, 0.08)
            text(c, "ENERGIA", 1360, 320, 44, "black", GREEN, ab)
            text(c, "o total gasto · em kWh", 1360, 380, 30, "bold", INK2, ab)
        acc = ep(t, C["16.c"], 0.5)
        if acc > 0:
            linha(c, [("1 kW", BLUE), ("  ×  ", GRAY), ("1 h", AMBER), ("  =  ", GRAY), ("1 kWh", GREEN)], W / 2, 540, 60, acc)
        ad = ep(t, C["16.d"], 0.5)
        if ad > 0:
            text(c, "litros = vazão × tempo", W / 2, 680, 34, "bold", GRAY, ad)
            linha(c, [("kWh = ", GREEN), ("potência × tempo", INK)], W / 2, 750, 44, ad)
        return
    a0 = ep(t, C["17"], 0.5)
    aa = ep(t, C["17.a"], 0.5)
    chuveiro(c, 380, 430, a0, aa)
    acc = ep(t, C["17.c"], 0.5)
    giro = ep(t, C["17.a"], 4.0)
    relogio_luz(c, 1500, 470, a0, giro * 3, "1,0" if acc > 0.5 else "0,0")
    if aa > 0:
        text(c, "5 kW · 12 min", 380, 650, 40, "black", INK, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        expr(c, "12/60 = 0,2", 940, 360, 72, ab, cores={2: AMBER})
        text(c, "hora", 940, 470, 34, "black", AMBER, ab)
    if acc > 0:
        linha(c, [("5 × 0,2 = ", INK), ("1 kWh", GREEN)], 940, 560, 56, acc)
    ad = ep(t, C["17.d"], 0.5)
    K.atalho(c, 660, 640, 560, 150, "ATALHO", ["kWh = kW × HORAS", "minutos viram hora antes"], ad, 30)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E CONVERTA", GREEN), ("19", "VAMOS CONFERIR", "PAUSE E CONVERTA", GREEN)])
    card(c, *CARD_R)
    contas = [("18.a", "18 km/h → m/s", "19.a", "5 m/s", "18 × 1 000 ÷ 3 600"),
              ("18.b", "40 pol → cm", "19.b", "101,6 cm", "40 × 2,54  ·  1 pol = 2,54 cm")]
    for k, (cue, s, cr, r, conta) in enumerate(contas):
        y = 330 + k * 210
        a = ep(t, C[cue], 0.5)
        rrect(c, 260, y - 75, 1400, 170, 22, "#F7F7F5", a)
        text(c, s, 600, y + 18, 56, "black", INK, a)
        text(c, "=", 1000, y + 18, 56, "black", GRAY, a)
        if t >= C["19"]:
            ar = ep(t, C[cr], 0.4)
            text(c, r, 1300, y + 18, 56, "black", GREEN, ar)
            text(c, conta, 960, y + 72, 26, "bold", GRAY, ar)
        else:
            text(c, "?", 1300, y + 18, 56, "black", AMBER, a)
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 790)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Multiplique por frações que valem 1.", "Risque as unidades; o que sobra é a resposta.",
          "Unidade de fora? A prova te dá o fator: use-o."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Montar a fração de conversão de cabeça para baixo", "os números são os mesmos: mil e um",
          "as unidades não se cancelam: a que você quer eliminar vai no andar oposto"),
         ("Converter só o numerador (g/cm³ → kg/m³ mudando só o grama)", "o quilo apareceu",
          "o cm³ continua lá: os DOIS andares mudam"),
         ("Dividir pelo fator da polegada em vez de multiplicar", "dividir parece o caminho natural",
          "a polegada é maior que o cm: o número em cm tem que CRESCER"),
         ("Achar que kWh é potência", "tem quilowatt no nome",
          "o hora no final muda tudo: kWh = potência × tempo = ENERGIA")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23", "24"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=32, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _rodape(c, a):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a, align="left")


ALTS5 = [("A", "0,0008 kg/m³", "só o andar de cima", RED), ("B", "0,8 kg/m³", "não converteu", RED),
         ("C", "80 kg/m³", "usou o fator 100", RED), ("D", "800 kg/m³", "", GREEN),
         ("E", "800 000 kg/m³", "só o andar de baixo", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "DENSIDADE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    _enunciado(c, [("Um óleo vegetal tem densidade de 0,8 g/cm³.", INK),
                   ("Essa densidade, expressa em quilogramas por metro cúbico, corresponde a", BLUE)], a0, 250)
    _rodape(c, a0)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABCE"}
    if t >= C["25.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS5, 1000, 250, 680, 40, C["26.ok"], "D", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["25.end"] - 1.9, 540, 660)
    sid = which(t, C, ["25", "26", "27"])
    if sid == "26":
        ra = ep(t, C["26"], 0.4)
        rrect(c, 170, 440, 760, 370, 18, "#FFFFFF", ra, shadow=True)
        r1 = ep(t, C["26.a"] + 1.4, 0.5)
        r2 = ep(t, C["26.b"] + 1.6, 0.5)
        termos = [("0,8", "g", "", "cm³"), ("1", "kg", "1 000", "g"), ("1 000 000", "cm³", "1", "m³")]
        cadeia(c, 550, 520, termos, 30, alfas=[1, ep(t, C["26.a"], 0.4), ep(t, C["26.b"], 0.4)],
               riscos={(0, "t"): r1, (1, "b"): r1, (0, "b"): r2, (2, "t"): r2}, gap=44, a=ra)
        acc = ep(t, C["26.c"], 0.4)
        if acc > 0:
            linha(c, [("= ", INK), ("800 kg/m³", GREEN)], 550, 640, 46, acc)
        ad = ep(t, C["26.d"], 0.4)
        if ad > 0:
            text(c, "água: 1 g/cm³ = 1 000 kg/m³", 550, 720, 28, "black", BLUE, ad)
            text(c, "óleo: menos denso → menos que 1 000 → boia", 550, 765, 24, "bold", GRAY, ad)
    elif sid == "27":
        ra = ep(t, C["27"], 0.4)
        rrect(c, 170, 470, 760, 330, 18, "#FFFFFF", ra, shadow=True)
        text(c, "converta os DOIS andares", 550, 540, 34, "black", PURPLE, ra)
        aa = ep(t, C["27.xa"], 0.4)
        if aa > 0:
            text(c, "A: só g → kg", 550, 620, 30, "black", RED, aa)
        ae = ep(t, C["27.xe"], 0.4)
        if ae > 0:
            text(c, "E: só cm³ → m³", 550, 680, 30, "black", RED, ae)


ALTS8 = [("A", "19,7 cm", "dividiu", RED), ("B", "52,5 cm", "somou", RED), ("C", "127 cm", "", GREEN),
         ("D", "254 cm", "usou 100 polegadas", RED), ("E", "1 270 cm", "isso é em mm", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "UNIDADE DE FORA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    _enunciado(c, [("Uma televisão é anunciada como tendo 50 polegadas de diagonal.", INK),
                   ("Considerando que 1 polegada equivale a 2,54 cm, a diagonal dessa televisão mede, em centímetros,",
                    BLUE)], a0, 250)
    _rodape(c, a0)
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABDE"}
    if t >= C["28.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS8, 1000, 250, 680, 44, C["29.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["28.end"] - 1.9, 540, 690)
    if t >= C["29"]:
        ra = ep(t, C["29"], 0.4)
        rrect(c, 170, 500, 760, 300, 18, "#FFFFFF", ra, shadow=True)
        r = ep(t, C["29.a"] + 2.4, 0.5)
        cadeia(c, 550, 570, [("50", "pol", "", ""), ("2,54", "cm", "1", "pol")], 40,
               alfas=[1, ep(t, C["29.a"], 0.4)], riscos={(0, "t"): r, (1, "b"): r}, gap=50, a=ra)
        ab = ep(t, C["29.b"], 0.4)
        if ab > 0:
            linha(c, [("= ", INK), ("127 cm", GREEN)], 550, 700, 52, ab)
            conferido(c, "cresceu: plausível", 420, 770, ep(t, C["29.ok"] + 0.6, 0.4), True, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        text(c, "juntamos tudo", W / 2, 330, 48, "black", INK, aa)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 440, ab, "PEGADINHAS", AMBER, -3, 40)
    acc = ep(t, C["31.c"], 0.5)
    for k, s in enumerate(("Matemática", "Física", "Química")):
        chip(c, s, 640 + k * 320, 580, BLUE, acc * ep(t, C["31.c"] + 0.6 * k, 0.4), 40)
    pill(c, "ep. 5 · revisão e treino", W / 2, 740, PURPLE, size=32, a=acc, anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Quantos cm tem a diagonal da sua TV?",
        canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, cotidiano=b_cotidiano, vale1=b_vale1, cadeia=b_cadeia,
              confere=b_confere, densidade=b_densidade, fora=b_fora, sentido=b_sentido, kwh=b_kwh, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q5=b_q5, q8=b_q8, ponte=b_ponte, cta=b_cta)
