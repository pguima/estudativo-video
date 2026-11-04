"""Visual — Redação ENEM, Introdução, Episódio 6: Oficina — montando uma introdução do zero (tema claro).
Usa o desenho da série (introducao_visual: etiqueta de 4 peças, rascunho com caligrafia, recap, erros, CTA com Anki).
Novo: CHECKLIST dos 6 passos (seção 09) fixo à esquerda (passo atual aceso, feitos com ✓) + RASCUNHO à direita, onde o
professor escreve ao vivo no ritmo da fala: tema de 2022, tese provisória, eixos, 1ª TENTATIVA (riscada com ✗), referência
constitucional, ponte, tese final; depois a conferência com a frase temática em cima e ✓ em cada bloco.
Cores: azul = tema/blocos · verde = método · âmbar = armadilha · vermelho = erro · roxo = regra oficial ·
peças da etiqueta em MOV (mapa azul, rua verde, tese laranja, lista azul-petróleo).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from introducao_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_introducao_ep6_oficina_seis_passos.mp4"

NUC, DEL = BLUE, GREEN
PASSOS = [("Tese provisória", "a resposta à pergunta-problema"),
          ("Eixos", "os dois argumentos, cada um com seu repertório"),
          ("Contextualização", "a referência que melhor prepara a tese"),
          ("Ponte", "a frase que liga a referência ao recorte"),
          ("Tese final", "a tese reescrita já com os dois eixos"),
          ("Conferência", "cobre os blocos? a conclusão vai retomá-la?")]

CURTO = ["Tese provisória", "Eixos", "Contexto", "Ponte", "Tese final", "Conferência"]

# material, seção 10 (tema de 2022)
TESEP = ("a valorização esbarra na insegurança sobre o território e no desconhecimento de seus modos de vida")
EIXO_A = "sem terra garantida, os modos de vida tradicionais não se sustentam"
EIXO_B = "a escola e a mídia pouco mostram esses povos fora de estereótipos"
TENTATIVA = "Desde os primórdios, os povos indígenas..."
S1 = ("A Constituição Federal de 1988 reconhece aos povos indígenas seus costumes, línguas e tradições, bem como os "
      "direitos sobre as terras que tradicionalmente ocupam, e assegura às comunidades quilombolas a propriedade de seus "
      "territórios.")
S1_FALA = S1.replace("1988", "mil novecentos e oitenta e oito")
S2 = ("Na prática, contudo, muitos desses grupos ainda lutam pela demarcação ou pela titulação de suas terras e são "
      "retratados de forma estereotipada, como se pertencessem apenas ao passado.")
S3 = ("Assim, a valorização das comunidades e dos povos tradicionais no Brasil depende de superar dois obstáculos: a "
      "insegurança territorial, que ameaça seus modos de vida, e o desconhecimento da sociedade sobre suas culturas.")
T22 = [("Desafios para", DEL, None, None, "09.b"), ("a valorização", DEL, None, None, "09.c"),
       ("de comunidades e povos tradicionais", NUC, None, None, "09.d"), ("no Brasil", DEL, None, None, "09.e")]

# área principal (à direita do checklist)
MX, MY, MW, MH = 470, 150, 1410, 700
DX = (MX + MW / 2) - W / 2
TX, TW = MX + 110, MW - 170     # texto manuscrito no rascunho


# ======================================================================
# utilidades
# ======================================================================

def checklist(c, cur, a=1.0, feitos=None, lit=None, x=40, y=150, w=400):
    """6 passos; cur = índice aceso (0–5) ou None; feitos = quantos já têm ✓; lit[k] = alpha de cada linha"""
    if a <= 0:
        return
    feitos = cur if feitos is None and cur is not None else (feitos or 0)
    rrect(c, x, y, w, 700, 24, "#FFFFFF", a, shadow=True)
    text(c, "CHECKLIST · 6 PASSOS", x + w / 2, y + 48, 20, "black", GRAY, a, tracking=2)
    for k, (nm, sub) in enumerate(PASSOS):
        la = a * (lit[k] if lit else 1.0)
        if la <= 0:
            continue
        yy = y + 80 + k * 102
        on_ = k == cur
        if on_:
            rrect(c, x + 14, yy - 8, w - 28, 98, 16, mix("#FFFFFF", GREEN, 0.14), la)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 14, yy - 8, w - 28, 98), 16, 16),
                        paint(GREEN, la, stroke=3))
        if k < feitos:
            check_icon(c, x + 52, yy + 26, 22, la, GREEN)
        else:
            badge_num(c, k + 1, x + 52, yy + 26, la, 22, bg=GREEN if on_ else LIGHT)
        text(c, nm, x + 90, yy + 36, 28, "black", INK if (on_ or k < feitos) else GRAY, la, align="left")
        if on_:
            para(c, sub, x + 90, yy + 62, 15, "bold", GREEN, la, w - 110, 17)


def rascunho(c, a=1.0):
    paper(c, MX, MY, MW, MH, a, lh=48, top=MY + 52)


def tema_topo(c, a=1.0, reveal=1.0, y=MY + 64):
    text(c, "ENEM 2022", TX, y - 6, 16, "black", BLUE, a, align="left", tracking=2)
    hand(c, TEMA22, TX + 120, y, 26, BLUE, a, reveal)


def span(sid, phrase, C, dur=4.0, cue=None):
    t0 = C[cue] if cue else C[sid]
    return phrase_span(sid, phrase, t0, t0 + dur)


def hpara(c, s, y, size=28, lh=46, a=1.0, reveal=1.0, color=None, x=None, maxw=None):
    """parágrafo manuscrito; retorna o y logo abaixo"""
    n = hand_para(c, s, x or TX, y, size, color or PEN, a, maxw or TW, lh, reveal)
    return y + n * lh


def eixos_strip(c, a=1.0, y=MY + 112):
    if a <= 0:
        return
    text(c, "CAIXA ARRUMADA:", TX, y + 8, 16, "black", GRAY, a, align="left", tracking=2)
    pill(c, "A · território", TX + 200, y, MOV["lista"], size=20, a=a, bounds=(0, 1920))
    pill(c, "B · desconhecimento", TX + 400, y, MOV["lista"], size=20, a=a, bounds=(0, 1920))


def tentativa_riscada(c, y, a=1.0, strike_p=1.0, size=26):
    hand(c, TENTATIVA, TX, y, size, GRAY, a * 0.9)
    w_ = hand_w(TENTATIVA, size)
    if strike_p > 0:
        strike(c, TX - 4, y - size * 0.3, TX + 4 + w_, y - size * 0.3, a, RED, strike_p)
        check_icon(c, TX + w_ + 40, y - size * 0.3, 18, a * clamp(strike_p * 2), RED, "x")


def clock(c, cx, cy, r, a, frac, label):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r + 12, paint(GREEN, a * 0.16))
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 360 * clamp(frac), False,
              paint(GREEN, a, stroke=r * 0.16, cap_round=True))
    text_mid(c, label, cx, cy - 8, r * 0.42, "black", INK, a)
    text(c, "de rascunho", cx, cy + r * 0.38, r * 0.16, "bold", GRAY, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM · INTRODUÇÃO", "OFICINA: DO ZERO", GREEN)
    aa = ep(t, C["01.a"], 0.5)
    paper(c, 200, 230, 760, 560, aa, lh=52, top=290, rot=-2)
    ab = ep(t, C["01.b"], 0.5)
    pen_draw(c, 900, 420, PEN, ab, -30, 0.9)
    ac = ep(t, C["01.c"], 0.5)
    hand(c, "Introdução", 300, 330, 44, PEN, ac, wreveal(t, (C["01.c"], C["01.c"] + 1.6)), bold=True)
    for k in range(4):
        line(c, 300, 400 + k * 52, 860 - (k % 2) * 120, 400 + k * 52, LIGHT, ac * ep(t, C["01.c"] + 1.0 + 0.3 * k, 0.3), 7)
    for k in range(6):
        a, d = rise(t, C["01.d"] + 0.18 * k)
        x = 1180 + (k % 3) * 190
        y = 380 + (k // 3) * 220 + d
        c.drawCircle(x, y, 74, paint(mix("#FFFFFF", GREEN, 0.14), a))
        badge_num(c, k + 1, x, y, a, 50, bg=GREEN)
        text(c, CURTO[k], x, y + 110, 24, "black", INK2, a)


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DA AULA", "UMA ORDEM DE TRABALHO", GREEN)
    aa = ep(t, C["02.a"], 0.5)
    checklist(c, None, aa, x=260, y=190, w=400, lit=[ep(t, C["02.a"] + 0.2 * k, 0.3) for k in range(6)])
    ab = ep(t, C["02.b"], 0.5)
    clock(c, 1180, 470, 190, ab, prog(t, C["02.b"], 2.5), "10 min")
    text(c, "para QUALQUER introdução", 1180, 760, 32, "black", GREEN, ab)


def marcador(c, x, y, col, a, ang=-20):
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.rotate(ang)
    rrect(c, -24, -130, 48, 200, 14, col, a, shadow=True)
    rrect(c, -24, -130, 48, 40, 12, mix(col, "#000000", 0.25), a)
    p = skia.Path(); p.moveTo(-24, 70); p.lineTo(24, 70); p.lineTo(10, 110); p.lineTo(-10, 110); p.close()
    c.drawPath(p, paint(mix(col, "#000000", 0.15), a))
    c.restore()


def b_material(c, t, C, B):
    frame(c, t, B["start"], "SEPARE AGORA", "PAPEL, CANETA E DUAS CORES", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    paper(c, 250, 230, 520, 400, aa, lh=48, top=290, rot=-3)
    text(c, "folha", 510, 690, 32, "black", INK2, aa)
    ab = ep(t, C["03.b"], 0.5)
    pen_draw(c, 960, 430, PEN, ab, 0, 1.0)
    text(c, "caneta", 960, 690, 32, "black", INK2, ab)
    ac = ep(t, C["03.c"], 0.5)
    marcador(c, 1240, 440, MOV["mapa"], ac, -12)
    marcador(c, 1400, 440, MOV["tese"], ep(t, C["03.c"] + 0.3, 0.5), 12)
    text(c, "+ 2 cores", 1320, 690, 32, "black", INK2, ac)
    ad = ep(t, C["03.d"], 0.4)
    pill(c, "uma cor para cada parte do parágrafo", W / 2, 770, GREEN, size=26, a=ad, anchor="center", bounds=(0, 1920))


# ======================================================================
# pré-requisitos
# ======================================================================

def b_prereq(c, t, C, B):
    sid = which(t, C, ["04", "05"])
    head_seq(c, t, C, [("04", "PRÉ-REQUISITOS · 45 s", "DA LEITURA DA PROPOSTA", BLUE),
                       ("05", "PRÉ-REQUISITOS · 45 s", "DESTA SÉRIE", BLUE)])
    card(c, *CARD_R)
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        c.save(); c.translate(0, 0)
        puzzle(c, t, C, T22, 290, aa, 26, [ep(t, C["04.a"] + 0.25 * k, 0.3) for k in range(4)], obriga=False)
        c.restore()
        text(c, "cada BLOCO é uma exigência", W / 2, 470, 40, "black", BLUE, aa)
        ab = ep(t, C["04.b"], 0.5)
        rrect(c, 360, 560, 1200, 190, 20, mix("#FFFFFF", GREEN, 0.08), ab)
        text(c, "TESE PROVISÓRIA", W / 2, 620, 22, "black", GREEN, ab, tracking=3)
        text(c, "a primeira resposta ao tema, que ainda pode mudar", W / 2, 690, 36, "black", INK, ab)
        return
    show = [ep(t, C["05.c"], 0.4), ep(t, C["05.d"], 0.4), ep(t, C["05.e"], 0.4), ep(t, C["05.e"] + 1.6, 0.4)]
    lit = [prog(t, C["05.c"], 0.4) * (1 - prog(t, C["05.d"], 0.3)), prog(t, C["05.d"], 0.4) * (1 - prog(t, C["05.e"], 0.3)),
           prog(t, C["05.e"], 0.4), prog(t, C["05.e"] + 1.6, 0.4)]
    etiqueta_intro(c, 340, 190, 1100, 1.0, show=show, lit=lit, perguntas=0.0, rowh=110)
    ac = ep(t, C["05.c"] + 1.4, 0.4)
    for k, s in enumerate(["lei", "história", "dado", "conceito"]):
        pill(c, s, 1620, 330 + k * 56, MOV["mapa"], size=22, a=ac * ep(t, C["05.c"] + 1.4 + 0.25 * k, 0.3),
             anchor="center", bounds=(0, 1920))


def b_caixa(c, t, C, B):
    frame(c, t, B["start"], "A ORDEM CERTA", "A CAIXA ANTES DA ETIQUETA", GREEN)
    aa = ep(t, C["06.t"], 0.5)
    q = 1 - ep(t, C["06.b"], 0.4)
    if q > 0:
        text(c, "colar a lista antes de saber o que vai dentro?", W / 2, 260, 40, "black", INK, aa * q)
        xmark(c, W / 2, 470, 90, ep(t, C["06.a"], 0.4) * q)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        badge_num(c, 1, 360, 240, ab, 30, bg=GREEN)
        text(c, "arrume a CAIXA", 410, 252, 36, "black", GREEN, ab, align="left")
        caixa(c, 300, 470, 320, 210, ab, open_=1 - ep(t, C["06.c"], 0.6) * 1.0 + 0.0,
              inner="eixo A · eixo B", inner_a=ep(t, C["06.b"] + 0.6, 0.6) * (1 - ep(t, C["06.c"], 0.4)))
        ac = ep(t, C["06.c"], 0.5)
        arrow(c, 700, 520, 860, 520, GREEN, ac, 6, 20, progress=ac)
        badge_num(c, 2, 960, 240, ac, 30, bg=MOV["lista"])
        text(c, "depois, a ETIQUETA", 1010, 252, 36, "black", MOV["lista"], ac, align="left")
        mini_etiqueta(c, 1160, 520, ac, [None, None, None, None], 1.3)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        rrect(c, 300, 720, 1320, 100, 20, mix("#FFFFFF", PURPLE, 0.08), ad)
        text_mid(c, "a introdução é a 1ª a ser LIDA", 660, 770, 34, "black", INK, ad)
        text_mid(c, "mas não a 1ª a ser PENSADA", 1300, 770, 34, "black", GREEN, ep(t, C["06.e"], 0.4))


def b_passos(c, t, C, B):
    sid = which(t, C, ["07", "08"])
    head(c, t, B["start"], "SEÇÃO 09 DO MATERIAL", "OS 6 PASSOS NO RASCUNHO", GREEN)
    cues = ["07.a", "07.b", "07.c", "08.d", "08.e", "08.f"]
    lit = [ep(t, C[q], 0.4) for q in cues]
    cur = max([k for k in range(6) if t >= C[cues[k]] - 0.05] or [0])
    checklist(c, cur if t < C["08.g"] else 2, 1.0, feitos=0, lit=lit)
    card(c, MX, MY, MW, MH)
    nm, sub = PASSOS[cur]
    a = ep(t, C[cues[cur]], 0.4)
    if t < C["08.g"]:
        badge_num(c, cur + 1, MX + 160, MY + 200, a, 60, bg=GREEN)
        text(c, nm, MX + 260, MY + 220, 64, "black", INK, a, align="left")
        para(c, sub, MX + 260, MY + 310, 38, "bold", GREEN, a, MW - 320, 48)
        # trilha: caixa (1–2) → etiqueta (3–5) → conferência (6)
        fases = [("ARRUMAR A CAIXA", (0, 1), KRAFT), ("ESCREVER A ETIQUETA", (2, 3, 4), MOV["lista"]), ("CONFERIR", (5,), PURPLE)]
        x = MX + 120
        for nmf, idx, col in fases:
            ww = 360 if len(idx) > 1 else 300
            on_ = cur in idx
            rrect(c, x, MY + 520, ww, 90, 16, mix("#FFFFFF", col, 0.18 if on_ else 0.05), 1.0)
            text_mid(c, nmf, x + ww / 2, MY + 565, 24, "black", col if on_ else LIGHT, 1.0)
            x += ww + 40
        return
    ag = ep(t, C["08.g"], 0.5)
    text(c, "a etiqueta só aparece no passo", MX + MW / 2, MY + 150, 40, "black", INK, ag)
    badge_num(c, 3, MX + MW / 2, MY + 260, ag, 56, bg=MOV["lista"])
    mini_etiqueta(c, MX + MW / 2, MY + 440, ag, [None] * 4, 1.2)
    metodo_selo(c, MX + MW / 2, MY + 620, ep(t, C["08.h"], 0.4), -3, 30)
    text(c, METODO, MX + MW / 2, MY + 690, 22, "bold", GREEN, ep(t, C["08.h"], 0.4))


# ======================================================================
# eu faço: tema de 2022
# ======================================================================

def b_tema(c, t, C, B):
    sid = which(t, C, ["09", "10"])
    head(c, t, B["start"], "EU FAÇO · ENEM 2022", "O TEMA EM BLOCOS", BLUE)
    checklist(c, None, 1.0)
    rascunho(c)
    aa = ep(t, C["09.a"], 0.4)
    tema_topo(c, aa, wreveal(t, span("09", TEMA22, C, 5.0, "09.a")))
    c.save(); c.translate(DX, 0)
    puzzle(c, t, C, T22, MY + 200, ep(t, C["09.b"], 0.4), 26, [ep(t, C[s[4]], 0.4) for s in T22], obriga=False)
    c.restore()
    if sid == "10":
        rows = [("10.a", "indígenas", ""), ("10.b", "quilombolas", "comunidades formadas a partir dos antigos quilombos"),
                ("10.c", "ribeirinhos", "vivem à beira dos rios")]
        for k, (cue, nm, d) in enumerate(rows):
            a = ep(t, C[cue], 0.4)
            y = MY + 400 + k * 80
            person(c, TX + 30, y - 40, BLUE, a, 0.45)
            hand(c, nm, TX + 90, y, 34, BLUE, a, bold=True)
            if d:
                text(c, "= " + d, TX + 120 + hand_w(nm, 34, True), y - 4, 26, "bold", INK2, a, align="left")
        text(c, "… entre outros", TX + 90, MY + 640, 24, "bold", GRAY, ep(t, C["10.c"] + 1.0, 0.4), align="left")


def b_p1(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · PASSO 1", "A TESE PROVISÓRIA", GREEN)
    checklist(c, 0, 1.0)
    rascunho(c)
    tema_topo(c)
    aa = ep(t, C["11.a"], 0.4)
    bubble(c, "o que impede essa valorização?", TX, MY + 140, 640, mix("#FFFFFF", GREEN, 0.18), aa, size=30, fg=GREEN)
    ab = ep(t, C["11.b"], 0.4)
    text(c, "TESE PROVISÓRIA", TX, MY + 330, 18, "black", GREEN, ab, align="left", tracking=2)
    hpara(c, TESEP, MY + 390, 32, 52, ab, wreveal(t, span("11", TESEP, C, 6.0, "11.b")))


def notas_plano(c, t, C, ra=1.0):
    """tese provisória + eixos (já escritos), em tamanho de nota"""
    text(c, "TESE PROVISÓRIA", TX, MY + 128, 16, "black", GREEN, ra, align="left", tracking=2)
    hpara(c, TESEP, MY + 170, 26, 42, ra)


def b_p2(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · PASSO 2", "OS DOIS EIXOS", GREEN)
    checklist(c, 1, 1.0)
    rascunho(c)
    tema_topo(c)
    notas_plano(c, t, C)
    for k, (cue, nm, s) in enumerate([("12.a", "EIXO A · território", EIXO_A), ("12.b", "EIXO B · desconhecimento", EIXO_B)]):
        a = ep(t, C[cue], 0.4)
        y = MY + 300 + k * 140
        pill(c, nm, TX, y, MOV["lista"], size=22, a=a, bounds=(0, 1920))
        hpara(c, s, y + 64, 30, 46, a, wreveal(t, span("12", s, C, 4.0, cue)), maxw=TW - 320)
    ac = ep(t, C["12.c"], 0.5)
    caixa(c, MX + MW - 260, MY + 540, 180, 120, ac)
    selo(c, MX + MW - 170, MY + 480, ac, "CAIXA ARRUMADA", GREEN, -5, 24)


# ======================================================================
# passo 3: a primeira tentativa e a troca
# ======================================================================

VARIA = ["Desde os primórdios, a escrita...", "Desde os primórdios, a música..."]


def b_p3(c, t, C, B):
    sid = which(t, C, ["13", "14", "15", "16"])
    head_seq(c, t, C, [("13", "EU FAÇO · PASSO 3", "A CONTEXTUALIZAÇÃO", GREEN), ("14", "EU FAÇO · PASSO 3", "DOIS TESTES", AMBER),
                       ("15", "EU FAÇO · PASSO 3", "UMA REFERÊNCIA LIGADA AO RECORTE", PURPLE),
                       ("16", "EU FAÇO · PASSO 3", "O MAPA ESCRITO", GREEN)])
    checklist(c, 2, 1.0)
    rascunho(c)
    tema_topo(c)
    eixos_strip(c)
    yT = MY + 230
    if sid in ("13", "14"):
        ab = ep(t, C["13.b"], 0.3)
        pill(c, "TENTATIVA 1", TX, yT - 52, AMBER, size=20, a=ab, bounds=(0, 1920))
        text(c, "tentativa elaborada para fins didáticos", TX + 160, yT - 44, 18, "medium", AMBER, ab, align="left")
        lift = 0.0
        if sid == "14":
            ret = prog(t, C["14.e"], 0.6) * (1 - prog(t, C["14.g"], 0.5))
            lift = ret
        a_t = ab * (1 - 0.75 * lift)
        c.save(); c.translate(0, -60 * lift)
        hand(c, TENTATIVA, TX, yT, 40, PEN, a_t, wreveal(t, (C["13.b"], C["13.b"] + 2.6)))
        c.restore()
        if sid == "13":
            pill(c, "parece bonito...", TX + 300, yT + 100, AMBER, size=26, a=ep(t, C["13.c"], 0.4), anchor="center", bounds=(0, 1920))
            pill(c, "vamos testar", TX + 300, yT + 170, GREEN, size=26, a=ep(t, C["13.d"], 0.4), anchor="center", bounds=(0, 1920))
            return
        # teste 1
        a1 = ep(t, C["14.a"], 0.4)
        boxed(c, TX - 20, yT + 50, 600, 300, AMBER, a1, 0.06)
        text(c, "TESTE 1 · serve para qualquer tema?", TX, yT + 96, 22, "black", AMBER, a1, align="left")
        for k, s in enumerate(VARIA):
            hand(c, s, TX + 10, yT + 160 + k * 56, 28, GRAY, ep(t, C["14.b"] + 1.2 * k, 0.4))
        ac = ep(t, C["14.c"], 0.4)
        text(c, "SERVE → não diz nada sobre o MEU", TX, yT + 310, 24, "black", RED, ac, align="left")
        # teste 2
        a2 = ep(t, C["14.d"], 0.4)
        x2 = TX + 640
        boxed(c, x2 - 20, yT + 50, 600, 300, PURPLE, a2, 0.06)
        text(c, "TESTE 2 · teste da retirada", x2, yT + 96, 22, "black", PURPLE, a2, align="left")
        ae = ep(t, C["14.e"], 0.4)
        para(c, "apago a frase: o texto perde alguma coisa?", x2, yT + 160, 26, "bold", INK, ae, 560, 32)
        af = ep(t, C["14.f"], 0.4)
        text(c, "NÃO PERDE", x2, yT + 260, 34, "black", RED, af, align="left")
        text(c, "→ não estava trabalhando", x2, yT + 310, 24, "black", RED, ep(t, C["14.g"], 0.4), align="left")
        ah = prog(t, C["14.h"], 0.7)
        if ah > 0:
            w_ = hand_w(TENTATIVA, 40)
            strike(c, TX - 6, yT - 12, TX + 6 + w_, yT - 12, 1.0, RED, ah)
            xmark(c, TX + w_ + 60, yT - 14, 26, ep(t, C["14.h"] + 0.3, 0.4))
        return
    # 15–16: tentativa riscada pequena + referência
    tentativa_riscada(c, yT - 30, 1.0, 1.0, 26)
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        rrect(c, TX - 20, yT + 10, TW + 40, 440, 20, "#FFFFFF", aa, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(TX - 20, yT + 10, TW + 40, 440), 20, 20), paint(PURPLE, aa, stroke=4))
        cartilha_txt = "CONSTITUIÇÃO FEDERAL DE 1988"
        text(c, cartilha_txt, TX + 10, yT + 64, 24, "black", PURPLE, aa, align="left", tracking=2)
        ab = ep(t, C["15.b"], 0.4)
        pill(c, "art. 231", TX + 10, yT + 120, PURPLE, size=22, a=ab, bounds=(0, 1920))
        para(c, "reconhece aos indígenas sua organização social, costumes, línguas, crenças e tradições, e os direitos "
                "sobre as terras que tradicionalmente ocupam", TX + 150, yT + 132, 28, "bold", INK, ab, TW - 170, 36)
        ac = ep(t, C["15.c"], 0.4)
        pill(c, "art. 68 do ADCT", TX + 10, yT + 290, PURPLE, size=22, a=ac, bounds=(0, 1920))
        para(c, "assegura aos remanescentes das comunidades dos quilombos a propriedade das terras que ocupam",
             TX + 250, yT + 302, 28, "bold", INK, ac, TW - 270, 36)
        text(c, "ADCT = Ato das Disposições Constitucionais Transitórias", TX + 10, yT + 420, 20, "medium", GRAY, ac, align="left")
        return
    at = ep(t, C["16.t"], 0.4)
    pill(c, "fala de TERRA = eixo A", TX + 760, yT - 52, MOV["lista"], size=22, a=at, bounds=(0, 1920))
    icone_peca(c, "mapa", MX + 44, yT + 40, ep(t, C["16.a"], 0.4), 0.42)
    hpara(c, S1, yT + 50, 30, 50, 1.0, wreveal(t, span("16", S1_FALA, C, 12.0, "16.a")))


# ======================================================================
# passos 4 e 5 + introdução pronta
# ======================================================================

def paragrafo(c, t, C, y, reveal=(1.0, 1.0, 1.0), size=30, lh=50, marks=0.0, icons=1.0, hl_ponte=0.0, show=(1, 1, 1)):
    """as 3 frases da introdução, cada uma numa linha nova; marks = sublinhado com a cor da peça"""
    cols = [MOV["mapa"], MOV["rua"], MOV["tese"]]
    keys = ["mapa", "rua", "tese"]
    for k, s in enumerate((S1, S2, S3)):
        if show[k] <= 0:
            continue
        lines = hwrap(s, size, TW)
        if marks > 0:
            for j, ln in enumerate(lines):
                underline(c, TX - 2, TX + hand_w(ln, size) + 4, y + j * lh + 10, cols[k], marks * show[k], 1.0, 4)
        if icons > 0:
            icone_peca(c, keys[k], MX + 44, y + 4, icons * show[k], 0.38)
        if k == 1 and hl_ponte > 0:
            w_ = hand_w("Na prática, contudo,", size)
            rrect(c, TX - 6, y - size * 0.95, w_ + 12, size * 1.3, 6, GREEN, 0.22 * hl_ponte)
        hand_para(c, s, TX, y, size, PEN, show[k], TW, lh, reveal[k])
        y += len(lines) * lh + 14
    return y


def b_p4(c, t, C, B):
    sid = which(t, C, ["17", "18"])
    head(c, t, B["start"], "EU FAÇO · PASSO 4", "A PONTE (RUA DE ACESSO)", GREEN)
    checklist(c, 3, 1.0)
    rascunho(c)
    tema_topo(c)
    eixos_strip(c)
    y0 = MY + 210
    tentativa_riscada(c, y0, 1.0, 1.0, 24)
    yy = y0 + 50
    r2 = wreveal(t, span("17", S2, C, 9.0, "17.c")) if sid == "17" else 1.0
    show2 = ep(t, C["17.c"], 0.3)
    yend = paragrafo(c, t, C, yy, (1.0, r2, 0.0), 28, 46, 0.0, 1.0, ep(t, C["17.b"], 0.4), (1, show2, 0))
    if sid == "17":
        aa = ep(t, C["17.a"], 0.4) * (1 - ep(t, C["17.c"], 0.3))
        pill(c, "a lei promete... e a realidade?", MX + MW / 2, MY + MH - 90, AMBER, size=28, a=aa, anchor="center", bounds=(0, 1920))
        ab = ep(t, C["17.b"], 0.4) * (1 - ep(t, C["17.c"], 0.3))
        pill(c, "“na prática, contudo” = a virada", MX + MW / 2, MY + MH - 160, GREEN, size=28, a=ab, anchor="center", bounds=(0, 1920))
        return
    defs = [("18.a", "DEMARCAÇÃO", "reconhecimento oficial dos limites de uma terra indígena"),
            ("18.b", "TITULAÇÃO", "entrega do título de propriedade a uma comunidade quilombola")]
    for k, (cue, nm, d) in enumerate(defs):
        a = ep(t, C[cue], 0.4) * (1 - ep(t, C["18.c"], 0.3))
        y = yend + 40 + k * 64
        pill(c, nm, TX, y, BLUE, size=22, a=a, bounds=(0, 1920))
        text(c, d, TX + 200, y + 8, 26, "bold", INK2, a, align="left")
    ac = ep(t, C["18.c"], 0.4)
    text(c, "a ponte já toca nos DOIS eixos:", TX, yend + 60, 26, "black", INK, ac, align="left")
    pill(c, "terra → A", TX + 430, yend + 52, MOV["lista"], size=22, a=ep(t, C["18.d"], 0.3), bounds=(0, 1920))
    pill(c, "estereótipo → B", TX + 600, yend + 52, MOV["lista"], size=22, a=ep(t, C["18.e"], 0.3), bounds=(0, 1920))


def b_p5(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · PASSO 5", "A TESE FINAL + A LISTA DA CAIXA", GREEN)
    checklist(c, 4, 1.0)
    rascunho(c)
    tema_topo(c)
    eixos_strip(c)
    y0 = MY + 200
    tentativa_riscada(c, y0, 1.0, 1.0, 22)
    show3 = ep(t, C["19.a"], 0.3)
    r3 = wreveal(t, span("19", S3, C, 12.0, "19.a"))
    paragrafo(c, t, C, y0 + 46, (1, 1, r3), 27, 43, 0.0, 1.0, 0.0, (1, 1, show3))
    ab, ac = ep(t, C["19.b"], 0.3), ep(t, C["19.c"], 0.3)
    text(c, "LISTA DA CAIXA:", TX, MY + MH - 42, 18, "black", MOV["lista"], ab, align="left", tracking=2)
    pill(c, "A · insegurança territorial", TX + 200, MY + MH - 50, MOV["lista"], size=22, a=ab, bounds=(0, 1920))
    pill(c, "B · desconhecimento", TX + 520, MY + MH - 50, MOV["lista"], size=22, a=ac, bounds=(0, 1920))


def b_pronta(c, t, C, B):
    head(c, t, B["start"], "SEÇÃO 10 DO MATERIAL", "A INTRODUÇÃO INTEIRA", GREEN)
    checklist(c, 4, 1.0, feitos=5)
    rascunho(c)
    tema_topo(c)
    y = MY + 140
    mk = ep(t, C["20.a"], 0.4)
    cols = [("20.a", "MAPA · referência verificável", MOV["mapa"]), ("20.b", "RUA · contraste com a realidade", MOV["rua"]),
            ("20.c", "ENDEREÇO + LISTA · tese com 2 eixos", MOV["tese"])]
    yend = paragrafo(c, t, C, y, (1, 1, 1), 27, 43, 0.0, 1.0)
    # sublinhado por frase, no ritmo da fala
    yy = y
    for k, s in enumerate((S1, S2, S3)):
        lines = hwrap(s, 27, TW)
        a = ep(t, C[cols[k][0]], 0.4)
        for j, ln in enumerate(lines):
            underline(c, TX - 2, TX + hand_w(ln, 27) + 4, yy + j * 43 + 10, cols[k][2], a, prog(t, C[cols[k][0]], 0.6), 4)
        yy += len(lines) * 43 + 14
    for k, (cue, s, col) in enumerate(cols):
        pill(c, s, TX + k * 420, MY + MH - 60, col, size=20, a=ep(t, C[cue], 0.4), bounds=(0, 1920))
    text(c, DIDATICO, MX + MW - 30, MY + MH + 26, 16, "medium", GRAY, 1.0, align="right")


def b_p6(c, t, C, B):
    sid = which(t, C, ["21", "22"])
    head(c, t, B["start"], "EU FAÇO · PASSO 6", "A CONFERÊNCIA", PURPLE)
    checklist(c, 5, 1.0, feitos=6 if t >= C["22.e"] else 5)
    rascunho(c)
    text(c, "FRASE TEMÁTICA", MX + MW / 2, MY + 52, 18, "black", BLUE, 1.0, tracking=2)
    c.save(); c.translate(DX, 0)
    puzzle(c, t, C, T22, MY + 80, 1.0, 24, None, obriga=False)
    marks = [ep(t, C["21.a"], 0.3), ep(t, C["21.b"], 0.3), ep(t, C["21.c"], 0.3), ep(t, C["21.d"], 0.3)]
    if sid == "21":
        for cx, a in zip(centros(T22, 24), marks):
            check_icon(c, cx, MY + 196, 22, a, GREEN)
    c.restore()
    if sid == "21":
        paragrafo(c, t, C, MY + 260, (1, 1, 1), 26, 41, 1.0, 1.0)
        return
    c.save(); c.translate(DX, 0)
    for cx in centros(T22, 24):
        check_icon(c, cx, MY + 196, 22, 1.0, GREEN)
    c.restore()
    # destinos dos eixos
    aa = ep(t, C["22.a"], 0.4)
    paragrafo(c, t, C, MY + 260, (1, 1, 1), 22, 34, 0.6, 0.0, 0.0, (1 - 0.6 * aa, 1 - 0.6 * aa, 1 - 0.6 * aa))
    if aa > 0:
        rrect(c, MX + 90, MY + 470, MW - 520, 200, 20, "#FFFFFF", aa, shadow=True)
        rows = [("22.b", "A · território", "1º parágrafo de desenvolvimento"), ("22.c", "B · desconhecimento", "2º parágrafo de desenvolvimento")]
        for k, (cue, e, d) in enumerate(rows):
            a = ep(t, C[cue], 0.4) * aa
            y = MY + 530 + k * 70
            pill(c, e, MX + 130, y, MOV["lista"], size=22, a=a, bounds=(0, 1920))
            arrow(c, MX + 430, y, MX + 560, y, MOV["lista"], a, 5, 16, progress=a)
            text(c, d, MX + 590, y + 9, 28, "black", INK, a, align="left")
        ad = ep(t, C["22.d"], 0.4)
        text(c, "+ a conclusão retoma os dois", MX + 130, MY + 655, 24, "bold", PURPLE, ad, align="left")
        selo(c, MX + MW - 220, MY + 570, ep(t, C["22.e"], 0.4), "INTRODUÇÃO PRONTA", GREEN, -6, 28)


# ======================================================================
# recap, questão 9, você faz, erros
# ======================================================================

FRASES = ["Arrume a caixa antes de escrever a etiqueta.", "Referência, ponte, tese com dois eixos.",
          "Conferir é passar a tese pela frase temática, bloco a bloco."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("23", "34"), FRASES, [MOV["lista"], MOV["rua"], PURPLE])


ALT9 = [("A", "A valorização dos povos tradicionais brasileiros esbarra na insegurança territorial e no desconhecimento da "
              "sociedade sobre seus modos de vida.", "24.A"),
        ("B", "No Brasil, comunidades quilombolas, indígenas e ribeirinhas ainda são pouco valorizadas porque o Estado demora "
              "a garantir seus territórios e a escola pouco as apresenta.", "25.B"),
        ("C", "A falta de demarcação de terras e o preconceito dificultam a valorização dos povos tradicionais no país.", "25.C"),
        ("D", "Os povos indígenas da América do Sul desenvolveram, ao longo dos séculos, técnicas agrícolas variadas.", "26.D"),
        ("E", "Valorizar os povos tradicionais do Brasil exige enfrentar o estereótipo que os associa apenas ao passado e a "
              "pressão econômica sobre suas terras.", "26.E")]
OKPILL = {"A": ("28.xa", "obstáculos à valorização no Brasil"), "B": ("28.xb", "grupos, lugar e dois desafios"),
          "C": ("28.xc", "“no país”"), "E": ("28.xe", "“do Brasil”")}


def b_q9(c, t, C, B):
    head(c, t, B["start"], "NÓS FAZEMOS · QUESTÃO 9", "QUAL TESE TANGENCIA?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["24.a"], 0.4)
    para(c, "Para o tema do Enem 2022, “" + TEMA22 + "”, uma das teses abaixo tende a levar o texto ao tangenciamento. Qual?",
         200, 215, 25, "black", INK, aa, 1500, 31)
    conf = ep(t, C["27.d1"], 0.5)
    w = 1500 - 470 * conf
    x, y, size = 230, 320, 23
    aok = ep(t, C["27.ok"], 0.5)
    for L, s, cue in ALT9:
        a, d = rise(t, C[cue])
        lines = wrap(s, "bold", size, w - 60)
        pk = OKPILL.get(L)
        hh = len(lines) * (size + 6) + 12 + (24 if pk else 0)
        ok = L == "D"
        hp = ep(t, C[pk[0]], 0.4) if pk else 0
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 20, y - size - 6 + d, w + 30, hh + 8, 12, AMBER, 0.18 * aok)
            badge_num(c, L, x + 6, y - size * 0.35 + d, a, 18, bg=AMBER if ok and aok > 0.5 else INK)
            for j, ln in enumerate(lines):
                text(c, ln, x + 40, y + d + j * (size + 6), size, "bold", INK, a, align="left")
            if hp > 0:
                pill(c, "✓ " + pk[1], x + 40, y + d + len(lines) * (size + 6) + 4, GREEN, size=15, a=hp, bounds=(0, 1920))
        y += hh + 10
    pause_timer(c, t, C["26.p"] + 0.3, 1700, 770)
    if conf > 0:
        x0 = 1290
        rrect(c, x0, 300, 360, 460, 18, mix("#FFFFFF", AMBER, 0.08), conf)
        text(c, "CONFERÊNCIA DA D", x0 + 180, 345, 20, "black", AMBER, conf, tracking=2)
        rows = [("27.d1", "desafios?"), ("27.d2", "valorização?"), ("27.d3", "Brasil? (América do Sul)")]
        for k, (cue, s) in enumerate(rows):
            a = ep(t, C[cue], 0.3) * conf
            yy = 410 + k * 70
            check_icon(c, x0 + 40, yy, 20, a, RED, "x")
            text(c, s, x0 + 72, yy + 8, 24, "black", INK, a, align="left")
        a4 = ep(t, C["27.d4"], 0.4)
        para(c, "só o assunto amplo (povos indígenas)", x0 + 30, 650, 22, "bold", INK2, a4, 300, 26)
        selo(c, x0 + 180, 720, a4, "TANGENCIAMENTO", AMBER, -4, 26)
    questao_rotulo(c, aa)


PORTAS = [("lei", "mapa"), ("história", "mapa"), ("dado", "mapa"), ("conceito", "mapa")]


def b_vocefaz(c, t, C, B):
    sid = which(t, C, ["29", "30"])
    head(c, t, B["start"], "VOCÊ FAZ · ENEM 2024", "SUA INTRODUÇÃO" if sid == "29" else "UMA RESPOSTA POSSÍVEL", GREEN)
    checklist(c, None, 1.0)
    if sid == "29":
        card(c, MX, MY, MW, MH)
        aa = ep(t, C["29.a"], 0.4)
        text(c, "ENEM 2024", MX + MW / 2, MY + 90, 22, "black", GRAY, aa, tracking=2)
        para(c, "“" + TEMA24 + "”", MX + 110, MY + 160, 42, "black", BLUE, aa, MW - 220, 52, align="left")
        ab = ep(t, C["29.b"], 0.4)
        text(c, "siga os 6 passos do checklist  ←", MX + 110, MY + 320, 32, "black", GREEN, ab, align="left")
        ad = ep(t, C["29.d"], 0.4)
        text(c, "abra por uma das 4 portas (episódio 2):", MX + 110, MY + 420, 28, "bold", INK2, ad, align="left")
        for k, (s, _) in enumerate(PORTAS):
            a = ep(t, C["29.d"] + 0.3 * k, 0.3)
            rrect(c, MX + 110 + k * 260, MY + 460, 230, 90, 16, mix("#FFFFFF", MOV["mapa"], 0.12), a)
            text_mid(c, s, MX + 110 + k * 260 + 115, MY + 505, 30, "black", MOV["mapa"], a)
        pause_timer(c, t, C["29.p"] + 0.3, MX + MW / 2, MY + 630)
        return
    rascunho(c)
    aa = ep(t, C["30.a"], 0.4)
    pill(c, "UMA resposta possível · Versão 3 (episódio 5)", TX, MY + 50, GREEN, size=20, a=aa, bounds=(0, 1920))
    cols = [("30.b", MOV["mapa"], "mapa"), ("30.c", MOV["rua"], "rua"), ("30.d", MOV["tese"], "tese")]
    y = MY + 140
    for k, s in enumerate(V3_BOA):
        lines = hwrap(s, 25, TW)
        a = ep(t, C[cols[k][0]], 0.4)
        for j, ln in enumerate(lines):
            underline(c, TX - 2, TX + hand_w(ln, 25) + 4, y + j * 40 + 10, cols[k][1], a, prog(t, C[cols[k][0]], 0.6), 4)
        icone_peca(c, cols[k][2], MX + 44, y + 4, aa, 0.38)
        hand_para(c, s, TX, y, 25, PEN, aa, TW, 40)
        y += len(lines) * 40 + 14
    ad = ep(t, C["30.d"], 0.4)
    pill(c, "A · escola", TX + 700, MY + MH - 70, MOV["lista"], size=22, a=ad, bounds=(0, 1920))
    pill(c, "B · mídia", TX + 870, MY + MH - 70, MOV["lista"], size=22, a=ad, bounds=(0, 1920))
    selo(c, TX + 260, MY + MH - 60, ep(t, C["30.e"], 0.4), "UMA, NÃO A ÚNICA", GREEN, -4, 26)
    text(c, DIDATICO, MX + MW - 30, MY + MH + 26, 16, "medium", GRAY, aa, align="right")


ERROS = [("31", "Escrever a antecipação ANTES de planejar os parágrafos", "a introdução vem primeiro na folha",
          "a lista da caixa se escreve DEPOIS de arrumar a caixa"),
         ("32", "Pular a conferência porque a introdução “ficou bonita”", "o parágrafo soa bem",
          "bonito não é completo: passe bloco a bloco"),
         ("33", "Deixar a introdução crescer com exemplos do desenvolvimento", "mostra que você sabe muito",
          "exemplos ficam no desenvolvimento: na introdução, só anuncie os eixos")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "ÚLTIMO EPISÓDIO DO ASSUNTO", "REVISÃO E DESAFIO", PURPLE)
    rows = [("35.b", "juntamos tudo", GREEN), ("35.c", "caçamos as PEGADINHAS", AMBER), ("35.d", "DESAFIO: 3 temas reais", PURPLE)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 420, y - 16, a, 34, bg=col)
        text(c, s, 490, y, 56, "black", INK, a, align="left")


def b_cta(c, t, C, B):
    cta_intro(c, t, C, "36", "Por qual porta você abriu a sua introdução?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, material=b_material, prereq=b_prereq, caixa=b_caixa, passos=b_passos,
              tema=b_tema, p1=b_p1, p2=b_p2, p3=b_p3, p4=b_p4, p5=b_p5, pronta=b_pronta, p6=b_p6, recap=b_recap,
              q9=b_q9, vocefaz=b_vocefaz, erros=b_erros, ponte=b_ponte, cta=b_cta)
