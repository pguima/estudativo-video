# Estudativo · MAT-FRA-021 — Praticando: números decimais (Matemática · Frações e Decimais · prática).
# Habilidade: fazer contas com decimais e trocar entre fração e decimal em problemas de dinheiro e medida.
# Pré-requisitos: MAT-FRA-014, MAT-FRA-015, MAT-FRA-016, MAT-FRA-017, MAT-FRA-018, MAT-FRA-019, MAT-FRA-020. Próxima: nenhuma (fim da trilha).
# Questões inéditas, criadas para esta aula. Última aula da trilha Frações e Decimais.

TITULO = "Praticando: números decimais"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações de dinheiro e de medida, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] É assim que os números decimais ficam de vez na cabeça."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}somar e subtrair alinhando a vírgula, [p=0.2] {b}multiplicar e dividir, [p=0.2] {c}trocar fração por decimal [p=0.2] e {d}reconhecer dízima. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: somar e subtrair
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] No mercado, você levou {b}pão por três reais e setenta e cinco centavos [p=0.1] e {c}carne por doze reais e noventa centavos. [p=0.3] Pagou com {d}uma nota de vinte reais. [p=0.3] {e}Qual é o troco?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Primeiro, o total, com {a}vírgula embaixo de vírgula: [p=0.2] {b}dezesseis reais e sessenta e cinco centavos. [p=0.3] Depois, o troco. [p=0.2] Escreva {c}a nota como vinte vírgula zero zero, [p=0.2] para as casas baterem, e subtraia. [p=0.3] Troco: {d}três reais e trinta e cinco centavos."),
    # situação 2: dividir por decimal e comparar
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] O mesmo arroz vem em pacotes diferentes. [p=0.2] O pacote A tem {b}dois quilos e meio e custa {c}catorze reais. [p=0.2] O pacote B tem {d}um quilo e meio e custa {e}oito reais e setenta centavos. [p=0.3] {f}Em qual pacote o quilo sai mais barato?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] O preço do quilo é {a}o preço dividido pelos quilos. [p=0.3] Pacote A: {b}catorze dividido por dois vírgula cinco. [p=0.2] O divisor tem uma casa, então ande uma casa em cada número: [p=0.2] {c}cento e quarenta dividido por vinte e cinco. [p=0.2] Dá cinco, e sobram quinze. [p=0.2] Com um zero, cento e cinquenta, que dá seis. [p=0.2] {d}Cinco reais e sessenta centavos o quilo."),
    dict(id="s09", block="resposta2", text="Pacote B: {a}oito vírgula sete dividido por um vírgula cinco. [p=0.2] Virou {b}oitenta e sete dividido por quinze. [p=0.2] Dá cinco, e sobram doze. [p=0.2] Com um zero, cento e vinte, que dá oito. [p=0.2] {c}Cinco reais e oitenta centavos o quilo. [p=0.3] Resposta: {d}o pacote A. [p=0.3] Essa é a armadilha: o pacote B custa menos no caixa, [p=0.2] mas {e}o quilo dele é mais caro."),
    # situação 3: fração em decimal e multiplicar
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Uma costureira comprou {b}três quartos de metro de tecido. [p=0.2] O metro custa {c}dezesseis reais e quarenta centavos. [p=0.3] {d}Quanto ela pagou?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] Troque a fração por decimal: {a}três dividido por quatro dá zero vírgula setenta e cinco. [p=0.3] Multiplique: {b}dezesseis vírgula quatro vezes zero vírgula setenta e cinco. [p=0.3] Sem as vírgulas, {c}cento e sessenta e quatro vezes setenta e cinco dá doze mil e trezentos. [p=0.3] Uma casa mais duas casas: {d}três casas no resultado. [p=0.2] Ela pagou {e}doze reais e trinta centavos."),
    # atalho
    dict(id="s13", block="atalho", text="Aqui cabe um atalho: [p=0.2] três quartos de um preço é {a}dividir por quatro e multiplicar por três. [p=0.3] {b}Dezesseis reais e quarenta centavos dividido por quatro, quatro reais e dez centavos. [p=0.2] {c}Vezes três, doze reais e trinta centavos."),
    dict(id="s14", block="atalho", text="Funciona porque o quarto é {a}uma parte de quatro iguais, e você quer três delas. [p=0.3] Não compensa quando a divisão por quatro não fecha nos centavos, como em {b}dezessete reais e trinta centavos. [p=0.2] Aí, {c}multiplique pelo decimal."),
    # situação 4: dízima e arredondar
    dict(id="s15", block="questao4", text="{a}Situação quatro. [p=0.2] Três amigos vão dividir igualmente {b}uma conta de cinquenta reais. [p=0.3] {c}A parte de cada um é decimal exato ou dízima? [p=0.2] {d}E quanto cada um paga, arredondando para o centavo?"),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Vamos lá. [p=0.2] A parte de cada um é {a}cinquenta terços. [p=0.2] Não simplifica, e o denominador é {b}três: dízima. [p=0.3] Dividindo, {c}dezesseis vírgula seis, seis, seis... [p=0.2] {d}o período é seis."),
    dict(id="s18", block="resposta4", text="Para arredondar no centavo, olhe {a}a terceira casa. [p=0.2] É seis, que é cinco ou mais, então {b}a segunda casa sobe. [p=0.2] Cada um paga {c}dezesseis reais e sessenta e sete centavos. [p=0.3] Somando as três partes, dá {d}cinquenta reais e um centavo. [p=0.2] Esse centavo a mais é {e}a dízima aparecendo no bolso."),
    # situação 5: decimal em fração e andar com a vírgula
    dict(id="s19", block="questao5", text="{a}Última situação. [p=0.2] Uma pessoa caminha {b}zero vírgula oitenta e cinco quilômetro por dia. [p=0.3] {c}Que fração do quilômetro é essa, na forma mais simples? [p=0.2] {d}E quantos quilômetros ela caminha em cem dias?"),
    dict(id="s20", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta5", text="Vamos lá. [p=0.2] Duas casas: {a}oitenta e cinco centésimos. [p=0.2] Oitenta e cinco termina em cinco, cem termina em zero: {b}divida em cima e embaixo por cinco. [p=0.2] {c}Dezessete vinte avos do quilômetro."),
    dict(id="s22", block="resposta5", text="Em cem dias, {a}multiplique por cem: [p=0.2] {b}a vírgula anda duas casas para a direita. [p=0.2] {c}Oitenta e cinco quilômetros."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}vírgula alinhada para somar, [p=0.2] {b}casas contadas para multiplicar, [p=0.2] {c}divisor sem vírgula para dividir [p=0.2] e {d}resposta conferida no final."),
    dict(id="s24", block="fim", text="E com isso, {a}a trilha de frações e decimais terminou. [p=0.3] Você saiu de {b}o que é uma fração [p=0.2] e chegou até {c}prever uma dízima sem dividir. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
