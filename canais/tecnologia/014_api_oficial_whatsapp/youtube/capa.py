"""Capas do vídeo Tecnologia 014 — API oficial do WhatsApp (tema 'tech'). 3 variações em 1280x720.
Sem logos: o WhatsApp aparece só como texto e balões desenhados aqui. Preços = tabela oficial da Meta em BRL (01/10/2026)."""
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


def base(c, col=CYAN, tag="WHATSAPP · API OFICIAL DA META"):
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


def lado_precos(c):
    panel(c, PX, PY, PW, PH, 1, GOLD, label="tabela oficial · BRL · 01/10/2026")
    rows = [("MARKETING", "R$ 0,3217", MAGENTA), ("UTILIDADE", "R$ 0,035", CYAN), ("AUTENTICAÇÃO", "R$ 0,035", VIOLET),
            ("ATENDIMENTO", "1.000 GRÁTIS", LIME)]
    for k, (nm, v, col) in enumerate(rows):
        y = PY + 140 + k * 150
        text(c, nm, PX + 60, y - 40, 30, "monob", col, 1, align="left")
        glow_text(c, v, PX + 60, y + 40, 76 if k < 3 else 64, "black", INK, 1, align="left", glow=0.2)
    text(c, "por mensagem · números do Brasil", PX + PW / 2, PY + PH - 40, 26, "mono", INK2, 1)


def lado_multi(c):
    panel(c, PX, PY, PW, PH, 1, MAGENTA, label="multiatendimento")
    cx = PX + PW / 2
    V.ic_phone(c, cx, PY + 190, 220, V.WA, 1)
    glow_text(c, "1 NÚMERO", cx, PY + 370, 64, "black", V.WA, 1, glow=0.3)
    for k in range(4):
        x = PX + 105 + k * 157
        link(c, cx, PY + 400, x, PY + 520, MAGENTA, 1, 2.0, pulses=0)
        V.ic_person(c, x, PY + 570, 100, (CYAN, LIME, GOLD, VIOLET)[k], 1)
    glow_text(c, "VÁRIOS", cx, PY + 710, 64, "black", INK, 1, glow=0.2)


def lado_passos(c):
    panel(c, PX, PY, PW, PH, 1, CYAN, label="configuração")
    for k, s in enumerate(("Portfólio da Meta", "App no Developers", "Número", "Token permanente", "Webhook",
                           "Multiatendimento")):
        y = PY + 110 + k * 110
        c.drawCircle(PX + 90, y - 12, 34, paint(PANEL)); c.drawCircle(PX + 90, y - 12, 34, paint(CYAN, stroke=4))
        text_mid(c, str(k + 1), PX + 90, y - 12, 38, "black", CYAN)
        text(c, s, PX + 150, y, 44, "bold", INK, 1, align="left")


def capa_preco(c):
    base(c, GOLD)
    big(c, "QUANTO CUSTA", "A API OFICIAL", "DO WHATSAPP?", V.WA)
    text(c, "preços da Meta em reais · out/2026", 90, 800, 42, "monob", INK2, align="left")
    lado_precos(c)


def capa_multi(c):
    base(c, MAGENTA, "WHATSAPP · CLOUD API · MULTIATENDIMENTO")
    big(c, "1 NÚMERO,", "VÁRIOS", "ATENDENTES", MAGENTA)
    text(c, "API oficial + sistema de atendimento", 90, 800, 40, "monob", INK2, align="left")
    lado_multi(c)


def capa_passos(c):
    base(c, CYAN, "WHATSAPP · CLOUD API · PASSO A PASSO")
    big(c, "API OFICIAL DO", "WHATSAPP:", "DO ZERO", CYAN)
    text(c, "custo, configuração e multiatendimento", 90, 800, 42, "monob", INK2, align="left")
    lado_passos(c)


if __name__ == "__main__":
    for nome, fn in (("capa_A_quanto_custa", capa_preco), ("capa_B_um_numero_varios_atendentes", capa_multi),
                     ("capa_C_do_zero", capa_passos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
