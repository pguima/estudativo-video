# Estudativo · Questão 038 — ENEM 2025, 2º dia, caderno amarelo, questão 151: a cúpula pentagonal giralongada (um
# poliedro de Johnson: faces regulares, mas não é de Platão, de Arquimedes, prisma nem antiprisma). A questão mostra o
# sólido em duas posições e uma planificação, e pergunta quantos vértices ele tem.
# Faces (pela planificação): 1 decágono, 1 pentágono, 5 quadrados e 25 triângulos = 32 faces.
# Lados: 10 + 5 + 5×4 + 25×3 = 110; cada aresta junta 2 faces → 110 ÷ 2 = 55 arestas.
# Euler: V − A + F = 2 → V − 55 + 32 = 2 → V = 25 → B. Conferência no 3D: 5 em cima + 10 no meio + 10 embaixo = 25.
# Pegadinhas: E (110 = soma dos lados de todas as faces), C (55 = arestas). A (21) e D (80) não saem de conta certa.
# Geometria do sólido em roteiro/poliedro.py (aresta 1, conferida: 25 vértices, 55 arestas, 32 faces).
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: vértice, aresta e face (cubo) → 2: relação de Euler (cubo) → passo 1: as faces → passo 2: as
# arestas → passo 3: Euler → conferência contando no 3D → B → pegadinhas → desafio → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: quantos vértices tem esse poliedro? (relação de Euler)"

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
        "{a}Questão cento e cinquenta e um do ENEM dois mil e vinte e cinco. [p=0.2] Esse sólido tem um nome "
        "comprido: [p=0.1] *cúpula pentagonal giralongada.* [p=0.3] {b}Todas as faces dele são polígonos regulares: "
        "[p=0.1] triângulos, [p=0.1] quadrados, [p=0.1] um pentágono [p=0.1] e um decágono. [p=0.3] {c}A questão "
        "mostra o sólido e uma *planificação* dele. [p=0.2] {d}E pergunta: [p=0.1] quantos *vértices* ele tem? "
        "[p=0.3] {e}Nessa aula, [p=0.1] você vai usar a *contagem de faces e arestas* [p=0.1] e a *relação de "
        "Euler.*"),
    dict(id="02", block="pecas", text=
        "{a}Ferramenta um: [p=0.1] as peças de um poliedro. [p=0.3] {b}As *faces* são os polígonos. [p=0.2] {c}As "
        "*arestas* são as linhas onde duas faces se encontram. [p=0.2] {d}E os *vértices* são os cantos, [p=0.1] as "
        "pontas. [p=0.3] {e}Num cubo: [p=0.1] seis faces, [p=0.1] doze arestas [p=0.1] e oito vértices."),
    dict(id="03", block="euler", text=
        "{a}Ferramenta dois: [p=0.1] a relação de Euler. [p=0.3] {b}Em poliedros como esse, [p=0.1] vale sempre: "
        "[p=0.1] *vértices, [p=0.1] menos arestas, [p=0.1] mais faces, [p=0.1] dá dois.* [p=0.3] {c}No cubo: [p=0.1] "
        "oito, [p=0.1] menos doze, [p=0.1] mais seis: [p=0.1] *dois.* [p=0.3] {d}Então, se você souber as faces e as "
        "arestas, [p=0.1] descobre os vértices."),
    dict(id="04", block="faces", text=
        "{a}Passo um: [p=0.1] contar as faces, [p=0.1] olhando a planificação. [p=0.3] {b}No centro, [p=0.1] *um "
        "decágono.* [p=0.2] {c}Na ponta, [p=0.1] *um pentágono.* [p=0.2] {d}*Cinco quadrados.* [p=0.2] {e}E "
        "*vinte e cinco triângulos.* [p=0.3] {f}Somando: [p=0.1] um, [p=0.1] mais um, [p=0.1] mais cinco, [p=0.1] "
        "mais vinte e cinco: [p=0.1] *trinta e duas faces.*"),
    dict(id="05", block="arestas", text=
        "{a}Passo dois: [p=0.1] as arestas. [p=0.3] {b}Primeiro, some os lados de todas as faces. [p=0.2] {c}Vinte e "
        "cinco triângulos, [p=0.1] vezes três: [p=0.1] setenta e cinco. [p=0.2] Cinco quadrados, [p=0.1] vezes "
        "quatro: [p=0.1] vinte. [p=0.2] Mais cinco do pentágono [p=0.1] e dez do decágono. [p=0.3] {d}Total: [p=0.1] "
        "*cento e dez lados.* [p=0.3] {e}Mas, quando o sólido é montado, [p=0.1] *cada aresta junta dois lados.* "
        "[p=0.2] {f}Então, [p=0.1] cento e dez dividido por dois: [p=0.1] *cinquenta e cinco arestas.*"),
    dict(id="06", block="conta", text=
        "{a}Passo três: [p=0.1] a relação de Euler. [p=0.3] {b}Vértices, [p=0.1] menos cinquenta e cinco, [p=0.1] "
        "mais trinta e dois, [p=0.1] igual a dois. [p=0.3] {c}Menos cinquenta e cinco mais trinta e dois [p=0.1] dá "
        "menos vinte e três. [p=0.3] {d}Então, [p=0.1] vértices é igual a dois mais vinte e três: [p=0.1] *vinte e "
        "cinco!*"),
    dict(id="07", block="confere", text=
        "{a}Vamos conferir contando direto no sólido. [p=0.3] {b}Em cima, [p=0.1] o pentágono tem *cinco* vértices. "
        "[p=0.3] {c}No meio, [p=0.1] a cúpula encosta num anel de *dez.* [p=0.3] {d}E embaixo, [p=0.1] o decágono "
        "tem mais *dez.* [p=0.3] {e}Cinco, [p=0.1] mais dez, [p=0.1] mais dez: [p=0.1] *vinte e cinco.* [p=0.2] "
        "Bateu!"),
    dict(id="08", block="resposta", text=
        "{a}A cúpula pentagonal giralongada tem *vinte e cinco vértices.* [p=0.3] {b}Alternativa *B.*"),
    dict(id="09", block="pegadinhas", text=
        "{a}E as outras? [p=0.3] {b}A *E,* [p=0.1] cento e dez, [p=0.1] é a soma dos lados de todas as faces: "
        "[p=0.1] cada canto do sólido foi contado várias vezes. [p=0.3] {c}A *C,* [p=0.1] cinquenta e cinco, [p=0.1] "
        "é o número de *arestas,* [p=0.1] não de vértices. [p=0.3] {d}E a *A* [p=0.1] e a *D* [p=0.1] não saem de "
        "nenhuma contagem certa."),
    dict(id="10", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}Um poliedro tem *vinte faces* [p=0.1] e *trinta arestas.* [p=0.3] {c}Quantos "
        "vértices ele tem? [p=0.3] {d}Deixe sua resposta nos comentários."),
    dict(id="11", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}Conte as faces de cada tipo. [p=0.2] {c}Some os lados e divida por dois "
        "[p=0.1] para achar as arestas. [p=0.2] {d}E use *vértices menos arestas mais faces igual a dois.*"),
    dict(id="12", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*poliedros,* [p=0.2] {c}*relação de Euler* [p=0.2] {d}e *planificação de sólidos.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
