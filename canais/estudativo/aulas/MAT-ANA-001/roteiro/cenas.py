# Estudativo · MAT-ANA-001 — Distância entre dois pontos (Matemática · Geometria Analítica · Pontos no plano).
# Habilidade: achar a distância entre (1, 2) e (4, 6) pelo triângulo retângulo (5).
# Pré-requisitos: MAT-FUN-001 (plano cartesiano: corredor e elevador), MAT-ANG-015 (Pitágoras). Próxima: MAT-ANA-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Pares narrados "xis um, ípsilon dois", como na MAT-FUN-001. Letra d narrada "dê".
# Delta (MAT-FUN-010) não está na ficha desta aula: diga "diferença dos xis" e "diferença dos ípsilons".

TITULO = "Distância entre dois pontos"

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
    dict(id="s01", block="gancho", text="{a}No mapa de um aplicativo, sua casa fica em {b}xis um, ípsilon dois, [p=0.2] e o mercado em {c}xis quatro, ípsilon seis, [p=0.2] com cada quadradinho valendo um quilômetro. [p=0.3] {d}Qual é a distância em linha reta? [p=0.3] Não é {e}sete. [p=0.2] É {f}cinco."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a distância entre quaisquer dois pontos do plano, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o plano cartesiano, primeiro o corredor, que é o xis, depois o elevador, que é o ípsilon; [p=0.2] e {c}o teorema de Pitágoras: num triângulo retângulo, a hipotenusa ao quadrado é a soma dos quadrados dos catetos. [p=0.3] Se faltar alguma, procure no canal."),
    # o triângulo escondido
    dict(id="s04", block="triangulo", text="Marque {a}os pontos da casa e do mercado [p=0.2] e ligue com {b}um segmento: é a distância que você quer. [p=0.3] Agora, saia da casa pelo corredor, {c}andando na horizontal, [p=0.2] e depois {d}suba pelo elevador até o mercado."),
    dict(id="s05", block="triangulo", text="Esse caminho desenha {a}um triângulo retângulo. [p=0.2] O canto é reto porque {b}o corredor e o elevador se cruzam em ângulo reto. [p=0.3] {c}Os catetos são o corredor e o elevador. [p=0.2] {d}A hipotenusa é a distância em linha reta."),
    dict(id="s06", block="triangulo", text="Quanto mede cada cateto? [p=0.2] {a}No corredor, o xis vai de um até quatro: [p=0.2] quatro menos um dá três. [p=0.3] {b}No elevador, o ípsilon vai de dois até seis: [p=0.2] seis menos dois dá quatro."),
    dict(id="s07", block="triangulo", text="Agora é Pitágoras. [p=0.2] {a}Três ao quadrado dá nove. [p=0.2] {b}Quatro ao quadrado dá dezesseis. [p=0.2] {c}Somando, dá vinte e cinco. [p=0.2] {d}A raiz de vinte e cinco dá cinco. [p=0.3] {e}Cinco quilômetros em linha reta."),
    # regra
    dict(id="s08", block="regra", text="Vale para quaisquer dois pontos: [p=0.2] {a}a distância ao quadrado é a diferença dos xis ao quadrado, [p=0.2] mais {b}a diferença dos ípsilons ao quadrado. [p=0.3] {c}No fim, tire a raiz. [p=0.3] Na tela, a fórmula como aparece nos livros: [p=0.2] {d}o dê é a distância, [p=0.2] e {e}os números pequenos dizem de qual ponto é cada coordenada."),
    # com negativos
    dict(id="s09", block="negativos", text="E com números negativos? [p=0.2] Vamos achar a distância entre {a}xis menos dois, ípsilon um, [p=0.2] e {b}xis quatro, ípsilon menos sete."),
    dict(id="s10", block="negativos", text="{a}Diferença dos xis: quatro menos, abre parênteses, menos dois. [p=0.2] Menos com menos vira mais: {b}quatro mais dois dá seis. [p=0.3] {c}Diferença dos ípsilons: menos sete menos um dá menos oito."),
    dict(id="s11", block="negativos", text="O menos oito não atrapalha: [p=0.2] {a}menos oito ao quadrado dá sessenta e quatro, positivo. [p=0.2] {b}Seis ao quadrado dá trinta e seis. [p=0.2] {c}Trinta e seis mais sessenta e quatro dá cem. [p=0.2] {d}A raiz de cem dá dez."),
    # erro
    dict(id="s12", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}somar os catetos sem Pitágoras. [p=0.3] No mapa do começo, a pessoa faz {b}três mais quatro, que dá sete, e responde sete quilômetros. [p=0.3] Sete é {c}o caminho pelas ruas: corredor e depois elevador."),
    dict(id="s13", block="erro", text="A linha reta é {a}a hipotenusa, sempre mais curta que a volta pelos catetos. [p=0.2] {b}Cinco é menor que sete. [p=0.3] {c}Some os quadrados, e só depois tire a raiz."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para fugir do sinal: [p=0.2] {a}cada diferença é só quantos passos separam os pontos. [p=0.3] {b}Com sinais diferentes, some os tamanhos: [p=0.2] de menos dois até quatro, {c}dois mais quatro dá seis passos. [p=0.3] {d}Com sinais iguais, subtraia: [p=0.2] de dois até seis, {e}seis menos dois dá quatro passos."),
    dict(id="s15", block="atalho", text="Funciona porque, com sinais diferentes, {a}o zero fica no meio: [p=0.2] você anda até o zero e depois passa dele. [p=0.3] E o sinal da diferença {b}não importa, porque o quadrado apaga o sinal. [p=0.3] {c}Não compensa quando a questão já traz o quadriculado: [p=0.2] aí, conte os quadradinhos."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Num mapa em quilômetros, {a}a escola fica em xis menos três, ípsilon menos um, [p=0.2] e {b}o hospital em xis dois, ípsilon onze. [p=0.3] {c}Qual é a distância em linha reta entre eles?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Nos xis, de menos três até dois: sinais diferentes, [p=0.2] três mais dois dá cinco. [p=0.3] {b}Nos ípsilons, de menos um até onze: [p=0.2] um mais onze dá doze."),
    dict(id="s19", block="resposta", text="{a}Cinco ao quadrado dá vinte e cinco. [p=0.2] {b}Doze ao quadrado dá cento e quarenta e quatro. [p=0.2] {c}Somando, dá cento e sessenta e nove. [p=0.2] {d}A raiz dá treze: [p=0.2] {e}treze quilômetros. [p=0.3] A volta pelas ruas seria {f}cinco mais doze, que dá dezessete. [p=0.2] Treze é menos: faz sentido."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}desenhe o triângulo, [p=0.2] {b}os catetos são as diferenças dos xis e dos ípsilons, [p=0.2] e {c}a distância é a hipotenusa."),
    dict(id="s21", block="fim", text="Na próxima aula, você acha {a}o ponto exatamente no meio de dois pontos [p=0.2] e {b}o ponto de equilíbrio de um triângulo, [p=0.2] com contas de cabeça. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
