# Estudativo · MAT-FRA-006 — Praticando: o que é uma fração (Matemática · Frações e Decimais · prática).
# Habilidade: simplificar, comparar e calcular a fração de uma quantidade em situações do dia a dia.
# Pré-requisitos: MAT-FRA-001, MAT-FRA-002, MAT-FRA-003, MAT-FRA-004, MAT-FRA-005. Próxima: MAT-FRA-007.
# Questões inéditas, criadas para esta aula. Soma e subtração de frações ainda não foram ensinadas (MAT-FRA-007).

TITULO = "Praticando: o que é uma fração"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações do dia a dia, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}simplificar, [p=0.2] {b}comparar, [p=0.2] {c}calcular a fração de uma quantidade [p=0.2] e {d}escrever número misto. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: simplificar
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Em um mês de {b}trinta dias, uma pessoa trabalhou {c}vinte e quatro. [p=0.3] {d}Que fração do mês ela trabalhou, na forma mais simples?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Parte em cima, total embaixo: {a}vinte e quatro trinta avos. [p=0.3] O MDC, o maior número que divide vinte e quatro e trinta, é {b}seis. [p=0.2] {c}Vinte e quatro dividido por seis, quatro. [p=0.2] {d}Trinta dividido por seis, cinco. [p=0.3] {e}Quatro quintos do mês. [p=0.3] Repare que embaixo vai {f}o mês inteiro, e não só os dias de folga."),
    dict(id="s06", block="resposta1", text="Não achou o MDC de primeira? [p=0.2] Sem problema. [p=0.2] {a}Divida em cima e embaixo por dois: doze quinze avos. [p=0.2] {b}Depois por três. [p=0.2] Chega nos mesmos {c}quatro quintos."),
    # situação 2: comparar
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Duas lojas vendem a mesma geladeira pelo mesmo preço. [p=0.2] A loja A pede {b}dois quintos de entrada. [p=0.2] A loja B pede {c}três oitavos. [p=0.3] {d}Qual pede a menor entrada?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Como o preço é o mesmo, dá para comparar só as frações. [p=0.2] Vamos pelo teste da cruz. [p=0.2] {a}Dois vezes oito, dezesseis, do lado de dois quintos. [p=0.2] {b}Cinco vezes três, quinze, do lado de três oitavos. [p=0.3] Dezesseis é maior, então {c}dois quintos é a fração maior. [p=0.3] Pelo MMC dá o mesmo: {d}dezesseis quarenta avos contra {e}quinze quarenta avos."),
    dict(id="s10", block="resposta2", text="Cuidado com a pergunta: ela quer {a}a menor entrada. [p=0.3] A resposta é {b}a loja B. [p=0.3] Esse é o erro mais comum: fazer a conta certa e {c}responder o contrário. [p=0.2] Leia o fim do enunciado de novo antes de responder."),
    # situação 3: fração de uma quantidade
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Em uma viagem de {b}duzentos e quarenta quilômetros, o carro já percorreu {c}cinco sextos do caminho. [p=0.3] {d}Quantos quilômetros ele já percorreu?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Duzentos e quarenta é {a}o total: divide pelo de baixo, multiplica pelo de cima. [p=0.3] {b}Duzentos e quarenta dividido por seis, quarenta. [p=0.2] {c}Quarenta vezes cinco, duzentos quilômetros."),
    # atalho
    dict(id="s14", block="atalho", text="Aqui cabe um atalho de prova: {a}tire o pedaço que falta. [p=0.3] Cinco sextos é tudo, menos um sexto. [p=0.2] {b}Duzentos e quarenta menos quarenta: {c}duzentos."),
    dict(id="s15", block="atalho", text="Funciona porque {a}falta só uma parte para o inteiro. [p=0.3] Não compensa quando falta muito, como em {b}dois sétimos: [p=0.2] aí, vale {c}a conta normal."),
    # situação 4: da parte para o total
    dict(id="s16", block="questao4", text="{a}Situação quatro. [p=0.2] Uma pessoa juntou {b}quatrocentos e cinquenta reais, [p=0.1] que são {c}três sétimos do preço de uma televisão. [p=0.3] {d}Quanto custa a televisão?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] Quatrocentos e cinquenta é {a}a parte, não o total. [p=0.2] Então divide pelo de cima: {b}quatrocentos e cinquenta dividido por três, cento e cinquenta. [p=0.2] Esse é o valor de um sétimo."),
    dict(id="s19", block="resposta4", text="O preço são sete partes: {a}cento e cinquenta vezes sete, {b}mil e cinquenta reais. [p=0.3] A resposta é {c}maior que a parte: faz sentido. [p=0.3] Para conferir: {d}mil e cinquenta dividido por sete, cento e cinquenta. [p=0.2] {e}Vezes três, quatrocentos e cinquenta. [p=0.2] Bateu."),
    # situação 5: número misto e simplificação
    dict(id="s20", block="questao5", text="{a}Última situação, e ela junta tudo. [p=0.2] Uma lanchonete corta cada torta em {b}seis pedaços. [p=0.2] Hoje, vendeu {c}vinte pedaços. [p=0.3] {d}Quantas tortas foram vendidas, em número misto e na forma mais simples?"),
    dict(id="s21", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta5", text="Vamos lá. [p=0.2] Cada pedaço é um sexto, então são {a}vinte sextos. [p=0.3] Tabuada do seis: {b}seis vezes três, dezoito. [p=0.2] De dezoito para vinte, {c}faltam dois. [p=0.3] Deu {d}três inteiros e dois sextos."),
    dict(id="s23", block="resposta5", text="Dois sextos ainda simplifica. [p=0.2] Dois e seis são pares, então {a}divida em cima e embaixo por dois: {b}um terço. [p=0.3] Resposta: {c}três inteiros e um terço de torta. [p=0.3] Outro caminho: {d}simplifique antes. [p=0.2] {e}Vinte sextos vira dez terços. [p=0.2] Dez dividido por três dá três e sobra um. [p=0.2] Com números menores, {f}a mesma resposta."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}leia o que a pergunta pede, [p=0.2] {b}veja se o número é a parte ou o total [p=0.2] e {c}confira se a resposta faz sentido."),
    dict(id="s25", block="fim", text="Na próxima aula, você começa a {a}somar e subtrair frações, [p=0.2] primeiro com {b}denominadores iguais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
