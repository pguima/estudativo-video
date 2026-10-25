"""Design system dos vídeos de MATEMÁTICA do Estudativo (aulas e questões; PT e Estudativo English), 1920x1080.
Nasceu na questão 001 (canais/enem/questoes/001_matematica_triangulo_cateto_5). No visual.py do vídeo:

    from matematica import *     # paleta, layout, componentes, figuras, fundo e legenda
    def OVERLAY(c, t): selo(c, L["selo"], t)

Tela de aula: figura à esquerda (centro LX), quadro com as contas à direita (centro RX, caixa BX0..BX1 × BY0..BY1),
título da cena no alto (header), selo no canto, legenda karaokê embaixo (CAP_Y).
Cores com função (sempre as mesmas):
    AMB  âmbar   dado do problema, número que o enunciado deu, passo atual, palavra falada na legenda
    CYA  ciano   incógnita principal / hipotenusa / destaque *x* do roteiro / fórmula em caixa
    MNT  menta   segunda incógnita / cateto b / certo, conferido
    RED  coral   erro, caso descartado
    WHITE, INK2  texto e texto secundário · BG0, BG1, BG2 fundo azul-noite (gradiente + papel quadriculado ciano)
A legenda converte a fala em notação: números por extenso → algarismos (0 a 999, pt e en), "ao quadrado"/"squared" → ²,
"mais" → +, "raiz de 26" → √26. Termos próprios do vídeo: matematica.NUMEROS_EXTRA[:] = [("noventa graus", "90°")] no visual.py."""
import math
from functools import lru_cache
import skia
import idioma
import motor
from motor import *  # noqa
from tech import blur_paint, glow_text, hash01  # noqa

BG0, BG1, BG2 = "#0A0F1C", "#111A2E", "#1A2744"
WHITE, INK2 = "#FFFFFF", "#A9B6D3"
AMB = "#FFB020"
CYA = "#4CC9F0"
MNT = "#33D6A6"
RED = "#FF5470"
LX, RX = 520, 1380                           # centro da figura (esquerda) e do quadro (direita)
BX0, BX1, BY0, BY1 = 930, 1830, 175, 905     # quadro
CAP_Y = 1000                                 # legenda


def fade(t, t0, t1, d=0.3, d_out=0.25):
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))


def pop(t, t0, d=0.3):
    return ease_back(clamp((t - t0) / d)) if t >= t0 else 0.0


def pill(c, s, cx, cy, size, bg, fg, a, peso="black"):
    if a <= 0:
        return
    w = text_w(s, peso, size) + size * 1.2
    h = size * 1.8
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(r, blur_paint(bg, 0.35 * a, 16))
    c.drawRRect(r, paint(bg, a))
    text_mid(c, s, cx, cy, size, peso, fg, a)


def popill(c, s, cx, cy, size, bg, fg, a, t, t0):
    k = pop(t, t0, 0.35)
    if a * k <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(k, k)
    pill(c, s, 0, 0, size, bg, fg, a)
    c.restore()


def label(c, s, x, y, a, size=34, col=INK2, peso="semibold", align="center"):
    if a > 0:
        text_mid(c, s, x, y, size, peso, col, ease_out(clamp(a)), align=align)


def eq(c, parts, cy, a, size=64, cx=RX, peso="black", box=None, k=1.0, maxw=840):
    """equação em uma linha, centrada: parts = [(texto, cor), ...]; box = caixa de destaque; devolve [(x0, x1)] de cada parte"""
    if a <= 0:
        return []
    f = ease_out(clamp(a))
    tot = sum(text_w(s, peso, size) for s, _ in parts)
    while tot > maxw:
        size -= 2
        tot = sum(text_w(s, peso, size) for s, _ in parts)
    x = cx - tot / 2
    yy = cy + (1 - f) * 18
    c.save(); c.translate(cx, yy); c.scale(k, k); c.translate(-cx, -yy)
    if box:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 26, yy - size * 0.78, tot + 52, size * 1.34), 18, 18)
        c.drawRRect(r, blur_paint(box, 0.3 * f, 22))
        c.drawRRect(r, paint(BG1, 0.95 * f))
        c.drawRRect(r, paint(box, f, stroke=4))
    pos = []
    for s, col in parts:
        w = text_w(s, peso, size)
        text(c, s, x, yy + size * 0.36, size, peso, col, f, align="left")
        pos.append((x, x + w))
        x += w
    c.restore()
    return pos


