"""Capas do MAT-FIN-012 (1280x720). Uso: python capa.py"""
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



def a(c):  # o gancho: mesmo empréstimo, mesma taxa, juros diferentes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "R$ 10.000 · 2% · 10 meses", 84, 360, 100, "g", BR)
    E.escreve(c, "qual cobra mais juros?", 84, 480, 90, "i", BR)
    E.escreve(c, "SAC", 84, 760, 190, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "R$ 1.100", 84, 900, 120, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "Price", 1000, 760, 190, "g", AMARELO)
    E.escreve(c, "≈ R$ 1.130", 1000, 900, 120, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Tabelas", "SAC e Price", "o financiamento")


def d(c):  # o atalho da SAC
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho da SAC", 84, 320, 110, "i", BR)
    E.escreve(c, "cada prestação:", 84, 500, 110, "i", BR)
    E.escreve(c, "R$ 20 a menos", 84, 690, 170, "g", AMARELO)
    E.escreve(c, "1.200 → 1.180 → 1.160…", 84, 900, 110, "g", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_cobra_mais", a), ("capa_B_sac_e_price", b), ("capa_C_atalho_sac", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
