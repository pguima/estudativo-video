"""Visual — Compreensão Global e Tese, Episódio 7: Revisão geral, pegadinhas e treino (tema claro).
Índice visual da revisão = os 6 ícones dos episódios: mesa (1), balão de WhatsApp (2), cabide com roupa (3),
claquete de cinema (4), placa de trânsito (5) e câmera fotográfica (6). Cada lembrete do V/F mostra o ícone do episódio.
V/F: afirmação no cartão → cronômetro na pausa → carimbo VERDADEIRO/FALSO → selo "PEGADINHA" (amarelo) → regra (roxo).
Questões 1–5 (inéditas): texto inteiro com marca-texto acompanhando a voz + "Texto elaborado para fins didáticos";
depois a tese própria (azul) e as alternativas, riscadas com o NOME da armadilha.
Cores: azul = tese/definição · verde = pista/palavra-sinal · amarelo = armadilha · vermelho = erro · roxo = regra.
Peças reaproveitadas dos eps. 1 a 6 (V1…V6).
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

HERE = Path(__file__).resolve().parent
SERIE = HERE.parent.parent


def _load(nome, path):
    spec = importlib.util.spec_from_file_location(nome, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


V6 = _load("visual_ep6", SERIE / "ep6_tese_implicita" / "roteiro" / "visual.py")
V5, V4, V3, V2, V1 = V6.V5, V6.V4, V6.V3, V6.V2, V6.V1
motor.set_theme("claro")
try:   # a leitura (classe do ep. 2) usa os tempos deste episódio
    V2._SC = {s["id"]: s for s in json.load(open(HERE.parent / "audio" / "tempos.json", encoding="utf-8"))["scenes"]}
except Exception:
    V2._SC = {}

MARCA = ""
ARQUIVO_FINAL = "enem_linguagens_compreensao_ep7_estrategia_revisao.mp4"
CARD_R = (140, 150, 1640, 690)

wrap, para, which, frame, head_seq, boxed, regra, selo, pause_timer = (
    V1.wrap, V1.para, V1.which, V1.frame, V1.head_seq, V1.boxed, V1.regra, V1.selo, V1.pause_timer)
notas, Leitura, caixa, alternativas = V2.notas, V2.Leitura, V4.caixa, V4.alternativas
DIDATICO = "Texto elaborado para fins didáticos"


# ======================================================================
# os 6 ícones dos episódios
# ======================================================================

def ic_mesa(c, cx, cy, s, a, col=BLUE):
    if a <= 0:
        return
    rrect(c, cx - 70 * s, cy - 34 * s, 140 * s, 24 * s, 6 * s, col, a, shadow=True)
    for dx in (-52, 40):
        rrect(c, cx + dx * s, cy - 12 * s, 12 * s, 66 * s, 3 * s, mix(col, "#000000", 0.25), a)
    text_mid(c, "TESE", cx, cy - 22 * s, 15 * s, "black", "#FFFFFF", a)


def ic_whats(c, cx, cy, s, a, col="#25A85A"):
    if a <= 0:
        return
    rrect(c, cx - 70 * s, cy - 44 * s, 140 * s, 74 * s, 22 * s, col, a, shadow=True)
    p = skia.Path(); p.moveTo(cx + 30 * s, cy + 28 * s); p.lineTo(cx + 58 * s, cy + 52 * s); p.lineTo(cx + 54 * s, cy + 22 * s); p.close()
    c.drawPath(p, paint(col, a))
    for j in range(2):
        rrect(c, cx - 50 * s, cy - 24 * s + j * 22 * s, (100 - 30 * j) * s, 10 * s, 5 * s, "#FFFFFF", a * 0.9)


def ic_cabide(c, cx, cy, s, a, col=AMBER):
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(cx, cy - 44 * s); p.quadTo(cx + 14 * s, cy - 58 * s, cx + 2 * s, cy - 66 * s)
    c.drawPath(p, paint(INK2, a, stroke=4 * s, cap_round=True))
    tri = skia.Path(); tri.moveTo(cx - 62 * s, cy - 14 * s); tri.lineTo(cx, cy - 44 * s); tri.lineTo(cx + 62 * s, cy - 14 * s)
    c.drawPath(tri, paint(INK2, a, stroke=5 * s, cap_round=True))
    V3.camisa(c, cx, cy + 2 * s, 46 * s, col, a)


def ic_claquete(c, cx, cy, s, a, col=INK):
    if a <= 0:
        return
    rrect(c, cx - 66 * s, cy - 18 * s, 132 * s, 72 * s, 6 * s, col, a, shadow=True)
    c.save(); c.translate(cx - 66 * s, cy - 22 * s); c.rotate(-14)
    rrect(c, 0, -22 * s, 134 * s, 22 * s, 4 * s, col, a)
    for k in range(5):
        p = skia.Path(); x0 = 8 * s + k * 26 * s
        p.moveTo(x0, 0); p.lineTo(x0 + 12 * s, -22 * s); p.lineTo(x0 + 24 * s, -22 * s); p.lineTo(x0 + 12 * s, 0); p.close()
        c.drawPath(p, paint("#FFFFFF", a))
    c.restore()
    for j in range(2):
        line(c, cx - 50 * s, cy + 6 * s + j * 22 * s, cx + 50 * s, cy + 6 * s + j * 22 * s, "#FFFFFF", a * 0.7, 3 * s)


def ic_placa(c, cx, cy, s, a):
    V5.placa(c, cx, cy, "curva", a, s * 0.75, label=False, poste=False)


def ic_camera(c, cx, cy, s, a):
    V6.camera(c, cx, cy - 10 * s, 0.62 * s, a)


ICONES = [ic_mesa, ic_whats, ic_cabide, ic_claquete, ic_placa, ic_camera]
EPS = [("EP. 1", "A MESA", "tampo = tese", BLUE), ("EP. 2", "O WHATSAPP", "resumo em 1 frase", GREEN),
       ("EP. 3", "A ROUPA", "armadilhas", AMBER), ("EP. 4", "O TRAILER", "onde está a tese", INK),
       ("EP. 5", "AS PLACAS", "palavras-sinal", GREEN), ("EP. 6", "O FOTÓGRAFO", "tese implícita", PURPLE)]


def icone(c, k, cx, cy, s, a):
    ICONES[k](c, cx, cy, s, a)


def indice(c, t, cues, y, a=1.0, hi=None, w=250, gap=20):
    """os 6 episódios lado a lado; cues = 6 tempos (ou None = já visível)"""
    x0 = W / 2 - (6 * w + 5 * gap) / 2
    for k in range(6):
        ak = a * (ep(t, cues[k], 0.4) if cues else 1.0)
        if ak <= 0:
            continue
        x = x0 + k * (w + gap)
        on = hi is None or hi == k
        rrect(c, x, y, w, 250, 20, "#FFFFFF" if on else "#F1F1EE", ak, shadow=on)
        icone(c, k, x + w / 2, y + 100, 0.95, ak * (1 if on else 0.35))
        ep_, nome, sub, col = EPS[k]
        text(c, ep_, x + w / 2, y + 30, 18, "black", GRAY, ak)
        text(c, nome, x + w / 2, y + 192, 25, "black", col if on else GRAY, ak)
        text(c, sub, x + w / 2, y + 226, 19, "bold", INK2, ak * (1 if on else 0.6))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "LINGUAGENS ENEM", "REVISÃO GERAL", BLUE)
    card(c, *CARD_R)
    areas = [("LINGUAGENS", BLUE), ("HUMANAS", AMBER), ("NATUREZA", GREEN)]
    for k, (s, col) in enumerate(areas):
        a, d = rise(t, C["01.a"] + 0.4 * k)
        y = 260 + k * 150 + d
        rrect(c, 260, y, 420, 110, 20, mix("#FFFFFF", col, 0.12), a)
        text(c, s, 470, y + 70, 38, "black", col, a)
        arrow(c, 700, y + 55, 900, 450, LIGHT, a * ep(t, C["01.b"], 0.4), 5, 18)
    ab = ep(t, C["01.b"], 0.5)
    rrect(c, 930, 330, 720, 240, 24, mix("#FFFFFF", BLUE, 0.10), ab, shadow=True)
    text(c, "o que o texto diz", 1290, 430, 50, "black", INK, ab)
    text(c, "COMO UM TODO", 1290, 500, 58, "black", BLUE, ab)
    selo(c, 1290, 680, ep(t, C["01.c"], 0.5), "O QUE MAIS RENDE PONTO", GREEN, -4, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "HOJE, A REVISÃO", "DOS SEIS EPISÓDIOS", PURPLE)
    cues = [C[f"02.{x}"] for x in "abcdef"]
    indice(c, t, cues, 230)
    ag = ep(t, C["02.g"], 0.5)
    if ag > 0:
        for k, (s, col) in enumerate((("EU PERGUNTO", BLUE), ("VOCÊ PAUSA", AMBER), ("VOCÊ RESPONDE", GREEN))):
            ak = ep(t, C["02.g"] + 0.5 * k, 0.4)
            pill(c, s, 520 + k * 440, 620, col, INK if col == AMBER else None, size=32, a=ak, anchor="center", bounds=(0, 1920))
            if k < 2:
                arrow(c, 680 + k * 440, 620, 760 + k * 440, 620, GRAY, ak, 4, 14)
        pause_timer(c, t, C["02.g"] + 1.0, W / 2, 760, ag, dur=1.6, r=36)


# ======================================================================
# como o ENEM cobra · os três hábitos
# ======================================================================

COBRA = [("03.a", "COMANDO DIRETO", "“a tese defendida é”"), ("03.b", "RESUMO", "“pode ser sintetizado como”"),
         ("03.c", "TÍTULO", "a relação com o texto"), ("03.d", "ORGANIZAÇÃO", "a função de um parágrafo"),
         ("03.e", "TESE IMPLÍCITA", "crônicas, charges, ironia")]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "COMO O ENEM PERGUNTA", "CINCO JEITOS", BLUE)
    for k, (cue, s, sub) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 312
        rrect(c, x, 260 + d, 290, 400, 20, mix("#FFFFFF", BLUE, 0.07), a, shadow=True)
        badge_num(c, k + 1, x + 145, 320 + d, a, 30, bg=BLUE)
        para(c, s, x + 145, 430 + d, 30, "black", BLUE, a, 250, 38, align="center")
        para(c, sub, x + 145, 540 + d, 24, "bold", INK2, a, 250, 32, align="center")


HABITOS = [("04.a", 0, "Separar ASSUNTO de TESE", "o assunto é a etiqueta; a tese, o tampo"),
           ("04.b", 1, "Formular a tese ANTES das alternativas", "numa frase, como mensagem de WhatsApp"),
           ("04.c", 2, "Reconhecer as ARMADILHAS", "as roupas do tamanho errado")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "TRÊS HÁBITOS", GREEN)
    for k, (cue, ic, s, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 220 + k * 200 + d
        rrect(c, 230, y, 1460, 170, 22, "#FFFFFF", a, shadow=True)
        icone(c, ic, 380, y + 90, 1.0, a)
        badge_num(c, k + 1, 540, y + 85, a, 30, bg=GREEN)
        text(c, s, 600, y + 80, 42, "black", INK, a, align="left")
        text(c, sub, 600, y + 132, 28, "bold", INK2, a, align="left")


# ======================================================================
# verdadeiro ou falso — os 9 erros da seção 11
# ======================================================================

VF = [  # (cena da afirmação, cena da resposta, ícone, lembrete, afirmação, verdadeiro?, por que engana, regra)
    ("06", "07", 0, "o tampo é a tese", "Pedem a tese; você responde “celular na escola”.", False,
     "tem as palavras do texto", "Tese tem verbo e posição."),
    ("08", "09", 0, "as pernas são exemplos", "O exemplo mais marcante costuma ser a ideia central.", False,
     "é o trecho que fica na memória", "Exemplo é perna, não tampo: redução."),
    ("10", "11", 3, "trailer × filme de detetive", "A primeira frase do texto é sempre a tese.", False,
     "muito texto começa pela tese", "Leia até o primeiro “mas”: a placa de curva."),
    ("12", "13", 2, "roupa larga demais", "Alternativa com “sempre”, “todos” ou “deve-se” merece desconfiança.", True,
     "essas palavras soam completas", "O texto vai tão longe? Se não: extrapolação."),
    ("14", "15", 2, "mesmo tecido, outro corte", "Se a alternativa usa as palavras do texto, ela está certa.", False,
     "você reconhece as palavras", "Confira o que se afirma: tema certo, tese errada."),
    ("16", "17", 2, "roupa de outro armário", "Uma alternativa verdadeira no mundo pode estar errada na questão.", True,
     "você SABE que aquilo é verdade", "Em que linha isso está?"),
    ("18", "19", 5, "a opinião está na escolha", "Num texto irônico, o elogio deve ser lido ao pé da letra.", False,
     "você repete o que está escrito", "Elogio irônico é crítica."),
    ("20", "21", 5, "seleção · contraste · tom", "Um texto sem nenhuma frase de opinião pode ter tese.", True,
     "“não achei nenhum eu acho”", "A opinião está na seleção, no contraste e no tom."),
    ("22", "23", 1, "a tese em uma frase", "Para ganhar tempo, leia as alternativas antes de ter a sua tese.", False,
     "parece economizar tempo", "Formule primeiro, compare depois."),
]
VF_IDS = [v[0] for v in VF] + [v[1] for v in VF]


def carimbo(c, x, y, ok, a, s=None):
    if a <= 0:
        return
    selo(c, x, y, a, s or ("VERDADEIRO" if ok else "FALSO"), GREEN if ok else RED, -8, 44)


def b_vf(c, t, C, B):
    sid = which(t, C, ["05"] + sorted(VF_IDS))
    if sid == "05":
        frame(c, t, B["start"], "VERDADEIRO OU FALSO?", "NOVE AFIRMAÇÕES", AMBER)
        a = ep(t, C["05.t"], 0.4)
        for k in range(9):
            ak = a * ep(t, C["05.t"] + 0.12 * k, 0.3)
            c.drawCircle(560 + k * 100, 420, 36, paint(mix("#FFFFFF", AMBER, 0.25), ak))
            text_mid(c, str(k + 1), 560 + k * 100, 420, 34, "black", INK, ak)
        pill(c, "pause em cada uma e responda em voz alta", W / 2, 600, AMBER, INK, size=32, a=ep(t, C["05.a"], 0.4),
             anchor="center")
        pause_timer(c, t, C["05.a"] + 0.8, W / 2, 740, ep(t, C["05.a"], 0.4))
        return
    n = next(i for i, v in enumerate(VF) if sid in (v[0], v[1]))
    sq, sr, ic, lemb, afirm, ok, why, rg = VF[n]
    head(c, t, C[sq], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    for k in range(9):   # progresso
        col = AMBER if k == n else (mix("#FFFFFF", AMBER, 0.45) if k < n else LIGHT)
        c.drawCircle(1040 + k * 52, 205, 15, paint(col, 1))
    # lembrete com o ícone do episódio
    a0 = ep(t, C[sq], 0.4)
    rrect(c, 200, 250, 440, 520, 22, "#F7F7F5", a0)
    text(c, "LEMBRA?", 420, 300, 24, "black", GRAY, a0)
    icone(c, ic, 420, 440, 1.5, a0)
    ep_, nome, _, col = EPS[ic]
    text(c, f"{ep_} · {nome}", 420, 600, 26, "black", col, a0)
    para(c, lemb, 420, 660, 28, "bold", INK2, a0, 380, 36, align="center")
    # a afirmação
    aq = ep(t, C[f"{sq}.q"], 0.5)
    ar = ep(t, C[f"{sr}.r"], 0.4) if t >= C[sr] - 0.05 else 0.0
    colq = mix(INK, GREEN if ok else RED, ar)
    para(c, afirm, 700, 330, 44, "black", colq, aq, 900, 56)
    if t < C[sr]:
        pause_timer(c, t, C[f"{sq}.p"] + 0.6, 1150, 640, aq, dur=1.8)
    carimbo(c, 1440, 520, ok, ar, "ERRADO" if n == 0 else None)
    aa = ep(t, C[f"{sr}.a"], 0.4) if t >= C[sr] else 0.0
    if aa > 0:
        selo(c, 830, 560, aa, "PEGADINHA", AMBER, -4, 26)
        text(c, "parece certo porque " + why, 700, 640, 28, "bold", INK2, aa, align="left")
    ab = ep(t, C[f"{sr}.b"], 0.5) if t >= C[sr] else 0.0
    if ab > 0:
        w = min(940, text_w(rg, "black", 34) + 60)
        boxed(c, 1170 - w / 2, 690, w, 90, PURPLE, ab, 0.10)
        text_mid(c, rg, 1170, 735, 34 if text_w(rg, "black", 34) < 880 else 28, "black", PURPLE, ab)


# ======================================================================
# os 6 passos
# ======================================================================

PASSOS = [("24.a", "o COMANDO", "o que ele pede?"), ("24.b", "a FONTE", "opinião ou informação?"),
          ("24.c", "LER marcando as viradas", "mas · porém · portanto"), ("24.d", "a SUA TESE", "uma frase, antes das alternativas"),
          ("24.e", "ELIMINAR pelo tipo de erro", "contradição → extrapolação → redução"),
          ("24.f", "a PALAVRA que decide", "entre as duas finalistas")]


def passos_lista(c, t, C, x, y, dy=86, a=1.0, size=34, cues=True):
    for k, (cue, s, sub) in enumerate(PASSOS):
        al, d = rise(t, C[cue]) if cues else (1.0, 0)
        al *= a
        if al <= 0:
            continue
        yy = y + k * dy + d
        badge_num(c, k + 1, x, yy, al, 24, bg=PURPLE)
        text(c, s, x + 50, yy + 12, size, "black", INK, al, align="left")
        text(c, sub, x + 50 + text_w(s, "black", size) + 24, yy + 12, size * 0.7, "bold", GRAY, al, align="left")


def b_passos(c, t, C, B):
    frame(c, t, B["start"], "AGORA, AS QUESTÕES", "OS SEIS PASSOS · EP. 3", PURPLE)
    a0 = ep(t, C["24.t"], 0.4)
    icone(c, 2, 1520, 300, 1.4, a0)
    pill(c, "5 questões NOVAS", 1520, 450, GREEN, size=28, a=a0, anchor="center", bounds=(0, 1920))
    passos_lista(c, t, C, 280, 260)


# ======================================================================
# questões 1–5 (inéditas)
# ======================================================================

Q = {}
Q[1] = dict(
    ids=("25", "26", "27"), cmd="A tese defendida no texto é a de que", tipo="ARTIGO DE OPINIÃO", ok="C",
    tese="Ler para crianças é barato e dá resultado.",
    leitura=Leitura(
        [("25", "f1", "c1", "Ler em voz alta para crianças pequenas é um dos investimentos mais baratos e eficazes que uma família pode fazer."),
         ("25", "f2", "f3", "A leitura compartilhada amplia o vocabulário antes da alfabetização."),
         ("25", "f3", "f4", "Também cria um momento de atenção exclusiva, cada vez mais raro na rotina das telas."),
         ("25", "f4", "c2", "E não exige nada além de um livro e quinze minutos por dia.")],
        [(0, "um dos investimentos mais baratos e eficazes que uma família pode fazer.", "fill", BLUE, "25.c1"),
         (1, "amplia o vocabulário", "under", INK2, "25.c2"), (2, "atenção exclusiva,", "under", INK2, "25.c2"),
         (3, "um livro e quinze minutos", "under", INK2, "25.c2")]),
    notas=[("25.c1", "1ª FRASE", "opinião logo de cara: trailer?", BLUE), ("25.c2", "TEXTO DEDUTIVO", "o resto sustenta a 1ª frase", GREEN)],
    alts=[("A", "a leitura compartilhada amplia o vocabulário antes da alfabetização.", "26.a", "27.a", "REDUÇÃO: uma perna só"),
          ("B", "as famílias devem proibir as telas para que as crianças leiam mais.", "26.b", "27.b", "EXTRAPOLAÇÃO"),
          ("C", "ler em voz alta para crianças pequenas é um investimento barato e eficaz.", "26.c", None, ""),
          ("D", "ler para crianças exige tempo e dinheiro que poucas famílias têm.", "26.d", "27.d", "CONTRADIÇÃO"),
          ("E", "crianças que leem mais tiram notas melhores na escola.", "26.e", "27.e", "VERDADE DO MUNDO")])
Q[2] = dict(
    ids=("28", "29", "30"), cmd="O autor defende que", tipo="ARTIGO DE OPINIÃO", ok="A",
    tese="O jovem lê; mudaram o quê e o onde.",
    leitura=Leitura(
        [("28", "f1", "c1", "Há quem diga que o jovem de hoje não lê."),
         ("28", "f2", "c2", "Mas basta ver as filas de autógrafos nas feiras de livros, os clubes de leitura nas redes e os romances que viralizam entre adolescentes."),
         ("28", "f3", "f4", "O jovem lê, e muito; o que mudou foi o que ele lê e onde conversa sobre isso."),
         ("28", "f4", "end", "Quem procura o leitor só na biblioteca é que não o encontra.")],
        [(0, "Há quem diga", "box", AMBER, "28.c1"), (1, "Mas", "box", GREEN, "28.c2"),
         (2, "O jovem lê, e muito; o que mudou foi o que ele lê e onde conversa sobre isso.", "fill", BLUE, "28.f4")]),
    notas=[("28.c1", "“HÁ QUEM DIGA”", "a voz do outro: desconfie", AMBER), ("28.c2", "PLACA DE CURVA", "“mas”: vem a opinião do autor", GREEN)],
    alts=[("A", "os jovens continuam lendo; mudaram o que leem e onde conversam sobre leitura.", "29.a", None, ""),
          ("B", "o jovem de hoje lê pouco, porque prefere as redes sociais aos livros.", "29.b", "30.b", "CONTRADIÇÃO: a voz que o autor derruba"),
          ("C", "as feiras de livros reúnem filas enormes de jovens atrás de autógrafos.", "29.c", "30.c", "REDUÇÃO: um exemplo"),
          ("D", "o interesse dos jovens pela leitura depende, sobretudo, das bibliotecas escolares.", "29.d", "30.d", "TEMA CERTO, TESE ERRADA"),
          ("E", "as bibliotecas deveriam ser substituídas por clubes de leitura nas redes.", "29.e", "30.e", "EXTRAPOLAÇÃO")])
Q[3] = dict(
    ids=("31", "32", "33"), cmd="A ideia central do texto é a de que", tipo="TEXTO DE OPINIÃO", ok="D",
    tese="Espaço público bem cuidado volta a ser ocupado.",
    leitura=Leitura(
        [("31", "f1", "f2", "Num bairro, uma praça ganhou bancos e iluminação e passou a receber feiras aos domingos."),
         ("31", "f2", "c2", "Em outro, uma rua fechada para carros nos fins de semana virou ponto de encontro de famílias."),
         ("31", "f3", "f4", "Num terceiro, um viaduto ganhou quadra e grafites e deixou de ser evitado à noite."),
         ("31", "f4", "c4", "Quando a cidade cuida do espaço público, as pessoas voltam a ocupá-lo.")],
        [(0, "Num bairro,", "under", GREEN, None), (1, "Em outro,", "under", GREEN, None), (2, "Num terceiro,", "under", GREEN, None),
         (3, "Quando a cidade cuida do espaço público, as pessoas voltam a ocupá-lo.", "fill", BLUE, "31.c4")]),
    notas=[("31.c2", "CASO, CASO...", "ainda nenhuma opinião", GREEN), ("31.c4", "TESE NO FIM", "filme de detetive: indutivo", BLUE)],
    alts=[("A", "uma praça reformada passou a receber feiras aos domingos.", "32.a", "33.a", "REDUÇÃO: um caso só"),
          ("B", "todas as cidades devem fechar ruas para carros nos fins de semana.", "32.b", "33.b", "EXTRAPOLAÇÃO: “todas”, “devem”"),
          ("C", "reformar espaços públicos afasta os moradores, que preferem lugares fechados.", "32.c", "33.c", "CONTRADIÇÃO"),
          ("D", "espaços públicos bem cuidados voltam a ser ocupados pelas pessoas.", "32.d", None, ""),
          ("E", "praças arborizadas ajudam a reduzir a temperatura das cidades.", "32.e", "33.e", "VERDADE DO MUNDO")])
Q[4] = dict(
    ids=("34", "35", "36"), cmd="A crônica sugere que", tipo="CRÔNICA", ok="B",
    tese="A praticidade não aproximou ninguém; foi preciso um imprevisto.",
    leitura=Leitura(
        [("34", "f1", "f2", "O condomínio instalou um aplicativo para tudo: reservar a churrasqueira, avisar da encomenda, reclamar do barulho."),
         ("34", "f2", "f3", "Ontem, o elevador parou entre dois andares, comigo e com o vizinho do 302."),
         ("34", "f3", "c3", "Em vinte minutos, descobri que ele é professor, torce para o meu time e mora ali há oito anos."),
         ("34", "f4", "end", "Quando a porta abriu, ele suspirou: — A gente devia quebrar o elevador mais vezes.")],
        [(0, "um aplicativo para tudo:", "box", GREEN, "35.a"), (2, "mora ali há oito anos.", "box", GREEN, "34.c3"),
         (3, "A gente devia quebrar o elevador mais vezes.", "under", AMBER, "36.c")]),
    notas=[("34.c3", "OITO ANOS", "e nunca tinham conversado", GREEN), ("35.a", "LADO A LADO", "app para TUDO × vizinho desconhecido", GREEN)],
    alts=[("A", "os vizinhos descobriram que torcem para o mesmo time.", "35.c", "36.a", "REDUÇÃO: um detalhe"),
          ("B", "a praticidade do aplicativo não aproximou os vizinhos, que só se conheceram por causa de um imprevisto.", "35.d", None, ""),
          ("C", "quebrar o elevador mais vezes é um bom jeito de os vizinhos se conhecerem.", "35.e", "36.c", "AO PÉ DA LETRA → CONTRADIÇÃO"),
          ("D", "os condomínios deveriam proibir aplicativos para obrigar os moradores a conversar.", "35.f", "36.d", "EXTRAPOLAÇÃO"),
          ("E", "o uso excessivo do celular está ligado a sintomas de ansiedade.", "35.g", "36.e", "VERDADE DO MUNDO")])
Q[5] = dict(
    ids=("37", "38", "39"), cmd="De acordo com o texto,", tipo="DIVULGAÇÃO CIENTÍFICA", ok="E",
    tese="Há relação, mas não está provado que uma coisa causa a outra.",
    leitura=Leitura(
        [("37", "f1", "c1", "Um levantamento com três mil adultos observou que quem caminhava ao ar livre pelo menos três vezes por semana relatava, em média, menos dificuldade para dormir."),
         ("37", "f2", "c2", "Os autores alertam que o estudo mostra uma relação, e não prova que a caminhada melhore o sono: quem dorme bem pode simplesmente ter mais disposição para sair de casa.")],
        [(0, "observou", "box", GREEN, "37.c1"), (1, "mostra uma relação, e não prova", "fill", BLUE, "37.c2")]),
    notas=[("37.c1", "“OBSERVOU”", "uma relação", GREEN), ("37.c2", "O TEXTO AVISA", "relação NÃO é causa", BLUE)],
    alts=[("A", "caminhar ao ar livre faz as pessoas dormirem melhor.", "38.a", "39.a", "EXTRAPOLAÇÃO: relação virou causa"),
          ("B", "a luz do sol regula o relógio biológico e melhora o sono.", "38.b", "39.b", "VERDADE DO MUNDO"),
          ("C", "o levantamento mostrou que não há relação entre caminhar e dormir bem.", "38.c", "39.c", "CONTRADIÇÃO"),
          ("D", "três mil adultos participaram do levantamento.", "38.d", "39.d", "REDUÇÃO: um dado"),
          ("E", "o estudo encontrou uma relação entre caminhar e dormir melhor, mas não provou que uma coisa cause a outra.", "38.e", None, "")])

QARGS = (200, 330, 1060, 32, 50)
QSMALL = (190, 330, 600, 20, 30)
TIPO_COR = {"ARTIGO DE OPINIÃO": BLUE, "TEXTO DE OPINIÃO": BLUE, "CRÔNICA": PURPLE, "DIVULGAÇÃO CIENTÍFICA": GREEN}


def b_questao(n):
    q = Q[n]
    s1, s2, s3 = q["ids"]

    def f(c, t, C, B):
        head_seq(c, t, C, [(s1, f"QUESTÃO {n} DE 5", q["tipo"], TIPO_COR[q["tipo"]]),
                           (s2, f"QUESTÃO {n} DE 5", "AS ALTERNATIVAS", AMBER), (s3, f"QUESTÃO {n} DE 5", "AS ARMADILHAS", RED)])
        card(c, *CARD_R)
        pill(c, "COMANDO: " + q["cmd"], 200, 200, BLUE, size=24, a=ep(t, C[f"{s1}.a"], 0.4), bounds=(0, 1920))
        ph = ep(t, C[s2], 0.7)
        L = q["leitura"]
        if ph < 1:
            a = 1 - ph
            L.draw(c, t, C, *QARGS, a * ep(t, C[f"{s1}.f1"] - 0.3, 0.4))
            text(c, DIDATICO, 200 + 1060, 805, 18, "bold", GRAY, a * ep(t, C[f"{s1}.f1"], 0.4), align="right")
            notas(c, t, C, q["notas"], 1310, 330, 110, 400, a)
        if ph > 0:
            L.draw(c, t, C, *QSMALL, ph * 0.9)
            text(c, DIDATICO, 790, 805, 15, "bold", GRAY, ph, align="right")
            # a tese própria
            at = ep(t, C[s2], 0.5)
            y_t = 640
            rrect(c, 180, y_t, 620, 120, 16, mix("#FFFFFF", BLUE, 0.10), at)
            pill(c, "MINHA TESE", 200, y_t, BLUE, size=18, a=at, bounds=(0, 1920))
            para(c, q["tese"], 490, y_t + 52, 24, "black", BLUE, at, 580, 30, align="center")
            ok_cue = f"{s3}.ok"
            aok = alternativas(c, t, C, q["alts"], ok_cue, 920, 250, 760, ph, 22)
            if t < C[s3]:
                pause_timer(c, t, C[f"{s2}.p"] + 0.4, 705, 555, ph, dur=1.8, r=30)
            result_box(c, f"Letra {q['ok']}", 1300, 800, 44, aok, GREEN)
    return f


# ======================================================================
# outras áreas · checklist · meta
# ======================================================================

def frasco(c, cx, cy, s, a, col=GREEN):
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(cx - 18 * s, cy - 70 * s); p.lineTo(cx - 18 * s, cy - 20 * s); p.lineTo(cx - 60 * s, cy + 50 * s)
    p.lineTo(cx + 60 * s, cy + 50 * s); p.lineTo(cx + 18 * s, cy - 20 * s); p.lineTo(cx + 18 * s, cy - 70 * s); p.close()
    c.drawPath(p, paint("#FFFFFF", a)); c.drawPath(p, paint(INK, a, stroke=5 * s))
    q = skia.Path(); q.moveTo(cx - 40 * s, cy + 18 * s); q.lineTo(cx - 60 * s, cy + 50 * s); q.lineTo(cx + 60 * s, cy + 50 * s)
    q.lineTo(cx + 40 * s, cy + 18 * s); q.close()
    c.drawPath(q, paint(col, a * 0.8))


def livro(c, cx, cy, s, a, col=AMBER):
    if a <= 0:
        return
    for d in (-1, 1):
        p = skia.Path(); p.moveTo(cx, cy - 40 * s); p.quadTo(cx + d * 40 * s, cy - 56 * s, cx + d * 80 * s, cy - 44 * s)
        p.lineTo(cx + d * 80 * s, cy + 46 * s); p.quadTo(cx + d * 40 * s, cy + 34 * s, cx, cy + 50 * s); p.close()
        c.drawPath(p, paint("#FFFFFF", a)); c.drawPath(p, paint(col, a, stroke=5 * s))
        for j in range(3):
            line(c, cx + d * 16 * s, cy - 20 * s + j * 18 * s, cx + d * 62 * s, cy - 24 * s + j * 18 * s, LIGHT, a, 3 * s)


def lapis(c, cx, cy, s, a, col=BLUE):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(-35)
    rrect(c, -80 * s, -14 * s, 130 * s, 28 * s, 4 * s, col, a)
    p = skia.Path(); p.moveTo(50 * s, -14 * s); p.lineTo(80 * s, 0); p.lineTo(50 * s, 14 * s); p.close()
    c.drawPath(p, paint("#F1C27D", a))
    c.drawCircle(76 * s, 0, 4 * s, paint(INK, a))
    rrect(c, -96 * s, -14 * s, 18 * s, 28 * s, 4 * s, "#F48FB1", a)
    c.restore()


def b_areas(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ LINGUAGENS", "A MESMA HABILIDADE NA PROVA TODA", BLUE)
    cols = [("40.a", "HUMANAS", "historiadores e filósofos", "a tese está lá", AMBER, livro),
            ("40.b", "NATUREZA", "divulgação científica", "relação não é causa", GREEN, frasco),
            ("40.c", "REDAÇÃO", "a tese que você acha...", "...é a que vai escrever", BLUE, lapis)]
    for k, (cue, s, sub, dica, col, ic) in enumerate(cols):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 510
        rrect(c, x, 230 + d, 460, 540, 22, mix("#FFFFFF", col, 0.08), a, shadow=True)
        ic(c, x + 230, 360 + d, 1.2, a, col)
        text(c, s, x + 230, 500 + d, 44, "black", col, a)
        text(c, sub, x + 230, 560 + d, 28, "bold", INK2, a)
        pill(c, dica, x + 230, 660 + d, col, INK if col == AMBER else None, size=26, a=a * ep(t, C[cue] + 1.0, 0.4),
             anchor="center", bounds=(0, 1920))


CHECK = [  # (cue, episódio, itens)
    ("41.e1", 0, ["Tema, assunto e tese (com exemplo)", "O teste da discordância", "O teste do apagamento"]),
    ("41.e2", 1, ["Resumo: assunto + afirmação + porquê"]),
    ("41.e3", 2, ["As armadilhas e a verdade do mundo", "A tese antes das alternativas", "Comandos: de acordo, infere-se, defende"]),
    ("41.e4", 3, ["Dedutivo e indutivo", "A 1ª frase que o autor vai derrubar"]),
    ("41.e5", 4, ["Título, tópico frasal e marcas", "A função de um parágrafo"]),
    ("41.e6", 5, ["Reconstruo uma tese implícita"]),
]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE SABE EXPLICAR", PURPLE)
    aa = ep(t, C["41.a"], 0.4)
    pill(c, "em voz alta, para outra pessoa, sem consultar nada", W / 2, 200, PURPLE, size=26, a=aa, anchor="center")
    for k, (cue, ic, itens) in enumerate(CHECK):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        col_x = 190 + (k % 3) * 520
        y = 250 + (k // 3) * 275 + d
        rrect(c, col_x, y, 490, 250, 18, "#FFFFFF", a, shadow=True)
        icone(c, ic, col_x + 70, y + 70, 0.62, a)
        ep_, nome, _, col = EPS[ic]
        text(c, ep_ + " · " + nome, col_x + 140, y + 60, 22, "black", col, a, align="left")
        for j, s in enumerate(itens):
            yy = y + 135 + j * 44
            rrect(c, col_x + 24, yy - 22, 26, 26, 6, "#FFFFFF", a, stroke=3, stroke_color=GRAY)
            text(c, s, col_x + 64, yy, 20, "bold", INK, a, align="left")
    ab = ep(t, C["41.b"], 0.5)
    pill(c, "o que não marcou → reveja o episódio correspondente", W / 2, 812, RED, size=26, a=ab, anchor="center")


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE MARCAR “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["42.a"], 0.5)
    text(c, "25 questões de interpretação", 560, 300, 44, "black", INK, aa)
    ab = ep(t, C["42.b"], 0.5)
    n = int(18 * ease_out(prog(t, C["42.b"], 1.4)))
    glow = ab
    text(c, f"{n}", 470, 490, 150, "black", GREEN, glow)
    text(c, "/ 25", 650, 490, 70, "black", GRAY, glow)
    if ab > 0:
        rrect(c, 260, 560, 600, 34, 17, "#EDEDE8", ab)
        rrect(c, 260, 560, 600 * n / 25, 34, 17, GREEN, ab)
        line(c, 260 + 600 * 0.7, 548, 260 + 600 * 0.7, 606, INK, ab, 4)
        text(c, "70%", 260 + 600 * 0.7, 640, 28, "black", INK, ab)
    ac = ep(t, C["42.c"], 0.5)
    if ac > 0:
        rrect(c, 1000, 240, 620, 480, 20, "#FFFFFF", ac, shadow=True)
        text(c, "EM CADA ERRO, QUAL ARMADILHA?", 1310, 300, 26, "black", AMBER, ac)
        rows = [("redução", 4), ("extrapolação", 6), ("contradição", 1), ("tema certo, tese errada", 2), ("verdade do mundo", 1)]
        for k, (s, m) in enumerate(rows):
            yy = 370 + k * 66
            text(c, s, 1040, yy, 28, "bold", INK, ac, align="left")
            for j in range(m):
                aj = ac * ep(t, C["42.c"] + 0.2 + 0.08 * (k * 6 + j), 0.2)
                line(c, 1400 + j * 22, yy - 26, 1400 + j * 22, yy + 4, RED, aj, 5)
        text(c, "exemplo", 1600, 700, 18, "bold", GRAY, ac, align="right")
    ad = ep(t, C["42.d"], 0.5)
    pill(c, "o padrão dos erros mostra o que treinar", 1310, 790, AMBER, INK, size=26, a=ad, anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO ASSUNTO", "INFORMAÇÕES EXPLÍCITAS E IMPLÍCITAS", PURPLE)
    a0 = ep(t, C["43.t"], 0.4)
    indice(c, t, None, 220, a0 * (1 - ep(t, C["43.a"], 0.5)))
    aa = ep(t, C["43.a"], 0.5)
    if aa > 0:
        z = ep(t, C["43.b"], 0.8)
        # o texto inteiro → uma frase
        x, y, w, h = lerp(260, 200, z), lerp(240, 300, z), lerp(560, 1520, z), lerp(460, 140, z)
        rrect(c, x, y, w, h, 16, "#FFFFFF", aa, shadow=True)
        if z < 0.5:
            V6.texto_fake(c, x + 50, y + 60, w - 100, 11, aa * (1 - 2 * z), LIGHT, 32)
        if z > 0.3:
            text(c, "“O condomínio instalou um aplicativo para tudo.”", x + w / 2, y + h / 2 + 14, 44, "black", INK,
                 aa * clamp((z - 0.3) / 0.5))
        text(c, "do TEXTO INTEIRO", 1300, 420, 40, "black", BLUE, aa * (1 - z))
        text(c, "para a FRASE", 1300, 490, 40, "black", PURPLE, aa * (1 - z) * ep(t, C["43.b"] - 0.6, 0.4))
    rows = [("43.c", "o que está ESCRITO", BLUE), ("43.c", "o que está SUGERIDO", GREEN), ("43.d", "até onde CONCLUIR", AMBER)]
    for k, (cue, s, col) in enumerate(rows):
        ak = ep(t, C[cue] + (1.2 if k == 1 else 0), 0.4)
        pill(c, s, 480 + k * 480, 600, col, INK if col == AMBER else None, size=32, a=ak, anchor="center", bounds=(0, 1920))
    pill(c, "o próximo assunto de Linguagens", W / 2, 760, PURPLE, size=30, a=ep(t, C["43.d"] + 1.0, 0.4), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["44.like"], C["44.sub"], C["44.bell"], C["44.com"], C["44.bye"], "Quantas das 5 questões você acertou?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, cobra=b_cobra, habitos=b_habitos, vf=b_vf, passos=b_passos,
              q1=b_questao(1), q2=b_questao(2), q3=b_questao(3), q4=b_questao(4), q5=b_questao(5),
              areas=b_areas, checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
