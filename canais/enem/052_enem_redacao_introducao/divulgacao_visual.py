"""Visual da divulgação da série Introdução da Redação (Redação ENEM) — compartilhado pelo Short (1080x1920, render.py
--vertical) e pelo horizontal (1920x1080). Cada projeto tem um visual.py curto que chama setup(PROJ) e define SOM/ARQUIVO.
Mesmo mundo da divulgação da série 014 (Leitura da Proposta): folha de redação sobre azul-noite, carimbo vermelho,
legenda grande palavra a palavra. Gancho = o começo clichê "Desde os primórdios da humanidade" riscado no 1º segundo.
Cores com função: azul = tema/mapa · verde = certo · amarelo = destaque · vermelho = erro · laranja = tese · teal = lista."""
import json
import math
from functools import lru_cache
from pathlib import Path
import skia
import motor
import tech
from motor import W, H, paint, text, text_mid, text_w, ep, prog, ease_out, ease_back, ease_io, clamp, lerp  # noqa
from tech import blur_paint, glow_text, hash01  # noqa

SERIE = Path(__file__).resolve().parent
S014 = SERIE.parent / "014_enem_redacao_leitura_proposta"
VERT = H > W
CX = W / 2
NAVY, NAVY2 = "#0A1430", "#16285A"
PAPER, PAPER_LN = "#FBF8F1", "#CBD7EE"
WHITE, INK, INK2, MUT = "#FFFFFF", "#18213A", "#B9C6E4", "#6B7591"
YEL, RED, GREEN, SKY, BLUE = "#FFD23F", "#FF4D5A", "#2BD47D", "#7CC4FF", "#3B6CF6"
ORANGE, TEAL, PEN = "#FF7A3D", "#22C3B5", "#1F3A93"
ENTRADA_SECA = True
MARCA = ""
SAMP = skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear)

# núcleo do título de cada episódio (antes do " | Introdução da Redação Ep. N")
EPISODIOS = ["As 3 perguntas que o 1º parágrafo precisa responder",
             "Desde os primórdios? 4 jeitos melhores de começar",
             "Sua citação de filósofo pode ser apagada? O teste da retirada",
             "Opinião não é tese: a tese e a antecipação",
             "Aristóteles na introdução? 3 versões, só 1 funciona",
             "Escreva uma introdução comigo, do zero, em 6 passos",
             "10 pegadinhas do 1º parágrafo: você cai?"]
CLICHE = ["Desde os primórdios da", "humanidade, a sociedade", "enfrenta diversos desafios..."]
# temas reais do ENEM (neutros) para mostrar que o clichê cabe em qualquer um
TEMAS = [("ENEM 2018", "Manipulação do comportamento do usuário pelo controle de dados na internet"),
         ("ENEM 2019", "Democratização do acesso ao cinema no Brasil"),
         ("ENEM 2021", "Invisibilidade e registro civil: garantia de acesso à cidadania no Brasil")]
PALAVRAS = {}   # (cena, palavra normalizada) -> instante absoluto da 1ª ocorrência
FLASH = []
CORTES = ("02", "03", "04") + (("05",) if VERT else ("12", "13"))


def setup(proj):
    t = json.loads((Path(proj) / "audio" / "tempos.json").read_text(encoding="utf-8"))
    for s in t["scenes"]:
        for tk in s["tokens"]:
            k = (s["id"], tk["disp"].lower().strip(".,:;!?*"))
            PALAVRAS.setdefault(k, s["start"] + tk["t0"])
    FLASH[:] = [s["start"] - 0.05 for s in t["scenes"][1:] if s["id"] in CORTES]


def w_at(cena, palavra, padrao):
    return PALAVRAS.get((cena, palavra), padrao)


@lru_cache(None)
def _img(path):
    return skia.Image.open(str(path))


def capa(i):
    """capa A do episódio i (0–6) da série; i = 'p' → capa do ep. 1 da série Leitura da Proposta"""
    if i == "p":
        return _img(next((sorted(S014.glob("ep1*"))[0] / "youtube").glob("capa_A*.jpg")))
    return _img(next((sorted(SERIE.glob("ep*"))[i] / "youtube").glob("capa_A*.jpg")))


def fade(t, t0, t1, d=0.3, d_out=0.25):
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))


def shake(t, t0, amp=14, d=0.3):
    u = prog(t, t0, d)
    if u <= 0 or u >= 1:
        return 0.0, 0.0
    k = (1 - u) * amp
    return k * math.sin(t * 90), k * math.cos(t * 77)


def fit(s, peso, size, maxw):
    while text_w(s, peso, size) > maxw and size > 10:
        size -= 2
    return size


