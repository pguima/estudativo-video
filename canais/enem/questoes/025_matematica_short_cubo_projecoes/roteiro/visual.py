"""Visual — Estudativo · Short 025 (vertical 1080x1920): ENEM 2025, questão 144, o cubo que se move no espaço (aula: 024).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 021/023 (selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras, contagem para pausar) e a cena 3D
da aula 024 (cena3d(), cubo(), sombras(), importadas de lá). Cores: âmbar = o cubo no começo (dado), ciano = a ferramenta
(o plano e a distância), menta = o cubo e as sombras no fim (a resposta), coral = a armadilha."""
import importlib.util
from pathlib import Path

import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

_spec = importlib.util.spec_from_file_location(
    "aula024", Path(__file__).resolve().parents[2] / "024_matematica_cubo_projecoes" / "roteiro" / "visual.py")
aula = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(aula)   # também desliga a regra "dois a" → "2a" da legenda (aqui é intervalo: de 2 a 3)
INI, FIM = aula.INI, aula.FIM

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_025_cubo_projecoes.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "whoosh@+1.9"], "01.b": "data", "01.c": "data", "01.d": "alert",
    "02.a": ["pop", "pop@+0.3", "pop@+0.6", "pop@+0.9", "pop@+1.2"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.79", "tick@+3.59", "tick2@+4.39"],   # tiques do cronômetro 3-2-1 (ajustados ao áudio)
    "03.a": ["impact", "deny@+0.3"], "03.b": "deny", "03.c": "confirm",
    "04.a": "data", "04.b": "whoosh", "04.c": "whoosh", "04.d": "whoosh",
    "05.a": "confirm", "05.b": "confirm", "05.c": "confirm", "05.d": ["impact", "shimmer@+0.3"],
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    onde=("WHERE DO THE", "ONDE FICAM AS"), sombras=("SHADOWS GO?", "SOMBRAS?"),
    m1=("closer to plane yz: 3", "aproxima 3 do plano yz"), m2=("away from plane xz: 5", "afasta 5 do plano xz"),
    m3=("closer to plane xy: 4", "aproxima 4 do plano xy"),
    qual=("WHICH FIGURE?", "QUAL FIGURA?"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    armadilha=("TRAP!", "ARMADILHA!"), nao=("not y, not z", "não é no y nem no z"),
    falta=("it's x: the axis MISSING from the name", "é no x: o eixo que FALTA no nome"),
    ini=("start: x 5–6 · y 1–2 · z 6–7", "início: x 5–6 · y 1–2 · z 6–7"),
    mv_x=("x: 5–6 → 2–3", "x: 5–6 → 2–3"), mv_y=("y: 1–2 → 6–7", "y: 1–2 → 6–7"), mv_z=("z: 6–7 → 2–3", "z: 6–7 → 2–3"),
    f_yz=("back wall: y 6–7 · z 2–3", "fundo: y 6–7 · z 2–3"), f_xz=("left wall: x 2–3 · z 2–3", "esquerda: x 2–3 · z 2–3"),
    f_xy=("floor: x 2–3 · y 6–7", "chão: x 2–3 · y 6–7"),
    letra=("ANSWER E", "LETRA E"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("xis ípsilon", "xy"), ("ípsilon zê", "yz"), ("xis zê", "xz"),
    ("xis", "x"), ("ípsilon", "y"), ("zê", "z"), ("dois", "2")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
CX = W / 2
CAP_Y = 1500
# a cena 3D da aula (desenhada para 1920x1080, centro ≈ (490, 578)) ampliada no meio da tela do Short
S3, C3, Y3, X3 = 1.05, (490.0, 578.0), 860.0, W / 2 + 10


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


class tela3d:
    """with tela3d(c): desenha com as coordenadas da cena 3D da aula"""
    def __init__(self, c, k=S3, y=Y3, x=X3):
        self.c, self.k, self.y, self.x = c, k, y, x

    def __enter__(self):
        self.c.save(); self.c.translate(self.x, self.y); self.c.scale(self.k, self.k); self.c.translate(-C3[0], -C3[1])

    def __exit__(self, *_):
        self.c.restore()


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
    # eixos e planos (x, y, z, xy, yz, xz) ficam em minúscula, como na prova
    words = [tk["disp"] if (any(ch_.isdigit() for ch_ in tk["disp"]) or tk["disp"].rstrip(".,:;!?") in
                            ("x", "y", "z", "xy", "yz", "xz")) else tk["disp"].upper() for tk in ch]
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


# ---------------------------------------------------------------- as cinco figuras da prova
GRADE = dict(A=(310, 595), B=(770, 595), C=(310, 925), D=(770, 925), E=(540, 1255))
FIG_W = 400


def figura(c, nome, cx, cy, a, w=FIG_W, cor=CYA, dim=0.0, marca=None):
    """a figura da alternativa (imagem da prova) num cartão branco, com a letra no canto"""
    if a <= 0:
        return
    img = aula._img(f"opcao_{nome}.png")
    h = img.height() * w / img.width()
    x, y = cx - w / 2, cy - h / 2
    k = a * (1 - 0.7 * dim)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 10, y - 10, w + 20, h + 20), 16, 16)
    c.drawRRect(r, paint("#FFFFFF", k))
    c.drawImageRect(img, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), paint(WHITE, k))
    c.drawRRect(r, paint(cor, k, stroke=5 if marca else 3))
    c.drawCircle(x + 14, y + 14, 34, paint(cor, k))
    text_mid(c, nome, x + 14, y + 14, 40, "black", BG0, k)
    if marca == "certo":
        check(c, x + w - 10, y + 14, 30, a)
    elif marca == "errado":
        cross(c, x + w - 10, y + 14, 30, a)


