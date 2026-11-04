"""Visual — Estudativo · Short 027 (vertical 1080x1920): ENEM 2025, questão 145, redes sociais e probabilidade (aula: 026).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 025 (selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras, contagem para pausar) e as peças da
aula 026 (cem(), barra(), frac(), importadas de lá). Cores: âmbar = as mulheres (o dado, 60%), ciano = os homens que acessam
(o que se pede), menta = a resposta, coral = as armadilhas, cinza vazado = quem não acessa."""
import importlib.util
from pathlib import Path

import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

_spec = importlib.util.spec_from_file_location(
    "aula026", Path(__file__).resolve().parents[2] / "026_matematica_redes_sociais_probabilidade" / "roteiro" / "visual.py")
aula = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(aula)
OPS = aula.OPS

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_027_redes_sociais_probabilidade.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "data@+2.2"], "01.b": "data", "01.c": "alert",
    "02.a": ["pop", "pop@+0.3", "pop@+0.6", "pop@+0.9", "pop@+1.2"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.07", "tick@+2.87", "tick2@+3.67"],   # tiques do cronômetro 3-2-1 (ajustados ao áudio)
    "03.a": ["impact", "deny@+0.3"], "03.b": "data", "03.c": "deny", "03.d": ["whoosh", "deny@+1.0", "confirm@+3.7"],
    "04.a": "pop", "04.b": "data", "04.c": "data", "04.d": "confirm",
    "05.a": "data", "05.b": "confirm", "05.c": ["impact", "shimmer@+0.3"],
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    chance=("WHAT ARE THE ODDS OF", "QUAL A CHANCE DE SER"), homem=("A MAN WHO USES IT?", "HOMEM QUE ACESSA?"),
    s90=("use social networks", "acessam redes sociais"), s60=("of the users are women", "de quem acessa são mulheres"),
    pede=("P(man who uses it) = ?", "P(homem que acessa) = ?"),
    qual=("WHICH FRACTION?", "QUAL FRAÇÃO?"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    armadilha=("TRAP!", "ARMADILHA!"), acessa=("who uses it", "quem acessa"), todo=("all internet users", "todos os internautas"),
    mulheres=("women", "mulheres"), homens=("men", "homens"), de_quem=("40% of the USERS", "40% de quem ACESSA"),
    so_quem=("90 below: only the users", "90 embaixo: só quem acessa"), todos=("the draw is among EVERYONE", "o sorteio é entre TODOS"),
    imagine=("IMAGINE 100", "IMAGINE 100"), c90=("90 USE IT · 10 DON'T", "90 ACESSAM · 10 NÃO"),
    c54=("60% OF 90 = 54", "60% DE 90 = 54"), c36=("90 − 54 = 36", "90 − 54 = 36"),
    l54=("54 women", "54 mulheres"), l36=("36 men", "36 homens"), l10=("10 don't", "10 não"),
    de100=("36 OUT OF 100", "36 DE 100"), direto=("40% of 90% = 0.4 × 0.9 = 0.36", "40% de 90% = 0,4 × 0,9 = 0,36"),
    letra=("ANSWER B", "LETRA B"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else (
    [(f"{matematica._extenso_pt(n)} por cento", f"{n}%") for n in (40, 60, 90)] +
    [("dois mil e vinte e cinco", "2025"), ("zero vírgula trinta e seis", "0,36")])
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
CX = W / 2
CAP_Y = 1500
GY = 880   # centro da grade dos 100 internautas


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
    words = [tk["disp"] if any(ch_.isdigit() for ch_ in tk["disp"]) else tk["disp"].upper() for tk in ch]
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


# ---------------------------------------------------------------- peças
GRADE = dict(A=(210, 730), B=(540, 730), C=(870, 730), D=(375, 1100), E=(705, 1100))
OP_W, OP_H = 290, 330


def opcao(c, le, cx, cy, a, cor=CYA, dim=0.0, marca=None, k=1.0):
    """a alternativa (fração) num cartão, com a letra no canto"""
    if a <= 0:
        return
    nu, de = next((n, d) for l_, n, d in OPS if l_ == le)
    al = a * (1 - 0.7 * dim)
    c.save(); c.translate(cx, cy); c.scale(k, k)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-OP_W / 2, -OP_H / 2, OP_W, OP_H), 22, 22)
    c.drawRRect(r, paint(BG1, 0.95 * al))
    c.drawRRect(r, paint(cor, al, stroke=6 if marca else 3))
    x0, y0 = -OP_W / 2 + 10, -OP_H / 2 + 10
    c.drawCircle(x0, y0, 36, paint(cor, al))
    text_mid(c, le, x0, y0, 42, "black", BG0, al)
    aula.frac(c, nu, de, 0, 12, 92, al, cn=WHITE, cd=WHITE, linha=cor)
    if marca == "certo":
        check(c, OP_W / 2 - 10, y0, 32, a)
    elif marca == "errado":
        cross(c, OP_W / 2 - 10, y0, 32, a)
    c.restore()


def opcoes(c, a, t, t0, certo=None, dim=0.0):
    for i, (le, (cx, cy)) in enumerate(GRADE.items()):
        k = a * pop(t, t0 + i * 0.3, 0.3)
        ok = le == certo
        opcao(c, le, cx, cy, k, MNT if ok else CYA, 0.0 if ok else dim, "certo" if ok else None)


def stat(c, num, txt, cy, cor, a, t, t0):
    """cartão de dado: número grande + o que ele conta"""
    if a <= 0:
        return
    k = pop(t, t0, 0.4)
    c.save(); c.translate(CX, cy); c.scale(k, k)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-420, -150, 840, 300), 26, 26)
    c.drawRRect(r, paint(BG1, 0.95 * a))
    c.drawRRect(r, paint(cor, a, stroke=4))
    glow_text(c, num, 0, 40, 170, "black", cor, a, glow=0.12)
    text_mid(c, txt, 0, 100, 44, "extrabold", WHITE, a)
    c.restore()


