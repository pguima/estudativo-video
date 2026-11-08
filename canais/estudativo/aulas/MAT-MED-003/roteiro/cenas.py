# Estudativo · MAT-MED-003 — Prefixos e unidades fora do sistema métrico (Matemática · Medidas e Unidades).
# Habilidade: escrever 2 GB em bytes usando potências de 10 e converter 50 polegadas em cm com o fator do enunciado.
# Pré-requisitos: MAT-MED-002 (massa e capacidade), MAT-POT-012 (notação científica). Próxima: MAT-MED-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Só conversões por multiplicação: dividir por decimal não está na cadeia.

TITULO = "Prefixos e unidades fora do sistema métrico"

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
    dict(id="s01", block="gancho", text="Seu celular tem {a}dois gigabytes livres. [p=0.3] Quantos bytes são isso? [p=0.3] Escrito por inteiro, o número tem {b}nove zeros. [p=0.2] Com potência de dez, {c}cabe em uma linha curta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar os prefixos gigantes e minúsculos, [p=0.2] converter {b}polegadas em centímetros [p=0.2] e ainda leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a escada das unidades, com quilo valendo mil, [p=0.2] e {c}a notação científica, com expoente negativo para números pequenos. [p=0.3] Se faltar alguma, procure no canal."),
    # prefixos grandes
    dict(id="s04", block="grandes", text="Primeiro, o que é {a}byte: [p=0.2] é a unidade que mede {b}o tamanho de um arquivo. [p=0.3] Uma letra de um texto simples ocupa {c}cerca de um byte."),
    dict(id="s05", block="grandes", text="Você já conhece o {a}quilo: mil, dez elevado a três. [p=0.3] Acima dele vem o {b}mega: um milhão, [p=0.2] dez elevado a seis. [p=0.3] E o {c}giga: um bilhão, [p=0.2] dez elevado a nove. [p=0.3] Uma foto de {d}três megabytes tem três vezes dez elevado a seis bytes: [p=0.2] {e}três milhões."),
    dict(id="s06", block="grandes", text="Então {a}dois gigabytes são dois vezes dez elevado a nove bytes. [p=0.3] {b}Dois bilhões de bytes. [p=0.3] E já está na notação científica: {c}a frente é dois, e a frente vai de um até menos de dez."),
    dict(id="s07", block="grandes", text="Em informática, às vezes o enunciado avisa que {a}cada prefixo vale mil e vinte e quatro vezes o anterior, em vez de mil. [p=0.2] Se avisar, {b}use o valor do enunciado."),
    # prefixos pequenos
    dict(id="s08", block="pequenos", text="Para baixo, o {a}mili você já conhece: [p=0.2] milésimo, dez elevado a menos três. [p=0.3] Depois vem o {b}micro: milionésimo, [p=0.2] dez elevado a menos seis. [p=0.3] E o {c}nano: bilionésimo, [p=0.2] dez elevado a menos nove."),
    dict(id="s09", block="pequenos", text="O vírus da gripe mede cerca de {a}cem nanômetros. [p=0.2] Em metros: {b}cem vezes dez elevado a menos nove. [p=0.3] Cem é dez ao quadrado. [p=0.2] Repete a base e soma os expoentes: [p=0.2] {c}dez elevado a menos sete metro."),
    # fora do sistema métrico
    dict(id="s10", block="fora", text="Agora, as unidades {a}fora do sistema métrico: [p=0.2] {b}polegada, pé, milha, libra. [p=0.3] Elas vieram de outros países e {c}não andam de dez em dez. [p=0.3] A boa notícia: a prova {d}dá o fator de conversão."),
    dict(id="s11", block="fora", text="Uma televisão de {a}cinquenta polegadas. [p=0.2] Esse número mede {b}a diagonal da tela, de um canto ao canto oposto. [p=0.3] O enunciado diz: {c}uma polegada vale dois vírgula cinquenta e quatro centímetros."),
    dict(id="s12", block="fora", text="Cada polegada vira dois vírgula cinquenta e quatro centímetros, [p=0.2] então {a}multiplique: cinquenta vezes dois vírgula cinquenta e quatro. [p=0.3] Cinquenta é metade de cem. [p=0.2] {b}Vezes cem: duzentos e cinquenta e quatro. [p=0.2] {c}Metade: cento e vinte e sete. [p=0.3] A diagonal tem {d}cento e vinte e sete centímetros."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}dividir pelo fator. [p=0.2] Cinquenta dividido por dois vírgula cinquenta e quatro dá {b}quase vinte. [p=0.3] Uma televisão de vinte centímetros? [p=0.3] {c}O centímetro é menor que a polegada, então o número tem que crescer."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho dos prefixos: {a}eles andam de três em três no expoente. [p=0.3] {b}Quilo, três. [p=0.1] Mega, seis. [p=0.1] Giga, nove. [p=0.3] {c}Mili, menos três. [p=0.1] Micro, menos seis. [p=0.1] Nano, menos nove."),
    dict(id="s15", block="atalho", text="Funciona porque {a}cada prefixo vale mil vezes o anterior, [p=0.2] e mil é dez elevado a três. [p=0.3] {b}Não compensa com centi e deci, que ficam fora dessa sequência: [p=0.2] para eles, volte à escada."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um pendrive tem {a}sessenta e quatro gigabytes. [p=0.2] {b}Escreva em bytes, na notação científica. [p=0.3] E uma corrida tem {c}cinco milhas. [p=0.2] O enunciado diz que {d}uma milha vale um vírgula seis quilômetro. [p=0.2] {e}Quantos quilômetros tem a corrida?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Giga é dez elevado a nove: {a}sessenta e quatro vezes dez elevado a nove. [p=0.3] Sessenta e quatro passa de dez, então {b}a vírgula anda uma casa para a esquerda [p=0.2] e {c}o expoente sobe um. [p=0.3] {d}Seis vírgula quatro vezes dez elevado a dez bytes."),
    dict(id="s19", block="resposta", text="Na corrida, cada milha vira um vírgula seis quilômetro: {a}multiplique. [p=0.2] Sem a vírgula, {b}cinco vezes dezesseis dá oitenta. [p=0.2] Uma casa: {c}oito quilômetros. [p=0.3] Quilômetro é menor que milha, e o número {d}cresceu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}os prefixos andam de três em três no expoente, [p=0.2] e {b}fora do sistema métrico, use o fator do enunciado, [p=0.2] conferindo se o número deve crescer ou diminuir."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai ver {a}o que é um metro quadrado [p=0.2] e por que, na área, {b}cada degrau da escada vale cem. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
