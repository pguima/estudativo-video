# Roteiro — Equações e Inequações do 1º Grau, Episódio 2 de 5: do texto à equação (idades, partes de um total e misturas).
# Base: Estudos/Enem/estudos/01-matematica/20-equacoes-inequacoes-1o-grau.html — seção 05 + Questões 5, 3 e 9 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A ETIQUETA do x: "x = idade do filho, em anos" (fica no canto da tela durante cada questão).
#   O TEMPO PASSA PARA TODOS: daqui a 4 anos, TODO MUNDO fica 4 anos mais velho.
#   Na mistura, o álcool que entra também aumenta o tanque: mexe EM CIMA e EMBAIXO da fração.
#   A RAIZ NÃO É A RESPOSTA: depois de achar o x, volte e leia a pergunta.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos dos blocos b e c: os do prompt e do material (consecutivos 84 → 27, 28, 29; Ana e Bia, 96 → 24 e 72).
#   Exemplos NOSSOS (conferidos em Python), para não entregar as questões:
#   bloco e (frações): salário de R$ 1.200,00, metade no aluguel; 1/4 "do salário" = R$ 300,00 × 1/4 "do restante" = R$ 150,00.
#   bloco f (mistura): 20 L com 10% de álcool (2 L), chegar a 20%: (2 + x)/(20 + x) = 0,2 → 0,8x = 2 → x = 2,5 L
#   (conferência: 4,5 L em 22,5 L = 20%). A Q9 é a "você faz".
# Nós fazemos (prompt): mãe 30, filha 6: 30 + k = 3(6 + k) → 12 = 2k → k = 6; conferência 36 = 3 · 12.
# QUESTÃO 5 (eu faço, texto idêntico): f + (52 − f); (52 − f) + 4 = 3(f + 4) → 44 = 4f → f = 11 → A. Conferência 45 = 3 · 15.
#   Erradas (material): B 13 ignora os 4 anos (p = 3f: certa se o triplo fosse HOJE); C 14 soma 4 só ao pai (p + 4 = 3f);
#   D 15 = idade do filho daqui a 4 anos; E 41 = idade atual do pai. O gancho ("quatro alternativas erradas são respostas
#   certas para outras perguntas") é dito como no prompt; o vídeo mostra a pergunta de cada uma (a da C é "torta":
#   o pai daqui a 4 anos contra o filho de hoje).
# QUESTÃO 3 (nós fazemos, texto idêntico): 1/3 + 1/4 = 7/12 do salário; sobram 5/12 → x = 1 250 · 12/5 = 3 000 → E.
#   Erradas (material): A 1.750 soma 1/3 + 1/4 = 2/7; B 1.979,17 aplica as frações aos 1.250 e soma tudo;
#   C 2.142,86 troca o que sobrou pelo gasto (7/12 x = 1 250); D 2.500 calcula a alimentação "do restante".
# QUESTÃO 9 (você faz, texto idêntico): 10 L de álcool; (10 + x)/(40 + x) = 0,4 → 0,6x = 6 → x = 10 → B.
#   Erradas (material): A 6 esquece que o volume cresce; C 15 divide 6 por 0,4; D 16 = álcool a 40% nos 40 L originais;
#   E 50 = volume final.
# Atalhos (verde, acrescentados por nós e conferidos): consecutivos — o do meio é a soma ÷ 3 (84 ÷ 3 = 28);
#   partes — total ÷ número de partes (96 ÷ 4 = 24); idades — a DIFERENÇA de idade nunca muda (mãe − filha = 24; no triplo,
#   a diferença vale 2 filhas → filha 12 → k = 6; Q5: diferença 30 → filho daqui a 4 anos 15 → hoje 11);
#   frações — "sobrou 5/12": divida por 5 e multiplique por 12; mistura — CONTE A ÁGUA, que não muda
#   (18 L = 80% → total 22,5 L → x = 2,5; Q9: 30 L = 60% → total 50 L → x = 10).
# Frases-chave (meio e fim, idênticas): 1. Primeiro a etiqueta do x, com unidade. 2. O tempo passa para todos.
#   3. Achou o x? Releia a pergunta.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Do texto à equação: idades, partes e misturas sem cair na pegadinha · Matemática ENEM, Equações episódio 2"

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
    "MMC": "eme eme cê",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Pai e filho somam *cinquenta e dois anos.* [p=0.3] {b}Daqui a quatro anos, [p=0.2] o pai terá o *triplo* da "
        "idade do filho. [p=0.5] {c}Quatro alternativas erradas dessa questão [p=0.2] são respostas *certas...* [p=0.4] "
        "{d}para *outras perguntas.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai transformar *texto em equação* [p=0.2] com um roteiro de *quatro passos* [p=0.3] "
        "{b}e não vai cair na resposta da *pergunta errada.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Da série de Expressões Algébricas: [p=0.2] *o dobro da soma* é "
        "dois vezes, abre parênteses, x mais y. [p=0.2] *A soma do dobro* é dois x mais y. [p=0.4] {b}Da série de "
        "Frações: [p=0.2] um terço mais um quarto, [p=0.2] pelo MMC doze, [p=0.2] dá *sete doze avos.* [p=0.4] {c}E do "
        "episódio um: [p=0.2] o roteiro para *resolver.* [p=0.2] Hoje, o passo de antes: [p=0.2] *montar.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine esta conversa. [p=0.3] {a}A Ana tem o *triplo* do dinheiro da Bia. [p=0.2] As duas juntas têm "
        "*noventa e seis reais.* [p=0.3] {b}Quanto tem cada uma? [p=0.5] {c}Dá para chutar: [p=0.2] Bia com dez, Ana com "
        "trinta? [p=0.2] Só quarenta. [p=0.4] {d}Chutar cansa. [p=0.2] A equação resolve de uma vez."),

    # ================= BLOCO A: O ROTEIRO =================
    dict(id="05", block="roteiro", text=
        "{t}Como transformar texto em conta? [p=0.4] {a}Passo um: [p=0.2] escolha a *incógnita,* [p=0.2] o valor "
        "escondido, [p=0.2] e escreva o que ela é, [p=0.2] *com unidade.* [p=0.2] É como preencher uma *etiqueta:* "
        "[p=0.2] x igual ao dinheiro da Bia, em reais. [p=0.4] {b}Passo dois: [p=0.2] escreva o resto *em função* dela. "
        "[p=0.2] A Ana tem o triplo: [p=0.2] *três x.* [p=0.4] {c}Passo três: [p=0.2] ache a *frase de igualdade.* "
        "[p=0.4] {d}Passo quatro: [p=0.2] resolva [p=0.2] e responda *o que foi pedido.*"),
    dict(id="06", block="roteiro", text=
        "{t}E que frase é essa? [p=0.4] {a}A *frase de igualdade* é o pedaço do texto que vira o *sinal de igual.* "
        "[p=0.4] {b}Ela aparece assim: [p=0.2] *é igual a,* [p=0.2] *custam o mesmo,* [p=0.2] *totaliza,* [p=0.2] "
        "*sobrou.* [p=0.4] {c}Na conversa: [p=0.2] *as duas juntas têm noventa e seis.*"),

    # ================= BLOCO B: CONSECUTIVOS =================
    dict(id="07", block="consecutivos", text=
        "{t}Três números seguidos somam oitenta e quatro. [p=0.2] Quais são? [p=0.4] {a}Números *consecutivos* são "
        "números seguidos, [p=0.2] como sete, oito, nove. [p=0.4] {b}Etiqueta: [p=0.2] x é o *menor.* [p=0.2] Depois, x "
        "mais um [p=0.2] e x mais dois. [p=0.4] {c}Somando: [p=0.2] três x mais três igual a oitenta e quatro. [p=0.2] x, "
        "*vinte e sete.* [p=0.4] {d}A resposta: [p=0.2] *vinte e sete, vinte e oito e vinte e nove.* [p=0.4] {e}Atalho: "
        "[p=0.2] o do *meio* é a soma dividida por três. [p=0.2] Oitenta e quatro por três: [p=0.2] vinte e oito."),

    # ================= BLOCO C: PARTES DE UM TOTAL =================
    dict(id="08", block="partes", text=
        "{t}E por que o x foi a Bia, [p=0.2] e não a Ana? [p=0.4] {a}x mais três x igual a noventa e seis. [p=0.2] Quatro "
        "x, noventa e seis. [p=0.2] x, *vinte e quatro.* [p=0.4] {b}A Bia tem *vinte e quatro reais;* [p=0.2] a Ana, "
        "*setenta e dois.* [p=0.4] {c}Se o x fosse a Ana, [p=0.2] a Bia seria *x sobre três:* [p=0.2] fração. [p=0.2] "
        "Chame de x a *menor parte.* [p=0.4] {d}Atalho: [p=0.2] Bia é uma parte, Ana são três. [p=0.2] Noventa e seis "
        "por quatro partes: [p=0.2] vinte e quatro."),

    # ================= BLOCO D: IDADES =================
    dict(id="09", block="idades", text=
        "{t}E nas idades, [p=0.2] onde está o perigo? [p=0.4] {a}Hoje, [p=0.2] o filho tem *f* anos [p=0.2] e "
        "o pai, *p.* [p=0.4] {b}Daqui a quatro anos, [p=0.2] o filho terá *f mais quatro.* [p=0.2] E o pai? [p=0.2] *p "
        "mais quatro.* [p=0.4] {c}*O tempo passa para todos.* [p=0.2] Daqui a quatro anos, [p=0.2] *todo mundo* fica "
        "quatro anos mais velho. [p=0.4] {d}E *há* três anos, [p=0.2] todo mundo tinha três a menos: [p=0.2] f menos "
        "três, [p=0.2] p menos três."),
    dict(id="10", block="idades", text=
        "{t}E tem um atalho de ouro. [p=0.4] {a}Se o pai é trinta anos mais velho, [p=0.2] daqui a quatro anos [p=0.2] "
        "continua trinta anos mais velho. [p=0.4] {b}A *diferença de idade nunca muda.* [p=0.2] Ela vai encurtar o "
        "exercício que vem aí."),

    # ================= BLOCO E: FRAÇÕES DE UM TOTAL =================
    dict(id="11", block="fracoes", text=
        "{t}Um quarto *do salário* [p=0.2] e um quarto *do restante* [p=0.2] são a mesma coisa? [p=0.4] {a}Salário de "
        "mil e duzentos. [p=0.2] Metade vai para o aluguel: [p=0.2] sobram seiscentos. [p=0.4] {b}Um quarto *do "
        "salário:* [p=0.2] *trezentos.* [p=0.4] {c}Um quarto *do restante,* [p=0.2] dos seiscentos: [p=0.2] *cento e "
        "cinquenta.* [p=0.4] {d}A diferença está numa palavra. [p=0.2] Como na série de Frações: [p=0.2] *sublinhe de "
        "quem é a fração.*"),

    # ================= BLOCO F: MISTURAS =================
    dict(id="12", block="mistura", text=
        "{t}E nas misturas, [p=0.2] o que muda quando entra álcool? [p=0.4] {a}O *soluto* é a substância que interessa, "
        "[p=0.2] aqui o álcool. [p=0.2] O *volume total* é o tanque inteiro. [p=0.4] {b}E a *concentração* é soluto "
        "[p=0.2] *dividido* pelo volume total. [p=0.4] {c}Vinte litros com dez por cento de álcool: [p=0.2] *dois litros* "
        "de álcool. [p=0.4] {d}Entra álcool puro: [p=0.2] sobe o álcool [p=0.2] *e sobe o tanque.* [p=0.2] Mexe *em "
        "cima* e *embaixo* da fração."),
    dict(id="13", block="mistura", text=
        "{t}Quanto álcool leva esse tanque a vinte por cento? [p=0.4] {a}Etiqueta: [p=0.2] x, os litros que entram. "
        "[p=0.2] Dois mais x, [p=0.2] sobre vinte mais x, [p=0.2] igual a zero vírgula dois. [p=0.4] {b}Dois mais x "
        "[p=0.2] igual a quatro mais zero vírgula dois x. [p=0.2] x, *dois litros e meio.* [p=0.4] {c}Atalho: [p=0.2] "
        "*conte a água,* [p=0.2] que não muda. [p=0.2] Dezoito litros, [p=0.2] que vão ser oitenta por cento. [p=0.2] "
        "Dezoito por zero vírgula oito: [p=0.2] vinte e dois e meio. [p=0.2] Menos vinte: [p=0.2] *dois e meio.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Hoje a mãe tem *trinta anos* [p=0.2] e a filha, *seis.* [p=0.2] Daqui a quantos anos a "
        "mãe terá o *triplo* da idade da filha? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Etiqueta: [p=0.2] *k,* os anos que vão passar. [p=0.2] O tempo passa para as "
        "duas: [p=0.2] trinta mais k [p=0.2] e seis mais k. [p=0.4] {b}A mãe terá o triplo: [p=0.2] trinta mais k [p=0.2] "
        "igual a três vezes seis mais k. [p=0.4] {c}Trinta mais k igual a dezoito mais três k. [p=0.2] Doze igual a dois "
        "k. [p=0.2] *k igual a seis.* [p=0.4] {d}Conferindo: [p=0.2] trinta e seis e doze. [p=0.2] Fechou. [p=0.4] "
        "{e}Pelo atalho: [p=0.2] a diferença é vinte e quatro, [p=0.2] e no triplo ela vale *duas* filhas. [p=0.2] Filha "
        "de doze: [p=0.2] seis anos depois."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] primeiro a etiqueta do x, com unidade. [p=0.5] {b}Dois: "
        "[p=0.2] o tempo passa para todos. [p=0.5] {c}Três: [p=0.2] achou o x? [p=0.2] Releia a pergunta."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar os quatro anos a uma pessoa só.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o texto fala dos anos *junto* com o nome de uma pessoa. [p=0.4] {c}Mas "
        "o tempo passa para todos: [p=0.2] some nos *dois.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] na mistura, [p=0.2] *esquecer que o volume total cresce.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque a gente só pensa no álcool que entrou. [p=0.4] {c}Mas o álcool entra *no tanque:* [p=0.2] ele mexe em "
        "cima e embaixo da fração."),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] *responder o x* quando a pergunta pede outra coisa. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o x deu um número bonito, [p=0.2] e ele está nas alternativas. [p=0.4] {c}A raiz não é a resposta. "
        "[p=0.2] Volte e leia a pergunta."),
    dict(id="20", block="erros", text=
        "{a}Quarto: [p=0.2] *somar frações sem MMC.* [p=0.2] Um terço mais um quarto [p=0.2] vira dois sétimos. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque é só somar em cima e somar embaixo. [p=0.4] {c}Mas terço e quarto são pedaços "
        "de tamanhos diferentes. [p=0.2] MMC doze: [p=0.2] *sete doze avos.*"),

    # ================= QUESTÃO 5 (EU FAÇO) =================
    dict(id="21", block="q5", text=
        "{t}Agora, questões do nosso material, [p=0.2] no estilo do ENEM. [p=0.2] A primeira é a do começo, "
        "[p=0.2] e eu resolvo com você. [p=0.4] {a}Hoje, a soma das idades de um pai e de seu filho é *cinquenta e dois "
        "anos.* [p=0.2] Daqui a *quatro anos,* [p=0.2] a idade do pai será o *triplo* da idade do filho. [p=0.2] A idade "
        "atual do filho é: [p=0.4] {qa}A: [p=0.2] onze anos. [p=0.3] {qb}B: [p=0.2] treze. [p=0.3] {qc}C: [p=0.2] "
        "catorze. [p=0.3] {qd}D: [p=0.2] quinze. [p=0.3] {qe}E: [p=0.2] quarenta e um anos."),
    dict(id="22", block="q5", text=
        "{t}Etiqueta primeiro: [p=0.2] *f,* a idade do filho *hoje,* em anos. [p=0.4] {a}O pai, hoje: [p=0.2] *cinquenta "
        "e dois menos f.* [p=0.4] {b}Daqui a quatro anos, [p=0.2] os dois ganham quatro: [p=0.2] cinquenta e seis menos "
        "f [p=0.2] igual a três vezes f mais quatro. [p=0.4] {c}Cinquenta e seis menos f [p=0.2] igual a três f mais "
        "doze. [p=0.2] Quarenta e quatro igual a quatro f. [p=0.2] *f igual a onze.* [p=0.4] {d}Conferindo: [p=0.2] o pai "
        "tem quarenta e um. [p=0.2] Daqui a quatro anos, [p=0.2] quarenta e cinco é o triplo de quinze. [p=0.4] {e}A "
        "pergunta é a idade *atual* do filho. [p=0.3] {ok}*Letra A!*"),
    dict(id="23", block="q5", text=
        "{t}E as outras? [p=0.2] Cada uma responde a outra pergunta. [p=0.4] {xb}A B, treze, [p=0.2] *ignora os quatro "
        "anos:* [p=0.2] o triplo *hoje.* [p=0.4] {xc}A C, catorze, [p=0.2] *soma quatro só ao pai.* [p=0.4] {xd}A D, "
        "quinze, [p=0.2] é o filho *daqui a quatro anos.* [p=0.4] {xe}E a E, quarenta e um, [p=0.2] é o *pai.* [p=0.4] "
        "{f}Atalho para conferir: [p=0.2] diferença de trinta, [p=0.2] que no triplo vale dois filhos. [p=0.2] Filho de "
        "quinze no futuro, [p=0.2] onze hoje."),

    # ================= QUESTÃO 3 (NÓS FAZEMOS) =================
    dict(id="24", block="q3", text=
        "{t}A próxima, a gente faz junto. [p=0.3] {a}Uma pessoa gasta *um terço* do seu salário com aluguel [p=0.2] e *um "
        "quarto do salário* com alimentação. [p=0.2] Depois desses dois gastos, [p=0.2] sobram *mil duzentos e cinquenta "
        "reais.* [p=0.2] O salário dessa pessoa é: [p=0.4] {qa}A: [p=0.2] mil setecentos e cinquenta. [p=0.3] {qb}B: "
        "[p=0.2] mil novecentos e setenta e nove e dezessete. [p=0.3] {qc}C: [p=0.2] dois mil cento e quarenta e dois e "
        "oitenta e seis. [p=0.3] {qd}D: [p=0.2] dois mil e quinhentos. [p=0.3] {qe}E: [p=0.2] três mil reais. [p=0.5] "
        "{p}De quem são as frações? [p=0.2] *Pause e tente.* [p=2.0]"),
    dict(id="25", block="q3", text=
        "{t}Etiqueta: [p=0.2] *x,* o salário, em reais. [p=0.4] {a}As duas frações são *do salário.* [p=0.2] Um terço "
        "mais um quarto: [p=0.2] *sete doze avos.* [p=0.4] {b}Sobram *cinco doze avos.* [p=0.2] Cinco doze avos de x "
        "[p=0.2] igual a mil duzentos e cinquenta. [p=0.4] {c}Atalho: [p=0.2] divida por cinco [p=0.2] e multiplique "
        "por doze. [p=0.2] Duzentos e cinquenta, [p=0.2] vezes doze, [p=0.2] *três mil.* [p=0.4] {d}Conferindo: [p=0.2] "
        "mil de aluguel, [p=0.2] setecentos e cinquenta de comida, [p=0.2] sobram mil duzentos e cinquenta. [p=0.3] "
        "{ok}*Letra E!*"),
    dict(id="26", block="q3", text=
        "{t}E as armadilhas? [p=0.4] {xd}A D, dois mil e quinhentos, [p=0.2] calculou a alimentação *do restante.* "
        "[p=0.2] Seria a certa [p=0.2] se o texto dissesse *do que sobrou,* [p=0.2] como na série de Frações. [p=0.2] "
        "Aqui, ele diz *do salário.* [p=0.4] {xa}A A somou as frações e achou *dois sétimos.* [p=0.4] {xc}A C trocou o "
        "que sobrou pelo que foi gasto. [p=0.4] {xb}E a B aplicou as frações aos mil duzentos e cinquenta."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="27", block="q9", text=
        "{t}E a última é sua. [p=0.3] {a}Um tanque contém *quarenta litros* de uma mistura com *vinte e cinco por cento* "
        "de álcool, em volume. [p=0.2] Deseja-se acrescentar álcool puro [p=0.2] para que a concentração passe a ser de "
        "*quarenta por cento.* [p=0.2] A quantidade de álcool puro a acrescentar, em litros, é: [p=0.4] {qa}A: [p=0.2] "
        "seis. [p=0.3] {qb}B: [p=0.2] dez. [p=0.3] {qc}C: [p=0.2] quinze. [p=0.3] {qd}D: [p=0.2] dezesseis. [p=0.3] "
        "{qe}E: [p=0.2] cinquenta. [p=0.5] {p}*Pause e resolva.* [p=2.0]"),
    dict(id="28", block="q9", text=
        "{t}Conferindo. [p=0.2] Etiqueta: [p=0.2] *x,* os litros de álcool puro. [p=0.4] {a}Álcool no tanque: "
        "[p=0.2] vinte e cinco por cento de quarenta, [p=0.2] *dez litros.* [p=0.4] {b}Dez mais x, [p=0.2] sobre quarenta "
        "mais x, [p=0.2] igual a zero vírgula quatro. [p=0.2] Zero vírgula seis x, seis. [p=0.2] *x igual a dez.* "
        "[p=0.4] {c}Pela água: [p=0.2] trinta litros, sessenta por cento. [p=0.2] Total, cinquenta. [p=0.2] Menos "
        "quarenta: [p=0.2] dez. [p=0.4] {d}Vinte de álcool em cinquenta: [p=0.2] quarenta por cento. [p=0.3] {ok}*Letra "
        "B!*"),
    dict(id="29", block="q9", text=
        "{t}E as erradas? [p=0.4] {xa}A A, seis, [p=0.2] *esqueceu que o tanque cresce.* [p=0.4] {xc}A C, quinze, "
        "[p=0.2] dividiu seis por zero vírgula *quatro,* [p=0.2] em vez de zero vírgula seis. [p=0.4] {xd}A D, dezesseis, "
        "[p=0.2] é o álcool que haveria a quarenta por cento [p=0.2] nos quarenta litros de antes. [p=0.4] {xe}E a E, "
        "cinquenta, [p=0.2] é o volume *final.*"),

    # ================= RECAP FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] primeiro a etiqueta do x, com unidade. [p=0.5] "
        "{b}Dois: [p=0.2] o tempo passa para todos. [p=0.5] {c}Três: [p=0.2] achou o x? [p=0.2] Releia a pergunta."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Um forno esfria segundo *T igual a duzentos e vinte menos oito t.* [p=0.3] Quando ele está a, *no máximo,* "
        "sessenta graus? [p=0.5] {b}Quem resolve como equação e esquece um detalhe [p=0.2] responde *no máximo vinte "
        "minutos,* [p=0.2] e erra. [p=0.5] {c}Próximo episódio: [p=0.2] *inequações.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na pegadinha dos quatro anos? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
