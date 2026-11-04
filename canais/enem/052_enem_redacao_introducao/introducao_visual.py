"""Visual compartilhado — Redação ENEM, série INTRODUÇÃO (052), tema claro.
Uso no roteiro/visual.py de cada episódio:
    import sys; from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from introducao_visual import *   # noqa
    usar_tempos(__file__)             # liga phrase_span/wreveal ao audio/tempos.json do episódio
Reaproveita a série Leitura da Proposta (014): V1 = ep1 (rascunho, caligrafia, etiqueta, caixa, caminhão, selo, pausa),
V2 = ep2 (alternativas, peças da frase temática), V4 = ep4 (placar, veredito).
Novo aqui: a ETIQUETA COMPLETA da encomenda com as 4 peças da introdução (MAPA · RUA DE ACESSO · ENDEREÇO + ENTREGA ·
LISTA DA CAIXA), os ícones das peças, recapitulação das 3 frases-chave, erros clássicos e CTA com flashcards (Anki).
Cores com função: azul = definição/tema · verde = dica/método · âmbar = armadilha · vermelho = erro/penalidade ·
roxo = regra oficial (Cartilha/edital). Cores das PEÇAS (sublinhados na folha de rascunho): MOV[...]
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

_BASE = Path(__file__).resolve().parent.parent / "014_enem_redacao_leitura_proposta"


def _load(nome, pasta):
    s = importlib.util.spec_from_file_location(nome, _BASE / pasta / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


V4 = _load("v014_ep4", "ep4_tangenciamento_fuga")
V2, V1 = V4.V2, V4.V1
motor.set_theme("claro")

paper, hand, hand_para, hwrap, hand_w = V1.paper, V1.hand, V1.hand_para, V1.hwrap, V1.hand_w
boxed, selo, pause_timer, which, para, wrap = V1.boxed, V1.selo, V1.pause_timer, V1.which, V1.para, V1.wrap
frame, head_seq, phrase_span, wreveal, underline = V1.frame, V1.head_seq, V1.phrase_span, V1.wreveal, V1.underline
regra, bubble, person, xmark = V1.regra, V1.bubble, V1.person, V1.xmark
caixa, etiqueta, truck, proposta_page, cartilha = V1.caixa, V1.etiqueta, V1.truck, V1.proposta_page, V1.cartilha
alts_panel, puzzle, seg_layout, draw_segs, pen_draw = V2.alts_panel, V2.puzzle, V2.seg_layout, V2.draw_segs, V2.pen_draw
placar, veredito, centros = V4.placar, V4.veredito, V4.centros
PEN, PAPER, KRAFT = V1.PEN, V1.PAPER, V1.KRAFT

MARCA = ""
CARD_R = (140, 150, 1640, 690)
DIDATICO = "Trecho elaborado para fins didáticos."
METODO = "método de estudo, não critério do Inep"

TEMA24 = "Desafios para a valorização da herança africana no Brasil"
TEMA25 = "Perspectivas acerca do envelhecimento na sociedade brasileira"
TEMA22 = "Desafios para a valorização de comunidades e povos tradicionais no Brasil"
TEMA21 = "Invisibilidade e registro civil: garantia de acesso à cidadania no Brasil"
TEMA20 = "O estigma associado às doenças mentais na sociedade brasileira"
TEMA17 = "Desafios para a formação educacional de surdos no Brasil"
TESE20 = ("No Brasil, o estigma associado às doenças mentais persiste em razão da desinformação sobre os transtornos e de "
          "representações midiáticas que associam o adoecimento psíquico à violência.")

# Versões da seção 07 (tema de 2024), EXATAMENTE como no material
V1_GEN = ("Desde os primórdios da humanidade, a cultura é fundamental para todos os povos. Nesse sentido, a herança africana "
          "também é importante e deve ser valorizada. Portanto, é necessário discutir esse tema.")
V2_BOLSO = ("Segundo Aristóteles, o homem é um animal político. Dessa forma, a valorização da herança africana no Brasil é um "
            "desafio que precisa ser enfrentado por toda a sociedade.")
V3_BOA = ["Sancionada em 2003, a Lei nº 10.639 tornou obrigatório o ensino de história e cultura afro-brasileira nas escolas "
          "do país, reconhecendo a contribuição africana na formação nacional.",
          "Mais de duas décadas depois, porém, essa herança ainda é frequentemente reduzida a estereótipos ou lembrada apenas "
          "em datas comemorativas.",
          "Esse quadro decorre, sobretudo, da aplicação irregular da lei nas escolas e da pouca visibilidade da cultura "
          "afro-brasileira nos meios de comunicação — obstáculos que precisam ser enfrentados para que essa herança seja, de "
          "fato, valorizada no Brasil."]


def usar_tempos(visual_file):
    """liga as funções de escrita sincronizada (phrase_span) ao tempos.json do episódio"""
    try:
        V1._SC = {s["id"]: s for s in json.load(open(Path(visual_file).resolve().parent.parent / "audio" / "tempos.json",
                                                     encoding="utf-8"))["scenes"]}
    except Exception:
        V1._SC = {}


# ======================================================================
# as 4 peças da etiqueta (analogia âncora da série)
# ======================================================================

MOV = dict(mapa=BLUE, rua=GREEN, tese="#D9480F", lista="#0E8C9A")
PECAS = [  # chave, nome na etiqueta, movimento, pergunta do leitor
    ("mapa", "MAPA", "contextualização", "de onde parte a discussão?"),
    ("rua", "RUA DE ACESSO", "ponte", "como a referência chega ao recorte?"),
    ("tese", "ENDEREÇO + ENTREGA", "tese", "o que o autor defende?"),
    ("lista", "LISTA DA CAIXA", "antecipação", "por quais caminhos vai provar?"),
]


def ic_mapa(c, cx, cy, s, a, col):
    p = skia.Path()
    xs = [-30, -10, 10, 30]
    p.moveTo(cx + xs[0] * s, cy - 18 * s)
    for k, x in enumerate(xs[1:]):
        p.lineTo(cx + x * s, cy + (-24 if k % 2 == 0 else -18) * s)
    p.lineTo(cx + 30 * s, cy + 24 * s)
    for k, x in enumerate(reversed(xs[:-1])):
        p.lineTo(cx + x * s, cy + (18 if k % 2 == 0 else 24) * s)
    p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.25), a))
    c.drawPath(p, paint(col, a, stroke=3 * s))
    for x in (-10, 10):
        line(c, cx + x * s, cy - 22 * s, cx + x * s, cy + 22 * s, col, a * 0.7, 2 * s)
    c.drawCircle(cx + 2 * s, cy - 4 * s, 6 * s, paint(RED, a))


def ic_rua(c, cx, cy, s, a, col):
    p = skia.Path()
    p.moveTo(cx - 34 * s, cy + 26 * s); p.lineTo(cx - 8 * s, cy - 26 * s); p.lineTo(cx + 8 * s, cy - 26 * s)
    p.lineTo(cx + 34 * s, cy + 26 * s); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.30), a))
    c.drawPath(p, paint(col, a, stroke=3 * s))
    for k in range(3):
        y0 = cy - 18 * s + k * 16 * s
        line(c, cx, y0, cx, y0 + 8 * s, col, a, 3.5 * s)


def ic_casa(c, cx, cy, s, a, col):
    p = skia.Path()
    p.moveTo(cx - 30 * s, cy - 2 * s); p.lineTo(cx, cy - 30 * s); p.lineTo(cx + 30 * s, cy - 2 * s); p.close()
    c.drawPath(p, paint(col, a))
    rrect(c, cx - 22 * s, cy - 4 * s, 44 * s, 32 * s, 3 * s, mix("#FFFFFF", col, 0.25), a, stroke=3 * s, stroke_color=col)
    rrect(c, cx - 6 * s, cy + 8 * s, 12 * s, 20 * s, 2 * s, col, a)


def ic_lista(c, cx, cy, s, a, col):
    rrect(c, cx - 30 * s, cy - 14 * s, 60 * s, 42 * s, 5 * s, KRAFT, a)
    rrect(c, cx - 34 * s, cy - 24 * s, 68 * s, 14 * s, 4 * s, mix(KRAFT, "#000000", 0.12), a)
    rrect(c, cx - 20 * s, cy - 6 * s, 40 * s, 28 * s, 3 * s, "#FFFFFF", a)
    for k in range(2):
        check_icon(c, cx - 12 * s, cy + 2 * s + k * 12 * s, 4 * s, a, col)
        line(c, cx - 4 * s, cy + 2 * s + k * 12 * s, cx + 14 * s, cy + 2 * s + k * 12 * s, col, a, 2.5 * s)


ICON_PECA = dict(mapa=ic_mapa, rua=ic_rua, tese=ic_casa, lista=ic_lista)


def icone_peca(c, key, cx, cy, a, s=1.0, lit=True, disc=True):
    if a <= 0:
        return
    col = MOV[key] if lit else LIGHT
    if disc:
        c.drawCircle(cx, cy, 46 * s, paint(mix("#FFFFFF", col, 0.14), a))
    ICON_PECA[key](c, cx, cy, s, a, col)


def etiqueta_intro(c, x, y, w, a, show=None, lit=None, ok=None, falta=None, perguntas=0.0, movs=1.0, keys=None, rowh=96,
                   title="ETIQUETA COMPLETA DA ENCOMENDA"):
    """etiqueta da introdução. keys = peças desenhadas (padrão: as 4; o ep. 1 usa ("mapa", "tese", "lista")).
    show[k] = alpha de cada faixa · lit[k] = destaque (0–1) · ok[k] = alpha do ✓ verde · falta[k] = alpha do ✗ vermelho
    perguntas = alpha das perguntas do leitor · movs = alpha do nome técnico (contextualização...). Retorna a altura."""
    if a <= 0:
        return 0
    keys = list(keys or [p[0] for p in PECAS])
    info = {p[0]: p for p in PECAS}
    n = len(keys)
    show = show or [1.0] * n
    lit = lit or [0.0] * n
    ok = ok or [0.0] * n
    falta = falta or [0.0] * n
    h = 96 + n * rowh + 24
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 10, y + 10, w - 20, h - 20), 12, 12), paint(LIGHT, a, stroke=2))
    bx = x + w - 230
    for k in range(28):
        c.drawRect(skia.Rect.MakeXYWH(bx + k * 6.5, y + 28, 3 if k % 3 else 6, 40), paint(INK, a * 0.85))
    text(c, title, x + 36, y + 62, 20, "black", GRAY, a, align="left", tracking=2)
    yy = y + 96
    for k, key in enumerate(keys):
        _, nome, mov, perg = info[key]
        col = MOV[key]
        ra = a * clamp(show[k])
        line(c, x + 26, yy, x + w - 26, yy, LINE, a, 2)
        if ra > 0:
            if lit[k] > 0:
                rrect(c, x + 16, yy + 6, w - 32, rowh - 12, 12, mix("#FFFFFF", col, 0.14), ra * lit[k])
            icone_peca(c, key, x + 70, yy + rowh / 2, ra, 0.62, disc=False)
            text(c, nome, x + 124, yy + rowh / 2 - 2 if perguntas <= 0 else yy + rowh / 2 - 12, 30, "black", col, ra,
                 align="left", tracking=1)
            if perguntas > 0:
                text(c, "“" + perg + "”", x + 124, yy + rowh / 2 + 24, 22, "bold", INK2, ra * perguntas, align="left")
            if movs > 0:
                pill(c, mov, x + w - 40 - (70 if (ok[k] > 0 or falta[k] > 0) else 0), yy + rowh / 2, col, size=20,
                     a=ra * movs, anchor="right", bounds=(0, 1920))
            if ok[k] > 0:
                check_icon(c, x + w - 62, yy + rowh / 2, 22, ra * ok[k], GREEN)
            if falta[k] > 0:
                check_icon(c, x + w - 62, yy + rowh / 2, 22, ra * falta[k], RED, "x")
        yy += rowh
    return h


def mini_etiqueta(c, cx, cy, a, oks, s=1.0, keys=None):
    """etiqueta em miniatura (4 faixas coloridas) — oks[k]: 1 = presente (verde), 0 = ausente (vermelho), None = neutro"""
    if a <= 0:
        return
    keys = list(keys or [p[0] for p in PECAS])
    w, rh = 300 * s, 34 * s
    h = 30 * s + len(keys) * rh + 10 * s
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, 10 * s, "#FFFFFF", a, shadow=True)
    for k in range(14):
        c.drawRect(skia.Rect.MakeXYWH(x + w - 80 * s + k * 4.6 * s, y + 8 * s, 2 * s, 16 * s), paint(INK, a * 0.8))
    for k, key in enumerate(keys):
        yy = y + 30 * s + k * rh
        o = oks[k] if k < len(oks) else None
        col = LIGHT if o is None else (GREEN if o else RED)
        rrect(c, x + 8 * s, yy + 3 * s, w - 16 * s, rh - 6 * s, 6 * s, mix("#FFFFFF", col, 0.18), a)
        ICON_PECA[key](c, x + 28 * s, yy + rh / 2, 0.32 * s, a, MOV[key])
        text(c, [p[1] for p in PECAS if p[0] == key][0], x + 50 * s, yy + rh / 2 + 7 * s, 15 * s, "black", INK2, a,
             align="left")
        if o is not None:
            check_icon(c, x + w - 24 * s, yy + rh / 2, 10 * s, a, col, "check" if o else "x")


# ======================================================================
# blocos-padrão (recapitulação, erros, CTA)
# ======================================================================

def recap(c, t, C, B, ids, frases, cols=None):
    """3 frases-chave; ids = (cena do meio, cena do fim); cues {a}{b}{c} em cada cena"""
    sid = which(t, C, list(ids))
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == ids[0] else "PARA FECHAR", PURPLE)
    for k, s in enumerate(frases):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        col = (cols or [PURPLE] * 3)[k]
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=col)
        para(c, s, 330, y, 46 if text_w(s, "black", 50) > 1300 else 50, "black", INK, a, 1340, 56)


def erros(c, t, C, B, lista):
    """lista = [(cena, erro, por que parece certo, correção)] — cues {a} erro · {b} parece · {c} correção"""
    ids = [e[0] for e in lista]
    sid = which(t, C, ids)
    n = ids.index(sid)
    _, err, parece, fix = lista[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE {len(lista)}", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(len(lista)):
        badge_num(c, k + 1, W / 2 - 40 * (len(lista) - 1) + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 330, 34, aa, RED, "x")
    para(c, err, 360, 345, 42, "black", RED, aa, 1300)
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 500, AMBER, size=26, a=ab, bounds=(0, 1920))
    para(c, parece, 300, 580, 36, "bold", INK2, ab, 1320, 44)
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 698, 34, ac, GREEN)
    para(c, fix, 360, 714, 38, "black", GREEN, ac, 1300)


def cta_intro(c, t, C, sid, pergunta):
    """CTA padrão com flashcards: cena com cues {like}{sub}{bell}{com}{anki}{bye}"""
    q = lambda x: C[f"{sid}.{x}"]
    cta(c, t, q("like"), q("sub"), q("bell"), q("com"), q("bye"), pergunta, canal="no Estudativo", anki=q("anki"))


def questao_rotulo(c, a, x=None, y=None, s="Questão do material de estudo (seção 12)"):
    text(c, s, x if x is not None else CARD_R[0], y if y is not None else CARD_R[1] + CARD_R[3] + 22, 16, "medium", GRAY, a,
         align="left")


def metodo_selo(c, x, y, a, rot=-4, size=24):
    """selo verde “MÉTODO, NÃO REGRA”"""
    selo(c, x, y, a, "MÉTODO, NÃO REGRA", GREEN, rot, size)
