# Estudativo · MAT-FAV-005 — Quando existe a inversa: função bijetora (Matemática · Funções Avançadas · Função composta e inversa).
# Habilidade: explicar por que y = x² em ℝ não tem inversa (−2 e 2 dão 4) e passa a ter quando x ≥ 0, dizendo se a função é injetora,
#   sobrejetora ou bijetora.
# Pré-requisitos: MAT-FUN-007 (ler um gráfico). Próxima: MAT-FAV-006.
# Questão inédita, criada para esta aula. Parábola (MAT-FUN-016) fora da ficha: o gráfico de x² aparece como "a curva", montado por pontos
#   (MAT-FUN-006, que ensinou o teste da reta vertical). Cálculo da inversa fica para a MAT-FAV-006.
# x² em ℝ → ℝ: (−2)² = 2² = 4 → não injetora · x² = −1 não tem solução → não sobrejetora.
# x ≥ 0 e contradomínio [0, +∞[ → bijetora · inversa: saída 4 → entrada √4 = 2.
# Questão: f(x) = x², domínio [0, +∞[, contradomínio ℝ · só sobe → injetora · −1 nunca sai → não sobrejetora → não bijetora ·
#   conserto: contradomínio [0, +∞[.
# Visual: máquina que desfaz (setas de ida e volta); plano −3..3 × −2..9 com a curva de x² (E.curva), reta horizontal y = 4 cortando em
#   (−2, 4) e (2, 4), reta y = −1 sem tocar; metade da esquerda apagando; diagrama de flechas pequeno; palco escuro no atalho.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.

TITULO = "Quando existe a inversa: função bijetora"

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
    dict(id="s01", block="gancho", text="{a}Pensei num número e elevei ao quadrado. [p=0.2] {b}Deu quatro. [p=0.3] Em que número eu pensei? [p=0.2] {c}Dois? [p=0.2] {d}Menos dois? [p=0.3] Não dá para saber. [p=0.2] E é por isso que {e}essa função não tem inversa."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você descobre quando uma função pode ser desfeita, [p=0.2] com três palavras: {b}injetora, sobrejetora e bijetora. [p=0.2] E leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}domínio, contradomínio e imagem. [p=0.2] O contradomínio é onde as saídas podem cair, [p=0.2] e a imagem é o que de fato sai. [p=0.3] E {b}ler um gráfico: onde ele sobe e onde desce. [p=0.3] Se faltar alguma, procure no canal."),
    # a inversa
    dict(id="s04", block="inversa", text="A função inversa é {a}a máquina que desfaz: [p=0.2] você dá a saída, e ela devolve a entrada. [p=0.3] Para isso funcionar, {b}cada saída tem que vir de uma entrada só, [p=0.2] e {c}toda saída pedida tem que existir. [p=0.3] Cada exigência tem um nome."),
    # injetora
    dict(id="s05", block="injetora", text="A primeira é ser {a}injetora: [p=0.2] {b}entradas diferentes dão saídas diferentes. [p=0.3] Ípsilon igual a xis ao quadrado falha: [p=0.2] {c}menos dois e dois são entradas diferentes, [p=0.2] e {d}ambas dão quatro."),
    dict(id="s06", block="injetora", text="No gráfico, isso aparece com {a}uma reta horizontal. [p=0.2] {b}Na altura quatro, ela corta a curva em dois pontos: [p=0.2] {c}em xis menos dois e em xis dois. [p=0.3] {d}Se alguma reta horizontal corta o gráfico mais de uma vez, a função não é injetora."),
    # sobrejetora
    dict(id="s07", block="sobrejetora", text="A segunda é ser {a}sobrejetora: [p=0.2] {b}a imagem é o contradomínio inteiro. [p=0.2] Ou seja, toda saída que a função promete, ela entrega."),
    dict(id="s08", block="sobrejetora", text="Agora, use {a}todos os reais como contradomínio. [p=0.2] Ele tem os negativos. [p=0.2] Mas {b}nenhum número ao quadrado dá menos um. [p=0.2] {c}A reta horizontal na altura menos um não toca a curva. [p=0.2] {d}Não é sobrejetora."),
    # bijetora
    dict(id="s09", block="bijetora", text="Quando a função é injetora e sobrejetora ao mesmo tempo, ela é {a}bijetora. [p=0.2] {b}Só a bijetora tem inversa."),
    dict(id="s10", block="bijetora", text="Dá para consertar o xis ao quadrado. [p=0.2] {a}Fique só com xis maior ou igual a zero: [p=0.2] {b}some a metade da esquerda, [p=0.2] e cada altura passa a ser tocada uma vez só. [p=0.2] {c}Agora é injetora."),
    dict(id="s11", block="bijetora", text="E troque o contradomínio por {a}de zero até mais infinito, fechado no zero. [p=0.2] {b}Toda saída prometida aparece. [p=0.2] {c}Bijetora. [p=0.3] E a inversa você já conhece: [p=0.2] {d}saiu quatro, a entrada foi a raiz quadrada de quatro, dois."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}usar a reta vertical. [p=0.2] {b}A reta vertical testa se o desenho é uma função: [p=0.2] cada xis com uma saída só. [p=0.3] {c}Xis ao quadrado passa nesse teste, [p=0.2] e mesmo assim não é injetora. [p=0.3] Para injetora, {d}a reta é horizontal."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: {a}veja se o gráfico só sobe ou só desce. [p=0.3] {b}Se ele nunca muda de direção, nenhuma altura se repete: [p=0.2] é injetora, sem testar ponto nenhum. [p=0.3] {c}Xis ao quadrado desce e depois sobe, [p=0.2] e as alturas se repetem."),
    dict(id="s14", block="atalho", text="{a}O atalho só responde se é injetora. [p=0.2] Para saber se é sobrejetora, [p=0.2] {b}compare sempre a imagem com o contradomínio."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] A função é {a}éfe de xis igual a xis ao quadrado, [p=0.2] com domínio {b}de zero até mais infinito [p=0.2] e contradomínio {c}todos os reais. [p=0.3] {d}Ela é injetora? Sobrejetora? Bijetora?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Com xis só de zero para cima, o gráfico só sobe: [p=0.2] {b}é injetora. [p=0.3] Mas o contradomínio tem os negativos, [p=0.2] e {c}nenhum quadrado dá negativo. [p=0.2] {d}Não é sobrejetora. [p=0.2] Então, {e}não é bijetora."),
    dict(id="s18", block="resposta", text="O conserto é {a}trocar o contradomínio por de zero até mais infinito. [p=0.2] {b}Mesma lei, mesmo desenho, [p=0.2] e agora ela é bijetora. [p=0.3] {c}O contradomínio faz parte da função."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}injetora não repete saída, [p=0.2] {b}sobrejetora entrega todo o contradomínio, [p=0.2] e {c}bijetora é as duas coisas: só ela tem inversa."),
    dict(id="s20", block="fim", text="Na próxima aula, você aprende a {a}calcular a inversa, [p=0.2] e vê que o gráfico dela é {b}um espelho do gráfico original. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
