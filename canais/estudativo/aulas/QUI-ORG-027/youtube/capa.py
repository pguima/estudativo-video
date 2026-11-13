"""Capas da QUI-ORG-027 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "roteiro"))
import skia
import editorial as E
import quimica as Q
import motor as M
import visual as V  # as peças de estrutura da aula, desenhadas paradas (t0 = None)
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
CLARO = E.mix(COR, BR, 0.5)


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def claro(c):
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)


def a(c):  # o gancho: pão, cabelo e pneu são polímeros
    claro(c)
    E.escreve(c, "pão, cabelo", 84, 380, 160, "g", BR)
    E.escreve(c, "e pneu", 84, 570, 170, "g", AMARELO)
    E.escreve(c, "também são polímeros", 84, 760, 110, "i", BR)
    V.pneu(c, 1560, 560, 230)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Plásticos e", "reciclagem", "do zero")


def d(c):  # o macete: soltas ou amarradas
    escuro(c)
    E.escreve(c, "cadeias soltas", 84, 340, 120, "g", BR)
    E.escreve(c, "ou amarradas?", 84, 500, 140, "g", AMARELO)
    E.escreve(c, "soltas derretem e reciclam", 84, 680, 76, "g", CLARO)
    V.espaguete(c, 0, 1500, 330, 480, 220)
    V.rede(c, 1500, 800, 440, 220, cor="#D8DCE0")


CAPAS = (("capa_A_pao_cabelo_pneu", a), ("capa_B_plasticos_reciclagem", b), ("capa_C_soltas_ou_amarradas", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
