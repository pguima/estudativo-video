"""Capas da QUI-ORG-021 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: vinho vira vinagre
    claro(c)
    E.escreve(c, "vinho vira", 84, 400, 170, "g", BR)
    E.escreve(c, "vinagre", 84, 600, 200, "g", AMARELO)
    E.escreve(c, "e o bafômetro muda de cor", 84, 790, 96, "i", BR)
    V.garrafa(c, 1380, 900)
    Q.tubo(c, 0, -9, 1700, 900, 130, 480, 0.55, V.VERDE, graduacao=False)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Oxidação", "de álcoois", "do zero")


def d(c):  # o macete: conte os H do carbono do OH
    escuro(c)
    E.escreve(c, "conte os H", 84, 340, 140, "g", BR)
    E.escreve(c, "do carbono do OH", 84, 500, 110, "g", AMARELO)
    for i, s in enumerate(("2 H → aldeído → ácido", "1 H → cetona", "nenhum H → não oxida")):
        E.escreve(c, s, 84, 680 + i * 110, 80, "g", CLARO)


CAPAS = (("capa_A_vinho_vira_vinagre", a), ("capa_B_oxidacao_de_alcoois", b), ("capa_C_conte_os_h", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
