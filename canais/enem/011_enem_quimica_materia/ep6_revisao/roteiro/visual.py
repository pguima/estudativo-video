"""Visual — Matéria, Substâncias e Misturas, Episódio 6: Revisão (tema claro).
Cores com função: azul = definição · roxo = regra · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Reaproveita as peças dos eps. 1 (V), 3 (V3), 4 (V4) e 5 (V5).
Peças próprias:
- icone_ep(): os 5 ícones dos episódios (LEGO, diamante e lápis, copo e salada, câmera e lista, gráfico com patamar).
- fluxo(): o roteiro de 3 perguntas como fluxograma; cada material percorre o caminho até a folha certa.
- pause_timer() e selo("PEGADINHA") nas 9 afirmações de verdadeiro ou falso.
"""
import importlib.util
import json
import math
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_BASE = Path(__file__).resolve().parents[2]


def _load(nome, rel):
    spec = importlib.util.spec_from_file_location(nome, _BASE / rel / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


V = _load("visual_quimica_ep1", "ep1_materia_e_substancias")
V3 = _load("visual_quimica_ep3", "ep3_misturas")
V4 = _load("visual_quimica_ep4", "ep4_fases_componentes")
V5 = _load("visual_quimica_ep5", "ep5_curva_aquecimento")

MARCA = ""
ARQUIVO_FINAL = "enem_quimica_materia_ep6_revisao.mp4"
CARD_R = (140, 150, 1640, 690)
EP_COL = [BLUE, "#5BA6D6", AMBER, PURPLE, GREEN]
EP_NOME = ["simples × composta", "alotropia", "misturas", "fases e componentes", "curva de aquecimento"]


# ======================================================================
# tempos das palavras
# ======================================================================

def _n(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(ch for ch in s if unicodedata.category(ch) != "Mn"))


@lru_cache(None)
def _words():
    p = Path(__file__).resolve().parents[1] / "audio" / "tempos.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {s["id"]: [(_n(w["disp"]), w["t0"]) for w in s.get("tokens", [])] for s in d["scenes"]}


def WT(C, sid, palavra, k=1, depois=None):
    ws = [(w, C[sid] + t0) for w, t0 in _words().get(sid, []) if w == _n(palavra)]
    if depois is not None:
        ws = [x for x in ws if x[1] >= depois - 0.05]
    if not ws:
        return (depois if depois is not None else C[sid]) + 1.2
    return ws[k - 1 if k > 0 else k][1]


# ======================================================================
# peças comuns
# ======================================================================

def icone_ep(c, k, cx, cy, s, a):
    """ícone de cada episódio dentro de um círculo (s = raio)"""
    if a <= 0:
        return
    col = EP_COL[k]
    c.drawCircle(cx, cy, s, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, s, paint(col, a, stroke=max(3, s * 0.06)))
    f = s / 100
    c.save(); c.translate(cx, cy); c.scale(f, f)
    if k == 0:
        V.brick(c, -55, -10, 110, 60, V.EL["O"], a)
    elif k == 1:
        V.diamante(c, -22, -6, a, 0.42)
        c.save(); c.translate(30, 10); c.scale(0.35, 0.35); V.lapis(c, 0, 0, a, 1.0); c.restore()
    elif k == 2:
        V3.vidro(c, -26, 45, 60, 90, a, "acucar", 0, 1)
        c.save(); c.translate(32, 10); c.scale(0.32, 0.32); V3.salada(c, 0, 0, a, 1.0); c.restore()
    elif k == 3:
        V4.icone_foto(c, -24, 0, a, PURPLE)
        V4.icone_receita(c, 28, 0, a, PURPLE)
    else:
        V5.grafico(c, -55, -50, 110, 95, a, V5.PURA, 1.0, INK, (), 1, larg=5, eixo=False)
    c.restore()


def pause_timer(c, t, t0, x, y, a=1.0, dur=2.0, r=46):
    u = clamp((t - t0) / dur)
    ap = a * ep(t, t0, 0.3) * (1 - prog(t, t0 + dur + 0.3, 0.4))
    if ap <= 0:
        return
    c.drawCircle(x, y, r + 14, paint(AMBER, ap * 0.18))
    c.drawCircle(x, y, r, paint("#FFFFFF", ap))
    c.drawArc(skia.Rect.MakeLTRB(x - r, y - r, x + r, y + r), -90, 360 * (1 - u), False, paint(AMBER, ap, stroke=10, cap_round=True))
    c.drawRect(skia.Rect.MakeXYWH(x - 15, y - 20, 10, 40), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(x + 5, y - 20, 10, 40), paint(INK, ap))
    text(c, "PAUSE", x, y + r + 40, 26, "black", AMBER, ap)


def selo(c, x, y, a, s="PEGADINHA", col=None, rot=-8, size=34):
    if a <= 0:
        return
    col = col or AMBER
    c.save(); c.translate(x, y); c.rotate(rot)
    w = text_w(s, "black", size) + 50
    sc = 0.8 + 0.2 * ease_back(clamp(a))
    c.scale(sc, sc)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -size * 0.95, w, size * 1.9), 12, 12), paint(col, a * 0.15))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -size * 0.95, w, size * 1.9), 12, 12), paint(col, a, stroke=5))
    text_mid(c, s, 0, 0, size, "black", col if col != AMBER else "#B07A00", a)
    c.restore()


