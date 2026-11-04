# Estudativo · Short 021 — ENEM 2025, questão 142 (a mesma da aula 020): gráfico da frequência respiratória de quem medita.
# Antes de t1: constante em f1; de t1 a t2: desce; depois de t2: constante em f2 → "diminui até t2 e depois fica
# constante" (D). Vertical 1080x1920, ~1 min, voz Gemini.
# Dinâmica de Short: pergunta em 3 s → opções → "comenta antes de ver" + contagem para pausar → pegadinha (inversamente
# proporcional: a curva desce, mas a inversa nunca deita) → leitura trecho por trecho → letra D (+ por que não é
# diretamente proporcional) → "você acertou?" + convite para a aula completa (020).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "O gráfico da respiração na meditação: a pegadinha do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] O gráfico mostra quantas vezes por minuto [p=0.1] uma "
        "pessoa respira enquanto medita. [p=0.2] {b}A meditação começa em *tê um.* [p=0.2] {c}Daí em diante, [p=0.1] "
        "o que acontece com a respiração?"),
    dict(id="02", block="opcoes", text=
        "{a}As opções: [p=0.1] fica constante, [p=0.1] diretamente proporcional, [p=0.1] inversamente proporcional, "
        "[p=0.1] diminui e depois fica constante, [p=0.1] ou diminui o tempo todo. [p=0.2] {b}Comenta antes de ver! "
        "[p=0.2] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="pegadinha", text=
        "{a}Se você marcou *inversamente proporcional,* [p=0.1] caiu na pegadinha. [p=0.2] {b}A curva desce, sim, "
        "[p=0.1] mas a inversa *nunca fica deitada.* [p=0.2] {c}E aqui, [p=0.1] depois de tê dois, [p=0.1] a linha "
        "*deita.*"),
    dict(id="04", block="trechos", text=
        "{a}Lendo trecho por trecho: [p=0.2] {b}de tê um até tê dois, [p=0.1] a linha *desce:* [p=0.1] a respiração "
        "*diminui.* [p=0.2] {c}Depois de tê dois, [p=0.1] a linha fica *deitada:* [p=0.1] a respiração é "
        "*constante.*"),
    dict(id="05", block="resposta", text=
        "{a}*Diminui, [p=0.1] e depois fica constante!* [p=0.2] {b}Letra *D.* [p=0.2] {c}E não é diretamente "
        "proporcional: [p=0.1] o tempo sobe, [p=0.1] e a respiração desce."),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
