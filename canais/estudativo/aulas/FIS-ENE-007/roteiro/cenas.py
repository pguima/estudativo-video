# Estudativo · FIS-ENE-007 — Quantidade de movimento e impulso (Física · Energia e Colisões · Impulso e colisões).
# Habilidade: calcular Q = m·v e I = F·Δt, usar I = ΔQ e explicar por que o airbag protege.
# Pré-requisitos: FIS-DIN-002 (F = m·a), FIS-CIN-007 (a = Δv/Δt). Próxima: FIS-ENE-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# "Já ensinado" NÃO tem trabalho, energia nem peso: a aula não fala de energia. I = ΔQ sai de F = m·a com a = Δv/Δt.
#   Inversamente proporcional: MAT-RAZ-004. Tempos de parada (0,01 s e 0,1 s) são valores ilustrativos.
# Contas: 0,5·20 = 10; 1.000·20 = 20.000 (2.000 vezes); chute 500·0,02 = 10 N·s → v = 10/0,5 = 20 m/s; airbag 70·20 = 1.400,
#   1.400/0,01 = 140.000 N, 1.400/0,1 = 14.000 N; parede 0,5·(−10 − 10) = −10; questão 0,4·(−10 − 15) = −10, 10/0,05 = 200 N
#   (erro: 0,4·(15 − 10) = 2, 2/0,05 = 40 N).

