# Estudativo · MAT-ESP-011 — Pirâmide: volume (Matemática · Geometria Espacial · Pirâmides e cones).
# Habilidade: usar V = área da base · altura / 3 e calcular o volume de uma pirâmide de base quadrada de lado 6 e altura 10 (120).
# Pré-requisitos: MAT-ESP-007 (volume do prisma = área da base · altura). Usa MAT-ESP-001 (pirâmide, vértice, quadrangular), MAT-ESP-005 (cubo), MAT-ARE-002 e MAT-ARE-003 (áreas). Próxima: MAT-ESP-012.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Cilindro e cone não entram (fora do "já ensinado").

TITULO = "Pirâmide: volume"

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
    dict(id="s01", block="gancho", text="{a}Uma caixa e uma pirâmide, com {b}a mesma base e a mesma altura. [p=0.3] Encha a pirâmide de areia e despeje na caixa. [p=0.2] Quantas vezes até encher? [p=0.3] {c}Três vezes, certinho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o volume de qualquer pirâmide [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}o volume do prisma é a área da base vezes a altura, [p=0.2] e {c}as áreas do quadrado e do triângulo. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="piramide", text="{a}A pirâmide tem {b}uma base só, um polígono, [p=0.2] e {c}faces laterais em forma de triângulo [p=0.2] que se encontram num ponto lá em cima, {d}o vértice da pirâmide. [p=0.3] O nome vem da base: {e}base quadrada, pirâmide quadrangular."),
    dict(id="s05", block="piramide", text="{a}A altura da pirâmide é a distância do vértice até a base, [p=0.2] {b}descendo em pé, por dentro, em ângulo reto com a base. [p=0.3] Ela não é {c}a aresta inclinada do lado."),
    # por que um terço
    dict(id="s06", block="terco", text="Por que três? [p=0.2] Pegue {a}um cubo e escolha um canto de cima. [p=0.2] Ele se corta em {b}três pirâmides iguais, [p=0.2] todas com o vértice nesse mesmo canto. [p=0.3] A base de cada uma é {c}uma das três faces que não encostam nesse canto: [p=0.2] o chão e as duas paredes do lado oposto. [p=0.3] E a altura de cada uma é {d}a aresta do cubo. [p=0.2] Essas pirâmides são tortas: o vértice fica em cima de um canto da base, [p=0.2] e por isso a altura cai sobre uma aresta, e não por dentro."),
    dict(id="s07", block="terco", text="Então cada pirâmide é {a}um terço do cubo. [p=0.3] E isso vale para toda pirâmide: [p=0.2] {b}o volume é um terço do prisma de mesma base e mesma altura."),
    dict(id="s08", block="terco", text="Na fórmula: {a}volume igual à área da base vezes a altura, dividido por três. [p=0.3] É a conta do prisma, {b}com o dividido por três no fim."),
    # exemplos
    dict(id="s09", block="quadrada", text="Pirâmide de {a}base quadrada, com lado seis e {b}altura dez. [p=0.3] Base: {c}seis ao quadrado dá trinta e seis. [p=0.2] {d}Trinta e seis vezes dez dá trezentos e sessenta: [p=0.2] esse é o prisma. [p=0.2] {e}Dividido por três dá cento e vinte."),
    dict(id="s10", block="triangular", text="Com base triangular, mesma conta. [p=0.2] A base é um triângulo de {a}base seis e altura quatro: [p=0.2] {b}seis vezes quatro dividido por dois dá doze. [p=0.2] A pirâmide tem {c}altura cinco. [p=0.3] {d}Doze vezes cinco dá sessenta, [p=0.2] e {e}dividido por três dá vinte."),
    dict(id="s11", block="triangular", text="Repare que aqui {a}são duas alturas: [p=0.2] {b}a do triângulo da base, deitada no chão, [p=0.2] e {c}a da pirâmide, em pé. [p=0.3] Cada uma entra na sua conta."),
    # erro comum
    dict(id="s12", block="erro", text="O erro mais comum é {a}esquecer o dividido por três. [p=0.2] Na pirâmide de lado seis e altura dez, a pessoa para em {b}trezentos e sessenta. [p=0.3] Esse é {c}o volume da caixa em volta dela. [p=0.2] {d}A pirâmide cabe três vezes nessa caixa."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}divida por três primeiro. [p=0.2] Procure {b}o número que é múltiplo de três. [p=0.3] {c}Trinta e seis dividido por três dá doze. [p=0.2] {d}Doze vezes dez dá cento e vinte. [p=0.2] Conta pequena, sem passar por trezentos e sessenta."),
    dict(id="s14", block="atalho", text="Funciona porque {a}numa conta só de vezes e dividido, a ordem não muda o resultado. [p=0.3] {b}Não compensa quando nenhum número é múltiplo de três: [p=0.2] base vinte e cinco e altura oito dão {c}duzentos dividido por três. [p=0.2] Aí, {d}deixe em fração: duzentos terços."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma vela tem forma de {a}pirâmide de base quadrada, [p=0.2] com {b}seis centímetros de lado e {c}doze de altura. [p=0.3] Ela é derretida, [p=0.2] e a cera vira {d}uma vela em forma de caixa, com a mesma base quadrada. [p=0.3] {e}Qual a altura da vela nova?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Volume da pirâmide, pelo atalho: [p=0.2] {a}doze dividido por três dá quatro, [p=0.2] e {b}trinta e seis vezes quatro dá cento e quarenta e quatro centímetros cúbicos."),
    dict(id="s18", block="resposta", text="A caixa tem a mesma cera: [p=0.2] {a}trinta e seis vezes a altura igual a cento e quarenta e quatro. [p=0.2] {b}Cento e quarenta e quatro dividido por trinta e seis dá quatro centímetros. [p=0.3] Repare: {c}quatro é um terço de doze. [p=0.2] Mesma base e mesmo volume: {d}a caixa tem um terço da altura da pirâmide."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}pirâmide, área da base vezes altura, dividido por três. [p=0.2] {b}Um terço do prisma de mesma base e mesma altura."),
    dict(id="s20", block="fim", text="Na próxima aula, você acha {a}a altura de cada face da pirâmide, a apótema, com Pitágoras: [p=0.2] numa pirâmide de base quadrada com lado seis e altura quatro, ela dá {b}cinco. [p=0.2] E soma as faces para {c}a área total. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
