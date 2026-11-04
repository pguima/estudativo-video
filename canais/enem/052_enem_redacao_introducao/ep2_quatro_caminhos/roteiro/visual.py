"""Visual — Redação ENEM, Introdução, Episódio 2: Contextualizar — quatro caminhos (tema claro).
Usa o desenho da série (introducao_visual: etiqueta, rascunho com caligrafia, alternativas, recap, erros, CTA).
Novo: QUATRO PORTAS lado a lado com ícones (balança = lei/obra · ampulheta = história · gráfico = dado · livro aberto =
conceito), cada uma com o seu DEGRAU SOLTO em amarelo (o risco típico), e o selo "COLETÂNEA ≠ REPERTÓRIO".
Cores: azul = definição/tema · verde = funciona/método · âmbar = armadilha (degrau solto) · vermelho = erro · roxo = regra.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from introducao_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_introducao_ep2_quatro_caminhos.mp4"
ABERTURA = "Abertura elaborada para fins didáticos."


# ======================================================================
# as quatro portas
# ======================================================================

def ic_balanca(c, cx, cy, s, a, col):
    w = 4 * s
    line(c, cx, cy - 44 * s, cx, cy + 40 * s, col, a, w)
    line(c, cx - 30 * s, cy + 42 * s, cx + 30 * s, cy + 42 * s, col, a, 6 * s)
    line(c, cx - 54 * s, cy - 32 * s, cx + 54 * s, cy - 32 * s, col, a, w)
    c.drawCircle(cx, cy - 44 * s, 6 * s, paint(col, a))
    for sx in (-1, 1):
        px = cx + sx * 54 * s
        line(c, px, cy - 32 * s, px - 20 * s, cy + 2 * s, col, a, 2.5 * s)
        line(c, px, cy - 32 * s, px + 20 * s, cy + 2 * s, col, a, 2.5 * s)
        c.drawArc(skia.Rect.MakeXYWH(px - 24 * s, cy - 12 * s, 48 * s, 28 * s), 0, 180, True, paint(col, a))


def ic_ampulheta(c, cx, cy, s, a, col):
    top = skia.Path(); top.moveTo(cx - 34 * s, cy - 44 * s); top.lineTo(cx + 34 * s, cy - 44 * s); top.lineTo(cx, cy); top.close()
    bot = skia.Path(); bot.moveTo(cx, cy); bot.lineTo(cx + 34 * s, cy + 44 * s); bot.lineTo(cx - 34 * s, cy + 44 * s); bot.close()
    sand = skia.Path(); sand.moveTo(cx, cy + 14 * s); sand.lineTo(cx + 24 * s, cy + 44 * s); sand.lineTo(cx - 24 * s, cy + 44 * s); sand.close()
    c.drawPath(sand, paint(AMBER, a))
    for p in (top, bot):
        c.drawPath(p, paint(col, a, stroke=4 * s))
    for yy in (-48, 48):
        line(c, cx - 44 * s, cy + yy * s, cx + 44 * s, cy + yy * s, col, a, 7 * s)


def ic_grafico(c, cx, cy, s, a, col):
    line(c, cx - 46 * s, cy - 46 * s, cx - 46 * s, cy + 44 * s, col, a, 4 * s)
    line(c, cx - 46 * s, cy + 44 * s, cx + 48 * s, cy + 44 * s, col, a, 4 * s)
    for k, hh in enumerate((30, 56, 82)):
        rrect(c, cx - 32 * s + k * 26 * s, cy + 38 * s - hh * s, 18 * s, hh * s, 3 * s, col, a)


def ic_livro(c, cx, cy, s, a, col):
    for sx in (-1, 1):
        p = skia.Path()
        p.moveTo(cx + sx * 3 * s, cy - 30 * s); p.lineTo(cx + sx * 56 * s, cy - 40 * s)
        p.lineTo(cx + sx * 56 * s, cy + 32 * s); p.lineTo(cx + sx * 3 * s, cy + 42 * s); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", col, 0.18), a))
        c.drawPath(p, paint(col, a, stroke=4 * s))
        for k in range(3):
            y0 = cy - 18 * s + k * 16 * s
            line(c, cx + sx * 14 * s, y0, cx + sx * 44 * s, y0 - 4 * s, col, a * 0.8, 2.5 * s)


PORTAS = [("REPERTÓRIO", "lei · obra · filme · pensador", "referência coringa", ic_balanca),
          ("HISTÓRIA", "fato histórico", "data incerta", ic_ampulheta),
          ("DADO", "número com fonte", "número sem fonte", ic_grafico),
          ("CONCEITO", "definição", "definição óbvia", ic_livro)]


def porta(c, cx, by, k, a, s=1.0, lit=True, degrau=1.0, solto=0.0, label=True, risco=0.0, sub=0.0):
    """porta k (0–3) com a base em by; degrau = alpha do degrau; solto (0–1) o inclina; risco = alpha da pílula"""
    if a <= 0:
        return
    nome, desc, rsk, fn = PORTAS[k]
    col = BLUE if lit else LIGHT
    w, h = 210 * s, 320 * s
    x, y = cx - w / 2, by - h
    rrect(c, x - 12 * s, y - 12 * s, w + 24 * s, h + 12 * s, 16 * s, mix("#FFFFFF", col, 0.30), a)
    rrect(c, x, y, w, h, 10 * s, "#FFFFFF", a, stroke=4 * s, stroke_color=col)
    c.drawCircle(x + w - 28 * s, y + h * 0.58, 8 * s, paint(col, a))
    fn(c, cx, y + h * 0.36, 1.25 * s, a, col)
    if degrau > 0:
        da = a * degrau
        c.save()
        sw, sh = 250 * s, 26 * s
        sx0, sy0 = cx - sw / 2, by + 4 * s
        if solto > 0:
            c.translate(sx0 + sw, sy0)
            c.rotate(9 * ease_out(solto))
            c.translate(-(sx0 + sw), -sy0)
            c.translate(0, 8 * s * solto)
        rrect(c, sx0, sy0, sw, sh, 5 * s, AMBER if (lit or solto > 0) else mix(AMBER, "#FFFFFF", 0.55), da)
        if solto > 0:
            for q in range(3):
                qx = sx0 + sw * (0.3 + 0.2 * q)
                line(c, qx, sy0 + 4 * s, qx + 8 * s, sy0 + sh - 4 * s, mix(AMBER, "#000000", 0.35), da * solto, 2.5 * s)
        c.restore()
    if label:
        text(c, nome, cx, by + 80 * s, 34 * s, "black", col if lit else GRAY, a)
        if sub > 0:
            text(c, desc, cx, by + 118 * s, 22 * s, "bold", INK2, a * sub)
    if risco > 0:
        pill(c, rsk, cx, by + (150 if sub > 0 else 120) * s, AMBER, size=int(22 * s) + 2, a=a * risco, anchor="center",
             bounds=(0, 1920))


def quatro(c, t, cx0, gap, by, s, alphas, lit=None, degraus=None, solto=None, risco=None, sub=None):
    for k in range(4):
        porta(c, cx0 + k * gap, by, k, alphas[k], s, lit is None or lit == k or (isinstance(lit, (list, tuple)) and lit[k]),
              degraus[k] if degraus else 1.0, solto[k] if solto else 0.0, True, risco[k] if risco else 0.0,
              sub[k] if sub else 0.0)


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

PRIMORDIOS = "Desde os primórdios da humanidade…"


def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM · INTRODUÇÃO", "4 CAMINHOS PARA CONTEXTUALIZAR", BLUE)
    aa = ep(t, C["01.a"], 0.4)
    paper(c, 160, 190, 900, 440, aa, lh=60, top=250)
    hand(c, PRIMORDIOS, 260, 360, 40, PEN, aa, wreveal(t, (C["01.a"] + 0.2, C["01.a"] + 2.2)))
    for k in range(3):
        line(c, 270, 440 + k * 60, 960 - k * 90, 440 + k * 60, LIGHT, aa * 0.8, 6)
    ab = ep(t, C["01.b"], 0.4)
    if ab > 0:
        bubble(c, "Você já começou assim?", 300, 700, 560, BLUE, ab, size=34)
    ac = ep(t, C["01.c"], 0.4)
    if ac > 0:
        strike(c, 252, 348, 268 + hand_w(PRIMORDIOS, 40), 348, ac, RED, ac)
        selo(c, 760, 560, ac, "SERVE PARA QUALQUER TEMA", AMBER, -5, 30)
    ad = ep(t, C["01.d"], 0.5)
    for k in range(4):
        porta(c, 1300 + (k % 2) * 320, 420 + (k // 2) * 300, k, ep(t, C["01.d"] + 0.2 * k, 0.4), 0.55, label=True)
    text(c, "4 começos que DIZEM", 1460, 850, 38, "black", GREEN, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    aa = ep(t, C["02.a"], 0.5)
    ab = ep(t, C["02.b"], 0.5)
    text(c, "contextualizar um tema por 4 CAMINHOS", W / 2, 260, 44, "black", INK, aa)
    quatro(c, t, 420, 360, 610, 0.72, [ep(t, C["02.a"] + 0.25 * k, 0.4) for k in range(4)], degraus=[ab] * 4,
           risco=[ep(t, C["02.b"] + 0.3 + 0.25 * k, 0.4) for k in range(4)])
    text(c, "e o cuidado de cada um", W / 2, 330, 32, "bold", AMBER, ab)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "EPISÓDIO 1 EM 30 SEGUNDOS", "A ETIQUETA COMPLETA", PURPLE)
    a = ep(t, C["03.a"], 0.5)
    sh = [ep(t, C["03.b"], 0.4), ep(t, C["03.c"], 0.4), ep(t, C["03.d"], 0.4)]
    ae = ep(t, C["03.e"], 0.5)
    lit = [max(0.0, 1 - prog(t, C["03.c"], 0.4)) * sh[0] if ae <= 0 else 1.0,
           sh[1] * (1 - prog(t, C["03.d"], 0.4)) * (1 - ae), sh[2] * (1 - ae)]
    etiqueta_intro(c, 460, 200, 1000, a, show=sh, lit=lit, keys=("mapa", "tese", "lista"), movs=1.0, perguntas=1.0, rowh=120)
    if ae > 0:
        pill(c, "HOJE: O MAPA", 1500, 360, BLUE, size=30, a=ae, anchor="left", bounds=(0, 1920))


# ======================================================================
# o visitante e o conceito
# ======================================================================

FALAS = [("04.a", "Fica perto da escola que abriu em tal ano."), ("04.b", "É no bairro onde mora metade da cidade."),
         ("04.c", "É a rua da lei nova.")]


def b_visita(c, t, C, B):
    frame(c, t, B["start"], "ONDE FICA A SUA CASA?", "JEITOS DE SITUAR", BLUE)
    at = ep(t, C["04"], 0.5)
    person(c, 250, 560, INK2, at, 1.1)
    text(c, "visitante?", 250, 760, 26, "bold", GRAY, at)
    ad = ep(t, C["04.d"], 0.5)
    for k, (cue, s) in enumerate(FALAS):
        a, d = rise(t, C[cue])
        y = 210 + k * 170 + d
        bubble(c, s, 400, y, 760, [BLUE, GREEN, PURPLE][k], a, size=32)
        if ad > 0:
            arrow(c, 1180, y + 45, 1420, 470 + (k - 1) * 40, [BLUE, GREEN, PURPLE][k], ad, 5, 18,
                  progress=ep(t, C["04.d"] + 0.2 * k, 0.5))
    ae = ep(t, C["04.e"], 0.5)
    icone_peca(c, "tese", 1560, 460, at, 2.6, disc=False)
    text(c, "a sua casa", 1560, 600, 30, "black", MOV["tese"], at)
    pill(c, "todos levam à MESMA casa", 1560, 680, GREEN, size=28, a=ae, anchor="center", bounds=(0, 1920))


def b_conceito(c, t, C, B):
    frame(c, t, B["start"], "CONTEXTUALIZAR", "O MAPA DA ETIQUETA", BLUE)
    aa = ep(t, C["05.a"], 0.5)
    icone_peca(c, "mapa", 300, 300, aa, 1.6)
    text(c, "CONTEXTUALIZAR =", 430, 270, 30, "black", BLUE, aa, align="left", tracking=1)
    text(c, "dar ao leitor o PONTO DE PARTIDA da discussão", 430, 330, 40, "black", INK, aa, align="left")
    pill(c, "= o MAPA da etiqueta", 430, 400, BLUE, size=26, a=ep(t, C["05.b"], 0.4), bounds=(0, 1920))
    ac = ep(t, C["05.c"], 0.4)
    text(c, "4 PORTAS DE ENTRADA", W / 2 + 60, 470, 26, "black", GRAY, ac, tracking=2)
    ah = ep(t, C["05.h"], 0.5)
    alphas = [ep(t, C["05." + q], 0.4) for q in "defg"]
    quatro(c, t, 520, 300, 700, 0.5, alphas, degraus=[ah] * 4, solto=[ah] * 4)
    pill(c, "DEGRAU SOLTO = o risco típico de cada caminho", W / 2 + 60, 808, AMBER, size=24, a=ah, anchor="center",
         bounds=(0, 1920))


def b_tema(c, t, C, B):
    frame(c, t, B["start"], "TEMA REAL", "ENEM 2024", BLUE)
    aa = ep(t, C["06.a"], 0.5)
    text(c, "ENEM 2024", W / 2, 250, 26, "black", GRAY, aa, tracking=3)
    para(c, "“" + TEMA24 + "”", W / 2, 330, 50, "black", BLUE, aa, 1300, 62, align="center")
    ab = ep(t, C["06.b"], 0.5)
    paper(c, 360, 480, 1200, 330, ab, lh=56, top=520)
    hand(c, "1 abertura por porta:", 470, 590, 36, PEN, ab)
    for k in range(4):
        porta(c, 560 + k * 260, 760, k, ep(t, C["06.b"] + 0.5 + 0.2 * k, 0.4), 0.33, label=False, degrau=0.0)
    text(c, "só referências do material", 1480, 590, 22, "bold", GREEN, ab, align="right")


# ======================================================================
# as portas, uma a uma (cenas 07–14)
# ======================================================================

O1 = "A Lei nº 10.639, de 2003, tornou obrigatório o ensino de história e cultura afro-brasileira nas escolas."
O2 = "O Brasil aboliu a escravidão tardiamente, em 1888, sem políticas de integração da população liberta."
O3 = "Segundo o Censo 2022, do IBGE, pretos e pardos somam 55,5% da população."
O4 = "A Constituição, no art. 216, reconhece o patrimônio cultural imaterial do país."
S1 = ("A Lei número dez mil seiscentos e trinta e nove, de dois mil e três, tornou obrigatório o ensino de história e "
      "cultura afro-brasileira nas escolas.")
S2 = ("O Brasil aboliu a escravidão tardiamente, em mil oitocentos e oitenta e oito, sem políticas de integração da "
      "população liberta.")
S3 = ("Segundo o Censo dois mil e vinte e dois, do I B G E, pretos e pardos somam cinquenta e cinco vírgula cinco por "
      "cento da população.")
S4 = "A Constituição, no artigo duzentos e dezesseis, reconhece o patrimônio cultural imaterial do país."

# por porta: (cena da abertura, cena do degrau, definição, chips {b}/{c}, abertura tela, abertura falada, "funciona")
PDEF = [("07", "08", "conhecimento que você traz DE FORA da prova", ["lei", "obra", "filme", "pensador"], O1, S1,
         "fala DIRETO do recorte: valorizar a herança africana"),
        ("09", "10", "o passado explica um problema que PERSISTE", [], O2, S2, "explica por que a desvalorização continua"),
        ("11", "12", "um número que mostra o TAMANHO do problema", [], O3, S3, None),
        ("13", "14", "uma definição esclarece o que está em jogo", ["músicas", "festas", "saberes", "jeitos de fazer"], O4, S4,
         None)]
HEADS = [("07", "PORTA 1 DE 4", "REPERTÓRIO", BLUE), ("08", "PORTA 1 · DEGRAU SOLTO", "A REFERÊNCIA CORINGA", AMBER),
         ("09", "PORTA 2 DE 4", "CONTEXTO HISTÓRICO", BLUE), ("10", "PORTA 2 · DEGRAU SOLTO", "DATA INCERTA", AMBER),
         ("11", "PORTA 3 DE 4", "DADO", BLUE), ("12", "PORTA 3 · DEGRAU SOLTO", "NÚMERO SEM FONTE", AMBER),
         ("13", "PORTA 4 DE 4", "CONCEITO", BLUE), ("14", "PORTA 4 · DEGRAU SOLTO", "DEFINIÇÃO ÓBVIA", AMBER)]


def b_portas(c, t, C, B):
    ids = [h[0] for h in HEADS]
    sid = which(t, C, ids)
    i = ids.index(sid)
    n, degr = i // 2, i % 2 == 1
    head_seq(c, t, C, HEADS)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    cena, cdeg, defin, chips, otela, ofala, func = PDEF[n]
    # progresso das 4 portas (miniaturas no topo, à direita)
    for k in range(4):
        badge_num(c, k + 1, 1460 + k * 66, 200, 1, 20, bg=BLUE if k == n else (INK2 if k < n else LIGHT))
    solto = ep(t, q("a"), 0.6) if degr else 0.0
    porta(c, 370, 640, n, 1.0, 1.0, True, 1.0, solto, True, solto, sub=1.0 if not degr else 0.0)
    X = 640
    if not degr:
        aa = ep(t, q("a"), 0.4)
        text(c, defin, X, 280, 34, "black", INK, aa, align="left")
        if chips:
            cue_ch = q("a") if n == 0 else q("c")
            xx = X
            if n == 3:
                ab = ep(t, q("b"), 0.4)
                pill(c, "patrimônio cultural imaterial", X, 340, PURPLE, size=24, a=ab, bounds=(0, 1920))
                xx += text_w("patrimônio cultural imaterial", "bold", 24) + 80
                text(c, "=", xx - 34, 350, 28, "black", GRAY, ep(t, q("c"), 0.3))
            for j, s in enumerate(chips):
                ach = ep(t, cue_ch + 0.25 * j, 0.3)
                pill(c, s, xx, 340, BLUE, size=24, a=ach, bounds=(0, 1920))
                xx += text_w(s, "bold", 24) + 60
        aw = ep(t, q("w"), 0.4)
        paper(c, X, 390, 1100, 300, aw, lh=56, top=420)
        span = phrase_span(sid, ofala, q("w") + 0.8, q("w") + 7.0)
        hand_para(c, otela, X + 110, 490, 34, PEN, aw, 960, 56, wreveal(t, span))
        text(c, ABERTURA, X, 716, 16, "medium", GRAY, aw, align="left")
        if func:
            af = ep(t, q("c"), 0.4)
            check_icon(c, X + 20, 778, 22, af, GREEN)
            text(c, "funciona: " + func, X + 56, 788, 28, "black", GREEN, af, align="left")
        if n == 2:
            for j, s in enumerate(("fonte", "ano", "número")):
                ac = ep(t, q("c") + 0.35 * j, 0.3)
                check_icon(c, X + 20 + j * 220, 778, 22, ac, GREEN)
                text(c, s, X + 52 + j * 220, 788, 30, "black", GREEN, ac, align="left")
        return
    # ---------- degrau solto ----------
    if n == 0:
        aa = ep(t, q("a"), 0.4)
        rrect(c, X, 270, 1080, 220, 18, mix("#FFFFFF", AMBER, 0.10), aa)
        text(c, "“Segundo um pensador famoso, …”", X + 540, 360, 42, "black", INK2, aa)
        text(c, "+ qualquer tema", X + 540, 430, 30, "bold", GRAY, aa)
        ab = ep(t, q("b"), 0.4)
        selo(c, X + 540, 590, ab, "SERVE PARA TUDO = NÃO DIZ NADA", AMBER, -3, 34)
    elif n == 1:
        aa = ep(t, q("a"), 0.4)
        text(c, "Em 18??, …", X + 300, 380, 80, "black", INK2, aa)
        selo(c, X + 820, 370, aa, "TEM CERTEZA?", AMBER, 6, 34)
        ab = ep(t, q("b"), 0.4)
        text(c, "um ano errado derruba a confiança no resto", X + 540, 530, 32, "bold", RED, ab)
        pill(c, "na dúvida, NÃO ARRISQUE", X + 540, 640, GREEN, size=32, a=ep(t, q("c"), 0.4), anchor="center",
             bounds=(0, 1920))
    elif n == 2:
        aa = ep(t, q("a"), 0.4)
        rrect(c, X, 260, 1080, 150, 18, mix("#FFFFFF", AMBER, 0.10), aa)
        text_mid(c, "“Pesquisas mostram que 90%…”", X + 540, 335, 46, "black", INK2, aa)
        for j, s in enumerate(("Que pesquisas?", "De quem?", "De quando?")):
            bubble(c, s, X + 20 + j * 370, 450, 330, AMBER, ep(t, q("b") + 0.5 * j, 0.3), size=30, fg=INK)
        ac = ep(t, q("c"), 0.4)
        check_icon(c, X + 20, 690, 26, ac, RED, "x")
        text(c, "número INVENTADO ou SEM FONTE: ninguém consegue verificar", X + 60, 700, 30, "black", RED, ac, align="left")
        ok = ep(t, q("c") + 1.0, 0.4)
        pill(c, "o bom: fonte + ano + número (Censo 2022, IBGE)", X, 790, GREEN, size=24, a=ok, bounds=(0, 1920))
    else:
        ab = ep(t, q("b"), 0.4)
        rrect(c, X, 280, 1080, 180, 18, mix("#FFFFFF", AMBER, 0.10), ab)
        text(c, "DICIONÁRIO", X + 30, 320, 18, "black", AMBER, ab, align="left", tracking=2)
        text_mid(c, "“Cultura é o conjunto de costumes de um povo.”", X + 540, 390, 38, "black", INK2, ab)
        ac = ep(t, q("c"), 0.4)
        if ac > 0:
            strike(c, X + 70, 392, X + 1010, 392, ac, AMBER, ac)
        selo(c, X + 540, 560, ac, "O LEITOR JÁ SABE", AMBER, -4, 36)
        pill(c, "não acrescenta nada ao seu tema", X + 540, 680, RED, size=28, a=ep(t, q("c") + 0.8, 0.4), anchor="center",
             bounds=(0, 1920))


# ======================================================================
# coletânea ≠ repertório
# ======================================================================

def b_coletanea(c, t, C, B):
    frame(c, t, B["start"], "ARMADILHA", "O DADO DA COLETÂNEA", AMBER)
    aa = ep(t, C["15.a"], 0.5)
    proposta_page(c, 200, 180, 520, 620, ep(t, C["15"], 0.5), hl=(0, aa, 0), dim=0.6)
    text(c, "textos motivadores = textos de apoio da PRÓPRIA PROVA", 760, 240, 26, "bold", INK2, aa, align="left")
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        rrect(c, 760, 280, 470, 120, 14, "#FFFFFF", ab, shadow=True)
        text(c, "DADO DO TEXTO II", 785, 318, 16, "black", GRAY, ab, align="left", tracking=2)
        for k in range(3):
            rrect(c, 790 + k * 60, 380 - (20 + 14 * k), 40, 20 + 14 * k, 3, BLUE, ab)
        line(c, 990, 350, 1200, 350, LIGHT, ab, 6)
        line(c, 990, 375, 1150, 375, LIGHT, ab, 6)
        selo(c, 1480, 340, ab, "COLETÂNEA ≠ REPERTÓRIO", RED, -5, 30)
    ac = ep(t, C["15.c"], 0.5)
    arrow(c, 790, 450, 870, 450, GREEN, ac, 4, 14, progress=ac)
    text(c, "PARÁFRASE, breve: a mesma ideia com as SUAS palavras", 890, 462, 28, "black", GREEN, ac, align="left")
    ad = ep(t, C["15.d"], 0.5)
    check_icon(c, 800, 530, 18, ad, RED, "x")
    text(c, "não substitui conhecimento SEU", 830, 540, 28, "black", RED, ad, align="left")
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        rrect(c, 780, 590, 920, 220, 12, PAPER, ae, shadow=True)
        for k in range(4):
            y = 630 + k * 44
            if k == 1:
                rrect(c, 800, y - 18, 880, 34, 6, mix("#FFFFFF", RED, 0.10), ae)
                line(c, 820, y, 1180, y, mix("#FFFFFF", INK2, 0.75), ae, 6)
                text(c, "LINHA FANTASMA: copiada, não conta", 1670, y + 8, 22, "black", RED, ae, align="right")
            else:
                line(c, 820, y, 1600 - k * 70, y, PEN, ae * 0.55, 5)


# ======================================================================
# nós fazemos
# ======================================================================

EX = [("16", "Sancionada em 2003, a Lei nº 10.639 levou a história e a cultura afro-brasileira para a sala de aula.", 0,
       "risco: virar CORINGA → a frase seguinte liga a lei ao recorte"),
      ("17", "Mais da metade da população brasileira é preta ou parda: 55,5%, segundo o Censo 2022.", 2,
       "risco: número sem fonte → aqui tem FONTE e ANO: dá para verificar")]


def b_exercicio(c, t, C, B):
    sid = which(t, C, ["16", "17"])
    n = 0 if sid == "16" else 1
    _, frase, porta_ok, risco = EX[n]
    head(c, t, C[sid], f"NÓS FAZEMOS · ABERTURA {n + 1} DE 2", "QUAL PORTA? QUAL RISCO?", GREEN)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, q("a"), 0.4)
    rrect(c, 200, 200, 1520, 170, 16, mix("#FFFFFF", BLUE, 0.07), aa)
    para(c, "“" + frase + "”", 240, 265, 34, "black", INK, aa, 1440, 44)
    text(c, ABERTURA, 200, 394, 16, "medium", GRAY, aa, align="left")
    ar = ep(t, q("r"), 0.4)
    ak = ep(t, q("k"), 0.4)
    for k in range(4):
        lit = ar <= 0 or k == porta_ok
        porta(c, 420 + k * 360, 700, k, aa * (1 if lit else 0.45), 0.5, lit, 1.0, 0.0, True)
        if ar <= 0:
            text_mid(c, "?", 420 + k * 360, 560, 60, "black", GRAY, aa * 0.6)
    pause_timer(c, t, q("p") + 0.3, 1700, 520)
    if ar > 0:
        cx = 420 + porta_ok * 360
        c.drawCircle(cx, 560, 140, paint(GREEN, 0.10 * ar))
        check_icon(c, cx + 80, 470, 26, ar, GREEN)
    pill(c, risco, W / 2, 815, AMBER, size=26, a=ak, anchor="center", bounds=(0, 1920))


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["Lei, história, dado ou conceito: quatro portas para o mesmo tema.",
          "Cada porta tem um degrau solto: coringa, data errada, número sem fonte, óbvio.",
          "Dado da coletânea não é repertório seu."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("18", "28"), FRASES, [BLUE, AMBER, RED])


ERROS = [("19", "Abrir com frase universal: “Desde os primórdios…”, “Hoje em dia, muito se fala…”",
          "soa elegante e serve para começar qualquer redação", "contextualize o RECORTE, não a humanidade"),
         ("20", "Inventar um número para parecer preciso", "número dá cara de pesquisa séria",
          "número que ninguém verifica fragiliza o argumento: use só dado com FONTE"),
         ("21", "Usar como repertório o dado do texto motivador", "é um dado oficial, bem ali na sua frente",
          "é informação da prova: retome por paráfrase e traga algo SEU")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


# ======================================================================
# questões 2 e 8
# ======================================================================

TRECHO2 = ("O Brasil foi o último país das Américas a abolir a escravidão, em 1888, e o fez sem nenhuma política de "
           "integração da população liberta.")
ALT2 = [("A", "um contexto histórico, usado para explicar a origem de um problema que persiste.", "22.A", None, "", GREEN),
        ("B", "um dado estatístico, usado para dimensionar o problema.", "22.B", "24.xb", "data ≠ dado: nada é medido", RED),
        ("C", "um conceito sociológico, usado para definir o que está em jogo.", "23.C", "24.xc", "nenhum conceito é definido", RED),
        ("D", "uma obra literária, usada como analogia.", "23.D", "24.xd", "não aparece no trecho", RED),
        ("E", "uma experiência vivida, usada como ilustração.", "23.E", "24.xe", "não aparece no trecho", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 DO MATERIAL", "QUE TIPO DE CONTEXTUALIZAÇÃO?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["22.a"], 0.4)
    text(c, "TEMA · ENEM 2024", 190, 230, 16, "black", GRAY, aa, align="left", tracking=2)
    h = para(c, "“" + TEMA24 + "”", 190, 270, 24, "black", BLUE, aa, 540, 30)
    af = ep(t, C["22.f"], 0.4)
    text(c, "INÍCIO DA INTRODUÇÃO", 190, 270 + h + 30, 16, "black", GRAY, af, align="left", tracking=2)
    h2 = para(c, "“" + TRECHO2 + "”", 190, 270 + h + 70, 24, "bold", INK, af, 540, 30)
    para(c, "Essa contextualização recorre principalmente a", 190, 270 + h + 70 + h2 + 20, 22, "black", INK2,
         ep(t, C["22.q"], 0.4), 540, 28)
    alts_panel(c, t, C, ALT2, 790, 240, 950, 26, "24.ok", "A", 8)
    pause_timer(c, t, C["23.p"] + 0.3, 1600, 760)
    ao = ep(t, C["24.ok"], 0.4)
    porta(c, 1580, 760, 1, ao, 0.42, label=False)
    questao_rotulo(c, aa)


ALT8 = [("A", "Segundo o Censo 2022 do IBGE, pretos e pardos somam 55,5% da população brasileira — maioria que contrasta "
              "com o espaço reduzido da cultura afro-brasileira nos currículos.", "25.A", None, "", GREEN),
        ("B", "Pesquisas mostram que 90% dos brasileiros desconhecem a cultura africana.", "25.B", "27.xb", "número sem fonte", RED),
        ("C", "Segundo especialistas, a herança africana é a mais importante do mundo.", "26.C", "27.xc",
         "especialistas anônimos, juízo vago", RED),
        ("D", "Todo mundo sabe que a maioria das pessoas valoriza a cultura africana.", "26.D", "27.xd", "senso comum, sem base", RED),
        ("E", "Segundo o Censo 2022, a população brasileira está envelhecendo.", "26.E", "27.xe", "dado de outro assunto", RED)]
MARCAS = [("27.m1", "FONTE E ANO", "Censo 2022 · IBGE"), ("27.m2", "PERTINÊNCIA", "composição da população"),
          ("27.m3", "INTERPRETAÇÃO", "maioria × pouco espaço nos currículos")]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 DO MATERIAL", "O DADO LEGÍTIMO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["25.a"], 0.4)
    para(c, "Para contextualizar o tema do Enem 2024, “" + TEMA24 + "”, o uso de dado mais adequado é:", 190, 230, 26,
         "black", INK, aa, 1500, 34)
    ok = ep(t, C["27.ok"], 0.5)
    alts_panel(c, t, C, ALT8, 190, 340, 1080, 24, "27.ok", "A", 7)
    pause_timer(c, t, C["26.p"] + 0.3, 1500, 520)
    if ok > 0:
        x0 = 1330
        rrect(c, x0, 280, 400, 520, 18, mix("#FFFFFF", GREEN, 0.07), ok)
        text(c, "AS 3 MARCAS", x0 + 200, 330, 22, "black", GREEN, ok, tracking=2)
        text(c, "DO DADO BOM", x0 + 200, 362, 22, "black", GREEN, ok, tracking=2)
        for k, (cue, s1, s2) in enumerate(MARCAS):
            a = ep(t, C[cue], 0.4)
            y = 440 + k * 120
            check_icon(c, x0 + 40, y, 20, a, GREEN)
            text(c, s1, x0 + 72, y + 8, 24, "black", INK, a, align="left")
            para(c, s2, x0 + 72, y + 44, 20, "bold", GRAY, a, 310, 24)
    questao_rotulo(c, aa)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A PONTE", GREEN)
    aa = ep(t, C["29.a"], 0.5)
    icone_peca(c, "mapa", 380, 420, aa, 2.0)
    text(c, "MAPA", 380, 560, 30, "black", BLUE, aa)
    icone_peca(c, "tese", 1540, 420, aa, 2.0)
    text(c, "CASA (o recorte)", 1540, 560, 30, "black", MOV["tese"], aa)
    ab = ep(t, C["29.b"], 0.5)
    if ab < 1:
        line(c, 500, 420, 1000, 420, GRAY, aa * (1 - ab), 6, dash=(18, 14), progress=prog(t, C["29.a"] + 0.4, 1.2))
        xmark(c, 1080, 420, 26, aa * (1 - ab) * ep(t, C["29.a"] + 1.6, 0.3))
    if ab > 0:
        arrow(c, 500, 420, 1410, 420, GREEN, ab, 8, 24, progress=ab)
        icone_peca(c, "rua", 960, 420, ab, 1.6)
        text(c, "PONTE: liga a referência ao recorte", 960, 560, 34, "black", GREEN, ab)
    selo(c, W / 2, 700, ep(t, C["29.c"], 0.4), "+ O TESTE DA RETIRADA", AMBER, -3, 36)


def b_cta(c, t, C, B):
    cta_intro(c, t, C, "30", "Qual das 4 portas você usaria no tema de 2024?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, visita=b_visita, conceito=b_conceito, tema=b_tema,
              portas=b_portas, coletanea=b_coletanea, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2,
              q8=b_q8, ponte=b_ponte, cta=b_cta)
