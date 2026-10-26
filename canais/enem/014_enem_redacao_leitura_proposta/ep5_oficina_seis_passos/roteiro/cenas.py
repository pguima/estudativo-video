# Roteiro — Redação ENEM, Leitura da Proposta, Episódio 5 de 6: Oficina — a leitura da proposta em 6 passos, do tema até a tese
# Base: Estudos/Enem/estudos/06-redacao/01-leitura-da-proposta.html — seções 09 e 10 + Questões 8 e 9 da seção 12.
#   Gestão do tempo (Planejamento do rascunho) e Introdução só citadas (séries próprias).
# Formato OFICINA: o professor faz tudo ao vivo no rascunho, pensando em voz alta; eu faço → nós fazemos → você faz.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora: os 6 passos são o CHECKLIST DO PILOTO (ninguém decola sem conferir) · da série: a tese precisa
#   chegar ao ENDEREÇO COMPLETO.
# Lidos EXATAMENTE como no material: tabela dos 6 passos ("o que fazer" e "pergunta de controle", cenas 07–09),
#   tabela de blocos de 2021 (12–13), pergunta-problema e tese (15, 18), "repare que a tese..." (19), repertório da
#   Lei nº 9.534/1997 (20), leitura que tangencia e o comentário (21–22), dica do tema difícil (23), Q9 e Q8.
# A 1ª tentativa de tese (cena 16) é do professor, para ser corrigida: falta o bloco "no Brasil". Marcada "tentativa".
# Os textos motivadores de 2021 NÃO estão no material: o passo 3 mostra o método sem inventar o conteúdo deles.
# Frases-chave (meio e fim, idênticas):
#   1. Blocos, pergunta, tese, conferência.
#   2. Tese = posição + dois eixos + todos os blocos.
#   3. Confira antes de desenvolver, não depois.
# Cores: azul = núcleo/tema · verde = delimitadores e método · amarelo = armadilha · vermelho = erro · roxo = regra oficial.

