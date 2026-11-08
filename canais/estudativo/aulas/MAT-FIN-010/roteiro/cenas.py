# Estudativo · MAT-FIN-010 — Taxa real de juros (Matemática · Matemática Financeira).
# Habilidade: descontar 5% de inflação de um rendimento de 10% e achar cerca de 4,8%.
# Pré-requisitos: MAT-FIN-009 (inflação acumulada), MAT-POR-006 (achar o preço antes do aumento). Próxima: MAT-FIN-011.
# Questão inédita, criada para esta aula. Fórmula dos juros compostos fora da cadeia: só fatores de variação.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Taxa real de juros"

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
    dict(id="s01", block="gancho", text="{a}Uma aplicação rendeu dez por cento em um ano. [p=0.2] {b}A inflação do ano foi de cinco por cento. [p=0.3] Você ficou cinco por cento mais rico? [p=0.2] Não. [p=0.2] Cerca de {c}quatro vírgula oito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai descontar a inflação de qualquer rendimento, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Juntar variações seguidas, como a inflação de vários anos, multiplicando os fatores. [p=0.2] E {b}achar o valor de antes, dividindo pelo fator. [p=0.3] Se faltar alguma, procure no canal."),
    # aparente e real
    dict(id="s04", block="nomes", text="Os dez por cento que o banco mostra são a {a}taxa aparente: [p=0.2] quanto o número na sua conta cresceu. [p=0.3] A {b}taxa real é quanto cresceu o que o seu dinheiro compra."),
    dict(id="s05", block="exemplo", text="Veja com {a}mil reais. [p=0.2] Rendendo dez por cento, viram {b}mil e cem. [p=0.3] Mas a inflação foi de cinco por cento: [p=0.2] o que custava mil reais agora custa {c}mil e cinquenta."),
    dict(id="s06", block="exemplo", text="Dos cem reais que você ganhou, {a}cinquenta só cobriram a inflação. [p=0.2] O ganho de verdade são os {b}outros cinquenta. [p=0.3] E eles valem sobre {c}mil e cinquenta, que é o que você precisava ter só para empatar."),
    dict(id="s07", block="exemplo", text="{a}Cinquenta dividido por mil e cinquenta. [p=0.2] Simplificando por cinquenta: {b}um vinte e um avos. [p=0.3] Em por cento, é cem dividido por vinte e um: [p=0.2] cabe quatro vezes e sobram dezesseis, e a conta segue depois da vírgula. [p=0.2] Dá {c}cerca de quatro vírgula oito por cento, [p=0.2] um pouco menos que os cinco por cento de um vigésimo."),
    # regra
    dict(id="s08", block="regra", text="A regra, com fatores. [p=0.2] O fator aparente é {a}o fator real vezes o fator da inflação. [p=0.3] Então, para achar o real, {b}divida o fator aparente pelo fator da inflação: [p=0.2] {c}um vírgula um dividido por um vírgula zero cinco."),
    dict(id="s09", block="regra", text="Ande duas casas em cada número: {a}cento e dez dividido por cento e cinco. [p=0.2] Simplificando por cinco, {b}vinte e dois dividido por vinte e um: [p=0.2] {c}um inteiro e um vinte e um avos. [p=0.2] O mesmo ganho real de cerca de quatro vírgula oito por cento."),
    dict(id="s10", block="regra", text="E se a inflação passar do rendimento? [p=0.2] Rendeu {a}quatro por cento, com inflação de cinco: [p=0.2] o fator real fica {b}menor que um. [p=0.2] O número na conta subiu, mas {c}você compra menos. [p=0.2] É uma taxa real negativa."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}subtrair: dez menos cinco dá cinco por cento. [p=0.3] Teste: cinco por cento de ganho real, mais cinco de inflação, são aumentos seguidos. [p=0.2] Cem reais viram cento e cinco, [p=0.2] e depois {b}cento e dez reais e vinte e cinco centavos. [p=0.2] O rendimento teria de ser {c}dez vírgula vinte e cinco por cento, e não dez."),
    # atalho
    dict(id="s12", block="atalho", text="Mas a subtração serve de {a}atalho para conferir. [p=0.2] Com taxas pequenas, {b}a taxa real fica um pouco abaixo da diferença. [p=0.2] Dez menos cinco dá cinco: a real fica {c}um pouco abaixo de cinco."),
    dict(id="s13", block="atalho", text="Funciona porque dividir pelo fator da inflação {a}encolhe um pouco o ganho. [p=0.3] Não compensa com taxas altas. [p=0.2] Rendeu {b}trinta por cento, com inflação de vinte: [p=0.2] a diferença é dez, mas a real é {c}cento e trinta dividido por cento e vinte, cerca de oito vírgula três por cento. [p=0.3] Nesses casos, {d}faça a divisão."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um investimento rendeu {a}vinte e seis por cento em dois anos. [p=0.2] No mesmo período, a inflação acumulada foi de {b}vinte por cento. [p=0.3] {c}Qual foi a taxa real de juros nesses dois anos?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Divida os fatores: {a}um vírgula vinte e seis dividido por um vírgula dois. [p=0.2] Ande duas casas: {b}cento e vinte e seis dividido por cento e vinte. [p=0.3] Cento e vinte cabe uma vez e sobram seis. [p=0.2] Seis é {c}cinco por cento de cento e vinte. [p=0.2] Fator {d}um vírgula zero cinco: taxa real de cinco por cento nos dois anos."),
    dict(id="s17", block="resposta", text="Confira: {a}um vírgula zero cinco vezes um vírgula dois dá um vírgula vinte e seis. [p=0.2] Bateu. [p=0.2] Quem subtraiu achou {b}seis por cento, e errou."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}a taxa real é o fator aparente dividido pelo fator da inflação. [p=0.2] {b}Subtrair só serve para conferir."),
    dict(id="s19", block="fim", text="Na próxima aula, você descobre {a}os juros escondidos numa compra a prazo: [p=0.2] duzentos reais à vista, ou cem de entrada e mais {b}cento e dez depois. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
