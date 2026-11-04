"""Elenco do canal Nós, os Antigos: personagens e objetos reutilizáveis no padrão de acabamento da Lume.

O padrão da Lume (ver antigos.lume) que todo elemento daqui segue:
  1. formas arredondadas, sem contorno preto;
  2. sombreamento plano: a cor base + UMA forma de sombra recortada dentro da peça (embaixo/à direita)
     + UM brilho claro (em cima/à esquerda);
  3. sombra de contato no chão, desfocada;
  4. rosto com vida: olho com reflexo branco, sobrancelha, boca que fala, bochecha;
  5. vida em repouso: respiração, piscadas e balanço em tempos determinísticos (função do tempo t).

Peças:
  antigo(c, x, y, s, p)          → uma pessoa do século 21 (pés em x, y; s=1 ≈ 172 px), p = antigo_pose(...)
  antigo_vivo(t, seed, **base)    → pose com respiração e piscadas
  pessoa2(...)                    → atalho com a assinatura da antiga antigos.pessoa (troca direta)
  mao(c, x, y, s, gesto, ...)     → mão em close (gestos: "aponta", "toque", "aberta"), punho em (x, y)
  rato(c, x, y, s, t, ...)        → rato de laboratório de perfil
  cerebro(c, cx, cy, s, flash)    → cérebro com sulcos e brilho de dopamina
  celular_aceso / tela_apps       → o celular (peça 002) com tela de apps ou feed
  mesa, caixa_madeira             → móveis de madeira com volume
  olho, sino, moeda, coracao, estrela, raio, simbolo, ampulheta, caca_niquel → objetos e ícones com volume

Catálogo com todas as poses: canais/antigos/visual/elenco/ (python elenco.py).
"""
import colorsys
import math
import random
import skia
from antigos import (INK, BONE, AMBER, CORAL, CYAN, PINK, SKY, PELE, hexc, mix, clamp, lerp, paint, linear, radial,
                     oval, rr, poly, glow, pop, text)

AZUL_TELA = "#4cc9ff"
CLARO = "#ffffff"


# =====================================================================
# utilitários de sombreamento (o "jeito Lume")
# =====================================================================
def sombra(cor, k=0.28):
    """tom de sombra de uma cor: escurece mantendo o matiz (mais saturado) e puxa um pouco para o azul-noturno
    do canal, nunca para o preto nem para o verde-oliva (amarelo escurece para âmbar/laranja)"""
    h = cor.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    hh, ss, vv = colorsys.rgb_to_hsv(r, g, b)
    if 0.08 < hh < 0.19:                     # amarelos/âmbar: a sombra gira para o laranja
        hh -= 0.045 * k / 0.28
    r, g, b = colorsys.hsv_to_rgb(hh, min(1, ss + 0.25 * k), vv * (1 - 0.85 * k))
    out = "#%02x%02x%02x" % tuple(int(round(x * 255)) for x in (r, g, b))
    return mix(out, INK, 0.25 * k)


def luz(cor, k=0.35):
    return mix(cor, CLARO, k)


def volume(c, path, cor, sh=None, hl=None, k_sh=0.28, k_hl=0.35, hl_a=0.5):
    """pinta a forma com a cor base + uma sombra e um brilho recortados dentro dela.
    sh / hl = (cx, cy, rx, ry) das manchas de sombra e de brilho, nas coordenadas locais"""
    c.drawPath(path, paint(cor))
    if sh is None and hl is None:
        return
    c.save()
    c.clipPath(path, doAntiAlias=True)
    if sh:
        c.drawOval(oval(*sh), paint(sombra(cor, k_sh)))
    if hl:
        c.drawOval(oval(*hl), paint(luz(cor, k_hl), hl_a))
    c.restore()


def capsula(x0, y0, x1, y1, r):
    """caminho de uma cápsula (bastão de pontas redondas) entre dois pontos"""
    p = skia.Path()
    ang = math.atan2(y1 - y0, x1 - x0)
    n = (math.cos(ang + math.pi / 2) * r, math.sin(ang + math.pi / 2) * r)
    p.moveTo(x0 + n[0], y0 + n[1])
    p.lineTo(x1 + n[0], y1 + n[1])
    p.arcTo(skia.Rect.MakeLTRB(x1 - r, y1 - r, x1 + r, y1 + r), math.degrees(ang) + 90, -180, False)
    p.lineTo(x0 - n[0], y0 - n[1])
    p.arcTo(skia.Rect.MakeLTRB(x0 - r, y0 - r, x0 + r, y0 + r), math.degrees(ang) - 90, -180, False)
    p.close()
    return p


def piscadas(t, seed=0, media=3.6):
    """0..1 (1 = olho fechado) em tempos pseudoaleatórios fixos por seed"""
    rnd = random.Random(seed * 7919 + 13)
    tb = rnd.uniform(0.4, media)
    while tb < t + 1:
        u = (t - tb) / 0.16
        if 0 <= u <= 1:
            return math.sin(math.pi * u)
        tb += rnd.uniform(media * 0.6, media * 1.5)
    return 0.0


# =====================================================================
# OS ANTIGOS (pessoas do século 21)
# =====================================================================
CABELOS = ["#2b1a12", "#4a2a18", "#1a1210", "#8a4a22", "#c9c9c9", "#d9a441"]
ESTILOS = ["curto", "franja", "coque", "cacheado", "rabo", "longo", "careca"]
CALCA = "#34449c"
SAPATO = "#1a2050"

ANTIGO = dict(roupa=CORAL, pele=PELE[0], cabelo=CABELOS[0], estilo="curto", calca=CALCA, face=1,
              braco_d=0.0, braco_e=0.0, cabeca=0.0, look=(0.6, 0.0), blink=0.0, lid=0.0, brow=0.0, smile=0.5,
              mouth=0.0, cheek=0.45, respira=0.0, celular=None, tela=1.0, tela_luz=0.0, t=0.0, oculos=False,
              pulo=0.0)


def antigo_pose(**kw):
    d = dict(ANTIGO)
    d.update(kw)
    return d


EXPRESSOES = dict(
    neutro=dict(),
    feliz=dict(smile=1.0, brow=0.2, cheek=0.7),
    surpreso=dict(mouth=0.55, brow=0.8, smile=0.0, lid=0.0),
    preocupado=dict(brow=-0.7, smile=-0.4),
    hipnotizado=dict(lid=0.45, look=(0.7, 0.9), smile=0.0, brow=0.0, tela_luz=1.0, cabeca=16),
    cansado=dict(lid=0.55, smile=-0.2, brow=-0.3),
    dormindo=dict(lid=1.0, smile=0.3),
)


def expressao(nome, **kw):
    d = dict(EXPRESSOES[nome])
    d.update(kw)
    return d


def antigo_vivo(t, seed=0, **base):
    """pose com vida (respiração, piscadas, cabeça balançando de leve); seed muda o ritmo de cada pessoa"""
    p = antigo_pose(**base)
    p["t"] = t
    ph = seed * 1.7
    p["respira"] = p["respira"] + math.sin(t * 2.0 + ph)
    p["blink"] = max(p["blink"], piscadas(t, seed))
    p["cabeca"] = p["cabeca"] + 1.6 * math.sin(t * 1.3 + ph)
    return p


