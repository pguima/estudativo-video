# Estudativo · MAT-EXP-014 — Escalas logarítmicas: pH, Richter e decibéis (Matemática · Exponencial e Logaritmo).
# Habilidade: dizer que pH 3 é 100 vezes mais ácido que pH 5, comparar as amplitudes de terremotos de magnitude 5 e 7 e ler +10 dB como 10 vezes mais intensidade, com a fórmula do enunciado.
# Pré-requisitos: MAT-EXP-009 (propriedades dos logaritmos). Próxima: MAT-EXP-015.
# Questão inédita, criada para esta aula; níveis em decibéis dados como valores criados para a aula. Log 2 (MAT-EXP-010) e gráfico do log (MAT-EXP-013) fora da ficha: log 2 só citado como assunto de outra aula.
# Base dez: log 100 = 2, log 1.000 = 3, log 1.000.000 = 6.
# pH = −log[H⁺] · [H⁺] = 10⁻³ → log = −3 → pH 3 · pH 5 → 10⁻⁵ · 10⁻³ ÷ 10⁻⁵ = 10² = 100.
# Richter M = log(A/A₀) = log A − log A₀ · M₇ − M₅ = log A₇ − log A₅ = log(A₇/A₅) = 2 → A₇/A₅ = 100.
# Decibéis β = 10 · log(I/I₀) · β₂ − β₁ = 10 · log(I₂/I₁) · +10 dB → log = 1 → 10 vezes · +20 dB → 100 vezes.
# Erro: pH 3 contra pH 5 → 5 − 3 = 2 → "duas vezes" (certo: 10 × 10 = 100).
# Atalho: diferença vira expoente do 10 (em dB, dividir por 10 antes): +30 dB → 10³ = 1.000 · não compensa: pH 3 contra 3,3 → 10^0,3 (pede log 2).
# Questão: 90 dB e 60 dB · 90 − 60 = 30 · 30 ÷ 10 = 3 · 10³ = 1.000 vezes · 90 = 60 + metade de 60.
# Visual: régua com saltos ×10 (escala logarítmica) e potências de dez; fórmulas pH = −log[H⁺], M = log(A/A₀), β = 10 · log(I/I₀) com cada letra legendada;
#   dois copos com pH 3 e pH 5 e 10⁻³ ÷ 10⁻⁵ = 10²; dois sismogramas (E.curva em onda) com amplitude 100 vezes maior; barras (E.colunas) de intensidade 1, 10, 100, 1.000.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; pH narrado "pê agá"; letras na tela; narração por nome (amplitude, intensidade, referência), beta, eme.

