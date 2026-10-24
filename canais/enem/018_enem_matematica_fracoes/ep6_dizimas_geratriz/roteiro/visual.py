"""Visual — Frações, Decimais e Dízimas, Episódio 6: Decimal exato ou dízima? E a fração geratriz (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (expr com frações empilhadas, alternativas, erro_cards...).
Peças deste episódio: a divisão "na chave" (1 ÷ 4 acaba; 1 ÷ 3 com o resto 1 voltando sempre), o denominador fatorado
(2 e 5 em verde, outros primos em âmbar), a dízima aberta por dentro (parte inteira, não periódica, período) e as FITAS com a
mesma cauda infinita, deslizando juntas; na subtração, a cauda some.
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
_s = importlib.util.spec_from_file_location("comum018", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr, expr, expr_w = K.fr, K.expr, K.expr_w
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w
WT = K.WT

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_fracoes_ep6_dizimas_geratriz.mp4"
CARD_R = K.CARD_R
FITA = "#FFF6DC"        # papel da fita
FITA_B = "#E3C98F"      # borda da fita
PER = BLUE              # período
NAOP = AMBER            # parte não periódica


# ======================================================================
# peças do episódio
# ======================================================================

def numero(c, s, x, cy, size, cores=None, a=1.0, align="left", peso="black"):
    """número desenhado caractere a caractere; cores = {índice: cor}. Devolve [(x0, x1)] de cada caractere."""
    ws = [ftext_w(ch, peso, size) for ch in s]
    total = sum(ws)
    xx = x - total / 2 if align == "center" else (x - total if align == "right" else x)
    pos = []
    for i, ch in enumerate(s):
        if a > 0:
            fmid(c, ch, xx, cy, size, peso, (cores or {}).get(i, INK), a, align="left")
        pos.append((xx, xx + ws[i]))
        xx += ws[i]
    return pos


def chave_sub(c, x0, x1, y, txt, col, a, size=30):
    """colchete por baixo de um trecho do número, com o rótulo"""
    if a <= 0:
        return
    line(c, x0 + 4, y, x1 - 4, y, col, a, 5)
    line(c, x0 + 4, y - 14, x0 + 4, y, col, a, 5)
    line(c, x1 - 4, y - 14, x1 - 4, y, col, a, 5)
    pill(c, txt, (x0 + x1) / 2, y + 44, col, size=size, a=a, anchor="center", bounds=(0, 1920))


def volta(c, cx, cy, r, a, col=None, fase=0.0, sw=5):
    """setinha circular (o resto que volta)"""
    if a <= 0:
        return
    col = AMBER if col is None else col
    a0 = fase * 360
    c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), a0, 290, False, paint(col, a, stroke=sw, cap_round=True))
    ang = math.radians(a0 + 290)
    hx, hy = cx + math.cos(ang) * r, cy + math.sin(ang) * r
    tx, ty = -math.sin(ang), math.cos(ang)
    p = skia.Path()
    p.moveTo(hx + tx * r * 0.45, hy + ty * r * 0.45)
    p.lineTo(hx + math.cos(ang) * r * 0.32, hy + math.sin(ang) * r * 0.32)
    p.lineTo(hx - math.cos(ang) * r * 0.32, hy - math.sin(ang) * r * 0.32)
    p.close()
    c.drawPath(p, paint(col, a))


# ---------------- a divisão na chave ----------------

DX, DY, DS = 40, 84, 72      # deslocamento por linha, espaçamento, tamanho dos algarismos


def chave(c, x, y, linhas, divisor, quoc, a, a_quoc=1.0):
    """divisão na chave (método curto): linhas = [(resto, a_resto, a_zero, cor_resto)]; cada linha vem uma casa à direita.
    quoc = texto do quociente (vai aparecendo)."""
    if a <= 0:
        return
    zw = ftext_w("0", "black", DS)
    xb = x + 4 * DX + 70
    for k, (r_, ar, az, col) in enumerate(linhas):
        xr = x + k * DX
        yy = y + k * DY
        if ar > 0:
            fmid(c, r_, xr - zw, yy, DS, "black", col, a * ar, align="right")
        if az > 0:
            fmid(c, "0", xr - zw, yy, DS, "black", GRAY, a * az, align="left")
    line(c, xb, y - 60, xb, y + 40, INK, a, 5)
    line(c, xb, y + 40, xb + 380, y + 40, INK, a, 5)
    fmid(c, divisor, xb + 40, y - 8, DS, "black", INK, a, align="left")
    if quoc:
        fmid(c, quoc, xb + 40, y + 100, DS, "black", PURPLE, a * a_quoc, align="left")


# ---------------- as fitas ----------------

CW, FH, NC = 64, 80, 8       # largura da casa, altura da fita, casas depois da vírgula
XV = 640                     # onde fica a vírgula (todas as fitas alinhadas por ela)


def fita(c, t, y, inteiro, fixos, periodo, a, label=None, cores=None, a_cauda=1.0, desliza=True, cor_label=None, entra=None):
    """fita de papel com o número: inteiro | vírgula | fixos (não repetem) | período repetido até o fim, com '…'.
    A cauda (o período) desliza para a esquerda sem parar, sempre igual; a_cauda some com ela."""
    if a <= 0:
        return
    c.save(); c.translate((1 - ease_out(clamp(a if entra is None else entra))) * 260, 0)
    x_ini = XV - 16 - len(inteiro) * CW
    x_fim = XV + 16 + NC * CW
    rrect(c, x_ini - 10, y - FH / 2 - 8, x_fim - x_ini + 70, FH + 16, 14, FITA, a, shadow=True)
    for i, d in enumerate(inteiro):
        x = x_ini + i * CW
        c.drawRect(skia.Rect.MakeXYWH(x, y - FH / 2, CW, FH), paint(FITA_B, a * 0.6, stroke=2))
        fmid(c, d, x + CW / 2, y, 50, "black", INK, a)
    fmid(c, ",", XV, y + 6, 50, "black", INK, a)
    x0 = XV + 16
    for i, d in enumerate(fixos):
        x = x0 + i * CW
        c.drawRect(skia.Rect.MakeXYWH(x, y - FH / 2, CW, FH), paint(FITA_B, a * 0.6, stroke=2))
        fmid(c, d, x + CW / 2, y, 50, "black", (cores or {}).get("fixo", NAOP), a)
    xc = x0 + len(fixos) * CW
    ac = a * a_cauda
    if ac > 0:
        p = len(periodo)
        off = 0
        c.save()
        c.clipRect(skia.Rect.MakeLTRB(xc, y - FH / 2 - 4, x_fim, y + FH / 2 + 4))
        n = NC - len(fixos) + p + 1
        for i in range(n):
            x = xc + i * CW - off
            c.drawRect(skia.Rect.MakeXYWH(x, y - FH / 2, CW, FH), paint(FITA_B, ac * 0.6, stroke=2))
            fmid(c, periodo[i % p], x + CW / 2, y, 50, "black", (cores or {}).get("per", PER), ac)
        c.restore()
        for k in range(6):
            c.drawRect(skia.Rect.MakeXYWH(x_fim - 60 + k * 10, y - FH / 2, 10, FH), paint(FITA, ac * (k + 1) / 7))
        fmid(c, "…", x_fim + 30, y, 50, "black", INK2, ac)
    if label:
        expr(c, label, x_ini - 30, y, 50, a, cores={0: cor_label or INK}, align="right")
    c.restore()


def fita_some(c, y, n_fixos, u):
    """a borracha passando na cauda: faixa verde que varre e o aviso 'a cauda SOME'"""
    if u <= 0 or u >= 1:
        return
    xc = XV + 16 + n_fixos * CW
    x_fim = XV + 16 + NC * CW + 60
    xx = lerp(xc, x_fim, u)
    rrect(c, xx - 8, y - FH / 2 - 10, 16, FH + 20, 8, GREEN, 1 - u)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DÍZIMAS E FRAÇÃO GERATRIZ", PURPLE)
    aa = ep(t, C["01.a"], 0.5)
    pos = numero(c, "0,999…", 760, 400, 170, {2: PER, 3: PER, 4: PER, 5: PER}, aa, align="center")
    ab = ep(t, C["01.b"], 0.5)
    acc = ep(t, C["01.c"], 0.5)
    fmid(c, "≈ 1 ?", 1260, 400, 150, "black", AMBER, ab * (1 - acc), align="left")
    if acc > 0:
        fmid(c, "= 1", 1260, 400, 170, "black", GREEN, acc, align="left")
        selo(c, 1380, 560, acc, "EXATAMENTE", GREEN, -5, 40)
    if ab > 0 and acc == 0:
        text(c, "quase?", 1340, 560, 44, "black", AMBER, ab)
    ad = ep(t, C["01.d"], 0.5)
    pill(c, "você vai PROVAR isso", W / 2, 690, PURPLE, size=40, a=ad, anchor="center", bounds=(0, 1920))
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        for k, (dz, f) in enumerate((("0,777…", "7/9"), ("0,8333…", "5/6"), ("1,2454545…", "137/110"))):
            a = ae * ep(t, C["01.e"] + 0.3 * k, 0.4)
            x = (470, 1000, 1590)[k]
            fmid(c, dz, x - 30, 820, 44, "black", INK2, a, align="right")
            arrow(c, x - 10, 820, x + 50, 820, LIGHT, a, 4, 12)
            n_, d_ = f.split("/")
            fr(c, n_, d_, x + 100, 806, 40, GREEN, a)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "saber DE ANTEMÃO: exato ou dízima", "olhando só o denominador"),
            ("02.b", "achar a FRAÇÃO GERATRIZ", "de qualquer dízima")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 230 + d
        check_icon(c, 280, y - 14, 34, a, GREEN)
        text(c, s, 340, y, 50, "black", INK, a, align="left")
        text(c, sub, 340, y + 56, 34, "bold", GRAY, a, align="left")
    aa = ep(t, C["02.a"] + 0.6, 0.5)
    expr(c, "3/8 → 0,375", 1500, 330, 54, aa, cores={2: GREEN})
    ab = ep(t, C["02.b"] + 0.6, 0.5)
    expr(c, "0,777… → 7/9", 1500, 560, 54, ab, cores={2: GREEN})


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    line(c, W / 2, 200, W / 2, 800, LINE, ep(t, C["03.b"], 0.5), 3)
    line(c, 200, 495, 1720, 495, LINE, ep(t, C["03.c"], 0.5), 3)
    itens = [("03.a", "PRIMO", 560, 240), ("03.b", "FATORAR", 1360, 240), ("03.c", "IRREDUTÍVEL", 560, 545),
             ("03.d", "RACIONAL", 1360, 545)]
    for cue, tit, x, y in itens:
        a = ep(t, C[cue], 0.5)
        pill(c, tit, x, y, BLUE, size=28, a=a, anchor="center", bounds=(0, 1920))
    aa = ep(t, C["03.a"], 0.5)
    text(c, "só divide por 1 e por ele mesmo", 560, 320, 30, "bold", INK2, aa)
    fmid(c, "2, 3, 5, 7, 11…", 560, 400, 56, "black", INK, aa)
    ab = ep(t, C["03.b"], 0.5)
    text(c, "escrever como multiplicação de primos", 1360, 320, 30, "bold", INK2, ab)
    fmid(c, "12 = 2 × 2 × 3", 1360, 400, 56, "black", INK, ab)
    acc = ep(t, C["03.c"], 0.5)
    text(c, "não dá mais para simplificar (ep. 1)", 560, 625, 30, "bold", INK2, acc)
    expr(c, "6/12 → 1/2", 560, 715, 60, acc, cores={2: GREEN})
    ad = ep(t, C["03.d"], 0.5)
    text(c, "todo número que vira fração", 1360, 625, 30, "bold", INK2, ad)
    expr(c, "0,5 = 1/2", 1360, 715, 60, ad, cores={2: GREEN})


# ======================================================================
# concreto: dividir de verdade
# ======================================================================

def _passos_1por3(C):
    """instantes de cada passo de 1 ÷ 3 (o resto 1 vira 10, sai um 3, sobra 1...)"""
    s = [C["05.a"], C["05.b"], C["05.c"], WT(C, "05", "novo", 3)]
    return s


def b_dividir(c, t, C, B):
    head_seq(c, t, C, [("04", "DIVIDINDO DE VERDADE", "1 ÷ 4", BLUE), ("05", "DIVIDINDO DE VERDADE", "1 ÷ 3", BLUE),
                       ("06", "DOIS NOMES", "EXATO E DÍZIMA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05", "06"])
    X0, Y0 = 420, 330
    if sid == "04":
        a0 = ep(t, C["04.t"], 0.5)
        ab = ep(t, C["04.b"], 0.4)
        acc = ep(t, C["04.c"] + 1.0, 0.4)
        ad = ep(t, C["04.d"], 0.4)
        t5 = WT(C, "04", "cinco")
        a5 = ep(t, t5, 0.4)
        az = ep(t, WT(C, "04", "zero", 2), 0.4)
        linhas = [("1", 1, ab, INK), ("2", acc, ad, AMBER), ("0", az, 0, GREEN)]
        q = "0," if ab > 0 else ""
        if acc > 0:
            q += "2"
        if a5 > 0:
            q += "5"
        chave(c, X0, Y0, linhas, "4", q, ep(t, C["04.a"], 0.5))
        expr(c, "1 ÷ 4", 1420, 300, 90, a0)
        text(c, "o 1 vira 10", 1420, 430, 36, "black", INK2, ab * (1 - acc))
        text(c, "10 ÷ 4 = 2, sobra 2", 1420, 430, 36, "black", INK2, acc * (1 - ad))
        text(c, "20 ÷ 4 = 5, sobra 0", 1420, 430, 36, "black", INK2, ad)
        if az > 0:
            check_icon(c, X0 + 2 * DX + 50, Y0 + 2 * DY, 22, az, GREEN)
        ae = ep(t, C["04.e"], 0.5)
        pill(c, "ACABOU", 1420, 560, GREEN, size=34, a=ae, anchor="center", bounds=(0, 1920))
        result_box(c, "0,25", 1420, 680, 70, ae, GREEN)
        return
    if sid == "05":
        a0 = ep(t, C["05.t"], 0.5)
        P = _passos_1por3(C)
        # passo k: a linha k ganha o zero, sai um 3 no quociente e a linha k+1 recebe o resto 1
        extra = int(max(0, (t - P[-1]) / 1.1)) if t > P[-1] else 0
        linhas = []
        for k in range(5):
            ar = 1.0 if k == 0 else ep(t, P[k - 1] + 0.9, 0.4) if k - 1 < len(P) else 0
            az = ep(t, P[k], 0.4) if k < len(P) and k < 4 else 0
            linhas.append(("1", ar if k == 0 else ar, az, INK if k == 0 else AMBER))
        n3 = min(5, sum(1 for p in P if t >= p + 0.6) + extra)
        q = ("0," if t >= P[0] else "") + "3" * n3 + ("…" if n3 >= 4 else "")
        chave(c, X0, Y0, linhas, "3", q, ep(t, C["05.t"], 0.5))
        expr(c, "1 ÷ 3", 1420, 300, 90, a0)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            for k in range(1, 5):
                xr = X0 + k * DX - ftext_w("0", "black", DS)
                if linhas[k][1] > 0.5:
                    volta(c, xr - 75, Y0 + k * DY, 24, ad * 0.85, AMBER, t * 0.6 + k * 0.2, 4)
            text(c, "o resto 1 VOLTA SEMPRE", 1460, 440, 38, "black", AMBER, ad)
            volta(c, 1420, 540, 46, ad, AMBER, t * 0.5)
        ae = ep(t, C["05.e"], 0.5)
        pill(c, "NUNCA ACABA", 1420, 650, AMBER, size=34, a=ae, anchor="center", bounds=(0, 1920))
        fmid(c, "0,333…", 1420, 750, 64, "black", PURPLE, ae)
        return
    # 06: os dois nomes
    aa = ep(t, C["06.a"], 0.5)
    expr(c, "1 ÷ 4 = 0,25", 560, 330, 70, aa, cores={4: PURPLE})
    pill(c, "DECIMAL EXATO", 560, 470, BLUE, size=36, a=aa, anchor="center", bounds=(0, 1920))
    text(c, "a divisão acaba", 560, 560, 34, "bold", INK2, aa)
    line(c, W / 2, 220, W / 2, 780, LINE, aa, 3)
    ab = ep(t, C["06.b"], 0.5)
    pos = numero(c, "1 ÷ 3 = 0,333…", 1360, 330, 70, {k: PURPLE for k in range(8, 14)}, ab, align="center")
    pill(c, "DÍZIMA PERIÓDICA", 1360, 470, BLUE, size=36, a=ab, anchor="center", bounds=(0, 1920))
    text(c, "um pedaço se repete para sempre", 1360, 560, 34, "bold", INK2, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        x0, x1 = pos[-1]
        boxed(c, x0 - 10, 280, x1 - x0 + 20, 90, AMBER, acc, 0.10, 14, 4)
        text(c, "“…” = continua igual, sem parar", 1360, 720, 36, "black", AMBER, acc)


# ======================================================================
# bloco A — o 10 e o critério
# ======================================================================

def b_dez(c, t, C, B):
    frame(c, t, B["start"], "DÁ PARA SABER ANTES?", "O SEGREDO DO 10", PURPLE)
    a0 = ep(t, C["07.t"], 0.5)
    text(c, "vai acabar ou vai repetir? dá para saber ANTES de dividir", W / 2, 240, 34, "black", INK2, a0)
    aa = ep(t, C["07.a"], 0.5)
    ab = ep(t, C["07.b"], 0.5)
    expr(c, "10 = 2 × 5", W / 2, 380, 110, aa, cores={2: GREEN, 4: GREEN}, alfas={1: ab, 2: ab, 3: ab, 4: ab})
    acc = ep(t, C["07.c"], 0.5)
    for k, s in enumerate(("10", "100", "1000")):
        chip(c, s, 340 + k * 210, 560, GREEN, acc * ep(t, C["07.c"] + 0.3 * k, 0.4), 44, w=180)
    text(c, "feitos de 2 e 5: CABEM certinho", 1000, 574, 36, "black", GREEN, acc, align="left")
    ad = ep(t, C["07.d"], 0.5)
    for k, s in enumerate(("3", "7", "11")):
        a = ad * ep(t, C["07.d"] + 0.3 * k, 0.4)
        chip(c, s, 340 + k * 210, 720, AMBER, a, 44, w=180)
        check_icon(c, 410 + k * 210, 680, 20, a, RED, "x")
    text(c, "outro primo NÃO cabe: repete", 1000, 734, 36, "black", AMBER, ad, align="left")


# linhas da tabela do critério: fração, fatores (texto, verde?), resultado, exato?
TAB = [("3", "8", [("2", 1), ("2", 1), ("2", 1)], "0,375", True),
       ("7", "20", [("2", 1), ("2", 1), ("5", 1)], "0,35", True),
       ("9", "40", [("2", 1), ("2", 1), ("2", 1), ("5", 1)], "0,225", True),
       ("5", "12", [("2", 1), ("2", 1), ("3", 0)], "0,41666…", False),
       ("2", "7", [("7", 0)], "0,285714…", False)]


def fatores(c, den, fs, x, cy, size, a, align="left"):
    """'12 = 2 × 2 × 3' com 2 e 5 em verde e os outros primos em âmbar"""
    if a <= 0:
        return
    pecas = [(den, INK), ("=", INK)]
    for k, (f, ok) in enumerate(fs):
        if k:
            pecas.append(("×", INK2))
        pecas.append((f, GREEN if ok else AMBER))
    gap = size * 0.3
    ws = [ftext_w(s, "black", size) for s, _ in pecas]
    tot = sum(ws) + gap * (len(ws) - 1)
    xx = x - tot / 2 if align == "center" else x
    for (s, col), w in zip(pecas, ws):
        fmid(c, s, xx, cy, size, "black", col, a, align="left")
        xx += w + gap


def tabela(c, t, cues, x_fr, x_fat, x_res, y0, dy, size=40, cab=True, a_cab=1.0):
    if cab and a_cab > 0:
        for s, x in (("fração", x_fr), ("denominador fatorado", x_fat + 150), ("resultado", x_res + 120)):
            text(c, s, x, y0 - 70, 26, "black", GRAY, a_cab)
    for k, (n_, d_, fs, res, ok) in enumerate(TAB):
        a = ep(t, cues[k], 0.5) if cues[k] is not None else 0
        if a <= 0:
            continue
        y = y0 + k * dy
        fr(c, n_, d_, x_fr, y - size * 0.4, size * 0.8, INK, a)
        fatores(c, d_, fs, x_fat, y, size, a)
        col = GREEN if ok else AMBER
        chip(c, "EXATO" if ok else "DÍZIMA", x_res + 60, y, col, a, 24, w=130)
        fmid(c, res, x_res + 145, y, size * 0.85, "black", col, a, align="left")


def b_criterio(c, t, C, B):
    head_seq(c, t, C, [("08", "A REGRA", "O CRITÉRIO DO DENOMINADOR", PURPLE), ("10", "O ATALHO", "DIVIDA POR 2 E POR 5", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "10"])
    if sid != "10":
        aa = ep(t, C["08.a"], 0.5)
        fmid(c, "com a fração JÁ simplificada, fatore o denominador", W / 2, 215, 32, "black", PURPLE, aa)
        chip(c, "só 2 e 5  →  EXATO", 640, 290, GREEN, ep(t, C["08.b"], 0.5), 34, w=480)
        chip(c, "outro primo  →  DÍZIMA", 1280, 290, AMBER, ep(t, C["08.c"], 0.5), 34, w=520)
        cues = [C["08.d"], C["08.e"], C["09.a"], C["09.b"], C["09.c"]]
        tabela(c, t, cues, 360, 560, 1180, 460, 82, 40, a_cab=ep(t, C["08.d"], 0.5))
        return
    aa = ep(t, C["10.a"], 0.5)
    regra(c, "divida o denominador por 2 e por 5, enquanto der", W / 2, 260, aa, 34, GREEN)

    def cadeia(nums, ops, y, t0, ok):
        xs = [360 + k * 250 for k in range(len(nums))]
        for k, n in enumerate(nums):
            a = ep(t, t0 + 0.45 * k, 0.35)
            ult = k == len(nums) - 1
            col = (GREEN if ok else AMBER) if ult else INK
            if ult and a > 0:
                c.drawCircle(xs[k], y, 62, paint(col, a * 0.15))
                c.drawCircle(xs[k], y, 62, paint(col, a, stroke=4))
            fmid(c, n, xs[k], y, 64, "black", col, a)
            if k < len(ops):
                aa_ = ep(t, t0 + 0.45 * k + 0.25, 0.35)
                arrow(c, xs[k] + 70, y, xs[k + 1] - 70, y, LIGHT, aa_, 4, 14, progress=aa_)
                text(c, ops[k], (xs[k] + xs[k + 1]) / 2, y - 26, 28, "black", GREEN, aa_)
        return xs[-1]

    ab = ep(t, C["10.b"], 0.3)
    if ab > 0:
        xl = cadeia(["40", "20", "10", "5", "1"], ["÷2", "÷2", "÷2", "÷5"], 440, C["10.b"], True)
        a2 = ep(t, C["10.b"] + 2.4, 0.4)
        check_icon(c, xl + 110, 440, 28, a2, GREEN)
        text(c, "ACABA", xl + 150, 454, 40, "black", GREEN, a2, align="left")
    acc = ep(t, C["10.c"], 0.3)
    if acc > 0:
        xl = cadeia(["12", "6", "3"], ["÷2", "÷2"], 650, C["10.c"], False)
        a2 = ep(t, C["10.c"] + 1.4, 0.4)
        text(c, "travou num número diferente de 1:", xl + 110, 640, 34, "black", AMBER, a2, align="left")
        text(c, "DÍZIMA", xl + 110, 690, 40, "black", AMBER, a2, align="left")


# ======================================================================
# bloco B — simplifique antes
# ======================================================================

def b_simplificar(c, t, C, B):
    frame(c, t, B["start"], "ARMADILHA", "SIMPLIFIQUE ANTES", AMBER)
    a0 = ep(t, C["11.t"], 0.5)
    fr(c, "6", "12", 440, 330, 110, INK, a0)
    aa = ep(t, C["11.a"], 0.5)
    ad = ep(t, C["11.d"], 0.5)
    fatores(c, "6", [("2", 1), ("3", 0)], 260, 560, 44, ad)
    fatores(c, "12", [("2", 1), ("2", 1), ("3", 0)], 260, 640, 44, aa)
    text(c, "parece dízima (tem o 3)", 440, 740, 32, "black", AMBER, aa * (1 - ad))
    if ad > 0:
        for (x0, x1, y) in ((426, 474, 560), (522, 570, 640)):
            strike(c, x0 - 6, y + 22, x1 + 6, y - 22, ad, RED, ad)
        text(c, "o 3 cancela com o 3", 440, 740, 32, "black", RED, ad)
    ab = ep(t, C["11.b"], 0.5)
    arrow(c, 590, 380, 790, 380, LIGHT, ab, 6, 18, progress=ab)
    text(c, "÷ 6", 690, 350, 34, "black", GREEN, ab)
    fr(c, "1", "2", 900, 330, 110, BLUE, ab)
    acc = ep(t, C["11.c"], 0.5)
    fmid(c, "= 0,5", 1040, 385, 100, "black", GREEN, acc, align="left")
    pill(c, "DECIMAL EXATO", 1230, 540, GREEN, size=34, a=acc, anchor="center", bounds=(0, 1920))
    regra(c, "o critério só vale na fração IRREDUTÍVEL", 1230, 680, ep(t, C["11.e"], 0.5), 32)


# ======================================================================
# bloco C — anatomia da dízima
# ======================================================================

def b_anatomia(c, t, C, B):
    head_seq(c, t, C, [("12", "POR DENTRO DE UMA DÍZIMA", "PARTE INTEIRA E PERÍODO", BLUE),
                       ("13", "POR DENTRO DE UMA DÍZIMA", "PARTE NÃO PERIÓDICA", BLUE),
                       ("14", "DOIS TIPOS", "SIMPLES E COMPOSTA", BLUE), ("15", "A BOA NOTÍCIA", "A FRAÇÃO GERATRIZ", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14", "15"])
    if sid in ("12", "13"):
        aa = ep(t, C["12.a"], 0.5)
        ab = ep(t, C["12.b"], 0.5)
        acc = ep(t, C["12.c"], 0.5)
        anp = ep(t, C["13.b"], 0.5) if sid == "13" else 0
        cores = {}
        if ab > 0.5:
            cores[0] = INK
        if acc > 0.5:
            cores.update({3: PER, 4: PER, 5: PER, 6: PER, 7: PER, 8: PER, 9: PER})
        if sid == "13" and ep(t, C["13.a"], 0.4) > 0.5:
            cores[2] = NAOP
        pos = numero(c, "2,3454545…", W / 2, 400, 150, cores, aa, align="center")
        chave_sub(c, pos[0][0], pos[0][1], 500, "PARTE INTEIRA", INK, ab, 26)
        if acc > 0:
            chave_sub(c, pos[3][0], pos[4][1], 500, "PERÍODO", PER, acc, 26)
            for k in (5, 7):
                line(c, pos[k][0] + 6, 500, pos[k + 1][1] - 6, 500, PER, acc * 0.6, 4, dash=[10, 8])
            text(c, "o pedaço que se repete", (pos[3][0] + pos[4][1]) / 2 + 160, 640, 30, "bold", PER, acc)
        if sid == "13":
            a13 = ep(t, C["13.a"], 0.5)
            line(c, pos[2][0] + 4, 290, pos[2][1] - 4, 290, NAOP, a13, 5)
            text(c, "não se repete", (pos[2][0] + pos[2][1]) / 2, 260, 30, "black", NAOP, a13 * (1 - anp))
            if anp > 0:
                pill(c, "PARTE NÃO PERIÓDICA", (pos[2][0] + pos[2][1]) / 2, 250, NAOP, size=26, a=anp, anchor="center",
                     bounds=(0, 1920))
                text(c, "entre a vírgula e o período", W / 2, 760, 34, "black", NAOP, anp)
        return
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        numero(c, "0,777…", 320, 330, 100, {2: PER, 3: PER, 4: PER, 5: PER}, aa)
        pill(c, "DÍZIMA SIMPLES", 1000, 320, BLUE, size=34, a=aa, anchor="left", bounds=(0, 1920))
        text(c, "repete logo depois da vírgula", 1000, 400, 32, "bold", INK2, aa, align="left")
        line(c, 220, 500, 1700, 500, LINE, ep(t, C["14.b"], 0.5), 3)
        ab = ep(t, C["14.b"], 0.5)
        numero(c, "0,8333…", 320, 640, 100, {2: NAOP, 3: PER, 4: PER, 5: PER, 6: PER}, ab)
        pill(c, "DÍZIMA COMPOSTA", 1000, 630, BLUE, size=34, a=ab, anchor="left", bounds=(0, 1920))
        text(c, "o 8 não repete: tem parte não periódica", 1000, 710, 32, "bold", INK2, ab, align="left")
        return
    # 15: a mãe da dízima
    aa = ep(t, C["15.a"], 0.5)
    regra(c, "TODA dízima periódica é RACIONAL", W / 2, 250, aa, 36, BLUE)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        boxed(c, 420, 380, 260, 300, PURPLE, ab, 0.08)
        fr(c, "?", "?", 550, 490, 110, PURPLE, ab)
        arrow(c, 720, 530, 1060, 530, PURPLE, ab, 6, 18, progress=ab)
        text(c, "gera", 890, 500, 34, "black", PURPLE, ab)
        numero(c, "0,777…", 1100, 530, 100, {2: PER, 3: PER, 4: PER, 5: PER}, ab)
        pill(c, "FRAÇÃO GERATRIZ", 550, 740, PURPLE, size=30, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["15.c"], 0.5)
    selo(c, 1250, 690, acc, "A MÃE DA DÍZIMA", PURPLE, -5, 36)


# ======================================================================
# blocos D e E — o método algébrico com as fitas
# ======================================================================

YF = (290, 420, 550)          # alturas das fitas (de cima para baixo)
XR = 1510                     # coluna das contas


def b_simples(c, t, C, B):
    head_seq(c, t, C, [("16", "O MÉTODO", "DÍZIMA SIMPLES: 0,777…", PURPLE),
                       ("17", "AS DUAS FITAS", "A CAUDA SOME", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["16", "17"])
    aa = ep(t, C["16.a"], 0.5) if sid == "16" else 1
    acc = ep(t, C["16.c"], 0.5) if sid == "16" else 1
    some = ep(t, C["17.b"], 1.2) if sid == "17" else 0
    fita(c, t, YF[0], "7", "", "7", acc, "10x =", a_cauda=1 - some)
    fita(c, t, YF[1], "0", "", "7", aa, "x =", a_cauda=1 - some)
    if sid == "16":
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            text(c, "× 10", XR, 270, 44, "black", PURPLE, ab)
            text(c, "a vírgula anda", XR, 330, 30, "bold", INK2, ab)
            text(c, "1 casa para a direita", XR, 370, 30, "bold", INK2, ab)
            arrow(c, XR - 90, 410, XR + 90, 410, PURPLE, ab, 5, 16, progress=ab)
        ad = ep(t, C["16.d"], 0.5)
        if ad > 0:
            for y in YF[:2]:
                boxed(c, XV + 12, y - FH / 2 - 12, NC * CW + 80, FH + 24, GREEN, ad, 0.0, 16, 5)
            pill(c, "a MESMA cauda infinita", XV + 300, 660, GREEN, size=34, a=ad, anchor="center", bounds=(0, 1920))
        return
    a17 = ep(t, C["17.a"], 0.5)
    fmid(c, "−", 300, (YF[0] + YF[1]) / 2, 80, "black", RED, a17)
    line(c, 380, 490, 1240, 490, INK, a17, 5)
    fita_some(c, YF[0], 0, prog(t, C["17.b"], 1.0))
    fita_some(c, YF[1], 0, prog(t, C["17.b"], 1.0))
    if some > 0:
        expr(c, "9x =", XV - 16 - CW - 30, 570, 56, some, align="right")
        fmid(c, "7", XV - 16 - CW / 2, 570, 70, "black", GREEN, some)
        pill(c, "a cauda SOME", XV + 300, 570, GREEN, size=34, a=some, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["17.c"], 0.5)
    fmid(c, "10x − x = 9x", XR, 280, 48, "black", INK, acc)
    fmid(c, "7,777… − 0,777… = 7", XR, 360, 36, "black", INK2, acc)
    ad = ep(t, C["17.d"], 0.5)
    fmid(c, "9x = 7", XR, 460, 60, "black", INK, ad)
    text(c, "÷ 9 dos dois lados", XR, 520, 28, "bold", GRAY, ad)
    if ad > 0:
        expr(c, "x = 7/9", XR, 660, 70, ep(t, C["17.d"] + 1.6, 0.5), cores={2: GREEN})
    ae = ep(t, C["17.e"], 0.5)
    check_icon(c, 470, 730, 26, ae, GREEN)
    text(c, "confira: 7 ÷ 9 = 0,777…", 510, 745, 38, "black", GREEN, ae, align="left")


def b_composta(c, t, C, B):
    head_seq(c, t, C, [("18", "O MÉTODO", "DÍZIMA COMPOSTA: 0,8333…", PURPLE),
                       ("19", "AS DUAS FITAS", "A CAUDA SOME DE NOVO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["18", "19"])
    a0 = ep(t, C["18.t"], 0.5) if sid == "18" else 1
    aa = ep(t, C["18.a"], 0.5) if sid == "18" else 1
    ab = ep(t, C["18.b"], 0.5) if sid == "18" else 1
    some = ep(t, C["19.b"] + 0.6, 1.2) if sid == "19" else 0
    sai_x = ep(t, C["19.t"], 0.5) if sid == "19" else 0
    fita(c, t, YF[0], "83", "", "3", ab, "100x =", a_cauda=1 - some)
    fita(c, t, YF[1], "8", "", "3", aa, "10x =", a_cauda=1 - some)
    fita(c, t, YF[2], "0", "8", "3", a0 * (1 - 0.75 * sai_x), "x =", entra=a0)
    if sid == "18":
        apa = ep(t, C["18.a"], 0.5)
        if apa > 0:
            text(c, "× 10", XR, 420, 40, "black", PURPLE, apa)
            text(c, "o 8 pula para antes da vírgula", XR, 470, 26, "bold", INK2, apa)
        if ab > 0:
            text(c, "× 100", XR, 270, 40, "black", PURPLE, ab)
            text(c, "pula também um período", XR, 320, 26, "bold", INK2, ab)
        return
    a19 = ep(t, C["19.a"], 0.5)
    fmid(c, "−", 260, (YF[0] + YF[1]) / 2, 80, "black", RED, a19)
    fita_some(c, YF[0], 0, prog(t, C["19.b"] + 0.6, 1.0))
    fita_some(c, YF[1], 0, prog(t, C["19.b"] + 0.6, 1.0))
    pill(c, "a cauda SOME", XV + 300, 680, GREEN, size=34, a=some, anchor="center", bounds=(0, 1920))
    fmid(c, "100x − 10x = 90x", XR, 270, 44, "black", INK, a19)
    ab_ = ep(t, C["19.b"], 0.5)
    fmid(c, "83 − 8 = 75", XR, 350, 44, "black", INK, ab_)
    acc = ep(t, C["19.c"], 0.5)
    expr(c, "x = 75/90", XR, 470, 60, acc)
    ad = ep(t, C["19.d"], 0.5)
    text(c, "÷ 15 em cima e embaixo", XR, 560, 28, "bold", GRAY, ad)
    expr(c, "= 5/6", XR, 690, 70, ad, cores={1: GREEN})
    ae = ep(t, C["19.e"], 0.5)
    check_icon(c, 430, 770, 26, ae, GREEN)
    text(c, "confira: 5 ÷ 6 = 0,8333…", 470, 785, 38, "black", GREEN, ae, align="left")


# ======================================================================
# bloco F — a regra prática e os atalhos
# ======================================================================

def b_regra(c, t, C, B):
    frame(c, t, B["start"], "A REGRA PRÁTICA", "GERATRIZ EM UM PASSO", PURPLE)
    a0 = ep(t, C["20.t"], 0.5)
    text(c, "o método explica; a regra faz em UM passo", W / 2, 230, 32, "black", INK2, a0)
    aa = ep(t, C["20.a"], 0.5)
    pill(c, "NUMERADOR", 300, 360, PURPLE, size=26, a=aa, anchor="center", bounds=(0, 1920))
    text(c, "o número todo, SEM a vírgula", 480, 352, 40, "black", INK, aa, align="left")
    text(c, "−  a parte que NÃO repete (tudo antes do período)", 480, 412, 34, "black", NAOP, ep(t, C["20.a"] + 1.4, 0.4),
         align="left")
    ab = ep(t, C["20.b"], 0.5)
    line(c, 240, 480, 1680, 480, PURPLE, max(aa, ab), 6)
    pill(c, "DENOMINADOR", 300, 580, PURPLE, size=26, a=ab, anchor="center", bounds=(0, 1920))
    chip(c, "9", 540, 580, PER, ab, 56, w=90)
    text(c, "um 9 para cada algarismo do PERÍODO", 620, 594, 36, "black", PER, ab, align="left")
    acc = ep(t, C["20.c"], 0.5)
    chip(c, "0", 540, 720, NAOP, acc, 56, w=90)
    text(c, "depois, um 0 para cada algarismo NÃO periódico", 620, 734, 36, "black", NAOP, acc, align="left")


def b_atalho_simples(c, t, C, B):
    frame(c, t, B["start"], "O ATALHO", "NOVES EMBAIXO", GREEN)
    for k, (cue, dz, per, n_, d_, nota) in enumerate((("21.a", "0,777…", 4, "7", "9", "1 algarismo repete → um 9"),
                                                     ("21.b", "0,2323…", 4, "23", "99", "2 algarismos repetem → dois 9"))):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        y = 330 + k * 220
        numero(c, dz, 700, y, 90, {i: PER for i in range(2, len(dz))}, a, align="right")
        fmid(c, "=", 770, y, 90, "black", INK, a)
        fr(c, n_, d_, 920, y - 36, 80, INK, a, num_col=PER, den_col=GREEN)
        text(c, nota, 1100, y + 14, 36, "black", GREEN, a, align="left")
    regra(c, "o período em cima, os noves embaixo", W / 2, 760, ep(t, C["21.c"], 0.5), 36, GREEN)


def b_atalho_composta(c, t, C, B):
    frame(c, t, B["start"], "O ATALHO NA COMPOSTA", "GERATRIZ EM UM PASSO", GREEN)
    a0 = ep(t, C["22.t"], 0.5)
    numero(c, "1,2454545…", W / 2, 270, 100, {0: INK, 2: NAOP, 3: PER, 4: PER, 5: PER, 6: PER, 7: PER, 8: PER, 9: PER}, a0,
           align="center")
    aa = ep(t, C["22.a"], 0.5)
    fr(c, "1245 − 12", "990" if ep(t, C["22.b"], 0.4) > 0.5 else "?", 520, 470, 64, INK, aa, num_col=INK)
    text(c, "sem vírgula − antes do período", 520, 640, 26, "bold", GRAY, aa)
    ab = ep(t, C["22.b"], 0.5)
    if ab > 0:
        chip(c, "99 → período de 2 algarismos", 1050, 720, PER, ab, 28, w=520)
        chip(c, "0 → 1 não periódico", 1520, 720, NAOP, ab, 28, w=360)
    aa2 = ep(t, C["22.a"] + 3.0, 0.4)
    fmid(c, "=", 790, 500, 70, "black", INK, aa2)
    fr(c, "1233", "990" if ab > 0.5 else "?", 960, 470, 64, INK, aa2)
    acc = ep(t, C["22.c"], 0.5)
    arrow(c, 1100, 500, 1260, 500, GREEN, acc, 5, 16, progress=acc)
    text(c, "÷ 9", 1180, 470, 32, "black", GREEN, acc)
    fr(c, "137", "110", 1390, 470, 76, GREEN, acc)


# ======================================================================
# bloco G — 0,999… = 1
# ======================================================================

def b_noves(c, t, C, B):
    frame(c, t, B["start"], "A PROVA PROMETIDA", "0,999… = 1", PURPLE)
    aa = ep(t, C["23.a"], 0.5)
    ab = ep(t, C["23.b"], 0.5)
    some = ep(t, C["23.c"] + 0.8, 1.2)
    fita(c, t, YF[0], "9", "", "9", ab, "10x =", a_cauda=1 - some)
    fita(c, t, YF[1], "0", "", "9", aa, "x =", a_cauda=1 - some)
    acc = ep(t, C["23.c"], 0.5)
    fmid(c, "−", 300, (YF[0] + YF[1]) / 2, 80, "black", RED, acc)
    fita_some(c, YF[0], 0, prog(t, C["23.c"] + 0.8, 1.0))
    fita_some(c, YF[1], 0, prog(t, C["23.c"] + 0.8, 1.0))
    pill(c, "a cauda SOME", XV + 300, 540, GREEN, size=34, a=some, anchor="center", bounds=(0, 1920))
    fmid(c, "10x − x = 9x", XR, 280, 48, "black", INK, acc)
    fmid(c, "9x = 9", XR, 370, 60, "black", INK, ep(t, C["23.c"] + 1.6, 0.5))
    ad = ep(t, C["23.d"], 0.5)
    result_box(c, "x = 1", XR, 480, 64, ad, GREEN)
    ae = ep(t, C["23.e"], 0.5)
    text(c, "pela regra:", XR, 575, 30, "bold", GRAY, ae)
    expr(c, "9/9 = 1", XR, 680, 60, ae, cores={2: GREEN})
    af = ep(t, C["23.f"], 0.5)
    pill(c, "não é arredondamento: é o MESMO número, escrito de dois jeitos", W / 2, 770, PURPLE, size=32, a=af,
         anchor="center", bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Denominador só com 2 e 5: acaba. Outro primo: dízima.", "Simplifique antes de aplicar o critério.",
          "Geratriz: 9 para cada algarismo que repete, 0 para cada um que não repete."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["24", "37"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "24" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=GREEN if k == 2 else PURPLE)
        para(c, s, 320, y, 44, "black", INK, a, 1340, 54)


ERROS = [("Aplicar o critério sem simplificar a fração", "o denominador está ali: é só fatorar",
          "um fator pode cancelar: 6/12 = 1/2 = 0,5, exato"),
         ("Achar que dízima periódica é irracional", "ela nunca acaba",
          "ela REPETE: tem fração geratriz, então é racional"),
         ("Parar na geratriz sem simplificar, quando pedem a irredutível", "a fração vale o mesmo",
          "a alternativa sem simplificar está lá, esperando: simplifique até o fim"),
         ("Achar que 0,999… é “quase” 1", "sempre falta um pedacinho",
          "os noves nunca param: não falta nada. 9/9 = 1, exatamente")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["25", "26", "27", "28"], ERROS)


# ======================================================================
# questões
# ======================================================================

NOTA_Q = "Questão no estilo do ENEM, do material de estudo."
NOTA_X = "Questão extra da série (estilo ENEM)"


def enunciado(c, t, C, rows, y=240, a_out=1.0):
    for cue, s, est in rows:
        a = ep(t, C[cue], 0.4) * a_out
        col = BLUE if est == "q" else INK
        y += para(c, s, 190, y, 30, "bold" if est == "q" else "black", col, a, 560, 38) + 14
    return y


ALTS3 = [("A", "1", "", RED), ("B", "2", "", RED), ("C", "3", "", GREEN), ("D", "4", "", RED), ("E", "5", "", RED)]


def b_q3(c, t, C, B):
    head_seq(c, t, C, [("29", "ESTILO ENEM · EU FAÇO COM VOCÊ", "EXATO OU DÍZIMA?", BLUE),
                       ("30", "ESTILO ENEM · EU FAÇO COM VOCÊ", "FATORANDO OS DENOMINADORES", BLUE)])
    card(c, *CARD_R)
    sai = ep(t, C["30.a"], 0.5)
    rows = [("29.a", "Considere as frações 3/8, 5/12, 7/20, 2/7 e 9/40.", "t"),
            ("29.b", "Quantas delas resultam em decimal exato?", "q")]
    enunciado(c, t, C, rows, a_out=1 - sai)
    text(c, NOTA_Q, 190, 830, 18, "medium", GRAY, ep(t, C["29.a"], 0.5), align="left")
    cues_in = {L: C[f"29.{x}"] for L, x in zip("ABCDE", "cdefg")}
    K.alternativas(c, t, C, ALTS3, 1240, 215, 440, 42, C["30.ok"], "C", cues_in, gap=22)
    a0 = ep(t, C["30.t"], 0.5)
    pill(c, "todas já estão irredutíveis", 190, 440, GREEN, size=26, a=a0 * (1 - sai), bounds=(0, 1920))
    if sai > 0:
        cues = [C["30.b"], C["30.c"], C["30.d"], C["30.e"], C["30.f"]]
        orig = [0, 3, 1, 4, 2]      # ordem do enunciado: 3/8, 5/12, 7/20, 2/7, 9/40
        y0, dy = 260, 106
        for k, i in enumerate(orig):
            n_, d_, fs, res, ok = TAB[i]
            a = ep(t, cues[k], 0.5) * sai
            if a <= 0:
                continue
            y = y0 + k * dy
            fr(c, n_, d_, 230, y - 28, 34, INK, a)
            fatores(c, d_, fs, 300, y, 40, a)
            col = GREEN if ok else AMBER
            chip(c, "EXATO" if ok else "DÍZIMA", 890, y, col, a, 24, w=130)
        ag = ep(t, C["30.g"], 0.5)
        if ag > 0:
            result_box(c, "3 exatos", 560, 790, 36, ag, GREEN)


ALTS_S = [("A", "= 5/6", "", GREEN), ("B", "= 83/100", "parou o 3: 0,83", AMBER), ("C", "= 833/999", "repetiu o 833", AMBER),
          ("D", "= 25/3", "", RED), ("E", "= 4/5", "", RED)]


def b_sensor(c, t, C, B):
    head_seq(c, t, C, [("31", "ESTILO ENEM · NÓS FAZEMOS", "O SENSOR", PURPLE),
                       ("33", "DE ONDE VÊM AS ERRADAS?", "O SENSOR", AMBER)])
    card(c, *CARD_R)
    rows = [("31.a", "Um sensor registra uma medida de 0,8333… metro, com o algarismo 3 repetindo indefinidamente.", "t"),
            ("31.b", "Essa medida corresponde exatamente à fração", "q")]
    enunciado(c, t, C, rows)
    text(c, NOTA_X, 190, 830, 18, "medium", GRAY, ep(t, C["31.a"], 0.5), align="left")
    cues_in = {L: C[f"31.{x}"] for L, x in zip("ABCDE", "cdefg")}
    K.alternativas(c, t, C, ALTS_S, 870, 205, 820, 40, C["32.ok"], "A", cues_in, {"B": C["33.a"], "C": C["33.b"]}, gap=12)
    ra = ep(t, C["32.t"], 0.4)
    if ra > 0:
        rrect(c, 170, 520, 620, 290, 18, "#FFFFFF", ra, shadow=True)
        ra2 = ep(t, C["32.a"], 0.4)
        numero(c, "0,8333…", 480, 565, 44, {2: NAOP, 3: PER, 4: PER, 5: PER, 6: PER}, ra, align="center")
        text(c, "8 não repete, 3 repete: COMPOSTA", 480, 630, 26, "black", BLUE, ra2)
        ab = ep(t, C["32.b"], 0.4)
        fr(c, "83 − 8", "90" if ep(t, C["32.c"], 0.4) > 0.5 else "?", 320, 676, 34, INK, ab)
        expr(c, "= 75/90 = 5/6", 560, 700, 44, ep(t, C["32.d"], 0.4), cores={3: GREEN})
        result_box(c, "Letra A", 480, 775, 30, ep(t, C["32.ok"], 0.5), GREEN)


ALTS4 = [("A", "= 1233/990", "não simplificou", AMBER), ("B", "= 137/110", "", GREEN), ("C", "= 1245/999", "", RED),
         ("D", "= 249/200", "", RED), ("E", "= 45/99", "", RED)]


def b_q4(c, t, C, B):
    head_seq(c, t, C, [("34", "ESTILO ENEM · AGORA É COM VOCÊ", "O EQUIPAMENTO", GREEN),
                       ("35", "VAMOS CONFERIR", "O EQUIPAMENTO", GREEN), ("36", "A ARMADILHA", "A LETRA A", AMBER)])
    card(c, *CARD_R)
    rows = [("34.a", "Um equipamento registra a medida 1,2454545…, em que o bloco 45 se repete indefinidamente.", "t"),
            ("34.b", "A fração irredutível correspondente a essa medida é", "q")]
    enunciado(c, t, C, rows)
    text(c, NOTA_Q, 190, 830, 18, "medium", GRAY, ep(t, C["34.a"], 0.5), align="left")
    cues_in = {L: C[f"34.{x}"] for L, x in zip("ABCDE", "cdefg")}
    K.alternativas(c, t, C, ALTS4, 870, 205, 820, 40, C["35.ok"], "B", cues_in, {"A": C["36.b"]}, gap=12)
    pause_timer(c, t, C["34.end"] - 1.9, 470, 680)
    ra = ep(t, C["35.t"], 0.4)
    if ra > 0:
        rrect(c, 170, 520, 620, 290, 18, "#FFFFFF", ra, shadow=True)
        numero(c, "1,2454545…", 480, 565, 44, {2: NAOP, 3: PER, 4: PER, 5: PER, 6: PER, 7: PER, 8: PER, 9: PER}, ra,
               align="center")
        ab = ep(t, C["35.b"], 0.4)
        fr(c, "1245 − 12", "990" if ep(t, C["35.c"], 0.4) > 0.5 else "?", 330, 650, 32, INK, ab)
        expr(c, "= 1233/990", 580, 672, 40, ep(t, C["35.b"] + 2.4, 0.4))
        ad = ep(t, C["35.d"], 0.4)
        text(c, "÷ 3 e ÷ 3 de novo", 330, 790, 24, "bold", GRAY, ad)
        expr(c, "= 137/110", 600, 770, 40, ad, cores={1: GREEN})
        a36 = ep(t, C["36.a"], 0.5)
        if a36 > 0:
            boxed(c, 470, 625, 240, 100, AMBER, a36, 0.06, 14, 4)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A TABELA QUE VALE OURO", PURPLE)
    aa = ep(t, C["38.a"], 0.5)
    for k, (s, tit) in enumerate((("3/8", "FRAÇÃO"), ("0,375", "DECIMAL"), ("37,5%", "PORCENTAGEM"))):
        a = aa * ep(t, C["38.a"] + 0.4 * k, 0.4)
        x = 520 + k * 440
        card(c, x - 180, 250, 360, 300, a)
        pill(c, tit, x, 300, BLUE, size=24, a=a, anchor="center", bounds=(0, 1920))
        expr(c, s, x, 430, 80, a)
        if k < 2:
            fmid(c, "=", x + 220, 430, 70, "black", GRAY, a)
    text(c, "três IDIOMAS do mesmo número", W / 2, 620, 40, "black", PURPLE, aa)
    ab = ep(t, C["38.b"], 0.5)
    text(c, "porcentagem · probabilidade · estatística", W / 2, 690, 34, "bold", INK2, ab)
    pill(c, "ep. 7 · a tabela que vale ouro", W / 2, 780, PURPLE, size=32, a=ep(t, C["38.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["39.like"], C["39.sub"], C["39.bell"], C["39.com"], C["39.bye"], "0,999… era “quase” 1 para você?",
        canal="no Estudativo", anki=C["39.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, dividir=b_dividir, dez=b_dez, criterio=b_criterio,
              simplificar=b_simplificar, anatomia=b_anatomia, simples=b_simples, composta=b_composta, regra=b_regra,
              atalho_simples=b_atalho_simples, atalho_composta=b_atalho_composta, noves=b_noves, recap=b_recap,
              erros=b_erros, q3=b_q3, sensor=b_sensor, q4=b_q4, ponte=b_ponte, cta=b_cta)
