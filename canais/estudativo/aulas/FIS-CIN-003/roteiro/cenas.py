# Estudativo · FIS-CIN-003 — Decompor um vetor nos eixos (Física · Cinemática · Queda livre e lançamentos).
# Habilidade: calcular as componentes x e y de um vetor com seno e cosseno e somar vetores pelo método dos eixos.
# Pré-requisitos: FIS-CIN-002 (soma de vetores), MAT-TRI-002 (sen 37° = 0,6; cos 37° = 0,8), MAT-TRI-003 (notáveis). Próxima: FIS-CIN-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Na trilha, vem depois de FIS-CIN-015, mas o "Já ensinado" de Física só tem 001 e 002:
# nada de queda livre nem lançamento horizontal aqui; o lançamento oblíquo só aparece como próxima aula.

TITULO = "Decompor um vetor nos eixos"

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
    dict(id="s01", block="gancho", text="{a}Uma bola é chutada a vinte metros por segundo, [p=0.2] inclinada em relação ao chão. [p=0.3] Ela não avança vinte metros por segundo: [p=0.2] {b}só dezesseis. [p=0.3] E {c}sobe a doze. [p=0.3] {d}Dezesseis mais doze dá vinte e oito, e não vinte. [p=0.2] E está tudo certo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dividir um vetor numa parte {b}deitada e numa {c}em pé, [p=0.2] e somar vetores inclinados {d}pelo método dos eixos."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}somar vetores em ângulo reto com Pitágoras; [p=0.2] {c}achar um cateto com seno e cosseno, como o seno de trinta e sete graus, zero vírgula seis, e o cosseno, zero vírgula oito; [p=0.2] e {d}os ângulos notáveis, trinta, quarenta e cinco e sessenta graus. [p=0.3] Se faltar alguma, procure no canal."),
    # decompor
    dict(id="s04", block="decompor", text="Na aula de soma, {a}dois vetores em ângulo reto viravam um só: a hipotenusa. [p=0.3] Decompor é {b}o caminho de volta: [p=0.2] trocar um vetor inclinado por {c}dois, um em cada eixo, [p=0.2] que somados fazem o mesmo efeito. [p=0.3] Eles se chamam {d}componentes."),
    dict(id="s05", block="decompor", text="Ponha o começo do vetor no cruzamento de {a}dois eixos: [p=0.1] {b}o xis, deitado, [p=0.1] e {c}o ípsilon, em pé. [p=0.3] {d}Trace a sombra da ponta em cada eixo. [p=0.2] Aparece {e}um triângulo retângulo: [p=0.2] {f}o vetor é a hipotenusa, e as componentes são os catetos."),
    dict(id="s06", block="decompor", text="O ângulo, que se chama teta, fica {a}entre o vetor e o eixo xis. [p=0.3] {b}A componente xis encosta no ângulo: é o cateto adjacente. [p=0.2] {c}Vê xis é vê vezes o cosseno de teta. [p=0.3] {d}A componente ípsilon fica de frente para o ângulo: é o oposto. [p=0.2] {e}Vê ípsilon é vê vezes o seno de teta."),
    # exemplos
    dict(id="s07", block="bola", text="Na bola: {a}vinte metros por segundo, a trinta e sete graus do chão. [p=0.3] {b}Vê xis: vinte vezes zero vírgula oito, dezesseis. [p=0.2] {c}Vê ípsilon: vinte vezes zero vírgula seis, doze. [p=0.3] {d}Confira com Pitágoras: [p=0.1] duzentos e cinquenta e seis mais cento e quarenta e quatro, [p=0.1] quatrocentos: {e}vinte ao quadrado."),
    dict(id="s08", block="bola", text="Por isso dezesseis mais doze não dá vinte: [p=0.2] {a}as componentes estão em ângulo reto, e não se somam em fila. [p=0.3] Com ângulo notável, o jeito é o mesmo. [p=0.2] {b}Um vetor de dez, a sessenta graus. [p=0.2] {c}Xis: dez vezes o cosseno de sessenta, um meio: cinco. [p=0.2] {d}Ípsilon: dez vezes o seno de sessenta, raiz de três dividido por dois: cinco raiz de três."),
    # método dos eixos
    dict(id="s09", block="eixos", text="E para somar vetores inclinados, {a}o método dos eixos. [p=0.2] {b}Decomponha cada vetor. [p=0.1] {c}Some todos os xis, [p=0.1] {d}some todos os ípsilon, [p=0.1] com sinal: para a esquerda ou para baixo, entra com menos. [p=0.2] {e}No fim, junte as duas somas com Pitágoras."),
    dict(id="s10", block="eixos", text="Um drone faz {a}dois deslocamentos: [p=0.2] {b}dez metros, subindo a trinta e sete graus com o chão, [p=0.2] e depois {c}nove metros na vertical, para cima. [p=0.3] {d}Xis: oito do primeiro, nada do segundo: oito. [p=0.2] {e}Ípsilon: seis mais nove, quinze. [p=0.3] {f}Pitágoras: sessenta e quatro mais duzentos e vinte e cinco, duzentos e oitenta e nove. [p=0.2] {g}A raiz é dezessete metros."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: {a}usar sempre o cosseno no xis, sem olhar onde está o ângulo. [p=0.3] {b}Se a prova dá o ângulo com a vertical, tudo troca: [p=0.2] {c}o cosseno vai para o ípsilon, e o seno, para o xis. [p=0.3] {d}A regra certa: o cosseno fica com o eixo que encosta no ângulo."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}trinta e sete e cinquenta e três graus são o triângulo três, quatro, cinco. [p=0.3] {b}Divida o vetor por cinco. [p=0.2] {c}Com trinta e sete graus, quatro partes vão para o eixo que encosta no ângulo. [p=0.2] {d}Três partes vão para o outro. [p=0.2] Com cinquenta e três, é ao contrário. [p=0.3] {e}Vinte dividido por cinco, quatro: [p=0.1] dezesseis e doze."),
    dict(id="s13", block="atalho", text="Funciona porque {a}zero vírgula oito é quatro quintos, e zero vírgula seis é três quintos. [p=0.3] {b}Não serve para trinta, quarenta e cinco ou sessenta graus: [p=0.2] aí, use a tabela dos notáveis."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma bola é chutada a {a}vinte e cinco metros por segundo, [p=0.1] a {b}trinta e sete graus do chão. [p=0.3] {c}Quais são as componentes deitada e em pé? [p=0.2] {d}E se os trinta e sete graus fossem com a vertical?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Vinte e cinco dividido por cinco, cinco. [p=0.2] {b}O ângulo é com o chão, então o eixo que encosta nele é o xis: [p=0.1] {c}cinco vezes quatro, vinte metros por segundo. [p=0.2] {d}No ípsilon, cinco vezes três, quinze. [p=0.3] {e}Confira: quinze, vinte e vinte e cinco formam o três, quatro, cinco, vezes cinco."),
    dict(id="s17", block="resposta", text="{a}Com o ângulo na vertical, o eixo que encosta nele é o ípsilon. [p=0.2] {b}Tudo troca: vinte para cima, [p=0.1] {c}quinze para a frente."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}as componentes são os catetos; [p=0.2] {b}o eixo que encosta no ângulo leva o cosseno; [p=0.2] {c}para somar, some os xis, some os ípsilon e feche com Pitágoras."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai usar isso no {a}lançamento oblíquo: [p=0.2] {b}a parte deitada da velocidade leva a bola para a frente, [p=0.1] e {c}a parte em pé, para cima. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
