"""Capas da QUI-SOL-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 40 g e 58,5 g, o mesmo 1 mol
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "40 g", 84, 420, 200, "g", BR)
    E.escreve(c, "=", 560, 420, 200, "g", AMARELO)
    E.escreve(c, "58,5 g?", 84, 620, 200, "g", BR)
    E.escreve(c, "em mol, sim:", 84, 790, 110, "i", BR)
    E.escreve(c, "1 mol cada", 84, 960, 150, "g", AMARELO)
    for x, f in ((1330, "NaOH"), (1680, "NaCl")):
        Q.bequer(c, 10, 0, x, 900, 260, 300, 0.75, Q.AGUA, graduacao=False, particulas=dict(n=22, estado="liquido", tipos=[(COR, 1.0)], r=9))
        Q.formula(c, f, x, 1010, 80, BR, 1.0, "center")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Mol por", "litro", "do zero")


def d(c):  # o macete: g/L ÷ massa molar
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "uma divisão só", 84, 330, 110, "i", BR)
    E.pilula(c, "g/L", 300, 560, 120, "g", fundo="#3A3B42")
    E.pilula(c, "mol/L", 1120, 560, 120, "g", fundo=COR)
    M.arrow(c, 500, 560, 880, 560, claro, 1, 10, 34)
    E.centro(c, "÷ massa molar", 690, 480, 64, "b", BR)
    E.escreve(c, "20 g/L ÷ 40 = 0,5 mol/L", 84, 860, 90, "g", claro)


salvar((("capa_A_um_mol_cada", a), ("capa_B_mol_por_litro", b), ("capa_C_uma_divisao", d)))
