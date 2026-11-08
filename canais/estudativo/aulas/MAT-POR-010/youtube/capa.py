"""Capas do MAT-POR-010 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 10% + 20% não dá 30%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "+10% e +20%", 84, 400, 170, "g", BR)
    E.escreve(c, "30%", 84, 690, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 720, 520, 520, 9, 0, AMARELO, 30)
    E.escreve(c, "32%", 640, 690, 230, "g", AMARELO)
    E.escreve(c, "porcentagens seguidas não se somam", 84, 960, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Aumentos", "seguidos", "e descontos sucessivos")


def d(c):  # o atalho: a + b + a × b ÷ 100
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    CL = E.mix(COR, BR, 0.55)
    E.escreve(c, "o atalho", 84, 330, 130, "i", BR)
    E.escreve(c, "a + b + a×b÷100", 76, 560, 170, "g", BR)
    E.escreve(c, "10 + 20 + 2 = 32%", 84, 830, 140, "g", CL)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_30", a), ("capa_B_sucessivos", b), ("capa_C_atalho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
