# Estudativo · Short 019 — ENEM 2025, questão 141 (a mesma da aula 018): prisma hexagonal regular reto + tronco de
# pirâmide hexagonal em cima; faces congruentes → mesma cor. Por fora: 1 hexágono + 6 retângulos + 6 trapézios + 1 hexágono
# menor → 4 cores (D). Vertical 1080x1920, ~1 min, voz Gemini.
# Dinâmica de Short: pergunta em 3 s → opções → "comenta antes de ver" + contagem para pausar → pegadinha (os dois
# hexágonos da mesma cor: 3, E) → as bases coladas somem e as faces de fora ganham cor, tipo a tipo → 4 cores, letra D →
# "você acertou?" + convite para a aula completa (018).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Quantas cores para pintar? A pegadinha dos hexágonos no ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Um prisma hexagonal [p=0.1] com um tronco de pirâmide em "
        "cima. [p=0.2] {b}Faces *congruentes* [p=0.1] ganham a *mesma cor.* [p=0.2] {c}Quantas cores vão ser usadas?"),
    dict(id="02", block="opcoes", text=
        "{a}As opções: [p=0.1] nove, [p=0.1] oito, [p=0.1] seis, [p=0.1] quatro [p=0.1] ou três. [p=0.2] {b}Comenta "
        "antes de ver! [p=0.2] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="pegadinha", text=
        "{a}Se você pintou os dois hexágonos da mesma cor, [p=0.1] deu três: [p=0.1] letra E. [p=0.2] {b}*Pegadinha!* "
        "[p=0.1] Congruente é mesma forma *e* mesmo tamanho. [p=0.2] O de cima é *menor:* [p=0.1] mesma forma, "
        "[p=0.1] tamanho diferente. [p=0.1] Não é congruente."),
    dict(id="04", block="faces", text=
        "{a}Primeiro: [p=0.1] as bases coladas ficam *dentro,* [p=0.1] sem tinta. [p=0.2] {b}Por fora, [p=0.1] os seis "
        "retângulos: [p=0.1] *uma cor.* [p=0.2] {c}Os seis trapézios: [p=0.1] *outra cor.* [p=0.2] {d}O hexágono de "
        "baixo: [p=0.1] *a terceira.* [p=0.2] {e}E o hexágono menor, lá em cima: [p=0.1] *a quarta.*"),
    dict(id="05", block="resposta", text=
        "{a}*Quatro cores!* [p=0.2] {b}Letra *D.* [p=0.2] {c}São catorze faces, [p=0.1] mas só quatro tipos. [p=0.3] "
        "{d}E se fosse uma pirâmide inteira em cima? [p=0.2] Sem o hexágono de cima: [p=0.1] só *três* cores."),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
