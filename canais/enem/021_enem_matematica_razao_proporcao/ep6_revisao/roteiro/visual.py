"""Visual — Razão, Proporção e Regra de Três, Episódio 6: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, pause_timer, selo...).
Índice visual da revisão: os 5 ícones dos episódios (icone()): copos de suco · receita dupla · barras direta/inversa ·
pacote de trabalho · gatos. Desenhos copiados dos visual.py dos eps 1–3 (copo, ovo, xícara, barras, pacote) para manter o traço.
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
_s = importlib.util.spec_from_file_location("comum021", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, expr_w = K.expr, K.expr_w
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_razao_ep6_revisao.mp4"
CARD_R = K.CARD_R
SUCO = "#F08A24"
AGUA = "#7CC3EA"
CASCA = "#FFF4DC"
XIC = "#6FA8DC"
CAIXA = "#C98B4B"
GATO = "#8C8C8C"
DIR, INV = BLUE, PURPLE


# ======================================================================
# peças (mesmo traço dos episódios 1–3)
# ======================================================================

def copo(c, x, y, w, h, col, a=1.0, nivel=0.85):
    """copo (trapézio) com líquido; (x, y) = canto superior esquerdo (ep1)"""
    if a <= 0:
        return
    inset = w * 0.12
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + w, y); p.lineTo(x + w - inset, y + h); p.lineTo(x + inset, y + h); p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    top = y + h * (1 - nivel)
    k = (top - y) / h
    q = skia.Path()
    q.moveTo(x + inset * k, top); q.lineTo(x + w - inset * k, top); q.lineTo(x + w - inset, y + h); q.lineTo(x + inset, y + h); q.close()
    c.drawPath(q, paint(col, a * 0.9))
    c.drawPath(p, paint(INK2, a, stroke=4, cap_round=True))


def ovo(c, x, y, r, a):
    if a <= 0:
        return
    rect = skia.Rect.MakeXYWH(x - r * 0.78, y - r, r * 1.56, r * 2)
    c.drawOval(rect, paint(CASCA, a))
    c.drawOval(rect, paint("#E3C98F", a, stroke=3))
    c.drawCircle(x - r * 0.25, y - r * 0.4, r * 0.18, paint("#FFFFFF", 0.8 * a))


def xicara(c, x, y, s, a):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x - s / 2, y - s * 0.35); p.lineTo(x + s / 2, y - s * 0.35)
    p.lineTo(x + s * 0.38, y + s * 0.35); p.lineTo(x - s * 0.38, y + s * 0.35); p.close()
    c.drawPath(p, paint(XIC, a))
    c.drawCircle(x + s * 0.5, y - s * 0.02, s * 0.17, paint(XIC, a, stroke=s * 0.07))
    c.drawOval(skia.Rect.MakeXYWH(x - s * 0.46, y - s * 0.46, s * 0.92, s * 0.22), paint("#FFFFFF", a))


def pacote(c, x, y, s, col, a):
    """pacote fechado com laço, centrado em (x, y) (ep2/ep4)"""
    if a <= 0:
        return
    w, h = s, s * 0.8
    rrect(c, x - w / 2, y - h / 2, w, h, 10, col, a, shadow=True)
    lid = h * 0.28
    rrect(c, x - w / 2 - 6, y - h / 2 - lid * 0.5, w + 12, lid, 8, mix(col, "#000000", 0.12), a)
    line(c, x, y - h / 2 + 8, x, y + h / 2, "#FFFFFF", a * 0.85, 6)
    line(c, x, y - h / 2 - lid * 0.5, x, y - h / 2 + lid * 0.5, "#FFFFFF", a * 0.85, 6)


def gato(c, x, y, r, a, col=GATO):
    """carinha de gato centrada em (x, y)"""
    if a <= 0:
        return
    for sx in (-1, 1):
        p = skia.Path()
        p.moveTo(x + sx * r * 0.85, y - r * 0.35); p.lineTo(x + sx * r * 0.75, y - r * 1.25); p.lineTo(x + sx * r * 0.2, y - r * 0.8)
        p.close()
        c.drawPath(p, paint(col, a))
    c.drawCircle(x, y, r, paint(col, a))
    for sx in (-1, 1):
        c.drawCircle(x + sx * r * 0.38, y - r * 0.1, r * 0.16, paint("#FFFFFF", a))
        c.drawCircle(x + sx * r * 0.38, y - r * 0.1, r * 0.08, paint(INK, a))
    c.drawCircle(x, y + r * 0.25, r * 0.1, paint("#F2A0A0", a))


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 5 ícones da série (índice da revisão), desenhados em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 copos de suco: 1 concentrado para 3 de água
        copo(c, -150, -70, 62, 92, SUCO, a)
        for j in range(3):
            copo(c, -40 + j * 70, -70, 62, 92, AGUA, a)
        fmid(c, "1 : 3", 0, 62, 34, "black", BLUE, a)
    elif k == 1:    # ep2 a receita dupla
        for j, (no, nx) in enumerate(((2, 3), (4, 6))):
            x0 = -95 + j * 190
            rrect(c, x0 - 82, -84, 164, 132, 14, "#FFFFFF", a, shadow=True)
            for i in range(no):
                ovo(c, x0 - (no - 1) * 15 + i * 30, -50, 13, a)
            for i in range(nx):
                xicara(c, x0 - (nx - 1) * 14 + i * 28, 6, 22, a)
        fmid(c, "=", 0, -20, 34, "black", PURPLE, a)
        fmid(c, "2 : 3 = 4 : 6", 0, 82, 28, "black", PURPLE, a)
    elif k == 2:    # ep3 barras direta × inversa
        for j, (h1, h2, col, lab) in enumerate(((50, 100, DIR, "direta"), (100, 50, INV, "inversa"))):
            x0 = -110 + j * 130
            rrect(c, x0, 40 - 70, 40, 70, 8, col, a)
            rrect(c, x0 + 50, 40 - (h1 if j else h2), 40, h1 if j else h2, 8, mix(col, "#FFFFFF", 0.35), a)
            text(c, lab, x0 + 45, 74, 22, "black", col, a)
        fmid(c, "× 2", -110 + 45, -86, 22, "black", AMBER, a)
    elif k == 3:    # ep4 pacote de trabalho
        pacote(c, 0, -14, 130, CAIXA, a)
        text_mid(c, "1 440", 0, -6, 30, "black", "#FFFFFF", a)
        text(c, "pessoa-hora", 0, 84, 24, "black", INK2, a)
    elif k == 4:    # ep5 os gatos
        gato(c, -62, -18, 40, a)
        gato(c, 62, -18, 40, a)
        rrect(c, -60, 50, 120, 44, 22, mix("#FFFFFF", AMBER, 0.15), a)
        text_mid(c, "2 min", 0, 72, 24, "black", AMBER, a)
    c.restore()


def barras(c, x, y, mode, u, a, l1, l2, col, bw=90, sp=120):
    """duas barras (ep3): DIRETA = crescem juntas; INVERSA = uma cresce e a outra encolhe"""
    if a <= 0:
        return
    h1 = 60 + 160 * u
    h2 = 60 + 160 * u if mode == "direta" else 220 - 160 * u * 0.75
    for k, (h, lab, cc) in enumerate(((h1, l1, col), (h2, l2, mix(col, "#FFFFFF", 0.35)))):
        bx = x + k * sp
        rrect(c, bx, y - h, bw, h, 14, cc, a)
        text(c, lab, bx + bw / 2, y + 32, 22, "black", INK2, a)


def selo_dobro(c, cx, cy, a, g1, g2, txt2, col, w=520):
    """o selo TESTE DO DOBRO (ep3): g1 ×2 → g2 (×2, ÷2 ou ×4)"""
    if a <= 0:
        return
    h = 150
    rrect(c, cx - w / 2, cy - h / 2, w, h, 20, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 20, AMBER, 0.08 * a)
    pill(c, "TESTE DO DOBRO", cx, cy - h / 2, AMBER, size=20, a=a, anchor="center", bounds=(0, 1920))
    text(c, g1, cx - w / 4, cy + 4, 28, "black", INK, a)
    fmid(c, "× 2", cx - w / 4, cy + 42, 30, "black", AMBER, a)
    arrow(c, cx - 40, cy + 20, cx + 40, cy + 20, LIGHT, a, 4, 12)
    text(c, g2, cx + w / 4, cy + 4, 28, "black", INK, a)
    fmid(c, txt2, cx + w / 4, cy + 42, 30, "black", col, a)


def mtext(c, s, cx, cy, size, a, col=None, align="center"):
    """'$...' = matemática (expr); senão texto (ftext, aceita ²)"""
    if a <= 0:
        return
    if s.startswith("$"):
        expr(c, s[1:], cx, cy, size, a, cores={i: col or INK for i in range(30)} if col else None, align=align)
    else:
        fmid(c, s, cx, cy, size, "black", col or INK, a, align=align)


def mtext_w(s, size):
    return expr_w(s[1:], size) if s.startswith("$") else K.ftext_w(s, "black", size)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 360, 190, 1200, 110, BLUE, aa, 0.08)
        text_mid(c, "o assunto de MAIOR RETORNO da Matemática básica", W / 2, 245, 40, "black", INK, aa)
    for k, s in enumerate(("porcentagem", "Física", "Química", "Geografia")):
        chip(c, s, 540 + k * 280, 380, PURPLE, ep(t, C["01.b"] + 0.5 * k, 0.4), 34)
    for k in range(5):
        icone(c, k, 380 + k * 290, 570, 0.8, ep(t, C["01.c"] + 0.2 * k, 0.4))
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "TREINO", 640, 760, PURPLE, ad, 36)
    chip(c, "9 PEGADINHAS", 960, 760, AMBER, ep(t, C["01.d"] + 0.5, 0.4), 36)
    chip(c, "5 QUESTÕES", 1280, 760, GREEN, ep(t, C["01.d"] + 1.0, 0.4), 36)


ONDE = [("02.a", "direto", "escala, velocidade, densidade, consumo, câmbio", "km/L"),
        ("02.b", "porcentagem", "todo aumento e desconto", "$30/100"),
        ("02.c", "Física", "quase toda fórmula é razão", "$v = d/t"),
        ("02.d", "Química", "estequiometria: regra de três com mols", "mol"),
        ("02.e", "Geografia", "densidade demográfica e escala", "hab/km²")]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "ONDE ELE APARECE", "A FERRAMENTA PADRÃO DA PROVA", BLUE)
    for k, (cue, s, sub, f_) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 330
        rrect(c, x - 150, 220 + d, 300, 470, 22, "#F7F7F5", a)
        badge_num(c, k + 1, x, 270 + d, a, 26, bg=BLUE if k == 0 else INK2)
        mtext(c, f_, x, 420 + d, 46, a, PURPLE)
        para(c, s, x, 560 + d, 30, "black", INK, a, 280, 36, align="center")
        para(c, sub, x, 620 + d, 22, "bold", GRAY, a, 270, 28, align="center")
    pill(c, "todo aumento e todo desconto é uma proporção", W / 2, 775, PURPLE, size=28,
         a=ep(t, C["02.b"] + 0.6, 0.5) * (1 - ep(t, C["02.d"], 0.4)), anchor="center")
    pill(c, "mol = a “dúzia” da Química: um jeito de contar partículas", W / 2, 775, BLUE, size=28,
         a=ep(t, C["02.d"] + 0.6, 0.5), anchor="center")


INDICE = [("EP. 1", "depois do “para”, embaixo"), ("EP. 2", "mesma receita · pontas × miolo · pacotinhos de k"),
          ("EP. 3", "o teste do dobro"), ("EP. 4", "uma coluna de cada vez · pacote fixo"),
          ("EP. 5", "a pergunta de ouro")]
IND_CUES = ["03.a", "03.b", "03.c", "04.a", "04.b"]
IND_POS = [(420, 195), (960, 195), (1500, 195), (690, 515), (1230, 515)]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x, y = IND_POS[k]
        rrect(c, x - 245, y, 490, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 245, y, 490, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x, y + 34, PURPLE if on_ else INK2, size=22, a=a, anchor="center", bounds=(0, 1920))
        icone(c, k, x, y + 145, 0.72, a)
        para(c, s, x, y + 258, 24, "black", INK if on_ else INK2, a, 450, 30, align="center")


def b_rendem(c, t, C, B):
    frame(c, t, B["start"], "SE TIVER TEMPO PARA DUAS", "AS QUE MAIS RENDEM", GREEN)
    aa, ab = ep(t, C["05.a"], 0.5), ep(t, C["05.b"], 0.5)
    for k, (a, tit, sub) in enumerate(((aa, "1 · DIRETA OU INVERSA?", "é aí que se erra, não na conta"),
                                       (ab, "2 · QUANDO NÃO VALE", "o ENEM cobra de propósito"))):
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 200, 680, 540, 24, "#F7F7F5", a)
        text(c, tit, x, 262, 36, "black", GREEN, a)
        text(c, sub, x, 312, 26, "bold", INK2, a)
        if k == 0:
            selo_dobro(c, x, 470, a, "operários", "dias", "÷ 2", INV)
            pill(c, "dobrou também? direta · virou metade? inversa", x, 650, DIR, size=24, a=a, anchor="center")
        else:
            icone(c, 4, x, 450, 1.0, a)
            pill(c, "PERGUNTA DE OURO: dobrar a causa dobra MESMO o efeito?", x, 650, AMBER, size=22, a=a, anchor="center")


# treino: (cue da pergunta, cue da resposta, situação, decisão, cor, teste)
TREINO = [("06.b", "07.a", "a quantidade de pães e o preço a pagar", "DIRETA", DIR, "pães × 2 → preço × 2"),
          ("06.c", "07.b", "pintores iguais e os dias para pintar o mesmo muro", "INVERSA", INV, "pintores × 2 → dias ÷ 2"),
          ("06.d", "07.c", "o lado de um quadrado e a área dele", "NEM É PROPORCIONAL", AMBER, "lado × 2 → área × 4"),
          ("06.e", "07.d", "o consumo e a conta de luz com tarifa por faixa", "NEM É PROPORCIONAL", AMBER,
           "o preço muda de faixa")]


def b_treino(c, t, C, B):
    head_seq(c, t, C, [("06", "TREINO-RELÂMPAGO", "DIRETA, INVERSA OU NEM É?", PURPLE),
                       ("07", "CONFERINDO", "O TESTE DO DOBRO DECIDE", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    for k, (s, col) in enumerate((("DIRETA", DIR), ("INVERSA", INV), ("NEM É PROPORCIONAL", AMBER))):
        pill(c, s, 640 + k * 330, 205, col, size=22, a=aa, anchor="center", bounds=(0, 1920))
    for k, (cq, cr, sit, dec, col, teste) in enumerate(TREINO):
        a, d = rise(t, C[cq])
        if a <= 0:
            continue
        x, y = 360 + k * 400, 260 + d
        ar = ep(t, C[cr], 0.4) if t >= C["07"] else 0
        on_ = ar > 0 and (k == 3 or t < C[TREINO[k + 1][1]])
        rrect(c, x - 180, y, 360, 420, 20, mix("#F7F7F5", col, 0.10 * ar), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 180, y, 360, 420), 20, 20), paint(col, a, stroke=4))
        badge_num(c, k + 1, x, y + 46, a, 24, bg=col if ar > 0 else INK2)
        para(c, sit, x, y + 130, 30, "black", INK, a, 310, 38, align="center")
        if ar <= 0:
            fmid(c, "?", x, y + 330, 64, "black", AMBER, a)
        else:
            pill(c, dec, x, y + 310, col, size=22 if len(dec) > 10 else 28, a=ar, anchor="center", bounds=(0, 1920))
            ftext(c, teste, x, y + 382, 22, "black", INK2, ar)
    pause_timer(c, t, C["06.end"] - 1.9, W / 2, 770)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["08"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["08.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["08.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["08.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone, selo de teste, série própria)
VF = [
    ("ônibus: 7 em pé e 21 sentados · em pé PARA O TOTAL", "$7/21", False, "o 21 parece o outro lado da comparação",
     "depois do “para” vai embaixo: o TOTAL, 28", "$7/28 = 1/4", 0, None, None),
    ("10 operários fazem uma obra em 6 dias", "20 operários → 12 dias", False, "a gente monta tudo como direta",
     "o dobro de operários leva METADE dos dias: inversa", "20 operários → 3 dias", 2, "TESTE DO DOBRO", None),
    ("antes de montar a regra de três", "horas e minutos → mesma unidade", True,
     "com unidades misturadas, a conta fecha igual", "e o resultado sai errado, sem alarme", "1 h 30 min = 90 min", 2,
     None, None),
    ("velocidades", "36 km/h = 36 m/s", False, "o número é o mesmo",
     "para passar de km/h a m/s, divida por 3,6", "km/h ÷ 3,6 = m/s", 0, None,
     "SÉRIE PRÓPRIA: Velocidade, densidade e vazão"),
    ("regra de três composta", "cada coluna × incógnita, uma por vez", True,
     "dá vontade de comparar as colunas entre si", "cada suspeito é interrogado SOZINHO", "as outras: fora da sala", 3,
     None, None),
    ("um quadrado", "lado × 2 → área × 2", False, "parece regra de três direta",
     "lado 1, área 1 · lado 2, área 4: a área vai AO QUADRADO", "lado × 2 → área × 4", 4, "TESTE DO DOBRO", None),
    ("juros compostos", "tempo × 2 → juros × 2", False, "nos juros simples é assim mesmo",
     "nos compostos, os juros rendem juros: o crescimento acelera", "só nos juros SIMPLES", 4, None, None),
    ("escalas", "1 : 50 000 é maior que 1 : 250 000", True, "250 000 é um número maior",
     "denominador menor = escala maior, com mais detalhe", "1 : 50 000 > 1 : 250 000", 0, None,
     "SÉRIE PRÓPRIA: Escalas, plantas e mapas"),
    ("2 gatos caçam 2 ratos em 2 minutos", "4 gatos, 4 ratos → 4 min", False, "parece regra de três",
     "cada gato caça o seu rato, todos ao mesmo tempo", "4 gatos, 4 ratos → 2 min", 4, None, None),
]
VF_IDS = [f"{9 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic, teste, serie = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 400, 0.85, a0)
    text(c, ctx, 960, 310, 32, "bold", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = 60
    while mtext_w(conta, sz) > 760:
        sz -= 2
    mtext(c, conta, 960, 410, sz, a0)
    if ar > 0 and not ver:
        w = mtext_w(conta, sz)
        strike(c, 960 - w / 2 - 10, 415, 960 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 400)
    selo(c, 1580, 400, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        text(c, engana, 640 if ver else 520, 552, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        para(c, regra_, 240, 700, 30, "black", GREEN, ag, 760)
        szf = 46
        while mtext_w(fix, szf) > 600:
            szf -= 2
        mtext(c, fix, 1340, 715, szf, ag, GREEN)
        if teste:
            selo(c, 1520, 600, ag, teste, AMBER, -5, 24)
    if serie:
        pill(c, serie, 960, 478, PURPLE, size=22, a=ep(t, q("s"), 0.5), anchor="center", bounds=(0, 1920))


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["18.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["18.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 150 + k * 150
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["18.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 640, GREEN, ab, 44)
    text(c, "no estilo do ENEM", W / 2, 750, 30, "bold", INK2, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · passos: (cue, texto ou '$expr') · ouro/dobro: texto curto dos dois selos

Q = {
    "q1": dict(ids=("19", "20"), titulo="PARA O TOTAL", ok="B", icone=0,
               enun=[("a", "Uma feira de ciências recebeu 40 trabalhos: 25 de escolas públicas e 15 de escolas particulares.",
                      False),
                     ("b", "A razão entre o número de trabalhos de escolas particulares e o número total de trabalhos é",
                      True)],
               alts=[("A", "= 3/5", "comparou com o outro grupo", AMBER), ("B", "= 3/8", "", GREEN),
                     ("C", "= 5/8", "públicas para o total", RED), ("D", "= 5/3", "inverteu a ordem", RED),
                     ("E", "= 8/3", "inverteu a ordem", RED)],
               ouro="regra de três? NÃO: é uma razão", dobro="o dobro de tudo: 30/80 = 3/8",
               passos=[("a", "$particulares/total = 15/40"), ("b", "$15/40 = 3/8")]),
    "q2": dict(ids=("21", "22"), titulo="AS BOMBAS D’ÁGUA", ok="C", icone=2,
               enun=[("a", "Duas bombas d’água iguais esvaziam um tanque em 1 hora e meia.", False),
                     ("b", "Com 3 bombas iguais a essas, no mesmo ritmo, em quantos minutos o mesmo tanque será "
                           "esvaziado?", True)],
               alts=[("A", "1", "fez em horas e não converteu", RED), ("B", "52", "leu 1 h 30 como 1,3 h", AMBER),
                     ("C", "60", "", GREEN), ("D", "90", "achou que nada muda", RED),
                     ("E", "135", "usou direta", AMBER)],
               ouro="o dobro de bombas, metade do tempo? SIM", dobro="bombas × 2 → tempo ÷ 2: INVERSA",
               passos=[("a", "1 h 30 min = 90 min"), ("b", "2 · 90 = 3 · x"), ("c", "x = 60 minutos")],
               plaus="mais bombas, menos tempo ✓"),
    "q3": dict(ids=("23", "24"), titulo="A CONFECÇÃO", ok="E", icone=3,
               enun=[("a", "Numa confecção, 6 costureiras, trabalhando 8 horas por dia, produzem um lote de uniformes "
                           "em 12 dias.", False),
                     ("b", "No mesmo ritmo, 4 costureiras, trabalhando 4 horas por dia, produzirão um lote idêntico em "
                           "quantos dias?", True)],
               alts=[("A", "4 dias", "não inverteu nenhuma coluna", RED), ("B", "9 dias", "não inverteu a das horas", RED),
                     ("C", "16 dias", "não inverteu a das costureiras", RED), ("D", "18 dias", "ignorou as horas", AMBER),
                     ("E", "36 dias", "", GREEN)],
               ouro="lote idêntico: o PACOTE de trabalho é fixo", dobro="costureiras e horas: as duas INVERSAS",
               passos=[("a", "6 · 8 · 12 = 576"), ("b", "4 · 4 · x = 16x"), ("c", "x = 576 ÷ 16 = 36 dias")],
               plaus="menos gente, menos horas → mais dias ✓"),
    "q4": dict(ids=("25", "26"), titulo="O PRÊMIO DA RIFA", ok="A", icone=1,
               enun=[("a", "Três amigas compraram juntas um bilhete de rifa: uma pagou R$ 20,00, outra R$ 30,00 e outra "
                           "R$ 50,00.", False),
                     ("b", "O prêmio de R$ 4 000,00 foi dividido na razão do que cada uma pagou.", False),
                     ("c", "Quanto recebeu a amiga que pagou menos?", True)],
               alts=[("A", "R$ 800,00", "", GREEN), ("B", "R$ 1 200,00", "a parte do meio", RED),
                     ("C", "R$ 1 333,33", "partes iguais", AMBER), ("D", "R$ 1 600,00", "esqueceu a 3ª amiga", RED),
                     ("E", "R$ 2 000,00", "a parte MAIOR", RED)],
               ouro="quem paga o dobro recebe o dobro? SIM", dobro="pagou × 2 → recebe × 2: DIRETA",
               passos=[("a", "20 : 30 : 50 = 2 : 3 : 5"), ("b", "10k = 4 000 → k = 400"), ("c", "2k = R$ 800")],
               plaus="800 + 1 200 + 2 000 = 4 000 ✓"),
    "q5": dict(ids=("27", "28"), titulo="O JARDIM QUADRADO", ok="D", icone=4,
               enun=[("a", "Um jardim quadrado com 4 m de lado precisa de 2 sacos de adubo, espalhados por igual em toda "
                           "a área.", False),
                     ("b", "Quantos sacos serão necessários para um jardim quadrado com 8 m de lado?", True)],
               alts=[("A", "1", "usou inversa", RED), ("B", "2", "achou que nada muda", RED),
                     ("C", "4", "regra de três com o lado", AMBER), ("D", "8", "", GREEN),
                     ("E", "16", "elevou ao cubo", RED)],
               ouro="dobrar o LADO dobra o adubo? NÃO", dobro="lado × 2 → área × 4",
               passos=[("a", "4 · 4 = 16 m²  ·  8 · 8 = 64 m²"), ("b", "área × 4 → 2 · 4 = 8 sacos")],
               plaus="cabem 4 jardins de 4 × 4 ✓"),
}


def selo_linha(c, x, y, w, rotulo, s, col, a):
    """caixa com rótulo (PERGUNTA DE OURO / TESTE DO DOBRO) e uma linha curta"""
    if a <= 0:
        return
    boxed(c, x, y, w, 84, col, a, 0.08)
    pill(c, rotulo, x + 20, y, col, size=18, a=a, bounds=(0, 1920))
    sz = 26
    while K.ftext_w(s, "black", sz) > w - 40:
        sz -= 1
    ftext(c, s, x + 20, y + 54, sz, "black", INK, a, align="left")


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · ESTILO ENEM", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        y = 270
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 620, 40)
            y += h + 18
        icone(c, d["icone"], 380, 715, 0.7, a0 * (1 - sol))
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 680, 715)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 34, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            selo_linha(c, 170, 250, 620, "PERGUNTA DE OURO", d["ouro"], AMBER, ep(t, C[f"{s2}.g"], 0.4) * sol)
            selo_linha(c, 170, 358, 620, "TESTE DO DOBRO", d["dobro"], PURPLE, ep(t, C[f"{s2}.d"], 0.4) * sol)
            yy = 498
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4)
                last = j == len(d["passos"]) - 1
                sz = 36
                while mtext_w(s, sz) > 600:
                    sz -= 2
                fr_ = s.startswith("$") and "/" in s
                if fr_ and j:
                    yy += 18
                mtext(c, s, 480, yy, sz, a, GREEN if last else None)
                yy += 84 if fr_ else 62
            if d.get("plaus"):
                pill(c, d["plaus"], 480, 690, GREEN, size=22, a=ep(t, C[f"{s2}.v"], 0.4), anchor="center",
                     bounds=(0, 1920))
            result_box(c, f"Letra {d['ok']}", 480, 770, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("29.b", "EP. 1", ["razão na ordem certa", "as razões do dia a dia"]),
         ("29.c", "EP. 2", ["a propriedade fundamental", "o truque do k"]),
         ("29.d", "EP. 3", ["direta ou inversa: teste do dobro", "unidades padronizadas"]),
         ("30.a", "EP. 4", ["composta, coluna por coluna", "o atalho dos homens-hora"]),
         ("30.b", "EP. 5", ["quando a regra de três não vale", "conferir se faz sentido", "reduzir ao valor unitário"]),
         ("30.c", "SÉRIES PRÓPRIAS", ["km/h ↔ m/s: Velocidade, densidade e vazão", "escala: Escalas, plantas e mapas"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["29.a"], 0.5) * (1 - ep(t, C["29.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 3 else 1
        x = 190 if col_ == 0 else 1000
        y0 = 200 + sum(len(CHECK[j][2]) * 52 + 34 for j in range(0 if col_ == 0 else 3, k))
        pill(c, ep_, x, y0 + 20, PURPLE if k < 5 else AMBER, size=20, a=a, bounds=(0, 1920))
        dx = 110 if k < 5 else 0
        for j, it in enumerate(itens):
            yy = y0 + 20 + j * 52 + (44 if k == 5 else 0)
            rrect(c, x + dx, yy - 16, 32, 32, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            ftext(c, it, x + dx + 50, yy + 11, 26 if k == 5 else 28, "bold", INK, a, align="left")
    ae = ep(t, C["30.d"], 0.5)
    if ae > 0:
        boxed(c, 190, 680, 700, 110, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 540, 735, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["31.a"], 0.5)
    ab = ep(t, C["31.b"], 0.5)
    for i in range(40):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["31.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 28
        x, y = 250 + k * 82, 230 + r_ * 92
        rrect(c, x, y, 66, 72, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "40 questões", 1450, 320, 52, "black", INK, aa)
    text(c, "e não 30", 1450, 380, 30, "bold", GRAY, aa)
    text(c, "28 acertos = 70%", 1450, 480, 46, "black", GREEN, ab)
    ac = ep(t, C["31.c"], 0.5)
    if ac > 0:
        boxed(c, 250, 650, 1420, 120, AMBER, ac, 0.10)
        text_mid(c, "inclua Física e Química: a regra de três com outra roupa", W / 2, 710, 34, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Grandezas proporcionais", W / 2, 330, 62, "black", PURPLE, aa)
    for k, s in enumerate(("gráfico", "tabela", "constante")):
        a = ep(t, C["32.b"] + 0.5 * k, 0.4)
        if a <= 0:
            continue
        x = 560 + k * 400
        rrect(c, x - 170, 420, 340, 300, 22, mix("#FFFFFF", PURPLE, 0.08), a)
        if k == 0:
            line(c, x - 110, 640, x + 110, 640, INK2, a, 4)
            line(c, x - 110, 640, x - 110, 460, INK2, a, 4)
            line(c, x - 110, 640, x + 100, 480, BLUE, a, 6)
        elif k == 1:
            for r_ in range(3):
                for c_ in range(2):
                    rrect(c, x - 110 + c_ * 115, 465 + r_ * 58, 105, 50, 8, "#FFFFFF", a, stroke=2, stroke_color=INK2)
            for r_, (u, v) in enumerate((("1", "3"), ("2", "6"), ("3", "9"))):
                text_mid(c, u, x - 57, 490 + r_ * 58, 26, "black", INK, a)
                text_mid(c, v, x + 58, 490 + r_ * 58, 26, "black", BLUE, a)
        else:
            fmid(c, "y/x = k", x, 560, 56, "black", PURPLE, a)
        text(c, s, x, 690, 30, "black", INK, a)


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Quantas das 9 frases você acertou?",
        canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, onde=b_onde, indice=b_indice, rendem=b_rendem, treino=b_treino, vf_intro=b_vf_intro, vf=b_vf,
              vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"), q3=faz_questao("q3"),
              q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
