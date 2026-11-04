"""Visual — Estudativo · Questão de Matemática 012 (aula horizontal 1920x1080): ENEM 2025, questão 138, o combustível descartado.
Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = dado do problema (30.000 L, 10.000, 10.200, 9.900) e o combustível no tanque, ciano = incógnita
(quanto enviar) e a parte proporcional, menta = o que chega / resultado conferido, coral = o descarte e as pegadinhas.
Figura principal: o caminhão-tanque (caminhao()) com o nível do tanque e a gota do descarte (gota())."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_012_matematica_combustivel_descarte.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.e": "shimmer", "02.c": "confirm", "02.e": "shimmer", "03.c": "impact", "03.d": "deny", "04.c": "confirm",
        "05.b": "confirm", "05.c": "alert", "06.c": "impact", "06.d": "confirm", "06.e": "confirm", "07.b": "deny",
        "07.c": "confirm", "07.d": "alert", "08.c": "lock", "10.a": "shimmer", "10.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo (só os efeitos); trilha só nos Shorts

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 012", "QUESTÃO DE MATEMÁTICA · 012"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_ferr=("THE TOOL · FIXED PART × PROPORTIONAL PART", "A FERRAMENTA · PARTE FIXA × PARTE PROPORCIONAL"),
    s_desc=("STEP 1 · HOW MUCH IS DISCARDED", "PASSO 1 · QUANTO É DESCARTADO"), s_fixo=("THE KEY IDEA · THE DISCARD IS FIXED", "A IDEIA · O DESCARTE É FIXO"),
    s_ped=("STEP 2 · THE NEW ORDER", "PASSO 2 · O NOVO PEDIDO"), s_env=("STEP 3 · HOW MUCH TO SEND", "PASSO 3 · QUANTO ENVIAR"),
    s_alt=("CHECKING EVERY OPTION", "CONFERINDO AS ALTERNATIVAS"), s_gen=("THE GENERAL RULE", "A REGRA GERAL"),
    s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 138", "ENEM 2025 · questão 138"),
    tanque=("tanker truck: ", "caminhão-tanque: "), descarte_igual=("same discard on every trip", "descarte: sempre o mesmo"),
    pedido_dados=("ordered 10,000 · sent 10,200 · got 9,900", "pediu 10.000 · enviou 10.200 · chegou 9.900"),
    dobro_pedido=("new order: TWICE as much", "novo pedido: o DOBRO"), minimo=("minimum to send = ", "envio mínimo = "),
    p_fixa=("FIXED PART", "PARTE FIXA"), p_prop=("PROPORTIONAL PART", "PARTE PROPORCIONAL"),
    pizza1=("1 pizza", "1 pizza"), pizza2=("2 pizzas", "2 pizzas"), entrega=("delivery", "entrega"),
    dobra=("proportional: DOUBLES", "proporcional: DOBRA"), fica=("fixed: STAYS THE SAME", "fixa: FICA IGUAL"),
    afim=("varying part + fixed part = linear function", "parte que varia + parte fixa = função afim"),
    chega_eq=("arrives = sent − discard", "chega = enviado − descarte"),
    enviou=("sent", "enviou"), chegou=("arrived", "chegou"), descarte=("discard", "descarte"),
    contou=("they counted 200 extra...", "contaram 200 a mais..."), faltaram=("...so 100 L were missing", "...e faltaram 100 L"),
    nao_dep=("doesn't depend on the amount", "não depende da quantidade"), e_fixa=("discard = FIXED PART", "descarte = PARTE FIXA"),
    como_taxa=("like the pizza delivery fee", "como a taxa de entrega da pizza"),
    mesmo=("same truck = same discard", "mesmo caminhão = mesmo descarte"),
    quer=("how much should arrive?", "quanto deve chegar?"), dobro_enc=("twice what was ORDERED", "o dobro do ENCOMENDADO"),
    nao_env=("2 × 10,200  (sent)", "2 × 10.200  (enviado)"), nao_cheg=("2 × 9,900  (arrived)", "2 × 9.900  (chegou)"),
    pedido=("order", "pedido"),
    env_eq=("send = order + discard", "enviar = pedido + descarte"),
    cabe=("fits in the 30,000 L truck", "cabe no caminhão de 30.000 L"),
    cada_envio=("arrives = sent − 300", "chega = enviado − 300"),
    falta=("short", "falta"), sobra=("extra", "sobra"), exato=("exact", "exato"),
    linha=("20,000 L", "20.000 L"),
    nao_chega=("doesn't arrive", "não chega"), a_mais=("too much", "a mais"),
    regra=("send = order + 300", "enviar = pedido + 300"),
    ex15=("order 15,000 → send 15,300", "pedido 15.000 → envia 15.300"),
    triplo=("what if the order were TRIPLE?", "e se o pedido fosse o TRIPLO?"), um_so=("would one truck do?", "um caminhão só dá conta?"),
    comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["discard: 10,200 − 9,900 = 300 L", "the discard is fixed: it doesn't double", "new order: 2 × 10,000 = 20,000 L",
             "send: 20,000 + 300 = 20,300 L  (C)"],
            ["descarte: 10.200 − 9.900 = 300 L", "o descarte é fixo: não dobra", "novo pedido: 2 × 10.000 = 20.000 L",
             "enviar: 20.000 + 300 = 20.300 L  (C)"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Proportional", "quantities"), ("", "Linear functions"), ("Linear", "equations")],
           [("Grandezas", "proporcionais"), ("", "Função afim"), ("Equações do", "1º grau")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}


def _mil(n):
    """'vinte mil e trezentos' → '20.300' (só milhares com centenas redondas, como os desta questão)"""
    k, r = divmod(n, 1000)
    s = ("" if k == 1 else matematica._extenso_pt(k) + " ") + "mil"
    return s + (" e " + matematica._extenso_pt(r) if r else ""), f"{n:,}".replace(",", ".")


_VALORES = (10000, 10200, 9900, 20000, 20100, 20200, 20300, 20400, 20600, 19800, 19900, 15000, 15300, 30000)
_EXTRA = [] if EN else (
    [("dois mil e vinte e cinco", "2025")]
    + [(f + " litros", d + " L") for f, d in map(_mil, _VALORES)] + [_mil(v) for v in _VALORES]
    + [("trezentos litros", "300 L"), ("cem litros", "100 L"), ("quarenta reais", "R$ 40"), ("seis reais", "R$ 6"),
       ("quarenta e seis reais", "R$ 46"), ("primeiro grau", "1º grau"), ("duas vezes", "2 ×")])
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
matematica.EXPRESSOES |= {("a", "mais"), ("nem", "mais"), ("nem", "menos"), ("é", "menos")}   # "a mais", "é menos que": palavras, não sinais
n_ = lambda s: s.replace(".", "#").replace(",", ".").replace("#", ",") if EN else s   # noqa: E731  troca , e . no inglês


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- figuras
METAL = "#D7E0EE"


def caminhao(c, cx, gy, s, a, nivel, t, cor=AMB, txt=None, txt_col=None):
    """caminhão-tanque de lado: tanque (cápsula) centrado em cx, rodas no chão gy, escala s (s = 1 → ~500 px).
    nivel ∈ [0, 1] = fração do tanque cheia (com ondinha na superfície); txt = número escrito no tanque"""
    if a <= 0:
        return
    c.save(); c.translate(cx, gy); c.scale(s, s)
    tx0, tx1, ty0, ty1 = -260, 90, -230, -70
    tank = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(tx0, ty0, tx1, ty1), 80, 80)
    rrect(c, -270, -64, 510, 18, 6, "#5B6B88", a)                                     # chassi
    cab = skia.Path(); cab.moveTo(108, -60); cab.lineTo(108, -170); cab.lineTo(185, -170); cab.lineTo(235, -112)
    cab.lineTo(240, -60); cab.close()
    c.drawPath(cab, paint(BG2, a)); c.drawPath(cab, paint(METAL, a, stroke=5))
    win = skia.Path(); win.moveTo(126, -150); win.lineTo(180, -150); win.lineTo(214, -112); win.lineTo(126, -112); win.close()
    c.drawPath(win, paint(CYA, 0.45 * a))
    c.drawRRect(tank, paint(BG2, 0.9 * a))
    if nivel > 0:   # combustível
        c.save(); c.clipRRect(tank, True)
        y = ty1 - (ty1 - ty0) * clamp(nivel)
        pth = skia.Path(); pth.moveTo(tx0, ty1)
        for i in range(0, 41):
            x = tx0 + (tx1 - tx0) * i / 40
            pth.lineTo(x, y + 4 * math.sin(x / 26 + t * 3))
        pth.lineTo(tx1, ty1); pth.close()
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([(0, ty0), (0, ty1)], [hexc("#FFD36A"), hexc(cor)]))
        p.setAlphaf(0.9 * a)
        c.drawPath(pth, p)
        c.restore()
    c.drawRRect(tank, paint(METAL, a, stroke=6))
    for x in (-200, -110, 170):   # rodas
        c.drawCircle(x, -30, 32, paint("#1B2236", a)); c.drawCircle(x, -30, 32, paint(METAL, a, stroke=5))
        c.drawCircle(x, -30, 10, paint(METAL, a))
    if txt:
        txt_col = txt_col or (BG0 if nivel > 0.55 else WHITE)   # escuro sobre o combustível, claro sobre o tanque vazio
        glow_text(c, txt, (tx0 + tx1) / 2, (ty0 + ty1) / 2, 50, "black", txt_col, a, glow=0.1)
    c.restore()


def gota(c, x, y, r, a, cor=RED):
    """gota (o combustível descartado): ponta para cima, centro da parte redonda em (x, y)"""
    if a <= 0:
        return
    pth = skia.Path(); pth.addCircle(x, y, r)
    tri_ = skia.Path(); tri_.moveTo(x - r * 0.86, y - r * 0.5); tri_.lineTo(x, y - r * 2.1); tri_.lineTo(x + r * 0.86, y - r * 0.5)
    tri_.close()
    pth = skia.Op(pth, tri_, skia.kUnion_PathOp)
    c.drawPath(pth, blur_paint(cor, 0.45 * a, 8))
    c.drawPath(pth, paint(cor, a))
    c.drawCircle(x - r * 0.35, y - r * 0.2, r * 0.22, paint(WHITE, 0.6 * a))


def descarte(c, cx, gy, s, a, t, t0, txt="−300 L"):
    """gota caindo da válvula do tanque (atrás do caminhão) com o rótulo do descarte; repete a cada 1,6 s a partir de t0"""
    if a <= 0 or t < t0:
        return
    vx, vy = cx - 285 * s, gy - 58 * s   # cano na traseira do chassi
    c.drawLine(vx + 15 * s, vy, vx, vy, paint(METAL, a, stroke=7 * s, cap_round=True))
    c.drawLine(vx, vy, vx, vy + 22 * s, paint(METAL, a, stroke=7 * s, cap_round=True))
    u = ((t - t0) % 1.6) / 1.6
    gota(c, vx, vy + 50 * s + 70 * s * ease_io(u), 18 * s, a * (1 - u * 0.6))
    label(c, txt, vx - 30 * s, vy + 95 * s, a * ep(t, t0, 0.3), 44 * min(1, s * 1.3), RED, "black", "right")


def seta(c, x0, y0, x1, y1, a, col=INK2, w=6):
    if a <= 0:
        return
    c.drawLine(x0, y0, x1, y1, paint(col, a, stroke=w, cap_round=True))
    ang = math.atan2(y1 - y0, x1 - x0)
    pth = skia.Path(); pth.moveTo(x1 + 4 * math.cos(ang), y1 + 4 * math.sin(ang))
    for d in (2.5, -2.5):
        pth.lineTo(x1 - 22 * math.cos(ang + d * 0.2), y1 - 22 * math.sin(ang + d * 0.2))
    pth.close()
    c.drawPath(pth, paint(col, a))


def pizza(c, x, y, r, a, k=1.0):
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    c.drawCircle(0, 0, r, paint("#E9A23B", a))
    c.drawCircle(0, 0, r * 0.84, paint("#F2C14E", a))
    for i, (dx, dy) in enumerate(((-0.4, -0.3), (0.35, -0.35), (0.05, 0.1), (-0.3, 0.42), (0.42, 0.35))):
        c.drawCircle(dx * r, dy * r, r * 0.13, paint(RED, a))
    for i in range(3):
        ang = i * math.pi / 3
        c.drawLine(-r * 0.84 * math.cos(ang), -r * 0.84 * math.sin(ang), r * 0.84 * math.cos(ang), r * 0.84 * math.sin(ang),
                   paint("#B8741A", 0.6 * a, stroke=2.5))
    c.restore()


def _card_enunciado(c, a):
    img = _img_enunciado()
    h = 800
    w = img.width() * h / img.height()
    x, y = LX - w / 2, 545 - h / 2
    rrect(c, x - 18, y - 18, w + 36, h + 36, 22, "#FFFFFF", a)
    c.drawImageRect(img, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), paint(WHITE, a))


@lru_cache(None)
def _img_enunciado():
    from pathlib import Path
    return skia.Image.open(str(Path(__file__).resolve().parent.parent / "enunciado" / "questao.png"))


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_enunciado(c, a)
    board(c, a)
    label(c, L["enem"], RX, 240, a, 40, INK2, "extrabold")
    eq(c, [(L["tanque"], WHITE), (n_("30.000") + " L", AMB)], 330, a, 50)
    label(c, L["descarte_igual"], RX, 420, a * ep(t, tb, 0.3), 40, RED, "black")
    label(c, L["pedido_dados"], RX, 505, a * ep(t, tc, 0.3), 36, AMB, "extrabold")
    label(c, L["dobro_pedido"], RX, 585, a * ep(t, td, 0.3), 40, WHITE, "black")
    eq(c, [(L["minimo"], WHITE), ("?", CYA)], 690, a * ep(t, te, 0.3), 56, box=CYA)
    ke = a * ep(t, te + 2.0, 0.3)
    popill(c, L["p_fixa"], RX, 800, 28, AMB, BG0, ke, t, te + 4.4)
    popill(c, L["p_prop"], RX, 868, 28, CYA, BG0, ke, t, te + 5.2)


def _barra(c, x, y, partes, a, h=56, esc=7.0):
    """barra empilhada: partes = [(valor, cor, texto)], largura = valor · esc"""
    for v, col, s in partes:
        w = v * esc
        rrect(c, x + 3, y - h / 2, w - 6, h, 12, col, a)
        text_mid(c, s, x + w / 2, y, 34, "black", BG0, a)
        x += w
    return x


def b_ferramenta(c, t, C, B):
    ta, tb, tc, td, te = (C[f"02.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ferr"], a)
    # linha 1: uma pizza + entrega; linha 2: duas pizzas + a mesma entrega
    kb = a * ep(t, tb, 0.3)
    x0 = 150
    if kb > 0:
        label(c, L["pizza1"], x0, 300, kb, 36, WHITE, "black", "left")
        pizza(c, x0 + 60, 380, 48, kb, pop(t, tb, 0.4))
        k1 = kb * ep(t, tb + 2.0, 0.3)
        xe = _barra(c, x0 + 140, 380, [(40, CYA, "R$ 40")], k1)
        k2 = kb * ep(t, tb + 3.4, 0.3)
        _barra(c, xe, 380, [(6, AMB, "")], k2)
        label(c, "R$ 6", xe + 21, 440, k2, 30, AMB, "black")
        label(c, "= R$ 46", xe + 130, 380, kb * ep(t, tb + 5.2, 0.3), 40, WHITE, "black")
    kc = a * ep(t, tc, 0.3)
    if kc > 0:
        label(c, L["pizza2"], x0, 560, kc, 36, WHITE, "black", "left")
        pizza(c, x0 + 40, 640, 40, kc, pop(t, tc, 0.4))
        pizza(c, x0 + 95, 655, 40, kc, pop(t, tc + 0.2, 0.4))
        k1 = kc * ep(t, tc + 1.6, 0.3)
        xe = _barra(c, x0 + 160, 650, [(40, CYA, "R$ 40"), (40, CYA, "R$ 40")], k1, esc=6.0)
        k2 = kc * ep(t, tc + 3.0, 0.3)
        _barra(c, xe, 650, [(6, AMB, "")], k2, esc=6.0)
        label(c, "R$ 6", xe + 18, 710, k2, 30, AMB, "black")
        label(c, L["entrega"], xe + 18, 750, k2, 26, INK2, "bold")
    board(c, a)
    eq(c, [("40 + ", WHITE), ("6", AMB), (" = 46", WHITE)], 280, a * ep(t, tb + 5.2, 0.3), 54)
    eq(c, [("80 + ", WHITE), ("6", AMB), (" = ", WHITE), ("86", MNT)], 400, a * ep(t, tc + 4.0, 0.3), 54)
    pos = eq(c, [("92", RED)], 490, a * ep(t, tc + 5.6, 0.3), 46)
    if pos:
        strike(c, pos[0][0] - 10, pos[-1][1] + 10, 490, a, ep(t, tc + 6.0, 0.3))
    label(c, L["dobra"], RX, 590, a * ep(t, td, 0.3), 40, CYA, "black")
    label(c, L["fica"], RX, 660, a * ep(t, td + 2.2, 0.3), 40, AMB, "black")
    eq(c, [("total = 40 · ", WHITE), ("n", CYA), (" + ", WHITE), ("6", AMB)], 780, a * ep(t, te, 0.3), 56, box=CYA)
    label(c, L["afim"], RX, 868, a * ep(t, te + 1.8, 0.3), 30, INK2, "bold")


def b_descarte(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_desc"], a)
    # o caminhão sai com 10.200; a gota leva 300; chegam 9.900 no posto
    cx, gy = 560, 560
    caminhao(c, cx, gy, 0.95, a, 0.34, t, txt=n_("10.200"))
    label(c, L["enviou"], cx - 80, gy - 270, a * ep(t, tb, 0.3), 34, AMB, "extrabold")
    descarte(c, cx, gy, 0.95, a * ep(t, tb + 1.0, 0.3), t, tb + 1.0)
    km = a * ep(t, tb + 2.0, 0.3)
    seta(c, cx, gy + 20, cx, gy + 140, km)
    eq(c, [(L["chegou"] + ": ", WHITE), (n_("9.900") + " L", MNT)], gy + 200, km, 48, cx=cx, maxw=700)
    board(c, a)
    label(c, L["chega_eq"], RX, 280, a * ep(t, tb, 0.3), 42, WHITE, "black")
    eq(c, [(n_("10.200"), AMB), (" − ", WHITE), (n_("9.900"), AMB), (" = ", WHITE)], 420, a * ep(t, tc + 2.2, 0.3), 60)
    eq(c, [(L["descarte"] + " = ", WHITE), ("300 L", RED)], 540, a * ep(t, tc + 5.0, 0.3), 66, box=RED)
    label(c, L["contou"], RX, 690, a * ep(t, td + 0.8, 0.3), 38, INK2, "bold")
    label(c, L["faltaram"], RX, 770, a * ep(t, td + 3.4, 0.3), 42, RED, "black")


def b_fixo(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_fixo"], a)
    # dois caminhões: 10.000 e 20.000 L; os dois perdem os mesmos 300 L
    kc = a * ep(t, tc, 0.4)
    cx = 600
    caminhao(c, cx, 480, 0.78, a, 0.33, t, txt=n_("10.000"))
    descarte(c, cx, 480, 0.78, kc, t, tc + 0.3)
    k2 = a * ep(t, tc + 1.4, 0.4)
    caminhao(c, cx, 870, 0.78, k2, 0.67, t, txt=n_("20.000"))
    descarte(c, cx, 870, 0.78, k2 * kc, t, tc + 1.9)
    board(c, a)
    label(c, L["nao_dep"], RX, 270, a * ep(t, ta + 1.5, 0.3), 40, WHITE, "black")
    eq(c, [(L["e_fixa"], AMB)], 380, a * ep(t, tb, 0.3), 54, box=AMB)
    label(c, L["como_taxa"], RX, 470, a * ep(t, tb + 2.0, 0.3), 34, INK2, "bold")
    eq(c, [(n_("10.000") + " L → ", WHITE), ("−300", RED)], 580, a * ep(t, tc + 0.3, 0.3), 50)
    eq(c, [(n_("20.000") + " L → ", WHITE), ("−300", RED)], 670, a * ep(t, tc + 1.9, 0.3), 50)
    label(c, L["mesmo"], RX, 800, a * ep(t, td + 1.0, 0.3), 40, MNT, "black")


def b_pedido(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ped"], a)
    # dois blocos de 10.000 viram 20.000
    kb = a * ep(t, tb + 2.0, 0.3)
    junta = ease_io(prog(t, tb + 4.4, 0.8))
    y = 470
    for i in range(2):
        k = kb * ep(t, tb + 2.0 + i * 0.6, 0.3)
        x = 160 + i * (380 - 20 * junta)
        rrect(c, x, y - 70, 360, 140, 22, AMB, k * 0.9)
        text_mid(c, n_("10.000") + " L", x + 180, y, 50, "black", BG0, k)
    label(c, L["pedido"] + " × 2", LX, y - 130, kb, 36, INK2, "bold")
    kj = a * ep(t, tb + 4.6, 0.3)
    seta(c, LX, y + 100, LX, y + 190, kj)
    eq(c, [(n_("20.000") + " L", MNT)], y + 260, kj, 76, cx=LX, maxw=700)
    board(c, a)
    label(c, L["quer"], RX, 270, a * ep(t, ta + 0.6, 0.3), 44, WHITE, "black")
    label(c, L["dobro_enc"], RX, 370, a * ep(t, tb, 0.3), 40, AMB, "black")
    eq(c, [("2 × " + n_("10.000") + " = ", WHITE), (n_("20.000") + " L", MNT)], 490, a * ep(t, tb + 4.4, 0.3), 58, box=MNT)
    for i, (s, dt) in enumerate(((L["nao_env"], 1.0), (L["nao_cheg"], 2.4))):
        y2 = 640 + i * 90
        k = a * ep(t, tc + dt, 0.3)
        pos = eq(c, [(s, RED)], y2, k, 40)
        if pos:
            strike(c, pos[0][0] - 8, pos[-1][1] + 8, y2, a, ep(t, tc + dt + 0.5, 0.3))
    check(c, BX1 - 60, 490, 24, a * ep(t, tc + 4.4, 0.2))


def b_envio(c, t, C, B):
    ta, tb, tc, td, te = (C[f"06.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_env"], a)
    cx, gy = 560, 640
    # enche até 20.000, depois +300; régua da capacidade (30.000)
    n = ep(t, tb + 1.0, 1.2) * (20000 / 30000) + ep(t, tb + 3.6, 0.6) * (300 / 30000)
    txt = n_("20.300") if t >= tc + 2.0 else n_("20.000")
    caminhao(c, cx, gy, 1.05, a, n, t, txt=txt if n > 0.1 else None)
    kd = a * ep(t, td, 0.3)
    if kd > 0:   # régua do tanque: 0, 20.300, 30.000
        x = cx - 300 * 1.05
        y0, y1 = gy - 70 * 1.05, gy - 230 * 1.05
        c.drawLine(x, y0, x, y1, paint(WHITE, kd, stroke=4))
        for f, s, col in ((0, "0", INK2), (20300 / 30000, n_("20.300"), CYA), (1, n_("30.000"), AMB)):
            yy = y0 + (y1 - y0) * f
            c.drawLine(x - 12, yy, x + 12, yy, paint(col, kd, stroke=4))
            label(c, s, x - 24, yy, kd, 30, col, "black", "right")
    descarte(c, cx, gy, 1.05, a * ep(t, tb + 3.6, 0.3), t, tb + 3.6)
    board(c, a)
    label(c, L["env_eq"], RX, 260, a * ep(t, tb, 0.3), 42, WHITE, "black")
    eq(c, [(n_("20.000"), MNT), (" + ", WHITE), ("300", RED), (" = ", WHITE), (n_("20.300") + " L", CYA)], 380,
       a * ep(t, tc + 0.4, 0.3), 60, box=CYA)
    eq(c, [(n_("20.300") + " < " + n_("30.000"), WHITE)], 510, kd * ep(t, td + 1.2, 0.3), 50)
    label(c, L["cabe"], RX, 590, kd * ep(t, td + 1.6, 0.3), 34, MNT, "bold")
    check(c, BX1 - 90, 510, 24, kd * ep(t, td + 2.0, 0.2))
    ops = [("A", "20.100"), ("B", "20.200"), ("C", "20.300"), ("D", "20.400"), ("E", "20.600")]
    ke = a * ep(t, te, 0.3)
    for i, (le, v) in enumerate(ops):
        x = BX0 + 100 + i * 175
        ok = le == "C"
        k = ke * ep(t, te + i * 0.08, 0.2)
        text_mid(c, le, x, 730, 38, "black", MNT if ok else INK2, k)
        text_mid(c, n_(v), x, 790, 36, "black", WHITE if ok else INK2, k)
    kk = ke * ep(t, te + 0.6, 0.3)
    if kk > 0:   # moldura na alternativa certa
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX0 + 100 + 2 * 175 - 80, 690, 160, 140), 16, 16)
        c.drawRRect(r, paint(MNT, kk, stroke=4))


def b_alternativas(c, t, C, B):
    ta, tb, tc, td = (C[f"07.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_alt"], a)
    # quanto falta ou sobra em relação aos 20.000 L (barras para baixo = falta, para cima = sobra)
    alts = [("A", 20100, tb), ("B", 20200, tb + 2.6), ("C", 20300, tc), ("D", 20400, td), ("E", 20600, td + 0.3)]
    y0, esc = 560, 0.9
    kl = a * ep(t, ta + 0.6, 0.3)
    c.drawLine(110, y0, 900, y0, paint(MNT, kl, stroke=4))
    label(c, L["linha"], 110, y0 - 30, kl, 30, MNT, "black", "left")
    for i, (le, v, t0) in enumerate(alts):
        x = 230 + i * 150
        dif = v - 300 - 20000
        k = a * ep(t, t0, 0.3)
        if k <= 0:
            continue
        h = dif * esc * ep(t, t0, 0.6)
        col = RED if dif < 0 else (MNT if dif == 0 else AMB)
        if dif:
            top, bot = (y0 - h, y0) if h > 0 else (y0, y0 - h)
            rrect(c, x - 45, top, 90, bot - top, 12, col, 0.9 * k)
            s = ("+" if dif > 0 else "−") + str(abs(dif))
            label(c, s, x, (y0 - h - 30) if h > 0 else (y0 - h + 34), k, 32, col, "black")
        else:
            c.drawCircle(x, y0, 18, paint(MNT, k))
            label(c, L["exato"], x, y0 - 44, k, 30, MNT, "black")
        text_mid(c, le, x, 900, 46, "black", col, k)
    board(c, a)
    label(c, L["cada_envio"], RX, 250, a * ep(t, ta + 0.6, 0.3), 40, WHITE, "black")
    for i, (le, v, t0) in enumerate(alts):
        y = 360 + i * 105
        k = a * ep(t, t0, 0.3)
        chega = v - 300
        col = RED if chega < 20000 else (MNT if chega == 20000 else AMB)
        eq(c, [(le + "   ", col), (n_(f"{v:,}".replace(",", ".")) + " − 300 = ", WHITE),
               (n_(f"{chega:,}".replace(",", ".")), col)], y, k, 46, cx=RX - 40)
        if chega < 20000:
            cross(c, BX1 - 60, y, 20, a * ep(t, t0 + 1.2, 0.2))
        elif chega == 20000:
            check(c, BX1 - 60, y, 22, a * ep(t, t0 + 1.0, 0.2))
        else:
            label(c, L["a_mais"], BX1 - 75, y, a * ep(t, td + 3.0, 0.3), 30, AMB, "black")


def b_generaliza(c, t, C, B):
    ta, tb, tc = (C[f"08.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gen"], a)
    ka = a * (1 - ep(t, tc, 0.3))
    cx, gy = 560, 640
    nv = 15300 / 30000 if t >= tb else 20300 / 30000
    caminhao(c, cx, gy, 1.0, ka, nv, t, txt=n_("15.300") if t >= tb else None)
    descarte(c, cx, gy, 1.0, ka, t, ta)
    kc = a * ep(t, tc, 0.3)
    if kc > 0:   # o desafio: o tanque cheio até a boca e o "?"
        caminhao(c, cx, gy, 1.0, kc, 1.0, t)
        glow_text(c, "?", cx - 85, gy - 110, 130, "black", CYA, kc * ep(t, tc + 2.0, 0.3), glow=0.12)
        popill(c, L["triplo"], LX, 260, 32, AMB, BG0, kc, t, tc + 0.6)
        label(c, L["um_so"], LX, 330, kc * ep(t, tc + 3.0, 0.3), 34, WHITE, "black")
    board(c, a)
    eq(c, [(L["regra"], CYA)], 300, a * ep(t, ta + 1.4, 0.3), 54, box=CYA)
    label(c, L["ex15"], RX, 430, a * ep(t, tb + 1.0, 0.3), 40, WHITE, "black")
    eq(c, [("3 × " + n_("10.000") + " = ?", AMB)], 600, kc * ep(t, tc + 1.6, 0.3), 54)
    eq(c, [(n_("30.000") + " L", AMB), (" = " + L["tanque"].strip(" :"), INK2)], 700, kc * ep(t, tc + 3.4, 0.3), 36)
    label(c, L["comenta"], RX, 840, kc * ep(t, tc + 5.0, 0.3), 38, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"09.{k}"] for k in "bcde"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resumo"], a)
    for i, (s, t0) in enumerate(zip(L["passos"], ks)):
        y = 280 + i * 160
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        x = 330
        c.drawCircle(x, y, 34, paint(AMB, ki))
        text_mid(c, str(i + 1), x, y, 38, "black", BG0, ki)
        text_mid(c, s, x + 70, y, 52, "black", WHITE, ki, align="left")
        check(c, 1640, y, 24, ki * ep(t, t0 + 0.5, 0.2))


def _icone(c, i, cx, cy, a, t):
    """miniatura de cada aula: barras que dobram · reta com a parte fixa · equação"""
    if i == 0:
        for j, (h, col) in enumerate(((50, CYA), (100, CYA))):
            rrect(c, cx - 70 + j * 90, cy + 50 - h, 60, h, 8, col, a)
        label(c, "× 2", cx + 100, cy - 30, a, 32, CYA, "black")
    elif i == 1:
        c.drawLine(cx - 90, cy + 60, cx + 90, cy + 60, paint(INK2, a, stroke=3))
        c.drawLine(cx - 90, cy + 60, cx - 90, cy - 70, paint(INK2, a, stroke=3))
        c.drawLine(cx - 90, cy + 20, cx + 90, cy - 60, paint(CYA, a, stroke=6, cap_round=True))
        c.drawCircle(cx - 90, cy + 20, 9, paint(AMB, a))
    else:
        eq(c, [("x", CYA), (" + 300 = " + n_("20.300"), WHITE)], cy, a, 36, cx=cx, maxw=380)


def b_aulas(c, t, C, B):
    """convite para as aulas do assunto no canal (toda questão termina assim) + CTA"""
    ta, tb, tc, td, te, tf = (C[f"10.{k}"] for k in "abcdef")
    a = fade(t, B["start"], B["end"], d_out=0.01)
    ka = a * (1 - ep(t, tf, 0.4))
    header(c, L["s_aulas"], ka)
    cores = (CYA, AMB, MNT)
    for i, (t0, (l1, l2)) in enumerate(zip((tb, tc, td), L["aulas"])):
        k = ka * pop(t, t0, 0.4)
        if k <= 0:
            continue
        x, w = 180 + i * 560, 480
        cx = x + w / 2
        c.save(); c.translate(cx, 520); c.scale(k, k); c.translate(-cx, -520)
        kk = min(1, ka)
        cartao(c, x, 260, w, 520, kk, cores[i], L["aula"])
        _icone(c, i, cx, 420, kk, t)
        if l1:
            text_mid(c, l1, cx, 610, 50, "black", WHITE, kk)
        text_mid(c, l2, cx, 674 if l1 else 640, 50, "black", cores[i], kk)
        c.restore()
    label(c, L["no_canal"], 960, 870, ka * ep(t, te, 0.3), 40, AMB, "extrabold")
    kg = a * ep(t, tf, 0.4)
    if kg > 0:
        glow_text(c, L["canal"], 960, 400, 120, "black", WHITE, kg, glow=0.12)
        w = text_w(L["canal"], "black", 120)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(960 - w / 2, 430, w * ep(t, tf + 0.3, 0.6), 14), 7, 7), paint(AMB, kg))
        pulse = 1 + 0.03 * math.sin(t * 5)
        c.save(); c.translate(960, 560); c.scale(pulse, pulse)
        pill(c, L["inscreva"], 0, 0, 38, CYA, BG0, kg * ep(t, tf + 0.8, 0.3))
        c.restore()
        caminhao(c, 990, 900, 0.55, kg * ep(t, tf + 1.2, 0.4), 0.68, t)


BLOCKS = dict(gancho=b_gancho, ferramenta=b_ferramenta, descarte=b_descarte, fixo=b_fixo, pedido=b_pedido, envio=b_envio,
              alternativas=b_alternativas, generaliza=b_generaliza, resumo=b_resumo, aulas=b_aulas)
