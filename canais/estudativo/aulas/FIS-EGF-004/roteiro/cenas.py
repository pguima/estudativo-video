# Estudativo · FIS-EGF-004 — Pressão: força por área (Física · Equilíbrio, Gravitação e Fluidos · Hidrostática).
# Habilidade: calcular p = F/A, converter Pa e atm e explicar por que a faca afiada corta melhor.
# Pré-requisitos: FIS-DIN-004 (peso e normal), MAT-MED-004 (converter área: 1 m² = 10.000 cm²). Próxima: FIS-EGF-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# 1 atm = 101.325 Pa ≈ 1 × 10⁵ Pa (o valor usado em prova). 10⁵ N em 1 m² = o peso de 10 toneladas.
# Contas: 600/2 = 300 Pa; 600/0,5 = 1.200 Pa; 600/0,002 = 300.000 Pa; 600/300 = 2 N/cm² = 20.000 Pa = 0,2 atm.

TITULO = "Pressão: força por área"

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
    dict(id="s01", block="gancho", text="{a}Uma faca cega amassa o tomate. [p=0.2] {b}Uma faca afiada corta de primeira, [p=0.1] com a mesma força da sua mão. [p=0.3] A diferença não está na força. [p=0.2] Está {c}na área onde ela se apoia."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular uma pressão, [p=0.2] {b}converter pascal em atmosfera [p=0.2] e {c}explicar a faca afiada com uma conta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}O peso: a massa vezes dez, em newtons. [p=0.2] E {c}converter área: um metro quadrado tem dez mil centímetros quadrados. [p=0.3] Se faltar alguma, procure no canal."),
    # pressão
    dict(id="s04", block="pressao", text="{a}Pressão é quanto de força cai em cada pedaço de área. [p=0.3] {b}Pê minúsculo, de pressão, igual a efe sobre á. [p=0.3] {c}Efe é a força que aperta a superfície, em ângulo reto com ela, em newtons. [p=0.2] {d}Á é a área onde ela se espalha, em metros quadrados. [p=0.3] {e}A unidade é o newton por metro quadrado, [p=0.1] que tem um nome próprio: {f}pascal."),
    dict(id="s05", block="pressao", text="{a}Uma caixa de seiscentos newtons está deitada, [p=0.1] {b}apoiada em dois metros quadrados. [p=0.2] {c}Seiscentos dividido por dois: [p=0.1] {d}trezentos pascals. [p=0.3] {e}Em pé, ela se apoia em meio metro quadrado. [p=0.2] {f}Seiscentos dividido por zero vírgula cinco: [p=0.1] {g}mil e duzentos pascals. [p=0.3] Área quatro vezes menor, {h}pressão quatro vezes maior."),
    dict(id="s06", block="pressao", text="{a}A faca é a mesma ideia. [p=0.2] {b}O fio de uma faca afiada é finíssimo: [p=0.1] a área é minúscula. [p=0.3] {c}A mesma força numa área muito menor dá uma pressão enorme, [p=0.1] {d}e a pressão enorme rompe a casca do tomate. [p=0.3] {e}Pelo mesmo motivo, o prego tem ponta, [p=0.2] e {f}o trator tem pneus largos: [p=0.1] área grande, pressão pequena, e ele não atola."),
    dict(id="s07", block="pressao", text="{a}O faquir deitado na cama de pregos usa o mesmo truque. [p=0.2] {b}Um prego sozinho furaria a pele. [p=0.3] {c}Com centenas de pregos, o peso se espalha por uma área bem maior, [p=0.2] e {d}a pressão em cada ponta fica pequena demais para furar."),
    # atmosfera
    dict(id="s08", block="atmosfera", text="{a}O ar também faz pressão. [p=0.2] {b}A camada de ar em cima de você pesa, [p=0.1] e aperta tudo. [p=0.3] {c}No nível do mar, essa pressão vale uma atmosfera, [p=0.1] {d}cerca de cem mil pascals: [p=0.1] {e}um vezes dez elevado a cinco."),
    dict(id="s09", block="atmosfera", text="{a}Cem mil pascals é muito: [p=0.2] {b}é como dez toneladas apoiadas em cada metro quadrado. [p=0.3] {c}Você não é esmagado porque o ar empurra de todos os lados, [p=0.2] e {d}o seu corpo empurra de volta, de dentro para fora."),
    dict(id="s10", block="atmosfera", text="Para converter, use {a}uma atmosfera igual a dez elevado a cinco pascals. [p=0.3] {b}Duas atmosferas: dois vezes dez elevado a cinco pascals. [p=0.2] {c}Cinquenta mil pascals: meia atmosfera. [p=0.2] {d}Para voltar de pascal para atmosfera, divida por cem mil."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar a área em centímetro quadrado. [p=0.3] {b}Seiscentos newtons sobre vinte centímetros quadrados. [p=0.2] A pessoa faz {c}seiscentos dividido por vinte, [p=0.1] e escreve {d}trinta pascals. [p=0.3] {e}Vinte centímetros quadrados são dois milésimos de metro quadrado. [p=0.2] {f}A pressão certa é trezentos mil pascals: [p=0.1] dez mil vezes mais."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.2] {a}faça a conta em newton por centímetro quadrado [p=0.1] e {b}multiplique por dez mil no final. [p=0.3] {c}Seiscentos sobre vinte: trinta newtons por centímetro quadrado. [p=0.2] {d}Vezes dez mil: trezentos mil pascals. [p=0.3] Funciona porque {e}cada metro quadrado tem dez mil centímetros quadrados."),
    dict(id="s13", block="atalho", text="{a}E para comparar, nem precisa converter: [p=0.2] {b}área dez vezes menor, pressão dez vezes maior. [p=0.3] {c}Só não pule a conversão quando a resposta tem que sair em pascal."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Uma pessoa de sessenta quilos está em pé. [p=0.2] {b}Os dois pés somam trezentos centímetros quadrados de apoio. [p=0.3] {c}Qual é a pressão nos pés, em pascal? [p=0.2] {d}E isso é quanto de uma atmosfera?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}O peso: sessenta vezes dez, seiscentos newtons. [p=0.3] {b}Seiscentos sobre trezentos: [p=0.1] {c}dois newtons por centímetro quadrado. [p=0.2] {d}Vezes dez mil: [p=0.1] {e}vinte mil pascals. [p=0.3] {f}Uma atmosfera é cem mil, [p=0.1] então isso é {g}dois décimos de atmosfera."),
    dict(id="s17", block="resposta", text="{a}E se ela ficar num pé só? [p=0.2] Metade da área, {b}o dobro da pressão: quarenta mil pascals."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}pressão é força sobre área; [p=0.2] {b}com a área em metro quadrado, a pressão sai em pascal; [p=0.2] e {c}uma atmosfera vale cerca de dez elevado a cinco pascals."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai mergulhar: [p=0.2] {a}a pressão dentro de um líquido, [p=0.1] {b}que cresce uma atmosfera a cada dez metros de água. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
