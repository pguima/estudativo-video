"""Visual — Divisão Proporcional, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, pause_timer, selo...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): pacotinhos · fração virando · retângulo de quadradinhos ·
montinho fixo separado. Caixa registradora (registradora()) "fechando o caixa" em cada questão.
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
_s = importlib.util.spec_from_file_location("comum023", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, expr_w = K.expr, K.expr_w
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisao_ep5_revisao.mp4"
CARD_R = K.CARD_R
NOTA = "#2E9E62"          # o dinheiro (pacotinhos), como no ep1
NOTA_ESC = "#1F7A4A"
DONOS = ["#E8743B", "#2BA3B8", "#D9468F"]   # as três pessoas (cores neutras, sem função)


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


# ======================================================================
# peças (mesmo traço dos episódios 1–3)
# ======================================================================

def pacote(c, x, y, w, h, col, a, label=None, lsize=24):
    """um pacotinho de dinheiro (ep1); (x, y) = canto superior esquerdo"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 12, col, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 6, y + 6, w - 12, h - 12), 8, 8),
                paint("#FFFFFF", a * 0.45, stroke=2))
    if label:
        text_mid(c, label, x + w / 2, y + h / 2, lsize, "black", "#FFFFFF", a)


def flip(c, n, cx, cy, size, u, a, col_n=None, col_f=None):
    """o número n gira de cabeça para baixo (u = 0..1) e reaparece como a fração 1/n (ep2)"""
    if a <= 0:
        return
    u = clamp(u)
    sy = math.cos(math.pi * u)
    c.save(); c.translate(cx, cy); c.scale(1, max(abs(sy), 0.02)); c.translate(-cx, -cy)
    if u < 0.5:
        fmid(c, str(n), cx, cy, size, "black", col_n or INK, a)
    else:
        expr(c, f"1/{n}", cx, cy, size * 0.75, a, cores={0: col_f or GREEN})
    c.restore()


def quadros(c, x, y, cols, rows, cell, a, col=None, gap=6):
    """retângulo de quadradinhos cols × rows (ep3); (x, y) = canto superior esquerdo"""
    if a <= 0:
        return
    for r in range(rows):
        for k in range(cols):
            rrect(c, x + k * cell, y + r * cell, cell - gap, cell - gap, 7, col or GREEN, a)


def montinho(c, cx, cy, a, rotulo, col=NOTA, w=120):
    """montinho de notas com etiqueta (ep4): a parte fixa separada"""
    if a <= 0:
        return
    for k in range(3):
        rrect(c, cx - w / 2 + (k % 2) * 8 - 4, cy - k * 14, w, 40, 8, col if k % 2 == 0 else NOTA_ESC, a, shadow=k == 0)
    text_mid(c, rotulo, cx, cy + 46, 22, "black", INK, a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), desenhados em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 os pacotinhos (pesos 2, 3, 4) e o k
        for j, n in enumerate((2, 3, 4)):
            for i in range(n):
                pacote(c, -150 + i * 62, -88 + j * 62, 54, 50, DONOS[j], a, "k", 22)
        text_mid(c, "9 pacotinhos", 0, 112, 26, "black", INK2, a)
    elif k == 1:    # ep2 a fração virando
        for j, n in enumerate((2, 3, 4)):
            flip(c, n, -110 + j * 110, -40, 64, 1.0, a)
            fmid(c, str(n), -110 + j * 110, 52, 40, "black", RED, a * 0.55)
        line(c, -160, 10, 160, 10, "#E6E6E2", a, 3)
        text_mid(c, "vire a FRAÇÃO, não a fila", 0, 112, 24, "black", GREEN, a)
    elif k == 2:    # ep3 o retângulo pessoa-dia
        quadros(c, -150, -80, 5, 2, 50, a, GREEN)
        text(c, "5 pessoas", -25, -94, 22, "black", INK2, a)
        text_mid(c, "× 2 dias = 10", 0, 72, 30, "black", INK, a)
    elif k == 3:    # ep4 o montinho fixo separado antes
        for j in range(3):
            montinho(c, -120 + j * 120, -40, a, "fixo", AMBER)
        text_mid(c, "separe antes, devolva depois", 0, 92, 24, "black", AMBER, a)
    c.restore()


