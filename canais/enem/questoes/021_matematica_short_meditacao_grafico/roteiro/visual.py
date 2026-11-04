"""Visual — Estudativo · Short 021 (vertical 1080x1920): ENEM 2025, questão 142, o gráfico da respiração na meditação
(aula: 020). render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py),
com o layout de Short do 015/017/019 (selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras, contagem
para pausar) e o gráfico da aula 020 (grafico()). Cores: âmbar = dados (f1, f2, t1, t2), ciano = o trecho que desce,
menta = o trecho deitado e a resposta, coral = as formas erradas (curva inversa, reta direta)."""
import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_021_meditacao_grafico.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "whoosh@+1.6"], "01.b": "data", "01.c": "alert",
    "02.a": ["pop", "pop@+1.4", "pop@+3.0", "pop@+4.8", "pop@+7.0"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.57", "tick@+3.37", "tick2@+4.17"],   # tiques do cronômetro 3-2-1 (ajustados ao áudio)
    "03.a": "deny", "03.b": ["impact", "deny@+0.3"], "03.c": "confirm",
    "04.a": "whoosh", "04.b": "confirm", "04.c": "confirm",
    "05.a": ["impact", "shimmer@+0.3"], "05.b": "confirm", "05.c": "deny",
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    oque=("WHAT HAPPENS", "O QUE ACONTECE"), depois=("AFTER t₁?", "DEPOIS DE t₁?"),
    rpm=("breaths per minute while meditating", "respirações por minuto, meditando"),
    comeca=("t₁ = meditation starts", "t₁ = começa a meditação"),
    eixo_t=("time (min)", "tempo (min)"), eixo_f=("rate (bpm)", "frequência (rpm)"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    peg=("TRAP!", "PEGADINHA!"), inversa=("inverse: NEVER goes flat", "inversa: NUNCA deita"),
    deita=("here it goes flat ✓", "aqui ela deita ✓"),
    trecho=("PART BY PART", "TRECHO POR TRECHO"), diminui=("↓ DECREASES", "↓ DIMINUI"), constante=("→ CONSTANT", "→ CONSTANTE"),
    resp1=("DECREASES,", "DIMINUI,"), resp2=("THEN CONSTANT", "DEPOIS CONSTANTE"), letra=("ANSWER D", "LETRA D"),
    direta=("not direct: time ↑, rate ↓", "não é direta: tempo ↑, respiração ↓"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025"), ("tê um", "t₁"), ("tê dois", "t₂")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
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






# ---------------------------------------------------------------- o gráfico (o mesmo da aula 020)
T1, T2 = 0.36, 0.66          # posições de t1 e t2 no eixo do tempo (0..1)
F1, F2 = 0.74, 0.36          # alturas de f1 e f2 (0..1)
GX, GY, GW, GH = 210, 1200, 720, 500     # origem do gráfico na tela do Short


def f(u):
    """altura (0..1) da linha no tempo u (0..1): deitada em F1, desce suave de T1 a T2, deitada em F2"""
    if u <= T1:
        return F1
    if u >= T2:
        return F2
    k = (u - T1) / (T2 - T1)
    k = k * k * k * (k * (6 * k - 15) + 10)
    return F1 + (F2 - F1) * k


def _xy(u, v, g):
    gx, gy, gw, gh = g
    return gx + u * gw, gy - v * gh


def _tracejado(col, a, w=3):
    p = paint(col, a, stroke=w)
    p.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
    return p


def _curva(c, u0, u1, g, col, a, w=9, glow=0.0, fn=f):
    if a <= 0 or u1 <= u0:
        return
    p = skia.Path()
    n = max(2, int((u1 - u0) * 160))
    for i in range(n + 1):
        u = u0 + (u1 - u0) * i / n
        x, y = _xy(u, fn(u), g)
        (p.moveTo if i == 0 else p.lineTo)(x, y)
    if glow > 0:
        c.drawPath(p, blur_paint(col, 0.6 * a * glow, 18, stroke=w * 2.4))
    st = paint(col, a, stroke=w, cap_round=True)
    st.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, st)


def eixos(c, a, g=(GX, GY, GW, GH), rot=True, size=1.0):
    gx, gy, gw, gh = g
    if a <= 0:
        return
    w = 4 * size
    c.drawLine(gx, gy, gx + gw + 30 * size, gy, paint(WHITE, a, stroke=w, cap_round=True))
    c.drawLine(gx, gy, gx, gy - gh - 30 * size, paint(WHITE, a, stroke=w, cap_round=True))
    for (x0, y0, dx, dy) in ((gx + gw + 30 * size, gy, 1, 0), (gx, gy - gh - 30 * size, 0, -1)):
        s = 16 * size
        p = skia.Path()
        p.moveTo(x0 + dx * s, y0 + dy * s)
        p.lineTo(x0 - dy * s * 0.6 - dx * 0.0, y0 + dx * s * 0.6)
        p.lineTo(x0 + dy * s * 0.6, y0 - dx * s * 0.6)
        p.close()
        c.drawPath(p, paint(WHITE, a))
    if rot:
        text_mid(c, L["eixo_t"], gx + gw, gy + 46 * size, 30 * size, "bold", INK2, a, align="right")
        c.save(); c.translate(gx - 100 * size, gy - gh / 2); c.rotate(-90)
        text_mid(c, L["eixo_f"], 0, 0, 30 * size, "bold", INK2, a)
        c.restore()


def grafico(c, a, t, draw=1.0, cores=None, ponto=None, guias=1.0, g=(GX, GY, GW, GH), marcas=1.0):
    """o gráfico da questão. cores = {"antes": (cor, alfa, glow), "desce": ..., "deitada": ...} pinta cada trecho;
    draw 0..1 desenha a linha da esquerda para a direita; ponto = u (0..1) mostra um ponto com as projeções"""
    if a <= 0:
        return
    gx, gy, gw, gh = g
    eixos(c, a, g)
    km = a * marcas
    # marcas f1, f2, t1, t2 e as guias tracejadas
    for v, s in ((F1, "f₁"), (F2, "f₂")):
        text_mid(c, s, gx - 24, gy - v * gh, 40, "black", AMB, km, align="right")
    for u, s in ((T1, "t₁"), (T2, "t₂")):
        text_mid(c, s, gx + u * gw, gy + 40, 40, "black", AMB, km)
    if guias > 0:
        x1, y1 = _xy(T1, F1, g)
        x2, y2 = _xy(T2, F2, g)
        c.drawLine(x1, y1, x1, gy, _tracejado(INK2, 0.7 * a * guias))
        c.drawLine(x2, y2, x2, gy, _tracejado(INK2, 0.7 * a * guias))
        c.drawLine(gx, y2, x2, y2, _tracejado(INK2, 0.5 * a * guias))
    cores = cores or {}
    padrao = (WHITE, 1.0, 0.0)
    for nome, u0, u1 in (("antes", 0.0, T1), ("desce", T1, T2), ("deitada", T2, 1.0)):
        col, al, gl = cores.get(nome, padrao)
        _curva(c, u0, min(u1, draw), g, col, a * al, glow=gl)
    if ponto is not None and 0 <= ponto <= 1:
        x, y = _xy(ponto, f(ponto), g)
        c.drawLine(x, y, x, gy, _tracejado(CYA, 0.9 * a))
        c.drawLine(gx, y, x, y, _tracejado(CYA, 0.9 * a))
        c.drawCircle(x, y, 22, blur_paint(CYA, 0.6 * a, 14))
        c.drawCircle(x, y, 13, paint(WHITE, a))
        c.drawCircle(x, y, 13, paint(CYA, a, stroke=5))


def mini(c, a, cx, cy, tipo, col, draw=1.0, w=150, h=110):
    """grafiquinho: 'sobe', 'desce', 'deitada', 'direta', 'inversa' (eixos + a forma)"""
    if a <= 0:
        return
    g = (cx - w / 2, cy + h / 2, w, h)
    eixos(c, a, g, rot=False, size=0.5)
    fn = {"sobe": lambda u: 0.15 + 0.7 * u, "desce": lambda u: 0.85 - 0.7 * u, "deitada": lambda u: 0.5,
          "direta": lambda u: 0.9 * u, "inversa": lambda u: min(1.0, 0.12 / max(u, 0.01))}[tipo]
    _curva(c, 0.0 if tipo != "inversa" else 0.12, draw, g, col, a, w=7, fn=fn)




OPS = ([("A", "stays constant"), ("B", "directly proportional"), ("C", "inversely proportional"),
        ("D", "decreases, then constant"), ("E", "decreases the whole time")] if EN else
       [("A", "fica constante"), ("B", "diretamente proporcional"), ("C", "inversamente proporcional"),
        ("D", "diminui, depois constante"), ("E", "diminui o tempo todo")])


def opcoes(c, y0, a, t, t0, certo=None, errado=None, dim=0.0, falas=None):
    """as cinco alternativas; falas = instantes em que cada uma entra (senão, em sequência a partir de t0)"""
    for i, (le, v) in enumerate(OPS):
        y = y0 + i * 118
        k = a * pop(t, falas[i] if falas else t0 + i * 0.15, 0.3)
        if k <= 0:
            continue
        col = MNT if le == certo else (RED if le == errado else CYA)
        fade_k = k * (1 - dim * 0.75 * (le not in (certo, errado)))
        rrect(c, 110, y - 48, 860, 96, 48, BG1, 0.92 * fade_k)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(110, y - 48, 860, 96), 48, 48),
                    paint(col, fade_k, stroke=4 if le in (certo, errado) else 2))
        c.drawCircle(170, y, 34, paint(col, fade_k))
        text_mid(c, le, 170, y, 40, "black", BG0, fade_k)
        sz = 46
        while text_w(v, "black", sz) > 660:
            sz -= 2
        text_mid(c, v, 230, y, sz, "black", WHITE, fade_k, align="left")
        if le == certo:
            check(c, 920, y, 30, k)
        if le == errado:
            cross(c, 920, y, 30, k)


