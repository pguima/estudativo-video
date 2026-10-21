"""Visual — Redação ENEM, Leitura da Proposta, Episódio 6: Revisão geral, pegadinhas e desafio prático (tema claro).
Reaproveita o ep5 (V5: checklist, rascunho, caligrafia) e, por ele, os eps 4, 3, 2 e 1 (placar, peças, alternativas).
Novo: ÍNDICE com os 5 ícones dos episódios (etiqueta · quebra-cabeça · GPS · mapa com pino · checklist), V ou F com
selo PEGADINHA, CRONÔMETRO de 5 minutos no desafio e checklist de domínio agrupado por episódio.
Cores: azul = definição/tema · verde = método · âmbar = armadilha · vermelho = erro/penalidade · roxo = regra oficial.
"""
import importlib.util
import json
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "ep5_oficina_seis_passos" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v_ep5", _p)
V5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V5)
V4, V2, V1 = V5.V4, V5.V2, V5.V1
motor.set_theme("claro")
try:
    V1._SC = {s["id"]: s for s in json.load(open(Path(__file__).resolve().parent.parent / "audio" / "tempos.json",
                                                 encoding="utf-8"))["scenes"]}
except Exception:
    V1._SC = {}

paper, hand, hand_para, hwrap = V1.paper, V1.hand, V1.hand_para, V1.hwrap
boxed, selo, pause_timer, which, para, wrap = V1.boxed, V1.selo, V1.pause_timer, V1.which, V1.para, V1.wrap
frame, head_seq, phrase_span, wreveal = V1.frame, V1.head_seq, V1.phrase_span, V1.wreveal
alts_panel, puzzle, centros = V2.alts_panel, V2.puzzle, V4.centros
PEN = V1.PEN

MARCA = ""
ARQUIVO_FINAL = "enem_redacao_leitura_proposta_ep6_revisao_desafio.mp4"
CARD_R = (140, 150, 1640, 690)
DIDATICO = "Tema elaborado para fins didáticos."


# ======================================================================
# os 5 ícones dos episódios (índice visual)
# ======================================================================

def ic_etiqueta(c, cx, cy, s, a, col):
    rrect(c, cx - 30 * s, cy - 20 * s, 60 * s, 40 * s, 6 * s, "#FFFFFF", a, stroke=3 * s, stroke_color=col)
    for k in range(6):
        c.drawRect(skia.Rect.MakeXYWH(cx + (4 + k * 4) * s, cy - 12 * s, 2 * s, 14 * s), paint(col, a))
    line(c, cx - 22 * s, cy - 6 * s, cx - 2 * s, cy - 6 * s, col, a, 3 * s)
    line(c, cx - 22 * s, cy + 6 * s, cx + 20 * s, cy + 6 * s, col, a, 3 * s)


def ic_puzzle(c, cx, cy, s, a, col):
    rrect(c, cx - 26 * s, cy - 20 * s, 44 * s, 40 * s, 6 * s, col, a)
    c.drawCircle(cx + 18 * s, cy, 9 * s, paint(col, a))
    c.drawCircle(cx - 4 * s, cy - 20 * s, 8 * s, paint(col, a))


def ic_gps(c, cx, cy, s, a, col):
    rrect(c, cx - 18 * s, cy - 30 * s, 36 * s, 60 * s, 8 * s, INK, a)
    rrect(c, cx - 13 * s, cy - 24 * s, 26 * s, 46 * s, 4 * s, "#EAF1E6", a)
    pth = skia.Path(); pth.moveTo(cx - 8 * s, cy + 16 * s); pth.lineTo(cx, cy); pth.lineTo(cx + 6 * s, cy - 12 * s)
    c.drawPath(pth, paint(col, a, stroke=3 * s, cap_round=True))
    c.drawCircle(cx + 6 * s, cy - 14 * s, 4 * s, paint(RED, a))


