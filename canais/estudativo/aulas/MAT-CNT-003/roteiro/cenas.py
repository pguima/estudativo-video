# Estudativo · MAT-CNT-003 — Contar os divisores de um número (Matemática · Contagem e Probabilidade).
# Habilidade: fatorar 72 = 2³ · 3² e dizer que ele tem 12 divisores, somando 1 a cada expoente e multiplicando.
# Pré-requisitos: MAT-CNT-001 (princípio multiplicativo), MAT-DIV-003 (fatoração), MAT-POT-004 (fatorar com potências). Próxima: MAT-CNT-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Fatoração pelas divisões sucessivas, como em MAT-DIV-003; expoente zero de MAT-POT-003.
# 72 → 36 → 18 → 9 → 3 → 1 = 2³ · 3². Fator 2: 2⁰, 2¹, 2², 2³ = 1, 2, 4, 8 · fator 3: 3⁰, 3¹, 3² = 1, 3, 9.
# Tabela (E.tabela) 4 × 3, linhas 1, 2, 4, 8 e colunas 1, 3, 9: 1 3 9 / 2 6 18 / 4 12 36 / 8 24 72 = 12 divisores.
# Erro: 3 × 2 = 6 (só 6, 12, 18, 24, 36, 72; somem 1, 2, 3, 4, 8, 9). Atalho: ímpares = 3 (1, 3, 9); pares = 12 − 3 = 9.
# Questão: 360 = 2³ · 3² · 5 → 4 × 3 × 2 = 24 divisores · ímpares 3 × 2 = 6 (1, 3, 5, 9, 15, 45).