def big(c, s, cx, y, a, size, col=WHITE, maxw=None, peso="black", glow=0.10):
    if a <= 0:
        return
    size = fit(s, peso, size, maxw or W - 120)
    glow_text(c, s, cx, y + (1 - ease_out(clamp(a))) * 26, size, peso, col, clamp(a), glow=glow)


def pill(c, s, cx, cy, size, bg, fg, a, peso="black"):
    if a <= 0:
        return
    w = text_w(s, peso, size) + size * 1.2
    h = size * 1.8
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(r, blur_paint(bg, 0.4 * a, 18))
    c.drawRRect(r, paint(bg, a))
    text_mid(c, s, cx, cy, size, peso, fg, a)


def marca_texto(c, s, cx, y, size, a, col=YEL, fg=NAVY, peso="black", k=1.0):
    """palavra com marca-texto passando (k = quanto do marca-texto já passou)"""
    if a <= 0:
        return
    size = fit(s, peso, size, W - 140)
    w = text_w(s, peso, size)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 - 16, y - size * 0.86, (w + 32) * clamp(k), size * 1.16), 10, 10),
                paint(col, a))
    text(c, s, cx, y, size, peso, fg if k > 0.5 else WHITE, a)


def cover(c, i, x, y, w, h, a, r=18, borda=None):
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r)
    c.drawRRect(rr, blur_paint("#000000", 0.45 * a, 24))
    c.save(); c.clipRRect(rr, True)
    p = skia.Paint(AntiAlias=True); p.setAlphaf(clamp(a))
    c.drawImageRect(capa(i), skia.Rect.MakeXYWH(x, y, w, h), SAMP, p)
    c.restore()
    if borda:
        c.drawRRect(rr, paint(borda, a, stroke=5))


# ---------------------------------------------------------------- letra manuscrita (Caveat, como nas aulas)
@lru_cache(None)
def _hfont(size):
    tf = skia.Typeface.MakeFromFile(str(Path(motor.__file__).parent / "fontes" / "Caveat-Medium.ttf"))
    return skia.Font(tf, size)


def hand(c, s, x, y, size, col, a, reveal=1.0):
    if a <= 0 or reveal <= 0:
        return 0
    s = s[:max(0, int(round(len(s) * clamp(reveal))))]
    c.drawString(s, x, y, _hfont(size), paint(col, a))
    return _hfont(size).measureText(s)


def hand_w(s, size):
    return _hfont(size).measureText(s)


# ---------------------------------------------------------------- a folha de redação
def folha(c, cx, cy, w, h, a, rot=0.0, n=14, titulo=True):
    """folha de redação: cabeçalho, margem vermelha, linhas numeradas. Devolve a geometria (coordenadas locais)."""
    if a <= 0:
        return None
    c.save(); c.translate(cx, cy); c.rotate(rot); c.translate(-w / 2, -h / 2)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeWH(w, h), 14, 14)
    c.drawRRect(rr, blur_paint("#000000", 0.5 * a, 30))
    c.drawRRect(rr, paint(PAPER, a))
    top = 0.13 * h if titulo else 0.06 * h
    if titulo:
        text(c, "REDAÇÃO", 40, top * 0.62, h * 0.04, "black", INK, a, align="left")
        text(c, "ENEM", w - 40, top * 0.62, h * 0.03, "extrabold", BLUE, a, align="right")
    lh = (h - top - 0.05 * h) / n
    mx = 70
    c.drawLine(mx, top - 6, mx, h - 20, paint(RED, 0.55 * a, stroke=2.5))
    for i in range(n):
        y = top + (i + 1) * lh
        c.drawLine(24, y, w - 24, y, paint(PAPER_LN, a, stroke=2))
        text(c, str(i + 1), mx - 14, y - lh * 0.22, lh * 0.36, "semibold", MUT, a * 0.8, align="right")
    return dict(top=top, lh=lh, mx=mx, w=w, h=h)   # o chamador faz c.restore()


def carimbo(c, s, sub, cx, cy, size, col, a, t, t0, rot=-0.18):
    """carimbo que bate: escala 1.7 → 1 em 0.18 s, com aro"""
    if t < t0 or a <= 0:
        return
    u = clamp((t - t0) / 0.18)
    sc = lerp(1.7, 1.0, ease_out(u))
    aa = a * clamp(u * 2)
    c.save(); c.translate(cx, cy); c.rotate(math.degrees(rot)); c.scale(sc, sc)
    tw = max(text_w(s, "black", size), text_w(sub, "black", size * 0.3) if sub else 0)
    w, h = tw + size * 0.7, size * (1.25 if sub else 1.05)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), size * 0.16, size * 0.16)
    c.drawRRect(rr, paint(col, aa * 0.12))
    c.drawRRect(rr, paint(col, aa, stroke=size * 0.07))
    text(c, s, 0, (size * 0.30 if not sub else size * 0.18), size, "black", col, aa)
    if sub:
        text(c, sub, 0, h / 2 - size * 0.12, size * 0.26, "black", col, aa)
    c.restore()


