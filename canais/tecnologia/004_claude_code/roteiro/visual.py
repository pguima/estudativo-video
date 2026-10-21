"""Visual do vídeo Tecnologia 004 — Claude Code: o agente de programação. Tema 'tech' (futurista)."""
import math
import skia
import tech
from motor import *  # noqa
from tech import *  # noqa

tech.SERIE = "TECH//004 · CLAUDE CODE"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_004_claude_code.mp4"
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay


# ---------------- peças deste vídeo ----------------
def tline(c, s, x, y, t, t0, col=INK, size=28, sym=None, sym_col=CYAN, peso="mono"):
    """linha de saída do terminal que aparece em t0"""
    a = ep(t, t0, 0.3)
    if a <= 0:
        return
    xx = x
    if sym:
        xx += text(c, sym + " ", x, y, size, "monob", sym_col, a, align="left")
    text(c, s, xx, y, size, peso, col, a, align="left")


def keycap(c, s, x, cy, a, col=CYAN, size=30, down=0.0):
    if a <= 0:
        return x
    w = text_w(s, "monob", size) + 40
    h = size * 1.9
    yy = cy - h / 2 + 4 * down
    rrect(c, x, yy + 6, w, h, 10, "#02040A", a)
    rrect(c, x, yy, w, h, 10, mix("#111A30", col, 0.25 * down), a, stroke=2, stroke_color=col)
    text_mid(c, s, x + w / 2, yy + h / 2, size, "monob", INK, a)
    return x + w


def file_tree(c, x, y, files, t, t0, a, lit_from=None, step=0.45, col=CYAN):
    """árvore de arquivos; a partir de lit_from, os arquivos 'abrem' um a um"""
    for i, (depth, name) in enumerate(files):
        ai = ep(t, t0 + 0.08 * i, 0.3) * a
        on = lit_from is not None and ep(t, lit_from + step * i, 0.3) > 0.5 and not name.endswith("/")
        yy = y + i * 46
        if on:
            rrect(c, x - 10, yy - 32, 440, 44, 6, col, 0.18 * ai)
        text(c, name, x + depth * 30, yy, 28, "mono", (col if on else INK2) if not name.endswith("/") else DIM, ai,
             align="left")


def toggle(c, x, cy, on, a):
    rrect(c, x, cy - 30, 120, 60, 30, mix("#1A2440", LIME, on), a)
    c.drawCircle(x + 30 + 60 * on, cy, 22, paint(INK, a))


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    terminal(c, 150, 200, 1620, 640, a0, "~/meu-projeto")
    if a0 <= 0:
        return
    typed(c, 'claude "escreva os testes do módulo de login,', 200, 310, 32, t, C["01.a"] - 0.2, cps=30, col=INK,
          prompt="$", cursor=False)
    typed(c, '  rode e corrija o que falhar"', 200, 360, 32, t, C["01.a"] + 1.6, cps=30, col=INK, cursor=t < C["01.c"])
    tline(c, "Lendo src/auth/login.ts", 200, 450, t, C["01.c"], sym=">", sym_col=CYAN)
    tline(c, "Escrevendo tests/login.test.ts  (14 testes)", 200, 510, t, C["01.d"], sym=">", sym_col=VIOLET)
    tline(c, "npm test  →  2 falharam", 200, 570, t, C["01.e"], col=ROSE, sym="$", sym_col=LIME)
    tline(c, "Corrigindo src/auth/login.ts:42", 200, 630, t, C["01.f"], sym=">", sym_col=GOLD)
    tline(c, "npm test  →  14 passaram", 200, 690, t, C["01.f"] + 1.4, col=LIME, sym="$", sym_col=LIME)
    ab = ep(t, C["01.b"], 0.5)
    chip(c, "E ELE FAZ", 1700, 270, CYAN, ab, anchor="right", size=30, filled=True)
    text(c, "dados ilustrativos", 1745, 820, 18, "mono", DIM, ep(t, C["01.d"], 0.4), align="right")


