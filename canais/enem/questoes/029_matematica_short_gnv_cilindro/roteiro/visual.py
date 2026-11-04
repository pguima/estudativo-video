"""Visual — Estudativo · Short 029 (vertical 1080x1920): ENEM 2025, questão 146, o cilindro de GNV (aula: 028).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 027 (big(), stamp(), contagem(), stat() e a legenda de 1 a 3 palavras, importados de lá) e as peças da aula 028
(cilindro(), cubo(), semana()). Cores: âmbar = os dados (30 km, 1 m³ a cada 13 km, a sobra), ciano = o gás, menta = o
cilindro certo, coral = os que não dão conta e a armadilha."""
import importlib.util
from pathlib import Path

import idioma
import matematica
from matematica import *  # noqa


def _carrega(nome, pasta):
    spec = importlib.util.spec_from_file_location(nome, Path(__file__).resolve().parents[2] / pasta / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


sh = _carrega("short027", "027_matematica_short_redes_sociais_probabilidade")
aula = _carrega("aula028", "028_matematica_gnv_cilindro")   # também tira "mais"/"menos" → + e − da legenda
big, stamp, contagem, stat, CAPTION = sh.big, sh.stamp, sh.contagem, sh.stat, sh.CAPTION
CX, CAP_Y = sh.CX, sh.CAP_Y

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_029_gnv_cilindro.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "data@+3.3"], "01.b": "data", "01.c": "alert",
    "02.a": ["pop", "pop@+0.5", "pop@+1.0", "pop@+1.5", "pop@+2.0"], "02.b": "notif",
    "02.c": ["alert", "tick@+1.65", "tick@+2.45", "tick2@+3.25"],   # tiques do cronômetro 3-2-1 (ajustados ao áudio)
    "03.a": "data", "03.b": "data", "03.c": ["data", "alert@+3.2"],
    "04.a": ["impact", "deny@+1.7"], "04.b": "deny", "04.c": "confirm",
    "05.a": "data", "05.b": ["deny", "confirm@+1.3"], "05.c": "confirm", "05.d": ["impact", "shimmer@+0.3"],
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    qual=("WHICH TANK", "QUAL CILINDRO"), aguenta=("LASTS THE WEEK?", "AGUENTA A SEMANA?"),
    s30=("a day · 7 days a week", "por dia · 7 dias por semana"), s13=("of gas every 13 km", "de gás a cada 13 km"),
    barato=("the cheapest one?", "o mais barato?"), qual2=("WHICH TANK?", "QUAL CILINDRO?"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    c210=("30 × 7 = 210 km", "30 × 7 = 210 km"), d13=("210 ÷ 13 = ?", "210 ÷ 13 = ?"), c208=("13 × 16 = 208", "13 × 16 = 208"),
    sob=("2 km LEFT OVER", "SOBRAM 2 km"), km13=("1 m³ → 13 km", "1 m³ → 13 km"), l208=("16 m³ = 208 km", "16 m³ = 208 km"),
    armadilha=("TRAP!", "ARMADILHA!"), nao16=("16 IS NOT ENOUGH!", "16 NÃO BASTA!"), faltam=("2 km short", "faltam 2 km"),
    arred=("left over? ROUND UP ↑", "sobrou? ARREDONDA PARA CIMA ↑"),
    mais16=("MORE THAN 16 m³", "MAIS DE 16 m³"), caros=("pricier", "mais caros"), letra=("ANSWER C", "LETRA C"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("dois quilômetros", "2 km"), ("metros cúbicos", "m³"), ("metro cúbico", "m³"), ("quilômetros", "km")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
CAPS, LETRAS = aula.CAPS, aula.LETRAS
XV = (220, 380, 540, 700, 860)
YB, KH = 1150, 24


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


def tanques(c, a, t, t0=None, cores=None, dim=None, passo=0.5, yb=YB, kh=KH):
    for i, (cap, x) in enumerate(zip(CAPS, XV)):
        k = pop(t, t0 + i * passo, 0.35) if t0 is not None else 1.0
        al = a * (1 - 0.7 * (dim or {}).get(cap, 0.0))
        aula.cilindro(c, x, yb, cap, al, (cores or {}).get(cap, WHITE), kh, letra=LETRAS[i], k=k)


def marca(c, cap, a, certo):
    x = XV[CAPS.index(cap)]
    (check if certo else cross)(c, x, YB - cap * KH - 75, 26, a)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = 1 - prog(t, B["end"] - 0.2, 0.2)
    kq = a * ep(t, ta + 0.3, 0.2)   # a pergunta já no começo
    if kq > 0:
        k = 1 + 0.04 * math.sin(t * 8) * ep(t, tc, 0.2)
        c.save(); c.translate(CX, 340); c.scale(k, k); c.translate(-CX, -340)
        big(c, L["qual"], 290, kq, WHITE, 84)
        big(c, L["aguenta"], 410, kq, WHITE, 96, hl=L["aguenta"], hl_col=CYA)
        c.restore()
    kc = ep(t, tc, 0.3)
    stat(c, "30 km", L["s30"], 680, WHITE, a * ep(t, ta + 3.3, 0.3) * (1 - 0.5 * kc), t, ta + 3.3)
    stat(c, "1 m³", L["s13"], 1020, AMB, a * ep(t, tb + 0.4, 0.3) * (1 - 0.5 * kc), t, tb + 0.4)
    popill(c, L["barato"], CX, 1290, 46, CYA, BG0, a * ep(t, tc + 0.6, 0.3), t, tc + 0.6)


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    kp = a * ep(t, t0, 0.2)
    big(c, L["qual2"], 290, a * (1 - kp), WHITE, 104, hl="?", hl_col=CYA)
    tanques(c, a, t, ta, dim={cap: 0.75 * kp for cap in CAPS})
    label(c, L["comenta"], CX, 380, a * ep(t, tb, 0.3) * (1 - kp), 46, AMB, "extrabold")
    if kp > 0:
        label(c, L["pausa"], CX, 290, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 800); c.scale(1.5, 1.5); c.translate(-CX, -800)
        contagem(c, CX, 800, kp, t, t0, 2.4)
        c.restore()


def b_conta(c, t, C, B):
    ta, tb, tc = (C[f"03.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    t_d, t_s = tb + 2.8, tc + 3.2
    for key, t0, t1, hl, hc in (("c210", ta + 1.1, t_d, "210 km", CYA), ("d13", t_d, tc, None, CYA),
                                ("c208", tc, t_s, "208", CYA), ("sob", t_s, B["end"] + 1, "2 km", AMB)):
        k = a * ep(t, t0, 0.3) * (1 - ep(t, t1, 0.2))
        if k > 0:
            big(c, L[key], 330, k, WHITE, 92, hl=hl, hl_col=hc)
    aula.semana(c, 90, 760, 900, a * (1 - ep(t, tc, 0.3)), t, ta + 0.8, km=210 * ep(t, ta + 2.2, 0.8))
    for i in range(16):   # 16 m³ = 208 km
        x, y = CX - 300 + (i % 6) * 120, 760 + (i // 6) * 150
        aula.cubo(c, x, y, 92, a, CYA, k=pop(t, tc + 1.0 + i * 0.08, 0.3), rot=None)
    aula.cubo(c, CX - 300 + 4 * 120, 1060, 92, a * ep(t, t_s, 0.3), AMB, u=2 / 13, k=pop(t, t_s, 0.35), rot=None)
    label(c, "+ 2 km", CX - 300 + 4 * 120, 1150, a * ep(t, t_s, 0.3), 36, AMB, "black")
    pill(c, L["km13"], CX, 1290, 40, AMB, BG0, a * ep(t, tb, 0.3) * (1 - ep(t, tc + 1.6, 0.2)), "black")
    pill(c, L["l208"], CX, 1290, 40, CYA, BG0, a * ep(t, tc + 1.6, 0.3), "black")


def b_pegadinha(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    stamp(c, L["armadilha"], CX, 300, RED, a * ep(t, ta + 0.2, 0.2), 76)
    big(c, L["nao16"], 520, a * ep(t, ta + 1.7, 0.3), RED, 100)
    km = 208 * ep(t, tb + 0.2, 1.4)
    aula.semana(c, 90, 760, 900, a * ep(t, ta + 1.7, 0.3), t, None, km=km)
    if km > 0:
        aula.carro(c, 90 + 900 * km / 210 - 40, 700, 120, a, CYA)
    kf = a * ep(t, tb + 1.6, 0.3)
    if kf > 0:
        xf = 90 + 900 * 208 / 210
        c.drawLine(xf, 750, xf, 880, paint(RED, kf, stroke=6, cap_round=True))
        popill(c, L["faltam"], 820, 950, 36, RED, BG0, kf, t, tb + 1.6)
    popill(c, L["arred"], CX, 1150, 40, AMB, BG0, a * ep(t, tc + 0.4, 0.3), t, tc + 0.4)


def b_resposta(c, t, C, B):
    ta, tb, tc, td = (C[f"05.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    t17 = tc + 1.6
    kd = ep(t, td, 0.3)
    cores = {}
    if t >= tb:
        cores[10] = cores[14] = RED
    if t >= tb + 1.3:
        cores[21] = cores[25] = MNT
    if t >= t17:
        cores[17] = MNT
    dim = {cap: 0.6 * ep(t, tc, 0.4) for cap in (10, 14, 21, 25)}
    tanques(c, a, t, None, cores=cores, dim=dim)
    aula.nivel_linha(c, YB - aula.PRECISA * KH, a * ep(t, ta + 0.4, 0.6), "16,2 m³" if not EN else "16.2 m³", x0=90, x1=990)
    for cap in (10, 14):
        marca(c, cap, a * ep(t, tb, 0.3) * (1 - dim[cap]), False)
    for cap in (21, 25):
        marca(c, cap, a * ep(t, tb + 1.3, 0.3) * (1 - dim[cap]), True)
    label(c, L["caros"], 780, 400, a * ep(t, tb + 2.6, 0.3) * (1 - ep(t, tc, 0.3)), 44, MNT, "black")
    marca(c, 17, a * pop(t, t17, 0.4), True)
    big(c, L["mais16"], 330, a * ep(t, ta + 0.3, 0.3) * (1 - kd), WHITE, 92, hl="16 m³", hl_col=CYA)
    big(c, L["letra"], 330, a * kd, WHITE, 120, hl="C", hl_col=MNT)


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 290, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        tanques(c, ka, t, None, cores={17: MNT}, dim={cap: 1.0 for cap in (10, 14, 21, 25)})
        marca(c, 17, ka, True)
        label(c, L["conta"], CX, 380, ka * ep(t, ta + 0.8, 0.3), 46, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 800, kb, CYA, L["aula"])
        c.save(); c.translate(CX, 0); c.scale(0.62, 0.62); c.translate(-CX, 0)
        tanques(c, kb, t, None, cores={17: MNT}, yb=1390)
        c.restore()
        text_mid(c, L["passo"], CX, 950, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1060, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1086, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, conta=b_conta, pegadinha=b_pegadinha, resposta=b_resposta, final=b_final)