def which(t, C, ids):
    cur = ids[0]
    for i in ids:
        if t >= C[i] - 0.05:
            cur = i
    return cur


def regra(c, s, cx, cy, a, size=34, col=None, w=None):
    V.regra(c, s, cx, cy, a, size, col, w)


# ======================================================================
# gancho e "como o ENEM cobra"
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "QUÍMICA ENEM", "REVISÃO · EPISÓDIO 6", BLUE)
    card(c, *CARD_R)
    for k in range(5):
        a = ep(t, C["01.a"] + 0.3 * k, 0.4)
        icone_ep(c, k, 340 + k * 310, 330, 95, a)
        text(c, EP_NOME[k], 340 + k * 310, 470, 24, "black", INK2, a)
    ab = ep(t, C["01.b"], 0.5)
    regra(c, "um roteiro de 3 perguntas para QUALQUER material", W / 2, 640, ab, 34, PURPLE, w=1200)


ENEM = [("02.a", 4, "curva de aquecimento", True), ("02.b", 3, "contagem de fases e componentes", False),
        ("02.c", 2, "classificação de materiais do dia a dia", False), ("02.d", 1, "alotropia do carbono (nanotecnologia)", False),
        ("02.e", 4, "tabelas de PF e PE", False)]


def b_enem(c, t, C, B):
    head(c, t, B["start"], "COMO O ENEM", "COBRA ESTE ASSUNTO", BLUE)
    card(c, *CARD_R)
    for j, (cue, k, s, top) in enumerate(ENEM):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + j * 112 + dy
        icone_ep(c, k, 290, y, 44, a)
        text_mid(c, s, 370, y, 40, "black", INK, a, align="left")
        if top:
            pill(c, "O MAIS COBRADO", 1440, y, AMBER, size=26, fg=INK, a=a, anchor="center", bounds=(0, 1920))


# ======================================================================
# o fluxograma de 3 perguntas
# ======================================================================

NODES = {
    "mat": (960, 205, "MATERIAL", INK),
    "q1": (960, 305, "1 substância ou mais?", PURPLE),
    "pura": (560, 420, "SUBSTÂNCIA PURA", BLUE),
    "mist": (1360, 420, "MISTURA", BLUE),
    "q2": (560, 525, "1 elemento ou mais?", PURPLE),
    "q3": (1360, 525, "quantas fases?", PURPLE),
    "simp": (380, 650, "SIMPLES", GREEN),
    "comp": (740, 650, "COMPOSTA", GREEN),
    "homo": (1180, 650, "HOMOGÊNEA", GREEN),
    "het": (1540, 650, "HETEROGÊNEA", GREEN),
}
EDGES = [("mat", "q1", ""), ("q1", "pura", "uma"), ("q1", "mist", "mais"), ("pura", "q2", ""), ("mist", "q3", ""),
         ("q2", "simp", "1"), ("q2", "comp", "2+"), ("q3", "homo", "1"), ("q3", "het", "2+")]
CAMINHOS = {"destilada": ["mat", "q1", "pura", "q2", "comp"], "ar": ["mat", "q1", "mist", "q3", "homo"],
            "granito": ["mat", "q1", "mist", "q3", "het"], "ozonio": ["mat", "q1", "pura", "q2", "simp"]}


def _node_w(k):
    x, y, s, col = NODES[k]
    return text_w(s, "black", 28) + 50


