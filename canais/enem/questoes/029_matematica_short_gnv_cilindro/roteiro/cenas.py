# Estudativo · Short 029 — ENEM 2025, questão 146 (a mesma da aula 028): cilindros de GNV de 10, 14, 17, 21 e 25 m³, preço
# proporcional à capacidade; o carro roda 30 km por dia, 7 dias, e gasta 1 m³ a cada 13 km. 30 × 7 = 210 km; 210 ÷ 13 ≈ 16,2
# (13 × 16 = 208, sobram 2 km) → precisa de mais de 16 m³ → o menor que serve é 17 → C.
# Vertical 1080x1920, ~1 min, voz Gemini. Dinâmica de Short: pergunta em 3 s → os cinco cilindros → "comenta antes de ver" +
# contagem para pausar → a conta (210 ÷ 13) → armadilha (16 não basta: sobrou, arredonda para cima) → 17, letra C →
# "você acertou?" + convite para a aula completa (028).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "16 não basta! A questão do cilindro de GNV do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Um carro roda *trinta quilômetros* por dia, [p=0.1] sete "
        "dias por semana, [p=0.2] {b}e gasta *um metro cúbico* de gás [p=0.1] a cada *treze quilômetros.* [p=0.2] {c}Qual "
        "é o cilindro *mais barato* [p=0.1] que aguenta a semana inteira?"),
    dict(id="02", block="opcoes", text=
        "{a}Dez, catorze, dezessete, vinte e um [p=0.1] ou vinte e cinco metros cúbicos? [p=0.2] {b}Comenta antes de ver! "
        "[p=0.2] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="conta", text=
        "{a}Na semana, [p=0.1] trinta vezes sete: [p=0.1] *duzentos e dez quilômetros.* [p=0.2] {b}Cada metro cúbico leva "
        "o carro por treze. [p=0.1] Então, duzentos e dez dividido por treze. [p=0.2] {c}Treze vezes dezesseis [p=0.1] dá "
        "duzentos e oito. [p=0.1] Sobram *dois quilômetros.*"),
    dict(id="04", block="pegadinha", text=
        "{a}E aqui está a armadilha: [p=0.1] *dezesseis* não basta! [p=0.2] {b}Com dezesseis metros cúbicos, [p=0.1] faltam "
        "dois quilômetros, [p=0.1] e o carro para antes do fim da semana. [p=0.2] {c}Sobrou? [p=0.1] *Arredonda para "
        "cima.*"),
    dict(id="05", block="resposta", text=
        "{a}O cilindro precisa ter *mais de dezesseis.* [p=0.2] {b}Catorze não dá. [p=0.1] Vinte e um e vinte e cinco dão, "
        "[p=0.1] mas são mais caros. [p=0.2] {c}O mais barato que aguenta [p=0.1] é o de *dezessete.* [p=0.2] {d}Letra "
        "*C!*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
