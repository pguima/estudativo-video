# Estudativo · MAT-EST-005 — Histograma (Matemática · Estatística · Dados, tabelas e gráficos).
# Habilidade: ler um histograma, dizer quantas pessoas estão numa faixa e diferenciá-lo de um gráfico de barras.
# Pré-requisitos: MAT-EST-002 (classes; "o primeiro entra e o último não"; idades das 20 pessoas), MAT-EST-003 (ler gráfico de barras: título, eixos, topo da barra). Próxima: MAT-EST-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula; dados do tempo de deslocamento inventados e ditos como "da questão".
# Dados: idades (EST-002): [10,20) 2 · [20,30) 7 · [30,40) 7 · [40,50) 3 · [50,60) 1 → total 20.
#   De 20 a 40: 7 + 7 = 14. Menos de 30: 2 + 7 = 9. 30 ou mais: 20 − 9 = 11 (= 7 + 3 + 1).
#   Questão (minutos, 40 funcionários): [0,15) 6 · [15,30) 14 · [30,45) 12 · [45,60) 8. De 15 a 45: 26. 30 ou mais: 20 = 50%.

TITULO = "Histograma: como ler e como não confundir"

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
    dict(id="s01", block="gancho", text="{a}Este gráfico parece um gráfico de barras. [p=0.2] Mas repare: {b}as colunas estão coladas, [p=0.2] e embaixo {c}não há nomes, só números. [p=0.3] É um {d}histograma, e ele se lê de outro jeito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê um histograma, diz quantas pessoas estão numa faixa [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a tabela de frequência com classes, como as idades de dez em dez anos, [p=0.2] e {c}a leitura de um gráfico de barras: título, eixos e o topo da barra. [p=0.3] Se faltar alguma, procure no canal."),
    # da tabela ao histograma
    dict(id="s04", block="tabela", text="Lembra das idades das vinte pessoas? [p=0.2] Na tabela, elas ficaram em classes. [p=0.2] {a}Duas pessoas na classe de dez a vinte anos. [p=0.2] {b}Sete na de vinte a trinta. [p=0.2] {c}Sete na de trinta a quarenta. [p=0.2] {d}Três na de quarenta a cinquenta. [p=0.2] {e}E uma na de cinquenta a sessenta."),
    dict(id="s05", block="histograma", text="O histograma desenha essa tabela. [p=0.2] {a}Cada classe vira uma coluna. [p=0.2] {b}A largura da coluna é a faixa de idade. [p=0.2] {c}A altura é a frequência: quantas pessoas estão naquela faixa."),
    dict(id="s06", block="histograma", text="O eixo de baixo é {a}uma reta numérica, com as bordas das classes: [p=0.2] dez [p=0.2] vinte [p=0.2] trinta, e assim por diante. [p=0.3] Onde uma classe termina, {b}a próxima começa. [p=0.2] Por isso {c}as colunas ficam coladas."),
    # ler uma faixa
    dict(id="s07", block="faixa", text="Quantas pessoas têm {a}de vinte anos até menos de quarenta? [p=0.2] Essa faixa pega {b}duas colunas: [p=0.2] {c}sete mais sete dá catorze pessoas. [p=0.3] E com menos de trinta anos? [p=0.2] {d}Duas mais sete dá nove."),
    dict(id="s08", block="faixa", text="Na borda, vale a regra da tabela: {a}o primeiro número entra e o último não. [p=0.2] {b}Quem tem trinta anos está na coluna de trinta a quarenta."),
    # barras x histograma
    dict(id="s09", block="diferenca", text="E qual é a diferença para o gráfico de barras? [p=0.2] No de barras, {a}cada barra é uma categoria, como ônibus ou carro. [p=0.2] A variável é qualitativa. [p=0.2] As barras ficam {b}separadas, e dá para trocar a ordem delas sem mudar nada."),
    dict(id="s10", block="diferenca", text="No histograma, {a}a variável é quantitativa, agrupada em classes. [p=0.2] {b}A ordem é a da reta numérica, e não muda. [p=0.2] E {c}não há espaço entre as colunas, porque não há buraco entre as faixas."),
    # erro
    dict(id="s11", block="erro", text="Agora, um erro muito comum: {a}tratar a coluna como uma idade só. [p=0.2] Pergunta: {b}quantas pessoas têm vinte e cinco anos? [p=0.2] A pessoa olha a coluna de vinte a trinta e responde {c}sete."),
    dict(id="s12", block="erro", text="Mas sete é {a}a faixa inteira, de vinte até vinte e nove anos. [p=0.2] Na lista das idades, {b}só uma pessoa tinha vinte e cinco. [p=0.3] O histograma mostra {c}faixas, não idades soltas. [p=0.2] Só com ele, {d}essa pergunta não tem resposta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}conte o lado menor e tire do total. [p=0.2] Quantas pessoas têm trinta anos ou mais? [p=0.2] Dá para somar as três colunas da direita. [p=0.2] Mas à esquerda há menos colunas: [p=0.2] {b}duas pessoas mais sete dá nove. [p=0.2] {c}Vinte menos nove dá onze."),
    dict(id="s14", block="atalho", text="Funciona porque {a}todas as colunas juntas somam o total. [p=0.2] O que não está de um lado está do outro. [p=0.3] {b}Não compensa quando o lado pedido já é o menor: [p=0.2] aí, some direto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] O histograma, criado para esta questão, mostra {a}quantos minutos quarenta funcionários levam até o trabalho. [p=0.3] {b}Seis pessoas levam de zero a quinze minutos. [p=0.2] {c}Catorze levam de quinze a trinta. [p=0.2] {d}Doze levam de trinta a quarenta e cinco. [p=0.2] {e}E oito levam de quarenta e cinco a sessenta."),
    dict(id="s16", block="questao", text="{a}Quantos levam de quinze minutos até menos de quarenta e cinco? [p=0.2] {b}Quantos por cento levam trinta minutos ou mais? [p=0.2] E {c}dá para saber quantos levam exatamente vinte minutos?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] De quinze até menos de quarenta e cinco são {a}duas colunas: [p=0.2] {b}catorze mais doze dá vinte e seis funcionários."),
    dict(id="s19", block="resposta", text="Trinta minutos ou mais: {a}doze mais oito dá vinte. [p=0.2] Pelo atalho, sai igual: {b}quarenta menos seis menos catorze dá vinte. [p=0.2] {c}Vinte de quarenta é a metade, que dá cinquenta por cento."),
    dict(id="s20", block="resposta", text="E {a}exatamente vinte minutos não dá para saber. [p=0.2] O histograma só diz que {b}catorze pessoas estão na faixa de quinze a trinta."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}no histograma, cada coluna é uma faixa, [p=0.2] {b}a altura conta quantos estão nela, [p=0.2] e {c}as colunas ficam coladas porque as faixas se encostam."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai {a}cruzar linha e coluna numa tabela, [p=0.2] {b}usar a legenda de cores de um mapa [p=0.2] e {c}tirar o dado certo de um infográfico. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
