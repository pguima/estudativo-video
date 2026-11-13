"""Capas da QUI-SOL-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5 questões de prova
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "5 questões", 84, 420, 180, "g", BR)
    E.escreve(c, "de soluções", 84, 600, 130, "i", BR)
    E.escreve(c, "você acerta?", 84, 860, 150, "g", AMARELO)
    V.garrafa(c, 1350, 950, 260, 560, "4%")
    Q.erlenmeyer(c, 10, 0, 1700, 950, 300, 320, 0.4, V.ROSA)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Soluções:", "praticando", "5 questões")


def d(c):  # o ângulo do erro: 0,5 + 1 = 1,5?
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o erro que derruba", 84, 330, 100, "i", BR)
    E.formula(c, "0,5 + 0,1 = 0,6?", 84, 560, 150, "g", V.ERRADO)
    E.risco(c, 70, 590, 1180, 440, 9, 0, V.ERRADO, 26)
    E.escreve(c, "some os mols", 84, 800, 140, "g", claro)
    for x, n, nv in ((1300, 20, 0.5), (1650, 6, 0.7)):
        Q.bequer(c, 10, 0, x, 900, 260, 340, nv, Q.AGUA, graduacao=False, escuro=True, particulas=dict(n=n, estado="gas", tipos=[(COR, 1.0)], r=9))


salvar((("capa_A_cinco_questoes", a), ("capa_B_praticando_solucoes", b), ("capa_C_some_os_mols", d)))
