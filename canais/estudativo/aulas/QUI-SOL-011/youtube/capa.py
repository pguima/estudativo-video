"""Capas da QUI-SOL-011 (1280x720). Uso: python capa.py"""
import importlib.util, subprocess, sys
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
_s = importlib.util.spec_from_file_location("v", Path(__file__).parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)
E.usar("Química")


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def salvar(capas):
    pasta = Path(__file__).parent
    s = skia.Surface(E.W, E.H)
    for nome, fn in capas:
        fn(s.getCanvas())
        tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
        tmp.unlink()


def a(c):  # o desafio: 5 questões
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "5 questões", 84, 420, 180, "g", BR)
    E.escreve(c, "ferver, congelar", 84, 580, 110, "i", BR)
    E.escreve(c, "e osmose", 84, 700, 110, "i", BR)
    E.escreve(c, "você acerta?", 84, 900, 150, "g", AMARELO)
    V.V8.panela(c, 2.0, 1500, 560, 320, 170, ferve=0.0, sal=6)
    V.uva(c, 1500, 860, 90, 0.3)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Coligativas:", "praticando", "5 questões")


def d(c):  # o macete: o que mudou?
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a pergunta que resolve", 84, 330, 100, "i", BR)
    E.escreve(c, "pressão", 84, 560, 170, "g", BR)
    E.escreve(c, "ou solução?", 84, 760, 170, "g", claro)
    V.V8.duelo(c, 10, 0, 1400, 900, 500, 1.0, 1.0, escuro=True, size=40)


salvar((("capa_A_cinco_questoes", a), ("capa_B_praticando_coligativas", b), ("capa_C_pressao_ou_solucao", d)))
