# Estudativo · MAT-ESP-005 — Volume do cubo e do bloco (Matemática · Geometria Espacial).
# Habilidade: calcular o volume de uma caixa de 2 m por 1,5 m por 1 m (3 m³) e dizer que nela cabem 3.000 L.
# Pré-requisitos: MAT-ARE-002 (base vezes altura), MAT-ESP-001 (cubo, paralelepípedo ou bloco, aresta), MAT-MED-005 (cubinhos de 1 m³, 1 m³ = 1.000 L, 1 dm³ = 1 L). Próxima: MAT-ESP-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Letra A narrada "á".
# "Volume = área da base vezes altura" prepara MAT-ESP-007 (prisma).

TITULO = "Volume do cubo e do bloco"

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
    dict(id="s01", block="gancho", text="{a}Uma caixa-d'água em forma de bloco: [p=0.2] dois metros por um metro e meio, com um metro de altura. [p=0.3] Quantos litros cabem? [p=0.2] {b}Somar as medidas não diz nada. [p=0.2] A resposta é {c}três mil litros, e você vai achar com uma multiplicação."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o volume de qualquer cubo ou bloco, [p=0.2] passa para litros [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}a área do retângulo é base vezes altura; [p=0.2] {c}o metro cúbico é um cubo de um metro de lado; [p=0.2] e {d}um metro cúbico guarda mil litros. [p=0.3] Se faltar alguma, procure no canal."),
    # camadas
    dict(id="s04", block="camadas", text="Volume é {a}quantos cubinhos iguais enchem o espaço. [p=0.2] Com cubinhos de um metro cúbico, ele sai em metros cúbicos. [p=0.2] {b}O bloco, ou paralelepípedo, é a caixa de faces retangulares. [p=0.2] {c}O cubo é o bloco com todas as arestas iguais."),
    dict(id="s05", block="camadas", text="Um bloco de {a}quatro metros por três, com dois de altura. [p=0.2] No fundo, cabem {b}quatro cubinhos por fileira, em três fileiras: [p=0.2] {c}doze cubinhos. [p=0.3] É o mesmo número da {d}área do fundo: quatro vezes três dá doze metros quadrados."),
    dict(id="s06", block="camadas", text="Com dois metros de altura, são {a}duas camadas de doze: [p=0.2] doze vezes dois dá {b}vinte e quatro metros cúbicos. [p=0.3] Cada metro quadrado do fundo {c}segura uma coluna de cubinhos, da altura da caixa."),
    # fórmula
    dict(id="s07", block="formula", text="Então, {a}volume é a área da base vezes a altura. [p=0.3] No bloco, a base é um retângulo, e fica {b}vê igual a á vezes bê vezes cê. [p=0.2] {c}Vê é o volume, [p=0.1] e {d}á, bê e cê são as três arestas: comprimento, largura e altura."),
    dict(id="s08", block="formula", text="No cubo, as três arestas são iguais: {a}á vezes á vezes á. [p=0.2] {b}Vê igual a á ao cubo. [p=0.2] É daí que vem o nome {c}ao cubo. [p=0.3] Um cubo de {d}três metros de aresta: [p=0.2] {e}três ao cubo dá vinte e sete metros cúbicos."),
    # a caixa-d'água
    dict(id="s09", block="caixa", text="Voltando à caixa-d'água. [p=0.2] Fundo: {a}dois vezes um vírgula cinco dá três metros quadrados. [p=0.2] Vezes {b}um metro de altura, dá três metros cúbicos. [p=0.3] Cada metro cúbico guarda mil litros: [p=0.2] {c}três vezes mil dá três mil litros."),
    # erro
    dict(id="s10", block="erro", text="Cuidado com o erro comum: {a}multiplicar medidas em unidades diferentes. [p=0.2] Um tanque de {b}dois metros por um vírgula cinco, com cinquenta centímetros de altura. [p=0.2] Quem multiplica direto faz {c}dois vezes um vírgula cinco vezes cinquenta, que dá cento e cinquenta."),
    dict(id="s11", block="erro", text="Cento e cinquenta metros cúbicos {a}seriam cento e cinquenta mil litros, [p=0.2] num tanque mais baixo que a caixa de três mil! [p=0.3] {b}Cinquenta centímetros são zero vírgula cinco metro. [p=0.2] {c}Três vezes zero vírgula cinco dá um vírgula cinco metro cúbico: [p=0.2] {d}mil e quinhentos litros."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}meça tudo em decímetros, e o volume sai direto em litros. [p=0.3] Na escada do metro, de metro para decímetro é {b}uma casa para a direita. [p=0.2] A caixa-d'água vira {c}vinte decímetros por quinze por dez. [p=0.2] {d}Vinte vezes quinze dá trezentos, [p=0.2] e {e}trezentos vezes dez dá três mil litros."),
    dict(id="s13", block="atalho", text="Funciona porque {a}um decímetro cúbico é exatamente um litro. [p=0.3] E ainda resolve o erro das unidades: {b}tudo vai para a mesma. [p=0.3] {c}Não compensa quando a prova pede a resposta em metros cúbicos: [p=0.2] aí, {d}fique em metros."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um aquário mede {a}sessenta centímetros de comprimento, trinta de largura e quarenta de altura. [p=0.2] {b}Quantos litros cabem nele? [p=0.3] E {c}uma caixa cúbica de dois metros de aresta: quantos litros ela guarda?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] No aquário, pelo atalho, {a}tudo em decímetros. [p=0.2] De centímetro para decímetro é um degrau para cima: uma casa para a esquerda. [p=0.2] Sessenta vira seis. [p=0.1] Trinta vira três. [p=0.1] Quarenta vira quatro. [p=0.2] {b}Seis vezes três dá dezoito. [p=0.2] {c}Dezoito vezes quatro dá setenta e dois litros."),
    dict(id="s17", block="resposta", text="Na caixa cúbica, {a}dois ao cubo dá oito metros cúbicos. [p=0.2] {b}Oito vezes mil dá oito mil litros. [p=0.3] Repare: {c}a aresta dobrou em relação ao cubo de um metro, [p=0.2] e o volume ficou {d}oito vezes maior."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}volume é a área da base vezes a altura. [p=0.2] {b}No bloco, á vezes bê vezes cê. [p=0.2] {c}No cubo, á ao cubo. [p=0.2] E {d}cada metro cúbico são mil litros."),
    dict(id="s19", block="fim", text="Na próxima aula, a casca da caixa: [p=0.2] {a}quanta tinta você gasta para pintar uma caixa por fora, [p=0.2] e {b}a diagonal do cubo, de um canto até o canto oposto, por dentro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