def check(c, cx, cy, r, a, ok=True):
    if a <= 0:
        return
    col = GREEN if ok else RED
    c.drawCircle(cx, cy, r, paint(col, a))
    p = paint(WHITE, a, stroke=r * 0.28, cap_round=True)
    k = ease_out(clamp(a))
    if ok:
        pth = skia.Path(); pth.moveTo(cx - r * 0.45, cy + r * 0.02); pth.lineTo(cx - r * 0.1, cy + r * 0.38); pth.lineTo(cx + r * 0.5, cy - r * 0.35)
        c.drawPath(pth, p)
    else:
        d = r * 0.38 * k
        c.drawLine(cx - d, cy - d, cx + d, cy + d, p); c.drawLine(cx + d, cy - d, cx - d, cy + d, p)


# ícones das 3 peças (mapa, endereço/casa, lista da caixa), desenhados à mão em vetor
def icone(c, key, cx, cy, r, col, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(col, a))
    s = r * 0.5
    p = paint(WHITE, a, stroke=r * 0.1, cap_round=True)
    if key == "mapa":   # mapa dobrado em 3 faixas + alfinete
        pth = skia.Path()
        pts = [(-1, -0.75), (-0.33, -1), (0.33, -0.75), (1, -1), (1, 0.75), (0.33, 1), (-0.33, 0.75), (-1, 1)]
        pth.moveTo(cx + pts[0][0] * s, cy + pts[0][1] * s)
        for x, y in pts[1:]:
            pth.lineTo(cx + x * s, cy + y * s)
        pth.close(); c.drawPath(pth, p)
        c.drawLine(cx - 0.33 * s, cy - s, cx - 0.33 * s, cy + 0.75 * s, p); c.drawLine(cx + 0.33 * s, cy - 0.75 * s, cx + 0.33 * s, cy + s, p)
    elif key == "casa":
        pth = skia.Path(); pth.moveTo(cx - s, cy - 0.05 * s); pth.lineTo(cx, cy - s); pth.lineTo(cx + s, cy - 0.05 * s)
        c.drawPath(pth, p)
        c.drawRect(skia.Rect.MakeLTRB(cx - 0.72 * s, cy - 0.2 * s, cx + 0.72 * s, cy + 0.95 * s), p)
        c.drawRect(skia.Rect.MakeLTRB(cx - 0.22 * s, cy + 0.3 * s, cx + 0.22 * s, cy + 0.95 * s), p)
    else:   # caixa com lista
        c.drawRect(skia.Rect.MakeLTRB(cx - s, cy - 0.85 * s, cx + s, cy + 0.9 * s), p)
        c.drawLine(cx - s, cy - 0.35 * s, cx + s, cy - 0.35 * s, p)
        for k in range(2):
            y = cy + 0.05 * s + k * 0.45 * s
            c.drawCircle(cx - 0.55 * s, y, r * 0.05, paint(WHITE, a))
            c.drawLine(cx - 0.3 * s, y, cx + 0.6 * s, y, p)


# ---------------------------------------------------------------- fundo, legenda e selo
@lru_cache(None)
def _bg():
    s = skia.Surface(W, H); c = s.getCanvas()
    p = skia.Paint(Shader=skia.GradientShader.MakeLinear([(0, 0), (W * 0.3, H)], [motor.hexc(NAVY), motor.hexc(NAVY2)]))
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    for y in range(0, H, 64):   # pauta de caderno, bem apagada
        c.drawLine(0, y, W, y, paint("#FFFFFF", 0.035, stroke=2))
    c.drawCircle(W * 0.85, H * 0.15, max(W, H) * 0.35, blur_paint(BLUE, 0.16, 160))
    c.drawCircle(W * 0.1, H * 0.9, max(W, H) * 0.3, blur_paint("#7C5CFA", 0.10, 160))
    return s.makeImageSnapshot()


def BACKGROUND(c, t):
    c.drawImage(_bg(), 0, 0)
    for i in range(22):
        x = hash01(i, 1) * W + math.sin(t * 0.5 + i) * 10
        y = H - ((hash01(i, 3) * H + t * (12 + 26 * hash01(i, 5))) % (H + 40))
        c.drawCircle(x, y, 1.5 + 2.5 * hash01(i, 7), paint(YEL if i % 4 == 0 else WHITE, 0.08 + 0.16 * hash01(i, 9)))


