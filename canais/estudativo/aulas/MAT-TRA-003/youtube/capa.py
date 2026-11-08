"""Capas do MAT-TRA-003 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
AGUA = "#7FD0FF"


def a(c):  # o gancho: o lago
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "senos ou", 84, 400, 150, "g", BR)
    E.escreve(c, "cossenos?", 84, 570, 150, "g", AMARELO)
    E.escreve(c, "a distância do outro", 84, 760, 90, "i", BR)
    E.escreve(c, "lado do lago", 84, 860, 90, "i", BR)
    k = 6.2
    Cc = (1430, 960)
    A = (Cc[0] - 80 * k * 0.5, Cc[1] - 80 * k * math.sqrt(3) / 2)
    B = (Cc[0] + 50 * k * 0.5, Cc[1] - 50 * k * math.sqrt(3) / 2)
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    ang = math.degrees(math.atan2(B[1] - A[1], B[0] - A[0]))
    L = math.dist(A, B)
    c.save(); c.translate(mx, my - 40); c.rotate(ang)
    p = skia.Path(); p.addOval(skia.Rect.MakeXYWH(-L * 0.42, -110, L * 0.84, 200))
    c.drawPath(p, M.paint(AGUA, 0.45)); c.restore()
    M.line(c, *Cc, *A, BR, 1.0, 10); M.line(c, *Cc, *B, BR, 1.0, 10)
    M.line(c, *A, *B, AMARELO, 1.0, 10, dash=[24, 16])
    for P in (A, B, Cc):
        c.drawCircle(*P, 18, M.paint(BR))
    E.escreve(c, "80 m", A[0] - 120, (A[1] + Cc[1]) / 2 + 40, 70, "g", BR)
    E.escreve(c, "50 m", (B[0] + Cc[0]) / 2 + 40, (B[1] + Cc[1]) / 2 + 20, 70, "g", BR)
    E.escreve(c, "60°", Cc[0] - 50, Cc[1] - 90, 60, "g", AMARELO)
    E.escreve(c, "?", mx - 20, my - 60, 110, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Senos ou", "cossenos?", "qual lei usar")


def d(c):  # o atalho: obtuso só pelos lados
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "tem ângulo obtuso?", 84, 360, 120, "i", BR)
    E.formula(c, "4, 5, 7:", 84, 600, 150, "g", BR)
    E.formula(c, "7^2 > 4^2 + 5^2", 760, 600, 150, "g", AMARELO)
    E.escreve(c, "49 > 41: obtusângulo", 84, 860, 130, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_lago", a), ("capa_B_qual_lei", b), ("capa_C_obtuso_pelos_lados", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
