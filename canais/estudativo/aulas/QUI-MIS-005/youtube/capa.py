"""Capas da QUI-MIS-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: O₂ + O₃ é substância pura? É mistura
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "só oxigênio:", 84, 340, 120, "i", BR)
    E.escreve(c, "é pura?", 84, 540, 190, "g", BR)
    E.risco(c, 70, 570, 760, 400, 10, 0, AMARELO, 30)
    E.escreve(c, "é mistura", 84, 780, 190, "g", AMARELO)
    E.escreve(c, "4 pegadinhas de prova", 84, 980, 80, "i", BR)
    for k, (m, x, y, g) in enumerate((("O2", 1300, 330, 20), ("O3", 1600, 420, 0), ("O2", 1350, 650, 110), ("O3", 1640, 760, 200))):
        Q.molecula_desenho(c, m, x, y, 120, 1, giro=g)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Misturas", "na prática", "4 questões")


def d(c):  # o macete: gelo é água
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "água, sal, gelo e óleo:", 84, 330, 100, "i", BR)
    E.escreve(c, "3 fases", 76, 540, 190, "g", BR)
    E.escreve(c, "3 componentes", 76, 740, 150, "g", claro)
    E.escreve(c, "gelo é água", 84, 920, 90, "i", BR)
    V.copo_camadas(c, 10, 0, 1500, 980, 440, 640, [(Q.AGUA, 0.5, None), (V.OLEO, 0.18, None)])
    for dx, g in ((-90, 10), (60, -14)):
        V.gelo(c, 1500 + dx, 980 - 640 * 0.5 + 10, 100, g)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_so_oxigenio_e_mistura", a), ("capa_B_misturas_na_pratica", b), ("capa_C_gelo_e_agua", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
