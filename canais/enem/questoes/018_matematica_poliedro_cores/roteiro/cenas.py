# Estudativo · Questão 018 — ENEM 2025, 2º dia, caderno amarelo, questão 141: um protótipo impresso em 3D é um poliedro
# convexo formado por um prisma hexagonal regular reto com um tronco de pirâmide hexagonal reta em cima (a base maior do
# tronco coincide com uma base do prisma). Faces congruentes → mesma cor; não congruentes → cores diferentes.
# Superfície: 1 hexágono (base do prisma) + 6 retângulos + 6 trapézios + 1 hexágono menor → 4 cores (alternativa D).
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: congruência (mesma forma E mesmo tamanho; quadrados de lado 2 e 4 não são) → A FERRAMENTA 2: as
# faces do prisma e do tronco → passo 1: a junção (as duas bases coladas ficam dentro, sem tinta) → passo 2: listar as 14
# faces da superfície → passo 3: agrupar as congruentes → 4 cores (D) → pegadinha: os dois hexágonos não são congruentes
# (3 cores, E) → generaliza (pirâmide inteira em cima: 3 cores) + desafio (cubo + tronco de base quadrada) → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: quantas cores para pintar o poliedro? (prisma, tronco de pirâmide e congruência)"

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
        "{a}Questão cento e quarenta e um do ENEM dois mil e vinte e cinco. [p=0.2] Uma fábrica imprimiu, [p=0.1] numa "
        "impressora três dê, [p=0.1] uma peça [p=0.1] formada por *dois sólidos* juntos: [p=0.1] um *prisma hexagonal* [p=0.1] e, em cima dele, "
        "[p=0.1] um *tronco de pirâmide hexagonal.* [p=0.3] {b}Depois, a superfície vai ser pintada com uma regra: "
        "[p=0.1] faces *congruentes* ganham a *mesma cor,* [p=0.1] e faces não congruentes, [p=0.1] cores diferentes. "
        "[p=0.3] {c}Quantas cores vão ser usadas? [p=0.3] Nessa aula, você vai resolver passo a passo, [p=0.1] e ver "
        "o detalhe que derruba muita gente."),
    dict(id="02", block="congruencia", text=
        "{a}Primeiro, a palavra-chave: [p=0.1] *congruente.* [p=0.3] {b}Duas figuras são congruentes [p=0.1] quando "
        "têm a *mesma forma* [p=0.1] e o *mesmo tamanho:* [p=0.1] uma encaixa perfeitamente em cima da outra. [p=0.3] "
        "{c}Dois quadrados de lado dois [p=0.1] são congruentes. [p=0.3] {d}Mas um quadrado de lado dois [p=0.1] e "
        "outro de lado quatro [p=0.1] *não são:* [p=0.1] têm a mesma forma, [p=0.1] mas tamanhos diferentes."),
    dict(id="03", block="solidos", text=
        "{a}Agora, os dois sólidos. [p=0.3] {b}O prisma hexagonal regular reto [p=0.1] tem *duas bases* [p=0.1] que são "
        "hexágonos regulares *iguais,* [p=0.1] e *seis faces laterais* [p=0.1] que são retângulos iguais. [p=0.3] "
        "{c}O tronco de pirâmide hexagonal [p=0.1] é uma pirâmide com a ponta cortada. [p=0.2] Ele tem uma base "
        "*maior* [p=0.1] e uma base *menor,* [p=0.1] as duas hexagonais, [p=0.1] e *seis faces laterais* [p=0.1] que "
        "são trapézios iguais."),
    dict(id="04", block="juncao", text=
        "{a}Passo um: [p=0.1] juntar as peças. [p=0.3] {b}A base maior do tronco [p=0.1] coincide com uma das bases do "
        "prisma: [p=0.1] as duas se encaixam e ficam *coladas.* [p=0.3] {c}Essas duas faces vão para *dentro* da "
        "peça. [p=0.2] Elas não fazem parte da superfície, [p=0.1] então *não recebem tinta.*"),
    dict(id="05", block="faces", text=
        "{a}Passo dois: [p=0.1] listar as faces que ficam *por fora.* [p=0.3] {b}Embaixo, [p=0.1] a outra base do "
        "prisma: [p=0.1] *um hexágono.* [p=0.3] {c}Em volta, [p=0.1] os *seis retângulos* do prisma. [p=0.3] "
        "{d}Subindo, [p=0.1] os *seis trapézios* do tronco. [p=0.3] {e}E lá em cima, [p=0.1] a base menor do tronco: "
        "[p=0.1] *um hexágono menor.* [p=0.2] Ao todo, [p=0.1] catorze faces."),
    dict(id="06", block="cores", text=
        "{a}Passo três: [p=0.1] juntar as faces congruentes. [p=0.3] {b}Os seis retângulos são iguais: [p=0.1] *uma "
        "cor.* [p=0.3] {c}Os seis trapézios também são iguais: [p=0.1] *outra cor.* [p=0.3] {d}Sobram os dois "
        "hexágonos. [p=0.2] O de baixo tem o tamanho da base do prisma, [p=0.1] e o de cima é *menor.* [p=0.2] Não "
        "são congruentes: [p=0.1] *uma cor para cada um.* [p=0.3] {e}Total: [p=0.1] *quatro cores.* [p=0.2] "
        "Alternativa *D.*"),
    dict(id="07", block="pegadinha", text=
        "{a}Agora, o detalhe que derruba muita gente. [p=0.2] {b}Quem pensa: [p=0.1] hexágono é hexágono, [p=0.1] "
        "pinta os dois da mesma cor [p=0.1] e chega a *três cores.* [p=0.2] Alternativa E. [p=0.3] {c}*Errado:* "
        "[p=0.1] os dois têm a mesma forma, [p=0.1] mas não o mesmo tamanho. [p=0.2] São *semelhantes,* [p=0.1] não "
        "*congruentes.* [p=0.3] {d}E repare: [p=0.1] a regra pede cores, [p=0.1] não faces. [p=0.2] São catorze "
        "faces, [p=0.1] mas só quatro tipos diferentes."),
    dict(id="08", block="generaliza", text=
        "{a}E se, em vez do tronco, [p=0.1] fosse uma *pirâmide inteira* em cima do prisma? [p=0.3] {b}Aí não "
        "existiria o hexágono de cima: [p=0.1] as faces laterais da pirâmide seriam *seis triângulos iguais.* [p=0.2] "
        "Hexágono, [p=0.1] retângulos [p=0.1] e triângulos: [p=0.1] *três cores.* [p=0.3] {c}Agora é com você: "
        "[p=0.1] e se o prisma fosse um *cubo,* [p=0.1] com um tronco de pirâmide de base quadrada em cima? [p=0.2] "
        "Quantas cores seriam usadas? [p=0.2] Deixe sua resposta nos comentários."),
    dict(id="09", block="resumo", text=
        "{a}Vamos recapitular o caminho. [p=0.2] {b}Primeiro, juntamos os sólidos: [p=0.1] as bases coladas ficam "
        "dentro e não são pintadas. [p=0.2] {c}Depois, listamos as catorze faces de fora. [p=0.2] {d}Agrupando as "
        "congruentes, [p=0.1] chegamos a quatro cores. [p=0.2] {e}E cuidado: [p=0.1] mesma forma com tamanho "
        "diferente [p=0.1] não é congruente."),
    dict(id="10", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*prismas,* [p=0.2] {c}*pirâmides e troncos* [p=0.2] {d}e *congruência e semelhança.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
