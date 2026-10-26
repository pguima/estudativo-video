# Roteiro — Progressão Aritmética, Episódio 2 de 5: contar termos e saltos (meios, postes, múltiplos e três termos)
# Base: Estudos/Enem/estudos/01-matematica/31-progressao-aritmetica.html — seção 07; da seção 05, só "termo do meio é a
#   média dos vizinhos" e "notação simétrica para três termos"; Questões 4, 5 e 6 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   POSTES E INTERVALOS: entre 7 postes há 6 vãos (bolinhas = termos, arcos = saltos, sempre um de diferença).
#   O "+ 1" conta o PRIMEIRO termo, que não é um salto.
#   Chame os três de x − r, x e x + r: na soma, o r se cancela e SOME.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos: os blocos b e c usam a Questão 4 (postes) e a contagem de múltiplos de 7, como pede o prompt (a Q4 é "eu faço";
#   a contagem de múltiplos de 7 já está no gancho do usuário e a Q5 é "nós fazemos": o novo nela são as alternativas).
#   Exemplo NOSSO no bloco a: 3 meios entre 2 e 14 → 5 termos, 4 saltos, r = 3 (2, 5, 8, 11, 14).
#   TROCA no bloco f: o prompt usava "soma 36 → o do meio é 12", que é o primeiro passo da Q6 ("você faz", perímetro 36).
#   Usei soma 45 → o do meio é 15 (ex.: 10, 15, 20). O triângulo 3-4-5 do material também só aparece na resolução da Q6.
#   O erro 1 usa os dados do prompt (5 meios entre 3 e 27: 24/5 × 24/6), já resolvidos no bloco b.
# Nós fazemos (prompt): múltiplos de 6 entre 50 e 200: 54 ... 198 → (198 − 54) ÷ 6 + 1 = 24 + 1 = 25.
# QUESTÃO 4 (texto idêntico na tela): 7 postes, 6 vãos, 24 ÷ 6 = 4 km → C. Erradas (do material): A = 24 ÷ 8 = 3;
#   B = 24 ÷ 7 ≈ 3,43; D = 24 ÷ 5 = 4,8; E = 24 ÷ 4 = 6.
# QUESTÃO 5 (texto idêntico): 105 ... 497 → (497 − 105) ÷ 7 + 1 = 57 → C. Erradas (do material): B (56) esquece o "+ 1";
#   A (55) esquece o "+ 1" e ainda deixa o 497 de fora (o material diz só "exclui também o 497": a explicação completa é
#   NOSSA — sem o 497 e com o "+ 1" daria 56, não 55); D (58) começa do 98, que é menor que 100;
#   E (71) conta todos os múltiplos de 7 desde o 7 (497 ÷ 7 = 71).
# QUESTÃO 6 (texto idêntico): x − r, x, x + r; 3x = 36 → x = 12; (12 + r)² = 12² + (12 − r)² → 48r = 144 → r = 3;
#   lados 9, 12, 15; área 9 · 12 ÷ 2 = 54 → B. Erradas (do material): A (36) confunde área com perímetro;
#   C (67,5) usa a hipotenusa como cateto: 9 · 15 ÷ 2; D (72) usa o termo do meio como os dois catetos: 12 · 12 ÷ 2;
#   E (108) esquece de dividir por 2.
# Atalhos (verde): desenhe a fila (saltos = termos − 1) · n = (último − primeiro) ÷ r + 1 · soma de três em PA ÷ 3 = o do meio.
# Frases-chave (meio e fim, idênticas): 1. k meios entre dois números: k + 2 termos e k + 1 saltos.
#   2. Contar termos: (último − primeiro) ÷ razão, mais 1. 3. Três em PA: x − r, x e x + r.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Postes, múltiplos e o erro de um: contar termos na PA | PA Ep. 2"
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
        "{a}Quantos números múltiplos de sete existem [p=0.2] de cento e cinco até quatrocentos e noventa e sete? "
        "[p=0.5] {b}A conta, [p=0.2] quatrocentos e noventa e sete menos cento e cinco, [p=0.2] dividido por sete, "
        "[p=0.2] dá *cinquenta e seis.* [p=0.4] {c}A resposta certa é *cinquenta e sete.* [p=0.4] {d}Um termo some, "
        "[p=0.2] e a alternativa errada [p=0.2] *está lá esperando.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai contar *termos, saltos e postes* sem errar por um, [p=0.3] {b}e "
        "resolver problemas de *três números em PA* [p=0.2] em uma linha."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] um termo qualquer é o *primeiro,* "
        "[p=0.2] mais *n menos um* saltos de tamanho *r.* [p=0.4] {b}Da série de Divisibilidade: [p=0.2] os "
        "*múltiplos de sete* são a tabuada do sete: [p=0.2] sete, catorze, vinte e um..."),
    dict(id="04", block="prereq", text=
        "{a}E Pitágoras, [p=0.2] no triângulo com *ângulo reto,* [p=0.2] o canto de esquadro. [p=0.4] "
        "{b}Os dois lados que formam esse canto são os *catetos.* [p=0.2] O lado maior, [p=0.2] do outro lado, [p=0.2] "
        "é a *hipotenusa.* [p=0.4] {c}A regra: [p=0.2] *hipotenusa ao quadrado [p=0.2] é igual a cateto ao quadrado "
        "mais cateto ao quadrado.* [p=0.4] {d}E a área desse triângulo [p=0.2] é *cateto vezes cateto, [p=0.2] dividido "
        "por dois.*"),

    # ================= CONCRETO =================
    dict(id="05", block="concreto", text=
        "{t}Agora, uma cerca. [p=0.3] {a}Ela tem *trinta metros,* [p=0.2] com uma estaca a cada *três metros,* [p=0.2] "
        "uma em cada ponta. [p=0.4] {b}Conte comigo, [p=0.2] no dedo: [p=0.2] os pedaços de cerca entre duas estacas "
        "[p=0.2] são *dez.* [p=0.4] {c}E as estacas? [p=0.3] *Onze.* [p=0.4] {d}Sempre *uma a mais.* [p=0.2] Guarde esse "
        "*um:* [p=0.2] ele é o assunto de hoje."),

    # ================= BLOCO A: INTERPOLAR =================
    dict(id="06", block="interpolar", text=
        "{t}O que é *interpolar?* [p=0.4] {a}É colocar números no meio [p=0.2] de dois números dados, [p=0.2] "
        "formando uma PA. [p=0.4] {b}Os dois números dados, [p=0.2] o primeiro e o último, [p=0.2] são os "
        "*extremos.* [p=0.2] E os números colocados entre eles [p=0.2] são os *meios aritméticos.* [p=0.4] {c}Exemplo: "
        "[p=0.2] três meios entre *dois* e *catorze.*"),
    dict(id="07", block="interpolar", text=
        "{t}Quantos termos fica a PA? [p=0.3] {a}Os três meios, [p=0.2] *mais os dois extremos:* [p=0.2] *cinco "
        "termos.* [p=0.4] {b}E quantos saltos entre eles? [p=0.3] Um a menos: [p=0.2] *quatro saltos.* [p=0.4] {c}De dois a "
        "catorze, [p=0.2] *doze;* [p=0.2] dividido por quatro saltos: [p=0.2] razão *três.* [p=0.4] {d}A PA fica: [p=0.2] dois, cinco, oito, onze, catorze. [p=0.4] {e}A regra: "
        "[p=0.2] com *k* meios, [p=0.2] são *k mais dois* termos [p=0.2] e *k mais um* saltos."),

    # ================= BLOCO B: OS POSTES =================
    dict(id="08", block="postes", text=
        "{t}Agora, uma rodovia. [p=0.3] {a}Tem um poste no *quilômetro três* [p=0.2] e outro no *quilômetro vinte e "
        "sete.* [p=0.4] {b}Vão instalar *cinco postes* no meio, [p=0.2] todos com o mesmo espaço. [p=0.2] Qual é a "
        "distância entre dois vizinhos? [p=0.4] {c}Conte os postes: [p=0.2] cinco novos, [p=0.2] mais os dois das "
        "pontas: [p=0.2] *sete postes.* [p=0.4] {d}E os vãos? [p=0.3] Entre sete postes, [p=0.2] *seis vãos.*"),
    dict(id="09", block="postes", text=
        "{t}E a conta é com os vãos. [p=0.3] {a}Vinte e sete menos três: [p=0.2] *vinte e "
        "quatro quilômetros.* [p=0.4] {b}Divididos em *seis* vãos iguais: [p=0.2] seis *r* igual a vinte e quatro, "
        "[p=0.2] *r* igual a *quatro quilômetros.* [p=0.4] {c}Postes e intervalos: [p=0.2] *entre sete postes há seis "
        "vãos.*"),
    dict(id="10", block="atalho_fila", text=
        "{t}O atalho que salva tudo isso: [p=0.3] {a}*desenhe a fila* antes de dividir. [p=0.4] {b}Uma bolinha para "
        "cada termo, [p=0.2] um arco para cada salto. [p=0.4] {c}Conte as bolinhas, [p=0.2] conte os arcos: [p=0.2] "
        "sempre *um arco a menos.* [p=0.2] E divida pelos *arcos.*"),

    # ================= BLOCO C: CONTAR TERMOS =================
    dict(id="11", block="contar", text=
        "{t}E quando a pergunta é *quantos termos?* [p=0.4] {a}Quantos múltiplos de sete há entre cem e quinhentos? "
        "[p=0.4] {b}*Múltiplo* de sete é um número que a divisão por sete deixa *sem resto.* [p=0.4] {c}O primeiro "
        "depois de cem: [p=0.2] cem dividido por sete dá catorze e sobra; [p=0.2] quinze vezes sete, [p=0.2] *cento e "
        "cinco.* [p=0.4] {d}O último antes de quinhentos: [p=0.2] setenta e um vezes sete, [p=0.2] *quatrocentos e "
        "noventa e sete.*"),
    dict(id="12", block="contar", text=
        "{t}Eles formam uma PA de razão sete. [p=0.3] {a}Pelo termo geral: [p=0.2] quatrocentos e noventa e sete "
        "[p=0.2] é igual a cento e cinco, [p=0.2] mais *n menos um* vezes sete. [p=0.4] {b}A distância, [p=0.2] "
        "trezentos e noventa e dois, [p=0.2] dividida por sete: [p=0.2] *n menos um* é *cinquenta e seis.* [p=0.4] "
        "{c}Então *n* é *cinquenta e sete.* [p=0.4] {d}Os cinquenta e seis eram os *saltos.* [p=0.2] Os termos são "
        "*um a mais.*"),
    dict(id="13", block="atalho_contar", text=
        "{t}Atalho para a prova: [p=0.3] {a}o número de termos é [p=0.2] *último menos primeiro, [p=0.2] dividido pela "
        "razão, [p=0.2] mais um.* [p=0.4] {b}A divisão conta os *saltos.* [p=0.4] {c}E o mais um? [p=0.3] *O mais um "
        "conta o primeiro termo, [p=0.2] que não é um salto.* "),

    # ================= BLOCO D: POSTES FORA DA FÓRMULA =================
    dict(id="14", block="cerca", text=
        "{t}Lembra da cerca? [p=0.3] {a}Trinta dividido por três [p=0.2] dá os *intervalos,* [p=0.2] os pedaços "
        "entre duas estacas: [p=0.2] *dez.* [p=0.2] {b}As estacas: [p=0.2] *onze.* [p=0.4] {c}Sem fórmula nenhuma, "
        "[p=0.2] é o mesmo *um.* [p=0.4] {d}Antes de responder, [p=0.2] pergunte: [p=0.2] o problema pediu os *objetos* "
        "[p=0.2] ou os *espaços* entre eles?"),

    # ================= BLOCO E: MÉDIA DOS VIZINHOS =================
    dict(id="15", block="media", text=
        "{t}E o termo do meio? [p=0.4] {a}A *média aritmética* de dois "
        "números [p=0.2] é a soma dividida por dois. [p=0.4] {b}Numa PA, [p=0.2] o termo do meio *é a média dos "
        "vizinhos.* [p=0.2] Ele dá um salto para cada lado: [p=0.2] fica bem no meio. [p=0.4] {c}Então: [p=0.2] "
        "*duas vezes o do meio [p=0.2] é igual à soma dos vizinhos.*"),
    dict(id="16", block="media", text=
        "{t}Exemplo: [p=0.2] *x, dez, dezesseis.* [p=0.2] Quanto vale *x*? [p=0.4] {a}Duas vezes dez, [p=0.2] vinte, "
        "[p=0.2] é igual a *x* mais dezesseis. [p=0.4] {b}*x* é *quatro.* [p=0.4] {c}Confira: [p=0.2] quatro, dez, "
        "dezesseis. [p=0.2] Saltos de seis. [p=0.2] *É PA.*"),

    # ================= BLOCO F: NOTAÇÃO SIMÉTRICA =================
    dict(id="17", block="simetrica", text=
        "{t}E quando são *três números em PA* [p=0.2] e só a soma é conhecida? [p=0.4] {a}Use a *notação simétrica:* "
        "[p=0.2] um jeito de dar nome aos três [p=0.2] a partir do *termo do meio.* [p=0.4] {b}Chame o do meio de "
        "*x.* [p=0.2] O da esquerda é *x menos r,* [p=0.2] o da direita, [p=0.2] *x mais r.* [p=0.4] {c}Agora some: "
        "[p=0.2] o menos *r* e o mais *r* [p=0.2] *se cancelam.* [p=0.2] O *r* some, [p=0.2] e sobra *três x.*"),
    dict(id="18", block="atalho_simetrica", text=
        "{t}O atalho: [p=0.3] {a}três números em PA [p=0.2] com soma *quarenta e cinco.* [p=0.4] {b}Três *x* igual a "
        "quarenta e cinco: [p=0.2] o do meio é *quinze,* [p=0.2] *na hora.* [p=0.4] {c}Dividiu a soma por três, "
        "[p=0.2] achou o do meio. "),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quantos *múltiplos de seis* há [p=0.2] entre *cinquenta* e *duzentos?* [p=0.4] "
        "{b}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O primeiro: [p=0.2] nove vezes seis, [p=0.2] *cinquenta e quatro.* [p=0.4] "
        "{b}O último: [p=0.2] trinta e três vezes seis, [p=0.2] *cento e noventa e oito.* "
        "[p=0.4] {c}Último menos primeiro: [p=0.2] *cento e quarenta e quatro.* [p=0.2] Dividido por seis: [p=0.2] "
        "*vinte e quatro saltos.* [p=0.4] {d}Mais um, [p=0.2] o primeiro termo: [p=0.2] *vinte e cinco.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] *k* meios entre dois números: [p=0.2] *k* mais dois "
        "termos [p=0.2] e *k* mais um saltos. [p=0.5] {b}Dois: [p=0.2] contar termos: [p=0.2] último menos primeiro, "
        "[p=0.2] dividido pela razão, [p=0.2] mais um. [p=0.5] {c}Três: [p=0.2] três em PA: [p=0.2] *x* menos *r,* "
        "[p=0.2] *x* [p=0.2] e *x* mais *r.*"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] cinco meios entre três e vinte e sete, "
        "[p=0.2] e a razão sai *vinte e quatro dividido por cinco.* [p=0.4] {b}Parece certo, [p=0.2] porque o "
        "enunciado falou *cinco.* [p=0.4] {c}Mas cinco são os postes *novos.* [p=0.2] Com os extremos, [p=0.2] são "
        "sete termos [p=0.2] e *seis* saltos: [p=0.2] vinte e quatro dividido por *seis.*"),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] *esquecer o mais um* [p=0.2] na contagem de múltiplos. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque cinquenta e seis sai redondinho. [p=0.4] {c}Mas a divisão contou os *saltos.* [p=0.2] Falta o "
        "primeiro termo: [p=0.2] *some o um.*"),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] contar os *intervalos* [p=0.2] quando o problema pede os *objetos,* [p=0.2] ou o "
        "contrário. [p=0.4] {b}Parece certo, [p=0.2] porque a divisão dá um número limpo. [p=0.4] {c}Mas dez "
        "são os pedaços da cerca; [p=0.2] estacas, *onze.* [p=0.2] *Desenhe a fila.*"),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="25", block="q4", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Esta, [p=0.2] eu resolvo "
        "com você. [p=0.4] {a}Em um trecho reto de rodovia, [p=0.2] há postes no *quilômetro três* e no *quilômetro "
        "vinte e sete.* [p=0.2] A concessionária vai instalar mais *cinco postes* entre esses dois, [p=0.2] de modo "
        "que todos os sete postes fiquem igualmente espaçados. [p=0.2] A distância entre dois postes vizinhos será "
        "de: [p=0.4] {qa}A: [p=0.2] três quilômetros. [p=0.3] {qb}B: [p=0.2] três vírgula quarenta e três. [p=0.3] "
        "{qc}C: [p=0.2] quatro. [p=0.3] {qd}D: [p=0.2] quatro vírgula oito. [p=0.3] {qe}E: [p=0.2] seis "
        "quilômetros."),
    dict(id="26", block="q4", text=
        "{t}Desenhe a fila. [p=0.3] {a}Sete postes: [p=0.2] sete bolinhas. [p=0.2] Entre elas, [p=0.2] *seis* arcos. "
        "[p=0.4] {b}Distância toda: [p=0.2] vinte e quatro quilômetros. [p=0.2] Dividida por seis vãos: [p=0.2] "
        "*quatro quilômetros.* [p=0.4] {c}Conferindo: [p=0.2] três, sete, onze, quinze, dezenove, vinte e três, "
        "[p=0.2] vinte e sete. [p=0.2] Fechou. [p=0.3] {ok}*Letra C!*"),
    dict(id="27", block="q4", text=
        "{t}E as erradas? [p=0.2] Cada uma dividiu por outro número. [p=0.4] {xa}A A, [p=0.2] por *oito.* [p=0.4] {xb}A B, [p=0.2] por *sete:* [p=0.2] o número de postes. "
        "[p=0.4] {xd}A D, [p=0.2] por *cinco:* [p=0.2] só os postes novos. [p=0.4] {xe}E a E, [p=0.2] por *quatro,* "
        "[p=0.2] como se fossem cinco postes no total."),

    # ================= QUESTÃO 5 (NÓS FAZEMOS) =================
    dict(id="28", block="q5", text=
        "{t}Agora, juntos. [p=0.3] {a}Uma gráfica numera ingressos de *cem* a *quinhentos.* [p=0.2] Os "
        "ingressos cujo número é *múltiplo de sete* [p=0.2] dão direito a um brinde. [p=0.2] A quantidade de ingressos "
        "premiados é: [p=0.4] {qa}A: [p=0.2] cinquenta e cinco. [p=0.3] {qb}B: [p=0.2] cinquenta e seis. [p=0.3] "
        "{qc}C: [p=0.2] cinquenta e sete. [p=0.3] {qd}D: [p=0.2] cinquenta e oito. [p=0.3] {qe}E: [p=0.2] setenta e "
        "um. [p=0.5] {p}Você já viu essa conta hoje. [p=0.2] *Pause e tente.* [p=2.0]"),
    dict(id="29", block="q5", text=
        "{t}Primeiro e último: [p=0.2] *cento e cinco* [p=0.2] e *quatrocentos e noventa e sete.* [p=0.4] {a}Último "
        "menos primeiro, [p=0.2] dividido por sete: [p=0.2] cinquenta e seis saltos. [p=0.2] Mais um: [p=0.2] "
        "*cinquenta e sete.* [p=0.3] {ok}*Letra C!* [p=0.4] {xb}A B [p=0.2] *esqueceu o mais um.* [p=0.4] {xa}A A "
        "esqueceu o mais um [p=0.2] *e ainda* deixou o quatrocentos e noventa e sete de fora. [p=0.4] {xd}A D começou "
        "no *noventa e oito,* [p=0.2] que é menor que cem. [p=0.4] {xe}E a E [p=0.2] contou desde o *sete.*"),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="30", block="q6", text=
        "{t}E esta é *sua.* [p=0.3] {a}Um terreno tem a forma de um *triângulo retângulo* [p=0.2] cujos lados, em "
        "metros, [p=0.2] formam uma *progressão aritmética.* [p=0.2] O *perímetro* do terreno, [p=0.2] a soma dos "
        "três lados, [p=0.2] é *trinta e seis metros.* [p=0.2] A área do terreno, em metros quadrados, é: [p=0.4] "
        "{qa}A: [p=0.2] trinta e seis. [p=0.3] {qb}B: [p=0.2] cinquenta e quatro. [p=0.3] {qc}C: [p=0.2] sessenta e "
        "sete vírgula cinco. [p=0.3] {qd}D: [p=0.2] setenta e dois. [p=0.3] {qe}E: [p=0.2] cento e oito. [p=0.5] "
        "{p}Dica: [p=0.2] notação simétrica. [p=0.2] *Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="31", block="q6", text=
        "{t}Conferindo. [p=0.3] {a}Lados: [p=0.2] *x menos r, x* e *x mais r.* [p=0.2] A soma é três *x:* [p=0.2] "
        "trinta e seis. [p=0.2] O do meio é *doze.* [p=0.4] {b}A hipotenusa é o maior lado: [p=0.2] *doze mais r.* "
        "[p=0.4] {c}Pitágoras: [p=0.2] doze mais *r,* ao quadrado, [p=0.2] é igual a doze ao quadrado [p=0.2] mais "
        "doze menos *r,* ao quadrado. [p=0.4] {d}Abrindo os quadrados, [p=0.2] o *r* ao quadrado cancela. [p=0.2] "
        "Sobra *quarenta e oito r* igual a *cento e quarenta e quatro:* [p=0.2] *r* é "
        "*três.*"),
    dict(id="32", block="q6", text=
        "{t}Os lados: [p=0.2] *nove, doze e quinze.* [p=0.4] {a}Confira Pitágoras: [p=0.2] oitenta e um mais cento e "
        "quarenta e quatro [p=0.2] dá duzentos e vinte e cinco, [p=0.2] que é quinze ao quadrado. [p=0.4] {b}Área: "
        "[p=0.2] cateto vezes cateto, [p=0.2] nove vezes doze, [p=0.2] dividido por dois: [p=0.2] *cinquenta e quatro "
        "metros quadrados.* [p=0.3] {ok}*Letra B!* [p=0.4] {xa}A A confundiu área com *perímetro.* [p=0.3] {xc}A C "
        "usou a *hipotenusa* como cateto. [p=0.3] {xd}A D usou o *doze* duas vezes. [p=0.3] {xe}E a E esqueceu de "
        "*dividir por dois.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] *k* meios entre dois números: [p=0.2] *k* mais "
        "dois termos [p=0.2] e *k* mais um saltos. [p=0.5] {b}Dois: [p=0.2] contar termos: [p=0.2] último menos "
        "primeiro, [p=0.2] dividido pela razão, [p=0.2] mais um. [p=0.5] {c}Três: [p=0.2] três em PA: [p=0.2] *x* "
        "menos *r,* [p=0.2] *x* [p=0.2] e *x* mais *r.*"),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Um menino somou [p=0.2] um mais dois mais três, [p=0.2] e assim por diante, até cem, [p=0.2] *em "
        "segundos,* [p=0.2] sem calculadora. [p=0.5] {b}O truque dele [p=0.2] soma *qualquer PA.* [p=0.5] "
        "{c}Próximo episódio."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já errou por um contando postes? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
