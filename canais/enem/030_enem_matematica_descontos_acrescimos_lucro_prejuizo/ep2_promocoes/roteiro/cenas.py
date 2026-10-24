# Roteiro — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 2 de 4: descontos encadeados, preço original, promoções e faixas
# Base: Estudos/Enem/estudos/01-matematica/15-descontos-acrescimos-lucro-prejuizo.html — seções 02, 06 e 07 + Questões 6, 5 e 8
#   (seção 12) + a QUESTÃO NOVA do prompt (no lugar da Questão 3, que repete a Questão 6 de Porcentagem).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Cada desconto ou acréscimo é um CARIMBO no preço: carimbos se MULTIPLICAM, não se somam, e a ordem não muda o resultado.
#   O desconto efetivo é a CONTA DO CAIXA: quanto você paga dividido pelo que você leva.
#   Desconto por faixa é como encher os ANDARES DE UM PRÉDIO: cada andar tem a sua taxa, e a do último não desce.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula".
# Exemplos dos blocos: os do material/prompt (R$ 200,00 com liquidação, Pix e frete; 10% e 10%; 25% e 20%; +25% e −20%;
#   tabela de promoções; faixas com compra de R$ 500,00). Exemplos NOSSOS: o pacote de R$ 10,00 na "segunda com 50%"
#   (10 + 5 = 15 de 20) e as 4 unidades de R$ 10,00 no "leve 3, pague 2" (paga 30 de 40 → 25%).
#   ERRO 2 com números nossos (R$ 68,00 depois de 15% → 68 ÷ 0,85 = 80; o erro dá 68 · 1,15 = 78,20): o prompt usava
#   R$ 102,00 → 120, que é a resposta da Questão 6 ("nós fazemos", com pausa) logo depois.
# Atalhos (verde): junte os carimbos num fator só (0,8 · 0,9 · 1,1 = 0,792) · desconto efetivo pela conta em unidades
#   (1 − pagas/levadas) · conferência multiplicando de volta.
# QUESTÃO NOVA (texto do prompt): 300 · 0,80 · 0,95 · 1,10 = 300 · 0,836 = 250,80 → C. Erradas (do prompt): A 228 esqueceu o
#   frete; B 247,50 somou os descontos (25%) e depois o frete; D 255 somou tudo (−15%); E 258 frete sobre a etiqueta.
# QUESTÃO 6 (material): 102 ÷ 0,85 = 120 → D. Erradas (do material): C 117,30 = +15% sobre 102; B 117 = somou 15 reais;
#   A 86,70 = descontou 15% de novo; E 680 = dividiu por 0,15.
# QUESTÃO 5 (material): I 48,00 · III 50,40 · II 54,00 → A (I, III, II). Erradas (do material): D lê "50% na segunda" como 50%
#   sobre tudo (36,00) e põe a II em primeiro; B compara os números anunciados (50% > 30%) e põe a II antes da III;
#   C e E acham "leve 3, pague 2" menor que 30%; a E ainda inverte a II e a I.
# QUESTÃO 8 (material): 0 + 0,05 · 200 + 0,10 · 200 = 30 → 600 − 30 = 570 → D. Erradas (do material): B 540 = 10% sobre tudo;
#   A 510 = 15% sobre tudo; C 560 = 10% sobre tudo o que passa de 200; E 580 = só a faixa mais alta.
# Frases-chave (meio e fim, idênticas): 1. Descontos e acréscimos em sequência: multiplique os fatores.
#   2. Para voltar ao preço original, divida pelo fator. 3. Toda promoção vira desconto efetivo antes da comparação.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Promoção desmascarada: descontos encadeados, preço original e faixas · Matemática ENEM, Descontos episódio 2"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Na mesma loja, [p=0.2] *segunda unidade com cinquenta por cento de desconto* [p=0.3] {b}e *trinta por cento em "
        "cada unidade.* [p=0.4] {c}Qual é a melhor? [p=0.5] {d}A de cinquenta parece imbatível, [p=0.3] {e}mas dá só "
        "*vinte e cinco por cento* de desconto. [p=0.5] {f}Hoje você aprende a *desmascarar promoção.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *encadear* descontos e acréscimos, [p=0.3] {b}recuperar o *preço "
        "original,* [p=0.3] {c}*comparar promoções* [p=0.3] {d}e calcular *descontos por faixa.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, trinta segundos da série de Porcentagem. [p=0.3] {a}Cada porcentagem vira um *fator,* [p=0.2] o número "
        "que multiplica o preço: [p=0.2] mais quinze por cento, [p=0.2] vezes *um vírgula quinze;* [p=0.2] menos trinta, "
        "[p=0.2] vezes *zero vírgula setenta.* [p=0.4] {b}Vários em sequência: [p=0.2] *multiplique os fatores.* [p=0.4] "
        "{c}E para voltar ao valor anterior, [p=0.2] *divida pelo fator.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Três cenas de compra. [p=0.3] {a}O *carrinho on-line,* [p=0.2] com cupom, [p=0.2] desconto no Pix [p=0.2] e "
        "*frete* no final. [p=0.4] {b}O cartaz do mercado: [p=0.2] *leve três, pague dois.* [p=0.4] {c}E a loja de "
        "material de construção [p=0.2] com *desconto progressivo.* [p=0.4] {d}Hoje a gente traduz os três para a mesma "
        "língua."),

    # ================= BLOCO A: CARIMBOS =================
    dict(id="05", block="carimbos", text=
        "{t}E quando aparece um *acréscimo* no meio dos descontos? [p=0.4] {a}Um produto de *duzentos reais,* [p=0.2] "
        "com vinte por cento de liquidação, [p=0.2] dez no Pix [p=0.2] e dez de frete. [p=0.4] {b}Cada porcentagem é um "
        "*carimbo* no preço. [p=0.2] Carimbos em fila são *descontos encadeados.* [p=0.4] {c}Vezes zero vírgula oitenta, "
        "[p=0.2] vezes zero vírgula noventa: [p=0.2] *cento e quarenta e quatro.* [p=0.4] {d}O frete, vezes um vírgula "
        "dez, [p=0.2] sobre o valor *já descontado:* [p=0.2] *cento e cinquenta e oito e quarenta.*"),
    dict(id="06", block="carimbos", text=
        "{t}E se o frete viesse primeiro? [p=0.4] {a}Duzentos, [p=0.2] vezes um vírgula dez, [p=0.2] vezes zero vírgula "
        "oitenta, [p=0.2] vezes zero vírgula noventa: [p=0.4] {b}*o mesmo cento e cinquenta e oito e quarenta.* [p=0.4] "
        "{c}Carimbos se *multiplicam,* [p=0.2] e *a ordem não muda o resultado.*"),
    dict(id="07", block="atalho1", text=
        "{t}Atalho: [p=0.2] junte os carimbos *antes.* [p=0.4] {a}Zero vírgula oito, [p=0.2] vezes zero vírgula nove, "
        "[p=0.2] vezes um vírgula um: [p=0.2] *zero vírgula setecentos e noventa e dois,* [p=0.2] o *fator total.* [p=0.4] "
        "{b}Duzentos vezes ele: [p=0.2] cento e cinquenta e oito e quarenta. [p=0.4] {c}Uma multiplicação só no preço."),

    # ================= BLOCO B: DESCONTO TOTAL EQUIVALENTE =================
    dict(id="08", block="equivalente", text=
        "{t}Dois descontos de dez por cento dão vinte? [p=0.4] {a}Zero vírgula nove vezes zero vírgula nove: [p=0.2] "
        "*zero vírgula oitenta e um.* [p=0.2] Você paga oitenta e um por cento. [p=0.4] {b}O *desconto total "
        "equivalente,* [p=0.2] o desconto único que faz o mesmo efeito, [p=0.2] é *um menos o produto dos fatores:* "
        "[p=0.2] *dezenove por cento.* [p=0.4] {c}Vinte e cinco com vinte: [p=0.2] zero vírgula setenta e cinco vezes "
        "zero vírgula oito, [p=0.2] zero vírgula seis. [p=0.2] Desconto de *quarenta,* [p=0.2] não quarenta e cinco."),

    # ================= BLOCO C: VOLTAR AO PREÇO =================
    dict(id="09", block="voltar", text=
        "{t}Um preço subiu vinte e cinco por cento. [p=0.2] Que desconto faz ele voltar? [p=0.4] {a}Para voltar, [p=0.2] "
        "*divida pelo fator,* [p=0.2] um vírgula vinte e cinco. [p=0.4] {b}E dividir por um vírgula vinte e cinco [p=0.2] "
        "é multiplicar por *zero vírgula oito:* [p=0.2] *vinte por cento* de desconto bastam. [p=0.4] {c}Por isso subir "
        "vinte e descontar vinte [p=0.2] termina *quatro por cento abaixo,* [p=0.2] como você viu em Porcentagem."),

    # ================= BLOCO D: DESCONTO EFETIVO =================
    dict(id="10", block="efetivo", text=
        "{t}E *leve três, pague dois:* [p=0.2] quanto de desconto é isso? [p=0.4] {a}Faça a *conta do caixa:* [p=0.2] "
        "quanto você paga [p=0.2] dividido pelo que você leva. [p=0.2] O que falta para cem por cento [p=0.2] é o "
        "*desconto efetivo,* [p=0.2] o desconto real. [p=0.4] {b}Paga dois de três: [p=0.2] desconto de um terço, "
        "[p=0.2] *trinta e três vírgula três por cento.* [p=0.4] {c}*Leve quatro, pague três:* [p=0.2] *vinte e cinco.*"),
    dict(id="11", block="efetivo", text=
        "{t}E a do gancho, [p=0.2] *segunda com cinquenta?* [p=0.4] {a}Um pacote de dez reais: [p=0.2] o par sai por dez "
        "mais cinco, [p=0.2] *quinze de vinte.* [p=0.4] {b}Desconto efetivo: [p=0.2] *vinte e cinco.* [p=0.4] "
        "{c}*Segunda grátis:* [p=0.2] cinquenta. [p=0.2] *Segunda com trinta:* [p=0.2] um vírgula sete de dois, [p=0.2] "
        "*quinze.* [p=0.4] {d}No gancho, [p=0.2] os trinta em cada unidade *ganham.*"),

    # ================= BLOCO E: A QUANTIDADE CERTA =================
    dict(id="12", block="quantidade", text=
        "{t}E se você levar *quatro* no leve três, pague dois? [p=0.4] {a}A promoção vale *de três em três:* [p=0.2] a "
        "quarta sai pelo *preço cheio.* [p=0.4] {b}Com o pacote de dez: [p=0.2] quarenta reais de preço cheio, [p=0.2] "
        "paga *trinta.* [p=0.4] {c}Desconto efetivo: [p=0.2] *vinte e cinco,* [p=0.2] não trinta e três. [p=0.2] Depende "
        "de *quantas você compra.*"),
    dict(id="13", block="atalho2", text=
        "{t}Atalho para promoção por quantidade. [p=0.4] {a}Conte em unidades: [p=0.2] *quantas você paga sobre quantas "
        "você leva.* [p=0.4] {b}O desconto efetivo [p=0.2] é *um menos essa fração.* [p=0.4] {c}Nem precisa do preço."),

    # ================= BLOCO F: DESCONTO POR FAIXA =================
    dict(id="14", block="faixa", text=
        "{t}E o desconto progressivo? [p=0.4] {a}É o *desconto por faixa:* [p=0.2] cada parte do valor [p=0.2] ganha a "
        "taxa da sua faixa. [p=0.4] {b}Pense num *prédio.* [p=0.2] Térreo, até duzentos reais: [p=0.2] *nada.* [p=0.2] "
        "Primeiro andar, até quatrocentos: [p=0.2] *cinco por cento.* [p=0.2] Cobertura, acima de quatrocentos: [p=0.2] "
        "*dez.* [p=0.4] {c}Uma compra de *quinhentos* enche duzentos, [p=0.2] duzentos [p=0.2] e cem. [p=0.4] {d}Zero, "
        "[p=0.2] mais *dez* reais, [p=0.2] mais *dez* reais: [p=0.2] desconto de *vinte reais.*"),
    dict(id="15", block="faixa", text=
        "{t}E dez por cento em tudo? [p=0.4] {a}Daria *cinquenta reais,* [p=0.2] mais que o *dobro* do correto. [p=0.4] "
        "{b}A taxa do último andar [p=0.2] *não desce* para os de baixo. [p=0.4] {c}Conta por partes [p=0.2] tem série "
        "própria, [p=0.2] em funções definidas por partes."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Na promoção *leve cinco, pague quatro,* [p=0.2] qual é o desconto efetivo? [p=0.4] "
        "{b}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Conta do caixa: [p=0.2] paga quatro de cada cinco, [p=0.2] *oitenta por cento.* "
        "[p=0.4] {b}Desconto efetivo: [p=0.2] *vinte por cento.* [p=0.4] {c}Quanto mais unidades por brinde, [p=0.2] "
        "menor o desconto."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] descontos e acréscimos em sequência: [p=0.2] multiplique "
        "os fatores. [p=0.5] {b}Dois: [p=0.2] para voltar ao preço original, [p=0.2] divida pelo fator. [p=0.5] {c}Três: "
        "[p=0.2] toda promoção vira desconto efetivo [p=0.2] antes da comparação."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar descontos sucessivos.* [p=0.2] Trinta e mais "
        "dez, [p=0.2] quarenta. [p=0.4] {b}Parece certo, [p=0.2] porque os dois são do mesmo produto. [p=0.4] {c}Mas o "
        "segundo incide sobre um preço *menor:* [p=0.2] zero vírgula sete vezes zero vírgula nove, [p=0.2] *trinta e sete "
        "por cento.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] voltar ao preço *somando* o desconto. [p=0.2] Sessenta e oito reais depois de quinze por "
        "cento, [p=0.2] mais quinze por cento, [p=0.2] setenta e oito e vinte. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "pôr de volta os quinze *parece* desfazer. [p=0.4] {c}Mas os quinze eram do preço *antigo,* que é maior. [p=0.2] "
        "Divida por zero vírgula oitenta e cinco: [p=0.2] *oitenta reais.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] ler *cinquenta na segunda* [p=0.2] como cinquenta de desconto. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o cinquenta está *enorme* no cartaz. [p=0.4] {c}Mas vale para *uma unidade em duas:* [p=0.2] "
        "sobre o par, [p=0.2] *vinte e cinco.*"),
    dict(id="22", block="erros", text=
        "{a}Quarto: [p=0.2] usar a taxa da *faixa mais alta* [p=0.2] no valor todo. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque a compra *chegou* na faixa dos dez. [p=0.4] {c}Mas os dez por cento só pegam a parte que *passou* dos "
        "quatrocentos."),

    # ================= QUESTÃO NOVA (EU FAÇO) =================
    dict(id="23", block="qn", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um produto tem preço "
        "de etiqueta de *trezentos reais.* [p=0.2] Na liquidação, há *vinte por cento* de desconto; [p=0.2] quem paga com "
        "Pix ganha mais *cinco por cento* de desconto sobre o valor já reduzido; [p=0.2] e a entrega acrescenta *dez por "
        "cento* de frete sobre o valor pago pelo produto. [p=0.2] O cliente que compra com Pix e com entrega paga, no "
        "total: [p=0.4] {qa}A: [p=0.2] duzentos e vinte e oito reais. [p=0.3] {qb}B: [p=0.2] duzentos e quarenta e sete e "
        "cinquenta. [p=0.3] {qc}C: [p=0.2] duzentos e cinquenta e oitenta. [p=0.3] {qd}D: [p=0.2] duzentos e cinquenta e "
        "cinco. [p=0.3] {qe}E: [p=0.2] duzentos e cinquenta e oito reais."),
    dict(id="24", block="qn", text=
        "{t}Três carimbos. [p=0.4] {a}Vezes zero vírgula oitenta, [p=0.2] vezes zero vírgula noventa e cinco, [p=0.2] "
        "vezes um vírgula dez. [p=0.4] {b}Fator total: [p=0.2] *zero vírgula oitocentos e trinta e seis.* [p=0.4] "
        "{c}Trezentos vezes ele: [p=0.2] *duzentos e cinquenta reais e oitenta centavos.* [p=0.4] {d}Plausível? [p=0.2] "
        "Os descontos pesam mais que o frete, [p=0.2] então fica abaixo de trezentos. [p=0.3] {ok}*Letra C!*"),
    dict(id="25", block="qn", text=
        "{t}E as outras? [p=0.3] {xa}A A *esqueceu o frete.* [p=0.4] {xb}A B *somou* os descontos, [p=0.2] vinte e cinco "
        "por cento, [p=0.2] e depois pôs o frete. [p=0.4] {xd}A D somou *tudo:* [p=0.2] menos quinze por cento. [p=0.4] "
        "{xe}E a E pôs o frete sobre a *etiqueta,* [p=0.2] não sobre o valor pago."),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="26", block="q6", text=
        "{t}A próxima, a gente faz junto. [p=0.3] {a}Após um desconto de *quinze por cento,* [p=0.2] uma camiseta passou "
        "a custar *cento e dois reais.* [p=0.2] O preço da camiseta antes do desconto era: [p=0.4] {qa}A: [p=0.2] oitenta "
        "e seis e setenta. [p=0.3] {qb}B: [p=0.2] cento e dezessete. [p=0.3] {qc}C: [p=0.2] cento e dezessete e trinta. "
        "[p=0.3] {qd}D: [p=0.2] cento e vinte. [p=0.3] {qe}E: [p=0.2] seiscentos e oitenta reais. [p=0.5] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="27", block="q6", text=
        "{t}O desconto foi um carimbo de *zero vírgula oitenta e cinco.* [p=0.4] {a}Para voltar, [p=0.2] *divida pelo "
        "fator:* [p=0.2] cento e dois dividido por zero vírgula oitenta e cinco, [p=0.2] *cento e vinte reais.* [p=0.4] "
        "{b}Conferindo: [p=0.2] cento e vinte vezes zero vírgula oitenta e cinco, [p=0.2] cento e dois. [p=0.3] "
        "{ok}*Letra D!* [p=0.4] {xc}A C pôs quinze por cento sobre os *cento e dois.* [p=0.3] {xb}A B somou quinze "
        "*reais.* [p=0.3] {xa}A A descontou *de novo.* [p=0.3] {xe}E a E dividiu por zero vírgula *quinze.*"),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="28", block="q5", text=
        "{t}Agora é *sua.* [p=0.3] {a}Uma pessoa precisa comprar *seis unidades* de um produto vendido por *doze reais* a "
        "unidade. [p=0.2] Três lojas fazem promoções diferentes: [p=0.2] loja um, [p=0.2] leve três, pague dois; [p=0.2] "
        "loja dois, [p=0.2] segunda unidade com cinquenta por cento de desconto; [p=0.2] loja três, [p=0.2] trinta por "
        "cento de desconto em cada unidade. [p=0.2] Ordenando as lojas da mais barata para a mais cara, [p=0.2] obtém-se: "
        "[p=0.4] {qa}A: [p=0.2] um, três, dois. [p=0.3] {qb}B: [p=0.2] um, dois, três. [p=0.3] {qc}C: [p=0.2] três, um, "
        "dois. [p=0.3] {qd}D: [p=0.2] dois, um, três. [p=0.3] {qe}E: [p=0.2] três, dois, um. [p=0.5] {p}*Pause o vídeo e "
        "resolva.* [p=2.0]"),
    dict(id="29", block="q5", text=
        "{t}Conferindo, [p=0.2] em reais. [p=0.2] Preço cheio das seis: [p=0.2] *setenta e dois.* [p=0.4] {a}Loja um: "
        "[p=0.2] paga quatro de seis, [p=0.2] *quarenta e oito.* [p=0.4] {b}Loja dois: [p=0.2] três pares de dezoito, "
        "[p=0.2] *cinquenta e quatro.* [p=0.4] {c}Loja três: [p=0.2] setenta e dois vezes zero vírgula setenta, [p=0.2] "
        "*cinquenta e quarenta.* [p=0.4] {d}Ordem: [p=0.2] um, três, dois. [p=0.3] {ok}*Letra A!*"),
    dict(id="30", block="q5", text=
        "{t}E as outras? [p=0.3] {xd}A D leu cinquenta na segunda [p=0.2] como cinquenta *sobre tudo.* [p=0.4] {xb}A B "
        "comparou os números do cartaz [p=0.2] sem fazer conta. [p=0.4] {xc}A C [p=0.2] {xe}e a E [p=0.2] acharam o leve "
        "três, pague dois [p=0.2] menor que trinta por cento. [p=0.2] Mas ele é *um terço.*"),

    # ================= QUESTÃO 8 (VOCÊ FAZ) =================
    dict(id="31", block="q8", text=
        "{t}E a última, [p=0.2] também *sua.* [p=0.3] {a}Uma loja de material de construção dá desconto progressivo: "
        "[p=0.2] nenhum desconto sobre os primeiros *duzentos reais* da compra, [p=0.2] *cinco por cento* sobre a parte "
        "entre duzentos e quatrocentos, [p=0.2] e *dez por cento* sobre a parte que exceder quatrocentos. [p=0.2] Um "
        "cliente fez uma compra de *seiscentos reais.* [p=0.2] Ele pagou: [p=0.4] {qa}A: [p=0.2] quinhentos e dez. "
        "[p=0.3] {qb}B: [p=0.2] quinhentos e quarenta. [p=0.3] {qc}C: [p=0.2] quinhentos e sessenta. [p=0.3] {qd}D: "
        "[p=0.2] quinhentos e setenta. [p=0.3] {qe}E: [p=0.2] quinhentos e oitenta reais. [p=0.5] {p}*Pause e encha o "
        "prédio.* [p=2.0]"),
    dict(id="32", block="q8", text=
        "{t}Seiscentos enchem os três andares: [p=0.2] *duzentos, duzentos e duzentos.* [p=0.4] {a}Térreo, zero. [p=0.2] "
        "Primeiro andar, [p=0.2] *dez.* [p=0.2] Cobertura, [p=0.2] dez por cento de duzentos, [p=0.2] *vinte.* [p=0.4] "
        "{b}Desconto de *trinta:* [p=0.2] pagou *quinhentos e setenta.* [p=0.3] {ok}*Letra D!* [p=0.4] {xb}A B pôs dez "
        "por cento em *tudo;* [p=0.2] {xa}a A, quinze. [p=0.4] {xc}A C pulou o andar dos cinco. [p=0.4] {xe}E a E [p=0.2] "
        "só descontou a cobertura."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] descontos e acréscimos em sequência: [p=0.2] "
        "multiplique os fatores. [p=0.5] {b}Dois: [p=0.2] para voltar ao preço original, [p=0.2] divida pelo fator. "
        "[p=0.5] {c}Três: [p=0.2] toda promoção vira desconto efetivo [p=0.2] antes da comparação."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Uma loja coloca *cinquenta por cento sobre o custo* na etiqueta [p=0.3] {b}e, na liquidação, [p=0.2] dá *um "
        "terço* de desconto. [p=0.5] {c}Ela ainda lucra? [p=0.5] {d}Próximo episódio."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual promoção já te enganou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
