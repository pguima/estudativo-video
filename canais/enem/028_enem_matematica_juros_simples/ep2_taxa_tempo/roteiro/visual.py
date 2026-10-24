"""Visual — Juros Simples, Episódio 2: taxa e tempo na mesma unidade (meses, anos, dias e o boleto atrasado) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: ficha() (TAXA e TEMPO, cada uma com a bandeirinha da sua unidade), cadeado() (fórmula trancada quando
as bandeiras são diferentes; abre quando uma ficha é traduzida), meses() (a fila de 12 meses de 2% que vira 24% ao ano),
ingresso() (a multa) e taximetro() (os juros de mora girando a cada dia), boleto(), linha().
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
_s = importlib.util.spec_from_file_location("comum028", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_juros_simples_ep2_taxa_tempo.mp4"
CARD_R = K.CARD_R
PAPEL = "#FFFDF6"


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


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def bandeira(c, x, y, s, col, a, size=26):
    """bandeirinha num mastro (x, y = pé do mastro), com o nome da unidade"""
    if a <= 0:
        return
    w = text_w(s, "black", size) + 34
    line(c, x, y, x, y - 92, INK2, a, 4)
    p = skia.Path(); p.moveTo(x + 2, y - 92); p.lineTo(x + w + 18, y - 92); p.lineTo(x + w, y - 70)
    p.lineTo(x + w + 18, y - 48); p.lineTo(x + 2, y - 48); p.close()
    c.drawPath(p, paint(col, a))
    text(c, s, x + 2 + w / 2, y - 61, size, "black", "#FFFFFF", a)


def ficha(c, cx, cy, titulo, valor, unid, col, a, w=430, h=200, ucol=None, vsize=78):
    """ficha TAXA ou TEMPO: cartão branco com o valor e a bandeirinha da unidade"""
    if a <= 0:
        return
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, 24, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), paint(col, a, stroke=5))
    text(c, titulo, x + 30, y + 46, 26, "black", col, a, align="left", tracking=2)
    fmid(c, valor, cx, cy + 30, vsize, "black", INK, a)
    bandeira(c, x + w - 150, y + 8, unid, ucol or col, a)


def cadeado(c, cx, cy, s, a, aberto=0.0):
    """cadeado: âmbar trancado; verde e com a alça levantada quando aberto (0 a 1)"""
    if a <= 0:
        return
    col = AMBER if aberto < 0.5 else GREEN
    lift = s * 0.45 * aberto
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - s * 0.42, cy - s * 1.05 - lift, s * 0.84, s * 0.9), 180, 180)
    c.drawPath(p, paint(INK2, a, stroke=s * 0.16))
    line(c, cx - s * 0.42, cy - s * 0.6 - lift, cx - s * 0.42, cy - s * 0.25 - lift * (1 - aberto), INK2, a, s * 0.16)
    line(c, cx + s * 0.42, cy - s * 0.6 - lift, cx + s * 0.42, cy - s * 0.25, INK2, a * (1 - aberto), s * 0.16)
    rrect(c, cx - s * 0.68, cy - s * 0.32, s * 1.36, s * 1.0, s * 0.16, col, a)
    c.drawCircle(cx, cy + s * 0.12, s * 0.13, paint("#FFFFFF", a))
    line(c, cx, cy + s * 0.12, cx, cy + s * 0.4, "#FFFFFF", a, s * 0.1)


def formula(c, cx, cy, a, size=64, aberta=None):
    """J = C · i · t numa faixa roxa; aberta (0 a 1) acende a faixa em verde"""
    if a <= 0:
        return
    s = "J = C · i · t"
    w = ftext_w(s, "black", size) + 90
    col = PURPLE if not aberta or aberta < 0.5 else GREEN
    boxed(c, cx - w / 2, cy - size * 0.85, w, size * 1.7, col, a, 0.10)
    fmid(c, s, cx, cy, size, "black", col, a)


def meses(c, x, y, w, a, ativos=12, val="2%", col=None, rot=True, h=86):
    """fila de 12 meses, cada um com `val`; os primeiros `ativos` acesos"""
    if a <= 0:
        return
    col = col or GREEN
    cw = w / 12
    for k in range(12):
        on = k < ativos
        rrect(c, x + k * cw + 4, y, cw - 8, h, 12, mix("#FFFFFF", col, 0.22) if on else "#F2F2EE", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + k * cw + 4, y, cw - 8, h), 12, 12),
                    paint(col if on else LIGHT, a, stroke=3))
        text(c, val, x + k * cw + cw / 2, y + h / 2 + 10, 26, "black", INK if on else GRAY, a)
        if rot:
            text(c, f"{k + 1}º", x + k * cw + cw / 2, y + h + 30, 18, "bold", GRAY, a)


def chave(c, x0, x1, y, s, col, a, size=30):
    """chave horizontal embaixo de um trecho, com rótulo"""
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(x0, y); p.quadTo(x0, y + 22, x0 + 22, y + 22); p.lineTo((x0 + x1) / 2 - 18, y + 22)
    p.quadTo((x0 + x1) / 2, y + 22, (x0 + x1) / 2, y + 42); p.quadTo((x0 + x1) / 2, y + 22, (x0 + x1) / 2 + 18, y + 22)
    p.lineTo(x1 - 22, y + 22); p.quadTo(x1, y + 22, x1, y)
    c.drawPath(p, paint(col, a, stroke=4))
    fmid(c, s, (x0 + x1) / 2, y + 80, size, "black", col, a)


def ingresso(c, cx, cy, valor, a, w=360, h=180, sub="uma vez só"):
    """o ingresso (a multa): bilhete âmbar com picote"""
    if a <= 0:
        return
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, 18, mix("#FFFFFF", AMBER, 0.30), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), paint(AMBER, a, stroke=4))
    for k in range(7):
        c.drawCircle(x + w * 0.72, y + 16 + k * (h - 32) / 6, 5, paint("#FFFFFF", a))
    text(c, "MULTA", x + w * 0.36, y + 52, 28, "black", AMBER, a, tracking=2)
    fmid(c, valor, x + w * 0.36, cy + 18, 48, "black", INK, a)
    text(c, sub, x + w * 0.36, y + h - 22, 20, "bold", INK2, a)
    c.save(); c.translate(x + w * 0.86, cy); c.rotate(-90)
    text_mid(c, "INGRESSO", 0, 0, 22, "black", AMBER, a)
    c.restore()


def taximetro(c, cx, cy, dias, valor, a, w=380, h=210):
    """o taxímetro (os juros de mora): visor com os dias rodando e o valor"""
    if a <= 0:
        return
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, 24, "#1F2430", a, shadow=True)
    text(c, "JUROS DE MORA", cx, y + 42, 24, "black", "#C9CED8", a, tracking=2)
    rrect(c, x + 24, y + 64, w - 48, 74, 12, "#0F1218", a)
    fmid(c, valor, cx, y + 101, 50, "black", GREEN, a)
    text(c, f"{dias} dia{'s' if dias != 1 else ''} de atraso", cx, y + h - 26, 26, "black", AMBER, a)
    # rodinha girando
    ang = dias * 0.9
    rx, ry = x + w - 34, y + 36
    c.drawCircle(rx, ry, 16, paint(AMBER, a, stroke=4))
    line(c, rx, ry, rx + 14 * math.cos(ang), ry + 14 * math.sin(ang), AMBER, a, 4)


def boleto(c, x, y, w, h, linhas, a):
    """boleto de papel com código de barras"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, PAPEL, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), paint(K.PAPEL_BORDA, a, stroke=3))
    text(c, "BOLETO", x + 30, y + 48, 28, "black", INK, a, align="left", tracking=3)
    yy = y + 104
    for s, col in linhas:
        ftext(c, s, x + 30, yy, 30, "black", col, a, align="left")
        yy += 50
    bx = x + 30
    for k in range(40):
        bw = 3 if k % 3 else 6
        c.drawRect(skia.Rect.MakeXYWH(bx, y + h - 70, bw, 46), paint(INK, a))
        bx += bw + 4


