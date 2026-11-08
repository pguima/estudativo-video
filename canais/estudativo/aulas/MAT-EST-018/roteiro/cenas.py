# Estudativo · MAT-EST-018 — Praticando: médias, mediana, moda e dispersão (Matemática · Estatística · Mediana, moda e dispersão · prática).
# Habilidade: calcular cada medida, escolher a mais adequada e comparar grupos pela regularidade.
# Pré-requisitos: MAT-EST-008 a MAT-EST-017. Próxima: MAT-EST-019.
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Telas: s03 tempos (min) 10 · 15 · 15 · 15 · 20 · 25 · 30 · 35 · 105 · s11 boxplot da bateria (h): mín. 8, Q1 12, mediana 15, Q3 18, máx. 26
#        s14 vendas por dia: Carla 8 · 10 · 10 · 12 · Dora 4 · 10 · 10 · 16 · s19 loja A média 200, DP 30 · loja B média 50, DP 10.

TITULO = "Praticando: médias, mediana, moda e dispersão"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, criadas para esta aula, com todas as medidas do módulo. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}três grupos de ferramentas: [p=0.2] {b}as médias, inclusive com pesos; [p=0.2] {c}mediana, moda, quartis e boxplot; [p=0.2] e {d}desvio padrão e coeficiente de variação. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: média, mediana e moda; qual usar
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] {b}Na tela, o tempo que nove pessoas levam até o trabalho, em minutos. [p=0.3] {c}Calcule a média, a mediana e a moda. [p=0.2] {d}Qual delas representa melhor o tempo típico desse grupo?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}A soma dá duzentos e setenta. [p=0.2] {b}Duzentos e setenta dividido por nove dá trinta minutos de média. [p=0.3] A lista já está em ordem. [p=0.2] Com nove dados, {c}nove mais um dá dez, e dez dividido por dois dá cinco. [p=0.2] {d}O quinto valor é vinte: essa é a mediana. [p=0.3] {e}A moda é quinze, que aparece três vezes."),
    dict(id="s06", block="resposta1", text="A média ficou {a}bem acima da mediana. [p=0.2] Sinal de um valor muito alto puxando: [p=0.2] {b}a pessoa que leva cento e cinco minutos. [p=0.3] {c}Sete das nove pessoas levam trinta minutos ou menos. [p=0.2] O tempo típico é {d}a mediana: vinte minutos."),
    # situação 2: média ponderada e valor que falta
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Num concurso, a nota final é uma média com pesos: [p=0.2] {b}prova objetiva com peso três [p=0.2] e {c}discursiva com peso dois. [p=0.3] Um candidato tirou {d}seis na objetiva. [p=0.2] {e}Quanto ele precisa tirar na discursiva para fechar média sete?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] O total é a média vezes a soma dos pesos. [p=0.2] {a}Os pesos somam cinco. [p=0.2] {b}Sete vezes cinco dá trinta e cinco. [p=0.3] A objetiva já rendeu {c}seis vezes três, que dá dezoito. [p=0.2] Faltam {d}trinta e cinco menos dezoito, que dá dezessete. [p=0.2] A discursiva tem peso dois: {e}dezessete dividido por dois dá oito vírgula cinco."),
    dict(id="s10", block="resposta2", text="Pelo atalho das sobras e faltas: [p=0.2] {a}o seis fica um abaixo do sete, com peso três. [p=0.2] {b}Faltam três. [p=0.3] A discursiva cobre isso com peso dois: [p=0.2] {c}três dividido por dois dá um vírgula cinco acima do sete. [p=0.2] {d}Sete mais um vírgula cinco dá oito vírgula cinco. [p=0.2] Bateu."),
    # situação 3: boxplot
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] {b}O boxplot mostra quantas horas dura a bateria de um modelo de celular, em vários testes. [p=0.3] {c}Item um: qual é a amplitude? [p=0.2] {d}Item dois: qual é a largura da caixa? [p=0.2] {e}Item três: em quantos por cento dos testes a bateria durou doze horas ou mais?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Amplitude é o maior menos o menor: {a}vinte e seis menos oito dá dezoito horas. [p=0.2] Um número só. [p=0.3] A caixa vai do primeiro ao terceiro quartil: {b}dezoito menos doze dá seis horas. [p=0.3] E doze é o primeiro quartil. [p=0.2] Acima dele ficam {c}três pedaços do desenho: [p=0.2] {d}cerca de setenta e cinco por cento dos testes."),
    # situação 4: desvio padrão e regularidade com a mesma média
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Na tela, as vendas por dia de Carla e de Dora, em quatro dias. [p=0.3] {c}Calcule a média e o desvio padrão de cada uma. [p=0.2] {d}Quem é mais regular?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}As vendas de Carla somam quarenta. [p=0.2] {b}As de Dora também. [p=0.2] {c}Quarenta dividido por quatro dá dez: a mesma média. [p=0.3] Os desvios de Carla são {d}menos dois [p=0.2] zero [p=0.2] zero e dois. [p=0.2] {e}Os quadrados somam oito. [p=0.2] {f}Oito dividido por quatro dá dois de variância."),
    dict(id="s17", block="resposta4", text="Os desvios de Dora são {a}menos seis [p=0.2] zero [p=0.2] zero e seis. [p=0.2] {b}Os quadrados somam setenta e dois. [p=0.2] {c}Setenta e dois dividido por quatro dá dezoito de variância. [p=0.3] Com a mesma média, {d}nem precisa tirar a raiz: [p=0.2] {e}Carla é mais regular."),
    dict(id="s18", block="resposta4", text="Se a prova pedir o desvio padrão, cerque: [p=0.2] {a}a raiz de dois dá cerca de um vírgula quatro. [p=0.2] {b}A raiz de dezoito dá cerca de quatro vírgula dois. [p=0.3] {c}Um vírgula quatro ao quadrado dá um vírgula noventa e seis. [p=0.2] {d}Quatro vírgula dois ao quadrado dá dezessete vírgula sessenta e quatro. [p=0.2] Bem perto."),
    # situação 5: coeficiente de variação
    dict(id="s19", block="questao5", text="{a}Última situação. [p=0.2] {b}A loja á vende, em média, duzentas peças por dia, com desvio padrão de trinta. [p=0.3] {c}A loja bê vende, em média, cinquenta, com desvio padrão de dez. [p=0.3] {d}Qual tem vendas mais regulares?"),
    dict(id="s20", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta5", text="Vamos lá. [p=0.2] As médias são diferentes: {a}coeficiente de variação. [p=0.3] {b}Trinta dividido por duzentos dá zero vírgula quinze: [p=0.2] quinze por cento. [p=0.3] {c}Dez dividido por cinquenta dá zero vírgula dois: [p=0.2] vinte por cento. [p=0.3] {d}A loja á é mais regular, [p=0.2] mesmo com o desvio padrão maior. [p=0.2] Quem comparou trinta com dez {e}caiu na armadilha."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: [p=0.2] {a}valor extremo, prefira a mediana; [p=0.2] {b}valor que falta, use o total; [p=0.2] {c}mesma média, compare o desvio padrão; [p=0.2] {d}médias diferentes, o coeficiente de variação."),
    dict(id="s23", block="fim", text="Na próxima aula, você aprende a {a}desconfiar de gráficos: [p=0.2] {b}eixo que não começa no zero, [p=0.2] {c}escala irregular [p=0.2] e {d}figura fora de proporção. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
