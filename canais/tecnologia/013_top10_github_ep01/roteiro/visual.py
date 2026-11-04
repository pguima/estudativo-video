"""Visual do vídeo Tecnologia 013 — Top 10 projetos do GitHub, episódio 1 (outubro de 2026). Tema 'tech', padrão da série:
sem roxo (2ª cor do fundo = esmeralda, fundo mais escuro e com mais contraste) e 3D (tech3d.py) onde carrega informação:
a posição do ranking extrudada, a estrela do gancho e o "10 → 1".
Só motion graphics próprios: nenhum logo ou captura de tela dos projetos; nomes, números e comandos como texto.
Números: original/api/*.json (API do GitHub) e github_trending_monthly_2026-10-27.html, consulta em 27/10/2026."""
import math
from contextlib import contextmanager
import skia
import motor
import tech
import tech3d
from motor import *  # noqa
from tech import *  # noqa
from tech3d import extrude, star3d, spin_in

# neste Linux não há Consolas: a fonte mono do tech.py não carrega. Usa DejaVu Sans Mono (como no 009/010).
motor.PESOS["mono"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono"
motor.PESOS["monob"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold"

tech.SERIE = "TECH//013 · TOP 10 GITHUB"
# série Top 10 GitHub: nada de degradê roxo; fundo mais escuro e órbitas mais discretas = mais contraste
EMERALD = "#34D399"
ORANGE = "#FB923C"
tech.ACENTO2 = EMERALD
tech.BASE = ("#0A1A26", "#040A10", "#010305")
tech.ORB_A = 0.16
MARCA = ""
ARQUIVO_FINAL = "tecnologia_013_top10_github_ep01.mp4"
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay

TOPO = 53014   # ganho do 1º lugar: escala das barras

# cena -> dados do projeto. fatos: (cue, texto, cor); alerta = fato com ícone de aviso
PROJ = {
    "03": dict(pos=10, nome="Ghidra", repo="NationalSecurityAgency/ghidra", tag="engenharia reversa, criada pela NSA",
               ganho=15099, total="94,7 mil", lic="Apache-2.0", col=CYAN, cmd="./ghidraRun",
               fatos=[("b", "desmonta e descompila executáveis", INK), ("b", "muito usado na análise de malware", INK),
                      ("c", "requer Java (JDK) 25", GOLD)],
               stat=("c", "12.2", "versão de 22/10")),
    "04": dict(pos=9, nome="AI Engineering from Scratch", repo="rohitg00/ai-engineering-from-scratch",
               tag="um curso inteiro de IA, de graça", ganho=16611, total="74,4 mil", lic="MIT", col=ORANGE,
               cmd=None,
               fatos=[("b", "da matemática básica até agentes", INK), ("b", "Python · TypeScript · Rust · Julia", INK),
                      ("c", "implementar, testar e ver onde falha", LIME)],
               stat=("b", "542", "lições em 20 fases")),
    "05": dict(pos=8, nome="Impeccable", repo="pbakaus/impeccable", tag="design para agentes de IA",
               ganho=17522, total="89,2 mil", lic="Apache-2.0", col=MAGENTA, cmd="npx impeccable install",
               fatos=[("b", "degradê roxo · tudo em Inter · card em card", ROSE),
                      ("c", "polish · audit · critique · e mais", INK), ("c", "regras que rodam sem IA", LIME)],
               stat=("c", "24 · 62", "comandos · regras")),
    "06": dict(pos=7, nome="Agent Reach", repo="Panniantong/Agent-Reach", tag="a internet que o seu agente não alcança",
               ganho=18035, total="103,6 mil", lic="MIT", col=LIME, cmd="agent-reach channels",
               fatos=[("b", "YouTube · Reddit · X · GitHub", INK), ("b", "LinkedIn · Bilibili e outros", INK),
                      ("e", "pacote 'agent-reach' do PyPI NÃO é o oficial", GOLD)],
               stat=None),
    "07": dict(pos=6, nome="HyperFrames", repo="heygen-com/hyperframes", tag="HTML vira vídeo · da HeyGen",
               ganho=19856, total="73 mil", lic="Apache-2.0", col=CYAN, cmd="npx skills add heygen-com/hyperframes",
               fatos=[("b", "HTML + CSS  →  MP4", INK), ("c", "feito para agentes (skills)", INK),
                      ("e", "transições, legendas, gráficos", INK)],
               stat=("e", "~450", "blocos prontos")),
    "08": dict(pos=5, nome="Paperclip", repo="paperclipai/paperclip", tag="agente = funcionário · Paperclip = empresa",
               ganho=21863, total="107,7 mil", lic="MIT", col=GOLD, cmd="npx paperclipai@latest onboard --yes",
               fatos=[("c", "objetivo → time: CEO, engenheiros, designers", INK), ("c", "agentes de qualquer fornecedor", INK),
                      ("e", "tarefas, aprovações, custos e orçamento", LIME)],
               stat=None),
    "09": dict(pos=4, nome="ECC", repo="affaan-m/ECC", tag="um time de engenharia para o seu agente",
               ganho=23245, total="289,8 mil", lic="MIT", col=ORANGE, cmd="npx ecc-universal@2.2.3 setup",
               fatos=[("b", "plan → test → implement → review", INK), ("c", "+ AgentShield (segurança)", LIME),
                      ("e", "Claude Code · Codex · Cursor…", INK)],
               stat=("c", "71 · 311", "agentes · skills")),
    "10": dict(pos=3, nome="Security Audit", repo="cloudflare/security-audit-skill", tag="skill da Cloudflare: o agente vira auditor",
               ganho=26289, total="48,5 mil", lic="MIT", col=ROSE,
               cmd="npx skills add …/cloudflare/security-audit-skill",
               fatos=[("b", "do mapeamento ao relatório", INK), ("c", "quem confere nunca é quem encontrou", LIME),
                      ("e", "use sandbox · só com autorização", GOLD)],
               stat=("b", "6", "fases")),
    "11": dict(pos=2, nome="Ponytail", repo="DietrichGebert/ponytail", tag="o sênior que troca 50 linhas por uma",
               ganho=31644, total="177,1 mil", lic="MIT", col=LIME, cmd="/plugin marketplace add DietrichGebert/ponytail",
               fatos=[("b", "-53% de código · -45% de tokens", LIME), ("c", "seletor de data: usa o do navegador", INK),
                      ("c", "sem cortar testes nem segurança", INK)],
               stat=("c", "335 → 10", "linhas"), nota="números do benchmark do próprio projeto"),
    "12": dict(pos=1, nome="VoiceStudio", repo="debpalash/VoiceStudio", tag="alternativa aberta ao ElevenLabs, local",
               ganho=53014, total="89,2 mil", lic="AGPL-3.0", col=CYAN, cmd="curl -fsSL https://voicestudio.sh/install | sh",
               fatos=[("b", "clona · cria vozes · dubla · transcreve", INK), ("c", "Windows · Mac · Linux · celular · GPU", INK),
                      ("e", "clone vozes só com permissão", ROSE)],
               stat=("b", "646", "idiomas")),
}
RANK = sorted(PROJ.items(), key=lambda kv: kv[1]["pos"])
AGENTES = {"Ponytail", "Security Audit", "ECC", "Paperclip", "HyperFrames", "Agent Reach", "Impeccable"}

# som padrão do canal (_ferramentas/som_tech.py); aqui só os efeitos que fogem do "pop" de cada cue
SOM = dict(sfx={"01.a": ["data@+0.1", "impact@+1.6"], "01.c": [f"pop@+{0.12 * k:.2f}" for k in range(9)],
                "02.d": "lock", "02.e": "whoosh",
                **{f"{k}.a": "impact" for k in PROJ}, **{f"{k}.d": "data" for k in PROJ},
                "06.e": "alert", "10.e": "alert", "12.e": "alert", "12.a": ["impact", "shimmer@+0.4"],
                "13.b": "confirm"})


def fmt(n):
    return f"{n:,}".replace(",", ".")


def fade(t, t0, t1, d=0.5, d_out=0.4):
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))


