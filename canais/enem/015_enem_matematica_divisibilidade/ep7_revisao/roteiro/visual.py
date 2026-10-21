"""Visual — Divisibilidade, Primos, MMC e MDC, Episódio 7: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Estrutura técnica da revisão da Redação (014 ep6): V ou F com selo PEGADINHA, questões inéditas com quadro "lembrando",
cronômetro nas pausas, checklist de domínio agrupado por episódio.
Peças próprias: os 6 ÍCONES dos episódios (retângulo de quadradinhos · tijolo · receita · ônibus · régua · placa
"repete × reparte") como índice visual; linha de alternativas em chips; régua MDC ≤ menor ≤ maior ≤ MMC em miniatura.
Texto matemático com expoente ^: ftext/fmid do ep. 1 da série 010. Pausa e selo: Redação 014 ep1.
Cores: azul = definição · roxo = regra · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_ROOT = Path(__file__).resolve().parents[3]          # canais/enem


def _load(nome, rel):
    sp = importlib.util.spec_from_file_location(nome, _ROOT / rel)
    mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
    return mod


M = _load("v010_ep1", "010_enem_matematica_conjuntos/ep1_ordem_e_sinais/roteiro/visual.py")      # ftext (expoente ^)
V1 = _load("v014_ep1", "014_enem_redacao_leitura_proposta/ep1_o_que_a_prova_pede/roteiro/visual.py")  # pausa, selo
motor.set_theme("claro")

ftext, fmid, ftext_w = M.ftext, M.fmid, M.ftext_w
pause_timer, which, para, frame, head_seq, boxed, selo = (V1.pause_timer, V1.which, V1.para, V1.frame, V1.head_seq,
                                                         V1.boxed, V1.selo)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisibilidade_ep7_revisao.mp4"
CARD_R = (140, 150, 1640, 690)
DIDATICO = "Situação elaborada para fins didáticos."
BRICK = "#C8553D"
ORANGE = "#F97316"


# ======================================================================
# os 6 ícones dos episódios (índice visual)
# ======================================================================

def ic_quadradinhos(c, cx, cy, s, a, col):
    for i in range(4):
        for j in range(3):
            rrect(c, cx - 30 * s + i * 15.5 * s, cy - 22 * s + j * 15.5 * s, 13 * s, 13 * s, 2.5 * s, col, a)


def ic_tijolo(c, cx, cy, s, a, col):
    for j, off in enumerate((0, 1, 0)):
        for i in range(2 if off else 2):
            x = cx - 32 * s + i * 34 * s + off * 17 * s
            if off and i == 1:
                continue
            rrect(c, x, cy - 24 * s + j * 17 * s, 30 * s, 14 * s, 2 * s, col, a)
    rrect(c, cx - 32 * s, cy - 7 * s, 13 * s, 14 * s, 2 * s, col, a)
    rrect(c, cx + 19 * s, cy - 7 * s, 13 * s, 14 * s, 2 * s, col, a)


def ic_receita(c, cx, cy, s, a, col):
    rrect(c, cx - 24 * s, cy - 30 * s, 48 * s, 60 * s, 5 * s, "#FFFFFF", a, stroke=3 * s, stroke_color=col)
    ftext(c, "2^3·3", cx, cy - 6 * s, 15 * s, "black", col, a)
    for k in range(2):
        line(c, cx - 15 * s, cy + 6 * s + k * 10 * s, cx + 15 * s - k * 8 * s, cy + 6 * s + k * 10 * s, LIGHT, a, 3 * s)


def ic_onibus(c, cx, cy, s, a, col):
    rrect(c, cx - 32 * s, cy - 20 * s, 64 * s, 34 * s, 7 * s, col, a)
    for k in range(3):
        rrect(c, cx - 26 * s + k * 18 * s, cy - 15 * s, 14 * s, 12 * s, 2 * s, "#DCEBFF", a)
    for wx in (cx - 18 * s, cx + 18 * s):
        c.drawCircle(wx, cy + 16 * s, 6.5 * s, paint(INK, a))


def ic_regua(c, cx, cy, s, a, col):
    c.save(); c.translate(cx, cy); c.rotate(-20)
    rrect(c, -36 * s, -11 * s, 72 * s, 22 * s, 4 * s, col, a)
    for k in range(9):
        hh = 9 * s if k % 2 == 0 else 5 * s
        line(c, -30 * s + k * 7.5 * s, -11 * s, -30 * s + k * 7.5 * s, -11 * s + hh, "#FFFFFF", a, 2 * s)
    c.restore()


def ic_placa(c, cx, cy, s, a, col):
    rrect(c, cx - 3 * s, cy - 18 * s, 6 * s, 50 * s, 2 * s, INK2, a)
    for k, (dx, cc) in enumerate(((-1, ORANGE), (1, GREEN))):
        y = cy - 22 * s + k * 18 * s
        p = skia.Path()
        x0, x1 = cx - 2 * s * dx, cx + 30 * s * dx
        p.moveTo(x0, y - 7 * s); p.lineTo(x1, y - 7 * s); p.lineTo(x1 + 7 * s * dx, y); p.lineTo(x1, y + 7 * s)
        p.lineTo(x0, y + 7 * s); p.close()
        c.drawPath(p, paint(cc, a))


ICONES = [(ic_quadradinhos, "divisores", BLUE), (ic_tijolo, "primos", BRICK), (ic_receita, "fatoração", PURPLE),
          (ic_onibus, "MMC", ORANGE), (ic_regua, "MDC", GREEN), (ic_placa, "decisão", AMBER)]


def icone(c, k, cx, cy, a, s=1.0, lit=True, label=True):
    if a <= 0:
        return
    fn, nm, col = ICONES[k]
    col_ = col if lit else LIGHT
    c.drawCircle(cx, cy, 48 * s, paint(mix("#FFFFFF", col_, 0.14), a))
    fn(c, cx, cy, s, a, col_)
    if label:
        text(c, f"EP. {k + 1}", cx, cy + 76 * s, 18 * s, "black", col_ if lit else GRAY, a, tracking=2)


def indice(c, a, cx, y, s=0.62, gap=112, lit=None, label=False):
    x0 = cx - gap * 2.5
    for k in range(6):
        icone(c, k, x0 + k * gap, y, a, s, lit is None or lit == k, label)


# ======================================================================
# abertura, como o ENEM cobra, mapa da série
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM · REVISÃO", "ESSE PONTO JÁ É SEU?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    text(c, "questão própria", W / 2, 270, 64, "black", INK, aa)
    text(c, "quase todo ano", W / 2, 330, 34, "bold", GRAY, aa)
    ab = ep(t, C["01.b"], 0.5)
    for k, (nm, sub, ic, col) in enumerate((("REPETE", "MMC", 3, ORANGE), ("REPARTE", "MDC", 4, GREEN))):
        x = 520 + k * 880 - 260
        a = ep(t, C["01.b"] + 0.4 * k, 0.4)
        rrect(c, x, 400, 520, 200, 22, mix("#FFFFFF", col, 0.10), a, shadow=True)
        icone(c, ic, x + 100, 500, a, 1.1, label=False)
        text(c, nm, x + 330, 490, 48, "black", col, a)
        text(c, sub, x + 330, 550, 34, "black", INK2, a)
    text(c, "um de dois", W / 2, 520, 36, "black", PURPLE, ab)
    indice(c, ep(t, C["01.c"], 0.5), W / 2, 740)


def b_cobra(c, t, C, B):
    head_seq(c, t, C, [("02", "TESTE DE MEMÓRIA", "QUAIS SÃO OS 2 FORMATOS?", PURPLE), ("03", "COMO O ENEM COBRA", "SEMPRE UM DE DOIS", PURPLE)])
    card(c, *CARD_R)
    if t < C["03"] - 0.05:
        a = ep(t, C["02.a"], 0.5)
        for k in range(2):
            rrect(c, 360 + k * 660, 280, 540, 260, 22, "#F4F5F7", a)
            text_mid(c, "?", 630 + k * 660, 410, 120, "black", LIGHT, a)
        pause_timer(c, t, C["02.p"] + 0.4, W / 2, 680)
        return
    cards = [("03.a", "MMC", "coisas que se REPETEM e voltam a coincidir", "ônibus · lâmpadas · remédios", 3, ORANGE),
             ("03.b", "MDC", "REPARTIR em pedaços iguais, do maior tamanho", "tábuas · grupos · estacas", 4, GREEN)]
    for k, (cue, nm, s1, s2, ic, col) in enumerate(cards):
        a, d = rise(t, C[cue])
        x = 220 + k * 760
        rrect(c, x, 210 + d, 720, 330, 22, mix("#FFFFFF", col, 0.08), a, shadow=True)
        icone(c, ic, x + 90, 300 + d, a, 1.0, label=False)
        text(c, nm, x + 170, 320 + d, 60, "black", col, a, align="left")
        para(c, s1, x + 40, 420 + d, 30, "black", INK, a, 640, 36)
        text(c, s2, x + 40, 515 + d, 26, "bold", GRAY, a, align="left")
    ac = ep(t, C["03.c"], 0.5)
    text(c, "COM MENOR FREQUÊNCIA", 220, 620, 20, "black", GRAY, ac, align="left", tracking=2)
    for k, s in enumerate(("critérios em código e senha", "contagem de divisores", "fatoração como ferramenta")):
        pill(c, s, 220 + k * 470, 680, BLUE, size=26, a=ep(t, C["03.c"] + 0.8 * k, 0.4), bounds=(0, 1920))


MAPA = [("04.a", 0, "divisores", "retângulos"), ("04.a", 0, "critério", "teste rápido"),
        ("04.b", 1, "primos", "tijolos"), ("04.c", 2, "fatoração", "receita do número"),
        ("04.c", 2, "contar divisores", "montar um lanche"), ("04.d", 3, "MMC", "o reencontro"),
        ("04.e", 4, "MDC", "a maior régua"), ("04.f", 5, "decisão", "repete ou reparte?")]


def b_mapa(c, t, C, B):
    frame(c, t, B["start"], "AS IMAGENS DA SÉRIE", "O MAPA DA REVISÃO", PURPLE)
    for k, (cue, ic, s1, s2) in enumerate(MAPA):
        a, d = rise(t, C[cue] + (0.9 if k in (1, 4) else 0))
        x = 210 + (k % 4) * 380
        y = 200 + (k // 4) * 310 + d
        rrect(c, x, y, 350, 280, 20, "#FFFFFF", a, shadow=True)
        icone(c, ic, x + 175, y + 85, a, 0.85, label=False)
        text(c, s1, x + 175, y + 185, 28, "black", INK, a)
        text(c, s2, x + 175, y + 235, 28, "black", ICONES[ic][2], a)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

VF = [("05", "O 1 é primo.", False, "só é dividido por 1 e por ele mesmo",
       "primo tem exatamente dois divisores; o 1 tem só um", 1),
      ("06", "O 2 é primo, e é o único primo par.", True, "parece que par não pode ser primo",
       "seus divisores são 1 e 2: exatamente dois", 1),
      ("07", "No MDC, pegue o MAIOR expoente de cada fator.", False, "no MMC é o maior",
       "no MDC é o menor: o divisor comum precisa caber nos dois", 4),
      ("08", "No MMC, entram TODOS os fatores, com o maior expoente.", True, "a pegadinha é usar só os comuns",
       "o múltiplo comum precisa conter cada número inteiro", 3),
      ("09", "Achou o MMC: a questão de “quantas vezes” está respondida.", False, "a conta difícil já foi feita",
       "quantidade num intervalo: ainda falta dividir pelo MMC", 3),
      ("10", "2^3 · 3^2 · 5 tem 24 divisores.", True, "quem multiplica só os expoentes acha 3 · 2 · 1 = 6",
       "(3+1)(2+1)(1+1) = 24: cada expoente pode valer zero", 2),
      ("11", "MDC · MMC = a · b · c, mesmo com três números.", False, "funciona direitinho com dois",
       "só vale para dois: com três, a igualdade não se sustenta", 5),
      ("12", "O 0 é divisor de todo número.", False, "o 0 aparece em toda tabuada",
       "é múltiplo de qualquer número, nunca divisor: divisão por zero não existe", 0),
      ("13", "Cerca de 24 m × 60 m: perímetro de 168 m.", True, "somar só 24 + 60 = 84 e parar",
       "2 · (24 + 60) = 168: o retângulo tem quatro lados", 4)]


def b_vf(c, t, C, B):
    ids = [v[0] for v in VF]
    sid = which(t, C, ids)
    n = ids.index(sid)
    _, frase, ok, engana, regra_, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    for k in range(9):
        badge_num(c, k + 1, 600 + k * 90, 205, 1, 20, bg=AMBER if k == n else (INK2 if k < n else LIGHT))
    q = lambda x: C[f"{sid}.{x}"]
    aq, d = rise(t, q("q"))
    icone(c, ic, 290, 360 + d, aq, 0.9, label=False)
    s = frase if "“" in frase or "^" in frase else "“" + frase + "”"
    if "^" in s:
        ftext(c, "“" + s + "”", 380, 375 + d, 48, "black", INK, aq, align="left")
    else:
        para(c, s, 380, 350 + d, 46, "black", INK, aq, 1180, 56)
    pause_timer(c, t, q("p") + 0.3, 1540, 560)
    ar = ep(t, q("r"), 0.4)
    if ar > 0:
        selo(c, 520, 560, ar, "VERDADEIRO" if ok else "FALSO", GREEN if ok else RED, -6, 56)
    aw = ep(t, q("w"), 0.4)
    if aw > 0:
        selo(c, 950, 560, aw, "PEGADINHA", AMBER, 4, 30)
        para(c, engana, 1100, 548, 26, "bold", INK2, aw, 520, 30)
    ak = ep(t, q("k"), 0.4)
    if ak > 0:
        rrect(c, 260, 690, 1400, 100, 18, mix("#FFFFFF", GREEN, 0.10), ak)
        check_icon(c, 310, 740, 26, ak, GREEN)
        fmid(c, regra_, 990, 740, 32, "black", GREEN, ak)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

def alt_row(c, t, C, alts, okL, ok_cue, x0=800, y=270, w=920):
    """5 chips lado a lado; errados riscados com o porquê embaixo; o certo acende em verde"""
    gap = w / 5
    aok = ep(t, C[ok_cue], 0.4)
    for k, (L, val, cin, cx_, why) in enumerate(alts):
        a = ep(t, C[cin], 0.35)
        if a <= 0:
            continue
        cx = x0 + gap * k + gap / 2
        good = L == okL and aok > 0
        ax = ep(t, C[cx_], 0.4) if cx_ else 0
        col = GREEN if good else (mix(INK, LIGHT, 0.6 * ax))
        rrect(c, cx - gap / 2 + 8, y - 50, gap - 16, 100, 16, mix("#FFFFFF", GREEN, 0.18) if good else "#FFFFFF", a, shadow=True)
        badge_num(c, L, cx - gap / 2 + 34, y - 26, a, 16, bg=GREEN if good else INK2)
        fmid(c, val, cx + 10, y + 6, 40 if len(val) <= 3 else 26, "black", col, a)
        if ax > 0:
            line(c, cx - gap / 2 + 26, y + 8, cx + gap / 2 - 26, y + 8, RED, ax, 5)
            para(c, why, cx, y + 80, 17, "bold", RED, ax, gap - 20, 21, align="center")


def regua_mini(c, x, y, w, a, menor, maior, valor, tipo):
    """MDC ≤ menor ≤ maior ≤ MMC, com o resultado encaixado (verde) ou fora do lugar (vermelho)"""
    if a <= 0:
        return
    line(c, x, y, x + w, y, LIGHT, a, 6)
    pts = [(x + w * 0.12, "MDC"), (x + w * 0.38, f"{menor}"), (x + w * 0.62, f"{maior}"), (x + w * 0.88, "MMC")]
    for px, lb in pts:
        c.drawCircle(px, y, 9, paint(INK2, a))
        text(c, lb, px, y + 40, 22, "black", INK2, a)
    text(c, "≤", x + w * 0.25, y + 40, 22, "black", GRAY, a)
    text(c, "≤", x + w * 0.50, y + 40, 22, "black", GRAY, a)
    text(c, "≤", x + w * 0.75, y + 40, 22, "black", GRAY, a)
    px = x + w * (0.12 if tipo == "MDC" else 0.88)
    c.drawCircle(px, y, 22, paint(GREEN, a))
    text_mid(c, str(valor), px, y - 46, 30, "black", GREEN, a)


def lembra(c, t, C, cue, ic, s):
    ar = ep(t, C[cue], 0.4)
    icone(c, ic, 230, 245, ar, 0.7, label=False)
    pill(c, "LEMBRANDO", 300, 220, PURPLE, size=18, a=ar, bounds=(0, 1920))
    para(c, s, 300, 272, 22, "black", PURPLE, ar, 420, 26)


def situacao(c, t, C, cue, linhas, y0=360):
    aa = ep(t, C[cue], 0.4)
    text(c, "SITUAÇÃO", 190, y0, 16, "black", GRAY, aa, align="left", tracking=2)
    y = y0 + 44
    for s, col in linhas:
        ftext(c, s, 190, y, 26, "black", col, aa, align="left")
        y += 40
    text(c, DIDATICO, 190, y + 4, 15, "medium", AMBER, aa, align="left")
    return y


def passos(c, t, C, rows, x=820, y=470, lh=58, size=30):
    for cue, s, col in rows:
        a, d = rise(t, C[cue])
        ftext(c, s, x, y + d, size, "black", col, a, align="left")
        y += lh


def varal_calc(nums):
    """linhas da decomposição simultânea: [(números, primo, dividiu todos?)]"""
    rows, n = [], list(nums)
    while any(v > 1 for v in n):
        p = min(q for q in (2, 3, 5, 7, 11, 13) if any(v % q == 0 and v > 1 for v in n))
        rows.append((n[:], p, all(v % p == 0 for v in n)))
        n = [v // p if v % p == 0 else v for v in n]
    rows.append((n[:], None, False))
    return rows


def varal_mini(c, x, y, nums, a, reveal=1.0, mark=0.0, size=30, lh=44, colw=None):
    """varal curto: números à esquerda, primo à direita; mark acende (verde) os primos que dividiram todos"""
    if a <= 0:
        return 0
    rows = varal_calc(nums)
    colw = colw or (len(nums) * size * 1.6)
    n_show = reveal * len(rows)
    line(c, x + colw + 14, y - size * 0.9, x + colw + 14, y + (len(rows) - 1) * lh + size * 0.3, INK2, a, 3)
    for k, (ns, p, todos) in enumerate(rows):
        ak = a * clamp(n_show - k)
        if ak <= 0:
            break
        yy = y + k * lh
        text(c, ", ".join(str(v) for v in ns), x + colw, yy, size, "black", INK, ak, align="right")
        if p:
            if todos and mark > 0:
                c.drawCircle(x + colw + 46, yy - size * 0.35, size * 0.72, paint(GREEN, ak * mark * 0.22))
                c.drawCircle(x + colw + 46, yy - size * 0.35, size * 0.72, paint(GREEN, ak * mark, stroke=3))
            text(c, str(p), x + colw + 46, yy, size, "black", GREEN if (todos and mark > 0.5) else PURPLE, ak)
    return len(rows) * lh


def qhead(c, t, C, sid, n, sub):
    head(c, t, C[sid], f"QUESTÃO {n} · INÉDITA", sub, BLUE)
    card(c, *CARD_R)


ALT1 = [("A", "1", "14.A", "15.xa", "soma 15: serve para o 3"), ("B", "4", "14.B", None, ""),
        ("C", "7", "14.C", "15.xa", "soma 21: serve para o 3"), ("D", "9", "14.D", "15.xd", "algarismo ≠ divisor"),
        ("E", "nenhum", "14.E", "15.xe", "não testou")]


def b_q1(c, t, C, B):
    qhead(c, t, C, "14", 1, "CRITÉRIO DE DIVISIBILIDADE")
    lembra(c, t, C, "14.r", 0, "critério = teste rápido · 9: some os algarismos")
    situacao(c, t, C, "14.a", [("código do cofre:", INK2), ("2  7  x  1  4", BLUE), ("divisível por 9", INK)])
    alt_row(c, t, C, ALT1, "B", "15.ok")
    passos(c, t, C, [("15.t", "2 + 7 + 1 + 4 = 14", INK), ("15.s", "14 + x = 18  →  x = 4", GREEN)])
    pause_timer(c, t, C["14.end"] - 1.9, 460, 790)


ALT2 = [("A", "4", "16.A", "17.xa", "expoentes sem +1"), ("B", "5", "16.B", "17.xb", "+1 só no primeiro"),
        ("C", "6", "16.C", "17.xc", "somou os expoentes"), ("D", "10", "16.D", "17.xd", "esqueceu o 7"),
        ("E", "20", "16.E", None, "")]


def b_q2(c, t, C, B):
    qhead(c, t, C, "16", 2, "CONTAGEM DE DIVISORES")
    lembra(c, t, C, "16.r", 2, "fatoração = receita · divisores = montar um lanche")
    situacao(c, t, C, "16.a", [("336 cadeiras em filas iguais", INK), ("336 = 2^4 · 3 · 7", BLUE), ("quantas filas possíveis?", INK2)])
    alt_row(c, t, C, ALT2, "E", "17.ok")
    passos(c, t, C, [("17.t", "cada fila possível = um divisor", INK2), ("17.s", "(4+1)(1+1)(1+1) = 5 · 2 · 2 = 20", GREEN)])
    pause_timer(c, t, C["16.end"] - 1.9, 460, 790)


def decisao(c, t, C, cue, tipo, x=820, y=440):
    a = ep(t, C[cue], 0.4)
    col = ORANGE if tipo == "REPETE" else GREEN
    pill(c, f"{tipo} → {'MMC' if tipo == 'REPETE' else 'MDC'}", x, y, col, size=26, a=a, bounds=(0, 1920))


def b_varal(c, t, C, B):
    frame(c, t, B["start"], "O ATALHO DA SÉRIE", "UM VARAL, DOIS RESULTADOS", GREEN)
    aa = ep(t, C["17b.a"], 0.5)
    pill(c, "fatore TODOS os números juntos", 330, 230, GREEN, size=28, a=aa, bounds=(0, 1920))
    ab = ep(t, C["17b.b"], 0.5)
    para(c, "divida pelo menor primo que dividir algum deles · quem não divide, desce igual", 330, 300, 26, "bold", INK2, ab, 640, 32)
    ac = ep(t, C["17b.c"], 0.4)
    varal_mini(c, 380, 450, (6, 10), ac, prog(t, C["17b.c"] + 0.8, 4.5), ep(t, C["17b.e"], 0.5), size=48, lh=72, colw=170)
    ad = ep(t, C["17b.d"], 0.5)
    rrect(c, 1000, 300, 620, 170, 20, mix("#FFFFFF", ORANGE, 0.10), ad, shadow=True)
    text(c, "MMC = TODOS os primos", 1310, 360, 30, "black", ORANGE, ad)
    ftext(c, "2 · 3 · 5 = 30", 1310, 425, 40, "black", INK, ad)
    ae = ep(t, C["17b.e"], 0.5)
    rrect(c, 1000, 510, 620, 170, 20, mix("#FFFFFF", GREEN, 0.10), ae, shadow=True)
    text(c, "MDC = só os que dividiram TODOS", 1310, 570, 30, "black", GREEN, ae)
    ftext(c, "2", 1310, 635, 40, "black", INK, ae)
    pill(c, "um varal, dois resultados", W / 2, 780, GREEN, size=30, a=ep(t, C["17b.f"], 0.4), anchor="center")


ALT3 = [("A", "5", "18.A", None, ""), ("B", "6", "18.B", "19.xb", "é o MDC"),
        ("C", "10", "18.C", "19.xc", "um farol só"), ("D", "30", "18.D", "19.xd", "dividiu pelo MDC"),
        ("E", "36", "18.E", "19.xe", "parou no MMC")]


def b_q3(c, t, C, B):
    qhead(c, t, C, "18", 3, "MMC E O “QUANTAS VEZES”")
    lembra(c, t, C, "18.r", 3, "MMC = o reencontro")
    situacao(c, t, C, "18.a", [("faróis: a cada 12 s e 18 s", INK), ("juntos agora", INK2), ("quantas vezes em 3 min?", BLUE)])
    alt_row(c, t, C, ALT3, "A", "19.ok")
    decisao(c, t, C, "19.d", "REPETE")
    varal_mini(c, 840, 520, (12, 18), ep(t, C["19.s"], 0.4), prog(t, C["19.s"] + 0.6, 3.2), ep(t, C["19.xb"], 0.5), size=28, lh=40)
    passos(c, t, C, [("19.m", "MMC = 2·2·3·3 = 36 s", ORANGE), ("19.u", "180 s ÷ 36 = 5", GREEN)], x=1180, y=600, lh=56, size=30)
    pill(c, "MDC = 2·3 = 6 (dividiram os dois)", 1180, 760, GREEN, size=20, a=ep(t, C["19.xb"], 0.4), bounds=(0, 1920))
    regua_mini(c, 1180, 480, 520, ep(t, C["19.g"], 0.4) * (1 - ep(t, C["19.u"], 0.3)), 12, 18, 36, "MMC")
    pause_timer(c, t, C["18.end"] - 1.9, 460, 790)


ALT4 = [("A", "6", "20.A", "21.xa", "parou no MDC"), ("B", "13", "20.B", "21.xb", "não dobrou o perímetro"),
        ("C", "26", "20.C", None, ""), ("D", "27", "20.D", "21.xd", "+1 na figura fechada"),
        ("E", "240", "20.E", "21.xe", "usou o MMC")]


def terreno(c, x, y, w, h, a, n_lado=(5, 8), u=1.0):
    """retângulo com estacas aparecendo pelo perímetro (u = fração já colocada)"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint(mix("#FFFFFF", GREEN, 0.12), a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint(GREEN, a, stroke=4))
    pts = []
    nx, ny = n_lado[1], n_lado[0]
    for i in range(nx):
        pts.append((x + w * i / nx, y))
    for j in range(ny):
        pts.append((x + w, y + h * j / ny))
    for i in range(nx):
        pts.append((x + w - w * i / nx, y + h))
    for j in range(ny):
        pts.append((x, y + h - h * j / ny))
    k_on = int(len(pts) * clamp(u) + 0.001)
    for k, (px, py) in enumerate(pts[:k_on]):
        c.drawCircle(px, py, 7, paint(BRICK, a))


