"""Visual — Estudativo · Short 015 (vertical 1080x1920): ENEM 2025, questão 139, a mediana das velocidades (aula: 014).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 011/013 (selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras, contagem para pausar) e as fichas
das velocidades da aula 014. Cores com função: âmbar = dado (as velocidades), ciano = o meio da lista, menta = certo,
coral = a pegadinha (o meio da tabela sem ordenar)."""
import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_015_mediana_velocidade.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "data@+1.8"], "01.b": "whoosh", "01.c": "impact",
    "02.a": ["pop", "pop@+0.9", "pop@+1.8", "pop@+2.7", "pop@+3.6"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.37", "tick@+3.17", "tick2@+3.97"],   # tiques do cronômetro 3-2-1
    "03.a": "deny", "03.b": ["impact", "deny@+0.3"],
    "04.a": "whoosh", "04.b": "data",
    "05.a": "data", "05.b": "impact",
    "06.a": ["impact", "shimmer@+0.3"], "06.b": "confirm",
    "07.a": "notif", "07.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    qual=("WHAT'S THE", "QUAL É A"), mediana_q=("MEDIAN?", "MEDIANA?"), dez=("10 cities · MB/s", "10 cidades · MB/s"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    tabela=("FROM THE TABLE?", "DA TABELA?"), peg=("TRAP!", "PEGADINHA!"), em_ordem=("IN ORDER", "EM ORDEM"),
    meio=("MIDDLE: 5th AND 6th", "MEIO: 5º E 6º"), media=("mean", "média"), moda=("mode", "moda"), maior=("largest", "maior"),
    letra=("ANSWER C", "LETRA C"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025"), ("quinto", "5º"), ("sexto", "6º")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
matematica.EXPRESSOES |= {("são", "dez")}
n_ = lambda s: s.replace(".", "#").replace(",", ".").replace("#", ",") if EN else s   # noqa: E731  troca , e . no inglês
CX = W / 2
CAP_Y = 1440


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


def big(c, s, y, a, col=WHITE, size=100, hl=None, hl_col=CYA, maxw=980):
    """título grande centralizado; hl = trecho em pílula colorida"""
    if a <= 0:
        return
    f = ease_out(clamp(a))
    while text_w(s, "black", size) > maxw:
        size -= 3
    w = text_w(s, "black", size)
    x = CX - w / 2
    yy = y + (1 - f) * 24
    if hl and hl in s:
        i_hl = s.rindex(hl)
        pre = s[:i_hl]
        hx = x + text_w(pre, "black", size)
        hw = text_w(hl, "black", size)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(hx - 14, yy - size * 0.84, hw + 28, size * 1.1), 14, 14), paint(hl_col, f))
        text(c, pre, x, yy, size, "black", col, f, align="left")
        text(c, hl, hx, yy, size, "black", BG0, f, align="left")
        text(c, s[i_hl + len(hl):], hx + hw, yy, size, "black", col, f, align="left")
    else:
        glow_text(c, s, CX, yy, size, "black", col, f, glow=0.14)


def stamp(c, s, cx, cy, col, a, size=56, rot=-7):
    if a <= 0:
        return
    k = 1 + 0.6 * (1 - ease_out(clamp(a * 2.2)))
    c.save(); c.translate(cx, cy); c.rotate(rot); c.scale(k, k)
    w = text_w(s, "black", size) + size * 0.9
    h = size * 1.45
    r = skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h)
    c.drawRRect(skia.RRect.MakeRectXY(r, 12, 12), blur_paint(col, 0.5 * a, 16))
    c.drawRRect(skia.RRect.MakeRectXY(r, 12, 12), paint(col, a))
    text_mid(c, s, 0, 0, size, "black", BG0, a)
    c.restore()


