"""Visual — Razão, Proporção e Regra de Três, Episódio 4: Regra de três composta e o atalho dos homens-hora (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: colunas() (a tabela com a sala de interrogatório), pacote() (a caixa de trabalho fixo), pedreiro().
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
_s = importlib.util.spec_from_file_location("comum021", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_razao_ep4_composta.mp4"
CARD_R = K.CARD_R
CAPACETE = "#F2B705"
TIJOLO = "#C8643B"
CAIXA = "#C9A06A"
CAIXA_ESC = "#9C7444"
SALA = "#2E3A4F"


# ======================================================================
# peças do episódio
# ======================================================================

def pedreiro(c, cx, cy, s, a=1.0, col=BLUE):
    """bonequinho de capacete; (cx, cy) = centro do corpo; s = altura total"""
    if a <= 0:
        return
    r = s * 0.17
    hy = cy - s * 0.30
    c.drawCircle(cx, hy, r, paint("#F1C9A5", a))
    c.drawArc(skia.Rect.MakeXYWH(cx - r * 1.15, hy - r * 1.25, r * 2.3, r * 2.0), 180, 180, True, paint(CAPACETE, a))
    rrect(c, cx - r * 1.35, hy - r * 0.32, r * 2.7, r * 0.3, r * 0.15, CAPACETE, a)
    rrect(c, cx - s * 0.22, cy - s * 0.10, s * 0.44, s * 0.48, s * 0.18, col, a)


def equipe(c, x, y, n, s, a, col=BLUE, por_linha=10, dx=None, dy=None, t=None, t0=None):
    dx = dx or s * 0.62
    dy = dy or s * 1.0
    for i in range(n):
        r_, k = divmod(i, por_linha)
        ai = a if t is None else a * ep(t, t0 + 0.04 * i, 0.3)
        pedreiro(c, x + k * dx, y + r_ * dy, s, ai, col)


def relogio(c, cx, cy, r, horas, a, col=PURPLE):
    """relógio com setor pintado = horas por dia (de 12)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, 360 * horas / 12, True, paint(col, a * 0.35))
    c.drawCircle(cx, cy, r, paint(INK, a, stroke=5))
    c.drawLine(cx, cy, cx, cy - r * 0.7, paint(INK, a, stroke=5, cap_round=True))
    c.drawLine(cx, cy, cx + r * 0.5 * math.sin(math.radians(30 * horas)), cy - r * 0.5 * math.cos(math.radians(30 * horas)),
               paint(INK, a, stroke=5, cap_round=True))


