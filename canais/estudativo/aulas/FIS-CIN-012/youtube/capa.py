"""Capas do FIS-CIN-012 (1280x720). Uso: python capa.py"""
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


def eixos(c, x, y, w, h, cor, rot_y="v", rot_x="t"):
    """eixos de um gráfico na capa: origem em (x, y + h)"""
    F.seta(c, x, y + h, x + w, y + h, cor, 1.0, 10)
    F.seta(c, x, y + h, x, y, cor, 1.0, 10)
    E.escreve(c, rot_y, x + 30, y + 40, 80, "g", cor)
    E.escreve(c, rot_x, x + w + 10, y + h + 20, 80, "g", cor)


def a(c):  # o gancho: o triângulo do gráfico dá a distância
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    x, y, w, h = 1080, 260, 700, 560
    p = skia.Path()
    p.moveTo(x, y + h); p.lineTo(x + w * 0.85, y + h); p.lineTo(x + w * 0.85, y + 60); p.close()
    c.drawPath(p, M.paint(AMARELO, 0.9))
    eixos(c, x, y, w, h, BR)
    M.line(c, x, y + h, x + w * 0.85, y + 60, BR, 1.0, 14)
    E.centro(c, "? m", x + w * 0.58, y + h - 90, 110, "g", "#3A2A00")
    F.medida(c, 20, "m/s", x + w * 0.85 - 20, y + 30, 70, BR, 1.0, "right", cor_u=BR)
    F.medida(c, 10, "s", x + w * 0.85, y + h + 90, 70, BR, 1.0, "center", cor_u=BR)
    E.escreve(c, "quantos", 84, 400, 150, "i", BR)
    E.escreve(c, "metros", 84, 590, 190, "g", BR)
    E.escreve(c, "andou?", 84, 790, 190, "g", BR)
    E.escreve(c, "é só a área", 84, 960, 100, "i", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Gráfico", "v × t", "área e inclinação")


def d(c):  # o macete: a escada
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a escada", 84, 330, 130, "i", BR)
    E.escreve(c, "dos gráficos", 76, 500, 150, "g", BR)
    for i, (l, nome) in enumerate((("s", "posição"), ("v", "velocidade"), ("a", "aceleração"))):
        x, y = 160 + i * 300, 600 + i * 140
        M.rrect(c, x, y, 640, 120, 18, E.mix(COR, "#07070F", 0.2 + 0.2 * i))
        E.escreve(c, l, x + 40, y + 92, 90, "g", BR)
        E.escreve(c, nome, x + 150, y + 84, 60, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    F.seta(c, 1250, 330, 1420, 640, claro, 1.0, 16)
    E.escreve(c, "inclinação", 1240, 300, 64, "g", claro)
    F.seta(c, 1620, 960, 1760, 560, BR, 1.0, 16)
    E.escreve(c, "área", 1660, 530, 72, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantos_metros_andou", a), ("capa_B_grafico_v_t", b), ("capa_C_a_escada_dos_graficos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
