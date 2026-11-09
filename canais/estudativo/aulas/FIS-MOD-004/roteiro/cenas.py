# Estudativo · FIS-MOD-004 — Dualidade onda-partícula (Física · Física Moderna · Quantização, dualidade e relatividade).
# Habilidade: calcular λ = h/(m·v) e dizer quais experimentos mostram onda e quais mostram partícula.
# Pré-requisitos: FIS-MOD-002 (efeito fotoelétrico), FIS-ENE-007 (Q = m·v), FIS-OND-004 (interferência). Próxima: FIS-MOD-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# FIS-MOD-003 (espectros) não está em "Já ensinado" desta aula: não é citada. Difração (FIS-OND-003) está.
# Fatos: Young, fenda dupla com luz (começo do século XIX, 1801–1803); de Broglie, 1924; difração de elétrons num cristal
# (Davisson e Germer, 1927). Massa do elétron 9,1 × 10⁻³¹ kg; v = 7,25 × 10⁶ m/s → Q = 6,6 × 10⁻²⁴ kg·m/s → λ = 10⁻¹⁰ m
# (tamanho de um átomo). Bola de tênis: 60 g (oficial 56–59,4 g) a 50 m/s → Q = 3 → λ = 2,2 × 10⁻³⁴ m. Próton ≈ 1.836 elétrons.

