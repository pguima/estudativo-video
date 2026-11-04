# Estudativo · Short 025 — ENEM 2025, questão 144 (a mesma da aula 024): um cubo de aresta 1 começa em x de 5 a 6, y de 1 a
# 2, z de 6 a 7; aproxima 3 do plano yz (x − 3), afasta 5 do plano xz (y + 5), aproxima 4 do plano xy (z − 4) e fica em
# x de 2 a 3, y de 6 a 7, z de 2 a 3. Sombras: yz → y 6–7, z 2–3; xz → x 2–3, z 2–3; xy → x 2–3, y 6–7 → E.
# Vertical 1080x1920, ~1 min, voz Gemini. Dinâmica de Short: pergunta em 3 s → as cinco figuras → "comenta antes de ver" +
# contagem para pausar → armadilha (a distância até o plano yz se mede no x, o eixo que falta no nome) → os três
# movimentos → as sombras no fim, letra E → "você acertou?" + convite para a aula completa (024).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Eixos por extenso (xis, ípsilon, zê); a legenda mostra x, y, z.

TITULO = "Para onde vai o cubo? A questão das projeções do ENEM 2025"

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
        "{a}Questão do ENEM dois mil e vinte e cinco. [p=0.1] Um cubo se *aproxima três* do plano ípsilon zê, [p=0.1] "
        "{b}se *afasta cinco* do plano xis zê [p=0.1] {c}e se *aproxima quatro* do plano xis ípsilon. [p=0.2] {d}Onde "
        "ficam as sombras dele?"),
    dict(id="02", block="opcoes", text=
        "{a}Qual dessas cinco figuras [p=0.1] mostra as projeções do cubo no fim? [p=0.2] {b}Comenta antes de ver! "
        "[p=0.2] {c}Pausa e pensa. [p=0.1] Valendo! [p=3.2]"),
    dict(id="03", block="pegadinha", text=
        "{a}A armadilha é confundir os planos. [p=0.2] {b}A distância até o plano ípsilon zê [p=0.1] não se mede no "
        "ípsilon nem no zê. [p=0.2] {c}Se mede no *xis,* [p=0.1] o eixo que *falta* no nome."),
    dict(id="04", block="movimentos", text=
        "{a}O cubo começa com xis de cinco a seis, [p=0.1] ípsilon de um a dois [p=0.1] e zê de seis a sete. [p=0.2] "
        "{b}Aproximou três do plano ípsilon zê: [p=0.1] o xis *diminui três.* [p=0.2] {c}Afastou cinco do plano xis zê: "
        "[p=0.1] o ípsilon *aumenta cinco.* [p=0.2] {d}Aproximou quatro do plano xis ípsilon: [p=0.1] o zê *diminui "
        "quatro.*"),
    dict(id="05", block="resposta", text=
        "{a}As sombras no fim: [p=0.1] na parede do fundo, [p=0.1] ípsilon de seis a sete [p=0.1] e zê de dois a três. "
        "[p=0.2] {b}Na parede da esquerda, [p=0.1] xis e zê de dois a três. [p=0.2] {c}No chão, [p=0.1] xis de dois a "
        "três [p=0.1] e ípsilon de seis a sete. [p=0.2] {d}Letra *E!*"),
    dict(id="06", block="final", text=
        "{a}Você acertou? [p=0.1] Conta aqui nos comentários. [p=0.2] {b}E a explicação completa, passo a passo, "
        "[p=0.1] está no vídeo da questão aqui no *Estudativo.*"),
]