def ic_pino(c, cx, cy, s, a, col):
    p = skia.Path(); p.moveTo(cx, cy + 26 * s); p.lineTo(cx - 16 * s, cy - 2 * s); p.lineTo(cx + 16 * s, cy - 2 * s); p.close()
    c.drawPath(p, paint(col, a))
    c.drawCircle(cx, cy - 10 * s, 18 * s, paint(col, a))
    c.drawCircle(cx, cy - 10 * s, 7 * s, paint("#FFFFFF", a))


def ic_check(c, cx, cy, s, a, col):
    rrect(c, cx - 24 * s, cy - 28 * s, 48 * s, 58 * s, 6 * s, "#C8955C", a)
    rrect(c, cx - 18 * s, cy - 20 * s, 36 * s, 44 * s, 4 * s, "#FFFFFF", a)
    for k in range(3):
        yy = cy - 10 * s + k * 13 * s
        check_icon(c, cx - 9 * s, yy, 4.5 * s, a, col)
        line(c, cx - 2 * s, yy, cx + 12 * s, yy, LIGHT, a, 2.5 * s)


ICONES = [(ic_etiqueta, "endereço", BLUE), (ic_puzzle, "blocos", GREEN), (ic_gps, "GPS", GREEN), (ic_pino, "entregas", AMBER),
          (ic_check, "checklist", PURPLE)]


def icone(c, k, cx, cy, a, s=1.0, lit=True, label=True):
    if a <= 0:
        return
    fn, nm, col = ICONES[k]
    col_ = col if lit else LIGHT
    c.drawCircle(cx, cy, 46 * s, paint(mix("#FFFFFF", col_, 0.14), a))
    fn(c, cx, cy, s, a, col_)
    if label:
        text(c, f"EP. {k + 1}", cx, cy + 74 * s, 18 * s, "black", col_ if lit else GRAY, a, tracking=2)


def indice(c, a, lit=None, y=120, x0=None, gap=110, s=0.6):
    """faixa com os 5 ícones; lit = índice aceso (os outros ficam cinza)"""
    x0 = x0 if x0 is not None else W - 5 * gap + gap / 2 - 60
    for k in range(5):
        icone(c, k, x0 + k * gap, y, a, s, lit is None or lit == k, label=False)


def cronometro(c, cx, cy, r, a, frac=1.0, label="5:00"):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r + 12, paint(AMBER, a * 0.16))
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 360 * clamp(frac), False,
              paint(AMBER, a, stroke=r * 0.18, cap_round=True))
    rrect(c, cx - 14, cy - r - 30, 28, 22, 6, INK2, a)
    text_mid(c, label, cx, cy, r * 0.5, "black", INK, a)


# ======================================================================
# abertura, hábitos, mapa da série
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM · REVISÃO", "VOCÊ ESTÁ PRONTO?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    cronometro(c, 450, 420, 140, aa, 1 - 0.25 * prog(t, C["01.a"], 2.5), "min")
    text(c, "poucos minutos de leitura", 450, 650, 34, "black", INK2, aa)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "decide se o texto pode chegar a", 1180, 260, 28, "bold", GRAY, ab)
    V4.placar(c, 920, 340, 420, ab, cap=ep(t, C["01.c"], 1.2), total=True, teto=True)
    for k in range(5):
        icone(c, k, 1200 - 220 + k * 110 + 110, 800, ep(t, C["01.d"] + 0.15 * k, 0.4), 0.55, label=False)


HAB = [("03.a", 1, "decomponha a frase temática em BLOCOS", "anote o que cada um obriga a discutir"),
       ("03.b", 2, "motivadores: para ENTENDER, não para preencher", "linhas copiadas não contam · a cópia baixa a nota"),
       ("03.c", 3, "teste a tese contra a frase temática ANTES de escrever", "bloco de fora = risco de tangenciar")]