TITULO = "Escalas logarítmicas: pH, Richter e decibéis"

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
    dict(id="s01", block="gancho", text="{a}Um líquido tem pê agá três. [p=0.2] {b}Outro tem pê agá cinco. [p=0.3] A diferença parece pequena: {c}só dois pontos. [p=0.3] Mas o primeiro é {d}cem vezes mais ácido que o segundo."),
    dict(id="s02", block="gancho", text="Isso acontece porque o pê agá é uma {a}escala logarítmica. [p=0.2] {b}Até o fim desta aula, você compara acidez, terremotos e barulho com a fórmula que a questão der, [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}o logaritmo como expoente, com a base dez escondida quando não aparece; [p=0.2] e {b}as propriedades, como logaritmo de uma divisão virar diferença de logaritmos. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="Por que medir com logaritmo? [p=0.2] Algumas grandezas vão de {a}números minúsculos a números gigantes. [p=0.2] O logaritmo na base dez {b}conta os zeros. [p=0.2] {c}Logaritmo de cem dá dois. [p=0.2] {d}De mil dá três. [p=0.2] {e}De um milhão dá seis. [p=0.3] Na escala, subir um ponto é {f}multiplicar por dez."),
    # pH
    dict(id="s05", block="ph", text="Comece pelo pê agá, que mede a acidez. [p=0.2] A fórmula é {a}pê agá igual a menos o logaritmo da concentração de hidrogênio. [p=0.3] Essa concentração mede {b}quanto hidrogênio há em cada litro, na forma que deixa o líquido ácido. [p=0.2] {c}Mais hidrogênio, mais ácido."),
    dict(id="s06", block="ph", text="Se a concentração é {a}dez elevado a menos três, [p=0.2] o logaritmo dela dá {b}menos três, [p=0.2] e o pê agá dá {c}três. [p=0.3] O menos da fórmula está lá só para o pê agá {d}sair positivo."),
    dict(id="s07", block="ph", text="Pê agá cinco é concentração {a}dez elevado a menos cinco. [p=0.2] Divida a concentração do pê agá três pela do pê agá cinco. [p=0.2] Mesma base, a divisão subtrai os expoentes: [p=0.2] de menos cinco até menos três, {b}são dois passos. [p=0.2] {c}Dez ao quadrado dá cem. [p=0.3] {d}Pê agá menor, mais ácido. [p=0.2] Cada ponto a menos {e}multiplica a acidez por dez."),
    # Richter
    dict(id="s08", block="richter", text="No terremoto, a escala Richter. [p=0.2] Uma fórmula comum nas questões é {a}eme igual ao logaritmo da amplitude dividida por uma amplitude de referência. [p=0.3] {b}Eme é a magnitude. [p=0.2] {c}A amplitude, a letra á maiúscula na tela, é o tamanho do tremor registrado no aparelho. [p=0.2] {d}A de referência, com um zero pequeno embaixo, é fixa."),
    dict(id="s09", block="richter", text="Compare {a}magnitude sete com magnitude cinco. [p=0.2] Sete menos cinco dá {b}dois. [p=0.3] Pela propriedade, cada magnitude é {c}o logaritmo da amplitude menos o logaritmo da referência. [p=0.2] Na subtração, {d}a referência se cancela, [p=0.2] e sobra {e}o logaritmo da amplitude do sete dividida pela do cinco, igual a dois."),
    dict(id="s10", block="richter", text="Logaritmo igual a dois quer dizer {a}dez ao quadrado. [p=0.2] A amplitude do terremoto sete é {b}cem vezes a do cinco."),
    # decibéis
    dict(id="s11", block="som", text="No som, a fórmula é {a}beta igual a dez vezes o logaritmo da intensidade dividida por uma intensidade de referência. [p=0.3] {b}Beta é o nível em decibéis. [p=0.2] {c}A intensidade, a letra i na tela, mede a energia do som que chega ao ouvido, [p=0.2] e {d}a de referência, com o zero pequeno, é fixa: o som mais fraco que o ouvido percebe. [p=0.3] Repare no {e}dez na frente: ele muda a conta."),
    dict(id="s12", block="som", text="Pense num som {a}dez decibéis mais alto que outro. [p=0.2] A diferença dos níveis fica {b}dez vezes o logaritmo da divisão das intensidades, igual a dez. [p=0.2] Divida por dez: {c}o logaritmo dá um. [p=0.2] Então {d}a intensidade fica dez vezes maior. [p=0.3] Com {e}vinte decibéis a mais, a intensidade fica cem vezes maior."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}ler a escala como uma régua comum. [p=0.2] A pessoa vê pê agá três e pê agá cinco, [p=0.2] calcula {b}cinco menos três, que dá dois, [p=0.2] e responde {c}duas vezes mais ácido."),
    dict(id="s14", block="erro", text="Mas cada ponto é {a}uma multiplicação por dez, não uma soma. [p=0.2] Dois pontos são {b}dez vezes dez, que dá cem vezes."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}a diferença vira expoente do dez. [p=0.2] Pê agá e Richter: {b}diferença dois vira dez ao quadrado, que dá cem vezes. [p=0.3] Decibéis: {c}divida a diferença por dez antes. [p=0.2] Trinta decibéis a mais dão expoente três, [p=0.2] e {d}dez ao cubo dá mil vezes."),
    dict(id="s16", block="atalho", text="Funciona porque a fórmula usa logaritmo na base dez, [p=0.2] e {a}a diferença de logaritmos é o logaritmo da divisão. [p=0.3] Não compensa quando {b}a diferença não é inteira, como pê agá três contra três vírgula três. [p=0.2] Aí o expoente é quebrado, e a conta pede {c}o logaritmo de dois, assunto de outra aula. [p=0.3] E leia sempre {d}a fórmula do enunciado: se o número na frente mudar, o atalho muda junto."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar, com valores criados para esta aula. [p=0.2] {a}Um liquidificador ligado chega a noventa decibéis. [p=0.2] {b}Uma conversa, a sessenta. [p=0.3] Com {c}beta igual a dez vezes o logaritmo da intensidade dividida pela de referência, [p=0.2] {d}quantas vezes a intensidade do liquidificador é maior?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] A diferença: {a}noventa menos sessenta dá trinta decibéis. [p=0.2] Tire o dez da frente: {b}trinta dividido por dez dá três. [p=0.2] O logaritmo da divisão das intensidades {c}dá três. [p=0.2] {d}Dez ao cubo dá mil. [p=0.2] Mil vezes mais intenso."),
    dict(id="s20", block="resposta", text="Repare: o nível subiu {a}de sessenta para noventa, só a metade a mais. [p=0.2] A intensidade ficou {b}mil vezes maior. [p=0.2] Essa é a força da escala logarítmica."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}na escala logarítmica, cada ponto multiplica por dez. [p=0.2] {b}Ache a diferença, ajuste pelo número da fórmula, [p=0.2] e {c}ela vira o expoente do dez."),
    dict(id="s22", block="fim", text="Na próxima aula, é a sua vez: {a}questões para praticar logaritmos, [p=0.2] com propriedades, equações e escalas de ciências. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
