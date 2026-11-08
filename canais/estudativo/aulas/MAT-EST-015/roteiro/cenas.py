# Estudativo · MAT-EST-015 — Boxplot e amplitude (Matemática · Estatística · Mediana, moda e dispersão).
# Habilidade: ler num boxplot o mínimo, os quartis, o máximo e a amplitude e comparar duas turmas.
# Pré-requisitos: MAT-EST-014 (quartis: medianas das metades; mesmas onze notas). Próxima: MAT-EST-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Boxplot sem valores discrepantes: bigodes do mínimo ao máximo.
# Dados (tela): as 11 notas da aula anterior: 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10 → resumo 2 · 4 · 6 · 8 · 10.
#   Amplitude 10 − 2 = 8. Amplitude interquartil (largura da caixa) 8 − 4 = 4.
#   Turmas: manhã 4 · 5 · 6 · 7 · 8 (amplitude 4; caixa 2); noite 1 · 4 · 6 · 8 · 10 (amplitude 9; caixa 4). Mesma mediana 6.
#   Noite: Q3 = 8 → cerca de 25% com nota 8 ou mais. Atalho: acima de Q1 = 3 pedaços = 75%; de Q1 a Q3 = 50%.
#   Questão: entrega em dias: centro 2 · 3 · 4 · 5 · 7 (amplitude 5); bairro 1 · 2 · 3 · 6 · 12 (amplitude 11).
#     Até 3 dias para pelo menos metade: bairro (mediana 3; no centro a mediana é 4). Mais previsível: centro.
# Visual (boxplot não está no kit: caixa e bigodes desenhados sobre E.reta, eixo horizontal com escala de 0 a 10):
#   s01: dois boxplots com a mesma mediana, um curto e um comprido.
#   s04-s06: onze notas viram os cinco números; caixa de Q1 a Q3 com traço na mediana; bigodes até 2 e 10.
#   s07-s08: chave de ponta a ponta "10 − 2 = 8"; "de 2 a 10" riscado em vermelho; largura da caixa "8 − 4 = 4".
#   s09-s10: quatro pedaços com "25%" cada; bigode longo e bigode curto, ambos com "25%".
#   s11-s12: pedaços acesos somando 75% e 50%.
#   s13-s14: boxplots das turmas manhã e noite, um sobre o outro, mesma escala.
#   s15-s18: boxplots das duas lojas, eixo de 0 a 12 dias.