def fluxo(c, t, alpha, ativo=None, aceso=(), size=28):
    """alpha(nó) -> visibilidade · ativo = lista de nós do caminho destacado"""
    ativo = ativo or []
    for a_, b_, lab in EDGES:
        aa = min(alpha(a_), alpha(b_))
        if aa <= 0:
            continue
        xa, ya = NODES[a_][:2]
        xb, yb = NODES[b_][:2]
        on_ = a_ in ativo and b_ in ativo
        col = AMBER if on_ else LIGHT
        arrow(c, xa, ya + 26, xb, yb - 28, col, aa, 6 if on_ else 4, 14)
        if lab:
            text_mid(c, lab, (xa + xb) / 2 + (18 if xb > xa else -18), (ya + yb) / 2, 22, "black", INK2, aa)
    for k, (x, y, s, col) in NODES.items():
        aa = alpha(k)
        if aa <= 0:
            continue
        w = _node_w(k)
        on_ = k in ativo
        rrect(c, x - w / 2, y - 26, w, 52, 14, col, aa * (0.9 if on_ else 0.12), shadow=on_)
        text_mid(c, s, x, y, size if k not in ("q1", "q2", "q3") else 24, "black", "#FFFFFF" if on_ else col, aa)


def b_roteiro(c, t, C, B):
    head(c, t, B["start"], "O ROTEIRO", "3 PERGUNTAS", PURPLE)
    card(c, 140, 150, 1640, 680)
    a0 = ep(t, B["start"], 0.5)
    vis = {"mat": C["03.t"], "q1": C["03.a"], "pura": C["03.b"], "mist": C["03.b"] + 1.2,
           "q2": C["04.a"], "simp": C["04.a"] + 1.2, "comp": C["04.a"] + 2.0,
           "q3": C["04.b"], "homo": C["04.b"] + 1.6, "het": C["04.b"] + 2.6}
    alpha = lambda k: a0 * ep(t, vis[k], 0.4)
    ativo, mat_lab = None, None
    seq = [("06.a", "destilada", "água destilada"), ("06.b", "ar", "ar"), ("06.c", "granito", "granito"), ("06.d", "ozonio", "ozônio")]
    for cue, key, lab in seq:
        if t >= C[cue] - 0.05:
            ativo, mat_lab = CAMINHOS[key], lab
    fluxo(c, t, alpha, ativo)
    # analogias ao lado das folhas
    if t < C["05"]:
        ab = ep(t, C["03.b"] + 0.4, 0.4)
        V.brick(c, 250, 380, 80, 50, V.EL["O"], ab)
        text(c, "1 montagem", 290, 470, 20, "bold", INK2, ab)
        ah = ep(t, C["04.b"] + 1.6, 0.4)
        V3.vidro(c, 1180, 790, 70, 100, ah * 0, "acucar", t, 1)
    # materiais
    am = ep(t, C["05.m"], 0.5)
    if am > 0:
        for j, (cue, key, lab) in enumerate(seq):
            leaf = CAMINHOS[key][-1]
            done = t >= C[cue] + 1.6
            x0, y0 = 250, 260 + j * 0
            if not done:
                pill(c, lab, 260, 235 + j * 52, INK2 if t < C[cue] else AMBER, size=22, fg=None if t < C[cue] else INK,
                     a=am, anchor="center", bounds=(0, 1920))
            else:
                lx, ly = NODES[leaf][:2]
                pill(c, lab, lx, ly + 60, AMBER, size=22, fg=INK, a=am, anchor="center", bounds=(0, 1920))
    pause_timer(c, t, C["05.p"], 1640, 270, 1.0, 2.0)
    if mat_lab:
        pill(c, mat_lab, NODES["mat"][0] + 230, NODES["mat"][1], AMBER, size=24, fg=INK, a=1.0, anchor="center", bounds=(0, 1920))


# ======================================================================
# verdadeiro ou falso
# ======================================================================

VF = [("08", 0, "O₂ é composta, porque tem 2 átomos", "2 átomos parece coisa composta", "conta-se COR, não peça: simples"),
      ("09", 3, "3 cubos de gelo na água = 4 fases", "a foto mostra 3 pedaços", "mesma coisa, mesmo estado: 1 fase"),
      ("10", 3, "fases e componentes: sempre o mesmo número", "em água e óleo, os dois dão 2", "foto e receita: conte duas vezes"),
      ("11", 4, "temperatura constante numa mudança = puro", "o patamar é a marca da pureza", "puro para nas DUAS cabines"),
      ("12", 2, "o ar é substância pura", "invisível e uniforme", "vários gases: mistura homogênea"),
      ("13", 2, "água mineral é substância pura", "transparente, parece só água", "sais dissolvidos: mistura"),
      ("14", 1, "O₂ e O₃ são a mesma substância", "os dois são oxigênio", "montagens diferentes: alótropos"),
      ("15", 2, "leite e sangue são homogêneos", "a olho nu, uma coisa só", "no microscópio: heterogêneos"),
      ("16", 4, "a curva diz se é simples ou composta", "ela já diz se é puro", "só a fórmula decide")]


