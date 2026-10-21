"""Visual — Compreensão Global e Tese, Episódio 1: Tema, assunto e tese (tema claro).
Analogias: BIBLIOTECA (prateleira = tema, livro = assunto, frase para levar = tese) e MESA (tampo = tese, pernas = apoios).
Leitura da Questão 1: texto inteiro na tela, marca-texto acompanhando cada palavra dita (tempos.json).
Cores: azul = tese/definição · verde = pista/palavra-sinal · âmbar = armadilha · vermelho = erro · roxo = regra.
"""
import json
import math
import re
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "enem_linguagens_compreensao_ep1_tema_assunto_tese.mp4"
CARD_R = (140, 150, 1640, 690)
TESE_CEL = "A escola deve ensinar a usar o celular, não só proibi-lo."

# ======================================================================
# utilidades
# ======================================================================

def wrap(s, peso, size, maxw):
    out, cur = [], ""
    for w in s.split():
        tst = (cur + " " + w).strip()
        if cur and text_w(tst, peso, size) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    if cur:
        out.append(cur)
    return out


def para(c, s, x, y, size, peso, color, a, maxw, lh=None, align="left"):
    """parágrafo com quebra automática; y = linha de base da 1ª linha. Retorna a altura usada."""
    lh = lh or size * 1.32
    lines = wrap(s, peso, size, maxw)
    if a > 0:
        for k, ln in enumerate(lines):
            text(c, ln, x, y + k * lh, size, peso, color, a, align=align)
    return len(lines) * lh


def which(t, C, ids):
    cur = ids[0]
    for i in ids:
        if t >= C[i] - 0.05:
            cur = i
    return cur


def frame(c, t, t0, l1, l2, col):
    head(c, t, t0, l1, l2, col)
    card(c, *CARD_R)


def head_seq(c, t, C, heads):
    """heads = [(sid, l1, l2, cor)] — troca o título a cada cena"""
    sid = which(t, C, [h[0] for h in heads])
    for h in heads:
        if h[0] == sid:
            head(c, t, C[sid], h[1], h[2], h[3])


def boxed(c, x, y, w, h, col, a, fill=0.10, r=22, sw=4):
    if a <= 0:
        return
    rrect(c, x, y, w, h, r, col, fill * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), paint(col, a, stroke=sw))


def regra(c, s, cy, a, size=40):
    """caixa roxa de regra/frase-chave"""
    if a <= 0:
        return
    w = text_w(s, "black", size) + 90
    boxed(c, W / 2 - w / 2, cy - 50, w, 100, PURPLE, a, 0.10)
    text_mid(c, s, W / 2, cy, size, "black", PURPLE, a)


def selo(c, x, y, a, s, col=None, rot=-6, size=32):
    if a <= 0:
        return
    col = col or AMBER
    c.save(); c.translate(x, y); c.rotate(rot)
    w = text_w(s, "black", size) + 50
    sc = 0.8 + 0.2 * ease_back(clamp(a))
    c.scale(sc, sc)
    boxed(c, -w / 2, -32, w, 64, col, a, 0.15, 12, 5)
    text_mid(c, s, 0, 0, size, "black", col, a)
    c.restore()


def pause_timer(c, t, t0, x, y, a=1.0, dur=1.6, r=44):
    u = clamp((t - t0) / dur)
    ap = a * ep(t, t0, 0.3) * (1 - prog(t, t0 + dur + 0.4, 0.4))
    if ap <= 0:
        return
    c.drawCircle(x, y, r + 14, paint(AMBER, ap * 0.18))
    c.drawCircle(x, y, r, paint("#FFFFFF", ap))
    c.drawArc(skia.Rect.MakeLTRB(x - r, y - r, x + r, y + r), -90, 360 * (1 - u), False, paint(AMBER, ap, stroke=10, cap_round=True))
    c.drawRect(skia.Rect.MakeXYWH(x - 15, y - 20, 10, 40), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(x + 5, y - 20, 10, 40), paint(INK, ap))
    text(c, "PAUSE", x, y + r + 40, 26, "black", AMBER, ap)


def bubble(c, s, x, y, w, col, a, left=True, size=32, fg=None):
    """balão de conversa; (x, y) = canto superior esquerdo. Retorna a altura."""
    if a <= 0:
        return 0
    lines = wrap(s, "bold", size, w - 60)
    h = len(lines) * size * 1.3 + 44
    rrect(c, x, y, w, h, 26, col, a, shadow=True)
    p = skia.Path()
    if left:
        p.moveTo(x + 30, y + h - 2); p.lineTo(x + 6, y + h + 22); p.lineTo(x + 64, y + h - 2)
    else:
        p.moveTo(x + w - 30, y + h - 2); p.lineTo(x + w - 6, y + h + 22); p.lineTo(x + w - 64, y + h - 2)
    c.drawPath(p, paint(col, a))
    for k, ln in enumerate(lines):
        text(c, ln, x + 30, y + 22 + size * 0.95 + k * size * 1.3, size, "bold", fg or on(col), a, align="left")
    return h


def person(c, x, y, col, a, s=1.0):
    if a <= 0:
        return
    c.drawCircle(x, y, 34 * s, paint(col, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 50 * s, y + 44 * s, 100 * s, 90 * s), 40 * s, 40 * s), paint(col, a))


def folder(c, x, y, w, h, label, a, col=None):
    if a <= 0:
        return
    col = col or "#F2C94C"
    rrect(c, x, y - 34, w * 0.4, 50, 12, mix(col, "#000000", 0.08), a)
    rrect(c, x, y, w, h, 16, col, a, shadow=True)
    lw = min(w - 60, text_w(label, "black", 30) + 50)
    rrect(c, x + w / 2 - lw / 2, y + h / 2 - 34, lw, 68, 10, "#FFFFFF", a)
    text_mid(c, label, x + w / 2, y + h / 2, 30, "black", INK, a)


# ======================================================================
# mesa (tampo = tese · pernas = argumentos · pés = exemplos)
# ======================================================================

LEG_X = (-470, 0, 470)


