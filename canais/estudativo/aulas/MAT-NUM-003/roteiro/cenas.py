# Estudativo · MAT-NUM-003 — Somar de cabeça e com a conta armada (Matemática · Números e Contas).
# Habilidade: calcular 8 + 7 de cabeça completando 10 e armar 478 + 356 com o vai-um.
# Pré-requisitos: MAT-NUM-001. Próxima: MAT-NUM-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Contas: 8 + 7 = 15 · 6 + 7 = 13 · 478 + 356 = 834 (sem vai um dá 724; faltam 110) · 700 + 120 = 820 · 199 + 47 = 246 · 436 + 257 = 693.
# Questão: 267 + 175 = 442 (sem vai um daria 332).

TITULO = "Somar de cabeça e com a conta armada"

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
    dict(id="s01", block="gancho", text="{a}Oito mais sete. [p=0.3] Se você usou os dedos, {b}sem problema: [p=0.2] existe um caminho mais rápido, e ele serve para a vida toda."),
    dict(id="s02", block="gancho", text="{a}Quatrocentos e setenta e oito mais trezentos e cinquenta e seis. [p=0.3] Se deu {b}setecentos e vinte e quatro, [p=0.2] {c}sumiram cento e dez reais no caminho."),
    dict(id="s03", block="gancho", text="{a}Até o fim desta aula, você soma de cabeça e com a conta armada, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s04", block="lembrete", text="Para acompanhar, você só precisa de {a}uma troca: [p=0.2] {b}dez moedas de um real viram uma nota de dez, [p=0.2] e {c}dez notas de dez viram uma nota de cem. [p=0.3] Se faltar, procure a aula no canal."),
    # completar dez
    dict(id="s05", block="dez", text="Somar é {a}juntar. [p=0.2] Cada número que entra na soma se chama {b}parcela, [p=0.2] como as parcelas de uma compra, [p=0.2] que juntas dão {c}o total."),
    dict(id="s06", block="dez", text="O número mais fácil de somar é {a}o dez: [p=0.2] dez mais cinco, qualquer um responde na hora. [p=0.3] Então a ideia é {b}chegar no dez primeiro."),
    dict(id="s07", block="dez", text="{a}Oito mais sete. [p=0.2] Para o oito virar dez, {b}faltam dois. [p=0.3] {c}Tire esses dois de dentro do sete: [p=0.2] sete é o mesmo que {d}dois mais cinco. [p=0.3] {e}Oito mais dois dá dez. [p=0.2] {f}Dez mais cinco dá quinze."),
    dict(id="s08", block="dez", text="Pense em duas pilhas de moedas: [p=0.2] {a}você só passou duas moedas de uma pilha para a outra. [p=0.3] {b}O total não mudou. [p=0.3] Veja mais uma: {c}seis mais sete. [p=0.2] {d}Faltam quatro para o dez. [p=0.2] Sete é {e}quatro mais três. [p=0.2] {f}Dez mais três dá treze."),
    # conta armada
    dict(id="s09", block="armar", text="E com números grandes? [p=0.2] Use a {a}conta armada: [p=0.2] um número embaixo do outro, [p=0.2] {b}unidade embaixo de unidade, [p=0.2] {c}dezena embaixo de dezena [p=0.2] e {d}centena embaixo de centena. [p=0.3] É juntar moeda com moeda e nota de dez com nota de dez."),
    dict(id="s10", block="armar", text="Some {a}da direita para a esquerda. [p=0.2] Nas unidades, {b}oito mais seis. [p=0.2] Completando o dez, dá {c}catorze."),
    dict(id="s11", block="armar", text="Catorze moedas não cabem numa casa, [p=0.2] porque {a}nenhuma casa guarda mais que nove. [p=0.3] Dez moedas viram {b}uma nota de dez. [p=0.2] Sobram {c}quatro moedas: [p=0.2] o quatro fica embaixo. [p=0.3] A nota sobe para a casa das dezenas: [p=0.2] é o famoso {d}vai um."),
    dict(id="s12", block="armar", text="Nas dezenas: {a}sete mais cinco dá doze, [p=0.2] {b}mais o um que veio dá treze. [p=0.3] São treze notas de dez. [p=0.2] Dez delas viram {c}uma nota de cem. [p=0.2] {d}Fica o três [p=0.2] e {e}vai um para as centenas."),
    dict(id="s13", block="armar", text="Nas centenas: {a}quatro mais três dá sete, [p=0.2] {b}mais o um que veio dá oito. [p=0.3] Resultado: {c}oitocentos e trinta e quatro."),
    dict(id="s14", block="armar", text="Somando dois números, a regra é esta: [p=0.2] {a}a casa deu dez ou mais? [p=0.2] Fica o algarismo da direita e {b}vai um. [p=0.3] {c}Deu nove ou menos? [p=0.2] Escreve direto, e não vai nada. [p=0.3] {d}Na última casa da esquerda, não há para onde ir: [p=0.2] deu dez ou mais, {e}escreva o número inteiro."),
    # erro
    dict(id="s15", block="erro", text="E aquele setecentos e vinte e quatro? [p=0.2] É o {a}vai um esquecido duas vezes. [p=0.2] A pessoa escreve o quatro e {b}perde a nota de dez que subiu. [p=0.2] Depois, perde também a nota de cem. [p=0.3] Dá para desconfiar sem refazer: [p=0.2] {c}quatrocentos mais trezentos já dá setecentos, [p=0.2] e {d}setenta mais cinquenta já dá cento e vinte. [p=0.2] Juntos, passam de oitocentos. [p=0.3] {e}O total não pode ser tão pequeno."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}complete o número redondo. [p=0.2] É o completar dez, em tamanho maior. [p=0.3] Veja {b}cento e noventa e nove mais quarenta e sete. [p=0.2] Cento e noventa e nove pede {c}só um para virar duzentos. [p=0.2] Quarenta e sete é {d}um mais quarenta e seis. [p=0.3] Fica {e}duzentos mais quarenta e seis: [p=0.2] {f}duzentos e quarenta e seis."),
    dict(id="s17", block="atalho", text="Funciona porque {a}você só passou um real de um lado para o outro. [p=0.3] {b}Não compensa quando nenhuma parcela está perto de um número redondo, [p=0.2] como {c}quatrocentos e trinta e seis mais duzentos e cinquenta e sete. [p=0.2] Aí, {d}arme a conta."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Você gastou {a}duzentos e sessenta e sete reais no mercado [p=0.2] e {b}cento e setenta e cinco reais na farmácia. [p=0.3] {c}Quanto gastou ao todo?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Nas unidades, {a}sete mais cinco dá doze. [p=0.2] {b}Fica o dois e {c}vai um. [p=0.3] Nas dezenas, {d}seis mais sete dá treze, [p=0.2] {e}mais o um que veio dá catorze. [p=0.2] {f}Fica o quatro e {g}vai um."),
    dict(id="s21", block="resposta", text="Nas centenas, {a}dois mais um dá três, [p=0.2] {b}mais o um que veio dá quatro. [p=0.3] Total: {c}quatrocentos e quarenta e dois reais."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}de cabeça, complete o dez. [p=0.2] {b}Na conta armada, junte casa com casa, [p=0.2] e {c}a cada dez, vai um."),
    dict(id="s23", block="fim", text="Na próxima aula, o caminho contrário: [p=0.2] {a}subtrair, [p=0.2] {b}conferir com uma soma [p=0.2] e {c}pedir emprestado, até quando o vizinho é zero. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
