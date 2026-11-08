"""Capas do MAT-TOP-018 (1280x720). Uso: python capa.py"""
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


def a(c):  # quatro situações
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "4", 84, 560, 380, "g", AMARELO)
    E.escreve(c, "situações", 370, 430, 120, "i", BR)
    E.escreve(c, "para revisar", 370, 580, 115, "g", BR)
    E.escreve(c, "pause e resolva", 84, 860, 110, "i", BR)
    for i, s in enumerate(("11010₂ = ?", "1,2 × 3,456", "tronco?", "área × k²")):
        y = 260 + i * 190
        M.rrect(c, 1180, y - 100, 620, 140, 28, BR, 0.14)
        E.escreve(c, s, 1220, y, 84, "g", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Praticando", "troncos", "e homotetia")


def d(c):  # o macete: 1 − k³
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o tronco numa", 84, 380, 140, "i", BR)
    E.escreve(c, "conta só", 84, 560, 170, "g", BR)
    E.formula(c, "1 − k^3", 84, 860, 220, "g", "#3CC7D3")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quatro_situacoes", a), ("capa_B_praticando", b), ("capa_C_um_menos_k_ao_cubo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
