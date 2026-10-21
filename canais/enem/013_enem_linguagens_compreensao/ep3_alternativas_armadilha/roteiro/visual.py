"""Visual — Compreensão Global e Tese, Episódio 3: As 5 alternativas-armadilha e o método de 6 passos (tema claro).
Analogia: a alternativa certa é a ROUPA DO TAMANHO EXATO do texto (camisa sobre o contorno tracejado do texto).
Cotidiano: a fofoca da Ana recontada em balões de WhatsApp. Diagrama do alvo com as cinco armadilhas.
Questões 8 e 9: texto inteiro com marca-texto palavra a palavra + etiqueta com o nome da armadilha em cada errada.
Cores: azul = tese/definição · verde = pista/palavra-sinal · âmbar = armadilha · vermelho = erro · roxo = fórmula/regra.
Peças reaproveitadas dos eps. 1 (V1) e 2 (V2).
"""
import importlib.util
import json
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

HERE = Path(__file__).resolve().parent
SERIE = HERE.parent.parent


def _load(nome, path):
    spec = importlib.util.spec_from_file_location(nome, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


V2 = _load("visual_ep2", SERIE / "ep2_resumo_uma_frase" / "roteiro" / "visual.py")
V1 = V2.V
motor.set_theme("claro")
try:   # a classe Leitura do ep. 2 lê os tempos deste episódio
    V2._SC = {s["id"]: s for s in json.load(open(HERE.parent / "audio" / "tempos.json", encoding="utf-8"))["scenes"]}
except Exception:
    V2._SC = {}

MARCA = ""
ARQUIVO_FINAL = "enem_linguagens_compreensao_ep3_alternativas_armadilha.mp4"
CARD_R = (140, 150, 1640, 690)
TESE_CEL = "A escola deve ensinar a usar o celular, não só proibi-lo."
FOFOCA = "A Ana foi promovida no trabalho, mas vai ter que mudar de cidade."

wrap, para, which, frame, head_seq, boxed, regra, selo, pause_timer = (
    V1.wrap, V1.para, V1.which, V1.frame, V1.head_seq, V1.boxed, V1.regra, V1.selo, V1.pause_timer)
wa_bubble, phone, notas, Leitura, colored = V2.wa_bubble, V2.phone, V2.notas, V2.Leitura, V2.colored


# ======================================================================
# a roupa
# ======================================================================

def shirt_path(cx, cy, s):
    """camiseta centrada em (cx, cy); s = meia-largura do corpo"""
    p = skia.Path()
    w, h = s, s * 1.25
    neck = s * 0.32
    sl = s * 0.62
    p.moveTo(cx - neck, cy - h)
    p.quadTo(cx, cy - h + neck * 0.9, cx + neck, cy - h)
    p.lineTo(cx + w, cy - h + s * 0.12)
    p.lineTo(cx + w + sl, cy - h + sl * 0.85)
    p.lineTo(cx + w + sl * 0.55, cy - h + sl * 1.45)
    p.lineTo(cx + w, cy - h + sl * 1.05)
    p.lineTo(cx + w, cy + h)
    p.lineTo(cx - w, cy + h)
    p.lineTo(cx - w, cy - h + sl * 1.05)
    p.lineTo(cx - w - sl * 0.55, cy - h + sl * 1.45)
    p.lineTo(cx - w - sl, cy - h + sl * 0.85)
    p.lineTo(cx - w, cy - h + s * 0.12)
    p.close()
    return p


def camisa(c, cx, cy, s, col, a, rot=0.0, avesso=False):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(rot); c.translate(-cx, -cy)
    p = shirt_path(cx, cy, s)
    c.drawPath(p, paint(col, a))
    c.drawPath(p, paint(mix(col, "#000000", 0.25), a, stroke=4))
    if avesso:
        pe = paint("#FFFFFF", a * 0.9, stroke=3); pe.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
        c.drawPath(shirt_path(cx, cy, s * 0.86), pe)
        rrect(c, cx - s * 0.42, cy - s * 0.55, s * 0.84, s * 0.4, 6, "#FFFFFF", a)
        text_mid(c, "AVESSO", cx, cy - s * 0.35, s * 0.2, "black", RED, a)
        for j in (-1, 1):
            line(c, cx + j * s * 0.86, cy - s * 0.6, cx + j * s * 0.86, cy + s * 1.1, mix(col, "#000000", 0.3), a, 3)
    c.restore()


def contorno(c, cx, cy, s, a, label="tamanho do texto"):
    if a <= 0:
        return
    pe = paint(BLUE, a, stroke=4); pe.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
    c.drawPath(shirt_path(cx, cy, s), pe)
    if label:
        text(c, label, cx, cy + s * 1.25 + 46, 24, "black", BLUE, a)


def guarda_roupa(c, x, y, w, h, a):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 12, "#C8A27A", a, shadow=True)
    rrect(c, x + 14, y + 14, w / 2 - 20, h - 28, 8, "#E6CDB0", a)
    rrect(c, x + w / 2 + 6, y + 14, w / 2 - 20, h - 28, 8, "#E6CDB0", a)
    c.drawCircle(x + w / 2 - 18, y + h / 2, 7, paint("#8B5E3C", a))
    c.drawCircle(x + w / 2 + 18, y + h / 2, 7, paint("#8B5E3C", a))


