"""Visual — Compreensão Global e Tese, Episódio 2: O resumo em uma frase (tema claro).
Analogia: o resumo é a MENSAGEM DE WHATSAPP para contar o texto a um amigo (balões de conversa).
Fórmula = três peças de quebra-cabeça que se encaixam: ASSUNTO (ciano) · O QUE O TEXTO AFIRMA (azul) · PORQUÊ (magenta);
cada pedaço do resumo ganha a cor da sua peça. Leituras com o texto inteiro na tela e marca-texto palavra a palavra.
Cores: azul = tese/definição · verde = palavra-sinal · âmbar = armadilha · vermelho = erro · roxo = fórmula/regra.
Peças de desenho reaproveitadas do ep. 1 (importado como V).
"""
import importlib.util
import json
import math
import re
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent.parent / "ep1_tema_assunto_tese" / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")

MARCA = ""
ARQUIVO_FINAL = "enem_linguagens_compreensao_ep2_resumo_uma_frase.mp4"
CARD_R = (140, 150, 1640, 690)
C_ASS, C_AFI, C_POR = "#0891B2", BLUE, "#DB2777"
PECAS = [("ASSUNTO", C_ASS), ("O QUE O TEXTO AFIRMA", C_AFI), ("O PORQUÊ", C_POR)]

wrap, para, which, frame, head_seq, boxed, regra, selo, pause_timer, bubble, folder = (
    V.wrap, V.para, V.which, V.frame, V.head_seq, V.boxed, V.regra, V.selo, V.pause_timer, V.bubble, V.folder)


# ======================================================================
# peças de quebra-cabeça
# ======================================================================

def piece_path(x, y, w, h, notch_l, bump_r, r=18, k=26):
    p = skia.Path()
    cy = y + h / 2
    p.moveTo(x + r, y)
    p.lineTo(x + w - r, y); p.quadTo(x + w, y, x + w, y + r)
    if bump_r:
        p.lineTo(x + w, cy - k)
        p.arcTo(skia.Rect.MakeXYWH(x + w - k, cy - k, 2 * k, 2 * k), -90, 180, False)
    p.lineTo(x + w, y + h - r); p.quadTo(x + w, y + h, x + w - r, y + h)
    p.lineTo(x + r, y + h); p.quadTo(x, y + h, x, y + h - r)
    if notch_l:
        p.lineTo(x, cy + k)
        p.arcTo(skia.Rect.MakeXYWH(x - k, cy - k, 2 * k, 2 * k), 90, -180, False)
    p.lineTo(x, y + r); p.quadTo(x, y, x + r, y)
    p.close()
    return p


def piece(c, x, y, w, h, col, a, label, sub="", notch_l=False, bump_r=False, size=30, fill=1.0):
    if a <= 0:
        return
    p = piece_path(x, y, w, h, notch_l, bump_r)
    c.save(); c.translate(0, 8)
    sp = paint("#000000", a * 0.10); sp.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawPath(p, sp); c.restore()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.14 + 0.86 * (1 - fill)), a))
    c.drawPath(p, paint(col, a, stroke=5))
    for j, ln in enumerate(label.split("\n")):
        text(c, ln, x + w / 2, y + h / 2 + 10 - (len(label.split("\n")) - 1) * 18 + j * 36 - (16 if sub else 0),
             size, "black", col, a)
    if sub:
        text(c, sub, x + w / 2, y + h / 2 + 40, 22, "bold", INK2, a)


def pieces_row(c, t, cues, y, w=440, h=150, gap=0.0, join=1.0, labels=None, subs=("", "", "")):
    """três peças lado a lado; join=1 encaixadas; cues = alfa de cada peça"""
    labels = labels or [p[0] for p in PECAS]
    total = 3 * w + 2 * lerp(80, 0, join)
    x = W / 2 - total / 2
    for k in range(3):
        a = cues[k]
        if a > 0:
            dy = (1 - a) * 30
            piece(c, x, y + dy, w, h, PECAS[k][1], a, labels[k].replace("O QUE O TEXTO AFIRMA", "O QUE O TEXTO\nAFIRMA"),
                  subs[k], notch_l=k > 0, bump_r=k < 2, size=28)
        x += w + lerp(80, 0, join)


def colored(c, segs, x, y, size, maxw, lh=None, peso="black", align="left"):
    """texto em segmentos coloridos com quebra de linha: segs = [(texto, cor, alfa)]"""
    lh = lh or size * 1.3
    words = []
    for s, col, a in segs:
        for w in s.split():
            words.append((w, col, a))
    lines, cur, cw = [], [], 0
    sp = text_w(" ", peso, size)
    for w, col, a in words:
        ww = text_w(w, peso, size)
        if cur and cw + sp + ww > maxw:
            lines.append((cur, cw)); cur, cw = [], 0
        cur.append((w, col, a, ww)); cw += (sp if len(cur) > 1 else 0) + ww
    if cur:
        lines.append((cur, cw))
    for j, (ln, lw) in enumerate(lines):
        xx = x - lw / 2 if align == "center" else x
        for w, col, a, ww in ln:
            if a > 0:
                text(c, w, xx, y + j * lh, size, peso, col, a, align="left")
            xx += ww + sp
    return len(lines) * lh


