# Roteiro — Juros Simples, Episódio 4 de 5: descobrindo capital, taxa ou tempo (e em quanto tempo o dinheiro dobra)
# Base: Estudos/Enem/estudos/01-matematica/13-juros-simples.html — seção 06 (inclusive "dobra ou triplica")
#   + Questões 3, 8 e 4 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   A MESA DE QUATRO PERNAS: J = C · i · t tem quatro letras; dadas três, a quarta sai dividindo os juros pelas outras duas.
#   O MONTANTE JÁ TEM O CAPITAL DENTRO: triplicar é ganhar DUAS vezes o capital em juros, não três (três pilhas de notas:
#     a primeira é o capital, "já estava lá").
#   A ENTRADA NÃO É EMPRÉSTIMO: a loja só financia o que falta pagar.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos dos blocos (do material/prompt): C = 360 ÷ (0,015 · 8) = 3.000 · i = 240 ÷ 6.000 = 4% a.m. ·
#   t = 400 ÷ 50 = 8 meses · a 4% a.m. dobrar 25 meses e triplicar 50 (= 4 anos e 2 meses).
#   Armadilha da taxa (NOSSA): dividir pelo montante no exemplo dos 240 → 240 ÷ (1.240 · 6) ≈ 3,2% (menor que 4%).
#   Taxa embutida (NOSSO, para não entregar a Q8, que é "nós fazemos"): TV de R$ 2.000,00 à vista ou R$ 500,00 de
#   entrada e R$ 1.590,00 em 3 meses → financiado 1.500; J = 90; i = 90 ÷ 4.500 = 2% a.m.
#   Nós fazemos (prompt): 180 ÷ (1.500 · 4) = 3% a.m.; dobrar a 5% → 0,05 · t = 1 → 20 meses (= 1 ano e 8 meses).
# QUESTÃO 3 (eu faço): J = 300; i = 300 ÷ 12.000 = 2,5% a.m.; anual 30% → E. Erradas (do material): B = a mensal;
#   D = 300 ÷ 1.200, sem dividir pelo tempo (25%); A e C = dividir pelo montante (300 ÷ 15.000 = 2% a.m., 24% a.a.).
# QUESTÃO 8 (nós fazemos): C = 1.000 − 400 = 600; J = 60; i = 60 ÷ 1.200 = 5% a.m. → A. Erradas: D = sem dividir pelos
#   2 meses (10%); B = 60 ÷ 1.000: preço total E sem dividir pelos 2 meses (com a divisão daria 3%, que nem está nas
#   alternativas) — CORREÇÃO DO MATERIAL, que atribui a B só ao "preço total"; C e E = sobre a entrada, com e sem a
#   divisão pelo tempo (60 ÷ 800 = 7,5% e 60 ÷ 400 = 15%).
# QUESTÃO 4 (você faz): J = 2C → 0,02 · t = 2 → 100 meses = 8 · 12 + 4 = 8 anos e 4 meses → C. Erradas (do material):
#   A = tempo para dobrar (50 meses); D = J = 3C (150 meses = 12 anos e 6 meses); B = 8,33 lido como 8 anos e 3 meses;
#   E = taxa mensal tratada como anual (100 anos).
# Atalhos (verde): "a perna que falta = J ÷ (produto das outras duas)" · "a taxa pelos juros de UM mês" ·
#   "tempo para multiplicar por k: (k − 1) ÷ i" · "meses em anos: divisão inteira por 12, o resto são os meses".
# Frases-chave (meio e fim, idênticas): 1. Dadas três letras, a quarta sai dividindo os juros pelas outras duas.
#   2. Triplicar é ganhar duas vezes o capital em juros. 3. A entrada não é empréstimo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Juros simples: descubra capital, taxa ou tempo (e quando o dinheiro dobra) | Juros Simples Ep. 4"
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
        "{a}A *dois por cento ao mês,* [p=0.2] em juros simples, [p=0.2] em quanto tempo o dinheiro *triplica?* "
        "[p=0.5] {b}Quem pensa *três vezes o capital em juros* [p=0.2] responde *doze anos e meio.* [p=0.5] {c}A "
        "resposta é *oito anos e quatro meses.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai descobrir *qualquer uma das quatro letras,* [p=0.3] {b}inclusive a "
        "*taxa escondida* numa compra parcelada [p=0.3] {c}e o *tempo* para dobrar ou triplicar."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] *J igual a C vezes i vezes t,* [p=0.2] e "
        "M igual a C mais J. [p=0.4] {b}Do episódio dois: [p=0.2] taxa e tempo [p=0.2] *na mesma "
        "unidade.* [p=0.4] {c}E do episódio três: [p=0.2] a taxa é o degrau de cada mês [p=0.2] *dividido pelo "
        "capital.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Uma loja anuncia uma geladeira: [p=0.2] *mil reais à vista,* "
        "[p=0.2] ou *quatrocentos de entrada* [p=0.2] e *seiscentos e sessenta* daqui a dois meses. [p=0.3] Quanto de "
        "juros tem aí dentro? [p=0.4] {b}E a pergunta que todo mundo já fez: [p=0.2] *em quanto tempo meu dinheiro "
        "dobra?* [p=0.4] {c}Nas duas, [p=0.2] a conta não pede os juros. [p=0.2] Pede outra letra da fórmula: [p=0.2] "
        "a *incógnita,* [p=0.2] que é só o nome da letra que falta."),

    # ================= BLOCO A: A MESA DE QUATRO PERNAS =================
    dict(id="05", block="mesa", text=
        "{t}E como se acha uma letra que falta? [p=0.4] {a}Pense na fórmula como uma *mesa de quatro pernas:* [p=0.2] "
        "*J,* [p=0.2] *C,* [p=0.2] *i* [p=0.2] e *t.* [p=0.4] {b}Se uma perna some, [p=0.2] você reconstrói com as "
        "outras três. [p=0.4] {c}Isso se chama *isolar:* [p=0.2] deixar a letra que você procura [p=0.2] sozinha de um "
        "lado do igual. [p=0.3] O truque da série de Velocidade, [p=0.2] com quatro letras."),
    dict(id="06", block="mesa", text=
        "{a}Falta o *capital?* [p=0.2] Juros dividido por *i vezes t.* [p=0.4] {b}Falta "
        "a *taxa?* [p=0.2] Juros dividido por *C vezes t.* [p=0.4] {c}Falta o *tempo?* [p=0.2] Juros dividido por *C "
        "vezes i.* [p=0.4] {d}Atalho: [p=0.2] a perna que falta [p=0.2] é *J dividido pelo produto das outras duas.*"),

    # ================= BLOCO B: ACHAR O CAPITAL =================
    dict(id="07", block="capital", text=
        "{t}Quanto foi aplicado, [p=0.2] se rendeu *trezentos e sessenta reais* [p=0.2] em *oito meses,* [p=0.2] a *um "
        "vírgula cinco por cento ao mês?* [p=0.4] {a}Antes de dividir, [p=0.2] etiquete. [p=0.2] *J* é trezentos e "
        "sessenta. [p=0.2] *i* é zero vírgula zero um cinco. [p=0.2] *t* é oito. [p=0.4] {b}As outras duas pernas: "
        "[p=0.2] zero vírgula zero um cinco vezes oito [p=0.2] dá *zero vírgula doze.* [p=0.4] {c}Trezentos e sessenta "
        "dividido por zero vírgula doze: [p=0.2] *três mil reais.* [p=0.4] {d}Confere: [p=0.2] quarenta e cinco por mês, "
        "[p=0.2] vezes oito, [p=0.2] trezentos e sessenta."),

    # ================= BLOCO C: ACHAR A TAXA =================
    dict(id="08", block="taxa", text=
        "{t}E a taxa? [p=0.3] *Mil reais* rendem *duzentos e quarenta* em *seis meses.* [p=0.4] {a}*J* é duzentos e "
        "quarenta. [p=0.2] *C* é mil. [p=0.2] *t* é seis. [p=0.4] {b}C vezes t: [p=0.2] *seis mil.* [p=0.3] Duzentos e "
        "quarenta dividido por seis mil: [p=0.2] *zero vírgula zero quatro,* [p=0.2] *quatro por cento ao mês.* [p=0.4] "
        "{c}Atalho: [p=0.2] ache os juros de *um mês só.* [p=0.2] Duzentos e quarenta em seis meses [p=0.2] são "
        "quarenta por mês. [p=0.2] Quarenta de mil: [p=0.2] *quatro por cento.*"),
    dict(id="09", block="taxa", text=
        "{t}E a armadilha da taxa? [p=0.4] {a}O montante é mil, duzentos e quarenta. [p=0.2] Quem divide por "
        "ele [p=0.2] encontra uns *três vírgula dois por cento.* [p=0.4] {b}Uma taxa *menor* que a real. [p=0.3] {c}Na "
        "taxa, [p=0.2] divida *pelo capital,* [p=0.2] o dinheiro do começo. [p=0.2] *Nunca pelo montante.*"),

    # ================= BLOCO D: ACHAR O TEMPO =================
    dict(id="10", block="tempo", text=
        "{t}E o tempo? [p=0.3] *Dois mil reais* a *dois vírgula cinco por cento ao mês:* [p=0.2] quando rendem "
        "*quatrocentos?* [p=0.4] {a}*J* é quatrocentos. [p=0.2] *C* é dois mil. [p=0.2] *i* é zero vírgula zero dois "
        "cinco. [p=0.4] {b}C vezes i: [p=0.2] *cinquenta reais.* [p=0.3] São os juros de cada mês. [p=0.4] "
        "{c}Quatrocentos dividido por cinquenta: [p=0.2] *oito meses.* [p=0.4] {d}Atalho: [p=0.2] quantas moedinhas de "
        "cinquenta [p=0.2] cabem em quatrocentos?"),

    # ================= BLOCO E: DOBRAR E TRIPLICAR =================
    dict(id="11", block="dobrar", text=
        "{t}E o tal dinheiro que dobra? [p=0.4] {a}*Dobrar* é o montante virar *duas vezes* o capital. [p=0.2] "
        "*Triplicar* é virar *três vezes.* [p=0.4] {b}Olhe as três pilhas de notas do triplo. [p=0.3] A primeira é o "
        "*capital:* [p=0.2] ela já estava lá. [p=0.4] {c}Só as outras duas são juros. [p=0.3] O montante já tem o "
        "capital dentro: [p=0.2] *triplicar é ganhar duas vezes o capital em juros,* [p=0.2] não três."),
    dict(id="12", block="dobrar", text=
        "{t}E a conta? [p=0.4] {a}Dobrar: [p=0.2] *J igual a C.* [p=0.2] Triplicar: [p=0.2] *J igual a dois C.* [p=0.4] "
        "{b}Na fórmula, [p=0.2] o *C* aparece dos dois lados [p=0.2] e *se cancela.* [p=0.2] Sobra só *i vezes t.* "
        "[p=0.4] {c}Para multiplicar por *k,* [p=0.2] *i vezes t igual a k menos um.* [p=0.4] {d}A quatro por cento ao "
        "mês: [p=0.2] dobrar é zero vírgula zero quatro vezes t igual a um: [p=0.2] *vinte e cinco meses.* [p=0.3] "
        "Triplicar é igual a dois: [p=0.2] *cinquenta meses.*"),
    dict(id="13", block="dobrar", text=
        "{t}E cinquenta meses são quantos anos? [p=0.4] {a}Divisão inteira por doze: [p=0.2] quatro vezes doze é "
        "quarenta e oito. [p=0.2] Sobram *dois.* [p=0.4] {b}*Quatro anos e dois meses.* [p=0.4] {c}Atalho: [p=0.2] "
        "tempo para multiplicar por *k* [p=0.2] é *k menos um, dividido pela taxa.* "),

    # ================= BLOCO F: A TAXA EMBUTIDA =================
    dict(id="14", block="embutida", text=
        "{t}E a taxa escondida na compra parcelada? [p=0.4] {a}A *entrada* é o que você paga *no ato.* [p=0.4] {b}O *valor financiado* é o que a loja realmente empresta: [p=0.2] o preço à vista "
        "*menos* a entrada. [p=0.4] {c}E a *taxa embutida* [p=0.2] é a taxa de juros que vem escondida no preço a "
        "prazo. [p=0.4] {d}A entrada não é empréstimo: [p=0.2] a loja só financia o que falta pagar."),
    dict(id="15", block="embutida", text=
        "{t}Um exemplo. [p=0.3] {a}Uma TV: [p=0.2] *dois mil à vista,* [p=0.2] ou *quinhentos de entrada* [p=0.2] e "
        "*mil, quinhentos e noventa* em três meses. [p=0.4] {b}Financiado: [p=0.2] dois mil menos quinhentos, "
        "[p=0.2] *mil e quinhentos.* [p=0.2] Juros: [p=0.2] *noventa.* [p=0.4] {c}Taxa: [p=0.2] noventa dividido por mil e quinhentos vezes três, [p=0.2] *dois "
        "por cento ao mês.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*Mil e quinhentos reais* renderam *cento e oitenta* [p=0.2] em *quatro meses,* "
        "[p=0.2] a juros simples. [p=0.2] Qual é a *taxa mensal?* [p=0.4] {b}E, numa outra aplicação a *cinco por "
        "cento ao mês,* [p=0.2] em quanto tempo um capital *dobraria?* [p=0.3] *Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}A taxa: [p=0.2] C vezes t é mil e quinhentos vezes quatro, [p=0.2] *seis mil.* "
        "[p=0.2] Cento e oitenta dividido por seis mil: [p=0.2] *zero vírgula zero três,* [p=0.2] *três por cento ao "
        "mês.* [p=0.4] {b}Dobrar a cinco por cento: [p=0.2] *J igual a C,* [p=0.2] então zero vírgula zero cinco vezes "
        "t igual a um. [p=0.3] {c}*Vinte meses:* [p=0.2] um ano e oito meses."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] dadas três letras, [p=0.2] a quarta sai dividindo os "
        "juros pelas outras duas. [p=0.5] {b}Dois: [p=0.2] triplicar é ganhar duas vezes o capital em juros. [p=0.5] "
        "{c}Três: [p=0.2] a entrada não é empréstimo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar a taxa dividindo pelo *montante.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o montante é o número que salta do enunciado. [p=0.4] "
        "{c}Mas a taxa é sempre sobre o *capital.* [p=0.2] Pelo montante, [p=0.2] ela sai *menor* que a real."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] triplicar com *J igual a três C.* [p=0.4] {b}Parece certo, [p=0.2] porque a palavra é "
        "*triplicar.* [p=0.4] {c}Mas o capital já está no montante: [p=0.2] *J igual a dois C.* [p=0.2] Com três C, "
        "[p=0.2] o tempo sai *cinquenta por cento maior.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] cem meses dividido por doze [p=0.2] dá oito vírgula trinta e três. [p=0.2] E alguém lê: "
        "[p=0.2] *oito anos e três meses.* [p=0.4] {b}Parece certo, [p=0.2] porque o três está ali, depois da "
        "vírgula. [p=0.4] {c}Mas zero vírgula trinta e três *ano* [p=0.2] vezes doze [p=0.2] são *quatro meses.* "
        "[p=0.2] Use a divisão inteira: [p=0.2] oito vezes doze, noventa e seis, [p=0.2] sobram quatro."),
    dict(id="22", block="erros", text=
        "{a}Quarto: [p=0.2] incluir a *entrada* no valor financiado. [p=0.4] {b}Parece certo, [p=0.2] porque a "
        "entrada também faz parte do preço. [p=0.4] {c}Mas ela é paga no ato. [p=0.2] O capital é o preço à vista "
        "*menos* a entrada."),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="23", block="q3", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Eu resolvo com você. "
        "[p=0.4] {a}Um capital de *mil e duzentos reais,* [p=0.2] aplicado a juros simples, [p=0.2] gerou um montante "
        "de *mil e quinhentos reais* [p=0.2] após *dez meses.* [p=0.2] A taxa *anual* de juros dessa aplicação foi de: "
        "[p=0.4] {qa}A: [p=0.2] dois por cento. [p=0.3] {qb}B: [p=0.2] dois vírgula cinco por cento. [p=0.3] {qc}C: "
        "[p=0.2] vinte e quatro por cento. [p=0.3] {qd}D: [p=0.2] vinte e cinco por cento. [p=0.3] {qe}E: [p=0.2] "
        "trinta por cento."),
    dict(id="24", block="q3", text=
        "{t}Etiquetas. [p=0.3] {a}*C* é mil e duzentos. [p=0.2] *M* é mil e quinhentos. [p=0.2] *t* é dez "
        "meses. [p=0.2] Falta a perna *i.* [p=0.4] {b}Os juros: [p=0.2] mil e quinhentos menos mil e duzentos, "
        "[p=0.2] *trezentos.* [p=0.4] {c}C vezes t: [p=0.2] *doze mil.* [p=0.2] Trezentos dividido por doze mil: "
        "[p=0.2] *dois vírgula cinco por cento ao mês.* [p=0.4] {d}Mas a pergunta é a taxa *anual:* [p=0.2] dois "
        "vírgula cinco vezes doze, [p=0.2] *trinta por cento ao ano.* [p=0.3] {ok}*Letra E!*"),
    dict(id="25", block="q3", text=
        "{t}E as outras? [p=0.3] {xb}A B é a taxa *mensal* certa, [p=0.2] mas a pergunta era a anual. [p=0.4] {xd}A D "
        "é trezentos dividido por mil e duzentos, [p=0.2] *sem dividir pelo tempo.* [p=0.4] {xa}A A [p=0.2] {xc}e a C "
        "[p=0.2] dividem pelo *montante:* [p=0.2] dois por cento ao mês, [p=0.2] vinte e quatro ao ano."),

    # ================= QUESTÃO 8 (NÓS FAZEMOS) =================
    dict(id="26", block="q8", text=
        "{t}Agora, a geladeira do começo da aula. [p=0.2] Essa a gente faz junto. [p=0.4] {a}Uma loja vende uma "
        "geladeira por *mil reais à vista* [p=0.2] ou, a prazo, [p=0.2] com entrada de *quatrocentos reais* [p=0.2] e "
        "um pagamento de *seiscentos e sessenta reais* [p=0.2] dois meses após a compra. [p=0.2] Considerando juros "
        "simples, [p=0.2] a taxa *mensal* cobrada é de: [p=0.4] {qa}A: [p=0.2] cinco por cento. [p=0.3] {qb}B: "
        "[p=0.2] seis. [p=0.3] {qc}C: [p=0.2] sete vírgula cinco. [p=0.3] {qd}D: [p=0.2] dez. [p=0.3] {qe}E: [p=0.2] "
        "quinze por cento. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q8", text=
        "{t}Vamos juntos, [p=0.2] pela linha do tempo. [p=0.4] {a}No dia zero, [p=0.2] a entrada de quatrocentos. "
        "[p=0.2] Ela é paga no ato: [p=0.2] *não é financiada.* [p=0.4] {b}O capital é o que a loja empresta: "
        "[p=0.2] mil menos quatrocentos, [p=0.2] *seiscentos.* [p=0.4] {c}No mês dois, [p=0.2] você paga seiscentos e "
        "sessenta. [p=0.2] Os juros: [p=0.2] *sessenta.* [p=0.4] {d}A taxa: [p=0.2] sessenta dividido por seiscentos "
        "vezes dois, [p=0.2] que é mil e duzentos. [p=0.2] *Cinco por cento ao mês.* [p=0.3] {ok}*Letra A!*"),
    dict(id="28", block="q8", text=
        "{t}E as erradas? [p=0.4] {xd}A D, dez por cento, [p=0.2] esquece de dividir pelos *dois meses.* [p=0.4] {xb}A "
        "B, seis por cento, [p=0.2] é sessenta dividido por mil: [p=0.2] usa o *preço total,* [p=0.2] como se tudo "
        "fosse financiado, [p=0.2] *e* esquece de dividir pelos dois meses. [p=0.4] {xc}A C [p=0.2] {xe}e a E "
        "[p=0.2] calculam sobre a *entrada,* [p=0.2] que não é dinheiro emprestado: [p=0.2] com e sem a divisão pelo "
        "tempo."),

    # ================= QUESTÃO 4 (VOCÊ FAZ) =================
    dict(id="29", block="q4", text=
        "{t}E agora é *sua.* [p=0.3] É a pergunta do começo da aula. [p=0.4] {a}Um investidor deseja *triplicar* seu "
        "capital [p=0.2] numa aplicação que paga juros simples de *dois por cento ao mês.* [p=0.2] O tempo mínimo "
        "necessário é de: [p=0.4] {qa}A: [p=0.2] quatro anos e dois meses. [p=0.3] {qb}B: [p=0.2] oito anos e três "
        "meses. [p=0.3] {qc}C: [p=0.2] oito anos e quatro meses. [p=0.3] {qd}D: [p=0.2] doze anos e seis meses. [p=0.3] "
        "{qe}E: [p=0.2] cem anos. [p=0.4] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="30", block="q4", text=
        "{t}Conferindo. [p=0.3] {a}Triplicar: [p=0.2] *J igual a dois C.* [p=0.2] O capital se cancela: [p=0.2] zero "
        "vírgula zero dois vezes t igual a dois. [p=0.4] {b}*Cem meses.* [p=0.4] {c}Em anos: [p=0.2] oito vezes doze, "
        "noventa e seis. [p=0.2] Sobram quatro. [p=0.2] *Oito anos e quatro meses.* [p=0.3] {ok}*Letra C!*"),
    dict(id="31", block="q4", text=
        "{t}E as erradas? [p=0.4] {xa}A A, cinquenta meses, [p=0.2] é o tempo para "
        "*dobrar.* [p=0.4] {xd}A D, cento e cinquenta meses, [p=0.2] fez *J igual a três C.* [p=0.4] {xb}A B leu oito "
        "vírgula trinta e três [p=0.2] como *oito anos e três meses.* [p=0.4] {xe}E a E tratou a taxa mensal [p=0.2] "
        "como se fosse *anual.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] dadas três letras, [p=0.2] a quarta sai "
        "dividindo os juros pelas outras duas. [p=0.5] {b}Dois: [p=0.2] triplicar é ganhar duas vezes o capital em "
        "juros. [p=0.5] {c}Três: [p=0.2] a entrada não é empréstimo."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as pegadinhas [p=0.3] {c}e "
        "treinamos com questões no formato do ENEM."),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] em quanto tempo o seu dinheiro dobraria a um por cento ao mês? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
