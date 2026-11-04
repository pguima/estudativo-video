"""Imagens do YouTube: miniaturas do vídeo 001 (3 versões para o "Testar e comparar"), avatar, banner e marca d'água.
python youtube.py → canais/antigos/visual/youtube/*.png|jpg
VIDEO_LANG=en python youtube.py → youtube_en/ (textos do 001_o_que_vai_sobrar/roteiro/textos_en.py)"""
import sys, math
from pathlib import Path
import skia
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "_ferramentas"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import idioma_antigos as lingua  # noqa: E402
lingua.preparar(globals(), Path(__file__).resolve().parent.parent / "001_o_que_vai_sobrar")
from antigos import *  # noqa: E402,F403
from antigos import _meia_lua  # noqa: E402,F401

OUT = Path(__file__).parent / f"youtube{lingua.SUF}"


def texto_capa(c, s, x, y, size, cor="#ffffff", contorno="#070c38"):
    """texto de miniatura: Rubik Black com contorno grosso"""
    size = min(size, size * 1780 / font("thumb", size, 900).measureText(s))
    f = font("thumb", size, 900)
    w = f.measureText(s)
    p = skia.Paint(AntiAlias=True, Color=hexc(contorno), Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.16,
                   StrokeJoin=skia.Paint.kRound_Join)
    c.drawString(s, x - w / 2, y, f, p)
    c.drawString(s, x - w / 2, y, f, paint(cor))


def palco(c, cor_fundo="#2540a8"):
    """fundo de miniatura: salão azul vivo, holofote e pedestal com etiqueta"""
    c.drawRect(skia.Rect.MakeWH(W, H), radial(W / 2, 520, 1100, [cor_fundo, "#14206b", "#0a1240"], [0, 0.6, 1]))
    for k, cor in enumerate((PINK, SKY, AMBER, CYAN)):
        x = [140, 420, 1500, 1780][k]
        c.drawRRect(rr(x - 90, 260, 180, 700, 90), paint(mix(cor, "#1d2f8f", 0.5), 0.55))
    holofote(c, W / 2, 0, 1000, 160, 820, 1.2)
    poeira(c, 3.0, (W / 2 - 380, 40, W / 2 + 380, 980), 60, seed=4, a=0.6)
    pedestal(c, W / 2, 960, 900, 200, None, 1.0)
    placa = "PEÇA Nº 001 · c. 2026 d.C."
    pw = max(540, text_w(placa, 30, "mono", 500) * 1.06 + 70)  # 1.06: tracking
    c.drawRRect(rr(W / 2 - pw / 2, 1000, pw, 60, 4), paint("#ffe9c2"))
    text(c, placa, W / 2, 1040, 30, "mono", 500, "#3a2c18", 1, "center", tracking=0.06)


def miniatura(nome, frase, peca):
    surf = skia.Surface(W, H)
    c = surf.getCanvas()
    palco(c)
    c.drawOval(oval(W / 2, 955, 420, 30), paint(AMBER, 0.3, blur=14))
    peca(c)
    vitrine_vidro(c, W / 2, 955, 860, 560, 1.0)
    lume(c, 300, 1050, 2.4, pose(look=(1.0, -0.4), brow=0.9, brow_y=0.7, o_mouth=True, mouth=0.6))
    texto_capa(c, frase, W / 2, 250, 210 if len(frase) < 12 else 170)
    img = surf.makeImageSnapshot()
    s2 = skia.Surface(1280, 720)
    s2.getCanvas().drawImageRect(img, skia.Rect.MakeWH(1280, 720), skia.SamplingOptions(skia.CubicResampler.Mitchell()))
    s2.makeImageSnapshot().save(str(OUT / f"{nome}.jpg"), skia.kJPEG, 92)
    print("ok", nome)


def peca_celular(c):
    peca_001(c, W / 2, 760, 2.0, 3.0, tela=0.0, raiox=0.0)


def peca_celular_raiox(c):
    peca_001(c, W / 2, 760, 2.0, 3.0, raiox=1.0, bateria=1.0)


def peca_osso(c):
    glow(c, W / 2, 700, 420, AMBER, 0.5)
    icone(c, "osso", W / 2, 700, 7.5, None, 1.0)


def avatar():
    surf = skia.Surface(800, 800)
    c = surf.getCanvas()
    c.drawRect(skia.Rect.MakeWH(800, 800), radial(400, 360, 560, ["#2e47c9", "#14206b"], [0, 1]))
    glow(c, 410, 170, 260, AMBER, 0.55)
    c.drawOval(oval(400, 735, 230, 26), paint(AMBER, 0.25, blur=10))
    lume(c, 400, 735, 3.0, pose(look=(0.15, -0.05), smile=0.85, cheek=0.6))
    surf.makeImageSnapshot().save(str(OUT / "avatar_800.png"), skia.kPNG)
    print("ok avatar")


def marca_dagua():
    surf = skia.Surface(150, 150)
    c = surf.getCanvas()
    c.clear(skia.ColorTRANSPARENT)
    c.drawCircle(75, 75, 72, paint("#14206b", 0.85))
    lume(c, 75, 132, 0.58, pose(smile=0.8))
    surf.makeImageSnapshot().save(str(OUT / "marca_dagua_150.png"), skia.kPNG)
    print("ok marca")


def banner():
    BW, BH = 2560, 1440
    surf = skia.Surface(BW, BH)
    c = surf.getCanvas()
    c.save()
    c.scale(BW / W, BH / H)
    salao(c, 3.0, titulo=None)
    for x, tipo in ((330, "garrafa"), (1590, "osso")):
        holofote(c, x, 72, 600, 40, 260, 0.8)
    c.restore()
    c.drawRect(skia.Rect.MakeWH(BW, BH), paint("#0a1240", 0.35))
    # área segura (aparece em todos os aparelhos): 1546 x 423 no centro
    sx, sy, sw, sh = (BW - 1546) / 2, (BH - 423) / 2, 1546, 423
    c.drawRRect(rr(sx + 380, sy + 40, 1140, 340, 30), paint("#0a1240", 0.55))
    logo(c, sx + 950, sy + 200, 1.15, 1.0, sub="CIÊNCIA DO NOSSO TEMPO, CONTADA DE 2526")
    glow(c, sx + 200, sy + 140, 260, AMBER, 0.4)
    lume(c, sx + 200, sy + 410, 1.5, pose(look=(0.9, -0.2), smile=0.9, arm_r=2.6))
    surf.makeImageSnapshot().save(str(OUT / "banner_2560x1440.png"), skia.kPNG)
    # prévia com a área segura marcada (só para conferir)
    c.drawRect(skia.Rect.MakeXYWH(sx, sy, sw, sh), paint("#ffffff", 0.9, stroke=4, cap_round=False))
    surf.makeImageSnapshot().save(str(OUT / "banner_area_segura.png"), skia.kPNG)
    print("ok banner")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    miniatura("miniatura_A_nos_ruinas", "NÓS = RUÍNAS", peca_celular)
    miniatura("miniatura_B_10000_anos", "DAQUI A 10.000 ANOS", peca_celular_raiox)
    miniatura("miniatura_C_era_do_frango", "A ERA DO FRANGO?", peca_osso)
    avatar()
    marca_dagua()
    banner()
