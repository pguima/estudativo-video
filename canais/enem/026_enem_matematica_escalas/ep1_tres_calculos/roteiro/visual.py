"""Visual — Escalas, Plantas e Mapas, Episódio 1: o que é escala, os três cálculos e a cadeia até o quilômetro (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: mapa() (folha de mapa com estrada, rio e duas cidades), cadeia() (escada cm → m → km, cada degrau
acendendo), tesoura() e corte() (a tesoura cortando os 5 zeros do denominador), vnum() (a vírgula andando), linha().
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
_s = importlib.util.spec_from_file_location("comum026", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_escalas_ep1_tres_calculos.mp4"
CARD_R = K.CARD_R
DEGRAU = K.DEGRAU
PAPEL = K.PAPEL
TERRA = "#E6EFD9"
TERRA2 = "#D5E4C2"
RIO = "#9CC3EE"
ESTRADA = "#C9A46A"


def num(v):
    """número com espaço de milhar: 3000000 -> '3 000 000'; aceita float com vírgula decimal"""
    if isinstance(v, float) and not v.is_integer():
        s = f"{v:.1f}".replace(".", ",")
        return s
    return f"{int(round(v)):,}".replace(",", " ")


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def mapa(c, x, y, w, h, a, cidades=True, nomes=True):
    """folha de mapa estilizada: terra, rio, estrada e duas cidades (A à esquerda, B à direita)"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, TERRA, a, shadow=True)
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y, w, h))
    for k in range(5):
        cx_, cy_ = x + w * (0.15 + 0.2 * k), y + h * (0.25 if k % 2 else 0.75)
        c.drawCircle(cx_, cy_, h * 0.22, paint(TERRA2, a))
    p = skia.Path(); p.moveTo(x + w * 0.55, y - 10)
    p.cubicTo(x + w * 0.45, y + h * 0.35, x + w * 0.7, y + h * 0.6, x + w * 0.58, y + h + 10)
    c.drawPath(p, paint(RIO, a, stroke=max(4, h * 0.05), cap_round=True))
    ya = y + h * 0.55
    p2 = skia.Path(); p2.moveTo(x + w * 0.12, ya)
    p2.cubicTo(x + w * 0.35, ya - h * 0.18, x + w * 0.65, ya + h * 0.18, x + w * 0.88, ya)
    c.drawPath(p2, paint(ESTRADA, a, stroke=max(3, h * 0.03), cap_round=True))
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), paint("#B9C7A6", a, stroke=3))
    if cidades:
        r = max(6, h * 0.035)
        for k, (fx, nm) in enumerate(((0.12, "A"), (0.88, "B"))):
            cx_ = x + w * fx
            c.drawCircle(cx_, ya, r + 3, paint("#FFFFFF", a))
            c.drawCircle(cx_, ya, r, paint(RED, a))
            if nomes:
                text(c, "cidade " + nm, cx_, ya - r - 14, max(16, h * 0.07), "black", INK2, a)


def cadeia(c, x0, y0, a, acesos=(1, 1, 1), setas=(1, 1), valores=("", "", ""), sw=330, sh=90, alt=170, size=56,
           vsize=34, cor=PURPLE):
    """a escada cm → m → km (subindo para a direita); cada degrau acende (acesos) e cada seta mostra ÷ 100, ÷ 1 000"""
    if a <= 0:
        return
    unid = ["cm", "m", "km"]
    floor = y0 + alt
    for i in range(3):
        x, y = x0 + i * sw, y0 - i * sh
        ai = acesos[i]
        rrect(c, x + 6, y, sw - 12, floor - y, 16, DEGRAU, a, shadow=True)
        if ai > 0:
            rrect(c, x + 6, y, sw - 12, floor - y, 16, mix(DEGRAU, cor, 0.22), a * ai)
            rrect(c, x + 6, y, sw - 12, 12, 6, cor, a * ai)
        text_mid(c, unid[i], x + sw / 2, y + 58, size, "black", cor if ai > 0.5 else GRAY, a)
        if valores[i]:
            text_mid(c, valores[i], x + sw / 2, y + 128, vsize, "black", INK, a * ai)
    for i, lbl in enumerate(("÷ 100", "÷ 1 000")):
        sa = a * setas[i]
        if sa <= 0:
            continue
        x1, y1 = x0 + i * sw + sw * 0.62, y0 - i * sh - 14
        x2, y2 = x0 + (i + 1) * sw + sw * 0.36, y0 - (i + 1) * sh - 14
        top = min(y1, y2) - 60
        p = skia.Path(); p.moveTo(x1, y1); p.quadTo((x1 + x2) / 2, top, x2, y2)
        c.drawPath(p, paint(AMBER, sa, stroke=5, cap_round=True))
        ang = math.atan2(y2 - top, x2 - (x1 + x2) / 2)
        for s_ in (-1, 1):
            c.drawLine(x2, y2, x2 - 18 * math.cos(ang + s_ * 0.5), y2 - 18 * math.sin(ang + s_ * 0.5),
                       paint(AMBER, sa, stroke=5, cap_round=True))
        rrect(c, (x1 + x2) / 2 - 72, top - 30, 144, 50, 25, "#FFFFFF", sa, shadow=True)
        text_mid(c, lbl, (x1 + x2) / 2, top - 5, 28, "black", AMBER, sa)


