"""Capas do FIS-ELE-023 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho: seis questões misturadas
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "6", 70, 700, 560, "g", BR)
    E.escreve(c, "questões", 470, 470, 150, "g", BR)
    E.escreve(c, "resolvidas", 470, 640, 130, "i", BR)
    for k, s in enumerate(("conta de luz", "chuveiro", "bateria", "motor")):
        x, y = 1100 + (k % 2) * 400, 840 + (k // 2) * 120
        w = E.larg(s, "g", 60) + 70
        M.rrect(c, x - w / 2, y - 55, w, 100, 50, BR if k % 2 == 0 else "#1B1B20")
        E.centro(c, s, x, y + 18, 60, "g", COR if k % 2 == 0 else BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Geradores", "e motores", "praticando")


def d(c):  # o macete: pergunte o que cada peça faz com a energia
    palco_capa(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o que cada peça faz", 84, 360, 120, "i", BR)
    E.escreve(c, "com a energia?", 84, 540, 150, "g", BR)
    claro = E.mix(COR, BR, 0.35)
    for k, (nome, f) in enumerate((("gerador", "U = ε − r · i"), ("receptor", "U = ε′ + r′ · i"))):
        y = 760 + k * 150
        E.escreve(c, nome, 84, y, 80, "i", BR)
        E.formula(c, f, 520, y, 96, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_seis_questoes", a), ("capa_B_geradores_e_motores", b), ("capa_C_o_que_cada_peca_faz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
