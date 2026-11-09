"""Kit visual de Física do Estudativo: peças animáveis no padrão de editorial.py. Leia só esta docstring para usar.

Uso no visual.py:  import editorial as E;  import fisica as F;  E.usar("Física", "<Trilha>")  (antes de desenhar).
O símbolo da Física (núcleo com duas órbitas) é E.orbita(c, cx, cy, r) / E.simbolo(c, cx, cy, r); capas: E.capa_modelo(c, "Física", ...).
Todas as peças com (c, t, t0, ...) entram sozinhas a partir de t0 (crescem, ganham foco); as sem t são desenhos parados com a = alfa.
Coordenadas em pixels (tela 1920x1080, y para baixo). Ângulo de força/vetor em graus, no sentido da Física: 0 = direita, 90 = para cima.
Texto em fórmula aceita a escrita de E.formula ("m/s^2", "f{d}{t}", "r{2}"). escuro=True = no palco (E.palco).

CORES FIXAS (a linguagem visual completa está no visual.py da FIS-CIN-001):
  E.COR (laranja) = a grandeza da vez, força, carga +, polo norte, quente, raio de luz, onda.   F.VEL (petróleo) = velocidade e
  deslocamento.   F.ACEL (violeta) = aceleração.   F.NEG (azul) = carga −, polo sul, frio.   F.UNID (cinza-tinta) = unidade.

NÚMERO, UNIDADE E FÓRMULA
  medida(c, valor, unidade, x, y, size, cor=None, a=1, align="left") → largura. "20" pesado + "m/s" menor e cinza. medida_em(c, t, t0, ...)
  letra_vetor(c, s, cx, y, size, cor, a) → letra com a setinha em cima (v⃗). y = linha de base.
  formula_legenda(c, t, t0, "v = f{d}{t}", [("v", "velocidade", "m/s"), ...], x, y, size=110, tl=None) — fórmula grande e,
      embaixo, cada letra com o nome e a unidade do SI. É o jeito padrão de apresentar uma fórmula nova.
  unidades(c, t, t0, [("d", "m"), ("=", None), ("v", "m/s"), ("·", None), ("t", "s")], cx, y, size, tu=None) — conferir a
      fórmula pela unidade: cada letra ganha a unidade embaixo, entre colchetes, no instante tu.
  termo(c, t, t0, cx, cy, size, ("72", "km"), ("1", "h"), cortes=[("b", "u", t1)]) e fila(c, t, [dict(t0, cima, baixo, cortes)], cx, cy, size)
      — conversão por fatores que valem 1, com a unidade riscada quando corta (o mesmo de MAT-RAZ-025). fila devolve (centros, borda dir.).
VETORES E FORÇAS
  seta(c, x0, y0, x1, y1, cor, a=1, largura=9, cabeca=None, p=1) — seta grossa parada (p = quanto já cresceu).
  vetor(c, t, t0, A, B, rotulo="v", modulo="20 m/s", cor=None, lado=1) — seta que cresce de A a B, com a letra-vetor e o módulo do lado.
  componentes(c, t, t0, O, B, rot_x="vx", rot_y="vy", cor=None) — tracejado até os eixos e as duas componentes.
  forca(c, t, t0, P, ang, comp, rotulo, cor=None, modulo=None) — vetor que sai de P no ângulo ang (graus, 90 = para cima).
  bloco(c, cx, cy, w, h, rotulo=None, cor=None, a=1, giro=0) — corpo com volume; rotulo dentro ("2 kg").
  corpo_livre(c, t, t0, cx, cy, [dict(ang=90, comp=170, rot="N", t=..., cor=..., de="borda"|"centro", modulo=...)], w, h, rotulo, chao=True)
      — diagrama de corpo livre: bloco, chão e cada força no seu instante.
  chao(c, x0, x1, y, a=1), teto(c, x0, x1, y, a=1), parede(c, x, y0, y1, lado=-1, a=1) — superfícies hachuradas.
  plano_inclinado(c, t, t0, x, y, base, ang, rotulo="θ") → R: rampa com vértice agudo em (x, y). R.ponto(u) = ponto da
      rampa (u de 0 a 1 subindo); R.ang; R.sobe = ângulo do vetor "rampa acima"; R.normal = ângulo da normal.
      bloco_rampa(c, R, u, w, h, rotulo=None, a=1) → centro do bloco apoiado na rampa (use com forca()).
  mola(c, x0, y0, x1, y1, voltas=8, larg_=36, cor=None, a=1) — mola em zigue-zague entre dois pontos (estique mudando x1).
  pendulo(c, t, t0, px, py, L, ang, r=36, amp=None, rotulo_L=None) — teto, fio e esfera; ang em graus da vertical
      (pode variar com t: use oscila(t, t0, amp, periodo)); amp desenha o arco da trajetória e as posições extremas.
CINEMÁTICA
  pista(c, t, t0, x0, x1, y, vmin, vmax, marcas, unidade="m") → vx(valor) em pixels: chão com marcas de posição.
  carrinho(c, x, y, w=220, cor=None, a=1, giro=0, sentido=1) — carro com a base das rodas em y, centro em x.
  movel(c, t, t0, vx, y, pos, t_fim=None, w=220, rastro=()) — carrinho andando: pos(s) = posição s segundos depois de t0;
      rastro = [(instante, valor, "0 s")] deixa uma marca fantasma com o tempo em cada posição (foto estroboscópica).
  cronometro(c, cx, cy, r, segundos, a=1, texto=None) — mostrador com ponteiro e o tempo escrito embaixo.
  grafico(c, t, t0, x, y, w, h, xmin, xmax, ymin, ymax, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=None, ...) → P
      (E.plano com nome e unidade nos eixos). Desenhe a linha com E.curva(c, t, t0, P, f, ...) e os pontos com E.ponto.
  area_graf(c, t, t0, P, f, a, b, rotulo=None, cor=None) — área sob a linha (no v × t, é o deslocamento) com o valor dentro.
ONDAS, ÓPTICA, CALOR
  onda(c, t, t0, x0, x1, y, A, lam, cor=None, d=1, velocidade=0, tl=None, ta=None, rot_lambda="λ", rot_A="A")
      — senoide desenhada da esquerda para a direita (velocidade em px/s faz a onda correr); tl/ta = instante da cota do
      comprimento de onda e da seta da amplitude. Devolve os x das cristas.
  raio(c, t, t0, [P0, P1, P2...], cor=None, d=0.8, setas=True, tracejado=False) — raio de luz que avança, com setas no meio.
  normal(c, t, t0, P, ang, comp=170) — reta normal tracejada passando por P (ang em graus, 90 = vertical).
  espelho_plano(c, t, t0, A, B, lado=1) — espelho com hachura atrás (lado escolhe de que lado fica a hachura).
  espelho_esferico(c, t, t0, vx, cy, R, abertura=70, concavo=True, eixo=None) → dict(F=x, C=x): vértice em (vx, cy),
      luz vindo da esquerda; desenha eixo, F e C.
  lente(c, t, t0, cx, cy, h, convergente=True, f=None, eixo=None) — lente com os focos F e F' a uma distância f.
  objeto(c, t, t0, x, ybase, h, cor=None, rotulo=None, tracejado=False) — seta de objeto/imagem (h < 0 = invertida).
  termometro(c, t, t0, cx, yb, h, nivel, vmin=0, vmax=100, marcas=(), unidade="°C", cor=None) — o líquido sobe até nivel.
ELETRICIDADE E MAGNETISMO
  fio(c, t, t0, [pontos], d=0.8) — fio que se desenha; no(c, P, a=1) — ponto de ligação.
  pilha(c, t, t0, A, B, rotulo=None), resistor(c, t, t0, A, B, rotulo=None), lampada(c, t, t0, A, B, acesa=None, rotulo=None),
  chave(c, t, t0, A, B, fechada=True) — componentes entre os pontos A e B; ligue os fios até A e B. Série = um atrás do outro
      no mesmo fio; paralelo = dois ramos entre os mesmos nós. acesa = instante em que a lâmpada acende.
  corrente(c, t, t0, [pontos], cor=None, vel=120, fecha=True) — setinhas andando no sentido da corrente.
  ima(c, t, t0, cx, cy, w=360, h=110, giro=0) — barra com N (laranja, à direita com giro 0) e S (azul).
  linhas_campo(c, t, t0, cx, cy, w=360, n=3, cor=None, h=110) — linhas do ímã de (cx, cy): saem do N, contornam e entram no S,
      com setas. Desenhe ANTES de ima() com o mesmo cx, cy, w, h, para o ímã ficar por cima.
  carga(c, t, t0, cx, cy, r=56, sinal="+", rotulo=None) — esfera laranja (+) ou azul (−) com o sinal.
  campo_carga(c, t, t0, cx, cy, r0, r1, n=8, sai=True) — setas radiais do campo (saem da + e entram na −).
Apoio: oscila(t, t0, amp, periodo), seta(...), poli(c, pts, p, cor, a, largura, dash) = polilinha parcial (p de 0 a 1).
"""
import math