def b_vf(c, t, C, B):
    head(c, t, B["start"], "VERDADEIRO OU FALSO?", "PAUSE E RESPONDA", AMBER)
    if t < C["08"] - 0.1:
        card(c, *CARD_R)
        a = ep(t, C["07.t"], 0.5)
        text(c, "9 afirmações", W / 2, 400, 90, "black", INK, a)
        pill(c, "pause e responda ANTES de eu falar", W / 2, 540, AMBER, size=34, fg=INK, a=ep(t, C["07.a"], 0.5), anchor="center", bounds=(0, 1920))
        return
    sid = which(t, C, [v[0] for v in VF])
    k = [v[0] for v in VF].index(sid)
    _, ep_k, frase, engana, regra_s = VF[k]
    card(c, 140, 150, 1640, 640)
    for j in range(9):
        col = RED if j < k else (AMBER if j == k else LIGHT)
        c.drawCircle(W / 2 - 4 * 46 + j * 46, 830, 12, paint(col, 1.0))
    icone_ep(c, ep_k, 250, 260, 60, ep(t, C[sid], 0.4))
    text(c, f"ep. {ep_k + 1}", 250, 350, 22, "black", INK2, ep(t, C[sid], 0.4))
    aa = ep(t, C[f"{sid}.a"], 0.4)
    text(c, f"{k + 1}.", 360, 290, 50, "black", INK2, aa, align="left")
    V.erro_tiles  # noqa (só para lembrar que os cartões de erro vêm do ep. 1)
    sz = 50 if text_w(frase, "black", 50) < 1300 else 44
    text(c, f"\"{frase}\"", 430, 290, sz, "black", INK, aa, align="left")
    pause_timer(c, t, C[f"{sid}.p"], 1640, 420, 1.0, 2.0)
    ar = ep(t, C[f"{sid}.r"], 0.35)
    if ar > 0:
        selo(c, 560, 450, ar, "FALSO", RED, -6, 48)
        selo(c, 1000, 450, ep(t, C[f"{sid}.r"] + 0.3, 0.35), "PEGADINHA", AMBER, 5, 34)
    aw = ep(t, C[f"{sid}.w"], 0.4)
    text(c, "engana porque: " + engana, 360, 600, 34, "bold", "#B07A00", aw, align="left")
    regra(c, regra_s, W / 2, 700, ep(t, C[f"{sid}.k"], 0.4), 34, PURPLE, w=1300)


def b_vf_placar(c, t, C, B):
    head(c, t, B["start"], "VERDADEIRO OU FALSO?", "O PLACAR", AMBER)
    card(c, *CARD_R)
    for j in range(9):
        a = ep(t, C["17.t"] + 0.12 * j, 0.3)
        x = 300 + (j % 9) * 165
        rrect(c, x - 70, 230, 140, 110, 16, RED, a * 0.12)
        text_mid(c, str(j + 1), x, 262, 30, "black", INK2, a)
        text_mid(c, "FALSO", x, 310, 26, "black", RED, a)
    text(c, "quantas você acertou?", W / 2, 470, 60, "black", INK, ep(t, C["17.a"], 0.5))
    ab = ep(t, C["17.b"], 0.5)
    for k in range(5):
        icone_ep(c, k, 520 + k * 220, 640, 56, ab * ep(t, C["17.b"] + 0.2 * k, 0.4))
    text(c, "cada erro aponta o episódio para rever", W / 2, 790, 30, "bold", INK2, ab)


# ======================================================================
# questões inéditas
# ======================================================================

def enunciado(c, t, linhas, y0=270, size=28):
    for k, (cue, s, col) in enumerate(linhas):
        text(c, s, 180, y0 + k * 42, size, "black", col or INK, ep(t, cue, 0.5), align="left")


