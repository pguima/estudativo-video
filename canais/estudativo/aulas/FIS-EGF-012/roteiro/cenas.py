# Estudativo · FIS-EGF-012 — Praticando: vazão e Bernoulli (Física · Equilíbrio, Gravitação e Fluidos · Hidrodinâmica · prática).
# Habilidade: resolver questões de vazão, continuidade e pressão em fluidos em movimento.
# Pré-requisitos: FIS-EGF-010, FIS-EGF-011. Próxima: nenhuma (fim da trilha). Questões inéditas, criadas para esta aula.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Aula de extensão (Fuvest). Ar: 1,2 kg/m³; água: 1.000 kg/m³.
# Contas: 0,0004·2,5 = 0,001 m³/s = 1 L/s → 1.000 s = 16 min 40 s; 30·2 = 60 m², 10·3 = 30 m² → 2 m/s;
# 500·(36 − 4) = 16.000 Pa; 0,6·(70 − 60)·(70 + 60) = 780 Pa → 780·20 = 15.600 N; √(20·5) = 10; √(20·1,25) = 5.

TITULO = "Praticando: vazão e Bernoulli"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações com fluidos em movimento, [p=0.1] criadas para esta aula: [p=0.2] {b}da caixa d'água [p=0.1] {c}até a asa de um avião. [p=0.3] Em cada uma, {d}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar três ferramentas: [p=0.2] {a}a vazão, quê igual a á vezes vê; [p=0.2] {b}a continuidade, á um vê um igual a á dois vê dois; [p=0.2] e {c}Bernoulli: onde o fluido corre mais, a pressão cai, [p=0.2] e no furo do tanque, vê é a raiz de dois gê agá. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: encher a caixa
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] {b}Um cano de quatro centímetros quadrados de área [p=0.1] {c}leva água a dois vírgula cinco metros por segundo. [p=0.3] {d}Em quanto tempo ele enche uma caixa d'água de mil litros?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Faça tudo em centímetro: [p=0.1] dois vírgula cinco metros por segundo são duzentos e cinquenta centímetros por segundo. [p=0.3] {b}Vazão: quatro vezes duzentos e cinquenta, [p=0.1] {c}mil centímetros cúbicos por segundo: [p=0.1] {d}um litro por segundo. [p=0.3] {e}Mil litros, a um litro por segundo: [p=0.1] {f}mil segundos, [p=0.1] dezesseis minutos e quarenta segundos."),
    # situação 2: o rio
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] {b}Um rio tem trinta metros de largura e dois de profundidade, [p=0.1] {c}e corre a um metro por segundo. [p=0.3] {d}Num trecho estreito, fica com dez metros de largura e três de profundidade. [p=0.2] {e}Com que velocidade a água passa ali?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] A seção do rio é um retângulo. [p=0.2] {a}No trecho largo: trinta vezes dois, sessenta metros quadrados. [p=0.2] {b}No estreito: dez vezes três, trinta. [p=0.3] {c}Sessenta vezes um, igual a trinta vezes vê. [p=0.2] {d}Vê igual a dois metros por segundo. [p=0.2] {e}Área pela metade, velocidade dobrada."),
    # situação 3: cano que afina
    dict(id="s09", block="questao3", text="{a}Situação três. [p=0.2] {b}Num cano deitado, a água passa de dois para seis metros por segundo quando o cano afina. [p=0.3] {c}Quanto a pressão cai, em pascal?"),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="Vamos lá. [p=0.2] {a}Cano deitado: o termo da altura é igual dos dois lados. [p=0.2] {b}A pressão cai o quanto cresce a densidade vezes vê ao quadrado, sobre dois. [p=0.3] {c}A densidade da água, mil, sobre dois: quinhentos, [p=0.1] {d}vezes seis ao quadrado menos dois ao quadrado, [p=0.1] trinta e seis menos quatro, trinta e dois. [p=0.3] {e}Quinhentos vezes trinta e dois: [p=0.1] {f}dezesseis mil pascals."),
    # atalho
    dict(id="s12", block="atalho", text="Repare num atalho de conta: [p=0.2] {a}a diferença de dois quadrados é a soma vezes a diferença. [p=0.3] {b}Seis ao quadrado menos dois ao quadrado: [p=0.1] {c}seis mais dois, oito, vezes seis menos dois, quatro: [p=0.1] {d}trinta e dois, sem elevar nada. [p=0.3] {e}Ele brilha com números grandes, como setenta e sessenta. [p=0.2] {f}Com números pequenos, tanto faz."),
    # situação 4: a asa
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Numa asa, o ar passa a setenta metros por segundo por cima [p=0.1] {c}e a sessenta por baixo. [p=0.2] {d}A densidade do ar é um vírgula dois quilo por metro cúbico, [p=0.1] {e}e a asa tem vinte metros quadrados. [p=0.3] {f}Qual é a força de sustentação?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] {a}A diferença de pressão: um vírgula dois sobre dois, zero vírgula seis, [p=0.1] {b}vezes setenta ao quadrado menos sessenta ao quadrado. [p=0.3] {c}Pelo atalho: setenta mais sessenta, cento e trinta, [p=0.1] vezes setenta menos sessenta, dez. [p=0.1] {d}Mil e trezentos. [p=0.2] {e}Zero vírgula seis vezes mil e trezentos: [p=0.1] {f}setecentos e oitenta pascals."),
    dict(id="s16", block="resposta4", text="{a}Pressão é força sobre área, [p=0.1] então força é pressão vezes área. [p=0.2] {b}Setecentos e oitenta vezes vinte: [p=0.1] {c}quinze mil e seiscentos newtons para cima."),
    # situação 5: o tanque que esvazia
    dict(id="s17", block="questao5", text="{a}Última situação. [p=0.2] {b}Um tanque aberto tem um furo cinco metros abaixo do nível da água. [p=0.3] {c}Com que velocidade a água sai? [p=0.2] {d}E quando o nível baixar até um metro e vinte e cinco acima do furo?"),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="Vamos lá. [p=0.2] {a}Vê ao quadrado é vinte vezes agá. [p=0.2] {b}Vinte vezes cinco, cem: [p=0.1] {c}vê igual a dez metros por segundo. [p=0.3] {d}Vinte vezes um vírgula vinte e cinco, vinte e cinco: [p=0.1] {e}vê igual a cinco. [p=0.3] {f}A altura caiu para um quarto, e a velocidade, para a metade: [p=0.1] {g}a velocidade acompanha a raiz da altura."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}vazão é área vezes velocidade, igual em todo o cano; [p=0.2] {b}onde o fluido corre mais, a pressão cai; [p=0.2] e {c}no furo do tanque, vê é a raiz de dois gê agá."),
    dict(id="s21", block="fim", text="E com isso, {a}a trilha de equilíbrio, gravitação e fluidos terminou. [p=0.3] Você saiu {b}da gangorra [p=0.1] e chegou {c}à asa do avião. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