def mesa(c, cx, top_y, a, top_txt="TESE", top_a=1.0, legs=None, wobble=0.0, lift=0.0, fall=0.0, top_size=34, w=1300):
    """legs = [(alpha_perna, texto_argumento|None, alpha_arg, texto_exemplo|None, alpha_ex)]"""
    if a <= 0:
        return
    legs = legs or [(1, None, 0, None, 0)] * 3
    base_y = top_y + 400
    c.save()
    c.translate(cx, base_y); c.rotate(wobble); c.translate(-cx, -base_y)
    for k, (la, arg, aa, ex, ea) in enumerate(legs):
        lx = cx + LEG_X[k]
        al = a * la * (1 - 0.7 * fall)
        if al <= 0:
            continue
        c.save()
        ang = fall * (38 if k == 0 else -38 if k == 2 else 14)
        c.translate(lx, base_y); c.rotate(ang); c.translate(-lx, -base_y)
        rrect(c, lx - 15, top_y + 100, 30, 300, 8, "#8B5E3C", al)
        c.restore()
        al = al * (1 - fall)
        if arg and aa > 0:
            ww = 400
            lines = wrap(arg, "black", 26, ww - 40)
            hh = len(lines) * 34 + 60
            rrect(c, lx - ww / 2, top_y + 140, ww, hh, 16, "#FFFFFF", al * aa, shadow=True)
            text(c, "ARGUMENTO", lx, top_y + 172, 18, "black", GRAY, al * aa, tracking=1)
            for j, ln in enumerate(lines):
                text(c, ln, lx, top_y + 208 + j * 34, 26, "black", INK, al * aa)
        if ex and ea > 0:
            ww = 400
            lines = wrap(ex, "bold", 24, ww - 40)
            hh = len(lines) * 31 + 54
            y0 = base_y + 14
            rrect(c, lx - ww / 2, y0, ww, hh, 16, "#F4F1EA", al * ea)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(lx - ww / 2, y0, ww, hh), 16, 16), paint(LIGHT, al * ea, stroke=2))
            text(c, "EXEMPLO", lx, y0 + 28, 17, "black", GRAY, al * ea, tracking=1)
            for j, ln in enumerate(lines):
                text(c, ln, lx, y0 + 60 + j * 31, 24, "bold", INK2, al * ea)
    at = a * top_a
    if at > 0:
        ty = top_y - lift * 160
        rrect(c, cx - w / 2, ty, w, 100, 18, mix("#FFFFFF", BLUE, 0.12), at, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, ty, w, 100), 18, 18), paint(BLUE, at, stroke=5))
        text_mid(c, top_txt, cx, ty + 50, top_size if text_w(top_txt, "black", top_size) < w - 60 else 28, "black", BLUE, at)
    c.restore()


# ======================================================================
# marca-texto sincronizado com a voz
# ======================================================================

TEMPOS = Path(__file__).resolve().parent.parent / "audio" / "tempos.json"
try:
    _SC = {s["id"]: s for s in json.load(open(TEMPOS, encoding="utf-8"))["scenes"]}
except Exception:
    _SC = {}


def _norm(w):
    return re.sub(r"[^\wà-ú]", "", w.lower())


def word_times(sid, sentence, cue_t, next_t):
    """instantes absolutos em que cada palavra de `sentence` é dita (fallback: distribuição linear)"""
    ws = sentence.split()
    sc = _SC.get(sid)
    if sc:
        toks = sc["tokens"]
        key = [_norm(w) for w in ws[:3]]
        for i in range(len(toks) - 2):
            if [_norm(toks[i + j]["disp"]) for j in range(3)] == key:
                ts = [sc["start"] + toks[min(i + j, len(toks) - 1)]["t0"] for j in range(len(ws))]
                return ts
    return [lerp(cue_t, next_t, j / max(1, len(ws))) for j in range(len(ws))]


Q1 = [("33", "f1", "Bibliotecas de bairro não são depósitos de livros velhos."),
      ("34", "f2", "Num tempo em que quase tudo se lê na tela, elas continuam sendo um dos poucos lugares públicos onde se pode passar a tarde sem pagar nada e sem que ninguém pergunte o que você vai consumir."),
      ("34", "f3", "Quem estuda para concurso encontra ali silêncio; quem não tem internet em casa, conexão; o aposentado, jornal e conversa."),
      ("35", "f4", "Fechar uma biblioteca para economizar parece racional na planilha, mas apaga um espaço de convivência que nenhum aplicativo substitui."),
      ("35", "f5", "Antes de cortar, as prefeituras deveriam contar quantas pessoas entram por aquela porta.")]
NEXT = {"f1": "c1", "f2": "c2", "f3": "c3", "f4": "c4", "f5": "c5"}
_LAY = {}
_WT = {}


def layout(x, y, maxw, size, lh):
    key = (x, y, maxw, size, lh)
    if key in _LAY:
        return _LAY[key]
    words = []
    for si, (_, _, s) in enumerate(Q1):
        for wi, w in enumerate(s.split()):
            words.append([w, si, wi])
    out, xx, yy = [], x, y
    sp = text_w(" ", "semibold", size)
    for w, si, wi in words:
        ww = text_w(w, "semibold", size)
        if xx > x and xx + ww > x + maxw:
            xx, yy = x, yy + lh
        out.append((w, si, wi, xx, yy, ww))
        xx += ww + sp
    _LAY[key] = out
    return out


def times(C):
    if "t" not in _WT:
        _WT["t"] = [word_times(sid, s, C[f"{sid}.{f}"], C[f"{sid}.{NEXT[f]}"]) for sid, f, s in Q1]
    return _WT["t"]


def leitura(c, t, C, x, y, maxw, size, lh, a=1.0):
    """texto-base inteiro + marca-texto; destaques: assunto (azul), concessão (âmbar), MAS (verde), posição (azul)"""
    if a <= 0:
        return
    T = times(C)
    lay = layout(x, y, maxw, size, lh)
    mas_i = Q1[3][2].split().index("mas,") if "mas," in Q1[3][2].split() else Q1[3][2].split().index("mas")
    a_assunto = ep(t, C["33.c1"], 0.4)
    a_conc = ep(t, C["35.c4"], 0.4)
    a_pos = ep(t, C["35.c4b"], 0.4)
    for w, si, wi, xx, yy, ww in lay:
        top, hh = yy - size * 0.86, size * 1.16
        said = ep(t, T[si][wi] - 0.05, 0.18)
        if said > 0:
            rrect(c, xx - 4, top, ww + 8, hh, 6, "#FFE58A", a * said * 0.55)
        if si == 0 and wi < 3 and a_assunto > 0:
            rrect(c, xx - 4, top, ww + 8, hh, 6, BLUE, a * a_assunto * 0.22)
        if si == 3 and wi < mas_i and a_conc > 0:
            line(c, xx - 2, yy + 8, xx + ww + 6, yy + 8, AMBER, a * a_conc, 4)
        if si == 3 and wi > mas_i and a_pos > 0:
            rrect(c, xx - 4, top, ww + 8, hh, 6, BLUE, a * a_pos * 0.22)
            line(c, xx - 2, yy + 8, xx + ww + 6, yy + 8, BLUE, a * a_pos, 4)
        col = INK
        if si == 3 and wi == mas_i:
            am = ep(t, T[si][wi] - 0.05, 0.25)
            if am > 0:
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx - 7, top - 3, ww + 14, hh + 6), 8, 8), paint(GREEN, a * am, stroke=4))
            col = mix(INK, GREEN, am)
        text(c, w, xx, yy, size, "semibold", col, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def doc_card(c, x, y, w, h, a, titulo, tag, tese, col):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, "#FFFFFF", a, shadow=True)
    text(c, titulo, x + 36, y + 56, 22, "black", GRAY, a, align="left", tracking=1)
    pill(c, tag, x + 36, y + 110, INK2, size=24, a=a, bounds=(0, 1920))
    for j in range(3):
        line(c, x + 36, y + 180 + j * 34, x + w - 36 - j * 60, y + 180 + j * 34, LINE, a, 10)
    text(c, "defende:", x + 36, y + h - 96, 24, "bold", GRAY, a, align="left")
    text(c, tese, x + 36, y + h - 46, 38, "black", col, a, align="left")