def alternativas(c, t, C, y0, alts, alt_cues, correta, cue_ok, xs, size=26, w=820):
    aok = ep(t, C[cue_ok], 0.5)
    for k, s in enumerate(alts):
        L = "ABCDE"[k]
        a, d = rise(t, C[alt_cues[k]])
        y = y0 + k * 54 + d
        ok = L == correta
        if ok and aok > 0:
            rrect(c, 170, y - 37, w, 52, 12, GREEN, 0.15 * aok)
        badge_num(c, L, 205, y - 12, a, 19, bg=GREEN if ok and aok > 0.5 else INK)
        x_cue, why = xs.get(L, (None, ""))
        ax = ep(t, C[x_cue], 0.4) if x_cue else 0
        text(c, s, 240, y, size, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 236, y - 10, 246 + text_w(s, "black", size), y - 10, ax, RED, ax)
            mesma = 260 + text_w(s, "black", size) + text_w(why, "black", 20) < 170 + w - 10
            text(c, why, 170 + w - 10, y - 2 if mesma else y + 22, 20 if mesma else 18, "black", RED, ax, align="right")


def q_base(c, t, C, B, n, tema):
    head(c, t, B["start"], f"QUESTÃO INÉDITA {n}", tema, BLUE)
    card(c, 140, 160, 860, 660)
    pill(c, f"QUESTÃO {n}", 170, 204, BLUE, size=22, bounds=(0, 1920))


def sol(c, t, C, cue, a_extra=1.0):
    ar = ep(t, C[cue], 0.5) * a_extra
    if ar > 0:
        card(c, 1040, 160, 740, 660, ar)
    return ar


Q1_MAT = [("I", "água destilada", 0), ("II", "ar do cilindro", 1), ("III", "aço inox", 1), ("IV", "água com óleo", 2), ("V", "leite", 2)]


def b_q1(c, t, C, B):
    q_base(c, t, C, B, 1, "CLASSIFICAÇÃO DE MATERIAIS")
    enunciado(c, t, [(C["18.e1"], "I água destilada · II ar comprimido (mergulho)", None),
                     (C["18.e1"], "III aço inox · IV água com óleo · V leite", None),
                     (C["18.e2"], "São misturas homogêneas apenas:", INK2)])
    alternativas(c, t, C, 440, ["I, II e III", "II e III", "II, III e V", "III", "II"], ["18.a", "18.b", "18.c", "18.d", "18.e"], "B", "19.ok",
                 {"C": ("19.xc", "leite é heterogêneo"), "D": ("19.xd", "o ar não é puro"), "E": ("19.xe", "o aço não é puro"),
                  "A": ("19.xa", "destilada é pura")})
    pause_timer(c, t, C["18.p"], 1400, 480, 1.0, 1.5)
    ar = sol(c, t, C, "19.t")
    if ar > 0:
        for k, (r, nome, col) in enumerate(Q1_MAT):
            a = ar * ep(t, C["19.s"] + 0.7 * k, 0.4)
            y = 250 + k * 100
            s, cc = V3.COLS[col]
            rrect(c, 1070, y - 36, 680, 74, 14, cc, a * 0.10)
            text(c, f"{r} · {nome}", 1090, y + 10, 30, "black", INK, a, align="left")
            pill(c, s, 1650, y, cc, size=20, fg=INK if cc == AMBER else None, a=a, anchor="center", bounds=(0, 1920))
        pill(c, "homogêneas: II e III → B", 1410, 770, GREEN, size=28, a=ep(t, C["19.ok"], 0.5), anchor="center", bounds=(0, 1920))


Q2_F = [("grafeno", "C", True), ("ozônio", "O3", True), ("metano", "CH4", False), ("diamante", "C", True), ("nitrogênio", "N2", True)]


