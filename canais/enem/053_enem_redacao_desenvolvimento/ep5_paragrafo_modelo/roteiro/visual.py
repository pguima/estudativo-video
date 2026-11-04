"""Visual — Redação ENEM, Desenvolvimento, Episódio 5: O parágrafo-modelo comentado e do fraco ao bom (tema claro).
Usa o desenho compartilhado da série (desenvolvimento_visual.py): ícones, ficha e mini-checklist das 5 etapas da entrega,
tese do estigma, rascunho com caligrafia, alternativas, recap, erros e CTA.
Novo aqui: os três entregadores do mesmo item; o parágrafo-modelo no rascunho com as frases numeradas, uma FAIXA colorida
por função e o painel "função + o que observar" à direita; a tabela "Frase | Função | O que observar"; as duas colunas
D1 × D2 com a mesma arquitetura e duas setas convergindo para a tese; as Versões 1 e 2 com o checklist das cinco etapas
EM CIMA (verde/vermelho) e o teste da retirada ao vivo; as três versões lado a lado; a Questão 7 com as frases se
reordenando nas cinco etapas.
"""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from desenvolvimento_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_desenvolvimento_ep5_paragrafo_modelo.mp4"


def frases(s):
    return re.split(r"(?<=[.!?])\s+", s.strip())


V1S = frases(V1_OPINIAO)
V2S = frases(V2_SOLTO)


# ======================================================================
# componentes novos deste episódio
# ======================================================================

def checklist_h(c, x, y, w, a, oks, h=66, tags=None):
    """checklist HORIZONTAL das 5 etapas (vai em cima de cada versão): oks[k] 1 = ✓ verde, 0 = ✗ vermelho, None = neutro"""
    if a <= 0:
        return
    cw = w / 5
    for k, key in enumerate(KEYS):
        o = oks[k] if k < len(oks) else None
        col = LIGHT if o is None else (GREEN if o else RED)
        xx = x + k * cw
        rrect(c, xx + 4, y, cw - 8, h, 12, "#FFFFFF", a, shadow=True)
        if o is not None:
            rrect(c, xx + 4, y, cw - 8, h, 12, mix("#FFFFFF", col, 0.22), a)
        rrect(c, xx + 4, y, 7, h, 3, PARTE[key], a)
        ICON_ETAPA[key](c, xx + 34, y + h / 2, 0.34, a, PARTE[key])
        s = NOMEP[key]
        sz = 19
        while text_w(s, "black", sz) > cw - 100 and sz > 13:
            sz -= 1
        text(c, s, xx + 56, y + h / 2 + sz * 0.36, sz, "black", INK2, a, align="left")
        if o is not None:
            check_icon(c, xx + cw - 26, y + h / 2, 13, a, col, "check" if o else "x")
        if tags and tags[k]:
            pill(c, tags[k], xx + cw / 2, y + h + 20, col if o is not None else GRAY, size=16, a=a, anchor="center",
                 bounds=(0, 1920))


def oks_at(t, cues, vals):
    """marca de cada etapa só depois do seu cue (None antes)"""
    return [vals[k] if (cues[k] is not None and t >= cues[k]) else None for k in range(5)]


def defbox(c, x, y, w, a, termo, s, col=BLUE, size=24):
    """caixa de definição: TERMO + frase simples. Retorna a altura."""
    if a <= 0:
        return 0
    lines = wrap(s, "bold", size, w - 40)
    h = 56 + len(lines) * (size + 8) + 8
    rrect(c, x, y, w, h, 14, mix("#FFFFFF", col, 0.10), a)
    rrect(c, x, y, 7, h, 3, col, a)
    text(c, termo, x + 22, y + 36, 18, "black", col, a, align="left", tracking=1.5)
    for j, ln in enumerate(lines):
        text(c, ln, x + 22, y + 70 + j * (size + 8), size, "bold", INK, a, align="left")
    return h


def folha_versao(c, t, x, y, w, h, sents, appear, title, bands=None, gone=None, size=32, lh=46, didatico=DIDATICO,
                 nums=False, a=1.0):
    """folha com a versão, uma frase por linha. appear[k] = alpha da frase · bands[k] = (alpha, cor) ·
    gone[k] = (alpha_saida 0–1, colapso 0–1) para o teste da retirada. Retorna [(y, n_linhas)]."""
    paper(c, x, y, w, h, a, lh=lh, top=y + 120 - 2 * lh + 6)
    text(c, title, x + 110, y + 50, 22, "black", GRAY, a, align="left", tracking=2)
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y, w, h))
    yy, out = y + 120, []
    for k, s in enumerate(sents):
        lines = wrap(s, "bold", size, w - 160)
        n = len(lines)
        out_a, col_ = 1.0, 0.0
        if gone and gone[k]:
            out_a, col_ = gone[k]
        ak = a * clamp(appear[k]) * (1 - out_a if gone and gone[k] else 1.0)
        dx = 300 * (out_a if gone and gone[k] else 0)
        if ak > 0:
            if bands and bands[k] and bands[k][0] > 0:
                ba, bc = bands[k]
                rrect(c, x + 96 + dx, yy - size - 6, w - 132, n * lh + 8, 10, mix("#FFFFFF", bc, 0.18), ak * ba)
                rrect(c, x + 96 + dx, yy - size - 6, 8, n * lh + 8, 4, bc, ak * ba)
            for j, ln in enumerate(lines):
                text(c, ln, x + 112 + dx, yy + j * lh, size, "bold", INK, ak, align="left")
        out.append((yy, n))
        yy += n * lh * (1 - col_)
    c.restore()
    if didatico:
        text(c, didatico, x + 110, y + h - 24, 18, "medium", AMBER, a * clamp(appear[0]), align="left")
    return out


# ======================================================================
# gancho, as três entregas, promessa
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], SERIE_SELO, "O PARÁGRAFO-MODELO", BLUE)
    card(c, *CARD_R)
    aa, ab, ac, ad = (ep(t, C[f"01.{x}"], 0.5) for x in "abcd")
    # a folha com as 5 frases
    if aa > 0:
        paper(c, 900, 190, 760, 610, aa, lh=100, top=268)
        text(c, "1º DESENVOLVIMENTO · da série Introdução", 1010, 240, 22, "black", BLUE, aa, align="left")
    for k, key in enumerate(KEYS):
        y = 300 + k * 100
        a = aa * ep(t, C["01.b"] + 0.15 * k, 0.4)
        badge_num(c, k + 1, 960, y, a, 24, bg=INK2)
        falta = ep(t, C["01.d"] + 0.6, 0.5) if k == 3 else 0
        col = mix(mix(PEN, "#FFFFFF", 0.45), PARTE[key], ep(t, C["01.c"] + 0.25 * k, 0.4))
        if a > 0:
            ww = [560, 600, 610, 590, 470][k]
            rrect(c, 1010, y - 12, ww, 26, 13, col, a * (1 - falta))
            if falta > 0:
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1010, y - 16, ww, 34), 14, 14),
                            paint(RED, a * falta, stroke=4))
                text_mid(c, "?", 1010 + ww / 2, y, 40, "black", RED, a * falta)
        icone_etapa(c, key, 1610 - 0 * k, y, a * ep(t, C["01.c"] + 0.25 * k, 0.4), 0.42, disc=False)
    text(c, "5", 450, 470, 260, "black", INK, ab)
    text(c, "FRASES", 450, 560, 64, "black", INK, ab)
    text(c, "cada uma, um TRABALHO", 450, 640, 36, "black", GREEN, ac)
    pill(c, "se uma faltar, você percebe", 450, 730, RED, size=28, a=ad, anchor="center", bounds=(0, 1920))


