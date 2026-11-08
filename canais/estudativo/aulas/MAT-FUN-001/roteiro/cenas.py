# Estudativo · MAT-FUN-001 — Plano cartesiano: marcar e ler pontos (Matemática · Funções · O que é função).
# Habilidade: marcar (3, −2) e (−1, 4), dizer em que quadrante cada ponto está e ler as coordenadas de um lugar num mapa quadriculado.
# Pré-requisitos: MAT-NUM-015 (negativos e reta numérica). Próxima: MAT-FUN-002.
# Questão inédita, criada para esta aula. Sem multiplicação nem frações: fora da ficha desta aula.
# Pontos: (3, −2) no 4º quadrante · (−1, 4) no 2º · (0, 3) no eixo y, sem quadrante · erro: trocar a ordem leva (3, −2) para (−2, 3), 2º quadrante.
# Mapa: praça = origem, 1 quadradinho = 1 quadra · escola (−4, 2), 2º · questão: farmácia (−3, −1), 3º · posto (2, −4), 4º.
# Pares narrados como "xis três, ípsilon menos dois" (vírgula entre dois números funde os números na voz).
# Visual: plano cartesiano (E.plano) com eixos x e y; pontos com guias (E.ponto); setas "corredor" (deitada) e "elevador" (em pé);
#   quadrantes numerados I a IV com os sinais (+, +), (−, +), (−, −), (+, −); mapa quadriculado com praça, escola, farmácia e posto.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Plano cartesiano: marcar e ler pontos"

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
    dict(id="s01", block="gancho", text="{a}Xis três, ípsilon menos dois. [p=0.3] {b}Xis menos dois, ípsilon três. [p=0.3] São os mesmos números, [p=0.2] mas {c}lugares bem diferentes no mapa. [p=0.3] Quem troca a ordem chega no endereço errado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você marca e lê qualquer ponto, [p=0.2] diz em que {b}quadrante ele está [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa só: [p=0.2] {b}a reta numérica. [p=0.2] O sinal diz o lado, [p=0.2] e o número diz quantos passos. [p=0.3] Se faltar, procure no canal."),
    # eixos
    dict(id="s04", block="eixos", text="Pegue {a}duas retas numéricas. [p=0.2] Uma fica {b}deitada, como sempre. [p=0.2] A outra fica {c}em pé, cruzando a primeira bem no zero. [p=0.3] Na reta em pé, {d}os positivos ficam para cima [p=0.2] e {e}os negativos, para baixo."),
    dict(id="s05", block="eixos", text="A reta deitada é o {a}eixo xis. [p=0.2] A reta em pé é o {b}eixo ípsilon. [p=0.2] O ponto onde elas se cruzam é a {c}origem: [p=0.2] o zero de cada eixo. [p=0.3] Juntas, elas formam o {d}plano cartesiano, [p=0.2] uma grade em que cada lugar tem um endereço."),
    # endereço
    dict(id="s06", block="endereco", text="O endereço de um ponto são {a}dois números entre parênteses. [p=0.3] {b}O primeiro é o xis: quantos passos para a direita ou para a esquerda. [p=0.2] {c}O segundo é o ípsilon: quantos passos para cima ou para baixo. [p=0.3] Esses números se chamam {d}coordenadas do ponto."),
    dict(id="s07", block="endereco", text="Para não esquecer a ordem, pense num prédio: [p=0.2] {a}primeiro você anda pelo corredor, [p=0.2] {b}depois pega o elevador. [p=0.3] O corredor é o xis, deitado. [p=0.2] O elevador é o ípsilon, em pé."),
    # marcar
    dict(id="s08", block="marcar", text="Vamos marcar {a}xis três, ípsilon menos dois. [p=0.3] {b}Saia da origem. [p=0.2] O xis é três, positivo: {c}três passos para a direita. [p=0.2] O ípsilon é menos dois, negativo: {d}dois passos para baixo. [p=0.3] {e}O ponto fica ali."),
    dict(id="s09", block="marcar", text="Outro ponto: {a}xis menos um, ípsilon quatro. [p=0.2] {b}Um passo para a esquerda. [p=0.2] {c}Quatro para cima. [p=0.3] E se uma coordenada for zero? [p=0.2] {d}Xis zero, ípsilon três: [p=0.2] você não anda pelo corredor, só sobe. [p=0.2] O ponto fica {e}em cima do eixo ípsilon."),
    # quadrantes
    dict(id="s10", block="quadrantes", text="Os eixos cortam o plano em {a}quatro partes, os quadrantes. [p=0.3] A contagem começa {b}em cima, à direita: primeiro quadrante. [p=0.2] E gira para a esquerda, {c}ao contrário do relógio. [p=0.2] {d}Segundo, em cima à esquerda. [p=0.2] {e}Terceiro, embaixo à esquerda. [p=0.2] {f}Quarto, embaixo à direita."),
    dict(id="s11", block="quadrantes", text="{a}O ponto xis três, ípsilon menos dois, foi para a direita e para baixo: [p=0.2] {b}quarto quadrante. [p=0.3] {c}O ponto xis menos um, ípsilon quatro, foi para a esquerda e para cima: [p=0.2] {d}segundo quadrante. [p=0.3] E {e}ponto em cima de um eixo não está em quadrante nenhum: [p=0.2] ele fica na divisa."),
    # ler
    dict(id="s12", block="mapa", text="Também dá para fazer o caminho de volta: [p=0.2] {a}ler o endereço de um ponto. [p=0.3] Num mapa quadriculado, a {b}praça é a origem, [p=0.2] e cada quadradinho é {c}uma quadra. [p=0.3] Onde está {d}a escola?"),
    dict(id="s13", block="mapa", text="Do ponto da escola, {a}desça em linha reta até o eixo xis: [p=0.2] ele marca {b}menos quatro. [p=0.2] Depois, volte à escola e {c}vá de lado até o eixo ípsilon: [p=0.2] ele marca {d}dois. [p=0.3] Endereço da escola: {e}xis menos quatro, ípsilon dois, [p=0.2] no segundo quadrante."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}começar pelo elevador. [p=0.2] Para marcar xis três, ípsilon menos dois, [p=0.2] a pessoa sobe {b}três passos e anda dois para a esquerda. [p=0.3] Cai no ponto {c}xis menos dois, ípsilon três, [p=0.2] lá no {d}segundo quadrante, longe do certo. [p=0.3] {e}A ordem dentro do parêntese nunca muda: primeiro o xis, depois o ípsilon."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}descubra o quadrante só pelos sinais, sem desenhar. [p=0.3] {b}Primeiro quadrante: mais e mais. [p=0.2] {c}Segundo: menos e mais. [p=0.2] {d}Terceiro: menos e menos. [p=0.2] {e}Quarto: mais e menos."),
    dict(id="s16", block="atalho", text="Funciona porque {a}o sinal do xis diz direita ou esquerda, [p=0.2] e {b}o sinal do ípsilon diz cima ou baixo. [p=0.3] {c}Não compensa quando uma coordenada é zero: [p=0.2] aí não tem sinal, o ponto está num eixo [p=0.2] e {d}não tem quadrante."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar, no mesmo mapa. [p=0.2] {a}A farmácia fica em xis menos três, ípsilon menos um. [p=0.2] {b}Em que quadrante ela está? [p=0.3] E {c}o posto é o ponto marcado na tela. [p=0.2] {d}Qual é o endereço dele, e em que quadrante fica?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] A farmácia tem {a}menos e menos: [p=0.2] {b}terceiro quadrante, embaixo à esquerda. [p=0.3] No posto, {c}suba em linha reta até o eixo xis: dois. [p=0.2] {d}Volte ao posto e vá de lado até o eixo ípsilon: menos quatro. [p=0.3] Endereço: {e}xis dois, ípsilon menos quatro. [p=0.2] Mais e menos: {f}quarto quadrante."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}primeiro o corredor, depois o elevador, [p=0.2] e {b}os sinais dizem o quadrante."),
    dict(id="s21", block="fim", text="Na próxima aula, você conhece a ideia que dá nome a esta trilha: [p=0.2] {a}função, [p=0.2] uma regra em que {b}cada entrada tem uma saída só, [p=0.2] como no {c}preço de uma corrida de táxi. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
