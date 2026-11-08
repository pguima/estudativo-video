"""Capas do MAT-POT-012 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: a conta certa na forma errada
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "45 × 10^3", 84, 520, 270, "g", BR)
    E.selo(c, 1560, 400, 130, False)
    E.escreve(c, "conta certa,", 84, 760, 130, "i", BR)
    E.escreve(c, "forma errada", 84, 960, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Escrever", "em notação", "científica")


def d(c):  # o atalho: conte os algarismos depois do primeiro
    escuro(c)
    E.escreve(c, "45.000.000", 84, 410, 220, "g", BR)
    E.escreve(c, "conte depois", 84, 590, 150, "i", BR)
    E.escreve(c, "do primeiro", 84, 750, 150, "i", BR)
    E.formula(c, "4,5 × 10^7", 84, 980, 200, "g", AMARELO)


NOMES = (("capa_A_forma_errada", a), ("capa_B_escrever_em_notacao", b), ("capa_C_atalho_dos_algarismos", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in NOMES:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()

