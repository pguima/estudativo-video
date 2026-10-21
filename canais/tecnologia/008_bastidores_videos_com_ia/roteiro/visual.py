"""Visual do vídeo Tecnologia 008 — Bastidores: como eu faço estes vídeos com IA. Tema 'tech' (futurista).
Mostra peças REAIS do projeto: trechos de cenas.py, palavras com tempo do Whisper, quadros e capas de vídeos já publicados
(assets/: enem.png, seguridade.png, tecnologia.png, capa1-3.jpg, folha.png)."""
import math
from pathlib import Path
import skia
import motor
import tech
from motor import *  # noqa
from tech import *  # noqa

tech.SERIE = "TECH//008 · BASTIDORES"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_008_bastidores_videos_com_ia.mp4"
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay

ASSETS = Path(__file__).resolve().parent.parent / "assets"
_IMG = {}
KW, NM, TX, NUM, STR = VIOLET, CYAN, INK, GOLD, LIME


def rise(t, t0, d=0.5):
    a = ep(t, t0, d)
    return a, (1 - a) * 24


def img(name):
    if name not in _IMG:
        _IMG[name] = skia.Image.open(str(ASSETS / name))
    return _IMG[name]


def picture(c, name, x, y, w, a, col=CYAN, label=None):
    """imagem real dentro de um painel chanfrado"""
    if a <= 0:
        return
    im = img(name)
    h = w * im.height() / im.width()
    panel(c, x - 12, y - 12, w + 24, h + 24, a, col, k=16, label=label)
    p = skia.Paint(AntiAlias=True)
    p.setAlphaf(a)
    c.drawImageRect(im, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), p)
    return h


def wave(c, x, y, w, h, a, t, col=CYAN, n=60, live=True):
    if a <= 0:
        return
    for i in range(n):
        u = i / n
        amp = (0.25 + 0.75 * abs(math.sin(i * 0.7 + (t * 6 if live else 0)) * math.sin(i * 0.23 + 1.3))) * h / 2
        x0 = x + u * w
        c.drawLine(x0, y - amp, x0, y + amp, paint(col, a * 0.85, stroke=max(2, w / n * 0.55), cap_round=True))


def strike_x(c, x0, y, x1, col, a, prog_=1.0):
    if a > 0:
        glow_line(c, x0, y, lerp(x0, x1, prog_), y, col, a, 5)


PIPE = [("ROTEIRO", "Claude Code", CYAN), ("VOZ", "Gemini TTS", MAGENTA), ("TRANSCRIÇÃO", "faster-whisper", VIOLET),
        ("ANIMAÇÃO", "Skia", LIME), ("RENDER", "ffmpeg", GOLD)]


def pipeline(c, t, cues, y=480, sub=False, a_all=1.0):
    xs = [260 + k * 350 for k in range(5)]
    for k, (lab, tool, col) in enumerate(PIPE):
        a = ep(t, cues[k], 0.5) * a_all
        if k > 0:
            link(c, xs[k - 1] + 80, y, xs[k] - 80, y, PIPE[k - 1][2], min(a, ep(t, cues[k - 1], 0.5) * a_all), t,
                 progress=ep(t, cues[k], 0.6))
        node(c, xs[k], y, 70, lab, tool if sub else None, col, a, t, glyph=str(k + 1), gsize=48)


