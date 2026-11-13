"""Capas da QUI-ATO-011 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: quem entrega o elétron?
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "sódio ou cloro:", 84, 380, 130, "g", BR)
    E.escreve(c, "quem entrega?", 84, 560, 150, "g", AMARELO)
    E.escreve(c, "ionização e eletronegatividade", 84, 720, 70, "i", BR)
    Q.atomo(c, 1420, 700, 150, "Na")
    Q.atomo(c, 1770, 700, 115, "Cl")
    E.bola(c, 1600, 500, 30, Q.ELETRON)
    M.arrow(c, 1480, 560, 1700, 560, AMARELO, 1, 10, 30)


def b(c):
    E.capa_modelo(c, "Química", "Energia de", "ionização", "e eletronegatividade")


def d(c):  # o macete: a frase da fila
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "Fui Ontem No Clube", 84, 400, 140, "g", BR)
    E.escreve(c, "Briguei, I Saí Correndo Para o Hospital", 84, 540, 74, "i", claro)
    for k, el in enumerate(("F", "O", "N", "Cl", "Br", "I", "S", "C", "P", "H")):
        M.rrect(c, 84 + k * 175, 680, 150, 150, 20, COR if k < 4 else "#2A2B33", 1)
        E.centro(c, el, 84 + k * 175 + 75, 785, 80, "g", BR, 1)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quem_entrega_o_eletron", a), ("capa_B_ionizacao_eletronegatividade", b), ("capa_C_fui_ontem_no_clube", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
