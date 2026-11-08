"""Capas do MAT-LEI-006 (1280x720). Uso: python capa.py"""
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


def garrafa(c, cx, base, h, rot, cor):
    w = h * 0.42
    p = skia.Path()
    p.moveTo(cx - w / 2, base - h * 0.62)
    p.cubicTo(cx - w / 2, base - h * 0.8, cx - w * 0.18, base - h * 0.8, cx - w * 0.18, base - h * 0.9)
    p.lineTo(cx + w * 0.18, base - h * 0.9)
    p.cubicTo(cx + w * 0.18, base - h * 0.8, cx + w / 2, base - h * 0.8, cx + w / 2, base - h * 0.62)
    p.lineTo(cx + w / 2, base)
    p.lineTo(cx - w / 2, base)
    p.close()
    c.drawPath(p, M.paint(BR))
    M.rrect(c, cx - w * 0.22, base - h, w * 0.44, h * 0.1, 6, cor)
    M.rrect(c, cx - w / 2, base - h * 0.5, w, h * 0.26, 4, cor)
    E.centro(c, rot, cx, base - h * 0.31, h * 0.12, "g", COR if cor != COR else BR)


def a(c):  # o gancho: a etiqueta menor engana
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    garrafa(c, 330, 860, 470, "1,5 L", E.mix(COR, BR, 0.55))
    garrafa(c, 820, 860, 560, "2 L", AMARELO)
    E.centro(c, "R$ 5,40", 330, 980, 90, "g", BR)
    E.centro(c, "R$ 7,00", 820, 980, 90, "g", AMARELO)
    E.escreve(c, "qual sai", 1120, 420, 150, "i", BR)
    E.escreve(c, "mais", 1120, 600, 190, "g", BR)
    E.escreve(c, "barato?", 1120, 780, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "A melhor", "compra", "preço por litro")


def d(c):  # o atalho: o máximo de pacotes da embalagem mais barata
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "comece pelo", 84, 360, 140, "i", BR)
    E.escreve(c, "máximo", 76, 600, 240, "g", BR)
    E.escreve(c, "3 de 6 = 18", 84, 850, 120, "g", "#E5484D")
    E.escreve(c, "→ 2 de 6 + 1 de 4", 720, 850, 120, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_sai_mais_barato", a), ("capa_B_a_melhor_compra", b), ("capa_C_comece_pelo_maximo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
