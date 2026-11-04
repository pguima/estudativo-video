# Estudativo · Short 013 — ENEM 2025, questão 138 (a mesma da aula 012): caminhão-tanque; em toda viagem um mesmo
# volume é descartado. Enviou 10.200, chegaram 9.900; novo pedido: o dobro de 10.000. Envio mínimo? → 20.300 L (C).
# Vertical 1080x1920, ~1 min, voz Gemini.
# Dinâmica de Short: pergunta em 3 s → opções → "comenta antes de ver" + contagem para pausar → o descarte (300 L) →
# pegadinha (2 × 10.200 = 20.400, D: o descarte não dobra) → 20.000 + 300 = 20.300 → resposta C → "você acertou?" +
# convite para a aula completa (012).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Quanto combustível o caminhão deve levar? A pegadinha do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Em toda viagem, [p=0.1] o caminhão-tanque descarta *o "
        "mesmo volume* de combustível. [p=0.2] {b}Mandaram dez mil e duzentos litros, [p=0.1] e chegaram só *nove mil e "
        "novecentos.* [p=0.2] {c}Agora o posto quer *o dobro* de dez mil litros. [p=0.1] Quanto mandar, no mínimo?"),
    dict(id="02", block="opcoes", text=
        "{a}As opções: [p=0.1] vinte mil e cem, [p=0.1] vinte mil e duzentos, [p=0.1] vinte mil e trezentos, [p=0.1] "
        "vinte mil e quatrocentos [p=0.1] ou vinte mil e seiscentos. [p=0.2] {b}Comenta antes de ver! [p=0.2] {c}Pausa "
        "e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="descarte", text=
        "{a}Primeiro, o descarte: [p=0.1] dez mil e duzentos menos nove mil e novecentos. [p=0.2] {b}*Trezentos "
        "litros.*"),
    dict(id="04", block="pegadinha", text=
        "{a}Se você dobrou tudo, [p=0.1] duas vezes dez mil e duzentos, [p=0.1] deu vinte mil e quatrocentos: [p=0.1] "
        "letra D. [p=0.2] {b}*Pegadinha!* [p=0.1] O descarte *não depende* da quantidade. [p=0.1] Ele *não dobra.*"),
    dict(id="05", block="conta", text=
        "{a}O posto quer vinte mil litros. [p=0.2] {b}Mais os trezentos do descarte: [p=0.1] *vinte mil e "
        "trezentos.*"),
    dict(id="06", block="resposta", text=
        "{a}*Vinte mil e trezentos litros!* [p=0.1] Tira o descarte, [p=0.1] e chegam exatamente vinte mil. [p=0.2] "
        "{b}Letra *C.*"),
    dict(id="07", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