def b_entregas(c, t, C, B):
    frame(c, t, B["start"], "TRÊS ENTREGADORES", "O MESMO ITEM", BLUE)
    q = lambda x: C[f"02.{x}"]
    xs = [440, 960, 1480]
    at = ep(t, q("t"), 0.5)
    for k, cx in enumerate(xs):
        text(c, f"ENTREGADOR {k + 1}", cx, 215, 24, "black", GRAY, at, tracking=2)
        caixa(c, cx - 110, 560, 220, 170, at, open_=ep(t, q("c") + 0.3, 0.6) if k == 2 else 0.0)
    # 1: só repete
    aa = ep(t, q("a"), 0.4)
    if aa > 0:
        bubble(c, "é um ótimo produto!", xs[0] - 200, 260, 400, INK2, aa, size=28)
        bubble(c, "é um ótimo produto!", xs[0] - 180, 380, 400, INK2, ep(t, q("a") + 1.0, 0.4), size=28)
        u = ep(t, q("a") + 2.6, 1.6)
        pill(c, "e vai embora →", xs[0], 780, RED, size=24, a=aa * u, anchor="center", bounds=(0, 1920))
    # 2: nota fiscal e vai embora
    ab = ep(t, q("b"), 0.4)
    if ab > 0:
        icone_etapa(c, "repertorio", xs[1], 390, ab, 1.6)
        text(c, "NOTA FISCAL", xs[1], 510, 26, "black", PARTE["repertorio"], ab, tracking=1)
        pill(c, "e vai embora →", xs[1], 780, RED, size=24, a=ep(t, q("b") + 1.5, 0.4), anchor="center", bounds=(0, 1920))
    # 3: entrega completa
    ac = ep(t, q("c"), 0.4)
    if ac > 0:
        oks = [1 if t >= q("c") + 0.6 + 0.55 * k else None for k in range(5)]
        mini_entrega(c, xs[2], 345, ac, oks, 0.92)
        pill(c, "entrega completa ✓", xs[2], 780, GREEN, size=24, a=ep(t, q("c") + 3.2, 0.4), anchor="center",
             bounds=(0, 1920))
    ad = ep(t, q("d"), 0.4)
    if ad > 0:
        for k, (s, col) in enumerate((("VERSÃO 1", RED), ("VERSÃO 2", RED), ("VERSÃO 3", GREEN))):
            selo(c, xs[k], 680, ad, s, col, -4, 30)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "NO FIM DESTA AULA", "VOCÊ VAI SABER", GREEN)
    a1, d1 = rise(t, C["03.a"])
    check_icon(c, 260, 300 + d1, 34, a1, GREEN)
    text(c, "RECONHECER as 5 partes em qualquer parágrafo", 320, 316 + d1, 46, "black", INK, a1, align="left")
    for k, key in enumerate(KEYS):
        a = a1 * ep(t, C["03.a"] + 0.4 + 0.2 * k, 0.4)
        icone_etapa(c, key, 380 + k * 150, 430 + d1, a, 0.8)
    a2, d2 = rise(t, C["03.b"])
    check_icon(c, 260, 570 + d2, 34, a2, GREEN)
    text(c, "CONSERTAR um parágrafo fraco", 320, 586 + d2, 46, "black", INK, a2, align="left")
    if a2 > 0:
        fx = ep(t, C["03.b"] + 0.6, 0.6)
        pill(c, "fraco", 330, 660 + d2, RED, size=26, a=a2, bounds=(0, 1920))
        arrow(c, 440, 660 + d2, 560, 660 + d2, INK2, a2 * fx, 4, 14, progress=fx)
        pill(c, "bom", 580, 660 + d2, GREEN, size=26, a=a2 * fx, bounds=(0, 1920))
    pill(c, "cada palavra nova, uma de cada vez", W / 2, 780, BLUE, size=28, a=ep(t, C["03.c"], 0.4), anchor="center")


# ======================================================================
# pré-requisitos
# ======================================================================