def b_intro(c, t, C, B):
    a0 = ep(t, C["02.a"], 0.6)
    cx = W / 2
    chip(c, "ANTHROPIC", cx, 250, DIM, a0, anchor="center", size=26)
    glow_text(c, "Claude Code", cx, 470, 170, "black", INK, a0, glow=0.0)
    glow_text(c, "Claude Code", cx, 470, 170, "black", CYAN, a0 * (0.3 + 0.1 * math.sin(t * 2)), glow=0.9)
    w = text_w("Claude Code", "black", 170)
    c.drawRect(skia.Rect.MakeXYWH(cx + w / 2 + 30, 360, 26, 110), paint(CYAN, a0 * (0.5 + 0.5 * math.sin(t * 6))))
    items = [("02.b", "LÊ O PROJETO", CYAN), ("02.c", "EDITA ARQUIVOS", VIOLET), ("02.d", "RODA COMANDOS", LIME),
             ("02.e", "INTEGRA FERRAMENTAS", MAGENTA)]
    total = sum(text_w(s, "monob", 26) + 26 * 1.3 for _, s, _ in items) + 30 * 3
    x = cx - total / 2
    for cue, s, col in items:
        x = chip(c, s, x, 640, col, ep(t, C[cue], 0.45), size=26)[1] + 30


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "ROTEIRO", "NESTE VÍDEO")
    items = [("03.a", "CHAT × AGENTE", "o que muda", CYAN), ("03.b", "ONDE RODA", "terminal, IDE, web", VIOLET),
             ("03.c", "INSTALAR", "um comando", LIME), ("03.d", "O QUE PEDIR", "perguntas e tarefas", MAGENTA),
             ("03.e", "PERMISSÕES", "os modos", GOLD), ("03.f", "PERSONALIZAR", "CLAUDE.md e mais", CYAN)]
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


def b_chat(c, t, C, B):
    head(c, t, B["start"], "A DIFERENÇA", "CHAT × AGENTE", CYAN)
    aa, dya = reveal(t, C["04.a"])
    if aa > 0:
        panel(c, 150, 240 + dya, 760, 520, aa, ROSE, label="no chat")
        panel(c, 190, 320 + dya, 260, 170, aa, DIM, k=12, glow=False)
        text(c, "seu editor", 320, 415 + dya, 28, "bold", INK2, aa)
        panel(c, 610, 320 + dya, 260, 170, aa, DIM, k=12, glow=False)
        text(c, "chat", 740, 415 + dya, 28, "bold", INK2, aa)
        u = (t * 0.5) % 1
        for k, (y, lab, d) in enumerate(((370, "copiar", 1), (450, "colar", -1))):
            x0, x1 = (455, 605) if d > 0 else (605, 455)
            arrow(c, x0, y + dya, x1, y + dya, GOLD, aa, 3, 12)
            text(c, lab, 530, y - 12 + dya, 20, "mono", GOLD, aa)
        node(c, 530, 620 + dya, 55, None, None, GOLD, aa, t, glyph="EU", gsize=34)
    ab = ep(t, C["04.b"], 0.5)
    chip(c, "VOCÊ É A PONTE", 530, 820, ROSE, ab, anchor="center", size=28, filled=True)
    ac, dyc = reveal(t, C["04.c"])
    if ac > 0:
        panel(c, 1010, 240 + dyc, 760, 520, ac, CYAN, label="claude code")
        files = [(0, "src/"), (1, "auth/login.ts"), (1, "auth/session.ts"), (1, "routes.ts"), (0, "tests/"),
                 (1, "login.test.ts"), (0, "package.json"), (0, "README.md")]
        file_tree(c, 1060, 320 + dyc, files, t, C["04.c"], ac, lit_from=C["04.d"])
        node(c, 1620, 420 + dyc, 70, None, None, CYAN, ac, t, glyph="AI", gsize=44)
    ad = ep(t, C["04.d"] + 1.5, 0.5)
    chip(c, "ELE ABRE O QUE PRECISA", 1390, 820, LIME, ad, anchor="center", size=28, filled=True)


