# Short da questão 153 do ENEM 2025 (2º dia, caderno amarelo) — vertical 1080x1920, ~1 min (mínimo de 1 min).
# Modelo do Short antigo de questão (canais/enem/questoes/041, git 5eeb6d2): o print da questão com marca-texto →
# alternativas + "comenta antes de ver" + contagem para pausar → o código montado pedaço por pedaço em casas grandes →
# o código em destaque e a letra D → a armadilha (E: sem o zero e com o 10; A e C: ordem invertida) → o atalho →
# "você acertou?" + convite para a resolução completa.
# Fatos: 2 | 08 | 109 | 0 = 2081090 (D). E = 2|8|109|10 · A = 0|109|08|2 · C = 10|109|8|2.
# Marcas: {cue} · *destaque* · [p=0.2] pausa

TITULO = "Questão do ENEM 2025: qual é o código do visitante?"

VOZ = dict(
    tags=["animada", "curiosa", "confiante"],
    prompt=("Narre um Short de desafio de matemática: voz masculina adulta, enérgica, clara e empolgada, como um "
            "professor de cursinho desafiando os alunos. Ritmo rápido desde a primeira palavra, sem introdução lenta. "
            "Bata forte nos números e nas palavras-chave, dígito por dígito. Tom de suspense antes da resposta e de "
            "surpresa na revelação. Respeite as pausas marcadas. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, pular ou repetir nada."),
)

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.8)

SCENES = [
    dict(id="s01", block="gancho", text=
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Uma empresa dá a cada visitante um *código de sete "
        "dígitos:* [p=0.1] {b}*andar,* [p=0.1] *setor,* [p=0.1] *funcionário* [p=0.1] e *turno.* [p=0.2] {c}O visitante "
        "foi ao *segundo andar,* [p=0.1] *setor zero oito,* [p=0.1] falar com o *funcionário cento e nove,* [p=0.1] às "
        "*dez da manhã.* [p=0.2] {d}Qual é o código dele?"),
    dict(id="s02", block="opcoes", text=
        "{a}São cinco alternativas, [p=0.1] e todas usam os mesmos números. [p=0.2] {b}Comenta antes de ver! [p=0.3] "
        "{c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="s03", block="conta", text=
        "{a}O segredo é montar o código *pedaço por pedaço.* [p=0.2] {b}Andar: [p=0.1] *dois.* [p=0.2] {c}Setor: "
        "[p=0.1] *zero oito,* [p=0.1] com o zero, porque o setor tem *duas casas.* [p=0.2] {d}Funcionário: [p=0.1] "
        "*um, zero, nove.* [p=0.2] {e}Turno: [p=0.1] manhã é *zero.*"),
    dict(id="s04", block="codigo", text=
        "{a}O código é [p=0.1] *dois, zero, oito, um, zero, nove, zero.* [p=0.2] {b}Letra *D!*"),
    dict(id="s05", block="pegadinha", text=
        "{a}E aqui está a armadilha: [p=0.1] {b}quem esquece o zero do setor [p=0.1] e escreve o *dez* do horário "
        "[p=0.1] marca a letra *E.* [p=0.2] {c}O dez é a hora, [p=0.1] não é o turno! [p=0.2] {d}E quem inverte a ordem "
        "dos pedaços [p=0.1] cai na *A* ou na *C.*"),
    dict(id="s06", block="macete", text=
        "{a}E tem um atalho: [p=0.1] o primeiro dígito é o andar, *dois:* [p=0.1] {b}sobram *D* e *E.* [p=0.2] {c}O "
        "segundo é o zero do setor: [p=0.1] {d}só a *D.*"),
    dict(id="s07", block="cta", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a resolução completa, passo a passo, "
        "[p=0.1] está no vídeo da questão [p=0.1] aqui no *Estudativo.*"),
]