import skia

import editorial as E
import motor as M
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, PAPEL, ep, prog, lerp, ease_io, ease_out, ease_back, clamp, mix, hexc
from editorial import foco, centro, escreve, larg

VEL = "#0E9AA7"   # velocidade e deslocamento
ACEL = "#7A3FD0"  # aceleração
NEG = "#1F6FEB"   # carga negativa, polo sul, frio
UNID = TINTA2     # unidade
BR = "#FFFFFF"


def _tinta(escuro):
    return BR if escuro else TINTA


def _unid(escuro):
    return E.CLARO if escuro else UNID


def _dir(ang):
    """ângulo da Física (graus, 90 = para cima) → vetor de tela"""
    r = math.radians(ang)
    return math.cos(r), -math.sin(r)


def oscila(t, t0, amp, periodo):
    """valor que vai e volta: amp no início, −amp na metade do período"""
    return amp * math.cos(2 * math.pi * max(0.0, t - t0) / periodo)


def poli(c, pts, p, cor, a=1.0, largura=6, dash=None):
    """polilinha desenhada até a fração p do comprimento; devolve a ponta atual"""
    if p <= 0 or a <= 0 or len(pts) < 2:
        return pts[0]
    comp = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    alvo = sum(comp) * clamp(p)
    path = skia.Path()
    path.moveTo(*pts[0])
    ponta = pts[0]
    for (x0, y0), (x1, y1), L in zip(pts, pts[1:], comp):
        if alvo <= 0:
            break
        f = 1.0 if L <= alvo else alvo / L
        ponta = (lerp(x0, x1, f), lerp(y0, y1, f))
        path.lineTo(*ponta)
        alvo -= L
    pt = M.paint(cor, a, stroke=largura, cap_round=True)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    if dash:
        pt.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawPath(path, pt)
    return ponta


def _cabeca(c, x, y, ux, uy, k, cor, a):
    nx, ny = -uy, ux
    bx, by = x - ux * k, y - uy * k
    p = skia.Path()
    p.moveTo(x, y); p.lineTo(bx + nx * k * 0.55, by + ny * k * 0.55); p.lineTo(bx - nx * k * 0.55, by - ny * k * 0.55); p.close()
    c.drawPath(p, M.paint(cor, a))


def seta(c, x0, y0, x1, y1, cor, a=1.0, largura=9, cabeca=None, p=1.0):
    """seta grossa de (x0, y0) até (x1, y1); p = quanto já cresceu"""
    if a <= 0 or p <= 0:
        return
    xe, ye = lerp(x0, x1, p), lerp(y0, y1, p)
    L = math.hypot(xe - x0, ye - y0)
    if L < 1:
        return
    ux, uy = (xe - x0) / L, (ye - y0) / L
    k = min(cabeca or max(22, largura * 2.8), L * 0.7)
    M.line(c, x0, y0, xe - ux * k * 0.8, ye - uy * k * 0.8, cor, a, largura, cap_round=False)
    _cabeca(c, xe, ye, ux, uy, k, cor, a)


# ---------------- número, unidade e fórmula ----------------
def medida(c, valor, unidade, x, y, size, cor=None, a=1.0, align="left", escuro=False, cor_u=None):
    """número pesado + unidade menor e cinza ("20" "m/s"); y = linha de base. Devolve a largura"""
    v = E._num(valor)
    wn = larg(v, "g", size)
    gap = size * 0.18 if unidade else 0
    wu = E.formula(None, unidade, 0, 0, size * 0.72, "b", a=0) if unidade else 0
    w = wn + gap + wu
    if a > 0 and c is not None:
        x0 = x - w / 2 if align == "center" else x - w if align == "right" else x
        escreve(c, v, x0, y, size, "g", cor or _tinta(escuro), a)
        if unidade:
            E.formula(c, unidade, x0 + wn + gap, y, size * 0.72, "b", cor_u or _unid(escuro), a)
    return w


def medida_em(c, t, t0, valor, unidade, x, y, size, cor=None, align="left", escuro=False, cor_u=None):
    foco(c, t, t0, 0.5, lambda a: medida(c, valor, unidade, x, y, size, cor, a, align, escuro, cor_u))


def letra_vetor(c, s, cx, y, size, cor=None, a=1.0, estilo="g"):
    """letra centrada em cx com a setinha de vetor em cima; y = linha de base. Devolve a largura"""
    w = E.formula(None, s, 0, 0, size, estilo, a=0)
    if a > 0 and c is not None:
        cor = cor or TINTA
        E.formula(c, s, cx - w / 2, y, size, estilo, cor, a)
        alta = any(ch.isupper() or ch.isdigit() or ch in "bdfhklt" for ch in s)  # letra com haste: a seta sobe
        ys = y - size * (0.98 if alta else 0.8)
        hw = max(w / 2 + size * 0.02, size * 0.26)
        M.line(c, cx - hw, ys, cx + hw - size * 0.05, ys, cor, a, max(3, size * 0.07))
        _cabeca(c, cx + hw + size * 0.06, ys, 1, 0, size * 0.2, cor, a)
    return w


def formula_legenda(c, t, t0, formula, legendas, x, y, size=110, tl=None, size_l=52, dy=None, escuro=False, cor=None):
    """fórmula grande em (x, y) e, embaixo, uma linha por letra: letra · nome · (unidade do SI). tl = instante de cada linha"""
    tinta = _tinta(escuro)
    cor = cor or (E.CLARO if escuro else E.COR_TEXTO)
    E.formula_em(c, t, t0, formula, x, y, size, "g", tinta)
    dy = dy or size_l * 1.45
    for i, (letra, nome, unidade) in enumerate(legendas):
        ti = tl[i] if tl else t0 + 0.6 + 0.35 * i
        yy = y + size * 0.55 + size_l * 1.2 + i * dy

        def lin(a, letra=letra, nome=nome, unidade=unidade, yy=yy):
            wl = E.formula(c, letra, x, yy, size_l * 1.1, "g", cor, a)
            xx = x + max(wl, size_l * 0.9) + size_l * 0.5
            escreve(c, nome, xx, yy, size_l, "i", tinta, a)
            if unidade:
                xx += larg(nome, "i", size_l) + size_l * 0.4
                E.formula(c, f"({unidade})", xx, yy, size_l * 0.9, "b", _unid(escuro), a)
        foco(c, t, ti, 0.5, lin)


