"""Capas do MAT-EST-006 (1280x720). Uso: python capa.py"""
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
TAB = [("", "presencial", "a distância", "total"), ("manhã", "120", "80", "200"), ("tarde", "100", "50", "150"),
       ("noite", "140", "210", "350"), ("total", "360", "340", "700")]


def tabela(c, x, y, ws, dy, size, cor, destaque=None, circ=()):
    """a tabela de dupla entrada em branco; destaque = linha com faixa; circ = [(linha, coluna, cor)] com anel"""
    xs = [x]
    for w in ws:
        xs.append(xs[-1] + w)
    if destaque is not None:
        M.rrect(c, x - 10, y + dy * destaque - size * 1.0, xs[-1] - x + 20, size * 1.4, 14, BR, 0.22)
    for j, lin in enumerate(TAB):
        yy = y + dy * j
        for k, s in enumerate(lin):
            est = "i" if j == 0 or (j == 4 and k == 0) else "g"
            E.centro(c, s, (xs[k] + xs[k + 1]) / 2, yy, size * (0.75 if j == 0 else 1), est, cor)
    M.line(c, x, y + dy * 0.35, xs[-1], y + dy * 0.35, cor, 0.8, 3)
    M.line(c, x, y + dy * 3.35, xs[-1], y + dy * 3.35, cor, 1, 6)
    for j, k, cc in circ:
        cx, cy = (xs[k] + xs[k + 1]) / 2, y + dy * j - size * 0.36
        c.drawOval(skia.Rect.MakeLTRB(cx - ws[k] * 0.4, cy - size * 0.75, cx + ws[k] * 0.4, cy + size * 0.75), M.paint(cc, 1, stroke=8))


def a(c):  # o gancho: 30% não, 60%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    tabela(c, 1000, 330, [200, 190, 230, 160], 110, 58, BR, 3, [(3, 2, AMARELO), (3, 3, AMARELO)])
    E.escreve(c, "da noite, a distância:", 84, 360, 76, "i", BR)
    E.escreve(c, "30%", 84, 560, 150, "g", VERMELHO)
    M.line(c, 80, 520, 380, 470, BR, 1, 12)
    E.escreve(c, "60%", 84, 780, 210, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Tabelas,", "mapas e", "infográficos")


def d(c):  # o atalho: a tabela se confere sozinha
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "número apagado?", 84, 360, 90, "i", BR)
    E.escreve(c, "total −", 84, 560, 150, "g", BR)
    E.escreve(c, "as outras", 84, 740, 150, "g", AMARELO)
    tabela(c, 1050, 330, [190, 180, 220, 150], 110, 54, BR, 3, [(3, 2, AMARELO)])


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_30_ou_60_por_cento", a), ("capa_B_tabelas_mapas_infograficos", b), ("capa_C_total_menos_as_outras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
