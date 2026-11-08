# Estudativo · MAT-FIN-002 — Achar capital, taxa ou tempo (Matemática · Matemática Financeira).
# Habilidade: descobrir em quantos meses um capital dobra a 5% ao mês.
# Pré-requisitos: MAT-FIN-001 (juros simples), MAT-EQU-011 (isolar uma letra numa fórmula). Próxima: MAT-FIN-003.
# Questão inédita, criada para esta aula. Dividir por decimal (MAT-FRA-018) fora da ficha: o capital sai pelo caminho do um por cento.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Achar capital, taxa ou tempo nos juros simples"

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
    dict(id="s01", block="gancho", text="Um dinheiro aplicado a {a}cinco por cento ao mês, em juros simples. [p=0.3] Em quanto tempo ele {b}dobra? [p=0.3] Quem responde {c}quarenta meses errou pelo dobro. [p=0.2] São {d}vinte."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar o capital, a taxa ou o tempo, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a fórmula dos juros simples, jota igual a cê vezes i vezes tê, [p=0.2] e {c}isolar uma letra numa fórmula. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia
    dict(id="s04", block="ideia", text="Até agora, a pergunta era sempre {a}quanto de juros. [p=0.2] Só que a prova pode esconder {b}qualquer letra da fórmula. [p=0.3] A fórmula é a mesma. [p=0.2] Muda {c}qual letra você isola."),
    # tempo
    dict(id="s05", block="tempo", text="Comece pelo tempo. [p=0.2] Na fórmula, o tempo está {a}multiplicado por cê vezes i. [p=0.2] {b}Divida cada lado por cê vezes i. [p=0.3] Fica {c}tê igual a jota dividido por cê vezes i."),
    dict(id="s06", block="tempo", text="E cê vezes i tem um sentido: [p=0.2] capital vezes taxa {a}é o juro de um período, [p=0.1] um mês, se a taxa for ao mês. [p=0.3] Então o tempo é {b}o juro total dividido pelo juro de um período. [p=0.2] Quantos períodos de juros cabem no total."),
    # dobrar
    dict(id="s07", block="dobrar", text="Agora, {a}dobrar. [p=0.2] Cinco por cento ao mês é muito mais do que rende uma aplicação de verdade: [p=0.1] a taxa foi escolhida para a conta sair redonda. [p=0.2] Use um capital de {b}mil reais. [p=0.2] Dobrar é chegar a {c}dois mil de montante. [p=0.3] Montante é capital mais juros, então os juros precisam ser {d}mil reais: [p=0.1] o próprio capital."),
    dict(id="s08", block="dobrar", text="Juro de um mês: {a}cinco por cento de mil dá cinquenta reais. [p=0.3] Tempo: {b}mil dividido por cinquenta dá vinte meses. [p=0.3] Conferindo: {c}cinquenta por mês, em vinte meses, dá mil de juros. [p=0.2] Com o capital, {d}dois mil. [p=0.2] Dobrou."),
    dict(id="s09", block="dobrar", text="E o capital não importa. [p=0.2] Com {a}quinhentos reais, o juro de um mês é vinte e cinco, [p=0.2] e {b}quinhentos dividido por vinte e cinco também dá vinte. [p=0.3] Por isso, {c}a pergunta nem precisa dizer quanto foi aplicado."),
    # taxa
    dict(id="s10", block="taxa", text="Quando falta a taxa, {a}divida cada lado por cê vezes tê. [p=0.2] Fica {b}i igual a jota dividido por cê vezes tê. [p=0.3] Um empréstimo de mil reais cobrou {c}cento e vinte de juros em quatro meses. [p=0.2] {d}Mil vezes quatro dá quatro mil. [p=0.2] {e}Cento e vinte dividido por quatro mil dá zero vírgula zero três: [p=0.1] {f}três por cento ao mês."),
    # capital
    dict(id="s11", block="capital", text="Quando falta o capital, {a}pense em porcentagem do capital. [p=0.3] Um empréstimo a {b}dois por cento ao mês, por seis meses, [p=0.1] cobrou {c}noventa reais de juros. [p=0.2] Dois por cento em seis meses: {d}doze por cento do capital."),
    dict(id="s12", block="capital", text="Então {a}doze por cento do capital são noventa reais. [p=0.2] {b}Um por cento é noventa dividido por doze: sete vírgula cinco. [p=0.2] O capital é cem por cento: {c}setecentos e cinquenta reais."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum está no dobrar. [p=0.2] A pessoa pensa: dobrar é dois mil, então {a}os juros são dois mil. [p=0.2] Faz {b}dois mil dividido por cinquenta e acha {c}quarenta meses. [p=0.3] Mas dois mil é o {d}montante. [p=0.2] Os juros são só {e}o que veio a mais: mil reais."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}para dobrar em juros simples, divida cem pela taxa. [p=0.2] A resposta sai na unidade da taxa. [p=0.3] {b}Cem dividido por cinco dá vinte meses. [p=0.2] {c}A dez por cento ao mês, dez meses."),
    dict(id="s15", block="atalho", text="Funciona porque dobrar é ganhar {a}cem por cento de juros, [p=0.2] e {b}cada mês rende a taxa. [p=0.3] Não compensa quando a meta não é dobrar, como {c}render noventa reais. [p=0.2] Aí, {d}use a fórmula. [p=0.2] E {e}só vale para juros simples."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma dívida cresce a {a}quatro por cento ao mês, em juros simples. [p=0.3] {b}Em quantos meses ela triplica?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Use mil reais. [p=0.2] Triplicar é chegar a {a}três mil de montante. [p=0.2] Tirando o capital, os juros são {b}dois mil. [p=0.3] Juro de um mês: {c}quatro por cento de mil dá quarenta. [p=0.2] {d}Dois mil dividido por quarenta dá cinquenta meses."),
    dict(id="s19", block="resposta", text="Pela ideia do atalho: triplicar é ganhar {a}duzentos por cento de juros. [p=0.2] {b}Duzentos dividido por quatro dá cinquenta. [p=0.3] Quem dividiu trezentos por quatro achou {c}setenta e cinco, [p=0.1] e esqueceu de tirar o capital."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}é sempre a mesma fórmula, [p=0.2] {b}isole a letra que falta [p=0.2] e {c}separe montante de juros."),
    dict(id="s21", block="fim", text="Na próxima aula, juros simples no dia a dia: [p=0.2] {a}uma conta de duzentos reais paga com dez dias de atraso, [p=0.2] com {b}multa e juros por dia. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
