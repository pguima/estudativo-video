"""Capas da QUI-TER-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: quebrar gasta, mas a queima libera
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "quebrar gasta", 84, 360, 130, "i", BR)
    E.escreve(c, "formar", 84, 590, 200, "g", BR)
    E.escreve(c, "libera", 84, 800, 200, "g", AMARELO)
    Q.molecula_desenho(c, "H2", 1450, 420, 200, separa=0.5)
    Q.molecula_desenho(c, "H2O", 1450, 780, 200)
    E.escreve(c, "o delta H pelas ligações", 84, 990, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Energia", "de ligação", "do zero")


def d(c):  # o macete: só as ligações que mudam
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete", 84, 320, 120, "i", BR)
    E.escreve(c, "conte só o", 76, 520, 140, "g", BR)
    E.escreve(c, "que muda", 76, 680, 140, "g", claro)
    E.formula(c, "ΔH = quebrar − formar", 84, 900, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quebrar_gasta_formar_libera", a), ("capa_B_energia_de_ligacao", b), ("capa_C_so_o_que_muda", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
