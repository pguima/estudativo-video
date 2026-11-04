"""Visual — Estudativo · Short 023 (vertical 1080x1920): ENEM 2025, questão 143, o recorde de Usain Bolt (aula: 022).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 019/021 (selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras, contagem para pausar) e a conta
armada da aula 022 (conta()). Cores: âmbar = os números do enunciado, ciano = os empréstimos, menta = o resultado certo e a
conferência, coral = as armadilhas (0,52 e 1,42)."""
import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_023_recorde_bolt.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "whoosh@+1.6"], "01.b": "data", "01.c": "alert",
    "02.a": ["pop", "pop@+1.3", "pop@+2.6", "pop@+3.9", "pop@+5.2"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.09", "tick@+2.89", "tick2@+3.69"],   # tiques do cronômetro 3-2-1 (ajustados ao áudio)
    "03.a": "deny", "03.b": ["impact", "deny@+0.3"],
    "04.a": "whoosh", "04.b": "data", "04.c": "confirm",
    "05.a": ["impact", "shimmer@+0.3"], "05.b": "confirm", "05.c": "confirm",
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    qual=("WHAT'S THE", "QUAL É A"), dif=("DIFFERENCE?", "DIFERENÇA?"),
    ref=("benchmark: 10.00 s", "referência: 10,00 s"), bolt=("Usain Bolt, 2009: 9.58 s", "Usain Bolt, 2009: 9,58 s"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    armadilha=("TRAP!", "ARMADILHA!"), esqueceu=("borrowed, but didn't take it off", "pegou emprestado e não descontou"),
    regra=("point under point", "vírgula embaixo de vírgula"), vira=("10 = 9 + 0.9 + 0.10", "10 = 9 + 0,9 + 0,10"),
    letra=("ANSWER B", "LETRA B"), confere=("9.58 + 0.42 = 10.00 ✓", "9,58 + 0,42 = 10,00 ✓"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("nove vírgula cinquenta e oito", "9,58"), ("dez vírgula zero zero", "10,00"),
    ("zero vírgula zero dois", "0,02"), ("zero vírgula quarenta e dois", "0,42"), ("zero vírgula cinquenta e dois", "0,52"),
    ("um vírgula zero dois", "1,02"), ("um vírgula quarenta e dois", "1,42")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
matematica.EXPRESSOES |= {("dez", "menos")}
n_ = lambda s: s.replace(",", ".") if EN else s   # noqa: E731
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







# ---------------------------------------------------------------- a conta armada (a mesma da aula 022)
CW = 100   # largura de uma coluna (algarismo)


def _xs(s, cx):
    """x de cada caractere de s, alinhado pela vírgula em cx (sem vírgula: as unidades terminam em cx)"""
    ref = s.index(",") if "," in s else len(s)
    out = []
    for i in range(len(s)):
        if i < ref:
            out.append(cx - 0.3 * CW - (ref - i - 0.5) * CW)
        elif i == ref:
            out.append(cx)
        else:
            out.append(cx + 0.3 * CW + (i - ref - 0.5) * CW)
    return out


def conta(c, a, t, cx, y0, top, bot, sinal="−", res=None, res_vis=None, res_col=MNT, novos=None, riscos=(), hl=(),
          hl_col=AMB, cores_res=None, size=104, bot_a=1.0, linha_a=1.0):
    """conta armada: top e bot com o mesmo comprimento (' ' = vazio); res = resultado (mesmo alinhamento),
    res_vis = índices já escritos; novos = {índice: texto do empréstimo em cima}; riscos = índices riscados em top;
    hl = colunas em destaque; cores_res = {índice: cor} (ex.: o algarismo errado em coral)"""
    if a <= 0:
        return
    xs = _xs(top, cx)
    y1, y2, yr = y0, y0 + 140, y0 + 300
    for i in hl:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[i] - CW * 0.46, y1 - 120, CW * 0.92, (yr if res else y2) - y1 + 170), 18, 18)
        c.drawRRect(r, blur_paint(hl_col, 0.35 * a, 14))
        c.drawRRect(r, paint(hl_col, 0.12 * a))
        c.drawRRect(r, paint(hl_col, 0.8 * a, stroke=3))
    for i, ch in enumerate(top):
        if ch.strip():
            text_mid(c, ch, xs[i], y1, size, "black", AMB if ch != "," else WHITE, a * (0.45 if i in riscos else 1))
            if i in riscos:
                c.drawLine(xs[i] - 30, y1 + 34, xs[i] + 30, y1 - 34, paint(RED, a, stroke=7, cap_round=True))
    for i, s in (novos or {}).items():
        if s:
            text_mid(c, s, xs[i], y1 - 92, size * 0.5, "black", CYA, a)
    kb = a * bot_a
    for i, ch in enumerate(bot):
        if ch.strip():
            text_mid(c, ch, xs[i], y2, size, "black", AMB if ch != "," else WHITE, kb)
    text_mid(c, sinal, min(xs) - CW * 0.95, y2, size, "black", WHITE, kb)
    kl = a * linha_a
    if kl > 0:
        c.drawLine(min(xs) - CW * 1.4, y2 + 80, max(xs) + CW * 0.5, y2 + 80, paint(WHITE, kl, stroke=6, cap_round=True))
    if res:
        vis = range(len(res)) if res_vis is None else res_vis
        for i in vis:
            ch = res[i]
            if ch.strip():
                col = (cores_res or {}).get(i, res_col if ch != "," else WHITE)
                text_mid(c, ch, xs[i], yr, size, "black", col, a)


OPS = [("A", "0,02"), ("B", "0,42"), ("C", "0,52"), ("D", "1,02"), ("E", "1,42")]


def opcoes(c, y0, a, t, t0, certo=None, errado=(), dim=0.0, falas=None):
    """as cinco alternativas (em segundos); falas = instantes em que cada uma entra"""
    for i, (le, v) in enumerate(OPS):
        y = y0 + i * 118
        k = a * pop(t, falas[i] if falas else t0 + i * 0.15, 0.3)
        if k <= 0:
            continue
        col = MNT if le == certo else (RED if le in errado else CYA)
        fade_k = k * (1 - dim * 0.75 * (le != certo and le not in errado))
        rrect(c, 170, y - 48, 740, 96, 48, BG1, 0.92 * fade_k)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(170, y - 48, 740, 96), 48, 48),
                    paint(col, fade_k, stroke=4 if (le == certo or le in errado) else 2))
        c.drawCircle(230, y, 34, paint(col, fade_k))
        text_mid(c, le, 230, y, 40, "black", BG0, fade_k)
        text_mid(c, n_(v) + " s", 300, y, 54, "black", WHITE, fade_k, align="left")
        if le == certo:
            check(c, 850, y, 30, k)
        if le in errado:
            cross(c, 850, y, 30, k)


