"""Visual — Redação ENEM, Introdução, Episódio 3: A ponte e o teste da retirada (tema claro).
Usa o desenho da série (introducao_visual.py: etiqueta de 4 peças, rascunho com caligrafia, alternativas, recap, erros, CTA).
Novo: CARTÃO-POSTAL genérico × MAPA com a rua até a casa · TESTE DA RETIRADA animado (a referência é puxada para fora
do parágrafo; sem ponte, o texto fica igual; com ponte, a frase seguinte desmorona) · FÓRMULA DE PONTE em 3 setas.
Cores: azul = definição/referência · verde = método (a ponte) · âmbar = armadilha (bolso) · vermelho = erro · roxo = Cartilha.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from introducao_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_introducao_ep3_ponte_teste_retirada.mp4"

# trechos da seção 04 (EXATOS) e versões faladas (para sincronizar a caligrafia com a voz)
SEM1 = "A Constituição Federal de 1988 é conhecida como Constituição Cidadã."
SEM2 = "Nesse sentido, a herança africana é muito importante para o Brasil."
COM1 = ("A Constituição Federal de 1988 reconhece como patrimônio cultural brasileiro os bens que guardam a memória dos "
        "diferentes grupos formadores da sociedade.")
COM2 = ("Entre esses grupos, porém, os povos africanos e seus descendentes ainda veem sua contribuição tratada como "
        "folclore ou restrita a datas comemorativas, o que revela a distância entre o reconhecimento legal e a "
        "valorização efetiva.")
F1988 = "A Constituição Federal de mil novecentos e oitenta e oito"
LEI = "A Lei nº 9.534/1997 tornou gratuitos o registro civil de nascimento e a primeira certidão."
LEI_F = ("A Lei nove mil quinhentos e trinta e quatro, de mil novecentos e noventa e sete, tornou gratuitos o registro civil "
         "de nascimento e a primeira certidão.")
ARIST = ("“Segundo Aristóteles, o ser humano é um animal político. Dessa forma, o envelhecimento é uma questão relevante "
         "na sociedade brasileira.”")
TRECHOS = "Trechos elaborados para fins didáticos."
QUOTE = "“poderia ser retirada da introdução sem alterar significativamente a compreensão do texto”"


def ease_in(x):
    x = clamp(x)
    return x * x


def ease_in_out(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def span(sid, written, spoken, ta, tb):
    return phrase_span(sid, spoken or written, ta, tb)


def sub_box(lines, x, y, lh, size, sub):
    """(x, y_linha, largura) de cada pedaço de `sub` nas linhas manuscritas (sub não pode quebrar de linha)"""
    out = []
    for k, ln in enumerate(lines):
        i = ln.find(sub)
        if i >= 0:
            out.append((x + hand_w(ln[:i], size), y + k * lh, hand_w(sub, size)))
    return out


def marca_texto(c, boxes, size, col, a, p=1.0):
    for bx, by, bw in boxes:
        rrect(c, bx - 6, by - size * 0.95, (bw + 12) * clamp(p), size * 1.35, 8, col, 0.22 * a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM · INTRODUÇÃO", "A PONTE E O TESTE DA RETIRADA", BLUE)
    card(c, *CARD_R)
    anos = [("2016", -5), ("2020", 2), ("2024", 7)]
    for k, (ano, rot) in enumerate(anos):
        a = ep(t, C["01.a"] + 0.35 * k, 0.4)
        x = 220 + k * 250
        paper(c, x, 260 + k * 30, 470, 400, a, lh=48, top=330 + k * 30, rot=rot)
        if a > 0:
            c.save(); c.translate(x + 235, 460 + k * 30); c.rotate(rot); c.translate(-(x + 235), -(460 + k * 30))
            pill(c, f"TEMA {ano}", x + 110, 305 + k * 30, BLUE, size=20, a=a, bounds=(0, 1920))
            hand_para(c, "Segundo Aristóteles, o homem é um animal político...", x + 110, 390 + k * 30, 30, PEN, a, 330, 48)
            c.restore()
    ab = ep(t, C["01.b"], 0.5)
    cartilha(c, 1290, 230, ab, 0.0, 1.0)
    ac = ep(t, C["01.c"], 0.4)
    selo(c, 1440, 770, ac, "REPERTÓRIO DE BOLSO", AMBER, -5, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "rua", "escrever a FRASE-PONTE", "que faz a referência trabalhar pelo seu tema"),
            ("02.b", "mapa", "TESTAR a referência", "ela está trabalhando ou é só enfeite?")]
    for k, (cue, key, s1, s2) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + k * 220 + d
        icone_peca(c, key, 360, y, a, 1.3)
        text(c, s1, 470, y - 4, 52, "black", MOV[key] if key == "rua" else BLUE, a, align="left")
        text(c, s2, 470, y + 56, 32, "bold", INK2, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "A ETIQUETA COMPLETA", PURPLE)
    a = ep(t, C["03.a"], 0.5)
    ab, ad = ep(t, C["03.b"], 0.5), ep(t, C["03.d"], 0.6)
    etiqueta_intro(c, 200, 190, 860, a, show=[1, 0.25 + 0.75 * ad, 0.25, 0.25], lit=[ab * (1 - ad), ad, 0, 0],
                   perguntas=0.0, movs=1.0, rowh=110)
    if ad > 0:
        selo(c, 760, 451, ad, "NOVA", GREEN, 6, 30)
    portas = ["lei ou obra", "fato histórico", "dado", "conceito"]
    text(c, "AS 4 PORTAS DO MAPA", 1420, 270, 22, "black", BLUE, ab, tracking=2)
    for k, s in enumerate(portas):
        ak = ep(t, C["03.c"] + 0.4 * k, 0.4) * (1 - 0.6 * ad)
        y = 330 + k * 100
        rrect(c, 1240, y, 360, 76, 14, mix("#FFFFFF", BLUE, 0.10), ak)
        rrect(c, 1240, y, 14, 76, 6, BLUE, ak)
        text_mid(c, s, 1430, y + 38, 32, "black", BLUE, ak)


# ======================================================================
# cartão-postal × mapa com a rua
# ======================================================================

def postal(c, x, y, w, h, a):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 12, "#FFFFFF", a, shadow=True)
    px, py, pw, ph = x + 22, y + 22, w - 44, h - 110
    rrect(c, px, py, pw, ph, 8, "#9CC9F5", a)
    rrect(c, px, py + ph * 0.55, pw, ph * 0.45, 0, "#F2C98A", a)
    c.drawCircle(px + pw * 0.78, py + ph * 0.25, 34, paint("#FFD54A", a))
    for k, (bw, bh) in enumerate([(50, 120), (70, 170), (44, 90), (80, 140), (56, 200), (40, 110), (66, 150)]):
        bx = px + 20 + k * (pw - 40) / 7
        rrect(c, bx, py + ph * 0.62 - bh, bw, bh, 3, "#5B6B86", a * 0.9)
    text(c, "LEMBRANÇAS DE QUALQUER LUGAR", x + w / 2, y + h - 38, 24, "black", INK2, a, tracking=1)


def mapa_rua(c, x, y, w, h, a, rua=0.0, casa=0.0):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 12, "#F1F4EC", a, shadow=True)
    for k in range(1, 5):
        line(c, x + k * w / 5, y + 10, x + k * w / 5, y + h - 10, "#DDE3D3", a, 3)
        line(c, x + 10, y + k * h / 5, x + w - 10, y + k * h / 5, "#DDE3D3", a, 3)
    # avenida principal (o mapa geral)
    rrect(c, x + 10, y + h * 0.78, w - 20, 40, 6, "#C9CED6", a)
    text(c, "AVENIDA PRINCIPAL", x + w - 40, y + h * 0.78 + 29, 18, "black", GRAY, a, align="right", tracking=1.5)
    # rua de acesso
    if rua > 0:
        p = skia.Path()
        p.moveTo(x + w * 0.28, y + h * 0.80); p.lineTo(x + w * 0.28, y + h * 0.45); p.lineTo(x + w * 0.70, y + h * 0.45)
        p.lineTo(x + w * 0.70, y + h * 0.30)
        pm = skia.PathMeasure(p, False)
        L = pm.getLength()
        seg = skia.Path(); pm.getSegment(0, L * clamp(rua), seg, True)
        c.drawPath(seg, paint(GREEN, a, stroke=26, cap_round=True))
        c.drawPath(seg, paint("#FFFFFF", a * 0.8, stroke=3, cap_round=True))
    if casa > 0:
        ic_casa(c, x + w * 0.70, y + h * 0.22, 1.5, a * casa, MOV["tese"])


def b_postal(c, t, C, B):
    sid = which(t, C, ["04", "05"])
    head_seq(c, t, C, [("04", "IMAGINE", "CARTÃO-POSTAL × MAPA", BLUE), ("05", "NA REDAÇÃO", "BOLSO × PONTE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    postal(c, 210, 220, 640, 430, aa)
    ab = ep(t, C["04.b"], 0.4)
    if ab > 0 and sid == "04":
        check_icon(c, 800, 250, 34, ab, RED, "x")
        text(c, "serve para qualquer cidade · não leva a casa nenhuma", 530, 710, 26, "bold", RED, ab)
    ac = ep(t, C["04.c"], 0.5)
    mapa_rua(c, 1010, 220, 640, 430, ac, rua=prog(t, C["04.c"] + 1.0, 2.2), casa=ep(t, C["04.c"] + 2.4, 0.4))
    ad = ep(t, C["04.d"], 0.4)
    if sid == "04":
        check_icon(c, 1600, 250, 34, ad, GREEN)
        text(c, "você usa de verdade", 1330, 710, 28, "bold", GREEN, ad)
        return
    # 05: rótulos da redação
    a_rec = ep(t, C["05.b"], 0.4)
    pill(c, "RECORTE = o endereço completo", 1330 + 120, 250, BLUE, size=24, a=a_rec, anchor="center", bounds=(0, 1920))
    a_b = ep(t, C["05.c"], 0.4)
    check_icon(c, 800, 250, 34, a_b, RED, "x")
    selo(c, 530, 720, a_b, "REPERTÓRIO DE BOLSO", AMBER, -4, 34)
    text(c, "referência decorada que serve para qualquer tema", 530, 800, 24, "bold", INK2, a_b)
    a_p = ep(t, C["05.d"], 0.4)
    selo(c, 1330, 720, a_p, "PONTE = RUA DE ACESSO", GREEN, 3, 34)
    text(c, "a frase que leva do mapa geral até a porta", 1330, 800, 24, "bold", INK2, a_p)


# ======================================================================
# o erro mais comum + Cartilha
# ======================================================================

def b_cartilha(c, t, C, B):
    frame(c, t, B["start"], "O ERRO MAIS COMUM", "FALTA DE LIGAÇÃO", RED)
    aa = ep(t, C["06.a"], 0.4)
    text(c, "não é a referência em si", 560, 250, 34, "black", GRAY, aa)
    strike(c, 380, 238, 740, 238, aa, RED, ep(t, C["06.a"] + 0.6, 0.4))
    ab = ep(t, C["06.b"], 0.4)
    text(c, "é a FALTA DE LIGAÇÃO com o tema", 1240, 250, 38, "black", RED, ab)
    ac = ep(t, C["06.c"], 0.5)
    cartilha(c, 230, 330, ac, 0.0, 0.62)
    boxed(c, 470, 320, 1190, 270, PURPLE, ac, 0.07)
    text(c, "CARTILHA 2026 · sobre A República, de Platão, na introdução:", 510, 370, 24, "black", PURPLE, ac, align="left")
    ad = ep(t, C["06.d"], 0.5)
    para(c, QUOTE, 510, 440, 36, "black", INK, ad, 1110, 46)
    af = ep(t, C["06.f"], 0.5)
    if af > 0:
        rrect(c, 230, 640, 1460, 160, 22, mix("#FFFFFF", GREEN, 0.12), af)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(230, 640, 1460, 160), 22, 22), paint(GREEN, af, stroke=4))
        text(c, "TESTE DA RETIRADA", 960, 700, 40, "black", GREEN, af, tracking=2)
        text(c, "se a referência sai e nada muda, ela não estava trabalhando", 960, 760, 32, "bold", INK, af)


# ======================================================================
# eu faço: teste da retirada sem ponte e com ponte
# ======================================================================

PX, PY, PW, PH = 200, 230, 1520, 580   # folha de rascunho
TX, TW, LH, SZ = 320, 1300, 62, 38     # texto manuscrito


def tema_topo(c, a):
    text(c, "ENEM 2024", 200, 210, 18, "black", GRAY, a, align="left", tracking=2)
    text(c, "“" + TEMA24 + "”", 330, 210, 24, "black", BLUE, a, align="left")


def pull_out(c, t, t0, draw, a, dx=900, dy=-60):
    """desenha a referência; a partir de t0 ela é puxada para fora (sobe, gira e some)"""
    p = ease_in_out(prog(t, t0, 1.0)) if t0 is not None else 0.0
    if p >= 1:
        return 1.0
    c.save()
    c.translate(dx * p, dy * p + -40 * math.sin(math.pi * p))
    c.rotate(8 * p)
    draw(a * (1 - 0.85 * p))
    c.restore()
    return p


def b_sem(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · TRECHO 1", "SEM PONTE", AMBER)
    q = lambda x: C[f"07.{x}"]
    tema_topo(c, ep(t, q("a"), 0.4))
    ap = ep(t, q("b"), 0.4)
    paper(c, PX, PY, PW, PH, ap, lh=LH, top=PY + 70)
    text(c, TRECHOS, PX, PY + PH + 30, 16, "medium", GRAY, ap, align="left")
    l1 = hwrap(SEM1, SZ, TW)
    r1 = wreveal(t, span("07", SEM1, F1988, q("c"), q("d")))
    r2 = wreveal(t, span("07", SEM2, None, q("d"), q("e")))

    def ref(a):
        if a <= 0:
            return
        rrect(c, TX - 16, PY + 70 + 14, hand_w(l1[0], SZ) + 32, LH * len(l1) + 20, 12, mix("#FFFFFF", BLUE, 0.16), a)
        hand_para(c, SEM1, TX, PY + 70 + LH, SZ, PEN, a, TW, LH, r1)
        if ep(t, q("i"), 0.4) > 0:
            pass
    p = pull_out(c, t, q("f"), ref, ap)
    y2 = PY + 70 + LH * (len(l1) + 1)
    hl = ep(t, q("g"), 0.4)
    if hl > 0:
        for k, ln in enumerate(hwrap(SEM2, SZ, TW)):
            marca_texto(c, [(TX, y2 + k * LH, hand_w(ln, SZ))], SZ, AMBER, hl)
    hand_para(c, SEM2, TX, y2, SZ, PEN, ap, TW, LH, r2)
    ah = ep(t, q("h"), 0.4)
    selo(c, 1240, 620, ah, "NADA MUDOU", RED, -5, 46)
    ai = ep(t, q("i"), 0.4)
    if ai > 0:
        pill(c, "a referência era só um RÓTULO", 520, 640, AMBER, size=30, a=ai, anchor="center", bounds=(0, 1920))


def crumble(c, lines, x, y, lh, size, a, p, seed=3):
    """linhas manuscritas que desmoronam (cada palavra cai com giro próprio)"""
    for k, ln in enumerate(lines):
        xx = x
        for j, w_ in enumerate(ln.split(" ")):
            ww = hand_w(w_ + " ", size)
            d = 0.12 * ((j * 7 + k * 3 + seed) % 5)
            q = ease_in(clamp((p - d) / (1 - 0.5)))
            c.save()
            c.translate(xx + ww / 2, y + k * lh + 260 * q * q + 30 * q)
            c.rotate((((j * 13 + k * 5) % 9) - 4) * 9 * q)
            hand(c, w_, -ww / 2, 0, size, mix(PEN, RED, clamp(p * 2)), a * (1 - 0.7 * q))
            c.restore()
            xx += ww


def b_com(c, t, C, B):
    sid = which(t, C, ["08", "09"])
    head_seq(c, t, C, [("08", "EU FAÇO · TRECHO 2", "COM PONTE", GREEN), ("09", "EU FAÇO · TRECHO 2", "TESTE DA RETIRADA", GREEN)])
    q8 = lambda x: C[f"08.{x}"]
    q = lambda x: C[f"09.{x}"]
    tema_topo(c, 1.0)
    paper(c, PX, PY, PW, PH, 1.0, lh=LH, top=PY + 70)
    text(c, TRECHOS, PX, PY + PH + 30, 16, "medium", GRAY, 1.0, align="left")
    l1 = hwrap(COM1, SZ, TW)
    l2 = hwrap(COM2, SZ, TW)
    r1 = wreveal(t, span("08", COM1, F1988 + " reconhece como patrimônio cultural brasileiro os bens que guardam a memória "
                                         "dos diferentes grupos formadores da sociedade.", q8("c"), q8("d")))
    r2 = wreveal(t, span("08", COM2, None, q8("d"), C["08.end"]))
    y1 = PY + 70 + LH
    ai_ = ep(t, q("i"), 0.6) if sid == "09" else 0.0   # volta: a referência retorna para a explicação

    def ref(a):
        if a <= 0:
            return
        rrect(c, TX - 16, y1 - LH + 14, TW + 32, LH * len(l1) + 20, 12, mix("#FFFFFF", BLUE, 0.16), a)
        hand_para(c, COM1, TX, y1, SZ, PEN, a, TW, LH, r1)
    if sid == "09" and ai_ <= 0:
        pull_out(c, t, q("f"), ref, 1.0)
    else:
        ref(1.0 if sid == "08" else ai_)
    y2 = y1 + LH * len(l1) + 10
    hc = ep(t, q("h"), 0.3) if sid == "09" else 0.0
    fall = prog(t, q("h"), 1.6) * (1 - ai_)
    if sid == "09" and hc > 0 and ai_ < 1:
        c.save(); c.clipRect(skia.Rect.MakeXYWH(PX, PY, PW, PH))
        crumble(c, l2, TX, y2, LH, SZ, 1.0 - ai_, fall)
        c.restore()
        selo(c, 1240, 700, hc * (1 - ai_), "DESMORONOU!", RED, -5, 46)
    else:
        if sid == "09":
            ag = ep(t, q("g"), 0.4) * (1 - ai_)
            if ag > 0:
                for sub_, (xx_, yy_) in (("Entre esses grupos", (0, 0)), ("o reconhecimento legal", (0, 0))):
                    bx = sub_box(l2, TX, y2, LH, SZ, sub_)
                    marca_texto(c, bx, SZ, RED, ag)
                    for bx_, by_, bw_ in bx:
                        text(c, "?", bx_ + bw_ + 4, by_ - SZ, 40, "black", RED, ag, align="left")
        hand_para(c, COM2, TX, y2, SZ, PEN, 1.0, TW, LH, r2 if sid == "08" else 1.0)
    if sid == "09" and ai_ > 0:
        aj, ak = ep(t, q("j"), 0.4), ep(t, q("k"), 0.4)
        marca_texto(c, sub_box(l1, TX, y1, LH, SZ, "reconhece como patrimônio cultural brasileiro"), SZ, BLUE, ai_)
        pill(c, "INTERPRETADA: o que ela reconhece", PX + PW - 20, PY + 34, BLUE, size=22, a=ai_, anchor="right", bounds=(0, 1920))
        for sub_ in ("tratada como folclore ou restrita a datas comemorativas,",):
            marca_texto(c, sub_box(l2, TX, y2, LH, SZ, sub_), SZ, AMBER, aj)
            for part in ("tratada como folclore", "restrita a datas comemorativas", "restrita a", "datas comemorativas"):
                marca_texto(c, sub_box(l2, TX, y2, LH, SZ, part), SZ, AMBER, aj)
        pill(c, "CONFRONTADA com a realidade", PX + 340, PY + PH + 40, AMBER, size=24, a=aj, bounds=(0, 1920))
        for part in ("a distância entre o", "reconhecimento legal e a valorização efetiva"):
            marca_texto(c, sub_box(l2, TX, y2, LH, SZ, part), SZ, GREEN, ak)
        pill(c, "CONTRASTE → já prepara a TESE", PX + PW, PY + PH + 40, GREEN, size=24, a=ak, anchor="right", bounds=(0, 1920))


# ======================================================================
# fórmula, expressões, autores clássicos
# ======================================================================

FORM = [("10.a", "REFERÊNCIA", "10.d", "a Constituição de 1988", BLUE),
        ("10.b", "O QUE ELA MOSTRA", "10.e", "reconhece a memória dos grupos formadores", BLUE),
        ("10.c", "COMO SE LIGA AO RECORTE", "10.f", "mas a herança africana ainda é tratada como folclore", GREEN)]


def b_formula(c, t, C, B):
    frame(c, t, B["start"], "MÉTODO", "A FÓRMULA DA PONTE", GREEN)
    metodo_selo(c, 1550, 230, ep(t, C["10.m"], 0.4), rot=4)
    for k, (cue, tit, cue2, ex, col) in enumerate(FORM):
        a, d = rise(t, C[cue])
        x = 200 + k * 530
        y = 340 + d
        rrect(c, x, y, 450, 140, 20, mix("#FFFFFF", col, 0.12), a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 450, 140), 20, 20), paint(col, a, stroke=4))
        badge_num(c, k + 1, x + 225, y, a, 26, bg=col)
        para(c, tit, x + 225, y + 70 if text_w(tit, "black", 34) < 400 else y + 62, 34, "black", col, a, 400, 40, align="center")
        if k < 2:
            arrow(c, x + 462, y + 70, x + 520, y + 70, GREEN, a, 6, 18, progress=ep(t, C[FORM[k + 1][0]], 0.4))
        a2 = ep(t, C[cue2], 0.4)
        if a2 > 0:
            paper(c, x, 540, 450, 220, a2, lh=50, top=560, margin=False)
            hand_para(c, ex, x + 30, 620, 30, PEN, a2, 390, 46, wreveal(t, (C[cue2], C[cue2] + 1.6)))


EXPR = [("11.c", "de modo semelhante"), ("11.d", "essa realidade, no entanto"), ("11.e", "tal cenário se repete"),
        ("11.f", "ao contrário do que prevê a lei")]


def b_expressoes(c, t, C, B):
    frame(c, t, B["start"], "COMO MARCAR A PASSAGEM", "CONECTIVOS DA PONTE", GREEN)
    aa = ep(t, C["11.a"], 0.4)
    boxed(c, 300, 210, 1320, 110, BLUE, aa, 0.08)
    text_mid(c, "CONECTIVO = a palavrinha que liga uma ideia à outra", 960, 265, 36, "black", BLUE, aa)
    ab = ep(t, C["11.b"], 0.4)
    text(c, "do contexto → ao problema", 960, 390, 30, "bold", INK2, ab)
    for k, (cue, s) in enumerate(EXPR):
        a, d = rise(t, C[cue])
        x = 330 + (k % 2) * 650
        y = 440 + (k // 2) * 130 + d
        rrect(c, x, y, 610, 96, 18, mix("#FFFFFF", GREEN, 0.12), a, shadow=True)
        icone_peca(c, "rua", x + 56, y + 48, a, 0.62, disc=False)
        text_mid(c, "“" + s + "”", x + 340, y + 48, 32, "black", GREEN, a)
    pill(c, "a série de Conectivos aprofunda", 960, 790, PURPLE, size=24, a=ep(t, C["11.g"], 0.4), anchor="center",
         bounds=(0, 1920))


def busto(c, cx, cy, nome, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy - 60, 56, paint("#E9E4D8", a))
    c.drawCircle(cx, cy - 60, 56, paint(GRAY, a, stroke=4))
    rrect(c, cx - 90, cy + 6, 180, 110, 50, "#E9E4D8", a)
    rrect(c, cx - 110, cy + 110, 220, 40, 6, "#D2CABA", a)
    text(c, nome, cx, cy + 190, 30, "black", INK, a)


def b_filosofo(c, t, C, B):
    frame(c, t, B["start"], "ESTÁ PROIBIDO?", "PLATÃO E ARISTÓTELES", PURPLE)
    a0 = ep(t, C["12"], 0.5)
    busto(c, 360, 400, "Platão", a0)
    busto(c, 620, 400, "Aristóteles", ep(t, C["12"] + 0.4, 0.5))
    aa = ep(t, C["12.a"], 0.3)
    selo(c, 490, 700, aa, "NÃO!", GREEN, -6, 60)
    rows = [("12.b", "nenhum autor é proibido", GREEN), ("12.c", "o problema é o ENCAIXE GENÉRICO", AMBER),
            ("12.d", "com a rua até o recorte, qualquer referência legítima trabalha", GREEN)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 290 + k * 140 + d
        check_icon(c, 860, y - 12, 26, a, RED if col == AMBER else GREEN, "x" if col == AMBER else "check")
        para(c, s, 910, y, 36, "black", col, a, 780, 44)
    pill(c, "critérios do repertório: série Repertório sociocultural", 1300, 770, PURPLE, size=22,
         a=ep(t, C["12.e"], 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

def b_nos(c, t, C, B):
    head(c, t, B["start"], "NÓS FAZEMOS", "ESCREVA A FRASE-PONTE", GREEN)
    q = lambda x: C[f"13.{x}"]
    aa = ep(t, q("a"), 0.4)
    text(c, "ENEM 2021", 200, 210, 18, "black", GRAY, aa, align="left", tracking=2)
    text(c, "“" + TEMA21 + "”", 330, 210, 24, "black", BLUE, aa, align="left")
    paper(c, PX, PY, PW, PH, aa, lh=LH, top=PY + 70)
    ab = ep(t, q("b"), 0.4)
    l1 = hwrap(LEI, SZ, TW)
    y1 = PY + 70 + LH
    rrect(c, TX - 16, y1 - LH + 14, TW + 32, LH * len(l1) + 20, 12, mix("#FFFFFF", BLUE, 0.16), ab)
    hand_para(c, LEI, TX, y1, SZ, PEN, ab, TW, LH, wreveal(t, span("13", LEI, LEI_F, q("b"), q("c"))))
    ac = ep(t, q("c"), 0.4)
    y2 = y1 + LH * (len(l1) + 1)
    for k in range(2):
        line(c, TX, y2 + k * LH, TX + TW - 200 * k, y2 + k * LH, GREEN, ac, 4, dash=[14, 10])
    pen_draw(c, TX + 450 + 500 * prog(t, q("c"), 3.0), y2 + LH - 80, PEN, ac, -35, 0.8)
    pill(c, "contraponha a LEI à REALIDADE", TX, y2 + LH * 2 + 20, GREEN, size=28, a=ac, bounds=(0, 1920))
    pause_timer(c, t, q("p") + 0.3, 1560, 700)
    pill(c, "guarde a sua frase: a questão confere", 960, PY + PH + 40, AMBER, size=24, a=ep(t, q("d"), 0.4),
         anchor="center", bounds=(0, 1920))


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["A ponte é a rua: leva do mapa até a porta.", "Referência → o que mostra → como se liga ao recorte.",
          "Tirou e nada mudou? Não estava trabalhando."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("14", "24"), FRASES, cols=[GREEN, GREEN, AMBER])


ERROS = [("15", "Citar e ABANDONAR a referência", "a citação está lá, bonita, e dá impressão de repertório",
          "sem ponte, ela não trabalha: faça a referência mostrar algo sobre o recorte"),
         ("16", "Achar que o problema é o AUTOR CLÁSSICO", "a Cartilha criticou justamente Platão e Aristóteles",
          "o que ela criticou foi o ENCAIXE GENÉRICO, não o autor"),
         ("17", "Usar o conectivo sem relação de verdade (“Nesse sentido...” e outro assunto)",
          "o conectivo dá cara de texto ligado", "conectivo não cria ligação: só MARCA a que existe na ideia")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


# ======================================================================
# questões 7 e 3
# ======================================================================

ALT7 = [("A", "Nesse sentido, as leis brasileiras são muito numerosas.", "18.A", "20.xa", "generaliza para as leis em geral", RED),
        ("B", "Além disso, o Brasil tem uma das maiores populações do mundo.", "18.B", "20.xb", "sem relação com o recorte", RED),
        ("C", "Por isso, todos os brasileiros já têm acesso pleno à cidadania.", "19.C", "20.xc", "a realidade contradiz: elimina o problema", RED),
        ("D", "Dessa forma, a cidadania surgiu na Grécia Antiga.", "19.D", "20.xd", "assunto amplo, fora do Brasil", RED),
        ("E", "Ainda assim, há brasileiros sem certidão de nascimento — e, sem ela, invisíveis para o Estado e afastados de direitos básicos.", "19.E", None, "", GREEN)]


def lado_questao(c, t, C, n, ano, tema, inicio, enun, a, strike_a=0.0, extra=None):
    text(c, f"QUESTÃO {n} · ENEM {ano}", 190, 230, 18, "black", GRAY, a, align="left", tracking=2)
    h = para(c, "“" + tema + "”", 190, 280, 26, "black", BLUE, a, 540, 32)
    y = 280 + h + 20
    text(c, "INÍCIO DA INTRODUÇÃO", 190, y, 16, "black", GRAY, a, align="left", tracking=2)
    lines = wrap(inicio, "bold", 24, 520)
    s1, done = inicio.split(". ")[0] + ".", 0
    rrect(c, 176, y + 14, 560, len(lines) * 31 + 24, 12, mix("#FFFFFF", BLUE, 0.10), a)
    for k, ln in enumerate(lines):
        yy = y + 48 + k * 31
        text(c, ln, 190, yy, 24, "bold", INK, a, align="left")
        if strike_a > 0 and done < len(s1):
            part = ln[:max(0, len(s1) - done)]
            strike(c, 186, yy - 8, 194 + text_w(part, "bold", 24), yy - 8, strike_a, RED, strike_a)
        done += len(ln) + 1
    y += len(lines) * 31 + 70
    para(c, enun, 190, y, 22, "black", INK, a, 540, 28)
    return y


def b_q7(c, t, C, B):
    head(c, t, C["18"], "QUESTÃO 7 · A PONTE QUE FALTA", "QUAL FRASE FAZ A PONTE?", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["18.a"], 0.4)
    lado_questao(c, t, C, 7, 2021, TEMA21, LEI, "A frase seguinte que melhor faz a ponte entre essa referência e o recorte "
                 "do tema é:", a)
    alts_panel(c, t, C, ALT7, 790, 232, 950, 24, "20.ok", "E", 8)
    pause_timer(c, t, C["19.end"] - 1.9, 460, 760)
    af = ep(t, C["20.f"], 0.4)
    selo(c, 460, 770, af, "VOCÊ CONSTRUIU A RUA", GREEN, -4, 28)
    questao_rotulo(c, a)


ALT3 = [("A", "autores da Antiguidade não podem ser citados na redação do Enem.", "21.A", "23.xa", "o problema é o encaixe, não o autor", RED),
        ("B", "a citação deveria vir entre aspas e com o ano da obra.", "21.B", "23.xb", "inventa uma exigência formal", RED),
        ("C", "a referência viola os direitos humanos e zera a Competência 5.", "22.C", "23.xc", "nada desrespeita direitos humanos", RED),
        ("D", "o trecho tem desvios de norma que comprometem a Competência 1.", "22.D", "23.xd", "sem desvio gramatical relevante", RED),
        ("E", "a referência é genérica e não se conecta ao recorte: poderia ser retirada sem mudar o sentido, o que caracteriza o repertório de bolso.", "22.E", None, "", GREEN)]


def b_q3(c, t, C, B):
    head(c, t, C["21"], "QUESTÃO 3 · O TESTE DA RETIRADA", "QUAL É O PROBLEMA?", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["21.a"], 0.4)
    st = ep(t, C["23.ok2"], 0.5)
    y = lado_questao(c, t, C, 3, 2025, TEMA25, ARIST, "Com base no que a Cartilha de 2026 diz sobre repertório, o principal "
                     "problema desse início é que", a, strike_a=st)
    alts_panel(c, t, C, ALT3, 790, 232, 950, 24, "23.ok", "E", 8)
    pause_timer(c, t, C["22.end"] - 1.9, 460, 780)
    selo(c, 460, 790, ep(t, C["23.ok2"] + 1.5, 0.4) * (1 - ep(t, C["23.xa"], 0.4)), "TIROU: NADA MUDOU", RED, -4, 28)
    questao_rotulo(c, a)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A TESE E A ANTECIPAÇÃO", BLUE)
    aa, ab, ac = ep(t, C["25.a"], 0.4), ep(t, C["25.b"], 0.4), ep(t, C["25.c"], 0.4)
    etiqueta_intro(c, 200, 190, 900, 1.0, show=[1, 1, 0.3 + 0.7 * ab, 0.3 + 0.7 * ac], lit=[0, 0, ab * (1 - ac), ac],
                   ok=[aa, aa, 0, 0], perguntas=1.0, movs=1.0, rowh=110)
    ad = ep(t, C["25.d"], 0.5)
    if ad > 0:
        rrect(c, 1180, 300, 520, 360, 24, "#FFFFFF", ad, shadow=True)
        text(c, "EPISÓDIO 4", 1440, 370, 24, "black", GRAY, ad, tracking=2)
        icone_peca(c, "tese", 1340, 480, ad, 1.0)
        icone_peca(c, "lista", 1540, 480, ad, 1.0)
        text(c, "a TESE e a", 1440, 590, 34, "black", MOV["tese"], ad)
        text(c, "ANTECIPAÇÃO dos eixos", 1440, 634, 34, "black", MOV["lista"], ad)


def b_cta(c, t, C, B):
    cta_intro(c, t, C, "26", "Qual foi a sua frase-ponte para a lei do registro civil?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, postal=b_postal, cartilha=b_cartilha, sem=b_sem,
              com=b_com, formula=b_formula, expressoes=b_expressoes, filosofo=b_filosofo, nos=b_nos, recap=b_recap,
              erros=b_erros, q7=b_q7, q3=b_q3, ponte=b_ponte, cta=b_cta)