def b_prereq(c, t, C, B):
    sid = which(t, C, ["04", "05"])
    head_seq(c, t, C, [("04", "REVISÃO RELÂMPAGO", "EPISÓDIOS 1 A 4", PURPLE),
                       ("05", "REVISÃO RELÂMPAGO", "A TESE DA SÉRIE INTRODUÇÃO", PURPLE)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "04":
        aa = ep(t, q("a"), 0.5)
        ab, ac, ad = (ep(t, q(x), 0.4) for x in "bcd")
        lit = [ab * (1 - ac), 0, 0, ac * (1 - ad), ad]
        ficha_entrega(c, 180, 190, 860, aa, lit=lit, partes=1.0, rowh=110, title="AS 5 PARTES · EP. 1")
        rows = [("b", "topico", "TÓPICO FRASAL · EP. 2", "anuncia o que o parágrafo vai provar"),
                ("c", "analise", "ANÁLISE · EP. 4", "mostra o que a referência revela sobre o problema"),
                ("d", "fechamento", "FECHAMENTO · EP. 4", "responde ao “e daí?” e liga tudo à tese")]
        for k, (cue, key, lab, s) in enumerate(rows):
            a, d = rise(t, q(cue))
            y = 210 + k * 200 + d
            if a > 0:
                rrect(c, 1090, y, 640, 170, 16, mix("#FFFFFF", PARTE[key], 0.10), a)
                rrect(c, 1090, y, 8, 170, 4, PARTE[key], a)
                text(c, lab, 1120, y + 46, 22, "black", PARTE[key], a, align="left", tracking=1.5)
                para(c, s, 1120, y + 96, 30, "black", INK, a, 590, 38)
        return
    tese_card(c, 220, 230, 1480, ep(t, q("a"), 0.5), eixos=0, size=36)
    yy = 230 + 96 + 3 * 46 + 30
    pill(c, "EIXO 1 · desinformação", 256, yy, PARTE["topico"], size=28, a=ep(t, q("b"), 0.4), bounds=(0, 1920))
    pill(c, "EIXO 2 · mídia", 680, yy, PARTE["argumento"], size=28, a=ep(t, q("c"), 0.4), bounds=(0, 1920))
    ab = ep(t, q("b"), 0.4)
    if ab > 0:
        text(c, "item A", 256 + 150, yy + 80, 26, "black", PARTE["topico"], ab, align="center")
        text(c, "item B", 680 + 110, yy + 80, 26, "black", PARTE["argumento"], ep(t, q("c"), 0.4), align="center")
    text(c, "ENEM 2020 · " + TEMA20, 220, 800, 22, "bold", GRAY, ep(t, q("t"), 0.5), align="left")


# ======================================================================
# bloco a — eu faço: o parágrafo-modelo, frase por frase
# ======================================================================

PX, PY, PW, PH = 140, 160, 1040, 680
HX, HS, HLH, HMW = 250, 26, 38, 900
RX, RY, RW, RH = 1210, 160, 570, 680


def modelo_layout():
    out, y = [], PY + 140
    for s in MODELO:
        lines = hwrap(s, HS, HMW)
        out.append((s, y, lines))
        y += len(lines) * HLH
    return out


_LAY = modelo_layout()


def destaque(c, k, frase, a, prog_=1.0, col=None):
    """sublinha um trecho da frase k do modelo (pode quebrar linha)"""
    if a <= 0:
        return
    s, y, lines = _LAY[k]
    i0 = s.find(frase)
    if i0 < 0:
        return
    i1 = i0 + len(frase)
    pos = 0
    col = col or mix(PARTE[KEYS[k]], "#000000", 0.15)
    total = len(frase)
    done = prog_ * total
    for j, ln in enumerate(lines):
        a0, a1 = pos, pos + len(ln)
        s0, s1 = max(i0, a0), min(i1, a1)
        if s0 < s1 and done > 0:
            seg = min(s1 - s0, done)
            x0 = HX + hand_w(ln[:s0 - a0], HS)
            x1 = HX + hand_w(ln[:s0 - a0 + int(seg)], HS)
            line(c, x0, y + j * HLH + 8, x1, y + j * HLH + 8, col, a, 5)
            done -= seg
        pos = a1 + 1


def rascunho_modelo(c, t, a, reveals, bands, nums, cur=-1, header=1.0):
    paper(c, PX, PY, PW, PH, a, lh=HLH, top=PY + 140 - 2 - 3 * HLH)
    text(c, "ENEM 2020 · D1 · eixo da desinformação", PX + 110, PY + 56, 22, "black", BLUE, a * header, align="left")
    text(c, PARAG_DIDATICO, PX + 110, PY + 90, 18, "medium", AMBER, a * header, align="left")
    for k, (s, y, lines) in enumerate(_LAY):
        dim = 1.0 if (cur < 0 or k == cur) else 0.5
        if bands[k] > 0:
            for j, ln in enumerate(lines):
                rrect(c, HX - 12, y + j * HLH - HS - 4, hand_w(ln, HS) + 24, HLH - 2, 8,
                      mix("#FFFFFF", PARTE[KEYS[k]], 0.22), a * bands[k] * dim)
            rrect(c, PX + 84, y - HS - 4, 7, len(lines) * HLH - 2, 3, PARTE[KEYS[k]], a * bands[k])
        badge_num(c, k + 1, PX + 45, y - 8, a * nums[k], 18, bg=PARTE[KEYS[k]] if bands[k] > 0.5 else INK2)
        hand_para(c, s, HX, y, HS, PEN, a * dim, HMW, HLH, reveal=reveals[k])


# cena -> índice da frase comentada
CUR = {"06": -1, "07": 0, "08": 1, "09": 2, "10": 2, "11": 3, "12": 3, "13": 4}
S_CUE = ["07.s1", "08.s2", "09.s3", "11.s4", "13.s5"]
F_CUE = ["07.f", "08.f", "09.f", "11.f", "13.f"]
OBS_CUE = ["07.o1", "08.o1", "10.o1", "12.o1", "13.o1"]
E_CUE = {"07": "07.e", "08": "08.e", "09": "09.e", "12": "12.e", "13": "13.e"}
DESTAQUES = [  # (cue, frase k, trecho)
    ("07.o1", 0, "Em primeiro lugar,"), ("07.o2", 0, "a desinformação"),
    ("08.o1", 1, "Como pouco se discute"), ("08.o2", 1, "fraqueza de caráter,"),
    ("10.o1", 2, "O Alienista,"), ("10.o2", 2, "Machado de Assis"),
    ("10.o3", 2, "satiriza o médico Simão Bacamarte, que, com critérios arbitrários, recolhe à Casa Verde a maior parte "
                 "da população de Itaguaí,"),
    ("12.o1", 3, "Mais de um século depois,"), ("12.o2", 3, "o que leva muitos a adiar a busca por ajuda por medo do julgamento."),
    ("13.o1", 4, "enquanto a informação não substituir o preconceito,"), ("13.o2", 4, "o estigma"),
]


def painel_frase(c, t, C, sid, k):
    key = KEYS[k]
    q = lambda x: C[f"{sid}.{x}"]
    a0 = 1.0
    badge_num(c, k + 1, RX + 56, RY + 62, a0, 26, bg=PARTE[key])
    text(c, f"FRASE {k + 1}", RX + 100, RY + 72, 26, "black", GRAY, a0, align="left", tracking=2)
    af = ep(t, C[F_CUE[k]], 0.4)
    icone_etapa(c, key, RX + 92, RY + 175, af, 0.95)
    text(c, "FUNÇÃO", RX + 170, RY + 150, 18, "black", GRAY, af, align="left", tracking=2)
    text(c, NOMEP[key].upper(), RX + 170, RY + 200, 40 if k != 0 else 36, "black", PARTE[key], af, align="left")
    ao = ep(t, C[OBS_CUE[k]], 0.4) if t >= C[OBS_CUE[k]] - 0.01 or OBS_CUE[k][:2] == sid else 0.0
    y = RY + 260
    if ao > 0:
        lines = wrap(MODELO_OBS[k], "bold", 25, RW - 80)
        hh = 60 + len(lines) * 33
        rrect(c, RX + 24, y, RW - 48, hh, 14, mix("#FFFFFF", PARTE[key], 0.10), ao)
        text(c, "O QUE OBSERVAR", RX + 46, y + 34, 18, "black", PARTE[key], ao, align="left", tracking=2)
        for j, ln in enumerate(lines):
            text(c, ln, RX + 46, y + 70 + j * 33, 25, "bold", INK, ao, align="left")
        y += hh + 18
    else:
        y += 0
    yb = RY + 450
    if sid == "07":
        defbox(c, RX + 24, yb, RW - 48, ep(t, q("o1"), 0.4), "CONECTIVO DE ORDENAÇÃO", "marca a posição na sequência")
        pill(c, "EIXO 1 · desinformação", RX + RW / 2, yb + 125, PARTE["topico"], size=24, a=ep(t, q("o2"), 0.4),
             anchor="center", bounds=(0, 1920))
    elif sid == "08":
        a1, a2 = ep(t, q("o1"), 0.4), ep(t, q("o2"), 0.4)
        if a1 > 0:
            rrect(c, RX + 24, yb + 10, 230, 110, 14, mix("#FFFFFF", PARTE["argumento"], 0.12), a1)
            text(c, "CAUSA", RX + 139, yb + 48, 18, "black", PARTE["argumento"], a1, tracking=2)
            text(c, "pouco se discute", RX + 139, yb + 92, 23, "black", INK, a1)
        arrow(c, RX + 262, yb + 65, RX + 312, yb + 65, INK2, a2, 4, 12, progress=a2)
        if a2 > 0:
            rrect(c, RX + 316, yb + 10, 230, 110, 14, mix("#FFFFFF", PARTE["argumento"], 0.12), a2)
            text(c, "EFEITO", RX + 431, yb + 48, 18, "black", PARTE["argumento"], a2, tracking=2)
            text(c, "lida como fraqueza", RX + 431, yb + 92, 23, "black", INK, a2)
    elif sid == "10":
        defbox(c, RX + 24, yb, RW - 48, ep(t, q("o3"), 0.4), "PARÁFRASE",
               "contar, com as suas palavras, o que a obra mostra")
        ae = ep(t, q("e"), 0.4)
        if ae > 0:
            check_icon(c, RX + 50, yb + 162, 14, ae, RED, "x")
            text(c, "só o nome do livro", RX + 74, yb + 170, 24, "black", RED, ae, align="left")
            check_icon(c, RX + 50, yb + 206, 14, ae, GREEN)
            text(c, "o que ACONTECE nele", RX + 74, yb + 214, 24, "black", GREEN, ae, align="left")
    elif sid == "12":
        defbox(c, RX + 24, yb, RW - 48, ep(t, q("o1"), 0.4), "ATUALIZAR",
               "trazer o que a obra mostra para o Brasil de hoje")
    elif sid == "13":
        a3 = ep(t, q("o3"), 0.4)
        if a3 > 0:
            check_icon(c, RX + 60, yb + 40, 18, a3, GREEN)
            text(c, "nenhuma informação nova", RX + 92, yb + 50, 28, "black", GREEN, a3, align="left")
    if sid in E_CUE:
        ae = ep(t, C[E_CUE[sid]], 0.4)
        pill(c, ETAPA[key], RX + RW / 2, RY + RH - 50, PARTE[key], size=26, a=ae, anchor="center", bounds=(0, 1920))


def b_eufaco(c, t, C, B):
    ids = ["06", "07", "08", "09", "10", "11", "12", "13"]
    sid = which(t, C, ids)
    head_seq(c, t, C, [("06", "EU FAÇO · AO VIVO", "O PARÁGRAFO-MODELO", GREEN)] +
             [(i, "EU FAÇO · FRASE POR FRASE", f"FRASE {CUR[i] + 1}", GREEN) for i in ids[1:]])
    a = ep(t, C["06"], 0.5)
    rv = [wreveal(t, (C[S_CUE[k]] + 1.0, C[F_CUE[k]] - 0.4)) for k in range(5)]
    bands = [ep(t, C[F_CUE[k]], 0.5) for k in range(5)]
    nums = [ep(t, C[S_CUE[k]], 0.3) for k in range(5)]
    cur = CUR[sid]
    rascunho_modelo(c, t, a, rv, bands, nums, cur, ep(t, C["06.b"], 0.4))
    for cue, k, fr in DESTAQUES:
        if t >= C[cue] and C[cue[:2]] <= t:
            destaque(c, k, fr, 1.0, ep(t, C[cue], 0.8))
    card(c, RX, RY, RW, RH)
    if sid == "06":
        q = lambda x: C[f"06.{x}"]
        para(c, "O que cada frase está fazendo ali?", RX + 40, RY + 90, 38, "black", INK, ep(t, q("t"), 0.4), RW - 80, 46)
        defbox(c, RX + 24, RY + 220, RW - 48, ep(t, q("a"), 0.4), "PARÁGRAFO-MODELO",
               "um parágrafo pronto, feito para você observar COMO ele foi construído", size=26)
        ab = ep(t, q("b"), 0.4)
        pill(c, "EIXO 1 · desinformação", RX + RW / 2, RY + 470, PARTE["topico"], size=24, a=ab, anchor="center",
             bounds=(0, 1920))
        ac = ep(t, q("c"), 0.4)
        text(c, "uma frase de cada vez", RX + RW / 2, RY + 560, 28, "black", GREEN, ac)
        for k in range(5):
            badge_num(c, k + 1, RX + 125 + k * 80, RY + 620, ac * ep(t, q("c") + 0.15 * k, 0.3), 24, bg=PARTE[KEYS[k]])
        return
    painel_frase(c, t, C, sid, cur)


# ======================================================================
# a tabela "Frase | Função | O que observar"
# ======================================================================

def b_tabela(c, t, C, B):
    frame(c, t, B["start"], "O PARÁGRAFO-MODELO", "FRASE · FUNÇÃO · O QUE OBSERVAR", GREEN)
    aa = ep(t, C["14.a"], 0.4)
    text(c, "FRASE", 200, 228, 20, "black", GRAY, aa, align="left", tracking=2)
    text(c, "FUNÇÃO", 330, 228, 20, "black", GRAY, aa, align="left", tracking=2)
    text(c, "O QUE OBSERVAR", 640, 228, 20, "black", GRAY, aa, align="left", tracking=2)
    for k, key in enumerate(KEYS):
        a, d = rise(t, C["14.a"] + 0.3 + 0.3 * k)
        y = 252 + k * 106 + d
        if a <= 0:
            continue
        rrect(c, 180, y, 1560, 94, 12, mix("#FFFFFF", PARTE[key], 0.10), a)
        rrect(c, 180, y, 8, 94, 4, PARTE[key], a)
        text_mid(c, f"[{k + 1}]", 240, y + 47, 30, "black", PARTE[key], a)
        text_mid(c, NOMEP[key], 330, y + 47, 30, "black", PARTE[key], a, align="left")
        lines = wrap(MODELO_OBS[k], "bold", 27, 1060)
        y0 = y + 47 - (len(lines) - 1) * 17
        for j, ln in enumerate(lines):
            text_mid(c, ln, 640, y0 + j * 34, 27, "bold", INK, a, align="left")
    ab = ep(t, C["14.b"], 0.4)
    if ab > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(312, 244, 300, 538), 14, 14), paint(GREEN, ab, stroke=4))
        pill(c, "5 funções diferentes", 462, 808, GREEN, size=22, a=ab, anchor="center", bounds=(0, 1920))
    selo(c, 1420, 808, ep(t, C["14.c"], 0.4), "NENHUMA FAZ O TRABALHO DA OUTRA", PURPLE, -2, 22)