TITULO = "Boxplot e amplitude"

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
    dict(id="s01", block="gancho", text="{a}Duas turmas, a mesma mediana: seis. [p=0.3] São parecidas? [p=0.2] {b}Nem um pouco. [p=0.3] Um desenho simples mostra a diferença de uma olhada: {c}o boxplot."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê um boxplot, calcula a amplitude [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}uma coisa: os quartis. [p=0.2] {b}O primeiro é a mediana da metade de baixo, [p=0.2] {c}o segundo é a própria mediana [p=0.2] e {d}o terceiro é a mediana da metade de cima. [p=0.3] Se faltar, procure no canal."),
    # cinco números
    dict(id="s04", block="cinco", text="Lembra das {a}onze notas da aula de quartis? [p=0.2] Elas cabem em {b}cinco números: [p=0.2] {c}a menor nota, dois; [p=0.2] {d}o primeiro quartil, quatro; [p=0.2] {e}a mediana, seis; [p=0.2] {f}o terceiro quartil, oito; [p=0.2] {g}e a maior nota, dez."),
    # desenho
    dict(id="s05", block="desenho", text="O boxplot desenha esses cinco números {a}sobre uma reta com escala. [p=0.3] {b}Uma caixa vai do primeiro ao terceiro quartil. [p=0.2] {c}Um traço dentro dela marca a mediana."),
    dict(id="s06", block="desenho", text="Da caixa saem {a}duas hastes, chamadas de bigodes. [p=0.2] {b}Uma vai até o menor valor, [p=0.2] {c}a outra vai até o maior. [p=0.3] Daí o nome: {d}caixa e bigodes."),
    # amplitude
    dict(id="s07", block="amplitude", text="A {a}amplitude é o maior valor menos o menor. [p=0.2] {b}Dez menos dois dá oito. [p=0.3] No desenho, é {c}a distância de uma ponta à outra dos bigodes. [p=0.2] E repare: a resposta é {d}um número só: oito. [p=0.2] Nada de {e}responder de dois a dez."),
    dict(id="s08", block="amplitude", text="A {a}largura da caixa também conta: [p=0.2] {b}oito menos quatro dá quatro. [p=0.3] É a {c}amplitude interquartil. [p=0.2] Ela mede o espalhamento só da {d}metade do meio dos dados."),
    # pedaços
    dict(id="s09", block="pedacos", text="O desenho tem {a}quatro pedaços: [p=0.2] bigode de baixo, metade de baixo da caixa, metade de cima e bigode de cima. [p=0.3] Como os quartis cortam os dados em quatro, [p=0.2] {b}cada pedaço guarda cerca de um quarto dos dados: vinte e cinco por cento."),
    # erro
    dict(id="s10", block="erro", text="E aqui está o erro mais comum: [p=0.2] achar que {a}o bigode mais comprido tem mais dados. [p=0.3] Não tem. [p=0.2] {b}Cada bigode guarda cerca de vinte e cinco por cento. [p=0.2] O comprido só mostra que {c}ali os valores estão mais espalhados."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: [p=0.2] {a}conte os pedaços em vez de fazer conta. [p=0.3] Quantos por cento tiraram {b}mais que o primeiro quartil? [p=0.2] {c}Três pedaços: setenta e cinco por cento. [p=0.3] E {d}dentro da caixa? [p=0.2] {e}Dois pedaços: cinquenta por cento."),
    dict(id="s12", block="atalho", text="Funciona porque {a}os pedaços têm a mesma quantidade de dados, [p=0.2] mesmo com tamanhos diferentes. [p=0.3] {b}Não compensa quando o valor perguntado não é um dos cinco números: [p=0.2] aí, {c}o boxplot só dá uma estimativa."),
    # comparar turmas
    dict(id="s13", block="turmas", text="Agora as turmas do começo, {a}uma sobre a outra, na mesma escala. [p=0.2] {b}Manhã: de quatro a oito, caixa de cinco a sete. [p=0.2] {c}Noite: de um a dez, caixa de quatro a oito. [p=0.3] {d}Manhã e noite têm a mesma mediana: seis."),
    dict(id="s14", block="turmas", text="Mas a amplitude da manhã é {a}oito menos quatro, que dá quatro. [p=0.2] A da noite, {b}dez menos um, que dá nove. [p=0.3] {c}A manhã é mais homogênea: as notas são parecidas. [p=0.2] {d}A noite é espalhada. [p=0.3] E na noite, {e}cerca de vinte e cinco por cento tiraram oito ou mais, [p=0.2] porque oito é o terceiro quartil dela."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Os boxplots mostram o tempo de entrega, em dias, de duas lojas. [p=0.3] {b}Item um: qual é a amplitude de cada uma? [p=0.2] {c}Item dois: em qual delas pelo menos metade das entregas chega em até três dias? [p=0.2] {d}Item três: qual é mais previsível?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Loja do centro: sete menos dois dá cinco dias. [p=0.2] {b}Loja do bairro: doze menos um dá onze dias. [p=0.3] Pelo menos metade em até três dias é {c}pergunta de mediana. [p=0.2] {d}A mediana do bairro é três; a do centro é quatro. [p=0.2] {e}Resposta: a loja do bairro."),
    dict(id="s18", block="resposta", text="Mas a {a}mais previsível é a do centro: [p=0.2] {b}caixa e bigodes curtos. [p=0.3] No bairro, a caixa vai de dois a seis, e {c}o bigode chega a doze dias. [p=0.2] Você pode receber rápido ou esperar quase duas semanas."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.2] {a}o boxplot mostra os cinco números, [p=0.2] {b}cada pedaço tem um quarto dos dados [p=0.2] e {c}a amplitude é a maior ponta menos a menor."),
    dict(id="s20", block="fim", text="Só que a amplitude {a}olha só as duas pontas. [p=0.2] Na próxima aula, medidas que usam {b}todos os dados: [p=0.2] quanto cada valor se afasta da média. [p=0.2] São {c}o desvio médio, a variância e o desvio padrão. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