@lru_cache(None)
def _falas_opcoes():
    """instantes (absolutos) em que a voz começa cada opção, pelas palavras do Whisper (analise/voz.json)"""
    import json
    from pathlib import Path
    ws = json.loads((Path(__file__).resolve().parent.parent / "analise" / "voz.json").read_text(encoding="utf-8"))[0]["words"]
    alvo = ["fica", "diretamente", "inversamente", "diminui", "diminui"]
    out, j = [], 0
    i0 = next((k for k, w in enumerate(ws) if w["w"].lower().startswith("opç")), 0)
    j = i0
    for p in alvo:
        while j < len(ws) and not ws[j]["w"].lower().startswith(p):
            j += 1
        if j == len(ws):
            return None
        out.append(ws[j]["s"] - 0.1); j += 1
    return out


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = ep(t, ta, 0.2) * (1 - prog(t, B["end"] - 0.2, 0.2))
    cores = {"antes": (WHITE, 1.0, 0), "desce": (WHITE, 1.0, 0), "deitada": (WHITE, 1.0, 0)}
    grafico(c, a, t, ep(t, ta + 0.6, 2.4), cores=cores, guias=ep(t, tb, 0.3), marcas=ep(t, ta + 1.0, 0.3))
    if t >= tb:   # t1 em destaque
        x = GX + T1 * GW
        c.drawCircle(x, GY + 40, 34, blur_paint(AMB, 0.7 * a * ep(t, tb, 0.3), 14))
    label(c, L["rpm"], CX, 560, a * ep(t, ta + 1.4, 0.3), 40, INK2, "bold")
    label(c, L["comeca"], CX, 1300, a * ep(t, tb, 0.3), 46, AMB, "black")
    kc = a * ep(t, ta + 0.3, 0.2)   # a pergunta já no começo (Short: pergunta nos 3 primeiros segundos)
    if kc > 0:
        k = 1 + 0.04 * math.sin(t * 8) * ep(t, tc, 0.2)
        c.save(); c.translate(CX, 330); c.scale(k, k); c.translate(-CX, -330)
        big(c, L["oque"], 290, kc, WHITE, 104)
        big(c, L["depois"], 420, kc, WHITE, 104, hl="t₁?", hl_col=AMB)
        c.restore()


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    ko = a * (1 - ep(t, t0, 0.2))
    big(c, L["oque"], 300, ko, WHITE, 96)
    big(c, L["depois"], 420, ko, WHITE, 96, hl="t₁?", hl_col=AMB)
    opcoes(c, 620, ko, t, ta + 0.6, falas=_falas_opcoes())
    label(c, L["comenta"], CX, 1250, ko * ep(t, tb, 0.3), 46, AMB, "extrabold")
    if t >= t0:
        kp = a * ep(t, t0, 0.2)
        label(c, L["pausa"], CX, 480, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 820); c.scale(1.5, 1.5); c.translate(-CX, -820)
        contagem(c, CX, 820, kp, t, t0, 2.4)
        c.restore()
        label(c, L["comenta"], CX, 1150, kp, 46, AMB, "extrabold")


