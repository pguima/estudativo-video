# Estudativo · FIS-ELE-022 — Receptores e associação de pilhas (Física · Eletricidade · Geradores e receptores).
# Habilidade: usar U = ε' + r'·i num motor e calcular a fem de pilhas em série e em paralelo.
# Pré-requisitos: FIS-ELE-021 (Pouillet), e por ela FIS-ELE-020 (gerador real), 011, 012 (R/n). Próxima: FIS-ELE-023.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# ε' = "épsilon linha", r' = "erre linha". Fato do gancho: motor travado não gera força contraeletromotriz, a corrente sobe e ele
# esquenta (motor de ventilador travado pode queimar). Leis de Kirchhoff (FIS-ELE-024) só citadas como outra aula.
# Contas: 1,5·2 = 3; 9 + 3 = 12 V; 9/12 = 75 %; travado: 12/1,5 = 8 A (4×), calor 1,5·64 = 96 W contra 1,5·4 = 6 W (16×).
#   Pilhas: 2·1,5 = 3 V; 4 com uma invertida: 3·1,5 − 1,5 = 3 V (em vez de 6). Paralelo: 1,5 V, r/n.
#   Atalho: (24 − 12)/(1 + 2) = 4 A; 24 − 1·4 = 20 = 12 + 2·4.  Questão: 4·1,5 = 6 V; 4·0,1 = 0,4 Ω; 6/(2,6 + 0,4) = 2 A; em paralelo 1,5 V.

