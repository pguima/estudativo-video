# Estudativo · MAT-EQU-021 — Praticando: sistemas de equações (Matemática · Equações do 1º Grau · prática).
# Habilidade: montar e resolver sistemas 2x2 em problemas de preços e quantidades.
# Pré-requisitos: MAT-EQU-018, MAT-EQU-019, MAT-EQU-020. Próxima: nenhuma (última aula da trilha).
# Questões inéditas, criadas para esta aula, com preços inventados.

TITULO = "Praticando: sistemas de equações"

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
    dict(id="s01", block="gancho", text="{a}Quatro problemas de preço e quantidade, [p=0.2] criados para esta aula, com preços inventados. [p=0.3] Em cada um, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você tem {a}três ferramentas: [p=0.2] {b}a substituição, [p=0.2] {c}a adição [p=0.2] e {d}o atalho de supor que tudo é de um tipo só. [p=0.3] E uma regra de ouro: {e}confira nas duas equações. [p=0.3] Se alguma travar, procure a aula no canal."),
    # problema 1: diferença entre compras
    dict(id="s03", block="questao1", text="{a}Problema um. [p=0.2] Numa padaria, {b}um suco e um pão de queijo custam nove reais. [p=0.3] {c}Dois sucos e um pão de queijo custam catorze reais. [p=0.3] {d}Quanto custa um suco?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}A letra xis é o preço do suco, {b}a letra ípsilon é o preço do pão de queijo. [p=0.3] {c}Suco mais pão igual a nove. [p=0.2] {d}Dois sucos mais pão igual a catorze. [p=0.3] O pão aparece uma vez em cada equação: [p=0.2] {e}subtraia a primeira da segunda. [p=0.2] Sobra {f}um suco igual a cinco. [p=0.2] O suco custa {g}cinco reais."),
    dict(id="s06", block="resposta1", text="Repare no atalho: [p=0.2] {a}a segunda compra é a primeira com um suco a mais. [p=0.2] Então {b}a diferença de preço é o suco. [p=0.3] Só dá para ver de olho quando as compras diferem {c}num item só. [p=0.3] Conferindo: o pão custa {d}nove menos cinco, que dá quatro reais. [p=0.2] {e}Dois sucos dão dez, mais quatro dá catorze. [p=0.2] Bateu."),
    # problema 2: substituição
    dict(id="s07", block="questao2", text="{a}Problema dois. [p=0.2] Numa loja, {b}uma calça custa três vezes o preço de uma camiseta. [p=0.3] {c}Uma calça e duas camisetas custam cento e cinquenta reais. [p=0.3] {d}Quanto custa a calça?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] {a}A letra xis é o preço da calça, {b}a letra ípsilon é o preço da camiseta. [p=0.3] A primeira informação já deixa a calça sozinha: {c}xis igual a três ípsilon. [p=0.2] É a deixa da substituição. [p=0.3] Na outra, troque a calça: [p=0.2] {d}três ípsilon mais dois ípsilon igual a cento e cinquenta."),
    dict(id="s10", block="resposta2", text="{a}Cinco ípsilon igual a cento e cinquenta, [p=0.2] então {b}a camiseta custa trinta reais. [p=0.3] Cuidado: a pergunta é {c}a calça. [p=0.2] Três vezes trinta: {d}a calça custa noventa reais. [p=0.3] Conferindo: {e}noventa mais sessenta dá cento e cinquenta, [p=0.2] e {f}noventa é o triplo de trinta. [p=0.2] Bateu nas duas."),
    # problema 3: adição e a soma pedida
    dict(id="s11", block="questao3", text="{a}Problema três. [p=0.2] {b}Três cadernos e duas canetas custam trinta e um reais. [p=0.3] {c}Dois cadernos e três canetas custam vinte e quatro reais. [p=0.3] {d}Quanto custam, juntos, um caderno e uma caneta?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] A pergunta quer {a}caderno mais caneta. [p=0.2] É o atalho da adição: {b}some as equações do jeito que estão. [p=0.3] {c}Cinco cadernos e cinco canetas custam cinquenta e cinco reais. [p=0.2] Dividindo por cinco: [p=0.2] {d}um caderno e uma caneta custam onze reais."),
    dict(id="s14", block="resposta3", text="Para conferir, ache cada preço. [p=0.2] {a}Multiplique a primeira por dois e a segunda por três: [p=0.2] o caderno fica com seis na frente nas duas. [p=0.3] Subtraindo, sobra {b}cinco canetas igual a dez reais: [p=0.2] {c}a caneta custa dois reais, [p=0.2] e {d}o caderno, onze menos dois, que dá nove."),
    dict(id="s15", block="resposta3", text="{a}Três cadernos dão vinte e sete, mais quatro dá trinta e um. [p=0.2] {b}Dois cadernos dão dezoito, mais seis dá vinte e quatro. [p=0.2] Bateu nas duas. [p=0.3] Com o atalho, {c}você respondia sem nada disso."),
    # problema 4: montar e supor
    dict(id="s16", block="questao4", text="{a}Último problema, e ele junta tudo. [p=0.2] Uma lanchonete vendeu {b}cinquenta lanches, uns de oito reais e outros de doze reais. [p=0.3] Ao todo, entraram {c}quinhentos e vinte reais. [p=0.3] {d}Quantos lanches de doze reais foram vendidos?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] O sistema tem {a}uma equação para as quantidades: [p=0.2] os lanches somam cinquenta. [p=0.2] E {b}uma para o dinheiro: [p=0.2] oito reais vezes os lanches baratos, mais doze reais vezes os caros, dá quinhentos e vinte. [p=0.3] Tem o total de coisas e só dois tipos: {c}vale o atalho."),
    dict(id="s19", block="resposta4", text="Suponha {a}todos de oito reais: [p=0.2] cinquenta lanches dariam {b}quatrocentos reais. [p=0.2] {c}Faltam cento e vinte. [p=0.3] Trocar um lanche de oito por um de doze {d}acrescenta quatro reais. [p=0.2] {e}Cento e vinte dividido por quatro dá trinta. [p=0.3] Foram {f}trinta lanches de doze reais."),
    dict(id="s20", block="resposta4", text="Os de oito reais são cinquenta menos trinta: [p=0.2] {a}vinte lanches. [p=0.3] Conferindo: [p=0.2] {b}trinta lanches de doze dão trezentos e sessenta reais. [p=0.2] {c}Vinte lanches de oito dão cento e sessenta. [p=0.2] {d}Somando, quinhentos e vinte. [p=0.2] Bateu nas duas."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}uma equação para as quantidades e outra para os valores, [p=0.2] {b}o caminho pelo formato do sistema [p=0.2] e {c}a conferência nas duas equações."),
    dict(id="s22", block="fim", text="Com isso, você fecha a trilha de {a}equações do primeiro grau. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
