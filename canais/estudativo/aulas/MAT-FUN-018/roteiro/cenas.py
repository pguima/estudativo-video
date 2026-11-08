# Estudativo · MAT-FUN-018 — Vértice da parábola (Matemática · Funções · Função quadrática).
# Habilidade: achar o vértice (2, −1) de f(x) = x² − 4x + 3 com x = −b/2a ou pela média das raízes e dizer a imagem da função.
# Pré-requisitos: MAT-FUN-004 (imagem e intervalo), MAT-FUN-017 (raízes da parábola). Próxima: MAT-FUN-019.
# Questão inédita, criada para esta aula. yv = −Δ/4a não entra: a ficha pede só x = −b/2a, a média das raízes e f(xv).
# Máximo e mínimo (MAT-FUN-007) fora da ficha: explicados na hora como ponto mais alto e mais baixo.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á".
# Visual: parábola de x² − 4x + 3 com pares simétricos (0 e 4, 1 e 3), eixo de simetria tracejado em x = 2, vértice (2, −1); imagem como sombra no eixo y de −1 para cima.

TITULO = "Vértice da parábola"

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
    dict(id="s01", block="gancho", text="{a}A parábola de xis ao quadrado menos quatro xis mais três desce, {b}faz a curva e sobe. [p=0.3] Esse ponto da virada é o {c}vértice. [p=0.2] É ele que responde perguntas de altura máxima, lucro máximo e menor custo. [p=0.3] E dá para achá-lo {d}sem desenhar."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o vértice de duas maneiras, diz a imagem da função [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}as raízes, onde a parábola corta o eixo xis, que nesta parábola são um e três, [p=0.2] e {b}a imagem, as saídas que a função tem de verdade, escrita como intervalo. [p=0.3] Se faltar alguma, procure no canal."),
    # simetria
    dict(id="s04", block="simetria", text="Olhe a tabela desta parábola. [p=0.2] {a}Efe de zero é três, e efe de quatro também. [p=0.2] {b}Efe de um é zero, e efe de três também. [p=0.3] Os valores se repetem aos pares, {c}em volta do dois."),
    dict(id="s05", block="simetria", text="A parábola é {a}simétrica. [p=0.2] Uma reta em pé, passando pelo xis dois, {b}divide a parábola em duas metades espelhadas. [p=0.2] Ela se chama {c}eixo de simetria. [p=0.3] E o vértice fica em cima dela."),
    # média das raízes
    dict(id="s06", block="media", text="Por isso, o xis do vértice fica {a}no meio das raízes. [p=0.2] O meio entre dois números é a média: {b}some e divida por dois. [p=0.2] {c}Um mais três dá quatro. [p=0.2] Dividido por dois dá dois."),
    dict(id="s07", block="media", text="E o ípsilon do vértice? [p=0.2] {a}Troque o xis por dois na função. [p=0.2] {b}Quatro menos oito mais três: menos um. [p=0.3] O vértice é {c}xis dois, ípsilon menos um. [p=0.2] Como o á é positivo, ele é {d}o ponto mais baixo da parábola, o mínimo da função."),
    # fórmula
    dict(id="s08", block="formula", text="E quando a parábola não tem raízes? [p=0.2] Existe uma fórmula que sempre funciona: [p=0.2] {a}xis do vértice igual a menos bê, dividido por dois á."),
    dict(id="s09", block="formula", text="Ela sai da Bhaskara. [p=0.2] As raízes são {a}menos bê mais raiz de delta, e menos bê menos raiz de delta, as duas divididas por dois á. [p=0.3] Some e divida por dois: {b}o mais raiz de delta e o menos raiz de delta se cancelam. [p=0.2] {c}Sobra menos bê, dividido por dois á. [p=0.3] Repare que o cê nem entra nessa fórmula. [p=0.2] Mudar o cê soma o mesmo número a todas as saídas: a parábola inteira sobe ou desce, e o vértice continua no mesmo xis. [p=0.2] Por isso a fórmula vale mesmo quando a parábola não toca o eixo xis."),
    dict(id="s10", block="formula", text="Na nossa parábola, {a}bê vale menos quatro, então menos bê é quatro. [p=0.2] {b}Dois á dá dois. [p=0.2] {c}Quatro dividido por dois dá dois. [p=0.3] O mesmo dois da média."),
    # imagem
    dict(id="s11", block="imagem", text="Agora, a imagem. [p=0.2] A parábola abre para cima {a}a partir do menos um, e sobe sem parar. [p=0.3] Então as saídas são {b}o menos um e tudo o que fica acima dele. [p=0.2] Como intervalo: {c}de menos um até mais infinito, [p=0.2] fechado no menos um, que a função alcança, e aberto no infinito."),
    dict(id="s12", block="imagem", text="Com á negativo, é o contrário. [p=0.2] O vértice é {a}o ponto mais alto, o máximo, [p=0.2] e a imagem vai {b}de menos infinito até o ípsilon do vértice."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}usar o xis do vértice na imagem. [p=0.2] A pessoa acha o dois e diz que a imagem vai de dois para cima. [p=0.3] Mas imagem é saída, e {b}saída é ípsilon. [p=0.2] O dois diz {c}onde a curva vira. [p=0.2] O menos um diz {d}até onde ela desce."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}quando as raízes vêm de graça, use a média. [p=0.2] Em {b}efe de xis igual a xis menos um, vezes xis menos cinco, [p=0.2] um produto só dá zero quando um fator vale zero: as raízes são {c}um e cinco, sem conta. [p=0.2] O xis do vértice é {d}três."),
    dict(id="s15", block="atalho", text="Funciona porque o vértice fica no eixo de simetria, bem no meio das raízes. [p=0.3] Não compensa quando {a}o delta é negativo e não há raízes, [p=0.2] ou quando as raízes não saem exatas. [p=0.2] Aí, vá de {b}menos bê dividido por dois á."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Ache o vértice de {a}efe de xis igual a menos xis ao quadrado mais seis xis menos cinco. [p=0.3] {b}Ele é o ponto mais alto ou o mais baixo? [p=0.2] E qual é a imagem da função?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Á vale menos um, e bê vale seis. [p=0.2] Menos bê é menos seis, e dois á é menos dois. [p=0.2] Xis do vértice: {b}menos seis dividido por menos dois, três. [p=0.3] Ípsilon do vértice: troque o xis por três. [p=0.2] Três ao quadrado é nove, e com o menos na frente, {c}menos nove. [p=0.2] Seis vezes três dá dezoito. [p=0.2] Menos nove, mais dezoito, menos cinco: {d}quatro. [p=0.2] Vértice: {e}xis três, ípsilon quatro."),
    dict(id="s19", block="resposta", text="Á negativo: a parábola abre para baixo, e o vértice é {a}o ponto mais alto, o máximo. [p=0.2] A imagem vai {b}de menos infinito até quatro, fechado no quatro. [p=0.3] Conferindo pela média: efe de um dá menos um mais seis menos cinco, zero. [p=0.2] Efe de cinco dá menos vinte e cinco mais trinta menos cinco, também zero. [p=0.2] As raízes são {c}um e cinco, e o meio é três. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}o xis do vértice é a média das raízes, ou menos bê dividido por dois á, [p=0.2] e {b}a imagem começa ou termina no ípsilon do vértice."),
    dict(id="s21", block="fim", text="Na próxima aula, o vértice resolve problemas: [p=0.2] {a}a altura máxima de uma bola lançada para cima e o lucro máximo de uma loja. [p=0.2] E a pergunta que decide: {b}ela quer o xis ou o ípsilon do vértice? [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