TITULO = "Receptores e associação de pilhas"

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
    dict(id="s01", block="gancho", text="{a}Quando a hélice de um ventilador ligado fica travada, [p=0.1] {b}o motor esquenta muito mais, [p=0.1] e {c}pode até queimar. [p=0.3] {d}Girando, o próprio motor segura a corrente. [p=0.2] Parado, não."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender o motor [p=0.2] e {b}calcular a tensão de várias pilhas juntas, [p=0.1] em série e em paralelo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}no gerador real, u igual a épsilon menos erre pequeno vezes i; [p=0.2] e {c}a lei de Pouillet: a corrente é épsilon dividido pela soma das resistências. [p=0.3] Se faltar alguma, procure no canal."),
    # receptor
    dict(id="s04", block="receptor", text="O gerador entrega energia elétrica. [p=0.2] {a}O receptor recebe energia elétrica [p=0.1] e {b}transforma em outra que não é só calor: [p=0.1] {c}movimento, no motor; [p=0.1] {d}energia química, na bateria do celular carregando."),
    dict(id="s05", block="receptor", text="{a}A parte da tensão que vira trabalho útil se chama força contraeletromotriz, [p=0.1] {b}épsilon linha, em volt. [p=0.3] {c}E o receptor também tem resistência interna, erre linha, [p=0.1] {d}que transforma uma parte da energia em calor."),
    dict(id="s06", block="receptor", text="Por isso, {a}o receptor precisa receber mais do que épsilon linha: [p=0.2] {b}u igual a épsilon linha mais erre linha vezes i. [p=0.3] {c}No gerador, a perda interna diminui a tensão que sai. [p=0.1] {d}No receptor, ela aumenta a tensão que precisa entrar."),
    dict(id="s07", block="motor", text="Exemplo: {a}um motor de nove volts de força contraeletromotriz, [p=0.1] com um vírgula cinco ohm interno, [p=0.1] {b}recebendo dois ampères. [p=0.3] {c}Um vírgula cinco vezes dois, três volts de perda. [p=0.2] {d}Ele precisa de nove mais três, [p=0.1] {e}doze volts."),
    dict(id="s08", block="motor", text="{a}O rendimento do receptor é a parte útil dividida pela que entrou: [p=0.1] {b}épsilon linha dividido por u. [p=0.2] {c}Nove dividido por doze, setenta e cinco por cento."),
    dict(id="s09", block="motor", text="E o ventilador travado? [p=0.2] {a}Sem girar, o motor não tem força contraeletromotriz: [p=0.1] {b}épsilon linha vira zero. [p=0.3] {c}Com os mesmos doze volts, a corrente é doze dividido por um vírgula cinco: [p=0.1] {d}oito ampères, quatro vezes mais. [p=0.2] {e}E o calor, erre linha vezes i ao quadrado, fica dezesseis vezes maior."),
    # pilhas
    dict(id="s10", block="pilhas", text="Agora, as pilhas. [p=0.2] {a}Em série, o polo positivo de uma encosta no negativo da outra. [p=0.2] {b}As forças eletromotrizes somam: [p=0.1] {c}duas pilhas de um vírgula cinco volts dão três volts. [p=0.3] {d}As resistências internas também somam, [p=0.1] porque estão em série."),
    dict(id="s11", block="pilhas", text="{a}Se uma pilha entrar invertida, ela subtrai. [p=0.2] {b}Quatro pilhas, uma invertida: [p=0.1] três vezes um vírgula cinco, quatro e meio, [p=0.1] menos um e meio: [p=0.1] {c}três volts, em vez de seis."),
    dict(id="s12", block="paralelo", text="{a}Em paralelo, pilhas iguais ligam positivo com positivo e negativo com negativo. [p=0.3] {b}A força eletromotriz não soma: [p=0.1] {c}continua um vírgula cinco volts. [p=0.2] {d}O que muda é a resistência interna: [p=0.1] {e}divida pela quantidade, como em resistores iguais em paralelo. [p=0.3] {f}Cada pilha fornece só uma parte da corrente, e o conjunto dura mais."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}somar as forças eletromotrizes em paralelo. [p=0.3] {b}Três pilhas de um vírgula cinco volts em paralelo não dão quatro e meio: [p=0.1] {c}dão um vírgula cinco. [p=0.2] {d}Só a série soma."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho para gerador e motor no mesmo circuito: [p=0.2] {a}com a bateria mais forte que o motor, a força contraeletromotriz entra subtraindo na lei de Pouillet. [p=0.3] {b}A corrente é épsilon menos épsilon linha, [p=0.1] dividido pela soma de todas as resistências."),
    dict(id="s15", block="atalho", text="Exemplo: {a}bateria de vinte e quatro volts com um ohm, [p=0.1] {b}motor de doze volts com dois ohms. [p=0.2] {c}Vinte e quatro menos doze, doze; [p=0.1] dividido por um mais dois, três: [p=0.1] {d}quatro ampères. [p=0.3] Funciona porque {e}o motor empurra contra a bateria. [p=0.2] {f}Não compensa com ramos em paralelo: [p=0.1] aí, entram as leis de Kirchhoff, assunto de outra aula."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Quatro pilhas de um vírgula cinco volts, cada uma com zero vírgula um ohm de resistência interna, [p=0.1] {b}são ligadas em série [p=0.1] a {c}uma lâmpada de dois vírgula seis ohms. [p=0.3] {d}Qual é a força eletromotriz do conjunto, [p=0.1] {e}qual é a corrente, [p=0.2] e {f}qual seria a força eletromotriz se as quatro fossem ligadas em paralelo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Em série, tudo soma: [p=0.1] {b}quatro vezes um vírgula cinco, seis volts; [p=0.1] {c}quatro vezes zero vírgula um, zero vírgula quatro ohm. [p=0.3] {d}Pouillet: seis dividido por dois vírgula seis mais zero vírgula quatro, [p=0.1] {e}seis dividido por três, [p=0.1] {f}dois ampères. [p=0.3] {g}Em paralelo, a força eletromotriz não soma: [p=0.1] {h}um vírgula cinco volts."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}no receptor, u igual a épsilon linha mais erre linha vezes i; [p=0.2] {b}pilhas em série somam tudo; [p=0.2] {c}em paralelo, se forem iguais, a força eletromotriz fica a mesma, e a resistência interna se divide."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai {a}praticar com conta de luz, chuveiro, baterias e motores. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
