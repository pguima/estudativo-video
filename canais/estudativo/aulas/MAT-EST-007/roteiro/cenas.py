# Estudativo · MAT-EST-007 — Praticando: dados, tabelas e gráficos (Matemática · Estatística · Dados, tabelas e gráficos · prática).
# Habilidade: ler dados em tabelas e gráficos e calcular porcentagens e variações a partir deles.
# Pré-requisitos: MAT-EST-001 a MAT-EST-006, MAT-POR-005 (variação percentual). Próxima: MAT-EST-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula; todos os dados são inventados.
# 1 Barras (50 pessoas, esporte; grade de 2 em 2): futebol 20, vôlei 12 (6ª linha), corrida 10, natação 8. Vôlei 12/50 = 24%.
# 2 Linhas (público de um cinema): jan 300, fev 360, mar 320, abr 480, mai 500. Altas +60, −40, +160, +20. Maior: mar→abr, 160/320 = 50%.
# 3 Setores (despesas; renda R$ 3.000): aluguel 108° = 3 · 36° = 30% → R$ 900.
# 4 Histograma (espera em minutos, 50 pessoas): [0,10) 18 · [10,20) 15 · [20,30) 12 · [30,40) 5. 20 ou mais: 17 = 34%.
# 5 Dupla entrada (aprovação): manhã 45 aprovados de 60 = 75%; noite 72 de 120 = 60%. Mais aprovados: noite; maior porcentagem: manhã.

TITULO = "Praticando: dados, tabelas e gráficos"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações com tabelas e gráficos, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}a tabela de frequência, [p=0.2] {b}os gráficos de barras, de linhas e de setores, [p=0.2] {c}o histograma [p=0.2] e {d}a tabela de dupla entrada. [p=0.3] Em quase todas, {e}porcentagem: a parte dividida pelo total. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: barras
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] O gráfico de barras mostra {b}o esporte preferido de cinquenta pessoas. [p=0.2] {c}Repare: cada linha da grade vale dois. [p=0.3] {d}Quantas pessoas preferem vôlei, e quantos por cento isso é?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] A barra do vôlei chega na {a}sexta linha. [p=0.2] Quem conta só as linhas diz seis pessoas. [p=0.2] Mas {b}seis linhas de dois dá doze. [p=0.3] Agora o atalho da porcentagem: {c}faça o total virar cem. [p=0.2] Cinquenta vezes dois dá cem, então {d}doze vezes dois dá vinte e quatro. [p=0.2] {e}Vinte e quatro por cento."),
    # situação 2: linhas e variação
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] O gráfico de linhas mostra {b}o público de um cinema, de janeiro a maio. [p=0.2] {c}Janeiro, trezentas pessoas. [p=0.2] Fevereiro, trezentas e sessenta. [p=0.2] Março, trezentas e vinte. [p=0.2] Abril, quatrocentas e oitenta. [p=0.2] Maio, quinhentas. [p=0.3] {d}Em que período houve a maior alta, e de quantos por cento?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] As subidas: {a}de janeiro para fevereiro, mais sessenta. [p=0.2] {b}De fevereiro para março, a linha desce. [p=0.2] {c}De março para abril, mais cento e sessenta. [p=0.2] {d}De abril para maio, mais vinte. [p=0.3] {e}Maior alta: de março para abril, o trecho mais em pé. [p=0.2] Maio tem o maior público, {f}mas não a maior alta."),
    dict(id="s09", block="resposta2", text="Em porcentagem, {a}a diferença dividida pelo valor de antes. [p=0.2] {b}Cento e sessenta dividido por trezentos e vinte dá zero vírgula cinco, [p=0.2] que são {c}cinquenta por cento de alta. [p=0.2] Faz sentido: cento e sessenta é a metade de trezentos e vinte."),
    # situação 3: setores
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Um gráfico de setores mostra {b}as despesas de uma família, que gasta três mil reais por mês. [p=0.2] {c}A fatia do aluguel tem cento e oito graus. [p=0.3] {d}Quantos reais vão para o aluguel?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] Use o atalho dos setores: {a}dez por cento vale trinta e seis graus. [p=0.2] Cento e oito é {b}três vezes trinta e seis, [p=0.2] então dá trinta por cento. [p=0.3] Agora, trinta por cento de três mil. [p=0.2] {c}Dez por cento dá trezentos. [p=0.2] {d}Vezes três dá novecentos reais. [p=0.3] Pela conta direta, chega no mesmo: {e}cento e oito dividido por trezentos e sessenta dá zero vírgula três."),
    # situação 4: histograma
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] Um histograma mostra {b}quantos minutos cinquenta pessoas esperaram numa fila. [p=0.2] {c}Dezoito pessoas esperaram de zero a dez minutos. [p=0.2] Quinze esperaram de dez a vinte. [p=0.2] Doze esperaram de vinte a trinta. [p=0.2] E cinco esperaram de trinta a quarenta. [p=0.3] {d}Quantos por cento esperaram vinte minutos ou mais?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] Na borda, o primeiro número entra: {a}quem esperou vinte minutos está na coluna de vinte a trinta. [p=0.2] Então são {b}duas colunas: doze mais cinco dá dezessete pessoas. [p=0.3] Total cinquenta: {c}faça o total virar cem. [p=0.2] {d}Dezessete vezes dois dá trinta e quatro por cento."),
    # situação 5: dupla entrada
    dict(id="s16", block="questao5", text="{a}Última situação. [p=0.2] Uma tabela de dupla entrada mostra {b}os aprovados de um curso, por turno. [p=0.2] {c}De manhã, quarenta e cinco aprovados em sessenta alunos. [p=0.2] {d}À noite, setenta e dois aprovados em cento e vinte. [p=0.3] {e}Qual turno teve a maior porcentagem de aprovação?"),
    dict(id="s17", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta5", text="Vamos lá. [p=0.2] Cada turno tem o seu cem por cento. [p=0.2] {a}Manhã: quarenta e cinco sessenta avos. [p=0.2] Dividindo em cima e embaixo por quinze, {b}dá três quartos, [p=0.2] que são setenta e cinco por cento. [p=0.3] {c}Noite: setenta e dois dividido por cento e vinte dá zero vírgula seis, [p=0.2] que são {d}sessenta por cento."),
    dict(id="s19", block="resposta5", text="Resposta: {a}a manhã. [p=0.2] E aqui está a armadilha. [p=0.2] A noite tem {b}mais aprovados, setenta e dois contra quarenta e cinco. [p=0.2] Mas a pergunta pede {c}porcentagem, e aí a manhã ganha. [p=0.2] Leia o fim do enunciado de novo antes de responder."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}leia título, eixos e legenda antes dos números, [p=0.2] {b}ache o cem por cento de cada pergunta [p=0.2] e {c}confira se ela pede quantidade ou porcentagem."),
    dict(id="s21", block="fim", text="Na próxima aula, começa uma parte nova: {a}a média aritmética. [p=0.2] Você vai calcular a média de três notas [p=0.2] e {b}descobrir a nota que falta para fechar média sete. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