def calcada(c, x, y, w, h, a, prog_=1.0):
    """faixa de calçada com lajotas; prog_ = parte já feita"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 10, "#E7E5DF", a)
    n = 12
    lw = w / n
    for k in range(n):
        fill = clamp(prog_ * n - k, 0, 1)
        if fill > 0:
            rrect(c, x + k * lw + 3, y + 3, lw * fill - 6 if fill < 1 else lw - 6, h - 6, 6, "#B9B5AA", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 10, 10), paint(INK2, a, stroke=3))


def colunas(c, x0, y0, cols, a, alfas=None, destaque=None, cw=300, ch=330, gap=40, inv=None):
    """tabela de colunas: cols = [(titulo, v1, v2, cor)]; alfas = {i: alfa}; destaque = índice da coluna na 'sala';
    inv = {i: 0..1} anima a inversão (troca a ordem dos valores)"""
    alfas = alfas or {}
    inv = inv or {}
    for i, (tit, v1, v2, col) in enumerate(cols):
        ai = a * alfas.get(i, 1.0)
        if ai <= 0:
            continue
        x = x0 + i * (cw + gap)
        rrect(c, x, y0, cw, ch, 22, "#FFFFFF", ai, shadow=True)
        if destaque == i:
            boxed(c, x - 8, y0 - 8, cw + 16, ch + 16, col, ai, 0.0, r=26, sw=6)
        rrect(c, x, y0, cw, 70, 22, col, ai)
        rrect(c, x, y0 + 40, cw, 30, 0, col, ai)
        text_mid(c, tit, x + cw / 2, y0 + 36, 30, "black", "#FFFFFF", ai)
        u = inv.get(i, 0.0)
        ya, yb = y0 + 150, y0 + 260
        if u > 0:
            ya, yb = lerp(ya, yb, ease_io(u)), lerp(yb, ya, ease_io(u))
        fmid(c, v1, x + cw / 2, ya, 64, "black", INK, ai)
        fmid(c, v2, x + cw / 2, yb, 64, "black", AMBER if v2 == "x" else INK, ai)
        line(c, x + 40, y0 + 205, x + cw - 40, y0 + 205, "#E3E1DB", ai, 3)


def pacote(c, cx, cy, s, valor, a, rotulo="pessoa-hora", col=CAIXA, pulse=0.0):
    """a caixa de trabalho fixo: s = lado; valor = número na etiqueta"""
    if a <= 0:
        return
    sc = 1 + 0.05 * math.sin(math.pi * pulse)
    s *= sc
    x, y = cx - s / 2, cy - s / 2
    # tampa em perspectiva
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + s * 0.18, y - s * 0.16); p.lineTo(x + s * 1.18, y - s * 0.16); p.lineTo(x + s, y); p.close()
    c.drawPath(p, paint("#DDBB86", a))
    q = skia.Path(); q.moveTo(x + s, y); q.lineTo(x + s * 1.18, y - s * 0.16); q.lineTo(x + s * 1.18, y + s * 0.84); q.lineTo(x + s, y + s); q.close()
    c.drawPath(q, paint(CAIXA_ESC, a))
    rrect(c, x, y, s, s, 6, col, a)
    rrect(c, x + s * 0.44, y, s * 0.12, s, 0, "#E9D3A6", a)
    rrect(c, x + s * 0.12, y + s * 0.34, s * 0.76, s * 0.36, 12, "#FFFFFF", a)
    fmid(c, valor, x + s / 2, y + s * 0.47, s * 0.17, "black", INK, a)
    text(c, rotulo, x + s / 2, y + s * 0.64, s * 0.075, "black", GRAY, a)


def sala(c, x, y, w, h, a, rotulo=True):
    """sala de interrogatório: retângulo escuro com lâmpada"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 26, "#F1F3F7", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26), paint(SALA, a, stroke=6))
    lx = x + w / 2
    c.drawLine(lx, y, lx, y + 40, paint(SALA, a, stroke=4))
    c.drawArc(skia.Rect.MakeXYWH(lx - 34, y + 30, 68, 50), 180, 180, True, paint(SALA, a))
    c.drawCircle(lx, y + 58, 10, paint(CAPACETE, a))
    if rotulo:
        text(c, "SALA DE INTERROGATÓRIO", x + 30, y + 40, 20, "black", SALA, a, align="left", tracking=2)


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


COLS = [("PEDREIROS", "10", "15", BLUE), ("HORAS/DIA", "6", "8", PURPLE), ("DIAS", "12", "x", GREEN)]


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REGRA DE TRÊS COMPOSTA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    for k, (tit, col) in enumerate((("operários", BLUE), ("horas/dia", PURPLE), ("dias", GREEN))):
        a = ep(t, C["01.a"] + 0.35 * k, 0.4)
        x = 560 + k * 400
        shake = 6 * math.sin(t * 14 + k) * (1 - ep(t, C["01.b"], 0.4))
        rrect(c, x - 160 + shake, 230, 320, 130, 24, col, a)
        text_mid(c, tit, x + shake, 295, 42, "black", "#FFFFFF", a)
    if aa > 0:
        text(c, "TRÊS grandezas ao mesmo tempo assustam", W / 2, 440, 44, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        boxed(c, 460, 500, 1000, 110, PURPLE, ab, 0.08)
        text_mid(c, "COMPOSTA = a SIMPLES repetida", W / 2, 555, 46, "black", PURPLE, ab)
    ac = ep(t, C["01.c"], 0.5)
    pacote(c, W / 2 - 20, 760, 150, "?", ac, "o atalho")
    selo(c, 1380, 760, ac, "SEM DECIDIR DIRETA OU INVERSA", GREEN, -4, 28)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "resolver qualquer regra de três composta", "três ou mais grandezas, sem pânico"),
            ("02.b", "de DOIS jeitos", "o interrogatório e o pacote de trabalho")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETE DO EP. 3", "O TESTE DO DOBRO", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    equipe(c, 260, 330, 10, 70, aa, BLUE, 10, 44)
    text(c, "10 pintores → 6 dias", 470, 470, 38, "black", INK, aa)
    ab = ep(t, C["03.b"], 0.5)
    equipe(c, 1060, 300, 20, 70, ab, BLUE, 10, 44, 70)
    text(c, "20 pintores → 3 dias", 1270, 470, 38, "black", INK, ab)
    chip(c, "×2 pintores · ÷2 dias = INVERSA", W / 2, 560, BLUE, ab, 32)
    ac = ep(t, C["03.c"], 0.5)
    if ac > 0:
        boxed(c, 560, 630, 800, 120, PURPLE, ac, 0.08)
        expr(c, "10 · 6 = 20 · 3 = 60", W / 2, 690, 54, ac, cores={6: GREEN})
    text(c, "na inversa, o PRODUTO não muda", W / 2, 800, 30, "black", PURPLE, ac)


