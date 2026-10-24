"""Capas do vídeo Tecnologia 010 — Claude Duet (tema 'tech'). 3 variações em 1280x720.
Só motion graphics, sem captura de tela; logo = ícone oficial do app (logo_claude_duet.svg, de claude.com/product/claude-duet).
Telas do Duet = mockup com selo ILUSTRATIVO."""
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


def base(c, col=CYAN, tag="IA · AGENTE PROATIVO · ANTHROPIC"):
    tech.background(c, 3.0)
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        tech._bracket(c, x, y, dx, dy, col, 0.7)
    chip(c, tag, 84, 110, col, 1, size=34, filled=True)


def logo(c, x, y, size):
    d = skia.SVGDOM.MakeFromStream(skia.Stream.MakeFromFile(str(HERE / "logo_claude_duet.svg")))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, size, size), size * .22, size * .22), blur_paint("#000000", 0.5, 24))
    c.save(); c.translate(x, y); c.scale(size / 1024, size / 1024); d.render(c); c.restore()


def rodape(c, s, size, icone=True):
    """ícone do Claude Duet + linha de apoio, sem invadir o painel da direita"""
    x = 90
    if icone:
        logo(c, 84, 724, 132)
        x = 246
    size = min(size, size * (1076 - x) / text_w(s, "monob", size))
    text(c, s, x, 806, size, "monob", INK2, align="left")


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


def lado_notif(c):
    """celular com notificações do Duet — mockup"""
    x, y, w, h = 1140, 150, 680, 760
    panel(c, x, y, w, h, 1, CYAN, label="duet · mockup")
    text(c, "08:00", x + w / 2, y + 140, 96, "black", INK, 1)
    text(c, "o que importa hoje", x + w / 2, y + 195, 28, "mono", INK2, 1)
    items = [("BRIEF DA MANHÃ", "3 e-mails pedem resposta", CYAN), ("ALERTA", "Reunião marcada no dia errado", ROSE),
             ("APROVAÇÃO", "Enviar lembrete de fatura?", GOLD)]
    for k, (t1, t2, col) in enumerate(items):
        V.notif(c, x + 40, y + 260 + k * 150, w - 80, 1, t1, t2, col, 30)
    V.selo(c, x + w / 2, y + h + 50, 1, "ILUSTRATIVO", anchor="center", size=24)


def lado_aprovacao(c):
    x, y, w, h = 1140, 150, 680, 760
    panel(c, x, y, w, h, 1, GOLD, label="exige aprovação")
    for k, s in enumerate(("ENVIAR", "PAGAR", "ASSINAR", "APAGAR")):
        yy = y + 150 + k * 125
        V.ic_lock(c, x + 100, yy - 18, 64, GOLD, 1)
        glow_text(c, s, x + 170, yy + 10, 72, "black", INK, 1, align="left", glow=0.15)
    chip(c, "PROIBIDO: TRANSFERIR ENTRE CONTAS", x + w / 2, y + 680, ROSE, 1, anchor="center", size=24, filled=True)


def lado_fluxo(c):
    x, y, w, h = 1140, 150, 680, 760
    panel(c, x, y, w, h, 1, VIOLET, label="como funciona")
    labs = (("APPS", CYAN), ("DUET", VIOLET), ("VOCÊ APROVA", GOLD), ("AÇÃO", LIME))
    for k, (lab, col) in enumerate(labs):
        cy = y + 120 + k * 180
        if k:
            link(c, x + 150, cy - 180 + 62, x + 150, cy - 62, labs[k - 1][1], 1, 0.3, pulses=3)
        node(c, x + 150, cy, 62, None, None, col, 1, 0.0)
        text(c, lab, x + 250, cy + 18, 50, "black", INK, 1, align="left")


def capa_antes(c):
    base(c, CYAN)
    big(c, "A IA QUE TRABALHA", "ANTES DE VOCÊ", "PEDIR", CYAN)
    rodape(c, "Claude Duet, da Anthropic", 44)
    lado_notif(c)


def capa_aprova(c):
    base(c, GOLD, "CLAUDE DUET · SEGURANÇA")
    big(c, "ELE AGE SOZINHO,", "MAS PEDE", "AUTORIZAÇÃO", GOLD)
    rodape(c, "o que o Claude Duet faz e o que é proibido", 40)
    lado_aprovacao(c)


def capa_nome(c):
    base(c, VIOLET, "NOVO · ANTHROPIC · 21/10/2026")
    big(c, "CLAUDE", "DUET", "CHEGOU", VIOLET)
    logo(c, 690, 205, 270)   # ícone grande ao lado do nome
    rodape(c, "brief · alertas · tarefas na nuvem", 44, icone=False)
    lado_fluxo(c)


if __name__ == "__main__":
    for nome, fn in (("capa_A_trabalha_antes", capa_antes), ("capa_B_pede_autorizacao", capa_aprova),
                     ("capa_C_claude_duet", capa_nome)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
