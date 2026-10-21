"""Visual — Cartografia, Episódio 6: Revisão geral, pegadinhas e treino (tema claro).
Índice visual: 5 ícones dos episódios (lupa, globo com grade, laranja, escada, balão).
Pausas com cronômetro circular; selo "PEGADINHA" em âmbar nos erros.
Cores: azul = definição · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import math
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa
import mapas

MARCA = ""
ARQUIVO_FINAL = "enem_geografia_cartografia_ep6_revisao.mp4"
CARD_R = (140, 150, 1640, 690)
EP_COL = [BLUE, GREEN, "#EA580C", "#A16207", PURPLE]
EP_NOME = ["Escala", "Coordenadas", "Projeções", "Curvas de nível", "Mapas temáticos"]
EP_ANCORA = ["ZOOM", "BATALHA NAVAL", "CASCA DE LARANJA", "DEGRAUS DE ESCADA", "MAPA DE BALÕES"]


# ======================================================================
# ícones dos episódios
# ======================================================================

def icon_ep(c, k, cx, cy, s, a):
    if a <= 0:
        return
    col = EP_COL[k]
    c.drawCircle(cx, cy, s, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, s, paint(col, a, stroke=max(3, s * 0.06)))
    r = s * 0.62
    if k == 0:      # lupa
        c.drawCircle(cx - r * 0.15, cy - r * 0.15, r * 0.55, paint(col, a, stroke=s * 0.1))
        line(c, cx + r * 0.25, cy + r * 0.25, cx + r * 0.7, cy + r * 0.7, col, a, s * 0.14)
    elif k == 1:    # globo com grade
        mapas.draw_globe(c, cx, cy, r, a, lon0=-40, lat0=10, grat_lats=(-30, 0, 30), grat_lons=(-80, -40, 0))
    elif k == 2:    # laranja
        c.drawCircle(cx, cy + r * 0.08, r * 0.75, paint("#FB923C", a))
        for j in range(3):
            w = r * 0.75 * (0.3 + 0.35 * j)
            c.drawOval(skia.Rect.MakeLTRB(cx - w, cy - r * 0.67, cx + w, cy + r * 0.83), paint("#EA580C", a * 0.5, stroke=2))
        c.drawOval(skia.Rect.MakeLTRB(cx, cy - r * 0.95, cx + r * 0.45, cy - r * 0.65), paint(GREEN, a))
    elif k == 3:    # escada
        p = skia.Path(); x0, y0, st = cx - r * 0.8, cy + r * 0.7, r * 0.4
        p.moveTo(x0, y0)
        for j in range(4):
            p.lineTo(x0 + j * st, y0 - (j + 1) * st); p.lineTo(x0 + (j + 1) * st, y0 - (j + 1) * st)
        p.lineTo(x0 + 4 * st, y0); p.close()
        c.drawPath(p, paint(col, a * 0.35)); c.drawPath(p, paint(col, a, stroke=s * 0.06))
    else:           # balão
        c.drawOval(skia.Rect.MakeLTRB(cx - r * 0.55, cy - r * 0.85, cx + r * 0.55, cy + r * 0.35), paint("#F59E0B", a))
        line(c, cx, cy + r * 0.35, cx, cy + r * 0.9, INK2, a, 3)


def ep_strip(c, t, active, a=1.0, y=118):
    """faixa de índice no topo, com o episódio ativo destacado"""
    for k in range(5):
        x = W / 2 + (k - 2) * 90
        on = k == active
        icon_ep(c, k, x, y, 34 if on else 26, a * (1.0 if on else 0.45))


def pause_timer(c, t, t0, x, y, a=1.0, dur=2.0, r=46):
    u = clamp((t - t0) / dur)
    ap = a * ep(t, t0, 0.3) * (1 - prog(t, t0 + dur + 0.3, 0.4))
    if ap <= 0:
        return
    c.drawCircle(x, y, r + 14, paint(AMBER, ap * 0.18))
    c.drawCircle(x, y, r, paint("#FFFFFF", ap))
    c.drawArc(skia.Rect.MakeLTRB(x - r, y - r, x + r, y + r), -90, 360 * (1 - u), False, paint(AMBER, ap, stroke=10, cap_round=True))
    c.drawRect(skia.Rect.MakeXYWH(x - 15, y - 20, 10, 40), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(x + 5, y - 20, 10, 40), paint(INK, ap))
    text(c, "PAUSE", x, y + r + 40, 26, "black", AMBER, ap)


def selo(c, x, y, a, s="PEGADINHA", col=None, rot=-8):
    if a <= 0:
        return
    col = col or AMBER
    c.save(); c.translate(x, y); c.rotate(rot)
    w = text_w(s, "black", 34) + 50
    sc = 0.8 + 0.2 * ease_back(clamp(a))
    c.scale(sc, sc)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -32, w, 64), 12, 12), paint(col, a * 0.15))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -32, w, 64), 12, 12), paint(col, a, stroke=5))
    text_mid(c, s, 0, 0, 34, "black", col, a)
    c.restore()


def badge_row(c, t, rows, x, y0, dy, size=44):
    for k, (tc, s, col) in enumerate(rows):
        a, d = rise(t, tc)
        yy = y0 + k * dy + d
        badge_num(c, k + 1, x, yy - size * 0.36, a, 30, bg=col)
        text(c, s, x + 56, yy, size, "black", INK, a, align="left")


def which(t, C, ids):
    """qual das cenas (ids) está ativa agora"""
    cur = ids[0]
    for i in ids:
        if t >= C[i] - 0.05:
            cur = i
    return cur


def alts(c, t, C, sid_q, sid_r, items, x, y0, dy, size=30, xmax=1730):
    """items = [(letra, texto, cue_x ou None)] · cues de entrada em sid_q, eliminação em sid_r"""
    aok = ep(t, C[sid_r + ".t"] + 1.0, 0.5)
    for k, (L, s, cx) in enumerate(items):
        a, d = rise(t, C[f"{sid_q}.{L.lower()}"])
        yy = y0 + k * dy + d
        ok = cx is None
        if ok and aok > 0:
            rrect(c, x - 40, yy - 34, xmax - x + 40, dy - 10, 14, GREEN, 0.15 * aok)
        badge_num(c, L, x, yy - 10, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cx], 0.4) if cx else 0
        text(c, s, x + 40, yy, size, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, x + 36, yy - 10, x + 46 + text_w(s, "black", size), yy - 10, ax, RED, ax)


def q_frame(c, t, C, B, k, titulo, linhas):
    head(c, t, B["start"], f"QUESTÃO INÉDITA {k + 1}", titulo, EP_COL[k])
    card(c, *CARD_R)
    icon_ep(c, k, 1700, 210, 36, 1)
    for j, (cue, s, col) in enumerate(linhas):
        text(c, s, 200, 230 + j * 50, 32, "black", col, ep(t, C[cue], 0.5), align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    card(c, *CARD_R)
    aa, ab = ep(t, C["01.a"], 0.5), ep(t, C["01.b"], 0.5)
    for k, (a, tt, sub, col) in enumerate(((aa, "COMO CONTA", "escala · distância · declividade", BLUE),
                                           (ab, "LEITURA CRÍTICA", "o que o mapa mostra (e esconde)", PURPLE))):
        x = 560 + k * 800
        rrect(c, x - 330, 300, 660, 300, 24, col, 0.1 * a)
        if a > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 330, 300, 660, 300), 24, 24), paint(col, a, stroke=4))
        text(c, tt, x, 430, 52, "black", col, a)
        text(c, sub, x, 500, 28, "bold", INK2, a)
    pill(c, "você está pronto para os dois?", W / 2, 720, AMBER, size=32, a=ep(t, C["01.c"], 0.5), anchor="center")


def b_doisjeitos(c, t, C, B):
    head(c, t, B["start"], "DOIS JEITOS DE CAIR", "OS MESMOS CONCEITOS", BLUE)
    card(c, *CARD_R)
    aa, ab = ep(t, C["01b.a"], 0.5), ep(t, C["01b.b"], 0.5)
    for j, s in enumerate(("escala", "distância", "declividade")):
        pill(c, s, 450, 330 + j * 90, BLUE, size=32, a=aa * ep(t, C["01b.a"] + 0.3 * j, 0.3), anchor="center")
    for j, s in enumerate(("Groenlândia enorme?", "norte em cima?", "o que o mapa quer mostrar?")):
        pill(c, s, 1300, 330 + j * 90, PURPLE, size=28, a=ab * ep(t, C["01b.b"] + 0.6 * j, 0.3), anchor="center")
    pill(c, "os MESMOS poucos conceitos", W / 2, 720, GREEN, size=32, a=ep(t, C["01b.c"], 0.5), anchor="center")


def b_indice(c, t, C, B):
    head(c, t, B["start"], "A REVISÃO EM 5 IMAGENS", "", PURPLE)
    card(c, *CARD_R)
    for k, cue in enumerate(("02.a", "02.b", "02.c", "02.d", "02.e")):
        a, d = rise(t, C[cue])
        x = 300 + k * 330
        icon_ep(c, k, x, 400 + d, 100, a)
        text(c, EP_NOME[k], x, 560 + d, 28, "black", INK2, a)
        text(c, EP_ANCORA[k], x, 620 + d, 24, "black", EP_COL[k], a)
        badge_num(c, k + 1, x - 80, 320 + d, a, 22, bg=EP_COL[k])


def b_ideias(c, t, C, B):
    head(c, t, B["start"], "AS 3 IDEIAS", "QUE MAIS RENDEM PONTOS", GREEN)
    card(c, *CARD_R)
    rows = [("03.a", 0, "Escala GRANDE = número de baixo PEQUENO", "mais detalhe · zoom aproximado"),
            ("03.b", 2, "Nenhuma projeção é NEUTRA", "conforme: forma · equivalente: área · nunca as 2"),
            ("03.c", 3, "Curvas PRÓXIMAS = terreno ÍNGREME", "degraus colados")]
    for j, (cue, k, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 290 + j * 170 + d
        icon_ep(c, k, 290, y, 56, a)
        text(c, s, 380, y - 4, 42, "black", INK, a, align="left")
        text(c, sub, 380, y + 46, 28, "bold", INK2, a, align="left")


# ======================================================================
# verdadeiro ou falso
# ======================================================================

VF = [("05", 0, "1 : 5 000 000 é escala GRANDE", "5 milhões é um número enorme", "número de baixo grande = escala PEQUENA"),
      ("06", 0, "Mapa ampliado: a escala numérica vale", "o número está impresso ali", "só a BARRINHA cresce junto"),
      ("07", 0, "8 cm em 1 : 250 000 = 2 km", "a conta parece fácil", "2 000 000 cm → corte 5 zeros = 20 km"),
      ("08", 1, "Latitude a partir de Greenwich", "Greenwich é o zero famoso", "latitude: a partir do EQUADOR"),
      ("09", 1, "5° N a 15° S = 10°", "a gente sempre subtrai", "lados opostos do Equador: SOMA = 20°"),
      ("10", 2, "Mercator mostra as áreas reais", "é o mapa da escola", "protege a FORMA e infla os polos"),
      ("11", 2, "Peters preserva as formas", "é a \"mais justa\"", "protege a ÁREA e estica as formas"),
      ("12", 3, "Curvas juntinhas = terreno plano", "linhas juntas parecem tranquilas", "degraus COLADOS = íngreme"),
      ("13", 4, "Anamorfose = projeção equivalente", "as duas falam de área", "equivalente MANTÉM a área; balões = DADO")]


def b_vf_intro(c, t, C, B):
    head(c, t, B["start"], "VERDADEIRO OU FALSO?", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    for k, (s, col) in enumerate((("V", GREEN), ("F", RED))):
        x = 760 + k * 400
        rrect(c, x - 130, 300, 260, 260, 40, col, 0.12 * aa)
        if aa > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 130, 300, 260, 260), 40, 40), paint(col, aa, stroke=6))
        text_mid(c, s, x, 430, 160, "black", col, aa)
    text(c, "9 frases · você pausa e responde", W / 2, 650, 36, "black", INK, aa)
    selo(c, W / 2, 750, ep(t, C["04.b"], 0.4), "TODAS SÃO PEGADINHAS")


def b_vf(c, t, C, B):
    sid = which(t, C, [v[0] for v in VF])
    n = [v[0] for v in VF].index(sid)
    _, k, frase, engana, regra = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO · {n + 1} de 9", EP_NOME[k].upper(), AMBER)
    card(c, *CARD_R)
    icon_ep(c, k, 300, 300, 70, 1)
    text(c, "episódio " + str(k + 1), 300, 410, 24, "bold", GRAY, 1)
    a0 = ep(t, C[sid] + 0.1, 0.4)
    text(c, f"\"{frase}\"", 1000, 320, 50 if len(frase) < 34 else 44, "black", INK, a0)
    pause_timer(c, t, C[sid + ".p"], 1000, 480)
    ar = ep(t, C[sid + ".r"], 0.4)
    if ar > 0:
        rrect(c, 760, 420, 480, 120, 30, RED, 0.12 * ar)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(760, 420, 480, 120), 30, 30), paint(RED, ar, stroke=5))
        text_mid(c, "FALSO", 1000, 480, 72, "black", RED, ar)
    ae = ep(t, C[sid + ".e"], 0.4)
    selo(c, 420, 620, ae)
    text(c, "engana porque " + engana, 600, 632, 30, "black", AMBER, ae, align="left")
    ac = ep(t, C[sid + ".c"], 0.4)
    check_icon(c, 420, 740, 26, ac, GREEN)
    text(c, regra, 470, 752, 34, "black", GREEN, ac, align="left")


def b_vf_fim(c, t, C, B):
    head(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "", GREEN)
    card(c, *CARD_R)
    text(c, "? / 9", W / 2, 420, 140, "black", INK, ep(t, C["13b.t"], 0.5))
    pill(c, "errou mais de 3? anote quais", W / 2, 560, AMBER, size=30, a=ep(t, C["13b.a"], 0.5), anchor="center")
    pill(c, "e reveja o episódio de cada uma", W / 2, 640, BLUE, size=30, a=ep(t, C["13b.b"], 0.5), anchor="center")
    pill(c, "errar aqui é melhor que errar na prova", W / 2, 740, GREEN, size=30, a=ep(t, C["13b.c"], 0.5), anchor="center")


# ======================================================================
# lembranças antes das questões
# ======================================================================

LEMBRA = {"13c": (0, ["o número de baixo = quantas vezes encolheu", "cm → km: corte CINCO zeros"]),
          "15b": (1, ["latitude = linha, a partir do EQUADOR", "longitude = coluna, a partir de GREENWICH",
                      "no oeste: número MAIOR = mais a OESTE"]),
          "17b": (2, ["rasga ou estica", "CONFORME protege a forma", "EQUIVALENTE protege a área"]),
          "19b": (3, ["desnível = quanto SOBE", "distância = quanto ANDA na horizontal", "÷ e × 100 · metro com metro"]),
          "21b": (4, ["cada país incha ou murcha conforme um DADO", "mas continua no MESMO lugar"])}


def b_lembra(c, t, C, B):
    sid = which(t, C, list(LEMBRA))
    k, linhas = LEMBRA[sid]
    head(c, t, C[sid], "LEMBRA?", EP_ANCORA[k], EP_COL[k])
    card(c, *CARD_R)
    if sid == "13c":
        pill(c, "5 questões inéditas · uma de cada episódio", W / 2, 210, PURPLE, size=28, a=ep(t, C["13c.t"], 0.5), anchor="center")
    icon_ep(c, k, 470, 490, 170, ep(t, C[sid] + 0.1, 0.5))
    cues = [c_ for c_ in ("a", "b", "c") if f"{sid}.{c_}" in C]
    for j, s in enumerate(linhas):
        cue = f"{sid}.{cues[min(j, len(cues) - 1)]}"
        a, d = rise(t, C[cue])
        text(c, s, 760, 380 + j * 110 + d, 38, "black", EP_COL[k] if j == len(linhas) - 1 else INK, a, align="left")


# ======================================================================
# questões inéditas
# ======================================================================

def b_q1(c, t, C, B):
    q_frame(c, t, C, B, 0, "DISTÂNCIA REAL", [("14.e1", "Mapa 1 : 200 000 · duas cidades a 6 cm.", INK),
                                              ("14.e2", "A distância real é de...", BLUE)])
    items = [("A", "1,2 km", "15.a"), ("B", "12 km", None), ("C", "120 km", "15.a"), ("D", "33 km", "15.d"), ("E", "1 200 km", "15.a")]
    alts(c, t, C, "14", "15", items, 260, 400, 80, 34, xmax=800)
    pause_timer(c, t, C["14.p"], 1500, 330)
    at = ep(t, C["15.t"], 0.5)
    text(c, "6 × 200 000 = 1 200 000 cm", 1260, 480, 40, "black", INK, at)
    text(c, "corte 5 zeros", 1260, 560, 34, "black", GREEN, at)
    result_box(c, "12 km", 1260, 670, 56, ep(t, C["15.t"] + 1.6, 0.5), GREEN)
    pill(c, "A, C, E: erraram os zeros · D: dividiu", 1260, 790, RED, size=24, a=ep(t, C["15.d"], 0.5), anchor="center", bounds=(0, 1920))


def b_q2(c, t, C, B):
    q_frame(c, t, C, B, 1, "PARA QUE LADO?", [("16.e1", "Sai de 20° S, 40° O", INK), ("16.e2", "Chega a 10° S, 55° O", INK),
                                              ("16.e3", "Para que lado ele foi?", BLUE)])
    items = [("A", "nordeste", "17.a"), ("B", "noroeste", None), ("C", "sudoeste", "17.c"), ("D", "sudeste", "17.d"), ("E", "norte", "17.e")]
    alts(c, t, C, "16", "17", items, 260, 440, 76, 32, xmax=640)
    pause_timer(c, t, C["16.p"], 1500, 300)
    ag = ep(t, C["17.t"], 0.5)
    gx, gy, gw, gh = 860, 420, 620, 340
    X = lambda lon: gx + (60 - lon) / 30 * gw
    Y = lambda lat: gy + lat / 30 * gh
    for lon in (60, 50, 40, 30):
        line(c, X(lon), gy, X(lon), gy + gh, LINE, ag, 2)
        text(c, f"{lon}° O", X(lon), gy + gh + 36, 22, "bold", GRAY, ag)
    for lat in (0, 10, 20, 30):
        line(c, gx, Y(lat), gx + gw, Y(lat), LINE, ag, 2)
        text(c, f"{lat}° S" if lat else "0°", gx - 12, Y(lat) + 8, 22, "bold", GRAY, ag, align="right")
    A, Bp = (X(40), Y(20)), (X(55), Y(10))
    if ag > 0:
        c.drawCircle(*A, 13, paint(INK, ag)); c.drawCircle(*Bp, 13, paint(RED, ag))
    a1, a2, ar = ep(t, C["17.s1"], 0.5), ep(t, C["17.s2"], 0.5), ep(t, C["17.r"], 0.5)
    arrow(c, A[0], A[1] - 14, A[0], Bp[1], BLUE, a1, 5, 18, progress=a1)
    pill(c, "NORTE", A[0] + 16, (A[1] + Bp[1]) / 2, BLUE, size=22, a=a1, bounds=(0, 1920))
    arrow(c, A[0], Bp[1], Bp[0] + 14, Bp[1], PURPLE, a2, 5, 18, progress=a2)
    pill(c, "OESTE", (A[0] + Bp[0]) / 2, Bp[1] - 36, PURPLE, size=22, a=a2, anchor="center", bounds=(0, 1920))
    arrow(c, A[0] - 8, A[1] - 8, Bp[0] + 12, Bp[1] + 12, RED, ar, 6, 22, progress=ar)


def b_q3(c, t, C, B):
    q_frame(c, t, C, B, 2, "COMPARAR ÁREAS", [("18.e1", "Atlas para comparar o tamanho das florestas", INK),
                                              ("18.e2", "de cada continente. Qual projeção?", BLUE)])
    items = [("A", "Mercator, conforme: preserva as formas", "19.a"),
             ("B", "Peters, equivalente: mantém a proporção das áreas", None),
             ("C", "cilíndrica qualquer: o Equador é onde o erro é maior", "19.c"),
             ("D", "anamorfose de população", "19.d"),
             ("E", "equivalente: preserva forma e área ao mesmo tempo", "19.e")]
    alts(c, t, C, "18", "19", items, 260, 380, 82, 30)
    pause_timer(c, t, C["18.p"], 1560, 330)
    whys = [("19.a", "infla os polos"), ("19.c", "onde toca, o erro é MENOR"), ("19.d", "troca a área por um dado"), ("19.e", "IMPOSSÍVEL")]
    for j, (cue, s) in enumerate(whys):
        yy = 380 + [0, 2, 3, 4][j] * 82
        text(c, s, 1720, yy, 22, "black", RED, ep(t, C[cue], 0.4), align="right")


def b_q4(c, t, C, B):
    q_frame(c, t, C, B, 3, "DECLIVIDADE", [("20.e1", "Carta 1 : 25 000", INK), ("20.e2", "Curvas de 300 m e 450 m", INK),
                                           ("20.e3", "2 cm entre os pontos · declividade?", BLUE)])
    items = [("A", "0,3%", "21.a"), ("B", "30%", None), ("C", "90%", "21.c"), ("D", "3%", "21.d"), ("E", "300%", "21.e")]
    alts(c, t, C, "20", "21", items, 260, 440, 76, 32, xmax=640)
    pause_timer(c, t, C["20.p"], 1500, 330)
    at = ep(t, C["21.t"], 0.5)
    rrect(c, 820, 420, 860, 360, 20, GREEN, 0.07 * at)
    for j, (cue, s) in enumerate((("21.t", "2 × 25 000 = 50 000 cm = 500 m"), ("21.s1", "450 − 300 = 150 m"), ("21.s2", "150 ÷ 500 × 100"))):
        text(c, s, 1250, 490 + j * 76, 38, "black", INK, ep(t, C[cue], 0.4))
    result_box(c, "= 30%", 1250, 720, 50, ep(t, C["21.s2"] + 1.4, 0.5), GREEN)
    pill(c, "30% = o limite da lei para lotear", 1250, 830, AMBER, size=24, a=ep(t, C["21.x"], 0.5), anchor="center")


def b_q5(c, t, C, B):
    q_frame(c, t, C, B, 4, "O MAPA DAS EMISSÕES", [("22.e1", "Tamanho de cada país PROPORCIONAL às emissões de CO₂.", INK),
                                                   ("22.e2", "EUA e China enormes; a África quase some.", INK)])
    items = [("A", "a África tem pouco território", "23.a"), ("B", "projeção equivalente: áreas reais", "23.b"),
             ("C", "os maiores no mapa são os que mais emitem", None), ("D", "a China é o maior país em território", "23.a"),
             ("E", "é um mapa de escala grande", "23.e")]
    alts(c, t, C, "22", "23", items, 260, 400, 82, 30)
    pause_timer(c, t, C["22.p"], 1560, 330)
    whys = [("23.a", 0, "tamanho lido como território"), ("23.b", 1, "anamorfose ≠ equivalente"), ("23.a", 3, "tamanho lido como território"),
            ("23.e", 4, "mapa-múndi = escala PEQUENA")]
    for cue, j, s in whys:
        text(c, s, 1720, 400 + j * 82, 22, "black", RED, ep(t, C[cue], 0.4), align="right")


# ======================================================================
# conexões, checklist, meta, ponte
# ======================================================================

def b_conexoes(c, t, C, B):
    head(c, t, B["start"], "CONEXÕES", "CARTOGRAFIA EM OUTRAS ÁREAS", PURPLE)
    data = [("24.a", 0, "Escala", "PROPORÇÃO", "Matemática"), ("24.b", 1, "Latitude e longitude", "ÂNGULOS", "Matemática"),
            ("24.c", 2, "Mercator", "GRANDES NAVEGAÇÕES", "História"), ("24.d", 1, "Longitude", "FUSOS HORÁRIOS", "Geografia"),
            ("24.e", 3, "Curvas de nível", "EROSÃO e relevo", "Geografia")]
    cw, gap = 316, 16
    x0 = W / 2 - (5 * cw + 4 * gap) / 2
    for j, (cue, k, a_, b_, area) in enumerate(data):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + j * (cw + gap)
        card(c, x, 200 + d, cw, 560, a)
        icon_ep(c, k, x + cw / 2, 300 + d, 56, a)
        text(c, a_, x + cw / 2, 420 + d, 28, "black", INK, a)
        arrow(c, x + cw / 2, 450 + d, x + cw / 2, 510 + d, GRAY, a, 4, 16)
        text(c, b_, x + cw / 2, 560 + d, 28 if len(b_) < 15 else 22, "black", EP_COL[k], a)
        pill(c, area, x + cw / 2, 680 + d, INK, size=22, a=a, anchor="center", bounds=(0, 1920))


CHECK = [("25.b", 0, ["distância pela escala", "o mapa ampliado", "escala grande ou pequena"]),
         ("25.c", 1, ["latitude e longitude", "as linhas da Terra", "distância no meridiano e direção"]),
         ("26.d", 2, ["tipos de projeção", "conforme x equivalente", "Mercator e Peters"]),
         ("26.e", 3, ["ler curvas de nível", "perfil topográfico", "declividade"]),
         ("26.f", 4, ["reconhecer uma anamorfose"])]


def b_checklist(c, t, C, B):
    head(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE SABE EXPLICAR", GREEN)
    card(c, *CARD_R)
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 200, BLUE, size=26, a=ep(t, C["25.a"], 0.5), anchor="center")
    y = 250
    for cue, k, itens in CHECK:
        a, d = rise(t, C[cue])
        icon_ep(c, k, 260, y + 50 + d, 34, a)
        pill(c, f"ep. {k + 1}", 260, y + 108 + d, EP_COL[k], size=20, a=a, anchor="center", bounds=(0, 1920))
        for j, s in enumerate(itens):
            xx = 340 + j * 450
            rrect(c, xx, y + 30 + d, 34, 34, 8, "#FFFFFF", a)
            if a > 0:
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, y + 30 + d, 34, 34), 8, 8), paint(EP_COL[k], a, stroke=3))
            text(c, s, xx + 48, y + 57 + d, 26, "black", INK, a, align="left")
        y += 112
    pill(c, "não marcou? REVEJA o episódio", W / 2, 830, AMBER, size=28, a=ep(t, C["26.g"], 0.5), anchor="center")


def b_meta(c, t, C, B):
    head(c, t, B["start"], "QUANDO VOCÊ DOMINOU?", "A META", GREEN)
    card(c, *CARD_R)
    aa, ab = ep(t, C["27.a"], 0.5), ep(t, C["27.b"], 0.5)
    for k in range(20):
        x = 360 + (k % 10) * 120
        y = 320 + (k // 10) * 130
        a = aa * ep(t, C["27.a"] + 0.05 * k, 0.3)
        ok = k < 14 and ab > 0
        rrect(c, x - 45, y - 45, 90, 90, 18, GREEN if ok else "#E5E7EB", a)
        if ok:
            check_icon(c, x, y, 26, ab * ep(t, C["27.b"] + 0.08 * k, 0.3), "#FFFFFF")
    text(c, "20 questões", 520, 580, 40, "black", INK, aa)
    text(c, "≥ 14 certas = 70%", 1300, 580, 40, "black", GREEN, ab)
    pill(c, "priorize ESCALA e PROJEÇÕES", 700, 700, BLUE, size=28, a=ep(t, C["27.c"], 0.5), anchor="center")
    pill(c, "+ pelo menos 3 de CURVAS DE NÍVEL", 1260, 700, AMBER, size=28, a=ep(t, C["27.d"], 0.5), anchor="center")


def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO ASSUNTO", "FUSOS HORÁRIOS", PURPLE)
    card(c, *CARD_R)
    at = ep(t, C["28.t"], 0.5)
    R = (220, 230, 1480, 420)
    mapas.draw_world(c, R, at)
    ab = ep(t, C["28.b"], 0.5)
    for k in range(25):
        lon = -180 + k * 15
        x0, y0 = mapas.to_xy(R, (lon, 84)); _, y1 = mapas.to_xy(R, (lon, -58))
        line(c, x0, y0, x0, y1, PURPLE if k % 2 else BLUE, ab * 0.8, 2)
    pill(c, "cada 15° de longitude = 1 HORA", W / 2, 720, PURPLE, size=32, a=ab, anchor="center")
    icon_ep(c, 1, 1640, 760, 44, ep(t, C["28.c"], 0.5))
    pill(c, "episódio 2 firme = vai ser rápido", W / 2, 800, GREEN, size=28, a=ep(t, C["28.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"], "Quantas das 9 pegadinhas você acertou?")


BLOCKS = dict(hook=b_hook, doisjeitos=b_doisjeitos, indice=b_indice, ideias=b_ideias, vf_intro=b_vf_intro, vf=b_vf,
              vf_fim=b_vf_fim, lembra=b_lembra, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, conexoes=b_conexoes,
              checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
