# Estudativo · Short 035 — ENEM 2025, questão 149 (a mesma da aula 034): escola de idiomas; pizza de 2023 em porcentagem
# (inglês 60%, espanhol 25%, francês 10%, alemão 5%) e barras de 2024 em quantidade (280, 80, 20, 20). Em 2025: total de
# 2024 e porcentagens de 2023. Total = 400; francês = 10% de 400 = 40 → E.
# Vertical 1080x1920, ~1 min, voz Gemini. Dinâmica de Short: pergunta em 3 s → os dois gráficos → "comenta antes de ver" +
# contagem para pausar → o total (400) → armadilha (20 é o francês de 2024; 2 é 10% de 20) → 40, letra E →
# "você acertou?" + convite para a aula completa (034).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Quantos alunos no francês? A questão dos dois gráficos do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Uma escola de idiomas tem *dois gráficos.* [p=0.2] {b}A "
        "pizza mostra as *porcentagens* de dois mil e vinte e três, [p=0.1] {c}e as barras, [p=0.1] as *quantidades* de "
        "dois mil e vinte e quatro."),
    dict(id="02", block="opcoes", text=
        "{a}Em dois mil e vinte e cinco, [p=0.1] o total vai ser o de dois mil e vinte e quatro, [p=0.1] com as "
        "porcentagens de dois mil e vinte e três. [p=0.2] Quantos alunos no *francês?* [p=0.2] {b}Comenta antes de ver! "
        "[p=0.3] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="conta", text=
        "{a}Primeiro, [p=0.1] o total de dois mil e vinte e quatro: [p=0.1] duzentos e oitenta, [p=0.1] mais oitenta, "
        "[p=0.1] mais vinte, [p=0.1] mais vinte. [p=0.2] {b}*Quatrocentos* alunos. [p=0.2] {c}O francês tinha *dez por "
        "cento* em dois mil e vinte e três. [p=0.1] Dez por cento de quatrocentos: [p=0.1] *quarenta.* [p=0.2] {d}Conferindo: "
        "[p=0.1] sessenta por cento dá duzentos e quarenta, [p=0.1] vinte e cinco por cento dá cem, [p=0.1] e cinco por "
        "cento dá vinte. [p=0.1] Somando tudo, [p=0.1] quatrocentos. [p=0.1] Fechou!"),
    dict(id="04", block="pegadinha", text=
        "{a}E aqui está a armadilha: [p=0.1] a barra do francês mostra *vinte!* [p=0.2] {b}Mas esse é o número de dois "
        "mil e vinte e quatro, [p=0.1] não a previsão. [p=0.2] {c}E quem calcula dez por cento de vinte [p=0.1] chega em "
        "*dois,* [p=0.1] que também está errado."),
    dict(id="05", block="resposta", text=
        "{a}O francês vai ter *quarenta* alunos, [p=0.1] o dobro de antes. [p=0.2] {b}Letra *E!*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
