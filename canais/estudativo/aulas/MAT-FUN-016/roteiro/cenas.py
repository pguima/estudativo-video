# Estudativo · MAT-FUN-016 — Função quadrática: a parábola (Matemática · Funções · Função quadrática).
# Habilidade: apontar a, b e c em f(x) = x² − 4x + 3, dizer se a parábola abre para cima ou para baixo e onde ela corta o eixo y.
# Pré-requisitos: MAT-FAT-007 (a, b e c; incompleta), MAT-FUN-006 (gráfico pela tabela; o U chamado parábola). Próxima: MAT-FUN-017.
# Questão inédita, criada para esta aula. Bhaskara (MAT-FAT-008) fora da ficha: raízes só aparecem lidas na tabela.
# O erro comum retoma 3 − x², a questão da MAT-FUN-006 ("U de cabeça para baixo").
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á".
# Visual: tabela e parábola de x² − 4x + 3 (pontos de x = 0 a 4); depois −x² + 4x − 3 no mesmo plano; corte no eixo y destacado.

TITULO = "Função quadrática: a parábola"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado menos quatro xis mais três. [p=0.3] Sem desenhar nada, dá para saber {b}se o gráfico é um sorriso ou uma cara triste, [p=0.2] e {c}onde ele cruza o eixo ípsilon. [p=0.3] Dois números da lei contam tudo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você aponta á, bê e cê numa função quadrática, diz para onde a parábola abre [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}apontar á, bê e cê numa equação do segundo grau, com o sinal junto, [p=0.2] e {b}desenhar um gráfico pela tabela: escolhe o xis, calcula o ípsilon e marca o ponto. [p=0.3] Se faltar alguma, procure no canal."),
    # a lei
    dict(id="s04", block="lei", text="Uma função do tipo {a}efe de xis igual a á xis ao quadrado, mais bê xis, mais cê, [p=0.2] com á diferente de zero, é uma {b}função quadrática. [p=0.2] Se o á fosse zero, o xis ao quadrado sumiria, e ela deixaria de ser do segundo grau. [p=0.3] É a equação do segundo grau virando função: {c}em vez do igual a zero, cada xis ganha a sua saída."),
    dict(id="s05", block="lei", text="Em {a}xis ao quadrado menos quatro xis mais três: [p=0.2] não tem número escrito na frente do xis ao quadrado, então {b}á vale um. [p=0.2] {c}Bê vale menos quatro, com o sinal junto. [p=0.2] {d}Cê vale três."),
    # tabela e gráfico
    dict(id="s06", block="tabela", text="Vamos à tabela, de zero a quatro. [p=0.2] {a}Efe de zero, três. [p=0.2] {b}Efe de um: um menos quatro mais três, zero. [p=0.2] {c}Efe de dois: quatro menos oito mais três, menos um. [p=0.2] {d}Efe de três dá zero, [p=0.2] e {e}efe de quatro dá três."),
    dict(id="s07", block="tabela", text="Marque os pontos e ligue com uma curva suave. [p=0.2] Sai {a}aquele U da aula de gráfico. [p=0.3] O gráfico de toda função quadrática tem essa forma, e ela se chama {b}parábola."),
    # concavidade
    dict(id="s08", block="concavidade", text="Agora troque os sinais: {a}menos xis ao quadrado mais quatro xis menos três. [p=0.2] Aqui, {b}á vale menos um. [p=0.3] A tabela, de zero a quatro, dá {c}menos três, zero, um, zero e menos três. [p=0.3] A mesma parábola, {d}virada de cabeça para baixo."),
    dict(id="s09", block="concavidade", text="Quem decide é o sinal do á. [p=0.2] {a}Á positivo, a parábola abre para cima, como um sorriso. [p=0.2] {b}Á negativo, abre para baixo, como uma cara triste. [p=0.3] O lado para onde ela abre se chama {c}concavidade."),
    dict(id="s10", block="concavidade", text="Por que o á? [p=0.2] Longe do zero, {a}o xis ao quadrado cresce muito mais rápido que o resto. [p=0.2] Em xis dez, ele vale cem, [p=0.2] enquanto menos quatro xis vale só menos quarenta. [p=0.3] Então, nas pontas, quem manda é {b}o á vezes xis ao quadrado, [p=0.2] e o sinal do á diz se as pontas sobem ou descem."),
    # corte no eixo y
    dict(id="s11", block="corte", text="E onde a parábola cruza o eixo ípsilon? [p=0.2] Todo ponto do eixo ípsilon tem {a}xis igual a zero. [p=0.2] Então calcule {b}efe de zero: á vezes zero, mais bê vezes zero, mais cê. [p=0.2] Sobra {c}só o cê."),
    dict(id="s12", block="corte", text="Em xis ao quadrado menos quatro xis mais três, o corte é em {a}xis zero, ípsilon três. [p=0.3] Na parábola virada, o cê é menos três, e o corte é em {b}xis zero, ípsilon menos três."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}olhar o primeiro número escrito. [p=0.2] Em {b}três menos xis ao quadrado, o três vem na frente, positivo, [p=0.2] e a pessoa diz que abre para cima. [p=0.3] Mas o á é o número do xis ao quadrado, esteja onde estiver: {c}menos um. [p=0.2] Abre para baixo. [p=0.2] É o U de cabeça para baixo que você desenhou na aula de gráfico."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}a parábola em dois segundos. [p=0.2] {b}O sinal do á dá a boca. [p=0.2] {c}O cê dá o corte no eixo ípsilon. [p=0.3] Em xis ao quadrado menos quatro xis mais três: {d}á positivo, sorriso, cortando no três."),
    dict(id="s15", block="atalho", text="Funciona porque o sinal do á manda nas pontas, e efe de zero apaga tudo menos o cê. [p=0.3] Não compensa quando a lei vem {a}em forma de produto, como xis menos um, vezes xis menos três. [p=0.2] Aí, o cê não aparece escrito. [p=0.2] {b}Calcule efe de zero direto: menos um vezes menos três, três."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Para {a}efe de xis igual a menos dois xis ao quadrado mais oito xis menos seis, [p=0.2] e para {b}gê de xis igual a quatro menos xis mais dois xis ao quadrado: [p=0.3] {c}aponte á, bê e cê, diga para onde cada parábola abre e onde ela corta o eixo ípsilon."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Em efe: {a}á vale menos dois, bê vale oito, cê vale menos seis. [p=0.2] Á negativo: {b}abre para baixo. [p=0.2] Corta o eixo ípsilon em {c}xis zero, ípsilon menos seis."),
    dict(id="s19", block="resposta", text="Em gê, a ordem está trocada. [p=0.2] O á é o do xis ao quadrado: {a}dois. [p=0.2] {b}Bê vale menos um. [p=0.2] {c}Cê vale quatro. [p=0.3] Abre {d}para cima, e corta em {e}xis zero, ípsilon quatro."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}o sinal do á diz para onde a parábola abre, [p=0.2] e {b}o cê diz onde ela corta o eixo ípsilon."),
    dict(id="s21", block="fim", text="Na próxima aula, o outro eixo: {a}onde a parábola corta o eixo xis. [p=0.2] Você vai achar {b}o um e o três desta mesma parábola, [p=0.2] e ver por que algumas parábolas {c}nem encostam no eixo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