@lru_cache(None)
def _falas_opcoes():
    """instantes (absolutos) em que a voz começa cada opção, pelas palavras do Whisper (analise/voz.json)"""
    import json
    from pathlib import Path
    ws = json.loads((Path(__file__).resolve().parent.parent / "analise" / "voz.json").read_text(encoding="utf-8"))[0]["words"]
    j = next((k for k, w in enumerate(ws) if w["w"].lower().startswith("opç")), None)
    if j is None:
        return None
    out = []
    for p in ("0", "0", "0", "1", "1"):
        j += 1
        while j < len(ws) and not ws[j]["w"].lstrip("(").startswith(p):
            j += 1
        if j >= len(ws):
            return None
        out.append(ws[j]["s"] - 0.1)
        j += 1
    return out


CY = 640   # topo da conta na tela do Short
ZOOM = 1.45


def contaG(c, a, t, *args, **kw):
    """a conta da aula, ampliada para a tela do Short (escala do quadro inteiro, sem apertar as colunas)"""
    kw.pop("size", None)
    oy = CY + 170
    c.save(); c.translate(CX, oy); c.scale(ZOOM, ZOOM); c.translate(-CX, -oy)
    conta(c, a, t, *args, **kw)
    c.restore()


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = ep(t, ta, 0.2) * (1 - prog(t, B["end"] - 0.2, 0.2))
    contaG(c, a * ep(t, ta + 0.4, 0.3), t, CX + 40, CY + 100, "10,00", " 9,58", bot_a=ep(t, tb, 0.3), linha_a=ep(t, tb, 0.3),
          res=" ?,??", res_vis=[1, 2, 3, 4] if t >= tc else [], res_col=CYA, size=124)
    label(c, n_(L["ref"]), CX, 560, a * ep(t, ta + 1.6, 0.3), 44, AMB, "black")
    label(c, n_(L["bolt"]), CX, 1290, a * ep(t, tb, 0.3), 44, MNT, "black")
    kc = a * ep(t, ta + 0.3, 0.2)   # a pergunta já no começo (Short: pergunta nos 3 primeiros segundos)
    if kc > 0:
        k = 1 + 0.04 * math.sin(t * 8) * ep(t, tc, 0.2)
        c.save(); c.translate(CX, 330); c.scale(k, k); c.translate(-CX, -330)
        big(c, L["qual"], 290, kc, WHITE, 110)
        big(c, L["dif"], 420, kc, WHITE, 110, hl=L["dif"], hl_col=CYA)
        c.restore()


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    ko = a * (1 - ep(t, t0, 0.2))
    big(c, n_("10,00 − 9,58 = ?"), 360, ko, WHITE, 104, hl="?", hl_col=CYA)
    opcoes(c, 600, ko, t, ta + 0.6, falas=_falas_opcoes())
    label(c, L["comenta"], CX, 1240, ko * ep(t, tb, 0.3), 46, AMB, "extrabold")
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
    segundo = t >= ta + 2.4
    res, cr, nv, hl = ((" 1,42", {1: RED}, {1: "10", 3: "9", 4: "10"}, (1,)) if segundo else
                       (" 0,52", {3: RED}, {1: "9", 3: "10", 4: "10"}, (3,)))
    contaG(c, a * ep(t, ta + 0.2, 0.3), t, CX + 40, CY + 20, "10,00", " 9,58", res=res, res_col=WHITE, cores_res=cr,
          novos=nv, riscos=(0, 1, 3, 4), hl=hl, hl_col=RED, size=124)
    stamp(c, L["armadilha"], CX, 330, RED, a * ep(t, ta + 2.0, 0.2), 76)
    label(c, L["esqueceu"], CX, 1300, a * ep(t, tb, 0.3), 48, RED, "black")


