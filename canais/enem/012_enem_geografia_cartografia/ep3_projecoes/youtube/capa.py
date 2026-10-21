"""Capas — Cartografia, Episódio 3: Projeções (tema claro). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
import mapas

MLAT = (-58, 80)


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "CARTOGRAFIA · EPISÓDIO 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def merc_with(c, R, extra):
    mapas.draw_world(c, R, 1, proj="mercator", lat=MLAT)
    fr = mapas.world_frame(R, "mercator", (-180, 180), MLAT)
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(*fr), 18, 18), True)
    extra(R)
    c.restore()


def capa_mentiu(c):
    background(c)
    selo(c)
    painel(c)
    R = (1150, 200, 640, 700)

    def ex(R):
        mapas.draw_rings_on(c, mapas._country_rings("Greenland"), R, 1, "#F59E0B", "#B45309", proj="mercator", lon=(-75, 60), lat=(-38, 82))
        mapas.draw_rings_on(c, mapas.continent_rings("Africa"), R, 1, "#F59E0B", "#B45309", proj="mercator", lon=(-75, 60), lat=(-38, 82))
    mapas.draw_world(c, R, 1, proj="mercator", lon=(-75, 60), lat=(-38, 82))
    fr = mapas.world_frame(R, "mercator", (-75, 60), (-38, 82))
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(*fr), 18, 18), True); ex(R); c.restore()
    pill(c, "14× maior", 1470, 900, RED, size=44, anchor="center", bounds=(0, 1920))
    text(c, "O MAPA DA", 80, 340, 128, "black", INK, align="left")
    text(c, "ESCOLA", 80, 470, 128, "black", INK, align="left")
    boxed(c, "MENTIU", 70, 520, 160, RED)
    text(c, "projeções cartográficas · ENEM", 90, 860, 52, "extrabold", INK2, align="left")


def capa_encolhe(c):
    background(c)
    selo(c)
    painel(c)
    R = (1150, 220, 640, 640)
    lon, lat = (-75, 60), (-38, 82)
    mapas.draw_world(c, R, 1, proj="mercator", lon=lon, lat=lat)
    fr = mapas.world_frame(R, "mercator", lon, lat)
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(*fr), 18, 18), True)
    mapas.draw_rings_on(c, mapas.continent_rings("Africa"), R, 1, "#CBD5E1", "#64748B", proj="mercator", lon=lon, lat=lat)
    mapas.draw_rings_on(c, mapas._country_rings("Greenland"), R, 0.45, "#F59E0B", "#B45309", proj="mercator", lon=lon, lat=lat)
    mapas.draw_rings_on(c, mapas.moved_rings("Greenland", (20, 4)), R, 1, "#E5484D", "#991B1B", proj="mercator", lon=lon, lat=lat)
    c.restore()
    text(c, "A GROENLÂNDIA", 80, 340, 112, "black", INK, align="left")
    text(c, "DE VERDADE É", 80, 470, 112, "black", INK, align="left")
    boxed(c, "PEQUENA", 70, 520, 160, AMBER, INK)
    text(c, "Mercator x Peters · ENEM", 90, 860, 54, "extrabold", INK2, align="left")


def capa_laranja(c):
    background(c)
    selo(c)
    painel(c)
    c.drawCircle(1300, 360, 120, paint("#FB923C")); c.drawCircle(1300, 360, 120, paint("#EA580C", 1, stroke=6))
    for k in range(6):
        x = 1240 + k * 75
        p = skia.Path(); p.moveTo(x, 600); p.quadTo(x + 34, 720, x, 840); p.quadTo(x - 34, 720, x, 600); p.close()
        c.drawPath(p, paint("#FB923C")); c.drawPath(p, paint("#EA580C", 1, stroke=4))
    arrow(c, 1300, 500, 1300, 580, INK2, 1, 6, 22)
    text(c, "rasga ou estica", 1470, 540, 44, "black", RED)
    text(c, "TODO MAPA", 80, 340, 136, "black", INK, align="left")
    text(c, "DISTORCE", 80, 470, 136, "black", INK, align="left")
    boxed(c, "ALGUMA COISA", 70, 520, 120, PURPLE)
    text(c, "por que nenhum mapa é perfeito", 90, 860, 52, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_mapa_mentiu", capa_mentiu), ("capa_B_groenlandia_pequena", capa_encolhe), ("capa_C_todo_mapa_distorce", capa_laranja)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
