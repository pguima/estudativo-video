# Roteiro — Empréstimos, Financiamentos e Parcelamentos, Episódio 3 de 5: o Sistema de Amortização Constante (SAC)
# Base: Estudos/Enem/estudos/01-matematica/17-emprestimos-financiamentos-parcelamentos.html — seção 06 e, da seção 02,
#   saldo devedor, juros da parcela, amortização e parcela (com as três relações) + Questões 2 e 3 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   No SAC, a dívida é FATIADA EM FATIAS IGUAIS: a fatia (amortização) é sempre a mesma, e o juro emagrece porque a
#     dívida emagrece.
#   Juros são o ALUGUEL DO DINHEIRO (episódio 1): só se paga aluguel do que ainda se deve, o saldo do início do mês.
#   A ESCADINHA DOS JUROS: eles descem sempre o mesmo degrau, taxa × amortização.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplo dos blocos: o da seção 06 (R$ 10.000,00 em 5 parcelas a 4% a.m.), pedido pelo prompt:
#   amortização 2.000; juros 400, 320, 240, 160, 80; parcelas 2.400, 2.320, 2.240, 2.160, 2.080; juros 1.200; pago 11.200.
#   Saldo no início da parcela k (exemplo NOSSO, k = 4): 10.000 − 3 · 2.000 = 4.000 → juros 160 → parcela 2.160 (bate).
# Nós fazemos (prompt): R$ 12.000,00, 4 parcelas, 5% a.m. → amortização 3.000; 1ª: juros 600 → 3.600;
#   última: saldo 3.000, juros 150 → 3.150; total de juros (600 + 150) · 4 ÷ 2 = 1.500.
# Erros clássicos com os números da seção 06 (para não entregar a Q3):
#   1. abater a parcela inteira: 10.000 − 2.400 = 7.600 (errado) × 10.000 − 2.000 = 8.000 (certo);
#   2. juros sobre o valor inicial todo mês: 400 · 5 = 2.000 (errado) × 1.200 (certo).
# QUESTÃO 2 (texto idêntico na tela, "eu faço"): 60.000 ÷ 10 = 6.000; 1% de 60.000 = 600; parcela 6.600 → D.
#   Erradas (do material): A só os juros; B só a amortização; C juros sobre a amortização (1% de 6.000 = 60 → 6.060);
#   E juros dos 10 meses de uma vez (6.000 + 10 · 600 = 12.000).
#   Conferência de plausibilidade (NOSSA): a 1ª parcela é um pouco mais que 1/10 da dívida.
# QUESTÃO 3 (texto idêntico, "você faz"): juros 600, 540, …, 60 (cai 1% de 6.000 = 60 por mês) →
#   (600 + 60) · 10 ÷ 2 = 3.300 → B. Erradas (do material): A (3.000) média entre 600 e zero, esquecendo os 60 do último
#   mês; C (6.000) juros constantes de 600; D (6.600) é a 1ª parcela; E (63.300) é o total pago.
#   Conferência de plausibilidade (NOSSA): menos que 10 · 600 = 6.000 e mais que a metade disso.
# Atalhos (verde): "4% de 10.000: tire dois zeros e multiplique por 4" · a escadinha (cai i · amortização por mês) ·
#   saldo da parcela k = financiado − (k − 1) · amortização · total de juros = (primeiro + último) · n ÷ 2.
# Frases-chave (meio e fim, idênticas): 1. No SAC, a amortização é fixa e os juros caem junto com o saldo.
#   2. O saldo cai pela amortização, não pela parcela inteira.
#   3. Juros do SAC somam como PA: primeiro mais último, vezes quantidade, dividido por 2.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "SAC do zero: por que a parcela diminui e como somar os juros | Financiamentos Ep. 3"
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
        "{a}Você paga uma parcela de *dois mil e quatrocentos reais* [p=0.3] {b}e a sua dívida cai só *dois mil.* "
        "[p=0.5] {c}Para onde foram os outros *quatrocentos?* [p=0.6] {d}Foram o *aluguel do dinheiro.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *montar a tabela* do SAC, [p=0.3] {b}calcular *qualquer parcela* sem "
        "montar todas [p=0.3] {c}e *somar os juros* do contrato inteiro de uma vez."),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido da série de Porcentagem. [p=0.3] {a}Quatro por cento de dez mil. [p=0.3] "
        "{b}Por cento quer dizer *por cem.* [p=0.4] {c}Atalho: [p=0.2] *tire dois zeros* do valor [p=0.2] e multiplique pela taxa. [p=0.2] Dez mil vira "
        "cem, [p=0.2] vezes quatro: [p=0.2] *quatrocentos.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Agora, um extrato de verdade. [p=0.3] {a}Alguém financiou um apartamento. [p=0.2] Chega o primeiro boleto, "
        "[p=0.2] {b}o segundo, um pouco *mais barato,* [p=0.2] {c}o terceiro, *mais barato ainda.* [p=0.4] {d}E a pessoa "
        "pergunta: [p=0.2] *por que a minha parcela diminui?*"),

    # ================= VOCABULÁRIO =================
    dict(id="05", block="vocab", text=
        "{t}Primeira palavra. [p=0.3] {a}*Saldo devedor* [p=0.2] é quanto você ainda deve [p=0.2] num certo momento. "
        "[p=0.4] {b}Ele começa na dívida inteira [p=0.2] e vai *caindo* até zero."),
    dict(id="06", block="vocab", text=
        "{t}Segunda. [p=0.3] {a}*Juros da parcela* [p=0.2] são o aluguel do dinheiro daquele mês. [p=0.4] {b}E aqui está "
        "o detalhe: [p=0.2] você só paga aluguel do que *ainda deve.* [p=0.2] {c}Por isso, os juros são a taxa vezes o "
        "saldo do *início* do mês."),
    dict(id="07", block="vocab", text=
        "{t}Terceira e quarta. [p=0.3] {a}*Amortização* [p=0.2] é a parte do pagamento que *abate a dívida* de verdade. "
        "[p=0.4] {b}E a *parcela,* [p=0.2] ou prestação, [p=0.2] é o boleto inteiro: [p=0.2] *amortização mais juros.*"),

    # ================= BLOCO A: AS TRÊS RELAÇÕES =================
    dict(id="08", block="relacoes", text=
        "{t}E como elas se ligam? [p=0.3] {a}Por três relações [p=0.2] que valem em *qualquer* financiamento. [p=0.4] {b}Um: [p=0.2] juros é a taxa vezes o saldo anterior. [p=0.3] {c}Dois: [p=0.2] parcela é "
        "amortização mais juros. [p=0.3] {d}Três: [p=0.2] o novo saldo é o saldo anterior *menos a amortização.*"),
    dict(id="09", block="relacoes", text=
        "{t}Repare na terceira. [p=0.3] {a}O saldo cai pela *amortização,* [p=0.2] e não pela parcela inteira. [p=0.4] "
        "{b}Lembra do gancho? [p=0.2] Parcela de dois mil e quatrocentos: [p=0.2] dois mil de amortização [p=0.2] e "
        "quatrocentos de juros. [p=0.4] {c}Os quatrocentos pagaram o aluguel. [p=0.2] *Só os dois mil* derrubaram a "
        "dívida."),

    # ================= BLOCO B: O SAC =================
    dict(id="10", block="sac", text=
        "{t}E como o banco decide quanto amortizar por mês? [p=0.4] {a}O jeito de hoje é o "
        "*SAC:* [p=0.2] *Sistema de Amortização Constante.* [p=0.4] {b}No SAC, [p=0.2] a dívida é *fatiada em fatias "
        "iguais.* [p=0.2] A fatia é a amortização, [p=0.2] e ela é sempre a mesma. [p=0.4] {c}Amortização é o valor "
        "financiado [p=0.2] dividido pelo número de parcelas."),
    dict(id="11", block="sac", text=
        "{t}Exemplo: [p=0.3] {a}dez mil reais em *cinco parcelas,* [p=0.2] a *quatro por cento* ao mês. "
        "[p=0.4] {b}Dez mil dividido por cinco: [p=0.2] fatias de *dois mil.* [p=0.4] {c}Sai uma fatia por mês, [p=0.2] e em cinco meses a dívida acabou."),

    # ================= BLOCO C: A TABELA =================
    dict(id="12", block="tabela", text=
        "{t}Agora a tabela, [p=0.2] linha por linha, [p=0.2] sempre na mesma ordem. [p=0.4] {a}Mês um. [p=0.2] Saldo: "
        "*dez mil.* [p=0.3] {b}Juros: [p=0.2] quatro por cento de dez mil, [p=0.2] *quatrocentos.* [p=0.3] "
        "{c}Amortização: [p=0.2] *dois mil.* [p=0.3] {d}Parcela: [p=0.2] dois mil mais quatrocentos, [p=0.2] *dois mil e "
        "quatrocentos.* [p=0.3] {e}Novo saldo: [p=0.2] dez mil menos dois mil, [p=0.2] *oito mil.*"),
    dict(id="13", block="tabela", text=
        "{t}Mês dois. [p=0.3] {a}Saldo: [p=0.2] *oito mil.* [p=0.2] Juros: [p=0.2] quatro por cento de oito mil, [p=0.2] "
        "*trezentos e vinte.* [p=0.4] {b}A amortização continua dois mil, [p=0.2] e a parcela fica *dois mil trezentos e "
        "vinte.* [p=0.4] {c}O saldo cai para *seis mil.*"),
    dict(id="14", block="tabela", text=
        "{t}E assim por diante. [p=0.3] {a}Mês três: [p=0.2] juros de *duzentos e quarenta.* [p=0.3] {b}Mês quatro: "
        "[p=0.2] *cento e sessenta.* [p=0.3] {c}Mês cinco: [p=0.2] só *oitenta.* [p=0.4] {d}Somando a coluna dos juros: "
        "[p=0.2] *mil e duzentos reais.* [p=0.2] E o total pago: [p=0.2] os dez mil da dívida mais os juros, [p=0.2] "
        "*onze mil e duzentos.*"),
    dict(id="15", block="tabela", text=
        "{t}Agora dá para responder ao extrato. [p=0.3] Por que a parcela diminui? [p=0.4] {a}A fatia é sempre a mesma. "
        "[p=0.3] {b}Mas a dívida *emagrece* a cada mês, [p=0.2] {c}e o juro, o aluguel do que sobrou, [p=0.2] "
        "*emagrece junto.*"),

    # ================= BLOCO D: ATALHOS =================
    dict(id="16", block="escadinha", text=
        "{t}Olhe a coluna dos juros. [p=0.3] Viu um padrão? [p=0.4] {a}Eles descem *sempre o mesmo degrau:* [p=0.2] *oitenta.* [p=0.3] {b}Uma lista assim, [p=0.2] "
        "que sobe ou desce sempre o mesmo valor, [p=0.2] se chama *progressão aritmética,* [p=0.2] ou PA. [p=0.4] "
        "{c}Atalho: [p=0.2] o degrau é a taxa vezes a amortização. [p=0.2] Quatro por cento de dois mil, [p=0.2] "
        "oitenta. [p=0.3] {d}E a parcela desce *o mesmo degrau.*"),
    dict(id="17", block="parcela_k", text=
        "{t}E se a questão pedir *uma* parcela lá no meio, [p=0.2] sem montar a tabela toda? [p=0.4] {a}Atalho: [p=0.2] o saldo no início da parcela *k* [p=0.2] é o valor financiado [p=0.2] menos *k menos "
        "um* fatias. [p=0.4] {b}Parcela quatro: [p=0.2] já saíram *três* fatias. [p=0.2] Dez mil menos seis mil: "
        "[p=0.2] *quatro mil.* [p=0.4] {c}Juros: [p=0.2] cento e sessenta. [p=0.2] Parcela: [p=0.2] *dois mil cento e "
        "sessenta.* [p=0.3] Bate com a tabela."),

    # ================= BLOCO E: SOMA DOS JUROS =================
    dict(id="18", block="soma", text=
        "{t}E para somar todos os juros, [p=0.2] sem somar um por um? [p=0.4] {a}Junte o *primeiro* com o *último:* "
        "[p=0.2] quatrocentos mais oitenta, [p=0.2] quatrocentos e oitenta. [p=0.3] {b}O segundo com o penúltimo: "
        "[p=0.2] trezentos e vinte mais cento e sessenta, [p=0.2] *quatrocentos e oitenta de novo.* [p=0.4] {c}Por "
        "isso a regra: [p=0.2] *primeiro mais último, [p=0.2] vezes quantidade, [p=0.2] dividido por dois.* [p=0.3] "
        "Quatrocentos e oitenta vezes cinco, [p=0.2] dividido por dois: [p=0.2] *mil e duzentos.* [p=0.4] {d}A PA tem "
        "série própria; [p=0.2] aqui, só a fórmula."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*Doze mil reais* em *quatro parcelas* pelo SAC, [p=0.2] a *cinco por cento* ao mês. "
        "[p=0.3] {b}Quanto vale a *primeira* parcela [p=0.2] e quanto vale a *última?* [p=0.4] {c}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}A fatia: [p=0.2] doze mil dividido por quatro, [p=0.2] *três mil.* [p=0.4] "
        "{b}Primeira: [p=0.2] saldo de doze mil, [p=0.2] juros de cinco por cento, [p=0.2] *seiscentos.* [p=0.2] "
        "Parcela: [p=0.2] *três mil e seiscentos.* [p=0.4] {c}Última: [p=0.2] só sobrou uma fatia, [p=0.2] três mil. "
        "[p=0.2] Juros: [p=0.2] *cento e cinquenta.* [p=0.2] Parcela: [p=0.2] *três mil cento e cinquenta.* [p=0.4] "
        "{d}E o total de juros: [p=0.2] seiscentos mais cento e cinquenta, [p=0.2] vezes quatro, [p=0.2] dividido por "
        "dois: [p=0.2] *mil e quinhentos.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] no SAC, a amortização é fixa [p=0.2] e os juros caem "
        "junto com o saldo. [p=0.5] {b}Dois: [p=0.2] o saldo cai pela amortização, [p=0.2] não pela parcela inteira. "
        "[p=0.5] {c}Três: [p=0.2] juros do SAC somam como PA: [p=0.2] primeiro mais último, [p=0.2] vezes quantidade, "
        "[p=0.2] dividido por dois."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *abater a parcela inteira* do saldo. [p=0.2] "
        "Dez mil menos dois mil e quatrocentos, [p=0.2] sete mil e seiscentos. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "você pagou dois mil e quatrocentos. [p=0.4] {c}Mas os "
        "juros só pagam o aluguel. [p=0.2] Abata *só a amortização:* [p=0.2] o saldo é *oito mil.*"),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] calcular os juros sobre o *valor inicial* em todo mês. [p=0.2] Quatrocentos vezes cinco, "
        "[p=0.2] dois mil de juros. [p=0.4] {b}Parece certo, [p=0.2] porque a taxa é a mesma todo mês: [p=0.2] quatro "
        "por cento. [p=0.4] {c}Mas a taxa incide sobre um saldo que *cai.* [p=0.2] Os juros descem a escadinha, "
        "[p=0.2] e o total é *mil e duzentos,* [p=0.2] não dois mil."),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="24", block="q2", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um empresário financiou *sessenta mil reais* em *dez parcelas* mensais pelo SAC, [p=0.2] com "
        "juros de *um por cento* ao mês sobre o saldo devedor. [p=0.2] O valor da *primeira parcela* é: [p=0.4] {qa}A: "
        "[p=0.2] seiscentos reais. [p=0.3] {qb}B: [p=0.2] seis mil. [p=0.3] {qc}C: [p=0.2] seis mil e sessenta. "
        "[p=0.3] {qd}D: [p=0.2] seis mil e seiscentos. [p=0.3] {qe}E: [p=0.2] doze mil reais."),
    dict(id="25", block="q2", text=
        "{t}Monto só a primeira linha da tabela. [p=0.3] {a}A fatia: [p=0.2] sessenta mil dividido por dez, [p=0.2] "
        "*seis mil.* [p=0.4] {b}Os juros do primeiro mês: [p=0.2] um por cento do saldo inteiro, [p=0.2] sessenta mil. "
        "[p=0.2] *Seiscentos.* [p=0.4] {c}Parcela: [p=0.2] seis mil mais seiscentos, [p=0.2] *seis mil e seiscentos.* "
        "[p=0.4] {d}Plausível? [p=0.2] Um pouco mais que um décimo da dívida, [p=0.2] em dez parcelas. [p=0.2] Faz "
        "sentido. [p=0.3] {ok}*Letra D!*"),
    dict(id="26", block="q2", text=
        "{t}E as outras? [p=0.3] {xa}A A [p=0.2] {xb}e a B [p=0.2] são *só metade* da conta: [p=0.2] uma tem só os juros, "
        "[p=0.2] a outra só a amortização. [p=0.4] {xc}A C calculou os juros sobre a *fatia,* [p=0.2] um por cento de "
        "seis mil, [p=0.2] e não sobre o saldo. [p=0.4] {xe}E a E [p=0.2] cobrou na primeira parcela [p=0.2] os juros "
        "dos *dez meses* de uma vez."),

    # ================= QUESTÃO 3 (VOCÊ FAZ) =================
    dict(id="27", block="q3", text=
        "{t}E esta é *sua.* [p=0.3] {a}No mesmo financiamento, [p=0.2] sessenta mil em dez parcelas pelo SAC, [p=0.2] a "
        "um por cento ao mês, [p=0.2] o *total de juros* pagos ao final do contrato é: [p=0.4] {qa}A: [p=0.2] três mil "
        "reais. [p=0.3] {qb}B: [p=0.2] três mil e trezentos. [p=0.3] {qc}C: [p=0.2] seis mil. [p=0.3] {qd}D: [p=0.2] "
        "seis mil e seiscentos. [p=0.3] {qe}E: [p=0.2] sessenta e três mil e trezentos. [p=0.5] {p}*Pause o vídeo e "
        "resolva.* [p=2.0]"),
    dict(id="28", block="q3", text=
        "{t}Conferindo. [p=0.3] {a}O primeiro juro você já tem: [p=0.2] *seiscentos.* [p=0.3] {b}O degrau da "
        "escadinha: [p=0.2] um por cento da fatia de seis mil, [p=0.2] *sessenta.* [p=0.2] Seiscentos, "
        "quinhentos e quarenta, quatrocentos e oitenta... [p=0.4] {c}E o último *não é "
        "zero:* [p=0.2] no décimo mês ainda sobra uma fatia de seis mil, [p=0.2] com juros de *sessenta.* [p=0.4] "
        "{d}Primeiro mais último, [p=0.2] seiscentos e sessenta, [p=0.2] vezes dez, [p=0.2] dividido por dois: "
        "[p=0.2] *três mil e trezentos.* [p=0.3] {ok}*Letra B!*"),
    dict(id="29", block="q3", text=
        "{t}Plausível? [p=0.2] Fica abaixo dos seis mil [p=0.2] de quem cobra seiscentos todo mês. [p=0.3] {xc}E esse "
        "é o erro da C: [p=0.2] juros *constantes,* [p=0.2] como se o saldo não caísse. "
        "[p=0.4] {xa}A A terminou a escadinha em *zero:* [p=0.2] esqueceu os sessenta do último mês. [p=0.4] {xd}A D é a "
        "*primeira parcela,* [p=0.2] confundida com juros. [p=0.3] {xe}E a E é o *total pago:* [p=0.2] a dívida mais "
        "os juros."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] no SAC, a amortização é fixa [p=0.2] e os juros "
        "caem junto com o saldo. [p=0.5] {b}Dois: [p=0.2] o saldo cai pela amortização, [p=0.2] não pela parcela "
        "inteira. [p=0.5] {c}Três: [p=0.2] juros do SAC somam como PA: [p=0.2] primeiro mais último, [p=0.2] vezes "
        "quantidade, [p=0.2] dividido por dois."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}E se o banco quiser que *todas as parcelas sejam iguais?* [p=0.5] {b}Quem paga mais juros no total, [p=0.2] "
        "o *SAC* [p=0.2] ou esse outro sistema? [p=0.5] {c}Próximo episódio: [p=0.2] *Price.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você sabia que os juros não abatem a sua dívida? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