def grade(c, a, t, k=1.0, cx=CX, cy=GY, **kw):
    """os 100 internautas da aula 026, centrados em (cx, cy) e escalados por k"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(k, k)
    aula.cem(c, a, t, cx=0, cy=0, **kw)
    c.restore()


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = 1 - prog(t, B["end"] - 0.2, 0.2)
    kq = a * ep(t, ta + 0.3, 0.2)   # a pergunta já no começo (Short: pergunta nos 3 primeiros segundos)
    if kq > 0:
        k = 1 + 0.04 * math.sin(t * 8) * ep(t, tc, 0.2)
        c.save(); c.translate(CX, 340); c.scale(k, k); c.translate(-CX, -340)
        big(c, L["chance"], 290, kq, WHITE, 76)
        big(c, L["homem"], 410, kq, WHITE, 96, hl=L["homem"], hl_col=CYA)
        c.restore()
    kc = ep(t, tc, 0.3)
    stat(c, "90%", L["s90"], 680, WHITE, a * ep(t, ta + 2.2, 0.3) * (1 - 0.5 * kc), t, ta + 2.2)
    stat(c, "60%", L["s60"], 1020, AMB, a * ep(t, tb + 0.2, 0.3) * (1 - 0.5 * kc), t, tb + 0.2)
    popill(c, L["pede"], CX, 1290, 44, CYA, BG0, a * kc, t, tc + 0.2)


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    kp = a * ep(t, t0, 0.2)
    big(c, L["qual"], 290, a * (1 - kp), WHITE, 104, hl="?", hl_col=CYA)
    opcoes(c, a, t, ta + 0.1, dim=0.75 * kp)
    label(c, L["comenta"], CX, 380, a * ep(t, tb, 0.3) * (1 - kp), 46, AMB, "extrabold")
    if kp > 0:
        label(c, L["pausa"], CX, 290, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 915); c.scale(1.5, 1.5); c.translate(-CX, -915)
        contagem(c, CX, 915, kp, t, t0, 2.4)
        c.restore()


def b_pegadinha(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    stamp(c, L["armadilha"], CX, 300, RED, a * ep(t, ta + 0.2, 0.2), 76)
    kd = ep(t, td, 0.3)
    k1 = a * (1 - kd)   # primeira armadilha: C (40/100)
    opcao(c, "C", CX, 590, k1 * pop(t, ta + 0.6, 0.4), RED, marca="errado" if t >= tc else None)
    u = ep(t, tb + 0.6, 0.5)
    aula.barra(c, 140, 830, 800, 110, k1 * ep(t, tb, 0.3),
               [(0.6, AMB, "60% " + L["mulheres"], False), (0.4, aula._mix(WHITE, CYA, u), "40% " + L["homens"], False)],
               rot=L["acessa"])
    kc = k1 * ep(t, tb + 1.6, 0.4)   # a barra de todos: quem acessa é só 90% dela
    aula.barra(c, 140, 1110, 800, 110, kc, [(0.9, WHITE, L["acessa"] + " · 90%", False), (0.1, INK2, "", True)],
               rot=L["todo"])
    if kc > 0:
        c.drawLine(142, 945, 142, 1058, aula._dash(INK2, kc))
        c.drawLine(938, 945, 140 + 720, 1106, aula._dash(INK2, kc))
    label(c, L["de_quem"], CX, 1300, k1 * ep(t, tc, 0.3), 52, RED, "black")
    if kd > 0:   # segunda armadilha: A, D, E (90 embaixo)
        for i, le in enumerate("ADE"):
            ki = a * kd * pop(t, td + i * 0.25, 0.3)
            opcao(c, le, CX + (i - 1) * 320, 680, ki, RED, marca="errado" if t >= td + 1.0 else None, k=0.95)
        label(c, L["so_quem"], CX, 950, a * ep(t, td + 1.0, 0.3), 52, RED, "black")
        popill(c, L["todos"], CX, 1120, 44, CYA, BG0, a * ep(t, td + 3.7, 0.3), t, td + 3.9)


def b_conta(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    t_ac, t_gen, t_hom = tb + 1.7, tc + 2.4, td + 0.5
    grade(c, a, t, t_in=ta + 0.2, t_ac=t_ac, t_gen=t_gen, t_hom=t_hom)
    for key, t0, t1, hl, hc in (("imagine", ta, tb, "100", AMB), ("c90", tb, tc + 2.2, None, CYA),
                                ("c54", tc + 2.2, td, "54", AMB), ("c36", td, B["end"] + 1, "36", CYA)):
        k = a * ep(t, t0, 0.3) * (1 - ep(t, t1, 0.2))
        if k > 0:
            big(c, L[key], 330, k, WHITE, 92, hl=hl, hl_col=hc)
    for x, key, cor, t0 in ((210, "l54", AMB, t_gen), (540, "l36", CYA, t_hom), (870, "l10", INK2, t_ac)):
        pill(c, L[key], x, 1300, 40, cor, BG0, a * ep(t, t0 + 0.3, 0.3), "black")


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kc = a * ep(t, tc, 0.3)
    k1 = a * (1 - kc)
    sob = ep(t, ta + 2.6, 0.6)   # a grade sobe e encolhe para a fração entrar embaixo
    grade(c, k1, t, k=1 - 0.38 * sob, cy=GY - 250 * sob, t_ac=-99, t_gen=-99, t_hom=-99, foco="H",
          foco_a=ep(t, ta + 0.2, 0.4))
    big(c, L["de100"], 290, k1 * ep(t, ta + 0.2, 0.3) * (1 - sob), WHITE, 96, hl="36", hl_col=CYA)
    kf = k1 * ep(t, ta + 2.8, 0.3)
    if kf > 0:
        k = pop(t, ta + 2.8, 0.4)
        c.save(); c.translate(CX, 1030); c.scale(k, k); c.translate(-CX, -1030)
        label(c, "P =", CX - 170, 1030, kf, 96, WHITE, "black")
        aula.frac(c, "36", "100", CX + 90, 1030, 120, kf, cn=CYA, cd=WHITE, linha=MNT)
        c.restore()
    if k1 * ep(t, tb + 0.4, 0.3) > 0:
        label(c, n_(L["direto"]), CX, 1300, k1 * ep(t, tb + 0.4, 0.3), 46, MNT, "black")
    if kc > 0:
        k = pop(t, tc, 0.4)
        opcao(c, "B", CX, 860, kc, MNT, marca="certo", k=1.7 * k)
        big(c, L["letra"], 360, kc, WHITE, 120, hl="B", hl_col=MNT)


def n_(s):
    return s


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 290, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        opcoes(c, ka, t, ta - 2.0, certo="B", dim=1.0)
        label(c, L["conta"], CX, 380, ka * ep(t, ta + 0.8, 0.3), 46, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 800, kb, CYA, L["aula"])
        grade(c, kb, t, k=0.52, cy=650, t_ac=-99, t_gen=-99, t_hom=-99)
        text_mid(c, L["passo"], CX, 950, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1060, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1086, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, pegadinha=b_pegadinha, conta=b_conta, resposta=b_resposta, final=b_final)
