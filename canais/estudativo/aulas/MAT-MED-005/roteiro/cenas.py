# Estudativo · MAT-MED-005 — Converter volume e litros (Matemática · Medidas e Unidades).
# Habilidade: explicar o que é 1 m³, ver que uma caixa de 3 m por 2 m por 1 m cabe em 6 cubinhos de 1 m³, transformar 2 m³ em dm³ e dizer que uma caixa de 2 m³ guarda 2.000 L.
# Pré-requisitos: MAT-MED-002 (litro e mililitro), MAT-MED-004 (área). Próxima: MAT-MED-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Fórmula do volume do bloco é de MAT-ESP-005: aqui só se contam cubinhos.

TITULO = "Converter volume e litros"

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
    dict(id="s01", block="gancho", text="Uma caixa-d'água de {a}dois metros cúbicos. [p=0.3] Quantos litros cabem nela? [p=0.3] Se você pensou {b}dois litros, [p=0.2] a caixa ficou do tamanho de {c}uma garrafa de refrigerante. [p=0.3] A resposta é {d}dois mil litros."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender o que é volume, [p=0.2] converter metros cúbicos em litros [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}na área, cada degrau vale cem, porque são duas direções, [p=0.2] e {c}um litro tem mil mililitros. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é volume
    dict(id="s04", block="volume", text="A área cobre um piso. [p=0.2] {a}O volume enche um espaço: [p=0.2] uma caixa, uma piscina, um quarto inteiro. [p=0.3] Medir volume é contar {b}quantos cubinhos iguais enchem esse espaço."),
    dict(id="s05", block="volume", text="O cubinho padrão é o {a}metro cúbico: [p=0.2] {b}um cubo com um metro de comprimento, um de largura e um de altura. [p=0.3] Ele se escreve com {c}um três pequeno no alto do eme, [p=0.2] o mesmo do ao cubo."),
    dict(id="s06", block="volume", text="Uma caixa mede {a}três metros por dois metros, com um metro de altura. [p=0.2] No fundo, cabem {b}três cubinhos por fileira, em duas fileiras: [p=0.2] {c}seis cubinhos. [p=0.3] A altura é um metro, então é {d}uma camada só. [p=0.2] O volume é {e}seis metros cúbicos."),
    dict(id="s07", block="volume", text="Se a mesma caixa tivesse {a}dois metros de altura, [p=0.2] seriam {b}duas camadas de seis: [p=0.2] {c}doze metros cúbicos."),
    # metro cúbico em decímetro cúbico
    dict(id="s08", block="dm3", text="Agora, metro cúbico em {a}decímetro cúbico. [p=0.2] O decímetro é a décima parte do metro: {b}dez centímetros. [p=0.3] Então o metro cúbico tem {c}dez cubinhos de comprimento, dez de largura e dez de altura."),
    dict(id="s09", block="dm3", text="{a}Dez vezes dez vezes dez: mil. [p=0.2] {b}Um metro cúbico tem mil decímetros cúbicos. [p=0.3] No volume, cada degrau vale {c}dez ao cubo, mil: [p=0.2] {d}três casas da vírgula."),
    dict(id="s10", block="dm3", text="{a}Dois metros cúbicos em decímetros cúbicos: [p=0.2] três casas para a direita. [p=0.2] {b}Dois mil decímetros cúbicos."),
    # a ponte com o litro
    dict(id="s11", block="litro", text="E aqui está a ponte para o litro: [p=0.2] {a}um decímetro cúbico é exatamente um litro. [p=0.3] {b}Um cubo de dez centímetros de lado, cheio de água, guarda um litro."),
    dict(id="s12", block="litro", text="Então {a}um metro cúbico guarda mil litros. [p=0.3] E a caixa-d'água do começo: {b}dois metros cúbicos são dois mil decímetros cúbicos, [p=0.2] ou seja, {c}dois mil litros. [p=0.3] É por isso que a conta de água mede o consumo em {d}metros cúbicos: [p=0.2] cada um são mil litros."),
    dict(id="s13", block="litro", text="E o caminho de volta: uma caixa de {a}quinhentos litros. [p=0.2] São quinhentos decímetros cúbicos. [p=0.2] Para o metro cúbico, {b}três casas para a esquerda: [p=0.2] {c}zero vírgula cinco metro cúbico."),
    dict(id="s14", block="litro", text="Descendo mais um degrau: {a}um decímetro cúbico tem mil centímetros cúbicos, [p=0.2] e um litro tem mil mililitros. [p=0.3] Então {b}um centímetro cúbico é um mililitro. [p=0.3] Uma seringa de {c}cinco mililitros guarda {d}cinco centímetros cúbicos."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro comum: {a}usar a regra da área no volume. [p=0.2] A pessoa anda duas casas e escreve {b}dois metros cúbicos igual a duzentos decímetros cúbicos. [p=0.3] Mas o volume tem {c}três direções: [p=0.2] comprimento, largura e altura. [p=0.2] Cada degrau vale {d}mil, não cem. [p=0.2] Duzentos decímetros cúbicos seriam só {e}duzentos litros."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}de metro cúbico para litro, vezes mil. [p=0.3] {b}Cinco metros cúbicos: cinco mil litros. [p=0.2] {c}Zero vírgula três metro cúbico: trezentos litros."),
    dict(id="s17", block="atalho", text="Funciona porque {a}um metro cúbico são mil decímetros cúbicos, e cada um é um litro. [p=0.3] {b}Não compensa com centímetro cúbico: [p=0.2] aí, lembre que {c}centímetro cúbico é mililitro."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Um reservatório tem {a}três vírgula cinco metros cúbicos. [p=0.2] {b}Quantos litros ele guarda? [p=0.3] E uma lata tem {c}novecentos centímetros cúbicos. [p=0.2] {d}Quantos litros cabem nela?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] De metro cúbico para litro, {a}três casas para a direita. [p=0.2] {b}Três mil e quinhentos litros. [p=0.2] São três caixas de mil litros, e mais meia."),
    dict(id="s21", block="resposta", text="Na lata, centímetro cúbico é mililitro: {a}novecentos mililitros. [p=0.2] Para chegar ao litro, {b}três casas para a esquerda. [p=0.2] {c}Zero vírgula nove litro. [p=0.2] Quase um litro: faz sentido para uma lata grande."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}no volume, cada degrau vale mil, [p=0.2] e {b}um decímetro cúbico é um litro."),
    dict(id="s23", block="fim", text="Na próxima aula, a unidade que {a}não anda de dez em dez: o tempo. [p=0.3] Você vai ler {b}duas vírgula duas horas sem cair na armadilha dos minutos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
