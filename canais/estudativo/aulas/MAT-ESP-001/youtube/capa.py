"""Capas do MAT-ESP-001 (1280x720). Uso: python capa.py"""
import itertools, math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
E.usar("Matemática", "Geometria Espacial")


def na_face(c, O, U, V, fn):
    m = skia.Matrix.MakeAll(U[0] - O[0], V[0] - O[0], O[0], U[1] - O[1], V[1] - O[1], O[1], 0, 0, 1)
    c.save(); c.concat(m); fn(); c.restore()


def dado(c, x, y, a):
    """o dado em linhas brancas, com as pintas"""
    pts = E.cubo(c, 99, 0, x, y, a, escuro=True, cor=BR, preenche=0.12, largura=9)
    tinta = M.paint(BR)
    pintas = {1: ((0.5, 0.5),), 3: ((0.25, 0.25), (0.5, 0.5), (0.75, 0.75)),
              5: ((0.25, 0.25), (0.75, 0.25), (0.5, 0.5), (0.25, 0.75), (0.75, 0.75))}
    for (O, U, V), n in (((pts[3], pts[2], pts[0]), 5), ((pts[7], pts[6], pts[3]), 1), ((pts[2], pts[6], pts[1]), 3)):
        na_face(c, O, U, V, lambda n=n: [c.drawOval(skia.Rect.MakeXYWH(u - 0.075, v - 0.075, 0.15, 0.15), tinta) for u, v in pintas[n]])
    return pts


def icosaedro(c, cx, cy, r):
    f = (1 + 5 ** 0.5) / 2
    V = []
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            V += [(0, s1, s2 * f), (s1, s2 * f, 0), (s2 * f, 0, s1)]
    k = r / math.sqrt(1 + f * f)
    V = [(x * k, y * k, z * k) for x, y, z in V]
    F = [tri for tri in itertools.combinations(range(12), 3)
         if all(abs(math.dist(V[i], V[j]) - 2 * k) < 1e-6 for i, j in itertools.combinations(tri, 2))]
    E._solido(c, 99, 0, V, F, E._vista_alta(-18, 14), cx, cy, preenche=0.18, escuro=True, largura=7)


def a(c):  # o gancho: quantas dobras tem o dado?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    pts = dado(c, 130, 930, 480)
    M.line(c, *pts[3], *pts[2], AMARELO, 1, 16)
    E.escreve(c, "6 faces", 1000, 380, 130, "g", BR)
    E.escreve(c, "8 pontas", 1000, 560, 130, "g", BR)
    E.escreve(c, "? dobras", 1000, 760, 150, "g", AMARELO)
    E.escreve(c, "sem contar", 1010, 940, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Poliedros", "e Euler", "do zero")


def d(c):  # o atalho: Euler
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a conta dos", 84, 370, 110, "i", BR)
    E.escreve(c, "poliedros", 84, 500, 110, "i", BR)
    E.escreve(c, "V − A + F = 2", 76, 780, 170, "g", AMARELO)
    icosaedro(c, 1530, 470, 300)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobras_do_dado", a), ("capa_B_poliedros_e_euler", b), ("capa_C_relacao_de_euler", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
