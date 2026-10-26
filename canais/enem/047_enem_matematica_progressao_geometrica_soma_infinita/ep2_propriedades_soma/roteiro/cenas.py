# Roteiro — Progressão Geométrica, Episódio 2 de 5: propriedades que poupam conta e a soma finita da PG
# Base: Estudos/Enem/estudos/01-matematica/32-progressao-geometrica-soma-infinita.html — seções 05 e 06 + Questões 4 e 5
#   (seção 12). A soma infinita fica para o episódio 3.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A PG É A PA COM A SOMA TROCADA POR MULTIPLICAÇÃO: média vira média geométrica; soma dos equidistantes vira produto.
#   x/q, x e x·q: no produto, o q se cancela e some.
#   MULTIPLICAR A SOMA POR q EMPURRA TODAS AS PARCELAS UM DEGRAU; subtraindo, sobra só a última menos a primeira.
#   (do ep. 1: a PG é uma MÁQUINA DE MULTIPLICAR ×q.)
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Blocos e (corrente: 1 092; só no 6º dia, 729) = mesmos números da Questão 4, que é "eu faço" (repetição pedida no prompt);
#   na Q4 o foco são as alternativas erradas.
# DESVIO do prompt (bloco b): o prompt usa "produto 216 → x = 6", que é o primeiro passo da Questão 5 ("você faz", com
#   pausa). O bloco usa produto 64 → x = 4 (cubo de 4). O 216 só aparece na Q5.
# DESVIO do prompt (bloco c): os equidistantes usam a PG (1, 2, 4, 8, 16, 32) — produto 32 em todos os pares — lado a lado
#   com a PA (1, 3, 5, 7, 9, 11) — soma 12. Não usa a PG do "nós fazemos" (2, 6, …, 486), para não mostrar antes o último termo.
# Nós fazemos (prompt): 2 + 6 + 18 + … com 6 termos, q = 3: S₆ = 2 · (3⁶ − 1)/2 = 728; conferência 2 + 6 + 18 + 54 + 162 + 486 = 728.
# Erros clássicos: erro 1 com a corrente (total = 3⁶ = 729, que é só o 6º dia; pedido no prompt); erros 2 e 3 com os números
#   do "nós fazemos" (já resolvido): sem ÷ (q − 1) → 1 456; fórmula da PA (2 + 486) · 6 ÷ 2 → 1 464. Nada da Q5.
# QUESTÃO 4 ("eu faço"): gabarito C (1 092). Erradas = material (A 18 = 3 por dia durante 6 dias, linear; B 729 = só o 6º dia;
#   D 2 184 = 3 · 728 sem dividir por q − 1 = 2; E 2 187 = 3⁷, quem receberia no 7º dia).
# QUESTÃO 5 ("você faz", com pausa): gabarito C (9). x/q, x, x·q: x³ = 216 → x = 6; 6/q + 6 + 6q = 19 → 6q² − 13q + 6 = 0;
#   Δ = 169 − 144 = 25; q = (13 ± 5)/12 = 3/2 ou 2/3; crescente → 3/2; idades 4, 6, 9 (soma 19, produto 216).
#   Erradas = material (A 4 é o mais novo; B 6 é o do meio, que sai direto do produto; D 12 supõe razão 2 sem usar a soma:
#   3, 6, 12 somam 21; E 13 = 19 − 6, subtrai a idade do meio da soma).
# Acréscimos NOSSOS (marcados): atalho verde "raiz cúbica do produto" (cena 07); atalho verde "próximo termo menos o
#   primeiro, dividido por q − 1" (cena 11: (2 187 − 3)/2 = 1 092; no tabuleiro, 2⁶⁴ − 1; no nós fazemos, (1 458 − 2)/2 = 728);
#   atalho verde "termo ou soma? liste os primeiros termos" (cena 13). Bhaskara relembrada em uma frase (cena 03) e na Q5.
# Frases-chave (meio e fim, idênticas): 1. Na PG, o termo do meio ao quadrado é o produto dos vizinhos.
#   2. Três em PG: x/q, x e x·q. 3. Soma finita: a₁ vezes (qⁿ − 1), dividido por (q − 1).
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Soma da PG e as propriedades que poupam conta | PG Ep. 2"
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
        "{a}Um grão de trigo na *primeira casa* do xadrez, [p=0.2] dois na segunda, [p=0.2] quatro na terceira… [p=0.5] "
        "{b}Na *sexagésima quarta casa,* [p=0.2] a soma passa de *dezoito quintilhões* de grãos: [p=0.3] {c}centenas de "
        "vezes a produção mundial de trigo de um ano. [p=0.5] {d}E a fórmula que faz essa conta [p=0.2] *cabe numa linha.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o segundo episódio da série de *Progressão geométrica.* [p=0.4] {a}Ao final, [p=0.2] você vai *somar "
        "qualquer PG finita* [p=0.3] {b}e resolver problemas de *três números em PG* [p=0.2] em poucas linhas."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] a PG é uma *máquina de multiplicar.* [p=0.2] O "
        "termo de posição n [p=0.2] é o primeiro [p=0.2] vezes *q elevado a n menos um.* [p=0.4] {b}Da série de "
        "Progressão aritmética: [p=0.2] três números em PA [p=0.2] se escrevem *x menos r, x, x mais r.* [p=0.4] "
        "{c}E da série de Equação do segundo grau: [p=0.2] *Bhaskara* acha as raízes [p=0.2] de qualquer equação com x ao "
        "quadrado. [p=0.3] Só isso."),

    # ================= BLOCO A: MÉDIA GEOMÉTRICA =================
    dict(id="04", block="media", text=
        "{t}Na PA, o termo do meio é a *média* dos vizinhos. [p=0.3] E na PG? [p=0.4] {a}Pense assim: [p=0.2] *a PG é a "
        "PA com a soma trocada por multiplicação.* [p=0.4] {b}Na PA, você *soma* os vizinhos e divide por dois. [p=0.3] "
        "{c}Na PG, você *multiplica* os vizinhos. [p=0.3] O termo do meio, *ao quadrado,* [p=0.2] dá esse produto. "
        "[p=0.4] {d}Isso tem nome: [p=0.2] *média geométrica.* [p=0.2] É o número que, ao quadrado, [p=0.2] dá o produto "
        "dos dois vizinhos."),
    dict(id="05", block="media", text=
        "{t}Vamos testar. [p=0.3] {a}*Quatro, x, vinte e cinco* [p=0.2] estão em PG, com termos positivos. [p=0.2] Quanto "
        "vale x? [p=0.4] {b}x ao quadrado [p=0.2] é quatro vezes vinte e cinco: [p=0.2] *cem.* [p=0.3] {c}x é *dez.* "
        "[p=0.4] {d}Confira na máquina: [p=0.2] quatro vezes dois e meio, [p=0.2] dez. [p=0.2] Dez vezes dois e meio, "
        "[p=0.2] *vinte e cinco.* [p=0.2] A mesma razão."),

    # ================= BLOCO B: NOTAÇÃO SIMÉTRICA =================
    dict(id="06", block="simetrica", text=
        "{t}E quando o problema dá o *produto* de três números em PG? [p=0.4] {a}Na PA, você chamava de x menos r, x, x "
        "mais r. [p=0.3] {b}Na PG, troque por divisão e multiplicação: [p=0.2] *x sobre q, x, x vezes q.* [p=0.4] {c}Isso "
        "se chama *notação simétrica:* [p=0.2] o x no centro, [p=0.2] e a razão saindo igual para os dois lados."),
    dict(id="07", block="simetrica", text=
        "{t}E por que isso ajuda? [p=0.4] {a}Multiplique os três. [p=0.2] O *q* de cima cancela o *q* de baixo. [p=0.3] "
        "{b}*O q some.* [p=0.2] Sobra x vezes x vezes x, [p=0.2] *x ao cubo.* [p=0.4] {c}Produto *sessenta e quatro?* "
        "[p=0.2] Que número vezes ele mesmo, três vezes, dá sessenta e quatro? [p=0.2] *Quatro.* [p=0.4] {d}Atalho: "
        "[p=0.2] o termo do meio é a *raiz cúbica do produto.* [p=0.2] Sai na hora, [p=0.2] sem saber a razão."),

    # ================= BLOCO C: EQUIDISTANTES =================
    dict(id="08", block="equidist", text=
        "{t}E numa PG mais comprida? [p=0.4] {a}Lembra dos *termos equidistantes* da PA? [p=0.2] São os que estão à "
        "*mesma distância* das pontas: [p=0.2] o primeiro e o último, [p=0.2] o segundo e o penúltimo. [p=0.4] {b}Na PA "
        "*um, três, cinco, sete, nove, onze,* [p=0.2] cada par *soma* doze. [p=0.4] {c}Na PG *um, dois, quatro, oito, "
        "dezesseis, trinta e dois,* [p=0.2] cada par tem o mesmo *produto:* [p=0.2] um vezes trinta e dois, [p=0.2] dois "
        "vezes dezesseis, [p=0.2] quatro vezes oito. [p=0.2] Todos dão *trinta e dois.* [p=0.4] {d}De novo: [p=0.2] a "
        "soma da PA [p=0.2] vira *produto* na PG."),

    # ================= BLOCO D: A SOMA FINITA =================
    dict(id="09", block="soma", text=
        "{t}E como somar os termos de uma PG sem somar um por um? [p=0.4] {a}A *soma finita* [p=0.2] é tudo somado, do "
        "primeiro até o de posição n. [p=0.2] Ela se escreve *esse ene.* [p=0.4] {b}Escreva a soma: [p=0.2] a um, [p=0.2] "
        "mais a um vezes q, [p=0.2] mais a um vezes q ao quadrado, [p=0.2] até o último. [p=0.4] {c}Agora o truque: "
        "[p=0.2] *multiplique a soma inteira por q.* [p=0.3] Cada parcela *sobe um degrau.*"),
    dict(id="10", block="soma", text=
        "{t}E o que acontece quando você subtrai? [p=0.4] {a}Coloque as duas linhas uma sobre a outra. [p=0.2] Quase "
        "todas as parcelas *são iguais.* [p=0.3] {b}Na subtração, elas *se apagam.* [p=0.4] {c}Sobra só a *última* da "
        "linha de cima [p=0.2] menos a *primeira* da linha de baixo. [p=0.4] {d}Arrumando: [p=0.2] *esse ene* é igual a "
        "*a um,* [p=0.2] vezes *q elevado a n, menos um,* [p=0.2] dividido por *q menos um.* [p=0.4] {e}Com *q diferente "
        "de um.* [p=0.2] Se q for um, [p=0.2] todos os termos são iguais, [p=0.2] e a soma é *n vezes a um.*"),
    dict(id="11", block="atalho", text=
        "{t}Tem jeito de lembrar sem decorar? [p=0.4] {a}Atalho: [p=0.2] a soma é o *próximo termo* [p=0.2] *menos o "
        "primeiro,* [p=0.2] dividido por *q menos um.* [p=0.4] {b}É exatamente o que sobrou na subtração: [p=0.2] a "
        "última parcela, empurrada um degrau, [p=0.2] menos a primeira. [p=0.3] {c}Na razão dois, [p=0.2] o divisor é "
        "*um:* [p=0.2] a soma é o próximo termo menos o primeiro."),

    # ================= BLOCO E: A CORRENTE =================
    dict(id="12", block="corrente", text=
        "{t}Quantas pessoas recebem uma corrente de mensagens? [p=0.4] {a}No primeiro dia, *três pessoas* recebem. "
        "[p=0.2] Cada uma repassa, no dia seguinte, [p=0.2] para *três* pessoas novas. [p=0.4] {b}Por dia: [p=0.2] três, "
        "[p=0.2] nove, [p=0.2] vinte e sete, [p=0.2] oitenta e um, [p=0.2] duzentos e quarenta e três, [p=0.2] *setecentos "
        "e vinte e nove.* [p=0.4] {c}Só no sexto dia: [p=0.2] *setecentas e vinte e nove* pessoas. [p=0.3] {d}Ao todo: "
        "[p=0.2] três, vezes três elevado a seis menos um, [p=0.2] sobre dois. [p=0.2] Três vezes setecentos e vinte e "
        "oito, [p=0.2] dividido por dois: [p=0.2] *mil e noventa e dois.*"),
    dict(id="13", block="termosoma", text=
        "{t}Mas como saber qual dos dois números a questão quer? [p=0.4] {a}Atalho: [p=0.2] antes de qualquer conta, "
        "[p=0.2] escreva *termo ou soma?* [p=0.3] {b}*No sexto dia* é termo. [p=0.2] *Ao todo* é soma. [p=0.4] {c}E "
        "*liste os primeiros termos* [p=0.2] para conferir. [p=0.2] Três mais nove mais vinte e sete: [p=0.2] trinta e "
        "nove. [p=0.2] Pela fórmula, com três dias: [p=0.2] três vezes vinte e seis, sobre dois: [p=0.2] *trinta e nove.* "
        "[p=0.3] Bateu."),

    # ================= BLOCO F: O TABULEIRO =================
    dict(id="14", block="tabuleiro", text=
        "{t}E o tabuleiro do gancho? [p=0.4] {a}Primeira casa: [p=0.2] um grão. [p=0.2] Razão *dois.* [p=0.2] *Sessenta e "
        "quatro* casas. [p=0.4] {b}A soma: [p=0.2] um, vezes dois elevado a sessenta e quatro menos um, [p=0.2] dividido "
        "por dois menos um, [p=0.2] que é *um.* [p=0.3] {c}Sobra *dois elevado a sessenta e quatro, menos um.* [p=0.4] "
        "{d}Isso dá cerca de *um vírgula oito vezes dez elevado a dezenove* grãos. [p=0.2] Dezoito quintilhões. [p=0.3] "
        "É a força de uma PG de razão dois."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quanto dá *dois, mais seis, mais dezoito,* e assim por diante, [p=0.2] com *seis termos?* "
        "[p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Termo ou soma? [p=0.2] *Soma.* [p=0.2] A razão: [p=0.2] seis dividido por dois, "
        "[p=0.2] *três.* [p=0.4] {b}Esse seis: [p=0.2] dois, vezes três elevado a seis menos um, [p=0.2] dividido por três "
        "menos um. [p=0.2] Dois vezes setecentos e vinte e oito, [p=0.2] dividido por *dois.* [p=0.2] *Setecentos e vinte "
        "e oito.* [p=0.4] {c}Confira somando: [p=0.2] dois, seis, dezoito, cinquenta e quatro, cento e sessenta e dois, "
        "quatrocentos e oitenta e seis. [p=0.2] Total: [p=0.2] *setecentos e vinte e oito.* [p=0.3] Bateu."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] na PG, o termo do meio ao quadrado é o produto dos "
        "vizinhos. [p=0.5] {b}Dois: [p=0.2] três em PG: [p=0.2] x sobre q, x e x vezes q. [p=0.5] {c}Três: [p=0.2] soma "
        "finita: [p=0.2] a um vezes, q elevado a n menos um, [p=0.2] dividido por, q menos um."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dizer que o total da corrente é *três elevado a "
        "seis,* [p=0.2] setecentos e vinte e nove. [p=0.4] {b}Parece certo, [p=0.2] porque três elevado a seis é o número "
        "que aparece no sexto dia. [p=0.4] {c}Mas esse é *só o último dia.* [p=0.2] O total soma os seis dias: [p=0.2] mil "
        "e noventa e dois."),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] *esquecer de dividir por q menos um.* [p=0.2] Na conta que fizemos juntos: [p=0.2] dois "
        "vezes setecentos e vinte e oito, [p=0.2] *mil quatrocentos e cinquenta e seis.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o começo da fórmula está todo ali. [p=0.4] {c}Mas, na subtração, sobrou *q menos um* vezes a soma. "
        "[p=0.2] Falta dividir: [p=0.2] setecentos e vinte e oito."),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] usar a fórmula da soma *da PA* numa PG. [p=0.2] Dois mais quatrocentos e oitenta e seis, "
        "[p=0.2] vezes seis, [p=0.2] sobre dois: [p=0.2] *mil quatrocentos e sessenta e quatro.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque na série de PA [p=0.2] essa conta sempre funcionou. [p=0.4] {c}Mas ela vale quando os termos "
        "crescem *somando.* [p=0.2] Na PG, eles crescem *multiplicando:* [p=0.2] use a fórmula da PG."),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="21", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}No primeiro dia "
        "de uma campanha, [p=0.2] *três pessoas* recebem uma mensagem. [p=0.2] Cada pessoa que recebe a repassa, no dia "
        "seguinte, [p=0.2] a exatamente *três pessoas* que ainda não a tinham recebido. [p=0.3] O *total* de pessoas que "
        "terão recebido a mensagem *ao fim do sexto dia* é: [p=0.3] {qa}A: [p=0.2] dezoito. [p=0.2] {qb}B: [p=0.2] "
        "setecentos e vinte e nove. [p=0.2] {qc}C: [p=0.2] mil e noventa e dois. [p=0.2] {qd}D: [p=0.2] dois mil cento e "
        "oitenta e quatro. [p=0.2] {qe}E: [p=0.2] dois mil cento e oitenta e sete. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="22", block="q4", text=
        "{t}Termo ou soma? [p=0.3] {a}*Total:* [p=0.2] é soma. [p=0.4] {b}Liste: [p=0.2] três, nove, vinte e sete, "
        "oitenta e um, duzentos e quarenta e três, setecentos e vinte e nove. [p=0.2] PG de razão *três.* [p=0.4] {c}Três "
        "vezes setecentos e vinte e oito, [p=0.2] dividido por dois: [p=0.2] *mil e noventa e dois.* [p=0.3] {ok}*Letra C!*"),
    dict(id="23", block="q4", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A trata o crescimento como *linear:* [p=0.2] três por dia, durante seis dias. "
        "[p=0.4] {xb}A B conta *só o sexto dia.* [p=0.4] {xd}A D *esquece de dividir* por q menos um, [p=0.2] que é dois. "
        "[p=0.4] {xe}E a E calcula três elevado a *sete:* [p=0.2] quem receberia no sétimo dia."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="24", block="q5", text=
        "{t}E esta é *sua.* [p=0.3] {a}As idades de *três irmãos,* em anos, [p=0.2] são números inteiros [p=0.2] em "
        "*progressão geométrica crescente.* [p=0.3] O *produto* das três idades é *duzentos e dezesseis,* [p=0.2] e a "
        "*soma* é *dezenove.* [p=0.3] A idade do irmão *mais velho* é: [p=0.3] {qa}A: [p=0.2] quatro. [p=0.2] {qb}B: "
        "[p=0.2] seis. [p=0.2] {qc}C: [p=0.2] nove. [p=0.2] {qd}D: [p=0.2] doze. [p=0.2] {qe}E: [p=0.2] treze. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q5", text=
        "{t}Conferindo. [p=0.3] {a}Produto dado: [p=0.2] notação simétrica. [p=0.2] x sobre q, x, x vezes q. [p=0.2] x ao "
        "cubo é duzentos e dezesseis: [p=0.2] *x é seis.* [p=0.4] {b}Agora a soma: [p=0.2] seis sobre q, mais seis, mais "
        "seis q, [p=0.2] igual a dezenove. [p=0.2] Multiplique tudo por q e arrume: [p=0.2] *seis q ao quadrado, menos "
        "treze q, mais seis, igual a zero.* [p=0.4] {c}Bhaskara: [p=0.2] delta é cento e sessenta e nove menos cento e "
        "quarenta e quatro, [p=0.2] *vinte e cinco.* [p=0.2] q é *três meios* [p=0.2] ou *dois terços.*"),
    dict(id="26", block="q5", text=
        "{t}E qual das duas? [p=0.4] {a}A PG é *crescente:* [p=0.2] q é três meios. [p=0.3] {b}Idades: [p=0.2] quatro, "
        "seis, *nove.* [p=0.4] {c}Confira: [p=0.2] quatro mais seis mais nove, [p=0.2] dezenove. [p=0.2] Quatro vezes seis "
        "vezes nove, [p=0.2] duzentos e dezesseis. [p=0.3] {ok}*Letra C!*"),
    dict(id="27", block="q5", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A é o irmão *mais novo.* [p=0.4] {xb}A B é o *do meio,* [p=0.2] que sai direto "
        "do produto. [p=0.4] {xd}A D supõe *razão dois* sem usar a soma: [p=0.2] três, seis e doze somam vinte e um, "
        "[p=0.2] não dezenove. [p=0.4] {xe}E a E *subtrai* a idade do meio da soma."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] na PG, o termo do meio ao quadrado é o produto dos "
        "vizinhos. [p=0.5] {b}Dois: [p=0.2] três em PG: [p=0.2] x sobre q, x e x vezes q. [p=0.5] {c}Três: [p=0.2] soma "
        "finita: [p=0.2] a um vezes, q elevado a n menos um, [p=0.2] dividido por, q menos um."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Pinte *metade* de um quadrado, [p=0.2] depois metade do que sobrou, [p=0.2] e assim *para sempre.* [p=0.4] "
        "{b}Infinitas pinceladas. [p=0.3] A área pintada fica *infinita?* [p=0.4] {c}Próximo episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você chutaria quantos grãos cabem no tabuleiro? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
