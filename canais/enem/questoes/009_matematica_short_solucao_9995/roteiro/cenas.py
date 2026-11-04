# Estudativo · Short 009 — ENEM 2025, questão 137 (a mesma da aula 008): 10 L de solução, 99,95% de S1 → 99,90%.
# Quanto S1 sai? → 5 L (E). Vertical 1080x1920, ~55 s, voz Gemini. Dinâmica de Short: pergunta em 3 s → opções →
# "comenta antes de ver" + contagem para pausar → pegadinha (A) → o que não muda (S2) → a % dobrou, o total cai à metade
# → resposta E → "você acertou?" + convite para a aula completa (008).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Essa questão do ENEM parece uma gotinha... mas sai METADE do recipiente"

VOZ = dict(
    tags=["animada", "curiosa", "confiante"],
    prompt=("Narre um Short de desafio de matemática: voz masculina adulta, enérgica, clara e empolgada, como um "
            "professor de cursinho desafiando os alunos. Ritmo rápido desde a primeira palavra, sem introdução lenta. "
            "Bata forte nos números e nas palavras-chave. 'S um' e 'S dois' são os nomes das substâncias (leia 'ésse um' "
            "e 'ésse dois'). Tom de suspense antes da resposta e de surpresa na revelação. Respeite as pausas marcadas. "
            "Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular ou repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.8)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Dez litros de solução: [p=0.1] noventa e nove vírgula "
        "noventa e cinco por cento é S um. [p=0.2] {b}Você vai tirar só S um, [p=0.1] até ele virar noventa e nove "
        "vírgula noventa por cento. [p=0.2] {c}Quanto sai?"),
    dict(id="02", block="opcoes", text=
        "{a}As opções vão de *cinco mililitros* [p=0.1] até *cinco litros.* [p=0.2] {b}Comenta antes de ver! [p=0.2] "
        "{c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="pegadinha", text=
        "{a}Se você subtraiu as porcentagens, [p=0.1] deu zero vírgula zero zero cinco litro: [p=0.1] letra A. [p=0.2] "
        "{b}*Pegadinha!* [p=0.1] As porcentagens são de *totais diferentes.*"),
    dict(id="04", block="segredo", text=
        "{a}O segredo é olhar para o que *não muda:* [p=0.1] o S dois. [p=0.2] {b}Ele é o que falta para cem: "
        "[p=0.1] zero vírgula zero cinco por cento de dez litros, [p=0.1] *zero vírgula zero zero cinco litro.*"),
    dict(id="05", block="dobro", text=
        "{a}No final, essa mesma quantidade [p=0.1] tem que ser zero vírgula dez por cento. [p=0.1] A porcentagem "
        "*dobrou.* [p=0.2] {b}Então o total cai pela *metade:* [p=0.1] *cinco litros.*"),
    dict(id="06", block="resposta", text=
        "{a}Saem *cinco litros* de S um! [p=0.1] Metade do recipiente. [p=0.2] {b}Letra *E.*"),
    dict(id="07", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
