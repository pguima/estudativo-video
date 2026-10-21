# Roteiro — Compreensão Global e Tese, Episódio 6: A tese implícita (aula para iniciantes)
# Base: Estudos/Enem/estudos/05-linguagens/01-compreensao-global-tese.html — seção 06 + Questão 4 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: o autor de um texto implícito é um FOTÓGRAFO. Não diz a opinião, mas escolhe o que enquadrar,
#   o que deixa de fora e o que coloca lado a lado. A opinião está na ESCOLHA.
# Recorte: ironia e humor (assunto 15) e inferência (assunto 03) terão séries próprias; aqui, só o necessário
#   para reconstruir a tese.
# Sequência eu faço → nós fazemos → você faz: Dona Lurdes (eu faço) → o amigo "que pontual!" com as três perguntas
#   (nós fazemos) → Questão 4 (você faz: pausa para as três perguntas antes das alternativas).
# Classificação das erradas (resolução do material + nomes do ep. 3):
#   Q4: A leitura literal da ironia (contradição) · D também ao pé da letra ("homem de fé") · B extrapolação ·
#   C redução que desloca o foco (o problema não é a fila, é quem a fura) · certa E.
# Frases-chave (meio e fim, idênticas):
#   1. A opinião está na escolha: o que mostra, o que contrasta, o tom.
#   2. Implícito não é livre: só vale o que o texto autoriza.
#   3. Elogio irônico é crítica.
# Cores: azul = tese/definição · verde = pista/palavra-sinal · amarelo = armadilha · vermelho = erro · roxo = regra.
# Textos-base (Dona Lurdes; Questão 4: texto, comando e alternativas) lidos EXATAMENTE como no material.
# Na gravação: a Questão 4 (cena 24) pede entonação irônica, de elogio exagerado.