def strike(c, x0, x1, y, a, u, col=RED):
    if a > 0 and u > 0:
        c.drawLine(x0, y + 8, x0 + (x1 - x0) * u, y - 8, paint(col, a, stroke=6, cap_round=True))


def check(c, cx, cy, r, a, col=MNT):
    if a <= 0:
        return
    k = ease_back(clamp(a))
    c.drawCircle(cx, cy, r * k, paint(col, a))
    p = skia.Path(); p.moveTo(cx - r * 0.45, cy + r * 0.02); p.lineTo(cx - r * 0.12, cy + r * 0.34); p.lineTo(cx + r * 0.5, cy - r * 0.32)
    c.drawPath(p, paint(BG0, a, stroke=r * 0.2, cap_round=True))


def cross(c, cx, cy, r, a, col=RED):
    if a <= 0:
        return
    k = ease_back(clamp(a))
    c.drawCircle(cx, cy, r * k, paint(col, a))
    d = r * 0.36
    c.drawLine(cx - d, cy - d, cx + d, cy + d, paint(BG0, a, stroke=r * 0.2, cap_round=True))
    c.drawLine(cx - d, cy + d, cx + d, cy - d, paint(BG0, a, stroke=r * 0.2, cap_round=True))


def board(c, a, x0=BX0, x1=BX1):
    """quadro das contas (direita)"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, BY0, x1, BY1), 26, 26)
    c.drawRRect(r, paint(BG2, 0.55 * a))
    c.drawRRect(r, paint(CYA, 0.18 * a, stroke=2))


def header(c, s, a):
    if a > 0:
        text_mid(c, s, 960, 66, 34, "black", AMB, a, tracking=2)


# ---------------------------------------------------------------- figuras
def tri(c, x0, y0, wb, hc, a, t, lab_a="a", lab_b="b", lab_c="c", size=48, hl=(), sub=None, draw=1.0, ang=None):
    """triângulo retângulo com o ângulo reto em (x0, y0): cateto c vertical (âmbar), cateto b na base (menta), hipotenusa a (ciano).
    hl: lados/ângulo em destaque ('a','b','c','ang'); sub: rótulos pequenos {'a': 'hipotenusa', ...}; ang: texto no ângulo reto"""
    if a <= 0:
        return
    sub = sub or {}
    A, B, Cc = (x0, y0), (x0 + wb, y0), (x0, y0 - hc)
    fill = skia.Path(); fill.moveTo(*A); fill.lineTo(*B); fill.lineTo(*Cc); fill.close()
    c.drawPath(fill, paint(CYA, 0.07 * a))
    pul = 0.5 + 0.5 * math.sin(t * 6)

    def seg(p, q, col, u, key):
        if u <= 0:
            return
        e = (p[0] + (q[0] - p[0]) * u, p[1] + (q[1] - p[1]) * u)
        on = key in hl
        c.drawLine(*p, *e, blur_paint(col, (0.5 + (0.6 * pul if on else 0)) * a, 20 if on else 10, stroke=18 if on else 10))
        c.drawLine(*p, *e, paint(col, a, stroke=14 if on else 10, cap_round=True))
    seg(A, Cc, AMB, clamp(draw * 3), "c")
    seg(A, B, MNT, clamp(draw * 3 - 1), "b")
    seg(Cc, B, CYA, clamp(draw * 3 - 2), "a")
    q = 36
    kq = clamp(draw * 3 - 1)
    if "ang" in hl:
        c.drawRect(skia.Rect.MakeXYWH(x0, y0 - q, q, q), paint(AMB, (0.25 + 0.3 * pul) * a * kq))
    c.drawRect(skia.Rect.MakeXYWH(x0, y0 - q, q, q), paint(WHITE, 0.85 * a * kq, stroke=4))
    if ang:
        text_mid(c, ang, x0 + q + 46, y0 - q - 26, 32, "black", AMB, a)
    ka = a * clamp(draw * 3 - 2)
    if ka <= 0:
        return
    if lab_c:
        text_mid(c, lab_c, x0 - 22, y0 - hc / 2, size, "black", AMB, ka, align="right")
        if "c" in sub:
            text_mid(c, sub["c"], x0 - 22, y0 - hc / 2 + size * 0.85, size * 0.5, "semibold", INK2, ka, align="right")
    if lab_b:
        text_mid(c, lab_b, x0 + wb / 2, y0 + size * 0.85, size, "black", MNT, ka)
        if "b" in sub:
            text_mid(c, sub["b"], x0 + wb / 2, y0 + size * 1.65, size * 0.5, "semibold", INK2, ka)
    if lab_a:
        nl = math.hypot(hc, wb) or 1
        off = 26 + size * 0.6
        mx, my = x0 + wb / 2 + hc / nl * off, y0 - hc / 2 - wb / nl * off
        c.save(); c.translate(mx, my); c.rotate(math.degrees(math.atan2(hc, wb)))   # paralelo à hipotenusa
        text_mid(c, lab_a, 0, 0, size, "black", CYA, ka)
        if "a" in sub:
            text_mid(c, sub["a"], 0, -size * 0.85, size * 0.5, "semibold", INK2, ka)
        c.restore()


def quadrados(c, a, t, A=420, Bq=240, u=0.0, lab=("a", "b"), show_b=1.0, cx=LX, cy=540):
    """prova geométrica: a² sem o canto b² (forma em L); com u → 1 o pedaço de cima gira e vira o retângulo (a + b) × (a − b)"""
    if a <= 0:
        return
    la, lb = lab
    x0 = cx - (A + Bq * u) / 2
    y0 = cy - A / 2 + (Bq / 2) * u
    R1 = skia.Rect.MakeXYWH(x0, y0 + Bq, A, A - Bq)                 # faixa de baixo: a × (a − b)
    w2, h2 = A - Bq, Bq                                               # pedaço de cima: (a − b) × b
    k = ease_io(clamp(u))
    px, py = x0 + A * k, y0 + Bq * k                                  # vai para a direita do R1
    c.drawRect(R1, paint(CYA, 0.28 * a)); c.drawRect(R1, paint(CYA, a, stroke=4))
    c.save(); c.translate(px, py); c.rotate(90 * k); c.translate(0, -h2 * k)
    c.drawRect(skia.Rect.MakeXYWH(0, 0, w2, h2), paint(CYA, 0.28 * a))
    c.drawRect(skia.Rect.MakeXYWH(0, 0, w2, h2), paint(CYA, a, stroke=4))
    c.restore()
    if u <= 0.02:
        sb = show_b * a
        if sb > 0:   # o quadrado b² retirado, tracejado
            p = paint(MNT, sb, stroke=4)
            p.setPathEffect(skia.DashPathEffect.Make([14, 10], t * 30 % 24))
            c.drawRect(skia.Rect.MakeXYWH(x0 + A - Bq, y0, Bq, Bq), p)
            text_mid(c, f"{lb}²", x0 + A - Bq / 2, y0 + Bq / 2, 52, "black", MNT, sb)
        text_mid(c, f"{la}² − {lb}²", x0 + (A - Bq) / 2 + 10, y0 + Bq + (A - Bq) / 2, 48, "black", WHITE, a)
        text_mid(c, la, x0 + A / 2, y0 + A + 40, 46, "black", CYA, a)
        text_mid(c, la, x0 - 30, y0 + A / 2, 46, "black", CYA, a, align="right")
        text_mid(c, lb, x0 + A + 28, y0 + Bq / 2, 42, "black", MNT, a * show_b, align="left")
    ku = a * ep(u, 0.92, 0.08) if u > 0 else 0
    if ku > 0:   # retângulo final
        tw = A + Bq
        text_mid(c, f"({la} + {lb})", x0 + tw / 2, y0 + A + 40, 46, "black", CYA, ku)
        text_mid(c, f"({la} − {lb})", x0 - 24, y0 + Bq + (A - Bq) / 2, 44, "black", MNT, ku, align="right")


def selo(c, s, t=0):
    """selo do canto (ex.: "QUESTÃO DE MATEMÁTICA · 001")"""
    w = text_w(s, "extrabold", 18) + 22
    pill(c, s, 52 + w / 2, 66, 18, AMB, BG0, 0.95, "extrabold")


def cartao(c, x, y, w, h, a, cor=CYA, rot=None):
    """cartão arredondado com borda colorida (ex.: aula indicada); rot = etiqueta no topo"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24)
    c.drawRRect(r, blur_paint(cor, 0.25 * a, 22))
    c.drawRRect(r, paint(BG1, 0.96 * a))
    c.drawRRect(r, paint(cor, a, stroke=4))
    if rot:
        tw = text_w(rot, "extrabold", 22) + 30
        pill(c, rot, x + 28 + tw / 2, y, 22, cor, BG0, a, "extrabold")


