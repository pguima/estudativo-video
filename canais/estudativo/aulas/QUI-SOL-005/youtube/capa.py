"""Capas da QUI-SOL-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: só água, a concentração cai para um quinto
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "só água", 84, 380, 150, "i", BR)
    E.formula(c, "0,5 → 0,1", 84, 620, 200, "g", BR)
    E.escreve(c, "mol/L", 84, 760, 110, "g", AMARELO)
    E.escreve(c, "numa linha", 84, 930, 120, "i", BR)
    for x, n, nv in ((1250, 16, 0.2), (1640, 16, 0.85)):
        Q.bequer(c, 10, 0, x, 920, 300, 520, nv, Q.AGUA, graduacao=False, particulas=dict(n=n, estado="gas", tipos=[(COR, 1.0)], r=10, semente=5))
    M.arrow(c, 1420, 640, 1470, 640, BR, 1, 8, 28)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Diluição", "e mistura", "do zero")


def d(c):  # o macete: C₁V₁ = C₂V₂
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a fórmula de uma linha", 84, 330, 100, "i", BR)
    E.formula(c, "C₁V₁ = C₂V₂", 84, 580, 210, "g", BR)
    E.formula(c, "volume × 5 → concentração ÷ 5", 84, 800, 80, "g", claro)


salvar((("capa_A_so_agua", a), ("capa_B_diluicao_mistura", b), ("capa_C_c1v1_c2v2", d)))