def unidades(c, t, t0, termos, cx, y, size, tu=None, escuro=False, cor=None, size_u=None):
    """fórmula com a unidade de cada letra embaixo: termos = [("d", "m"), ("=", None), ...]. tu = instante (ou lista, um por termo)
    das unidades. Devolve os centros de cada termo"""
    tinta = _tinta(escuro)
    su = size_u or size * 0.5
    gap = size * 0.25
    ws = [max(E.formula(None, s, 0, 0, size, "g", a=0), E.formula(None, f"[{u}]", 0, 0, su, "b", a=0) if u else 0) for s, u in termos]
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    cs = []
    for i, ((s, u), w) in enumerate(zip(termos, ws)):
        xm = x + w / 2
        cs.append(xm)
        cr = (cor or E.COR_TEXTO) if u else tinta
        E.formula_em(c, t, t0 + 0.12 * i, s, xm, y, size, "g", cr, "center")
        if u:
            ti = (tu[i] if isinstance(tu, (list, tuple)) else tu) if tu is not None else t0 + 0.6
            E.formula_em(c, t, ti, f"[{u}]", xm, y + size * 0.95, su, "b", _unid(escuro), "center")
        x += w + gap
    return cs


def _partes(p, size):
    n, u = p
    wn = larg(n, "g", size) if n else 0
    wu = E.formula(None, u, 0, 0, size * 0.8, "b", a=0) if u else 0
    return wn, (size * 0.2 if n and u else 0), wu


def larg_termo(cima, baixo, size):
    w = sum(_partes(cima, size))
    if baixo:
        w = max(w, sum(_partes(baixo, size)))
    return w + size * 0.3


def termo(c, t, t0, cx, cy, size, cima, baixo=None, cor=None, cortes=(), escuro=False, cor_corte=None):
    """número com unidade, em linha (baixo=None) ou como fração. cima/baixo = (número, unidade).
    cortes = [(onde "c"|"b", qual "n"|"u", instante)]: risca a parte que corta. Devolve as caixas de cada parte"""
    cor = cor or _tinta(escuro)
    cu = _unid(escuro)
    linhas = {"c": (cima, cy - size * 0.2 if baixo else cy + size * 0.35)}
    if baixo:
        linhas["b"] = (baixo, cy + size * 0.9)
    caixas = {}
    for k, (p, y) in linhas.items():
        wn, gap, wu = _partes(p, size)
        x = cx - (wn + gap + wu) / 2
        caixas[(k, "n")] = (x, y, wn)
        caixas[(k, "u")] = (x + wn + gap, y, wu)

    def desenha(a):
        for k, (p, y) in linhas.items():
            x, _, _ = caixas[(k, "n")]
            if p[0]:
                escreve(c, p[0], x, y, size, "g", cor, a)
            if p[1]:
                E.formula(c, p[1], caixas[(k, "u")][0], y, size * 0.8, "b", cu, a)
        if baixo:
            lw = larg_termo(cima, baixo, size) - size * 0.15
            b = size * 0.075
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + size * 0.03, lw, b), b / 2, b / 2), M.paint(cor, a))
    foco(c, t, t0, 0.5, desenha)
    for onde, qual, tc in cortes:
        p = ep(t, tc, 0.35)
        if p > 0 and (onde, qual) in caixas:
            x, y, w = caixas[(onde, qual)]
            M.line(c, x - 6, y + size * 0.08, x + w + 6, y - size * 0.72, cor_corte or (E.CLARO if escuro else E.COR), 1.0, max(5, size * 0.08), progress=p)
    return caixas


def fila(c, t, itens, cx, cy, size, escuro=False, gap=None):
    """itens = [dict(t0, cima, baixo=None, cortes=(), cor=None)]: termos com "×" entre eles, centrados pelo tamanho final.
    Devolve (centros, borda direita)"""
    gap = gap or size * 0.75
    ws = [larg_termo(i["cima"], i.get("baixo"), size) for i in itens]
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    xs = []
    for k, (it, w) in enumerate(zip(itens, ws)):
        xm = x + w / 2
        xs.append(xm)
        if k:
            foco(c, t, it["t0"], 0.5, lambda a, x=x: centro(c, "×", x - gap / 2, cy + size * 0.3, size * 0.8, "g", BR if escuro else TINTA2, a))
        termo(c, t, it["t0"], xm, cy, size, it["cima"], it.get("baixo"), it.get("cor"), it.get("cortes", ()), escuro)
        x += w + gap
    return xs, x - gap


# ---------------- vetores e forças ----------------
def _rotulo_vetor(c, rotulo, modulo, mx, my, nx, ny, gap, size, cor, a, escuro):
    """letra-vetor (e " = módulo") encostada no ponto (mx, my) pelo lado (nx, ny)"""
    if a <= 0 or not (rotulo or modulo):
        return
    wl = letra_vetor(None, rotulo, 0, 0, size) if rotulo else 0
    ig = larg(" = ", "g", size * 0.8) if rotulo and modulo else 0
    wm = 0
    if modulo:
        v, _, u = modulo.partition(" ")
        wm = medida(None, v, u, 0, 0, size * 0.8)
    w, hh = wl + ig + wm, size * 0.62
    k = gap + min(abs(nx) * w / 2 + abs(ny) * hh, math.hypot(w / 2, hh))
    cx, cy = mx + nx * k, my + ny * k
    x0, yb = cx - w / 2, cy + size * 0.36
    if rotulo:
        letra_vetor(c, rotulo, x0 + wl / 2, yb, size, cor, a)
    if modulo:
        if rotulo:
            escreve(c, " = ", x0 + wl, yb, size * 0.8, "g", _tinta(escuro), a)
        v, _, u = modulo.partition(" ")
        medida(c, v, u, x0 + wl + ig, yb, size * 0.8, _tinta(escuro), a, escuro=escuro)


def vetor(c, t, t0, A, B, rotulo=None, modulo=None, cor=None, largura=9, d=0.6, lado=1, size=56, escuro=False, gap=18, em=0.5):
    """seta que cresce de A até B, com a letra-vetor e o módulo ao lado (lado = 1 ou −1); em = onde fica o rótulo (0 a 1)"""
    if t < t0:
        return
    cor = cor or E.COR
    seta(c, *A, *B, cor, 1.0, largura, p=ease_out(prog(t, t0, d)))
    ux, uy = E._uni(*A, *B)
    nx, ny = uy * lado, -ux * lado
    mx, my = lerp(A[0], B[0], em), lerp(A[1], B[1], em)
    cr = (E.CLARO if escuro else E.COR_TEXTO) if cor == E.COR else cor
    foco(c, t, t0 + d * 0.7, 0.4, lambda a: _rotulo_vetor(c, rotulo, modulo, mx, my, nx, ny, gap, size, cr, a, escuro))


def componentes(c, t, t0, O, B, rot_x=None, rot_y=None, cor=None, d=0.6, size=48, escuro=False):
    """projeções tracejadas de B nos eixos que passam por O e as duas componentes, mais claras"""
    if t < t0:
        return
    cor = mix(cor or E.COR, BR if not escuro else "#000000", 0.25)
    tinta = _tinta(escuro)
    q = ep(t, t0, d)
    M.line(c, *B, B[0], O[1], tinta, 0.6, 4, dash=E.TRACO, progress=q)
    M.line(c, *B, O[0], B[1], tinta, 0.6, 4, dash=E.TRACO, progress=q)
    vetor(c, t, t0 + d * 0.6, O, (B[0], O[1]), rot_x, None, cor, 8, d, lado=-1 if B[1] < O[1] else 1, size=size, escuro=escuro)
    vetor(c, t, t0 + d * 0.9, O, (O[0], B[1]), rot_y, None, cor, 8, d, lado=1 if B[0] > O[0] else -1, size=size, escuro=escuro)


