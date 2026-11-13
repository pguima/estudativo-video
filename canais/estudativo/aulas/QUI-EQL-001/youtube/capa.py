"""Capas da QUI-EQL-001 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


NOMES = ("capa_A_nada_para_nada_muda", "capa_B_equilibrio_e_kc", "capa_C_produtos_sobre_reagentes")


def a(c):  # o gancho: nada para, nada muda
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "nada para,", 84, 420, 190, "g", BR)
    E.escreve(c, "nada muda", 84, 630, 190, "g", AMARELO)
    Q.formula(c, "N2O4 <=> 2 NO2", 84, 830, 120, BR)
    E.escreve(c, "o equilíbrio dinâmico", 84, 1000, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Equilíbrio", "e Kc", "do zero")


def d(c):  # o macete: produtos sobre reagentes, sem sólido
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "qualquer K em 3 regras", 84, 320, 110, "i", BR)
    for k, s in enumerate(("produtos sobre reagentes", "coeficiente vira expoente", "sólido e líquido fora")):
        E.escreve(c, s, 84, 520 + k * 170, 110, "g", claro if k == 2 else BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