def b_loop(c, t, C, B):
    head(c, t, B["start"], "COMO TRABALHA", "UM CICLO", VIOLET)
    cx, cy, R = 960, 520, 200
    steps = [("05.s1", "DESCREVER", "você", VIOLET, "?"), ("05.s2", "PLANEJAR", "o caminho", CYAN, "1-2-3"),
             ("05.s3", "ESCREVER", "vários arquivos", MAGENTA, "</>"), ("05.s4", "VERIFICAR", "roda os testes", LIME, "OK")]
    pos = []
    for k in range(4):
        ang = -math.pi / 2 + k * math.pi / 2
        pos.append((cx + R * 1.5 * math.cos(ang), cy + R * math.sin(ang)))
    for k, (cue, lab, sub, col, g) in enumerate(steps):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y = pos[k]
        if k > 0:
            x0, y0 = pos[k - 1]
            link(c, x0, y0, x, y, steps[k - 1][3], a, t, progress=ep(t, C[cue] - 0.1, 0.5), pulses=2)
        node(c, x, y, 70, None, None, col, a, t, glyph=g, gsize=40 if len(g) < 4 else 28)
        side = -1 if x <= cx - 10 else 1
        tx = x + side * 105
        ty = y + 4
        al = "left" if side > 0 else "right"
        text(c, lab, tx, ty, 34, "extrabold", INK, a, align=al)
        text(c, sub, tx, ty + 36, 24, "mono", DIM, a, align=al)
    a5 = ep(t, C["05.s5"], 0.5)
    if a5 > 0:
        x0, y0 = pos[3]
        x1, y1 = pos[0]
        link(c, x0, y0, x1, y1, ROSE, a5, t, progress=ep(t, C["05.s5"], 0.6), pulses=2, dash=True)
        chip(c, "ERRO? VOLTA AO CICLO", cx, cy, ROSE, a5, anchor="center", size=28, filled=True)


def b_bastidor(c, t, C, B):
    head(c, t, B["start"], "BASTIDOR", "ESTE CANAL USA CLAUDE CODE", GOLD)
    aa = ep(t, C["06.a"], 0.5)
    chip(c, "TECH//001 → 004", 1770, 150, GOLD, aa, anchor="right", size=24)
    cards = [("06.b", "cenas.py", "ROTEIRO", VIOLET), ("06.c", "visual.py", "ANIMAÇÕES", CYAN), ("06.d", "render.py", "RENDER", LIME)]
    for k, (cue, lab, title, col) in enumerate(cards):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 550
        y = 250 + dy
        panel(c, x, y, 500, 560, a, col, label=lab)
        text(c, title, x + 250, y + 90, 40, "black", INK, a)
        if k == 0:
            for i, s in enumerate(('dict(id="06",', '  block="bastidor",', '  text="E um bastidor:', '  [p=0.3] {a}os', '  vídeos *deste*..."),')):
                text(c, s, x + 40, y + 180 + i * 46, 24, "mono", INK2 if i != 4 else VIOLET, a, align="left")
        elif k == 1:
            for i, s in enumerate(("def b_bastidor(c, t):", "  head(c, t, ...)", "  panel(c, x, y,", "        500, 560)", "  chip(c, 'TECH')")):
                text(c, s, x + 40, y + 180 + i * 46, 24, "mono", CYAN if i == 0 else INK2, a, align="left")
        else:
            n = int(clamp(prog(t, C[cue], 3.0)) * 16)
            text(c, f"segmento {n}/16", x + 40, y + 200, 28, "monob", LIME, a, align="left")
            bar_meter(c, x + 40, y + 230, 420, 16, n / 16, LIME, a)
            for i in range(8):
                rrect(c, x + 40 + i * 54, y + 300, 46, 70, 4, LIME if i < n / 2 else "#1A2440", a * 0.8)
            text(c, "→ final.mp4", x + 40, y + 450, 30, "monob", INK, ep(t, C[cue] + 3.0, 0.4), align="left")


