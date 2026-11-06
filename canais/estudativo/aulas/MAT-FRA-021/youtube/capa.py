"""Capas do MAT-FRA-021 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"



def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: o pacote que parece mais barato
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "R$ 14", 84, 450, 230, "g", BR)
    E.escreve(c, "2,5 kg", 84, 590, 120, "i", BR)
    E.escreve(c, "ou", 750, 450, 170, "i", BR)
    E.escreve(c, "R$ 8,70", 1010, 450, 230, "g", AMARELO)
    E.escreve(c, "1,5 kg", 1010, 590, 120, "i", AMARELO)
    E.escreve(c, "qual sai mais", 84, 850, 160, "i", BR)
    E.escreve(c, "barato?", 900, 850, 190, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "decimais", "dinheiro e medida")


def d(c):  # o macete: três quartos de um preço
    palco(c)
    E.fracao(c, 3, 4, 200, 330, 140, BR)
    E.escreve(c, "de um preço", 340, 420, 170, "i", BR)
    E.escreve(c, "÷ 4", 84, 700, 270, "g", AMARELO)
    E.escreve(c, "e", 640, 700, 200, "i", BR)
    E.escreve(c, "× 3", 830, 700, 270, "g", AMARELO)
    E.escreve(c, "sem armar a conta", 84, 930, 150, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_sai_mais_barato", a), ("capa_B_praticando_decimais", b), ("capa_C_tres_quartos_de_um_preco", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
