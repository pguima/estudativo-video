# Roteiro — Progressão Aritmética, Episódio 3 de 5: a soma de Gauss (somar dezenas de termos em uma linha)
# Base: Estudos/Enem/estudos/01-matematica/31-progressao-aritmetica.html — seção 06, da seção 05 só "termos equidistantes
#   dos extremos têm a mesma soma", estratégia 3 da seção 09 (soma = nº de termos × termo médio) + Questões 3, 8 e 9 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O TRUQUE DE GAUSS: junte o primeiro com o último, o segundo com o penúltimo; todos os pares dão a mesma soma.
#   AS DUAS ESCADAS: duas escadas encaixadas formam um retângulo; por isso se divide por 2.
#   SOMA = QUANTOS TERMOS × A MÉDIA ENTRE O PRIMEIRO E O ÚLTIMO.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Bloco d (teatro: a₂₅ = 68, S = 44 · 25 = 1 100) = mesmos números da Questão 3, que é "eu faço" (repetição pedida no
#   prompt); na Q3 o foco são as alternativas erradas.
# DESVIO do prompt (bloco f): o prompt usa a₃ + a₁₈ = a₁ + a₂₀ numa PA de 20 termos, que é exatamente a montagem da
#   Questão 9 ("você faz", com pausa). O bloco usa uma PA NOSSA de 12 termos, (3, 5, 7, …, 25): a₂ + a₁₁ = 5 + 23 = 28
#   = a₁ + a₁₂ = 3 + 25 (índices somando 13); soma = 28 · 12 ÷ 2 = 168. O "20 termos / índices 21" só aparece na Q9.
# Nós fazemos (prompt): (5, 8, 11, …), 20 termos: a₂₀ = 5 + 19 · 3 = 62; S = (5 + 62) · 20 ÷ 2 = 67 · 10 = 670.
# Erros clássicos com os números do "nós fazemos" (já resolvido): sem ÷ 2 → 1 340; "no 20º" (62) × "ao todo" (670);
#   20 saltos → a₂₀ = 65 e S = 700. Nada da Q8 nem da Q9.
# QUESTÃO 3 ("eu faço"): gabarito A (1 100). Erradas = material (B a₂₅ = 70, um salto a mais: 90 · 25 ÷ 2 = 1 125;
#   C 25 · 20 + (2 + 4 + … + 50) = 500 + 650 = 1 150, como se a primeira fileira também ganhasse 2; D todas com 68:
#   68 · 25 = 1 700; E sem dividir por 2: 88 · 25 = 2 200).
# QUESTÃO 8 ("nós fazemos"): gabarito B (57 km). Erradas = material (A esquece o primeiro termo: 7,5 · 12 ÷ 2 = 45;
#   C a₁₂ = 2 + 12 · 0,5 = 8 → 60; D 7,5 · 12 = 90, como se corresse 7,5 todos os dias; E sem dividir por 2: 114).
# QUESTÃO 9 ("você faz", com pausa): gabarito D (500). Erradas = material (A divide por 2 duas vezes: 250; B 18 termos:
#   450; C 19 termos: 475; E sem dividir por 2: 1 000).
# Acréscimos NOSSOS (marcados): atalho verde "a metade antes" (divida por 2 o número que for par antes de multiplicar,
#   cena 08); atalho verde "termo médio" (cena 12, estratégia 3 da seção 09); atalho verde "índices somando n + 1"
#   (cena 11); atalho verde "termo ou soma?" (cena 18, sublinhe a palavra).
# Frases-chave (meio e fim, idênticas): 1. Primeiro com último: todos os pares dão a mesma soma.
#   2. Soma é número de termos vezes a média dos extremos. 3. "No 12º" é termo; "em 12" ou "ao todo" é soma.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "A soma de Gauss: some qualquer PA em uma linha | PA Ep. 3"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}*Um, mais dois, mais três,* [p=0.2] e assim por diante, [p=0.2] até *cem.* [p=0.5] {b}Um menino de *dez anos* "
        "[p=0.2] deu a resposta em segundos: [p=0.3] *cinco mil e cinquenta.* [p=0.5] {c}Ele não era mais rápido nas "
        "contas; [p=0.3] {d}ele só *juntou os números do jeito certo.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Progressão aritmética.* [p=0.4] {a}Ao final, [p=0.2] você vai "
        "*somar qualquer PA em uma linha* [p=0.3] {b}e distinguir, no enunciado, [p=0.2] quando a pergunta é o *termo* "
        "[p=0.2] e quando é a *soma.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] o *termo geral.* [p=0.2] O termo de posição n "
        "[p=0.2] é o primeiro, [p=0.2] mais *n menos um* saltos de razão. [p=0.4] {b}E a *média* de dois números: "
        "[p=0.2] some e divida por dois. [p=0.2] Vinte e sessenta e oito: [p=0.2] oitenta e oito, [p=0.2] metade, "
        "[p=0.2] *quarenta e quatro.* [p=0.3] Só isso."),

    # ================= BLOCO A: GAUSS =================
    dict(id="04", block="gauss", text=
        "{t}Como alguém soma cem números em segundos? [p=0.4] {a}O menino era *Gauss,* [p=0.2] que virou um dos "
        "maiores matemáticos da história. [p=0.4] {b}Ele não somou na ordem. [p=0.2] Juntou o *primeiro com o último:* "
        "[p=0.2] um mais cem, [p=0.2] *cento e um.* [p=0.4] {c}Depois o segundo com o penúltimo: [p=0.2] dois mais "
        "noventa e nove, [p=0.2] *cento e um* de novo. [p=0.3] Três mais noventa e oito: [p=0.2] *cento e um.*"),
    dict(id="05", block="gauss", text=
        "{t}E quantos pares são? [p=0.4] {a}Cem números, [p=0.2] de dois em dois: [p=0.2] *cinquenta pares.* [p=0.4] "
        "{b}Todos valendo cento e um. [p=0.2] Cinquenta vezes cento e um: [p=0.2] *cinco mil e cinquenta.* [p=0.4] "
        "{c}O primeiro e o último têm nome: [p=0.2] são os *extremos.* [p=0.3] {d}O truque de Gauss: [p=0.2] *todos os "
        "pares dão a mesma soma.*"),

    # ================= BLOCO B: AS DUAS ESCADAS =================
    dict(id="06", block="escadas", text=
        "{t}Mas por que os pares dão sempre igual? [p=0.4] {a}Monte uma escada de bloquinhos: [p=0.2] um, dois, três, "
        "quatro, cinco, *seis.* [p=0.4] {b}Agora uma *segunda escada,* igual, [p=0.2] de cabeça para baixo. [p=0.3] "
        "{c}Encaixe as duas. [p=0.2] Elas formam um *retângulo:* [p=0.2] *seis colunas* [p=0.2] de *sete* "
        "bloquinhos cada. [p=0.4] {d}Duas somas valem seis vezes sete, [p=0.2] *quarenta e dois.* [p=0.2] Uma soma só "
        "[p=0.2] é a *metade:* [p=0.2] vinte e um. [p=0.3] É por isso que se *divide por dois.*"),

    # ================= BLOCO C: A FÓRMULA =================
    dict(id="07", block="formula", text=
        "{t}E isso vira fórmula? [p=0.4] {a}Vira. [p=0.2] A *soma dos n primeiros termos* [p=0.2] é tudo somado, do "
        "primeiro até o de posição n. [p=0.2] Ela se escreve *esse ene.* [p=0.4] {b}*Esse ene* [p=0.2] é igual a "
        "*a um mais a ene,* [p=0.2] vezes *n,* [p=0.2] dividido por *dois.* [p=0.4] {c}Leia assim: [p=0.2] *número "
        "de termos* [p=0.2] vezes a *média dos extremos.* [p=0.3] {d}A média do primeiro com o último, [p=0.2] vezes "
        "quantos termos há."),
    dict(id="08", block="metade", text=
        "{t}E como fazer essa conta sem calculadora? [p=0.4] {a}Atalho: [p=0.2] *divida por dois antes.* [p=0.4] "
        "{b}Procure o número *par:* [p=0.2] a soma dos extremos [p=0.2] ou o número de termos. [p=0.2] Corte ele pela "
        "metade primeiro. [p=0.4] {c}De um a cem: [p=0.2] cento e um vezes cem, [p=0.2] dividido por dois. [p=0.2] "
        "Corte o cem: [p=0.2] *cento e um vezes cinquenta.* [p=0.3] Conta de cabeça."),

    # ================= BLOCO D: O TEATRO =================
    dict(id="09", block="teatro", text=
        "{t}E numa PA que não começa no um? [p=0.4] {a}Um teatro tem *vinte e cinco fileiras.* [p=0.2] A primeira tem "
        "*vinte cadeiras;* [p=0.2] cada uma tem *duas a mais* que a anterior. [p=0.4] {b}A última fileira não foi "
        "dada. [p=0.2] Calcule antes: [p=0.2] vinte, [p=0.2] mais *vinte e quatro* saltos de dois. [p=0.2] *Sessenta e "
        "oito.* [p=0.4] {c}Média dos extremos: [p=0.2] *quarenta e quatro.* [p=0.2] Vezes vinte e cinco fileiras: "
        "[p=0.2] *mil e cem cadeiras.*"),

    # ================= BLOCO E: SOMAS PARA DECORAR =================
    dict(id="10", block="decorar", text=
        "{t}Tem alguma soma que vale a pena decorar? [p=0.4] {a}Duas. [p=0.2] A dos *n primeiros números naturais:* "
        "[p=0.2] um mais dois até n [p=0.2] dá *n vezes n mais um, sobre dois.* [p=0.2] É o Gauss em uma linha. "
        "[p=0.4] {b}E a dos *ímpares:* [p=0.2] os n primeiros ímpares [p=0.2] somam *n ao quadrado.* [p=0.3] {c}Um mais "
        "três: [p=0.2] quatro. [p=0.2] Mais cinco: [p=0.2] nove. [p=0.2] Os dez primeiros ímpares: [p=0.2] *cem.*"),

    # ================= BLOCO F: TERMOS EQUIDISTANTES =================
    dict(id="11", block="equidist", text=
        "{t}E se você não souber o primeiro nem o último? [p=0.4] {a}*Termos equidistantes* dos extremos [p=0.2] "
        "são os que estão à *mesma distância* das pontas: [p=0.2] o segundo e o penúltimo, [p=0.2] o terceiro e o "
        "antepenúltimo. [p=0.4] {b}Na PA *três, cinco, sete,* até *vinte e cinco,* [p=0.2] com doze termos: [p=0.2] o "
        "segundo mais o décimo primeiro [p=0.2] dá cinco mais vinte e três, [p=0.2] *vinte e oito.* [p=0.2] Igual a "
        "três mais vinte e cinco. [p=0.4] {c}Atalho: [p=0.2] os índices somam *n mais um.* [p=0.2] Dois mais onze, "
        "[p=0.2] *treze.* [p=0.4] {d}Basta *um par* [p=0.2] para ter a soma: [p=0.2] vinte e oito vezes doze, "
        "[p=0.2] dividido por dois, [p=0.2] *cento e sessenta e oito.*"),

    # ================= BLOCO G: O TERMO MÉDIO =================
    dict(id="12", block="medio", text=
        "{t}E quando a quantidade de termos é *ímpar?* [p=0.4] {a}Aí existe um *termo médio:* [p=0.2] o que fica "
        "exatamente no meio da fila. [p=0.4] {b}Atalho: [p=0.2] ele *já é* a média dos extremos. [p=0.3] {c}Oito, "
        "onze, quatorze, dezessete, vinte. [p=0.2] O do meio é *quatorze.* [p=0.2] Cinco termos vezes quatorze: "
        "[p=0.2] *setenta.* [p=0.3] {d}Sem somar nada."),

    # ================= BLOCO H: O SAC =================
    dict(id="13", block="sac", text=
        "{t}E você já usou isso sem saber? [p=0.4] {a}Já, [p=0.2] *disfarçado.* [p=0.2] Na série de Empréstimos, "
        "[p=0.2] os juros do *SAC* caíam assim: [p=0.2] quatrocentos, [p=0.2] trezentos e vinte, [p=0.2] duzentos e "
        "quarenta, [p=0.2] cento e sessenta, [p=0.2] oitenta. [p=0.4] {b}Uma PA. [p=0.2] O total de juros foi "
        "quatrocentos mais oitenta, [p=0.2] vezes cinco, [p=0.2] dividido por dois: [p=0.2] *mil e duzentos.* [p=0.3] "
        "{c}Era a soma de Gauss [p=0.2] o tempo todo."),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quanto dá a soma dos *vinte primeiros termos* [p=0.2] de *cinco, oito, onze,* e assim "
        "por diante? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O último termo não foi dado. [p=0.2] Primeiro ele: [p=0.2] cinco, [p=0.2] mais "
        "*dezenove* saltos de três. [p=0.2] Cinco mais cinquenta e sete: [p=0.2] *sessenta e dois.* [p=0.4] {b}Agora "
        "a soma: [p=0.2] cinco mais sessenta e dois, [p=0.2] *sessenta e sete.* [p=0.2] Vezes vinte, [p=0.2] dividido "
        "por dois. [p=0.4] {c}A metade antes: [p=0.2] vinte vira *dez.* [p=0.2] Sessenta e sete vezes dez: [p=0.2] "
        "*seiscentos e setenta.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] primeiro com último: [p=0.2] todos os pares dão a "
        "mesma soma. [p=0.5] {b}Dois: [p=0.2] soma é número de termos vezes a média dos extremos. [p=0.5] {c}Três: "
        "[p=0.2] *no décimo segundo* é termo; [p=0.2] *em doze* ou *ao todo* é soma."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *esquecer de dividir por dois.* [p=0.2] "
        "Sessenta e sete vezes vinte: [p=0.2] *mil trezentos e quarenta.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "você juntou os extremos e multiplicou pelos termos. [p=0.4] {c}Mas assim você somou a fila *duas vezes:* "
        "[p=0.2] as duas escadas. [p=0.2] A soma é a metade: [p=0.2] seiscentos e setenta."),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] responder o *termo* quando pedem a *soma,* [p=0.2] ou o contrário. [p=0.2] Sessenta e "
        "dois [p=0.2] no lugar de seiscentos e setenta. [p=0.4] {b}Parece certo, [p=0.2] porque as duas contas "
        "aparecem na resolução, [p=0.2] e as duas estão nas alternativas. [p=0.4] {c}Atalho: [p=0.2] *sublinhe a "
        "palavra.* [p=0.2] *No vigésimo* é termo; [p=0.2] *ao todo* é soma."),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] calcular o último termo com *n saltos.* [p=0.2] Cinco mais vinte vezes três: "
        "[p=0.2] *sessenta e cinco.* [p=0.2] E a soma vira *setecentos.* [p=0.4] {b}Parece certo, [p=0.2] porque são "
        "vinte termos, [p=0.2] então parecem vinte saltos. [p=0.4] {c}Mas do primeiro ao vigésimo [p=0.2] são "
        "*dezenove* saltos. [p=0.2] Sempre *n menos um.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="20", block="q3", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um teatro tem "
        "*vinte e cinco fileiras.* [p=0.2] A primeira tem *vinte cadeiras,* [p=0.2] e cada fileira seguinte tem *duas "
        "a mais* que a anterior. [p=0.3] O número *total* de cadeiras do teatro é: [p=0.3] {qa}A: [p=0.2] mil e cem. "
        "[p=0.2] {qb}B: [p=0.2] mil cento e vinte e cinco. [p=0.2] {qc}C: [p=0.2] mil cento e cinquenta. [p=0.2] "
        "{qd}D: [p=0.2] mil e setecentos. [p=0.2] {qe}E: [p=0.2] dois mil e duzentos. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="21", block="q3", text=
        "{t}Termo ou soma? [p=0.3] {a}*Total:* [p=0.2] é soma. [p=0.4] {b}Última fileira: [p=0.2] vinte mais vinte e "
        "quatro vezes dois, [p=0.2] *sessenta e oito.* [p=0.4] {c}Vinte mais sessenta e oito: [p=0.2] oitenta e oito. "
        "[p=0.2] Metade: [p=0.2] *quarenta e quatro.* [p=0.2] Vezes vinte e cinco: [p=0.2] *mil e cem.* [p=0.3] "
        "{d}Faz sentido: [p=0.2] a fileira do meio tem quarenta e quatro cadeiras. [p=0.2] {ok}*Letra A!*"),
    dict(id="22", block="q3", text=
        "{t}E as armadilhas? [p=0.3] {xb}A B dá *um salto a mais:* [p=0.2] última fileira com setenta. [p=0.4] {xc}A C "
        "faz a primeira fileira *também* ganhar duas cadeiras: [p=0.2] quinhentos mais seiscentos e cinquenta. [p=0.4] "
        "{xd}A D supõe que *todas* as fileiras têm sessenta e oito. [p=0.4] {xe}E a E *esquece de dividir por dois.*"),

    # ================= QUESTÃO 8 (NÓS FAZEMOS) =================
    dict(id="23", block="q8", text=
        "{t}Agora fazemos juntos. [p=0.3] {a}Um atleta correu *dois quilômetros* no primeiro dia de treino [p=0.2] e, "
        "a cada dia seguinte, [p=0.2] *meio quilômetro a mais.* [p=0.3] *Ao fim dos doze primeiros dias,* [p=0.2] a "
        "distância total foi, em quilômetros: [p=0.3] {qa}A: [p=0.2] quarenta e cinco. [p=0.2] {qb}B: [p=0.2] "
        "cinquenta e sete. [p=0.2] {qc}C: [p=0.2] sessenta. [p=0.2] {qd}D: [p=0.2] noventa. [p=0.2] {qe}E: [p=0.2] "
        "cento e quatorze. [p=0.5] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q8", text=
        "{t}Sublinhe a palavra. [p=0.3] {a}*Ao fim dos doze dias:* [p=0.2] é *soma.* [p=0.4] {b}O décimo segundo dia: "
        "[p=0.2] dois, [p=0.2] mais *onze* saltos de meio. [p=0.2] Dois mais cinco e meio: [p=0.2] *sete e meio.* "
        "[p=0.4] {c}Extremos: [p=0.2] dois mais sete e meio, [p=0.2] nove e meio. [p=0.2] A metade antes: [p=0.2] doze "
        "vira *seis.* [p=0.2] Nove e meio vezes seis: [p=0.2] *cinquenta e sete.* [p=0.3] {ok}*Letra B!*"),
    dict(id="25", block="q8", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A *esquece o primeiro termo* na soma. [p=0.4] {xc}A C dá *doze* saltos: "
        "[p=0.2] último dia com oito. [p=0.4] {xd}A D faz o atleta correr sete e meio *todos* os dias. [p=0.4] {xe}E a "
        "E esquece de dividir por dois."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="26", block="q9", text=
        "{t}E esta é *sua.* [p=0.3] {a}Em uma progressão aritmética de *vinte termos,* [p=0.2] a soma do *terceiro* "
        "com o *décimo oitavo* termo [p=0.2] é igual a *cinquenta.* [p=0.3] A soma de *todos* os vinte termos é: "
        "[p=0.3] {qa}A: [p=0.2] duzentos e cinquenta. [p=0.2] {qb}B: [p=0.2] quatrocentos e cinquenta. [p=0.2] {qc}C: "
        "[p=0.2] quatrocentos e setenta e cinco. [p=0.2] {qd}D: [p=0.2] quinhentos. [p=0.2] {qe}E: [p=0.2] mil. "
        "[p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="q9", text=
        "{t}Conferindo. [p=0.3] {a}Três mais dezoito: [p=0.2] *vinte e um.* [p=0.2] Um mais vinte: [p=0.2] também "
        "vinte e um. [p=0.2] São *equidistantes.* [p=0.4] {b}Então o primeiro mais o último [p=0.2] também dá "
        "*cinquenta.* [p=0.4] {c}Soma: [p=0.2] cinquenta vezes vinte, [p=0.2] dividido por dois. [p=0.2] Cinquenta "
        "vezes dez: [p=0.2] *quinhentos.* [p=0.3] {d}Sem achar o primeiro termo, [p=0.2] sem achar a razão. [p=0.2] "
        "{ok}*Letra D!*"),
    dict(id="28", block="q9", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A divide por dois *duas vezes.* [p=0.4] {xb}A B conta *dezoito* termos, "
        "[p=0.2] {xc}e a C, *dezenove:* [p=0.2] erros de contagem. [p=0.4] {xe}E a E esquece de dividir por dois."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] primeiro com último: [p=0.2] todos os pares "
        "dão a mesma soma. [p=0.5] {b}Dois: [p=0.2] soma é número de termos vezes a média dos extremos. [p=0.5] "
        "{c}Três: [p=0.2] *no décimo segundo* é termo; [p=0.2] *em doze* ou *ao todo* é soma."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}Juros simples, [p=0.2] calendário, [p=0.2] prestação de financiamento: [p=0.3] a PA aparece em muito lugar "
        "*sem dizer o nome.* [p=0.4] {b}E você já esbarrou nela em outras séries. [p=0.4] {c}Próximo episódio: "
        "[p=0.2] *a PA disfarçada.*"),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você conseguiria somar de um a cem antes do Gauss? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
