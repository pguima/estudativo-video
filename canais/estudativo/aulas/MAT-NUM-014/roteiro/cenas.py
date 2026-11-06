# Estudativo · MAT-NUM-014 — Montar a expressão de um problema (Matemática · Números e Contas).
# Habilidade: escrever 200 − (3 × 25 + 2 × 40) para o troco de uma compra.
# Pré-requisitos: MAT-NUM-011 (qual conta o problema pede), MAT-NUM-013 (ordem das operações). Próxima: MAT-NUM-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Preços inventados para a conta.

TITULO = "Montar a expressão de um problema"

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
    dict(id="s01", block="gancho", text="Você paga com {a}duzentos reais, [p=0.2] faz a conta do troco e dá {b}duzentos e cinco. [p=0.3] {c}Troco maior que o dinheiro entregue! [p=0.3] Faltou {d}um par de parênteses."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você transforma um problema em uma expressão só, [p=0.2] com um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}saber qual conta o problema pede [p=0.2] e {c}a ordem das operações: [p=0.2] parênteses, depois vezes e dividido, por último mais e menos. [p=0.3] Se faltar alguma, procure no canal."),
    # montar
    dict(id="s04", block="problema", text="Expressão é uma conta com mais de uma operação. [p=0.2] Veja o problema. [p=0.2] Você compra {a}três camisetas de vinte e cinco reais cada [p=0.2] e {b}duas bermudas de quarenta reais cada. [p=0.3] Paga com {c}duzentos reais. [p=0.3] {d}Como escrever o troco em uma expressão só?"),
    dict(id="s05", block="problema", text="Comece pela frase, sem número nenhum: [p=0.2] {a}troco é o que paguei menos o que gastei. [p=0.3] {b}O que paguei é duzentos. [p=0.2] Falta descobrir {c}o que gastei."),
    dict(id="s06", block="problema", text="As palavras do problema dão pistas, e a história decide. [p=0.2] {a}Aqui, a palavra cada, com preço repetido, pede vezes. [p=0.2] O total junta os gastos, então pede mais. [p=0.2] O troco tira o gasto do que foi pago, então pede menos. [p=0.3] {b}Camisetas: três vezes vinte e cinco. [p=0.2] {c}Bermudas: duas vezes quarenta. [p=0.3] O gasto é a soma: {d}três vezes vinte e cinco mais duas vezes quarenta."),
    dict(id="s07", block="problema", text="Esse gasto é {a}uma coisa só, [p=0.2] e o menos precisa tirar ele inteiro. [p=0.3] Por isso ele vai {b}entre parênteses. [p=0.3] A expressão fica {c}duzentos menos, abre parênteses, três vezes vinte e cinco mais duas vezes quarenta, fecha parênteses. [p=0.3] Repare: nada foi calculado ainda. [p=0.2] A expressão só conta a história da compra."),
    dict(id="s08", block="problema", text="Resolvendo: [p=0.2] {a}três vezes vinte e cinco dá setenta e cinco. [p=0.2] {b}Duas vezes quarenta dá oitenta. [p=0.2] {c}Somando, cento e cinquenta e cinco. [p=0.3] {d}Duzentos menos cento e cinquenta e cinco [p=0.2] dá {e}quarenta e cinco reais de troco. [p=0.3] Confira: {f}quarenta e cinco de troco mais cento e cinquenta e cinco de gasto dá duzentos."),
    # juntar antes de dividir
    dict(id="s09", block="dividir", text="O parêntese também aparece quando é preciso juntar antes de dividir. [p=0.2] {a}Três amigos dividem igualmente um presente de noventa reais {b}e a entrega de trinta reais. [p=0.3] {c}Noventa mais trinta entre parênteses, dividido por três, [p=0.2] {d}dá quarenta para cada um. [p=0.3] Sem o parêntese, só a entrega seria dividida, [p=0.2] e a conta daria {e}cem."),
    # erro
    dict(id="s10", block="erro", text="E aquele troco de duzentos e cinco? [p=0.2] A pessoa {a}esqueceu os parênteses. [p=0.3] Sem eles, o menos {b}só tira as camisetas. [p=0.2] As bermudas {c}entram somando, [p=0.2] como se a loja te pagasse oitenta reais. [p=0.3] {d}Duzentos menos setenta e cinco mais oitenta dá duzentos e cinco. [p=0.3] Dá para tirar um item de cada vez: {e}duzentos menos setenta e cinco menos oitenta dá os mesmos quarenta e cinco. [p=0.2] O que não pode é tirar um e somar o outro."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: {a}a frase primeiro. [p=0.2] Escreva a conta em palavras e {b}troque cada palavra por números. [p=0.3] Se a frase diz {c}menos o total, [p=0.2] o total {d}vai entre parênteses."),
    dict(id="s12", block="atalho", text="Funciona porque a frase já mostra {a}o que precisa acontecer primeiro: [p=0.2] você só tira o total depois de somar. [p=0.3] {b}Não compensa com um item só: [p=0.2] em {c}duzentos menos três vezes vinte e cinco, [p=0.2] o vezes já vem antes, e o parêntese não faz falta."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Você compra {a}quatro cadernos de oito reais cada [p=0.2] e {b}cinco canetas de três reais cada. [p=0.2] Paga com {c}uma nota de cem reais. [p=0.3] {d}Escreva a expressão do troco e calcule o valor dele."),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] A frase: {a}troco é o que paguei menos o total. [p=0.2] A expressão: {b}cem menos, abre parênteses, quatro vezes oito mais cinco vezes três, fecha parênteses."),
    dict(id="s16", block="resposta", text="{a}Quatro vezes oito dá trinta e dois. [p=0.2] {b}Cinco vezes três dá quinze. [p=0.2] Total: {c}quarenta e sete reais. [p=0.3] {d}Cem menos quarenta e sete [p=0.2] dá {e}cinquenta e três reais de troco. [p=0.3] Confira: {f}cinquenta e três mais quarenta e sete dá cem. [p=0.2] Sem os parênteses, daria {g}um troco inflado de oitenta e três reais."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}primeiro a frase, [p=0.2] {b}depois os números, [p=0.2] e {c}total que se tira vai entre parênteses."),
    dict(id="s18", block="fim", text="E quando você {a}gasta mais do que tem? [p=0.3] Na próxima aula, você conhece os {b}números negativos [p=0.2] e {c}a reta numérica. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