def wa_bubble(c, segs, x, y, w, a, size=34, out=True):
    """balão de WhatsApp com texto colorido; retorna a altura"""
    if a <= 0:
        return 0
    words = " ".join(s for s, _, _ in segs)
    n = len(wrap(words, "black", size, w - 60))
    h = n * size * 1.3 + 46
    col = "#DCF8C6" if out else "#FFFFFF"
    rrect(c, x, y, w, h, 24, col, a, shadow=True)
    p = skia.Path()
    if out:
        p.moveTo(x + w - 28, y + h - 2); p.lineTo(x + w + 2, y + h + 20); p.lineTo(x + w - 62, y + h - 2)
    else:
        p.moveTo(x + 28, y + h - 2); p.lineTo(x - 2, y + h + 20); p.lineTo(x + 62, y + h - 2)
    c.drawPath(p, paint(col, a))
    colored(c, [(s, cc, aa * a) for s, cc, aa in segs], x + 30, y + 24 + size * 0.95, size, w - 60)
    return h


def phone(c, x, y, w, h, a, title="Amigo"):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 46, "#1C1C1E", a, shadow=True)
    rrect(c, x + 18, y + 18, w - 36, h - 36, 34, "#ECE5DD", a)
    rrect(c, x + 18, y + 18, w - 36, 70, 0, "#075E54", a)
    c.drawCircle(x + 70, y + 53, 22, paint("#FFFFFF", a * 0.85))
    text(c, title, x + 108, y + 63, 28, "bold", "#FFFFFF", a, align="left")


# ======================================================================
# leitura com marca-texto (tempos.json deste episódio)
# ======================================================================

TEMPOS = HERE.parent / "audio" / "tempos.json"
try:
    _SC = {s["id"]: s for s in json.load(open(TEMPOS, encoding="utf-8"))["scenes"]}
except Exception:
    _SC = {}


def _norm(w):
    return re.sub(r"[^\wà-ú]", "", w.lower())


class Leitura:
    """sents = [(sid, cue_ini, cue_fim, texto)] · marks = [(i_frase, trecho, tipo, cor, cue)] tipo: fill/under/box"""

    def __init__(self, sents, marks):
        self.sents, self.marks, self._lay, self._t = sents, marks, {}, None
        self._mk = []
        for si, frag, kind, col, cue in marks:
            ws = [_norm(w) for w in sents[si][3].split()]
            fs = [_norm(w) for w in frag.split()]
            for i in range(len(ws) - len(fs) + 1):
                if ws[i:i + len(fs)] == fs:
                    self._mk.append((si, i, i + len(fs), kind, col, cue)); break
            else:
                raise ValueError("trecho não encontrado: " + frag)

    def times(self, C):
        if self._t is None:
            out = []
            for sid, c0, c1, s in self.sents:
                ws = s.split(); sc = _SC.get(sid); got = None
                if sc:
                    toks = sc["tokens"]; key = [_norm(w) for w in ws[:3]]
                    for i in range(len(toks) - 2):
                        if [_norm(toks[i + j]["disp"]) for j in range(3)] == key:
                            got = [sc["start"] + toks[min(i + j, len(toks) - 1)]["t0"] for j in range(len(ws))]; break
                out.append(got or [lerp(C[f"{sid}.{c0}"], C[f"{sid}.{c1}"], j / len(ws)) for j in range(len(ws))])
            self._t = out
        return self._t

    def layout(self, x, y, maxw, size, lh):
        key = (x, y, maxw, size, lh)
        if key not in self._lay:
            out, xx, yy = [], x, y
            sp = text_w(" ", "semibold", size)
            for si, (_, _, _, s) in enumerate(self.sents):
                for wi, w in enumerate(s.split()):
                    ww = text_w(w, "semibold", size)
                    if xx > x and xx + ww > x + maxw:
                        xx, yy = x, yy + lh
                    out.append((w, si, wi, xx, yy, ww)); xx += ww + sp
            self._lay[key] = out
        return self._lay[key]

    def draw(self, c, t, C, x, y, maxw, size, lh, a=1.0):
        if a <= 0:
            return
        T = self.times(C)
        for w, si, wi, xx, yy, ww in self.layout(x, y, maxw, size, lh):
            top, hh = yy - size * 0.86, size * 1.16
            said = ep(t, T[si][wi] - 0.05, 0.18)
            if said > 0:
                rrect(c, xx - 4, top, ww + 8, hh, 6, "#FFE58A", a * said * 0.55)
            col = INK
            for msi, i0, i1, kind, mcol, cue in self._mk:
                if msi == si and i0 <= wi < i1:
                    am = ep(t, C[cue], 0.35) if isinstance(cue, str) else ep(t, T[si][wi] - 0.05, 0.25)
                    if am <= 0:
                        continue
                    if kind == "fill":
                        rrect(c, xx - 4, top, ww + 8, hh, 6, mcol, a * am * 0.25)
                    elif kind == "under":
                        line(c, xx - 2, yy + 8, xx + ww + 6, yy + 8, mcol, a * am, 4)
                    elif kind == "strike":
                        line(c, xx - 4, yy - size * 0.32, xx + ww + 8, yy - size * 0.32, mcol, a * am, 4, progress=am)
                    elif kind == "box":
                        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx - 7, top - 3, ww + 14, hh + 6), 8, 8),
                                    paint(mcol, a * am, stroke=4))
                        col = mix(INK, mcol, am)
            text(c, w, xx, yy, size, "semibold", col, a, align="left")


