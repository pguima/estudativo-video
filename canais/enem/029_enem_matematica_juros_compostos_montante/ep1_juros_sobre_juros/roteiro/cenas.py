# Roteiro — Juros Compostos e Montante, Episódio 1 de 5: juros sobre juros e a fórmula M = C · (1 + i)ᵗ
# Base: Estudos/Enem/estudos/01-matematica/14-juros-compostos-montante.html — seções 02 e 03 + Questões 1 e 5 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A BOLA DE NEVE: a cada volta ela pega neve sobre a neve que já tinha, e cresce cada vez mais rápido.
#   PENSE EM FATORES, não em porcentagens somadas: cada período MULTIPLICA o saldo por (1 + i).
#   O EXPOENTE CONTA quantas vezes o fator foi aplicado: três anos, três multiplicações.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos: a tabela do material (R$ 1.000,00 a 10% a.m.: juros 100, 110, 121, 133,10; saldos 1.100, 1.210, 1.331, 1.464,10)
#   e o exemplo do material (R$ 5.000,00 a 2% a.m. por 3 meses: 1,02³ = 1,061208; M = 5.306,04; J = 306,04; simples 300).
#   Nós fazemos (prompt): R$ 2.000,00 a 10% a.m. por 2 meses → 1,21; M = 2.420; J = 420 (simples 400).
#   Bloco h (NOSSO, para não entregar a Q5 "você faz"): +5% e depois +10% → 1,05 · 1,10 = 1,155 → 15,5%, não 15%.
#   Atalho (NOSSO): multiplicar por 1,1 = somar o número com o seu décimo (1,21 + 0,121 = 1,331);
#   multiplicar por 1,02 = somar 2% do próprio número.
#   Erros (NOSSOS, com os números do exemplo do material): simples no lugar de composto (5.300 × 5.306,04);
#   10% por 2 anos = 21% (prompt); montante × juros (5.306,04 × 306,04); período a mais (3 anos = expoente 3).
# QUESTÃO 1 (eu faço; erradas do material, que estão certas): 1,1³ = 1,331 → R$ 13.310,00 (C). B = montante simples
#   (13.000); A = só os juros (3.310); E = expoente 4 (14.641); D = montante simples de 4 anos (14.000).
# QUESTÃO 5 (você faz; erradas do material): 1,10 · 1,20 · 0,75 = 1,32 · 0,75 = 0,99 → perda de 1% (A). B = soma das taxas
#   (5%); D = soma só dos ganhos (30%); C = tamanho certo, sinal errado; E = "quase se anulam" (a perda incide sobre um
#   valor maior). Conferência de plausibilidade (NOSSA): 25% de 132 = 33 > 32 ganhos → tem que dar perda.
# Frases-chave (meio e fim, idênticas): 1. Juros compostos: juros sobre juros, como bola de neve.
#   2. Cada período multiplica o saldo por 1 + i. 3. Os juros saem por diferença: montante menos capital.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Juros compostos do zero: juros sobre juros e a fórmula M = C · (1 + i)ᵗ · Matemática ENEM, Juros compostos episódio 1"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}*Mil reais* a *dez por cento ao mês.* [p=0.4] {b}Em juros simples, [p=0.2] depois de quatro meses, [p=0.2] "
        "*mil e quatrocentos reais.* [p=0.4] {c}Em juros compostos, [p=0.2] *mil, quatrocentos e sessenta e quatro reais "
        "e dez centavos.* [p=0.4] {d}Os mesmos dez por cento. [p=0.4] {e}Quem cria esses *sessenta e quatro reais e dez* "
        "a mais [p=0.2] são os *juros que passaram a render juros.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular *qualquer montante* em juros compostos [p=0.3] {b}e encadear "
        "*taxas diferentes* [p=0.2] sem somar porcentagens."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Da série de Juros simples: [p=0.2] *capital* é o valor do começo, "
        "[p=0.2] *juros* é o acréscimo, [p=0.2] *montante* é o total. [p=0.4] {b}Da Porcentagem: [p=0.2] aumentar dez por"
        " cento é multiplicar por *um vírgula dez,* [p=0.2] e dois aumentos seguidos [p=0.2] *multiplicam* os fatores. "
        "[p=0.4] {c}E da Potenciação: [p=0.2] um vírgula um ao cubo [p=0.2] é *um vírgula um, três vezes, multiplicado.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Sabe aquela dívida do *cartão de crédito* [p=0.2] que parece *crescer sozinha?* [p=0.4] {a}Você não gasta "
        "mais nada, [p=0.2] e todo mês ela está maior que no mês anterior. [p=0.4] {b}E a *poupança* faz o mesmo, [p=0.2]"
        " só que a seu favor: [p=0.2] ela rende sobre o que *já rendeu.* [p=0.4] {c}É uma *bola de neve:* [p=0.2] a cada "
        "volta, [p=0.2] ela pega neve sobre a neve que já tinha, [p=0.2] e cresce cada vez mais rápido."),

    # ================= BLOCO A: A DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}E o que muda, exatamente, dos juros simples para os compostos? [p=0.4] {a}O *saldo* é quanto você tem na "
        "conta naquele momento. [p=0.4] {b}Em *juros compostos,* [p=0.2] os juros de cada mês são calculados sobre o "
        "*saldo do mês anterior,* [p=0.2] que já inclui os juros acumulados. [p=0.4] {c}O juro do mês entra no saldo "
        "[p=0.2] e passa a render também. [p=0.2] Isso se chama *incorporar os juros,* [p=0.2] ou *capitalizar.*"),

    # ================= BLOCO B: A TABELA =================
    dict(id="06", block="tabela", text=
        "{t}Quanto isso faz de diferença? [p=0.3] Vamos montar mês a mês: [p=0.2] mil reais, [p=0.2] dez por cento ao "
        "mês. [p=0.4] {a}No primeiro mês, [p=0.2] dez por cento de mil: [p=0.2] *cem reais.* [p=0.2] Saldo, [p=0.2] *mil "
        "e cem.* [p=0.4] {b}No segundo mês, [p=0.2] os juros são dez por cento de *mil e cem:* [p=0.2] *cento e dez.* "
        "[p=0.2] Saldo, [p=0.2] *mil, duzentos e dez.*"),
    dict(id="07", block="tabela", text=
        "{a}No terceiro, [p=0.2] dez por cento de mil, duzentos e dez: [p=0.2] *cento e vinte e um.* [p=0.2] Saldo, "
        "[p=0.2] *mil, trezentos e trinta e um.* [p=0.4] {b}No quarto, [p=0.2] *cento e trinta e três e dez.* [p=0.2] "
        "Saldo, [p=0.2] *mil, quatrocentos e sessenta e quatro e dez.* [p=0.4] {c}E em juros simples? [p=0.2] *Cem reais "
        "todo mês,* [p=0.2] sempre sobre os mil do começo. [p=0.4] {d}Repare: [p=0.2] é sempre dez por cento, [p=0.2] mas"
        " de um saldo *cada vez maior.*"),

    # ================= BLOCO C: ONDE NASCE A DIFERENÇA =================
    dict(id="08", block="diferenca", text=
        "{t}E quando os dois regimes começam a se separar? [p=0.4] {a}No primeiro mês, [p=0.2] *empatam:* [p=0.2] cem "
        "contra cem. [p=0.4] {b}A diferença *nasce no segundo mês:* [p=0.2] dez reais, [p=0.2] que são os juros dos cem "
        "do primeiro mês. [p=0.4] {c}Depois, [p=0.2] vinte e um, [p=0.2] trinta e três e dez... [p=0.2] e cresce *sem "
        "parar.* [p=0.2] É a bola de neve."),

    # ================= BLOCO D: A FÓRMULA =================
    dict(id="09", block="formula", text=
        "{t}E dá para pular a tabela? [p=0.4] {a}Dá. [p=0.2] Repare que cada mês faz a mesma coisa: [p=0.2] o saldo "
        "*vezes um vírgula dez.* [p=0.4] {b}Mil vezes um vírgula um, [p=0.2] mil e cem. [p=0.2] Vezes um vírgula um, "
        "[p=0.2] mil, duzentos e dez. [p=0.4] {c}Pense em *fatores,* [p=0.2] não em porcentagens somadas: [p=0.2] cada "
        "período *multiplica* o saldo por *um mais i.*"),
    dict(id="10", block="formula", text=
        "{t}E depois de *t* meses? [p=0.4] {a}O capital foi multiplicado *t vezes* pelo mesmo fator. [p=0.2] E "
        "multiplicação repetida [p=0.2] se escreve como *potência.* [p=0.4] {b}*M igual a C vezes, abre parênteses, um "
        "mais i, fecha parênteses, elevado a t.* [p=0.4] {c}O número pequeno lá em cima [p=0.2] é o *expoente.* [p=0.2] "
        "Ele conta quantas vezes o fator foi aplicado: [p=0.2] *três anos, três multiplicações.* [p=0.4] {d}E o número "
        "*um mais i, elevado a t* [p=0.2] tem nome: [p=0.2] *fator de capitalização.*"),

    # ================= BLOCO E: OS JUROS POR DIFERENÇA =================
    dict(id="11", block="jdif", text=
        "{t}E se a questão pedir só os *juros?* [p=0.4] {a}Em juros compostos, [p=0.2] *não existe* fórmula direta dos "
        "juros. [p=0.4] {b}Você calcula o montante [p=0.2] e tira o capital: [p=0.2] *J igual a M menos C.*"),

    # ================= BLOCO F: O EXEMPLO DO MATERIAL =================
    dict(id="12", block="exemplo", text=
        "{t}Agora um exemplo completo. [p=0.3] {a}*Cinco mil reais* [p=0.2] a *dois por cento ao mês,* [p=0.2] durante "
        "*três meses.* [p=0.4] {b}Primeiro, [p=0.2] o fator de *um* mês: [p=0.2] dois por cento a mais [p=0.2] é *um "
        "vírgula zero dois.* [p=0.4] {c}Três meses, [p=0.2] três multiplicações: [p=0.2] *um vírgula zero dois ao cubo.*"),
    dict(id="13", block="exemplo", text=
        "{t}Passo a passo. [p=0.3] {a}Um vírgula zero dois vezes um vírgula zero dois: [p=0.2] *um vírgula zero quatro "
        "zero quatro.* [p=0.4] {b}Vezes um vírgula zero dois de novo: [p=0.2] *um vírgula zero seis um dois zero oito.* "
        "[p=0.4] {c}Montante: [p=0.2] cinco mil vezes esse fator, [p=0.2] *cinco mil, trezentos e seis reais e quatro "
        "centavos.* [p=0.2] Juros: [p=0.2] *trezentos e seis e quatro.* [p=0.4] {d}Em juros simples, [p=0.2] seriam "
        "trezentos redondos. [p=0.2] Os *seis reais e quatro centavos* a mais [p=0.2] são os juros sobre os juros."),

    # ================= ATALHO =================
    dict(id="14", block="atalho", text=
        "{t}E como multiplicar esses fatores *sem calculadora?* [p=0.4] {a}Atalho: [p=0.2] multiplicar por *um vírgula "
        "um* [p=0.2] é somar o número com *o décimo dele.* [p=0.4] {b}Um vírgula vinte e um, [p=0.2] mais zero vírgula "
        "cento e vinte e um: [p=0.2] *um vírgula trezentos e trinta e um.* [p=0.4] {c}E multiplicar por *um vírgula zero "
        "dois* [p=0.2] é somar *dois por cento* do próprio número: [p=0.2] cinco mil mais cem, [p=0.2] cinco mil e cem."),

    # ================= BLOCO G: TAXA E TEMPO =================
    dict(id="15", block="unidade", text=
        "{t}E se a taxa for ao ano [p=0.2] e o prazo, em meses? [p=0.4] {a}A regra é a mesma dos juros simples: [p=0.2] "
        "taxa e tempo *no mesmo período.* [p=0.4] {b}Mas aqui, [p=0.2] *dividir a taxa anual por doze não funciona.* "
        "[p=0.2] Isso tem série própria: [p=0.2] *taxas equivalentes.* [p=0.4] {c}Nas questões deste assunto, [p=0.2] a "
        "taxa já vem no período certo."),

    # ================= BLOCO H: TAXAS DIFERENTES =================
    dict(id="16", block="sequencia", text=
        "{t}E se cada mês tiver uma taxa *diferente?* [p=0.4] {a}Você já viu isso na Porcentagem: [p=0.2] *multiplique os"
        " fatores* de cada período. [p=0.4] {b}Cinco por cento num mês, [p=0.2] dez por cento no outro: [p=0.2] um "
        "vírgula zero cinco [p=0.2] vezes um vírgula dez, [p=0.2] *um vírgula cento e cinquenta e cinco.* [p=0.4] "
        "{c}Aumento de *quinze vírgula cinco por cento,* [p=0.2] e não de quinze."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*Dois mil reais* a juros compostos [p=0.2] de *dez por cento ao mês,* [p=0.2] durante "
        "*dois meses.* [p=0.4] {b}Qual é o montante, [p=0.2] e quanto foi de juros? [p=0.3] *Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Fator de um mês: [p=0.2] *um vírgula um.* [p=0.2] Dois meses: [p=0.2] um vírgula um "
        "ao quadrado, [p=0.2] *um vírgula vinte e um.* [p=0.4] {b}Montante: [p=0.2] dois mil vezes um vírgula vinte e um,"
        " [p=0.2] *dois mil, quatrocentos e vinte reais.* [p=0.4] {c}Juros, [p=0.2] por diferença: [p=0.2] *quatrocentos "
        "e vinte.* [p=0.4] {d}Em juros simples, [p=0.2] seriam quatrocentos."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] juros compostos: juros sobre juros, como bola de neve. "
        "[p=0.5] {b}Dois: [p=0.2] cada período multiplica o saldo por um mais i. [p=0.5] {c}Três: [p=0.2] os juros saem "
        "por diferença: montante menos capital."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] usar a fórmula dos *simples,* [p=0.2] C vezes "
        "um mais i vezes t, [p=0.2] quando o regime é composto. [p=0.2] Daria cinco mil e trezentos, [p=0.2] e não cinco "
        "mil, trezentos e seis. [p=0.4] {b}Parece certo, [p=0.2] porque você acabou de aprender essa fórmula. [p=0.4] "
        "{c}Leia a palavra no enunciado: [p=0.2] *compostos* pede *potência.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] *somar* as taxas. [p=0.2] Dez por cento por dois anos [p=0.2] seria vinte por cento. [p=0.4]"
        " {b}Parece certo, [p=0.2] porque dez mais dez é vinte. [p=0.4] {c}Mas em compostos [p=0.2] é um vírgula um ao "
        "quadrado, [p=0.2] um vírgula vinte e um: [p=0.2] *vinte e um por cento.*"),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] responder o *montante* quando pedem os *juros,* [p=0.2] ou o contrário. [p=0.2] Cinco mil, "
        "trezentos e seis [p=0.2] no lugar de trezentos e seis. [p=0.4] {b}Parece certo, [p=0.2] porque a fórmula entrega"
        " o montante, [p=0.2] e ele está nas alternativas. [p=0.4] {c}Se a pergunta é *quanto rendeu,* [p=0.2] tire o "
        "capital."),
    dict(id="23", block="erros", text=
        "{a}Quarto: [p=0.2] contar *um período a mais.* [p=0.2] Três anos [p=0.2] viram expoente quatro. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque do ano zero ao ano três [p=0.2] há quatro números. [p=0.4] {c}Mas o expoente "
        "conta *multiplicações:* [p=0.2] três anos, [p=0.2] *expoente três.*"),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="24", block="q1", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Eu resolvo com você. "
        "[p=0.4] {a}Uma pessoa aplicou *dez mil reais* [p=0.2] a juros compostos de *dez por cento ao ano.* [p=0.2] Sem "
        "novos depósitos nem retiradas, [p=0.2] o *saldo* ao final de *três anos* será de: [p=0.4] {qa}A: [p=0.2] três "
        "mil, trezentos e dez reais. [p=0.3] {qb}B: [p=0.2] treze mil. [p=0.3] {qc}C: [p=0.2] treze mil, trezentos e dez."
        " [p=0.3] {qd}D: [p=0.2] catorze mil. [p=0.3] {qe}E: [p=0.2] catorze mil, seiscentos e quarenta e um reais."),
    dict(id="25", block="q1", text=
        "{t}Primeiro, [p=0.2] o fator de *um* ano: [p=0.2] dez por cento a mais, [p=0.2] *um vírgula um.* [p=0.4] {a}Três"
        " anos, [p=0.2] três multiplicações: [p=0.2] *um vírgula um ao cubo.* [p=0.2] Um vírgula um, [p=0.2] um vírgula "
        "vinte e um, [p=0.2] *um vírgula trezentos e trinta e um.* [p=0.4] {b}Saldo: [p=0.2] dez mil vezes um vírgula "
        "trezentos e trinta e um, [p=0.2] *treze mil, trezentos e dez reais.* [p=0.4] {c}E a pergunta? [p=0.2] O *saldo,*"
        " [p=0.2] que é o montante. [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="q1", text=
        "{t}E as outras? [p=0.4] {xb}A B, [p=0.2] treze mil, [p=0.2] é o montante em *juros simples:* [p=0.2] trinta por "
        "cento em três anos. [p=0.4] {xa}A A, [p=0.2] três mil, trezentos e dez, [p=0.2] são *só os juros,* [p=0.2] mas a"
        " pergunta é o saldo. [p=0.4] {xe}A E usou *quatro anos:* [p=0.2] expoente quatro. [p=0.4] {xd}E a D é o montante"
        " simples [p=0.2] desse mesmo prazo errado."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="27", block="q5", text=
        "{t}E agora é *sua.* [p=0.3] {a}Um investimento de risco rendeu *dez por cento* no primeiro mês [p=0.2] e *vinte "
        "por cento* no segundo, [p=0.2] mas teve *perda de vinte e cinco por cento* no terceiro. [p=0.2] Em relação ao "
        "valor investido no início, [p=0.2] ao final do terceiro mês o investidor teve: [p=0.4] {qa}A: [p=0.2] perda de "
        "um por cento. [p=0.3] {qb}B: [p=0.2] ganho de cinco por cento. [p=0.3] {qc}C: [p=0.2] ganho de um por cento. "
        "[p=0.3] {qd}D: [p=0.2] ganho de trinta por cento. [p=0.3] {qe}E: [p=0.2] resultado nulo. [p=0.4] {b}Escreva o "
        "fator de cada mês. [p=0.2] *Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="28", block="q5", text=
        "{t}Conferindo. [p=0.3] {a}Os fatores: [p=0.2] *um vírgula dez,* [p=0.2] *um vírgula vinte* [p=0.2] e, na perda, "
        "[p=0.2] *zero vírgula setenta e cinco.* [p=0.4] {b}O um vírgula dez vezes um vírgula vinte, [p=0.2] um vírgula "
        "trinta e dois, [p=0.2] você já conhece da série de Porcentagem. [p=0.4] {c}Agora, [p=0.2] um vírgula trinta e "
        "dois vezes zero vírgula setenta e cinco: [p=0.2] *zero vírgula noventa e nove.* [p=0.4] {d}Sobrou noventa e nove"
        " por cento do início: [p=0.2] *perda de um por cento.* [p=0.3] {ok}*Letra A!*"),
    dict(id="29", block="q5", text=
        "{t}E as armadilhas? [p=0.4] {xb}A B *somou as taxas:* [p=0.2] dez mais vinte menos vinte e cinco, [p=0.2] cinco."
        " [p=0.2] É o raciocínio dos simples. [p=0.4] {xd}A D somou *só os ganhos.* [p=0.4] {xc}A C acertou o tamanho "
        "[p=0.2] e *errou o sinal.* [p=0.4] {xe}E a E achou que ganhos e perda *quase se anulam.* [p=0.2] Não se anulam: "
        "[p=0.2] a perda incide sobre um valor *maior.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] juros compostos: juros sobre juros, como bola de "
        "neve. [p=0.5] {b}Dois: [p=0.2] cada período multiplica o saldo por um mais i. [p=0.5] {c}Três: [p=0.2] os juros "
        "saem por diferença: montante menos capital."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Se juros compostos são juros sobre juros, [p=0.2] eles sempre rendem mais que os simples, [p=0.2] certo? "
        "[p=0.5] {b}*Errado:* [p=0.3] existe um prazo em que os *simples ganham.* [p=0.5] {c}Próximo episódio."),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] você já tinha somado taxas que deviam ser multiplicadas? [p=0.5] {anki}E tem mais: "
        "[p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o "
        "aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, e "
        "*até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