def _cabelo_atras(c, p, hx, hy, R):
    e, cor = p["estilo"], p["cabelo"]
    if e == "longo":
        cab = skia.Path()
        cab.moveTo(hx - R * 1.02, hy - R * 0.1)
        cab.cubicTo(hx - R * 1.25, hy + R * 0.9, hx - R * 0.9, hy + R * 1.65, hx - R * 0.2, hy + R * 1.55)
        cab.lineTo(hx + R * 0.2, hy + R * 0.6)
        cab.lineTo(hx + R * 0.9, hy - R * 0.2)
        cab.close()
        volume(c, cab, cor, sh=(hx - R * 0.2, hy + R * 1.3, R * 0.8, R * 0.5))
    elif e == "rabo":
        cab = capsula(hx - R * 0.95, hy - R * 0.25, hx - R * 1.45, hy + R * 0.85, R * 0.32)
        volume(c, cab, cor, sh=(hx - R * 1.3, hy + R * 0.8, R * 0.4, R * 0.3))
        c.drawCircle(hx - R * 0.98, hy - R * 0.22, R * 0.2, paint(mix(cor, CORAL, 0.6)))
    elif e == "coque":
        cq = skia.Path()
        cq.addCircle(hx - R * 0.35, hy - R * 1.08, R * 0.42)
        volume(c, cq, cor, sh=(hx - R * 0.15, hy - R * 0.9, R * 0.4, R * 0.3), hl=(hx - R * 0.5, hy - R * 1.25, R * 0.16, R * 0.1))


def _cabelo_frente(c, p, hx, hy, R):
    e, cor = p["estilo"], p["cabelo"]
    if e == "careca":
        lado = skia.Path()
        lado.addOval(oval(hx - R * 0.72, hy + R * 0.02, R * 0.3, R * 0.42))
        c.drawPath(lado, paint(cor, 0.9))
        return
    if e == "cacheado":
        cab = skia.Path()
        for ang in range(130, 345, 19):
            a = math.radians(ang)
            cab.addCircle(hx - R * 0.08 + math.cos(a) * R * 0.95, hy - R * 0.12 + math.sin(a) * R * 0.9, R * 0.34)
        cab.addOval(oval(hx - R * 0.2, hy - R * 0.62, R * 0.9, R * 0.42))
        volume(c, cab, cor, sh=(hx + R * 0.5, hy - R * 0.2, R * 0.7, R * 0.45),
               hl=(hx - R * 0.4, hy - R * 0.95, R * 0.35, R * 0.18), hl_a=0.45)
        return
    # touca base: cobre o alto da cabeça e a nuca (lado de trás = esquerda, porque o rosto olha p/ direita)
    cab = skia.Path()
    cab.moveTo(hx - R * 1.04, hy + R * 0.25)
    cab.cubicTo(hx - R * 1.18, hy - R * 1.05, hx + R * 0.55, hy - R * 1.38, hx + R * 1.02, hy - R * 0.3)
    if e == "franja":
        cab.cubicTo(hx + R * 0.8, hy - R * 0.12, hx + R * 0.45, hy - R * 0.2, hx + R * 0.3, hy - R * 0.35)
        cab.cubicTo(hx + R * 0.1, hy - R * 0.12, hx - R * 0.15, hy - R * 0.25, hx - R * 0.25, hy - R * 0.38)
        cab.cubicTo(hx - R * 0.4, hy - R * 0.1, hx - R * 0.55, hy, hx - R * 0.5, hy + R * 0.22)
    else:
        cab.cubicTo(hx + R * 0.6, hy - R * 0.62, hx + R * 0.05, hy - R * 0.55, hx - R * 0.3, hy - R * 0.42)
        cab.cubicTo(hx - R * 0.45, hy - R * 0.2, hx - R * 0.5, hy, hx - R * 0.45, hy + R * 0.22)
    cab.cubicTo(hx - R * 0.6, hy + R * 0.42, hx - R * 0.95, hy + R * 0.45, hx - R * 1.04, hy + R * 0.25)
    cab.close()
    volume(c, cab, cor, sh=(hx - R * 0.6, hy + R * 0.1, R * 0.6, R * 0.5),
           hl=(hx - R * 0.15, hy - R * 0.88, R * 0.42, R * 0.13), hl_a=0.4)


def _rosto(c, p, hx, hy, R):
    """rosto no estilo das referências: olhos = ovais escuros com um brilho, bochecha rosada, nariz como
    uma bolinha de pele mais escura, boca pequena; tudo deslocado para o lado em que a pessoa olha"""
    pele = p["pele"]
    lx, ly = p["look"]
    fx = hx + R * 0.26
    ey = hy + R * 0.02
    fech = max(p["blink"], p["lid"])
    # orelha (lado de trás)
    c.drawOval(oval(hx - R * 0.62, hy + R * 0.08, R * 0.17, R * 0.24), paint(sombra(pele, 0.16)))
    # bochecha
    if p["cheek"] > 0:
        c.drawOval(oval(fx + R * 0.5, hy + R * 0.36, R * 0.22, R * 0.13), paint("#ff7a86", p["cheek"] * 0.55))
    for k, ox in enumerate((-R * 0.3, R * 0.3)):
        ex = fx + ox + lx * R * 0.07
        ry = R * 0.2 * (1 - 0.92 * fech)
        rx = R * (0.13 if k == 0 else 0.15)
        if fech > 0.85:
            f = skia.Path()
            f.moveTo(ex - rx * 1.3, ey + R * 0.02)
            f.quadTo(ex, ey + R * 0.14, ex + rx * 1.3, ey + R * 0.02)
            c.drawPath(f, paint("#1d1626", stroke=R * 0.075))
        else:
            c.drawOval(oval(ex, ey + ly * R * 0.06, rx, ry), paint("#1d1626"))
            c.drawCircle(ex - rx * 0.35, ey + ly * R * 0.06 - ry * 0.4, R * 0.045, paint(CLARO, 0.9))
            if p["lid"] > 0.05:                 # pálpebra pesada (cansado / hipnotizado)
                c.drawRect(skia.Rect.MakeLTRB(ex - rx * 1.4, ey - R * 0.3, ex + rx * 1.4, ey - ry + 2 * ry * p["lid"]),
                           paint(sombra(pele, 0.08)))
        # sobrancelha
        c.save()
        c.translate(ex, ey - R * 0.36 - R * 0.07 * max(0, p["brow"]))
        c.rotate((-1 if k == 0 else 1) * 14 * p["brow"])
        c.drawLine(-rx * 1.2, 0, rx * 1.2, 0, paint(sombra(p["cabelo"], 0.05), stroke=R * 0.1))
        c.restore()
    if p.get("oculos"):
        for ox in (-R * 0.3, R * 0.3):
            c.drawCircle(fx + ox, ey, R * 0.27, paint("#2a2440", stroke=R * 0.06))
        c.drawLine(fx - R * 0.04, ey, fx + R * 0.04, ey, paint("#2a2440", stroke=R * 0.06))
    # nariz
    c.drawOval(oval(fx + R * 0.08, ey + R * 0.27, R * 0.15, R * 0.11), paint(sombra(pele, 0.17)))
    # boca
    mx, my, mo, sm = fx + R * 0.06, hy + R * 0.58, p["mouth"], p["smile"]
    if mo < 0.06:
        b = skia.Path()
        b.moveTo(mx - R * 0.17, my - R * 0.03 * sm)
        b.quadTo(mx, my + R * 0.15 * sm, mx + R * 0.17, my - R * 0.03 * sm)
        c.drawPath(b, paint(sombra(pele, 0.55), stroke=R * 0.075))
    else:
        h = R * (0.08 + 0.24 * mo)
        b = skia.Path()
        b.addOval(oval(mx, my + h * 0.4, R * 0.16, h * 0.7))
        c.drawPath(b, paint("#4a1a24"))
        c.save()
        c.clipPath(b, doAntiAlias=True)
        c.drawOval(oval(mx, my + h * 1.0, R * 0.12, h * 0.4), paint(CORAL, 0.9))
        c.restore()


