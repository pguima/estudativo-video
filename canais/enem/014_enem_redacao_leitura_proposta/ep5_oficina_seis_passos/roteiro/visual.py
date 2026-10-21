"""Visual — Redação ENEM, Leitura da Proposta, Episódio 5: Oficina — a leitura em 6 passos (tema claro).
Reaproveita o ep4 (V4: placar, marcas, veredito) e, por ele, o ep3, o ep2 (V2: peças, frase em blocos, alternativas)
e o ep1 (V1: rascunho, caligrafia, etiqueta).
Novo: CHECKLIST dos 6 passos fixo à esquerda (passo atual aceso, feitos com ✓) + RASCUNHO à direita, onde o professor
escreve ao vivo (frase temática sublinhada em duas cores, notas dos blocos, pergunta, tese com 1ª tentativa riscada).
Cores: azul = núcleo/tema · verde = delimitadores e método · âmbar = armadilha · vermelho = erro · roxo = regra oficial.
"""
import importlib.util
import json
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "ep4_tangenciamento_fuga" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v_ep4", _p)
V4 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V4)
V2, V1 = V4.V2, V4.V1
motor.set_theme("claro")
try:
    V1._SC = {s["id"]: s for s in json.load(open(Path(__file__).resolve().parent.parent / "audio" / "tempos.json",
                                                 encoding="utf-8"))["scenes"]}
except Exception:
    V1._SC = {}

paper, hand, hand_para, hwrap, hand_w = V1.paper, V1.hand, V1.hand_para, V1.hwrap, V1.hand_w
boxed, selo, pause_timer, which, para, wrap = V1.boxed, V1.selo, V1.pause_timer, V1.which, V1.para, V1.wrap
frame, head_seq, phrase_span, wreveal, underline = V1.frame, V1.head_seq, V1.phrase_span, V1.wreveal, V1.underline
alts_panel, puzzle, seg_layout, draw_segs, pen_draw = V2.alts_panel, V2.puzzle, V2.seg_layout, V2.draw_segs, V2.pen_draw
centros, veredito = V4.centros, V4.veredito
PEN = V1.PEN
NUC, DEL = BLUE, GREEN

MARCA = ""
ARQUIVO_FINAL = "enem_redacao_leitura_proposta_ep5_oficina_seis_passos.mp4"
CARD_R = (140, 150, 1640, 690)

TEMA21 = "Invisibilidade e registro civil: garantia de acesso à cidadania no Brasil"
PERGUNTA = ("Por que parte da população brasileira ainda vive sem registro civil, e o que isso significa para o acesso à "
            "cidadania?")
TENTATIVA = ("A falta de registro civil torna muitas pessoas invisíveis para o Estado e as afasta de direitos básicos, por "
             "causa da distância dos cartórios e da desinformação.")
TESE = ("A falta de registro civil torna milhares de brasileiros invisíveis para o Estado, o que os afasta de direitos "
        "básicos; esse quadro persiste pela distância entre os cartórios e as populações mais isoladas e pela "
        "desinformação sobre a gratuidade do registro.")
TANG = ("A cidadania é um conceito antigo, que surgiu na Grécia e se transformou ao longo da história até chegar às "
        "democracias modernas.")
TEMA20 = "O estigma associado às doenças mentais na sociedade brasileira"

PASSOS = [("Frase temática", "ler primeiro e copiar no rascunho", "sei dizer o tema com as palavras da prova?"),
          ("Blocos", "separar núcleo e delimitadores", "o que cada bloco obriga a discutir?"),
          ("Motivadores", "ler com os três passos da Cartilha, anotando na margem", "qual é a situação-problema?"),
          ("Pergunta-problema", "reescrever o tema como pergunta", "a pergunta contém todos os blocos?"),
          ("Tese provisória", "responder à pergunta com uma posição e dois eixos", "alguém poderia discordar dela?"),
          ("Conferência", "pôr a tese ao lado da frase temática", "algum bloco ficou de fora?")]

# peças da frase de 2021 (ordem da frase); a cue serve para o sublinhado colorido no rascunho
T21 = [("Invisibilidade", DEL, "PROBLEMA", None, "12.b"), ("registro civil", NUC, "NÚCLEO", None, "11.a"),
       ("garantia de acesso à cidadania", DEL, "RELAÇÃO", None, "12.c"), ("no Brasil", DEL, "LUGAR", None, "13.d")]
# a frase manuscrita, palavra a palavra, com o bloco de cada trecho ("e" e ":" ficam na cor da caneta)
SEG_FRASE = [("Invisibilidade", DEL, "", None, "12.b"), ("e", PEN, "", None, "40.bye"),
             ("registro civil:", NUC, "", None, "11.a"), ("garantia de acesso à cidadania", DEL, "", None, "12.c"),
             ("no Brasil", DEL, "", None, "13.d")]

# área principal (à direita do checklist)
MX, MY, MW, MH = 470, 150, 1410, 700
DX = (MX + MW / 2) - W / 2   # deslocamento para centralizar peças na área principal


# ======================================================================
# checklist fixo
# ======================================================================