def figuras(c, a, t, t0, certo=None, dim=0.0, escala=1.0, oy=0.0):
    for i, (nome, (cx, cy)) in enumerate(GRADE.items()):
        k = a * pop(t, t0 + i * 0.3, 0.3)
        cy = 640 + (cy - 640) * escala + oy
        cx = CX + (cx - CX) * escala
        ok = nome == certo
        figura(c, nome, cx, cy, k, FIG_W * escala, MNT if ok else CYA, 0.0 if ok else dim, "certo" if ok else None)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td = (C[f"01.{k}"] for k in "abcd")
    a = 1 - prog(t, B["end"] - 0.2, 0.2)
    with tela3d(c):
        aula.cena3d(c, a * ep(t, ta + 0.2, 0.4))
        aula.sombras(c, INI, a * ep(t, td, 0.4), CYA)
        aula.cubo(c, INI, a * ep(t, ta + 0.4, 0.3), AMB, glow=0.5)
    kc = a * ep(t, ta + 0.3, 0.2)   # a pergunta já no começo (Short: pergunta nos 3 primeiros segundos)
    if kc > 0:
        k = 1 + 0.04 * math.sin(t * 8) * ep(t, td, 0.2)
        c.save(); c.translate(CX, 330); c.scale(k, k); c.translate(-CX, -330)
        big(c, L["onde"], 290, kc, WHITE, 100)
        big(c, L["sombras"], 410, kc, WHITE, 100, hl=L["sombras"], hl_col=CYA)
        c.restore()
    for j, (key, t0) in enumerate((("m1", ta + 1.9), ("m2", tb), ("m3", tc))):
        y = 1270 + j * 0   # um de cada vez, no mesmo lugar
        k = a * ep(t, t0, 0.25) * (1 - ep(t, (tb, tc, td, B["end"])[j], 0.2))
        pill(c, L[key], CX, y, 40, AMB, BG0, k, "black")


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    kp = a * ep(t, t0, 0.2)
    big(c, L["qual"], 290, a * (1 - kp), WHITE, 104, hl="?", hl_col=CYA)
    figuras(c, a, t, ta + 0.3, dim=0.75 * kp)
    label(c, L["comenta"], CX, 380, a * ep(t, tb, 0.3), 46, AMB, "extrabold")
    if kp > 0:
        label(c, L["pausa"], CX, 290, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 900); c.scale(1.5, 1.5); c.translate(-CX, -900)
        contagem(c, CX, 900, kp, t, t0, 2.4)
        c.restore()


