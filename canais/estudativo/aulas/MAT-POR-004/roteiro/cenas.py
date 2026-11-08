# Estudativo · MAT-POR-004 — Fatores de aumento e de desconto (Matemática · Porcentagem).
# Habilidade: somar 15% a um preço multiplicando por 1,15 e tirar 20% multiplicando por 0,8.
# Pré-requisitos: MAT-POR-002 (porcentagem de um valor), MAT-FRA-016 (multiplicar decimais). Próxima: MAT-POR-005.
# Questão inédita, criada para esta aula. Soma de decimais fora da ficha: o fator sai de cem mais ou menos a taxa, em por cento.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Fatores de aumento e de desconto"

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
    dict(id="s01", block="gancho", text="Um produto de {a}duzentos reais vai subir {b}quinze por cento. [p=0.3] O normal é calcular o aumento e depois somar. [p=0.2] São {c}duas contas. [p=0.3] Dá para fazer com {d}uma só."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai aumentar e descontar com uma multiplicação, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}trocar porcentagem por decimal [p=0.2] e {c}calcular a porcentagem de um valor. [p=0.3] Se faltar alguma, procure no canal."),
    # jeito longo
    dict(id="s04", block="longo", text="Primeiro, do jeito longo. [p=0.2] {a}Quinze por cento de duzentos: [p=0.2] dez por cento dá vinte, e cinco por cento dá dez. [p=0.3] O aumento é de {b}trinta reais. [p=0.2] Preço novo: {c}duzentos mais trinta dá duzentos e trinta reais."),
    # fator de aumento
    dict(id="s05", block="aumento", text="Agora pense assim. [p=0.2] O preço antigo é {a}cem por cento. [p=0.2] Com o aumento, o cliente paga {b}cem por cento mais quinze por cento. [p=0.3] Ao todo, {c}cento e quinze por cento do preço antigo."),
    dict(id="s06", block="aumento", text="Cento e quinze por cento são cento e quinze centésimos: {a}um vírgula quinze. [p=0.2] Então o preço novo é {b}duzentos vezes um vírgula quinze. [p=0.3] Sem a vírgula, duzentos vezes cento e quinze dá vinte e três mil. [p=0.2] Com duas casas, {c}duzentos e trinta reais."),
    dict(id="s07", block="aumento", text="O mesmo resultado, numa conta só. [p=0.2] Esse um vírgula quinze se chama {a}fator de aumento: [p=0.2] o número que você multiplica para aplicar o aumento. [p=0.3] Repare: com o fator, você {b}nem calcula o aumento separado."),
    # fator de desconto
    dict(id="s08", block="desconto", text="Com desconto, a ideia é a mesma, só que {a}tirando. [p=0.2] Um tênis de {b}duzentos e cinquenta reais está com {c}vinte por cento de desconto. [p=0.3] O cliente paga {d}cem por cento menos vinte por cento, [p=0.2] que dá oitenta por cento do preço."),
    dict(id="s09", block="desconto", text="Oitenta por cento é {a}zero vírgula oito. [p=0.2] {b}Duzentos e cinquenta vezes zero vírgula oito dá duzentos reais. [p=0.3] Esse zero vírgula oito é o {c}fator de desconto."),
    # regra
    dict(id="s10", block="regra", text="A regra: {a}no aumento, cem mais a taxa. [p=0.2] {b}No desconto, cem menos a taxa. [p=0.2] Depois, {c}passe para decimal e multiplique. [p=0.3] {d}Aumento de oito por cento: cento e oito por cento, fator um vírgula zero oito. [p=0.2] {e}Desconto de trinta e cinco por cento: sessenta e cinco por cento, fator zero vírgula sessenta e cinco."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com um erro comum: {a}aumento de cinco por cento vira um vírgula cinco. [p=0.3] Mas um vírgula cinco são {b}cento e cinquenta por cento: [p=0.2] isso é um aumento de {c}cinquenta por cento."),
    dict(id="s12", block="erro", text="Cem mais cinco dá {a}cento e cinco por cento. [p=0.2] O fator certo é {b}um vírgula zero cinco, [p=0.2] com o zero guardando a casa dos décimos."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho de prova: {a}leia o fator ao contrário. [p=0.3] Viu {b}vezes zero vírgula sete? [p=0.2] O cliente paga setenta por cento, então foi {c}desconto de trinta por cento. [p=0.3] Viu {d}vezes um vírgula vinte e cinco? [p=0.2] Foi {e}aumento de vinte e cinco por cento."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o fator é o preço novo, em por cento do antigo. [p=0.3] Já a conta com fator nem sempre compensa. [p=0.2] Em conta redonda de cabeça, como {b}dez por cento de desconto em cinquenta reais, [p=0.2] tire cinco e pague {c}quarenta e cinco."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma conta de luz de {a}cento e oitenta reais vai subir {b}doze por cento. [p=0.3] E um fogão de {c}seiscentos reais está com {d}quinze por cento de desconto. [p=0.3] {e}Qual é o fator e o valor novo de cada um?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Na conta de luz, cem mais doze dá cento e doze por cento: {a}fator um vírgula doze. [p=0.2] {b}Cento e oitenta vezes cento e doze dá vinte mil cento e sessenta. [p=0.2] Com duas casas, {c}duzentos e um reais e sessenta centavos."),
    dict(id="s18", block="resposta", text="No fogão, cem menos quinze dá oitenta e cinco por cento: {a}fator zero vírgula oitenta e cinco. [p=0.2] {b}Seiscentos vezes oitenta e cinco dá cinquenta e um mil. [p=0.2] Com duas casas, {c}quinhentos e dez reais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}aumento, cem mais a taxa. [p=0.2] {b}Desconto, cem menos a taxa. [p=0.2] {c}Passe para decimal e multiplique uma vez só."),
    dict(id="s20", block="fim", text="Até aqui, você já sabia a porcentagem. [p=0.2] Na próxima aula, é o contrário: um preço {a}passou de oitenta para cem reais, [p=0.2] e você descobre {b}de quantos por cento foi o aumento. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
