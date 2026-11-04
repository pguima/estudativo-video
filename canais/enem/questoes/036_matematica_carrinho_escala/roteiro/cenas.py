# Estudativo · Questão 036 — ENEM 2025, 2º dia, caderno amarelo, questão 150: a tela do controle remoto de um carrinho
# mostra cada deslocamento numa escala diferente (a tela ajusta a escala sozinha). Cinco telas:
# I 9 cm a 1:100 · II 5 cm a 1:300 · III 5 cm a 1:600 · IV 3 cm a 1:700 · V 2 cm a 1:1000.
# Real = desenho × denominador: 900 cm (9 m) · 1500 (15 m) · 3000 (30 m) · 2100 (21 m) · 2000 (20 m) → maior: III → C.
# Pegadinhas: A (maior desenho, 9 cm, mas só 9 m), E (maior escala, 1:1000, mas 20 m), D (21 m, o segundo maior), B (15 m).
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: o que é escala → 2: o desenho engana (cada tela tem a sua escala) → passo 1: I, II e III →
# passo 2: IV e V → comparar em metros → C → pegadinhas → desafio → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: o carrinho de controle remoto (escala)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nas contas, fale devagar e com clareza, número por número. Faça as perguntas com "
            "curiosidade genuína, mostre surpresa na resposta e comemore o resultado. Respeite as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão cento e cinquenta do ENEM dois mil e vinte e cinco. [p=0.2] O controle remoto de um carrinho de "
        "brinquedo tem uma *tela* [p=0.1] que mostra cada deslocamento do carrinho. [p=0.3] {b}Mas a tela *ajusta a "
        "escala sozinha:* [p=0.1] cada desenho tem uma escala diferente. [p=0.3] {c}São cinco deslocamentos. [p=0.2] "
        "{d}Qual deles foi o *mais comprido* de verdade? [p=0.3] {e}Nessa aula, [p=0.1] você vai usar a *escala* "
        "[p=0.1] e a *conversão de unidades.*"),
    dict(id="02", block="escala", text=
        "{a}Ferramenta um: [p=0.1] o que é escala. [p=0.3] {b}A escala um para cem quer dizer: [p=0.1] *um "
        "centímetro* no desenho [p=0.1] vale *cem centímetros* na realidade. [p=0.3] {c}Então, para achar o tamanho "
        "real, [p=0.1] é só *multiplicar* a medida do desenho [p=0.1] pelo número de baixo da escala. [p=0.3] {d}Por "
        "exemplo: [p=0.1] nove centímetros, na escala um para cem, [p=0.1] são novecentos centímetros. [p=0.2] Nove "
        "metros."),
    dict(id="03", block="engana", text=
        "{a}Ferramenta dois: [p=0.1] o desenho engana. [p=0.3] {b}O maior desenho é o da tela um, [p=0.1] com nove "
        "centímetros. [p=0.2] {c}Mas cada tela usa uma escala diferente. [p=0.2] {d}Então, *comparar os desenhos* "
        "[p=0.1] não diz qual deslocamento foi maior. [p=0.3] {e}Primeiro, [p=0.1] tudo tem que virar *tamanho "
        "real.*"),
    dict(id="04", block="passo1", text=
        "{a}Passo um: [p=0.1] as três primeiras telas. [p=0.3] {b}Tela um: [p=0.1] nove centímetros, [p=0.1] vezes "
        "cem: [p=0.1] *novecentos* centímetros. [p=0.3] {c}Tela dois: [p=0.1] cinco, [p=0.1] vezes trezentos: [p=0.1] "
        "*mil e quinhentos* centímetros. [p=0.3] {d}Tela três: [p=0.1] cinco, [p=0.1] vezes seiscentos: [p=0.1] *três "
        "mil* centímetros."),
    dict(id="05", block="passo2", text=
        "{a}Passo dois: [p=0.1] as outras duas. [p=0.3] {b}Tela quatro: [p=0.1] três, [p=0.1] vezes setecentos: "
        "[p=0.1] *dois mil e cem* centímetros. [p=0.3] {c}Tela cinco: [p=0.1] dois, [p=0.1] vezes mil: [p=0.1] *dois "
        "mil* centímetros."),
    dict(id="06", block="comparar", text=
        "{a}Agora, vamos comparar em *metros.* [p=0.2] {b}Cem centímetros são um metro, [p=0.1] então é só dividir "
        "por cem. [p=0.3] {c}Nove metros, [p=0.1] quinze, [p=0.1] trinta, [p=0.1] vinte e um [p=0.1] e vinte. [p=0.3] "
        "{d}O maior é *trinta metros:* [p=0.1] a tela três!"),
    dict(id="07", block="resposta", text=
        "{a}O deslocamento mais comprido foi o da tela *três:* [p=0.1] trinta metros. [p=0.3] {b}E repare: [p=0.1] o "
        "desenho dele tem só cinco centímetros! [p=0.3] {c}Alternativa *C.*"),
    dict(id="08", block="pegadinhas", text=
        "{a}E as outras? [p=0.3] {b}A *A* [p=0.1] escolhe o *maior desenho:* [p=0.1] nove centímetros, [p=0.1] mas só "
        "nove metros de verdade. [p=0.3] {c}A *E* [p=0.1] escolhe a *maior escala,* [p=0.1] um para mil: [p=0.1] mas "
        "o desenho é pequeno, [p=0.1] e dá vinte metros. [p=0.3] {d}A *D,* [p=0.1] vinte e um metros, [p=0.1] é a "
        "segunda maior. [p=0.2] {e}E a *B* [p=0.1] tem só quinze metros."),
    dict(id="09", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}Uma sexta tela mostra *quatro centímetros* [p=0.1] na escala *um para "
        "oitocentos.* [p=0.3] {c}Esse deslocamento seria maior que o da tela três? [p=0.3] {d}Deixe sua resposta nos "
        "comentários."),
    dict(id="10", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}Leia a escala de cada desenho. [p=0.2] {c}Multiplique a medida do desenho "
        "[p=0.1] pelo número da escala. [p=0.2] {d}E compare tudo na *mesma unidade.*"),
    dict(id="11", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*escalas,* [p=0.2] {c}*unidades e conversões* [p=0.2] {d}e *razão e proporção.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
