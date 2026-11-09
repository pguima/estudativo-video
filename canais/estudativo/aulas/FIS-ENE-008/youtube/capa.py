"""Capas do FIS-ENE-008 (1280x720). Uso: python capa.py"""
import subprocess, sys
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho: de onde vem o coice?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "de onde vem", 84, 380, 130, "i", BR)
    E.escreve(c, "o coice?", 84, 620, 220, "g", BR)
    E.escreve(c, "Q antes = Q depois", 84, 860, 110, "g", AMARELO)
    claro = E.mix(COR, BR, 0.85)
    M.rrect(c, 1180, 500, 260, 110, 30, E.mix(COR, "#000000", 0.35))
    M.rrect(c, 1400, 525, 460, 50, 16, claro)
    F.seta(c, 1360, 720, 1130, 720, BR, 1.0, 18)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Conservação", 76, 450, 190, "g", BR)
    E.escreve(c, "de Q = m·v", 76, 660, 190, "g", BR)
    E.escreve(c, "recuos e explosões", 84, 860, 110, "i", BR)
    E.simbolo(c, 1620, 780, 230, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: razão inversa das massas
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "começou parado?", 84, 340, 110, "i", BR)
    E.escreve(c, "massa × 2", 76, 580, 150, "g", BR)
    E.escreve(c, "velocidade ÷ 2", 76, 780, 150, "g", E.mix(COR, BR, 0.5))
    E.bola(c, 1450, 900, 130, COR)
    E.bola(c, 1740, 920, 90, F.VEL)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_de_onde_vem_o_coice", a), ("capa_B_conservacao_da_quantidade_de_movimento", b), ("capa_C_razao_inversa_das_massas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
