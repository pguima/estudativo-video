"""Capas do vídeo Tecnologia 011 — FireTrace (tema 'tech'). 3 variações em 1280x720.
Nenhum quadro do vídeo original: a interface aparece só como RECRIAÇÃO desenhada (relevo procedural, perímetro,
câmera térmica sintética), com o selo RECRIAÇÃO ILUSTRATIVA. Sem logos."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
sys.path.insert(0, str(HERE.parent / "roteiro"))
import skia
import tech
from motor import *  # noqa
from tech import *  # noqa
import visual as V  # também troca a fonte mono para DejaVu Sans Mono

PX, PY, PW, PH = 1140, 150, 680, 760


def base(c, col=CYAN, tag="IA · CLAUDE OPUS 5.5 · PROTÓTIPO"):
    tech.background(c, 3.0)
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        tech._bracket(c, x, y, dx, dy, col, 0.7)
    chip(c, tag, 84, 110, col, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    for s, y in ((l1, 330), (l2, 460)):
        size = min(120, 120 * 1000 / text_w(s, "black", 120))
        glow_text(c, s, 80, y, size, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 510, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 597, size, "black", "#03050B")


def selo(c):
    chip(c, "RECRIAÇÃO ILUSTRATIVA", PX + PW / 2, PY + PH + 50, GOLD, 1, anchor="center", size=24, filled=True)


def lado_mapa(c):
    panel(c, PX, PY, PW, PH, 1, V.ORG, label="firetrace · recriação")
    V.map_view(c, PX + 16, PY + 30, PW - 32, PH - 46, 1, 1.0, 1.0, marks=False)
    # marcas de hora (só 3, para caber)
    w, h = PW - 32, PH - 46
    for s, lab in ((0.0, "IGNIÇÃO 14:26"), (0.52, "15 AGO 00:00"), (1.0, "15 AGO 12:00")):
        x, y = V.proj(*V._center(s), w, h)
        c.drawCircle(PX + 16 + x, PY + 30 + y, 9, paint("#FFFFFF"))
        c.drawCircle(PX + 16 + x, PY + 30 + y, 9, paint(V.ORG, stroke=3))
        chip(c, lab, PX + 16 + x + 16, PY + 30 + y - 30, V.ORG, 1, size=22, filled=True)
    for k, (u, v) in enumerate(V.DRONES_UV[:4]):
        x, y = V.proj(u, v, w, h)
        gx, gy = PX + 16 + x, PY + 30 + y - 60
        c.drawCircle(gx, gy, 28, paint("#0B1426", 0.9))
        V.ic_drone(c, gx, gy, 36, CYAN, 1, 0.3)
    selo(c)


def lado_termica(c):
    panel(c, PX, PY, PW, PH, 1, ROSE, label="câmera IR · recriação")
    V.thermal_cam(c, PX + 24, PY + 40, PW - 48, 420, 1, 0.3)
    for k, (cod, nome, fun, _) in enumerate(V.FROTA):
        y = PY + 520 + k * 38
        V.ic_drone(c, PX + 60, y - 8, 26, CYAN if k != 1 else V.ORG, 1, 0.3)
        text(c, f"{cod} {nome}", PX + 95, y, 24, "bold", INK, 1, align="left")
        text(c, fun, PX + 330, y, 22, "mono", INK2, 1, align="left")
    selo(c)


def lado_limites(c):
    panel(c, PX, PY, PW, PH, 1, GOLD, label="o vídeo não mostra")
    for k, s in enumerate(("CÓDIGO", "PROMPTS", "TEMPO GASTO", "DADOS REAIS?")):
        y = PY + 150 + k * 150
        c.drawCircle(PX + 100, y - 20, 44, paint(ROSE, 0.15)); c.drawCircle(PX + 100, y - 20, 44, paint(ROSE, 1, stroke=4))
        text_mid(c, "?", PX + 100, y - 20, 56, "black", ROSE)
        glow_text(c, s, PX + 175, y + 4, 60, "black", INK, 1, align="left", glow=0.15)
    chip(c, "SÓ EXISTE EM VÍDEO", PX + PW / 2, PY + PH - 50, GOLD, 1, anchor="center", size=28, filled=True)


def capa_painel(c):
    base(c, V.ORG)
    big(c, "UM PAINEL DE", "INCÊNDIO FEITO", "COM IA", V.ORG)
    text(c, "FireTrace, feito com o Claude Opus 5.5", 90, 800, 42, "monob", INK2, align="left")
    lado_mapa(c)


def capa_drones(c):
    base(c, ROSE, "PROTÓTIPO · DRONES · CÂMERA TÉRMICA")
    big(c, "6 DRONES NO AR,", "1 PONTO QUENTE:", "983 °C", ROSE)
    text(c, "o que o FireTrace mostra (e o que não)", 90, 800, 42, "monob", INK2, align="left")
    lado_termica(c)


def capa_nome(c):
    base(c, GOLD, "OPUS 5.5 · ANÁLISE SEM HYPE")
    big(c, "FIRETRACE:", "O QUE O VÍDEO", "NÃO MOSTRA", GOLD)
    text(c, "protótipo bonito × sistema real", 90, 800, 44, "monob", INK2, align="left")
    lado_limites(c)


if __name__ == "__main__":
    for nome, fn in (("capa_A_painel_com_ia", capa_painel), ("capa_B_983_graus", capa_drones),
                     ("capa_C_o_que_nao_mostra", capa_nome)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
