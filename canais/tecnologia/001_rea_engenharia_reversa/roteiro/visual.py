"""Visual do vídeo Tecnologia 001 — REA: engenharia reversa com agentes de IA. Tema 'tech' (futurista)."""
import math
import skia
import tech
from motor import *  # noqa
from tech import *  # noqa

tech.SERIE = "TECH//001 · REA"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_001_rea_engenharia_reversa.mp4"
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay

HEX = ["55 48 89 E5 48 83 EC 20", "8B 45 FC 0F AF 45 F8 89", "C7 45 F4 00 00 80 3F F3", "0F 10 45 F4 F3 0F 59 C1",
       "E8 2A 01 00 00 48 8B 4D", "F0 31 C0 85 C9 74 0B 83", "F9 5B 74 1E 83 F9 5C 74", "48 83 C4 20 5D C3 CC CC"]


def hexdump(c, x, y, t, a, rows=8, size=26, col=None, scroll=True):
    col = col or INK2
    off = (t * 1.5) if scroll else 0
    for i in range(rows):
        k = int(i + off) % len(HEX)
        addr = f"{0x401000 + (int(i + off)) * 16:08X}"
        text(c, addr, x, y + i * 40, size, "mono", DIM, a, align="left")
        text(c, HEX[k], x + 170, y + i * 40, size, "mono", col, a, align="left")


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.6)
    panel(c, 170, 220, 760, 520, a0, CYAN, label="app.exe")
    hexdump(c, 220, 320, t, a0)
    q = 0.5 + 0.5 * math.sin(t * 3)
    glow_text(c, "?", 1290, 470, 220, "black", VIOLET, a0 * ep(t, B["start"] + 0.8, 0.5) * (1 - ep(t, C["01.c"], 0.4)), glow=0.4 + 0.3 * q)
    aa = ep(t, C["01.a"], 0.5)
    chip(c, "CÓDIGO-FONTE: INDISPONÍVEL", 1290, 560, ROSE, aa * (1 - ep(t, C["01.c"], 0.4)), anchor="center", size=26)
    ab = ep(t, C["01.b"], 0.5)
    chip(c, "SÓ O BINÁRIO COMPILADO", 550, 790, GOLD, ab, anchor="center", size=24)
    ac = ep(t, C["01.c"], 0.6)
    if ac > 0:
        # feixe de varredura sobre o binário
        sy = 300 + (t * 160) % 340
        c.drawRect(skia.Rect.MakeXYWH(190, sy, 720, 4), blur_paint(CYAN, 0.8 * ac, 6))
        node(c, 1290, 360, 90, None, None, CYAN, ac, t, glyph="AI", gsize=56)
        text(c, "AGENTE DE IA", 1290, 495, 30, "monob", CYAN, ac)
        link(c, 1195, 360, 935, 420, CYAN, ac, t, progress=ep(t, C["01.c"] + 0.3, 0.6))
        panel(c, 1040, 560, 560, 210, ep(t, C["01.c"] + 1.2, 0.5), LIME, k=18, label="rebuild.c")
        code_lines(c, [[("int ", VIOLET), ("feature", CYAN), ("(int x) {", INK2)],
                       [("  return ", VIOLET), ("x * 2 + 1", INK), (";", INK2)], [("}", INK2)]],
                   1080, 640, 28, t, C["01.c"] + 1.5, a=ep(t, C["01.c"] + 1.2, 0.5))


