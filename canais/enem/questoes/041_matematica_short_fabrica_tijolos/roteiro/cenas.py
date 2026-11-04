# Estudativo · Short 041 — ENEM 2025, questão 152 (a mesma da aula 040): 3 funcionários × 6 h fazem 720 tijolos por
# dia; com 5 funcionários × 9 h, quantos por dia? Horas de trabalho: 18 → 720 ÷ 18 = 40 por hora de trabalho;
# 5 × 9 = 45 → 45 × 40 = 1 800 → D.
# Vertical 1080x1920, ~1 min, voz Gemini. Dinâmica de Short: pergunta em 3 s com a grade funcionários × horas → as
# alternativas, "comenta antes de ver" + contagem para pausar → a conta pela grade → armadilha (1 200 só funcionários,
# 1 080 só horas, 2 520 somou a antiga) → 1 800, letra D → "você acertou?" + convite para a aula completa (040).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Quantos tijolos por dia? A questão de proporção do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Três funcionários, [p=0.1] seis horas por dia cada, "
        "[p=0.1] fazem *setecentos e vinte tijolos.* [p=0.2] {b}Com *cinco funcionários* trabalhando *nove horas,* "
        "[p=0.1] quantos tijolos saem por dia?"),
    dict(id="02", block="opcoes", text=
        "{a}Oitocentos, [p=0.1] mil e oitenta, [p=0.1] mil e duzentos, [p=0.1] mil e oitocentos [p=0.1] ou dois mil "
        "quinhentos e vinte? [p=0.2] {b}Comenta antes de ver! [p=0.3] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="conta", text=
        "{a}O segredo é contar as *horas de trabalho.* [p=0.1] Cada quadradinho é um funcionário trabalhando uma "
        "hora. [p=0.2] {b}Antes: [p=0.1] três vezes seis, [p=0.1] *dezoito* horas de trabalho. [p=0.2] {c}Setecentos "
        "e vinte dividido por dezoito: [p=0.1] *quarenta tijolos* por hora de trabalho. [p=0.2] {d}Agora: [p=0.1] "
        "cinco vezes nove, [p=0.1] *quarenta e cinco* horas de trabalho. [p=0.2] {e}Quarenta e cinco vezes quarenta: "
        "[p=0.1] *mil e oitocentos!*"),
    dict(id="04", block="pegadinha", text=
        "{a}E aqui está a armadilha: [p=0.1] mil e duzentos só aumenta os *funcionários!* [p=0.2] {b}Mil e oitenta "
        "só aumenta as *horas.* [p=0.2] {c}E dois mil quinhentos e vinte *soma* a produção antiga. [p=0.2] {d}Tem "
        "que aumentar as *duas coisas* juntas."),
    dict(id="05", block="resposta", text=
        "{a}São *mil e oitocentos* tijolos por dia. [p=0.2] {b}Letra *D!*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
