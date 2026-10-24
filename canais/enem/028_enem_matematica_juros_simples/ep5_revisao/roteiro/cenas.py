# Roteiro — Juros Simples, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/13-juros-simples.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho: frase do usuário, IDÊNTICA (só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 juros = ALUGUEL DO DINHEIRO, sempre sobre o capital inicial (pilha de notas parada, moedinhas iguais) ·
#     a CONTA DE UM MÊS SÓ · juros é o acréscimo, montante é o total ·
#   ep2 TAXA E TEMPO FALAM A MESMA LÍNGUA (fichas com bandeirinhas) · TRADUZA SÓ UM DOS DOIS · a MULTA é o INGRESSO,
#     os JUROS DE MORA são o TAXÍMETRO ·
#   ep3 a ESCADA DE DEGRAUS IGUAIS · a RETA COMEÇA NO CAPITAL · taxa = degrau ÷ capital ·
#   ep4 a MESA DE QUATRO PERNAS (dadas três, a quarta sai) · o MONTANTE JÁ TEM O CAPITAL DENTRO · a ENTRADA NÃO É
#     EMPRÉSTIMO. (O ep4 foi escrito em paralelo: frases tiradas do prompt do vídeo 4 e das frases-chave dele.)
# O que a prova cobra (seção 01): juros/montante com conversão · descobrir taxa, capital ou prazo · multa e mora ·
#   gráfico/tabela (crescimento linear) · taxa embutida numa compra com entrada.
# Onde aparece (seção 10): função afim e PA (séries próprias, só citadas) · Física (s = s₀ + v·t: o capital no papel da
#   posição inicial) · porcentagem e regra de três · Ciências Humanas (endividamento, crédito, juros de mora).
# Estratégia (seção 09): sublinhar as unidades · juros ou montante? · o valor de um período · a ordem de grandeza.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras):
#   1 F (18% a.a. por 8 meses = C · 0,18 · 8; é 0,015 · 8) ·
#   2 F (2% a.m. por 2 anos: 24% a.a. com 24 meses; converta só um: R$ 1.000,00 → certo 480; 24% com 24 = 5.760, 12 vezes
#     MAIS; 2% com 2 = 40, 12 vezes MENOS — "12 vezes errado, para mais ou para menos, conforme o sentido", como o prompt
#     pede; o material diz "12 vezes menor" nos dois casos) ·
#   3 V (pegou 1.000, devolveu 1.120: juros = 120) · 4 F (1,5% entra como 0,15; é 0,015) ·
#   5 F (taxa = juros ÷ montante ÷ tempo; é ÷ capital) · 6 V (triplicar: juros = 2 vezes o capital) ·
#   7 F (1 ano e 3 meses = 1,3 ano; são 15 meses ou 1,25 ano) · 8 V (conta atrasada: multa E juros de mora) ·
#   9 F (2% a.m. = 2 ÷ 12 ao ano; multiplique: 24% a.a.).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico):
#   Q1 (cofrinho/aplicação) R$ 6.000,00 a 15% a.a. por 10 meses, pede os JUROS → 15 ÷ 12 = 1,25% a.m. → 75 por mês →
#      × 10 = R$ 750,00 → E. A 75 (um mês só) · B 6.750 (montante) · C 900 (um ano inteiro) · D 9.000 (taxa anual com o
#      tempo em meses). Ordem de grandeza: 10 meses são quase um ano, e um ano renderia 900.
#   Q2 (prazo em dias, ano comercial) R$ 3.600,00 a 30% a.a. por 40 dias → 3.600 · 0,30 = 1.080 por ano ÷ 360 = R$ 3,00 por
#      dia → × 40 = R$ 120,00 → B. A 43.200 (40 dias como se fossem anos) · C 3.720 (montante) · D 3.600 (40 dias como se
#      fossem meses, a 2,5% a.m.) · E 118,36 (ano de 365 dias; o enunciado manda o comercial).
#   Q3 (conta de água atrasada) R$ 180,00, multa 2%, juros de mora 1% a.m. proporcionais, 20 dias → multa 3,60; mora
#      180 · 0,01 = 1,80 por mês · 20/30 = 1,20 → R$ 184,80 → D. A 181,20 (esqueceu a multa) · B 183,60 (esqueceu os
#      juros de mora) · C 185,40 (cobrou o mês inteiro de juros) · E 219,60 (tratou 1% como taxa por dia).
#   Q4 (tabela de montantes) mês 0 a 3: 2.500, 2.575, 2.650, 2.725 → degrau 75 → 75 ÷ 2.500 = 3% a.m. → A.
#      B 0,3% (vírgula) · C ≈ 2,75% (dividiu pelo montante final, 2.725) · D 9% (225 ÷ 2.500: não dividiu pelos 3 meses) ·
#      E 75% (leu o degrau de R$ 75,00 como taxa).
#   Q5 (triplicar) a 5% a.m. → i · t = 3 − 1 = 2 → t = 40 meses = 3 anos e 4 meses → C. A 5 anos (J = 3C, 60 meses) ·
#      B 1 ano e 8 meses (dobrar: 20 meses) · D 3 anos e 3 meses (leu 3,33 ano como 3 anos e 3 meses) · E 40 anos (achou
#      40 e não olhou a unidade da taxa).
# Gabaritos: E, B, D, A, C.
# Checklist (seção 13, 13 itens) → episódio: C, i, t, J, M; J = C·i·t e M = C(1 + it) com decimal: ep1 · mesma unidade,
#   taxas proporcionais (só em simples), ano comercial, "1 ano e 3 meses", multa e mora: ep2 · função afim no gráfico,
#   PA de razão C·i: ep3 · isolar dividindo pelo capital, dobrar e triplicar, taxa embutida com entrada: ep4 ·
#   o que muda nos compostos: próxima série.
# Meta (material): 20 questões, pelo menos 14 acertos (70%), com conversão, boleto atrasado ou gráfico.
# Ponte (do usuário): Juros compostos e montante.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de juros simples: 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, episódio 5"

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
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}Boleto atrasado, [p=0.2] compra parcelada, [p=0.2] empréstimo entre parentes. [p=0.4] {b}O ENEM *nunca* "
        "pergunta: [p=0.2] calcule os juros simples. [p=0.3] {c}Ele conta uma *história,* [p=0.2] e a conversão de unidade "
        "está *escondida no meio.* [p=0.4] {d}Hoje: [p=0.2] nove frases de verdadeiro ou falso [p=0.2] e cinco questões "
        "novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E que histórias são essas? [p=0.4] {a}Juros ou montante, [p=0.2] com uma *conversão* de unidade no meio. "
        "[p=0.3] {b}Descobrir a *taxa,* [p=0.2] o *capital* [p=0.2] ou o *prazo.* [p=0.3] {c}*Multa* e *juros de mora* "
        "numa conta atrasada. [p=0.3] {d}Um *gráfico* ou uma *tabela* de montante. [p=0.3] {e}E a *taxa escondida* numa "
        "compra com entrada."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] vamos relembrar cada episódio. [p=0.4] {a}Um: [p=0.2] juros são o *aluguel do "
        "dinheiro,* [p=0.2] sempre sobre o capital inicial. [p=0.2] Faça a conta de *um mês só* [p=0.2] e multiplique "
        "pelo tempo. [p=0.3] Juros é o acréscimo; [p=0.2] montante é o total. [p=0.4] {b}Dois: [p=0.2] taxa e tempo "
        "*falam a mesma língua.* [p=0.2] Traduza *só um dos dois.* [p=0.3] E na conta atrasada, [p=0.2] a multa é o "
        "*ingresso,* [p=0.2] e os juros de mora são o *taxímetro.*"),
    dict(id="04", block="indice", text=
        "{a}Três: [p=0.2] o montante sobe uma *escada de degraus iguais.* [p=0.2] A reta *começa no capital,* [p=0.2] e a "
        "taxa é o degrau dividido pelo capital. [p=0.4] {b}Quatro: [p=0.2] a fórmula é uma *mesa de quatro pernas:* "
        "[p=0.2] dadas três, [p=0.2] a quarta sai. [p=0.3] O montante *já tem o capital dentro.* [p=0.2] E a entrada "
        "*não é empréstimo.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="05", block="onde", text=
        "{t}E onde mais isso aparece? [p=0.4] {a}O montante é uma *função afim,* [p=0.2] e os montantes formam uma *PA.* "
        "[p=0.2] As duas têm série própria. [p=0.3] {b}Na *Física,* [p=0.2] é o movimento uniforme: [p=0.2] o capital "
        "faz o papel da posição inicial, [p=0.2] e o gráfico também é uma reta. [p=0.3] {c}É *porcentagem* e *regra de "
        "três.* [p=0.3] {d}E nas *Ciências Humanas,* [p=0.2] em textos sobre endividamento, [p=0.2] crédito [p=0.2] e "
        "juros de mora."),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 09) =================
    dict(id="06", block="habitos", text=
        "{t}Na prova, [p=0.2] quatro hábitos. [p=0.4] {a}Um: [p=0.2] *sublinhe as unidades* [p=0.2] da taxa e do prazo, "
        "[p=0.2] antes de tudo. [p=0.3] {b}Dois: [p=0.2] pergunte: [p=0.2] *juros ou montante?* [p=0.3] {c}Três: [p=0.2] "
        "calcule o valor de *um período* [p=0.2] e multiplique. [p=0.3] {d}Quatro: [p=0.2] confira a *ordem de "
        "grandeza.* [p=0.2] Juros de poucos meses [p=0.2] são poucos por cento do capital."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="07", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="08", block="vf", text=
        "{t}Um: [p=0.2] a dezoito por cento *ao ano,* [p=0.2] por oito *meses,* [p=0.2] os juros são o capital vezes "
        "zero vírgula dezoito vezes oito. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque todos os números "
        "estão no enunciado. [p=0.3] {g}Mas taxa anual não conversa com meses. [p=0.2] Dezoito ao ano [p=0.2] é *um "
        "vírgula cinco ao mês.*"),
    dict(id="09", block="vf", text=
        "{t}Dois: [p=0.2] a dois por cento ao mês, [p=0.2] por dois anos, [p=0.2] eu passo a taxa para vinte e quatro "
        "ao ano [p=0.2] *e* o tempo para vinte e quatro meses. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque parece capricho: [p=0.2] converteu tudo. [p=0.3] {g}Mas a conversão é *uma só.* [p=0.2] Traduza os dois, "
        "[p=0.2] e o resultado sai *doze vezes errado,* [p=0.2] para mais ou para menos, [p=0.2] conforme o sentido."),
    dict(id="10", block="vf", text=
        "{t}Três: [p=0.2] quem pegou mil reais emprestados [p=0.2] e devolveu mil cento e vinte [p=0.2] pagou *cento e "
        "vinte* de juros. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o número que "
        "aparece é o mil cento e vinte. [p=0.3] {g}Mas juros é só o *acréscimo.* [p=0.2] O total é o montante, [p=0.2] e "
        "os dois estão nas alternativas."),
    dict(id="11", block="vf", text=
        "{t}Quatro: [p=0.2] uma taxa de um vírgula cinco por cento [p=0.2] entra na fórmula como *zero vírgula quinze.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque os algarismos são os mesmos. [p=0.3] {g}Mas zero "
        "vírgula quinze é quinze por cento. [p=0.2] Ande *duas casas:* [p=0.2] *zero vírgula zero quinze.*"),
    dict(id="12", block="vf", text=
        "{t}Cinco: [p=0.2] para achar a taxa, [p=0.2] divida os juros pelo *montante* [p=0.2] e pelo tempo. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o montante é o número maior e mais visível. [p=0.3] "
        "{g}Mas o aluguel é cobrado sobre o *capital.* [p=0.2] Juros [p=0.2] dividido por capital vezes tempo."),
    dict(id="13", block="vf", text=
        "{t}Seis: [p=0.2] para *triplicar* um capital, [p=0.2] os juros precisam ser *duas vezes* o capital. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque triplicar lembra o número três. [p=0.3] "
        "{g}Mas o montante *já tem o capital dentro.* [p=0.2] Um capital seu, [p=0.2] mais dois de juros."),
    dict(id="14", block="vf", text=
        "{t}Sete: [p=0.2] um ano e três meses [p=0.2] é *um vírgula três* ano. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque é assim que se escreve no papel. [p=0.3] {g}Mas mês não é décimo de ano. [p=0.2] São "
        "*quinze meses,* [p=0.2] ou *um vírgula vinte e cinco* ano."),
    dict(id="15", block="vf", text=
        "{t}Oito: [p=0.2] numa conta paga com atraso, [p=0.2] você paga a *multa* [p=0.2] *e também* os juros de mora. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque parece cobrar duas vezes. [p=0.3] "
        "{g}Mas a multa é o *ingresso,* [p=0.2] cobrado uma vez. [p=0.2] E os juros são o *taxímetro,* [p=0.2] que corre "
        "a cada dia."),
    dict(id="16", block="vf", text=
        "{t}E nove: [p=0.2] dois por cento ao mês [p=0.2] é o mesmo que dois *dividido por doze* ao ano. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o ano tem doze meses, [p=0.2] e dividir parece natural. "
        "[p=0.3] {g}Mas em um ano cabem doze aluguéis: [p=0.2] *multiplique.* [p=0.2] Vinte e quatro por cento ao ano. "
        "[p=0.2] Período maior, [p=0.2] taxa maior."),
    dict(id="17", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas. [p=0.2] Em todas, [p=0.2] escreva a unidade da *taxa* [p=0.2] e a do "
        "*tempo.*"),

    # ================= QUESTÃO 1: APLICAÇÃO (taxa anual, prazo em meses) =================
    dict(id="18", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma pessoa aplicou *seis mil reais* [p=0.2] a juros simples de *quinze por cento ao "
        "ano,* [p=0.2] por *dez meses.* [p=0.3] {b}Os juros recebidos foram de [p=0.4] {la}A, [p=0.2] setenta e cinco "
        "reais. [p=0.2] {lb}B, [p=0.2] seis mil, setecentos e cinquenta. [p=0.2] {lc}C, [p=0.2] novecentos. [p=0.2] "
        "{ld}D, [p=0.2] nove mil. [p=0.2] {le}E, [p=0.2] setecentos e cinquenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="q1", text=
        "{d}Taxa ao *ano,* [p=0.2] tempo em *meses.* [p=0.2] Traduza a taxa. [p=0.3] {a}Quinze dividido por doze: "
        "[p=0.2] *um vírgula vinte e cinco por cento ao mês.* [p=0.2] Um mês rende *setenta e cinco reais.* [p=0.3] "
        "{b}Dez meses: [p=0.2] *setecentos e cinquenta.* [p=0.2] {ok}*Letra E!* [p=0.3] {v}Confere: [p=0.2] um ano "
        "inteiro renderia novecentos. [p=0.2] Dez meses, um pouco menos. [p=0.4] {xa}A A parou em um mês. [p=0.2] {xc}A "
        "C pegou o ano inteiro. [p=0.2] {xd}A D usou a taxa anual com os meses, [p=0.2] {xb}e a B é o montante."),

    # ================= QUESTÃO 2: PRAZO EM DIAS (ano comercial) =================
    dict(id="20", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Um empréstimo de *três mil e seiscentos reais,* [p=0.2] a *trinta por cento ao "
        "ano,* [p=0.2] foi pago em *quarenta dias.* [p=0.2] Use o ano comercial. [p=0.3] {b}Os juros foram de [p=0.4] "
        "{la}A, [p=0.2] quarenta e três mil e duzentos. [p=0.2] {lb}B, [p=0.2] cento e vinte. [p=0.2] {lc}C, [p=0.2] "
        "três mil, setecentos e vinte. [p=0.2] {ld}D, [p=0.2] três mil e seiscentos. [p=0.2] {le}E, [p=0.2] cento e "
        "dezoito e trinta e seis centavos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q2", text=
        "{d}Ano comercial: [p=0.2] *trezentos e sessenta dias.* [p=0.3] {a}Em um ano, [p=0.2] os juros seriam mil e "
        "oitenta. [p=0.2] Dividido por trezentos e sessenta: [p=0.2] *três reais por dia.* [p=0.3] {b}Quarenta dias: "
        "[p=0.2] *cento e vinte reais.* [p=0.2] {ok}*Letra B!* [p=0.4] {xe}A E usou o ano de trezentos e sessenta e "
        "cinco. [p=0.2] {xd}A D tratou os dias como meses, [p=0.2] {xa}e a A, como anos. [p=0.2] {xc}E a C é o "
        "montante."),

    # ================= QUESTÃO 3: CONTA DE ÁGUA ATRASADA =================
    dict(id="22", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Uma conta de água de *cento e oitenta reais* [p=0.2] foi paga com *vinte dias* de "
        "atraso. [p=0.2] A multa é de *dois por cento,* [p=0.2] e os juros de mora, [p=0.2] de *um por cento ao mês,* "
        "[p=0.2] proporcionais aos dias. [p=0.3] {b}O valor pago foi [p=0.4] {la}A, [p=0.2] cento e oitenta e um e "
        "vinte. [p=0.2] {lb}B, [p=0.2] cento e oitenta e três e sessenta. [p=0.2] {lc}C, [p=0.2] cento e oitenta e cinco "
        "e quarenta. [p=0.2] {ld}D, [p=0.2] cento e oitenta e quatro e oitenta. [p=0.2] {le}E, [p=0.2] duzentos e "
        "dezenove e sessenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q3", text=
        "{d}O ingresso e o taxímetro. [p=0.3] {a}A multa: [p=0.2] dois por cento de cento e oitenta, [p=0.2] *três e "
        "sessenta.* [p=0.3] {b}Os juros: [p=0.2] um mês seria um e oitenta. [p=0.2] Vinte dias são dois terços do mês: "
        "[p=0.2] *um e vinte.* [p=0.3] {c}Total: [p=0.2] *cento e oitenta e quatro e oitenta.* [p=0.2] {ok}*Letra D!* "
        "[p=0.4] {xa}A A esqueceu a multa, [p=0.2] {xb}e a B, os juros. [p=0.2] {xc}A C cobrou o mês inteiro, [p=0.2] "
        "{xe}e a E tratou o um por cento como taxa *por dia.*"),

    # ================= QUESTÃO 4: TABELA DE MONTANTES =================
    dict(id="24", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Uma tabela mostra o montante de uma aplicação, [p=0.2] mês a mês: [p=0.2] dois mil "
        "e quinhentos, [p=0.2] dois mil quinhentos e setenta e cinco, [p=0.2] dois mil seiscentos e cinquenta, [p=0.2] "
        "dois mil setecentos e vinte e cinco. [p=0.3] {b}A taxa mensal é de [p=0.4] {la}A, [p=0.2] três por cento. "
        "[p=0.2] {lb}B, [p=0.2] zero vírgula três. [p=0.2] {lc}C, [p=0.2] cerca de dois vírgula setenta e cinco. [p=0.2] "
        "{ld}D, [p=0.2] nove. [p=0.2] {le}E, [p=0.2] setenta e cinco. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{d}Degraus iguais: [p=0.2] é juros simples. [p=0.3] {a}Cada degrau: [p=0.2] *setenta e cinco reais.* [p=0.2] "
        "{b}A reta começa no capital, [p=0.2] dois mil e quinhentos. [p=0.2] Setenta e cinco sobre dois mil e quinhentos: "
        "[p=0.2] *três por cento ao mês.* [p=0.2] {ok}*Letra A!* [p=0.4] {xc}A C dividiu pelo montante final. [p=0.2] "
        "{xd}A D esqueceu de dividir pelos três meses. [p=0.2] {xe}A E leu o degrau como taxa, [p=0.2] {xb}e a B errou "
        "a vírgula."),

    # ================= QUESTÃO 5: TRIPLICAR =================
    dict(id="26", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}A juros simples de *cinco por cento ao mês,* [p=0.2] em quanto tempo um "
        "capital *triplica?* [p=0.4] {la}A, [p=0.2] cinco anos. [p=0.2] {lb}B, [p=0.2] um ano e oito meses. [p=0.2] "
        "{lc}C, [p=0.2] três anos e quatro meses. [p=0.2] {ld}D, [p=0.2] três anos e três meses. [p=0.2] {le}E, [p=0.2] "
        "quarenta anos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q5", text=
        "{d}O montante já tem o capital dentro: [p=0.2] os juros são *duas vezes* o capital. [p=0.3] {a}Então, [p=0.2] "
        "taxa vezes tempo [p=0.2] é igual a dois. [p=0.2] Dois dividido por zero vírgula zero cinco: [p=0.2] *quarenta "
        "meses.* [p=0.3] {b}Quarenta meses [p=0.2] são *três anos e quatro meses.* [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A "
        "usou juros iguais a três capitais. [p=0.2] {xb}A B só dobrou. [p=0.2] {xd}A D leu três vírgula trinta e três "
        "como três anos e três meses. [p=0.2] {xe}E a E esqueceu que a taxa é *ao mês.*"),

    # ================= CHECKLIST (seção 13) =================
    dict(id="28", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Vocabulário e fórmula: [p=0.2] episódio um. [p=0.3] "
        "{c}Unidades, [p=0.2] dias [p=0.2] e boleto: [p=0.2] episódio dois."),
    dict(id="29", block="checklist", text=
        "{a}Gráfico e PA: [p=0.2] episódio três. [p=0.3] {b}Isolar as letras, [p=0.2] dobrar [p=0.2] e a compra a prazo: "
        "[p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="30", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte questões* de juros simples [p=0.2] {b}e acerte pelo menos *catorze,* "
        "[p=0.2] setenta por cento. [p=0.4] {c}De preferência, [p=0.2] com conversão de unidade, [p=0.2] boleto atrasado "
        "[p=0.2] ou gráfico."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}O próximo assunto é *Juros compostos e montante:* [p=0.3] {b}juros sobre juros, [p=0.2] {c}a curva no lugar "
        "da reta [p=0.2] {d}e a PG no lugar da PA."),
    dict(id="32", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de juros simples está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
