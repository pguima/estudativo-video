# Estudativo · MAT-RAZ-013 — Dividir em partes diretamente proporcionais (Matemática · Razão e Proporção).
# Habilidade: repartir R$ 1.200 na razão 3 para 5 e dividir o lucro entre sócios pelo capital vezes o tempo de cada um.
# Pré-requisitos: MAT-RAZ-003 (truque do k). Próxima: MAT-RAZ-014.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Dividir em partes diretamente proporcionais"

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
    dict(id="s01", block="gancho", text="Dois sócios abriram um negócio. [p=0.2] {a}Um pôs três mil reais. [p=0.2] {b}O outro pôs cinco mil. [p=0.3] No fim do mês, o lucro foi de {c}mil e duzentos reais. [p=0.3] Metade para cada? [p=0.2] {d}Não seria justo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reparte qualquer valor na proporção certa, [p=0.2] até quando os sócios ficam tempos diferentes, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}o truque do cá. [p=0.2] Dois números na razão três para cinco são {c}três cá e cinco cá, [p=0.2] e o cá é o tamanho de uma parte. [p=0.3] Se faltar, procure no canal."),
    # a ideia
    dict(id="s04", block="ideia", text="Dividir em partes {a}diretamente proporcionais quer dizer: [p=0.2] quem pôs mais leva mais, [p=0.2] na mesma razão. [p=0.3] Os números da razão são {b}os pesos de cada um."),
    dict(id="s05", block="ideia", text="Os capitais são três mil e cinco mil. [p=0.2] A razão entre eles é {a}três para cinco. [p=0.3] Então o lucro vira {b}oito partes iguais: [p=0.2] {c}três partes para o primeiro sócio [p=0.2] e {d}cinco para o segundo."),
    dict(id="s06", block="conta", text="Com o truque do cá: {a}três cá mais cinco cá igual a mil e duzentos. [p=0.3] Juntando, {b}oito cá igual a mil e duzentos. [p=0.3] {c}Mil e duzentos dividido por oito dá cento e cinquenta. [p=0.2] Esse é o cá: {d}o valor de uma parte."),
    dict(id="s07", block="conta", text="{a}Primeiro sócio: três vezes cento e cinquenta dá quatrocentos e cinquenta reais. [p=0.3] {b}Segundo sócio: cinco vezes cento e cinquenta dá setecentos e cinquenta reais. [p=0.3] Conferindo: {c}quatrocentos e cinquenta mais setecentos e cinquenta dá mil e duzentos. [p=0.2] Bateu."),
    # método
    dict(id="s08", block="metodo", text="O método tem {a}três passos. [p=0.2] {b}Some os pesos. [p=0.2] {c}Divida o total pela soma: esse é o cá. [p=0.2] {d}Multiplique o cá pelo peso de cada um. [p=0.3] Vale para quantas pessoas forem."),
    # capital vezes tempo
    dict(id="s09", block="tempo", text="E se os sócios ficam {a}tempos diferentes? [p=0.3] A Carla pôs {b}quatro mil reais, por seis meses. [p=0.2] O Davi pôs {c}três mil reais, por dez meses. [p=0.3] O lucro foi de {d}seis mil e trezentos reais."),
    dict(id="s10", block="tempo", text="Aqui o peso é {a}capital vezes tempo. [p=0.3] Por quê? [p=0.2] Quatro mil reais trabalhando no negócio por seis meses [p=0.2] rendem como {b}vinte e quatro mil por um mês só. [p=0.3] Dinheiro e tempo contam juntos, então {c}se multiplicam."),
    dict(id="s11", block="tempo", text="{a}Carla: quatro mil vezes seis dá vinte e quatro mil. [p=0.3] {b}Davi: três mil vezes dez dá trinta mil. [p=0.3] Números grandes. [p=0.2] Divida cada um pelo mesmo número, como quem simplifica uma fração. [p=0.2] O maior que serve é o MDC: seis mil. [p=0.2] {c}Os pesos ficam quatro e cinco. [p=0.3] Dividir todos os pesos pelo mesmo número não muda a divisão."),
    dict(id="s12", block="tempo", text="{a}Quatro cá mais cinco cá igual a seis mil e trezentos. [p=0.3] {b}Nove cá igual a seis mil e trezentos. [p=0.2] {c}O cá é setecentos. [p=0.3] {d}Carla: quatro vezes setecentos dá dois mil e oitocentos reais. [p=0.3] {e}Davi: cinco vezes setecentos dá três mil e quinhentos reais."),
    dict(id="s13", block="tempo", text="Conferindo: {a}dois mil e oitocentos mais três mil e quinhentos dá seis mil e trezentos. [p=0.3] Repare: a Carla pôs mais dinheiro, [p=0.2] mas {b}o Davi leva mais, porque ficou mais tempo."),
    # erro
    dict(id="s14", block="erro", text="O erro comum aqui é {a}olhar só o capital. [p=0.3] Aí os pesos seriam {b}quatro e três, sete partes. [p=0.3] {c}Seis mil e trezentos dividido por sete dá novecentos. [p=0.3] A Carla levaria {d}três mil e seiscentos reais, [p=0.2] e o Davi, só dois mil e setecentos."),
    dict(id="s15", block="erro", text="A soma fecha, mas {a}o tempo sumiu da história. [p=0.3] Se o enunciado fala em tempo, {b}multiplique capital por tempo antes de tudo."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho. [p=0.2] Muitas questões perguntam {a}quanto um recebeu a mais que o outro. [p=0.3] Não precisa calcular as duas partes. [p=0.2] {b}Multiplique a diferença dos pesos pelo cá."),
    dict(id="s17", block="atalho", text="Davi e Carla têm pesos cinco e quatro: {a}diferença de um. [p=0.3] {b}Um vezes setecentos: o Davi recebe setecentos reais a mais. [p=0.3] Confere com as partes: {c}três mil e quinhentos menos dois mil e oitocentos dá setecentos."),
    dict(id="s18", block="atalho", text="Funciona porque {a}cada parte é o peso vezes o cá. [p=0.2] Tirar uma parte da outra é tirar os pesos, com o mesmo cá. [p=0.3] {b}Não compensa quando a questão pede todas as partes: [p=0.2] aí você calcula cada uma de qualquer jeito."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] A Ana pôs {a}dois mil reais numa sociedade, por nove meses. [p=0.3] A Bia pôs {b}três mil reais, por quatro meses. [p=0.3] O lucro foi de {c}três mil reais. [p=0.3] {d}Quanto cada uma recebe?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] O peso é capital vezes tempo. [p=0.2] {a}Ana: dois mil vezes nove dá dezoito mil. [p=0.3] {b}Bia: três mil vezes quatro dá doze mil. [p=0.3] Dividindo cada um por seis mil, {c}os pesos ficam três e dois."),
    dict(id="s22", block="resposta", text="{a}Três cá mais dois cá igual a três mil. [p=0.3] {b}Cinco cá igual a três mil, e o cá é seiscentos. [p=0.3] {c}Ana: três vezes seiscentos dá mil e oitocentos reais. [p=0.3] {d}Bia: dois vezes seiscentos dá mil e duzentos reais. [p=0.3] Somando, {e}três mil. [p=0.2] Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}some os pesos, [p=0.2] {b}ache o valor de uma parte [p=0.2] e {c}multiplique pelo peso de cada um. [p=0.3] Com tempo na história, {d}o peso é capital vezes tempo."),
    dict(id="s24", block="fim", text="Na próxima aula, você reparte ao contrário: [p=0.2] {a}um prêmio em que quem falta menos leva mais. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