def tesoura(c, cx, cy, s, a, abre=0.5, col=None):
    """tesoura com a ponta para a ESQUERDA; abre = 0 (fechada) a 1 (aberta)"""
    if a <= 0:
        return
    col = col or GREEN
    ang = 6 + 16 * clamp(abre)
    for sg in (-1, 1):
        c.save(); c.translate(cx, cy); c.rotate(sg * ang)
        p = skia.Path()
        p.moveTo(0, -s * 0.07); p.quadTo(-s * 0.55, -s * 0.09, -s * 0.95, 0); p.quadTo(-s * 0.55, s * 0.03, 0, s * 0.05)
        p.close()
        c.drawPath(p, paint("#C9CED6", a))
        c.drawPath(p, paint("#7D8590", a, stroke=2))
        c.drawCircle(s * 0.42, sg * s * 0.10, s * 0.17, paint(col, a, stroke=s * 0.07))
        line(c, 0, 0, s * 0.27, sg * s * 0.07, col, a, s * 0.07)
        c.restore()
    c.drawCircle(cx, cy, s * 0.05, paint(INK, a))


def corte(c, digitos, cx, cy, size, a, u, ncorte=5):
    """denominador (ex.: '500000') com os últimos zeros (até ncorte) cortados pela tesoura conforme u (0 → 1).
    no fim, o que sobrou se junta à esquerda; u de 1 → 0 faz os zeros VOLTAREM. Devolve o x do fim do que sobrou."""
    if a <= 0:
        return cx
    n = len(digitos)
    nz = 0
    while nz < min(ncorte, n - 1) and digitos[n - 1 - nz] == "0":
        nz += 1
    chars = []
    for i, d in enumerate(digitos):
        if i > 0 and (n - i) % 3 == 0:
            chars.append((" ", None))
        chars.append((d, i))
    dw = text_w("0", "black", size) * 1.02
    sp = dw * 0.4
    tw = sum(dw if i is not None else sp for _, i in chars)
    x = cx - tw / 2
    xs = []
    for ch, i in chars:
        w_ = dw if i is not None else sp
        xs.append((ch, i, x + w_ / 2))
        x += w_
    cut0 = n - nz                        # índice do 1º zero cortado
    x_right = xs[-1][2] + dw * 0.9
    x_left = next(xx for ch, i, xx in xs if i == cut0) - dw * 1.4
    uu = clamp(u / 0.8)                  # a tesoura passa em 80% do tempo; depois o que sobrou se junta
    xt = lerp(x_right, x_left, uu)
    m = ease_io(clamp((u - 0.8) / 0.2))
    resto = [(ch, i, xx) for ch, i, xx in xs if i is not None and i < cut0]
    x_ini = xs[0][2]
    fim = cx
    for j, (ch, i, xx) in enumerate(resto):
        xf = lerp(xx, x_ini + j * dw, m)
        fmid(c, ch, xf, cy, size, "black", INK, a)
        fim = xf + dw / 2
    for ch, i, xx in xs:
        if i is None or i < cut0:
            continue
        k = clamp((xx - xt) / (dw * 0.6)) if xt < xx else 0.0
        fall = ease_io(k)
        fmid(c, ch, xx, cy + fall * size * 1.1, size, "black", mix(INK, RED, min(1, k * 3)), a * (1 - fall))
    if 0 < uu < 1:
        ab = abs(math.sin(uu * math.pi * 2 * max(1, nz)))
        tesoura(c, xt + size * 0.75, cy, size * 1.3, a * ep(uu, 0, 0.08) * (1 - prog(uu, 0.92, 0.08)), ab)
    return fim


def vnum(c, digitos, p0, s, cx, cy, size, a, col=None, zero_col=None):
    """número sem vírgula (ex.: '3') com a vírgula depois de p0 algarismos; s = casas andadas
    (positivo = para a DIREITA, multiplica; negativo = para a ESQUERDA, divide). Zeros aparecem conforme a vírgula passa."""
    if a <= 0:
        return
    col = col or INK
    zero_col = zero_col or GRAY
    n = len(digitos)
    p = p0 + s
    rp = max(0, math.ceil(p - n - 1e-9))
    lp = max(0, math.ceil(1 - p - 1e-9))
    ds = "0" * lp + digitos + "0" * rp
    dw = text_w("0", "black", size) * 1.02
    x0 = cx - len(ds) * dw / 2
    for i, d in enumerate(ds):
        if i < lp:
            fade = a * clamp((1 - p) - (lp - i - 1))
            cc = zero_col
        elif i >= lp + n:
            fade = a * clamp(p - n - (i - lp - n))
            cc = zero_col
        else:
            fade, cc = a, col
        fmid(c, d, x0 + dw * (i + 0.5), cy, size, "black", cc, fade)
    ci = p + lp
    xv = x0 + dw * ci
    jump = abs(math.sin(math.pi * (abs(s) % 1))) * size * 0.35
    va = a * clamp(len(ds) - ci + 0.05)
    fmid(c, ",", xv, cy + size * 0.18 - jump, size, "black", RED, va)