# ======================================================================
# bloco b — dois parágrafos, a mesma arquitetura
# ======================================================================

def coluna_d(c, x, y, w, a, rot, cone, cor, show, glow_fecho=0.0, item=None, item_a=0.0, eixo_a=1.0, con_a=1.0):
    if a <= 0:
        return
    rrect(c, x, y, w, 520, 20, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 70, 20, mix("#FFFFFF", cor, 0.18 * eixo_a), a)
    text_mid(c, rot, x + w / 2, y + 36, 30, "black", mix(INK2, cor, eixo_a), a)
    if item and item_a > 0:
        badge_num(c, item, x + 40, y + 36, a * item_a, 24, bg=MOV["lista"])
    pill(c, cone, x + w / 2, y + 112, INK2, size=24, a=a * con_a, anchor="center", bounds=(0, 1920))
    for k, key in enumerate(KEYS):
        ak = a * clamp(show[k])
        yy = y + 150 + k * 72
        rrect(c, x + 30, yy, w - 60, 60, 12, mix("#FFFFFF", PARTE[key], 0.16), ak)
        if key == "fechamento" and glow_fecho > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 26, yy - 4, w - 52, 68), 14, 14),
                        paint(PARTE[key], ak * glow_fecho, stroke=4))
        ICON_ETAPA[key](c, x + 70, yy + 30, 0.36, ak, PARTE[key])
        text_mid(c, NOMEP[key], x + 110, yy + 30, 26, "black", PARTE[key], ak, align="left")


