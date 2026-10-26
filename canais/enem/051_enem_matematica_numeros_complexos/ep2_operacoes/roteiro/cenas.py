# Roteiro — Números Complexos, Episódio 2 de 5: as operações (soma, produto, conjugado, divisão e igualdade)
# Base: Estudos/Enem/estudos/01-matematica/36-numeros-complexos.html — seções 04 e 05 + Questões 2, 3 e 9.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   FRUTAS COM FRUTAS: maçã com maçã, banana com banana → real com real, imaginária com imaginária.
#   O PEDÁGIO: trate i como x e, no fim, pague o pedágio: todo i² vira −1 e muda de time, indo para a parte real.
#   O ESPELHO: o conjugado troca só o sinal da parte imaginária.
#   O ANDAR DE BAIXO LIMPO: dividir é multiplicar em cima e embaixo pelo conjugado do denominador; embaixo fica real.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: i² = −1 (episódio 1); distributiva 2 × 2 = 4 produtos (Expressões algébricas);
#   multiplicar em cima e embaixo pelo mesmo número não muda a fração (Frações); sistema 2 × 2 (Sistemas).
# Exemplos do prompt nos blocos: (1 + 2i)(3 − i) = 5 + 5i · (5 + 5i) ÷ (3 − i) = 1 + 2i · (a + 2i)(1 + i) da seção 05.
# Exemplos NOSSOS (marcados):
#   - bloco c: 3 + 4i → conjugado 3 − 4i, oposto −3 − 4i, z·z̄ = 25 e z + z̄ = 6;
#   - bloco f: z + 2z̄ = 6 + i → 3a − bi = 6 + i → z = 2 − i (a Q9 é "você faz"; o prompt não dava exemplo);
#   - erro 2: (5 + 5i) ÷ (3 − i) parte por parte dá 5/3 − 5 (certo 1 + 2i); o "parece certo" usa (6 + 4i) ÷ 2 = 3 + 2i.
# Acréscimos NOSSOS (marcados): cenas verdes de ATALHO "na subtração, troque os sinais do segundo antes",
#   "parte real = ac − bd, parte imaginária = ad + bc", "o andar de baixo vira a² + b², direto" e
#   "troque z por a + bi e z̄ por a − bi; uma equação vira duas".
# RESSALVA: o resultado do bloco d (1 + 2i, desenho do prompt) é o mesmo da Q3 (nós fazemos). Mantido; na Q3 o que é
#   novo é a conta com 1 − i e as alternativas erradas.
# QUESTÃO 2 (eu faço): 2 − 2i + 3i − 3i² = 5 + i (A). Erradas = material (B i² = 1 → −1 + i; C só correspondentes
#   → 2 − 3i; D sinal dos termos em i → 5 − i; E é a soma z + w = 3 + 2i).
# QUESTÃO 3 (nós fazemos): × (1 + i): (2 + 4i) ÷ 2 = 1 + 2i (E). Conferência (1 + 2i)(1 − i) = 3 + i. Erradas = material
#   (A esquece ÷ 2; B parte por parte 3 ÷ 1 e 1 ÷ (−1); C troca as partes; D divide só a parte real).
# QUESTÃO 9 (você faz, com pausa): 3a + bi = 6 − 2i → a = 2, b = −2 → 2 − 2i (E). Conferência 2(2 − 2i) + (2 + 2i) = 6 − 2i.
#   Erradas = material (A erra o sinal de b; B trata z̄ como z: 3z = 6 − 2i; C conjugado −a + bi; D só o 2z na parte real).
# Nós fazemos (prompt): (4 − i)(2 + 3i) = 11 + 10i; conjugado de −2 + 5i = −2 − 5i.
# Frases-chave (meio e fim, idênticas): 1. Trate i como letra e troque i² por −1 no fim. 2. Conjugado: só a parte
#   imaginária troca de sinal. 3. Na divisão, multiplique em cima e embaixo pelo conjugado do denominador.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.
#   Na tela: parte REAL em azul, parte IMAGINÁRIA em roxo.