# ======================================================================
# abertura
# ======================================================================

TRAPS = [("REDUÇÃO", "roupa apertada"), ("EXTRAPOLAÇÃO", "roupa larga demais"), ("CONTRADIÇÃO", "roupa do avesso"),
         ("TEMA CERTO, TESE ERRADA", "da mesma loja, de outra pessoa"), ("VERDADE DO MUNDO", "nem está no guarda-roupa")]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "LINGUAGENS ENEM", "AS 5 ALTERNATIVAS-ARMADILHA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    text(c, "alternativas erradas NÃO são aleatórias", W / 2, 270, 44, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.4)
    for k in range(5):
        a = ab * ep(t, C["01.b"] + 0.25 * k, 0.3)
        x = 400 + k * 280
        if a > 0:
            rrect(c, x - 110, 340, 220, 220, 22, mix("#FFFFFF", AMBER, 0.12), a)
            pe = paint(AMBER, a, stroke=5); pe.setPathEffect(skia.DashPathEffect.Make([16, 10], 0))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 110, 340, 220, 220), 22, 22), pe)
            text_mid(c, str(k + 1), x, 450, 100, "black", AMBER, a)
    text(c, "5 MOLDES", W / 2, 640, 50, "black", AMBER, ab)
    ac = ep(t, C["01.c"], 0.4)
    pill(c, "quem conhece os moldes elimina em SEGUNDOS", W / 2, 740, GREEN, size=32, a=ac, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "reconhecer cada ARMADILHA", "os 5 moldes de alternativa errada"),
            ("02.b", "aplicar o MÉTODO DE 6 PASSOS", "em qualquer questão de interpretação")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")
        text(c, sub, 400, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DUAS LEMBRANÇAS", "EPISÓDIOS 1 E 2", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    pill(c, "EP. 1 · TESE = o que o texto afirma", 300, 240, BLUE, size=28, a=aa, bounds=(0, 1920))
    boxed(c, 300, 290, 1320, 120, BLUE, aa, 0.08)
    text_mid(c, "“" + TESE_CEL + "”", W / 2, 350, 40, "black", BLUE, aa)
    ab = ep(t, C["03.b"], 0.5)
    pill(c, "EP. 2 · RESUMO em uma frase", 300, 480, PURPLE, size=28, a=ab, bounds=(0, 1920))
    V2.pieces_row(c, t, [ab, ep(t, C["03.b"] + 0.4, 0.4), ep(t, C["03.b"] + 0.8, 0.4)], 530, 420, 130, join=1)
    pill(c, "a tese do celular vai servir de exemplo", W / 2, 760, GREEN, size=28, a=ep(t, C["03.c"], 0.4), anchor="center")


def b_roupa(c, t, C, B):
    frame(c, t, B["start"], "O NOME DAS ERRADAS", "DISTRATOR", BLUE)
    aa = ep(t, C["04.a"], 0.5)
    pill(c, "DISTRATOR", 560, 270, AMBER, INK, size=40, a=aa, anchor="center", bounds=(0, 1920))
    text(c, "alternativa errada feita", 560, 360, 36, "bold", INK, aa)
    text(c, "para PARECER certa", 560, 410, 36, "black", AMBER, aa)
    acc = ep(t, C["04.c"], 0.5)
    contorno(c, 1340, 480, 150, acc)
    ad = ep(t, C["04.d"], 0.6)
    camisa(c, 1340, 480 + (1 - ad) * -60, 150, GREEN, ad)
    text(c, "a certa = roupa do", 560, 560, 38, "black", GREEN, ad)
    text(c, "TAMANHO EXATO do texto", 560, 610, 38, "black", GREEN, ad)
    for j, s in enumerate(("nem apertada", "nem larga", "nem do avesso")):
        pill(c, s, 340 + j * 230, 720, INK2, size=24, a=ad * ep(t, C["04.d"] + 1.2 + 0.5 * j, 0.3), anchor="center", bounds=(0, 1920))


def b_fofoca(c, t, C, B):
    frame(c, t, B["start"], "COMO SE FAZ UM DISTRATOR?", "A FOFOCA", AMBER)
    ab = ep(t, C["05.b"], 0.5)
    phone(c, 230, 170, 640, 650, ep(t, C["05.a"], 0.5), "Vizinha")
    wa_bubble(c, [(FOFOCA, INK, 1)], 280, 300, 500, ab, 34, out=False)
    acc = ep(t, C["05.c"], 0.5)
    for k in range(5):
        a = acc * ep(t, C["05.c"] + 0.3 * k, 0.3)
        x = 1020 + (k % 3) * 220 + (110 if k >= 3 else 0)
        y = 330 + (k // 3) * 260
        V1.person(c, x, y, [AMBER, "#F97316", RED, PURPLE, "#0EA5E9"][k], a, 0.9)
        badge_num(c, k + 1, x + 50, y - 30, a, 20, bg=INK)
    text(c, "5 pessoas recontam · 5 jeitos de errar", 1350, 800, 30, "black", AMBER, acc)


# ======================================================================
# as cinco armadilhas (cena 1: fofoca + roupa · cena 2: como reconhecer + mini-exemplo)
# ======================================================================

ARM = {
    "reducao": dict(ids=("06", "07"), nome="REDUÇÃO", conto="A Ana vai mudar de cidade.",
                    defi="pegar uma PARTE como se fosse o TODO", roupa="roupa APERTADA: cobre só um pedaço",
                    regra="verdadeira, mas cobre UM trecho só", ex="O aluno usa o celular às escondidas.",
                    selo_ex="SÓ UM PEDAÇO"),
    "extrapolacao": dict(ids=("08", "09"), nome="EXTRAPOLAÇÃO",
                         conto="A Ana virou diretora da empresa inteira, e vai morar no exterior.",
                         defi="dizer MAIS do que o texto autoriza", roupa="roupa LARGA DEMAIS: passa da borda",
                         regra="desconfie de: sempre · todos · principalmente · deve-se",
                         ex="Todas as escolas devem liberar o celular o tempo todo.", selo_ex="FOI ALÉM",
                         red=("Todas", "o tempo todo.")),
    "contradicao": dict(ids=("10", "11"), nome="CONTRADIÇÃO", conto="A Ana foi rebaixada.",
                        defi="dizer o OPOSTO do texto", roupa="roupa DO AVESSO: lugar certo, sentido trocado",
                        regra="muitas vezes é a opinião que o autor DERRUBA",
                        ex="A escola deve proibir o celular.", selo_ex="O OPOSTO"),
    "temacerto": dict(ids=("12", "13"), nome="TEMA CERTO, TESE ERRADA", conto="A Ana pediu para mudar de emprego.",
                      defi="o MESMO assunto, defendendo OUTRA posição", roupa="roupa da MESMA LOJA, de outra pessoa",
                      regra="as palavras-chave do texto com OUTRO VERBO",
                      ex="A escola deve comprar celulares para os alunos.", selo_ex="OUTRA TESE"),
    "verdade": dict(ids=("14", "15"), nome="VERDADE DO MUNDO", conto="Mudar de cidade custa caro.",
                    defi="CERTA na vida real, mas NÃO está no texto", roupa="roupa bonita que NEM ESTÁ no seu guarda-roupa",
                    regra="pergunte: em que linha isso está?",
                    ex="O uso exagerado do celular pode atrapalhar o sono.", selo_ex="NÃO ESTÁ NO TEXTO"),
}
ARM_ORDEM = ["reducao", "extrapolacao", "contradicao", "temacerto", "verdade"]


def roupa_da(c, t, chave, cx, cy, a, k):
    """a camisa de cada armadilha sobre o contorno tracejado do texto"""
    s = 120
    if chave == "verdade":
        guarda_roupa(c, cx - 250, cy - 170, 260, 340, a)
        contorno(c, cx - 120, cy, 70, a * 0.8, "")
        camisa(c, cx + 140, cy, 110, PURPLE, a * k)
        for j in range(3):
            ang = t * 2 + j * 2.1
            c.drawCircle(cx + 140 + 150 * math.cos(ang), cy - 90 + 30 * math.sin(ang), 6, paint(AMBER, a * k))
        return
    contorno(c, cx, cy, s, a)
    if chave == "reducao":
        camisa(c, cx, cy + 40, s * lerp(1, 0.5, k), AMBER, a * k)
    elif chave == "extrapolacao":
        camisa(c, cx, cy, s * lerp(1, 1.4, k), AMBER, a * k * 0.85)
        contorno(c, cx, cy, s, a, "")
    elif chave == "contradicao":
        camisa(c, cx, cy, s, mix(AMBER, "#FFFFFF", 0.35 * k), a, avesso=k > 0.3)
    elif chave == "temacerto":
        camisa(c, cx, cy, s * 0.92, "#F97316", a * k)
        pill(c, "de OUTRA pessoa", cx, cy + 40, INK, size=22, a=a * k, anchor="center", bounds=(0, 1920))


def armadilha(chave):
    d = ARM[chave]
    s1, s2 = d["ids"]
    n = ARM_ORDEM.index(chave)

    def bloco(c, t, C, B):
        sid = which(t, C, [s1, s2])
        head(c, t, C[s1] if sid == s1 else C[s2], f"ARMADILHA {n + 1} DE 5", d["nome"], AMBER)
        card(c, *CARD_R)
        for k in range(5):
            badge_num(c, k + 1, 800 + k * 80, 205, 1, 20, bg=AMBER if k == n else LIGHT)
        p2 = ep(t, C[s2], 0.6)
        if p2 < 1:
            a = 1 - p2
            # fofoca: original + reconto
            text(c, "a vizinha contou:", 220, 290, 24, "black", GRAY, a, align="left")
            wa_bubble(c, [(FOFOCA, INK2, 1)], 220, 310, 760, a, 28, out=False)
            text(c, f"a pessoa {n + 1} reconta:", 220, 470, 24, "black", AMBER, a * ep(t, C[f"{s1}.t"], 0.4), align="left")
            wa_bubble(c, [(d["conto"], INK, 1)], 220, 490, 760, a * ep(t, C[f"{s1}.t"], 0.4), 34)
            ab = ep(t, C[f"{s1}.b"], 0.4) * a
            pill(c, d["nome"], 600, 690, AMBER, INK, size=34, a=ab, anchor="center", bounds=(0, 1920))
            text(c, d["defi"], 600, 770, 30, "black", INK, ab)
            acr = ep(t, C[f"{s1}.c"], 0.6)
            roupa_da(c, t, chave, 1380, 470, a * ep(t, C[f"{s1}.t"], 0.4), acr)
            text(c, d["roupa"], 1380, 790, 28, "black", AMBER, a * acr)
        if p2 > 0:
            a = p2
            pill(c, "COMO RECONHECER", 260, 290, BLUE, size=26, a=a * ep(t, C[f"{s2}.t"], 0.4), bounds=(0, 1920))
            ar = ep(t, C[f"{s2}.a"], 0.4) * a
            text(c, d["regra"], 260, 380, 40, "black", INK, ar, align="left")
            text(c, "tese do texto:", 260, 470, 24, "black", BLUE, a * ep(t, C[f"{s2}.b"] if chave != "verdade" else C[f"{s2}.a"], 0.4), align="left")
            at = a * ep(t, C[f"{s2}.b"] if chave != "verdade" else C[f"{s2}.a"], 0.4)
            boxed(c, 260, 490, 1400, 84, BLUE, at, 0.06, 16, 3)
            text_mid(c, TESE_CEL, 960, 532, 32, "black", BLUE, at)
            ae = at
            if ae > 0:
                boxed(c, 260, 610, 1400, 100, AMBER, ae, 0.12, 16, 4)
                text(c, "ALTERNATIVA", 290, 640, 18, "black", AMBER, ae, align="left", tracking=1)
                text(c, d["ex"], 290, 690, 34, "black", INK, ae, align="left")
                if chave == "extrapolacao":
                    ak = ep(t, C[f"{s2}.c"], 0.4)
                    for w in d["red"]:
                        x0 = 290 + text_w(d["ex"][:d["ex"].index(w)], "black", 34)
                        line(c, x0, 700, x0 + text_w(w, "black", 34), 700, RED, ae * ak, 5)
                if chave == "temacerto":
                    ak = ep(t, C[f"{s2}.c"], 0.4)
                    w = "comprar"
                    x0 = 290 + text_w(d["ex"][:d["ex"].index(w)], "black", 34)
                    line(c, x0, 700, x0 + text_w(w, "black", 34), 700, RED, ae * ak, 5)
                    w2 = "ensinar"
                    x1 = 960 - text_w(TESE_CEL, "black", 32) / 2 + text_w(TESE_CEL[:TESE_CEL.index(w2)], "black", 32)
                    line(c, x1, 545, x1 + text_w(w2, "black", 32), 545, BLUE, at * ak, 5)
            sc = C[f"{s2}.c"]
            selo(c, 1520, 600, ep(t, sc, 0.4) * a, d["selo_ex"], AMBER, -5, 26)
            if chave == "contradicao":
                for j, w in enumerate(("mas", "porém", "engano")):
                    pill(c, w, 1100 + j * 140, 790, GREEN, size=26, a=a * ep(t, sc + 0.6 + 0.4 * j, 0.3), anchor="center", bounds=(0, 1920))
                text(c, "confira as frases de", 850, 800, 28, "black", GREEN, a * ep(t, sc + 0.4, 0.3), align="right")
            if chave == "verdade":
                regra(c, "Em que linha isso está?", 790, a * ep(t, sc, 0.4), 36)
    return bloco


# ======================================================================
# o alvo, as perguntas, a palavra
# ======================================================================

def b_alvo(c, t, C, B):
    frame(c, t, B["start"], "AS CINCO JUNTAS", "O ALVO", PURPLE)
    a0 = ep(t, C["16.t"], 0.5)
    # região do texto e faixa central
    rrect(c, 300, 230, 1040, 500, 30, "#F7F7F5", a0)
    if a0 > 0:
        pe = paint(LIGHT, a0, stroke=3); pe.setPathEffect(skia.DashPathEffect.Make([12, 8], 0))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(300, 230, 1040, 500), 30, 30), pe)
    text(c, "O TEXTO", 330, 270, 22, "black", GRAY, a0, align="left", tracking=1)
    aa = ep(t, C["16.a"], 0.5)
    rrect(c, 420, 400, 800, 150, 20, BLUE, aa * 0.12)
    if aa > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(420, 400, 800, 150), 20, 20), paint(BLUE, aa, stroke=4))
    text(c, "o que o texto afirma", 820, 390, 24, "black", BLUE, aa)
    rrect(c, 440, 420, 760, 110, 16, GREEN, aa * 0.25)
    text_mid(c, "CERTA", 540, 475, 34, "black", GREEN, aa)
    ab = ep(t, C["16.b"], 0.4)
    rrect(c, 650, 445, 130, 60, 12, AMBER, ab * 0.9)
    text_mid(c, "redução", 715, 475, 22, "black", INK, ab)
    acc = ep(t, C["16.c"], 0.4)
    rrect(c, 1080, 420, 360, 110, 12, AMBER, acc * 0.85)
    text_mid(c, "extrapolação", 1300, 475, 26, "black", INK, acc)
    ad = ep(t, C["16.d"], 0.4)
    rrect(c, 800, 435, 250, 80, 12, RED, ad * 0.85)
    text_mid(c, "− contradição", 925, 475, 24, "black", "#FFFFFF", ad)
    ae = ep(t, C["16.e"], 0.4)
    rrect(c, 520, 580, 420, 100, 14, "#F97316", ae * 0.85)
    text_mid(c, "tema certo, tese errada", 730, 630, 24, "black", "#FFFFFF", ae)
    af = ep(t, C["16.f"], 0.4)
    rrect(c, 1460, 600, 300, 120, 14, PURPLE, af * 0.85)
    text_mid(c, "verdade do mundo", 1610, 660, 24, "black", "#FFFFFF", af)
    text(c, "fora do texto", 1610, 760, 26, "black", PURPLE, af)


