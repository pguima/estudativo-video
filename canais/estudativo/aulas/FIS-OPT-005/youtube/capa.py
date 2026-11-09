"""Capas do FIS-OPT-005 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a luz", 84, 400, 170, "g", BR)
    E.escreve(c, "fica presa", 84, 580, 170, "g", AMARELO)
    E.escreve(c, "reflexão total e fibra óptica", 84, 780, 80, "i", BR)
    pts = [(1180, 900), (1350, 780), (1500, 620), (1650, 460), (1820, 380)]
    p = M.paint("#FFFFFF", 0.35, stroke=110, cap_round=True)
    pa = skia.Path(); pa.moveTo(*pts[0])
    for P in pts[1:]:
        pa.lineTo(*P)
    c.drawPath(pa, p)
    zz = [(1180, 900), (1290, 790), (1330, 860), (1430, 680), (1500, 720), (1580, 520), (1640, 560), (1740, 380), (1820, 380)]
    pz = skia.Path(); pz.moveTo(*zz[0])
    for P in zz[1:]:
        pz.lineTo(*P)
    c.drawPath(pz, M.paint(AMARELO, 1.0, stroke=10))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Reflexão", "total", "dispersão e cor")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "ângulo limite:", 84, 330, 120, "i", BR)
    E.formula(c, "sen L = f{menor}{maior}", 84, 620, 170, "g", BR)
    E.escreve(c, "deu mais que 1? inverteu", 84, 900, 84, "g", claro)
    E.orbita(c, 1640, 300, 170, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_luz_presa_no_vidro", a), ("capa_B_reflexao_total_e_cor", b), ("capa_C_seno_do_limite", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
