# Estudativo · FIS-ELE-025 — Circuito com duas malhas (Física · Eletricidade · Leis de Kirchhoff · extensão).
# Habilidade: montar e resolver o sistema de equações de um circuito com dois geradores.
# Pré-requisitos: FIS-ELE-024 (nós, malhas, sinais), MAT-EQU-020 (montar sistema), e por ela MAT-EQU-018 (substituição). Próxima: FIS-ELE-026.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Circuito: nós A (em cima) e B (embaixo); esquerda ε1 = 10 V + R1 = 2 Ω; meio R3 = 1 Ω; direita ε2 = 6 V + R2 = 2 Ω; os dois + para A.
# Atalho (tensão U entre os dois nós; cada ramo i = (ε − U)/R) usa só U = R·i, gerador e nós; vale para circuitos de dois nós.
# Contas: 10 = 2i1 + i3; 6 = 2i2 + i3; i3 = i1 + i2 → 10 = 3i1 + i2; 6 = i1 + 3i2; i2 = 10 − 3i1 → 6 = 30 − 8i1 → i1 = 3, i2 = 1, i3 = 4.
#   Malha de fora: 10 − 2·3 + 2·1 − 6 = 0. Atalho: (10 − U) + (6 − U) = 2U → U = 4 V.
#   Questão (sistema): 10 = 4i1 + i2; 8 = i1 + 3i2; i2 = 10 − 4i1 → 8 = 30 − 11i1 → i1 = 2; i2 = 2; i3 = 4.
#   Conferência pelo atalho: (10 − U)/3 + (8 − U)/2 = U → 20 − 2U + 24 − 3U = 6U → U = 4; i1 = 2, i2 = 2, i3 = 4.

