# Estudativo · MAT-FIN-009 — Inflação acumulada e poder de compra (Matemática · Matemática Financeira).
# Habilidade: achar que 5% e 4% acumulam 9,2% e dizer que preços 25% mais altos tiram 20% do poder de compra.
# Pré-requisitos: MAT-POR-010 (aumentos e descontos sucessivos), MAT-POR-011 (voltar ao valor original). Próxima: MAT-FIN-010.
# Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Inflação acumulada e poder de compra"

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
    dict(id="s01", block="gancho", text="{a}A inflação foi de cinco por cento em um ano {b}e de quatro por cento no ano seguinte. [p=0.3] Os preços subiram nove por cento? [p=0.2] Quase. [p=0.2] Subiram {c}nove vírgula dois."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai acumular inflação e medir quanto o seu dinheiro perde, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Aumentos seguidos se juntam multiplicando os fatores. [p=0.2] E {b}para desfazer uma variação, divida um pelo fator. [p=0.3] Se faltar alguma, procure no canal."),
    # inflação acumulada
    dict(id="s04", block="acumulada", text="{a}Inflação é a subida geral dos preços, medida em por cento. [p=0.3] Inflação de cinco por cento num ano quer dizer que, em média, [p=0.2] {b}o que custava cem reais passou a custar cento e cinco."),
    dict(id="s05", block="acumulada", text="No ano seguinte, os quatro por cento valem sobre {a}os preços que já subiram. [p=0.2] São aumentos seguidos: {b}multiplique os fatores. [p=0.3] {c}Um vírgula zero cinco vezes um vírgula zero quatro."),
    dict(id="s06", block="acumulada", text="Sem as vírgulas, {a}cento e cinco vezes cento e quatro dá dez mil novecentos e vinte. [p=0.2] Com quatro casas, {b}um vírgula zero nove dois. [p=0.3] Tire o inteiro: {c}nove vírgula dois por cento. [p=0.2] Essa é a {d}inflação acumulada, a subida total do período."),
    dict(id="s07", block="acumulada", text="O atalho de aumentos seguidos confirma. [p=0.2] {a}Cinco mais quatro dá nove. [p=0.2] {b}Cinco vezes quatro dá vinte, dividido por cem dá zero vírgula dois. [p=0.2] Juntos, {c}nove vírgula dois."),
    # poder de compra
    dict(id="s08", block="poder", text="Agora, o outro lado. [p=0.2] {a}Poder de compra é quanto o seu dinheiro consegue comprar. [p=0.3] Imagine um pacote de café a {b}vinte reais. [p=0.2] Com cem reais, você leva {c}cinco pacotes."),
    dict(id="s09", block="poder", text="Os preços sobem {a}vinte e cinco por cento, e o seu dinheiro continua o mesmo. [p=0.2] O café vai para {b}vinte e cinco reais. [p=0.2] Com cem reais, agora você leva {c}quatro pacotes."),
    dict(id="s10", block="poder", text="Eram cinco e ficaram quatro. [p=0.2] Você perdeu {a}um pacote em cinco: [p=0.2] um quinto, que são {b}vinte por cento do poder de compra. [p=0.3] Os preços subiram vinte e cinco, [p=0.2] mas a perda é de {c}vinte."),
    dict(id="s11", block="poder", text="A regra: o poder de compra novo é {a}um dividido pelo fator da inflação. [p=0.2] {b}Um dividido por um vírgula vinte e cinco dá zero vírgula oito. [p=0.2] O dinheiro compra oitenta por cento do que comprava: {c}perda de vinte por cento."),
    dict(id="s12", block="poder", text="É a conta de voltar ao valor original, vista do outro lado. [p=0.2] Para recuperar o que comprava, {a}o salário precisa subir vinte e cinco por cento, [p=0.2] {b}o mesmo que os preços."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é achar que {a}preço vinte e cinco por cento mais alto tira vinte e cinco por cento do poder de compra. [p=0.3] Se fosse assim, com cem reais você levaria {b}três pacotes e três quartos. [p=0.2] Mas você leva {c}quatro."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, com frações. [p=0.2] {a}Vinte e cinco por cento é um quarto. [p=0.2] Os preços tinham quatro partes e ganharam uma: {b}ficaram cinco. [p=0.2] O seu dinheiro paga {c}quatro dessas cinco: perdeu um quinto."),
    dict(id="s15", block="atalho", text="{a}Subiu um quarto, perde um quinto. [p=0.2] {b}Subiu um terço, perde um quarto. [p=0.3] Funciona porque a perda é medida sobre {c}o preço novo, que é maior. [p=0.2] Não compensa quando a inflação não vira fração simples, como sete por cento: [p=0.2] aí, {d}divida um pelo fator."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Num país em época de inflação alta, os preços subiram {a}vinte e cinco por cento em um ano {b}e vinte por cento no seguinte. [p=0.2] O salário de Ana não mudou. [p=0.3] {c}Qual foi a inflação acumulada? [p=0.2] E {d}quanto Ana perdeu de poder de compra?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Fatores: {a}um vírgula vinte e cinco e um vírgula dois. [p=0.2] Sem as vírgulas, {b}cento e vinte e cinco vezes doze dá mil e quinhentos. [p=0.2] Com três casas, {c}um vírgula cinco: inflação acumulada de cinquenta por cento. [p=0.2] Quem somou achou {d}quarenta e cinco."),
    dict(id="s19", block="resposta", text="Agora o poder de compra. [p=0.2] Cinquenta por cento é metade: os preços tinham {a}duas partes e ganharam uma, ficaram três. [p=0.2] O dinheiro de Ana paga {b}duas dessas três. [p=0.2] Ela perdeu {c}um terço, cerca de trinta e três por cento. [p=0.3] Pelo fator: {d}um dividido por um vírgula cinco dá dois terços."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}inflação se acumula multiplicando os fatores, [p=0.2] e o poder de compra se mede {b}dividindo um pelo fator."),
    dict(id="s21", block="fim", text="Na próxima aula, você usa isso num rendimento. [p=0.2] Uma aplicação rendeu {a}dez por cento, a inflação foi de cinco, [p=0.2] e o seu ganho de verdade {b}não é cinco por cento. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