@contextmanager
def cam(c, t, B, z0=1.0, z1=1.04, cx=W / 2, cy=H / 2):
    u = clamp((t - B["start"]) / max(1.0, B["end"] - B["start"]))
    u = u * u * (3 - 2 * u)
    z = lerp(z0, z1, u)
    c.save(); c.translate(cx, cy); c.scale(z, z); c.translate(-cx, -cy)
    try:
        yield
    finally:
        c.restore()


def fit(s, peso, size, maxw):
    w = text_w(s, peso, size)
    return size if w <= maxw else size * maxw / w


def ic_warn(c, cx, cy, s, col, a):
    p = skia.Path(); p.moveTo(cx, cy - s * 0.5); p.lineTo(cx + s * 0.55, cy + s * 0.45); p.lineTo(cx - s * 0.55, cy + s * 0.45); p.close()
    pp = paint(col, a, stroke=s * 0.1); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pp)
    c.drawLine(cx, cy - s * 0.15, cx, cy + s * 0.15, paint(col, a, stroke=s * 0.1, cap_round=True))
    c.drawCircle(cx, cy + s * 0.3, s * 0.06, paint(col, a))


# ======================================================================  01 — GANCHO
def b_gancho(c, t, C, B):
    ta, tb, tc = C["01.a"], C["01.b"], C["01.c"]
    with cam(c, t, B, 1.0, 1.05):
        out = 1 - prog(t, tc - 0.2, 0.5)
        u = ep(t, ta, 1.8)
        a = ep(t, ta, 0.4) * out
        if a > 0:
            nw = text_w(fmt(TOPO), "black", 230)
            star3d(c, W / 2 - nw / 2 - 120, 425, 82, a, ry=1.8 * (1 - u) + 0.35 * math.sin(t * 0.9), rx=0.15)
            glow_text(c, fmt(int(TOPO * u)), W / 2 + 40, 500, 230, "black", INK, a, glow=0.25)
            text(c, "ESTRELAS EM 1 MÊS", W / 2, 610, 46, "monob", CYAN, a, tracking=4)
            glow_line(c, W / 2 - 420, 640, W / 2 + 420, 640, CYAN, a, 3, progress=u)
            chip(c, "TOP 10 · GITHUB · OUTUBRO 2026", W / 2, 250, CYAN, a, anchor="center", size=28)
        ab = ep(t, tb, 0.5) * out
        if ab > 0:
            chip(c, "DE GRAÇA", W / 2 - 30, 730, LIME, ab, anchor="right", size=30, filled=True)
            chip(c, "NO SEU COMPUTADOR", W / 2 + 30, 730, LIME, ep(t, tb + 0.6, 0.5) * out, anchor="left", size=30)
            # o nome do 1º lugar fica escondido até a cena 12
            panel(c, W / 2 - 260, 790, 520, 90, ab, DIM, k=14, fill=0.9, glow=False)
            for k in range(9):
                x = W / 2 - 200 + k * 50
                c.drawRect(skia.Rect.MakeXYWH(x, 822, 38, 26), blur_paint(INK2, 0.35 * ab, 6))
            text_mid(c, "#1 = ?", W / 2 + 330, 835, 34, "monob", GOLD, ab, align="left")
    a = ep(t, tc, 0.5)
    if a > 0:
        glow_text(c, "ANTES DELE:", W / 2, 360, 70, "black", INK, a, glow=0.2)
        for k in range(9):
            ak = ep(t, tc + 0.12 * k, 0.4)
            x = 330 + k * 157
            node(c, x, 560, 62, None, None, [CYAN, ORANGE, MAGENTA, LIME][k % 4], ak, t, glyph=f"#{10 - k}", gsize=38)
        text(c, "9 projetos que estão mudando o jeito de programar com IA", W / 2, 760, 34, "mono", INK2,
             ep(t, tc + 1.2, 0.6))