def b_hook(c, t, C, B):
    head(c, t, B["start"], "LINGUAGENS ENEM", "ASSUNTO × TESE", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    doc_card(c, 260, 190, 620, 400, aa, "TEXTO 1", "celular na escola", "PROIBIR", RED)
    doc_card(c, 1040, 190, 620, 400, ep(t, C["01.a"] + 0.5, 0.5), "TEXTO 2", "celular na escola", "ENSINAR A USAR", BLUE)
    pill(c, "mesmo assunto · teses opostas", W / 2, 640, PURPLE, size=28, a=ep(t, C["01.a"] + 1.4, 0.5), anchor="center")
    ab = ep(t, C["01.b"], 0.4)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        boxed(c, 460, 700, 1000, 110, AMBER, ac, 0.12)
        text(c, "ALTERNATIVA", 500, 742, 20, "black", AMBER, ac, align="left", tracking=1)
        text(c, "celular · escola · aluno · uso · regras...", 500, 790, 34, "black", INK, ac, align="left")
    selo(c, 1500, 790, ep(t, C["01.d"], 0.4), "ERROU", RED, 8)
    text(c, "sobre o que fala?", W / 2, 690, 30, "black", GRAY, ab * (1 - ac))
    ae = ep(t, C["01.e"], 0.5)
    pill(c, "HOJE: SOBRE O QUE FALA × O QUE DIZ", W / 2, 870, GREEN, size=30, a=ae, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "separar o ASSUNTO da TESE", "de qualquer texto"), ("02.b", "saber o que é CENTRAL", "e o que é só APOIO")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 190 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")
        text(c, sub, 400, y + 56, 32, "bold", GRAY, a, align="left")
    pill(c, "cada palavra vai ser explicada", W / 2, 760, BLUE, size=30, a=ep(t, C["02.c"], 0.5), anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "PRÉ-REQUISITOS", "NENHUM", GREEN)
    a0 = ep(t, C["03.t"], 0.5)
    text(c, "0", 520, 560, 300, "black", GREEN, a0)
    aa, dy = rise(t, C["03.a"])
    text(c, "regras de gramática", 820, 400 + dy, 44, "black", INK2, aa, align="left")
    line(c, 810, 386 + dy, 810 + text_w("regras de gramática", "black", 44) + 20, 386 + dy, RED, aa, 5, progress=ep(t, C["03.a"] + 0.4, 0.5))
    ab = ep(t, C["03.b"], 0.5)
    bubble(c, "acompanha o grupo da família?", 820, 480, 760, GREEN, ab, size=34)
    text(c, "então já tem tudo o que precisa", 820, 680, 36, "black", GREEN, ep(t, C["03.b"] + 1.2, 0.5), align="left")


# ======================================================================
# bloco A — os três níveis
# ======================================================================

def b_familia(c, t, C, B):
    head(c, t, B["start"], "GRUPO DA FAMÍLIA", "A DISCUSSÃO", BLUE)
    a0 = ep(t, C["04.t"], 0.5)
    rrect(c, 620, 160, 680, 680, 48, "#1C1C1E", a0, shadow=True)
    rrect(c, 640, 180, 640, 640, 36, "#ECE5DD", a0)
    text(c, "Família", 960, 230, 28, "black", INK2, a0)
    aa = ep(t, C["04.a"], 0.4)
    text(c, "Tia", 680, 290, 22, "black", RED, aa, align="left")
    bubble(c, "Celular na escola tem que ser proibido!", 670, 304, 520, "#FFFFFF", aa, True, 30, INK)
    ab = ep(t, C["04.b"], 0.4)
    text(c, "Primo", 1240, 490, 22, "black", BLUE, ab, align="right")
    bubble(c, "A escola tem que ensinar a usar.", 760, 504, 480, "#DCF8C6", ab, False, 30, INK)
    ac, ad = ep(t, C["04.c"], 0.4), ep(t, C["04.d"], 0.4)
    check_icon(c, 300, 400, 34, ac, GREEN)
    text(c, "FALAM da", 220, 480, 34, "black", GREEN, ac, align="left")
    text(c, "mesma coisa", 220, 524, 34, "black", GREEN, ac, align="left")
    check_icon(c, 1620, 400, 34, ad, RED, "x")
    text(c, "DIZEM a", 1540, 480, 34, "black", RED, ad, align="left")
    text(c, "mesma coisa?", 1540, 524, 34, "black", RED, ad, align="left")


def shelf(c, x, y, a, hl=0.0, pull=0.0):
    """prateleira com livros; o 4º livro (celular na escola) pode sair (pull) e acender (hl)"""
    if a <= 0:
        return
    rrect(c, x, y + 250, 470, 26, 6, "#8B5E3C", a, shadow=True)
    rrect(c, x, y - 20, 470, 22, 6, "#8B5E3C", a)
    cols = ["#E5484D", "#3B6CF6", "#16A36A", "#E8A317", "#7C5CFA", "#0EA5E9", "#F97316"]
    xx = x + 22
    for k, col in enumerate(cols):
        bw, bh = (52, 230) if k != 3 else (66, 250)
        dy = 0 if k != 3 else -pull * 60
        aa = a * (1 - 0.6 * hl if k != 3 else 1)
        rrect(c, xx, y + 250 - bh + dy, bw, bh, 6, col, aa)
        if k == 3 and hl > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx - 5, y + 245 - bh + dy, bw + 10, bh + 10), 9, 9), paint(BLUE, a * hl, stroke=5))
        xx += bw + 8