def b_q4(c, t, C, B):
    qhead(c, t, C, "20", 4, "MDC E A QUANTIDADE")
    lembra(c, t, C, "20.r", 4, "MDC = a maior régua")
    y = situacao(c, t, C, "20.a", [("terreno de 30 m × 48 m", INK), ("estacas iguais, a maior distância", INK2), ("quantas estacas?", BLUE)])
    alt_row(c, t, C, ALT4, "C", "21.ok")
    decisao(c, t, C, "21.d", "REPARTE")
    a_var = ep(t, C["21.s"], 0.4) * (1 - ep(t, C["21.pe"], 0.4))
    varal_mini(c, 840, 500, (30, 48), a_var, prog(t, C["21.s"] + 0.3, 2.5), ep(t, C["21.s"] + 1.6, 0.5), size=24, lh=34)
    passos(c, t, C, [("21.m", "MDC = 2·3 = 6 m", GREEN)], x=1260, y=780, size=30)
    regua_mini(c, 1180, 480, 520, ep(t, C["21.g"], 0.4) * (1 - ep(t, C["21.pe"], 0.3)), 30, 48, 6, "MDC")
    ap = ep(t, C["21.pe"], 0.4)
    if ap > 0:
        pill(c, "PERÍMETRO = a volta inteira (soma dos lados)", 820, 505, BLUE, size=22, a=ap, bounds=(0, 1920))
        ftext(c, "retângulo: 2 · (comprimento + largura)", 820, 575, 26, "black", PURPLE, ap, align="left")
        ftext(c, "2 · (30 + 48) = 156 m", 820, 640, 30, "black", INK, ep(t, C["21.u"], 0.4), align="left")
        ftext(c, "156 ÷ 6 = 26 estacas", 820, 700, 30, "black", GREEN, ep(t, C["21.v"], 0.4), align="left")
    au = ep(t, C["21.pe"], 0.4)
    tx, ty, tw, th = 260, y + 70, 320, 200
    terreno(c, tx, ty, tw, th, au, (5, 8), prog(t, C["21.v"], 4.0))
    if au > 0:
        text(c, "48 m", tx + tw / 2, ty - 14, 22, "black", INK2, au)
        text(c, "30 m", tx - 14, ty + th / 2 + 8, 22, "black", INK2, au, align="right")
        pr = prog(t, C["21.pe"] + 0.6, 3.0)
        per = 2 * (tw + th); d = per * pr
        segs = [(tx, ty, tx + tw, ty), (tx + tw, ty, tx + tw, ty + th), (tx + tw, ty + th, tx, ty + th), (tx, ty + th, tx, ty)]
        for (x0, y0, x1, y1) in segs:
            L = abs(x1 - x0) + abs(y1 - y0)
            f = clamp(d / L); d -= L
            if f <= 0:
                break
            line(c, x0, y0, x0 + (x1 - x0) * f, y0 + (y1 - y0) * f, BLUE, au, 8)
    pause_timer(c, t, C["20.end"] - 1.9, 460, 790)


