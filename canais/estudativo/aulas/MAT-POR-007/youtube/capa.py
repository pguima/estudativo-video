"""Capas do MAT-POR-007 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def a(c):  # o gancho: o mesmo lucro, duas porcentagens
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "comprei por 80", 84, 360, 120, "i", BR)
    E.escreve(c, "vendi por 100", 84, 490, 120, "i", BR)
    x = 84 + E.larg("25%", "g", 240) + 40
    E.escreve(c, "25%", 84, 800, 240, "g", AMARELO)
    E.escreve(c, "ou", x, 780, 120, "i", BR)
    E.escreve(c, "20%?", x + E.larg("ou", "i", 120) + 40, 800, 240, "g", BR)
    E.escreve(c, "de lucro", 90, 980, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Lucro", "sobre o custo", "ou sobre a venda")


def d(c):  # o atalho: pense em partes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    CL = E.mix(COR, BR, 0.55)
    E.escreve(c, "o atalho das partes", 84, 330, 120, "i", BR)
    for i in range(5):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(84 + i * 230, 420, 210, 170), 22, 22)
        c.drawRRect(r, M.paint(BR if i == 4 else CL))
    E.escreve(c, "custo 4", 84, 700, 90, "i", CL)
    E.escreve(c, "lucro 1", 950, 700, 90, "i", BR)
    E.escreve(c, "1/4 = 25%", 84, 900, 150, "g", CL)
    E.escreve(c, "1/5 = 20%", 900, 900, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_25_ou_20", a), ("capa_B_custo_ou_venda", b), ("capa_C_partes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
