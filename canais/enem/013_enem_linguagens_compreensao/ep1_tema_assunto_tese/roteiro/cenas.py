# Roteiro — Compreensão Global e Tese, Episódio 1: Tema, assunto e tese (aula para iniciantes)
# Base: Estudos/Enem/estudos/05-linguagens/01-compreensao-global-tese.html — seções 02 e 03 + Questão 1 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   BIBLIOTECA: prateleira = tema (Educação) · livro = assunto (celular na escola) · frase para levar para casa = tese.
#   MESA: tampo = tese · pernas = argumentos e exemplos. Tira uma perna: balança, mas fica de pé. Tira o tampo: não sobra mesa.
# Sequência eu faço → nós fazemos → você faz: mapa do texto do celular (cena 23) → "assunto ou tese?" (15–16) → Questão 1 (33–38).
# Frases-chave (meio e fim, idênticas):
#   1. Assunto é sobre o que fala; tese é o que diz.
#   2. Se ninguém pode discordar, ainda não é a tese.
#   3. Apague a frase: se o texto perde o rumo, ela é central.
# Cores: azul = tese/definição · verde = pista/palavra-sinal · amarelo = armadilha · vermelho = erro · roxo = regra.
# Textos-base (tabela da seção 02, mapa da seção 03, Questão 1) lidos EXATAMENTE como no material.
# Leitura da Questão 1: texto inteiro fixo na tela; marca-texto acompanha cada frase ({f1}…{f5});
# os comentários ({c1}…{c5}) aparecem como notas na margem, sem tirar o texto da tela.