def _membro(x0, y0, x1, y1, r0, r1):
    """membro que afina (cápsula com pontas de raios diferentes)"""
    ang = math.atan2(y1 - y0, x1 - x0)
    nx, ny = math.cos(ang + math.pi / 2), math.sin(ang + math.pi / 2)
    p = skia.Path()
    p.moveTo(x0 + nx * r0, y0 + ny * r0)
    p.lineTo(x1 + nx * r1, y1 + ny * r1)
    p.arcTo(skia.Rect.MakeLTRB(x1 - r1, y1 - r1, x1 + r1, y1 + r1), math.degrees(ang) + 90, -180, False)
    p.lineTo(x0 - nx * r0, y0 - ny * r0)
    p.arcTo(skia.Rect.MakeLTRB(x0 - r0, y0 - r0, x0 + r0, y0 + r0), math.degrees(ang) - 90, -180, False)
    p.close()
    return p


def _ik(ox, oy, tx, ty, l1, l2):
    """cotovelo de um braço de dois segmentos (ombro → alvo); escolhe o cotovelo mais baixo/para trás"""
    dx, dy = tx - ox, ty - oy
    d = max(1e-3, min(math.hypot(dx, dy), l1 + l2 - 1e-3))
    a = math.atan2(dy, dx)
    cb = clamp((l1 * l1 + d * d - l2 * l2) / (2 * l1 * d), -1, 1)
    b = math.acos(cb)
    op = [(ox + math.cos(a + sg * b) * l1, oy + math.sin(a + sg * b) * l1) for sg in (1, -1)]
    return max(op, key=lambda e: e[1] - 0.25 * e[0])


def _braco(c, p, lado, ombro, ang, pele, manga):
    """braço inteiro (manga longa + mão de luva) com cotovelo; ang 0 = pendurado, 1.25 = segura o celular na
    frente do rosto, 2.6 = para cima. Devolve a posição da mão."""
    ox, oy = ombro
    D = 54.0 - 4.0 * clamp(ang / 1.25)            # pendurado: quase reto; levantado: cotovelo dobra
    tx, ty = ox + math.sin(ang) * D, oy + math.cos(ang) * D
    ex, ey = _ik(ox, oy, tx, ty, 28.0, 28.0)
    cor = manga if lado > 0 else sombra(manga, 0.2)
    pc = pele if lado > 0 else sombra(pele, 0.14)
    if lado > 0:                                   # sombra do braço da frente sobre o tronco
        c.drawPath(_membro(ox - 2, oy + 4, ex - 2, ey + 4, 6.5, 5.5), paint(sombra(manga, 0.35), 0.45, blur=2.5))
    # mão de luva (antes da manga, que cobre o punho)
    ha = math.atan2(ty - ey, tx - ex)
    hx, hy = tx + math.cos(ha) * 2, ty + math.sin(ha) * 2
    c.save()
    c.translate(hx, hy)
    c.rotate(math.degrees(ha) - 90)
    mao_p = skia.Path()
    mao_p.addOval(oval(0, 0.5, 5.0, 6.3))
    volume(c, mao_p, pc, sh=(3.6, 2.5, 3, 6), k_sh=0.12)
    c.drawOval(oval(-4.6 * lado, -1.5, 2.6, 4.0), paint(sombra(pc, 0.1)))     # polegar
    c.restore()
    braco_p = _membro(ox, oy, ex, ey, 6.6, 5.4)
    braco_p.addPath(_membro(ex, ey, tx - math.cos(ha) * 3, ty - math.sin(ha) * 3, 5.4, 4.6))
    c.drawPath(braco_p, paint(cor))
    c.save()
    c.clipPath(braco_p, doAntiAlias=True)
    c.drawPath(_membro(ox + 3.5, oy + 1, ex + 3.5, ey + 1, 3.6, 3), paint(sombra(cor, 0.2)))
    c.drawPath(_membro(ex + 3, ey, tx + 3, ty, 3, 2.6), paint(sombra(cor, 0.2)))
    c.restore()
    return hx, hy


def antigo(c, x, y, s=1.0, p=None, a=1.0):
    """um Antigo com os pés em (x, y); s=1 → ~172 px. p = antigo_pose(...) / antigo_vivo(...)
    Proporções das referências (Kurzgesagt / Infographics Show): cabeça ≈ 1/5 da altura, pescoço, ombros
    caídos, tronco que afina na cintura, braços e pernas longos que afinam, mãos de luva, pés pequenos.
    face: 1 olha p/ direita, -1 p/ esquerda · braco_d/braco_e: ângulo em radianos (0 = pendurado,
    1.25 = celular na frente do rosto, 2.6 = para cima) · cabeca: inclinação em graus (+ = pescoço dobrado)
    · celular: None ou "d" · tela_luz: luz azul da tela no rosto · pulo: px para cima
    Devolve a posição (tela) da mão da frente."""
    p = p or ANTIGO
    if a <= 0:
        return (x, y)
    if a < 1:
        c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.drawOval(oval(x, y + 2, 30 * s * (1 - 0.003 * p["pulo"]), 5.5 * s), paint(INK, 0.35, blur=4 * s))
    c.save()
    c.translate(x, y - p["pulo"] * s)
    c.scale(s * p["face"], s)
    pele, roupa, calca = p["pele"], p["roupa"], p["calca"]
    rs = 1 + 0.012 * p["respira"]
    # pernas (afinam até o tornozelo) e pés
    for lx, cor in ((-6, sombra(calca, 0.18)), (6, calca)):
        perna = _membro(lx, -84, lx + 1.5, -9, 7.4, 4.8)
        c.drawPath(perna, paint(cor))
        c.save()
        c.clipPath(perna, doAntiAlias=True)
        c.drawPath(_membro(lx + 4.5, -84, lx + 5, -9, 3.6, 2.2), paint(sombra(cor, 0.2)))
        c.restore()
        pe = skia.Path()
        pe.addOval(oval(lx + 5.5, -4.5, 9.5, 4.8))
        volume(c, pe, SAPATO if lx > 0 else sombra(SAPATO, 0.1), hl=(lx + 3, -7, 5, 1.4), hl_a=0.35)
    # braço de trás
    _braco(c, p, -1, (-12, -119), p["braco_e"], pele, roupa)
    # pescoço
    pc = skia.Path()
    pc.addRRect(rr(-5, -140, 10.5, 16, 4))
    volume(c, pc, sombra(pele, 0.1), sh=(5, -128, 4, 10))
    # tronco único: ombros caídos, cintura, quadril
    c.save()
    c.translate(0, -80)
    c.scale(1, rs)
    tr = skia.Path()
    tr.moveTo(-6, -49)
    tr.cubicTo(-14, -48, -20, -45, -20, -36)
    tr.cubicTo(-20, -25, -15, -16, -15, -8)
    tr.cubicTo(-16, -2, -16, 2, -15, 5)
    tr.lineTo(15, 5)
    tr.cubicTo(16, 2, 16, -2, 15, -8)
    tr.cubicTo(15, -16, 20, -25, 20, -36)
    tr.cubicTo(20, -45, 14, -48, 6, -49)
    tr.cubicTo(3, -46, -3, -46, -6, -49)
    tr.close()
    volume(c, tr, roupa, sh=(24, -16, 13, 40), hl=(-13, -40, 4, 5), k_sh=0.22, hl_a=0.4)
    c.save()
    c.clipPath(tr, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeLTRB(-22, 0, 22, 8), paint(sombra(roupa, 0.12)))     # barra
    c.drawOval(oval(0, -48, 6.5, 3.6), paint(sombra(roupa, 0.25)))              # gola
    c.restore()
    c.restore()
    # cabeça (inclina em volta do pescoço)
    R = 17.0
    c.save()
    c.translate(1, -136)
    c.rotate(p["cabeca"])
    hx, hy = 0.0, -17.0
    _cabelo_atras(c, p, hx, hy, R)
    cab = skia.Path()
    cab.moveTo(hx - R * 0.95, hy - R * 0.1)
    cab.cubicTo(hx - R * 1.0, hy - R * 1.25, hx + R * 1.0, hy - R * 1.25, hx + R * 0.95, hy - R * 0.1)
    cab.cubicTo(hx + R * 0.95, hy + R * 0.6, hx + R * 0.55, hy + R * 1.08, hx + R * 0.05, hy + R * 1.08)
    cab.cubicTo(hx - R * 0.5, hy + R * 1.08, hx - R * 0.95, hy + R * 0.6, hx - R * 0.95, hy - R * 0.1)
    cab.close()
    volume(c, cab, pele, sh=(hx - R * 0.75, hy + R * 0.45, R * 0.55, R * 0.9), k_sh=0.13,
           hl=(hx + R * 0.35, hy - R * 0.55, R * 0.26, R * 0.14), hl_a=0.35)
    _rosto(c, p, hx, hy, R)
    _cabelo_frente(c, p, hx, hy, R)
    if p["tela_luz"] > 0:
        c.save()
        c.clipPath(cab, doAntiAlias=True)
        c.drawRect(skia.Rect.MakeLTRB(-R * 2, hy - R * 1.3, R * 2, hy + R * 1.2),
                   radial(hx + R * 0.9, hy + R * 1.4, R * 2.1, [(AZUL_TELA, 0.55 * p["tela_luz"]), (AZUL_TELA, 0)],
                          blend=skia.BlendMode.kScreen))
        c.restore()
    c.restore()
    # braço da frente (e o celular nele)
    hxm, hym = _braco(c, p, 1, (12, -120), p["braco_d"], pele, roupa)
    if p["celular"]:
        cx_, cy_ = hxm + 2, hym - 13
        if p["tela"] > 0:
            glow(c, cx_, cy_, 46, AZUL_TELA, 0.45 * p["tela"])
        celular_aceso(c, cx_, cy_, 0.17, p["t"], p["tela"], ang=-20, a=1.0, brilho=False)
        luva = skia.Path()
        luva.addOval(oval(hxm, hym, 5.6, 6.6))
        volume(c, luva, pele, sh=(hxm + 3.5, hym + 3, 4, 6), k_sh=0.18)
        c.drawOval(oval(hxm - 3, hym - 6, 2.6, 4), paint(sombra(pele, 0.08)))   # polegar sobre a borda
    c.restore()
    if a < 1:
        c.restore()
    f = p["face"]
    return (x + f * hxm * s, y - p["pulo"] * s + hym * s)


