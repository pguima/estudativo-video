# Roteiro em PT-BR — "Candle Range Theory (CRT): reversão primeiro, continuação depois"
# Marcações:
#   {cue}     -> dispara uma animação no instante da próxima palavra
#   *texto*   -> palavra(s) em destaque (negrito) na legenda
#   [p=1.5]   -> pausa de narração (segundos)

TITULO = "Candle Range Theory (CRT): a estratégia completa do candle diário"

PRONUNCIA = {
    "CRT": "C R T",
    "CISD": "C I S D",
    "ICT": "I C T",
    "FVG": "F V G",
    "2R": "dois R",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "O candle diário fechou *exatamente* como você queria. [p=0.4] {a}Forte, de alta, com o corpo lá em cima. [p=0.5] "
        "{b}No dia seguinte, o preço passa da máxima... [p=0.3] {c}aparece um candle vermelho... [p=0.4] "
        "{d}e você *vende.* [p=0.6] {e}Só que o preço *nunca volta.*"),
    dict(id="02", block="hook", text=
        "E aí começa o pior erro que um trader pode cometer com um modelo claro: [p=0.4] {f}*mudar de opinião* no meio do caminho. "
        "[p=0.5] Hoje você vai aprender a *não* fazer isso."),
    dict(id="03", block="mapa", text=
        "Nesta aula, eu vou te mostrar a *Candle Range Theory,* ou CRT, na ordem *exata* em que a análise acontece. [p=0.5] "
        "{a}Primeiro, o *candle diário* que define o viés. [p=0.3] {b}Depois, a *reversão,* que é sempre a primeira opção. "
        "[p=0.3] {c}E só se ela *falhar,* a *continuação.* [p=0.5] {d}Com regras objetivas de entrada, stop e alvo."),

    # ================= O QUE É CRT =================
    dict(id="04", block="range", text=
        "Vamos começar pelo conceito. [p=0.3] {a}Todo candle tem um *range:* [p=0.2] {hi}a *máxima* [p=0.2] {lo}e a *mínima.* "
        "[p=0.4] {box}Esse intervalo entre elas é o que a CRT estuda."),
    dict(id="05", block="range", text=
        "{n}No candle seguinte, o preço costuma *buscar a liquidez* de um dos lados desse range. [p=0.4] "
        "{r}Às vezes ele toma a máxima e *volta para dentro:* [p=0.2] isso é uma *reversão.* [p=0.4] "
        "{cn}Às vezes ele rompe e *continua:* [p=0.2] isso é uma *continuação.* [p=0.4] "
        "{q}O segredo é saber *qual das duas* você está autorizado a operar."),

    # ================= PASSO 1: O DIÁRIO =================
    dict(id="06", block="diario", text=
        "{t}Passo um: *um único candle diário.* [p=0.4] Não é o gráfico de uma hora. [p=0.2] Não é o candle em que você vai clicar para comprar. "
        "[p=0.3] {d}É o candle diário que *acabou de fechar.* [p=0.4] "
        "Porque antes dele fechar, você não tem uma análise. [p=0.2] Você tem um *palpite.*"),
    dict(id="07", block="diario", text=
        "{f}E não é qualquer candle. [p=0.2] Eu quero um fechamento *forte:* [p=0.2] corpo grande, fechando *perto da máxima.* [p=0.4] "
        "{w}Um candle que ficou o dia todo indo e voltando e fechou verde por poucos pontos *não serve.* [p=0.3] "
        "O corpo não fez o trabalho."),
    dict(id="08", block="diario", text=
        "{b}Um fechamento forte de alta me dá um *viés de alta* para o dia seguinte. [p=0.4] "
        "{x}Mas atenção: [p=0.2] o diário me deixou *otimista.* [p=0.2] Ele *não* me transformou em *comprador.*"),
    dict(id="09", block="diario", text=
        "{r1}Regra número um: [p=0.2] se aparecer uma continuação, ela *só pode ser de compra.* [p=0.4] "
        "{r2}Regra número dois: [p=0.2] mesmo assim, a primeira coisa que eu procuro é a *reversão.* [p=0.4] "
        "{inv}E se o diário fechar forte *de baixa,* [p=0.2] é o mesmo modelo, *invertido.*"),
    dict(id="10", block="niveis", text=
        "{m}Agora, marque a *máxima do dia anterior* [p=0.2] {l}e a *mínima do dia anterior.* [p=0.4] "
        "{z}Essas duas linhas são o seu *range de trabalho.* [p=0.4] {g}E então, saia do diário. [p=0.2] Ele já disse o que tinha para dizer."),

    # ================= PASSO 2: A REVERSÃO =================
    dict(id="11", block="reversao", text=
        "{t}Passo dois: *a reversão vem primeiro.* [p=0.4] No gráfico de uma hora, eu quero ver o preço *passar acima* da máxima do dia anterior. "
        "[p=0.3] {run}Não um pavio rápido. [p=0.2] Eu quero que a máxima seja realmente *tomada.*"),
    dict(id="12", block="reversao", text=
        "Depois disso, eu preciso de duas confirmações *no mesmo movimento.* [p=0.4] "
        "{c1}A primeira: [p=0.2] o *corpo* do candle precisa fechar *de volta dentro do range,* abaixo da máxima do dia anterior."),
    dict(id="13", block="reversao", text=
        "{c2}A segunda: [p=0.2] um *CISD de baixa.* [p=0.3] CISD é a *mudança no estado de entrega* do preço. [p=0.4] "
        "{lv}Você pega os candles de alta que levaram o preço até a máxima, [p=0.2] e marca a *abertura* do primeiro deles. "
        "[p=0.4] {cl}Quando um corpo fecha *abaixo* dessa linha, o fluxo virou."),
    dict(id="14", block="reversao", text=
        "{ok}Fechou de volta no range, *e* deu CISD de baixa? [p=0.3] Essa é a sua *reversão.* [p=0.4] "
        "{tr}Entrada na confirmação, [p=0.2] stop acima da máxima que foi tomada, [p=0.2] e alvo fixo de *2R.*"),
    dict(id="15", block="pavio", text=
        "{t}E aqui está a regra que mais protege o seu dinheiro: [p=0.4] {w}*pavio não é fechamento.* [p=0.4] "
        "{wk}Não importa se o pavio rejeitou bonito. [p=0.3] {bd}O que confirma é o *corpo* fechando. [p=0.3] "
        "{nc}Sem fechamento, *sem reversão.*"),

    # ================= PASSO 3: A FALHA =================
    dict(id="16", block="falha", text=
        "{t}Passo três: [p=0.2] tomada a máxima, só existe *uma pergunta.* [p=0.3] {q}O preço fechou *de volta para dentro?* [p=0.5] "
        "{l}Se fechou, com CISD, é a reversão. [p=0.2] Você opera e *não procura outra ideia.*"),
    dict(id="17", block="falha", text=
        "{r}Mas olhe este outro cenário. [p=0.3] {bc}Aparece um candle de baixa, [p=0.2] tem pavio, parece uma rejeição... [p=0.4] "
        "{ab}só que o corpo continua *acima* da máxima do dia anterior. [p=0.5] {f}A reversão *falhou.*"),
    dict(id="18", block="falha", text=
        "{n1}E agora vem a parte difícil. [p=0.3] Não é esperar *mais um candle* para ver se a venda funciona. [p=0.3] "
        "{n2}Também não é decidir que o diário estava errado. [p=0.5] "
        "{two}São *dois fatos* ao mesmo tempo: [p=0.2] o diário *continua de alta,* [p=0.2] e a ideia de venda *morreu.*"),
    dict(id="19", block="falha", text=
        "{go}Só agora, *e não antes,* você está autorizado a procurar a *continuação.*"),

    # ================= PASSO 4: A CONTINUAÇÃO =================
    dict(id="20", block="continua", text=
        "{t}Passo quatro: *a continuação.* [p=0.4] {a}O preço já fechou acima da máxima do dia anterior. [p=0.3] "
        "É por isso que essa operação existe. [p=0.4] {pb}Agora eu espero um *recuo* até uma região de interesse: "
        "[p=0.2] {poi}um *Fair Value Gap,* [p=0.2] ou um *ponto de swing.*"),
    dict(id="21", block="continua", text=
        "{nr}Não um candle vermelho qualquer no meio do movimento, que você *achou* que está barato. [p=0.4] "
        "{lv}Dentro da região, eu quero o *CISD de alta:* [p=0.2] o preço fecha *acima* da abertura dos candles de baixa que fizeram a mínima. "
        "[p=0.4] {cb}Esse é o meu *bloco de continuação.*"),
    dict(id="22", block="continua", text=
        "{ag}E ele precisa *concordar* com o diário. [p=0.3] Diário de alta, só bloco de alta. [p=0.3] "
        "Se não concorda, *não tem operação.* [p=0.2] Você não força."),
    dict(id="23", block="continua", text=
        "{en}A entrada é na *abertura do candle seguinte* à confirmação. [p=0.4] "
        "{sl}O stop vai onde a ideia é *invalidada:* abaixo da mínima que formou o bloco. [p=0.4] "
        "{tp}E o alvo é fixo: [p=0.2] *2R.*"),
    dict(id="24", block="continua", text=
        "{s1}Não aperte o stop só para a operação parecer melhor. [p=0.3] {s2}E não transforme um alvo de 2R em seis R, "
        "só porque o diário parece forte. [p=0.4] {s3}A força do diário *já foi usada:* [p=0.2] ela definiu o viés."),

    # ================= EXEMPLO 1: CONTINUAÇÃO =================
    dict(id="25", block="ex1", text=
        "{t}Vamos ver isso num exemplo real. [p=0.3] {d}No diário, o preço fechou *forte,* acima de três candles de baixa. "
        "[p=0.3] {b}Viés de alta para o dia seguinte."),
    dict(id="26", block="ex1", text=
        "{h1}No gráfico de uma hora, eu marco a máxima do dia anterior. [p=0.3] É a única coisa que importa agora. [p=0.4] "
        "{run}O preço sobe e *toma* essa máxima."),
    dict(id="27", block="ex1", text=
        "{in}Logo depois, um candle fecha *de volta abaixo* da máxima. [p=0.3] Isso já me dá uma operação? [p=0.4] "
        "{no}*Não.* [p=0.2] Porque não teve CISD. [p=0.3] {cl}Nenhum corpo fechou abaixo da linha do CISD. "
        "[p=0.4] Você precisa das *duas* coisas."),
    dict(id="28", block="ex1", text=
        "{fl}A reversão falhou. [p=0.3] O mercado continua de alta. [p=0.4] {fvg}E veja: o recuo terminou dentro de um *Fair Value Gap.* "
        "[p=0.4] {cisd}Dali, o preço fecha acima dos dois candles de baixa que fizeram a mínima. [p=0.3] {cb}Bloco de continuação."),
    dict(id="29", block="ex1", text=
        "{en}Entrada na abertura do candle seguinte. [p=0.3] {sl}Stop abaixo da mínima do bloco. [p=0.3] {tp}Alvo de 2R. "
        "[p=0.3] {run}Agora é deixar o mercado trabalhar. [p=2.8] {hit}*Alvo atingido.*"),

    # ================= EXEMPLO 2: REVERSÃO =================
    dict(id="30", block="ex2", text=
        "{t}Agora, um exemplo de *reversão.* [p=0.3] {d}O diário fecha *acima* da máxima do candle anterior, e perto da própria máxima. "
        "[p=0.3] Fechamento forte. [p=0.4] {m}Marco a máxima e a mínima desse candle, [p=0.2] e desço para uma hora."),
    dict(id="31", block="ex2", text=
        "{run}O preço toma a máxima do dia anterior. [p=0.3] {lv}A linha do CISD fica na abertura dos *dois* candles de alta que fizeram o topo. "
        "[p=0.4] {wk}Mas o preço só *fura com pavio.* [p=0.3] Pavio não é fechamento. [p=0.2] Eu espero."),
    dict(id="32", block="ex2", text=
        "{nh}Então o preço faz uma *nova máxima,* com um único candle de alta. [p=0.4] {nl}Esse candle passa a ser o meu *novo* CISD. "
        "[p=0.4] {cl}E agora o corpo fecha *abaixo* dele."),
    dict(id="33", block="ex2", text=
        "Duas perguntas. [p=0.3] {q1}Tomou a máxima do dia anterior? [p=0.2] *Sim.* [p=0.3] {q2}Deu CISD de baixa, fechando de volta no range? "
        "[p=0.2] *Sim.* [p=0.4] {ok}Venda válida."),
    dict(id="34", block="ex2", text=
        "{en}Entrada na confirmação. [p=0.3] {sl}Stop *acima da máxima,* que é onde a ideia é invalidada. [p=0.3] {tp}Alvo de 2R. "
        "[p=0.3] {run}Deixe correr. [p=2.6] {hit}*Alvo atingido.*"),
    dict(id="35", block="ex2", text=
        "{pdl}Repare que o outro lado do range, a *mínima do dia anterior,* é o próximo alvo natural. [p=0.4] "
        "Mas isso não acontece sempre. [p=0.3] {simple}Para manter simples: *pegue os 2R* e espere o próximo setup."),

    # ================= RESUMO =================
    dict(id="36", block="fluxo", text=
        "Vamos juntar tudo. [p=0.4] {s1}Candle diário forte define o viés. [p=0.3] {s2}Marque a máxima e a mínima do dia anterior. "
        "[p=0.3] {s3}No gráfico de uma hora, espere o preço tomar um dos lados."),
    dict(id="37", block="fluxo", text=
        "{q}Fechou de volta no range com CISD? [p=0.3] {y}Opere a *reversão.* [p=0.4] "
        "{n}Não fechou? [p=0.2] {c}Procure a *continuação:* [p=0.2] recuo para um FVG ou swing, CISD a favor do diário, "
        "entrada, stop na invalidação e alvo de 2R."),
    dict(id="38", block="fluxo", text=
        "{k}A entrada nunca foi a parte mais importante. [p=0.3] O importante é saber em *qual operação* você está autorizado a estar."),

    # ================= ENCERRAMENTO =================
    dict(id="39", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal, [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas aulas. [p=0.5] "
        "{com}E me conte nos *comentários:* você costuma operar a reversão ou a continuação? [p=0.5] "
        "{bye}Bons trades, e *até a próxima.* [p=1.5]"),
]
