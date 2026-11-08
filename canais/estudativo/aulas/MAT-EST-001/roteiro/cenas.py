# Estudativo · MAT-EST-001 — População, amostra e tipos de variáveis (Matemática · Estatística · Dados, tabelas e gráficos).
# Habilidade: dizer se uma pesquisa é censo ou amostra, classificar variáveis em qualitativas e quantitativas e calcular quantos alunos de cada turno entram numa amostra proporcional.
# Pré-requisitos: MAT-POR-003 (quantos por cento: parte dividida pelo total). Usa MAT-POR-002 (porcentagem de um valor). Próxima: MAT-EST-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Amostra ruim só de passagem (MAT-EST-020 trata disso). Média ainda não foi ensinada (MAT-EST-008).
# Fato real estável: o censo do IBGE visita todos os domicílios do país.
# Contas: 500 + 300 + 200 = 1 000; 500/1 000 = 50%, 30%, 20%; de 80: 40, 24, 16 (soma 80). 80/1 000 = 0,08 = 8%: 40, 24, 16.
#   Não compensa: 90/1 200 = 7,5%; 600, 400, 200 = metade, terço, sexto; 45, 30, 15 (soma 90).
#   Questão: 240 + 100 + 60 = 400; 40/400 = 10%: 24, 10, 6 (soma 40).
# Visual:
#   s01: panela e colher.
#   s04-s07: um grupo grande de pontos (população); todos destacados (censo); só alguns (amostra); lâmpadas; colher de um canto só.
#   s08-s09: duas colunas, qualitativa e quantitativa, com os exemplos caindo em cada uma; camisa 10 e camisa 5.
#   s10-s14: escola com três blocos de alunos (manhã 500, tarde 300, noite 200) e a amostra de 80 dividida em 40, 24, 16.

