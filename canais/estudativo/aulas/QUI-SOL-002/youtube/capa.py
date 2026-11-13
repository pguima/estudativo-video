"""Capas da QUI-SOL-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 14 g que não somem
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "mexa quanto", 84, 380, 130, "i", BR)
    E.escreve(c, "quiser:", 84, 520, 130, "i", BR)
    E.escreve(c, "14 g", 84, 790, 260, "g", AMARELO)
    E.escreve(c, "ficam no fundo", 84, 960, 100, "i", BR)
    Q.bequer(c, 10, 0, 1440, 920, 480, 560, 0.72, Q.AGUA, graduacao=False)
    V.dissolvido(c, 10, 0, 1440, 920, 480, 560, 90)
    V.fundo_sal(c, 10, 0, 1440, 920, 480, 48, 13)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Curva de", "solubilidade", "do zero")


def d(c):  # o macete: o ponto no gráfico
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "abaixo, sobre", 84, 330, 120, "g", BR)
    E.escreve(c, "ou acima?", 84, 470, 120, "g", claro)
    E.escreve(c, "a curva responde", 84, 620, 90, "i", BR)
    P = Q.solubilidade(c, 10, 0, 1060, 260, 700, 600, [dict(nome="", pts=V.KNO3)], tmax=80, smax=180, d=0.1, escuro=True, passo=20, passo_y=40, size=30)
    for (x, y), cor in (((40, 40), "#7FC8F8"), ((40, 64), claro), ((40, 110), V.ERRADO)):
        c.drawCircle(P.x(x), P.y(y), 22, M.paint(cor)); c.drawCircle(P.x(x), P.y(y), 22, M.paint(BR, 1, stroke=4))


salvar((("capa_A_14g_no_fundo", a), ("capa_B_curva_de_solubilidade", b), ("capa_C_abaixo_ou_acima", d)))