ALT5 = [("A", "3", "22.A", "23.xa", "nº de caixas"), ("B", "4", "22.B", "23.xb", "MDC: 4 < 12"),
        ("C", "20", "22.C", "23.xc", "somou"), ("D", "24", "22.D", None, ""),
        ("E", "96", "22.E", "23.xe", "comum, não o menor")]


def b_q5(c, t, C, B):
    qhead(c, t, C, "22", 5, "A DECISÃO DISFARÇADA")
    lembra(c, t, C, "22.r", 5, "na dúvida: repete ou reparte?")
    situacao(c, t, C, "22.a", [("copos: caixas de 8", INK), ("pratos: caixas de 12", INK), ("mesma quantidade, sem sobrar", BLUE)])
    alt_row(c, t, C, ALT5, "D", "23.ok")
    ad = ep(t, C["23.d"], 0.4)
    pill(c, "“sem sobrar” parece MDC...", 820, 440, AMBER, size=24, a=ad * (1 - ep(t, C["23.s"], 0.3)), bounds=(0, 1920))
    decisao(c, t, C, "23.s", "REPETE")
    passos(c, t, C, [("23.d", "8, 16, 24 · 12, 24", INK2)], y=520)
    varal_mini(c, 840, 600, (8, 12), ep(t, C["23.v"], 0.4), prog(t, C["23.v"] + 0.6, 3.0), ep(t, C["23.xb"], 0.5), size=26, lh=38)
    passos(c, t, C, [("23.m", "MMC = 2·2·2·3 = 24", ORANGE)], x=1180, y=640, size=30)
    pill(c, "MDC = 2·2 = 4 (dividiram os dois)", 1180, 760, GREEN, size=20, a=ep(t, C["23.xb"], 0.4), bounds=(0, 1920))
    regua_mini(c, 1180, 480, 520, ep(t, C["23.m"], 0.4), 8, 12, 24, "MMC")
    pause_timer(c, t, C["22.end"] - 1.9, 460, 790)


