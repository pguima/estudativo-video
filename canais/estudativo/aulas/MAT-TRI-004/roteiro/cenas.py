# Estudativo · MAT-TRI-004 — Altura, rampa e distância inacessível (Matemática · Trigonometria).
# Habilidade: achar a altura de uma torre vista a 30 m sob ângulo de 60° (30√3 ≈ 52 m) e a inclinação de uma rampa.
# Pré-requisitos: MAT-TRI-002 (três perguntas: ângulo, lado conhecido, lado procurado), MAT-TRI-003 (tabela de 30°, 45° e 60°; metade do equilátero 1, √3, 2). Próxima: MAT-TRI-005.
# Questão inédita, criada para esta aula. Seno, cosseno e tangente narrados por extenso. Aproximação das aulas anteriores: √3 ≈ 1,7 (aqui também 1,73, para chegar a 52).

TITULO = "Altura, rampa e distância inacessível"

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
    dict(id="s01", block="gancho", text="{a}Uma torre. [p=0.2] Você está a {b}trinta metros do pé dela [p=0.2] e enxerga o topo sob {c}um ângulo de sessenta graus. [p=0.3] {d}Qual é a altura da torre? [p=0.3] Sem subir e sem trena: {e}a tangente resolve."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você mede alturas e distâncias que não dá para alcançar, [p=0.2] acha {b}a inclinação de uma rampa [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}as três perguntas para escolher a razão: qual o ângulo, que lado eu conheço, que lado eu quero; [p=0.2] {c}a tabela de trinta, quarenta e cinco e sessenta graus; [p=0.2] e {d}raiz de três perto de um vírgula sete. [p=0.3] Se faltar alguma, procure no canal."),
    # torre
    dict(id="s04", block="torre", text="{a}O ângulo entre o chão e a linha do seu olhar até o topo [p=0.2] se chama {b}ângulo de elevação. [p=0.3] {c}A torre, o chão e essa linha formam um triângulo retângulo, [p=0.2] porque {d}a torre fica em pé, em ângulo reto com o chão."),
    dict(id="s05", block="torre", text="As três perguntas. [p=0.2] {a}O ângulo é o de sessenta graus, no seu pé. [p=0.2] {b}Você conhece os trinta metros do chão: eles encostam no ângulo, são o cateto adjacente. [p=0.2] {c}Você quer a altura: ela fica de frente para o ângulo, é o cateto oposto. [p=0.3] {d}Oposto e adjacente: tangente."),
    dict(id="s06", block="torre", text="{a}A tangente de sessenta graus é raiz de três. [p=0.2] Chame a altura de {b}agá. [p=0.2] {c}Raiz de três igual a agá dividido por trinta. [p=0.2] {d}Multiplique cada lado por trinta: [p=0.2] {e}agá igual a trinta raiz de três metros."),
    dict(id="s07", block="torre", text="Quanto é isso? [p=0.2] {a}Trinta vezes um vírgula sete dá cinquenta e um. [p=0.2] Com uma casa decimal a mais, {b}raiz de três perto de um vírgula setenta e três, [p=0.2] dá {c}cinquenta e um vírgula nove: cerca de cinquenta e dois metros. [p=0.3] A diferença vem do arredondamento: um vírgula sete é um pouco menos que raiz de três. [p=0.2] Na prova, {d}use o valor que o enunciado der."),
    dict(id="s08", block="torre", text="Um detalhe: aqui, {a}o olho ficou na altura do chão. [p=0.2] Se a prova der {b}a altura da pessoa, [p=0.2] {c}some essa altura no final."),
    # rampa
    dict(id="s09", block="rampa", text="Agora, a rampa. [p=0.2] {a}A inclinação de uma rampa é o ângulo que ela faz com o chão. [p=0.3] Uma rampa de skate tem {b}quatro metros de comprimento [p=0.2] e sobe até {c}dois metros de altura. [p=0.3] {d}Qual é a inclinação?"),
    dict(id="s10", block="rampa", text="Desta vez, {a}o que falta é o ângulo. [p=0.2] {b}A rampa é a hipotenusa: quatro. [p=0.2] {c}A altura fica de frente para o ângulo: oposto, dois. [p=0.2] {d}Oposto e hipotenusa: seno. [p=0.2] {e}Dois dividido por quatro dá um meio."),
    dict(id="s11", block="rampa", text="Que ângulo tem seno um meio? [p=0.2] {a}Na tabela, o seno de trinta graus é um meio. [p=0.2] {b}A rampa tem trinta graus de inclinação. [p=0.3] Isso sai de cabeça porque {c}um meio está na tabela. [p=0.2] Com outro número, {d}a prova precisa dar o valor."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum na torre é {a}tratar os trinta metros como hipotenusa. [p=0.2] A pessoa usa o seno: {b}trinta vezes raiz de três dividido por dois dá quinze raiz de três, [p=0.2] {c}cerca de vinte e cinco metros e meio."),
    dict(id="s13", block="erro", text="Mas os trinta metros estão {a}no chão, encostados no ângulo: são o adjacente. [p=0.2] {b}A hipotenusa é a linha do olhar, que ninguém mediu. [p=0.3] {c}Antes da conta, dê nome aos três lados."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para trinta e sessenta graus. [p=0.2] Lembre {a}a metade do triângulo equilátero: lados um, raiz de três e dois. [p=0.3] {b}De frente para o trinta, o menor lado. [p=0.2] {c}De frente para o sessenta, o menor vezes raiz de três. [p=0.2] {d}A hipotenusa é o dobro do menor."),
    dict(id="s15", block="atalho", text="Na torre, o ângulo lá no topo mede {a}cento e oitenta menos noventa menos sessenta, que dá trinta. [p=0.2] {b}Os trinta metros do chão ficam de frente para ele: são o menor lado. [p=0.2] {c}A altura, de frente para o sessenta, é trinta raiz de três. [p=0.2] Sem equação."),
    dict(id="s16", block="atalho", text="Funciona porque {a}todo triângulo com ângulos de trinta, sessenta e noventa graus é semelhante a essa metade: [p=0.2] {b}os lados mantêm a mesma proporção. [p=0.3] {c}Não compensa com ângulo fora da tabela, como trinta e sete graus. [p=0.2] Aí, {d}use o valor que a prova der."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Você quer {a}a largura de um rio, sem atravessar. [p=0.2] Na margem, você fica {b}bem em frente a uma árvore da outra margem. [p=0.2] {c}Anda trinta metros pela margem, em linha reta, [p=0.2] e vê a árvore sob {d}um ângulo de trinta graus com a margem. [p=0.3] {e}Qual a largura do rio? [p=0.2] Use raiz de três perto de um vírgula sete."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}O ângulo reto fica no ponto em frente à árvore. [p=0.2] {b}Os trinta metros da margem encostam no ângulo de trinta graus: adjacente. [p=0.2] {c}A largura fica de frente para ele: oposto. [p=0.2] {d}Oposto e adjacente: tangente."),
    dict(id="s20", block="resposta", text="{a}A tangente de trinta graus é raiz de três dividido por três. [p=0.2] Chame a largura de xis: [p=0.2] {b}raiz de três dividido por três igual a xis dividido por trinta. [p=0.2] {c}Multiplique por trinta: xis igual a trinta raiz de três, dividido por três. [p=0.2] Trinta dividido por três dá dez: {d}xis igual a dez raiz de três. [p=0.3] {e}Dez vezes um vírgula sete dá dezessete metros."),
    dict(id="s21", block="resposta", text="Faz sentido: {a}de frente para o ângulo de trinta graus fica o menor lado, [p=0.2] e {b}dezessete é menos que a margem. [p=0.3] Pelo atalho, {c}a margem é a largura vezes raiz de três, [p=0.2] então {d}a largura é trinta dividido por raiz de três. [p=0.2] Tirando a raiz de baixo, {e}o mesmo dez raiz de três."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}desenhe o triângulo retângulo, [p=0.2] {b}dê nome aos lados a partir do ângulo [p=0.2] e {c}use a razão que liga o que você tem ao que você quer."),
    dict(id="s23", block="fim", text="Na próxima aula, você mede {a}a altura de um morro de dois pontos diferentes, [p=0.2] com ângulos de {b}trinta e de sessenta graus, a cem metros um do outro. [p=0.2] E {c}monta um sistema para achar a altura. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
