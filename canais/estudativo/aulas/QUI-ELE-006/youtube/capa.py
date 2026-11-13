"""Capas da QUI-ELE-006 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def base(c):
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)


def salvar(capas):
    pasta = Path(__file__).parent
    s = skia.Surface(E.W, E.H)
    for nome, fn in capas:
        fn(s.getCanvas())
        tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
        tmp.unlink()


def navio(c, cx, cy, w):
    h = w * 0.28
    p = skia.Path()
    p.moveTo(cx - w / 2, cy - h * 0.3); p.lineTo(cx + w / 2, cy - h * 0.3); p.lineTo(cx + w * 0.38, cy + h * 0.6)
    p.lineTo(cx - w * 0.42, cy + h * 0.6); p.close()
    c.drawPath(p, M.paint("#3D4350"))
    M.rrect(c, cx - w * 0.3, cy - h * 0.8, w * 0.42, h * 0.5, 10, "#E8E8E2", 1)
    M.rrect(c, cx - w * 0.6, cy + h * 0.15, w * 1.2, h * 0.9, 0, "#9CCBE8", 0.55)
    for k in range(4):
        M.rrect(c, cx - w * 0.3 + k * w * 0.18 - w * 0.04, cy + h * 0.5, w * 0.08, h * 0.18, 4, AMARELO, 1)


def a(c):  # o gancho: por que o zinco se gasta no lugar do ferro
    base(c)
    navio(c, 1400, 560, 760)
    E.escreve(c, "o zinco", 84, 440, 150, "g", AMARELO)
    E.escreve(c, "se sacrifica", 84, 610, 150, "g", BR)
    E.escreve(c, "pelo navio", 84, 780, 150, "g", BR)
    E.escreve(c, "corrosão e proteção dos metais", 84, 950, 70, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Ferrugem", "e proteção", "dos metais")


def d(c):  # o macete: abaixo do ferro
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete do sacrifício", 84, 300, 110, "i", BR)
    E.escreve(c, "abaixo do ferro", 84, 520, 150, "g", BR)
    E.escreve(c, "na escada", 84, 700, 130, "g", claro)
    Q.formula(c, "Fe^2+/Fe", 84, 920, 110, BR, escuro=True); E.escreve(c, "−0,44 V", 620, 920, 110, "g", AMARELO)


salvar((("capa_A_o_zinco_se_sacrifica", a), ("capa_B_ferrugem_e_protecao", b), ("capa_C_abaixo_do_ferro", d)))