# ---------------------------------------------------------------- fundo
@lru_cache(None)
def _bg():
    s = skia.Surface(W, H); c = s.getCanvas()
    p = skia.Paint()
    p.setShader(skia.GradientShader.MakeRadial(center=(W * 0.5, H * 0.45), radius=W * 0.75,
                                               colors=[hexc(BG2), hexc(BG1), hexc(BG0)], positions=[0, 0.5, 1]))
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    fino, grosso = paint(CYA, 0.04, stroke=1.2), paint(CYA, 0.08, stroke=1.6)
    for i, x in enumerate(range(0, W + 1, 48)):
        c.drawLine(x, 0, x, H, grosso if i % 5 == 0 else fino)
    for i, y in enumerate(range(0, H + 1, 48)):
        c.drawLine(0, y, W, y, grosso if i % 5 == 0 else fino)
    return s.makeImageSnapshot()


SIMBOLOS = "π √ ∑ ∞ ² Δ θ ÷ × ±".split()


def BACKGROUND(c, t):
    c.drawImage(_bg(), 0, 0)
    for i in range(14):
        x = hash01(i, 1) * W + math.sin(t * 0.4 + i) * 14
        y = H - ((hash01(i, 3) * H + t * (8 + 14 * hash01(i, 5))) % (H + 80))
        text_mid(c, SIMBOLOS[i % len(SIMBOLOS)], x, y, 36 + 36 * hash01(i, 7), "black", WHITE, 0.03 + 0.04 * hash01(i, 9))


