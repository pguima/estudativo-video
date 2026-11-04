"""Visual — Estudativo · Questão de Matemática 018 (aula horizontal 1920x1080): ENEM 2025, questão 141, as cores do poliedro.
Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Figura principal: o protótipo em 3D (solido()), um prisma de n lados com um tronco de pirâmide em cima, projetado em
perspectiva paralela com descarte das faces de trás (cada sólido é convexo); explode afasta o tronco do prisma.
As faces são de cinco tipos: 'base' (hexágono de baixo), 'ret' (retângulos), 'cola' (as bases coladas, que ficam dentro),
'trap' (trapézios) e 'topo' (hexágono menor). Cores das QUATRO classes pintadas: âmbar (base), ciano (retângulos),
menta (trapézios), rosa (topo); coral = erro (a pegadinha dos dois hexágonos)."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_018_matematica_poliedro_cores.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.c": "shimmer", "02.c": "confirm", "02.d": "deny", "03.b": "whoosh", "03.c": "whoosh", "04.b": "impact",
        "05.b": "data", "05.c": "data", "05.d": "data", "05.e": "data", "06.b": "confirm", "06.c": "confirm",
        "06.d": "confirm", "06.e": "impact", "07.b": "alert", "07.c": "deny", "08.b": "confirm", "08.c": "lock",
        "10.a": "shimmer", "10.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo (só os efeitos)

ROSA = "#FF8FB1"
COR = dict(base=AMB, ret=CYA, trap=MNT, topo=ROSA)

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 018", "QUESTÃO DE MATEMÁTICA · 018"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_cong=("THE KEY WORD · CONGRUENT", "A PALAVRA-CHAVE · CONGRUENTE"),
    s_sol=("THE TWO SOLIDS", "OS DOIS SÓLIDOS"), s_jun=("STEP 1 · JOIN THE PIECES", "PASSO 1 · JUNTAR AS PEÇAS"),
    s_faces=("STEP 2 · THE OUTSIDE FACES", "PASSO 2 · AS FACES DE FORA"), s_cores=("STEP 3 · GROUP THE CONGRUENT ONES", "PASSO 3 · AGRUPAR AS CONGRUENTES"),
    s_peg=("THE TRAP · THE TWO HEXAGONS", "A PEGADINHA · OS DOIS HEXÁGONOS"),
    s_gen=("WHAT IF IT WERE A FULL PYRAMID?", "E SE FOSSE UMA PIRÂMIDE INTEIRA?"), s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 141", "ENEM 2025 · questão 141"),
    prisma=("hexagonal prism", "prisma hexagonal"), tronco=("+ hexagonal frustum", "+ tronco de pirâmide hexagonal"),
    regra=("congruent faces → same color", "faces congruentes → mesma cor"), cores_q=("colors = ", "cores = "),
    cong_def=("congruent =", "congruente ="), forma=("same SHAPE", "mesma FORMA"), tam=("+ same SIZE", "+ mesmo TAMANHO"),
    encaixa=("one fits exactly on the other", "uma encaixa certinho na outra"),
    sim=("side 2 and side 2: congruent", "lado 2 e lado 2: congruentes"), nao=("side 2 and side 4: NOT congruent", "lado 2 e lado 4: NÃO são"),
    p_bases=("2 equal hexagons (bases)", "2 hexágonos iguais (bases)"), p_lat=("6 equal rectangles", "6 retângulos iguais"),
    t_bases=("1 larger + 1 smaller hexagon", "1 hexágono maior + 1 menor"), t_lat=("6 equal trapezoids", "6 trapézios iguais"),
    l_prisma=("PRISM", "PRISMA"), l_tronco=("FRUSTUM", "TRONCO"),
    coincide=("larger base = base of the prism", "base maior = base do prisma"), coladas=("glued faces → INSIDE", "faces coladas → DENTRO"),
    sem_tinta=("no paint", "sem tinta"),
    f_base=("1 hexagon (bottom)", "1 hexágono (embaixo)"), f_ret=("6 rectangles", "6 retângulos"), f_trap=("6 trapezoids", "6 trapézios"),
    f_topo=("1 smaller hexagon (top)", "1 hexágono menor (em cima)"), f_tot=("14 faces", "14 faces"),
    c_ret=("rectangles", "retângulos"), c_trap=("trapezoids", "trapézios"), c_base=("bottom hexagon", "hexágono de baixo"),
    c_topo=("top hexagon (smaller)", "hexágono de cima (menor)"), quatro=("4 colors", "4 cores"),
    hex_hex=("hexagon = hexagon?", "hexágono = hexágono?"), tres=("3 colors → E ?", "3 cores → E ?"),
    semelhantes=("SIMILAR, not congruent", "SEMELHANTES, não congruentes"), faces_cores=("14 faces · 4 kinds", "14 faces · 4 tipos"),
    piramide=("hexagon · rectangles · triangles", "hexágono · retângulos · triângulos"), tres_c=("3 colors", "3 cores"),
    desafio=("a CUBE + a square frustum?", "um CUBO + tronco de base quadrada?"), quantas=("how many colors?", "quantas cores?"),
    comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["join: glued bases go inside", "list the 14 outside faces", "group the congruent ones: 4 colors (D)",
             "same shape, different size: not congruent"],
            ["juntar: as bases coladas ficam dentro", "listar as 14 faces de fora", "agrupar as congruentes: 4 cores (D)",
             "mesma forma e tamanho diferente: não é"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("", "Prisms"), ("Pyramids and", "frustums"), ("Congruence and", "similarity")],
           [("", "Prismas"), ("Pirâmides e", "troncos"), ("Congruência e", "semelhança")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025"), ("três dê", "3D"), ("três cores", "3 cores")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
matematica.EXPRESSOES |= {("forma", "mais")}


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- o sólido em 3D
def _faces(n=6, R=1.0, H=1.1, r=0.55, F=0.75, explode=0.0, ponta=False):
    """faces do protótipo (coordenadas do mundo, y para cima): lista de (tipo, sólido, [vértices]).
    sólido 0 = prisma (y de 0 a H), 1 = tronco (y de H a H + F, deslocado para cima por explode)"""
    ang = [2 * math.pi * k / n + math.pi / n for k in range(n)]
    P = lambda rr, y: [(rr * math.cos(a), y, rr * math.sin(a)) for a in ang]   # noqa: E731
    b0, b1 = P(R, 0), P(R, H)
    y2 = H + explode
    g0, g1 = P(R, y2), ([(0, y2 + F, 0)] * n if ponta else P(r, y2 + F))
    out = [("base", 0, b0[::-1]), ("cola", 0, b1)]
    for k in range(n):
        j = (k + 1) % n
        out.append(("ret", 0, [b0[k], b0[j], b1[j], b1[k]]))
    out.append(("cola", 1, g0[::-1]))
    if not ponta:
        out.append(("topo", 1, g1))
    for k in range(n):
        j = (k + 1) % n
        out.append(("trap", 1, [g0[k], g0[j], g1[j], g1[k]] if not ponta else [g0[k], g0[j], g1[0]]))
    return out


def solido(c, cx, cy, s, t, a=1.0, yaw=None, pitch=0.42, explode=0.0, pintura=None, so=None, hl=None, n=6, R=1.0, H=1.1,
           r=0.55, F=0.75, ponta=False, fundo=None):
    """desenha o protótipo. pintura = {tipo: alfa da cor} (0 = cinza-azulado); so = {sólidos visíveis};
    hl = {tipo: alfa de um contorno âmbar}; cy = altura do centro do prisma; fundo = alfa das faces de trás (tracejado)"""
    if a <= 0:
        return
    yaw = (0.35 + 0.18 * t) if yaw is None else yaw
    cyw, syw, cp, sp = math.cos(yaw), math.sin(yaw), math.cos(pitch), math.sin(pitch)
    ymid = (H + F + explode) / 2

    def rot(p):
        x, y, z = p
        return (x * cyw + z * syw, y - ymid, -x * syw + z * cyw)

    def proj(q):
        return (cx + s * q[0], cy - s * (q[1] * cp) + s * q[2] * sp)
    v = (0.0, sp, cp)                                         # direção de quem olha (de cima e da frente)
    luz = (-0.35, 0.8, 0.5)
    faces = _faces(n, R, H, r, F, explode, ponta)
    centros = {}
    for so_ in (0, 1):
        pts = [p for _, k, vs in faces if k == so_ for p in vs]
        centros[so_] = [sum(q[i] for q in pts) / len(pts) for i in range(3)]
    pintura = pintura or {}
    hl = hl or {}
    for so_ in ((0, 1) if sp >= 0 else (1, 0)):   # de cima, o tronco por último; de baixo, o prisma por último
        if so is not None and so_ not in so:
            continue
        cen = rot(centros[so_])
        desenhar = []
        for tipo, k, vs in faces:
            if k != so_ or (tipo == "cola" and explode < 0.02 and so is None):   # juntas, as bases coladas somem
                continue
            q = [rot(p) for p in vs]
            u = [q[1][i] - q[0][i] for i in range(3)]
            w = [q[-1][i] - q[0][i] for i in range(3)]
            nn = [u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]]
            fc = [sum(p[i] for p in q) / len(q) for i in range(3)]
            if sum(nn[i] * (fc[i] - cen[i]) for i in range(3)) < 0:
                nn = [-x for x in nn]
            ln = math.sqrt(sum(x * x for x in nn)) or 1
            nn = [x / ln for x in nn]
            vis = sum(nn[i] * v[i] for i in range(3)) > 1e-6
            desenhar.append((vis, tipo, q, nn))
        if fundo:
            for vis, tipo, q, nn in desenhar:
                if not vis:
                    pth = skia.Path(); pth.addPoly([skia.Point(*proj(p)) for p in q], True)
                    pd = paint(INK2, a * fundo * 0.6, stroke=2); pd.setPathEffect(skia.DashPathEffect.Make([8, 8], 0))
                    c.drawPath(pth, pd)
        for vis, tipo, q, nn in desenhar:
            if not vis:
                continue
            br = 0.55 + 0.45 * max(0.0, sum(nn[i] * luz[i] for i in range(3)) / 1.03)
            pth = skia.Path(); pth.addPoly([skia.Point(*proj(p)) for p in q], True)
            base = mix_hex(BG2, "#3A4F7A", br)
            kp = pintura.get(tipo, 0.0)
            cor = mix_hex(base, mix_hex("#000000", COR.get(tipo, RED if tipo == "cola" else AMB), 0.45 + 0.55 * br), kp)
            c.drawPath(pth, paint(cor, a))
            c.drawPath(pth, paint(WHITE if kp < 0.5 else BG0, a * 0.75, stroke=2.5))
            if hl.get(tipo, 0) > 0:
                c.drawPath(pth, paint(AMB, a * hl[tipo], stroke=6))


def mix_hex(c1, c2, u):
    """mistura de duas cores '#RRGGBB' (u = 0 → c1, 1 → c2)"""
    u = clamp(u)
    a_ = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b_ = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{int(round(x + (y - x) * u)):02X}" for x, y in zip(a_, b_))


def hexagono(c, cx, cy, R, cor, a, stroke=False):
    pth = skia.Path()
    pth.addPoly([skia.Point(cx + R * math.cos(math.pi / 3 * k), cy + R * math.sin(math.pi / 3 * k)) for k in range(6)], True)
    c.drawPath(pth, paint(cor, a, stroke=4) if stroke else paint(cor, a))


def _card_enunciado(c, a):
    img = _img_enunciado()
    w = 760
    h = img.height() * w / img.width()
    x, y = LX - w / 2 - 20, 545 - h / 2
    rrect(c, x - 18, y - 18, w + 36, h + 36, 22, "#FFFFFF", a)
    c.drawImageRect(img, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), paint(WHITE, a))


@lru_cache(None)
def _img_enunciado():
    from pathlib import Path
    return skia.Image.open(str(Path(__file__).resolve().parent.parent / "enunciado" / "questao.png"))


def item(c, y, s, a, col=WHITE, marca=None, size=42):
    """linha do quadro com um quadradinho de cor (marca) à esquerda"""
    if a <= 0:
        return
    x = BX0 + 80
    if marca:
        rrect(c, x - 22, y - 22, 44, 44, 10, marca, a)
    text_mid(c, s, x + 44, y, size, "black", col, a, align="left")


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_enunciado(c, a)
    board(c, a)
    label(c, L["enem"], RX, 250, a, 40, INK2, "extrabold")
    label(c, L["prisma"], RX, 345, a, 46, AMB, "black")
    label(c, L["tronco"], RX, 410, a, 40, AMB, "black")
    label(c, L["regra"], RX, 540, a * ep(t, tb, 0.3), 42, WHITE, "black")
    eq(c, [(L["cores_q"], WHITE), ("?", CYA)], 690, a * ep(t, tc, 0.3), 64, box=CYA)


def quadrado(c, x, y, lado, cor, a, k=1.0):
    if a <= 0:
        return
    w = lado * k
    rrect(c, x - w / 2, y - w / 2, w, w, 8, cor, 0.25 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2, y - w / 2, w, w), 8, 8), paint(cor, a, stroke=4))


def b_congruencia(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_cong"], a)
    kc = a * ep(t, tb + 1.5, 0.3) * (1 - ep(t, td, 0.3))
    if kc > 0:   # dois quadrados de lado 2: um desliza para cima do outro
        u = ease_io(prog(t, tc + 0.6, 1.2))
        quadrado(c, LX - 150, 470, 160, MNT, kc)
        quadrado(c, LX + 150 - 300 * u, 470, 160, CYA, kc)
        label(c, "2", LX - 150, 580, kc, 36, INK2, "black")
        if u >= 1:
            check(c, LX - 150, 470, 34, kc * ep(t, tc + 1.9, 0.2))
    kd = a * ep(t, td, 0.3)
    if kd > 0:   # lado 2 e lado 4
        quadrado(c, LX - 200, 520, 120, CYA, kd)
        quadrado(c, LX + 110, 520, 240, AMB, kd)
        label(c, "2", LX - 200, 610, kd, 36, INK2, "black")
        label(c, "4", LX + 110, 670, kd, 36, INK2, "black")
        cross(c, LX - 45, 520, 30, kd * ep(t, td + 3.0, 0.2))
    board(c, a)
    label(c, L["cong_def"], RX, 270, a * ep(t, ta + 0.6, 0.3), 44, CYA, "black")
    label(c, L["forma"], RX, 360, a * ep(t, tb + 1.5, 0.3), 48, WHITE, "black")
    label(c, L["tam"], RX, 440, a * ep(t, tb + 2.4, 0.3), 48, WHITE, "black")
    label(c, L["encaixa"], RX, 530, a * ep(t, tb + 3.6, 0.3), 32, INK2, "bold")
    eq(c, [(L["sim"], MNT)], 660, a * ep(t, tc + 0.5, 0.3), 40)
    eq(c, [(L["nao"], RED)], 770, a * ep(t, td + 1.0, 0.3), 40, box=RED)


def b_solidos(c, t, C, B):
    ta, tb, tc = (C[f"03.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_sol"], a)
    kb = a * ep(t, tb, 0.4)
    kc = a * ep(t, tc, 0.4)
    solido(c, LX - 215, 540, 160, t, kb, so={0}, explode=0)
    label(c, L["l_prisma"], LX - 215, 820, kb, 32, CYA, "black")
    # o tronco sozinho, ao lado (cy ajustado: o centro do desenho é o meio da peça inteira)
    solido(c, LX + 215, 620, 160, t, kc, so={1}, explode=0)
    label(c, L["l_tronco"], LX + 215, 820, kc, 32, MNT, "black")
    board(c, a)
    label(c, L["l_prisma"], RX, 260, kb, 36, CYA, "black")
    item(c, 340, L["p_bases"], a * ep(t, tb + 2.0, 0.3), WHITE, AMB)
    item(c, 420, L["p_lat"], a * ep(t, tb + 5.0, 0.3), WHITE, CYA)
    label(c, L["l_tronco"], RX, 540, kc, 36, MNT, "black")
    item(c, 620, L["t_bases"], a * ep(t, tc + 4.0, 0.3), WHITE, ROSA)
    item(c, 700, L["t_lat"], a * ep(t, tc + 7.5, 0.3), WHITE, MNT)


def b_juncao(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_jun"], a)
    ex = 0.9 * (1 - ease_io(prog(t, tc - 0.4, 1.6)))
    kh = ep(t, tb + 1.0, 0.3)
    solido(c, LX, 560, 190, t, a, explode=ex, pitch=0.62, pintura={"cola": kh * (1 - ep(t, tc + 1.5, 0.5))}, fundo=0.8)
    board(c, a)
    label(c, L["coincide"], RX, 300, a * ep(t, tb + 0.4, 0.3), 40, WHITE, "black")
    eq(c, [(L["coladas"], RED)], 460, a * ep(t, tc, 0.3), 48, box=RED)
    popill(c, L["sem_tinta"], RX, 600, 34, RED, BG0, a * ep(t, tc + 3.0, 0.3), t, tc + 3.0)


_ORDEM_F = ["base", "ret", "trap", "topo"]


def b_faces(c, t, C, B):
    ta, tb, tc, td, te = (C[f"05.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_faces"], a)
    ts = dict(base=tb, ret=tc, trap=td, topo=te)
    atual = max([k for k in _ORDEM_F if t >= ts[k]], key=lambda k: ts[k], default=None)
    hl = {k: (1.0 if k == atual else 0.0) for k in _ORDEM_F}
    pv = 0.42 + (-0.35 - 0.42) * ep(t, tb, 0.6) * (1 - ep(t, tc - 0.3, 0.6))
    solido(c, LX, 540, 215, t, a, pitch=pv, hl=hl)
    board(c, a)
    linhas = [("base", L["f_base"]), ("ret", L["f_ret"]), ("trap", L["f_trap"]), ("topo", L["f_topo"])]
    for j, (k, s) in enumerate(linhas):
        item(c, 280 + j * 95, s, a * ep(t, ts[k] + 0.4, 0.3), AMB if k == atual else WHITE, INK2)
    eq(c, [(L["f_tot"], CYA)], 720, a * ep(t, te + 3.0, 0.3), 56, box=CYA)


def b_cores(c, t, C, B):
    ta, tb, tc, td, te = (C[f"06.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_cores"], a)
    pint = dict(ret=ep(t, tb + 1.0, 0.5), trap=ep(t, tc + 1.0, 0.5), base=ep(t, td + 3.0, 0.5), topo=ep(t, td + 5.0, 0.5))
    pv = 0.42 + (-0.3 - 0.42) * ep(t, td + 2.4, 0.6) * (1 - ep(t, td + 4.6, 0.6))
    solido(c, LX, 540, 215, t, a, pitch=pv, pintura=pint)
    board(c, a)
    item(c, 270, L["c_ret"], a * ep(t, tb + 0.8, 0.3), WHITE, CYA)
    item(c, 360, L["c_trap"], a * ep(t, tc + 0.8, 0.3), WHITE, MNT)
    item(c, 450, L["c_base"], a * ep(t, td + 3.0, 0.3), WHITE, AMB)
    item(c, 540, L["c_topo"], a * ep(t, td + 5.0, 0.3), WHITE, ROSA)
    eq(c, [(L["quatro"], MNT)], 670, a * ep(t, te + 0.6, 0.3), 64, box=MNT)
    for j, (le, v) in enumerate(zip("ABCDE", ("9", "8", "6", "4", "3"))):
        x = BX0 + 130 + j * 160
        k = a * ep(t, te + 2.0 + j * 0.08, 0.2)
        col = MNT if le == "D" else INK2
        text_mid(c, le, x - 22, 810, 40, "black", col, k)
        text_mid(c, v, x + 14, 810, 40, "black", WHITE if le == "D" else INK2, k, align="left")
    kk = a * ep(t, te + 2.6, 0.3)
    if kk > 0:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX0 + 130 + 3 * 160 - 56, 810 - 38, 112, 76), 16, 16)
        c.drawRRect(r, paint(MNT, kk, stroke=4))


def b_pegadinha(c, t, C, B):
    ta, tb, tc, td = (C[f"07.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    kh = a * ep(t, ta + 0.5, 0.3) * (1 - ep(t, td, 0.3))
    if kh > 0:   # os dois hexágonos, lado a lado; depois o menor vai para cima do maior
        u = ease_io(prog(t, tc + 0.8, 1.2))
        hexagono(c, LX - 150, 520, 170, AMB, kh * 0.3)
        hexagono(c, LX - 150, 520, 170, AMB, kh, stroke=True)
        x2 = LX + 200 - 350 * u
        hexagono(c, x2, 520, 95, ROSA, kh * 0.3)
        hexagono(c, x2, 520, 95, ROSA, kh, stroke=True)
        label(c, L["semelhantes"], LX, 780, kh * ep(t, tc + 2.6, 0.3), 36, WHITE, "black")
    kd = a * ep(t, td, 0.3)
    if kd > 0:
        solido(c, LX, 540, 215, t, kd, pintura=dict(ret=1, trap=1, base=1, topo=1))
    board(c, a)
    label(c, L["hex_hex"], RX, 280, a * ep(t, tb + 0.6, 0.3), 46, WHITE, "black")
    pos = eq(c, [(L["tres"], RED)], 400, a * ep(t, tb + 3.6, 0.3), 54)
    if pos:
        strike(c, pos[0][0], pos[-1][1], 400, a, ep(t, tc, 0.4))
    label(c, L["semelhantes"], RX, 520, a * ep(t, tc + 2.6, 0.3), 36, RED, "black")
    eq(c, [(L["faces_cores"], MNT)], 680, a * ep(t, td + 3.0, 0.3), 50, box=MNT)


def b_generaliza(c, t, C, B):
    ta, tb, tc = (C[f"08.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gen"], a)
    ka = a * (1 - ep(t, tc, 0.3))
    if ka > 0:
        kp = ep(t, tb + 2.0, 0.5)
        solido(c, LX, 540, 200, t, ka, ponta=True, F=1.0, pintura=dict(base=kp, ret=kp, trap=kp))
    kc = a * ep(t, tc, 0.3)
    if kc > 0:   # o desafio: cubo + tronco de base quadrada (sem pintar: não entrega a resposta)
        R4 = 1.0
        solido(c, LX, 540, 200, t, kc, n=4, R=R4, H=R4 * math.sqrt(2), r=0.45, F=0.6)
    board(c, a)
    if ka > 0:
        label(c, L["piramide"], RX, 330, ka * ep(t, tb + 2.0, 0.3), 36, WHITE, "black")
        eq(c, [(L["tres_c"], MNT)], 470, ka * ep(t, tb + 5.6, 0.3), 60, box=MNT)
    if kc > 0:
        label(c, L["desafio"], RX, 330, kc * ep(t, tc + 0.8, 0.3), 38, AMB, "black")
        label(c, L["quantas"], RX, 470, kc * ep(t, tc + 4.6, 0.3), 54, WHITE, "black")
        label(c, L["comenta"], RX, 640, kc * ep(t, tc + 6.0, 0.3), 38, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"09.{k}"] for k in "bcde"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resumo"], a)
    for i, (s, t0) in enumerate(zip(L["passos"], ks)):
        y = 280 + i * 160
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        x = 300
        c.drawCircle(x, y, 34, paint(AMB, ki))
        text_mid(c, str(i + 1), x, y, 38, "black", BG0, ki)
        text_mid(c, s, x + 70, y, 50, "black", WHITE, ki, align="left")
        check(c, 1660, y, 24, ki * ep(t, t0 + 0.5, 0.2))


def b_aulas(c, t, C, B):
    """convite para as aulas do assunto no canal (toda questão termina assim) + CTA"""
    ta, tb, tc, td, te, tf = (C[f"10.{k}"] for k in "abcdef")
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
        if i == 0:
            solido(c, cx, 440, 70, t, kk, so={0}, pintura=dict(base=1, ret=1), F=0.0)
        elif i == 1:
            solido(c, cx, 420, 80, t, kk, so={1}, H=0.0, pintura=dict(trap=1, topo=1))
        else:
            hexagono(c, cx - 50, 420, 70, AMB, kk, stroke=True)
            hexagono(c, cx + 75, 435, 42, ROSA, kk, stroke=True)
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
        solido(c, 960, 790, 70, t, kg * ep(t, tf + 1.2, 0.4), pintura=dict(base=1, ret=1, trap=1, topo=1))


BLOCKS = dict(gancho=b_gancho, congruencia=b_congruencia, solidos=b_solidos, juncao=b_juncao, faces=b_faces,
              cores=b_cores, pegadinha=b_pegadinha, generaliza=b_generaliza, resumo=b_resumo, aulas=b_aulas)