def b_q2(c, t, C, B):
    q_base(c, t, C, B, 2, "SIMPLES, COMPOSTA, ALÓTROPOS")
    enunciado(c, t, [(C["20.e1"], "Grafeno, ozônio, metano (CH₄),", None), (C["20.e1"], "diamante e nitrogênio (N₂).", None),
                     (C["20.e2"], "É correto afirmar:", INK2)])
    alternativas(c, t, C, 440, ["O₃ é composto: 3 átomos", "grafeno = diamante (mesma)", "diferem por impurezas",
                                "metano é alótropo do C", "alótropos; só o metano é composto"],
                 ["20.a", "20.b", "20.c", "20.d", "20.e"], "E", "21.ok",
                 {"A": ("21.xa", "contou peças"), "B": ("21.xb", "alótropos são diferentes"), "C": ("21.xc", "é o arranjo"),
                  "D": ("21.xd", "alótropo é simples")})
    pause_timer(c, t, C["20.p"], 1400, 480, 1.0, 1.5)
    ar = sol(c, t, C, "21.t")
    if ar > 0:
        for k, (nome, f, simp) in enumerate(Q2_F):
            a = ar * ep(t, C["21.s"] + 0.6 * k, 0.4)
            y = 250 + k * 96
            V.formula(c, f, 1170, y, 50, a, lit=V.n_el(f) * ep(t, C["21.s"] + 0.6 * k + 0.3, 0.4), upper=True)
            text(c, nome, 1260, y + 10, 28, "black", INK, a, align="left")
            text(c, "SIMPLES" if simp else "COMPOSTA", 1720, y + 10, 26, "black", PURPLE if simp else RED, a, align="right")
        aal = ar * ep(t, C["21.s"] + 0.3, 0.4)
        if aal > 0:
            line(c, 1090, 250, 1090, 538, "#5BA6D6", aal, 4)
            text(c, "alótropos", 1080, 400, 20, "black", "#5BA6D6", aal, align="right")
        pill(c, "→ letra E", 1410, 770, GREEN, size=28, a=ep(t, C["21.ok"], 0.5), anchor="center", bounds=(0, 1920))


def b_q3(c, t, C, B):
    q_base(c, t, C, B, 3, "FASES E COMPONENTES")
    enunciado(c, t, [(C["22.e1"], "Copo com água, 2 cubos de gelo,", None), (C["22.e1"], "sal dissolvido e areia no fundo.", None),
                     (C["22.e2"], "Fases e componentes:", INK2)])
    alternativas(c, t, C, 440, ["3 e 3", "4 e 3", "3 e 4", "4 e 4", "3 e 2"], ["22.a", "22.b", "22.c", "22.d", "22.e"], "A", "23.ok",
                 {"B": ("23.xb", "cada cubo como fase"), "C": ("23.xc", "gelo como componente"), "D": ("23.xd", "os dois erros"),
                  "E": ("23.xe", "esqueceu o sal")})
    pause_timer(c, t, C["22.p"], 1400, 480, 1.0, 1.5)
    ar = sol(c, t, C, "23.t")
    if ar > 0:
        x, y, w, h = 1070, 300, 230, 360

        def obj(c, aa):
            V4.areia_graos(c, x + 4, y + h * 0.84 + 4, w - 8, h * 0.16 - 10, aa, 5)
            for k in range(2):
                V4.cubo(c, x + w * (0.35 + 0.3 * k), y + h * 0.28 + 8, w * 0.2, aa, (-6, 5)[k])
        V4.recipiente(c, x, y, w, h, ar, [(0, 0.16, V4.SAND, 1.0), (0.16, 0.72, "#9CC4F2", 0.6)], [obj])
        af = ep(t, C["23.f"], 0.4) * ar
        for k in range(2):
            cx = x + w * (0.35 + 0.3 * k)
            s = w * 0.2
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s * 0.66, y + h * 0.28 + 8 - s * 0.66, s * 1.32, s * 1.32), 8, 8), V4._dash(PURPLE, af))
        V4.fase_box(c, x + 6, y + h * 0.36 + 4, w - 12, h * 0.46, 2, ep(t, C["23.f"] + 0.5, 0.4) * ar, badge_x=x + w + 26)
        V4.fase_box(c, x + 6, y + h * 0.86, w - 12, h * 0.14 - 6, 3, ep(t, C["23.f"] + 1.0, 0.4) * ar, badge_x=x + w + 26)
        badge_num(c, 1, x + w * 0.5, y + h * 0.28 - 40, af, 16, bg=PURPLE)
        V4.colunas(c, t, 1360, 180, 400, 620,
                   [(C["23.f"], "gelo ×2", V4.ICE), (C["23.f"] + 0.5, "água salgada", "#9CC4F2"), (C["23.f"] + 1.0, "areia", V4.SAND)],
                   [(C["23.r"], "água", "#9CC4F2"), (C["23.r"] + 0.5, "sal", "#E5E5EA"), (C["23.r"] + 1.0, "areia", V4.SAND)],
                   (C["23.f"] + 1.6, "3 fases"), (C["23.r"] + 1.8, "3 comp."), a=ar)


