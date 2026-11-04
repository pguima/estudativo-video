# Roteiro — Redação ENEM, Introdução, Episódio 2 de 7: Contextualizar — quatro caminhos para começar a redação
# Base: Estudos/Enem/estudos/06-redacao/02-introducao.html — seção 03 (quatro caminhos, tabela "funciona bem quando /
#   cuidado com", caixa "Dado da coletânea não é repertório") + Questões 2 e 8 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia da série: a introdução é a ETIQUETA COMPLETA DA ENCOMENDA; a contextualização é o MAPA.
#   Deste episódio: quatro PORTAS de entrada no mapa (lei/obra, fato histórico, dado, conceito), cada uma com um
#   DEGRAU SOLTO (o risco típico: coringa, data incerta, número sem fonte, definição óbvia).
# Fidelidade: SÓ as referências da figura da seção 03 — Lei nº 10.639/2003; abolição em 1888 sem políticas de integração;
#   Censo 2022 do IBGE, pretos e pardos = 55,5% da população; patrimônio cultural imaterial no art. 216 da Constituição.
#   As aberturas escritas no rascunho e as do "nós fazemos" são elaboradas para fins didáticos (aviso na tela) e não
#   acrescentam leis, datas ou números. "Pesquisas mostram que 90%…" e a definição de dicionário aparecem só como
#   CONTRAEXEMPLO. Questões 2 e 8 reproduzidas sem alteração (gabaritos: Q2 A · Q8 A).
# Cores: azul = definição/tema · verde = método/funciona · amarelo = armadilha (degrau solto) · vermelho = erro ·
#   roxo = regra oficial.

