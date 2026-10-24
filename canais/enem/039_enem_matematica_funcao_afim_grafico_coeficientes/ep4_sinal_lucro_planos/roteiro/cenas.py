# Roteiro — Função Afim, Episódio 4 de 5: estudo do sinal, custo, receita, lucro e comparação de planos
# Base: Estudos/Enem/estudos/01-matematica/24-funcao-afim-grafico-coeficientes.html — seção 07 e o trecho
#   "Os três modelos de uma pequena empresa" (com o gráfico do ponto de equilíbrio) da seção 08 + Questões 4 e 7 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O SINAL: depois do zero, a função tem o sinal de a; antes do zero, o sinal contrário.
#   O EMPATE: o ponto de equilíbrio é o empate; lucro zero não é lucro.
#   A CORRIDA DE DOIS PLANOS: quem tem a bandeirada menor larga na frente; quem tem o km mais barato ganha no fim.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida (série de Equações e inequações do 1º grau): inequação, ponto de equilíbrio, n > 800 → 801 e o atalho da
#   diferença. O novo aqui: ler o equilíbrio como CRUZAMENTO de retas e o lucro como ESTUDO DO SINAL.
# Bloco d = exemplo da seção 08 (fixo R$ 2.000,00, R$ 15,00 por peça, venda a R$ 25,00 → L = 10x − 2 000, empate em 200
#   peças com R$ 5.000,00 de custo e de receita).
# Exemplos NOSSOS (marcados), para não entregar a Questão 7 ("você faz"):
#   bloco f e erro 3 usam dois aplicativos: A = 4 + 3x e B = 10 + 2x (empate em 6 km, os dois a R$ 22,00);
#   erro 3: somar as bandeiradas dá (4 + 10) ÷ 1 = 14 km, errado.
#   Erros 1 e 2 usam o exemplo da seção 08 (200 peças; 2 000 ÷ 25 = 80 peças dá prejuízo de R$ 1.200,00), não a Q4.
# Acréscimos NOSSOS (marcados): atalho verde "ache o zero, olhe o a" (cena 07); atalho verde "fixo ÷ o que sobra de cada
#   unidade" (cena 12: 2 000 ÷ (25 − 15) = 200); teste de um valor de cada lado do equilíbrio em todas as questões.
# Nós fazemos (prompt): doceira, L(x) = 10x − (600 + 4x) = 6x − 600 → empate em 100 → lucro a partir de 101 bolos.
# QUESTÃO 4 ("eu faço", com pausa): gabarito E (601). Erradas = material (D é o equilíbrio 600; B = 12 000 ÷ 50 = 240;
#   C = 12 000 ÷ 30 = 400; A = 12 000 ÷ (50 + 30) = 150). Testes: L(600) = 0; L(601) = 20.
# QUESTÃO 7 ("você faz", com pausa): gabarito B (5 km). Lei de B por dois pontos: a = (28 − 8) ÷ 10 = 2, b = 8.
#   6 + 2,4x > 8 + 2x → 0,4x > 2 → x > 5. Testes: 4 km (A 15,60 · B 16,00) e 6 km (A 20,40 · B 20,00).
#   Erradas = material (A = 8 − 6 = 2 sem dividir; E = 14 ÷ 0,4 = 35; D = 8 ÷ 0,4 = 20; C = 6 ÷ 0,4 = 15).
# Frases-chave (meio e fim, idênticas): 1. Depois do zero, a função tem o sinal de a.
#   2. Lucro é receita menos custo, com o custo entre parênteses. 3. No equilíbrio o lucro é zero: com unidades inteiras, some 1.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Lucro, prejuízo e ponto de equilíbrio: estudo do sinal · Matemática ENEM, Função afim episódio 4"

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
        "{a}Uma confecção precisa vender *seiscentas camisetas* para empatar. [p=0.5] {b}Qual é o número mínimo de "
        "camisetas para ter *lucro?* [p=0.5] {c}Seiscentos está nas alternativas, [p=0.2] *e está errado.* [p=0.5] "
        "{d}A resposta é *seiscentos e um.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o quarto episódio da série de *Função afim.* [p=0.4] {a}Ao final, [p=0.2] você vai dizer onde uma "
        "função afim é *positiva ou negativa,* [p=0.3] {b}montar *custo, receita e lucro* [p=0.3] {c}e decidir *a partir "
        "de quando* um plano compensa."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Equações e Inequações: [p=0.2] uma *inequação* se resolve "
        "como uma equação, [p=0.2] e o *ponto de equilíbrio* é onde dois valores empatam. [p=0.4] {b}Da mesma série: "
        "[p=0.2] se n tem que ser *maior que oitocentos,* [p=0.2] o menor inteiro é *oitocentos e um.* [p=0.4] {c}E do "
        "episódio três: [p=0.2] com *dois pontos,* [p=0.2] a taxa é a variação do y [p=0.2] dividida pela variação do x."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine uma pequena *fábrica de peças.* [p=0.4] {a}Todo mês ela paga o *aluguel* e as *máquinas,* [p=0.2] "
        "vendendo ou não. [p=0.4] {b}Cada peça gasta um pouco de *material.* [p=0.4] {c}E cada peça é vendida por um "
        "*preço.* [p=0.4] {d}E pense em *dois aplicativos de transporte,* [p=0.2] cada um com a sua bandeirada [p=0.2] "
        "e o seu preço por quilômetro. [p=0.3] Hoje, os dois viram *retas.*"),

    # ================= BLOCO A: ESTUDO DO SINAL =================
    dict(id="05", block="sinal", text=
        "{t}Onde uma função é *positiva?* [p=0.4] {a}Fazer o *estudo do sinal* [p=0.2] é descobrir para quais valores de "
        "x [p=0.2] o resultado dá *positivo,* [p=0.2] *negativo* [p=0.2] ou *zero.* [p=0.4] {b}Pegue *dois x menos "
        "seis.* [p=0.3] O zero é onde ela vale zero: [p=0.2] dois x igual a seis, [p=0.2] *x igual a três.* [p=0.4] "
        "{c}Antes do três, [p=0.2] teste o zero: [p=0.2] menos seis. [p=0.2] *Negativa.* [p=0.4] {d}Depois do três, "
        "[p=0.2] teste o cinco: [p=0.2] dez menos seis, [p=0.2] quatro. [p=0.2] *Positiva.*"),
    dict(id="06", block="sinal", text=
        "{t}E se o a for negativo? [p=0.4] {a}Pegue *menos x mais quatro.* [p=0.3] O zero é *x igual a quatro.* [p=0.4] "
        "{b}Antes do quatro, [p=0.2] teste o zero: [p=0.2] *mais quatro.* [p=0.2] Positiva. [p=0.4] {c}Depois do "
        "quatro, [p=0.2] teste o seis: [p=0.2] menos seis mais quatro, [p=0.2] *menos dois.* [p=0.2] Negativa. [p=0.4] "
        "{d}Ficou ao contrário da primeira. [p=0.2] Por quê?"),
    dict(id="07", block="regra", text=
        "{t}Porque quem manda é o *a.* [p=0.4] {a}Regra para guardar: [p=0.2] *depois do zero, [p=0.2] a função tem o "
        "sinal de a; [p=0.2] antes do zero, [p=0.2] o sinal contrário.* [p=0.4] {b}Dois x menos seis: [p=0.2] a é "
        "positivo, [p=0.2] depois do três é positiva. [p=0.3] Menos x mais quatro: [p=0.2] a é negativo, [p=0.2] depois "
        "do quatro é negativa. [p=0.4] {c}Atalho: [p=0.2] *ache o zero, [p=0.2] olhe o a.* [p=0.2] Sem tabela, sem "
        "conta."),

    # ================= BLOCO C: OS TRÊS MODELOS =================
    dict(id="08", block="modelos", text=
        "{t}Como a fábrica vira função? [p=0.4] {a}O *custo fixo* é o que se paga mesmo sem produzir nada: [p=0.2] "
        "aluguel, máquinas. [p=0.4] {b}O *custo variável* cresce com cada peça: [p=0.2] o custo de uma peça, [p=0.2] "
        "vezes o número de peças. [p=0.4] {c}Juntos: [p=0.2] *C de x igual ao fixo, [p=0.2] mais c vezes x.* [p=0.3] "
        "Uma função afim. [p=0.4] {d}A *receita* é o dinheiro que entra das vendas: [p=0.2] *R de x igual a p vezes "
        "x,* [p=0.2] o preço vezes as peças. [p=0.2] Uma reta que sai da origem."),
    dict(id="09", block="modelos", text=
        "{t}E o lucro? [p=0.4] {a}O *lucro* é o que sobra: [p=0.2] *receita menos custo.* [p=0.4] {b}E aqui mora um "
        "detalhe: [p=0.2] escreva o custo *entre parênteses.* [p=0.2] *L de x igual a R de x, [p=0.2] menos, [p=0.2] "
        "abre parênteses, [p=0.2] fixo mais c x.* [p=0.4] {c}O menos vale para o custo *inteiro.* [p=0.4] {d}E quando o "
        "lucro dá negativo, [p=0.2] ele tem outro nome: [p=0.2] *prejuízo.*"),

    # ================= BLOCO D: O EXEMPLO DO MATERIAL =================
    dict(id="10", block="exemplo", text=
        "{t}Vamos com números. [p=0.4] {a}Custo fixo de *dois mil reais.* [p=0.2] *Quinze reais* para fazer cada peça. "
        "[p=0.2] Venda a *vinte e cinco.* [p=0.4] {b}Lucro: [p=0.2] vinte e cinco x, [p=0.2] menos, [p=0.2] entre "
        "parênteses, [p=0.2] dois mil mais quinze x. [p=0.4] {c}Abre os parênteses: [p=0.2] *dez x menos dois mil.* "
        "[p=0.4] {d}O *ponto de equilíbrio* é a quantidade em que o lucro é *zero:* [p=0.2] nem ganha, [p=0.2] nem "
        "perde. [p=0.2] Dez x igual a dois mil: [p=0.2] *duzentas peças.*"),
    dict(id="11", block="grafico", text=
        "{t}E no gráfico, [p=0.2] o que é esse empate? [p=0.4] {a}A *receita* sai da origem: [p=0.2] sem vendas, "
        "[p=0.2] sem dinheiro. [p=0.4] {b}O *custo* sai de *dois mil:* [p=0.2] o aluguel já está lá. [p=0.4] {c}As duas "
        "retas se *cruzam* em duzentas peças, [p=0.2] com *cinco mil reais* de custo e de receita. [p=0.4] {d}Antes do "
        "cruzamento, [p=0.2] o custo fica em cima: [p=0.2] *prejuízo.* [p=0.3] Depois, [p=0.2] a receita fica em cima: "
        "[p=0.2] *lucro.* [p=0.3] {e}E cada peça a mais rende *dez reais.*"),
    dict(id="12", block="margem", text=
        "{t}Dá para achar o empate mais rápido? [p=0.4] {a}Atalho: [p=0.2] *o fixo, [p=0.2] dividido pelo que sobra de "
        "cada unidade.* [p=0.4] {b}De cada peça sobram vinte e cinco menos quinze, [p=0.2] *dez reais.* [p=0.3] Esses "
        "dez vão pagando o aluguel. [p=0.4] {c}Dois mil dividido por dez: [p=0.2] *duzentas peças.* [p=0.2] Mesma "
        "resposta, [p=0.2] em uma linha."),

    # ================= BLOCO E: LUCRO É ESTUDO DO SINAL =================
    dict(id="13", block="lucrosinal", text=
        "{t}E a partir de quantas peças há lucro? [p=0.4] {a}Lucro positivo [p=0.2] é *L de x maior que zero.* [p=0.2] "
        "Isso é estudo do sinal! [p=0.4] {b}O zero é duzentos. [p=0.2] O a é dez, [p=0.2] positivo. [p=0.2] Depois do "
        "duzentos, [p=0.2] *lucro.* [p=0.4] {c}Repare no sinal: [p=0.2] *maior que,* [p=0.2] sem o igual. [p=0.2] Isso "
        "é uma *desigualdade estrita:* [p=0.2] o próprio duzentos não serve. [p=0.4] {d}Com duzentas peças, [p=0.2] o "
        "lucro é zero. [p=0.2] E *lucro zero não é lucro.* [p=0.3] A resposta é *duzentas e uma.*"),

    # ================= BLOCO F: A CORRIDA DE DOIS PLANOS =================
    dict(id="14", block="corrida", text=
        "{t}E os dois aplicativos? [p=0.4] {a}O A cobra *quatro reais* de bandeirada, [p=0.2] mais *três* por "
        "quilômetro. [p=0.4] {b}O B cobra *dez* de bandeirada, [p=0.2] mais *dois* por quilômetro. [p=0.4] {c}Pense numa "
        "*corrida:* [p=0.2] quem tem a bandeirada menor *larga na frente;* [p=0.2] quem tem o quilômetro mais barato "
        "*ganha no fim.* [p=0.4] {d}As duas retas se cruzam [p=0.2] em algum quilômetro. [p=0.2] Onde?"),
    dict(id="15", block="corrida", text=
        "{t}Pela série de Equações, [p=0.2] você já sabe o atalho. [p=0.4] {a}Atalho da diferença: [p=0.2] a diferença "
        "das bandeiradas, [p=0.2] *dez menos quatro,* [p=0.2] seis, [p=0.2] dividida pela diferença por quilômetro, "
        "[p=0.2] *três menos dois,* [p=0.2] um. [p=0.2] *Seis quilômetros.* [p=0.4] {b}Conferindo: [p=0.2] o A dá "
        "vinte e dois, [p=0.2] o B dá vinte e dois. [p=0.2] Empate. [p=0.4] {c}E o novo: [p=0.2] o A fica *mais caro* "
        "quando A menos B é *positivo.* [p=0.2] *x menos seis maior que zero.* [p=0.2] Estudo do sinal de novo. [p=0.4] "
        "{d}Até seis quilômetros, [p=0.2] o A compensa. [p=0.2] Depois, [p=0.2] o B."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma doceira tem custo fixo de *seiscentos reais* por mês, [p=0.2] gasta *quatro reais* "
        "por bolo [p=0.2] e vende cada um a *dez reais.* [p=0.4] {b}A partir de quantos bolos [p=0.2] ela tem *lucro?* "
        "[p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Lucro: [p=0.2] dez x, [p=0.2] menos, [p=0.2] entre parênteses, [p=0.2] seiscentos "
        "mais quatro x. [p=0.2] Dá *seis x menos seiscentos.* [p=0.4] {b}Empate: [p=0.2] seis x igual a seiscentos, "
        "[p=0.2] *cem bolos.* [p=0.4] {c}O a é seis, [p=0.2] positivo: [p=0.2] depois do cem, lucro. [p=0.3] Com cem "
        "bolos, [p=0.2] lucro zero. [p=0.2] Com cento e um, [p=0.2] *seis reais.* [p=0.4] {d}Resposta: [p=0.2] *a partir "
        "de cento e um bolos.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] depois do zero, [p=0.2] a função tem o sinal de a. "
        "[p=0.5] {b}Dois: [p=0.2] lucro é receita menos custo, [p=0.2] com o custo entre parênteses. [p=0.5] {c}Três: "
        "[p=0.2] no equilíbrio o lucro é zero: [p=0.2] com unidades inteiras, [p=0.2] some um."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] responder o *ponto de equilíbrio* [p=0.2] como "
        "a primeira quantidade com lucro. [p=0.2] Duzentas peças. [p=0.4] {b}Parece certo, [p=0.2] porque a conta que "
        "você acabou de fazer [p=0.2] deu exatamente esse número. [p=0.4] {c}Mas em duzentas o lucro é zero. [p=0.2] "
        "Lucro começa em *duzentas e uma.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] dividir o custo fixo [p=0.2] pelo *preço de venda.* [p=0.2] Dois mil dividido por vinte e "
        "cinco, [p=0.2] oitenta peças. [p=0.4] {b}Parece certo, [p=0.2] porque cada venda ajuda a pagar o aluguel. "
        "[p=0.4] {c}Mas cada peça *custa quinze* para fazer. [p=0.2] Só sobram dez. [p=0.2] Com oitenta peças, [p=0.2] "
        "o prejuízo é de *mil e duzentos.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] *somar* as bandeiradas ao comparar planos. [p=0.2] Quatro mais dez, [p=0.2] catorze, "
        "[p=0.2] dividido por um: [p=0.2] catorze quilômetros. [p=0.4] {b}Parece certo, [p=0.2] porque as duas "
        "bandeiradas entram na conta. [p=0.4] {c}Mas o que importa é *quanto um larga na frente do outro:* [p=0.2] a "
        "*diferença.* [p=0.2] Dez menos quatro, [p=0.2] seis quilômetros."),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="22", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Uma confecção "
        "tem custo fixo mensal de *doze mil reais* [p=0.2] e gasta *trinta reais* para produzir cada camiseta, [p=0.2] "
        "vendida a *cinquenta.* [p=0.3] O número mínimo de camisetas para ter lucro é: [p=0.3] {qa}A: [p=0.2] cento e "
        "cinquenta. [p=0.2] {qb}B: [p=0.2] duzentos e quarenta. [p=0.2] {qc}C: [p=0.2] quatrocentos. [p=0.2] {qd}D: "
        "[p=0.2] seiscentos. [p=0.2] {qe}E: [p=0.2] seiscentos e um. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q4", text=
        "{t}Pergunta: [p=0.2] a partir de quando há *lucro.* [p=0.2] Estudo do sinal. [p=0.4] {a}Lucro: [p=0.2] "
        "cinquenta x, [p=0.2] menos, [p=0.2] entre parênteses, [p=0.2] doze mil mais trinta x. [p=0.2] Dá *vinte x "
        "menos doze mil.* [p=0.4] {b}Lucro maior que zero: [p=0.2] vinte x maior que doze mil, [p=0.2] *x maior que "
        "seiscentos.* [p=0.4] {c}Testando: [p=0.2] seiscentas camisetas, [p=0.2] lucro *zero.* [p=0.2] Seiscentas e "
        "uma, [p=0.2] lucro de *vinte reais.* [p=0.3] {ok}*Letra E!*"),
    dict(id="24", block="q4", text=
        "{t}E as armadilhas? [p=0.3] {xd}A D é o *ponto de equilíbrio:* [p=0.2] nem lucro, [p=0.2] nem prejuízo. "
        "[p=0.4] {xb}A B divide doze mil pelo preço de venda, [p=0.2] esquecendo o custo de cada camiseta. [p=0.4] "
        "{xc}A C divide pelo custo de cada uma. [p=0.4] {xa}E a A divide pela *soma,* [p=0.2] cinquenta mais trinta."),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="25", block="q7", text=
        "{t}E esta é *sua.* [p=0.3] {a}A empresa *A* cobra *seis reais* fixos [p=0.2] mais *dois e quarenta* por "
        "quilômetro. [p=0.3] Na empresa *B,* [p=0.2] o preço também é afim: [p=0.2] uma corrida de *zero quilômetro* "
        "custa *oito reais,* [p=0.2] e uma de *dez quilômetros* custa *vinte e oito.* [p=0.3] A empresa A passa a ser "
        "mais cara que a B [p=0.2] para corridas com mais de: [p=0.3] {qa}A: [p=0.2] dois quilômetros. [p=0.2] {qb}B: "
        "[p=0.2] cinco. [p=0.2] {qc}C: [p=0.2] quinze. [p=0.2] {qd}D: [p=0.2] vinte. [p=0.2] {qe}E: [p=0.2] trinta e "
        "cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q7", text=
        "{t}Conferindo. [p=0.3] {a}Primeiro, [p=0.2] a lei da B, [p=0.2] pelos dois pontos. [p=0.2] De zero a dez "
        "quilômetros, [p=0.2] o preço foi de oito a vinte e oito: [p=0.2] *vinte a mais em dez quilômetros,* [p=0.2] "
        "*dois reais* por quilômetro. [p=0.2] Bandeirada: [p=0.2] *oito.* [p=0.4] {b}A mais cara que B: [p=0.2] seis "
        "mais dois e quarenta x, [p=0.2] maior que oito mais dois x. [p=0.3] Zero vírgula quatro x maior que dois: "
        "[p=0.2] *x maior que cinco.* [p=0.4] {c}Testando: [p=0.2] com quatro quilômetros, [p=0.2] o A ainda é mais "
        "barato. [p=0.2] Com seis, [p=0.2] o A já é mais caro. [p=0.3] {ok}*Letra B!*"),
    dict(id="27", block="q7", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A é a diferença das bandeiradas [p=0.2] *sem dividir* pela diferença por "
        "quilômetro. [p=0.4] {xe}A E *soma* as bandeiradas: [p=0.2] catorze dividido por zero vírgula quatro. [p=0.4] "
        "{xd}A D [p=0.2] {xc}e a C [p=0.2] dividem por zero vírgula quatro [p=0.2] a bandeirada de *uma empresa só:* "
        "[p=0.2] oito, [p=0.2] e seis."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] depois do zero, [p=0.2] a função tem o sinal de "
        "a. [p=0.5] {b}Dois: [p=0.2] lucro é receita menos custo, [p=0.2] com o custo entre parênteses. [p=0.5] "
        "{c}Três: [p=0.2] no equilíbrio o lucro é zero: [p=0.2] com unidades inteiras, [p=0.2] some um."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}vemos a função afim escondida na "
        "*Física,* [p=0.2] na *termometria,* [p=0.2] nos *juros simples* [p=0.2] e nas *progressões* [p=0.3] {c}e "
        "caçamos as *pegadinhas.*"),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] que negócio você abriria, [p=0.2] e quantas unidades precisaria "
        "vender para empatar? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você "
        "adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em "
        "poucos minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