def carrinho(c, cx, cy, s, a, col=BLUE):
    if a <= 0:
        return
    rrect(c, cx - s, cy - s * 0.25, 2 * s, s * 0.5, s * 0.18, col, a)
    rrect(c, cx - s * 0.55, cy - s * 0.62, s * 1.0, s * 0.45, s * 0.18, col, a)
    rrect(c, cx - s * 0.42, cy - s * 0.54, s * 0.36, s * 0.3, s * 0.06, "#DCE6FF", a)
    rrect(c, cx + 0.02 * s, cy - s * 0.54, s * 0.36, s * 0.3, s * 0.06, "#DCE6FF", a)
    for fx in (-0.55, 0.55):
        c.drawCircle(cx + fx * s, cy + s * 0.27, s * 0.22, paint(INK, a))
        c.drawCircle(cx + fx * s, cy + s * 0.27, s * 0.09, paint("#C9CED6", a))


def planta(c, x, y, w, h, a):
    """planta baixa mínima: contorno e três cômodos"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 6, PAPEL, a, shadow=True)
    st = paint(INK2, a, stroke=5)
    c.drawRect(skia.Rect.MakeXYWH(x + 14, y + 14, w - 28, h - 28), st)
    c.drawLine(x + w * 0.55, y + 14, x + w * 0.55, y + h - 14, st)
    c.drawLine(x + w * 0.55, y + h * 0.5, x + w - 14, y + h * 0.5, st)
    text_mid(c, "sala", x + w * 0.3, y + h / 2, 22, "bold", GRAY, a)
    text_mid(c, "quarto", x + w * 0.77, y + h * 0.3, 18, "bold", GRAY, a)
    text_mid(c, "cozinha", x + w * 0.77, y + h * 0.72, 18, "bold", GRAY, a)


def objeto(c, x, y, w, h, tit, sub, a, col=BLUE):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 60, 24, col, a * 0.14)
    text(c, tit, x + w / 2, y + 42, 28, "black", col, a)
    text(c, sub, x + w / 2, y + h - 30, 30, "black", INK, a)


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    """faixa com a pergunta do bloco"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "ESCALAS, PLANTAS E MAPAS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 240, 1460, 130, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("6 cm × 500 000 = ", INK), ("3 000 000 cm", GREEN)], W / 2, 305, 64, aa)
        conferido(c, "fácil", 1520, 320, ep(t, C["01.a"] + 1.2, 0.4), True, 34)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        cadeia(c, 300, 650, ab, (1, ep(t, C["01.b"] + 1.0, 0.4), ep(t, C["01.b"] + 2.0, 0.4)),
               (ep(t, C["01.b"] + 0.6, 0.4), ep(t, C["01.b"] + 1.6, 0.4)), sw=250, sh=70, alt=140, size=46)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        pill(c, "pulou o ÷ 100  →  erro de × 100", 1160, 500, RED, size=28, a=acc)
        pill(c, "pulou o ÷ 1 000  →  erro de × 1 000", 1160, 580, RED, size=28, a=ep(t, C["01.c"] + 1.4, 0.4))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1420, 730, ad, "A ALTERNATIVA ERRADA ESTÁ LÁ", AMBER, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "resolver os 3 tipos de questão de escala", "achar o real · achar o desenho · achar a escala"),
            ("02.b", "chegar ao quilômetro sem pular degrau", "cm  →  m  →  km")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "RAZÃO = comparação por DIVISÃO", 560, 290, 34, "black", BLUE, aa)
        text(c, "série de Razão", 560, 340, 26, "bold", GRAY, aa)
        fr(c, "2", "5", 460, 470, 90, INK, aa)
        text_mid(c, "= 2 ÷ 5", 650, 480, 64, "black", INK, ep(t, C["03.a"] + 2.5, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "A ESCADA (série de Unidades)", 1370, 290, 30, "black", PURPLE, ab)
        cadeia(c, 1040, 520, ab, (1, ep(t, C["03.b"] + 2.0, 0.4), ep(t, C["03.b"] + 3.6, 0.4)),
               (ep(t, C["03.b"] + 1.6, 0.4), ep(t, C["03.b"] + 3.2, 0.4)), sw=220, sh=60, alt=130, size=42)
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS OBJETOS", "O QUE ELES TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    a1 = ep(t, C["04.a"], 0.5)
    objeto(c, 220, 230, 460, 420, "MAPA RODOVIÁRIO", "centenas de km num palmo", a1)
    mapa(c, 260, 310, 380, 220, a1)
    a2 = ep(t, C["04.b"], 0.5)
    objeto(c, 730, 230, 460, 420, "PLANTA DO APÊ", "a sala em poucos cm", a2)
    planta(c, 800, 310, 320, 230, a2)
    a3 = ep(t, C["04.c"], 0.5)
    objeto(c, 1240, 230, 460, 420, "MINIATURA", "escala 1 : 43", a3)
    carrinho(c, 1470, 450, 120, a3)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "uma FOTO ENCOLHIDA do mundo", W / 2, 745, ad, 40, BLUE)


