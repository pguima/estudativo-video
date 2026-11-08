# Estudativo · MAT-POR-002 — Calcular porcentagem de cabeça e na conta (Matemática · Porcentagem).
# Habilidade: achar 15% de 80 somando 10% com 5% e calcular 37% de 240 multiplicando por 0,37.
# Pré-requisitos: MAT-FRA-002 (fração de uma quantidade), MAT-FRA-016 (andar com a vírgula), MAT-POR-001 (porcentagem como fração e decimal). Próxima: MAT-POR-003.
# Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Calcular porcentagem de cabeça e na conta"

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
    dict(id="s01", block="gancho", text="{a}Quinze por cento de oitenta. [p=0.3] Dá para fazer de cabeça, em poucos segundos, [p=0.2] e sem decorar tabela nenhuma. [p=0.3] A resposta é {b}doze."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular porcentagem de cabeça e na conta, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}trocar porcentagem por fração ou decimal, [p=0.2] {c}calcular a fração de uma quantidade [p=0.2] e {d}andar com a vírgula. [p=0.3] Se faltar alguma, procure no canal."),
    # dez por cento
    dict(id="s04", block="dez", text="Comece pelo mais útil: {a}dez por cento. [p=0.2] Dez por cento vale {b}um décimo. [p=0.3] E a fração de uma quantidade segue a frase: divide pelo de baixo, multiplica pelo de cima. [p=0.2] Com um décimo, é só {c}dividir por dez."),
    dict(id="s05", block="dez", text="Dividir por dez é {a}andar a vírgula uma casa para a esquerda. [p=0.3] {b}Dez por cento de oitenta dá oito. [p=0.2] {c}Dez por cento de trezentos e quarenta e cinco dá trinta e quatro vírgula cinco."),
    # montar as outras
    dict(id="s06", block="montar", text="Com o dez por cento na mão, você monta quase todas as outras. [p=0.2] {a}Cinco por cento é a metade de dez por cento. [p=0.2] De oitenta, dá {b}quatro. [p=0.3] {c}Vinte por cento é o dobro de dez por cento. [p=0.2] De oitenta, dá {d}dezesseis."),
    dict(id="s07", block="montar", text="E {a}quinze por cento é dez por cento mais cinco por cento. [p=0.2] {b}Oito mais quatro dá doze. [p=0.3] Quinze por cento de oitenta é {c}doze, como no começo. [p=0.3] Precisa de um por cento? [p=0.2] {d}Divida por cem, andando a vírgula duas casas. [p=0.2] {e}Um por cento de oitenta dá zero vírgula oito."),
    # na conta
    dict(id="s08", block="conta", text="Mas e {a}trinta e sete por cento de duzentos e quarenta? [p=0.3] Montar isso de cabeça dá trabalho. [p=0.2] Aqui entra {b}o decimal."),
    dict(id="s09", block="conta", text="Trinta e sete por cento são {a}trinta e sete centésimos. [p=0.2] Pela fração de uma quantidade, você {b}divide por cem e multiplica por trinta e sete. [p=0.3] Multiplicar por {c}zero vírgula trinta e sete faz isso tudo de uma vez."),
    dict(id="s10", block="conta", text="{a}Duzentos e quarenta vezes zero vírgula trinta e sete. [p=0.2] {b}Ignore a vírgula: duzentos e quarenta vezes trinta e sete dá oito mil oitocentos e oitenta. [p=0.3] {c}Ponha as duas casas de volta: oitenta e oito vírgula oito."),
    dict(id="s11", block="conta", text="Confira de cabeça. [p=0.2] Trinta e sete por cento é {a}um pouco menos que quarenta por cento. [p=0.2] Quarenta por cento de duzentos e quarenta é quatro vezes vinte e quatro: {b}noventa e seis. [p=0.3] Oitenta e oito vírgula oito ficou um pouco abaixo. [p=0.2] {c}Faz sentido."),
    # erro
    dict(id="s12", block="erro", text="O erro comum aqui é {a}esquecer as casas. [p=0.2] A pessoa multiplica por trinta e sete e para em {b}oito mil oitocentos e oitenta. [p=0.3] Mas trinta e sete por cento é {c}só um pedaço do total. [p=0.2] O resultado tem que ser {d}menor que duzentos e quarenta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}troque a ordem. [p=0.3] {b}Oito por cento de cinquenta parece chato. [p=0.2] Mas {c}cinquenta por cento de oito é a metade de oito: {d}quatro. [p=0.3] E as contas dão o mesmo resultado."),
    dict(id="s14", block="atalho", text="Funciona porque a conta é sempre a mesma: {a}oito vezes cinquenta, dividido por cem. [p=0.3] Mudar a ordem da multiplicação não muda o resultado. [p=0.2] Não compensa quando {b}nenhum lado fica fácil, como trinta e sete por cento de duzentos e quarenta. [p=0.2] Aí, {c}vá de decimal."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] A conta do restaurante deu {a}cento e quarenta reais. [p=0.2] A taxa de serviço é de {b}quinze por cento. [p=0.3] {c}Quanto é a taxa? [p=0.2] Tente de cabeça."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Dez por cento de cento e quarenta: a vírgula anda uma casa, e fica catorze. [p=0.2] {b}Cinco por cento é a metade disso: sete. [p=0.3] {c}Catorze mais sete dá vinte e um reais de taxa."),
    dict(id="s18", block="resposta", text="Pela conta, o resultado é igual. [p=0.2] {a}Cento e quarenta vezes zero vírgula quinze. [p=0.2] Cento e quarenta vezes quinze dá dois mil e cem. [p=0.2] Com duas casas, {b}vinte e um reais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}de cabeça, parta do dez por cento. [p=0.2] {b}Na conta, multiplique pelo decimal. [p=0.2] E {c}confira se o tamanho do resultado faz sentido."),
    dict(id="s20", block="fim", text="Até aqui, você sabia o total e a porcentagem. [p=0.2] Na próxima aula, você descobre {a}quantos por cento trinta é de cento e vinte, [p=0.2] e {b}acha o total quando só conhece a parte. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
