# Estudativo · Resolução ENEM 2025, 2º dia, caderno 5 (amarelo), questão 153 — código de identificação de visitante.
# Modelo das questões antigas (canais/enem/questoes, git 5eeb6d2): print do enunciado no 1º quadro, ferramentas pelo nome,
# passos numerados, por que as outras estão erradas, atalho, desafio, resumo e convite para as aulas. Com efeitos, sem trilha.
# Regra: 7 dígitos = andar (1 casa, 1 a 4) | setor (2 casas, 01 a 20) | funcionário (3 casas, 001 a 135) | turno (0 manhã, 1 tarde).
# Dados: 10 h da manhã, funcionário 109, setor 08, 2º andar → 2 | 08 | 109 | 0 = 2081090 → D.
# Pegadinhas: A 0|109|08|2 (ordem invertida) · B 02|8|109|0 (zero no andar) · C 10|109|8|2 (hora 10 e ordem invertida)
# · E 2|8|109|10 (sem o zero do setor e hora 10 no lugar do turno).
# Desafio: 15 h (tarde), funcionário 42, setor 15, 4º andar → 4 | 15 | 042 | 1 = 4150421.
# Aulas: MAT-NUM-001 (Algarismos e valor posicional) · MAT-LEI-001 (Achar a pergunta e os dados úteis).
# Enunciado: enunciado/questao.png. Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "ENEM 2025, questão 153: o código do visitante"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nos números, fale devagar e com clareza, dígito por dígito. Faça as perguntas com "
            "curiosidade genuína, mostre surpresa nas pegadinhas e comemore o resultado. Respeite as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="s01", block="gancho", text=
        "{a}Questão cento e cinquenta e três do ENEM dois mil e vinte e cinco. [p=0.2] Uma empresa identifica cada "
        "visitante com um *código de sete dígitos.* [p=0.3] {b}O código tem quatro pedaços: [p=0.1] *andar, setor, "
        "funcionário* e *turno.* [p=0.3] {c}O visitante chegou às *dez da manhã,* [p=0.1] vai falar com o *funcionário "
        "cento e nove,* [p=0.1] do *setor zero oito,* [p=0.1] no *segundo andar.* [p=0.3] {d}Qual é o código dele? "
        "[p=0.3] {e}Nessa resolução, você vai usar duas ideias: [p=0.1] *a posição de cada dígito* [p=0.1] e o *zero "
        "à esquerda.*"),
    dict(id="s02", block="posicao", text=
        "{a}Ideia um: [p=0.1] *a posição manda.* [p=0.3] {b}Num código, cada casa tem uma função fixa. [p=0.3] "
        "{c}Se você trocar a ordem dos pedaços, [p=0.1] {d}sai *outro código,* [p=0.1] mesmo usando os mesmos números. "
        "[p=0.3] {e}Por isso a questão avisa: [p=0.1] *da esquerda para a direita.*"),
    dict(id="s03", block="zero", text=
        "{a}Ideia dois: [p=0.1] o *zero à esquerda.* [p=0.3] {b}O setor sempre ocupa *duas casas,* [p=0.1] por isso "
        "vai de *zero um* a vinte. [p=0.3] {c}O setor oito vira *zero oito.* [p=0.3] {d}E o funcionário ocupa *três "
        "casas:* [p=0.1] o funcionário sete, por exemplo, seria *zero zero sete.* [p=0.3] {e}O zero à esquerda não "
        "muda o número. [p=0.1] Ele só *preenche a casa.*"),
    dict(id="s04", block="monta", text=
        "{a}Agora, a resolução. [p=0.2] {b}Passo um: [p=0.1] o andar. [p=0.2] Segundo andar: [p=0.1] {c}a primeira "
        "casa é *dois.*"),
    dict(id="s05", block="monta", text=
        "{a}Passo dois: [p=0.1] o setor. [p=0.2] Setor zero oito: [p=0.1] {b}as casas dois e três ficam *zero* e "
        "*oito.*"),
    dict(id="s06", block="monta", text=
        "{a}Passo três: [p=0.1] o funcionário. [p=0.2] Funcionário cento e nove: [p=0.1] {b}*um, zero, nove,* [p=0.1] "
        "nas casas quatro, cinco e seis."),
    dict(id="s07", block="monta", text=
        "{a}Passo quatro: [p=0.1] o turno. [p=0.2] Ele chegou às dez da *manhã.* [p=0.3] {b}Atenção: [p=0.1] o dez é "
        "o horário, [p=0.1] e *não entra no código.* [p=0.3] {c}Manhã é o dígito *zero.*"),
    dict(id="s08", block="monta", text=
        "{a}Juntando tudo: [p=0.1] *dois, zero, oito, um, zero, nove, zero.* [p=0.3] {b}Sete dígitos, [p=0.1] cada um "
        "na sua casa. [p=0.3] {c}Alternativa *D.*"),
    dict(id="s09", block="pegadinhas", text=
        "{a}E as outras? [p=0.2] Todas usam os números certos, [p=0.1] mas no lugar errado. [p=0.3] {b}A *A* [p=0.1] "
        "inverteu a ordem: [p=0.1] começou pelo turno e terminou no andar. [p=0.3] {c}A *B* [p=0.1] colocou o zero no "
        "andar, [p=0.1] e não no setor. [p=0.3] {d}A *C* [p=0.1] usou o *dez* do horário [p=0.1] e ainda inverteu a "
        "ordem. [p=0.3] {e}E a *E* [p=0.1] esqueceu o zero do setor [p=0.1] e trocou o turno pelo *dez.*"),
    dict(id="s10", block="atalho", text=
        "{a}Agora, o atalho de prova. [p=0.2] Você nem precisa montar o código inteiro. [p=0.2] {b}O primeiro dígito "
        "é o andar, *dois:* [p=0.1] {c}corta a A, a B e a C. [p=0.3] {d}O segundo dígito é o começo do setor, *zero:* "
        "[p=0.1] {e}corta a E. [p=0.3] {f}Sobrou a *D,* em dois olhares."),
    dict(id="s11", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}Um visitante chegou às *três da tarde* [p=0.1] para falar com o *funcionário "
        "quarenta e dois,* [p=0.1] do *setor quinze,* [p=0.1] no *quarto andar.* [p=0.3] {c}Qual é o código dele? "
        "[p=0.3] {d}Deixe sua resposta nos comentários."),
    dict(id="s12", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}Separe o código em pedaços. [p=0.2] {c}Complete cada pedaço com zeros à "
        "esquerda. [p=0.2] {d}E não confunda o horário com o turno."),
    dict(id="s13", block="aulas", text=
        "{a}As ideias dessa questão [p=0.1] têm *aula completa* aqui no Estudativo: [p=0.3] {b}*algarismos e valor "
        "posicional* [p=0.2] {c}e *achar a pergunta e os dados úteis.* [p=0.3] {d}Se quiser aprender desde o começo, "
        "[p=0.1] procure essas aulas aqui no canal. [p=0.4] {e}E se essa questão te ajudou, [p=0.1] inscreva-se no "
        "*Estudativo* [p=0.1] para não perder a próxima questão."),
]
