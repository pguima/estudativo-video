"""Visual — Função Composta e Função Inversa, Episódio 4: quem tem inversa e o espelho na reta y = x (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: Plano (plano cartesiano quadrado com a diagonal y = x), dobra() (a folha dobrando na diagonal e
carimbando o reflexo), flechas() (diagrama de flechas com selo "dois donos" / "ninguém chega"), armarios() (chaves e
armários), tabela().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
A função f (e a exponencial) é AZUL; a inversa (e o logaritmo) é ROXA em todo o episódio.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum045", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                 K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_composta_inversa_ep4_bijetora_espelho.mp4"
CARD_R = K.CARD_R
COL_F, COL_I = BLUE, PURPLE
TINTA = "#7C5CFA"


# ======================================================================
# peças do episódio
# ======================================================================

class Plano:
    """plano quadrado de L0 a L1 nos dois eixos; (ox, oy) = pixel da origem; u = pixels por unidade"""

    def __init__(self, cx, cy, lado, L0=-2, L1=9):
        self.L0, self.L1 = L0, L1
        self.u = lado / (L1 - L0)
        self.x0 = cx - lado / 2
        self.y1 = cy + lado / 2
        self.lado = lado

    def P(self, x, y):
        return self.x0 + (x - self.L0) * self.u, self.y1 - (y - self.L0) * self.u

    def fundo(self, c, a, diag=1.0, grade=True):
        if a <= 0:
            return
        x0, y0 = self.P(self.L0, self.L1)
        rrect(c, x0 - 10, y0 - 10, self.lado + 20, self.lado + 20, 14, "#FFFFFF", a, shadow=True)
        if grade:
            for k in range(self.L0, self.L1 + 1):
                xa, ya = self.P(k, self.L0); xb, yb = self.P(k, self.L1)
                line(c, xa, ya, xb, yb, "#EDEDEA", a, 1.5)
                xa, ya = self.P(self.L0, k); xb, yb = self.P(self.L1, k)
                line(c, xa, ya, xb, yb, "#EDEDEA", a, 1.5)
        xa, ya = self.P(self.L0, 0); xb, yb = self.P(self.L1, 0)
        arrow(c, xa, ya, xb + 6, yb, INK2, a, 3, 12)
        xa, ya = self.P(0, self.L0); xb, yb = self.P(0, self.L1)
        arrow(c, xa, ya, xb, yb - 6, INK2, a, 3, 12)
        ex, ey = self.P(self.L1, 0)
        text(c, "x", ex - 6, ey + 34, 24, "black", GRAY, a)
        ex, ey = self.P(0, self.L1)
        text(c, "y", ex - 22, ey + 16, 24, "black", GRAY, a)
        if diag > 0:
            xa, ya = self.P(self.L0, self.L0); xb, yb = self.P(self.L1, self.L1)
            line(c, xa, ya, xb, yb, AMBER, a * diag, 4, dash=[16, 12])
            lx, ly = self.P(self.L1 - 1.6, self.L1 - 0.6)
            text(c, "y = x", lx, ly, 22, "black", AMBER, a * diag)

    def curva(self, c, f, xa, xb, col, a, prog_=1.0, width=6, k=1.0, n=120, clip=True):
        """desenha y = f(x) de xa a xb; k = fator da dobra (1 = original, −1 = refletida em y = x)"""
        if a <= 0 or prog_ <= 0:
            return
        path = skia.Path(); first = True
        xe = xa + (xb - xa) * prog_
        for i in range(n + 1):
            x = xa + (xe - xa) * i / n
            y = f(x)
            if clip and not (self.L0 - 0.01 <= y <= self.L1 + 0.01):
                first = True
                continue
            m = (x + y) / 2
            xx, yy = m + k * (x - m), m + k * (y - m)
            px, py = self.P(xx, yy)
            if first:
                path.moveTo(px, py); first = False
            else:
                path.lineTo(px, py)
        c.drawPath(path, paint(col, a, stroke=width, cap_round=True))

    def ponto(self, c, x, y, col, a, rot=None, lado="dir", r=11, size=26):
        if a <= 0:
            return
        px, py = self.P(x, y)
        c.drawCircle(px, py, r + 6, paint(col, a * 0.18))
        c.drawCircle(px, py, r, paint(col, a))
        if rot:
            dx = 22 if lado == "dir" else -22
            text(c, rot, px + dx, py - 16, size, "black", col, a, align="left" if lado == "dir" else "right")


def dobra(c, pl, k, a, cor_papel="#F4F1FF"):
    """aba de papel (metade acima da diagonal) dobrando: k de 1 (aberta) a −1 (dobrada sobre a outra metade)"""
    if a <= 0 or k >= 0.999:
        return
    pts = [(pl.L0, pl.L0), (pl.L0, pl.L1), (pl.L1, pl.L1)]
    path = skia.Path()
    for i, (x, y) in enumerate(pts):
        m = (x + y) / 2
        px, py = pl.P(m + k * (x - m), m + k * (y - m))
        (path.moveTo if i == 0 else path.lineTo)(px, py)
    path.close()
    sh = abs(k)
    c.drawPath(path, paint(mix("#FFFFFF", cor_papel, 0.6 + 0.4 * (1 - sh)), a * (0.55 + 0.35 * (1 - sh))))
    c.drawPath(path, paint("#B9B2D9", a, stroke=2))


def flechas(c, cx, cy, esq, dir_, pares, a, prog_=1.0, col=None, sozinho=None, rot_e="entradas", rot_d="saídas",
            w=560, h=360, dest=None):
    """diagrama de flechas: dois ovais (entradas / saídas) e flechas pares = [(i_esq, j_dir)]"""
    if a <= 0:
        return {}
    col = col or COL_F
    xl, xr = cx - w / 2, cx + w / 2
    for xx, lst, rot in ((xl, esq, rot_e), (xr, dir_, rot_d)):
        c.drawOval(skia.Rect.MakeLTRB(xx - 90, cy - h / 2, xx + 90, cy + h / 2), paint(mix("#FFFFFF", col, 0.08), a))
        c.drawOval(skia.Rect.MakeLTRB(xx - 90, cy - h / 2, xx + 90, cy + h / 2), paint(col, a, stroke=4))
        text(c, rot, xx, cy - h / 2 - 22, 24, "black", GRAY, a)
    pos = {}
    for lado, xx, lst in (("e", xl, esq), ("d", xr, dir_)):
        n = len(lst)
        for i, s in enumerate(lst):
            y = cy - h / 2 + h * (i + 1) / (n + 1)
            pos[(lado, i)] = (xx, y)
            cor = AMBER if dest and (lado, i) in dest else INK
            fmid(c, s, xx, y, 40, "black", cor, a)
    for n_, (i, j) in enumerate(pares):
        (x0, y0), (x1, y1) = pos[("e", i)], pos[("d", j)]
        pr = clamp(prog_ * len(pares) - n_)
        cor = AMBER if dest and (("e", i) in dest or ("d", j) in dest) else col
        arrow(c, x0 + 42, y0, x1 - 46, y1, cor, a, 4, 14, progress=pr)
    return pos


def armarios(c, cx, cy, a, t=0.0, t_volta=1e9, abre=None):
    """4 chaves à esquerda, 4 armários à direita, uma flecha por chave; 'abre' = índice do armário aberto"""
    if a <= 0:
        return
    for i in range(4):
        y = cy - 210 + i * 140
        # chave
        kx = cx - 330
        c.drawCircle(kx - 40, y, 26, paint(AMBER, a, stroke=9))
        rrect(c, kx - 16, y - 7, 90, 14, 5, AMBER, a)
        rrect(c, kx + 50, y + 4, 10, 20, 3, AMBER, a)
        rrect(c, kx + 30, y + 4, 10, 16, 3, AMBER, a)
        text(c, str(i + 1), kx - 40, y + 9, 22, "black", AMBER, a)
        # armário
        ax = cx + 230
        aberto = abre == i
        rrect(c, ax, y - 58, 150, 116, 12, mix("#FFFFFF", BLUE, 0.20 if aberto else 0.10), a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(ax, y - 58, 150, 116), 12, 12), paint(BLUE, a, stroke=4))
        c.drawCircle(ax + 128, y, 7, paint(BLUE, a))
        text(c, "ABCD"[i], ax + 60, y + 14, 40, "black", BLUE, a)
        arrow(c, kx + 100, y, ax - 16, y, INK2, a, 4, 14, progress=ep(t, 0, 0.6) if t else 1.0)
        if aberto:
            av = ep(t, t_volta, 0.6)
            if av > 0:
                p = skia.Path(); p.moveTo(ax + 75, y + 62); p.cubicTo(ax + 40, y + 130, kx + 60, y + 130, kx - 30, y + 34)
                pp = paint(GREEN, av, stroke=5, cap_round=True); pp.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
                c.drawPath(p, pp)
                pill(c, "dá para VOLTAR", cx, y + 112, GREEN, size=24, a=av, anchor="center")


def tabela(c, x, y, linhas, a, cw=120, rh=86, cor_rot=None, hl=None, lw=150):
    """linhas = [(rótulo, [valores])]; hl = {(linha, coluna): cor} destaca células. Coluna 0 = rótulos."""
    if a <= 0:
        return
    ncol = len(linhas[0][1])
    W_ = lw + cw * ncol
    rrect(c, x, y, W_, rh * len(linhas), 12, "#FFFFFF", a, shadow=True)
    for r, (rot, vals) in enumerate(linhas):
        yy = y + r * rh
        rrect(c, x, yy, lw, rh, 0, mix("#FFFFFF", (cor_rot or {}).get(r, GRAY), 0.14), a)
        fmid(c, rot, x + lw / 2, yy + rh / 2, 34, "black", (cor_rot or {}).get(r, INK), a)
        for j, v in enumerate(vals):
            cx_ = x + lw + cw * j + cw / 2
            hc = (hl or {}).get((r, j))
            if hc:
                rrect(c, cx_ - cw / 2 + 6, yy + 6, cw - 12, rh - 12, 12, hc, a * 0.22)
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx_ - cw / 2 + 6, yy + 6, cw - 12, rh - 12), 12, 12),
                            paint(hc, a, stroke=4))
            fmid(c, str(v), cx_, yy + rh / 2, 38, "black", hc or INK, a)
        if r > 0:
            line(c, x, yy, x + W_, yy, LINE, a, 2)
    for j in range(ncol + 1):
        xx = x + lw + cw * j
        line(c, xx, y, xx, y + rh * len(linhas), LINE, a, 2)
    return W_


def cel(x, y, r, j, cw=120, rh=86, lw=150):
    return x + lw + cw * j + cw / 2, y + r * rh + rh / 2


def rotulo(c, s, cx, cy, col, a, size=26):
    pill(c, s, cx, cy, col, size=size, a=a, anchor="center")


exp2 = lambda x: 2 ** x
log2 = lambda x: math.log2(x) if x > 0 else -99


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "QUEM TEM INVERSA?", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        K.expr(c, "(?)^2 = 9", W / 2, 300, 110, aa, cores={0: AMBER})
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        for k, (s_, x) in enumerate((("3", 640), ("−3", 1280))):
            a = ep(t, C["01.b"] + k * 0.9, 0.4)
            c.drawCircle(x, 520, 74, paint("#FFFFFF", a)); c.drawCircle(x, 520, 74, paint(BLUE, a, stroke=7))
            fmid(c, s_, x, 520, 64, "black", BLUE, a)
            K.expr(c, f"({s_})^2 = 9", x, 650, 46, a)
        fmid(c, "ou", W / 2, 520, 48, "black", GRAY, ep(t, C["01.b"] + 0.9, 0.4))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 760, acc, "ESSA DÚVIDA TEM NOME", AMBER, -3, 34)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        pill(c, "dá para DESFAZER a função?", W / 2, 860, PURPLE, size=30, a=ad, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = (("02.a", "dizer se uma função TEM INVERSA"), ("02.b", "achar pontos e o gráfico pelo ESPELHO"),
             ("02.c", "ler inversas em TABELAS"))
    for k, (cue, s_) in enumerate(itens):
        a, d = rise(t, C[cue])
        check_icon(c, 300, 316 + k * 150 + d, 34, a, GREEN)
        text(c, s_, 360, 330 + k * 150 + d, 50, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "Episódio 3", 400, 270, 26, "bold", GRAY, aa)
        K.expr(c, "f(1) = 3", 400, 370, 52, aa, cores={0: COL_F})
        K.expr(c, "f⁻¹(3) = 1", 400, 470, 52, ep(t, C["03.a"] + 1.4, 0.4), cores={0: COL_I})
        text(c, "a inversa DESFAZ o caminho", 400, 560, 28, "black", PURPLE, ep(t, C["03.a"] + 1.4, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "Conceito de Função", 1000, 270, 26, "bold", GRAY, ab)
        pill(c, "DOMÍNIO = o que pode entrar", 1000, 380, BLUE, size=30, a=ab, anchor="center")
        pill(c, "IMAGEM = o que de fato sai", 1000, 480, BLUE, size=30, a=ep(t, C["03.b"] + 1.4, 0.4), anchor="center")
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        text(c, "Exponencial e Logaritmo", 1560, 270, 26, "bold", GRAY, acc)
        K.expr(c, "2^3 = 8", 1560, 370, 54, acc, cores={0: COL_F})
        fmid(c, "⇔", 1560, 450, 50, "black", GRAY, acc)
        K.expr(c, "log₂ 8 = 3", 1560, 530, 54, acc, cores={0: COL_I})
        text(c, "a mesma informação", 1560, 610, 28, "black", GREEN, acc)
    line(c, 700, 240, 700, 760, "#E6E6E2", ab, 3)
    line(c, 1300, 240, 1300, 760, "#E6E6E2", acc, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "O ARMÁRIO DE CHAVES", "DÁ PARA VOLTAR?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    armarios(c, 760, 500, aa, t - C["04.a"] if t > C["04.a"] else 0.001, C["04.c"] - C["04.a"],
             abre=2 if t >= C["04.c"] else None)
    ab = ep(t, C["04.a"], 0.5)
    if ab > 0:
        pill(c, "cada chave → UM armário", 1460, 380, BLUE, size=28, a=ab, anchor="center")
    pill(c, "todo armário TEM chave", 1460, 480, BLUE, size=28, a=ep(t, C["04.b"], 0.4), anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "assim dá para VOLTAR", 1460, 640, ad, 32, GREEN)


# ======================================================================
# blocos a–d: injetora, sobrejetora, bijetora, restringir
# ======================================================================

def b_injetora(c, t, C, B):
    head_seq(c, t, C, [("05", "INJETORA", "CADA SAÍDA, UM DONO", BLUE), ("06", "ATALHO", "TESTE x E −x", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            armarios(c, 560, 500, aa * (1 - ep(t, C["05.b"], 0.4)), 0)
            selo(c, 560, 780, aa * (1 - ep(t, C["05.b"], 0.4)), "2 CHAVES, 1 ARMÁRIO?", AMBER, -3, 28)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            rrect(c, 230, 250, 700, 200, 22, mix("#FFFFFF", BLUE, 0.10), ab)
            text(c, "INJETORA", 580, 310, 32, "black", BLUE, ab)
            para(c, "entradas diferentes dão saídas diferentes", 270, 380, 34, "black", INK, ab, 640, 44)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            K.expr(c, "f(x) = x^2", 580, 540, 52, acc, cores={0: COL_F})
            K.expr(c, "(−3)^2 = 3^2 = 9", 580, 640, 50, acc)
            text(c, "nos números reais", 580, 720, 26, "black", GRAY, acc)
        flechas(c, 1340, 520, ["−3", "3", "2"], ["9", "4"], [(0, 0), (1, 0), (2, 1)], acc,
                ep(t, C["05.c"] + 0.5, 1.6), dest={("e", 0), ("e", 1), ("d", 0)} if t >= C["05.d"] else None,
                w=520, h=380)
        ad = ep(t, C["05.d"], 0.4)
        if ad > 0:
            selo(c, 1340, 790, ad, "DOIS DONOS", AMBER, -4, 32)
    else:
        aa = ep(t, C["06.a"], 0.5)
        K.atalho(c, 300, 250, 1320, 140, "ATALHO", ["teste um número e o OPOSTO dele: 2 e −2"], aa, 34)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            regra(c, "mesma saída?  NÃO é injetora", W / 2, 470, ab, 34, AMBER)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            K.expr(c, "2^2 = 4", 700, 640, 60, acc)
            K.expr(c, "(−2)^2 = 4", 1220, 640, 60, acc)
            selo(c, W / 2, 760, acc, "MESMA SAÍDA", RED, -3, 30)


def b_sobrejetora(c, t, C, B):
    head(c, t, B["start"], "SOBREJETORA", "TODO ENDEREÇO É ATINGIDO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 230, 720, 180, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "CONTRADOMÍNIO", 580, 285, 30, "black", BLUE, aa)
        para(c, "as saídas que a função PROMETE", 270, 350, 34, "black", INK, aa, 640, 44)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 220, 440, 720, 180, 22, mix("#FFFFFF", BLUE, 0.10), ab)
        text(c, "SOBREJETORA", 580, 495, 30, "black", BLUE, ab)
        para(c, "TODA saída prometida é atingida", 270, 560, 34, "black", INK, ab, 640, 44)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        K.expr(c, "f(x) = 2^x", 580, 690, 52, acc, cores={0: COL_F})
        text(c, "promete todos os reais", 580, 770, 26, "black", GRAY, acc)
    flechas(c, 1340, 520, ["0", "1", "2", "3"], ["1", "2", "4", "8", "−1"], [(0, 0), (1, 1), (2, 2), (3, 3)], acc,
            ep(t, C["07.c"] + 0.5, 1.6), dest={("d", 4)} if t >= C["07.d"] else None, w=520, h=440)
    ad = ep(t, C["07.d"], 0.4)
    if ad > 0:
        selo(c, 1480, 800, ad, "NINGUÉM CHEGA", AMBER, -4, 30)
        pill(c, "2ˣ é sempre POSITIVO", 1130, 800, BLUE, size=24, a=ad, anchor="center")


def b_bijetora(c, t, C, B):
    head(c, t, B["start"], "BIJETORA", "QUEM TEM INVERSA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        linha_ = [("INJETORA", BLUE), ("  +  ", GRAY), ("SOBREJETORA", BLUE), ("  =  ", GRAY), ("BIJETORA", PURPLE)]
        ws = [ftext_w(s, "black", 50) for s, _ in linha_]
        x = W / 2 - sum(ws) / 2
        for (s, col), w_ in zip(linha_, ws):
            ftext(c, s, x, 330, 50, "black", col, aa, align="left"); x += w_
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        check_icon(c, 480, 450, 30, ab, GREEN)
        text(c, "cada saída com UM dono", 530, 464, 42, "black", INK, ab, align="left")
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        check_icon(c, 480, 560, 30, acc, GREEN)
        text(c, "todo endereço EXISTE", 530, 574, 42, "black", INK, acc, align="left")
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        regra(c, "faltou uma?  NÃO existe inversa", W / 2, 730, ad, 38, PURPLE)


def b_restringir(c, t, C, B):
    head(c, t, B["start"], "RESTRINGIR O DOMÍNIO", "SALVA A INVERSA", BLUE)
    card(c, *CARD_R)
    pl = Plano(520, 500, 600, -4, 4)
    a0 = ep(t, C["09"], 0.5)
    pl.fundo(c, a0, diag=0, grade=True)
    ab = ep(t, C["09.b"], 0.6)
    pl.curva(c, lambda x: x * x / 2, -4, 0, COL_F, a0 * (1 - 0.75 * ab), 1.0, 6)
    pl.curva(c, lambda x: x * x / 2, 0, 4, COL_F, a0, 1.0, 7)
    if ab > 0:
        x0, y0 = pl.P(-4, -4); x1, _ = pl.P(0, -4)
        rrect(c, x0, y0 - pl.lado, x1 - x0, pl.lado, 0, "#9AA0AA", ab * 0.18)
        text(c, "não entra", (x0 + x1) / 2, pl.P(0, -3)[1], 26, "black", GRAY, ab)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, 900, 230, 820, 150, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "RESTRINGIR O DOMÍNIO", 1310, 285, 30, "black", BLUE, aa)
        text(c, "deixar entrar só uma parte dos números", 1310, 345, 32, "black", INK, aa)
    if ab > 0:
        K.expr(c, "x^2 , com x ≥ 0", 1310, 450, 50, ab, cores={0: COL_F})
        text(c, "o 9 tem UM dono só: o 3", 1310, 530, 32, "black", GREEN, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        K.expr(c, "f⁻¹(x) = √x", 1310, 630, 56, acc, cores={0: COL_I})
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        regra(c, "√9 = 3  (e não −3)", 1310, 760, ad, 36, PURPLE)


# ======================================================================
# blocos e–f: o espelho e o par exponencial–logaritmo
# ======================================================================

def _desenho(x):
    """o 'desenho de tinta' do bloco e: uma onda acima da diagonal"""
    return 2.4 + 0.25 * x * x + 0.6 * math.sin(x * 1.6)


def b_espelho(c, t, C, B):
    head_seq(c, t, C, [("10", "O GRÁFICO DA INVERSA", "A FOLHA DOBRADA", BLUE),
                       ("11", "POR QUE ESSA RETA?", "TROCAR AS COORDENADAS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    pl = Plano(560, 495, 640, -1, 6)
    a0 = ep(t, C["10"], 0.5)
    if sid == "10":
        pl.fundo(c, a0, diag=ep(t, C["10.b"], 0.5), grade=False)
        aa = ep(t, C["10.a"], 0.5)
        pl.curva(c, _desenho, -0.6, 2.3, COL_F, aa, ep(t, C["10.a"], 1.4), 9)
        kd = 1 - 2 * ease_io(ep(t, C["10.b"] + 0.4, 1.2)) + 2 * ease_io(ep(t, C["10.c"], 1.0))
        dobra(c, pl, kd, aa)
        if kd < 0.999 and aa > 0:
            pl.curva(c, _desenho, -0.6, 2.3, COL_F, aa * 0.9, 1.0, 9, k=kd)
        acc = ep(t, C["10.c"] + 0.6, 0.6)
        pl.curva(c, _desenho, -0.6, 2.3, TINTA, acc, 1.0, 9, k=-1)
        if acc > 0:
            pill(c, "SIMÉTRICO = igual, mas espelhado", 1360, 470, PURPLE, size=28, a=acc, anchor="center")
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            rrect(c, 980, 560, 760, 210, 22, mix("#FFFFFF", AMBER, 0.12), ad)
            text(c, "A RETA y = x", 1360, 615, 32, "black", AMBER, ad)
            text(c, "as duas coordenadas iguais", 1360, 675, 32, "black", INK, ad)
            K.expr(c, "(1,1)   (2,2)   (3,3)", 1360, 735, 38, ad)
            for k in (1, 2, 3):
                pl.ponto(c, k, k, AMBER, ad, r=8)
        ab = ep(t, C["10.b"], 0.4)
        if ab > 0 and t < C["10.c"]:
            pill(c, "dobre na DIAGONAL", 1360, 330, AMBER, size=30, a=ab, anchor="center")
    else:
        pl.fundo(c, 1, diag=1)
        aa = ep(t, C["11.a"], 0.5)
        pl.ponto(c, 1, 3, COL_F, aa, "(1, 3)", "esq")
        if aa > 0:
            K.expr(c, "f(1) = 3", 1360, 300, 54, aa, cores={0: COL_F})
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            x0, y0 = pl.P(1, 3); x1, y1 = pl.P(3, 1)
            line(c, x0, y0, x1, y1, GRAY, ab, 3, dash=[8, 8])
            pl.ponto(c, 3, 1, COL_I, ab, "(3, 1)")
            K.expr(c, "f⁻¹(3) = 1", 1360, 410, 54, ab, cores={0: COL_I})
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            K.expr(c, "(1,3) → (3,1)", 1360, 540, 60, acc, cores={0: COL_F, 2: COL_I})
            text(c, "trocar entrada e saída = refletir em y = x", 1360, 620, 28, "black", AMBER, acc)
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            for k, s_ in enumerate(("não no eixo y", "nem na origem")):
                x = 1170 + k * 380
                pill(c, s_, x, 740, RED, size=28, a=ad, anchor="center")


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO DO ESPELHO", "PONTO DA INVERSA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    K.atalho(c, 300, 250, 1320, 140, "ATALHO", ["troque as duas coordenadas de LUGAR"], aa, 36)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        K.expr(c, "(a,b)", 640, 560, 100, ab, cores={0: COL_F})
        arrow(c, 840, 560, 1060, 560, INK2, ab, 6, 22)
        K.expr(c, "(b,a)", 1280, 560, 100, ab, cores={0: COL_I})
        text(c, "função", 640, 670, 30, "black", COL_F, ab)
        text(c, "inversa", 1280, 670, 30, "black", COL_I, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        pill(c, "nenhum sinal muda: só a ORDEM", W / 2, 770, AMBER, size=30, a=acc, anchor="center")


def _par(c, t, pl, t_pinta, t_dobra, t_desdobra, a0):
    """a exponencial pintada, a folha dobrando e o logaritmo carimbado"""
    ap = ep(t, t_pinta, 0.4)
    pl.curva(c, exp2, -2, math.log2(9), COL_F, a0 * ap, ep(t, t_pinta, 1.4), 7)
    kd = 1 - 2 * ease_io(ep(t, t_dobra, 1.2)) + 2 * ease_io(ep(t, t_desdobra, 1.0))
    dobra(c, pl, kd, a0)
    if kd < 0.999:
        pl.curva(c, exp2, -2, math.log2(9), COL_F, a0 * 0.9, 1.0, 7, k=kd)
    pl.curva(c, exp2, -2, math.log2(9), COL_I, a0 * ep(t, t_desdobra + 0.5, 0.6), 1.0, 7, k=-1)


def b_par(c, t, C, B):
    head_seq(c, t, C, [("13", "O PAR MAIS COBRADO", "EXPONENCIAL E LOGARITMO", BLUE),
                       ("14", "DOMÍNIO E IMAGEM", "TROCAM DE LUGAR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    pl = Plano(560, 495, 640, -2, 9)
    if sid == "13":
        a0 = ep(t, C["13"], 0.5)
        pl.fundo(c, a0, diag=ep(t, C["13.b"], 0.5))
        _par(c, t, pl, C["13.b"], C["13.b"] + 1.6, C["13.c"], a0)
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            K.expr(c, "y = 2^x", 1360, 290, 60, aa, cores={2: COL_F})
            K.expr(c, "y = log₂ x", 1360, 400, 60, ep(t, C["13.a"] + 1.2, 0.4), cores={2: COL_I})
        acc = ep(t, C["13.c"] + 0.6, 0.5)
        if acc > 0:
            pill(c, "o carimbo é o LOGARITMO", 1360, 500, PURPLE, size=28, a=acc, anchor="center")
        ad = ep(t, C["13.d"], 0.5)
        pl.ponto(c, 0, 1, COL_F, ad, "(0, 1)", "esq")
        pl.ponto(c, 1, 0, COL_I, ep(t, C["13.d"] + 1.0, 0.4), "(1, 0)")
        if ad > 0:
            K.expr(c, "(0,1) → (1,0)", 1360, 640, 56, ad, cores={0: COL_F, 2: COL_I})
    else:
        pl.fundo(c, 1, diag=1)
        pl.curva(c, exp2, -2, math.log2(9), COL_F, 1, 1.0, 7)
        pl.curva(c, exp2, -2, math.log2(9), COL_I, 1, 1.0, 7, k=-1)
        for k, (cue, nome, col, dom, img) in enumerate((("14.a", "y = 2^x", COL_F, "todos os reais", "acima de zero"),
                                                       ("14.b", "y = log₂ x", COL_I, "acima de zero", "todos os reais"))):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            y = 250 + k * 260
            rrect(c, 980, y, 760, 220, 22, mix("#FFFFFF", col, 0.10), a)
            K.expr(c, nome, 1360, y + 50, 42, a, cores={2: col})
            text(c, "DOMÍNIO", 1170, y + 120, 24, "black", GRAY, a)
            text(c, dom, 1170, y + 170, 32, "black", INK, a)
            text(c, "IMAGEM", 1550, y + 120, 24, "black", GRAY, a)
            text(c, img, 1550, y + 170, 32, "black", INK, a)
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            regra(c, "domínio e imagem TROCAM de lugar", 1360, 790, acc, 30, PURPLE)


# ======================================================================
# nós fazemos e tabelas
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "NÓS FAZEMOS", GREEN), ("16", "VAMOS JUNTOS", "O ESPELHO FUNCIONA", GREEN)])
    card(c, *CARD_R)
    pl = Plano(560, 495, 640, -2, 9)
    pl.fundo(c, 1, diag=1)
    pl.curva(c, exp2, -2, math.log2(9), COL_F, 1, 1.0, 6)
    pl.curva(c, exp2, -2, math.log2(9), COL_I, 1, 1.0, 6, k=-1)
    aa = ep(t, C["15.a"], 0.5)
    pl.ponto(c, 3, 8, COL_F, aa, "(3, 8)")
    if aa > 0:
        K.expr(c, "y = 2^x  passa por  (3,8)", 1360, 300, 44, aa, cores={2: COL_F, 5: COL_F})
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        K.expr(c, "y = log₂ x  passa por  ?", 1360, 400, 44, ab, cores={2: COL_I, 5: AMBER})
    pause_timer(c, t, C["15.c"], 1360, 560)
    if t >= C["16"]:
        aa = ep(t, C["16.a"], 0.5)
        if aa > 0:
            x0, y0 = pl.P(3, 8); x1, y1 = pl.P(8, 3)
            line(c, x0, y0, x1, y1, GRAY, aa, 3, dash=[8, 8])
            pl.ponto(c, 8, 3, COL_I, aa, "(8, 3)", "esq")
            K.expr(c, "(3,8) → (8,3)", 1360, 540, 56, aa, cores={0: COL_F, 2: COL_I})
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            K.expr(c, "log₂ 8 = 3  porque  2^3 = 8", 1360, 650, 40, ab, cores={6: GREEN})
        acc = ep(t, C["16.c"], 0.5)
        if acc > 0:
            selo(c, 1360, 770, acc, "PONTO (8, 3)", GREEN, -3, 32)


TAB_X, TAB_Y = 260, 330
TAB_H = [("x", [1, 2, 3, 4]), ("h(x)", [3, 1, 4, 2]), ("k(x)", [2, 4, 1, 3])]


def b_tabela(c, t, C, B):
    head_seq(c, t, C, [("17", "INVERSA EM TABELA", "DE BAIXO PARA CIMA", BLUE),
                       ("18", "COMPOSTA EM TABELA", "DE DENTRO PARA FORA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["17", "18"])
    a0 = ep(t, C["17.a"], 0.5)
    hl = {}
    if sid == "17":
        linhas = TAB_H[:2]
        if t >= C["17.c"]:
            hl[(1, 2)] = PURPLE
        if t >= C["17.c"] + 2.2:
            hl[(0, 2)] = GREEN
        tabela(c, TAB_X, TAB_Y, linhas, a0, cw=140, rh=100, lw=170, cor_rot={0: GRAY, 1: COL_F}, hl=hl)
        if a0 > 0:
            text(c, "entradas", TAB_X - 20, TAB_Y + 62, 24, "black", GRAY, a0, align="right")
            text(c, "saídas", TAB_X - 20, TAB_Y + 162, 24, "black", COL_F, a0, align="right")
        ab = ep(t, C["17.b"], 0.5)
        if ab > 0:
            K.expr(c, "h⁻¹(4) = ?", 1420, 360, 64, ab, cores={0: COL_I})
        acc = ep(t, C["17.c"], 0.5)
        if acc > 0:
            pill(c, "qual ENTRADA dá 4?", 1420, 470, AMBER, size=30, a=acc, anchor="center")
            x1, y1 = cel(TAB_X, TAB_Y, 1, 2, 140, 100, 170)
            arrow(c, x1, y1 - 30, x1, y1 - 80, GREEN, ep(t, C["17.c"] + 2.2, 0.5), 6, 18)
        ad = ep(t, C["17.d"], 0.5)
        if ad > 0:
            K.expr(c, "h⁻¹(4) = 3", 1420, 600, 64, ad, cores={0: COL_I, 2: GREEN})
            K.atalho(c, 260, 640, 840, 150, "ATALHO", ["a inversa se lê de BAIXO para CIMA"], ad, 32)
    else:
        if t >= C["18.b"]:
            hl[(2, 0)] = COL_I
        if t >= C["18.c"]:
            hl[(1, 1)] = GREEN
        tabela(c, TAB_X, TAB_Y - 30, TAB_H, 1, cw=140, rh=100, lw=170, cor_rot={0: GRAY, 1: COL_F, 2: COL_I}, hl=hl)
        aa = ep(t, C["18.a"], 0.5)
        if aa > 0:
            K.expr(c, "h(k(1)) = ?", 1420, 330, 64, aa)
        ab = ep(t, C["18.b"], 0.5)
        if ab > 0:
            K.expr(c, "k(1) = 2", 1420, 440, 54, ab, cores={0: COL_I, 2: COL_I})
        acc = ep(t, C["18.c"], 0.5)
        if acc > 0:
            K.expr(c, "h(2) = 1", 1420, 540, 54, acc, cores={0: COL_F, 2: GREEN})
        ad = ep(t, C["18.d"], 0.5)
        if ad > 0:
            K.atalho(c, 260, 650, 1400, 150, "ATALHO DE TABELA",
                     ["função: de CIMA para BAIXO  ·  inversa: de BAIXO para CIMA"], ad, 32)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Só tem inversa quem é bijetora: cada saída com um dono, e todas existindo.",
          "O gráfico da inversa é o espelho em y = x: (a,b) vira (b,a).",
          "Em tabela, procure o número nas saídas."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Achar que x² tem inversa √x em todos os reais", "a raiz desfaz o quadrado nas contas do dia a dia",
          "o 9 tem dois donos: a volta só existe com x ≥ 0"),
         ("Refletir (1,3) no eixo y: (−1,3). Ou trocar os sinais: (−1,−3)",
          "espelho lembra virar para o outro lado", "o espelho é a DIAGONAL y = x: só a ordem troca, (3, 1)"),
         ("Para h⁻¹(4), procurar o 4 nas ENTRADAS e responder h(4)=2",
          "a gente sempre lê a tabela de cima para baixo", "qual entrada dá 4? procure nas SAÍDAS: a resposta é 3")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS7 = [("A", "= f(x) = x^2", "2 e −2: mesma saída", RED), ("B", "= f(x) = |x|", "2 e −2: mesma saída", RED),
         ("C", "= f(x) = 2^x", "nenhum x dá −1", RED), ("D", "= f(x) = x^3 + 1", "", GREEN),
         ("E", "= f(x) = 5", "de onde veio o 5?", RED)]


def b_q7(c, t, C, B):
    head_seq(c, t, C, [("23", "QUESTÃO 7 · EU FAÇO", "QUEM TEM INVERSA", BLUE),
                       ("24", "TESTANDO COM NÚMEROS", "QUEM CAI", AMBER), ("25", "SOBROU A D", "x³ + 1", GREEN)])
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    sid = which(t, C, ["23", "24", "25"])
    enun = ("Um programa de computador só consegue “desfazer” uma função f de ℝ em ℝ, recuperando cada entrada a partir "
            "da saída, quando f é bijetora. Entre as funções abaixo, todas de ℝ em ℝ, a única que o programa consegue "
            "desfazer é")
    yend = 240
    if sid == "23":
        yend = _enunciado(c, [(enun, INK)], a0, 240, 27)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        if t >= C["23.qe"]:
            text(c, "(E: para todo x real)", 1000, 800, 22, "black", GRAY, ep(t, C["23.qe"], 0.4), align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS7, 1000, 250, 690, 34, C["25.ok"], "D", cues_in, cues_x, gap=26)
    pause_timer(c, t, C["23.end"] - 1.9, 540, yend + 110)
    if sid == "24":
        y0 = 230
        _painel(c, y0, ep(t, C["24"], 0.4))
        for k, (cue, s_, col) in enumerate((("xa", "(2)^2 = (−2)^2 = 4", RED), ("xb", "|2| = |−2| = 2", RED),
                                            ("xc", "2^x = −1 ?  nenhum x", AMBER), ("xe", "sempre 5", RED))):
            a = ep(t, C["24." + cue], 0.4)
            if a > 0:
                badge_num(c, "ABCE"[k], 220, y0 + 80 + k * 130, a, 22, bg=col)
                K.expr(c, s_, 560, y0 + 80 + k * 130, 38, a)
        ac = ep(t, C["24.xc"], 0.4)
        if ac > 0:
            pill(c, "C: injetora, mas NÃO sobrejetora", 540, y0 + 560, AMBER, size=24, a=ac, anchor="center")
    elif sid == "25":
        y0 = 230
        _painel(c, y0, ep(t, C["25"], 0.4))
        aa = ep(t, C["25.a"], 0.4)
        if aa > 0:
            check_icon(c, 220, y0 + 70, 22, aa, GREEN)
            text(c, "sempre crescente: ninguém repete", 260, y0 + 82, 28, "black", INK, aa, align="left")
        ab = ep(t, C["25.b"], 0.4)
        if ab > 0:
            check_icon(c, 220, y0 + 160, 22, ab, GREEN)
            text(c, "atinge todos os reais", 260, y0 + 172, 28, "black", INK, ab, align="left")
            K.expr(c, "(−2)^3 + 1 = −7", 540, y0 + 240, 36, ab)
        acc = ep(t, C["25.c"], 0.4)
        if acc > 0:
            K.expr(c, "volta:  x = √[3]{y-1}", 540, y0 + 340, 42, acc, cores={0: COL_I})
        ad = ep(t, C["25.d"], 0.4)
        if ad > 0:
            K.atalho(c, 200, y0 + 400, 680, 190, "ATALHO: IDA E VOLTA",
                     [("m", "2 → 2^3 + 1 = 9"), ("m", "9 → √[3]{9-1} = 2")], ad, 30)


ALTS5 = [("A", "= (3,7)", "o ponto da própria f", RED), ("B", "= (7,3)", "", GREEN),
         ("C", "= (−3,−7)", "refletiu na origem", RED), ("D", "= (3,1/7)", "f⁻¹ não é 1/f", RED),
         ("E", "= (−7,−3)", "trocou os sinais", RED)]


def b_q5(c, t, C, B):
    head_seq(c, t, C, [("26", "QUESTÃO 5 · NÓS FAZEMOS", "PONTO DA INVERSA", GREEN),
                       ("27", "O QUE O PONTO DIZ?", "O ESPELHO", PURPLE)])
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    sid = which(t, C, ["26", "27"])
    enun = ("Uma função f, de ℝ em ℝ, é crescente e invertível, e seu gráfico passa pelo ponto (3,7). O gráfico da "
            "função inversa f⁻¹ certamente passa pelo ponto")
    yend = 240
    if sid == "26":
        yend = _enunciado(c, [(enun, INK)], a0, 240, 30)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS5, 1000, 250, 690, 40, C["27.ok"], "B", cues_in, cues_x, gap=26)
    pause_timer(c, t, C["26.end"] - 1.9, 540, yend + 130)
    if sid == "27":
        pl = Plano(540, 500, 560, -8, 8)
        a = ep(t, C["27"], 0.4)
        pl.fundo(c, a, diag=1, grade=False)
        aa = ep(t, C["27.a"], 0.4)
        pl.ponto(c, 3, 7, COL_F, aa, "(3, 7)", "esq")
        ab = ep(t, C["27.b"], 0.4)
        if ab > 0:
            x0, y0 = pl.P(3, 7); x1, y1 = pl.P(7, 3)
            line(c, x0, y0, x1, y1, GRAY, ab, 3, dash=[8, 8])
            pl.ponto(c, 7, 3, COL_I, ab, "(7, 3)", "esq")
        ax = ep(t, C["27.xc"], 0.4)
        if ax > 0:
            for (x, y) in ((-3, -7), (-7, -3)):
                px, py = pl.P(x, y)
                check_icon(c, px, py, 16, ax, RED, "x")
            text(c, "origem: NÃO é inversa", 540, 800, 24, "black", RED, ax)


TAB9 = [("x", [1, 2, 3, 4, 5]), ("f(x)", [4, 5, 1, 2, 3]), ("g(x)", [3, 1, 5, 2, 4])]


def b_q9(c, t, C, B):
    head_seq(c, t, C, [("28", "QUESTÃO 9 · VOCÊ FAZ", "DECODIFICAR COM TABELAS", GREEN),
                       ("29", "CONFERINDO", "DE DENTRO PARA FORA", BLUE), ("30", "AS ERRADAS", "CADA UMA, UM ERRO", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    sid = which(t, C, ["28", "29", "30"])
    enun = ("Um sistema de senhas transforma cada dígito de 1 a 5 em duas etapas. Primeiro aplica o embaralhamento g; "
            "depois aplica o código f. Um técnico precisa calcular f⁻¹(g(3)). Esse valor é")
    hl = {}
    if t >= C["29.a"]:
        hl[(2, 2)] = COL_I
    if t >= C["29.b"] + 1.6:
        hl[(1, 1)] = GREEN
    if sid == "28":
        yend = _enunciado(c, [(enun, INK)], a0, 240, 26, 720)
        tabela(c, 190, yend + 10, TAB9, a0, cw=100, rh=74, lw=130, cor_rot={1: COL_F, 2: COL_I})
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        pause_timer(c, t, C["28.end"] - 1.9, 830, 300)
    else:
        tabela(c, 190, 260, TAB9, 1, cw=100, rh=80, lw=130, cor_rot={1: COL_F, 2: COL_I}, hl=hl)
        if sid == "29":
            aa = ep(t, C["29.a"], 0.4)
            if aa > 0:
                K.expr(c, "g(3) = 5", 540, 580, 46, aa, cores={0: COL_I, 2: COL_I})
            ab = ep(t, C["29.b"], 0.4)
            if ab > 0:
                K.expr(c, "f⁻¹(5) = ?", 540, 670, 46, ab, cores={0: COL_F})
                pill(c, "procure o 5 na linha do f", 540, 740, AMBER, size=24, a=ab, anchor="center")
            aok = ep(t, C["29.ok"], 0.4)
            if aok > 0:
                selo(c, 540, 800, aok, "f⁻¹(g(3)) = 2", GREEN, -3, 30)
        else:
            for k, (cue, s_) in enumerate((("xa", "A: f(3) = 1, ignorou o g"), ("xc", "C: f(5) = 3, usou f no lugar de f⁻¹"),
                                           ("xd", "D: g(5) = 4, aplicou g duas vezes"),
                                           ("xe", "E: parou em g(3) = 5"))):
                a = ep(t, C["30." + cue], 0.4)
                if a > 0:
                    check_icon(c, 215, 560 + k * 66, 16, a, RED, "x")
                    ftext(c, s_, 245, 570 + k * 66, 26, "black", INK, a, align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ACDE"}
    ALTS9 = [("A", "1", "f(3)", RED), ("B", "2", "", GREEN), ("C", "3", "f(5)", RED), ("D", "4", "g(5)", RED),
             ("E", "5", "só g(3)", RED)]
    K.alternativas(c, t, C, ALTS9, 1060, 250, 620, 46, C["29.ok"], "B", cues_in, cues_x, gap=30)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    for k, (cue, s_, col) in enumerate((("32.a", "COMPOSTA + INVERSA", BLUE), ("32.b", "PEGADINHAS", AMBER),
                                        ("32.c", "TREINO PARA O ENEM", GREEN))):
        a, d = rise(t, C[cue])
        if a > 0:
            x = 420 + k * 540
            rrect(c, x - 230, 330 + d, 460, 260, 26, mix("#FFFFFF", col, 0.12), a, shadow=True)
            badge_num(c, k + 1, x, 400 + d, a, 30, bg=col)
            text_mid(c, s_, x, 510 + d, 34, "black", col, a)
    pill(c, "ep. 5 · revisão", W / 2, 720, PURPLE, size=32, a=ep(t, C["32.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Qual teste você vai usar primeiro?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, injetora=b_injetora,
              sobrejetora=b_sobrejetora, bijetora=b_bijetora, restringir=b_restringir, espelho=b_espelho,
              atalho=b_atalho, par=b_par, exercicio=b_exercicio, tabela=b_tabela, recap=b_recap, erros=b_erros,
              q7=b_q7, q5=b_q5, q9=b_q9, ponte=b_ponte, cta=b_cta)