# ======================================================================
def b_hook(c, t, C, B):
    items = [("01.a", "CÂMERA", 380), ("01.b", "MICROFONE", 960), ("01.c", "EDITOR DE VÍDEO", 1540)]
    ad = ep(t, C["01.d"], 0.5)
    for cue, s, x in items:
        a = ep(t, C[cue], 0.4) * (1 - 0.6 * ad)
        if a <= 0:
            continue
        chip(c, s, x, 300, ROSE, a, anchor="center", size=40)
        w = text_w(s, "monob", 40) + 52
        strike_x(c, x - w / 2 - 10, 300, x + w / 2 + 10, ROSE, a, ep(t, C[cue] + 0.4, 0.4))
    if ad > 0:
        glow_text(c, "CÓDIGO + IA", W / 2, 500, 110, "black", CYAN, ad, glow=0.5)
    ae = ep(t, C["01.e"], 0.5)
    stats = [("53", "vídeos"), ("~7 h", "de aula"), ("4", "canais")]
    for k, (n, s) in enumerate(stats):
        a = ae * ep(t, C["01.e"] + 0.6 * k, 0.4)
        x = 560 + k * 400
        if a <= 0:
            continue
        panel(c, x - 170, 590, 340, 200, a, (CYAN, MAGENTA, LIME)[k], k=18)
        glow_text(c, n, x, 700, 76, "black", INK, a, glow=0.25)
        text(c, s, x, 760, 30, "mono", DIM, a)
    chip(c, "OS BASTIDORES", W / 2, 860, GOLD, ep(t, C["01.f"], 0.5), anchor="center", size=30, filled=True)


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "O PIPELINE", "CINCO ETAPAS")
    pipeline(c, t, [C["02.a"], C["02.b"], C["02.c"], C["02.d"], C["02.e"]], 480)
    chip(c, "+ O QUE DEU ERRADO", W / 2, 760, ROSE, ep(t, C["02.f"], 0.5), anchor="center", size=32, filled=True)


def b_roteiro(c, t, C, B):
    head(c, t, B["start"], "ETAPA 1 · ROTEIRO", "DO MATERIAL AO CENAS.PY", CYAN)
    a0 = ep(t, C["03.t"], 0.5)
    if a0 > 0:
        panel(c, 150, 260, 470, 520, a0, DIM, label="apostila.html")
        for i in range(11):
            rrect(c, 190, 320 + i * 40, 390 * (0.55 + 0.4 * hash01(i, 2)), 14, 7, "#22304F", a0)
    aa = ep(t, C["03.a"], 0.5)
    node(c, 790, 500, 80, "Claude Code", "lê e escreve", CYAN, aa, t, glyph="AI", gsize=46)
    link(c, 630, 500, 700, 500, CYAN, aa, t)
    ab = ep(t, C["03.b"], 0.5)
    link(c, 880, 500, 960, 500, CYAN, ab, t)
    if ab > 0:
        lines = [[("SCENES", NM), (" = [", TX)],
                 [("  dict(", TX), ("id", KW), ("=", TX), ('"08"', STR), (", ", TX), ("block", KW), ("=", TX), ('"sindico"', STR), (",", TX)],
                 [("    text", KW), ("=", TX), ('"E agora o *campeão* de prova: "', STR)],
                 [('         "o *síndico!* [p=0.5] "', STR)],
                 [('         "{a}Síndico *remunerado?*"', STR), ("),", TX)],
                 [("  dict(", TX), ("id", KW), ("=", TX), ('"09"', STR), (", ...", TX)],
                 [("]", TX)]]
        panel(c, 960, 260, 820, 520, ab, CYAN, label="cenas.py")
        code_lines(c, lines, 995, 340, 25, t, C["03.b"] + 0.2, step=0.15, lh=46, a=ab)
    chip(c, "1 cena = 1 item da lista", 1370, 830, CYAN, ep(t, C["03.c"], 0.5), anchor="center", size=26)