def pessoa2(c, x, y, s=1.0, roupa=CORAL, pele=PELE[0], capacete=None, braco=0.0, a=1.0, cabelo="#3a2416", olhar=1,
            t=0.0, seed=0, estilo=None, **kw):
    """troca direta da antiga antigos.pessoa (mesmos argumentos), já com vida e rosto"""
    est = estilo or ESTILOS[seed % 5]
    p = antigo_vivo(t, seed, roupa=roupa, pele=pele, cabelo=cabelo, estilo=est, face=olhar, braco_d=braco,
                    braco_e=0.12, **kw)
    return antigo(c, x, y, s * 1.12, p, a)   # o corpo novo é mais esguio que a pessoa antiga: compensa a escala


# =====================================================================
# A MÃO (close)
# =====================================================================
def _salsicha(c, x0, y0, x1, y1, r, pele, lado_sh=1):
    """dedo grosso de luva: cápsula com uma faixa de sombra num lado e um brilho no outro (sem unha, sem ruga)"""
    d = capsula(x0, y0, x1, y1, r)
    ang = math.atan2(y1 - y0, x1 - x0)
    nx, ny = math.cos(ang + math.pi / 2) * lado_sh, math.sin(ang + math.pi / 2) * lado_sh
    c.drawPath(d, paint(pele))
    c.save()
    c.clipPath(d, doAntiAlias=True)
    c.drawPath(capsula(x0 + nx * r * 0.9, y0 + ny * r * 0.9, x1 + nx * r * 0.9, y1 + ny * r * 0.9, r * 0.7),
               paint(sombra(pele, 0.17)))
    c.drawPath(capsula(x0 - nx * r * 0.5, y0 - ny * r * 0.5, x1 - nx * r * 0.5, y1 - ny * r * 0.5, r * 0.14),
               paint(luz(pele, 0.3), 0.3))
    c.restore()
    return d


def mao(c, x, y, s=1.0, gesto="aponta", ang=0.0, pele=None, manga=SKY, braco=260.0, aperta=0.0, a=1.0):
    """mão em close no estilo das referências: luva gorda e simples, dedos grossos encostados, um tom de sombra.
    Punho em (x, y), dedos para cima (ang em graus gira tudo); s=1 → ~230 px do punho à ponta do indicador.
    gesto: "aponta", "toque" (= aponta, a ponta achata conforme aperta 0..1), "aberta".
    braco: comprimento da manga para baixo. Devolve a posição da ponta do indicador."""
    pele = pele or PELE[0]
    if a <= 0:
        return (x, y)
    if a < 1:
        c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.save()
    c.translate(x, y)
    c.rotate(ang)
    c.scale(s, s)
    sh = sombra(pele, 0.17)
    c.drawRRect(rr(-56 + 18, -70 + 20, 118, 150 + braco, 54), paint(INK, 0.2, blur=16))
    # manga larga com punho
    mg = skia.Path()
    mg.addRRect(rr(-58, 40, 120, braco, 40))
    volume(c, mg, manga, sh=(58, 40 + braco / 2, 34, braco), k_sh=0.2)
    c.drawRRect(rr(-62, 30, 128, 34, 17), paint(sombra(manga, 0.1)))
    c.drawRRect(rr(-54, 33, 108, 7, 3.5), paint(luz(manga, 0.3), 0.55))
    if gesto in ("aponta", "toque"):
        sq = 0.18 * aperta
        top = -170 + 8 * aperta
        # indicador grosso (a ponta achata no toque)
        c.save()
        c.translate(-26, top)
        c.scale(1 + sq, 1 - sq * 0.5)
        c.translate(26, -top)
        _salsicha(c, -26, -40, -26, top, 18, pele)
        c.restore()
        # punho: os três dedos dobrados formam uma massa redonda com três gomos em cima
        pu = skia.Path()
        pu.addRRect(rr(-48, -62, 102, 104, 44))
        for gx, gy, gr in ((2, -60, 17), (26, -56, 16), (44, -46, 14)):
            pu.addCircle(gx, gy, gr)
        c.drawPath(pu, paint(pele))
        c.save()
        c.clipPath(pu, doAntiAlias=True)
        c.drawOval(oval(54, -10, 34, 70), paint(sh))
        c.drawOval(oval(-30, -30, 10, 26), paint(luz(pele, 0.4), 0.45))
        for gx in (14, 36):                    # vãos entre os dedos dobrados (só uma sombra suave)
            c.drawOval(oval(gx, -50, 3, 14), paint(sh, 0.8))
        c.restore()
        # polegar grosso encostado no lado do punho, apontando para cima
        _salsicha(c, -50, 26, -46, -22, 15.5, pele, lado_sh=1)
        c.drawOval(oval(-34, 2, 3, 20), paint(sh, 0.7))
        ponta = (-26, top - 18)
    else:  # aberta: palma redonda + quatro dedos grossos encostados + polegar
        for fx, ln, r, ab in ((-30, 88, 16, -0.16), (-4, 104, 16.5, -0.04), (22, 98, 16, 0.08), (44, 76, 14.5, 0.2)):
            _salsicha(c, fx, -40, fx + math.sin(ab) * ln, -40 - math.cos(ab) * ln, r, pele)
        pal = skia.Path()
        pal.addRRect(rr(-50, -60, 108, 102, 46))
        volume(c, pal, pele, sh=(58, -6, 32, 66), hl=(-28, -28, 10, 24), k_sh=0.17, hl_a=0.45)
        _salsicha(c, -40, 14, -86, -36, 16, pele, lado_sh=-1)
        ponta = (-4 + math.sin(-0.04) * 104, -40 - math.cos(-0.04) * 104 - 16.5)
    c.restore()
    if a < 1:
        c.restore()
    ra = math.radians(ang)
    px, py = ponta[0] * s, ponta[1] * s
    return (x + px * math.cos(ra) - py * math.sin(ra), y + px * math.sin(ra) + py * math.cos(ra))


