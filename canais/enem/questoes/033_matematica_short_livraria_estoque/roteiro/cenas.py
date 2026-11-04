# Estudativo · Short 033 — ENEM 2025, questão 148 (a mesma da aula 032): estoque (barras: autor brasileiro e estrangeiro) e
# demanda (linha) de quatro gêneros; o gerente só encomenda o gênero cujo estoque não atende a demanda. Ficção 200 ≥ 160,
# autoajuda 130 < 135, romance 145 ≥ 140, biografia 95 ≥ 80 → autoajuda, letra C (valores lidos no gráfico da prova).
# Vertical 1080x1920, ~1 min, voz Gemini. Dinâmica de Short: pergunta em 3 s → o gráfico → "comenta antes de ver" +
# contagem para pausar → soma as barras de cada gênero → armadilha (romance passa por pouco; ficção tem a maior demanda,
# mas sobra) → autoajuda, letra C → "você acertou?" + convite para a aula completa (032).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Qual livro está faltando? A questão do gráfico da livraria no ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Uma livraria tem quatro gêneros de livro. [p=0.2] {b}As "
        "barras mostram o *estoque,* [p=0.1] e a linha azul, [p=0.1] a *demanda* dos clientes. [p=0.2] {c}Em qual gênero "
        "[p=0.1] o estoque *não dá conta?*"),
    dict(id="02", block="opcoes", text=
        "{a}Ficção, [p=0.1] autoajuda, [p=0.1] romance [p=0.1] ou biografia? [p=0.2] {b}Comenta antes de ver! [p=0.2] "
        "{c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="conta", text=
        "{a}O segredo é *somar as duas barras* de cada gênero. [p=0.2] {b}Ficção: [p=0.1] oitenta mais cento e vinte, "
        "[p=0.1] duzentos. [p=0.1] A demanda é cento e sessenta. [p=0.1] Sobra! [p=0.2] {c}Autoajuda: [p=0.1] cinquenta "
        "mais oitenta, [p=0.1] *cento e trinta.* [p=0.1] Mas o ponto azul está *acima* disso, [p=0.1] perto de cento e "
        "trinta e cinco."),
    dict(id="04", block="pegadinha", text=
        "{a}E cuidado com a armadilha: [p=0.1] a *maior demanda* é a de ficção, [p=0.1] mas lá sobra livro! [p=0.2] "
        "{b}Romance: [p=0.1] quarenta mais cento e cinco, [p=0.1] cento e quarenta e cinco, [p=0.1] para uma demanda de "
        "cento e quarenta. [p=0.1] Passa por pouco. [p=0.2] {c}Biografia: [p=0.1] noventa e cinco, [p=0.1] para oitenta. "
        "[p=0.1] Também passa."),
    dict(id="05", block="resposta", text=
        "{a}Só um gênero tem estoque *menor* que a demanda: [p=0.2] {b}a *autoajuda.* [p=0.2] {c}Letra *C!*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
