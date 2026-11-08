# Estudativo · MAT-ESP-002 — Planificações: montar e desmontar sólidos (Matemática · Geometria Espacial).
# Habilidade: dizer qual sólido sai de um molde, achar a face oposta num cubo planificado e ligar a lateral do cilindro a um retângulo de largura 2πr.
# Pré-requisitos: MAT-ESP-001 (prisma, pirâmide, cilindro, cone, esfera; face e aresta), MAT-POL-004 (C = 2πr, π = 3). Próxima: MAT-ESP-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Molde do cubo nas cenas s07–s08: faixa de quatro quadrados em pé (1 a 4, de cima para baixo), aba 5 à esquerda do 2 e aba 6 à direita do 2.
# Molde da questão: faixa 1 a 4 em pé, aba 5 à esquerda do 1 e aba 6 à direita do 3 (molde válido).

TITULO = "Planificações: montar e desmontar sólidos"

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
    dict(id="s01", block="gancho", text="{a}Desmonte uma caixa de sapato e abra no chão. [p=0.2] Sai {b}uma figura plana, feita de retângulos. [p=0.3] Se alguém te der só essa figura, {c}você consegue dizer que sólido ela monta? [p=0.2] E {d}qual face vai ficar de frente para qual?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você monta e desmonta sólidos de cabeça [p=0.2] e leva um {b}atalho de prova para o cubo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o prisma tem duas bases iguais ligadas por retângulos, e a pirâmide tem uma base e triângulos que se encontram num ponto; [p=0.2] e {c}a volta de uma circunferência mede dois pi érre. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="molde", text="{a}Planificação é o sólido aberto e esticado no plano, [p=0.2] como {b}o molde de papel que você recorta, dobra e cola. [p=0.3] {c}Cada face do sólido vira uma figura do molde."),
    dict(id="s05", block="molde", text="Para descobrir o sólido, {a}olhe as formas do molde. [p=0.2] {b}Duas figuras iguais e vários retângulos: é prisma. [p=0.2] As figuras iguais são as bases. [p=0.2] {c}Dois triângulos e três retângulos, prisma de base triangular."),
    dict(id="s06", block="molde", text="{a}Uma figura só, cercada de triângulos que dobram até se encontrar num ponto: é pirâmide. [p=0.2] {b}Um quadrado com quatro triângulos em volta, pirâmide quadrangular."),
    # cubo
    dict(id="s07", block="cubo", text="O cubo tem seis faces quadradas. [p=0.2] Um molde famoso é {a}a cruz: [p=0.2] {b}uma faixa de quatro quadrados [p=0.2] e {c}uma aba de cada lado. [p=0.3] Ao dobrar, {d}a faixa dá a volta e forma quatro faces, [p=0.2] e {e}as abas fecham as pontas que sobraram."),
    dict(id="s08", block="cubo", text="Qual face fica de frente para qual? [p=0.2] Numere a faixa {a}de um a quatro, de cima para baixo. [p=0.3] Na volta, {b}o um fica de frente para o três, [p=0.2] e {c}o dois, de frente para o quatro. [p=0.3] As abas, {d}cinco e seis, fecham as pontas opostas: [p=0.2] {e}ficam de frente uma para a outra."),
    # cilindro e cone
    dict(id="s09", block="cilindro", text="Agora um corpo redondo: {a}a lata, um cilindro. [p=0.2] Tire as tampas: {b}dois círculos. [p=0.2] Corte a lateral de cima a baixo e desenrole: [p=0.2] {c}ela vira um retângulo, como o rótulo."),
    dict(id="s10", block="cilindro", text="A altura desse retângulo é {a}a altura da lata. [p=0.2] E a largura? [p=0.2] O rótulo dava {b}a volta inteira na tampa. [p=0.2] Então a largura é {c}a volta da circunferência: dois pi érre, com érre igual ao raio da tampa."),
    dict(id="s11", block="cilindro", text="Uma lata de {a}raio três centímetros e dez de altura, com pi igual a três. [p=0.2] {b}Duas vezes pi, que é três, vezes o raio, que também é três, dá dezoito. [p=0.2] O rótulo é {c}um retângulo de dezoito centímetros por dez."),
    dict(id="s12", block="cilindro", text="{a}O cone abre num círculo, a base, [p=0.2] e {b}num pedaço de círculo, como um leque. [p=0.3] Já {c}a esfera não tem planificação: [p=0.2] tente abrir {d}uma casca de laranja no plano, e ela rasga ou enruga."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}achar que o rótulo tem a largura da lata. [p=0.2] A pessoa mede a tampa de lado a lado, {b}seis centímetros, o diâmetro, [p=0.2] e desenha um rótulo de seis por dez. [p=0.3] Esse rótulo {c}não cobre nem metade da volta. [p=0.2] A largura certa é {d}a volta toda: dezoito centímetros, o triplo do diâmetro."),
    # atalho
    dict(id="s14", block="atalho", text="E o atalho para o cubo: {a}pula uma. [p=0.3] Numa fileira reta de quadrados do molde, {b}a face oposta é a que vem logo depois da vizinha. [p=0.2] {c}O um com o três. [p=0.2] O dois com o quatro."),
    dict(id="s15", block="atalho", text="Funciona porque {a}cada dobra é um ângulo reto. [p=0.2] Duas dobras {b}somam cento e oitenta graus, [p=0.2] e a face fica {c}virada para o lado contrário. [p=0.3] {d}Não serve para quadrados que não estão na mesma fileira reta, como abas presas em alturas diferentes da faixa. [p=0.2] Aí, lembre: {e}numa faixa de quatro, a aba da esquerda fica de frente para a aba da direita."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um molde de cubo tem {a}uma faixa de quatro quadrados em pé, numerados de um a quatro, de cima para baixo. [p=0.2] {b}O cinco está colado à esquerda do um, [p=0.2] e {c}o seis, à direita do três."),
    dict(id="s17", block="questao", text="{a}Qual face fica de frente para o dois? [p=0.2] {b}E para o cinco? [p=0.3] E mais uma: {c}qual a largura do rótulo de uma lata de raio cinco centímetros, com pi igual a três?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O dois está na faixa. [p=0.2] Pula uma: {a}pula o três e chega no quatro. [p=0.2] {b}O dois fica de frente para o quatro."),
    dict(id="s20", block="resposta", text="O cinco é aba, e não está na mesma fileira do seis. [p=0.2] Mas {a}o cinco fica do lado esquerdo da faixa, e o seis, do lado direito. [p=0.2] Ao dobrar, {b}cada um fecha uma ponta: [p=0.2] {c}o cinco fica de frente para o seis."),
    dict(id="s21", block="resposta", text="O rótulo: {a}duas vezes três vezes cinco dá trinta centímetros de largura. [p=0.2] Pelo triplo do diâmetro, {b}três vezes dez dá trinta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}as formas do molde dizem o sólido, [p=0.2] {b}no cubo, pula uma, [p=0.2] e {c}a lateral do cilindro é um retângulo da largura da volta."),
    dict(id="s23", block="fim", text="Na próxima aula, você olha os sólidos {a}de frente e de cima, como numa planta de casa, [p=0.2] e descobre {b}qual sombra cada um faz no chão. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