TITULO = "Operações com números complexos: produto, conjugado e divisão | Números Complexos Ep. 2"
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
        "{a}*Dois mais três i,* [p=0.2] vezes *um menos i,* [p=0.2] dá *cinco mais i.* [p=0.5] {b}Quem esquece que *i ao "
        "quadrado é menos um* [p=0.2] marca *menos um mais i,* [p=0.3] {c}e essa alternativa está lá *esperando.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o segundo episódio da série de *Números complexos.* [p=0.4] {a}Ao final, [p=0.2] você vai *somar, "
        "multiplicar e dividir* complexos [p=0.3] {b}e resolver *equações com z e o conjugado de z.*"),
    dict(id="03", block="prereq", text=
        "{t}Quatro lembretes. [p=0.3] {a}Episódio um: [p=0.2] *i ao quadrado é menos um.* [p=0.4] {b}Expressões "
        "algébricas: [p=0.2] dois termos vezes dois termos [p=0.2] dão *quatro produtos.* [p=0.4] {c}Frações: [p=0.2] "
        "multiplicar *em cima e embaixo* pelo mesmo número [p=0.2] *não muda* a fração. [p=0.4] {d}Sistemas: [p=0.2] "
        "*duas equações,* *duas incógnitas.*"),

    # ================= CONCRETO: FRUTAS COM FRUTAS =================
    dict(id="04", block="frutas", text=
        "{t}Comece pela feira. [p=0.3] {a}*Duas maçãs e três bananas,* [p=0.2] mais *uma maçã e menos cinco bananas.* "
        "[p=0.4] {b}Maçã com maçã: [p=0.2] *três.* [p=0.2] Banana com banana: [p=0.2] três menos cinco, [p=0.2] *menos "
        "duas.* [p=0.4] {c}Agora troque banana por *i:* [p=0.2] dois mais três i, [p=0.2] mais um menos cinco i, "
        "[p=0.2] dá *três menos dois i.* [p=0.4] {d}Parte *real* com real; [p=0.2] parte *imaginária,* a do i, [p=0.2] "
        "com imaginária."),

    # ================= BLOCO A: SUBTRAÇÃO =================
    dict(id="05", block="subtracao", text=
        "{t}E na *subtração?* [p=0.4] {a}Dois mais três i, [p=0.2] *menos* um menos cinco i. [p=0.4] {b}O sinal de menos "
        "entra nas *duas* partes: [p=0.2] menos um, [p=0.2] e menos com menos cinco i [p=0.2] vira *mais cinco i.* "
        "[p=0.4] {c}Dois menos um, *um.* [p=0.2] Três i mais cinco i, *oito i.* [p=0.2] Resultado: [p=0.2] *um mais oito "
        "i.*"),
    dict(id="06", block="atalho_soma", text=
        "{t}Atalho. [p=0.4] {a}Na subtração, [p=0.2] *troque os sinais* do segundo número antes. [p=0.4] {b}Depois é só "
        "somar: [p=0.2] *real com real,* [p=0.2] *imaginária com imaginária.*"),

    # ================= BLOCO B: MULTIPLICAÇÃO E O PEDÁGIO =================
    dict(id="07", block="mult", text=
        "{t}E para *multiplicar?* [p=0.4] {a}Vamos fazer *um mais dois i,* [p=0.2] vezes *três menos i.* [p=0.4] {b}Trate "
        "o i como se fosse um *x* [p=0.2] e use a distributiva: [p=0.2] *todos com todos.* [p=0.4] {c}Três, "
        "[p=0.2] menos i, [p=0.3] {d}mais seis i, [p=0.2] menos *dois i ao quadrado.*"),
    dict(id="08", block="pedagio", text=
        "{t}E aquele *i ao quadrado?* [p=0.4] {a}Agora vem o *pedágio:* [p=0.2] todo i ao quadrado vira *menos um.* "
        "[p=0.4] {b}Menos dois vezes menos um: [p=0.2] *mais dois.* [p=0.2] E ele *muda de time:* [p=0.2] pula para a "
        "*parte real.* [p=0.4] {c}Real: [p=0.2] três mais dois, *cinco.* [p=0.2] Imaginária: [p=0.2] menos i mais seis i, "
        "*cinco i.* [p=0.3] {d}*Cinco mais cinco i.*"),
    dict(id="09", block="atalho_mult", text=
        "{t}Atalho. [p=0.4] {a}Em a mais b i, vezes c mais d i, [p=0.2] a parte real é *a vezes c, menos b vezes d.* "
        "[p=0.4] {b}A imaginária é *a vezes d, mais b vezes c.* [p=0.4] {c}Aqui: [p=0.2] três mais dois, *cinco;* [p=0.2] menos um mais seis, *cinco.* [p=0.2] Bateu."),

    # ================= BLOCO C: O CONJUGADO =================
    dict(id="10", block="conjugado", text=
        "{t}E o que é o tal do *conjugado?* [p=0.4] {a}O *conjugado* de a mais b i [p=0.2] é *a menos b i.* [p=0.3] É "
        "o *espelho:* [p=0.2] troca *só* o sinal da parte imaginária. [p=0.4] {b}O nome: [p=0.2] *z barra,* [p=0.2] um z com "
        "tracinho em cima. [p=0.4] {c}O conjugado de *três mais quatro i* [p=0.2] é *três "
        "menos quatro i.* [p=0.4] {d}Já *menos três menos quatro i* é o *oposto,* [p=0.2] que troca tudo."),
    dict(id="11", block="conj_prop", text=
        "{t}E para que serve o espelho? [p=0.4] {a}Três mais quatro i, vezes "
        "três menos quatro i. [p=0.4] {b}Os termos com i *se cancelam:* [p=0.2] nove mais dezesseis, [p=0.2] "
        "*vinte e cinco.* [p=0.3] Um número *real.* [p=0.4] {c}A regra: [p=0.2] *z vezes z barra* é *a ao quadrado mais "
        "b ao quadrado,* [p=0.2] sempre real, [p=0.2] e nunca negativo. [p=0.4] {d}E *z mais z barra* [p=0.2] é *dois "
        "a:* [p=0.2] aqui, *seis.*"),

    # ================= BLOCO D: A DIVISÃO =================
    dict(id="12", block="divisao", text=
        "{t}E como se *divide* por um número com i? [p=0.4] {a}Vamos dividir *cinco mais cinco i* [p=0.2] por *três menos "
        "i.* [p=0.4] {b}O problema é o *i no andar de baixo.* [p=0.4] {c}A saída: [p=0.2] multiplique *em cima e "
        "embaixo* [p=0.2] pelo *conjugado* do denominador, [p=0.2] *três mais i.* [p=0.3] Mesmo número nos dois andares: [p=0.2] a "
        "fração *não muda.*"),
    dict(id="13", block="divisao", text=
        "{t}Primeiro, o andar de cima. [p=0.4] {a}Cinco mais cinco i, vezes três mais i: [p=0.2] quinze, "
        "mais cinco i, mais quinze i, [p=0.2] mais cinco i ao quadrado. [p=0.4] {b}Pedágio: [p=0.2] vira *menos cinco.* "
        "[p=0.2] Fica *dez mais vinte i.* [p=0.4] {c}Embaixo: [p=0.2] nove mais um, [p=0.2] *dez.* [p=0.3] {d}*Andar de baixo limpo!* [p=0.4] {e}Dez mais "
        "vinte i, dividido por dez: [p=0.2] *um mais dois i.*"),
    dict(id="14", block="divisao_conf", text=
        "{t}E como ter certeza? [p=0.4] {a}*Multiplique de volta:* [p=0.2] um mais dois i, vezes três menos i. [p=0.4] "
        "{b}Essa conta você já fez: [p=0.2] dá *cinco mais cinco i.* [p=0.2] O número do começo."),
    dict(id="15", block="atalho_div", text=
        "{t}Atalho. [p=0.4] {a}O andar de baixo vira *a ao "
        "quadrado mais b ao quadrado:* [p=0.2] nove mais um, *dez,* direto. [p=0.4] {b}E no fim, [p=0.2] *multiplique de "
        "volta.*"),

    # ================= BLOCO E: IGUALDADE =================
    dict(id="16", block="igualdade", text=
        "{t}E quando dois complexos são *iguais?* [p=0.4] {a}*Igualdade de complexos:* [p=0.2] a mais b i é igual a c "
        "mais d i [p=0.2] *só se* a for igual a c, [p=0.2] *e* b for igual a d. [p=0.4] {b}Por isso, [p=0.2] *uma "
        "equação complexa vale por duas* equações reais. [p=0.4] {c}E *imaginário "
        "puro* [p=0.2] é o de parte real *zero* [p=0.2] e imaginária *não nula,* [p=0.2] como *cinco i.*"),
    dict(id="17", block="igualdade_ex", text=
        "{t}Exemplo. [p=0.4] {a}Desenvolva *a mais dois i, vezes um mais i.* [p=0.2] Fica *a menos dois,* "
        "[p=0.2] mais *a mais dois* vezes i. [p=0.4] {b}Para o resultado ser *real,* [p=0.2] a parte imaginária some: "
        "[p=0.2] a mais dois é zero, [p=0.2] *a é menos dois.* [p=0.4] {c}Para ser *imaginário puro,* [p=0.2] some a "
        "parte real: [p=0.2] a menos dois é zero, [p=0.2] *a é dois.*"),

    # ================= BLOCO F: EQUAÇÕES COM z E z̄ =================
    dict(id="18", block="eq_z", text=
        "{t}E se a equação tiver *z e z barra?* [p=0.4] {a}Resolva *z mais dois z barra, igual a seis mais i.* [p=0.4] "
        "{b}Escreva z como *a mais b i* [p=0.2] e z barra como *a menos b i.* [p=0.4] {c}Juntando: [p=0.2] *três a, menos b i.* [p=0.4] {d}Iguale as partes: [p=0.2] três a é seis, *a é dois;* "
        "[p=0.2] menos b é um, *b é menos um.* [p=0.3] {e}Então *z é dois menos i.*"),
    dict(id="19", block="atalho_eq", text=
        "{t}Atalho. [p=0.4] {a}Troque *z por a mais b i* [p=0.2] e *z barra por a menos b i.* [p=0.4] {b}Separe as partes: [p=0.2] *uma "
        "equação vira duas.* [p=0.4] {c}E confira: [p=0.2] dois menos i, mais quatro mais dois i: [p=0.2] *seis mais i.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="20", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Calcule *quatro menos i,* [p=0.2] vezes *dois mais três i.* [p=0.4] {b}E escreva o "
        "*conjugado* de *menos dois mais cinco i.* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Oito, [p=0.2] mais doze i, [p=0.2] menos dois i, "
        "[p=0.2] menos *três i ao quadrado.* [p=0.4] {b}Pedágio: [p=0.2] *mais três.* "
        "[p=0.4] {c}Onze, [p=0.2] mais dez i: [p=0.2] *onze mais dez i.* [p=0.4] {d}E o conjugado: [p=0.2] o real *fica,* [p=0.2] o imaginário troca: [p=0.2] *menos dois menos cinco i.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="22", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] trate i como letra e troque i ao quadrado por menos um no "
        "fim. [p=0.5] {b}Dois: [p=0.2] conjugado: [p=0.2] só a parte imaginária troca de sinal. [p=0.5] {c}Três: "
        "[p=0.2] na divisão, multiplique em cima e embaixo pelo conjugado do denominador."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="23", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dois mais três i, vezes um menos i, [p=0.2] igual a "
        "*dois menos três i.* [p=0.4] {b}Parece certo, [p=0.2] porque na *soma* é assim: [p=0.2] real com real, imaginária "
        "com imaginária. [p=0.4] {c}Mas no produto são *quatro* contas, [p=0.2] mais o pedágio: "
        "[p=0.2] *cinco mais i.*"),
    dict(id="24", block="erros", text=
        "{t}Segundo: [p=0.2] dividir *parte por parte.* [p=0.4] {a}Cinco mais cinco i, sobre três menos i, [p=0.2] vira "
        "cinco terços [p=0.2] mais cinco i sobre menos i. [p=0.4] {b}Parece certo, [p=0.2] porque com denominador "
        "*real* funciona: [p=0.2] seis mais quatro i, sobre dois, [p=0.2] é três mais dois i. [p=0.4] {c}Mas com i "
        "*embaixo,* [p=0.2] primeiro limpe o andar de baixo. [p=0.2] O certo é *um mais dois i.*"),
    dict(id="25", block="erros", text=
        "{t}Terceiro: [p=0.2] {a}achar que o conjugado de três mais quatro i [p=0.2] é *menos três menos quatro i.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque *conjugar* soa como *inverter tudo.* [p=0.4] {c}Mas esse é o *oposto.* "
        "[p=0.2] O espelho troca *só* a parte imaginária: [p=0.2] *três menos quatro i.*"),

    # ================= QUESTÃO 2: EU FAÇO =================
    dict(id="26", block="q2", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {a}Em um exercício sobre circuitos, [p=0.2] duas "
        "grandezas são representadas pelos números complexos [p=0.2] *z igual a dois mais três i* [p=0.2] e *w igual a "
        "um menos i.* [p=0.2] O produto z vezes w é: [p=0.3] {qa}A: cinco mais i. [p=0.2] {qb}B: menos um mais i. "
        "[p=0.2] {qc}C: dois menos três i. [p=0.2] {qd}D: cinco menos i. [p=0.2] {qe}E: três mais dois i."),
    dict(id="27", block="q2", text=
        "{t}Essa, [p=0.2] *eu faço.* [p=0.4] {a}Quatro produtos: [p=0.2] dois, [p=0.2] menos dois i, [p=0.2] mais três "
        "i, [p=0.2] menos três i ao quadrado. [p=0.4] {b}Pedágio: [p=0.2] *mais três,* [p=0.2] na parte real. [p=0.4] "
        "{c}Real, *cinco;* [p=0.2] imaginária, *i.* [p=0.3] {d}*Cinco mais i.* [p=0.3] {ok}*Letra A!*"),
    dict(id="28", block="q2", text=
        "{t}E as armadilhas? [p=0.3] {xb}A B usa *i ao quadrado igual a um:* [p=0.2] o menos três i ao quadrado vira menos "
        "três. [p=0.4] {xc}A C multiplica *só* as partes correspondentes. [p=0.4] {xd}A D erra o *sinal* "
        "dos termos em i. [p=0.4] {xe}E a E é a *soma,* [p=0.2] z mais w, [p=0.2] e não o produto."),

    # ================= QUESTÃO 3: NÓS FAZEMOS =================
    dict(id="29", block="q3", text=
        "{t}A próxima, [p=0.2] *nós fazemos.* [p=0.4] {a}O quociente de *três mais i* [p=0.2] por *um menos i,* [p=0.2] "
        "escrito na forma a mais b i, é: [p=0.3] {qa}A: dois mais quatro i. [p=0.2] {qb}B: três menos i. [p=0.2] {qc}C: "
        "dois mais i. [p=0.2] {qd}D: um mais quatro i. [p=0.2] {qe}E: um mais dois i. [p=0.4] {p}Qual é o *espelho* do "
        "denominador? [p=1.5]"),
    dict(id="30", block="q3", text=
        "{t}O espelho de um menos i [p=0.2] é *um mais i.* [p=0.4] {a}Em cima: [p=0.2] três, "
        "mais três i, mais i, mais i ao quadrado: [p=0.2] *dois mais quatro i.* [p=0.4] {b}Embaixo: [p=0.2] um mais um, "
        "[p=0.2] *dois.* [p=0.4] {c}Dois mais quatro i, dividido por dois: "
        "[p=0.2] *um mais dois i.* [p=0.3] {ok}*Letra E!* [p=0.3] {d}Confere: [p=0.2] vezes um menos i, dá *três mais i.*"),
    dict(id="31", block="q3", text=
        "{t}E as erradas? [p=0.3] {xa}A A *esquece* de dividir pelo dois. [p=0.4] {xb}A B divide *parte por parte:* "
        "[p=0.2] três por um, [p=0.2] e um por menos um. [p=0.4] {xc}A C *troca* a parte real com a imaginária. [p=0.4] "
        "{xd}E a D divide por dois *só* a parte real."),

    # ================= QUESTÃO 9: VOCÊ FAZ =================
    dict(id="32", block="q9", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}Sendo z barra o conjugado do número complexo z, [p=0.2] o número que "
        "satisfaz *dois z mais z barra, igual a seis menos dois i,* é: [p=0.3] {qa}A: dois mais dois i. [p=0.2] {qb}B: "
        "dois menos dois terços de i. [p=0.2] {qc}C: seis menos dois terços de i. [p=0.2] {qd}D: três menos dois i. "
        "[p=0.2] {qe}E: dois menos dois i. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="33", block="q9", text=
        "{t}Vamos conferir. [p=0.3] {a}z é a mais b i; [p=0.2] z barra, a menos b i. [p=0.4] "
        "{b}Juntando: [p=0.2] *três a, mais b i.* [p=0.4] {c}Iguale: [p=0.2] três a é seis, *a é dois;* [p=0.2] "
        "*b é menos dois.* [p=0.3] {d}*z é dois menos dois i.* [p=0.3] {ok}*Letra E!* [p=0.3] {e}Confere: [p=0.2] quatro "
        "menos quatro i, mais dois mais dois i, [p=0.2] dá *seis menos dois i.*"),
    dict(id="34", block="q9", text=
        "{t}E as erradas? [p=0.3] {xa}A A erra o *sinal* de b no fim. [p=0.4] {xb}A B trata z barra *como se fosse z:* "
        "[p=0.2] três z igual a seis menos dois i. [p=0.4] {xc}A C escreve o conjugado como *menos a mais b i,* [p=0.2] "
        "trocando o sinal da parte errada. [p=0.4] {xd}E a D só considera o *dois z* na parte real."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="35", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] trate i como letra e troque i ao quadrado por menos "
        "um no fim. [p=0.5] {b}Dois: [p=0.2] conjugado: [p=0.2] só a parte imaginária troca de sinal. [p=0.5] {c}Três: "
        "[p=0.2] na divisão, multiplique em cima e embaixo pelo conjugado do denominador."),

    # ================= PONTE E CTA =================
    dict(id="36", block="ponte", text=
        "{a}E se *três mais quatro i* for um *ponto num mapa?* [p=0.4] {b}A que distância ele está da *origem?* [p=0.4] "
        "{c}E o que acontece com o ponto quando você *multiplica por i?* [p=0.4] {d}*Próximo episódio.*"),
    dict(id="37", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído no pedágio do i ao quadrado? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
