"""Capas da QUI-MIS-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o filtro não tira o sal
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "água do mar no filtro", 84, 360, 110, "i", BR)
    E.escreve(c, "tira o sal?", 84, 560, 180, "g", BR)
    E.escreve(c, "não!", 84, 780, 200, "g", AMARELO)
    E.escreve(c, "decantar, filtrar e centrifugar", 84, 980, 74, "i", BR)
    V.filtro(c, 10, 0, 1480, 280, tp=None)
    V.copo(c, 10, 0, 1480, 990, 300, 300, 0.5, "#9FD3E6")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Decantar", "e filtrar", "do zero")


def d(c):  # o macete: sai o mais denso
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "no funil, quem sai primeiro?", 84, 330, 96, "i", BR)
    E.escreve(c, "o mais", 76, 530, 180, "g", BR)
    E.escreve(c, "denso", 76, 720, 180, "g", claro)
    E.escreve(c, "nem sempre é a água", 84, 900, 80, "i", BR)
    V.funil_sep(c, 10, 0, 1500, 240, V.DENSO, Q.AGUA, 0.3)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_filtro_nao_tira_o_sal", a), ("capa_B_decantar_e_filtrar", b), ("capa_C_sai_o_mais_denso", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
