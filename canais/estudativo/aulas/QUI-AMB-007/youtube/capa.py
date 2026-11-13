"""Capas da QUI-AMB-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: etanol, emissão zero? Não
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "carro a etanol:", 84, 360, 110, "i", BR)
    E.escreve(c, "emissão zero?", 84, 560, 170, "g", BR)
    E.risco(c, 70, 590, 1150, 420, 10, 0, AMARELO, 30)
    E.escreve(c, "4 armadilhas de prova", 84, 800, 120, "g", AMARELO)
    E.escreve(c, "energia, poluição e água", 84, 970, 80, "i", BR)
    Q.molecula_desenho(c, "C2H6O", 1560, 400, 150)
    Q.molecula_desenho(c, "CO2", 1560, 760, 130)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Química e", "ambiente", "4 questões")


def d(c):  # o macete: renovável não é emissão zero
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a lição que mais cai:", 84, 330, 100, "i", BR)
    E.escreve(c, "renovável", 76, 530, 170, "g", claro)
    E.escreve(c, "≠ emissão zero", 76, 720, 150, "g", BR)
    for k, s in enumerate(("+ enxofre vira chuva ácida", "+ água quente também asfixia")):
        E.escreve(c, s, 84, 870 + 90 * k, 56, "b", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_emissao_zero", a), ("capa_B_quimica_e_ambiente", b), ("capa_C_renovavel_nao_e_zero", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