def forca(c, t, t0, P, ang, comp, rotulo=None, cor=None, modulo=None, largura=9, d=0.5, size=56, escuro=False, lado=None):
    """força saindo de P no ângulo ang (graus, 90 = para cima) com comprimento comp em pixels"""
    dx, dy = _dir(ang)
    B = (P[0] + dx * comp, P[1] + dy * comp)
    if lado is None:
        lado = 1 if -45 < (ang % 360) <= 135 else -1  # rótulo do lado de fora, sem tapar o bloco
    vetor(c, t, t0, P, B, rotulo, modulo, cor, largura, d, lado=lado, size=size, escuro=escuro, em=0.62)
    return B


def bloco(c, cx, cy, w, h, rotulo=None, cor=None, a=1.0, giro=0.0, size=None):
    """corpo com volume centrado em (cx, cy), girado giro graus; rotulo escrito dentro"""
    if a <= 0:
        return
    cor = cor or E.COR
    c.save(); c.translate(cx, cy); c.rotate(-giro)
    s = skia.Paint(AntiAlias=True, Color=hexc("#000000", 0.18 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + 5, -h / 2 + 9, w, h), 12, 12), s)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(-w / 2, -h / 2), skia.Point(w / 2, h / 2)],
                                               [hexc(mix(cor, BR, 0.2), a), hexc(mix(cor, "#000000", 0.22), a)]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 12, 12), p)
    if rotulo:
        sz = size or min(h * 0.42, w * 0.3)
        E._meio(c, rotulo, 0, 0, sz, "g", M.on(cor), a)
    c.restore()


def _hachura(c, x0, y0, x1, y1, nx, ny, a, cor, passo=26, k=22):
    """linha da superfície com tracinhos inclinados do lado (nx, ny)"""
    M.line(c, x0, y0, x1, y1, cor, a, 6)
    L = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    n = int(L // passo)
    for i in range(n + 1):
        px, py = x0 + ux * (i * passo + 8), y0 + uy * (i * passo + 8)
        if i * passo + 8 > L:
            break
        M.line(c, px, py, px + nx * k - ux * k * 0.7, py + ny * k - uy * k * 0.7, cor, a * 0.55, 3)


def chao(c, x0, x1, y, a=1.0, escuro=False):
    _hachura(c, x0, y, x1, y, 0, 1, a, _tinta(escuro))


def teto(c, x0, x1, y, a=1.0, escuro=False):
    _hachura(c, x0, y, x1, y, 0, -1, a, _tinta(escuro))


def parede(c, x, y0, y1, lado=-1, a=1.0, escuro=False):
    _hachura(c, x, y0, x, y1, lado, 0, a, _tinta(escuro))


def _borda(cx, cy, w, h, ang):
    """ponto da borda do retângulo (centro cx, cy) na direção ang"""
    dx, dy = _dir(ang)
    k = min(w / 2 / abs(dx) if abs(dx) > 1e-9 else 1e9, h / 2 / abs(dy) if abs(dy) > 1e-9 else 1e9)
    return cx + dx * k, cy + dy * k


def corpo_livre(c, t, t0, cx, cy, forcas, w=200, h=150, rotulo=None, chao_=True, cor_bloco=None, escuro=False, size=56):
    """diagrama de corpo livre: forcas = [dict(ang, comp, rot, t=None, cor=None, de="borda"|"centro", modulo=None)]"""
    k = ease_back(prog(t, t0, 0.5))
    if chao_ and t >= t0:
        chao(c, cx - w * 1.3, cx + w * 1.3, cy + h / 2, ep(t, t0, 0.4), escuro)
    # forças que saem do centro vão por baixo do bloco: a seta aparece a partir da borda e não risca o rótulo
    def _desenha(do_centro):
        for i, f in enumerate(forcas):
            if (f.get("de") == "centro") != do_centro:
                continue
            ti = f.get("t", t0 + 0.5 + 0.4 * i)
            P = (cx, cy) if do_centro else _borda(cx, cy, w, h, f["ang"])
            forca(c, t, ti, P, f["ang"], f["comp"], f.get("rot"), f.get("cor"), f.get("modulo"), size=size, escuro=escuro)
    _desenha(True)
    if k > 0:
        bloco(c, cx, cy, w * k, h * k, rotulo, cor_bloco or (TINTA2 if not escuro else "#5A5A66"), clamp(k))
    _desenha(False)


class Rampa:
    """o que plano_inclinado devolve"""

    def __init__(s, x, y, base, ang):
        s.x, s.y, s.base, s.ang = x, y, base, ang
        s.alto = base * math.tan(math.radians(ang))
        s.topo = (x + base, y - s.alto)
        s.sobe, s.desce, s.normal = ang, ang + 180, ang + 90

    def ponto(s, u):
        return lerp(s.x, s.topo[0], u), lerp(s.y, s.topo[1], u)


def plano_inclinado(c, t, t0, x, y, base, ang, rotulo="θ", cor=None, d=0.7, escuro=False, size=52):
    """rampa com o ângulo agudo em (x, y), subindo para a direita; devolve Rampa (ponto(u), sobe, desce, normal)"""
    R = Rampa(x, y, base, ang)
    if t < t0:
        return R
    tinta = _tinta(escuro)
    q = ease_io(prog(t, t0, d))
    pts = [(x, y), (x + base, y), R.topo]
    path = skia.Path(); path.addPoly(pts, True)
    c.drawPath(path, M.paint(cor or tinta, 0.07 * q))
    E._contorno(c, pts, q, tinta, 6)
    chao(c, x - 80, x + base + 80, y, q * 0.8, escuro)
    if rotulo:
        E.angulo(c, t, t0 + d * 0.8, (x, y), (x + 200, y), R.topo, rotulo, r=110, cor=cor or E.COR, size=size)
    return R


def bloco_rampa(c, R, u, w, h, rotulo=None, a=1.0, cor=None):
    """bloco apoiado na rampa na posição u (0 a 1); devolve o centro (para as forças)"""
    px, py = R.ponto(u)
    nx, ny = _dir(R.normal)
    cx, cy = px + nx * h / 2, py + ny * h / 2
    bloco(c, cx, cy, w, h, rotulo, cor, a, giro=R.ang)
    return cx, cy


def mola(c, x0, y0, x1, y1, voltas=8, larg_=36, cor=None, a=1.0, largura=5, pontas=26):
    """mola em zigue-zague de (x0, y0) até (x1, y1), com pontas retas"""
    if a <= 0:
        return
    L = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = -uy, ux
    pts = [(x0, y0), (x0 + ux * pontas, y0 + uy * pontas)]
    miolo = L - 2 * pontas
    n = voltas * 2
    for i in range(1, n):
        s = pontas + miolo * i / n
        k = larg_ / 2 * (1 if i % 2 else -1)
        pts.append((x0 + ux * s + nx * k, y0 + uy * s + ny * k))
    pts += [(x1 - ux * pontas, y1 - uy * pontas), (x1, y1)]
    poli(c, pts, 1.0, cor or TINTA2, a, largura)


def pendulo(c, t, t0, px, py, L, ang, r=36, cor=None, amp=None, rotulo_L=None, escuro=False, d=0.6):
    """teto em (px, py), fio de comprimento L e esfera; ang = graus a partir da vertical (positivo para a direita)"""
    if t < t0:
        return
    tinta = _tinta(escuro)
    q = ep(t, t0, 0.4)
    teto(c, px - 110, px + 110, py, q, escuro)
    if amp:
        qa = ep(t, t0 + d, 0.6)
        for s_ in (-1, 1):
            a_ = math.radians(amp * s_)
            ex, ey = px + L * math.sin(a_), py + L * math.cos(a_)
            M.line(c, px, py, ex, ey, tinta, 0.25 * qa, 3, dash=E.TRACO)
            c.drawCircle(ex, ey, r, M.paint(cor or E.COR, 0.15 * qa))
        ret = skia.Rect.MakeXYWH(px - L, py - L, 2 * L, 2 * L)
        pt = M.paint(tinta, 0.4 * qa, stroke=3)
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawArc(ret, 90 - amp, 2 * amp, False, pt)
    a_ = math.radians(ang)
    bx, by = px + L * math.sin(a_), py + L * math.cos(a_)
    p = ease_io(prog(t, t0, d))
    M.line(c, px, py, lerp(px, bx, p), lerp(py, by, p), tinta, 1.0, 4)
    c.drawCircle(px, py, 9, M.paint(tinta))
    k = ease_back(prog(t, t0 + d * 0.8, 0.45))
    if k > 0:
        E.bola(c, bx, by, r * k, cor)
    if rotulo_L:
        foco(c, t, t0 + d, 0.4, lambda a: E._cola(c, rotulo_L, (px + bx) / 2, (py + by) / 2, -math.cos(a_), math.sin(a_), 16, 48, "b", tinta, a))


# ---------------- cinemática ----------------
def pista(c, t, t0, x0, x1, y, vmin, vmax, marcas, unidade="m", fmt=None, size=40, escuro=False, d=0.6):
    """chão do movimento com marcas de posição embaixo; devolve vx(valor) → pixel"""
    tinta = _tinta(escuro)
    fmt = fmt or E._num
    vx = lambda v: x0 + (float(v) - vmin) / (vmax - vmin) * (x1 - x0)
    if t >= t0:
        M.line(c, x0 - 40, y, lerp(x0 - 40, x1 + 40, ease_io(prog(t, t0, d))), y, tinta, 1.0, 6)
    for i, v in enumerate(marcas):
        foco(c, t, t0 + 0.2 + i * 0.06, 0.4, lambda a, v=v: (
            M.line(c, vx(v), y, vx(v), y + 18, tinta, a, 4),
            medida(c, fmt(v), unidade, vx(v), y + 22 + size, size, tinta, a, "center", escuro)), sobe=6)
    return vx


def carrinho(c, x, y, w=220, cor=None, a=1.0, giro=0.0, sentido=1):
    """carro de lado: centro em x, rodas tocando y. giro = ângulo das rodas (graus)"""
    if a <= 0:
        return
    cor = cor or E.COR
    r = w * 0.12
    base = y - r * 0.9
    s = skia.Paint(AntiAlias=True, Color=hexc("#000000", 0.16 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
    c.drawOval(skia.Rect.MakeXYWH(x - w * 0.5, y - 8, w, 16), s)
    # cabine: trapézio com o para-brisa inclinado para a frente
    sg = 1 if sentido > 0 else -1
    yt, yb_ = base - w * 0.46, base - w * 0.26
    tras, frente = x - sg * w * 0.36, x + sg * w * 0.16
    cab = skia.Path()
    cab.moveTo(tras, yb_ + 4); cab.lineTo(tras + sg * w * 0.04, yt); cab.lineTo(frente - sg * w * 0.08, yt); cab.lineTo(frente + sg * w * 0.06, yb_ + 4); cab.close()
    c.drawPath(cab, M.paint(mix(cor, "#000000", 0.12), a))
    jan = skia.Path()
    m_ = w * 0.035
    jan.moveTo(tras + sg * m_, yb_); jan.lineTo(tras + sg * (w * 0.04 + m_ * 0.6), yt + m_); jan.lineTo(frente - sg * (w * 0.08 + m_ * 0.4), yt + m_)
    jan.lineTo(frente + sg * (w * 0.06 - m_ * 1.2), yb_); jan.close()
    c.drawPath(jan, M.paint(mix(cor, BR, 0.78), a))
    xm_ = (tras + frente) / 2 + sg * w * 0.02
    M.line(c, xm_, yt + m_, xm_, yb_, mix(cor, "#000000", 0.12), a, max(3, w * 0.025), cap_round=False)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(x, base - w * 0.28), skia.Point(x, base)],
                                               [hexc(mix(cor, BR, 0.18), a), hexc(mix(cor, "#000000", 0.2), a)]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2, base - w * 0.28, w, w * 0.28), w * 0.07, w * 0.07), p)
    fx = x + w / 2 - 14 if sentido > 0 else x - w / 2 + 4
    M.rrect(c, fx, base - w * 0.22, 10, w * 0.07, 4, "#FFE08A", a)
    for wx in (x - w * 0.3, x + w * 0.3):
        c.drawCircle(wx, y - r, r, M.paint("#1B1B20", a))
        c.drawCircle(wx, y - r, r * 0.5, M.paint("#9A9AA2", a))
        for k in range(3):
            g = math.radians(giro + k * 120)
            M.line(c, wx, y - r, wx + math.cos(g) * r * 0.45, y - r + math.sin(g) * r * 0.45, "#1B1B20", a, 3)


