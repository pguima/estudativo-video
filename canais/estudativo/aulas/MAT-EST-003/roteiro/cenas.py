# Estudativo · MAT-EST-003 — Gráficos de barras e de linhas (Matemática · Estatística · Dados, tabelas e gráficos).
# Habilidade: ler um gráfico de barras ou de linhas, dizer o período de maior alta e calcular uma variação percentual.
# Pré-requisitos: MAT-EST-002 (tabela de frequência; dados do transporte), MAT-POR-005 (variação = diferença dividida pelo valor de antes). Próxima: MAT-EST-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Eixo que não começa no zero fica para MAT-EST-019 (gráficos que enganam).
# Dados: barras do transporte (EST-002): ônibus 8, carro 5, bicicleta 4, a pé 3; eixo de 0 a 10, linhas da grade de 2 em 2.
#   Erro: ônibus na 4ª linha; 4 · 2 = 8.
#   Linha (vendas, unidades): jan 40, fev 50, mar 80, abr 100, mai 90. Subidas +10, +30, +20; queda −10.
#   Maior alta fev → mar: 30/50 = 0,6 = 60%. Queda abr → mai: 10/100 = 10%.
#   Questão (visitantes): jun 200, jul 250, ago 450, set 360, out 500. +50, +200, −90, +140. Maior alta jul → ago: 200/250 = 0,8 = 80%.
# Visual:
#   s01, s08-s12: E.serie com os cinco meses; s10 cada subida marcada com o valor; s01 e s10: ponto de abril em destaque e trecho fev → mar na cor da matéria.
#   s04-s07: E.colunas do transporte com título, eixo de baixo (categorias) e eixo do lado (pessoas); s06 linha tracejada do topo da barra até o eixo.
#   s13: grade de 2 em 2: contagem de linhas errada (4, vermelho) e certa (8, verde).
#   s14-s15: palco escuro com o trecho mais inclinado em destaque; contraexemplo com anos pulados no eixo de baixo.
#   s16-s19: E.serie dos visitantes (jun a out).