# ======================================================================
# a obra, a tabela e o método
# ======================================================================

def b_historia(c, t, C, B):
    frame(c, t, B["start"], "UMA OBRA", "TRÊS GRANDEZAS MUDANDO", BLUE)
    aa = ep(t, C["04.a"], 0.5)
    equipe(c, 250, 300, 10, 72, aa, BLUE, 10, 46, t=t, t0=C["04.a"])
    relogio(c, 830, 290, 56, 6, aa)
    text(c, "6 h/dia", 830, 380, 30, "black", PURPLE, aa)
    calcada(c, 950, 255, 520, 70, aa, ep(t, C["04.a"] + 0.6, 1.4))
    text(c, "12 dias", 1210, 380, 30, "black", GREEN, aa)
    ab = ep(t, C["04.b"], 0.5)
    equipe(c, 250, 470, 15, 72, ab, BLUE, 15, 32, t=t, t0=C["04.b"])
    relogio(c, 830, 470, 56, 8, ab)
    text(c, "8 h/dia", 830, 560, 30, "black", PURPLE, ab)
    calcada(c, 950, 435, 520, 70, ab, 0.0)
    acx = ep(t, C["04.c"], 0.5)
    if acx > 0:
        fmid(c, "? dias", 1210, 560, 40, "black", AMBER, acx)
    ad = ep(t, C["04.d"], 0.5)
    chip(c, "3 grandezas mudam juntas", W / 2, 650, AMBER, ad, 32)
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        boxed(c, 360, 710, 1200, 100, BLUE, ae, 0.08)
        text_mid(c, "REGRA DE TRÊS COMPOSTA = três ou mais grandezas", W / 2, 760, 38, "black", BLUE, ae)


def b_tabela(c, t, C, B):
    frame(c, t, B["start"], "PASSO 1", "UMA COLUNA POR GRANDEZA", BLUE)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "COLUNA = uma fileira em pé com os dois valores", W / 2, 250, 32, "black", BLUE, aa)
    al = {0: ep(t, C["05.b"], 0.5), 1: ep(t, C["05.c"], 0.5), 2: ep(t, C["05.d"], 0.5)}
    colunas(c, 450, 320, COLS, 1.0, al)
    ae = ep(t, C["05.e"], 0.5)
    if ae > 0:
        chip(c, "x = INCÓGNITA: o valor procurado", W / 2, 760, AMBER, ae, 32)


METODO = ["uma coluna por grandeza", "compare CADA coluna com a da incógnita, uma de cada vez",
          "inverta as colunas inversas", "razão da incógnita = PRODUTO das outras razões"]


def passos(c, x, y, a, ativo=None, n=4, size=34, gap=78, alfas=None):
    for k in range(n):
        ak = a * (alfas[k] if alfas else 1.0)
        if ak <= 0:
            continue
        on = ativo is None or ativo == k
        badge_num(c, k + 1, x, y + k * gap - 12, ak, 30, bg=PURPLE if on else LIGHT)
        text(c, METODO[k], x + 50, y + k * gap, size, "black", INK if on else GRAY, ak, align="left")


def b_metodo(c, t, C, B):
    frame(c, t, B["start"], "O MÉTODO", "QUATRO PASSOS", PURPLE)
    al = [ep(t, C[f"06.{x}"], 0.5) for x in "abcd"]
    passos(c, 330, 330, 1.0, None, alfas=al, size=40, gap=110)


# ======================================================================
# o interrogatório
# ======================================================================

