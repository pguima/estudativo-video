# Roteiro — Empréstimos, Financiamentos e Parcelamentos, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e
#   treino para o ENEM (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/17-emprestimos-financiamentos-parcelamentos.html — seções 01, 10, 11 e 13
#   (e 05, 08, 09 só para "onde aparece"). NÃO usa as Questões 1–9 da seção 12 nem a questão nova do ep1 (3 × 1.331).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS.
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 o GUICHÊ DE CÂMBIO (datas diferentes = moedas de países diferentes) · multiplique para o futuro, divida para o
#   presente · juros = ALUGUEL do que ainda se deve · ep2 a ENTRADA NÃO VIAJA · o "sem juros" com FANTASIA ·
#   ep3 as FATIAS IGUAIS do SAC e a ESCADINHA dos juros · ep4 a CAIXA DE TAMANHO FIXO da Price.
# V/F (os 9 erros da seção 11, com números NOSSOS; 6 falsas e 3 verdadeiras):
#   1 F taxa sobre o preço total (800 à vista ou 300 + 560: 60 ÷ 500 = 12%, não 60 ÷ 800 = 7,5%) ·
#   2 V "sem juros" com desconto tem juros (6 × 100 ou 540 à vista: 60 de juros) ·
#   3 F 550 em 1 mês + 605 em 2 meses a 10% valem 1.155 hoje (são 500 + 500 = 1.000) ·
#   4 V cada parcela é trazida pelo SEU prazo · 5 F pagar a parcela abate a parcela inteira (SAC 6.000 em 6 a 2%:
#   parcela 1.120, saldo 5.000, não 4.880) · 6 F juros do SAC sobre o valor inicial (720 contra 420) ·
#   7 F amortização constante na Price · 8 V mesma taxa e prazo: SAC paga menos juros (ep4: 1.200 × 1.231,35) ·
#   9 F dois meses a 10% no rotativo = × 1,20 (é × 1,21).
# QUESTÕES INÉDITAS (números e distratores do prompt; conferidas em trabalho/conferir_questoes.py):
#   Q1 entrada + parcela: 2.400 à vista ou 1.000 + 1.540 em 30 dias → financiado 1.400, juros 140 → 10% → E.
#      A 0% (anúncio não diz juros) · B ≈ 5,5% (÷ 2.540, total a prazo) · C ≈ 5,8% (÷ 2.400, à vista) ·
#      D ≈ 9,1% (÷ 1.540, a parcela).
#   Q2 SAC 24.000 em 12 a 2%: 5ª parcela → amortização 2.000; saldo no início da 5ª = 24.000 − 4 · 2.000 = 16.000;
#      juros 320 → 2.320 → D. A 320 só os juros · B 2.000 só a amortização · C 2.280 tirou 5 amortizações ·
#      E 2.480 juros sobre o valor inicial.
#   Q3 Price 8.000 em 12 de 733,44 a 1,5%: saldo depois da 1ª → juros 120; amortização 613,44; saldo 7.386,56 → B
#      (alternativas em ordem DECRESCENTE). A 8.120 somou os juros · C 7.333,33 amortização do SAC ·
#      D 7.266,56 abateu a parcela inteira · E 613,44 é a amortização, não o saldo.
#   Q4 cheque especial 1.000 a 8% por 2 meses: 1.000 · 1,08² = 1.166,40 → C. A 1.080 um mês só · B 1.160 juros
#      simples · D 1.259,71 um mês a mais (1,08³) · E 2.166,40 somou de novo o saldo inicial.
#   Q5 5 × "sem juros" = 1.500 ou 1.350 à vista → há 150 de juros e o preço real é 1.350 → A.
#      B acreditou no anúncio · C comparou com a etiqueta · D tomou 1.500 como preço real (e o desconto é 10%, não 15%:
#      NOSSO, o prompt só dá a frase) · E juros "só de quem atrasa".
#   Conferências de plausibilidade (NOSSAS): Q1 a taxa certa é a MAIOR candidata (o financiado é o menor denominador) ·
#   Q2 a parcela do SAC fica entre a 1ª (2.480) e a última (2.040) · Q3 o saldo cai MENOS que a parcela ·
#   Q4 composto passa um pouco do simples.
# Atalho (verde, NOSSO): "linha do tempo em 10 segundos" (o hábito 1 virado em gesto) e "quanto se deve AGORA?".
# Checklist (seção 13) → episódio: valor no tempo, sequência de parcelas, rotativo, quitação: ep1 · valor financiado,
#   entrada + parcela, "sem juros": ep2 · saldo/juros/amortização, tabela do SAC, soma dos juros em PA: ep3 ·
#   Price com o fator, SAC × Price: ep4.
# Meta (material): 20 questões, pelo menos 14 acertos (70%), priorizando entrada + parcela e tabela do SAC.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de empréstimos e financiamentos: 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, episódio 5"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
    "SAC": "Sac",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}Toda compra a prazo é um *empréstimo disfarçado.* [p=0.4] {b}Hoje você aprende a *tirar a fantasia* [p=0.2] "
        "de qualquer anúncio de loja [p=0.2] ou contrato de banco. [p=0.4] {c}Com nove frases [p=0.2] e cinco questões "
        "novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}O que a prova cobra? [p=0.3] Quatro coisas. [p=0.4] {a}A *taxa "
        "escondida* [p=0.2] numa entrada mais uma parcela. [p=0.3] {b}Quanto valem *hoje* parcelas futuras, [p=0.2] ou "
        "quanto custa quitar antes. [p=0.3] {c}Quanto de cada parcela é *juro* [p=0.2] e quanto é *amortização,* "
        "[p=0.2] no SAC e na Price. [p=0.3] {d}E quanto cresce uma dívida de *cartão* ou de *cheque especial.*"),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] uma frase por episódio. [p=0.4] {a}Um: [p=0.2] datas diferentes são *moedas de "
        "países diferentes.* [p=0.2] Só se somam depois do *câmbio.* [p=0.2] Para o futuro, multiplique pelo fator; "
        "[p=0.2] para hoje, divida. [p=0.2] E juro é o *aluguel* do que você ainda deve. [p=0.4] {b}Dois: [p=0.2] a "
        "*entrada não viaja.* [p=0.2] E o sem juros com desconto à vista [p=0.2] é um preço *fantasiado.*"),
    dict(id="04", block="indice", text=
        "{a}Três: [p=0.2] no SAC, a dívida é cortada em *fatias iguais,* [p=0.2] e os juros descem uma *escadinha.* "
        "[p=0.4] {b}E quatro: [p=0.2] na Price, a parcela é uma *caixa de tamanho fixo.* [p=0.2] Dentro dela, [p=0.2] "
        "o juro encolhe [p=0.2] e a amortização cresce."),

    # ================= ONDE APARECE (seções 05, 08 e 09) =================
    dict(id="05", block="onde", text=
        "{t}E onde isso aparece? [p=0.3] {a}Na *casa própria:* [p=0.2] SAC. [p=0.3] {b}No *crediário:* [p=0.2] parcelas "
        "fixas, [p=0.2] Price. [p=0.3] {c}No *cartão* e no cheque especial: [p=0.2] juros compostos, [p=0.2] como em "
        "Taxas equivalentes. [p=0.3] {d}A soma dos juros do SAC [p=0.2] volta em *Progressão aritmética.* [p=0.3] "
        "{e}E à vista ou a prazo, [p=0.2] na próxima série."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 10) =================
    dict(id="06", block="habitos", text=
        "{t}Na prova, três hábitos. [p=0.4] {a}Um: [p=0.2] *desenhe a linha do tempo.* [p=0.2] Em dez segundos, [p=0.2] "
        "você vê o que é entrada [p=0.2] e o que foi financiado. [p=0.4] {b}Dois: [p=0.2] juros só sobre o *saldo devedor.* [p=0.2] Antes de qualquer juro, pergunte: [p=0.2] "
        "*quanto se deve agora?* [p=0.4] {c}Três: [p=0.2] no SAC, monte a *primeira linha;* [p=0.2] na Price, use o "
        "*fator* que o enunciado dá."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="07", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="08", block="vf", text=
        "{t}Um: [p=0.2] oitocentos à vista, [p=0.2] ou trezentos de entrada mais quinhentos e sessenta em trinta dias. "
        "[p=0.2] A taxa é sessenta sobre *oitocentos.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque "
        "oitocentos é o preço do produto. [p=0.3] {g}Mas a entrada não viaja: [p=0.2] divida pelo financiado, "
        "[p=0.2] quinhentos. [p=0.2] *Doze por cento.*"),
    dict(id="09", block="vf", text=
        "{t}Dois: [p=0.2] seis vezes cem, *sem juros,* [p=0.2] ou quinhentos e quarenta à vista. [p=0.2] Tem juros "
        "embutidos. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o cartaz jura que não "
        "tem. [p=0.3] {g}Mas o preço real é o à vista. [p=0.2] A diferença, [p=0.2] *sessenta reais,* são juros."),
    dict(id="10", block="vf", text=
        "{t}Três: [p=0.2] a dez por cento ao mês, [p=0.2] quinhentos e cinquenta daqui a um mês [p=0.2] mais seiscentos "
        "e cinco daqui a dois [p=0.2] valem hoje *mil cento e cinquenta e cinco.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque a soma está certa. [p=0.3] {g}Mas datas diferentes não se somam: [p=0.2] cada uma "
        "passa pelo câmbio. [p=0.2] Quinhentos mais quinhentos: [p=0.2] *mil reais.*"),
    dict(id="11", block="vf", text=
        "{t}Quatro: [p=0.2] para trazer parcelas a hoje, [p=0.2] cada uma é dividida pelo fator do *seu* prazo. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade de usar um prazo só. "
        "[p=0.3] {g}Mas a de um mês divide por um vírgula um; [p=0.2] a de dois, por *um vírgula vinte e um.*"),
    dict(id="12", block="vf", text=
        "{t}Cinco: [p=0.2] você deve seis mil no SAC, [p=0.2] a dois por cento, [p=0.2] e paga uma parcela de mil cento e "
        "vinte. [p=0.2] Agora deve *quatro mil oitocentos e oitenta.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] "
        "{e}Engana porque você pagou mil cento e vinte. [p=0.3] {g}Mas cento e vinte eram juros, [p=0.2] aluguel. "
        "[p=0.2] Só a amortização abate: [p=0.2] deve *cinco mil.*"),
    dict(id="13", block="vf", text=
        "{t}Seis: [p=0.2] nesse SAC de seis parcelas, [p=0.2] os juros são cento e vinte *todo mês.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a taxa é sempre a mesma. [p=0.3] {g}Mas o saldo cai, [p=0.2] e "
        "o juro desce a escadinha: [p=0.2] cento e vinte, cem, oitenta... [p=0.2] O total é *quatrocentos e vinte,* "
        "[p=0.2] não setecentos e vinte."),
    dict(id="14", block="vf", text=
        "{t}Sete: [p=0.2] na Price, [p=0.2] a *amortização* é constante. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] "
        "{e}Engana porque alguma coisa é constante, [p=0.2] e a gente troca. [p=0.3] {g}Na Price, constante é a "
        "*caixa,* a parcela. [p=0.2] Fatias iguais de dívida [p=0.2] são o SAC."),
    dict(id="15", block="vf", text=
        "{t}Oito: [p=0.2] com a mesma taxa e o mesmo prazo, [p=0.2] o SAC paga *menos juros* que a Price. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a taxa é igual. [p=0.3] {g}Mas no SAC o "
        "saldo cai mais depressa, [p=0.2] e o aluguel é cobrado sobre um saldo menor."),
    dict(id="16", block="vf", text=
        "{t}E nove: [p=0.2] no rotativo, [p=0.2] dois meses a dez por cento [p=0.2] multiplicam a dívida por *um "
        "vírgula vinte.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque dez mais dez dá vinte. [p=0.3] "
        "{g}Mas são juros *compostos:* [p=0.2] um vírgula um vezes um vírgula um, [p=0.2] *um vírgula vinte e um.*"),
    dict(id="17", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas, [p=0.2] no estilo do ENEM. [p=0.2] Em todas, [p=0.2] *desenhe a linha do "
        "tempo* antes da conta."),

    # ================= QUESTÃO 1: ENTRADA + UMA PARCELA =================
    dict(id="18", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Um celular custa *dois mil e quatrocentos reais* à vista, [p=0.2] ou *mil reais* de "
        "entrada [p=0.2] mais *mil quinhentos e quarenta* em trinta dias. [p=0.3] {b}A taxa mensal de juros do "
        "parcelamento é [p=0.4] {la}A, [p=0.2] zero por cento. [p=0.2] {lb}B, [p=0.2] cerca de cinco vírgula cinco. "
        "[p=0.2] {lc}C, [p=0.2] cerca de cinco vírgula oito. [p=0.2] {ld}D, [p=0.2] cerca de nove vírgula um. [p=0.2] "
        "{le}E, [p=0.2] dez por cento. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="q1", text=
        "{d}Linha do tempo: [p=0.2] mil hoje, [p=0.2] mil quinhentos e quarenta daqui a um mês. [p=0.3] {a}A entrada não "
        "viaja: [p=0.2] financiado, [p=0.2] dois mil e quatrocentos menos mil, [p=0.2] *mil e quatrocentos.* [p=0.3] "
        "{b}Juros: [p=0.2] *cento e quarenta.* [p=0.2] Cento e quarenta sobre mil e quatrocentos: [p=0.2] *dez por "
        "cento.* [p=0.2] {ok}*Letra E!* [p=0.3] {v}Confere: [p=0.2] a taxa certa é sempre a *maior* candidata. [p=0.4] "
        "{xc}A C dividiu pelo à vista. [p=0.2] {xb}A B, pelo total a prazo. [p=0.2] {xd}A D, pela parcela. [p=0.2] "
        "{xa}E a A acreditou no anúncio."),

    # ================= QUESTÃO 2: PARCELA DO SAC =================
    dict(id="20", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Um empréstimo de *vinte e quatro mil reais* [p=0.2] é pago no SAC, [p=0.2] em "
        "*doze* parcelas, [p=0.2] a *dois por cento* ao mês. [p=0.3] {b}O valor da *quinta* parcela é [p=0.4] {la}A, "
        "[p=0.2] trezentos e vinte. [p=0.2] {lb}B, [p=0.2] dois mil. [p=0.2] {lc}C, [p=0.2] dois mil duzentos e oitenta. "
        "[p=0.2] {ld}D, [p=0.2] dois mil trezentos e vinte. [p=0.2] {le}E, [p=0.2] dois mil quatrocentos e oitenta. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q2", text=
        "{d}Primeira linha do SAC: [p=0.2] a fatia é vinte e quatro mil dividido por doze, [p=0.2] *dois mil.* [p=0.3] "
        "{a}Antes da quinta, [p=0.2] foram pagas *quatro* fatias: [p=0.2] o saldo é vinte e quatro mil menos oito mil, "
        "[p=0.2] *dezesseis mil.* [p=0.3] {b}Juros: [p=0.2] dois por cento disso, [p=0.2] trezentos e vinte. [p=0.2] "
        "Parcela: [p=0.2] *dois mil trezentos e vinte.* [p=0.2] {ok}*Letra D!* [p=0.4] {xc}A C tirou cinco fatias. "
        "[p=0.2] {xe}A E cobrou juros sobre o valor inicial. [p=0.2] {xa}A A ficou só nos juros, [p=0.2] {xb}e a B, só "
        "na fatia."),

    # ================= QUESTÃO 3: SALDO NA PRICE =================
    dict(id="22", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Um financiamento de *oito mil reais* na Price [p=0.2] tem *doze* parcelas de "
        "*setecentos e trinta e três e quarenta e quatro,* [p=0.2] a *um e meio por cento* ao mês. [p=0.3] {b}Depois da "
        "primeira parcela, [p=0.2] o saldo devedor é [p=0.4] {la}A, [p=0.2] oito mil cento e vinte. [p=0.2] {lb}B, "
        "[p=0.2] sete mil trezentos e oitenta e seis e cinquenta e seis. [p=0.2] {lc}C, [p=0.2] sete mil trezentos e "
        "trinta e três e trinta e três. [p=0.2] {ld}D, [p=0.2] sete mil duzentos e sessenta e seis e cinquenta e seis. "
        "[p=0.2] {le}E, [p=0.2] seiscentos e treze e quarenta e quatro. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q3", text=
        "{d}Quanto se deve agora? [p=0.2] Oito mil. [p=0.3] {a}Juros do mês: [p=0.2] um e meio por cento, [p=0.2] *cento "
        "e vinte.* [p=0.3] {b}O resto da caixa é amortização: [p=0.2] seiscentos e treze e quarenta e quatro. [p=0.2] "
        "Saldo: [p=0.2] *sete mil trezentos e oitenta e seis e cinquenta e seis.* [p=0.2] {ok}*Letra B!* [p=0.4] "
        "{xd}A D abateu a parcela inteira. [p=0.2] {xc}A C usou a fatia do SAC. [p=0.2] {xa}A A somou os juros, [p=0.2] "
        "{xe}e a E parou na amortização."),

    # ================= QUESTÃO 4: CHEQUE ESPECIAL =================
    dict(id="24", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Uma conta fica com saldo *negativo* de *mil reais* no cheque especial, [p=0.2] a "
        "*oito por cento* ao mês, [p=0.2] por *dois meses,* sem nenhum pagamento. [p=0.3] {b}A dívida passa a ser "
        "[p=0.4] {la}A, [p=0.2] mil e oitenta. [p=0.2] {lb}B, [p=0.2] mil cento e sessenta. [p=0.2] {lc}C, [p=0.2] mil "
        "cento e sessenta e seis e quarenta. [p=0.2] {ld}D, [p=0.2] mil duzentos e cinquenta e nove e setenta e um. "
        "[p=0.2] {le}E, [p=0.2] dois mil cento e sessenta e seis e quarenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{d}Para o futuro, [p=0.2] multiplique, [p=0.2] uma vez por mês. [p=0.3] {a}Um vírgula zero oito ao quadrado: "
        "[p=0.2] *um vírgula um seis seis quatro.* [p=0.3] {b}Vezes mil: [p=0.2] *mil cento e sessenta e seis e "
        "quarenta.* [p=0.2] {ok}*Letra C!* [p=0.3] {v}Confere: [p=0.2] um pouco acima dos juros simples. [p=0.4] "
        "{xb}A B é juros simples. [p=0.2] {xa}A A contou um mês. [p=0.2] {xd}A D, três. [p=0.2] {xe}E a E somou de novo "
        "os mil."),

    # ================= QUESTÃO 5: O "SEM JUROS" =================
    dict(id="26", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Uma TV custa *cinco vezes de trezentos, sem juros,* [p=0.2] ou *mil trezentos "
        "e cinquenta* à vista. [p=0.3] {b}Qual afirmação é correta? [p=0.4] {la}A, [p=0.2] há cento e cinquenta reais de "
        "juros embutidos, [p=0.2] e o preço real é mil trezentos e cinquenta. [p=0.2] {lb}B, [p=0.2] não há juros, "
        "[p=0.2] pois o anúncio diz sem juros. [p=0.2] {lc}C, [p=0.2] não há juros, [p=0.2] pois o total parcelado é "
        "igual à etiqueta. [p=0.2] {ld}D, [p=0.2] o preço real é mil e quinhentos, [p=0.2] e o desconto é de quinze por "
        "cento. [p=0.2] {le}E, [p=0.2] há juros, [p=0.2] mas só para quem atrasa. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q5", text=
        "{d}Tire a fantasia: [p=0.2] o preço real é o *à vista.* [p=0.3] {a}Mil e quinhentos menos mil trezentos e "
        "cinquenta: [p=0.2] *cento e cinquenta* de juros, [p=0.2] pagos por quem parcela. [p=0.2] {ok}*Letra A!* "
        "[p=0.4] {xb}A B e a C {xc}acreditaram no cartaz. [p=0.2] {xd}A D errou o preço real, [p=0.2] e o desconto é "
        "de dez por cento. [p=0.2] {xe}E a E confundiu juros com multa."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="28", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Levar e trazer valores no tempo, [p=0.2] parcelas "
        "cada uma pelo seu prazo, [p=0.2] quitação e rotativo: [p=0.2] episódio um. [p=0.3] {c}Valor financiado, "
        "[p=0.2] entrada mais parcela [p=0.2] e o sem juros: [p=0.2] episódio dois."),
    dict(id="29", block="checklist", text=
        "{a}Saldo, juros e amortização, [p=0.2] a tabela do SAC [p=0.2] e a soma dos juros: [p=0.2] episódio três. "
        "[p=0.3] {b}A Price com o fator [p=0.2] e a comparação com o SAC: [p=0.2] episódio quatro. [p=0.4] {c}O que você "
        "*não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="30", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte questões* [p=0.2] {b}e acerte pelo menos *catorze,* [p=0.2] setenta por "
        "cento. [p=0.4] {c}Comece pelas de *entrada mais parcela* [p=0.2] e pelas de *tabela do SAC:* [p=0.2] são as "
        "que mais caem."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="31", block="ponte", text=
        "{a}O próximo assunto é *Comparação de propostas e tomada de decisão,* [p=0.3] {b}que fecha a Matemática "
        "Financeira: [p=0.3] {c}à vista ou parcelado, [p=0.2] plano A ou plano B."),
    dict(id="32", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de empréstimos e financiamentos está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