TITULO = "Sua Tese Esqueceu um Bloco? Do Tema à Tese em 6 Passos | Proposta de Redação Ep. 5"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase "
            "forte às palavras-chave. Esta aula é uma oficina: quando escrever no rascunho e conferir a tese, soe como "
            "quem está raciocinando de verdade, em voz alta. Ritmo didático e tranquilo, sem pressa, respeitando as "
            "pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem "
            "repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Hoje você não vai só assistir. [p=0.5] {b}Pegue *papel e caneta:* [p=0.3] {c}vamos ler uma proposta real do "
        "ENEM juntos, [p=0.2] do zero até a tese, [p=0.3] {d}em *seis passos.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai ter um *método* para usar em qualquer proposta [p=0.4] {b}e uma *tese* que cobre o "
        "tema inteiro."),
    dict(id="03", block="material", text=
        "{t}Então, [p=0.2] separe agora: [p=0.3] {a}uma folha, [p=0.2] {b}uma caneta, [p=0.2] {c}e mais *duas cores.* "
        "[p=0.4] {d}Uma cor para o *núcleo,* [p=0.2] a palavra central do tema, [p=0.3] {e}e outra para os "
        "*delimitadores,* [p=0.2] as partes que fecham o recorte. [p=0.4] {f}Pegou? [p=0.3] Então vamos."),
    dict(id="04", block="prereq", text=
        "{t}Antes, [p=0.2] o que você já sabe, em quarenta e cinco segundos. [p=0.4] {a}Episódio dois: [p=0.2] a frase "
        "temática se desmonta em *blocos,* [p=0.2] e cada bloco é uma exigência. [p=0.3] {b}E dá para reescrever o tema como "
        "uma *pergunta-problema.* [p=0.4] {c}Episódio três: [p=0.2] os textos motivadores são GPS: [p=0.2] ajudam a chegar, "
        "[p=0.2] não fazem a entrega. [p=0.4] {d}Episódio quatro: [p=0.2] esquecer um bloco é *tangenciar:* [p=0.2] bairro "
        "certo, [p=0.2] casa errada."),

    # ================= O CHECKLIST DO PILOTO =================
    dict(id="05", block="piloto", text=
        "{t}Agora, [p=0.2] uma pergunta: [p=0.2] o que você confere antes de sair de casa? [p=0.4] {a}Chave, [p=0.2] "
        "{b}carteira, [p=0.2] {c}celular. [p=0.4] {d}O piloto de avião faz igual, [p=0.2] só que por escrito: [p=0.2] "
        "*ninguém decola sem conferir.* [p=0.4] {e}Os seis passos de hoje [p=0.2] são o seu *checklist,* [p=0.2] uma lista "
        "de conferência. [p=0.3] {f}E é uma *sugestão de método,* [p=0.2] não uma regra da prova."),
    dict(id="06", block="passos", text=
        "{t}Cada passo vem com uma *pergunta de controle:* [p=0.3] a pergunta que você faz a si mesmo [p=0.2] para saber se "
        "o passo deu certo. [p=0.4] {g}Como dividir o tempo da prova entre esses passos [p=0.2] vai ter uma série própria."),
    dict(id="07", block="passos", text=
        "{a}Passo um, [p=0.2] *frase temática:* [p=0.2] ler primeiro e copiar no rascunho. [p=0.3] {a2}Controle: [p=0.2] "
        "sei dizer o tema com as palavras da prova? [p=0.5] {b}Passo dois, [p=0.2] *blocos:* [p=0.2] separar núcleo e "
        "delimitadores. [p=0.3] {b2}Controle: [p=0.2] o que cada bloco obriga a discutir?"),
    dict(id="08", block="passos", text=
        "{c}Passo três, [p=0.2] *motivadores:* [p=0.2] ler com os três passos da Cartilha, [p=0.2] anotando na margem. "
        "[p=0.3] {c2}Controle: [p=0.2] qual é a situação-problema? [p=0.5] {d}Passo quatro, [p=0.2] *pergunta-problema:* "
        "[p=0.2] reescrever o tema como pergunta. [p=0.3] {d2}Controle: [p=0.2] a pergunta contém todos os blocos?"),
    dict(id="09", block="passos", text=
        "{e}Passo cinco, [p=0.2] *tese provisória:* [p=0.2] responder à pergunta com uma posição e dois eixos. [p=0.3] "
        "{e3}Tese provisória é a primeira versão da sua tese, [p=0.2] que ainda pode mudar. [p=0.3] {e4}E *eixo* é um "
        "caminho que o desenvolvimento vai seguir. [p=0.3] {e2}Controle: [p=0.2] alguém poderia discordar dela? [p=0.5] "
        "{f}Passo seis, [p=0.2] *conferência:* [p=0.2] pôr a tese ao lado da frase temática. [p=0.3] {f2}Controle: [p=0.2] "
        "algum bloco ficou de fora?"),

    # ================= EU FAÇO: ENEM 2021 =================
    dict(id="10", block="p1", text=
        "{t}Agora, [p=0.2] eu faço, [p=0.2] e você acompanha no seu papel. [p=0.4] {a}Tema do ENEM de dois mil e vinte e um. "
        "[p=0.3] Passo um: [p=0.2] copio no rascunho. [p=0.3] {b}Invisibilidade e registro civil: [p=0.2] garantia de acesso "
        "à cidadania no Brasil. [p=0.5] {c}Sei dizer o tema com as palavras da prova? [p=0.3] Sei. [p=0.2] Passo um, conferido."),
    dict(id="11", block="p2", text=
        "{t}Passo dois: [p=0.2] os blocos. [p=0.3] Pegue as suas cores. [p=0.4] {a}O núcleo é *registro civil.* [p=0.3] "
        "{a2}Obriga a discutir a *certidão de nascimento* e a documentação básica. [p=0.4] {a3}Certidão de nascimento é o "
        "documento que prova que você nasceu, [p=0.2] e quem você é. [p=0.3] {a4}E ela é feita no *cartório,* [p=0.2] o "
        "lugar oficial onde o nascimento é registrado."),
    dict(id="12", block="p2", text=
        "{b}Primeiro delimitador: [p=0.2] *invisibilidade,* [p=0.2] o problema. [p=0.3] {b2}Obriga a discutir pessoas que, "
        "sem registro, [p=0.2] não existem para o Estado. [p=0.5] {c}Segundo: [p=0.2] *garantia de acesso à cidadania,* "
        "[p=0.2] a relação. [p=0.3] {c2}O registro como porta de entrada para direitos: [p=0.2] escola, [p=0.2] saúde, "
        "[p=0.2] benefícios, [p=0.2] voto."),
    dict(id="13", block="p2", text=
        "{d}E o terceiro: [p=0.2] *no Brasil,* [p=0.2] o lugar. [p=0.3] {d2}A realidade brasileira, [p=0.2] e não a de outros "
        "países. [p=0.5] {e}Quatro blocos, [p=0.2] quatro exigências. [p=0.3] Passo dois, conferido."),
    dict(id="14", block="p3", text=
        "{t}Passo três: [p=0.2] os motivadores. [p=0.4] {a}Na prova, [p=0.2] eu leria cada texto com os três passos da "
        "Cartilha, [p=0.2] anotando na margem. [p=0.4] {b}E levaria uma pergunta só: [p=0.2] *qual é a situação-problema?* "
        "[p=0.4] {c}Os textos daquela prova não estão no nosso material, [p=0.2] então eu sigo para o passo quatro."),
    dict(id="15", block="p4", text=
        "{t}Passo quatro: [p=0.2] o tema vira pergunta. [p=0.4] {a}Por que parte da população brasileira ainda vive sem "
        "registro civil, [p=0.2] e o que isso significa para o acesso à cidadania? [p=0.5] {b}Contém todos os blocos? [p=0.3] "
        "{b1}Registro civil, [p=0.2] {b2}tem. [p=0.2] {b3}Sem registro, invisível, [p=0.2] tem. [p=0.2] {b4}Cidadania, [p=0.2] "
        "tem. [p=0.2] {b5}Brasileira, [p=0.2] tem."),

    # ---- passo 5: primeira tentativa (imperfeita) ----
    dict(id="16", block="p5", text=
        "{t}Passo cinco: [p=0.2] a tese provisória. [p=0.3] Vou tentar. [p=0.4] {a}A falta de registro civil torna muitas "
        "pessoas invisíveis para o Estado [p=0.2] e as afasta de direitos básicos, [p=0.2] por causa da distância dos cartórios "
        "e da desinformação. [p=0.5] {b}Alguém poderia discordar? [p=0.3] Poderia. [p=0.2] Tem posição. [p=0.3] {c}Parece "
        "boa, né?"),
    dict(id="17", block="p6", text=
        "{t}Mas parecer boa não basta. [p=0.3] Passo seis: [p=0.2] conferência. [p=0.3] {a}Coloco a tese embaixo da frase "
        "temática [p=0.2] e confiro bloco por bloco. [p=0.4] {b}Registro civil? [p=0.2] Tem. [p=0.3] {c}Invisibilidade? "
        "[p=0.2] Tem. [p=0.3] {d}Cidadania? [p=0.2] Direitos básicos, [p=0.2] tem. [p=0.3] {e}No Brasil? [p=0.5] Opa. "
        "[p=0.3] *Não tem.* [p=0.5] {f}Esqueci um bloco. [p=0.2] É o bairro certo, [p=0.2] sem número: [p=0.2] o caminho do "
        "*tangenciamento.*"),
    dict(id="18", block="p6", text=
        "{t}Então eu corrijo, [p=0.2] ainda no rascunho. [p=0.4] {a}A falta de registro civil torna milhares de brasileiros "
        "invisíveis para o Estado, [p=0.2] o que os afasta de direitos básicos; [p=0.3] {b}esse quadro persiste pela "
        "distância entre os cartórios e as populações mais isoladas [p=0.2] e pela desinformação sobre a gratuidade do "
        "registro."),
    dict(id="19", block="p6", text=
        "{t}Confere de novo. [p=0.3] {a}Repare que a tese cita os *quatro blocos* [p=0.3] {b}e anuncia *dois eixos:* "
        "[p=0.2] {c}distância [p=0.2] {d}e desinformação. [p=0.4] {e}Agora sim: [p=0.2] *endereço completo.*"),
    dict(id="20", block="repertorio", text=
        "{t}E para escrever sobre esses eixos, [p=0.2] você vai precisar de *repertório:* [p=0.2] informação de fora da "
        "prova [p=0.2] que você leva para o texto. [p=0.4] {a}Um repertório possível para o segundo eixo [p=0.2] é a Lei "
        "número nove mil, quinhentos e trinta e quatro, [p=0.2] de mil novecentos e noventa e sete, [p=0.3] {b}que tornou "
        "gratuitos o registro civil de nascimento e a primeira certidão. [p=0.4] {c}Informação de fora da prova, [p=0.2] "
        "ligada diretamente ao recorte."),

    # ================= CONTRAEXEMPLO =================
    dict(id="21", block="lado", text=
        "{t}Agora, [p=0.2] veja como *não* começar. [p=0.4] {a}Leitura que tangencia: [p=0.3] {b}A cidadania é um conceito "
        "antigo, [p=0.2] que surgiu na Grécia [p=0.2] e se transformou ao longo da história [p=0.2] até chegar às democracias "
        "modernas."),
    dict(id="22", block="lado", text=
        "{a}Parece um começo bonito, [p=0.2] né? [p=0.4] {b}Mas esse começo fica no assunto amplo, [p=0.2] cidadania em geral, "
        "[p=0.3] {c}e abandona o registro civil, [p=0.2] a invisibilidade [p=0.2] e o Brasil. [p=0.4] {d}Se o texto inteiro "
        "seguir por esse caminho, [p=0.2] o risco de tangenciamento é real."),
    dict(id="23", block="dica", text=
        "{t}E se o tema for difícil, [p=0.2] daqueles que você nunca ouviu falar? [p=0.4] {a}A Cartilha observa que os textos "
        "motivadores podem ser de grande ajuda [p=0.2] quando o tema é pouco familiar. [p=0.4] {b}Use-os para descobrir qual é "
        "*o problema* [p=0.2] e quais aspectos dele estão em jogo; [p=0.3] {c}depois, [p=0.2] procure no que você já estudou, "
        "[p=0.2] {d}História, [p=0.2] Geografia, [p=0.2] Sociologia, [p=0.2] Literatura, [p=0.2] notícias, [p=0.3] algo que "
        "se ligue a esses aspectos."),
    dict(id="24", block="dica", text=
        "{a}E repare: [p=0.2] a tese que cobre o recorte [p=0.2] é exatamente onde começa a *introdução,* [p=0.3] o próximo "
        "assunto da série."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="25", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] blocos, [p=0.2] pergunta, [p=0.2] tese, [p=0.2] "
        "conferência. [p=0.5] {b}Dois: [p=0.2] tese é igual a posição, [p=0.2] mais dois eixos, [p=0.2] mais todos os "
        "blocos. [p=0.5] {c}Três: [p=0.2] confira antes de desenvolver, [p=0.2] não depois."),

    # ================= NÓS FAZEMOS: QUESTÃO 9 =================
    dict(id="26", block="q9", text=
        "{t}Agora, [p=0.2] nós fazemos. [p=0.3] {a}Para o tema do ENEM de dois mil e vinte e um, [p=0.2] Invisibilidade e "
        "registro civil: garantia de acesso à cidadania no Brasil, [p=0.3] a frase que deixa de apenas repetir o tema e "
        "apresenta uma tese é:"),
    dict(id="27", block="q9", text=
        "{a}A: [p=0.2] A invisibilidade e o registro civil são questões relacionadas à garantia de acesso à cidadania no "
        "Brasil. [p=0.5] {b}B: [p=0.2] Sem certidão de nascimento, parte dos brasileiros fica invisível para o Estado [p=0.2] "
        "e perde acesso a direitos básicos, [p=0.2] situação mantida pela distância dos cartórios [p=0.2] e pela desinformação "
        "sobre a gratuidade do registro. [p=0.5] {c}C: [p=0.2] O registro civil é um assunto que merece a atenção de toda a "
        "sociedade brasileira."),
    dict(id="28", block="q9", text=
        "{d}D: [p=0.2] Muitas pessoas falam sobre invisibilidade e registro civil, [p=0.2] e é preciso refletir sobre o tema. "
        "[p=0.5] {e}E: [p=0.2] Este texto vai discutir a invisibilidade e o registro civil como garantia de acesso à cidadania "
        "no Brasil. [p=0.5] {p}*Pause o vídeo,* [p=0.2] diga qual frase é tese, [p=0.2] e por que as outras não são. [p=2.0]"),
    dict(id="29", block="q9", text=
        "{t}Vamos juntos. [p=0.3] {ok}A B toma uma posição contestável sobre o recorte, [p=0.2] a falta de "
        "registro torna pessoas invisíveis e as afasta de direitos, [p=0.3] e aponta causas que o "
        "desenvolvimento pode sustentar. [p=0.2] É uma tese. [p=0.5] {xa}A A reescreve a frase temática sem afirmar nada "
        "discutível. [p=0.4] {xc}A C declara importância, [p=0.2] não posição. [p=0.4] {xd}A D é genérica e adia a reflexão. "
        "[p=0.4] {xe}E a E anuncia o tema, [p=0.2] mas não diz o que o texto defende. [p=0.5] {fim}*Letra B!*"),

    # ================= VOCÊ FAZ: QUESTÃO 8 =================
    dict(id="30", block="q8", text=
        "{t}Agora, [p=0.2] você faz sozinho. [p=0.4] {a}O tema do ENEM de dois mil e vinte foi: [p=0.3] *O estigma associado "
        "às doenças mentais na sociedade brasileira.* [p=0.5] {b}*Estigma* é uma marca negativa [p=0.2] que a sociedade cola "
        "numa pessoa. [p=0.4] {c}Antes de ver as alternativas, [p=0.2] *pause o vídeo* [p=0.2] e escreva a sua tese "
        "provisória, [p=0.2] com dois eixos. [p=2.0]"),
    dict(id="31", block="q8", text=
        "{t}Pronto? [p=0.3] {q}A tese que atende ao recorte completo desse tema é: [p=0.4] {a}A: [p=0.2] As doenças mentais "
        "afetam milhões de pessoas no mundo e exigem mais pesquisas científicas. [p=0.5] {b}B: [p=0.2] O Sistema Único de "
        "Saúde precisa ampliar a oferta de medicamentos para todas as doenças crônicas."),
    dict(id="32", block="q8", text=
        "{c}C: [p=0.2] No Brasil, [p=0.2] a associação entre transtorno mental e fraqueza ou perigo afasta as pessoas do "
        "tratamento, [p=0.2] preconceito que é reforçado pela desinformação [p=0.2] e por representações estereotipadas na "
        "mídia. [p=0.5] {d}D: [p=0.2] O estigma associado às doenças mentais na sociedade brasileira é um tema muito "
        "importante que deve ser discutido por todos. [p=0.5] {e}E: [p=0.2] Os transtornos mentais têm causas genéticas e "
        "ambientais, [p=0.2] estudadas pela psiquiatria desde o século dezenove. [p=0.5] {p}*Pause e confira!* [p=2.0]"),
    dict(id="33", block="q8", text=
        "{t}Conferência, [p=0.2] bloco por bloco: [p=0.2] estigma, [p=0.2] doenças mentais, [p=0.2] sociedade brasileira. "
        "[p=0.4] {xa}A A fala de doenças mentais sem o estigma e fora do Brasil: [p=0.2] assunto amplo. [p=0.4] {xb}A B amplia "
        "para todas as doenças crônicas [p=0.2] e troca o estigma por oferta de remédios. [p=0.4] {xd}A D apenas repete a "
        "frase temática: [p=0.2] não há posição nem eixos. [p=0.4] {xe}A E fica no assunto amplo, [p=0.2] sob o ângulo "
        "científico, [p=0.2] sem estigma nem Brasil."),
    dict(id="34", block="q8", text=
        "{ok}E a C cobre estigma, [p=0.2] a associação a fraqueza ou perigo, [p=0.3] doenças mentais [p=0.2] e sociedade "
        "brasileira, [p=0.3] toma posição [p=0.2] {ok2}e anuncia dois eixos: [p=0.2] desinformação e mídia. [p=0.5] "
        "{fim}*Letra C!* [p=0.3] Compare com a sua: [p=0.2] ela tinha posição, [p=0.2] dois eixos [p=0.2] e os três blocos?"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="35", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *pular a conferência* [p=0.2] porque a tese parece "
        "boa. [p=0.4] {b}Parece certo, [p=0.2] porque você está com pressa [p=0.2] e a frase soa bem. [p=0.4] {c}Mas foi "
        "assim que a minha primeira tentativa esqueceu o Brasil. [p=0.2] *Confira sempre.*"),
    dict(id="36", block="erros", text=
        "{a}Segundo: [p=0.2] uma tese que *repete o tema* [p=0.2] ou só o anuncia: [p=0.3] Este texto vai discutir... "
        "[p=0.4] {b}Parece certo, [p=0.2] porque usa todas as palavras da prova. [p=0.4] {c}Mas não diz o que você defende: "
        "[p=0.2] *tome posição.*"),
    dict(id="37", block="erros", text=
        "{a}Terceiro: [p=0.2] *começar pelo assunto amplo.* [p=0.4] {b}Parece certo, [p=0.2] porque contextualizar soa "
        "inteligente. [p=0.4] {c}Mas o texto sai do recorte [p=0.2] logo na primeira linha. [p=0.2] *Comece pelo tema.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="38", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] blocos, [p=0.2] pergunta, [p=0.2] tese, [p=0.2] "
        "conferência. [p=0.5] {b}Dois: [p=0.2] tese é igual a posição, [p=0.2] mais dois eixos, [p=0.2] mais todos os "
        "blocos. [p=0.5] {c}Três: [p=0.2] confira antes de desenvolver, [p=0.2] não depois."),

    # ================= PONTE E CTA =================
    dict(id="39", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] {b}juntamos tudo, [p=0.3] {c}caçamos as *pegadinhas* [p=0.3] {d}e você "
        "recebe um *desafio prático* [p=0.2] com cinco temas reais."),
    dict(id="40", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual foi a sua tese para o tema das doenças mentais? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
