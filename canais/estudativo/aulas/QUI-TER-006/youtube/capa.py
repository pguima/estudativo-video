"""Capas da QUI-TER-006 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


NOMES = ("capa_A_o_morro_da_reacao", "capa_B_energia_de_ativacao", "capa_C_catalisador_so_o_topo")


def morro(c, x0, y0, w, h, alto, cor, largura=14, dash=False):
    import math as _m
    pts = [(x0 + k * w / 100, y0 - alto * _m.exp(-((k - 50) / 16) ** 2) - (0 if k < 50 else h * (k - 50) / 50 * 0)) for k in range(101)]
    pth = skia.Path(); pth.moveTo(*pts[0])
    for p in pts[1:]:
        pth.lineTo(*p)
    pt = M.paint(cor, 1, stroke=largura, cap_round=True)
    if dash:
        pt.setPathEffect(skia.DashPathEffect.Make([30, 22], 0))
    c.drawPath(pth, pt)


def a(c):  # o gancho: o empurrão do fósforo
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "o papel não queima", 84, 360, 110, "i", BR)
    E.escreve(c, "sozinho.", 84, 560, 190, "g", BR)
    E.escreve(c, "por quê?", 84, 780, 190, "g", AMARELO)
    morro(c, 1080, 820, 760, 0, 420, BR)
    E.bola(c, 1150, 780, 40, AMARELO)
    E.escreve(c, "a subida de toda reação", 84, 990, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Energia", "de ativação", "e catalisador")


def d(c):  # o macete: o catalisador só abaixa o topo
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "catalisador:", 84, 330, 120, "i", BR)
    E.escreve(c, "só abaixa", 84, 520, 150, "g", BR)
    E.escreve(c, "o topo", 84, 690, 150, "g", claro)
    E.formula(c, "ΔH não muda", 84, 900, 100, "g", BR)
    morro(c, 1100, 800, 720, 0, 460, BR, 12)
    morro(c, 1100, 800, 720, 0, 240, claro, 10, dash=True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
