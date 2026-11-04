"""Visual — Estudativo · Questão de Matemática 007 (aula horizontal 1920x1080): dois muros (3 e 5), cordas cruzadas, altura do homem.
Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = dado do problema (muros 3 e 5), ciano = h (incógnita, o homem), menta = x / certo,
branco = y e d, vermelho = descartado. Frações empilhadas no quadro com row()."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_007_matematica_altura_do_homem_muros.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.c": "impact", "01.d": "deny", "01.e": "shimmer", "02.c": "confirm", "02.e": "confirm", "03.c": "confirm",
        "04.e": "impact", "05.d": "impact", "06.d": "shimmer", "06.e": "confirm", "07.d": "confirm", "08.e": "impact",
        "09.a": "deny", "10.c": "confirm", "11.a": "shimmer", "11.c": "confirm", "11.d": "lock", "13.a": "shimmer",
        "13.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.20, lufs=-14, bpm=100, sfx=_SFX)

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 007", "QUESTÃO DE MATEMÁTICA · 007"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_sem=("SIMILAR TRIANGLES", "SEMELHANÇA DE TRIÂNGULOS"),
    s_nomes=("THE NAMES", "OS NOMES"), s_par1=("STEP 1 · ROPE FROM THE 5 WALL", "PASSO 1 · A CORDA DO MURO DE 5"),
    s_par2=("STEP 2 · ROPE FROM THE 3 WALL", "PASSO 2 · A CORDA DO MURO DE 3"), s_somar=("STEP 3 · ADD THEM", "PASSO 3 · SOMAR"),
    s_frac=("STEP 4 · ADD FRACTIONS", "PASSO 4 · SOMA DE FRAÇÕES"), s_res=("STEP 5 · SOLVE", "PASSO 5 · RESOLVER"),
    s_dist=("WHAT ABOUT THE DISTANCE?", "E A DISTÂNCIA?"), s_conf=("CHECK", "CONFERÊNCIA"),
    s_gen=("THE GENERAL FORMULA", "A FÓRMULA GERAL"), s_resumo=("SUMMARY", "RESUMO"),
    pergunta=("How tall is the man?", "Qual a altura do homem?"),
    falta=("Missing the distance?", "Falta a distância?"), nao_falta=("NOT AT ALL!", "NÃO FALTA!"),
    p_sem=("SIMILAR TRIANGLES", "SEMELHANÇA"), p_frac=("FRACTIONS", "FRAÇÕES"),
    mesmos=("same angles", "mesmos ângulos"), foto=("an enlarged photo: same shape", "foto ampliada: mesma forma"),
    prop=("SIDES IN PROPORTION", "LADOS PROPORCIONAIS"), dois_ang=("2 equal angles → similar", "2 ângulos iguais → semelhantes"),
    soma180=("(the angles always add up to 180°)", "(a soma dos ângulos é sempre 180°)"),
    altura=("height of the man", "altura do homem"), total=("total distance", "distância total"),
    guarde=("keep this one!", "guarde essa!"),
    grande=("big △:  height 5,  base d", "△ grande:  altura 5,  base d"),
    pequeno=("small △:  height h,  base x", "△ pequeno:  altura h,  base x"),
    grande3=("big △:  height 3,  base d", "△ grande:  altura 3,  base d"),
    pequeno3=("small △:  height h,  base y", "△ pequeno:  altura h,  base y"),
    angs=("right angle + same angle", "ângulo reto + mesmo ângulo"), semel=("SIMILAR!", "SEMELHANTES!"),
    sumiu=("d is gone!", "o d sumiu!"), mmc=("lcm(5, 3) = 15", "mmc(5, 3) = 15"),
    inverso=("× 15/8 on both sides", "× 15/8 dos dois lados"),
    mesmo=("same thing", "é a mesma coisa"), x15=("× 15 on both sides", "× 15 dos dois lados"),
    d8=("÷ 8 on both sides", "÷ 8 dos dois lados"), sozinho=("goal: h alone", "objetivo: h sozinho"),
    cabeca=("upside down!", "de cabeça para baixo!"), atalho=("shortcut: × the inverse", "atalho: × o inverso"),
    metros=("in meters: 1.875 m", "em metros: 1,875 m"), alto=("a tall man!", "um homem bem alto!"),
    nao_imp=("IT DOESN'T MATTER", "NÃO IMPORTA"), cancelou=("d canceled out in the sum", "o d se cancelou na soma"),
    caso=("d = 8", "d = 8"), prod_soma=("product over sum", "produto sobre a soma"),
    iguais=("equal walls → half", "muros iguais → metade"), desafio=("AND WITH 10 AND 15?", "E COM 10 E 15?"),
    comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["Name h, x, y and d", "Similar triangles (×2)", "Add: d disappears", "Add fractions: h = 15/8"],
            ["Nomear h, x, y e d", "Semelhança (×2)", "Somar: o d some", "Soma de frações: h = 15/8"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Similar", "triangles"), ("Ratio and", "proportion"), ("", "Fractions")],
           [("Semelhança de", "triângulos"), ("Razão e", "proporção"), ("", "Frações")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
DEC = "." if EN else ","
H_TXT = "1.875" if EN else "1,875"
matematica.NUMEROS_EXTRA[:] = [] if EN else [
    ("cento e vinte sobre cento e vinte", "120/120"), ("quinze sobre oito", "15/8"), ("oito agá", "8h"),
    ("um vírgula oitocentos e setenta e cinco", "1,875"), ("cento e oitenta graus", "180°"),
    ("quinze oitavos", "15/8"), ("oito quinze avos", "8/15"), ("três quinze avos", "3/15"), ("cinco quinze avos", "5/15"),
    ("cinco oitavos", "5/8"), ("um quinto", "1/5"), ("um terço", "1/3"), ("agá", "h"), ("sobre", "/")]


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- linha de contas com frações empilhadas
P = lambda s, col=WHITE: (s, col)            # noqa: E731
F = lambda n, d, col=WHITE: ("/", n, d, col)  # noqa: E731


def _w(it, size):
    if it[0] == "/":
        return max(text_w(it[1], "black", size * 0.8), text_w(it[2], "black", size * 0.8)) + size * 0.3
    return text_w(it[0], "black", size)


def row(c, items, cy, a, size=64, cx=RX, box=None, maxw=840):
    """como eq(), mas aceita frações F(num, den, cor); devolve [(x0, x1)] de cada item"""
    if a <= 0:
        return []
    f = ease_out(clamp(a))
    tot = sum(_w(it, size) for it in items)
    while tot > maxw:
        size -= 2
        tot = sum(_w(it, size) for it in items)
    tem_frac = any(it[0] == "/" for it in items)
    x = cx - tot / 2
    yy = cy + (1 - f) * 18
    if box:
        hh = size * (2.3 if tem_frac else 1.34)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 26, yy - hh / 2, tot + 52, hh), 18, 18)
        c.drawRRect(r, blur_paint(box, 0.3 * f, 22))
        c.drawRRect(r, paint(BG1, 0.95 * f))
        c.drawRRect(r, paint(box, f, stroke=4))
    pos = []
    for it in items:
        w = _w(it, size)
        if it[0] == "/":
            _, n, d, col = it
            s2 = size * 0.8
            m = x + w / 2
            text_mid(c, n, m, yy - s2 * 0.62, s2, "black", col, f)
            text_mid(c, d, m, yy + s2 * 0.62, s2, "black", col, f)
            c.drawLine(x + size * 0.1, yy, x + w - size * 0.1, yy, paint(col, f, stroke=max(3, size * 0.06), cap_round=True))
        else:
            text(c, it[0], x, yy + size * 0.36, size, "black", it[1], f, align="left")
        pos.append((x, x + w))
        x += w
    return pos


# ---------------------------------------------------------------- figura: os dois muros, as cordas e o homem
Y0 = 780          # chão


def _muro(c, x, y0, alt, lado, a, hl=0.0, rot="", t=0):
    """muro de tijolos (contorno âmbar); lado = -1 cresce para a esquerda de x, +1 para a direita"""
    if a <= 0 or alt <= 0:
        return
    w = 46
    x0 = x - w if lado < 0 else x
    r = skia.Rect.MakeXYWH(x0, y0 - alt, w, alt)
    c.drawRect(r, paint(AMB, (0.16 + 0.2 * hl) * a))
    c.save(); c.clipRect(r)
    fiada = 22
    n = int(alt // fiada) + 1
    for i in range(n):
        y = y0 - (i + 1) * fiada
        c.drawLine(x0, y, x0 + w, y, paint(AMB, 0.45 * a, stroke=2))
        xm = x0 + (w / 2 if i % 2 == 0 else w / 4)
        c.drawLine(xm, y, xm, y + fiada, paint(AMB, 0.45 * a, stroke=2))
        if i % 2:
            c.drawLine(xm + w / 2, y, xm + w / 2, y + fiada, paint(AMB, 0.45 * a, stroke=2))
    c.restore()
    if hl > 0:
        c.drawRect(r, blur_paint(AMB, 0.6 * hl * a * (0.6 + 0.4 * math.sin(t * 6)), 16, stroke=10))
    c.drawRect(r, paint(AMB, a, stroke=4))
    if rot:
        text_mid(c, rot, x0 + w / 2 + lado * (w / 2 + 34), y0 - alt / 2, 56, "black", AMB, a,
                 align="right" if lado < 0 else "left")


def _homem(c, x, y0, alt, a, hl=0.0, t=0):
    """homem estilizado em ciano: cabeça no topo (y0 - alt)"""
    if a <= 0:
        return
    k = alt / 130
    top = y0 - alt
    rh = 13 * k
    glow = 0.35 + 0.5 * hl * (0.5 + 0.5 * math.sin(t * 6))
    pb = blur_paint(CYA, glow * a, 10, stroke=12 * k)
    for p_ in (pb, paint(CYA, a, stroke=9 * k, cap_round=True)):
        c.drawLine(x, top + 2 * rh + 4 * k, x, top + 0.62 * alt, p_)                      # tronco
        c.drawLine(x, top + 0.62 * alt, x - 13 * k, y0 - 2, p_)                           # pernas
        c.drawLine(x, top + 0.62 * alt, x + 13 * k, y0 - 2, p_)
        c.drawLine(x, top + 2 * rh + 12 * k, x - 20 * k, top + 0.55 * alt, p_)            # braços
        c.drawLine(x, top + 2 * rh + 12 * k, x + 20 * k, top + 0.55 * alt, p_)
    c.drawCircle(x, top + rh, rh, blur_paint(CYA, glow * a, 10))
    c.drawCircle(x, top + rh, rh, paint(CYA, a))


def _poly(c, pts, col, a, fill=0.2, stroke=4):
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, paint(col, fill * a))
    c.drawPath(p, paint(col, a, stroke=stroke))


def _arco(c, cx, cy, r, ang0, ang1, col, a):
    if a > 0:
        c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), ang0, ang1 - ang0, False,
                  paint(col, a, stroke=5, cap_round=True))


def _reto(c, x, y, lado, col, a, q=24):
    if a > 0:
        c.drawRect(skia.Rect.MakeXYWH(x if lado > 0 else x - q, y - q, q, q), paint(col, a, stroke=3))


def _cota(c, x0, x1, y, s, col, a, size=40):
    """cota horizontal com marcas nas pontas e rótulo embaixo"""
    if a <= 0:
        return
    c.drawLine(x0 + 3, y, x1 - 3, y, paint(col, a, stroke=3, cap_round=True))
    for x in (x0, x1):
        c.drawLine(x, y - 12, x, y + 12, paint(col, a, stroke=3, cap_round=True))
    if s:
        text_mid(c, s, (x0 + x1) / 2, y + size * 0.85, size, "black", col, a)


def cena(c, a, t, A=3, B=5, d=8, U=70, cx=LX, rotA="3", rotB="5", rot_h="", hl_corda=None, tri_hl=None,
         angs=0.0, cotas=None, linha_h=0.0, hl_homem=0.0, hl_muros=0.0, draw=1.0):
    """a figura completa (unidades → pixels com U). hl_corda: 'B' (corda do topo do muro B) ou 'A';
    tri_hl: (qual, k_grande, k_pequeno); cotas: dict(x=k, y=k, d=k, rot={...}); devolve a geometria"""
    if a <= 0:
        return None
    dp = d * U
    xl, xr = cx - dp / 2, cx + dp / 2
    h = A * B / (A + B)
    xm = xl + dp * A / (A + B)
    yh = Y0 - h * U
    # chão
    c.drawLine(xl - 120, Y0, xr + 120, Y0, paint(INK2, 0.5 * a, stroke=3))
    # triângulos destacados (embaixo de tudo)
    if tri_hl:
        qual, kg, kp = tri_hl
        if qual == "B":
            _poly(c, [(xl, Y0), (xr, Y0), (xr, Y0 - B * U)], AMB, a * kg, 0.16)
            _poly(c, [(xl, Y0), (xm, Y0), (xm, yh)], CYA, a * kp, 0.35)
        else:
            _poly(c, [(xr, Y0), (xl, Y0), (xl, Y0 - A * U)], AMB, a * kg, 0.16)
            _poly(c, [(xr, Y0), (xm, Y0), (xm, yh)], CYA, a * kp, 0.35)
    if linha_h > 0:   # a altura do cruzamento, tracejada
        p = paint(CYA, 0.7 * a * linha_h, stroke=3)
        p.setPathEffect(skia.DashPathEffect.Make([16, 12], -t * 30 % 28))
        c.drawLine(cx - 420, yh, cx + 420, yh, p)
    _muro(c, xl, Y0, A * U, -1, a, hl_muros, rotA, t)
    _muro(c, xr, Y0, B * U, +1, a, hl_muros, rotB, t)
    _homem(c, xm, Y0, h * U, a, hl_homem, t)
    # cordas
    for qual, p0, p1 in (("B", (xr, Y0 - B * U), (xl, Y0)), ("A", (xl, Y0 - A * U), (xr, Y0))):
        on = hl_corda == qual
        dim = 0.35 if hl_corda and not on else 1.0
        e = (p0[0] + (p1[0] - p0[0]) * draw, p0[1] + (p1[1] - p0[1]) * draw)
        if on:
            c.drawLine(*p0, *e, blur_paint(WHITE, 0.6 * a, 12, stroke=10))
        c.drawLine(*p0, *e, paint(WHITE, a * dim, stroke=6 if on else 4, cap_round=True))
    c.drawCircle(xm, yh, 7, paint(WHITE, a * clamp(draw * 4 - 3)))
    if angs > 0 and tri_hl:
        if tri_hl[0] == "B":
            ang = math.degrees(math.atan2(B * U, dp))
            for r in (60, 74):
                _arco(c, xl, Y0, r, -ang, 0, MNT, a * angs)
            _reto(c, xr, Y0, -1, WHITE, a * angs)
            _reto(c, xm, Y0, -1, WHITE, a * angs)
        else:
            ang = math.degrees(math.atan2(A * U, dp))
            for r in (60, 74):
                _arco(c, xr, Y0, r, 180, 180 + ang, MNT, a * angs)
            _reto(c, xl, Y0, +1, WHITE, a * angs)
            _reto(c, xm, Y0, +1, WHITE, a * angs)
    if rot_h:
        text_mid(c, rot_h, xm + 30, yh + h * U * 0.5, 44, "black", CYA, a, align="left")
    if cotas:
        rot = cotas.get("rot", {})
        _cota(c, xl, xm, Y0 + 40, rot.get("x", "x"), MNT, a * cotas.get("x", 0))
        _cota(c, xm, xr, Y0 + 40, rot.get("y", "y"), WHITE, a * cotas.get("y", 0))
        _cota(c, xl, xr, Y0 + (40 if not (cotas.get("x") or cotas.get("y")) else 115), rot.get("d", "d"), WHITE,
              a * cotas.get("d", 0))
    return dict(xl=xl, xr=xr, xm=xm, yh=yh, h=h)


# ---------------------------------------------------------------- blocos
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    kb = ep(t, tb, 0.4) * (1 - ep(t, tc, 0.4))
    cena(c, a, t, hl_homem=ep(t, tb + 2.5, 0.4) * (1 - ep(t, td, 0.3)), hl_muros=ep(t, ta, 0.3) * (1 - kb) * (1 - ep(t, tb, 0.3)),
         rot_h="?" if t >= tc else "", cotas=dict(d=ep(t, td, 0.3) * (1 - ep(t, te, 0.3)), rot=dict(d="d = ?")),
         hl_corda=None)
    board(c, a)
    label(c, L["pergunta"], RX, 280, a, 54, WHITE, "black")
    row(c, [P("muros: " if not EN else "walls: "), P("3", AMB), P("  e  " if not EN else "  and  "), P("5", AMB)], 400, a, 60)
    row(c, [P("h = ?", CYA)], 530, a * ep(t, tc, 0.3), 96, box=CYA)
    kd = a * ep(t, td, 0.25) * (1 - ep(t, te, 0.3))
    label(c, L["falta"], RX, 680, kd, 46, INK2, "bold")
    popill(c, L["nao_falta"], RX, 770, 40, AMB, BG0, kd, t, td + 2.6)
    ke = a * ep(t, te, 0.3)
    w1, w2 = (text_w(s, "black", 34) + 41 for s in (L["p_sem"], L["p_frac"]))
    x1 = RX - (w1 + w2 + 90) / 2 + w1 / 2
    x2 = x1 + w1 / 2 + 90 + w2 / 2
    popill(c, L["p_sem"], x1, 730, 34, CYA, BG0, ke, t, te + 2.0)
    label(c, "+", x1 + w1 / 2 + 45, 730, ke * ep(t, te + 2.6, 0.2), 54, WHITE, "black")
    popill(c, L["p_frac"], x2, 730, 34, AMB, BG0, ke, t, te + 3.2)


def _ang_marks(c, x0, y0, wb, hc, a, col=MNT):
    """marca do ângulo da base (vértice da direita) de um triângulo retângulo"""
    ang = math.degrees(math.atan2(hc, wb))
    for r in (44, 56):
        _arco(c, x0 + wb, y0, r, 180, 180 + ang, col, a)


def b_semelhanca(c, t, C, B):
    ta, tb, tc, td, te = (C[f"02.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_sem"], a)
    # pequeno 3-4 e grande 6-8 (a foto ampliada cresce a partir do pequeno)
    s = 46
    tri(c, 130, 800, 4 * s, 3 * s, a * ep(t, ta + 0.3, 0.4), t, "", "4" if t >= td else "", "3" if t >= td else "", size=44)
    u = ease_io(prog(t, tb + 0.3, 1.2))
    k = 1 + u
    x0 = 130 + (400 - 130) * u
    tri(c, x0, 800, 4 * s * k, 3 * s * k, a * ep(t, tb, 0.3), t, "", "8" if t >= td + 1.2 else "",
        "6" if t >= td + 1.2 else "", size=44)
    ke = a * ep(t, te, 0.3)
    _ang_marks(c, 130, 800, 4 * s, 3 * s, ke)
    _ang_marks(c, x0, 800, 4 * s * k, 3 * s * k, ke)
    if ke > 0:
        for (xx, ww, hh) in ((130, 4 * s, 3 * s), (x0, 4 * s * k, 3 * s * k)):
            c.drawRect(skia.Rect.MakeXYWH(xx, 800 - 36, 36, 36), paint(AMB, 0.4 * ke))
    label(c, "× 2", 640, 470, a * ep(t, tb + 1.4, 0.3), 54, AMB, "black")
    board(c, a)
    label(c, L["mesmos"], RX, 270, a * ep(t, ta + 1.2, 0.3), 46, WHITE, "black")
    label(c, L["foto"], RX, 350, a * ep(t, tb, 0.3), 36, INK2, "bold")
    row(c, [P(L["prop"], CYA)], 460, a * ep(t, tc, 0.3), 52, box=CYA)
    row(c, [F("6", "3"), P(" = 2   ·   "), F("8", "4"), P(" = 2")], 610, a * ep(t, td + 2.4, 0.3), 70)
    label(c, L["dois_ang"], RX, 760, a * ep(t, te, 0.3), 40, MNT, "black")
    label(c, L["soma180"], RX, 830, a * ep(t, te + 2.6, 0.3), 32, INK2, "bold")


def b_nomes(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_nomes"], a)
    kx = ep(t, tb, 0.3)
    cena(c, a, t, rot_h="h" if t >= ta + 1.5 else "", hl_homem=ep(t, ta + 1.5, 0.3) * (1 - ep(t, tb, 0.3)),
         cotas=dict(x=kx, y=ep(t, tb + 2.2, 0.3), d=ep(t, tc, 0.3)))
    board(c, a)
    row(c, [P("h", CYA), P("  →  " + L["altura"])], 280, a * ep(t, ta + 1.5, 0.3), 54)
    row(c, [P("x", MNT), P(",  "), P("y")], 400, a * kx, 64)
    row(c, [P("d"), P("  →  " + L["total"])], 520, a * ep(t, tc, 0.3), 54)
    row(c, [P("x", MNT), P(" + y = d")], 680, a * ep(t, tc + 2.6, 0.3), 84, box=AMB)
    label(c, L["guarde"], RX, 800, a * ep(t, td, 0.3), 38, AMB, "black")


def _par(c, t, C, B, cid, qual, alt):
    ta, tb, tc, td, *r = (C[f"{cid}.{k}"] for k in "abcde" if f"{cid}.{k}" in C)
    te = r[0] if r else td
    a = fade(t, B["start"], B["end"])
    header(c, L["s_par1" if qual == "B" else "s_par2"], a)
    kg, kp = ep(t, tb, 0.3), ep(t, tc, 0.3)
    base = "x" if qual == "B" else "y"
    cena(c, a, t, hl_corda=qual if t >= ta else None, tri_hl=(qual, kg, kp), angs=ep(t, td, 0.3),
         rot_h="h" if t >= tc else "", cotas=dict(x=kp if qual == "B" else 0, y=kp if qual == "A" else 0, d=kg))
    board(c, a)
    label(c, L["grande" if qual == "B" else "grande3"], RX, 280, a * kg, 42, AMB, "black")
    label(c, L["pequeno" if qual == "B" else "pequeno3"], RX, 370, a * kp, 42, CYA, "black")
    label(c, L["angs"], RX, 480, a * ep(t, td, 0.3), 38, MNT, "bold")
    popill(c, L["semel"], RX, 560, 36, MNT, BG0, a, t, td + (3.5 if qual == "B" else 1.5))
    row(c, [F("h", alt, CYA), P(" = "), F(base, "d", MNT if base == "x" else WHITE)], 760, a * ep(t, te if qual == "B" else td, 0.3),
        96, box=AMB)


def b_par1(c, t, C, B):
    _par(c, t, C, B, "04", "B", "5")


def b_par2(c, t, C, B):
    _par(c, t, C, B, "05", "A", "3")


def b_somar(c, t, C, B):
    ta, tb, tc, td, te = (C[f"06.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_somar"], a)
    cena(c, a, t, rot_h="h", cotas=dict(x=1, y=1, d=ep(t, td, 0.3)))
    board(c, a)
    dim = 1 - 0.5 * ep(t, tb, 0.3)
    row(c, [F("h", "5", CYA), P(" = "), F("x", "d", MNT)], 260, a * dim, 64, cx=RX - 200)
    row(c, [F("h", "3", CYA), P(" = "), F("y", "d")], 260, a * dim, 64, cx=RX + 200)
    row(c, [F("h", "5", CYA), P(" + "), F("h", "3", CYA), P(" = "), F("x", "d", MNT), P(" + "), F("y", "d")], 400,
        a * ep(t, tb + 0.4, 0.3), 64)
    pos = row(c, [P("= "), F("x + y", "d")], 610, a * ep(t, tc, 0.3), 64, cx=RX + 170)
    if pos and t >= td:
        kd = a * ep(t, td + 1.0, 0.3)
        x0, x1 = pos[1]
        strike(c, x0 + 6, x1 - 6, 610 - 34, kd, ep(t, td + 1.0, 0.3), AMB)
        label(c, "d", (x0 + x1) / 2, 610 - 90, kd, 50, AMB, "black")
        row(c, [P("= 1", AMB)], 610, a * ep(t, td + 2.6, 0.3), 64, cx=RX + 360)
    popill(c, L["sumiu"], RX - 250, 610, 34, AMB, BG0, a, t, te)
    row(c, [F("h", "5", CYA), P(" + "), F("h", "3", CYA), P(" = 1")], 770, a * ep(t, te + 1.2, 0.3), 84, box=AMB)


def b_fracoes(c, t, C, B):
    ta, tb, tc, td = (C[f"07.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_frac"], a)
    # barra de 15 pedaços: 3 (1/5) + 5 (1/3) = 8
    n3 = ep(t, tc + 0.4, 0.4)
    n5 = ep(t, tc + 2.4, 0.4)
    w, x0, y0, hh = 50, LX - 375, 470, 90
    for i in range(15):
        r = skia.Rect.MakeXYWH(x0 + i * w, y0, w, hh)
        col = MNT if i < 3 else CYA if i < 8 else None
        k = (n3 if i < 3 else n5 if i < 8 else 0) * a
        if col:
            c.drawRect(r, paint(col, 0.75 * k))
        c.drawRect(r, paint(INK2, a * ep(t, tb, 0.3), stroke=2))
    label(c, "15", LX, y0 - 50, a * ep(t, tb, 0.3), 44, WHITE, "black")
    label(c, "1/5 = 3/15", x0 + 75, y0 + hh + 55, a * n3, 34, MNT, "black")
    label(c, "1/3 = 5/15", x0 + 5.5 * w, y0 + hh + 55, a * n5, 34, CYA, "black")
    label(c, "8/15", LX, y0 + hh + 160, a * ep(t, td, 0.3), 64, AMB, "black")
    board(c, a)
    row(c, [F("h", "5", CYA), P(" + "), F("h", "3", CYA), P(" = 1")], 270, a, 56)
    row(c, [P("h", CYA), P(" · ( "), F("1", "5"), P(" + "), F("1", "3"), P(" ) = 1")], 400, a * ep(t, ta + 2.2, 0.3), 60)
    label(c, L["mmc"], RX, 520, a * ep(t, tb + 1.4, 0.3), 46, AMB, "black")
    row(c, [F("1", "5"), P(" = "), F("3", "15", MNT), P("    "), F("1", "3"), P(" = "), F("5", "15", CYA)], 640,
        a * ep(t, tc, 0.3), 60)
    row(c, [F("3", "15", MNT), P(" + "), F("5", "15", CYA), P(" = "), F("8", "15", AMB)], 790, a * ep(t, td, 0.3), 70, box=AMB)


def b_resolve(c, t, C, B):
    """isolar o h passo a passo: ×15 dos dois lados → 8h = 15 → ÷8 → h = 15/8; depois o atalho do inverso"""
    S = B["start"]
    tb, tc, td, te, tf = (C[f"08.{k}"] for k in "bcdef")
    K = lambda x: S + x  # noqa: E731  (segundos da fala desta cena)
    a = fade(t, B["start"], B["end"])
    header(c, L["s_res"], a)
    cena(c, a, t, rot_h=f"h = {H_TXT}" if t >= te else "h", hl_homem=ep(t, te, 0.3), linha_h=ep(t, te, 0.4))
    board(c, a)
    fase = lambda t0, t1: a * ep(t, t0, 0.35) * (1 - prog(t, t1 - 0.35, 0.35))  # noqa: E731
    # A — a equação e a forma 8h/15
    fa = fase(S, tb)
    row(c, [P("h", CYA), P(" · "), F("8", "15", AMB), P(" = 1")], 300, fa * ep(t, K(1.0), 0.3), 70)
    label(c, L["mesmo"], RX, 430, fa * ep(t, K(6.5), 0.3), 36, INK2, "bold")
    row(c, [F("8h", "15", CYA), P(" = 1")], 560, fa * ep(t, K(7.0), 0.3), 80, box=AMB)
    # B — ×15 dos dois lados
    fb = fase(tb, tc)
    row(c, [F("8h", "15", CYA), P(" = 1")], 270, fb, 60)
    label(c, L["sozinho"], RX + 270, 270, fb * ep(t, K(10.5), 0.3), 30, CYA, "bold")
    label(c, L["x15"], RX, 385, fb * ep(t, K(15.2), 0.3), 40, AMB, "black")
    pos = row(c, [F("8h", "15", CYA), P(" · 15", AMB), P("  =  "), P("1 · 15", AMB)], 510, fb * ep(t, K(15.6), 0.3), 70)
    if pos and t >= K(18.8):
        u = ep(t, K(18.8), 0.5)
        x0, x1 = pos[0]
        m0 = (x0 + x1) / 2
        strike(c, m0 - text_w("15", "black", 56) / 2 - 6, m0 + text_w("15", "black", 56) / 2 + 6, 510 + 56 * 0.62, fb, u, RED)
        x0, x1 = pos[1]
        strike(c, x1 - text_w("15", "black", 70) - 4, x1 + 4, 510, fb, u, RED)   # o 15 que multiplica
        label(c, "15 ÷ 15 = 1", (pos[0][0] + pos[1][1]) / 2, 600, fb * ep(t, K(19.6), 0.3), 32, RED, "bold")
    row(c, [P("8h", CYA), P(" = 15")], 730, fb * ep(t, K(24.8), 0.3), 84, box=AMB)
    # C — ÷8 dos dois lados
    fc = fase(tc, td)
    row(c, [P("8h", CYA), P(" = 15")], 270, fc, 60)
    label(c, L["d8"], RX, 385, fc * ep(t, K(31.9), 0.3), 40, AMB, "black")
    pos = row(c, [F("8h", "8", CYA), P("  =  "), F("15", "8")], 520, fc * ep(t, K(32.3), 0.3), 76)
    if pos and t >= K(33.6):
        x0, x1 = pos[0]
        u = ep(t, K(33.6), 0.5)
        m, s2 = (x0 + x1) / 2, 76 * 0.8
        xl = m - text_w("8h", "black", s2) / 2
        strike(c, xl - 4, xl + text_w("8", "black", s2) + 4, 520 - s2 * 0.62, fc, u, RED)   # o 8 de cima
        strike(c, m - text_w("8", "black", s2) / 2 - 6, m + text_w("8", "black", s2) / 2 + 6, 520 + s2 * 0.62, fc, u, RED)
    row(c, [P("h = ", CYA), F("15", "8", CYA)], 720, fc * ep(t, K(34.8), 0.3), 84, box=CYA)
    # D — de cabeça para baixo (o atalho do inverso)
    fd = fase(td, te)
    p1 = row(c, [P("h", CYA), P(" · "), F("8", "15", AMB), P(" = 1")], 290, fd, 64, cx=RX - 160)
    p2 = row(c, [P("h = ", CYA), F("15", "8", AMB)], 290, fd * ep(t, K(42.0), 0.3), 64, cx=RX + 250)
    if p1 and p2:
        ua = ep(t, K(40.3), 1.2)
        x0 = (p1[2][0] + p1[2][1]) / 2
        x1 = (p2[1][0] + p2[1][1]) / 2
        pth = skia.Path()
        pth.moveTo(x0, 360); pth.quadTo((x0 + x1) / 2, 470, x1, 360)
        meas = skia.PathMeasure(pth, False)
        seg = skia.Path(); meas.getSegment(0, meas.getLength() * ua, seg, True)
        c.drawPath(seg, paint(AMB, fd, stroke=5, cap_round=True))
        label(c, L["cabeca"], (x0 + x1) / 2, 500, fd * ep(t, K(43.0), 0.3), 36, AMB, "black")
    label(c, L["atalho"], RX, 590, fd * ep(t, K(46.4), 0.3), 40, CYA, "black")
    row(c, [F("8", "15", AMB), P(" · "), F("15", "8", AMB), P(" = "), F("120", "120"), P(" = 1", MNT)], 740,
        fd * ep(t, K(50.8), 0.3), 70, box=MNT)
    # E — resultado (como antes)
    fe = a * ep(t, te, 0.35)
    row(c, [P("h", CYA), P(" · "), F("8", "15", AMB), P(" = 1")], 280, fe, 60)
    row(c, [P("h = ", CYA), F("15", "8", CYA), P(f" = {H_TXT}", CYA)], 500, fe * ep(t, K(59.6), 0.3), 90, box=CYA)
    label(c, L["metros"], RX, 680, a * ep(t, tf + 3.8, 0.3), 44, WHITE, "black")
    popill(c, L["alto"], RX, 790, 32, MNT, BG0, a, t, K(72.8))


def b_distancia(c, t, C, B):
    ta, tb, tc, td = (C[f"09.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_dist"], a)
    # d: 8 → 11 (afastam) → 5 (aproximam) → 8
    if t < tb:
        d = 8
    elif t < tc:
        d = 8 + 2.5 * ease_io(prog(t, tb + 0.3, 2.2))
    elif t < td:
        d = 10.5 - 5.5 * ease_io(prog(t, tc, 2.4))
    else:
        d = 5 + 3 * ease_io(prog(t, td, 1.6))
    g = cena(c, a, t, d=d, U=58, cx=LX - 30, rot_h=H_TXT, linha_h=ep(t, tb, 0.4), hl_homem=0.3,
             cotas=dict(d=1, rot=dict(d=f"d = {d:.1f}".replace(".", DEC))))
    board(c, a)
    row(c, [P("d = ?")], 290, a * ep(t, ta, 0.3), 70)
    popill(c, L["nao_imp"], RX, 400, 40, AMB, BG0, a, t, ta + 1.6)
    row(c, [P("h = ", CYA), P(H_TXT, CYA)], 560, a * ep(t, tb, 0.3), 84, box=CYA)
    label(c, L["cancelou"], RX, 760, a * ep(t, td, 0.3), 40, MNT, "black")


def b_confere(c, t, C, B):
    ta, tb, tc = (C[f"10.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_conf"], a)
    cena(c, a, t, rot_h="h", cotas=dict(x=ep(t, tb + 1.0, 0.3), y=ep(t, tb + 4.5, 0.3), d=ep(t, ta + 1.0, 0.3),
                                         rot=dict(x="3", y="5", d="8")))
    board(c, a)
    row(c, [P(L["caso"])], 270, a * ep(t, ta + 1.0, 0.3), 64)
    row(c, [P("x", MNT), P(" = 8 · "), F("h", "5", CYA), P(" = "), P("3", MNT)], 400, a * ep(t, tb, 0.3), 64)
    row(c, [P("y = 8 − 3 = 5")], 520, a * ep(t, tb + 4.5, 0.3), 64)
    row(c, [F("h", "3", CYA), P(" = "), F("15", "8 · 3"), P(" = "), F("5", "8", AMB)], 680, a * ep(t, tc + 3.0, 0.3), 64)
    pos = row(c, [F("y", "d"), P(" = "), F("5", "8", AMB)], 820, a * ep(t, tc + 0.6, 0.3), 64)
    if pos:
        check(c, pos[-1][1] + 60, 820, 30, a * ep(t, tc + 5.5, 0.25))


def b_generaliza(c, t, C, B):
    ta, tb, tc, td = (C[f"11.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gen"], a)
    if t < tc:
        A_, B_, U, rA, rB = 3, 5, 70, "a" if t < tb else "3", "b" if t < tb else "5"
    elif t < td:
        u = ease_io(prog(t, tc, 1.0))
        A_, B_, U, rA, rB = 3 + u, 5 - u, 70, "4", "4"
    else:
        u = ease_io(prog(t, td, 1.2))
        A_, B_, U, rA, rB = 4 + 6 * u, 4 + 11 * u, 70 - 41 * u, "10", "15"
    rh = "?" if t >= td else (f"h = {H_TXT}" if tb <= t < tc else ("h = 2" if t >= tc + 3 else "h"))
    cena(c, a, t, A=A_, B=B_, d=8 if t < td else 13, U=U, rotA=rA, rotB=rB, rot_h=rh, linha_h=ep(t, tc + 3, 0.3) * (1 - ep(t, td, 0.3)))
    board(c, a)
    row(c, [P("h = ", CYA), F("a · b", "a + b")], 290, a * ep(t, ta + 2.0, 0.3), 80, box=CYA)
    label(c, L["prod_soma"], RX, 400, a * ep(t, ta + 6.0, 0.3), 34, INK2, "bold")
    row(c, [F("3 · 5", "3 + 5", AMB), P(" = "), F("15", "8", CYA)], 520, a * ep(t, tb, 0.3) * (1 - 0.5 * ep(t, td, 0.3)), 56)
    row(c, [F("4 · 4", "4 + 4", AMB), P(" = "), F("16", "8"), P(" = "), P("2", MNT)], 640,
        a * ep(t, tc + 1.2, 0.3) * (1 - 0.5 * ep(t, td, 0.3)), 56)
    label(c, L["iguais"], RX, 720, a * ep(t, tc + 4.0, 0.3) * (1 - 0.5 * ep(t, td, 0.3)), 32, MNT, "bold")
    row(c, [P(L["desafio"], AMB)], 810, a * ep(t, td, 0.3), 60, box=AMB)
    label(c, L["comenta"], RX, 880, a * ep(t, td + 3.0, 0.3), 30, INK2, "bold")


def b_resumo(c, t, C, B):
    ks = [C[f"12.{k}"] for k in "bcde"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resumo"], a)
    for i, (s, t0) in enumerate(zip(L["passos"], ks)):
        y = 300 + i * 150
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        x = 560
        c.drawCircle(x, y, 34, paint(AMB, ki))
        text_mid(c, str(i + 1), x, y, 38, "black", BG0, ki)
        text_mid(c, s, x + 70, y, 56, "black", WHITE, ki, align="left")
        check(c, 1420, y, 24, ki * ep(t, t0 + 0.5, 0.2))


def _icone(c, i, cx, cy, a, t):
    """miniatura de cada aula: dois triângulos semelhantes · proporção · soma de frações"""
    if i == 0:
        tri(c, cx - 150, cy + 50, 100, 75, a, t, "", "", "", size=20)
        tri(c, cx - 20, cy + 50, 170, 128, a, t, "", "", "", size=20)
    elif i == 1:
        row(c, [F("h", "5", CYA), P(" = "), F("x", "d", MNT)], cy, a, 56, cx=cx, maxw=300)
    else:
        row(c, [F("3", "15", MNT), P(" + "), F("5", "15", CYA)], cy, a, 56, cx=cx, maxw=300)


def b_aulas(c, t, C, B):
    """convite para as aulas do assunto no canal (toda questão termina assim) + CTA"""
    ta, tb, tc, td, te, tf = (C[f"13.{k}"] for k in "abcdef")
    a = fade(t, B["start"], B["end"], d_out=0.01)
    ka = a * (1 - ep(t, tf, 0.4))
    header(c, L["s_aulas"], ka)
    cores = (CYA, AMB, MNT)
    for i, (t0, (l1, l2)) in enumerate(zip((tb, tc, td), L["aulas"])):
        k = ka * pop(t, t0, 0.4)
        if k <= 0:
            continue
        x, w = 180 + i * 560, 480
        cx = x + w / 2
        c.save(); c.translate(cx, 520); c.scale(k, k); c.translate(-cx, -520)
        kk = min(1, ka)
        cartao(c, x, 260, w, 520, kk, cores[i], L["aula"])
        _icone(c, i, cx, 420, kk, t)
        if l1:
            text_mid(c, l1, cx, 610, 50, "black", WHITE, kk)
        text_mid(c, l2, cx, 674 if l1 else 640, 50, "black", cores[i], kk)
        c.restore()
    label(c, L["no_canal"], 960, 870, ka * ep(t, te, 0.3), 40, AMB, "extrabold")
    kg = a * ep(t, tf, 0.4)
    if kg > 0:
        glow_text(c, L["canal"], 960, 400, 120, "black", WHITE, kg, glow=0.12)
        w = text_w(L["canal"], "black", 120)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(960 - w / 2, 430, w * ep(t, tf + 0.3, 0.6), 14), 7, 7), paint(AMB, kg))
        pulse = 1 + 0.03 * math.sin(t * 5)
        c.save(); c.translate(960, 560); c.scale(pulse, pulse)
        pill(c, L["inscreva"], 0, 0, 38, CYA, BG0, kg * ep(t, tf + 0.8, 0.3))
        c.restore()
        c.save(); c.translate(960, 900); c.scale(0.5, 0.5); c.translate(-960, -820)
        cena(c, kg * 0.9 * ep(t, tf + 1.2, 0.4), t, cx=960, rotA="", rotB="")
        c.restore()


BLOCKS = dict(gancho=b_gancho, semelhanca=b_semelhanca, nomes=b_nomes, par1=b_par1, par2=b_par2, somar=b_somar,
              fracoes=b_fracoes, resolve=b_resolve, distancia=b_distancia, confere=b_confere, generaliza=b_generaliza,
              resumo=b_resumo, aulas=b_aulas)