def b_arquitetura(c, t, C, B):
    sid = which(t, C, ["15", "16"])
    head_seq(c, t, C, [("15", "DOIS PARÁGRAFOS", "A MESMA ARQUITETURA", BLUE), ("16", "DOIS PARÁGRAFOS", "A MESMA TESE", BLUE)])
    card(c, *CARD_R)
    at = ep(t, C["15.t"], 0.5)
    sh = [ep(t, C["15.a"] + 0.2 * k, 0.4) for k in range(5)]
    ab, ac = ep(t, C["15.b"], 0.4), ep(t, C["15.c"], 0.4)
    gl = ep(t, C["16.a"], 0.4) if "16.a" in C else 0
    item_a = ep(t, C["16.d"], 0.4)
    coluna_d(c, 260, 175, 600, at, "D1 · desinformação", "“Em primeiro lugar,”", PARTE["topico"], sh, gl, "A", item_a,
             eixo_a=ab, con_a=ep(t, C["15.d1"], 0.4))
    coluna_d(c, 1060, 175, 600, at, "D2 · mídia", "“Além disso,”", PARTE["argumento"], sh, gl, "B", item_a,
             eixo_a=ac, con_a=ep(t, C["15.d2"], 0.4))
    ad = ep(t, C["15.d"], 0.4)
    if ad > 0 and sid == "15":
        text(c, "conectivo de PROGRESSÃO: o texto avança", W / 2, 760, 28, "black", BLUE, ad * (1 - gl))
    # setas convergindo para a tese
    pb = ep(t, C["16.b"], 1.0)
    if pb > 0:
        arrow(c, 560, 700, 840, 752, PARTE["fechamento"], 1.0, 6, 18, progress=pb)
        arrow(c, 1360, 700, 1080, 752, PARTE["fechamento"], 1.0, 6, 18, progress=pb)
    at2 = ep(t, C["16.b"] + 0.6, 0.4)
    if at2 > 0:
        rrect(c, 760, 730, 400, 64, 16, MOV["tese"], at2, shadow=True)
        text_mid(c, "TESE · desinformação + mídia", 960, 762, 24, "black", "#FFFFFF", at2)
    acp = ep(t, C["16.c"], 0.4)
    if acp > 0:
        pill(c, "PROJETO DE TEXTO", 260, 762, BLUE, size=22, a=acp, bounds=(0, 1920))
        text(c, "= o plano que liga a redação inteira", 1190, 770, 22, "black", BLUE, acp, align="left")


# ======================================================================
# blocos c e d — versão 1 e versão 2
# ======================================================================

FX, FY, FW, FH = 140, 270, 1100, 570
NX, NW = 1270, 510


def nota(c, x, y, s, a, ok, w=NW, size=26, col=None):
    if a <= 0:
        return 0
    check_icon(c, x + 18, y - 8, 16, a, GREEN if ok else RED, "check" if ok else "x")
    return para(c, s, x + 48, y, size, "black", col or INK, a, w - 50, size + 6)


def b_v1(c, t, C, B):
    sid = which(t, C, ["17", "18"])
    head_seq(c, t, C, [("17", "VERSÃO 1", "SÓ OPINIÃO", INK2), ("18", "VERSÃO 1 · CONFERINDO A ENTREGA", "SÓ OPINIÃO", RED)])
    an = sid == "18"
    spans = [phrase_span("17", s, C["17.b"] + 3.5 * k, C["17.b"] + 3.5 * k + 3) for k, s in enumerate(V1S)]
    appear = [ep(t, sp[0], 0.4) for sp in spans]
    bands = None
    if an:
        aa = ep(t, C["18.a"], 0.4)
        ab = ep(t, C["18.b"], 0.4)
        bands = [(aa, GREEN), (ab, RED), (ab, RED), (aa, GREEN)]
    lay = folha_versao(c, t, FX, FY, FW, FH, V1S, appear, "VERSÃO 1 · SÓ OPINIÃO", bands=bands, size=34, lh=50)
    cues = [C["18.a"], C["18.c"], C["18.d"], C["18.e"], C["18.a"]] if an else [None] * 5
    checklist_h(c, FX, 175, FW, ep(t, C["17.a"], 0.4), oks_at(t, cues, [1, 0, 0, 0, 1]))
    if not an:
        icone_etapa(c, "topico", NX + NW / 2, 420, 0, 1.0)
        pill(c, "o mesmo eixo · desinformação", NX + NW / 2, 360, BLUE, size=22, a=ep(t, C["17.t"], 0.4),
             anchor="center", bounds=(0, 1920))
        para(c, "o que esse parágrafo entrega?", NX + 20, 470, 36, "black", INK, ep(t, C["17.a"], 0.4), NW - 20, 44)
        return
    ab = ep(t, C["18.b"], 0.4)
    if ab > 0:
        y1 = lay[1][0]
        y2 = lay[2][0] + (lay[2][1] - 1) * 50
        pill(c, "REPETE", FX + FW - 30, (y1 + y2) / 2 - 10, RED, size=22, a=ab, anchor="right", bounds=(0, 1920))
    y = 320
    y += nota(c, NX, y, "o meio repete a mesma ideia", ep(t, C["18.b"], 0.4), False) + 14
    y += nota(c, NX, y, "sem causa, sem repertório, sem análise", ep(t, C["18.e"], 0.4), False) + 24
    af = ep(t, C["18.f"], 0.4)
    if af > 0:
        rrect(c, NX - 10, y - 10, NW + 10, 150, 14, mix("#FFFFFF", PURPLE, 0.08), af)
        text(c, "PELOS DESCRITORES, TENDE A", NX + 10, y + 24, 17, "black", PURPLE, af, align="left", tracking=1.5)
        para(c, "informações pouco desenvolvidas, com argumentação previsível", NX + 10, y + 62, 25, "black", INK, af,
             NW - 30, 32)
        y += 162
        defbox(c, NX - 10, y, NW + 10, ep(t, C["18.f"] + 2.5, 0.4), "ARGUMENTAÇÃO PREVISÍVEL",
               "só diz o óbvio, sem explicar nem provar", size=23)
    selo(c, FX + FW - 250, FY + FH - 80, ep(t, C["18.g"], 0.4), "“ÓTIMO PRODUTO!”", RED, -5, 30)