def contagem(c, cx, cy, a, t, t0, dur=3.0):
    """cronômetro 3 → 1 com anel que esvazia"""
    if a <= 0 or t < t0:
        return
    u = clamp((t - t0) / dur)
    n = max(1, 3 - int((t - t0) / (dur / 3)))
    r = 120
    c.drawCircle(cx, cy, r, paint(BG1, 0.9 * a))
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, 360 * (1 - u), False, paint(AMB, a, stroke=14, cap_round=True))
    k = 1 + 0.25 * (1 - ep(t, t0 + (3 - n) * dur / 3, 0.25))
    c.save(); c.translate(cx, cy); c.scale(k, k)
    text_mid(c, str(n), 0, 0, 130, "black", WHITE, a)
    c.restore()



# ---------------------------------------------------------------- legenda de Short (1 a 3 palavras, grandes)
def _chunks(tokens):
    out, cur = [], []
    for tk in _num(tokens):
        cur.append(tk)
        end = tk["disp"][-1:] in PUNCT
        if len(cur) >= 3 or end or sum(len(x["disp"]) + 1 for x in cur) > 15:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def CAPTION(c, scene, t):
    lt = t - scene["start"]
    chunks = scene.setdefault("_chs", _chunks(scene["tokens"]))
    for i, ch in enumerate(chunks):
        s = ch[0]["t0"] - 0.06
        e = chunks[i + 1][0]["t0"] - 0.06 if i + 1 < len(chunks) else min(scene["dur"] - 0.05, ch[-1]["t1"] + 0.6)
        if s <= lt < e:
            break
    else:
        return
    words = [tk["disp"].upper() if not any(ch_.isdigit() for ch_ in tk["disp"]) else tk["disp"] for tk in ch]
    size, sp = 92, 24
    while sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1) > 960:
        size -= 3
    tot = sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1)
    pp = ease_back(clamp((lt - s) / 0.16))
    x = CX - tot / 2
    c.save(); c.translate(CX, CAP_Y); c.scale(0.85 + 0.15 * pp, 0.85 + 0.15 * pp); c.translate(-CX, -CAP_Y)
    f = motor.font("black", size)
    for tk, wd in zip(ch, words):
        falando = tk["t0"] - 0.05 <= lt < tk["t1"] + 0.25
        col = AMB if falando else (CYA if tk["bold"] else WHITE)
        sh = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.16, Color=hexc(BG0))
        sh.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, sh)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, paint(col, 1.0))
        x += text_w(wd, "black", size) + sp
    c.restore()


# ---------------------------------------------------------------- figuras
VALS = [390, 380, 320, 390, 340, 380, 390, 400, 350, 360]          # C1..C10, como no quadro
ORDEM = sorted(range(10), key=lambda i: (VALS[i], i))               # índices em ordem crescente
POS = {i: k for k, i in enumerate(ORDEM)}                           # posição de cada cidade na lista ordenada
FW, FH, PASSO_Y, Y0 = 330, 54, 64, 228                              # ficha: largura, altura; coluna: passo e topo