def b_biblioteca(c, t, C, B):
    head_seq(c, t, C, [("05", "A BIBLIOTECA", "FALAR × DIZER", BLUE), ("06", "1º DEGRAU", "TEMA", BLUE),
                       ("07", "2º DEGRAU", "ASSUNTO", BLUE), ("08", "3º DEGRAU", "TESE", BLUE)])
    card(c, *CARD_R)
    # prateleira
    aa = ep(t, C["05.a"], 0.5)
    ab = ep(t, C["05.b"], 0.5)
    shelf(c, 210, 300, aa, hl=ep(t, C["05.c"], 0.4), pull=ep(t, C["05.c"], 0.6))
    pill(c, "EDUCAÇÃO", 445, 250, INK2, size=28, a=ab, anchor="center", bounds=(0, 1920))
    # livro
    ac = ep(t, C["05.c"] + 0.3, 0.5)
    arrow(c, 700, 420, 780, 420, GRAY, ac, 4, 16, progress=ac)
    if ac > 0:
        rrect(c, 800, 260, 300, 340, 18, "#E8A317", ac, shadow=True)
        rrect(c, 800, 260, 30, 340, 8, mix("#E8A317", "#000000", 0.2), ac)
        rrect(c, 850, 360, 220, 120, 10, "#FFFFFF", ac)
        text(c, "celular", 960, 410, 30, "black", INK, ac)
        text(c, "na escola", 960, 450, 30, "black", INK, ac)
    # frase
    ad = ep(t, C["05.d"], 0.5)
    arrow(c, 1120, 420, 1190, 420, GRAY, ad, 4, 16, progress=ad)
    if ad > 0:
        boxed(c, 1210, 270, 500, 320, BLUE, ad, 0.08)
        text(c, "“", 1250, 360, 110, "black", BLUE, ad, align="left")
        para(c, "A escola deve ensinar a usar o celular, não só proibir.", 1250, 390, 36, "black", BLUE, ad, 430)
    # rótulos dos degraus
    lab = [("06", 445, "TEMA", "a área ampla"), ("07", 950, "ASSUNTO", "o pedaço específico"), ("08", 1460, "TESE", "o que o texto AFIRMA")]
    for sid, x, s, sub in lab:
        a = ep(t, C[f"{sid}.a"], 0.5)
        pill(c, s, x, 680, BLUE, size=38, a=a, anchor="center", bounds=(0, 1920))
        text(c, sub, x, 760, 30, "bold", INK2, a)
    a6 = fw(t, C["06.b"], C["07"])
    for j, s in enumerate(("educação", "cidade", "consumo", "trabalho")):
        pill(c, s, 445 + (j - 1.5) * 118, 815, LIGHT, INK, size=20, a=a6 * ep(t, C["06.b"] + 0.25 * j, 0.3), anchor="center", bounds=(0, 1920))
    a7 = ep(t, C["07.b"], 0.5)
    text(c, "não é “educação em geral”", 950, 815, 24, "bold", GRAY, a7)


TAB = [("09.a", "educação", "celular na sala de aula", "A escola deve ensinar a usar o celular, não só proibi-lo."),
       ("09.b", "cidade", "feiras livres", "A feira deve continuar na rua, porque é espaço de encontro e de venda direta."),
       ("09.c", "consumo", "roupas muito baratas", "O preço baixo esconde custos pagos por quem não estava na loja.")]


def b_tabela(c, t, C, B):
    frame(c, t, B["start"], "OS TRÊS DEGRAUS", "EM TRÊS EXEMPLOS", BLUE)
    xs = (200, 470, 860)
    ws = (250, 370, 860)
    a0 = ep(t, C["09.t"], 0.4)
    for x, s in zip(xs, ("TEMA", "ASSUNTO", "TESE")):
        text(c, s, x + 20, 230, 26, "black", BLUE if s == "TESE" else GRAY, a0, align="left", tracking=1.5)
    line(c, 200, 255, 1720, 255, LINE, a0, 3)
    for k, (cue, tema, ass, tese) in enumerate(TAB):
        a, d = rise(t, C[cue])
        y = 320 + k * 165 + d
        text(c, tema, xs[0] + 20, y, 32, "bold", INK2, a, align="left")
        para(c, ass, xs[1] + 20, y, 32, "bold", INK, a, ws[1] - 40)
        para(c, "“" + tese + "”", xs[2] + 20, y, 30, "black", BLUE, a, ws[2] - 40, 40)
        if k < 2:
            line(c, 200, y + 105, 1720, y + 105, LINE, a, 2)
    ad = ep(t, C["09.d"], 0.5)
    boxed(c, 855, 270, 870, 500, BLUE, ad, 0.0, 22, 5)
    pill(c, "só esta coluna DIZ alguma coisa", 1290, 800, BLUE, size=28, a=ad, anchor="center")


# ======================================================================
# bloco B — teste da discordância
# ======================================================================

def b_futebol(c, t, C, B):
    frame(c, t, B["start"], "DOIS AMIGOS", "FALANDO DE FUTEBOL", BLUE)
    a0 = ep(t, C["10.a"], 0.5)
    person(c, 330, 520, BLUE, a0)
    person(c, 1590, 520, "#F97316", a0)
    ab = fw(t, C["10.b"], C["10.c"])
    bubble(c, "O meu time.", 420, 330, 400, BLUE, ab, True, 40)
    text(c, "só um nome · nada a discordar", 960, 640, 32, "bold", GRAY, ep(t, C["10.b"] + 0.9, 0.4) * (1 - prog(t, C["10.c"], 0.4)))
    ac = ep(t, C["10.c"], 0.5)
    bubble(c, "O meu time vai ser campeão este ano.", 420, 300, 760, BLUE, ac, True, 40)
    ad = ep(t, C["10.d"], 0.4)
    bubble(c, "NUNCA!", 1250, 330, 260, "#F97316", ad, False, 44)
    selo(c, 960, 700, ad, "JÁ DÁ BRIGA", AMBER)


def b_discordancia(c, t, C, B):
    frame(c, t, B["start"], "O TESTE DA", "DISCORDÂNCIA", PURPLE)
    a0 = ep(t, C["11.t"], 0.5)
    para(c, "O celular deve ser ensinado, não só proibido.", 960, 290, 44, "black", INK, a0, 1400, align="center")
    aa = ep(t, C["11.a"], 0.4)
    xv = 960 - text_w("O celular deve ser ensinado, não só proibido.", "black", 44) / 2 + text_w("O celular ", "black", 44)
    wv = text_w("deve ser", "black", 44)
    if aa > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xv - 2, 245, wv + 16, 62), 10, 10), paint(GREEN, aa, stroke=4))
    pill(c, "VERBO", xv + wv / 2, 360, GREEN, size=26, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["11.b"], 0.4)
    pill(c, "POSIÇÃO: alguém discordaria?", 1300, 360, BLUE, size=26, a=ab, anchor="center", bounds=(0, 1920))
    check_icon(c, 1560, 360, 24, ep(t, C["11.b"] + 0.8, 0.3), GREEN)
    text(c, "= TESE", 960, 470, 40, "black", BLUE, ab)
    acc = ep(t, C["11.c"], 0.5)
    folder(c, 760, 520, 400, 150, "celular na escola", acc)
    text(c, "= ASSUNTO (etiqueta)", 1200, 610, 32, "black", INK2, acc, align="left")
    regra(c, "Se ninguém pode discordar, ainda não é a tese.", 770, ep(t, C["11.d"], 0.5), 38)


