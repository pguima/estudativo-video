"""Estudos de visual do canal: folha da Lume, salão do museu, vitrine da peça 001 e o mundo quente.
python estudo.py [saida_dir]  → lume_folha.png, salao.png, peca001.png, recon.png"""
import sys
from pathlib import Path
import skia
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "_ferramentas"))
from antigos import *  # noqa: E402,F403

# vitrines do salão (mundo = plano geral 1920x1080): cx, topo do pedestal, largura, altura do vidro, escala
CENTRAL = dict(cx=960, top=640, w=340, h=300)
LATERAIS = [dict(cx=330, top=610, w=230, h=200, obj="garrafa"), dict(cx=1590, top=610, w=230, h=200, obj="osso")]


def peca_lateral(c, tipo, cx, base):
    if tipo == "garrafa":  # garrafa PET amassada
        c.drawPath(poly([(cx - 26, base - 10), (cx - 30, base - 90), (cx - 12, base - 120), (cx - 10, base - 140),
                         (cx + 10, base - 140), (cx + 12, base - 120), (cx + 34, base - 96), (cx + 24, base - 10)]),
                   paint("#9fe3ff", 0.55))
        c.drawRRect(rr(cx - 12, base - 156, 24, 18, 4), paint("#3a7bd5"))
        c.drawRect(skia.Rect.MakeLTRB(cx - 30, base - 70, cx + 30, base - 46), paint(CORAL, 0.8))
    else:  # osso de frango
        c.save()
        c.translate(cx, base - 40)
        c.rotate(-24)
        c.drawRRect(rr(-50, -8, 100, 16, 8), paint(BONE))
        for ex in (-52, 52):
            c.drawCircle(ex, -8, 13, paint(BONE))
            c.drawCircle(ex, 8, 13, paint(BONE))
        c.restore()


def mundo(c, t, st):
    """o salão inteiro. st: dict com luz (0..1 do holofote central), salao (0..1 das outras luzes),
    lume = (x, y, s, pose) ou None, e os efeitos da peça (tela, raiox, bateria)"""
    salao(c, t, titulo=st.get("titulo", "ALA 01 · O QUE SOBROU"), titulo_a=st.get("titulo_a", 1.0))
    # o salão fica no escuro até o holofote central acender
    luz_salao = st.get("salao", 1.0)
    for v in LATERAIS:
        holofote(c, v["cx"], 72, v["top"], 40, v["w"] * 1.1, 0.75 * luz_salao)
        pedestal(c, v["cx"], v["top"], v["w"] + 30, 200, None, 0.75 * luz_salao)
        peca_lateral(c, v["obj"], v["cx"], v["top"] - 6)
        vitrine_vidro(c, v["cx"], v["top"], v["w"], v["h"], t)
    if luz_salao < 1:
        c.drawRect(skia.Rect.MakeLTRB(0, 0, W, H + 400), paint("#0a1240", 0.82 * (1 - luz_salao)))
    v, luz = CENTRAL, st.get("luz", 1.0)
    holofote(c, v["cx"], 72, v["top"], 50, v["w"] * 1.25, luz)
    pedestal(c, v["cx"], v["top"], v["w"] + 40, 230, "PEÇA Nº 001 · c. 2026 d.C.", luz)
    c.drawOval(oval(v["cx"], v["top"] - 2, v["w"] * 0.5, 14), paint(AMBER, 0.25 * luz, blur=10))
    peca_001(c, v["cx"], v["top"] - 100, 0.92, t, st.get("tela", 0), st.get("raiox", 0), st.get("bateria", 0), luz)
    vitrine_vidro(c, v["cx"], v["top"], v["w"], v["h"], t)
    poeira(c, t, (v["cx"] - 170, 90, v["cx"] + 170, v["top"]), 46, seed=2, a=0.55 * luz, zoom=st.get("zoom", 1))
    if luz_salao > 0:
        for i, lv in enumerate(LATERAIS):
            poeira(c, t, (lv["cx"] - 110, 90, lv["cx"] + 110, lv["top"]), 18, seed=10 + i, a=0.4 * luz_salao)
    if st.get("lume"):
        x, y, s, p = st["lume"]
        lume(c, x, y, s, p)


def salvar(surf, caminho):
    surf.makeImageSnapshot().save(str(caminho), skia.kPNG)
    print("ok", caminho)


def tela_salao(out):
    surf = skia.Surface(W, H)
    c = surf.getCanvas()
    c.save()
    camera(c, 960, 560, 1.0)
    mundo(c, 3.0, dict(lume=(640, 880, 1.25, pose(look=(0.8, -0.3), brow=0.6, arm_r=2.2, smile=0.8))))
    c.restore()
    logo(c, W / 2, 160, 0.62, 0.0)
    vinheta(c, 0.6)
    salvar(surf, out / "salao.png")


