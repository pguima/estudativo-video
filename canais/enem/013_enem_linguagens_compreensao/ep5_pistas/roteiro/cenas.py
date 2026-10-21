# Roteiro — Compreensão Global e Tese, Episódio 5: As pistas que entregam a tese (aula para iniciantes)
# Base: Estudos/Enem/estudos/05-linguagens/01-compreensao-global-tese.html — seção 05 + Questões 5 e 7 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: as palavras-sinal são PLACAS DE TRÂNSITO do texto.
#   CURVA (mas, porém, no entanto, engano): a direção vai mudar, e a opinião do autor vem agora.
#   CHEGADA (portanto, assim, logo, em suma): lá vem a conclusão.
#   OPINIÃO (é preciso, deveria, é um erro; e também defendo, acredito): o autor está avaliando.
# Só a FUNÇÃO de cada parágrafo (a estrutura argumentativa completa terá série própria).
# Sequência eu faço → nós fazemos → você faz: Questão 5 (título como hipótese) → 4 frases soltas "qual placa?"
#   → Questão 7 (pausa para dar a função dos três parágrafos antes das alternativas).
# Classificação das erradas (resolução do material + nomes do ep. 3):
#   Q5: B contradição (toma como posição do autor o que vem antes do "Mas") · C não está no texto (aumento de preço) ·
#   D redução (detalhe de um exemplo) · E extrapolação (vendedor enganou) · certa A.
#   Q7: D parágrafo errado (descreve o 3º) · A função errada (a posição está no 1º e no 3º) · C não está no texto
#   (inventa uma voz contrária) · E troca o assunto (preço de aparelhos novos) · certa B.
# Frases-chave (meio e fim, idênticas):
#   1. O título é hipótese; o texto confirma.
#   2. Mas, porém, engano: lá vem a opinião do autor.
#   3. Para que serve este parágrafo?
# Cores: azul = tese/definição · verde = pista/palavra-sinal · amarelo = armadilha · vermelho = erro · roxo = regra.
# Textos-base (Questões 5 e 7: título, texto, comando e alternativas) lidos EXATAMENTE como no material.

