"""Capas da QUI-TER-007 (1280x720). Uso: python capa.py"""
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


NOMES = ("capa_A_dobrou_quadruplicou", "capa_B_lei_da_velocidade", "capa_C_fator_elevado_a_ordem")


def a(c):  # o gancho: dobrou e quadruplicou
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "dobrou o reagente", 84, 350, 110, "i", BR)
    E.formula(c, "v × 4", 84, 620, 260, "g", AMARELO)
    E.escreve(c, "por quê?", 84, 830, 150, "g", BR)
    Q.formula(c, "v = k · [A]^{2}", 1080, 560, 150, BR, cores={"carga": AMARELO})
    E.escreve(c, "a ordem de reação", 84, 990, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Lei da", "velocidade", "e ordem de reação")


def d(c):  # o macete: fator elevado à ordem
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete", 84, 320, 120, "i", BR)
    E.formula(c, "× 2 → v × 4", 84, 540, 150, "g", BR)
    E.formula(c, "2^2: ordem 2", 84, 740, 150, "g", claro)
    E.formula(c, "fator^{ordem}", 84, 940, 100, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
