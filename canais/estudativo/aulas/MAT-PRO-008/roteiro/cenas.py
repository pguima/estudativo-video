# Estudativo · MAT-PRO-008 — Progressão geométrica: razão e termo geral (Matemática · Progressões · Progressão geométrica).
# Habilidade: achar a razão de 3, 6, 12, …, calcular o 8º termo com aₙ = a₁ · qⁿ⁻¹ e ver a PG como uma função exponencial, como o montante mês a mês.
# Pré-requisitos: MAT-PRO-004 (razão, saltos e termo geral da PA), MAT-FIN-004 (juros compostos), MAT-EXP-002 (crescer multiplicando). Próxima: MAT-PRO-009.
# Questão inédita, criada para esta aula. Termos como na MAT-PRO-004 (razão, saltos, á ene, "pê á") e na MAT-FIN-004 /
#   MAT-EXP-002 (montante, fator, "o fator na base e o tempo no expoente"). PG = "pê gê"; razão da PG = "quê".
# Contas: 6 / 3 = 12 / 6 = 2 · a₈ = 3 · 2⁷ = 3 · 128 = 384 · a₄ = 24, a₅ = 48.
# Razões: 80, 40, 20 → 1/2 · 1, −2, 4, −8 → −2.
# Juros: 1.000, 1.100, 1.210, 1.331 · 1.100 / 1.000 = 1,1 · M = 1.000 · 1,1ᵗ (o 1º termo é o mês zero; t = n − 1).
# Erro: fórmula da PA, 3 + 7 · 2 = 17 (mas a₅ já é 48). Atalho: de a₄ = 24, 4 saltos: 2⁴ = 16 · 24 · 16 = 384; não compensa se o termo conhecido é o 1º.
# Questão: 2, 6, 18 → q = 3 · a₆ = 2 · 3⁵ = 2 · 243 = 486 · carro R$ 40.000, −10% ao ano → q = 0,9 · 36.000 · 32.400.
# Visual: lista 3, 6, 12, 24 com "×2" em arco entre os termos (contraste com o "+4" da PA); fórmula aₙ = a₁ · q^{n−1}
#   (E.formula) com cada letra apontada; plano (E.plano) com os montantes de 0 a 10 meses (E.ponto, 1.000 a ≈2.594) em cima
#   da curva 1.000 · 1,1ˣ (E.curva), ao lado da reta pontilhada de uma PA para comparar "reta x curva".
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Progressão geométrica: razão e termo geral"

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
    dict(id="s01", block="gancho", text="{a}Três, [p=0.1] seis, [p=0.1] doze, [p=0.1] vinte e quatro. [p=0.3] Aqui não se soma sempre o mesmo número: [p=0.2] {b}cada termo é o dobro do anterior. [p=0.3] Qual é o {c}oitavo termo? [p=0.2] {d}Trezentos e oitenta e quatro, com uma conta só."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a razão desse tipo de lista e calcula qualquer termo com uma fórmula. [p=0.2] Vai reconhecer nela {b}os juros compostos. [p=0.2] E ainda leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}o termo geral da pê á, que conta os saltos, [p=0.2] {b}os juros compostos, mês a mês, [p=0.2] e {c}a exponencial, com o fator na base e o tempo no expoente. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é PG
    dict(id="s04", block="pg", text="Sequência que anda {a}multiplicando sempre pelo mesmo número se chama {b}progressão geométrica, ou pê gê. [p=0.3] O número que multiplica é {c}a razão da pê gê, e a letra dela é {d}quê."),
    dict(id="s05", block="pg", text="Para achar a razão, {a}divida um termo pelo anterior. [p=0.2] {b}Seis dividido por três dá dois. [p=0.2] {c}Doze dividido por seis também dá dois. [p=0.3] {d}A razão é dois. [p=0.3] Na pê á, você subtraía. [p=0.2] {e}Na pê gê, você divide."),
    dict(id="s06", block="pg", text="A razão pode ser fração. [p=0.2] Em {a}oitenta, [p=0.1] quarenta, [p=0.1] vinte, [p=0.2] {b}a razão é um meio, e a lista cai pela metade. [p=0.3] E pode ser negativa: [p=0.2] em {c}um, [p=0.1] menos dois, [p=0.1] quatro, [p=0.1] menos oito, [p=0.2] a razão é {d}menos dois, e o sinal fica trocando."),
    # termo geral
    dict(id="s07", block="saltos", text="Agora, o oitavo termo. [p=0.2] Do primeiro ao oitavo são {a}sete saltos, como na pê á. [p=0.2] Só que cada salto {b}multiplica por dois. [p=0.3] Multiplicar por dois sete vezes é {c}multiplicar por dois elevado a sete."),
    dict(id="s08", block="formula", text="Daí sai {a}o termo geral da pê gê: [p=0.2] {b}á índice ene igual a á índice um vezes quê elevado a ene menos um. [p=0.3] {c}Á índice um é o primeiro termo. [p=0.1] {d}Quê é a razão. [p=0.1] {e}Ene menos um é o número de saltos, que agora vai no expoente."),
    dict(id="s09", block="formula", text="Para o oitavo: {a}á índice oito igual a três vezes dois elevado a sete. [p=0.2] {b}Dois elevado a sete dá cento e vinte e oito. [p=0.2] {c}Três vezes cento e vinte e oito dá trezentos e oitenta e quatro. [p=0.3] Atenção à ordem: {d}primeiro a potência, depois a multiplicação pelo primeiro termo."),
    # PG como exponencial
    dict(id="s10", block="juros", text="E onde você já viu isso? [p=0.2] Mil reais a {a}dez por cento ao mês, em juros compostos: [p=0.2] {b}mil, [p=0.1] mil e cem, [p=0.1] mil duzentos e dez, [p=0.1] mil trezentos e trinta e um. [p=0.3] {c}Mil e cem dividido por mil dá um vírgula um. [p=0.2] É uma pê gê, e {d}a razão é o fator."),
    dict(id="s11", block="juros", text="Repare: o primeiro termo é {a}o mês zero, o dinheiro do começo. [p=0.2] Por isso o expoente, ene menos um, é {b}o número de meses que passaram. [p=0.3] Com tê meses: {c}eme igual a mil vezes um vírgula um elevado a tê. [p=0.2] É a fórmula dos juros compostos, e é {d}uma função exponencial."),
    dict(id="s12", block="juros", text="No plano, marque {a}o montante mês a mês. [p=0.2] Os pontos não ficam alinhados: [p=0.2] {b}sobem cada vez mais, em cima de uma curva exponencial. [p=0.3] {c}A pê á mora numa reta. [p=0.2] {d}A pê gê mora numa curva exponencial."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}usar a fórmula da pê á. [p=0.2] A pessoa faz {b}três mais sete vezes dois, [p=0.2] e responde {c}dezessete."),
    dict(id="s14", block="erro", text="Mas o quinto termo já é {a}quarenta e oito. [p=0.2] O oitavo não pode ser dezessete. [p=0.3] {b}Na pê á, a razão se soma uma vez por salto. [p=0.2] {c}Na pê gê, a razão multiplica, e os saltos vão para o expoente."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}pule do termo mais perto. [p=0.3] Você já sabe que {b}á índice quatro é vinte e quatro. [p=0.2] Do quarto ao oitavo são {c}quatro saltos, e dois elevado a quatro dá dezesseis. [p=0.2] {d}Vinte e quatro vezes dezesseis dá trezentos e oitenta e quatro."),
    dict(id="s16", block="atalho", text="Funciona porque {a}cada salto multiplica pela razão, não importa de onde você parte. [p=0.3] E guarde {b}as potências de dois até dois elevado a dez, que dá mil e vinte e quatro: [p=0.2] elas aparecem demais. [p=0.3] Não compensa quando o termo conhecido é {c}o primeiro: [p=0.2] {d}aí, o pulo é a própria fórmula."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Na pê gê dois, [p=0.1] seis, [p=0.1] dezoito, qual é a razão e qual é o sexto termo? [p=0.3] E um carro de {b}quarenta mil reais perde dez por cento do valor por ano. [p=0.2] {c}Os valores, ano a ano, formam uma pê gê de que razão? [p=0.2] {d}Quanto o carro vale depois de dois anos?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Seis dividido por dois dá três: a razão é três. [p=0.2] Sexto termo: {b}cinco saltos. [p=0.2] {c}Três elevado a cinco dá duzentos e quarenta e três. [p=0.2] {d}Dois vezes duzentos e quarenta e três dá quatrocentos e oitenta e seis."),
    dict(id="s20", block="resposta", text="No carro, perder dez por cento é multiplicar pelo fator {a}zero vírgula nove: essa é a razão. [p=0.3] {b}Quarenta mil vezes zero vírgula nove dá trinta e seis mil. [p=0.2] {c}Vezes zero vírgula nove de novo dá trinta e dois mil e quatrocentos reais."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}na pê gê, a razão é um termo dividido pelo anterior. [p=0.2] {b}Os saltos vão no expoente da razão. [p=0.2] E {c}a pê gê é uma exponencial, como o montante mês a mês."),
    dict(id="s22", block="fim", text="Na próxima aula, os atalhos da pê gê: [p=0.2] {a}o termo do meio de quatro, [p=0.1] xis, [p=0.1] nove, [p=0.2] e {b}três termos escritos como xis dividido por quê, xis e xis vezes quê. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
