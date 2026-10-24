# Roteiro — Tecnologia 011: FireTrace, o protótipo de análise de incêndios feito com o Claude Opus 5.5
# Base: original/fonte_firetrace.md (post de @DilumSanjaya no X, 08/10/2026; anúncio oficial do Opus 5.5;
# fontes oficiais sobre combate a incêndios). Consulta em 23/10/2026.
# Regra: o que o autor não contou (tempo, prompts, bibliotecas, código) NÃO é inventado; a parte "como se constrói"
# é hipótese rotulada ("costumam", "tipicamente"). Interface aparece só como RECRIAÇÃO desenhada.
# Marcações: {cue} animação · *texto* destaque · [p=0.4] pausa

TITULO = "Um painel de incêndios florestais feito com o Claude Opus 5.5? O que o FireTrace mostra (e o que não mostra)"

VOZ = dict(
    tags=["alegre", "confiante"],
    prompt=("Narre como um apresentador de canal de tecnologia mostrando um projeto impressionante que viu na internet: "
            "voz masculina adulta, grave, segura e entusiasmada, mas precisa e sem exagero. Curiosidade genuína no "
            "começo, clareza didática no tour pela interface e um tom mais sério e cuidadoso na parte do mundo real e "
            "dos limites. Dê ênfase às palavras-chave e aos números. Ritmo natural, sem pressa, respeitando as pausas "
            "entre as frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular nem repetir nada."),
)