def b_pegadinha(c, t, C, B):
    ta, tb, tc = (C[f"03.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    x, y, z = INI
    with tela3d(c):
        aula.cena3d(c, a, tints={"yz": (CYA, ep(t, tb, 0.3), "yz")})
        aula.cubo(c, INI, a, AMB)
        kb = a * ep(t, tb + 1.4, 0.3) * (1 - ep(t, tc, 0.3))   # o caminho errado: andar no y ou no z
        aula.seta3d(c, (x + 0.5, y, z + 0.5), (x + 0.5, 0.05, z + 0.5), kb, RED, "y?")
        aula.seta3d(c, (x + 0.5, y + 0.5, z), (x + 0.5, y + 0.5, 0.05), kb, RED, "z?")
        aula.seta3d(c, (x, y + 0.5, z + 0.5), (0.05, y + 0.5, z + 0.5), a * ep(t, tc + 0.6, 0.3), CYA, "x", w=8)
    stamp(c, L["armadilha"], CX, 320, RED, a * ep(t, ta + 0.2, 0.2), 76)
    label(c, L["nao"], CX, 1300, a * ep(t, tb + 1.4, 0.3) * (1 - ep(t, tc, 0.3)), 50, RED, "black")
    label(c, L["falta"], CX, 1300, a * ep(t, tc + 0.6, 0.3), 44, CYA, "black")


def b_movimentos(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    pos = aula.pos_mov(t, tb, tc, td, dur=1.4)
    fim = t >= td + 3.0
    with tela3d(c):
        aula.cena3d(c, a, numeros=1.0)
        aula.cubo(c, INI, a * 0.25 * ep(t, tb + 1.4, 0.3), AMB, contorno=INK2)   # onde ele estava
        aula.cubo(c, pos, a, MNT if fim else AMB, glow=0.6)
        ka = a * ep(t, ta + 0.6, 0.3) * (1 - ep(t, tb, 0.3))
        for eixo, v in zip("xyz", INI):
            aula.faixa_eixo(c, eixo, v, v + 1, ka, AMB)
        aula.faixa_eixo(c, "x", pos[0], pos[0] + 1, a * ep(t, tb, 0.3) * (1 - ep(t, tc, 0.3)), CYA)
        aula.faixa_eixo(c, "y", pos[1], pos[1] + 1, a * ep(t, tc, 0.3) * (1 - ep(t, td, 0.3)), CYA)
        aula.faixa_eixo(c, "z", pos[2], pos[2] + 1, a * ep(t, td, 0.3), CYA)
    label(c, L["ini"], CX, 320, ka, 50, AMB, "black")
    for key, op, t0, t1 in (("mv_x", "−3", tb, tc), ("mv_y", "+5", tc, td), ("mv_z", "−4", td, B["end"] + 1)):
        k = a * ep(t, t0, 0.3) * (1 - ep(t, t1, 0.2))
        if k <= 0:
            continue
        big(c, L[key], 330, k, WHITE, 90)
        popill(c, op, CX, 1290, 44, CYA if op[0] == "+" else AMB, BG0, k, t, t0 + 0.8)


def b_resposta(c, t, C, B):
    ta, tb, tc, td = (C[f"05.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ke = a * ep(t, td, 0.3)
    k3 = a * (1 - 0.8 * ke)
    with tela3d(c):
        aula.cena3d(c, k3, numeros=1.0)
        aula.sombras(c, FIM, k3, MNT, ks={"yz": ep(t, ta + 0.8, 0.4), "xz": ep(t, tb, 0.4), "xy": ep(t, tc, 0.4)})
        aula.cubo(c, FIM, k3, MNT)
    for key, t0, t1 in (("f_yz", ta + 0.8, tb), ("f_xz", tb, tc), ("f_xy", tc, td)):
        k = a * ep(t, t0, 0.3) * (1 - ep(t, t1, 0.2))
        if k > 0:
            pill(c, L[key], CX, 1290, 40, MNT, BG0, k, "black")
    if ke > 0:
        k = pop(t, td, 0.4)
        c.save(); c.translate(CX, 820); c.scale(k, k); c.translate(-CX, -820)
        figura(c, "E", CX, 820, ke, 760, MNT, marca="certo")
        c.restore()
        big(c, L["letra"], 360, ke, WHITE, 120, hl="E", hl_col=MNT)


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 290, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        figuras(c, ka, t, ta - 2.0, certo="E", dim=1.0)
        label(c, L["conta"], CX, 380, ka * ep(t, ta + 0.8, 0.3), 46, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 800, kb, CYA, L["aula"])
        with tela3d(c, 0.72, 660):
            aula.cena3d(c, kb, numeros=0.0)
            aula.sombras(c, FIM, kb, MNT)
            aula.cubo(c, FIM, kb, MNT)
        text_mid(c, L["passo"], CX, 950, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1060, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1086, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, pegadinha=b_pegadinha, movimentos=b_movimentos, resposta=b_resposta,
              final=b_final)
