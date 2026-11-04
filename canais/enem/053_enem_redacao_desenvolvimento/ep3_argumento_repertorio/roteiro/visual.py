"""Visual — Redação ENEM, Desenvolvimento, Episódio 3: Argumento e repertório — explicar e comprovar (tema claro).
Usa o desenho compartilhado da série (desenvolvimento_visual.py): ícones e ficha das 5 etapas da entrega, rascunho com
caligrafia, alternativas, recap, erros e CTA.
Novo aqui: o VENDEDOR DO LIQUIDIFICADOR (afirmação → razão → selo de fora), a seta “COMO… → …” ligando causa e
consequência no argumento da seção 04, a lista de ESTRATÉGIAS da Cartilha em ícones pequenos com o selo “série própria”,
a NOTA FISCAL do repertório com três campos (QUEM/O QUÊ · CONTEÚDO · FONTE CERTA), o bolso da citação pronta e o texto
com trechos marcados por cor (rich) para a tabela “Como apresentar” e a resolução da Questão 4.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from desenvolvimento_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_desenvolvimento_ep3_argumento_repertorio.mp4"

ARG = PARTE["argumento"]
REP = PARTE["repertorio"]
TOP = PARTE["topico"]
ANA = PARTE["analise"]
FEC = PARTE["fechamento"]

LEI_FRACA = "A Lei nº 10.216/2001 é muito importante."
SO_NOME = "Machado de Assis escreveu O Alienista, obra muito importante da literatura brasileira."   # seção 09, V2
CAMPOS = ["QUEM / O QUÊ", "CONTEÚDO", "FONTE CERTA"]


# ======================================================================
# utilidades: texto com trechos coloridos (digitado e manuscrito)
# ======================================================================

def rich_layout(segs, size, maxw, peso="bold", hand_=False):
    """segs = [(texto, cor, realce)] → linhas de palavras [(palavra, seg, x)]"""
    wfun = (lambda s: hand_w(s, size)) if hand_ else (lambda s: text_w(s, peso, size))
    sp = wfun(" ")
    lines, cur, x = [], [], 0.0
    for k, seg in enumerate(segs):
        for wd in seg[0].split():
            ww = wfun(wd)
            if cur and x + ww > maxw:
                lines.append(cur); cur, x = [], 0.0
            cur.append((wd, k, x, ww))
            x += ww + sp
    if cur:
        lines.append(cur)
    return lines


def rich(c, segs, x, y, size, maxw, lh, a, peso="bold", hl=None, hl_col=None, fade=None, hand_=False, reveal=1.0):
    """desenha segs; hl[k] = alpha do marca-texto do trecho k (cor hl_col[k] ou a do trecho); fade[k] = esmaecer.
    Retorna (altura, caixas) com caixas[k] = [(x0, x1, y_base)] por linha."""
    lines = rich_layout(segs, size, maxw, peso, hand_)
    boxes = {}
    for j, ln in enumerate(lines):
        yy = y + j * lh
        for wd, k, wx, ww in ln:
            boxes.setdefault(k, [])
            if boxes[k] and abs(boxes[k][-1][2] - yy) < 1:
                x0, _, _ = boxes[k][-1]
                boxes[k][-1] = (x0, x + wx + ww, yy)
            else:
                boxes[k].append((x + wx, x + wx + ww, yy))
    if a > 0:
        for k, bl in boxes.items():
            h = (hl or {}).get(k, 0) if isinstance(hl, dict) else (hl[k] if hl and k < len(hl) else 0)
            if h > 0:
                col = (hl_col[k] if hl_col else None) or segs[k][1]
                for x0, x1, yy in bl:
                    rrect(c, x0 - 6, yy - size * 0.95, (x1 - x0 + 12) * clamp(h * 1.5), size * 1.32, 8, col, 0.20 * a * clamp(h))
        tot = sum(len(w[0]) for ln in lines for w in ln)
        done = reveal * tot
        for j, ln in enumerate(lines):
            yy = y + j * lh
            for wd, k, wx, ww in ln:
                if done <= 0:
                    break
                fk = (fade[k] if fade and k < len(fade) else 0)
                col = segs[k][1]
                r = clamp(done / max(1, len(wd)))
                if hand_:
                    hand(c, wd, x + wx, yy, size, col, a * (1 - 0.6 * fk), r)
                else:
                    text(c, wd, x + wx, yy, size, peso, col, a * (1 - 0.6 * fk), align="left")
                done -= len(wd)
    return len(lines) * lh, boxes


def rich_h(segs, size, maxw, lh, peso="bold", hand_=False):
    return len(rich_layout(segs, size, maxw, peso, hand_)) * lh


def mid(bl):
    """centro (x, y_base) da primeira linha de um trecho"""
    x0, x1, y = bl[0]
    return (x0 + x1) / 2, y


# ======================================================================
# componentes novos
# ======================================================================

def nota_fiscal(c, x, y, w, a, vals=None, val_a=None, status=None, lit=None, title="NOTA FISCAL", sub="REPERTÓRIO",
                size=24, rowmin=86, labels=None):
    """a nota fiscal do repertório: 3 campos (QUEM/O QUÊ · CONTEÚDO · FONTE CERTA). vals[k] = texto do campo;
    status[k] = True (✓ verde) / False (✗ vermelho) / None; lit[k] = destaque ocre. Retorna a altura."""
    if a <= 0:
        return 0
    labels = labels or CAMPOS
    vals = vals or [""] * 3
    val_a = val_a or [1.0] * 3
    status = status or [None] * 3
    lit = lit or [0.0] * 3
    rows = []
    for k in range(3):
        lines = wrap(vals[k], "bold", size, w - 130) if vals[k] else []
        rows.append((lines, max(rowmin, 52 + len(lines) * (size + 8))))
    h = 92 + sum(r[1] for r in rows) + 30
    # corpo com borda serrilhada
    shadow_rrect(c, x, y, w, h, 6, a)
    p = skia.Path()
    p.moveTo(x, y); p.lineTo(x + w, y); p.lineTo(x + w, y + h)
    n = int(w // 28)
    for k in range(n):
        p.lineTo(x + w - (k + 0.5) * w / n, y + h - 12); p.lineTo(x + w - (k + 1) * w / n, y + h)
    p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    c.drawPath(p, paint(REP, a, stroke=3))
    rrect(c, x, y, w, 76, 0, mix("#FFFFFF", REP, 0.85), a)
    text(c, title, x + 30, y + 50, 30, "black", "#FFFFFF", a, align="left", tracking=2)
    text(c, sub, x + w - 30, y + 48, 20, "black", "#FFF3D6", a, align="right", tracking=2)
    for k in range(7):
        c.drawRect(skia.Rect.MakeXYWH(x + w - 210 + k * 9, y + 14, 3 if k % 2 else 5, 22), paint("#FFFFFF", a * 0.0))
    yy = y + 92
    for k, (lines, rh) in enumerate(rows):
        if lit[k] > 0:
            rrect(c, x + 12, yy - 4, w - 24, rh - 6, 10, mix("#FFFFFF", REP, 0.16), a * lit[k])
        text(c, labels[k], x + 30, yy + 28, 19, "black", REP, a, align="left", tracking=2)
        if not lines:
            line(c, x + 30, yy + rh - 22, x + w - 100, yy + rh - 22, LIGHT, a, 2, dash=(8, 8))
        for j, ln in enumerate(lines):
            text(c, ln, x + 30, yy + 64 + j * (size + 8), size, "bold", INK, a * clamp(val_a[k]), align="left")
        if status[k] is not None:
            check_icon(c, x + w - 52, yy + rh / 2, 20, a, GREEN if status[k] else RED, "check" if status[k] else "x")
        if k < 2:
            line(c, x + 20, yy + rh - 4, x + w - 20, yy + rh - 4, LINE, a, 2, dash=(6, 6))
        yy += rh
    return h


def nota_h(vals, w, size=24, rowmin=86):
    return 92 + sum(max(rowmin, 52 + len(wrap(v, "bold", size, w - 130) if v else []) * (size + 8)) for v in vals) + 30


def liquidificador(c, cx, cy, s, a, run=0.0):
    """liquidificador neutro (copo + base); run > 0 = ondas de movimento"""
    if a <= 0:
        return
    col = "#5B6B86"
    p = skia.Path()
    p.moveTo(cx - 60 * s, cy - 110 * s); p.lineTo(cx + 60 * s, cy - 110 * s); p.lineTo(cx + 42 * s, cy + 20 * s)
    p.lineTo(cx - 42 * s, cy + 20 * s); p.close()
    c.drawPath(p, paint("#E3F2FD", a))
    c.drawPath(p, paint(col, a, stroke=5 * s))
    rrect(c, cx - 70 * s, cy - 126 * s, 140 * s, 20 * s, 6 * s, col, a)
    rrect(c, cx - 66 * s, cy + 20 * s, 132 * s, 84 * s, 16 * s, col, a)
    c.drawCircle(cx, cy + 62 * s, 16 * s, paint("#FFFFFF", a))
    c.drawCircle(cx, cy + 62 * s, 7 * s, paint(col, a))
    if run > 0:
        for k, dx in enumerate((-95, 95)):
            for j in range(3):
                xx = cx + dx * s + (j * 16 if dx > 0 else -j * 16) * s
                line(c, xx, cy - 70 * s, xx, cy - 20 * s, ARG, a * run * (0.9 - 0.25 * j), 5 * s)


def selo_redondo(c, cx, cy, r, a, col=REP):
    """selo de certificação genérico (prova que vem de fora)"""
    if a <= 0:
        return
    sc = 0.7 + 0.3 * ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.scale(sc, sc)
    n = 24
    p = skia.Path()
    for k in range(2 * n):
        ang = math.pi * k / n
        rr = r if k % 2 == 0 else r * 0.88
        px, py = rr * math.cos(ang), rr * math.sin(ang)
        (p.moveTo if k == 0 else p.lineTo)(px, py)
    p.close()
    c.drawPath(p, paint(col, a))
    c.drawCircle(0, 0, r * 0.72, paint("#FFFFFF", a))
    c.drawCircle(0, 0, r * 0.62, paint(col, a, stroke=3))
    check_icon(c, 0, -r * 0.08, r * 0.32, a, col)
    text(c, "SELO", 0, r * 0.45, r * 0.2, "black", col, a, tracking=2)
    c.restore()


def bolso(c, x, y, w, h, a, puxa=0.0):
    """bolso de calça com uma citação pronta saindo"""
    if a <= 0:
        return
    jeans, dark = "#3E5C8A", "#2C4468"
    # papel saindo do bolso
    py = y - 120 * ease_out(clamp(puxa))
    rrect(c, x + w * 0.2, py + 10, w * 0.6, 200, 6, "#FFFFFF", a, shadow=True)
    text(c, "“CITAÇÃO", x + w / 2, py + 70, 26, "black", AMBER, a)
    text(c, "PRONTA”", x + w / 2, py + 108, 26, "black", AMBER, a)
    text(c, "serve p/ qualquer tema", x + w / 2, py + 146, 18, "bold", GRAY, a)
    # bolso
    p = skia.Path()
    p.moveTo(x, y + 60); p.lineTo(x + w, y + 60); p.lineTo(x + w - 20, y + h - 60)
    p.lineTo(x + w / 2, y + h); p.lineTo(x + 20, y + h - 60); p.close()
    c.drawPath(p, paint(jeans, a))
    q = skia.Path()
    q.moveTo(x + 14, y + 74); q.lineTo(x + w - 14, y + 74); q.lineTo(x + w - 32, y + h - 68)
    q.lineTo(x + w / 2, y + h - 16); q.lineTo(x + 32, y + h - 68); q.close()
    pp = paint("#E8A317", a, stroke=3)
    pp.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
    c.drawPath(q, pp)
    rrect(c, x - 10, y + 50, w + 20, 22, 6, dark, a)


# ---- ícones pequenos das estratégias da Cartilha ----

def _ic_exemplos(c, cx, cy, s, a, col):
    for k in range(3):
        c.drawCircle(cx - 16 * s, cy - 14 * s + k * 14 * s, 3.5 * s, paint(col, a))
        line(c, cx - 6 * s, cy - 14 * s + k * 14 * s, cx + 20 * s, cy - 14 * s + k * 14 * s, col, a, 3.5 * s)


def _ic_dados(c, cx, cy, s, a, col):
    for k, hh in enumerate((14, 26, 36)):
        rrect(c, cx - 20 * s + k * 14 * s, cy + 18 * s - hh * s, 10 * s, hh * s, 2 * s, col, a)
    line(c, cx - 24 * s, cy + 19 * s, cx + 24 * s, cy + 19 * s, col, a, 3 * s)


def _ic_pesquisas(c, cx, cy, s, a, col):
    c.drawCircle(cx - 5 * s, cy - 5 * s, 14 * s, paint(col, a, stroke=4 * s))
    line(c, cx + 5 * s, cy + 5 * s, cx + 20 * s, cy + 20 * s, col, a, 5 * s)


def _ic_fatos(c, cx, cy, s, a, col):
    check_icon(c, cx, cy, 18 * s, a, col)


def _ic_citacoes(c, cx, cy, s, a, col):
    text_mid(c, "“ ”", cx, cy + 6 * s, 50 * s, "black", col, a)


def _ic_narrativas(c, cx, cy, s, a, col):
    p = skia.Path()
    p.moveTo(cx, cy - 12 * s); p.lineTo(cx - 24 * s, cy - 18 * s); p.lineTo(cx - 24 * s, cy + 16 * s); p.lineTo(cx, cy + 22 * s)
    p.lineTo(cx + 24 * s, cy + 16 * s); p.lineTo(cx + 24 * s, cy - 18 * s); p.close()
    c.drawPath(p, paint(col, a, stroke=3.5 * s))
    line(c, cx, cy - 12 * s, cx, cy + 22 * s, col, a, 3 * s)


def _ic_historia(c, cx, cy, s, a, col):
    p = skia.Path()
    p.moveTo(cx - 16 * s, cy - 22 * s); p.lineTo(cx + 16 * s, cy - 22 * s); p.lineTo(cx - 16 * s, cy + 22 * s)
    p.lineTo(cx + 16 * s, cy + 22 * s); p.close()
    c.drawPath(p, paint(col, a, stroke=3.5 * s))


def _ic_comparar(c, cx, cy, s, a, col):
    line(c, cx, cy - 20 * s, cx, cy + 20 * s, col, a, 3.5 * s)
    line(c, cx - 24 * s, cy - 12 * s, cx + 24 * s, cy - 12 * s, col, a, 3.5 * s)
    for dx in (-18, 18):
        c.drawArc(skia.Rect.MakeLTRB(cx + (dx - 10) * s, cy - 6 * s, cx + (dx + 10) * s, cy + 14 * s), 0, 180, True, paint(col, a))
    line(c, cx - 12 * s, cy + 22 * s, cx + 12 * s, cy + 22 * s, col, a, 3.5 * s)


IC_ESTR = [_ic_exemplos, _ic_dados, _ic_pesquisas, _ic_fatos, _ic_citacoes, _ic_narrativas, _ic_historia, _ic_comparar]


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], SERIE_SELO, "ARGUMENTO E REPERTÓRIO", ARG)
    card(c, *CARD_R)
    aa, ab, ac = (ep(t, C[f"01.{x}"], 0.5) for x in "abc")
    if aa > 0:
        rrect(c, 220, 260, 560, 300, 22, mix("#FFFFFF", GRAY, 0.10), aa, shadow=True)
        text(c, "OPINIÃO", 500, 380, 72, "black", GRAY, aa)
        text(c, "todo mundo tem", 500, 450, 32, "bold", INK2, aa)
        for k in range(3):
            bubble(c, "acho que…", 250 + k * 170, 580 + (k % 2) * 40, 170, LIGHT, aa * ep(t, C["01.a"] + 0.3 * k, 0.3),
                   size=22, fg=INK2)
    if ab > 0:
        rrect(c, 1140, 260, 560, 300, 22, mix("#FFFFFF", ARG, 0.12), ab, shadow=True)
        text(c, "ARGUMENTO", 1420, 380, 66, "black", ARG, ab)
        para(c, "a razão que faz o outro ACEITAR a sua opinião", 1420, 450, 30, "bold", INK2, ab, 480, 38, align="center")
    if ac > 0:
        arrow(c, 800, 410, 1120, 410, ARG, ac, 7, 22, progress=ac)
        pill(c, "1 FRASE: “porque…”", 960, 340, ARG, size=28, a=ac, anchor="center", bounds=(0, 1920))
        text(c, "transforma uma na outra", 960, 500, 26, "black", ARG, ac)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "argumento", "EXPLICAR uma afirmação", "com causa e consequência", ARG),
            ("02.b", "repertorio", "APRESENTAR um repertório", "com nome, conteúdo e atribuição corretos", REP)]
    for k, (cue, key, s1, s2, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + k * 220 + d
        icone_etapa(c, key, 360, y, a, 1.3)
        text(c, s1, 470, y - 4, 52, "black", col, a, align="left")
        text(c, s2, 470, y + 52, 32, "bold", INK2, a, align="left")
    pill(c, "cada palavra nova, uma de cada vez", W / 2, 770, BLUE, size=28, a=ep(t, C["02.c"], 0.4), anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "EPISÓDIO 2", PURPLE)
    aa, d = rise(t, C["03.a"])
    pill(c, "TÓPICO FRASAL", 220, 260 + d, TOP, size=30, a=aa, bounds=(0, 1920))
    para(c, "a frase (em geral a 1ª do parágrafo) que anuncia o que ele vai provar", 560, 272 + d, 34, "black", INK, aa,
         1120, 44)
    ab = ep(t, C["03.b"], 0.4)
    icone_etapa(c, "topico", 300, 450, ab, 1.1)
    text(c, "= ETIQUETA DO ITEM", 380, 466, 44, "black", TOP, ab, align="left")
    ac = ep(t, C["03.c"], 0.5)
    if ac > 0:
        rrect(c, 220, 560, 1480, 220, 18, "#FFFFFF", ac, shadow=True)
        rrect(c, 220, 560, 10, 220, 5, TOP, ac)
        pill(c, "EIXO 1 · desinformação", 260, 610, TOP, size=22, a=ac, bounds=(0, 1920))
    ad = ep(t, C["03.d"], 0.5)
    para(c, "“" + TOPICO_04 + "”", 260, 690, 34, "bold", INK, ad, 1400, 46)


# ======================================================================
# o vendedor do liquidificador e a analogia
# ======================================================================

def b_vendedor(c, t, C, B):
    frame(c, t, B["start"], "CONCRETO ANTES DO ABSTRATO", "O VENDEDOR", BLUE)
    q = lambda x: C[f"04.{x}"]
    aT = ep(t, q("t"), 0.5)
    ac = ep(t, q("c"), 0.5)
    liquidificador(c, 420, 470, 1.6, aT, run=ep(t, q("b"), 0.5))
    if aT > 0:
        rrect(c, 230, 660, 380, 22, 6, mix("#FFFFFF", GRAY, 0.4), aT)
    selo_redondo(c, 600, 330, 64, ac)
    rows = [("a", "“Este liquidificador é ótimo.”", "AFIRMAÇÃO", INK2),
            ("b", "“…porque tem motor de 1000 W.”", "RAZÃO", ARG),
            ("c", "selo do Inmetro", "PROVA DE FORA", REP)]
    for k, (cue, s, lab, col) in enumerate(rows):
        a, d = rise(t, q(cue))
        y = 230 + k * 150 + d
        if a > 0:
            rrect(c, 760, y, 900, 120, 18, mix("#FFFFFF", col, 0.10), a, shadow=True)
            rrect(c, 760, y, 10, 120, 5, col, a)
        text(c, s, 800, y + 76, 38, "black", INK, a, align="left")
        pill(c, lab, 1630, y + 60, col, size=22, a=a, anchor="right", bounds=(0, 1920))
    ad = ep(t, q("d"), 0.4)
    for k, (s, key) in enumerate((("afirmar", "topico"), ("explicar", "argumento"), ("comprovar", "repertorio"))):
        a = ep(t, q("d") + 0.3 * k, 0.4)
        x = 820 + k * 300
        pill(c, s, x, 730, PARTE[key], size=30, a=a, anchor="left", bounds=(0, 1920))
        if k < 2:
            arrow(c, x + 200, 730, x + 270, 730, GRAY, a * ad, 4, 12)


def b_analogia(c, t, C, B):
    frame(c, t, B["start"], "A ANALOGIA DA SÉRIE", "AS ETAPAS 2 E 3 DA ENTREGA", BLUE)
    q = lambda x: C[f"05.{x}"]
    aT = ep(t, q("t"), 0.5)
    aa = ep(t, q("a"), 0.4)
    shw = [1 - 0.7 * aa, 1, 1, 1 - 0.7 * aa, 1 - 0.7 * aa]
    lit = [0, aa, aa, 0, 0]
    ficha_entrega(c, 190, 180, 760, aT, show=shw, lit=lit, partes=1.0, rowh=104)
    for k, (cue, key, s1, s2) in enumerate((("b", "argumento", "POR QUE ESTÁ NA CAIXA", "= o ARGUMENTO"),
                                            ("c", "repertorio", "A NOTA FISCAL", "= o REPERTÓRIO"))):
        a, d = rise(t, q(cue))
        y = 300 + k * 260 + d
        icone_etapa(c, key, 1090, y, a, 1.2)
        text(c, s1, 1170, y - 6, 40, "black", PARTE[key], a, align="left")
        text(c, s2, 1170, y + 44, 34, "black", INK, a, align="left")
    ac = ep(t, q("c"), 0.4)
    text(c, "prova de fora, com nome e conteúdo certos", 1170, 660, 26, "bold", INK2, ac, align="left")


# ======================================================================
# bloco a: depois de afirmar, explicar (+ eu faço no rascunho)
# ======================================================================

def b_argumento(c, t, C, B):
    frame(c, t, B["start"], "DEPOIS DE AFIRMAR", "EXPLICAR", ARG)
    q = lambda x: C[f"06.{x}"]
    aT = ep(t, q("t"), 0.5)
    if aT > 0:
        rrect(c, 220, 200, 1480, 120, 16, mix("#FFFFFF", TOP, 0.08), aT)
        rrect(c, 220, 200, 10, 120, 5, TOP, aT)
        icone_etapa(c, "topico", 290, 260, aT, 0.6, disc=False)
        para(c, TOPICO_04, 350, 250, 30, "bold", INK, aT, 1300, 40)
    aa = ep(t, q("a"), 0.4)
    arrow(c, 960, 330, 960, 400, ARG, aa, 6, 18, progress=aa)
    ab = ep(t, q("b"), 0.4)
    if ab > 0:
        bubble(c, "por que a afirmação do tópico frasal PROCEDE?", 440, 420, 1040, ARG, ab, size=38)
    ac = ep(t, q("c"), 0.4)
    if ac > 0:
        boxed(c, 220, 600, 1080, 170, BLUE, ac, 0.07)
        text(c, "ARGUMENTO", 260, 652, 24, "black", BLUE, ac, align="left", tracking=2)
        text(c, "a razão que torna a tese aceitável", 260, 720, 42, "black", INK, ac, align="left")
    ad = ep(t, q("d"), 0.4)
    liquidificador(c, 1500, 680, 0.75, ad, run=ad)
    text(c, "motor de 1000 W", 1500, 800, 26, "black", ARG, ad)


PX, PY, PW, PH = 150, 160, 1620, 470
HX, HS, HLH, HMW = 270, 33, 54, 1420
ARG_SEGS = [("Como pouco se discute saúde mental nas escolas e nas famílias,", ARG),
            ("sintomas como a tristeza persistente ou a ansiedade intensa", INK),
            ("costumam ser interpretados como fraqueza de caráter,", ANA),
            ("e não como condições que têm tratamento.", INK)]
assert " ".join(s for s, _ in ARG_SEGS) == ARGUMENTO_04
TOP_LINES = hwrap(TOPICO_04, HS, HMW)
ARG_Y = PY + 170 + len(TOP_LINES) * HLH + 20


def rascunho_arg(c, t, a, r_top=1.0, r_arg=1.0, hl=(0, 0, 0, 0), ink=False, icons=(0, 0)):
    paper(c, PX, PY, PW, PH, a, lh=HLH, top=PY + 170 - 2 - 3 * HLH)
    text(c, "ENEM 2020 · D1 · eixo da desinformação", PX + 110, PY + 64, 24, "black", BLUE, a, align="left")
    text(c, DIDATICO, PX + 110, PY + 100, 18, "medium", AMBER, a, align="left")
    hand_para(c, TOPICO_04, HX, PY + 170, HS, PEN, a, HMW, HLH, reveal=r_top)
    segs = [(s, (col if ink else PEN), None) for s, col in ARG_SEGS]
    _, boxes = rich(c, segs, HX, ARG_Y, HS, HMW, HLH, a, hand_=True, reveal=r_arg, hl=list(hl),
                    hl_col=[ARG, None, ANA, None])
    if icons[0] > 0:
        icone_etapa(c, "topico", PX + 48, PY + 160, a * icons[0], 0.34)
    if icons[1] > 0:
        icone_etapa(c, "argumento", PX + 48, ARG_Y - 10, a * icons[1], 0.34)
    return boxes


def b_eufaco(c, t, C, B):
    sid = which(t, C, ["07", "08"])
    head_seq(c, t, C, [("07", "EU FAÇO · AO VIVO", "A ETIQUETA E O PORQUÊ", GREEN),
                       ("08", "EU FAÇO · AO VIVO", "CAUSA E CONSEQUÊNCIA", ARG)])
    a = ep(t, C["07"], 0.5)
    sp1 = phrase_span("07", "Em primeiro lugar, a desinformação", C["07.s1"], C["07.m"] - 0.5)
    r_top = wreveal(t, (C["07.s1"], C["07.m"] - 0.6))
    r_arg = wreveal(t, (C["07.s2"], C["07.end"] - 0.5))
    if sid == "07":
        rascunho_arg(c, t, a, r_top, r_arg, icons=(ep(t, C["07.s1"], 0.4), ep(t, C["07.s2"], 0.4)))
        am = ep(t, C["07.m"], 0.4) * (1 - ep(t, C["07.s2"] + 1.5, 0.5))
        if am > 0:
            bubble(c, "Por quê? O que acontece quando ninguém fala do assunto?", 560, 660, 860, GREEN, am, size=32)
        return
    q = lambda x: C[f"08.{x}"]
    hb, hc = ep(t, q("b"), 0.6), ep(t, q("c"), 0.6)
    boxes = rascunho_arg(c, t, 1.0, 1, 1, hl=(hb, 0, hc, 0), ink=True, icons=(1, 1))
    aa = ep(t, q("a"), 0.4)
    pill(c, "CAUSA E CONSEQUÊNCIA = uma coisa PROVOCA a outra", W / 2, 668, BLUE, size=26, a=aa, anchor="center",
         bounds=(0, 1920))
    # a seta COMO… → …
    y = 785
    if hb > 0:
        rrect(c, 260, y - 46, 560, 80, 16, mix("#FFFFFF", ARG, 0.14), hb)
        text(c, "CAUSA", 290, y - 12, 20, "black", ARG, hb, align="left", tracking=2)
        text(c, "COMO pouco se discute…", 290, y + 20, 30, "black", INK, hb, align="left")
    if hc > 0:
        arrow(c, 840, y - 6, 1000, y - 6, INK2, hc, 6, 20, progress=hc)
        rrect(c, 1020, y - 46, 640, 80, 16, mix("#FFFFFF", ANA, 0.14), hc)
        text(c, "CONSEQUÊNCIA", 1050, y - 12, 20, "black", ANA, hc, align="left", tracking=2)
        text(c, "…costumam ser interpretados", 1050, y + 20, 30, "black", INK, hc, align="left")
    ad = ep(t, q("d"), 0.4)
    if ad > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(240, y - 58, 1440, 106), 20, 20), paint(GREEN, ad, stroke=4))
        pill(c, "falta de informação PRODUZ a leitura preconceituosa", 1680, y + 84, GREEN, size=22, a=ad, anchor="right",
             bounds=(0, 1920))


def b_solto(c, t, C, B):
    head(c, t, B["start"], "LADO A LADO", "TÓPICO SOLTO × TÓPICO + ARGUMENTO", ARG)
    for x in (160, 990):
        card(c, x, 150, 770, 690)
    q = lambda x: C[f"09.{x}"]
    aa = ep(t, q("a"), 0.5)
    aT = ep(t, q("t"), 0.4)
    pill(c, "SÓ O TÓPICO FRASAL", 200, 200, RED, size=24, a=aT, bounds=(0, 1920))
    if aa > 0:
        fl = 8 * math.sin(t * 2.0)
        faixas_paragrafo(c, 214, 300 + fl, 690, 30, 40, [TOPICO_04], ["topico"], aa, faixa=[1], nums=False)
        text(c, "?", 545, 560, 120, "black", LIGHT, aa)
    ac = ep(t, q("c"), 0.4)
    selo(c, 545, 690, ac, "AFIRMAÇÃO SOLTA", RED, -5, 34)
    ad = ep(t, q("d"), 0.4)
    text(c, "= “é ótimo!” …e vai embora", 545, 790, 26, "black", RED, ad)
    ab = ep(t, q("b"), 0.5)
    pill(c, "TÓPICO + ARGUMENTO", 1030, 200, GREEN, size=24, a=aT, bounds=(0, 1920))
    if ab > 0:
        faixas_paragrafo(c, 1044, 290, 690, 27, 36, [TOPICO_04, ARGUMENTO_04], ["topico", "argumento"], ab, faixa=[1, 1],
                         nums=False)
        text(c, DIDATICO, 1030, 700, 16, "medium", AMBER, ab, align="left")
        check_icon(c, 1375, 770, 30, ab, GREEN)
        text(c, "tem um porquê", 1420, 781, 28, "black", GREEN, ab, align="left")


# ======================================================================
# bloco b: as estratégias da Cartilha (só a lista)
# ======================================================================

def b_estrategias(c, t, C, B):
    frame(c, t, B["start"], "CARTILHA DO PARTICIPANTE", "ESTRATÉGIAS ARGUMENTATIVAS", PURPLE)
    q = lambda x: C[f"10.{x}"]
    aa = ep(t, q("a"), 0.5)
    cartilha(c, 200, 210, ep(t, q("t"), 0.5), 0.0, 0.78)
    if aa > 0:
        para(c, "estratégia argumentativa = recurso para sustentar uma ideia", 200, 580, 26, "black", BLUE, aa, 300, 34)
    for k, s in enumerate(ESTRATEGIAS):
        a, d = rise(t, q(f"e{k + 1}"), 0.4)
        col_, row = k % 2, k // 2
        x, y = 560 + col_ * 590, 200 + row * 130 + d
        if a <= 0:
            continue
        rrect(c, x, y, 560, 110, 16, mix("#FFFFFF", PURPLE, 0.07), a, shadow=True)
        c.drawCircle(x + 56, y + 55, 36, paint(mix("#FFFFFF", PURPLE, 0.16), a))
        IC_ESTR[k](c, x + 56, y + 55, 0.9, a, PURPLE)
        lines = wrap(s, "black", 25, 430)
        y0 = y + 55 + 9 - (len(lines) - 1) * 16
        for j, ln in enumerate(lines):
            text(c, ln, x + 112, y0 + j * 32, 25, "black", INK, a, align="left")
    asl = ep(t, q("s"), 0.4)
    selo(c, 1440, 760, asl, "SÉRIE PRÓPRIA · Tipos de argumento", BLUE, -3, 26)
    text(c, "aqui: só a lista", 830, 772, 26, "black", GRAY, asl)


# ======================================================================
# bloco c: o repertório (definição) e a nota fiscal
# ======================================================================

def b_repertorio(c, t, C, B):
    frame(c, t, B["start"], "A NOTA FISCAL", "O REPERTÓRIO SOCIOCULTURAL", REP)
    q = lambda x: C[f"11.{x}"]
    aq = ep(t, q("t"), 0.5) * (1 - ep(t, q("a") - 0.3, 0.3))
    if aq > 0:
        icone_etapa(c, "repertorio", W / 2, 420, aq, 2.0)
        text(c, "o que conta como prova DE FORA?", W / 2, 620, 50, "black", REP, aq)
    aa, d = rise(t, q("a"))
    if aa > 0:
        boxed(c, 220, 200 + d, 1480, 110, BLUE, aa, 0.07)
        text(c, "REPERTÓRIO SOCIOCULTURAL", 260, 245 + d, 22, "black", BLUE, aa, align="left", tracking=2)
        text(c, "= o conhecimento que você traz de FORA da prova", 260, 290 + d, 34, "black", INK, aa, align="left")
    ab = ep(t, q("b"), 0.5)
    if ab > 0:
        boxed(c, 220, 350, 1480, 230, PURPLE, ab, 0.06)
        text(c, "NA DEFINIÇÃO DA CARTILHA", 260, 394, 20, "black", PURPLE, ab, align="left", tracking=2)
        para(c, "“" + REPERTORIO_DEF + "”", 260, 450, 34, "black", INK, ab, 1400, 44)
        for k, s in enumerate(("informação", "fato", "citação", "experiência vivida")):
            pill(c, s, 260 + [0, 230, 380, 560][k], 552, PURPLE, size=22, a=ab * ep(t, q("b") + 0.6 + 0.5 * k, 0.3),
                 bounds=(0, 1920))
    ac = ep(t, q("c"), 0.4)
    icone_etapa(c, "repertorio", 330, 720, ac, 1.0)
    text(c, "no parágrafo, ele", 420, 732, 32, "black", INK2, ac, align="left")
    pill(c, "COMPROVA", 730, 722, REP, size=30, a=ac, bounds=(0, 1920))
    text(c, "ou", 1000, 732, 32, "black", INK2, ac, align="left")
    pill(c, "ILUSTRA", 1060, 722, REP, size=30, a=ep(t, q("c") + 0.8, 0.4), bounds=(0, 1920))
    text(c, "o argumento", 1290, 732, 32, "black", INK2, ac, align="left")


def b_nota(c, t, C, B):
    frame(c, t, B["start"], "A NOTA FISCAL", "3 CAMPOS", REP)
    q = lambda x: C[f"12.{x}"]
    aT = ep(t, q("t"), 0.5)
    la = [ep(t, q(x), 0.4) for x in "abc"]
    lit = [la[k] * (1 - (la[k + 1] if k < 2 else ep(t, q("d"), 0.3))) for k in range(3)]
    nota_fiscal(c, 220, 190, 640, aT, lit=lit, rowmin=150)
    expl = [("a", "QUEM vendeu e O QUÊ", "nome"), ("b", "o que EXATAMENTE foi entregue", "conteúdo"),
            ("c", "de onde veio, de verdade", "atribuição")]
    ad = ep(t, q("d"), 0.5)
    for k, (cue, s, rep) in enumerate(expl):
        a, d = rise(t, q(cue))
        y = 345 + k * 150 + d
        text(c, s, 940, y, 34, "black", INK, a, align="left")
        if ad > 0:
            arrow(c, 940, y + 36, 1000, y + 36, REP, a * ad, 4, 12)
            pill(c, rep, 1020, y + 36, REP, size=24, a=a * ad, bounds=(0, 1920))
    ae = ep(t, q("e"), 0.4)
    if ae > 0:
        boxed(c, 940, 700, 760, 110, BLUE, ae, 0.07)
        text(c, "ATRIBUIÇÃO", 970, 740, 20, "black", BLUE, ae, align="left", tracking=2)
        text(c, "dizer de quem é a ideia: o autor ou a origem certa", 970, 786, 27, "black", INK, ae, align="left")


# ======================================================================
# bloco d: as três orientações contra o repertório de bolso
# ======================================================================

def b_bolso(c, t, C, B):
    frame(c, t, B["start"], "A NOTA FISCAL FALSA", "O REPERTÓRIO DE BOLSO", AMBER)
    q = lambda x: C[f"13.{x}"]
    aT = ep(t, q("t"), 0.5)
    bolso(c, 250, 430, 340, 330, aT, puxa=ep(t, q("t") + 0.6, 0.8))
    aa = ep(t, q("a"), 0.4)
    selo(c, 420, 790, aa, "REPERTÓRIO DE BOLSO", AMBER, -4, 28)
    if aa > 0:
        para(c, "citação decorada, pronta, encaixada em QUALQUER tema", 200, 250, 26, "black", AMBER, aa, 440, 34)
    ab = ep(t, q("b"), 0.5)
    if ab > 0:
        boxed(c, 700, 190, 1020, 620, PURPLE, ab, 0.05)
        text(c, "CARTILHA 2026 · 3 ORIENTAÇÕES", 740, 240, 22, "black", PURPLE, ab, align="left", tracking=2)
    for k, s in enumerate(ORIENTACOES_2026):
        a, d = rise(t, q(f"o{k + 1}"))
        y = 320 + k * 165 + d
        badge_num(c, k + 1, 770, y + 10, a, 30, bg=PURPLE)
        para(c, s, 830, y + 22, 34, "black", INK, a, 850, 44)
    aam = ep(t, q("o2") + 4.0, 0.4) * ep(t, q("o2"), 0.4)
    pill(c, "articular = amarrar", 830, 595, GREEN, size=22, a=aam, bounds=(0, 1920))


# ======================================================================
# bloco e: como apresentar (tabela da seção 05)
# ======================================================================

ALIENISTA_SEGS = [("“Em", INK, None), ("O Alienista, de Machado de Assis,", TOP, None),
                  ("o médico Simão Bacamarte recolhe à Casa Verde a maior parte da população de Itaguaí…”", REP, None)]
LEI_SEGS = [("“A", INK, None), ("Lei nº 10.216/2001,", TOP, None),
            ("que trata dos direitos das pessoas com transtornos mentais, redirecionou o modelo de assistência em saúde "
             "mental…”", REP, None)]
CF_SEGS = [("“Promulgada em 1988,", REP, None), ("a Constituição Federal…”", TOP, None)]
assert "".join(s for s, _, _ in ALIENISTA_SEGS).replace(" ", "") == APRESENTAR[0][1].replace(" ", "")
assert "".join(s for s, _, _ in LEI_SEGS).replace(" ", "") == APRESENTAR[1][1].replace(" ", "")
assert "".join(s for s, _, _ in CF_SEGS).replace(" ", "") == APRESENTAR[2][1].replace(" ", "")
TAB_SEGS = [ALIENISTA_SEGS, LEI_SEGS, CF_SEGS]


def tabela_apresentar(c, t, a, rows_a, hl, x=180, y=190, w=1560, size=29):
    """tabela “Como apresentar” (seção 05) com as 3 linhas; hl[k] = alpha do realce por cor da linha k"""
    if a <= 0:
        return
    rrect(c, x, y, w, 58, 12, mix("#FFFFFF", REP, 0.85), a)
    text(c, "COMO APRESENTAR", x + 30, y + 38, 20, "black", "#FFFFFF", a, align="left", tracking=2)
    text(c, "EXEMPLO (SEÇÃO 05)", x + 480, y + 38, 20, "black", "#FFFFFF", a, align="left", tracking=2)
    yy = y + 70
    for k, (form, _) in enumerate(APRESENTAR):
        segs = TAB_SEGS[k]
        hh = max(100, rich_h(segs, size, w - 520, size + 12) + 40)
        ak = a * clamp(rows_a[k])
        if ak > 0:
            rrect(c, x, yy, w, hh, 12, "#FFFFFF", ak, shadow=True)
            para(c, form, x + 30, yy + 48, 28, "black", REP, ak, 400, 34)
            rich(c, [(s, col if hl[k] > 0 else INK, None) for s, col, _ in segs], x + 480, yy + 50, size, w - 520,
                 size + 12, ak, hl={1: hl[k], 2: hl[k]} if k < 2 else {0: hl[k], 1: hl[k]})
        yy += hh + 14


def b_apresentar(c, t, C, B):
    sid = which(t, C, ["14", "15", "16"])
    head_seq(c, t, C, [("14", "COMO APRESENTAR", "QUEM/O QUÊ + CONTEÚDO EXATO", REP),
                       ("15", "LADO A LADO", "NOME × NOME + CONTEÚDO", REP),
                       ("16", "COMO APRESENTAR", "LEI · FATO HISTÓRICO", REP)])
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "14":
        card(c, *CARD_R)
        aa = ep(t, q("a"), 0.4)
        pill(c, "quem/o quê + conteúdo exato", 200, 220, REP, size=30, a=aa, bounds=(0, 1920))
        ab = ep(t, q("b"), 0.5)
        hc = ep(t, q("c"), 0.5)
        segs = [(s, col if hc > 0 else INK, None) for s, col, _ in ALIENISTA_SEGS]
        _, bx = rich(c, segs, 200, 330, 36, 900, 50, ab, hl={1: hc, 2: hc})
        vals = ["O Alienista, de Machado de Assis", "Simão Bacamarte recolhe à Casa Verde a maior parte da população de Itaguaí",
                "obra e autor certos"]
        nota_fiscal(c, 1150, 200, 560, ep(t, q("t"), 0.5), vals=vals, val_a=[hc] * 3,
                    status=[True, True, True] if hc > 0.5 else None, size=23, rowmin=80)
        pill(c, "QUEM / O QUÊ", 200, 560, TOP, size=24, a=hc, bounds=(0, 1920))
        pill(c, "CONTEÚDO EXATO", 440, 560, REP, size=24, a=ep(t, q("c") + 0.8, 0.4), bounds=(0, 1920))
        ad = ep(t, q("d"), 0.4)
        if ad > 0:
            boxed(c, 200, 650, 900, 130, BLUE, ad, 0.07)
            text(c, "DOMÍNIO PÚBLICO", 230, 690, 20, "black", BLUE, ad, align="left", tracking=2)
            text(c, "clássico livre: qualquer pessoa pode ler e conferir", 230, 745, 30, "black", INK, ad, align="left")
        return
    if sid == "15":
        for x in (160, 990):
            card(c, x, 150, 770, 690)
        pill(c, "NOME + CONTEÚDO", 200, 200, GREEN, size=24, bounds=(0, 1920))
        rich(c, [(s, col, None) for s, col, _ in ALIENISTA_SEGS], 214, 280, 28, 680, 38, 1.0)
        nota_fiscal(c, 230, 440, 630, 1.0, vals=["O Alienista, de Machado de Assis", "o que acontece na obra", "obra e autor certos"],
                    status=[True, True, True], size=22, rowmin=70, sub="")
        aa = ep(t, q("a"), 0.5)
        pill(c, "SÓ O NOME", 1030, 200, RED, size=24, a=aa, bounds=(0, 1920))
        para(c, "“" + SO_NOME + "”", 1044, 280, 28, "bold", INK, aa, 680, 38)
        text(c, DIDATICO, 1044, 410, 16, "medium", AMBER, aa, align="left")
        ab, ac = ep(t, q("b"), 0.4), ep(t, q("c"), 0.4)
        nota_fiscal(c, 1060, 440, 630, aa, vals=["O Alienista, de Machado de Assis" if ab > 0 else "", "", ""],
                    status=[True if ab > 0.5 else None, False if ac > 0.5 else None, None], size=22, rowmin=70, sub="",
                    lit=[0, ac, 0])
        ad = ep(t, q("d"), 0.4)
        selo(c, 1375, 772, ad, "SEM A LISTA DO QUE FOI ENTREGUE", RED, -3, 22)
        return
    card(c, *CARD_R)
    ra = [1.0, ep(t, q("a"), 0.5), ep(t, q("c"), 0.5)]
    hl = [0.0, ep(t, q("b"), 0.6), ep(t, q("d"), 0.6)]
    tabela_apresentar(c, t, 1.0, ra, hl)
    ae = ep(t, q("e"), 0.4)
    pill(c, "promulgada = oficialmente publicada", 1700, 790, BLUE, size=26, a=ae, anchor="right", bounds=(0, 1920))
    ac = ep(t, q("c"), 0.4)
    pill(c, "data segura = a que você tem certeza", 220, 790, GREEN, size=26, a=ac, bounds=(0, 1920))


# ======================================================================
# bloco f: prefira a paráfrase; na dúvida, não atribua
# ======================================================================

def b_parafrase(c, t, C, B):
    sid = which(t, C, ["17", "18"])
    head_seq(c, t, C, [("17", "PREFIRA A PARÁFRASE", "CITAÇÃO × PARÁFRASE", GREEN),
                       ("18", "NA DÚVIDA", "NÃO ATRIBUA", GREEN)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "17":
        aq = ep(t, q("t"), 0.5) * (1 - ep(t, q("a") - 0.3, 0.3))
        if aq > 0:
            text(c, "“   ”", W / 2, 470, 220, "black", mix("#FFFFFF", BLUE, 0.6), aq)
            text(c, "aquelas frases famosas, entre aspas?", W / 2, 620, 50, "black", BLUE, aq)
        for k, (cue, lab, s, big) in enumerate((("a", "CITAÇÃO", "as palavras EXATAS de alguém, entre aspas", "“ ”"),
                                                ("b", "PARÁFRASE", "a mesma ideia, com as SUAS palavras", "≈"))):
            a, d = rise(t, q(cue))
            x = 220 + k * 760
            if a > 0:
                boxed(c, x, 200 + d, 720, 220, BLUE, a, 0.06)
            text(c, big, x + 90, 340 + d, 110, "black", BLUE, a)
            text(c, lab, x + 190, 280 + d, 26, "black", BLUE, a, align="left", tracking=2)
            para(c, s, x + 190, 340 + d, 32, "black", INK, a, 500, 40)
        ac = ep(t, q("c"), 0.4)
        if ac > 0:
            boxed(c, 220, 460, 1480, 130, AMBER, ac, 0.08)
            text(c, "ARMADILHA", 250, 500, 20, "black", AMBER, ac, align="left", tracking=2)
            text(c, "citação longa entre aspas: ocupa linhas e raramente sai exata", 250, 555, 32, "black", INK, ac,
                 align="left")
        for k, s in enumerate(("parafraseie a ideia", "atribua corretamente", "linhas para a ANÁLISE")):
            a = ep(t, q("d") + 0.6 * k, 0.4)
            x = 260 + k * 500
            pill(c, s, x, 700, GREEN if k < 2 else ANA, size=30, a=a, bounds=(0, 1920))
            if k < 2:
                arrow(c, x + 400, 700, x + 470, 700, GRAY, a, 4, 12)
        return
    aT = ep(t, q("t"), 0.5)
    text(c, "?", 380, 500, 260, "black", mix("#FFFFFF", AMBER, 0.8), aT)
    text(c, "não tem certeza da autoria ou do conteúdo?", 560, 300, 36, "black", INK, aT, align="left")
    aa = ep(t, q("a"), 0.4)
    selo(c, 860, 420, aa, "NÃO ATRIBUA", GREEN, -4, 44)
    ab = ep(t, q("b"), 0.4)
    if ab > 0:
        boxed(c, 560, 510, 1100, 100, GREEN, ab, 0.08)
        text_mid(c, "apresente a ideia como ARGUMENTO SEU", 1110, 560, 36, "black", GREEN, ab)
    ac = ep(t, q("c"), 0.4)
    if ac > 0:
        check_icon(c, 600, 710, 26, ac, GREEN)
        text(c, "ideia sua, bem explicada", 640, 722, 30, "black", GREEN, ac, align="left")
        text(c, ">", 1060, 724, 40, "black", INK2, ac)
        check_icon(c, 1120, 710, 26, ac, RED, "x")
        text(c, "nota fiscal com o nome errado", 1160, 722, 30, "black", RED, ac, align="left")


# ======================================================================
# nós fazemos: a lei sem conteúdo
# ======================================================================

EX_X, EX_Y, EX_W, EX_H = 150, 160, 1620, 690
EXS = 38


def b_exercicio(c, t, C, B):
    sid = which(t, C, ["19", "20"])
    head_seq(c, t, C, [("19", "NÓS FAZEMOS", "LEI + O QUE ELA DETERMINA", AMBER), ("20", "NÓS FAZEMOS", "CONFERINDO", GREEN)])
    paper(c, EX_X, EX_Y, EX_W, EX_H, 1.0, lh=60, top=EX_Y + 160 - 2 - 2 * 60)
    text(c, "ENEM 2020 · repertório", EX_X + 110, EX_Y + 64, 24, "black", BLUE, 1.0, align="left")
    aa = ep(t, C["19.a"], 0.4)
    x0, y0 = 270, EX_Y + 160
    hand(c, LEI_FRACA, x0, y0, EXS, PEN, aa)
    wl = hand_w(LEI_FRACA, EXS)
    w_nome = hand_w("A Lei nº 10.216/2001", EXS)
    ab = ep(t, C["19.b"], 0.4)
    if ab > 0:
        underline(c, x0 + hand_w("A ", EXS), x0 + w_nome, y0 + 12, GREEN, ab, ab, 5)
        pill(c, "nome ✓", x0 + 80, y0 + 60, GREEN, size=20, a=ab, bounds=(0, 1920))
        aq = ep(t, C["19.b"] + 1.2, 0.4)
        underline(c, x0 + w_nome + 10, x0 + wl, y0 + 12, RED, aq, aq, 5)
        pill(c, "conteúdo?", x0 + w_nome + 40, y0 + 60, RED, size=20, a=aq, bounds=(0, 1920))
    if sid == "19":
        ac = ep(t, C["19.c"], 0.4)
        if ac > 0:
            boxed(c, 270, 520, 900, 110, GREEN, ac, 0.08)
            text(c, "MODELO", 300, 560, 20, "black", GREEN, ac, align="left", tracking=2)
            text(c, "lei + o que ela determina", 300, 608, 38, "black", INK, ac, align="left")
        pause_timer(c, t, C["19.p"] + 0.3, EX_X + EX_W - 140, EX_Y + EX_H - 150)
        return
    aa2 = ep(t, C["20.a"], 0.4)
    strike(c, x0 + w_nome + 10, y0 - 10, x0 + wl, y0 - 10, aa2, RED, aa2)
    sp = phrase_span("20", "A Lei número dez mil duzentos e dezesseis,", C["20.s"], C["20.b"] - 0.4)
    r = wreveal(t, (C["20.s"], C["20.b"] - 0.4))
    hb = ep(t, C["20.b"], 0.6)
    segs = [(s, PEN, None) for s, _, _ in LEI_SEGS]
    segs[0] = ("A", PEN, None)
    segs[2] = (segs[2][0].rstrip("”"), PEN, None)
    _, bx = rich(c, segs, x0, y0 + 2 * 60 + 20, EXS, 1400, 60, 1.0, hand_=True, reveal=r, hl={2: hb}, hl_col=[None, None, REP])
    if hb > 0:
        pill(c, "o que a lei FAZ = conteúdo", 270, 655, REP, size=24, a=hb, bounds=(0, 1920))
        text(c, "tabela da seção 05", 760, 665, 20, "medium", GRAY, hb, align="left")
    ac = ep(t, C["20.c"], 0.4)
    if ac > 0:
        boxed(c, 270, 712, 1380, 96, GREEN, ac, 0.08)
        text_mid(c, "a sua versão: diga o que a lei determina, só com o que você tem certeza", 960, 760, 30, "black",
                 GREEN, ac)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Afirmou? Explique o porquê.", "Repertório é nota fiscal: nome e conteúdo certos.",
          "Paráfrase curta, atribuição certa; na dúvida, não atribua."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("21", "32"), FRASES, cols=[ARG, REP, GREEN])


ERROS = [("22", "Afirmar e passar direto para o exemplo, sem explicar", "o exemplo parece provar tudo sozinho",
          "opinião repetida não é argumento: diga por que a afirmação procede"),
         ("23", "Citar o nome da obra sem dizer o que ela mostra", "um nome famoso impressiona",
          "repertório sem uso tende a não ser produtivo: resuma o conteúdo e use"),
         ("24", "Decorar citação longa e errar palavras ou autoria", "aspas parecem prova de estudo",
          "paráfrase curta e atribuição correta: gaste as linhas na análise")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


# ======================================================================
# questão 8 (a estratégia usada)
# ======================================================================

Q8_ANTES = "Em um parágrafo sobre o tema do Enem 2025, lê-se:"
Q8_TRECHO = [("“Assim como", ARG, None),
             ("as cidades brasileiras foram redesenhadas, ao longo do século XX, para a circulação dos automóveis,", INK, None),
             ("precisam agora", ARG, None), ("ser adaptadas para quem caminha mais devagar.”", INK, None)]
Q8_DEPOIS = "A estratégia argumentativa predominante nesse trecho é a"
ALT8 = [("A", "citação de autoridade.", "25.A", "27.xa", "nenhum especialista citado", RED),
        ("B", "apresentação de dado estatístico.", "25.B", "27.xb", "nenhum número", RED),
        ("C", "narrativa ilustrativa.", "25.C", "27.xc", "nenhuma história com personagens", RED),
        ("D", "comparação entre situações.", "26.D", None, "", GREEN),
        ("E", "definição de conceito.", "26.E", "27.xe", "nenhum termo definido", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "A ESTRATÉGIA USADA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["25.a"], 0.4)
    aq = ep(t, C["25.t"], 0.4) * (1 - ep(t, C["25.a"] - 0.3, 0.3))
    if aq > 0:
        text(c, "2 questões no estilo ENEM", W / 2, 470, 60, "black", BLUE, aq)
        for k, s in enumerate(("Questão 8 · a estratégia usada", "Questão 4 · repertório que trabalha")):
            pill(c, s, W / 2, 560 + 70 * k, BLUE if k == 0 else REP, size=28, a=aq, anchor="center", bounds=(0, 1920))
    text(c, "QUESTÃO 8", 190, 220, 18, "black", GRAY, aa, align="left", tracking=2)
    para(c, Q8_ANTES, 190, 270, 28, "black", INK, aa, 760, 36)
    aok = ep(t, C["27.ok"], 0.5)
    hh, _ = rich(c, [(s, col if aok > 0 else INK, None) for s, col, _ in Q8_TRECHO], 190, 330, 28, 740, 38, aa,
                 hl={0: aok, 2: aok})
    ab = ep(t, C["25.b"], 0.4)
    para(c, Q8_DEPOIS, 190, 330 + hh + 30, 28, "black", INK, ab, 760, 36)
    if aok > 0:
        pill(c, "compara: automóvel × envelhecimento", 190, 770, ARG, size=22, a=aok, bounds=(0, 1920))
    alts_panel(c, t, C, ALT8, 1010, 260, 680, 30, "27.ok", "D", 8, gap_why=36, why_size=20)
    pause_timer(c, t, C["26.end"] - 1.9, 1600, 700)
    aL = ep(t, C["27.ok"] + 3.0, 0.4)
    pill(c, "uma das estratégias da lista da Cartilha", 1030, 790, PURPLE, size=22, a=aL, bounds=(0, 1920))
    questao_rotulo(c, aa)


# ======================================================================
# questão 4 (repertório que trabalha)
# ======================================================================

Q4_ENUN = ("Para o tema do Enem 2025, “Perspectivas acerca do envelhecimento na sociedade brasileira”, o trecho de "
           "desenvolvimento em que o repertório é usado de forma produtiva é:")
Q4_A_SEGS = [("O Estatuto da Pessoa Idosa atribui à família, à sociedade e ao poder público o dever de assegurar à pessoa "
              "idosa direitos como a convivência comunitária.", REP, None),
             ("Muitas cidades, porém, não têm calçadas acessíveis nem espaços de convivência,", ARG, None),
             ("o que confina idosos em casa e transforma esse direito em promessa.", ANA, None)]
Q4_A = " ".join(s for s, _, _ in Q4_A_SEGS)
ALT4 = [("A", Q4_A, "28.A", None, "", GREEN),
        ("B", "Segundo Aristóteles, o homem é um animal político. Portanto, o envelhecimento deve ser discutido por todos.",
         "29.B", "31.xb", "repertório de bolso (Cartilha 2026)", AMBER),
        ("C", "O Estatuto da Pessoa Idosa é uma lei brasileira. Ele é muito importante para o país.", "29.C", "31.xc",
         "cita a lei sem dizer o que determina nem usá-la", RED),
        ("D", "Como diz o ditado, quem espera sempre alcança. Por isso, os idosos devem ter paciência.", "29.D", "31.xd",
         "ditado sem relação; conclusão desrespeitosa", RED),
        ("E", "Conforme o texto motivador da prova, a população idosa cresceu no Brasil.", "29.E", "31.xe",
         "só retoma a coletânea: não é repertório", RED)]
MARCAS4 = [("m1", "CONTEÚDO DA LEI", REP), ("m2", "CONFRONTO COM A REALIDADE", ARG), ("m3", "CONSEQUÊNCIA", ANA)]


def b_q4(c, t, C, B):
    sid = which(t, C, ["28", "29", "30", "31"])
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "REPERTÓRIO QUE TRABALHA", BLUE)
    card(c, *CARD_R)
    if sid == "30":
        text(c, "QUESTÃO 4 · ALTERNATIVA A", 200, 220, 18, "black", GREEN, 1.0, align="left", tracking=2)
        hl = [ep(t, C[f"30.{m}"], 0.6) for m, _, _ in MARCAS4]
        segs = [(s, col if hl[k] > 0 else INK, None) for k, (s, col, _) in enumerate(Q4_A_SEGS)]
        hh, bx = rich(c, segs, 200, 300, 38, 1520, 56, 1.0, hl=hl)
        for k, (m, lab, col) in enumerate(MARCAS4):
            a, d = rise(t, C[f"30.{m}"])
            x = 200 + k * 520
            if a > 0:
                rrect(c, x, 640 + d, 490, 70, 14, mix("#FFFFFF", col, 0.16), a)
                rrect(c, x, 640 + d, 10, 70, 5, col, a)
                badge_num(c, k + 1, x + 46, 675 + d, a, 20, bg=col)
                text(c, lab, x + 80, 685 + d, 25, "black", col, a, align="left")
        af = ep(t, C["30.f"], 0.4)
        pill(c, "→ uma perspectiva sobre o envelhecimento no Brasil", W / 2, 780, GREEN, size=26, a=af, anchor="center",
             bounds=(0, 1920))
        questao_rotulo(c, 1.0)
        return
    at = ep(t, C["28.t"], 0.4)
    text(c, "QUESTÃO 4", 190, 215, 18, "black", GRAY, at, align="left", tracking=2)
    para(c, Q4_ENUN, 190, 258, 25, "black", INK, at, 1540, 33)
    alts_panel(c, t, C, ALT4, 210, 372, 1500, 26, "30.ok", "A", 6)
    pause_timer(c, t, C["29.end"] - 1.9, 1640, 740)
    questao_rotulo(c, at)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O PRODUTO FUNCIONANDO", ANA)
    aa = ep(t, C["33.a"], 0.4)
    icone_etapa(c, "repertorio", 420, 430, aa, 1.8)
    text(c, "nota fiscal", 420, 560, 30, "black", REP, aa)
    text(c, "não basta", 420, 610, 34, "black", RED, ep(t, C["33.a"] + 0.8, 0.4))
    ab = ep(t, C["33.b"], 0.4)
    arrow(c, 560, 450, 760, 450, GRAY, ab, 6, 18, progress=ab)
    icone_etapa(c, "analise", 960, 430, ab, 1.8)
    text(c, "produto funcionando", 960, 560, 30, "black", ANA, ab)
    text(c, "na casa do cliente", 960, 605, 26, "bold", INK2, ab)
    ac = ep(t, C["33.c"], 0.4)
    arrow(c, 1110, 450, 1310, 450, GRAY, ac, 6, 18, progress=ac)
    icone_etapa(c, "fechamento", 1500, 430, ac, 1.8)
    text(c, "recibo assinado", 1500, 560, 30, "black", FEC, ac)
    pill(c, "Ep. 4 · a ANÁLISE e o FECHAMENTO", W / 2, 750, GREEN, size=30, a=ac, anchor="center")


def b_cta(c, t, C, B):
    cta_dev(c, t, C, "34", "Qual referência você já citou só pelo nome?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, vendedor=b_vendedor, analogia=b_analogia,
              argumento=b_argumento, eufaco=b_eufaco, solto=b_solto, estrategias=b_estrategias, repertorio=b_repertorio,
              nota=b_nota, bolso=b_bolso, apresentar=b_apresentar, parafrase=b_parafrase, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q8=b_q8, q4=b_q4, ponte=b_ponte, cta=b_cta)