def cal_mes(c, x, y, a, marcados=0, col=None, cel=46):
    """mês comercial: grade de 30 dias (6 × 5); os primeiros `marcados` pintados"""
    if a <= 0:
        return
    col = col or AMBER
    for k in range(30):
        cx, cy = x + (k % 6) * (cel + 6), y + (k // 6) * (cel + 6)
        on = k < marcados
        rrect(c, cx, cy, cel, cel, 8, mix("#FFFFFF", col, 0.45) if on else "#FFFFFF", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx, cy, cel, cel), 8, 8), paint(col if on else LIGHT, a, stroke=2))
        text(c, str(k + 1), cx + cel / 2, cy + cel / 2 + 7, 18, "bold", INK if on else GRAY, a)


def unidades(c, x, y, taxa, tempo, a, aberto=0.0, size=26):
    """faixa 'taxa: ___ / tempo: ___' com o cadeado (painel das questões)"""
    if a <= 0:
        return
    rrect(c, x, y, 660, 70, 16, mix("#FFFFFF", AMBER if aberto < 0.5 else GREEN, 0.12), a)
    linha(c, [("taxa: ", GRAY), (taxa, PURPLE), ("   tempo: ", GRAY), (tempo, BLUE)], x + 30, y + 35, size, a,
          align="left")
    cadeado(c, x + 620, y + 44, 30, a, aberto)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "JUROS SIMPLES", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    ficha(c, 560, 360, "TAXA", "18%", "ao ano", PURPLE, aa)
    ficha(c, 1360, 360, "TEMPO", "8", "meses", BLUE, ep(t, C["01.a"] + 1.4, 0.5))
    if aa > 0:
        linha(c, [("capital: ", GRAY), ("R$ 5.000,00", INK)], W / 2, 360, 28, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 230, 520, 700, 170, 24, mix("#FFFFFF", RED, 0.08), ab)
        linha(c, [("5.000 × 0,18 × 8", RED)], 580, 575, 44, ab)
        linha(c, [("= R$ 7.200,00", RED)], 580, 640, 50, ep(t, C["01.b"] + 1.4, 0.4))
        check_icon(c, 890, 545, 36, ep(t, C["01.b"] + 2.4, 0.4), RED, "x")
        text(c, "mais que o próprio capital!", 580, 730, 28, "black", RED, ep(t, C["01.b"] + 3.0, 0.4))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 990, 520, 700, 170, 24, mix("#FFFFFF", GREEN, 0.10), acc)
        linha(c, [("conta certa", GREEN)], 1340, 575, 36, acc)
        linha(c, [("R$ 600,00", GREEN)], 1340, 640, 60, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 800, ad, "A DIFERENÇA: “AO ANO”", AMBER, -3, 44)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "igualar taxa e tempo em qualquer questão", "meses · anos · dias"),
            ("02.b", "calcular um boleto pago com atraso", "multa + juros de mora")]
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
        rrect(c, 200, 230, 720, 560, 24, "#FFFFFF", aa, shadow=True)
        rrect(c, 200, 230, 720, 64, 24, PURPLE, aa * 0.14)
        text(c, "JUROS SIMPLES", 560, 274, 30, "black", PURPLE, aa)
        text(c, "episódio 1", 560, 334, 22, "bold", GRAY, aa)
        formula(c, 560, 450, aa, 60)
        text(c, "a conta de UM MÊS só", 560, 600, 34, "black", INK, aa)
        text(c, "× o número de meses", 560, 652, 34, "black", INK, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 230, 720, 560, 24, "#FFFFFF", ab, shadow=True)
        rrect(c, 1000, 230, 720, 64, 24, BLUE, ab * 0.14)
        text(c, "A ESCADA DO TEMPO", 1360, 274, 30, "black", BLUE, ab)
        text(c, "série de Unidades", 1360, 334, 22, "bold", GRAY, ab)
        linha(c, [("1 ano = ", INK), ("12 meses", BLUE)], 1360, 420, 46, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        linha(c, [("1 ano e 3 meses = ", INK), ("15 meses", GREEN)], 1360, 520, 36, acc)
        linha(c, [("= ", INK), ("1,25 ano", GREEN), ("   nunca ", INK2), ("1,3", RED)], 1360, 590, 36, acc)
        pill(c, "PRAZO MISTO: duas unidades juntas", 1360, 700, BLUE, size=24, a=ep(t, C["03.c"] + 4.0, 0.4),
             anchor="center")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS SITUAÇÕES", "DO DIA A DIA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    boleto(c, 230, 220, 680, 470, [("CONTA DE LUZ", BLUE), ("venceu: dia 10", INK2), ("multa: 2%", AMBER),
                                   ("juros: 1% ao mês", PURPLE)], aa)
    if aa > 0:
        selo(c, 760, 300, ep(t, C["04.a"] + 1.0, 0.4), "ATRASADA", RED, 8, 30)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 1010, 220, 680, 470, 14, PAPEL, ab, shadow=True)
        text(c, "CONTRATO DE EMPRÉSTIMO", 1350, 280, 30, "black", INK, ab, tracking=1)
        for k in range(4):
            line(c, 1060, 340 + k * 40, 1640, 340 + k * 40, LIGHT, ab, 6)
        linha(c, [("taxa: ", INK), ("18% AO ANO", PURPLE)], 1350, 540, 40, ab)
        linha(c, [("prazo: ", INK), ("8 MESES", BLUE)], 1350, 610, 40, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        rrect(c, 560, 730, 800, 84, 42, mix("#FFFFFF", AMBER, 0.14), acc)
        fmid(c, "a taxa fala de um período, o tempo de outro", W / 2, 772, 32, "black", AMBER, acc)


# ======================================================================
# bloco a — a regra e a tradução
# ======================================================================

def b_regra(c, t, C, B):
    head_seq(c, t, C, [("05", "A REGRA", "A MESMA UNIDADE", PURPLE), ("06", "COMO DESTRANCAR", "TRADUZA SÓ UM", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        formula(c, W / 2, 260, aa, 60)
        if aa > 0:
            text(c, "i e t na MESMA unidade", W / 2, 350, 34, "black", PURPLE, ep(t, C["05.a"] + 1.6, 0.4))
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            linha(c, [("taxa mensal", PURPLE), ("  ↔  ", INK2), ("meses", BLUE)], 560, 450, 40, ab)
            linha(c, [("taxa anual", PURPLE), ("  ↔  ", INK2), ("anos", BLUE)], 1360, 450,  40, ep(t, C["05.b"] + 1.6, 0.4))
        acc = ep(t, C["05.c"], 0.5)
        ficha(c, 560, 650, "TAXA", "18%", "ao ano", PURPLE, acc, h=180, vsize=64)
        ficha(c, 1360, 650, "TEMPO", "8", "meses", BLUE, acc, h=180, vsize=64)
        cadeado(c, W / 2, 660, 70, ep(t, C["05.c"] + 2.0, 0.4))
        if acc > 0:
            text(c, "línguas diferentes", W / 2, 780, 26, "black", AMBER, ep(t, C["05.c"] + 2.0, 0.4))
        return
    a0 = ep(t, C["06"], 0.4)
    formula(c, W / 2, 260, a0, 56, aberta=ep(t, C["06.b"] + 2.6, 0.4))
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        text(c, "TRADUZA", W / 2, 380, 52, "black", GREEN, aa, tracking=3)
    ab = ep(t, C["06.b"], 0.5)
    g = ep(t, C["06.b"] + 1.0, 1.2)
    if g < 0.5:
        ficha(c, 560, 600, "TAXA", "18%", "ao ano", PURPLE, a0, h=180, vsize=64)
    else:
        ficha(c, 560, 600, "TAXA", "1,5%", "ao mês", PURPLE, a0, h=180, vsize=64, ucol=GREEN)
    ficha(c, 1360, 600, "TEMPO", "8", "meses", BLUE, a0, h=180, vsize=64)
    cadeado(c, W / 2, 610, 70, a0, ep(t, C["06.b"] + 2.6, 0.5))
    if ab > 0:
        pill(c, "18% ÷ 12 = 1,5% ao mês", 560, 722, GREEN, size=24, a=ab * g, anchor="center")
        pill(c, "ou: 8 meses = 8/12 de ano", 1360, 722, GRAY, size=22, a=ep(t, C["06.b"] + 2.0, 0.4), anchor="center")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 805, acc, "SÓ UM DOS DOIS · NUNCA OS DOIS", AMBER, -2, 30)


# ======================================================================
# bloco b — taxas proporcionais
# ======================================================================

def b_proporcionais(c, t, C, B):
    head(c, t, B["start"], "TAXAS PROPORCIONAIS", "SÓ EM JUROS SIMPLES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        pill(c, "TAXAS PROPORCIONAIS: a taxa cresce na mesma proporção do tempo", W / 2, 230, BLUE, size=26, a=aa,
             anchor="center")
    ab = ep(t, C["07.b"], 0.5)
    x0, wq = 240, 1440
    n = 12
    if t >= C["07.c"]:
        g = ep(t, C["07.c"], 4.5)
        n = 1 if g < 0.25 else 3 if g < 0.5 else 6 if g < 0.75 else 12
    meses(c, x0, 330, wq, max(aa, ab), ativos=(12 if t < C["07.c"] else n))
    if ab > 0:
        chave(c, x0 + 4, x0 + wq - 4, 450, "", GREEN, ab)
        linha(c, [("24% ao ano", PURPLE), ("  ÷ 12  =  ", INK), ("2% ao mês", GREEN)], W / 2, 560, 46, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        itens = [("2% a.m.", "1 mês"), ("6% a.t.", "trimestre: 3 meses"), ("12% a.s.", "semestre: 6 meses"),
                 ("24% a.a.", "1 ano: 12 meses")]
        for k, (s, sub) in enumerate(itens):
            ak = ep(t, C["07.c"] + k * 1.1, 0.4)
            x = 330 + k * 420
            chip(c, s, x, 680, GREEN if k == 0 else PURPLE, ak, 34, w=250)
            text(c, sub, x, 760, 22, "bold", GRAY, ak)
            if k:
                text_mid(c, "=", x - 210, 680, 40, "black", INK2, ak)


def b_aviso(c, t, C, B):
    head(c, t, B["start"], "ATENÇÃO", "DIVIDIR POR 12 SÓ VALE AQUI", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        boxed(c, 260, 260, 640, 360, GREEN, aa, 0.08)
        text(c, "JUROS SIMPLES", 580, 330, 36, "black", GREEN, aa)
        linha(c, [("2% a.m. = 24% a.a.", INK)], 580, 450, 44, aa)
        conferido(c, "taxa proporcional", 440, 560, aa, True, 32)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        boxed(c, 1020, 260, 640, 360, RED, ab, 0.06)
        text(c, "JUROS COMPOSTOS", 1340, 330, 36, "black", RED, ab)
        linha(c, [("2% a.m. ≠ 24% a.a.", RED)], 1340, 450, 44, ab)
        conferido(c, "a conversão é outra", 1180, 560, ab, False, 32)
        pill(c, "série própria: Taxas equivalentes e inflação", W / 2, 720, PURPLE, size=26,
             a=ep(t, C["08.b"] + 2.4, 0.4), anchor="center")


# ======================================================================
# bloco c — o sentido da conversão
# ======================================================================

def b_sentido(c, t, C, B):
    head(c, t, B["start"], "MULTIPLICA OU DIVIDE?", "PERÍODO MAIOR, TAXA MAIOR", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 260, 110, 80, 12, mix("#FFFFFF", GREEN, 0.22), aa)
        text(c, "1 mês", 315, 310, 24, "black", INK, aa)
        rrect(c, 260, 370, 1400 * ep(t, C["09.a"] + 0.6, 1.4), 80, 12, mix("#FFFFFF", PURPLE, 0.20), aa)
        text(c, "1 ano = 12 meses: o dinheiro fica alugado 12 vezes mais", 960, 420, 28, "black", PURPLE,
             ep(t, C["09.a"] + 1.8, 0.4))
        text(c, "PERÍODO MAIOR, TAXA MAIOR", W / 2, 530, 40, "black", PURPLE, ep(t, C["09.a"] + 3.0, 0.4))
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 600, 660, 160, 24, mix("#FFFFFF", GREEN, 0.10), ab)
        linha(c, [("mensal", INK), ("  →  ", INK2), ("anual", INK)], 590, 650, 38, ab)
        linha(c, [("× 12", GREEN)], 590, 720, 50, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 600, 660, 160, 24, mix("#FFFFFF", PURPLE, 0.08), acc)
        linha(c, [("anual", INK), ("  →  ", INK2), ("mensal", INK)], 1330, 650, 38, acc)
        linha(c, [("÷ 12", PURPLE)], 1330, 720, 50, acc)


def b_atalho_sent(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "A ANUAL É SEMPRE A MAIOR", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    K.atalho(c, 260, 210, 1400, 130, "ATALHO", ["a taxa ANUAL é sempre a MAIOR das duas"], aa, 42)
    if aa > 0:
        rrect(c, 300, 420, 620, 150, 24, mix("#FFFFFF", GREEN, 0.10), aa)
        linha(c, [("2% a.m.  →  ", INK), ("24% a.a.", GREEN)], 610, 495, 46, aa)
        check_icon(c, 880, 470, 30, aa, GREEN)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 420, 620, 150, 24, mix("#FFFFFF", RED, 0.08), ab)
        linha(c, [("2% a.m.  →  ", INK), ("0,17% a.a.", RED)], 1310, 495, 46, ab)
        check_icon(c, 1580, 470, 30, ab, RED, "x")
        selo(c, 1310, 680, ep(t, C["10.b"] + 2.2, 0.4), "ENCOLHEU? INVERTEU", RED, -3, 38)


# ======================================================================
# bloco d — o ano comercial
# ======================================================================

def b_comercial(c, t, C, B):
    head(c, t, B["start"], "PRAZO EM DIAS", "O ANO COMERCIAL", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        cal_mes(c, 260, 260, aa, int(30 * ep(t, C["11.a"] + 0.6, 1.6)), BLUE)
        boxed(c, 680, 250, 520, 320, BLUE, aa, 0.08)
        text(c, "ANO COMERCIAL", 940, 310, 34, "black", BLUE, aa)
        linha(c, [("mês = ", INK), ("30 dias", BLUE)], 940, 410, 42, aa)
        linha(c, [("ano = ", INK), ("360 dias", BLUE)], 940, 490, 42, ep(t, C["11.a"] + 2.0, 0.4))
        text(c, "é o que as questões usam", 940, 620, 26, "bold", GRAY, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        boxed(c, 1260, 250, 420, 320, AMBER, ab, 0.08)
        text(c, "ANO CIVIL", 1470, 310, 34, "black", AMBER, ab)
        linha(c, [("365 dias", AMBER)], 1470, 430, 48, ab)
        text(c, "só se o enunciado", 1470, 510, 24, "black", INK2, ab)
        text(c, "avisar", 1470, 545, 24, "black", INK2, ab)


# ======================================================================
# bloco e — os 45 dias e o caminho mais limpo
# ======================================================================

def b_dias45(c, t, C, B):
    head_seq(c, t, C, [("12", "EXEMPLO: 45 DIAS", "CAMINHO 1: EM ANOS", PURPLE),
                       ("13", "EXEMPLO: 45 DIAS", "CAMINHO 2: EM MESES", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            linha(c, [("capital: ", GRAY), ("R$ 3.000,00", INK)], W / 2, 520, 32, aa)
        g = ep(t, C["12.b"] + 1.6, 0.6)
        ficha(c, 560, 380, "TAXA", "24%", "ao ano", PURPLE, aa, h=170, vsize=60)
        if g < 0.5:
            ficha(c, 1360, 380, "TEMPO", "45", "dias", BLUE, aa, h=170, vsize=60)
        else:
            ficha(c, 1360, 380, "TEMPO", "45/360", "de ano", BLUE, aa, h=170, vsize=40, ucol=GREEN)
        cadeado(c, W / 2, 390, 60, aa, ep(t, C["12.b"] + 2.4, 0.5))
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            K.expr(c, "3.000 · 0,24 · 45/360 =", 820, 650, 54, acc)
            linha(c, [("R$ 90,00", GREEN)], 1460, 650, 64, ep(t, C["12.c"] + 3.0, 0.4))
        return
    aa = ep(t, C["13.a"], 0.5)
    ficha(c, 560, 330, "TAXA", "2%", "ao mês", PURPLE, aa, h=170, vsize=60, ucol=GREEN)
    ficha(c, 1360, 330, "TEMPO", "1,5", "mês", BLUE, aa, h=170, vsize=60, ucol=GREEN)
    cadeado(c, W / 2, 340, 60, aa, 1.0)
    if aa > 0:
        text(c, "24% ÷ 12", 560, 460, 24, "bold", GRAY, aa)
        text(c, "45 ÷ 30", 1360, 460, 24, "bold", GRAY, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("1 mês: 2% de 3.000 = ", INK), ("R$ 60,00", BLUE)], W / 2, 560, 40, ab)
        linha(c, [("1,5 mês: 60 × 1,5 = ", INK), ("R$ 90,00", GREEN)], W / 2, 630, 40, ep(t, C["13.b"] + 1.8, 0.4))
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 760, acc, "O MESMO RESULTADO: R$ 90,00", GREEN, -2, 36)


def b_facil(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TRADUZA O QUE FICA LIMPO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 120, "ATALHO", ["traduza o que deixar a conta MAIS LIMPA"], aa, 40)
    if aa > 0:
        linha(c, [("8 meses", BLUE), ("  a  ", INK2), ("18% ao ano", PURPLE)], W / 2, 390, 42, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        boxed(c, 240, 450, 680, 300, AMBER, ab, 0.08)
        text(c, "tempo em anos", 580, 510, 30, "black", AMBER, ab)
        K.expr(c, "8/12 = 0,666... ano", 580, 610, 48, ab)
        text(c, "dízima: conta chata", 580, 710, 26, "black", AMBER, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        boxed(c, 1000, 450, 680, 300, GREEN, acc, 0.10)
        text(c, "taxa em meses", 1340, 510, 30, "black", GREEN, acc)
        linha(c, [("18% ÷ 12 = ", INK), ("1,5% a.m.", GREEN)], 1340, 605, 44, acc)
        linha(c, [("1,5% × 8", GREEN)], 1340, 680, 44, acc)
        check_icon(c, 1640, 490, 28, acc, GREEN)


# ======================================================================
# bloco f — o boleto atrasado
# ======================================================================

def b_boleto_def(c, t, C, B):
    head(c, t, B["start"], "O BOLETO ATRASADO", "DUAS COBRANÇAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    ingresso(c, 560, 400, "2%", aa, w=420, h=210)
    if aa > 0:
        text(c, "MULTA: fixa, cobrada uma vez só", 560, 560, 28, "black", BLUE, aa)
        text(c, "1 dia ou 20 dias: a mesma", 560, 610, 24, "bold", GRAY, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        d = int(30 * ep(t, C["15.b"] + 0.6, 4.0))
        taximetro(c, 1360, 400, d, "dia a dia", ab)
        text(c, "JUROS DE MORA: mora = atraso", 1360, 560, 28, "black", BLUE, ab)
        text(c, "taxa mensal, proporcional aos dias", 1360, 610, 24, "bold", GRAY, ab)
        pill(c, "pro rata die = proporcional ao dia", 1360, 670, BLUE, size=22, a=ep(t, C["15.b"] + 4.0, 0.4),
             anchor="center")
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        regra(c, "multa = ingresso  ·  juros de mora = taxímetro", W / 2, 770, acc, 36)


def b_boleto(c, t, C, B):
    head(c, t, B["start"], "NA PRÁTICA", "CONTA DE R$ 450,00", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    boleto(c, 200, 200, 560, 420, [("valor: R$ 450,00", INK), ("multa: 2%", AMBER), ("juros: 1% ao mês", PURPLE),
                                   ("atraso: 10 dias", RED)], aa)
    ab = ep(t, C["16.b"], 0.5)
    ingresso(c, 1050, 300, "R$ 9,00", ab, w=380, h=170)
    if ab > 0:
        text(c, "450 × 0,02", 1050, 420, 26, "bold", GRAY, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        d = int(10 * ep(t, C["16.c"] + 2.4, 2.0))
        taximetro(c, 1500, 310, d, f"R$ {d * 0.15:.2f}".replace(".", ","), acc, w=360, h=200)
        text(c, "R$ 4,50 por mês · 10 dias = 1/3", 1500, 450, 24, "bold", GRAY, acc)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        rrect(c, 840, 520, 860, 220, 24, mix("#FFFFFF", GREEN, 0.10), ad)
        linha(c, [("450 + 9,00 + 1,50", INK)], 1270, 590, 40, ad)
        linha(c, [("= R$ 460,50", GREEN)], 1270, 670, 60, ep(t, C["16.d"] + 1.0, 0.4))


def b_atalho_dias(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DIAS ÷ 30", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 120, "ATALHO", ["dias ÷ 30 = a FRAÇÃO do mês"], aa, 40)
    if aa > 0:
        cal_mes(c, 300, 380, aa, 10, AMBER)
        fmid(c, "10 dias = 1/3 do mês", 445, 720, 32, "black", AMBER, aa)
        a2 = ep(t, C["17.a"] + 2.4, 0.4)
        cal_mes(c, 780, 380, a2, 15, GREEN)
        fmid(c, "15 dias = 1/2 do mês", 925, 720, 32, "black", GREEN, a2)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        boxed(c, 1240, 400, 440, 300, PURPLE, ab, 0.08)
        text(c, "1. juros do mês", 1460, 480, 32, "black", PURPLE, ab)
        text(c, "INTEIRO", 1460, 525, 32, "black", PURPLE, ab)
        text(c, "2. pegue só", 1460, 600, 32, "black", PURPLE, ab)
        text(c, "a fração", 1460, 645, 32, "black", PURPLE, ab)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "TRADUZA A TAXA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        linha(c, [("capital: ", GRAY), ("R$ 1.200,00", INK), ("   ·   juros = ?", PURPLE)], 1360, 510, 30, aa)
    g = ep(t, C.get("19.a", 1e9) + 1.6, 0.5) if t >= C["19"] else 0
    if g < 0.5:
        ficha(c, 560, 380, "TAXA", "36%", "ao ano", PURPLE, aa, h=170, vsize=60)
    else:
        ficha(c, 560, 380, "TAXA", "3%", "ao mês", PURPLE, aa, h=170, vsize=60, ucol=GREEN)
    ficha(c, 1360, 380, "TEMPO", "4", "meses", BLUE, aa, h=170, vsize=60)
    cadeado(c, W / 2, 390, 60, aa, ep(t, C.get("19.a", 1e9) + 2.2, 0.5) if t >= C["19"] else 0)
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 620)
    if t < C["19"]:
        return
    a1 = ep(t, C["19.a"], 0.5)
    if a1 > 0:
        pill(c, "36% ÷ 12 = 3% ao mês", 560, 500, GREEN, size=26, a=a1, anchor="center")
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0:
        linha(c, [("1 mês: 3% de 1.200 = ", INK), ("R$ 36,00", BLUE)], W / 2, 610, 44, ab)
    acc = ep(t, C["19.c"], 0.5)
    if acc > 0:
        linha(c, [("4 meses: 36 × 4 = ", INK), ("R$ 144,00", GREEN)], W / 2, 710, 52, acc)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Taxa e tempo falam a mesma língua.",
          "Traduza só um dos dois.",
          "A multa é o ingresso; os juros de mora são o taxímetro."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "35"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Taxa anual com tempo em meses: 18% × 8", "os dois números estão ali no enunciado",
          "8 meses não são 8 anos: iguale as unidades antes"),
         ("Converter a taxa E o tempo", "traduzir tudo parece capricho · 24% com 24 meses: 5.760 (12× mais) · 2% com 2: "
          "40 (12× menos)", "só um: 1.000 × 0,02 × 24 = R$ 480,00"),
         ("2% ao mês ÷ 12 para achar a taxa anual", "o 12 sempre aparece na conversão",
          "período maior, taxa maior: 2% a.m. = 24% a.a."),
         ("Ler 1 ano e 3 meses como 1,3 ano", "no dinheiro e no metro a vírgula funciona assim",
          "são 15 meses, ou 1,25 ano"),
         ("Boleto: esquecer uma cobrança, o mês inteiro por poucos dias, ou taxa mensal como diária",
          "o boleto só mostra as porcentagens", "o ingresso uma vez + o taxímetro só dos dias")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23", "24", "25"], ERROS)


# ======================================================================
# questões
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


ALTS1 = [("A", "R$ 600,00", "", GREEN), ("B", "R$ 900,00", "um ano inteiro", RED),
         ("C", "R$ 5.600,00", "montante, não juros", RED), ("D", "R$ 7.200,00", "18% com 8", RED),
         ("E", "R$ 12.200,00", "montante da D", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "TAXA ANUAL, PRAZO EM MESES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    yend = _enunciado(c, [("Um capital de R$ 5.000,00 foi emprestado a juros simples, à taxa de 18% ao ano. Os juros "
                           "devidos após 8 meses são de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
         align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 44, C["27.ok"], "A", cues_in, cues_x, gap=34)
    if t >= C["27"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["27"], 0.4))
        unidades(c, 210, y0 + 20, "18% ao ano", "8 meses", ep(t, C["27.a"], 0.4), ep(t, C["27.b"] + 1.0, 0.4))
        linha(c, [("18% ÷ 12 = ", INK), ("1,5% ao mês", GREEN)], 540, y0 + 140, 30, ep(t, C["27.b"], 0.4))
        linha(c, [("1 mês: 75  ·  8 meses: ", INK), ("R$ 600,00", GREEN)], 540, y0 + 205, 30, ep(t, C["27.c"], 0.4))
        conferido(c, "1 ano: 900 · 2/3 do ano: 600", 220, y0 + 275, ep(t, C["27.d"], 0.4), True, 26)
    af = ep(t, C["28.f"], 0.5)
    if af > 0:
        selo(c, 1340, 790, af, "D E E: MAIS QUE O PRÓPRIO CAPITAL", AMBER, -2, 26)


ALTS2 = [("A", "R$ 3.000,00", "só os juros", RED), ("B", "R$ 10.250,00", "2% como anual", RED),
         ("C", "R$ 12.400,00", "só 12 meses", RED), ("D", "R$ 13.000,00", "", GREEN),
         ("E", "R$ 13.120,00", "leu 1,3 ano", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · NÓS FAZEMOS", "PRAZO MISTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    yend = _enunciado(c, [("Um empréstimo de R$ 10.000,00 foi feito a juros simples de 2% ao mês e será quitado em um "
                           "único pagamento após 1 ano e 3 meses. O valor desse pagamento é", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["30"], 0.3)),
         align="left")
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 44, C["30.ok"], "D", cues_in, cues_x, gap=34)
    ap = ep(t, C["29.p"], 0.4) * (1 - ep(t, C["30"], 0.3))
    if ap > 0:
        pill(c, "taxa: 2% ao ___ ?", 540, yend + 60, AMBER, size=30, a=ap, anchor="center")
    if t >= C["30"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["30"], 0.4))
        unidades(c, 210, y0 + 20, "2% ao mês", "1 ano e 3 meses", ep(t, C["30"], 0.4), ep(t, C["30.a"] + 2.0, 0.4))
        linha(c, [("12 + 3 = ", INK), ("15 meses", BLUE), ("  ·  2% × 15 = ", INK), ("30%", PURPLE)], 540, y0 + 140, 28,
              ep(t, C["30.a"], 0.4))
        linha(c, [("juros: 30% de 10.000 = 3.000", INK)], 540, y0 + 200, 28, ep(t, C["30.b"], 0.4))
        linha(c, [("pagamento: ", INK), ("R$ 13.000,00", GREEN)], 540, y0 + 262, 32, ep(t, C["30.c"], 0.4))


ALTS3 = [("A", "R$ 301,50", "só os juros", RED), ("B", "R$ 303,00", "mês inteiro, sem multa", RED),
         ("C", "R$ 306,00", "só a multa", RED), ("D", "R$ 307,50", "", GREEN), ("E", "R$ 351,00", "1% ao dia", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · VOCÊ FAZ", "BOLETO PAGO COM ATRASO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["32.a"], 0.4)
    yend = _enunciado(c, [("Uma conta de R$ 300,00 foi paga com 15 dias de atraso. Há multa de 2% sobre o valor da conta "
                           "e juros de mora de 1% ao mês, simples e proporcionais aos dias de atraso (mês de 30 dias). "
                           "O valor pago foi de", INK)], a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["33"], 0.3)),
         align="left")
    cues_in = {L: C[f"32.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"34.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 44, C["33.ok"], "D", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["32.end"] - 1.9, 540, yend + 130)
    if t >= C["33"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["33"], 0.4))
        linha(c, [("ingresso: 2% de 300 = ", INK), ("6,00", AMBER)], 540, y0 + 60, 30, ep(t, C["33.a"], 0.4))
        linha(c, [("taxímetro: 3,00 por mês · 15 dias = ½: ", INK), ("1,50", PURPLE)], 540, y0 + 125, 24,
              ep(t, C["33.b"], 0.4))
        linha(c, [("300 + 6 + 1,50 = ", INK), ("R$ 307,50", GREEN)], 540, y0 + 195, 34, ep(t, C["33.c"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUE FORMA APARECE?", PURPLE)
    aa = ep(t, C["36.a"], 0.5)
    x0, y0, w, h = 420, 240, 1080, 520
    if aa > 0:
        line(c, x0, y0 + h, x0 + w, y0 + h, INK, aa, 4)
        line(c, x0, y0, x0, y0 + h, INK, aa, 4)
        text(c, "meses", x0 + w - 40, y0 + h + 44, 24, "bold", GRAY, aa)
        text(c, "montante (R$)", x0 + 10, y0 - 20, 24, "bold", GRAY, aa, align="left")
        linha(c, [("R$ 1.000,00 a 5% ao mês", INK)], W / 2, y0 + 30, 36, aa)
    vals = [1000, 1050, 1100, 1150]
    for k, v in enumerate(vals):
        ak = ep(t, C["36.b"] + k * 1.0, 0.4) if k else ep(t, C["36.a"] + 1.0, 0.4)
        if ak <= 0:
            continue
        X = x0 + 60 + k * 230
        Y = y0 + h - 60 - (v - 1000) * 2.2
        c.drawCircle(X, Y, 16, paint(PURPLE, ak))
        text(c, f"{v // 1000}.{v % 1000:03d}", X, Y - 30, 26, "black", PURPLE, ak)
        text(c, str(k), X, y0 + h + 40, 22, "bold", GRAY, ak)
    acc = ep(t, C["36.c"], 0.5)
    if acc > 0:
        text(c, "?", 1380, 420, 120, "black", AMBER, acc)
    pill(c, "ep. 3 · o montante no gráfico", W / 2, 830, PURPLE, size=30, a=ep(t, C["36.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"],
        "Já pagou um boleto atrasado sem saber a conta?", canal="no Estudativo", anki=C["37.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, regra=b_regra,
              proporcionais=b_proporcionais, aviso=b_aviso, sentido=b_sentido, atalho_sent=b_atalho_sent,
              comercial=b_comercial, dias45=b_dias45, facil=b_facil, boleto_def=b_boleto_def, boleto=b_boleto,
              atalho_dias=b_atalho_dias, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q2=b_q2,
              q3=b_q3, ponte=b_ponte, cta=b_cta)
