# Estudativo · MAT-FRA-010 — Fração do restante (Matemática · Frações e Decimais).
# Habilidade: resolver o caso de quem gastou 1/3 e depois 1/4 do que sobrou.
# Pré-requisitos: MAT-FRA-007 (quanto falta para o inteiro), MAT-FRA-009 (multiplicar). Próxima: MAT-FRA-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Denominadores diferentes e MMC não estão na ficha: tudo sai por multiplicação e por quanto falta para o inteiro.

TITULO = "Fração do restante"

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
    dict(id="s01", block="gancho", text="{a}Salário de mil e duzentos reais. [p=0.2] A pessoa gasta {b}um terço. [p=0.2] Depois, gasta {c}um quarto do que sobrou. [p=0.3] {d}Quanto restou?"),
    dict(id="s02", block="gancho", text="Se a sua resposta foi {a}quinhentos reais, [p=0.2] você caiu na armadilha mais comum das frações. [p=0.3] Ela mora em três palavrinhas: {b}do que sobrou."),
    dict(id="s03", block="gancho", text="{a}Até o fim desta aula, você vai resolver esse tipo de problema com ou sem o valor em reais, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s04", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas. [p=0.2] Primeiro, {b}quanto falta para um inteiro: [p=0.2] o inteiro são três terços; [p=0.2] tira um terço, ficam dois terços. [p=0.3] Depois, {c}multiplicar frações, lembrando que a palavra de vira vezes. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # barra
    dict(id="s05", block="barra", text="Antes de cada conta, pergunte: {a}fração de quê? [p=0.3] Desenhe o salário como {b}uma barra de doze quadradinhos. [p=0.2] Doze porque é três vezes quatro: dá para tirar terços e, depois, quartos sem quebrar quadradinho. [p=0.3] Mil e duzentos dividido por doze: cada um vale {c}cem reais."),
    dict(id="s06", block="barra", text="Primeiro gasto: um terço {a}do salário. [p=0.2] Doze dividido por três, {b}quatro quadradinhos. [p=0.2] {c}Quatrocentos reais. [p=0.3] Sobraram {d}oito quadradinhos."),
    dict(id="s07", block="barra", text="Segundo gasto: um quarto {a}do que sobrou. [p=0.2] A conta agora usa os oito quadradinhos que sobraram, não os doze. [p=0.3] Oito dividido por quatro, {b}dois quadradinhos. [p=0.2] {c}Duzentos reais."),
    dict(id="s08", block="barra", text="Restaram {a}seis quadradinhos: [p=0.2] {b}seiscentos reais. [p=0.3] Seis de doze é {c}metade do salário. [p=0.3] Ao todo, ela gastou {d}a outra metade: [p=0.2] quatrocentos mais duzentos, {e}seiscentos reais."),
    # só com frações
    dict(id="s09", block="fracoes", text="E se o enunciado não disser o salário? [p=0.2] Dá para fazer só com frações. [p=0.3] Depois do primeiro gasto, sobraram {a}dois terços do salário. [p=0.3] O segundo gasto é {b}um quarto de dois terços."),
    dict(id="s10", block="fracoes", text="A palavra de vira vezes. [p=0.2] Corte em cruz: {a}dois e quatro, divida por dois, ficam um e dois. [p=0.3] {b}Em cima, um vezes um. [p=0.2] {c}Embaixo, dois vezes três. [p=0.3] Um sexto do salário, {d}não um quarto. [p=0.3] Faz sentido: o que sobrou é menor que o salário, então um quarto do que sobrou é menor que um quarto do salário."),
    dict(id="s11", block="fracoes", text="Confira: {a}um sexto de mil e duzentos, duzentos reais. [p=0.2] {b}Bateu com a barra."),
    # erro
    dict(id="s12", block="erro", text="E os quinhentos do começo? [p=0.2] Quem cai na armadilha calcula um quarto {a}do salário inteiro: [p=0.2] {b}trezentos reais. [p=0.2] Com os quatrocentos, são {c}setecentos gastos, e sobram quinhentos."),
    dict(id="s13", block="erro", text="Mas, no segundo gasto, a pessoa só tinha {a}oitocentos reais. [p=0.3] Fique de olho nestas expressões: {b}do que sobrou, {c}do restante, {d}do resto. [p=0.2] Todas apontam para o que ficou, não para o começo. [p=0.3] Sublinhe essas palavras no enunciado, e pergunte de novo: {e}fração de quê?"),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho prometido: {a}multiplique só as sobras. [p=0.3] Gastou um terço? {b}Sobram dois terços. [p=0.2] Gastou um quarto do resto? {c}Sobram três quartos desse resto. [p=0.3] Então fica {d}três quartos de dois terços."),
    dict(id="s15", block="atalho", text="Corte em cruz: {a}três e três, ficam um e um. [p=0.2] {b}Dois e quatro, ficam um e dois. [p=0.3] {c}Um meio. [p=0.2] Metade do salário, em uma linha só."),
    dict(id="s16", block="atalho", text="Mais um, sem nenhum valor. [p=0.2] Uma caixa de água estava cheia. [p=0.2] De manhã, saiu {a}um quinto da água. [p=0.2] À tarde, {b}metade do restante. [p=0.3] Sobram {c}quatro quintos, [p=0.2] e depois {d}um meio deles. [p=0.3] {e}Um meio de quatro quintos: [p=0.2] {f}dois quintos da caixa ainda têm água."),
    dict(id="s17", block="atalho", text="Funciona porque {a}cada sobra é uma fração da sobra anterior, [p=0.2] e fração de fração é vezes. [p=0.3] Não compensa quando a pergunta é {b}quanto saiu em uma etapa: [p=0.2] aí, calcule aquela etapa, como fizemos com {c}o segundo gasto, um sexto do salário."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Uma loja tem {a}noventa camisetas. [p=0.2] De manhã, vendeu {b}dois quintos. [p=0.2] À tarde, vendeu {c}dois terços do restante. [p=0.3] {d}Quantas camisetas sobraram?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá, pelas sobras. [p=0.2] Vendeu dois quintos: {a}sobram três quintos. [p=0.2] Vendeu dois terços do restante: {b}sobra um terço desse restante. [p=0.3] {c}Um terço de três quintos: corte o três com o três, {d}fica um quinto."),
    dict(id="s21", block="resposta", text="Um quinto de noventa: {a}dezoito camisetas. [p=0.3] Confira pelas vendas: {b}de manhã, trinta e seis. [p=0.2] {c}Ficam cinquenta e quatro. [p=0.2] {d}À tarde, trinta e seis. [p=0.2] {e}Ficam dezoito. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: antes de cada conta, pergunte {a}fração de quê. [p=0.2] E, quando for do restante, {b}multiplique as sobras."),
    dict(id="s23", block="fim", text="Na próxima aula, você vai {a}dividir frações [p=0.2] e descobrir {b}quantos copos de um quarto de litro cabem em três litros. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
