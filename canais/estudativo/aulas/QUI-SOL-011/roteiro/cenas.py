# Estudativo · QUI-SOL-011 — Praticando: propriedades coligativas (Química · Soluções · Propriedades coligativas).
# Habilidade: comparar soluções e explicar fenômenos do dia a dia com os efeitos coligativos.
# Pré-requisitos: QUI-SOL-008, QUI-SOL-009, QUI-SOL-010. Próxima: nenhuma (última aula da trilha).
# Aula de prática: cinco questões inéditas, criadas para esta aula, cada uma com pausa e resolução.
# Q1: montanha e panela de pressão = pressão externa (não coligativo); sal no macarrão = ebulioscopia (coligativo, < 0,5 °C).
# Q2: sacarose 0,2 × 1 = 0,2; KCl 0,1 × 2 = 0,2; MgCl₂ 0,1 × 3 = 0,3 → MgCl₂ ferve mais quente; sacarose e KCl empatam.
# Q3: uva-passa (muito açúcar dentro) em água pura incha: a água entra; náufrago que bebe água do mar: o sangue fica mais
# concentrado que as células, a água sai delas e a sede piora.
# Q5: lado A NaCl 0,1 mol/L = 0,2 de partículas; lado B glicose 0,15 = 0,15 → a água vai de B para A (erro: comparar 0,1 com 0,15).
# Q4: estrada com neve: crioscopia; por mol, CaCl₂ (3 partículas) rende mais que NaCl (2): 1 mol de CaCl₂ solta 3 mol de partículas.
# Alface temperada murcha: osmose (a água sai das folhas para o tempero salgado).