def b_v2(c, t, C, B):
    sid = which(t, C, ["19", "20", "21"])
    head_seq(c, t, C, [("19", "VERSÃO 2", "REPERTÓRIO SOLTO", INK2), ("20", "VERSÃO 2 · CONFERINDO", "REPERTÓRIO SOLTO", RED),
                       ("21", "TESTE DA RETIRADA", "AO VIVO", AMBER)])
    spans = [phrase_span("19", s, C["19.b"] + 3.5 * k, C["19.b"] + 3.5 * k + 3) for k, s in enumerate(V2S)]
    appear = [ep(t, sp[0], 0.4) for sp in spans]
    bands, gone = None, None
    if sid in ("20", "21"):
        aa, ab = ep(t, C["20.a"], 0.4), ep(t, C["20.b"], 0.4)
        bands = [(ab, GREEN), (aa, AMBER), (ab, GREEN)]
        px = ep(t, C["20.x"] + 0.4, 1.0)
        colap = ep(t, C["21.a"] - 0.2, 0.6) if "21.a" in C else 0
        gone = [None, (px, colap), None]
    folha_versao(c, t, FX, FY, FW, FH, V2S, appear, "VERSÃO 2 · REPERTÓRIO SOLTO", bands=bands, gone=gone, size=34, lh=50)
    an = sid != "19"
    cues = [C["20.b"], C["20.b"], C["20.b"], C["20.b"], C["20.b"]] if an else [None] * 5
    oks = oks_at(t, cues, [1, 0, 0, 0, 1])
    tags = [None, None, "só mencionado" if oks[2] is not None else None, None, None]
    checklist_h(c, FX, 175, FW, ep(t, C["19.a"], 0.4), oks, tags=tags)
    if sid == "19":
        para(c, "então basta colocar uma referência?", NX + 20, 470, 36, "black", INK, ep(t, C["19.t"], 0.4), NW - 20, 44)
        return
    if sid == "20":
        aa = ep(t, C["20.a"], 0.4)
        pill(c, "LEGÍTIMA ✓", NX, 320, BLUE, size=24, a=aa, bounds=(0, 1920))
        pill(c, "PERTINENTE ✓", NX + 220, 320, BLUE, size=24, a=ep(t, C["20.a"] + 0.6, 0.4), bounds=(0, 1920))
        text(c, "a obra existe e tem a ver com o tema", NX, 380, 22, "bold", INK2, aa, align="left")
        y = 450
        y += nota(c, NX, y, "mas é apenas MENCIONADA", ep(t, C["20.b"], 0.4), False) + 10
        y += nota(c, NX, y, "não diz o que a obra mostra nem como se liga ao problema", ep(t, C["20.b"] + 1.0, 0.4),
                  False, size=23) + 26
        acx = ep(t, C["20.c"], 0.4)
        if acx > 0:
            rrect(c, NX - 10, y - 10, NW + 10, 190, 16, mix("#FFFFFF", AMBER, 0.10), acx)
            text(c, "TESTE DA RETIRADA · SÉRIE INTRODUÇÃO", NX + 10, y + 24, 17, "black", AMBER, acx, align="left",
                 tracking=1)
            para(c, "se a referência sai e nada muda, ela não estava trabalhando", NX + 10, y + 66, 26, "black", INK, acx,
                 NW - 30, 34)
        return
    q = lambda x: C[f"21.{x}"]
    ab = ep(t, q("b"), 0.4)
    text(c, "fez falta?", NX + NW / 2, 330, 40, "black", INK, ab)
    selo(c, NX + NW / 2, 410, ab, "NENHUMA", RED, -5, 40)
    ac = ep(t, q("c"), 0.4)
    if ac > 0:
        cartilha(c, NX, 470, ac, inep=0, s=0.4)
        text(c, "CARTILHA DO PARTICIPANTE", NX + 145, 520, 17, "black", PURPLE, ac, align="left", tracking=1)
        text(c, "uso NÃO PRODUTIVO", NX + 145, 565, 32, "black", PURPLE, ac, align="left")
        defbox(c, NX - 10, 660, NW + 10, ep(t, q("c") + 2.5, 0.4), "REPERTÓRIO NÃO PRODUTIVO",
               "está no texto, mas não trabalha pelo argumento", col=PURPLE, size=23)
    ad = ep(t, q("d"), 0.4)
    if ad > 0:
        icone_etapa(c, "repertorio", FX + FW - 340, FY + FH - 110, ad, 0.7)
        pill(c, "nota fiscal… e vai embora", FX + FW - 30, FY + FH - 110, RED, size=22, a=ad, anchor="right",
             bounds=(0, 1920))


# ======================================================================
# bloco e — as três versões lado a lado e o que mudou
# ======================================================================

V3_RESUMO = ["Em primeiro lugar, a desinformação…", "Como pouco se discute…", "…em O Alienista, Machado de Assis…",
             "Mais de um século depois…", "Dessa forma, enquanto a informação…"]


