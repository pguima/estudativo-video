# Estudativo · Short 023 — ENEM 2025, questão 143 (a mesma da aula 022): marca de referência dos 100 m rasos = 10,00 s;
# Usain Bolt (2009) = 9,58 s. Diferença: 10,00 − 9,58 = 0,42 s (B). Vertical 1080x1920, ~1 min, voz Gemini.
# Dinâmica de Short: pergunta em 3 s → opções → "comenta antes de ver" + contagem para pausar → armadilhas (0,52 e 1,42:
# esqueceu de descontar um empréstimo) → a conta com os empréstimos em cadeia → 0,42, letra B, conferência pela soma →
# "você acertou?" + convite para a aula completa (022).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "10,00 − 9,58: a conta do recorde de Usain Bolt no ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Nos cem metros rasos, [p=0.1] a marca de referência é "
        "*dez segundos.* [p=0.2] {b}Usain Bolt fez *nove vírgula cinquenta e oito.* [p=0.2] {c}Qual é a diferença?"),
    dict(id="02", block="opcoes", text=
        "{a}As opções: [p=0.1] zero vírgula zero dois, [p=0.1] zero vírgula quarenta e dois, [p=0.1] zero vírgula "
        "cinquenta e dois, [p=0.1] um vírgula zero dois [p=0.1] ou um vírgula quarenta e dois. [p=0.2] {b}Comenta "
        "antes de ver! [p=0.2] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="pegadinha", text=
        "{a}Se deu zero vírgula cinquenta e dois [p=0.1] ou um vírgula quarenta e dois, [p=0.1] caiu na armadilha. "
        "[p=0.2] {b}Você pegou um empréstimo [p=0.1] e esqueceu de *descontar.*"),
    dict(id="04", block="conta", text=
        "{a}Vírgula embaixo de vírgula: [p=0.1] dez vírgula zero zero [p=0.1] menos nove vírgula cinquenta e oito. "
        "[p=0.2] {b}Zero menos oito não dá: [p=0.1] o dez vira *nove inteiros, [p=0.1] nove décimos [p=0.1] e dez "
        "centésimos.* [p=0.2] {c}Dez menos oito, [p=0.1] dois. [p=0.1] Nove menos cinco, [p=0.1] quatro. [p=0.1] Nove "
        "menos nove, [p=0.1] zero."),
    dict(id="05", block="resposta", text=
        "{a}*Zero vírgula quarenta e dois segundo!* [p=0.2] {b}Letra *B.* [p=0.2] {c}Confere: [p=0.1] nove vírgula "
        "cinquenta e oito mais zero vírgula quarenta e dois [p=0.1] dá exatamente *dez.*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
