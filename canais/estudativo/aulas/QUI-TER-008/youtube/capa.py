"""Capas da QUI-TER-008 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


NOMES = ("capa_A_cinco_questoes", "capa_B_praticando_energia_velocidade", "capa_C_caixa_de_ferramentas")


def a(c):  # o gancho: cinco questões, uma por ferramenta
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "5 questões", 84, 420, 200, "g", BR)
    E.escreve(c, "de prova", 84, 610, 170, "g", AMARELO)
    E.escreve(c, "ΔH, Hess, ligações, velocidade e ordem", 84, 820, 70, "b", BR)
    E.escreve(c, "você consegue?", 84, 990, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Energia e", "velocidade", "praticando")


def d(c):  # o macete: a caixa de ferramentas
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a caixa de ferramentas", 84, 320, 110, "i", BR)
    for k, s in enumerate(("ΔH = chegada − partida", "Ea = topo − reagentes", "v = Δ[ ] / Δt")):
        E.formula(c, s, 84, 520 + k * 170, 110, "g", claro if k == 1 else BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
