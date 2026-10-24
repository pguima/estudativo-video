"""Visual — Função Modular e Funções por Partes, Episódio 1: funções por partes, ache a faixa antes de calcular (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: chave() (a lei com chave e as condições de cada linha), predio() (os três andares/faixas, com o
elevador levando o valor até o andar que acende e só a regra dele à mostra), grafico_agua() (desenhado pedaço por pedaço:
horizontal, inclinação 6, inclinação 9), escada_estac() (gráfico em escada com bolinhas cheias e vazias), linha().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum044", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                 K.selo, K.pause_timer)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_partes_ep1_faixas_andares.mp4"
CARD_R = K.CARD_R
ANDAR = [BLUE, PURPLE, AMBER]   # cor de cada andar/faixa (só para separar; a regra acesa vem em roxo)


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


def chave_path(c, x, y0, y1, a, col=INK, wd=5):
    """chave '{' de altura y1 - y0, com a ponta em x"""
    if a <= 0:
        return
    m = (y0 + y1) / 2
    k = 26
    pth = skia.Path()
    pth.moveTo(x + k, y0)
    pth.cubicTo(x + 4, y0, x + k, m - 10, x, m)
    pth.cubicTo(x + k, m + 10, x + 4, y1, x + k, y1)
    p = paint(col, a, stroke=wd, cap_round=True)
    c.drawPath(pth, p)


def chave(c, x, y, linhas, a, size=34, lh=74, acesa=-1, prefixo="f(x) =", wreg=None, cols=None):
    """lei por partes: prefixo, chave e linhas [(regra, condição)]. acesa = linha destacada (as outras ficam claras)."""
    if a <= 0:
        return
    pw = ftext_w(prefixo, "black", size) + 20
    n = len(linhas)
    yc = y + (n - 1) * lh / 2
    ftext(c, prefixo, x, yc + size * 0.36, size, "black", INK, a, align="left")
    chave_path(c, x + pw, y - lh * 0.45, y + (n - 1) * lh + lh * 0.45, a)
    wreg = wreg or max(ftext_w(r, "black", size) for r, _ in linhas) + 40
    for k, (reg, cond) in enumerate(linhas):
        yy = y + k * lh
        ak = a * (0.3 if 0 <= acesa != k else 1.0)
        if acesa == k:
            rrect(c, x + pw + 30, yy - lh * 0.42, wreg + ftext_w(cond, "bold", size * 0.85) + 40, lh * 0.84, 14,
                  mix("#FFFFFF", PURPLE, 0.16), a)
        ftext(c, reg, x + pw + 44, yy + size * 0.36, size, "black", (cols[k] if cols else PURPLE), ak, align="left")
        ftext(c, cond, x + pw + 44 + wreg, yy + size * 0.32, size * 0.85, "bold", GRAY, ak, align="left")


AGUA = [("40", "se 0 ≤ x ≤ 10"), ("40 + 6(x − 10)", "se 10 < x ≤ 20"), ("100 + 9(x − 20)", "se x > 20")]


def predio(c, x, y, a, aceso=-1, prog=0.0, valor=None, regras=False, fw=720, fh=128):
    """prédio de 3 andares (de baixo para cima = faixas 1, 2, 3). Elevador à esquerda leva o chip 'valor' até o andar
    'aceso' (prog 0..1). Só a regra do andar aceso aparece (ou todas, se regras=True)."""
    if a <= 0:
        return
    faixas = ["até 10 m³", "de 10 a 20 m³", "acima de 20 m³"]
    ex = x
    ew = 130
    bx = x + ew + 10
    total = 3 * fh
    # telhado
    pth = skia.Path()
    pth.moveTo(bx - 20, y); pth.lineTo(bx + fw / 2, y - 70); pth.lineTo(bx + fw + 20, y); pth.close()
    c.drawPath(pth, paint("#C9C2B0", a))
    # poço do elevador
    rrect(c, ex, y, ew, total, 10, "#E8E5DC", a)
    for k in range(3):
        j = 2 - k          # andar k (0 = térreo) é desenhado de baixo para cima
        yy = y + j * fh
        lit = (k == aceso)
        col = ANDAR[k]
        rrect(c, bx, yy + 4, fw, fh - 8, 12, mix("#FFFFFF", col, 0.30 if lit else 0.08), a, shadow=lit)
        if lit:
            rrect(c, bx, yy + 4, 14, fh - 8, 6, col, a)
        for w_ in range(3):
            rrect(c, bx + fw - 150 + w_ * 46, yy + 30, 32, fh - 60, 6, "#FFE9A8" if lit else "#FFFFFF", a * 0.9)
        text(c, f"{k + 1}º ANDAR", bx + 40, yy + 44, 22, "black", col, a, align="left", tracking=1)
        ftext(c, faixas[k], bx + 40, yy + 92, 30, "black", INK if (lit or aceso < 0) else GRAY, a, align="left")
        if regras or lit:
            ftext(c, AGUA[k][0], bx + 300, yy + 80, 34, "black", PURPLE, a * (1 if lit or aceso < 0 else 0.4),
                  align="left")
    # cabine
    if valor is not None:
        k = max(0, aceso)
        y_ch = y + total - fh / 2 - prog * k * fh
        rrect(c, ex + 10, y_ch - fh / 2 + 12, ew - 20, fh - 24, 10, INK2, a)
        fmid(c, valor, ex + ew / 2, y_ch, 30, "black", "#FFFFFF", a)


def grafico_agua(c, x0, y0, w, h, a, prog=3.0, marca=None, rot=True):
    """gráfico da conta de água: x de 0 a 30 m³, y de 0 a 200 reais. prog 0..3 desenha os 3 pedaços em sequência."""
    if a <= 0:
        return
    ox, oy = x0 + 80, y0 + h - 60
    sx, sy = (w - 130) / 30, (h - 100) / 200
    P = lambda xx, yy: (ox + xx * sx, oy - yy * sy)
    line(c, ox, oy, x0 + w - 20, oy, INK2, a, 3)
    line(c, ox, oy, ox, y0 + 10, INK2, a, 3)
    ftext(c, "m³", x0 + w - 10, oy - 18, 24, "black", INK2, a)
    ftext(c, "R$", ox - 40, y0 + 30, 24, "black", INK2, a)
    for v in (10, 20, 30):
        px, py = P(v, 0)
        line(c, px, oy - 8, px, oy + 8, INK2, a, 3)
        ftext(c, str(v), px, oy + 40, 24, "bold", GRAY, a)
    for v in (40, 100):
        px, py = P(0, v)
        line(c, ox - 8, py, ox + 8, py, INK2, a, 3)
        ftext(c, str(v), ox - 22, py + 9, 24, "bold", GRAY, a, align="right")
    segs = [((0, 40), (10, 40), BLUE, "fixo"), ((10, 40), (20, 100), PURPLE, "6 por m³"),
            ((20, 100), (30, 190), AMBER, "9 por m³")]
    for k, ((xa, ya), (xb, yb), col, lab) in enumerate(segs):
        q = max(0.0, min(1.0, prog - k))
        if q <= 0:
            continue
        p0 = P(xa, ya); p1 = P(xa + (xb - xa) * q, ya + (yb - ya) * q)
        line(c, p0[0], p0[1], p1[0], p1[1], col, a, 9)
        if rot and q >= 1:
            mx, my = P((xa + xb) / 2, (ya + yb) / 2)
            pill(c, lab, mx + (0 if k == 0 else -26), my - 46 - (0 if k == 0 else 20), col, size=22, a=a,
                 anchor="center" if k == 0 else "right", bounds=(0, 1920))
    if marca:
        xv, yv = marca
        px, py = P(xv, yv)
        line(c, px, oy, px, py, GRAY, a, 3, dash=(10, 8))
        line(c, ox, py, px, py, GRAY, a, 3, dash=(10, 8))
        c.drawCircle(px, py, 12, paint(GREEN, a))


def escada_estac(c, x0, y0, w, h, a, horas=4, marca=None, bol=1.0, destaca=-1):
    """gráfico em escada do estacionamento (R$ 10 a 1ª hora + R$ 4 por hora adicional ou fração).
    bol = alfa das bolinhas. marca = horas (float) com linha tracejada até o degrau. destaca = índice do degrau."""
    if a <= 0:
        return
    ox, oy = x0 + 80, y0 + h - 60
    sx, sy = (w - 130) / horas, (h - 100) / 30
    P = lambda xx, yy: (ox + xx * sx, oy - yy * sy)
    line(c, ox, oy, x0 + w - 20, oy, INK2, a, 3)
    line(c, ox, oy, ox, y0 + 10, INK2, a, 3)
    ftext(c, "horas", x0 + w - 50, oy + 44, 22, "black", INK2, a)
    ftext(c, "R$", ox - 40, y0 + 30, 24, "black", INK2, a)
    for k in range(horas):
        v0, v1 = k, k + 1
        val = 10 + 4 * k
        p0 = P(v0, val); p1 = P(v1, val)
        col = GREEN if k == destaca else PURPLE
        line(c, p0[0], p0[1], p1[0], p1[1], col, a, 9 if k == destaca else 7)
        ftext(c, str(v1), P(v1, 0)[0], oy + 40, 24, "bold", GRAY, a)
        line(c, P(v1, 0)[0], oy - 8, P(v1, 0)[0], oy + 8, INK2, a, 3)
        ftext(c, str(val), ox - 22, p0[1] + 9, 22, "bold", GRAY, a, align="right")
        if bol > 0:
            c.drawCircle(p0[0], p0[1], 11, paint("#FFFFFF", a * bol))
            c.drawCircle(p0[0], p0[1], 11, paint(col, a * bol, stroke=4))
            c.drawCircle(p1[0], p1[1], 12, paint(col, a * bol))
    if marca is not None:
        k = max(0, int(-(-marca // 1)) - 1)
        val = 10 + 4 * k
        px, py = P(marca, val)
        line(c, px, oy, px, py, GRAY, a, 3, dash=(10, 8))
        c.drawCircle(px, py, 10, paint(GREEN, a))


def placa(c, x, y, a, w=520):
    """placa do estacionamento"""
    if a <= 0:
        return
    rrect(c, x, y, w, 300, 22, "#1F4E9C", a, shadow=True)
    text(c, "E", x + 70, y + 110, 90, "black", "#FFFFFF", a)
    ftext(c, "1ª hora: R$ 10,00", x + 130, y + 90, 36, "black", "#FFFFFF", a, align="left")
    ftext(c, "hora adicional", x + 130, y + 160, 34, "bold", "#FFFFFF", a, align="left")
    ftext(c, "ou fração: R$ 4,00", x + 130, y + 215, 36, "black", "#FFE9A8", a, align="left")


def conta_agua(c, x, y, a, w=440):
    """boleto da conta de água com a tarifa mínima"""
    if a <= 0:
        return
    rrect(c, x, y, w, 300, 14, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 70, 14, BLUE, a)
    text(c, "CONTA DE ÁGUA", x + w / 2, y + 48, 28, "black", "#FFFFFF", a, tracking=1)
    ftext(c, "tarifa mínima", x + 30, y + 130, 28, "bold", GRAY, a, align="left")
    ftext(c, "até 10 m³: R$ 40", x + 30, y + 185, 34, "black", INK, a, align="left")
    for k in range(3):
        rrect(c, x + 30, y + 220 + k * 20, w - 60 - k * 90, 8, 4, "#E6E6E2", a)


def celular(c, x, y, a):
    """tela de celular com a franquia de dados"""
    if a <= 0:
        return
    rrect(c, x, y, 250, 430, 36, INK2, a, shadow=True)
    rrect(c, x + 16, y + 40, 218, 350, 18, "#FFFFFF", a)
    text(c, "FRANQUIA", x + 125, y + 100, 24, "black", BLUE, a, tracking=1)
    rrect(c, x + 36, y + 140, 178, 30, 15, "#E6E6E2", a)
    rrect(c, x + 36, y + 140, 178, 30, 15, BLUE, a)
    ftext(c, "10 GB", x + 125, y + 220, 40, "black", INK, a)
    ftext(c, "passou?", x + 125, y + 290, 26, "bold", GRAY, a)
    ftext(c, "+ excedente", x + 125, y + 340, 28, "black", AMBER, a)


def _enunciado(c, linhas, a, y0=250, size=30, w=720):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 760, y1 - y0, 18, "#FFFFFF", a, shadow=True)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÕES POR PARTES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 240, 600, 260, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "CASA 1", 560, 300, 30, "black", BLUE, aa, tracking=2)
        ftext(c, "10 m³", 560, 390, 70, "black", INK, aa)
        ftext(c, "R$ 40,00", 560, 460, 46, "black", BLUE, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 1060, 240, 600, 260, 22, mix("#FFFFFF", PURPLE, 0.10), ab)
        text(c, "VIZINHA · O DOBRO", 1360, 300, 30, "black", PURPLE, ab, tracking=2)
        ftext(c, "20 m³", 1360, 390, 70, "black", INK, ab)
    acc = ep(t, C["01.c"], 0.5)
    ad = ep(t, C["01.d"], 0.5)
    if acc > 0:
        ftext(c, "R$ 80,00?", 1360, 460, 46, "black", AMBER, acc * (1 - 0.6 * ad))
        if ad > 0:
            strike(c, 1250, 446, 1470, 446, ad, RED, ad)
    if ad > 0:
        rrect(c, 1110, 540, 500, 110, 22, GREEN, 0.15 * ad)
        ftext(c, "R$ 100,00", 1360, 618, 64, "black", GREEN, ad)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        regra(c, "A REGRA MUDOU NO MEIO DO CAMINHO", W / 2, 750, ae, 40, PURPLE)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "ler qualquer tarifa por faixas", "água, luz, imposto"),
            ("02.b", "montar a lei de um plano com franquia", "a fatura do celular"),
            ("02.c", "reconhecer o gráfico de cada uma", "pedaços de reta e escada")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 180 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        ftext(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "f(x)", 560, 290, 34, "black", BLUE, aa)
        text(c, "série de Conceito de Função", 560, 340, 26, "bold", GRAY, aa)
        fmid(c, "recebe um número", 560, 470, 46, "black", INK, aa)
        fmid(c, "→ devolve outro", 560, 550, 46, "black", INK, aa)
    ab = ep(t, C["03.b"], 0.5)
    line(c, 960, 240, 960, 790, "#E6E6E2", ab, 3)
    if ab > 0:
        text(c, "PARTE FIXA + POR UNIDADE", 1370, 290, 32, "black", PURPLE, ab)
        text(c, "série de Função Afim", 1370, 340, 26, "bold", GRAY, ab)
        line(c, 1120, 720, 1640, 720, INK2, ab, 3)
        line(c, 1120, 720, 1120, 400, INK2, ab, 3)
        line(c, 1120, 640, 1600, 450, PURPLE, ab, 8)
        ftext(c, "reta", 1600, 430, 30, "black", PURPLE, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        line(c, 1120, 640, 1440, 400, AMBER, acc, 8)
        pill(c, "mais caro por unidade = mais inclinada", 1380, 770, AMBER, size=24, a=acc, anchor="center")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS COISAS", "QUE VOCÊ CONHECE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    conta_agua(c, 220, 260, aa, 440)
    ab = ep(t, C["04.b"], 0.5)
    celular(c, 830, 240, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        c.save(); c.translate(1220, 280); c.scale(0.95, 0.95)
        placa(c, 0, 0, acc)
        c.restore()
    if aa > 0:
        pill(c, "TARIFA MÍNIMA = paga mesmo gastando pouco", 440, 610, BLUE, size=22, a=ep(t, C["04.a"] + 1.5, 0.4),
             anchor="center")
    if ab > 0:
        pill(c, "FRANQUIA · EXCEDENTE", 955, 710, BLUE, size=22, a=ep(t, C["04.b"] + 2.5, 0.4), anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "A REGRA MUDA CONFORME O USO", W / 2, 790, ad, 36, PURPLE)


# ======================================================================
# bloco a: definição
# ======================================================================

def b_definicao(c, t, C, B):
    head(c, t, B["start"], "FUNÇÃO POR PARTES", "UMA LEI EM CADA FAIXA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 220, 1480, 90, BLUE, aa)
        linha(c, [("FUNÇÃO DEFINIDA POR PARTES", BLUE), (": uma lei diferente em cada faixa", INK)], W / 2, 265, 36, aa)
    ab = ep(t, C["05.b"], 0.5)
    acc = ep(t, C["05.c"], 0.5)
    if ab > 0:
        x0, x1, yy = 300, 1620, 470
        line(c, x0, yy, x1, yy, INK2, ab, 4)
        for k, v in enumerate((0, 10, 20, 30)):
            px = x0 + 60 + k * 400
            line(c, px, yy - 14, px, yy + 14, INK2, ab, 4)
            ftext(c, str(v), px, yy + 54, 30, "bold", GRAY, ab)
        rrect(c, 760, yy - 26, 400, 52, 14, BLUE, 0.35 * ab)
        ftext(c, "FAIXA (intervalo): de 10 a 20", 960, yy - 52, 30, "black", BLUE, ab)
    if acc > 0:
        for px in (760, 1160):
            c.drawCircle(px, 470, 16, paint(AMBER, acc))
        pill(c, "FRONTEIRA", 760, 560, AMBER, size=24, a=acc, anchor="center")
        pill(c, "FRONTEIRA", 1160, 560, AMBER, size=24, a=acc, anchor="center")
    ad = ep(t, C["05.d"], 0.5)
    chave(c, 520, 660, [("regra 1", "condição 1"), ("regra 2", "condição 2")], ad, 32, 64, prefixo="f(x) =", wreg=200)


# ======================================================================
# bloco b: a conta de água
# ======================================================================

def b_agua(c, t, C, B):
    head(c, t, B["start"], "A CONTA DE ÁGUA", "LINHA POR LINHA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    ab = ep(t, C["06.b"], 0.5)
    ad = ep(t, C["06.d"], 0.5)
    n = 1 if ab <= 0 else (2 if ad <= 0 else 3)
    acesa = n - 1
    chave(c, 300, 320, AGUA[:n], aa, 46, 110, acesa=acesa, wreg=470)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 640, 1320, 130, 22, mix("#FFFFFF", AMBER, 0.12), acc * (1 - ad))
        linha(c, [("x − 10", AMBER), (" = o que PASSOU de 10  ·  ", INK), ("R$ 6", PURPLE), (" cada m³ desses", INK)],
              W / 2, 705, 38, acc * (1 - ad))
    if aa > 0:
        pill(c, "tarifa mínima", 1560, 320, BLUE, size=24, a=aa * (1 - ep(t, C["06.b"], 0.3)), anchor="center")


def b_cem(c, t, C, B):
    head(c, t, B["start"], "DE ONDE SAIU O 100?", "A CONTA EM 20 m³", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.4)
    chave(c, 260, 290, AGUA, a0, 34, 76, acesa=2, wreg=330)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        linha(c, [("f(20) = 40 + 6 · 10 = ", INK), ("100", GREEN)], 640, 560, 48, aa)
        pill(c, "conta exatamente em 20 m³", 640, 630, GREEN, size=24, a=aa, anchor="center")
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        regra(c, "CADA FAIXA PARTE DE ONDE A ANTERIOR PAROU", W / 2, 740, ab, 36, PURPLE)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 1240, 470, 420, 190, 20, mix("#FFFFFF", GREEN, 0.10), acc)
        ftext(c, "vizinha: 20 m³", 1450, 530, 32, "black", INK, acc)
        ftext(c, "R$ 100 (não 80)", 1450, 600, 36, "black", GREEN, acc)


# ======================================================================
# bloco c: o método do prédio
# ======================================================================

def b_predio(c, t, C, B):
    head(c, t, B["start"], "26 m³", "EM QUE ANDAR MORA?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    ab = ep(t, C["08.b"], 0.5)
    acc = ep(t, C["08.c"], 0.5)
    sobe = ep(t, C["08.b"] + 0.4, 2.0)
    predio(c, 220, 300, aa, aceso=2 if sobe >= 1 else -1, prog=sobe, valor="26" if ab > 0 else None)
    if ab > 0:
        badge_num(c, 1, 1300, 250, ab, 24, bg=BLUE)
        ftext(c, "descubra o andar", 1340, 260, 32, "black", INK, ab, align="left")
        ftext(c, "26 > 20 → 3º andar", 1340, 310, 30, "bold", AMBER, ab, align="left")
    if acc > 0:
        badge_num(c, 2, 1300, 760, acc, 24, bg=PURPLE)
        ftext(c, "use só essa regra", 1340, 770, 32, "black", INK, acc, align="left")
        rrect(c, 1140, 640, 560, 80, 18, GREEN, 0.14 * acc)
        linha(c, [("100 + 9 · 6 = ", INK), ("R$ 154", GREEN)], 1420, 680, 44, acc)


def b_fronteira(c, t, C, B):
    head(c, t, B["start"], "EXATAMENTE 20?", "OLHE O SINAL", AMBER)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    ab = ep(t, C["09.b"], 0.5)
    chave(c, 260, 290, AGUA, a0, 36, 80, acesa=1 if ab > 0 else -1, wreg=340)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, 1260, 250, 420, 170, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        linha(c, [("≤", BLUE), ("  inclui a fronteira", INK)], 1470, 305, 32, aa)
        linha(c, [("<", RED), ("  não inclui", INK)], 1470, 375, 32, aa)
    if ab > 0:
        linha(c, [("x = 20 → 2ª linha:  40 + 6 · 10 = ", INK), ("100", GREEN)], 760, 600, 40, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        linha(c, [("3ª linha em 20:  100 + 9 · 0 = ", GRAY), ("100", GRAY)], 760, 680, 34, acc)
        pill(c, "as faixas se encostam: sem salto", 760, 760, GREEN, size=26, a=acc, anchor="center")


def b_atalho_faixa(c, t, C, B):
    head(c, t, B["start"], "ATALHO DA FAIXA", "DA FRONTEIRA PARA CIMA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        K.atalho(c, 260, 240, 1400, 220, "ATALHO · COMECE NA FRONTEIRA DE BAIXO",
                 ["valor na fronteira + taxa da faixa · o pedaço que passou"], aa, 40)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("fronteira 20 → ", INK), ("R$ 100", BLUE), ("   ·   passou ", INK), ("6 m³", AMBER),
                  (" a ", INK), ("R$ 9", PURPLE)], W / 2, 560, 40, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 620, 640, 680, 110, 22, GREEN, 0.14 * acc)
        linha(c, [("100 + 54 = ", INK), ("R$ 154", GREEN)], W / 2, 695, 52, acc)


# ======================================================================
# bloco d: o gráfico
# ======================================================================

def b_grafico(c, t, C, B):
    head(c, t, B["start"], "O GRÁFICO", "PEDAÇO POR PEDAÇO", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    prog = (ep(t, C["11.a"], 1.2) + ep(t, C["11.b"], 1.4) + ep(t, C["11.c"], 1.4))
    grafico_agua(c, 220, 200, 1000, 620, a0, prog)
    rows = [("11.a", "até 10: horizontal", BLUE), ("11.b", "10 a 20: inclinada (6)", PURPLE),
            ("11.c", "acima de 20: mais (9)", AMBER)]
    for j, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a > 0:
            ftext(c, s, 1270, 300 + j * 90 + d, 32, "black", col, a, align="left")
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        boxed(c, 1260, 600, 470, 170, GREEN, ad)
        ftext(c, "inclinação =", 1495, 665, 32, "black", INK, ad)
        ftext(c, "preço por unidade", 1495, 725, 36, "black", GREEN, ad)


# ======================================================================
# bloco e: a escada
# ======================================================================

def b_escada(c, t, C, B):
    head(c, t, B["start"], "QUANDO O GRÁFICO PULA", "A ESCADA DO ESTACIONAMENTO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        c.save(); c.translate(1230, 220); c.scale(0.8, 0.8)
        placa(c, 0, 0, aa)
        c.restore()
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        pill(c, "já visto em Conceito de Função · novo: o desenho", 1440, 500, BLUE, size=22, a=ab, anchor="center")
    acc = ep(t, C["12.c"], 0.5)
    escada_estac(c, 200, 200, 980, 620, acc, bol=0.0)
    if acc > 0:
        pill(c, "GRÁFICO EM ESCADA", 690, 230, PURPLE, size=26, a=acc, anchor="center")
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        rrect(c, 1240, 580, 460, 200, 20, mix("#FFFFFF", GREEN, 0.12), ad)
        ftext(c, "2 h 05 = 3 h", 1470, 645, 40, "black", INK, ad)
        linha(c, [("10 + 2 · 4 = ", INK), ("R$ 18", GREEN)], 1470, 720, 40, ad)
        escada_estac(c, 200, 200, 980, 620, ad, bol=0.0, marca=2 + 5 / 60, destaca=2)


def b_bolinhas(c, t, C, B):
    head(c, t, B["start"], "NA BEIRADA DO DEGRAU", "BOLINHA CHEIA × VAZIA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["13"], 0.4)
    ab = ep(t, C["13.b"], 0.5)
    acc = ep(t, C["13.c"], 0.5)
    ad = ep(t, C["13.d"], 0.5)
    escada_estac(c, 200, 200, 980, 620, a0, bol=ep(t, C["13.a"], 0.5),
                 destaca=0 if acc > 0 and ad <= 0 else (1 if ad > 0 else -1))
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        c.drawCircle(1290, 290, 16, paint(PURPLE, aa))
        ftext(c, "cheia = VALE na fronteira", 1325, 300, 30, "black", INK, aa, align="left")
    if ab > 0:
        c.drawCircle(1290, 370, 16, paint("#FFFFFF", ab))
        c.drawCircle(1290, 370, 16, paint(PURPLE, ab, stroke=5))
        ftext(c, "vazia = NÃO vale", 1325, 380, 30, "black", INK, ab, align="left")
    if acc > 0:
        linha(c, [("1 h exata → ", INK), ("R$ 10", GREEN)], 1280, 540, 36, acc, align="left")
    if ad > 0:
        linha(c, [("1 h 01 min → ", INK), ("R$ 14", AMBER)], 1280, 620, 36, ad, align="left")


def b_atalho_catraca(c, t, C, B):
    head(c, t, B["start"], "ATALHO DO \"OU FRAÇÃO\"", "A CATRACA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        cx, cy = 420, 400
        rrect(c, cx - 20, cy - 140, 40, 280, 10, INK2, aa)
        ang = ep(t, C["14.a"] + 0.4, 1.2) * 120
        import math
        for k in range(3):
            th = math.radians(ang + k * 120)
            line(c, cx, cy, cx + 130 * math.cos(th), cy + 130 * math.sin(th) * 0.5, GREEN, aa, 14)
        ftext(c, "encostou = pagou inteira", cx, 640, 32, "black", GREEN, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rows = ["tire o que a parte fixa cobre", "ARREDONDE O RESTO PARA CIMA", "× tarifa adicional", "+ parte fixa"]
        boxed(c, 760, 230, 920, 380, GREEN, ab, 0.06)
        for j, s in enumerate(rows):
            a, d = rise(t, C["14.b"] + j * 0.8)
            badge_num(c, j + 1, 820, 300 + j * 85 + d, a, 24, bg=GREEN)
            ftext(c, s, 870, 312 + j * 85 + d, 34, "black", AMBER if j == 1 else INK, a, align="left")
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 760, 650, 920, 120, 22, GREEN, 0.14 * acc)
        linha(c, [("2 h 05 − 1 h = 1 h 05 → ", INK), ("2", AMBER), ("  ·  10 + 8 = ", INK), ("R$ 18", GREEN)],
              1220, 710, 38, acc)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "ANDAR PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 215, 1400, 130, 24, "#F7F7F5", aa)
        linha(c, [("academia: ", INK), ("R$ 80", PURPLE), (" até 12 aulas  ·  ", INK), ("R$ 7", PURPLE),
                  (" por aula acima de 12", INK)], W / 2, 280, 40, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("17 aulas", AMBER), (" → paga quanto?", INK)], W / 2, 410, 44, ab)
    pause_timer(c, t, C["15.end"] - 1.9, W / 2, 600)
    if t < C["16"]:
        return
    a1 = ep(t, C["16.a"], 0.4)
    chave(c, 300, 520, [("80", "se 0 ≤ x ≤ 12"), ("80 + 7(x − 12)", "se x > 12")], a1, 34, 80,
          acesa=1 if a1 > 0 else -1, wreg=310)
    if a1 > 0:
        pill(c, "17 > 12 → 2ª faixa", 1350, 520, AMBER, size=28, a=a1, anchor="center")
    ab2 = ep(t, C["16.b"], 0.5)
    if ab2 > 0:
        linha(c, [("passaram 5 · 7 = ", INK), ("35", PURPLE)], 1350, 620, 40, ab2)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        rrect(c, 1080, 680, 540, 100, 20, GREEN, 0.14 * acc)
        linha(c, [("80 + 35 = ", INK), ("R$ 115", GREEN)], 1350, 730, 46, acc)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Primeiro descubra a faixa; depois use só a regra dela.",
          "Cada faixa parte de onde a anterior parou.",
          "Hora ou fração: começou, pagou inteira."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("26 m³ pela 2ª linha: 40 + 6 · 16 = R$ 136", "26 passa de 10, e a 2ª linha começa no 10",
          "a 2ª linha vai só até 20 (≤ 20) · 26 é do 3º andar: R$ 154"),
         ("\"Ou fração\" proporcional: 2 h 30 → 10 + 4 · 1,5 = R$ 16", "parece justo pagar só pelo tempo usado",
          "catraca: a meia hora conta inteira · 10 + 2 · 4 = R$ 18"),
         ("Esquecer a parte fixa: 17 aulas → só 5 · 7 = R$ 35", "a conta nova é sobre o que passou",
          "os R$ 80 continuam · 80 + 35 = R$ 115")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20"], ERROS)


# ======================================================================
# questões
# ======================================================================

ENUN8 = ("Um plano de internet móvel custa R$ 50,00 por mês e inclui 10 GB. Cada GB consumido além da franquia custa "
         "R$ 8,00. Sendo x o consumo mensal em GB e f(x) o valor da fatura em reais, a lei de f é")
ALTS8 = [("A", "50 + 8x, para todo x ≥ 0", "", RED),
         ("B", "50 se 0 ≤ x ≤ 10; 8(x − 10) se x > 10", "", RED),
         ("C", "50 se 0 ≤ x ≤ 10; 50 + 8(x − 10) se x > 10", "", GREEN),
         ("D", "50 se 0 ≤ x ≤ 10; 50 + 0,8(x − 10) se x > 10", "", RED),
         ("E", "50 + 8(x − 10), para todo x ≥ 0", "", RED)]
# os motivos das erradas da Q8 vão no painel da esquerda (o texto das alternativas é longo demais para as etiquetas)
POR8 = [("xa", "A", "cobra todos os GB, até os da franquia"), ("xb", "B", "esquece os R$ 50: com 11 GB, fatura de R$ 8"),
        ("xd", "D", "cobra R$ 0,80 por GB"), ("xe", "E", "vale para todo x: com 5 GB, R$ 10")]

ENUNF = ("Uma transportadora cobra R$ 25,00 para entregar pacotes de até 5 kg e R$ 6,00 por quilograma adicional ou "
         "fração de quilograma adicional. O valor cobrado para entregar um pacote de 8,3 kg é")
ALTSF = [("A", "R$ 43,00", "ignorou a fração", RED), ("B", "R$ 44,80", "proporcional: 6 · 3,3", RED),
         ("C", "R$ 49,00", "", GREEN), ("D", "R$ 49,80", "6 · 8,3: sem a tarifa fixa", RED),
         ("E", "R$ 79,00", "9 kg todos como adicionais", RED)]


def b_q8(c, t, C, B):
    head_seq(c, t, C, [("21", "QUESTÃO 8 · EU FAÇO", "A LEI DO PLANO", BLUE), ("22", "RESOLVENDO", "FAIXAS PRIMEIRO", BLUE),
                       ("23", "E AS ERRADAS?", "UMA POR UMA", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    yend = _enunciado(c, [(ENUN8, INK)], a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["22"], 0.3)),
         align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] + 0.15 * k for k, L in enumerate("ABCDE")}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABDE"}
    ftext(c, "f(x) =", 1000, 240, 28, "black", INK, ep(t, C["21.qa"], 0.4), align="left")
    K.alternativas(c, t, C, ALTS8, 1000, 270, 720, 30, C["22.ok"], "C", cues_in, cues_x, gap=22)
    if t < C["22"]:
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["22"], 0.4))
    if t >= C["23"]:
        for j, (cue, L, s) in enumerate(POR8):
            a = ep(t, C[f"23.{cue}"], 0.4)
            badge_num(c, L, 220, y0 + 50 + j * 64, a, 20, bg=RED)
            ftext(c, s, 256, y0 + 60 + j * 64, 24, "black", RED, a, align="left")
        ae2 = ep(t, C["23.xe2"], 0.5)
        if ae2 > 0:
            linha(c, [("E com x = 0:  50 + 8 · (0 − 10) = ", INK), ("−30", RED)], 550, y0 + 300, 28, ae2)
            selo(c, 550, y0 + 355, ae2, "FATURA NEGATIVA", RED, -4, 28)
        return
    aa = ep(t, C["22.a"], 0.4)
    ab = ep(t, C["22.b"], 0.4)
    chave(c, 200, y0 + 70, [("50", "se 0 ≤ x ≤ 10"), ("50 + 8(x − 10)", "se x > 10")], aa, 28, 60,
          acesa=1 if ab > 0 else 0, wreg=250)
    conferido(c, "f(10) = 50 pelas duas linhas: sem salto", 200, y0 + 210, ep(t, C["22.c"], 0.4), True, 24)
    conferido(c, "f(15) = 50 + 40 = 90", 200, y0 + 260, ep(t, C["22.d"], 0.4), True, 24)


def b_qfrete(c, t, C, B):
    head_seq(c, t, C, [("24", "QUESTÃO NOVA · VOCÊ FAZ", "PAUSE E RESOLVA", GREEN),
                       ("25", "CONFERINDO", "ANDAR E CATRACA", GREEN), ("26", "E AS ERRADAS?", "UMA POR UMA", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [(ENUNF, INK)], a0, 240, 26)
    text(c, "Questão inédita no estilo ENEM", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTSF, 1010, 260, 660, 44, C["25.ok"], "C", cues_in, cues_x, gap=34)
    if t < C["25"]:
        pause_timer(c, t, C["24.end"] - 1.9, 1340, 800)
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["25"], 0.4))
    linha(c, [("8,3 > 5 → 2ª faixa", AMBER)], 550, y0 + 50, 30, ep(t, C["25.a"], 0.4))
    linha(c, [("excedente: 8,3 − 5 = ", INK), ("3,3 kg", PURPLE)], 550, y0 + 110, 30, ep(t, C["25.b"], 0.4))
    linha(c, [("ou fração: 3,3 → ", INK), ("4 kg", AMBER)], 550, y0 + 170, 30, ep(t, C["25.c"], 0.4))
    linha(c, [("25 + 4 · 6 = 25 + 24 = ", INK), ("R$ 49", GREEN)], 550, y0 + 240, 34, ep(t, C["25.d"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "FAIXAS PROGRESSIVAS", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        x0, yy = 300, 420
        line(c, x0, yy, 1620, yy, INK2, aa, 4)
        for v, px in (("0", 300), ("2 000", 700), ("5 000", 1100), ("7 000", 1500)):
            line(c, px, yy - 14, px, yy + 14, INK2, aa, 4)
            ftext(c, v, px, yy + 54, 28, "bold", GRAY, aa)
        rrect(c, 700, yy - 30, 400, 60, 12, PURPLE, 0.35 * aa)
        rrect(c, 1100, yy - 30, 400, 60, 12, AMBER, 0.40 * aa)
        ftext(c, "10%", 900, yy - 50, 34, "black", PURPLE, aa)
        ftext(c, "20%", 1300, yy - 50, 34, "black", AMBER, aa)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        linha(c, [("lucro de R$ 7 000 → ", INK), ("20% de 7 000?", AMBER)], W / 2, 600, 44, ab)
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 700, acc, "R$ 1 400 = O DOBRO", RED, -4, 36)
    pill(c, "ep. 2 · cada parte paga a taxa da sua faixa", W / 2, 800, PURPLE, size=28, a=ep(t, C["28.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Sua conta de água tem tarifa mínima?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao, agua=b_agua,
              cem=b_cem, predio=b_predio, fronteira=b_fronteira, atalho_faixa=b_atalho_faixa, grafico=b_grafico,
              escada=b_escada, bolinhas=b_bolinhas, atalho_catraca=b_atalho_catraca, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q8=b_q8, qfrete=b_qfrete, ponte=b_ponte, cta=b_cta)