CAP_Y = 1470 if VERT else 1000
CAP_SIZE = 84 if VERT else 58
CAP_MAXW = 960 if VERT else 1500


def _chunks(tokens):
    out, cur = [], []
    lim = 3 if VERT else 5
    for tk in tokens:
        cur.append(tk)
        end = tk["disp"].rstrip()[-1:] in ".,:?!;"
        if len(cur) >= lim or end or sum(len(x["disp"]) + 1 for x in cur) > (18 if VERT else 30):
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def CAPTION(c, scene, t):
    """legenda de redes sociais: poucas palavras, grandes, com contorno; palavra falada em amarelo, destaque em azul"""
    lt = t - scene["start"]
    chunks = scene.setdefault("_ch", _chunks(scene["tokens"]))
    for i, ch in enumerate(chunks):
        s = ch[0]["t0"] - 0.06
        e = chunks[i + 1][0]["t0"] - 0.06 if i + 1 < len(chunks) else scene["dur"] - 0.05
        if s <= lt < e or (i == 0 and lt < s and scene["id"] == "01"):   # 1º quadro do vídeo já com legenda
            break
    else:
        return
    words = [tk["disp"].upper() for tk in ch]
    size, sp = CAP_SIZE, CAP_SIZE * 0.27
    while sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1) > CAP_MAXW:
        size -= 3
    tot = sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1)
    pop = 1.0 if scene["id"] == "01" and lt < 0.2 else ease_back(clamp((lt - s) / 0.16))
    x = CX - tot / 2
    c.save(); c.translate(CX, CAP_Y); c.scale(0.86 + 0.14 * pop, 0.86 + 0.14 * pop); c.translate(-CX, -CAP_Y)
    f = motor.font("black", size)
    for tk, wd in zip(ch, words):
        falando = tk["t0"] - 0.05 <= lt < tk["t1"] + 0.25
        col = YEL if falando else (SKY if tk["bold"] else WHITE)
        st = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.17, Color=skia.Color(4, 10, 28))
        st.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, st)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, paint(col, 1.0))
        x += text_w(wd, "black", size) + sp
    c.restore()


def OVERLAY(c, t):
    if VERT:
        pill(c, "REDAÇÃO ENEM · INTRODUÇÃO", CX, 150, 26, YEL, NAVY, 0.95, "extrabold")
    else:
        pill(c, "REDAÇÃO ENEM · INTRODUÇÃO", 250, 62, 20, YEL, NAVY, 0.95, "extrabold")
    for t0 in FLASH:   # corte seco com clarão nas viradas
        u = (t - t0) / 0.16
        if 0 <= u < 1:
            c.drawRect(skia.Rect.MakeWH(W, H), paint(WHITE, 0.28 * (1 - u)))


# ---------------------------------------------------------------- blocos
def b_gancho(c, t, C, B):
    """1º quadro: a folha já com o clichê escrito e a pergunta; em "pare" o carimbo bate e risca tudo"""
    a = 1 - prog(t, B["end"] - 0.1, 0.2)
    t_pare = w_at("01", "pare", C["01.b"] + 0.05)
    if VERT:
        big(c, "SUA REDAÇÃO", CX, 310, a, 112, WHITE)
        big(c, "COMEÇA ASSIM?", CX, 430, a, 112, YEL)
        fx, fy, fw, fh, hs, n = CX, 880, 980, 760, 82, 7
    else:
        big(c, "SUA REDAÇÃO", 560, 200, a, 92, WHITE, maxw=900)
        big(c, "COMEÇA ASSIM?", 560, 300, a, 92, YEL, maxw=900)
        fx, fy, fw, fh, hs, n = 560, 640, 900, 560, 70, 6
    dx, dy = shake(t, t_pare, 16)
    g = folha(c, fx + dx * 0.3, fy + dy * 0.3, fw, fh, a, rot=-1.5, n=n)
    if g:
        risco = ease_out(clamp((t - t_pare - 0.1) / 0.35))
        for j, ln in enumerate(CLICHE):
            y = g["top"] + (j + 1) * g["lh"] - g["lh"] * 0.18
            ww = hand(c, ln, g["mx"] + 20, y, hs, PEN, a)
            if risco > 0:
                k = clamp(risco * 3 - j)
                c.drawLine(g["mx"] + 10, y - hs * 0.25, g["mx"] + 10 + (ww + 20) * k, y - hs * 0.32, paint(RED, a, stroke=9, cap_round=True))
        c.restore()
    if VERT:
        carimbo(c, "PARE!", "", CX + dx, 1010 + dy, 210, RED, a, t, t_pare, rot=-0.14)
    else:
        carimbo(c, "PARE!", "", 1430 + dx, 560 + dy, 200, RED, a, t, t_pare, rot=-0.12)