def b_habitos(c, t, C, B):
    head_seq(c, t, C, [("02", "TESTE DE MEMÓRIA", "QUAIS SÃO OS 3 HÁBITOS?", PURPLE), ("03", "O QUE RENDE MAIS", "OS 3 HÁBITOS", GREEN)])
    card(c, *CARD_R)
    if t < C["03"] - 0.05:
        a = ep(t, C["02.a"], 0.5)
        for k in range(3):
            badge_num(c, k + 1, 500 + k * 460, 420, a, 70, bg=LIGHT)
            text_mid(c, "?", 500 + k * 460, 560, 80, "black", GRAY, a)
        pause_timer(c, t, C["02.p"] + 0.4, W / 2, 720)
        return
    for k, (cue, ic, s1, s2) in enumerate(HAB):
        a, d = rise(t, C[cue])
        y = 290 + k * 190 + d
        icone(c, ic, 300, y, a, 1.0, label=True)
        text(c, s1, 400, y, 40, "black", INK, a, align="left")
        text(c, s2, 400, y + 52, 28, "bold", GREEN, a, align="left")


MAPA = [("04.a", 0, "frase temática", "endereço completo"), ("04.a", 1, "blocos", "partes do endereço"),
        ("04.b", 1, "foco", "escolher a porta"), ("04.c", 2, "motivadores", "GPS"),
        ("04.d", 2, "cópia", "linha fantasma"), ("04.e", 3, "tangenciar", "bairro certo, casa errada"),
        ("04.e", 3, "fuga", "outra cidade"), ("04.f", 4, "6 passos", "checklist do piloto")]


