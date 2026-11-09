# Estudativo · FIS-ELE-004 — Potencial elétrico e energia (Física · Eletricidade · Eletrostática).
# Habilidade: calcular V = k·Q/d, usar U = E·d e achar o trabalho com τ = q·U.
# Pré-requisitos: FIS-ELE-003 (campo), FIS-ENE-001 (trabalho de uma força). Próxima: FIS-ELE-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Energia potencial gravitacional não está em "Já ensinado": a escada é só imagem.
# Trabalho da força elétrica de A até B: τ = q·(V_A − V_B) = q·U; positivo quando a carga positiva vai do potencial maior
# para o menor. Contas: 9e9·2e-6/3 = 6e3 V (com d² daria 2e3); 500·0,2 = 100 V; 3e-6·100 = 3e-4 J; 2000·0,05 = 100 V;
# 2e-6·100 = 2e-4 J.

TITULO = "Potencial elétrico e energia"

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
    dict(id="s01", block="gancho", text="{a}Pilha de um vírgula cinco volt, [p=0.1] {b}tomada de cento e vinte e sete, [p=0.1] {c}fio de alta tensão com milhares de volts. [p=0.3] Mas {d}volt mede o quê? [p=0.3] {e}Energia por coulomb de carga."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular o potencial de uma carga, [p=0.2] {b}a tensão num campo uniforme [p=0.2] e {c}o trabalho para levar uma carga de um ponto a outro."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o campo de uma carga é cá vezes Q, dividido por dê ao quadrado; [p=0.3] e {c}trabalho é força vezes deslocamento, em joule. [p=0.3] Se faltar alguma, procure no canal."),
    # energia e potencial
    dict(id="s04", block="potencial", text="Pense numa bola {a}no alto de uma escada. [p=0.2] Ela tem energia guardada pela posição: [p=0.2] {b}solta, ela desce sozinha, [p=0.1] e a força que a puxa realiza trabalho. [p=0.3] Com cargas é igual. [p=0.2] {c}Uma carga num campo elétrico guarda energia: [p=0.1] a {d}energia potencial elétrica, em joule."),
    dict(id="s05", block="potencial", text="O {a}potencial elétrico é essa energia dividida pela carga: [p=0.2] a energia por coulomb. [p=0.3] Ele se mede em {b}volt, com a letra vê: [p=0.2] {c}um volt é um joule por coulomb. [p=0.3] Na pilha, {d}um vírgula cinco volt quer dizer um vírgula cinco joule por coulomb, [p=0.1] de uma ponta à outra."),
    dict(id="s06", block="potencial", text="Perto de uma carga Q, o potencial é {a}vê igual a cá vezes Q, dividido por dê. [p=0.3] {b}Repare: dê sem o quadrado. [p=0.2] E {c}o sinal da carga entra na conta: [p=0.1] carga negativa dá potencial negativo. [p=0.3] {d}O potencial é escalar: [p=0.1] é só um número, sem seta."),
    dict(id="s07", block="potencial", text="Uma carga de {a}dois microcoulombs, a {b}três metros: [p=0.2] {c}nove vezes dois, dezoito, [p=0.1] e nove menos seis, três. [p=0.2] {d}Dividido por três: [p=0.2] {e}seis vezes dez ao cubo volts, [p=0.1] ou seis mil volts."),
    # tensão
    dict(id="s08", block="tensao", text="O que mais importa é {a}a diferença de potencial entre dois pontos, [p=0.1] a {b}dê dê pê, [p=0.2] também chamada de {c}tensão, a letra U. [p=0.3] {d}U é o potencial do ponto um menos o potencial do ponto dois. [p=0.3] É como {e}a altura de um degrau: [p=0.1] o que conta é quanto se desce."),
    dict(id="s09", block="tensao", text="No campo uniforme, entre placas paralelas, [p=0.2] a tensão é {a}U igual a ê vezes dê: [p=0.2] o campo vezes a distância ao longo das linhas. [p=0.3] {b}Andando no sentido das linhas, o potencial cai. [p=0.3] Campo de {c}quinhentos newtons por coulomb, [p=0.1] {d}vinte centímetros, que são zero vírgula dois metro: [p=0.2] {e}quinhentos vezes zero vírgula dois, cem volts."),
    # trabalho
    dict(id="s10", block="trabalho", text="O trabalho da força elétrica para levar uma carga quê do ponto um ao ponto dois é [p=0.2] {a}tau igual a quê vezes U. [p=0.3] {b}Tau é o trabalho, em joule; [p=0.2] {c}quê é a carga, em coulomb; [p=0.2] {d}U é a tensão entre os pontos, em volt."),
    dict(id="s11", block="trabalho", text="Uma carga de {a}três microcoulombs vai do ponto um ao ponto dois, [p=0.2] e o ponto um está {b}cem volts acima do ponto dois. [p=0.3] {c}Três vezes dez elevado a menos seis, vezes cem: [p=0.2] {d}três vezes dez elevado a menos quatro joule. [p=0.3] {e}Positivo: a força elétrica ajudou o movimento, [p=0.1] como na bola que desce a escada."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}pôr dê ao quadrado no potencial. [p=0.3] {b}O campo tem dê ao quadrado; [p=0.1] {c}o potencial, não. [p=0.3] Na carga de dois microcoulombs a três metros, [p=0.2] quem usa o quadrado acha {d}dois mil volts, [p=0.2] {e}e o certo é seis mil."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}o potencial é escalar. [p=0.2] Com várias cargas, {b}some os potenciais com o sinal, [p=0.2] sem desenhar seta nenhuma. [p=0.3] {c}Mais dois mil volts de uma carga e menos dois mil de outra: [p=0.2] {d}potencial zero no ponto."),
    dict(id="s14", block="atalho", text="Funciona porque {a}energia não tem direção. [p=0.3] {b}Não vale para o campo: [p=0.1] campo é vetor, [p=0.1] e no mesmo ponto de potencial zero {c}o campo pode ser bem forte."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Entre duas placas, o campo é uniforme, de {a}dois mil newtons por coulomb. [p=0.3] {b}Qual é a tensão entre dois pontos a cinco centímetros um do outro, ao longo das linhas? [p=0.3] {c}E qual é o trabalho da força elétrica numa carga positiva de dois microcoulombs [p=0.1] {d}que vai do ponto de potencial maior para o de menor?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Cinco centímetros são zero vírgula zero cinco metro. [p=0.2] {b}U igual a ê vezes dê: [p=0.1] dois mil vezes zero vírgula zero cinco, [p=0.2] {c}cem volts."),
    dict(id="s18", block="resposta", text="{a}Tau igual a quê vezes U: [p=0.1] {b}dois vezes dez elevado a menos seis, vezes cem, [p=0.2] {c}dois vezes dez elevado a menos quatro joule. [p=0.3] {d}Positivo: a carga positiva foi do potencial maior para o menor, [p=0.1] e a força elétrica ajudou."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}vê é cá vezes Q, dividido por dê, sem quadrado e com sinal; [p=0.2] {b}no campo uniforme, U é o campo vezes a distância; [p=0.2] e {c}o trabalho é quê vezes U."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ver {a}onde a carga fica num condutor de metal, [p=0.2] {b}como funciona o para-raios [p=0.1] e por que o carro protege do raio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
