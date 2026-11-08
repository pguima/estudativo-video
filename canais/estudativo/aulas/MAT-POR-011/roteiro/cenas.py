# Estudativo · MAT-POR-011 — Voltar ao valor original (Matemática · Porcentagem).
# Habilidade: descobrir que quem caiu 20% precisa subir 25% para voltar.
# Pré-requisitos: MAT-POR-010 (sucessivos), MAT-POR-005 (variação percentual), MAT-FRA-018 (dividir por decimal). Próxima: MAT-POR-012.
# Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Voltar ao valor original"

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
    dict(id="s01", block="gancho", text="Um salário foi {a}cortado em vinte por cento. [p=0.2] Meses depois, ganhou {b}um aumento de vinte por cento. [p=0.3] Voltou ao que era? [p=0.3] {c}Não. Para voltar, o aumento precisava ser de vinte e cinco por cento."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber quanto qualquer valor precisa subir para se recuperar de uma queda, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas. [p=0.2] {b}A variação percentual: a diferença dividida pelo valor de antes. [p=0.2] {c}Juntar variações seguidas, multiplicando os fatores. [p=0.2] E {d}dividir por um número com vírgula. [p=0.3] Se faltar alguma, procure no canal."),
    # com cem reais
    dict(id="s04", block="cem", text="Comece com {a}cem reais. [p=0.2] Cai vinte por cento: {b}oitenta. [p=0.3] Sobe vinte por cento, agora sobre oitenta: [p=0.2] {c}dezesseis reais a mais, noventa e seis. [p=0.2] {d}Não chegou a cem."),
    dict(id="s05", block="cem", text="Para voltar a cem, você precisa {a}ganhar vinte reais. [p=0.2] E o valor de antes, agora, é {b}oitenta, não cem. [p=0.3] {c}Vinte dividido por oitenta: zero vírgula vinte e cinco. [p=0.2] {d}Vinte e cinco por cento. [p=0.2] É a variação percentual {e}de oitenta para cem."),
    dict(id="s06", block="cem", text="O motivo: {a}a queda foi calculada sobre um valor maior, [p=0.2] e a subida é calculada {b}sobre um valor menor. [p=0.2] Para recuperar os mesmos vinte reais, {c}a porcentagem precisa ser maior."),
    # fatores
    dict(id="s07", block="fator", text="Com fatores: [p=0.2] cair vinte por cento é {a}multiplicar por zero vírgula oito. [p=0.2] Para voltar, você quer {b}um fator que, vezes zero vírgula oito, dê um. [p=0.3] Esse fator é {c}um dividido por zero vírgula oito."),
    dict(id="s08", block="fator", text="Ande uma casa nos dois números: {a}dez dividido por oito dá um vírgula vinte e cinco. [p=0.2] Fator {b}um vírgula vinte e cinco: subir vinte e cinco por cento. [p=0.3] Confira: {c}oitenta vezes um vírgula vinte e cinco dá cem. [p=0.3] A regra: {d}para voltar, divida um pelo fator."),
    dict(id="s09", block="fator", text="Vale para qualquer queda. [p=0.2] {a}Caiu cinquenta por cento? [p=0.2] {b}Um dividido por zero vírgula cinco dá dois. [p=0.2] Fator dois é dobrar: {c}precisa subir cem por cento. [p=0.3] E vale ao contrário: {d}subiu vinte e cinco por cento? [p=0.2] {e}Um dividido por um vírgula vinte e cinco dá zero vírgula oito: [p=0.1] cair vinte por cento desfaz."),
    # erro
    dict(id="s10", block="erro", text="O erro comum é {a}subir a mesma porcentagem que caiu. [p=0.2] {b}Zero vírgula oito vezes um vírgula dois dá zero vírgula noventa e seis. [p=0.2] {c}Ainda faltam quatro por cento do valor original."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho, com frações. [p=0.2] {a}Vinte por cento é um quinto. [p=0.2] O valor tinha {b}cinco partes e perdeu uma: ficaram {c}quatro. [p=0.3] Para voltar, você precisa ganhar {d}uma parte em cima das quatro que ficaram: [p=0.2] {e}um quarto, vinte e cinco por cento."),
    dict(id="s12", block="atalho", text="{a}Perdeu um quinto, ganha um quarto. [p=0.2] {b}Perdeu um quarto, ganha um terço, cerca de trinta e três por cento. [p=0.2] {c}Perdeu um décimo, ganha um nono, cerca de onze por cento. [p=0.3] Funciona porque {d}o que falta é o mesmo, mas agora vai sobre o que ficou. [p=0.2] Não compensa quando a queda {e}não vira fração simples, como dezessete por cento: [p=0.2] aí, {f}divida um pelo fator."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Uma sorveteria vendia {a}quarenta mil reais por mês no verão. [p=0.2] No inverno, as vendas {b}caíram setenta e cinco por cento. [p=0.3] {c}Quantos por cento as vendas precisam subir para voltar ao que eram?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}Setenta e cinco por cento de quarenta mil são trinta mil. [p=0.2] As vendas ficaram em {b}dez mil. [p=0.3] Para voltar, precisam ganhar {c}trinta mil, sobre dez mil. [p=0.2] {d}Trinta mil dividido por dez mil dá três: [p=0.1] {e}trezentos por cento."),
    dict(id="s16", block="resposta", text="Pelo fator: {a}caiu setenta e cinco, fator zero vírgula vinte e cinco. [p=0.2] {b}Um dividido por zero vírgula vinte e cinco dá quatro. [p=0.2] Fator quatro é {c}o valor inteiro mais três vezes ele: subir trezentos por cento. [p=0.3] Confira: {d}dez mil vezes quatro dá quarenta mil. [p=0.3] Quem respondeu setenta e cinco {e}parou em dezessete mil e quinhentos."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}para voltar, divida um pelo fator, [p=0.2] ou {b}calcule o que falta sobre o valor que ficou. [p=0.3] Depois de uma queda, {c}a volta sempre pede uma porcentagem maior."),
    dict(id="s18", block="fim", text="Na próxima aula, você vê por que passar de {a}oito por cento para dez por cento [p=0.2] é subir {b}dois pontos percentuais, [p=0.2] e também {c}vinte e cinco por cento. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
