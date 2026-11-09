"""Capas do FIS-MAG-010 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def painel(c, cx, cy, w, h):
    p = skia.Path()
    p.moveTo(cx - w / 2, cy + h / 2); p.lineTo(cx + w / 2, cy + h / 2); p.lineTo(cx + w / 2 - w * 0.12, cy - h / 2); p.lineTo(cx - w / 2 + w * 0.12, cy - h / 2); p.close()
    c.drawPath(p, M.paint("#22416E")); c.drawPath(p, M.paint(BR, 1, stroke=6))


def a(c):  # o gancho: o painel não gera à noite
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "à noite, o", 84, 380, 140, "i", BR)
    E.escreve(c, "painel solar", 84, 590, 170, "g", BR)
    E.escreve(c, "gera zero", 84, 790, 190, "g", AMARELO)
    c.drawCircle(1480, 300, 110, M.paint("#F4F1EA"))
    c.drawCircle(1540, 270, 100, M.paint(COR))
    painel(c, 1460, 640, 560, 240)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Vento e sol:", "rendimento", "e intermitência")


def d(c):  # o macete: duas perguntas
    palco_capa(c)
    E.escreve(c, "2 perguntas", 84, 340, 150, "g", BR)
    E.escreve(c, "gira um gerador?", 84, 540, 110, "b", E.mix(COR, BR, 0.5))
    E.escreve(c, "liga quando eu quero?", 84, 700, 110, "b", E.mix(COR, BR, 0.5))
    E.escreve(c, "e cada fonte se encaixa", 84, 880, 90, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_painel_a_noite", a), ("capa_B_vento_e_sol", b), ("capa_C_duas_perguntas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