def registradora(c, x, y, a, visor, ok=True, ok_a=0.0, w=300):
    """caixa registradora "fechando o caixa": visor com a soma; selo FECHOU (verde) ou NÃO FECHOU; (x, y) = topo esquerdo"""
    if a <= 0:
        return
    rrect(c, x + 20, y + 40, w - 40, 26, 8, "#2B3240", a)                       # visor (moldura)
    rrect(c, x + 30, y, w - 60, 60, 10, "#1E2530", a, shadow=True)
    sz = 30
    while ftw(visor, sz) > w - 90 and sz > 16:
        sz -= 1
    ftext(c, visor, x + w / 2, y + 41, sz, "black", "#3DE38A", a)
    rrect(c, x, y + 66, w, 92, 16, "#3C4656", a, shadow=True)                 # corpo
    for i in range(4):
        for j in range(2):
            rrect(c, x + 26 + i * 44, y + 82 + j * 34, 34, 24, 6, "#E6E6E2", a)
    rrect(c, x + w - 84, y + 86, 58, 52, 8, GREEN if ok else RED, a)
    rrect(c, x - 10, y + 158, w + 20, 34, 10, "#2B3240", a)                     # gaveta
    if ok_a > 0:
        selo(c, x + w + 40, y + 70, ok_a, "FECHOU!" if ok else "NÃO FECHOU", GREEN if ok else RED, -6, 28)


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 200, 640, 230, 24, mix("#FFFFFF", PURPLE, 0.10), aa, shadow=True)
        text(c, "PROCEDIMENTO", 580, 280, 48, "black", PURPLE, aa)
        text(c, "um caminho único, todos os casos", 580, 350, 28, "bold", INK2, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 1020, 200, 640, 230, 24, mix("#FFFFFF", AMBER, 0.12), ab, shadow=True)
        text(c, "A DIFICULDADE", 1340, 262, 30, "black", AMBER, ab)
        text(c, "quais são os pesos?", 1340, 345, 50, "black", INK, ab)
        text(c, "(não a conta)", 1340, 400, 26, "bold", INK2, ab)
    for k in range(4):
        icone(c, k, 420 + k * 360, 590, 0.62, ep(t, C["01.b"] + 1.2 + 0.25 * k, 0.4))
    ac = ep(t, C["01.c"], 0.5)
    chip(c, "TREINO", 640, 790, PURPLE, ac, 36)
    chip(c, "9 FRASES", 960, 790, AMBER, ep(t, C["01.c"] + 0.5, 0.4), 36)
    chip(c, "5 QUESTÕES", 1280, 790, GREEN, ep(t, C["01.c"] + 1.0, 0.4), 36)


CONTEXTOS = [("02.a", "SOCIEDADE", "lucro entre sócios"), ("02.b", "RATEIO", "luz, condomínio, viagem"),
             ("02.c", "VERBAS", "setores, escolas"), ("02.d", "HERANÇA", "entre herdeiros"),
             ("02.e", "PREMIAÇÃO", "por desempenho")]