def movel(c, t, t0, vx, y, pos, t_fim=None, w=220, rastro=(), cor=None, escuro=False, a=1.0):
    """carrinho que anda: pos(s) = posição (valor da pista) s segundos depois de t0; para em t_fim (segundos depois de t0).
    rastro = [(instante, valor, rótulo)]: marca fantasma da posição naquele instante, com o rótulo do tempo"""
    for ti, v, rot in rastro:
        q = ep(t, ti, 0.4)
        if q > 0:
            X = vx(v)
            carrinho(c, X, y, w, cor, 0.18 * q * a)
            M.line(c, X, y - 4, X, y - w * 0.62, _tinta(escuro), 0.35 * q * a, 3, dash=E.TRACO)
            if rot:
                E.pilula(c, rot, X, y - w * 0.62 - 34, 36, "b", fundo=_tinta(escuro), cor=PAPEL if not escuro else "#07070F", a=q * a)
    s = clamp(t - t0, 0, t_fim if t_fim is not None else 1e9)
    X = vx(pos(s))
    giro = (X - vx(pos(0))) / (w * 0.12) * 180 / math.pi
    carrinho(c, X, y, w, cor, a * ep(t, t0 - 0.4, 0.4), giro)
    return X


def cronometro(c, cx, cy, r, segundos, a=1.0, texto=None, cor=None, escuro=False):
    """mostrador de cronômetro (uma volta = 60 s) com o tempo escrito embaixo"""
    if a <= 0:
        return
    tinta = _tinta(escuro)
    c.drawCircle(cx, cy, r, M.paint(PAPEL if not escuro else "#14141C", a))
    c.drawCircle(cx, cy, r, M.paint(tinta, a, stroke=max(4, r * 0.07)))
    M.rrect(c, cx - r * 0.18, cy - r * 1.28, r * 0.36, r * 0.2, 6, tinta, a)
    for k in range(12):
        g = math.radians(k * 30)
        M.line(c, cx + math.sin(g) * r * 0.78, cy - math.cos(g) * r * 0.78, cx + math.sin(g) * r * 0.9, cy - math.cos(g) * r * 0.9, tinta, a * 0.6, 3)
    g = math.radians(segundos * 6)
    cr = cor or E.COR
    c.drawArc(skia.Rect.MakeXYWH(cx - r * 0.62, cy - r * 0.62, r * 1.24, r * 1.24), -90, segundos * 6 % 360, True, M.paint(cr, 0.18 * a))
    M.line(c, cx, cy, cx + math.sin(g) * r * 0.74, cy - math.cos(g) * r * 0.74, cr, a, max(4, r * 0.06))
    c.drawCircle(cx, cy, r * 0.07, M.paint(cr, a))
    s = texto if texto is not None else E._num(round(segundos, 1)) + " s"
    if s:
        v, _, u = s.partition(" ")
        medida(c, v, u, cx, cy + r + r * 0.55, r * 0.45, tinta, a, "center", escuro)


