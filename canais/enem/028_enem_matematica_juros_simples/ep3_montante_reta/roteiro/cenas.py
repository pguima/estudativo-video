# Roteiro — Juros Simples, Episódio 3 de 5: o montante é uma reta (gráfico, tabela e PA)
# Base: Estudos/Enem/estudos/01-matematica/13-juros-simples.html — seções 05 e 07 + Questões 7 e 6 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   O montante sobe uma ESCADA DE DEGRAUS IGUAIS: cada degrau são os juros de um mês (C · i).
#   A RETA COMEÇA NO CAPITAL: o ponto onde ela corta o eixo vertical é o dinheiro do dia zero.
#   Para achar a taxa, divida o DEGRAU pelo CAPITAL, nunca pelo montante.
# Frases do usuário mantidas IGUAIS: gancho, promessa (com "Ao final desta aula"), as 3 frases-chave e a ponte.
# Função afim e PA: só o que o material traz + "tem série própria". Juros compostos: só a promessa do contraste.
# Exemplos:
#   Bloco b/c/d (material): R$ 1.000,00 a 5% a.m. → 1.050, 1.100, 1.150...; degrau de R$ 50,00; 2 meses = R$ 100,00.
#   Bloco e (NOSSO, mesma reta): pontos (0; 1.000) e (4; 1.200) → 200 ÷ 4 = 50 por mês → 50 ÷ 1.000 = 5%.
#   Bloco f (NOSSO): rendeu R$ 150,00 em 3 meses → em 12 meses, R$ 600,00 (só em juros simples).
#   Bloco g (material): R$ 1.000,00 a 3% a.m. → 1.030, 1.060, 1.090, 1.120; razão C · i = 30.
#   Nós fazemos (prompt): 2.500 no mês 0 e 2.750 no mês 5 → 250 ÷ 5 = 50 → 50 ÷ 2.500 = 2% a.m.
#   Erros 1 e 2 usam os números do nós fazemos (já resolvido): 50 ÷ 2.750 ≈ 1,8% · 250 ÷ 2.500 = 10%.
#   Erro 3 usa a PA do bloco g: razão 30 reais × taxa 3%.
# QUESTÃO 7 (eu faço): 5.100, 5.200, 5.300 → PA de razão 100 → E. Erradas (do material e do prompt): A = juros compostos
#   (PG de razão 1,02, próxima série; 5.100, 5.202, 5.306,04); B = razão confundida com a taxa (2);
#   C e D misturam os dois tipos de progressão com a razão do outro (C: PG com a razão 100; D: PA com a razão 1,02).
# QUESTÃO 6 (você faz): C = 1.600 (t = 0); 400 em 10 meses = 40 por mês; 40 ÷ 1.600 = 2,5% → B. Erradas (material):
#   D = 400 ÷ 1.600 = 25% (sem dividir pelos 10 meses); A = 40 ÷ 2.000 = 2%; C = 400 ÷ 2.000 = 20% (base no montante
#   final); E = R$ 40,00 por mês lido como 40%. Conferência de plausibilidade (NOSSA): 2,5% de 1.600 = 40 ✓.
# Atalhos (verde): "ler um gráfico em 3 passos" · "regra de três rápida (só em juros simples)" · "razão da PA = C · i".
# Frases-chave (meio e fim, idênticas): 1. O montante sobe uma escada de degraus iguais. 2. A reta começa no capital.
#   3. Taxa é o degrau dividido pelo capital.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Juros simples no gráfico: capital, taxa e a PA dos montantes | Juros Simples Ep. 3"
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
        "{a}Um gráfico com uma *reta* [p=0.2] e *dois pontos.* [p=0.3] Só isso. [p=0.5] {b}E dele dá para tirar o "
        "*capital,* [p=0.2] {c}os *juros de cada mês* [p=0.2] {d}e a *taxa da aplicação,* [p=0.3] {e}sem nenhuma "
        "*fórmula nova.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai ler *capital e taxa* num gráfico ou numa tabela [p=0.3] {b}e "
        "reconhecer a *sequência dos montantes.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio 1: [p=0.2] *M igual a C mais C vezes i vezes t;* [p=0.2] e "
        "os juros de *um* mês são *C vezes i.* [p=0.4] {b}E num gráfico, [p=0.2] cada *eixo* é uma régua: [p=0.2] no "
        "*horizontal,* o tempo; [p=0.2] no *vertical,* o montante. [p=0.4] {c}Cada ponto diz: [p=0.2] *no mês tal, havia "
        "tanto.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe o extrato de uma aplicação. [p=0.3] {a}Começou com *mil reais.* [p=0.2] Mês um: [p=0.2] *mil e "
        "cinquenta.* [p=0.2] Mês dois: [p=0.2] *mil e cem.* [p=0.2] Mês três: [p=0.2] *mil, cento e cinquenta.* "
        "[p=0.4] {b}Sobe *sempre cinquenta.* [p=0.4] {c}O montante sobe uma *escada de degraus iguais:* [p=0.2] cada "
        "degrau são os *juros de um mês.*"),

    # ================= BLOCO A: MONTANTE COMO FUNÇÃO DO TEMPO =================
    dict(id="05", block="funcao", text=
        "{t}Dá para escrever essa escada numa linha só? [p=0.4] {a}Dá. [p=0.2] Pense numa *regra:* [p=0.2] você diz o "
        "mês, [p=0.2] ela devolve o montante. [p=0.4] {b}*M de t* [p=0.2] *igual a C* [p=0.2] *mais C vezes i, vezes t.* "
        "[p=0.4] {c}*C* é onde a escada começa; [p=0.2] *C vezes i,* a altura de *cada degrau;* [p=0.2] e *t* conta os "
        "degraus."),

    # ================= BLOCO B: O GRÁFICO DO MATERIAL =================
    dict(id="06", block="grafico", text=
        "{t}E como fica no desenho? [p=0.4] {a}Um *gráfico* mostra como uma coisa muda com outra. [p=0.2] Aqui: "
        "[p=0.2] mil reais a *cinco por cento ao mês.* [p=0.4] {b}A escada sobe *cinquenta reais* por mês. [p=0.2] Ligue "
        "as pontas dos degraus: [p=0.2] vira uma *reta.* [p=0.4] {c}Agora, uma linha "
        "tracejada na altura do capital, [p=0.2] os mil reais. [p=0.4] {d}A distância entre a reta e essa linha "
        "[p=0.2] são os *juros acumulados.* [p=0.2] No mês seis, [p=0.2] *trezentos reais.*"),

    # ================= BLOCO C: A FORMA DE FUNÇÃO AFIM =================
    dict(id="07", block="afim", text=
        "{t}Onde essa reta *começa?* [p=0.4] {a}No mês zero, [p=0.2] o dia do depósito. [p=0.2] Ali ainda não há juros: "
        "[p=0.2] o montante é o próprio *capital.* [p=0.4] {b}Esse é o *ponto inicial:* [p=0.2] a reta começa no "
        "capital. [p=0.2] O ponto onde ela corta o eixo vertical [p=0.2] é o *dinheiro do dia zero.* [p=0.4] {c}E o quanto ela sobe a cada mês [p=0.2] se chama *inclinação:* [p=0.2] aqui, "
        "*C vezes i,* [p=0.2] cinquenta reais. [p=0.4] {d}Reta com começo e inclinação, [p=0.2] *y igual a b mais a vezes x,* [p=0.2] se chama *função afim.* "
        "[p=0.2] Ela tem série própria."),

    # ================= BLOCO D: JUROS IGUAIS EM TEMPOS IGUAIS =================
    dict(id="08", block="iguais", text=
        "{t}Rende mais no começo ou no fim? [p=0.4] {a}Dois meses no começo: [p=0.2] de mil para mil e cem. [p=0.2] *Cem reais.* [p=0.4] {b}Dois meses no fim, [p=0.2] do mês oito ao dez: "
        "[p=0.2] de mil e quatrocentos para mil e quinhentos. [p=0.2] *Cem reais* de novo. [p=0.4] {c}*Tempos "
        "iguais, juros iguais.*"),

    # ================= BLOCO E: LER O GRÁFICO =================
    dict(id="09", block="ler", text=
        "{t}E se eu só te der *dois pontos* da reta? [p=0.4] {a}Mês zero, [p=0.2] mil reais. [p=0.2] Mês quatro, "
        "[p=0.2] mil e duzentos. [p=0.4] {b}O capital é o valor no mês zero: [p=0.2] *mil reais.* [p=0.4] {c}Os juros "
        "por mês: [p=0.2] a subida dividida pelo tempo. [p=0.2] Subiu duzentos em quatro meses: [p=0.2] *cinquenta por "
        "mês.* [p=0.4] {d}E a taxa? [p=0.2] Divida o degrau pelo capital, [p=0.2] *nunca pelo montante.* [p=0.2] "
        "Cinquenta dividido por mil: [p=0.2] *zero vírgula zero cinco,* [p=0.2] *cinco por cento ao mês.*"),
    dict(id="10", block="ler", text=
        "{t}O atalho em três passos. [p=0.3] {a}Um: [p=0.2] capital é o valor em *t igual a zero.* [p=0.4] {b}Dois: "
        "[p=0.2] juros por mês é a *variação dividida pelo tempo.* [p=0.4] {c}Três: [p=0.2] taxa é o *degrau dividido "
        "pelo capital.*"),

    # ================= BLOCO F: DOBRO DO TEMPO, DOBRO DOS JUROS =================
    dict(id="11", block="dobro", text=
        "{t}E por que a regra de três funciona aqui? [p=0.4] {a}Porque cada mês põe o *mesmo degrau.* [p=0.2] Dois "
        "meses, [p=0.2] cem reais. [p=0.2] Quatro meses, [p=0.2] duzentos. [p=0.2] *O dobro do tempo dá o dobro dos "
        "juros.* [p=0.4] {b}Juros e tempo são *proporcionais.* [p=0.4] {c}Rendeu cento e cinquenta em três meses? [p=0.2] Em "
        "doze meses, [p=0.2] *seiscentos.* [p=0.4] {d}Mas isso vale em juros *simples,* [p=0.2] *e só neles.*"),

    # ================= BLOCO G: A PA =================
    dict(id="12", block="pa", text=
        "{t}E a lista dos montantes, [p=0.2] tem nome? [p=0.4] {a}Mil reais a *três por cento ao mês.* [p=0.2] "
        "Montantes: [p=0.2] *mil e trinta, [p=0.2] mil e sessenta, [p=0.2] mil e noventa, [p=0.2] mil, cento e "
        "vinte.* [p=0.4] {b}Uma lista em que se soma *sempre o mesmo número* [p=0.2] se chama *progressão aritmética,* "
        "[p=0.2] ou *PA.* [p=0.4] {c}E esse número somado é a *razão da PA.* [p=0.2] Aqui, [p=0.2] mil vezes zero "
        "vírgula zero três: [p=0.2] *trinta reais.* [p=0.4] {d}Atalho: [p=0.2] *a razão é C vezes i,* [p=0.2] o degrau "
        "da escada. [p=0.2] PA tem série própria."),

    # ================= BLOCO H: ONDE SE USA =================
    dict(id="13", block="mercado", text=
        "{t}E quem usa juros simples de verdade? [p=0.4] {a}*Conta atrasada,* [p=0.2] *empréstimo informal* [p=0.2] e "
        "*cobranças por dia.* "
        "[p=0.4] {b}Já *bancos e cartões* [p=0.2] usam *juros compostos:* [p=0.2] próxima série. [p=0.4] {c}Na prova, [p=0.2] o enunciado diz o regime."),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Num gráfico de juros simples, [p=0.2] o montante vale *dois mil e quinhentos reais* no "
        "*mês zero* [p=0.2] e *dois mil, setecentos e cinquenta* no *mês cinco.* [p=0.4] {b}Qual é a *taxa mensal?* "
        "[p=0.3] *Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos, [p=0.2] pelos três passos. [p=0.4] {a}Capital: [p=0.2] o valor no mês zero, [p=0.2] *dois "
        "mil e quinhentos.* [p=0.4] {b}Juros em cinco meses: [p=0.2] dois mil, setecentos e cinquenta menos dois mil e "
        "quinhentos, [p=0.2] *duzentos e cinquenta.* [p=0.2] Por mês: [p=0.2] duzentos e cinquenta dividido por cinco, "
        "[p=0.2] *cinquenta reais.* [p=0.4] {c}Taxa: [p=0.2] cinquenta dividido por dois mil e quinhentos, [p=0.2] *zero "
        "vírgula zero dois.* [p=0.2] *Dois por cento ao mês.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] o montante sobe uma escada de degraus iguais. [p=0.5] "
        "{b}Dois: [p=0.2] a reta começa no capital. [p=0.5] {c}Três: [p=0.2] taxa é o degrau dividido pelo capital."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dividir pelo *montante final.* [p=0.2] "
        "Cinquenta dividido por dois mil, setecentos e cinquenta: [p=0.2] *um vírgula oito por cento.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque o montante é o número que mais chama a atenção. [p=0.4] {c}Mas a taxa é sobre o *capital:* [p=0.2] o valor do mês zero."),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] esquecer de dividir pelo número de meses. [p=0.2] Duzentos e cinquenta dividido por dois "
        "mil e quinhentos: [p=0.2] *dez por cento ao mês!* [p=0.4] {b}Parece certo, [p=0.2] porque duzentos e "
        "cinquenta é a subida que você vê no gráfico. [p=0.4] {c}Mas essa subida é de *cinco meses.* [p=0.2] Primeiro "
        "ache o degrau de *um* mês."),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] confundir a *razão da PA* com a *taxa:* [p=0.2] razão três, [p=0.2] ou taxa de trinta "
        "por cento. [p=0.4] {b}Parece certo, [p=0.2] porque as duas medem o crescimento. [p=0.4] {c}Mas a razão é em "
        "*reais,* [p=0.2] trinta; [p=0.2] a taxa, em *por cento,* [p=0.2] três."),

    # ================= QUESTÃO 7 (EU FAÇO) =================
    dict(id="20", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Eu resolvo com você. "
        "[p=0.4] {a}Um capital de *cinco mil reais* [p=0.2] é aplicado a juros simples de *dois por cento ao mês.* "
        "[p=0.2] Os montantes ao final de cada mês, [p=0.2] a partir do primeiro, [p=0.2] formam uma: [p=0.4] {qa}A: "
        "[p=0.2] progressão geométrica de razão um vírgula zero dois. [p=0.3] {qb}B: [p=0.2] progressão aritmética de "
        "razão dois. [p=0.3] {qc}C: [p=0.2] progressão geométrica de razão cem. [p=0.3] {qd}D: [p=0.2] progressão "
        "aritmética de razão um vírgula zero dois. [p=0.3] {qe}E: [p=0.2] progressão aritmética de razão cem."),
    dict(id="21", block="q7", text=
        "{t}Primeiro, [p=0.2] o degrau. [p=0.3] {a}Dois por cento de cinco mil: [p=0.2] *cem reais* por mês. [p=0.4] "
        "{b}Os montantes: [p=0.2] *cinco mil e cem, [p=0.2] cinco mil e duzentos, [p=0.2] cinco mil e trezentos.* "
        "[p=0.4] {c}Soma *sempre cem:* [p=0.2] é uma *PA.* [p=0.2] E a razão é *C vezes i:* [p=0.2] *cem reais.* "
        "[p=0.3] {ok}*Letra E!*"),
    dict(id="22", block="q7", text=
        "{t}E as outras? [p=0.4] {xa}A A descreve *juros compostos,* [p=0.2] em que o saldo é *multiplicado* por um "
        "vírgula zero dois a cada mês. [p=0.2] A progressão *geométrica:* [p=0.2] próxima série. [p=0.4] {xb}A B confunde a razão com a *taxa:* [p=0.2] dois é o por cento, [p=0.2] não os "
        "reais. [p=0.4] {xc}A C e a D misturam os dois tipos: [p=0.2] a C põe a razão certa no tipo errado, [p=0.4] "
        "{xd}e a D, [p=0.2] o tipo certo com a razão dos compostos."),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="23", block="q6", text=
        "{t}E agora, [p=0.2] é *você* quem faz. [p=0.3] {a}O gráfico mostra a evolução do montante de uma aplicação a "
        "juros simples, [p=0.2] desde o dia em que o capital foi depositado. [p=0.3] {g}A reta começa em *mil e "
        "seiscentos reais* no mês zero [p=0.2] e chega a *dois mil reais* no mês dez. [p=0.4] {b}A taxa mensal de juros "
        "dessa aplicação é de: [p=0.3] {qa}A: [p=0.2] dois por cento. [p=0.2] {qb}B: [p=0.2] dois vírgula cinco por "
        "cento. [p=0.2] {qc}C: [p=0.2] vinte por cento. [p=0.2] {qd}D: [p=0.2] vinte e cinco por cento. [p=0.2] "
        "{qe}E: [p=0.2] quarenta por cento. [p=0.4] {c}*Pause o vídeo* [p=0.2] e tente. [p=2.0]"),
    dict(id="24", block="q6", text=
        "{t}Conferindo. [p=0.3] {a}Capital: [p=0.2] o valor no mês zero, [p=0.2] *mil e seiscentos.* [p=0.4] {b}Juros "
        "em dez meses: [p=0.2] dois mil menos mil e seiscentos, [p=0.2] *quatrocentos.* [p=0.2] Por mês: [p=0.2] "
        "*quarenta reais,* [p=0.2] a inclinação. [p=0.4] {c}Taxa: [p=0.2] quarenta dividido por mil e "
        "seiscentos, [p=0.2] *zero vírgula zero vinte e cinco.* [p=0.2] *Dois vírgula cinco por cento ao mês.* [p=0.4] "
        "{d}Plausível? [p=0.2] Dois e meio por cento de mil e seiscentos [p=0.2] dá quarenta. [p=0.3] {ok}*Letra B!*"),
    dict(id="25", block="q6", text=
        "{t}E as erradas? [p=0.4] {xd}A D, [p=0.2] quatrocentos dividido por mil e seiscentos, [p=0.2] *esqueceu os dez "
        "meses.* [p=0.4] {xa}A A e a C dividem pelo *montante final,* "
        "[p=0.2] dois mil: [p=0.2] quarenta ou quatrocentos sobre dois mil. [p=0.4] {xc}Dois e vinte por cento. [p=0.4] {xe}E a E leu *quarenta reais* por mês [p=0.2] como "
        "*quarenta por cento.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] o montante sobe uma escada de degraus iguais. "
        "[p=0.5] {b}Dois: [p=0.2] a reta começa no capital. [p=0.5] {c}Três: [p=0.2] taxa é o degrau dividido pelo "
        "capital."),

    # ================= PONTE E CTA =================
    dict(id="27", block="ponte", text=
        "{a}*Mil e duzentos reais* viraram *mil e quinhentos* [p=0.2] em *dez meses.* [p=0.3] Qual foi a *taxa anual?* "
        "[p=0.5] {b}E em quanto tempo um capital *triplica* [p=0.2] a dois por cento ao mês? [p=0.5] {c}Próximo "
        "episódio: [p=0.2] *descobrindo capital, taxa ou tempo.*"),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha visto juros num gráfico? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
