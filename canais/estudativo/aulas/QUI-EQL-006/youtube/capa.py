"""Capas da QUI-EQL-006 (1280x720). Uso: python capa.py"""
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


NOMES = ("capa_A_quem_segura_o_ph", "capa_B_solucao_tampao", "capa_C_ph_igual_pka")


def a(c):  # o gancho: quem segura o pH do sangue
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "seu sangue:", 84, 340, 110, "i", BR)
    E.formula(c, "pH 7,4", 84, 590, 240, "g", AMARELO)
    E.escreve(c, "quem segura?", 84, 800, 160, "g", BR)
    E.escreve(c, "a solução tampão", 84, 990, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Solução", "tampão", "do zero")


def d(c):  # o macete: pH = pKa
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete", 84, 320, 120, "i", BR)
    E.escreve(c, "ácido = sal", 84, 560, 170, "g", BR)
    E.formula(c, "pH = pKa", 84, 800, 200, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