def b_interroga(c, t, C, B):
    sid = which(t, C, ["07", "08"])
    head_seq(c, t, C, [("07", "PASSO 2", "1º SUSPEITO: PEDREIROS", BLUE), ("08", "PASSO 2", "2º SUSPEITO: HORAS POR DIA", PURPLE)])
    card(c, *CARD_R)
    a0 = ep(t, C["07.a"], 0.5)
    sala(c, 680, 190, 1080, 470, a0)
    # a incógnita fica sempre na sala; o suspeito entra; o outro espera lá fora (esmaecido, à esquerda)
    colunas(c, 1340, 270, [COLS[2]], a0, cw=260, ch=300)
    if sid == "07":
        u = ep(t, C["07.b"], 0.8)
        colunas(c, lerp(260, 900, u), 270, [COLS[0]], 1.0, destaque=0 if u > 0.9 else None, cw=260, ch=300)
        colunas(c, 260, 270, [COLS[1]], lerp(1.0, 0.3, u) if u > 0 else 0.0, cw=260, ch=300)
        out_a = 0.6 * u
    else:
        u = ep(t, C["08"], 0.8)
        colunas(c, lerp(900, 260, u), 270, [COLS[0]], lerp(1.0, 0.3, u), cw=260, ch=300)
        colunas(c, lerp(260, 900, u), 270, [COLS[1]], lerp(0.3, 1.0, u), destaque=0 if u > 0.9 else None, cw=260, ch=300)
        out_a = 0.6
    text(c, "lá fora", 390, 610, 26, "black", GRAY, out_a)
    q = sid
    ac = ep(t, C[f"{q}.{'c' if q == '07' else 'b'}"], 0.5)
    if ac > 0:
        rrect(c, 880, 595, 760, 52, 14, "#FFFFFF", ac)
        ftext(c, ("dobro de pedreiros → metade dos dias" if q == "07" else "dobro de horas → metade dos dias"), 1260, 631, 28,
              "black", INK, ac)
    ad = ep(t, C[f"{q}.{'d' if q == '07' else 'c'}"], 0.5)
    selo(c, 1600, 230, ad, "INVERSA", BLUE, -6, 34)
    selo(c, 1210, 730, ad, "TESTE DO DOBRO: ×2 → ÷2", GREEN, -2, 26)
    if q == "08":
        at = ep(t, C["08.d"], 0.5)
        if at > 0:
            K.atalho(c, 160, 680, 560, 140, "ATALHO", ["sempre pergunte: e os DIAS?"], at, 30)


def b_montar(c, t, C, B):
    sid = which(t, C, ["09", "10"])
    head_seq(c, t, C, [("09", "PASSOS 3 E 4", "INVERTA E MULTIPLIQUE", PURPLE), ("10", "A CONTA", "PASSO A PASSO", PURPLE)])
    card(c, *CARD_R)
    if sid == "09":
        inv = {0: ep(t, C["09.a"], 0.8), 1: ep(t, C["09.b"], 0.8)}
        colunas(c, 330, 230, COLS, 1.0, inv=inv, cw=260, ch=300)
        text(c, "inversas: de cabeça para baixo", 640, 590, 30, "black", BLUE, ep(t, C["09"], 0.5))
        ac = ep(t, C["09.c"], 0.5)
        if ac > 0:
            boxed(c, 330, 650, 1260, 150, PURPLE, ac, 0.08)
            expr(c, "12/x = 15/10 · 8/6", W / 2, 725, 66, ac, cores={0: GREEN, 2: BLUE, 4: PURPLE})
    else:
        expr(c, "12/x = 15/10 · 8/6", W / 2, 280, 60, 1.0, cores={0: GREEN, 2: BLUE, 4: PURPLE})
        aa = ep(t, C["10.a"], 0.4)
        ab = ep(t, C["10.b"], 0.4)
        acc = ep(t, C["10.c"], 0.4)
        if aa > 0:
            expr(c, "15/10 = 1,5", 600, 430, 52, aa, cores={2: BLUE})
        if ab > 0:
            expr(c, "8/6 = 4/3", 1320, 430, 52, ab, cores={2: PURPLE})
        if acc > 0:
            expr(c, "1,5 · 4/3 = 2", W / 2, 550, 56, acc, cores={4: GREEN})
        ad = ep(t, C["10.d"], 0.4)
        if ad > 0:
            expr(c, "12/x = 2 → x = 12 ÷ 2", W / 2, 660, 52, ad)
        ae = ep(t, C["10.e"], 0.4)
        selo(c, 1480, 660, ae, "x = 6 DIAS", GREEN, -5, 40)
        af = ep(t, C["10.f"], 0.4)
        if af > 0:
            K.atalho(c, 560, 720, 800, 100, "ATALHO · CONFIRA O SENTIDO", ["mais gente e mais horas → MENOS dias: 6 < 12 ✓"], af, 28)