def grafico(c, t, t0, x, y, w, h, xmin, xmax, ymin, ymax, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=None,
            marcas_x=None, marcas_y=None, size=38, escuro=False, grade=True):
    """E.plano com o nome e a unidade de cada eixo ("t (s)", "v (m/s)"). Devolve P"""
    P = E.plano(c, t, t0, x, y, w, h, xmin, xmax, ymin, ymax, passo, passo_y, marcas_x, marcas_y, grade, ("", ""), size=size, escuro=escuro)
    tinta = _tinta(escuro)
    for s, X, Y, al in ((eixo_x, x + w + 50, P.oy + size * 2 + 44, "right"), (eixo_y, P.ox + 30, y - 22, "left")):
        if s:
            letra, _, u = s.partition(" ")

            def nome(a, letra=letra, u=u, X=X, Y=Y, al=al):
                wl = E.formula(None, letra, 0, 0, 56, "g", a=0)
                wu = E.formula(None, u, 0, 0, 40, "b", a=0) if u else 0
                x0 = X - wl - 10 - wu if al == "right" else X
                E.formula(c, letra, x0, Y, 56, "g", E.CLARO if escuro else E.COR_TEXTO, a)
                if u:
                    E.formula(c, u, x0 + wl + 10, Y, 40, "b", _unid(escuro), a)
            foco(c, t, t0 + 0.5, 0.4, nome)
    return P


def area_graf(c, t, t0, P, f, a, b, rotulo=None, cor=None, alfa=0.26, d=0.8, size=52):
    """área sob a linha de a até b; rotulo (ex.: "100 m") escrito no meio dela"""
    E.area(c, t, t0, P, f, a, b, cor=cor, alfa=alfa, d=d)
    if rotulo:
        xm = (a + b) / 2
        ym = (E._avalia(f, xm) or 0) / 2
        v, _, u = rotulo.partition(" ")
        foco(c, t, t0 + d, 0.4, lambda q: medida(c, v, u, P.x(xm), P.y(ym) + size * 0.36, size, E.COR_TEXTO if not P.escuro else BR, q, "center"))


# ---------------- ondas, óptica e calor ----------------
def onda(c, t, t0, x0, x1, y, A, lam, cor=None, d=1.0, velocidade=0.0, largura=7, tl=None, ta=None, rot_lambda="λ", rot_A="A",
         size=52, escuro=False, eixo=True):
    """senoide de x0 a x1 em torno de y, amplitude A e comprimento de onda lam (pixels); velocidade (px/s) faz correr.
    tl/ta = instantes da cota do comprimento de onda e da seta da amplitude. Devolve os x das cristas"""
    if t < t0:
        return []
    cor = cor or E.COR
    tinta = _tinta(escuro)
    desl = velocidade * max(0.0, t - t0)
    fase = lambda x: 2 * math.pi * (x - x0 - desl) / lam
    p = ease_io(prog(t, t0, d))
    if eixo:
        M.line(c, x0 - 20, y, x1 + 20, y, tinta, 0.35, 3, dash=E.TRACO, progress=p)
    n = max(2, int((x1 - x0) / 4))
    pts = [(x0 + (x1 - x0) * i / n, y - A * math.sin(fase(x0 + (x1 - x0) * i / n))) for i in range(n + 1)]
    poli(c, pts, p, cor, 1.0, largura)
    # cristas: sin = 1 → fase = π/2 + 2kπ
    cristas = []
    k = math.floor(-desl / lam - 0.25)
    while True:
        xc = x0 + desl + lam * (0.25 + k)
        if xc > x1:
            break
        if xc >= x0:
            cristas.append(xc)
        k += 1
    if tl is not None and len(cristas) >= 2:
        xa, xb = cristas[0], cristas[1]
        yy = y - A - 60
        q = ep(t, tl, 0.5)
        if q > 0:
            for xx in (xa, xb):
                M.line(c, xx, y - A - 12, xx, yy - 16, tinta, 0.5 * q, 3, dash=E.TRACO)
            xm = (xa + xb) / 2
            seta(c, xm, yy, lerp(xm, xa, 1), yy, tinta, q, 5, 20, q)
            seta(c, xm, yy, xb, yy, tinta, q, 5, 20, q)
            foco(c, t, tl + 0.2, 0.4, lambda a: E._meio(c, rot_lambda, xm, yy - size * 0.75, size, "g", E.CLARO if escuro else E.COR_TEXTO, a))
    if ta is not None and cristas:
        xc = cristas[-1] if len(cristas) > 2 else cristas[0]
        q = ep(t, ta, 0.5)
        if q > 0:
            seta(c, xc, y, xc, y - A, tinta, q, 5, 20, q)
            foco(c, t, ta + 0.2, 0.4, lambda a: E._cola(c, rot_A, xc, y - A / 2, 1, 0, lam * 0.2 + 12, size, "g", E.CLARO if escuro else E.COR_TEXTO, a))
    return cristas


def raio(c, t, t0, pts, cor=None, d=0.8, largura=6, setas=True, tracejado=False):
    """raio de luz que avança pela polilinha pts, com uma seta no meio de cada trecho já desenhado"""
    if t < t0:
        return
    cor = cor or E.COR
    p = ease_io(prog(t, t0, d))
    poli(c, pts, p, cor, 1.0, largura, E.TRACO if tracejado else None)
    if setas:
        comp = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
        alvo, ac = sum(comp) * p, 0.0
        for (x0, y0), (x1, y1), L in zip(pts, pts[1:], comp):
            if ac + L * 0.55 <= alvo and L > 1:
                ux, uy = (x1 - x0) / L, (y1 - y0) / L
                _cabeca(c, lerp(x0, x1, 0.55), lerp(y0, y1, 0.55), ux, uy, largura * 3.6, cor, 1.0)
            ac += L


def normal(c, t, t0, P, ang, comp=170, rotulo=None, escuro=False):
    """reta normal tracejada passando por P (ang em graus, 90 = vertical)"""
    if t < t0:
        return
    dx, dy = _dir(ang)
    q = ease_io(prog(t, t0, 0.5))
    tinta = _tinta(escuro)
    M.line(c, P[0], P[1], P[0] + dx * comp * q, P[1] + dy * comp * q, tinta, 0.6, 4, dash=E.TRACO)
    M.line(c, P[0], P[1], P[0] - dx * comp * q, P[1] - dy * comp * q, tinta, 0.6, 4, dash=E.TRACO)
    if rotulo:
        foco(c, t, t0 + 0.4, 0.4, lambda a: E._cola(c, rotulo, P[0] + dx * comp, P[1] + dy * comp, dx, dy, 10, 44, "i", tinta, a))


