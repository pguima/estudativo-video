# Estudativo · MAT-EST-009 — Média ponderada (Matemática · Estatística · Médias).
# Habilidade: calcular a média com pesos, como notas 6 (peso 2) e 8 (peso 3), que dão 7,2.
# Pré-requisitos: MAT-EST-008 (média = soma ÷ quantidade; total = média × quantidade). Próxima: MAT-EST-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula (processo seletivo fictício).
# Dados: 6·2 + 8·3 = 12 + 24 = 36; pesos 5; 36 ÷ 5 = 7,2 (= média de 6, 6, 8, 8, 8).
#   Loja: 30 camisas a R$ 20 e 10 a R$ 40 → 600 + 400 = 1000; 1000 ÷ 40 = 25. Erro: (20 + 40) ÷ 2 = 30.
#   Atalho (dois valores): 6 + (3/5)·2 = 6 + 1,2 = 7,2; 20 + (10/40)·20 = 20 + 5 = 25.
#   Questão: 6·3 + 7·2 + 9·5 = 18 + 14 + 45 = 77; pesos 10; 7,7.

TITULO = "Média ponderada: quando cada nota tem um peso"

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
    dict(id="s01", block="gancho", text="{a}Seis numa prova com peso dois. [p=0.2] {b}Oito na outra, com peso três. [p=0.3] A média não é sete. [p=0.2] {c}É sete vírgula dois. [p=0.3] E o peso explica por quê."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula qualquer média com pesos [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}uma coisa só: a média aritmética, [p=0.2] {b}a soma dividida pela quantidade. [p=0.3] Se faltar, procure no canal."),
    # o que é peso
    dict(id="s04", block="peso", text="O que é peso? [p=0.2] Na média ponderada, {a}cada valor tem um peso: quantas vezes ele conta. [p=0.2] Peso dois quer dizer que {b}o seis entra duas vezes. [p=0.2] Peso três: {c}o oito entra três vezes."),
    dict(id="s05", block="peso", text="Então é como se fossem {a}cinco notas: o seis entra duas vezes, e o oito entra três vezes. [p=0.3] Agora é a média que você já conhece. [p=0.2] {b}Somando as cinco notas, dá trinta e seis. [p=0.2] {c}Trinta e seis dividido por cinco dá sete vírgula dois."),
    # regra
    dict(id="s06", block="regra", text="Sem escrever a lista toda, a regra fica assim: [p=0.2] {a}multiplique cada valor pelo seu peso, [p=0.2] {b}some os resultados [p=0.2] e {c}divida pela soma dos pesos."),
    dict(id="s07", block="regra", text="{a}Seis vezes dois dá doze. [p=0.2] {b}Oito vezes três dá vinte e quatro. [p=0.2] {c}Doze mais vinte e quatro dá trinta e seis. [p=0.2] {d}A soma dos pesos é cinco. [p=0.2] {e}Trinta e seis dividido por cinco dá sete vírgula dois."),
    dict(id="s08", block="regra", text="Repare: {a}sete vírgula dois fica mais perto do oito, [p=0.2] porque o oito pesa mais. [p=0.2] A média ponderada {b}é puxada para o valor de maior peso."),
    dict(id="s09", block="regra", text="E se os pesos fossem iguais? [p=0.2] Com peso um para cada nota, {a}a ponderada vira a média aritmética: [p=0.2] seis mais oito dá catorze, e catorze dividido por dois dá sete. [p=0.3] É por isso que, no gancho, muita gente responde sete: {b}esquece o peso."),
    # peso como quantidade
    dict(id="s10", block="loja", text="O peso nem sempre vem escrito como peso. [p=0.2] Uma loja vendeu {a}trinta camisas a vinte reais [p=0.2] e {b}dez camisas a quarenta reais. [p=0.2] Qual foi o preço médio? [p=0.3] Aqui, {c}o peso de cada preço é quantas camisas saíram por ele."),
    dict(id="s11", block="loja", text="{a}Trinta vezes vinte dá seiscentos. [p=0.2] {b}Dez vezes quarenta dá quatrocentos. [p=0.2] {c}Seiscentos mais quatrocentos dá mil reais. [p=0.2] Os pesos somam {d}quarenta camisas. [p=0.2] {e}Mil dividido por quarenta dá vinte e cinco reais."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}esquecer os pesos e fazer a média dos preços. [p=0.2] {b}Vinte mais quarenta dá sessenta, e sessenta dividido por dois dá trinta reais. [p=0.3] Mas saíram {c}muito mais camisas de vinte. [p=0.2] O preço médio tem que ficar {d}mais perto de vinte, e não no meio do caminho."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para dois valores: {a}ande do menor para o maior, na fração do peso. [p=0.2] De seis para oito, {b}a distância é dois. [p=0.2] O oito tem {c}três dos cinco pesos, [p=0.2] então ande três quintos do caminho. [p=0.2] {d}Três quintos de dois dá um vírgula dois. [p=0.2] {e}Seis mais um vírgula dois dá sete vírgula dois."),
    dict(id="s14", block="atalho", text="Funciona porque, das cinco notas, {a}três subiram de seis para oito. [p=0.2] Elas puxam a média três quintos do caminho. [p=0.3] Na loja, de vinte a quarenta são vinte reais, [p=0.2] e o quarenta tem {b}dez das quarenta camisas: um quarto. [p=0.2] {c}Um quarto de vinte dá cinco. [p=0.2] Vinte mais cinco dá vinte e cinco reais. [p=0.3] {d}Não compensa com três valores ou mais: [p=0.2] aí, multiplique, some e divida."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Num processo seletivo criado para esta questão, {a}a nota final usa pesos: [p=0.2] matemática com peso três, [p=0.2] português com peso dois [p=0.2] e redação com peso cinco. [p=0.3] Uma candidata tirou {b}seis em matemática, [p=0.2] sete em português [p=0.2] e nove na redação. [p=0.3] {c}Qual é a nota final dela?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Seis vezes três dá dezoito. [p=0.2] {b}Sete vezes dois dá catorze. [p=0.2] {c}Nove vezes cinco dá quarenta e cinco. [p=0.2] {d}Somando tudo, dá setenta e sete."),
    dict(id="s18", block="resposta", text="Os pesos somam {a}três mais dois mais cinco, que dá dez. [p=0.2] Dividir por dez é {b}andar a vírgula uma casa para a esquerda. [p=0.2] {c}Setenta e sete dividido por dez dá sete vírgula sete. [p=0.3] O nove, {d}a nota de maior peso, puxou a nota final para cima. [p=0.2] Faz sentido."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}multiplique cada valor pelo peso, [p=0.2] {b}some [p=0.2] e {c}divida pela soma dos pesos. [p=0.2] A média é {d}puxada para o valor que pesa mais."),
    dict(id="s20", block="fim", text="Na próxima aula, mais duas médias. [p=0.2] {a}A geométrica, em que a média de quatro e nove dá seis. [p=0.2] E {b}a harmônica: ida a quarenta e volta a sessenta quilômetros por hora dão média de quarenta e oito. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
