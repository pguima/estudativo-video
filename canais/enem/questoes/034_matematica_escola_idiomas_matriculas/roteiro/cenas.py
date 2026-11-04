# Estudativo · Questão 034 — ENEM 2025, 2º dia, caderno amarelo, questão 149: escola de idiomas; o gráfico de setores dá a
# porcentagem de matrículas por idioma em 2023 (inglês 60%, espanhol 25%, francês 10%, alemão 5%) e o de barras dá a
# quantidade em 2024 (280, 80, 20, 20). Em 2025: total igual ao de 2024 e porcentagens iguais às de 2023.
# Total 2024 = 280 + 80 + 20 + 20 = 400; francês = 10% de 400 = 40 → alternativa E. Conferência: 240 + 100 + 40 + 20 = 400.
# Pegadinhas: C (20 = francês em 2024, gráfico errado), A (2 = 10% de 20), D (22 = 20 + 2).
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: os dois gráficos (o que cada um mede) → 2: porcentagem de um total → passo 1: total de 2024 →
# passo 2: 10% de 400 → conferência (todos os idiomas) → E → pegadinhas → desafio → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: matrículas na escola de idiomas (porcentagem e gráficos)"

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
        "{a}Questão cento e quarenta e nove do ENEM dois mil e vinte e cinco. [p=0.2] Uma escola de idiomas tem cursos de "
        "inglês, [p=0.1] espanhol, [p=0.1] francês [p=0.1] e alemão. [p=0.3] {b}Para dois mil e vinte e cinco, [p=0.1] o "
        "gerente estimou o *total* de matrículas igual ao de dois mil e vinte e quatro, [p=0.2] {c}e as *porcentagens* "
        "iguais às de dois mil e vinte e três. [p=0.3] {d}Quantas matrículas o curso de *francês* vai ter? [p=0.3] "
        "{e}Nessa aula, [p=0.1] você vai usar a *leitura de gráficos* [p=0.1] e a *porcentagem.*"),
    dict(id="02", block="graficos", text=
        "{a}Ferramenta um: [p=0.1] os dois gráficos. [p=0.3] {b}A pizza é de dois mil e vinte e três [p=0.1] e mostra "
        "*porcentagens:* [p=0.2] inglês sessenta, [p=0.1] espanhol vinte e cinco, [p=0.1] francês dez [p=0.1] e alemão "
        "cinco por cento. [p=0.3] {c}As barras são de dois mil e vinte e quatro [p=0.1] e mostram *quantidades* de alunos."),
    dict(id="03", block="porcentagem", text=
        "{a}Ferramenta dois: [p=0.1] porcentagem de um total. [p=0.3] {b}Dez por cento é *dez em cada cem.* [p=0.2] "
        "{c}Então, dez por cento de um número [p=0.1] é esse número *dividido por dez.* [p=0.3] {d}Por exemplo: [p=0.1] "
        "dez por cento de cem [p=0.1] é dez."),
    dict(id="04", block="total", text=
        "{a}Passo um: [p=0.1] o total de dois mil e vinte e quatro. [p=0.3] {b}Somando as barras: [p=0.1] duzentos e "
        "oitenta, [p=0.1] mais oitenta, [p=0.1] mais vinte, [p=0.1] mais vinte. [p=0.3] {c}Dá *quatrocentas* matrículas. "
        "[p=0.2] {d}E esse é o total previsto para dois mil e vinte e cinco."),
    dict(id="05", block="frances", text=
        "{a}Passo dois: [p=0.1] o francês. [p=0.3] {b}Em dois mil e vinte e três, [p=0.1] o francês tinha *dez por cento* "
        "das matrículas. [p=0.3] {c}Dez por cento de quatrocentos: [p=0.1] quatrocentos dividido por dez. [p=0.2] {d}Dá "
        "*quarenta* matrículas."),
    dict(id="06", block="conferencia", text=
        "{a}Vamos conferir com todos os idiomas. [p=0.3] {b}Sessenta por cento de quatrocentos: [p=0.1] duzentos e "
        "quarenta. [p=0.2] Vinte e cinco por cento: [p=0.1] cem. [p=0.2] Dez por cento: [p=0.1] quarenta. [p=0.2] Cinco "
        "por cento: [p=0.1] vinte. [p=0.3] {c}Somando tudo: [p=0.1] *quatrocentos.* [p=0.2] Fechou!"),
    dict(id="07", block="resposta", text=
        "{a}Em dois mil e vinte e cinco, [p=0.1] o francês deve ter *quarenta* matrículas. [p=0.3] {b}O dobro do que "
        "tinha em dois mil e vinte e quatro! [p=0.3] {c}Alternativa *E.*"),
    dict(id="08", block="pegadinhas", text=
        "{a}E as outras? [p=0.3] {b}A *C,* [p=0.1] vinte, [p=0.1] é o francês de dois mil e vinte e quatro: [p=0.1] é ler "
        "o gráfico errado. [p=0.3] {c}A *A,* [p=0.1] dois, [p=0.1] é dez por cento de vinte. [p=0.2] {d}E a *D,* [p=0.1] "
        "vinte e dois, [p=0.1] soma esse dois aos vinte. [p=0.3] {e}A *B,* [p=0.1] doze, [p=0.1] também não sai da conta "
        "certa."),
    dict(id="09", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}Se o total de dois mil e vinte e cinco fosse *quinhentas* matrículas, [p=0.1] "
        "quantos alunos teria o *espanhol?* [p=0.3] {c}Deixe sua resposta nos comentários."),
    dict(id="10", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}Veja o que cada gráfico mede: [p=0.1] porcentagem ou quantidade. [p=0.2] {c}Ache "
        "o total. [p=0.2] {d}E aplique a porcentagem sobre esse total."),
    dict(id="11", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*porcentagem,* [p=0.2] {c}*gráfico de setores* [p=0.2] {d}e *gráfico de barras.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
