# Estudativo · MAT-EST-017 — Interpretar a dispersão (Matemática · Estatística · Mediana, moda e dispersão).
# Habilidade: dizer qual atleta é mais regular comparando desvios padrão e usar o coeficiente de variação quando as médias são diferentes.
# Pré-requisitos: MAT-EST-016 (desvio padrão = raiz da variância, na unidade dos dados), MAT-POR-003 (quantos por cento: parte dividida pelo total). Próxima: MAT-EST-018.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Atletas e dados criados para esta aula.
# Tela s05: saltos (m) Ana 5,8 · 6,2 · 6,2 · 5,8 (média 6, variância 0,04, DP 0,2); Bia 5,3 · 6,7 · 5,9 · 6,1 (média 6, variância 0,25, DP 0,5).

TITULO = "Interpretar a dispersão: desvio padrão e coeficiente de variação"

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
    dict(id="s01", block="gancho", text="{a}Nos tempos de um corredor de cem metros, o desvio padrão é de zero vírgula seis segundo. [p=0.3] {b}Nos de um corredor de quatrocentos metros, é de um segundo inteiro. [p=0.3] Quem é mais regular? [p=0.2] Quase todo mundo diz {c}o de cem metros. [p=0.3] {d}É o de quatrocentos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê o desvio padrão, [p=0.2] compara grupos com médias diferentes [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}o desvio padrão, a raiz da variância, que fica na mesma unidade dos dados, [p=0.2] e {c}quantos por cento uma parte é do total, dividindo a parte pelo total. [p=0.3] Se faltar alguma, procure no canal."),
    # ler o desvio padrão
    dict(id="s04", block="ler", text="O que o desvio padrão diz? [p=0.2] {a}O quanto os valores costumam se afastar da média. [p=0.3] {b}Desvio padrão pequeno: valores perto da média, grupo homogêneo, atleta regular. [p=0.2] {c}Desvio padrão grande: valores espalhados, grupo heterogêneo, atleta irregular."),
    dict(id="s05", block="saltos", text="Veja duas atletas de salto em distância. [p=0.2] {a}Os saltos de cada uma estão na tela. [p=0.3] {b}Ana e Bia têm a mesma média: seis metros. [p=0.2] {c}O desvio padrão de Ana é zero vírgula dois metro. [p=0.2] {d}O de Bia é zero vírgula cinco."),
    dict(id="s06", block="saltos", text="Com a mesma média, a comparação é direta: [p=0.2] {a}Ana é mais regular, porque o desvio padrão dela é menor. [p=0.3] Se o técnico precisa de um salto seguro, {b}leva a Ana. [p=0.3] Repare: {c}regular não quer dizer melhor. [p=0.2] Quem salta mais longe é assunto da média. [p=0.2] {d}Regularidade é assunto do desvio padrão."),
    # médias diferentes
    dict(id="s07", block="cv", text="E quando as médias são diferentes? [p=0.2] Volte aos corredores. [p=0.2] {a}O de cem metros faz, em média, doze segundos, [p=0.2] com desvio padrão de zero vírgula seis. [p=0.3] {b}O de quatrocentos faz, em média, cinquenta segundos, [p=0.2] com desvio padrão de um segundo."),
    dict(id="s08", block="cv", text="Um segundo pesa pouco numa prova de cinquenta segundos. [p=0.2] Zero vírgula seis pesa mais numa prova de doze. [p=0.3] Para comparar, pergunte: [p=0.2] {a}o desvio padrão é quantos por cento da média? [p=0.2] Esse número se chama {b}coeficiente de variação."),
    dict(id="s09", block="cv", text="A conta é a de sempre: {a}parte dividida pelo total. [p=0.2] Aqui, {b}desvio padrão dividido pela média. [p=0.3] {c}Zero vírgula seis dividido por doze dá zero vírgula zero cinco: [p=0.2] cinco por cento. [p=0.3] {d}Um dividido por cinquenta dá zero vírgula zero dois: [p=0.2] dois por cento."),
    dict(id="s10", block="cv", text="{a}Menor coeficiente de variação, mais regular. [p=0.2] {b}O corredor de quatrocentos metros varia só dois por cento [p=0.2] do próprio tempo. [p=0.3] O coeficiente {c}não tem unidade, [p=0.2] porque segundo dividido por segundo se cancela. [p=0.2] Por isso, ele compara até {d}coisas medidas em unidades diferentes."),
    # erro
    dict(id="s11", block="erro", text="O erro do começo é {a}comparar os desvios padrão com médias diferentes. [p=0.3] Zero vírgula seis é menor que um, [p=0.2] e a pessoa {b}escolhe o corredor de cem metros. [p=0.3] Mas o desvio padrão é medido em segundos, [p=0.2] e {c}uma prova dura doze segundos, a outra dura cinquenta. [p=0.2] Antes de comparar, {d}divida cada um pela sua média."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: [p=0.2] com a mesma média, {a}compare as variâncias direto, sem tirar a raiz. [p=0.3] Ana e Bia: variância de {b}zero vírgula zero quatro [p=0.2] contra {c}zero vírgula vinte e cinco: [p=0.2] {d}a menor é a do grupo mais regular."),
    dict(id="s13", block="atalho", text="Funciona porque {a}número maior tem raiz maior: [p=0.2] a ordem não muda. [p=0.3] Não compensa quando {b}as médias são diferentes. [p=0.2] Aí, você precisa do desvio padrão [p=0.2] para {c}dividir pela média."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Item um: dois arremessadores têm a mesma média. [p=0.2] As variâncias estão na tela: {b}zero vírgula sessenta e quatro para o primeiro [p=0.2] e zero vírgula vinte e cinco para o segundo. [p=0.2] {c}Qual é mais regular?"),
    dict(id="s15", block="questao", text="{a}Item dois: um ciclista faz, em média, quarenta minutos num percurso, [p=0.2] com desvio padrão de dois minutos. [p=0.2] {b}Outro faz, em média, oitenta minutos noutro percurso, [p=0.2] com desvio padrão de dois vírgula quatro. [p=0.3] {c}Qual é mais regular?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] No item um, as médias são iguais. [p=0.2] {a}Zero vírgula vinte e cinco é a menor variância, [p=0.2] então {b}o segundo arremessador é mais regular. [p=0.3] Se quiser conferir, {c}as raízes dão zero vírgula oito [p=0.2] e zero vírgula cinco."),
    dict(id="s18", block="resposta", text="No item dois, as médias são diferentes: {a}coeficiente de variação. [p=0.2] {b}Dois dividido por quarenta dá zero vírgula zero cinco: [p=0.2] cinco por cento. [p=0.3] {c}Dois vírgula quatro dividido por oitenta dá zero vírgula zero três: [p=0.2] três por cento. [p=0.3] {d}O segundo ciclista é mais regular, [p=0.2] mesmo com desvio padrão maior."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.2] {a}com médias iguais, menor desvio padrão é mais regular. [p=0.2] {b}Com médias diferentes, divida o desvio padrão pela média [p=0.2] e compare os coeficientes de variação."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}você pratica tudo do módulo: [p=0.2] {b}calcular cada medida, [p=0.2] {c}escolher a mais adequada [p=0.2] e {d}comparar grupos pela regularidade. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