TITULO = "Quantidade de movimento e impulso"

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
    dict(id="s01", block="gancho", text="{a}Numa batida a setenta e dois quilômetros por hora, o motorista vai parar de qualquer jeito. [p=0.3] {b}Então, como o airbag salva a vida dele? [p=0.3] A resposta está em {c}duas grandezas novas."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a quantidade de movimento e o impulso, [p=0.2] {b}ligar um ao outro [p=0.2] e {c}explicar o airbag com uma conta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a segunda lei de Newton, força resultante igual a massa vezes aceleração; [p=0.2] e {c}a aceleração, a variação da velocidade dividida pelo tempo. [p=0.3] Se faltar alguma, procure no canal."),
    # quantidade de movimento
    dict(id="s04", block="quantidade", text="Para parar um corpo, o que pesa mais: a massa ou a velocidade? [p=0.2] {a}As duas. [p=0.2] Uma bola de futebol a vinte metros por segundo dá para segurar. [p=0.2] {b}Um carro na mesma velocidade, não. [p=0.3] Por isso a Física junta as duas numa grandeza só: [p=0.2] {c}a quantidade de movimento."),
    dict(id="s05", block="quantidade", text="{a}Quantidade de movimento é a massa vezes a velocidade: [p=0.2] {b}quê igual a eme vezes vê. [p=0.2] A unidade é {c}quilograma vezes metro por segundo. [p=0.3] {d}Ela é vetorial: tem a direção e o sentido da velocidade."),
    dict(id="s06", block="quantidade", text="{a}A bola de meio quilograma, a vinte metros por segundo: [p=0.2] {b}quantidade de movimento dez. [p=0.2] {c}O carro de mil quilogramas, na mesma velocidade: [p=0.2] {d}vinte mil. [p=0.2] Duas mil vezes mais."),
    # impulso
    dict(id="s07", block="impulso", text="Para mudar a quantidade de movimento, é preciso uma força agindo durante um tempo. [p=0.2] {a}Impulso é a força vezes o intervalo de tempo: [p=0.2] {b}í igual a efe vezes delta tê. [p=0.2] A unidade é {c}newton vezes segundo. [p=0.2] {d}Também é vetorial, com o sentido da força."),
    dict(id="s08", block="impulso", text="Falta a ligação. [p=0.2] {a}Comece com a segunda lei: força resultante igual a massa vezes aceleração. [p=0.2] {b}Troque a aceleração por delta vê dividido por delta tê. [p=0.2] {c}Passe o delta tê para o outro lado, multiplicando. [p=0.3] Fica {d}efe vezes delta tê igual a eme vezes delta vê."),
    dict(id="s09", block="impulso", text="{a}Do lado esquerdo está o impulso da força resultante. [p=0.2] {b}Do direito, a variação da quantidade de movimento. [p=0.3] {c}Impulso igual a delta quê: [p=0.2] {d}a quantidade de movimento do fim menos a do começo."),
    dict(id="s10", block="impulso", text="Num chute, o pé empurra a bola com {a}quinhentos newtons, durante {b}dois centésimos de segundo. [p=0.2] {c}Impulso: quinhentos vezes zero vírgula zero dois, dez newtons vezes segundo. [p=0.3] A bola estava parada, então {d}sai com quantidade de movimento dez. [p=0.2] {e}Com meio quilograma, ela sai a vinte metros por segundo."),
    # airbag
    dict(id="s11", block="airbag", text="Volte ao airbag. [p=0.2] {a}Uma pessoa de setenta quilogramas, a vinte metros por segundo, os setenta e dois quilômetros por hora, para. [p=0.2] {b}A variação da quantidade de movimento vale mil e quatrocentos, contra o movimento, com ou sem airbag. [p=0.3] {c}Contra o volante, ela para em um centésimo de segundo: [p=0.2] {d}força de cento e quarenta mil newtons."),
    dict(id="s12", block="airbag", text="{a}No airbag, ela para em um décimo de segundo, [p=0.2] dez vezes mais tempo. [p=0.2] {b}A força cai para catorze mil newtons, dez vezes menor. [p=0.3] {c}O mesmo impulso, espalhado num tempo maior, dá uma força menor. [p=0.2] É por isso que {d}você dobra os joelhos ao pular de um muro."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer o sentido. [p=0.2] Uma bola de meio quilograma chega a uma parede a {b}dez metros por segundo e volta a dez metros por segundo. [p=0.2] A pessoa faz {c}dez menos dez, zero, [p=0.1] e diz que {d}não houve impulso."),
    dict(id="s14", block="erro", text="Mas a bola {a}inverteu o sentido. [p=0.2] {b}Com a ida positiva, a volta é menos dez. [p=0.2] {c}Delta vê: menos dez menos dez, menos vinte. [p=0.2] {d}Delta quê: meio vezes menos vinte, menos dez. [p=0.3] {e}O impulso vale dez, apontando para fora da parede."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}bater e voltar com a mesma velocidade dá o dobro do impulso de bater e parar. [p=0.3] {b}Para parar, a quantidade vai de dez a zero. [p=0.2] {c}Para voltar, vai de dez a menos dez: o dobro. [p=0.3] {d}E, com o mesmo impulso, tempo dez vezes maior dá força dez vezes menor."),
    dict(id="s16", block="atalho", text="Funciona porque, {a}com o impulso fixo, força e tempo são inversamente proporcionais. [p=0.3] {b}Não compensa quando a velocidade de volta é diferente da de ida: [p=0.2] aí, faça a conta com os sinais."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma bola de {a}zero vírgula quatro quilograma chega a uma parede a {b}quinze metros por segundo [p=0.2] e volta a {c}dez metros por segundo. [p=0.2] O contato dura {d}cinco centésimos de segundo. [p=0.3] {e}Qual é o impulso da parede, e qual é a força média?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Ida positiva, volta negativa. [p=0.2] {b}Delta vê: menos dez menos quinze, menos vinte e cinco. [p=0.2] {c}Delta quê: zero vírgula quatro vezes menos vinte e cinco, menos dez. [p=0.2] {d}O impulso vale dez newtons vezes segundo, para fora da parede."),
    dict(id="s20", block="resposta", text="{a}A força muda durante o toque, e a força média é a força constante que daria o mesmo impulso. [p=0.2] {b}Dez dividido por zero vírgula zero cinco: [p=0.1] {c}duzentos newtons. [p=0.3] Quem esquece o sinal faz quinze menos dez e acha {d}só quarenta."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}quantidade de movimento é massa vezes velocidade; [p=0.2] {b}impulso é força vezes tempo; [p=0.2] {c}o impulso é a variação da quantidade de movimento; [p=0.2] e {d}mais tempo de parada, menos força."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai ver que, {a}quando nada de fora empurra, [p=0.2] {b}a quantidade de movimento total não muda, [p=0.2] e usar isso no coice da espingarda. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