def b_tres(c, t, C, B):
    frame(c, t, B["start"], "AS TRÊS VERSÕES", "LADO A LADO", PURPLE)
    q = lambda x: C[f"22.{x}"]
    xs = [180, 720, 1260]
    w = 480
    at = ep(t, q("t"), 0.5)
    tit = [("VERSÃO 1 · só opinião", RED), ("VERSÃO 2 · repertório solto", RED), ("VERSÃO 3 · parágrafo-modelo", GREEN)]
    vals = [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    marks = [q("c"), q("d"), q("e")]
    ab = ep(t, q("b"), 0.4)
    for k, x in enumerate(xs):
        ak = at if k < 2 else ep(t, q("a"), 0.4)
        text(c, tit[k][0], x + w / 2, 196, 22, "black", INK2, at, tracking=1)
        oks = vals[k] if t >= marks[k] else [None] * 5
        mini_entrega(c, x + w / 2, 312, ab, oks, 1.0)
        if ak <= 0:
            continue
        rrect(c, x, 425, w, 375, 14, PAPER, ak, shadow=True)
        if k < 2:
            para(c, (V1_OPINIAO, V2_SOLTO)[k], x + 24, 468, 23, "bold", INK, ak, w - 48, 31)
        else:
            for j, s in enumerate(V3_RESUMO):
                yy = 440 + j * 64
                rrect(c, x + 14, yy, w - 28, 56, 8, mix("#FFFFFF", PARTE[KEYS[j]], 0.20), ak)
                rrect(c, x + 14, yy, 6, 56, 3, PARTE[KEYS[j]], ak)
                text_mid(c, f"[{j + 1}] " + s, x + 30, yy + 28, 20, "bold", INK, ak, align="left")
            text(c, PARAG_DIDATICO, x + 24, 780, 15, "medium", AMBER, ak, align="left")
        if k < 2:
            text(c, DIDATICO, x + 24, 780, 15, "medium", AMBER, ak, align="left")
    ad = ep(t, q("d"), 0.4)
    if ad > 0:
        pill(c, "nota fiscal que não trabalha", xs[1] + w / 2, 820, RED, size=18, a=ad, anchor="center", bounds=(0, 1920))
    ac = ep(t, q("c"), 0.4)
    pill(c, "só 2 etapas", xs[0] + w / 2, 820, RED, size=18, a=ac, anchor="center", bounds=(0, 1920))
    pill(c, "entrega completa", xs[2] + w / 2, 820, GREEN, size=18, a=ep(t, q("e"), 0.4), anchor="center",
         bounds=(0, 1920))


def b_mudou(c, t, C, B):
    frame(c, t, B["start"], "DO FRACO AO BOM", "O QUE MUDOU", PURPLE)
    aa = ep(t, C["23.t"], 0.5)
    text(c, "VERSÕES 1 E 2", 540, 240, 24, "black", RED, aa, tracking=2)
    text(c, "VERSÃO 3", 1340, 240, 24, "black", GREEN, aa, tracking=2)
    rows = [("23.a", "repetição", "explicação causal", "argumento"),
            ("23.b", "menção", "conteúdo da referência", "repertorio"),
            ("23.c", "salto para o fechamento", "análise que conecta passado e presente", "analise")]
    for k, (cue, s1, s2, key) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + k * 170 + d
        icone_etapa(c, key, 230, y + 55, a, 0.8)
        rrect(c, 310, y, 460, 110, 16, mix("#FFFFFF", RED, 0.08), a)
        sz = 32 if text_w(s1, "black", 32) < 420 else 27
        text_mid(c, s1, 540, y + 55, sz, "black", RED, a)
        arrow(c, 790, y + 55, 940, y + 55, INK2, a, 5, 18, progress=ep(t, C[cue] + 0.6, 0.5))
        a2 = ep(t, C[cue] + 0.8, 0.4)
        rrect(c, 960, y, 760, 110, 16, mix("#FFFFFF", GREEN, 0.10), a2)
        text_mid(c, s2, 1340, y + 55, 32 if text_w(s2, "black", 32) < 720 else 28, "black", GREEN, a2)


# ======================================================================
# nós fazemos: a frase [2] que falta
# ======================================================================

def b_exercicio(c, t, C, B):
    sid = which(t, C, ["24", "25"])
    head_seq(c, t, C, [("24", "NÓS FAZEMOS", "ESCREVA A FRASE [2]", AMBER), ("25", "NÓS FAZEMOS", "COMPARANDO", GREEN)])
    a = 1.0
    x, y, w, h = FX, FY, FW, FH
    paper(c, x, y, w, h, a, lh=46, top=y + 110 - 2 * 46 + 6)
    text(c, "VERSÃO 1 + A FRASE [2] QUE FALTA", x + 110, y + 50, 22, "black", GRAY, a, align="left", tracking=2)
    badge_num(c, 1, x + 45, y + 102, a, 18, bg=PARTE["topico"])
    text(c, V1S[0], x + 112, y + 110, 30, "bold", INK, a, align="left")
    fill = ep(t, C["25.s"], 0.6) if "25.s" in C else 0
    badge_num(c, 2, x + 45, y + 168, a, 18, bg=PARTE["argumento"])
    sy = y + 140
    if fill < 1:
        aa = ep(t, C["24.a"], 0.4) * (1 - fill)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 100, sy, w - 140, 170), 12, 12),
                    paint(AMBER, aa, stroke=4))
        text_mid(c, "?  o PORQUÊ: causa + consequência", x + w / 2 + 20, sy + 85, 32, "black", AMBER, aa)
    if fill > 0:
        rrect(c, x + 100, sy, w - 140, 170, 12, mix("#FFFFFF", PARTE["argumento"], 0.16), fill)
        rrect(c, x + 100, sy, 8, 170, 4, PARTE["argumento"], fill)
        para(c, MODELO[1], x + 124, sy + 40, 27, "bold", INK, fill, w - 180, 36)
        ab, ac = ep(t, C["25.b"], 0.6), ep(t, C["25.c"], 0.6)
        if ab > 0:
            ww = text_w("Como pouco se discute", "bold", 27)
            line(c, x + 124, sy + 48, x + 124 + ww * ab, sy + 48, mix(PARTE["argumento"], "#000000", 0.2), fill, 5)
        if ac > 0:
            lines = wrap(MODELO[1], "bold", 27, w - 180)
            for j, ln in enumerate(lines):
                i = ln.find("fraqueza de caráter")
                if i >= 0:
                    x0 = x + 124 + text_w(ln[:i], "bold", 27)
                    ww = text_w("fraqueza de caráter", "bold", 27)
                    line(c, x0, sy + 48 + j * 36, x0 + ww * ac, sy + 48 + j * 36, mix(PARTE["argumento"], "#000000", 0.2),
                         fill, 5)
        text(c, "frase [2] do parágrafo-modelo", x + w - 50, sy + 200, 18, "medium", PARTE["argumento"], fill,
             align="right")
    rest_a = 0.45
    yy = y + 360 + 24
    for k, s in enumerate(V1S[1:]):
        yy += para(c, s, x + 112, yy, 26, "bold", INK2, rest_a * (1 - fill * 0.3), w - 160, 34)
    text(c, DIDATICO, x + 110, y + h - 24, 18, "medium", AMBER, a, align="left")
    if sid == "24":
        q = lambda k_: C[f"24.{k_}"]
        checklist_h(c, FX, 175, FW, 1.0, [1, 0 if t >= q("a") else None, None, None, 1])
        ab = ep(t, q("b"), 0.4)
        para(c, "pause e escreva a frase [2]:", NX, 330, 34, "black", INK, ab, NW, 42)
        para(c, "o PORQUÊ, com causa e consequência", NX, 430, 34, "black", PARTE["argumento"], ab, NW, 42)
        pause_timer(c, t, C["24.p"] + 0.3, NX + NW / 2, 680)
        return
    q = lambda k_: C[f"25.{k_}"]
    checklist_h(c, FX, 175, FW, 1.0, [1, 1 if t >= q("d") else 0, None, None, 1])
    y = 360
    for cue, s in (("b", "a sua frase tem uma CAUSA?"), ("c", "e um EFEITO?")):
        a_ = ep(t, q(cue), 0.4)
        check_icon(c, NX + 20, y - 10, 18, a_, GREEN)
        text(c, s, NX + 54, y, 30, "black", INK, a_, align="left")
        y += 70
    ad = ep(t, q("d"), 0.4)
    para(c, "não precisa ser igual: precisa fazer o MESMO TRABALHO", NX, 560, 30, "black", GREEN, ad, NW, 38)
    selo(c, NX + NW / 2, 720, ad, "EXPLICOU ✓", GREEN, -4, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Cinco frases, cinco trabalhos.", "Repetir não é explicar; mencionar não é usar.",
          "Dois parágrafos, a mesma arquitetura, a mesma tese."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("26", "34"), FRASES, cols=[PARTE["topico"], RED, GREEN])