def _cartao_tema(c, x, y, w, h, ano, tema, a, carimbo_k):
    """mini-folha: ano + tema no topo, e o MESMO clichê manuscrito embaixo"""
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18)
    c.drawRRect(rr, blur_paint("#000000", 0.4 * a, 20))
    c.drawRRect(rr, paint(PAPER, a))
    aw = text(c, ano, x + 28, y + 44, 26, "black", BLUE, a, align="left")
    # tema em até 2 linhas, ao lado do ano
    tx, tw, ts = x + 28 + aw + 18, w - aw - 74, 22
    ws, ls, cur = tema.split(), [], ""
    for wd in ws:
        if text_w((cur + " " + wd).strip(), "bold", ts) > tw:
            ls.append(cur); cur = wd
        else:
            cur = (cur + " " + wd).strip()
    ls.append(cur)
    for j, ln in enumerate(ls[:4]):
        text(c, ln, tx, y + 36 + j * 26, ts, "bold", INK, a, align="left")
    top = y + 36 + max(len(ls[:4]) - 1, 0) * 26 + 22
    c.drawLine(x + 20, top, x + w - 20, top, paint(PAPER_LN, a, stroke=2))
    frase = "Desde os primórdios da humanidade..."
    hs = min(h * 0.5, (h - (top - y)) * 0.62)
    while hand_w(frase, hs) > w - 60:
        hs -= 2
    hand(c, frase, x + 30, top + (y + h - top) / 2 + hs * 0.3, hs, PEN, a)
    if carimbo_k > 0:
        c.drawRRect(rr, paint(RED, a * carimbo_k, stroke=6))


def b_generico(c, t, C, B):
    a = ep(t, B["start"], 0.15) * (1 - prog(t, B["end"] - 0.1, 0.2))
    ta, tb = C["02.a"], C["02.b"]
    t_qual = w_at("02", "qualquer", ta + 1.0)
    t_nada = w_at("02", "nada", tb + 0.6)
    gen = ep(t, t_nada, 0.2)
    if VERT:
        big(c, "O MESMO COMEÇO", CX, 300, a, 84, WHITE)
        big(c, "EM QUALQUER TEMA", CX, 395, a * ep(t, t_qual - 0.1, 0.25), 84, YEL)
        for i, (ano, tema) in enumerate(TEMAS):
            k = ep(t, ta + 0.25 * i, 0.25) * a
            _cartao_tema(c, 70, 470 + i * 250 + (1 - ease_back(clamp(k))) * 50, 940, 210, ano, tema, k, gen)
        dx, dy = shake(t, t_nada, 14)
        carimbo(c, "GENÉRICO", "NÃO DIZ NADA SOBRE O TEMA", CX + dx, 1250 + dy, 150, RED, a, t, t_nada, rot=-0.07)
    else:
        big(c, "O MESMO COMEÇO EM QUALQUER TEMA", CX, 190, a * ep(t, t_qual - 0.1, 0.25), 70, YEL)
        for i, (ano, tema) in enumerate(TEMAS):
            k = ep(t, ta + 0.25 * i, 0.25) * a
            _cartao_tema(c, 110 + i * 580, 300 + (1 - ease_back(clamp(k))) * 50, 540, 300, ano, tema, k, gen)
        dx, dy = shake(t, t_nada, 14)
        carimbo(c, "GENÉRICO", "NÃO DIZ NADA SOBRE O TEMA", CX + dx, 780 + dy, 150, RED, a, t, t_nada, rot=-0.05)


PERGUNTAS = [("mapa", "De onde parte a discussão?", BLUE, "03.b"),
             ("casa", "O que você defende?", ORANGE, "03.c"),
             ("caixa", "Por quais caminhos vai provar?", TEAL, "03.d")]