TITULO = "Desde os Primórdios? 4 Jeitos Melhores de Começar a Redação | Introdução da Redação Ep. 2"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Nesta aula você abre quatro portas para começar a redação: "
            "apresente cada porta com curiosidade, avise dos riscos com cuidado de quem quer proteger o aluno e "
            "comemore os acertos nas questões. Quando ler o que está escrevendo na folha, fale um pouco mais devagar, "
            "como quem pensa em voz alta. Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. "
            "Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO E PROMESSA =================
    dict(id="01", block="hook", text=
        "{a}Desde os primórdios da humanidade… [p=0.5] {b}Você já começou uma redação assim? [p=0.4] {c}Essa frase serve para "
        "*qualquer* tema, [p=0.2] e por isso não diz *nada* sobre o seu. [p=0.4] {d}Hoje você vai aprender *quatro "
        "começos* que dizem."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai saber contextualizar um tema por *quatro caminhos* [p=0.3] {b}e qual cuidado tomar "
        "em cada um."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Relembrando o episódio um, [p=0.2] bem rápido. [p=0.3] {a}A introdução é a *etiqueta completa da encomenda.* "
        "[p=0.3] {b}O *mapa* mostra de onde parte a entrega: [p=0.2] é a contextualização. [p=0.3] {c}O *endereço,* com o "
        "que você entrega, [p=0.2] é a tese. [p=0.3] {d}E a *lista* colada na caixa [p=0.2] é a antecipação dos argumentos. "
        "[p=0.4] {e}Hoje, [p=0.2] a gente abre o *mapa.*"),

    # ================= O QUE É CONTEXTUALIZAR =================
    dict(id="04", block="visita", text=
        "{t}Imagine que um visitante pergunta onde fica a sua casa. [p=0.4] {a}Você pode dizer: [p=0.2] fica perto da escola "
        "que abriu em tal ano. [p=0.4] {b}Ou: [p=0.2] é no bairro onde mora metade da cidade. [p=0.4] {c}Ou ainda: [p=0.2] "
        "é a rua da lei nova. [p=0.4] {d}São jeitos diferentes de *situar* alguém. [p=0.2] {e}E todos levam à *mesma casa.*"),
    dict(id="05", block="conceito", text=
        "{t}Na redação é igual. [p=0.3] {a}*Contextualizar* é dar ao leitor o *ponto de partida* da discussão. [p=0.4] "
        "{b}É o *mapa* da nossa etiqueta. [p=0.4] {c}E esse mapa tem *quatro portas de entrada:* [p=0.3] {d}lei ou obra, "
        "[p=0.2] {e}fato histórico, [p=0.2] {f}dado [p=0.2] {g}e conceito. [p=0.4] {h}Só que cada porta tem um *degrau "
        "solto:* [p=0.2] o risco típico daquele caminho."),
    dict(id="06", block="tema", text=
        "{t}Vamos testar as quatro portas num tema real. [p=0.3] {a}Enem dois mil e vinte e quatro: [p=0.3] Desafios para a "
        "valorização da herança africana no Brasil. [p=0.4] {b}Eu vou escrever na folha de rascunho [p=0.2] uma abertura "
        "por porta, [p=0.2] usando só referências do nosso material."),

    # ================= PORTA 1: REPERTÓRIO =================
    dict(id="07", block="portas", text=
        "{t}Porta um: [p=0.2] *repertório.* [p=0.3] {a}Repertório é o conhecimento que você traz de fora da prova: [p=0.2] "
        "uma lei, [p=0.2] uma obra, [p=0.2] um filme, [p=0.2] um pensador. [p=0.4] {b}Para este tema, [p=0.2] eu penso numa "
        "lei. [p=0.3] {w}Escrevo assim: [p=0.2] A Lei número dez mil seiscentos e trinta e nove, de dois mil e três, "
        "tornou obrigatório o ensino de história e cultura afro-brasileira nas escolas. [p=0.5] {c}Funciona porque fala "
        "*direto* do recorte: [p=0.2] a valorização da herança africana."),
    dict(id="08", block="portas", text=
        "{a}O degrau solto desta porta é a referência *coringa:* [p=0.3] aquela frase de pensador que você decorou [p=0.2] e "
        "que serviria para *qualquer* tema. [p=0.4] {b}Se serve para tudo, [p=0.2] não diz nada sobre o seu."),

    # ================= PORTA 2: CONTEXTO HISTÓRICO =================
    dict(id="09", block="portas", text=
        "{t}Porta dois: [p=0.2] *contexto histórico.* [p=0.3] {a}Aqui, o passado explica um problema que *persiste* até "
        "hoje. [p=0.4] {b}Para este tema, [p=0.2] a abolição da escravidão. [p=0.3] {w}Escrevo: [p=0.2] O Brasil aboliu a "
        "escravidão tardiamente, em mil oitocentos e oitenta e oito, sem políticas de integração da população liberta. "
        "[p=0.5] {c}O passado ajuda a entender por que a desvalorização continua."),
    dict(id="10", block="portas", text=
        "{a}O degrau solto: [p=0.2] *datas e fatos* de que você não tem certeza. [p=0.4] {b}Um ano errado derruba a "
        "confiança do leitor no resto. [p=0.3] {c}Na dúvida, [p=0.2] não arrisque."),

    # ================= PORTA 3: DADO =================
    dict(id="11", block="portas", text=
        "{t}Porta três: [p=0.2] *dado.* [p=0.3] {a}Um dado é um número que mostra o *tamanho* do problema. [p=0.3] E todo "
        "dado precisa de *fonte:* [p=0.2] quem mediu, [p=0.2] e quando. [p=0.4] {w}Escrevo: [p=0.2] Segundo o Censo dois "
        "mil e vinte e dois, do I B G E, pretos e pardos somam cinquenta e cinco vírgula cinco por cento da população. "
        "[p=0.5] {c}Fonte, [p=0.2] ano [p=0.2] e número."),
    dict(id="12", block="portas", text=
        "{a}Agora compare com isto: [p=0.2] pesquisas mostram que noventa por cento… [p=0.4] {b}Que pesquisas? [p=0.2] De "
        "quem? [p=0.2] De quando? [p=0.4] {c}Esse é o degrau solto: [p=0.2] número *inventado* ou *sem fonte.* [p=0.3] "
        "Parece preciso, [p=0.2] mas ninguém consegue verificar."),

    # ================= PORTA 4: CONCEITO =================
    dict(id="13", block="portas", text=
        "{t}Porta quatro: [p=0.2] *conceito.* [p=0.3] {a}Aqui, uma definição esclarece o que está em jogo. [p=0.4] {b}Para "
        "este tema: [p=0.2] *patrimônio cultural imaterial.* [p=0.3] {c}Imaterial é o que não se pega com a mão: [p=0.2] "
        "músicas, [p=0.2] festas, [p=0.2] saberes, [p=0.2] jeitos de fazer. [p=0.4] {w}Escrevo: [p=0.2] A Constituição, "
        "no artigo duzentos e dezesseis, reconhece o patrimônio cultural imaterial do país."),
    dict(id="14", block="portas", text=
        "{a}O degrau solto: [p=0.2] a definição de *dicionário,* [p=0.2] óbvia. [p=0.3] {b}Tipo: [p=0.2] cultura é o "
        "conjunto de costumes de um povo. [p=0.4] {c}Isso o leitor já sabe. [p=0.2] Não acrescenta nada ao seu tema."),

    # ================= COLETÂNEA ≠ REPERTÓRIO =================
    dict(id="15", block="coletanea", text=
        "{t}E agora, [p=0.2] uma armadilha que pega muita gente. [p=0.3] {a}Os *textos motivadores* são os textos de apoio "
        "que a própria prova entrega. [p=0.3] E às vezes eles trazem um dado. [p=0.4] {b}Esse dado *não é repertório:* "
        "[p=0.2] é informação da própria prova. [p=0.4] {c}Você pode retomá-lo brevemente, [p=0.2] por *paráfrase,* [p=0.2] "
        "que é dizer a mesma ideia com as suas palavras. [p=0.4] {d}Mas ele não substitui conhecimento seu. [p=0.4] {e}E "
        "se copiar, [p=0.2] lembra da série anterior? [p=0.2] As linhas deixam de contar: [p=0.2] é a *linha fantasma.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Agora é a sua vez. [p=0.3] Duas aberturas curtas para o mesmo tema. [p=0.3] Em cada uma, [p=0.2] diga qual "
        "*porta* ela usa [p=0.2] e qual é o *risco* dela. [p=0.4] {a}Primeira: [p=0.2] Sancionada em dois mil e três, a "
        "Lei número dez mil seiscentos e trinta e nove levou a história e a cultura afro-brasileira para a sala de aula. "
        "[p=0.4] {p}Pause e responda. [p=2.0] {r}Porta do *repertório:* [p=0.2] uma lei. [p=0.3] {k}O risco é virar "
        "coringa. [p=0.2] Por isso, a frase seguinte precisa ligar a lei ao recorte."),
    dict(id="17", block="exercicio", text=
        "{a}Segunda: [p=0.2] Mais da metade da população brasileira é preta ou parda: [p=0.2] cinquenta e cinco vírgula "
        "cinco por cento, segundo o Censo dois mil e vinte e dois. [p=0.4] {p}Pause e responda. [p=2.0] {r}Porta do "
        "*dado.* [p=0.3] {k}O risco é o número sem fonte. [p=0.2] Aqui tem fonte e ano: [p=0.2] dá para verificar."),

    # ================= RECAPITULAÇÃO DO MEIO =================
    dict(id="18", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Lei, história, dado ou conceito: [p=0.2] quatro portas para o mesmo tema. "
        "[p=0.5] {b}Cada porta tem um degrau solto: [p=0.2] coringa, [p=0.2] data errada, [p=0.2] número sem fonte, "
        "[p=0.2] óbvio. [p=0.5] {c}Dado da coletânea não é repertório seu."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.3] {a}Erro um: [p=0.2] abrir com uma frase universal, [p=0.2] tipo desde os "
        "primórdios, [p=0.2] ou hoje em dia muito se fala. [p=0.4] {b}Parece certo porque soa elegante [p=0.2] e serve para "
        "começar qualquer redação. [p=0.4] {c}E esse é o problema: [p=0.2] não informa nada sobre o recorte. [p=0.2] "
        "Contextualize o *tema,* [p=0.2] não a humanidade."),
    dict(id="20", block="erros", text=
        "{a}Erro dois: [p=0.2] inventar um número para parecer preciso. [p=0.4] {b}Parece certo porque número dá cara de "
        "pesquisa séria. [p=0.4] {c}Mas número que ninguém pode verificar fragiliza o argumento. [p=0.2] Use só dado com "
        "*fonte.*"),
    dict(id="21", block="erros", text=
        "{a}Erro três: [p=0.2] usar como repertório o dado do texto motivador. [p=0.4] {b}Parece certo porque é um dado "
        "oficial, [p=0.2] bem ali na sua frente. [p=0.4] {c}Mas é informação da prova. [p=0.2] Retome por paráfrase, "
        "[p=0.2] e traga algo *seu.*"),

    # ================= QUESTÃO 2 =================
    dict(id="22", block="q2", text=
        "{t}Questão no estilo Enem. [p=0.3] {a}Leia o início de uma introdução para o tema do Enem dois mil e vinte e "
        "quatro: [p=0.3] {f}O Brasil foi o último país das Américas a abolir a escravidão, em mil oitocentos e oitenta e "
        "oito, e o fez sem nenhuma política de integração da população liberta. [p=0.4] {q}Essa contextualização recorre "
        "principalmente a: [p=0.4] {A}A: [p=0.2] um contexto histórico, usado para explicar a origem de um problema que "
        "persiste. [p=0.4] {B}B: [p=0.2] um dado estatístico, usado para dimensionar o problema."),
    dict(id="23", block="q2", text=
        "{C}C: [p=0.2] um conceito sociológico, usado para definir o que está em jogo. [p=0.4] {D}D: [p=0.2] uma obra "
        "literária, usada como analogia. [p=0.4] {E}E: [p=0.2] uma experiência vivida, usada como ilustração. [p=0.4] "
        "{p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="24", block="q2", text=
        "{ok}Letra *A.* [p=0.3] O trecho traz um *fato histórico:* [p=0.2] a abolição tardia e sem integração, [p=0.2] que "
        "pode explicar problemas atuais ligados à valorização da herança africana. [p=0.4] {xb}A B confunde a *data* com "
        "um dado estatístico: [p=0.2] não há quantidade sendo medida. [p=0.3] {xc}A C não se aplica: [p=0.2] nenhum "
        "conceito é definido. [p=0.3] {xd}A D [p=0.2] {xe}e a E descrevem fontes que não aparecem no trecho."),

    # ================= QUESTÃO 8 =================
    dict(id="25", block="q8", text=
        "{t}Mais uma. [p=0.3] {a}Para contextualizar o tema do Enem dois mil e vinte e quatro, [p=0.2] o uso de dado mais "
        "adequado é: [p=0.4] {A}A: [p=0.2] Segundo o Censo dois mil e vinte e dois do I B G E, pretos e pardos somam "
        "cinquenta e cinco vírgula cinco por cento da população brasileira, [p=0.2] maioria que contrasta com o espaço "
        "reduzido da cultura afro-brasileira nos currículos. [p=0.4] {B}B: [p=0.2] Pesquisas mostram que noventa por cento "
        "dos brasileiros desconhecem a cultura africana."),
    dict(id="26", block="q8", text=
        "{C}C: [p=0.2] Segundo especialistas, a herança africana é a mais importante do mundo. [p=0.4] {D}D: [p=0.2] Todo "
        "mundo sabe que a maioria das pessoas valoriza a cultura africana. [p=0.4] {E}E: [p=0.2] Segundo o Censo dois mil e "
        "vinte e dois, a população brasileira está envelhecendo. [p=0.4] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="27", block="q8", text=
        "{ok}Letra *A.* [p=0.3] Repare nas *três marcas* do dado bom. [p=0.3] {m1}Fonte e ano. [p=0.3] {m2}Pertinência: "
        "[p=0.2] fala da composição da população. [p=0.3] {m3}E *interpretação:* [p=0.2] o contraste entre a maioria negra "
        "e o pouco espaço nos currículos já prepara a tese. [p=0.4] {xb}A B é número sem fonte: [p=0.2] não dá para "
        "verificar. [p=0.3] {xc}A C atribui a especialistas anônimos um juízo vago. [p=0.3] {xd}A D é senso comum, [p=0.2] "
        "sem base. [p=0.3] {xe}E a E traz um dado de outro assunto."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Lei, história, dado ou conceito: [p=0.2] quatro portas "
        "para o mesmo tema. [p=0.5] {b}Cada porta tem um degrau solto: [p=0.2] coringa, [p=0.2] data errada, [p=0.2] número "
        "sem fonte, [p=0.2] óbvio. [p=0.5] {c}Dado da coletânea não é repertório seu."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Só que um mapa bonito que não leva à casa [p=0.2] não serve para nada. [p=0.4] {b}No próximo episódio: [p=0.2] "
        "a *ponte* que liga a referência ao recorte, [p=0.3] {c}e o *teste* que denuncia o repertório que não trabalha."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual das quatro portas você usaria para o tema de dois mil e vinte e "
        "quatro? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards "
        "do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
