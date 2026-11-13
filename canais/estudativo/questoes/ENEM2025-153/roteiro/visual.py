"""Visual — Estudativo · Resolução ENEM 2025 (2º dia, caderno amarelo), questão 153: o código do visitante.
Estrutura do modelo antigo de questões (canais/enem/questoes, git 5eeb6d2): print do enunciado no 1º quadro com
marca-texto acompanhando a fala, ideias pelo nome, passos numerados, pegadinhas, atalho, desafio, resumo e aulas.
Identidade editorial da Matemática (papel claro, índigo, palco escuro só no atalho). Peça central: as 7 casas do código,
agrupadas em andar | setor | funcionário | turno. Vermelho = erro, verde = certo. Efeitos sonoros sem trilha (aula horizontal).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
from functools import lru_cache
from pathlib import Path

import skia
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_out, ease_back, centro, palco, clamp
import motor as M

E.usar("Matemática", "Questões do ENEM")
COR, CLARO = E.COR_TEXTO, E.CLARO
BR = "#FFFFFF"
MARCA_TEXTO = "#FFE45C"
ARQUIVO_FINAL = "estudativo_ENEM2025_questao153_codigo_do_visitante.mp4"
MARCA = ""
ENTRADA_SECA = True   # o enunciado aparece no primeiro quadro, sem fade
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("posicao", "monta", "pegadinhas", "atalho", "desafio"))

# efeitos acertados com o desenho; aula horizontal: sem trilha de fundo
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx={
    "s01.b": ["data"], "s01.c": ["data"], "s01.d": ["alert"], "s01.e": ["shimmer"],
    "s02.b": ["pop@+0.3"], "s02.c": ["whoosh@+0.2"], "s02.d": ["deny@+0.2"], "s02.e": ["data"],
    "s03.b": ["pop@+0.3"], "s03.c": ["confirm@+0.5"], "s03.d": ["confirm@+1.6"], "s03.e": ["lock"],
    "s04.c": ["pop"], "s05.b": ["pop", "pop@+0.3"], "s06.b": ["pop", "pop@+0.3", "pop@+0.6"],
    "s07.b": ["deny@+0.3"], "s07.c": ["pop"], "s08.a": ["confirm@+1.0"], "s08.c": ["impact"],
    "s09.b": ["deny@+0.4"], "s09.c": ["deny@+0.4"], "s09.d": ["deny@+0.4"], "s09.e": ["deny@+0.4"],
    "s10.b": ["data"], "s10.c": ["deny", "deny@+0.35", "deny@+0.7"], "s10.d": ["data"], "s10.e": ["deny"],
    "s10.f": ["confirm", "shimmer@+0.3"], "s11.b": ["data"], "s11.c": ["alert"], "s12.a": ["shimmer"],
    "s13.b": ["pop"], "s13.c": ["pop"], "s13.e": ["click@+0.9", "notif@+1.0"],
})

CODIGO = "2081090"
GRUPOS = (("andar", 1, "1 a 4", "2º andar"), ("setor", 2, "01 a 20", "setor 08"),
          ("funcionário", 3, "001 a 135", "funcionário 109"), ("turno", 1, "0 manhã · 1 tarde", "10 h da manhã"))
ALT = (("A", "0109082"), ("B", "0281090"), ("C", "1010982"), ("D", "2081090"), ("E", "2810910"))
# cada alternativa lida em pedaços: (dígitos, o que ela pôs ali, pedaço errado?)
LEITURA = {
    "A": ([("0", "turno", 1), ("109", "func.", 0), ("08", "setor", 1), ("2", "andar", 1)], "ordem invertida"),
    "B": ([("02", "andar", 1), ("8", "setor", 1), ("109", "func.", 0), ("0", "turno", 0)], "zero no andar, não no setor"),
    "C": ([("10", "hora!", 1), ("109", "func.", 0), ("8", "setor", 1), ("2", "andar", 1)], "usou o 10 e inverteu"),
    "D": ([("2", "andar", 0), ("08", "setor", 0), ("109", "func.", 0), ("0", "turno", 0)], "cada um na sua casa"),
    "E": ([("2", "andar", 0), ("8", "setor", 1), ("109", "func.", 0), ("10", "hora!", 1)], "sem o zero e com o 10"),
}
assert "2" + "08" + "109" + "0" == CODIGO == dict(ALT)["D"]
assert all("".join(p for p, _, _ in LEITURA[l][0]) == s for l, s in ALT)
assert [l for l, s in ALT if s[0] == "2" and s[1] == "0"] == ["D"]
assert "4" + "15" + "042" + "1" == "4150421"   # desafio: 15 h (tarde), func. 42, setor 15, 4º andar

ENUNCIADO = Path(__file__).resolve().parents[1] / "enunciado" / "questao.png"


@lru_cache(None)
def img_questao():
    return skia.Image.open(str(ENUNCIADO))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def pop(t, t0, d=0.45):
    return ease_back(prog(t, t0, d))


def layout(bw, gap=14, ggap=50, cx=W / 2):
    """x de cada casa e (x0, x1) de cada grupo, centrado em cx"""
    total = 7 * bw + 3 * gap + 3 * ggap
    x, xs, gs = cx - total / 2, [], []
    for _, n, _, _ in GRUPOS:
        g0 = x
        for k in range(n):
            xs.append(x)
            x += bw + (gap if k < n - 1 else ggap)
        gs.append((g0, x - ggap))
    return xs, gs


def casa(c, x, y, bw, bh, a=1.0, borda=None, fundo=BR, s=1.0, grossa=4):
    if a <= 0:
        return
    cx, cy = x + bw / 2, y + bh / 2
    c.save(); c.translate(cx, cy); c.scale(s, s)
    M.rrect(c, -bw / 2, -bh / 2, bw, bh, 18, fundo, a, shadow=True)
    M.rrect(c, -bw / 2, -bh / 2, bw, bh, 18, None, a, stroke=grossa, stroke_color=borda or COR)
    c.restore()


def digito(c, ch, x, y, bw, bh, cor=TINTA, a=1.0, size=None):
    size = size or bh * 0.62
    centro(c, ch, x + bw / 2, y + bh / 2 + size * 0.36, size, "g", cor, a)


def fileira(c, t, t0, digs, x0, y, bw, bh, borda=COR, cor_dig=TINTA, gap=12, cores=None):
    """7 casas seguidas (sem grupos), entrando uma a uma"""
    for i, ch in enumerate(digs):
        x = x0 + i * (bw + gap)
        s = pop(t, t0 + 0.05 * i, 0.4)
        if s > 0:
            casa(c, x, y, bw, bh, min(1, s * 1.2), borda=borda, s=s)
            digito(c, ch, x, y, bw, bh, (cores or {}).get(i, cor_dig), min(1, s))


def titulo(c, t, t0, rot, nome, t1=None):
    """título da tela: "ideia 1 ·" em itálico + o nome em negrito"""
    fn = lambda: E.frase(c, t, t0, [(rot, "i", 64, COR), (nome, "g", 64, TINTA)], XE, 150, "left", 0.15)
    if t1 is None:
        fn()
    else:
        E.saida(c, t, t1, fn)


# ---------------- 1. a questão: print do enunciado + o que ela pede ----------------
PX, PY, PH = 64, 60, 960          # print à esquerda
DX = 1370                          # centro da coluna da direita


def marca(c, t, t0, y0, y1, d=0.6):
    """marca-texto sobre o print (coordenadas do PNG original)"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    img = img_questao()
    k = PH / img.height()
    x0 = PX + 6 * k
    w = (img.width() - 10) * k
    c.drawRect(skia.Rect.MakeXYWH(x0, PY + y0 * k, w * p, (y1 - y0) * k), M.paint(MARCA_TEXTO, 0.42))


