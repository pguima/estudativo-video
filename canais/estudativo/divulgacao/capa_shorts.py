"""Capas verticais (1080x1920) dos Shorts-convite. Uso: python capa_shorts.py [MAT-FRA_short ...] (sem argumento: todas)
O conteúdo fica na faixa central (y 300–1500), que aparece inteira na prateleira de Shorts e no recorte quadrado."""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M

E.W, E.H = 1080, 1920          # capa_base desenha no tamanho vertical
W, H, CX = 1080, 1920, 540
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
PASTA = Path(__file__).parent


def topo(c):
    E.capa_base(c, COR)
    s = "MATEMÁTICA"
    w = E.larg(s, "b", 46) + 76
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 250, w, 88), 44, 44), M.paint(M.on(COR)))
    E.centro(c, s, CX, 310, 46, "b", COR)


def relogio(c, y):  # o cronômetro "3 s": o laço aberto do desafio
    E.bola(c, CX, y, 120, AMARELO)
    E.centro(c, "3s", CX, y + 40, 112, "g", "#1A1A1A")


def rodape(c, s):
    E.centro(c, s, CX, 1500, 64, "i", BR)
    E.centro(c, "ESTUDATIVO", CX, 1600, 44, "b", BR, 0.8)


def num(c):
    topo(c)
    E.centro(c, "quanto é", CX, 560, 96, "i", BR)
    E.centro(c, "48 × 5", CX, 800, 230, "g", BR)
    E.centro(c, "= ?", CX, 1010, 200, "g", AMARELO)
    relogio(c, 1230)
    rodape(c, "você tem 3 segundos")


def div(c):
    topo(c)
    E.centro(c, "4.572", CX, 700, 250, "g", BR)
    E.centro(c, "÷ 9 ?", CX, 920, 200, "g", AMARELO)
    E.centro(c, "sem fazer a conta", CX, 1060, 76, "i", BR)
    relogio(c, 1260)
    rodape(c, "você tem 3 segundos")


def fra(c):
    topo(c)
    E.centro(c, "quanto é", CX, 520, 96, "i", BR)
    for x, d in ((CX - 250, 2), (CX + 250, 3)):
        E.fracao(c, 1, d, x, 760, 190, BR)
    E.centro(c, "+", CX, 760 + 68, 180, "g", AMARELO)
    E.centro(c, "= ?", CX, 1100, 200, "g", AMARELO)
    relogio(c, 1300)
    rodape(c, "você tem 3 segundos")


def q153(c):  # questão 153 do ENEM 2025: o código do visitante
    topo(c)
    E.centro(c, "ENEM 2025 · questão 153", CX, 470, 54, "b", AMARELO)
    E.centro(c, "qual é o", CX, 600, 96, "i", BR)
    E.centro(c, "código?", CX, 790, 200, "g", BR)
    bw, bh, gap, gg = 104, 140, 10, 28
    x = CX - (7 * bw + 3 * gap + 3 * gg) / 2
    for n in (1, 2, 3, 1):
        for k in range(n):
            M.rrect(c, x, 880, bw, bh, 18, BR, 1, shadow=True)
            E.centro(c, "?", x + bw / 2, 880 + bh / 2 + 34, 96, "g", COR)
            x += bw + (gap if k < n - 1 else gg)
    E.centro(c, "2º andar · setor 08 · func. 109 · manhã", CX, 1100, 46, "i", BR)
    relogio(c, 1290)
    rodape(c, "você tem 3 segundos")


for pasta, nome, fn in (("MAT-NUM_short", "capa_short_48x5", num), ("MAT-DIV_short", "capa_short_4572_div_9", div),
                        ("MAT-FRA_short", "capa_short_meio_mais_terco", fra),
                        ("../questoes/ENEM2025-153_short", "capa_short_enem2025_q153", q153)):
    if sys.argv[1:] and pasta not in sys.argv[1:]:
        continue
    s = skia.Surface(W, H)
    fn(s.getCanvas())
    out = PASTA / pasta / "youtube"
    tmp = out / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-q:v", "2", str(out / f"{nome}.jpg")], check=True)
    tmp.unlink()
    print(out / f"{nome}.jpg")
