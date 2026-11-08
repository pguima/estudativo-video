# Estudativo · MAT-EST-014 — Quartis e percentis (Matemática · Estatística · Mediana, moda e dispersão).
# Habilidade: dividir dados ordenados em quatro partes, achar Q1, Q2 e Q3 e interpretar o percentil 90 de uma prova.
# Pré-requisitos: MAT-EST-011 (mediana; posição do meio = (n + 1)/2). Usa MAT-POR-002 (porcentagem de um número). Próxima: MAT-EST-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Listas só na tela (vírgula entre números funde a leitura da voz).
# Método: Q2 = mediana; Q1 = mediana da metade de baixo; Q3 = mediana da metade de cima; com n ímpar a mediana fica fora das metades.
# Dados (tela): 11 notas em ordem: 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10.
#   (11 + 1)/2 = 6 → 6º = 6 = Q2. Metade de baixo 2, 3, 4, 4, 5 → 3º = 4 = Q1. Metade de cima 7, 7, 8, 9, 10 → 3º = 8 = Q3.
#   Percentil: P25 = Q1, P50 = Q2, P75 = Q3. P90: cerca de 90% com nota igual ou menor; entre os 10% mais altos.
#   Erro: percentil 90 com 62 acertos em 100 questões (62% de acerto).
#   Atalho: 100 − 90 = 10%; 10% de 2 000 = 200.
#   Questão: 6, 9, 3, 10, 6, 7, 5, 8 → em ordem 3, 5, 6, 6, 7, 8, 9, 10; Q2 = (6 + 7)/2 = 6,5;
#     Q1 = (5 + 6)/2 = 5,5; Q3 = (8 + 9)/2 = 8,5. Nota igual a Q3: cerca de 75% com nota igual ou menor; entre os 25% mais altos.
# Visual:
#   s01: boletim "percentil 90" e "62 acertos de 100" lado a lado.
#   s04-s07: E.reta com as onze notas; corte na mediana; cortes nas metades; rótulos Q1, Q2, Q3; quatro faixas com "25%".
#   s08-s09: régua de 0 a 100% com P25, P50, P75 e P90 marcados.
#   s10: "62%" em vermelho riscado; "acima de 90% dos candidatos" em verde.
#   s11-s12: 2 000 candidatos como bloco de pontos; os 200 de cima acesos.

