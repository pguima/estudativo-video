# Estudativo · Questão 026 — ENEM 2025, 2º dia, caderno amarelo, questão 145: num infográfico (revista Galileu, 2015),
# 90% dos internautas brasileiros acessam redes sociais e 60% dos que acessam são mulheres. Sorteando um internauta
# brasileiro qualquer, a probabilidade de ser um homem que acessa = 40% de 90% = 0,4 × 0,9 = 0,36 = 36/100 → alternativa B.
# (Com 100 internautas: 90 acessam, 10 não; das 90, 54 mulheres e 36 homens; 54 + 36 + 10 = 100.)
# Pegadinhas: C (40/100) usa 40% de todos, esquecendo os 10% que não acessam; A, D e E põem 90 no denominador (sorteiam só
# entre quem acessa) — e mesmo nesse caso seria 36/90, que não está nas opções.
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: probabilidade = casos que servem / todos os casos (exemplo: 10 de 40 alunos de óculos) → A
# FERRAMENTA 2: porcentagem de porcentagem ("de" vira "vezes": 50% de 50% = 25%) → A FERRAMENTA 3: o que sobra (60% → 40%,
# mas de quem acessa) → passo 1: de onde se sorteia (todos: imagine 100) → passo 2: 90 acessam, 10 não → passo 3: 54
# mulheres, 36 homens → 36/100, conferência → B → por que as outras estão erradas → desafio → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: redes sociais e probabilidade (porcentagem de porcentagem)"

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
        "{a}Questão cento e quarenta e cinco do ENEM dois mil e vinte e cinco. [p=0.2] Uma reportagem mostrou que "
        "*noventa por cento* dos internautas brasileiros [p=0.1] acessam redes sociais. [p=0.3] {b}E que, entre os que "
        "acessam, [p=0.1] *sessenta por cento* são mulheres. [p=0.3] {c}Sorteando um internauta qualquer, [p=0.1] qual "
        "é a probabilidade de ele ser um *homem que acessa* alguma rede social? [p=0.3] {d}Nessa aula, [p=0.1] você vai "
        "ver por que a resposta não é quarenta por cento."),
    dict(id="02", block="probabilidade", text=
        "{a}Primeiro, [p=0.1] a ferramenta: [p=0.1] a *probabilidade.* [p=0.3] {b}Ela é uma fração: [p=0.1] os casos "
        "que *servem,* [p=0.1] divididos por *todos* os casos possíveis. [p=0.3] {c}Numa turma de quarenta alunos, "
        "[p=0.1] dez usam óculos. [p=0.2] Sorteando um aluno, [p=0.1] a chance de ele usar óculos é *dez em quarenta.* "
        "[p=0.3] {d}A parte de baixo da fração [p=0.1] é sempre o grupo *de onde se sorteia.*"),
    dict(id="03", block="porcentagem", text=
        "{a}Ferramenta dois: [p=0.1] a *porcentagem de uma porcentagem.* [p=0.3] {b}Metade da metade de uma pizza "
        "[p=0.1] é *um quarto* da pizza. [p=0.3] {c}Em porcentagem: [p=0.1] cinquenta por cento de cinquenta por cento "
        "[p=0.1] é *vinte e cinco por cento.* [p=0.3] {d}A palavra *de* vira *vezes:* [p=0.1] zero vírgula cinco vezes "
        "zero vírgula cinco, [p=0.1] zero vírgula vinte e cinco."),
    dict(id="04", block="sobra", text=
        "{a}Ferramenta três: [p=0.1] o que *sobra.* [p=0.3] {b}No infográfico, [p=0.1] quem acessa redes sociais "
        "[p=0.1] está dividido em mulheres e homens. [p=0.3] {c}Se sessenta por cento são mulheres, [p=0.1] os homens são "
        "*quarenta por cento.* [p=0.3] {d}Mas atenção: [p=0.1] quarenta por cento de quem *acessa,* [p=0.1] e não de todo "
        "mundo."),
    dict(id="05", block="universo", text=
        "{a}Passo um: [p=0.1] de onde se sorteia? [p=0.3] {b}A questão escolhe *um internauta brasileiro qualquer,* "
        "[p=0.1] e não só entre quem acessa. [p=0.3] {c}Então a parte de baixo da fração [p=0.1] são *todos* os "
        "internautas. [p=0.2] Para ficar fácil de ver, [p=0.1] vamos imaginar *cem.*"),
    dict(id="06", block="acessam", text=
        "{a}Passo dois: [p=0.1] quem acessa. [p=0.3] {b}Noventa por cento de cem: [p=0.1] *noventa* internautas acessam "
        "redes sociais. [p=0.3] {c}E *dez* não acessam."),
    dict(id="07", block="homens", text=
        "{a}Passo três: [p=0.1] entre os noventa, [p=0.1] quantos são homens? [p=0.3] {b}Sessenta por cento de noventa "
        "são mulheres: [p=0.1] *cinquenta e quatro.* [p=0.3] {c}Os homens são o resto: [p=0.1] noventa menos cinquenta e "
        "quatro, [p=0.1] *trinta e seis.* [p=0.3] {d}Ou direto: [p=0.1] quarenta por cento de noventa, [p=0.1] trinta e "
        "seis."),
    dict(id="08", block="resposta", text=
        "{a}Então, [p=0.1] de cem internautas, [p=0.1] *trinta e seis* são homens que acessam. [p=0.3] {b}A probabilidade "
        "é *trinta e seis em cem.* [p=0.3] {c}Conferindo: [p=0.1] cinquenta e quatro mulheres, [p=0.1] mais trinta e seis "
        "homens, [p=0.1] mais dez que não acessam, [p=0.1] dá cem. [p=0.3] {d}Alternativa *B.*"),
    dict(id="09", block="pegadinhas", text=
        "{a}E as outras? [p=0.3] {b}Quarenta em cem, [p=0.1] a *C,* [p=0.1] usa quarenta por cento de *todo mundo,* "
        "[p=0.1] e esquece os dez que não acessam. [p=0.3] {c}A, D e E põem *noventa* embaixo: [p=0.1] sorteiam só entre "
        "quem acessa. [p=0.3] {d}Mas a questão sorteia entre *todos* os internautas. [p=0.2] E, mesmo sorteando só entre "
        "quem acessa, [p=0.1] daria trinta e seis em noventa, [p=0.1] que nem está nas opções."),
    dict(id="10", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}Sorteando um internauta brasileiro, [p=0.1] qual é a probabilidade [p=0.1] de "
        "ser uma *mulher que acessa* redes sociais? [p=0.3] {c}Deixe sua resposta nos comentários."),
    dict(id="11", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}Probabilidade é o que serve [p=0.1] dividido por todo o grupo de onde se "
        "sorteia. [p=0.2] {c}Porcentagem de porcentagem [p=0.1] é multiplicação. [p=0.2] {d}E imaginar cem pessoas "
        "[p=0.1] deixa a conta fácil de ver."),
    dict(id="12", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*porcentagem,* [p=0.2] {c}*probabilidade* [p=0.2] {d}e *frações e decimais.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