# ---------------------------------------------------------------- legenda karaokê com notação matemática
PUNCT = ".,:;?!"
NUMEROS_EXTRA = []   # no visual.py: matematica.NUMEROS_EXTRA[:] = [("noventa graus", "90°"), ...] (vem antes dos números)


def _extenso_pt(n):
    U = "zero um dois três quatro cinco seis sete oito nove dez onze doze treze catorze quinze dezesseis dezessete dezoito dezenove".split()
    D = "_ _ vinte trinta quarenta cinquenta sessenta setenta oitenta noventa".split()
    C = "_ cento duzentos trezentos quatrocentos quinhentos seiscentos setecentos oitocentos novecentos".split()
    if n < 20:
        return U[n]
    if n < 100:
        return D[n // 10] + ("" if n % 10 == 0 else " e " + U[n % 10])
    if n == 100:
        return "cem"
    return C[n // 100] + ("" if n % 100 == 0 else " e " + _extenso_pt(n % 100))


def _extenso_en(n):
    U = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen "
         "eighteen nineteen").split()
    D = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
    if n < 20:
        return U[n]
    if n < 100:
        return D[n // 10] + ("" if n % 10 == 0 else "-" + U[n % 10])
    return U[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + _extenso_en(n % 100))


@lru_cache(None)
def _lingua(lang):
    """(números + operadores em ordem de busca, palavras do 'ao quadrado', um, dois, vezes)"""
    if lang == "en":
        nums = [(_extenso_en(n), str(n)) for n in range(1000) if n not in (1, 2)]
        nums += [("a hundred", "100"), ("one thousand", "1000"), ("a thousand", "1000")]
        ops = [("the square root of", "√"), ("square root of", "√"), ("x y", "xy"), ("is equal to", "="),
               ("equals", "="), ("plus", "+"), ("minus", "−"), ("times", "×")]
        esp = (["squared"], ("one",), ("two",), ("times",))
    else:
        nums = [(_extenso_pt(n), str(n)) for n in range(1000) if n not in (1, 2)]
        nums += [("quatorze", "14"), ("mil", "1000")]
        ops = [("raiz de", "√"), ("x y", "xy"), ("é igual a", "="), ("igual a", "="), ("mais", "+"),
               ("menos", "−"), ("vezes", "×")]
        esp = (["ao", "quadrado"], ("um",), ("dois",), ("vezes",))
    nums.sort(key=lambda p: (-len(p[0].split()), -len(p[0])))   # "vinte e cinco" antes de "vinte" e de "cinco"
    return (nums + ops,) + esp


EXPRESSOES = {("do", "zero"), ("from", "zero")}   # "aprender do zero": não vira algarismo


def _limpo(s):
    return s.lower().replace("*", "").rstrip(PUNCT)


def _num(tokens):
    """legenda em notação: números por extenso → algarismos, 'ao quadrado' → ², 'mais' → +, 'raiz de 26' → √26"""
    numeros, QUAD, UM, DOIS, VEZES = _lingua(idioma.LANG)
    numeros = list(NUMEROS_EXTRA) + numeros
    por_palavra = {}
    for frase, dig in numeros:
        por_palavra.setdefault(frase.split()[0], []).append((frase, dig))
    out, i = [], 0
    while i < len(tokens):
        g = tokens[i:i + len(QUAD)]
        if out and len(g) == len(QUAD) and [_limpo(x["disp"]) for x in g] == QUAD:
            fim = g[-1]["disp"].replace("*", "")
            out[-1] = dict(out[-1], disp=out[-1]["disp"].replace("*", "").rstrip(PUNCT) + "²" + fim[len(fim.rstrip(PUNCT)):],
                           t1=g[-1]["t1"])
            i += len(QUAD); continue
        tk = tokens[i]
        w = _limpo(tk["disp"])
        nxt = _limpo(tokens[i + 1]["disp"]) if i + 1 < len(tokens) else ""
        d = tk["disp"].replace("*", "")
        if w in UM and (d[-1:] in PUNCT or nxt in VEZES):
            out.append(dict(tk, disp="1" + d[len(w):])); i += 1; continue
        if w in DOIS and nxt == "a":
            fim = tokens[i + 1]["disp"].replace("*", "")
            out.append(dict(tk, disp="2a" + fim[1:], t1=tokens[i + 1]["t1"])); i += 2; continue
        antes = _limpo(tokens[i - 1]["disp"]) if i else ""
        for frase, dig in () if (antes, w) in EXPRESSOES else por_palavra.get(w, ()):
            n = len(frase.split())
            gg = tokens[i:i + n]
            txt = " ".join(x["disp"] for x in gg).replace("*", "")
            if len(gg) == n and txt.lower().rstrip(PUNCT) == frase:
                out.append(dict(disp=dig + txt[len(txt.rstrip(PUNCT)):], bold=any(x["bold"] for x in gg), t0=gg[0]["t0"], t1=gg[-1]["t1"]))
                i += n
                break
        else:
            out.append(dict(tk, disp=d)); i += 1
    res = []   # √ gruda no número seguinte
    for tk in out:
        if res and res[-1]["disp"] == "√":
            res[-1] = dict(tk, disp="√" + tk["disp"], t0=res[-1]["t0"])
        else:
            res.append(tk)
    return res


def _chunks(tokens):
    out, cur = [], []
    for tk in _num(tokens):
        cur.append(tk)
        end = tk["disp"][-1:] in PUNCT
        if len(cur) >= 7 or (end and len(cur) >= 2) or sum(len(x["disp"]) + 1 for x in cur) > 40:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def CAPTION(c, scene, t):
    """legenda de aula: até 7 palavras numa faixa escura; palavra falada em âmbar; destaque *x* em ciano"""
    lt = t - scene["start"]
    chunks = scene.setdefault("_ch", _chunks(scene["tokens"]))
    for i, ch in enumerate(chunks):
        s = ch[0]["t0"] - 0.06
        e = chunks[i + 1][0]["t0"] - 0.06 if i + 1 < len(chunks) else scene["dur"] - 0.05
        if s <= lt < e:
            break
    else:
        return
    words = [tk["disp"] for tk in ch]
    size, sp = 46, 14
    while sum(text_w(wd, "extrabold", size) for wd in words) + sp * (len(words) - 1) > 1500:
        size -= 2
    tot = sum(text_w(wd, "extrabold", size) for wd in words) + sp * (len(words) - 1)
    k = ease_out(clamp((lt - s) / 0.14))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(960 - tot / 2 - 28, CAP_Y - size * 0.9, tot + 56, size * 1.8), 18, 18)
    c.drawRRect(r, paint(BG0, 0.72 * k))
    x = 960 - tot / 2
    f = motor.font("extrabold", size)
    for tk, wd in zip(ch, words):
        falando = tk["t0"] - 0.05 <= lt < tk["t1"] + 0.2
        col = AMB if falando else (CYA if tk["bold"] else WHITE)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, paint(col, k))
        x += text_w(wd, "extrabold", size) + sp
