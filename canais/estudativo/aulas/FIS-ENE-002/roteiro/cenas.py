# Estudativo · FIS-ENE-002 — Potência e rendimento (Física · Energia e Colisões · Trabalho e energia).
# Habilidade: calcular potência em watt e rendimento em porcentagem e converter kW, cv e hp.
# Pré-requisitos: FIS-ENE-001 (trabalho, joule), MAT-POR-003 (quantos por cento), MAT-MED-006 (tempo), MAT-MED-003 (prefixos).
#   Próxima: FIS-ENE-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Peso não está em "Já ensinado": o trabalho das caixas vem dado (6.000 J). 1 cv ≈ 735 W e 1 hp ≈ 746 W (valores usuais;
#   a prova costuma dar o valor no enunciado). P = F·v deduzido de τ = F·d e v = d/Δt (MU, FIS-CIN-005).
# Contas: 6.000 / 60 = 100 W; 6.000 / 240 = 25 W; 100 · 735 = 73.500 W = 73,5 kW; 800 / 1.000 = 0,8 = 80 % (erro 1.000 / 800 = 125 %);
#   100 · 746 = 74.600 W = 74,6 kW; 1.000 · 20 = 20.000 W = 20 kW; questão 30.000 / 20 = 1.500 W; 1.500 / 2.000 = 0,75 = 75 %; 2.000 − 1.500 = 500 W.