def b_perguntas(c, t, C, B):
    a = ep(t, B["start"], 0.15) * (1 - prog(t, B["end"] - 0.1, 0.2))
    ta = C["03.a"]
    t3 = w_at("03", "três", ta + 1.2)
    if VERT:
        big(c, "UMA BOA INTRODUÇÃO", CX, 300, a, 76, WHITE)
        marca_texto(c, "RESPONDE 3 PERGUNTAS", CX, 410, 76, a * ep(t, t3 - 0.1, 0.2), k=ep(t, t3, 0.4))
        for i, (ic, q, col, cue) in enumerate(PERGUNTAS):
            k = ep(t, C[cue] - 0.1, 0.3) * a
            y = 560 + i * 270 + (1 - ease_back(clamp(k))) * 40
            rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(70, y, 940, 220), 28, 28)
            c.drawRRect(rr, paint("#FFFFFF", 0.96 * k))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(70, y, 16, 220), 8, 8), paint(col, k))
            icone(c, ic, 190, y + 110, 70, col, k)
            ls = q.split(" ", 2) if len(q) > 24 else [q]
            if len(ls) > 1:
                ls = [" ".join(ls[:2]), ls[2]]
            for j, ln in enumerate(ls):
                text(c, ln, 300, y + 110 + 22 - (len(ls) - 1) * 32 + j * 64, fit(ln, "black", 56, 680), "black", INK, k, align="left")
    else:
        big(c, "UMA BOA INTRODUÇÃO", 560, 180, a, 64, WHITE, maxw=900)
        marca_texto(c, "RESPONDE 3 PERGUNTAS", 1380, 180, 64, a * ep(t, t3 - 0.1, 0.2), k=ep(t, t3, 0.4))
        for i, (ic, q, col, cue) in enumerate(PERGUNTAS):
            k = ep(t, C[cue] - 0.1, 0.3) * a
            x = 110 + i * 580
            y = 300 + (1 - ease_back(clamp(k))) * 40
            rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 540, 470), 28, 28)
            c.drawRRect(rr, paint("#FFFFFF", 0.96 * k))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 540, 16), 8, 8), paint(col, k))
            icone(c, ic, x + 270, y + 140, 80, col, k)
            ws, ls, cur = q.split(), [], ""
            for wd in ws:
                if text_w((cur + " " + wd).strip(), "black", 46) > 460:
                    ls.append(cur); cur = wd
                else:
                    cur = (cur + " " + wd).strip()
            ls.append(cur)
            for j, ln in enumerate(ls):
                text(c, ln, x + 270, y + 300 + j * 58, 46, "black", INK, k)


def b_serie(c, t, C, B):   # Short: as 7 capas de uma vez
    a = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    ta = C["04.a"]
    big(c, "SÉRIE INTRODUÇÃO DA REDAÇÃO", CX, 270, a, 60, WHITE)
    big(c, "7 AULAS · DO ZERO", CX, 360, a * ep(t, C["04.b"], 0.25), 84, YEL)
    cw, ch, gx, gy = 400, 225, 36, 26
    x0, y0 = CX - cw - gx / 2, 410
    for i in range(7):
        k = ep(t, ta + 0.25 + 0.14 * i, 0.3) * a
        col, row = i % 2, i // 2
        x = x0 + col * (cw + gx) if i < 6 else CX - cw / 2
        y = y0 + row * (ch + gy) + (1 - ease_back(clamp(k))) * 60
        cover(c, i, x, y, cw, ch, k, r=14)


def b_intro(c, t, C, B):   # horizontal: nome da série + fileira de capas
    a = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    big(c, "SÉRIE", CX, 230, a, 50, INK2)
    marca_texto(c, "INTRODUÇÃO DA REDAÇÃO", CX, 380, 120, a, k=ep(t, C["04.a"] + 0.3, 0.5))
    big(c, "7 aulas para quem está começando", CX, 500, a * ep(t, C["04.b"], 0.3), 54, WHITE)
    cw, ch, gx = 232, 130, 20
    x0 = CX - (7 * cw + 6 * gx) / 2
    for i in range(7):
        k = ep(t, C["04.b"] + 0.1 * i, 0.3) * a
        cover(c, i, x0 + i * (cw + gx), 620 + (1 - ease_back(clamp(k))) * 50, cw, ch, k, r=12)


EPS_IDS = ["05", "06", "07", "08", "09", "10", "11"]


def b_eps(c, t, C, B):   # horizontal: um episódio por cena (05–11), capa grande + título
    k_atual = max((i for i, s in enumerate(EPS_IDS) if C[s] - 0.15 <= t), default=0)
    a_bl = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    t0 = C[EPS_IDS[k_atual]] - 0.15
    u = ease_out(clamp((t - t0) / 0.35))
    x, y, w, h = 120, 190, 960, 540
    if k_atual > 0 and u < 1:
        cover(c, k_atual - 1, x - 400 * u, y, w, h, a_bl * (1 - u), r=22)
    cover(c, k_atual, x + 300 * (1 - u), y, w, h, a_bl * u, r=22, borda=YEL)
    tx = 1160
    pill(c, f"EPISÓDIO {k_atual + 1}", tx + 120, 260, 30, YEL, NAVY, a_bl * u)
    palavras, linhas, cur = EPISODIOS[k_atual].split(), [], ""
    for p in palavras:
        if text_w((cur + " " + p).strip(), "black", 52) > 660:
            linhas.append(cur); cur = p
        else:
            cur = (cur + " " + p).strip()
    linhas.append(cur)
    for j, ln in enumerate(linhas[:4]):
        text(c, ln, tx, 380 + j * 66, 52, "black", WHITE, a_bl * ep(t, t0 + 0.1 + 0.06 * j, 0.3), align="left")
    for i in range(7):
        cx = tx + 30 + i * 64
        on = i <= k_atual
        c.drawCircle(cx, 700, 22 if i == k_atual else 16, paint(YEL if on else "#FFFFFF", a_bl * (1 if on else 0.25)))
        if on:
            text_mid(c, str(i + 1), cx, 700, 22 if i == k_atual else 16, "black", NAVY, a_bl)