TITULO = "Contar os divisores de um número"

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
    dict(id="s01", block="gancho", text="{a}Setenta e duas cadeiras, [p=0.2] arrumadas em {b}fileiras iguais. [p=0.3] De quantos jeitos dá para arrumar? [p=0.3] Uma fileira de setenta e duas cadeiras, [p=0.2] duas fileiras de trinta e seis, [p=0.2] três fileiras de vinte e quatro... [p=0.3] Cada jeito é {c}um divisor de setenta e dois. [p=0.2] E dá para contar todos {d}sem listar nenhum."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta os divisores de qualquer número [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai precisar de {a}três coisas: [p=0.2] {b}fatorar usando potências, [p=0.2] {c}o princípio multiplicativo, com as casinhas, [p=0.2] e {d}saber que um número elevado a zero dá um. [p=0.3] Se faltar alguma, procure no canal."),
    # fatorar
    dict(id="s04", block="fatorar", text="Primeiro, fatore. [p=0.2] {a}Setenta e dois dividido por dois dá trinta e seis. [p=0.2] Por dois dá {b}dezoito. [p=0.2] Por dois dá {c}nove. [p=0.2] Por três dá {d}três. [p=0.2] Por três dá {e}um. [p=0.3] Para conferir: oito vezes nove dá setenta e dois."),
    dict(id="s05", block="fatorar", text="Foram {a}três divisões por dois e duas por três. [p=0.3] {b}Setenta e dois é dois ao cubo vezes três ao quadrado."),
    # casinhas
    dict(id="s06", block="ideia", text="Agora pense: [p=0.2] {a}o que é um divisor de setenta e dois? [p=0.3] É um número {b}montado só com pedaços dessa fatoração. [p=0.2] Ele pode usar fatores dois e fatores três, [p=0.2] mas {c}nunca mais do que o setenta e dois tem, [p=0.2] e {d}nenhum outro primo. [p=0.3] O seis, por exemplo, usa um fator dois e um fator três."),
    dict(id="s07", block="ideia", text="Quantas vezes o fator dois pode aparecer no divisor? [p=0.2] {a}Nenhuma vez, [p=0.2] uma, [p=0.2] duas ou três vezes. [p=0.3] São {b}quatro opções: [p=0.2] dois elevado a zero, a um, ao quadrado e ao cubo. [p=0.2] Elas dão {c}um, [p=0.2] dois, [p=0.2] quatro e oito."),
    dict(id="s08", block="ideia", text="E o fator três? [p=0.2] {a}Nenhuma vez, [p=0.2] uma ou duas vezes. [p=0.3] São {b}três opções: [p=0.2] {c}um, [p=0.2] três e nove."),
    dict(id="s09", block="ideia", text="Montar um divisor é escolher {a}uma opção do fator dois e uma opção do fator três. [p=0.3] São etapas, e você faz todas: [p=0.2] é o princípio multiplicativo. [p=0.2] {b}Quatro vezes três dá doze divisores."),
    # tabela
    dict(id="s10", block="tabela", text="Veja na tabela. [p=0.2] {a}Nas linhas, um, [p=0.2] dois, [p=0.2] quatro e oito. [p=0.3] {b}Nas colunas, um, [p=0.2] três e nove. [p=0.3] Cada quadradinho é {c}a linha vezes a coluna. [p=0.3] Saem {d}doze divisores, nenhum repetido, nenhum faltando: [p=0.2] do {e}um até o setenta e dois."),
    # regra
    dict(id="s11", block="regra", text="A regra: {a}fatore usando potências, [p=0.2] {b}some um em cada expoente [p=0.2] e {c}multiplique os resultados. [p=0.3] Esse mais um é {d}a opção nenhuma vez."),
    dict(id="s12", block="regra", text="No setenta e dois, os expoentes são {a}três e dois. [p=0.2] {b}Três mais um dá quatro. [p=0.2] {c}Dois mais um dá três. [p=0.2] {d}Quatro vezes três dá doze. [p=0.3] Sem tabela e sem lista."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}esquecer esse mais um. [p=0.2] A pessoa multiplica os expoentes: [p=0.2] {b}três vezes dois dá seis. [p=0.3] Mas a tabela mostrou doze. [p=0.2] Ficaram de fora {c}os divisores sem o fator dois, como o nove, [p=0.2] {d}os sem o fator três, como o oito, [p=0.2] e até o {e}um."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para quando a prova pede {a}só os divisores ímpares, ou só os pares. [p=0.3] Ímpar não tem fator dois. [p=0.2] Então {b}ignore o dois: [p=0.2] sobra só o fator três, com {c}três opções. [p=0.2] Setenta e dois tem {d}três divisores ímpares: [p=0.2] um, [p=0.2] três e nove."),
    dict(id="s15", block="atalho", text="E os pares? [p=0.2] {a}Doze menos três dá nove. [p=0.3] Funciona porque {b}todo divisor ou é par, ou é ímpar. [p=0.3] Não compensa quando a questão quer {c}os divisores escritos, não só quantos são: [p=0.2] aí, {d}monte a tabela."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Você já viu que {a}trezentos e sessenta [p=0.2] é {b}dois ao cubo vezes três ao quadrado vezes cinco. [p=0.3] {c}Quantos divisores ele tem? [p=0.2] E {d}quantos são ímpares?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Some um em cada expoente. [p=0.2] {a}Três mais um dá quatro. [p=0.2] {b}Dois mais um dá três. [p=0.3] E o cinco? [p=0.2] Ele aparece uma vez: {c}o expoente é um, que não se escreve. [p=0.2] {d}Um mais um dá dois."),
    dict(id="s19", block="resposta", text="{a}Quatro vezes três dá doze. [p=0.2] {b}Doze vezes dois dá vinte e quatro divisores. [p=0.3] Para os ímpares, ignore o fator dois: [p=0.2] {c}três vezes dois dá seis."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}fatore, [p=0.2] {b}some um em cada expoente [p=0.2] e {c}multiplique."),
    dict(id="s21", block="fim", text="Na próxima aula, uma multiplicação que aparece o tempo todo em contagem ganha nome próprio: [p=0.2] {a}o fatorial. [p=0.3] E você aprende a {b}cortar contas enormes antes de fazer. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
