# Estudativo · FIS-ELE-005 — Condutores: pontas e gaiola de Faraday (Física · Eletricidade · Eletrostática).
# Habilidade: explicar onde a carga fica num condutor, o para-raios e por que o carro protege do raio.
# Pré-requisitos: FIS-ELE-004 (potencial, U = E·d). Próxima: FIS-ELE-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Aula conceitual; questão inédita, criada para esta aula. Corrente elétrica (FIS-ELE-008) não está em "Já ensinado":
# a descarga do raio é chamada de "descarga", sem falar em ampère. O carro protege pela lataria de metal (gaiola de
# Faraday), não pelos pneus. Celular no elevador e tela do micro-ondas: blindagem metálica, citada sem falar em ondas.

TITULO = "Condutores: pontas e gaiola de Faraday"

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
    dict(id="s01", block="gancho", text="{a}Um raio cai num carro na estrada. [p=0.3] {b}Quem está dentro sai sem um arranhão. [p=0.3] E {c}não é por causa dos pneus de borracha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar onde a carga fica num condutor, [p=0.2] {b}como funciona o para-raios [p=0.2] e {c}por que o carro protege do raio."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}num metal, os elétrons andam com facilidade, e cargas de mesmo sinal se repelem; [p=0.3] e {c}no campo uniforme, a tensão é o campo vezes a distância. [p=0.3] Se faltar alguma, procure no canal."),
    # onde a carga fica
    dict(id="s04", block="superficie", text="Ponha {a}carga a mais numa esfera de metal. [p=0.2] As cargas de mesmo sinal {b}se repelem [p=0.1] e se afastam o máximo que podem. [p=0.3] O lugar mais longe possível é {c}a superfície de fora."),
    dict(id="s05", block="superficie", text="Em pouco tempo, as cargas param, [p=0.1] e o condutor fica em {a}equilíbrio. [p=0.3] Aí valem três fatos. [p=0.2] {b}A carga a mais fica toda na superfície de fora. [p=0.2] {c}O campo elétrico lá dentro é zero. [p=0.2] {d}E o potencial é o mesmo em todos os pontos do condutor."),
    dict(id="s06", block="superficie", text="Por que o campo dentro é zero? [p=0.2] {a}Se não fosse, ele empurraria os elétrons, [p=0.1] e eles andariam. [p=0.3] {b}Como estão parados, [p=0.1] {c}o campo lá dentro só pode ser zero. [p=0.3] E com campo zero, {d}a tensão, que é o campo vezes a distância, dá zero: [p=0.1] o potencial não muda de um ponto para outro."),
    # pontas
    dict(id="s07", block="pontas", text="Agora, um condutor com {a}ponta. [p=0.2] {b}A carga se acumula mais nas partes pontudas, [p=0.1] e ali {c}o campo fica muito mais forte. [p=0.3] Esse é o {d}poder das pontas."),
    dict(id="s08", block="pontas", text="O ar é isolante. [p=0.2] Mas, num campo muito forte, {a}ele passa a conduzir, [p=0.1] e {b}a carga escapa numa faísca. [p=0.3] {c}Por isso, as faíscas saltam das pontas."),
    dict(id="s09", block="pontas", text="O {a}para-raios usa isso. [p=0.2] É {b}uma haste de metal pontuda no alto do prédio, [p=0.1] {c}ligada à terra por um cabo grosso. [p=0.3] Na tempestade, {d}a ponta concentra o campo [p=0.1] e oferece ao raio um caminho fácil. [p=0.3] {e}A descarga, que é a carga do raio passando de uma vez, [p=0.1] desce pelo cabo até o chão, e não pelas paredes."),
    # gaiola
    dict(id="s10", block="gaiola", text="E o carro? [p=0.2] Uma caixa de metal fechada funciona como uma {a}gaiola de Faraday. [p=0.2] {b}A carga anda pela superfície de fora, [p=0.1] e {c}lá dentro o campo continua praticamente zero. [p=0.3] Quando o raio cai, {d}a descarga corre pela lataria [p=0.1] e salta para o chão. [p=0.2] {e}Quem está dentro fica protegido."),
    dict(id="s11", block="gaiola", text="A mesma blindagem aparece no dia a dia: [p=0.2] {a}no elevador de metal, onde o celular perde o sinal, [p=0.2] e {b}na tela de metal da porta do micro-ondas. [p=0.3] As ondas desses exemplos são assunto de outra aula."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que são os pneus que isolam o carro. [p=0.3] {b}O raio atravessa centenas de metros de ar, que é isolante. [p=0.2] {c}Alguns centímetros de borracha não seguram isso. [p=0.3] {d}Quem protege é a lataria de metal."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}condutor em equilíbrio tem três respostas prontas. [p=0.3] {b}A carga? Na superfície de fora. [p=0.2] {c}O campo dentro? Zero. [p=0.2] {d}O potencial? Igual em todo ponto. [p=0.3] E {e}o campo é mais forte onde a superfície é mais pontuda."),
    dict(id="s14", block="atalho", text="Funciona porque {a}tudo vem de uma ideia só: [p=0.2] as cargas se repelem e só param quando não sobra força lá dentro. [p=0.3] {b}Não vale para isolantes: [p=0.1] neles, a carga fica onde foi posta."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma esfera oca de metal recebe {a}carga positiva e fica em equilíbrio. [p=0.3] {b}Onde fica a carga? [p=0.2] {c}Quanto vale o campo no centro? [p=0.3] E {d}se a esfera tivesse uma ponta, onde o campo seria mais forte?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}A carga fica na superfície de fora. [p=0.3] {b}O campo no centro, e em todo o lado de dentro, é zero. [p=0.3] {c}E, com uma ponta, o campo seria mais forte na ponta, [p=0.1] {d}onde a carga se acumula."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}no condutor em equilíbrio, a carga fica na superfície de fora [p=0.1] {b}e o campo dentro é zero; [p=0.2] e {c}as pontas concentram a carga, como no para-raios."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai ver {a}o capacitor, [p=0.2] a peça que guarda carga e energia [p=0.1] {b}e solta tudo de uma vez no flash da câmera. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
