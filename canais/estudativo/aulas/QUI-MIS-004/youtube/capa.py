"""Capas da QUI-MIS-004 (1280x720). Uso: python capa.py"""
import importlib.util
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")
_s = importlib.util.spec_from_file_location("visual_aula", Path(__file__).parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)


def curva(c, x, y, w, h, nos, cor_linha, cor_plat, largura=14, eixo=BR):
    G = V.Graf(x, y, w, h, min(T for _, T in nos), max(T for _, T in nos))
    M.line(c, G.x, G.y + G.h, G.x, G.y, eixo, 0.8, 6)
    M.line(c, G.x, G.y + G.h, G.x + G.w, G.y + G.h, eixo, 0.8, 6)
    pl = V.patamares(nos)
    for k in range(5):
        (m0, T0), (m1, T1) = nos[k], nos[k + 1]
        plat = (k == 1 and pl[0]) or (k == 3 and pl[1])
        M.line(c, G.X(m0), G.Y(T0), G.X(m1), G.Y(T1), cor_plat if plat else cor_linha, 1, largura + (6 if plat else 0))
    return G


def a(c):  # o gancho: o fogo aceso e o termômetro parado
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "fogo aceso,", 84, 360, 130, "i", BR)
    E.escreve(c, "e o termômetro", 84, 500, 120, "i", BR)
    E.escreve(c, "trava no 0", 84, 720, 190, "g", AMARELO)
    E.escreve(c, "pura ou mistura?", 84, 960, 90, "i", BR)
    G = curva(c, 1120, 300, 700, 600, V.AGUA, BR, AMARELO)
    c.drawCircle((G.X(2) + G.X(4)) / 2, G.Y(0), 80, M.paint(AMARELO, 1, stroke=8))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Pura ou", "mistura?", "pela curva")


def d(c):  # o macete: conte os patamares
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "pura ou mistura?", 84, 330, 110, "i", BR)
    E.escreve(c, "conte os", 76, 520, 170, "g", BR)
    E.escreve(c, "patamares", 76, 700, 170, "g", claro)
    for k, (nos, nome) in enumerate(((V.AGUA, "2 patamares = pura"), (V.SOLDA, "só embaixo = eutética"), (V.ALCOOL, "só em cima = azeotrópica"))):
        y = 250 + 270 * k
        curva(c, 1180, y, 260, 170, nos, BR, claro, 7, "#8A8D99")
        E.escreve(c, nome.split(" = ")[0], 1490, y + 100, 48, "b", BR)
        E.escreve(c, nome.split(" = ")[1], 1490, y + 160, 48, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_trava_no_zero", a), ("capa_B_curva_de_aquecimento", b), ("capa_C_conte_os_patamares", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
