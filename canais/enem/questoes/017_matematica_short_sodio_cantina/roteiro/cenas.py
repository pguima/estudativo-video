# Estudativo · Short 017 — ENEM 2025, questão 140 (a mesma da aula 016): cinco lanches da cantina, o rótulo dá o sódio
# POR PORÇÃO e a estudante quer o menor sódio TOTAL POR PACOTE. Chips 3 × 170 = 510 · Palitos 4 × 501 = 2.004 ·
# Multigrãos 8 × 264 = 2.112 · Polvilho 6 × 175 = 1.050 · Água e sal 5 × 166 = 830 → batata chips (A).
# Vertical 1080x1920, ~1 min, voz Gemini.
# Dinâmica de Short: pergunta em 3 s → opções → "comenta antes de ver" + contagem para pausar → pegadinha (o menor POR
# PORÇÃO: 166, água e sal, E) → os cinco totais → resposta A (510) → "você acertou?" + convite para a aula completa (016).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Qual lanche tem menos sódio? A pegadinha do rótulo no ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Cinco lanches da cantina. [p=0.2] {b}Qual tem *menos "
        "sódio* no pacote inteiro? [p=0.2] {c}Detalhe: [p=0.1] o rótulo mostra o sódio de *uma porção* só."),
    dict(id="02", block="opcoes", text=
        "{a}As opções: [p=0.1] batata chips, [p=0.1] palitos salgados, [p=0.1] biscoito multigrãos, [p=0.1] biscoito "
        "de polvilho [p=0.1] ou biscoito de água e sal. [p=0.2] {b}Comenta antes de ver! [p=0.2] {c}Pausa e pensa. "
        "[p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="pegadinha", text=
        "{a}Se você foi no menor número do rótulo, [p=0.1] cento e sessenta e seis, [p=0.1] do biscoito de água e sal, "
        "[p=0.1] marcou a letra E. [p=0.2] {b}*Pegadinha!* [p=0.1] Isso é *uma* porção, [p=0.1] e esse pacote tem "
        "*cinco.*"),
    dict(id="04", block="contas", text=
        "{a}O total é porções vezes sódio por porção. [p=0.2] {b}Batata: [p=0.1] três vezes cento e setenta, [p=0.1] "
        "quinhentos e dez. [p=0.2] {c}Palitos: [p=0.1] quatro vezes quinhentos e um, [p=0.1] dois mil e quatro. "
        "[p=0.2] {d}Multigrãos: [p=0.1] oito vezes duzentos e sessenta e quatro, [p=0.1] dois mil cento e doze. "
        "[p=0.2] {e}Polvilho: [p=0.1] seis vezes cento e setenta e cinco, [p=0.1] mil e cinquenta. [p=0.2] {f}Água e "
        "sal: [p=0.1] cinco vezes cento e sessenta e seis, [p=0.1] oitocentos e trinta."),
    dict(id="05", block="resposta", text=
        "{a}O menor é *quinhentos e dez!* [p=0.2] {b}Batata chips, [p=0.1] letra *A.* [p=0.2] {c}E as gramas da "
        "porção? [p=0.1] Nem entram na conta."),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
