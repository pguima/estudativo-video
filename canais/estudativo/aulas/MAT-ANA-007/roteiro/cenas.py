# Estudativo · MAT-ANA-007 — Praticando: pontos e retas (Matemática · Geometria Analítica · prática).
# Habilidade: calcular distâncias, achar a equação de uma reta e dizer como duas retas se cruzam.
# Pré-requisitos: MAT-ANA-001, MAT-ANA-002, MAT-ANA-003, MAT-ANA-004, MAT-ANA-005, MAT-ANA-006. Próxima: MAT-ANA-008.
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.
# Visual: plano com dois pontos e o triângulo da distância; reta por dois pontos; duas retas paralelas; duas retas perpendiculares com o ponto de encontro (2, 4).

TITULO = "Praticando: pontos e retas"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações com pontos e retas, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}quatro ferramentas: [p=0.2] {b}a distância, que é a hipotenusa do triângulo entre os pontos; [p=0.2] {c}o eme, delta ípsilon dividido por delta xis; [p=0.2] {d}a equação reduzida e a geral; [p=0.2] e {e}o eme das paralelas e das perpendiculares. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: distância
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Num mapa em quilômetros, um posto fica em {b}xis menos dois, ípsilon três, [p=0.2] e uma oficina em {c}xis seis, ípsilon menos três. [p=0.3] {d}Qual é a distância em linha reta entre eles?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Nos xis, de menos dois até seis: sinais diferentes, [p=0.2] dois mais seis dá oito. [p=0.2] {b}Nos ípsilons, de três até menos três: [p=0.2] três mais três dá seis. [p=0.3] {c}Oito ao quadrado dá sessenta e quatro. [p=0.2] {d}Seis ao quadrado dá trinta e seis. [p=0.2] {e}Somando, dá cem, e a raiz dá dez: dez quilômetros."),
    dict(id="s06", block="resposta1", text="Quem somou os catetos achou {a}catorze. [p=0.2] Esse é {b}o caminho pelas ruas, corredor e depois elevador. [p=0.3] A linha reta é a hipotenusa, e {c}dez é menos que catorze. [p=0.2] Faz sentido."),
    # situação 2: equação da reta
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma reta passa por {b}xis um, ípsilon um, [p=0.2] e por {c}xis três, ípsilon sete. [p=0.3] {d}Escreva a equação reduzida e a geral dessa reta."),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] {a}Delta ípsilon: sete menos um dá seis. [p=0.2] {b}Delta xis: três menos um dá dois. [p=0.2] {c}Eme igual a seis dividido por dois, que dá três. [p=0.3] Então {d}ípsilon igual a três xis mais ene. [p=0.2] Troque o primeiro ponto: {e}um igual a três mais ene, [p=0.2] e o ene dá menos dois."),
    dict(id="s10", block="resposta2", text="Reduzida: {a}ípsilon igual a três xis menos dois. [p=0.2] Tirando ípsilon de cada lado, a geral: {b}três xis menos ípsilon menos dois igual a zero. [p=0.3] Confira com o outro ponto: {c}três vezes três dá nove, menos dois dá sete. [p=0.2] Bateu."),
    # situação 3: paralelas
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] A reta {b}seis xis menos dois ípsilon mais cinco igual a zero [p=0.2] cruza a reta da situação dois? [p=0.3] {c}Se cruzar, é em ângulo reto?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Na geral, o eme não se lê direto: {a}isole o ípsilon. [p=0.2] Somando dois ípsilon de cada lado: {b}dois ípsilon igual a seis xis mais cinco. [p=0.2] Dividindo tudo por dois: {c}ípsilon igual a três xis mais dois vírgula cinco."),
    dict(id="s14", block="resposta3", text="{a}Eme igual a três, o mesmo da outra reta. [p=0.2] E o ene é diferente: {b}dois vírgula cinco contra menos dois. [p=0.3] Mesma inclinação, cortes diferentes no eixo ípsilon: [p=0.2] {c}são paralelas e nunca se cruzam. [p=0.3] Quem leu o seis da geral como eme {d}achou inclinações diferentes, e disse que elas se cruzam."),
    # atalho
    dict(id="s15", block="atalho", text="Isolar o ípsilon, como você fez, sempre funciona. [p=0.2] Para conferir rápido, cabe um atalho de prova: [p=0.2] {a}na geral, o eme é menos o número do xis, dividido pelo número do ípsilon, cada um com o seu sinal. [p=0.3] Em seis xis menos dois ípsilon mais cinco: [p=0.2] {b}menos seis dividido por menos dois dá três. [p=0.2] Sem isolar nada."),
    dict(id="s16", block="atalho", text="Funciona porque {a}isolar o ípsilon pode levar o termo do xis para o outro lado, com o sinal trocado, [p=0.2] e {b}depois dividir tudo pelo número do ípsilon. [p=0.2] Na situação, você passou o ípsilon, e seis dividido por dois deu o mesmo três. [p=0.3] {c}Não compensa quando você também precisa do ene, [p=0.2] como para dizer onde a reta corta o eixo ípsilon: [p=0.2] aí, {d}isole o ípsilon de uma vez. [p=0.2] E sem ípsilon, como em xis menos três igual a zero, a reta fica em pé e não tem eme."),
    # situação 4: perpendicular e encontro
    dict(id="s17", block="questao4", text="{a}Última situação, e ela junta tudo. [p=0.2] Ache a reta que passa por {b}xis seis, ípsilon dois, [p=0.2] e é {c}perpendicular a ípsilon igual a dois xis. [p=0.3] Depois, {d}diga em que ponto as duas retas se cruzam."),
    dict(id="s18", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta4", text="Vamos lá. [p=0.2] A reta dada tem {a}eme igual a dois. [p=0.2] Nas perpendiculares, o produto dos emes dá menos um: [p=0.2] {b}inverta e troque o sinal, e o eme vira menos um meio. [p=0.2] Confira: {c}dois vezes menos um meio dá menos um."),
    dict(id="s20", block="resposta4", text="Pelo atalho do ponto e da inclinação: [p=0.2] {a}ípsilon menos dois igual a menos um meio vezes, abre parênteses, xis menos seis. [p=0.2] {b}Menos um meio vezes menos seis dá três. [p=0.2] {c}Ípsilon menos dois igual a menos um meio xis mais três. [p=0.2] Somando dois de cada lado: {d}ípsilon igual a menos um meio xis mais cinco."),
    dict(id="s21", block="resposta4", text="Agora, o encontro. [p=0.2] Ali, {a}o ípsilon é o mesmo nas duas retas: [p=0.2] {b}dois xis igual a menos um meio xis mais cinco. [p=0.3] Multiplique tudo por dois para sumir a fração: {c}quatro xis igual a menos xis mais dez. [p=0.2] Somando xis de cada lado: {d}cinco xis igual a dez, e xis igual a dois."),
    dict(id="s22", block="resposta4", text="{a}Ípsilon igual a dois vezes dois, que dá quatro. [p=0.3] As retas se cruzam em {b}xis dois, ípsilon quatro, em ângulo reto. [p=0.2] Confira na outra reta: [p=0.2] {c}menos um meio vezes dois dá menos um, mais cinco dá quatro. [p=0.2] Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}a distância é a hipotenusa, [p=0.2] {b}o eme diz se as retas são paralelas ou perpendiculares, [p=0.2] e {c}o encontro sai de um sistema."),
    dict(id="s24", block="fim", text="Na próxima aula, a linha deixa de ser reta: [p=0.2] você conhece {a}a equação da circunferência [p=0.2] e lê {b}o centro e o raio dela de olho. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
