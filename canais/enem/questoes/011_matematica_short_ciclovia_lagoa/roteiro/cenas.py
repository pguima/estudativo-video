# Estudativo · Short 011 — ENEM 2025, questão 136 (a mesma da aula 010): lagoa circular de raio 1 km com ciclovia;
# um policial protege até 200 m; π ≈ 3. Mínimo de policiais? → 15 (C). Vertical 1080x1920, ~1 min, voz Gemini.
# Dinâmica de Short: pergunta em 3 s → opções → "comenta antes de ver" + contagem para pausar → a volta (6.000 m) →
# pegadinha (6.000 ÷ 200 = 30, D) → 200 para cada lado = 400 m → 6.000 ÷ 400 = 15 → resposta C (com 14 sobram 400 m)
# → "você acertou?" + convite para a aula completa (010).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Quantos policiais protegem a ciclovia? A pegadinha do ENEM 2025"

VOZ = dict(
    tags=["animada", "curiosa", "confiante"],
    prompt=("Narre um Short de desafio de matemática: voz masculina adulta, enérgica, clara e empolgada, como um "
            "professor de cursinho desafiando os alunos. Ritmo rápido desde a primeira palavra, sem introdução lenta. "
            "Bata forte nos números e nas palavras-chave. 'Pi' é a letra grega (leia 'pí'). Tom de suspense antes da "
            "resposta e de surpresa na revelação. Respeite as pausas marcadas. Leia apenas o texto, exatamente como está "
            "escrito, sem acrescentar, pular ou repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.8)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Uma lagoa com um raio de *um quilômetro* [p=0.1] e uma "
        "ciclovia em volta. [p=0.2] {b}Um policial protege quem está a até *duzentos metros* dele. [p=0.2] {c}Quantos "
        "policiais, no mínimo, [p=0.1] para proteger a ciclovia inteira?"),
    dict(id="02", block="opcoes", text=
        "{a}As opções: [p=0.1] quatro, [p=0.1] oito, [p=0.1] quinze, [p=0.1] trinta [p=0.1] ou sessenta. [p=0.2] "
        "{b}Comenta antes de ver! [p=0.2] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="volta", text=
        "{a}Primeiro, a volta da ciclovia: [p=0.1] *dois vezes pi vezes r.* [p=0.2] {b}Com pi igual a três [p=0.1] e "
        "raio de mil metros, [p=0.1] dá *seis mil metros.*"),
    dict(id="04", block="pegadinha", text=
        "{a}Se você dividiu seis mil por duzentos, [p=0.1] deu trinta: [p=0.1] letra D. [p=0.2] {b}*Pegadinha!* "
        "[p=0.1] O policial protege duzentos metros *para cada lado.*"),
    dict(id="05", block="cobertura", text=
        "{a}Duzentos à frente, [p=0.1] duzentos atrás: [p=0.1] *quatrocentos metros* por policial. [p=0.2] {b}Seis mil "
        "dividido por quatrocentos: [p=0.1] *quinze.*"),
    dict(id="06", block="resposta", text=
        "{a}*Quinze policiais!* [p=0.1] Com quatorze, [p=0.1] sobrariam quatrocentos metros sem proteção. [p=0.2] "
        "{b}Letra *C.*"),
    dict(id="07", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
