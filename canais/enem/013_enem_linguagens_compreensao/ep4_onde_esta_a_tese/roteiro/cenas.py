# Roteiro — Compreensão Global e Tese, Episódio 4: Onde a tese se esconde (aula para iniciantes)
# Base: Estudos/Enem/estudos/05-linguagens/01-compreensao-global-tese.html — seção 04 + Questões 2 e 3 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   DEDUTIVO = TRAILER (a conclusão vem primeiro e o resto prova) · INDUTIVO = FILME DE DETETIVE (pistas antes, revelação no fim)
#   IMPLÍCITO = FOTO SEM LEGENDA (ninguém fala, você monta o sentido) · "Há quem diga que…" = o autor põe o ADVERSÁRIO
#   para falar primeiro, só para derrubá-lo em seguida.
# Tese implícita: só apresentada (o ep. 6 aprofunda).
# Sequência eu faço → nós fazemos → você faz: esquemas + mini-exemplo do celular → Questão 2 (eu faço, virada no "Engano.")
#   → Questão 3 (você faz: pausa para dizer se é dedutivo ou indutivo antes das alternativas).
# Classificação das erradas (resolução do material + nomes do ep. 3):
#   Q2: A contradição (é a opinião refutada na 1ª frase) · B não está no texto (troca o assunto; preços) · C contradição
#   (o argumento da prefeitura, que o texto rejeita) · E extrapolação (crédito rural) · certa D.
#   Q3: A extrapolação (punição) · C organização trocada (descreve a dedutiva) · D redução (um dos três exemplos) ·
#   E "sem tese" (ignora a última frase = erro clássico 2) · certa B.
# Frases-chave (meio e fim, idênticas):
#   1. Dedutivo: tese no começo. Indutivo: tese no fim. Implícito: tese em lugar nenhum.
#   2. "Há quem diga" é a voz do outro, não a do autor.
#   3. Leia até o primeiro "mas".
# Cores: azul = tese/definição · verde = pista/palavra-sinal · amarelo = armadilha · vermelho = erro · roxo = regra.
# Textos-base (Questões 2 e 3: texto, comando e alternativas) lidos EXATAMENTE como no material.

