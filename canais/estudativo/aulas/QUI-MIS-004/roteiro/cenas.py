# Estudativo · QUI-MIS-004 — Curva de aquecimento: pura ou mistura (Química · Matéria e Misturas · Matéria, substâncias e estados físicos).
# Habilidade: achar os pontos de fusão e de ebulição numa curva de aquecimento e dizer pelos patamares se o material é
# substância pura, mistura comum, eutética ou azeotrópica.
# Pré-requisitos: QUI-MIS-002, QUI-MIS-003, MAT-EST-003, MAT-NUM-015. Próxima: QUI-MIS-005 (praticando).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: água pura ao nível do mar: PF 0 °C, PE 100 °C; água com sal começa a ferver acima de 100 °C e a temperatura sobe
# enquanto ferve; solda de estanho e chumbo (cerca de 63% e 37%) funde a 183 °C constantes (eutética); álcool 96%
# (etanol e água) ferve a cerca de 78 °C constantes (azeotrópica). Etimologia: eutético, do grego "que funde bem";
# azeótropo, "que não muda ao ferver". "°C" é lido "graus".

TITULO = "Curva de aquecimento: pura ou mistura"

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
    dict(id="s01", block="gancho", text="{a}Você põe gelo a vinte graus negativos no fogo e não desliga mais. [p=0.3] {b}O termômetro sobe, sobe [p=0.1] e, {c}no zero, trava. [p=0.3] Fica parado por minutos, com o fogo aceso. [p=0.3] {d}Para onde vai esse calor?"),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai ler {b}uma curva de aquecimento, [p=0.2] {c}achar nela os pontos de fusão e de ebulição [p=0.2] e {d}descobrir, só pelo desenho, se o material é puro ou é mistura."),
    # lembrete
    dict(id="s03", block="lembrete", text="Três lembretes rápidos. [p=0.2] {a}Substância pura tem um tipo só de partícula; mistura tem mais de um. [p=0.3] {b}Fusão é de sólido para líquido; ebulição é a vaporização com bolhas, e as duas absorvem calor. [p=0.3] {c}E no gráfico de linhas, cada ponto junta dois valores: um no eixo de baixo e outro no eixo do lado."),
    # curva da água
    dict(id="s04", block="curva", text="{a}Esta é a curva de aquecimento da água pura. [p=0.2] {b}No eixo de baixo, o tempo de fogo. [p=0.2] {c}No eixo do lado, a temperatura, em graus."),
    dict(id="s05", block="curva", text="{a}O gelo começa a vinte graus negativos e esquenta: a linha sobe. [p=0.3] {b}No zero, a linha deita. [p=0.2] Esse trecho deitado se chama {c}patamar. [p=0.3] É o gelo derretendo: {d}sólido e líquido juntos, e a temperatura parada."),
    dict(id="s06", block="curva", text="{a}Quando o último pedaço derrete, a água líquida esquenta e a linha volta a subir. [p=0.3] {b}No cem, um novo patamar: a água fervendo. [p=0.3] {c}Depois, só vapor, que segue esquentando."),
    dict(id="s07", block="curva", text="E o calor do patamar? [p=0.2] {a}Ele não some. [p=0.2] {b}É usado para soltar as partículas umas das outras, e não para agitá-las mais. [p=0.3] {c}Por isso a temperatura fica parada até a mudança de estado terminar."),
    dict(id="s08", block="curva", text="A temperatura do primeiro patamar é {a}o ponto de fusão. [p=0.2] {b}A do segundo é o ponto de ebulição. [p=0.3] Na água, ao nível do mar, {c}zero e cem graus. [p=0.3] {d}Cada substância pura tem os seus valores, como uma impressão digital."),
    # misturas
    dict(id="s09", block="misturas", text="E se a água tiver sal? [p=0.2] {a}Na água salgada, a fervura começa um pouco acima de cem graus [p=0.1] e {b}a temperatura continua subindo enquanto ferve. [p=0.3] {c}A linha não deita: ela só fica menos inclinada. [p=0.3] O gelo de água salgada também derrete com a temperatura mudando. [p=0.2] {d}Na mistura comum, não há patamar nenhum."),
    dict(id="s10", block="misturas", text="Mas algumas misturas enganam. [p=0.2] {a}A solda de estanho e chumbo, usada em eletrônica, [p=0.1] {b}derrete num patamar, sempre a cento e oitenta e três graus, como se fosse pura. [p=0.3] {c}Só a fervura sobe sem parar. [p=0.2] Essa é uma {d}mistura eutética."),
    dict(id="s11", block="misturas", text="{a}O álcool noventa e seis por cento, de álcool e água, faz o contrário. [p=0.2] {b}Ferve num patamar, perto de setenta e oito graus, [p=0.1] {c}e o derretimento é que sobe. [p=0.3] Essa é uma {d}mistura azeotrópica."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.1] {a}conte os patamares. [p=0.3] {b}Dois patamares: substância pura. [p=0.2] {c}Nenhum: mistura comum. [p=0.2] {d}Só o de baixo, da fusão: eutética. [p=0.2] {e}Só o de cima, da ebulição: azeotrópica."),
    dict(id="s13", block="atalho", text="Para não trocar os nomes, use a origem deles. [p=0.2] {a}Eutético vem do grego e quer dizer que funde bem. [p=0.3] {b}Azeótropo quer dizer que não muda ao ferver. [p=0.3] Funciona porque {c}cada nome diz qual patamar fica."),
    dict(id="s14", block="atalho", text="{a}Não compensa quando o gráfico mostra só um trecho, [p=0.1] como só o líquido fervendo. [p=0.2] {b}Aí, você só pode julgar o patamar que aparece."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}ler o patamar no eixo errado. [p=0.3] {b}No gráfico da água, a fusão vai de dois a quatro minutos, [p=0.1] e a pessoa responde que o ponto de fusão é dois."),
    dict(id="s16", block="erro", text="{a}Mas ponto de fusão é temperatura, não tempo. [p=0.2] {b}Siga o patamar até o eixo do lado: [p=0.1] {c}zero grau. [p=0.3] {d}O eixo de baixo só diz por quanto tempo a fusão durou."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Um material é aquecido. [p=0.2] {b}A fusão vai de dez a dezoito graus, subindo. [p=0.2] {c}Depois, a linha deita nos setenta e oito graus até o fim da fervura. [p=0.3] {d}Qual é o ponto de ebulição? [p=0.2] {e}E o material é puro ou é mistura? De que tipo?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}O patamar está nos setenta e oito graus: [p=0.1] {b}esse é o ponto de ebulição. [p=0.3] {c}A fusão subiu de dez a dezoito: ali não há patamar."),
    dict(id="s20", block="resposta", text="{a}Um patamar só, e é o de cima. [p=0.2] {b}Então é uma mistura azeotrópica, como o álcool noventa e seis por cento. [p=0.3] {c}Quem viu o patamar e respondeu substância pura esqueceu de olhar a fusão."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.1] {a}o patamar é a mudança de estado; [p=0.2] {b}a temperatura dele, lida no eixo do lado, é o ponto de fusão ou de ebulição; [p=0.2] e {c}contar os patamares diz se é pura, comum, eutética ou azeotrópica."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica tudo isso em questões de prova: [p=0.2] {a}classificar materiais e ler gráficos de aquecimento. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