# ======================================================================
# bloco C — mesmo assunto, teses opostas
# ======================================================================

def b_opostas(c, t, C, B):
    head_seq(c, t, C, [("12", "MESMO ASSUNTO", "TESES OPOSTAS", BLUE), ("13", "COMO A PROVA", "MONTA A ARMADILHA", AMBER)])
    card(c, *CARD_R)
    a13 = ep(t, C["13"], 0.6)
    yy = 190 - 10 * a13
    sc = 1 - 0.18 * a13
    c.save(); c.translate(W / 2, yy); c.scale(sc, sc); c.translate(-W / 2, -yy)
    doc_card(c, 270, yy, 620, 400, ep(t, C["12.b"], 0.5), "ARTIGO 1", "celular na escola", "PROIBIÇÃO TOTAL", RED)
    doc_card(c, 1030, yy, 620, 400, ep(t, C["12.c"], 0.5), "ARTIGO 2", "celular na escola", "USO ORIENTADO", BLUE)
    c.restore()
    pill(c, "mesmo assunto · teses opostas", W / 2, 680, PURPLE, size=30, a=ep(t, C["12.d"], 0.5) * (1 - a13), anchor="center")
    aa = ep(t, C["13.a"], 0.4)
    pill(c, "O TEXTO", 1340, 170, BLUE, size=24, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        boxed(c, 360, 560, 1200, 170, AMBER, ab, 0.12)
        text(c, "ALTERNATIVA", 400, 600, 20, "black", AMBER, ab, align="left", tracking=1)
        text(c, "celular · escola · aluno", 400, 655, 40, "black", INK, ab, align="left")
    acc = ep(t, C["13.c"], 0.4)
    text(c, "+ defende a PROIBIÇÃO", 400, 710, 34, "black", RED, acc, align="left")
    selo(c, 1300, 650, ep(t, C["13.d"], 0.4), "ASSUNTO CERTO, TESE ERRADA", AMBER, -4, 28)
    text(c, "conferir só as palavras = cair", W / 2, 800, 32, "black", RED, ep(t, C["13.e"], 0.4))


def b_nomes(c, t, C, B):
    frame(c, t, B["start"], "OBSERVAÇÃO", "RÁPIDA", GREEN)
    aa = ep(t, C["14.a"], 0.5)
    text(c, "livros e Redação do ENEM", 560, 300, 32, "bold", GRAY, aa)
    pill(c, "TEMA", 560, 370, INK2, size=40, a=aa, anchor="center", bounds=(0, 1920))
    text(c, "=", 960, 390, 80, "black", GRAY, aa)
    text(c, "nesta aula", 1360, 300, 32, "bold", GRAY, aa)
    pill(c, "ASSUNTO", 1360, 370, BLUE, size=40, a=aa, anchor="center", bounds=(0, 1920))
    text(c, "não se prenda ao nome", W / 2, 490, 32, "black", GREEN, ep(t, C["14.b"], 0.5))
    ac = ep(t, C["14.c"], 0.5)
    boxed(c, 300, 560, 560, 160, INK2, ac, 0.05)
    text_mid(c, "sobre o que FALA", 580, 640, 42, "black", INK2, ac)
    text_mid(c, "≠", 960, 640, 90, "black", RED, ac)
    boxed(c, 1060, 560, 560, 160, BLUE, ac, 0.08)
    text_mid(c, "o que DIZ", 1340, 640, 42, "black", BLUE, ac)


# ======================================================================
# nós fazemos
# ======================================================================

EXE = [("15.c", "16.a", "o transporte público", False),
       ("15.d", "16.b", "o transporte público deveria ser gratuito para estudantes", True),
       ("15.e", "16.c", "a violência no futebol", False)]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "AGORA É COM VOCÊ", "ASSUNTO OU TESE?", GREEN), ("16", "VAMOS CONFERIR", "ASSUNTO OU TESE?", GREEN)])
    card(c, *CARD_R)
    pill(c, "pause o vídeo e diga", 360, 210, AMBER, size=26, a=ep(t, C["15.a"], 0.4), anchor="center", bounds=(0, 1920))
    pill(c, "dica: teste da discordância", 1480, 210, GREEN, size=26, a=ep(t, C["15.b"], 0.4), anchor="center", bounds=(0, 1920))
    for k, (cq, cr, s, tese) in enumerate(EXE):
        a, d = rise(t, C[cq])
        y = 300 + k * 160 + d
        if a > 0:
            rrect(c, 220, y, 1200, 120, 20, "#F7F7F5", a)
            badge_num(c, k + 1, 290, y + 60, a, 28, bg=INK)
            para(c, "“" + s + "”", 350, y + 52 if len(s) > 40 else y + 72, 36 if len(s) <= 40 else 32, "black", INK, a, 1040, 40)
        ar = ep(t, C[cr], 0.4)
        if tese:
            pill(c, "TESE", 1560, y + 60, BLUE, size=34, a=ar, anchor="center", bounds=(0, 1920))
        else:
            pill(c, "ASSUNTO", 1560, y + 60, INK2, size=34, a=ar, anchor="center", bounds=(0, 1920))
    pause_timer(c, t, C["15.end"] - 1.7, 1560, 740)


# ======================================================================
# bloco E — ideia central × secundárias
# ======================================================================

def b_restaurante(c, t, C, B):
    head_seq(c, t, C, [("17", "AVALIAÇÃO DE", "RESTAURANTE", BLUE), ("18", "A FRASE QUE MANDA", "IDEIA CENTRAL", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["17.a"], 0.5)
    rrect(c, 520, 200, 880, 600, 24, "#FFFFFF", a0, shadow=True)
    for k in range(5):
        icon(c, "", 600 + k * 54, 260, 40, AMBER if k == 0 else LIGHT, a0)
    text(c, "avaliação · há 2 dias", 1360, 270, 22, "bold", GRAY, a0, align="right")
    ab = ep(t, C["17.b"], 0.4)
    text(c, "Não volto mais.", 960, 400, 64, "black", INK, ab)
    rows = [("17.c", "A comida chegou fria."), ("17.c", "Esperei uma hora.")]
    for j, (cue, s) in enumerate(rows):
        a = ep(t, C[cue] + j * 1.2, 0.4)
        text(c, s, 960, 560 + j * 70, 38, "bold", INK2, a)
    ad = ep(t, C["17.d"], 0.5)
    arrow(c, 620, 610, 620, 420, GREEN, ad, 5, 18, progress=ad)
    text(c, "por quê?", 600, 520, 28, "black", GREEN, ad, align="right")
    a18 = ep(t, C["18.t"], 0.5)
    if a18 > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(700, 330, 520, 100), 16, 16), paint(BLUE, a18, stroke=5))
    pill(c, "IDEIA CENTRAL", 1260, 380, BLUE, size=28, a=a18, bounds=(0, 1920))
    text(c, "a ideia que organiza todas as outras", 960, 760, 34, "black", BLUE, a18)


