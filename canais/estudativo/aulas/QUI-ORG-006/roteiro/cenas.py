# Estudativo · QUI-ORG-006 — Álcool, fenol e éter (Química · Química Orgânica · Funções orgânicas).
# Habilidade: reconhecer pelo oxigênio de ligações simples se a molécula é álcool, fenol ou éter e nomear o etanol e o metoxietano.
# Pré-requisitos: QUI-ORG-003 (prefixo, infixo, sufixo; benzeno). Próxima: QUI-ORG-007 (aldeído e cetona; etanal e propanona).
# Marcas: {cue} animação · [p=0.2] pausa. Nomes falados: propan-1-ol = "propan um ol"; propan-2-ol = "propan dois ol".
# Primeira aula do módulo Funções orgânicas: o visual.py acrescenta a linguagem do grupo funcional.
# Fatos: propan-2-ol = álcool isopropílico (limpeza de eletrônicos); fenol C6H5OH, desinfetante de Lister (séc. XIX), tóxico;
# etoxietano = éter etílico (anestésico); álcool benzílico C6H5–CH2–OH é álcool, não fenol.
# Questão: propan-1-ol (álcool), p-cresol (fenol), CH3–O–CH2–CH2–CH3 = metoxipropano (éter). Questão inédita, criada para esta aula.

TITULO = "Álcool, fenol e éter"

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
    dict(id="s01", block="gancho", text="{a}O álcool da farmácia, [p=0.1] {b}um desinfetante antigo de hospital [p=0.1] {c}e o éter dos primeiros anestésicos. [p=0.3] {d}Nos três, há um oxigênio preso só por ligações simples. [p=0.2] {e}O que muda é quem está do lado dele."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai olhar os vizinhos do oxigênio [p=0.1] e dizer {b}se é álcool, fenol ou éter, [p=0.2] e ainda dar nome ao {c}etanol [p=0.1] e ao {d}metoxietano."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula passada: [p=0.2] {a}o nome tem prefixo, infixo e sufixo, [p=0.1] {b}como em etano: dois carbonos, só simples. [p=0.2] {c}E o anel aromático de seis carbonos é o benzeno."),
    # função orgânica
    dict(id="s04", block="funcao", text="{a}Função orgânica é uma família de compostos que têm o mesmo pedaço, [p=0.1] {b}o grupo funcional. [p=0.2] {c}Quem tem o mesmo grupo se comporta de um jeito parecido. [p=0.3] {d}Os três grupos de hoje têm um oxigênio [p=0.1] {e}com duas ligações simples."),
    # álcool
    dict(id="s05", block="alcool", text="{a}Primeiro, o álcool: [p=0.1] um ó agá preso a um carbono de cadeia [p=0.1] {b}que só faz ligações simples. [p=0.3] {c}O nome troca o ó do fim por ol. [p=0.2] {d}Etano vira etanol: [p=0.1] {e}cê agá três, cê agá dois, ó agá, o álcool comum."),
    dict(id="s06", block="alcool", text="{a}Com três carbonos ou mais, um número diz onde está o ó agá. [p=0.2] {b}No propan um ol, ele fica na ponta. [p=0.2] {c}No propan dois ol, ele fica no meio: [p=0.1] {d}é o álcool isopropílico, usado para limpar telas."),
    # fenol
    dict(id="s07", block="fenol", text="{a}Agora, o fenol: [p=0.1] o ó agá preso direto num carbono do anel aromático, o do benzeno. [p=0.3] {b}O mais simples se chama fenol mesmo: [p=0.1] {c}o benzeno com um ó agá. [p=0.2] {d}Já foi usado para desinfetar salas de cirurgia, e é tóxico."),
    # éter
    dict(id="s08", block="eter", text="{a}E o éter: [p=0.1] o oxigênio entre dois carbonos, sem hidrogênio nele. [p=0.2] {b}Cê agá três, ó, cê agá dois, cê agá três. [p=0.3] {c}Para dar o nome, separe os lados do oxigênio."),
    dict(id="s09", block="eter", text="{a}O lado menor vira o prefixo com óxi: [p=0.1] {b}um carbono, metóxi. [p=0.2] {c}O lado maior leva o nome do hidrocarboneto: [p=0.1] {d}dois carbonos, etano. [p=0.3] {e}Juntando: metoxietano."),
    dict(id="s10", block="eter", text="{a}O éter dos anestésicos tem dois carbonos de cada lado: [p=0.1] {b}etoxietano. [p=0.2] {c}Muita gente chama de éter etílico, ou só de éter."),
    # erro comum
    dict(id="s11", block="erro", text="{a}O erro mais comum é chamar de fenol todo ó agá perto de um anel aromático. [p=0.3] {b}Nesta molécula, o ó agá está num cê agá dois, [p=0.1] e esse cê agá dois é que se prende ao anel. [p=0.2] {c}O carbono do ó agá não é do anel: [p=0.1] {d}isto é um álcool."),
    dict(id="s12", block="erro", text="{a}Fenol, só quando o ó agá encosta no próprio anel aromático."),
    # atalho
    dict(id="s13", block="atalho", text="{a}O atalho: [p=0.1] olhe os dois vizinhos do oxigênio. [p=0.2] {b}Agá e um carbono só com simples, fora do anel aromático: álcool. [p=0.2] {c}Agá e um carbono do anel aromático: fenol. [p=0.2] {d}Carbono e carbono: éter."),
    dict(id="s14", block="atalho", text="{a}Funciona porque o oxigênio faz duas ligações, [p=0.1] e os três grupos só mudam quem ocupa cada uma delas. [p=0.3] {b}Não vale quando o oxigênio tem ligação dupla: [p=0.1] {c}aí é outra família, a da próxima aula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Classifique as três moléculas: [p=0.1] álcool, fenol ou éter? [p=0.2] {b}E dê o nome do éter."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}A primeira tem o ó agá na ponta de uma cadeia: [p=0.1] álcool, o propan um ol. [p=0.2] {b}A segunda tem o ó agá direto no anel: fenol. [p=0.1] O galho de carbono não muda isso. [p=0.2] {c}A terceira tem o oxigênio entre dois carbonos: éter."),
    dict(id="s18", block="resposta", text="{a}O nome do éter: [p=0.1] {b}o lado menor tem um carbono, metóxi; [p=0.2] {c}o maior tem três, propano. [p=0.2] {d}Metoxipropano."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] olhe os vizinhos do oxigênio. [p=0.1] {a}Agá e carbono fora do anel aromático é álcool, com ol. [p=0.2] {b}Agá e anel aromático é fenol. [p=0.2] {c}Carbono dos dois lados é éter, com óxi."),
    dict(id="s20", block="fim", text="Na próxima aula, o oxigênio ganha ligação dupla: [p=0.2] você vai diferenciar {a}aldeído de cetona [p=0.1] e dar nome ao {b}etanal e à {c}propanona, a acetona. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
