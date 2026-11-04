# Estudativo · Questão 022 — ENEM 2025, 2º dia, caderno amarelo, questão 143: nos 100 metros rasos, a marca de
# referência é 10,00 s; em 2009, Usain Bolt fez 9,58 s. Diferença: 10,00 − 9,58 = 0,42 s → alternativa B.
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: casas decimais (9,58 = 9 inteiros, 5 décimos, 8 centésimos; 10 = 10,00) → A FERRAMENTA 2:
# subtração com empréstimo (52 − 17) → passo 1: armar a conta, vírgula embaixo de vírgula → passo 2: os empréstimos em
# cadeia (10,00 = 9 inteiros + 9 décimos + 10 centésimos) → 0,42 → passo 3: conferir pela soma (9,58 + 0,42 = 10,00) → B
# → pegadinhas: esquecer um empréstimo dá 0,52 (C) ou 1,42 (E), e a soma de conferência derruba as duas →
# generaliza: 0,42 s na pista (quem faz 10,00 s corre 10 m por segundo: em 9,58 s, 95,8 m → 4,2 m atrás, supondo
# velocidade constante) + desafio (9,87 s) → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: o recorde de Usain Bolt (subtração com decimais e empréstimo)"

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
        "{a}Questão cento e quarenta e três do ENEM dois mil e vinte e cinco. [p=0.2] Nos cem metros rasos, [p=0.1] a "
        "marca de referência é *dez segundos.* [p=0.3] {b}Em dois mil e nove, [p=0.1] Usain Bolt fez [p=0.1] *nove "
        "vírgula cinquenta e oito segundos.* [p=0.3] {c}A pergunta: [p=0.1] qual é a diferença entre as duas marcas? "
        "[p=0.3] {d}Parece fácil, [p=0.1] mas duas alternativas são armadilhas [p=0.1] para quem esquece um detalhe da "
        "conta."),
    dict(id="02", block="decimais", text=
        "{a}Primeiro, [p=0.1] o que cada algarismo vale. [p=0.3] {b}Em nove vírgula cinquenta e oito, [p=0.1] o nove "
        "são *nove inteiros,* [p=0.1] o cinco são *cinco décimos* [p=0.1] e o oito são *oito centésimos.* [p=0.3] "
        "{c}E o dez? [p=0.2] Dez é o mesmo que *dez vírgula zero zero:* [p=0.1] zero décimos [p=0.1] e zero "
        "centésimos. [p=0.2] {d}Completar com zeros não muda o número, [p=0.1] e deixa as duas marcas com o mesmo "
        "número de casas."),
    dict(id="03", block="emprestimo", text=
        "{a}Agora, [p=0.1] a ferramenta da conta: [p=0.1] a subtração com *empréstimo.* [p=0.3] {b}Cinquenta e dois "
        "menos dezessete. [p=0.2] Dois menos sete [p=0.1] não dá. [p=0.3] {c}Então o dois pede *uma dezena* emprestada "
        "ao cinco: [p=0.1] vira doze, [p=0.1] e o cinco vira quatro. [p=0.3] {d}Doze menos sete, [p=0.1] cinco. "
        "[p=0.2] Quatro menos um, [p=0.1] três. [p=0.2] Trinta e cinco."),
    dict(id="04", block="armar", text=
        "{a}Passo um: [p=0.1] armar a conta. [p=0.3] {b}A regra de ouro: [p=0.1] *vírgula embaixo de vírgula.* "
        "[p=0.2] Assim, [p=0.1] inteiro fica embaixo de inteiro, [p=0.1] décimo embaixo de décimo [p=0.1] e centésimo "
        "embaixo de centésimo. [p=0.3] {c}Em cima, [p=0.1] o maior: [p=0.1] dez vírgula zero zero. [p=0.2] Embaixo, "
        "[p=0.1] nove vírgula cinquenta e oito."),
    dict(id="05", block="conta", text=
        "{a}Passo dois: [p=0.1] a conta, da direita para a esquerda. [p=0.3] {b}Zero menos oito [p=0.1] não dá, "
        "[p=0.1] e o vizinho também é zero. [p=0.2] O empréstimo vem *lá do dez.* [p=0.3] {c}Dez inteiros viram *nove "
        "inteiros, [p=0.1] nove décimos [p=0.1] e dez centésimos.* [p=0.3] {d}Agora vai: [p=0.1] dez menos oito, "
        "[p=0.1] dois. [p=0.2] Nove menos cinco, [p=0.1] quatro. [p=0.2] Nove menos nove, [p=0.1] zero. [p=0.3] "
        "{e}Zero vírgula quarenta e dois."),
    dict(id="06", block="conferir", text=
        "{a}Passo três: [p=0.1] conferir. [p=0.3] {b}Se a diferença está certa, [p=0.1] somar com o tempo do Bolt "
        "[p=0.1] tem que dar a marca de referência. [p=0.3] {c}Nove vírgula cinquenta e oito [p=0.1] mais zero vírgula "
        "quarenta e dois: [p=0.1] *dez vírgula zero zero.* [p=0.2] Confere! [p=0.3] {d}Alternativa *B.*"),
    dict(id="07", block="pegadinhas", text=
        "{a}Agora, [p=0.1] as armadilhas. [p=0.3] {b}Quem pega o empréstimo para os centésimos [p=0.1] mas esquece de "
        "descontar nos décimos [p=0.1] faz dez menos cinco, [p=0.1] e chega a *zero vírgula cinquenta e dois.* "
        "[p=0.2] Letra C. [p=0.3] {c}Quem esquece de descontar nos inteiros [p=0.1] faz dez menos nove, [p=0.1] e "
        "chega a *um vírgula quarenta e dois.* [p=0.2] Letra E. [p=0.3] {d}A conferência derruba as duas: [p=0.1] nove "
        "vírgula cinquenta e oito mais zero vírgula cinquenta e dois [p=0.1] dá dez vírgula um, [p=0.2] e mais um "
        "vírgula quarenta e dois [p=0.1] dá onze."),
    dict(id="08", block="generaliza", text=
        "{a}E quanto é zero vírgula quarenta e dois segundo [p=0.1] na pista? [p=0.3] {b}Quem faz cem metros em dez "
        "segundos [p=0.1] corre dez metros por segundo, [p=0.1] supondo a mesma velocidade o tempo todo. [p=0.2] Em "
        "nove vírgula cinquenta e oito segundos, [p=0.1] percorre noventa e cinco vírgula oito metros. [p=0.3] "
        "{c}Quando o Bolt cruza a linha, [p=0.1] esse corredor ainda está *quatro vírgula dois metros* atrás. [p=0.3] "
        "{d}Agora é com você: [p=0.1] um atleta fez nove vírgula oitenta e sete. [p=0.2] Quantos segundos mais lento "
        "que o Bolt? [p=0.2] Deixe sua resposta nos comentários."),
    dict(id="09", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}Primeiro, [p=0.1] complete com zeros [p=0.1] e ponha vírgula embaixo de "
        "vírgula. [p=0.2] {c}Depois, [p=0.1] subtraia da direita para a esquerda, [p=0.1] pegando emprestado quando "
        "não der. [p=0.2] {d}Cada empréstimo tem que ser *descontado* na casa vizinha. [p=0.2] {e}E confira pela "
        "soma."),
    dict(id="10", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*números decimais,* [p=0.2] {c}*adição e subtração de decimais* [p=0.2] {d}e *velocidade média.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