def checklist(c, cur, a=1.0, feitos=None, ctrl_a=1.0, x=40, y=150, w=400):
    """6 passos; cur = índice aceso (0–5) ou None; feitos = quantos já têm ✓"""
    if a <= 0:
        return
    feitos = cur if feitos is None and cur is not None else (feitos or 0)
    rrect(c, x, y, w, 700, 24, "#FFFFFF", a, shadow=True)
    text(c, "CHECKLIST", x + w / 2, y + 48, 22, "black", GRAY, a, tracking=3)
    for k, (nm, _, ctrl) in enumerate(PASSOS):
        yy = y + 80 + k * 102
        on_ = k == cur
        if on_:
            rrect(c, x + 14, yy - 8, w - 28, 104, 16, mix("#FFFFFF", GREEN, 0.14), a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 14, yy - 8, w - 28, 104), 16, 16), paint(GREEN, a, stroke=3))
        done = k < feitos
        if done:
            check_icon(c, x + 52, yy + 26, 22, a, GREEN)
        else:
            badge_num(c, k + 1, x + 52, yy + 26, a, 22, bg=GREEN if on_ else LIGHT)
        text(c, nm, x + 90, yy + 34, 28, "black", INK if (on_ or done) else GRAY, a, align="left")
        if on_:
            para(c, ctrl, x + 90, yy + 62, 15, "bold", GREEN, a * ctrl_a, w - 110, 17)


def rascunho(c, a=1.0):
    paper(c, MX, MY, MW, MH, a, lh=56, top=MY + 64)


def frase_rascunho(c, t, C, a=1.0, reveal=1.0, y=MY + 110, under=True):
    lay = seg_layout(SEG_FRASE, MX + 110, y, 36, MW - 160, 56)
    draw_segs(c, t, C, SEG_FRASE, lay, 36, a, True, reveal, under=under)


def hspan(sid, phrase, C, dur=3.0):
    t0 = C[sid]
    return phrase_span(sid, phrase, t0, t0 + dur)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM · OFICINA", "DO TEMA ATÉ A TESE", GREEN)
    paper(c, 1000, 180, 760, 640, ep(t, C["01.a"], 0.5), lh=56, top=240)
    pen_draw(c, 1560, 600, PEN, ep(t, C["01.b"], 0.5), -35, 1.4)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "PEGUE", 220, 330, 40, "black", GRAY, ab, align="left", tracking=3)
    text(c, "papel e caneta", 220, 420, 76, "black", INK, ab, align="left")
    ac = ep(t, C["01.c"], 0.5)
    text(c, "uma proposta real · do zero até a tese", 220, 510, 34, "bold", INK2, ac, align="left")
    for k in range(6):
        a = ep(t, C["01.d"] + 0.15 * k, 0.4)
        badge_num(c, k + 1, 260 + k * 100, 640, a, 36, bg=GREEN)
    text(c, "6 PASSOS", 1380, 300, 60, "black", GREEN, ep(t, C["01.d"], 0.5))
    for k in range(6):
        hand(c, f"{k + 1}. ________", 1110, 390 + k * 56, 32, PEN, ep(t, C["01.d"] + 0.15 * k, 0.4))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI TER", GREEN)
    rows = [("02.a", "um MÉTODO para qualquer proposta"), ("02.b", "uma TESE que cobre o tema inteiro")]
    for j, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 180 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 56, "black", INK, a, align="left")


