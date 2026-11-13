"""Capas da QUI-AMB-005 (1280x720). Uso: python capa.py"""
import importlib.util
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")
_s = importlib.util.spec_from_file_location("visual_aula", Path(__file__).parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)


def a(c):  # o gancho: rio cheio de comida, peixes sem ar
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "rio cheio de comida", 84, 360, 110, "i", BR)
    E.escreve(c, "e os peixes", 84, 550, 160, "g", BR)
    E.escreve(c, "sem ar", 84, 750, 190, "g", AMARELO)
    E.escreve(c, "o que a DBO denuncia", 84, 960, 80, "i", BR)
    V.rio(c, 1080, 360, 740, 480, 0.6)
    V.peixe(c, 1300, 520, 80, 1, 0.0)
    V.peixe(c, 1600, 700, 70, 1, 0.0)
    V.cano(c, 0, 1300, 330, 1, 0)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Esgoto", "e DBO", "do zero")


def d(c):  # o macete: DBO alta, OD baixo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "nunca mais confunda:", 84, 330, 100, "i", BR)
    E.escreve(c, "DBO alta,", 76, 530, 170, "g", claro)
    E.escreve(c, "OD baixo", 76, 720, 170, "g", BR)
    for k, (rot, v, cor) in enumerate((("DBO", 0.9, claro), ("OD", 0.15, BR))):
        x = 1300 + 260 * k
        M.rrect(c, x, 300, 140, 560, 30, "#1F2030", 1)
        M.rrect(c, x, 300 + 560 * (1 - v), 140, 560 * v, 30, cor, 1)
        E.centro(c, rot, x + 70, 940, 64, "g", BR, 1)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_peixes_sem_ar", a), ("capa_B_esgoto_e_dbo", b), ("capa_C_dbo_alta_od_baixo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