def toque_onda(c, x, y, k, cor=CLARO, a=1.0):
    """onda do toque na tela (k: 0..1 desde o toque)"""
    if 0 < k < 1:
        c.drawCircle(x, y, 10 + 60 * k, paint(cor, a * (1 - k) * 0.8, stroke=5 * (1 - k) + 1))
        c.drawCircle(x, y, 16 * (1 - k), paint(cor, a * 0.5 * (1 - k)))


# =====================================================================
# O CELULAR (peça 002)
# =====================================================================
APPS = [CORAL, AMBER, SKY, CYAN, PINK, "#7be36b", "#ff9f43", "#3a63e0"]


def tela_apps(c, x, y, w, h, t, badge=0.0, feed=0.0, a=1.0):
    """conteúdo da tela: grade de apps (feed=0) ou feed rolando (feed=1)"""
    c.save()
    c.clipRRect(rr(x, y, w, h, 10), doAntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), linear(x, y, x, y + h, ["#3fb8ff", "#2e47c9"], a=a))
    if feed < 1:
        al = a * (1 - feed)
        ic = w / 4.2
        for r_ in range(5):
            for k in range(3):
                cx, cy = x + w * (0.2 + k * 0.3), y + h * 0.13 + r_ * ic * 1.25
                cor = APPS[(r_ * 3 + k) % 8]
                c.drawRRect(rr(cx - ic / 2, cy - ic / 2, ic, ic, ic * 0.28), paint(cor, al))
                c.drawRRect(rr(cx - ic / 2, cy - ic / 2, ic, ic * 0.45, ic * 0.28), paint(CLARO, al * 0.18))
        if badge > 0:
            bx, by = x + w * 0.2 + ic / 2, y + h * 0.13 - ic / 2
            r = ic * 0.3 * pop(badge)
            c.drawCircle(bx, by, r, paint("#ff2d55", al))
            text(c, "3", bx, by + r * 0.42, r * 1.25, "display", 800, "#ffffff", al * clamp(badge * 2), "center")
    if feed > 0:
        off = (t * h * 0.35) % (h * 0.42)
        for k in range(-1, 4):
            yy = y + k * h * 0.42 - off + h * 0.04
            c.drawRRect(rr(x + w * 0.08, yy, w * 0.84, h * 0.36, 8), paint("#ffffff", 0.92 * a * feed))
            c.drawRRect(rr(x + w * 0.12, yy + h * 0.03, w * 0.76, h * 0.2, 6), paint(APPS[(k + 9) % 8], a * feed))
            c.drawCircle(x + w * 0.17, yy + h * 0.29, w * 0.045, paint(APPS[(k + 4) % 8], a * feed))
            c.drawRRect(rr(x + w * 0.25, yy + h * 0.27, w * 0.42, h * 0.022, 3), paint(INK, 0.4 * a * feed))
            c.drawRRect(rr(x + w * 0.25, yy + h * 0.31, w * 0.28, h * 0.018, 3), paint(INK, 0.22 * a * feed))
    c.restore()


def celular_aceso(c, cx, cy, s=1.0, t=0.0, tela=1.0, badge=0.0, feed=0.0, ang=0.0, a=1.0, brilho=True):
    """celular em pé (cx, cy = centro), tela 0 = apagada, 1 = acesa"""
    if a <= 0:
        return
    c.save()
    c.translate(cx, cy)
    c.rotate(ang)
    c.scale(s, s)
    w, h = 120, 236
    if tela > 0 and brilho:
        glow(c, 0, 0, 260, AZUL_TELA, 0.5 * tela * a)
    c.drawRRect(rr(-w / 2 + 8, -h / 2 + 10, w, h, 20), paint(INK, 0.45 * a, blur=8))
    # botões laterais
    c.drawRRect(rr(w / 2 - 2, -h * 0.22, 5, 34, 2), paint("#9aa6ad", a))
    c.drawRRect(rr(-w / 2 - 3, -h * 0.28, 5, 22, 2), paint("#9aa6ad", a))
    c.drawRRect(rr(-w / 2 - 3, -h * 0.16, 5, 22, 2), paint("#9aa6ad", a))
    c.drawRRect(rr(-w / 2, -h / 2, w, h, 20), paint("#1c232c", a))
    c.drawRRect(rr(-w / 2, -h / 2, w, h, 20), paint("#c9d3d6", 0.9 * a, stroke=4))
    c.drawRRect(rr(-w / 2 + 8, -h / 2 + 10, w - 16, h - 20, 12), paint("#141b24", a))
    if tela > 0:
        c.saveLayerAlpha(None, int(255 * clamp(tela) * a))
        tela_apps(c, -w / 2 + 8, -h / 2 + 10, w - 16, h - 20, t, badge, feed)
        c.restore()
    c.drawRRect(rr(-14, -h / 2 + 4, 28, 5, 2), paint("#0b0f14", a))
    # reflexo do vidro
    c.drawPath(poly([(-w / 2 + 10, -h / 2 + 12), (-w / 2 + 50, -h / 2 + 12), (-w / 2 + 10, -h / 2 + 90)]), paint("#ffffff", 0.07 * a))
    c.drawPath(poly([(w / 2 - 30, h / 2 - 12), (w / 2 - 10, h / 2 - 12), (w / 2 - 10, h / 2 - 60)]), paint("#ffffff", 0.05 * a))
    c.restore()


# =====================================================================
# O RATO (laboratório de Skinner)
# =====================================================================
RATO = dict(corpo="#cdd3ea", sombra="#a3abd0", barriga="#eef0fa", rosa="#f4a3b6", nariz="#f0738f")


