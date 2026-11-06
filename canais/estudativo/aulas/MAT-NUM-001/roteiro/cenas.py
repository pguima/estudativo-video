# Estudativo · MAT-NUM-001 — Algarismos e valor posicional (Matemática · Números e Contas).
# Habilidade: dizer quanto vale o 3 em 352 e em 235 e escrever 352 como 300 + 50 + 2.
# Pré-requisitos: nenhum. Próxima: MAT-NUM-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Contas: 352 = 300 + 50 + 2 · 235 = 200 + 30 + 5 · 302 = 300 + 0 + 2 · 3002 é outro número.
# Questão: 647 = 600 + 40 + 7 → o 4 vale 40.

TITULO = "Algarismos e valor posicional"

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
    dict(id="s01", block="gancho", text="Olhe para {a}este três. [p=0.3] Num boleto, ele pode valer {b}três reais. [p=0.2] Em outro, {c}trinta. [p=0.2] Em outro, {d}trezentos. [p=0.3] O desenho é o mesmo. [p=0.2] {e}O que muda é o lugar."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai olhar para qualquer número e dizer quanto vale cada pedaço dele, [p=0.2] e ainda leva um {b}atalho de prova."),
    # acolhida
    dict(id="s03", block="acolhida", text="Se faz anos que você não estuda, está no lugar certo. [p=0.3] {a}Você já usa isso toda vez que confere um troco. [p=0.2] A gente só vai dar nome ao que você já faz."),
    # algarismos
    dict(id="s04", block="algarismos", text="Para escrever qualquer número, a gente usa só {a}dez símbolos, [p=0.2] do zero até o nove. [p=0.3] Cada símbolo desses se chama {b}algarismo. [p=0.3] É como as letras: [p=0.2] {c}com poucas letras se escreve qualquer palavra, [p=0.2] e com dez algarismos se escreve qualquer número."),
    dict(id="s05", block="algarismos", text="{a}Trezentos e cinquenta e dois é um número só, [p=0.2] escrito com {b}três algarismos. [p=0.3] A pergunta é: [p=0.2] {c}quanto vale cada um deles?"),
    # casas
    dict(id="s06", block="casas", text="Imagine pagar trezentos e cinquenta e dois reais em dinheiro, [p=0.2] usando só {a}moedas de um real, [p=0.2] {b}notas de dez [p=0.2] e {c}notas de cem."),
    dict(id="s07", block="casas", text="Comece pela ponta direita. [p=0.2] Cada lugar do número se chama casa. [p=0.3] O dois conta {a}moedas de um real. [p=0.3] Essa casa se chama {b}unidade, [p=0.2] porque conta de um em um. [p=0.2] Duas unidades valem {c}dois reais."),
    dict(id="s08", block="casas", text="No meio, o cinco conta {a}notas de dez. [p=0.3] Essa casa se chama {b}dezena. [p=0.2] Dezena é um grupo de dez, [p=0.2] como dúzia é um grupo de doze. [p=0.2] Cinco dezenas valem {c}cinquenta reais."),
    dict(id="s09", block="casas", text="Na ponta esquerda, o três conta {a}notas de cem. [p=0.3] Essa casa se chama {b}centena, [p=0.2] um grupo de cem. [p=0.2] Três centenas valem {c}trezentos reais."),
    # por que
    dict(id="s10", block="troca", text="Por que as casas são assim? [p=0.2] Por causa de {a}uma troca que você já conhece. [p=0.3] {b}Dez moedas de um real valem uma nota de dez. [p=0.2] {c}Dez notas de dez valem uma nota de cem."),
    dict(id="s11", block="troca", text="Por isso, {a}nenhuma casa guarda mais que nove. [p=0.3] Juntou dez, você troca por uma só, [p=0.2] e ela {b}sobe para a casa da esquerda."),
    # mesmo algarismo, outro lugar
    dict(id="s12", block="lugar", text="Troque os mesmos algarismos de lugar: {a}duzentos e trinta e cinco. [p=0.3] Agora {b}o três está no meio, na casa das dezenas. [p=0.2] Ele conta notas de dez: [p=0.2] vale {c}trinta reais."),
    dict(id="s13", block="lugar", text="No primeiro número, {a}valia trezentos. [p=0.2] Aqui, {b}vale trinta. [p=0.3] {c}Mesmo algarismo, lugar diferente, valor diferente. [p=0.3] É isso que se chama {d}valor posicional: [p=0.2] o valor que vem da posição."),
    # abrir o número
    dict(id="s14", block="abrir", text="Com isso, dá para abrir o número. [p=0.2] Trezentos e cinquenta e dois é {a}trezentos, [p=0.2] {b}mais cinquenta, [p=0.2] {c}mais dois. [p=0.3] O sinal de {d}mais quer dizer juntar. [p=0.3] E o próprio nome do número já avisa: [p=0.2] trezentos {e}e cinquenta {f}e dois. [p=0.2] Esse {g}e funciona como um mais escondido."),
    # erro
    dict(id="s15", block="erro", text="O erro mais comum é {a}escrever como se fala. [p=0.2] Ouviu trezentos e dois? [p=0.2] A pessoa escreve {b}o trezentos inteiro e depois o dois. [p=0.3] Saem {c}quatro algarismos, [p=0.2] e esse já é outro número, [p=0.2] bem maior: {d}três mil e dois."),
    dict(id="s16", block="erro", text="Trezentos e dois tem {a}três centenas, [p=0.2] {b}nenhuma dezena [p=0.2] e {c}duas unidades. [p=0.3] Sem nota de dez, {d}a casa do meio fica com zero. [p=0.3] O zero avisa que a casa está vazia, [p=0.2] e segura o lugar: [p=0.2] tire esse zero e {e}o número vira trinta e dois."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho: {a}conte as casas à direita. [p=0.3] Quantas casas vêm depois do algarismo? [p=0.2] Esse é o {b}número de zeros que ele ganha. [p=0.3] Em trezentos e cinquenta e dois, depois do três vêm {c}duas casas: [p=0.2] três com dois zeros dá {d}trezentos. [p=0.3] Em duzentos e trinta e cinco, vem {e}uma casa: [p=0.2] três com um zero dá {f}trinta."),
    dict(id="s18", block="atalho", text="Funciona porque as casas contam {a}de um em um, [p=0.2] {b}de dez em dez [p=0.2] e {c}de cem em cem: [p=0.2] cada passo para a esquerda ganha um zero. [p=0.3] {d}Não compensa quando você quer o número inteiro: [p=0.2] aí, é só ler."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Chegou um boleto de {a}seiscentos e quarenta e sete reais. [p=0.3] {b}Quanto vale o quatro nesse número? [p=0.2] E como fica o número {c}aberto em partes, com o sinal de mais?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] O quatro está {a}no meio, na casa das dezenas. [p=0.2] Depois dele vem {b}uma casa, [p=0.2] então ele ganha um zero: [p=0.2] vale {c}quarenta. [p=0.3] Aberto em partes, fica {d}seiscentos [p=0.2] {e}mais quarenta [p=0.2] {f}mais sete."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}quem dá o valor ao algarismo é o lugar onde ele está."),
    dict(id="s23", block="fim", text="Na próxima aula, os números crescem: [p=0.2] você vai {a}ler números na casa dos milhões [p=0.2] e {b}dizer qual é maior, usando sinais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