# ======================================================================  02 — CRITÉRIO
def b_criterio(c, t, C, B):
    ta, tb, tc, td, te = (C[f"02.{k}"] for k in "abcde")
    out = 1 - prog(t, te - 0.1, 0.4)
    head(c, t, B["start"], "CRITÉRIO", "MAIS ESTRELAS EM 30 DIAS", CYAN, t_out=te - 0.1)
    a = ep(t, ta, 0.6) * out
    if a > 0:
        panel(c, 150, 250, 980, 600, a, CYAN, label="github.com/trending")
        for i, (s, on) in enumerate((("Today", 0), ("This week", 0), ("This month", 1))):
            x = 200 + i * 230
            chip(c, s, x, 320, CYAN if on else DIM, a, size=24, filled=bool(on))
        for i in range(5):
            ai = ep(t, ta + 0.5 + 0.15 * i, 0.4) * out
            y = 410 + i * 86
            text(c, f"{i + 1:>2}", 205, y + 12, 28, "monob", DIM, ai, align="left")
            c.drawRect(skia.Rect.MakeXYWH(260, y - 12, 300 - i * 25, 22), paint(INK2, 0.35 * ai))
            bar_meter(c, 640, y - 8, 430, 16, (0.95 - 0.13 * i) * ep(t, ta + 0.8 + 0.15 * i, 0.8), CYAN, ai)
    ab = ep(t, tb, 0.5) * out
    chip(c, "CONSULTA: 27/10/2026", 1240, 330, GOLD, ab, size=28, filled=True)
    ac = ep(t, tc, 0.5) * out
    if ac > 0:
        panel(c, 1240, 420, 530, 170, ac, ORANGE, k=16)
        text(c, "SÉRIE MENSAL", 1290, 490, 44, "black", INK, ac, align="left")
        text(c, "uma lista nova todo mês", 1290, 545, 28, "mono", INK2, ac, align="left")
    ad = ep(t, td, 0.5) * out
    if ad > 0:
        panel(c, 1240, 630, 530, 220, ad, LIME, k=16)
        text(c, "NÃO REPETE", 1290, 705, 44, "black", LIME, ad, align="left")
        text(c, "só volta quem lançar", 1290, 760, 28, "mono", INK2, ad, align="left")
        text(c, "uma versão nova", 1290, 800, 28, "mono", INK2, ad, align="left")
    ae = ep(t, te, 0.5)
    if ae > 0:
        extrude(c, "10 → 1", W / 2, 520, 200, ae, rx=0.12, ry=spin_in(t, te, 1.0, -1.2, -0.22, 0.05), depth=50,
                side=CYAN, layers=20, shine=prog(t, te + 0.5, 1.0))
        glow_line(c, W / 2 - 380, 640, W / 2 + 380, 640, CYAN, ae, 4, progress=ep(t, te + 0.2, 0.7))


