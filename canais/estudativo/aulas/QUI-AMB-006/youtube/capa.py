"""Capas da QUI-AMB-006 (1280x720). Uso: python capa.py"""
import importlib.util
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


def a(c):  # o gancho: 100% de rendimento e quase metade no lixo
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "rendimento 100%", 84, 360, 120, "b", BR)
    E.escreve(c, "e 44% vai", 84, 560, 180, "g", BR)
    E.escreve(c, "para o lixo", 84, 760, 180, "g", AMARELO)
    E.escreve(c, "a conta da economia atômica", 84, 960, 80, "i", BR)
    M.rrect(c, 1200, 400, 620, 110, 55, "#E8FBF7", 0.35)
    M.rrect(c, 1200, 400, 620 * 0.56, 110, 55, BR, 1)
    E.escreve(c, "56%", 1240, 478, 70, "g", COR)
    E.escreve(c, "44% CO₂", 1580, 478, 56, "g", BR)
    Q.formula(c, "CaCO3 -> CaO + CO2", 1510, 720, 66, BR, align="center")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Química", "verde", "do zero")


def d(c):  # o macete: um produto só = 100%
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "economia atômica sem conta:", 84, 330, 96, "i", BR)
    E.escreve(c, "um produto só", 76, 530, 160, "g", BR)
    E.escreve(c, "= 100%", 76, 720, 190, "g", claro)
    Q.formula(c, "N2 + 3 H2 -> 2 NH3", 84, 930, 100, BR, escuro=True, cores={"NH3": claro})


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_44_para_o_lixo", a), ("capa_B_quimica_verde", b), ("capa_C_um_produto_so", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
