# Estudativo · Questão 032 — ENEM 2025, 2º dia, caderno amarelo, questão 148: uma livraria tem estoque de ficção científica,
# autoajuda, romance e biografia (barras: autor brasileiro e estrangeiro) e uma enquete deu a demanda de cada gênero (linha).
# O gerente só encomenda o gênero cujo estoque não atende a demanda. Leitura do gráfico (escala de 10 em 10; valores lidos
# na figura): ficção 80 + 120 = 200 ≥ 160; autoajuda 50 + 80 = 130 < 135 (faltam 5); romance 40 + 105 = 145 ≥ 140;
# biografia 45 + 50 = 95 ≥ 80. Só autoajuda falta → alternativa C. Pegadinhas: A (maior demanda, mas sobra estoque),
# B e D (biografia: menor demanda e menor estoque, mas sobra), E (romance: menos livros brasileiros, mas o total atende).
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: ler o gráfico (barras × linha, escala) → 2: estoque total e a comparação com a demanda →
# passo 1: ficção → passo 2: autoajuda → passo 3: romance → passo 4: biografia → C → pegadinhas → desafio → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: estoque e demanda na livraria (leitura de gráfico)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nas contas, fale devagar e com clareza, número por número. Faça as perguntas com "
            "curiosidade genuína, mostre surpresa na resposta e comemore o resultado. Respeite as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão cento e quarenta e oito do ENEM dois mil e vinte e cinco. [p=0.2] Uma livraria vende quatro gêneros: "
        "[p=0.1] ficção científica, [p=0.1] autoajuda, [p=0.1] romance [p=0.1] e biografia. [p=0.3] {b}O gráfico mostra "
        "o *estoque* de cada gênero [p=0.1] e a *demanda* dos clientes. [p=0.3] {c}O gerente só vai encomendar livros "
        "[p=0.1] do gênero em que o estoque *não dá conta* da demanda. [p=0.3] {d}Qual é esse gênero? [p=0.3] {e}Nessa "
        "aula, [p=0.1] você vai usar a *leitura de gráfico* [p=0.1] e a *comparação* entre estoque e demanda."),
    dict(id="02", block="leitura", text=
        "{a}Ferramenta um: [p=0.1] ler o gráfico. [p=0.3] {b}Cada gênero tem *duas barras:* [p=0.1] a laranja é de "
        "autores brasileiros, [p=0.1] e a verde, [p=0.1] de autores estrangeiros. [p=0.3] {c}A *linha azul* é a demanda. "
        "[p=0.3] {d}E a escala vai de *dez em dez:* [p=0.1] siga o topo de cada barra [p=0.1] até o eixo da esquerda."),
    dict(id="03", block="comparar", text=
        "{a}Ferramenta dois: [p=0.1] comparar. [p=0.3] {b}O estoque de um gênero [p=0.1] é a *soma* das duas barras. "
        "[p=0.3] {c}Se o estoque for *maior ou igual* à demanda, [p=0.1] dá conta. [p=0.2] {d}Se for *menor,* [p=0.1] "
        "falta livro, [p=0.1] e o gerente precisa encomendar."),
    dict(id="04", block="ficcao", text=
        "{a}Passo um: [p=0.1] ficção científica. [p=0.3] {b}Oitenta brasileiros [p=0.1] mais cento e vinte estrangeiros: "
        "[p=0.1] *duzentos* livros. [p=0.3] {c}A demanda é cento e sessenta. [p=0.2] Sobram quarenta. [p=0.1] *Dá conta.*"),
    dict(id="05", block="autoajuda", text=
        "{a}Passo dois: [p=0.1] autoajuda. [p=0.3] {b}Cinquenta [p=0.1] mais oitenta: [p=0.1] *cento e trinta* livros. "
        "[p=0.3] {c}E a demanda? [p=0.2] O ponto azul fica *acima* do cento e trinta, [p=0.1] perto de cento e trinta e "
        "cinco. [p=0.3] {d}O estoque é *menor* que a demanda. [p=0.2] Aqui *falta* livro!"),
    dict(id="06", block="romance", text=
        "{a}Passo três: [p=0.1] romance. [p=0.3] {b}Quarenta [p=0.1] mais cento e cinco: [p=0.1] *cento e quarenta e "
        "cinco.* [p=0.3] {c}A demanda é cento e quarenta. [p=0.2] Foi por pouco, [p=0.1] mas *dá conta.*"),
    dict(id="07", block="biografia", text=
        "{a}Passo quatro: [p=0.1] biografia. [p=0.3] {b}Quarenta e cinco [p=0.1] mais cinquenta: [p=0.1] *noventa e "
        "cinco.* [p=0.3] {c}A demanda é oitenta. [p=0.2] *Dá conta* também."),
    dict(id="08", block="resposta", text=
        "{a}Resumindo: [p=0.1] ficção, romance e biografia dão conta. [p=0.3] {b}O único gênero em que o estoque é menor "
        "que a demanda [p=0.1] é a *autoajuda.* [p=0.3] {c}Alternativa *C.*"),
    dict(id="09", block="pegadinhas", text=
        "{a}E as outras? [p=0.3] {b}A *A* olha só a maior demanda, [p=0.1] mas ficção tem duzentos livros: [p=0.1] "
        "sobra estoque. [p=0.3] {c}A *B* e a *D* falam da biografia, [p=0.1] que tem a menor demanda e o menor estoque, "
        "[p=0.1] mas o estoque dá conta. [p=0.3] {d}E a *E* olha só os autores brasileiros do romance, [p=0.1] e esquece os "
        "estrangeiros."),
    dict(id="10", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}Se a demanda por biografia *dobrasse,* [p=0.1] o gerente teria que encomendar? "
        "[p=0.2] Quantos livros, [p=0.1] no mínimo? [p=0.3] {c}Deixe sua resposta nos comentários."),
    dict(id="11", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}Leia cada barra [p=0.1] na escala do gráfico. [p=0.2] {c}Some as barras do "
        "mesmo gênero. [p=0.2] {d}E compare com a demanda: [p=0.1] estoque menor, [p=0.1] encomenda."),
    dict(id="12", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*gráfico de barras,* [p=0.2] {c}*gráfico de linhas* [p=0.2] {d}e *leitura de gráficos e tabelas.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