def b_contextos(c, t, C, B):
    frame(c, t, B["start"], "ONDE APARECE NA PROVA", "SEMPRE OS MESMOS CONTEXTOS", BLUE)
    for k, (cue, tit, sub) in enumerate(CONTEXTOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 330
        rrect(c, x - 150, 260 + d, 300, 420, 24, "#F7F7F5", a)
        badge_num(c, k + 1, x, 312 + d, a, 24, bg=BLUE)
        for j in range(3):
            pacote(c, x - 90 + j * 62, 400 + d, 54, 50, DONOS[j], a)
        text(c, tit, x, 540 + d, 32, "black", BLUE, a)
        para(c, sub, x, 590 + d, 24, "bold", INK2, a, 260, 30, align="center")
    at = ep(t, C["02.e"] + 1.2, 0.5)
    pill(c, "em todos: um total repartido conforme o PESO de cada um", W / 2, 760, PURPLE, size=28, a=at, anchor="center")


INDICE = [("EP. 1", "some, divida, multiplique: o k é UM pacotinho"), ("EP. 2", "vire a fração, não a fila (MMC)"),
          ("EP. 3", "dois critérios: MULTIPLIQUE (pessoa-dia)"), ("EP. 4", "parte fixa = bandeirada · feche o caixa")]
IND_CUES = ["03.a", "03.b", "04.a", "04.b"]
IND_POS = [(690, 195), (1230, 195), (690, 515), (1230, 515)]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x, y = IND_POS[k]
        rrect(c, x - 255, y, 510, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 255, y, 510, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x, y + 34, PURPLE if on_ else INK2, size=22, a=a, anchor="center", bounds=(0, 1920))
        icone(c, k, x, y + 140, 0.62, a)
        para(c, s, x, y + 262, 24, "black", INK if on_ else INK2, a, 470, 30, align="center")


def b_rendem(c, t, C, B):
    frame(c, t, B["start"], "SE TIVER TEMPO PARA DUAS", "AS QUE MAIS RENDEM", GREEN)
    aa, ab = ep(t, C["05.a"], 0.5), ep(t, C["05.b"], 0.5)
    for k, (a, tit, sub) in enumerate(((aa, "1 · O ATALHO DO MMC", "na divisão inversa"),
                                       (ab, "2 · MULTIPLICAR", "na divisão composta"))):
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 200, 680, 560, 24, "#F7F7F5", a)
        text(c, tit, x, 262, 36, "black", GREEN, a)
        text(c, sub, x, 312, 26, "bold", INK2, a)
        if k == 0:
            for j, n in enumerate((2, 3, 4)):
                flip(c, n, x - 200 + j * 200, 420, 70, ep(t, C["05.a"] + 0.6 + 0.3 * j, 0.6), a)
            fmid(c, "× 12", x, 520, 40, "black", PURPLE, ep(t, C["05.a"] + 1.8, 0.4))
            for j, n in enumerate((6, 4, 3)):
                fmid(c, str(n), x - 200 + j * 200, 620, 70, "black", GREEN, ep(t, C["05.a"] + 2.2, 0.4))
            pill(c, "pesos inteiros", x, 710, GREEN, size=24, a=ep(t, C["05.a"] + 2.2, 0.4), anchor="center",
                 bounds=(0, 1920))
        else:
            quadros(c, x - 240, 380, 5, 2, 70, a, GREEN)
            text(c, "5 × 2 = 10", x - 65, 590, 44, "black", GREEN, a)
            ar = ep(t, C["05.b"] + 1.4, 0.4)
            text(c, "5 + 2 = 7", x + 200, 470, 40, "black", RED, ar)
            strike(c, x + 110, 458, x + 290, 458, ar, RED, ar)
            pill(c, "o instinto manda somar", x + 200, 540, AMBER, size=22, a=ar, anchor="center", bounds=(0, 1920))


# treino: (cue da pergunta, cue da resposta, tipo, enunciado curto (linhas), pesos, cor)
TREINO = [("06.b", "07.a", "DIRETA", ["prêmio pelos pontos", "20, 30 e 50"], "2 : 3 : 5", BLUE, "÷ 10"),
          ("06.c", "07.b", "INVERSA", ["bônus, inversamente", "às faltas 1, 2 e 4"], "4 : 2 : 1", PURPLE, "inversos × 4"),
          ("06.d", "07.c", "COMPOSTA", ["2 e 3 pessoas", "5 e 4 dias"], "10 : 12 = 5 : 6", GREEN, "multiplique"),
          ("06.e", "07.d", "PARTE FIXA", ["R$ 1 000 para cada", "resto em 1 e 2"], "1 : 2 no resto", AMBER, "separe o fixo antes")]


