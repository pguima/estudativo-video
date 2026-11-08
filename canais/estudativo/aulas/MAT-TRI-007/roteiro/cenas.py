# Estudativo · MAT-TRI-007 — Radianos e o ciclo trigonométrico (Matemática · Trigonometria).
# Habilidade: transformar 60° em π/3 rad, marcar um arco no ciclo e dizer que 390° cai no mesmo ponto que 30°.
# Pré-requisitos: MAT-FUN-001 (plano cartesiano, quadrantes), MAT-POL-005 (arco, ângulo central, regra de três), MAT-TRI-003 (ângulos notáveis). Usa MAT-POL-004 (C = 2πr) e MAT-RAZ-006 (regra de três direta). Próxima: MAT-TRI-008.
# Questão inédita, criada para esta aula. Graus por extenso; radianos lidos como frações ("pi terços", "pi meios"), nunca "pi sobre três". Na tela, π/3 rad.

TITULO = "Radianos e o ciclo trigonométrico"

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
    dict(id="s01", block="gancho", text="{a}Trezentos e noventa graus. [p=0.2] É mais que uma volta inteira. [p=0.3] Mesmo assim, ele cai {b}exatamente no mesmo ponto que trinta graus. [p=0.3] E a prova às vezes nem fala em graus: [p=0.2] escreve {c}pi terços."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você troca graus por radianos e volta, [p=0.2] {b}marca qualquer arco no ciclo trigonométrico [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}o plano cartesiano, com os eixos xis e ípsilon e os quatro quadrantes; [p=0.2] {c}o arco, um pedaço da circunferência, e a volta inteira, que mede dois pi érre; [p=0.2] e {d}a regra de três. [p=0.3] Se faltar alguma, procure no canal."),
    # radiano
    dict(id="s04", block="radiano", text="Até aqui, você mediu ângulo em graus. [p=0.2] {a}Há outro jeito: medir pelo arco. [p=0.3] Numa circunferência, pegue {b}um arco com o mesmo comprimento do raio. [p=0.2] {c}O ângulo central desse arco vale um radiano."),
    dict(id="s05", block="radiano", text="Quantos radianos cabem numa volta? [p=0.2] {a}A volta mede dois pi érre. [p=0.2] {b}Cada radiano ocupa um pedaço de arco do tamanho do raio, érre. [p=0.2] {c}Dois pi érre dividido por érre dá dois pi. [p=0.3] {d}A volta inteira tem dois pi radianos."),
    dict(id="s06", block="radiano", text="{a}Volta inteira: trezentos e sessenta graus, ou dois pi radianos. [p=0.2] {b}Meia volta: cento e oitenta graus, ou pi radianos. [p=0.3] Guarde esta: {c}pi radianos é igual a cento e oitenta graus. [p=0.2] Um radiano sozinho dá {d}pouco mais de cinquenta e sete graus."),
    # conversão
    dict(id="s07", block="converter", text="Para converter, {a}regra de três. [p=0.2] Na primeira linha, {b}cento e oitenta graus para pi radianos. [p=0.2] Na segunda, {c}sessenta graus para xis."),
    dict(id="s08", block="converter", text="Na cruz: {a}cento e oitenta xis igual a sessenta pi. [p=0.2] {b}Xis igual a sessenta pi, dividido por cento e oitenta. [p=0.2] {c}Sessenta dividido por cento e oitenta dá um terço. [p=0.3] {d}Sessenta graus é pi terços radianos."),
    # ciclo
    dict(id="s09", block="ciclo", text="Agora, o ciclo trigonométrico. [p=0.2] {a}É uma circunferência de raio um, com o centro na origem do plano cartesiano. [p=0.2] {b}Os eixos dividem o ciclo nos quatro quadrantes."),
    dict(id="s10", block="ciclo", text="Duas regras para marcar um arco. [p=0.2] {a}O ponto de partida fica onde o ciclo corta o eixo xis, à direita. [p=0.2] {b}O sentido positivo é o anti-horário: o contrário do relógio, subindo."),
    dict(id="s11", block="ciclo", text="Marque {a}sessenta graus: [p=0.2] você sobe dois terços do caminho até o topo, ainda no primeiro quadrante. [p=0.3] {b}Noventa graus é o topo. [p=0.2] {c}Cento e oitenta, o lado esquerdo. [p=0.2] {d}Duzentos e setenta, embaixo. [p=0.3] Em radianos: {e}pi meios, pi e três pi meios."),
    # mais de uma volta
    dict(id="s12", block="voltas", text="E trezentos e noventa? [p=0.2] {a}Uma volta inteira é trezentos e sessenta. [p=0.2] {b}Trezentos e noventa menos trezentos e sessenta dá trinta. [p=0.3] {c}Você dá uma volta completa, volta ao início [p=0.2] e anda mais trinta. [p=0.2] {d}Para em cima do ponto de trinta graus."),
    dict(id="s13", block="voltas", text="Ângulo maior que uma volta: {a}tire trezentos e sessenta até ficar abaixo de trezentos e sessenta. [p=0.3] {b}Setecentos e cinquenta menos trezentos e sessenta dá trezentos e noventa. [p=0.2] {c}Menos trezentos e sessenta de novo dá trinta. [p=0.2] Mesmo ponto."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}girar no sentido do relógio. [p=0.2] Quem faz isso marca trinta graus {b}embaixo do eixo xis, no quarto quadrante. [p=0.3] {c}O certo é subir: trinta graus fica no primeiro quadrante. [p=0.2] Girar no sentido do relógio também existe, [p=0.2] mas aí o ângulo ganha sinal: {d}aquele ponto é menos trinta graus."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}de radiano para grau, troque pi por cento e oitenta. [p=0.3] {b}Pi terços: cento e oitenta dividido por três dá sessenta graus. [p=0.2] {c}Três pi quartos: três vezes cento e oitenta dá quinhentos e quarenta, [p=0.2] e dividido por quatro dá cento e trinta e cinco graus."),
    dict(id="s16", block="atalho", text="E de grau para radiano: [p=0.2] {a}quantas vezes o ângulo cabe em cento e oitenta? [p=0.2] {b}Sessenta cabe três vezes: pi terços. [p=0.2] {c}Quarenta e cinco cabe quatro vezes: pi quartos. [p=0.3] {d}Cento e vinte não cabe um número inteiro de vezes: aí, use a regra de três."),
    dict(id="s17", block="atalho", text="Funciona porque {a}pi radianos e cento e oitenta graus são o mesmo ângulo. [p=0.3] {b}Só vale quando o pi é um ângulo em radianos. [p=0.2] No comprimento da volta, dois pi érre, {c}o pi é o número três vírgula catorze, e não cento e oitenta."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}Transforme cento e vinte graus em radianos. [p=0.3] {b}Depois, diga em que quadrante cai o arco de quatrocentos e oitenta graus."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Cento e oitenta graus para pi, cento e vinte para xis. [p=0.2] {b}Xis igual a cento e vinte pi, dividido por cento e oitenta. [p=0.2] Simplificando por sessenta, {c}cento e vinte dividido por cento e oitenta dá dois terços. [p=0.2] {d}Dois pi terços radianos."),
    dict(id="s21", block="resposta", text="Conferindo pelo atalho: {a}duas vezes cento e oitenta dá trezentos e sessenta, [p=0.2] e dividido por três dá cento e vinte. [p=0.2] Bateu. [p=0.3] {b}Quatrocentos e oitenta menos trezentos e sessenta dá cento e vinte. [p=0.2] Cento e vinte fica {c}entre noventa e cento e oitenta: [p=0.2] {d}segundo quadrante."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}pi radianos é cento e oitenta graus. [p=0.2] {b}No ciclo, comece à direita e gire no anti-horário. [p=0.2] {c}A cada volta inteira, você cai no mesmo ponto."),
    dict(id="s23", block="fim", text="Na próxima aula, o ciclo ganha seno e cosseno: [p=0.2] {a}o seno se lê no eixo vertical, e o cosseno no horizontal. [p=0.2] Você vê que {b}seno de noventa graus dá um, que cosseno de cento e oitenta dá menos um, [p=0.2] e {c}o sinal de cada um em cada quadrante. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
