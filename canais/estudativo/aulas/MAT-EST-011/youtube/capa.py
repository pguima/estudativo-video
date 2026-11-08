"""Capas do MAT-EST-011 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
VERMELHO = "#FF5A5A"


def fichas(c, vals, x, y, size, cores=None):
    """as notas em pílulas brancas; cores = {índice: cor de fundo}"""
    for i, v in enumerate(vals):
        cx = x + i * size * 2.3
        h = size * 1.55
        w = E.larg(v, "g", size) + size * 1.1
        fundo = (cores or {}).get(i, BR)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - h / 2, w, h), h / 2, h / 2), M.paint(fundo))
        E.centro(c, v, cx, y + size * 0.36, size, "g", COR if fundo == BR else "#111111", 1.0)


def a(c):  # o gancho: o do meio não é o 9
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a nota do meio", 84, 330, 110, "i", BR)
    E.escreve(c, "é o 9?", 84, 530, 190, "g", BR)
    fichas(c, ["7", "2", "9", "4", "5"], 230, 780, 100, {2: VERMELHO})
    M.line(c, 610, 860, 790, 700, BR, 1, 16)
    E.escreve(c, "não!", 1420, 560, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Moda e", "mediana", "sem errar")


def d(c):  # o atalho: a posição do meio
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "lista grande?", 84, 360, 110, "i", BR)
    E.escreve(c, "o meio é a", 84, 540, 140, "g", BR)
    E.escreve(c, "posição", 84, 720, 160, "g", AMARELO)
    E.formula(c, "f{n + 1}{2}", 1480, 700, 230, "g", AMARELO, 1.0, "center")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_do_meio_nao_e_o_9", a), ("capa_B_moda_e_mediana", b), ("capa_C_posicao_do_meio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