def b_gancho(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s01.{k}"] for k in "abcde")
    img = img_questao()
    k = PH / img.height()
    pw = img.width() * k
    M.rrect(c, PX - 18, PY - 18, pw + 36, PH + 36, 22, BR, 1, shadow=True)
    c.drawImageRect(img, skia.Rect.MakeXYWH(PX, PY, pw, PH), skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear))
    # o marca-texto acompanha a fala
    marca(c, t, b_, 360, 850)
    marca(c, t, c_, 878, 1035)
    marca(c, t, d_, 1055, 1105)
    # coluna da direita, cheia desde o quadro 0
    E.pilula(c, "ENEM 2025 · questão 153", DX, 130, 40, "g", fundo=E.COR, cor=BR)
    E.frase(c, t, -1, [("o código", "i", 76, TINTA2), ("do visitante", "g", 72, TINTA)], DX, 250, "center", 0.15)
    E.foco(c, t, a_ + 3.0, 0.45, lambda a: E.pilula(c, "7 dígitos", DX, 330, 40, "g", fundo=TINTA, cor=BR, a=a))
    xs, gs = layout(84, 8, 30, DX)
    for i, x in enumerate(xs):
        s = pop(t, b_ + 0.05 * i, 0.4)
        if s > 0:
            casa(c, x, 400, 84, 100, min(1, s * 1.2), s=s)
    for j, ((nome, _, _, _), (g0, g1)) in enumerate(zip(GRUPOS, gs)):
        E.foco(c, t, b_ + 0.6 + 0.45 * j, 0.4, lambda a, g0=g0, g1=g1, nome=nome: centro(c, nome, (g0 + g1) / 2, 550, 34, "g", COR, a))
    # os dados, na ordem da fala
    for j, s_ in enumerate(("10 h da manhã", "funcionário 109", "setor 08", "2º andar")):
        E.foco(c, t, c_ + 0.3 + 1.5 * j, 0.4, lambda a, s_=s_, j=j: E.pilula(c, s_, DX + (-220 if j % 2 == 0 else 220), 650 + 90 * (j // 2), 38, "b", fundo=TINTA, cor=BR, a=a))
    s = pop(t, d_, 0.5)
    if s > 0:
        c.save(); c.translate(DX, 880); c.scale(s, s)
        E.pilula(c, "qual é o código?", 0, 0, 52, "g", fundo=E.COR, cor=BR)
        c.restore()
    E.foco(c, t, e_ + 2.2, 0.4, lambda a: E.pilula(c, "posição de cada dígito", DX - 210, 1000, 34, "b", fundo=CERTO, cor=BR, a=a))
    E.foco(c, t, e_ + 3.6, 0.4, lambda a: E.pilula(c, "zero à esquerda", DX + 250, 1000, 34, "b", fundo=CERTO, cor=BR, a=a))


# ---------------- 2. ideia 1: a posição manda ----------------
def b_posicao(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s02.{k}"] for k in "abcde")
    titulo(c, t, a_, "ideia 1 ·", "a posição manda")
    xs, gs = layout(130, 12, 46)
    for i, x in enumerate(xs):
        s = pop(t, b_ + 0.05 * i, 0.4)
        if s > 0:
            casa(c, x, 260, 130, 150, min(1, s * 1.2), s=s)
            digito(c, CODIGO[i], x, 260, 130, 150, TINTA, min(1, s))
    for j, ((nome, _, _, _), (g0, g1)) in enumerate(zip(GRUPOS, gs)):
        E.chave(c, g0, g1, 430, COR, ep(t, b_ + 0.4 + 0.15 * j, 0.4), h=20)
        E.foco(c, t, b_ + 0.5 + 0.15 * j, 0.4, lambda a, g0=g0, g1=g1, nome=nome: centro(c, nome, (g0 + g1) / 2, 500, 40, "g", COR, a))
    # os mesmos números em outra ordem
    if t >= c_:
        bw = 130
        x0 = W / 2 - (7 * bw + 6 * 12) / 2
        fileira(c, t, c_ + 0.2, "0109082", x0, 590, bw, 150, borda=E.ERRADO if t >= d_ else CINZA)
        if t >= d_ + 0.2:
            E.risco(c, x0 - 20, 700, x0 + 7 * bw + 6 * 12 + 20, 640, t, d_ + 0.2, largura=12)
        E.foco(c, t, d_ + 0.5, 0.4, lambda a: E.pilula(c, "outro código", W / 2, 810, 40, "g", fundo=E.ERRADO, cor=BR, a=a))
    p = ep(t, e_, 0.6)
    if p > 0:
        M.arrow(c, 420, 940, 420 + 1080 * p, 940, COR, p, 7, 22, p)
        E.foco(c, t, e_ + 0.4, 0.4, lambda a: E.pilula(c, "da esquerda para a direita", W / 2, 1000, 38, "b", fundo=COR, cor=BR, a=a))


# ---------------- 3. ideia 2: o zero à esquerda ----------------
def b_zero(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s03.{k}"] for k in "abcde")
    titulo(c, t, a_, "ideia 2 ·", "o zero à esquerda")
    LX, RX = 560, 1380
    # o setor: duas casas
    E.frase(c, t, b_, [("setor:", "i", 56, TINTA2), ("01 a 20", "g", 60, COR)], LX, 300, "center", 0.15)
    E.foco(c, t, b_ + 0.6, 0.4, lambda a: E.pilula(c, "2 casas", LX, 370, 34, "g", fundo=TINTA, cor=BR, a=a))
    E.foco(c, t, c_, 0.45, lambda a: centro(c, "8", LX - 250, 640, 170, "g", TINTA2, a))
    p = ep(t, c_ + 0.3, 0.4)
    if p > 0:
        M.arrow(c, LX - 160, 580, LX - 160 + 90 * p, 580, COR, p, 6, 18, p)
    for k, ch in enumerate("08"):
        x = LX - 40 + k * 160
        s = pop(t, c_ + 0.5 + 0.15 * k, 0.45)
        if s > 0:
            casa(c, x - 70, 470, 140, 170, min(1, s * 1.2), s=s, borda=E.ERRADO if k == 0 else COR)
            digito(c, ch, x - 70, 470, 140, 170, E.ERRADO if k == 0 else TINTA, min(1, s))
    # o funcionário: três casas
    E.frase(c, t, d_, [("funcionário:", "i", 56, TINTA2), ("001 a 135", "g", 60, COR)], RX, 300, "center", 0.15)
    E.foco(c, t, d_ + 0.6, 0.4, lambda a: E.pilula(c, "3 casas", RX, 370, 34, "g", fundo=TINTA, cor=BR, a=a))
    for k, ch in enumerate("007"):
        x = RX - 230 + k * 160
        s = pop(t, d_ + 1.5 + 0.15 * k, 0.45)
        if s > 0:
            casa(c, x, 470, 140, 170, min(1, s * 1.2), s=s, borda=E.ERRADO if k < 2 else COR)
            digito(c, ch, x, 470, 140, 170, E.ERRADO if k < 2 else TINTA, min(1, s))
    E.foco(c, t, d_ + 2.0, 0.4, lambda a: centro(c, "funcionário 7", RX, 720, 40, "i", TINTA2, a))
    E.foco(c, t, c_ + 0.9, 0.4, lambda a: centro(c, "setor 8", LX + 40, 720, 40, "i", TINTA2, a))
    E.frase(c, t, e_, [("08 = 8", "g", 70, COR), ("e", "i", 64, TINTA2), ("007 = 7", "g", 70, COR)], W / 2, 870, "center", 0.2)
    E.frase(c, t, e_ + 1.6, [("o zero só", "i", 60, TINTA2), ("preenche a casa", "g", 60, TINTA)], W / 2, 980, "center", 0.15)


# ---------------- 4. a resolução: passo a passo nas casas ----------------
BW, BH, YB = 150, 180, 250
PASSOS = (("passo 1 ·", "o andar"), ("passo 2 ·", "o setor"), ("passo 3 ·", "o funcionário"), ("passo 4 ·", "o turno"),
          ("juntando ·", "o código"))


def b_monta(c, t, C, b):
    ini = [C["s04.b"], C["s05.a"], C["s06.a"], C["s07.a"], C["s08.a"]]
    fins = ini[1:] + [b["end"] + 1]
    for (rot, nome), t0, t1 in zip(PASSOS, ini, fins):
        if t >= t0 - 0.1:
            titulo(c, t, t0, rot, nome, t1 - 0.15 if t1 < b["end"] else None)
    E.frase(c, t, C["s04.a"], [("a resolução", "i", 64, COR)], XE, 150, "left") if t < ini[0] - 0.15 else None
    xs, gs = layout(BW)
    t_dig = [C["s04.c"], C["s05.b"], C["s05.b"] + 0.3, C["s06.b"], C["s06.b"] + 0.3, C["s06.b"] + 0.6, C["s07.c"]]
    ativo = next((k for k in range(3, -1, -1) if t >= ini[k]), None) if t < ini[4] else None
    grupo_de = [0, 1, 1, 2, 2, 2, 3]
    for i, x in enumerate(xs):
        s = pop(t, C["s04.a"] + 0.05 * i, 0.4)
        on = ativo is not None and grupo_de[i] == ativo
        casa(c, x, YB, BW, BH, min(1, s * 1.2), borda=COR, fundo="#EEF0FF" if on else BR, s=max(0.01, s), grossa=7 if on else 4)
        if t >= t_dig[i]:
            k = pop(t, t_dig[i], 0.4)
            cor = E.ERRADO if i == 1 else (CERTO if t >= C["s08.a"] + 1.0 else TINTA)
            digito(c, CODIGO[i], x, YB, BW, BH, cor, min(1, k * 1.3), BH * 0.62 * max(0.01, k))
    for j, ((nome, _, faixa, _), (g0, g1)) in enumerate(zip(GRUPOS, gs)):
        E.chave(c, g0, g1, YB + BH + 26, COR, ep(t, C["s04.a"] + 0.2 * j, 0.4), h=22)
        cx = (g0 + g1) / 2
        E.foco(c, t, C["s04.a"] + 0.2 * j, 0.4, lambda a, cx=cx, nome=nome: centro(c, nome, cx, YB + BH + 100, 46, "g", COR, a))
        E.foco(c, t, C["s04.a"] + 0.3 + 0.2 * j, 0.4, lambda a, cx=cx, faixa=faixa: centro(c, faixa, cx, YB + BH + 150, 38, "i", TINTA2, a))

    # os dados do visitante, embaixo do seu pedaço; cada um sobe quando é usado
    def dados():
        for j, ((_, _, _, dado), (g0, g1)) in enumerate(zip(GRUPOS, gs)):
            cx = (g0 + g1) / 2
            usado = t >= ini[j] + 0.1
            fundo = COR if usado else TINTA
            E.foco(c, t, C["s04.a"] + 0.6 + 0.15 * j, 0.4, lambda a, cx=cx, dado=dado, fundo=fundo: E.pilula(c, dado, cx, 760, 40, "b", fundo=fundo, cor=BR, a=a))
            p = ep(t, ini[j] + 0.2, 0.4)
            if p > 0:
                M.arrow(c, cx, 715, cx, 715 - 90 * p, COR, p, 5, 16, p)
        # o "10" do horário não entra
        if t >= C["s07.b"] + 0.3:
            g0, g1 = gs[3]
            cx = (g0 + g1) / 2
            E.risco(c, cx - 150, 772, cx - 70, 748, t, C["s07.b"] + 0.3, largura=8)
            E.foco(c, t, C["s07.b"] + 0.6, 0.4, lambda a: E.pilula(c, "horário ≠ turno", cx - 40, 850, 34, "g", fundo=E.ERRADO, cor=BR, a=a))
        if t >= C["s05.a"] + 0.4 and t < C["s06.a"]:
            g0, g1 = gs[1]
            E.foco(c, t, C["s05.a"] + 0.4, 0.4, lambda a: E.pilula(c, "zero à esquerda", (g0 + g1) / 2, 850, 34, "g", fundo=E.ERRADO, cor=BR, a=a))
    E.saida(c, t, C["s08"], dados)

    # o código e a alternativa
    E.frase(c, t, C["s08.a"] + 0.2, [("código:", "i", 80, TINTA2), (CODIGO, "g", 120, CERTO)], W / 2 - 110, 900, "center", 0.2)
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "7 dígitos, cada um na sua casa", W / 2 - 110, 990, 34, "b", fundo=TINTA, cor=BR, a=a))
    s = pop(t, C["s08.c"], 0.5)
    if s > 0:
        E.bola(c, 1560, 860, 95 * s, CERTO)
        centro(c, "D", 1560, 860 + 40 * s, 110 * s, "g", BR)


# ---------------- 5. por que as outras estão erradas ----------------
def pedaco(c, x, y, s_, rot, errado, a, ok=False):
    """um pedaço do código: dígitos numa caixa, com o que a alternativa pôs ali embaixo"""
    dw, h = 52, 86
    w = len(s_) * dw + 26
    cor = E.ERRADO if errado else (CERTO if ok else COR)
    M.rrect(c, x, y - h / 2, w, h, 14, "#FFF1F1" if errado else BR, a, shadow=True)
    M.rrect(c, x, y - h / 2, w, h, 14, None, a, stroke=4, stroke_color=cor)
    for i, ch in enumerate(s_):
        centro(c, ch, x + 13 + dw * i + dw / 2, y + 22, 62, "g", cor if errado else TINTA, a)
    centro(c, rot, x + w / 2, y + h / 2 + 34, 28, "b", cor, a)
    return w


def b_pegadinhas(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s09.{k}"] for k in "abcde")
    E.frase(c, t, a_, [("por que as outras", "i", 60, COR), ("estão erradas", "g", 60, TINTA)], XE, 130, "left", 0.15)
    tl = {"A": b_, "B": c_, "C": d_, "D": a_ + 0.6, "E": e_}
    for k, (l, _) in enumerate(ALT):
        y = 260 + k * 160
        a = ep(t, tl[l], 0.45)
        if a <= 0:
            continue
        ok = l == "D"
        E.bola(c, 210, y, 46, CERTO if ok else E.ERRADO, a)
        centro(c, l, 210, y + 20, 56, "g", BR, a)
        x = 300
        pecas, nota = LEITURA[l]
        for s_, rot, err in pecas:
            x += pedaco(c, x, y, s_, rot, bool(err) and not ok, a, ok) + 18
        E.escreve(c, nota, 1000, y + 16, 44, "b" if not ok else "g", CERTO if ok else E.ERRADO, a)
        if ok:
            E.selo(c, 1500, y, 34 * pop(t, tl[l] + 0.3), True)


# ---------------- 6. o atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s10.a"], [("o", "i", 90, CLARO), ("atalho", "g", 90, BR)], XE, 170, "left", 0.15)
    E.frase(c, t, C["s10.a"] + 0.5, [("sem montar o código", "i", 54, CLARO)], XE, 245, "left")
    x0, y0, dy, dx, sz = 640, 360, 128, 92, 92
    for col, tc in ((0, C["s10.b"]), (1, C["s10.d"])):
        p = ep(t, tc, 0.4)
        if p > 0:
            M.rrect(c, x0 + col * dx - 8, y0 - dy * 0.55, dx - 4, dy * 5 - 20, 20, E.COR, 0.55 * p)
    cortes = {"A": C["s10.c"], "B": C["s10.c"] + 0.35, "C": C["s10.c"] + 0.7, "E": C["s10.e"]}
    for k, (l, s) in enumerate(ALT):
        y = y0 + k * dy
        a = ep(t, C["s10.a"] + 0.6 + 0.12 * k, 0.4)
        if a <= 0:
            continue
        tc = cortes.get(l)
        aa = a * (0.35 if tc is not None and t >= tc + 0.35 else 1)
        certo = l == "D" and t >= C["s10.f"]
        E.bola(c, x0 - 110, y, 46, CERTO if certo else E.COR, aa)
        centro(c, l, x0 - 110, y + 20, 56, "g", BR, aa)
        for i, ch in enumerate(s):
            centro(c, ch, x0 + i * dx + dx / 2 - 10, y + 34, sz, "g", "#5BE3A4" if certo else BR, aa)
        if tc is not None and t >= tc:
            E.risco(c, x0 - 170, y + 5, x0 + 7 * dx + 10, y - 5, t, tc, largura=10)
    E.foco(c, t, C["s10.b"] + 0.3, 0.45, lambda a: E.pilula(c, "andar = 2", 1600, 430, 46, "g", fundo=E.COR, cor=BR, a=a))
    E.foco(c, t, C["s10.d"] + 0.3, 0.45, lambda a: E.pilula(c, "setor = 0 8", 1600, 560, 46, "g", fundo=E.COR, cor=BR, a=a))
    if t >= C["s10.f"]:
        E.selo(c, x0 + 7 * dx + 70, y0 + 3 * dy, 50 * pop(t, C["s10.f"]), True)
        E.foco(c, t, C["s10.f"] + 0.3, 0.45, lambda a: E.pilula(c, "2 olhares", 1600, 750, 46, "g", fundo=CERTO, cor=BR, a=a))


# ---------------- 7. desafio ----------------
def b_desafio(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s11.{k}"] for k in "abcd")
    E.frase(c, t, a_, [("agora", "i", 80, COR), ("é com você", "g", 80, TINTA)], W / 2, 200, "center", 0.15)
    for j, s_ in enumerate(("15 h · tarde", "funcionário 42", "setor 15", "4º andar")):
        E.foco(c, t, b_ + 0.2 + 1.3 * j, 0.4, lambda a, s_=s_, j=j: E.pilula(c, s_, 330 + j * 420, 340, 42, "b", fundo=TINTA, cor=BR, a=a))
    xs, gs = layout(130, 12, 46)
    for i, x in enumerate(xs):
        s = pop(t, c_ + 0.05 * i, 0.4)
        if s > 0:
            casa(c, x, 470, 130, 160, min(1, s * 1.2), s=s)
            digito(c, "?", x, 470, 130, 160, CINZA, min(1, s))
    for (nome, _, _, _), (g0, g1) in zip(GRUPOS, gs):
        E.foco(c, t, c_ + 0.3, 0.4, lambda a, g0=g0, g1=g1, nome=nome: centro(c, nome, (g0 + g1) / 2, 700, 40, "g", COR, a))
    s = pop(t, d_, 0.5)
    if s > 0:
        c.save(); c.translate(W / 2, 880); c.scale(s, s)
        E.pilula(c, "responda nos comentários", 0, 0, 52, "g", fundo=E.COR, cor=BR)
        c.restore()


# ---------------- 8. resumo ----------------
def b_resumo(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("resumo", "g", 80, TINTA)], XE, 200, "left")
    itens = (("separe o código em pedaços", "s12.b"), ("complete com zeros à esquerda", "s12.c"),
             ("horário não é turno", "s12.d"))
    for k, (s_, cue) in enumerate(itens):
        y = 380 + k * 190
        sb = pop(t, C[cue], 0.45)
        if sb > 0:
            E.bola(c, XE + 60, y, 56 * sb, E.COR)
            centro(c, str(k + 1), XE + 60, y + 26 * sb, 70 * sb, "g", BR)
        E.frase(c, t, C[cue] + 0.1, [(s_, "g", 72, TINTA)], XE + 160, y + 26, "left")


# ---------------- 9. aulas do canal ----------------
AULAS = (("Algarismos e", "valor posicional", "s13.b"), ("Achar a pergunta", "e os dados úteis", "s13.c"))


def b_aulas(c, t, C, b):
    E.frase(c, t, C["s13.a"], [("aulas completas", "g", 72, TINTA), ("no canal", "i", 72, COR)], W / 2, 200, "center", 0.15)
    for k, (l1, l2, cue) in enumerate(AULAS):
        s = pop(t, C[cue], 0.5)
        if s <= 0:
            continue
        cx = W / 2 + (-380 if k == 0 else 380)
        c.save(); c.translate(cx, 520); c.scale(s, s)
        M.rrect(c, -330, -200, 660, 400, 30, BR, 1, shadow=True)
        M.rrect(c, -330, -200, 660, 90, 30, E.COR, 1)
        c.drawRect(skia.Rect.MakeXYWH(-330, -140, 660, 30), M.paint(E.COR))
        centro(c, "AULA", 0, -138, 44, "g", BR)
        centro(c, l1, 0, 20, 58, "g", TINTA)
        centro(c, l2, 0, 100, 58, "g", COR)
        c.restore()
    E.frase(c, t, C["s13.d"] + 0.3, [("procure essas aulas", "i", 60, TINTA2), ("aqui no canal", "g", 60, TINTA)], W / 2, 830, "center", 0.15)
    s = pop(t, C["s13.e"] + 0.5, 0.45)
    if s > 0:
        clk = 1 - 0.06 * math.sin(math.pi * clamp(prog(t, C["s13.e"] + 0.9, 0.25)))
        c.save(); c.translate(W / 2, 960); c.scale(s * clk, s * clk)
        inscrito = t >= C["s13.e"] + 1.0
        E.pilula(c, "INSCRITO ✓" if inscrito else "INSCREVA-SE", 0, 0, 60, "g", fundo=TINTA2 if inscrito else E.ERRADO, cor=BR)
        c.restore()


BLOCKS = dict(gancho=b_gancho, posicao=b_posicao, zero=b_zero, monta=b_monta, pegadinhas=b_pegadinhas,
              atalho=b_atalho, desafio=b_desafio, resumo=b_resumo, aulas=b_aulas)
