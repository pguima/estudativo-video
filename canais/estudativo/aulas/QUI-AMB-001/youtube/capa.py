"""Capas da QUI-AMB-001 (1280x720). Uso: python capa.py"""
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
_s = importlib.util.spec_from_file_location("visual_aula", Path(__file__).parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)


def a(c):  # o gancho: o etanol solta CO₂ e é renovável
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "etanol solta CO₂", 84, 360, 110, "b", BR)
    E.escreve(c, "e mesmo assim", 84, 540, 130, "i", BR)
    E.escreve(c, "é renovável", 84, 760, 180, "g", AMARELO)
    E.escreve(c, "fóssil × biocombustível", 84, 960, 80, "i", BR)
    V.cana(c, 1500, 960, 520, cor="#E8FBF7")
    Q.molecula_desenho(c, "CO2", 1520, 260, 130)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Gasolina", "ou etanol?", "do zero")


def d(c):  # o macete: mais oxigênio, menos energia
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "qual rende mais?", 84, 330, 110, "i", BR)
    E.escreve(c, "mais oxigênio,", 76, 520, 150, "g", BR)
    E.escreve(c, "menos energia", 76, 690, 150, "g", claro)
    for k, (nome, v) in enumerate((("gasolina", 48), ("biodiesel", 40), ("etanol", 30))):
        y = 820 + 80 * k
        E.escreve(c, nome, 84, y + 40, 50, "b", BR)
        M.rrect(c, 380, y, 14 * v, 50, 25, claro if k else "#9AA0A8", 1)
        E.escreve(c, f"{v} kJ/g", 400 + 14 * v, y + 40, 46, "g", BR)
    Q.formula(c, "C2H6O", 1250, 560, 180, BR, cores={"O": claro}, escuro=True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_etanol_e_renovavel", a), ("capa_B_gasolina_ou_etanol", b), ("capa_C_mais_oxigenio_menos_energia", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