TITULO = "Praticando: propriedades coligativas"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões, cinco situações do dia a dia: [p=0.2] {b}a cozinha, a lista de soluções, a uva-passa, a estrada com neve [p=0.1] e uma membrana. [p=0.3] {c}Pause em cada uma, tente, e confira comigo."),
    # lembrete
    dict(id="s02", block="lembrete", text="Suas ferramentas. [p=0.2] {a}O soluto faz a solução {b}ferver mais quente [p=0.1] {c}e congelar mais frio. [p=0.3] {d}Esses efeitos são coligativos: dependem só de quantas partículas há."),
    dict(id="s03", block="lembrete", text="{a}Para comparar, multiplique a concentração pelo número de partículas de cada fórmula. [p=0.3] {b}E, na osmose, a água corre atrás do soluto, [p=0.1] {c}do lado menos concentrado para o mais concentrado."),
    # questão 1
    dict(id="s04", block="q1", text="Questão um. [p=0.2] Três situações na cozinha. [p=0.2] {a}Um: na serra, o feijão demora mais para cozinhar. [p=0.2] {b}Dois: na panela de pressão, ele cozinha mais rápido. [p=0.2] {c}Três: a água do macarrão, com sal, ferve um pouco acima de cem graus. [p=0.3] {d}Em quais delas o efeito é coligativo?"),
    dict(id="s05", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s06", block="r1", text="Pergunte: o que mudou? [p=0.2] {a}Na serra, a pressão do ar é menor: [p=0.1] a água ferve abaixo de cem, e não é coligativo. [p=0.3] {b}Na panela, a pressão é maior: [p=0.1] a água ferve acima de cem, e também não é coligativo. [p=0.3] {c}Só a situação três é coligativa: [p=0.1] mudou o que está dissolvido."),
    dict(id="s07", block="r1", text="{a}E repare: o sal sobe a fervura em menos de meio grau. [p=0.2] {b}Não é ele que faz o macarrão cozinhar mais rápido."),
    # questão 2
    dict(id="s08", block="q2", text="Questão dois. [p=0.2] {a}Três soluções. [p=0.1] {b}A: sacarose, o açúcar comum, com zero vírgula dois mol por litro. [p=0.2] {c}B: cloreto de potássio, com zero vírgula um. [p=0.2] {d}C: cloreto de magnésio, também com zero vírgula um. [p=0.3] {e}Qual ferve mais quente? [p=0.1] {f}E há alguma que empata?"),
    dict(id="s09", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="r2", text="Conte as partículas. [p=0.2] {a}A sacarose não se separa: zero vírgula dois vezes um dá zero vírgula dois. [p=0.3] {b}O cloreto de potássio vira potássio e cloreto: zero vírgula um vezes dois dá zero vírgula dois. [p=0.3] {c}O cloreto de magnésio vira um magnésio e dois cloretos: zero vírgula um vezes três dá zero vírgula três."),
    dict(id="s11", block="r2", text="{a}O cloreto de magnésio tem mais partículas: ferve mais quente. [p=0.3] {b}A sacarose e o cloreto de potássio empatam, [p=0.1] {c}mesmo com concentrações diferentes."),
    # questão 3
    dict(id="s12", block="q3", text="Questão três. [p=0.2] {a}Uma uva-passa, cheia de açúcar por dentro, fica de molho em água pura. [p=0.3] {b}E um náufrago, sem água doce, bebe água do mar. [p=0.3] {c}O que acontece com a uva-passa? [p=0.2] {d}E com as células do náufrago?"),
    dict(id="s13", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="r3", text="{a}Dentro da uva-passa, a concentração é maior que na água pura. [p=0.2] {b}A água corre atrás do soluto: [p=0.1] {c}entra na uva, e ela incha."),
    dict(id="s15", block="r3", text="{a}Com o náufrago, é o contrário. [p=0.2] {b}A água do mar deixa o sangue mais concentrado que as células. [p=0.3] {c}A água sai das células, [p=0.1] {d}e a sede piora. [p=0.2] {e}Por isso beber água do mar desidrata."),
    # questão 4
    dict(id="s16", block="q4", text="Questão quatro. [p=0.2] {a}Em cidades com neve, as estradas recebem sal de cozinha ou cloreto de cálcio. [p=0.3] {b}Qual efeito explica o gelo derreter? [p=0.2] {c}E por que, mol por mol, o cloreto de cálcio funciona melhor que o sal de cozinha?"),
    dict(id="s17", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="r4", text="{a}O sal faz a água congelar abaixo de zero: é a crioscopia. [p=0.3] {b}Com o ponto de congelamento mais baixo, o gelo derrete mesmo no frio. [p=0.3] {c}O sal de cozinha solta duas partículas, sódio e cloreto. [p=0.2] {d}O cloreto de cálcio solta três: um cálcio e dois cloretos. [p=0.3] {e}Mais partículas por mol, maior o efeito."),
    # questão 5
    dict(id="s19", block="q5", text="Questão cinco. [p=0.2] {a}Uma membrana semipermeável separa duas soluções. [p=0.2] {b}No lado A, sal de cozinha, com zero vírgula um mol por litro. [p=0.2] {c}No lado B, glicose, com zero vírgula quinze. [p=0.3] {d}Para que lado vai a água?"),
    dict(id="s20", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="r5", text="Conte as partículas. [p=0.2] {a}O sal vira sódio e cloreto: zero vírgula um vezes dois dá zero vírgula dois. [p=0.3] {b}A glicose não se separa: fica em zero vírgula quinze. [p=0.3] {c}O lado A tem mais partículas: [p=0.1] {d}a água vai de B para A."),
    dict(id="s22", block="r5", text="{a}Quem comparou só zero vírgula um com zero vírgula quinze [p=0.1] {b}mandou a água para o lado errado."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo o módulo: [p=0.1] {a}pergunte o que mudou, a pressão ou a solução; [p=0.2] {b}conte as partículas para comparar; [p=0.1] e {c}na osmose, a água corre atrás do soluto."),
    dict(id="s24", block="fim", text="Com isso, você fechou a trilha de soluções: [p=0.2] {a}da mistura no copo até a água atravessando a membrana. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