def rato(c, x, y, s=1.0, t=0.0, aperta=0.0, dorme=0.0, a=1.0, seed=3):
    """rato fofo de perfil (olhando p/ direita), pés em (x, y); aperta = pata na alavanca (0..1);
    dorme = deitado de olhos fechados (0..1)"""
    if a <= 0:
        return
    R = RATO
    if a < 1:
        c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.drawOval(oval(x, y + 1, 78 * s, 9 * s), paint(INK, 0.3, blur=5 * s))
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    resp = 0.02 * math.sin(t * (2.0 if dorme > 0.5 else 5.0))
    c.rotate(-8 * aperta)
    dy = 10 * dorme
    # cauda (afina até a ponta)
    k = math.sin(t * 2.6)
    pts = [(-62, -14 + dy)]
    for i in range(1, 9):
        u = i / 8
        pts.append((-62 - 95 * u, -14 + dy - 50 * u * u + 10 * k * u * u * math.sin(u * 3)))
    for i in range(len(pts) - 1):
        c.drawLine(*pts[i], *pts[i + 1], paint(R["rosa"], stroke=7.5 * (1 - i / 9) + 1.5))
    # pata de trás
    pt = skia.Path()
    pt.addOval(oval(-38, -6, 18, 9))
    volume(c, pt, R["sombra"])
    # corpo (gota) com sombra, barriga e brilho
    c.save()
    c.scale(1 + resp, 1 - resp)
    corpo = skia.Path()
    corpo.addOval(oval(-4, -38 + dy, 70, 40 - dy * 0.6))
    volume(c, corpo, R["corpo"], sh=(10, -6 + dy, 70, 28), hl=(-28, -64 + dy, 26, 9), k_sh=0.0, hl_a=0.6)
    c.save()
    c.clipPath(corpo, doAntiAlias=True)
    c.drawOval(oval(14, -2 + dy, 70, 20), paint(R["sombra"]))
    c.drawOval(oval(18, -14 + dy, 40, 16), paint(R["barriga"], 0.75))
    c.restore()
    c.restore()
    # cabeça
    hx, hy = 54, -56 + dy * 1.4
    orelha = skia.Path()
    orelha.addCircle(hx - 14, hy - 30, 19)
    volume(c, orelha, R["corpo"], sh=(hx - 4, hy - 20, 14, 14))
    c.drawCircle(hx - 13, hy - 29, 11, paint(R["rosa"]))
    c.drawOval(oval(hx - 17, hy - 33, 4, 3), paint(CLARO, 0.5))
    cab = skia.Path()
    cab.moveTo(hx - 28, hy - 12)
    cab.cubicTo(hx - 26, hy - 34, hx + 4, hy - 34, hx + 22, hy - 16)
    cab.cubicTo(hx + 34, hy - 6, hx + 42, hy + 4, hx + 38, hy + 10)
    cab.cubicTo(hx + 30, hy + 20, hx - 6, hy + 24, hx - 20, hy + 16)
    cab.cubicTo(hx - 30, hy + 10, hx - 30, hy, hx - 28, hy - 12)
    cab.close()
    volume(c, cab, R["corpo"], sh=(hx + 4, hy + 20, 34, 12), hl=(hx - 10, hy - 22, 12, 6), hl_a=0.6)
    c.drawOval(oval(hx + 14, hy + 8, 7, 4.5), paint("#ff8a9a", 0.75))       # bochecha
    c.drawCircle(hx + 39, hy + 5, 6.5, paint(R["nariz"]))
    c.drawCircle(hx + 37, hy + 3, 2.2, paint(CLARO, 0.8))
    ex, ey = hx + 12, hy - 8
    fech = max(clamp((dorme - 0.4) / 0.4), piscadas(t, seed, 3.0))
    if fech > 0.9:
        f = skia.Path()
        f.moveTo(ex - 6, ey)
        f.quadTo(ex, ey + 5, ex + 6, ey)
        c.drawPath(f, paint(INK, stroke=2.6))
    else:
        olho = skia.Path()
        olho.addOval(oval(ex, ey, 7.5, 8.5 * (1 - fech)))
        c.drawPath(olho, paint("#1a1622"))
        c.drawCircle(ex - 2.4, ey - 3, 2.6, paint(CLARO, 0.95))
        c.drawCircle(ex + 2.6, ey + 2.6, 1.2, paint(CLARO, 0.6))
    for wy in (-5, 3, 10):
        c.drawLine(hx + 34, hy + 8, hx + 66, hy + 8 + wy * 1.6, paint(INK, 0.35, stroke=1.4))
    # pata da frente (sobe para a alavanca)
    px_, py_ = 46 + 20 * aperta, -4 - 40 * aperta + dy
    c.drawPath(capsula(40, -22 + dy, px_, py_, 6.5), paint(R["corpo"]))
    c.drawPath(capsula(43, -20 + dy, px_ + 3, py_, 3.5), paint(R["sombra"], 0.6))
    c.drawCircle(px_, py_, 6.5, paint(R["rosa"]))
    c.drawCircle(px_ - 2, py_ - 2, 2, paint(CLARO, 0.6))
    c.restore()
    if a < 1:
        c.restore()


# =====================================================================
# O CÉREBRO
# =====================================================================
def cerebro(c, cx, cy, s=1.0, flash=0.0, a=1.0):
    """cérebro de perfil (frente à direita), com sulcos e o brilho dos neurônios de dopamina (flash 0..1)"""
    if a <= 0:
        return
    if a < 1:
        c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.save()
    c.translate(cx, cy)
    c.scale(s, s)
    base, sh = "#ff9fbf", "#e66f99"
    c.drawOval(oval(10, 128, 120, 12), paint(INK, 0.3, blur=8))
    # tronco e cerebelo
    tronco = capsula(-10, 40, -20, 112, 16)
    volume(c, tronco, sh, sh=(-6, 90, 12, 30))
    cb = skia.Path()
    cb.addOval(oval(-62, 62, 42, 30))
    volume(c, cb, "#f088ad", sh=(-50, 80, 40, 20))
    for i in range(3):
        c.drawLine(-92 + i * 6, 52 + i * 10, -28, 54 + i * 10, paint(sh, stroke=3))
    # o cérebro (lobos)
    br = skia.Path()
    br.moveTo(-120, 30)
    br.cubicTo(-150, -40, -90, -110, -10, -108)
    br.cubicTo(70, -112, 136, -70, 130, 0)
    br.cubicTo(128, 40, 96, 60, 60, 54)
    br.cubicTo(30, 70, -10, 60, -40, 50)
    br.cubicTo(-80, 66, -112, 56, -120, 30)
    br.close()
    volume(c, br, base, sh=(30, 70, 150, 60), hl=(-40, -80, 60, 20), k_sh=0.0, hl_a=0.55)
    c.save()
    c.clipPath(br, doAntiAlias=True)
    c.drawOval(oval(30, 72, 150, 56), paint(sh, 0.6))
    rnd = random.Random(5)
    for k in range(9):                            # sulcos (giros)
        x0 = -110 + k * 26
        g = skia.Path()
        g.moveTo(x0, -90 + rnd.uniform(-8, 8))
        for j in range(4):
            g.quadTo(x0 + rnd.uniform(-22, 22), -60 + j * 32, x0 + rnd.uniform(-10, 10), -44 + j * 32)
        c.drawPath(g, paint(sh, 0.9, stroke=5))
    c.drawLine(-100, 6, 40, 14, paint(sh, stroke=6))   # sulco lateral
    c.restore()
    if flash > 0:
        glow(c, 10, 30, 140 * (0.6 + 0.4 * flash), AMBER, 0.85 * flash)
        c.drawCircle(10, 30, 14 * flash, paint(CLARO, flash))
    c.restore()
    if a < 1:
        c.restore()


def mao_na_ponta(c, px, py, s=1.0, gesto="toque", ang=0.0, **kw):
    """desenha a mão de modo que a ponta do indicador fique em (px, py) (útil para tocar/arrastar na tela)"""
    ap = kw.get("aperta", 0.0)
    lx, ly = (-26, -170 + 8 * ap - 18) if gesto != "aberta" else (-4 + math.sin(-0.04) * 104, -40 - math.cos(-0.04) * 104 - 16.5)
    ra = math.radians(ang)
    ox, oy = lx * s * math.cos(ra) - ly * s * math.sin(ra), lx * s * math.sin(ra) + ly * s * math.cos(ra)
    return mao(c, px - ox, py - oy, s, gesto, ang, **kw)


# =====================================================================
# MÓVEIS E OBJETOS
# =====================================================================
MADEIRA = dict(base="#b8693a", sombra="#8a4b2f", escuro="#6a3520", brilho="#e09a62")


