# Estudativo · MAT-PRO-012 — Praticando: progressão geométrica (Matemática · Progressões · Progressão geométrica · prática).
# Habilidade: achar termos e somas de PG em problemas de juros, meia-vida e quiques.
# Pré-requisitos: MAT-PRO-008, MAT-PRO-009, MAT-PRO-010, MAT-PRO-011. Próxima: nenhuma na trilha (fecha Progressões; a aula seguinte do curso é MAT-TRI-001).
# Questões inéditas, criadas para esta aula. Meia-vida explicada na hora (o assunto tem aula própria em Exponencial). Termos narrados como "o quarto termo" (sem "á quatro").
# 1 Juros: 2.000 a 10% ao mês, 3 meses · 2.000; 2.200; 2.420; 2.662 · 2.000 · 1,1³ = 2.000 · 1,331 = 2.662 (quarto termo: mês zero é o primeiro).
# 2 Meia-vida: 800 mg, 6 h, 24 h · 24/6 = 4 · 800; 400; 200; 100; 50 · 800/2⁴ = 50 · erro 800/4 = 200.
# 3 Termo do meio: 9 mil e 16 mil · x² = 144 · x = 12 mil (−12 descartado) · razão 12/9 = 16/12 = 4/3 · armadilha média (9 + 16)/2 = 12,5 (PA).
# 4 Soma: 300, razão 2, 6 semanas · 300 · (2⁶ − 1)/(2 − 1) = 300 · 63 = 18.900 · atalho: 6ª semana 300 · 2⁵ = 9.600; seguinte 19.200 − 300 = 18.900.
# 5 Quiques: 5 m, sobe 3/5 · atalho 5 · (8/5)/(2/5) = 5 · 4 = 20 · somas: subidas 3/(2/5) = 7,5 · 5 + 7,5 + 7,5 = 20.
# Visual: um cartão por problema (número grande do problema + ícone: cofre, gota de remédio, placa de Petri, cofrinho de campanha, bola);
#   fila de caixas com mês 0 a 3 embaixo no problema 1; E.colunas caindo pela metade no 2; 9 · 16 = 144 com √ no 3; 200 riscado em vermelho no 2 e 12,5 no 3;
#   bola quicando (E.curva) no 5.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: progressão geométrica"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # gancho
    dict(id="s01", block="gancho", text="{a}Cinco problemas de progressão geométrica, [p=0.2] criados para esta aula. [p=0.3] Em cada um, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}o termo geral, [p=0.2] {b}o termo do meio, [p=0.2] {c}a soma de uma quantidade de termos [p=0.2] e {d}a soma infinita. [p=0.3] Se alguma travar, procure a aula no canal."),
    # problema 1: juros
    dict(id="s03", block="questao1", text="{a}Problema um. [p=0.2] Você aplica {b}dois mil reais a dez por cento ao mês, em juros compostos. [p=0.3] Os valores de cada mês formam uma pê gê. [p=0.2] {c}Quanto você tem depois de três meses?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Somar dez por cento é {a}multiplicar por um vírgula um: essa é a razão. [p=0.2] A lista começa no dinheiro de hoje. [p=0.2] {b}Dois mil. [p=0.2] Depois, dois mil e duzentos. [p=0.2] Depois, dois mil quatrocentos e vinte. [p=0.2] Depois, {c}dois mil seiscentos e sessenta e dois reais."),
    dict(id="s06", block="resposta1", text="Pelo termo geral: {a}dois mil vezes um vírgula um ao cubo. [p=0.2] {b}Um vírgula um ao cubo dá um vírgula trezentos e trinta e um. [p=0.2] {c}Vezes dois mil dá dois mil seiscentos e sessenta e dois. [p=0.3] Repare: três meses depois é {d}o quarto termo, não o terceiro, [p=0.2] porque {e}o dinheiro de hoje é o primeiro."),
    # problema 2: meia-vida
    dict(id="s07", block="questao2", text="{a}Problema dois. [p=0.2] {b}Meia-vida é o tempo para uma quantidade cair pela metade. [p=0.2] Um remédio tem meia-vida de {c}seis horas no sangue. [p=0.2] Uma pessoa toma {d}oitocentos miligramas. [p=0.3] {e}Quanto resta depois de vinte e quatro horas?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] {a}Vinte e quatro dividido por seis dá quatro: são quatro meias-vidas. [p=0.2] É uma pê gê de {b}razão um meio. [p=0.2] {c}Oitocentos. [p=0.2] Quatrocentos. [p=0.2] Duzentos. [p=0.2] Cem. [p=0.2] {d}Restam cinquenta miligramas."),
    dict(id="s10", block="resposta2", text="O erro aqui é {a}dividir oitocentos por quatro e achar duzentos. [p=0.2] São quatro metades seguidas: [p=0.2] {b}oitocentos dividido por dezesseis, [p=0.2] porque {c}dois elevado a quatro dá dezesseis."),
    # problema 3: termo do meio
    dict(id="s11", block="questao3", text="{a}Problema três. [p=0.2] Uma cultura de bactérias cresce em pê gê, hora a hora. [p=0.2] {b}Às oito da manhã, eram nove mil. [p=0.2] {c}Às dez, eram dezesseis mil. [p=0.3] {d}Quantas eram às nove?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] As nove horas são {a}o termo do meio. [p=0.2] O do meio ao quadrado é {b}o produto dos vizinhos. [p=0.2] Contando em milhares, {c}nove vezes dezesseis dá cento e quarenta e quatro. [p=0.2] {d}A raiz dá doze: doze mil bactérias. [p=0.2] Menos doze não serve, porque {e}não existe quantidade negativa."),
    dict(id="s14", block="resposta3", text="Quem fez {a}a média, e achou doze mil e quinhentos, [p=0.2] tratou a lista como pê á, [p=0.2] que soma o mesmo número a cada hora. [p=0.3] Na pê gê, {b}a razão é quatro terços nas duas horas: [p=0.2] de nove para doze, e de doze para dezesseis."),
    # problema 4: soma finita
    dict(id="s15", block="questao4", text="{a}Problema quatro. [p=0.2] Uma campanha arrecadou {b}trezentos reais na primeira semana. [p=0.2] Em cada semana seguinte, {c}o dobro da anterior. [p=0.3] {d}Quanto arrecadou ao todo em seis semanas?"),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Vamos lá. [p=0.2] Pê gê de {a}primeiro termo trezentos, razão dois e seis termos. [p=0.2] {b}Dois elevado a seis dá sessenta e quatro. [p=0.2] {c}Menos um dá sessenta e três. [p=0.2] {d}Vezes trezentos dá dezoito mil e novecentos. [p=0.2] Dividido por dois menos um, que dá um, [p=0.2] {e}continuam dezoito mil e novecentos reais."),
    dict(id="s18", block="resposta4", text="Pelo atalho: a sexta semana teve {a}trezentos vezes trinta e dois, que dá nove mil e seiscentos. [p=0.2] {b}A semana seguinte teria dezenove mil e duzentos. [p=0.2] {c}Tire os trezentos do começo: sobram dezoito mil e novecentos. [p=0.2] Bateu."),
    # problema 5: quiques
    dict(id="s19", block="questao5", text="{a}Último problema. [p=0.2] Uma bola cai de {b}cinco metros. [p=0.2] Em cada quique, sobe {c}três quintos da altura de que caiu. [p=0.3] {d}Que distância ela percorre até parar?"),
    dict(id="s20", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta5", text="Vamos lá, pelo atalho da bola. [p=0.2] {a}Um mais três quintos dá oito quintos. [p=0.2] {b}Um menos três quintos dá dois quintos. [p=0.2] {c}Oito quintos dividido por dois quintos dá quatro. [p=0.2] {d}Cinco vezes quatro dá vinte metros."),
    dict(id="s22", block="resposta5", text="Conferindo pelas somas: as subidas começam em {a}três metros. [p=0.2] {b}Três dividido por dois quintos dá sete e meio. [p=0.2] {c}Cinco da queda, mais sete e meio subindo, mais sete e meio descendo, dá vinte. [p=0.2] Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}uma posição pede o termo geral. [p=0.2] {b}Dois vizinhos pedem o termo do meio. [p=0.2] {c}Um total pede a soma, [p=0.2] e {d}a bola pede a soma infinita, com subida e descida."),
    dict(id="s24", block="fim", text="Com isso, você fecha {a}progressões. [p=0.3] Na próxima aula, começa {b}trigonometria: [p=0.2] {c}seno, cosseno e tangente no triângulo retângulo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
