"""Capas da QUI-TER-002 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def a(c):  # o gancho: o ΔH que ninguém mede, mas está na tabela
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "ninguém mede", 84, 330, 110, "i", BR)
    Q.formula(c, "C + ½ O2 -> CO", 84, 540, 150, BR)
    E.formula(c, "ΔH = ?", 84, 760, 190, "g", BR)
    E.risco(c, 560, 780, 800, 600, 1, 0, AMARELO, 26)
    E.formula(c, "−111 kJ", 860, 760, 190, "g", AMARELO)
    E.escreve(c, "somando equações", 84, 960, 96, "i", BR)
    Q.molecula_desenho(c, "CO", 1560, 470, 190)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Lei", "de Hess", "do zero")


def d(c):  # o macete: as três regras
    escuro(c)
    E.escreve(c, "as 3 regras", 84, 320, 120, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for k, (a1, a2) in enumerate((("inverteu", "troca o sinal"), ("multiplicou", "multiplica"), ("somou", "soma"))):
        y = 520 + k * 190
        E.escreve(c, a1, 84, y, 130, "g", BR)
        E.escreve(c, "→ " + a2, 84 + E.larg(a1 + " ", "g", 130), y, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_delta_h_que_ninguem_mede", a), ("capa_B_lei_de_hess", b), ("capa_C_tres_regras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
