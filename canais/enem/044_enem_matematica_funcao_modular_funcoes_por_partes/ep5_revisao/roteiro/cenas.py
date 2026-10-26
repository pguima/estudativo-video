# Roteiro — Função Modular e Funções por Partes, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e
#   treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/29-funcao-modular-funcoes-por-partes.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9; a Q5 nem aparece). As 5 questões são INÉDITAS (números e erros do prompt do usuário).
#   Função composta e inversa: só a ponte.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (números por extenso; o gancho só acrescenta, depois delas, o que a aula
#   vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 o PRÉDIO DE ANDARES (descubra o andar antes da regra) · CADA FAIXA PARTE DE ONDE A ANTERIOR PAROU · a CATRACA
#       do "hora ou fração" (ícone: prédio de andares) ·
#   ep2 a ESCADA DE CAIXINHAS · o ALARME do "excedente" · o TROCO da parcela a deduzir (ícone: escada de caixinhas) ·
#   ep3 MÓDULO É DISTÂNCIA · o VÉRTICE MORA ONDE O DE DENTRO ZERA · o ESPELHO NO CHÃO do |f(x)| (ícone: V na reta) ·
#   ep4 MENOR FICA ENTRE, MAIOR FICA FORA · o ELÁSTICO da tolerância (ícone: elástico).
# Prática de recuperação: a cena 04 abre com uma pergunta e pausa antes do índice; cada V/F e cada questão têm pausa.
# O que a prova cobra (seção 01): tarifas por faixas · escolher o gráfico · tolerância (|x − 50| ≤ 2) · distâncias na
#   reta. O que mais rende: localizar a faixa antes de calcular; no progressivo, cada parte na sua faixa.
# Onde aparece (seção 10): Física (vai 3 km e volta 3 km: deslocamento 0, percurso 6 km; erro de medida x ± Δx) ·
#   Estatística (desvio médio absoluto) · Matemática Financeira (impostos progressivos) · Geografia (|9 − (−4)| = 13 °C).
# V/F (os 9 erros da seção 11, NA ORDEM do material). DESVIO NOSSO (marcado): para o jogo não ter resposta previsível,
#   três frases aparecem na versão CERTA (verdadeiras: 2, 6 e 8); as outras seis são o erro (falsas):
#   1 F |x| = 5 → x = 5 (5 ou −5) · 2 V |x| = −3 não tem solução · 3 F |x| < 4 → x < ±4 (−4 < x < 4) ·
#   4 F |x − 3|: o V vai 3 para a esquerda (direita: x = 3) · 5 F |a + b| = |a| + |b| sempre (|−3 + 3| = 0, mas 6) ·
#   6 V √(x²) = |x| · 7 F progressivo: a alíquota da última faixa vale para o valor todo (faixa por faixa) ·
#   8 V descubra a faixa antes de escolher a lei · 9 F "hora ou fração" proporcional: R$ 5,00 a hora, 2 h 20 min →
#   R$ 11,67 (arredonda para cima: 3 h, R$ 15,00). Números NOSSOS, fora das Q1–Q9 e das questões dos eps. 1 a 4.
# QUESTÕES INÉDITAS (do prompt; conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro
#   clássico; a ordem das letras é nossa, com as alternativas numéricas em ordem crescente):
#   Q1 energia progressiva (até 100 kWh R$ 0,50; 100–200 R$ 0,80 no excedente; acima de 200 R$ 1,10 no excedente),
#      250 kWh: 50 + 80 + 55 = R$ 185,00 → C. A 125 (1ª taxa sobre tudo) · B 170 (esqueceu a 3ª faixa: 50 + 150 · 0,80) ·
#      D 215 (pulou a do meio: 50 + 150 · 1,10) · E 275 (taxa da última faixa sobre tudo).
#   Q2 qual gráfico: R$ 30,00 com 5 GB e R$ 6,00 por GB excedente → trecho horizontal até 5 e reta subindo, SEM salto → E.
#      Teste de dois pontos: f(2) = 30 e f(8) = 48. A reta desde a origem (f(2) = 12) · B reta começando em 30 desde o
#      zero (f(2) = 42) · C salto em 5, cobrando de novo os 5 GB da franquia (f(8) = 78) · D escada: ACRÉSCIMO NOSSO
#      (marcado) — a escada passa nos dois pontos de teste; o que a elimina é o meio: não está escrito "ou fração",
#      então 6,5 GB custam 30 + 6 · 1,5 = 39, e a escada daria 42.
#   Q3 bicicleta: R$ 8,00 pela 1ª meia hora + R$ 3,00 por meia hora adicional ou fração; 1 h 50 min = 110 min → sobram
#      80 min = 2 meias horas + 20 min (conta como mais uma) → 8 + 3 · 3 = R$ 17,00 → D. A 12 (3 · 4, esqueceu a 1ª
#      tarifa) · B 14 (ignorou a fração) · C 16 (proporcional: 8 + 3 · 80/30) · E 20 (cobrou as 4 meias horas como
#      adicionais).
#   Q4 câmara fria a no máximo 1,5 °C de −18 °C: |T + 18| ≤ 1,5 → −19,5 ≤ T ≤ −16,5 → A. B 16,5 a 19,5 (erro de sinal:
#      o centro é −18) · C −18,75 a −17,25 (dividiu a tolerância por 2) · D pontas excluídas ("no máximo" inclui) ·
#      E T ≤ −19,5 ou T ≥ −16,5 (o "fora").
#   Q5 entregador a 7 km do km 30: |x − 30| = 7 → 23 ou 37 → B. A só 37 · C só 23 (esqueceram um lado) · D 23 e 30
#      (confundiu o centro com uma resposta) · E −23 e 37 (errou o sinal ao subtrair).
# Gabaritos: C, E, D, A, B.
# Atalhos (verde): os 3 hábitos (cenas 08 e 09) · a catraca na Q3 · a conferência substituindo na Q5.
# Checklist (seção 13) → episódio (como o prompt pede): tarifas, franquia, escada e gráfico por partes → ep1 ·
#   progressivo → ep2 · módulo, V e rebatimento → ep3 · equações, inequações e tolerância → ep4.
# Meta (prompt e material): 25 questões, 18 acertos, com pelo menos dez de tarifas por faixas ou gráfico por partes.
# Ponte (do usuário): Função composta e função inversa.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão: conta de água, estacionamento e tolerância | Função Modular Ep. 5"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, passo a passo. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}O ENEM quase nunca escreve *\"função modular\".* [p=0.4] {b}Ele escreve *\"conta de água\",* [p=0.2] "
        "*\"estacionamento\",* [p=0.2] *\"tolerância de dois milímetros\".* [p=0.4] {c}Hoje você aprende a ver *a função "
        "por trás do texto.* [p=0.4] {d}Nove frases de verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Calcular uma tarifa por faixas:* [p=0.2] água, energia, frete, plano de "
        "celular. [p=0.3] {b}*Escolher o gráfico certo.* [p=0.3] {c}Interpretar *tolerâncias:* [p=0.2] variar no máximo "
        "dois milímetros em torno de cinquenta é módulo de xis menos cinquenta, menor ou igual a dois. [p=0.3] {d}E "
        "*distâncias na reta.*"),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.3] Duas habilidades. [p=0.4] {a}Primeiro: [p=0.2] *descobrir a faixa* antes de "
        "aplicar a fórmula. [p=0.2] A lei certa depende da entrada. [p=0.4] {b}Segundo: [p=0.2] no progressivo, [p=0.2] "
        "*cada parte paga a taxa da sua faixa,* [p=0.2] e não o valor inteiro na taxa da última."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] tente lembrar: [p=0.2] numa função por partes, [p=0.2] qual é o *primeiro* passo? "
        "[p=1.2] {a}Um: [p=0.2] o *prédio de andares.* [p=0.2] Descubra o andar antes da regra. [p=0.2] Cada faixa "
        "*parte de onde a anterior parou,* [p=0.2] e \"hora ou fração\" é *catraca.* [p=0.4] {b}Dois: [p=0.2] a *escada "
        "de caixinhas* do progressivo. [p=0.2] A palavra *\"excedente\"* é o alarme, [p=0.2] e a parcela a deduzir é o "
        "*troco.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] *módulo é distância.* [p=0.2] O vértice mora *onde o de dentro zera,* [p=0.2] e o módulo de "
        "efe de xis é um *espelho no chão.* [p=0.4] {b}Quatro: [p=0.2] *menor fica entre, maior fica fora,* [p=0.2] e a "
        "tolerância é um *elástico* preso no centro."),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}Na *Física,* [p=0.2] quem vai três quilômetros para a frente e volta três "
        "[p=0.2] tem deslocamento *zero,* [p=0.2] mas percorreu *seis.* [p=0.2] E o erro de medida, xis mais ou menos "
        "delta xis, [p=0.2] é uma tolerância. [p=0.3] {b}Na *Estatística,* [p=0.2] o desvio médio usa módulo [p=0.2] "
        "para os desvios *não se anularem.*"),
    dict(id="07", block="onde", text=
        "{c}Na *Matemática Financeira,* [p=0.2] impostos progressivos: [p=0.2] cada parte na sua alíquota. [p=0.3] {d}E "
        "na *Geografia,* [p=0.2] a amplitude térmica entre menos quatro e nove graus [p=0.2] é o módulo de nove menos "
        "menos quatro: [p=0.2] *treze graus.*"),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Três hábitos. [p=0.4] {a}Um: [p=0.2] *localize a faixa antes de calcular.* "
        "[p=0.2] Escreva ao lado do valor qual linha da regra ele usa, [p=0.2] e calcule só com ela. [p=0.2] {a2}Na "
        "fronteira, [p=0.2] confira o *menor ou igual.*"),
    dict(id="09", block="habitos", text=
        "{b}Dois: [p=0.2] em \"qual gráfico\", [p=0.2] *teste dois pontos,* um de cada faixa. [p=0.2] Trecho horizontal é "
        "valor fixo; [p=0.2] salto é mudança de regra sem continuidade. [p=0.4] {c}Três: [p=0.2] *transforme módulo em "
        "distância,* [p=0.2] desenhe a reta [p=0.2] e *confira substituindo.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] se o módulo de xis é cinco, [p=0.2] então xis é *cinco.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque o cinco está ali, pronto. [p=0.3] {g}Mas *dois* pontos estão a cinco do zero: [p=0.2] "
        "*cinco e menos cinco.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] módulo de xis igual a *menos três* [p=0.2] não tem solução. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade de escrever mais ou menos três. [p=0.3] {g}Mas "
        "distância *nunca é negativa:* [p=0.2] conjunto vazio."),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] módulo de xis menor que quatro [p=0.2] dá *xis menor que mais ou menos quatro.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque imita a equação. [p=0.3] {g}Mas *menor fica entre:* "
        "[p=0.2] xis entre menos quatro e quatro."),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] no gráfico de módulo de xis menos três, [p=0.2] o vê anda três para a *esquerda.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o sinal de menos parece \"para trás\". [p=0.3] {g}Mas o "
        "vértice mora *onde o de dentro zera:* [p=0.2] xis igual a três, *para a direita.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] o módulo de uma soma [p=0.2] é *sempre* a soma dos módulos. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque funciona com dois positivos. [p=0.3] {g}Mas módulo de menos três mais "
        "três é *zero,* [p=0.2] e a soma dos módulos dá *seis.* [p=0.2] Só vale com o *mesmo sinal.*"),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] a raiz quadrada de xis ao quadrado [p=0.2] é o *módulo* de xis. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a raiz \"desfaz\" o quadrado. [p=0.3] {g}Mas teste menos cinco: "
        "[p=0.2] ao quadrado, vinte e cinco; [p=0.2] a raiz dá *cinco,* positivo."),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] num imposto progressivo, [p=0.2] a alíquota da *última faixa* vale para o lucro todo. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a tabela mostra a alíquota da faixa onde o lucro "
        "terminou. [p=0.3] {g}Mas é a *escada de caixinhas:* [p=0.2] *cada fatia paga a taxa da sua.*"),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] numa função por partes, [p=0.2] primeiro você descobre a *faixa* da entrada, [p=0.2] e só "
        "depois escolhe a lei. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece exagero porque a primeira "
        "linha está bem ali. [p=0.3] {g}Mas é o *prédio:* [p=0.2] o andar decide a regra, [p=0.2] e na fronteira, "
        "confira o *menor ou igual.*"),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] um estacionamento cobra *cinco reais por hora ou fração.* [p=0.2] Duas horas e vinte "
        "custam *onze e sessenta e sete.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a conta "
        "proporcional parece justa. [p=0.3] {g}Mas é *catraca:* [p=0.2] começou a hora, pagou inteira. [p=0.2] Três "
        "horas, *quinze reais.*"),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *ache a faixa* ou *a distância* antes de qualquer conta, [p=0.2] e "
        "*confira* no fim."),

    # ================= QUESTÃO 1: ENERGIA PROGRESSIVA =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma companhia cobra a energia por faixas: [p=0.2] até cem quilowatts-hora, "
        "*cinquenta centavos* por quilowatt-hora; [p=0.2] de cem a duzentos, *oitenta centavos* por quilowatt-hora "
        "excedente; [p=0.2] acima de duzentos, *um real e dez* por quilowatt-hora excedente. [p=0.3] {b}Quanto paga quem "
        "consome *duzentos e cinquenta?* [p=0.4] {la}A, [p=0.2] cento e vinte e cinco reais. [p=0.2] {lb}B, [p=0.2] "
        "cento e setenta. [p=0.2] {lc}C, [p=0.2] cento e oitenta e cinco. [p=0.2] {ld}D, [p=0.2] duzentos e quinze. "
        "[p=0.2] {le}E, [p=0.2] duzentos e setenta e cinco. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}O alarme tocou: [p=0.2] *\"excedente\".* [p=0.2] É progressivo. [p=0.3] {a}Fatie o consumo: [p=0.2] cem a "
        "cinquenta centavos, *cinquenta reais;* [p=0.2] mais cem a oitenta centavos, *oitenta;* [p=0.2] e os cinquenta "
        "que passaram de duzentos, a um e dez, *cinquenta e cinco.* [p=0.2] Total: *cento e oitenta e cinco.* [p=0.2] "
        "{ok}*Letra C!* [p=0.4] {xe}A E pôs a taxa da última faixa *em tudo.* [p=0.2] {xa}A A usou a primeira em tudo. "
        "[p=0.2] {xb}A B esqueceu a terceira faixa, [p=0.2] {xd}e a D pulou a do meio."),

    # ================= QUESTÃO 2: QUAL GRÁFICO =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Um plano de celular custa *trinta reais* com *cinco gigas* de franquia, [p=0.2] e "
        "*seis reais* por giga excedente. [p=0.3] {b}Qual gráfico representa o valor da conta em função do consumo? "
        "[p=0.4] {la}A, [p=0.2] {lb}B, [p=0.2] {lc}C, [p=0.2] {ld}D [p=0.2] {le}ou E. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Teste dois pontos, um de cada faixa. [p=0.2] Com dois gigas, [p=0.2] dentro da franquia: [p=0.2] *trinta.* "
        "[p=0.2] Com oito, [p=0.2] três excedentes: [p=0.2] trinta mais dezoito, *quarenta e oito.* [p=0.3] {xa}A A sai "
        "da origem, [p=0.2] {xb}e a B começa a subir desde o zero: [p=0.2] as duas erram o dois. [p=0.2] {xc}A C dá um "
        "*salto* no cinco: [p=0.2] cobrou de novo os gigas da franquia. [p=0.3] {xd}E a escada passa nos dois pontos, "
        "[p=0.2] mas o texto *não diz* \"ou fração\": [p=0.2] o pedaço do meio é reta. [p=0.2] {ok}*Letra E!*"),

    # ================= QUESTÃO 3: HORA OU FRAÇÃO =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Um aluguel de bicicletas cobra *oito reais* pela primeira meia hora [p=0.2] e *três "
        "reais* por meia hora adicional *ou fração.* [p=0.3] {b}Quanto paga quem usa a bicicleta por *uma hora e "
        "cinquenta minutos?* [p=0.4] {la}A, [p=0.2] doze reais. [p=0.2] {lb}B, [p=0.2] catorze. [p=0.2] {lc}C, [p=0.2] "
        "dezesseis. [p=0.2] {ld}D, [p=0.2] dezessete. [p=0.2] {le}E, [p=0.2] vinte. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Uma hora e cinquenta são *cento e dez minutos.* [p=0.2] Tire a primeira meia hora: [p=0.2] sobram *oitenta.* "
        "[p=0.3] {a}Oitenta minutos são duas meias horas e mais vinte. [p=0.2] Catraca: [p=0.2] os vinte contam como "
        "*mais uma.* [p=0.2] Três adicionais: [p=0.2] oito mais nove, *dezessete reais.* [p=0.2] {ok}*Letra D!* [p=0.4] "
        "{xc}A C cobrou a fração *proporcional.* [p=0.2] {xb}A B ignorou a fração, [p=0.2] {xe}a E cobrou as quatro meias "
        "horas como adicionais, [p=0.2] {xa}e a A esqueceu a primeira tarifa."),

    # ================= QUESTÃO 4: TOLERÂNCIA =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Uma câmara fria deve ficar a *no máximo um vírgula cinco grau* de *menos "
        "dezoito.* [p=0.3] {b}As temperaturas permitidas são: [p=0.4] {la}A, [p=0.2] de menos dezenove e meio a menos "
        "dezesseis e meio. [p=0.2] {lb}B, [p=0.2] de dezesseis e meio a dezenove e meio. [p=0.2] {lc}C, [p=0.2] de menos "
        "dezoito vírgula setenta e cinco a menos dezessete vírgula vinte e cinco. [p=0.2] {ld}D, [p=0.2] entre menos "
        "dezenove e meio e menos dezesseis e meio, sem as pontas. [p=0.2] {le}E, [p=0.2] até menos dezenove e meio, ou a "
        "partir de menos dezesseis e meio. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}O elástico: [p=0.2] preso no centro, *menos dezoito,* [p=0.2] estica *um e meio* para cada lado. [p=0.2] Em "
        "módulo: [p=0.2] módulo de tê mais dezoito, *menor ou igual* a um e meio. [p=0.3] {a}Menor fica entre: [p=0.2] "
        "de *menos dezenove e meio* a *menos dezesseis e meio,* [p=0.2] com as pontas. [p=0.2] {ok}*Letra A!* [p=0.4] "
        "{xb}A B errou o sinal do centro. [p=0.2] {xc}A C dividiu o elástico por dois, [p=0.2] {xd}a D tirou as pontas, "
        "[p=0.2] e \"no máximo\" inclui. [p=0.2] {xe}E a E pegou o *fora.*"),

    # ================= QUESTÃO 5: DISTÂNCIA NA RETA =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Numa avenida retilínea, [p=0.2] um entregador está a *sete quilômetros* do "
        "*quilômetro trinta.* [p=0.3] {b}Em que quilômetro ele pode estar? [p=0.4] {la}A, [p=0.2] só no trinta e sete. "
        "[p=0.2] {lb}B, [p=0.2] no vinte e três ou no trinta e sete. [p=0.2] {lc}C, [p=0.2] só no vinte e três. [p=0.2] "
        "{ld}D, [p=0.2] no vinte e três ou no trinta. [p=0.2] {le}E, [p=0.2] no menos vinte e três ou no trinta e sete. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Módulo é distância: [p=0.2] módulo de xis menos trinta, *igual a sete.* [p=0.3] {a}Na reta, [p=0.2] ande sete "
        "para cada lado do trinta: [p=0.2] *vinte e três* [p=0.2] e *trinta e sete.* [p=0.2] {v}Confira substituindo: "
        "[p=0.2] trinta e sete menos trinta, sete; [p=0.2] vinte e três menos trinta, menos sete, em módulo, sete. "
        "[p=0.2] {ok}*Letra B!* [p=0.4] {xa}{xc}A A e a C esqueceram *um lado.* [p=0.2] {xd}A D pôs o centro como "
        "resposta, [p=0.2] {xe}e a E errou o sinal."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}Tarifas, franquia, a escada do \"hora ou fração\" e o gráfico por partes: "
        "[p=0.2] episódio um. [p=0.3] {c}Imposto e tarifa progressiva, faixa por faixa: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Módulo como distância, o vê deslocado e o rebatimento: [p=0.2] episódio três. [p=0.3] {b}Equações, "
        "inequações e tolerância: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o "
        "episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte e cinco questões* [p=0.2] {b}e acerte pelo menos *dezoito.* [p=0.4] {c}E "
        "pelo menos *dez* delas de tarifas por faixas [p=0.2] ou de leitura de gráfico por partes."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Função composta e função inversa:* [p=0.3] {b}as funções passam a ser *encadeadas,* "
        "[p=0.2] uma dentro da outra, [p=0.3] {c}e *desfeitas.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de função modular e funções por partes "
        "está completa. [p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
