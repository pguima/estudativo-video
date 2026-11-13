"""Capas da QUI-INO-009 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: chama azul x amarela
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "chama amarela", 84, 400, 140, "g", AMARELO)
    E.escreve(c, "solta um gás", 84, 570, 140, "g", BR)
    E.escreve(c, "que mata", 84, 740, 140, "g", BR)
    Q.formula(c, "CO", 84, 960, 140, BR)
    Q.molecula_desenho(c, "CO", 1500, 560, 260)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Síntese,", "análise", "e combustão")


def d(c):  # o macete: conte as substâncias
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "conte as substâncias", 84, 340, 100, "i", BR)
    E.escreve(c, "várias → 1: síntese", 84, 560, 110, "g", BR)
    E.escreve(c, "1 → várias: análise", 84, 740, 110, "g", claro)
    E.escreve(c, "+ O₂ e calor: combustão", 84, 920, 90, "g", BR)


CAPAS = (("capa_A_chama_amarela", a), ("capa_B_sintese_analise_combustao", b), ("capa_C_conte_as_substancias", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
