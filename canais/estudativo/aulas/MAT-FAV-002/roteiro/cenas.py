# Estudativo · MAT-FAV-002 — Módulo de um número e gráfico em V (Matemática · Funções Avançadas · Função modular e definida por partes).
# Habilidade: dizer que |−7| = 7, desenhar o V de y = |x|, deslocá-lo em y = |x − 2| + 1 e rebater para cima a parte negativa de y = |x² − 4|.
# Pré-requisitos: MAT-FAV-001 (definida por partes), MAT-FUN-017 (raízes da parábola). Próxima: MAT-FAV-003.
# Questão inédita, criada para esta aula. Vértice da parábola por fórmula (fora da ficha): não usado; o fundo de x² − 4 é o corte no eixo y.
# Módulo: |−7| = 7, |7| = 7, |0| = 0 · |x| = x se x ≥ 0; −x se x < 0 · x = −7 → −x = 7.
# Tabela de |x|: 0 → 0, ±1 → 1, ±2 → 2, ±3 → 3.
# |x − 2| + 1: vértice (2, 1) · x = 0 e x = 4 → |∓2| + 1 = 3.
# x² − 4: raízes −2 e 2 (x² = 4), corta o eixo y em −4 · |x² − 4|: parte entre −2 e 2 rebatida, (0, −4) → (0, 4).
# Erro: |x − 2| levado para a esquerda; x − 2 = 0 → x = 2.
# Questão: y = |x + 3| − 2 · vértice: x + 3 = 0 → x = −3, y = −2 · eixo y: |0 + 3| − 2 = 1.
# Visual: reta numérica com os sete passos de −7 e de 7; chave do módulo; tabela e plano −4..4 com o V (E.curva de abs);
#   V que anda para (2, 1) com setas; parábola x² − 4 e a parte de baixo rebatendo (dobra no eixo x); palco escuro no atalho.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; "módulo de xis".