def ficha(c, x, y, cidade, v, a, borda=INK2, fundo=BG1, cor_v=WHITE, glow=0.0, k=1.0):
    """ficha de uma cidade: 'C3' à esquerda, a velocidade à direita; (x, y) = centro"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-FW / 2, -FH / 2, FW, FH), 16, 16)
    if glow > 0:
        c.drawRRect(r, blur_paint(borda, 0.5 * a * glow, 14))
    c.drawRRect(r, paint(fundo, 0.95 * a))
    c.drawRRect(r, paint(borda, a, stroke=3))
    if cidade:
        text_mid(c, cidade, -FW / 2 + 26, 0, 28, "bold", INK2, a, align="left")
    text_mid(c, str(v), FW / 2 - 26, 0, 38, "black", cor_v, a, align="right")
    c.restore()


def coluna(c, a, u, estilo=None, x=W / 2, y0=Y0, passo=PASSO_Y, extra=None, vals=None):
    """as dez fichas; u = 0: ordem do quadro, u = 1: ordem crescente (cada ficha desliza da linha i para POS[i]).
    estilo(i, k) → dict(borda, fundo, cor_v, glow) para a ficha da cidade i que está na posição k da lista ordenada.
    extra = (rótulo, valor) de uma 11ª ficha no fim da lista."""
    vals = vals or VALS
    ordem = sorted(range(len(vals)), key=lambda i: (vals[i], i))
    pos = {i: k for k, i in enumerate(ordem)}
    for i, v in enumerate(vals):
        uu = ease_io(clamp(u * 1.4 - 0.4 * (i / 9)))    # deslizam um pouco escalonadas
        y = y0 + passo * (i + (pos[i] - i) * uu)
        dx = 70 * math.sin(math.pi * uu) * (1 if (pos[i] - i) > 0 else -1) if pos[i] != i else 0
        st = dict(borda=INK2, fundo=BG1, cor_v=WHITE, glow=0.0)
        if estilo:
            st.update(estilo(i, pos[i]) or {})
        ficha(c, x + dx, y, f"C{i + 1}", v, a, **st)
    if extra:
        ficha(c, x, y0 + passo * len(vals), extra[0], extra[1], a, borda=MNT, cor_v=MNT)


def chave(c, x, y0, y1, s, a, col=INK2, lado=1):
    """chave vertical de y0 a y1 ao lado de x, com rótulo"""
    if a <= 0:
        return
    pth = skia.Path(); m = (y0 + y1) / 2; d = 18 * lado
    pth.moveTo(x, y0); pth.quadTo(x + d, y0, x + d, y0 + 20); pth.lineTo(x + d, m - 14); pth.quadTo(x + d, m, x + 2 * d, m)
    pth.quadTo(x + d, m, x + d, m + 14); pth.lineTo(x + d, y1 - 20); pth.quadTo(x + d, y1, x, y1)
    c.drawPath(pth, paint(col, a, stroke=3.5, cap_round=True))
    label(c, s, x + 2 * d + 14 * lado, m, a, 30, col, "black", "left" if lado > 0 else "right")


def bolinha(c, x, y, v, a, col=INK2, fundo=BG1, glow=0.0, k=1.0):
    """número numa bolinha (exemplos da ferramenta)"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    if glow:
        c.drawCircle(0, 0, 46, blur_paint(col, 0.5 * a * glow, 14))
    c.drawCircle(0, 0, 42, paint(fundo, 0.95 * a))
    c.drawCircle(0, 0, 42, paint(col, a, stroke=4))
    text_mid(c, str(v), 0, 0, 40 if v < 100 else 30, "black", WHITE, a)
    c.restore()



def opcoes(c, y0, a, t, t0, certo=None, errado=None, dim=0.0, extra=None):
    """as cinco alternativas; extra = {letra: rótulo} (ex.: 'média') ao lado da alternativa"""
    ops = [("A", "360"), ("B", "370"), ("C", "380"), ("D", "390"), ("E", "400")]
    for i, (le, v) in enumerate(ops):
        y = y0 + i * 118
        k = a * pop(t, t0 + i * 0.15, 0.3)
        if k <= 0:
            continue
        col = MNT if le == certo else (RED if le == errado else CYA)
        fade_k = k * (1 - dim * 0.75 * (le not in (certo, errado)))
        rrect(c, 170, y - 48, 740, 96, 48, BG1, 0.92 * fade_k)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(170, y - 48, 740, 96), 48, 48),
                    paint(col, fade_k, stroke=4 if le in (certo, errado) else 2))
        c.drawCircle(230, y, 34, paint(col, fade_k))
        text_mid(c, le, 230, y, 40, "black", BG0, fade_k)
        text_mid(c, v + " MB/s", 300, y, 54, "black", WHITE, fade_k, align="left")
        if extra and le in extra:
            text_mid(c, extra[le], 820, y, 38, "black", AMB, k, align="right")
        if le == certo:
            check(c, 850, y, 30, k)
        if le == errado:
            cross(c, 850, y, 30, k)