def b_intro(c, t, C, B):
    a0 = ep(t, C["02.a"], 0.6)
    cx = W / 2
    glow_text(c, "REA", cx, 470, 260, "black", INK, a0, glow=0.0)
    glow_text(c, "REA", cx, 470, 260, "black", CYAN, a0 * (0.35 + 0.15 * math.sin(t * 2)), glow=0.9)
    ex = ep(t, C["02.a"] + 1.0, 0.7)
    for k, (w, col) in enumerate((("Reverse", CYAN), ("Engineer", VIOLET), ("Anything", MAGENTA))):
        a = ep(t, C["02.a"] + 1.0 + 0.35 * k, 0.5)
        x = cx - 520 + k * 520
        glow_text(c, w, x, 590, 54, "black", col, a, glow=0.35)
    text(c, "engenharia reversa de qualquer coisa", cx, 660, 34, "mono", INK2, ex)
    ab = ep(t, C["02.b"], 0.5)
    chip(c, "OPEN SOURCE", cx - 330, 760, LIME, ab, anchor="center", size=28)
    chip(c, "LICENÇA MIT", cx - 30, 760, LIME, ep(t, C["02.b"] + 0.4, 0.5), anchor="center", size=28)
    acs = ep(t, C["02.c"], 0.5)
    if acs > 0:
        n = int(250000 * ease_out(prog(t, C["02.c"], 1.8)))
        s = f"{n:,}+".replace(",", ".")
        chip(c, s + " ESTRELAS", cx + 380, 760, GOLD, acs, anchor="center", size=28, filled=True)
    chip(c, "github.com/morluto/rea", cx, 215, DIM, ep(t, B["start"] + 0.3, 0.5), anchor="center", size=24)


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "ROTEIRO", "NESTE VÍDEO")
    items = [("03.a", "O QUE É", "engenharia reversa", CYAN), ("03.b", "COMO FUNCIONA", "REA + seu agente", VIOLET),
             ("03.c", "ALVOS", "o que dá para analisar", CYAN), ("03.d", "EXEMPLOS", "3 casos reais", MAGENTA),
             ("03.e", "INSTALAÇÃO", "npx rea-agents setup", LIME), ("03.f", "CUIDADOS", "uso legal", ROSE)]
    for k, (cue, t1, t2, col) in enumerate(items):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + (k % 3) * 550
        y = 260 + (k // 3) * 290 + dy
        panel(c, x, y, 500, 230, a, col)
        glow_text(c, f"0{k + 1}", x + 40, y + 90, 60, "black", col, a, align="left", glow=0.4)
        text(c, t1, x + 40, y + 155, 38, "black", INK, a, align="left")
        text(c, t2, x + 40, y + 198, 26, "mono", INK2, a, align="left")


def b_compila(c, t, C, B):
    head(c, t, B["start"], "O CONCEITO", "DO CÓDIGO AO BINÁRIO")
    aa = ep(t, B["start"] + 0.4, 0.5)
    panel(c, 150, 240, 660, 470, aa, VIOLET, label="calc.c")
    gone = ep(t, C["04.b"], 0.8)
    lines = [[("// aplica a porcentagem", mix(LIME, "#1B2440", gone))],
             [("float ", VIOLET), ("aplicaPercentual", mix(CYAN, "#1B2440", gone)), ("(", INK2)],
             [("    float ", VIOLET), ("total", mix(INK, "#1B2440", gone)), (", float ", VIOLET), ("pct", mix(INK, "#1B2440", gone)), (") {", INK2)],
             [("  return ", VIOLET), ("total * pct / 100", INK), (";", INK2)], [("}", INK2)]]
    code_lines(c, lines, 190, 340, 28, t, B["start"] + 0.6, a=aa)
    if gone > 0:
        text(c, "nomes e comentários: PERDIDOS", 480, 650, 28, "monob", ROSE, gone)
    ac = ep(t, C["04.a"], 0.5)
    arrow(c, 840, 420, 1080, 420, CYAN, ac, 4, 18, progress=ep(t, C["04.a"], 0.7))
    text(c, "COMPILAR", 960, 395, 22, "monob", CYAN, ac)
    panel(c, 1110, 240, 660, 470, ac, CYAN, label="calc.exe")
    hexdump(c, 1160, 340, t, ac, rows=8, size=24)
    ar = ep(t, C["04.c"], 0.5)
    if ar > 0:
        p = skia.Path(); p.moveTo(1440, 730); p.quadTo(960, 860, 480, 730)
        pr = ep(t, C["04.c"], 1.0)
        g = paint(MAGENTA, ar, stroke=5, cap_round=True)
        g.setPathEffect(skia.DashPathEffect.Make([1600 * pr + 1, 4000], 0))
        c.drawPath(p, blur_paint(MAGENTA, 0.5 * ar, 8, stroke=10))
        c.drawPath(p, g)
        chip(c, "ENGENHARIA REVERSA ◄", 960, 800, MAGENTA, ep(t, C["04.c"] + 0.5, 0.5), anchor="center", size=28, filled=True)


def b_ferramentas(c, t, C, B):
    head(c, t, B["start"], "O JEITO TRADICIONAL", "FERRAMENTAS PESADAS")
    tools = [("05.a", "Ghidra"), ("05.b", "IDA"), ("05.c", "Hopper")]
    e = ep(t, C["05.e"], 0.6)
    for k, (cue, name) in enumerate(tools):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 1130
        y = 230 + k * 150 + dy
        panel(c, x, y, 560, 120, a, GOLD, k=16)
        glow_text(c, name, x + 280, y + 76, 48, "black", INK, a, glow=0.1)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        terminal(c, 150, 230, 860, 420, ad * (1 - e), "disassembly", GOLD)
        asm = [("push", "rbp"), ("mov", "rbp, rsp"), ("sub", "rsp, 0x20"), ("cmp", "ecx, 0x5b"), ("je", "0x401a3e"),
               ("cmp", "ecx, 0x5c"), ("mulss", "xmm0, xmm1")]
        off = int(t * 2) % len(asm)
        for i in range(7):
            op, arg = asm[(i + off) % len(asm)]
            a = ad * (1 - e)
            text(c, op, 200, 330 + i * 44, 28, "monob", GOLD, a, align="left")
            text(c, arg, 340, 330 + i * 44, 28, "mono", INK2, a, align="left")
        chip(c, "HORAS LENDO ASSEMBLY", 580, 700, GOLD, ad * (1 - e), anchor="center", size=26)
    if e > 0:
        node(c, 420, 420, 100, "AGENTE DE IA", None, CYAN, e, t, glyph="AI", gsize=58)
        glow_line(c, 530, 420, 1120, 420, CYAN, e, 4, progress=ep(t, C["05.e"] + 0.3, 0.8))
        chip(c, "REA = PONTE", 820, 380, CYAN, ep(t, C["05.e"] + 0.8, 0.5), anchor="center", size=30, filled=True)
        text(c, "não substitui as ferramentas", 820, 480, 28, "mono", INK2, ep(t, C["05.e"] + 0.8, 0.5))


def b_mcp(c, t, C, B):
    head(c, t, B["start"], "COMO FUNCIONA", "UM SERVIDOR MCP")
    a0 = ep(t, B["start"] + 0.3, 0.6)
    node(c, W / 2, 480, 130, "REA", "servidor MCP", CYAN, a0, t, glyph="MCP", gsize=56)
    aa = ep(t, C["06.a"], 0.5)
    chip(c, "MODEL CONTEXT PROTOCOL", W / 2, 260, VIOLET, aa, anchor="center", size=26)
    text(c, "padrão para agentes de IA usarem ferramentas externas", W / 2, 320, 28, "mono", INK2, aa)
    agentes = ["Claude Code", "Codex", "Cursor", "Gemini CLI"]
    for k, nome in enumerate(agentes):
        a = ep(t, C["06.b"] + 0.55 * k, 0.5)
        y = 410 + k * 100
        panel(c, 190, y - 38, 360, 76, a, VIOLET, k=14, glow=False)
        text_mid(c, nome, 370, y, 32, "bold", INK, a)
        link(c, 555, y, W / 2 - 120, 480, VIOLET, a, t, progress=ep(t, C["06.b"] + 0.55 * k + 0.2, 0.5), pulses=2)
    ac = ep(t, C["06.c"], 0.5)
    if ac > 0:
        panel(c, 1370, 380, 360, 200, ac, CYAN, label="programa")
        hexdump(c, 1400, 450, t, ac, rows=3, size=20)
        link(c, W / 2 + 125, 480, 1365, 480, CYAN, ac, t, progress=ep(t, C["06.c"], 0.6), pulses=3)
        chip(c, "INSPECIONAR", 1550, 640, CYAN, ac, anchor="center", size=24, filled=True)


def b_fluxo(c, t, C, B):
    head(c, t, B["start"], "O FLUXO", "TRÊS PASSOS")
    steps = [("07.s1", "VOCÊ", "pergunta + programa", VIOLET, "?"), ("07.s2", "REA", "inspeciona e rastreia", CYAN, "</>"),
             ("07.s3", "EVIDÊNCIAS", "código · instruções", LIME, "{ }"), ("07.s4", "AGENTE", "explica · testa", MAGENTA, "AI")]
    xs = [300, 740, 1180, 1620]
    for k, (cue, lab, sub, col, g) in enumerate(steps):
        a = ep(t, C[cue], 0.55)
        if a <= 0:
            continue
        node(c, xs[k], 450, 105, lab, sub, col, a, t, glyph=g, gsize=70 if len(g) == 1 else 54)
        if k < 3:
            num = f"0{k + 1}"
            glow_text(c, num, xs[k], 290, 34, "monob", col, a, glow=0.4)
        if k > 0:
            link(c, xs[k - 1] + 110, 450, xs[k] - 110, 450, steps[k - 1][3], a, t, progress=ep(t, C[cue] - 0.2, 0.5))
    a4 = ep(t, C["07.s4"] + 1.0, 0.5)
    chip(c, "EXPLICAR", 1520, 760, MAGENTA, a4, anchor="center", size=24)
    chip(c, "ESCREVER + TESTAR", 1720, 760, MAGENTA, ep(t, C["07.s4"] + 1.8, 0.5), anchor="center", size=24, filled=True)


def b_evidencia(c, t, C, B):
    head(c, t, B["start"], "O PONTO MAIS IMPORTANTE", "EVIDÊNCIA, NÃO PALPITE", LIME)
    aa = ep(t, C["08.a"], 0.5)
    chip(c, "EVIDÊNCIA", 1000, 150, LIME, aa, anchor="center", size=26, filled=True)
    chip(c, "LIMITAÇÕES", 1260, 150, GOLD, ep(t, C["08.a"] + 0.8, 0.5), anchor="center", size=26, filled=True)
    ab, dyb = reveal(t, C["08.b"])
    if ab > 0:
        panel(c, 150, 260 + dyb, 780, 440, ab, LIME, label="DADOS DO REA")
        rows = [("código", "sub_401a20  · 63 bytes"), ("instruções", "cmp ecx, 0x5c"), ("chamadas", "→ sub_4019f0"),
                ("desconhecido", "rótulo 0x5b sem nome")]
        for i, (k, v) in enumerate(rows):
            a = ep(t, C["08.b"] + 0.3 + 0.35 * i, 0.4)
            text(c, k.upper(), 200, 370 + i * 80, 24, "monob", LIME if i < 3 else GOLD, a, align="left")
            text(c, v, 430, 370 + i * 80, 28, "mono", INK, a, align="left")
    ac, dyc = reveal(t, C["08.c"])
    if ac > 0:
        panel(c, 990, 260 + dyc, 780, 440, ac, VIOLET, label="INTERPRETAÇÃO DO AGENTE")
        for i, s in enumerate(("“Este trecho decide o", "comportamento do % conforme", "o operador anterior.”")):
            text(c, s, 1040, 380 + i * 56 + dyc, 34, "semibold", INK2, ep(t, C["08.c"] + 0.4 * i, 0.4), align="left")
        chip(c, "→ apoiada em 3 evidências", 1040, 600 + dyc, VIOLET, ep(t, C["08.c"] + 1.5, 0.5), size=24)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        glow_text(c, "VOCÊ VÊ A PROVA.", W / 2, 800, 64, "black", LIME, ad, glow=0.5)


def b_alvos(c, t, C, B):
    head(c, t, B["start"], "ALVOS", "O QUE DÁ PARA ANALISAR")
    tiles = [("09.a1", ".exe  .dll", "binários nativos", CYAN), ("09.a2", "Go · Rust", "binários compilados", CYAN),
             ("09.a3", "JS · Electron", "apps desktop e web", VIOLET), ("09.a4", ".NET", "assemblies", VIOLET),
             ("09.a5", "Android", "APK e dispositivo", LIME), ("09.a6", "Web", "sites no navegador", LIME)]
    for k, (cue, big, sub, col) in enumerate(tiles):
        a, dy = reveal(t, C[cue], 0.45)
        if a <= 0:
            continue
        x = 150 + (k % 3) * 550
        y = 230 + (k // 3) * 210 + dy
        panel(c, x, y, 500, 180, a, col, k=18)
        glow_text(c, big, x + 40, y + 92, 52, "black", INK, a, align="left", glow=0.12)
        text(c, sub, x + 40, y + 145, 26, "mono", col, a, align="left")
    extra = ["WebAssembly", "Ethereum (EVM)", "SQLite", "firmware", "captura de rede"]
    for k, s in enumerate(extra):
        a = ep(t, C["09.a7"] + 0.45 * k, 0.4)
        chip(c, s, 270 + k * 345, 720, MAGENTA, a, anchor="center", size=26)
    chip(c, "~25 TIPOS DE ALVO", W / 2, 800, MAGENTA, ep(t, C["09.a7"] + 2.6, 0.5), anchor="center", size=26, filled=True)


def b_local(c, t, C, B):
    head(c, t, B["start"], "PRIVACIDADE", "TUDO RODA LOCALMENTE", LIME)
    a0 = ep(t, B["start"] + 0.3, 0.6)
    # "máquina" no centro
    panel(c, 700, 240, 520, 300, a0, LIME, label="localhost")
    glow_text(c, "127.0.0.1", 960, 380, 64, "black", LIME, a0, glow=0.4)
    text(c, "sua máquina", 960, 450, 30, "mono", INK2, a0)
    for k in range(4):
        r = 190 + 50 * ((t * 0.6 + k / 4) % 1)
        c.drawCircle(960, 390, r, paint(LIME, a0 * 0.25 * (1 - ((t * 0.6 + k / 4) % 1)), stroke=2))
    aa, dya = reveal(t, C["10.a"])
    if aa > 0:
        panel(c, 150, 590 + dya, 780, 200, aa, CYAN, k=18)
        text(c, "ESTÁTICO · JS e .NET", 200, 660 + dya, 34, "black", CYAN, aa, align="left")
        text(c, "só lê os arquivos, sem executar", 200, 720 + dya, 30, "mono", INK, aa, align="left")
    ab, dyb = reveal(t, C["10.b"])
    if ab > 0:
        panel(c, 990, 590 + dyb, 780, 200, ab, GOLD, k=18)
        text(c, "TEMPO DE EXECUÇÃO", 1040, 660 + dyb, 34, "black", GOLD, ab, align="left")
        text(c, "roda o programa com SUAS permissões", 1040, 720 + dyb, 30, "mono", INK, ab, align="left")


def b_calc(c, t, C, B):
    head(c, t, B["start"], "EXEMPLO 01", "CALCULADORA DO WINDOWS", CYAN)
    a0 = ep(t, B["start"] + 0.4, 0.6)
    panel(c, 150, 220, 440, 600, a0, CYAN, label="Calculator x64")
    rrect(c, 180, 270, 380, 110, 10, "#060B16", a0)
    hi = (t - C["11.c"]) if t >= C["11.c"] else (t - C["11.b"])
    disp = "20" if t >= C["11.c2"] else "220" if t >= C["11.b2"] else "200"
    glow_text(c, disp, 540, 355, 70, "black", INK, a0, align="right", glow=0.15)
    keys = ["7", "8", "9", "÷", "4", "5", "6", "×", "1", "2", "3", "+", "0", "%", ".", "="]
    for i, k in enumerate(keys):
        kx = 185 + (i % 4) * 95
        ky = 405 + (i // 4) * 95
        is_pct = k == "%"
        on = is_pct and t >= C["11.t"] + 2.5
        col = CYAN if on else "#13203A"
        rrect(c, kx, ky, 80, 80, 12, col, a0 * (0.9 if on else 1))
        if on:
            c.drawRect(skia.Rect.MakeXYWH(kx, ky, 80, 80), blur_paint(CYAN, 0.5 * a0 * (0.6 + 0.4 * math.sin(t * 5)), 14))
        text_mid(c, k, kx + 40, ky + 40, 36, "bold", "#03050B" if on else INK2, a0)
    aa = ep(t, C["11.a"], 0.5)
    chip(c, "2 REGRAS NO BINÁRIO", 700, 250, CYAN, aa, size=26)
    ab, dyb = reveal(t, C["11.b"])
    if ab > 0:
        panel(c, 680, 310 + dyb, 1090, 200, ab, LIME, k=18, label="DEPOIS DO +")
        text(c, "% do primeiro número", 720, 395 + dyb, 30, "mono", INK2, ab, align="left")
        glow_text(c, "200 + 10% = 220", 720, 470 + dyb, 54, "black", LIME, ep(t, C["11.b2"], 0.5), align="left", glow=0.3)
    ac, dyc = reveal(t, C["11.c"])
    if ac > 0:
        panel(c, 680, 560 + dyc, 1090, 200, ac, MAGENTA, k=18, label="DEPOIS DO × (OU ÷)")
        text(c, "10% vira 0,1", 720, 645 + dyc, 30, "mono", INK2, ac, align="left")
        glow_text(c, "200 × 10% = 20", 720, 720 + dyc, 54, "black", MAGENTA, ep(t, C["11.c2"], 0.5), align="left", glow=0.3)
    ad = ep(t, C["11.d"], 0.5)
    chip(c, "MESMA TECLA · 2 COMPORTAMENTOS", 1225, 820, GOLD, ad, anchor="center", size=26, filled=True)


def b_dino(c, t, C, B):
    head(c, t, B["start"], "EXEMPLO 02", "O JOGO DO DINOSSAURO", LIME)
    a0 = ep(t, B["start"] + 0.4, 0.6)
    gx, gy, gw, gh = 210, 250, 900, 480
    panel(c, gx - 60, gy - 30, gw + 120, gh + 110, a0, LIME, label="velocidade × atualizações")
    line(c, gx, gy + gh, gx + gw, gy + gh, DIM, a0, 2)
    line(c, gx, gy, gx, gy + gh, DIM, a0, 2)
    def Y(v):
        return gy + gh - (v - 4) / 11 * gh
    def X(u):
        return gx + u / 12000 * gw
    for v in (6, 10, 13):
        text(c, str(v), gx - 18, Y(v) + 10, 24, "mono", DIM, a0, align="right")
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        c.drawCircle(X(0), Y(6), 9, paint(LIME, aa))
        chip(c, "início: 6", X(0) + 30, Y(6) + 6, LIME, aa, size=24)
    ab = ep(t, C["12.b"], 1.6)
    if ab > 0:
        n = int(60 * ab)
        p = skia.Path(); p.moveTo(X(0), Y(6))
        for i in range(1, n + 1):
            u = i / 60 * 12000
            p.lineTo(X(u), Y(min(13, 6 + 0.001 * u)))
        c.drawPath(p, blur_paint(LIME, 0.5, 6, stroke=10))
        c.drawPath(p, paint(LIME, 1, stroke=4, cap_round=True))
        chip(c, "+0,001 por atualização", X(2600), Y(10) - 70, LIME, ep(t, C["12.b"], 0.5), anchor="center", size=24)
    ac = ep(t, C["12.c"], 0.5)
    if ac > 0:
        line(c, gx, Y(13), gx + gw, Y(13), ROSE, ac, 2.5, dash=[12, 8])
        chip(c, "teto: 13", X(10500), Y(13) - 34, ROSE, ac, anchor="center", size=24, filled=True)
    ad, dyd = reveal(t, C["12.d"])
    if ad > 0:
        panel(c, 1240, 250 + dyd, 520, 510, ad, CYAN, label="minijogo")
        ground = 560 + dyd
        line(c, 1270, ground, 1730, ground, INK2, ad, 2)
        jump = max(0, math.sin(((t * 1.1) % 1) * math.pi)) * 90 if (t * 1.1) % 2 < 1 else 0
        rrect(c, 1330, ground - 70 - jump, 56, 70, 6, LIME, ad)
        ox = 1730 - ((t * 260) % 460)
        rrect(c, ox, ground - 60, 26, 60, 4, ROSE, ad)
        text(c, "VELOCIDADE", 1290, 640 + dyd, 24, "monob", CYAN, ad, align="left")
        sv = 0.25 + 0.6 * (0.5 + 0.5 * math.sin(t * 0.8))
        bar_meter(c, 1290, 670 + dyd, 420, 14, sv, CYAN, ad)
        c.drawCircle(1290 + 420 * sv, 677 + dyd, 16, paint(INK, ad))


def b_dxball(c, t, C, B):
    head(c, t, B["start"], "EXEMPLO 03", "DX-BALL (1996)", MAGENTA)
    a0 = ep(t, B["start"] + 0.4, 0.6)
    ax, ay, aw, ah = 150, 230, 760, 520
    panel(c, ax, ay, aw, ah, a0, MAGENTA, label="DXBALL.EXE")
    for r in range(4):
        for k in range(9):
            cols = (ROSE, GOLD, LIME, CYAN)
            rrect(c, ax + 40 + k * 76, ay + 50 + r * 34, 68, 26, 4, cols[r], a0 * 0.85)
    u = 0.5 + 0.5 * math.sin(t * 1.3)
    bx = ax + 60 + u * (aw - 120)
    by = ay + 260 + 120 * abs(math.sin(t * 2.6))
    aa = ep(t, C["13.a"], 0.5)
    c.drawCircle(bx, by, 14, blur_paint(INK, 0.6 * a0, 8))
    c.drawCircle(bx, by, 12, paint(INK, a0))
    rrect(c, bx - 70, ay + ah - 50, 140, 18, 9, MAGENTA, a0)
    if aa > 0:
        # caixas de som L e R
        for side, xx in ((0, ax + aw + 50), (1, ax + aw + 170)):
            lvl = (1 - u) if side == 0 else u
            text(c, "L" if side == 0 else "R", xx + 40, ay + 60, 34, "black", INK, aa)
            for b in range(8):
                on = b < lvl * 8
                rrect(c, xx, ay + 380 - b * 40, 80, 30, 4, MAGENTA if on else "#1A2440", aa)
        text(c, "posição → pan", ax + aw + 165, ay + 470, 26, "mono", INK2, aa)
    ab, dyb = reveal(t, C["13.b"])
    if ab > 0:
        panel(c, 1240, 230 + dyb, 530, 250, ab, CYAN, k=18, label="pan.c")
        code_lines(c, [[("int ", VIOLET), ("pan", CYAN), ("(int x) {", INK2)],
                       [("  return ", VIOLET), ("(x - 320)", INK), (" * k;", INK2)], [("}", INK2)]],
                   1280, 320 + dyb, 28, t, C["13.b"] + 0.3)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        n = int(3205 * ease_out(prog(t, C["13.c"], 2.0)))
        text(c, "TESTES", 1240, 560, 26, "monob", LIME, acc, align="left")
        glow_text(c, f"{n:,}/3.205".replace(",", "."), 1770, 560, 40, "black", LIME, acc, align="right", glow=0.3)
        bar_meter(c, 1240, 580, 530, 14, n / 3205, LIME, acc)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        text(c, "BYTES DA FUNÇÃO", 1240, 650, 26, "monob", GOLD, ad, align="left")
        for i in range(63):
            on = ep(t, C["13.d"] + i * 0.03, 0.2)
            rrect(c, 1240 + (i % 21) * 25, 670 + (i // 21) * 25, 20, 20, 3, GOLD if on > 0.5 else "#1A2440", ad)
        glow_text(c, "63/63", 1770, 650, 34, "black", GOLD, ad, align="right", glow=0.3)


def b_instalar(c, t, C, B):
    head(c, t, B["start"], "COMO USAR", "INSTALAÇÃO", LIME)
    aa = ep(t, C["14.a"], 0.5)
    chip(c, "Node.js ≥ 22", 1000, 150, LIME, aa, anchor="center", size=26)
    chip(c, "+ agente de código", 1290, 150, LIME, ep(t, C["14.a"] + 0.9, 0.5), anchor="center", size=26)
    ab = ep(t, C["14.b"] - 0.4, 0.5)
    terminal(c, 150, 230, 1620, 580, ab, "terminal")
    if ab > 0:
        typed(c, "npx rea-agents setup", 200, 340, 40, t, C["14.b"], cps=14, col=INK, prompt="$")
        rows = [("14.c", "?", "Quais agentes configurar?", "[x] Claude Code  [x] Codex  [x] Cursor  [ ] Gemini CLI", CYAN),
                ("14.d", "›", "Plano de mudanças", "revise antes de aplicar · [aprovar]", GOLD),
                ("14.e", "+", "Backup da configuração", "config.json → config.json.bak", LIME),
                ("14.f", "+", "Pronto!", "reinicie o seu agente", LIME)]
        for i, (cue, sym, l1, l2, col) in enumerate(rows):
            a = ep(t, C[cue], 0.4)
            y = 430 + i * 92
            text(c, sym, 200, y, 32, "monob", col, a, align="left")
            text(c, l1, 250, y, 32, "monob", INK, a, align="left")
            text(c, l2, 250, y + 38, 26, "mono", INK2, a, align="left")


def b_prompt(c, t, C, B):
    head(c, t, B["start"], "COMO USAR", "PEDINDO EM LINGUAGEM NATURAL", VIOLET)
    aa = ep(t, C["15.a"] - 0.3, 0.5)
    panel(c, 150, 230, 1620, 330, aa, VIOLET, label="você → agente")
    if aa > 0:
        msg = ["Entenda como funciona a busca do app de Notas,", "me mostre as evidências e construa um recurso parecido."]
        t0 = C["15.a"]
        for i, s in enumerate(msg):
            typed(c, s, 200, 340 + i * 70, 38, t, t0 + i * len(msg[0]) / 30, cps=30, col=INK, peso="semibold",
                  cursor=i == 1)
        chip(c, "ENVIAR →", 1650, 500, VIOLET, ep(t, C["15.a"] + 3.8, 0.4), anchor="right", size=26, filled=True)
    ab = ep(t, C["15.b"] - 0.3, 0.5)
    terminal(c, 150, 610, 1620, 220, ab, "CLI")
    if ab > 0:
        typed(c, "rea --help", 200, 720, 38, t, C["15.b"] + 0.6, cps=14, col=INK, prompt="$")
        text(c, "os mesmos fluxos, direto no terminal", 200, 780, 26, "mono", DIM, ep(t, C["15.b"] + 1.6, 0.4), align="left")


def b_licencas(c, t, C, B):
    head(c, t, B["start"], "DETALHE", "AS FERRAMENTAS POR TRÁS", GOLD)
    tools = [("16.a", "Ghidra", "GRATUITO", LIME), ("16.b", "IDA", "COMERCIAL", GOLD), ("16.b", "Hopper", "COMERCIAL", GOLD)]
    for k, (cue, name, kind, col) in enumerate(tools):
        a, dy = reveal(t, C[cue] + (0.6 if k == 2 else 0))
        if a <= 0:
            continue
        x = 150 + k * 550
        panel(c, x, 260 + dy, 500, 300, a, col)
        glow_text(c, name, x + 250, 400 + dy, 72, "black", INK, a, glow=0.12)
        chip(c, kind, x + 250, 480 + dy, col, a, anchor="center", size=26, filled=True)
    ac = ep(t, C["16.c"], 0.5)
    if ac > 0:
        chip(c, "O REA NÃO FORNECE LICENÇA", W / 2, 660, ROSE, ac, anchor="center", size=32, filled=True)
        text(c, "você precisa ter a sua", W / 2, 750, 32, "mono", INK2, ep(t, C["16.c"] + 0.8, 0.4))


def b_legal(c, t, C, B):
    head(c, t, B["start"], "CUIDADOS", "USO LEGAL E ÉTICO", ROSE)
    ok = ["pesquisa legal", "educação", "interoperabilidade", "preservação de software"]
    aa = ep(t, C["17.a"], 0.5)
    panel(c, 150, 230, 800, 470, aa, LIME, label="PERMITIDO")
    for i, s in enumerate(ok):
        a = ep(t, C["17.a"] + 0.6 * i, 0.4)
        check_icon(c, 210, 320 + i * 72, 18, a, LIME)
        text(c, s, 250, 332 + i * 72, 34, "bold", INK, a, align="left")
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        check_icon(c, 210, 320 + 4 * 72, 18, ab, LIME)
        text(c, "programas SEUS ou AUTORIZADOS", 250, 332 + 4 * 72, 34, "black", LIME, ab, align="left")
    ac = ep(t, C["17.c"], 0.5)
    panel(c, 1010, 230, 760, 470, ac, ROSE, label="PROIBIDO")
    for i, s in enumerate(("copiar software protegido", "burlar licença", "usar cópias crackeadas")):
        a = ep(t, C["17.c"] + 0.6 * i, 0.4)
        check_icon(c, 1070, 330 + i * 90, 18, a, ROSE, "x")
        text(c, s, 1110, 342 + i * 90, 34, "bold", INK, a, align="left")
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        glow_text(c, "PODER  +  RESPONSABILIDADE", W / 2, 800, 58, "black", GOLD, ad, glow=0.4)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR DESTE VÍDEO", CYAN)
    panel(c, 150, 220, 1620, 620, ep(t, B["start"] + 0.3, 0.5), CYAN, label="README.md")
    rows = [("18.a", "servidor MCP open source: engenharia reversa para o seu agente", CYAN),
            ("18.b", "analisa de binários nativos a sites (~25 tipos de alvo)", VIOLET),
            ("18.c", "roda localmente, na sua máquina", LIME), ("18.d", "cada conclusão vem com evidência e limitações", LIME),
            ("18.e", "entender, aprender e reconstruir — sempre com autorização", GOLD)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = reveal(t, C[cue], 0.45)
        y = 330 + k * 105 + dy
        glow_text(c, f"0{k + 1}", 220, y, 40, "black", col, a, align="left", glow=0.4)
        text(c, s, 310, y, 38, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    tech.cta(c, t, C["19.like"], C["19.sub"], C["19.bell"], C["19.com"], C["19.bye"],
             "Qual aplicativo você abriria por dentro?")
    a = ep(t, B["start"], 0.5) * (1 - prog(t, C["19.like"] - 0.4, 0.4))
    if a > 0:
        glow_text(c, "REA", W / 2, 520, 200, "black", CYAN, a, glow=0.8)
        text(c, "github.com/morluto/rea  ·  rea.tools", W / 2, 620, 34, "mono", INK2, a)


BLOCKS = dict(hook=b_hook, intro=b_intro, mapa=b_mapa, compila=b_compila, ferramentas=b_ferramentas, mcp=b_mcp,
              fluxo=b_fluxo, evidencia=b_evidencia, alvos=b_alvos, local=b_local, calc=b_calc, dino=b_dino,
              dxball=b_dxball, instalar=b_instalar, prompt=b_prompt, licencas=b_licencas, legal=b_legal,
              resumo=b_resumo, cta=b_cta)
