# Estudativo · MAT-TOP-005 — Princípio da inclusão-exclusão (Matemática · Tópicos Avançados · Binômio, distribuição binomial e casa dos pombos).
# Habilidade: contar quantos números de 1 a 100 são múltiplos de 2 ou 3 (50 + 33 − 16 = 67) e estender a conta para 2, 3 ou 5 (74).
# Pré-requisitos: MAT-CON-003 (Venn e n(A ∪ B) = n(A) + n(B) − n(A ∩ B)), MAT-DIV-005 (MMC). Próxima: MAT-TOP-019.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Leitura da fórmula como na MAT-CON-003 ("ene da união é ene de á, mais ene de bê,
# menos ene da interseção"). Contar múltiplos = dividir e ignorar o resto (divisão com resto, MAT-NUM-009).

TITULO = "Princípio da inclusão-exclusão"

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
    dict(id="s01", block="gancho", text="De um a cem, quantos números são {a}múltiplos de dois ou de três? [p=0.3] São {b}cinquenta múltiplos de dois [p=0.2] e {c}trinta e três de três. [p=0.2] Muita gente soma e responde {d}oitenta e três. [p=0.3] A resposta certa é {e}sessenta e sete."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta uniões sem contar nenhum número duas vezes, [p=0.2] com dois e com três conjuntos, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas. [p=0.2] {b}A fórmula da união: ene da união é ene de á, mais ene de bê, menos ene da interseção. [p=0.2] E {c}o MMC, o menor múltiplo comum. [p=0.3] Se faltar alguma, procure no canal."),
    # contar múltiplos
    dict(id="s04", block="contar", text="Primeiro, como contar múltiplos sem listar: [p=0.2] {a}divida e ignore o resto. [p=0.3] {b}Cem dividido por dois dá cinquenta: cinquenta múltiplos de dois. [p=0.2] {c}Cem dividido por três dá trinta e três, e sobra um: [p=0.2] trinta e três múltiplos de três. [p=0.3] O resto só mostra que {d}o último pedaço não completou mais um múltiplo."),
    dict(id="s05", block="contar", text="Por que oitenta e três está errado? [p=0.2] Números como {a}seis, doze e dezoito [p=0.2] são múltiplos de dois e de três ao mesmo tempo. [p=0.2] {b}Entraram na conta do dois e na conta do três: [p=0.2] foram contados {c}duas vezes."),
    dict(id="s06", block="contar", text="Quem é múltiplo de dois e de três ao mesmo tempo é {a}múltiplo do MMC, seis. [p=0.2] {b}Cem dividido por seis dá dezesseis, e sobra quatro. [p=0.3] Tire os repetidos uma vez: [p=0.2] {c}cinquenta mais trinta e três, menos dezesseis, [p=0.2] dá {d}sessenta e sete."),
    # regra
    dict(id="s07", block="regra", text="Esse é o {a}princípio da inclusão-exclusão. [p=0.2] {b}Inclua cada conjunto inteiro, [p=0.2] e {c}exclua o que foi contado duas vezes. [p=0.3] Com dois conjuntos, {d}é a fórmula da união que você já conhece."),
    # três conjuntos
    dict(id="s08", block="tres", text="E com {a}dois, três ou cinco? [p=0.2] Primeiro, {b}some os três conjuntos: [p=0.2] múltiplos de cinco são {c}cem dividido por cinco, vinte. [p=0.2] Cinquenta mais trinta e três mais vinte dá {d}cento e três."),
    dict(id="s09", block="tres", text="{a}Depois, tire as duplas, cada uma pelo MMC: [p=0.2] {b}de dois e três, os múltiplos de seis: dezesseis. [p=0.2] {c}De dois e cinco, os de dez: dez. [p=0.2] {d}De três e cinco, os de quinze: seis. [p=0.3] Cento e três menos trinta e dois dá {e}setenta e um."),
    dict(id="s10", block="tres", text="Mas falta um detalhe. [p=0.2] Os múltiplos de dois, três e cinco ao mesmo tempo, {a}os de trinta, no miolo do diagrama, [p=0.2] foram {b}somados três vezes e tirados três vezes: [p=0.2] {c}sumiram da conta. [p=0.3] {d}Cem dividido por trinta dá três. [p=0.2] Devolva: {e}setenta e um mais três, setenta e quatro."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}multiplicar em vez de usar o MMC. [p=0.2] Quais números são {b}múltiplos de quatro e de seis ao mesmo tempo? [p=0.2] Quem multiplica responde {c}os de vinte e quatro. [p=0.3] Mas {d}o doze já é múltiplo de quatro e de seis, [p=0.2] e ficou de fora. [p=0.2] {e}A resposta são os múltiplos do MMC, doze. [p=0.2] O produto só serve quando os números não têm divisor comum além do um, como dois e três."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: [p=0.2] {a}o desenho dos múltiplos se repete a cada MMC. [p=0.2] De um a seis, os múltiplos de dois ou de três são {b}dois, três, quatro e seis: quatro números. [p=0.3] Até noventa e seis, cabem {c}dezesseis blocos de seis: [p=0.2] {d}dezesseis vezes quatro, sessenta e quatro. [p=0.2] Sobram {e}noventa e sete a cem, com três números que servem. [p=0.2] {f}Sessenta e quatro mais três, sessenta e sete."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a cada seis números, o desenho recomeça igual. [p=0.3] {b}Não compensa quando o MMC é grande, [p=0.2] como o trinta de dois, três e cinco. [p=0.2] Aí, {c}use a conta de incluir e excluir."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}De um a duzentos, [p=0.2] {b}quantos números são múltiplos de três ou de cinco?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Duzentos dividido por três dá sessenta e seis, e sobra dois. [p=0.2] {b}Duzentos dividido por cinco dá quarenta. [p=0.3] Os dois ao mesmo tempo: {c}o MMC de três e cinco é quinze. [p=0.2] {d}Duzentos dividido por quinze dá treze, e sobra cinco."),
    dict(id="s17", block="resposta", text="{a}Sessenta e seis mais quarenta, menos treze: [p=0.2] {b}noventa e três números."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}some cada conjunto, [p=0.2] {b}tire o que foi contado duas vezes, [p=0.2] e, com três conjuntos, {c}devolva o miolo."),
    dict(id="s19", block="fim", text="Na próxima aula, você conta escolhas {a}em que pode repetir: [p=0.2] por exemplo, {b}de quantos jeitos escolher três doces entre quatro sabores, levando sabores iguais se quiser. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