def b_marcas(c, t, C, B):
    head(c, t, B["start"], "ETAPA 1 · ROTEIRO", "AS MARCAÇÕES", CYAN)
    a0 = ep(t, C["04.t"], 0.5)
    parts = [("{a}", CYAN, "04.a"), ("Síndico ", INK, None), ("*remunerado?*", MAGENTA, "04.b"), (" ", INK, None),
             ("[p=0.2]", GOLD, "04.c"), (" Contribuinte individual.", INK, None)]
    size = 44
    tot = sum(text_w(s, "monob", size) for s, _, _ in parts)
    x = W / 2 - tot / 2
    if a0 > 0:
        panel(c, 150, 300, 1620, 140, a0, DIM, k=18, label="cenas.py")
    pos = {}
    for s, col, cue in parts:
        hl = ep(t, C[cue], 0.4) if cue else 0
        ccol = mix(INK, col, hl) if cue else INK
        w = text(c, s, x, 390, size, "monob", ccol, a0, align="left")
        if cue:
            pos[cue] = x + w / 2
            if hl > 0:
                c.drawRect(skia.Rect.MakeXYWH(x - 4, 400, w + 8, 6), paint(col, hl))
        x += w
    expl = [("04.a", "GATILHO", "uma animação começa nesta palavra", CYAN),
            ("04.b", "DESTAQUE", "a palavra brilha na legenda", MAGENTA),
            ("04.c", "PAUSA", "0,2 segundo de respiro", GOLD)]
    for k, (cue, lab, s, col) in enumerate(expl):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        xx = 380 + k * 580
        link(c, pos.get(cue, xx), 420, xx, 520, col, a, t, pulses=1)
        panel(c, xx - 250, 530, 500, 170, a, col, k=16)
        text(c, lab, xx, 590, 30, "monob", col, a, tracking=2)
        text(c, s, xx, 650, 28, "bold", INK, a)
    chip(c, "o roteiro já sabe ONDE cada coisa acontece", W / 2, 790, LIME, ep(t, C["04.d"], 0.5), anchor="center", size=28, filled=True)


