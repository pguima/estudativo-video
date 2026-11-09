# Estudativo · FIS-ELE-026 — Praticando: leis de Kirchhoff (Física · Eletricidade · Leis de Kirchhoff · extensão · prática).
# Habilidade: resolver circuitos que não se reduzem a um resistor equivalente.
# Pré-requisitos: FIS-ELE-024 (nós, malhas, sinais, atalho de uma malha), FIS-ELE-025 (sistema, atalho da tensão entre dois nós).
# Próxima: nenhuma (última aula da trilha Eletricidade).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Prática: quatro questões inéditas, criadas para esta aula.
# Contas: Q1 3 + i = 5 + 2 → i = 4 A.  Q2 (12 + 6 − 3)/5 = 15/5 = 3 A.
#   Q3 ε1 = 8 V, R1 = 2; ε2 = 14 V, R2 = 4; R3 = 2: 8 = 2i1 + 2i3; 14 = 4i2 + 2i3; i3 = i1 + i2 → 8 = 4i1 + 2i2; 14 = 2i1 + 6i2;
#      i2 = 4 − 2i1 → 14 = 2i1 + 24 − 12i1 → 10i1 = 10 → i1 = 1, i2 = 2, i3 = 3 (atalho: U = 6 V).
#   Q4 ε1 = 12 V, R1 = 1; ε2 = 6 V, R2 = 1; R3 = 4: 4(12 − U) + 4(6 − U) = U → 72 = 9U → U = 8; i1 = 4, i2 = −2, i3 = 2;
#      guardada ε2·|i2| = 6·2 = 12 W; R2·i2² = 1·4 = 4 W (o ramo recebe 8·2 = 16 W = 12 + 4).

TITULO = "Praticando: leis de Kirchhoff"

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
    dict(id="s01", block="gancho", text="{a}Na prova, Kirchhoff aparece de três jeitos: [p=0.1] {b}um nó, [p=0.1] {c}uma malha [p=0.1] {d}ou duas malhas. [p=0.3] {e}Até o fim desta aula, você vai resolver uma questão de cada, [p=0.1] {f}mais uma com uma surpresa no sinal."),
    # método
    dict(id="s02", block="metodo", text="Antes, o método. [p=0.2] {a}Dê nome e sentido a cada corrente. [p=0.2] {b}No nó, o que chega é igual ao que sai. [p=0.2] {c}Na malha, o gerador soma épsilon se você entra pelo negativo, [p=0.1] e o resistor subtrai erre vezes i se você anda a favor da corrente. [p=0.3] {d}Com só dois nós, use a tensão entre eles."),
    # questão 1
    dict(id="s03", block="q1", text="Questão um. [p=0.2] {a}Num nó chegam três ampères e uma corrente desconhecida. [p=0.2] {b}Saem cinco ampères e dois ampères. [p=0.3] {c}Quanto vale a corrente desconhecida? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s04", block="q1", text="{a}O que chega é igual ao que sai: [p=0.1] {b}três mais i, igual a cinco mais dois. [p=0.2] {c}Três mais i, igual a sete: [p=0.1] {d}i vale quatro ampères."),
    # questão 2
    dict(id="s05", block="q2", text="Questão dois. [p=0.2] {a}Uma malha tem três geradores: [p=0.1] {b}doze volts e seis volts empurrando num sentido, [p=0.1] {c}e três volts empurrando no outro. [p=0.2] {d}As resistências da volta somam cinco ohms. [p=0.3] {e}Qual é a corrente? [p=0.2] {f}Pause e tente. [p=3.0]"),
    dict(id="s06", block="q2", text="{a}Uma malha só: use o atalho. [p=0.2] {b}A favor: doze mais seis, dezoito. [p=0.1] {c}Contra: três. [p=0.2] {d}Dezoito menos três, quinze, dividido por cinco: [p=0.1] {e}três ampères, no sentido dos geradores de doze e de seis volts."),
    # questão 3
    dict(id="s07", block="q3", text="Questão três. [p=0.2] {a}Esquerda: gerador de oito volts e resistor de dois ohms. [p=0.1] {b}Direita: gerador de catorze volts e resistor de quatro ohms. [p=0.1] {c}Meio: dois ohms. [p=0.2] Os geradores têm o positivo para cima. [p=0.3] {d}Monte o sistema e ache as correntes. [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s08", block="q3", text="{a}i um sobe pela esquerda, i dois sobe pela direita, i três desce pelo meio: [p=0.1] {b}i três igual a i um mais i dois. [p=0.3] {c}Malha da esquerda: oito igual a dois i um mais dois i três. [p=0.1] {d}Da direita: catorze igual a quatro i dois mais dois i três."),
    dict(id="s09", block="q3", text="{a}Trocando i três: [p=0.1] oito igual a quatro i um mais dois i dois; [p=0.1] {b}catorze igual a dois i um mais seis i dois. [p=0.3] {c}Da primeira, dividida por dois: i dois igual a quatro menos dois i um. [p=0.2] {d}Na segunda: catorze igual a dois i um, mais vinte e quatro, menos doze i um, [p=0.1] que é vinte e quatro menos dez i um. [p=0.2] {e}Dez i um igual a dez: [p=0.1] {f}i um vale um ampère, [p=0.1] i dois, dois, [p=0.1] e i três, três."),
    # questão 4
    dict(id="s10", block="q4", text="Questão quatro. [p=0.2] {a}Esquerda: gerador de doze volts e resistor de um ohm. [p=0.1] {b}Direita: uma bateria de seis volts e resistor de um ohm. [p=0.1] {c}Meio: quatro ohms. [p=0.2] As duas com o positivo para cima. [p=0.3] {d}A bateria de seis volts está fornecendo energia ou sendo carregada? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s11", block="q4", text="{a}Dois nós: use a tensão entre eles. [p=0.2] {b}Doze menos u, sobre um, mais seis menos u, sobre um, igual a u sobre quatro. [p=0.3] {c}Multiplique tudo por quatro: [p=0.1] setenta e dois menos oito u, igual a u. [p=0.2] {d}u vale oito volts."),
    dict(id="s12", block="q4", text="{a}Na direita: seis menos oito, dividido por um: [p=0.1] {b}menos dois ampères. [p=0.3] {c}O sinal de menos diz que a corrente desce pela bateria de seis volts: [p=0.1] {d}ela entra pelo positivo. [p=0.2] {e}A bateria está sendo carregada. [p=0.3] {f}Confira o nó: na esquerda, doze menos oito, quatro ampères. [p=0.2] Quatro menos dois, dois, [p=0.1] igual a oito sobre quatro."),
    dict(id="s13", block="q4", text="{a}E quanta potência vira energia química nela? [p=0.2] {b}Épsilon vezes i: [p=0.1] {c}seis vezes dois, doze watts, [p=0.1] ou seja, doze joules a cada segundo. [p=0.3] {d}E o resistor de um ohm do mesmo ramo esquenta com um vezes dois ao quadrado: [p=0.1] {e}quatro watts."),
    # fechamento
    dict(id="s14", block="fim", text="Resumindo: {a}nó, malha e sistema, [p=0.1] sempre com a regra de sinais; [p=0.2] {b}e o sinal de menos na resposta não é erro: [p=0.1] {c}é o sentido real da corrente. [p=0.3] {d}Com esta aula, você fecha a trilha de Eletricidade. [p=0.2] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