def b_perguntas(c, t, C, B):
    frame(c, t, B["start"], "AS 3 PERGUNTAS", "QUE ELIMINAM", PURPLE)
    rows = [("17.b", "O texto diz ISSO?", "não → contradição ou verdade do mundo"),
            ("17.c", "Diz SÓ isso?", "diz mais coisa → redução"),
            ("17.d", "Diz isso TUDO?", "não vai tão longe → extrapolação")]
    for k, (cue, q, r) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 290 + k * 170 + d
        badge_num(c, k + 1, 290, y - 16, a, 36, bg=PURPLE)
        text(c, q, 360, y, 52, "black", INK, a, align="left")
        text(c, r, 360, y + 58, 32, "black", AMBER, ep(t, C[cue] + 1.2, 0.4), align="left")


def b_palavra(c, t, C, B):
    frame(c, t, B["start"], "UMA PALAVRA", "ESTRAGA A ALTERNATIVA", RED)
    aa = ep(t, C["18.a"], 0.5)
    s1 = "O celular deve ser ensinado na escola, porque faz parte da vida dos alunos"
    s2 = " e, por isso, deve ser proibido."
    ab = ep(t, C["18.b"], 0.4)
    if aa > 0:
        boxed(c, 240, 290, 1440, 200, AMBER, aa, 0.10, 18, 4)
        text(c, "ALTERNATIVA", 280, 330, 18, "black", AMBER, aa, align="left", tracking=1)
        colored(c, [(s1, INK, aa), (s2, RED, ab)], 280, 390, 40, 1360)
    check_icon(c, 1600, 270, 30, aa * (1 - ab), GREEN)
    acc = ep(t, C["18.c"], 0.4)
    pill(c, "o erro costuma estar no FIM", W / 2, 590, RED, size=32, a=acc, anchor="center")
    regra(c, "Leia a alternativa até o fim.", 730, ep(t, C["18.d"], 0.5), 40)


