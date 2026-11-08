# Estudativo · MAT-TOP-010 — Parábola: foco e diretriz (Matemática · Tópicos Avançados · Noções de cônicas).
# Habilidade: ler em x² = 8y o foco (0, 2) e a diretriz y = −2 e explicar que cada ponto fica à mesma distância dos dois.
# Pré-requisitos: MAT-ANA-001 (distância entre dois pontos), MAT-FUN-018 (vértice da parábola). Próxima: MAT-TOP-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Pares narrados "xis quatro, ípsilon dois" (MAT-ANA-001). Letra p narrada "pê".
# Equação da reta (MAT-ANA-004) não está na ficha: "y = −2" é apresentada como a reta deitada em que todo ponto tem y = −2;
# a distância até ela é só a diferença dos ípsilons. A antena parabólica é fato conhecido (reflete os sinais para o foco).

TITULO = "Parábola: foco e diretriz"

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
    dict(id="s01", block="gancho", text="A antena parabólica tem esse nome porque {a}o corte dela é uma parábola. [p=0.2] Os sinais batem na antena e vão todos para {b}um ponto só: o foco. [p=0.3] Na parábola {c}xis ao quadrado igual a oito ípsilon, [p=0.2] o foco é {d}xis zero, ípsilon dois. [p=0.2] E dá para achar isso {e}de olho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê o foco e a diretriz na equação de uma parábola, [p=0.2] entende de onde eles vêm [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}a distância entre dois pontos, pelo triângulo retângulo; [p=0.2] e {c}o vértice da parábola, o ponto onde ela faz a curva e volta. [p=0.3] Se faltar alguma, procure no canal."),
    # definição
    dict(id="s04", block="definicao", text="Pegue {a}um ponto, o foco, [p=0.2] e {b}uma reta, a diretriz. [p=0.3] A parábola é {c}o conjunto de todos os pontos que ficam à mesma distância do foco e da diretriz. [p=0.3] E a distância até a reta é {d}o caminho mais curto, que chega em ângulo reto."),
    dict(id="s05", block="definicao", text="No exemplo, o foco é {a}xis zero, ípsilon dois. [p=0.2] A diretriz é {b}a reta ípsilon igual a menos dois: [p=0.2] {c}a reta deitada em que todo ponto tem ípsilon igual a menos dois."),
    dict(id="s06", block="definicao", text="Teste o ponto {a}xis quatro, ípsilon dois. [p=0.2] {b}Até o foco, ele anda quatro na horizontal: distância quatro. [p=0.2] {c}Até a diretriz, desce de dois até menos dois: distância quatro. [p=0.3] {d}Iguais: o ponto está na parábola."),
    dict(id="s07", block="definicao", text="Agora, {a}xis oito, ípsilon oito. [p=0.2] {b}Até o foco: catetos oito e seis, hipotenusa dez. [p=0.2] {c}Até a diretriz: de oito até menos dois, dez. [p=0.3] {d}Iguais de novo. [p=0.2] E {e}o vértice, xis zero, ípsilon zero, fica bem no meio: a dois do foco e a dois da diretriz."),
    # equação
    dict(id="s08", block="equacao", text="De onde vem o oito? [p=0.2] Chame de {a}pê a distância do vértice até o foco. [p=0.3] Com o vértice na origem e a parábola aberta para cima, [p=0.2] o foco fica em {b}xis zero, ípsilon pê, [p=0.2] e a diretriz em {c}ípsilon igual a menos pê. [p=0.3] Igualando as duas distâncias, depois de algumas contas, [p=0.2] sobra {d}xis ao quadrado igual a quatro pê ípsilon. [p=0.2] O importante aqui é guardar o resultado."),
    dict(id="s09", block="equacao", text="Então, {a}o número na frente do ípsilon é quatro pê. [p=0.2] Em xis ao quadrado igual a oito ípsilon, {b}quatro pê é oito, e pê é dois. [p=0.3] {c}Foco: xis zero, ípsilon dois. [p=0.2] {d}Diretriz: ípsilon igual a menos dois."),
    dict(id="s10", block="equacao", text="Se o número for negativo, como em {a}xis ao quadrado igual a menos oito ípsilon, [p=0.2] a parábola {b}abre para baixo: [p=0.2] {c}o foco desce para xis zero, ípsilon menos dois, [p=0.2] e {d}a diretriz sobe para ípsilon igual a dois."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}ler o número direto como foco. [p=0.2] Em xis ao quadrado igual a oito ípsilon, a pessoa diz: {b}foco em xis zero, ípsilon oito. [p=0.3] Mas o oito é {c}quatro pê, não pê. [p=0.2] Teste com o ponto xis oito, ípsilon oito: [p=0.2] ele ficaria {d}a oito desse foco e a dezesseis da diretriz. [p=0.2] Não bate. [p=0.2] {e}Divida por quatro: o foco está em ípsilon dois."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, para desenhar rápido: [p=0.2] {a}na altura do foco, a parábola tem largura quatro pê. [p=0.3] Em xis ao quadrado igual a oito ípsilon, {b}na altura ípsilon dois, ela vai de menos quatro até quatro: [p=0.2] largura oito. [p=0.3] {c}Com o vértice e esses dois pontos, o desenho sai no lugar certo."),
    dict(id="s13", block="atalho", text="Funciona porque, na altura do foco, {a}a distância até a diretriz é dois pê. [p=0.2] Então {b}cada lado fica a dois pê do foco: largura quatro pê. [p=0.3] {c}Com o vértice fora da origem, ache o vértice primeiro e meça a partir dele."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Na parábola {a}xis ao quadrado igual a doze ípsilon, [p=0.2] {b}onde estão o foco e a diretriz? [p=0.2] E {c}confira com o ponto xis seis, ípsilon três."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Quatro pê é doze, então pê é três. [p=0.2] {b}Foco: xis zero, ípsilon três. [p=0.2] {c}Diretriz: ípsilon igual a menos três."),
    dict(id="s17", block="resposta", text="E o ponto xis seis, ípsilon três: [p=0.2] {a}seis ao quadrado é trinta e seis, e doze vezes três também: ele está na parábola. [p=0.3] {b}Até o foco, anda seis: distância seis. [p=0.2] {c}Até a diretriz, de três até menos três: seis. [p=0.2] {d}Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}cada ponto da parábola fica à mesma distância do foco e da diretriz, [p=0.2] e, em {b}xis ao quadrado igual a quatro pê ípsilon, o foco está a pê do vértice."),
    dict(id="s19", block="fim", text="Na próxima aula, a curva ganha {a}dois focos: [p=0.2] é {b}a elipse. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
