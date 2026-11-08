# Estudativo · MAT-POR-005 — Variação percentual (Matemática · Porcentagem).
# Habilidade: dizer que passar de 80 para 100 é um aumento de 25%.
# Pré-requisitos: MAT-POR-003 (quantos por cento: parte dividida pelo total). Próxima: MAT-POR-014.
# Questão inédita, criada para esta aula. MAT-POR-004 (fatores) não está na cadeia desta aula: nada de fator.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Variação percentual"

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
    dict(id="s01", block="gancho", text="Um preço {a}passou de oitenta para cem reais. [p=0.2] Subiu vinte reais. [p=0.3] Muita gente diz: {b}aumento de vinte por cento. [p=0.3] Errado. [p=0.2] O aumento foi de {c}vinte e cinco por cento."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular de quantos por cento algo subiu ou caiu, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa só: [p=0.2] {b}descobrir quantos por cento uma parte é do total, [p=0.2] dividindo a parte pelo total. [p=0.3] Se faltar, procure no canal."),
    # de quê
    dict(id="s04", block="base", text="{a}Variação percentual é quanto um valor mudou, contado em por cento. [p=0.3] A pergunta-chave é: vinte reais são quantos por cento {b}de quê? [p=0.3] A mudança é sempre medida em cima do {c}valor de antes. [p=0.2] O preço antigo, oitenta reais, é o {d}cem por cento."),
    dict(id="s05", block="base", text="Então é a conta que você já conhece: {a}parte dividida pelo total. [p=0.2] A parte é o aumento, {b}vinte. [p=0.2] O total é o valor antigo, {c}oitenta. [p=0.3] {d}Vinte oitenta avos simplifica para um quarto, [p=0.2] que vale {e}vinte e cinco por cento."),
    # regra
    dict(id="s06", block="regra", text="A regra tem {a}três passos. [p=0.2] {b}Passo um: a diferença entre o novo e o antigo. [p=0.2] {c}Passo dois: divida pelo antigo. [p=0.2] {d}Passo três: ande a vírgula duas casas para a direita."),
    dict(id="s07", block="regra", text="Mais um exemplo. [p=0.2] Uma passagem {a}foi de cinquenta para setenta e cinco reais. [p=0.2] {b}A diferença é de vinte e cinco. [p=0.2] {c}Vinte e cinco dividido por cinquenta dá zero vírgula cinco. [p=0.2] Andando a vírgula, {d}aumento de cinquenta por cento. [p=0.3] Faz sentido: subiu {e}metade do que custava."),
    # queda
    dict(id="s08", block="queda", text="Na queda, é igual. [p=0.2] Um preço {a}caiu de cem para oitenta. [p=0.2] A diferença é de {b}vinte reais. [p=0.2] Só que agora o valor de antes é {c}cem. [p=0.3] {d}Vinte dividido por cem dá zero vírgula vinte: [p=0.2] uma queda de {e}vinte por cento."),
    dict(id="s09", block="queda", text="Repare: {a}a mesma diferença de vinte reais. [p=0.2] Subindo a partir de oitenta, são {b}vinte e cinco por cento. [p=0.2] Descendo a partir de cem, são {c}vinte por cento. [p=0.3] O que muda é {d}o valor de antes."),
    # erro
    dict(id="s10", block="erro", text="Por isso, o erro mais comum é {a}dividir pelo valor novo. [p=0.2] No aumento de oitenta para cem, a pessoa faz {b}vinte dividido por cem [p=0.2] e responde {c}vinte por cento. [p=0.3] Mas o aumento se mede {d}em cima do preço de antes, que era oitenta."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: {a}divida o novo pelo antigo. [p=0.3] {b}Cem dividido por oitenta dá um vírgula vinte e cinco. [p=0.2] Andando a vírgula, {c}cento e vinte e cinco por cento do valor antigo. [p=0.3] O que passou de cem é o aumento: {d}vinte e cinco por cento."),
    dict(id="s12", block="atalho", text="Na queda: {a}oitenta dividido por cem dá zero vírgula oito, [p=0.2] que são oitenta por cento. [p=0.2] Faltam {b}vinte para chegar a cem: queda de vinte por cento. [p=0.3] Funciona porque {c}o antigo vira o cem por cento. [p=0.3] E vem um bônus: {d}quem dobra fica com duzentos por cento do antigo, [p=0.2] então aumentou cem por cento."),
    dict(id="s13", block="atalho", text="Não compensa quando {a}a diferença é um número pequeno e fácil. [p=0.2] De cento e sessenta para cento e oitenta, a diferença é vinte, [p=0.2] e {b}vinte cento e sessenta avos simplifica para um oitavo, [p=0.1] que vale doze vírgula cinco por cento. [p=0.3] Dividir cento e oitenta por cento e sessenta daria mais trabalho."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um aluguel {a}passou de mil e duzentos para mil trezentos e oitenta reais. [p=0.2] {b}De quantos por cento foi o aumento? [p=0.3] E um produto {c}caiu de sessenta para quarenta e cinco reais. [p=0.2] {d}De quantos por cento foi a queda?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] No aluguel, a diferença é de {a}cento e oitenta reais. [p=0.2] Divida pelo antigo: {b}cento e oitenta dividido por mil e duzentos dá zero vírgula quinze. [p=0.2] {c}Aumento de quinze por cento. [p=0.3] Confira: {d}dez por cento de mil e duzentos dá cento e vinte, [p=0.2] cinco por cento dá sessenta, [p=0.2] e juntos dão cento e oitenta. [p=0.2] Bateu."),
    dict(id="s17", block="resposta", text="No produto, a diferença é de {a}quinze reais. [p=0.2] O antigo é sessenta: {b}quinze sessenta avos simplifica para um quarto. [p=0.2] {c}Queda de vinte e cinco por cento. [p=0.3] Confira: um quarto de sessenta é quinze. [p=0.3] Repare que dividir pelo novo daria {d}um terço, e a resposta sairia errada."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}a diferença dividida pelo valor de antes. [p=0.2] {b}O antigo é sempre o cem por cento."),
    dict(id="s19", block="fim", text="Essa mesma conta serve para {a}medir erros. [p=0.2] Na próxima aula, você descobre qual erro pesa mais: [p=0.2] {b}um centímetro em dois metros [p=0.2] ou {c}um milímetro em um centímetro. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
