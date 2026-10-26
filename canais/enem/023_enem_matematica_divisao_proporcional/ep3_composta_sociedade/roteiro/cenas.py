# Roteiro — Divisão Proporcional, Episódio 3 de 5: Divisão composta e regra de sociedade (multiplicar, nunca somar)
# Base: Estudos/Enem/estudos/01-matematica/08-divisao-proporcional.html — seções 06 e 07 (+ Questões 4, 3 e 5 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   PESSOA-DIA é uma unidade combinada, como os homens-hora da série de Razão: 5 pessoas por 2 dias = 10 pessoa-dia, não 7.
#   O RETÂNGULO de quadradinhos: 5 de largura por 2 de altura dão 10 quadradinhos; unidades combinadas só existem multiplicando.
#   Na sociedade, quem manda é o PRODUTO capital × tempo, não cada um sozinho.
# Exemplos (decisão da série): o bloco b) é a própria Questão 4 (R$ 5 600; 2, 3, 5 integrantes; 3, 4, 2 dias), como o usuário
#   desenhou ("eu faço"); a Questão 4 volta depois só como leitura de prova e análise das alternativas.
#   O bloco e) só SIMPLIFICA os capitais da Questão 3 (30 000 : 45 000 : 75 000 = 2 : 3 : 5); a divisão do lucro fica para a questão.
#   O bloco f) NÃO usa os números da Questão 5 ("você faz"): A 10 mil por 6 meses, B 15 mil por 8 meses → 60 000 e 120 000 → 1 : 2;
#   lucro R$ 9 000 → k = 3 000 → 3 000 e 6 000. O bloco g) usa 20 mil × 12 = 30 mil × 8 = 240 000 (o do prompt).
#   Bloco d) (simplificar só depois): pessoas 6 e 8, dias 10 e 5 → produtos 60 e 40 → ÷ 20 → 3 : 2 (erro: parar em 3 : 4, só pessoas).
#   Série inversa no bloco a): pessoas 2 e 3, inversamente às faltas 1 e 3 → inversos 1 e 1/3 → produtos 2 e 1 → 2 : 1.
#   Prejuízo: R$ 10 000 em 2 : 3 : 5 → k = 1 000 → 2 000, 3 000 e 5 000.
# Nós fazemos (prompt): 4 e 6 pessoas, 5 e 2 dias → 20 e 12 → 5 : 3.
# QUESTÃO 4 do material (eu faço): produtos 6, 12, 10 → 28 → k = 200 → 1 200, 2 400, 2 000 → D (2 400). Destaque do material:
#   a equipe maior (5) ficou com menos que a segunda, por ter trabalhado menos dias. Explicações NOSSAS (o material não explica
#   as erradas): A (1 200) = a menor parte, a da primeira equipe; C (2 000) = a equipe de 5 integrantes ("mais gente, mais
#   dinheiro"); E (2 800) = olhou só os integrantes (2 : 3 : 5 → k = 560 → 5 · 560); B (1 600) não sai de caminho coerente.
# QUESTÃO 3 do material (nós fazemos): 2 : 3 : 5 → k = 4 500 → 9 000, 13 500, 22 500 → B. C (15 000) = lucro em partes
#   iguais (material). NOSSAS: A (9 000) e E (22 500) = partes do primeiro e do terceiro (responderam o sócio errado);
#   D (18 000) não sai de peso nenhum: a conferência elimina.
# QUESTÃO 5 do material (você faz): 240 000, 300 000, 120 000 → ÷ 60 000 → 4 : 5 : 2 → k = 3 000 → B = 15 000 → D.
#   NOSSAS: A (6 000) = parte do sócio C; C (12 000) = parte do sócio A; B (11 000) = partes iguais (e também quem olhou só
#   o tempo: 10/30 de 33 000); E (16 500) = a metade do lucro, sem conta coerente.
# Frases-chave (meio e fim, idênticas): 1. Dois critérios? Multiplique, nunca some.
#   2. Unidades combinadas só existem multiplicando. 3. Na sociedade, quem manda é capital vezes tempo.
# Atalhos (verde): "monte o retângulo: um critério é a largura, o outro a altura" · "a ordem: multiplique, simplifique, some,
#   ache o k" · "simplifique os capitais pelo MDC antes de somar" · "capital vezes tempo: corte os zeros iguais".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Divisão composta e regra de sociedade: multiplicar, nunca somar | Divisão Proporcional Ep. 3"
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
        "{a}Dois critérios ao mesmo tempo: [p=0.2] *pessoas* e *dias.* [p=0.5] {b}O instinto manda *somar.* [p=0.5] {c}A "
        "alternativa de quem somou [p=0.2] *sempre* está lá esperando."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai resolver qualquer divisão com *dois critérios* [p=0.4] {b}e qualquer questão "
        "de *sociedade,* [p=0.4] {c}inclusive com sócios que ficaram *tempos diferentes.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Os *pacotinhos,* do episódio um: [p=0.2] some os pesos, [p=0.2] divida "
        "o total pela soma, [p=0.2] e esse é o *k,* [p=0.2] o valor de um pacotinho. [p=0.4] {b}A divisão *inversa,* do "
        "episódio dois: [p=0.2] troque cada número pelo seu *inverso.* [p=0.4] {c}E simplificar pelo *MDC:* [p=0.2] dividir "
        "todos os pesos pelo mesmo número [p=0.2] não muda a divisão."),

    # ================= CONCRETO: A HISTÓRIA =================
    dict(id="04", block="historia", text=
        "{t}Imagine uma verba para duas equipes de um mutirão. [p=0.4] {a}A equipe *Azul* tem *duas* pessoas, [p=0.2] e "
        "trabalhou *três* dias. [p=0.4] {b}A equipe *Verde* tem *cinco* pessoas, [p=0.2] e trabalhou só *dois* dias. [p=0.4] "
        "{c}Quem trabalhou mais? [p=0.3] {d}A Verde tem mais gente. [p=0.2] A Azul ficou mais tempo. [p=0.3] Os dois contam."),
    dict(id="05", block="historia", text=
        "{t}E nos negócios é igual. [p=0.3] {a}Duas amigas abrem uma loja. [p=0.3] Uma coloca *dez mil reais* [p=0.2] e fica "
        "o ano inteiro. [p=0.4] {b}A outra coloca *vinte mil,* [p=0.2] mas sai depois de *três meses.* [p=0.4] {c}Na hora de "
        "dividir o lucro, [p=0.2] quem merece mais? [p=0.3] Hoje você vai saber responder."),

    # ================= BLOCO A: A REGRA =================
    dict(id="06", block="regra", text=
        "{t}Quando a divisão depende de dois critérios, [p=0.2] ela se chama *divisão composta.* [p=0.4] {a}Cada critério vira "
        "uma *série:* [p=0.2] uma lista de números, [p=0.2] na ordem das equipes. [p=0.4] {b}Os *termos correspondentes* são "
        "os da mesma equipe. [p=0.4] {c}E a regra é uma só: [p=0.2] *multiplique* os termos correspondentes. [p=0.3] {d}Os "
        "produtos são os *pesos.*"),
    dict(id="07", block="regra", text=
        "{t}E se um dos critérios for *inverso?* [p=0.3] {a}Por exemplo: [p=0.2] proporcional às pessoas, [p=0.2] dois e "
        "três, [p=0.2] e inversamente às faltas, [p=0.2] um e três. [p=0.4] {b}Primeiro, inverta só a série inversa: [p=0.2] "
        "um e *um terço.* [p=0.4] {c}Depois, multiplique: [p=0.2] dois vezes um, [p=0.2] dois. [p=0.2] Três vezes um terço, "
        "[p=0.2] um. [p=0.3] {d}Pesos *dois e um.*"),

    # ================= BLOCO B: EU FAÇO =================
    dict(id="08", block="eufaco", text=
        "{t}Vamos fazer uma inteira. [p=0.3] {a}*Cinco mil e seiscentos reais* para três equipes. [p=0.3] {b}Integrantes: "
        "[p=0.2] dois, [p=0.2] três [p=0.2] e cinco. [p=0.3] {c}Dias trabalhados: [p=0.2] três, [p=0.2] quatro [p=0.2] e dois. "
        "[p=0.4] {d}Multiplique cada equipe: [p=0.2] dois vezes três, *seis.* [p=0.2] Três vezes quatro, *doze.* [p=0.2] Cinco "
        "vezes dois, *dez.*"),
    dict(id="09", block="eufaco", text=
        "{t}Agora é o procedimento de sempre. [p=0.3] {a}Some os pesos: [p=0.2] seis, mais doze, mais dez, [p=0.2] *vinte e "
        "oito.* [p=0.4] {b}O k: [p=0.2] cinco mil e seiscentos dividido por vinte e oito, [p=0.2] *duzentos.* [p=0.4] {c}As "
        "partes: [p=0.2] mil e duzentos, [p=0.2] dois mil e quatrocentos [p=0.2] e dois mil. [p=0.4] {d}Confira: [p=0.2] somam "
        "*cinco mil e seiscentos.* [p=0.2] Fechou!"),

    # ================= BLOCO C: POR QUE MULTIPLICAR =================
    dict(id="10", block="porque", text=
        "{t}Mas por que multiplicar, [p=0.2] e não somar? [p=0.4] {a}Olhe a terceira equipe: [p=0.2] *cinco pessoas* por *dois "
        "dias.* [p=0.4] {b}Cada pessoa trabalhou dois dias. [p=0.2] São cinco vezes dois: [p=0.2] *dez* dias de trabalho. "
        "[p=0.4] {c}Isso tem nome: [p=0.2] *pessoa-dia.* [p=0.2] É como os homens-hora da série de Razão. [p=0.4] {d}Somando, "
        "[p=0.2] daria *sete.* [p=0.2] E sete não mede nada."),
    dict(id="11", block="porque", text=
        "{t}Pense num *retângulo* de quadradinhos. [p=0.3] {a}Cinco de largura, [p=0.2] dois de altura: [p=0.2] *dez "
        "quadradinhos.* [p=0.4] {b}Pessoa-dia é uma *unidade combinada:* [p=0.2] ela junta dois critérios numa coisa só. "
        "[p=0.4] {c}E unidades combinadas só existem *multiplicando.* [p=0.4] {d}Atalho: [p=0.2] um critério é a largura, "
        "[p=0.2] o outro é a altura. [p=0.2] O peso é a *área.*"),

    # ================= BLOCO D: SIMPLIFICAR DEPOIS =================
    dict(id="12", block="simplificar", text=
        "{t}E dá para simplificar? [p=0.3] Dá, [p=0.2] mas na hora certa. [p=0.4] {a}Pessoas: [p=0.2] seis e oito. [p=0.2] "
        "Dias: [p=0.2] dez e cinco. [p=0.4] {b}Multiplique primeiro: [p=0.2] *sessenta* e *quarenta.* [p=0.4] {c}Agora "
        "simplifique os pesos finais, [p=0.2] dividindo por vinte: [p=0.2] *três e dois.* [p=0.4] {d}Quem simplifica só as "
        "pessoas [p=0.2] chega em três e quatro, [p=0.2] e esquece os dias pelo caminho."),
    dict(id="13", block="simplificar", text=
        "{t}Então guarde a ordem. [p=0.3] {a}*Multiplique.* [p=0.3] {b}*Simplifique.* [p=0.3] {c}*Some* os pesos. [p=0.3] "
        "{d}Ache o *k.* [p=0.3] {e}E multiplique cada peso pelo k. [p=0.3] Simplificar só *depois* de multiplicar."),

    # ================= BLOCO E: REGRA DE SOCIEDADE =================
    dict(id="14", block="sociedade", text=
        "{t}Agora, os negócios. [p=0.3] {a}*Capital* é o dinheiro que cada sócio colocou. [p=0.3] {b}*Lucro* é o que a "
        "empresa ganhou. [p=0.3] {c}E a *regra de sociedade* diz: [p=0.2] o lucro é dividido *proporcionalmente ao capital.* "
        "[p=0.5] {d}Três sócios colocaram trinta mil, [p=0.2] quarenta e cinco mil [p=0.2] e setenta e cinco mil. [p=0.4] "
        "{e}Divida tudo por quinze mil: [p=0.2] pesos *dois, três e cinco.*"),
    dict(id="15", block="sociedade", text=
        "{t}E se der *prejuízo,* [p=0.2] que é quando a empresa perde dinheiro? [p=0.4] {a}Funciona igual. [p=0.3] Quem "
        "colocou mais, [p=0.2] absorve mais da perda. [p=0.4] {b}Um prejuízo de *dez mil,* [p=0.2] com pesos dois, três e "
        "cinco: [p=0.2] k igual a *mil.* [p=0.4] {c}Perdas de dois mil, [p=0.2] três mil [p=0.2] e cinco mil. [p=0.4] {d}Atalho: "
        "[p=0.2] simplifique os capitais pelo *MDC* [p=0.2] antes de somar."),

    # ================= BLOCO F: TEMPOS DIFERENTES =================
    dict(id="16", block="tempos", text=
        "{t}E quando os sócios ficam *tempos diferentes?* [p=0.4] {a}Aí são dois critérios: [p=0.2] capital *e* tempo. [p=0.3] "
        "É uma divisão composta! [p=0.4] {b}O peso de cada sócio é *capital vezes tempo.* [p=0.4] {c}A sócia A colocou *dez "
        "mil* por *seis* meses: [p=0.2] sessenta mil. [p=0.4] {d}A sócia B, *quinze mil* por *oito* meses: [p=0.2] cento e "
        "vinte mil."),
    dict(id="17", block="tempos", text=
        "{t}Simplifique: [p=0.2] sessenta mil e cento e vinte mil [p=0.2] viram *um e dois.* [p=0.4] {a}Lucro de *nove mil:* "
        "[p=0.2] soma dos pesos, três; [p=0.2] k igual a *três mil.* [p=0.4] {b}A recebe três mil. [p=0.2] B recebe *seis mil.* "
        "[p=0.4] {c}Confira: [p=0.2] nove mil. [p=0.2] Fechou! [p=0.4] {d}Atalho: [p=0.2] em capital vezes tempo, [p=0.2] corte "
        "os zeros iguais antes de multiplicar."),

    # ================= BLOCO G: CAPITAL MAIOR =================
    dict(id="18", block="capital", text=
        "{t}Então, capital maior leva sempre mais? [p=0.4] {a}Veja: [p=0.2] *vinte mil* por *doze* meses [p=0.2] dá duzentos "
        "e quarenta mil. [p=0.4] {b}*Trinta mil* por só *oito* meses [p=0.2] dá… [p=0.2] duzentos e quarenta mil também! "
        "[p=0.4] {c}Mesmo peso: [p=0.2] partes *iguais.* [p=0.4] {d}E as amigas do começo? [p=0.2] Dez mil por doze meses, "
        "[p=0.2] cento e vinte mil. [p=0.2] Vinte mil por três meses, [p=0.2] sessenta mil. [p=0.3] {e}Quem colocou *menos* "
        "leva o *dobro.* [p=0.3] Quem manda é o *produto,* [p=0.2] não cada um sozinho."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma verba vai para dois grupos. [p=0.3] {b}O primeiro tem *quatro pessoas* [p=0.2] e trabalhou "
        "*cinco dias.* [p=0.3] {c}O segundo tem *seis pessoas* [p=0.2] e trabalhou *dois dias.* [p=0.4] {d}Quais são os pesos? "
        "[p=0.3] *Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Quatro vezes cinco: [p=0.2] *vinte.* [p=0.3] {b}Seis vezes dois: [p=0.2] *doze.* "
        "[p=0.4] {c}Simplificando por quatro: [p=0.2] *cinco e três.* [p=0.4] {d}Repare: [p=0.2] o grupo menor leva mais, "
        "[p=0.2] porque trabalhou mais dias."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] dois critérios? [p=0.2] Multiplique, [p=0.2] nunca some. "
        "[p=0.5] {b}Dois: [p=0.2] unidades combinadas só existem multiplicando. [p=0.5] {c}Três: [p=0.2] na sociedade, [p=0.2] "
        "quem manda é capital vezes tempo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar* as duas séries. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque os dois critérios contam. [p=0.4] {c}Mas cinco pessoas por dois dias são dez pessoa-dia, [p=0.2] não "
        "sete. [p=0.3] Multiplique."),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] simplificar *uma* série [p=0.2] e esquecer a outra. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "os números ficam pequenos e bonitos. [p=0.4] {c}Mas um critério sumiu da conta. [p=0.3] Multiplique primeiro, "
        "[p=0.2] simplifique depois."),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] dividir o lucro em partes *iguais.* [p=0.4] {b}Parece certo, [p=0.2] porque todos são sócios. "
        "[p=0.4] {c}Mas a regra de sociedade é proporcional ao capital. [p=0.3] Quem colocou mais, [p=0.2] leva mais."),
    dict(id="25", block="erros", text=
        "{a}Quarto: [p=0.2] achar que o capital *maior* sempre leva mais. [p=0.4] {b}Parece certo, [p=0.2] porque dinheiro "
        "maior assusta. [p=0.4] {c}Mas, com tempos diferentes, [p=0.2] o peso é capital vezes tempo. [p=0.3] Faça a conta."),

    # ================= QUESTÃO 4 DO MATERIAL (EU FAÇO) =================
    dict(id="26", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Uma verba de *cinco mil e "
        "seiscentos reais* será distribuída entre três equipes, [p=0.2] proporcionalmente ao número de integrantes de cada "
        "uma, [p=0.2] dois, três e cinco, [p=0.3] {b}e ao número de dias trabalhados, [p=0.2] três, quatro e dois. [p=0.4] "
        "{c}A equipe que receberá a *maior* verba ficará com: [p=0.4] {qa}A: [p=0.2] mil e duzentos reais. [p=0.3] {qb}B: "
        "[p=0.2] mil e seiscentos. [p=0.3] {qc}C: [p=0.2] dois mil. [p=0.3] {qd}D: [p=0.2] dois mil e quatrocentos. [p=0.3] "
        "{qe}E: [p=0.2] dois mil e oitocentos."),
    dict(id="27", block="q4", text=
        "{t}Você já fez essa conta. [p=0.3] {a}Produtos: [p=0.2] seis, doze e dez. [p=0.2] Soma vinte e oito, [p=0.2] k igual "
        "a duzentos. [p=0.4] {b}A maior parte é a do maior peso, [p=0.2] o doze: [p=0.2] *dois mil e quatrocentos.* [p=0.3] "
        "{ok}*Letra D!* [p=0.4] {c}E repare: [p=0.2] a equipe com *mais* gente [p=0.2] ficou com *menos* que a segunda, "
        "[p=0.3] porque trabalhou menos dias. [p=0.3] Somando, [p=0.2] esse efeito sumiria."),
    dict(id="28", block="q4", text=
        "{t}E as outras? [p=0.3] {xa}A A é a menor parte, [p=0.2] a da primeira equipe. [p=0.4] {xc}A C é a equipe de cinco "
        "pessoas: [p=0.2] mais gente, [p=0.2] mais dinheiro? [p=0.2] Não. [p=0.4] {xe}A E olhou *só* os integrantes. [p=0.4] "
        "{xb}E a B não sai de nenhum caminho certo."),

    # ================= QUESTÃO 3 DO MATERIAL (NÓS FAZEMOS) =================
    dict(id="29", block="q3", text=
        "{t}Mais uma, [p=0.2] e essa a gente faz junto. [p=0.3] {a}Três sócios investiram *trinta mil,* [p=0.2] *quarenta e "
        "cinco mil* [p=0.2] e *setenta e cinco mil* reais na abertura de uma empresa. [p=0.4] {b}Ao fim do primeiro ano, "
        "[p=0.2] o lucro de *quarenta e cinco mil* foi dividido proporcionalmente ao capital investido. [p=0.3] {c}O "
        "*segundo* sócio recebeu: [p=0.4] {qa}A: [p=0.2] nove mil. [p=0.3] {qb}B: [p=0.2] treze mil e quinhentos. [p=0.3] "
        "{qc}C: [p=0.2] quinze mil. [p=0.3] {qd}D: [p=0.2] dezoito mil. [p=0.3] {qe}E: [p=0.2] vinte e dois mil e quinhentos."),
    dict(id="30", block="q3", text=
        "{t}Os pesos você já conhece: [p=0.2] *dois, três e cinco.* [p=0.4] {a}Soma: [p=0.2] dez. [p=0.3] {b}k: [p=0.2] "
        "quarenta e cinco mil dividido por dez, [p=0.2] *quatro mil e quinhentos.* [p=0.4] {c}O segundo sócio tem peso três: "
        "[p=0.2] *treze mil e quinhentos.* [p=0.3] {ok}*Letra B!* [p=0.4] {d}Confira: [p=0.2] nove mil, mais treze mil e "
        "quinhentos, mais vinte e dois mil e quinhentos: [p=0.2] *quarenta e cinco mil.* [p=0.2] Fechou!"),
    dict(id="31", block="q3", text=
        "{t}E as outras? [p=0.3] {xc}A C dividiu o lucro em partes *iguais,* [p=0.2] ignorando os capitais. [p=0.4] {xa}A A "
        "e {xe}a E são as partes do primeiro e do terceiro: [p=0.2] responderam o sócio errado. [p=0.4] {xd}E a D não sai de "
        "peso nenhum: [p=0.2] a conferência elimina."),

    # ================= QUESTÃO 5 DO MATERIAL (VOCÊ FAZ) =================
    dict(id="32", block="q5", text=
        "{t}Agora é com você. [p=0.3] {a}Em uma sociedade, [p=0.2] o sócio A entrou com *vinte mil reais* [p=0.2] e permaneceu "
        "*doze* meses; [p=0.3] {b}o sócio B, com *trinta mil,* [p=0.2] por *dez* meses; [p=0.3] {c}e o sócio C, com *quinze "
        "mil,* [p=0.2] por *oito* meses. [p=0.4] {d}O lucro de *trinta e três mil* foi dividido proporcionalmente ao capital "
        "e ao tempo de permanência. [p=0.3] {e}O sócio *B* recebeu: [p=0.4] {qa}A: [p=0.2] seis mil. [p=0.3] {qb}B: [p=0.2] "
        "onze mil. [p=0.3] {qc}C: [p=0.2] doze mil. [p=0.3] {qd}D: [p=0.2] quinze mil. [p=0.3] {qe}E: [p=0.2] dezesseis mil "
        "e quinhentos. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="33", block="q5", text=
        "{t}Vamos resolver. [p=0.3] {a}Peso é capital vezes tempo: [p=0.2] duzentos e quarenta mil, [p=0.2] trezentos mil "
        "[p=0.2] e cento e vinte mil. [p=0.4] {b}Dividindo por sessenta mil: [p=0.2] *quatro, cinco e dois.* [p=0.4] {c}Soma "
        "onze. [p=0.2] k: [p=0.2] trinta e três mil dividido por onze, [p=0.2] *três mil.* [p=0.4] {d}O sócio B tem peso "
        "cinco: [p=0.2] *quinze mil.* [p=0.3] {ok}*Letra D!* [p=0.4] {e}Confira: [p=0.2] doze mil, mais quinze mil, mais seis "
        "mil: [p=0.2] *trinta e três mil.* [p=0.2] Fechou!"),
    dict(id="34", block="q5", text=
        "{t}E as outras? [p=0.3] {xa}A A é a parte do sócio C, [p=0.2] {xc}e a C é a do sócio A: [p=0.2] sócio errado. "
        "[p=0.4] {xb}A B dividiu em partes *iguais.* [p=0.4] {xe}E a E é a metade do lucro: [p=0.2] não sai de conta "
        "nenhuma."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="35", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] dois critérios? [p=0.2] Multiplique, [p=0.2] nunca "
        "some. [p=0.5] {b}Dois: [p=0.2] unidades combinadas só existem multiplicando. [p=0.5] {c}Três: [p=0.2] na sociedade, "
        "[p=0.2] quem manda é capital vezes tempo."),

    # ================= PONTE E CTA =================
    dict(id="36", block="ponte", text=
        "{a}O ENEM às vezes monta uma questão [p=0.2] com cara de divisão proporcional [p=0.3] {b}em que a proporção *não vale "
        "sobre o total.* [p=0.4] {c}Próximo episódio."),
    dict(id="37", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também tinha o instinto de somar? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
