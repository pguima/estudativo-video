# Roteiro — Função logarítmica e aplicações, Episódio 2 de 5: escalas logarítmicas e o pH
# Base: Estudos/Enem/estudos/01-matematica/28-funcao-logaritmica-aplicacoes.html — seções 05 e 06 (e o quadro "O que rende
#   mais aqui" da seção 01) + Questões 1, 2 e 6 (seção 12). Só as fórmulas e os valores do material: pH = −log[H⁺],
#   [H⁺] = 10^(−pH) mol/L, neutro pH 7 a 25 °C, pH + pOH = 14 só citado. Richter e decibéis ficam para os eps. 3 e 4.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Narração por extenso ("pê agá", "agá mais"): o gerar_voz_local.py não aplica PRONUNCIA.
# Analogias âncora (retomadas na série):
#   A escala logarítmica é uma RÉGUA DE ZEROS: cada passo igual na régua é um fator 10 na grandeza.
#   A DIFERENÇA DE LEITURA VIRA EXPOENTE DA RAZÃO.
#   O pH é uma escala DE CABEÇA PARA BAIXO: menor pH, mais ácido (a pilha de bolinhas de H⁺ cresce ×10 a cada passo
#   para a esquerda).
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Definições em uma frase (pedidas no prompt): escala logarítmica, leitura, grandeza, razão, concentração, íon H⁺, mol/L,
#   pH, ácido, neutro. "Mol é uma unidade de quantidade, como a dúzia" é só a definição em linguagem simples.
# Exemplos NOSSOS (o recorte não traz contas além da tabela): limão, café e água da chuva no concreto (pH 2 e 5 do
#   material); o atalho "1 seguido de tantos zeros quanto a diferença"; log 5 = 1 − 0,30 = 0,70 (5 = 10 ÷ 2, kit da série
#   de Logaritmos) para a linha 5 · 10⁻⁴ da tabela da seção 06.
# Nós fazemos (prompt): pH 4 x pH 6 → diferença 2 → 10² = 100 vezes (a de pH menor tem mais H⁺).
# QUESTÃO 1 (eu faço, texto do material): 10⁻³ ÷ 10⁻⁶ = 10³ = 1 000 → D. Erradas (material): A divide os pHs (6 ÷ 3);
#   B para na diferença; C multiplica a diferença por 10; E usa só o pH da chuva como expoente (10⁶).
# QUESTÃO 2 (nós fazemos, texto do material): −(0,30 − 4) = 3,7 → B; o atalho já diz "entre 3 e 4" e elimina C, D, E.
#   Erradas (material): A 3,4 desconta 2 · log 2 (como se fosse 4 · 10⁻⁴); C 4,0 ignora o 2; D 4,3 soma o log 2 (sinal);
#   E 4,6 erra o sinal e dobra o log 2.
# QUESTÃO 6 (você faz, com pausa, texto do material): menor pH da faixa → 10^(−7,2) → B. Erradas (material): A inverte a
#   relação; C usa a largura da faixa (0,6); D e E esquecem o sinal (10^7,2 ≈ 16 milhões de mol/L, absurdo).
# Atalhos (verde): "um seguido de tantos zeros quanto a diferença" (+ 0,3 a mais ≈ dobro) · o atalho do pH
#   (k · 10⁻ⁿ → entre n − 1 e n), usado de novo na Q2 antes da conta.
# Contas conferidas em trabalho/conferir_contas.py.
# Frases-chave (meio e fim, idênticas): 1. Numa escala de base 10, a diferença de leitura é o expoente da razão.
#   2. Menor pH, mais ácido: cada unidade a menos é 10 vezes mais H⁺. 3. Se [H⁺] = k · 10⁻ⁿ, o pH fica entre n − 1 e n.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Escala logarítmica e pH: por que pH 2 é 1 000 vezes mais ácido que pH 5 | Função Logarítmica Ep. 2"
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
        "{a}*Pê agá dois* [p=0.2] e *pê agá cinco.* [p=0.4] {b}Diferença de *três.* [p=0.4] {c}Quem responde [p=0.2] "
        "*três vezes mais ácido* [p=0.2] *erra por muito:* [p=0.4] {d}a concentração de agá mais [p=0.2] é *mil vezes "
        "maior.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *comparar duas leituras* de uma escala logarítmica [p=0.3] {b}e "
        "calcular o *pê agá* de uma solução, [p=0.2] mesmo com um *dois* ou um *cinco* na frente da potência de dez."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Notação científica: [p=0.2] *quantas vezes maior* é "
        "*divisão,* [p=0.2] e duas ordens de grandeza de diferença [p=0.2] são um fator *cem.* [p=0.4] {b}Da série de "
        "Logaritmos: [p=0.2] log de *M vezes N* [p=0.2] é *log de M mais log de N.* [p=0.4] {c}E *log de dois* "
        "[p=0.2] é mais ou menos *zero vírgula trinta.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em três líquidos. [p=0.3] {a}O suco de *limão:* [p=0.2] pê agá perto de *dois.* [p=0.3] {b}O "
        "*café:* [p=0.2] pê agá perto de *cinco.* [p=0.3] {c}E a *água da chuva,* [p=0.2] que também é um pouco "
        "ácida. [p=0.4] {d}*Ácido,* [p=0.2] no dia a dia, [p=0.2] é o que é azedo, como o limão. [p=0.4] {e}Quem é "
        "mais ácido, [p=0.2] e *quantas vezes?*"),

    # ================= BLOCO A: O PROBLEMA DA RÉGUA COMUM =================
    dict(id="05", block="problema", text=
        "{t}Por que inventaram essa escala? [p=0.4] {a}O ouvido percebe sons [p=0.2] de *dez elevado a menos doze* "
        "[p=0.2] até *um* watt por metro quadrado. [p=0.4] {b}Do mais fraco ao mais forte, [p=0.2] um fator de *um "
        "trilhão.* [p=0.4] {c}Numa régua comum, [p=0.2] quase todos os sons do dia a dia [p=0.2] ficariam *espremidos "
        "perto do zero.*"),
    dict(id="06", block="problema", text=
        "{t}A solução. [p=0.3] {a}Uma *escala logarítmica* [p=0.2] troca cada *fator dez* [p=0.2] por um *passo "
        "igual.* [p=0.4] {b}É uma *régua de zeros:* [p=0.2] um passo, [p=0.2] vezes dez; [p=0.2] dois passos, "
        "[p=0.2] vezes cem. [p=0.4] {c}O número que você lê na régua [p=0.2] é a *leitura.* [p=0.3] {d}O que se mede "
        "de verdade, [p=0.2] como a intensidade do som, [p=0.2] é a *grandeza.*"),

    # ================= BLOCO B: A REGRA =================
    dict(id="07", block="regra", text=
        "{t}E como comparar duas leituras? [p=0.4] {a}A *razão* [p=0.2] é o resultado da divisão: [p=0.2] diz *quantas "
        "vezes* uma grandeza é maior. [p=0.4] {b}A regra: [p=0.2] *G dois sobre G um* [p=0.2] é *dez elevado a E dois "
        "menos E um.* [p=0.4] {c}Por quê? [p=0.2] Cada passo de diferença [p=0.2] é mais um *vezes dez.* [p=0.4] {d}A "
        "*diferença de leitura* [p=0.2] vira o *expoente da razão.*"),

    # ================= BLOCO C: A TABELA =================
    dict(id="08", block="tabela", text=
        "{t}Uma tabela que vale ouro. [p=0.3] {a}Diferença *um:* [p=0.2] razão *dez.* [p=0.3] {b}Diferença *dois:* "
        "[p=0.2] *cem.* [p=0.3] {c}Diferença *três:* [p=0.2] *mil.* [p=0.4] {d}Diferença *zero vírgula três:* [p=0.2] "
        "mais ou menos *dois,* [p=0.2] porque log de dois é zero vírgula trinta. [p=0.4] {e}E diferença *um e meio:* "
        "[p=0.2] dez vezes raiz de dez, [p=0.2] mais ou menos *trinta e dois.*"),

    # ================= ATALHO: OS ZEROS =================
    dict(id="09", block="atalho", text=
        "{t}Atalho. [p=0.3] {a}Diferença inteira? [p=0.2] Escreva *um* [p=0.2] e coloque *tantos zeros* quanto a "
        "diferença. [p=0.3] Três de diferença: [p=0.2] um, zero, zero, zero, [p=0.2] *mil.* [p=0.4] {b}E *zero vírgula "
        "três* a mais [p=0.2] é quase o *dobro.*"),

    # ================= BLOCO D: DIFERENÇA NÃO É RAZÃO =================
    dict(id="10", block="armadilha", text=
        "{t}Agora, a armadilha. [p=0.4] {a}Pê agá dois e pê agá cinco. [p=0.3] {b}Dividir as leituras: [p=0.2] cinco "
        "dividido por dois, [p=0.2] *dois e meio.* [p=0.2] Errado. [p=0.4] {c}Subtrair e parar: [p=0.2] *três.* "
        "[p=0.2] Também errado. [p=0.4] {d}Esses são os *dois distratores clássicos.* [p=0.3] {e}A diferença, três, "
        "[p=0.2] é o *expoente:* [p=0.2] dez ao cubo, [p=0.2] *mil.*"),

    # ================= BLOCO E: O QUE É pH =================
    dict(id="11", block="ph", text=
        "{t}E o que é esse pê agá? [p=0.4] {a}*Concentração* [p=0.2] é quanto de uma coisa está dissolvida num "
        "volume. [p=0.4] {b}No pê agá, [p=0.2] a coisa é o *íon hidrogênio,* [p=0.2] o *agá mais:* [p=0.2] uma "
        "partícula minúscula que deixa a solução ácida. [p=0.4] {c}Ela é medida em *mol por litro:* [p=0.2] mol é só "
        "uma unidade de quantidade, [p=0.2] como a dúzia. [p=0.4] {d}E o *pê agá* [p=0.2] é *menos o log* da "
        "concentração de agá mais."),
    dict(id="12", block="ph", text=
        "{t}A mesma fórmula, ao contrário. [p=0.3] {a}{b}A concentração é *dez elevado a menos pê agá,* [p=0.2] em mol por litro. [p=0.4] {c}Por que "
        "o *menos?* [p=0.2] As concentrações são potências *negativas* de dez, [p=0.2] como dez elevado a menos três. "
        "[p=0.3] O log dá menos três, [p=0.2] e o menos da fórmula [p=0.2] deixa o pê agá *positivo:* três. [p=0.4] "
        "{d}A vinte e cinco graus, [p=0.2] solução *neutra* [p=0.2] tem pê agá "
        "*sete.* [p=0.3] {e}O pê ó agá, [p=0.2] que soma catorze com ele, [p=0.2] fica para a Química."),

    # ================= BLOCO F: NÚMERO NA FRENTE DA POTÊNCIA =================
    dict(id="13", block="contas", text=
        "{t}E se aparecer um número na frente? [p=0.4] {a}Dez elevado a menos três: [p=0.2] pê agá *três,* direto. "
        "[p=0.4] {b}Agora, *dois vezes dez elevado a menos cinco.* [p=0.3] {c}Log do produto é *soma:* [p=0.2] log de "
        "dois, [p=0.2] zero vírgula trinta, [p=0.2] *mais* o log de dez elevado a menos cinco, [p=0.2] menos cinco. "
        "[p=0.4] {d}Zero vírgula trinta menos cinco: [p=0.2] *menos quatro vírgula sete.* [p=0.3] O menos da fórmula "
        "vira o sinal: [p=0.2] pê agá *quatro vírgula sete.*"),
    dict(id="14", block="contas", text=
        "{t}Mais um. [p=0.3] {a}*Cinco vezes dez elevado a menos quatro.* [p=0.3] {b}Log de cinco: [p=0.2] cinco é dez "
        "dividido por dois, [p=0.2] então é um menos zero vírgula trinta, [p=0.2] *zero vírgula setenta.* [p=0.4] "
        "{c}Zero vírgula setenta menos quatro: [p=0.2] menos três vírgula três. [p=0.3] {d}Pê agá *três vírgula "
        "três.*"),

    # ================= ATALHO DO pH =================
    dict(id="15", block="atalho2", text=
        "{t}Atalho do pê agá. [p=0.3] {a}Se a concentração é *k vezes dez elevado a menos n,* [p=0.2] com k entre um e "
        "dez, [p=0.3] {b}o pê agá é *n menos log de k:* [p=0.2] fica *entre n menos um e n.* [p=0.4] {c}Dois vezes "
        "dez elevado a menos cinco: [p=0.2] entre *quatro e cinco.* [p=0.2] Deu quatro vírgula sete. [p=0.4] {d}Isso "
        "elimina alternativas *antes de qualquer conta.*"),

    # ================= BLOCO H: MENOR pH, MAIS ÁCIDO =================
    dict(id="16", block="regua_ph", text=
        "{t}E quem é mais ácido? [p=0.4] {a}Olhe a régua de zero a catorze. [p=0.3] {b}Cada passo para a *esquerda,* "
        "[p=0.2] a pilha de agá mais fica *dez vezes maior.* [p=0.4] {c}O pê agá é uma escala *de cabeça para baixo:* "
        "[p=0.2] *menor pê agá, mais ácido.* [p=0.4] {d}Limão em dois, café em cinco: [p=0.2] três passos, [p=0.2] o "
        "limão tem cerca de *mil vezes* mais agá mais."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma solução tem *pê agá quatro,* [p=0.2] e outra, *pê agá seis.* [p=0.3] {b}Quantas "
        "vezes mais agá mais [p=0.2] tem a *primeira?* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Primeiro, a *diferença:* [p=0.2] seis menos quatro, [p=0.2] *dois.* [p=0.4] {b}A "
        "diferença vira expoente: [p=0.2] dez ao quadrado, [p=0.2] *cem vezes.* [p=0.4] {c}E é a primeira que tem "
        "mais, [p=0.2] porque tem o pê agá *menor.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] numa escala de base dez, [p=0.2] a diferença de "
        "leitura é o expoente da razão. [p=0.5] {b}Dois: [p=0.2] menor pê agá, mais ácido: [p=0.2] cada unidade a "
        "menos é dez vezes mais agá mais. [p=0.5] {c}Três: [p=0.2] se a concentração é k vezes dez elevado a menos n, "
        "[p=0.2] o pê agá fica entre n menos um e n."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] pê agá dois e pê agá cinco, [p=0.2] *três vezes* "
        "mais ácido. [p=0.3] {b}Parece certo, [p=0.2] porque os passos da régua são iguais, [p=0.2] e subtrair parece "
        "natural. [p=0.3] {c}Mas cada passo é um *vezes dez:* [p=0.2] dez ao cubo, [p=0.2] *mil vezes.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] pê agá *maior,* [p=0.2] *mais ácido.* [p=0.3] {b}Parece certo, [p=0.2] porque número "
        "maior costuma significar *mais.* [p=0.3] {c}Mas o *menos* da fórmula inverte tudo: [p=0.2] pê agá maior é "
        "*menos* agá mais."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] log de dois vezes dez elevado a menos cinco [p=0.2] igual a log de dois *vezes* menos "
        "cinco. [p=0.3] {b}Parece certo, [p=0.2] porque tem um *vezes* lá dentro. [p=0.3] {c}Mas log do produto é "
        "*soma:* [p=0.2] zero vírgula trinta *menos cinco.* [p=0.3] O jeito errado daria pê agá um e meio, [p=0.2] "
        "fora da faixa de quatro a cinco."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="23", block="q1", text=
        "{t}Agora, questões do nosso material. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um suco "
        "industrializado tem *pê agá três,* [p=0.2] e uma amostra de água de chuva, [p=0.2] *pê agá seis.* [p=0.3] A "
        "concentração de agá mais no suco [p=0.2] é, em relação à da chuva: [p=0.4] {qa}A: [p=0.2] duas vezes maior. "
        "[p=0.3] {qb}B: [p=0.2] três vezes. [p=0.3] {qc}C: [p=0.2] trinta vezes. [p=0.3] {qd}D: [p=0.2] mil vezes. "
        "[p=0.3] {qe}E: [p=0.2] um milhão de vezes."),
    dict(id="24", block="q1", text=
        "{t}Que tipo de pergunta é essa? [p=0.2] *Comparar* duas leituras. [p=0.4] {a}Primeiro, a diferença: [p=0.2] "
        "seis menos três, [p=0.2] *três.* [p=0.4] {b}Dez elevado a menos três [p=0.2] dividido por dez elevado a menos "
        "seis: [p=0.2] *dez ao cubo,* mil. [p=0.4] {c}Faz sentido? [p=0.2] O suco tem o pê agá *menor,* [p=0.2] então "
        "é ele que tem mais agá mais. [p=0.3] {ok}*Letra D!*"),
    dict(id="25", block="q1", text=
        "{t}E as outras? [p=0.3] {xa}A A [p=0.2] *divide* os pê agás: [p=0.2] seis por três. [p=0.4] {xb}A B [p=0.2] "
        "subtrai e *para* na diferença. [p=0.4] {xc}A C [p=0.2] *multiplica* a diferença por dez, [p=0.2] em vez de "
        "usar como expoente. [p=0.4] {xe}E a E [p=0.2] usa só o pê agá da chuva como expoente, [p=0.2] *esquecendo o "
        "suco.*"),

    # ================= QUESTÃO 2 (NÓS FAZEMOS) =================
    dict(id="26", block="q2", text=
        "{t}Esta a gente faz junto. [p=0.3] {a}Uma estação coletou chuva com concentração de agá mais [p=0.2] de *dois "
        "vezes dez elevado a menos quatro* mol por litro. [p=0.3] Com log de dois igual a zero vírgula trinta, [p=0.2] "
        "o pê agá é: [p=0.4] {qa}A: [p=0.2] três vírgula quatro. [p=0.3] {qb}B: [p=0.2] três vírgula sete. [p=0.3] "
        "{qc}C: [p=0.2] quatro. [p=0.3] {qd}D: [p=0.2] quatro vírgula três. [p=0.3] {qe}E: [p=0.2] quatro vírgula seis. "
        "[p=0.4] {p}Antes da conta: [p=0.2] o atalho diz que o pê agá fica entre quanto e quanto? [p=1.5]"),
    dict(id="27", block="q2", text=
        "{t}Entre *três e quatro.* [p=0.2] Já caem a C, a D e a E. [p=0.4] {a}Agora, a conta: [p=0.2] log do produto é "
        "soma, [p=0.2] zero vírgula trinta *mais* menos quatro, [p=0.2] *menos três vírgula sete.* [p=0.4] {b}O menos "
        "da fórmula vira o sinal: [p=0.2] pê agá *três vírgula sete.* [p=0.3] {c}Mais perto de quatro, [p=0.2] porque "
        "o dois é pequeno. [p=0.3] {ok}*Letra B!*"),
    dict(id="28", block="q2", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] desconta *duas vezes* o log de dois, [p=0.2] como se fosse quatro "
        "vezes dez elevado a menos quatro. [p=0.4] {xc}A C [p=0.2] *ignora* o dois. [p=0.4] {xd}A D [p=0.2] *soma* o "
        "log de dois: [p=0.2] erro no sinal. [p=0.4] {xe}E a E [p=0.2] erra o sinal [p=0.2] e ainda *dobra* o log de "
        "dois."),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="29", block="q6", text=
        "{t}E esta é *sua.* [p=0.3] {a}Recomenda-se que o pê agá de uma piscina [p=0.2] fique *entre sete vírgula dois "
        "e sete vírgula oito.* [p=0.3] A *maior* "
        "concentração de agá mais admitida é: [p=0.4] {qa}A: [p=0.2] dez elevado a menos sete vírgula oito. [p=0.3] "
        "{qb}B: [p=0.2] dez elevado a menos sete vírgula dois. [p=0.3] {qc}C: [p=0.2] dez elevado a menos zero vírgula "
        "seis. [p=0.3] {qd}D: [p=0.2] dez elevado a sete vírgula dois. [p=0.3] {qe}E: [p=0.2] dez elevado a sete "
        "vírgula oito. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="30", block="q6", text=
        "{t}Conferindo. [p=0.3] {a}Maior concentração [p=0.2] é *menor pê agá:* [p=0.2] o menor da faixa é *sete "
        "vírgula dois.* [p=0.4] {b}Então, dez elevado a *menos sete vírgula dois.* [p=0.4] {c}Confira: [p=0.2] menos "
        "sete vírgula dois é *maior* que menos sete vírgula oito, [p=0.2] porque está mais perto do zero. [p=0.3] "
        "{ok}*Letra B!*"),
    dict(id="31", block="q6", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] liga maior concentração a *maior* pê agá: [p=0.2] inverteu. [p=0.4] "
        "{xc}A C [p=0.2] usa a *largura* da faixa como expoente. [p=0.4] {xd}A D [p=0.2] {xe}e a E [p=0.2] *esquecem o "
        "sinal de menos:* [p=0.2] dariam mais de *dez milhões* de mol por litro, [p=0.2] um absurdo."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] numa escala de base dez, [p=0.2] a diferença de "
        "leitura é o expoente da razão. [p=0.5] {b}Dois: [p=0.2] menor pê agá, mais ácido: [p=0.2] cada unidade a "
        "menos é dez vezes mais agá mais. [p=0.5] {c}Três: [p=0.2] se a concentração é k vezes dez elevado a menos n, "
        "[p=0.2] o pê agá fica entre n menos um e n."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}Um terremoto de *magnitude sete* [p=0.2] contra um de *magnitude cinco:* [p=0.4] {b}a energia é *duas* "
        "vezes maior? [p=0.3] *Cem* vezes? [p=0.3] *Mil* vezes? [p=0.5] {c}Próximo episódio."),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído no três vezes mais ácido? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
