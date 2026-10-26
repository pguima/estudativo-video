# Roteiro — Função Afim, Episódio 2 de 5: o coeficiente angular (taxa de variação), o linear (valor inicial) e o zero
# Base: Estudos/Enem/estudos/01-matematica/24-funcao-afim-grafico-coeficientes.html — seções 03 e 04 + Questões 3, 8 e 1
#   (seção 12). Leitura do gráfico (inclinação, crescente/decrescente) e lei por dois pontos genéricos ficam para o ep. 3.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Δy SOBRE Δx: quanto a SAÍDA andou dividido por quanto a ENTRADA andou.
#   O b É A FOTO NO INSTANTE ZERO: se a tabela começa depois do zero, volte o filme até o zero.
#   O ZERO É A HORA EM QUE ACABA: a vela some, o tanque seca, a dívida zera.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Regra de exemplos: a Q1 (vela 17 → 13, resposta 95 min) é a "você faz". A animação principal pedida (vela que rebobina
#   até 19 cm e some em 95 min) aparece SÓ na resolução da Q1, depois da pausa. Nos blocos d, f e no erro 5, a vela é
#   NOSSA: 14 cm aos 5 min, perde 0,4 cm/min → b = 16 cm, acaba em 40 min (o erro de "esquecer o tempo" dá 35 min).
#   O gancho (17 cm, 0,2 cm/min, "85 erra") é do usuário e fica igual: ele não dá os 19 cm nem os 95 min.
# Exemplos NOSSOS (marcados): x irregular (0 → 500, 1 → 440, 3 → 320: −120 em 2 h = −60); ordens trocadas
#   ((380 − 500)/(0 − 2) = +60, sinal errado); fração invertida (2/−120 ≈ −0,017); "+" na taxa (500 + 60·2 = 620 L);
#   pré-requisito 3x − 12 = 0 → x = 4. Todas as contas conferidas em Python.
# Nós fazemos (prompt): tabela de 2 em 2 (30, 26, 22, 18) → a = −2, b = 30, zero em 15 (usar −4 dá 7,5).
# QUESTÃO 3 ("eu faço"): gabarito D (20 h). Erradas = material (E 25 h esvaziar; C 15 h conta da 5ª hora;
#   A 1,25 h proporção 400/1 600; B 4 = 1 600 ÷ 400).
# QUESTÃO 8 ("nós fazemos"): gabarito C (R$ 18.000,00). Erradas = material (A perda anual 6 000; B 42 000 − 5·6 000 = 12 000,
#   desconta 5 anos quando faltam 4; D 60 000 − 2·18 000 = 24 000; E ≈ 26 000, queda de 30% a cada 3 anos = exponencial).
# QUESTÃO 1 ("você faz"): gabarito D (95 min). Erradas = material (C 85 = 17 ÷ 0,2; B 65 = 13 ÷ 0,2; A 47,5 = 19 ÷ 0,4).
#   A E (105 = 21 ÷ 0,2): o material só diz "extrapola errado a altura inicial (21 cm)"; a explicação de COMO se chega a
#   21 (somar a queda inteira de 4 cm, a dos 20 min entre as medições, em vez dos 2 cm dos 10 min iniciais) é NOSSA.
# Acréscimos NOSSOS (cenas verdes de ATALHO): cena 10 "escreva os dois pontos: segundo menos primeiro, em cima e embaixo;
#   diminui → taxa negativa"; cena 13 "voltar o filme: b = valor medido + o que se perdeu até ali"; cena 16 "decimal de
#   hora × 60 = minutos (0,3 h = 20 min, não 30)".
# Frases-chave (meio e fim, idênticas): 1. Taxa é Δy sobre Δx, com unidade e com sinal. 2. b é o valor no instante zero,
#   não o primeiro dado da tabela. 3. "Quando acaba?" pede o zero: ax + b = 0.
# Cores: azul = definição / b · roxo = regra / a · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Taxa de variação, valor inicial e o zero da função | Função Afim Ep. 2"
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
        "{a}Uma vela mede *dezessete centímetros* [p=0.2] dez minutos depois de acesa. [p=0.3] {b}Ela perde *zero vírgula "
        "dois centímetro* por minuto. [p=0.4] {c}Quem faz dezessete dividido por zero vírgula dois [p=0.2] responde "
        "*oitenta e cinco minutos* [p=0.2] e erra: [p=0.3] {d}a pergunta contava o tempo desde que a vela foi *acesa.* "
        "[p=0.4] {e}Hoje você aprende a *voltar o filme até o zero.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o segundo episódio da série de *Função afim.* [p=0.4] {a}Ao final, [p=0.2] você vai tirar a *taxa* "
        "de dois dados quaisquer, [p=0.3] {b}achar o *valor inicial* mesmo quando ele não aparece [p=0.3] {c}e "
        "responder *quando acaba?* [p=0.2] com uma conta."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] em *a x mais b,* [p=0.2] o *a* é a *taxa* "
        "[p=0.2] e o *b* é o *valor inicial.* [p=0.4] {b}E da série de Equações do primeiro grau: [p=0.2] *três x menos "
        "doze igual a zero.* [p=0.2] Passa o doze, [p=0.2] divide por três: [p=0.2] *x igual a quatro.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}O que estas três coisas têm em comum? [p=0.4] {a}Um *tanque* de quinhentos litros esvaziando, [p=0.2] com "
        "uma marca a cada hora. [p=0.4] {b}Uma *vela* acesa. [p=0.4] {c}E um *carro* que perde valor a cada ano: "
        "[p=0.2] a *depreciação.* [p=0.4] {d}Nas três, [p=0.2] algo *diminui* [p=0.2] sempre no *mesmo ritmo.*"),

    # ================= BLOCO A: A TAXA DE VARIAÇÃO =================
    dict(id="05", block="delta", text=
        "{t}Como medir esse ritmo? [p=0.4] {a}Com o *delta,* [p=0.2] uma letra grega em forma de triângulo. [p=0.3] "
        "Quer dizer *variação:* [p=0.2] o valor final menos o inicial. [p=0.4] {b}Na função afim, [p=0.2] cada vez que "
        "o x aumenta *um,* [p=0.2] o y muda *exatamente a.* [p=0.4] {c}Esse *a* é o *coeficiente angular,* [p=0.2] ou "
        "*taxa de variação.*"),
    dict(id="06", block="formula", text=
        "{t}E se eu só tiver dois pontos? [p=0.4] {a}*a igual a delta y sobre delta x:* [p=0.2] y dois menos y um, "
        "[p=0.2] sobre x dois menos x um. [p=0.4] {b}Quanto a *saída* andou, [p=0.2] dividido por quanto a *entrada* "
        "andou. [p=0.4] {c}E a taxa tem *unidade:* [p=0.2] litros *por* hora, [p=0.2] centímetros *por* minuto, "
        "[p=0.2] reais *por* ano."),

    # ================= BLOCO B: A TABELA DO TANQUE =================
    dict(id="07", block="tanque", text=
        "{t}Vamos ao tanque. [p=0.3] {a}Hora zero: [p=0.2] *quinhentos litros.* [p=0.2] Depois quatrocentos e "
        "quarenta, [p=0.2] trezentos e oitenta, [p=0.2] trezentos e vinte, [p=0.2] duzentos e sessenta. [p=0.4] {b}De "
        "uma linha para a outra: [p=0.2] *menos sessenta,* [p=0.2] sempre. [p=0.4] {c}A taxa é *menos sessenta litros "
        "por hora,* [p=0.2] com *menos* porque o tanque *diminui.* [p=0.4] {d}O b é *quinhentos.* [p=0.2] A lei: "
        "[p=0.2] *y igual a quinhentos menos sessenta x.*"),
    dict(id="08", block="irregular", text=
        "{t}E se as horas *pularem?* [p=0.4] {a}Hora um: [p=0.2] quatrocentos e quarenta. [p=0.2] Hora *três:* [p=0.2] "
        "trezentos e vinte. [p=0.4] {b}O y caiu *cento e vinte,* [p=0.2] mas o x andou *duas* horas. [p=0.4] {c}Menos "
        "cento e vinte sobre dois: [p=0.2] *menos sessenta.* [p=0.2] A mesma taxa."),

    # ================= BLOCO C: A ORDEM =================
    dict(id="09", block="ordem", text=
        "{t}E a ordem da subtração importa? [p=0.4] {a}*Delta y sobre delta x,* [p=0.2] nessa ordem [p=0.2] e com os "
        "*mesmos pontos.* [p=0.4] {b}Veja: [p=0.2] em cima, [p=0.2] trezentos e oitenta menos quinhentos. [p=0.2] "
        "Embaixo, [p=0.2] *zero* menos *dois.* [p=0.2] Dá *mais sessenta.* [p=0.4] {c}O tanque *encheria?* [p=0.2] "
        "Não. [p=0.2] Cada andar subtraiu numa ordem, [p=0.2] e o sinal virou."),
    dict(id="10", block="pontos", text=
        "{t}Como nunca errar isso? [p=0.4] {a}Atalho: [p=0.2] *escreva os dois pontos.* [p=0.4] {b}Subtraia *segundo "
        "menos primeiro,* [p=0.2] em cima *e* embaixo. [p=0.4] {c}E confira o *sinal:* [p=0.2] se a coisa diminui, "
        "[p=0.2] a taxa é *negativa.*"),

    # ================= BLOCO D: O COEFICIENTE LINEAR =================
    dict(id="11", block="linear", text=
        "{t}E o b? [p=0.4] {a}Ponha *x igual a zero:* [p=0.2] sobra *f de zero igual a b.* [p=0.4] {b}O b é o "
        "*coeficiente linear:* [p=0.2] o valor *no início.* [p=0.2] No gráfico, [p=0.2] assunto do episódio três, "
        "[p=0.2] é onde a reta corta o eixo vertical. [p=0.4] {c}Pense no b como a *foto no instante zero.*"),
    dict(id="12", block="filme", text=
        "{t}E se a tabela não começa no zero? [p=0.4] {a}Se ela começa aos dez minutos, [p=0.2] você precisa *voltar o "
        "filme* até o zero. [p=0.4] {b}Outra vela: [p=0.2] aos *cinco* minutos, [p=0.2] *catorze centímetros,* [p=0.2] "
        "perdendo *zero vírgula quatro* por minuto. [p=0.4] {c}Volte cinco minutos: [p=0.2] ela tinha *dois* "
        "centímetros a mais. [p=0.4] {d}*Dezesseis centímetros.* [p=0.2] Esse é o b."),
    dict(id="13", block="voltar", text=
        "{a}Atalho: [p=0.2] *b é o valor medido, [p=0.2] mais o que se perdeu até ali.* [p=0.4] {b}Taxa vezes o tempo "
        "que passou: [p=0.2] zero vírgula quatro vezes cinco, [p=0.2] dois. [p=0.4] {c}Se a coisa *crescesse,* "
        "[p=0.2] você *tiraria* o que ganhou."),

    # ================= BLOCO E: O ZERO =================
    dict(id="14", block="zero", text=
        "{t}E quando o y chega a zero? [p=0.4] {a}O x que faz a função dar *zero* [p=0.2] se chama *zero,* [p=0.2] ou "
        "*raiz* da função. [p=0.4] {b}A conta: [p=0.2] *a x mais b igual a zero.* [p=0.2] Passa o b, [p=0.2] divide por "
        "a: [p=0.2] *x igual a menos b sobre a.* [p=0.4] {c}Em *dois x menos seis,* [p=0.2] *x igual a três.*"),
    dict(id="15", block="seca", text=
        "{t}Quando o tanque *seca?* [p=0.4] {a}Quinhentos menos sessenta x [p=0.2] igual a zero. [p=0.4] {b}X igual a "
        "quinhentos sobre sessenta, [p=0.2] *oito vírgula três horas.* [p=0.4] {c}No relógio, [p=0.2] não é oito e "
        "meia: [p=0.2] é *oito horas e vinte minutos.*"),
    dict(id="16", block="horas", text=
        "{t}Por que vinte? [p=0.4] {a}Atalho: [p=0.2] o que vem depois da vírgula é *fração de hora.* [p=0.2] "
        "Multiplique por *sessenta.* [p=0.4] {b}Um terço de hora vezes sessenta: [p=0.2] *vinte minutos.* [p=0.2] A "
        "hora tem sessenta minutos, [p=0.2] não cem."),

    # ================= BLOCO F: O ZERO TEM NOME =================
    dict(id="17", block="nome", text=
        "{t}E na prova, como o zero aparece? [p=0.4] {a}Com *nome.* [p=0.2] A hora em que a vela *acaba,* [p=0.2] o "
        "tanque *seca,* [p=0.2] a dívida *zera.* [p=0.4] {b}A pergunta *quando acaba?* [p=0.2] pede o zero da função. "
        "[p=0.4] {c}Nossa vela de dezesseis centímetros: [p=0.2] dezesseis menos zero vírgula quatro t igual a zero. "
        "[p=0.2] *Quarenta minutos.* [p=0.4] {d}Usamos a lei *além* dos dados: [p=0.2] isso é *extrapolar,* [p=0.2] "
        "supor que o ritmo continua."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma tabela: [p=0.2] x zero, [p=0.2] y *trinta.* [p=0.2] X dois, [p=0.2] y vinte e "
        "seis. [p=0.2] X quatro, [p=0.2] vinte e dois. [p=0.2] X seis, [p=0.2] dezoito. [p=0.4] {b}Qual é a *taxa,* "
        "[p=0.2] qual é o *b* [p=0.2] e quando o y chega a *zero?* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O y cai *quatro,* [p=0.2] mas o x pula de *dois em dois.* [p=0.2] Menos quatro "
        "sobre dois: [p=0.2] taxa *menos dois.* [p=0.4] {b}O b: [p=0.2] aqui a foto do zero *está* na tabela. [p=0.2] "
        "*Trinta.* [p=0.4] {c}Trinta menos dois x igual a zero: [p=0.2] *x igual a quinze.* [p=0.4] {d}Quem usa menos "
        "quatro como taxa, [p=0.2] esquecendo o pulo do x, [p=0.2] acha *sete e meio.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] taxa é delta y sobre delta x, [p=0.2] com unidade e "
        "com sinal. [p=0.5] {b}Dois: [p=0.2] b é o valor no instante zero, [p=0.2] não o primeiro dado da tabela. "
        "[p=0.5] {c}Três: [p=0.2] *quando acaba?* [p=0.2] pede o zero: [p=0.2] a x mais b igual a zero."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os cinco erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] a fração *invertida,* [p=0.2] dois sobre "
        "menos cento e vinte. [p=0.4] {b}Parece certo, [p=0.2] porque as duas dividem as diferenças. [p=0.4] {c}Mas a "
        "taxa é *saída* sobre *entrada:* [p=0.2] menos sessenta."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] tomar o *primeiro dado* da tabela como b. [p=0.2] Catorze centímetros, aos cinco minutos. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque é o primeiro número que aparece. [p=0.4] {c}Mas o b é a foto do "
        "*zero:* [p=0.2] *dezesseis.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] confundir o *zero* com o *b.* [p=0.4] {b}Parece certo, [p=0.2] porque os dois têm "
        "*zero* na história. [p=0.4] {c}Mas o b é o y quando *x* é zero: [p=0.2] quinhentos litros. [p=0.2] O zero é "
        "o x que zera o *y:* [p=0.2] oito horas e vinte."),
    dict(id="24", block="erros", text=
        "{a}Quarto: [p=0.2] taxa com *mais* numa coisa que *diminui:* [p=0.2] quinhentos *mais* sessenta x. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque o enunciado diz *perde sessenta* [p=0.2] e a gente anota só o número. "
        "[p=0.4] {c}Mas em duas horas o tanque teria seiscentos e vinte litros. [p=0.2] Diminui: [p=0.2] *menos* "
        "sessenta x."),
    dict(id="25", block="erros", text=
        "{a}Quinto: [p=0.2] esquecer o *tempo que já passou.* [p=0.2] Catorze dividido por zero vírgula quatro, "
        "[p=0.2] trinta e cinco minutos. [p=0.4] {b}Parece certo, [p=0.2] porque a conta acha quanto *falta.* [p=0.4] "
        "{c}Mas, desde que a vela foi acesa, [p=0.2] são *quarenta.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="26", block="q3", text=
        "{t}Uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um "
        "reservatório tinha *dois mil litros* [p=0.2] quando começou um vazamento constante. [p=0.3] *Cinco horas* "
        "depois, [p=0.2] restavam *mil e seiscentos.* [p=0.3] Ele terá *quatrocentos litros* após: [p=0.3] {qa}A: "
        "[p=0.2] uma vírgula vinte e cinco hora. [p=0.2] {qb}B: [p=0.2] quatro horas. [p=0.2] {qc}C: [p=0.2] quinze. "
        "[p=0.2] {qd}D: [p=0.2] vinte. [p=0.2] {qe}E: [p=0.2] vinte e cinco horas. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="27", block="q3", text=
        "{t}Primeiro, os dois pontos. [p=0.3] {a}Zero, dois mil. [p=0.2] Cinco, mil e seiscentos. [p=0.4] {b}Taxa: "
        "[p=0.2] menos quatrocentos sobre cinco, [p=0.2] *menos oitenta litros por hora.* [p=0.4] {c}Dois mil menos "
        "oitenta t igual a quatrocentos: [p=0.2] oitenta t igual a mil e seiscentos, [p=0.2] *t igual a vinte.* "
        "[p=0.4] {d}Conferindo com o outro dado: [p=0.2] em cinco horas, [p=0.2] mil e seiscentos. [p=0.2] Bate. "
        "[p=0.3] {ok}*Letra D!*"),
    dict(id="28", block="q3", text=
        "{t}E as armadilhas? [p=0.3] {xe}A E é o tempo para *esvaziar,* [p=0.2] que não foi pedido. [p=0.4] {xc}A C "
        "conta a partir da *quinta hora.* [p=0.4] {xa}A A faz proporção entre quatrocentos e mil e seiscentos litros. "
        "[p=0.4] {xb}E a B divide mil e seiscentos por quatrocentos, [p=0.2] misturando litros com horas."),

    # ================= QUESTÃO 8 (NÓS FAZEMOS) =================
    dict(id="29", block="q8", text=
        "{t}Agora, *nós* fazemos. [p=0.3] {a}Um carro comprado por *sessenta mil reais* [p=0.2] passou a valer "
        "*quarenta e dois mil* três anos depois. [p=0.3] A *depreciação* é *linear:* [p=0.2] a mesma quantia por ano. "
        "[p=0.3] Sete anos após a compra, [p=0.2] ele valerá: [p=0.3] {qa}A: [p=0.2] seis mil reais. [p=0.2] "
        "{qb}B: [p=0.2] doze mil. [p=0.2] {qc}C: [p=0.2] dezoito mil. [p=0.2] {qd}D: [p=0.2] vinte e quatro mil. "
        "[p=0.2] {qe}E: [p=0.2] cerca de vinte e seis mil. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="30", block="q8", text=
        "{t}Os dois pontos: [p=0.2] zero, sessenta mil; [p=0.2] três, quarenta e dois mil. [p=0.4] {a}Taxa: [p=0.2] "
        "menos dezoito mil sobre três, [p=0.2] *menos seis mil reais por ano.* [p=0.4] {b}Em sete anos: [p=0.2] sessenta "
        "mil menos quarenta e dois mil, [p=0.2] *dezoito mil.* [p=0.4] {c}Conferindo: [p=0.2] em três anos, [p=0.2] "
        "quarenta e dois mil. [p=0.2] Bate. [p=0.3] {ok}*Letra C!*"),
    dict(id="31", block="q8", text=
        "{t}E as outras? [p=0.3] {xa}A A é a perda *por ano,* [p=0.2] não o valor. [p=0.4] {xb}A B desconta *cinco* "
        "anos depois dos quarenta e dois mil, [p=0.2] quando faltavam *quatro.* [p=0.4] {xd}A D desconta duas vezes a "
        "perda de três anos, [p=0.2] como se sete fossem seis. [p=0.4] {xe}E a E aplica a queda em *porcentagem:* "
        "[p=0.2] o modelo exponencial, [p=0.2] a próxima família de funções."),

    # ================= QUESTÃO 1 (VOCÊ FAZ) =================
    dict(id="32", block="q1", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma vela acesa diminui num ritmo constante. [p=0.3] Dez minutos depois de "
        "acesa, [p=0.2] media *dezessete centímetros;* [p=0.2] trinta minutos depois, [p=0.2] *treze.* [p=0.3] O tempo "
        "total, [p=0.2] contado desde que foi acesa, [p=0.2] até ela acabar é: [p=0.3] {qa}A: [p=0.2] quarenta e sete "
        "vírgula cinco minutos. [p=0.2] {qb}B: [p=0.2] sessenta e cinco. [p=0.2] {qc}C: [p=0.2] oitenta e cinco. "
        "[p=0.2] {qd}D: [p=0.2] noventa e cinco. [p=0.2] {qe}E: [p=0.2] cento e cinco. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="33", block="q1", text=
        "{t}Conferindo. [p=0.3] {a}Os pontos: [p=0.2] dez, dezessete; [p=0.2] trinta, treze. [p=0.2] Menos quatro "
        "sobre vinte: [p=0.2] *menos zero vírgula dois centímetro por minuto.* [p=0.4] {b}Volte o filme dez minutos: "
        "[p=0.2] mais dois centímetros. [p=0.2] *Dezenove.* [p=0.2] Esse é o b. [p=0.4] {c}Dezenove menos zero vírgula "
        "dois t igual a zero: [p=0.2] *t igual a noventa e cinco.* [p=0.4] {d}Conferindo: [p=0.2] aos trinta, "
        "[p=0.2] dezenove menos seis, [p=0.2] treze. [p=0.2] {ok}*Letra D!*"),
    dict(id="34", block="q1", text=
        "{t}E as armadilhas? [p=0.3] {xc}A C é a do gancho: [p=0.2] o que falta a partir dos dez minutos. [p=0.4] "
        "{xb}A B faz o mesmo a partir dos trinta. [p=0.4] {xe}A E soma a queda inteira, [p=0.2] quatro centímetros, "
        "[p=0.2] e começa em vinte e um. [p=0.4] {xa}E a A usa a altura certa com a taxa *errada:* [p=0.2] quatro "
        "centímetros em dez minutos, [p=0.2] em vez de vinte."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="35", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] taxa é delta y sobre delta x, [p=0.2] com "
        "unidade e com sinal. [p=0.5] {b}Dois: [p=0.2] b é o valor no instante zero, [p=0.2] não o primeiro dado da "
        "tabela. [p=0.5] {c}Três: [p=0.2] *quando acaba?* [p=0.2] pede o zero: [p=0.2] a x mais b igual a zero."),

    # ================= PONTE E CTA =================
    dict(id="36", block="ponte", text=
        "{a}Uma reta que corta o eixo vertical em *menos três* [p=0.2] e passa pelo ponto *dois, um:* [p=0.3] qual é a "
        "lei? [p=0.4] {b}E como saber, [p=0.2] só de olhar, [p=0.2] se ela *sobe* ou *desce?* [p=0.4] {c}Próximo "
        "episódio: [p=0.2] *o gráfico.*"),
    dict(id="37", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] o que na sua casa tem uma *hora em que acaba?* "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
