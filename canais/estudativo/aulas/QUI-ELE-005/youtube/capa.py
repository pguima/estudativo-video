"""Capas da QUI-ELE-005 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def base(c):
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)


def salvar(capas):
    pasta = Path(__file__).parent
    s = skia.Surface(E.W, E.H)
    for nome, fn in capas:
        fn(s.getCanvas())
        tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
        tmp.unlink()


def bateria(c, cx, cy, w, h):
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#2A2B31", 1)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h * 0.2, 22, "#3A3B42", 1)
    for dx, s in ((-0.3, "−"), (0.3, "+")):
        M.rrect(c, cx + dx * w - 26, cy - h / 2 - 34, 52, 40, 8, "#9AA0A8", 1)
        E.centro(c, s, cx + dx * w, cy - h / 2 + h * 0.15, 56, "g", BR, 1)
    M.rrect(c, cx - w * 0.36, cy - h * 0.05, w * 0.72, h * 0.38, 14, COR, 1)
    E.centro(c, "12 V", cx, cy + h * 0.24, h * 0.2, "g", BR, 1)


def a(c):  # o gancho: por que uma recarrega e a outra não
    base(c)
    bateria(c, 1420, 600, 600, 420)
    E.escreve(c, "por que essa", 84, 440, 140, "g", BR)
    E.escreve(c, "recarrega", 84, 610, 160, "g", AMARELO)
    E.escreve(c, "e a pilha não?", 84, 770, 120, "g", BR)
    E.escreve(c, "pilhas e baterias por dentro", 84, 950, 72, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Pilhas", "e baterias", "por dentro")


def d(c):  # o macete: metal puro x óxido
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete de prova", 84, 300, 110, "i", BR)
    E.escreve(c, "metal puro", 84, 500, 130, "g", "#FFB347"); E.escreve(c, "= ânodo", 900, 500, 130, "g", BR)
    E.escreve(c, "óxido", 84, 700, 130, "g", "#7FB2FF"); E.escreve(c, "= cátodo", 900, 700, 130, "g", BR)
    Q.formula(c, "Pb + PbO2", 84, 920, 120, claro, escuro=True)


salvar((("capa_A_por_que_recarrega", a), ("capa_B_pilhas_e_baterias", b), ("capa_C_metal_e_oxido", d)))