def b_conta(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    dur = B["end"] - tc
    t2, t4, t0 = tc + 0.05 * dur, tc + 0.35 * dur, tc + 0.65 * dur
    emp = t >= tb + 1.6
    vis = [i for i, tt in ((4, t2), (3, t4), (2, t0), (1, t0)) if t >= tt]
    if t < tb + 1.6:
        hl, hc = ((4, 3) if t >= tb else (2,)), (RED if t >= tb else CYA)
    elif t < tc:
        hl, hc = (0, 1, 3, 4), CYA
    else:
        hl, hc = ((4,) if t < t4 else (3,) if t < t0 else (1,)), AMB
    contaG(c, a, t, CX + 40, CY + 20, "10,00", " 9,58", res=" 0,42", res_vis=vis,
          novos={1: "9", 3: "9", 4: "10"} if emp else None, riscos=(0, 1, 3, 4) if emp else (), hl=hl, hl_col=hc, size=124)
    label(c, L["regra"], CX, 330, a * ep(t, ta + 0.2, 0.3) * (1 - ep(t, tb + 1.6, 0.3)), 64, CYA, "black")
    label(c, n_(L["vira"]), CX, 330, a * ep(t, tb + 1.6, 0.3), 64, CYA, "black")


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kc = ep(t, tc, 0.3)
    if kc < 1:
        contaG(c, a * (1 - kc), t, CX + 40, CY + 20, "10,00", " 9,58", res=" 0,42", novos={1: "9", 3: "9", 4: "10"},
              riscos=(0, 1, 3, 4), size=124)
    if kc > 0:   # a conferência pela soma
        vis = [i for i, tt in ((4, 0.0), (3, 0.6), (2, 1.2), (1, 1.2), (0, 1.8)) if t >= tc + 0.8 + tt]
        contaG(c, a * kc, t, CX + 40, CY + 20, " 9,58", " 0,42", sinal="+", res="10,00", res_vis=vis,
              novos={3: "1", 1: "1"} if t >= tc + 0.8 else None, size=124)
    k = pop(t, ta, 0.4)
    c.save(); c.translate(CX, 380); c.scale(k, k); c.translate(-CX, -380)
    glow_text(c, n_("0,42 s"), CX, 400, 170, "black", MNT, a * (1 - ep(t, tb, 0.25)), glow=0.3)
    c.restore()
    big(c, L["letra"], 380, a * ep(t, tb, 0.3) * (1 - kc), WHITE, 130, hl="B", hl_col=MNT)
    big(c, L["letra"], 330, a * kc, WHITE, 100, hl="B", hl_col=MNT)
    label(c, n_(L["confere"]), CX, 1300, a * ep(t, tc + 3.4, 0.3), 56, MNT, "black")


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 380, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        opcoes(c, 560, ka, t, ta - 1.0, certo="B", dim=1.0)
        label(c, L["conta"], CX, 1200, ka * ep(t, ta + 0.8, 0.3), 50, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 760, kb, CYA, L["aula"])
        c.save(); c.translate(CX, 600); c.scale(0.62, 0.62); c.translate(-CX, -600)
        conta(c, kb, t, CX + 60, 430, "10,00", " 9,58", res=" 0,42", novos={1: "9", 3: "9", 4: "10"}, riscos=(0, 1, 3, 4))
        c.restore()
        text_mid(c, L["passo"], CX, 900, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1020, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1046, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, pegadinha=b_pegadinha, conta=b_conta, resposta=b_resposta, final=b_final)