def notas(c, t, C, rows, x, y0, dy, w=440, a=1.0):
    """rows = [(cue, título, texto, cor)]"""
    for k, (cue, tt, s, col) in enumerate(rows):
        al, d = rise(t, C[cue])
        al *= a
        y = y0 + k * dy + d
        if al > 0:
            rrect(c, x, y - 20, w, 84, 14, mix("#FFFFFF", col, 0.08), al)
            c.drawRect(skia.Rect.MakeXYWH(x, y - 20, 8, 84), paint(col, al))
            text(c, tt, x + 24, y + 12, 22, "black", col, al, align="left", tracking=1)
            text(c, s, x + 24, y + 48, 24, "bold", INK2, al, align="left")


HORTAS = Leitura(
    [("08", "f1", "c1", "Hortas em terrenos baldios costumam ser lembradas pela alface que produzem, mas o que elas cultivam de mais valioso é outra coisa."),
     ("09", "f2", "c2", "O terreno que juntava entulho passa a ter dono coletivo; vizinhos que não se cumprimentavam dividem ferramentas e turnos de rega; crianças aprendem de onde vem a comida."),
     ("09", "f3", "c3", "A colheita é o pretexto — o fruto é a vizinhança.")],
    [(0, "Hortas em terrenos baldios", "fill", C_ASS, "10.s1"),
     (0, "mas", "box", GREEN, None),
     (0, "alface", "under", AMBER, "08.c1b"),
     (1, "vizinhos que não se cumprimentavam dividem ferramentas", "under", C_POR, "10.s3"),
     (1, "crianças aprendem de onde vem a comida", "under", C_POR, "10.s3"),
     (2, "o fruto é a vizinhança", "fill", C_AFI, "09.c3")])

