"""Capas da QUI-INO-007 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def a(c):  # o gancho: a massa não some
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "12 g + 32 g", 84, 420, 150, "g", BR)
    E.escreve(c, "= ?", 84, 600, 150, "g", AMARELO)
    E.escreve(c, "a massa", 84, 820, 130, "i", BR)
    E.escreve(c, "não some", 84, 970, 130, "g", BR)
    Q.molecula_desenho(c, "CO2", 1480, 520, 170)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Equação", "química", "do zero")


def d(c):  # o macete: reagentes = produtos
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "massa antes", 84, 360, 120, "i", BR)
    E.escreve(c, "= massa depois", 84, 540, 150, "g", BR)
    Q.formula(c, "C + O2 -> CO2", 84, 790, 150, BR, escuro=True)
    E.formula(c, "12 + 32 = 44", 84, 990, 110, "g", claro)
    E.balanca(c, 1480, 560, "12 + 32", "44", 0, 1, 80, 560, cor=COR, escuro=True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_massa_nao_some", a), ("capa_B_equacao_quimica", b), ("capa_C_antes_igual_depois", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