PRONUNCIA = {}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="gancho", text=
        "{a}Um mapa em três dimensões [p=0.2] de uma serra na Califórnia. [p=0.3] {b}O fogo avançando, [p=0.2] "
        "*hora a hora.* [p=0.4] {c}Seis drones no ar, [p=0.2] {d}e uma câmera térmica marcando um ponto quente de "
        "*novecentos e oitenta e três graus.* [p=0.5] {e}Parece software de centro de comando. [p=0.3] "
        "Mas é um *protótipo,* [p=0.2] que um desenvolvedor diz ter feito [p=0.2] com o *Claude Opus cinco ponto cinco.*"),

    # ================= O POST =================
    dict(id="02", block="post", text=
        "{t}O post é do *Dilum Sanjaya,* [p=0.2] um desenvolvedor que posta no X demonstrações visuais feitas com IA. [p=0.4] {a}No dia *oito de outubro,* [p=0.2] ele escreveu: [p=0.3] {b}brinquei com uma ideia "
        "de ferramenta de *análise de incêndios florestais.* [p=0.3] Ela mostra o avanço do fogo ao longo do tempo, "
        "[p=0.2] rastreia *pontos quentes* com drones [p=0.2] e acompanha o *combate.* [p=0.3] {c}Feito com o "
        "*Opus cinco ponto cinco.* [p=0.5] {d}Junto, um vídeo de quase *dois minutos,* [p=0.2] sem som. [p=0.4] "
        "{e}Oito dias depois, [p=0.2] a conta oficial do *Claude* destacou o projeto [p=0.2] numa lista de *seis* "
        "criações da comunidade."),

    # ================= TOUR =================
    dict(id="03", block="incidente", text=
        "{s}Tudo o que você vê aqui é uma *recriação* nossa, [p=0.2] "
        "desenhada para explicar. [p=0.5] {a}O app se chama *FireTrace:* [p=0.2] análise forense de incêndios. [p=0.4] "
        "{b}O caso é o incidente *Ridgeview,* [p=0.2] nas montanhas de San Gabriel, na Califórnia, [p=0.2] de catorze a "
        "dezoito de agosto de dois mil e vinte e quatro. [p=0.3] {c}Pelo jeito, [p=0.2] um cenário de *demonstração.* "
        "[p=0.5] {d}No centro, um *mapa 3D* do relevo, [p=0.3] {e}e o *perímetro* do fogo crescendo, [p=0.2] com a hora "
        "marcada em cada trecho, [p=0.2] desde a ignição, às catorze e vinte e seis."),
    dict(id="04", block="tempo", text=
        "{a}Embaixo, uma *linha do tempo* que você toca como um vídeo, [p=0.3] {b}com os eventos-chave: [p=0.2] "
        "ignição, [p=0.2] crescimento rápido, [p=0.2] um foco secundário, [p=0.2] o fogo cruzando a crista [p=0.2] "
        "e a contenção. [p=0.4] {c}Ao lado, gráficos de *área queimada,* [p=0.2] *velocidade de avanço* [p=0.2] e "
        "*perfil de elevação.* [p=0.4] {d}À direita, *camadas* que ligam e desligam: [p=0.2] relevo, [p=0.2] imagem "
        "aérea, [p=0.2] cicatriz da queimada, [p=0.2] propagação modelada [p=0.2] e linhas de contenção. [p=0.4] "
        "{e}E um painel de *clima.*"),
    dict(id="05", block="drones", text=
        "{t}Na aba de *drones,* [p=0.2] seis de seis estão no ar, [p=0.2] cada um com uma *função.* [p=0.4] "
        "{a}Um mapeia o perímetro, [p=0.2] {b}outro circula a frente mais ativa do fogo, [p=0.2] {c}outro vigia um "
        "foco secundário. [p=0.3] {d}Tem patrulha, [p=0.2] levantamento [p=0.2] e até um drone só para *retransmitir* "
        "o sinal. [p=0.4] {e}Clicando num deles, [p=0.2] abre a *câmera infravermelha,* [p=0.2] com a "
        "telemetria na tela. [p=0.4] {f}E as detecções caem numa lista: [p=0.2] *ponto quente,* "
        "[p=0.2] novecentos e oitenta e três graus Celsius."),
    dict(id="06", block="recursos", text=
        "{t}A terceira aba mostra os *recursos* em campo: [p=0.2] *treze unidades.* [p=0.4] {a}Aviões-tanque, [p=0.2] "
        "como um *DC-10* [p=0.2] e um *C-130,* [p=0.3] {b}helicópteros [p=0.2] e um avião de coordenação aérea, [p=0.3] "
        "{c}caminhões, [p=0.2] equipes em solo [p=0.2] e um trator. [p=0.4] {d}Tem o registro de cada *lançamento de "
        "retardante,* [p=0.3] {e}e gráficos de galões, [p=0.2] de linha construída [p=0.2] e de pessoal. [p=0.3] {f}Dá até para seguir um avião com uma câmera de *perseguição.*"),

    # ================= COMO SE CONSTRÓI =================
    dict(id="07", block="camadas", text=
        "{t}E como se constrói uma coisa assim? [p=0.4] {a}Primeiro, o que *não sabemos:* [p=0.2] o Dilum não contou "
        "quanto tempo levou, [p=0.2] quais pedidos fez à IA, [p=0.2] que bibliotecas usou, [p=0.2] e não publicou o "
        "código. [p=0.5] {b}Então, o que segue é como apps assim *costumam* ser feitos. [p=0.4] "
        "{c}Na base, uma camada de *dados:* [p=0.2] perímetros por hora, [p=0.2] posições dos drones, [p=0.2] "
        "lançamentos de retardante. [p=0.3] Num protótipo, [p=0.2] dados *simulados.* [p=0.4] {d}Em cima, o *mapa 3D,* "
        "[p=0.2] tipicamente desenhado com *WebGL* [p=0.2] a partir de um modelo de elevação do terreno. [p=0.4] "
        "{e}Depois, a *linha do tempo,* [p=0.3] {f}e por fim os *painéis* e gráficos."),
    dict(id="08", block="relogio", text=
        "{a}O segredo de um painel desses é ter *um relógio só.* [p=0.4] {b}Você arrasta a linha do tempo [p=0.2] e "
        "*tudo* se atualiza junto: [p=0.3] {c}o perímetro no mapa, [p=0.2] {d}a posição dos drones, [p=0.2] "
        "{e}os gráficos [p=0.2] e a lista de eventos. [p=0.5] {f}São *muitas peças* conversando entre si."),

    # ================= OPUS 5.5 =================
    dict(id="09", block="opus", text=
        "{t}E o que isso diz sobre o *Opus cinco ponto cinco?* [p=0.4] {a}A Anthropic lançou o modelo em *vinte e dois "
        "de setembro.* [p=0.3] {b}Segundo a empresa, [p=0.2] ele chega ao nível do *Claude Fable cinco ponto um* na maior "
        "parte do trabalho, [p=0.3] {c}custando cerca de *quarenta por cento menos* que o Opus cinco. [p=0.4] "
        "{d}A Anthropic destaca tarefas *longas,* [p=0.3] {e}e cita um teste em que vários modelos criaram um jogo a "
        "partir de um único pedido: [p=0.3] o Opus cinco ponto cinco teve a maior nota em *gráficos e acabamento.* "
        "[p=0.5] {f}Só que um vídeo não mostra *quantas tentativas* [p=0.2] nem "
        "quanto ajuste manual foi preciso."),

    # ================= MUNDO REAL =================
    dict(id="10", block="real", text=
        "{t}E no mundo real? [p=0.3] Isso já existe, [p=0.2] com dados de verdade. [p=0.4] {a}A NASA mantém o *FIRMS,* [p=0.2] que distribui focos de incêndio vistos por "
        "satélite [p=0.2] em até *três horas* depois da observação. [p=0.4] {b}Nos Estados Unidos, [p=0.2] aviões com "
        "*infravermelho* voam *à noite,* [p=0.2] e atualizam o "
        "perímetro de calor *uma vez por dia.* [p=0.4] {c}Os drones do Serviço Florestal americano [p=0.2] enxergam "
        "através da *fumaça,* [p=0.2] e, segundo o órgão, [p=0.2] acham um foco de *cinco por cinco centímetros* [p=0.2] "
        "a quase *oitocentos metros.* [p=0.4] {d}E aqui no Brasil, [p=0.2] o *INPE* processa mais de *duzentas imagens* "
        "de satélite por dia [p=0.2] para detectar *focos de calor,* [p=0.2] no programa Queimadas."),
    dict(id="11", block="compara", text=
        "{t}Só que existe uma distância grande [p=0.2] entre um protótipo bonito [p=0.2] e um sistema de combate. [p=0.4] "
        "{a}No protótipo, os dados são de *demonstração;* [p=0.2] no real, vêm de *sensores,* satélites e equipes. "
        "[p=0.4] {b}No protótipo, atraso não importa; [p=0.2] no real, *minutos* contam. [p=0.4] {c}E um sistema real "
        "precisa ser *testado em campo* [p=0.3] {d}e ter alguém *responsável* pelas decisões tomadas com ele."),

    # ================= LIMITES =================
    dict(id="12", block="limites", text=
        "{t}E os cuidados com esse post. [p=0.4] {a}O protótipo só existe *em vídeo:* [p=0.2] não há código nem demo "
        "para testar. [p=0.4] {b}O autor não diz se os dados são *reais ou simulados.* [p=0.4] {c}O feito com Opus cinco "
        "ponto cinco é a *palavra dele;* [p=0.2] não sabemos quanta intervenção manual houve. [p=0.4] {d}E o destaque da "
        "conta do Claude é *vitrine,* [p=0.2] não uma avaliação independente."),

    # ================= RESUMO =================
    dict(id="13", block="resumo", text=
        "{t}Resumindo. [p=0.4] {a}O FireTrace é um protótipo de análise de incêndios, [p=0.2] postado pelo Dilum Sanjaya "
        "em oito de outubro. [p=0.4] {b}Mapa 3D, linha do tempo, drones com câmera térmica e recursos em campo, [p=0.2] "
        "tudo *sincronizado.* [p=0.4] {c}Ele diz que fez com o *Opus cinco ponto cinco,* [p=0.2] mas não mostrou como. "
        "[p=0.4] {d}O mundo real já usa satélites, aviões e drones, [p=0.2] com dados *validados.* [p=0.4] "
        "{e}É uma ótima *ideia ilustrada,* [p=0.2] não uma ferramenta pronta."),

    # ================= CTA + FONTES =================
    dict(id="14", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal "
        "[p=0.2] {bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] que ferramenta você tentaria criar com uma IA dessas? [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.0]"),
    dict(id="15", block="fontes", text=
        "{a}As *fontes* deste vídeo [p=0.2] estão na tela [p=0.2] e na descrição. [p=5.0]"),
]
