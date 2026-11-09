"""Capas do FIS-ELE-020 (1280x720). Uso: python capa.py"""
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


def pilha(c, cx, cy, w, h, rot):
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h * 0.18, "#22222A", 1, shadow=True)
    M.rrect(c, cx + w * 0.12, cy - h / 2, w * 0.38, h, h * 0.18, BR)
    M.rrect(c, cx + w / 2 - 6, cy - h * 0.17, h * 0.22, h * 0.34, 6, "#B9BCC4")
    E.centro(c, rot, cx - w * 0.15, cy + h * 0.16, h * 0.42, "g", BR)
    E.centro(c, "+", cx + w * 0.31, cy + h * 0.17, h * 0.45, "g", COR)


def a(c):  # o gancho: a tensão que se perde dentro da pilha
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a pilha perde", 84, 390, 130, "i", BR)
    E.escreve(c, "tensão", 84, 580, 190, "g", BR)
    M.rrect(c, 70, 650, 760, 230, 30, BR)
    E.escreve(c, "dentro", 110, 825, 170, "g", COR)
    pilha(c, 1450, 560, 640, 240, "1,5 V")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Gerador", "real", "e rendimento")


def d(c):  # o macete: rendimento = U / ε
    palco_capa(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "rendimento", 84, 360, 130, "i", BR)
    E.escreve(c, "num passo só", 84, 540, 150, "g", BR)
    E.formula(c, "f{U}{ε}", 1450, 640, 300, "g", E.mix(COR, BR, 0.35), 1.0, "center")
    E.escreve(c, "9 ÷ 12 = 75 %", 84, 900, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_pilha_perde_tensao", a), ("capa_B_gerador_real", b), ("capa_C_rendimento_U_sobre_epsilon", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
