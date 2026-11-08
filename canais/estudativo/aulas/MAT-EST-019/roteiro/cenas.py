# Estudativo · MAT-EST-019 — Gráficos que enganam (Matemática · Estatística · Análise crítica de gráficos).
# Habilidade: perceber um eixo que não começa em zero, uma escala irregular ou uma figura fora de proporção e dizer qual foi o crescimento real.
# Pré-requisitos: MAT-EST-003 (ler título, eixos e unidade; variação percentual no gráfico), MAT-EST-004 (setores). Usa MAT-POR-005 (diferença dividida pelo valor de antes). Próxima: MAT-EST-020.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Gráficos e dados criados para esta aula.
# Telas: s01/s04 colunas A = 50, B = 55 com eixo de 45 a 55 (B parece o dobro) e depois de 0 a 60
#        s08 linha jan 100, fev 110, mar 120, dez 210, com dez colado em mar (marcas iguais) e depois com os meses todos
#        s11 pictograma: garrafa de 3 mil litros e garrafa com o dobro da altura e da largura para 6 mil
#        s17 colunas matrículas 400 e 420, eixo começando em 390 · garrafas do item dois: 2 mil e 4 mil litros, dobro de altura e largura.

TITULO = "Gráficos que enganam: eixo cortado, escala e figura"

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
    dict(id="s01", block="gancho", text="{a}Num anúncio, a coluna da marca bê é o dobro da coluna da marca á. [p=0.3] Parece que bê vende {b}duas vezes mais. [p=0.3] Mas leia os números: [p=0.2] {c}cinquenta contra cinquenta e cinco. [p=0.2] {d}A diferença real é de só dez por cento."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reconhece três truques de gráfico, [p=0.2] calcula o crescimento de verdade [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}ler o título, os eixos e a unidade de um gráfico, [p=0.2] e {c}a variação percentual: a diferença dividida pelo valor de antes. [p=0.3] Se faltar alguma, procure no canal."),
    # truque 1: eixo cortado
    dict(id="s04", block="eixo", text="{a}Primeiro truque: o eixo que não começa no zero. [p=0.3] Olhe o eixo do lado do anúncio: {b}ele começa em quarenta e cinco. [p=0.2] Então a coluna de á só mostra {c}cinquenta menos quarenta e cinco, que dá cinco. [p=0.2] A de bê mostra {d}cinquenta e cinco menos quarenta e cinco, que dá dez."),
    dict(id="s05", block="eixo", text="Cortar o eixo {a}come o mesmo pedaço de baixo de todas as colunas. [p=0.2] O que sobra {b}exagera a diferença. [p=0.3] Desenhe de novo, {c}com o eixo começando no zero: [p=0.2] {d}as colunas ficam quase do mesmo tamanho."),
    dict(id="s06", block="eixo", text="O crescimento real sai dos números, não do desenho: [p=0.2] {a}cinquenta e cinco menos cinquenta dá cinco. [p=0.2] {b}Cinco dividido por cinquenta dá zero vírgula um: [p=0.2] dez por cento."),
    dict(id="s07", block="eixo", text="Em {a}gráfico de linhas, o eixo cortado é comum, [p=0.2] porque ali o que importa é a subida e a descida. [p=0.2] Mesmo assim, {b}confira onde o eixo começa antes de dizer que algo disparou."),
    # truque 2: escala irregular
    dict(id="s08", block="escala", text="{a}Segundo truque: a escala irregular. [p=0.3] Um gráfico de vendas mostra {b}janeiro, fevereiro, março e dezembro, [p=0.2] {c}com o mesmo espaço entre eles. [p=0.3] De março para dezembro, {d}a linha parece disparar num salto só."),
    dict(id="s09", block="escala", text="Mas de março a dezembro são {a}nove meses. [p=0.2] As vendas subiram de cento e vinte para duzentos e dez: [p=0.2] {b}uma alta de noventa. [p=0.2] {c}Noventa dividido por nove dá dez por mês. [p=0.3] É {d}o mesmo ritmo do começo do ano: dez por mês. [p=0.2] Com os meses no lugar certo, {e}a linha sobe sempre igual."),
    dict(id="s10", block="escala", text="A regra: {a}marcas com o mesmo espaço precisam ter o mesmo passo. [p=0.2] Vale no eixo de baixo [p=0.2] e {b}no eixo do lado."),
    # truque 3: figura fora de proporção
    dict(id="s11", block="figura", text="{a}Terceiro truque: a figura fora de proporção. [p=0.3] A produção de leite de uma fazenda {b}dobrou: de três mil para seis mil litros. [p=0.3] O desenhista {c}dobrou a altura da garrafa [p=0.2] e {d}dobrou também a largura."),
    dict(id="s12", block="figura", text="Só que o olho não mede só a altura. [p=0.2] Ele mede {a}o espaço que a figura ocupa, a área: [p=0.2] largura vezes altura. [p=0.3] {b}Duas vezes mais larga e duas vezes mais alta dá quatro vezes a área. [p=0.3] A garrafa nova {c}parece quatro vezes maior. [p=0.2] O real é {d}o dobro: um aumento de cem por cento."),
    # erro
    dict(id="s13", block="erro", text="Agora, o erro mais comum: [p=0.2] {a}medir o crescimento pelo desenho. [p=0.3] No anúncio, o pedaço desenhado da coluna passou de cinco para dez. [p=0.2] A pessoa calcula pelo desenho: {b}dez menos cinco dá cinco. [p=0.2] Cinco dividido por cinco dá um: [p=0.2] cem por cento. [p=0.3] Mas esses pedaços {c}não são os valores. [p=0.2] Os valores são {d}cinquenta [p=0.2] e cinquenta e cinco: dez por cento."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}três olhares antes de acreditar. [p=0.3] {b}O eixo começa no zero? [p=0.2] {c}Marcas com o mesmo espaço têm o mesmo passo? [p=0.2] {d}A figura cresceu numa direção só? [p=0.3] Qualquer não, {e}ignore o desenho e faça a conta com os números."),
    dict(id="s15", block="atalho", text="Funciona porque, num gráfico honesto, {a}o tamanho do desenho é proporcional ao valor. [p=0.2] Cada truque quebra essa proporção. [p=0.3] Não compensa quando {b}o gráfico não traz números. [p=0.2] Aí, você só pode {c}comparar tamanhos se os três olhares passarem."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Item um: um gráfico de colunas mostra as matrículas de uma escola em dois anos. [p=0.2] {b}O eixo do lado começa em trezentos e noventa. [p=0.2] As colunas marcam {c}quatrocentos [p=0.2] e quatrocentos e vinte. [p=0.3] {d}Quantas vezes a segunda coluna parece maior? [p=0.2] {e}E qual foi o crescimento real?"),
    dict(id="s17", block="questao", text="{a}Item dois: a produção de uma horta passou de dois mil para quatro mil quilos. [p=0.2] {b}O caixote do desenho dobrou de altura e de largura. [p=0.3] {c}Quantas vezes maior ele parece? [p=0.2] {d}E quantas vezes a produção cresceu?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Com o eixo em trezentos e noventa, {a}a primeira coluna mostra quatrocentos menos trezentos e noventa, que dá dez, [p=0.2] e {b}a segunda mostra quatrocentos e vinte menos trezentos e noventa, que dá trinta. [p=0.2] {c}Trinta dividido por dez dá três: parece três vezes maior. [p=0.3] O real: {d}quatrocentos e vinte menos quatrocentos dá vinte. [p=0.2] {e}Vinte dividido por quatrocentos dá zero vírgula zero cinco: [p=0.2] {f}cinco por cento de crescimento."),
    dict(id="s20", block="resposta", text="No caixote, {a}dobro da altura vezes dobro da largura: [p=0.2] {b}parece quatro vezes maior. [p=0.3] Mas {c}quatro mil dividido por dois mil dá dois. [p=0.2] {d}A produção só dobrou."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.2] {a}confira o começo do eixo, o passo da escala e o tamanho da figura. [p=0.2] E {b}calcule o crescimento com os números, nunca com o desenho."),
    dict(id="s22", block="fim", text="Na próxima aula, quem engana são {a}os próprios números: [p=0.2] {b}amostra ruim, [p=0.2] {c}porcentagem sobre base pequena [p=0.2] e {d}correlação que não é causa. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
