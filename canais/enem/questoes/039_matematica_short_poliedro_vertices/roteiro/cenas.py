# Estudativo · Short 039 — ENEM 2025, questão 151 (a mesma da aula 038): quantos vértices tem a cúpula pentagonal
# giralongada? Faces: 1 decágono + 1 pentágono + 5 quadrados + 25 triângulos = 32. Lados: 75 + 20 + 5 + 10 = 110 →
# 55 arestas. Euler: V = 2 + 55 − 32 = 25 → B. Conferência: 5 + 10 + 10.
# Vertical 1080x1920, ~1 min, voz Gemini. Dinâmica de Short: pergunta em 3 s com o sólido girando → as alternativas,
# "comenta antes de ver" + contagem para pausar → faces, lados, arestas e Euler → armadilha (110 = lados, 55 = arestas)
# + conferência nos anéis → 25, letra B → "você acertou?" + convite para a aula completa (038).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Quantos vértices tem esse poliedro? A questão de Euler do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Esse sólido se chama *cúpula pentagonal giralongada.* "
        "[p=0.2] {b}Quantos *vértices* ele tem?"),
    dict(id="02", block="opcoes", text=
        "{a}Vinte e um, [p=0.1] vinte e cinco, [p=0.1] cinquenta e cinco, [p=0.1] oitenta [p=0.1] ou cento e dez? "
        "[p=0.2] {b}Comenta antes de ver! [p=0.3] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="conta", text=
        "{a}Primeiro, as faces: [p=0.1] um decágono, [p=0.1] um pentágono, [p=0.1] cinco quadrados [p=0.1] e vinte e "
        "cinco triângulos. [p=0.1] *Trinta e duas faces.* [p=0.2] {b}Agora some os lados: [p=0.1] setenta e cinco, "
        "[p=0.1] mais vinte, [p=0.1] mais cinco, [p=0.1] mais dez: [p=0.1] *cento e dez.* [p=0.2] {c}Cada aresta junta "
        "dois lados: [p=0.1] *cinquenta e cinco arestas.* [p=0.2] {d}E a relação de Euler: [p=0.1] vértices menos "
        "arestas mais faces [p=0.1] dá dois. [p=0.2] {e}Então: [p=0.1] dois, [p=0.1] mais cinquenta e cinco, [p=0.1] "
        "menos trinta e dois: [p=0.1] *vinte e cinco!*"),
    dict(id="04", block="pegadinha", text=
        "{a}E aqui está a armadilha: [p=0.1] cento e dez são os *lados* das faces, [p=0.1] não os vértices! [p=0.2] "
        "{b}E cinquenta e cinco são as *arestas.* [p=0.2] {c}Conferindo no sólido: [p=0.1] cinco em cima, [p=0.1] dez "
        "no meio [p=0.1] e dez embaixo."),
    dict(id="05", block="resposta", text=
        "{a}São *vinte e cinco vértices.* [p=0.2] {b}Letra *B!*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