TITULO = "Dualidade onda-partícula"

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
    dict(id="s01", block="gancho", text="{a}Atire elétrons, um de cada vez, contra uma placa com duas fendas. [p=0.3] Do outro lado, {b}eles não fazem dois montinhos, como bolinhas fariam. [p=0.3] {c}Depois de muitos elétrons, fazem faixas claras e escuras, [p=0.2] {d}a marca de uma onda."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular o comprimento de onda de uma partícula [p=0.2] e {b}dizer quais experimentos mostram onda [p=0.1] {c}e quais mostram partícula."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a quantidade de movimento, quê, é a massa vezes a velocidade; [p=0.2] e {c}duas ondas que se encontram se reforçam ou se cancelam: é a interferência. [p=0.3] Se faltar alguma, procure no canal."),
    # luz como onda
    dict(id="s04", block="luz", text="Comece pela luz. [p=0.2] No começo do século dezenove, {a}o inglês Thomas Young passou luz por duas fendas finas. [p=0.3] {b}Na parede, apareceram faixas claras e escuras. [p=0.2] {c}Clara onde as ondas se reforçam, escura onde se cancelam. [p=0.3] {d}Interferência é coisa de onda: [p=0.1] {e}a luz é onda."),
    dict(id="s05", block="luz", text="Mas, na aula do efeito fotoelétrico, {a}a luz arrancou elétrons do metal em pacotes, um fóton por elétron. [p=0.3] {b}Isso é coisa de partícula. [p=0.3] {c}A luz é as duas coisas. [p=0.2] {d}Em cada experimento, ela mostra um lado. [p=0.2] Isso se chama {e}dualidade onda-partícula."),
    dict(id="s06", block="luz", text="A regra para a prova: [p=0.2] {a}quando a luz se espalha, contorna e interfere, [p=0.1] ela se mostra {b}onda: [p=0.1] interferência, difração. [p=0.3] {c}Quando ela troca energia num ponto, um pacote de cada vez, [p=0.1] se mostra {d}partícula: [p=0.1] o efeito fotoelétrico."),
    # de Broglie
    dict(id="s07", block="broglie", text="Em mil novecentos e vinte e quatro, {a}o francês Louis de Broglie fez a pergunta ao contrário: [p=0.2] {b}se a onda de luz age como partícula, [p=0.1] {c}a partícula também age como onda? [p=0.3] {d}Ele propôs que sim, [p=0.2] e deu o comprimento de onda de qualquer corpo."),
    dict(id="s08", block="broglie", text="{a}Lambda igual a agá dividido pela massa vezes a velocidade. [p=0.3] {b}Massa vezes velocidade é a quantidade de movimento, [p=0.1] então {c}lambda é agá dividido por quê. [p=0.3] {d}Agá é a constante de Planck, seis vírgula seis vezes dez elevado a menos trinta e quatro, [p=0.2] {e}e lambda sai em metro."),
    # exemplo do elétron
    dict(id="s09", block="exemplo", text="Um elétron a uns {a}sete milhões de metros por segundo [p=0.1] tem quantidade de movimento de {b}seis vírgula seis vezes dez elevado a menos vinte e quatro quilograma metro por segundo. [p=0.3] {c}Seis vírgula seis dividido por seis vírgula seis: um. [p=0.2] {d}Menos trinta e quatro menos, abre parênteses, menos vinte e quatro: menos dez. [p=0.3] {e}Lambda vale dez elevado a menos dez metros."),
    dict(id="s10", block="exemplo", text="{a}Esse é o tamanho de um átomo. [p=0.2] E a difração aparece quando a fresta tem o tamanho do comprimento de onda. [p=0.3] {b}Num cristal, os átomos enfileirados fazem as frestas certas. [p=0.2] {c}Em mil novecentos e vinte e sete, elétrons bateram num cristal e fizeram difração. [p=0.2] {d}De Broglie estava certo."),
    # por que a bola não
    dict(id="s11", block="bola", text="E por que uma bola não faz difração? [p=0.2] {a}Uma bola de tênis de sessenta gramas, a cinquenta metros por segundo. [p=0.3] {b}Zero vírgula zero seis vezes cinquenta: quê vale três. [p=0.3] {c}Seis vírgula seis vezes dez elevado a menos trinta e quatro, dividido por três: [p=0.2] {d}dois vírgula dois vezes dez elevado a menos trinta e quatro metros. [p=0.3] {e}Não existe fresta tão pequena. [p=0.2] {f}A onda existe, mas nunca aparece."),
    # erro
    dict(id="s12", block="erro", text="Nessa conta, o erro mais comum é {a}deixar a massa em grama. [p=0.3] {b}Sessenta vezes cinquenta dá três mil, [p=0.2] e o lambda sai {c}mil vezes menor do que é. [p=0.3] {d}A constante agá está em joule vezes segundo, que é do Sistema Internacional: [p=0.2] {e}a massa vai em quilograma, a velocidade em metro por segundo."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}lambda é inversamente proporcional à quantidade de movimento. [p=0.3] {b}Dobrou a velocidade, o lambda cai pela metade. [p=0.2] {c}Para comparar dois corpos, nem calcule: compare massa vezes velocidade. [p=0.3] {d}Quem tem o maior quê, tem o menor lambda."),
    dict(id="s14", block="atalho", text="{a}Um próton tem quase mil oitocentas e quarenta vezes a massa do elétron. [p=0.2] {b}Na mesma velocidade, o lambda dele é quase mil oitocentas e quarenta vezes menor. [p=0.3] {c}Não compensa quando a questão pede o valor: [p=0.1] aí, divida agá por quê."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Um elétron tem quantidade de movimento de três vírgula três vezes dez elevado a menos vinte e quatro quilograma metro por segundo. [p=0.3] {b}Qual é o comprimento de onda dele? [p=0.3] E {c}um próton na mesma velocidade desse elétron teria lambda maior ou menor?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá, pelo atalho. [p=0.2] {a}Três vírgula três é metade de seis vírgula seis. [p=0.2] {b}Metade da quantidade de movimento, o dobro do lambda. [p=0.3] {c}Dois vezes dez elevado a menos dez metros. [p=0.2] {d}Pela conta: seis vírgula seis dividido por três vírgula três, dois, [p=0.1] e dez elevado a menos dez."),
    dict(id="s18", block="resposta", text="{a}E o próton: mesma velocidade, massa muito maior. [p=0.2] {b}Quantidade de movimento maior, [p=0.1] {c}lambda menor. [p=0.3] {d}Quase mil oitocentas e quarenta vezes menor que o do elétron."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}luz e matéria são onda e partícula; [p=0.2] {b}interferência e difração mostram a onda, o efeito fotoelétrico mostra a partícula; [p=0.2] e {c}lambda é agá dividido pela massa vezes a velocidade."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}a velocidade da luz vira um limite, [p=0.2] e você vai ver {b}o tempo passar mais devagar para quem viaja rápido. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