def tela_peca(out):
    surf = skia.Surface(W, H)
    c = surf.getCanvas()
    c.save()
    camera(c, 960, 520, 2.7)
    mundo(c, 3.0, dict(salao=0.0, raiox=1.0, bateria=1.0, zoom=2.7))
    c.restore()
    vinheta(c, 0.8)
    salvar(surf, out / "peca001.png")


def tela_recon(out):
    surf = skia.Surface(W, H)
    c = surf.getCanvas()
    cidade_quente(c, 2.0)
    # a Lume também entra nas reconstituições: visitante do futuro olhando o passado
    c.drawRect(skia.Rect.MakeLTRB(0, 1000, W, H), paint("#4a52b8"))
    c.drawRect(skia.Rect.MakeLTRB(0, 1000, W, 1008), paint("#8a93ff"))
    lume(c, 330, 1030, 1.5, pose(face=1, look=(0.7, -0.6), brow=0.8, brow_y=0.5, smile=0.9, arm_r=2.3))
    rotulo(c, "SÉCULO 21", 330, 610, CORAL)
    rotulo(c, "8 BILHÕES", 1560, 200, AMBER)
    vinheta(c, 0.25)
    salvar(surf, out / "recon.png")


def tela_folha(out):
    """folha de personagem: Lume grande + expressões + escala + paleta"""
    surf = skia.Surface(W, H)
    c = surf.getCanvas()
    c.drawRect(skia.Rect.MakeWH(W, H), linear(0, 0, 0, H, ["#0e1e2a", INK]))
    text(c, "A LUME · CURADORA DO MUSEU DA ERA DOS ANTIGOS", 80, 92, 22, "mono", 500, AMBER, tracking=0.2)
    text(c, "Folha de personagem", 80, 160, 60, "display", 800, BONE)
    # a Lume grande, com holofote
    c.drawOval(oval(400, 860, 260, 40), paint(AMBER, 0.12, blur=20))
    lume(c, 400, 860, 2.6, pose(look=(0.35, -0.1), smile=0.7))
    # notas com linha até a parte (posições = pontos da Lume na escala 2.6)
    for s, (px, py), (tx, ty) in (("LANTERNA NA ANTENA", (442, 390), (560, 300)), ("UM OLHO GRANDE", (470, 640), (640, 560)),
                                  ("CRACHÁ DE CURADORA", (322, 746), (250, 600)), ("PÉS CURTOS", (340, 850), (250, 960))):
        c.drawCircle(px, py, 5, paint(AMBER))
        c.drawLine(px, py, tx, ty + 6, paint(AMBER, 0.6, stroke=1.5))
        text(c, s, tx + (8 if tx > px else -8), ty, 15, "mono", 500, BONE, align="left" if tx > px else "right", tracking=0.12)
    # expressões
    exps = [("neutra", pose()),
            ("curiosa", pose(brow=0.9, brow_y=0.6, look=(0.6, -0.5), smile=0.4)),
            ("falando", pose(mouth=0.7, smile=0.6, brow_y=0.3)),
            ("surpresa", pose(o_mouth=True, mouth=0.8, brow_y=1.0, look=(0, -0.2), squash=-0.06)),
            ("preocupada", pose(brow=-0.9, lid=0.25, smile=-0.4, look=(-0.4, 0.3), tilt=-0.08)),
            ("apresentando", pose(arm_r=2.4, arm_l=0.5, smile=0.9, mouth=0.35, brow_y=0.4)),
            ("acenando", pose(arm_r=2.9, smile=1.0, lid=0.15, tilt=0.06)),
            ("olhando a peça", pose(face=-1, look=(0.8, 0.2), brow=0.5, smile=0.3))]
    for i, (nome, p) in enumerate(exps):
        col, lin = i % 4, i // 4
        x, y = 900 + col * 250, 470 + lin * 330
        c.drawRRect(rr(x - 110, y - 300, 220, 310, 14), paint(VAULT, 0.9))
        c.drawRRect(rr(x - 110, y - 300, 220, 310, 14), paint(LINE, 1, stroke=1.5))
        lume(c, x, y - 50, 1.05, p)
        text(c, nome.upper(), x, y - 16, 15, "mono", 500, DUST, align="center", tracking=0.14)
    # paleta
    cores = [("Corpo", LUME["corpo"]), ("Sombra", LUME["sombra"]), ("Traço", LUME["sombra2"]), ("Lanterna", LUME["lanterna"]),
             ("Crachá", LUME["cracha"]), ("Salão", INK), ("Osso", BONE)]
    for i, (n, cor) in enumerate(cores):
        x = 900 + i * 140
        c.drawRRect(rr(x - 110 + 20, 960, 110, 36, 6), paint(cor))
        c.drawRRect(rr(x - 110 + 20, 960, 110, 36, 6), paint(LINE, stroke=1.5))
        text(c, f"{n} {cor.upper()}", x - 90, 1024, 12, "mono", 500, DUST)
    salvar(surf, out / "lume_folha.png")


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "estudos"
    out.mkdir(parents=True, exist_ok=True)
    for f in (tela_folha, tela_salao, tela_peca, tela_recon):
        f(out)
