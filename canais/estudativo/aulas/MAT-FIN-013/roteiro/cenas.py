# Estudativo · MAT-FIN-013 — Rendimento líquido (Matemática · Matemática Financeira).
# Habilidade: descontar 15% de imposto só sobre o rendimento de uma aplicação e comparar duas opções.
# Pré-requisitos: MAT-FIN-004 (juros compostos), MAT-POR-002 (porcentagem de cabeça). Próxima: MAT-FIN-014.
# Questão inédita, criada para esta aula. Os 15% são o dado da questão, não a alíquota real de nenhuma aplicação.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Rendimento líquido"

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
    dict(id="s01", block="gancho", text="{a}Você aplicou dez mil reais, e a aplicação chegou a onze mil. [p=0.2] O imposto é de {b}quinze por cento. [p=0.3] Você leva para casa nove mil trezentos e cinquenta? [p=0.2] Não. [p=0.2] {c}Dez mil oitocentos e cinquenta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai descontar o imposto do jeito certo e comparar duas aplicações, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Porcentagem de cabeça: quinze por cento é dez por cento mais cinco. [p=0.2] E o {b}montante dos juros compostos: o capital vezes o fator, período a período. [p=0.3] Se faltar alguma, procure no canal."),
    # bruto, imposto, líquido
    dict(id="s04", block="nomes", text="Primeiro, os nomes. [p=0.2] Montante é o valor final, e capital é o que você aplicou. [p=0.2] {a}Rendimento bruto é o montante menos o capital. [p=0.2] Onze mil menos dez mil dá {b}mil reais."),
    dict(id="s05", block="nomes", text="Neste exemplo, o {a}imposto é de quinze por cento, e vale só sobre o rendimento. [p=0.2] Quinze por cento de mil: {b}cem mais cinquenta dá cento e cinquenta. [p=0.3] O que sobra é o {c}rendimento líquido: [p=0.2] mil menos cento e cinquenta dá {d}oitocentos e cinquenta."),
    dict(id="s06", block="nomes", text="Você leva para casa {a}o capital mais o rendimento líquido: [p=0.2] {b}dez mil oitocentos e cinquenta reais."),
    # regra
    dict(id="s07", block="regra", text="A regra: [p=0.2] {a}o rendimento líquido é o bruto vezes zero vírgula oitenta e cinco. [p=0.2] Tirar quinze por cento é {b}ficar com oitenta e cinco. [p=0.3] E vale também para a taxa: {c}dez por cento brutos viram oito vírgula cinco líquidos."),
    # juros compostos
    dict(id="s08", block="compostos", text="Com juros compostos, a ideia é a mesma. [p=0.2] {a}Dez mil reais a dez por cento ao ano, por dois anos. [p=0.2] Fator {b}um vírgula vinte e um: montante de doze mil e cem. [p=0.3] Rendimento bruto: {c}dois mil e cem."),
    dict(id="s09", block="compostos", text="Imposto: dez por cento de dois mil e cem dá {a}duzentos e dez; [p=0.2] cinco por cento, {b}cento e cinco. [p=0.2] Juntos, {c}trezentos e quinze. [p=0.2] Líquido: {d}mil setecentos e oitenta e cinco reais. [p=0.3] Repare: {e}o imposto vale sobre o rendimento do período todo, de uma vez."),
    # comparar
    dict(id="s10", block="comparar", text="Agora, comparar. [p=0.2] A aplicação A rende {a}dez por cento ao ano, com quinze por cento de imposto. [p=0.2] A aplicação B rende {b}nove por cento ao ano, sem imposto. [p=0.3] A taxa maior engana. [p=0.2] Líquido de A: {c}oito vírgula cinco por cento. [p=0.2] B rende {d}nove: B ganha. [p=0.3] Em reais, com dez mil aplicados, {e}A deixa oitocentos e cinquenta, e B, novecentos."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é tirar o imposto {a}de tudo, até do capital. [p=0.2] Quinze por cento de onze mil dá {b}mil seiscentos e cinquenta, [p=0.2] e sobrariam {c}nove mil trezentos e cinquenta: [p=0.2] menos do que você aplicou! [p=0.3] O imposto {d}nunca come o capital."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho para comparar: [p=0.2] {a}tire da taxa bruta dez por cento dela, e mais cinco por cento dela. [p=0.3] Doze por cento brutos: tire {b}um vírgula dois e zero vírgula seis. [p=0.2] Sobram {c}dez vírgula dois por cento líquidos."),
    dict(id="s13", block="atalho", text="Funciona porque o imposto é {a}uma fração fixa do rendimento, [p=0.2] então tirar quinze por cento do rendimento ou da taxa dá no mesmo. [p=0.3] Não compensa quando os prazos são diferentes, [p=0.2] ou quando a aplicação dura vários períodos: [p=0.2] aí, {b}calcule o rendimento do período todo em reais."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Você tem {a}vinte mil reais para aplicar por um ano. [p=0.2] Opção A: {b}doze por cento ao ano, com quinze por cento de imposto sobre o rendimento. [p=0.2] Opção B: {c}dez por cento ao ano, sem imposto. [p=0.3] {d}Qual rende mais, e quanto a mais?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Em A, o bruto é doze por cento de vinte mil: {a}dois mil e quatrocentos. [p=0.2] Imposto: dez por cento, duzentos e quarenta; [p=0.2] cinco por cento, cento e vinte. [p=0.2] Juntos, {b}trezentos e sessenta. [p=0.2] Líquido: {c}dois mil e quarenta reais."),
    dict(id="s17", block="resposta", text="Em B, dez por cento de vinte mil: {a}dois mil, sem desconto. [p=0.3] A rende mais, por {b}quarenta reais. [p=0.2] Pelo atalho: doze por cento brutos viram {c}dez vírgula dois líquidos, contra dez. [p=0.3] Nem sempre {d}a aplicação sem imposto ganha: faça a conta."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}o imposto vale só sobre o rendimento. [p=0.2] Compare sempre {b}o líquido."),
    dict(id="s19", block="fim", text="Na próxima aula, é hora de praticar. [p=0.2] Você junta {a}taxas, inflação, compras a prazo, financiamentos e aplicações [p=0.2] para escolher {b}a melhor proposta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
