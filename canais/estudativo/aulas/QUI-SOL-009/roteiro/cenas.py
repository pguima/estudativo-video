# Estudativo · QUI-SOL-009 — Congelar mais tarde: contar as partículas (Química · Soluções · Propriedades coligativas).
# Habilidade: explicar o anticongelante e ordenar soluções de açúcar, NaCl e CaCl₂ de mesma concentração em mol/L pelo número
# de partículas.
# Pré-requisitos: QUI-SOL-008, QUI-SOL-004, QUI-INO-003. Próxima: QUI-SOL-010 (osmose e pressão osmótica).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Fatos: crioscopia = abaixamento do ponto de congelamento. Anticongelante do radiador = etilenoglicol (meio a meio com água,
# congela perto de −35 °C e ferve acima de 100 °C). Sal (NaCl) derrete gelo de estrada até cerca de −20 °C.
# Partículas por fórmula: sacarose 1; NaCl → Na⁺ + Cl⁻ = 2; CaCl₂ → Ca²⁺ + 2 Cl⁻ = 3 (na prova conta-se o número cheio; na
# realidade o efeito do CaCl₂ fica um pouco abaixo de 3 vezes). 0,1 mol/L: 0,1; 0,2; 0,3 mol/L de partículas.
# Atalho: 0,3 mol/L de açúcar × 1 = 0,3 = 0,1 mol/L de CaCl₂ × 3 (empate).
# Questão: glicose 0,25 × 1 = 0,25; NaCl 0,1 × 2 = 0,2; CaCl₂ 0,1 × 3 = 0,3. Congela primeiro (mais quente) B, depois A, por último C.

TITULO = "Congelar mais tarde: contar as partículas"

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
    dict(id="s01", block="gancho", text="{a}Três copos com a mesma concentração: [p=0.1] {b}zero vírgula um mol por litro. [p=0.3] {c}Um de açúcar, um de sal de cozinha, um de cloreto de cálcio. [p=0.3] {d}No congelador, o de açúcar congela primeiro. [p=0.2] {e}O de cloreto de cálcio, por último. [p=0.3] {f}Mesma concentração, efeitos diferentes. Por quê?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}explicar o anticongelante [p=0.2] e {c}contar partículas para pôr qualquer lista de soluções em ordem."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}o soluto baixa a pressão de vapor e faz a solução ferver mais quente. [p=0.3] {b}Esse efeito depende de quantas partículas há, não de qual soluto é: é coligativo. [p=0.3] E {c}na água, um sal se separa em íons: {d}o sal de cozinha vira sódio e cloreto."),
    # crioscopia
    dict(id="s04", block="congelar", text="{a}Para congelar, as partículas de água precisam se arrumar em fileiras, formando o gelo. [p=0.3] {b}As partículas de soluto ficam no meio do caminho [p=0.1] {c}e atrapalham a arrumação. [p=0.3] {d}É preciso esfriar mais para o gelo se formar."),
    dict(id="s05", block="congelar", text="{a}Então a solução congela abaixo de zero grau. [p=0.3] {b}A descida do ponto de congelamento se chama crioscopia. [p=0.3] {c}Ela também é coligativa: [p=0.1] quanto mais partículas, mais frio é preciso."),
    # anticongelante
    dict(id="s06", block="anti", text="{a}O anticongelante do radiador usa isso. [p=0.2] {b}Misturado meio a meio com a água, ele faz a mistura congelar só perto de trinta e cinco graus abaixo de zero. [p=0.3] {c}E, de quebra, ela ferve acima de cem graus. [p=0.3] {d}O motor fica protegido no frio e no calor."),
    dict(id="s07", block="anti", text="{a}Nos países com neve, joga-se sal na estrada pelo mesmo motivo: [p=0.2] {b}a água salgada só congela bem abaixo de zero, [p=0.1] {c}e o gelo derrete."),
    # contar partículas
    dict(id="s08", block="contar", text="Agora, o segredo da prova: [p=0.2] {a}contar as partículas. [p=0.3] {b}O açúcar se dissolve inteiro: [p=0.1] {c}cada molécula de açúcar continua inteira, uma partícula só. [p=0.3] {d}Zero vírgula um mol por litro de açúcar dá zero vírgula um mol por litro de partículas."),
    dict(id="s09", block="contar", text="{a}O sal de cozinha se separa em dois íons: [p=0.1] {b}um sódio e um cloreto. [p=0.3] {c}Zero vírgula um mol por litro de sal dá zero vírgula dois mol por litro de partículas."),
    dict(id="s10", block="contar", text="{a}O cloreto de cálcio se separa em três: [p=0.1] {b}um cálcio e dois cloretos. [p=0.3] {c}Zero vírgula um mol por litro dá zero vírgula três mol por litro de partículas."),
    dict(id="s11", block="contar", text="{a}Mais partículas, maior o efeito: [p=0.2] {b}o cloreto de cálcio congela numa temperatura mais baixa e ferve mais quente. [p=0.3] {c}O açúcar tem o menor efeito: [p=0.1] {d}congela primeiro."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum: [p=0.2] {a}achar que a mesma concentração dá o mesmo efeito. [p=0.3] {b}A pessoa vê zero vírgula um nos três copos e diz que eles congelam juntos. [p=0.3] {c}Mas a concentração conta as unidades de soluto, [p=0.1] {d}e o que decide é o número de partículas soltas na água."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.2] {a}multiplique a concentração pelo número de partículas de cada fórmula. [p=0.3] {b}O maior resultado tem o maior efeito: [p=0.1] {c}congela mais frio, ferve mais quente. [p=0.3] {d}Assim, zero vírgula três de açúcar [p=0.1] {e}empata com zero vírgula um de cloreto de cálcio: [p=0.1] {f}e ambos dão zero vírgula três."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o efeito coligativo só olha a quantidade de partículas. [p=0.3] {b}Não compensa com ácidos fracos, que soltam só parte dos íons: [p=0.2] aí a prova dá a fração que se separa, e isso é assunto de outra aula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Três soluções. [p=0.2] {a}A: glicose, um açúcar, com zero vírgula vinte e cinco mol por litro. [p=0.2] {b}B: sal de cozinha, com zero vírgula um. [p=0.2] {c}C: cloreto de cálcio, também com zero vírgula um. [p=0.3] {d}Ponha em ordem, da que congela primeiro para a que congela por último."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Conte as partículas. [p=0.2] {a}A glicose não se separa: zero vírgula vinte e cinco vezes um dá zero vírgula vinte e cinco. [p=0.3] {b}O sal: zero vírgula um vezes dois dá zero vírgula dois. [p=0.3] {c}O cloreto de cálcio: zero vírgula um vezes três dá zero vírgula três."),
    dict(id="s18", block="resposta", text="{a}Menos partículas, menor efeito, congela primeiro. [p=0.2] {b}A ordem é B, depois A, depois C. [p=0.3] {c}Repare: a glicose tinha a maior concentração, [p=0.1] {d}mas o sal, com menos concentração, ficou com menos partículas e congelou antes dela."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}o soluto faz a solução congelar abaixo de zero; [p=0.2] {b}multiplique a concentração pelo número de partículas, [p=0.1] e {c}o maior resultado tem o maior efeito."),
    dict(id="s20", block="fim", text="Na próxima aula, a água vai atravessar uma película: [p=0.2] {a}a osmose, [p=0.1] que explica {b}por que o sal conserva a carne [p=0.1] e {c}como se tira o sal da água do mar. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