# ======================================================================
# blocos a, b, c — definição, leitura, ampliação
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("05", "O QUE É ESCALA", "DESENHO SOBRE REAL", BLUE), ("06", "A CONDIÇÃO", "MESMA UNIDADE", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        text(c, "ESCALA", W / 2, 290, 64, "black", BLUE, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            text_mid(c, "E  =", 760, 470, 80, "black", INK, ab)
            fr(c, "desenho", "real", 1010, 460, 72, INK, ab, num_col=BLUE, den_col=GREEN)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            rrect(c, 260, 610, 660, 120, 20, mix("#FFFFFF", BLUE, 0.08), acc)
            text(c, "DESENHO = medida no papel", 590, 662, 32, "black", BLUE, acc)
            text(c, "a que você mede com a régua", 590, 704, 26, "bold", GRAY, acc)
            a2 = ep(t, C["05.c"] + 2.4, 0.4)
            rrect(c, 1000, 610, 660, 120, 20, mix("#FFFFFF", GREEN, 0.08), a2)
            text(c, "REAL = medida do mundo", 1330, 662, 32, "black", GREEN, a2)
            text(c, "a que existe de verdade", 1330, 704, 26, "bold", GRAY, a2)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            text_mid(c, "=  desenho ÷ real", 1440, 470, 44, "black", PURPLE, ad)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        text(c, "as duas na MESMA unidade", W / 2, 280, 40, "black", PURPLE, aa)
        cx = 760
        n_, d_ = "1 cm", "250 000 cm"
        fr(c, n_, d_, cx, 450, 76, INK, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            for s_, yy in ((n_, 450 - 76 * 0.16), (d_, 450 + 76 * 0.98)):
                w_ = ftext_w(s_, "black", 76)
                wc = ftext_w("cm", "black", 76)
                xe = cx + w_ / 2
                strike(c, xe - wc - 6, yy - 18, xe + 6, yy - 46, ab, RED, ab)
            text_mid(c, "=", 1180, 470, 76, "black", INK, ab)
            text_mid(c, "1 : 250 000", 1450, 470, 76, "black", BLUE, ab)
            pill(c, "NÚMERO PURO: sem unidade", 1450, 580, BLUE, size=28, a=ep(t, C["06.b"] + 2.0, 0.4), anchor="center")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        regra(c, "a escala não tem cm, nem km: é só  1 : 250 000", W / 2, 730, acc, 34)


def b_ler(c, t, C, B):
    head(c, t, B["start"], "COMO SE LÊ", "1 : 250 000", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.5)
    hl = ep(t, C["07.a"], 0.5)
    if a0 > 0:
        linha(c, [("1 : ", INK), ("250 000", mix(INK, BLUE, hl))], W / 2, 290, 96, a0)
    if hl > 0:
        x1 = W / 2 - text_w("1 : 250 000", "black", 96) / 2 + text_w("1 : ", "black", 96)
        x2 = W / 2 + text_w("1 : 250 000", "black", 96) / 2
        line(c, x1, 350, x2, 350, BLUE, hl, 6)
        text(c, "DENOMINADOR: o número de baixo (depois dos dois-pontos)", (x1 + x2) / 2, 400, 26, "black", BLUE, hl)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 460, 160, 160, 10, PAPEL, ab, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(300, 500, 80, 80), paint(BLUE, ab, stroke=4))
        text(c, "1 cm", 340, 660, 34, "black", BLUE, ab)
        text(c, "no papel", 340, 700, 26, "bold", GRAY, ab)
        g = ep(t, C["07.b"] + 1.0, 1.4)
        arrow(c, 450, 540, 450 + 200 * g, 540, AMBER, ab, 6, 18)
        rrect(c, 700, 500, 960 * g, 80, 10, mix("#FFFFFF", GREEN, 0.22), ab)
        c.drawRect(skia.Rect.MakeXYWH(700, 500, 960 * g, 80), paint(GREEN, ab, stroke=4))
        text(c, "250 000 cm no terreno", 1180, 660, 34, "black", GREEN, ab * g)
        text(c, "= 2,5 km", 1180, 700, 26, "bold", GRAY, ab * g)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        pill(c, "cada 1 cm do papel GUARDA 250 000 cm do mundo", W / 2, 775, BLUE, size=30, a=acc, anchor="center")


def b_ampliacao(c, t, C, B):
    head(c, t, B["start"], "A ESCALA SEMPRE ENCOLHE?", "REDUÇÃO · AMPLIAÇÃO", BLUE)
    card(c, *CARD_R)
    cols = [("08.a", "REDUÇÃO", "1 : 500 000", "desenho MENOR que o real", "mapas e plantas", 40, 150, GREEN),
            ("08.b", "AMPLIAÇÃO", "10 : 1", "desenho MAIOR que o real", "peças pequenininhas", 150, 15, AMBER),
            ("08.c", "TAMANHO NATURAL", "1 : 1", "desenho = real", "", 80, 80, PURPLE)]
    for k, (cue, tit, esc, sub, ex_, rd, rr, col) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 220 + k * 510
        rrect(c, x, 240, 460, 460, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x, 240, 460, 60, 24, col, a * 0.14)
        text(c, tit, x + 230, 282, 28, "black", col, a)
        text(c, esc, x + 230, 370, 56, "black", INK, a)
        # desenho (à esquerda) e real (à direita), como círculos
        yb = 520
        c.drawCircle(x + 120, yb, min(rd, 95) * 0.8, paint(mix("#FFFFFF", col, 0.25), a))
        c.drawCircle(x + 120, yb, min(rd, 95) * 0.8, paint(col, a, stroke=3))
        c.drawCircle(x + 330, yb, min(rr, 95) * 0.8, paint(mix("#FFFFFF", INK2, 0.15), a))
        c.drawCircle(x + 330, yb, min(rr, 95) * 0.8, paint(INK2, a, stroke=3))
        text(c, "desenho", x + 120, 620, 22, "bold", col, a)
        text(c, "real", x + 330, 620, 22, "bold", INK2, a)
        text(c, sub, x + 230, 664, 24, "black", INK, a)
        if ex_:
            text(c, ex_, x + 230, 694, 20, "bold", GRAY, a)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        pill(c, "hoje: só REDUÇÃO", W / 2, 770, GREEN, size=30, a=ad, anchor="center")


# ======================================================================
# bloco d — cálculo 1: o mapa desencolhendo
# ======================================================================

MX, MY, MW, MH = 190, 290, 1080, 440


def b_calc1(c, t, C, B):
    head(c, t, B["start"], "CÁLCULO 1", "ACHAR A MEDIDA REAL", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.5)
    linha(c, [("6 cm", BLUE), (" no mapa  ·  escala ", INK), ("1 : 500 000", PURPLE), ("  →  real = ?", INK)],
          W / 2, 220, 40, a0)
    u = ease_io(clamp((t - C["09.a"]) / max(0.5, C["09.c"] - C["09.a"])))
    seg0, seg1 = 300, 960
    L = lerp(seg0, seg1, u)
    xa, ya = MX + 60, MY + MH * 0.55
    if a0 > 0:
        c.save(); c.clipRect(skia.Rect.MakeXYWH(MX, MY, MW, MH))
        z = L / seg0
        c.translate(xa, ya); c.scale(z, z); c.translate(-xa, -ya)
        mw = seg0 / 0.76
        mapa(c, xa - mw * 0.12, ya - 0.55 * 260, mw, 260, a0, cidades=False)
        c.restore()
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(MX, MY, MW, MH), 14, 14), paint("#B9C7A6", a0, stroke=3))
        line(c, xa, ya, xa + L, ya, RED, a0, 8)
        for xx in (xa, xa + L):
            c.drawCircle(xx, ya, 13, paint("#FFFFFF", a0)); c.drawCircle(xx, ya, 9, paint(RED, a0))
        # régua embaixo do segmento
        if u < 0.02:
            for k in range(7):
                xx = xa + k * seg0 / 6
                line(c, xx, ya + 26, xx, ya + 46, INK, a0, 3)
                text(c, str(k), xx, ya + 74, 20, "bold", INK2, a0)
            text(c, "6 cm", xa + seg0 / 2, ya - 26, 30, "black", RED, a0)
    # contador
    ab = ep(t, C["09.b"], 0.4)
    cx_ = 1520
    rrect(c, 1310, 300, 420, 300, 22, "#FFFFFF", a0, shadow=True)
    text(c, "MEDIDA REAL", cx_, 350, 24, "black", GRAY, a0)
    v = round(6 * 500000 ** u) if t >= C["09.a"] else 6
    if u >= 0.999:
        v = 3000000
    text_mid(c, num(v), cx_, 440, 60 if v < 1e6 else 54, "black", GREEN if u >= 0.999 else INK, a0)
    text(c, "cm", cx_, 520, 34, "black", INK2, a0)
    if ab > 0:
        text(c, "6 cm × 500 000", cx_, 570, 28, "black", PURPLE, ab)
    acc = ep(t, C["09.c"], 0.4)
    if acc > 0:
        selo(c, cx_, 660, acc, "3 000 000 cm", GREEN, -3, 34)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        regra(c, "MAPA → MUNDO: o número CRESCE  ·  × denominador", W / 2, 790, ad, 34)


