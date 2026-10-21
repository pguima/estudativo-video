# Roteiro — Redação ENEM, Leitura da Proposta, Episódio 2 de 6: A frase temática bloco a bloco (aula para iniciantes)
# Base: Estudos/Enem/estudos/06-redacao/01-leitura-da-proposta.html — seções 04 e 05 + Questões 5 e 7 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   ENDEREÇO (da série): cada bloco da frase temática é uma parte do endereço; esqueceu uma, a entrega falha.
#   PORTA: o foco é escolher por qual porta entrar na casa certa; você escolhe a porta, mas não troca de endereço.
# "Núcleo" e "delimitador" são nomes de MÉTODO DE ESTUDO (o material avisa: não são termos da Cartilha).
# A tabela das expressões de abertura é "leitura de estudo", não regra oficial (dito na cena 17).
# Eu faço → nós fazemos → você faz: 2023 no rascunho (10–14) → 2017 (29–31) → Questões 5 e 7 (36–43).
# A divisão do tema de 2017 em blocos e a pergunta-problema dele aplicam o método do material (não são texto oficial).
# Frases-chave (meio e fim, idênticas):
#   1. Cada bloco é uma exigência.
#   2. Escolha a porta, não troque de endereço.
#   3. Transforme o tema em pergunta; a tese é a resposta.
# Cores: azul = núcleo/tema · verde = delimitadores e método · amarelo = armadilha · vermelho = erro · roxo = regra oficial.

TITULO = "A frase temática bloco a bloco: núcleo, delimitadores e foco — Redação ENEM, episódio 2"

# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase "
            "forte às palavras-chave. Quando pensar em voz alta no rascunho, soe como quem está raciocinando de verdade. "
            "Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, "
            "exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}A Cartilha do ENEM diz que a redação precisa abordar *todos os elementos* da frase temática. [p=0.5] "
        "{b}Quase ninguém confere isso, [p=0.3] {c}e é assim que bons textos *perdem pontos* [p=0.2] sem perceber."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *desmontar* qualquer frase temática em blocos, [p=0.4] {b}saber o que "
        "cada bloco *obriga* você a discutir, [p=0.4] {c}e transformar o tema numa *pergunta.*"),
    dict(id="03", block="caneta", text=
        "{t}Antes de começar, [p=0.2] pegue *papel* e *caneta.* [p=0.4] {a}E se tiver, [p=0.2] *duas canetas de cores "
        "diferentes.* [p=0.4] {b}Hoje a gente vai sublinhar bastante."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="04", block="prereq", text=
        "{t}Lembrando o episódio um, [p=0.2] em trinta segundos. [p=0.3] {a}A frase temática é um *endereço de entrega "
        "completo.* [p=0.4] {b}O *assunto* é a cidade: [p=0.2] a área ampla. [p=0.3] {c}O *tema* é o endereço inteiro, "
        "[p=0.2] o recorte que a prova dá. [p=0.3] {d}E a *tese* é o que vai dentro da caixa: [p=0.2] a sua posição."),

    # ================= BLOCO A: NÚCLEO E DELIMITADORES =================
    dict(id="05", block="etiqueta", text=
        "{t}Agora, uma pergunta: [p=0.2] por que um endereço tem *tantas partes?* [p=0.4] {a}Olhe a etiqueta de uma "
        "encomenda. [p=0.3] {b}A *cidade* diz a região. [p=0.3] {c}O *bairro* aperta o cerco. [p=0.3] {d}A *rua* "
        "aperta mais. [p=0.3] {e}E o *número* diz a porta exata. [p=0.4] {f}Cada parte tem uma função. [p=0.3] "
        "*Esqueceu uma, [p=0.2] a entrega falha.*"),
    dict(id="06", block="etiqueta", text=
        "{t}A frase temática funciona igualzinho. [p=0.3] {a}Ela é feita de *blocos.* [p=0.3] {b}E cada bloco é uma "
        "parte do endereço."),
    dict(id="07", block="nucleo", text=
        "{t}O bloco principal tem um nome: [p=0.2] *núcleo.* [p=0.4] {a}O núcleo é a palavra que *nomeia o assunto.* "
        "[p=0.4] {b}Por exemplo: [p=0.2] envelhecimento, [p=0.2] cinema, [p=0.2] registro civil. [p=0.4] {c}Um aviso: "
        "[p=0.2] núcleo é um nome de *método de estudo.* [p=0.2] Não é um termo da Cartilha."),
    dict(id="08", block="nucleo", text=
        "{t}E o resto da frase? [p=0.3] {a}São os *delimitadores:* [p=0.2] tudo o que *restringe* o núcleo, [p=0.2] "
        "{b}como o bairro, a rua e o número restringem a cidade. [p=0.4] {c}Também é nome de método, [p=0.2] não da Cartilha."),
    dict(id="09", block="tipos", text=
        "{t}E eles costumam ser de quatro tipos. [p=0.4] {a}O *aspecto:* [p=0.2] estigma, [p=0.2] invisibilidade, "
        "[p=0.2] acesso. [p=0.4] {b}O *grupo:* [p=0.2] surdos, [p=0.2] mulher, [p=0.2] povos tradicionais. [p=0.4] "
        "{c}O *lugar:* [p=0.2] no Brasil. [p=0.4] {d}E a *orientação da discussão:* [p=0.2] desafios para, [p=0.2] "
        "caminhos para."),

    # ================= BLOCO B: EU FAÇO — 2023 =================
    dict(id="10", block="eufaco", text=
        "{t}Vou fazer na sua frente, [p=0.2] no rascunho, [p=0.2] com o tema de dois mil e vinte e três. [p=0.4] "
        "{q}Desafios para o enfrentamento da invisibilidade do trabalho de cuidado realizado pela mulher no Brasil. [p=0.5] "
        "{a}Primeiro, [p=0.2] eu procuro o núcleo. [p=0.3] De que assunto essa frase fala? [p=0.4] {b}Do *trabalho de "
        "cuidado.* [p=0.2] Esse vai de azul."),
    dict(id="11", block="eufaco", text=
        "{a}Agora, os delimitadores, [p=0.2] de verde. [p=0.4] {b}*Desafios para o enfrentamento:* [p=0.3] {b2}isso "
        "obriga a discutir os *obstáculos* [p=0.2] e as *saídas* para superá-los."),
    dict(id="12", block="eufaco", text=
        "{a}*Da invisibilidade:* [p=0.3] {a2}esse é o problema. [p=0.2] Um trabalho que *não é reconhecido.*"),
    dict(id="13", block="eufaco", text=
        "{a}*Realizado pela mulher:* [p=0.3] {a2}de *quem* se fala. [p=0.4] {b}*No Brasil:* [p=0.3] {b2}*onde.*"),
    dict(id="14", block="eufaco", text=
        "{t}Pronto: [p=0.2] cinco blocos, [p=0.2] cinco exigências. [p=0.4] {a}Agora imagine um texto sobre trabalho de "
        "cuidado *em geral.* [p=0.3] {b}Sem a invisibilidade, [p=0.2] sem a mulher, [p=0.2] sem o Brasil. [p=0.4] "
        "{c}Ele deixaria *peças do recorte de fora.* [p=0.3] {d}A encomenda não chega."),

    # ================= BLOCO C: AS EXPRESSÕES DE ABERTURA =================
    dict(id="15", block="aberturas", text=
        "{t}E repare no comecinho das frases temáticas. [p=0.3] Ele não está ali à toa. [p=0.4] {a}*Desafios para:* "
        "[p=0.2] apontar obstáculos concretos [p=0.2] e discutir como superá-los. [p=0.5] {b}*Caminhos para combater:* "
        "[p=0.2] reconhecer o problema [p=0.2] e discutir formas de enfrentá-lo."),
    dict(id="16", block="aberturas", text=
        "{a}*Perspectivas acerca de:* [p=0.2] discutir modos de ver [p=0.2] e de lidar com o fenômeno. [p=0.5] "
        "{b}*A persistência de:* [p=0.2] explicar por que o problema *continua* existindo. [p=0.5] {c}*Democratização do "
        "acesso a:* [p=0.2] discutir quem tem [p=0.2] e quem não tem acesso, [p=0.2] e por quê."),
    dict(id="17", block="aberturas", text=
        "{t}Mas atenção: [p=0.2] essa tabela é uma *leitura de estudo.* [p=0.4] {a}Não existe regra oficial [p=0.2] que "
        "obrigue um formato para cada expressão. [p=0.4] {b}Ela serve para uma coisa: [p=0.2] você *não esquecer metade* "
        "do recorte."),

    # ================= BLOCO D: CORES =================
    dict(id="18", block="cores", text=
        "{t}E aqui entram as suas duas canetas. [p=0.4] {a}No caderno de questões, [p=0.2] marque o *núcleo* de uma cor. "
        "[p=0.4] {b}E cada *delimitador* de outra. [p=0.5] {c}Depois, [p=0.2] quando reler o seu texto, [p=0.2] é só "
        "conferir se *todas as marcas* aparecem nele: [p=0.3] {d}com as mesmas palavras, [p=0.2] ou com sinônimos precisos."),

    # ================= BLOCO E: DO TEMA AO FOCO =================
    dict(id="19", block="foco", text=
        "{t}Agora, uma dúvida que muita gente tem: [p=0.3] se o tema é igual para todos, [p=0.2] os textos saem todos "
        "iguais? [p=0.5] {a}Não! [p=0.3] {b}Dentro do tema, [p=0.2] cada um escolhe o seu *foco:* [p=0.3] {c}a parte do "
        "tema que você decide desenvolver, [p=0.2] como as causas, [p=0.2] ou as consequências."),
    dict(id="20", block="foco", text=
        "{t}E a Cartilha recomenda exatamente isso: [p=0.3] {a}refletir sobre o tema [p=0.2] para decidir *como abordá-lo,* "
        "[p=0.3] *qual ponto de vista adotar* [p=0.2] e *como defendê-lo.*"),
    dict(id="21", block="porta", text=
        "{t}Pense assim. [p=0.3] {a}O tema é a *casa certa,* [p=0.2] no endereço certo. [p=0.4] {b}O foco é escolher "
        "*por qual porta* entrar. [p=0.4] {c}Pela frente, [p=0.2] pelos fundos, [p=0.2] pela garagem: [p=0.2] você "
        "escolhe. [p=0.4] {d}Só não pode *trocar de endereço.*"),
    dict(id="22", block="funil", text=
        "{t}Veja o caminho completo, [p=0.2] como um funil, [p=0.2] com o tema de dois mil e vinte. [p=0.4] {a}Em cima, "
        "[p=0.2] o *assunto:* [p=0.2] saúde mental. [p=0.4] {b}Depois, [p=0.2] o *tema:* [p=0.2] o estigma associado às "
        "doenças mentais na sociedade brasileira. [p=0.4] {c}Esses dois, [p=0.2] *a prova te dá.*"),
    dict(id="23", block="funil", text=
        "{t}Agora vem a parte sua. [p=0.3] {a}O *foco* pode ter *dois eixos.* [p=0.3] Eixo é cada linha de argumento que "
        "você escolhe seguir. [p=0.4] {b}Primeiro eixo: [p=0.2] o estigma *afasta as pessoas do tratamento.* [p=0.4] "
        "{c}Segundo eixo: [p=0.2] a *mídia* reforça estereótipos. [p=0.4] {d}E no fundo do funil, [p=0.2] a *tese:* "
        "[p=0.2] a posição que junta esses eixos. [p=0.4] {e}Esses dois, [p=0.2] *você constrói.*"),

    # ================= BLOCO F: FOCO NÃO É CORTE =================
    dict(id="24", block="corte", text=
        "{t}E aqui mora uma confusão. [p=0.3] {a}Discutir só *duas causas* do estigma das doenças mentais? [p=0.3] "
        "{a2}*Foco legítimo.* [p=0.2] Você entrou por uma porta. [p=0.5] {b}Discutir saúde mental *sem falar de estigma?* "
        "[p=0.3] {b2}Aí você ficou no assunto amplo. [p=0.2] *Trocou de endereço.*"),
    dict(id="25", block="corte", text=
        "{t}Isso tem nome: [p=0.2] *tangenciar,* [p=0.2] que é passar raspando pelo tema, [p=0.2] ficando só no assunto "
        "amplo. [p=0.4] {a}Então guarde: [p=0.2] escolher eixos *é permitido.* [p=0.3] {b}Tirar um bloco da frase "
        "temática, *não é.* [p=0.4] {c}Escolher um foco não é tangenciar."),

    # ================= BLOCO G: A PERGUNTA-PROBLEMA =================
    dict(id="26", block="pergunta", text=
        "{t}E como prender o seu texto no endereço certo? [p=0.4] {a}Com uma *pergunta-problema:* [p=0.3] a frase "
        "temática reescrita *como pergunta.* [p=0.5] {b}Olha só: [p=0.2] por que o estigma associado às doenças mentais "
        "persiste na sociedade brasileira, [p=0.2] e como enfrentá-lo?"),
    dict(id="27", block="pergunta", text=
        "{t}E repare como o texto inteiro sai dessa pergunta. [p=0.4] {a}A *tese* é a *resposta* a ela. [p=0.4] "
        "{b}O *desenvolvimento,* [p=0.2] que são os parágrafos do meio, [p=0.2] traz as *razões* dessa resposta."),
    dict(id="28", block="pergunta", text=
        "{a}E a *conclusão,* [p=0.2] o último parágrafo, [p=0.2] traz a *proposta:* [p=0.2] o que fazer com o problema."),

    # ================= NÓS FAZEMOS — 2017 =================
    dict(id="29", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Tema de dois mil e dezessete: [p=0.3] {b}*Desafios para a formação educacional de surdos "
        "no Brasil.* [p=0.4] {c}Pause o vídeo. [p=0.2] Divida em blocos, [p=0.2] com as duas cores, [p=0.3] {d}e escreva "
        "a pergunta-problema. [p=2.0]"),
    dict(id="30", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}O núcleo, [p=0.2] de azul: [p=0.2] *formação educacional.* [p=0.4] {b}De verde: "
        "[p=0.2] *desafios para,* [p=0.2] a orientação. [p=0.3] {c}*De surdos,* [p=0.2] o grupo. [p=0.3] {d}*No Brasil,* "
        "[p=0.2] o lugar."),
    dict(id="31", block="exercicio", text=
        "{t}E uma pergunta-problema possível: [p=0.3] {a}quais obstáculos dificultam a formação educacional de surdos no "
        "Brasil, [p=0.2] e como superá-los? [p=0.5] {b}Repare: [p=0.2] *todos* os blocos estão dentro dela."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="32", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] cada bloco é uma exigência. [p=0.5] {b}Dois: [p=0.2] "
        "escolha a porta, [p=0.2] não troque de endereço. [p=0.5] {c}Três: [p=0.2] transforme o tema em pergunta; [p=0.2] "
        "a tese é a resposta."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="33", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] ler só o *núcleo* [p=0.2] e esquecer os "
        "delimitadores. [p=0.4] {b}Parece certo, [p=0.2] porque o núcleo é a palavra mais forte da frase. [p=0.4] "
        "{c}Mas cada delimitador é uma parte do endereço. [p=0.2] *Sublinhe todos.*"),
    dict(id="34", block="erros", text=
        "{a}Segundo: [p=0.2] achar que *no Brasil* é enfeite. [p=0.4] {b}Parece certo, [p=0.2] porque quase todo tema "
        "termina assim. [p=0.4] {c}Mas no Brasil é *exigência:* [p=0.2] o seu texto tem que falar da realidade daqui."),
    dict(id="35", block="erros", text=
        "{a}Terceiro: [p=0.2] confundir escolher um foco [p=0.2] com tangenciar. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "nos dois casos você não fala de tudo. [p=0.4] {c}Mas o foco escolhe a *porta,* [p=0.2] e mantém *todos os "
        "blocos.* [p=0.2] Tangenciar é sair do endereço."),

    # ================= QUESTÃO 5 =================
    dict(id="36", block="q5", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.4] {a}O tema do ENEM de dois mil e dezesseis foi: [p=0.3] {b}Caminhos "
        "para combater a intolerância religiosa no Brasil. [p=0.4] {c}Primeiro, [p=0.2] os blocos: [p=0.2] o núcleo, "
        "[p=0.2] *intolerância religiosa.* [p=0.3] {d}A orientação, [p=0.2] *caminhos para combater.* [p=0.3] {e}O lugar, "
        "[p=0.2] *no Brasil.* [p=0.4] {f}O planejamento que atende ao recorte completo desse tema é:"),
    dict(id="37", block="q5", text=
        "{a}A: [p=0.2] introdução sobre a origem das grandes religiões; [p=0.2] desenvolvimento descrevendo as crenças de "
        "cada uma; [p=0.2] conclusão sobre a importância da fé. [p=0.5] {b}B: [p=0.2] introdução sobre a intolerância em "
        "geral; [p=0.2] desenvolvimento sobre preconceito racial e polarização política; [p=0.2] conclusão pedindo mais "
        "respeito entre as pessoas. [p=0.5] {c}C: [p=0.2] introdução com a garantia constitucional da liberdade de crença; "
        "[p=0.2] desenvolvimento sobre a desinformação acerca das religiões de matriz africana [p=0.2] e a impunidade dos "
        "ataques a templos no país; [p=0.2] conclusão com ações de educação e de responsabilização."),
    dict(id="38", block="q5", text=
        "{d}D: [p=0.2] introdução sobre as guerras religiosas na Europa; [p=0.2] desenvolvimento sobre conflitos religiosos "
        "no Oriente Médio; [p=0.2] conclusão sobre a paz mundial. [p=0.5] {e}E: [p=0.2] relato, do início ao fim, da "
        "história de uma família vítima de intolerância, [p=0.2] sem defesa de ponto de vista. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="39", block="q5", text=
        "{t}Vamos conferir bloco por bloco. [p=0.3] {xa}A fala de religiões, [p=0.2] mas não discute a intolerância, "
        "[p=0.2] nem como combatê-la. [p=0.4] {xb}A B amplia para a intolerância *em geral:* [p=0.2] perdeu o religiosa. "
        "[p=0.4] {xd}A D tira o *Brasil.* [p=0.4] {xe}E a E só conta uma história, [p=0.2] sem defender ponto de vista. "
        "[p=0.5] {ok}Sobra a *C:* [p=0.2] intolerância religiosa, [p=0.2] no país, [p=0.2] e ações para combater. [p=0.3] "
        "*Todos os blocos!*"),

    # ================= QUESTÃO 7 =================
    dict(id="40", block="q7", text=
        "{t}Próxima. [p=0.3] {a}Para o tema de dois mil e vinte e três, [p=0.2] aquele do trabalho de cuidado, [p=0.3] "
        "{b}uma estudante planejou discutir só dois aspectos: [p=0.3] {c}a herança de uma divisão de tarefas que atribui o "
        "cuidado às mulheres [p=0.3] {d}e a falta de políticas públicas, [p=0.2] como creches e serviços de apoio a idosos, "
        "[p=0.2] que dividam esse trabalho. [p=0.4] {e}Sua tese menciona o trabalho de cuidado, [p=0.2] a mulher, [p=0.2] "
        "a invisibilidade e o Brasil. [p=0.4] {f}Sobre esse planejamento, é correto afirmar que:"),
    dict(id="41", block="q7", text=
        "{a}A: [p=0.2] tangencia o tema, [p=0.2] pois deixa de fora outros aspectos possíveis do trabalho de cuidado. "
        "[p=0.5] {b}B: [p=0.2] foge ao tema, [p=0.2] pois creches e serviços de apoio a idosos são assuntos de outra área. "
        "[p=0.5] {c}C: [p=0.2] só atenderia ao tema se comentasse, um a um, [p=0.2] todos os textos motivadores da proposta. "
        "[p=0.5] {d}D: [p=0.2] tangencia o tema, [p=0.2] pois a frase temática fala em desafios, [p=0.2] e não em políticas "
        "públicas. [p=0.5] {e}E: [p=0.2] é legítimo: [p=0.2] escolher eixos dentro do recorte define o foco do texto, "
        "[p=0.2] sem retirar nenhum bloco da frase temática. [p=0.5] {p}*Pause e tente!* [p=2.0]"),
    dict(id="42", block="q7", text=
        "{t}Confira os blocos na tese dela: [p=0.3] {k1}trabalho de cuidado, [p=0.2] {k2}mulher, [p=0.2] {k3}invisibilidade, "
        "[p=0.2] {k4}Brasil. [p=0.2] {k5}E os desafios aparecem na falta de políticas. [p=0.3] Está *tudo* lá. [p=0.4] "
        "{xa}A A confunde foco com corte: [p=0.2] ela escolheu uma porta, [p=0.2] e isso é permitido. [p=0.4] {xb}A B diz "
        "que ela fugiu, [p=0.2] que é falar de outro assunto. [p=0.2] Mas creche divide o trabalho de cuidado!"),
    dict(id="43", block="q7", text=
        "{xc}A C inventa uma exigência: [p=0.2] os textos de apoio orientam, [p=0.2] não precisam ser comentados um a um. "
        "[p=0.4] {xd}A D separa coisas que andam juntas: [p=0.2] a falta de políticas *é* um dos desafios. [p=0.5] "
        "{ok}*Letra E!* [p=0.3] Ela escolheu a porta, [p=0.2] e não trocou de endereço."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="44", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] cada bloco é uma exigência. [p=0.5] {b}Dois: "
        "[p=0.2] escolha a porta, [p=0.2] não troque de endereço. [p=0.5] {c}Três: [p=0.2] transforme o tema em pergunta; "
        "[p=0.2] a tese é a resposta."),

    # ================= PONTE E CTA =================
    dict(id="45", block="ponte", text=
        "{a}Além da frase temática, [p=0.2] a prova te dá vários textos. [p=0.4] {b}Eles ajudam muito, [p=0.3] {c}mas se "
        "você copiar uma linha, [p=0.2] ela simplesmente *deixa de existir* para o corretor. [p=0.5] {d}Próximo episódio: "
        "[p=0.2] *textos motivadores e o risco da cópia.*"),
    dict(id="46", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual foi a sua pergunta-problema para o tema de dois mil e dezessete? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
