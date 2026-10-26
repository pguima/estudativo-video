# Roteiro — Juros Compostos e Montante, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/14-juros-compostos-montante.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 a BOLA DE NEVE · PENSE EM FATORES, não em porcentagens somadas · o EXPOENTE CONTA as multiplicações ·
#   ep2 a escada de DEGRAUS IGUAIS (reta) × a de DEGRAUS CRESCENTES (curva) · o CRUZAMENTO em t = 1 ·
#     DOBRAR, DOBRAR, DOBRAR (× 8) ·
#   ep3 multiplicar por 1,1 = SOMAR A DÉCIMA PARTE · DOBRAR O TEMPO é ELEVAR AO QUADRADO · a regra do 72 é o RADAR ·
#   ep4 o FILME AO CONTRÁRIO (para hoje, divida pelo mesmo fator).
#   (O ep3 foi escrito em paralelo: as frases dele vêm do prompt do vídeo 3 e do cabeçalho do cenas.py dele.)
# O que a prova cobra (seção 01): montante com a potência dada · tempo por tentativa ou com logaritmos · trazer um valor
#   futuro para hoje · comparar simples e compostos (números ou gráfico) · encadear taxas multiplicando fatores.
# Onde aparece (seção 10): Biologia (populações, bactérias) · Química (meia-vida, fator 1/2) · Geografia (população, PIB) ·
#   Álgebra e Funções (PG, exponencial e logaritmo: séries próprias) · inflação (série de Taxas equivalentes e inflação).
# Estratégia (seção 09): procure as potências · elimine pelo simples · estime com a regra do 72 · fatores até o fim.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras):
#   1 F (10% por 2 anos = 20%; é 1,1² = 1,21 → 21%) · 2 F (composto: M = C(1 + i·t); é C(1 + i)ᵗ) ·
#   3 V (aplicou 1.000, montante 1.210: juros 210) · 4 F (6 meses → 1,34; 12 meses → 2,68; é 1,34² ≈ 1,80) ·
#   5 F (12% ao ano em compostos = 1% ao mês; a conversão usa potência, série própria — sem calcular a taxa) ·
#   6 V (R$ 1.210,00 daqui a 2 anos a 10% valem R$ 1.000,00 hoje: 1.210 ÷ 1,21) ·
#   7 F (tabela do ano 0 ao ano 3: expoente 4; é 3) · 8 V (dobrar a 10%: log 2 ÷ log 1,1) ·
#   9 F (compostos sempre rendem mais que simples à mesma taxa; só depois do 1º período).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico):
#   Q1 (cofrinho) R$ 6.000,00 a 5% a.m. por 2 meses, pede os JUROS → 1,05² = 1,1025 → M = 6.615 → J = R$ 615,00 → D.
#      A 300 (juros de um mês só) · B 6.615 (montante) · C 600 (juros simples: somou as taxas) · E 6.600 (montante simples).
#   Q2 (cartão de crédito) R$ 2.500,00 a 8% a.m., 12 meses, dado 1,08⁶ ≈ 1,59 → 1,59² = 2,5281 → R$ 6.320,25 → A.
#      B 3.975 (só 6 meses) · C 4.900 (juros simples: 96%) · D 5.450 (somou os semestres: 59% + 59%) ·
#      E 7.950 (dobrou o fator: 2 · 1,59). (Com a potência exata, 1,08¹² ≈ 2,518 → ≈ R$ 6.295: o enunciado manda usar 1,59.)
#   Q3 (relógio) triplicar a 12% a.a., log 3 ≈ 0,48, log 2 ≈ 0,30, log 1,12 ≈ 0,05 → 0,48 ÷ 0,05 = 9,6 anos → E.
#      A 4 (dividiu log 3 pela taxa, 0,12) · B 6 (usou log 2: é o tempo de DOBRAR) · C ≈ 16,7 (triplicar em simples:
#      0,12·t = 2) · D 25 (simples com J = 3C). Radar: 72 ÷ 12 = 6 anos para dobrar → triplicar fica entre 6 e 12 (quadruplicar).
#   Q4 (alvo/linha do tempo) R$ 9.680,00 daqui a 2 anos, 10% a.a. → 9.680 ÷ 1,21 = R$ 8.000,00 → C.
#      A 7.840,80 (tirou 10% duas vezes) · B ≈ 8.066,67 (fator de juros simples, 1,20) · D 8.800 (só um ano) ·
#      E 11.712,80 (multiplicou: foi para o futuro).
#   Q5 (gráfico reta × curva) R$ 20.000,00 por 2 anos: I simples 16% a.a. (1,32 → 26.400) × II compostos 15% a.a.
#      (1,3225 → 26.450) → II, R$ 50,00 a mais → B. A I, 400 (calculou a II como simples) · C I, 462 (calculou a I como
#      composta) · D II, 4.017,50 (um período a mais na II) · E II, 19.600 (dobrou o fator: 2 · 1,15). A conta foi feita:
#      a regra geral não decide, porque as taxas são diferentes.
# Gabaritos: D, A, E, C, B.
# Checklist (seção 13, 13 itens) → episódio: juros sobre juros, M = C(1 + i)ᵗ e J = M − C, taxas em sequência: ep1 ·
#   simples × compostos, PG e exponencial: ep2 · potências à mão, combinar potências, dobrar o tempo, tentativa, logaritmos,
#   regra do 72: ep3 · valor presente: ep4 · o último item (fatores em Descontos) é a ponte.
# Meta (material): 20 questões, pelo menos 14 acertos (70%), com logaritmos fornecidos e comparação entre regimes.
# Ponte (do usuário): Descontos, acréscimos, lucro e prejuízo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de juros compostos: 9 pegadinhas e 5 questões estilo ENEM | Juros Compostos Ep. 5"
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
        "{a}Poupança, [p=0.2] cartão de crédito, [p=0.2] cheque especial, [p=0.2] financiamento. [p=0.3] Tudo funciona em "
        "*juros compostos.* [p=0.4] {b}E o ENEM sabe que você está *sem calculadora:* [p=0.2] {c}por isso ele *entrega* "
        "as potências e os logaritmos. [p=0.3] Hoje você aprende a *usá-los.* [p=0.4] {d}Nove frases de verdadeiro ou "
        "falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova cobra? [p=0.4] {a}O *montante,* [p=0.2] com a potência dada. [p=0.3] {b}O *tempo,* [p=0.2] "
        "por tentativa [p=0.2] ou com logaritmos. [p=0.3] {c}Trazer um valor do futuro *para hoje.* [p=0.3] {d}Comparar "
        "*simples e compostos,* [p=0.2] em números [p=0.2] ou num gráfico. [p=0.3] {e}E encadear taxas diferentes, "
        "[p=0.2] *multiplicando os fatores.*"),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] vamos relembrar cada episódio. [p=0.4] {a}Um: [p=0.2] juros compostos são uma *bola "
        "de neve:* [p=0.2] juros sobre juros. [p=0.3] Pense em *fatores,* [p=0.2] não em porcentagens somadas. [p=0.2] E o "
        "*expoente conta* as multiplicações. [p=0.4] {b}Dois: [p=0.2] o simples é uma escada de *degraus iguais;* "
        "[p=0.2] o composto, de *degraus crescentes.* [p=0.3] As duas se *cruzam* em um período. [p=0.2] E dobrar, "
        "dobrar, dobrar [p=0.2] é *vezes oito.*"),
    dict(id="04", block="indice", text=
        "{a}Três: [p=0.2] multiplicar por um vírgula um [p=0.2] é *somar a décima parte.* [p=0.3] *Dobrar o tempo* "
        "[p=0.2] é *elevar o fator ao quadrado.* [p=0.3] E a regra do setenta e dois [p=0.2] é o seu *radar.* [p=0.4] "
        "{b}Quatro: [p=0.2] trazer para hoje [p=0.2] é passar o *filme ao contrário:* [p=0.2] divida pelo mesmo fator."),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="05", block="onde", text=
        "{t}E onde mais isso aparece? [p=0.4] {a}Na *Biologia,* [p=0.2] populações e colônias de bactérias [p=0.2] "
        "crescem a uma taxa fixa. [p=0.3] {b}Na *Química,* [p=0.2] a meia-vida [p=0.2] multiplica a massa por *um "
        "meio* [p=0.2] a cada período. [p=0.3] {c}Na *Geografia,* [p=0.2] projeções de população e de PIB. [p=0.3] "
        "{d}PG, [p=0.2] função exponencial [p=0.2] e logaritmo [p=0.2] têm *séries próprias.* [p=0.3] {e}E a "
        "*inflação* [p=0.2] volta na série de Taxas equivalentes."),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 09) =================
    dict(id="06", block="habitos", text=
        "{t}Na prova, [p=0.2] quatro hábitos. [p=0.4] {a}Um: [p=0.2] *procure as potências* no enunciado. [p=0.2] Elas "
        "mostram o caminho. [p=0.3] {b}Dois: [p=0.2] *elimine pelo simples.* [p=0.2] Depois de um período, [p=0.2] o "
        "composto é maior. [p=0.3] {c}Três: [p=0.2] *estime* com a regra do setenta e dois. [p=0.3] {d}Quatro: [p=0.2] "
        "trabalhe com *fatores até o fim,* [p=0.2] e só no final converta em reais."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="07", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="08", block="vf", text=
        "{t}Um: [p=0.2] dez por cento ao ano, [p=0.2] por dois anos, [p=0.2] em juros compostos, [p=0.2] rende *vinte "
        "por cento.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque dez mais dez dá vinte. [p=0.3] "
        "{g}Mas fatores se *multiplicam:* [p=0.2] um vírgula um ao quadrado [p=0.2] é *um vírgula vinte e um.* [p=0.2] "
        "Vinte e um por cento."),
    dict(id="09", block="vf", text=
        "{t}Dois: [p=0.2] em juros compostos, [p=0.2] o montante é o capital vezes *um mais i vezes t.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque é a fórmula que você usou na série anterior. [p=0.3] "
        "{g}Essa é a dos *simples.* [p=0.2] Nos compostos, [p=0.2] *um mais i, elevado a t.* [p=0.2] E a alternativa de "
        "juros simples [p=0.2] está sempre lá, esperando."),
    dict(id="10", block="vf", text=
        "{t}Três: [p=0.2] quem aplicou mil reais [p=0.2] e terminou com mil duzentos e dez [p=0.2] recebeu *duzentos e "
        "dez* de juros. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o número que a fórmula "
        "entrega é o mil duzentos e dez. [p=0.3] {g}Mas a fórmula dá o *montante.* [p=0.2] Os juros saem por diferença: "
        "[p=0.2] montante *menos* capital."),
    dict(id="11", block="vf", text=
        "{t}Quatro: [p=0.2] se seis meses multiplicam por um vírgula trinta e quatro, [p=0.2] doze meses multiplicam por "
        "*dois vírgula sessenta e oito.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o tempo dobrou, "
        "[p=0.2] e dobrar o fator parece justo. [p=0.3] {g}Mas dobrar o tempo é *elevar ao quadrado:* [p=0.2] um vírgula "
        "trinta e quatro ao quadrado, [p=0.2] cerca de *um vírgula oitenta.*"),
    dict(id="12", block="vf", text=
        "{t}Cinco: [p=0.2] em juros compostos, [p=0.2] doze por cento ao ano [p=0.2] é o mesmo que *um por cento ao "
        "mês.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque nos juros simples era assim mesmo. "
        "[p=0.3] {g}Mas aqui, [p=0.2] um por cento ao mês, [p=0.2] doze vezes, [p=0.2] é *bola de neve:* [p=0.2] passa de "
        "doze. [p=0.2] Essa conversão usa *potência,* [p=0.2] e tem série própria."),
    dict(id="13", block="vf", text=
        "{t}Seis: [p=0.2] mil duzentos e dez reais, [p=0.2] daqui a dois anos, [p=0.2] a dez por cento ao ano, [p=0.2] "
        "valem *mil reais hoje.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente "
        "tiraria dez por cento duas vezes, [p=0.2] e acharia outro número. [p=0.3] {g}Mas é o *filme ao contrário:* "
        "[p=0.2] mil duzentos e dez [p=0.2] *dividido* por um vírgula vinte e um."),
    dict(id="14", block="vf", text=
        "{t}Sete: [p=0.2] uma tabela vai do *ano zero* ao *ano três.* [p=0.2] Então o expoente é *quatro.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a tabela tem quatro linhas. [p=0.3] {g}Mas o expoente "
        "conta as *multiplicações,* [p=0.2] e não as linhas. [p=0.2] Do ano zero ao ano três, [p=0.2] *três* "
        "capitalizações."),
    dict(id="15", block="vf", text=
        "{t}Oito: [p=0.2] para saber em quanto tempo um capital *dobra* a dez por cento, [p=0.2] divido log de dois [p=0.2] "
        "por *log de um vírgula um.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a "
        "tentação é dividir pela taxa, [p=0.2] zero vírgula um. [p=0.3] {g}Mas o denominador é o *log do fator.* [p=0.2] "
        "E o radar confirma: [p=0.2] uns *sete anos.*"),
    dict(id="16", block="vf", text=
        "{t}E nove: [p=0.2] à mesma taxa, [p=0.2] juros compostos rendem *sempre* mais que juros simples. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque, na maioria das contas, [p=0.2] é isso que acontece. "
        "[p=0.3] {g}Mas as escadas se cruzam em *um período.* [p=0.2] Antes dele, [p=0.2] o *simples* rende mais."),
    dict(id="17", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas. [p=0.2] Em todas, [p=0.2] comece escrevendo o *fator de um período.*"),

    # ================= QUESTÃO 1: JUROS COM POTÊNCIA FÁCIL =================
    dict(id="18", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma pessoa aplicou *seis mil reais* [p=0.2] a juros compostos de *cinco por cento ao "
        "mês,* [p=0.2] por *dois meses.* [p=0.3] {b}Os *juros* recebidos foram de [p=0.4] {la}A, [p=0.2] trezentos "
        "reais. [p=0.2] {lb}B, [p=0.2] seis mil seiscentos e quinze. [p=0.2] {lc}C, [p=0.2] seiscentos. [p=0.2] "
        "{ld}D, [p=0.2] seiscentos e quinze. [p=0.2] {le}E, [p=0.2] seis mil e seiscentos. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="19", block="q1", text=
        "{d}Fator de um mês: [p=0.2] *um vírgula zero cinco.* [p=0.3] {a}Dois meses: [p=0.2] ao quadrado, [p=0.2] *um "
        "vírgula um zero dois cinco.* [p=0.3] {b}Montante: [p=0.2] seis mil seiscentos e quinze. [p=0.2] Menos o capital: "
        "[p=0.2] *seiscentos e quinze.* [p=0.2] {ok}*Letra D!* [p=0.3] {v}Elimine pelo simples: [p=0.2] seiscentos. "
        "[p=0.2] O composto tem que passar disso. [p=0.4] {xc}A C é o juro simples, [p=0.2] {xa}a A parou em um mês. "
        "[p=0.2] {xb}A B é o montante, [p=0.2] {xe}e a E, o montante simples."),

    # ================= QUESTÃO 2: DÍVIDA COM POTÊNCIA DADA =================
    dict(id="20", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma dívida de *dois mil e quinhentos reais* no cartão [p=0.2] cresce *oito por "
        "cento ao mês.* [p=0.2] Use: [p=0.2] um vírgula zero oito *elevado a seis* [p=0.2] é cerca de *um vírgula "
        "cinquenta e nove.* [p=0.3] {b}Sem pagamentos, [p=0.2] depois de *doze meses,* [p=0.2] a dívida será de [p=0.4] "
        "{la}A, [p=0.2] seis mil trezentos e vinte e vinte e cinco centavos. [p=0.2] {lb}B, [p=0.2] três mil novecentos e "
        "setenta e cinco. [p=0.2] {lc}C, [p=0.2] quatro mil e novecentos. [p=0.2] {ld}D, [p=0.2] cinco mil quatrocentos "
        "e cinquenta. [p=0.2] {le}E, [p=0.2] sete mil novecentos e cinquenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q2", text=
        "{d}O enunciado deu *seis* meses, [p=0.2] e pede *doze:* [p=0.2] o dobro do tempo. [p=0.3] {a}Dobrar o tempo é "
        "*elevar ao quadrado:* [p=0.2] um vírgula cinquenta e nove ao quadrado, [p=0.2] *dois vírgula cinco dois oito "
        "um.* [p=0.3] {b}Vezes dois mil e quinhentos: [p=0.2] *seis mil trezentos e vinte e vinte e cinco.* [p=0.2] "
        "{ok}*Letra A!* [p=0.4] {xe}A E dobrou o fator. [p=0.2] {xd}A D somou os dois semestres. [p=0.2] {xb}A B parou em "
        "seis meses, [p=0.2] {xc}e a C é juro simples."),

    # ================= QUESTÃO 3: TEMPO PARA TRIPLICAR =================
    dict(id="22", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Um investimento rende *doze por cento ao ano,* [p=0.2] a juros compostos. [p=0.2] "
        "Use: [p=0.2] log de três, [p=0.2] zero vírgula quarenta e oito; [p=0.2] log de dois, [p=0.2] zero vírgula "
        "trinta; [p=0.2] log de um vírgula doze, [p=0.2] zero vírgula zero cinco. [p=0.3] {b}Em quanto tempo o capital "
        "*triplica?* [p=0.4] {la}A, [p=0.2] quatro anos. [p=0.2] {lb}B, [p=0.2] seis anos. [p=0.2] {lc}C, [p=0.2] cerca de "
        "dezesseis vírgula sete. [p=0.2] {ld}D, [p=0.2] vinte e cinco. [p=0.2] {le}E, [p=0.2] nove vírgula seis anos. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q3", text=
        "{d}Triplicar: [p=0.2] log de *três.* [p=0.2] Dividido pelo *log do fator.* [p=0.3] {a}Zero vírgula quarenta e "
        "oito [p=0.2] dividido por zero vírgula zero cinco: [p=0.2] *nove vírgula seis anos.* [p=0.2] {ok}*Letra E!* "
        "[p=0.3] {v}O radar: [p=0.2] setenta e dois dividido por doze, [p=0.2] seis anos para *dobrar.* [p=0.2] Triplicar "
        "vem depois. [p=0.4] {xb}A B usou log de dois, [p=0.2] {xa}e a A dividiu pela taxa. [p=0.2] {xc}A C e {xd}a D são "
        "juros simples."),

    # ================= QUESTÃO 4: VALOR PRESENTE =================
    dict(id="24", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Quanto alguém precisa aplicar *hoje,* [p=0.2] a *dez por cento ao ano,* [p=0.2] "
        "a juros compostos, [p=0.2] para ter *nove mil seiscentos e oitenta reais* [p=0.2] daqui a *dois anos?* [p=0.4] "
        "{la}A, [p=0.2] sete mil oitocentos e quarenta e oitenta. [p=0.2] {lb}B, [p=0.2] cerca de oito mil e sessenta e "
        "seis. [p=0.2] {lc}C, [p=0.2] oito mil. [p=0.2] {ld}D, [p=0.2] oito mil e oitocentos. [p=0.2] {le}E, [p=0.2] onze "
        "mil setecentos e doze e oitenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{d}O filme ao contrário: [p=0.2] *divida* pelo fator. [p=0.3] {a}Dois anos a dez por cento: [p=0.2] *um vírgula "
        "vinte e um.* [p=0.3] {b}Nove mil seiscentos e oitenta [p=0.2] dividido por um vírgula vinte e um: [p=0.2] *oito "
        "mil reais.* [p=0.2] {ok}*Letra C!* [p=0.3] {v}Confira multiplicando de volta: [p=0.2] oito mil vezes um vírgula "
        "vinte e um [p=0.2] dá os nove mil seiscentos e oitenta. [p=0.4] {xa}A A tirou dez por cento duas vezes. [p=0.2] "
        "{xb}A B usou o fator simples, [p=0.2] {xd}a D voltou só um ano, [p=0.2] {xe}e a E multiplicou."),

    # ================= QUESTÃO 5: SIMPLES × COMPOSTOS COM TAXAS DIFERENTES =================
    dict(id="26", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Para aplicar *vinte mil reais* por *dois anos,* [p=0.2] um banco oferece: "
        "[p=0.2] proposta um, [p=0.2] juros *simples* de *dezesseis* por cento ao ano; [p=0.2] proposta dois, [p=0.2] "
        "juros *compostos* de *quinze* por cento ao ano. [p=0.3] {b}A proposta que rende mais, [p=0.2] e quanto a mais: "
        "[p=0.4] {la}A, [p=0.2] a um, [p=0.2] quatrocentos reais. [p=0.2] {lb}B, [p=0.2] a dois, [p=0.2] cinquenta reais. "
        "[p=0.2] {lc}C, [p=0.2] a um, [p=0.2] quatrocentos e sessenta e dois. [p=0.2] {ld}D, [p=0.2] a dois, [p=0.2] quatro "
        "mil e dezessete e cinquenta. [p=0.2] {le}E, [p=0.2] a dois, [p=0.2] dezenove mil e seiscentos. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q5", text=
        "{d}As taxas são diferentes: [p=0.2] a regra geral *não decide.* [p=0.2] Faça a conta. [p=0.3] {a}Proposta um: "
        "[p=0.2] dezesseis mais dezesseis, [p=0.2] *trinta e dois por cento.* [p=0.2] Vinte e seis mil e quatrocentos. "
        "[p=0.3] {b}Proposta dois: [p=0.2] um vírgula quinze ao quadrado, [p=0.2] *um vírgula três dois dois cinco.* "
        "[p=0.2] Vinte e seis mil quatrocentos e cinquenta. [p=0.3] {c}A dois ganha por *cinquenta reais.* [p=0.2] "
        "{ok}*Letra B!* [p=0.4] {xa}A A calculou a dois como simples, [p=0.2] {xc}e a C, a um como composta. [p=0.2] "
        "{xd}A D contou um ano a mais, [p=0.2] {xe}e a E dobrou o fator."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="28", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Juros sobre juros, [p=0.2] a fórmula [p=0.2] e as "
        "taxas em sequência: [p=0.2] episódio um. [p=0.3] {c}Simples contra compostos, [p=0.2] PG [p=0.2] e duplicação: "
        "[p=0.2] episódio dois."),
    dict(id="29", block="checklist", text=
        "{a}Potências, [p=0.2] tentativa, [p=0.2] logaritmos [p=0.2] e a regra do setenta e dois: [p=0.2] episódio três. "
        "[p=0.3] {b}Valor presente: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o "
        "episódio correspondente."),

    # ================= META =================
    dict(id="30", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte questões* de juros compostos [p=0.2] {b}e acerte pelo menos *catorze,* "
        "[p=0.2] setenta por cento. [p=0.4] {c}Inclua questões com *logaritmos fornecidos* [p=0.2] e com *comparação "
        "entre regimes.*"),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}O próximo assunto é *Descontos, acréscimos, lucro e prejuízo:* [p=0.3] {b}a matemática do balcão, [p=0.2] com "
        "os mesmos fatores, [p=0.3] {c}e uma pergunta nova que derruba muita gente: [p=0.3] {d}porcentagem *de quê,* "
        "[p=0.2] do *custo* ou da *venda?*"),
    dict(id="32", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de juros compostos está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
