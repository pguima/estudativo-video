# Estudativo · MAT-NUM-002 — Ler e comparar números grandes (Matemática · Números e Contas).
# Habilidade: ler em voz alta 2.048.500 e dizer qual é maior entre 1.099 e 1.101, usando os sinais > e <.
# Pré-requisitos: MAT-NUM-001. Próxima: MAT-NUM-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Contas: 2.048.500 = 2 milhões, 48 mil e 500 · 1.101 > 1.099 · 1.000.000 ÷ 1.000 = 1.000 meses ≈ 83 anos · 1.000.010 > 990.000.
# Questão: 1.040.705 > 1.040.698 (erro de olhar o fim: 98 contra 5 inverteria a resposta).

TITULO = "Ler e comparar números grandes"

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
    dict(id="s01", block="gancho", text="Olhe {a}este prêmio. [p=0.3] Você lê de primeira, em voz alta? [p=0.3] Muita gente {b}trava e sai contando casa com o dedo."),
    dict(id="s02", block="gancho", text="E entre {a}estes dois preços, qual é o maior? [p=0.3] Aqui, muita gente {b}erra por olhar para o lugar errado."),
    dict(id="s03", block="gancho", text="{a}Até o fim desta aula, você lê qualquer número desse tamanho e compara sem erro, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s04", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] o algarismo vale pelo lugar onde está: [p=0.2] {b}unidade, [p=0.2] {c}dezena [p=0.2] e {d}centena. [p=0.3] Se faltar, procure a aula no canal."),
    # grupos
    dict(id="s05", block="grupos", text="Depois da centena, vêm mais casas. [p=0.2] {a}Dez notas de cem fazem mil reais: [p=0.2] essa casa é o {b}milhar, [p=0.2] um grupo de mil. [p=0.3] E {c}mil grupos de mil fazem um {d}milhão. [p=0.3] Guardando mil reais por mês, [p=0.2] você levaria {e}mais de oitenta anos para juntar um milhão."),
    dict(id="s06", block="grupos", text="Para não se perder, a gente separa o número em {a}grupos de três algarismos, [p=0.2] {b}da direita para a esquerda. [p=0.3] {c}Os pontos fazem essa separação. [p=0.2] Por isso eles aparecem em preço e em salário."),
    dict(id="s07", block="grupos", text="Cada ponto tem um nome. [p=0.2] Contando da direita, o {a}primeiro ponto é mil. [p=0.2] O {b}segundo ponto é milhão. [p=0.3] E dentro de cada grupo, {c}as casas se repetem: [p=0.2] centena, dezena, unidade. [p=0.3] Você só lê um grupo de cada vez."),
    # leitura
    dict(id="s08", block="leitura", text="Vamos ler o prêmio. [p=0.2] Os pontos se contam da direita, [p=0.2] mas a leitura começa pela esquerda. [p=0.3] {a}O primeiro grupo é o dois, [p=0.2] e o ponto logo depois dele é o de milhão: [p=0.2] {b}dois milhões."),
    dict(id="s09", block="leitura", text="O grupo seguinte {a}começa com zero: [p=0.2] centena vazia, que não se fala. [p=0.2] Sobra {b}quarenta e oito, [p=0.2] e o ponto depois dele é o de mil: [p=0.2] {c}quarenta e oito mil."),
    dict(id="s10", block="leitura", text="O último grupo {a}não tem ponto depois, então não ganha nome: [p=0.2] {b}quinhentos. [p=0.3] Junte tudo: [p=0.2] {c}dois milhões, [p=0.2] quarenta e oito mil e quinhentos."),
    # comparar
    dict(id="s11", block="comparar", text="Para comparar números sem vírgula, a primeira pergunta é: [p=0.2] {a}quem tem mais algarismos? [p=0.3] Esse é o maior. [p=0.2] {b}Mil tem quatro algarismos. [p=0.2] {c}Novecentos e noventa e nove tem três. [p=0.3] Com vírgula, a conversa é outra, e fica para outra aula."),
    dict(id="s12", block="comparar", text="Deu empate? [p=0.2] Compare {a}casa por casa, da esquerda para a direita. [p=0.2] {b}A primeira casa diferente decide."),
    dict(id="s13", block="comparar", text="{a}Mil e noventa e nove contra {b}mil cento e um. [p=0.3] Quatro algarismos em cada: empate. [p=0.2] Casa do milhar: {c}um contra um, empate. [p=0.2] Casa da centena: {d}zero contra um. [p=0.3] Decidido: {e}mil cento e um é maior."),
    dict(id="s14", block="comparar", text="Por que a esquerda manda? [p=0.2] Mil cento e um tem {a}uma nota de cem depois do mil. [p=0.2] Mil e noventa e nove não tem nenhuma, [p=0.2] só {b}noventa e nove reais depois do mil, [p=0.2] e isso não chega a cem. [p=0.3] {c}Uma nota só na casa da esquerda vale mais que tudo o que vem depois dela."),
    # sinais
    dict(id="s15", block="sinais", text="Isso se escreve com {a}dois sinais. [p=0.2] Este é o {b}maior que. [p=0.2] Este é o {c}menor que. [p=0.3] Para não trocar: [p=0.2] {d}a abertura fica virada para o número maior, [p=0.2] e {e}a ponta para o menor."),
    dict(id="s16", block="sinais", text="{a}Mil cento e um é maior que mil e noventa e nove. [p=0.3] Trocando os números de lado, o sinal vira: [p=0.2] {b}mil e noventa e nove é menor que mil cento e um. [p=0.3] {c}É a mesma informação."),
    # erro
    dict(id="s17", block="erro", text="O erro mais comum é {a}olhar o fim do número. [p=0.2] A pessoa vê {b}noventa e nove contra um [p=0.2] e escolhe mil e noventa e nove como o maior. [p=0.3] Só que o fim é a parte que {c}menos vale. [p=0.2] É como comparar dois valores olhando só as moedas e {d}ignorando as notas."),
    # atalho
    dict(id="s18", block="atalho", text="Agora o atalho: {a}conte os pontos primeiro. [p=0.2] {b}Mais pontos, número maior. [p=0.3] {c}Novecentos e noventa mil tem um ponto. [p=0.2] {d}Um milhão e dez tem dois pontos, [p=0.2] e o grupo só de zeros não se fala. [p=0.2] {e}Decidido, sem ler mais nada."),
    dict(id="s19", block="atalho", text="Funciona porque cada ponto é {a}um grupo de casas a mais. [p=0.3] {b}Não compensa quando a quantidade de pontos é igual: [p=0.2] aí, {c}volte para a comparação casa por casa."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Dois apartamentos estão à venda, [p=0.2] {a}um por este preço [p=0.2] e {b}outro por este. [p=0.3] {c}Leia cada preço em voz alta. [p=0.2] Depois, {d}escreva qual é maior, usando o sinal."),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] Primeiro preço: {a}um milhão, [p=0.2] quarenta mil, [p=0.2] seiscentos e noventa e oito reais. [p=0.3] Segundo preço: {b}um milhão, [p=0.2] quarenta mil, [p=0.2] setecentos e cinco reais."),
    dict(id="s23", block="resposta", text="Mesma quantidade de algarismos. [p=0.2] Da esquerda para a direita, {a}tudo empata até a casa da centena: [p=0.2] {b}seis contra sete. [p=0.3] O sete decide, mesmo com o fim menor: [p=0.2] {c}o segundo preço é maior que o primeiro."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}grupos de três para ler, [p=0.2] e {b}esquerda primeiro para comparar."),
    dict(id="s25", block="fim", text="Na próxima aula, começam as contas: [p=0.2] {a}somar de cabeça completando dez [p=0.2] e {b}armar a conta com o vai um. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