def b_onde(c, t, C, B):
    head(c, t, B["start"], "ONDE RODA", "VÁRIAS SUPERFÍCIES", CYAN)
    tiles = [("07.a1", "Terminal", "CLI completa", LIME, ">_"), ("07.a2", "VS Code", "e Cursor", CYAN, "{ }"),
             ("07.a3", "JetBrains", "IntelliJ, PyCharm...", VIOLET, "IJ"), ("07.a4", "Desktop", "Mac e Windows", MAGENTA, "[ ]"),
             ("07.a5", "Navegador", "claude.ai/code", GOLD, "www"), ("07.a6", "Celular", "app do Claude", ROSE, "app")]
    hub = (960, 840)
    for k, (cue, name, sub, col, g) in enumerate(tiles):
        a, dy = reveal(t, C[cue], 0.45)
        if a <= 0:
            continue
        x = 150 + (k % 3) * 550
        y = 230 + (k // 3) * 210 + dy
        panel(c, x, y, 500, 180, a, col, k=18)
        glow_text(c, g, x + 70, y + 108, 44, "black", col, a, glow=0.4)
        text(c, name, x + 150, y + 85, 44, "black", INK, a, align="left")
        text(c, sub, x + 150, y + 135, 24, "mono", INK2, a, align="left")
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        chip(c, "MESMO MOTOR · MESMAS CONFIGURAÇÕES", hub[0], 700, CYAN, ab, anchor="center", size=28, filled=True)


def b_instalar(c, t, C, B):
    head(c, t, B["start"], "INSTALAR", "UM COMANDO SÓ", LIME)
    ab0 = ep(t, C["08.a"] - 0.4, 0.5)
    terminal(c, 150, 220, 1620, 620, ab0, "terminal")
    if ab0 <= 0:
        return
    tline(c, "# macOS, Linux e WSL", 200, 320, t, C["08.a"], col=DIM, size=28)
    typed(c, "curl -fsSL https://claude.ai/install.sh | bash", 200, 370, 32, t, C["08.a"] + 0.3, cps=34, col=INK,
          prompt="$", cursor=False)
    tline(c, "# Windows (PowerShell)", 200, 450, t, C["08.b"], col=DIM, size=28)
    typed(c, "irm https://claude.ai/install.ps1 | iex", 200, 500, 32, t, C["08.b"] + 0.3, cps=34, col=INK,
          prompt="PS>", cursor=False)
    typed(c, "cd meu-projeto", 200, 600, 32, t, C["08.c"] + 0.2, cps=20, col=INK, prompt="$", cursor=False)
    typed(c, "claude", 200, 650, 32, t, C["08.d"], cps=14, col=CYAN, peso="monob", prompt="$", cursor=t < C["08.e"])
    ae = ep(t, C["08.e"], 0.4)
    if ae > 0:
        panel(c, 1080, 580, 640, 200, ae, VIOLET, k=14, label="primeiro uso")
        text(c, "Faça login para continuar", 1120, 660, 30, "bold", INK, ae, align="left")
        chip(c, "Entrar com o Claude →", 1120, 725, VIOLET, ae, size=24, filled=True, peso="bold")


def b_planos(c, t, C, B):
    head(c, t, B["start"], "CONTA", "QUEM PODE USAR", GOLD)
    for k, s in enumerate(("Pro", "Max", "Team", "Enterprise")):
        a, dy = reveal(t, C["09.a"] + 0.35 * k)
        if a <= 0:
            continue
        panel(c, 150 + k * 410, 280 + dy, 370, 180, a, CYAN, k=16)
        text(c, "PLANO", 335 + k * 410, 340 + dy, 22, "monob", DIM, a)
        glow_text(c, s, 335 + k * 410, 410 + dy, 52, "black", INK, a, glow=0.12)
    ab, dyb = reveal(t, C["09.b"])
    if ab > 0:
        panel(c, 150, 560 + dyb, 1620, 220, ab, GOLD, label="ou")
        text(c, "Console da Anthropic", 210, 660 + dyb, 48, "black", INK, ab, align="left")
        text(c, "créditos pré-pagos · paga pelo uso da API", 210, 720 + dyb, 30, "mono", INK2, ab, align="left")


def b_perguntas(c, t, C, B):
    head(c, t, B["start"], "COMECE PERGUNTANDO", "ENTENDA O PROJETO", CYAN)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    terminal(c, 150, 220, 1620, 600, a0, "claude · ~/projeto-novo")
    qs = [("10.a", "O que esse projeto faz?", "API de agendamentos em Node.js + PostgreSQL"),
          ("10.b", "Onde está o ponto de entrada?", "src/server.ts → inicia o Express na porta 3000"),
          ("10.c", "Explique a estrutura de pastas.", "src/ código · tests/ testes · migrations/ banco")]
    for i, (cue, q, ans) in enumerate(qs):
        y = 320 + i * 150
        typed(c, q, 200, y, 32, t, C[cue], cps=30, col=INK, peso="semibold", prompt=">", prompt_col=CYAN,
              cursor=False)
        tline(c, ans, 240, y + 50, t, C[cue] + 1.3, col=INK2, size=26, sym="→", sym_col=DIM)
    text(c, "respostas ilustrativas", 1745, 800, 18, "mono", DIM, a0, align="right")
    ad = ep(t, C["10.d"], 0.5)
    chip(c, "PROJETO QUE VOCÊ NUNCA VIU", W / 2, 870, LIME, ad, anchor="center", size=28, filled=True)


def b_tarefas(c, t, C, B):
    head(c, t, B["start"], "PASSE TAREFAS", "DO BUG AO PULL REQUEST", MAGENTA)
    cards = [("11.a", "BUG", ROSE), ("11.b", "FUNCIONALIDADE", CYAN), ("11.c", "TESTES", VIOLET)]
    for k, (cue, title, col) in enumerate(cards):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 340
        y = 240 + dy
        panel(c, x, y, 310, 300, a, col, k=16)
        text(c, title, x + 155, y + 70, 30, "black", INK, a)
        if k == 0:
            text(c, "TypeError: cannot", x + 30, y + 140, 22, "mono", ROSE, a, align="left")
            text(c, "read 'id' of null", x + 30, y + 172, 22, "mono", ROSE, a, align="left")
            text(c, "→ causa → correção", x + 30, y + 240, 22, "monob", LIME, ep(t, C[cue] + 1.2, 0.4), align="left")
        elif k == 1:
            text(c, "“adicione validação", x + 30, y + 150, 24, "semibold", INK2, a, align="left")
            text(c, "ao formulário”", x + 30, y + 185, 24, "semibold", INK2, a, align="left")
        else:
            n = int(14 * clamp(prog(t, C[cue] + 0.3, 1.5)))
            glow_text(c, f"+{n}", x + 155, y + 200, 72, "black", VIOLET, a, glow=0.4)
            text(c, "testes novos", x + 155, y + 250, 24, "mono", INK2, a)
    ad, dyd = reveal(t, C["11.d"])
    if ad > 0:
        panel(c, 1180, 240 + dyd, 590, 560, ad, LIME, label="git")
        text(c, "commit", 1220, 330 + dyd, 22, "monob", DIM, ad, align="left")
        typed(c, "feat: valida formulário de cadastro", 1220, 375, 24, t, C["11.d"] + 1.5, cps=30, col=INK, cursor=False)
        ae = ep(t, C["11.e"], 0.4)
        text(c, "branch", 1220, 450 + dyd, 22, "monob", DIM, ae, align="left")
        text(c, "feature/validacao", 1220, 495 + dyd, 26, "mono", CYAN, ae, align="left")
        chip(c, "PULL REQUEST ABERTO", 1220, 600 + dyd, LIME, ep(t, C["11.e"] + 1.0, 0.4), size=24, filled=True)
        # trilho do git
        for i in range(4):
            cy = 700 + dyd
            c.drawCircle(1240 + i * 120, cy, 12, paint(LIME if i < 3 else CYAN, ad))
            if i:
                c.drawLine(1252 + (i - 1) * 120, cy, 1228 + i * 120, cy, paint(LIME, ad, stroke=3))
    text(c, "exemplos ilustrativos", 150, 860, 18, "mono", DIM, ep(t, C["11.a"], 0.4), align="left")


def b_permissao(c, t, C, B):
    head(c, t, B["start"], "PERMISSÕES", "ELE PEDE ANTES", GOLD)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        panel(c, 150, 230, 1000, 560, aa, GOLD, label="modo manual")
        text(c, "Editar src/auth/login.ts?", 200, 320, 36, "black", INK, aa, align="left")
        rows = [("-", "  if (user.id) {", ROSE), ("+", "  if (user?.id) {", LIME), (" ", "    return session", INK2)]
        for i, (sg, s, col) in enumerate(rows):
            rrect(c, 200, 350 + i * 50, 900, 44, 4, col, 0.10 * aa)
            text(c, sg + s, 214, 382 + i * 50, 26, "mono", col, aa, align="left")
        opts = ["1. Sim", "2. Sim, e não perguntar de novo nesta sessão", "3. Não, faça diferente"]
        sel = int((t * 0.8) % 3)
        for i, s in enumerate(opts):
            on = i == sel
            text(c, ("› " if on else "  ") + s, 200, 560 + i * 54, 28, "monob" if on else "mono", GOLD if on else INK2, aa,
                 align="left")
        text(c, "ilustrativo", 1120, 770, 18, "mono", DIM, aa, align="right")
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        down = 1.0 if (t - C["12.b"]) % 1.6 < 0.2 else 0.0
        x = keycap(c, "Shift", 1230, 360, ab, CYAN, down=down)
        text(c, "+", x + 26, 372, 40, "black", INK2, ab)
        keycap(c, "Tab", x + 56, 360, ab, CYAN, down=down)
        modes = ["manual", "aceitar edições", "plano", "automático"]
        k = int(max(0, t - C["12.b"]) / 1.6) % 4
        for i, m in enumerate(modes):
            on = i == k
            chip(c, m, 1230, 480 + i * 80, CYAN if on else DIM, ab, size=26, filled=on)


def b_modos(c, t, C, B):
    head(c, t, B["start"], "PERMISSÕES", "OS MODOS MAIS ÚTEIS", GOLD)
    cards = [("13.a", "PLANO", "só lê e propõe;", "edita depois do seu OK", VIOLET),
             ("13.b", "ACEITAR EDIÇÕES", "edita sem perguntar;", "você revisa junto", CYAN),
             ("13.c", "AUTOMÁTICO", "um 2º modelo revisa", "cada ação", LIME)]
    for k, (cue, title, l1, l2, col) in enumerate(cards):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 550
        y = 250 + dy
        panel(c, x, y, 500, 430, a, col, label=f"0{k + 1}")
        text(c, title, x + 250, y + 100, 36, "black", INK, a)
        text(c, l1, x + 250, y + 180, 28, "mono", INK2, a)
        text(c, l2, x + 250, y + 220, 28, "mono", INK2, a)
        if k == 0:
            for i in range(3):
                check_icon(c, x + 120, y + 290 + i * 40, 10, a, VIOLET)
                rrect(c, x + 145, y + 282 + i * 40, 220 - i * 40, 14, 7, "#2A3552", a)
        elif k == 1:
            rrect(c, x + 80, y + 290, 340, 40, 4, LIME, 0.15 * a)
            text(c, "+ if (user?.id)", x + 95, y + 318, 24, "mono", LIME, a, align="left")
        else:
            node(c, x + 170, y + 330, 40, None, None, LIME, a, t, glyph="AI", gsize=24)
            node(c, x + 330, y + 330, 40, None, None, CYAN, a, t, glyph="OK", gsize=22)
            link(c, x + 212, y + 330, x + 288, y + 330, LIME, a, t, pulses=1)
    ad = ep(t, C["13.d"], 0.5)
    chip(c, "PULAR TUDO: SÓ EM CONTAINER OU VM ISOLADA", W / 2, 790, ROSE, ad, anchor="center", size=28, filled=True)


def b_claudemd(c, t, C, B):
    head(c, t, B["start"], "PERSONALIZAR", "O ARQUIVO CLAUDE.md", CYAN)
    aa, dya = reveal(t, C["14.a"])
    if aa > 0:
        panel(c, 150, 230 + dya, 900, 580, aa, CYAN, label="CLAUDE.md")
        lines = [("# Projeto: API de agendamentos", INK, "bold"), ("", INK, "mono"),
                 ("## Padrões", CYAN, "monob"), ("- TypeScript estrito, sem any", INK2, "mono"),
                 ("- testes com Vitest antes do PR", INK2, "mono"), ("## Arquitetura", CYAN, "monob"),
                 ("- rotas em src/routes, regras em src/services", INK2, "mono"), ("## Bibliotecas", CYAN, "monob"),
                 ("- datas: date-fns (não usar moment)", INK2, "mono")]
        for i, (s, col, peso) in enumerate(lines):
            text(c, s, 200, 310 + i * 52 + dya, 28, peso, col, ep(t, C["14.c"] - 0.6 + 0.12 * i, 0.3) * aa, align="left")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        text(c, "raiz do projeto/", 1130, 300, 26, "monob", DIM, ab, align="left")
        chip(c, "CLAUDE.md", 1160, 350, CYAN, ab, size=26, filled=True)
        for i in range(3):
            ai = ep(t, C["14.b"] + 0.6 * i, 0.4)
            y = 450 + i * 90
            panel(c, 1130, y, 330, 70, ai, DIM, k=10, glow=False)
            text(c, f"sessão {i + 1}", 1160, y + 46, 26, "monob", INK, ai, align="left")
            check_icon(c, 1420, y + 35, 14, ai, LIME)
        text(c, "lido no início de toda sessão", 1130, 750, 26, "mono", INK2, ab, align="left")
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        chip(c, "+ MEMÓRIA AUTOMÁTICA", 1500, 360, VIOLET, ad, size=24, filled=True)
        text(c, "aprende trabalhando", 1500, 420, 24, "mono", INK2, ad, align="left")


def b_extensoes(c, t, C, B):
    head(c, t, B["start"], "IR ALÉM", "SKILLS · HOOKS · MCP", VIOLET)
    aa, dya = reveal(t, C["15.a"])
    if aa > 0:
        panel(c, 150, 240 + dya, 500, 470, aa, VIOLET, label="skills")
        text(c, "fluxos reutilizáveis", 400, 330 + dya, 26, "mono", INK2, aa)
        for i, s in enumerate(("/review-pr", "/deploy-staging")):
            chip(c, s, 400, 420 + i * 90 + dya, VIOLET, ep(t, C["15.a"] + 0.5 + 0.4 * i, 0.4), anchor="center", size=30,
                 filled=i == 0)
    ab, dyb = reveal(t, C["15.b"])
    if ab > 0:
        panel(c, 710, 240 + dyb, 500, 470, ab, GOLD, label="hooks")
        rows = [("depois de editar", "→ formatar"), ("antes do commit", "→ rodar o lint")]
        for i, (k, v) in enumerate(rows):
            y = 360 + i * 140 + dyb
            text(c, k.upper(), 750, y, 22, "monob", DIM, ab, align="left")
            text(c, v, 750, y + 50, 34, "black", GOLD, ab, align="left")
    ac, dyc = reveal(t, C["15.c"])
    if ac > 0:
        panel(c, 1270, 240 + dyc, 500, 470, ac, CYAN, label="MCP")
        node(c, 1520, 360 + dyc, 55, None, None, CYAN, ac, t, glyph="AI", gsize=32)
        for i, (cue, s) in enumerate((("15.c1", "Google Drive"), ("15.c2", "Jira"), ("15.c3", "Slack"))):
            ai = ep(t, C[cue], 0.4)
            x = 1330 + i * 150
            link(c, 1520, 415 + dyc, x + 60, 560 + dyc, CYAN, ai, t, pulses=1)
            chip(c, s, x + 60, 590 + dyc, CYAN, ai, anchor="center", size=20)
    ad = ep(t, C["15.d"], 0.5)
    chip(c, "MESMO PROTOCOLO DO REA · TECH//001", W / 2, 800, MAGENTA, ad, anchor="center", size=28, filled=True)


def b_avancado(c, t, C, B):
    head(c, t, B["start"], "AUTOMATIZAR", "PARA QUEM QUER MAIS", LIME)
    aa, dya = reveal(t, C["16.a"])
    if aa > 0:
        panel(c, 150, 240 + dya, 520, 540, aa, CYAN, label="agentes em paralelo")
        node(c, 410, 360 + dya, 60, None, None, CYAN, aa, t, glyph="AI", gsize=34)
        for i in range(3):
            x = 230 + i * 180
            link(c, 410, 420 + dya, x, 560 + dya, CYAN, aa, t, pulses=1)
            node(c, x, 600 + dya, 42, None, None, VIOLET, aa, t, glyph=str(i + 1), gsize=34)
    ab, dyb = reveal(t, C["16.b"])
    if ab > 0:
        terminal(c, 720, 240 + dyb, 1050, 250, ab, "script / CI")
        typed(c, 'tail -200 app.log | claude -p "procure anomalias"', 760, 380 + dyb, 26, t, C["16.b"] + 0.4, cps=34,
              col=INK, prompt="$")
    ac, dyc = reveal(t, C["16.c"])
    if ac > 0:
        panel(c, 720, 540 + dyc, 1050, 240, ac, GOLD, label="rotina na nuvem")
        text(c, "todo dia · 08:00", 770, 630 + dyc, 40, "black", INK, ac, align="left")
        text(c, "revisar os PRs abertos", 770, 690 + dyc, 28, "mono", INK2, ac, align="left")
        chip(c, "PC DESLIGADO: RODA MESMO ASSIM", 1740, 740 + dyc, GOLD, ac, anchor="right", size=20, filled=True)


def b_dicas(c, t, C, B):
    head(c, t, B["start"], "DICAS OFICIAIS", "COMO PEDIR BEM", GOLD)
    aa, dya = reveal(t, C["17.a"])
    if aa > 0:
        panel(c, 150, 240 + dya, 1620, 270, aa, LIME, label="01 · seja específico")
        text(c, "“corrija o bug”", 200, 340 + dya, 34, "semibold", INK2, aa, align="left")
        st = ep(t, C["17.a2"], 0.4)
        c.drawLine(195, 330 + dya, 195 + 290 * st, 330 + dya, paint(ROSE, aa, stroke=4))
        a2 = ep(t, C["17.a2"], 0.5)
        text(c, "“corrija o bug em que o usuário vê uma tela em branco", 200, 410 + dya, 34, "bold", INK, a2, align="left")
        text(c, "depois de errar a senha”", 200, 460 + dya, 34, "bold", LIME, a2, align="left")
    ab, dyb = reveal(t, C["17.b"])
    if ab > 0:
        panel(c, 150, 560 + dyb, 780, 260, ab, CYAN, label="02 · em passos")
        for i, s in enumerate(("1. crie a tabela de perfis", "2. crie a rota da API", "3. crie a página")):
            text(c, s, 200, 640 + i * 52 + dyb, 28, "mono", INK, ep(t, C["17.b"] + 0.3 * i, 0.4), align="left")
    ac, dyc = reveal(t, C["17.c"])
    if ac > 0:
        panel(c, 990, 560 + dyc, 780, 260, ac, VIOLET, label="03 · explorar primeiro")
        text(c, "“analise o esquema do banco”", 1040, 670 + dyc, 32, "semibold", INK, ac, align="left")
        text(c, "antes de pedir a mudança", 1040, 730 + dyc, 28, "mono", INK2, ac, align="left")


def b_cuidados(c, t, C, B):
    head(c, t, B["start"], "CUIDADOS", "ANTES DE SAIR USANDO", ROSE)
    rows = [("18.a", "Revise o que ele muda", "como o código de um colega", CYAN),
            ("18.b", "Trabalhe com Git", "commits frequentes = voltar atrás é fácil", LIME),
            ("18.c", "Código sensível? Modo manual", "você aprova cada ação", GOLD),
            ("18.d", "Uso conta no limite do plano", "tarefas longas consomem mais", ROSE)]
    for k, (cue, t1, t2, col) in enumerate(rows):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        y = 240 + k * 150 + dy
        panel(c, 150, y, 1620, 125, a, col, k=14, glow=False)
        glow_text(c, f"0{k + 1}", 200, y + 80, 48, "black", col, a, align="left", glow=0.4)
        text(c, t1, 310, y + 62, 38, "black", INK, a, align="left")
        text(c, t2, 310, y + 102, 26, "mono", INK2, a, align="left")


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR DESTE VÍDEO", CYAN)
    panel(c, 150, 220, 1620, 620, ep(t, B["start"] + 0.3, 0.5), CYAN, label="README.md")
    rows = [("19.a", "um agente que trabalha dentro do seu projeto", CYAN),
            ("19.b", "lê, planeja, edita e verifica (em ciclo)", VIOLET),
            ("19.c", "terminal · IDEs · desktop · navegador", LIME),
            ("19.d", "pede permissão: você escolhe o modo (Shift+Tab)", GOLD),
            ("19.e", "CLAUDE.md ensina o seu jeito de programar", MAGENTA)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = reveal(t, C[cue], 0.45)
        y = 330 + k * 105 + dy
        glow_text(c, f"0{k + 1}", 220, y, 40, "black", col, a, align="left", glow=0.4)
        text(c, s, 310, y, 38, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    tech.cta(c, t, C["20.like"], C["20.sub"], C["20.bell"], C["20.com"], C["20.bye"],
             "Que tarefa chata você entregaria a ele?")
    a = ep(t, B["start"], 0.5) * (1 - prog(t, C["20.like"] - 0.4, 0.4))
    if a > 0:
        glow_text(c, "Claude Code", W / 2, 520, 140, "black", CYAN, a, glow=0.7)
        text(c, "code.claude.com", W / 2, 620, 34, "mono", INK2, a)


BLOCKS = dict(hook=b_hook, intro=b_intro, mapa=b_mapa, chat=b_chat, loop=b_loop, bastidor=b_bastidor, onde=b_onde,
              instalar=b_instalar, planos=b_planos, perguntas=b_perguntas, tarefas=b_tarefas, permissao=b_permissao,
              modos=b_modos, claudemd=b_claudemd, extensoes=b_extensoes, avancado=b_avancado, dicas=b_dicas,
              cuidados=b_cuidados, resumo=b_resumo, cta=b_cta)
