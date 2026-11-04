# Estudativo · Questão 014 — ENEM 2025, 2º dia, caderno amarelo, questão 139: o novo padrão de velocidade de internet
# será a MEDIANA das velocidades de referência de dez cidades (390, 380, 320, 390, 340, 380, 390, 400, 350, 360 MB/s).
# → 380 (alternativa C). Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA: mediana = o valor do meio da lista ORDENADA (ímpar: 3, 5, 8 → 5; par: 2, 4, 6, 10 → média dos
# dois do meio = 5) → passo 1: ordenar → passo 2: dez valores, dois do meio (5º e 6º: 380 e 380) → passo 3: média dos
# dois = 380 (C) → pegadinha: sem ordenar, o 5º e o 6º da tabela (340 e 380) dão 360 (A) → as outras alternativas são
# outras medidas: média 370 (B), moda 390 (D), maior valor 400 (E) → ímpar (11 cidades) + desafio (C3 = 420 → 385) →
# resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: qual é a mediana das velocidades de internet? (média, moda e mediana)"

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
        "{a}Questão cento e trinta e nove do ENEM dois mil e vinte e cinco. [p=0.2] Uma empresa de internet vai "
        "escolher uma velocidade padrão [p=0.1] para os clientes de *dez cidades.* [p=0.3] {b}A regra: [p=0.1] o novo "
        "padrão vai ser a *mediana* das velocidades dessas cidades. [p=0.3] {c}Os valores estão no quadro, [p=0.1] em "
        "megabytes por segundo. [p=0.3] {d}Qual velocidade a empresa vai adotar? [p=0.3] Nessa aula, você vai resolver "
        "passo a passo, [p=0.1] e ainda descobrir por que *quase todas* as alternativas erradas [p=0.1] são uma "
        "pegadinha diferente."),
    dict(id="02", block="ferramenta", text=
        "{a}Primeiro, a ferramenta: [p=0.1] a *mediana.* [p=0.2] É o valor que fica *no meio* da lista, [p=0.1] "
        "*depois de colocar os números em ordem.* [p=0.3] {b}Um exemplo: [p=0.1] três, oito e cinco. [p=0.2] Em ordem: "
        "[p=0.1] três, cinco, oito. [p=0.2] O do meio é o *cinco.* [p=0.3] {c}E quando a lista tem uma quantidade "
        "*par* de números? [p=0.2] Aí existem *dois* no meio. [p=0.2] Em dois, quatro, seis e dez, [p=0.1] os do meio "
        "são quatro e seis. [p=0.3] {d}A mediana é a *média* desses dois: [p=0.1] quatro mais seis, [p=0.1] dividido "
        "por dois, [p=0.1] *cinco.*"),
    dict(id="03", block="ordenar", text=
        "{a}Passo um: [p=0.1] colocar as dez velocidades *em ordem,* [p=0.1] da menor para a maior. [p=0.3] "
        "{b}Trezentos e vinte, [p=0.1] trezentos e quarenta, [p=0.1] trezentos e cinquenta, [p=0.1] trezentos e "
        "sessenta, [p=0.1] trezentos e oitenta, [p=0.1] trezentos e oitenta, [p=0.1] trezentos e noventa, [p=0.1] "
        "trezentos e noventa, [p=0.1] trezentos e noventa [p=0.1] e quatrocentos. [p=0.3] {c}Repare: [p=0.1] valor "
        "repetido entra na lista *todas as vezes* que aparece."),
    dict(id="04", block="meio", text=
        "{a}Passo dois: [p=0.1] achar o meio. [p=0.2] São *dez* valores: [p=0.1] uma quantidade par. [p=0.3] {b}Então "
        "o meio fica entre o *quinto* e o *sexto* valor: [p=0.1] cinco ficam antes, [p=0.1] cinco ficam depois. [p=0.3] "
        "{c}O quinto é trezentos e oitenta, [p=0.1] e o sexto também é *trezentos e oitenta.*"),
    dict(id="05", block="mediana", text=
        "{a}Passo três: [p=0.1] a média dos dois do meio. [p=0.3] {b}Trezentos e oitenta mais trezentos e oitenta, "
        "[p=0.1] dividido por dois: [p=0.1] *trezentos e oitenta.* [p=0.3] {c}A velocidade padrão vai ser *trezentos e "
        "oitenta* megabytes por segundo. [p=0.2] Alternativa *C.*"),
    dict(id="06", block="pegadinha", text=
        "{a}Agora, a pegadinha mais comum. [p=0.2] Quem *esquece de ordenar* [p=0.1] pega o quinto e o sexto valor do "
        "jeito que estão no quadro. [p=0.3] {b}Na tabela, [p=0.1] a quinta cidade tem trezentos e quarenta, [p=0.1] e a "
        "sexta, trezentos e oitenta. [p=0.2] A média dá *trezentos e sessenta.* [p=0.2] Alternativa A. [p=0.3] "
        "{c}*Errado:* [p=0.1] sem ordenar, [p=0.1] o meio da tabela não é o meio dos valores."),
    dict(id="07", block="medidas", text=
        "{a}E as outras alternativas? [p=0.2] Cada uma é *outra medida.* [p=0.3] {b}Somando as dez velocidades, [p=0.1] "
        "dá três mil e setecentos. [p=0.2] Dividido por dez: [p=0.1] trezentos e setenta. [p=0.2] Essa é a *média,* "
        "[p=0.1] alternativa B. [p=0.3] {c}O valor que *mais se repete* [p=0.1] é trezentos e noventa, [p=0.1] que "
        "aparece três vezes. [p=0.2] Essa é a *moda,* [p=0.1] alternativa D. [p=0.3] {d}E quatrocentos é só o *maior* "
        "valor, [p=0.1] alternativa E. [p=0.3] {e}A questão pediu a *mediana.* [p=0.2] Por isso, [p=0.1] *trezentos e "
        "oitenta.*"),
    dict(id="08", block="generaliza", text=
        "{a}E se fossem *onze* cidades? [p=0.2] Imagine uma nova cidade com quatrocentos e dez. [p=0.3] {b}Com onze "
        "valores, [p=0.1] a quantidade é ímpar, [p=0.1] e o meio é *um valor só:* [p=0.1] o *sexto,* [p=0.1] com cinco "
        "antes e cinco depois. [p=0.2] A mediana continuaria trezentos e oitenta. [p=0.3] {c}Agora é com você: "
        "[p=0.1] e se a cidade três tivesse *quatrocentos e vinte* [p=0.1] em vez de trezentos e vinte? [p=0.2] Qual "
        "seria a mediana? [p=0.2] Deixe sua resposta nos comentários."),
    dict(id="09", block="resumo", text=
        "{a}Vamos recapitular o caminho. [p=0.2] {b}Primeiro, colocamos as dez velocidades em ordem. [p=0.2] {c}Dez "
        "valores é par: [p=0.1] o meio fica no quinto e no sexto, [p=0.1] trezentos e oitenta e trezentos e oitenta. "
        "[p=0.2] {d}A média dos dois dá trezentos e oitenta. [p=0.2] {e}E cuidado para não confundir com a média, "
        "[p=0.1] a moda [p=0.1] ou o maior valor."),
    dict(id="10", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*média aritmética,* [p=0.2] {c}*moda e mediana* [p=0.2] {d}e *leitura de tabelas.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