FRASES = ["A certa cobre o texto: nem menos, nem mais, nem o contrário.", "Diz isso? Diz só isso? Diz isso tudo?",
          "Em que linha isso está?"]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "35"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 230, y - 16, a, 36, bg=PURPLE)
        text(c, s, 300, y, 44 if k == 0 else 50, "black", INK, a, align="left")


# ======================================================================
# método e avisos
# ======================================================================

PASSOS = [("20.a", "Leia o COMANDO primeiro", "a pergunta antes das alternativas"),
          ("20.b", "Olhe título, fonte e data", ""),
          ("20.c", "Leia o texto inteiro", "marque viradas (mas, porém) e conclusões (portanto)"),
          ("21.a", "Diga a TESE com suas palavras", "ANTES das alternativas"),
          ("21.b", "Elimine pelo tipo de erro", "contradições → extrapolações → reduções"),
          ("21.c", "Sobraram duas? Volte ao texto", "ache a palavra que decide")]


def b_metodo(c, t, C, B):
    frame(c, t, B["start"], "O MÉTODO", "6 PASSOS", PURPLE)
    for k, (cue, s, sub) in enumerate(PASSOS):
        a, d = rise(t, C[cue])
        y = 225 + k * 102 + d
        rrect(c, 230, y - 40, 1460, 88, 16, mix("#FFFFFF", PURPLE, 0.05), a)
        badge_num(c, k + 1, 290, y + 4, a, 28, bg=PURPLE)
        text(c, s, 345, y + 16, 36, "black", INK, a, align="left")
        if sub:
            text(c, sub, 1660, y + 14, 26, "bold", GRAY, a, align="right")