# ======================================================================  03–12 — UM PROJETO POR CENA
def b_proj(c, t, C, B, sid):
    p = PROJ[sid]
    col = p["col"]
    cue = lambda k: C.get(f"{sid}.{k}", B["start"] + 99)
    ta = cue("a")
    # coluna esquerda: posição gigante, ganho no mês e barra relativa ao 1º lugar
    a = ep(t, ta - 0.1, 0.45)
    text(c, "LUGAR", 330, 236, 30, "monob", col, a, tracking=6)
    first = p["pos"] == 1
    extrude(c, f"#{p['pos']}", 330, 385, 230, a, rx=0.10, ry=spin_in(t, ta - 0.1, 1.0, -1.4, -0.30, 0.06), depth=60,
            face=GOLD if first else INK, side=GOLD if first else col, layers=22, glow=0.35,
            shine=prog(t, ta + 0.5, 1.1))
    glow_line(c, 170, 520, 490, 520, col, a, 4, progress=ep(t, ta + 0.1, 0.6))
    td = cue("d")
    u = ep(t, td, 1.2)
    ag = ep(t, ta + 0.4, 0.5)
    ganho = int(lerp(p["ganho"] * 0.6, p["ganho"], u)) if t >= td else p["ganho"]
    glow_text(c, "+" + fmt(ganho), 330, 615, 64, "black", col, ag, glow=0.35 + 0.3 * math.sin(math.pi * u))
    text(c, "estrelas no mês", 330, 660, 26, "mono", INK2, ag)
    bar_meter(c, 175, 700, 310, 14, p["ganho"] / TOPO * ep(t, ta + 0.5, 1.0), col, ag)
    text(c, f"total: {p['total']}", 330, 760, 26, "mono", DIM, ag)
    chip(c, "LICENÇA " + p["lic"], 330, 820, col, ep(t, td + 0.6, 0.4) if t >= td else ag * 0.0, anchor="center",
         size=24, filled=True)
    # painel do projeto
    ap = ep(t, ta, 0.55)
    if ap <= 0:
        return
    x, y, w, h = 640, 190, 1130, 470
    panel(c, x, y + (1 - ap) * 20, w, h, ap, col, label="README.md")
    yy = y + (1 - ap) * 20
    text(c, p["repo"], x + 50, yy + 70, 24, "mono", DIM, ap, align="left")
    nsize = fit(p["nome"], "black", 76, 700 if p.get("stat") else 1000)
    glow_text(c, p["nome"], x + 50, yy + 150, nsize, "black", INK, ap, align="left", glow=0.18)
    text(c, p["tag"], x + 50, yy + 205, fit(p["tag"], "bold", 32, 1020), "bold", col, ap, align="left")
    for i, (k, sft, fc) in enumerate(p["fatos"]):
        af = ep(t, cue(k) + 0.15 * i, 0.45)
        if af <= 0:
            continue
        fy = yy + 280 + i * 60
        if fc in (GOLD, ROSE):
            ic_warn(c, x + 68, fy - 10, 30, fc, af)
        else:
            check_icon(c, x + 68, fy - 10, 15, af, fc if fc != INK else col)
        text(c, sft, x + 100 + (1 - af) * 16, fy, fit(sft, "semibold", 30, 640 if p.get("stat") else 960), "semibold",
             fc, af, align="left")
    if p.get("stat"):
        k, big, small = p["stat"]
        ast = ep(t, cue(k), 0.5)
        if ast > 0:
            cx = x + w - 200
            sz = fit(big, "black", 92, 330) * (1 + 0.15 * (1 - ast))
            glow_text(c, big, cx, yy + 330, sz, "black", col, ast, glow=0.45)
            text(c, small, cx, yy + 385, 26, "mono", INK2, ast)
    if p.get("nota"):
        text(c, p["nota"], x + w - 30, yy + h - 22, 20, "mono", DIM, ep(t, cue("b") + 0.6, 0.5), align="right")
    # terminal com o comando de instalação
    if p.get("cmd"):
        at = ep(t, ta + 0.8, 0.5)
        terminal(c, x, 700, w, 120, at, title="bash", col=col)
        size = fit("$ " + p["cmd"], "mono", 30, w - 90)
        typed(c, p["cmd"], x + 40, 785, size, t, ta + 1.2, cps=24, a=at, prompt="$")


