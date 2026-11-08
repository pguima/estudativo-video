# Estudativo · MAT-TRI-005 — Dois ângulos de visão (Matemática · Trigonometria).
# Habilidade: achar a altura de um morro medido de dois pontos, com ângulos de 30° e 60° a 100 m um do outro, montando um sistema.
# Pré-requisitos: MAT-TRI-004 (altura com tangente; ângulo de elevação), MAT-EQU-018 (sistema por substituição). Usa a tabela de MAT-TRI-003, o atalho "oposto = hipotenusa × seno" de MAT-TRI-002 e o ângulo externo e o isósceles de MAT-ANG-004 e MAT-ANG-005. Próxima: MAT-TRI-006.
# Questão inédita, criada para esta aula. Seno, cosseno e tangente narrados por extenso. Pontos narrados "á" e "bê"; altura "agá". √3 ≈ 1,7.

TITULO = "Dois ângulos de visão"

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
    dict(id="s01", block="gancho", text="{a}Um morro. [p=0.2] Você não consegue medir {b}a distância até o ponto bem embaixo do topo: [p=0.2] ele fica dentro do morro. [p=0.3] Mas dá para ver o topo de dois lugares. [p=0.2] {c}Daqui, sob trinta graus. [p=0.2] {d}Cem metros mais perto, sob sessenta graus. [p=0.3] Só com isso, {e}você acha a altura."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve esse tipo de problema com um sistema [p=0.2] e leva um {b}atalho que dispensa o sistema."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}achar uma altura com a tangente, sabendo que tangente de trinta graus é raiz de três dividido por três [p=0.2] e tangente de sessenta é raiz de três; [p=0.2] e {c}resolver sistema por substituição: isolar uma letra e trocar na outra equação. [p=0.3] Se faltar alguma, procure no canal."),
    # desenho
    dict(id="s04", block="desenho", text="Desenhe. [p=0.2] {a}Do topo, desça a altura até o chão. [p=0.2] {b}No ponto á, você viu o topo sob trinta graus. [p=0.2] {c}No ponto bê, cem metros mais perto, sob sessenta graus. [p=0.3] São {d}dois triângulos retângulos com a mesma altura."),
    dict(id="s05", block="desenho", text="Você não sabe {a}duas coisas: [p=0.2] {b}a altura, agá, [p=0.2] e {c}a distância de bê até o pé da altura, xis. [p=0.2] Do ponto á, a distância é {d}xis mais cem. [p=0.3] Duas letras pedem {e}duas equações."),
    # equações
    dict(id="s06", block="sistema", text="{a}Triângulo do ponto bê: oposto agá, adjacente xis. [p=0.2] Tangente de sessenta: {b}raiz de três igual a agá dividido por xis. [p=0.2] Isolando: {c}agá igual a xis raiz de três."),
    dict(id="s07", block="sistema", text="{a}Triângulo do ponto á: oposto agá, adjacente xis mais cem. [p=0.2] Tangente de trinta: {b}raiz de três dividido por três igual a agá dividido por, abre parênteses, xis mais cem, fecha parênteses. [p=0.2] Isolando: {c}agá igual a, abre parênteses, xis mais cem, fecha parênteses, vezes raiz de três, dividido por três."),
    dict(id="s08", block="sistema", text="Esse é o sistema. [p=0.2] {a}Substituição: troque o agá da segunda equação por xis raiz de três. [p=0.3] {b}A raiz de três aparece de cada lado: divida tudo por ela. [p=0.2] Sobra {c}xis igual a, abre parênteses, xis mais cem, fecha parênteses, dividido por três."),
    dict(id="s09", block="sistema", text="{a}Multiplique cada lado por três: três xis igual a xis mais cem. [p=0.2] {b}Tire xis de cada lado: dois xis igual a cem. [p=0.2] {c}Xis igual a cinquenta metros."),
    dict(id="s10", block="sistema", text="Volte na primeira equação: {a}agá igual a cinquenta raiz de três. [p=0.2] {b}Cinquenta vezes um vírgula sete dá oitenta e cinco. [p=0.2] {c}O morro tem pouco mais de oitenta e cinco metros."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}usar os cem metros como a distância até o morro. [p=0.2] A pessoa faz {b}cem vezes tangente de trinta: cem raiz de três dividido por três, [p=0.2] {c}cerca de cinquenta e sete metros."),
    dict(id="s12", block="erro", text="Mas os cem metros são {a}só o caminho de á até bê. [p=0.2] {b}Do ponto á até o pé da altura, a distância é xis mais cem, [p=0.2] e o xis você ainda não sabe. [p=0.3] Por isso {c}precisa das duas equações."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para trinta e sessenta graus. [p=0.2] Olhe {a}o triângulo de á, bê e o topo. [p=0.2] {b}O ângulo de sessenta, em bê, é externo a esse triângulo. [p=0.2] Ele vale {c}a soma dos internos de longe: trinta mais o ângulo do topo. [p=0.2] {d}Então o ângulo do topo mede trinta graus."),
    dict(id="s14", block="atalho", text="{a}Dois ângulos de trinta: o triângulo é isósceles. [p=0.2] {b}A distância de bê até o topo é igual à de á até bê: cem metros. [p=0.3] No triângulo do ponto bê, {c}cem é a hipotenusa, e a altura é o oposto. [p=0.2] {d}Cem vezes seno de sessenta: cem vezes raiz de três dividido por dois dá cinquenta raiz de três. [p=0.2] O mesmo, sem sistema."),
    dict(id="s15", block="atalho", text="Funciona porque {a}sessenta é o dobro de trinta: [p=0.2] o ângulo do topo sai igual ao ângulo em á. [p=0.3] {b}Não compensa com outros ângulos, como trinta graus e quarenta e cinco graus. [p=0.2] Aí o triângulo não é isósceles, e {c}o sistema é o caminho."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Do ponto á, você vê o topo de um prédio sob trinta graus. [p=0.2] {b}Anda oitenta metros em direção ao prédio, até o ponto bê, [p=0.2] e vê o topo sob {c}sessenta graus. [p=0.3] {d}Qual a altura do prédio? [p=0.2] {e}E a que distância bê está do prédio? [p=0.2] Use raiz de três perto de um vírgula sete."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Do ponto bê: {a}agá igual a xis raiz de três. [p=0.2] Do ponto á: {b}agá igual a, abre parênteses, xis mais oitenta, fecha parênteses, vezes raiz de três, dividido por três. [p=0.3] {c}Substitua e divida por raiz de três: três xis igual a xis mais oitenta. [p=0.2] {d}Dois xis igual a oitenta: xis igual a quarenta metros."),
    dict(id="s19", block="resposta", text="{a}Agá igual a quarenta raiz de três. [p=0.2] {b}Quarenta vezes um vírgula sete dá sessenta e oito: o prédio tem pouco mais de sessenta e oito metros. [p=0.3] Pelo atalho: {c}de bê até o topo são oitenta metros, [p=0.2] e {d}oitenta vezes raiz de três dividido por dois dá quarenta raiz de três. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}uma letra para a altura, outra para a distância que falta, [p=0.2] {b}uma equação de cada ponto [p=0.2] e {c}substituição."),
    dict(id="s21", block="fim", text="Na próxima aula, você pratica {a}problemas de altura, rampa e distância, [p=0.2] {b}com e sem ângulo da tabela, [p=0.2] escolhendo a razão certa em cada um. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