TITULO = "Gráficos de barras e de linhas"

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
    dict(id="s01", block="gancho", text="{a}As vendas de uma loja, mês a mês, num gráfico de linhas. [p=0.2] Em que período as vendas {b}mais subiram? [p=0.3] Muita gente aponta {c}abril, o ponto mais alto. [p=0.3] Mas a maior alta foi {d}de fevereiro para março."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê gráficos de barras e de linhas, [p=0.2] acha a maior alta, calcula a variação em porcentagem [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a tabela de frequência [p=0.2] e {c}a variação percentual: a diferença dividida pelo valor de antes. [p=0.3] Se faltar alguma, procure no canal."),
    # barras
    dict(id="s04", block="barras", text="Comece pelas barras. [p=0.2] Lembra das vinte pessoas e do jeito de ir ao trabalho? [p=0.2] {a}Cada resposta vira uma barra. [p=0.2] {b}A altura da barra é a frequência."),
    dict(id="s05", block="barras", text="Antes de ler, olhe {a}três coisas: [p=0.2] {b}o título, que diz do que é o gráfico; [p=0.2] {c}o eixo de baixo, com as categorias; [p=0.2] e {d}o eixo do lado, com os valores e a unidade."),
    dict(id="s06", block="barras", text="Agora, veja {a}onde o topo da barra encontra o eixo do lado. [p=0.2] {b}Ônibus chega no oito. [p=0.2] {c}Carro, no cinco. [p=0.3] Quantas pessoas a mais vão de ônibus que de carro? [p=0.2] {d}Oito menos cinco dá três."),
    # linhas
    dict(id="s07", block="linhas", text="O gráfico de linhas serve para {a}o que muda com o tempo. [p=0.2] {b}Os meses ficam no eixo de baixo, [p=0.2] {c}cada ponto é o valor daquele mês, [p=0.2] e a linha liga os pontos {d}em ordem."),
    dict(id="s08", block="linhas", text="As vendas da loja, em unidades: [p=0.2] {a}janeiro, quarenta. [p=0.2] {b}Fevereiro, cinquenta. [p=0.2] {c}Março, oitenta. [p=0.2] {d}Abril, cem. [p=0.2] {e}Maio, noventa."),
    dict(id="s09", block="alta", text="Alta é a subida {a}de um ponto para o seguinte. [p=0.2] Calcule cada uma: [p=0.2] {b}cinquenta menos quarenta dá dez. [p=0.2] {c}Oitenta menos cinquenta dá trinta. [p=0.2] {d}Cem menos oitenta dá vinte. [p=0.2] E de abril para maio, {e}a linha desce dez."),
    dict(id="s10", block="alta", text="{a}A maior alta é de fevereiro para março. [p=0.2] Abril tem o maior valor, [p=0.2] mas {b}subiu menos para chegar lá."),
    dict(id="s11", block="variacao", text="E quanto foi essa alta, em porcentagem? [p=0.2] {a}A diferença dividida pelo valor de antes. [p=0.3] {b}Trinta dividido por cinquenta dá zero vírgula seis, [p=0.2] que são {c}sessenta por cento de alta."),
    dict(id="s12", block="variacao", text="Na queda, a conta é a mesma: [p=0.2] {a}de cem para noventa, caiu dez. [p=0.2] {b}Dez dividido por cem dá zero vírgula um, [p=0.2] que são {c}dez por cento de queda."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}contar as linhas da grade sem ler o eixo. [p=0.2] No gráfico de barras, {b}cada linha vale dois. [p=0.2] A barra do ônibus chega na {c}quarta linha. [p=0.2] Quem conta linha por linha diz {d}quatro pessoas. [p=0.3] Mas {e}quatro linhas de dois dá oito."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}procure o trecho mais em pé. [p=0.3] {b}Quanto mais inclinada a subida, maior a alta. [p=0.2] De fevereiro para março, {c}a linha quase dispara. [p=0.2] Você acha o período {d}sem fazer conta."),
    dict(id="s15", block="atalho", text="Funciona porque {a}os meses estão igualmente espaçados: [p=0.2] no mesmo passo para o lado, {b}quem sobe mais fica mais em pé. [p=0.3] {c}Não compensa quando o espaço entre os pontos muda, [p=0.2] como em {d}anos pulados no eixo, [p=0.2] ou quando duas subidas parecem iguais. [p=0.2] Aí, {e}calcule as diferenças."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}O gráfico mostra os visitantes de um museu, de junho a outubro. [p=0.2] {b}Junho, duzentos. [p=0.2] Julho, duzentos e cinquenta. [p=0.2] Agosto, quatrocentos e cinquenta. [p=0.2] Setembro, trezentos e sessenta. [p=0.2] Outubro, quinhentos. [p=0.3] {c}Em que período houve a maior alta? [p=0.2] {d}E de quantos por cento foi essa alta?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] As subidas: {a}de junho para julho, duzentos e cinquenta menos duzentos dá cinquenta. [p=0.2] {b}De julho para agosto, quatrocentos e cinquenta menos duzentos e cinquenta dá duzentos. [p=0.2] {c}De agosto para setembro, a linha desce. [p=0.2] {d}De setembro para outubro, quinhentos menos trezentos e sessenta dá cento e quarenta. [p=0.3] {e}Maior alta: de julho para agosto, o trecho mais em pé. [p=0.2] Outubro tem {f}o maior valor, mas não a maior alta."),
    dict(id="s19", block="resposta", text="Em porcentagem: {a}duzentos dividido por duzentos e cinquenta dá zero vírgula oito, [p=0.2] que são {b}oitenta por cento de alta."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}leia título, eixos e unidade antes dos números. [p=0.2] E {b}a maior alta é a maior subida entre dois pontos seguidos, não o ponto mais alto."),
    dict(id="s21", block="fim", text="Na próxima aula, {a}o gráfico de setores, a famosa pizza. [p=0.2] Você vai passar de porcentagem para ângulo e de volta: [p=0.2] {b}vinte e cinco por cento viram noventa graus. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