def b_fidelidade(c, t, C, B):
    head(c, t, B["start"], "REGRA DE OURO", "A IA NÃO INVENTA", LIME)
    aa = ep(t, C["05.a"], 0.5)
    for k, s in enumerate(("citações", "leis", "números")):
        chip(c, s, 420 + k * 300, 300, LIME, aa * ep(t, C["05.a"] + 0.4 * k, 0.3), anchor="center", size=32)
    text(c, "têm que estar no material", 1440, 312, 34, "bold", INK, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        panel(c, 150, 420, 760, 360, ab, DIM, label="material original")
        panel(c, 1010, 420, 760, 360, ab, CYAN, label="roteiro")
        rows = ["“tema = delimitação de um assunto…”", "“A partir da leitura dos textos…”", "Caminhos para combater a…"]
        for i, s in enumerate(rows):
            y = 520 + i * 80
            text(c, s, 190, y, 26, "mono", INK2, ab, align="left")
            text(c, s, 1050, y, 26, "mono", INK, ab, align="left")
            ok = ep(t, C["05.b"] + 1.0 + 0.6 * i, 0.3)
            if ok > 0:
                link(c, 860, y - 8, 1040, y - 8, LIME, ok, t, pulses=1)
                text(c, "OK", 950, y - 22, 22, "monob", LIME, ok)
        u = (t * 0.5) % 1
        c.drawLine(150, 450 + u * 320, 1770, 450 + u * 320, blur_paint(CYAN, 0.5 * ab, 4, stroke=2))


def b_voz(c, t, C, B):
    head(c, t, B["start"], "ETAPA 2 · VOZ", "GEMINI TTS NO MEU COMPUTADOR", MAGENTA)
    aa = ep(t, C["06.a"], 0.5)
    node(c, 1460, 460, 90, "Gemini TTS Studio", "localhost:3000", MAGENTA, ep(t, C["06.b"], 0.5), t, glyph="TTS", gsize=40)
    ac = ep(t, C["06.c"], 0.5)
    if ac > 0:
        terminal(c, 150, 250, 960, 470, ac, "gerar_voz_local.py", MAGENTA)
        lines = [[("POST ", KW), ("/api/tts/generate", NM)],
                 [("{", TX)],
                 [('  "text": ', TX), ('"parte 1 do roteiro…"', STR), (",", TX)],
                 [('  "voiceName": ', TX), ('"Neno"', STR), (",", TX)],
                 [('  "tags": ', TX), ('["alegre", "curiosa"]', STR), (",", TX)],
                 [('  "customPrompt": ', TX), ('"professor apaixonado…"', STR)],
                 [("}", TX)]]
        cues = [C["06.c"], C["06.c"] + 0.3, C["06.c"] + 0.6, C["06.d"], C["06.e"], C["06.f"], C["06.f"] + 0.3]
        for i, segs in enumerate(lines):
            ai = ep(t, cues[i], 0.3) * ac
            xx = 190
            for s, col in segs:
                xx += text(c, s, xx, 340 + i * 50, 26, "mono", col, ai, align="left")
        link(c, 1110, 460, 1360, 460, MAGENTA, ep(t, C["06.d"], 0.5), t)
    ag = ep(t, C["06.g"], 0.5)
    if ag > 0:
        wave(c, 1250, 720, 440, 120, ag, t, MAGENTA)
        text(c, "a voz que você está ouvindo agora", 1470, 830, 28, "bold", MAGENTA, ag)


def b_voz_erros(c, t, C, B):
    head(c, t, B["start"], "ETAPA 2 · VOZ", "A VOZ DE IA APRONTA", ROSE)
    rows = [("07.a", "leu um trecho DUAS VEZES"), ("07.b", "INVENTOU uma frase"), ("07.c", "modelo reserva → OUTRA VOZ")]
    for k, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 140 + d
        panel(c, 250, y - 50, 1420, 100, a, ROSE, k=14)
        check_icon(c, 310, y, 22, a, ROSE, "x")
        text(c, s, 360, y + 14, 42, "black", INK, a, align="left")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        terminal(c, 400, 700, 1120, 140, ad, "bash", LIME)
        text(c, "parte 2: veio …-lite-tts, tentando de novo", 440, 800, 28, "mono", GOLD, ad, align="left")


def b_whisper(c, t, C, B):
    head(c, t, B["start"], "ETAPA 3 · TRANSCRIÇÃO", "FASTER-WHISPER", VIOLET)
    aa = ep(t, C["08.a"], 0.5)
    wave(c, 160, 420, 600, 220, aa, t, MAGENTA)
    ab = ep(t, C["08.b"], 0.5)
    link(c, 780, 420, 900, 420, VIOLET, ab, t)
    if ab > 0:
        chip(c, 'WhisperModel("small", device="cpu")', 160, 620, VIOLET, ab, size=24)
    ac = ep(t, C["08.c"], 0.5)
    if ac > 0:
        panel(c, 920, 250, 860, 520, ac, VIOLET, label="palavras.json")
        words = [("A", "0.00"), ("redação", "0.44"), ("começa", "0.90"), ("antes", "1.26"), ("da", "1.96"),
                 ("primeira", "2.06"), ("linha.", "2.42")]
        for i, (w_, s) in enumerate(words):
            ai = ep(t, C["08.c"] + 0.25 * i, 0.3) * ac
            y = 330 + i * 60
            text(c, w_, 980, y, 34, "monob", INK, ai, align="left")
            text(c, s + " s", 1700, y, 34, "monob", GOLD, ai, align="right")


def b_diff(c, t, C, B):
    head(c, t, B["start"], "ETAPA 3 · CONFERÊNCIA", "ROTEIRO × TRANSCRIÇÃO", VIOLET)
    aa, ab = ep(t, C["09.a"], 0.5), ep(t, C["09.b"], 0.5)
    if aa > 0:
        panel(c, 150, 250, 760, 400, aa, CYAN, label="roteiro")
    if ab > 0:
        panel(c, 1010, 250, 760, 400, ab, VIOLET, label="transcrição")
    rot = ["Isso é a tese:", "a sua posição sobre o tema.", "O tema é dado pela prova"]
    voz = ["Isso é a tese:", "a sua posição sobre o tema.", "a sua posição sobre o tema.", "O tema é dado pela prova"]
    for i, s in enumerate(rot):
        text(c, s, 190, 340 + i * 60 + (60 if i == 2 else 0), 30, "mono", INK, aa, align="left")
    ac = ep(t, C["09.c"], 0.4)
    for i, s in enumerate(voz):
        bad = i == 2
        if bad and ac > 0:
            rrect(c, 1040, 340 + i * 60 - 36, 700, 50, 6, ROSE, 0.25 * ac)
        text(c, s, 1050, 340 + i * 60, 30, "mono", ROSE if (bad and ac > 0.5) else INK, ab, align="left")
    chip(c, "SOBROU → repetição: CORTA", 1050, 610, ROSE, ac, size=24, filled=True)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        panel(c, 150, 700, 1620, 130, ad, GOLD, k=16)
        for i in range(40):
            gap = 14 <= i < 24
            x = 200 + i * 38
            if not gap:
                rrect(c, x, 745, 30, 40, 4, VIOLET, ad * 0.8)
        text(c, "7 s sem palavras", 200 + 19 * 38, 778, 30, "monob", GOLD, ad)
        chip(c, "A VOZ ESTAVA CERTA → retranscrevi o trecho", W / 2, 860, LIME, ep(t, C["09.e"], 0.5), anchor="center", size=26, filled=True)


def b_alinha(c, t, C, B):
    head(c, t, B["start"], "O PULO DO GATO", "CADA GATILHO VIRA UM INSTANTE", CYAN)
    aa = ep(t, C["10.a"], 0.5)
    words = ["Síndico", "remunerado?", "Contribuinte", "individual.", "E", "se,", "em", "vez", "de", "salário,"]
    xs, x = [], 220
    for w_ in words:
        xs.append(x)
        x += text_w(w_, "monob", 24) + 34
    if aa > 0:
        panel(c, 150, 300, 1620, 300, aa, CYAN, k=18, label="tempos.json")
        line(c, 200, 520, 1720, 520, DIM, aa, 2)
        for i, w_ in enumerate(words):
            x = xs[i]
            ai = ep(t, C["10.a"] + 0.15 * i, 0.3) * aa
            c.drawLine(x, 505, x, 535, paint(CYAN, ai, stroke=3))
            text(c, w_, x, 470, 24, "monob", INK, ai, align="left")
            if i % 2 == 0:
                text(c, f"{1.2 + 0.42 * i:.2f} s", x, 570, 20, "mono", DIM, ai, align="left")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        for k, (lab, i) in enumerate((("{a}", 0), ("{b}", 4))):
            x = xs[i]
            y = lerp(380, 400, ab)
            chip(c, lab, x - 8, y - 40, GOLD, ab, size=24, filled=True)
            glow_line(c, x, y - 20, x, 520, GOLD, ab, 3)
    pill_a = ep(t, C["10.c"], 0.5)
    chip(c, "a animação acontece BEM NA PALAVRA", W / 2, 720, LIME, pill_a, anchor="center", size=32, filled=True)


def b_skia(c, t, C, B):
    head(c, t, B["start"], "ETAPA 4 · ANIMAÇÃO", "O QUADRO É FUNÇÃO DO TEMPO", LIME)
    aa = ep(t, C["11.a"], 0.5) * (1 - ep(t, C["11.b"], 0.4))
    if aa > 0:
        for k, s in enumerate(("linha do tempo", "arrastar caixinha")):
            x = 640 + k * 640
            chip(c, s, x, 450, ROSE, aa, anchor="center", size=40)
            w = text_w(s, "monob", 40) + 52
            strike_x(c, x - w / 2 - 10, 450, x + w / 2 + 10, ROSE, aa, ep(t, C["11.a"] + 0.6, 0.4))
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        lines = [[("def ", KW), ("b_cena", NM), ("(c, t, C, B):", TX)],
                 [("    x = ", TX), ("lerp", NM), ("(300, 1500, ", TX), ("ep", NM), ("(t, C[", TX), ('"02.a"', STR), ("]))", TX)],
                 [("    c.", TX), ("drawCircle", NM), ("(x, 500, ", TX), ("60", NUM), (", tinta)", TX)]]
        panel(c, 150, 260, 900, 330, ab, LIME, label="visual.py")
        code_lines(c, lines, 190, 360, 27, t, C["11.b"] + 0.2, step=0.3, lh=62, a=ab)
    ac = ep(t, C["11.c"], 0.5)
    if ac > 0:
        panel(c, 1110, 260, 660, 330, ac, LIME, label="quadro")
        u = (math.sin(t * 1.4) + 1) / 2
        x = 1170 + u * 540
        c.drawCircle(x, 450, 40, blur_paint(MAGENTA, 0.6 * ac, 12))
        c.drawCircle(x, 450, 32, paint(MAGENTA, ac))
        text(c, f"t = {t % 60:05.2f} s", 1440, 560, 32, "monob", GOLD, ac)
        chip(c, "Skia · a biblioteca 2D do Chrome", 1110, 650, LIME, ac, size=24)
    chip(c, "mudou o tempo → muda o desenho", W / 2, 790, CYAN, ep(t, C["11.d"], 0.5), anchor="center", size=30, filled=True)


def b_temas(c, t, C, B):
    head(c, t, B["start"], "CADA CANAL, UM ESTILO", "QUADROS REAIS", LIME)
    shots = [("12.a", "enem.png", "AULAS ENEM", CYAN), ("12.b", "seguridade.png", "SEGURIDADE SOCIAL", LIME),
             ("12.c", "tecnologia.png", "TECNOLOGIA", VIOLET)]
    for k, (cue, f, lab, col) in enumerate(shots):
        a, d = rise(t, C[cue])
        x = 165 + k * 545
        picture(c, f, x, 300 + d, 500, a, col, lab)
    ad = ep(t, C["12.d"], 0.5)
    for k, s in enumerate(("motor.py", "aula.py", "tech.py")):
        chip(c, s, 640 + k * 320, 700, CYAN, ad * ep(t, C["12.d"] + 0.3 * k, 0.3), anchor="center", size=30, filled=True)
    text(c, "bibliotecas compartilhadas", W / 2, 790, 30, "mono", DIM, ad)


def b_legenda(c, t, C, B):
    head(c, t, B["start"], "A LEGENDA", "PALAVRA POR PALAVRA", MAGENTA)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        panel(c, 260, 300, 1400, 300, aa, MAGENTA, k=18, label="caption()")
        words = [("cada", False), ("palavra", False), ("aparece", False), ("NA", True), ("HORA", True)]
        x = 360
        for i, (w_, hl) in enumerate(words):
            ai = ep(t, C["13.a"] + 0.35 * i, 0.25) * aa
            if hl:
                w = glow_text(c, w_, x, 480, 60, "black", CYAN, ai, align="left", glow=0.6)
            else:
                w = text(c, w_, x, 480, 60, "bold", INK, ai, align="left")
            x += w + 28
    ab = ep(t, C["13.b"], 0.5)
    chip(c, "*asterisco* → brilha", W / 2, 700, CYAN, ab, anchor="center", size=34, filled=True)


def b_render(c, t, C, B):
    head(c, t, B["start"], "ETAPA 5 · RENDER", "DEZOITO MIL QUADROS", GOLD)
    aa = ep(t, C["14.a"], 0.5)
    glow_text(c, "30 fps", 420, 380, 90, "black", INK, aa, glow=0.3)
    ab = ep(t, C["14.b"], 0.5)
    glow_text(c, "10 min = 18.000 quadros", 1200, 380, 64, "black", GOLD, ab, glow=0.3)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        n = 30
        for i in range(n):
            x = 160 + i * 53
            fill = clamp((t - C["14.d"] - (i // 3) * 0.55) / 1.2) if t > C["14.d"] else 0
            rrect(c, x, 520, 46, 90, 6, "#111A30", acc)
            if fill > 0:
                rrect(c, x, 520 + 90 * (1 - fill), 46, 90 * fill, 6, (CYAN, MAGENTA, LIME)[i % 3], acc)
        text(c, "pedaços de 20 s", 160, 660, 28, "mono", DIM, acc, align="left")
    ad = ep(t, C["14.d"], 0.5)
    chip(c, "3 processos desenhando ao mesmo tempo", 160, 720, CYAN, ad, size=26)
    ae = ep(t, C["14.e"], 0.5)
    node(c, 1600, 700, 70, "ffmpeg", "+ narração", GOLD, ae, t, glyph="MP4", gsize=36)


def b_ram(c, t, C, B):
    head(c, t, B["start"], "A VIDA REAL", "OITO GIGAS DE MEMÓRIA", ROSE)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        panel(c, 150, 260, 1620, 220, aa, DIM, k=18, label="RAM 8 GB")
    over = ep(t, C["15.b"], 0.6) * (1 - ep(t, C["15.d"], 0.5))
    ok = ep(t, C["15.d"], 0.5)
    n = int(round(lerp(0, 7, over))) if over > 0 else (3 if ok > 0 else 0)
    for i in range(7):
        on_ = i < n
        if not on_:
            continue
        col = ROSE if (over > 0.5 and i >= 5) else (LIME if ok > 0 else CYAN)
        rrect(c, 200 + i * 220, 330, 200, 100, 10, col, aa * 0.85)
        text_mid(c, f"proc {i + 1}", 300 + i * 220, 380, 26, "monob", "#03050B", aa)
    acc = ep(t, C["15.c"], 0.4) * (1 - ok)
    if acc > 0:
        terminal(c, 400, 560, 1120, 140, acc, "bash", ROSE)
        text(c, "MemoryError", 440, 660, 40, "monob", ROSE, acc, align="left")
    chip(c, "hoje: --jobs 3", 400, 620, LIME, ok, size=34, filled=True)
    chip(c, "falhou? --retomar refaz só os pedaços que faltam", 400, 720, CYAN, ep(t, C["15.e"], 0.5), size=26)


def b_previa(c, t, C, B):
    head(c, t, B["start"], "ANTES DO RENDER", "UMA FOLHA DE PRÉVIA", CYAN)
    aa = ep(t, C["16.a"], 0.5)
    fw_ = 500
    h = picture(c, "folha.png", 710, 250, fw_, aa, CYAN, "trabalho/sheet_01.png")
    ac = ep(t, C["16.c"], 0.5)
    if ac > 0 and h:
        # destaca uma célula (a seta da cena 04 que foi corrigida)
        cw, ch = fw_ / 3, h / 6
        x, y = 710, 250 + ch
        c.drawRect(skia.Rect.MakeXYWH(x, y, cw, ch), paint(ROSE, ac, stroke=5))
        chip(c, "seta no lugar errado", x - 20, y + ch / 2, ROSE, ac, anchor="right", size=24, filled=True)
    chip(c, "corrige ANTES de gastar o render", 1390, 760, LIME, ep(t, C["16.d"], 0.5), size=26, filled=True)


def b_capas(c, t, C, B):
    head(c, t, B["start"], "PRONTO PARA PUBLICAR", "CAPAS E DESCRIÇÃO", GOLD)
    aa = ep(t, C["17.a"], 0.5)
    for k, f in enumerate(("capa1.jpg", "capa2.jpg", "capa3.jpg")):
        a = aa * ep(t, C["17.a"] + 0.3 * k, 0.4)
        picture(c, f, 170 + k * 360, 280, 320, a, GOLD, f"capa {'ABC'[k]}" if k == 0 else None)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        panel(c, 1270, 260, 500, 520, ab, GOLD, label="publicacao.md")
        rows = [("## Título", VIOLET), ("## Descrição", VIOLET), ("## Tags", VIOLET), ("## Capítulos", CYAN)]
        for i, (s, col) in enumerate(rows):
            text(c, s, 1310, 340 + i * 60, 28, "monob", col, ab, align="left")
        acc = ep(t, C["17.c"], 0.5)
        for i, s in enumerate(("00:00 A banca descreve…", "00:19 Art. 11…", "00:37 O empregado")):
            text(c, s, 1310, 590 + i * 50, 24, "mono", GOLD, acc, align="left")
    chip(c, "capítulos calculados dos tempos da narração", 170, 720, GOLD, ep(t, C["17.c"], 0.5), size=26)


def b_humano(c, t, C, B):
    head(c, t, B["start"], "ENTÃO A IA FAZ TUDO?", "NÃO!", ROSE)
    ab, db = rise(t, C["18.b"])
    if ab > 0:
        panel(c, 200, 280 + db, 700, 420, ab, CYAN, label="EU")
        for i, s in enumerate(("escolho o tema", "defino o estilo", "aprovo cada etapa")):
            check_icon(c, 260, 380 + i * 90 + db, 20, ab, CYAN)
            text(c, s, 300, 394 + i * 90 + db, 40, "black", INK, ab, align="left")
    ac, dc = rise(t, C["18.c"])
    if ac > 0:
        panel(c, 1020, 280 + dc, 700, 420, ac, MAGENTA, label="IA")
        text(c, "o trabalho", 1370, 450 + dc, 50, "black", INK, ac)
        glow_text(c, "PESADO", 1370, 540 + dc, 80, "black", MAGENTA, ac, glow=0.4)
    chip(c, "o critério continua sendo MEU", W / 2, 790, LIME, ep(t, C["18.d"], 0.5), anchor="center", size=32, filled=True)


def b_cuidados(c, t, C, B):
    head(c, t, B["start"], "SE VOCÊ QUISER FAZER", "TRÊS CUIDADOS", GOLD)
    rows = [("19.a", "FONTE CONFIÁVEL", "e não deixe a IA inventar", LIME),
            ("19.b", "CONFIRA A VOZ", "sempre", CYAN),
            ("19.c", "SEJA TRANSPARENTE", "declare a narração sintética", GOLD)]
    for k, (cue, s, sub, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 160 + d
        panel(c, 250, y - 60, 1420, 120, a, col, k=16)
        glow_text(c, str(k + 1), 320, y + 22, 64, "black", col, a, glow=0.4)
        text(c, s, 400, y + 16, 46, "black", INK, a, align="left")
        text(c, sub, 1620, y + 14, 30, "mono", DIM, a, align="right")


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMINDO", "CINCO FERRAMENTAS, UMA PASTA", LIME)
    pipeline(c, t, [C["20.a"], C["20.b"], C["20.c"], C["20.d"], C["20.e"]], 460, sub=True)
    chip(c, "1 vídeo = 1 pasta", W / 2, 800, CYAN, ep(t, C["20.f"], 0.5), anchor="center", size=32, filled=True)


def b_cta(c, t, C, B):
    tech.cta(c, t, C["21.like"], C["21.sub"], C["21.bell"], C["21.com"], C["21.bye"],
             "Qual etapa você quer ver em detalhe?")
    a = ep(t, B["start"], 0.5) * (1 - prog(t, C["21.like"] - 0.4, 0.4))
    if a > 0:
        glow_text(c, "roteiro → voz → whisper → skia → ffmpeg", W / 2, 540, 48, "black", INK, a, glow=0.3)


BLOCKS = dict(hook=b_hook, mapa=b_mapa, roteiro=b_roteiro, marcas=b_marcas, fidelidade=b_fidelidade, voz=b_voz,
              voz_erros=b_voz_erros, whisper=b_whisper, diff=b_diff, alinha=b_alinha, skia=b_skia, temas=b_temas,
              legenda=b_legenda, render=b_render, ram=b_ram, previa=b_previa, capas=b_capas, humano=b_humano,
              cuidados=b_cuidados, resumo=b_resumo, cta=b_cta)
