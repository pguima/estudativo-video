"""Capas do MAT-FIN-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5 situações de dinheiro, resolva antes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5", 84, 560, 420, "g", AMARELO)
    E.escreve(c, "situações de dinheiro", 380, 300, 92, "g", BR)
    E.escreve(c, "empréstimo, aplicação,", 380, 410, 66, "i", BR)
    E.escreve(c, "conta atrasada", 380, 490, 66, "i", BR)
    E.escreve(c, "pause e resolva!", 84, 860, 150, "g", E.mix(COR, BR, 0.55))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando:", "juros", "simples e compostos")


def d(c):  # o atalho para dobrar
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "para dobrar, a 8% ao mês", 84, 330, 96, "i", BR)
    E.escreve(c, "simples: 100 ÷ 8 = 12,5", 84, 560, 120, "g", BR)
    E.escreve(c, "compostos: 72 ÷ 8 ≈ 9", 84, 740, 120, "g", AMARELO)
    E.escreve(c, "meses para dobrar", 84, 900, 90, "i", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_5_situacoes", a), ("capa_B_praticando_juros", b), ("capa_C_dobrar_100_72", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
