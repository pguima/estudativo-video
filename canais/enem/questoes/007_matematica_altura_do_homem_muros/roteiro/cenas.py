# Estudativo · Questão 007 — dois muros (3 e 5), cordas do topo de cada um até o pé do outro, cruzando na cabeça do homem:
# qual a altura do homem? Enunciado: enunciado/questao.jpg (sem unidade e sem a distância entre os muros).
# Aula horizontal 1920x1080 (~5 min), explicada passo a passo.
# Caminho: falta a distância? → SEMELHANÇA DE TRIÂNGULOS (o que é, caso ângulo-ângulo, exemplo numérico) → nomes (h, x, y, d) →
# par 1 (corda que sai do muro 5): h/5 = x/d → par 2 (muro 3): h/3 = y/d → somar: x + y = d, o d some →
# SOMA DE FRAÇÕES (mmc 15) → h = 15/8 = 1,875 → por que a distância não importa (muros se afastando) →
# conferência com d = 8 → fórmula geral h = ab/(a + b) (muros iguais = metade) → desafio 10 e 15 → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. "agá" = h (a legenda mostra h).

TITULO = "Qual a altura do homem? Dois muros, duas cordas e semelhança de triângulos (a distância nem importa!)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão para um aluno: voz masculina "
            "adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, sem "
            "introdução. Nas contas, fale devagar e com clareza, número por número. A palavra 'agá' é o nome da letra h. "
            "Faça as perguntas com curiosidade genuína, mostre surpresa no truque e comemore o resultado. Respeite as "
            "pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem "
            "repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Dois muros: [p=0.1] um de altura *três,* [p=0.1] outro de altura *cinco.* [p=0.3] {b}Do topo de cada muro, "
        "uma corda esticada vai até o pé do outro muro, [p=0.2] e as duas cordas se cruzam *exatamente na cabeça do "
        "homem.* [p=0.3] {c}Qual é a altura do homem? [p=0.4] {d}Parece que falta uma informação: [p=0.1] a *distância* "
        "entre os muros. [p=0.2] Mas não falta. [p=0.3] {e}Nessa aula, você vai resolver isso passo a passo, [p=0.1] "
        "usando *semelhança de triângulos* [p=0.1] e *soma de frações.*"),
    dict(id="02", block="semelhanca", text=
        "{a}Primeiro, a ferramenta. [p=0.2] Dois triângulos são *semelhantes* quando têm *os mesmos ângulos.* [p=0.3] "
        "{b}Um é como uma foto ampliada do outro: [p=0.1] muda o tamanho, [p=0.1] mas não muda a forma. [p=0.3] "
        "{c}E aí vem a consequência que interessa: [p=0.1] os lados correspondentes são *proporcionais.* [p=0.3] "
        "{d}Por exemplo: [p=0.1] um triângulo de altura três e base quatro, [p=0.1] e outro de altura seis e base oito. "
        "[p=0.2] Seis dividido por três dá dois, [p=0.1] oito dividido por quatro também dá dois. [p=0.2] Tudo dobrou "
        "na mesma razão. [p=0.3] {e}E para saber se dois triângulos são semelhantes, [p=0.1] basta ter *dois ângulos "
        "iguais.* [p=0.2] O terceiro vem de graça, [p=0.1] porque a soma dos ângulos é sempre cento e oitenta graus."),
    dict(id="03", block="nomes", text=
        "{a}Agora, os nomes. [p=0.2] A altura do homem, que queremos descobrir, [p=0.1] vamos chamar de *agá.* [p=0.3] "
        "{b}A distância do muro de três até o homem [p=0.1] vamos chamar de *x,* [p=0.2] e a distância do homem até o "
        "muro de cinco, [p=0.1] de *y.* [p=0.3] {c}Juntas, elas formam a distância total entre os muros, [p=0.1] que "
        "vamos chamar de *d.* [p=0.2] Então *x mais y é igual a d.* [p=0.3] {d}Guarde essa igualdade, [p=0.1] porque "
        "ela vai fazer a mágica no final."),
    dict(id="04", block="par1", text=
        "{a}Olhe para a corda que sai do topo do muro de cinco [p=0.1] e desce até o pé do muro de três. [p=0.3] "
        "{b}Ela forma um *triângulo grande:* [p=0.1] altura cinco, [p=0.1] base d. [p=0.3] {c}E forma também um "
        "*triângulo pequeno:* [p=0.1] a altura é o homem, agá, [p=0.1] e a base é x. [p=0.3] {d}Os dois têm um ângulo "
        "reto, [p=0.1] porque o muro e o homem estão de pé, [p=0.2] e os dois têm o *mesmo ângulo* lá no pé do muro de "
        "três. [p=0.2] Dois ângulos iguais: [p=0.1] são *semelhantes.* [p=0.3] {e}Então os lados são proporcionais: "
        "[p=0.1] *agá sobre cinco [p=0.1] é igual a x sobre d.*"),
    dict(id="05", block="par2", text=
        "{a}Agora, a outra corda, [p=0.1] que sai do topo do muro de três [p=0.1] e desce até o pé do muro de cinco. "
        "[p=0.3] {b}Mesmo raciocínio: [p=0.1] triângulo grande com altura três e base d, [p=0.2] triângulo pequeno com "
        "altura agá e base y. [p=0.3] {c}Ângulo reto nos dois, [p=0.1] e o mesmo ângulo no pé do muro de cinco. "
        "[p=0.2] Semelhantes de novo! [p=0.3] {d}Então: [p=0.1] *agá sobre três [p=0.1] é igual a y sobre d.*"),
    dict(id="06", block="somar", text=
        "{a}Temos duas equações, [p=0.1] e as duas têm o d, [p=0.1] que a gente não conhece. [p=0.3] {b}O truque é "
        "*somar as duas.* [p=0.2] Do lado esquerdo: [p=0.1] agá sobre cinco, mais agá sobre três. [p=0.2] Do lado "
        "direito: [p=0.1] x sobre d, mais y sobre d. [p=0.3] {c}Como as frações da direita têm o mesmo denominador, "
        "[p=0.1] é só somar os de cima: [p=0.1] x mais y, sobre d. [p=0.3] {d}Mas x mais y é igual a d! [p=0.2] Então "
        "fica d sobre d, [p=0.1] que é igual a *um.* [p=0.3] {e}O d *sumiu* da conta. [p=0.2] Sobrou: [p=0.1] *agá sobre "
        "cinco, mais agá sobre três, é igual a um.*"),
    dict(id="07", block="fracoes", text=
        "{a}Agora é soma de frações. [p=0.2] Agá sobre cinco mais agá sobre três [p=0.1] é o mesmo que agá vezes um "
        "quinto mais um terço. [p=0.3] {b}Para somar frações com denominadores diferentes, [p=0.1] a gente procura um "
        "denominador comum: [p=0.1] o *mínimo múltiplo comum* de cinco e três, [p=0.1] que é *quinze.* [p=0.3] {c}Um "
        "quinto vira três quinze avos, [p=0.2] e um terço vira cinco quinze avos. [p=0.3] {d}Somando, [p=0.1] três "
        "mais cinco, [p=0.1] dá *oito quinze avos.*"),
    dict(id="08", block="resolve", text=
        "{a}Então a equação ficou assim: [p=0.1] agá vezes oito quinze avos [p=0.1] é igual a um. [p=0.2] Que é o "
        "mesmo que *oito agá, sobre quinze,* [p=0.1] igual a um. [p=0.3] {b}Queremos o agá *sozinho.* [p=0.2] "
        "Primeiro, vamos tirar o quinze de baixo: [p=0.1] multiplicamos *os dois lados por quinze.* [p=0.2] Do lado "
        "esquerdo, o quinze de cima cancela o quinze de baixo; [p=0.1] do lado direito, um vezes quinze dá quinze. "
        "[p=0.2] Fica: [p=0.1] *oito agá igual a quinze.* [p=0.3] {c}Agora, o oito está multiplicando o agá. [p=0.2] "
        "Para desfazer, [p=0.1] *dividimos os dois lados por oito.* [p=0.2] Fica: [p=0.1] *agá igual a quinze sobre "
        "oito.* [p=0.3] {d}Repare no que aconteceu: [p=0.1] o oito quinze avos foi para o outro lado *de cabeça para "
        "baixo,* [p=0.1] e virou quinze oitavos. [p=0.2] Esse é o atalho: [p=0.1] multiplicar os dois lados pelo "
        "*inverso.* [p=0.2] Funciona porque oito quinze avos vezes quinze oitavos [p=0.1] dá cento e vinte sobre "
        "cento e vinte, [p=0.1] que é *um.* [p=0.3] {e}E chegamos lá: [p=0.1] *agá é igual a quinze oitavos,* [p=0.2] "
        "que dá *um vírgula oitocentos e setenta e cinco.* [p=0.3] {f}A figura não mostra a unidade, [p=0.1] mas, se "
        "os muros estiverem em metros, [p=0.1] o homem tem um metro e oitenta e sete e meio. [p=0.2] Um homem bem "
        "alto!"),
    dict(id="09", block="distancia", text=
        "{a}E a distância entre os muros? [p=0.2] Ela *não importa.* [p=0.3] {b}Repare: [p=0.1] se os muros se "
        "afastam, [p=0.1] o cruzamento das cordas também se move, [p=0.2] mas a altura do cruzamento *continua a "
        "mesma.* [p=0.3] {c}Se os muros se aproximam, [p=0.1] a mesma coisa. [p=0.3] {d}Foi exatamente isso que a conta "
        "mostrou: [p=0.1] o d apareceu nas duas equações, [p=0.1] e *se cancelou* quando somamos."),
    dict(id="10", block="confere", text=
        "{a}Vamos conferir com um caso concreto. [p=0.2] Imagine os muros a oito de distância. [p=0.3] {b}Pela primeira "
        "equação, [p=0.1] x é igual a d vezes agá sobre cinco, [p=0.1] ou seja, *três.* [p=0.2] E y é o resto: [p=0.1] "
        "oito menos três, [p=0.1] *cinco.* [p=0.3] {c}Agora, testando a segunda equação: [p=0.1] agá sobre três deveria "
        "ser igual a y sobre d, [p=0.1] cinco oitavos. [p=0.2] E quinze oitavos dividido por três [p=0.1] dá *cinco "
        "oitavos.* [p=0.2] Confere!"),
    dict(id="11", block="generaliza", text=
        "{a}E dá para ir além. [p=0.2] Se os muros tiverem alturas *a* e *b,* [p=0.1] a mesma conta leva a uma fórmula: "
        "[p=0.2] *agá é igual a a vezes b, sobre a mais b.* [p=0.2] O produto sobre a soma. [p=0.3] {b}No nosso caso: "
        "[p=0.1] três vezes cinco é quinze, [p=0.1] três mais cinco é oito, [p=0.1] quinze oitavos. [p=0.3] {c}E se os "
        "dois muros forem iguais, [p=0.1] de altura quatro? [p=0.2] Quatro vezes quatro é dezesseis, [p=0.1] sobre "
        "oito, [p=0.1] dá *dois:* [p=0.1] exatamente a *metade* da altura do muro. [p=0.3] {d}Agora é com você: [p=0.1] "
        "se os muros tiverem *dez* e *quinze,* [p=0.1] qual é a altura do cruzamento? [p=0.2] Deixe sua resposta nos "
        "comentários."),
    dict(id="12", block="resumo", text=
        "{a}Vamos recapitular o caminho. [p=0.2] {b}Primeiro, demos nomes: [p=0.1] agá, x, y e d. [p=0.2] {c}Depois, "
        "usamos a semelhança de triângulos [p=0.1] nas duas cordas. [p=0.2] {d}Em seguida, somamos as duas equações, "
        "[p=0.1] e o d sumiu. [p=0.2] {e}E, por último, resolvemos a soma de frações [p=0.1] e encontramos quinze "
        "oitavos."),
    dict(id="13", block="aulas", text=
        "{a}Cada uma dessas ferramentas [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*semelhança de triângulos,* [p=0.2] {c}*razão e proporção* [p=0.2] {d}e *frações.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima aula."),
]