TITULO = "Onde a tese se esconde: no começo, no fim ou em lugar nenhum — Linguagens ENEM, episódio 4"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Muita gente marca a *primeira frase* do texto [p=0.2] como a opinião do autor. [p=0.5] {b}Às vezes, [p=0.2] ela é "
        "exatamente a opinião [p=0.2] que o autor vai *destruir.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber *onde procurar a tese,* [p=0.3] {b}e não vai mais cair na armadilha "
        "da primeira frase."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Duas lembranças. [p=0.3] {a}Episódio um: [p=0.2] a *tese* é o que o texto afirma, [p=0.2] a frase que o autor quer que "
        "você leve para casa. [p=0.4] {b}Episódio três: [p=0.2] *contradição* é a alternativa que diz o oposto do texto, "
        "[p=0.2] a roupa do avesso."),

    # ================= BLOCO A: DEDUTIVO =================
    dict(id="04", block="dedutivo", text=
        "{t}Sabe aquele *trailer* que já entrega o final do filme? [p=0.4] {a}Você vê a conclusão primeiro, [p=0.2] e o resto do "
        "filme só mostra como se chegou lá. [p=0.4] {b}Tem texto assim: [p=0.2] a tese vem logo no início, [p=0.2] em geral no "
        "primeiro parágrafo, [p=0.3] {c}e o resto prova. [p=0.3] {d}No fim, [p=0.2] a conclusão *repete* a tese, [p=0.2] com "
        "outras palavras."),
    dict(id="05", block="dedutivo", text=
        "{t}Esse jeito de organizar tem nome: [p=0.2] *dedutivo.* [p=0.3] {a}Dedutivo: [p=0.2] tese no começo, [p=0.2] apoios "
        "depois. [p=0.4] {b}Ele aparece muito no *artigo de opinião:* [p=0.2] o texto de jornal em que alguém assina a própria "
        "opinião. [p=0.4] {c}E na *Redação do ENEM,* [p=0.2] que você mesmo vai escrever."),
    dict(id="06", block="dedutivo", text=
        "{a}Aparece também no *editorial:* [p=0.2] o texto que traz a opinião do próprio jornal, [p=0.2] sem a assinatura de "
        "ninguém. [p=0.4] {b}Viu um desses? [p=0.2] Procure a tese *no começo.*"),

    # ================= BLOCO B: INDUTIVO =================
    dict(id="07", block="indutivo", text=
        "{t}E o filme de detetive? [p=0.4] {a}Primeiro, as pistas: [p=0.2] uma pegada, [p=0.2] uma porta aberta, [p=0.2] um copo "
        "quebrado. [p=0.4] {b}Só no fim, [p=0.2] o detetive revela o culpado. [p=0.4] {c}Tem texto assim: [p=0.2] primeiro os casos "
        "e os exemplos, [p=0.3] {d}e a tese só no final."),
    dict(id="08", block="indutivo", text=
        "{t}Esse jeito se chama *indutivo:* [p=0.2] casos primeiro, [p=0.2] tese no fim. [p=0.4] {a}Ele é comum na *crônica,* "
        "[p=0.2] o texto curto que parte de uma cena do dia a dia, [p=0.3] {b}quando ela quer convencer você de alguma coisa. "
        "[p=0.3] {c}E na carta. [p=0.4] {d}Começou contando casos? [p=0.2] Procure a tese *no fim.*"),

    # ================= BLOCO C: TESE IMPLÍCITA =================
    dict(id="09", block="implicita", text=
        "{t}E quando ninguém escreve a tese? [p=0.4] {a}Pense numa foto *sem legenda.* [p=0.3] {b}Ninguém diz nada. [p=0.3] "
        "{c}Mas, olhando, [p=0.2] você monta o sentido. [p=0.4] {d}Até aqui, [p=0.2] a tese estava escrita numa frase: [p=0.2] "
        "isso é a *tese explícita.*"),
    dict(id="10", block="implicita", text=
        "{t}Na foto sem legenda, [p=0.2] a tese é *implícita:* [p=0.2] nenhuma frase sozinha a diz. [p=0.3] {a}É você, leitor, "
        "[p=0.2] que reconstrói, [p=0.2] juntando o que o texto mostra. [p=0.4] {b}Ela aparece na crônica irônica, [p=0.2] no poema, "
        "[p=0.2] no anúncio, [p=0.2] na tirinha, [p=0.3] {c}e na *charge:* [p=0.2] o desenho de humor do jornal, [p=0.2] que critica "
        "alguma coisa. [p=0.4] {d}No episódio seis, [p=0.2] você aprende a montar essa tese."),
    dict(id="11", block="esquemas", text=
        "{t}Os três, lado a lado. [p=0.3] {a}Dedutivo: [p=0.2] a tese em cima, [p=0.2] os apoios embaixo. [p=0.4] {b}Indutivo: "
        "[p=0.2] os casos, [p=0.2] uma seta, [p=0.2] e a tese no fim. [p=0.4] {c}Implícito: [p=0.2] fatos espalhados, [p=0.2] "
        "que se juntam numa tese [p=0.2] que ninguém escreveu."),

    # ================= BLOCO D: A ARMADILHA DA PRIMEIRA FRASE =================
    dict(id="12", block="armadilha", text=
        "{t}Agora, a armadilha que dá nome a esta aula. [p=0.4] {a}Muitos textos começam assim: [p=0.2] *há quem diga que,* "
        "[p=0.2] *muita gente acredita que,* [p=0.2] *diz-se que.* [p=0.4] {b}Quem está falando aí? [p=0.3] {c}Não é o autor. "
        "[p=0.2] É a voz do *outro.* [p=0.4] {d}O autor põe o adversário para falar primeiro, [p=0.2] só para derrubá-lo em seguida."),
    dict(id="13", block="armadilha", text=
        "{t}Derrubar uma ideia, [p=0.2] mostrando que ela está errada, [p=0.2] tem nome: [p=0.2] *refutar.* [p=0.4] {a}Veja: "
        "[p=0.2] há quem diga que o celular na escola só atrapalha. [p=0.4] {b}Não é bem assim: [p=0.2] a escola deve ensinar a usar. "
        "[p=0.4] {c}A tese não é a primeira frase. [p=0.2] É a que vem *depois da virada.*"),
    dict(id="14", block="armadilha", text=
        "{t}E como achar a virada? [p=0.3] {a}*Leia até o primeiro mas.* [p=0.3] {b}Ou porém, [p=0.2] engano, [p=0.2] não é bem "
        "assim. [p=0.4] {c}Quem marca a primeira frase como tese [p=0.2] marca justamente a opinião que o autor refuta. [p=0.3] "
        "{d}E isso, [p=0.2] você já sabe o nome: [p=0.2] *contradição.*"),

    # ================= BLOCO E: IMPLÍCITA NÃO É LIVRE =================
    dict(id="15", block="livre", text=
        "{t}Mas, se a tese implícita não está escrita, [p=0.2] vale qualquer uma? [p=0.4] {a}Não. [p=0.3] {b}Uma foto mostra uma fila "
        "enorme na porta de um posto de saúde. [p=0.4] {c}Você pode concluir: [p=0.2] o atendimento está demorado. [p=0.4] "
        "{d}Não pode concluir: [p=0.2] o prefeito é corrupto. [p=0.3] A foto não mostra isso. [p=0.4] {e}*Implícita não quer dizer "
        "livre:* [p=0.2] o texto precisa autorizar."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] dedutivo: [p=0.2] tese no começo. [p=0.2] Indutivo: [p=0.2] tese no "
        "fim. [p=0.2] Implícito: [p=0.2] tese em lugar nenhum. [p=0.5] {b}Dois: [p=0.2] há quem diga [p=0.2] é a voz do outro, "
        "[p=0.2] não a do autor. [p=0.5] {c}Três: [p=0.2] leia até o primeiro mas."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] tomar a primeira frase como tese. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque muito texto começa mesmo pela tese. [p=0.4] {c}Mas, se a primeira frase é a voz do outro, "
        "[p=0.2] ela vai ser derrubada. [p=0.2] *Leia até o primeiro mas.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] achar que um texto que só conta casos não tem tese. [p=0.4] {b}Parece certo, [p=0.2] porque nenhuma "
        "frase do começo dá opinião. [p=0.4] {c}Mas é o filme de detetive: [p=0.2] a revelação vem *no fim.*"),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] na tese implícita, [p=0.2] inventar uma conclusão que o texto não autoriza. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque, se ninguém escreveu a tese, [p=0.2] parece que vale tudo. [p=0.4] {c}Mas é a fila do posto: [p=0.2] "
        "*só vale o que a foto mostra.*"),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="20", block="questao2", text=
        "{t}Agora, eu faço, [p=0.2] pensando em voz alta. [p=0.4] {a}O comando: [p=0.2] *O assunto e a tese do texto são, "
        "respectivamente.* [p=0.3] Respectivamente: [p=0.2] primeiro o assunto, [p=0.2] depois a tese. [p=0.4] {f1}Há quem veja a "
        "feira livre como resquício de um tempo sem supermercado. [p=0.4] {c1}Há quem veja! [p=0.2] É a voz do outro. [p=0.3] "
        "Resquício é uma sobra de outra época."),
    dict(id="21", block="questao2", text=
        "{f2}Engano. [p=0.5] {c2}Aqui está a *virada.* [p=0.3] O autor acabou de derrubar a primeira frase. [p=0.4] {f3}A feira é "
        "onde o pequeno produtor vende sem intermediário, [p=0.2] onde o preço se negocia olhando no olho [p=0.2] e onde a cidade "
        "ainda se encontra na rua num domingo de manhã. [p=0.4] {c3}Sem intermediário: [p=0.2] sem ninguém no meio. [p=0.2] "
        "Três motivos: [p=0.2] a feira *tem valor.*"),
    dict(id="22", block="questao2", text=
        "{f4}Quando uma prefeitura transfere a feira para um galpão afastado, [p=0.2] alegando problemas de trânsito, [p=0.2] não está "
        "organizando o espaço: [p=0.2] está empurrando para longe um dos últimos mercados em que quem planta conversa com quem come. "
        "[p=0.4] {c4}Alegando: [p=0.2] é a desculpa da prefeitura. [p=0.2] O autor não aceita. [p=0.4] {d}Então: [p=0.2] assunto, "
        "[p=0.2] a feira livre. [p=0.2] Tese: [p=0.2] a feira tem valor, [p=0.2] e deve ficar na rua."),
    dict(id="23", block="questao2", text=
        "{t}As alternativas. [p=0.3] {a}A: [p=0.2] a feira livre; [p=0.2] a feira é um resquício de um tempo em que não havia "
        "supermercados. [p=0.4] {b}B: [p=0.2] o comércio de alimentos; [p=0.2] os supermercados oferecem preços mais baixos que as "
        "feiras. [p=0.4] {c}C: [p=0.2] o trânsito urbano; [p=0.2] as prefeituras devem organizar o uso das ruas. [p=0.4] {d}D: "
        "[p=0.2] a feira livre; [p=0.2] a feira tem valor econômico e social que justifica mantê-la no espaço da rua. [p=0.4] {e}E: "
        "[p=0.2] a agricultura familiar; [p=0.2] o pequeno produtor precisa de mais crédito rural."),
    dict(id="24", block="questao2", text=
        "{a}A A é a armadilha da primeira frase. [p=0.3] Assunto certo, [p=0.2] mas a tese é a opinião que o autor derruba. [p=0.2] "
        "*Contradição.* [p=0.4] {c}A C pega a desculpa da prefeitura, [p=0.2] que o texto rejeita. [p=0.2] *Contradição* de novo. "
        "[p=0.4] {b}A B fala de preços. [p=0.2] Em que linha isso está? [p=0.2] *Não está no texto.* [p=0.4] {e}A E fala em crédito: "
        "[p=0.2] *extrapolação.* [p=0.4] {ok}Sobra a D. [p=0.2] *Letra D.*"),

    # ================= QUESTÃO 3 (VOCÊ FAZ) =================
    dict(id="25", block="questao3", text=
        "{t}Agora, você faz. [p=0.3] {a}O comando: [p=0.2] *Quanto à construção do sentido global, o texto.* [p=0.3] Ou seja: "
        "[p=0.2] como o texto monta a sua ideia. [p=0.4] {f1}Na rua de cima, o portão quebrado ficou um ano sem conserto; [p=0.2] "
        "logo vieram as pichações, depois o lixo acumulado na calçada. [p=0.4] {f2}Na praça, o banco arrancado nunca foi reposto, "
        "[p=0.2] e as famílias deixaram de ir. [p=0.4] {c2}Um caso, [p=0.2] outro caso."),
    dict(id="26", block="questao3", text=
        "{f3}No posto de saúde, a lâmpada queimada da entrada transformou o fim de tarde em hora de medo. [p=0.4] {c3}Terceiro caso. "
        "[p=0.3] Pista, [p=0.2] pista, [p=0.2] pista. [p=0.4] {f4}Nenhum desses problemas, isolado, parecia urgente. [p=0.4] "
        "{f5}Juntos, ensinam uma lição que os orçamentos públicos costumam esquecer: [p=0.2] a manutenção miúda e constante custa menos "
        "do que a reforma tardia, [p=0.2] e é ela que mantém um espaço vivo. [p=0.4] {c5}Manutenção miúda: [p=0.2] os consertos pequenos, "
        "[p=0.2] feitos sempre."),
    dict(id="27", block="questao3", text=
        "{t}*Pause o vídeo.* [p=0.3] Esse texto é dedutivo ou indutivo? [p=0.2] Onde está a tese? [p=1.5] {a}Indutivo. [p=0.3] Três "
        "casos, [p=0.2] e a lição *no fim:* [p=0.2] o detetive revelando o culpado. [p=0.4] {b}Agora, as alternativas. [p=0.4] "
        "{al}A: [p=0.2] defende, desde a primeira frase, que pichações devem ser punidas com rigor. [p=0.4] {bl}B: [p=0.2] relata "
        "casos particulares e só no final explicita a tese de que a manutenção constante é preferível à reforma tardia."),
    dict(id="28", block="questao3", text=
        "{cl}C: [p=0.2] apresenta a tese no primeiro período e a retoma, com outras palavras, no último. [p=0.4] {dl}D: [p=0.2] tem "
        "como ideia central a insegurança na entrada do posto de saúde. [p=0.4] {el}E: [p=0.2] não apresenta tese, limitando-se a "
        "descrever problemas de um bairro. [p=0.5] {p}*Pause e dê o nome do erro de cada uma.* [p=1.5]"),
    dict(id="29", block="questao3", text=
        "{t}Vamos conferir. [p=0.3] {c}C: [p=0.2] tese no primeiro período, [p=0.2] ou seja, na primeira frase. [p=0.2] É o *dedutivo,* [p=0.2] e este texto é indutivo. [p=0.4] {e}E: [p=0.2] "
        "sem tese? [p=0.2] É o segundo erro clássico: [p=0.2] a tese está na última frase. [p=0.4] {d}D: [p=0.2] um dos três casos: "
        "[p=0.2] *redução.* [p=0.4] {a}A: [p=0.2] punir pichação? [p=0.2] O texto não fala em punição: [p=0.2] *extrapolação.* [p=0.4] "
        "{ok}Sobra a B: [p=0.2] casos primeiro, [p=0.2] tese no fim. [p=0.2] *Letra B.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] dedutivo: [p=0.2] tese no começo. [p=0.2] Indutivo: [p=0.2] "
        "tese no fim. [p=0.2] Implícito: [p=0.2] tese em lugar nenhum. [p=0.5] {b}Dois: [p=0.2] há quem diga [p=0.2] é a voz do outro, "
        "[p=0.2] não a do autor. [p=0.5] {c}Três: [p=0.2] leia até o primeiro mas."),

    # ================= PONTE =================
    dict(id="31", block="ponte", text=
        "{t}O texto deixa *placas* pelo caminho: [p=0.3] {a}o título, [p=0.2] {b}o começo dos parágrafos, [p=0.2] {c}e algumas "
        "palavrinhas. [p=0.4] {d}Próximo episódio: [p=0.2] *as pistas que entregam a tese.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *Linguagens do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já marcou a primeira frase como tese? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
