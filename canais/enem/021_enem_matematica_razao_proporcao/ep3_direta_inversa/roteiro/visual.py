"""Visual — Razão, Proporção e Regra de Três, Episódio 3: Direta ou inversa? e a regra de três simples (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, pizza, atalho...).
Cores com função: azul = definição (e o lado DIRETA) · roxo = regra/fórmula (e o lado INVERSA) · âmbar = armadilha ·
verde = atalho/dica · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum021", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_razao_ep3_direta_inversa.mp4"
CARD_R = K.CARD_R
DIR, INV = BLUE, PURPLE          # lado DIRETA / lado INVERSA
PAO, PAO_ESC = "#D9A55B", "#B07A35"
PELE = "#F2C9A0"


# ======================================================================
# peças do episódio
# ======================================================================

def boneco(c, x, y, s, col, a=1.0):
    """bonequinho: cabeça + corpo; (x, y) = base dos pés"""
    if a <= 0:
        return
    c.drawCircle(x, y - s * 1.55, s * 0.36, paint(PELE, a))
    rrect(c, x - s * 0.42, y - s * 1.12, s * 0.84, s * 1.12, s * 0.3, col, a)


def pao(c, cx, cy, a=1.0, s=1.0):
    if a <= 0:
        return
    w, h = 120 * s, 62 * s
    rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, PAO, a, shadow=True)
    for k in (-1, 0, 1):
        line(c, cx + k * 28 * s - 10 * s, cy - 14 * s, cx + k * 28 * s + 10 * s, cy + 12 * s, PAO_ESC, a, 4 * s)


def barras(c, x, y, mode, u, a, l1, l2, col, bw=90, sp=120):
    """duas barras: DIRETA = as duas crescem juntas; INVERSA = uma cresce e a outra encolhe. (x, y) = canto esquerdo da base"""
    if a <= 0:
        return
    h1 = 60 + 160 * u
    h2 = 60 + 160 * u if mode == "direta" else 220 - 160 * u * 0.75
    for k, (h, lab, cc) in enumerate(((h1, l1, col), (h2, l2, mix(col, "#FFFFFF", 0.35)))):
        bx = x + k * sp
        rrect(c, bx, y - h, bw, h, 14, cc, a)
        text(c, lab, bx + bw / 2, y + 32, 22, "black", INK2, a)


def selo_dobro(c, cx, cy, a, g1, g2, direta, w=520):
    """o selo TESTE DO DOBRO: g1 ×2 → g2 ×2 (direta) ou ÷2 (inversa)"""
    if a <= 0:
        return
    col = DIR if direta else INV
    h = 150
    rrect(c, cx - w / 2, cy - h / 2, w, h, 20, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 20, AMBER, 0.08 * a)
    pill(c, "TESTE DO DOBRO", cx, cy - h / 2, AMBER, size=20, a=a, anchor="center", bounds=(0, 1920))
    text(c, g1, cx - w / 4, cy + 4, 28, "black", INK, a)
    fmid(c, "× 2", cx - w / 4, cy + 42, 30, "black", AMBER, a)
    arrow(c, cx - 40, cy + 20, cx + 40, cy + 20, LIGHT, a, 4, 12)
    text(c, g2, cx + w / 4, cy + 4, 28, "black", INK, a)
    fmid(c, "× 2" if direta else "÷ 2", cx + w / 4, cy + 42, 30, "black", col, a)


PASSOS = ["padronize as unidades", "monte duas colunas", "direta ou inversa?", "se inversa, inverta uma coluna",
          "multiplique em cruz"]
PASSOS_CURTOS = ["unidades", "colunas", "direta ou inversa?", "inverter?", "cruz"]


def passos_h(c, cx, y, ativo, a=1.0, feitos=0):
    """os 5 passos numa faixa horizontal; `ativo` = passo aceso (1..5); passos < feitos ficam marcados"""
    if a <= 0:
        return
    ws = [text_w(s, "black", 20) + 64 for s in PASSOS_CURTOS]
    gap = 10
    x = cx - (sum(ws) + gap * 4) / 2
    for k, (s, w) in enumerate(zip(PASSOS_CURTOS, ws)):
        n = k + 1
        on = n == ativo
        done = n < feitos or (feitos and n < ativo)
        bg = PURPLE if on else ("#F1EEFE" if done else "#F4F4F2")
        rrect(c, x, y - 22, w, 44, 22, bg, a)
        badge_num(c, n, x + 22, y, a, 14, bg="#FFFFFF" if on else (PURPLE if done else LIGHT), fg=PURPLE if on else "#FFFFFF")
        text_mid(c, s, x + 40 + (w - 40) / 2, y, 20, "black", "#FFFFFF" if on else (PURPLE if done else GRAY), a)
        x += w + gap


def colunas(c, x, y, h1, h2, v, a=1.0, cruz=0.0, inv=0.0, alfas=None, w=170, col=INK):
    """tabela de duas colunas: cabeçalhos h1, h2; v = [[a, b], [c, d]] (texto); inv = 0..1 gira a coluna 1 (inverte);
    cruz = 0..1 desenha o X do produto cruzado. (x, y) = topo à esquerda"""
    if a <= 0:
        return
    alfas = alfas or {}
    for j, h in enumerate((h1, h2)):
        cx = x + w / 2 + j * (w + 40)
        text(c, h, cx, y + 26, 24, "black", GRAY, a)
        line(c, cx - w / 2 + 10, y + 42, cx + w / 2 - 10, y + 42, LINE, a, 3)
    for i in range(2):
        for j in range(2):
            s = v[i][j]
            aij = a * alfas.get((i, j), 1.0)
            if aij <= 0:
                continue
            cx = x + w / 2 + j * (w + 40)
            cy = y + 100 + i * 90
            if j == 0 and inv > 0:
                # a coluna 1 troca de lugar (de cabeça para baixo)
                cy = y + 100 + (i + (1 - 2 * i) * ease_io(inv)) * 90
            fmid(c, s, cx, cy, 52, "black", RED if s == "x" else col, aij)
    if cruz > 0:
        x0, x1 = x + w / 2 + 40, x + w / 2 + (w + 40) - 40
        line(c, x0, y + 110, x1, y + 180, AMBER, a * cruz, 5, progress=cruz)
        line(c, x0, y + 180, x1, y + 110, AMBER, a * cruz, 5, progress=cruz)


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REGRA DE TRÊS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        card(c, 260, 220, 620, 300, aa)
        text(c, "a multiplicação", 570, 280, 30, "black", GRAY, aa)
        expr(c, "8 · x = 4800", 570, 380, 64, aa)
        check_icon(c, 570, 470, 30, aa, GREEN)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        card(c, 1040, 220, 620, 300, ab)
        text(c, "a decisão", 1350, 280, 30, "black", GRAY, ab)
        chip(c, "DIRETA", 1230, 390, DIR, ab, 34)
        chip(c, "INVERSA", 1470, 390, INV, ab, 34)
        acx = ep(t, C["01.b"] + 1.4, 0.4)
        check_icon(c, 1350, 470, 30, acx, RED, "x")
    ac = ep(t, C["01.c"], 0.5)
    selo(c, W / 2, 690, ac, "CONTA PERFEITA, PROBLEMA TROCADO", RED, -3, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "decidir em segundos", "direta ou inversa?"), ("02.b", "resolver qualquer regra de três simples", "em 5 passos")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 54, 32, "bold", GRAY, a, align="left")
    ac = ep(t, C["02.c"], 0.5)
    if ac > 0:
        boxed(c, 460, 650, 1000, 120, AMBER, ac, 0.10)
        text_mid(c, "a pergunta: o que acontece no DOBRO?", W / 2, 710, 44, "black", INK, ac)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETE DO EPISÓDIO 2", "PONTAS E MIOLO", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    cx, cy = 700, 420
    expr(c, "2/3 = 4/6", cx, cy, 130, aa, cores={0: INK, 2: INK})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        # X ligando pontas (2 e 6) e miolo (3 e 4)
        line(c, cx - 200, cy - 60, cx + 200, cy + 60, AMBER, ab, 6, progress=ab)
        line(c, cx - 200, cy + 60, cx + 200, cy - 60, PURPLE, ab, 6, progress=ab)
        text(c, "pontas", cx - 260, cy - 110, 28, "black", AMBER, ab)
        text(c, "miolo", cx - 260, cy + 150, 28, "black", PURPLE, ab)
    acc = ep(t, C["03.c"], 0.5)
    expr(c, "2 · 6 = 12", 1350, 360, 64, acc, cores={4: AMBER})
    expr(c, "3 · 4 = 12", 1350, 480, 64, ep(t, C["03.c"] + 1.2, 0.5), cores={4: PURPLE})
    ad = ep(t, C["03.d"], 0.5)
    pill(c, "multiplicar em X = PRODUTO CRUZADO", W / 2, 720, BLUE, size=34, a=ad, anchor="center", bounds=(0, 1920))


# ======================================================================
# cotidiano: pão e pizza
# ======================================================================

def b_cotidiano(c, t, C, B):
    head_seq(c, t, C, [("04", "DUAS CENAS DO DIA A DIA", "O QUE ACONTECE NO DOBRO?", BLUE),
                       ("05", "PÃO, PREÇO, AMIGOS, FATIAS", "GRANDEZAS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    line(c, 960, 210, 960, 800, "#E6E6E2", ep(t, C["04"], 0.4), 3)
    baixo = 1 - ep(t, C["05.a"], 0.4) if sid == "05" else 1.0
    # padaria
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        text(c, "PADARIA", 560, 240, 26, "black", GRAY, aa, tracking=2)
        pao(c, 400, 340, aa)
        pill(c, "R$ 1", 400, 410, INK2, size=26, a=aa, anchor="center", bounds=(0, 1920))
        ab = ep(t, C["04.b"], 0.5)
        dx = ep(t, C["04.a"] + 0.8, 0.5)
        pao(c, 660, 320, dx * aa, 0.85); pao(c, 760, 360, dx * aa, 0.85)
        fmid(c, "× 2", 560, 340, 40, "black", AMBER, dx * aa)
        pill(c, "R$ 2", 710, 430, DIR, size=26, a=ab, anchor="center", bounds=(0, 1920))
        chip(c, "dobrou também", 560, 540, DIR, ab * baixo, 32)
    # pizza
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        text(c, "PIZZA DE 8 FATIAS", 1360, 240, 26, "black", GRAY, acc, tracking=2)
        ad = ep(t, C["04.d"], 0.5)
        n = 2 if ad < 0.5 else 4
        K.pizza(c, 1360, 400, 120, 8, 8 // n, acc, pull=0.25)
        for k in range(n):
            x = 1360 - (n - 1) * 70 + k * 140
            boneco(c, x, 640, 44, [BLUE, GREEN, AMBER, PURPLE][k], (acc if k < 2 else ad) * baixo)
        ae = ep(t, C["04.e"], 0.5)
        text(c, f"{8 // n} fatias para cada um", 1360, 700, 30, "black", INV if n == 4 else INK2, acc * baixo)
        chip(c, "virou metade", 1360, 770, INV, ae * baixo, 32)
    if sid == "05":
        ag = ep(t, C["05.a"], 0.5)
        if ag > 0:
            rrect(c, 300, 590, 1320, 200, 24, "#FFFFFF", ag, shadow=True)
            text(c, "GRANDEZA = tudo o que dá para MEDIR ou CONTAR", W / 2, 655, 38, "black", BLUE, ag)
            for k, s in enumerate(["pão", "preço", "amigos", "fatias"]):
                chip(c, s, 520 + k * 290, 735, BLUE, ag * ep(t, C["05.a"] + 0.3 * k, 0.3), 30, fill=False)


# ======================================================================
# blocos A e B — direta e inversa (tela dividida)
# ======================================================================

def b_tipos(c, t, C, B):
    head_seq(c, t, C, [("06", "O JEITO DO PÃO", "DIRETAMENTE PROPORCIONAIS", DIR), ("07", "O JEITO DA PIZZA", "INVERSAMENTE PROPORCIONAIS", INV)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    line(c, 960, 210, 960, 800, "#E6E6E2", 1.0, 3)
    on_l = 1.0 if sid == "06" else 0.45
    # ---- DIRETA ----
    a0 = ep(t, C["06"], 0.5) * on_l
    pill(c, "DIRETA", 550, 215, DIR, size=26, a=a0, anchor="center", bounds=(0, 1920))
    rows = [("06.a", "1 kg", "R$ 8"), ("06.b", "2 kg", "R$ 16"), ("06.c", "3 kg", "R$ 24")]
    u = 0.0
    for k, (cue, q, p_) in enumerate(rows):
        a = ep(t, C[cue], 0.4) * on_l
        if a > 0:
            u = k / 2
        y = 300 + k * 70
        text(c, q, 260, y, 40, "black", INK, a, align="left")
        arrow(c, 390, y - 12, 450, y - 12, LIGHT, a, 4, 12)
        text(c, p_, 480, y, 40, "black", DIR, a, align="left")
    barras(c, 690, 480, "direta", u, a0, "kg", "R$", DIR)
    ad = ep(t, C["06.d"], 0.5) * on_l
    chip(c, "uma aumenta → a outra aumenta igual", 550, 570, DIR, ad, 26)
    ae = ep(t, C["06.e"], 0.5) * on_l
    if ae > 0:
        expr(c, "16 ÷ 2 = 8", 400, 640, 40, ae, cores={4: GREEN})
        expr(c, "24 ÷ 3 = 8", 700, 640, 40, ep(t, C["06.e"] + 1.6, 0.4) * on_l, cores={4: GREEN})
    af = ep(t, C["06.f"], 0.5) * on_l
    if af > 0:
        boxed(c, 210, 690, 680, 110, DIR, af, 0.08)
        text(c, "QUOCIENTE (resultado da divisão) = CONSTANTE", 550, 735, 24, "black", DIR, af)
        text(c, "constante = um valor que não muda", 550, 778, 24, "bold", INK2, af)
    # ---- INVERSA ----
    if sid != "07":
        return
    b0 = ep(t, C["07"], 0.5)
    pill(c, "INVERSA", 1370, 215, INV, size=26, a=b0, anchor="center", bounds=(0, 1920))
    rows = [("07.a", 2, 4), ("07.b", 4, 2), ("07.c", 8, 1)]
    u = 0.0
    for k, (cue, n, f) in enumerate(rows):
        a = ep(t, C[cue], 0.4)
        if a > 0:
            u = k / 2
        y = 300 + k * 70
        text(c, f"{n} pessoas", 1050, y, 36, "black", INK, a, align="left")
        arrow(c, 1250, y - 12, 1300, y - 12, LIGHT, a, 4, 12)
        text(c, f"{f} fatia{'s' if f > 1 else ''} cada", 1320, y, 36, "black", INV, a, align="left")
    barras(c, 1560, 480, "inversa", u, b0, "pessoas", "fatias", INV, bw=70, sp=100)
    bd = ep(t, C["07.d"], 0.5)
    chip(c, "uma aumenta → a outra diminui igual", 1370, 570, INV, bd, 26)
    be = ep(t, C["07.e"], 0.5)
    for k, s in enumerate(["2 · 4 = 8", "4 · 2 = 8", "8 · 1 = 8"]):
        expr(c, s, 1130 + k * 250, 640, 38, be * ep(t, C["07.e"] + 0.9 + 1.0 * k, 0.4), cores={4: GREEN})
    bf = ep(t, C["07.f"], 0.5)
    if bf > 0:
        boxed(c, 1030, 690, 680, 110, INV, bf, 0.08)
        text(c, "PRODUTO (resultado da multiplicação) = CONSTANTE", 1370, 735, 22, "black", INV, bf)
        text(c, "a pizza inteira: 8 fatias", 1370, 778, 24, "bold", INK2, bf)


# ======================================================================
# bloco C — o teste do dobro
# ======================================================================

def b_teste(c, t, C, B):
    head_seq(c, t, C, [("08", "COMO DECIDIR RÁPIDO?", "O TESTE DO DOBRO", AMBER), ("09", "VAMOS TESTAR", "O TESTE DO DOBRO", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        selo(c, W / 2, 270, aa, "TESTE DO DOBRO", AMBER, -3, 56)
        ab = ep(t, C["08.b"], 0.5)
        text(c, "dobre uma grandeza e pergunte: e a outra?", W / 2, 400, 40, "black", INK, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            boxed(c, 300, 470, 600, 260, DIR, acc, 0.08)
            text(c, "dobrou também?", 600, 560, 40, "black", INK, acc)
            fmid(c, "× 2  →  × 2", 600, 625, 44, "black", AMBER, acc)
            text(c, "DIRETA", 600, 705, 52, "black", DIR, acc)
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            boxed(c, 1020, 470, 600, 260, INV, ad, 0.08)
            text(c, "virou metade?", 1320, 560, 40, "black", INK, ad)
            fmid(c, "× 2  →  ÷ 2", 1320, 625, 44, "black", AMBER, ad)
            text(c, "INVERSA", 1320, 705, 52, "black", INV, ad)
        return
    a0 = ep(t, C["09.a"], 0.5)
    text(c, "operários × dias da obra", 560, 250, 32, "black", INK2, a0)
    for k in range(4):
        aa_ = a0 if k < 2 else ep(t, C["09.a"] + 1.4, 0.4)
        boneco(c, 380 + k * 120, 420, 40, AMBER, aa_)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        for k in range(10):
            on = k < 5 or ab < 0.5
            rrect(c, 300 + k * 52, 470, 42, 42, 8, INV if on else "#EEEEEC", ab)
        text(c, "dias", 300 + 10 * 52 + 20, 500, 24, "bold", GRAY, ab, align="left")
    selo_dobro(c, 560, 640, ep(t, C["09.c"], 0.5), "operários", "dias", False)
    line(c, 960, 220, 960, 760, "#E6E6E2", ep(t, C["09.d"], 0.4), 3)
    ad = ep(t, C["09.d"], 0.5)
    text(c, "quilos × preço", 1360, 250, 32, "black", INK2, ad)
    if ad > 0:
        for k in range(2):
            rrect(c, 1180 + k * 110, 340, 90, 110, 14, "#C9A27A", ad * (1 if k == 0 else ep(t, C["09.d"] + 1.2, 0.4)))
            text_mid(c, "1 kg", 1225 + k * 110, 395, 24, "black", "#FFFFFF", ad * (1 if k == 0 else ep(t, C["09.d"] + 1.2, 0.4)))
        ae = ep(t, C["09.e"], 0.5)
        pill(c, "R$ 8", 1500, 370, INK2, size=28, a=ad * (1 - ae), anchor="center", bounds=(0, 1920))
        pill(c, "R$ 16", 1500, 370, DIR, size=28, a=ae, anchor="center", bounds=(0, 1920))
    selo_dobro(c, 1360, 640, ep(t, C["09.f"], 0.5), "quilos", "preço", True)
    ag = ep(t, C["09.g"], 0.5)
    if ag > 0:
        rrect(c, 260, 720, 1400, 100, 20, "#FFFFFF", ag, shadow=True)
        boxed(c, 260, 720, 1400, 100, GREEN, ag, 0.10)
        text(c, "ATALHO", 400, 780, 22, "black", GREEN, ag, tracking=2)
        text(c, "em voz alta: “se eu dobrar ISSO, AQUILO dobra ou vira metade?”", 1010, 780, 32, "black", INK, ag)


# ======================================================================
# bloco D — crescer junto não basta
# ======================================================================

def crianca(c, x, base, alt_px, a, col, tracejada=False):
    if a <= 0:
        return
    s = alt_px / 2.4
    if tracejada:
        rrect(c, x - s * 0.5, base - alt_px, s, alt_px, s * 0.4, None, a, stroke=4, stroke_color=RED)
        return
    c.drawCircle(x, base - alt_px + s * 0.38, s * 0.38, paint(PELE, a))
    rrect(c, x - s * 0.45, base - alt_px + s * 0.8, s * 0.9, alt_px - s * 0.8, s * 0.3, col, a)


def b_junto(c, t, C, B):
    frame(c, t, B["start"], "CRESCER JUNTO É SER PROPORCIONAL?", "A PEGADINHA", AMBER)
    base, px_m = 760, 230           # 1 m = 230 px
    line(c, 260, base, 1120, base, LIGHT, ep(t, C["10"], 0.4), 3)
    aa = ep(t, C["10.a"], 0.5)
    crianca(c, 420, base, 1.10 * px_m, aa, BLUE)
    text(c, "5 anos", 420, base + 40, 28, "black", INK2, aa)
    text(c, "≈ 1,10 m", 520, base - 1.10 * px_m + 10, 28, "black", BLUE, aa, align="left")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        crianca(c, 820, base, 2.20 * px_m, ab * (1 - 0.6 * ep(t, C["10.c"], 0.4)), RED, True)
        text(c, "2,20 m?", 950, base - 2.20 * px_m + 20, 30, "black", RED, ab, align="left")
    acc = ep(t, C["10.c"], 0.5)
    crianca(c, 820, base, 1.40 * px_m, acc, GREEN)
    text(c, "10 anos", 820, base + 40, 28, "black", INK2, ab)
    text(c, "≈ 1,40 m", 950, base - 1.40 * px_m + 10, 28, "black", GREEN, acc, align="left")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        boxed(c, 1200, 300, 460, 160, AMBER, ad, 0.10)
        text(c, "idade × 2", 1430, 360, 32, "black", INK, ad)
        text(c, "altura NÃO × 2", 1430, 420, 32, "black", RED, ad)
    regra(c, "proporcional = dobrar uma dobra EXATAMENTE a outra", 1430, 560, ep(t, C["10.e"], 0.5), 22)


# ======================================================================
# bloco E — o procedimento em 5 passos
# ======================================================================

def b_procedimento(c, t, C, B):
    head_seq(c, t, C, [("11", "REGRA DE TRÊS SIMPLES", "O PROCEDIMENTO EM 5 PASSOS", PURPLE),
                       ("12", "UM EXEMPLO DIRETO", "TECIDO E PREÇO", DIR), ("13", "UM EXEMPLO INVERSO", "JARDINEIROS E DIAS", INV),
                       ("14", "ATALHO DA INVERSA", "O PRODUTO NÃO MUDA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12", "13", "14"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        text(c, "REGRA DE TRÊS: achar 1 valor desconhecido conhecendo outros 3", W / 2, 230, 32, "black", BLUE, aa)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            chip(c, "INCÓGNITA = o valor desconhecido = x", W / 2, 290, BLUE, ab, 28, fill=False)
        for k, s in enumerate(PASSOS):
            a, d = rise(t, C["11." + "defgh"[k]])
            y = 380 + k * 86 + d
            rrect(c, 420, y - 34, 1080, 70, 18, mix("#FFFFFF", PURPLE, 0.06), a)
            badge_num(c, k + 1, 470, y, a, 24, bg=PURPLE)
            text_mid(c, s, 520, y, 36, "black", INK, a, align="left")
            if k == 0:
                pill(c, "PASSO ZERO", 1480, y, AMBER, size=22, a=a, anchor="right", bounds=(0, 1920))
                text_mid(c, "horas com horas", 1040, y, 24, "bold", GRAY, a, align="left")
            if k == 2:
                pill(c, "teste do dobro", 1480, y, AMBER, size=22, a=a, anchor="right", bounds=(0, 1920))
            if k == 4:
                pill(c, "pontas e miolo", 1480, y, AMBER, size=22, a=a, anchor="right", bounds=(0, 1920))
        return
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        text(c, "6 m de tecido custam R$ 48. E 15 m?", W / 2, 240, 40, "black", INK, aa)
        cue_ativo = [("12.b", 1), ("12.c", 2), ("12.d", 3), ("12.e", 4), ("12.f", 5)]
        ativo = 0
        for cue, n in cue_ativo:
            if t >= C[cue] - 0.1:
                ativo = n
        passos_h(c, W / 2, 315, ativo, ep(t, C["12.b"], 0.4))
        acc = ep(t, C["12.c"], 0.5)
        colunas(c, 330, 370, "metros", "reais", [["6", "48"], ["15", "x"]], acc, cruz=ep(t, C["12.f"], 0.6))
        ad = ep(t, C["12.d"], 0.5)
        selo_dobro(c, 1300, 450, ad, "tecido", "preço", True, w=460)
        chip(c, "DIRETA: nada a inverter", 1300, 580, DIR, ep(t, C["12.e"], 0.5), 28)
        af = ep(t, C["12.f"], 0.5)
        if af > 0:
            rrect(c, 950, 640, 700, 150, 18, "#FFFFFF", af, shadow=True)
            expr(c, "6 · x = 48 · 15 = 720", 1300, 685, 40, af)
            expr(c, "x = 720 ÷ 6 = 120", 1300, 750, 44, ep(t, C["12.g"], 0.4), cores={6: GREEN})
        text(c, "R$ 120", 465, 760, 40, "black", GREEN, ep(t, C["12.g"] + 1.0, 0.4))
        return
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        text(c, "6 jardineiros: 10 dias. E 4 jardineiros?", W / 2, 240, 40, "black", INK, aa)
        ativo = 1 if t < C["13.b"] else (3 if t < C["13.c"] else (4 if t < C["13.d"] else 5))
        passos_h(c, W / 2, 315, ativo, aa)
        ab = ep(t, C["13.b"], 0.5)
        selo_dobro(c, 1300, 450, ab, "jardineiros", "dias", False, w=460)
        inv = ep(t, C["13.c"] + 0.8, 0.9)
        colunas(c, 330, 370, "jardineiros", "dias", [["6", "10"], ["4", "x"]], aa, inv=inv, cruz=ep(t, C["13.d"], 0.6))
        chip(c, "INVERSA: inverta UMA coluna", 1300, 580, INV, ep(t, C["13.c"], 0.5), 28)
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            rrect(c, 950, 640, 700, 150, 18, "#FFFFFF", ad, shadow=True)
            expr(c, "4 · x = 6 · 10 = 60", 1300, 685, 40, ad)
            expr(c, "x = 60 ÷ 4 = 15", 1300, 750, 44, ep(t, C["13.e"], 0.4), cores={6: GREEN})
        af = ep(t, C["13.f"], 0.5)
        if af > 0:
            text(c, "15 dias", 465, 760, 40, "black", GREEN, af)
            check_icon(c, 600, 748, 22, af, GREEN)
            text(c, "menos jardineiros → mais dias", 465, 810, 24, "bold", INK2, af)
        return
    # 14 atalho da inversa
    a0 = ep(t, C["14"], 0.5)
    K.pizza(c, 420, 470, 150, 8, 0, a0 * 0.9)
    text(c, "o produto não muda", 420, 680, 30, "black", INV, a0)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        boxed(c, 720, 240, 980, 520, GREEN, aa, 0.06)
        text(c, "ATALHO DA INVERSA", 1210, 300, 24, "black", GREEN, aa, tracking=2)
        expr(c, "6 · 10 = 60", 1210, 410, 66, ep(t, C["14.b"], 0.4), cores={4: GREEN})
        expr(c, "4 · x = 60", 1210, 520, 66, ep(t, C["14.c"], 0.4), cores={4: GREEN})
        expr(c, "x = 15", 1210, 640, 72, ep(t, C["14.d"], 0.4), cores={2: GREEN})
        text(c, "sem inverter coluna nenhuma", 1210, 720, 28, "bold", INK2, ep(t, C["14.d"] + 0.8, 0.4))


# ======================================================================
# bloco F — o erro silencioso
# ======================================================================

def b_unidades(c, t, C, B):
    frame(c, t, B["start"], "POR QUE O PASSO ZERO?", "O ERRO SILENCIOSO", AMBER)
    aa = ep(t, C["15.a"], 0.5)
    text(c, "40 garrafas em 1 HORA. Quantas em 30 MINUTOS?", W / 2, 240, 40, "black", INK, aa)
    line(c, 960, 290, 960, 800, "#E6E6E2", aa, 3)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        pill(c, "SEM PADRONIZAR", 560, 320, RED, size=24, a=ab, anchor="center", bounds=(0, 1920))
        expr(c, "40/1 = x/30", 560, 440, 64, ab)
        acc = ep(t, C["15.c"], 0.5)
        expr(c, "x = 1200", 560, 570, 64, acc, cores={2: RED})
        ad = ep(t, C["15.d"], 0.5)
        if ad > 0:
            text(c, "a conta fecha… e nenhum alarme toca", 560, 660, 28, "black", INK2, ad)
            selo(c, 560, 740, ad, "ERRO SILENCIOSO", RED, -4, 32)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        pill(c, "PADRONIZANDO: 1 h = 60 min", 1360, 320, GREEN, size=24, a=ae, anchor="center", bounds=(0, 1920))
        expr(c, "40/60 = x/30", 1360, 440, 64, ae)
        af = ep(t, C["15.f"], 0.5)
        expr(c, "x = 20", 1360, 570, 64, af, cores={2: GREEN})
        text(c, "metade do tempo, metade das garrafas", 1360, 660, 28, "black", INK2, af)
        check_icon(c, 1360, 735, 30, af, GREEN)


# ======================================================================
# TREINO — dobrou ou virou metade?
# ======================================================================

TREINO = [("17", "litros de tinta  ×  área pintada", "com a mesma tinta", "tinta × área", True, "tinta", "área"),
          ("18", "velocidade do carro  ×  tempo da viagem", "a mesma viagem", "velocidade × tempo", False, "velocidade", "tempo"),
          ("19", "torneiras iguais  ×  tempo para encher", "o mesmo tanque", "torneiras × tempo", False, "torneiras", "tempo"),
          ("20", "horas trabalhadas  ×  salário", "quem ganha por hora", "horas × salário", True, "horas", "salário"),
          ("21", "pessoas no prêmio  ×  parte de cada uma", "dividido em partes iguais", "pessoas × parte", False, "pessoas", "parte"),
          ("22", "distância  ×  litros de combustível", "no mesmo ritmo", "distância × litros", True, "distância", "litros")]
CX, CY, CW, CH = 960, 470, 640, 420


def _slot(lado_dir, n):
    return (410 if lado_dir else 1510), 330 + n * 74


def b_treino(c, t, C, B):
    frame(c, t, B["start"], "TREINO RÁPIDO", "DOBROU OU VIROU METADE?", AMBER)
    a0 = ep(t, C["16"], 0.5)
    for lado, (x, nome, col) in enumerate(((410, "DIRETA", DIR), (1510, "INVERSA", INV))):
        rrect(c, x - 230, 200, 460, 620, 22, mix("#FFFFFF", col, 0.06), a0)
        pill(c, nome, x, 250, col, size=30, a=a0, anchor="center", bounds=(0, 1920))
        text(c, "dobrou também" if lado == 0 else "virou metade", x, 300, 22, "bold", GRAY, a0)
    sid = which(t, C, ["16"] + [s[0] for s in TREINO])
    if sid == "16":
        aa = ep(t, C["16.a"], 0.5)
        if aa > 0:
            card(c, CX - CW / 2, CY - CH / 2, CW, CH, aa)
            text(c, "6 situações", CX, 400, 56, "black", INK, aa)
            text(c, "sem conta: só a decisão", CX, 470, 32, "bold", INK2, aa)
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            chip(c, "5 segundos para cada uma", CX, 560, AMBER, ab, 32)
    # situações já decididas (nos lados)
    cont = {True: 0, False: 0}
    for k, (s_id, txt, sub, curto, direta, g1, g2) in enumerate(TREINO):
        if t < C[s_id]:
            break
        r, end = C[f"{s_id}.r"], C[f"{s_id}.end"]
        n = cont[direta]; cont[direta] += 1
        sx, sy = _slot(direta, n)
        fly = prog(t, end - 0.9, 0.8)
        if t >= end - 0.9:
            fx, fy = lerp(CX, sx, ease_io(fly)), lerp(CY, sy, ease_io(fly))
            sc = lerp(1.0, 0.0, ease_io(fly))
            if fly < 1:
                # cartão encolhendo a caminho do lado
                rrect(c, fx - CW / 2 * max(sc, 0.25), fy - CH / 2 * max(sc, 0.12), CW * max(sc, 0.25), CH * max(sc, 0.12), 20,
                      "#FFFFFF", 1 - fly * 0.3, shadow=True)
            ac = ep(t, end - 0.2, 0.3)
            rrect(c, sx - 200, sy - 28, 400, 56, 16, "#FFFFFF", ac, shadow=True)
            badge_num(c, k + 1, sx - 170, sy, ac, 16, bg=DIR if direta else INV)
            text_mid(c, curto, sx + 15, sy, 24, "black", INK, ac)
            continue
        # cartão central da situação atual
        aq = ep(t, C[s_id], 0.4)
        card(c, CX - CW / 2, CY - CH / 2, CW, CH, aq)
        text(c, f"SITUAÇÃO {k + 1}", CX, CY - CH / 2 + 50, 22, "black", GRAY, aq, tracking=2)
        partes = txt.split("  ×  ")
        text(c, partes[0], CX, CY - 80, 38, "black", INK, aq)
        fmid(c, "×", CX, CY - 30, 34, "black", AMBER, aq)
        text(c, partes[1], CX, CY + 30, 38, "black", INK, aq)
        text(c, sub, CX, CY + 80, 26, "bold", GRAY, aq)
        # cronômetro de 5 s
        ap = ep(t, C[f"{s_id}.p"], 0.3) * (1 - ep(t, r, 0.3))
        if ap > 0:
            u = clamp((t - (r - 5.0)) / 5.0)
            x, y, rr = CX, CY + 160, 40
            c.drawCircle(x, y, rr + 10, paint(AMBER, ap * 0.18))
            c.drawCircle(x, y, rr, paint("#FFFFFF", ap))
            c.drawArc(skia.Rect.MakeLTRB(x - rr, y - rr, x + rr, y + rr), -90, 360 * (1 - u), False,
                      paint(AMBER, ap, stroke=8, cap_round=True))
            seg = max(1, math.ceil(r - t)) if t >= r - 5.0 else 5
            text_mid(c, str(min(5, seg)), x, y, 38, "black", INK, ap)
        ar = ep(t, r, 0.4)
        if ar > 0:
            rrect(c, CX - 200, CY + 120, 400, 80, 20, DIR if direta else INV, ar)
            text_mid(c, "DIRETA" if direta else "INVERSA", CX, CY + 160, 40, "black", "#FFFFFF", ar)
            aw = ep(t, C[f"{s_id}.w"], 0.4)
            fmid(c, f"{g1} × 2  →  {g2} {'× 2' if direta else '÷ 2'}", CX, CY + 248, 30, "black", AMBER, aw)
    if sid == "22":
        af = ep(t, C["22.f"], 0.5) * (1 - prog(t, C["22.end"] - 0.9, 0.3))
        if af > 0:
            pill(c, "quantas você acertou?", CX, 760, GREEN, size=30, a=af, anchor="center", bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Dobrou também? Direta. Virou metade? Inversa.", "Na direta, o quociente é constante; na inversa, o produto.",
          "Unidades iguais antes de tudo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["23", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "23" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


ERROS = [("Mais operários, MAIS dias (direta onde é inversa)", "a gente se acostuma a montar tudo do mesmo jeito",
          "teste do dobro: o dobro de operários termina em metade dos dias"),
         ("Crescer junto = ser proporcional", "as duas grandezas sobem ao mesmo tempo",
          "proporcional é dobrar EXATAMENTE: idade × 2 não dá altura × 2"),
         ("Regra de três com horas de um lado e minutos do outro", "a conta fecha sem nenhum erro",
          "converta primeiro, monte depois: 1 h = 60 min")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["24", "25", "26"], ERROS)


# ======================================================================
# Questão 4 do material — eu faço
# ======================================================================

Q4_TXT = ("Uma impressora industrial produz 240 páginas em 8 minutos, mantendo ritmo constante. Nessas condições, "
          "em 20 minutos ela produzirá")
Q4_ALTS = [("A", "96 páginas", "montou como inversa", RED), ("B", "480 páginas", "chute de “dobro”", RED),
           ("C", "600 páginas", "", GREEN), ("D", "720 páginas", "chute de “triplo”", RED),
           ("E", "4 800 páginas", "esqueceu de dividir por 8", RED)]
Q5_TXT = ("Uma obra seria concluída por 15 operários em 24 dias. Se a construtora alocar 20 operários com o mesmo ritmo "
          "de trabalho, a obra será concluída em")
Q5_ALTS = [("A", "15 dias", "copiou os operários", RED), ("B", "18 dias", "", GREEN), ("C", "20 dias", "copiou os operários", RED),
           ("D", "24 dias", "achou que nada muda", RED), ("E", "32 dias", "montou como direta", RED)]


def _enunciado(c, txt, a):
    para(c, txt, 190, 240, 32, "black", INK, a, 760, 42)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a, align="left")


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EU FAÇO COM VOCÊ", "REGRA DE TRÊS DIRETA", DIR)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    _enunciado(c, Q4_TXT, a0)
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["29.xa"], "B": C["29.xb"], "D": C["29.xd"], "E": C["29.xe"]}
    if t >= C["27.qa"] - 0.3:
        K.alternativas(c, t, C, Q4_ALTS, 1080, 230, 640, 36, C["28.ok"], "C", cues_in, cues_x, gap=22)
    if t < C["28"]:
        return
    sid = which(t, C, ["28", "29"])
    ra = ep(t, C["28"], 0.4)
    rrect(c, 170, 400, 860, 405, 18, "#FFFFFF", ra, shadow=True)
    if sid == "28":
        ativo = 1 if t < C["28.a"] else (2 if t < C["28.b"] else (3 if t < C["28.c"] else (4 if t < C["28.d"] else 5)))
        passos_h(c, 600, 440, ativo, ra)
        colunas(c, 210, 470, "páginas", "minutos", [["240", "8"], ["x", "20"]], ep(t, C["28.a"], 0.5), cruz=ep(t, C["28.d"], 0.6),
                w=160)
        selo_dobro(c, 830, 560, ep(t, C["28.b"], 0.5), "tempo", "páginas", True, w=330)
        ad = ep(t, C["28.d"], 0.5)
        expr(c, "8 · x = 240 · 20 = 4800", 600, 705, 36, ad)
        expr(c, "x = 4800 ÷ 8 = 600", 600, 765, 40, ep(t, C["28.e"], 0.4), cores={6: GREEN})
        return
    aa = ep(t, C["29"], 0.4)
    text(c, "ATALHO: VALOR UNITÁRIO", 600, 460, 24, "black", GREEN, aa, tracking=2)
    text(c, "quanto sai em UMA unidade", 600, 500, 26, "bold", INK2, aa)
    expr(c, "240 ÷ 8 = 30", 600, 580, 50, ep(t, C["29.a"], 0.4), cores={4: GREEN})
    text(c, "páginas por minuto", 600, 630, 24, "bold", GRAY, ep(t, C["29.a"], 0.4))
    expr(c, "30 · 20 = 600", 600, 695, 54, ep(t, C["29.b"], 0.4), cores={4: GREEN})
    af = ep(t, C["29.f"], 0.5)
    if af > 0:
        rrect(c, 230, 735, 740, 56, 14, AMBER, 0.12 * af)
        text_mid(c, "20 min = 2,5 × 8 min: nem dobro, nem triplo", 600, 763, 26, "black", INK, af)


# ======================================================================
# Questão 5 do material — você faz
# ======================================================================

def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · VOCÊ FAZ", "PAUSE E TENTE", INV)
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.4)
    _enunciado(c, Q5_TXT, a0)
    cues_in = {L: C[f"30.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["32.xa"], "C": C["32.xc"], "D": C["32.xd"], "E": C["32.xe"]}
    if t >= C["30.qa"] - 0.3:
        K.alternativas(c, t, C, Q5_ALTS, 1080, 230, 640, 36, C["31.ok"], "B", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["30.end"] - 1.9, 580, 600)
    if t < C["31"]:
        return
    ra = ep(t, C["31"], 0.4)
    rrect(c, 170, 400, 860, 405, 18, "#FFFFFF", ra, shadow=True)
    sid = which(t, C, ["31", "32"])
    ativo = 3 if t < C["31.b"] else 5
    passos_h(c, 600, 440, ativo, ra * (1.0 if sid == "31" else 0.5))
    selo_dobro(c, 600, 562, ep(t, C["31.a"], 0.5), "operários", "dias", False, w=440)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        text(c, "inversa: o PRODUTO é constante", 600, 668, 26, "black", INV, ab)
        expr(c, "15 · 24 = 360", 400, 720, 40, ab, cores={4: INV})
        expr(c, "20 · x = 360", 800, 720, 40, ep(t, C["31.c"], 0.4), cores={4: INV})
    expr(c, "x = 360 ÷ 20 = 18", 600, 772, 40, ep(t, C["31.d"], 0.4), cores={6: GREEN})
    ae = ep(t, C["31.e"], 0.5) * (1 - ep(t, C["32"], 0.3))
    if ae > 0:
        rrect(c, 1080, 760, 640, 60, 16, GREEN, 0.14 * ae)
        text_mid(c, "mais operários → menos dias: 18 < 24 ✓", 1400, 790, 26, "black", GREEN, ae)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REGRA DE TRÊS COMPOSTA", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    for k, s in enumerate(["operários", "horas por dia", "dias"]):
        a = aa * ep(t, C["34.a"] + 0.5 * k, 0.4)
        x = 560 + k * 400
        card(c, x - 160, 260, 320, 200, a)
        text(c, s, x, 340, 36, "black", INK, a)
        fmid(c, "?" if k == 2 else "", x, 410, 50, "black", PURPLE, a)
    ab = ep(t, C["34.b"], 0.5)
    chip(c, "a simples, REPETIDA", W / 2, 560, PURPLE, ab, 38)
    ac = ep(t, C["34.c"], 0.5)
    chip(c, "+ um atalho", W / 2, 650, GREEN, ac, 34)
    pill(c, "ep. 4 · regra de três composta", W / 2, 770, PURPLE, size=32, a=ep(t, C["34.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Quantas das 6 situações do treino você acertou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, cotidiano=b_cotidiano, tipos=b_tipos, teste=b_teste,
              junto=b_junto, procedimento=b_procedimento, unidades=b_unidades, treino=b_treino, recap=b_recap, erros=b_erros,
              q4=b_q4, q5=b_q5, ponte=b_ponte, cta=b_cta)
