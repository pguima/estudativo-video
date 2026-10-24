# Roteiro — Equações e Inequações do 1º Grau, Episódio 3 de 5: inequações, a regra do sinal, intervalos e resposta inteira.
# Base: Estudos/Enem/estudos/01-matematica/20-equacoes-inequacoes-1o-grau.html — seções 06 e 07 + Questões 4, 8 e 7.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Multiplicar por negativo é olhar a reta no ESPELHO: quem estava à esquerda vai para a direita, e o sinal vira.
#   Bolinha aberta é PORTA FECHADA (o extremo não entra); bolinha fechada é PORTA ABERTA (o extremo entra).
#   O INFINITO NUNCA ENTRA: o colchete do lado dele fica sempre aberto.
#   Pessoas e cartazes NÃO VÊM EM PEDAÇOS: n > 800 começa no 801.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Notação de intervalo do material (brasileira): ]2, 5], [−1, +∞[, ]−∞, 3[ — colchete virado para fora = extremo fora.
# Exemplos (prompt e material), todos conferidos em Python:
#   2 < 5 e −2 > −5 · −2x + 7 > 1 → −2x > −6 → x < 3; teste x = 0 (7 > 1, V) e x = 4 (−1 > 1, F)
#   1 < 2x − 3 ≤ 7 → 4 < 2x ≤ 10 → 2 < x ≤ 5 = ]2, 5] (x = 2 fica fora, x = 5 entra) · n > 800 → 801 · n > 342,8 → 343
#   Nossos: x + 2 > 5 → x > 3 (bloco a) · 2 < 5 → 2 + 3 < 5 + 3 e 2·3 < 5·3 (bloco b) · n ≥ 800 → 800 (contraste do bloco f).
# Nós fazemos (prompt): 5 − 3x ≥ −7 → −3x ≥ −12 → x ≤ 4 = ]−∞, 4]; teste x = 0 (5 ≥ −7, V) e x = 5 (−10 ≥ −7, F).
# QUESTÃO 4 (eu faço, texto idêntico): 220 − 8t ≤ 60 → −8t ≤ −160 → t ≥ 20 → C (no mínimo 20 minutos).
#   Erradas (do material e do prompt): B resolve certo e não inverte o sinal; E troca o sinal do 60 (280 ÷ 8 = 35);
#   D calcula quando chegaria a 0 °C (220 ÷ 8 = 27,5), fora até do prazo de 25 min; A divide 60 por 8 (7,5).
#   Teste nosso: t = 25 → 20 °C (serve); t = 10 → 140 °C (não serve).
# QUESTÃO 8 (nós fazemos, texto idêntico): 26 < 6 + 2d ≤ 46 → 20 < 2d ≤ 40 → 10 < d ≤ 20 = ]10, 20] → C.
#   Erradas (do material): A e B erram só os colchetes; D esquece a tarifa fixa (13 < d ≤ 23); E soma 6 (16 < d ≤ 26).
#   Teste nosso: d = 15 → R$ 36,00 (serve); d = 10 → R$ 26,00 (não ganha o cupom).
# QUESTÃO 7 (você faz, texto idêntico): (2 · 4,5 + 3T)/5 ≥ 6 → 9 + 3T ≥ 30 → T ≥ 7 → B.
#   Erradas (do material): C média simples, (4,5 + T)/2 ≥ 6 → 7,5; D esquece o peso da prova, 4,5 + 3T ≥ 30 → 8,5;
#   E divide 21 por 2 → 10,5; A supõe que basta tirar a própria média exigida (6,0 → média 5,4). Conferência nossa: T = 7 → 6,0.
# Acréscimos nossos (verde): o espelho vale só para NEGATIVO (×3 não vira); "teste um de dentro e um de fora";
#   "colchete virado para fora = extremo fora"; "> arredonda para o próximo; ≥ pode ser o próprio".
# Frases-chave (meio e fim, idênticas): 1. Multiplicou ou dividiu por negativo, o sinal vira. 2. Bolinha aberta: o extremo
#   fica de fora. 3. Teste um número de dentro e um de fora.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Inequações do zero: o sinal que vira, os intervalos e a resposta inteira · Matemática ENEM, Equações episódio 3"

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
        "{a}*Dois é menor que cinco.* [p=0.4] {b}Agora multiplique os dois por *menos um:* [p=0.3] {c}*menos dois é MAIOR "
        "que menos cinco.* [p=0.5] {d}Essa virada é a *única regra nova* das inequações, [p=0.2] e é a que *mais "
        "derruba.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai *resolver inequações,* [p=0.2] {b}escrever a resposta como *intervalo* [p=0.2] "
        "{c}e achar o *menor número inteiro* que serve."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] o *roteiro em cinco passos,* [p=0.2] que "
        "sempre termina em *conferir.* [p=0.4] {b}E da série de Operações: [p=0.2] na reta, quanto mais à *direita,* "
        "[p=0.2] *maior* o número. [p=0.2] Menos dois está à direita de menos cinco."),

    # ================= CONCRETO: AS PLACAS =================
    dict(id="04", block="placas", text=
        "{t}Você já obedece inequações [p=0.2] sem saber. [p=0.4] {a}No parque: [p=0.2] *altura mínima de um metro e "
        "quarenta.* [p=0.4] {b}Na fábrica: [p=0.2] retire a peça com *no máximo sessenta graus.* [p=0.4] {c}No "
        "aplicativo: [p=0.2] corrida de *mais de vinte e seis reais* ganha cupom. [p=0.4] {d}Nenhuma placa diz *um* "
        "número. [p=0.2] Todas dizem *uma faixa.*"),
    dict(id="05", block="simbolos", text=
        "{t}E como a matemática escreve essas placas? [p=0.4] {a}Altura *maior ou igual* a um vírgula quarenta. [p=0.4] "
        "{b}Temperatura *menor ou igual* a sessenta. [p=0.4] {c}Preço *maior que* vinte e seis. [p=0.4] {d}Quando o "
        "próprio número *não serve,* [p=0.2] a desigualdade é *estrita:* [p=0.2] sem o tracinho embaixo."),

    # ================= BLOCO A: O QUE MUDA =================
    dict(id="06", block="conjunto", text=
        "{t}E o que muda da equação para a inequação? [p=0.4] {a}*Inequação* é uma conta com *desigualdade* [p=0.2] no "
        "lugar do igual. [p=0.4] {b}x mais dois *igual* a cinco: [p=0.2] *um* número, o três. [p=0.4] {c}x mais dois "
        "*maior que* cinco: [p=0.2] serve quatro, [p=0.2] três e meio, [p=0.2] cem... [p=0.4] {d}A resposta vira o "
        "*conjunto solução:* [p=0.2] todos os números que servem."),

    # ================= BLOCO B: A REGRA DE OURO =================
    dict(id="07", block="regra", text=
        "{t}E dá para resolver como equação? [p=0.4] {a}Quase igual. [p=0.2] Some três nos dois lados de *dois menor "
        "que cinco:* [p=0.2] cinco menor que oito. [p=0.2] *Continua certo.* [p=0.4] {b}Multiplique por *três:* [p=0.2] "
        "seis menor que quinze. [p=0.2] *Continua certo.* [p=0.4] {c}Com número *positivo,* [p=0.2] o sinal *não muda.*"),
    dict(id="08", block="espelho", text=
        "{t}E por *negativo?* [p=0.4] {a}Na reta, o dois está à *esquerda* do cinco. [p=0.4] "
        "{b}Multiplicar por menos um [p=0.2] é olhar a reta *no espelho.* [p=0.3] {c}O dois vira menos dois, [p=0.2] o "
        "cinco vira menos cinco, [p=0.2] e eles *trocam de lado.* [p=0.4] {d}Agora o menos dois está à *direita:* [p=0.2] "
        "*o sinal vira.*"),
    dict(id="09", block="espelho", text=
        "{t}Então guarde a regra de ouro. [p=0.4] {a}Multiplicou ou dividiu os dois lados por um número *negativo:* "
        "[p=0.2] *inverta o sinal.* [p=0.4] {b}Atalho: [p=0.2] o espelho só aparece com o *menos.* [p=0.2] Somar e "
        "subtrair *nunca* viram nada."),

    # ================= BLOCO C: O EXEMPLO =================
    dict(id="10", block="exemplo", text=
        "{t}Vamos usar. [p=0.3] {a}*Menos dois x mais sete, maior que um.* [p=0.4] {b}Tira sete dos dois lados: [p=0.2] "
        "*menos dois x maior que menos seis.* [p=0.4] {c}Agora divida por *menos dois.* "
        "[p=0.3] {v}Pare: [p=0.2] *o sinal vira.* [p=0.3] {d}Menos seis dividido por menos dois, [p=0.2] três. [p=0.2] "
        "*x menor que três.*"),
    dict(id="11", block="teste", text=
        "{t}Como saber se não errei o sinal? [p=0.4] {a}Teste um número *de dentro:* [p=0.2] x igual a zero. [p=0.2] "
        "Menos dois vezes zero, mais sete: [p=0.2] *sete maior que um.* [p=0.2] Verdade. [p=0.4] {b}Agora um *de fora:* "
        "[p=0.2] x igual a quatro. [p=0.2] Menos oito mais sete: [p=0.2] *menos um maior que um?* [p=0.2] Falso. [p=0.4] "
        "{c}Atalho: [p=0.2] o de dentro *passa,* [p=0.2] o de fora *falha.* [p=0.2] Deu o contrário? [p=0.2] O sinal "
        "está errado."),

    # ================= BLOCO D: A RETA E OS INTERVALOS =================
    dict(id="12", block="bolinhas", text=
        "{t}E como desenhar *x menor que três?* [p=0.4] {a}Na reta, [p=0.2] pinte tudo à esquerda do três. [p=0.2] O "
        "número da ponta se chama *extremo.* [p=0.4] {b}E o três serve? [p=0.2] Não. [p=0.2] Ele ganha uma *bolinha "
        "aberta:* [p=0.2] *porta fechada,* [p=0.2] o extremo não entra. [p=0.4] {c}Com *menor ou igual,* [p=0.2] "
        "*bolinha fechada:* [p=0.2] *porta aberta,* [p=0.2] o extremo entra."),
    dict(id="13", block="intervalos", text=
        "{t}E como escrever esse pedaço da reta? [p=0.4] {a}Um *intervalo* é um trecho da reta, [p=0.2] escrito com "
        "colchetes. [p=0.4] {b}Dois menor que x, menor ou igual a cinco: [p=0.2] *aberto no dois, fechado no cinco.* "
        "[p=0.4] {c}x maior ou igual a menos um: [p=0.2] *fechado no menos um,* [p=0.2] até o *infinito.* [p=0.4] "
        "{d}x menor que três: [p=0.2] do *menos infinito* [p=0.2] até três, *aberto.* [p=0.4] {e}E repare: [p=0.2] *o "
        "infinito nunca entra.* [p=0.2] Ele não é um número, [p=0.2] e o colchete do lado dele fica sempre aberto."),
    dict(id="14", block="intervalos", text=
        "{t}E como ler os colchetes sem decorar? [p=0.4] {a}Atalho: [p=0.2] colchete *abraçando* o número, [p=0.2] o "
        "extremo *entra.* [p=0.2] Colchete *virado para fora,* [p=0.2] o extremo *fica de fora.*"),

    # ================= BLOCO E: INEQUAÇÃO DUPLA =================
    dict(id="15", block="dupla", text=
        "{t}E quando a placa tem *dois* limites? [p=0.4] {a}*Um menor que dois x menos três, menor ou igual a sete.* "
        "[p=0.2] Isso é uma *inequação dupla.* [p=0.4] {b}A regra: [p=0.2] a mesma operação [p=0.2] *nas três partes ao "
        "mesmo tempo.* [p=0.4] {c}Some três nas três: [p=0.2] *quatro menor que dois x, menor ou igual a dez.* [p=0.4] "
        "{d}Divida as três por dois: [p=0.2] *dois menor que x, menor ou igual a cinco.* [p=0.4] {e}Aberto no dois, "
        "[p=0.2] fechado no cinco."),

    # ================= BLOCO F: RESPOSTA INTEIRA =================
    dict(id="16", block="inteira", text=
        "{t}E se a resposta forem *pessoas?* [p=0.4] {a}A conta deu *n maior que oitocentos.* [p=0.2] O oitocentos "
        "não serve: [p=0.2] é estrita. [p=0.4] {b}E pessoas *não vêm em "
        "pedaços.* [p=0.2] O menor que serve é *oitocentos e um.* [p=0.4] {c}Deu *n maior que trezentos e "
        "quarenta e dois vírgula oito?* [p=0.2] O menor inteiro é *trezentos e quarenta e três.* [p=0.4] {d}Atalho: "
        "[p=0.2] com *maior que,* pule para o próximo inteiro. [p=0.2] Com *maior ou igual,* [p=0.2] o próprio número "
        "*já serve.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva *cinco menos três x, maior ou igual a menos sete,* [p=0.2] e escreva como "
        "intervalo. [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Tira cinco dos dois lados: [p=0.2] *menos três x maior ou igual a menos doze.* "
        "[p=0.4] {b}Divide por menos três. [p=0.2] {v}*O sinal vira:* [p=0.2] *x menor ou igual a quatro.* [p=0.4] {c}Do "
        "menos infinito até quatro, [p=0.2] *fechado no quatro.* [p=0.4] {d}Teste. [p=0.2] Zero: [p=0.2] cinco maior ou "
        "igual a menos sete, [p=0.2] *verdade.* [p=0.2] Cinco: [p=0.2] menos dez, *falso.* [p=0.2] Confere."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] multiplicou ou dividiu por negativo, o sinal vira. "
        "[p=0.5] {b}Dois: [p=0.2] bolinha aberta: o extremo fica de fora. [p=0.5] {c}Três: [p=0.2] teste um número de "
        "dentro e um de fora."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *menos dois x maior que menos seis* [p=0.2] "
        "virar *x maior que três.* [p=0.4] {b}Parece certo, [p=0.2] porque na equação o sinal de igual nunca muda. "
        "[p=0.4] {c}Mas dividiu por negativo: [p=0.2] o sinal vira. [p=0.2] *x menor que três.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] *n maior que oitocentos* [p=0.2] virar *n igual a oitocentos.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque oitocentos é o número que aparece na conta. [p=0.4] {c}Mas a desigualdade estrita *exclui* o "
        "extremo: [p=0.2] *oitocentos e um.*"),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] *dois menor que x, menor ou igual a cinco* [p=0.2] virar *fechado nos dois lados.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque os dois números são as pontas do mesmo trecho. [p=0.4] {c}Mas cada ponta tem o "
        "seu sinal: [p=0.2] *aberto no dois, fechado no cinco.*"),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="23", block="q4", text=
        "{t}Agora, questões do nosso material. [p=0.2] Esta, eu faço. [p=0.4] {a}Após ser "
        "desligado, [p=0.2] um forno industrial esfria segundo o modelo *T igual a duzentos e vinte menos oito t,* [p=0.2] "
        "em que T é a temperatura, em graus, [p=0.2] e t o tempo, em minutos, [p=0.2] válido nos primeiros vinte e cinco "
        "minutos. [p=0.2] Por segurança, [p=0.2] uma peça só pode ser retirada quando a temperatura for de, [p=0.2] *no "
        "máximo, sessenta graus.* [p=0.2] Para isso, deve-se esperar: [p=0.4] {qa}A: [p=0.2] no máximo sete vírgula cinco "
        "minutos. [p=0.3] {qb}B: [p=0.2] no máximo vinte minutos. [p=0.3] {qc}C: [p=0.2] no mínimo vinte minutos. [p=0.3] "
        "{qd}D: [p=0.2] no mínimo vinte e sete vírgula cinco minutos. [p=0.3] {qe}E: [p=0.2] no mínimo trinta e cinco "
        "minutos."),
    dict(id="24", block="q4", text=
        "{t}Primeiro, traduzir. [p=0.3] {a}*No máximo sessenta:* [p=0.2] T *menor ou igual* a sessenta. [p=0.4] {b}Duzentos "
        "e vinte menos oito t, [p=0.2] menor ou igual a sessenta. [p=0.2] Tira duzentos e vinte: [p=0.2] *menos oito t "
        "menor ou igual a menos cento e sessenta.* [p=0.4] {c}Divide por menos oito. [p=0.2] {v}*O sinal vira:* [p=0.2] "
        "*t maior ou igual a vinte.* [p=0.4] {d}Faz sentido? [p=0.2] O forno *esfria* com o tempo, [p=0.2] então é "
        "preciso *esperar.* [p=0.2] Vinte e cinco minutos: [p=0.2] vinte graus, serve. [p=0.3] {ok}*Letra C:* [p=0.2] no mínimo vinte minutos!"),
    dict(id="25", block="q4", text=
        "{t}E as erradas? [p=0.3] {xb}A B fez a conta certa [p=0.2] e *não inverteu o sinal.* [p=0.4] {xe}A E trocou o "
        "sinal do sessenta: [p=0.2] duzentos e oitenta dividido por oito. [p=0.4] {xd}A D calculou quando o forno chegaria "
        "a *zero grau:* [p=0.2] duzentos e vinte dividido por oito, [p=0.2] fora até do prazo do modelo. [p=0.4] {xa}E a A "
        "dividiu sessenta por oito, [p=0.2] sem montar a inequação."),

    # ================= QUESTÃO 8 (NÓS FAZEMOS) =================
    dict(id="26", block="q8", text=
        "{t}Esta, nós fazemos juntos. [p=0.4] {a}Um aplicativo cobra, por corrida, [p=0.2] *C igual a seis mais dois d* "
        "reais, [p=0.2] em que d é a distância em quilômetros. [p=0.2] Um passageiro só ganha um cupom [p=0.2] se a "
        "corrida custar *mais de vinte e seis reais,* [p=0.2] e ele tem *quarenta e seis reais* disponíveis para pagá-la. "
        "[p=0.2] As distâncias d que lhe permitem ganhar o cupom e pagar a corrida [p=0.2] formam o intervalo: [p=0.4] "
        "{qa}A: [p=0.2] fechado de dez a vinte. [p=0.3] {qb}B: [p=0.2] aberto de dez a vinte. [p=0.3] {qc}C: [p=0.2] "
        "aberto no dez, fechado no vinte. [p=0.3] {qd}D: [p=0.2] aberto no treze, fechado no vinte e três. [p=0.3] {qe}E: "
        "[p=0.2] aberto no dezesseis, fechado no vinte e seis. [p=0.4] {p}*Pause e traduza as duas placas.* [p=2.0]"),
    dict(id="27", block="q8", text=
        "{t}Vamos juntos. [p=0.3] {a}*Mais de vinte e seis:* [p=0.2] estrito. [p=0.2] *Tem quarenta e seis:* [p=0.2] "
        "pode custar exatamente quarenta e seis. [p=0.4] {b}Vinte e seis *menor que* seis mais dois d, [p=0.2] *menor ou "
        "igual* a quarenta e seis. [p=0.4] {c}Tira seis nas três partes: [p=0.2] *vinte menor que dois d, menor ou igual "
        "a quarenta.* [p=0.4] {d}Divide as três por dois: [p=0.2] *dez menor que d, menor ou igual a vinte.* [p=0.4] "
        "{e}Teste: [p=0.2] quinze quilômetros, [p=0.2] trinta e seis reais, serve. [p=0.3] {ok}*Letra C!*"),
    dict(id="28", block="q8", text=
        "{t}E as erradas? [p=0.3] {xa}A A e a B [p=0.2] {xb}erraram só os colchetes, [p=0.2] tratando as duas pontas do "
        "mesmo jeito. [p=0.4] {xd}A D esqueceu a tarifa fixa de seis reais. [p=0.4] {xe}E a E *somou* seis, [p=0.2] em "
        "vez de subtrair."),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="29", block="q7", text=
        "{t}E esta, [p=0.2] *você faz.* [p=0.4] {a}Em uma disciplina, [p=0.2] a média final é calculada com *peso dois "
        "para a prova* e *peso três para o trabalho.* [p=0.2] Para ser aprovado, [p=0.2] o aluno precisa de média final "
        "*igual ou superior a seis.* [p=0.2] Um aluno tirou *quatro e meio* na prova. [p=0.2] A menor nota que ele precisa "
        "tirar no trabalho para ser aprovado é: [p=0.4] {qa}A: [p=0.2] seis. [p=0.3] {qb}B: [p=0.2] sete. [p=0.3] {qc}C: "
        "[p=0.2] sete e meio. [p=0.3] {qd}D: [p=0.2] oito e meio. [p=0.3] {qe}E: [p=0.2] dez e meio. [p=0.4] {f}Lembrete: "
        "[p=0.2] média com pesos é cada nota vezes o seu peso, [p=0.2] somadas, [p=0.2] divididas pela soma dos pesos. "
        "[p=0.4] {p}*Pause e resolva.* [p=2.5]"),
    dict(id="30", block="q7", text=
        "{t}Conferindo. [p=0.3] {a}*Igual ou superior a seis:* [p=0.2] maior ou igual. [p=0.4] {b}Dois vezes quatro e "
        "meio, mais três T, [p=0.2] tudo sobre cinco, [p=0.2] maior ou igual a seis. [p=0.4] {c}Multiplica por cinco, "
        "que é positivo, [p=0.2] e o sinal fica: [p=0.2] *nove mais três T maior ou igual a trinta.* [p=0.4] {d}Três T maior "
        "ou igual a vinte e um: [p=0.2] *T maior ou igual a sete.* [p=0.4] {e}Teste: [p=0.2] com sete, [p=0.2] nove mais "
        "vinte e um, trinta, [p=0.2] sobre cinco, *seis.* [p=0.2] Passa raspando. [p=0.3] {ok}*Letra B!*"),
    dict(id="31", block="q7", text=
        "{t}E as erradas? [p=0.3] {xc}A C usou *média simples,* [p=0.2] sem os pesos. [p=0.4] {xd}A D esqueceu o peso da "
        "prova. [p=0.4] {xe}A E dividiu vinte e um por *dois,* [p=0.2] em vez de por três. [p=0.4] {xa}E a A achou que "
        "bastava tirar seis: [p=0.2] a média ficaria em cinco vírgula quatro."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] multiplicou ou dividiu por negativo, o sinal vira. "
        "[p=0.5] {b}Dois: [p=0.2] bolinha aberta: o extremo fica de fora. [p=0.5] {c}Três: [p=0.2] teste um número de "
        "dentro e um de fora."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}Locadora A: [p=0.2] *noventa reais* por dia [p=0.2] mais *cinquenta centavos* por quilômetro. [p=0.4] "
        "{b}Locadora B: [p=0.2] *sessenta reais* [p=0.2] mais *oitenta centavos* por quilômetro. [p=0.4] {c}Qual "
        "compensa? [p=0.3] Depende de quanto você vai rodar. [p=0.5] {d}Próximo episódio: [p=0.2] *o ponto de "
        "equilíbrio.*"),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha esquecido de virar o sinal? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
