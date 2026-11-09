"""Capas do FIS-CIN-004 (1280x720). Uso: python capa.py"""
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
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: no ônibus, parado ou em movimento?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.55)
    E.escreve(c, "Você está", 84, 380, 150, "g", BR)
    E.escreve(c, "parado?", 84, 560, 190, "g", AMARELO)
    E.escreve(c, "depende de quem olha", 84, 760, 90, "i", claro)
    x, y, w = 1130, 960, 700
    h = w * 0.36
    M.rrect(c, x, y - h - 40, w, h, 26, BR, 1.0)
    for k in range(5):
        M.rrect(c, x + 34 + k * (w - 68) / 5, y - h - 14, (w - 68) / 5 - 16, h * 0.4, 10, E.mix(COR, BR, 0.55), 1.0)
    for wx in (x + w * 0.2, x + w * 0.8):
        c.drawCircle(wx, y - 50, 50, M.paint("#1B1B20"))
    M.line(c, 1000, y, 1900, y, BR, 1.0, 8)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Referencial", "e posição", "do zero")


def d(c):  # o macete: deslocamento ignora o caminho
    palco(c)
    E.escreve(c, "ignore o caminho", 84, 330, 120, "i", BR)
    E.formula(c, "Δs = final − inicial", 76, 540, 150, "g", BR)
    pts = [(260, 840), (700, 840), (700, 700), (1150, 700), (1150, 840), (1660, 840)]
    F.poli(c, pts, 1.0, E.mix(COR, BR, 0.5), 1.0, 10, dash=[26, 18])
    F.seta(c, 260, 930, 1660, 930, COR, 1.0, 22)
    E.escreve(c, "começo", 200, 1010, 60, "i", BR); E.escreve(c, "fim", 1600, 1010, 60, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_voce_esta_parado", a), ("capa_B_referencial_e_posicao", b), ("capa_C_ignore_o_caminho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