# ======================================================================
# bloco e — a cadeia de conversão
# ======================================================================

def b_cadeia(c, t, C, B):
    head_seq(c, t, C, [("10", "A CADEIA", "DE CENTÍMETRO ATÉ QUILÔMETRO", PURPLE),
                       ("11", "DE UMA VEZ SÓ", "÷ 100 000", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        a0 = ep(t, C["10"], 0.5)
        l0 = ep(t, C["10.a"], 0.5)
        l1 = ep(t, C["10.b"] + 1.4, 0.5)
        l2 = ep(t, C["10.c"] + 1.4, 0.5)
        cadeia(c, 330, 520, a0, (l0, l1, l2), (ep(t, C["10.b"], 0.5), ep(t, C["10.c"], 0.5)),
               ("3 000 000 cm", "30 000 m", "30 km"), sw=420, sh=100, alt=220, size=64, vsize=38)
        if l0 > 0:
            pill(c, "certo, mas em cm", 540, 790, AMBER, size=26, a=l0 * (1 - l2), anchor="center")
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            conferido(c, "30 km: distância de estrada", 1050, 800, ad, True, 34)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, [("÷ 100", AMBER), ("  e depois  ", INK), ("÷ 1 000", AMBER), ("   =   ", INK), ("÷ 100 000", PURPLE)],
              W / 2, 280, 56, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        text(c, "100 000 → CINCO zeros → a vírgula anda 5 casas para a esquerda", W / 2, 400, 34, "black", PURPLE, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        s = -5 * ep(t, C["11.c"] + 0.3, 1.6)
        vnum(c, "3", 7, s, W / 2, 560, 120, acc, INK)
        text(c, "cm" if s > -4.95 else "km", W / 2, 700, 44, "black", GRAY if s > -4.95 else GREEN, acc)
        if s <= -4.95:
            linha(c, [("3 000 000 cm = ", INK), ("30 km", GREEN)], W / 2, 780, 44, ep(t, C["11.c"] + 2.0, 0.4))


# ======================================================================
# bloco f — o atalho dos 5 zeros
# ======================================================================

def b_atalho(c, t, C, B):
    head_seq(c, t, C, [("12", "ATALHO", "CORTE CINCO ZEROS", GREEN), ("13", "TREINO DA TESOURA", "km POR CENTÍMETRO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        K.atalho(c, 260, 200, 1400, 130, "ATALHO DOS 5 ZEROS", ["em 1 : n, cada cm vale  n ÷ 100 000  km"], aa, 40)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            linha(c, [("1 : ", INK)], 560, 470, 100, ab)
            u = ep(t, C["12.c"] + 0.4, 2.2)
            corte(c, "500000", 900, 470, 100, ab, u)
            acc = ep(t, C["12.c"] + 2.8, 0.4)
            if acc > 0:
                linha(c, [("1 cm = ", INK), ("5 km", GREEN)], 1420, 470, 72, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            rrect(c, 460, 620, 1000, 130, 24, mix("#FFFFFF", GREEN, 0.10), ad)
            linha(c, [("6 cm × 5 km = ", INK), ("30 km", GREEN)], W / 2, 670, 56, ad)
            text(c, "de cabeça", W / 2, 738, 28, "black", GREEN, ad)
        return
    rows = [("13.a", "1000000", "10 km", "5 zeros fora: sobra 10", 5),
            ("13.b", "250000", "2,5 km", "só 4 zeros: a vírgula anda mais 1 casa", 4),
            ("13.c", "50000", "0,5 km", "só 4 zeros: mais 1 casa → meio km", 4)]
    for k, (cue, dig, res, nota, nz) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        y = 290 + k * 180
        rrect(c, 200, y - 70, 1520, 150, 18, "#F7F7F5", a)
        text_mid(c, "1 :", 330, y, 64, "black", INK, a)
        u = ep(t, C[cue] + 0.6, 1.8)
        corte(c, dig, 640, y, 64, a, u)
        ar = ep(t, C[cue] + 2.6, 0.4)
        if ar > 0:
            text_mid(c, "→", 950, y, 60, "black", GRAY, ar)
            linha(c, [(res, GREEN), (" por cm", INK)], 1180, y - 14, 52, ar)
            text(c, nota, 1180, y + 52, 24, "bold", AMBER if nz < 5 else GRAY, ar)


# ======================================================================
# bloco g — cálculo 2
# ======================================================================

def b_calc2(c, t, C, B):
    head(c, t, B["start"], "CÁLCULO 2", "ACHAR A MEDIDA NO DESENHO", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["14"], 0.5)
    pergunta(c, "do MUNDO para o MAPA: quanto ocupa no papel?", W / 2, 230, a0, PURPLE, 34)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        linha(c, [("20 km", GREEN), (" no mundo  ·  escala ", INK), ("1 : 500 000", PURPLE)], W / 2, 320, 44, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, 220, 390, 720, 300, 22, "#FFFFFF", ab, shadow=True)
        text(c, "1º  passe para cm", 580, 440, 30, "black", BLUE, ab)
        linha(c, [("20 km = ", INK), ("2 000 000 cm", BLUE)], 580, 510, 44, ab)
        text(c, "(× 100 000: devolva os 5 zeros)", 580, 580, 24, "bold", GRAY, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 390, 720, 300, 22, "#FFFFFF", acc, shadow=True)
        text(c, "2º  divida pelo denominador", 1340, 440, 30, "black", PURPLE, acc)
        linha(c, [("2 000 000 cm ÷ 500 000", INK)], 1340, 510, 38, acc)
        linha(c, [("= ", INK), ("4 cm", GREEN)], 1340, 580, 56, ep(t, C["14.c"] + 2.4, 0.4))
        # segmento encolhendo
        g = ep(t, C["14.c"] + 0.6, 1.8)
        Ls = lerp(560, 160, g)
        line(c, 1340 - Ls / 2, 650, 1340 + Ls / 2, 650, RED, acc, 7)
        pill(c, "MUNDO → MAPA: encolhe · ÷ denominador", 1340, 745 - 20, PURPLE, size=22, a=acc, anchor="center")
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        K.atalho(c, 220, 712, 720, 110, "ATALHO", ["1 cm = 5 km  →  20 ÷ 5 = 4 cm"], ad, 32)


# ======================================================================
# bloco h — cálculo 3
# ======================================================================

def b_calc3(c, t, C, B):
    head_seq(c, t, C, [("15", "CÁLCULO 3", "ACHAR A ESCALA", PURPLE), ("16", "ATALHO", "DEVOLVA OS 5 ZEROS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        if aa > 0:
            linha(c, [("3 cm", BLUE), (" no mapa  ↔  ", INK), ("15 km", GREEN), (" no mundo  →  escala = ?", INK)],
                  W / 2, 240, 44, aa)
        ab = ep(t, C["15.b"], 0.5)
        if ab > 0:
            regra(c, "E = desenho ÷ real, na MESMA unidade", W / 2, 350, ab, 34)
            linha(c, [("15 km = ", INK), ("1 500 000 cm", GREEN)], W / 2, 450, 44, ep(t, C["15.b"] + 2.2, 0.4))
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            fr(c, "3 cm", "1 500 000 cm", 560, 600, 56, INK, acc)
            text_mid(c, "÷ 3", 900, 620, 44, "black", AMBER, ep(t, C["15.c"] + 2.0, 0.4))
            text_mid(c, "=", 1000, 620, 60, "black", INK, ep(t, C["15.c"] + 2.0, 0.4))
            a2 = ep(t, C["15.c"] + 3.0, 0.4)
            fr(c, "1", "500 000", 1190, 600, 56, INK, a2)
            text_mid(c, "=  1 : 500 000", 1530, 620, 50, "black", GREEN, ep(t, C["15.c"] + 3.8, 0.4))
        return
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        linha(c, [("15 km ÷ 3 cm = ", INK), ("5 km por cm", GREEN)], W / 2, 260, 52, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        text(c, "a tesoura AO CONTRÁRIO: devolva os 5 zeros", W / 2, 380, 32, "black", GREEN, ab)
        u = 1 - ep(t, C["16.b"] + 0.6, 2.0)
        corte(c, "500000", W / 2, 500, 96, ab, u)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        K.atalho(c, 460, 620, 1000, 130, "ATALHO", ["km ÷ cm = km por cm  →  devolva 5 zeros: 1 : 500 000"], acc, 32)
        conferido(c, "os dois caminhos batem", 760, 800, ep(t, C["16.c"] + 2.0, 0.4), True, 30)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "PELO ATALHO E PELA CADEIA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 130, 24, "#F7F7F5", aa)
        linha(c, [("mapa ", INK), ("1 : 200 000", PURPLE), ("  ·  ", INK), ("3 cm", BLUE), ("  =  ? km", INK)],
              W / 2, 285, 58, aa)
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 560)
    if t < C["18"]:
        return
    a1 = ep(t, C["18.a"], 0.4)
    pill(c, "MAPA → MUNDO: cresce", W / 2, 410, PURPLE, size=28, a=a1, anchor="center")
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        text_mid(c, "1 :", 380, 530, 60, "black", INK, ab)
        corte(c, "200000", 640, 530, 60, ab, ep(t, C["18.b"] + 0.5, 1.6))
        linha(c, [("→ 1 cm = ", INK), ("2 km", GREEN)], 1180, 530 - 20, 52, ep(t, C["18.b"] + 2.4, 0.4))
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        linha(c, [("3 cm × 2 km = ", INK), ("6 km", GREEN)], W / 2, 640, 60, acc)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        linha(c, [("3 × 200 000 = 600 000 cm → 6 000 m → ", INK2), ("6 km", GREEN)], W / 2, 750, 34, ad)
        conferido(c, "bateu", 1560, 770, ep(t, C["18.d"] + 3.0, 0.4), True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Escala é desenho sobre real, na mesma unidade.",
          "Do mapa para o mundo, multiplique; do mundo para o mapa, divida.",
          "Em 1 : n, cada centímetro vale n ÷ 100 000 km."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Parar nos centímetros reais", "a multiplicação está perfeita: 3 000 000",
          "ainda faltam os degraus: ÷ 100 000 e chegue ao km"),
         ("Multiplicar quando devia dividir (ou o contrário)", "os números são os mesmos: só muda a operação",
          "para o MUNDO, cresce: ×  ·  para o MAPA, encolhe: ÷"),
         ("Unidades diferentes: 4 cm e 12 km → 4/12 = 1 : 3", "a fração simplificou bonitinho",
          "1 : 3 seria um mapa com 1/3 do tamanho da estrada! Passe tudo para cm ANTES"),
         ("Inverter a razão: 250 000 : 1", "os números são os de sempre",
          "seria um mapa MAIOR que o mundo: desenho sobre real, o 1 vem primeiro")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22", "23"], ERROS)


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


ALTS1 = [("A", "3 km", "cortou 6 zeros", RED), ("B", "30 km", "", GREEN), ("C", "300 km", "cortou só 4 zeros", RED),
         ("D", "3 000 km", "pulou o degrau do m", RED), ("E", "30 000 km", "parou nos metros", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "DO MAPA PARA O REAL", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Em um mapa rodoviário de escala 1 : 500 000, a distância entre duas cidades é representada "
                           "por um segmento de 6 cm. A distância real entre essas cidades é de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 44, C["25.ok"], "B", cues_in, cues_x, gap=34)
    if t >= C["25"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["25"], 0.4))
        pill(c, "CÁLCULO 1 · mapa → mundo · ×", 540, y0 + 40, PURPLE, size=22, a=ep(t, C["25.a"], 0.4), anchor="center")
        linha(c, [("6 cm × 500 000 = ", INK), ("3 000 000 cm", BLUE)], 540, y0 + 100, 32, ep(t, C["25.b"], 0.4))
        linha(c, [("÷ 100 → 30 000 m  ÷ 1 000 → ", INK2), ("30 km", GREEN)], 540, y0 + 160, 30, ep(t, C["25.c"], 0.4))
        linha(c, [("atalho: 5 km por cm × 6 = ", GREEN), ("30 km", GREEN)], 540, y0 + 220, 30, ep(t, C["25.d"], 0.4))
        conferido(c, "30 km entre cidades: plausível", 230, y0 + 285, ep(t, C["25.e"], 0.4), True, 26)
    af = ep(t, C["26.f"], 0.5)
    if af > 0:
        selo(c, 1340, 790, af, "CADA DEGRAU ERRADO TEM SUA ALTERNATIVA", AMBER, -2, 24)


ALTS2 = [("A", "0,3 cm", "um zero a menos", RED), ("B", "3 cm", "", GREEN), ("C", "30 cm", "um zero a mais", RED),
         ("D", "33 cm", "dividiu ao contrário", RED), ("E", "300 cm", "3 metros de mapa!", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · NÓS FAZEMOS", "DO REAL PARA O MAPA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    yend = _enunciado(c, [("Um cartógrafo precisa representar uma distância real de 45 km em um mapa de escala "
                           "1 : 1 500 000. No mapa, essa distância ocupará", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["28"], 0.3)),
         align="left")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 44, C["28.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["27.end"] - 1.9, 540, yend + 140)
    if t >= C["28"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["28"], 0.4))
        pill(c, "CÁLCULO 2 · mundo → mapa · ÷", 540, y0 + 40, PURPLE, size=22, a=ep(t, C["28"], 0.4), anchor="center")
        linha(c, [("45 km = ", INK), ("4 500 000 cm", BLUE)], 540, y0 + 100, 32, ep(t, C["28.a"], 0.4))
        linha(c, [("4 500 000 cm ÷ 1 500 000 = ", INK), ("3 cm", GREEN)], 540, y0 + 160, 28, ep(t, C["28.b"], 0.4))
        linha(c, [("atalho: 1 cm = 15 km → 45 ÷ 15 = ", GREEN), ("3 cm", GREEN)], 540, y0 + 220, 26, ep(t, C["28.c"], 0.4))
        conferido(c, "3 cm cabem numa folha", 230, y0 + 280, ep(t, C["28.d"], 0.4), True, 26)


ALTS3 = [("A", "1 : 3 000", "parou nos metros", RED), ("B", "1 : 30 000", "perdeu um zero", RED),
         ("C", "1 : 300 000", "", GREEN), ("D", "1 : 3 000 000", "um zero a mais", RED),
         ("E", "1 : 4 800 000", "multiplicou", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · VOCÊ FAZ", "ACHAR A ESCALA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.4)
    yend = _enunciado(c, [("Em um mapa, um trecho de estrada com 12 km de extensão real está representado por um "
                           "segmento de 4 cm. A escala desse mapa é", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["31"], 0.3)),
         align="left")
    cues_in = {L: C[f"30.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 44, C["31.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["30.end"] - 1.9, 540, yend + 140)
    if t >= C["31"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["31"], 0.4))
        pill(c, "CÁLCULO 3 · desenho ÷ real", 540, y0 + 40, PURPLE, size=22, a=ep(t, C["31"], 0.4), anchor="center")
        linha(c, [("12 km = ", INK), ("1 200 000 cm", BLUE)], 540, y0 + 100, 32, ep(t, C["31.a"], 0.4))
        ab = ep(t, C["31.b"], 0.4)
        if ab > 0:
            fr(c, "4 cm", "1 200 000 cm", 400, y0 + 160, 28, INK, ab)
            linha(c, [("÷ 4  =  ", AMBER), ("1 : 300 000", GREEN)], 700, y0 + 176, 30, ep(t, C["31.b"] + 2.4, 0.4))
        linha(c, [("atalho: 12 ÷ 4 = 3 km por cm → ", GREEN), ("300 000", GREEN)], 540, y0 + 260, 26, ep(t, C["31.c"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "GRÁFICA × NUMÉRICA", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        g = ep(t, C["34.a"] + 0.8, 1.6)
        s = lerp(1.0, 1.5, g)
        w, h = 330 * s, 200 * s
        x, y = 260, 260
        mapa(c, x, y, w, h, aa, nomes=False)
        text(c, "1 : 50 000", x + 20, y + h - 18, 26 * s, "black", INK, aa, align="left")
        # barrinha gráfica
        bx, by = x + w - 20 - 120 * s, y + h - 30
        rrect(c, bx, by, 120 * s, 10 * s, 2, INK, aa)
        rrect(c, bx + 60 * s, by, 60 * s, 10 * s, 2, "#FFFFFF", aa)
        text(c, "?", x + w + 60, y + h / 2, 90, "black", AMBER, aa)
        text(c, "o NÚMERO ou a BARRINHA?", 520, 720, 34, "black", PURPLE, ep(t, C["34.a"] + 2.4, 0.4))
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        text(c, "1 : 10 000", 1370, 380, 72, "black", INK, ab)
        chip(c, "GRANDE?", 1240, 500, GREEN, ab, 40)
        chip(c, "PEQUENA?", 1500, 500, AMBER, ab, 40)
    pill(c, "ep. 2 · escala gráfica e escala grande × pequena", W / 2, 790, PURPLE, size=30, a=ep(t, C["34.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Você já conhecia o atalho dos 5 zeros?", canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao, ler=b_ler,
              ampliacao=b_ampliacao, calc1=b_calc1, cadeia=b_cadeia, atalho=b_atalho, calc2=b_calc2, calc3=b_calc3,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q2=b_q2, q3=b_q3, ponte=b_ponte, cta=b_cta)
