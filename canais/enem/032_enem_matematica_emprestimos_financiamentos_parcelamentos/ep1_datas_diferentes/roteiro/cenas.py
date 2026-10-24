# Roteiro — Empréstimos, Financiamentos e Parcelamentos, Episódio 1 de 5: dinheiro em datas diferentes
#   (parcelas, quitação antecipada e rotativo do cartão)
# Base: Estudos/Enem/estudos/01-matematica/17-emprestimos-financiamentos-parcelamentos.html — seções 03 e 09
#   + Questões 7 e 6 (seção 12) + QUESTÃO NOVA do prompt (no lugar da Questão 8, que repete a Q3 de Juros Compostos).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   MOEDAS DE PAÍSES DIFERENTES: valores em datas diferentes só se somam depois do CÂMBIO para a mesma data.
#   PARA O FUTURO, MULTIPLIQUE PELO FATOR; PARA O PRESENTE, DIVIDA. Cada parcela viaja pelo SEU prazo.
#   JUROS SÃO O ALUGUEL DO DINHEIRO: só se paga aluguel do que ainda está com você (o saldo não pago).
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos (material/prompt): 2.662 ÷ 1,331 = 2.000; duas de 1.210 → 1.100 + 1.000 = 2.100 (gancho e bloco c, como o
#   prompt pede: são os números da Q6, que é "nós fazemos" — mantidos); rotativo 2.000 − 500 = 1.500 → 1.500 · 1,12 =
#   1.680; 3 meses 1.500 · 1,12³ ≈ 1.500 · 1,405 ≈ 2.107,50 (versão do material; o vídeo NÃO usa 2.107,39 junto);
#   12% três vezes ≈ 40,5%, não 36%. Nós fazemos (prompt): 1.100 ÷ 1,1 + 1.210 ÷ 1,21 = 1.000 + 1.000 = 2.000.
#   Erro 2 (NOSSO, com os números do "nós fazemos", já resolvido): descontar as duas por 1 mês só → 1.000 + 1.100 = 2.100,
#   cem a mais que os 2.000 certos. Erro 3 (prompt): dois meses a 10% → × 1,21, não × 1,20.
#   Atalho (NOSSO, verde): dividir por 1,1 / 1,21 / 1,331 = dividir por 11 / 121 / 1.331 e acrescentar 1 / 2 / 3 zeros.
#   Conferência (prompt): o valor hoje é sempre MENOR que a soma das parcelas.
# QUESTÃO 7 (eu faço; erradas do material, que estão certas): 800 · 1,21 = 968 (C). A = só um mês (880); B = juros
#   simples, 20% (960); D = soma de volta os 200 pagos (1.168); E = juros sobre a fatura inteira (1.210).
# QUESTÃO 6 (nós fazemos; erradas do material, certas): 1.100 + 1.000 = 2.100 (C). E = somou sem descontar (2.420);
#   B = descontou as duas por 2 meses (2.000); D = tirou 10% do total (2.178); A = tirou 20% do total (1.936).
# QUESTÃO NOVA (você faz; texto, gabarito e erradas do prompt, conferidos): 1.210 + 1.100 + 1.000 = 3.310 (B).
#   A = as três por 3 meses (3.000); C = tirou 10% de cada uma vez só (3 · 1.197,90 = 3.593,70); D = as três por 1 mês
#   (3.630); E = somou sem trazer (3.993).
# Frases-chave (meio e fim, idênticas): 1. Só se somam valores na mesma data. 2. Para o futuro, multiplique pelo fator;
#   para o presente, divida. 3. Juros incidem sobre o que ainda se deve.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = ("Parcelas, quitação e rotativo: dinheiro em datas diferentes · Matemática ENEM, Empréstimos e "
          "financiamentos episódio 1")

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
        "{a}Duas parcelas de *mil, duzentos e dez reais* [p=0.2] somam *dois mil, quatrocentos e vinte,* certo? [p=0.4] "
        "{b}Na calculadora, sim. [p=0.3] {c}No tempo, a dez por cento ao mês, [p=0.2] elas valem hoje *dois mil e cem "
        "reais.* [p=0.4] {d}Somar parcelas de datas diferentes [p=0.2] é *somar real com dólar.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular *quanto vale hoje* uma sequência de parcelas, [p=0.3] "
        "{b}quanto custa *quitar uma dívida* antes do prazo [p=0.3] {c}e quanto cresce o *rotativo do cartão.*"),
    dict(id="03", block="prereq", text=
        "{t}Um lembrete rápido, [p=0.2] da série de Juros Compostos. [p=0.3] {a}Para o futuro, [p=0.2] *M igual a C "
        "vezes um mais i, elevado a t.* [p=0.2] Para hoje, [p=0.2] *divida* pelo mesmo fator. [p=0.4] {b}E duas "
        "potências: [p=0.2] um vírgula um ao quadrado [p=0.2] é *um vírgula vinte e um.* [p=0.2] "
        "Ao cubo, [p=0.2] *um vírgula trezentos e trinta e um.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Pense num *carnê,* [p=0.2] o caderninho de boletos de uma compra parcelada. [p=0.2] Cada boleto é uma "
        "*parcela,* [p=0.2] com a sua data. [p=0.4] {b}Um dia chega um aviso: [p=0.2] *quite seu "
        "financiamento com desconto.* [p=0.4] {c}E na fatura do cartão [p=0.2] aparece um botão tentador: [p=0.2] "
        "*pagar o mínimo.* [p=0.4] {d}As três têm a mesma conta escondida."),
    dict(id="05", block="concreto", text=
        "{t}Para enxergar essa conta, [p=0.2] desenhe uma *linha do tempo.* [p=0.4] {a}Um traço deitado, "
        "[p=0.2] com as datas: [p=0.2] zero, um, dois, três meses. [p=0.4] {b}A *data zero* é *hoje.* [p=0.4] "
        "{c}E cada parcela vira uma *moedinha* [p=0.2] em cima da sua data."),

    # ================= BLOCO A: MIL HOJE ≠ MIL AMANHÃ =================
    dict(id="06", block="datas", text=
        "{t}Mil reais hoje [p=0.2] valem o mesmo que mil reais daqui a um mês? [p=0.5] {a}Não. [p=0.2] O dinheiro de "
        "hoje pode *render juros.* [p=0.2] Aplicado a dez por cento, [p=0.2] daqui a um mês ele vira *mil e cem.* "
        "[p=0.4] {b}Por isso, [p=0.2] valores em datas diferentes [p=0.2] são como *moedas de países diferentes.* "
        "[p=0.4] {c}Antes de somar, [p=0.2] você faz o *câmbio* [p=0.2] para a mesma data."),
    dict(id="07", block="datas", text=
        "{t}Dois nomes para guardar. [p=0.3] {a}*Valor presente* [p=0.2] é quanto o dinheiro vale *hoje,* [p=0.2] na "
        "data zero. [p=0.4] {b}*Valor futuro* [p=0.2] é quanto ele vale *lá na frente,* [p=0.2] numa data depois. "
        "[p=0.4] {c}O câmbio entre eles [p=0.2] é o *fator:* [p=0.2] um mais i, elevado aos meses."),

    # ================= BLOCO B: LEVAR E TRAZER =================
    dict(id="08", block="levar", text=
        "{t}E para que lado é a conta? [p=0.4] {a}Para o *futuro,* [p=0.2] *multiplique* pelo fator. [p=0.4] {b}Para o "
        "*presente,* [p=0.2] *divida.* [p=0.4] {c}Exemplo do material: [p=0.2] quanto valem hoje *dois mil, seiscentos e "
        "sessenta e dois reais,* [p=0.2] a receber daqui a *três meses,* [p=0.2] a dez por cento ao mês? [p=0.4] "
        "{d}Três meses: [p=0.2] o fator é *um vírgula trezentos e trinta e um.* [p=0.2] Dois mil, seiscentos e sessenta "
        "e dois, [p=0.2] dividido por ele: [p=0.2] *dois mil reais.*"),
    dict(id="09", block="levar", text=
        "{t}E dividir por um vírgula trezentos e trinta e um, [p=0.2] sem calculadora? [p=0.4] {a}Atalho: [p=0.2] tire "
        "a vírgula e devolva com zeros. [p=0.2] Por *um vírgula um,* [p=0.2] divida por *onze* e ponha *um zero.* [p=0.4] "
        "{b}Por *um vírgula vinte e um,* [p=0.2] por *cento e vinte e um* e *dois zeros.* [p=0.4] {c}Por *um vírgula "
        "trezentos e trinta e um,* [p=0.2] por *mil, trezentos e trinta e um* e *três zeros.* [p=0.2] Aqui dá *dois,* "
        "[p=0.2] mais três zeros: [p=0.2] *dois mil.*"),

    # ================= BLOCO C: A SEQUÊNCIA DE PARCELAS =================
    dict(id="10", block="sequencia", text=
        "{t}E quando são *várias* parcelas? [p=0.4] {a}Volte ao gancho: [p=0.2] uma parcela de mil, duzentos e dez "
        "daqui a *um* mês, [p=0.2] outra daqui a *dois.* [p=0.4] {b}Cada moedinha viaja até a data zero [p=0.2] *pelo "
        "seu próprio prazo.* [p=0.4] {c}A de um mês [p=0.2] passa pelo câmbio de *um vírgula um:* [p=0.2] vira *mil e "
        "cem.* [p=0.4] {d}A de dois meses [p=0.2] passa pelo de *um vírgula vinte e um:* [p=0.2] vira *mil.*"),
    dict(id="11", block="sequencia", text=
        "{t}Agora as duas estão na mesma data. [p=0.3] {a}Só agora pode somar: [p=0.2] mil e cem mais mil, [p=0.2] *dois "
        "mil e cem reais.* [p=0.4] {b}É o *valor justo* [p=0.2] para comprar *à vista.* "
        "[p=0.4] {c}E é também o valor da *quitação antecipada:* [p=0.2] pagar hoje, de uma vez, [p=0.2] parcelas que "
        "só venceriam depois."),

    # ================= BLOCO D: ROTATIVO =================
    dict(id="12", block="rotativo", text=
        "{t}E o botão *pagar o mínimo?* [p=0.4] {a}A *fatura* é a conta do mês do cartão: [p=0.2] *dois "
        "mil reais.* [p=0.4] {b}Você paga só *quinhentos.* [p=0.2] O resto, [p=0.2] o *saldo não pago,* [p=0.2] vira um "
        "empréstimo automático: [p=0.2] o *rotativo.* [p=0.4] {c}Juros de *doze por cento ao mês.* [p=0.2] Sobre quanto?"),
    dict(id="13", block="rotativo", text=
        "{t}Pense assim: [p=0.2] *juros são o aluguel do dinheiro.* [p=0.4] {a}E só se paga aluguel [p=0.2] do que "
        "*ainda está com você.* [p=0.2] Os quinhentos já voltaram. [p=0.4] {b}O saldo é *mil e "
        "quinhentos.* [p=0.2] Mil e quinhentos vezes um vírgula doze: [p=0.2] a próxima fatura vem com *mil, seiscentos e "
        "oitenta reais.* [p=0.4] {c}Juros sobre o saldo, [p=0.2] não sobre a fatura inteira."),
    dict(id="14", block="rotativo", text=
        "{t}E se você não pagar nada [p=0.2] por *três meses?* [p=0.4] {a}O saldo é levado ao futuro, [p=0.2] mês a mês. "
        "[p=0.2] Um vírgula doze ao cubo [p=0.2] é mais ou menos *um vírgula quatrocentos e cinco.* [p=0.2] A dívida vai "
        "a uns *dois mil, cento e sete e cinquenta.* [p=0.4] {b}Três meses a doze por cento [p=0.2] "
        "não somam trinta e seis. [p=0.2] Somam uns *quarenta e meio* por cento. [p=0.4] {c}O *cheque especial,* "
        "[p=0.2] o limite extra da conta corrente, [p=0.2] funciona igual, sobre o saldo negativo. [p=0.2] Taxas mensais "
        "assim [p=0.2] viram anuais de *três dígitos.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quanto valem *hoje* [p=0.2] uma parcela de *mil e cem reais* daqui a *um mês* [p=0.2] e "
        "outra de *mil, duzentos e dez* daqui a *dois meses,* [p=0.2] a dez por cento ao mês? [p=0.3] {b}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos, [p=0.2] com a linha do tempo. [p=0.3] {a}A de um mês volta por um vírgula um: [p=0.2] mil e "
        "cem dividido por um vírgula um, [p=0.2] *mil.* [p=0.4] {b}A de dois meses volta por um vírgula vinte e um: "
        "[p=0.2] mil, duzentos e dez dividido por um vírgula vinte e um, [p=0.2] *mil* também. [p=0.4] {c}Na mesma "
        "data, [p=0.2] pode somar: [p=0.2] *dois mil reais.* [p=0.2] Menor que a soma das parcelas, "
        "como tem que ser."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] só se somam valores na mesma data. [p=0.5] {b}Dois: "
        "[p=0.2] para o futuro, multiplique pelo fator; [p=0.2] para o presente, divida. [p=0.5] {c}Três: [p=0.2] "
        "juros incidem sobre o que ainda se deve."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar parcelas de datas diferentes.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque é exatamente o que a calculadora faz. [p=0.4] {c}Mas é somar real com dólar: "
        "[p=0.2] as duas de mil, duzentos e dez [p=0.2] valem hoje *dois mil e cem,* [p=0.2] não dois mil, quatrocentos "
        "e vinte."),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] descontar *todas as parcelas pelo mesmo prazo.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "uma conta só é mais rápida. [p=0.4] {c}Mas cada moedinha viaja pelo *seu* prazo. [p=0.2] No exercício que a "
        "gente fez, [p=0.2] trazer as duas por um mês só [p=0.2] dá *dois mil e cem,* [p=0.2] cem reais a mais que os "
        "dois mil certos."),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] *juros simples* no rotativo. [p=0.4] {b}Parece certo, [p=0.2] porque dez por cento mais "
        "dez por cento [p=0.2] dá vinte. [p=0.4] {c}Mas o rotativo cobra *juros sobre juros:* [p=0.2] dois meses a dez "
        "por cento [p=0.2] multiplicam por *um vírgula vinte e um,* [p=0.2] não por um vírgula vinte."),

    # ================= QUESTÃO 7 (EU FAÇO) =================
    dict(id="21", block="q7", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.4] {a}A fatura de um cartão de "
        "crédito era de *mil reais,* [p=0.2] e o titular pagou apenas *duzentos.* [p=0.2] Sobre o saldo restante "
        "[p=0.2] incidem juros compostos de *dez por cento ao mês.* [p=0.2] Se o titular não fizer nenhum outro "
        "pagamento nem novas compras, [p=0.2] sua dívida *dois meses depois* será de: [p=0.4] {qa}A: [p=0.2] "
        "oitocentos e oitenta reais. [p=0.3] {qb}B: [p=0.2] novecentos e sessenta. [p=0.3] {qc}C: [p=0.2] novecentos e "
        "sessenta e oito. [p=0.3] {qd}D: [p=0.2] mil, cento e sessenta e oito. [p=0.3] {qe}E: [p=0.2] mil, duzentos e "
        "dez."),
    dict(id="22", block="q7", text=
        "{t}Eu resolvo. [p=0.3] {a}Linha do tempo: [p=0.2] hoje, o que *ainda se deve* [p=0.2] é mil menos "
        "duzentos, [p=0.2] *oitocentos.* [p=0.4] {b}Esse saldo vai ao futuro, [p=0.2] dois meses: [p=0.2] vezes *um "
        "vírgula vinte e um.* [p=0.4] {c}Oitocentos vezes um vírgula vinte e um: [p=0.2] *novecentos e sessenta e "
        "oito.* [p=0.3] {ok}*Letra C!*"),
    dict(id="23", block="q7", text=
        "{t}E as outras? [p=0.3] {xa}A A cobra *um mês só* de juros. [p=0.4] {xb}A B usa *juros simples:* [p=0.2] "
        "vinte por cento em dois meses. [p=0.4] {xd}A D *soma de volta* os duzentos que já foram pagos. [p=0.4] {xe}E a "
        "E aplica os juros sobre a *fatura inteira,* [p=0.2] e não sobre o que ficou devendo: [p=0.2] aluguel de "
        "dinheiro que já voltou."),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="24", block="q6", text=
        "{t}Agora, juntos. [p=0.3] {a}Uma compra pode ser paga em *duas parcelas de mil, duzentos e dez "
        "reais,* [p=0.2] com vencimentos em *trinta e sessenta dias,* [p=0.2] sem entrada. [p=0.2] Se a taxa de juros "
        "é de *dez por cento ao mês,* [p=0.2] no regime composto, [p=0.2] o valor *à vista equivalente* a esse "
        "parcelamento é: [p=0.4] {qa}A: [p=0.2] mil, novecentos e trinta e seis. [p=0.3] {qb}B: [p=0.2] dois mil. "
        "[p=0.3] {qc}C: [p=0.2] dois mil e cem. [p=0.3] {qd}D: [p=0.2] dois mil, cento e setenta e oito. [p=0.3] "
        "{qe}E: [p=0.2] dois mil, quatrocentos e vinte. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q6", text=
        "{t}São as parcelas do gancho. [p=0.3] {a}Valor à vista é *valor presente:* [p=0.2] cada parcela volta pelo seu "
        "prazo. [p=0.4] {b}A de trinta dias, [p=0.2] dividida por um vírgula um: [p=0.2] *mil e cem.* [p=0.2] A de "
        "sessenta, [p=0.2] por um vírgula vinte e um: [p=0.2] *mil.* [p=0.4] {c}Total: [p=0.2] *dois mil e cem.* "
        "[p=0.2] Menor que a soma das parcelas. [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="q6", text=
        "{t}E as erradas? [p=0.3] {xe}A E soma as parcelas *sem trazer para hoje.* [p=0.4] {xb}A B desconta as duas "
        "por *dois meses.* [p=0.4] {xd}A D tira *dez por cento do total,* uma vez só. [p=0.4] {xa}E a A tira *vinte por "
        "cento* do total. [p=0.4] {d}Essas duas tratam a taxa como desconto, [p=0.2] não como "
        "*divisão pelo fator.*"),

    # ================= QUESTÃO NOVA (VOCÊ FAZ) =================
    dict(id="27", block="qn", text=
        "{t}Agora é com você. [p=0.3] {a}Um cliente deve as *três últimas parcelas* de um financiamento, [p=0.2] de "
        "*mil, trezentos e trinta e um reais* cada, [p=0.2] com vencimentos daqui a *um, dois e três meses.* [p=0.2] "
        "O contrato permite *quitar a dívida hoje,* [p=0.2] trazendo cada parcela ao presente [p=0.2] pela taxa do "
        "financiamento, [p=0.2] *dez por cento ao mês,* [p=0.2] no regime composto. [p=0.2] Considere um vírgula um ao quadrado igual a um vírgula vinte e um, [p=0.2] "
        "e ao cubo, um vírgula trezentos e trinta e um. [p=0.2] Para quitar a dívida hoje, o cliente deve pagar: [p=0.4] {qa}A: [p=0.2] três mil reais. [p=0.3] {qb}B: [p=0.2] três mil, trezentos e "
        "dez. [p=0.3] {qc}C: [p=0.2] três mil, quinhentos e noventa e três e setenta. [p=0.3] {qd}D: [p=0.2] três mil, "
        "seiscentos e trinta. [p=0.3] {qe}E: [p=0.2] três mil, novecentos e noventa e três. [p=0.4] {p}*Pause o vídeo "
        "e resolva sozinho.* [p=2.5]"),
    dict(id="28", block="qn", text=
        "{t}Confira. [p=0.3] {a}Três moedinhas, [p=0.2] três prazos, [p=0.2] três câmbios. [p=0.4] {b}A de um mês, "
        "[p=0.2] dividida por um vírgula um: [p=0.2] *mil, duzentos e dez.* [p=0.2] A de dois meses, [p=0.2] por um "
        "vírgula vinte e um: [p=0.2] *mil e cem.* [p=0.2] A de três meses, [p=0.2] por um vírgula trezentos e trinta e "
        "um: [p=0.2] *mil.* [p=0.4] {c}Somando: [p=0.2] *três mil, trezentos e dez.* [p=0.2] Menor que a soma das "
        "parcelas. [p=0.3] {ok}*Letra B!*"),
    dict(id="29", block="qn", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A desconta as três por *três meses.* [p=0.4] {xc}A C tira *dez por cento* "
        "de cada parcela, [p=0.2] uma vez só, [p=0.2] como desconto simples. [p=0.4] {xd}A D desconta as três por *um "
        "mês só.* [p=0.4] {xe}E a E soma as parcelas *sem trazer para hoje.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] só se somam valores na mesma data. [p=0.5] "
        "{b}Dois: [p=0.2] para o futuro, multiplique pelo fator; [p=0.2] para o presente, divida. [p=0.5] {c}Três: "
        "[p=0.2] juros incidem sobre o que ainda se deve."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Geladeira: [p=0.2] *mil e novecentos reais* à vista, [p=0.2] ou *duas de mil,* [p=0.2] a primeira no ato. "
        "[p=0.4] {b}Os cem reais a mais [p=0.2] são *cinco por cento* de juros? [p=0.4] {c}São *mais que o dobro* "
        "disso. [p=0.3] Próximo episódio."),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já pagou só o mínimo da fatura? [p=0.5] {anki}E tem mais: "
        "[p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] "
        "o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, "
        "e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