def card_playlist(c, x, y, w, a, capa_i, nome, sub, destaque=True, rotulo="PLAYLIST"):
    if a <= 0:
        return
    h = w * 0.36
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 28, 28)
    c.drawRRect(rr, paint("#0B1C44", a))
    c.drawRRect(rr, paint(YEL if destaque else "#FFFFFF", a * (0.9 if destaque else 0.35), stroke=4))
    tw, th = h * 0.86 * 16 / 9, h * 0.86
    tx, ty = x + h * 0.07, y + h * 0.07
    for k in (2, 1):   # pilha de capas (é uma playlist)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(tx + 10 * k, ty - 8 * k, tw, th), 12, 12), paint("#FFFFFF", a * 0.15 * (3 - k)))
    cover(c, capa_i, tx, ty, tw, th, a, r=12)
    tl = x + h * 0.07 + tw + 34
    maxw = x + w - tl - 30
    text(c, rotulo, tl, y + h * 0.33, h * 0.11, "black", YEL if destaque else INK2, a, align="left")
    text(c, nome, tl, y + h * 0.56, fit(nome, "black", h * 0.17, maxw), "black", WHITE, a, align="left")
    text(c, sub, tl, y + h * 0.77, fit(sub, "semibold", h * 0.11, maxw), "semibold", INK2, a, align="left")


def b_anteriores(c, t, C, B):
    """a trilha da Redação: série 1 (Leitura da Proposta, já no canal) → série 2 (Introdução, a nova)"""
    a = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    cid = B_ANT
    tb = C[cid + ".b"]
    tc = C[cid + ".c"]
    k1 = ep(t, tb - 0.1, 0.35) * a
    k2 = ep(t, (tc if tc < 1e8 else tb + 0.9), 0.35) * a
    if VERT:
        big(c, "A TRILHA DA REDAÇÃO", CX, 300, a, 80, WHITE)
        pill(c, "1ª SÉRIE · COMECE POR AQUI", CX, 420, 30, GREEN, NAVY, k1)
        card_playlist(c, 80, 480, 920, k1, "p", "Leitura da Proposta", "6 aulas · ler o tema sem fugir dele", rotulo="SÉRIE")
        motor.arrow(c, CX, 830, CX, 930, YEL, k2, width=10, head=30, progress=k2)
        pill(c, "2ª SÉRIE · NOVA", CX, 990, 30, YEL, NAVY, k2)
        card_playlist(c, 80, 1050, 920, k2, 0, "Introdução da Redação", "7 aulas · o 1º parágrafo do zero", rotulo="SÉRIE")
    else:
        big(c, "A TRILHA DA REDAÇÃO", CX, 170, a, 70, WHITE)
        pill(c, "1ª SÉRIE · JÁ NO CANAL", 500, 290, 28, GREEN, NAVY, k1)
        card_playlist(c, 110, 350, 780, k1, "p", "Leitura da Proposta", "6 aulas · ler o tema sem fugir dele", rotulo="SÉRIE")
        motor.arrow(c, 920, 490, 1010, 490, YEL, k2, width=10, head=30, progress=k2)
        pill(c, "2ª SÉRIE · NOVA", 1420, 290, 28, YEL, NAVY, k2)
        card_playlist(c, 1030, 350, 780, k2, 0, "Introdução da Redação", "7 aulas · o 1º parágrafo do zero", rotulo="SÉRIE")


def wordmark(c, cx, cy, size, a, col=WHITE):
    if a <= 0:
        return
    w = text_w("ESTUDATIVO", "black", size)
    text(c, "ESTUDATIVO", cx - w / 2, cy + size * 0.35, size, "black", col, a, align="left")
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy + size * 0.55, w * ep(a, 0.2, 0.6), size * 0.12), 4, 4),
                paint(YEL, a))


