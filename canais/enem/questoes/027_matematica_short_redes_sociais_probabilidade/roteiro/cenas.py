# Estudativo · Short 027 — ENEM 2025, questão 145 (a mesma da aula 026): 90% dos internautas brasileiros acessam redes
# sociais e 60% dos que acessam são mulheres. Sorteando um internauta qualquer, P(homem que acessa) = 40% de 90% = 0,36 =
# 36/100 → B. Com 100 internautas: 90 acessam (54 mulheres + 36 homens) e 10 não.
# Vertical 1080x1920, ~1 min, voz Gemini. Dinâmica de Short: pergunta em 3 s → as cinco frações → "comenta antes de ver" +
# contagem para pausar → armadilhas (40/100: os 40% são de quem acessa, não de todo mundo; 90 embaixo: só quem acessa) → imagine 100 → 36/100, letra B →
# "você acertou?" + convite para a aula completa (026).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Não é 40%! A questão de probabilidade das redes sociais do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] *Noventa por cento* dos internautas acessam redes sociais. "
        "[p=0.2] {b}E *sessenta por cento* de quem acessa [p=0.1] são mulheres. [p=0.2] {c}Sorteando um internauta "
        "qualquer, [p=0.1] qual é a chance de ser um *homem que acessa?*"),
    dict(id="02", block="opcoes", text=
        "{a}Qual dessas cinco frações é a resposta? [p=0.2] {b}Comenta antes de ver! [p=0.2] {c}Pausa e pensa. [p=0.1] "
        "Valendo! [p=3.2]"),
    dict(id="03", block="pegadinha", text=
        "{a}A armadilha é responder *quarenta em cem.* [p=0.2] {b}Os quarenta por cento de homens [p=0.1] são de quem "
        "*acessa,* [p=0.2] {c}e não de *todo mundo.* [p=0.3] {d}E quem põe *noventa* embaixo [p=0.1] sorteia só entre quem "
        "acessa. [p=0.2] Mas a questão sorteia entre *todos.*"),
    dict(id="04", block="conta", text=
        "{a}Imagine *cem* internautas. [p=0.2] {b}Noventa acessam redes sociais, [p=0.1] e dez não. [p=0.2] {c}Dos "
        "noventa, [p=0.1] sessenta por cento são mulheres: [p=0.1] *cinquenta e quatro.* [p=0.2] {d}Sobram *trinta e seis* "
        "homens."),
    dict(id="05", block="resposta", text=
        "{a}Trinta e seis homens que acessam, [p=0.1] em cem internautas: [p=0.1] *trinta e seis em cem.* [p=0.2] {b}Ou "
        "direto: [p=0.1] quarenta por cento de noventa por cento, [p=0.1] zero vírgula trinta e seis. [p=0.2] {c}Letra "
        "*B!*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
