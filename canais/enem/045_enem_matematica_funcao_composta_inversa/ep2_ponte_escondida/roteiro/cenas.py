# Roteiro — Função Composta e Função Inversa, Episódio 2 de 5: composição em contexto e a função escondida
# Base: Estudos/Enem/estudos/01-matematica/30-funcao-composta-inversa.html — seções 04 e 05 + Questões 1 e 4 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   MÁQUINAS EM FILA (a do episódio 1): o que sai da primeira entra na segunda.
#   A GRANDEZA INTERMEDIÁRIA É A PONTE: você atravessa por ela e ela some da resposta.
#   A DE DENTRO RECEBE O QUE VOCÊ TEM; A DE FORA ENTREGA O QUE VOCÊ QUER.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material: balão h(t) = 0,2t e T(h) = 25 − 6h → 25 − 1,2t; aos 10 min, 13 °C; tabela das cadeias;
#   caso 2, g(x) = x + 1 e f(g(x)) = x² + 2x → f(u) = u² − 1.
# DESVIO DO PROMPT (bloco d e erro 4): o caso 1 do prompt (f(x) = 3x − 2 e f(g(x)) = 6x + 7) é exatamente a Questão 4,
#   que é "você faz". O bloco usa um exemplo nosso: f(x) = 2x + 5 e f(g(x)) = 8x − 1 → 2g(x) + 5 = 8x − 1 →
#   g(x) = 4x − 3 (confere: f(4x − 3) = 8x − 1). O erro 4 usa o mesmo exemplo: parar em 2g(x) = 8x − 6 ou passar o +5
#   sem trocar o sinal (g = 4x + 2, que dá f = 8x + 9).
# Erros 1 a 3: usam os números do exercício "nós fazemos" (gráfica, já resolvido), e não os da Questão 1, para não gastar
#   antes as alternativas dela: ordem trocada p(C(t)) = 50 · (20 + 0,1t) = 1 000 + 5t; somar 50 + 0,1 → 20 + 50,1t;
#   sem o fixo, 5t (R$ 50 em vez de R$ 70 aos 10 min).
# Nós fazemos (prompt): p(t) = 50t, C(p) = 20 + 0,1p → C(p(t)) = 20 + 5t; aos 10 min, 500 páginas e R$ 70 pelos dois caminhos.
# QUESTÃO 1 ("eu faço", texto idêntico na tela): C(n(t)) = 500 + 3 · 40t = 500 + 120t → C. Erradas como no material:
#   A ordem errada n(C(t)) = 40(500 + 3t) = 20 000 + 120t; B soma 40 + 3; D usa t como se fosse o número de peças;
#   E esquece o custo fixo. Conferência em 2 h: 80 peças, R$ 740,00.
# QUESTÃO 4 ("você faz", com pausa): 3g(x) − 2 = 6x + 7 → 3g(x) = 6x + 9 → g(x) = 2x + 3 → E. Erradas como no material:
#   A calcula f(6x + 7) = 18x + 19; B para em 3g(x) = 6x + 9; C passa o −2 sem trocar o sinal (3g = 6x + 5);
#   D erra o sinal ao dividir o 9. Conferência: f(2x + 3) = 6x + 9 − 2 = 6x + 7.
# Atalhos (verde): "multiplique as taxas" (0,2 km/min · 6 °C/km = 1,2 °C/min, o km se cancela; acréscimo nosso) ·
#   "confira com um número" (x = 1 no caso 1: g(1) = 1, f(1) = 7 e 8 · 1 − 1 = 7).
# Contas conferidas em ../trabalho/conferir_contas.py.
# Frases-chave (meio e fim, idênticas): 1. A grandeza que aparece nas duas fórmulas é a ponte.
#   2. Substitua a ponte e ela some da resposta. 3. Achou a função escondida? Monte a composta de novo e confira.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Função composta no ENEM: junte duas fórmulas numa só · Matemática ENEM, Composta e Inversa ep. 2"

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
        "{a}Um balão sobe *zero vírgula dois quilômetro por minuto,* [p=0.3] {b}e a cada quilômetro o ar esfria *seis "
        "graus.* [p=0.4] {c}Que temperatura ele encontra aos *dez minutos?* [p=0.4] {d}Dá para responder com *uma "
        "fórmula só,* [p=0.2] em que a altitude *nem aparece.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *juntar duas fórmulas* de um enunciado numa só [p=0.3] {b}e descobrir "
        "uma *função escondida* dentro de uma composta."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] *f de g de x* se lê de dentro para fora; [p=0.2] "
        "o que sai da de dentro entra na de fora. [p=0.4] {b}Da série de Função Afim: [p=0.2] *custo* é o *fixo* "
        "[p=0.2] mais o *preço por unidade* vezes a *quantidade.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense no balão subindo. [p=0.3] {a}Mais tempo, [p=0.2] *mais alto.* [p=0.2] Mais alto, [p=0.2] *mais frio.* "
        "[p=0.4] {b}Agora uma fábrica, [p=0.2] com um relógio e uma pilha de peças: [p=0.2] mais horas, mais peças, "
        "mais custo. [p=0.4] {c}Tempo, altura, temperatura, reais: [p=0.2] tudo isso é *grandeza,* [p=0.2] algo que dá "
        "para medir."),

    # ================= BLOCO A: A ESTRATÉGIA =================
    dict(id="05", block="estrategia", text=
        "{t}E como o ENEM monta essa questão? [p=0.4] {a}Com *duas fórmulas* [p=0.2] ligadas por uma *grandeza "
        "intermediária,* [p=0.2] a que aparece *nas duas.* [p=0.4] {b}Ela é uma *ponte:* [p=0.2] você atravessa por "
        "ela, [p=0.2] e ela some da resposta. [p=0.4] {c}A estratégia: [p=0.2] *substituir* a ponte, [p=0.2] trocar a "
        "letra dela pelo que ela vale."),

    # ================= BLOCO B: O BALÃO =================
    dict(id="06", block="balao", text=
        "{t}Vamos ao balão. [p=0.3] {a}A altitude, em quilômetros, [p=0.2] depois de *t* minutos: [p=0.2] *h de t igual "
        "a zero vírgula dois t.* [p=0.4] {b}A temperatura, em graus: [p=0.2] *T de h igual a vinte e cinco, menos seis "
        "h.* [p=0.4] {c}Quem aparece nas duas? [p=0.2] A *altitude.* [p=0.2] Ela é a ponte."),
    dict(id="07", block="balao", text=
        "{t}Agora, substitua. [p=0.3] {a}No lugar do *h,* [p=0.2] ponha *zero vírgula dois t:* [p=0.2] vinte e cinco, "
        "menos seis vezes zero vírgula dois t. [p=0.4] {b}Fica *vinte e cinco, menos um vírgula dois t.* [p=0.4] {c}Aos "
        "dez minutos: [p=0.2] vinte e cinco menos doze, [p=0.2] *treze graus.* [p=0.4] {d}E a altitude *sumiu* da "
        "fórmula."),
    dict(id="08", block="atalho", text=
        "{t}Confere pelo caminho longo? [p=0.4] {a}Aos dez minutos, [p=0.2] o balão está a *dois quilômetros;* [p=0.2] "
        "lá, vinte e cinco menos doze, [p=0.2] *treze.* [p=0.4] {b}Atalho: [p=0.2] *multiplique as taxas.* [p=0.2] Zero "
        "vírgula dois quilômetro por minuto, [p=0.2] vezes seis graus por quilômetro: [p=0.4] {c}o quilômetro se "
        "cancela, [p=0.2] e sobra *um vírgula dois grau por minuto.*"),

    # ================= BLOCO C: AS CADEIAS =================
    dict(id="09", block="cadeias", text=
        "{t}E quem vai dentro, [p=0.2] e quem vai fora? [p=0.4] {a}Veja as cadeias: [p=0.2] tempo, peças, custo; "
        "[p=0.2] tempo, altitude, temperatura; [p=0.2] dólar, real, imposto. [p=0.4] {b}A *de dentro* [p=0.2] recebe o "
        "que você *tem.* [p=0.4] {c}A *de fora* [p=0.2] entrega o que você *quer.* [p=0.4] {d}Tem o tempo, quer o "
        "custo? [p=0.2] Dentro, as peças; fora, o custo."),

    # ================= BLOCO D: CASO 1 =================
    dict(id="10", block="caso1", text=
        "{t}E se a prova *esconder* uma das funções? [p=0.4] {a}Caso um: [p=0.2] você conhece a *de fora.* [p=0.2] *f "
        "de x igual a dois x mais cinco,* [p=0.2] e *f de g de x igual a oito x menos um.* [p=0.4] {b}Trate o *g de x* "
        "como uma *incógnita:* [p=0.2] uma caixa fechada com o valor que você procura. [p=0.4] {c}A f dobra e soma "
        "cinco: [p=0.2] *dois vezes a caixa, mais cinco, [p=0.2] igual a oito x menos um.*"),
    dict(id="11", block="caso1", text=
        "{t}Agora, abra a caixa. [p=0.3] {a}Passe o *mais cinco* para o outro lado, [p=0.2] *trocando o sinal:* [p=0.2] "
        "dois vezes a caixa [p=0.2] igual a oito x menos seis. [p=0.4] {b}Divida *tudo* por dois: [p=0.2] *quatro x "
        "menos três.* [p=0.4] {c}A função escondida era *g de x igual a quatro x menos três.*"),

    # ================= BLOCO E: CASO 2 =================
    dict(id="12", block="caso2", text=
        "{t}E se você conhecer a *de dentro?* [p=0.4] {a}Caso dois: [p=0.2] *g de x igual a x mais um,* [p=0.2] e *f de "
        "g de x igual a x ao quadrado, mais dois x.* [p=0.4] {b}Chame o que entra na f de *u:* [p=0.2] u é x mais um, "
        "[p=0.2] então *x é u menos um.* [p=0.4] {c}Troque: [p=0.2] u menos um, ao quadrado, [p=0.2] mais duas vezes u "
        "menos um. [p=0.4] {d}Desenvolva, [p=0.2] e sobra *f de x igual a x ao quadrado, menos um.*"),

    # ================= BLOCO F: SEMPRE CONFIRA =================
    dict(id="13", block="confira", text=
        "{t}E como ter certeza? [p=0.4] {a}*Sempre confira:* [p=0.2] monte a composta de novo com a função achada. "
        "[p=0.4] {b}No caso um: [p=0.2] f de quatro x menos três [p=0.2] é oito x menos seis, mais cinco: [p=0.2] *oito "
        "x menos um.* [p=0.2] Confere. [p=0.4] {c}Atalho: [p=0.2] teste com *x igual a um.* [p=0.2] g de um é um, "
        "[p=0.2] f de um é sete, [p=0.2] e oito menos um, *sete.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma gráfica imprime *p de t igual a cinquenta t* páginas em *t* minutos. [p=0.4] {b}O "
        "custo de *p* páginas é *C de p igual a vinte, mais zero vírgula um p,* reais. [p=0.4] {c}Qual é o custo em "
        "função do *tempo,* [p=0.2] e quanto custam *dez minutos?* [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}A ponte são as *páginas.* [p=0.2] No lugar do *p,* [p=0.2] ponha cinquenta t: "
        "[p=0.2] vinte, mais zero vírgula um vezes cinquenta t. [p=0.4] {b}Fica *vinte, mais cinco t.* [p=0.4] {c}Dez "
        "minutos: [p=0.2] vinte mais cinquenta, [p=0.2] *setenta reais.* [p=0.4] {d}Pelo caminho longo: [p=0.2] "
        "*quinhentas páginas,* [p=0.2] vinte mais cinquenta, [p=0.2] *setenta.* [p=0.2] Bateu."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a grandeza que aparece nas duas fórmulas é a ponte. "
        "[p=0.5] {b}Dois: [p=0.2] substitua a ponte e ela some da resposta. [p=0.5] {c}Três: [p=0.2] achou a função "
        "escondida? [p=0.2] Monte a composta de novo e confira."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] compor na *ordem errada,* [p=0.2] jogando o "
        "custo dentro da fórmula das páginas: [p=0.2] mil mais cinco t. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "qualquer encaixe das duas fórmulas dá uma fórmula. [p=0.4] {c}Mas a de dentro recebe o que você *tem:* [p=0.2] "
        "o tempo."),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] *somar* cinquenta mais zero vírgula um. [p=0.4] {b}Parece certo, [p=0.2] porque são dois "
        "números *por unidade,* lado a lado. [p=0.4] {c}Mas um encaixa no outro: [p=0.2] zero vírgula um real por "
        "página, [p=0.2] *vezes* cinquenta páginas por minuto: [p=0.2] *cinco reais por minuto.*"),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] esquecer o *custo fixo* [p=0.2] e responder só *cinco t.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque a atenção toda vai para o termo do t. [p=0.4] {c}Mas os vinte reais *continuam lá:* [p=0.2] dez "
        "minutos custam setenta, não cinquenta."),
    dict(id="20", block="erros", text=
        "{a}Quarto, [p=0.2] na função escondida: [p=0.2] parar em *dois g de x igual a oito x menos seis,* [p=0.2] sem "
        "dividir por dois, [p=0.2] ou passar o *mais cinco* sem trocar o sinal. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "a caixa já está quase sozinha. [p=0.4] {c}Mas a conferência denuncia: [p=0.2] com esses erros, [p=0.2] a "
        "composta *não* volta a oito x menos um."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="21", block="q1", text=
        "{t}Agora, uma questão do nosso material. [p=0.2] Esta, eu resolvo com você. [p=0.4] {a}Uma pequena fábrica "
        "produz *n de t igual a quarenta t* peças [p=0.2] em *t* horas de funcionamento. [p=0.2] O custo de produção, "
        "em reais, de *n* peças [p=0.2] é *C de n igual a quinhentos, mais três n.* [p=0.2] O custo em função do tempo "
        "*t* é dado por: [p=0.4] {qa}A: [p=0.2] vinte mil, mais cento e vinte t. [p=0.3] {qb}B: [p=0.2] quinhentos, "
        "mais quarenta e três t. [p=0.3] {qc}C: [p=0.2] quinhentos, mais cento e vinte t. [p=0.3] {qd}D: [p=0.2] "
        "quinhentos, mais três t. [p=0.3] {qe}E: [p=0.2] cento e vinte t. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{t}A ponte é o *número de peças:* [p=0.2] tenho o tempo, quero o custo. [p=0.4] {a}No lugar do *n,* [p=0.2] "
        "ponha quarenta t: [p=0.2] quinhentos, mais três vezes quarenta t. [p=0.4] {b}Fica *quinhentos, mais cento e "
        "vinte t.* [p=0.4] {c}Confira em duas horas: [p=0.2] *oitenta peças,* [p=0.2] quinhentos mais duzentos e "
        "quarenta, [p=0.2] *setecentos e quarenta;* [p=0.2] pela fórmula, o mesmo. [p=0.4] {ok}*Letra C!*"),
    dict(id="23", block="q1", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] compôs na *ordem errada:* [p=0.2] quarenta vezes o custo. [p=0.3] "
        "{xb}A B [p=0.2] *somou* quarenta e três. [p=0.3] {xd}A D [p=0.2] usou o *t* como se fosse o número de peças. "
        "[p=0.3] {xe}E a E [p=0.2] *esqueceu* o custo fixo."),

    # ================= QUESTÃO 4 (VOCÊ FAZ) =================
    dict(id="24", block="q4", text=
        "{t}E a última é *sua.* [p=0.4] {a}Sejam *f* e *g* funções afins, [p=0.2] com *f de x igual a três x menos "
        "dois,* [p=0.2] e *f de g de x igual a seis x mais sete,* [p=0.2] para todo x real. [p=0.2] A lei de *g* é: "
        "[p=0.4] {qa}A: [p=0.2] dezoito x mais dezenove. [p=0.3] {qb}B: [p=0.2] seis x mais nove. [p=0.3] {qc}C: "
        "[p=0.2] dois x, mais cinco terços. [p=0.3] {qd}D: [p=0.2] dois x menos três. [p=0.3] {qe}E: [p=0.2] dois x "
        "mais três. [p=0.5] {p}*Pause e resolva.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{t}Conferindo. [p=0.2] Você conhece a *de fora.* [p=0.4] {a}A caixa é o *g de x:* [p=0.2] três vezes a caixa, "
        "menos dois, [p=0.2] igual a seis x mais sete. [p=0.4] {b}Passe o menos dois, trocando o sinal: [p=0.2] seis x "
        "mais nove. [p=0.4] {c}Divida tudo por três: [p=0.2] *dois x mais três.* [p=0.4] {d}Confira: [p=0.2] f de dois "
        "x mais três [p=0.2] é seis x mais nove, menos dois: [p=0.2] *seis x mais sete.* [p=0.4] {ok}*Letra E!*"),
    dict(id="26", block="q4", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] aplicou a f *sobre a composta.* [p=0.3] {xb}A B [p=0.2] não *dividiu "
        "por três.* [p=0.3] {xc}A C [p=0.2] passou o menos dois *sem trocar o sinal.* [p=0.3] {xd}E a D [p=0.2] errou o "
        "sinal ao dividir o nove."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a grandeza que aparece nas duas fórmulas é a "
        "ponte. [p=0.5] {b}Dois: [p=0.2] substitua a ponte e ela some da resposta. [p=0.5] {c}Três: [p=0.2] achou a "
        "função escondida? [p=0.2] Monte a composta de novo e confira."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}A corrida de táxi custa *quatro vírgula cinco, mais dois vírgula cinco x* reais. [p=0.4] {b}Você tem *trinta "
        "e sete reais:* [p=0.2] quantos quilômetros pode andar? [p=0.4] {c}E qual fórmula faz essa conta [p=0.2] para "
        "*qualquer* valor? [p=0.5] {d}Próximo episódio: [p=0.2] a função que *desfaz.*"),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] que duas grandezas do seu dia a dia [p=0.2] se ligam por uma terceira? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