def b_avisos(c, t, C, B):
    head_seq(c, t, C, [("22", "AVISO 1", "NÃO RESPONDA COM A SUA OPINIÃO", RED), ("23", "AVISO 2", "LEIA O COMANDO COM PRECISÃO", BLUE)])
    card(c, *CARD_R)
    p2 = ep(t, C["23"], 0.6)
    if p2 < 1:
        a = 1 - p2
        aa = ep(t, C["22.a"], 0.4) * a
        check_icon(c, 400, 330, 34, aa, RED, "x")
        text(c, "a SUA opinião", 460, 346, 44, "black", RED, aa, align="left")
        check_icon(c, 1060, 330, 34, aa, GREEN)
        text(c, "o que o TEXTO defende", 1120, 346, 44, "black", GREEN, aa, align="left")
        ab = ep(t, C["22.b"], 0.4) * a
        text(c, "a certa pode ser uma ideia da qual você DISCORDA", W / 2, 540, 38, "black", INK, ab)
        text(c, "a errada, uma da qual você CONCORDA", W / 2, 610, 38, "black", INK, ep(t, C["22.b"] + 1.6, 0.4) * a)
    if p2 > 0:
        rows = [("23.b", "“De acordo com o texto”", "o que está ESCRITO"),
                ("23.c", "“Infere-se”", "uma CONCLUSÃO que o texto permite"),
                ("23.d", "“O autor defende”", "a TESE")]
        for k, (cue, cmd, pede) in enumerate(rows):
            a, d = rise(t, C[cue])
            a *= p2
            y = 270 + k * 170 + d
            rrect(c, 230, y - 50, 1460, 120, 18, "#F7F7F5", a)
            text(c, cmd, 270, y + 22, 40, "black", INK, a, align="left")
            text(c, "pede →", 980, y + 22, 30, "bold", GRAY, a, align="left")
            text(c, pede, 1090, y + 22, 34, "black", BLUE, a, align="left")
        ai = ep(t, C["23.c"] + 1.5, 0.4) * p2
        pill(c, "INFERIR = tirar uma conclusão que o texto permite, sem estar escrita com todas as letras", W / 2, 770, BLUE,
             size=22, a=ai * (1 - ep(t, C["23.d"], 0.3)), anchor="center")


