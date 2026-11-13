# Estudativo · QUI-INO-003 — Neutralização e sais (Química · Funções e Reações Inorgânicas · Ácidos, bases, sais e óxidos).
# Habilidade: escrever HCl + NaOH → NaCl + H₂O e dar nome a sais como cloreto, sulfato, nitrato e carbonato.
# Pré-requisitos: QUI-INO-001, QUI-INO-002. Próxima: QUI-INO-004 (óxidos ácidos, básicos e neutros).
# Balancear por tentativas é de outra aula (QUI-INO-008): aqui o coeficiente sai da conta "cada H⁺ pede um OH⁻", que a
# aula ensina. Cruzar cargas (QUI-LIG-001) e parênteses (QUI-INO-002) já foram ensinados.
# Fórmula com parênteses não é lida letra a letra: diz-se o nome e a fórmula fica na tela.
# Fatos: NaCl = sal de cozinha. CaCO₃ = calcário, mármore, casca de ovo. Mg(OH)₂ = leite de magnésia (antiácido); o ácido do
# estômago é HCl. Mg(OH)₂ + 2 HCl → MgCl₂ + 2 H₂O. H₂SO₄ + 2 NaOH → Na₂SO₄ + 2 H₂O. Al³⁺ + SO₄²⁻ → Al₂(SO₄)₃.
# Questão inédita.

TITULO = "Neutralização e sais"

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
    dict(id="s01", block="gancho", text="{a}Pegue um ácido que corrói. [p=0.2] {b}Junte uma base que também corrói, na medida certa. [p=0.3] {c}O que sobra é água com sal de cozinha. [p=0.3] {d}Onde foi parar o perigo?"),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}escrever a reação entre um ácido e uma base, [p=0.2] {b}montar a fórmula do sal [p=0.2] e {c}dar nome a ele: [p=0.1] cloreto, sulfato, nitrato ou carbonato."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre das duas aulas anteriores. [p=0.2] {a}Ácido solta agá mais na água. [p=0.2] {b}Base solta ó agá menos. [p=0.3] {c}E o ácido clorídrico, além do agá mais, solta o cloreto, cê éle menos."),
    # neutralização
    dict(id="s04", block="neutraliza", text="Agora, junte ácido e base. [p=0.2] {a}Quando um agá mais encontra um ó agá menos, [p=0.1] {b}eles se prendem [p=0.1] e {c}formam uma molécula de água. [p=0.3] {d}A carga mais e a carga menos se cancelam."),
    dict(id="s05", block="neutraliza", text="Isso é a {a}neutralização. [p=0.2] Na medida certa, {b}o ácido e a base deixam de agir, [p=0.1] e a solução fica neutra: [p=0.1] {c}nem ácida, nem básica."),
    dict(id="s06", block="neutraliza", text="Veja a reação inteira. [p=0.2] {a}Agá cê éle, [p=0.1] {b}mais ene á ó agá, [p=0.1] {c}produz ene á cê éle, [p=0.1] {d}mais agá dois ó. [p=0.3] {e}O íon agá mais e o íon ó agá menos viraram água."),
    dict(id="s07", block="neutraliza", text="{a}Sobraram o ene á mais, que veio da base, [p=0.1] {b}e o cê éle menos, que veio do ácido. [p=0.3] Juntos, eles formam {c}o cloreto de sódio, o sal de cozinha."),
    # sal
    dict(id="s08", block="sal", text="Esta é a regra: [p=0.2] {a}ácido mais base produz sal mais água. [p=0.3] E {b}sal é o composto iônico em que o íon positivo vem da base [p=0.1] {c}e o íon negativo vem do ácido."),
    dict(id="s09", block="sal", text="E com o ácido sulfúrico? [p=0.2] {a}Ele solta dois agá mais [p=0.1] e o íon {b}sulfato, ésse ó quatro, com duas cargas negativas. [p=0.3] {c}O sódio tem uma carga positiva só. [p=0.2] {d}Para zerar as cargas, são dois sódios para um sulfato: [p=0.1] {e}ene á dois ésse ó quatro."),
    dict(id="s10", block="sal", text="{a}E dois agá mais pedem dois ó agá menos. [p=0.2] Por isso, {b}entram dois ene á ó agá [p=0.1] {c}e saem duas águas. [p=0.3] {d}Cada agá mais que o ácido solta faz uma água."),
    # nomes
    dict(id="s11", block="nomes", text="O nome do sal vem do nome do ácido, com a terminação trocada. [p=0.2] {a}Ídrico vira eto: [p=0.1] clorídrico dá cloreto. [p=0.3] {b}Ico vira ato: [p=0.1] {c}sulfúrico dá sulfato, [p=0.1] {d}nítrico dá nitrato, [p=0.1] {e}carbônico dá carbonato."),
    dict(id="s12", block="nomes", text="Depois, vem {a}de, e o nome do metal. [p=0.2] {b}Ene á dois ésse ó quatro é o sulfato de sódio. [p=0.2] {c}Cá ene ó três, o nitrato de potássio. [p=0.2] {d}Cê á cê ó três, o carbonato de cálcio, [p=0.1] que forma o calcário, o mármore e a casca de ovo."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}escrever o sulfato de sódio com um sódio só: [p=0.1] {b}ene á ésse ó quatro. [p=0.3] {c}Some as cargas: mais um com menos dois dá menos um. [p=0.2] {d}Sobrou carga, então a fórmula está errada. [p=0.2] {e}Num sal, as cargas somam zero."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.2] {a}cruze as cargas. [p=0.1] A carga de um íon vira o índice do outro. [p=0.3] {b}Alumínio três mais com sulfato dois menos: [p=0.2] {c}dois alumínios e três sulfatos, [p=0.1] {d}o sulfato entre parênteses."),
    dict(id="s15", block="atalho", text="Funciona porque {a}os dois alumínios somam seis cargas positivas, [p=0.1] {b}e os três sulfatos somam seis cargas negativas. [p=0.3] {c}Só cuidado quando as cargas são iguais, como cálcio dois mais e sulfato dois menos: [p=0.2] {d}um de cada já zera. [p=0.1] {e}É cê á ésse ó quatro."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}O leite de magnésia, o hidróxido de magnésio, combate a azia. [p=0.2] {b}Ele reage com o ácido clorídrico do estômago. [p=0.3] {c}Qual é o sal que se forma, com fórmula e nome? [p=0.2] E {d}quantas moléculas de água saem?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O íon positivo vem da base: eme gê dois mais. [p=0.2] {b}O negativo vem do ácido: cê éle menos. [p=0.3] {c}Para zerar, um magnésio e dois cloretos: [p=0.1] {d}eme gê cê éle dois, o cloreto de magnésio."),
    dict(id="s19", block="resposta", text="{a}A base solta dois ó agá menos, [p=0.1] então são precisos {b}dois agá mais, [p=0.1] de duas moléculas de agá cê éle. [p=0.3] {c}Dois agá mais com dois ó agá menos: [p=0.1] {d}duas moléculas de água."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}ácido mais base dá sal mais água, [p=0.1] {b}o agá mais e o ó agá menos fazem a água, [p=0.1] e {c}o nome do sal troca ídrico por eto e ico por ato."),
    dict(id="s21", block="fim", text="Na próxima aula, você conhece os {a}óxidos: [p=0.2] {b}por que o gás carbônico deixa a água ácida e a cal deixa a água básica. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
