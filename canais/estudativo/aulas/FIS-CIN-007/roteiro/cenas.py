# Estudativo · FIS-CIN-007 — Aceleração e velocidade no MUV (Física · Cinemática · Movimento uniforme e variado).
# Habilidade: calcular a aceleração, usar v = v0 + a·t e dizer se o movimento é acelerado ou retardado.
# Pré-requisitos: FIS-CIN-005 (função horária). Já ensinado inclui MAT-NUM-017 (regra de sinais). Próxima: FIS-CIN-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. m/s² foi prometido em FIS-CIN-001 ("unidade da aceleração, assunto de outra aula").

TITULO = "Aceleração e velocidade no MUV"

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
    dict(id="s01", block="gancho", text="{a}Metro por segundo ao quadrado. [p=0.3] É a unidade da aceleração. [p=0.2] Mas o que seria {b}um segundo ao quadrado? [p=0.3] {c}Nenhum relógio marca isso. [p=0.3] {d}Até o fim desta aula, essa unidade vai fazer todo o sentido."),
    dict(id="s02", block="gancho", text="E você vai {a}calcular a aceleração, [p=0.2] {b}achar a velocidade em qualquer instante [p=0.2] e dizer se o movimento é {c}acelerado ou retardado."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o movimento uniforme, com velocidade constante; [p=0.2] e {c}o delta, que é o final menos o inicial. [p=0.3] Se faltar alguma, procure no canal."),
    # aceleração
    dict(id="s04", block="aceleracao", text="{a}Um carro sai parado de um sinal. [p=0.2] {b}Um segundo depois, está a quatro metros por segundo. [p=0.2] {c}Dois segundos depois, a oito. [p=0.1] {d}Três segundos, doze. [p=0.3] {e}A cada segundo, a velocidade ganha quatro metros por segundo."),
    dict(id="s05", block="aceleracao", text="Isso é a {a}aceleração: [p=0.2] quanto a velocidade muda a cada segundo. [p=0.3] {b}Á igual a delta vê dividido por delta tê: [p=0.2] a variação da velocidade dividida pelo tempo. [p=0.3] {c}De zero a vinte metros por segundo, em cinco segundos: [p=0.2] {d}vinte dividido por cinco, quatro."),
    dict(id="s06", block="aceleracao", text="E a unidade? [p=0.2] {a}Metro por segundo, dividido por segundo. [p=0.3] {b}Quatro metros por segundo a cada segundo. [p=0.2] O segundo aparece duas vezes embaixo: [p=0.1] {c}metro por segundo ao quadrado. [p=0.3] {d}Segundo ao quadrado é só o jeito curto de escrever: por segundo, a cada segundo."),
    # MUV e função
    dict(id="s07", block="funcao", text="Quando a aceleração é {a}constante, o movimento se chama {b}uniformemente variado: [p=0.2] o {c}eme u vê. [p=0.3] A velocidade muda sempre o mesmo tanto a cada segundo."),
    dict(id="s08", block="funcao", text="Daí sai a função da velocidade: [p=0.2] {a}vê igual a vê zero mais á tê. [p=0.3] {b}Vê é a velocidade no instante tê. [p=0.2] {c}Vê zero é a velocidade inicial. [p=0.2] {d}Á é a aceleração, em metro por segundo ao quadrado. [p=0.3] {e}Á vezes tê é o quanto a velocidade ganhou. [p=0.2] É a mesma ideia do sorvete, agora com a velocidade."),
    dict(id="s09", block="funcao", text="Um ônibus está a {a}dez metros por segundo e acelera {b}dois metros por segundo ao quadrado. [p=0.3] Depois de {c}seis segundos: [p=0.2] {d}dez mais dois vezes seis, [p=0.1] {e}vinte e dois metros por segundo."),
    # freada
    dict(id="s10", block="freada", text="{a}E quando o carro freia? [p=0.2] A velocidade diminui, então {b}a aceleração tem o sinal contrário ao da velocidade. [p=0.3] Um carro a {c}vinte metros por segundo freia com aceleração de {d}menos quatro metros por segundo ao quadrado. [p=0.2] Quando ele para? [p=0.2] {e}Parar é vê igual a zero: [p=0.1] {f}zero igual a vinte menos quatro tê. [p=0.2] {g}Cinco segundos."),
    dict(id="s11", block="freada", text="Quando a velocidade, em módulo, {a}aumenta, o movimento é {b}acelerado. [p=0.2] Quando {c}diminui, é {d}retardado. [p=0.3] {e}O ônibus estava acelerado. [p=0.1] {f}O carro que freia, retardado."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: {a}achar que aceleração negativa é sempre freada. [p=0.3] Com a frente do carro como sentido positivo, [p=0.1] um carro anda {b}de ré, a menos três metros por segundo, [p=0.2] com aceleração de {c}menos dois. [p=0.3] Um segundo depois: [p=0.1] {d}menos três menos dois, menos cinco. [p=0.2] {e}Cinco metros por segundo é mais rápido que três: [p=0.2] {f}ele está acelerando, para trás."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}olhe só os sinais de vê e de á. [p=0.3] {b}Sinais iguais: acelerado. [p=0.2] {c}Sinais diferentes: retardado. [p=0.3] É como a regra de sinais da multiplicação: {d}sinais iguais dão mais."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a aceleração no mesmo sentido da velocidade empurra a favor do movimento, [p=0.2] e {b}no sentido contrário, empurra contra. [p=0.3] {c}Não serve no instante em que a velocidade é zero: [p=0.2] ali o corpo está parado por um instante, partindo ou virando, [p=0.1] e não é nem um nem outro."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma moto {a}parte do repouso, [p=0.1] ou seja, com velocidade inicial zero, [p=0.2] e chega a {b}trinta metros por segundo em {c}seis segundos. [p=0.3] {d}Qual é a aceleração? [p=0.2] {e}Qual é a velocidade depois de quatro segundos? [p=0.2] {f}E o movimento é acelerado ou retardado?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Delta vê: trinta menos zero, trinta. [p=0.2] {b}Trinta dividido por seis: cinco metros por segundo ao quadrado. [p=0.3] {c}Vê igual a zero mais cinco vezes quatro: [p=0.2] {d}vinte metros por segundo. [p=0.3] {e}Vê e á positivos, sinais iguais: acelerado."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}aceleração é quanto a velocidade muda por segundo; [p=0.2] {b}vê igual a vê zero mais á tê; [p=0.2] {c}sinais iguais, acelerado; diferentes, retardado."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai descobrir {a}onde o corpo está quando a velocidade muda, [p=0.2] com uma {b}função do segundo grau. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
