"""Visual — Divisibilidade, Primos, MMC e MDC, Episódio 4: MMC — quando as coisas voltam a coincidir (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Peças próprias deste episódio (reaproveitáveis no ep. 6, "repete × reparte"):
- linha_tempo(): cada coisa que se repete marca seus eventos numa faixa colorida; no MMC as marcas se alinham e acendem juntas.
- varal(): a decomposição simultânea escrita linha por linha (números à esquerda, primo à direita, quem não divide desce igual).
- ícones do cotidiano: ônibus, lâmpada, engrenagem, cápsula de remédio.
Texto matemático com expoente ^ e símbolos: ftext/fmid do ep. 1 da série 010.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_ROOT = Path(__file__).resolve().parents[3]          # canais/enem


def _load(nome, rel):
    sp = importlib.util.spec_from_file_location(nome, _ROOT / rel)
    mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
    return mod


M = _load("v010_ep1", "010_enem_matematica_conjuntos/ep1_ordem_e_sinais/roteiro/visual.py")      # ftext, fbox, regra
V2 = _load("v014_ep2", "014_enem_redacao_leitura_proposta/ep2_frase_tematica_blocos/roteiro/visual.py")  # alternativas
V1 = V2.V1
motor.set_theme("claro")

ftext, fmid, ftext_w, fbox, regra = M.ftext, M.fmid, M.ftext_w, M.fbox, M.regra
pause_timer, which, para, wrap, frame, head_seq, boxed, selo = (V1.pause_timer, V1.which, V1.para, V1.wrap, V1.frame,
                                                                 V1.head_seq, V1.boxed, V1.selo)
alts_panel = V2.alts_panel

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisibilidade_ep4_mmc.mp4"
CARD_R = (140, 150, 1640, 690)

COR_A, COR_B, COR_C = "#3B6CF6", "#F97316", "#16A36A"   # as três "coisas que se repetem"
GLOW = "#E8A317"


# ======================================================================
# ícones do cotidiano
# ======================================================================

def onibus(c, cx, cy, s, a, col=COR_A):
    if a <= 0:
        return
    rrect(c, cx - 60 * s, cy - 34 * s, 120 * s, 62 * s, 12 * s, col, a, shadow=True)
    for k in range(3):
        rrect(c, cx - 50 * s + k * 34 * s, cy - 26 * s, 26 * s, 22 * s, 4 * s, "#DCEBFF", a)
    for wx in (cx - 34 * s, cx + 34 * s):
        c.drawCircle(wx, cy + 30 * s, 11 * s, paint(INK, a))
        c.drawCircle(wx, cy + 30 * s, 4 * s, paint(LIGHT, a))


def lampada(c, cx, cy, s, a, col=GLOW, on_=1.0):
    if a <= 0:
        return
    if on_ > 0:
        c.drawCircle(cx, cy - 10 * s, 52 * s, paint(col, a * 0.25 * on_))
    c.drawCircle(cx, cy - 10 * s, 32 * s, paint(mix("#E5E5E0", col, on_), a))
    rrect(c, cx - 16 * s, cy + 18 * s, 32 * s, 26 * s, 5 * s, INK2, a)
    for k in range(2):
        line(c, cx - 16 * s, cy + 26 * s + k * 9 * s, cx + 16 * s, cy + 26 * s + k * 9 * s, LIGHT, a, 2 * s)


def engrenagem(c, cx, cy, s, a, col=PURPLE, ang=0.0):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    for k in range(8):
        c.save(); c.rotate(k * 45)
        rrect(c, -9 * s, -46 * s, 18 * s, 18 * s, 3 * s, col, a)
        c.restore()
    c.drawCircle(0, 0, 34 * s, paint(col, a))
    c.drawCircle(0, 0, 12 * s, paint("#FFFFFF", a))
    c.restore()


def capsula(c, cx, cy, s, a, col=RED):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(-30)
    rrect(c, -50 * s, -20 * s, 100 * s, 40 * s, 20 * s, "#FFFFFF", a, shadow=True)
    c.save(); c.clipRect(skia.Rect.MakeLTRB(-50 * s, -20 * s, 0, 20 * s))
    rrect(c, -50 * s, -20 * s, 100 * s, 40 * s, 20 * s, col, a)
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-50 * s, -20 * s, 100 * s, 40 * s), 20 * s, 20 * s),
                paint(INK2, a * 0.5, stroke=2))
    c.restore()


# ======================================================================
# linha do tempo: cada série marca seus eventos; o reencontro acende
# ======================================================================

def linha_tempo(c, t, x0, y, w, tmax, series, coinc=(), coinc_a=0.0, unit="h", tick=None, a=1.0, row_h=74,
                label_w=210):
    """series = [dict(step, col, label, reveal 0..1, a)] · coinc = valores em que todas coincidem (acendem)
    · tick = espaçamento das marcas do eixo (padrão = menor step)"""
    if a <= 0:
        return
    xa = x0 + label_w
    wa = w - label_w
    X = lambda v: xa + wa * v / tmax
    n = len(series)
    y_axis = y + n * row_h + 10
    # faixas
    for i, sr in enumerate(series):
        sa = a * sr.get("a", 1.0)
        if sa <= 0:
            continue
        yy = y + i * row_h + row_h / 2
        rrect(c, x0, yy - 26, label_w - 20, 52, 14, mix("#FFFFFF", sr["col"], 0.14), sa)
        text_mid(c, sr["label"], x0 + (label_w - 20) / 2, yy, 24, "black", sr["col"], sa)
        line(c, xa, yy, xa + wa, yy, LINE, sa, 3)
        k = 1
        ks = []
        while sr["step"] * k <= tmax + 1e-9:
            ks.append(k); k += 1
        shown = sr.get("reveal", 1.0) * len(ks)
        for j, k in enumerate(ks):
            r = clamp(shown - j)
            if r <= 0:
                break
            v = sr["step"] * k
            hit = v in coinc and coinc_a > 0
            rad = 13 * (0.6 + 0.4 * ease_back(r))
            if hit:
                c.drawCircle(X(v), yy, rad + 12 * coinc_a, paint(GLOW, sa * 0.35 * coinc_a))
            c.drawCircle(X(v), yy, rad, paint(sr["col"], sa * r))
    # eixo
    line(c, xa, y_axis, xa + wa, y_axis, INK2, a, 3)
    tick = tick or min(sr["step"] for sr in series)
    v = 0
    while v <= tmax + 1e-9:
        line(c, X(v), y_axis - 6, X(v), y_axis + 6, INK2, a, 2)
        big_ = v in coinc and coinc_a > 0
        text(c, f"{v:g}", X(v), y_axis + 34, 24 if not big_ else 30, "black" if big_ else "bold",
             GLOW if big_ else GRAY, a)
        v += tick
    text(c, unit, xa + wa + 22, y_axis + 8, 22, "bold", GRAY, a, align="left")
    # colunas de reencontro
    for v in coinc:
        if coinc_a <= 0:
            continue
        rrect(c, X(v) - 22, y - 6, 44, n * row_h + 16, 18, GLOW, a * 0.12 * coinc_a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(X(v) - 22, y - 6, 44, n * row_h + 16), 18, 18),
                    paint(GLOW, a * coinc_a, stroke=3))


# ======================================================================
# varal da decomposição simultânea
# ======================================================================

def varal(c, x, y, rows, shown, a=1.0, size=40, lh=62, colw=110, final=None, final_a=0.0, hl=None):
    """rows = [([números], primo)] · shown = linhas reveladas (float) · final = texto do produto da coluna da direita"""
    if a <= 0:
        return
    n = len(rows[0][0])
    xbar = x + n * colw + 20
    for i, (nums, p) in enumerate(rows + [([1] * n, None)]):
        r = clamp(shown - i)
        if r <= 0:
            break
        yy = y + i * lh
        for j, v in enumerate(nums):
            prev = rows[i - 1][0][j] if i > 0 else None
            pdiv = rows[i - 1][1] if i > 0 else None
            desceu = i > 0 and prev % pdiv != 0
            col = GRAY if (v == 1 and i > 0) else (AMBER if desceu else INK)
            fmid(c, str(v), x + j * colw + colw / 2, yy, size, "black", col, a * r)
        if p is not None:
            fmid(c, str(p), xbar + 50, yy, size, "black", PURPLE, a * r)
        if hl is not None and i == hl:
            rrect(c, x - 10, yy - lh / 2 + 4, n * colw + 20, lh - 8, 12, AMBER, a * 0.12)
    nlin = min(len(rows) + 1, math.ceil(shown))
    line(c, xbar, y - lh / 2, xbar, y - lh / 2 + max(1, nlin) * lh, INK2, a, 4)
    if final and final_a > 0:
        fbox(c, final, x + (n * colw + 120) / 2, y + (len(rows) + 1) * lh + 40, size * 0.9, final_a, GREEN)


ROWS = [([12, 18, 30], 2), ([6, 9, 15], 2), ([3, 9, 15], 3), ([1, 3, 5], 3), ([1, 1, 5], 5)]   # pelo macete


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "QUANDO VOLTAM A COINCIDIR?", BLUE)
    card(c, *CARD_R)
    items = [("01.a", onibus, "ônibus"), ("01.b", lampada, "lâmpadas"), ("01.c", engrenagem, "engrenagens"), ("01.d", capsula, "remédios")]
    for k, (cue, fn, nm) in enumerate(items):
        a, d = rise(t, C[cue])
        cx = 380 + k * 390
        if fn is engrenagem:
            fn(c, cx, 290 + d, 1.3, a, PURPLE, 40 * t)
        elif fn is lampada:
            fn(c, cx, 290 + d, 1.3, a, GLOW, 0.5 + 0.5 * math.sin(t * 5))
        else:
            fn(c, cx, 290 + d, 1.3, a)
        text(c, nm, cx, 400 + d, 30, "black", INK2, a)
    ae = ep(t, C["01.e"], 0.5)
    series = [dict(step=2, col=COR_A, label="a cada 2", reveal=prog(t, C["01.d"], 2.5)),
              dict(step=3, col=COR_B, label="a cada 3", reveal=prog(t, C["01.d"] + 0.5, 2.5))]
    linha_tempo(c, t, 300, 470, 1320, 13, series, coinc=(6, 12), coinc_a=ae, unit="s", tick=1,
                a=ep(t, C["01.d"], 0.5), row_h=64)
    pill(c, "vale ponto quase todo ano", W / 2, 780, GREEN, size=28, a=ep(t, C["01.f"], 0.4), anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "calcular o MMC de 3 jeitos", ["linha do tempo", "varal (atalho)", "receita"]),
            ("02.b", "não cair no “QUANTAS VEZES”", [])]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 230 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 56, "black", INK, a, align="left")
        for k, ss in enumerate(sub):
            pill(c, ss, 410 + k * 270, y + 80, BLUE, size=26, a=a * ep(t, C[cue] + 0.5 + 0.3 * k, 0.3), bounds=(0, 1920))


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRANDO", "EM 30 SEGUNDOS", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    text(c, "MÚLTIPLO = a tabuada", 560, 250, 40, "black", BLUE, aa)
    for k, v in enumerate((6, 12, 18, 24)):
        a = ep(t, C["03.a"] + 0.4 + 0.25 * k, 0.3)
        c.drawCircle(300 + k * 150, 380, 48, paint(mix("#FFFFFF", BLUE, 0.14), a))
        fmid(c, str(v), 300 + k * 150, 380, 38, "black", INK, a)
    text(c, "... não acabam", 560, 490, 28, "bold", GRAY, ep(t, C["03.a"] + 1.6, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    text(c, "FATORAR = a receita", 1360, 250, 40, "black", PURPLE, ab)
    text(c, "quais primos (tijolos) e quantos de cada", 1360, 310, 26, "bold", INK2, ab)
    fbox(c, "12 = 2^2 · 3", 1360, 420, 56, ep(t, C["03.c"], 0.4), PURPLE)
    line(c, W / 2, 220, W / 2, 620, LINE, max(aa, ab), 2)


# ======================================================================
# bloco A: a linha do tempo dos remédios
# ======================================================================

def b_remedios(c, t, C, B):
    sid = which(t, C, ["04", "05", "06"])
    head_seq(c, t, C, [("04", "UMA PERGUNTA", "QUANDO JUNTOS DE NOVO?", BLUE), ("05", "NA LINHA DO TEMPO", "AS TABUADAS CRESCEM", BLUE),
                       ("06", "O PRIMEIRO ENCONTRO", "É O REENCONTRO", GREEN)])
    card(c, *CARD_R)
    if sid == "04":
        aa, ab = ep(t, C["04.a"], 0.5), ep(t, C["04.b"], 0.5)
        capsula(c, 560, 330, 1.6, aa, COR_A)
        text(c, "de 6 em 6 horas", 560, 460, 40, "black", COR_A, aa)
        capsula(c, 1360, 330, 1.6, ab, COR_B)
        text(c, "de 8 em 8 horas", 1360, 460, 40, "black", COR_B, ab)
        text(c, "juntos de novo... quando?", W / 2, 580, 44, "black", INK, ep(t, C["04.c"], 0.4))
        pill(c, "INTERVALO = o tempo entre uma vez e a próxima", W / 2, 700, BLUE, size=28, a=ep(t, C["04.d"], 0.4), anchor="center")
        return
    tmax = 26 if sid == "05" else lerp(26, 74, ease_out(prog(t, C["06.a"], 1.2)))
    series = [dict(step=6, col=COR_A, label="6 em 6 h", reveal=prog(t, C["05.a"], 2.6) if sid == "05" else 1.0),
              dict(step=8, col=COR_B, label="8 em 8 h", reveal=prog(t, C["05.b"], 2.0) if sid == "05" else 1.0)]
    co = (24,) if sid == "05" else (24, 48, 72)
    ca = ep(t, C["05.c"], 0.5) if sid == "05" else 1.0
    linha_tempo(c, t, 220, 260, 1480, tmax, series, coinc=co, coinc_a=ca, unit="h",
                tick=2 if sid == "05" else 6)
    if sid == "05":
        pill(c, "24 h: juntos de novo", W / 2, 640, GLOW, size=32, a=ep(t, C["05.d"], 0.4), anchor="center")
    else:
        pill(c, "MÚLTIPLOS COMUNS: 24, 48, 72...", W / 2, 620, BLUE, size=30, a=ep(t, C["06.b"], 0.4), anchor="center")
        pill(c, "o primeiro = o REENCONTRO", W / 2, 710, GREEN, size=30, a=ep(t, C["06.c"], 0.4), anchor="center")


def b_luzes(c, t, C, B):
    frame(c, t, B["start"], "QUALQUER COISA QUE SE REPETE", "LUZES DE NATAL", GREEN)
    aa, ab = ep(t, C["06b.a"], 0.4), ep(t, C["06b.b"], 0.4)
    coinc_on = ep(t, C["06b.e"], 0.3)
    tt = t - C["06b.a"]
    on1 = 1.0 if (int(tt * 2) % 2 == 0) else 0.2
    lampada(c, 520, 320, 1.4, aa, COR_A, max(on1, coinc_on))
    text(c, "a cada 2 s", 520, 440, 34, "black", COR_A, aa)
    on2 = 1.0 if (int(tt * 1.5) % 2 == 0) else 0.2
    lampada(c, 1400, 320, 1.4, ab, COR_B, max(on2, coinc_on))
    text(c, "a cada 3 s", 1400, 440, 34, "black", COR_B, ab)
    series = [dict(step=2, col=COR_A, label="2 em 2 s", reveal=prog(t, C["06b.c"], 1.5), a=aa),
              dict(step=3, col=COR_B, label="3 em 3 s", reveal=prog(t, C["06b.d"], 1.0), a=ab)]
    linha_tempo(c, t, 260, 500, 1400, 7, series, coinc=(6,), coinc_a=coinc_on, unit="s", tick=1, row_h=60)


# ======================================================================
# bloco B: definição
# ======================================================================

def b_definicao(c, t, C, B):
    sid = which(t, C, ["07", "08"])
    head_seq(c, t, C, [("07", "O NOME DO REENCONTRO", "MMC", BLUE), ("08", "E O ZERO?", "NÃO CONTA", AMBER)])
    card(c, *CARD_R)
    if sid == "07":
        a0 = ep(t, C["07.t"], 0.5)
        letras = [("M", "MÍNIMO", "o menor", "07.a"), ("M", "MÚLTIPLO", "a tabuada", "07.b"), ("C", "COMUM", "de todos", "07.b")]
        for k, (L, w1, w2, cue) in enumerate(letras):
            a = ep(t, C[cue] + (0.5 if k == 2 else 0), 0.4) if k else ep(t, C[cue], 0.4)
            x = 520 + k * 440
            text(c, L, x, 330, 120, "black", BLUE, a0)
            text(c, w1, x, 400, 30, "black", INK, a)
            text(c, w2, x, 445, 26, "bold", GRAY, a)
        ac = ep(t, C["07.c"], 0.5)
        boxed(c, 300, 520, 1320, 150, BLUE, ac, 0.07)
        text(c, "DEFINIÇÃO", 340, 562, 18, "black", BLUE, ac, align="left", tracking=2)
        text(c, "o menor número, diferente de zero, múltiplo de todos os dados", W / 2, 625, 36, "black", INK, ac)
        return
    series = [dict(step=6, col=COR_A, label="6 em 6 h"), dict(step=8, col=COR_B, label="8 em 8 h")]
    linha_tempo(c, t, 220, 260, 1480, 26, series, coinc=(24,), coinc_a=ep(t, C["08.b"], 0.4), unit="h", tick=2)
    aa = ep(t, C["08.a"], 0.4)
    if aa > 0:
        # o zero é a largada: destaque âmbar no início do eixo
        rrect(c, 220 + 210 - 26, 250, 52, 170, 18, AMBER, aa * 0.15)
        pill(c, "0 = a largada (não conta)", 520, 560, AMBER, size=28, a=aa, anchor="center")
    fbox(c, "MMC(6, 8) = 24", W / 2, 690, 54, ep(t, C["08.c"], 0.4), GREEN)


# ======================================================================
# bloco C: o atalho — o varal (decomposição simultânea)
# ======================================================================

def rows_varal(nums, primos=(2, 3, 5, 7)):
    """linhas do varal pelo macete: menor primo primeiro, repete enquanto dividir alguém"""
    rows, cur = [], list(nums)
    for p in primos:
        while any(v % p == 0 for v in cur):
            rows.append((cur[:], p))
            cur = [v // p if v % p == 0 else v for v in cur]
    return rows


def varal_anim(c, t, x, y, rows, marks, size=46, lh=66, colw=130, final=None, final_cue=None, glow=None):
    """varal revelado linha a linha (marks = instantes de cada linha) com a coluna dos primos acendendo em verde"""
    shown = sum(ep(t, m, 0.5) for m in marks)
    varal(c, x, y, rows, shown, 1.0, size=size, lh=lh, colw=colw, final=final,
          final_a=ep(t, final_cue, 0.4) if final_cue is not None else 0.0)
    if glow is not None:
        n = len(rows[0][0])
        g = ep(t, glow, 0.4)
        bx = x + n * colw + 30
        rrect(c, bx, y - lh / 2 + 2, 90, lh * len(rows) - 4, 16, GREEN, 0.16 * g)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, y - lh / 2 + 2, 90, lh * len(rows) - 4), 16, 16),
                    paint(GREEN, g, stroke=3))


def b_atalho(c, t, C, B):
    frame(c, t, B["start"], "O ATALHO DA PROVA", "FATORAR TODOS JUNTOS", GREEN)
    aa = ep(t, C["09.a"], 0.5)
    fmid(c, "72 = ...", 470, 300, 44, "black", GRAY, aa * 0.8)
    fmid(c, "120 = ...", 470, 380, 44, "black", GRAY, aa * 0.8)
    text(c, "um de cada vez", 470, 470, 28, "bold", GRAY, aa)
    arrow(c, 760, 360, 980, 360, GREEN, aa, 6, 20, progress=aa)
    varal(c, 1060, 300, [([72, 120], 2), ([36, 60], 2)], 1.4 * aa, aa, size=44, lh=66, colw=130)
    text(c, "todos no mesmo varal", 1290, 470, 30, "black", GREEN, aa)
    ab = ep(t, C["09.b"], 0.5)
    boxed(c, 360, 560, 1200, 130, BLUE, ab, 0.07)
    text(c, "DECOMPOSIÇÃO SIMULTÂNEA", W / 2, 615, 36, "black", BLUE, ab)
    text(c, "simultânea = ao mesmo tempo", W / 2, 662, 28, "bold", INK2, ab)


R68 = rows_varal([6, 8])
R72 = rows_varal([72, 120])
R410 = rows_varal([4, 10])


def b_varal68(c, t, C, B):
    frame(c, t, B["start"], "EU FAÇO NO VARAL", "MMC(6, 8)", GREEN)
    marks = [C["10.a"], C["10.b"], C["10.c"], C["10.d"], C["10.e"]]
    varal_anim(c, t, 520, 250, R68, marks, size=50, lh=74, colw=140, final="2 · 2 · 2 · 3 = 24", final_cue=C["10.f"],
               glow=C["10.f"])
    if C["10.c"] <= t < C["10.d"] + 0.8:
        pill(c, "o 3 não divide por 2: desce igual", 1380, 400, AMBER, size=26, a=ep(t, C["10.c"], 0.4), anchor="center",
             bounds=(0, 1920))
    pill(c, "o mesmo reencontro da linha do tempo!", 1380, 560, GREEN, size=26, a=ep(t, C["10.g"], 0.4), anchor="center",
         bounds=(0, 1920))


MACETES = [("11.a", "comece pelo MENOR primo: o 2"), ("11.b", "repita o primo enquanto ele dividir ALGUÉM"),
           ("11.c", "quem não divide DESCE IGUAL"), ("11.d", "pare só quando a linha for toda de 1")]


def b_macetes(c, t, C, B):
    frame(c, t, B["start"], "4 MACETES", "VARAL SEM ERRO", GREEN)
    for k, (cue, s) in enumerate(MACETES):
        a, d = rise(t, C[cue])
        y = 290 + k * 130 + d
        badge_num(c, k + 1, 300, y - 14, a, 34, bg=GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")


def b_varal72(c, t, C, B):
    frame(c, t, B["start"], "EU FAÇO NO VARAL", "MMC(72, 120)", GREEN)
    marks = [C["12.t"] + 0.3, C["12.a"], C["12.b"], C["12.c"], C["12.d"], C["12.e"], C["12.f"]]
    varal_anim(c, t, 330, 215, R72, marks, size=42, lh=62, colw=130, glow=C["12.g"])
    fbox(c, "2 · 2 · 2 · 3 · 3 · 5 = 360", 1300, 330, 46, ep(t, C["12.g"], 0.4), GREEN)
    fmid(c, "360 ÷ 72 = 5 ✓", 1300, 470, 40, "black", GREEN, ep(t, C["12.h"], 0.4))
    fmid(c, "360 ÷ 120 = 3 ✓", 1300, 550, 40, "black", GREEN, ep(t, C["12.h"] + 1.2, 0.4))
    pill(c, "os dois cabem dentro dele", 1300, 650, GREEN, size=26, a=ep(t, C["12.h"] + 2.4, 0.4), anchor="center",
         bounds=(0, 1920))


def b_porque(c, t, C, B):
    frame(c, t, B["start"], "POR QUE O VARAL FUNCIONA?", "A RECEITA DE TODOS DE UMA VEZ", PURPLE)
    ab = ep(t, C["14b.b"], 0.4)
    fmid(c, "72 = 2^3 · 3^2", 520, 280, 50, "black", INK, ab)
    fmid(c, "120 = 2^3 · 3 · 5", 520, 370, 50, "black", INK, ep(t, C["14b.b"] + 1.5, 0.4))
    regra(c, "TODOS os fatores, com o MAIOR expoente", W / 2, 480, ep(t, C["14b.c"], 0.5), 40)
    ad = ep(t, C["14b.d"], 0.4)
    text(c, "o múltiplo comum precisa CONTER cada número: nenhum tijolo pode faltar", W / 2, 580, 28, "black", INK2, ad)
    ae = ep(t, C["14b.e"], 0.4)
    fbox(c, "2^3 · 3^2 · 5 = 360", 520, 690, 46, ae, PURPLE)
    text(c, "= a coluna do varal: 2 · 2 · 2 · 3 · 3 · 5", 1260, 702, 32, "black", GREEN, ae)
    pill(c, "próximo episódio: o MESMO varal dá o MDC", 1300, 300, BLUE, size=24, a=ep(t, C["14b.f"], 0.4), anchor="center",
         bounds=(0, 1920))


def b_nosfazemos(c, t, C, B):
    frame(c, t, B["start"], "SUA VEZ", "MMC(4, 10) NO VARAL", GREEN)
    fbox(c, "MMC(4, 10) = ?", 560, 250, 60, ep(t, C["12b.a"], 0.4), BLUE)
    pause_timer(c, t, C["12b.p"] + 0.3, 1500, 270)
    bb = C["12b.b"]
    varal_anim(c, t, 380, 380, R410, [bb, bb + 1.2, bb + 2.4, bb + 3.4], size=46, lh=66, colw=130, glow=C["12b.c"])
    fbox(c, "2 · 2 · 5 = 20", 560, 700, 50, ep(t, C["12b.c"], 0.4), GREEN)
    ad = ep(t, C["12b.d"], 0.4)
    for k, v in enumerate((4, 8, 12, 16, 20)):
        fmid(c, str(v), 1060 + k * 120, 470, 44, "black", GLOW if v == 20 else COR_A, ad * ep(t, C["12b.d"] + 0.3 * k, 0.3))
    for k, v in enumerate((10, 20)):
        fmid(c, str(v), 1300 + k * 240, 580, 44, "black", GLOW if v == 20 else COR_B, ad * ep(t, C["12b.d"] + 1.8 + 0.3 * k, 0.3))
    text(c, "tabuada do 4", 960, 420, 22, "bold", COR_A, ad, align="left")
    text(c, "tabuada do 10", 960, 530, 22, "bold", COR_B, ad, align="left")


# ======================================================================
# bloco D: decomposição simultânea
# ======================================================================

def b_varal(c, t, C, B):
    head_seq(c, t, C, [("13", "TRÊS NÚMEROS?", "O VARAL É IGUAL", GREEN), ("14", "COLUNA DA DIREITA", "MMC(12, 18, 30)", GREEN)])
    card(c, *CARD_R)
    marks = [C["13.b"], C["13.c"], C["13.d"], C["14.a"], C["14.b"], C["14.c"]]
    varal_anim(c, t, 360, 250, ROWS, marks, size=46, lh=72, colw=130, final="2 · 2 · 3 · 3 · 5 = 180", final_cue=C["14.e"],
               glow=C["14.d"])
    pill(c, "é aí que o varal mais economiza tempo", 1380, 230, GREEN, size=24, a=ep(t, C["13.a"], 0.4), anchor="center",
         bounds=(0, 1920))
    if C["13.d"] <= t < C["14.a"] + 0.8:
        pill(c, "o 6 ainda é par: 2 de novo", 1380, 420, AMBER, size=26, a=ep(t, C["13.d"], 0.4), anchor="center", bounds=(0, 1920))
        pill(c, "9 e 15 descem iguais", 1380, 500, AMBER, size=26, a=ep(t, C["13.d"] + 1.5, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# blocos E, F, G: reconhecer, sanidade, quantas vezes
# ======================================================================

def b_reconhecer(c, t, C, B):
    frame(c, t, B["start"], "COMO RECONHECER", "AS PALAVRAS DO ENUNCIADO", GREEN)
    frases = [("15.a", "“voltarão a coincidir”"), ("15.b", "“ao mesmo tempo novamente”"), ("15.c", "“juntos de novo”"),
              ("15.d", "“de quanto em quanto tempo se encontram”")]
    for k, (cue, s) in enumerate(frases):
        a, d = rise(t, C[cue])
        x = 560 if k % 2 == 0 else 1360
        y = 290 + (k // 2) * 150 + d
        rrect(c, x - 360, y - 50, 720, 100, 18, mix("#FFFFFF", GREEN, 0.10), a)
        text_mid(c, s, x, y, 32, "black", INK, a)
    fbox(c, "se repete e se reencontra → MMC", W / 2, 680, 48, ep(t, C["15.e"], 0.4), GREEN)


def b_sanidade(c, t, C, B):
    frame(c, t, B["start"], "CHECAGEM RÁPIDA", "O MMC NUNCA É MENOR", GREEN)
    regra(c, "MMC  ≥  maior dos números dados", W / 2, 270, ep(t, C["16.a"], 0.5), 46)
    text(c, "o reencontro não vem antes da volta mais lenta", W / 2, 390, 32, "black", INK2, ep(t, C["16.b"], 0.4))
    for k, (cue, s) in enumerate((("16.c", "180 ≥ 30 ✓"), ("16.d", "360 ≥ 120 ✓"))):
        fbox(c, s, 640 + k * 640, 560, 54, ep(t, C[cue], 0.4), GREEN)


def b_quantas(c, t, C, B):
    frame(c, t, B["start"], "A PEGADINHA MAIS FAMOSA", "QUANDO × QUANTAS VEZES", AMBER)
    aa = ep(t, C["17.a"], 0.4)
    series = [dict(step=6, col=COR_A, label="6 em 6 h"), dict(step=8, col=COR_B, label="8 em 8 h")]
    ab = ep(t, C["17.b"], 0.4)
    tmax = lerp(26, 74, ease_out(prog(t, C["17.b"], 1.0)))
    linha_tempo(c, t, 220, 200, 1480, tmax, series, coinc=(24, 48, 72), coinc_a=aa, unit="h", tick=6, row_h=64)
    pill(c, "QUANDO? a cada 24 h = MMC", 560, 470, BLUE, size=28, a=aa * (1 - ab * 0.4), anchor="center", bounds=(0, 1920))
    pill(c, "QUANTAS VEZES em 3 dias?", 1360, 470, AMBER, size=28, a=ab, anchor="center", bounds=(0, 1920))
    fmid(c, "3 dias = 72 h", 1360, 560, 40, "black", INK, ep(t, C["17.c"], 0.4))
    fbox(c, "72 ÷ 24 = 3 vezes", 1360, 660, 46, ep(t, C["17.d"], 0.4), GREEN)
    af = ep(t, C["17.f"], 0.4)
    pill(c, "a largada (0) não conta", 560, 560, AMBER, size=24, a=af, anchor="center", bounds=(0, 1920))
    pill(c, "MMC é o meio do caminho: ainda falta DIVIDIR", W / 2, 790, PURPLE, size=28, a=ep(t, C["17.e"], 0.4), anchor="center")


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Coisas que se repetem e se reencontram: MMC.", "Todos os fatores, maior expoente.",
          "Pediram “quantas vezes”? Ainda falta dividir."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 50, "black", INK, a, align="left")


ERROS = [("19", "Usar só os fatores COMUNS", "MMC(72, 120) = 2^3 · 3 = 24", "a palavra “comum” está no nome",
          "24 < 120: a checagem denuncia. Use TODOS os fatores"),
         ("20", "Achar o MMC e PARAR", "“quantas vezes?” → responde o MMC", "a conta difícil já foi feita",
          "quantas vezes = intervalo ÷ MMC"),
         ("21", "Esquecer de CONVERTER as unidades", "180 min ≠ 1 h 80", "os números estão todos ali",
          "minuto, hora e segundo não se misturam: 180 min = 3 h")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, ex, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(3):
        badge_num(c, k + 1, 880 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 320, 34, aa, RED, "x")
    text(c, err, 360, 335, 46, "black", RED, aa, align="left")
    ftext(c, ex, 360, 405, 34, "bold", INK2, ep(t, cue("a") + 0.8, 0.4), align="left")
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 500, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 575, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 690, 34, ac, GREEN)
    text(c, fix, 360, 705, 38, "black", GREEN, ac, align="left")


# ======================================================================
# questões 1 e 5
# ======================================================================

Q1 = ("Três linhas de ônibus partem do mesmo terminal. A linha A parte a cada 12 minutos, a linha B a cada 18 minutos e a "
      "linha C a cada 30 minutos. Se as três partiram juntas às 6h, a que horas voltarão a partir juntas pela primeira vez?")
ALT1 = [("A", "7h", "22.d", "24.x", "somou os intervalos: 12 + 18 + 30 = 60 min", RED),
        ("B", "8h", "22.e", "24.ok", "não é 6h + 3h", RED),
        ("C", "9h", "22.f", None, "", GREEN),
        ("D", "10h", "22.g", "24.ok", "não é 6h + 3h", RED),
        ("E", "12h", "22.h", "24.ok", "não é 6h + 3h", RED)]


def b_q1(c, t, C, B):
    sid = which(t, C, ["22", "23", "24"])
    head(c, t, B["start"], "QUESTÃO 1", "TRÊS LINHAS DE ÔNIBUS", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["22.a"], 0.5)
    res = ep(t, C["23"], 0.5)
    para(c, Q1, 180, 240, 26, "bold", INK, a * (1 - res), 560, 34)
    for k, (cue, col) in enumerate((("22.b", COR_A), ("22.b", COR_B), ("22.b", COR_C))):
        onibus(c, 280 + k * 180, 640, 0.9, ep(t, C[cue] + 0.3 * k, 0.4) * (1 - res), col)
    if res > 0:
        pill(c, "voltar a partir juntas → MMC", 440, 230, GREEN, size=24, a=ep(t, C["23.a"], 0.4), anchor="center", bounds=(0, 1920))
        varal(c, 200, 330, ROWS, 6 * ep(t, C["23.f"], 0.6), 1.0, size=30, lh=46, colw=78)
        rrect(c, 200 + 3 * 78 + 30, 330 - 23, 70, 46 * 5, 12, GREEN, 0.16 * ep(t, C["23.g"], 0.4))
        ftext(c, "2·2·3·3·5 = 180 min", 190, 660, 34, "black", GREEN, ep(t, C["23.c"], 0.4), align="left")
        ftext(c, "180 min = 3 h → 6h + 3h = 9h", 190, 720, 30, "black", GREEN, ep(t, C["23.d"], 0.4), align="left")
        pill(c, "180 ≥ 30 ✓", 440, 760, GREEN, size=24, a=ep(t, C["24.b"], 0.4), anchor="center", bounds=(0, 1920))
    alts_panel(c, t, C, ALT1, 860, 260, 860, 34, "24.ok", "C", 26)
    if C.get("22.p"):
        pause_timer(c, t, C["22.end"] - 1.9, 1560, 720)
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


Q5 = ("Três lâmpadas de um painel piscam em intervalos regulares: a primeira a cada 4 segundos, a segunda a cada 6 segundos e "
      "a terceira a cada 10 segundos. Num certo instante as três piscam juntas. Nos 10 minutos seguintes, quantas vezes elas "
      "voltam a piscar simultaneamente?")
ALT5 = [("A", "6", "26.a", "29.y", "60 ÷ 10 sem converter minutos", RED),
        ("B", "10", "26.b", None, "", GREEN),
        ("C", "12", "26.c", "28.ok", "não sai de 600 ÷ 60", RED),
        ("D", "15", "26.d", "28.ok", "não sai de 600 ÷ 60", RED),
        ("E", "60", "26.e", "29.x", "parou no MMC", RED)]


def b_q5(c, t, C, B):
    sid = which(t, C, ["25", "26", "27", "28", "29"])
    head(c, t, B["start"], "QUESTÃO 5", "A PEGADINHA DO “QUANTAS VEZES”", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["25.a"], 0.5)
    res = ep(t, C["27"], 0.5)
    para(c, Q5, 180, 240, 25, "bold", INK, a * (1 - res), 580, 33)
    for k, (col, per) in enumerate(((COR_A, 4), (COR_B, 6), (COR_C, 10))):
        on_ = 1.0 if int((t - C["25.b"]) / (per / 4)) % 2 == 0 else 0.15
        lampada(c, 280 + k * 170, 680, 0.9, ep(t, C["25.b"] + 0.3 * k, 0.4) * (1 - res), col, on_)
    if res > 0:
        R5 = rows_varal([4, 6, 10])
        marks5 = (C["27.t"] + 0.3, C["27.a"] + 0.8, C["27.b"], C["27.c"], C["27.c"] + 1.6)
        varal(c, 200, 290, R5, sum(ep(t, m, 0.5) for m in marks5), 1.0, size=28, lh=40, colw=74)
        ftext(c, "2·2·3·5 = 60 s", 190, 520, 34, "black", GREEN, ep(t, C["27.e"], 0.4), align="left")
        pill(c, "60 ≥ 10 ✓", 560, 510, GREEN, size=22, a=ep(t, C["27.g"], 0.4), anchor="center", bounds=(0, 1920))
        q = ep(t, C["28"], 0.4)
        pill(c, "QUANTAS VEZES → ainda falta dividir", 440, 620, AMBER, size=22, a=q, anchor="center", bounds=(0, 1920))
        ftext(c, "10 min = 600 s", 190, 700, 34, "black", INK, ep(t, C["28.a"], 0.4), align="left")
        ftext(c, "600 ÷ 60 = 10 vezes", 190, 770, 38, "black", GREEN, ep(t, C["28.b"], 0.4), align="left")
    if t >= C["26"] - 0.2:
        alts_panel(c, t, C, ALT5, 860, 260, 860, 34, "28.ok", "B", 26)
        pause_timer(c, t, C["26.end"] - 1.9, 1560, 720)
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def tabua(c, x, y, w, a, col="#C8955C", cortes=0, cut_a=0.0):
    rrect(c, x, y, w, 46, 6, col, a, shadow=True)
    for k in range(1, cortes):
        xx = x + w * k / cortes
        line(c, xx, y - 8, xx, y + 54, RED, a * cut_a, 3, dash=(8, 6))


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUANDO É PRECISO CORTAR", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    tabua(c, 300, 300, 720, aa, cortes=4, cut_a=ep(t, C["31.a"] + 1.0, 0.4))
    tabua(c, 300, 400, 480, aa, cortes=4, cut_a=ep(t, C["31.a"] + 1.0, 0.4))
    text(c, "cortar tábuas em pedaços iguais", 660, 520, 30, "black", INK2, aa)
    ab = ep(t, C["31.b"], 0.5)
    for g in range(3):
        for k in range(3):
            c.drawCircle(1200 + g * 150 + (k % 2) * 34, 330 + (k // 2) * 40, 16, paint([COR_A, COR_B, COR_C][g], ab))
    text(c, "formar grupos iguais", 1350, 520, 30, "black", INK2, ab)
    text(c, "o maior tamanho possível?", W / 2, 620, 40, "black", AMBER, ep(t, C["31.c"], 0.4))
    fbox(c, "ep. 5 · MDC", W / 2, 730, 46, ep(t, C["31.d"], 0.4), PURPLE)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Você já tinha caído na pegadinha do “quantas vezes”?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, remedios=b_remedios, luzes=b_luzes, definicao=b_definicao,
              atalho=b_atalho, varal68=b_varal68, macetes=b_macetes, varal72=b_varal72,
              porque=b_porque, nosfazemos=b_nosfazemos, varal=b_varal, reconhecer=b_reconhecer, sanidade=b_sanidade,
              quantas=b_quantas, recap=b_recap, erros=b_erros, q1=b_q1, q5=b_q5, ponte=b_ponte, cta=b_cta)