def b_tipos(c, t, C, B):
    frame(c, t, B["start"], "E NOS TEXTOS", "DA PROVA?", BLUE)
    data = [("19.a", "19.b", 220, "TEXTO ARGUMENTATIVO", "defende uma opinião", "ex.: artigo de jornal", "TESE"),
            ("20.a", "20.b", 1000, "TEXTO EXPOSITIVO", "só informa", "ex.: notícia", "INFORMAÇÃO PRINCIPAL")]
    foco = ep(t, C["20.c"], 0.5)
    for k, (ca, cb, x, tt, d1, d2, res) in enumerate(data):
        a, dy = rise(t, C[ca])
        if a <= 0:
            continue
        al = a * (1 - 0.5 * foco if k == 1 else 1)
        rrect(c, x, 220 + dy, 700, 560, 24, "#FFFFFF", al, shadow=True)
        if k == 0 and foco > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 220 + dy, 700, 560), 24, 24), paint(GREEN, foco, stroke=6))
        text(c, tt, x + 350, 300 + dy, 36, "black", BLUE, al)
        text(c, d1, x + 350, 370 + dy, 34, "bold", INK, al)
        text(c, d2, x + 350, 420 + dy, 28, "bold", GRAY, al)
        ab = ep(t, C[cb], 0.4) * al
        text(c, "ideia central =", x + 350, 560 + dy, 30, "bold", INK2, ab)
        pill(c, res, x + 350, 640 + dy, BLUE, size=32 if len(res) < 10 else 26, a=ab, anchor="center", bounds=(0, 1920))
    pill(c, "HOJE: o argumentativo", 570, 830, GREEN, size=26, a=foco, anchor="center", bounds=(0, 1920))


def b_mesa(c, t, C, B):
    head_seq(c, t, C, [("21", "IDEIAS SECUNDÁRIAS", "A MESA", BLUE), ("22", "AS PERNAS", "ARGUMENTO E EXEMPLO", BLUE),
                       ("23", "A MESA MONTADA", "CELULAR NA ESCOLA", BLUE)])
    card(c, *CARD_R)
    aa = ep(t, C["21.a"], 0.5) * (1 - ep(t, C["21.b"], 0.4))
    text(c, "IDEIAS SECUNDÁRIAS", W / 2, 430, 54, "black", INK, aa)
    text(c, "estão no texto para SUSTENTAR a central", W / 2, 510, 36, "bold", INK2, aa)
    ab = ep(t, C["21.b"], 0.5)
    a23 = ep(t, C["23.tese"], 0.6)
    top_txt = "TESE" if a23 < 0.5 else TESE_CEL
    top_a = ep(t, C["21.c"], 0.4)
    if C["23.tese"] - 0.3 < t < C["23.tese"] + 0.6:
        top_a *= abs(1 - 2 * clamp((t - C["23.tese"] + 0.3) / 0.9)) * 0.7 + 0.3
    p1, p2, p3 = (ep(t, C[f"23.p{k}"], 0.4) for k in (1, 2, 3))
    e1, e2, e3 = (ep(t, C[f"23.e{k}"], 0.4) for k in (1, 2, 3))
    g1, g2 = ep(t, C["22.a"], 0.4) * (1 - a23), ep(t, C["22.b"], 0.4) * (1 - a23)
    legs = [(1, "faz parte da vida dos estudantes" if p1 > 0 else "por quê?", max(p1, g1),
             "fora da escola, ninguém proíbe" if e1 > 0 else "onde isso se vê?", max(e1, g2)),
            (1, "proibir não gera autocontrole", p2, "o aluno usa às escondidas", e2),
            (1, "pode servir como ferramenta de aula", p3, "aula de checagem de notícias falsas", e3)]
    mesa(c, W / 2, 230, ab, top_txt, top_a, legs)
    ad = ep(t, C["21.d"], 0.4) * (1 - ep(t, C["22.a"], 0.4))
    pill(c, "PERNAS = o que sustenta", W / 2, 520, INK2, size=30, a=ad, anchor="center")
    ax = ep(t, C["23.x"], 0.4)
    if ax > 0:
        for k in range(3):
            arrow(c, W / 2 + LEG_X[k] + 220, 400, W / 2 + LEG_X[k] + 220, 345, GREEN, ax, 4, 14, progress=ax)


def b_concessao(c, t, C, B):
    frame(c, t, B["start"], "UMA PERNA QUE ENGANA", "A CONCESSÃO", AMBER)
    ab = ep(t, C["24.b"], 0.5)
    p1, pm, p2 = "É verdade que o celular distrai,", "MAS", "proibir não ensina nada."
    size = 46
    wt = text_w(p1, "black", size) + text_w(pm, "black", size) + text_w(p2, "black", size) + 60
    x0 = W / 2 - wt / 2
    y = 380
    ac = ep(t, C["24.c"], 0.4)
    ad = ep(t, C["24.d"], 0.4)
    text(c, p1, x0, y, size, "black", mix(INK, AMBER, ac), ab, align="left")
    xm = x0 + text_w(p1, "black", size) + 30
    text(c, pm, xm, y, size, "black", GREEN, ab, align="left")
    if ad > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xm - 10, y - 48, text_w(pm, "black", size) + 20, 66), 10, 10), paint(GREEN, ad, stroke=5))
    x2 = xm + text_w(pm, "black", size) + 30
    text(c, p2, x2, y, size, "black", mix(INK, BLUE, ad), ab, align="left")
    pill(c, "CONCESSÃO", x0 + text_w(p1, "black", size) / 2, 460, AMBER, size=28, a=ac, anchor="center", bounds=(0, 1920))
    text(c, "reconhece um ponto do outro lado...", W / 2, 600, 36, "bold", INK2, ac)
    text(c, "...antes de voltar à própria posição", W / 2, 655, 36, "bold", INK2, ep(t, C["24.c"] + 1.2, 0.4))
    pill(c, "PALAVRA-SINAL", xm + 40, 300, GREEN, size=24, a=ad, anchor="center", bounds=(0, 1920))
    pill(c, "POSIÇÃO DO AUTOR", x2 + text_w(p2, "black", size) / 2, 460, BLUE, size=28, a=ep(t, C["24.d"] + 0.8, 0.4), anchor="center", bounds=(0, 1920))
    arrow(c, W / 2 - 260, 760, W / 2 + 260, 760, GREEN, ad, 5, 18, progress=ad)
    text(c, "depois do MAS vem a posição", W / 2, 820, 30, "black", GREEN, ad)


