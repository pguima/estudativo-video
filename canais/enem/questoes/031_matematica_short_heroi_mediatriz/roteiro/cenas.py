# Estudativo · Short 031 — ENEM 2025, questão 147 (a mesma da aula 030): num jogo, o herói é atacado pelo vilão mais
# próximo; os vilões estão em T(2; 4) e V(8; 6), cantos do quadrado STUV, e o herói começa em S(6; 2). O caminho sem ataque
# é a mediatriz de TV: ponto médio (5; 5), TV sobe 2 e anda 6 (1/3), perpendicular −3 → y = −3x + 20 → A.
# Vertical 1080x1920, ~1 min, voz Gemini. Dinâmica de Short: pergunta em 3 s → as cinco retas → "comenta antes de ver" +
# contagem para pausar → a mediatriz e o ponto médio → armadilha (o sinal: D e E usam +3) → a equação, letra A →
# "você acertou?" + convite para a aula completa (030).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Por onde o herói foge dos dois vilões? A questão da mediatriz do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Num jogo, [p=0.1] o herói é atacado pelo vilão *mais perto.* "
        "[p=0.2] {b}Os dois vilões estão em *T* e em *V,* [p=0.1] cantos de um quadrado. [p=0.2] {c}Por qual caminho "
        "[p=0.1] o herói anda *sem ser atacado?*"),
    dict(id="02", block="opcoes", text=
        "{a}Ípsilon igual a menos três xis mais vinte? [p=0.1] Mais dezesseis? [p=0.1] Menos vinte? [p=0.1] Ou será "
        "que é mais três xis? [p=0.2] {b}Comenta antes de ver! [p=0.2] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="conta", text=
        "{a}Ficar à mesma distância de dois pontos [p=0.1] é andar na *mediatriz* entre eles. [p=0.2] {b}T fica no ponto "
        "dois e quatro, [p=0.1] e V, no oito e seis. [p=0.1] O meio do caminho é o ponto *cinco e cinco.* [p=0.2] {c}De T "
        "até V, [p=0.1] o ípsilon sobe dois [p=0.1] e o xis anda seis: [p=0.1] inclinação de *um terço.*"),
    dict(id="04", block="pegadinha", text=
        "{a}E aqui está a armadilha: [p=0.1] a mediatriz é *perpendicular!* [p=0.2] {b}A inclinação dela é o inverso, "
        "[p=0.1] *com o sinal trocado:* [p=0.1] menos três. [p=0.2] {c}Quem esquece o sinal [p=0.1] cai na *D* ou na *E.*"),
    dict(id="05", block="resposta", text=
        "{a}Pelo ponto cinco e cinco, [p=0.1] com inclinação menos três: [p=0.2] {b}*ípsilon igual a menos três xis mais "
        "vinte.* [p=0.2] {c}E ela passa bem em cima do S, [p=0.1] onde o herói começa! [p=0.2] {d}Letra *A!*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
