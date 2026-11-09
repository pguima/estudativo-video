# Estudativo · FIS-ELE-015 — Medidores e ponte de Wheatstone (Física · Eletricidade · Corrente, Ohm e circuitos).
# Habilidade: dizer como ligar amperímetro e voltímetro e achar um resistor na ponte com o produto cruzado.
# Pré-requisitos: FIS-ELE-013 (associação mista). Próxima: FIS-ELE-016.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# FIS-ELE-014 (curto-circuito) NÃO está em "Já ensinado": o amperímetro em paralelo é explicado só com o paralelo
#   (caminho de resistência zero leva quase toda a corrente). A regra da ponte sai do divisor de tensão da série (FIS-ELE-011).
# Ponte: lado esquerdo R1 (em cima) e R2 (embaixo); lado direito R3 (em cima) e R4 (embaixo). Opostos: R1 com R4, R2 com R3.
#   Equilíbrio: R1/R2 = R3/R4 → R1·R4 = R2·R3.
# Contas: 2·R4 = 8·3 = 24 → R4 = 12 Ω; atalho: 2 + 8 = 10, 3 + 12 = 15, 10·15/25 = 150/25 = 6 Ω.
#   Medidores: 12/(2 + 4) = 2 A; 4·2 = 8 V. Questão: 3·R4 = 9·6 = 54 → R4 = 18 Ω; 3/9 = 6/18 = 1/3.

TITULO = "Medidores e ponte de Wheatstone"

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
    dict(id="s01", block="gancho", text="{a}Ligue um amperímetro do jeito errado [p=0.2] e {b}ele pode queimar na hora. [p=0.3] {c}Ligue um voltímetro do jeito errado [p=0.1] e {d}o circuito para de funcionar."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber ligar os dois medidores, [p=0.2] e {b}achar um resistor desconhecido com uma multiplicação cruzada."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}em série, a corrente é a mesma, e a tensão se divide na proporção das resistências; [p=0.2] e {c}em paralelo, a tensão é a mesma, e a menor resistência leva a maior corrente. [p=0.3] Se faltar alguma, procure no canal."),
    # medidores
    dict(id="s04", block="medidores", text="{a}O amperímetro mede a corrente. [p=0.2] {b}Para medir a corrente de um resistor, ela precisa passar por dentro do aparelho: [p=0.2] {c}então, ele entra em série, [p=0.1] no mesmo fio do resistor. [p=0.3] {d}O ideal é que tenha resistência zero, [p=0.2] para não mudar a corrente que mede."),
    dict(id="s05", block="medidores", text="{a}O voltímetro mede a tensão entre dois pontos. [p=0.2] {b}Então, ele entra em paralelo, [p=0.1] com uma ponta de cada lado do resistor, [p=0.2] e {c}fica com a mesma tensão dele. [p=0.3] {d}O ideal é ter resistência enorme, [p=0.2] para quase nenhuma corrente desviar por ele."),
    dict(id="s06", block="medidores", text="Para não esquecer: {a}o amperímetro fica no caminho da corrente, como uma catraca; [p=0.3] {b}o voltímetro fica por fora, como uma régua, com uma ponta em cada lado. [p=0.3] {c}Com doze volts, dois ohms e quatro ohms em série: [p=0.2] {d}o amperímetro, em qualquer ponto do fio, marca dois ampères; [p=0.2] {e}o voltímetro, nas pontas do de quatro, marca oito volts."),
    # erro
    dict(id="s07", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}trocar as ligações. [p=0.3] {b}Amperímetro em paralelo é um caminho de resistência zero ao lado do resistor: [p=0.2] {c}quase toda a corrente desvia por ele, [p=0.1] a corrente fica enorme, e {d}o aparelho pode queimar."),
    dict(id="s08", block="erro", text="{a}Voltímetro em série põe uma resistência enorme no caminho: [p=0.2] {b}a corrente quase zera, e o circuito para de funcionar."),
    # ponte
    dict(id="s09", block="ponte", text="Agora, a ponte de Wheatstone. [p=0.2] São {a}quatro resistores num losango, [p=0.2] ligados à pilha {b}pelo ponto de cima e pelo de baixo. [p=0.3] {c}À esquerda, erre um em cima e erre dois embaixo; [p=0.2] {d}à direita, erre três em cima e erre quatro embaixo. [p=0.3] {e}No meio, de um lado ao outro, fica um amperímetro bem sensível, o galvanômetro."),
    dict(id="s10", block="ponte", text="Quando {a}o galvanômetro marca zero, [p=0.1] a ponte está {b}em equilíbrio. [p=0.3] E vale a regra: [p=0.2] {c}o produto dos resistores opostos, na diagonal, é igual. [p=0.2] {d}Erre um vezes erre quatro é igual a erre dois vezes erre três."),
    dict(id="s11", block="ponte", text="Por quê? [p=0.2] {a}Sem corrente no meio, cada lado do losango é uma série simples, com a tensão da pilha. [p=0.3] {b}E, para não passar corrente pelo galvanômetro, não pode haver tensão entre as pontas dele. [p=0.2] {c}Então, a tensão se divide na mesma proporção dos dois lados: [p=0.2] {d}erre um está para erre dois, assim como erre três está para erre quatro. [p=0.2] {e}Multiplicando em cruz, sai a regra."),
    dict(id="s12", block="ponte", text="Exemplo. [p=0.2] Com a ponte em equilíbrio, {a}erre um vale dois ohms, [p=0.1] {b}erre dois, oito, [p=0.1] {c}erre três, três, [p=0.2] e {d}erre quatro é o desconhecido. [p=0.3] {e}Dois vezes erre quatro igual a oito vezes três, vinte e quatro. [p=0.2] {f}Erre quatro vale doze ohms."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho: [p=0.2] {a}ponte em equilíbrio, apague o que está no meio. [p=0.3] {b}Se não passa corrente por ali, tanto faz ter um galvanômetro, um resistor ou nada. [p=0.3] {c}Sobram os dois lados em série, ligados em paralelo. [p=0.2] {d}Dois mais oito, dez; [p=0.1] três mais doze, quinze. [p=0.2] {e}Produto pela soma: cento e cinquenta dividido por vinte e cinco, seis ohms."),
    dict(id="s14", block="atalho", text="{a}Antes de apagar, confira o produto cruzado. [p=0.2] {b}Se ele não fechar, passa corrente no meio, [p=0.1] e o meio não pode sair."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Numa ponte em equilíbrio, {a}erre um vale três ohms, [p=0.1] {b}erre dois, nove ohms, [p=0.1] {c}e erre três, seis ohms. [p=0.3] {d}Quanto vale erre quatro?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Os opostos são erre um com erre quatro, e erre dois com erre três. [p=0.2] {b}Três vezes erre quatro igual a nove vezes seis, [p=0.1] cinquenta e quatro. [p=0.2] {c}Erre quatro vale dezoito ohms. [p=0.3] {d}Confira pela proporção: três está para nove assim como seis está para dezoito. [p=0.2] {e}Um terço, dos dois lados."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}amperímetro em série, com resistência quase zero; [p=0.2] {b}voltímetro em paralelo, com resistência enorme; [p=0.2] e {c}ponte em equilíbrio: produto dos opostos igual, e o meio pode ser apagado."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai {a}praticar o módulo inteiro: [p=0.2] {b}fio, série, paralelo, circuito misto, curto e medidores. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