def b_q4(c, t, C, B):
    q_base(c, t, C, B, 4, "CURVA COM UM PATAMAR")
    enunciado(c, t, [(C["24.e1"], "Líquido congelado e depois aquecido.", None), (C["24.e2"], "Fusão: temperatura subindo sem parar.", None),
                     (C["24.e2"], "Ebulição: constante a 78 °C.", None), (C["24.e3"], "Ele é:", INK2)])
    alternativas(c, t, C, 480, ["substância pura", "mistura eutética", "mistura comum", "mistura azeotrópica", "substância composta"],
                 ["24.a", "24.b", "24.c", "24.d", "24.e"], "D", "25.ok",
                 {"A": ("25.xa", "1 patamar não prova pureza"), "B": ("25.xb", "eutética é na fusão"),
                  "C": ("25.xc", "há um patamar"), "E": ("25.xe", "a curva não diz")})
    pause_timer(c, t, C["24.p"], 1400, 480, 1.0, 1.5)
    ar = sol(c, t, C, "25.t")
    if ar > 0:
        V5.grafico(c, 1140, 260, 560, 360, ar, V5.AZEO, 1.0, INK, [(0.72, "78 °C", RED)], 22)
        V5.patamar_rotulo(c, 1140, 260, 560, 360, V5.AZEO, 3, "1 cabine: ferver", ar * ep(t, C["25.s"], 0.4), GREEN, -40, 20)
        V5.patamar_rotulo(c, 1140, 260, 560, 360, V5.AZEO, 1, "faixa", ar * ep(t, C["25.s"], 0.4), AMBER, -40, 20)
        pill(c, "ferve certinho → AZEOTRÓPICA", 1410, 740, PURPLE, size=28, a=ep(t, C["25.s"] + 1.5, 0.5), anchor="center", bounds=(0, 1920))


TAB5 = [("Bromo", -7, 59, "27.s1", "sólido"), ("Cloro", -101, -34, "27.s2", "gás"), ("Mercúrio", -39, 357, "27.s3", "LÍQUIDO"),
        ("Etanol", -114, 78, "27.s3", "LÍQUIDO"), ("Água", 0, 100, "27.s4", "sólido")]


def b_q5(c, t, C, B):
    q_base(c, t, C, B, 5, "ESTADO FÍSICO A −20 °C")
    ae = ep(t, C["26.e1"], 0.5)
    text(c, "PF (°C)", 600, 266, 22, "black", INK2, ae, align="right")
    text(c, "PE (°C)", 780, 266, 22, "black", INK2, ae, align="right")
    for k, (nome, pf, pe, _, _) in enumerate(TAB5):
        ak = ae * ep(t, C["26.e1"] + 1.4 * k, 0.4)
        y = 304 + k * 36
        text(c, nome, 190, y, 26, "black", INK, ak, align="left")
        text(c, str(pf).replace("-", "−"), 600, y, 26, "black", INK, ak, align="right")
        text(c, str(pe).replace("-", "−"), 780, y, 26, "black", INK, ak, align="right")
    text(c, "A −20 °C, líquidos apenas:", 180, 500, 26, "black", INK2, ep(t, C["26.e2"], 0.5), align="left")
    alternativas(c, t, C, 556, ["etanol", "bromo, mercúrio e etanol", "mercúrio e etanol", "cloro, mercúrio e etanol",
                                "mercúrio, etanol e água"], ["26.a", "26.b", "26.c", "26.d", "26.e"], "C", "27.ok",
                 {"B": ("27.xb", "sinal do bromo"), "D": ("27.xb", "sinal do cloro"), "A": ("27.xa", "esqueceu o mercúrio"),
                  "E": ("27.xe", "a água congela")})
    pause_timer(c, t, C["26.p"], 1400, 480, 1.0, 1.5)
    ar = sol(c, t, C, "27.t")
    if ar > 0:
        text(c, "linha vermelha = −20 °C", 1410, 210, 22, "bold", INK2, ar)
        for k, (nome, pf, pe, cue, est) in enumerate(TAB5):
            ak = ar * ep(t, C[cue], 0.4)
            x = 1090 + k * 140
            lo, hi = min(pf, -20) - 40, max(pe, -20) + 40
            V5.regua(c, x, 250, 400, ak, pf, pe, lo, hi, -20, w=46, rotulos=False, size=18)
            text(c, nome, x + 23, 700, 22, "black", INK, ak)
            text(c, est, x + 23, 738, 20, "black", GREEN if est == "LÍQUIDO" else INK2, ak)


