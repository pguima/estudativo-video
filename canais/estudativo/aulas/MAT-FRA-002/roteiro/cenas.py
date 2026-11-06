# Estudativo · MAT-FRA-002 — Fração de uma quantidade: a parte e o total (Matemática · Frações e Decimais).
# Habilidade: calcular 3/4 de 20 e descobrir o salário inteiro sabendo que 2/5 dele são R$ 600.
# Pré-requisitos: MAT-FRA-001, MAT-NUM-007. Próxima: MAT-FRA-003.
# Simplificação ainda não foi ensinada (MAT-FRA-003): nenhuma conta precisa dela.

TITULO = "Fração de uma quantidade: a parte e o total"

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
    dict(id="s01", block="gancho", text="{a}Dois quintos do seu salário são {b}seiscentos reais. [p=0.3] Qual é o salário? [p=0.3] Se a sua resposta foi {c}duzentos e quarenta reais, [p=0.2] tem algo muito errado: o salário inteiro ficou menor que um pedaço dele."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}calcular a fração de qualquer quantidade, [p=0.2] {b}fazer o caminho de volta, da parte para o total, [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}saber o que é uma fração, [p=0.2] com o de baixo dizendo em quantas partes o inteiro foi dividido, [p=0.2] e {c}multiplicar por um algarismo. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # a barra
    dict(id="s04", block="barra", text="Pegue {a}uma barra de chocolate com {b}vinte quadradinhos. [p=0.3] Quanto é {c}três quartos dela?"),
    dict(id="s05", block="barra", text="O de baixo é quatro, então {a}corte a barra em quatro partes iguais. [p=0.3] Vinte dividido por quatro: {b}cada parte tem cinco quadradinhos."),
    dict(id="s06", block="barra", text="O de cima é três, então {a}pegue três partes. [p=0.2] Três vezes cinco: {b}quinze quadradinhos. [p=0.3] {c}Três quartos de vinte é quinze."),
    # regra
    dict(id="s07", block="regra", text="Toda fração de uma quantidade segue esta frase: {a}divide pelo de baixo, [p=0.2] {b}multiplica pelo de cima. [p=0.3] Dividir acha o tamanho de {c}uma parte. [p=0.2] Multiplicar junta {d}as partes que você quer."),
    dict(id="s08", block="regra", text="Com dinheiro é igual. [p=0.2] Uma conta de {a}trezentos reais, e você pagou {b}dois quintos dela. [p=0.3] Trezentos dividido por cinco, {c}sessenta. [p=0.2] Sessenta vezes dois, {d}cento e vinte reais."),
    # caminho de volta
    dict(id="s09", block="volta", text="Voltando à pergunta do começo. [p=0.2] Aqui você {a}não tem o total. [p=0.2] Você tem {b}a parte: dois quintos do salário são seiscentos reais."),
    dict(id="s10", block="volta", text="Desenhe o salário como {a}uma barra cortada em cinco partes iguais. [p=0.2] {b}Duas partes, juntas, valem seiscentos. [p=0.3] Então {c}uma parte vale seiscentos dividido por dois: {d}trezentos reais."),
    dict(id="s11", block="volta", text="Um quinto são trezentos, e o salário inteiro são {a}cinco partes. [p=0.2] Cinco vezes trezentos: {b}mil e quinhentos reais."),
    dict(id="s12", block="volta", text="Repare: a conta virou do avesso. [p=0.2] {a}Divide pelo de cima, [p=0.2] {b}multiplica pelo de baixo. [p=0.3] E dá para conferir: {c}mil e quinhentos dividido por cinco, trezentos. [p=0.2] {d}Vezes dois, seiscentos. [p=0.2] Bateu."),
    # qual caminho
    dict(id="s13", block="escolha", text="Como saber qual caminho usar? [p=0.2] Pergunte: {a}o número que eu tenho é o total ou a parte? [p=0.3] {b}Tem o total, divide pelo de baixo. [p=0.2] {c}Tem a parte, divide pelo de cima."),
    dict(id="s14", block="escolha", text="Veja a diferença em frases parecidas. [p=0.2] {a}Três quartos de oitenta balas: [p=0.2] oitenta é o total. [p=0.2] Oitenta dividido por quatro, vinte. [p=0.2] Vezes três, {b}sessenta. [p=0.3] {c}Três quartos do pacote são sessenta balas: [p=0.2] sessenta é a parte. [p=0.2] Sessenta dividido por três, vinte. [p=0.2] Vezes quatro, {d}oitenta."),
    # erro
    dict(id="s15", block="erro", text="O erro do começo é pular essa pergunta. [p=0.2] A pessoa vê a fração e usa o caminho do total: {a}seiscentos dividido por cinco, [p=0.2] {b}vezes dois, [p=0.2] {c}duzentos e quarenta."),
    dict(id="s16", block="erro", text="Mas seiscentos é {a}só uma parte do salário. [p=0.2] O salário não pode ser {b}menor que a parte. [p=0.3] Olhe sempre o tamanho da resposta: {c}o total é maior que a parte."),
    # atalho
    dict(id="s17", block="atalho", text="E o atalho prometido: {a}tire o pedaço que falta. [p=0.3] Vale quando a fração é quase o inteiro, como {b}quatro quintos de quatrocentos."),
    dict(id="s18", block="atalho", text="Ache só um quinto: {a}oitenta. [p=0.3] Quatro quintos é tudo, menos um quinto. [p=0.2] {b}Quatrocentos menos oitenta: {c}trezentos e vinte. [p=0.3] Nos vinte quadradinhos, é a mesma coisa: {d}vinte menos cinco, quinze."),
    dict(id="s19", block="atalho", text="Funciona porque {a}falta só uma parte para completar o inteiro, [p=0.2] e subtrair é mais rápido que multiplicar. [p=0.3] Não compensa quando falta muito, como em {b}dois nonos: [p=0.2] aí, {c}divida e multiplique normalmente."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Um tanque de combustível está com {a}três quartos da capacidade, [p=0.2] o que dá {b}trinta e seis litros. [p=0.3] {c}Quantos litros cabem no tanque cheio?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] Trinta e seis litros é {a}a parte, então divide pelo de cima: {b}trinta e seis dividido por três, doze. [p=0.2] Cada parte tem doze litros. [p=0.3] O tanque tem quatro partes: {c}doze vezes quatro, {d}quarenta e oito litros. [p=0.3] Maior que a parte: faz sentido."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}tem o total, divide pelo de baixo e multiplica pelo de cima. [p=0.2] {b}Tem a parte, divide pelo de cima e multiplica pelo de baixo."),
    dict(id="s24", block="fim", text="Na próxima aula, você vai ver que {a}um meio, dois quartos e três sextos são a mesma quantidade, [p=0.2] e como {b}simplificar uma fração. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