def espelho_plano(c, t, t0, A, B, lado=1, escuro=False):
    """espelho de A até B com a hachura do lado de trás"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    ux, uy = E._uni(*A, *B)
    nx, ny = uy * lado, -ux * lado
    _hachura(c, *A, *B, nx, ny, q, TINTA2 if not escuro else E.CLARO, 24, 20)
    M.line(c, *A, *B, TINTA if not escuro else BR, q, 8)


def _ponto_eixo(c, x, y, s, a, tinta, cor):
    c.drawCircle(x, y, 9, M.paint(cor, a))
    E._meio(c, s, x, y + 48, 44, "b", tinta, a)


def espelho_esferico(c, t, t0, vx, cy, R, abertura=70, concavo=True, eixo=None, focos=True, escuro=False):
    """espelho esférico com o vértice em (vx, cy), luz vindo da esquerda; desenha o eixo, F e C (o vértice V fica em vx). Devolve dict(F=x, C=x, V=x)"""
    tinta = _tinta(escuro)
    lado = -1 if concavo else 1
    Cx, Fx = vx + lado * R, vx + lado * R / 2
    if t < t0:
        return dict(F=Fx, C=Cx, V=vx)
    q = ep(t, t0, 0.6)
    if eixo:
        M.line(c, eixo[0], cy, eixo[1], cy, tinta, 0.5, 3, dash=E.TRACO, progress=q)
    a0 = (0 if concavo else 180) - abertura / 2
    cxc = Cx
    ret = skia.Rect.MakeXYWH(cxc - R, cy - R, 2 * R, 2 * R)
    for i in range(0, 15):
        g = math.radians(a0 + abertura * (i + 0.5) / 15)
        px, py = cxc + R * math.cos(g), cy + R * math.sin(g)
        sx = 1 if concavo else -1
        M.line(c, px, py, px + sx * 22 * math.cos(g) - 10, py + sx * 22 * math.sin(g) + 8, TINTA2 if not escuro else E.CLARO, 0.55 * q, 3)
    c.drawArc(ret, a0, abertura * ease_io(q), False, M.paint(tinta, 1.0, stroke=8, cap_round=True))
    if focos:
        foco(c, t, t0 + 0.4, 0.4, lambda a: (_ponto_eixo(c, Fx, cy, "F", a, tinta, E.COR), _ponto_eixo(c, Cx, cy, "C", a, tinta, tinta)))
    return dict(F=Fx, C=Cx, V=vx)


def lente(c, t, t0, cx, cy, h, convergente=True, f=None, eixo=None, escuro=False, cor=None):
    """lente de altura h centrada em (cx, cy); f = distância focal em pixels (marca F e F')"""
    if t < t0:
        return
    tinta = _tinta(escuro)
    q = ep(t, t0, 0.6)
    if eixo:
        M.line(c, eixo[0], cy, eixo[1], cy, tinta, 0.5, 3, dash=E.TRACO, progress=q)
    k = ease_back(q)
    hh, bw = h / 2 * k, h * 0.11
    p = skia.Path()
    if convergente:
        p.moveTo(cx, cy - hh); p.quadTo(cx + bw * 2, cy, cx, cy + hh); p.quadTo(cx - bw * 2, cy, cx, cy - hh)
    else:
        e = bw * 0.9
        p.moveTo(cx - e, cy - hh); p.lineTo(cx + e, cy - hh); p.quadTo(cx + e * 0.15, cy, cx + e, cy + hh)
        p.lineTo(cx - e, cy + hh); p.quadTo(cx - e * 0.15, cy, cx - e, cy - hh)
    p.close()
    c.drawPath(p, M.paint(cor or "#7FC8E8", 0.35 * q))
    pt = M.paint(tinta, q, stroke=5)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    if f:
        foco(c, t, t0 + 0.4, 0.4, lambda a: (_ponto_eixo(c, cx - f, cy, "F", a, tinta, E.COR), _ponto_eixo(c, cx + f, cy, "F'", a, tinta, E.COR)))


def objeto(c, t, t0, x, ybase, h, cor=None, rotulo=None, tracejado=False, largura=9, d=0.5, escuro=False):
    """seta vertical de objeto ou imagem a partir de (x, ybase); h > 0 para cima, h < 0 invertida"""
    if t < t0:
        return
    cor = cor or E.COR
    p = ease_out(prog(t, t0, d))
    if tracejado:
        M.line(c, x, ybase, x, ybase - (h - math.copysign(20, h)) * p, cor, 1.0, largura - 2, dash=E.TRACO)
        if p > 0.95:
            _cabeca(c, x, ybase - h, 0, -math.copysign(1, h), 30, cor, 1.0)
    else:
        seta(c, x, ybase, x, ybase - h, cor, 1.0, largura, 30, p)
    if rotulo:
        foco(c, t, t0 + d, 0.4, lambda a: E._cola(c, rotulo, x, ybase - h, 0, -math.copysign(1, h), 14, 46, "b", _tinta(escuro), a))


def termometro(c, t, t0, cx, yb, h, nivel, vmin=0, vmax=100, marcas=(), unidade="°C", cor=None, d=1.0, escuro=False, size=40):
    """termômetro com o bulbo em (cx, yb) e altura h; o líquido sobe de vmin até nivel em d segundos; marcas = valores com traço"""
    if t < t0:
        return
    tinta = _tinta(escuro)
    cor = cor or E.COR
    q = ep(t, t0, 0.4)
    rb, wt = 40, 32
    topo, base_t = yb - h, yb - rb * 0.6
    yv = lambda v: base_t - (float(v) - vmin) / (vmax - vmin) * (base_t - topo - wt / 2)
    vidro = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - wt / 2 - 8, topo - 8, wt + 16, base_t - topo + 20), wt / 2 + 8, wt / 2 + 8)
    c.drawRRect(vidro, M.paint(PAPEL if not escuro else "#14141C", q))
    c.drawCircle(cx, yb, rb + 8, M.paint(PAPEL if not escuro else "#14141C", q))
    c.drawRRect(vidro, M.paint(tinta, q, stroke=4))
    c.drawCircle(cx, yb, rb + 8, M.paint(tinta, q, stroke=4))
    c.drawCircle(cx, yb, rb, M.paint(cor, q))
    v = lerp(vmin, nivel, ease_io(prog(t, t0 + 0.3, d)))
    yl = yv(v)
    c.drawRect(skia.Rect.MakeLTRB(cx - wt / 2 + 4, yl, cx + wt / 2 - 4, yb - rb * 0.5), M.paint(cor, q))
    for i, m in enumerate(marcas):
        foco(c, t, t0 + 0.3 + 0.05 * i, 0.4, lambda a, m=m: (
            M.line(c, cx + wt / 2 + 14, yv(m), cx + wt / 2 + 40, yv(m), tinta, a, 4),
            medida(c, m, unidade, cx + wt / 2 + 54, yv(m) + size * 0.36, size, tinta, a, escuro=escuro)), sobe=6)


# ---------------- eletricidade e magnetismo ----------------
def fio(c, t, t0, pts, d=0.8, cor=None, largura=6, escuro=False):
    if t >= t0:
        poli(c, pts, ease_io(prog(t, t0, d)), cor or _tinta(escuro), 1.0, largura)


def no(c, P, a=1.0, escuro=False):
    if a > 0:
        c.drawCircle(*P, 11, M.paint(_tinta(escuro), a))


def _peca(c, t, t0, A, B, meio, desenha, rotulo, escuro, lado=1, gap=24, size=46):
    """componente entre A e B: fios das pontas até o miolo de tamanho `meio` e o desenho no sistema do componente"""
    ux, uy = E._uni(*A, *B)
    L = math.dist(A, B)
    cx, cy = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    tinta = _tinta(escuro)

    def fn(a):
        M.line(c, *A, cx - ux * meio / 2, cy - uy * meio / 2, tinta, a, 6)
        M.line(c, cx + ux * meio / 2, cy + uy * meio / 2, *B, tinta, a, 6)
        c.save(); c.translate(cx, cy); c.rotate(math.degrees(math.atan2(uy, ux)))
        desenha(a)
        c.restore()
        if rotulo:
            nx, ny = uy * lado, -ux * lado
            E._cola(c, rotulo, cx, cy, nx, ny, gap + 34, size, "b", tinta, a)
    foco(c, t, t0, 0.5, fn)


def resistor(c, t, t0, A, B, rotulo=None, escuro=False, lado=1, cor=None):
    """resistor em zigue-zague entre A e B"""
    def d(a):
        pts = [(-70, 0)] + [(-70 + 140 * i / 8, 22 * (1 if i % 2 else -1)) for i in range(1, 8)] + [(70, 0)]
        poli(c, pts, 1.0, cor or _tinta(escuro), a, 6)
    _peca(c, t, t0, A, B, 140, d, rotulo, escuro, lado)