# ======================================================================
# questões 8 e 9
# ======================================================================

Q8 = Leitura(
    [("24", "f1", "f2", "Barulho costuma ser tratado como incômodo menor, assunto de reclamação entre vizinhos."),
     ("24", "f2", "c2", "É um erro de escala."),
     ("25", "f3", "c3", "O ruído constante do trânsito e das obras atravessa paredes, interrompe o sono e eleva o estresse de quem não tem como se mudar para uma rua mais calma — em geral, quem mora perto das grandes avenidas porque ali o aluguel é mais barato."),
     ("26", "f4", "c4", "Tratar o barulho como questão de saúde pública, com medição, fiscalização e planejamento urbano, é reconhecer que o silêncio também está mal distribuído.")],
    [(1, "É um erro de escala.", "box", GREEN, None),
     (0, "assunto de reclamação entre vizinhos.", "under", AMBER, "29.b"),
     (2, "trânsito e das obras", "under", AMBER, "28.e"),
     (2, "interrompe o sono", "under", AMBER, "29.d"),
     (2, "quem não tem como se mudar", "under", RED, "28.c"),
     (3, "é reconhecer que o silêncio também está mal distribuído.", "fill", BLUE, "26.c4")])

Q9 = Leitura(
    [("30", "f1", "c1", "A cisterna ao lado da casa mudou menos a paisagem do semiárido do que a rotina de quem vive nele."),
     ("31", "f2", "c2", "A água da chuva, guardada no período chuvoso, passa a estar a poucos passos da cozinha nos meses secos, e a longa caminhada até o açude — tarefa que costumava recair sobre mulheres e crianças — deixa de ser diária."),
     ("31", "f3", "c3", "A tecnologia é simples; o que ela devolve é tempo: para a escola, para o trabalho, para o descanso.")],
    [(0, "mudou menos a paisagem", "under", GREEN, "30.c1b"),
     (1, "deixa de ser diária.", "under", GREEN, "31.c2"),
     (1, "mulheres e crianças", "fill", BLUE, "34.c"),
     (2, "o que ela devolve é tempo:", "fill", BLUE, "31.c3")])

