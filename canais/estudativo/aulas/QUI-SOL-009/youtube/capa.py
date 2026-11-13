"""Capas da QUI-SOL-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: mesma concentração, congela em tempos diferentes
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "mesmo 0,1 mol/L", 84, 380, 120, "g", BR)
    E.escreve(c, "e um congela", 84, 560, 120, "i", BR)
    E.escreve(c, "por último", 84, 760, 190, "g", AMARELO)
    E.escreve(c, "por quê?", 84, 940, 110, "i", BR)
    for k, f in enumerate(("açúcar", "NaCl", "CaCl2")):
        V.unidade(c, 10, 0, f, 1420, 380 + k * 230, 46, abre=0)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Crioscopia", "e partículas", "do zero")


def d(c):  # o macete: concentração × partículas
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete das partículas", 84, 330, 100, "i", BR)
    E.formula(c, "0,1 × 3", 84, 580, 200, "g", BR)
    E.formula(c, "= 0,3", 84, 790, 200, "g", claro)
    V.unidade(c, 10, 0, "CaCl2", 1480, 620, 64, abre=0)
    Q.formula(c, "CaCl2", 1480, 860, 90, BR, align="center", escuro=True)


salvar((("capa_A_congela_por_ultimo", a), ("capa_B_crioscopia", b), ("capa_C_vezes_tres", d)))
