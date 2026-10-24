"""Visual — Logaritmos, Episódio 4: equações logarítmicas e a condição de existência (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências e frações, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: lrow() (linha com "log" e a base em subscrito, como no ep. 1), porta() + seguranca() + fila() (a
porta do log com o segurança conferindo o documento de cada raiz: verde entra, vermelha é barrada), quadro_cond() (as
condições de existência no canto da tela), lista4() (o roteiro de 4 passos sendo riscado durante a resolução).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum042", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_logaritmos_ep4_equacoes_condicao.mp4"
CARD_R = K.CARD_R
FARDA = "#2F3A56"     # uniforme do segurança


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def _txt(s):
    """parênteses e colchetes sem potência vão como texto (o expr não aceita "(x" partido no espaço)"""
    return any(ch in s for ch in "([") and "^" not in s


def mx(c, s, cx, cy, size, a, col=None, align="center"):
    """expressão matemática de uma cor só (potências, frações); com parênteses e sem potência, texto"""
    if _txt(s):
        w = ftext_w(s, "black", size)
        if a > 0:
            x = cx - w / 2 if align == "center" else cx
            ftext(c, s, x, cy + size * 0.36, size, "black", col or INK, a, align="left")
        return w
    n = len(s.split())
    return K.expr(c, s, cx, cy, size, a, cores={i: col or INK for i in range(n)}, align=align)


def _pw(p, size):
    if p[0] == "log":
        w = ftext_w("log", "black", size)
        return w + (ftext_w(p[1], "black", size * 0.58) + size * 0.04 if p[1] else 0)
    if p[0] == "m":
        return ftext_w(p[1], "black", size) if _txt(p[1]) else K.math_w(p[1], size)
    return ftext_w(p[1], "black", size)


def lrow(c, partes, cx, cy, size, a, align="center", gap=None):
    """linha com logs: partes = [("log", base, cor[, cor_base]), ("m", expr, cor), ("t", texto, cor)].
    A base vai em subscrito; base "" = log decimal. Devolve a largura."""
    gap = size * 0.22 if gap is None else gap
    ws = [_pw(p, size) for p in partes]
    total = sum(ws) + gap * (len(partes) - 1)
    if a <= 0:
        return total
    x = cx - total / 2 if align == "center" else (cx - total if align == "right" else cx)
    for p, w_ in zip(partes, ws):
        col = p[2] if len(p) > 2 and p[2] else INK
        if p[0] == "log":
            ftext(c, "log", x, cy + size * 0.36, size, "black", col, a, align="left")
            if p[1]:
                cb = p[3] if len(p) > 3 else col
                ftext(c, p[1], x + ftext_w("log", "black", size) + size * 0.04, cy + size * 0.62, size * 0.58, "black",
                      cb, a, align="left")
        elif p[0] == "m":
            mx(c, p[1], x, cy, size, a, col, align="left")
        else:
            ftext(c, p[1], x, cy + size * 0.36, size, "black", col, a, align="left")
        x += w_ + gap
    return total


def cartao(c, x, y, w, h, a, col=None, fill=False):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if (fill and col) else "#FFFFFF", a, shadow=True)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 76, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 38, size, a, align="left")


# ---------------- a porta do log ----------------

def seguranca(c, cx, cy, s, a, braco=0.0):
    """segurança de terno escuro com boné e crachá; braco = 0..1 levanta o braço (barrando)"""
    if a <= 0:
        return
    # pernas e corpo
    rrect(c, cx - 0.30 * s, cy + 0.05 * s, 0.24 * s, 0.62 * s, 0.06 * s, FARDA, a)
    rrect(c, cx + 0.06 * s, cy + 0.05 * s, 0.24 * s, 0.62 * s, 0.06 * s, FARDA, a)
    rrect(c, cx - 0.40 * s, cy - 0.55 * s, 0.80 * s, 0.70 * s, 0.16 * s, FARDA, a)
    # braço que barra
    c.save(); c.translate(cx - 0.36 * s, cy - 0.46 * s); c.rotate(-80 * clamp(braco) + 10)
    rrect(c, -0.09 * s, 0, 0.18 * s, 0.56 * s, 0.09 * s, mix(FARDA, "#000000", 0.15), a)
    c.drawCircle(0, 0.58 * s, 0.10 * s, paint("#E9B98F", a))
    c.restore()
    rrect(c, cx + 0.27 * s, cy - 0.46 * s, 0.18 * s, 0.50 * s, 0.09 * s, mix(FARDA, "#000000", 0.15), a)
    # crachá
    rrect(c, cx + 0.06 * s, cy - 0.40 * s, 0.22 * s, 0.14 * s, 0.03 * s, "#FFFFFF", a)
    line(c, cx + 0.10 * s, cy - 0.33 * s, cx + 0.24 * s, cy - 0.33 * s, BLUE, a, max(2, 0.02 * s))
    # cabeça e boné
    c.drawCircle(cx, cy - 0.78 * s, 0.22 * s, paint("#E9B98F", a))
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - 0.23 * s, cy - 1.03 * s, 0.46 * s, 0.40 * s), 180, 180)
    p.close()
    c.drawPath(p, paint(FARDA, a))
    rrect(c, cx - 0.05 * s, cy - 0.88 * s, 0.36 * s, 0.06 * s, 0.03 * s, FARDA, a)


def porta(c, cx, cy, a, placa, w=230, h=380):
    """porta aberta com a placa (partes de lrow) em cima"""
    if a <= 0:
        return
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x - 18, y - 18, w + 36, h + 18, 16, mix("#FFFFFF", INK, 0.18), a)
    rrect(c, x, y, w, h, 10, mix("#FFFFFF", PURPLE, 0.10), a)
    # folha da porta entreaberta
    p = skia.Path()
    p.moveTo(x + w, y); p.lineTo(x + w + 70, y + 30); p.lineTo(x + w + 70, y + h - 30); p.lineTo(x + w, y + h); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", PURPLE, 0.45), a))
    c.drawCircle(x + w + 54, y + h / 2, 7, paint(INK, a))
    pw = lrow(c, placa, cx, y - 70, 40, 0) + 60
    rrect(c, cx - pw / 2, y - 110, pw, 80, 18, "#FFFFFF", a, shadow=True)
    lrow(c, placa, cx, y - 70, 40, a)


def _ficha(c, cx, cy, s, a, col, r=50):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(mix("#FFFFFF", col, 0.18), a))
    c.drawCircle(cx, cy, r, paint(col, a, stroke=5))
    text_mid(c, s, cx, cy, 40 if len(s) < 3 else 32, "black", col, a)


def fila(c, t, cx, cy, a, fichas, guarda=True, dx_ok=300):
    """a porta em (cx, cy): cada ficha = (texto, t_chega, ok, aviso). Chega da esquerda em 1,2 s, mostra o documento e:
    ok → passa pela porta (vai para a direita, verde); não → é barrada (fica de lado, vermelha, com o aviso)."""
    if a <= 0:
        return
    xg = cx - 190
    braco = 0.0
    nok = nno = 0
    avisos = []
    for s_, t0, ok, aviso in fichas:
        if t < t0:
            continue
        u = ease_io(clamp((t - t0) / 1.2))
        dec = ep(t, t0 + 1.5, 0.4)
        xf = cx - 760 + (cx - 340 - (cx - 760)) * u
        yf = cy + 120
        col = INK2
        if dec > 0:
            col = GREEN if ok else RED
            if ok:
                v = ease_io(clamp((t - t0 - 1.7) / 1.0))
                xf = xf + (cx + dx_ok + nok * 120 - xf) * v
                yf = yf + (cy + 40 - yf) * v
            else:
                braco = max(braco, dec * (1 - ep(t, t0 + 3.6, 0.5)))
                v = ease_io(clamp((t - t0 - 2.4) / 0.8))
                xf = xf + (cx - 330 - nno * 120 - xf) * v
                yf = yf + (cy + 220 - yf) * v
        _ficha(c, xf, yf, s_, a, col)
        if dec > 0:
            if ok:
                check_icon(c, xf + 44, yf - 44, 18, a * dec, GREEN)
            else:
                check_icon(c, xf + 44, yf - 44, 18, a * dec, RED, "x")
                if aviso:
                    avisos.append((aviso, xf, yf, dec, ease_io(clamp((t - t0 - 2.4) / 0.8))))
        if dec > 0.5:
            if ok:
                nok += 1
            else:
                nno += 1
    if guarda:
        seguranca(c, xg, cy + 40, 200, a, braco)
    for aviso, xf, yf, dec, v in avisos:
        # durante a conferência, em cima do segurança; depois, embaixo da ficha barrada
        if v < 1:
            pill(c, aviso, xg, cy - 250, RED, size=26, a=a * dec * (1 - v), anchor="center", bounds=(0, 1920))
        pill(c, aviso, xf, yf + 78, RED, size=20, a=a * v, anchor="center", bounds=(0, 1920))


# ---------------- condições e roteiro ----------------

PASSOS = ["condições de existência", "juntar os logs", "eliminar o log", "resolver e testar"]


def quadro_cond(c, linhas, a, x=1300, y=200, w=420):
    """as condições de existência no canto: linhas = [(expr, cor)]"""
    if a <= 0:
        return
    h = 92 + 70 * len(linhas)
    rrect(c, x, y, w, h, 20, mix("#FFFFFF", BLUE, 0.10), a, shadow=True)
    text(c, "CONDIÇÕES", x + w / 2, y + 46, 24, "black", BLUE, a, tracking=2)
    for k, (s_, col) in enumerate(linhas):
        mx(c, s_, x + w / 2, y + 108 + 70 * k, 38, a, col or INK)


def lista4(c, t, marcas, a, x=1300, y=470, w=420):
    """o roteiro de 4 passos: marcas = instantes em que cada passo é riscado (feito)"""
    if a <= 0:
        return
    rrect(c, x, y, w, 360, 20, "#FFFFFF", a, shadow=True)
    text(c, "ROTEIRO", x + w / 2, y + 44, 22, "black", PURPLE, a, tracking=2)
    for k, s_ in enumerate(PASSOS):
        yy = y + 100 + 66 * k
        f = ep(t, marcas[k], 0.4) if k < len(marcas) and marcas[k] is not None else 0
        badge_num(c, k + 1, x + 44, yy, a, 20, bg=GREEN if f > 0.5 else PURPLE)
        text(c, s_, x + 80, yy + 10, 26, "bold", mix(INK, GRAY, f), a, align="left")
        if f > 0:
            strike(c, x + 76, yy, x + 84 + text_w(s_, "bold", 26), yy, f, GREEN, f)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "LOGARITMOS · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        cartao(c, 260, 220, 1400, 150, aa)
        lrow(c, [("log", "", INK), ("m", "x +", INK), ("log", "", INK), ("m", "(x + 3) = 1", INK)], 700, 295, 58, aa)
        arrow(c, 1050, 295, 1150, 295, PURPLE, ep(t, C["01.a"] + 1.5, 0.4), 5, 16)
        mx(c, "x^2 + 3x − 10 = 0", 1400, 295, 46, ep(t, C["01.a"] + 1.8, 0.4), PURPLE)
    ab = ep(t, C["01.b"], 0.5)
    alts = [("A", "{2}"), ("B", "{−5}"), ("C", "{2, −5}"), ("D", "{5}"), ("E", "∅")]
    for k, (L, s_) in enumerate(alts):
        ak = ab * ep(t, C["01.b"] + 0.15 * k, 0.3)
        if ak <= 0:
            continue
        x = 380 + k * 290
        hot = L == "C"
        col = AMBER if hot else INK2
        rrect(c, x - 125, 440, 250, 160, 22, mix("#FFFFFF", col, 0.16 if hot else 0.04), ak, shadow=True)
        badge_num(c, L, x, 440, ak, 22, bg=col if hot else INK)
        text_mid(c, s_, x, 530, 54, "black", col if hot else INK, ak)
    if ab > 0:
        pill(c, "as duas raízes: SEMPRE está lá", 960, 660, AMBER, size=30, a=ep(t, C["01.b"] + 1.6, 0.4),
             anchor="center")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, 960, 770, acc, "E QUASE SEMPRE ESTÁ ERRADA", RED, -3, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "LOGARITMOS · EP. 4", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "4º episódio da série de LOGARITMOS", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "4 PASSOS", "para qualquer equação logarítmica", PURPLE),
             ("02.b", "NENHUMA RAIZ PROIBIDA", "o segurança confere todas", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 640 + k * 640
        rrect(c, x - 290, 330, 580, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 290, 330, 580, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 26, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "episódio 1", 300, y - 75, BLUE, size=22, a=a)
        lrow(c, [("log", "b", INK, BLUE), ("m", "(▢)", BLUE), ("t", "→  ▢ > 0", BLUE)], 700, y + 4, 52, a)
        text(c, "o logaritmando é POSITIVO", 1300, y + 14, 32, "black", BLUE, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 500 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "episódio 2", 300, y - 75, PURPLE, size=22, a=a)
        lrow(c, [("log", "", INK), ("m", "M +", INK), ("log", "", INK), ("m", "N =", INK), ("log", "", PURPLE),
                 ("m", "(M · N)", PURPLE)], 960, y + 4, 54, a)
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 700 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "série de Equação do 2º grau", 300, y - 75, GREEN, size=22, a=a)
        mx(c, "x^2 + 3x − 10 = 0", 640, y + 4, 50, a, INK)
        text(c, "soma −3 · produto −10", 1030, y + 14, 28, "bold", INK2, a)
        ak = ep(t, C["03.c"] + 5.0, 0.4)
        linha(c, [("raízes: ", INK2), ("2", GREEN), (" e ", INK2), ("−5", GREEN)], 1430, y + 2, 42, ak)


# ======================================================================
# concreto — a porta com segurança · definições
# ======================================================================

def b_porta(c, t, C, B):
    head(c, t, B["start"], "UMA PORTA COM SEGURANÇA", "SÓ ENTRA NÚMERO POSITIVO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    porta(c, 1150, 440, aa, [("log", "", PURPLE), ("m", "x", PURPLE)])
    fila(c, t, 1150, 440, aa, [("3", C["04.b"], True, ""), ("−2", C["04.c"], False, "log(−2) não existe")])
    if aa > 0:
        pill(c, "só entra POSITIVO", 1150, 690, BLUE, size=26, a=ep(t, C["04.a"] + 2.0, 0.4), anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    defin(c, "CONDIÇÃO DE EXISTÊNCIA", "quem pode ficar dentro do log", 300, 760, 1320, ad, BLUE, 32)


def b_definicoes(c, t, C, B):
    head(c, t, B["start"], "ONDE O SEGURANÇA TRABALHA", "QUATRO NOMES", BLUE)
    card(c, *CARD_R)
    itens = [("05.a", "EQUAÇÃO LOGARÍTMICA", "o x aparece dentro de um log", BLUE),
             ("05.b", "RAIZ ESTRANHA", "sai da conta, mas o segurança barra", RED),
             ("05.c", "CONJUNTO SOLUÇÃO", "a lista das respostas que valem", GREEN),
             ("05.d", "CONJUNTO VAZIO  ∅", "nenhuma resposta vale", AMBER)]
    for k, (cue, termo, s_, col) in enumerate(itens):
        ak, d = rise(t, C[cue])
        defin(c, termo, s_, 280, 240 + k * 140 + d, 1360, ak, col, 34)


# ======================================================================
# bloco a — o roteiro de 4 passos
# ======================================================================

def b_roteiro(c, t, C, B):
    head(c, t, B["start"], "O CAMINHO QUE FUNCIONA SEMPRE", "4 PASSOS", PURPLE)
    card(c, *CARD_R)
    subs = ["o segurança anota quem pode entrar", "junte as peças: um log de cada lado",
            "pela definição ou igualando o de dentro", "descarte quem o segurança barrar"]
    for k, (s_, sub) in enumerate(zip(PASSOS, subs)):
        ak = ep(t, C[f"06.{'abcd'[k]}"], 0.5)
        if ak <= 0:
            continue
        y = 260 + k * 140
        rrect(c, 300, y - 50, 1320, 110, 22, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, 370, y + 5, ak, 32, bg=GREEN if k in (0, 3) else PURPLE)
        text(c, s_.upper(), 430, y + 18, 40, "black", INK, ak, align="left")
        text(c, sub, 1580, y + 16, 26, "bold", GREEN if k in (0, 3) else PURPLE, ak, align="right")


# ======================================================================
# blocos b, c, d — os três tipos
# ======================================================================

def _passo(c, k, partes_ou_expr, t, cue, y, col=INK, size=52, x=720):
    ak = ep(t, cue, 0.5)
    if ak <= 0:
        return 0
    if isinstance(partes_ou_expr, str):
        mx(c, partes_ou_expr, x, y, size, ak, col)
    else:
        lrow(c, partes_ou_expr, x, y, size, ak)
    return ak


def b_tipo1(c, t, C, B):
    head(c, t, B["start"], "TIPO 1 · PELA DEFINIÇÃO", "O LOG É IGUAL A UM NÚMERO", PURPLE)
    card(c, *CARD_R)
    _passo(c, 0, [("log", "3", INK, BLUE), ("m", "(x − 1) = 2", INK)], t, C["07.a"], 270, size=64)
    quadro_cond(c, [("x − 1 > 0", INK), ("x > 1", BLUE)], ep(t, C["07.b"], 0.5))
    lista4(c, t, [C["07.b"] + 2.0, C["07.c"] - 0.2, C["07.c"] + 2.0, C["07.e"] + 1.0], ep(t, C["07.a"], 0.5))
    ac = _passo(c, 1, "3^2 = x − 1", t, C["07.c"], 420, PURPLE)
    if ac > 0:
        pill(c, "a base sobe e o 2 vira expoente", 720, 490, PURPLE, size=22, a=ac, anchor="center", bounds=(160, 1270))
    _passo(c, 2, "9 = x − 1", t, C["07.c"] + 2.4, 570)
    ad = _passo(c, 3, "x = 10", t, C["07.d"], 690, GREEN, 70)
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        rrect(c, 380, 770, 680, 70, 18, mix("#FFFFFF", GREEN, 0.14), ae)
        linha(c, [("10 > 1 ?  ", INK), ("SIM · ENTRA", GREEN)], 720, 805, 32, ae)


def b_tipo2(c, t, C, B):
    head(c, t, B["start"], "TIPO 2 · MESMA BASE", "LOG DOS DOIS LADOS", PURPLE)
    card(c, *CARD_R)
    _passo(c, 0, [("log", "2", INK, BLUE), ("m", "(3x − 1) =", INK), ("log", "2", INK, BLUE), ("m", "(x + 5)", INK)], t,
           C["08.a"], 270, size=56)
    quadro_cond(c, [("3x − 1 > 0", INK), ("x + 5 > 0", INK)], ep(t, C["08.b"], 0.5))
    lista4(c, t, [C["08.b"] + 2.0, C["08.c"] - 0.2, C["08.c"] + 2.4, C["08.e"] + 1.0], ep(t, C["08.a"], 0.5))
    ac = _passo(c, 1, "3x − 1 = x + 5", t, C["08.c"] + 2.4, 440, PURPLE)
    if ac > 0:
        pill(c, "mesma base: iguale o de dentro", 720, 510, PURPLE, size=22, a=ac, anchor="center", bounds=(160, 1270))
    _passo(c, 2, "2x = 6", t, C["08.d"], 580)
    _passo(c, 3, "x = 3", t, C["08.d"] + 1.6, 680, GREEN, 70)
    ae = ep(t, C["08.e"], 0.5)
    if ae > 0:
        rrect(c, 300, 760, 840, 76, 18, mix("#FFFFFF", GREEN, 0.14), ae)
        linha(c, [("3·3 − 1 = 8   ·   3 + 5 = 8   ", INK), ("ENTRA", GREEN)], 720, 798, 32, ae)


def b_atalho_base(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "A BASE PULA PARA O OUTRO LADO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · TIPO 1", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["09.a"], 0.5)
    lrow(c, [("log", "b", INK, BLUE), ("m", "(algo) = c", INK)], 960, 360, 70, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        arrow(c, 960, 420, 960, 490, GREEN, ab, 6, 18)
        mx(c, "algo = b^c", 960, 560, 80, ab, GREEN)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rrect(c, 380, 650, 1160, 110, 22, "#FFFFFF", acc, shadow=True)
        lrow(c, [("log", "3", INK, BLUE), ("m", "(algo) = 2", INK), ("t", "→", GREEN), ("m", "algo = 3^2", GREEN)], 960,
             705, 50, acc)


def b_tipo3(c, t, C, B):
    sid = which(t, C, ["10", "11"])
    head(c, t, B["start"] if sid == "10" else C["11"], "TIPO 3 · JUNTANDO OS LOGS",
         "JUNTE AS PEÇAS" if sid == "10" else "HORA DO DOCUMENTO", PURPLE if sid == "10" else GREEN)
    card(c, *CARD_R)
    quadro_cond(c, [("x > 0", INK), ("x + 3 > 0", INK)], ep(t, C["10.b"], 0.5))
    lista4(c, t, [C["10.b"] + 2.0, C["10.c"] + 1.0, C["10.d"] + 1.0, C["11.c"]], ep(t, C["10.a"], 0.5))
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        lrow(c, [("log", "", INK), ("m", "x +", INK), ("log", "", INK), ("m", "(x + 3) = 1", INK)], 720, 270, 56, aa)
        if aa > 0:
            pill(c, "sem base escrita: base 10", 720, 345, BLUE, size=22, a=ep(t, C["10.a"] + 2.2, 0.4),
                 anchor="center", bounds=(160, 1270))
        ac = ep(t, C["10.c"], 0.5)
        if ac > 0:
            lrow(c, [("log", "", PURPLE), ("m", "[x(x + 3)] = 1", PURPLE)], 720, 440, 54, ac)
            pill(c, "soma de logs = log do PRODUTO", 720, 510, PURPLE, size=22, a=ac, anchor="center",
                 bounds=(160, 1270))
        _passo(c, 2, [("t", "x(x + 3) =", INK), ("m", "10^1 = 10", INK)], t, C["10.d"], 600)
        ae = ep(t, C["10.e"], 0.5)
        if ae > 0:
            mx(c, "x^2 + 3x − 10 = 0", 720, 700, 50, ae, INK)
            linha(c, [("raízes: ", INK2), ("2", GREEN), ("  e  ", INK2), ("−5", AMBER)], 720, 790, 44,
                  ep(t, C["10.e"] + 2.4, 0.4))
        return
    a0 = ep(t, C["11"], 0.4)
    porta(c, 800, 420, a0, [("log", "", PURPLE), ("t", "x   e", INK2), ("log", "", PURPLE), ("t", "(x + 3)", PURPLE)],
          w=200, h=320)
    fila(c, t, 800, 420, a0, [("2", C["11.a"], True, ""), ("−5", C["11.b"], False, "log(−5) não existe")], dx_ok=260)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 780, 650, 440, 80, 20, mix("#FFFFFF", GREEN, 0.16), acc)
        linha(c, [("S = ", INK), ("{2}", GREEN)], 1000, 690, 44, acc)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        lrow(c, [("log", "", INK), ("m", "2 +", INK), ("log", "", INK), ("m", "5 =", INK), ("log", "", INK),
                 ("m", "10 = 1", GREEN)], 1000, 790, 36, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("12", "SUA VEZ", "PAUSE E TENTE", GREEN), ("13", "VAMOS JUNTOS", "OS 4 PASSOS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    lrow(c, [("log", "2", INK, BLUE), ("m", "(x + 3) = 4", INK)], 720 if t >= C["13"] else 960, 300, 70, aa)
    if t < C["13"]:
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            pill(c, "comece pela condição", 960, 420, BLUE, size=30, a=ab, anchor="center")
        pause_timer(c, t, C["12.end"] - 1.9, 960, 620)
        return
    quadro_cond(c, [("x + 3 > 0", INK), ("x > −3", BLUE)], ep(t, C["13.a"], 0.5))
    lista4(c, t, [C["13.a"] + 2.0, C["13.b"] - 0.2, C["13.b"] + 1.6, C["13.d"] + 1.0], 1.0)
    _passo(c, 1, "x + 3 = 2^4 = 16", t, C["13.b"], 450, PURPLE)
    _passo(c, 2, "x = 13", t, C["13.c"], 580, GREEN, 72)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        rrect(c, 360, 690, 720, 80, 18, mix("#FFFFFF", GREEN, 0.14), ad)
        linha(c, [("13 + 3 = 16 > 0   ", INK), ("ENTRA", GREEN)], 720, 730, 34, ad)


# ======================================================================
# recap, atalho do documento, erros
# ======================================================================

FRASES = ["Escreva as condições de existência antes de começar.",
          "Junte os logs até sobrar um só de cada lado.",
          "Toda raiz precisa passar no teste do logaritmando positivo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["14", "21"])
    frame(c, t, B["start"] if sid == "14" else C["21"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "14" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


def b_atalho_doc(c, t, C, B):
    head(c, t, B["start"], "ATALHO PARA A PROVA", "O TESTE DO DOCUMENTO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 620, GREEN, a0, 0.08)
        text(c, "ATALHO · DESCONFIE DAS DUAS RAÍZES", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 760, 300, 400, 120, 22, mix("#FFFFFF", AMBER, 0.2), aa)
        text_mid(c, "{ r₁ , r₂ }", 960, 360, 56, "black", AMBER, aa)
        selo(c, 1330, 360, aa, "DESCONFIE", AMBER, -5, 34)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("cada raiz → nos logaritmandos ", INK), ("ORIGINAIS", GREEN), (", um por um", INK)], 960, 500, 40,
              ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        for k, (s_, col, ok) in enumerate((("positivo", GREEN, True), ("zero ou negativo", RED, False))):
            x = 660 + k * 600
            rrect(c, x - 250, 600, 500, 150, 24, "#FFFFFF", acc, shadow=True)
            if ok:
                check_icon(c, x - 170, 675, 30, acc, col)
            else:
                check_icon(c, x - 170, 675, 30, acc, col, "x")
            text(c, s_, x - 120, 670, 36, "black", col, acc, align="left")
            text(c, "ENTRA" if ok else "BARRADO", x - 120, 720, 26, "bold", INK2, acc, align="left")


ERROS = [("Aceitar x = −5 em log x + log(x + 3) = 1",
          "−5 é raiz de verdade da equação do 2º grau",
          "a pergunta tem log: log(−5) NÃO EXISTE. Teste cada raiz nos logaritmandos originais."),
         ("Somar os de dentro: log x + log(x + 3) = log(2x + 3)",
          "do lado de fora está escrito “mais”",
          "dá x = 3,5, que não confere. Soma de logs vira log do PRODUTO: log[x(x + 3)].")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["16", "17"], ERROS)


# ======================================================================
# questão 3 (você faz)
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS3 = [("A", "{−2}", "ficou com a proibida", RED), ("B", "{4}", "", GREEN), ("C", "{−2, 4}", "esqueceu de testar", RED),
         ("D", "{5}", "somou os de dentro", RED), ("E", "∅", "descartou a que valia", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · VOCÊ FAZ", "A CONDIÇÃO DE EXISTÊNCIA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["18.a"], 0.4)
    cues_in = {L: C[f"18.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"20.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS3, 1100, 250, 560, 40, C["19.ok"], "B", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["19"], 0.3)),
         align="left")
    if t < C["19"]:
        yend = _enunciado(c, [("O conjunto solução, nos reais, da equação", INK)], a0, 260, 32)
        wq = lrow(c, [("log", "2", INK, BLUE), ("m", "x +", INK), ("log", "2", INK, BLUE), ("m", "(x − 2) = 3", INK),
                      ("t", "é", INK)], 190, yend + 50, 54, a0, align="left")
        pause_timer(c, t, C["18.end"] - 1.9, 560, 640)
        return
    a1 = ep(t, C["19"], 0.4)
    rrect(c, 170, 200, 880, 630, 18, "#FFFFFF", a1, shadow=True)
    if t < C["19.d"]:
        lrow(c, [("log", "2", INK, BLUE), ("m", "x +", INK), ("log", "2", INK, BLUE), ("m", "(x − 2) = 3", INK)], 610,
             250, 44, a1)
        if a1 > 0:
            rrect(c, 230, 300, 760, 80, 16, mix("#FFFFFF", BLUE, 0.12), a1)
            linha(c, [("x > 0  e  x > 2   →   ", INK), ("x > 2", BLUE)], 610, 340, 34, a1)
        aa = ep(t, C["19.a"], 0.4)
        lrow(c, [("log", "2", PURPLE, BLUE), ("m", "[x(x − 2)] = 3", PURPLE)], 610, 450, 44, aa)
        ab = ep(t, C["19.b"], 0.4)
        mx(c, "x^2 − 2x = 2^3 = 8", 610, 560, 44, ab, PURPLE)
        acc = ep(t, C["19.c"], 0.4)
        linha(c, [("raízes: ", INK2), ("4", GREEN), ("  e  ", INK2), ("−2", AMBER)], 610, 680, 44, acc)
        return
    # o segurança confere o documento das duas raízes (animação principal)
    porta(c, 680, 420, a1, [("log", "2", PURPLE, BLUE), ("t", "x  e", INK2), ("log", "2", PURPLE, BLUE),
                            ("t", "(x − 2)", PURPLE)], w=170, h=300)
    fila(c, t, 680, 420, a1, [("4", C["19.d"], True, ""), ("−2", C["19.e"], False, "log₂(−2) não existe")], dx_ok=210)
    af = ep(t, C["19.f"], 0.4)
    if af > 0:
        rrect(c, 520, 740, 500, 76, 16, mix("#FFFFFF", GREEN, 0.14), af)
        lrow(c, [("log", "2", INK, BLUE), ("m", "4 +", INK), ("log", "2", INK, BLUE), ("m", "2 = 3", GREEN)],
             770, 778, 34, af)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    aa = ep(t, C["22.a"], 0.5)
    if aa > 0:
        selo(c, W / 2, 290, aa, "CAÇA ÀS PEGADINHAS", AMBER, -3, 46)
    ab = ep(t, C["22.b"], 0.5)
    for k, (s_, col) in enumerate((("crescimento", GREEN), ("decaimento", RED))):
        ak = ab * ep(t, C["22.b"] + 1.2 * k, 0.4)
        if ak > 0:
            x = 660 + k * 600
            cartao(c, x - 250, 410, 500, 150, ak)
            text_mid(c, s_, x, 485, 50, "black", col, ak)
    acc = ep(t, C["22.c"], 0.5)
    for k, (s_, col) in enumerate((("2 ≈ 0,30", BLUE), ("3 ≈ 0,48", PURPLE))):
        ak = acc * ep(t, C["22.c"] + 1.2 * k, 0.4)
        if ak > 0:
            x = 660 + k * 600
            cartao(c, x - 250, 610, 500, 150, ak)
            lrow(c, [("log", "", INK), ("m", s_, col)], x, 685, 54, ak)


def b_cta(c, t, C, B):
    cta(c, t, C["23.like"], C["23.sub"], C["23.bell"], C["23.com"], C["23.bye"],
        "Você já tinha marcado a alternativa com as duas raízes?", canal="no Estudativo", anki=C["23.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, porta=b_porta, definicoes=b_definicoes,
              roteiro=b_roteiro, tipo1=b_tipo1, tipo2=b_tipo2, atalho_base=b_atalho_base, tipo3=b_tipo3,
              tipo3b=b_tipo3, exercicio=b_exercicio, recap=b_recap, atalho_doc=b_atalho_doc, erros=b_erros, q3=b_q3,
              ponte=b_ponte, cta=b_cta)
