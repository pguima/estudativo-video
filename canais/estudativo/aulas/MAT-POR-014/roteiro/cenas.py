# Estudativo · MAT-POR-014 — Erro relativo: qual erro pesa mais (Matemática · Porcentagem).
# Habilidade: dizer qual erro pesa mais, 1 cm em 2 m (0,5%) ou 1 mm em 1 cm (10%), dividindo o erro pela medida.
# Pré-requisitos: MAT-MED-001 (escada do metro), MAT-POR-005 (variação percentual). Próxima: MAT-POR-006.
# Questão inédita, criada para esta aula. Só comprimento: conversão de massa (MAT-MED-002) fora da ficha.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Erro relativo: qual erro pesa mais"

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
    dict(id="s01", block="gancho", text="Um pedreiro errou {a}um centímetro ao medir uma parede de dois metros. [p=0.2] Um relojoeiro errou {b}um milímetro numa peça de um centímetro. [p=0.3] Um centímetro é dez vezes mais que um milímetro. [p=0.2] Mas o erro que {c}pesa mais é o do relojoeiro."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai medir o peso de um erro em por cento, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}converter metro, centímetro e milímetro, [p=0.1] com cada degrau da escada valendo dez, [p=0.2] e {c}calcular uma variação percentual. [p=0.3] Se faltar alguma, procure no canal."),
    # absoluto e relativo
    dict(id="s04", block="ideia", text="Quanto um erro pesa depende do {a}tamanho do que você mede. [p=0.2] Um centímetro a mais numa parede {b}quase não se nota. [p=0.2] Um milímetro a mais numa peça de relógio pode {c}estragar a peça."),
    dict(id="s05", block="ideia", text="Por isso, existem dois jeitos de olhar um erro. [p=0.2] {a}O erro absoluto é o tamanho do erro, na unidade da medida. [p=0.3] {b}O erro relativo compara o erro com a medida: [p=0.2] {c}é o erro dividido pela medida. [p=0.3] Com erro e medida na mesma unidade, {d}o resultado fica sem unidade: é só um número. [p=0.2] Por isso dá para comparar uma parede com um relógio."),
    dict(id="s06", block="ideia", text="É a mesma conta da variação percentual: [p=0.2] {a}a diferença dividida pelo valor de referência. [p=0.2] Só que aqui a diferença é {b}o erro, [p=0.2] e a referência é {c}a medida."),
    # pedreiro
    dict(id="s07", block="pedreiro", text="Vamos ao pedreiro. [p=0.2] Antes de dividir, {a}ponha tudo na mesma unidade. [p=0.2] Na escada do metro, de metro para centímetro são dois degraus: {b}vezes cem. [p=0.2] Dois metros viram {c}duzentos centímetros."),
    dict(id="s08", block="pedreiro", text="{a}Um dividido por duzentos dá zero vírgula zero zero cinco. [p=0.3] Ande a vírgula duas casas para a direita: {b}zero vírgula cinco por cento. [p=0.2] Menos de {c}um por cento da parede."),
    # relojoeiro
    dict(id="s09", block="relojoeiro", text="Agora o relojoeiro. [p=0.2] De centímetro para milímetro é um degrau: {a}um centímetro tem dez milímetros. [p=0.2] {b}Um dividido por dez dá zero vírgula um. [p=0.2] Andando a vírgula, {c}dez por cento da peça."),
    dict(id="s10", block="relojoeiro", text="{a}Dez por cento contra {b}zero vírgula cinco por cento. [p=0.3] O erro do relojoeiro pesa {c}vinte vezes mais, [p=0.2] mesmo sendo o menor erro em tamanho. [p=0.3] Em prova, isso aparece como {d}precisão: [p=0.2] quanto menor o erro relativo, {e}mais precisa é a medida."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}dividir sem converter. [p=0.2] A pessoa pega {b}um centímetro e dois metros, [p=0.2] faz um dividido por dois [p=0.2] e acha {c}cinquenta por cento. [p=0.3] Seria um erro de meia parede! [p=0.2] Com {d}unidades diferentes, a divisão não vale. [p=0.3] É como na razão: {e}primeiro converta, para as medidas ficarem na mesma unidade. [p=0.2] Só depois, divida."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}com o mesmo número em cima, olhe só embaixo. [p=0.3] Com cada erro na unidade da sua medida, as frações ficam {b}um duzentos avos [p=0.2] e {c}um décimo. [p=0.3] Com o mesmo número em cima, {d}quem tem o menor número embaixo é a fração maior. [p=0.2] Um décimo pesa mais, sem fazer conta."),
    dict(id="s13", block="atalho", text="Funciona porque é como repartir uma pizza: {a}cortada em dez, cada fatia é bem maior que cortada em duzentos. [p=0.3] Não compensa quando {b}os números de cima são diferentes, [p=0.2] como quatro duzentos avos contra três centésimos. [p=0.2] Aí, {c}calcule cada porcentagem."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um marceneiro errou {a}dois milímetros numa peça de dez centímetros. [p=0.2] Um pedreiro errou {b}três centímetros numa parede de cinco metros. [p=0.3] {c}Qual erro pesa mais?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Marceneiro: {a}dez centímetros são cem milímetros. [p=0.2] {b}Dois dividido por cem dá zero vírgula zero dois, [p=0.2] que são {c}dois por cento."),
    dict(id="s17", block="resposta", text="Pedreiro: {a}cinco metros são quinhentos centímetros. [p=0.2] {b}Três dividido por quinhentos dá zero vírgula zero zero seis, [p=0.2] que são {c}zero vírgula seis por cento. [p=0.3] {d}Pesa mais o erro do marceneiro, [p=0.2] mesmo sendo o menor em tamanho. [p=0.3] Se você olhasse só o tamanho, {e}escolheria o pedreiro, [p=0.2] porque três centímetros é mais que dois milímetros. [p=0.2] E erraria."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}erro relativo é o erro dividido pela medida, [p=0.2] {b}sempre na mesma unidade. [p=0.2] {c}Em por cento, ele diz quanto o erro pesa."),
    dict(id="s19", block="fim", text="Na próxima aula, a porcentagem volta para o preço. [p=0.2] Você vê {a}um produto de noventa e seis reais, já com vinte por cento de desconto, [p=0.2] e descobre que ele custava {b}cento e vinte. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