def pilha(c, t, t0, A, B, rotulo=None, escuro=False, lado=1):
    """pilha (gerador) entre A e B: placa longa e fina é o polo +, a curta e grossa é o −; o + fica do lado de B"""
    tinta = _tinta(escuro)

    def d(a):
        M.line(c, 12, -46, 12, 46, tinta, a, 6, cap_round=False)
        M.line(c, -12, -24, -12, 24, tinta, a, 14, cap_round=False)
        E._meio(c, "+", 34, -46, 36, "g", E.COR, a)
    _peca(c, t, t0, A, B, 24, d, rotulo, escuro, lado, gap=40)


def lampada(c, t, t0, A, B, acesa=None, rotulo=None, escuro=False, lado=1, r=42):
    """lâmpada entre A e B; acesa = instante em que acende (brilho amarelo)"""
    tinta = _tinta(escuro)
    q = ep(t, acesa, 0.5) if acesa is not None else 0

    def d(a):
        if q > 0:
            g = skia.Paint(AntiAlias=True)
            g.setShader(skia.GradientShader.MakeRadial(skia.Point(0, 0), r * 2.6, [hexc("#FFC400", 0.55 * q * a), hexc("#FFC400", 0)], [0, 1]))
            c.drawCircle(0, 0, r * 2.6, g)
        c.drawCircle(0, 0, r, M.paint(mix("#FFFFFF", "#FFC400", q) if not escuro else mix("#14141C", "#FFC400", q), a))
        c.drawCircle(0, 0, r, M.paint(tinta, a, stroke=5))
        k = r * 0.68
        M.line(c, -k, -k, k, k, tinta, a, 5)
        M.line(c, -k, k, k, -k, tinta, a, 5)
    _peca(c, t, t0, A, B, 2 * r, d, rotulo, escuro, lado, gap=r - 10)


def chave(c, t, t0, A, B, fechada=True, escuro=False, rotulo=None, lado=1):
    """chave (interruptor) entre A e B; fechada pode ser 0..1 para animar"""
    tinta = _tinta(escuro)
    f = float(fechada)

    def d(a):
        c.drawCircle(-50, 0, 9, M.paint(tinta, a))
        c.drawCircle(50, 0, 9, M.paint(tinta, a))
        g = math.radians(-32 * (1 - f))
        M.line(c, -50, 0, -50 + 100 * math.cos(g), 100 * math.sin(g), tinta, a, 6)
    _peca(c, t, t0, A, B, 100, d, rotulo, escuro, lado)


def corrente(c, t, t0, pts, cor=None, vel=120, espaco=110, fecha=True, a=1.0):
    """setinhas que andam pela polilinha no sentido da corrente (convencional: do + para o −, por fora da pilha)"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    cor = cor or E.COR
    ps = list(pts) + ([pts[0]] if fecha else [])
    comp = [math.dist(ps[i], ps[i + 1]) for i in range(len(ps) - 1)]
    total = sum(comp)
    s = (t - t0) * vel % espaco
    while s < total:
        ac = 0.0
        for (x0, y0), (x1, y1), L in zip(ps, ps[1:], comp):
            if ac + L >= s and L > 0:
                f = (s - ac) / L
                _cabeca(c, lerp(x0, x1, f), lerp(y0, y1, f), (x1 - x0) / L, (y1 - y0) / L, 22, cor, q)
                break
            ac += L
        s += espaco


def ima(c, t, t0, cx, cy, w=360, h=110, giro=0.0, size=None):
    """ímã em barra: N laranja à direita (com giro = 0) e S azul"""
    k = ease_back(prog(t, t0, 0.5))
    if k <= 0:
        return
    a = clamp(k)
    c.save(); c.translate(cx, cy); c.rotate(-giro); c.scale(k, k)
    sz = size or h * 0.55
    for lado, cor, s in ((1, E.COR, "N"), (-1, NEG, "S")):
        x0 = 0 if lado > 0 else -w / 2
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, -h / 2), skia.Point(0, h / 2)],
                                                   [hexc(mix(cor, BR, 0.2), a), hexc(mix(cor, "#000000", 0.2), a)]))
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, -h / 2, w / 2, h), 10, 10)
        c.drawRRect(rr, p)
        E._meio(c, s, lado * w / 4, 0, sz, "g", BR, a)
    c.restore()


def _bezier(P0, P1, P2, P3, n=60):
    out = []
    for i in range(n + 1):
        u = i / n
        v = 1 - u
        out.append((v ** 3 * P0[0] + 3 * v * v * u * P1[0] + 3 * v * u * u * P2[0] + u ** 3 * P3[0],
                    v ** 3 * P0[1] + 3 * v * v * u * P1[1] + 3 * v * u * u * P2[1] + u ** 3 * P3[1]))
    return out


def linhas_campo(c, t, t0, cx, cy, w=360, n=3, cor=None, d=1.2, h=110, escuro=False, largura=4):
    """linhas de campo do ímã em barra de (cx, cy) com N à direita: saem do N, contornam e entram no S, com setas"""
    if t < t0:
        return
    cor = cor or (TINTA2 if not escuro else E.CLARO)
    p = ease_io(prog(t, t0, d))
    xn, xs = cx + w / 2, cx - w / 2
    for k in range(1, n + 1):
        Hk, Dk, o = h * (0.45 + 0.7 * k), w * (0.12 + 0.16 * k), h * 0.2
        for s_ in (-1, 1):
            topo = cy + s_ * (h / 2 + Hk)
            dir_ = _bezier((xn, cy + s_ * o), (xn + Dk * 1.3, cy + s_ * o), (xn + Dk, topo), (cx, topo), 40)
            esq = _bezier((cx, topo), (xs - Dk, topo), (xs - Dk * 1.3, cy + s_ * o), (xs, cy + s_ * o), 40)
            poli(c, dir_ + esq[1:], p, cor, 1.0, largura)
            if p > 0.6:
                _cabeca(c, cx - 11, topo, -1, 0, 22, cor, ep(t, t0 + d * 0.6, 0.3))
    for x0, x1 in ((xn + 10, xn + w * 0.75), (xs - w * 0.75, xs - 10)):
        M.line(c, x0, cy, lerp(x0, x1, p), cy, cor, 1.0, largura)
        if p > 0.6:
            _cabeca(c, (x0 + x1) / 2 + 11, cy, 1, 0, 22, cor, ep(t, t0 + d * 0.6, 0.3))


def carga(c, t, t0, cx, cy, r=56, sinal="+", rotulo=None, escuro=False):
    """esfera laranja (+) ou azul (−) com o sinal desenhado"""
    k = ease_back(prog(t, t0, 0.5))
    if k <= 0:
        return
    cor = E.COR if sinal == "+" else NEG
    E.bola(c, cx, cy, r * k, cor)
    s = r * k * 0.45
    M.line(c, cx - s, cy, cx + s, cy, BR, 1.0, max(4, r * 0.13))
    if sinal == "+":
        M.line(c, cx, cy - s, cx, cy + s, BR, 1.0, max(4, r * 0.13))
    if rotulo:
        foco(c, t, t0 + 0.3, 0.4, lambda a: E._cola(c, rotulo, cx, cy + r, 0, 1, 16, 46, "b", _tinta(escuro), a))


def campo_carga(c, t, t0, cx, cy, r0, r1, n=8, sai=True, cor=None, d=0.6, escuro=False):
    """setas radiais de r0 até r1: saem da carga + (sai=True) ou entram na − (sai=False)"""
    cor = cor or (TINTA2 if not escuro else E.CLARO)
    for i in range(n):
        g = 2 * math.pi * i / n + math.pi / n
        dx, dy = math.cos(g), math.sin(g)
        A, B = (cx + dx * r0, cy + dy * r0), (cx + dx * r1, cy + dy * r1)
        if not sai:
            A, B = B, A
        q = ease_out(prog(t, t0 + 0.04 * i, d))
        seta(c, *A, *B, cor, 1.0, 5, 22, q)