TITULO = "As placas que entregam a tese: título, parágrafos e palavras-sinal — Linguagens ENEM, episódio 5"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Antes de chegar à tese, [p=0.2] o texto já te avisou onde ela está. [p=0.5] {b}Só que quase ninguém repara "
        "*nas placas.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai usar o título, [p=0.2] o começo dos parágrafos [p=0.2] e algumas palavrinhas "
        "[p=0.2] para achar a tese mais rápido, [p=0.3] {b}e responder às questões de *função do parágrafo.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Duas lembranças. [p=0.3] {a}Episódio um: [p=0.2] a *tese* é o que o texto afirma. [p=0.4] {b}Episódio quatro: [p=0.2] "
        "ela costuma ficar no começo, [p=0.2] no fim, [p=0.2] ou em lugar nenhum. [p=0.3] {c}Hoje, [p=0.2] as pistas que "
        "mostram onde."),

    # ================= AS PLACAS (CONCRETO) =================
    dict(id="04", block="estrada", text=
        "{t}Pense numa estrada. [p=0.3] {a}Antes da curva, [p=0.2] uma placa avisa: [p=0.2] curva à frente. [p=0.4] {b}Antes da "
        "cidade, [p=0.2] outra: [p=0.2] chegada. [p=0.4] {c}Você ainda não viu a curva, [p=0.2] mas já sabe que ela vem. [p=0.4] "
        "{d}O texto faz o mesmo. [p=0.2] Ele também tem *placas.*"),

    # ================= BLOCO A: O TÍTULO =================
    dict(id="05", block="titulo", text=
        "{t}Qual é a primeira placa do texto? [p=0.4] {a}O *título:* [p=0.2] o nome que vem em cima do texto. [p=0.4] {b}Às vezes, "
        "[p=0.2] ele anuncia só o *assunto:* [p=0.2] Feiras livres. [p=0.4] {c}Às vezes, [p=0.2] já entrega a *tese:* [p=0.2] "
        "O barato que sai caro. [p=0.4] {d}Quando entrega a tese, [p=0.2] é a melhor pista que você tem, [p=0.2] antes de ler uma linha."),

    # ================= BLOCO B: TÍTULO DE EFEITO ENGANA =================
    dict(id="06", block="efeito", text=
        "{t}Mas toda placa diz a verdade? [p=0.4] {a}Tem título feito só para chamar atenção. [p=0.3] {b}Título irônico, [p=0.2] "
        "que diz uma coisa querendo dizer outra. [p=0.4] {c}Título em pergunta: [p=0.2] O fim do livro? [p=0.4] {d}E trocadilho, "
        "[p=0.2] o jogo de palavras. [p=0.4] {e}Esses títulos podem dizer o *contrário* do que o texto defende."),
    dict(id="07", block="efeito", text=
        "{t}Então, o que fazer com o título? [p=0.4] {a}Use como *hipótese:* [p=0.2] um palpite, [p=0.2] que ainda precisa ser "
        "conferido. [p=0.4] {b}Leia o título, [p=0.2] imagine a tese, [p=0.3] {c}e *confirme* no corpo do texto."),

    # ================= BLOCO C: PARAGRAFAÇÃO =================
    dict(id="08", block="paragrafos", text=
        "{t}E a segunda placa? [p=0.3] {a}Está no começo de cada *parágrafo:* [p=0.2] cada bloco de texto que começa numa linha "
        "nova. [p=0.4] {b}O jeito como o texto se divide em parágrafos [p=0.2] se chama *paragrafação.* [p=0.4] {c}E cada parágrafo "
        "costuma tratar de *um* tema só."),
    dict(id="09", block="paragrafos", text=
        "{t}Onde esse tema aparece? [p=0.4] {a}Muitas vezes, [p=0.2] na *primeira frase* do parágrafo. [p=0.4] {b}Essa frase que "
        "anuncia o parágrafo [p=0.2] se chama *tópico frasal.* [p=0.4] {c}Leia a primeira frase de cada parágrafo, [p=0.2] e você "
        "já tem o esqueleto do texto."),
    dict(id="10", block="paragrafos", text=
        "{t}E num texto que defende uma opinião? [p=0.4] {a}O primeiro parágrafo [p=0.2] apresenta o assunto e a tese. [p=0.4] "
        "{b}Os do meio [p=0.2] trazem os argumentos. [p=0.4] {c}E o último [p=0.2] retoma a tese, [p=0.2] ou propõe uma solução."),

    # ================= BLOCO D: A PERGUNTA-CHAVE =================
    dict(id="11", block="pergunta", text=
        "{t}E como isso cai na prova? [p=0.4] {a}O ENEM pergunta: [p=0.2] qual a função do segundo parágrafo? [p=0.4] {b}Função "
        "é o trabalho que ele faz no texto. [p=0.4] {c}A pergunta que resolve é uma só: [p=0.3] *para que serve este parágrafo?* "
        "[p=0.4] {d}Apresentar o problema? [p=0.2] Explicar por quê? [p=0.2] Propor uma solução?"),

    # ================= BLOCO E: AS PALAVRAS-SINAL =================
    dict(id="12", block="sinais", text=
        "{t}E a terceira placa? [p=0.3] {a}São palavrinhas que avisam o que vem depois. [p=0.3] Elas se chamam *palavras-sinal.* "
        "[p=0.3] {b}Muitos livros dizem *marcas linguísticas.* [p=0.2] É a mesma coisa. [p=0.4] {c}A primeira é a placa de *curva:* "
        "[p=0.2] mas, [p=0.2] porém, [p=0.2] no entanto, [p=0.2] engano. [p=0.4] {d}A direção vai mudar, [p=0.2] e a opinião do "
        "autor vem agora."),
    dict(id="13", block="sinais", text=
        "{a}A segunda é a placa de *chegada:* [p=0.2] portanto, [p=0.2] assim, [p=0.2] logo, [p=0.2] em suma. [p=0.4] {b}Lá vem a "
        "*conclusão:* [p=0.2] o ponto aonde o texto queria chegar."),
    dict(id="14", block="sinais", text=
        "{a}E a terceira é a placa de *opinião:* [p=0.2] é preciso, [p=0.2] deveria, [p=0.2] é um erro. [p=0.4] {b}O autor está "
        "*avaliando.* [p=0.4] {c}Nela entram também as palavras em que o autor fala por si: [p=0.2] defendo, [p=0.2] acredito. "
        "[p=0.4] {d}Viu uma dessas placas? [p=0.2] A tese está *por perto.*"),

    # ================= BLOCO F: A PALAVRA QUE VOLTA =================
    dict(id="15", block="volta", text=
        "{t}E tem uma última pista. [p=0.3] {a}Qual palavra aparece em quase todos os parágrafos? [p=0.4] {b}Ela indica o *assunto.* "
        "[p=0.4] {c}E o que o texto afirma com mais força sobre ela, [p=0.2] perto de uma placa, [p=0.3] {d}indica a *tese.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Agora é com você. [p=0.3] Quatro frases soltas. [p=0.2] *Pause e diga qual placa é esta.* [p=0.4] {a}Um: [p=0.2] "
        "Portanto, a cidade precisa de mais ciclovias. [p=0.4] {b}Dois: [p=0.2] Muitos acham que o livro vai acabar, [p=0.2] porém "
        "as bibliotecas estão cheias. [p=0.4] {c}Três: [p=0.2] É preciso investir no transporte público. [p=0.4] {d}Quatro: "
        "[p=0.2] Defendo que a escola comece mais tarde. [p=1.5]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Um: [p=0.2] portanto: [p=0.2] *chegada.* [p=0.4] {b}Dois: [p=0.2] porém: [p=0.2] *curva.* "
        "[p=0.2] E repare: [p=0.2] o que vem antes do porém [p=0.2] é a ideia que o autor derruba. [p=0.4] {c}Três: [p=0.2] é preciso: "
        "[p=0.2] *opinião.* [p=0.4] {d}Quatro: [p=0.2] defendo: [p=0.2] *opinião* também, [p=0.2] o autor falando por si."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] o título é hipótese; [p=0.2] o texto confirma. [p=0.5] {b}Dois: "
        "[p=0.2] mas, [p=0.2] porém, [p=0.2] engano: [p=0.2] lá vem a opinião do autor. [p=0.5] {c}Três: [p=0.2] para que serve "
        "este parágrafo?"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] confiar num título irônico ou em forma de "
        "pergunta. [p=0.4] {b}Parece certo, [p=0.2] porque o título é a primeira coisa que o autor escreveu para você. [p=0.4] "
        "{c}Mas ele pode ser só efeito. [p=0.2] *Confirme no texto.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] tomar como posição do autor [p=0.2] a ideia que vem *antes* do mas. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque ela está escrita no texto, [p=0.2] com todas as letras. [p=0.4] {c}Mas é a placa de curva: [p=0.2] a opinião do "
        "autor vem *depois.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] descrever a função de *outro* parágrafo, [p=0.2] e não do que foi perguntado. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque a alternativa descreve mesmo alguma coisa do texto. [p=0.4] {c}Mas de outro lugar. [p=0.2] Confira: "
        "[p=0.2] *qual parágrafo a questão pediu?*"),

    # ================= QUESTÃO 5 (EU FAÇO) =================
    dict(id="22", block="questao5", text=
        "{t}Agora, eu faço. [p=0.3] {a}O comando: [p=0.2] *Em relação ao texto, o título.* [p=0.3] A questão é sobre o título. [p=0.4] "
        "{f0}O barato que sai caro [p=0.4] {c0}É um ditado. [p=0.2] Minha hipótese: [p=0.2] uma coisa barata [p=0.2] acaba custando "
        "caro. [p=0.3] Agora, vamos confirmar."),
    dict(id="23", block="questao5", text=
        "{f1}Uma camiseta pelo preço de um lanche parece vitória do consumidor. [p=0.4] {c1}Parece. [p=0.2] Guarde essa palavra. "
        "[p=0.4] {f2}Mas alguém pagou a diferença: [p=0.2] o costureiro que recebe por peça, [p=0.2] o rio que recebe o corante, "
        "[p=0.2] o aterro que recebe a roupa descartada depois de três lavagens. [p=0.4] {c2}Placa de curva! [p=0.2] O que vinha antes "
        "do mas, [p=0.2] a vitória do consumidor, [p=0.2] o autor derruba. [p=0.3] Aterro é o lugar onde o lixo é enterrado."),
    dict(id="24", block="questao5", text=
        "{f3}O preço da etiqueta é só a parte da conta que chega ao caixa; [p=0.2] o resto é dividido entre quem não estava na loja. "
        "[p=0.4] {c3}Confirmado. [p=0.2] O barato da loja sai caro para outros: [p=0.2] o trabalhador, [p=0.2] o rio, [p=0.2] o aterro. "
        "[p=0.4] {d}O título antecipou a tese."),
    dict(id="25", block="questao5", text=
        "{t}As alternativas. [p=0.3] {a}A: [p=0.2] antecipa a tese de que o preço baixo esconde custos sociais e ambientais pagos por "
        "outros. [p=0.4] {b}B: [p=0.2] contradiz o texto, que defende a compra de roupas baratas como vitória do consumidor. [p=0.4] "
        "{c}C: [p=0.2] indica que o texto tratará do aumento recente no preço das roupas. [p=0.4] {d}D: [p=0.2] refere-se apenas à "
        "baixa durabilidade das camisetas, descartadas após poucas lavagens. [p=0.4] {e}E: [p=0.2] sugere que o consumidor foi "
        "enganado pelo vendedor no momento da compra."),
    dict(id="26", block="questao5", text=
        "{b}A B toma como opinião do autor [p=0.2] o que vem antes do mas. [p=0.2] *Contradição.* [p=0.4] {d}A D fica com um detalhe "
        "de um exemplo, [p=0.2] as três lavagens: [p=0.2] *redução.* [p=0.4] {c}A C fala em aumento de preço: [p=0.2] *não está no "
        "texto.* [p=0.4] {e}A E inventa um vendedor enganador: [p=0.2] *extrapolação.* [p=0.4] {ok}Sobra a A, [p=0.2] a hipótese "
        "confirmada. [p=0.2] *Letra A.*"),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="27", block="questao7", text=
        "{t}Agora, você faz. [p=0.3] {a}O comando: [p=0.2] *Na organização do texto, o segundo parágrafo.* [p=0.3] Guarde: "
        "[p=0.2] *o segundo.* [p=0.4] {f1}Consertar um aparelho deveria ser mais simples do que comprar outro. [p=0.2] Hoje, porém, "
        "o caminho costuma ser o inverso. [p=0.4] {c1}Deveria: [p=0.2] placa de opinião. [p=0.2] Porém: [p=0.2] placa de curva."),
    dict(id="28", block="questao7", text=
        "{f2}Peças coladas em vez de parafusadas, [p=0.2] baterias que não se removem, [p=0.2] manuais técnicos que o fabricante não "
        "divulga: [p=0.2] cada um desses detalhes de projeto encarece o reparo até o ponto em que ele deixa de compensar. [p=0.4] "
        "{c2}Reparo é o conserto. [p=0.4] {f3}Leis que obriguem a oferta de peças e de informações técnicas por um prazo mínimo "
        "não resolvem tudo, [p=0.2] mas devolvem ao consumidor uma escolha que hoje lhe é tirada antes mesmo da compra."),
    dict(id="29", block="questao7", text=
        "{t}*Pause o vídeo.* [p=0.3] Para que serve cada um dos três parágrafos? [p=1.5] {a}O primeiro [p=0.2] *apresenta o problema:* "
        "[p=0.2] consertar ficou mais difícil do que trocar. [p=0.4] {b}O segundo [p=0.2] *explica por quê,* [p=0.2] com três exemplos. "
        "[p=0.4] {c}O terceiro [p=0.2] *propõe uma solução:* [p=0.2] leis."),
    dict(id="30", block="questao7", text=
        "{t}Agora, as alternativas. [p=0.3] {a}A: [p=0.2] apresenta a tese, que é retomada no terceiro parágrafo. [p=0.4] {b}B: "
        "[p=0.2] fundamenta a afirmação do primeiro parágrafo com exemplos de como o projeto dos aparelhos dificulta o conserto. "
        "[p=0.4] {c}C: [p=0.2] introduz uma opinião contrária à do autor, que é refutada no terceiro parágrafo. [p=0.4] {d}D: [p=0.2] "
        "propõe a solução defendida pelo autor para o problema apresentado. [p=0.4] {e}E: [p=0.2] abandona o assunto inicial para "
        "tratar do preço dos aparelhos novos. [p=0.5] {p}*Pause e dê o nome do erro de cada uma.* [p=1.5]"),
    dict(id="31", block="questao7", text=
        "{t}Vamos conferir. [p=0.3] {d}A D descreve o *terceiro* parágrafo, [p=0.2] não o segundo: [p=0.2] o terceiro erro clássico. "
        "[p=0.4] {a}A A erra a função: [p=0.2] a posição do autor está no primeiro e no terceiro. [p=0.4] {c}A C inventa uma opinião "
        "contrária: [p=0.2] *não está no texto.* [p=0.4] {e}A E troca o assunto: [p=0.2] o parágrafo fala do custo do conserto. "
        "[p=0.4] {ok}Sobra a B: [p=0.2] fundamenta, [p=0.2] ou seja, [p=0.2] dá a base, [p=0.2] explica por quê. [p=0.2] *Letra B.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] o título é hipótese; [p=0.2] o texto confirma. [p=0.5] "
        "{b}Dois: [p=0.2] mas, [p=0.2] porém, [p=0.2] engano: [p=0.2] lá vem a opinião do autor. [p=0.5] {c}Três: [p=0.2] para que "
        "serve este parágrafo?"),

    # ================= PONTE =================
    dict(id="33", block="ponte", text=
        "{t}E quando o texto não tem nenhuma placa, [p=0.3] {a}nenhuma frase de opinião, [p=0.3] {b}e mesmo assim defende alguma "
        "coisa? [p=0.4] {c}Próximo episódio: [p=0.2] *a tese implícita.*"),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *Linguagens do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das quatro placas você acertou? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
