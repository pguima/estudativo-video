# Estudativo · MAT-FUN-008 — Praticando: o que é função (Matemática · Funções · O que é função · prática).
# Habilidade: ler funções em fórmulas, tabelas e gráficos e responder se a pergunta pede o x ou o y.
# Pré-requisitos: MAT-FUN-001 a MAT-FUN-007. Próxima: MAT-FUN-009.
# Questões inéditas, criadas para esta aula. Função afim ainda não foi ensinada (MAT-FUN-009): a fórmula aparece só como regra de cálculo.
# Situação 1: C(n) = 20 + 0,5n · C(100) = 70 · C(n) = 45 → 0,5n = 25 → n = 50.
# Situação 2: tabela A (x 1, 2, 3, 4 → y 5, 5, 7, 9) é função · tabela B (x 1, 1, 2, 3 → y 2, 4, 6, 8) não é · o V (ponta para baixo) passa no teste da reta vertical: é função.
# Situação 3: f(x) = √(x − 5) → x ≥ 5 → [5, +∞[ · g(x) = 1/(x + 2) → x ≠ −2 · teste: x = 4 dá √(−1), fora.
# Situação 4: reservatório (x = hora, y = mil litros): (0, 4), (4, 8), (10, 2), (12, 3), trechos retos ·
#   máximo 8 às 4 h · 6 mil litros às 2 h e às 6 h · imagem [2, 8].
# Visual: fórmula com caixas "entrada" e "saída"; duas tabelas lado a lado; V no plano com reta vertical tocando um ponto só;
#   reta numérica com o intervalo [5, +∞[; plano (E.plano) com o gráfico do reservatório (E.curva por trechos), reta horizontal y = 6
#   tracejada cortando a curva em dois pontos com guias (E.ponto).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: o que é função"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, criadas para esta aula: [p=0.2] uma {b}fórmula, [p=0.1] {c}tabelas, [p=0.1] um {d}domínio [p=0.1] e um {e}gráfico. [p=0.3] Em cada uma, {f}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Antes de cada conta, faça {a}uma pergunta: [p=0.2] {b}o número que eu tenho é a entrada, o xis, [p=0.2] {c}ou a saída, o ípsilon? [p=0.3] Essa pergunta decide o caminho. [p=0.2] Se alguma ideia travar, procure a aula no canal."),
    # situação 1: fórmula
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma gráfica cobra {b}vinte reais fixos, mais cinquenta centavos por cópia. [p=0.3] O preço é {c}cê de ene igual a vinte mais zero vírgula cinco vezes ene, [p=0.2] em que ene é o número de cópias. [p=0.3] {d}Quanto custam cem cópias? [p=0.2] E {e}com quarenta e cinco reais, quantas cópias dá para fazer?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Na primeira, cem é {a}o número de cópias: a entrada. [p=0.2] É só calcular: [p=0.2] {b}zero vírgula cinco vezes cem dá cinquenta. [p=0.2] {c}Mais vinte: setenta reais."),
    dict(id="s06", block="resposta1", text="Na segunda, quarenta e cinco é {a}o preço: a saída. [p=0.2] Agora é o caminho de volta, com uma equação: [p=0.2] {b}vinte mais zero vírgula cinco vezes ene igual a quarenta e cinco. [p=0.3] {c}Tire vinte de cada lado: zero vírgula cinco vezes ene igual a vinte e cinco. [p=0.2] {d}Divida por zero vírgula cinco: cinquenta cópias."),
    dict(id="s07", block="resposta1", text="Aqui cabe um atalho: [p=0.2] {a}zero vírgula cinco é metade. [p=0.2] Se metade do ene é vinte e cinco, [p=0.2] {b}o ene é o dobro: cinquenta. [p=0.3] Confira: {c}cinquenta cópias custam vinte e cinco reais. [p=0.2] Com os vinte fixos, dá quarenta e cinco. [p=0.2] Bateu. [p=0.3] {d}Quem colocasse quarenta e cinco no lugar do ene [p=0.2] responderia um preço, e a pergunta queria cópias."),
    # situação 2: é função?
    dict(id="s08", block="questao2", text="{a}Situação dois. [p=0.2] Quais destas três são função? [p=0.3] {b}Na tabela A, o um vai no cinco. [p=0.1] O dois vai no cinco. [p=0.1] O três vai no sete. [p=0.1] E o quatro vai no nove. [p=0.3] {c}Na tabela B, o um vai no dois. [p=0.1] O um também vai no quatro. [p=0.1] O dois vai no seis. [p=0.1] E o três vai no oito. [p=0.3] E {d}a terceira é um vê no plano, com a ponta para baixo, como a letra."),
    dict(id="s09", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="resposta2", text="Vamos lá. [p=0.2] A regra é {a}cada entrada com uma saída só. [p=0.3] Na tabela A, {b}o cinco aparece duas vezes, [p=0.2] mas como saída. [p=0.2] {c}Entradas diferentes podem dar a mesma saída. [p=0.2] Cada entrada tem uma saída só: {d}é função."),
    dict(id="s11", block="resposta2", text="Na tabela B, {a}a entrada um tem duas saídas: dois e quatro. [p=0.2] {b}Não é função. [p=0.3] No vê, use {c}o teste da reta vertical. [p=0.2] Uma reta em pé, em qualquer lugar, {d}toca o vê uma vez só: [p=0.2] cada xis com um ípsilon. [p=0.2] {e}É função, mesmo com a ponta."),
    # situação 3: domínio pela fórmula
    dict(id="s12", block="questao3", text="{a}Situação três. [p=0.2] Qual é o domínio de {b}efe de xis igual à raiz quadrada de xis menos cinco, [p=0.2] com o xis menos cinco todo dentro da raiz? [p=0.3] Escreva {c}como intervalo. [p=0.2] E {d}qual número fica fora do domínio de gê de xis igual a um dividido por xis mais dois, [p=0.2] com o xis mais dois todo embaixo?"),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] Raiz quadrada de negativo {a}não dá número da reta. [p=0.2] Então o que está dentro da raiz precisa ser {b}zero ou positivo: [p=0.2] {c}xis menos cinco, maior ou igual a zero. [p=0.2] {d}Some cinco de cada lado: xis maior ou igual a cinco. [p=0.3] Intervalo: {e}de cinco até mais infinito, fechado no cinco."),
    dict(id="s15", block="resposta3", text="Teste um número de fora, como o quatro: [p=0.2] {a}quatro menos cinco dá menos um, [p=0.2] e não existe raiz de menos um na reta. [p=0.3] Em gê de xis, {b}não se divide por zero. [p=0.2] O de baixo zera quando {c}xis vale menos dois. [p=0.2] {d}Menos dois fica fora."),
    # situação 4: gráfico
    dict(id="s16", block="questao4", text="{a}Situação quatro, a última. [p=0.2] O gráfico mostra {b}a água de um reservatório, em mil litros, [p=0.2] {c}das zero às doze horas. [p=0.3] {d}Qual foi o maior volume? [p=0.2] {e}Em que horários ele estava com seis mil litros? [p=0.2] E {f}qual é a imagem?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] O ponto mais alto é {a}xis quatro, ípsilon oito. [p=0.2] A pergunta quer {b}o volume, que é o ípsilon: [p=0.2] {c}oito mil litros, às quatro horas."),
    dict(id="s19", block="resposta4", text="Na segunda, o seis mil é {a}o ípsilon, e a pergunta quer o xis. [p=0.3] {b}Saia do seis no eixo ípsilon e vá de lado. [p=0.2] Você encontra a curva {c}duas vezes: [p=0.2] {d}às duas horas, subindo, [p=0.2] e {e}às seis horas, descendo. [p=0.3] Quem para no primeiro encontro {f}perde metade da resposta."),
    dict(id="s20", block="resposta4", text="Para a imagem, {a}a sombra no eixo ípsilon. [p=0.2] O mais baixo é {b}dois, às dez horas. [p=0.2] O mais alto é {c}oito. [p=0.2] Imagem: {d}de dois a oito, fechado nas pontas."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}veja se o número dado é o xis ou o ípsilon, [p=0.2] {b}faça a conta no sentido certo [p=0.2] e {c}confira com a fórmula ou com o gráfico."),
    dict(id="s22", block="fim", text="Na próxima aula, começa a {a}função afim. [p=0.2] Você escreve {b}a lei de uma corrida de táxi [p=0.2] e descobre que o gráfico dela {c}é uma reta, desenhada com dois pontos só. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