TITULO = "Quartis e percentis"

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
    dict(id="s01", block="gancho", text="{a}Uma pessoa acertou sessenta e duas questões de cem [p=0.2] e ficou no {b}percentil noventa. [p=0.3] Foi mal ou foi bem? [p=0.3] {c}Foi muito bem. [p=0.2] E até o fim desta aula você entende por quê."),
    dict(id="s02", block="gancho", text="{a}Você vai dividir os dados em quatro partes, [p=0.2] achar os quartis [p=0.2] e levar um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}uma coisa: a mediana. [p=0.2] {b}Ordene os dados e pegue o meio. [p=0.2] {c}Para achar a posição, some um à quantidade e divida por dois. [p=0.3] Se faltar, procure no canal."),
    # quartis
    dict(id="s04", block="quartis", text="A mediana corta os dados {a}em duas metades. [p=0.2] Os {b}quartis cortam em quatro partes, [p=0.2] cada uma com {c}cerca de um quarto dos dados. [p=0.3] São três cortes: {d}primeiro, segundo e terceiro quartil."),
    dict(id="s05", block="quartis", text="Veja {a}onze notas na tela, já em ordem. [p=0.2] {b}Onze mais um dá doze, e doze dividido por dois dá seis: [p=0.2] a mediana está na sexta posição. [p=0.2] O valor que está lá é {c}seis. [p=0.2] Aqui os números coincidiram, mas a mediana é o valor, não a posição. [p=0.3] Ela é {d}o segundo quartil."),
    dict(id="s06", block="quartis", text="Agora, faça a mesma coisa em cada metade. [p=0.2] Com quantidade ímpar, {a}a mediana fica de fora das metades. [p=0.3] Sobram {b}cinco notas embaixo. [p=0.2] A do meio delas é {c}quatro: o primeiro quartil. [p=0.3] Sobram {d}cinco notas em cima. [p=0.2] A do meio é {e}oito: o terceiro quartil."),
    dict(id="s07", block="quartis", text="Então, {a}o primeiro quartil é a mediana da metade de baixo. [p=0.2] {b}O terceiro é a mediana da metade de cima. [p=0.3] Cerca de um quarto das notas fica {c}até o primeiro quartil, [p=0.2] e cerca de três quartos, {d}até o terceiro. [p=0.3] Entre esses cortes fica {e}cerca de metade das notas: a metade do meio. [p=0.3] Atenção: livros e planilhas têm outros jeitos de calcular os quartis, [p=0.2] que podem dar valores um pouco diferentes. [p=0.2] Neste curso, o jeito é sempre este: a mediana de cada metade. [p=0.2] Se o enunciado da prova ensinar outro, siga o enunciado."),
    # percentis
    dict(id="s08", block="percentil", text="E o {a}percentil? [p=0.2] É a mesma ideia, cortando em cem partes. [p=0.3] O percentil noventa é o valor que deixa {b}cerca de noventa por cento dos dados abaixo dele ou iguais a ele."),
    dict(id="s09", block="percentil", text="Por isso, {a}o primeiro quartil é o percentil vinte e cinco. [p=0.2] {b}A mediana é o percentil cinquenta. [p=0.2] {c}O terceiro quartil é o percentil setenta e cinco. [p=0.3] Ficar no percentil noventa de uma prova é ir {d}melhor ou igual a cerca de noventa por cento dos candidatos."),
    # erro
    dict(id="s10", block="erro", text="E aqui está o erro do começo. [p=0.2] Muita gente lê percentil noventa como {a}acertar noventa por cento da prova. [p=0.3] Não é. [p=0.2] O percentil {b}compara você com os outros. [p=0.3] Com sessenta e dois acertos, a pessoa {c}ficou acima de cerca de noventa por cento dos candidatos. [p=0.2] A prova é que foi difícil."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: [p=0.2] para saber quantos ficaram acima, {a}faça cem menos o percentil. [p=0.3] Percentil noventa? {b}Cem menos noventa dá dez. [p=0.2] Você está {c}entre os dez por cento mais altos. [p=0.3] Numa prova com {d}dois mil candidatos, dez por cento de dois mil dá duzentos. [p=0.2] Você está entre os cerca de duzentos primeiros."),
    dict(id="s12", block="atalho", text="Funciona porque {a}quem não está abaixo, está acima. [p=0.3] Mas o resultado é sempre {b}aproximado: [p=0.2] em lista pequena ou com muitas notas iguais, {c}conte na lista em vez de usar a porcentagem."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}As notas de oito alunos estão na tela. [p=0.3] {b}Item um: ache o primeiro, o segundo e o terceiro quartil. [p=0.3] {c}Item dois: numa prova grande, Bia tirou nota igual ao terceiro quartil. [p=0.2] O que isso diz sobre ela?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}Primeiro, em ordem. [p=0.2] Com oito notas, a mediana é {b}a média da quarta e da quinta nota. [p=0.2] Seis mais sete dá treze, e treze dividido por dois dá seis vírgula cinco. [p=0.3] Com quantidade par, {c}as metades ficam com quatro notas cada."),
    dict(id="s16", block="resposta", text="Na metade de baixo, os valores do meio são cinco e seis: [p=0.2] a média deles dá {a}cinco vírgula cinco, o primeiro quartil. [p=0.2] Na metade de cima, oito e nove: [p=0.2] a média dá {b}oito vírgula cinco, o terceiro quartil. [p=0.3] E a Bia: [p=0.2] {c}cerca de setenta e cinco por cento tiraram nota igual ou menor que a dela. [p=0.2] {d}Ela está entre os vinte e cinco por cento mais altos."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.2] {a}os quartis são medianas das metades, [p=0.2] e {b}o percentil diz quantos ficaram abaixo de você, não quanto você acertou."),
    dict(id="s18", block="fim", text="Na próxima aula, esses números viram um desenho: {a}o boxplot. [p=0.2] Nele você lê {b}mínimo, quartis, máximo e amplitude [p=0.2] e compara duas turmas de uma olhada. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