TITULO = "A tese implícita: quando o texto defende algo sem dizer \"eu defendo\" — Linguagens ENEM, episódio 6"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Um texto pode não ter *nenhuma* frase de opinião [p=0.3] {b}e mesmo assim defender uma ideia com muita força. "
        "[p=0.5] {c}No ENEM, [p=0.2] crônicas, [p=0.2] charges e anúncios fazem isso *o tempo todo.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai reconstruir a *tese escondida* de um texto, [p=0.3] {b}sem inventar nada além "
        "do que ele *autoriza.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Três lembranças. [p=0.3] {a}Episódio um: [p=0.2] a *tese* é o que o texto afirma. [p=0.4] {b}Episódio quatro: [p=0.2] "
        "quando ela não está escrita em frase nenhuma, [p=0.2] é a *tese implícita.* [p=0.4] {c}Episódio três: [p=0.2] "
        "*contradição* é dizer o contrário do texto; [p=0.3] {d}*extrapolação* é ir além dele."),

    # ================= CONCRETO: O AMIGO E A FOTO =================
    dict(id="04", block="amigo", text=
        "{t}Imagine a cena. [p=0.3] {a}Você chega *uma hora* atrasado. [p=0.3] {b}E o seu amigo diz: [p=0.2] Nossa, [p=0.2] que "
        "pontual! [p=0.5] {c}Ele não disse você se atrasou. [p=0.2] Mas você *entendeu.* [p=0.4] {d}O que está escrito com todas "
        "as letras é *explícito.* [p=0.3] {e}O que não está escrito, [p=0.2] mas a situação deixa entender, [p=0.2] é *implícito.* "
        "[p=0.3] Guarde esse amigo. [p=0.2] Ele volta."),
    dict(id="05", block="foto", text=
        "{t}Agora, uma foto. [p=0.3] {a}De um lado, [p=0.2] um prédio de luxo. [p=0.3] {b}Do outro, [p=0.2] colada nele, "
        "[p=0.2] uma favela. [p=0.3] {c}Sem legenda. [p=0.4] {d}Mesmo assim, [p=0.2] a foto diz "
        "alguma coisa sobre desigualdade. [p=0.4] {e}Você *inferiu:* [p=0.2] tirou uma conclusão a partir de pistas. [p=0.4] "
        "{f}Mas quem falou? [p=0.3] O *fotógrafo.* [p=0.2] Ele escolheu pôr os dois lado a lado."),
    dict(id="06", block="fotografo", text=
        "{t}Guarde essa imagem. [p=0.3] {a}O autor de um texto implícito é como um *fotógrafo.* [p=0.4] "
        "{b}Ele não diz a opinião. [p=0.3] {c}Mas escolhe o que enquadrar, [p=0.2] o que deixa de fora, [p=0.2] e o que coloca lado "
        "a lado. [p=0.4] {d}A opinião está na *escolha.*"),

    # ================= BLOCO A: ONDE A OPINIÃO APARECE =================
    dict(id="07", block="generos", text=
        "{t}Quem escreve assim? [p=0.3] {a}A *crônica:* [p=0.2] um texto curto que conta uma cena do dia a dia. [p=0.4] {b}A "
        "*charge:* [p=0.2] um desenho de humor que comenta uma notícia. [p=0.4] {c}E o *anúncio:* [p=0.2] a propaganda. [p=0.4] "
        "{d}Eles quase nunca dizem: [p=0.2] eu defendo que. [p=0.3] Então, [p=0.2] onde está a opinião?"),
    dict(id="08", block="onde", text=
        "{a}Primeiro lugar: [p=0.2] na *seleção.* [p=0.3] Seleção é o que o texto escolhe mostrar, [p=0.2] e o que deixa de fora. "
        "[p=0.4] {b}É o *enquadramento* do fotógrafo: [p=0.2] o que fica dentro da foto."),
    dict(id="09", block="onde", text=
        "{a}Segundo lugar: [p=0.2] no *contraste.* [p=0.3] Contraste é pôr lado a lado duas coisas que brigam entre si. [p=0.4] "
        "{b}O prédio de luxo [p=0.2] colado na favela."),
    dict(id="10", block="onde", text=
        "{a}Terceiro lugar: [p=0.2] no *tom.* [p=0.3] Tom é o jeito de falar: [p=0.2] sério, [p=0.2] exagerado, [p=0.2] "
        "debochado. [p=0.4] {b}Foi o tom que fez o que pontual do seu amigo [p=0.2] significar o *contrário.*"),

    # ================= BLOCO B: EU FAÇO (DONA LURDES) =================
    dict(id="11", block="lurdes", text=
        "{t}Agora, eu faço. [p=0.3] Um texto curtinho, [p=0.2] e eu vou pensar em voz alta. [p=0.4] {f1}Na sala de espera do posto "
        "de saúde, a televisão anunciava um aplicativo para marcar consultas “em segundos”. [p=0.4] {c1}Repare nas aspas: [p=0.2] *em segundos.* [p=0.2] É a promessa."),
    dict(id="12", block="lurdes", text=
        "{f2}Dona Lurdes, que chegara às cinco da manhã para pegar senha, assistiu ao anúncio inteiro. [p=0.4] {c2}Cinco da manhã. "
        "[p=0.2] Guarde esse horário. [p=0.4] {f3}Às onze, foi chamada. [p=0.5] {c3}Onze horas. [p=0.2] Das cinco às onze, "
        "[p=0.2] são *seis horas* de espera."),
    dict(id="13", block="lurdes", text=
        "{t}Repare: [p=0.2] {a}nenhuma frase opina. [p=0.2] Ninguém escreveu: [p=0.2] isso é um absurdo. [p=0.4] {b}Mas o "
        "texto pôs lado a lado [p=0.2] a promessa de *segundos* [p=0.3] {c}e as *seis horas* de espera real. [p=0.4] {d}O "
        "fotógrafo enquadrou a TV e a Dona Lurdes *na mesma foto.*"),
    dict(id="14", block="lurdes", text=
        "{t}Então, qual é a tese? [p=0.4] {a}Algo como: [p=0.2] *a modernização anunciada está longe da experiência de quem de fato "
        "usa o serviço.* [p=0.4] {b}Modernização é deixar o serviço mais moderno, [p=0.2] com tecnologia. [p=0.4] {c}A promessa "
        "da TV [p=0.2] não chegou à cadeira da Dona Lurdes."),

    # ================= BLOCO C: O LIMITE =================
    dict(id="15", block="limite", text=
        "{t}Dá para ir mais longe? [p=0.4] {a}Alguém diria: [p=0.2] *o texto defende o fim dos aplicativos.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque o aplicativo saiu mal na história. [p=0.4] {c}Só que o texto não pede o fim de nada. "
        "[p=0.3] {d}Isso é *extrapolação.*"),
    dict(id="16", block="limite", text=
        "{a}Outra: [p=0.2] *o posto é mal administrado.* [p=0.4] {b}Parece certo, [p=0.2] porque seis horas de espera é muito. "
        "[p=0.4] {c}Só que o texto não diz por que a espera foi longa. [p=0.3] {d}*Extrapolação* "
        "de novo. [p=0.4] {e}O fotógrafo só responde pelo que está *dentro* da foto."),

    # ================= BLOCO D: AS TRÊS PERGUNTAS =================
    dict(id="17", block="perguntas", text=
        "{t}Como chegar à tese sem passar do ponto? [p=0.4] Com três perguntas. [p=0.4] {a}Um: [p=0.2] o que o texto escolheu "
        "mostrar, [p=0.2] e o que deixou de fora? [p=0.4] {b}Dois: [p=0.2] há contraste ou exagero? [p=0.2] Entre o quê e o quê? "
        "[p=0.4] {c}Três: [p=0.2] quem, [p=0.2] ou o que, [p=0.2] sai criticado ou valorizado no fim?"),

    # ================= NÓS FAZEMOS: O AMIGO DE VOLTA =================
    dict(id="18", block="nosfazemos", text=
        "{t}Vamos fazer juntos, [p=0.2] com aquele amigo. [p=0.2] Nossa, que pontual! [p=0.4] {a}O que ele escolheu mostrar? "
        "[p=0.2] A pontualidade. [p=0.4] {b}Há contraste? [p=0.2] Sim: [p=0.2] o elogio contra uma hora de atraso. [p=0.4] "
        "{c}Quem sai criticado? [p=0.2] *Quem chegou atrasado.* [p=0.4] {d}As palavras elogiam. [p=0.2] A mensagem *critica.*"),

    # ================= BLOCO E: IRONIA AO PÉ DA LETRA =================
    dict(id="19", block="ironia", text=
        "{t}Isso tem nome. [p=0.3] {a}*Ironia* é dizer uma coisa para significar outra. [p=0.3] {b}Em geral, [p=0.2] o texto "
        "irônico *elogia para criticar.* [p=0.4] {c}Ler ao pé da letra é ler só o que as palavras dizem, "
        "[p=0.2] sem o tom. [p=0.4] {d}Leia a ironia ao pé da letra, [p=0.2] e você vai marcar o *contrário* do texto: "
        "[p=0.2] uma contradição. [p=0.4] {e}A ironia ainda terá uma série só dela."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a opinião está na escolha: [p=0.2] o que mostra, [p=0.2] o que "
        "contrasta, [p=0.2] o tom. [p=0.5] {b}Dois: [p=0.2] implícito não é livre: [p=0.2] só vale o que o texto autoriza. "
        "[p=0.5] {c}Três: [p=0.2] elogio irônico é crítica."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que um texto sem frase de opinião "
        "*não tem tese.* [p=0.4] {b}Parece certo, [p=0.2] porque você não achou nenhum eu acho. [p=0.4] {c}Mas a opinião "
        "está na escolha. [p=0.2] *Faça as três perguntas.*"),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] ler a ironia *ao pé da letra.* [p=0.4] {b}Parece certo, [p=0.2] porque você está repetindo o que o "
        "texto escreveu. [p=0.4] {c}Mas o tom vira o sentido do avesso. [p=0.2] *Elogio irônico é crítica.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] ir *além* do texto ao montar a tese. [p=0.4] {b}Parece certo, [p=0.2] porque a conclusão faz "
        "sentido no mundo. [p=0.4] {c}Mas não está na foto. [p=0.2] *Só vale o que o texto autoriza.*"),

    # ================= QUESTÃO 4 (VOCÊ FAZ) =================
    dict(id="24", block="questao4", text=
        "{t}Agora, você faz. [p=0.3] {a}O comando: [p=0.2] *O texto, construído em tom irônico, tem como ideia central.* [p=0.3] "
        "Ele já te avisou: [p=0.2] tom irônico. [p=0.4] "
        "{f1}Admiro profundamente o motorista que para na vaga de idoso “só por um minutinho”. [p=0.3] "
        "{f2}É um homem de fé: acredita que o tempo dele vale mais que o joelho alheio. [p=0.3] "
        "{f3}Admiro também quem fura a fila do pão com um sorriso, convicto de que a pressa é um documento. [p=0.3] "
        "{f4}Gente assim nos ensina, todos os dias, que a regra é ótima — para os outros. [p=0.5] "
        "{g}Alheio quer dizer: [p=0.2] de outra pessoa. [p=0.2] Convicto: [p=0.2] certo, [p=0.2] convencido."),
    dict(id="25", block="questao4", text=
        "{t}*Pause o vídeo* [p=0.2] e aplique as três perguntas. [p=1.5]"),
    dict(id="26", block="questao4", text=
        "{t}Vamos conferir. [p=0.3] {a}Escolheu mostrar: [p=0.2] o motorista na vaga de idoso [p=0.2] e quem fura a fila. [p=0.4] "
        "{b}Contraste: [p=0.2] a palavra admiro, [p=0.2] contra atitudes que ninguém admira. [p=0.4] {c}Então, o admiro vira do "
        "avesso: [p=0.2] *critico.* [p=0.4] {d}E a última frase entrega a tese: [p=0.2] a regra é ótima, [p=0.2] *para os outros.* "
        "[p=0.4] {e}Ou seja: [p=0.2] essas pessoas se acham *exceção* às regras."),
    dict(id="27", block="questao4", text=
        "{t}Agora, as alternativas. [p=0.3] {a}A: [p=0.2] o elogio a pessoas que sabem aproveitar bem o próprio tempo. [p=0.4] "
        "{b}B: [p=0.2] a defesa de que o número de vagas para idosos seja ampliado. [p=0.4] {c}C: [p=0.2] a constatação de que as "
        "filas das padarias são desorganizadas. [p=0.4] {d}D: [p=0.2] a ideia de que a fé leva as pessoas a agir com pressa. "
        "[p=0.4] {e}E: [p=0.2] a crítica a quem desrespeita regras de convivência por se julgar uma exceção a elas. [p=0.5] "
        "{p}*Pause e dê o nome da armadilha de cada uma.* [p=1.5]"),
    dict(id="28", block="questao4", text=
        "{t}Vamos conferir. [p=0.3] {a}A A lê o admiro ao pé da letra: [p=0.2] *contradição.* [p=0.4] {d}A D faz o mesmo "
        "com homem de fé. [p=0.4] {b}A B fala em ampliar vagas, [p=0.2] e o texto não propõe isso: [p=0.2] *extrapolação.* [p=0.4] "
        "{c}A C fica só com a fila, [p=0.2] mas o problema é quem fura: [p=0.2] *redução.* [p=0.4] {ok}Sobra a E: [p=0.2] "
        "a crítica a quem se acha exceção. [p=0.2] *Letra E.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a opinião está na escolha: [p=0.2] o que mostra, [p=0.2] "
        "o que contrasta, [p=0.2] o tom. [p=0.5] {b}Dois: [p=0.2] implícito não é livre: [p=0.2] só vale o que o texto autoriza. "
        "[p=0.5] {c}Três: [p=0.2] elogio irônico é crítica."),

    # ================= PONTE =================
    dict(id="30", block="ponte", text=
        "{t}Você viu todas as peças da compreensão global. [p=0.4] {a}No último episódio, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos "
        "as pegadinhas, [p=0.3] {c}e treinamos com *questões novas.*"),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *Linguagens do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual foi o elogio mais irônico que você já ouviu? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