TITULO = "Circuito com duas malhas"

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
    dict(id="s01", block="gancho", text="{a}Dois geradores, três ramos, três correntes desconhecidas. [p=0.3] {b}Parece muito, [p=0.1] mas {c}a lei dos nós e a das malhas viram um sistema de equações [p=0.1] que você já sabe resolver."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai montar e resolver esse sistema, [p=0.2] e {b}conhecer um atalho que resolve tudo com uma equação só."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}as leis de Kirchhoff, com a regra de sinais; [p=0.2] e {c}resolver um sistema por substituição: [p=0.1] isolar uma letra numa equação e levar para a outra. [p=0.3] Se faltar alguma, procure no canal."),
    # o circuito e as correntes
    dict(id="s04", block="circuito", text="Veja o circuito. [p=0.2] {a}No ramo da esquerda, um gerador de dez volts e um resistor de dois ohms. [p=0.2] {b}No da direita, um gerador de seis volts e outro resistor de dois ohms. [p=0.2] {c}No meio, um resistor de um ohm. [p=0.3] {d}Os três ramos ligam os mesmos dois nós: A em cima e B embaixo."),
    dict(id="s05", block="circuito", text="{a}Passo um: dê nome e sentido à corrente de cada ramo. [p=0.2] {b}i um sobe pela esquerda, [p=0.1] {c}i dois sobe pela direita, [p=0.1] {d}e i três desce pelo meio. [p=0.3] {e}Se algum chute estiver errado, a conta avisa com um sinal de menos."),
    dict(id="s06", block="circuito", text="{a}Passo dois: a lei dos nós em A. [p=0.2] {b}Chegam i um e i dois, e sai i três: [p=0.1] {c}i três é igual a i um mais i dois."),
    dict(id="s07", block="circuito", text="{a}Passo três: uma malha de cada lado. [p=0.2] {b}Na esquerda, subindo pelo gerador: mais dez, [p=0.1] {c}menos dois i um, [p=0.1] {d}menos um vezes i três, igual a zero. [p=0.3] {e}Na direita, do mesmo jeito: [p=0.1] {f}seis, menos dois i dois, menos i três, igual a zero."),
    # o sistema
    dict(id="s08", block="sistema", text="{a}Passo quatro: troque i três por i um mais i dois. [p=0.2] {b}Na esquerda: dez igual a três vezes i um, mais i dois. [p=0.2] {c}Na direita: seis igual a i um, mais três vezes i dois. [p=0.3] {d}Duas equações, duas letras: [p=0.1] um sistema."),
    dict(id="s09", block="sistema", text="{a}Isole i dois na primeira: [p=0.1] {b}i dois igual a dez menos três i um. [p=0.3] {c}Leve para a segunda: [p=0.1] seis igual a i um, mais três vezes, abre parênteses, dez menos três i um, fecha parênteses. [p=0.3] {d}Seis igual a trinta menos oito i um: [p=0.1] {e}i um vale três ampères."),
    dict(id="s10", block="sistema", text="{a}Volte: i dois é dez menos nove, [p=0.1] {b}um ampère. [p=0.2] {c}E i três é três mais um, [p=0.1] {d}quatro ampères. [p=0.3] {e}Todos positivos: os chutes estavam certos."),
    dict(id="s11", block="sistema", text="{a}Confira na malha de fora, que você não usou. [p=0.2] {b}Mais dez, menos dois vezes três. [p=0.1] {c}Descendo pela direita, você anda contra i dois: mais dois vezes um. [p=0.1] {d}E entra pelo positivo do gerador de seis: menos seis. [p=0.2] {e}Dez, menos seis do resistor, mais dois, menos os seis volts do gerador: zero."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}escrever a lei dos nós em A e em B [p=0.1] e achar que tem duas equações. [p=0.3] {b}Em B, chega i três e saem i um e i dois: [p=0.1] {c}é a mesma equação, virada. [p=0.2] {d}A segunda equação tem que vir de uma malha."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho: [p=0.2] {a}chame de u a tensão entre A e B. [p=0.3] {b}No meio, a corrente é u dividido por um. [p=0.2] {c}Na esquerda, o gerador perde no resistor: [p=0.1] {d}i um é dez menos u, dividido por dois. [p=0.1] {e}Na direita, seis menos u, dividido por dois."),
    dict(id="s14", block="atalho", text="{a}Lei dos nós: dez menos u, sobre dois, mais seis menos u, sobre dois, igual a u. [p=0.3] {b}Multiplique tudo por dois: [p=0.1] dezesseis menos dois u, igual a dois u. [p=0.2] {c}u vale quatro volts. [p=0.3] {d}Daí, cada corrente sai direto: [p=0.1] três, um e quatro ampères."),
    dict(id="s15", block="atalho", text="Funciona porque {a}os três ramos ligam os mesmos dois nós: [p=0.1] {b}a tensão entre eles é a mesma para todos. [p=0.3] {c}Não compensa quando o circuito tem mais de dois nós: [p=0.1] aí, volte às malhas."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Esquerda: gerador de dez volts e resistor de três ohms. [p=0.1] {b}Direita: gerador de oito volts e resistor de dois ohms. [p=0.1] {c}Meio: um ohm. [p=0.2] {d}Os dois geradores têm o positivo para o nó de cima. [p=0.3] {e}Monte o sistema e ache as três correntes."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Nó em A: i três igual a i um mais i dois. [p=0.2] {b}Malha da esquerda: dez igual a três vezes i um, mais i três. [p=0.1] {c}Da direita: oito igual a dois vezes i dois, mais i três. [p=0.3] {d}Trocando i três: dez igual a quatro vezes i um, mais i dois, [p=0.1] {e}e oito igual a i um, mais três vezes i dois."),
    dict(id="s19", block="resposta", text="{a}Da primeira: i dois igual a dez menos quatro i um. [p=0.2] {b}Na segunda: oito igual a i um, mais trinta, menos doze i um. [p=0.2] {c}Onze i um igual a vinte e dois: [p=0.1] {d}i um vale dois ampères. [p=0.2] {e}i dois é dez menos oito, dois ampères, [p=0.1] {f}e i três, quatro."),
    dict(id="s20", block="resposta", text="{a}Confira pelo atalho: [p=0.1] dez menos u, sobre três, mais oito menos u, sobre dois, igual a u. [p=0.3] {b}Multiplique tudo por seis: [p=0.1] quarenta e quatro igual a onze u, [p=0.1] {c}e u vale quatro volts. [p=0.2] {d}No meio, quatro dividido por um: quatro ampères. [p=0.1] Confere."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}corrente com nome e sentido em cada ramo, [p=0.1] {b}um nó, [p=0.1] {c}duas malhas [p=0.1] {d}e o sistema por substituição. [p=0.3] {e}Com só dois nós, a tensão entre eles resolve tudo numa equação."),
    dict(id="s22", block="fim", text="Na próxima aula, {a}você vai praticar com circuitos que não se reduzem a um resistor só. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