def busca(c, cx, cy, w, h, a, t, t0, termo="Estudativo"):
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(rr, blur_paint("#000000", 0.4 * a, 20))
    c.drawRRect(rr, paint(WHITE, a))
    lx, r = cx - w / 2 + h * 0.6, h * 0.2
    c.drawCircle(lx, cy - r * 0.2, r, paint(MUT, a, stroke=h * 0.07))
    c.drawLine(lx + r * 0.7, cy + r * 0.5, lx + r * 1.4, cy + r * 1.2, paint(MUT, a, stroke=h * 0.08, cap_round=True))
    n = int(clamp((t - t0) / 0.7) * len(termo))
    s = termo[:n]
    tw = text(c, s, lx + h * 0.55, cy + h * 0.15, h * 0.42, "bold", INK, a, align="left")
    if (t * 2) % 1 < 0.6:
        c.drawRect(skia.Rect.MakeXYWH(lx + h * 0.55 + tw + 6, cy - h * 0.24, 4, h * 0.48), paint(INK, a))


def b_cta(c, t, C, B):
    a = ep(t, B["start"], 0.25)
    cid = B_CTA
    ta, tb, tc, td = C[cid + ".a"], C[cid + ".b"], C[cid + ".c"], C[cid + ".d"]
    fim = td if td < 1e8 else tc
    if VERT:
        wordmark(c, CX, 330, 120, a)
        busca(c, CX, 520, 860, 120, a * ep(t, ta, 0.3), t, ta + 0.2)
        card_playlist(c, 80, 660, 920, a * ep(t, tb, 0.35), 0, "Redação: Introdução", "7 aulas · do zero")
        kf = ep(t, fim, 0.3)
        pulse = 1 + 0.04 * math.sin(t * 6) * kf
        c.save(); c.translate(CX, 1150); c.scale(pulse, pulse)
        pill(c, "BONS ESTUDOS!", 0, 0, 56, YEL, NAVY, a * kf)
        c.restore()
    else:
        wordmark(c, 540, 300, 120, a)
        busca(c, 540, 500, 780, 116, a * ep(t, ta, 0.3), t, ta + 0.2)
        card_playlist(c, 1040, 150, 780, a * ep(t, tb, 0.35), 0, "Redação: Introdução", "A série · 7 aulas do zero")
        card_playlist(c, 1040, 470, 780, a * ep(t, tc, 0.35), "p", "Redação ENEM do Zero", "A trilha completa da redação", destaque=False)
        kf = ep(t, fim, 0.3)
        pulse = 1 + 0.04 * math.sin(t * 6) * kf
        c.save(); c.translate(540, 700); c.scale(pulse, pulse)
        pill(c, "TE VEJO NA 1ª AULA!", 0, 0, 52, YEL, NAVY, a * kf)
        c.restore()


B_ANT = "05" if VERT else "12"
B_CTA = "06" if VERT else "13"
BLOCKS = dict(gancho=b_gancho, generico=b_generico, perguntas=b_perguntas, serie=b_serie, intro=b_intro, eps=b_eps,
              anteriores=b_anteriores, cta=b_cta)

# efeitos sonoros (som_tech.py): carimbo = impact, viradas = whoosh, capas = pop
SFX_short = {"01.b": ["impact"], "02.a": ["pop", "pop@+0.25", "pop@+0.5"], "02.b": ["deny@+0.5"],
             "03.b": ["pop"], "03.c": ["pop"], "03.d": ["pop"],
             "04.a": ["pop@+0.25", "pop@+0.39", "pop@+0.53", "pop@+0.67", "pop@+0.81", "pop@+0.95", "pop@+1.09"],
             "05.b": ["confirm"], "06.a": ["typing@+0.2"], "06.b": ["lock"], "06.c": ["shimmer"]}
SFX_horizontal = {"01.b": ["impact"], "02.a": ["pop", "pop@+0.25", "pop@+0.5"], "02.b": ["deny@+0.5"],
                  "03.b": ["pop"], "03.c": ["pop"], "03.d": ["pop"], "04.a": ["shimmer@+0.3"],
                  "04.b": ["pop", "pop@+0.1", "pop@+0.2", "pop@+0.3", "pop@+0.4", "pop@+0.5", "pop@+0.6"],
                  "05.a": ["whoosh@-0.3"], "06.a": ["whoosh@-0.3"], "07.a": ["whoosh@-0.3"], "08.a": ["whoosh@-0.3"],
                  "09.a": ["whoosh@-0.3"], "10.a": ["whoosh@-0.3"], "11.a": ["whoosh@-0.3"],
                  "12.b": ["confirm"], "12.c": ["whoosh"],
                  "13.a": ["typing@+0.2"], "13.b": ["lock"], "13.c": ["lock"], "13.d": ["shimmer"]}
