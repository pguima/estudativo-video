# Estudativo · MAT-FRA-005 — Comparar frações e marcar na reta (Matemática · Frações e Decimais).
# Habilidade: dizer qual é maior entre 2/3 e 3/5, pelo MMC ou pelo produto cruzado, e marcar 3/4 e 5/2 numa reta numérica.
# Pré-requisitos: MAT-DIV-005, MAT-FRA-003, MAT-FRA-004, MAT-NUM-015. Próxima: MAT-FRA-006.
# MAT-FRA-002 não está na cadeia: a troca de denominador usa a regra de equivalentes da MAT-FRA-003.

TITULO = "Comparar frações e marcar na reta"

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
    dict(id="s01", block="gancho", text="{a}Dois terços ou {b}três quintos: qual é maior? [p=0.3] Três e cinco são números maiores, {c}então três quintos ganha? [p=0.3] Não. [p=0.2] Em fração, o tamanho dos números engana."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}comparar frações por dois caminhos, [p=0.2] {b}marcar frações na reta [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}quatro coisas: [p=0.2] {b}frações equivalentes, [p=0.2] {c}o MMC, [p=0.2] {d}número misto [p=0.2] e {e}a reta numérica. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # pedaços
    dict(id="s04", block="pedacos", text="Comparar fração é fácil em um caso: [p=0.2] quando {a}o de baixo é igual. [p=0.3] {b}Cinco sétimos e três sétimos têm pedaços do mesmo tamanho. [p=0.2] Quem tem mais pedaços ganha: {c}cinco sétimos é maior."),
    dict(id="s05", block="pedacos", text="Com dois terços e três quintos, os pedaços têm {a}tamanhos diferentes. [p=0.3] Contar pedaços não adianta. [p=0.2] A saída é cortar tudo no {b}mesmo tamanho."),
    # MMC
    dict(id="s06", block="mmc", text="Aqui entra o {a}MMC, o mínimo múltiplo comum: [p=0.2] o menor número que aparece na tabuada do três e também na do cinco. [p=0.3] MMC de três e cinco: {b}quinze."),
    dict(id="s07", block="mmc", text="Troque cada fração por uma equivalente com quinze embaixo. [p=0.3] {a}Dois terços: do três para o quinze, multiplicou por cinco. [p=0.2] Faça o mesmo em cima: {b}dois vezes cinco, dez. [p=0.2] {c}Dez quinze avos."),
    dict(id="s08", block="mmc", text="{a}Três quintos: do cinco para o quinze, multiplicou por três. [p=0.2] {b}Três vezes três, nove. [p=0.2] {c}Nove quinze avos."),
    dict(id="s09", block="mmc", text="Pedaços iguais, é só contar: {a}dez é maior que nove. [p=0.3] Então {b}dois terços é maior que três quintos. [p=0.2] Por pouco, mas é."),
    # erro
    dict(id="s10", block="erro", text="Esse é o erro mais comum: {a}achar que número maior é fração maior. [p=0.3] Compare {b}um meio e {c}um oitavo na barra de chocolate."),
    dict(id="s11", block="erro", text="Oito é maior que dois, mas {a}cortar em oito dá pedaços menores. [p=0.3] Quanto maior o de baixo, {b}menor o pedaço. [p=0.2] Por isso, nenhum número sozinho decide."),
    # atalho
    dict(id="s12", block="atalho", text="E o atalho prometido: {a}o teste da cruz, o mesmo produto cruzado da aula de frações equivalentes. [p=0.3] Lá, ele dizia se duas frações eram iguais. [p=0.2] Ele também diz {b}qual é a maior."),
    dict(id="s13", block="atalho", text="Multiplique em cruz, e deixe cada resultado {a}do lado da fração que deu o número de cima. [p=0.3] {b}Dois vezes cinco, dez, do lado de dois terços. [p=0.2] {c}Três vezes três, nove, do lado de três quintos. [p=0.3] {d}Dez é maior que nove: dois terços é maior."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a cruz deixa as duas frações com o mesmo número embaixo: [p=0.2] aqui, {b}três vezes cinco, sem escrever. [p=0.3] Não compensa com {c}três frações ou mais, [p=0.2] porque ela só compara de duas em duas. [p=0.2] Aí, {d}use o MMC."),
    # reta
    dict(id="s15", block="reta", text="Vamos para a reta. [p=0.2] A reta numérica é {a}uma linha com os números em ordem, [p=0.2] e {b}quanto mais à direita, maior o número. [p=0.3] Fração também tem lugar nela."),
    dict(id="s16", block="reta", text="Para marcar {a}três quartos: [p=0.2] o de cima é menor que o de baixo, então fica {b}entre zero e um. [p=0.3] {c}Corte esse trecho em quatro partes iguais [p=0.2] e {d}ande três partes a partir do zero."),
    dict(id="s17", block="reta", text="Para marcar {a}cinco meios: [p=0.2] o de cima é maior, então vire número misto. [p=0.3] {b}Cinco dividido por dois dá dois e sobra um: [p=0.2] {c}dois inteiros e um meio. [p=0.3] {d}Vá até o dois [p=0.2] e {e}ande metade do caminho até o três."),
    dict(id="s18", block="reta", text="Na reta, {a}três quartos fica antes do um, [p=0.2] e {b}cinco meios fica depois do dois. [p=0.3] Você vê a comparação sem conta: {c}cinco meios está mais à direita, então é maior."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Duas garrafas iguais de suco. [p=0.2] Uma está com {a}quatro sétimos, [p=0.1] a outra com {b}três quintos. [p=0.3] {c}Qual tem mais suco?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá, pela cruz. [p=0.2] {a}Quatro vezes cinco, vinte, do lado de quatro sétimos. [p=0.2] {b}Sete vezes três, vinte e um, do lado de três quintos. [p=0.3] {c}Vinte e um é maior: a garrafa com três quintos tem mais suco."),
    dict(id="s22", block="resposta", text="Pelo MMC dá o mesmo: {a}vinte trinta e cinco avos [p=0.2] contra {b}vinte e um trinta e cinco avos."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}para comparar, deixe os pedaços do mesmo tamanho, [p=0.2] ou use {b}a cruz. [p=0.3] {c}Na reta, quanto mais à direita, maior."),
    dict(id="s24", block="fim", text="Na próxima aula, você vai {a}praticar: simplificar, comparar e calcular a fração de uma quantidade em situações do dia a dia. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
