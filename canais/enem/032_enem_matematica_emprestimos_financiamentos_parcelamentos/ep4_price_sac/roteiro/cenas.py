# Roteiro — Empréstimos, Financiamentos e Parcelamentos, Episódio 4 de 5: o sistema Price (parcelas fixas) e SAC × Price
# Base: Estudos/Enem/estudos/01-matematica/17-emprestimos-financiamentos-parcelamentos.html — seções 07 e 08
#   + Questões 4, 9 e 5 (seção 12). A fórmula da parcela da Price NÃO é cobrada: o fator vem dado.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   Na Price, a parcela é uma CAIXA DE TAMANHO FIXO: dentro dela, o juro (laranja) encolhe e a amortização (azul)
#   ocupa o espaço que sobra.
#   No SAC, FATIAS IGUAIS DE DÍVIDA (episódio 3); na Price, CAIXAS IGUAIS DE PAGAMENTO.
#   Antes de calcular juros, pergunte: QUANTO SE DEVE AGORA?
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplo da seção 07 (blocos a–e): R$ 10.000,00, 5 parcelas, 4% a.m., fator 0,224627 → parcela ≈ 2.246,27.
#   Linha 1: juros 400; amortização 1.846,27; saldo 8.153,73. Linha 2: juros 326,15; amortização 1.920,12;
#   saldo 6.233,61. Total de juros 1.231,35 (o último mês absorve o arredondamento). SAC: amortização 2.000;
#   1ª parcela 2.400; total de juros 1.200. Segundo mês (bloco e, conta NOSSA): SAC deve 8.000 → juros 320;
#   Price deve 8.153,73 → juros 326,15.
# Atalhos (verde, NOSSOS): "total pago = parcela × nº de parcelas; juros totais = total − valor financiado"
#   (2.246,27 × 5 = 11.231,35 → 1.231,35) · "quanto da 1ª parcela abate a dívida = parcela − taxa × valor financiado"
#   · conferência de plausibilidade "parcela um pouco maior que valor ÷ nº de parcelas" (é a do material, Q4).
# Nós fazemos (prompt): R$ 5.000,00, 5 parcelas de R$ 1.091,77, 3% a.m. → juros 150; amortização 941,77;
#   saldo 4.058,23 (conferido: o fator da Price para 3% e 5 meses é 0,218355 → 1.091,77).
# O erro 3 usa o exemplo de 10.000 (10.000 − 2.246,27 = 7.753,73, errado; certo 8.153,73), para não entregar a Q9.
# QUESTÃO 4 (eu faço, texto idêntico na tela): 20.000 × 0,0946 = 1.892 → C. Erradas (material): A ignora os juros;
#   B aplica 2% uma vez sobre a parcela sem juros (1.666,67 × 1,02 = 1.700); D juros simples de 24% sobre o total,
#   dividido por 12 (24.800 ÷ 12 = 2.066,67); E é o total pago (12 × 1.892 = 22.704).
# QUESTÃO 9 (nós fazemos, texto idêntico): juros 400; amortização 1.492; saldo 18.508 → D. Erradas (material):
#   A é a amortização; B abate a parcela inteira (18.108); C usa a amortização do SAC (20.000 − 1.666,67 = 18.333,33);
#   E soma os juros sem descontar o pagamento (20.400).
# QUESTÃO 5 (você faz, texto idêntico): A. Erradas (material): B troca os sistemas (amortização constante é do SAC);
#   C confunde taxa fixa com juros fixos; D inverte (a 1ª parcela MAIOR é a do SAC); E ignora que o SAC gera menos juros.
#   O prompt pede "qual troca de sistema ela faz": B e D trocam SAC e Price; C não descreve nenhum dos dois (nos dois os
#   juros caem); E apaga a diferença entre eles. Assim no vídeo.
# Frases-chave (meio e fim, idênticas): 1. Na Price, a parcela é fixa e a amortização cresce.
#   2. Na primeira parcela, os juros são iguais nos dois sistemas: taxa × valor financiado.
#   3. Mesma taxa, mas o SAC paga menos juros porque abate a dívida mais cedo.
# Cores: azul = definição (e a amortização nas caixas) · laranja/âmbar = juros e armadilha · roxo = regra/fórmula ·
#   verde = atalho/dica · vermelho = erro.