def b_apoios(c, t, C, B):
    frame(c, t, B["start"], "JUNTANDO TUDO", "AS PERNAS DA MESA", BLUE)
    items = ["argumentos", "exemplos", "dados = números", "relatos = histórias", "concessões"]
    aa = ep(t, C["25.a"], 0.4)
    for k, s in enumerate(items):
        a = aa * ep(t, C["25.a"] + 0.55 * k, 0.4)
        pill(c, s, 380 + k * 290, 330 if k % 2 == 0 else 400, INK2, size=28, a=a, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["25.b"], 0.5)
    check_icon(c, 640, 560, 36, ab, GREEN)
    text(c, "SUSTENTAM a tese", 700, 580, 48, "black", GREEN, ab, align="left")
    ac = ep(t, C["25.c"], 0.5)
    check_icon(c, 640, 700, 36, ac, RED, "x")
    text(c, "SUBSTITUEM a tese", 700, 720, 48, "black", RED, ac, align="left")


def b_apagamento(c, t, C, B):
    head_seq(c, t, C, [("26", "TAMPO OU PERNA?", "O TESTE DO APAGAMENTO", PURPLE), ("27", "GUARDE A REGRA", "O TESTE DO APAGAMENTO", PURPLE)])
    card(c, *CARD_R)
    a0 = ep(t, C["26.t"], 0.5)
    tb = ep(t, C["26.b"], 0.6)
    td = ep(t, C["26.d"], 0.5)
    te = ep(t, C["26.e"], 0.8)
    a27 = ep(t, C["27.a"], 0.5)
    wob = 0.0
    if t > C["26.c"] and t < C["26.d"]:
        u = t - C["26.c"]
        wob = 3.5 * math.sin(u * 7) * math.exp(-u * 0.7)
    leg2 = 1 - tb * (1 - td)          # a perna 2 volta quando o tampo é apagado
    legs = [(1, "faz parte da vida dos estudantes", 1, "fora da escola, ninguém proíbe", 1),
            (leg2, "proibir não gera autocontrole", 1, "o aluno usa às escondidas", 1),
            (1, "pode servir como ferramenta de aula", 1, "aula de checagem de notícias falsas", 1)]
    mesa(c, W / 2, 230, a0 * (1 - a27), TESE_CEL, 1 - td, legs, wobble=wob, lift=td, fall=te)
    # borracha
    ea = ep(t, C["26.a"], 0.4) * (1 - a27)
    if ea > 0:
        ex = lerp(1560, W / 2 + 40, tb) if t < C["26.d"] else lerp(W / 2 + 40, W / 2 + 500, td)
        ey = lerp(220, 560, tb) if t < C["26.d"] else lerp(560, 280, td)
        rrect(c, ex - 50, ey - 30, 100, 60, 12, "#F9A8D4", ea, shadow=True)
        rrect(c, ex - 50, ey - 30, 40, 60, 10, "#60A5FA", ea)
    pill(c, "balança, mas fica de pé → era PERNA", W / 2, 180, GREEN, size=28, a=fw(t, C["26.c"], C["26.d"]) * (1 - a27), anchor="center")
    selo(c, W / 2, 780, te * (1 - a27), "NÃO SOBRA MESA", RED, -4, 40)
    regra(c, "Apague a frase: se o texto perde o rumo, ela é central.", 420, a27, 40)
    check_icon(c, 560, 570, 30, ep(t, C["27.a"] + 0.6, 0.4), BLUE)
    text(c, "perde o rumo → CENTRAL (tampo)", 610, 584, 38, "black", BLUE, ep(t, C["27.a"] + 0.6, 0.4), align="left")
    check_icon(c, 560, 680, 30, ep(t, C["27.b"], 0.4), INK2)
    text(c, "perde só um apoio → SECUNDÁRIA (perna)", 610, 694, 38, "black", INK2, ep(t, C["27.b"], 0.5), align="left")