SONO = Leitura(
    [("21", "f1", "c1", "Na adolescência, o relógio biológico costuma se atrasar: o sono chega mais tarde e, com ele, a tendência de acordar mais tarde."),
     ("22", "f2", "c2", "A escola, porém, continua começando cedo."),
     ("22", "f3", "c3", "O resultado é uma privação de sono que muitos adultos interpretam como preguiça."),
     ("23", "f4", "c4", "Por isso, algumas redes de ensino em outros países testaram adiar o início das aulas, e pesquisadores acompanham os efeitos dessa mudança sobre a atenção e a frequência dos alunos.")],
    [(0, "Na adolescência, o relógio biológico", "fill", C_ASS, "21.c1b"),
     (1, "porém,", "box", GREEN, None),
     (2, "privação de sono", "fill", C_AFI, "24.s2"),
     (2, "muitos adultos interpretam como preguiça.", "under", AMBER, "22.c3b"),
     (3, "Por isso,", "box", GREEN, None),
     (3, "testaram adiar o início das aulas,", "fill", C_POR, "24.s3")])


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "LINGUAGENS ENEM", "O RESUMO EM UMA FRASE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    u = ep(t, C["01.a"] + 1.0, 1.6)
    for k in range(9):
        y = lerp(240 + k * 46, 460, u)
        w = lerp(820 - (k % 3) * 120, 900, u)
        line(c, 520, y, 520 + w, y, LINE, aa * (1 - u), 16)
    if u > 0.4:
        a2 = aa * (u - 0.4) / 0.6
        boxed(c, 480, 410, 980, 110, BLUE, a2, 0.08)
        text_mid(c, "1 FRASE", 970, 465, 54, "black", BLUE, a2)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "não consegue? ainda não entendeu o texto", W / 2, 620, 36, "black", RED, ab)
    ac = ep(t, C["01.c"], 0.5)
    pieces_row(c, t, [ac, ep(t, C["01.c"] + 0.3, 0.4), ep(t, C["01.c"] + 0.6, 0.4)], 680, 300, 110, join=1, labels=["", "", ""])
    pill(c, "existe uma FÓRMULA", W / 2, 735, PURPLE, size=30, a=ep(t, C["01.c"] + 1.0, 0.4), anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "resumir qualquer texto", "em UMA frase"), ("02.b", "achar a alternativa certa", "ANTES de ler as opções")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")
        text(c, sub, 400, y + 60, 36, "black", BLUE, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRA DO EPISÓDIO 1?", "ASSUNTO × TESE", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    folder(c, 300, 330, 460, 170, "celular na escola", aa)
    pill(c, "ASSUNTO = sobre o que FALA", 530, 590, INK2, size=30, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["03.b"], 0.5)
    pill(c, "TESE = o que DIZ (verbo + posição)", 1360, 590, BLUE, size=30, a=ab, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["03.c"], 0.5)
    boxed(c, 1010, 300, 700, 220, BLUE, max(ac, ab * 0.3), 0.08)
    if ac > 0:
        para(c, "“A escola deve ensinar a usar o celular.”", 1360, 395, 42, "black", BLUE, ac, 620, align="center")


# ======================================================================
# whatsapp e resumo
# ======================================================================

def b_whatsapp(c, t, C, B):
    head_seq(c, t, C, [("04", "CONTANDO UMA SÉRIE", "NO WHATSAPP", GREEN), ("05", "ISSO TEM NOME", "RESUMO", BLUE)])
    card(c, *CARD_R)
    a05 = ep(t, C["05"], 0.6)
    px = lerp(660, 220, a05)
    a0 = ep(t, C["04.t"], 0.5)
    phone(c, px, 170, 600, 660, a0)
    aa = ep(t, C["04.a"], 0.4)
    wa_bubble(c, [("E aí, é boa?", INK, 1)], px + 50, 290, 300, aa, 32, out=False)
    ab = fw(t, C["04.b"], C["04.c"] + 0.3)
    for j, s in enumerate(("cena 1...", "cena 2...", "cena 3...", "cena 47...")):
        text(c, s, px + 330, 440 + j * 50, 30, "bold", GRAY, ab, align="left")
    line(c, px + 320, 520, px + 520, 520, RED, ab, 6, progress=ep(t, C["04.b"] + 0.6, 0.4))
    ac = ep(t, C["04.c"], 0.4)
    wa_bubble(c, [("É sobre uma família, e vale a pena: prende do início ao fim.", INK, 1)], px + 160, 420, 380, ac, 30)
    # definição
    if a05 > 0:
        x0 = 900
        pill(c, "RESUMO", x0 + 380, 250, BLUE, size=44, a=a05, anchor="center", bounds=(0, 1920))
        text(c, "o texto inteiro em poucas palavras,", x0 + 380, 350, 34, "bold", INK, a05)
        text(c, "com as SUAS palavras", x0 + 380, 400, 34, "black", BLUE, a05)
        asb = ep(t, C["05.b"], 0.4)
        text(c, "= SÍNTESE (outro nome)", x0 + 380, 470, 32, "bold", GRAY, asb)
        ad = ep(t, C["05.d"], 0.4)
        for j, s in enumerate(("curta", "com suas palavras", "sem a sua opinião")):
            a = ad * ep(t, C["05.d"] + 0.7 * j, 0.3)
            check_icon(c, x0 + 130, 572 + j * 76, 24, a, GREEN)
            text(c, s, x0 + 175, 584 + j * 76, 36, "black", INK, a, align="left")


# ======================================================================
# bloco A — a fórmula
# ======================================================================

def b_formula(c, t, C, B):
    head_seq(c, t, C, [("06", "A FÓRMULA", "TRÊS PEÇAS", PURPLE), ("07", "A FÓRMULA", "NA MENSAGEM DA SÉRIE", PURPLE)])
    card(c, *CARD_R)
    a7 = ep(t, C["07.a"], 0.8)
    join = ep(t, C["06.e"] + 1.0, 0.8)
    y = lerp(330, 220, a7)
    pieces_row(c, t, [ep(t, C["06.b"], 0.5), ep(t, C["06.c"], 0.5), ep(t, C["06.d"], 0.5)], y, 470, 160, join=join,
               subs=("sobre o que fala", "a tese", "o motivo mais forte"))
    text(c, "(ou a PROPOSTA, se o texto sugere uma solução)", W / 2 + 470, y + 220, 26, "black", C_POR,
         ep(t, C["06.e"], 0.4) * (1 - a7), align="center")
    if a7 > 0:
        segs = [("a série da família Silva", C_ASS, ep(t, C["07.s1"], 0.4)),
                ("vale muito a pena,", C_AFI, ep(t, C["07.s2"], 0.4)),
                ("porque prende do primeiro ao último episódio.", C_POR, ep(t, C["07.s3"], 0.4))]
        wa_bubble(c, segs, 420, 470, 1080, a7, 42)
        pill(c, "3 peças = 1 frase", W / 2, 780, PURPLE, size=32, a=ep(t, C["07.b"], 0.4), anchor="center")


# ======================================================================
# bloco B — eu faço (hortas)
# ======================================================================

def b_hortas(c, t, C, B):
    head_seq(c, t, C, [("08", "EU FAÇO", "PENSANDO EM VOZ ALTA", BLUE), ("10", "EU FAÇO", "PEÇA POR PEÇA", PURPLE),
                       ("11", "O RESUMO", "FIEL", GREEN)])
    card(c, *CARD_R)
    ph2 = ep(t, C["10.t"], 0.7)
    a11 = ep(t, C["11.a"], 0.6)
    if ph2 < 1:
        a = 1 - ph2
        HORTAS.draw(c, t, C, 200, 270, 1060, 38, 60, a)
        text(c, "Texto elaborado para fins didáticos.", 200, 800, 20, "medium", GRAY, a, align="left")
        notas(c, t, C, [("08.c1", "TERRENO BALDIO", "terreno vazio, abandonado", INK2),
                        ("08.c1b", "MAS = PALAVRA-SINAL", "a alface NÃO é o principal", GREEN),
                        ("09.c2", "3 EXEMPLOS", "todos falam de PESSOAS juntas", C_POR),
                        ("09.c3", "PRETEXTO", "a desculpa para começar", C_AFI)], 1310, 240, 110, 420, a)
    if ph2 > 0:
        HORTAS.draw(c, t, C, 190, 220, 680, 24, 36, ph2 * (1 - 0.6 * a11))
        sx = 920
        rows = [("10.s1", "ASSUNTO", "hortas comunitárias", C_ASS),
                ("10.s2", "O QUE O TEXTO AFIRMA", "valem menos pela comida do que pela convivência", C_AFI),
                ("10.s3", "O PORQUÊ", "os exemplos: as hortas CRIAM laços", C_POR)]
        for k, (cue, tt, s, col) in enumerate(rows):
            a, d = rise(t, C[cue])
            a *= ph2 * (1 - a11 * 0.6)
            y = 210 + k * 140 + d
            piece(c, sx, y, 800, 118, col, a, "", notch_l=k > 0, bump_r=False)
            text(c, tt, sx + 40, y + 44, 22, "black", col, a, align="left", tracking=1)
            text(c, s, sx + 40, y + 88, 27, "black", INK, a, align="left")
        if a11 > 0:
            ar = ep(t, C["11.r"], 0.5)
            segs = [("Hortas comunitárias", C_ASS, ar), ("valem menos pelo alimento que produzem do que pelos laços de convivência", C_AFI, ar),
                    ("que criam.", C_POR, ar)]
            h = wa_bubble(c, segs, 300, 650, 1320, a11, 36)
            selo(c, 1580, 650, ep(t, C["11.b"], 0.4), "FIEL", GREEN, 6, 34)


# ======================================================================
# bloco C — os dois resumos errados
# ======================================================================

def b_errados(c, t, C, B):
    head_seq(c, t, C, [("12", "RESUMO ERRADO 1", "REDUÇÃO", AMBER), ("13", "RESUMO ERRADO 2", "EXTRAPOLAÇÃO", AMBER)])
    card(c, *CARD_R)
    a1 = ep(t, C["12.a"], 0.4)
    wa_bubble(c, [("Hortas comunitárias produzem", INK, 1), ("alface.", RED, ep(t, C["12.b"], 0.4))], 260, 220, 640, a1, 36)
    selo(c, 760, 380, ep(t, C["12.b"] + 0.6, 0.4), "SÓ UM PEDAÇO", AMBER, -6, 30)
    ac = ep(t, C["12.c"], 0.4)
    pill(c, "REDUÇÃO", 580, 500, AMBER, INK, size=34, a=ac, anchor="center", bounds=(0, 1920))
    text(c, "pegar uma PARTE", 580, 580, 32, "black", INK, ac)
    text(c, "como se fosse o TODO", 580, 625, 32, "black", INK, ac)
    a2 = ep(t, C["13.a"], 0.4)
    ab = ep(t, C["13.b"], 0.4)
    wa_bubble(c, [("Todo", RED if ab > 0.5 else INK, 1), ("terreno baldio deveria virar horta", INK, 1),
                  ("por lei.", RED if ab > 0.5 else INK, 1)], 1020, 220, 640, a2, 36)
    selo(c, 1520, 400, ep(t, C["13.b"] + 1.5, 0.4), "FOI ALÉM", AMBER, 6, 30)
    ad = ep(t, C["13.c"], 0.4)
    pill(c, "EXTRAPOLAÇÃO", 1340, 500, AMBER, INK, size=34, a=ad, anchor="center", bounds=(0, 1920))
    text(c, "dizer MAIS do que", 1340, 580, 32, "black", INK, ad)
    text(c, "o texto diz", 1340, 625, 32, "black", INK, ad)
    pill(c, "episódio 3: com calma", W / 2, 770, PURPLE, size=28, a=ep(t, C["13.d"], 0.4), anchor="center")


def b_eixo(c, t, C, B):
    frame(c, t, B["start"], "O RESUMO FIEL ACERTA", "O EIXO DO TEXTO", BLUE)
    cx, cy, R = 700, 500, 270
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        c.drawCircle(cx, cy, R, paint(mix("#FFFFFF", BLUE, 0.05), aa))
        c.drawCircle(cx, cy, R, paint(INK2, aa, stroke=10))
        for k in range(8):
            ang = k * math.pi / 4 + t * 0.4
            line(c, cx, cy, cx + R * math.cos(ang), cy + R * math.sin(ang), LIGHT, aa, 5)
        c.drawCircle(cx, cy, 60, paint(BLUE, aa))
    text(c, "EIXO DO TEXTO", 1400, 330, 44, "black", BLUE, aa)
    text(c, "a ideia em volta da qual", 1400, 390, 32, "bold", INK2, aa)
    text(c, "tudo gira", 1400, 435, 32, "bold", INK2, aa)
    ab = ep(t, C["14.b"], 0.4)
    pill(c, "vizinhança", cx, cy, BLUE, size=30, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["14.c"], 0.4)
    c.drawCircle(cx - 200, cy + 150, 16, paint(AMBER, acc))
    pill(c, "“alface”: longe do eixo", cx - 200, cy + 200, AMBER, INK, size=24, a=acc, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["14.d"], 0.4)
    c.drawCircle(cx + 330, cy - 200, 16, paint(AMBER, ad))
    pill(c, "“por lei”: passou da borda", cx + 400, cy - 250, AMBER, INK, size=24, a=ad, anchor="center", bounds=(0, 1920))
    text(c, "redução: ficou longe", 1400, 600, 32, "black", AMBER, acc)
    text(c, "extrapolação: passou dele", 1400, 660, 32, "black", AMBER, ad)


# ======================================================================
# blocos D e E — cópia e opinião
# ======================================================================

def b_copia(c, t, C, B):
    frame(c, t, B["start"], "RESUMO NÃO É", "CÓPIA", PURPLE)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        boxed(c, 260, 230, 760, 170, INK2, aa, 0.04)
        text(c, "“A colheita é o pretexto —", 640, 300, 40, "black", INK, aa)
        text(c, "o fruto é a vizinhança.”", 640, 355, 40, "black", INK, aa)
    pill(c, "linda frase ✨", 640, 450, GREEN, size=26, a=ep(t, C["15.a"] + 2.2, 0.4), anchor="center", bounds=(0, 1920))
    ab = ep(t, C["15.b"], 0.4)
    phone(c, 1120, 180, 520, 520, ab)
    wa_bubble(c, [("A colheita é o pretexto — o fruto é a vizinhança.", INK, 1)], 1270, 290, 330, ab, 26)
    a2 = ep(t, C["15.b"] + 1.6, 0.4)
    wa_bubble(c, [("Pretexto de quê? Que fruto?", INK, 1)], 1160, 470, 330, a2, 28, out=False)
    selo(c, 640, 560, ep(t, C["15.c"], 0.4), "REDUÇÃO", AMBER, -5, 34)
    regra(c, "Reescreva com as suas palavras.", 740, ep(t, C["15.d"], 0.5), 40)


def b_opiniao(c, t, C, B):
    frame(c, t, B["start"], "RESUMO NÃO", "OPINA", PURPLE)
    aa = ep(t, C["16.a"], 0.4)
    wa_bubble(c, [("Hortas são ótimas, e toda cidade devia ter uma.", INK, 1)], 560, 220, 800, aa, 38)
    ab = ep(t, C["16.b"], 0.4)
    selo(c, 1380, 330, ab, "SUA OPINIÃO", RED, 6, 32)
    acc = ep(t, C["16.c"], 0.5)
    for k, (s, col, ok) in enumerate((("o que o TEXTO defende", GREEN, True), ("o que VOCÊ acha", RED, False))):
        x = 560 + k * 800
        check_icon(c, x - 170, 512, 28, acc, col, "check" if ok else "x")
        text(c, s, x - 125, 525, 38, "black", col, acc, align="left")
    pill(c, "no WhatsApp: conta o texto, não dá palpite", W / 2, 700, BLUE, size=30, a=ep(t, C["16.d"], 0.4), anchor="center")


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["Assunto + o que o texto afirma + o porquê.", "Com suas palavras, não copiando.", "Resumo conta o texto, não a sua opinião."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        if k == 0:
            colored(c, [("Assunto", C_ASS, a), ("+ o que o texto afirma", C_AFI, a), ("+ o porquê.", C_POR, a)], 350, y, 50, 1400)
        else:
            text(c, s, 350, y, 50, "black", INK, a, align="left")


ERROS = [("18", "Copiar a FRASE DE EFEITO", "a frase está no texto", "bonita não é completa: reescreva pela fórmula"),
         ("19", "Resumir só UM EXEMPLO", "o exemplo é fácil de lembrar", "exemplo é PERNA, não tampo"),
         ("20", "Pôr a sua OPINIÃO ou uma PROPOSTA que o texto não faz", "parece a continuação natural", "em que linha isso está?")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(3):
        badge_num(c, k + 1, 880 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 330, 34, aa, RED, "x")
    para(c, err, 360, 345, 44, "black", RED, aa, 1300)
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 480, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 560, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 678, 34, ac, GREEN)
    text(c, fix, 360, 694, 42, "black", GREEN, ac, align="left")
    if sid == "19" and ac > 0:
        c.save(); c.translate(1500, 560); c.scale(0.22, 0.22); c.translate(-W / 2, -230)
        V.mesa(c, W / 2, 230, ac, "TESE", 1, [(1, None, 0, None, 0), (1 - ep(t, cue("c") + 1.0, 0.5), None, 0, None, 0), (1, None, 0, None, 0)], top_size=80)
        c.restore()


# ======================================================================
# questão 6 — nós fazemos
# ======================================================================

ALTS = [("A", "Adolescentes que dormem tarde precisam de mais disciplina para acordar cedo.", "26.a", "o texto NÃO aceita", RED),
        ("B", "O horário das escolas brasileiras deve ser adiado imediatamente.", "26.b", "FOI ALÉM", AMBER),
        ("C", "Em outros países, pesquisadores acompanham redes de ensino.", "26.c", "SÓ UM PEDAÇO", AMBER),
        ("D", None, None, "", GREEN),
        ("E", "A atenção dos alunos depende exclusivamente do horário em que as aulas começam.", "27.e", "FOI ALÉM", AMBER)]
D_SEGS = [("O descompasso entre o relógio biológico do adolescente e o horário escolar", C_ASS, "27.s1"),
          ("provoca privação de sono,", C_AFI, "27.s2"),
          ("o que levou a testes de adiamento das aulas.", C_POR, "27.s3")]


def resumo_sono(c, t, C, x, y, w, a, size=30):
    segs = [("O sono do adolescente e o horário da escola:", C_ASS, ep(t, C["24.s1"], 0.4)),
            ("corpo e escola desencontrados tiram o sono do aluno,", C_AFI, ep(t, C["24.s2"], 0.4)),
            ("e alguns lugares testaram começar mais tarde.", C_POR, ep(t, C["24.s3"], 0.4))]
    return wa_bubble(c, segs, x, y, w, a, size)


def b_questao(c, t, C, B):
    head_seq(c, t, C, [("21", "QUESTÃO · ESTILO ENEM", "NÓS FAZEMOS", BLUE), ("24", "ANTES DAS ALTERNATIVAS", "O SEU RESUMO", PURPLE),
                       ("25", "QUESTÃO · ESTILO ENEM", "COMPARE COM O RESUMO", BLUE)])
    card(c, *CARD_R)
    p24 = ep(t, C["24"], 0.7)
    p25 = ep(t, C["25"], 0.7)
    # fase 1: leitura
    if p24 < 1:
        a = 1 - p24
        SONO.draw(c, t, C, 200, 260, 1060, 34, 54, a)
        text(c, "Texto elaborado para fins didáticos.", 200, 800, 20, "medium", GRAY, a, align="left")
        notas(c, t, C, [("21.c1", "RELÓGIO BIOLÓGICO", "o relógio de dentro do corpo", INK2),
                        ("21.c1b", "ASSUNTO", "o sono do adolescente", C_ASS),
                        ("22.c2", "PORÉM = PALAVRA-SINAL", "corpo × escola", GREEN),
                        ("22.c3", "PRIVAÇÃO DE SONO", "dormir menos do que precisa", INK2),
                        ("22.c3b", "“PREGUIÇA”", "é a ideia dos ADULTOS", AMBER),
                        ("23.c4", "CONSEQUÊNCIA", "testes, ainda acompanhados", C_POR)], 1310, 230, 98, 420, a)
    # fase 2: o seu resumo
    if p24 > 0 and p25 < 1:
        a = p24 * (1 - p25)
        pause_timer(c, t, C["24.b"] - 1.7, W / 2, 330, a, dur=1.5, r=60)
        text(c, "escreva o SEU resumo em 1 frase", W / 2, 470, 40, "black", PURPLE, a * ep(t, C["24.t"], 0.4))
        pieces_row(c, t, [a * ep(t, C["24.s1"], 0.4), a * ep(t, C["24.s2"], 0.4), a * ep(t, C["24.s3"], 0.4)], 230, 420, 130,
                   join=1, labels=["ASSUNTO", "O QUE O TEXTO AFIRMA", "CONSEQUÊNCIA"])
        resumo_sono(c, t, C, 300, 560, 1320, a * ep(t, C["24.s1"], 0.4), 34)
    # fase 3: alternativas × resumo
    if p25 > 0:
        a = p25
        resumo_sono(c, t, C, 180, 230, 600, a, 28)
        text(c, "SEU RESUMO", 200, 210, 22, "black", PURPLE, a, align="left", tracking=1)
        text(c, "A alternativa que melhor resume o texto é:", 860, 215, 26, "black", BLUE, a * ep(t, C["25.t"], 0.4), align="left")
        aok = ep(t, C["27.ok"], 0.5)
        y = 270
        for L, s, cx, why, col in ALTS:
            al, d = rise(t, C[f"25.{L.lower()}"])
            al *= a
            ok = s is None
            if ok:
                segs = [(ss, mix(INK, cc, ep(t, C[cue], 0.4)), al) for ss, cc, cue in D_SEGS]
                hh = len(wrap(" ".join(x[0] for x in D_SEGS), "black", 23, 800)) * 30 + 12
                if aok > 0:
                    rrect(c, 840, y - 30 + d, 920, hh + 12, 12, GREEN, 0.13 * aok)
                badge_num(c, L, 870, y - 8 + d, al, 20, bg=GREEN if aok > 0.5 else INK)
                colored(c, segs, 910, y + d, 23, 800, 30, "black")
                y += hh + 22
                continue
            lines = wrap(s, "black", 23, 800)
            hh = len(lines) * 30 + 12 + 28
            badge_num(c, L, 870, y - 8 + d, al, 20, bg=INK)
            ax = ep(t, C[cx], 0.4)
            for j, ln in enumerate(lines):
                text(c, ln, 910, y + d + j * 30, 23, "black", INK, al * (1 - 0.5 * ax), align="left")
                if ax > 0:
                    strike(c, 906, y + d + j * 30 - 8, 914 + text_w(ln, "black", 23), y + d + j * 30 - 8, ax, RED, ax)
            if ax > 0:
                pill(c, why, 910, y + d + len(lines) * 30 + 2, col, INK if col == AMBER else None, size=18, a=ax, bounds=(0, 1920))
            y += hh + 22
        pause_timer(c, t, C["25.end"] - 1.7, 480, 650, a)
        result_box(c, "Letra D", 480, 700, 56, aok, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "AS 5 ALTERNATIVAS-ARMADILHA", PURPLE)
    items = [("29.a", "SÓ UM PEDAÇO"), ("29.b", "FOI ALÉM"), ("29.c", "?"), ("29.c", "?"), ("29.c", "?")]
    for k, (cue, s) in enumerate(items):
        a, d = rise(t, C[cue] + (0.3 * (k - 2) if k >= 2 else 0))
        x = 330 + k * 315
        if a <= 0:
            continue
        col = AMBER if k < 2 else LIGHT
        rrect(c, x - 140, 300 + d, 280, 260, 22, "#FFFFFF", a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 140, 300 + d, 280, 260), 22, 22), paint(col, a, stroke=5))
        badge_num(c, k + 1, x, 360 + d, a, 28, bg=AMBER if k < 2 else GRAY)
        text_mid(c, s, x, 470 + d, 30 if k < 2 else 80, "black", INK if k < 2 else GRAY, a)
    pill(c, "eles se repetem SEMPRE", W / 2, 650, AMBER, INK, size=30, a=ep(t, C["29.c"] + 1.2, 0.4), anchor="center")
    pill(c, "ep. 3 · as 5 alternativas-armadilha", W / 2, 750, PURPLE, size=34, a=ep(t, C["29.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"], "Desafio: resuma esta aula em uma frase!")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, whatsapp=b_whatsapp, formula=b_formula, hortas=b_hortas,
              errados=b_errados, eixo=b_eixo, copia=b_copia, opiniao=b_opiniao, recap=b_recap, erros=b_erros,
              questao=b_questao, ponte=b_ponte, cta=b_cta)