ERROS = [("27", "Misturar os dois eixos no mesmo parágrafo", "o parágrafo fica mais cheio de ideias",
          "cada parágrafo entrega UM item: desinformação num, mídia no outro"),
         ("28", "Repetir no 2º parágrafo o argumento do 1º", "insistir na ideia parece reforçar a tese",
          "o 2º parágrafo entrega o OUTRO item: mesma arquitetura, eixo novo"),
         ("29", "Achar que um parágrafo “com citação” já é bom", "citar uma obra famosa impressiona",
          "mencionar não é usar: conteúdo + análise (faça o teste da retirada)")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


# ======================================================================
# questão 7 (tema de 2017)
# ======================================================================

Q7_FR = {1: "Assim, sem professores preparados em Libras, a escola continua excluindo quem deveria acolher.",
         2: "Em primeiro lugar, a falta de formação dos professores em Libras compromete a educação de estudantes surdos.",
         3: "A Lei nº 10.436/2002 reconhece a Língua Brasileira de Sinais como meio legal de comunicação e expressão.",
         4: "Isso ocorre porque, sem domínio da língua de sinais, o docente não consegue explicar os conteúdos ao aluno surdo.",
         5: "Apesar desse reconhecimento, muitas escolas ainda não contam com professores ou intérpretes capazes de usá-la, "
            "o que deixa o aluno surdo à margem das aulas."}
Q7_ORDEM = [2, 4, 3, 5, 1]
Q7_CUE = {1: "30.f1", 2: "30.f2", 3: "30.f3", 4: "31.f4", 5: "31.f5"}
Q7_ENUN = "A sequência que segue o modelo tópico frasal – argumento – repertório – análise – fechamento é"
ALT7 = [("A", "2 – 4 – 3 – 5 – 1", "31.A", None, "", GREEN),
        ("B", "3 – 2 – 4 – 1 – 5", "31.B", "33.xb", "fecho antes da análise", RED),
        ("C", "2 – 3 – 1 – 4 – 5", "31.C", "33.xc", "fecho no meio", RED),
        ("D", "1 – 2 – 3 – 4 – 5", "31.D", "33.xd", "começa pelo fecho", RED),
        ("E", "4 – 2 – 5 – 3 – 1", "31.E", "33.xe", "retoma o que não foi dito", RED)]
QX, QW, QS, QLH, QGAP = 262, 830, 23, 31, 16


def q7_layout(ordem):
    ys, y = {}, 330
    for n in ordem:
        ys[n] = y
        y += len(wrap(Q7_FR[n], "bold", QS, QW)) * QLH + QGAP
    return ys


_Q7_ORIG = q7_layout([1, 2, 3, 4, 5])
_Q7_NOVA = q7_layout(Q7_ORDEM)


def b_q7(c, t, C, B):
    sid = which(t, C, ["30", "31", "32", "33"])
    head(c, t, B["start"], "QUESTÃO 7 · ESTILO ENEM", "PONDO EM ORDEM", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["30.t"], 0.4)
    text(c, "ENEM 2017 · “" + TEMA17 + "”", 190, 210, 22, "black", BLUE, aa, align="left")
    text(c, "As frases abaixo, sobre o tema do Enem 2017, estão fora de ordem:", 190, 262, 23, "bold", INK,
         ep(t, C["30.a"], 0.4), align="left")
    pill(c, "Libras = Língua Brasileira de Sinais", 1080, 254, BLUE, size=18, a=ep(t, C["30.a"] + 1.5, 0.4),
         bounds=(0, 1920))
    u = ep(t, C["32.ok"] + 1.4, 1.2) if "32.ok" in C else 0
    for n in range(1, 6):
        a = ep(t, C[Q7_CUE[n]], 0.4)
        if a <= 0:
            continue
        y = lerp(_Q7_ORIG[n], _Q7_NOVA[n], ease_io(u))
        lines = wrap(Q7_FR[n], "bold", QS, QW)
        slot = Q7_ORDEM.index(n)
        key = KEYS[slot]
        eb = ep(t, C[f"32.e{slot + 1}"], 0.4) if f"32.e{slot + 1}" in C else 0
        if eb > 0:
            rrect(c, QX - 70, y - QS - 6, QW + 90, len(lines) * QLH + 6, 8, mix("#FFFFFF", PARTE[key], 0.18), eb)
            rrect(c, QX - 70, y - QS - 6, 6, len(lines) * QLH + 6, 3, PARTE[key], eb)
            pill(c, NOMEP[key], QX + QW + 30, y - 8, PARTE[key], size=17, a=eb, bounds=(0, 1920))
        badge_num(c, n, QX - 32, y - 8, a, 17, bg=INK2)
        for j, ln in enumerate(lines):
            text(c, ln, QX, y + j * QLH, QS, "bold", INK, a, align="left")
    # destaque "Apesar desse reconhecimento" × "reconhece"
    if sid == "33":
        q = lambda x: C[f"33.{x}"]
        a1, a2 = ep(t, q("a"), 0.6), ep(t, q("b"), 0.6)
        y5, y3 = _Q7_NOVA[5], _Q7_NOVA[3]
        line(c, QX, y5 + 7, QX + text_w("Apesar desse reconhecimento,", "bold", QS) * a1, y5 + 7, AMBER, 1.0, 5)
        x3 = QX + text_w("A Lei nº 10.436/2002 ", "bold", QS)
        line(c, x3, y3 + 7, x3 + text_w("reconhece", "bold", QS) * a2, y3 + 7, AMBER, 1.0, 5)
        if a2 > 0:
            arrow(c, QX - 60, y5 - 10, QX - 60, y3 - 2, AMBER, a2, 4, 14, progress=a2)
        ac = ep(t, q("c"), 0.4) * (1 - ep(t, q("xb"), 0.4))
        if ac > 0:
            rrect(c, 190, 742, 1180, 88, 14, mix("#FFFFFF", AMBER, 0.14), ac)
            text(c, "“Apesar desse reconhecimento” retoma a lei da frase 3:", 220, 776, 24, "black", INK, ac, align="left")
            text(c, "sem a lei antes, a expressão aponta para o nada", 220, 812, 24, "black", AMBER, ac, align="left")
    # enunciado e alternativas
    aq = ep(t, C["31.q"], 0.4)
    para(c, Q7_ENUN, 1430, 236, 19, "bold", INK, aq, 320, 25)
    alts_panel(c, t, C, ALT7, 1440, 410, 300, 28, "32.ok", "A", 6)
    pause_timer(c, t, C["31.end"] - 1.9, 1260, 740)
    if "32.ok" in C:
        ao = ep(t, C["32.ok"], 0.4) * (1 - ep(t, C["33.t"], 0.4))
        selo(c, 760, 760, ao, "2 – 4 – 3 – 5 – 1", GREEN, -3, 34)
    questao_rotulo(c, aa)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O SEGUNDO PARÁGRAFO", GREEN)
    aa = ep(t, C["35.a"], 0.4)
    text(c, "D1 · desinformação", 470, 250, 30, "black", PARTE["topico"], aa)
    mini_entrega(c, 470, 440, aa, [1, 1, 1, 1, 1], 1.4)
    selo(c, 470, 650, aa, "PRONTO ✓", GREEN, -4, 36)
    ab = ep(t, C["35.b"], 0.4)
    text(c, "D2 · mídia", 1300, 250, 30, "black", PARTE["argumento"], ab)
    if ab > 0:
        paper(c, 1010, 290, 580, 330, ab, lh=50, top=340)
        for k, key in enumerate(KEYS):
            y = 352 + k * 50
            text(c, ["Tópico", "Por quê", "Repertório", "Análise", "Fecho"][k], 1100, y, 22, "black", PARTE[key], ab,
                 align="left")
            line(c, 1250, y + 4, 1550, y + 4, LIGHT, ab, 3, dash=(10, 8))
        pen_draw(c, 1520, 600, PEN, ab, -35, 1.0)
    pill(c, "Ep. 6 · do rascunho ao texto, JUNTOS", W / 2, 740, GREEN, size=30, a=ep(t, C["35.c"], 0.4), anchor="center")


def b_cta(c, t, C, B):
    cta_dev(c, t, C, "36", "Qual das três versões parece com os seus parágrafos?")


BLOCKS = dict(hook=b_hook, entregas=b_entregas, promessa=b_promessa, prereq=b_prereq, eufaco=b_eufaco, tabela=b_tabela,
              arquitetura=b_arquitetura, v1=b_v1, v2=b_v2, tres=b_tres, mudou=b_mudou, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q7=b_q7, ponte=b_ponte, cta=b_cta)
