# Roteiro — Progressão Geométrica, Episódio 3 de 5: soma infinita (infinitas parcelas, um número finito)
# Base: Estudos/Enem/estudos/01-matematica/32-progressao-geometrica-soma-infinita.html — seção 07 e, da seção 08, só a bola
#   que quica e o quadro "Subidas e descidas" + Questões 8, 6 e 3 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   METADE DO QUE SOBROU: você nunca passa do chocolate inteiro, mas chega tão perto quanto quiser.
#   A FÓRMULA SÓ FUNCIONA COM FREIO: a razão entre −1 e 1.
#   A BOLA CAI UMA VEZ da altura inicial; depois disso, cada altura é percorrida duas vezes.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# O gancho do usuário já diz "56 metros" (o resultado da Questão 3, "você faz"): mantido, é o desenho do prompt.
# DESVIO do prompt (bloco f): o prompt resolve a bola de 8 m com razão 3/4 (32 + 24 = 56), que é exatamente a Questão 3
#   ("você faz", com pausa). O bloco usa uma bola NOSSA: solta de 9 m, sobe 2/3 da altura anterior. Descidas
#   9 + 6 + 4 + … = 9 ÷ (1/3) = 27; subidas 6 + 4 + … = 6 ÷ (1/3) = 18; total 9 + 2 · 18 = 45 m. A animação principal da
#   bola com as barras 32 e 24 virando 56 fica na resolução da Q3. O erro 3 também usa a bola de 9 m (27 em vez de 45).
# Bloco e (0,2727… = 3/11) = mesmos números da Questão 6, que é "nós fazemos" (repetição pedida no prompt); na Q6 o foco
#   é a conferência 3 ÷ 11 e as alternativas erradas. O erro 4 (27/100) segue o prompt.
# Nós fazemos (prompt): 9 + 3 + 1 + 1/3 + … → q = 1/3 (entre −1 e 1) → S = 9 ÷ (2/3) = 27/2 = 13,5.
# Erros clássicos com números já resolvidos: a₁/q → 9 ÷ (1/3) = 27 (certo 13,5); q = 2 → 3 ÷ (1 − 2) = −3; bola sem as
#   subidas → 27 (certo 45); 0,2727… = 27/100 (certo 27/99 = 3/11).
# QUESTÃO 8 ("eu faço"): gabarito C (16 cm²). Erradas = material (A só a 1ª etapa: 12; B só três etapas: 12 + 3 + 0,75 =
#   15,75; D razão 1/2: 12 ÷ (1/2) = 24; E divide pela razão: 12 ÷ (1/4) = 48).
# QUESTÃO 6 ("nós fazemos"): gabarito B (3/11). Erradas = material (A só o 1º termo: 0,27 = 27/100; C 1 − q = 0,9:
#   0,27 ÷ 0,9 = 27/90; D 27/999 = 1/37 = 0,027027…, três noves para um período de dois algarismos; E 2/7 ≈ 0,2857…).
# QUESTÃO 3 ("você faz", com pausa): gabarito D (56). Erradas = material (A 24 só subidas; B 32 só descidas; C 48 dobra as
#   subidas e esquece a queda de 8 m; E 64 dobra as descidas, contando a queda inicial duas vezes).
# Acréscimos NOSSOS (marcados): atalho verde "1 − q = 1/k → multiplique a₁ por k" (cena 09); atalho verde "noves = 1 − q"
#   (cena 12); atalho verde da bola, total = h · (1 + q)/(1 − q) (cena 14: 9 · (5/3) ÷ (1/3) = 45; na Q3,
#   8 · (7/4) ÷ (1/4) = 56); atalho verde "palavra-sinal" (indefinidamente, até parar, para sempre: cena 23).
# Frases-chave (meio e fim, idênticas): 1. Com razão entre −1 e 1, a soma infinita é a₁ sobre (1 − q).
#   2. Razão fora disso: a soma não para de crescer. 3. Bola: a primeira queda uma vez; o resto, duas.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Soma infinita da PG: infinitas parcelas, um número finito | PG Ep. 3"
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
        "{a}Uma bola solta de *oito metros* [p=0.2] quica *para sempre,* [p=0.2] cada vez a *três quartos* da altura "
        "anterior. [p=0.5] {b}*Infinitos quiques.* [p=0.4] {c}Quanto ela percorre ao todo? [p=0.6] {d}Exatamente "
        "*cinquenta e seis metros.* [p=0.4] {e}Nem um centímetro a mais."),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Progressão geométrica.* [p=0.4] {a}Ao final, [p=0.2] você vai *somar "
        "infinitos termos,* [p=0.3] {b}transformar *dízimas em fração* [p=0.3] {c}e resolver o *problema da bola* "
        "[p=0.2] sem cair nos distratores."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] a *soma finita* da PG, [p=0.2] que tem um *q "
        "elevado a n* dentro dela. [p=0.4] {b}Da série de Frações: [p=0.2] um menos três quartos [p=0.2] é *um quarto.* "
        "[p=0.2] E dividir por uma fração [p=0.2] é *multiplicar pelo inverso:* [p=0.2] cinco dividido por um quarto "
        "[p=0.2] é cinco vezes quatro, [p=0.2] *vinte.* [p=0.4] {c}E da série de dízimas: [p=0.2] zero vírgula dois sete "
        "dois sete [p=0.2] é *vinte e sete sobre noventa e nove.* [p=0.3] Hoje você vai ver *por quê.*"),

    # ================= CONCRETO: O CHOCOLATE =================
    dict(id="04", block="chocolate", text=
        "{t}Dá para somar *infinitas* coisas [p=0.2] e o resultado não ser infinito? [p=0.4] {a}Pegue uma barra de "
        "chocolate. [p=0.2] Coma a *metade.* [p=0.3] {b}Depois, a metade *do que sobrou.* [p=0.4] "
        "{c}Meio, [p=0.2] três quartos, [p=0.2] sete oitavos. [p=0.3] Você *nunca passa* "
        "do chocolate inteiro, [p=0.2] {d}mas chega *tão perto quanto quiser.*"),
    dict(id="05", block="chocolate", text=
        "{t}Isso tem nome. [p=0.3] {a}*Soma infinita* [p=0.2] é somar os termos de uma PG [p=0.2] *sem parar nunca.* "
        "[p=0.4] {b}E cada parada no caminho [p=0.2] é uma *soma parcial:* [p=0.2] a soma dos primeiros pedaços. "
        "[p=0.4] {c}Quando as somas parciais chegam cada vez "
        "mais perto de um número, [p=0.2] a gente diz que a soma *converge.* [p=0.3] Esse número é o *limite.*"),

    # ================= BLOCO A: POR QUE A SOMA PODE SER FINITA =================
    dict(id="06", block="freio", text=
        "{t}Mas por que algumas somas infinitas *param* num número? [p=0.4] {a}Olhe a razão. [p=0.2] No chocolate, "
        "[p=0.2] ela é *um meio.* [p=0.3] {b}Multiplicar por um meio de novo e de novo [p=0.2] encolhe o pedaço: "
        "[p=0.2] um quarto, [p=0.2] um oitavo, [p=0.2] um sobre mil e vinte e quatro. [p=0.4] {c}*q elevado a n* "
        "[p=0.2] fica *perto de zero.* [p=0.3] {d}Isso acontece quando a razão está *entre menos um e um.* [p=0.2] Em "
        "símbolos: [p=0.2] *módulo de q menor que um.*"),
    dict(id="07", block="freio", text=
        "{t}E o que acontece com a fórmula? [p=0.4] {a}Na soma finita, [p=0.2] aquele *q elevado a n* [p=0.2] vai "
        "virando zero, [p=0.2] e *some.* [p=0.4] {b}Sobra uma fórmula curtinha: [p=0.3] *esse infinito* [p=0.2] é "
        "igual a *a um,* [p=0.2] dividido por *um menos q.* [p=0.4] {c}Ela dá o *limite* das somas parciais: [p=0.2] "
        "o número do qual elas se aproximam, sem nunca passar."),

    # ================= BLOCO C: O QUADRADO PINTADO =================
    dict(id="08", block="quadrado", text=
        "{t}Vamos ver a fórmula funcionar? [p=0.4] {a}Um quadrado de *área um.* [p=0.2] Pinte a metade. [p=0.2] Depois "
        "metade do que sobrou. [p=0.4] {b}Zero vírgula cinco, [p=0.2] zero vírgula setenta e "
        "cinco, [p=0.2] zero vírgula oitocentos e setenta e cinco. [p=0.3] Nunca passa de um. [p=0.4] {c}Agora a "
        "fórmula. [p=0.2] Primeiro, o freio: [p=0.2] *q é um meio, está entre menos um e um.* [p=0.2] Pode usar. "
        "[p=0.4] {d}Um meio, [p=0.2] dividido por um menos um meio. [p=0.2] Um meio sobre um meio: [p=0.2] *um.* "
        "[p=0.3] O quadrado inteiro."),
    dict(id="09", block="atalho_k", text=
        "{t}E como dividir por *um menos q* sem sofrer? [p=0.4] {a}Atalho: [p=0.2] se *um menos q* é *um sobre k,* "
        "[p=0.2] a soma é *k vezes a um.* [p=0.4] {b}Razão três quartos: [p=0.2] um menos três quartos é um quarto. "
        "[p=0.2] Então a soma é *quatro vezes* o primeiro termo. [p=0.4] {c}Razão um meio: [p=0.2] *duas vezes.* "
        "[p=0.2] Razão dois terços: [p=0.2] *três vezes.*"),

    # ================= BLOCO D: SEM FREIO =================
    dict(id="10", block="semfreio", text=
        "{t}E se a razão for *dois?* [p=0.4] {a}Um, [p=0.2] mais dois, [p=0.2] mais quatro, [p=0.2] mais oito. "
        "[p=0.2] A soma *não para de crescer.* [p=0.4] {b}Se você usar a fórmula mesmo assim: [p=0.2] um dividido por "
        "um menos dois [p=0.2] dá *menos um.* [p=0.4] {c}Somando números positivos, [p=0.2] deu *negativo.* [p=0.2] Um "
        "absurdo. [p=0.4] {d}A fórmula só funciona *com freio:* [p=0.2] a razão entre menos um e um."),

    # ================= BLOCO E: A DÍZIMA COMO PG =================
    dict(id="11", block="dizima", text=
        "{t}E o que a dízima tem a ver com isso? [p=0.4] {a}*Dízima periódica* [p=0.2] é um número com casas decimais "
        "que se repetem para sempre. [p=0.2] O bloco que se repete [p=0.2] é o *período.* [p=0.4] {b}Zero vírgula dois "
        "sete dois sete: [p=0.2] o período é *vinte e sete.* [p=0.4] {c}Quebre em pedaços: [p=0.2] zero vírgula vinte e "
        "sete, [p=0.2] mais zero vírgula zero zero vinte e sete, [p=0.2] e assim por diante. [p=0.3] É uma PG! "
        "[p=0.2] Primeiro termo *zero vírgula vinte e sete,* [p=0.2] razão *zero vírgula zero um.*"),
    dict(id="12", block="dizima", text=
        "{t}Tem freio? [p=0.3] {a}Zero vírgula zero um [p=0.2] está entre menos um e um. [p=0.2] *Tem.* [p=0.4] "
        "{b}Zero vírgula vinte e sete, [p=0.2] dividido por *zero vírgula noventa e nove.* [p=0.2] Tire as vírgulas: "
        "[p=0.2] *vinte e sete sobre noventa e nove.* [p=0.2] Simplificando por nove: [p=0.2] *três onze avos.* "
        "[p=0.4] {c}Atalho: [p=0.2] os *noves* da regra prática [p=0.2] são o *um menos q.* [p=0.3] {d}A regra dos "
        "noves que você aprendeu na série de Frações [p=0.2] *tem esta explicação.*"),

    # ================= BLOCO F: A BOLA =================
    dict(id="13", block="bola", text=
        "{t}E a bola que quica para sempre? [p=0.4] {a}Pense numa bola solta de *nove metros* [p=0.2] que sobe "
        "*dois terços* da altura anterior. [p=0.4] {b}A bola *cai uma vez* de nove metros. [p=0.2] Depois disso, "
        "[p=0.2] cada altura é percorrida *duas vezes:* [p=0.2] ela sobe e desce. [p=0.4] {c}Descidas: [p=0.2] nove, "
        "seis, quatro, e assim por diante. [p=0.2] Um menos dois terços é um terço: [p=0.2] *três vezes nove,* [p=0.2] "
        "*vinte e sete.* [p=0.4] {d}Subidas: [p=0.2] seis, quatro, e assim por diante: [p=0.2] três vezes seis, [p=0.2] "
        "*dezoito.* [p=0.3] Total: [p=0.2] *quarenta e cinco metros.*"),
    dict(id="14", block="bola_atalho", text=
        "{t}Dá para fazer em uma conta só? [p=0.4] {a}Dá. [p=0.2] O total é a *queda inicial,* [p=0.2] mais *duas "
        "vezes* as subidas. [p=0.4] {b}Atalho: [p=0.2] *h vezes um mais q, sobre um menos q.* [p=0.4] {c}Nove, vezes "
        "cinco terços, [p=0.2] dividido por um terço: [p=0.2] nove vezes cinco, [p=0.2] *quarenta e cinco.* [p=0.3] "
        "Bateu."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quanto dá *nove, mais três, mais um, mais um terço,* [p=0.2] e assim por diante? "
        "[p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}A razão: [p=0.2] três dividido por nove, [p=0.2] *um terço.* [p=0.2] Está entre "
        "menos um e um? [p=0.2] *Está.* [p=0.4] {b}Um menos um terço: [p=0.2] *dois terços.* [p=0.4] {c}Nove dividido "
        "por dois terços: [p=0.2] nove vezes três meios, [p=0.2] vinte e sete meios. [p=0.2] *Treze e meio.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] com razão entre menos um e um, [p=0.2] a soma infinita "
        "é *a um* sobre *um menos q.* [p=0.5] {b}Dois: [p=0.2] razão fora disso: [p=0.2] a soma *não para de crescer.* "
        "[p=0.5] {c}Três: [p=0.2] bola: [p=0.2] a primeira queda *uma vez;* [p=0.2] o resto, *duas.*"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dividir *pela razão.* [p=0.2] Nove dividido "
        "por um terço: [p=0.2] *vinte e sete.* [p=0.4] {b}Parece certo, [p=0.2] porque o q é o número que aparece na "
        "PG. [p=0.4] {c}Mas o denominador é *um menos q.* [p=0.2] A soma certa é treze e meio."),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] somar uma PG infinita *de razão dois.* [p=0.2] Três, seis, doze: [p=0.2] a fórmula daria "
        "*menos três.* [p=0.4] {b}Parece certo, [p=0.2] porque a fórmula aceita qualquer número. [p=0.4] {c}Mas ela só "
        "vale *com freio.*"),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] na bola, [p=0.2] fazer só *altura sobre um menos q.* [p=0.2] Na bola de nove metros: "
        "[p=0.2] *vinte e sete.* [p=0.4] {b}Parece certo, [p=0.2] porque é a fórmula da soma infinita. [p=0.4] {c}Mas "
        "isso é só a *descida.* [p=0.2] Faltaram as subidas: [p=0.2] o certo é *quarenta e cinco.*"),
    dict(id="21", block="erros", text=
        "{a}Quarto: [p=0.2] escrever zero vírgula dois sete dois sete [p=0.2] como *vinte e sete sobre cem.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque são duas casas depois da vírgula. [p=0.4] {c}Mas vinte e sete centésimos "
        "[p=0.2] *para* no sete; [p=0.2] a dízima continua. [p=0.2] O certo é *noventa e nove.*"),

    # ================= QUESTÃO 8 (EU FAÇO) =================
    dict(id="22", block="q8", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um designer cria "
        "um logotipo em etapas. [p=0.2] Na primeira, [p=0.2] um triângulo de *doze centímetros quadrados.* [p=0.2] Em "
        "cada etapa seguinte, [p=0.2] acrescenta triângulos cuja área total é *um quarto* da área acrescentada na etapa "
        "anterior. [p=0.3] Repetindo *indefinidamente,* [p=0.2] a área se aproxima de: [p=0.3] {qa}A: [p=0.2] doze. "
        "[p=0.2] {qb}B: [p=0.2] quinze vírgula setenta e cinco. [p=0.2] {qc}C: [p=0.2] dezesseis. [p=0.2] {qd}D: "
        "[p=0.2] vinte e quatro. [p=0.2] {qe}E: [p=0.2] quarenta e oito. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q8", text=
        "{t}A palavra-sinal. [p=0.3] {a}Atalho: [p=0.2] *indefinidamente,* [p=0.2] *até parar,* [p=0.2] *para "
        "sempre:* [p=0.2] é soma infinita. [p=0.4] {b}As áreas acrescentadas: [p=0.2] doze, [p=0.2] três, [p=0.2] zero "
        "vírgula setenta e cinco. [p=0.2] Razão *um quarto,* [p=0.2] entre menos um e um. [p=0.4] {c}Um menos um quarto "
        "é três quartos. [p=0.2] Doze dividido por três quartos: [p=0.2] doze vezes quatro terços, [p=0.2] *dezesseis.* "
        "[p=0.3] {ok}*Letra C!*"),
    dict(id="24", block="q8", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A fica *só na primeira etapa.* [p=0.4] {xb}A B soma *só três etapas:* "
        "[p=0.2] o processo é infinito. [p=0.4] {xd}A D usa razão *um meio.* [p=0.4] {xe}E a E divide *pela razão,* "
        "[p=0.2] e não por um menos q."),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="25", block="q6", text=
        "{t}Agora fazemos juntos. [p=0.3] {a}Um programa exibe o número *zero vírgula dois sete dois sete,* [p=0.2] com o "
        "bloco vinte e sete se repetindo *indefinidamente.* [p=0.3] Somando os infinitos termos, [p=0.2] obtém-se a "
        "fração: [p=0.3] {qa}A: [p=0.2] vinte e sete sobre cem. [p=0.2] {qb}B: [p=0.2] três onze avos. [p=0.2] {qc}C: "
        "[p=0.2] vinte e sete sobre noventa. [p=0.2] {qd}D: [p=0.2] um sobre trinta e sete. [p=0.2] {qe}E: [p=0.2] dois "
        "sétimos. [p=0.5] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q6", text=
        "{t}Juntos, então. [p=0.3] {a}Primeiro termo, [p=0.2] *zero vírgula vinte e sete;* [p=0.2] razão, [p=0.2] *zero "
        "vírgula zero um.* [p=0.2] Tem freio. [p=0.4] {b}Zero vírgula vinte e sete sobre zero vírgula noventa e nove: "
        "[p=0.2] vinte e sete noventa e nove avos, [p=0.2] *três onze avos.* [p=0.4] {c}Confira na conta: [p=0.2] três "
        "dividido por onze [p=0.2] dá zero vírgula dois sete dois sete. [p=0.2] {ok}*Letra B!*"),
    dict(id="27", block="q6", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A fica *só com o primeiro termo.* [p=0.4] {xc}A C usa *zero vírgula nove* no "
        "denominador, [p=0.2] como se a razão fosse zero vírgula um. [p=0.4] {xd}A D usa *três noves* [p=0.2] para um "
        "período de dois algarismos. [p=0.4] {xe}E a E é só uma *aproximação:* [p=0.2] zero vírgula dois oito."),

    # ================= QUESTÃO 3 (VOCÊ FAZ) =================
    dict(id="28", block="q3", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma bola é solta de *oito metros* [p=0.2] e, a cada toque no chão, [p=0.2] sobe "
        "até *três quartos* da altura de que caiu. [p=0.3] Mantido o padrão *indefinidamente,* [p=0.2] a distância "
        "vertical total, [p=0.2] em metros, [p=0.2] até parar, é: [p=0.3] {qa}A: [p=0.2] vinte e quatro. [p=0.2] {qb}B: "
        "[p=0.2] trinta e dois. [p=0.2] {qc}C: [p=0.2] quarenta e oito. [p=0.2] {qd}D: [p=0.2] cinquenta e seis. "
        "[p=0.2] {qe}E: [p=0.2] sessenta e quatro. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="29", block="q3", text=
        "{t}Conferindo. [p=0.3] {a}Razão três quartos: [p=0.2] freio ok. [p=0.2] Um menos três quartos é um quarto: "
        "[p=0.2] a soma é *quatro vezes* o primeiro termo. [p=0.4] {b}Descidas: [p=0.2] oito, seis, quatro e meio. "
        "[p=0.2] Quatro vezes oito: [p=0.2] *trinta e dois.* [p=0.4] {c}Subidas: [p=0.2] seis, quatro e meio. [p=0.2] "
        "Quatro vezes seis: [p=0.2] *vinte e quatro.* [p=0.4] {d}Juntas: [p=0.2] *cinquenta e seis metros.* [p=0.2] "
        "Pelo atalho: [p=0.2] oito vezes sete quartos, sobre um quarto: [p=0.2] oito vezes sete. [p=0.2] {ok}*Letra D!*"),
    dict(id="30", block="q3", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A conta *só as subidas.* [p=0.4] {xb}A B conta *só as descidas.* [p=0.4] "
        "{xc}A C dobra as subidas [p=0.2] e *esquece a queda* de oito metros. [p=0.4] {xe}E a E dobra *tudo:* [p=0.2] "
        "conta a primeira queda duas vezes."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] com razão entre menos um e um, [p=0.2] a soma "
        "infinita é *a um* sobre *um menos q.* [p=0.5] {b}Dois: [p=0.2] razão fora disso: [p=0.2] a soma *não para de "
        "crescer.* [p=0.5] {c}Três: [p=0.2] bola: [p=0.2] a primeira queda *uma vez;* [p=0.2] o resto, *duas.*"),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}Juros compostos, [p=0.2] remédio que cai à metade, [p=0.2] carro que perde valor todo ano: [p=0.3] {b}você "
        "já esbarrou na PG em outras séries [p=0.2] *sem que ela dissesse o nome.* [p=0.4] {c}Próximo episódio: [p=0.2] "
        "*a PG disfarçada.*"),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] antes desta aula, você achava que infinitos termos podiam dar um "
        "número finito? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os "
        "*flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
