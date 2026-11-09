"""Capas do FIS-MOD-006 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


def pacote(c, x, y, cor, a=1.0, n=3, amp=40, lam=70, largura=12):
    """fóton: trecho de onda com envelope e ponta em seta, andando para a direita"""
    L = n * lam
    path = skia.Path()
    for i in range(61):
        s = -L / 2 + L * i / 60
        d = amp * math.sin(math.pi * i / 60) * math.sin(2 * math.pi * s / lam)
        path.moveTo(x + s, y - d) if i == 0 else path.lineTo(x + s, y - d)
    c.drawPath(path, M.paint(cor, a, stroke=largura, cap_round=True))
    F._cabeca(c, x + L / 2 + 34, y, 1, 0, 40, cor, a)


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: a luz vem em pacotes
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a luz vem", 84, 400, 150, "i", BR)
    E.escreve(c, "em pacotes", 76, 620, 230, "g", BR)
    for i, y in enumerate((800, 900, 1000)):
        pacote(c, 330 + 330 * i, y - 20, BR if i != 1 else AMARELO, 1.0)
def chip(c, x, y, w, h, t=1.3):
    M.rrect(c, x, y, w, h, 30, "#2A2A30")
    for i in range(9):
        for j in range(6):
            on = math.sin(t * 9 + i * 1.7 + j * 2.3) > 0
            M.rrect(c, x + 30 + i * (w - 60) / 9, y + 30 + j * (h - 60) / 6, (w - 60) / 9 - 12, (h - 60) / 6 - 12, 6, AMARELO if on else "#4A4A55")


def diodo(c, x, y, k, cor):
    M.line(c, x - 3 * k, y, x - k, y, cor, 1.0, 12)
    M.line(c, x + k, y, x + 3 * k, y, cor, 1.0, 12)
    p = skia.Path(); p.moveTo(x - k, y - k); p.lineTo(x - k, y + k); p.lineTo(x + k, y); p.close()
    c.drawPath(p, M.paint(cor))
    M.line(c, x + k, y - k, x + k, y + k, cor, 1.0, 14)


def a(c):  # o gancho: bilhões de chaves
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "10 bilhões", 76, 400, 190, "g", BR)
    E.escreve(c, "de chaves no", 84, 560, 120, "i", BR)
    E.escreve(c, "seu celular", 76, 760, 170, "g", AMARELO)
    chip(c, 1220, 260, 600, 500)
    E.escreve(c, "feitas de silício", 84, 960, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Diodo e", "transistor", "do zero")


def d(c):  # o macete: 5 → n, 3 → p
    escuro(c)
    E.escreve(c, "tipo n ou tipo p?", 84, 330, 110, "i", BR)
    E.escreve(c, "5 elétrons → n", 84, 560, 160, "g", BR)
    E.escreve(c, "3 elétrons → p", 84, 760, 160, "g", AMARELO)
    diodo(c, 1500, 950, 70, BR)
    E.escreve(c, "compare com os 4 do silício", 84, 970, 70, "i", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_bilhoes_de_chaves", a), ("capa_B_diodo_e_transistor", b), ("capa_C_tipo_n_ou_p", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
