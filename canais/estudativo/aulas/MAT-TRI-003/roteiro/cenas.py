# Estudativo · MAT-TRI-003 — Ângulos notáveis: 30°, 45° e 60° (Matemática · Trigonometria).
# Habilidade: montar a tabela de cabeça com um macete, deduzi-la do quadrado e do triângulo equilátero e dizer que tg 30° = √3/3.
# Pré-requisitos: MAT-TRI-001 (seno, cosseno, tangente; tangente = seno ÷ cosseno), MAT-ANG-017 (diagonal ℓ√2, altura ℓ√3/2), MAT-FAT-005 (racionalizar 1/√2 = √2/2). Próxima: MAT-TRI-004.
# Questão inédita, criada para esta aula. Seno, cosseno e tangente narrados por extenso. Aproximações das aulas anteriores: √2 ≈ 1,4 e √3 ≈ 1,7.
# MAT-TRI-002 (achar lado) não está em "Já ensinado" desta ficha: não usado.
# Contas: quadrado de lado 1, diagonal √2 · ângulos 45° (catetos iguais, 90/2) · sen 45 = 1/√2 = √2/2 = cos 45 · tg 45 = 1.
# Equilátero de lado 2: metade com hipotenusa 2, base 1, altura √3 (4 − 1 = 3) · topo 180 − 90 − 60 = 30.
# sen 30 = 1/2 · cos 30 = √3/2 · tg 30 = 1/√3 = √3/3 ≈ 0,57 (1,7/3 = 0,566…; √3/3 = 0,577…) · sen 60 = √3/2 · cos 60 = 1/2 · tg 60 = √3.
# Erro: 30° na base → sen 30 = √3/2 (troca); regra: menor ângulo de frente para o menor lado.
# Macete: seno = √1/2, √2/2, √3/2; cosseno ao contrário; tangente = seno ÷ cosseno (os "÷ 2" se cancelam): √3/3, 1, √3.
# Questão: sen 45 · cos 45 + tg 30 · tg 60 = (√2/2)² + (√3/3)·√3 = 2/4 + 3/3 = 1/2 + 1 = 3/2 (um e meio).
# Visual (E.triangulo, E.angulo):
#   s04-s05: quadrado de lado 1 com a diagonal √2; um dos triângulos em destaque, arcos de 45° nos dois cantos.
#   s06-s10: equilátero de lado 2 com os três 60°; altura √3 com o quadradinho do reto; metade em destaque com 30° no topo e 60° na base; lado 1 e √3 rotulados.
#   s11: a metade com 30° na base em vermelho, riscada.
#   s12-s14: tabela 3 × 3 sendo montada: linha do seno √1, √2, √3 sobre 2; √1 virando 1; linha do cosseno espelhada com seta; linha da tangente.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Ângulos notáveis: 30°, 45° e 60°"

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
    dict(id="s01", block="gancho", text="{a}Seno de trinta graus: um meio. [p=0.2] {b}Cosseno de quarenta e cinco graus: raiz de dois dividido por dois. [p=0.2] {c}Tangente de sessenta graus: raiz de três. [p=0.3] Esses valores caem em prova o tempo todo, [p=0.2] e {d}dá para montar a tabela inteira de cabeça em poucos segundos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você monta essa tabela com um macete [p=0.2] e sabe {b}de onde vem cada número."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}seno, cosseno e tangente no triângulo retângulo; [p=0.2] {c}a diagonal do quadrado e a altura do triângulo equilátero; [p=0.2] e {d}tirar a raiz de baixo, como um dividido por raiz de dois virar raiz de dois dividido por dois. [p=0.3] Se faltar alguma, procure no canal."),
    # 45 graus
    dict(id="s04", block="quadrado", text="Comece pelo {a}quadrado de lado um. [p=0.2] {b}A diagonal mede raiz de dois [p=0.2] e corta o quadrado em {c}dois triângulos retângulos. [p=0.3] Cada um tem os catetos iguais, então {d}os ângulos agudos também são iguais. [p=0.2] Juntos, eles somam noventa, porque o triângulo soma cento e oitenta: [p=0.2] {e}noventa dividido por dois dá quarenta e cinco graus."),
    dict(id="s05", block="quadrado", text="Para quarenta e cinco graus: {a}oposto um, adjacente um, hipotenusa raiz de dois. [p=0.2] {b}Seno: um dividido por raiz de dois. [p=0.2] Tirando a raiz de baixo, {c}raiz de dois dividido por dois. [p=0.2] {d}O cosseno é igual, porque os catetos são iguais. [p=0.2] {e}A tangente é um dividido por um, que dá um."),
    # 30 e 60 graus
    dict(id="s06", block="equilatero", text="Agora, o {a}triângulo equilátero de lado dois, com os três ângulos de sessenta graus. [p=0.2] {b}A altura parte o triângulo em duas metades. [p=0.2] Cada metade tem {c}hipotenusa dois, [p=0.2] {d}base um [p=0.2] e {e}altura raiz de três: por Pitágoras, dois ao quadrado menos um ao quadrado dá três, e a altura é a raiz disso."),
    dict(id="s07", block="equilatero", text="Os ângulos da metade: {a}embaixo, o sessenta continua. [p=0.2] {b}No topo, cento e oitenta menos noventa menos sessenta dá trinta. [p=0.3] {c}O trinta fica de frente para o lado um. [p=0.2] {d}O sessenta fica de frente para raiz de três."),
    dict(id="s08", block="equilatero", text="{a}Seno de trinta: oposto um, hipotenusa dois, que dá um meio. [p=0.2] {b}Cosseno de trinta: adjacente raiz de três, hipotenusa dois, que dá raiz de três dividido por dois. [p=0.2] {c}Tangente de trinta: oposto um, adjacente raiz de três, que dá um dividido por raiz de três."),
    dict(id="s09", block="equilatero", text="Tire a raiz de baixo: {a}multiplique em cima e embaixo por raiz de três. [p=0.2] Em cima, {b}fica raiz de três. [p=0.2] Embaixo, {c}raiz de três vezes raiz de três dá três. [p=0.2] {d}A tangente de trinta dá raiz de três dividido por três. [p=0.2] Com raiz de três perto de um vírgula sete, {e}dá cerca de zero vírgula cinquenta e sete."),
    dict(id="s10", block="equilatero", text="Para sessenta graus, {a}os catetos trocam de papel. [p=0.2] {b}O seno de sessenta dá raiz de três dividido por dois. [p=0.2] {c}O cosseno de sessenta dá um meio. [p=0.2] {d}A tangente de sessenta é raiz de três dividido por um, que dá raiz de três."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}trocar o trinta com o sessenta na metade do equilátero. [p=0.2] Quem põe o trinta embaixo acha {b}seno de trinta igual a raiz de três dividido por dois. [p=0.3] Confira com uma regra simples: [p=0.2] {c}o menor ângulo fica de frente para o menor lado. [p=0.2] {d}O trinta fica de frente para o um, e o seno de trinta dá um meio."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o macete da tabela. [p=0.2] Escreva {a}os três ângulos em ordem. [p=0.2] Na linha do seno: {b}raiz de um, [p=0.2] raiz de dois [p=0.2] e raiz de três, [p=0.2] tudo dividido por dois. [p=0.3] {c}Raiz de um é um, então o seno de trinta dá um meio."),
    dict(id="s13", block="atalho", text="{a}O cosseno é a mesma linha, de trás para a frente. [p=0.3] E a tangente é {b}o seno dividido pelo cosseno: [p=0.2] o dividido por dois de cima e o de baixo se cancelam. [p=0.2] Em trinta graus, sobra um dividido por raiz de três, {c}que vira raiz de três dividido por três. [p=0.2] Em quarenta e cinco, um. [p=0.2] Em sessenta, raiz de três."),
    dict(id="s14", block="atalho", text="Funciona porque {a}trinta e sessenta somam noventa: [p=0.2] o cateto de frente para um desses ângulos encosta no outro. [p=0.2] Por isso o cosseno é {b}o seno ao contrário. [p=0.3] E a linha do seno é só um jeito de lembrar os valores que você calculou no quadrado e no equilátero. [p=0.3] {c}O macete só vale para esses três ângulos. [p=0.2] Para trinta e sete graus, por exemplo, {d}a prova precisa dar o valor."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar, {a}sem olhar a tabela. [p=0.2] Calcule {b}seno de quarenta e cinco vezes cosseno de quarenta e cinco, [p=0.2] {c}mais tangente de trinta vezes tangente de sessenta."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Raiz de dois dividido por dois, vezes ele mesmo. [p=0.2] Em cima, {b}raiz de dois vezes raiz de dois dá dois. [p=0.2] Embaixo, {c}dois vezes dois dá quatro. [p=0.2] {d}Dois quartos, que dá um meio."),
    dict(id="s18", block="resposta", text="{a}Raiz de três dividido por três, vezes raiz de três. [p=0.2] Em cima, {b}raiz de três vezes raiz de três dá três. [p=0.2] {c}Três dividido por três dá um. [p=0.3] {d}Um meio mais um dá um e meio."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o seno sobe com raiz de um, de dois e de três, dividido por dois. [p=0.2] {b}O cosseno é a mesma linha, ao contrário. [p=0.2] {c}A tangente é o seno dividido pelo cosseno."),
    dict(id="s20", block="fim", text="Na próxima aula, a tabela vai para a rua: [p=0.2] você acha {a}a altura de uma torre vista a trinta metros, sob um ângulo de sessenta graus, [p=0.2] e {b}a inclinação de uma rampa. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
