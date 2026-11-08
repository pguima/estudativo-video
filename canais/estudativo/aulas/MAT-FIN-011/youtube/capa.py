"""Capas do MAT-FIN-011 (1280x720). Uso: python capa.py"""
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



def a(c):  # o gancho: parece 5% a mais, mas são 10% ao mês
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "R$ 200 à vista", 84, 380, 150, "g", BR)
    E.escreve(c, "ou R$ 100 + R$ 110", 84, 540, 120, "i", BR)
    E.escreve(c, "só 5% a mais?", 84, 780, 150, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 810, 1080, 660, 9, 0, AMARELO, 30)
    E.escreve(c, "10%", 1180, 820, 220, "g", AMARELO)
    E.escreve(c, "ao mês", 1250, 960, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "À vista", "ou a prazo?", "os juros escondidos")


def d(c):  # o atalho: parcela ÷ saldo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 320, 120, "i", BR)
    E.escreve(c, "parcela ÷ saldo", 84, 540, 170, "g", BR)
    E.escreve(c, "110 ÷ 100 = 1,1", 84, 760, 140, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "= 10% ao mês", 84, 940, 150, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_juros_escondidos", a), ("capa_B_a_vista_ou_a_prazo", b), ("capa_C_parcela_saldo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