# ======================================================================
# checklist de domínio, meta
# ======================================================================

DOM = [("25.e1", 0, ["múltiplo × divisor (divisores acabam)", "critérios do 2, 3, 4, 5, 6, 9 e 10"]),
       ("25.e2", 1, ["o 1 não é primo; o 2 é o único par", "os 25 primos até 100", "testar pela raiz quadrada"]),
       ("25.e3", 2, ["fatorar em primos", "contar divisores: +1 em cada expoente"]),
       ("26.e4", 3, ["MMC: fatoração e decomposição", "o último passo do “quantas vezes”"]),
       ("26.e5", 4, ["MDC: fatoração e Euclides"]),
       ("26.e6", 5, ["decidir entre MMC e MDC", "a régua MDC ≤ menor ≤ maior ≤ MMC", "MDC · MMC = a · b só para dois"])]


def b_dominio(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE SABE EXPLICAR", PURPLE)
    a0 = ep(t, C["24.a"], 0.5)
    if t < C["25"] - 0.05:
        boxed(c, 300, 300, 1320, 170, PURPLE, a0, 0.07)
        text(c, "só o que você explicaria EM VOZ ALTA", W / 2, 370, 40, "black", PURPLE, a0)
        text(c, "para outra pessoa, sem consultar nada", W / 2, 430, 32, "bold", INK2, a0)
        pill(c, "não marcou? reveja o episódio correspondente", W / 2, 580, AMBER, size=30, a=ep(t, C["24.b"], 0.4), anchor="center")
        indice(c, ep(t, C["24.b"], 0.5), W / 2, 720, 0.7, 130)
        return
    cols = [(0, 1, 2), (3, 4, 5)]
    for ci, idxs in enumerate(cols):
        y = 190
        for i in idxs:
            cue, ic, itens = DOM[i]
            a = ep(t, C[cue], 0.4)
            x = 190 + ci * 790
            icone(c, ic, x + 40, y + 40, a, 0.6, label=False)
            text(c, f"EPISÓDIO {i + 1}", x + 100, y + 30, 18, "black", ICONES[ic][2], a, align="left", tracking=2)
            for j, s in enumerate(itens):
                yy = y + 70 + j * 40
                rrect(c, x + 100, yy - 22, 26, 26, 6, "#FFFFFF", a, stroke=2.5, stroke_color=INK2)
                text(c, s, x + 140, yy, 24, "bold", INK, a * ep(t, C[cue] + 0.4 * j, 0.3), align="left")
            y += 70 + len(itens) * 40 + 16


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE MARCAR “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["27.a"], 0.5)
    text(c, "30 questões", W / 2, 320, 80, "black", INK, aa)
    ab = ep(t, C["27.b"], 0.5)
    x0, w = 360, 1200
    for k in range(30):
        on_ = k < 21
        col = GREEN if on_ else LIGHT
        rrect(c, x0 + k * w / 30 + 3, 400, w / 30 - 6, 70, 6, col, aa * (ep(t, C["27.b"] + 0.05 * k, 0.2) if on_ else 1))
    text(c, "pelo menos 21 acertos = 70%", W / 2, 540, 44, "black", GREEN, ab)
    pill(c, "priorize MMC e MDC contextualizadas: são as que caem", W / 2, 660, PURPLE, size=28, a=ep(t, C["27.c"], 0.4), anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO ASSUNTO", "FRAÇÕES, DECIMAIS E DÍZIMAS", BLUE)
    aa = ep(t, C["28.a"], 0.5)
    text(c, "Frações, decimais e dízimas", W / 2, 280, 52, "black", BLUE, aa)
    ab = ep(t, C["28.b"], 0.5)
    icone(c, 3, 560, 470, ab, 1.4, label=False)
    text(c, "o MMC daqui", 560, 600, 32, "black", ORANGE, ab)
    ac = ep(t, C["28.c"], 0.5)
    arrow(c, 720, 470, 900, 470, ORANGE, ac, 6, 20, progress=ac)
    rrect(c, 940, 380, 620, 200, 20, "#FFFFFF", ac, shadow=True)
    ftext(c, "1/12 + 1/18 = 3/36 + 2/36", 1250, 470, 36, "black", INK, ac)
    text(c, "somar frações", 1250, 540, 28, "bold", GREEN, ac)


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"], "Quantas das nove você acertou no verdadeiro ou falso?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, cobra=b_cobra, mapa=b_mapa, vf=b_vf, q1=b_q1, q2=b_q2, varal=b_varal, q3=b_q3, q4=b_q4, q5=b_q5,
              dominio=b_dominio, meta=b_meta, ponte=b_ponte, cta=b_cta)