ALTS8 = [("A", "O ruído urbano é um problema de saúde pública que atinge a população de forma desigual e exige ação do poder público.", None, ""),
         ("B", "Conflitos entre vizinhos causados por barulho devem ser resolvidos com diálogo.", "29.b", "TEMA CERTO, TESE ERRADA"),
         ("C", "Quem mora perto das grandes avenidas deveria se mudar para ruas mais calmas.", "28.c", "CONTRADIÇÃO"),
         ("D", "O ruído do trânsito interrompe o sono dos moradores.", "29.d", "REDUÇÃO"),
         ("E", "O barulho das cidades é causado principalmente pelas obras da construção civil.", "28.e", "EXTRAPOLAÇÃO")]
ALTS9 = [("A", "reduzir as doenças ligadas ao consumo de água contaminada.", "34.a", "VERDADE DO MUNDO"),
         ("B", "transformar a paisagem do semiárido.", "33.b", "CONTRADIÇÃO"),
         ("C", "liberar tempo, sobretudo de mulheres e crianças, antes gasto na busca de água.", None, ""),
         ("D", "substituir os açudes como fonte de água da região.", "33.d", "EXTRAPOLAÇÃO"),
         ("E", "acabar com os efeitos da seca no semiárido.", "33.e", "EXTRAPOLAÇÃO")]


def passos(c, t, C, cues, x=1500, y=200):
    """faixa com os 6 passos; acende o passo atual"""
    cur = -1
    for k, cue in enumerate(cues):
        if cue and t >= C[cue] - 0.05:
            cur = k
    for k in range(6):
        on = k == cur
        badge_num(c, k + 1, x + k * 48, y, 1, 20 if on else 15, bg=PURPLE if on else LIGHT)
    text(c, "PASSO", x - 40, y + 8, 18, "black", PURPLE, 1 if cur >= 0 else 0, align="right")


def alternativas(c, t, C, alts, cmd, ok_cue, show_cue, x0, y0, maxw, a=1.0, size=23):
    text(c, cmd, x0 - 40, y0 - 50, 26, "black", BLUE, a * ep(t, C[show_cue], 0.4), align="left")
    aok = ep(t, C[ok_cue], 0.5)
    y = y0
    for L, s, cx, why in alts:
        al, d = rise(t, C[f"{show_cue[:2]}.{L.lower()}"])
        al *= a
        lines = wrap(s, "black", size, maxw)
        hh = len(lines) * (size + 7) + 12 + (26 if cx else 0)
        ok = cx is None
        if ok and aok > 0:
            rrect(c, x0 - 70, y - 30 + d, maxw + 100, hh + 10, 12, GREEN, 0.14 * aok * a)
        badge_num(c, L, x0 - 40, y - 8 + d, al, 20, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cx], 0.4) * a if cx else 0
        for j, ln in enumerate(lines):
            text(c, ln, x0, y + d + j * (size + 7), size, "black", INK, al * (1 - 0.5 * ax), align="left")
            if ax > 0:
                strike(c, x0 - 4, y + d + j * (size + 7) - 8, x0 + 4 + text_w(ln, "black", size), y + d + j * (size + 7) - 8, ax, RED, ax)
        if ax > 0:
            pill(c, why, x0, y + d + len(lines) * (size + 7) + 2, AMBER, INK, size=17, a=ax, bounds=(0, 1920))
        y += hh + 18
    return aok


