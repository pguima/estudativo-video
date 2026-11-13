"""Capas da QUI-SOL-006 (1280x720). Uso: python capa.py"""
import importlib.util, subprocess, sys
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
_s = importlib.util.spec_from_file_location("v", Path(__file__).parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)
E.usar("Química")


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def salvar(capas):
    pasta = Path(__file__).parent
    s = skia.Surface(E.W, E.H)
    for nome, fn in capas:
        fn(s.getCanvas())
        tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
        tmp.unlink()


def a(c):  # o gancho: a gota que fica rosa
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "uma gota", 84, 400, 170, "g", BR)
    E.escreve(c, "e a cor", 84, 560, 130, "i", BR)
    E.escreve(c, "conta a", 84, 700, 130, "i", BR)
    E.escreve(c, "resposta", 84, 880, 170, "g", AMARELO)
    V.montagem(c, 10, 0, 1480, 90, tv=0, nivel_b=0.6, rot=False, h=380)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Titulação", "do zero", "sem decorar")


def d(c):  # o macete: H · M · V = OH · M · V
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "conte os H e os OH", 84, 330, 100, "i", BR)
    E.formula(c, "H · M · V", 84, 560, 170, "g", claro)
    E.formula(c, "= OH · M · V", 84, 760, 170, "g", BR)
    Q.formula(c, "H2SO4 + 2 NaOH", 84, 950, 90, BR, cores={"coef": claro}, escuro=True)
    V.montagem(c, 10, 0, 1500, 110, tv=0, nivel_b=0.6, rot=False, h=380)


salvar((("capa_A_uma_gota", a), ("capa_B_titulacao", b), ("capa_C_conte_h_e_oh", d)))