TITULO = "Potência e rendimento"

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
    dict(id="s01", block="gancho", text="{a}Duas pessoas levam caixas iguais até o mesmo andar. [p=0.2] {b}Uma leva um minuto. [p=0.1] {c}A outra, quatro. [p=0.3] {d}O trabalho das duas é o mesmo. [p=0.2] Então, o que muda?"),
    dict(id="s02", block="gancho", text="Muda {a}a potência. [p=0.2] Até o fim desta aula, você vai calcular potência em {b}watt, [p=0.2] o rendimento de uma máquina em {c}porcentagem [p=0.2] e converter {d}quilowatt, cavalo-vapor e agá pê."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}o trabalho de uma força, em joule; [p=0.2] {c}porcentagem, a parte de cem; [p=0.2] e {d}os prefixos, como o quilo, que vale mil. [p=0.3] Se faltar alguma, procure no canal."),
    # potência
    dict(id="s04", block="potencia", text="{a}Potência é a rapidez com que um trabalho é feito. [p=0.2] É {b}o trabalho dividido pelo tempo: [p=0.2] {c}pê igual a tau dividido por delta tê. [p=0.3] {d}Delta tê é o intervalo de tempo, em segundo: [p=0.2] o instante do fim menos o do começo."),
    dict(id="s05", block="potencia", text="A unidade é {a}joule por segundo, [p=0.2] que se chama {b}watt, o W. [p=0.3] Um motor de {c}dez watts faz dez joules de trabalho a cada segundo."),
    dict(id="s06", block="potencia", text="De volta às caixas. [p=0.2] Digamos que o trabalho seja de {a}seis mil joules. [p=0.2] {b}Um minuto são sessenta segundos: [p=0.2] {c}seis mil dividido por sessenta, cem watts. [p=0.3] {d}Quatro minutos são duzentos e quarenta segundos: [p=0.2] {e}seis mil dividido por duzentos e quarenta, vinte e cinco watts. [p=0.3] {f}Quatro vezes mais tempo, um quarto da potência."),
    # unidades
    dict(id="s07", block="unidades", text="Máquinas têm potências grandes, então entra o prefixo: [p=0.2] {a}um quilowatt, o kW, é mil watts. [p=0.3] Em carros e motores, aparecem duas unidades fora do Sistema Internacional: [p=0.2] {b}o cavalo-vapor, o cv, que vale cerca de setecentos e trinta e cinco watts, [p=0.2] e {c}o agá pê, do inglês, que vale cerca de setecentos e quarenta e seis."),
    dict(id="s08", block="unidades", text="Um motor de {a}cem cavalos-vapor tem {b}cem vezes setecentos e trinta e cinco: [p=0.2] {c}setenta e três mil e quinhentos watts, [p=0.2] ou {d}setenta e três vírgula cinco quilowatts. [p=0.2] {e}Com cem agá pê, seriam setenta e quatro vírgula seis quilowatts. [p=0.3] {f}Na prova, esses valores costumam vir no enunciado: use o que estiver lá."),
    # rendimento
    dict(id="s09", block="rendimento", text="Nenhuma máquina aproveita tudo o que recebe. [p=0.2] {a}Um motor elétrico recebe mil watts da tomada [p=0.2] e {b}entrega oitocentos watts no eixo que gira. [p=0.3] {c}Os outros duzentos viram calor e barulho: [p=0.2] é a potência {d}dissipada, a que se perde."),
    dict(id="s10", block="rendimento", text="{a}Rendimento é a parte útil dividida pelo total recebido: [p=0.2] {b}eta igual à potência útil dividida pela potência total. [p=0.3] Eta é essa letra grega, parecida com um ene. [p=0.2] {c}Oitocentos dividido por mil: [p=0.1] {d}zero vírgula oito, [p=0.1] ou {e}oitenta por cento."),
    dict(id="s11", block="rendimento", text="Repare: o rendimento {a}não tem unidade, [p=0.2] porque watt corta com watt. [p=0.2] {b}Com trabalho em joule no lugar da potência, a conta é igual. [p=0.3] E ele {c}nunca passa de cem por cento: [p=0.2] uma máquina não entrega mais do que recebe."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}dividir ao contrário. [p=0.2] A pessoa faz {b}mil dividido por oitocentos [p=0.1] e acha {c}cento e vinte e cinco por cento."),
    dict(id="s13", block="erro", text="{a}Mais de cem por cento é impossível, [p=0.2] e isso já entrega o erro. [p=0.3] {b}O útil é sempre a parte menor, [p=0.2] e {c}ele vai em cima."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova. [p=0.2] Quando a força e a velocidade são constantes e apontam para o mesmo lado, [p=0.2] {a}a potência é a força vezes a velocidade: [p=0.2] {b}pê igual a efe vezes vê."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o trabalho é força vezes distância, [p=0.2] e {b}distância dividida por tempo é a velocidade. [p=0.3] Um carro a {c}vinte metros por segundo, com uma força de mil newtons para a frente: [p=0.2] {d}mil vezes vinte, vinte mil watts, [p=0.1] ou vinte quilowatts. [p=0.3] {e}Se a velocidade muda, efe vezes vê dá a potência só daquele instante: [p=0.2] para a média, use o trabalho dividido pelo tempo."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um motor {a}recebe dois mil watts da tomada. [p=0.2] Em {b}vinte segundos, ele faz {c}um trabalho útil de trinta mil joules. [p=0.3] {d}Qual é a potência útil, e qual é o rendimento?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Potência útil é o trabalho útil dividido pelo tempo: [p=0.2] {b}trinta mil dividido por vinte, [p=0.1] {c}mil e quinhentos watts."),
    dict(id="s19", block="resposta", text="{a}Rendimento: mil e quinhentos dividido por dois mil. [p=0.2] {b}Zero vírgula setenta e cinco: setenta e cinco por cento. [p=0.3] E {c}os quinhentos watts que sobram viram calor."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}potência é trabalho dividido por tempo, em watt; [p=0.2] {b}um quilowatt é mil watts, e o cv tem cerca de setecentos e trinta e cinco; [p=0.2] e {c}rendimento é útil dividido por total, nunca acima de cem por cento."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai conhecer {a}a energia cinética, a energia do movimento, [p=0.2] e descobrir por que {b}dobrar a velocidade multiplica essa energia por quatro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