def b_questao8(c, t, C, B):
    head_seq(c, t, C, [("24", "EU FAÇO", "QUESTÃO 8 · OS 6 PASSOS", BLUE), ("27", "EU FAÇO", "ELIMINANDO PELO NOME", AMBER)])
    card(c, *CARD_R)
    passos(c, t, C, ["24.a", "24.b", "24.c", "26.d", "28.t", None], 1450, 190)
    ph = ep(t, C["27"], 0.7)
    aa = ep(t, C["24.a"], 0.4)
    pill(c, "COMANDO: A tese do texto está expressa em:", 200, 200, BLUE, size=24, a=aa, bounds=(0, 1920))
    pill(c, "sem título · texto feito para a aula", 200, 260, LIGHT, INK, size=20, a=fw(t, C["24.b"], C["24.c"] + 1), bounds=(0, 1920))
    if ph < 1:
        a = 1 - ph
        Q8.draw(c, t, C, 200, 330, 1060, 32, 50, a * ep(t, C["24.c"], 0.4))
        notas(c, t, C, [("24.c2", "VIRADA", "erro de escala: o pequeno é grande", GREEN),
                        ("25.c3", "EXEMPLOS", "o estrago, e QUEM sofre mais", INK2),
                        ("26.c4", "CONCLUSÃO", "o silêncio está mal distribuído", BLUE)], 1310, 330, 110, 430, a)
        ad = ep(t, C["26.d"], 0.5) * a
        if ad > 0:
            wa_bubble(c, [("Minha tese: barulho é problema de saúde, pesa mais para os mais pobres, e o governo precisa agir.", BLUE, 1)],
                      1310, 640, 430, ad, 24)
    if ph > 0:
        Q8.draw(c, t, C, 190, 330, 600, 20, 30, ph * 0.9)
        wa_bubble(c, [("Minha tese: barulho é problema de saúde, pesa mais para os mais pobres, e o governo precisa agir.", BLUE, 1)],
                  190, 640, 600, ph, 22)
        aok = alternativas(c, t, C, ALTS8, "", "29.ok", "27.t", 920, 340, 760, ph, 22)
        result_box(c, "Letra A", 490, 800, 50, aok, GREEN)


def b_questao9(c, t, C, B):
    head_seq(c, t, C, [("30", "VOCÊ FAZ", "QUESTÃO 9", GREEN), ("32", "VOCÊ FAZ", "DÊ O NOME DE CADA ARMADILHA", AMBER),
                       ("33", "CONFERINDO", "QUESTÃO 9", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["30.a"], 0.4)
    pill(c, "COMANDO: De acordo com o texto, a principal contribuição das cisternas é", 200, 200, BLUE, size=22, a=aa, bounds=(0, 1920))
    ph = ep(t, C["32"], 0.7)
    if ph < 1:
        a = 1 - ph
        pill(c, "CISTERNA = tanque que guarda a água da chuva", 200, 260, LIGHT, INK, size=20, a=a * ep(t, C["30.b"], 0.4), bounds=(0, 1920))
        Q9.draw(c, t, C, 200, 340, 1060, 32, 50, a * ep(t, C["30.f1"] - 0.3, 0.4))
        notas(c, t, C, [("30.a", "“DE ACORDO COM O TEXTO”", "vale o que está ESCRITO", BLUE),
                        ("30.c1", "SEMIÁRIDO", "região seca do interior do Nordeste", INK2),
                        ("31.c2", "AÇUDE", "grande reservatório de água", INK2),
                        ("31.c3", "CONCLUSÃO", "o que ela devolve é TEMPO", BLUE)], 1310, 300, 110, 430, a)
    if ph > 0:
        Q9.draw(c, t, C, 190, 330, 600, 21, 31, ph * 0.9)
        aok = alternativas(c, t, C, ALTS9, "", "34.ok", "32.t", 920, 330, 760, ph, 24)
        pause_timer(c, t, C["32.end"] - 1.7, 490, 700, ph)
        result_box(c, "Letra C", 490, 760, 50, aok, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "ONDE A TESE SE ESCONDE", PURPLE)
    ab = ep(t, C["36.b"], 0.4)
    for k, (s, pos) in enumerate((("no começo?", 0), ("no fim?", 6), ("em lugar nenhum?", -1))):
        a = ab * ep(t, C["36.b"] + 0.7 * k, 0.4)
        x = 480 + k * 480
        if a <= 0:
            continue
        rrect(c, x - 140, 230, 280, 360, 18, "#FFFFFF", a, shadow=True)
        for j in range(7):
            col = BLUE if j == pos else LINE
            line(c, x - 100, 280 + j * 44, x + 100 - (j % 3) * 30, 280 + j * 44, col, a, 14 if j == pos else 10)
        if pos < 0:
            text_mid(c, "?", x, 410, 120, "black", PURPLE, a * 0.8)
        text(c, s, x, 650, 34, "black", INK, a)
    pill(c, "ep. 4 · onde a tese se esconde", W / 2, 760, PURPLE, size=34, a=ep(t, C["36.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"], "Quantas armadilhas das cisternas você acertou?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, roupa=b_roupa, fofoca=b_fofoca,
              reducao=armadilha("reducao"), extrapolacao=armadilha("extrapolacao"), contradicao=armadilha("contradicao"),
              temacerto=armadilha("temacerto"), verdade=armadilha("verdade"), alvo=b_alvo, perguntas=b_perguntas,
              palavra=b_palavra, recap=b_recap, metodo=b_metodo, avisos=b_avisos, questao8=b_questao8,
              questao9=b_questao9, ponte=b_ponte, cta=b_cta)