# ======================================================================
# checklist, meta, ponte
# ======================================================================

CHECK = [("28.a", 0, "propriedades gerais × específicas · simples × composta"), ("28.b", 1, "alotropia: oxigênio e carbono"),
         ("28.c", 2, "misturas pelas fases · gases · ar, água mineral, ligas, granito"), ("28.d", 3, "fases e componentes, separados"),
         ("28.e", 4, "PF e PE · curva · eutética × azeotrópica"), ("28.f", None, "o roteiro de 3 perguntas")]


def b_checklist(c, t, C, B):
    if t < C["29"] - 0.1:
        head(c, t, B["start"], "CHECKLIST", "DE DOMÍNIO", GREEN)
        card(c, *CARD_R)
        text(c, "marque só o que você explicaria em voz alta, sem consultar", W / 2, 220, 28, "black", "#B07A00", ep(t, C["28.t"], 0.5))
        for j, (cue, k, s) in enumerate(CHECK):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 300 + j * 88 + dy
            rrect(c, 230, y - 26, 52, 52, 10, "#FFFFFF", a, stroke=4, stroke_color=INK2)
            if k is not None:
                icone_ep(c, k, 340, y, 34, a)
            else:
                text_mid(c, "?", 340, y, 40, "black", PURPLE, a)
            text_mid(c, s, 400, y, 32, "bold", INK, a, align="left")
        return
    head(c, t, C["29"], "O QUE NÃO MARCOU", "REVEJA O EPISÓDIO", GREEN)
    card(c, *CARD_R)
    for k, cue in enumerate(("29.a", "29.b", "29.c", "29.d", "29.e")):
        a, dy = rise(t, C[cue])
        x = 300 + k * 330
        icone_ep(c, k, x, 400 + dy, 100, a)
        text(c, f"EPISÓDIO {k + 1}", x, 560 + dy, 30, "black", EP_COL[k] if k != 2 else "#B07A00", a)
        text(c, EP_NOME[k], x, 605 + dy, 24, "bold", INK2, a)


def b_meta(c, t, C, B):
    head(c, t, B["start"], "A META", "ANTES DE DAR COMO DOMINADO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["30.a"], 0.5)
    for k in range(30):
        i, j = k % 10, k // 10
        x, y = 280 + i * 80, 260 + j * 90
        g = ep(t, C["30.a"] + 0.05 * k, 0.25) if k < 21 else 0
        rrect(c, x, y, 64, 64, 12, mix("#E5E5EA", GREEN, g), aa)
    text(c, "21 de 30", 1400, 380, 90, "black", GREEN, ep(t, C["30.a"] + 1.6, 0.5))
    text(c, "= 70%", 1400, 480, 70, "black", INK, ep(t, C["30.a"] + 2.0, 0.5))
    ab = ep(t, C["30.b"], 0.5)
    icone_ep(c, 4, 520, 680, 50, ab); icone_ep(c, 3, 640, 680, 50, ab)
    text_mid(c, "comece pela curva e pela contagem de fases", 720, 680, 32, "black", INK, ab, align="left")


def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO ASSUNTO", "SEPARAÇÃO DE MISTURAS", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["31.t"], 0.5)
    V3.vidro(c, 460, 620, 240, 340, a0, "areia")
    text(c, "aqui: você CLASSIFICOU", 460, 690, 30, "black", INK, a0)
    aa = ep(t, C["31.a"], 0.5)
    arrow(c, 640, 480, 1000, 480, PURPLE, aa, 6, 20, progress=ease_io(prog(t, C["31.a"], 0.8)))
    V.funil(c, 1240, 420, aa)
    V3.vidro(c, 1240, 640, 160, 160, aa, "agua")
    text(c, "lá: você vai SEPARAR", 1240, 720, 30, "black", PURPLE, ep(t, C["31.b"], 0.5))
    pill(c, "PRÓXIMO: SEPARAÇÃO DE MISTURAS", W / 2, 800, PURPLE, size=30, a=ep(t, C["31.b"] + 1.0, 0.5), anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Quantas das nove pegadinhas você acertou?")


BLOCKS = dict(hook=b_hook, enem=b_enem, roteiro=b_roteiro, vf=b_vf, vf_placar=b_vf_placar, q1=b_q1, q2=b_q2, q3=b_q3,
              q4=b_q4, q5=b_q5, checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