def mesa(c, x0, x1, ytopo, ychao, a=1.0, esp=34, perna=26):
    """mesa de madeira vista de frente: tampo de x0 a x1 com o topo em ytopo, pés no chão em ychao"""
    M = MADEIRA
    if a < 1:
        c.saveLayerAlpha(None, int(255 * clamp(a)))
    for lx in (x0 + 34, x1 - 34 - perna):
        c.drawOval(oval(lx + perna / 2, ychao, perna * 1.3, 6), paint(INK, 0.3, blur=4))
        pe = skia.Path()
        pe.addRRect(rr(lx, ytopo + esp - 6, perna, ychao - ytopo - esp + 6, 6))
        volume(c, pe, M["sombra"], sh=(lx + perna, (ytopo + ychao) / 2, perna * 0.45, ychao - ytopo))
    c.drawRect(skia.Rect.MakeLTRB(x0 + 20, ytopo + esp, x1 - 20, ytopo + esp + 14), paint(INK, 0.25, blur=6))
    tp = skia.Path()
    tp.addRRect(rr(x0, ytopo, x1 - x0, esp, 10))
    volume(c, tp, M["base"])
    c.save()
    c.clipPath(tp, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeLTRB(x0, ytopo + esp * 0.45, x1, ytopo + esp), paint(M["sombra"]))
    c.drawRect(skia.Rect.MakeLTRB(x0, ytopo, x1, ytopo + 5), paint(M["brilho"], 0.8))
    for k in range(3):                       # veios da madeira
        yy = ytopo + esp * (0.62 + k * 0.12)
        c.drawLine(x0 + 30 + k * 90, yy, x0 + (x1 - x0) * (0.35 + 0.2 * k), yy, paint(M["escuro"], 0.35, stroke=2))
    c.restore()
    if a < 1:
        c.restore()


def caixa_madeira(c, x, y, w, h, tampa_h=None, a=1.0, aberta=0.0):
    """caixa/gaveta de madeira (x, y = canto de cima do corpo); a tampa fica por cima; aberta 0..1 levanta a tampa"""
    M = MADEIRA
    th = tampa_h or max(18, h * 0.16)
    if a < 1:
        c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.drawOval(oval(x + w / 2, y + h, w * 0.55, 10), paint(INK, 0.3, blur=6))
    corpo = skia.Path()
    corpo.addRRect(rr(x, y, w, h, 14))
    volume(c, corpo, M["sombra"], sh=(x + w, y + h / 2, w * 0.18, h), hl=(x + w * 0.15, y + h * 0.3, w * 0.05, h * 0.3),
           k_sh=0.2, hl_a=0.3)
    c.save()
    c.clipPath(corpo, doAntiAlias=True)
    for k in range(1, 3):                    # tábuas
        yy = y + h * k / 3
        c.drawLine(x, yy, x + w, yy, paint(M["escuro"], 0.55, stroke=3))
    c.restore()
    c.drawRRect(rr(x + w / 2 - 26, y + h * 0.42, 52, 14, 7), paint(M["escuro"]))      # puxador
    c.drawRRect(rr(x + w / 2 - 22, y + h * 0.42, 44, 5, 3), paint(M["brilho"], 0.5))
    c.save()
    c.translate(x + w, y)
    c.rotate(-50 * aberta)
    tp = skia.Path()
    tp.addRRect(rr(-w - 14, -th, w + 28, th, th / 2))
    volume(c, tp, M["base"], hl=(-w * 0.55, -th * 0.75, w * 0.4, th * 0.18), hl_a=0.55)
    c.restore()
    if a < 1:
        c.restore()


def olho(c, x, y, s=1.0, a=1.0, look=0.0, blink=0.0):
    """olho amendoado no estilo do olho da Lume (íris, pupila, dois reflexos, pálpebra com cílios)"""
    if a <= 0:
        return
    if a < 1:
        c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    am = skia.Path()
    am.moveTo(-38, 0)
    am.cubicTo(-22, -28, 22, -28, 38, 0)
    am.cubicTo(22, 26, -22, 26, -38, 0)
    am.close()
    c.drawPath(am, paint(INK, 0.25, blur=4))
    c.drawPath(am, paint(BONE))
    c.save()
    c.clipPath(am, doAntiAlias=True)
    c.drawOval(oval(0, -16, 44, 14), paint("#d9d2c4", 0.8))
    ix = look * 12
    c.drawCircle(ix, 0, 16, paint("#2b8fd6"))
    c.drawCircle(ix, 0, 16, paint(CYAN, 0.6, stroke=2.4))
    c.drawCircle(ix, 0, 8, paint("#0b1622"))
    c.drawCircle(ix - 6, -6, 4.6, paint(CLARO, 0.95))
    c.drawCircle(ix + 5, 5, 2, paint(CLARO, 0.6))
    if blink > 0.01:
        c.drawRect(skia.Rect.MakeLTRB(-40, -30, 40, -26 + 52 * blink), paint("#f2d0b8"))
    c.restore()
    tp = skia.Path()
    yb = -20 + 40 * blink
    tp.moveTo(-40, 0)
    tp.cubicTo(-22, yb - 8, 22, yb - 8, 40, 0)
    c.drawPath(tp, paint(INK, stroke=4))
    for k in (-1, 0, 1):
        bx = k * 16
        c.drawLine(bx, yb - 6 - abs(k) * 1, bx + k * 6, yb - 16, paint(INK, stroke=3))
    c.restore()
    if a < 1:
        c.restore()


def estrela(c, x, y, r, cor, a=1.0, pontas=5):
    pts = []
    for k in range(pontas * 2):
        an = -math.pi / 2 + k * math.pi / pontas
        rr_ = r if k % 2 == 0 else r * 0.45
        pts.append((x + math.cos(an) * rr_, y + math.sin(an) * rr_))
    pth = poly(pts)
    c.drawPath(pth, paint(cor, a))
    c.save()
    c.clipPath(pth, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeLTRB(x, y - r, x + r, y + r), paint(sombra(cor, 0.18), a))
    c.restore()


def raio(c, x, y, s, cor, a=1.0):
    c.drawPath(poly([(x + 6 * s, y - 40 * s), (x - 18 * s, y + 4 * s), (x - 2 * s, y + 4 * s), (x - 8 * s, y + 40 * s),
                     (x + 18 * s, y - 6 * s), (x + 2 * s, y - 6 * s)]), paint(cor, a))


def coracao(c, cx, cy, r, cor=CORAL, a=1.0):
    p = skia.Path()
    p.moveTo(cx, cy + r)
    p.cubicTo(cx - r * 1.6, cy - r * 0.2, cx - r * 0.8, cy - r * 1.4, cx, cy - r * 0.5)
    p.cubicTo(cx + r * 0.8, cy - r * 1.4, cx + r * 1.6, cy - r * 0.2, cx, cy + r)
    c.drawPath(p, paint(cor, a))
    c.save()
    c.clipPath(p, doAntiAlias=True)
    c.drawOval(oval(cx + r * 0.7, cy + r * 0.4, r * 0.9, r * 0.9), paint(sombra(cor, 0.2), a))
    c.drawOval(oval(cx - r * 0.55, cy - r * 0.55, r * 0.28, r * 0.2), paint(CLARO, 0.55 * a))
    c.restore()


def simbolo(c, k, x, y, size, cor):
    k %= 5
    if k == 0:
        text(c, "7", x, y + size * 0.36, size, "display", 800, cor, 1, "center")
    elif k == 1:
        estrela(c, x, y, size * 0.45, cor)
    elif k == 2:
        lz = poly([(x, y - size * 0.45), (x + size * 0.33, y), (x, y + size * 0.45), (x - size * 0.33, y)])
        c.drawPath(lz, paint(cor))
        c.drawPath(poly([(x, y - size * 0.45), (x + size * 0.33, y), (x, y + size * 0.45)]), paint(sombra(cor, 0.18)))
    elif k == 3:
        b = skia.Path()
        b.addCircle(x, y, size * 0.32)
        volume(c, b, cor, sh=(x + size * 0.2, y + size * 0.2, size * 0.3, size * 0.3),
               hl=(x - size * 0.12, y - size * 0.14, size * 0.08, size * 0.05), hl_a=0.7)
    else:
        coracao(c, x, y, size * 0.28, cor)


