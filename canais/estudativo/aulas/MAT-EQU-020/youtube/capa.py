"""Capas do MAT-EQU-020 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def carro(c, cx, cy, s, cor, fundo):
    M.rrect(c, cx - s * 0.25, cy - s * 0.4, s * 0.5, s * 0.3, s * 0.1, cor)
    M.rrect(c, cx - s * 0.5, cy - s * 0.18, s, s * 0.3, s * 0.1, cor)
    for dx in (-0.28, 0.28):
        c.drawCircle(cx + s * dx, cy + s * 0.13, s * 0.14, M.paint(fundo))
        c.drawCircle(cx + s * dx, cy + s * 0.13, s * 0.1, M.paint(cor))


def moto(c, cx, cy, s, cor):
    for dx in (-0.32, 0.32):
        c.drawCircle(cx + s * dx, cy + s * 0.1, s * 0.17, M.paint(cor, stroke=max(3, s * 0.07)))
        c.drawCircle(cx + s * dx, cy + s * 0.1, s * 0.05, M.paint(cor))
    p = skia.Path()
    p.moveTo(cx - s * 0.36, cy - s * 0.1); p.lineTo(cx - s * 0.12, cy - s * 0.2); p.lineTo(cx + s * 0.16, cy - s * 0.2)
    p.lineTo(cx + s * 0.2, cy - s * 0.04); p.lineTo(cx + s * 0.02, cy + s * 0.12); p.lineTo(cx - s * 0.14, cy + s * 0.12); p.close()
    c.drawPath(p, M.paint(cor))
    M.line(c, cx + s * 0.16, cy - s * 0.3, cx + s * 0.32, cy + s * 0.1, cor, 1, s * 0.07)
    M.line(c, cx + s * 0.08, cy - s * 0.32, cx + s * 0.24, cy - s * 0.32, cor, 1, s * 0.07)


def a(c):  # o gancho: 30 veículos e 100 rodas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "30 veículos", 84, 400, 190, "g", BR)
    E.escreve(c, "100 rodas", 84, 620, 190, "g", BR)
    E.escreve(c, "quantos carros?", 84, 900, 170, "i", AMARELO)
    carro(c, 1500, 330, 300, BR, COR)
    moto(c, 1560, 620, 300, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Montar", "o sistema", "do problema")


def d(c):  # o atalho: suponha que todos são motos
    palco(c)
    E.escreve(c, "suponha: todos motos", 84, 360, 130, "i", BR)
    E.escreve(c, "20 carros", 84, 650, 260, "g", AMARELO)
    E.escreve(c, "sem letra nenhuma", 84, 900, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_30_veiculos", a), ("capa_B_montar_sistema", b), ("capa_C_todos_motos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
