"""Capas da QUI-ELE-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: quem perde e quem ganha
    base(c)
    Q.formula(c, "Zn + Cu^2+ -> Zn^2+ + Cu", 84, 380, 140, BR)
    E.escreve(c, "quem se oxida?", 84, 640, 150, "g", BR)
    E.escreve(c, "quem se reduz?", 84, 820, 150, "g", AMARELO)
    E.escreve(c, "e quem são os agentes", 84, 980, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Oxirredução", "e agentes", "do zero")


def d(c):  # o macete: os nomes se cruzam
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "os nomes se cruzam", 84, 300, 120, "i", BR)
    E.escreve(c, "Nox sobe", 84, 540, 150, "g", BR)
    E.escreve(c, "= redutor", 900, 540, 150, "g", "#FFB347")
    E.escreve(c, "Nox desce", 84, 760, 150, "g", BR)
    E.escreve(c, "= oxidante", 900, 760, 150, "g", "#7FB2FF")
    E.escreve(c, "o atalho de prova", 84, 960, 80, "i", claro)


salvar((("capa_A_quem_perde_quem_ganha", a), ("capa_B_oxirreducao", b), ("capa_C_os_nomes_se_cruzam", d)))
