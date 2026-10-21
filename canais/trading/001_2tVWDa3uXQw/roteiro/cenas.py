# Roteiro em PT-BR — "Fair Value Gap: quais operar, onde entrar e quais ignorar"
# Marcações:
#   {cue}     -> dispara uma animação no instante da próxima palavra
#   *texto*   -> palavra(s) em destaque (negrito) na legenda
#   [p=1.5]   -> pausa de narração (segundos)

TITULO = "Fair Value Gap: quais operar, onde entrar e quais ignorar"

# Como a voz deve pronunciar (a legenda mantém o texto original)
PRONUNCIA = {
    "ICT": "I C T",
    "CE": "C E",
    "FVG": "F V G",
    "Consequent": "Cónsequent",
    "Encroachment": "Encróutchment",
}

SCENES = [
    # ---------------- ABERTURA ----------------
    dict(id="01", block="hook", text=
        "Ninguém te conta isso sobre os *Fair Value Gaps.* [p=0.5] "
        "{a}A maioria dos traders entra no instante em que o preço *toca o gap...* [p=0.4] "
        "{b}e é *estopada* logo antes do movimento acontecer."),
    dict(id="02", block="promessa", text=
        "Até o final deste vídeo, você vai saber {a}*quais* Fair Value Gaps operar, [p=0.3] "
        "{b}exatamente *onde entrar,* [p=0.3] {c}e quais deles *ignorar.*"),

    # ---------------- O QUE É ----------------
    dict(id="03", block="definicao", text=
        "Vamos começar pelo básico. [p=0.3] {a}Isto é um *Fair Value Gap.* [p=0.4] "
        "São *três candles:* [p=0.2] {c1}candle *um,* [p=0.2] {c2}candle *dois,* [p=0.2] {c3}e candle *três.*"),
    dict(id="04", block="definicao", text=
        "Agora observe {w1}o *pavio* do candle um... [p=0.2] {w3}e o *pavio* do candle três. [p=0.4] "
        "{gap}Eles *não se tocam.* [p=0.3] Esse *espaço vazio* entre eles é o Fair Value Gap. [p=0.3] "
        "{pt}Em português, algo como *lacuna de valor justo.*"),
    dict(id="05", block="definicao", text=
        "{col}As *cores* dos candles não importam. [p=0.3] {wk}Só os *pavios* importam."),
    dict(id="06", block="definicao", text=
        "Mas por que isso é importante? [p=0.4] "
        "{a}O candle dois se moveu *tão rápido* que o preço negociou em *uma única direção* naquela região. [p=0.4] "
        "{b}O ICT ensina que o preço gosta de *voltar* para *reequilibrar* essa área. [p=0.4] "
        "{c}Por isso, quando o preço retorna ao Fair Value Gap, é ali que você procura a sua *entrada.*"),
    dict(id="07", block="alta", text=
        "Esta é a versão *de alta.* [p=0.3] {a}O preço sobe rápido, e o gap fica *abaixo.* [p=0.3] "
        "{b}Você espera o preço *voltar* para dentro dele."),
    dict(id="08", block="baixa", text=
        "E esta é a versão *de baixa.* [p=0.3] {a}O preço cai rápido, e o gap fica *acima.* [p=0.3] "
        "{b}Você espera o preço *subir de volta* para dentro dele."),

    # ---------------- QUAIS OPERAR ----------------
    dict(id="09", block="filtro", text=
        "Agora, atenção: [p=0.3] {t}*nem todo* Fair Value Gap vale a pena ser operado. [p=0.4] "
        "Os que realmente importam aparecem depois de *três coisas.*"),
    dict(id="10", block="filtro", text=
        "{s}Um: [p=0.2] o preço *varre a liquidez.* [p=0.3] "
        "{s2}Ele captura uma máxima ou uma mínima onde os *stops* estão acumulados."),
    dict(id="11", block="filtro", text=
        "{d}Dois: [p=0.2] *deslocamento.* [p=0.2] {d2}Candles *grandes e rápidos* na direção contrária."),
    dict(id="12", block="filtro", text=
        "{b}Três: [p=0.2] o preço *quebra a estrutura.* [p=0.4] "
        "{f}O Fair Value Gap que se forma *dentro* desse deslocamento... [p=0.3] {ok}é esse que você opera."),

    # ---------------- ONDE ENTRAR ----------------
    dict(id="13", block="ce", text=
        "E você *não entra na borda* do gap. [p=0.2] Você entra *no meio.* [p=0.4] "
        "{ce}O meio do Fair Value Gap é chamado de *Consequent Encroachment,* [p=0.2] ou CE. [p=0.3] "
        "{pct}Na prática, é o ponto de *cinquenta por cento* do gap."),
    dict(id="14", block="ce", text=
        "{top}A borda superior te coloca na operação *cedo demais.* [p=0.4] "
        "{bot}A borda inferior, muitas vezes, o preço *nem alcança.* [p=0.4] "
        "{mid}O meio é o *equilíbrio* entre as duas."),
    dict(id="15", block="falha", text=
        "E mais um detalhe. [p=0.3] Se o *corpo* de um candle fechar completamente *através* do Fair Value Gap... [p=0.3] "
        "{f}o gap *falhou.* [p=0.4] {i}O ICT chama isso de *Inversion Fair Value Gap,* e ele *inverte* de função. [p=0.3] "
        "Mas esse é assunto para um vídeo inteiro."),

    # ---------------- EXEMPLO 1: NOVA YORK (COMPRA) ----------------
    dict(id="16", block="ny", text=
        "Agora, vamos ver isso no *gráfico.* [p=0.3] {s}Esta é a sessão de *Nova York,* "
        "logo depois das nove e meia da manhã, no horário de Nova York. [p=0.3] {dn}O preço está *caindo* na abertura."),
    dict(id="17", block="ny", text=
        "Bem aqui, temos {eq}*mínimas iguais.* [p=0.3] Os stops estão posicionados logo *abaixo* delas. [p=0.3] "
        "{ssl}Isso é *liquidez do lado vendedor.*"),
    dict(id="18", block="ny", text=
        "Agora, observe. [p=0.4] {sw}O preço desce *abaixo* das mínimas iguais, e os stops são *capturados.* [p=0.3] "
        "{lab}*Liquidez varrida.* [p=0.3] {cl}E veja o candle: ele *fecha de volta acima.*"),
    dict(id="19", block="ny", text=
        "Agora, o *deslocamento.* [p=0.2] {d1}Um, [p=0.2] {d2}dois, [p=0.2] {d3}três. [p=0.2] "
        "Candles verdes, *grandes e rápidos.* [p=0.3] {bos}O preço *quebra a estrutura* logo acima desta máxima."),
    dict(id="20", block="ny", text=
        "E dentro desse movimento, {fvg}está o nosso *Fair Value Gap.* [p=0.3] "
        "{w1}Pavio do candle *um.* [p=0.2] {w3}Pavio do candle *três.* [p=0.2] Eles *não se tocam.*"),
    dict(id="21", block="ny", text=
        "{m}Meça o Fair Value Gap, *do topo até a base.* [p=0.3] {ce}O meio é o *CE,* o ponto de cinquenta por cento. [p=0.3] "
        "{en}Essa é a sua *entrada.*"),
    dict(id="22", block="ny", text=
        "Agora, nós *esperamos.* [p=0.3] {pb}O preço recua para dentro do gap... [p=0.4] {tc}e *toca o meio.* [p=0.3] "
        "{lg}*Compra.* [p=0.3] {sl}Stop loss *abaixo* da mínima da varrida. [p=0.3] "
        "{tp}Alvo na *liquidez do lado comprador,* acima da máxima."),
    dict(id="23", block="ny", text=
        "{run}Agora é deixar o mercado *trabalhar.* [p=3.0] {hit}*Alvo atingido.*"),
    dict(id="24", block="ny", text=
        "Repare no que aconteceu. [p=0.3] {st}O preço *nem chegou perto* do stop. [p=0.3] "
        "A varrida já tinha *tirado os vendedores* do mercado, antes mesmo de entrarmos."),
    dict(id="25", block="ny", text=
        "E repare no *horário.* [p=0.3] {kz}Tudo isso aconteceu dentro da *Kill Zone de Nova York,* "
        "entre *sete e dez da manhã,* no horário de Nova York."),
    dict(id="26", block="resumo", text=
        "{s1}Varrida. [p=0.4] {s2}Deslocamento. [p=0.4] {s3}Quebra de estrutura. [p=0.4] "
        "{s4}Fair Value Gap. [p=0.4] {s5}Entrada no meio."),

    # ---------------- EXEMPLO 2: LONDRES (VENDA) ----------------
    dict(id="27", block="ldn", text=
        "Agora, a *direção oposta.* [p=0.3] {s}Esta é a sessão de *Londres,* por volta das três da manhã, no horário de Nova York. [p=0.3] "
        "{up}O preço está *subindo.* [p=0.3] Bem aqui, {oh}há uma *máxima antiga.* [p=0.3] "
        "{bsl}A *liquidez do lado comprador* está acima dela."),
    dict(id="28", block="ldn", text=
        "{sw}O preço *ultrapassa* a máxima, captura os stops, [p=0.2] {cl}e *fecha de volta abaixo.* [p=0.3] "
        "{lab}*Liquidez varrida.*"),
    dict(id="29", block="ldn", text=
        "Agora, o deslocamento *para baixo.* [p=0.2] {d1}Um, [p=0.2] {d2}dois. [p=0.3] "
        "{bos}O preço *quebra a estrutura* abaixo desta mínima. [p=0.3] "
        "{fvg}E aqui está o Fair Value Gap, posicionado *acima* do preço."),
    dict(id="30", block="ldn", text=
        "{m}Meça do topo até a base. [p=0.2] {ce}O meio é o *CE.* [p=0.2] Essa é a sua *entrada.* [p=0.3] "
        "{pb}O preço recua para cima, entra no gap... [p=0.3] {tc}e *toca o meio.* [p=0.3] {sh}*Venda.* [p=0.3] "
        "{sl}Stop loss *acima* da máxima da varrida. [p=0.3] {tp}Alvo na *liquidez do lado vendedor,* abaixo da mínima."),
    dict(id="31", block="ldn", text=
        "{run}Agora, deixe *correr.* [p=3.0] {hit}*Alvo atingido.* [p=0.4] Os mesmos *cinco passos,* só que *invertidos.*"),

    # ---------------- MAIS DE UM FVG ----------------
    dict(id="32", block="multi", text=
        "Agora, um ponto em que muita gente *se confunde.* [p=0.3] E se o movimento deixar *mais de um* Fair Value Gap? [p=0.4] "
        "{sw}Aqui, o preço varre a mínima... [p=0.2] {run}e sobe *com força.* [p=0.3] "
        "{f1}Um Fair Value Gap *aqui...* [p=0.3] {f2}e outro *aqui,* mais acima. [p=0.4] Qual deles você opera?"),
    dict(id="33", block="multi", text=
        "{bk}Aquele criado pelos candles que *quebraram a estrutura.* [p=0.4] "
        "{l1}Este de baixo se formou *antes* do preço romper a máxima. [p=0.3] "
        "{l2}Este de cima se formou *exatamente quando* o preço rompeu. [p=0.3] {ok}*É esse.*"),
    dict(id="34", block="multi", text=
        "{m}Meça do topo até a base. [p=0.2] {ce}O meio é a sua *entrada.* [p=0.3] "
        "{pb}O preço recua, *ignora* o nível do primeiro gap... [p=0.3] {tc}e toca o meio daquele que *quebrou a estrutura.* [p=0.3] "
        "{lg}*Compra.* [p=0.2] {sl}Stop abaixo da mínima da varrida. [p=0.2] {tp}Alvo na liquidez acima da máxima. [p=0.3] "
        "{run}Deixe correr. [p=2.8] {hit}*Alvo atingido.*"),

    # ---------------- ERRO 1: SEM VARRIDA ----------------
    dict(id="35", block="erro1", text=
        "Agora, a operação que mais *estopa* as pessoas. [p=0.4] {up}O preço sobe, [p=0.2] {fvg}um Fair Value Gap se forma, [p=0.2] "
        "{pb}o preço volta para dentro dele. [p=0.3] {lg}*Compra.* [p=1.2] {slh}*Stop loss atingido.* [p=0.4] Então... o que faltou?"),
    dict(id="36", block="erro1", text=
        "{rw}Vamos *voltar.* [p=0.3] Olhe *antes* do movimento. [p=0.3] {ns}*Não houve varrida.* "
        "O preço não capturou nenhuma liquidez antes. [p=0.3] "
        "O ICT ensina que a varrida é o *combustível* do movimento. [p=0.2] Sem ela, o Fair Value Gap *não tem nada por trás.* [p=0.4] "
        "{ed}E veja a entrada: bem na *borda superior* do gap. [p=0.2] Não no meio."),
    dict(id="37", block="erro1", text=
        "{ok}Esta é a operação *correta.* [p=0.2] Espere o preço *varrer a mínima* primeiro. [p=0.3] "
        "{sw}Bem aqui. [p=0.2] {lab}*Liquidez varrida.* [p=0.3] {d}Deslocamento. [p=0.2] {bos}Quebra de estrutura. [p=0.2] "
        "{fvg}Um *novo* Fair Value Gap. [p=0.3] {ce}O meio é a sua entrada. [p=0.3] {lg}*Compra.* [p=0.2] "
        "{sl}Stop abaixo da mínima da varrida. [p=0.2] {tp}Alvo na liquidez acima da máxima. [p=0.3] "
        "{run}Deixe correr. [p=2.8] {hit}*Alvo atingido.*"),

    # ---------------- ERRO 2: GAP QUE FALHOU ----------------
    dict(id="38", block="erro2", text=
        "Este é o *segundo erro.* [p=0.4] {sw}O preço varre a mínima. [p=0.2] {d}Deslocamento. [p=0.2] {bos}Quebra de estrutura. [p=0.2] "
        "{fvg}Um Fair Value Gap se forma. [p=0.4] {bc}Mas olhe este candle: [p=0.2] o *corpo* dele fecha completamente *abaixo* do gap. [p=0.3] "
        "{fail}*O gap falhou.*"),
    dict(id="39", block="erro2", text=
        "A maioria dos traders *compra mesmo assim...* [p=0.3] {st}e é estopada. [p=0.4] "
        "{rule}Se o corpo de um candle fechar através do gap *antes da sua entrada,* a operação está *cancelada.* [p=0.3] "
        "Você *não compra* um gap que falhou. [p=0.3] "
        "{w}Você espera a *próxima varrida,* o *próximo deslocamento,* e um *novo* Fair Value Gap."),
    dict(id="40", block="erro2", text=
        "{sw}Bem aqui. [p=0.2] {lab}*Liquidez varrida* de novo. [p=0.3] {d}Deslocamento. [p=0.2] {bos}Quebra de estrutura. [p=0.2] "
        "{fvg}Um Fair Value Gap *novo.* [p=0.3] {ce}O meio é a sua entrada. [p=0.3] {lg}*Compra.* [p=0.2] "
        "{sl}Stop abaixo da varrida. [p=0.2] {tp}Alvo acima da máxima. [p=0.3] {run}Deixe correr. [p=2.8] {hit}*Alvo atingido.*"),

    # ---------------- CHECKLIST ----------------
    dict(id="41", block="checklist", text=
        "Aqui está o *checklist.* [p=0.4] {i1}Um: *liquidez varrida.* [p=0.3] {i2}Dois: *deslocamento.* [p=0.3] "
        "{i3}Três: *quebra de estrutura.* [p=0.3] {i4}Quatro: um *Fair Value Gap* dentro desse movimento. [p=0.3] "
        "{i5}Cinco: entrada no *meio do gap,* o CE, com o stop *além da varrida.* [p=0.5] "
        "{x}Faltou um? [p=0.3] Então você *pula* a operação."),

    # ---------------- ENCERRAMENTO ----------------
    dict(id="42", block="cta", text=
        "Se este vídeo te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal, [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas aulas. [p=0.5] "
        "{com}E me conte nos *comentários:* qual assunto você quer que eu explique no próximo vídeo? [p=0.5] "
        "{bye}Bons trades, e *até a próxima.* [p=1.5]"),
]
