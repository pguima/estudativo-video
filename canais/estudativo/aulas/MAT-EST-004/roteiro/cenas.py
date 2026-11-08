# Estudativo · MAT-EST-004 — Gráfico de setores (Matemática · Estatística · Dados, tabelas e gráficos).
# Habilidade: passar de porcentagem para ângulo e de volta: 25% viram 90° e 72° viram 20%.
# Pré-requisitos: MAT-ANG-001 (volta = 360°; canto da folha = 90°), MAT-EST-002 (frequência relativa; dados do transporte), MAT-RAZ-006 (regra de três e "cruz"). Próxima: MAT-EST-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula; dados da pesquisa de frutas inventados e ditos como "da questão".
# Dados: transporte de 20 pessoas (EST-002): ônibus 8 = 40% → 144°; carro 5 = 25% → 90°; bicicleta 4 = 20% → 72°; a pé 3 = 15% → 54°. Soma 360°.
#   Erro: 8 pessoas lidas como 8% → 8% de 360 = 28,8°.
#   Atalho: 10% = 36°. Questão: 200 pessoas; banana 30% → 108°; maçã 54° → 15% → 30 pessoas.

TITULO = "Gráfico de setores: porcentagem e ângulo"

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
    dict(id="s01", block="gancho", text="{a}Num gráfico de pizza, uma fatia vale {b}vinte e cinco por cento. [p=0.3] Quantos graus tem essa fatia? [p=0.3] Se você pensou {c}vinte e cinco graus, [p=0.2] olhe o tamanho: seria uma fatia fininha. [p=0.3] A resposta é {d}noventa graus, o canto da folha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você passa de porcentagem para ângulo e de ângulo para porcentagem, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}uma volta inteira tem trezentos e sessenta graus, [p=0.2] {c}a frequência relativa, que diz quanto cada resposta é do total, em porcentagem, [p=0.2] e {d}a regra de três. [p=0.3] Se faltar alguma, procure no canal."),
    # o gráfico
    dict(id="s04", block="setores", text="O gráfico de pizza tem um nome oficial: {a}gráfico de setores. [p=0.2] {b}O círculo inteiro é o total da pesquisa, cem por cento. [p=0.2] {c}Cada fatia é um setor, e mostra uma resposta. [p=0.2] {d}Quanto maior a parte, maior a fatia."),
    dict(id="s05", block="setores", text="Lembra das {a}vinte pessoas que responderam como vão ao trabalho? [p=0.2] Na tabela de frequência, {b}ônibus ficou com quarenta por cento. [p=0.2] {c}Carro, vinte e cinco. [p=0.2] {d}Bicicleta, vinte. [p=0.2] {e}A pé, quinze."),
    # porcentagem para ângulo
    dict(id="s06", block="angulo", text="Para desenhar cada fatia, você precisa do {a}ângulo no centro do círculo. [p=0.3] A ideia é uma só: {b}cem por cento é a volta inteira, trezentos e sessenta graus. [p=0.2] Então {c}o ângulo da fatia é a mesma porcentagem de trezentos e sessenta."),
    dict(id="s07", block="angulo", text="{a}Carro, com vinte e cinco por cento, é um quarto da pizza. [p=0.2] {b}Trezentos e sessenta dividido por quatro dá noventa graus. [p=0.2] Um quarto de volta: {c}o canto da folha."),
    dict(id="s08", block="regra3", text="E o ônibus, com quarenta por cento? [p=0.2] Monte a regra de três: {a}por cento de um lado, graus do outro. [p=0.2] {b}Cem por cento com trezentos e sessenta graus. [p=0.2] {c}Quarenta por cento com xis. [p=0.3] Cruz: {d}cem xis igual a quarenta vezes trezentos e sessenta, que dá catorze mil e quatrocentos. [p=0.2] Divida por cem: {e}xis igual a cento e quarenta e quatro graus."),
    dict(id="s09", block="regra3", text="Pela mesma conta, {a}a bicicleta fica com setenta e dois graus [p=0.2] e {b}quem vai a pé, com cinquenta e quatro. [p=0.3] Confira: {c}somando os quatro ângulos, dá trezentos e sessenta. [p=0.2] A pizza fecha."),
    # ângulo para porcentagem
    dict(id="s10", block="volta", text="Agora, o caminho de volta. [p=0.2] Uma fatia tem {a}setenta e dois graus. [p=0.2] Quantos por cento ela é? [p=0.3] É a conta de sempre: {b}a parte dividida pelo total. [p=0.2] A parte é setenta e dois. [p=0.2] O total é {c}a volta inteira, trezentos e sessenta."),
    dict(id="s11", block="volta", text="Fica {a}setenta e dois trezentos e sessenta avos. [p=0.2] Setenta e dois cabe cinco vezes em trezentos e sessenta, então {b}divida em cima e embaixo por setenta e dois. [p=0.2] Dá um quinto. [p=0.2] {c}Um quinto vale vinte por cento. [p=0.3] Com vinte pessoas na pesquisa, {d}vinte por cento de vinte dá quatro pessoas: a bicicleta."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com um erro muito comum: {a}usar o número de pessoas como se fosse porcentagem. [p=0.2] Oito pessoas vão de ônibus. [p=0.2] A pessoa calcula {b}oito por cento de trezentos e sessenta [p=0.2] e desenha uma fatia de {c}vinte e oito vírgula oito graus. [p=0.3] Fininha demais para oito pessoas em vinte."),
    dict(id="s13", block="erro", text="Oito é {a}a frequência absoluta, em pessoas. [p=0.2] Primeiro, a relativa: {b}oito dividido por vinte dá zero vírgula quatro, [p=0.2] que são quarenta por cento. [p=0.2] Só então o ângulo: {c}cento e quarenta e quatro graus."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}dez por cento vale trinta e seis graus. [p=0.2] É trezentos e sessenta dividido por dez. [p=0.3] {b}Vinte por cento: duas vezes trinta e seis dá setenta e dois. [p=0.2] {c}Quarenta por cento: quatro vezes trinta e seis dá cento e quarenta e quatro. [p=0.2] {d}Quinze por cento: trinta e seis mais a metade dele, que é dezoito. [p=0.2] Dá cinquenta e quatro."),
    dict(id="s15", block="atalho", text="Na volta, {a}conte quantos trinta e seis cabem no ângulo. [p=0.2] Setenta e dois é {b}duas vezes trinta e seis, [p=0.2] então dá vinte por cento. [p=0.3] Funciona porque {c}dez por cento é um décimo da volta. [p=0.2] {d}Não compensa com porcentagem quebrada, como trinta e sete por cento. [p=0.2] Aí, {e}vá de regra de três."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Numa pesquisa criada para esta questão, {a}duzentas pessoas disseram a fruta preferida. [p=0.3] {b}A fatia da banana tem trinta por cento. [p=0.2] Quantos graus ela tem? [p=0.3] {c}A fatia da maçã tem cinquenta e quatro graus. [p=0.2] Quantos por cento ela é, [p=0.2] e {d}quantas pessoas escolheram maçã?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Banana: trinta por cento são {a}três vezes dez por cento. [p=0.2] {b}Três vezes trinta e seis dá cento e oito graus."),
    dict(id="s19", block="resposta", text="Maçã: {a}cinquenta e quatro dividido por trezentos e sessenta dá zero vírgula quinze, [p=0.2] que são {b}quinze por cento. [p=0.2] Pelo atalho, é trinta e seis mais dezoito: dez por cento mais cinco por cento. [p=0.3] Agora, as pessoas. [p=0.2] {c}Dez por cento de duzentas dá vinte. [p=0.2] Cinco por cento é a metade, que dá dez. [p=0.2] {d}Vinte mais dez dá trinta pessoas."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a pizza inteira é cem por cento e trezentos e sessenta graus. [p=0.2] {b}Da porcentagem para o ângulo, tire a porcentagem de trezentos e sessenta. [p=0.2] {c}Do ângulo para a porcentagem, divida por trezentos e sessenta."),
    dict(id="s21", block="fim", text="Na próxima aula, as idades agrupadas em classes viram um gráfico: {a}o histograma. [p=0.2] Você vai ler {b}quantas pessoas estão numa faixa [p=0.2] e ver {c}por que ele não é um gráfico de barras. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