# ---------------------------------------------------------------- cenas
CY0, CP, ESC = 560, 60, 1.35     # coluna das fichas: topo, passo (antes da escala) e escala (fichas maiores no Short)


def _yc(k):
    return CY0 + CP * k * ESC


def col(c, a, u, estilo=None):
    """a coluna das dez fichas, ampliada em volta do topo"""
    c.save(); c.translate(CX, CY0); c.scale(ESC, ESC); c.translate(-CX, -CY0)
    coluna(c, a, u, estilo, y0=CY0, passo=CP)
    c.restore()


def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = ep(t, ta, 0.2) * (1 - prog(t, B["end"] - 0.2, 0.2))
    col(c, a, 0, lambda i, k: dict(borda=AMB, cor_v=AMB) if t >= ta + 1.8 + i * 0.12 else None)
    label(c, L["dez"], CX, 470, a * ep(t, ta + 1.8, 0.3), 46, AMB, "black")
    kb = a * ep(t, tb, 0.2)
    if kb > 0:
        k = 1 + 0.04 * math.sin(t * 8)
        c.save(); c.translate(CX, 330); c.scale(k, k); c.translate(-CX, -330)
        big(c, L["qual"], 280, kb, WHITE, 110)
        big(c, L["mediana_q"], 400, kb, WHITE, 110, hl=L["mediana_q"], hl_col=CYA)
        c.restore()


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    ko = a * (1 - ep(t, t0, 0.2))
    big(c, L["qual"], 300, ko, WHITE, 96)
    big(c, L["mediana_q"], 420, ko, WHITE, 96, hl=L["mediana_q"], hl_col=CYA)
    opcoes(c, 580, ko, t, ta + 0.6)
    label(c, L["comenta"], CX, 1200, ko * ep(t, tb, 0.3), 46, AMB, "extrabold")
    if t >= t0:
        kp = a * ep(t, t0, 0.2)
        label(c, L["pausa"], CX, 480, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 820); c.scale(1.5, 1.5); c.translate(-CX, -820)
        contagem(c, CX, 820, kp, t, t0, 2.4)
        c.restore()
        label(c, L["comenta"], CX, 1150, kp, 46, AMB, "extrabold")