def b_pegadinha(c, t, C, B):
    ta, tb, tc = (C[f"03.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kc = ep(t, tc, 0.3)
    cores = {"antes": (INK2, 0.4, 0), "desce": (WHITE, 1.0, 0), "deitada": (MNT if kc else WHITE, 1.0, kc)}
    grafico(c, a, t, 1.0, cores=cores)
    fi = lambda u: min(1.05, 0.2 / max(u, 0.01))   # noqa: E731  a curva inversa (nunca deita)
    kb = a * ep(t, ta + 0.4, 0.3)
    _curva(c, 0.19, 0.19 + 0.81 * ep(t, ta + 0.6, 1.4), (GX, GY, GW, GH), RED, kb, w=7, fn=fi, glow=0.3)
    stamp(c, L["peg"], CX, 330, RED, a * ep(t, ta + 2.0, 0.2), 76)
    label(c, L["inversa"], CX, 480, a * ep(t, tb + 1.2, 0.3), 56, RED, "black")
    label(c, L["deita"], CX, 1300, a * ep(t, tc + 1.4, 0.3), 54, MNT, "black")


def b_trechos(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kb, kc = ep(t, tb, 0.3), ep(t, tc, 0.3)
    cores = {"antes": (INK2, 0.4, 0), "desce": (CYA if kb else WHITE, 1.0, kb), "deitada": (MNT if kc else WHITE, 1.0, kc)}
    pu = None
    if tb <= t < tc:
        pu = T1 + (T2 - T1) * ease_io(prog(t, tb + 0.2, 2.2))
    elif t >= tc:
        pu = T2 + (1 - T2) * ease_io(prog(t, tc + 0.2, 2.6))
    grafico(c, a, t, 1.0, cores=cores, ponto=pu)
    big(c, L["trecho"], 330, a * ep(t, ta + 0.2, 0.3), WHITE, 92)
    popill(c, L["diminui"], CX - 200, 500, 50, CYA, BG0, a * ep(t, tb + 1.4, 0.3), t, tb + 1.4)
    popill(c, L["constante"], CX + 210, 500, 50, MNT, BG0, a * ep(t, tc + 1.4, 0.3), t, tc + 1.4)


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kc = ep(t, tc, 0.3)
    cores = {"antes": (INK2, 0.4, 0), "desce": (CYA, 1.0, 1.0 - kc), "deitada": (MNT, 1.0, 1.0 - kc)}
    grafico(c, a, t, 1.0, cores=cores)
    if kc > 0:   # a reta da diretamente proporcional, que subiria
        _curva(c, 0.0, ep(t, tc + 0.4, 1.0), (GX, GY, GW, GH), RED, a * kc, w=7, fn=lambda u: 0.08 + 0.85 * u)
    k = pop(t, ta, 0.4)
    ka = a * (1 - ep(t, tb, 0.25))
    c.save(); c.translate(CX, 380); c.scale(k, k); c.translate(-CX, -380)
    big(c, L["resp1"], 330, ka, CYA, 110)
    big(c, L["resp2"], 460, ka, MNT, 110)
    c.restore()
    big(c, L["letra"], 380, a * ep(t, tb, 0.3) * (1 - kc), WHITE, 130, hl="D", hl_col=MNT)
    big(c, L["letra"], 330, a * kc, WHITE, 100, hl="D", hl_col=MNT)
    label(c, L["direta"], CX, 470, a * ep(t, tc + 0.6, 0.3), 46, RED, "black")


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 380, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        opcoes(c, 560, ka, t, ta - 1.0, certo="D", dim=1.0)
        label(c, L["conta"], CX, 1200, ka * ep(t, ta + 0.8, 0.3), 50, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 760, kb, CYA, L["aula"])
        g = (330, 760, 420, 280)
        grafico(c, kb, t, 1.0, cores={"antes": (INK2, 0.5, 0), "desce": (CYA, 1, 0.6), "deitada": (MNT, 1, 0.6)}, g=g, marcas=0,
                guias=0)
        text_mid(c, L["passo"], CX, 880, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1010, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1036, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, pegadinha=b_pegadinha, trechos=b_trechos, resposta=b_resposta, final=b_final)