def moeda(c, x, y, s=1.0, a=1.0):
    c.drawCircle(x + 2 * s, y + 3 * s, 22 * s, paint(INK, 0.25 * a))
    c.drawCircle(x, y, 22 * s, paint("#d18d12", a))
    c.drawCircle(x, y, 17 * s, paint(AMBER, a))
    c.drawArc(oval(x, y, 13 * s, 13 * s), 200, 70, False, paint(CLARO, 0.7 * a, stroke=3 * s))
    text(c, "$", x, y + 9 * s, 26 * s, "display", 800, "#a8700e", a, "center")


def sino(c, x, y, s=1.0, cor=AMBER, a=1.0, ang=0.0, riscado=False):
    """sino de notificação com volume; riscado = silenciado"""
    c.save()
    c.translate(x, y)
    c.rotate(ang)
    c.scale(s, s)
    if a < 1:
        c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.drawCircle(0, -48, 7, paint(sombra(cor, 0.25), stroke=4))
    badalo = skia.Path()
    badalo.addCircle(0 + 4 * math.sin(math.radians(-ang)), 32, 9)
    volume(c, badalo, sombra(cor, 0.15), hl=(-3, 29, 3, 2), hl_a=0.7)
    p = skia.Path()
    p.moveTo(-36, 20)
    p.cubicTo(-30, -10, -32, -42, 0, -44)
    p.cubicTo(32, -42, 30, -10, 36, 20)
    p.close()
    volume(c, p, cor, sh=(30, 0, 22, 40), hl=(-14, -26, 6, 12), hl_a=0.7)
    aba = skia.Path()
    aba.addRRect(rr(-42, 14, 84, 12, 6))
    volume(c, aba, sombra(cor, 0.1), hl=(-10, 16, 26, 2), hl_a=0.5)
    if a < 1:
        c.restore()
    c.restore()
    if riscado:
        c.drawLine(x - 50 * s, y - 50 * s, x + 50 * s, y + 50 * s, paint(BONE, a, stroke=16 * s))
        c.drawLine(x - 50 * s, y - 50 * s, x + 50 * s, y + 50 * s, paint(CORAL, a, stroke=10 * s))


def ampulheta(c, cx, cy, s, cheio, a=1.0):
    M = MADEIRA
    c.save()
    c.translate(cx, cy)
    c.scale(s, s)
    if a < 1:
        c.saveLayerAlpha(None, int(255 * clamp(a)))
    for yy in (-170, 146):
        tb = skia.Path()
        tb.addRRect(rr(-110, yy, 220, 24, 8))
        volume(c, tb, M["base"], sh=(0, yy + 24, 120, 10), hl=(-40, yy + 4, 50, 3), hl_a=0.6)
    for xx in (-100, 92):
        c.drawRRect(rr(xx, -146, 8, 292, 4), paint(M["sombra"]))
    vidro = poly([(-90, -146), (90, -146), (14, 0), (90, 146), (-90, 146), (-14, 0)])
    c.drawPath(vidro, paint("#d6f1fa", 0.35))
    c.save()
    c.clipPath(vidro, doAntiAlias=True)
    topo = -146 + (1 - cheio) * 140
    c.drawRect(skia.Rect.MakeLTRB(-90, topo, 90, 0), paint(AMBER))
    c.drawRect(skia.Rect.MakeLTRB(-90, 146 - (1 - cheio) * 120, 90, 146), paint(AMBER))
    c.drawRect(skia.Rect.MakeLTRB(30, -146, 90, 146), paint("#c98a10", 0.35))
    if 0.02 < cheio < 0.98:
        c.drawRect(skia.Rect.MakeLTRB(-3, 0, 3, 146), paint(AMBER, 0.8))
    c.drawPath(poly([(-70, -140), (-52, -140), (-10, -10), (-20, -10)]), paint(CLARO, 0.45))
    c.restore()
    c.drawPath(vidro, paint("#ffffff", 0.8, stroke=4))
    if a < 1:
        c.restore()
    c.restore()


def caca_niquel(c, cx, cy, t, a=1.0):
    """máquina caça-níquel com rolos girando, letreiro de lâmpadas piscando e alavanca cromada"""
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.drawOval(oval(cx, cy + 268, 330, 18), paint(INK, 0.3, blur=8))
    corpo = skia.Path()
    corpo.addRRect(rr(cx - 300, cy - 260, 600, 520, 40))
    volume(c, corpo, CORAL, sh=(cx + 330, cy, 90, 300), hl=(cx - 250, cy, 14, 200), k_sh=0.22, hl_a=0.3)
    let = skia.Path()
    let.addRRect(rr(cx - 300, cy - 260, 600, 120, 40))
    volume(c, let, "#ff8fa0", hl=(cx - 120, cy - 240, 200, 10), hl_a=0.5)
    for k in range(14):                      # lâmpadas do letreiro
        on = (int(t * 6) + k) % 2 == 0
        bx = cx - 260 + k * 40
        c.drawCircle(bx, cy - 150, 7, paint(AMBER if on else "#ffd9a8"))
        if on:
            glow(c, bx, cy - 150, 18, AMBER, 0.5)
    text(c, "777", cx, cy - 175, 60, "display", 800, AMBER, 1, "center")
    c.drawRRect(rr(cx - 250, cy - 112, 500, 224, 22), paint(sombra(CORAL, 0.35)))
    for k in range(3):
        x0 = cx - 230 + k * 160
        c.drawRRect(rr(x0, cy - 100, 140, 200, 16), paint("#ffffff"))
        c.save()
        c.clipRRect(rr(x0, cy - 100, 140, 200, 16), doAntiAlias=True)
        off = (t * (9 + k * 2) * 100) % 100
        for i in range(-1, 3):
            sk = int(t * (9 + k * 2)) + i + k
            simbolo(c, sk, x0 + 70, cy + i * 100 - off - 30, 80, FESTA_[sk % 5])
        c.drawRect(skia.Rect.MakeXYWH(x0, cy - 100, 140, 40), linear(0, cy - 100, 0, cy - 60, [(INK, 0.35), (INK, 0)]))
        c.drawRect(skia.Rect.MakeXYWH(x0, cy + 60, 140, 40), linear(0, cy + 60, 0, cy + 100, [(INK, 0), (INK, 0.35)]))
        c.restore()
    c.drawRRect(rr(cx - 200, cy + 150, 400, 60, 18), paint(sombra(CORAL, 0.4)))         # bandeja
    c.drawRRect(rr(cx - 190, cy + 150, 380, 14, 7), paint(INK, 0.3))
    # alavanca cromada
    ky = cy - 210 + 60 * (0.5 + 0.5 * math.sin(t * 5))
    c.drawRRect(rr(cx + 296, cy - 40, 30, 70, 10), paint("#8a93c8"))
    hst = capsula(cx + 313, cy - 10, cx + 313, ky, 10)
    volume(c, hst, "#c9cfe6", sh=(cx + 322, (cy + ky) / 2, 6, 200), hl=(cx + 308, (cy + ky) / 2, 2, 200), hl_a=0.8)
    bola = skia.Path()
    bola.addCircle(cx + 313, ky, 30)
    volume(c, bola, AMBER, sh=(cx + 330, ky + 16, 26, 22), hl=(cx + 302, ky - 12, 9, 6), hl_a=0.8)
    c.restore()


FESTA_ = [PINK, SKY, AMBER, CYAN, CORAL]