TITULO = "População, amostra e tipos de variáveis"

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
    dict(id="s01", block="gancho", text="{a}Para saber se a sopa está salgada, [p=0.2] você não toma a panela inteira. [p=0.3] {b}Uma colher basta, [p=0.2] desde que você {c}mexa a panela antes. [p=0.3] Essa é a ideia central da estatística."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você sabe quando uma pesquisa ouve todos e quando ouve só uma parte, [p=0.2] separa os tipos de dado [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}uma coisa só: porcentagem. [p=0.2] {b}Saber quantos por cento uma parte é do total, [p=0.2] dividindo a parte pelo total, [p=0.2] e {c}calcular a porcentagem de um número. [p=0.3] Se faltar, procure no canal."),
    # população e censo
    dict(id="s04", block="populacao", text="Toda pesquisa começa com uma pergunta: [p=0.2] {a}quem me interessa? [p=0.2] Esse grupo inteiro é a {b}população. [p=0.3] Se a pesquisa é sobre os alunos de uma escola, [p=0.2] {c}a população são todos os alunos dela. [p=0.2] E não precisa ser gente: [p=0.2] {d}as lâmpadas de uma fábrica também formam uma população."),
    dict(id="s05", block="populacao", text="Quando a pesquisa ouve {a}a população inteira, ela é um {b}censo. [p=0.2] O censo do IBGE, por exemplo, {c}visita todos os domicílios do país. [p=0.3] É completo, [p=0.2] mas {d}caro e demorado."),
    # amostra
    dict(id="s06", block="amostra", text="Por isso, quase toda pesquisa ouve {a}só uma parte da população: a {b}amostra. [p=0.3] Às vezes, nem dá para testar tudo. [p=0.2] Para saber quanto dura uma lâmpada, {c}é preciso deixar acesa até queimar. [p=0.2] Testar todas {d}acabaria com o estoque."),
    dict(id="s07", block="amostra", text="Mas a amostra precisa {a}parecer com a população, [p=0.2] como a colher da sopa mexida. [p=0.3] Perguntar sobre futebol {b}só na porta do estádio [p=0.2] é tomar a colher {c}de um canto só da panela."),
    # variáveis
    dict(id="s08", block="variaveis", text="O que a pesquisa pergunta é a {a}variável. [p=0.2] E ela tem {b}dois tipos. [p=0.3] {c}Qualitativa: a resposta é uma qualidade, uma categoria. [p=0.2] Cor preferida, time, {d}turno de estudo. [p=0.3] {e}Quantitativa: a resposta é uma quantidade, um número que se conta ou se mede. [p=0.2] {f}Idade, altura, número de filhos."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é achar que {a}toda resposta com número é quantitativa. [p=0.2] Veja {b}o número da camisa de um jogador. [p=0.2] É número, [p=0.2] mas a camisa dez {c}não vale o dobro da camisa cinco. [p=0.2] Ele só dá nome. [p=0.3] {d}É qualitativa, como o CEP e o número do telefone. [p=0.3] O teste: {e}faz sentido somar ou comparar quantidades? [p=0.2] Com idade, sim. [p=0.2] Com camisa, não."),
    # amostra proporcional
    dict(id="s10", block="proporcional", text="Agora, a amostra {a}proporcional. [p=0.2] Uma escola tem {b}mil alunos: [p=0.2] quinhentos de manhã, trezentos à tarde e duzentos à noite. [p=0.3] A pesquisa vai ouvir {c}oitenta alunos. [p=0.2] Quantos de cada turno?"),
    dict(id="s11", block="proporcional", text="Proporcional quer dizer que {a}cada turno pesa na amostra o mesmo que pesa na escola. [p=0.3] {b}Manhã: quinhentos dividido por mil dá zero vírgula cinco, [p=0.2] que são cinquenta por cento. [p=0.2] {c}Tarde: trezentos dividido por mil dá trinta por cento. [p=0.2] {d}Noite: duzentos dividido por mil dá vinte por cento."),
    dict(id="s12", block="proporcional", text="Aplique as mesmas porcentagens à amostra. [p=0.2] {a}Cinquenta por cento de oitenta dá quarenta. [p=0.2] {b}Trinta por cento de oitenta dá vinte e quatro. [p=0.2] {c}Vinte por cento de oitenta dá dezesseis. [p=0.3] Confira: {d}quarenta mais vinte e quatro mais dezesseis dá oitenta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}veja quantos por cento a amostra é da população. [p=0.2] {b}Oitenta dividido por mil dá zero vírgula zero oito, [p=0.2] que são oito por cento. [p=0.3] Tire {c}oito por cento de cada turno. [p=0.2] {d}Oito por cento de quinhentos dá quarenta, [p=0.2] de trezentos dá vinte e quatro [p=0.2] e de duzentos dá dezesseis."),
    dict(id="s14", block="atalho", text="Funciona porque proporcional é {a}a mesma fatia de cada turno. [p=0.3] {b}Não compensa quando essa porcentagem sai quebrada. [p=0.2] Amostra de {c}noventa numa escola de mil e duzentos dá sete vírgula cinco por cento. [p=0.2] Se a manhã tiver {d}metade da escola, [p=0.2] {e}noventa dividido por dois dá quarenta e cinco alunos. [p=0.2] Se a tarde tiver um terço, [p=0.2] {f}noventa dividido por três dá trinta alunos."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma empresa tem {a}quatrocentos funcionários: [p=0.2] duzentos e quarenta na produção, cem no escritório e sessenta nas vendas. [p=0.3] Uma pesquisa vai ouvir {b}quarenta deles, em amostra proporcional ao setor. [p=0.3] {c}É censo ou amostra? [p=0.2] {d}Quantos de cada setor? [p=0.2] E {e}que tipo de variável é o setor, o salário e o número do crachá?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] A pesquisa ouve uma parte: {a}é amostra. [p=0.2] Pelo atalho, {b}quarenta dividido por quatrocentos dá zero vírgula um, [p=0.2] que são dez por cento. [p=0.3] {c}Dez por cento de duzentos e quarenta dá vinte e quatro, na produção. [p=0.2] {d}Dez por cento de cem dá dez, no escritório. [p=0.2] {e}Dez por cento de sessenta dá seis, nas vendas. [p=0.2] Vinte e quatro mais dez mais seis dá quarenta. [p=0.2] Bateu."),
    dict(id="s18", block="resposta", text="{a}Setor é qualitativa: a resposta é uma categoria. [p=0.2] {b}Salário é quantitativa: dá para somar e comparar. [p=0.2] E {c}o número do crachá é qualitativa: [p=0.2] ele só identifica a pessoa."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}censo ouve todos, amostra ouve uma parte. [p=0.2] {b}Qualitativa é categoria, quantitativa é quantidade. [p=0.2] E na amostra proporcional, {c}cada grupo entra com a mesma porcentagem."),
    dict(id="s20", block="fim", text="Na próxima aula, você organiza as respostas de uma pesquisa numa {a}tabela de frequência: [p=0.2] {b}quantas vezes cada resposta aparece, em número e em porcentagem, [p=0.2] e {c}idades agrupadas de dez em dez anos. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
