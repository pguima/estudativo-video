# Roteiro — Taxas Equivalentes e Inflação, Episódio 4 de 5: taxa real de juros e a armadilha da subtração
# Base: Estudos/Enem/estudos/01-matematica/16-taxas-equivalentes-inflacao.html — parte "Deflacionar" da seção 07 e
#   seções 08 e 09 + Questões 6, 8 e 7 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   A ESCADA ROLANTE DE PREÇOS (episódio 3): o quanto você subiu DE VERDADE é o que você andou acima da escada; andar mais
#     devagar que a escada é descer.
#   TAXA REAL: DIVIDA OS FATORES, NUNCA SUBTRAIA AS TAXAS.
#   DEFLACIONAR é traduzir um valor de hoje para o dinheiro de antigamente, dividindo pelo fator da inflação.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material/prompt: salário 2.000 → 2.400 com 20% (2.400 ÷ 1,20 = 2.000) · R$ 100 → 105 → 115,50 ·
#   1,155 ÷ 1,05 = 1,10 · 1,08 ÷ 1,10 ≈ 0,982 (−1,8%) · 1,01 ÷ 1,005 ≈ 1,004975 · 1,26 ÷ 1,20 = 1,05 ·
#   nós fazemos 1,32 ÷ 1,10 = 1,20 (subtração daria 22%). O erro 1 usa 26% e 20%, como pede o prompt (é a mesma conta da
#   Questão 6, que é "eu faço" e vem logo depois: repetir é ok).
# Atalhos (NOSSOS, verde): "tire a vírgula" (÷ 1,20 = ×10 ÷ 12: 24 000 ÷ 12 = 2 000; 12,6 ÷ 12 = 1,05) e "confira
#   multiplicando de volta" (real × inflação = nominal: 1,10 · 1,05 = 1,155).
# CORREÇÃO AO PROMPT (plausibilidade): o prompt diz "a taxa real fica um pouco ABAIXO da diferença nominal − inflação".
#   Isso vale quando há ganho (Q6: 5 < 6; Q8: 15 < 18), mas não na perda: na Q7 a diferença é −4 e a real é ≈ −3,6, ACIMA
#   dela. A regra geral (i_real = (i − π) ÷ (1 + π), com π > 0) é: a taxa real fica um pouco MAIS PERTO DE ZERO que a
#   diferença — ganho um pouco menor, ou perda um pouco menor. É o que o próprio prompt diz da Q7 ("a subtração exagera a
#   perda"). O vídeo usa essa forma.
# QUESTÃO 6 (eu faço): 1,26 ÷ 1,20 = 1,05 → 5% (B). Erradas (material): C subtração 26 − 20; A divisão invertida
#   1 − 1,20 ÷ 1,26 ≈ 4,76%; D soma 26 + 20; E multiplica os fatores 1,26 · 1,20 = 1,512 (D e E tratam a inflação como ganho).
# QUESTÃO 8 (nós fazemos): 276 ÷ 1,20 = 230 → 230 ÷ 200 = 1,15; ou 276 ÷ 200 = 1,38 e 1,38 ÷ 1,20 = 1,15 → 15% (A).
#   Erradas (material): B 38 − 20; C aumento nominal; D soma 38 + 20; E fator 1,38 escrito como 138%.
# QUESTÃO 7 (você faz): 1,06 ÷ 1,10 ≈ 0,964 → perda de cerca de 3,6% (E). Erradas (material): D subtração 6 − 10 (exagera a
#   perda); C soma reajuste e inflação; A e B trocam o sinal.
# Frases-chave (meio e fim, idênticas): 1. Taxa real: divida o fator nominal pelo fator da inflação. 2. Subtrair as taxas
#   é só uma estimativa; na prova, divida. 3. Rendimento abaixo da inflação é perda, mesmo com saldo maior.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Rendeu 8%, a inflação foi 10%: quanto você perdeu? Taxa real · Matemática ENEM, Taxas e Inflação episódio 4"

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
        "{a}A poupança rendeu *oito por cento* [p=0.2] e a inflação foi de *dez por cento.* [p=0.4] {b}Seu saldo "
        "*cresceu,* [p=0.3] {c}e mesmo assim [p=0.2] você ficou *mais pobre.* [p=0.4] {d}Hoje você descobre "
        "*quanto.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular a *taxa real* de qualquer rendimento ou reajuste [p=0.3] "
        "{b}e saber quando a *subtração* engana."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes do episódio anterior. [p=0.3] {a}*Fator da inflação:* [p=0.2] um mais a taxa. [p=0.2] "
        "Inflação de vinte por cento [p=0.2] é fator *um vírgula vinte.* [p=0.4] {b}E o *poder de compra,* [p=0.2] o "
        "quanto o seu dinheiro compra, [p=0.2] fica *dividido* por esse fator."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe três coisas do dia a dia. [p=0.3] {a}Uma manchete: [p=0.2] *juros de doze por cento e inflação de "
        "cinco: [p=0.2] ganho real de sete.* [p=0.4] {b}O extrato da poupança, [p=0.2] dizendo que ela *rendeu.* "
        "[p=0.4] {c}E o aviso de *reajuste salarial* da categoria. [p=0.4] {d}Nos três, [p=0.2] a mesma pergunta: "
        "[p=0.2] o dinheiro aumentou *de verdade?*"),
    dict(id="05", block="escada", text=
        "{t}Lembra da *escada rolante de preços?* [p=0.4] {a}Os preços sobem sozinhos, [p=0.2] como uma escada "
        "rolante. [p=0.2] E o seu dinheiro sobe a pé, [p=0.2] ao lado dela. [p=0.4] {b}O quanto você subiu *de "
        "verdade* [p=0.2] é o que você andou *acima* da escada. [p=0.4] {c}E se você anda *mais devagar* que a "
        "escada? [p=0.3] {d}Em relação aos preços, [p=0.2] você está *descendo.*"),

    # ================= BLOCO A: DEFLACIONAR =================
    dict(id="06", block="deflacionar", text=
        "{t}Um salário passou de *dois mil* [p=0.2] para *dois mil e quatrocentos reais,* [p=0.2] num período com "
        "inflação de *vinte por cento.* [p=0.2] Ele aumentou de verdade? [p=0.4] {a}Para responder, [p=0.2] a gente "
        "vai *deflacionar.* [p=0.4] {b}*Deflacionar* é traduzir um valor de hoje [p=0.2] para o *dinheiro de "
        "antigamente,* [p=0.2] dividindo pelo fator da inflação."),
    dict(id="07", block="deflacionar", text=
        "{a}Dois mil e quatrocentos [p=0.2] dividido por um vírgula vinte: [p=0.2] *dois mil.* [p=0.4] {b}Esse é o "
        "*valor em dinheiro da data antiga.* [p=0.4] {c}Deu dois mil, [p=0.2] o mesmo salário de antes. [p=0.2] O *poder de compra* não mudou. "
        "[p=0.4] {d}O aumento de vinte por cento [p=0.2] só *repôs a inflação.*"),
    dict(id="08", block="deflacionar", text=
        "{t}E como dividir por um vírgula vinte sem calculadora? [p=0.4] {a}Atalho: [p=0.2] *tire a vírgula.* "
        "[p=0.2] Multiplique os dois números por dez. [p=0.4] {b}Dois mil e quatrocentos dividido por um vírgula "
        "vinte [p=0.2] vira *vinte e quatro mil dividido por doze.* [p=0.2] Dois mil. [p=0.2] Conta de cabeça."),

    # ================= BLOCO B: NOMINAL × REAL =================
    dict(id="09", block="definicao", text=
        "{t}Então existem *duas* taxas em jogo. [p=0.3] Quais? [p=0.4] {a}A *taxa nominal,* [p=0.2] também chamada "
        "de *aparente:* [p=0.2] o quanto o saldo cresceu *em reais.* [p=0.4] "
        "{b}E a *taxa real:* [p=0.2] o quanto cresceu o seu *poder de compra,* [p=0.2] depois de descontar a "
        "inflação. [p=0.4] {c}Na escada rolante: [p=0.2] a nominal é quanto você subiu; [p=0.2] a real é quanto "
        "você subiu *acima da escada.*"),

    # ================= BLOCO C: A FIGURA 100 → 105 → 115,50 =================
    dict(id="10", block="barra", text=
        "{t}E por que não dá para simplesmente somar ou subtrair? [p=0.4] {a}Cem reais aplicados, [p=0.2] "
        "inflação de *cinco por cento.* [p=0.4] {b}Primeiro, [p=0.2] eles precisam virar *cento e cinco,* "
        "[p=0.2] só para *manter* o poder de compra. [p=0.2] É só acompanhar a escada. "
        "[p=0.4] {c}Agora, [p=0.2] um ganho real de *dez por cento.* [p=0.2] Dez por cento *de quê?* [p=0.3] Dos "
        "cento e cinco. [p=0.4] {d}Cento e cinco [p=0.2] vezes um vírgula dez: [p=0.2] *cento e quinze e "
        "cinquenta.*"),
    dict(id="11", block="relacao", text=
        "{t}Repare no que aconteceu. [p=0.3] {a}O rendimento foi de *quinze e cinquenta,* [p=0.2] e não de quinze. "
        "[p=0.2] O ganho real incidiu sobre um valor que *já tinha subido.* [p=0.4] {b}Por isso os *fatores* se "
        "multiplicam: [p=0.2] um vírgula zero cinco [p=0.2] vezes um vírgula dez [p=0.2] dá *um vírgula cento e "
        "cinquenta e cinco.* [p=0.4] {c}A regra: [p=0.2] *fator nominal [p=0.2] igual a fator real [p=0.2] vezes "
        "fator da inflação.*"),
    dict(id="12", block="relacao", text=
        "{t}E se eu quero a taxa *real?* [p=0.4] {a}É só desfazer a multiplicação: [p=0.2] *um mais a taxa real* "
        "[p=0.2] é igual ao fator nominal [p=0.2] *dividido* pelo fator da inflação. [p=0.4] {b}Guarde assim: "
        "[p=0.2] *taxa real: [p=0.2] divida os fatores, [p=0.2] nunca subtraia as taxas.*"),

    # ================= BLOCO D: OS DOIS EXEMPLOS =================
    dict(id="13", block="exemplos", text=
        "{t}Vamos usar. [p=0.3] Uma aplicação rendeu *quinze e meio por cento* [p=0.2] num ano de inflação de "
        "*cinco.* [p=0.4] {a}Os três fatores lado a lado: [p=0.2] nominal, *um vírgula cento e cinquenta e cinco;* "
        "[p=0.2] inflação, *um vírgula zero cinco.* [p=0.4] {b}Dividindo: [p=0.2] *um vírgula dez.* [p=0.2] Ganho "
        "real de *dez por cento.* [p=0.4] {c}Atalho para conferir: [p=0.2] *multiplique de volta.* [p=0.2] Um vírgula "
        "dez vezes um vírgula zero cinco [p=0.2] dá um vírgula cento e cinquenta e cinco. [p=0.2] Bateu."),
    dict(id="14", block="exemplos", text=
        "{t}Agora, o gancho. [p=0.3] A poupança rendeu *oito,* [p=0.2] a inflação foi *dez.* [p=0.4] {a}Um vírgula "
        "zero oito [p=0.2] dividido por um vírgula dez: [p=0.2] mais ou menos *zero vírgula nove oito dois.* [p=0.4] "
        "{b}O fator ficou *abaixo de um.* [p=0.2] A taxa real é de mais ou menos *menos um vírgula oito por cento:* "
        "[p=0.2] uma *perda.* [p=0.4] {c}Na escada rolante: [p=0.2] você andou *mais devagar* que a escada. [p=0.2] "
        "*Taxa real negativa.* [p=0.4] {d}O saldo aumentou em reais, [p=0.2] mas compra *menos* do que antes."),

    # ================= BLOCO E: A APROXIMAÇÃO =================
    dict(id="15", block="aproximacao", text=
        "{t}E a manchete dos doze menos cinco? [p=0.3] Está errada? [p=0.4] {a}Ela usa uma *aproximação:* [p=0.2] uma "
        "conta que só chega *perto* do valor certo. [p=0.2] Taxa real, [p=0.2] *mais ou menos* "
        "nominal menos inflação. [p=0.4] {b}Com taxas pequenas, [p=0.2] funciona. [p=0.2] Um por cento ao mês, "
        "[p=0.2] com inflação de meio por cento: [p=0.2] a subtração dá *zero vírgula cinco;* [p=0.2] a conta exata "
        "dá *zero vírgula quatro nove sete cinco.* [p=0.4] {c}Diferença desprezível."),
    dict(id="16", block="aproximacao", text=
        "{t}Mas com taxas grandes? [p=0.4] {a}Rendeu vinte e seis, [p=0.2] inflação de vinte. [p=0.2] A subtração "
        "dá *seis.* [p=0.4] {b}A conta exata: [p=0.2] um vírgula vinte e seis dividido por um vírgula vinte, "
        "[p=0.2] *um vírgula zero cinco.* [p=0.2] *Cinco por cento.* [p=0.2] Um ponto inteiro. [p=0.4] "
        "{c}Na prova, [p=0.2] use a conta *exata.* [p=0.2] A subtração serve só para conferir a *ordem de "
        "grandeza.* [p=0.4] {d}E guarde: [p=0.2] a taxa real fica sempre um pouco *mais perto do zero* que a "
        "subtração. [p=0.2] Ganho um pouco menor, [p=0.2] ou perda um pouco menor."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma aplicação rendeu *trinta e dois por cento* [p=0.2] num ano de inflação de *dez "
        "por cento.* [p=0.2] Qual foi a taxa real? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Os fatores: [p=0.2] nominal, *um vírgula trinta e dois;* [p=0.2] inflação, "
        "*um vírgula dez.* [p=0.4] {b}Tire a vírgula: [p=0.2] cento e trinta e dois dividido por cento e dez. "
        "[p=0.2] *Um vírgula vinte.* [p=0.2] Taxa real de *vinte por cento.* [p=0.4] {c}Multiplicando de volta: "
        "[p=0.2] um vírgula vinte vezes um vírgula dez, [p=0.2] um vírgula trinta e dois. [p=0.2] Bateu. [p=0.4] "
        "{d}E a subtração daria *vinte e dois.* [p=0.2] Longe demais do zero."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] taxa real: [p=0.2] divida o fator nominal pelo "
        "fator da inflação. [p=0.5] {b}Dois: [p=0.2] subtrair as taxas é só uma estimativa; [p=0.2] na prova, "
        "divida. [p=0.5] {c}Três: [p=0.2] rendimento abaixo da inflação é perda, [p=0.2] mesmo com saldo maior."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *taxa real igual a nominal menos "
        "inflação.* [p=0.2] Vinte e seis menos vinte, [p=0.2] seis. [p=0.4] {b}Parece certo, [p=0.2] porque é o "
        "que a manchete faz. [p=0.4] {c}Mas o certo é dividir os "
        "fatores: [p=0.2] *cinco por cento,* [p=0.2] não seis."),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] achar que *rendimento positivo é sempre ganho.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "o número no extrato *aumentou.* [p=0.4] {c}Mas render oito com inflação de dez [p=0.2] é *perder* poder de "
        "compra. [p=0.2] Compare sempre com a escada."),

    # ================= QUESTÃO 6 (EU FAÇO) =================
    dict(id="22", block="q6", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Esta, [p=0.2] eu resolvo "
        "com você. [p=0.4] {a}Um investidor aplicou suas economias por um ano [p=0.2] e obteve rendimento de *vinte "
        "e seis por cento.* [p=0.2] No mesmo ano, [p=0.2] a inflação foi de *vinte por cento.* [p=0.2] A taxa real de "
        "rendimento foi de: [p=0.4] {qa}A: [p=0.2] quatro vírgula setenta e seis por cento. [p=0.3] {qb}B: [p=0.2] "
        "cinco. [p=0.3] {qc}C: [p=0.2] seis. [p=0.3] {qd}D: [p=0.2] quarenta e seis. [p=0.3] {qe}E: [p=0.2] "
        "cinquenta e um vírgula vinte por cento."),
    dict(id="23", block="q6", text=
        "{t}Os três fatores. [p=0.3] {a}Nominal: [p=0.2] um vírgula vinte e seis. [p=0.2] Inflação: [p=0.2] um "
        "vírgula vinte. [p=0.4] {b}Divida: [p=0.2] tire a vírgula, [p=0.2] doze vírgula seis dividido por doze, "
        "[p=0.2] *um vírgula zero cinco.* [p=0.2] Cinco por cento. [p=0.4] {c}Plausível? [p=0.2] Cinco fica um pouco "
        "mais perto do zero que a subtração, seis. [p=0.2] Faz sentido. [p=0.3] {ok}*Letra B!*"),
    dict(id="24", block="q6", text=
        "{t}E as outras? [p=0.3] {xc}A C, [p=0.2] seis, [p=0.2] é a *subtração:* [p=0.2] a armadilha da aula. "
        "[p=0.4] {xa}A A [p=0.2] fez a divisão *invertida:* [p=0.2] um vírgula vinte por um vírgula vinte e seis. "
        "[p=0.4] {xd}A D *soma* as taxas, [p=0.2] {xe}e a E *multiplica* os fatores. [p=0.2] As duas tratam a "
        "inflação como *ganho.*"),

    # ================= QUESTÃO 8 (NÓS FAZEMOS) =================
    dict(id="25", block="q8", text=
        "{t}A próxima, a gente faz junto. [p=0.3] {a}O preço de um eletrodoméstico passou de *duzentos* para "
        "*duzentos e setenta e seis reais,* [p=0.2] num período de inflação acumulada de *vinte por cento.* [p=0.2] "
        "Descontada a inflação, [p=0.2] o aumento real foi de: [p=0.4] {qa}A: [p=0.2] quinze por cento. [p=0.3] "
        "{qb}B: [p=0.2] dezoito. [p=0.3] {qc}C: [p=0.2] trinta e oito. [p=0.3] {qd}D: [p=0.2] cinquenta e oito. "
        "[p=0.3] {qe}E: [p=0.2] cento e trinta e oito. [p=0.5] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q8", text=
        "{t}*Aumento real* é o aumento descontada a inflação. [p=0.2] Dois caminhos. [p=0.4] {a}Primeiro: "
        "[p=0.2] *deflacione.* [p=0.2] Duzentos e setenta e seis dividido por um vírgula vinte: [p=0.2] *duzentos e "
        "trinta,* [p=0.2] em dinheiro da data antiga. [p=0.2] E duzentos e trinta sobre duzentos: [p=0.2] *um "
        "vírgula quinze.* [p=0.4] {b}Segundo: [p=0.2] o fator nominal, [p=0.2] duzentos e setenta e seis sobre "
        "duzentos, [p=0.2] *um vírgula trinta e oito.* [p=0.2] Dividido por um vírgula vinte: [p=0.2] um vírgula "
        "quinze. [p=0.4] {c}Os dois batem: [p=0.2] *quinze por cento.* [p=0.3] {ok}*Letra A!*"),
    dict(id="27", block="q8", text=
        "{t}E as erradas? [p=0.3] {xb}A B, [p=0.2] dezoito, [p=0.2] subtraiu: [p=0.2] trinta e oito menos vinte. "
        "[p=0.4] {xc}A C é o aumento *nominal,* [p=0.2] sem descontar nada. [p=0.4] {xd}A D *soma* aumento e "
        "inflação. [p=0.4] {xe}E a E [p=0.2] escreveu o *fator* um vírgula trinta e oito [p=0.2] como se fosse a "
        "taxa."),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="28", block="q7", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma categoria profissional recebeu reajuste salarial de *seis por cento* "
        "[p=0.2] num ano em que a inflação foi de *dez por cento.* [p=0.2] Considere um vírgula zero seis dividido "
        "por um vírgula dez, [p=0.2] aproximadamente zero vírgula nove seis quatro. [p=0.2] Em termos reais, "
        "[p=0.2] esses trabalhadores tiveram: [p=0.4] {qa}A: [p=0.2] ganho de quatro por cento. [p=0.3] {qb}B: "
        "[p=0.2] ganho de cerca de três vírgula seis. [p=0.3] {qc}C: [p=0.2] perda de dezesseis. [p=0.3] {qd}D: "
        "[p=0.2] perda de quatro. [p=0.3] {qe}E: [p=0.2] perda de cerca de três vírgula seis. [p=0.5] {p}*Pause o "
        "vídeo e resolva.* [p=2.0]"),
    dict(id="29", block="q7", text=
        "{t}Conferindo. [p=0.3] {a}O reajuste ficou *abaixo* da inflação: [p=0.2] andou mais devagar que a "
        "escada. [p=0.2] Então é *perda.* [p=0.4] {b}O tamanho: [p=0.2] o fator real é zero vírgula nove seis "
        "quatro. [p=0.2] O salário compra noventa e seis vírgula quatro por cento do que comprava: [p=0.2] *perda de "
        "cerca de três vírgula seis.* [p=0.3] {ok}*Letra E!*"),
    dict(id="30", block="q7", text=
        "{t}E as outras? [p=0.3] {xd}A D, [p=0.2] perda de quatro, [p=0.2] é a *subtração:* [p=0.2] seis menos dez. "
        "[p=0.2] Ela *exagera* a perda, [p=0.2] porque se afasta demais do zero. [p=0.4] {xc}A C *soma* reajuste e "
        "inflação, [p=0.2] como se os dois fossem perdas. [p=0.4] {xa}A A [p=0.2] {xb}e a B [p=0.2] trocaram o "
        "*sinal:* [p=0.2] reajuste positivo parece ganho, [p=0.2] mas não quando os preços sobem mais."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] taxa real: [p=0.2] divida o fator nominal "
        "pelo fator da inflação. [p=0.5] {b}Dois: [p=0.2] subtrair as taxas é só uma estimativa; [p=0.2] na prova, "
        "divida. [p=0.5] {c}Três: [p=0.2] rendimento abaixo da inflação é perda, [p=0.2] mesmo com saldo maior."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos *tudo,* [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] "
        "{c}e treinamos com *questões inéditas.*"),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] o seu último reajuste ganhou ou perdeu da inflação? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
