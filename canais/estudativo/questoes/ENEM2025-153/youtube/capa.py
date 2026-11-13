"""Capas da resolução ENEM 2025 · questão 153 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def casas(c, digs, y, bw=200, bh=240, cor_dig=None, destaque=()):
    gap, ggap = 18, 60
    total = 7 * bw + 3 * gap + 3 * ggap
    x = (E.W - total) / 2
    for i, n in enumerate((1, 2, 3, 1)):
        for k in range(n):
            j = sum((1, 2, 3, 1)[:i]) + k
            M.rrect(c, x, y, bw, bh, 26, AMARELO if j in destaque else BR, 1, shadow=True)
            d = digs[j]
            E.centro(c, d, x + bw / 2, y + bh / 2 + bh * 0.22, bh * 0.62, "g", cor_dig or COR)
            x += bw + (gap if k < n - 1 else ggap)


def a(c):  # o código com o zero que derruba
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "ENEM 2025 · questão 153", 84, 300, 96, "g", BR)
    casas(c, "2?81090", 480, destaque=(1,))
    E.escreve(c, "o zero que derruba", 84, 960, 140, "i", BR)


def b(c):  # modelo padrão
    E.capa_modelo(c, "Matemática", "ENEM 2025", "questão", "153")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "acerte em", 84, 330, 150, "i", BR)
    E.escreve(c, "2 olhares", 84, 560, 240, "g", BR)
    for k, (l, s, ok) in enumerate((("C", "1010982", False), ("D", "2081090", True), ("E", "2810910", False))):
        y = 760 + k * 120
        E.bola(c, 1180, y, 46, E.CERTO if ok else COR, 1 if ok else 0.5)
        E.centro(c, l, 1180, y + 20, 56, "g", BR, 1 if ok else 0.5)
        E.escreve(c, s, 1260, y + 36, 100, "g", "#5BE3A4" if ok else BR, 1 if ok else 0.4)
        if not ok:
            M.line(c, 1120, y + 4, 1740, y - 4, E.ERRADO, 1, 10)
    E.escreve(c, "ENEM 2025 · Q153", 84, 1010, 70, "b", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_zero", a), ("capa_B_questao_153", b), ("capa_C_dois_olhares", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
