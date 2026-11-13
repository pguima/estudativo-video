"""Capas da QUI-AMB-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o buraco no ozônio esquenta o planeta? Não
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "buraco no ozônio", 84, 360, 110, "i", BR)
    E.escreve(c, "esquenta", 84, 540, 170, "g", BR)
    E.escreve(c, "o planeta?", 84, 710, 170, "g", BR)
    E.escreve(c, "não!", 84, 930, 170, "g", AMARELO)
    V.ceu(c, 1120, 220, 700, 700)
    V.sol(c, 1260, 320, 60)
    M.rrect(c, 1120, 430, 700, 90, 0, E.COR, 0.8)
    for k in range(3):
        V.seta_reta(c, 1450 + 120 * k, 260, 1450 + 120 * k, 420, V.UV)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Estufa", "ou ozônio?", "sem confundir")


def d(c):  # o macete: a direção da luz
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "nunca mais confunda:", 84, 330, 100, "i", BR)
    E.escreve(c, "a direção", 76, 520, 160, "g", BR)
    E.escreve(c, "da luz", 76, 690, 160, "g", E.mix(COR, BR, 0.5))
    V.seta_ir(c, 1250, 900, 1250, 400, 1, 1, "#F5A04A", 0)
    E.escreve(c, "calor sai:", 1310, 600, 60, "g", "#F5A04A")
    E.escreve(c, "estufa", 1310, 680, 60, "g", BR)
    V.seta_reta(c, 1600, 400, 1600, 900, "#B79CFF")
    E.escreve(c, "UV entra:", 1650, 800, 50, "g", "#B79CFF")
    E.escreve(c, "ozônio", 1650, 870, 50, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_buraco_esquenta_nao", a), ("capa_B_estufa_ou_ozonio", b), ("capa_C_a_direcao_da_luz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
