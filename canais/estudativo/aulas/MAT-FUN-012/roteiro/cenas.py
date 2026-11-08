# Estudativo · MAT-FUN-012 — Achar a lei por dois pontos (Matemática · Funções · Função afim).
# Habilidade: descobrir f(x) = 2x + 3 a partir dos pontos (1, 5) e (3, 9), ou lendo o gráfico, e prever o valor seguinte.
# Pré-requisitos: MAT-FUN-010 (coeficientes: a = Δy/Δx e valor inicial). Próxima: MAT-FUN-013.
# Questão inédita, criada para esta aula. Letras narradas: "á", "bê", "xis", "ípsilon"; Δ = "delta", como na MAT-FUN-010.
# Zero e estudo do sinal (MAT-FUN-011) não estão na ficha desta aula: não usar os termos.
# (1, 5) e (3, 9): a = (9 − 5)/(3 − 1) = 2 · 2·1 + b = 5 → b = 3 · f(x) = 2x + 3 · confere f(3) = 9 · prevê f(4) = 11.
# Gráfico: reta por (0, 6) e (2, 2): b = 6 lido no eixo y · a = (2 − 6)/(2 − 0) = −2 · f(x) = −2x + 6 · confere f(2) = 2.
# Erro: ordem trocada (9 − 5)/(1 − 3) = −2 → b = 7 → f(x) = −2x + 7 → f(3) = 1, não 9.
# Atalho: voltar até x = 0: 5 − 2 = 3 = b.
# Questão: técnico, 2 h → R$ 150 e 5 h → R$ 300 · a = 150/3 = 50 · b = 150 − 100 = 50 · f(x) = 50x + 50 · f(6) = 350.
# Visual: tabela com xis um → cinco, xis três → nove; plano (E.plano) com (1, 5) e (3, 9) e a reta (E.reta_pontos), degrau Δx e Δy;
#   b aparecendo em (0, 3) no eixo y; depois plano com a reta por (0, 6) e (2, 2) para leitura; setas "voltando" de x = 1 para x = 0.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Achar a lei por dois pontos"

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
    dict(id="s01", block="gancho", text="Uma função afim passa por {a}dois pontos: [p=0.2] {b}xis um, ípsilon cinco, [p=0.2] e {c}xis três, ípsilon nove. [p=0.3] Só com isso, dá para descobrir {d}a fórmula inteira [p=0.2] e {e}prever qualquer outro valor."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a lei de uma função afim por dois pontos [p=0.2] ou {b}lendo o gráfico, [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}os coeficientes da função afim, á xis mais bê. [p=0.3] {c}O á é a taxa de variação: delta ípsilon dividido por delta xis. [p=0.2] {d}O bê é o valor inicial: o ípsilon quando o xis é zero. [p=0.3] Se faltar, procure no canal."),
    # passo 1
    dict(id="s04", block="metodo", text="O método tem {a}dois passos: [p=0.2] primeiro o á, depois o bê."),
    dict(id="s05", block="metodo", text="{a}Passo um: o á. [p=0.2] {b}Delta ípsilon: nove menos cinco dá quatro. [p=0.2] {c}Delta xis: três menos um dá dois. [p=0.2] {d}Quatro dividido por dois: á igual a dois. [p=0.3] Cada vez que o xis anda um, {e}o ípsilon sobe dois."),
    # passo 2
    dict(id="s06", block="metodo", text="{a}Passo dois: o bê. [p=0.2] A lei já está quase pronta: {b}efe de xis igual a dois xis mais bê. [p=0.3] Use {c}um dos pontos, xis um, ípsilon cinco. [p=0.2] Troque o xis por um e o efe de xis por cinco: [p=0.2] {d}dois vezes um mais bê igual a cinco."),
    dict(id="s07", block="metodo", text="{a}Dois mais bê igual a cinco. [p=0.2] {b}Tire dois de cada lado: bê igual a três. [p=0.3] A lei é {c}efe de xis igual a dois xis mais três."),
    # conferir e prever
    dict(id="s08", block="prever", text="Confira com {a}o outro ponto: [p=0.2] {b}dois vezes três dá seis, mais três dá nove. [p=0.2] {c}Bateu. [p=0.3] Agora, prever é só calcular. [p=0.2] O valor seguinte, {d}com xis quatro: [p=0.2] {e}dois vezes quatro dá oito, mais três dá onze."),
    # gráfico
    dict(id="s09", block="grafico", text="E se vier {a}um gráfico, e não os pontos? [p=0.3] Procure {b}dois pontos em que a reta passa bem no cruzamento da grade. [p=0.2] Nesta reta: {c}xis zero, ípsilon seis, [p=0.2] e {d}xis dois, ípsilon dois."),
    dict(id="s10", block="grafico", text="Um deles está {a}em cima do eixo ípsilon. [p=0.2] Ali o xis é zero, [p=0.2] então {b}o bê se lê direto: seis. [p=0.3] O á: {c}delta ípsilon, dois menos seis, dá menos quatro. [p=0.2] {d}Delta xis, dois menos zero, dá dois. [p=0.2] {e}Menos quatro dividido por dois: menos dois. [p=0.3] Lei: {f}efe de xis igual a menos dois xis mais seis."),
    # erro
    dict(id="s11", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}trocar a ordem dos pontos no meio da conta. [p=0.3] A pessoa faz {b}nove menos cinco em cima, [p=0.2] mas {c}um menos três embaixo. [p=0.2] Dá {d}quatro dividido por menos dois: menos dois. [p=0.3] A reta, que sobe, {e}viraria uma reta que desce."),
    dict(id="s12", block="erro", text="Com á igual a menos dois, o bê sairia {a}sete, [p=0.2] e a lei seria menos dois xis mais sete. [p=0.2] Teste no xis três: {b}menos seis mais sete dá um, [p=0.2] mas o ponto pede nove. [p=0.3] {c}O ponto que entra primeiro em cima entra primeiro embaixo. [p=0.2] E a conferência {d}sempre denuncia a troca."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho para o bê: [p=0.2] {a}ande para trás até o xis zero. [p=0.3] O á é dois: {b}cada passo para trás no xis tira dois do ípsilon. [p=0.2] Saia do ponto {c}xis um, ípsilon cinco. [p=0.2] {d}Um passo para trás: [p=0.2] {e}cinco menos dois dá três. [p=0.2] {f}É o bê."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o bê é o ípsilon no xis zero, [p=0.2] e o á diz quanto o ípsilon muda a cada passo. [p=0.2] Com á negativo, é o contrário: [p=0.2] cada passo para trás soma. [p=0.3] {b}Não compensa quando os pontos estão longe do zero, [p=0.2] como {c}xis cem. [p=0.2] Cem passos para trás é muita conta: [p=0.2] aí, {d}troque o ponto na fórmula, como no passo dois."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um técnico cobra pela fórmula de uma função afim. [p=0.2] {a}Duas horas de serviço custam cento e cinquenta reais. [p=0.2] {b}Cinco horas custam trezentos. [p=0.3] {c}Qual é a lei do preço? [p=0.2] E {d}quanto custam seis horas?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Os pontos são {a}xis dois, ípsilon cento e cinquenta, [p=0.2] e {b}xis cinco, ípsilon trezentos. [p=0.3] {c}Delta ípsilon: trezentos menos cento e cinquenta dá cento e cinquenta. [p=0.2] {d}Delta xis: cinco menos dois dá três. [p=0.2] {e}Cento e cinquenta dividido por três: á igual a cinquenta reais por hora."),
    dict(id="s18", block="resposta", text="O bê, pelo atalho: [p=0.2] {a}dois passos para trás a partir do xis dois, tirando cinquenta em cada um. [p=0.2] {b}Cento e cinquenta menos cem dá cinquenta. [p=0.3] Lei: {c}efe de xis igual a cinquenta xis mais cinquenta. [p=0.2] Seis horas: {d}cinquenta vezes seis dá trezentos, [p=0.2] {e}mais cinquenta: trezentos e cinquenta reais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o á vem do delta ípsilon dividido pelo delta xis, [p=0.2] {b}o bê vem de um ponto na fórmula [p=0.2] e {c}o outro ponto confere."),
    dict(id="s20", block="fim", text="Na próxima aula, você conhece {a}a reta que passa pela origem, [p=0.2] a das {b}grandezas proporcionais, [p=0.2] e descobre {c}por que o táxi com bandeirada não é proporcional. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
