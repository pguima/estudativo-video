# Estudativo · MAT-ESP-004 — Retas e planos no espaço (Matemática · Geometria Espacial).
# Habilidade: dizer, olhando as arestas de uma caixa, quais são paralelas, concorrentes ou reversas e quando uma reta é perpendicular a um plano.
# Pré-requisitos: MAT-ANG-003 (paralelas, concorrentes, perpendiculares no plano), MAT-ESP-001 (aresta, face, paralelepípedo). Próxima: MAT-ESP-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Arestas nomeadas pela posição, sem letras (a letra "é" soaria como verbo). Caixa: largura da esquerda para a direita, profundidade da frente para o fundo.
# Aresta escolhida (s05–s09): a da frente, embaixo, deitada da esquerda para a direita.

TITULO = "Retas e planos no espaço"

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
    dict(id="s01", block="gancho", text="{a}Duas retas que nunca se encontram são paralelas? [p=0.3] No papel, sim. [p=0.2] {b}Numa caixa, nem sempre. [p=0.3] Existe {c}um terceiro tipo de reta, que só aparece fora do papel."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você olha duas arestas de uma caixa e diz a posição delas, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}no papel, retas que se cruzam são concorrentes, e, se o cruzamento tem ângulo reto, são perpendiculares; [p=0.2] e {c}aresta é o encontro de duas faces de um sólido. [p=0.3] Se faltar alguma, procure no canal."),
    # plano
    dict(id="s04", block="plano", text="Primeiro, {a}o plano. [p=0.2] É como {b}uma folha de papel sem bordas, que se estende para todos os lados. [p=0.3] {c}O chão, uma parede, o tampo da mesa: [p=0.2] cada um é um pedaço de plano. [p=0.2] Numa caixa, {d}cada face está num plano."),
    # posições
    dict(id="s05", block="posicoes", text="Pegue {a}uma caixa de sapato fechada. [p=0.2] Escolha {b}a aresta da frente, embaixo, deitada da esquerda para a direita. [p=0.3] Vamos comparar essa aresta com as outras."),
    dict(id="s06", block="posicoes", text="{a}A aresta da frente, em cima, nunca encontra a escolhida. [p=0.2] Elas apontam {b}na mesma direção [p=0.2] e estão {c}na mesma face, a da frente. [p=0.3] São {d}paralelas: no espaço, paralelas não se cruzam e ficam no mesmo plano."),
    dict(id="s07", block="posicoes", text="{a}A aresta em pé, no canto da frente à direita, toca a escolhida na ponta. [p=0.2] Elas se cruzam num ponto: {b}são concorrentes. [p=0.2] E, como a caixa tem cantos retos, {c}são também perpendiculares."),
    dict(id="s08", block="posicoes", text="Agora {a}a aresta em pé, no canto de trás, à esquerda. [p=0.2] Ela {b}nunca encontra a escolhida, por mais que você estique as duas. [p=0.2] Mas {c}não apontam na mesma direção: [p=0.2] uma vai para o lado, a outra sobe."),
    dict(id="s09", block="posicoes", text="São {a}retas reversas: [p=0.2] {b}não se cruzam e não estão no mesmo plano. [p=0.3] Não existe {c}folha nenhuma que passe pelas duas ao mesmo tempo. [p=0.2] Esse é o tipo que {d}só existe no espaço."),
    # reta perpendicular ao plano
    dict(id="s10", block="perpendicular", text="E uma reta com um plano? [p=0.2] {a}A aresta em pé, no canto da frente à direita, chega ao chão da caixa [p=0.2] como {b}um poste chega à calçada. [p=0.3] Ela faz {c}ângulo reto com as duas arestas do chão que saem do pé dela."),
    dict(id="s11", block="perpendicular", text="Por isso ela é {a}perpendicular ao plano do chão: [p=0.2] {b}faz ângulo reto com toda reta do chão que passa pelo pé dela. [p=0.3] Para testar, {c}bastam duas retas do plano que se cruzam no pé. [p=0.2] Ângulo reto com as duas, {d}perpendicular ao plano."),
    dict(id="s12", block="perpendicular", text="E por que precisa de duas retas? [p=0.2] {a}Um poste torto, inclinado para a frente, [p=0.2] ainda faz ângulo reto com {b}a linha da calçada que corre de lado, no pé dele. [p=0.2] Mas, com {c}a linha que vai para a frente, não. [p=0.3] {d}Uma reta só não garante."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}chamar de paralelas quaisquer retas que não se encontram. [p=0.2] A aresta deitada da frente e a aresta em pé lá de trás {b}nunca se encontram. [p=0.2] Mas {c}uma vai para o lado e a outra sobe. [p=0.3] Para serem paralelas, {d}não basta não se cruzar: precisam estar no mesmo plano."),
    # atalho
    dict(id="s14", block="atalho", text="E o atalho: {a}duas perguntas, nesta ordem. [p=0.3] {b}Elas se cruzam, mesmo esticando? [p=0.2] Concorrentes. [p=0.2] {c}Não se cruzam, mas apontam na mesma direção? [p=0.2] Paralelas. [p=0.2] {d}Nenhuma das coisas? [p=0.2] Reversas."),
    dict(id="s15", block="atalho", text="E, para conferir, numa caixa {a}cada aresta tem três paralelas, quatro concorrentes e quatro reversas. [p=0.3] As paralelas são {b}as outras três da mesma direção. [p=0.2] As concorrentes, {c}duas em cada ponta. [p=0.2] {d}O que sobra das onze é reversa."),
    dict(id="s16", block="atalho", text="Funciona porque {a}a caixa só tem três direções: para o lado, para o fundo e para cima, [p=0.2] com quatro arestas em cada uma. [p=0.3] {b}Essa conta não vale numa pirâmide: [p=0.2] lá, as arestas apontam para muitas direções, e {c}você usa só as duas perguntas."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Na mesma caixa, pegue {a}a aresta em pé, no canto da frente à esquerda. [p=0.3] Qual a posição dela com: [p=0.2] {b}a aresta de cima, no fundo, deitada da esquerda para a direita? [p=0.2] {c}A aresta em pé, no canto de trás à direita? [p=0.2] E {d}a aresta de cima, do lado esquerdo, que vai da frente para o fundo?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=0.2] Vale apontar as arestas de uma caixa de verdade. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}A aresta de cima, no fundo, não toca a escolhida, [p=0.2] e uma vai para o lado enquanto a outra sobe. [p=0.2] {b}Reversas."),
    dict(id="s20", block="resposta", text="{a}A aresta em pé, de trás à direita, também não toca, [p=0.2] mas {b}sobe na mesma direção. [p=0.2] {c}Paralelas. [p=0.3] {d}A aresta de cima, do lado esquerdo, encosta no topo da escolhida: [p=0.2] {e}concorrentes, e também perpendiculares."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}se cruzam, concorrentes; [p=0.2] {b}mesma direção, paralelas; [p=0.2] {c}nenhum dos casos, reversas. [p=0.3] E {d}reta perpendicular a um plano faz ângulo reto com duas retas dele que se cruzam no seu pé."),
    dict(id="s22", block="fim", text="Na próxima aula, você enche essa caixa: [p=0.2] {a}o volume do cubo e do bloco. [p=0.2] E descobre quantos {b}litros cabem numa caixa de dois metros por um metro e meio por um metro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