def b_regra(c, t, C, B):
    frame(c, t, B["start"], "A REGRA QUE EVITA A CONFUSÃO", "NUNCA ENTRE SI", RED)
    aa = ep(t, C["11.a"], 0.5)
    colunas(c, 330, 250, COLS, aa, cw=260, ch=280)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        # seta entre pedreiros e horas, riscada
        y = 230
        c.drawLine(460, y, 760, y, paint(RED, ab, stroke=6, cap_round=True))
        check_icon(c, 610, y - 20, 30, ab, RED, "x")
        text(c, "pedreiros × horas? não interessa", 610, 600, 32, "black", RED, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        text(c, "tudo ao mesmo tempo", 1470, 380, 30, "black", AMBER, acc)
        text(c, "= parece impossível", 1470, 425, 30, "black", AMBER, acc)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        boxed(c, 360, 680, 1200, 110, PURPLE, ad, 0.08)
        text_mid(c, "um suspeito de cada vez, SEMPRE contra a incógnita", W / 2, 735, 38, "black", PURPLE, ad)
    if ad > 0:
        for k in (0, 1):
            x = 330 + k * 300 + 130
            c.drawLine(x, 545, 330 + 2 * 300 + 130, 545, paint(GREEN, ad * 0.8, stroke=5, cap_round=True))


# ======================================================================
# o atalho dos homens-hora
# ======================================================================

def b_pacote(c, t, C, B):
    sid = which(t, C, ["12", "13"])
    head_seq(c, t, C, [("12", "O ATALHO", "O PACOTE DE TRABALHO", GREEN), ("13", "O ATALHO", "O PACOTE NÃO MUDA", GREEN)])
    card(c, *CARD_R)
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            boxed(c, 200, 230, 820, 110, BLUE, ab, 0.08)
            text_mid(c, "HOMEM-HORA = 1 pessoa trabalhando 1 hora", 610, 285, 34, "black", BLUE, ab)
        acx = ep(t, C["12.c"], 0.5)
        if acx > 0:
            expr(c, "10 · 6 · 12 = 720", 610, 470, 64, acx, cores={6: GREEN})
            text(c, "pedreiros · horas/dia · dias", 610, 560, 28, "black", GRAY, acx)
        ad = ep(t, C["12.d"], 0.5)
        pacote(c, 1360, 470, 300, "720" if acx > 0.5 else "?", max(aa, acx), pulse=ep(t, C["12.d"], 0.6))
        if ad > 0:
            chip(c, "TRABALHO TOTAL: o que a calçada exige", 1360, 740, GREEN, ad, 30)
    else:
        pacote(c, 1360, 470, 300, "720", 1.0)
        text(c, "o mesmo pacote", 1360, 740, 30, "black", GREEN, 1.0)
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            expr(c, "15 · 8 · x = 720", 600, 330, 60, aa, cores={4: AMBER})
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            expr(c, "120 · x = 720", 600, 460, 56, ab)
        acx = ep(t, C["13.c"], 0.5)
        if acx > 0:
            expr(c, "x = 720 ÷ 120 = 6", 600, 590, 56, acx, cores={6: GREEN})
        ad = ep(t, C["13.d"], 0.5)
        selo(c, 600, 730, ad, "SEM DECIDIR DIRETA OU INVERSA", GREEN, -3, 28)


def b_quando(c, t, C, B):
    frame(c, t, B["start"], "QUANDO USAR O ATALHO", "OBRA FIXA", GREEN)
    itens = [("trabalhadores", BLUE), ("ritmo (horas/dia)", PURPLE), ("tempo (dias)", GREEN)]
    aa = ep(t, C["14.a"], 0.5)
    for k, (s, col) in enumerate(itens):
        a = ep(t, C["14.a"] + 0.5 * k, 0.4)
        x = 420 + k * 540
        rrect(c, x - 230, 260, 460, 110, 24, col, a)
        text_mid(c, s, x, 315, 38, "black", "#FFFFFF", a)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        text(c, "produzindo uma quantidade FIXA:", W / 2, 450, 38, "black", INK, ab)
        text(c, "o mesmo muro · a mesma calçada · a mesma casa", W / 2, 510, 34, "bold", GRAY, ab)
    acx = ep(t, C["14.c"], 0.5)
    if acx > 0:
        K.atalho(c, 400, 580, 1120, 200, "ATALHO", ["obra fixa? multiplique tudo de um lado", "e iguale ao outro"], acx, 36)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    sid = which(t, C, ["15", "16"])
    head_seq(c, t, C, [("15", "SUA VEZ", "PELO ATALHO", GREEN), ("16", "VAMOS CONFERIR", "PELO ATALHO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        text(c, "ANTES", 300, 250, 26, "black", GRAY, aa)
        ftext(c, "5 pintores · 6 h por dia · 8 dias", 400, 262, 40, "black", INK, aa, align="left")
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        text(c, "DEPOIS", 300, 340, 26, "black", GRAY, ab)
        ftext(c, "4 pintores · 8 h por dia · x dias", 400, 352, 40, "black", INK, ab, align="left")
        text(c, "a MESMA casa", 1180, 352, 30, "black", GREEN, ab, align="left")
    pause_timer(c, t, C["15.end"] - 1.9, W / 2, 560)
    if sid == "16":
        ra = ep(t, C["16.a"], 0.4)
        if ra > 0:
            expr(c, "5 · 6 · 8 = 240", 520, 470, 50, ra, cores={6: GREEN})
        pacote(c, 1450, 520, 210, "240", ra)
        rb = ep(t, C["16.b"], 0.4)
        if rb > 0:
            expr(c, "4 · 8 · x = 32 · x", 520, 580, 46, rb)
        rc = ep(t, C["16.c"], 0.4)
        if rc > 0:
            expr(c, "x = 240 ÷ 32 = 7,5 dias", 520, 690, 50, rc, cores={6: GREEN, 7: GREEN})
        rd = ep(t, C["16.d"], 0.4)
        if rd > 0:
            text(c, "por dia: 32 h de trabalho > 30 h", 1000, 720, 30, "black", INK2, rd, align="left")
            text(c, "um pouco mais por dia → um pouco menos dias ✓", 1000, 770, 26, "black", GREEN, rd, align="left")


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Composta é a simples repetida.", "Cada coluna frente a frente com a incógnita, uma de cada vez.",
          "Obra fixa? O pacote de pessoa-hora não muda."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "25"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1340, 58)


ERROS = [("Comparar as colunas entre si", "todas estão na mesma tabela, uma do lado da outra",
          "só a incógnita interessa: cada coluna contra ela, uma de cada vez"),
         ("Esquecer de inverter uma coluna inversa", "você decidiu direitinho e só esqueceu um detalhe ao montar",
          "uma coluna sem inverter muda a resposta inteira: confira pelo pacote"),
         ("Usar o atalho quando a obra muda de tamanho", "continuam sendo pedreiros, horas e dias",
          "calçada com o DOBRO do comprimento: o pacote dobra (720 → 1440)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20"], ERROS)


# ======================================================================
# Questão 6 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=34, w=640):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS6 = [("A", "6 dias", "não fecha o pacote: 1 080 < 1 440", RED), ("B", "8 dias", "", GREEN),
         ("C", "10 dias", "só interrogou os operários", RED), ("D", "12 dias", "só interrogou as horas", RED),
         ("E", "18 dias", "operários como direta", RED)]


def b_q6(c, t, C, B):
    sid = which(t, C, ["21", "22", "23", "24"])
    head(c, t, B["start"], "QUESTÃO · REGRA DE TRÊS COMPOSTA", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    _enunciado(c, [("Doze operários, trabalhando 8 horas por dia, constroem um muro em 15 dias.", INK),
                   ("Mantido o mesmo ritmo, dezoito operários trabalhando 10 horas por dia construirão um muro idêntico em", BLUE)],
               a0, 240, 30, 680)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ACDE"}
    if t >= C["21.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS6, 980, 220, 700, 40, C["23.ok"], "B", cues_in, cues_x, gap=16)
    pause_timer(c, t, C["21.end"] - 1.9, 470, 660)
    if sid == "22":
        ra = ep(t, C["22"], 0.4)
        rrect(c, 170, 500, 720, 310, 18, "#FFFFFF", ra, shadow=True)
        text(c, "1º caminho: o interrogatório", 530, 545, 26, "black", PURPLE, ra)
        ftext(c, "operários × dias: INVERSA", 530, 595, 28, "black", BLUE, ep(t, C["22.a"], 0.4))
        ftext(c, "horas × dias: INVERSA", 530, 640, 28, "black", PURPLE, ep(t, C["22.b"], 0.4))
        acx = ep(t, C["22.c"], 0.4)
        if acx > 0:
            expr(c, "15/x = 18/12 · 10/8", 530, 710, 38, acx, cores={0: GREEN})
        ae = ep(t, C["22.d"], 0.4)
        if ae > 0:
            expr(c, "= 1,875 → x = 15 ÷ 1,875 = 8", 530, 780, 30, ae, cores={6: GREEN})
    elif sid in ("23", "24"):
        ra = ep(t, C["23"], 0.4)
        rrect(c, 170, 500, 720, 310, 18, "#FFFFFF", ra, shadow=True)
        text(c, "2º caminho: o pacote", 530, 545, 26, "black", GREEN, ra)
        aa = ep(t, C["23.a"], 0.4)
        if aa > 0:
            expr(c, "12 · 8 · 15 = 1 440", 470, 610, 38, aa, cores={6: GREEN, 7: GREEN})
        pacote(c, 800, 620, 110, "1 440", aa, "")
        ab = ep(t, C["23.b"], 0.4)
        if ab > 0:
            expr(c, "18 · 10 · x = 180 · x", 470, 690, 36, ab)
        acx = ep(t, C["23.c"], 0.4)
        if acx > 0:
            expr(c, "x = 1 440 ÷ 180 = 8", 470, 770, 38, acx, cores={7: GREEN})


# ======================================================================
# ponte e CTA
# ======================================================================

def gato(c, cx, cy, s, a, col=INK2):
    if a <= 0:
        return
    c.drawCircle(cx, cy, s * 0.32, paint(col, a))
    for sg in (-1, 1):
        p = skia.Path(); p.moveTo(cx + sg * s * 0.28, cy - s * 0.12); p.lineTo(cx + sg * s * 0.30, cy - s * 0.46)
        p.lineTo(cx + sg * s * 0.06, cy - s * 0.30); p.close()
        c.drawPath(p, paint(col, a))
        c.drawCircle(cx + sg * s * 0.12, cy - s * 0.04, s * 0.05, paint(CAPACETE, a))
    rrect(c, cx - s * 0.30, cy + s * 0.22, s * 0.6, s * 0.46, s * 0.2, col, a)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUANDO A REGRA DE TRÊS NÃO VALE", PURPLE)
    aa = ep(t, C["26.a"], 0.5)
    if aa > 0:
        boxed(c, 360, 230, 1200, 110, AMBER, aa, 0.08)
        text_mid(c, "cara de regra de três… e aplicar dá ERRADO", W / 2, 285, 40, "black", AMBER, aa)
    ab = ep(t, C["26.b"], 0.5)
    for k in range(2):
        gato(c, 700 + k * 140, 520, 140, ab * ep(t, C["26.b"] + 0.3 * k, 0.3))
    if ab > 0:
        text(c, "2 gatos · 2 ratos · 2 minutos", 1200, 540, 40, "black", INK, ab)
    pill(c, "ep. 5 · quando a regra de três NÃO funciona", W / 2, 760, PURPLE, size=32, a=ep(t, C["26.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["27.like"], C["27.sub"], C["27.bell"], C["27.com"], C["27.bye"], "Interrogatório ou pacote: qual você prefere?",
        canal="no Estudativo", anki=C["27.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, historia=b_historia, tabela=b_tabela, metodo=b_metodo,
              interroga=b_interroga, montar=b_montar, regra=b_regra, pacote=b_pacote, quando=b_quando,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q6=b_q6, ponte=b_ponte, cta=b_cta)