def b_mapa(c, t, C, B):
    frame(c, t, B["start"], "AS IMAGENS DA SÉRIE", "O MAPA DA REVISÃO", PURPLE)
    for k, (cue, ic, s1, s2) in enumerate(MAPA):
        a, d = rise(t, C[cue] + (0.6 if k in (1, 6) else 0))
        x = 210 + (k % 4) * 380
        y = 210 + (k // 4) * 300 + d
        rrect(c, x, y, 350, 270, 20, "#FFFFFF", a, shadow=True)
        icone(c, ic, x + 175, y + 80, a, 0.8, label=False)
        text(c, s1, x + 175, y + 175, 28, "black", INK, a)
        text(c, s2, x + 175, y + 225, 26, "black", ICONES[ic][2], a)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

VF = [("05", "Dá para descobrir o tema lendo só os textos motivadores.", False, "os motivadores falam do mesmo problema",
       "a frase temática é a referência: o recorte está nela", 2),
      ("06", "Um texto só sobre o assunto amplo tangencia: C2, C3 e C5 limitadas a 40.", True, "o texto fala do assunto...",
       "cada bloco da frase temática precisa ser discutido", 3),
      ("07", "“No Brasil” é só um enfeite da frase temática.", False, "aparece quase sempre, no fim",
       "é exigência: tratar só de outro país foi tangenciamento oficial em 2025", 3),
      ("08", "Escolher só duas causas para discutir é um foco legítimo.", True, "parece corte: muita coisa ficou de fora",
       "selecionar causas é legítimo; retirar um delimitador, não", 1),
      ("09", "Dizer que “é um tema importante” já é ter uma tese.", False, "a frase usa as palavras da prova",
       "“é um tema importante” não é ponto de vista: tome posição", 4),
      ("10", "Uma linha com um pedaço copiado deixa de contar inteira.", True, "parece injusto: o resto da linha é seu",
       "linhas copiadas, mesmo em parte, não contam", 2),
      ("11", "Uma redação só com as ideias da coletânea chega ao topo da C3.", False, "são fontes oficiais da prova",
       "argumentos limitados aos motivadores ficam nos níveis médios da C3", 2),
      ("12", "Gráficos e imagens também mostram o problema.", True, "muita gente acha que só o texto escrito conta",
       "interprete-os em vez de transcrevê-los", 2),
      ("13", "Tangenciar zera a redação.", False, "os dois são erros de tema",
       "zera a fuga; tangenciar limita 3 competências (C1 e C4 seguem normais)", 3),
      ("14", "O melhor momento de conferir o tema é no fim, na folha definitiva.", False, "parece revisão caprichada",
       "confira na tese: no rascunho custa minutos; na definitiva, a nota", 4)]


def b_vf(c, t, C, B):
    ids = [v[0] for v in VF]
    sid = which(t, C, ids)
    n = ids.index(sid)
    _, frase, ok, engana, regra, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 10", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    for k in range(10):
        done = k < n
        badge_num(c, k + 1, 560 + k * 80, 205, 1, 20, bg=AMBER if k == n else (INK2 if done else LIGHT))
    q = lambda x: C[f"{sid}.{x}"]
    aq, d = rise(t, q("q"))
    icone(c, ic, 290, 360 + d, aq, 0.9, label=False)
    para(c, frase if "“" in frase else "“" + frase + "”", 380, 340 + d, 46, "black", INK, aq, 1180, 56)
    pause_timer(c, t, q("p") + 0.3, 1540, 560)
    ar = ep(t, q("r"), 0.4)
    if ar > 0:
        selo(c, 520, 560, ar, "VERDADEIRO" if ok else "FALSO", GREEN if ok else RED, -6, 56)
    aw = ep(t, q("w"), 0.4)
    if aw > 0:
        selo(c, 950, 560, aw, "PEGADINHA", AMBER, 4, 30)
        para(c, engana, 1100, 548, 26, "bold", INK2, aw, 520, 30)
    ak = ep(t, q("k"), 0.4)
    if ak > 0:
        rrect(c, 260, 690, 1400, 100, 18, mix("#FFFFFF", GREEN, 0.10), ak)
        check_icon(c, 310, 740, 26, ak, GREEN)
        text_mid(c, regra, 990, 740, 32, "black", GREEN, ak)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

def questao(c, t, C, n, sub, lembra, ic, tema, enun, alts, okc, okL, extra=None, size=22):
    head(c, t, C[lembra[0]], f"QUESTÃO {n} · INÉDITA", sub, BLUE)
    card(c, *CARD_R)
    cue_r, s_r = lembra[1], lembra[2]
    ar = ep(t, C[cue_r], 0.4)
    icone(c, ic, 230, 250, ar, 0.7, label=False)
    pill(c, "LEMBRANDO", 300, 222, PURPLE, size=18, a=ar, bounds=(0, 1920))
    para(c, s_r, 300, 275, 22, "black", PURPLE, ar, 420, 26)
    aa = ep(t, C[enun[0]], 0.4)
    text(c, "TEMA", 190, 380, 16, "black", GRAY, aa, align="left", tracking=2)
    h = para(c, "“" + tema + "”", 190, 420, 26, "black", BLUE, aa, 540, 32)
    text(c, DIDATICO, 190, 420 + h + 4, 15, "medium", AMBER, aa, align="left")
    if enun[1]:
        para(c, enun[1], 190, 420 + h + 50, 22, "bold", INK, aa, 540, 28)
    if extra:
        extra(c, t, C)
    alts_panel(c, t, C, alts, 790, 222, 950, size, okc, okL, 6)


ALT1 = [("A", "assunto: a frase inteira; tema: inclusão digital.", "15.A", "16.xa", "inverte assunto e tema", RED),
        ("B", "assunto: inclusão digital; tema: a frase temática inteira.", "15.B", None, "", GREEN),
        ("C", "assunto: inclusão digital; tema: os idosos precisam de apoio do Estado para usar a internet.", "15.C", "16.xc", "isso é TESE, não tema", RED),
        ("D", "assunto: idosos; tema: inclusão digital.", "15.D", "16.xd", "fica no núcleo, perde blocos", RED),
        ("E", "assunto e tema são a mesma coisa.", "15.E", "16.xe", "tema = recorte do assunto", RED)]


def b_q1(c, t, C, B):
    questao(c, t, C, 1, "ASSUNTO × TEMA", ("15", "15.r", "assunto = a cidade · tema = o endereço completo"), 0,
            "Desafios para a inclusão digital de idosos no Brasil", ("15.a", "Assinale o assunto amplo e o tema."), ALT1, "16.ok", "B")
    pause_timer(c, t, C["15.end"] - 1.9, 460, 760)


ALT2 = [("A", "O desperdício de alimentos é um problema que afeta o mundo inteiro.", "17.A", "19.xa", "assunto amplo: sem Brasil, sem caminhos", RED),
        ("B", "O desperdício de alimentos no Brasil é um tema muito importante, que deve ser discutido.", "17.B", "19.xb", "repete o tema", RED),
        ("C", "No Brasil, o desperdício de alimentos persiste pela falta de informação sobre o reaproveitamento e pela falta de incentivo à doação, e combatê-lo exige educação alimentar e regras que facilitem doar.", "18.C", None, "", GREEN),
        ("D", "No Brasil, muitos alimentos são jogados fora todos os dias.", "18.D", "19.xd", "fato: sem posição, sem caminhos", RED),
        ("E", "Este texto vai discutir caminhos para combater o desperdício de alimentos no Brasil.", "18.E", "19.xe", "só anuncia", RED)]


def b_q2(c, t, C, B):
    questao(c, t, C, 2, "A TESE QUE COBRE OS BLOCOS", ("17", "17.r", "tese = posição + dois eixos + todos os blocos"), 4,
            "Caminhos para combater o desperdício de alimentos no Brasil", ("17.a", "Qual tese cobre todos os blocos?"), ALT2, "19.ok", "C")
    pause_timer(c, t, C["18.end"] - 1.9, 460, 760)


ALT3 = [("A", "copiar a frase na introdução, porque ela resume bem o problema.", "20.A", "22.xa", "cópia: linha fantasma", RED),
        ("B", "copiar só metade da frase e completar a linha com palavras suas.", "20.B", "22.xb", "meia linha copiada = linha inteira fora", RED),
        ("C", "retomar a ideia com outra estrutura e acrescentar uma causa própria.", "21.C", None, "", GREEN),
        ("D", "ignorar o texto, porque a frase temática já basta.", "21.D", "22.xd", "abandona o GPS", RED),
        ("E", "construir todos os argumentos só com os textos motivadores.", "21.E", "22.xe", "presa à coletânea: níveis médios", RED)]


def b_q3(c, t, C, B):
    questao(c, t, C, 3, "MOTIVADORES × CÓPIA", ("20", "20.r", "motivador = GPS · linha copiada = linha fantasma"), 2,
            "Desafios para o acesso à leitura no Brasil",
            ("20.a", "Texto motivador: “Bibliotecas públicas de várias cidades reduziram o horário por falta de servidores.” Qual uso está de acordo com a Cartilha?"),
            ALT3, "22.ok", "C")
    pause_timer(c, t, C["21.end"] - 1.9, 460, 790)


ALT4 = [("A", "I foge ao tema; II é completa; III foge.", "24.A", "25.xa", "I está na cidade certa", RED),
        ("B", "I tangencia, com C2, C3 e C5 limitadas a 40; II é completa; III foge e zera.", "24.B", None, "", GREEN),
        ("C", "I tangencia e recebe zero; II é completa; III foge.", "24.C", "25.xc", "tangenciar não zera", RED),
        ("D", "I tangencia, com as cinco competências limitadas a 40; II é completa; III foge.", "24.D", "25.xd", "o teto é só em C2, C3 e C5", RED),
        ("E", "I e III tangenciam; II é completa.", "24.E", "25.xe", "III nem fala de professores", RED)]
RED4 = [("23.i", "I", "só os professores da Finlândia, sem ligar ao Brasil"),
        ("23.ii", "II", "salários e falta de reconhecimento dos professores brasileiros, e como superar"),
        ("23.iii", "III", "uso de redes sociais por adolescentes")]


def _red4(c, t, C):
    y = 600
    for cue, n, s in RED4:
        a = ep(t, C[cue], 0.4)
        badge_num(c, n, 210, y, a, 20, bg=INK2)
        para(c, s, 245, y + 8, 21, "black", INK, a, 500, 25)
        y += 70


def b_q4(c, t, C, B):
    questao(c, t, C, 4, "COMPLETA × TANGENCIA × FUGA", ("23", "23.r", "exato: completa · bairro certo, casa errada: tangencia · outra cidade: fuga"), 3,
            "Desafios para a valorização dos professores da educação básica no Brasil", ("23.a", ""), ALT4, "25.ok", "B", extra=_red4, size=23)
    pause_timer(c, t, C["24.end"] - 1.9, 1560, 790)


ALT5 = [("A", "discutir só a falta de rampas e o transporte público inadequado no Brasil, e como superá-los.", "26.A", None, "", GREEN),
        ("B", "discutir o trânsito das grandes cidades, sem falar de pessoas com deficiência.", "26.B", "28.xb", "corta o GRUPO", RED),
        ("C", "discutir a mobilidade de pessoas com deficiência em outros países.", "27.C", "28.xc", "corta o LUGAR", RED),
        ("D", "tratar de todas as causas possíveis, porque escolher só duas seria tangenciar.", "27.D", "28.xd", "confunde foco com corte", RED),
        ("E", "discutir as dificuldades de pessoas com deficiência no mercado de trabalho brasileiro.", "27.E", "28.xe", "troca o NÚCLEO", RED)]


def b_q5(c, t, C, B):
    questao(c, t, C, 5, "FOCO LEGÍTIMO × CORTE", ("26", "26.r", "foco = escolher a porta, sem trocar de endereço"), 1,
            "Desafios para a mobilidade urbana de pessoas com deficiência no Brasil", ("26.a", "Qual plano faz um foco legítimo?"),
            ALT5, "28.ok", "A", size=23)
    pause_timer(c, t, C["27.end"] - 1.9, 460, 790)


# ======================================================================
# desafio prático
# ======================================================================

TEMAS = [("2016", "Caminhos para combater a intolerância religiosa no Brasil"),
         ("2017", "Desafios para a formação educacional de surdos no Brasil"),
         ("2020", "O estigma associado às doenças mentais na sociedade brasileira"),
         ("2022", "Desafios para a valorização de comunidades e povos tradicionais no Brasil"),
         ("2025", "Perspectivas acerca do envelhecimento na sociedade brasileira")]


def b_desafio(c, t, C, B):
    head(c, t, B["start"], "DESAFIO PRÁTICO", "5 TEMAS REAIS · 5 MINUTOS CADA", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["29.a"], 0.5)
    for k, (ano, tema) in enumerate(TEMAS):
        a = ep(t, C["29.a"] + 0.5 * k, 0.4)
        y = 230 + k * 78
        pill(c, ano, 200, y, BLUE, size=24, a=a, bounds=(0, 1920))
        text(c, tema, 310, y + 10, 26, "black", INK, a, align="left")
    ab = ep(t, C["29.b"], 0.5)
    cronometro(c, 1460, 330, 110, ab, 1 - 0.5 * prog(t, C["29.b"], 6.0), "5:00")
    passos = [("29.c", "blocos"), ("29.d", "pergunta-problema"), ("29.e", "tese provisória + 2 eixos")]
    for k, (cue, s) in enumerate(passos):
        a = ep(t, C[cue], 0.4)
        badge_num(c, k + 1, 230 + k * 400, 690, a, 26, bg=GREEN)
        text(c, s, 270 + k * 400, 700, 30, "black", GREEN, a, align="left")
    pill(c, "depois: tese ao lado da frase temática · faltou bloco? REESCREVA", W / 2, 790, PURPLE, size=24,
         a=ep(t, C["29.f"], 0.4), anchor="center")


T16 = [("Caminhos para combater", V2.DEL, "ORIENTAÇÃO", None, "30.b"), ("a intolerância religiosa", V2.NUC, "NÚCLEO", None, "30.c"),
       ("no Brasil", V2.DEL, "LUGAR", None, "30.d")]
PERG16 = "Por que a intolerância religiosa persiste no Brasil, e como combatê-la?"
TESE16 = ("No Brasil, a intolerância religiosa persiste pelo desconhecimento sobre as diferentes crenças e pela falta de "
          "punição aos ataques, e combatê-la exige educação para o respeito à diversidade e punição efetiva.")


def b_modelo(c, t, C, B):
    sid = which(t, C, ["30", "31", "32"])
    head_seq(c, t, C, [("30", "EU FAÇO O PRIMEIRO · 2016", "OS BLOCOS", GREEN), ("31", "EU FAÇO O PRIMEIRO · 2016", "PERGUNTA E TESE", GREEN),
                       ("32", "EU FAÇO O PRIMEIRO · 2016", "CONFERÊNCIA", GREEN)])
    paper(c, 160, 150, 1600, 700, 1.0, lh=56, top=214)
    cronometro(c, 1660, 290, 56, 1.0, 1 - 0.8 * prog(t, C["30"], 40), "5:00")
    show = [ep(t, C[s[4]], 0.4) for s in T16]
    c.save(); c.translate(-40, 0)
    puzzle(c, t, C, T16, 210, ep(t, C["30.a"], 0.4), 28, show, obriga=False)
    if sid == "32":
        for cx, cue in zip(centros(T16, 28), ("32.a", "32.b", "32.c")):
            check_icon(c, cx, 330, 26, ep(t, C[cue], 0.3), GREEN)
    c.restore()
    if sid == "30":
        ab = ep(t, C["30.b"], 0.4)
        text(c, "caminhos para combater →", 280, 440, 28, "black", GREEN, ab, align="left")
        hand(c, "reconhecer o problema e discutir formas de enfrentá-lo", 690, 440, 32, PEN, ab, wreveal(t, (C["30.b"] + 1.0, C["30.b"] + 4.0)))
        text(c, "a intolerância religiosa →", 280, 520, 28, "black", BLUE, ep(t, C["30.c"], 0.4), align="left")
        hand(c, "o núcleo", 690, 520, 32, PEN, ep(t, C["30.c"], 0.4))
        text(c, "no Brasil →", 280, 600, 28, "black", GREEN, ep(t, C["30.d"], 0.4), align="left")
        hand(c, "o lugar", 690, 600, 32, PEN, ep(t, C["30.d"], 0.4))
        return
    text(c, "PERGUNTA", 280, 420, 18, "black", BLUE, 1.0, align="left", tracking=2)
    hand_para(c, PERG16, 280, 470, 32, PEN, 1.0, 1380, 50, wreveal(t, phrase_span("31", PERG16, C["31.a"], C["31.b"])) if sid == "31" else 1.0)
    text(c, "TESE PROVISÓRIA", 280, 560, 18, "black", GREEN, ep(t, C["31.b"], 0.3), align="left", tracking=2)
    hand_para(c, TESE16, 280, 610, 32, PEN, 1.0, 1380, 50,
              wreveal(t, phrase_span("31", TESE16, C["31.b"], C["31.end"])) if sid == "31" else 1.0)
    text(c, "Pergunta e tese elaboradas para fins didáticos.", 280, 830, 16, "medium", GRAY, 1.0, align="left")
    if sid == "32":
        ad = ep(t, C["32.d"], 0.4)
        text(c, "2 EIXOS:", 900, 830, 22, "black", GREEN, ad, align="left", tracking=2)
        pill(c, "desconhecimento", 1030, 822, GREEN, size=22, a=ad, bounds=(0, 1920))
        pill(c, "falta de punição", 1260, 822, GREEN, size=22, a=ep(t, C["32.d"] + 0.6, 0.3), bounds=(0, 1920))
        ae = ep(t, C["32.e"], 0.5)
        if ae > 0:
            rrect(c, 360, 380, 1200, 360, 24, "#FFFFFF", ae, shadow=True)
            text(c, "AGORA É COM VOCÊ", W / 2, 450, 40, "black", AMBER, ae, tracking=2)
            for k, (ano, _) in enumerate(TEMAS[1:]):
                pill(c, ano, 560 + k * 270, 560, BLUE, size=40, a=ae * ep(t, C["32.e"] + 0.3 * k, 0.3), anchor="center", bounds=(0, 1920))
            cronometro(c, W / 2, 670, 46, ae, 1.0, "5:00")


# ======================================================================
# checklist de domínio
# ======================================================================

DOM = [("34.e1", 0, ["as 3 partes da proposta", "as exigências do comando", "assunto, tema e tese (exemplo real)"]),
       ("34.e2", 1, ["núcleo e delimitadores", "“desafios para”, “caminhos para”, “perspectivas acerca de”", "foco × tema",
                     "pergunta-problema"]),
       ("35.e3", 2, ["os 3 passos da Cartilha nos motivadores", "linhas copiadas, inteiras ou em parte", "paráfrase + algo meu"]),
       ("35.e4", 3, ["completa, tangencia e fuga, com as consequências"]),
       ("35.e5", 4, ["tese provisória com todos os blocos", "conferir a tese antes de desenvolver"])]


def b_dominio(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE SABE EXPLICAR", PURPLE)
    a0 = ep(t, C["33.a"], 0.5)
    if t < C["34"] - 0.05:
        boxed(c, 300, 330, 1320, 170, PURPLE, a0, 0.07)
        text(c, "só o que você explicaria EM VOZ ALTA", W / 2, 400, 40, "black", PURPLE, a0)
        text(c, "para outra pessoa, sem consultar nada", W / 2, 460, 32, "bold", INK2, a0)
        pill(c, "não marcou? reveja o episódio correspondente", W / 2, 620, AMBER, size=30, a=ep(t, C["33.b"], 0.4), anchor="center")
        return
    cols = [(0, 1), (2, 3, 4)]
    for ci, idxs in enumerate(cols):
        y = 210
        for i in idxs:
            cue, ic, itens = DOM[i]
            a = ep(t, C[cue], 0.4)
            x = 200 + ci * 780
            icone(c, ic, x + 40, y + 40, a, 0.62, label=False)
            text(c, f"EPISÓDIO {i + 1}", x + 100, y + 30, 18, "black", ICONES[ic][2], a, align="left", tracking=2)
            for j, s in enumerate(itens):
                yy = y + 72 + j * 42
                rrect(c, x + 100, yy - 22, 26, 26, 6, "#FFFFFF", a, stroke=2.5, stroke_color=INK2)
                text(c, s, x + 140, yy, 24, "bold", INK, a * ep(t, C[cue] + 0.4 * j, 0.3), align="left")
            y += 84 + len(itens) * 42


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO ASSUNTO", "INTRODUÇÃO", BLUE)
    aa = ep(t, C["36.a"], 0.5)
    text(c, "Introdução: contextualização e apresentação da tese", W / 2, 260, 40, "black", BLUE, aa)
    ac = ep(t, C["36.c"], 0.5)
    rrect(c, 280, 360, 560, 240, 20, mix("#FFFFFF", GREEN, 0.08), ac, shadow=True)
    text(c, "TESE", 560, 460, 54, "black", GREEN, ac)
    text(c, "que cobre o recorte", 560, 520, 28, "bold", INK2, ac)
    ad = ep(t, C["36.d"], 0.5)
    arrow(c, 880, 480, 1040, 480, BLUE, ad, 6, 20, progress=ad)
    paper(c, 1080, 340, 560, 300, ad, lh=46, top=380)
    hand(c, "1º parágrafo", 1180, 420, 36, PEN, ad)
    for k in range(4):
        line(c, 1180, 470 + k * 40, 1560 - (k % 2) * 80, 470 + k * 40, LIGHT, ad, 7)


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"], "Quantas das dez você acertou no verdadeiro ou falso?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, habitos=b_habitos, mapa=b_mapa, vf=b_vf, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5,
              desafio=b_desafio, modelo=b_modelo, dominio=b_dominio, ponte=b_ponte, cta=b_cta)