def b_treino(c, t, C, B):
    head_seq(c, t, C, [("06", "TREINO-RELÂMPAGO", "QUAIS SÃO OS PESOS?", PURPLE),
                       ("07", "CONFERINDO", "SÓ OS PESOS", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["06"], 0.5)
    pill(c, "só os pesos, sem terminar a conta", W / 2, 205, PURPLE, size=24, a=aa, anchor="center", bounds=(0, 1920))
    for k, (cq, cr, tipo, linhas, pesos, col, dica) in enumerate(TREINO):
        a, d = rise(t, C[cq])
        if a <= 0:
            continue
        x, y = 360 + k * 400, 260 + d
        ar = ep(t, C[cr], 0.4) if t >= C["07"] else 0
        on_ = ar > 0 and (k == 3 or t < C[TREINO[k + 1][1]])
        rrect(c, x - 180, y, 360, 440, 20, mix("#F7F7F5", col, 0.10 * ar), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 180, y, 360, 440), 20, 20), paint(col, a, stroke=4))
        badge_num(c, k + 1, x, y + 44, a, 24, bg=col if ar > 0 else INK2)
        pill(c, tipo, x, y + 104, col, size=20, a=a, anchor="center", bounds=(0, 1920))
        for j, s in enumerate(linhas):
            ftext(c, s, x, y + 176 + j * 42, 28, "bold", INK, a)
        if ar <= 0:
            fmid(c, "?", x, y + 330, 64, "black", AMBER, a)
        else:
            sz = 40
            while ftw(pesos, sz) > 320:
                sz -= 2
            fmid(c, pesos, x, y + 320, sz, "black", col, ar)
            ftext(c, dica, x, y + 392, 22, "black", INK2, ar)
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


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone)
VF = [
    ("dividir INVERSAMENTE a 2, 3 e 4", "pesos 2, 3 e 4", False, "são os números do enunciado",
     "aí o maior número levaria mais: use os INVERSOS", "pesos 6, 4 e 3", 1),
    ("dividir INVERSAMENTE a 2, 3 e 4", "pesos 4, 3 e 2", False, "o menor passa a levar mais",
     "virar a FILA não é virar a FRAÇÃO: 1/2, 1/3, 1/4 × 12", "pesos 6, 4 e 3", 1),
    ("divisão composta", "5 pessoas por 2 dias: peso 10, não 7", True, "somar parece mais natural",
     "é um retângulo: 5 por 2 dá 10 quadradinhos de trabalho", "5 × 2 = 10", 2),
    ("R$ 3 600 em 2 : 3 : 4", "cada um: 3 600 ÷ 3", False, "são três pessoas",
     "são 9 pacotinhos: divida pela SOMA dos pesos", "k = 3 600 ÷ 9 = 400", 0),
    ("R$ 1 000 fixos para cada", "a proporção vale sobre o total", False, "o total é o número que aparece",
     "a proporção vale só sobre o RESTO", "separe antes, devolva depois", 3),
    ("um k que não dá exato", "mantenha como fração até o fim", True, "arredondar parece mais prático",
     "arredondar faz a soma das partes não fechar", "k exato até o fim", 0),
    ("partes calculadas certinho", "não tem como errar a questão", False, "a conta está perfeita",
     "pode pedir a menor, a do 2º sócio, a diferença", "RELEIA o pedido", 3),
    ("divisão composta", "simplificar só as pessoas e usar como peso", False, "simplificar sempre ajuda",
     "assim os dias ficam pelo caminho", "multiplique, depois simplifique", 2),
    ("a soma das partes", "conferir pega erro de k, de peso ou de método", True, "parece só uma conferência",
     "se o caixa não fecha, algo deu errado: refaça", "feche o caixa", 3),
]
VF_IDS = [f"{9 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 410, 0.7, a0)
    text(c, ctx, 960, 310, 32, "bold", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = 56
    while ftw(conta, sz) > 760:
        sz -= 2
    fmid(c, conta, 960, 410, sz, "black", INK, a0)
    if ar > 0 and not ver:
        w = ftw(conta, sz)
        strike(c, 960 - w / 2 - 10, 415, 960 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 410, a=1 - ar)
    selo(c, 1580, 410, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
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
        szf = 44
        while ftw(fix, szf) > 600:
            szf -= 2
        fmid(c, fix, 1340, 715, szf, "black", GREEN, ag)


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
# enun: (cue, texto, destaque?) · passos: (cue, texto) · selo1: (rótulo, linha, cor, cue) · caixa: (visor, linha de ordem)

Q = {
    "q1": dict(ids=("19", "20"), titulo="AS TURMAS", ok="B",
               enun=[("a", "Uma escola vai dividir R$ 18 000,00 entre três turmas, em partes diretamente proporcionais ao "
                           "número de alunos: 24, 30 e 36.", False),
                     ("b", "A diferença entre a maior e a menor parte é de", True)],
               alts=[("A", "R$ 1 200,00", "parou no k", RED), ("B", "R$ 2 400,00", "", GREEN),
                     ("C", "R$ 4 800,00", "é a menor parte", AMBER), ("D", "R$ 6 000,00", "dividiu por 3 turmas", RED),
                     ("E", "R$ 7 200,00", "é a maior parte", AMBER)],
               selo1=("RELEIA O PEDIDO", "a DIFERENÇA, não uma parte", AMBER, "d"),
               passos=[("a", "24 : 30 : 36 = 4 : 5 : 6  (soma 15)"), ("b", "k = 18 000 ÷ 15 = 1 200"),
                       ("c", "(6 − 4) × 1 200 = 2 400")],
               caixa=("4 800 + 6 000 + 7 200 = 18 000", None)),
    "q2": dict(ids=("21", "22"), titulo="O BÔNUS", ok="D",
               enun=[("a", "Um bônus de R$ 4 000,00 será dividido entre três atendentes, em partes inversamente "
                           "proporcionais ao número de reclamações do mês: 3, 4 e 12.", False),
                     ("b", "A atendente com 3 reclamações receberá", True)],
               alts=[("A", "R$ 500,00", "deu a quem reclamou mais", RED), ("B", "R$ 631,58", "usou 3, 4, 12", AMBER),
                     ("C", "R$ 1 333,33", "dividiu igual", RED), ("D", "R$ 2 000,00", "", GREEN),
                     ("E", "R$ 2 526,32", "virou a fila", AMBER)],
               selo1=("VIRE A FRAÇÃO", "menos reclamação, mais bônus: inversa", PURPLE, "d"),
               passos=[("a", "1/3, 1/4, 1/12 × 12 → 4 : 3 : 1"), ("b", "k = 4 000 ÷ 8 = 500"), ("c", "4 × 500 = 2 000")],
               caixa=("2 000 + 1 500 + 500 = 4 000", "menos reclamação levou mais ✓")),
    "q3": dict(ids=("23", "24"), titulo="AS EQUIPES", ok="A",
               enun=[("a", "Um prêmio de R$ 9 000,00 será dividido entre três equipes, diretamente proporcional ao "
                           "número de integrantes (2, 3 e 4)", False),
                     ("b", "e inversamente proporcional ao número de faltas da equipe (1, 2 e 4).", False),
                     ("c", "A equipe de 4 integrantes receberá", True)],
               alts=[("A", "R$ 2 000,00", "", GREEN), ("B", "R$ 3 000,00", "dividiu igual", RED),
                     ("C", "R$ 4 000,00", "só os integrantes", RED), ("D", "R$ 4 500,00", "SOMOU as séries", AMBER),
                     ("E", "R$ 6 000,00", "não inverteu as faltas", AMBER)],
               selo1=("INVERTA ANTES", "faltas → inversos, DEPOIS multiplique", PURPLE, "d"),
               passos=[("a", "faltas 1, 2, 4 → inversos × 4 = 4, 2, 1"), ("b", "2·4 = 8 · 3·2 = 6 · 4·1 = 4  → 4 : 3 : 2"),
                       ("c", "k = 1 000 → equipe de 4: 2 000")],
               caixa=("4 000 + 3 000 + 2 000 = 9 000", "a maior equipe faltou mais ✓")),
    "q4": dict(ids=("25", "26"), titulo="OS SÓCIOS", ok="B",
               enun=[("a", "Três sócios dividem um lucro de R$ 30 000,00.", False),
                     ("b", "A investiu R$ 12 000,00 por 10 meses; B, R$ 15 000,00 por 10 meses; e C, R$ 18 000,00 por "
                           "5 meses.", False),
                     ("c", "Dividindo pelo capital e pelo tempo, o sócio C recebe", True)],
               alts=[("A", "R$ 6 000,00", "só o tempo", RED), ("B", "R$ 7 500,00", "", GREEN),
                     ("C", "R$ 10 000,00", "dividiu igual", RED), ("D", "R$ 12 000,00", "só o capital", AMBER),
                     ("E", "R$ 12 500,00", "é a parte do B", AMBER)],
               selo1=("CAPITAL × TEMPO", "quem manda é o PRODUTO", PURPLE, "d"),
               passos=[("a", "12·10 = 120 · 15·10 = 150 · 18·5 = 90"), ("b", "÷ 30 → 4 : 5 : 3 · k = 2 500"),
                       ("c", "C: 3 × 2 500 = 7 500")],
               caixa=("10 000 + 12 500 + 7 500 = 30 000", "o maior capital levou a MENOR parte")),
    "q5": dict(ids=("27", "28"), titulo="OS FINALISTAS", ok="C",
               enun=[("a", "Um prêmio de R$ 12 000,00 vai para três finalistas.", False),
                     ("b", "Cada um recebe R$ 2 000,00 fixos, e o restante é dividido em partes proporcionais às notas "
                           "1, 3 e 4.", False),
                     ("c", "O finalista de nota 4 recebe, no total,", True)],
               alts=[("A", "R$ 2 750,00", "é a parte do nota 1", AMBER), ("B", "R$ 3 000,00", "não devolveu o fixo", AMBER),
                     ("C", "R$ 5 000,00", "", GREEN), ("D", "R$ 6 000,00", "proporção sobre o total", RED),
                     ("E", "R$ 8 000,00", "sobre o total + fixo", RED)],
               selo1=("A BANDEIRADA", "separe o fixo antes, devolva depois", AMBER, "d"),
               passos=[("a", "12 000 − 3 × 2 000 = 6 000"), ("b", "k = 6 000 ÷ 8 = 750 → 4 × 750 = 3 000"),
                       ("c", "2 000 + 3 000 = 5 000")],
               caixa=("2 750 + 4 250 + 5 000 = 12 000", None)),
}


def selo_linha(c, x, y, w, rotulo, s, col, a):
    """caixa com rótulo (RELEIA O PEDIDO, VIRE A FRAÇÃO...) e uma linha curta"""
    if a <= 0:
        return
    boxed(c, x, y, w, 84, col, a, 0.08)
    pill(c, rotulo, x + 20, y, col, size=18, a=a, bounds=(0, 1920))
    sz = 26
    while ftw(s, sz) > w - 40:
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
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 270
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para(c, s, 180, y + 22, 29, "black" if dest else "bold", BLUE if dest else INK, a, 640, 38)
            y += h + 16
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 34, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            rot, s_, col, cue = d["selo1"]
            selo_linha(c, 170, 250, 650, rot, s_, col, ep(t, C[f"{s2}.{cue}"], 0.4) * sol)
            yy = 400
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4)
                last = j == len(d["passos"]) - 1
                sz = 34
                while ftw(s, sz) > 640:
                    sz -= 2
                ftext(c, s, 180, yy, sz, "black", GREEN if last else INK, a, align="left")
                yy += 58
            visor, ordem = d["caixa"]
            av = ep(t, C[f"{s2}.v"], 0.4) if f"{s2}.v" in C else ep(t, C[f"{s2}.ok"] + 0.6, 0.4)
            av *= sol
            soma, total = visor.split(" = ")
            registradora(c, 180, 590, av, total, True, 0.0, w=250)
            ftext(c, soma, 460, 640, 30, "black", INK, av, align="left")
            ftext(c, "= " + total, 460, 690, 34, "black", GREEN, av, align="left")
            selo(c, 740, 680, av, "FECHOU!", GREEN, -6, 26)
            if ordem:
                ftext(c, ordem, 460, 745, 24, "black", GREEN, av, align="left")
            result_box(c, f"Letra {d['ok']}", 1290, 640, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("29.b", "EP. 1", ["k = total ÷ soma dos pesos", "por que dividir pela soma funciona", "simplificar pelo MDC",
                            "total por uma parte · diferença"]),
         ("29.c", "EP. 2", ["inversa: inversos × MMC", "inverter o valor, não a ordem"]),
         ("30.a", "EP. 3", ["composta: multiplicar as séries", "sociedade: capital e capital × tempo"]),
         ("30.b", "EP. 4", ["separar a parte fixa", "conferir: soma, ordem e o pedido"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["29.a"], 0.5) * (1 - ep(t, C["29.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 2 else 1
        x = 190 if col_ == 0 else 1000
        y0 = 200 + sum(len(CHECK[j][2]) * 52 + 34 for j in range(0 if col_ == 0 else 2, k))
        pill(c, ep_, x, y0 + 20, PURPLE, size=20, a=a, bounds=(0, 1920))
        for j, it in enumerate(itens):
            yy = y0 + 20 + j * 52
            rrect(c, x + 110, yy - 16, 32, 32, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            ftext(c, it, x + 160, yy + 11, 28, "bold", INK, a, align="left")
    ae = ep(t, C["30.c"], 0.5)
    if ae > 0:
        boxed(c, 1000, 640, 700, 110, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1350, 695, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["31.a"], 0.5)
    ab = ep(t, C["31.b"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["31.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 250 + k * 82, 250 + r_ * 92
        rrect(c, x, y, 66, 72, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 320, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 420, 46, "black", GREEN, ab)
    ac = ep(t, C["31.c"], 0.5)
    if ac > 0:
        boxed(c, 250, 600, 1420, 160, AMBER, ac, 0.10)
        icone(c, 1, 420, 690, 0.42, ac)
        icone(c, 2, 1500, 690, 0.42, ac)
        text_mid(c, "priorize: INVERSA e COMPOSTA", W / 2, 680, 38, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Porcentagem", W / 2, 330, 62, "black", PURPLE, aa)
    fmid(c, "%", W / 2, 480, 120, "black", PURPLE, ep(t, C["32.a"] + 0.6, 0.5))
    ab = ep(t, C["32.b"], 0.5)
    for k, (s, col) in enumerate((("AUMENTOS", GREEN), ("DESCONTOS", RED), ("JUROS", BLUE))):
        chip(c, s, 600 + k * 360, 660, col, ab * ep(t, C["32.b"] + 0.8 + 0.4 * k, 0.4), 40)
    text(c, "razão e proporção viram a ferramenta", W / 2, 780, 30, "bold", INK2, ab)


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Qual questão te pegou?",
        canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, contextos=b_contextos, indice=b_indice, rendem=b_rendem, treino=b_treino, vf_intro=b_vf_intro,
              vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"), q3=faz_questao("q3"),
              q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