TITULO = "Assunto Não É Tese: Interpretação de Texto do Zero | Interpretação Ep. 1"
PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Dois textos falam do *mesmo assunto* [p=0.2] e defendem coisas *opostas.* [p=0.5] {b}Se você só sabe dizer *sobre o que* "
        "o texto fala, [p=0.3] {c}o ENEM monta uma alternativa com todas as palavras do texto, [p=0.3] {d}e você erra. [p=0.5] "
        "{e}Hoje você aprende a diferença."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai separar o *assunto* da *tese* de qualquer texto, [p=0.3] {b}e saber o que é *central* "
        "[p=0.2] e o que é só *apoio.* [p=0.4] {c}Calma: [p=0.2] cada uma dessas palavras vai ser explicada."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}E você não precisa saber nada antes. [p=0.3] {a}Nenhuma regra de gramática. [p=0.4] "
        "{b}Se você acompanha uma discussão no grupo da família, [p=0.2] já tem tudo o que precisa."),

    # ================= BLOCO A: OS TRÊS NÍVEIS =================
    dict(id="04", block="familia", text=
        "{t}Aliás, [p=0.2] imagine uma discussão no grupo da família. [p=0.3] {a}Sua tia escreve: [p=0.2] "
        "celular na escola tem que ser proibido! [p=0.4] {b}Seu primo responde: [p=0.2] a escola tem que ensinar a usar. [p=0.4] "
        "{c}Os dois falam da mesma coisa? [p=0.3] Falam. [p=0.4] {d}Dizem a mesma coisa? [p=0.3] *De jeito nenhum.*"),
    dict(id="05", block="biblioteca", text=
        "{t}Então, como separar o que um texto *fala* do que ele *diz?* [p=0.4] {a}Imagine uma biblioteca. [p=0.3] "
        "{b}Você vai até uma *prateleira:* [p=0.2] Educação. [p=0.4] {c}Escolhe um *livro:* [p=0.2] celular na escola. [p=0.4] "
        "{d}E no livro há *uma frase* que o autor quer que você leve para casa: [p=0.3] a escola deve ensinar a usar o celular, "
        "[p=0.2] não só proibir."),
    dict(id="06", block="biblioteca", text=
        "{t}Esses três degraus têm nome. [p=0.3] {a}A prateleira é o *tema:* [p=0.2] a área ampla onde o texto está. "
        "[p=0.4] {b}Educação, [p=0.2] cidade, [p=0.2] consumo, [p=0.2] trabalho."),
    dict(id="07", block="biblioteca", text=
        "{a}O livro que você escolheu é o *assunto:* [p=0.2] o pedaço específico de que o texto trata. [p=0.4] "
        "{b}Não é educação em geral. [p=0.2] É o *celular na sala de aula.*"),
    dict(id="08", block="biblioteca", text=
        "{a}E a frase para levar para casa é a *tese:* [p=0.2] o que o texto *afirma* sobre o assunto. [p=0.4] "
        "{b}A escola deve ensinar a usar o celular, [p=0.2] não só proibir."),
    dict(id="09", block="tabela", text=
        "{t}Veja os três degraus em três exemplos. [p=0.3] {a}Tema: [p=0.2] educação. [p=0.2] Assunto: [p=0.2] celular na sala de aula. "
        "[p=0.2] Tese: [p=0.2] A escola deve ensinar a usar o celular, [p=0.2] não só proibi-lo. [p=0.5] "
        "{b}Tema: [p=0.2] cidade. [p=0.2] Assunto: [p=0.2] feiras livres, [p=0.2] aquelas feiras de rua. [p=0.2] Tese: [p=0.2] "
        "A feira deve continuar na rua, [p=0.2] porque é espaço de encontro e de venda direta. [p=0.5] "
        "{c}Tema: [p=0.2] consumo. [p=0.2] Assunto: [p=0.2] roupas muito baratas. [p=0.2] Tese: [p=0.2] "
        "O preço baixo esconde custos pagos por quem não estava na loja. [p=0.5] {d}Repare: [p=0.2] só a última coluna "
        "*diz* alguma coisa."),

    # ================= BLOCO B: TESTE DA DISCORDÂNCIA =================
    dict(id="10", block="futebol", text=
        "{t}Mas como ter certeza de que você achou a tese, [p=0.2] e não o assunto? [p=0.4] {a}Pense em dois amigos falando de futebol. "
        "[p=0.3] {b}Um diz: [p=0.2] o meu time. [p=0.3] Não tem o que discordar. [p=0.4] "
        "{c}Agora ele diz: [p=0.2] o meu time vai ser campeão este ano. [p=0.4] {d}Pronto: [p=0.2] *já dá briga.*"),
    dict(id="11", block="discordancia", text=
        "{t}Isso é o *teste da discordância.* [p=0.4] {a}A tese tem *verbo,* [p=0.2] a palavra que diz o que é ou o que deve ser, "
        "[p=0.2] como deve, [p=0.2] vai ser. [p=0.4] {b}E tem *posição:* [p=0.2] alguém poderia discordar dela. [p=0.4] "
        "{c}O assunto cabe na *etiqueta de uma pasta:* [p=0.2] celular na escola. [p=0.4] "
        "{d}*Se ninguém pode discordar, ainda não é a tese.*"),

    # ================= BLOCO C: MESMO ASSUNTO, TESES OPOSTAS =================
    dict(id="12", block="opostas", text=
        "{t}E por que essa diferença derruba tanta gente na prova? [p=0.4] {a}Imagine dois artigos sobre celular na escola. [p=0.3] "
        "{b}Um defende a *proibição total.* [p=0.3] {c}O outro defende o *uso orientado:* [p=0.2] o professor ensinando a usar. "
        "[p=0.4] {d}*Mesmo assunto. [p=0.2] Teses opostas.*"),
    dict(id="13", block="opostas", text=
        "{t}Agora pense como quem monta a prova. [p=0.3] {a}O texto defende o uso orientado. [p=0.3] {b}Basta escrever uma alternativa "
        "com as mesmas palavras, [p=0.2] celular, [p=0.2] escola, [p=0.2] aluno, [p=0.3] {c}defendendo a proibição. [p=0.4] "
        "{d}*Assunto certo, tese errada.* [p=0.3] {e}Quem confere só as palavras, [p=0.2] cai."),

    # ================= BLOCO D: NOMENCLATURA =================
    dict(id="14", block="nomes", text=
        "{t}Uma observação rápida. [p=0.3] {a}Muitos livros, [p=0.2] e até a Redação do ENEM, "
        "[p=0.2] chamam de *tema* o que aqui chamamos de assunto. [p=0.4] "
        "{b}Não se prenda ao nome. [p=0.3] {c}O que importa é não confundir *sobre o que o texto fala* [p=0.2] com *o que ele diz.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Agora é com você. [p=0.3] Vou mostrar três frases. [p=0.3] {a}Para cada uma, [p=0.2] *pause o vídeo e diga:* "
        "[p=0.2] é assunto ou tese? [p=0.4] {b}Dica: [p=0.2] faça o teste da discordância. [p=0.4] {c}Primeira: [p=0.2] "
        "o transporte público. [p=0.5] {d}Segunda: [p=0.2] o transporte público deveria ser gratuito para estudantes. [p=0.5] "
        "{e}Terceira: [p=0.2] a violência no futebol. [p=1.5]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}O transporte público: [p=0.2] dá para discordar? [p=0.2] Não. [p=0.2] Cabe numa etiqueta. "
        "[p=0.2] *Assunto.* [p=0.4] {b}Deveria ser gratuito para estudantes: [p=0.2] tem verbo, [p=0.2] tem posição, [p=0.2] "
        "e muita gente discordaria. [p=0.2] *Tese.* [p=0.4] {c}A violência no futebol: [p=0.2] outra etiqueta. [p=0.2] *Assunto.*"),

    # ================= BLOCO E: IDEIA CENTRAL × SECUNDÁRIAS =================
    dict(id="17", block="restaurante", text=
        "{t}E o resto do texto, [p=0.2] serve para quê? [p=0.4] "
        "{a}Pense numa avaliação de restaurante na internet. [p=0.3] {b}Não volto mais. [p=0.4] {c}A comida chegou fria. [p=0.2] "
        "Esperei uma hora. [p=0.4] {d}Uma frase manda. [p=0.2] As outras *explicam por quê.*"),
    dict(id="18", block="restaurante", text=
        "{t}A frase que manda é a *ideia central:* [p=0.2] a ideia que organiza todas as outras. [p=0.4] "
        "{a}Aqui, [p=0.2] não volto mais."),
    dict(id="19", block="tipos", text=
        "{t}E nos textos da prova? [p=0.3] {a}Num *texto argumentativo,* [p=0.2] "
        "o texto que defende uma opinião, [p=0.2] como um artigo de jornal, [p=0.3] {b}a ideia central é a *tese.*"),
    dict(id="20", block="tipos", text=
        "{a}Num *texto expositivo,* [p=0.2] o que só informa, [p=0.2] como uma notícia, [p=0.3] "
        "{b}a ideia central é a *informação principal.* [p=0.4] {c}Hoje, o foco é o argumentativo."),
    dict(id="21", block="mesa", text=
        "{t}E as outras frases? [p=0.3] {a}São as *ideias secundárias:* [p=0.2] as que estão no texto para *sustentar* a central. "
        "[p=0.4] {b}Pense numa mesa. [p=0.3] {c}A tese é o *tampo.* [p=0.3] {d}O que sustenta a tese são as *pernas.*"),
    dict(id="22", block="mesa", text=
        "{t}E que pernas são essas? [p=0.3] {a}A primeira é o *argumento:* [p=0.2] um motivo para acreditar na tese. "
        "[p=0.3] Ele responde: [p=0.2] por quê? [p=0.4] {b}A segunda é o *exemplo:* [p=0.2] ele responde: [p=0.2] onde isso se vê?"),
    dict(id="23", block="mesa", text=
        "{t}Veja a mesa montada, [p=0.2] num texto sobre celular na escola. [p=0.3] {tese}No tampo, [p=0.2] a tese: [p=0.2] "
        "A escola deve ensinar a usar o celular, [p=0.2] não só proibi-lo. [p=0.4] {p1}Primeira perna: [p=0.2] faz parte da vida "
        "dos estudantes. [p=0.2] {e1}Exemplo: [p=0.2] fora da escola, [p=0.2] ninguém proíbe. [p=0.4] {p2}Segunda: [p=0.2] proibir não gera "
        "*autocontrole,* [p=0.2] que é saber se controlar sozinho. [p=0.2] {e2}Exemplo: [p=0.2] o aluno usa às escondidas. [p=0.4] "
        "{p3}Terceira: [p=0.2] pode servir como ferramenta de aula. [p=0.2] {e3}Exemplo: [p=0.2] aula de checagem de notícias falsas. "
        "[p=0.4] {x}Tudo embaixo do tampo, [p=0.2] *a serviço da tese.*"),
    dict(id="24", block="concessao", text=
        "{t}Uma perna engana muita gente. [p=0.3] {a}O autor dá um pouco de razão ao outro lado: [p=0.3] "
        "{b}é verdade que o celular distrai, [p=0.2] *mas* proibir não ensina nada. [p=0.4] {c}Isso é uma *concessão:* [p=0.2] "
        "reconhecer um ponto do outro lado, [p=0.2] antes de voltar à própria posição. [p=0.4] {d}E o mas é uma *palavra-sinal:* "
        "[p=0.2] avisa que a posição do autor vem depois."),
    dict(id="25", block="apoios", text=
        "{t}Juntando tudo: [p=0.3] {a}argumentos, [p=0.2] exemplos, [p=0.2] dados, que são números, [p=0.2] relatos, "
        "que são histórias, [p=0.2] e concessões. [p=0.4] {b}Tudo isso *sustenta* a tese. [p=0.3] {c}Nada disso *substitui* a tese."),

    # ================= BLOCO F: TESTE DO APAGAMENTO =================
    dict(id="26", block="apagamento", text=
        "{t}E na prova, como saber se uma frase é tampo ou perna? [p=0.4] {a}Faça o *teste do apagamento:* [p=0.2] "
        "apague a frase na sua cabeça. [p=0.4] {b}Apague o exemplo do aluno que usa às escondidas. [p=0.3] "
        "{c}A mesa *balança,* [p=0.2] mas fica de pé. [p=0.2] Era perna. [p=0.4] {d}Agora apague a tese. [p=0.3] "
        "{e}As pernas ficam soltas. [p=0.2] *Não sobra mesa.*"),
    dict(id="27", block="apagamento", text=
        "{a}Guarde a regra: [p=0.2] *apague a frase: [p=0.2] se o texto perde o rumo, ela é central.* [p=0.4] "
        "{b}Se perde só um apoio, [p=0.2] ela é secundária."),

    # ================= BLOCO G: A FRASE MAIS MARCANTE =================
    dict(id="28", block="marcante", text=
        "{t}E a frase que mais chama a atenção? [p=0.2] É a central? [p=0.4] {a}Imagine que o texto do celular traga um dado "
        "assustador: [p=0.2] tem aluno que olha o celular cem vezes por aula. [p=0.4] {b}Apague. [p=0.2] A tese continua de pé. [p=0.4] "
        "{c}O dado impressionante, [p=0.2] a história comovente: [p=0.2] *quase sempre são perna, [p=0.2] não tampo.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="29", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] assunto é sobre o que fala; [p=0.2] tese é o que diz. [p=0.5] "
        "{b}Dois: [p=0.2] se ninguém pode discordar, [p=0.2] ainda não é a tese. [p=0.5] {c}Três: [p=0.2] apague a frase: "
        "[p=0.2] se o texto perde o rumo, [p=0.2] ela é central."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="30", block="erros", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] a questão pede a tese, [p=0.2] e você responde "
        "com o assunto. [p=0.4] {b}Parece certo, [p=0.2] porque a alternativa fala daquilo que o texto fala. [p=0.4] "
        "{c}Mas faça o teste: [p=0.2] *tem verbo e posição?* [p=0.2] Se não tem, [p=0.2] é só etiqueta."),
    dict(id="31", block="erros", text=
        "{a}Segundo: [p=0.2] escolher o exemplo mais marcante como ideia central. [p=0.4] {b}Parece certo, [p=0.2] porque é o trecho "
        "que ficou na sua cabeça. [p=0.4] {c}Mas apague o exemplo: [p=0.2] a mesa fica de pé. [p=0.2] *Era perna.*"),
    dict(id="32", block="erros", text=
        "{a}Terceiro: [p=0.2] ficar com a alternativa que repete as palavras do texto. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "reconhecer as palavras dá segurança. [p=0.4] {c}Mas confira o que ela *afirma* com essas palavras. "
        "[p=0.3] Pode ser assunto certo [p=0.2] com tese errada."),

    # ================= QUESTÃO 1 (VOCÊ FAZ) =================
    dict(id="33", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.3] {a}Vou ler devagar, [p=0.2] pensando em voz alta. [p=0.4] "
        "{f1}Bibliotecas de bairro não são depósitos de livros velhos. [p=0.4] {c1}Bibliotecas de bairro: [p=0.2] o *assunto.*"),
    dict(id="34", block="questao", text=
        "{f2}Num tempo em que quase tudo se lê na tela, [p=0.2] elas continuam sendo um dos poucos lugares públicos [p=0.2] onde se "
        "pode passar a tarde sem pagar nada [p=0.2] e sem que ninguém pergunte o que você vai consumir. [p=0.4] {c2}Um motivo: "
        "[p=0.2] lugar público e de graça. [p=0.2] *Perna.* [p=0.4] {f3}Quem estuda para concurso encontra ali silêncio; [p=0.2] "
        "quem não tem internet em casa, [p=0.2] conexão; [p=0.2] o aposentado, [p=0.2] jornal e conversa. [p=0.4] "
        "{c3}Três exemplos. [p=0.2] Mais *pernas.*"),
    dict(id="35", block="questao", text=
        "{f4}Fechar uma biblioteca para economizar parece racional na planilha, [p=0.2] *mas* apaga um espaço de convivência "
        "[p=0.2] que nenhum aplicativo substitui. [p=0.5] {c4}Olha o mas! [p=0.3] Antes dele, [p=0.2] uma concessão. [p=0.3] "
        "{c4b}Depois dele, [p=0.2] a posição do autor. [p=0.2] *Essa é a frase do tampo.* [p=0.4] "
        "{f5}Antes de cortar, [p=0.2] as prefeituras deveriam contar quantas pessoas entram por aquela porta. [p=0.4] "
        "{c5}Uma proposta, [p=0.2] que nasce da tese."),
    dict(id="36", block="questao", text=
        "{t}A tese defendida no texto é a de que: [p=0.4] {a}A: [p=0.2] as bibliotecas de bairro deveriam ser substituídas por "
        "aplicativos de leitura, [p=0.2] mais baratos. [p=0.4] {b}B: [p=0.2] a leitura em tela reduziu o interesse da população "
        "pelos livros impressos. [p=0.4] {c}C: [p=0.2] as bibliotecas de bairro têm valor como espaço público de convivência, "
        "[p=0.2] e por isso fechá-las para economizar é um erro. [p=0.4] {d}D: [p=0.2] estudantes que se preparam para concursos "
        "precisam de silêncio para estudar. [p=0.4] {e}E: [p=0.2] as prefeituras gastam demais com cultura [p=0.2] e deveriam rever "
        "seus orçamentos. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="37", block="questao", text=
        "{t}Vamos eliminar. [p=0.3] {a}A: [p=0.2] trocar por aplicativos. [p=0.2] O texto diz o *contrário:* [p=0.2] nenhum aplicativo "
        "substitui. [p=0.4] {d}D: [p=0.2] silêncio para quem estuda. [p=0.2] Está no texto, [p=0.2] mas é *um* exemplo só. [p=0.2] "
        "Uma perna. [p=0.4] {b}B: [p=0.2] o texto cita a tela, [p=0.2] mas não diz que as pessoas perderam "
        "o interesse pelos livros. [p=0.2] Vai *além* do texto."),
    dict(id="38", block="questao", text=
        "{e}E: [p=0.2] usa as palavras do texto, [p=0.2] prefeituras, [p=0.2] cortar. [p=0.3] Mas o texto pede que elas *contem* "
        "antes de cortar, [p=0.2] não que cortem. [p=0.2] Assunto certo, [p=0.2] tese errada. [p=0.4] {c}Sobra a C: [p=0.2] "
        "a frase do mas, [p=0.2] com outras palavras. [p=0.3] {ok}*Letra C.* [p=0.4] {x}No episódio três, [p=0.2] você vai "
        "conhecer os nomes desses tipos de erro."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="39", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] assunto é sobre o que fala; [p=0.2] tese é o que diz. [p=0.5] "
        "{b}Dois: [p=0.2] se ninguém pode discordar, [p=0.2] ainda não é a tese. [p=0.5] {c}Três: [p=0.2] apague a frase: "
        "[p=0.2] se o texto perde o rumo, [p=0.2] ela é central."),

    # ================= PONTE =================
    dict(id="40", block="ponte", text=
        "{a}Uma última ideia: [p=0.2] se você consegue dizer o texto inteiro em *uma única frase,* [p=0.3] "
        "{b}você entendeu o texto. [p=0.5] {c}Próximo episódio: [p=0.2] *o resumo em uma frase.*"),
    dict(id="41", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *Linguagens do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das três frases do exercício você acertou? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