def b_material(c, t, C, B):
    frame(c, t, B["start"], "SEPARE AGORA", "FOLHA, CANETA E DUAS CORES", GREEN)
    itens = [("03.a", "folha", None), ("03.b", "caneta", PEN), ("03.d", "cor 1", BLUE), ("03.e", "cor 2", GREEN)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        x = 380 + k * 380
        if a <= 0:
            continue
        if col is None:
            paper(c, x - 110, 230 + d, 220, 280, a, lh=40, top=270 + d, margin=False)
        else:
            pen_draw(c, x - 40, 420 + d, col, a, -35, 1.6)
        text(c, s, x, 610 + d, 40, "black", col or INK2, a)
    text(c, "NÚCLEO", 1140, 690, 30, "black", BLUE, ep(t, C["03.d"], 0.4))
    text(c, "a palavra central do tema", 1140, 730, 22, "bold", INK2, ep(t, C["03.d"], 0.4))
    text(c, "DELIMITADORES", 1520, 690, 30, "black", GREEN, ep(t, C["03.e"], 0.4))
    text(c, "as partes que fecham o recorte", 1520, 730, 22, "bold", INK2, ep(t, C["03.e"], 0.4))
    pill(c, "pegou? então vamos", 520, 780, GREEN, size=28, a=ep(t, C["03.f"], 0.4), anchor="center", bounds=(0, 1920))


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "O QUE VOCÊ JÁ SABE", "EM 45 SEGUNDOS", BLUE)
    cards = [("04.a", "EP. 2", "a frase temática em BLOCOS", "cada bloco, uma exigência", BLUE),
             ("04.b", "EP. 2", "o tema vira PERGUNTA-PROBLEMA", "", BLUE),
             ("04.c", "EP. 3", "motivadores são GPS", "ajudam a chegar, não fazem a entrega", GREEN),
             ("04.d", "EP. 4", "esquecer um bloco = TANGENCIAR", "bairro certo, casa errada", AMBER)]
    for k, (cue, ep_, s1, s2, col) in enumerate(cards):
        a, d = rise(t, C[cue])
        x = 220 + (k % 2) * 760
        y = 210 + (k // 2) * 300 + d
        rrect(c, x, y, 720, 250, 20, mix("#FFFFFF", col, 0.07), a, shadow=True)
        pill(c, ep_, x + 30, y + 44, col, size=22, a=a, bounds=(0, 1920))
        para(c, s1, x + 30, y + 130, 40, "black", INK, a, 660, 46)
        text(c, s2, x + 30, y + 215, 26, "bold", INK2, a, align="left")


# ======================================================================
# checklist do piloto e a tabela dos 6 passos
# ======================================================================

def prancheta(c, x, y, a, itens, alphas, titulo):
    rrect(c, x, y, 460, 520, 18, "#C8955C", a, shadow=True)
    rrect(c, x + 160, y - 18, 140, 44, 10, "#8E8E93", a)
    rrect(c, x + 30, y + 40, 400, 450, 10, "#FFFFFF", a)
    text(c, titulo, x + 230, y + 100, 26, "black", GRAY, a, tracking=2)
    for k, (s, al) in enumerate(zip(itens, alphas)):
        yy = y + 180 + k * 90
        rrect(c, x + 70, yy - 30, 40, 40, 8, "#FFFFFF", a, stroke=3, stroke_color=INK2)
        check_icon(c, x + 90, yy - 10, 26, al * a, GREEN)
        text(c, s, x + 140, yy, 38, "black", INK, a, align="left")


def b_piloto(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE SAIR DE CASA", "VOCÊ CONFERE O QUÊ?", GREEN)
    a0 = ep(t, C["05.t"], 0.5)
    prancheta(c, 260, 230, a0, ["chave", "carteira", "celular"],
              [ep(t, C["05.a"], 0.3), ep(t, C["05.b"], 0.3), ep(t, C["05.c"], 0.3)], "ANTES DE SAIR")
    ad = ep(t, C["05.d"], 0.5)
    text(c, "O PILOTO", 1240, 300, 30, "black", GRAY, ad, tracking=3)
    text(c, "ninguém decola", 1240, 390, 60, "black", INK, ad)
    text(c, "sem conferir", 1240, 460, 60, "black", GREEN, ad)
    ae = ep(t, C["05.e"], 0.5)
    pill(c, "6 PASSOS = o seu CHECKLIST (lista de conferência)", 1240, 580, GREEN, size=26, a=ae, anchor="center", bounds=(0, 1920))
    pill(c, "sugestão de método · não é regra da prova", 1240, 680, PURPLE, size=24, a=ep(t, C["05.f"], 0.4), anchor="center",
         bounds=(0, 1920))


ROW_CUES = [("07.a", "07.a2"), ("07.b", "07.b2"), ("08.c", "08.c2"), ("08.d", "08.d2"), ("09.e", "09.e2"), ("09.f", "09.f2")]


def b_passos(c, t, C, B):
    head(c, t, B["start"], "OS 6 PASSOS", "CADA UM COM A SUA PERGUNTA DE CONTROLE", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["06.t"], 0.5)
    text(c, "PASSO", 270, 205, 18, "black", GRAY, a0, align="left", tracking=2)
    text(c, "O QUE FAZER", 640, 205, 18, "black", GRAY, a0, align="left", tracking=2)
    text(c, "PERGUNTA DE CONTROLE", 1190, 205, 18, "black", GREEN, a0, align="left", tracking=2)
    sid = which(t, C, ["06", "07", "08", "09"])
    if sid == "06":
        boxed(c, 300, 330, 1320, 170, GREEN, ep(t, C["06.t"], 0.5), 0.07)
        text(c, "PERGUNTA DE CONTROLE", W / 2, 395, 34, "black", GREEN, a0)
        text(c, "a pergunta que você faz a si mesmo para saber se o passo deu certo", W / 2, 455, 30, "bold", INK2, a0)
        pill(c, "dividir o tempo da prova: série própria", W / 2, 620, PURPLE, size=26, a=ep(t, C["06.g"], 0.4), anchor="center")
        return
    for k, ((nm, fazer, ctrl), (ca, cb)) in enumerate(zip(PASSOS, ROW_CUES)):
        a, d = rise(t, C[ca])
        if a <= 0:
            continue
        y = 270 + k * 88 + d
        badge_num(c, k + 1, 220, y - 10, a, 24, bg=GREEN)
        text(c, nm, 270, y, 28, "black", INK, a, align="left")
        para(c, fazer, 640, y - 10, 22, "bold", INK2, a, 520, 26)
        b = ep(t, C[cb], 0.4)
        rrect(c, 1170, y - 40, 450, 66, 12, mix("#FFFFFF", GREEN, 0.10), b)
        para(c, ctrl, 1190, y - 12, 22, "black", GREEN, b, 420, 26)
    if sid == "09":
        pill(c, "TESE PROVISÓRIA = a 1ª versão, que ainda pode mudar", 620, 818, BLUE, size=20,
             a=ep(t, C["09.e3"], 0.4) * (1 - ep(t, C["09.f"], 0.3)), anchor="center", bounds=(0, 1920))
        pill(c, "EIXO = um caminho que o desenvolvimento vai seguir", 1240, 818, BLUE, size=20,
             a=ep(t, C["09.e4"], 0.4) * (1 - ep(t, C["09.f"], 0.3)), anchor="center", bounds=(0, 1920))


# ======================================================================
# EU FAÇO — passos 1 a 4 no rascunho
# ======================================================================

def b_p1(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · ENEM 2021", "PASSO 1: COPIAR A FRASE", GREEN)
    checklist(c, 0, ep(t, C["10.t"], 0.4), feitos=1 if t >= C["10.c"] + 1.5 else 0)
    rascunho(c, ep(t, C["10.t"], 0.4))
    text(c, "ENEM 2021", MX + 110, MY + 50, 20, "black", GRAY, ep(t, C["10.a"], 0.4), align="left", tracking=2)
    sp = hspan("10", TEMA21, C, 4)
    frase_rascunho(c, t, C, 1.0, wreveal(t, sp), under=False)
    ac = ep(t, C["10.c"], 0.4)
    check_icon(c, MX + MW - 120, MY + 230, 30, ac, GREEN)
    text(c, "sei dizer o tema com as palavras da prova", MX + MW - 170, MY + 240, 24, "black", GREEN, ac, align="right")


NOTAS = [("11.a2", "11", "registro civil", "a certidão de nascimento e a documentação básica", NUC, "núcleo"),
         ("12.b2", "12", "invisibilidade", "pessoas que, sem registro, não existem para o Estado", DEL, "delimitador (problema)"),
         ("12.c2", "12", "garantia de acesso à cidadania", "o registro como porta de entrada para direitos: escola, saúde, benefícios, voto",
          DEL, "delimitador (relação)"),
         ("13.d2", "13", "no Brasil", "a realidade brasileira, e não a de outros países", DEL, "delimitador (lugar)")]


def b_p2(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · ENEM 2021", "PASSO 2: OS BLOCOS", GREEN)
    checklist(c, 1, 1.0)
    rascunho(c)
    frase_rascunho(c, t, C)
    y = MY + 300
    for cue, sid, bl, obr, col, tipo in NOTAS:
        a = ep(t, C[cue], 0.3)
        if a <= 0:
            y += 100
            continue
        text(c, bl, MX + 110, y, 26, "black", col, a, align="left")
        text(c, tipo, MX + 110, y + 30, 16, "bold", GRAY, a, align="left")
        n = hand_para(c, "→ " + obr, MX + 520, y, 28, PEN, 1.0, MW - 600, 40, wreveal(t, (C[cue], C[cue] + 2.6)))
        y += max(2, n) * 40 + 24
    ad = ep(t, C["11.a3"], 0.4) * (1 - ep(t, C["12"], 0.3))
    pill(c, "CERTIDÃO DE NASCIMENTO = prova que você nasceu, e quem você é", MX + MW / 2, MY + MH - 120, BLUE, size=22, a=ad,
         anchor="center", bounds=(0, 1920))
    pill(c, "CARTÓRIO = lugar oficial onde o nascimento é registrado", MX + MW / 2, MY + MH - 60, BLUE, size=22,
         a=ep(t, C["11.a4"], 0.4) * (1 - ep(t, C["12"], 0.3)), anchor="center", bounds=(0, 1920))
    pill(c, "4 blocos = 4 exigências", MX + MW - 220, MY + MH - 60, GREEN, size=26, a=ep(t, C["13.e"], 0.4), anchor="center",
         bounds=(0, 1920))


def b_p3(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · ENEM 2021", "PASSO 3: OS MOTIVADORES", GREEN)
    checklist(c, 2, 1.0)
    rascunho(c)
    frase_rascunho(c, t, C)
    aa = ep(t, C["14.a"], 0.5)
    for k, s in enumerate(("1. observar posição e situação-problema", "2. ponto de vista e argumentos", "3. refletir e definir a SUA posição")):
        hand(c, s, MX + 120, MY + 320 + k * 56, 30, PEN, aa * ep(t, C["14.a"] + 0.5 * k, 0.4))
    text(c, "os 3 passos da Cartilha (ep. 3)", MX + 120, MY + 270, 20, "black", PURPLE, aa, align="left", tracking=1)
    ab = ep(t, C["14.b"], 0.5)
    boxed(c, MX + 760, MY + 290, 560, 140, GREEN, ab, 0.07)
    text(c, "qual é a", MX + 1040, MY + 345, 30, "bold", INK2, ab)
    text(c, "SITUAÇÃO-PROBLEMA?", MX + 1040, MY + 395, 38, "black", GREEN, ab)
    pill(c, "os textos de 2021 não estão no nosso material → passo 4", MX + MW / 2, MY + MH - 80, AMBER, size=24,
         a=ep(t, C["14.c"], 0.4), anchor="center", bounds=(0, 1920))


def b_p4(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · ENEM 2021", "PASSO 4: A PERGUNTA-PROBLEMA", GREEN)
    checklist(c, 3, 1.0)
    rascunho(c)
    frase_rascunho(c, t, C)
    text(c, "PERGUNTA", MX + 110, MY + 290, 20, "black", BLUE, ep(t, C["15.a"], 0.4), align="left", tracking=2)
    n = hand_para(c, PERGUNTA, MX + 110, MY + 350, 36, PEN, 1.0, MW - 180, 56, wreveal(t, hspan("15", PERGUNTA, C, 6)))
    for k, (cue, s, col) in enumerate((("15.b2", "registro civil", NUC), ("15.b3", "invisibilidade", DEL),
                                       ("15.b4", "cidadania", DEL), ("15.b5", "Brasil", DEL))):
        a = ep(t, C[cue], 0.3)
        x = MX + 140 + k * 320
        y = MY + MH - 110
        rrect(c, x, y - 34, 290, 68, 14, mix("#FFFFFF", col, 0.12), a)
        check_icon(c, x + 36, y, 20, a, GREEN)
        text(c, s, x + 66, y + 10, 26, "black", INK, a, align="left")


# ======================================================================
# EU FAÇO — tese provisória e conferência
# ======================================================================

def b_p5(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · ENEM 2021", "PASSO 5: A TESE PROVISÓRIA", GREEN)
    checklist(c, 4, 1.0)
    rascunho(c)
    frase_rascunho(c, t, C)
    pill(c, "TENTATIVA 1", MX + 110, MY + 290, AMBER, size=22, a=ep(t, C["16.a"], 0.4), bounds=(0, 1920))
    hand_para(c, TENTATIVA, MX + 110, MY + 360, 34, PEN, 1.0, MW - 180, 56, wreveal(t, hspan("16", TENTATIVA, C, 7)))
    ab = ep(t, C["16.b"], 0.4)
    check_icon(c, MX + 140, MY + MH - 90, 24, ab, GREEN)
    text(c, "alguém poderia discordar? sim: tem posição", MX + 180, MY + MH - 80, 28, "black", GREEN, ab, align="left")
    pill(c, "parece boa, né?", MX + MW - 220, MY + MH - 90, AMBER, size=28, a=ep(t, C["16.c"], 0.4), anchor="center", bounds=(0, 1920))


def pecas21(c, t, C, y, marks=None):
    """as 4 peças da frase de 2021 na área principal, com ✓/✗ embaixo"""
    c.save(); c.translate(DX, 0)
    puzzle(c, t, C, T21, y, 1.0, 26, None, obriga=False)
    if marks:
        for cx, (a, ok) in zip(centros(T21, 26), marks):
            check_icon(c, cx, y + 120, 28, a, GREEN if ok else RED, "check" if ok else "x")
    c.restore()


def b_p6(c, t, C, B):
    sid = which(t, C, ["17", "18", "19"])
    head_seq(c, t, C, [("17", "PASSO 6", "A CONFERÊNCIA", GREEN), ("18", "PASSO 6", "CORRIGINDO NO RASCUNHO", GREEN),
                       ("19", "PASSO 6", "CONFERE DE NOVO", GREEN)])
    checklist(c, 5, 1.0, feitos=6 if t >= C["19.e"] else 5)
    rascunho(c)
    text(c, "FRASE TEMÁTICA", MX + MW / 2, MY + 60, 18, "black", BLUE, 1.0, tracking=2)
    if sid == "17":
        marks = [(ep(t, C["17.c"], 0.3), True), (ep(t, C["17.b"], 0.3), True), (ep(t, C["17.d"], 0.3), True),
                 (ep(t, C["17.e"] + 0.8, 0.3), False)]
    else:
        al = ep(t, C["19.t"], 0.3) if sid == "19" else 0
        marks = [(al, True)] * 4
    pecas21(c, t, C, MY + 110, marks)
    yt = MY + 340
    if sid == "17":
        pill(c, "TENTATIVA 1", MX + 110, yt - 40, AMBER, size=20, a=1.0, bounds=(0, 1920))
        hand_para(c, TENTATIVA, MX + 110, yt + 20, 32, PEN, ep(t, C["17.a"], 0.4), MW - 180, 52)
        af = ep(t, C["17.f"], 0.4)
        pill(c, "esqueceu um bloco → caminho do TANGENCIAMENTO", MX + MW / 2, MY + MH - 70, AMBER, size=26, a=af,
             anchor="center", bounds=(0, 1920))
        return
    if sid == "19":
        pill(c, "TESE", MX + 110, yt - 40, GREEN, size=20, a=1.0, bounds=(0, 1920))
        hand_para(c, TESE, MX + 110, yt + 20, 30, PEN, 1.0, MW - 180, 48)
        ab = ep(t, C["19.b"], 0.4)
        text(c, "2 EIXOS:", MX + 120, MY + MH - 50, 24, "black", GREEN, ab, align="left", tracking=2)
        pill(c, "distância", MX + 290, MY + MH - 58, GREEN, size=24, a=ep(t, C["19.c"], 0.3), bounds=(0, 1920))
        pill(c, "desinformação", MX + 470, MY + MH - 58, GREEN, size=24, a=ep(t, C["19.d"], 0.3), bounds=(0, 1920))
        selo(c, MX + MW - 260, MY + MH - 70, ep(t, C["19.e"], 0.4), "ENDEREÇO COMPLETO", GREEN, -5, 30)
        return
    # tentativa riscada, tese corrigida embaixo
    pill(c, "TENTATIVA 1", MX + 110, yt - 40, LIGHT, size=18, a=1.0, bounds=(0, 1920))
    lines = hwrap(TENTATIVA, 22, MW - 180)
    for k, ln in enumerate(lines):
        hand(c, ln, MX + 110, yt + k * 32, 22, GRAY, 0.8)
        strike(c, MX + 106, yt + k * 32 - 7, MX + 114 + hand_w(ln, 22), yt + k * 32 - 7, 0.8, RED)
    yy = yt + len(lines) * 32 + 40
    pill(c, "TESE CORRIGIDA", MX + 110, yy, GREEN, size=20, a=ep(t, C["18.t"], 0.4), bounds=(0, 1920))
    sp = hspan("18", TESE, C, 12)
    if sid == "18":
        hand_para(c, TESE, MX + 110, yy + 60, 30, PEN, 1.0, MW - 180, 48, wreveal(t, sp))
        return
    # 19: quatro blocos + dois eixos
    hand_para(c, TESE, MX + 110, yy + 60, 30, PEN, 1.0, MW - 180, 48)
    ab = ep(t, C["19.b"], 0.4)
    text(c, "2 EIXOS:", MX + 120, MY + MH - 50, 24, "black", GREEN, ab, align="left", tracking=2)
    pill(c, "distância", MX + 290, MY + MH - 58, GREEN, size=24, a=ep(t, C["19.c"], 0.3), bounds=(0, 1920))
    pill(c, "desinformação", MX + 470, MY + MH - 58, GREEN, size=24, a=ep(t, C["19.d"], 0.3), bounds=(0, 1920))
    selo(c, MX + MW - 260, MY + MH - 70, ep(t, C["19.e"], 0.4), "ENDEREÇO COMPLETO", GREEN, -5, 30)


def b_repertorio(c, t, C, B):
    head(c, t, B["start"], "PARA O SEGUNDO EIXO", "UM REPERTÓRIO DO MATERIAL", PURPLE)
    checklist(c, None, 1.0, feitos=6)
    card(c, MX, MY, MW, MH)
    a0 = ep(t, C["20.t"], 0.5)
    text(c, "REPERTÓRIO", MX + MW / 2, MY + 90, 44, "black", BLUE, a0)
    text(c, "informação de fora da prova que você leva para o texto", MX + MW / 2, MY + 145, 28, "bold", INK2, a0)
    aa = ep(t, C["20.a"], 0.5)
    boxed(c, MX + 120, MY + 220, 700, 260, PURPLE, aa, 0.07)
    text(c, "Lei nº 9.534/1997", MX + 470, MY + 300, 50, "black", PURPLE, aa)
    para(c, "tornou gratuitos o registro civil de nascimento e a primeira certidão", MX + 470, MY + 370, 28, "black", INK,
         ep(t, C["20.b"], 0.4), 600, 34, align="center")
    arrow(c, MX + 840, MY + 350, MX + 960, MY + 350, GREEN, aa, 5, 16)
    rrect(c, MX + 980, MY + 260, 330, 180, 18, mix("#FFFFFF", GREEN, 0.10), aa)
    text(c, "EIXO 2", MX + 1145, MY + 310, 20, "black", GREEN, aa, tracking=2)
    para(c, "desinformação sobre a gratuidade do registro", MX + 1145, MY + 360, 26, "black", INK, aa, 290, 30, align="center")
    pill(c, "de fora da prova · ligada diretamente ao recorte", MX + MW / 2, MY + 580, GREEN, size=28, a=ep(t, C["20.c"], 0.4),
         anchor="center", bounds=(0, 1920))


# ======================================================================
# contraexemplo, dica
# ======================================================================

def b_lado(c, t, C, B):
    head_seq(c, t, C, [("21", "COMO NÃO COMEÇAR", "LEITURA QUE TANGENCIA", AMBER), ("22", "LADO A LADO", "TANGENCIA × COMPLETA", AMBER)])
    card(c, *CARD_R)
    ab = ep(t, C["21.b"], 0.5)
    rrect(c, 200, 200, 740, 470, 20, mix("#FFFFFF", AMBER, 0.08), ab, shadow=True)
    pill(c, "LEITURA QUE TANGENCIA", 240, 245, AMBER, size=22, a=ab, bounds=(0, 1920))
    hand_para(c, TANG, 240, 330, 32, PEN, 1.0, 660, 50, wreveal(t, hspan("21", TANG, C, 6)))
    text(c, "Trecho elaborado para fins didáticos.", 240, 650, 16, "medium", GRAY, ab, align="left")
    a2 = ep(t, C["22"], 0.5)
    rrect(c, 980, 200, 740, 470, 20, mix("#FFFFFF", GREEN, 0.07), a2, shadow=True)
    pill(c, "LEITURA COMPLETA", 1020, 245, GREEN, size=22, a=a2, bounds=(0, 1920))
    hand_para(c, TESE, 1020, 320, 25, PEN, a2, 660, 38)
    pill(c, "parece um começo bonito...", 570, 720, AMBER, size=24, a=ep(t, C["22.a"], 0.4) * (1 - ep(t, C["22.b"], 0.3)),
         anchor="center", bounds=(0, 1920))
    pill(c, "assunto amplo: cidadania em geral", 570, 720, AMBER, size=24, a=ep(t, C["22.b"], 0.4), anchor="center", bounds=(0, 1920))
    for k, s in enumerate(("registro civil", "invisibilidade", "Brasil")):
        a = ep(t, C["22.c"] + 0.5 * k, 0.3)
        x = 230 + k * 240
        check_icon(c, x, 790, 20, a, RED, "x")
        text(c, s, x + 30, 800, 24, "black", RED, a, align="left")
    pill(c, "risco REAL de tangenciamento", 1350, 760, RED, size=28, a=ep(t, C["22.d"], 0.4), anchor="center", bounds=(0, 1920))


def b_dica(c, t, C, B):
    head_seq(c, t, C, [("23", "TEMA DIFÍCIL?", "OS MOTIVADORES AJUDAM", GREEN), ("24", "E REPARE", "A TESE ABRE A INTRODUÇÃO", BLUE)])
    card(c, *CARD_R)
    if t < C["24"] - 0.05:
        aa = ep(t, C["23.a"], 0.5)
        boxed(c, 260, 210, 1400, 130, PURPLE, aa, 0.07)
        text(c, "A CARTILHA OBSERVA", 300, 252, 18, "black", PURPLE, aa, align="left", tracking=2)
        text(c, "os motivadores podem ser de grande ajuda quando o tema é pouco familiar", 300, 305, 32, "black", INK, aa, align="left")
        ab = ep(t, C["23.b"], 0.5)
        badge_num(c, 1, 300, 420, ab, 26, bg=GREEN)
        text(c, "descubra qual é o PROBLEMA e quais aspectos estão em jogo", 350, 432, 32, "black", INK, ab, align="left")
        ac = ep(t, C["23.c"], 0.5)
        badge_num(c, 2, 300, 520, ac, 26, bg=GREEN)
        text(c, "procure no que você já estudou", 350, 532, 32, "black", INK, ac, align="left")
        for k, s in enumerate(("História", "Geografia", "Sociologia", "Literatura", "notícias")):
            pill(c, s, 360 + k * 250, 640, GREEN, size=28, a=ep(t, C["23.d"] + 0.4 * k, 0.3), bounds=(0, 1920))
        text(c, "algo que se ligue a esses aspectos", 360, 740, 28, "bold", INK2, ep(t, C["23.d"] + 2.4, 0.4), align="left")
        return
    aa = ep(t, C["24.a"], 0.5)
    rrect(c, 300, 300, 560, 240, 20, mix("#FFFFFF", GREEN, 0.08), aa, shadow=True)
    text(c, "TESE", 580, 400, 54, "black", GREEN, aa)
    text(c, "que cobre o recorte", 580, 460, 28, "bold", INK2, aa)
    arrow(c, 900, 420, 1060, 420, BLUE, aa, 6, 20, progress=aa)
    rrect(c, 1080, 300, 560, 240, 20, mix("#FFFFFF", BLUE, 0.08), aa, shadow=True)
    text(c, "INTRODUÇÃO", 1360, 400, 50, "black", BLUE, aa)
    text(c, "o próximo assunto da série", 1360, 460, 28, "bold", INK2, aa)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Blocos, pergunta, tese, conferência.", "Tese = posição + dois eixos + todos os blocos.",
          "Confira antes de desenvolver, não depois."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["25", "38"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "25" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 50, "black", INK, a, align="left")


ERROS = [("35", "Pular a conferência porque a tese “parece boa”", "você está com pressa e a frase soa bem", "foi assim que a tentativa 1 esqueceu o Brasil: CONFIRA"),
         ("36", "Tese que repete o tema ou o anuncia: “Este texto vai discutir…”", "usa todas as palavras da prova", "não diz o que você defende: TOME POSIÇÃO"),
         ("37", "Começar a redação pelo assunto amplo", "contextualizar soa inteligente", "sai do recorte na 1ª linha: COMECE PELO TEMA")]


def b_erros(c, t, C, B):
    V4.ERROS = ERROS
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(3):
        badge_num(c, k + 1, 880 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 330, 34, aa, RED, "x")
    para(c, err, 360, 345, 42, "black", RED, aa, 1300)
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 500, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 580, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 698, 34, ac, GREEN)
    para(c, fix, 360, 714, 38, "black", GREEN, ac, 1300)


# ======================================================================
# questões 9 (nós fazemos) e 8 (você faz)
# ======================================================================

ALT9 = [("A", "A invisibilidade e o registro civil são questões relacionadas à garantia de acesso à cidadania no Brasil.", "27.a", "29.xa", "reescreve a frase: nada discutível", RED),
        ("B", "Sem certidão de nascimento, parte dos brasileiros fica invisível para o Estado e perde acesso a direitos básicos, situação mantida pela distância dos cartórios e pela desinformação sobre a gratuidade do registro.", "27.b", None, "", GREEN),
        ("C", "O registro civil é um assunto que merece a atenção de toda a sociedade brasileira.", "27.c", "29.xc", "importância, não posição", RED),
        ("D", "Muitas pessoas falam sobre invisibilidade e registro civil, e é preciso refletir sobre o tema.", "28.d", "29.xd", "genérica: adia a reflexão", RED),
        ("E", "Este texto vai discutir a invisibilidade e o registro civil como garantia de acesso à cidadania no Brasil.", "28.e", "29.xe", "anuncia, não defende", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "NÓS FAZEMOS · QUESTÃO 9", "DA FRASE TEMÁTICA À TESE", BLUE)
    checklist(c, 4, 1.0, ctrl_a=1.0)
    card(c, MX, MY, MW, MH)
    a = ep(t, C["26.a"], 0.5)
    alt_on = ep(t, C["27"], 0.5)
    if alt_on < 1:
        para(c, "Para o tema do Enem 2021, “" + TEMA21 + "”, a frase que deixa de apenas repetir o tema e apresenta uma tese é:",
             MX + 60, MY + 120, 40, "black", INK, a * (1 - alt_on), MW - 120, 52)
    if alt_on > 0:
        alts_panel(c, t, C, ALT9, MX + 60, MY + 70, MW - 120, 23, "29.fim", "B", 6)
        pause_timer(c, t, C["28.end"] - 1.9, MX + MW - 90, MY + MH - 90)
        ao = ep(t, C["29.ok"], 0.4)
        pill(c, "posição contestável + causas que o desenvolvimento pode sustentar", MX + MW / 2, MY + MH - 40, GREEN, size=22,
             a=ao, anchor="center", bounds=(0, 1920))
    text(c, "Questão do material de estudo (seção 12)", MX, MY + MH + 22, 16, "medium", GRAY, a, align="left")


ALT8 = [("A", "As doenças mentais afetam milhões de pessoas no mundo e exigem mais pesquisas científicas.", "31.a", "33.xa", "sem estigma e fora do Brasil", RED),
        ("B", "O Sistema Único de Saúde precisa ampliar a oferta de medicamentos para todas as doenças crônicas.", "31.b", "33.xb", "troca o estigma por remédios", RED),
        ("C", "No Brasil, a associação entre transtorno mental e fraqueza ou perigo afasta as pessoas do tratamento, preconceito que é reforçado pela desinformação e por representações estereotipadas na mídia.", "32.c", None, "", GREEN),
        ("D", "O estigma associado às doenças mentais na sociedade brasileira é um tema muito importante que deve ser discutido por todos.", "32.d", "33.xd", "só repete: sem posição nem eixos", RED),
        ("E", "Os transtornos mentais têm causas genéticas e ambientais, estudadas pela psiquiatria desde o século XIX.", "32.e", "33.xe", "ângulo científico: assunto amplo", RED)]
T20 = [("O estigma", DEL, "PROBLEMA", None, "30.a"), ("associado às doenças mentais", NUC, "NÚCLEO", None, "30.a"),
       ("na sociedade brasileira", DEL, "LUGAR", None, "30.a")]


def b_q8(c, t, C, B):
    sid = which(t, C, ["30", "31", "32", "33", "34"])
    head(c, t, B["start"], "VOCÊ FAZ · QUESTÃO 8", "A TESE QUE COBRE O RECORTE", BLUE)
    if sid == "30":
        card(c, *CARD_R)
        aa = ep(t, C["30.a"], 0.5)
        text(c, "ENEM 2020", W / 2, 230, 22, "black", GRAY, aa, tracking=2)
        text(c, "“" + TEMA20 + "”", W / 2, 300, 44, "black", BLUE, aa)
        puzzle(c, t, C, T20, 380, aa, 30, None, obriga=False)
        pill(c, "ESTIGMA = uma marca negativa que a sociedade cola numa pessoa", W / 2, 540, BLUE, size=26,
             a=ep(t, C["30.b"], 0.4), anchor="center")
        ac = ep(t, C["30.c"], 0.4)
        paper(c, 360, 600, 1000, 220, ac, lh=50, top=640)
        hand(c, "Minha tese: ____________________", 460, 700, 32, PEN, ac)
        hand(c, "eixo 1: ________   eixo 2: ________", 460, 770, 30, PEN, ac)
        pause_timer(c, t, C["30.end"] - 1.9, 1520, 700)
        return
    checklist(c, 5 if sid in ("33", "34") else 4, 1.0)
    card(c, MX, MY, MW, MH)
    text(c, "A tese que atende ao recorte completo desse tema é:", MX + 60, MY + 60, 26, "black", INK, ep(t, C["31.q"], 0.4),
         align="left")
    conf = ep(t, C["33"], 0.5)
    alts_panel(c, t, C, ALT8, MX + 60, MY + 120, MW - 520 if conf > 0 else MW - 120, 22, "34.fim", "C", 6)
    pause_timer(c, t, C["32.end"] - 1.9, MX + MW - 90, MY + MH - 90)
    if conf > 0:
        x0 = MX + MW - 420
        rrect(c, x0, MY + 90, 390, 560, 18, mix("#FFFFFF", GREEN, 0.06), conf)
        text(c, "CONFERÊNCIA DA C", x0 + 195, MY + 140, 20, "black", GREEN, conf, tracking=2)
        rows = [("estigma", "34.ok"), ("doenças mentais", "34.ok"), ("sociedade brasileira", "34.ok"), ("posição", "34.ok"),
                ("2 eixos: desinformação e mídia", "34.ok2")]
        for k, (s, cue) in enumerate(rows):
            a = ep(t, C[cue] + 0.6 * min(k, 3), 0.3) * conf
            y = MY + 210 + k * 80
            check_icon(c, x0 + 40, y, 20, a, GREEN)
            para(c, s, x0 + 72, y + 8, 24, "black", INK, a, 300, 28)
    text(c, "Questão do material de estudo (seção 12)", MX, MY + MH + 22, 16, "medium", GRAY, 1.0, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "ÚLTIMO EPISÓDIO DO ASSUNTO", "JUNTAMOS TUDO", PURPLE)
    rows = [("39.b", "juntamos tudo", GREEN), ("39.c", "caçamos as PEGADINHAS", AMBER), ("39.d", "DESAFIO: 5 temas reais", PURPLE)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 420, y - 16, a, 34, bg=col)
        text(c, s, 490, y, 56, "black", INK, a, align="left")


def b_cta(c, t, C, B):
    cta(c, t, C["40.like"], C["40.sub"], C["40.bell"], C["40.com"], C["40.bye"], "Qual foi a sua tese para o tema das doenças mentais?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, material=b_material, prereq=b_prereq, piloto=b_piloto, passos=b_passos,
              p1=b_p1, p2=b_p2, p3=b_p3, p4=b_p4, p5=b_p5, p6=b_p6, repertorio=b_repertorio, lado=b_lado, dica=b_dica,
              recap=b_recap, erros=b_erros, q9=b_q9, q8=b_q8, ponte=b_ponte, cta=b_cta)
