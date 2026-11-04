# Estudativo · Short 037 — ENEM 2025, questão 150 (a mesma da aula 036): a tela do controle remoto de um carrinho mostra
# cinco deslocamentos, cada um numa escala: I 9 cm a 1:100 · II 5 cm a 1:300 · III 5 cm a 1:600 · IV 3 cm a 1:700 ·
# V 2 cm a 1:1000. Real = desenho × escala: 9 m · 15 m · 30 m · 21 m · 20 m → III → C.
# Vertical 1080x1920, ~1 min, voz Gemini. Dinâmica de Short: pergunta em 3 s → as cinco telas → "comenta antes de ver" +
# contagem para pausar → a conta tela por tela → armadilha (maior desenho = 9 m; maior escala = 20 m) → 30 m, letra C →
# "você acertou?" + convite para a aula completa (036).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Qual carrinho andou mais? A questão das escalas do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] A tela do controle remoto de um carrinho [p=0.1] mostra "
        "*cinco deslocamentos,* [p=0.1] {b}cada um numa *escala diferente.* [p=0.2] {c}Qual foi o mais comprido *de "
        "verdade?*"),
    dict(id="02", block="opcoes", text=
        "{a}O maior desenho é o da tela um, [p=0.1] e a maior escala, [p=0.1] a da tela cinco. [p=0.2] Qual você "
        "escolhe? [p=0.2] {b}Comenta antes de ver! [p=0.3] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="conta", text=
        "{a}A escala diz quanto vale cada centímetro. [p=0.1] Um para cem: [p=0.1] um centímetro vale *cem* "
        "centímetros. [p=0.2] {b}Então é só *multiplicar.* [p=0.1] Tela um: [p=0.1] nove vezes cem, [p=0.1] nove "
        "metros. [p=0.2] Tela dois: [p=0.1] cinco vezes trezentos, [p=0.1] quinze metros. [p=0.2] {c}Tela três: "
        "[p=0.1] cinco vezes seiscentos, [p=0.1] *trinta metros!* [p=0.2] {d}Tela quatro: [p=0.1] três vezes "
        "setecentos, [p=0.1] vinte e um metros. [p=0.2] Tela cinco: [p=0.1] dois vezes mil, [p=0.1] vinte metros."),
    dict(id="04", block="pegadinha", text=
        "{a}E aqui está a armadilha: [p=0.1] o *maior desenho* [p=0.1] deu só nove metros! [p=0.2] {b}E a *maior "
        "escala* [p=0.1] deu vinte. [p=0.2] {c}O que conta é o desenho *vezes* a escala."),
    dict(id="05", block="resposta", text=
        "{a}O mais comprido foi o da tela três: [p=0.1] *trinta metros,* [p=0.1] com um desenho de só cinco "
        "centímetros. [p=0.2] {b}Letra *C!*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
