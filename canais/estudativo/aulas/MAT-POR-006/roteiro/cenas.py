# Estudativo · MAT-POR-006 — Achar o preço antes do aumento ou desconto (Matemática · Porcentagem).
# Habilidade: descobrir que um produto de R$ 96 com 20% de desconto custava R$ 120.
# Pré-requisitos: MAT-POR-004 (fatores de aumento e de desconto), MAT-FRA-018 (dividir por decimal). Próxima: MAT-POR-007.
# Questão inédita, criada para esta aula. Sem equação e sem regra de três: esta cadeia não tem MAT-EQU nem MAT-RAZ.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Achar o preço antes do aumento ou desconto"

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
    dict(id="s01", block="gancho", text="Você pagou {a}noventa e seis reais em um produto, [p=0.2] {b}com vinte por cento de desconto. [p=0.3] Quanto ele custava antes? [p=0.3] Se você somou vinte por cento e achou {c}cento e quinze reais e vinte centavos, [p=0.2] errou por quase cinco reais."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar o preço de antes de qualquer aumento ou desconto, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas. [p=0.2] {b}Os fatores: tirar vinte por cento é multiplicar por zero vírgula oito, [p=0.2] e somar quinze por cento é multiplicar por um vírgula quinze. [p=0.3] E {c}dividir por um número com vírgula, tirando a vírgula do divisor. [p=0.3] Se faltar alguma, procure no canal."),
    # a máquina
    dict(id="s04", block="maquina", text="Pense no desconto como {a}uma máquina. [p=0.2] Entra o preço antigo, [p=0.2] {b}a máquina multiplica por zero vírgula oito, [p=0.2] e {c}sai o preço com desconto."),
    dict(id="s05", block="maquina", text="Só que aqui você tem o que saiu: {a}noventa e seis. [p=0.2] Para descobrir o que entrou, {b}rode a máquina ao contrário. [p=0.3] E o contrário de multiplicar é {c}dividir."),
    # a conta
    dict(id="s06", block="conta", text="A conta é {a}noventa e seis dividido por zero vírgula oito. [p=0.2] O divisor tem {b}uma casa depois da vírgula, [p=0.2] então ande uma casa nos dois números: [p=0.2] {c}novecentos e sessenta dividido por oito."),
    dict(id="s07", block="conta", text="{a}Novecentos e sessenta dividido por oito dá cento e vinte. [p=0.3] O produto custava {b}cento e vinte reais. [p=0.3] Confira: {c}vinte por cento de cento e vinte é vinte e quatro, [p=0.2] e {d}cento e vinte menos vinte e quatro dá noventa e seis. [p=0.2] Bateu."),
    # regra
    dict(id="s08", block="regra", text="A regra vale para qualquer caso: [p=0.2] {a}o preço de antes é o preço de agora dividido pelo fator. [p=0.3] {b}No desconto, o fator é menor que um. [p=0.2] {c}No aumento, maior que um."),
    # aumento
    dict(id="s09", block="aumento", text="Veja com aumento. [p=0.2] Depois de subir {a}quinze por cento, [p=0.2] uma mensalidade ficou em {b}duzentos e trinta reais. [p=0.3] {c}Quanto era antes?"),
    dict(id="s10", block="aumento", text="O fator é {a}um vírgula quinze, com duas casas. [p=0.2] Ande duas casas nos dois números: [p=0.2] {b}duzentos e trinta vira vinte e três mil, [p=0.2] e {c}um vírgula quinze vira cento e quinze."),
    dict(id="s11", block="aumento", text="{a}Cento e quinze vezes dois dá duzentos e trinta. [p=0.2] Então cento e quinze vezes duzentos dá vinte e três mil, [p=0.2] e {b}vinte e três mil dividido por cento e quinze dá duzentos. [p=0.3] A mensalidade era {c}duzentos reais."),
    # erro
    dict(id="s12", block="erro", text="O erro do começo é {a}fazer a porcentagem em cima do preço de agora. [p=0.2] A pessoa calcula {b}vinte por cento de noventa e seis dá dezenove reais e vinte centavos, [p=0.2] soma e acha {c}cento e quinze reais e vinte centavos."),
    dict(id="s13", block="erro", text="Mas o desconto foi de vinte por cento {a}do preço antigo, que é maior. [p=0.3] Teste: {b}tire vinte por cento de cento e quinze reais e vinte centavos. [p=0.2] Sobram {c}noventa e dois reais e dezesseis centavos. [p=0.2] {d}Não dá noventa e seis."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, com frações. [p=0.2] {a}Vinte por cento é um quinto. [p=0.2] Então o preço antigo tem {b}cinco partes, [p=0.2] o desconto levou {c}uma, [p=0.2] e você pagou {d}quatro."),
    dict(id="s15", block="atalho", text="Se quatro partes são noventa e seis, [p=0.2] {a}uma parte é noventa e seis dividido por quatro: vinte e quatro. [p=0.2] O preço antigo tem {b}cinco partes: [p=0.1] {c}cinco vezes vinte e quatro dá cento e vinte. [p=0.3] É a mesma ideia de achar o total a partir da parte: [p=0.2] {d}divide pelo de cima, multiplica pelo de baixo."),
    dict(id="s16", block="atalho", text="Funciona porque {a}vinte por cento vira uma fração simples. [p=0.2] Vale também para {b}vinte e cinco, cinquenta ou setenta e cinco por cento. [p=0.3] Não compensa com {c}um desconto de dezessete por cento: [p=0.2] aí, {d}divida por zero vírgula oitenta e três."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma conta de luz {a}subiu doze por cento [p=0.2] e veio {b}cento e sessenta e oito reais. [p=0.3] {c}Quanto era a conta antes do aumento?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Aumento de doze por cento: fator {a}um vírgula doze. [p=0.2] A conta é {b}cento e sessenta e oito dividido por um vírgula doze. [p=0.3] Duas casas: {c}dezesseis mil e oitocentos dividido por cento e doze."),
    dict(id="s20", block="resposta", text="{a}Cento e sessenta e oito dividido por cento e doze dá um, e sobram cinquenta e seis. [p=0.2] {b}Desça o zero: quinhentos e sessenta dividido por cento e doze dá cinco, e não sobra nada. [p=0.2] {c}Desça o último zero: dá zero. [p=0.3] A conta era de {d}cento e cinquenta reais."),
    dict(id="s21", block="resposta", text="Confira: {a}doze por cento de cento e cinquenta é dezoito. [p=0.2] {b}Cento e cinquenta mais dezoito dá cento e sessenta e oito. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}o preço de agora dividido pelo fator [p=0.2] devolve {b}o preço de antes. [p=0.3] {c}Nunca faça a porcentagem em cima do preço de agora."),
    dict(id="s23", block="fim", text="Na próxima aula, você vai ver que {a}o mesmo lucro de vinte reais [p=0.2] pode ser {b}vinte e cinco por cento ou vinte por cento, [p=0.2] dependendo de ser {c}sobre o custo ou sobre a venda. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
