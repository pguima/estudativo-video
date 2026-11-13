"""Capas da QUI-TER-001 (1280x720). Uso: python capa.py"""
import importlib.util
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")
_s = importlib.util.spec_from_file_location("visual", Path(__file__).resolve().parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)


def a(c):  # o gancho: a bolsa gelada é exo? Não: endo
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "ficou gelada:", 84, 360, 110, "i", BR)
    E.escreve(c, "EXO?", 84, 600, 220, "g", BR)
    E.risco(c, 70, 630, 640, 440, 1, 0, AMARELO, 30)
    E.escreve(c, "ENDO", 84, 850, 220, "g", AMARELO)
    V.bolsa(c, 1430, 520, 640, 440, 1.0, 1.0, 0.0)
    E.escreve(c, "a bolsa que engana", 84, 1000, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Exo, endo", "e ΔH", "do zero")


def d(c):  # o macete: o sinal é o contrário do termômetro
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "o sinal do", 84, 330, 120, "i", BR)
    E.formula(c, "ΔH", 84 + E.larg("o sinal do ", "i", 120), 330, 110, "g", BR)
    E.escreve(c, "em 2 segundos", 76, 520, 150, "g", BR)
    V.termometro(c, 170, 620, 260, 0.9, 1, escuro=True)
    E.escreve(c, "esquentou:", 280, 740, 76, "i", BR)
    E.formula(c, "ΔH < 0", 280, 900, 130, "g", "#74A9FF")
    V.termometro(c, 1170, 620, 260, 0.15, 1, escuro=True)
    E.escreve(c, "esfriou:", 1280, 740, 76, "i", BR)
    E.formula(c, "ΔH > 0", 1280, 900, 130, "g", V.AMBAR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_bolsa_gelada", a), ("capa_B_exo_endo_delta_h", b), ("capa_C_sinal_do_termometro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