def b_pegadinha(c, t, C, B):
    ta, tb = C["03.a"], C["03.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kr = ep(t, ta + 1.0, 0.3)
    col(c, a, 0, lambda i, k: dict(borda=RED, glow=kr, cor_v=RED) if i in (4, 5) and kr > 0 else None)
    if kr > 0:
        chave(c, CX + FW * ESC / 2 + 16, _yc(4) - 24, _yc(5) + 24, "5ª e 6ª", a * kr, RED)
    pos = eq(c, [("(340 + 380) ÷ 2 = ", WHITE), ("360", RED)], 440, a * ep(t, ta + 2.6, 0.3), 76, cx=CX, maxw=980)
    big(c, L["tabela"], 320, a * ep(t, ta + 0.6, 0.3), AMB, 100)
    if pos:
        strike(c, pos[0][0], pos[-1][1], 440, a, ep(t, tb, 0.3))
    stamp(c, L["peg"], CX, 1270, RED, a * ep(t, tb, 0.2), 76)


@lru_cache(None)
def _leitura():
    """instantes (absolutos) em que a voz lê cada valor da lista ordenada (cena 04): palavras do Whisper
    (analise/voz.json), deslocadas para o vídeo pelo "Então" que abre a cena"""
    import json
    from pathlib import Path
    raiz = Path(__file__).resolve().parent.parent
    tp = json.loads((raiz / "audio" / "tempos.json").read_text(encoding="utf-8"))
    sc = next(x for x in tp["scenes"] if x["id"] == "04")
    ws = json.loads((raiz / "analise" / "voz.json").read_text(encoding="utf-8"))[0]["words"]
    i0 = [j for j, w in enumerate(ws) if w["w"].startswith("Então")][0]
    desl = sc["start"] + sc["cues"]["a"] - ws[i0]["s"]
    out, j = [], i0
    for v in ["320", "340", "350", "360", "380", "380", "390", "390", "390", "400"]:
        while j < len(ws) and ws[j]["w"].strip(",.") != v:
            j += 1
        if j == len(ws):
            return []
        out.append(ws[j]["s"] + desl); j += 1
    return out


def b_ordenar(c, t, C, B):
    ta, tb = C["04.a"], C["04.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    u = prog(t, ta + 0.4, 1.6)
    kb = ep(t, tb + 1.2, 0.3)
    ts = _leitura()

    def est(i, k):
        if kb > 0:
            return dict(borda=CYA, glow=kb, cor_v=CYA) if k in (4, 5) else None
        if len(ts) == 10 and t >= ts[k]:
            falando = t < (ts[k + 1] if k < 9 else ts[k] + 0.9)
            return dict(borda=AMB if falando else CYA, glow=1.0 if falando else 0.0)
        return None
    col(c, a, u, est)
    big(c, L["em_ordem"], 330, a * ep(t, ta, 0.3), WHITE, 120, hl=L["em_ordem"].split()[-1], hl_col=MNT)
    big(c, L["meio"], 460, a * ep(t, tb, 0.3), CYA, 80)
    if kb > 0:
        ym = (_yc(4) + _yc(5)) / 2
        pd = paint(CYA, a * kb, stroke=4); pd.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
        c.drawLine(CX - FW * ESC / 2 - 70, ym, CX + FW * ESC / 2 + 70, ym, pd)
        label(c, "5º", CX - FW * ESC / 2 - 44, _yc(4), a * kb, 34, CYA, "black")
        label(c, "6º", CX - FW * ESC / 2 - 44, _yc(5), a * kb, 34, CYA, "black")


def b_meio(c, t, C, B):
    ta, tb = C["05.a"], C["05.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kb = ep(t, tb + 1.2, 0.3)
    cor = MNT if kb > 0 else CYA
    col(c, a, 1, lambda i, k: dict(borda=cor, glow=1.0, cor_v=cor) if k in (4, 5) else None)
    eq(c, [("(380 + 380) ÷ 2", WHITE)], 320, a * ep(t, tb, 0.3), 84, cx=CX, maxw=980)
    eq(c, [("= ", WHITE), ("380", MNT)], 450, a * kb, 110, cx=CX, maxw=980, box=MNT)


def b_resposta(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        k = pop(t, ta, 0.4)
        c.save(); c.translate(CX, 400); c.scale(k, k); c.translate(-CX, -400)
        glow_text(c, "380", CX, 420, 230, "black", MNT, ka, glow=0.3)
        c.restore()
        label(c, "MB/s", CX, 520, ka, 64, WHITE, "black")
        opcoes(c, 680, ka, t, ta + 0.8, certo="C", dim=1.0,
               extra={k: v for k, v, dt in (("B", L["media"], 1.0), ("D", L["moda"], 2.4), ("E", L["maior"], 3.8)) if t >= ta + dt})
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        big(c, L["letra"], 340, kb, WHITE, 110, hl="C", hl_col=MNT)
        opcoes(c, 560, kb, t, tb - 0.4, certo="C", errado="A", dim=1.0)


def b_final(c, t, C, B):
    ta, tb = C["07.a"], C["07.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 380, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        opcoes(c, 560, ka, t, ta - 1.0, certo="C")
        label(c, L["conta"], CX, 1180, ka * ep(t, ta + 0.8, 0.3), 50, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 760, kb, CYA, L["aula"])
        for j, v in enumerate((320, 360, 380, 390, 400)):
            bolinha(c, CX - 280 + j * 140, 680, v, kb, MNT if j == 2 else INK2, glow=1.0 if j == 2 else 0, k=1.0)
        text_mid(c, L["passo"], CX, 860, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1000, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1026, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, pegadinha=b_pegadinha, ordenar=b_ordenar, meio=b_meio,
              resposta=b_resposta, final=b_final)
