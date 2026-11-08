"""Capas do MAT-TOP-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 50 + 33 não é 83
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "múltiplos de 2 ou de 3, de 1 a 100", 84, 300, 80, "i", BR)
    E.escreve(c, "50 + 33 = 83", 84, 560, 200, "g", BR)
    E.risco(c, 60, 600, 1300, 380, 9, 0, AMARELO, 30)
    E.escreve(c, "são", 84, 860, 130, "i", BR)
    E.escreve(c, "67", 330, 900, 260, "g", AMARELO)
    E.escreve(c, "por quê?", 900, 860, 130, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Inclusão", "e exclusão", "sem contar 2 vezes")


def d(c):  # o atalho: repete a cada MMC
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 360, 140, "i", BR)
    E.escreve(c, "repete a cada 6", 76, 570, 190, "g", BR)
    for i in range(1, 7):
        ok = i % 2 == 0 or i % 3 == 0
        x = 90 + (i - 1) * 190
        M.rrect(c, x, 700, 170, 170, 26, AMARELO if ok else "#2A2A33", 1)
        E.centro(c, str(i), x + 85, 820, 110, "g", COR if ok else BR)
    E.escreve(c, "4 em 6", 1300, 830, 140, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_83", a), ("capa_B_inclusao_exclusao", b), ("capa_C_repete_a_cada_mmc", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
