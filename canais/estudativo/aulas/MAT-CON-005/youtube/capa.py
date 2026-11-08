"""Capas do MAT-CON-005 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def a(c):  # o gancho: 0,444… não é 4/10, é 4/9
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "0,444…", 84, 470, 250, "g", BR)
    E.escreve(c, "que fração é essa?", 84, 640, 100, "i", BR)
    E.formula(c, "f{4}{10}", 120, 900, 150, "g", BR)
    E.risco(c, 90, 960, 330, 740, 9, 0, AMARELO, 26)
    E.bola(c, 1560, 640, 260, AMARELO)
    E.fracao(c, 4, 9, 1560, 625, 220, COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Fração", "geratriz", "sem decorar")


def d(c):  # o macete dos noves
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o macete", 84, 380, 130, "i", BR)
    E.escreve(c, "dos noves", 76, 600, 210, "g", BR)
    E.formula(c, "0,1212… = f{12}{99}", 84, 900, 150, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_que_fracao_e_essa", a), ("capa_B_fracao_geratriz", b), ("capa_C_macete_dos_noves", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
