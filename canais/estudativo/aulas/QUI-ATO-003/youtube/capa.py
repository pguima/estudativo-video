"""Capas da QUI-ATO-003 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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
LUZ = dict(Sr="#E8352E", Ba="#3DBE4C", Na="#F7C81E", Cu="#1FB5A5")


def fogos(c, cx, cy, r, cor, n=18):
    for k in range(n):
        g = math.tau * k / n + 0.2
        M.line(c, cx + r * 0.5 * math.cos(g), cy + r * 0.5 * math.sin(g), cx + r * math.cos(g), cy + r * math.sin(g), cor, 1, 9)
        c.drawCircle(cx + r * math.cos(g), cy + r * math.sin(g), 11, M.paint(cor))
    c.drawCircle(cx, cy, r * 0.18, M.paint(BR, 0.9))


def atomo(c, cx, cy, tinta=BR, luz=None):
    for r in (90, 160, 230):
        c.drawCircle(cx, cy, r, M.paint(tinta, 0.8, stroke=5))
    E.bola(c, cx, cy, 44, AMARELO if tinta == BR else COR)
    E.bola(c, cx + 230 * math.cos(-0.6), cy + 230 * math.sin(-0.6), 24, Q.ELETRON)
    if luz:
        x0, y0 = cx + 120, cy - 230
        pth = skia.Path()
        for k in range(90):
            s = k * 5
            pth.moveTo(x0 + s, y0 - s * 0.55 + 18 * math.sin(s / 40 * math.tau)) if k == 0 else pth.lineTo(x0 + s, y0 - s * 0.55 + 18 * math.sin(s / 40 * math.tau))
        c.drawPath(pth, M.paint(luz, 1, stroke=9, cap_round=True))


def a(c):  # o gancho: de onde vem a cor dos fogos
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "a cor dos fogos", 84, 380, 120, "i", BR)
    E.escreve(c, "vem do", 84, 560, 190, "g", BR)
    E.escreve(c, "elétron", 84, 760, 190, "g", AMARELO)
    fogos(c, 1500, 330, 190, LUZ["Sr"])
    fogos(c, 1700, 720, 170, LUZ["Na"])
    fogos(c, 1260, 800, 150, LUZ["Ba"])


def b(c):
    E.capa_modelo(c, "Química", "Bohr:", "saltos", "e cores do zero")


def d(c):  # o macete: sobe, volta, solta luz
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "sobe,", 84, 400, 150, "g", BR)
    E.escreve(c, "volta,", 84, 580, 150, "g", BR)
    E.escreve(c, "solta luz", 84, 760, 150, "g", AMARELO)
    E.escreve(c, "a resposta é Bohr", 84, 940, 80, "i", claro)
    atomo(c, 1500, 620, BR, LUZ["Na"])


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_cor_vem_do_eletron", a), ("capa_B_bohr_saltos_e_cores", b), ("capa_C_sobe_volta_solta_luz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