# ======================================================================  13 — RESUMO
def b_resumo(c, t, C, B):
    ta, tb, tc = C["13.a"], C["13.b"], C["13.c"]
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "RESUMO", "TOP 10 · OUTUBRO 2026", CYAN)
        hi = ep(t, tb, 0.6)
        for i, (sid, p) in enumerate(RANK):
            a = ep(t, ta + 0.32 * i, 0.4)
            if a <= 0:
                continue
            col_i, row = i // 5, i % 5
            x, y = 150 + col_i * 830, 240 + row * 128
            ag = p["nome"] in AGENTES
            col = mix(p["col"], CYAN if ag else DIM, hi)
            panel(c, x, y + (1 - a) * 16, 790, 104, a * (1 - 0.45 * hi * (not ag)), col, k=14, fill=0.85, glow=ag and hi > 0.5)
            yy = y + (1 - a) * 16 + 66
            text(c, f"#{p['pos']}", x + 40, yy, 44, "black", col, a, align="left")
            nm = p["nome"]
            ns = fit(nm, "extrabold", 36, 400)
            nw = text(c, nm, x + 160, yy, ns, "extrabold", INK if (ag or hi < 0.5) else INK2, a, align="left")
            text(c, "+" + fmt(p["ganho"]), x + 760, yy, 30, "monob", INK2, a, align="right")
            if ag and hi > 0:
                chip(c, "AGENTES", x + 180 + text_w(nm, "extrabold", ns), yy - 12, CYAN, hi * a, size=18, filled=True)
        ac = ep(t, tc, 0.5)
        if ac > 0:
            glow_text(c, "7 DE 10 SÃO PARA AGENTES DE IA", W / 2, 905, 50, "black", CYAN, ac, glow=0.4)


# ======================================================================  14 — CTA
def b_cta(c, t, C, B):
    head(c, t, B["start"], "TECH//013", "OBRIGADO POR ASSISTIR", CYAN)
    cta(c, t, C["14.like"], C["14.sub"], C["14.bell"], C["14.com"], C["14.bye"], "Qual desses você vai testar primeiro?")


BLOCKS = dict(gancho=b_gancho, criterio=b_criterio, resumo=b_resumo, cta=b_cta,
              **{f"p{k}": (lambda k: lambda c, t, C, B: b_proj(c, t, C, B, k))(k) for k in PROJ})