TITULO = ("Sistema Price e SAC × Price: parcela fixa, juros e amortização · Matemática ENEM, Empréstimos e "
          "Financiamentos episódio 4")

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
    "SAC": "Sac",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Mesma dívida, [p=0.2] mesma taxa, [p=0.2] mesmo prazo. [p=0.4] {b}Num sistema você paga *mil e duzentos "
        "reais* de juros; [p=0.3] {c}no outro, [p=0.2] *mil, duzentos e trinta e um reais e trinta e cinco centavos.* "
        "[p=0.5] {d}A taxa é igual. [p=0.3] *O que muda?*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular a parcela da *Price* com o fator dado, [p=0.3] {b}separar "
        "*juros* e *amortização* [p=0.3] {c}e dizer quando o *SAC* ou a *Price* paga menos."),
    dict(id="03", block="prereq", text=
        "{t}Um lembrete rápido do episódio três. [p=0.3] {a}Toda parcela tem três contas, [p=0.2] sempre nesta ordem: "
        "[p=0.2] *juros* é a taxa vezes o saldo; [p=0.2] *amortização* é a parte da parcela que abate a dívida; "
        "[p=0.2] e o *novo saldo* é o saldo menos a amortização. [p=0.4] {b}E no *SAC,* [p=0.2] a dívida é cortada em "
        "*fatias iguais:* [p=0.2] a amortização é sempre a mesma."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense num *carnê* de loja. [p=0.3] {a}Uma compra no *crediário,* [p=0.2] a prazo, [p=0.2] em doze parcelas "
        "mensais [p=0.2] *todas iguais.* [p=0.4] {b}Agora a pergunta: [p=0.2] se a "
        "parcela é sempre igual, [p=0.3] *a dívida cai sempre o mesmo valor?* [p=0.6] {c}Guarde o seu palpite."),

    # ================= BLOCO A: A PRICE =================
    dict(id="05", block="price", text=
        "{t}Que sistema é esse, [p=0.2] de parcela sempre igual? [p=0.4] {a}É o *sistema Price,* [p=0.2] também "
        "chamado de *francês.* [p=0.3] {b}Nele, todas as parcelas são iguais: [p=0.2] é a *parcela fixa.* [p=0.4] "
        "{c}E de onde sai o valor dela? [p=0.2] De uma fórmula comprida, [p=0.2] que o ENEM *não cobra.* [p=0.3] A prova "
        "dá o *fator da Price* [p=0.2] ou a própria parcela."),
    dict(id="06", block="price", text=
        "{t}E como se usa o fator? [p=0.3] {a}Uma multiplicação: [p=0.2] *parcela é o valor financiado vezes o fator.* "
        "[p=0.4] {b}Exemplo: [p=0.2] *dez mil reais* em *cinco parcelas,* [p=0.2] a *quatro por cento* ao mês, "
        "[p=0.2] com o fator da tela. [p=0.4] {c}Dez mil vezes o fator: [p=0.2] "
        "*dois mil, duzentos e quarenta e seis reais* [p=0.2] e uns centavos, por mês. [p=0.4] {d}Faz sentido? "
        "[p=0.2] Sem juros, [p=0.2] seriam dez mil dividido por cinco, [p=0.2] dois mil. [p=0.2] Com juros, [p=0.2] "
        "*um pouco mais.* [p=0.2] Bateu."),
    dict(id="07", block="atalho1", text=
        "{t}E quanto se paga de juros no total? [p=0.4] {a}Atalho: [p=0.2] parcela fixa vezes o número de parcelas "
        "[p=0.2] é o *total pago:* [p=0.2] *onze mil, duzentos e trinta e um.* [p=0.4] {b}Tire os dez mil emprestados: "
        "[p=0.2] sobram *mil, duzentos e trinta e um* de juros. [p=0.3] O número do começo da aula."),

    # ================= BLOCO B: A TABELA =================
    dict(id="08", block="tabela", text=
        "{t}Mas dentro de cada parcela, [p=0.2] quanto é juro [p=0.2] e quanto abate a dívida? [p=0.4] {a}Antes de "
        "calcular juros, [p=0.2] pergunte: [p=0.2] *quanto se deve agora?* [p=0.2] No primeiro mês, [p=0.2] dez mil. "
        "[p=0.4] {b}Juros: [p=0.2] quatro por cento de dez mil, [p=0.2] *quatrocentos.* [p=0.4] {c}Amortização: "
        "[p=0.2] a parcela menos os juros, [p=0.2] *mil, oitocentos e quarenta e seis e vinte e sete.* [p=0.4] {d}Novo "
        "saldo: [p=0.2] dez mil menos a amortização, [p=0.2] *oito mil, cento e cinquenta e três e setenta e três.*"),
    dict(id="09", block="tabela", text=
        "{t}E no segundo mês? [p=0.2] Quanto se deve agora? [p=0.3] {a}Oito mil, cento e cinquenta e três. [p=0.2] Os "
        "juros são quatro por cento disso: [p=0.2] *trezentos e vinte e seis e quinze.* [p=0.4] {b}Os juros *caíram.* "
        "[p=0.2] E a parcela não mudou. [p=0.2] Então a amortização *cresceu:* [p=0.2] *mil, novecentos e vinte e doze.* "
        "[p=0.4] {c}É a *amortização crescente:* [p=0.2] mês a mês, [p=0.2] uma parte maior da parcela abate a "
        "dívida. [p=0.4] {d}E o último mês acerta os centavos."),
    dict(id="10", block="caixa", text=
        "{t}Lembra do palpite? [p=0.2] A dívida *não* cai sempre o mesmo valor. [p=0.4] {a}Pense na parcela como uma "
        "*caixa de tamanho fixo.* [p=0.3] {b}Dentro dela, [p=0.2] o *juro,* em laranja, [p=0.2] vai encolhendo, "
        "[p=0.3] {c}e a *amortização,* em azul, [p=0.2] vai ocupando o espaço que sobra. [p=0.4] {d}No último mês, "
        "[p=0.2] a caixa é quase toda azul."),

    # ================= BLOCO C: A PRIMEIRA LINHA =================
    dict(id="11", block="linha1", text=
        "{t}E pelo *SAC,* [p=0.2] muda o juro da primeira parcela? [p=0.4] {a}Não. "
        "[p=0.2] Nos dois, [p=0.2] se deve dez mil. [p=0.3] Juros de *quatrocentos* "
        "[p=0.2] no SAC [p=0.2] *e* na Price. [p=0.4] {b}O que muda é a amortização. [p=0.3] No SAC, [p=0.2] *fixa:* "
        "[p=0.2] dez mil dividido por cinco, [p=0.2] dois mil. [p=0.3] {c}Na Price, [p=0.2] *a parcela menos os juros:* "
        "[p=0.2] mil, oitocentos e quarenta e seis."),
    dict(id="12", block="atalho2", text=
        "{t}E se a questão perguntar só quanto da primeira parcela abate a dívida? [p=0.4] {a}Atalho: [p=0.2] você nem "
        "precisa da tabela. [p=0.3] *Parcela menos taxa vezes o valor financiado.* [p=0.4] {b}Uma linha [p=0.2] e "
        "acabou."),

    # ================= BLOCO D: LADO A LADO =================
    dict(id="13", block="lado", text=
        "{t}E como fica o empréstimo inteiro, [p=0.2] lado a lado? [p=0.4] {a}No SAC, [p=0.2] *fatias iguais de "
        "dívida:* [p=0.2] a amortização é *constante,* [p=0.2] e a parcela *diminui* todo mês. [p=0.4] {b}Na Price, "
        "[p=0.2] *caixas iguais de pagamento:* [p=0.2] a parcela é *constante,* [p=0.2] e a amortização *cresce.* "
        "[p=0.4] {c}E nos dois, [p=0.2] os juros *caem.*"),
    dict(id="14", block="lado", text=
        "{t}E quem começa pagando mais? [p=0.4] {a}O SAC: [p=0.2] primeira parcela de *dois mil e quatrocentos,* "
        "[p=0.2] contra *dois mil, duzentos e quarenta e seis* da Price. [p=0.4] {b}E no total de juros? "
        "[p=0.3] A Price paga *mil, duzentos e trinta e um;* [p=0.2] o SAC, *mil e duzentos.* [p=0.4] {c}O SAC começa *mais pesado* [p=0.2] e termina *mais barato.*"),

    # ================= BLOCO E: POR QUE O SAC PAGA MENOS =================
    dict(id="15", block="porque", text=
        "{t}Mas, se a taxa é a mesma, [p=0.2] por que o SAC paga menos juros? [p=0.4] {a}Volte à pergunta: [p=0.2] "
        "*quanto se deve agora?* [p=0.3] {b}Depois da primeira parcela, [p=0.2] no SAC você deve *oito mil.* [p=0.2] Na "
        "Price, [p=0.2] *oito mil, cento e cinquenta e três.* [p=0.4] {c}No segundo mês, [p=0.2] juros de *trezentos e vinte* "
        "contra *trezentos e vinte e seis.* [p=0.4] {d}O SAC abate "
        "a dívida *mais depressa,* [p=0.2] e juro só incide sobre o que se deve."),
    dict(id="16", block="porque", text=
        "{t}E onde cada um aparece? [p=0.3] {a}O SAC é comum no *financiamento imobiliário:* [p=0.2] a casa em muitos anos. "
        "[p=0.4] {b}A Price, no *crediário* [p=0.2] e no *crédito pessoal:* [p=0.2] a parcela fixa é *previsível.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Cinco mil reais pela Price, [p=0.2] em cinco parcelas de *mil e noventa e um e setenta e "
        "sete,* [p=0.2] a *três por cento* ao mês. [p=0.4] {b}Quanto da primeira parcela é juros, [p=0.2] quanto "
        "amortiza [p=0.2] e qual é o saldo depois dela? [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos, [p=0.2] na ordem. [p=0.3] {a}Quanto se deve agora? [p=0.2] Cinco mil. [p=0.2] Juros: "
        "[p=0.2] três por cento de cinco mil, [p=0.2] *cento e cinquenta.* [p=0.4] {b}Amortização: [p=0.2] mil e "
        "noventa e um e setenta e sete, [p=0.2] menos cento e cinquenta: [p=0.2] *novecentos e quarenta e um e setenta "
        "e sete.* [p=0.4] {c}Saldo: [p=0.2] cinco mil menos a amortização: [p=0.2] *quatro mil e cinquenta e oito e "
        "vinte e três.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] na Price, a parcela é fixa e a amortização cresce. "
        "[p=0.5] {b}Dois: [p=0.2] na primeira parcela, os juros são iguais nos dois sistemas: [p=0.2] taxa vezes valor "
        "financiado. [p=0.5] {c}Três: [p=0.2] mesma taxa, mas o SAC paga menos juros [p=0.2] porque abate a dívida mais "
        "cedo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que, na Price, [p=0.2] a *amortização* "
        "é constante. [p=0.4] {b}Parece certo, [p=0.2] porque *alguma coisa* é constante na Price. [p=0.4] {c}Mas "
        "constante é a *parcela.* [p=0.2] Amortização constante [p=0.2] é o *SAC.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] achar que SAC e Price custam os *mesmos juros.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "a taxa, o prazo e a dívida são iguais. [p=0.4] {c}Mas o juro depende de *quanto se deve,* [p=0.2] e o SAC "
        "deve menos mais cedo."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] abater a *parcela inteira* do saldo. [p=0.4] {b}Parece certo, [p=0.2] porque você "
        "pagou a parcela inteira. [p=0.4] {c}Mas os quatrocentos de juros *não* abatem nada: [p=0.2] são o aluguel do "
        "dinheiro. [p=0.2] Só a *amortização* sai do saldo."),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="23", block="q4", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Esta primeira, [p=0.2] eu "
        "resolvo com você. [p=0.4] {a}Uma pessoa financiou *vinte mil reais* [p=0.2] em *doze* parcelas mensais "
        "iguais, [p=0.2] pelo sistema Price, [p=0.2] com juros de *dois por cento* ao mês. [p=0.2] A parcela é o "
        "valor financiado vezes o fator *zero vírgula zero, nove, quatro, seis.* [p=0.2] Cada parcela vale: [p=0.4] {qa}A: [p=0.2] mil, seiscentos e sessenta e seis e sessenta e sete. "
        "[p=0.3] {qb}B: [p=0.2] mil e setecentos. [p=0.3] {qc}C: [p=0.2] mil, oitocentos e noventa e dois. [p=0.3] "
        "{qd}D: [p=0.2] dois mil e sessenta e seis e sessenta e sete. [p=0.3] {qe}E: [p=0.2] vinte e dois mil, "
        "setecentos e quatro."),
    dict(id="24", block="q4", text=
        "{t}Que sistema é? [p=0.2] *Price,* [p=0.2] com o fator dado. [p=0.3] {a}Então é só multiplicar: [p=0.2] vinte "
        "mil vezes zero vírgula zero, nove, quatro, seis: [p=0.2] *mil, oitocentos e noventa e dois reais.* [p=0.4] "
        "{b}Plausível? [p=0.2] Sem juros, [p=0.2] vinte mil dividido por doze, [p=0.2] uns mil, seiscentos e "
        "sessenta e sete. [p=0.2] Com juros, *um pouco mais.* [p=0.2] Bateu. [p=0.3] {ok}*Letra C!*"),
    dict(id="25", block="q4", text=
        "{t}E as erradas? [p=0.3] {xa}A A *ignorou os juros:* [p=0.2] é a parcela sem juros. [p=0.4] {xb}A B aplicou "
        "dois por cento *uma vez só* [p=0.2] sobre essa parcela sem juros. [p=0.4] {xd}A D fez *juros simples:* "
        "[p=0.2] vinte e quatro por cento sobre o total, [p=0.2] dividido por doze. [p=0.4] {xe}E a E [p=0.2] é o "
        "*total pago* nas doze parcelas, [p=0.2] não a parcela."),

    # ================= QUESTÃO 9 (NÓS FAZEMOS) =================
    dict(id="26", block="q9", text=
        "{t}A próxima, a gente faz junto. [p=0.3] {a}No mesmo financiamento da questão anterior, [p=0.2] o *saldo "
        "devedor* logo depois da primeira parcela é: [p=0.4] {qa}A: [p=0.2] mil, quatrocentos e noventa e dois. "
        "[p=0.3] {qb}B: [p=0.2] dezoito mil, cento e oito. [p=0.3] {qc}C: [p=0.2] dezoito mil, trezentos e trinta e "
        "três e trinta e três. [p=0.3] {qd}D: [p=0.2] dezoito mil, quinhentos e oito. [p=0.3] {qe}E: [p=0.2] vinte "
        "mil e quatrocentos. [p=0.5] {p}Lembre da ordem: [p=0.2] juros, amortização, saldo. [p=0.2] *Pause e tente.* "
        "[p=2.0]"),
    dict(id="27", block="q9", text=
        "{t}Quanto se deve agora? [p=0.2] Vinte mil. [p=0.3] {a}Juros: [p=0.2] dois por cento de vinte mil, [p=0.2] "
        "*quatrocentos.* [p=0.4] {b}Amortização: [p=0.2] mil, oitocentos e noventa e dois menos quatrocentos, [p=0.2] "
        "*mil, quatrocentos e noventa e dois.* [p=0.4] {c}Novo saldo: [p=0.2] vinte mil menos a amortização: [p=0.2] "
        "*dezoito mil, quinhentos e oito.* [p=0.4] {d}Caiu pouco? [p=0.2] Faz sentido: [p=0.2] no começo, [p=0.2] a caixa tem muito juro. [p=0.3] {ok}*Letra D!*"),
    dict(id="28", block="q9", text=
        "{t}E as outras? [p=0.3] {xb}A B [p=0.2] abateu a *parcela inteira:* [p=0.2] o erro número três. [p=0.4] "
        "{xc}A C [p=0.2] usou a amortização do *SAC,* [p=0.2] vinte mil dividido por doze. [p=0.4] {xa}A A [p=0.2] "
        "parou na amortização: [p=0.2] respondeu o que abateu, [p=0.2] não o que sobrou. [p=0.4] {xe}E a E [p=0.2] "
        "somou os juros à dívida [p=0.2] e esqueceu que a parcela foi paga."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="29", block="q5", text=
        "{t}E esta é *sua.* [p=0.3] {a}O mesmo financiamento, [p=0.2] mesma taxa, [p=0.2] mesmo número de parcelas, "
        "[p=0.2] pelo SAC ou pela Price. [p=0.2] É correto afirmar que: [p=0.4] {qa}A: "
        "[p=0.2] no SAC, as parcelas diminuem, [p=0.2] porque a amortização é constante [p=0.2] e o saldo cai. [p=0.3] {qb}B: [p=0.2] na Price, a amortização é a mesma em todas as parcelas. "
        "[p=0.3] {qc}C: [p=0.2] no SAC, os juros de cada parcela são iguais, [p=0.2] pois a taxa é fixa. [p=0.3] "
        "{qd}D: [p=0.2] na Price, a primeira parcela é maior que a do SAC. [p=0.3] {qe}E: [p=0.2] os dois resultam no "
        "mesmo total de juros. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{t}Conferindo. [p=0.3] {a}A A descreve *exatamente* o SAC: [p=0.2] fatias iguais de dívida, [p=0.2] o saldo "
        "caindo, [p=0.2] os juros e as parcelas diminuindo. [p=0.3] {ok}*Letra A!*"),
    dict(id="31", block="q5", text=
        "{t}E que troca cada errada faz? [p=0.3] {xb}A B [p=0.2] *troca os sistemas:* [p=0.2] amortização constante é "
        "do SAC. [p=0.4] {xd}A D também troca: [p=0.2] a primeira parcela *maior* é a do SAC. [p=0.4] {xc}A C confunde "
        "*taxa* fixa com *juros* fixos: [p=0.2] nos dois sistemas, os juros caem. [p=0.4] {xe}E a E apaga a diferença: "
        "[p=0.2] o SAC abate mais cedo [p=0.2] e paga menos."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] na Price, a parcela é fixa e a amortização "
        "cresce. [p=0.5] {b}Dois: [p=0.2] na primeira parcela, os juros são iguais nos dois sistemas: [p=0.2] taxa "
        "vezes valor financiado. [p=0.5] {c}Três: [p=0.2] mesma taxa, mas o SAC paga menos juros [p=0.2] porque abate "
        "a dívida mais cedo."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] {c}e "
        "treinamos com *questões inéditas.*"),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já sabia que a parcela fixa custa mais juros? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
