# Estudativo · Short 015 — ENEM 2025, questão 139 (a mesma da aula 014): o padrão de velocidade de internet será a
# MEDIANA das velocidades de dez cidades (390, 380, 320, 390, 340, 380, 390, 400, 350, 360 MB/s). → 380 (C).
# Vertical 1080x1920, ~1 min, voz Gemini.
# Dinâmica de Short: pergunta em 3 s → opções → "comenta antes de ver" + contagem para pausar → pegadinha (5º e 6º da TABELA: 340 e 380 → 360, A) → em ordem: 380 e 380 → 380 → resposta C (370 é
# a média, 390 é a moda) → "você acertou?" + convite para a aula completa (014).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Média, moda ou mediana? A pegadinha da internet no ENEM 2025"

VOZ = dict(
    tags=["animada", "curiosa", "confiante"],
    prompt=("Narre um Short de desafio de matemática: voz masculina adulta, enérgica, clara e empolgada, como um "
            "professor de cursinho desafiando os alunos. Ritmo rápido desde a primeira palavra, sem introdução lenta. "
            "Bata forte nos números e nas palavras-chave. Tom de suspense antes da resposta e de surpresa na revelação. "
            "Respeite as pausas marcadas. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular ou "
            "repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.8)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Dez cidades, [p=0.1] dez velocidades de internet. [p=0.2] "
        "{b}A empresa vai adotar a *mediana* desses valores. [p=0.2] {c}Qual velocidade ela vai escolher?"),
    dict(id="02", block="opcoes", text=
        "{a}As opções: [p=0.1] trezentos e sessenta, [p=0.1] trezentos e setenta, [p=0.1] trezentos e oitenta, [p=0.1] "
        "trezentos e noventa [p=0.1] ou quatrocentos. [p=0.2] {b}Comenta antes de ver! [p=0.2] {c}Pausa e pensa. "
        "[p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="pegadinha", text=
        "{a}Se você pegou o quinto e o sexto valor *da tabela,* [p=0.1] trezentos e quarenta e trezentos e oitenta, "
        "[p=0.1] deu trezentos e sessenta: [p=0.1] letra A. [p=0.2] {b}*Pegadinha!* [p=0.1] A mediana só vale com a "
        "lista *em ordem.*"),
    dict(id="04", block="ordenar", text=
        "{a}Então, em ordem, [p=0.1] da menor para a maior: [p=0.2] trezentos e vinte, [p=0.1] trezentos e quarenta, "
        "[p=0.1] trezentos e cinquenta, [p=0.1] trezentos e sessenta, [p=0.1] trezentos e oitenta, [p=0.1] trezentos e "
        "oitenta, [p=0.1] trezentos e noventa, [p=0.1] trezentos e noventa, [p=0.1] trezentos e noventa [p=0.1] e "
        "quatrocentos. [p=0.2] {b}São dez valores: [p=0.1] o meio fica entre o *quinto* e o *sexto.*"),
    dict(id="05", block="meio", text=
        "{a}O quinto é trezentos e oitenta, [p=0.1] e o sexto também. [p=0.2] {b}A média dos dois: [p=0.1] *trezentos "
        "e oitenta.*"),
    dict(id="06", block="resposta", text=
        "{a}*Trezentos e oitenta!* [p=0.1] Trezentos e setenta é a *média,* [p=0.1] trezentos e noventa é a *moda,* "
        "[p=0.1] e quatrocentos é só o *maior.* [p=0.2] {b}Letra *C.*"),
    dict(id="07", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
