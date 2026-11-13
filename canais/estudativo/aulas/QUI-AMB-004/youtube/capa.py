"""Capas da QUI-AMB-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: do rio barrento à torneira
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "do rio barrento", 84, 360, 120, "i", BR)
    E.escreve(c, "à torneira", 84, 560, 180, "g", BR)
    E.escreve(c, "em 6 etapas", 84, 760, 160, "g", AMARELO)
    E.escreve(c, "a química de cada uma", 84, 960, 80, "i", BR)
    V.tanque(c, 0, 1060, 300, 360, 300, junta=0.0)
    M.arrow(c, 1440, 450, 1560, 450, BR, 1, 10, 30)
    Q.bequer(c, 10, 0, 1720, 620, 260, 300, 0.7, Q.AGUA, graduacao=False)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Tratamento", "de água", "do zero")


def d(c):  # o macete: juntar, tirar, proteger
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a ordem em 3 verbos", 84, 330, 110, "i", BR)
    E.escreve(c, "juntar,", 76, 520, 160, "g", claro)
    E.escreve(c, "tirar,", 76, 690, 160, "g", BR)
    E.escreve(c, "proteger", 76, 860, 160, "g", "#6FA8FF")
    for k, nome in enumerate(V.ETAPAS):
        y = 280 + 110 * k
        E.bola(c, 1250, y, 34, V.COR_G[V.GRUPO[nome]] if V.GRUPO[nome] != "tirar" else "#5B6470")
        E.centro(c, str(k + 1), 1250, y + 16, 40, "g", BR, 1)
        E.escreve(c, nome, 1310, y + 18, 54, "b", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_rio_a_torneira", a), ("capa_B_tratamento_de_agua", b), ("capa_C_juntar_tirar_proteger", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
