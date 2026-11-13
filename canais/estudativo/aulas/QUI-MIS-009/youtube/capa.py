"""Capas da QUI-MIS-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: areia, sal e ferro, a ordem importa
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "areia, sal e ferro:", 84, 340, 110, "i", BR)
    E.escreve(c, "a ordem", 84, 540, 190, "g", BR)
    E.escreve(c, "importa", 84, 740, 190, "g", AMARELO)
    E.escreve(c, "4 misturas, 4 sequências", 84, 960, 80, "i", BR)
    for k, tipo in enumerate(("areia", "sal", "ferro")):
        V.ficha(c, 10, 0, tipo, 1260 + 230 * k, 480, 100)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Ordem da", "separação", "4 questões")


def d(c):  # o macete: seco, água, filtro, fogo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a ordem certa", 84, 330, 110, "i", BR)
    E.escreve(c, "seco, água,", 76, 520, 150, "g", BR)
    E.escreve(c, "filtro, fogo", 76, 690, 150, "g", claro)
    for k in range(4):
        x = 1130 + 200 * k
        c.drawCircle(x, 880, 80, M.paint(BR, 1))
        V.icone_etapa(c, k, x, 880, 1, 0)
        E.bola(c, x - 60, 810, 28)
        E.centro(c, str(k + 1), x - 60, 823, 36, "g", BR, 1)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_ordem_importa", a), ("capa_B_ordem_da_separacao", b), ("capa_C_seco_agua_filtro_fogo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