TITULO = "Módulo de um número e gráfico em V"

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
    dict(id="s01", block="gancho", text="{a}Menos sete e sete são números diferentes. [p=0.2] Mas cada um está {b}a sete passos do zero. [p=0.3] Essa distância tem nome: {c}módulo. [p=0.2] E o gráfico dela tem a forma de {d}um vê."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o módulo, [p=0.2] {b}desenha o vê, [p=0.2] {c}leva o vê para qualquer lugar do plano [p=0.2] e {d}rebate para cima a parte de baixo de um gráfico."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}a função definida por partes, com a chave e as condições; [p=0.2] e {b}as raízes de uma parábola, onde ela corta o eixo xis. [p=0.3] Se faltar alguma, procure no canal."),
    # módulo
    dict(id="s04", block="modulo", text="O módulo de um número é {a}a distância dele até o zero, na reta. [p=0.2] Ele se escreve entre {b}duas barras em pé. [p=0.3] {c}Módulo de menos sete é sete. [p=0.2] {d}Módulo de sete é sete. [p=0.2] {e}Módulo de zero é zero. [p=0.3] Distância nunca é negativa, então {f}o módulo nunca dá negativo."),
    dict(id="s05", block="modulo", text="Como função, o módulo é {a}uma função por partes. [p=0.2] {b}Se xis for maior ou igual a zero, o módulo é o próprio xis. [p=0.2] {c}Se xis for negativo, o módulo é menos xis. [p=0.3] Parece estranho, mas olhe: [p=0.2] com xis igual a menos sete, menos xis é o oposto de menos sete: {d}sete. [p=0.2] O sinal de menos {e}desfaz o negativo."),
    # o vê
    dict(id="s06", block="ve", text="Monte a tabela de {a}ípsilon igual ao módulo de xis. [p=0.2] {b}Xis zero dá zero. [p=0.2] {c}Xis um e menos um dão um. [p=0.2] {d}Xis dois e menos dois dão dois. [p=0.2] {e}Xis três e menos três dão três."),
    dict(id="s07", block="ve", text="Marque os pontos e ligue: [p=0.2] {a}um vê, com a ponta na origem. [p=0.2] A ponta se chama {b}vértice. [p=0.3] À direita, é a reta ípsilon igual a xis. [p=0.2] À esquerda, ípsilon igual a menos xis: {c}as duas linhas da chave."),
    # deslocar
    dict(id="s08", block="desloca", text="Agora, {a}ípsilon igual ao módulo de xis menos dois, mais um. [p=0.3] {b}O mais um, fora do módulo, sobe o vê uma casa. [p=0.2] {c}O menos dois, dentro, leva o vê duas casas para a direita. [p=0.3] Vértice em {d}xis dois, ípsilon um."),
    dict(id="s09", block="desloca", text="Confira: [p=0.2] {a}com xis igual a dois, fica módulo de zero, mais um: um. [p=0.2] É o menor valor possível, [p=0.2] porque {b}o módulo nunca fica abaixo de zero. [p=0.3] {c}Xis zero e xis quatro dão três: o vê continua simétrico."),
    # rebater
    dict(id="s10", block="rebate", text="O módulo também {a}dobra gráficos. [p=0.2] Veja {b}ípsilon igual a xis ao quadrado menos quatro. [p=0.2] É uma parábola que corta o eixo xis em {c}menos dois e dois, [p=0.2] e corta o eixo ípsilon {d}lá embaixo, em menos quatro."),
    dict(id="s11", block="rebate", text="Agora coloque tudo dentro do módulo. [p=0.2] O que estava {a}acima do eixo xis fica igual. [p=0.2] O que estava {b}abaixo vira positivo: [p=0.2] {c}rebate para cima, como num espelho no eixo xis. [p=0.3] O ponto mais baixo, que era menos quatro, vira {d}mais quatro."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}andar para o lado errado. [p=0.2] No módulo de xis menos dois, a pessoa vê o sinal de menos e {b}leva o vê para a esquerda."),
    dict(id="s13", block="erro", text="Teste: [p=0.2] a ponta do vê fica onde o módulo vale zero. [p=0.2] {a}Xis menos dois dá zero quando xis é dois, [p=0.2] e não menos dois. [p=0.3] {b}Dentro do módulo, o sinal engana: [p=0.2] menos leva para a direita, mais leva para a esquerda."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: {a}o vértice está onde o de dentro zera. [p=0.3] {b}Iguale o de dentro a zero: esse é o xis do vértice. [p=0.2] {c}O número de fora é o ípsilon do vértice. [p=0.3] No módulo de xis menos dois, mais um: {d}xis dois, ípsilon um, sem desenhar nada."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o módulo é o menor possível quando vale zero, [p=0.2] e é ali que o vê faz a ponta. [p=0.3] {b}Não vale quando o de dentro tem xis ao quadrado, como na parábola rebatida: [p=0.2] ali, o de dentro zera em dois lugares, e o desenho não é um vê."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Para {a}ípsilon igual ao módulo de xis mais três, menos dois: [p=0.3] {b}onde fica o vértice? [p=0.2] E {c}em que ponto o gráfico corta o eixo ípsilon?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Xis mais três zera quando xis é menos três. [p=0.2] {b}O número de fora é menos dois. [p=0.2] Vértice em {c}xis menos três, ípsilon menos dois: [p=0.2] o vê foi três casas para a esquerda e desceu duas."),
    dict(id="s19", block="resposta", text="No eixo ípsilon, {a}xis vale zero. [p=0.2] {b}Módulo de três é três; menos dois, um. [p=0.2] Corta em {c}ípsilon igual a um. [p=0.3] Repare: {d}o menos dois de fora levou a ponta do vê para baixo do eixo xis. [p=0.2] O módulo nunca é negativo, mas o que vem depois dele pode ser."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}módulo é distância até o zero, [p=0.2] {b}o gráfico é um vê, [p=0.2] e {c}o vértice está onde o de dentro zera."),
    dict(id="s21", block="fim", text="Na próxima aula, essa distância resolve {a}equações e inequações com módulo, [p=0.2] como {b}módulo de xis menos três igual a cinco, que tem duas respostas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
