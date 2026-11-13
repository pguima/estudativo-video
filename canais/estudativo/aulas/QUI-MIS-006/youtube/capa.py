"""Capas da QUI-MIS-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: ouro da areia só com água
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "separar ouro da areia", 84, 360, 110, "i", BR)
    E.escreve(c, "só com", 84, 560, 190, "g", BR)
    E.escreve(c, "água", 84, 760, 190, "g", AMARELO)
    E.escreve(c, "e outros 6 métodos", 84, 970, 80, "i", BR)
    V.bateia(c, 1.0, 1440, 600, 760, 1.0, 0.45, gira=False)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Separar", "sólidos", "do zero")


def d(c):  # o macete: ache a diferença
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "qual método?", 84, 330, 110, "i", BR)
    E.escreve(c, "ache a", 76, 520, 170, "g", BR)
    E.escreve(c, "diferença", 76, 700, 170, "g", claro)
    for k, (dif, met) in enumerate((("tamanho", "peneira"), ("densidade", "ar ou água"), ("ímã", "magnética"), ("dissolve", "dissolução"))):
        y = 300 + 170 * k
        E.pilula(c, dif, 1260, y, 50, "g", fundo="#1F2030")
        E.escreve(c, "→ " + met, 1450, y + 18, 54, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_ouro_so_com_agua", a), ("capa_B_separar_solidos", b), ("capa_C_ache_a_diferenca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