def b_marcante(c, t, C, B):
    frame(c, t, B["start"], "A FRASE QUE MAIS", "CHAMA A ATENÇÃO", AMBER)
    aa = ep(t, C["28.a"], 0.5)
    ab = ep(t, C["28.b"], 0.5)
    k = 1 + 0.03 * math.sin(t * 6) * aa * (1 - ab)
    c.save(); c.translate(W / 2, 360); c.scale(k, k); c.translate(-W / 2, -360)
    if aa > 0:
        boxed(c, 360, 260, 1200, 200, AMBER, aa * (1 - 0.7 * ab), 0.15)
        text(c, "“tem aluno que olha o celular", W / 2, 345, 48, "black", INK, aa * (1 - 0.7 * ab))
        text(c, "100 vezes por aula!”", W / 2, 410, 48, "black", INK, aa * (1 - 0.7 * ab))
        if ab > 0:
            line(c, 380, 360, 1540, 360, RED, ab, 6, progress=ab)
    c.restore()
    text(c, "apague → a tese continua de pé", W / 2, 560, 40, "black", GREEN, ab)
    ac = ep(t, C["28.c"], 0.5)
    pill(c, "dado impressionante", 620, 680, AMBER, size=30, a=ac, anchor="center")
    pill(c, "história comovente", 1300, 680, AMBER, size=30, a=ep(t, C["28.c"] + 0.8, 0.4), anchor="center")
    text(c, "quase sempre são PERNA, não tampo", W / 2, 790, 40, "black", INK, ep(t, C["28.c"] + 1.6, 0.5))


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["Assunto é sobre o que fala; tese é o que diz.",
          "Se ninguém pode discordar, ainda não é a tese.",
          "Apague a frase: se o texto perde o rumo, ela é central."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["29", "39"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "29" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 46, "black", INK, a, align="left")


ERROS = [("30", "Responder com o ASSUNTO quando pedem a TESE", "a alternativa fala daquilo que o texto fala", "tem verbo e posição? se não, é etiqueta"),
         ("31", "Escolher o exemplo mais MARCANTE como central", "é o trecho que ficou na sua cabeça", "apague: a mesa fica de pé → era perna"),
         ("32", "Ficar com a alternativa que REPETE as palavras", "reconhecer as palavras dá segurança", "confira o que ela AFIRMA com elas")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS QUE MAIS DERRUBAM", RED)
    card(c, *CARD_R)
    for k in range(3):
        badge_num(c, k + 1, 880 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 330, 34, aa, RED, "x")
    para(c, err, 360, 345, 44, "black", RED, aa, 1300)
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 470, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 550, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 668, 34, ac, GREEN)
    text(c, fix, 360, 684, 42, "black", GREEN, ac, align="left")
    if sid == "32":
        selo(c, 1400, 780, ep(t, cue("c") + 2.2, 0.4), "ASSUNTO CERTO, TESE ERRADA", AMBER, -4, 26)


# ======================================================================
# questão 1 — leitura com marca-texto + alternativas
# ======================================================================

ALTS = [("A", "as bibliotecas de bairro deveriam ser substituídas por aplicativos de leitura, mais baratos.", "37.a", "diz o CONTRÁRIO", RED),
        ("B", "a leitura em tela reduziu o interesse da população pelos livros impressos.", "37.b", "vai ALÉM do texto", RED),
        ("C", "as bibliotecas de bairro têm valor como espaço público de convivência, e por isso fechá-las para economizar é um erro.", None, "", GREEN),
        ("D", "estudantes que se preparam para concursos precisam de silêncio para estudar.", "37.d", "só UM exemplo (uma perna)", RED),
        ("E", "as prefeituras gastam demais com cultura e deveriam rever seus orçamentos.", "38.e", "assunto certo, tese errada", AMBER)]

NOTAS = [("33.c1", "ASSUNTO", "bibliotecas de bairro", BLUE),
         ("34.c2", "PERNA", "lugar público e de graça", INK2),
         ("34.c3", "PERNAS", "três exemplos de quem usa", INK2),
         ("35.c4", "CONCESSÃO + MAS", "“parece racional...” MAS", GREEN),
         ("35.c4b", "TAMPO = TESE", "depois do mas: a posição", BLUE),
         ("35.c5", "PROPOSTA", "nasce da tese", INK2)]


def b_questao(c, t, C, B):
    alt_on = ep(t, C["36"], 0.7)
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "A TESE DE UM ARTIGO", BLUE)
    card(c, *CARD_R)
    # fase 1: leitura grande + notas na margem
    a1 = 1 - alt_on
    if a1 > 0:
        leitura(c, t, C, 200, 250, 1060, 34, 52, a1)
        text(c, "Texto elaborado para fins didáticos.", 200, 815, 20, "medium", GRAY, a1, align="left")
        for k, (cue, tt, s, col) in enumerate(NOTAS):
            a, d = rise(t, C[cue])
            a *= a1
            y = 230 + k * 100 + d
            if a > 0:
                rrect(c, 1320, y - 20, 420, 84, 14, mix("#FFFFFF", col, 0.08), a)
                c.drawRect(skia.Rect.MakeXYWH(1320, y - 20, 8, 84), paint(col, a))
                text(c, tt, 1344, y + 12, 22, "black", col, a, align="left", tracking=1)
                text(c, s, 1344, y + 48, 24, "bold", INK2, a, align="left")
    # fase 2: texto compacto à esquerda + alternativas à direita
    if alt_on > 0:
        leitura(c, t, C, 180, 260, 740, 24, 35, alt_on)
        text(c, "Texto elaborado para fins didáticos.", 180, 700, 18, "medium", GRAY, alt_on, align="left")
        text(c, "A tese defendida no texto é a de que", 980, 220, 28, "black", BLUE, alt_on * ep(t, C["36.t"], 0.4), align="left")
        aok = ep(t, C["38.ok"], 0.5)
        y = 270
        for L, s, cx, why, col in ALTS:
            a, d = rise(t, C[f"36.{L.lower()}"])
            a *= alt_on
            lines = wrap(s, "bold", 22, 690)
            hh = len(lines) * 28 + 14 + (30 if cx else 0)
            ok = cx is None
            if ok and aok > 0:
                rrect(c, 960, y - 30 + d, 800, hh + 10, 12, GREEN, 0.15 * aok)
            badge_num(c, L, 990, y - 8 + d, a, 20, bg=GREEN if ok and aok > 0.5 else INK)
            ax = ep(t, C[cx], 0.4) if cx else 0
            for j, ln in enumerate(lines):
                text(c, ln, 1030, y + d + j * 28, 22, "bold", INK, a * (1 - 0.5 * ax), align="left")
                if ax > 0:
                    strike(c, 1026, y + d + j * 28 - 8, 1034 + text_w(ln, "bold", 22), y + d + j * 28 - 8, ax, RED, ax)
            if ax > 0:
                pill(c, why, 1030, y + d + len(lines) * 28 + 4, col, size=18, a=ax, bounds=(0, 1920))
            y += hh + 18
        pause_timer(c, t, C["36.end"] - 1.7, 550, 760)
        result_box(c, "Letra C", 550, 790, 50, aok, GREEN)
        pill(c, "episódio 3: os nomes desses erros", 1360, 850, PURPLE, size=24, a=ep(t, C["38.x"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O RESUMO EM UMA FRASE", PURPLE)
    aa = ep(t, C["40.a"], 0.5)
    u = ep(t, C["40.a"] + 1.2, 1.4)
    for k in range(8):
        y = lerp(260 + k * 44, 470, u)
        w = lerp(700 - (k % 3) * 90, 900, u)
        line(c, 360, y, 360 + w, y, LINE, aa * (1 - u), 14)
    if u > 0.5:
        boxed(c, 330, 420, 960, 100, BLUE, aa * (u - 0.5) * 2, 0.08)
        text_mid(c, "1 frase", 810, 470, 44, "black", BLUE, aa * (u - 0.5) * 2)
    ab = ep(t, C["40.b"], 0.5)
    check_icon(c, 1420, 470, 40, ab, GREEN)
    text(c, "entendeu", 1480, 486, 44, "black", GREEN, ab, align="left")
    text(c, "o texto", 1480, 536, 44, "black", GREEN, ab, align="left")
    pill(c, "ep. 2 · o resumo em uma frase", W / 2, 720, PURPLE, size=34, a=ep(t, C["40.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["41.like"], C["41.sub"], C["41.bell"], C["41.com"], C["41.bye"], "Quantas das 3 frases do exercício você acertou?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, familia=b_familia, biblioteca=b_biblioteca, tabela=b_tabela,
              futebol=b_futebol, discordancia=b_discordancia, opostas=b_opostas, nomes=b_nomes, exercicio=b_exercicio,
              restaurante=b_restaurante, tipos=b_tipos, mesa=b_mesa, concessao=b_concessao, apoios=b_apoios,
              apagamento=b_apagamento, marcante=b_marcante, recap=b_recap, erros=b_erros, questao=b_questao,
              ponte=b_ponte, cta=b_cta)
