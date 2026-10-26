# Roteiro — Frações, Decimais e Dízimas, Episódio 2 de 8: Números mistos e como saber qual fração é maior (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/03-fracoes-decimais-dizimas.html — seções 04 e 05 + Questões 6 e 2 da seção 12
#   + questão extra das tintas (de outro material da série, enviada completa no prompt).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   PIZZAS INTEIRAS + PEDAÇO: número misto é contar pizzas inteiras e mais um pedaço; a imprópria conta tudo em fatias:
#     2 pizzas e 3/4 são 11 fatias de quarto, ou 11/4.
#   PIZZA PARA MENOS GENTE: com o mesmo numerador, denominador MENOR dá pedaço MAIOR (pizza para 5 × pizza para 7).
#   A METADE COMO RÉGUA: a fração passou da metade da pizza ou não?
# Pré-requisitos: numerador e denominador (ep. 1); divisão com resto: 11 ÷ 4 = 2, resto 3.
# Números do material: 3/4 (própria) · 7/4 (imprópria) · 8/4 = 2 (aparente) · 2 3/4 = (2·4 + 3)/4 = 11/4 · 11/4 → 2 resto 3 → 2 3/4 ·
#   5/7 > 3/7 · 3/5 > 3/7 · 3/5 vs 5/8 → 24 vs 25 · 7/16 < 1/2 < 9/16. Exemplo próprio do bloco h: 3/4 = 0,75 · 2/3 ≈ 0,667 · 5/8 = 0,625.
# Questão 6 (material): 2 3/4 xícaras × 3 = 11/4 · 3 = 33/4 = 8 1/4 → C. A (6 3/4) = multiplicou só o inteiro.
#   B 7 1/2, D 8 3/4 e E 9 não saem de conta certa (D = copiou o 3/4 do enunciado; E = arredondou) — explicação nossa.
# Questão 2 (material): Ana 5/8 = 0,625 · Bruno 3/5 = 0,600 · Carla 7/10 = 0,700 · Diego 2/3 ≈ 0,667 → Carla, Diego, Ana, Bruno → A.
#   B troca Ana e Diego (0,625 × 0,667) · C põe Diego na frente de Carla · D é a ordem CRESCENTE (de trás para a frente) ·
#   E põe Ana primeiro.
# Questão extra das tintas: X 3/5 = 0,600 · Y 5/8 = 0,625 · Z 7/11 ≈ 0,636 → decrescente Z, Y, X → C.
#   A (X, Y, Z) = ordem crescente · B, D, E = comparou "no olho".
# Frases-chave (meio e fim, idênticas):
#   1. Misto vira impróprio antes de qualquer conta.
#   2. Mesmo numerador: denominador menor, pedaço maior.
#   3. Três ou mais frações: transforme em decimal.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "3/7 ou 3/5: qual é maior? Números mistos e comparação de frações | Frações Ep. 2"
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
        "{a}Três sétimos ou três quintos: [p=0.2] *qual é maior?* [p=0.5] {b}Muita gente responde três sétimos, [p=0.2] "
        "porque sete é maior que cinco. [p=0.5] {c}É *exatamente o contrário,* [p=0.3] {d}e você vai entender por quê [p=0.2] "
        "*com uma pizza.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai operar com *números mistos* sem errar, [p=0.4] {b}e colocar qualquer lista "
        "de frações *em ordem.* [p=0.4] {c}Cada palavra nova vai ser explicada, [p=0.2] uma de cada vez."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] o *denominador* diz em quantas fatias a pizza foi "
        "cortada; [p=0.2] o *numerador,* [p=0.2] quantas você pegou. [p=0.4] {b}E a divisão com resto: [p=0.2] onze dividido "
        "por quatro dá *dois,* [p=0.2] {c}porque dois vezes quatro é oito, [p=0.2] e *sobram três.* [p=0.3] {d}Esse três é o "
        "*resto.*"),

    # ================= BLOCO A: TIPOS DE FRAÇÃO =================
    dict(id="04", block="tipos", text=
        "{t}Pergunta de cozinha: [p=0.2] uma receita pede *duas xícaras e três quartos* de farinha. [p=0.4] Isso é mais ou "
        "menos que uma xícara? [p=0.5] {a}Mais! [p=0.3] E as frações também se dividem assim. [p=0.4] {b}Três quartos é uma "
        "fração *própria:* [p=0.2] o numerador é menor que o denominador, [p=0.2] {c}e ela vale *menos que um* inteiro."),
    dict(id="05", block="tipos", text=
        "{t}Agora, *sete quartos.* [p=0.3] {a}O numerador é *maior* que o denominador. [p=0.3] {b}Você pegou sete fatias, "
        "[p=0.2] mas a pizza só tinha quatro: [p=0.2] precisou de outra pizza. [p=0.4] {c}Essa é a fração *imprópria:* "
        "[p=0.2] vale *mais que um.*"),
    dict(id="06", block="tipos", text=
        "{t}E *oito quartos?* [p=0.3] {a}Oito fatias de quarto [p=0.2] são exatamente *duas pizzas inteiras.* [p=0.4] "
        "{b}É a fração *aparente:* [p=0.2] um inteiro disfarçado. [p=0.3] {c}Acontece quando o numerador está na tabuada do "
        "denominador: [p=0.2] oito quartos é igual a *dois.*"),
    dict(id="07", block="tipos", text=
        "{t}E as duas xícaras e três quartos da receita? [p=0.4] {a}Isso é um *número misto:* [p=0.2] uma parte inteira, "
        "[p=0.2] o dois, [p=0.3] {b}mais uma parte em fração, [p=0.2] o três quartos. [p=0.4] {c}Lê-se *dois inteiros e "
        "três quartos.*"),

    # ================= BLOCO B: MISTO → IMPRÓPRIA =================
    dict(id="08", block="mista", text=
        "{t}Agora, uma pergunta: [p=0.2] dois inteiros e três quartos [p=0.2] *são quantas fatias de quarto?* [p=0.4] "
        "{a}Imagine duas pizzas inteiras [p=0.2] e mais três quartos de outra. [p=0.4] {b}Corte tudo em quartos. [p=0.3] "
        "{c}Cada pizza inteira dá quatro fatias: [p=0.2] duas pizzas, [p=0.2] *oito fatias.* [p=0.3] {d}Mais as três do "
        "pedaço: [p=0.2] *onze fatias de quarto.* [p=0.4] {e}Onze quartos."),
    dict(id="09", block="mista", text=
        "{t}Isso vira uma regra. [p=0.3] {a}Inteiro *vezes* denominador, [p=0.2] *mais* o numerador. [p=0.3] E o denominador "
        "continua o mesmo. [p=0.4] {b}Dois vezes quatro, [p=0.2] oito, [p=0.2] mais três, [p=0.2] *onze.* [p=0.2] Onze quartos. "
        "[p=0.5] {c}O atalho para não esquecer: [p=0.2] *a volta da ferradura.* [p=0.3] {d}Começa embaixo, [p=0.2] multiplica "
        "o inteiro, [p=0.2] e sobe somando o de cima."),

    # ================= BLOCO C: IMPRÓPRIA → MISTA =================
    dict(id="10", block="impropria", text=
        "{t}E o caminho de volta? [p=0.2] Onze quartos são quantas pizzas inteiras? [p=0.4] {a}Junte as onze fatias de quatro "
        "em quatro. [p=0.3] {b}Fecham *duas* pizzas, [p=0.2] e sobram *três* fatias. [p=0.4] {c}Na conta, [p=0.2] é a divisão "
        "com resto: [p=0.2] onze dividido por quatro, [p=0.2] *dois, resto três.* [p=0.4] {d}O resultado da divisão vira o "
        "*inteiro.* [p=0.3] {e}O resto vira o *numerador.* [p=0.3] {f}E o denominador fica o mesmo: [p=0.2] *dois inteiros e "
        "três quartos.*"),

    # ================= BLOCO D: REGRA DE OURO =================
    dict(id="11", block="ouro", text=
        "{t}E agora, a regra de ouro: [p=0.3] *nunca faça conta com o número misto direto.* [p=0.4] {a}Converta para "
        "imprópria primeiro, [p=0.2] {b}faça a conta, [p=0.2] {c}e só volte para misto se a resposta pedir. [p=0.5] {d}Somar "
        "os inteiros de um lado e as frações do outro [p=0.2] até funciona na soma, [p=0.3] {e}mas *quebra feio* na "
        "multiplicação e na divisão."),

    # ================= BLOCO E: MESMO DENOMINADOR =================
    dict(id="12", block="mesmo_den", text=
        "{t}Agora, comparar. [p=0.3] Cinco sétimos ou três sétimos: [p=0.2] qual é maior? [p=0.4] {a}As duas pizzas foram "
        "cortadas em *sete.* [p=0.3] As fatias têm o mesmo tamanho. [p=0.4] {b}Quem pegou cinco fatias, [p=0.2] comeu mais. "
        "[p=0.4] {c}Mesmo denominador: [p=0.2] *o maior numerador vence.*"),

    # ================= BLOCO F: MESMO NUMERADOR =================
    dict(id="13", block="mesmo_num", text=
        "{t}E a pergunta do começo: [p=0.2] três quintos ou três sétimos? [p=0.4] {a}Agora as duas têm *três* fatias. [p=0.3] "
        "{b}Mas uma pizza foi dividida entre *cinco* pessoas, [p=0.3] {c}e a outra entre *sete.* [p=0.4] {d}Quanto mais gente "
        "dividindo, [p=0.2] *menor* a fatia de cada um. [p=0.4] {e}Três fatias grandes [p=0.2] são mais pizza que três "
        "fatias pequenas. [p=0.3] {f}Três quintos é *maior.*"),
    dict(id="14", block="mesmo_num", text=
        "{t}Por que o sete engana? [p=0.3] {a}Porque, no dia a dia, [p=0.2] número maior é coisa maior. [p=0.4] {b}Mas o "
        "denominador não conta pedaços que você tem: [p=0.2] ele conta *em quantos pedaços* o inteiro foi cortado. [p=0.4] "
        "{c}A regra: [p=0.2] mesmo numerador, [p=0.2] *denominador menor, [p=0.2] pedaço maior.*"),

    # ================= BLOCO G: PRODUTO CRUZADO =================
    dict(id="15", block="cruzado", text=
        "{t}E quando os dois são diferentes? [p=0.3] Três quintos ou cinco oitavos? [p=0.4] {a}Para comparar só *duas* "
        "frações, [p=0.2] use o *produto cruzado* do episódio um: [p=0.2] multiplicar em xis. [p=0.4] {b}Três vezes oito, "
        "[p=0.2] *vinte e quatro.* [p=0.2] Esse resultado fica do lado do três quintos. [p=0.4] {c}Cinco vezes cinco, [p=0.2] "
        "*vinte e cinco.* [p=0.2] Fica do lado do cinco oitavos. [p=0.4] {d}Vinte e cinco é maior: [p=0.2] *cinco oitavos "
        "vence.* [p=0.4] {e}O atalho: [p=0.2] cada produto fica do lado do *numerador* que você usou."),

    # ================= BLOCO H: TRÊS OU MAIS → DECIMAL =================
    dict(id="16", block="decimal", text=
        "{t}E se forem três, quatro frações? [p=0.4] {a}Aí o caminho mais seguro é *transformar em decimal:* [p=0.3] "
        "{b}dividir o numerador pelo denominador. [p=0.4] {c}Três quartos, [p=0.2] zero vírgula setenta e cinco. [p=0.3] "
        "{d}Dois terços, [p=0.2] mais ou menos zero vírgula seiscentos e sessenta e sete. [p=0.3] {e}Cinco oitavos, [p=0.2] "
        "zero vírgula seiscentos e vinte e cinco. [p=0.4] {f}Agora é só olhar: [p=0.2] *ordem decrescente,* [p=0.2] que é do "
        "maior para o menor: [p=0.2] três quartos, [p=0.2] dois terços, [p=0.2] cinco oitavos. [p=0.4] {g}E a *ordem "
        "crescente* é o contrário: [p=0.2] do menor para o maior."),

    # ================= BLOCO I: A REFERÊNCIA 1/2 =================
    dict(id="17", block="metade", text=
        "{t}E um truque que elimina alternativas na hora: [p=0.3] *compare com a metade.* [p=0.4] {a}A fração passou da metade "
        "da pizza ou não? [p=0.4] {b}Sete dezesseis avos: [p=0.2] a metade de dezesseis é oito. [p=0.3] {c}Sete é *menos* que "
        "oito: [p=0.2] *não* chegou na metade. [p=0.4] {d}Nove dezesseis avos: [p=0.2] nove é *mais* que oito: [p=0.2] "
        "*passou* da metade. [p=0.4] {e}Sem fazer conta nenhuma."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] misto vira impróprio antes de qualquer conta. [p=0.5] "
        "{b}Dois: [p=0.2] mesmo numerador: [p=0.2] denominador menor, [p=0.2] pedaço maior. [p=0.5] {c}Três: [p=0.2] três ou "
        "mais frações: [p=0.2] transforme em decimal."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] multiplicar *só o inteiro* do número misto. [p=0.3] "
        "Dois inteiros e três quartos vezes três [p=0.2] vira seis inteiros e três quartos. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o inteiro é a parte que salta aos olhos. [p=0.4] {c}Mas o três quartos também é multiplicado. [p=0.2] "
        "*Converta para imprópria antes.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] achar que três sétimos é maior que três quintos [p=0.2] porque sete é maior que cinco. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque número maior costuma ser coisa maior. [p=0.4] {c}Mas o denominador é em quantas "
        "fatias a pizza foi cortada: [p=0.2] *mais fatias, fatias menores.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] comparar *no olho* frações muito próximas. [p=0.4] {b}Parece certo, [p=0.2] porque elas parecem "
        "quase iguais. [p=0.4] {c}Mas quando estão perto, [p=0.2] o olho erra. [p=0.2] *Transforme em decimal* e compare."),

    # ================= QUESTÃO 6 (EU FAÇO) =================
    dict(id="22", block="q6", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.3] A primeira eu faço com você. [p=0.4] {a}Uma receita de bolo leva *dois "
        "inteiros e três quartos* de xícaras de farinha. [p=0.4] {b}Para preparar três receitas iguais, [p=0.2] quantas xícaras "
        "de farinha serão necessárias? [p=0.5] {c}A: [p=0.2] seis inteiros e três quartos. [p=0.3] {d}B: [p=0.2] sete e meio. "
        "[p=0.3] {e}C: [p=0.2] oito inteiros e um quarto. [p=0.3] {f}D: [p=0.2] oito inteiros e três quartos. [p=0.3] {g}E: "
        "[p=0.2] nove. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q6", text=
        "{t}Vamos lá. [p=0.3] Regra de ouro: [p=0.2] misto vira impróprio. [p=0.4] {a}Dois vezes quatro, [p=0.2] oito, "
        "[p=0.2] mais três, [p=0.2] *onze quartos.* [p=0.4] {b}Onze quartos vezes três: [p=0.2] *trinta e três quartos.* "
        "[p=0.4] {c}Voltando para misto: [p=0.2] trinta e três dividido por quatro, [p=0.2] *oito, resto um.* [p=0.3] {d}Oito "
        "inteiros e um quarto. [p=0.3] {ok}*Letra C!*"),
    dict(id="24", block="q6", text=
        "{t}E a armadilha? [p=0.3] {xa}A letra A, [p=0.2] seis inteiros e três quartos, [p=0.2] é de quem multiplicou *só o "
        "inteiro* por três [p=0.2] e repetiu a fração. [p=0.4] {xd}A D acertou o oito, [p=0.2] mas copiou o três quartos do "
        "enunciado. [p=0.4] {xb}E a B e a E [p=0.2] {xe}não saem de nenhuma conta certa: [p=0.2] trinta e três quartos é "
        "*exatamente* oito e um quarto."),

    # ================= QUESTÃO 2 (NÓS FAZEMOS) =================
    dict(id="25", block="q2", text=
        "{t}A próxima a gente faz junto. [p=0.3] {a}Quatro candidatos acertaram as seguintes frações de uma prova: [p=0.3] "
        "{b}Ana, [p=0.2] cinco oitavos; [p=0.2] Bruno, [p=0.2] três quintos; [p=0.2] Carla, [p=0.2] sete décimos; [p=0.2] e "
        "Diego, [p=0.2] dois terços. [p=0.4] {c}Qual é a ordem decrescente de acertos? [p=0.4] {d}A: [p=0.2] Carla, Diego, "
        "Ana, Bruno. [p=0.3] {e}B: [p=0.2] Carla, Ana, Diego, Bruno. [p=0.3] {f}C: [p=0.2] Diego, Carla, Ana, Bruno. [p=0.3] "
        "{g}D: [p=0.2] Bruno, Ana, Diego, Carla. [p=0.3] {h}E: [p=0.2] Ana, Carla, Diego, Bruno."),
    dict(id="26", block="q2", text=
        "{t}Uma dica antes de pausar: [p=0.2] são *quatro* frações. [p=0.3] {a}Qual é o caminho mais seguro? [p=0.4] {b}Pause e "
        "tente. [p=2.0]"),
    dict(id="27", block="q2", text=
        "{t}Isso: [p=0.2] *decimal.* [p=0.4] {a}Ana, [p=0.2] zero vírgula seiscentos e vinte e cinco. [p=0.3] {b}Bruno, "
        "[p=0.2] zero vírgula seiscentos. [p=0.3] {c}Carla, [p=0.2] zero vírgula setecentos. [p=0.3] {d}Diego, [p=0.2] mais ou "
        "menos zero vírgula seiscentos e sessenta e sete. [p=0.4] {e}Do maior para o menor: [p=0.2] Carla, [p=0.2] Diego, "
        "[p=0.2] Ana, [p=0.2] Bruno. [p=0.3] {ok}*Letra A!*"),
    dict(id="28", block="q2", text=
        "{t}E as outras? [p=0.3] {xb}A B troca Ana e Diego: [p=0.2] seiscentos e vinte e cinco é menos que seiscentos e "
        "sessenta e sete. [p=0.4] {xc}A C põe Diego na frente de Carla. [p=0.4] {xd}A D é a ordem *crescente,* [p=0.2] de trás "
        "para a frente. [p=0.4] {xe}E a E põe Ana em primeiro. [p=0.4] {x}As quatro estão entre zero vírgula seis e zero "
        "vírgula sete: [p=0.2] no olho, [p=0.2] não daria."),

    # ================= QUESTÃO EXTRA (VOCÊ FAZ) =================
    dict(id="29", block="tintas", text=
        "{t}E a última, [p=0.2] *você* faz. [p=0.4] {a}Três marcas de tinta informam o rendimento por lata [p=0.2] em relação "
        "a uma parede padrão: [p=0.3] {b}a marca X cobre três quintos da parede, [p=0.2] a marca Y cobre cinco oitavos [p=0.2] "
        "e a marca Z cobre sete onze avos. [p=0.4] {c}Qual é a ordem decrescente de rendimento? [p=0.4] {d}A: [p=0.2] X, Y, Z. "
        "[p=0.3] {e}B: [p=0.2] Y, X, Z. [p=0.3] {f}C: [p=0.2] Z, Y, X. [p=0.3] {g}D: [p=0.2] Z, X, Y. [p=0.3] {h}E: [p=0.2] "
        "Y, Z, X. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="30", block="tintas", text=
        "{t}Vamos conferir. [p=0.3] São três frações: [p=0.2] decimal. [p=0.4] {a}Três quintos, [p=0.2] zero vírgula "
        "seiscentos. [p=0.3] {b}Cinco oitavos, [p=0.2] zero vírgula seiscentos e vinte e cinco. [p=0.3] {c}Sete onze avos, "
        "[p=0.2] mais ou menos zero vírgula seiscentos e trinta e seis. [p=0.4] {d}Do maior para o menor: [p=0.2] Z, [p=0.2] "
        "Y, [p=0.2] X. [p=0.3] {ok}*Letra C!*"),
    dict(id="31", block="tintas", text=
        "{t}E repare: [p=0.2] as três estão perto de zero vírgula seis. [p=0.4] {a}Por isso comparar no olho não funciona: "
        "[p=0.2] *é preciso dividir de fato.* [p=0.4] {xa}A letra A é a ordem crescente, [p=0.2] de trás para a frente. [p=0.4] "
        "{xb}E a B, [p=0.2] a D e a E [p=0.2] são chute de quem comparou no olho."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] misto vira impróprio antes de qualquer conta. [p=0.5] "
        "{b}Dois: [p=0.2] mesmo numerador: [p=0.2] denominador menor, [p=0.2] pedaço maior. [p=0.5] {c}Três: [p=0.2] três ou "
        "mais frações: [p=0.2] transforme em decimal."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}Você já sabe *ler* e *comparar* frações. [p=0.4] {b}Agora vamos fazer contas com elas: [p=0.3] {c}somar, [p=0.2] "
        "subtrair, [p=0.2] multiplicar [p=0.2] e dividir. [p=0.4] {d}Próximo episódio."),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você acertou a questão das tintas? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
