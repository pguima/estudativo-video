"""Capas do MAT-DIV-007 (1280x720). Uso: python capa.py"""
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


def onibus(c, x, y, w, cor):
    """ônibus de perfil, claro sobre a cor da matéria"""
    h = w * 0.42
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - h, w, h * 0.82), w * 0.06, w * 0.06), M.paint(cor))
    for i in range(4):
        M.rrect(c, x + w * 0.05 + i * w * 0.23, y - h * 0.88, w * 0.17, h * 0.3, w * 0.02, COR)
    for dx in (0.22, 0.78):
        c.drawCircle(x + w * dx, y - h * 0.14, w * 0.075, M.paint("#07070F"))


def a(c):  # o gancho: quando saem juntos de novo?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    onibus(c, 84, 420, 400, BR)
    E.escreve(c, "a cada 12 min", 540, 385, 150, "g", BR)
    onibus(c, 84, 640, 400, BR)
    E.escreve(c, "a cada 18 min", 540, 605, 150, "g", BR)
    E.escreve(c, "quando saem", 84, 785, 130, "i", BR)
    E.escreve(c, "juntos de novo?", 84, 980, 180, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Problemas", "de MMC", "encontros")


def d(c):  # o atalho: a pista no texto
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "reparte ou repete?", 84, 350, 150, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a cada", 84, 520, 120, "g", claro)
    E.escreve(c, "ao mesmo tempo", 84, 660, 120, "g", claro)
    E.escreve(c, "juntos de novo", 84, 800, 120, "g", claro)
    E.escreve(c, "= MMC", 1130, 660, 180, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_juntos_de_novo", a), ("capa_B_problemas_de_mmc", b), ("capa_C_pista_no_texto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
