# Roteiro — Logaritmos: definição, propriedades e equações, Episódio 2 de 5: as três propriedades e o kit log 2 e log 3
# Base: Estudos/Enem/estudos/01-matematica/27-logaritmos-propriedades-equacoes.html — seções 04 e 06 + Questões 2, 9 e 7
#   (seção 12). Mudança de base fica para o episódio 3 (aqui, só "b sobre a é log de três na base dois", na Q9).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   As propriedades do log são as regras de potência LIDAS DE TRÁS PARA FRENTE (lá, multiplicar soma expoentes).
#   O KIT 2, 3 e 10: todo número feito de 2, 3 e 5 sai do kit, porque 5 = 10 ÷ 2.
#   Soma dentro do log é PORTA TRANCADA: não tem regra.
#   A RÉGUA DE CÁLCULO: o trecho de 1 a 2 emendado ao de 1 a 3 chega ao 6 (somar logs = multiplicar números).
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Testes das propriedades com potências de 10 (exemplos NOSSOS): log(10 · 100) = 3 = 1 + 2 · log(1000 ÷ 10) = 2 = 3 − 1 ·
#   log 10³ = 3 = 3 · 1 · log √2 = ½ · 0,301 ≈ 0,15.
# DESVIO DO PROMPT (exemplo NOSSO): o bloco d testa "log M ÷ log N ≠ log M − log N" com 1 000 e 10 (3 contra 2), e o erro 2
#   com 1 000 e 100 (1,5 contra 1), para não usar antes os números a = 100 e b = 10, que são o teste da afirmação III da
#   Questão 7 ("você faz", com pausa). O teste do log(10 + 10) é o do próprio prompt (gancho).
# Kit (seção 06, conferido): 4 → 0,602 · 5 → 0,699 · 6 → 0,778 · 9 → 0,954 · 12 → 1,079 · 1,5 → 0,176 · 0,9 → −0,046 ·
#   0,2 → −0,699. A decomposição aparece na tela antes de cada conta.
# Nós fazemos (prompt): log 18 = 0,30 + 2 · 0,48 = 1,26 (18 = 2 · 3²; entre 10 e 100 → log entre 1 e 2).
# QUESTÃO 2 (texto do material): 72 = 2³ · 3² → 0,90 + 0,96 = 1,86 → E. Erradas (material): A 0,78 = log 6;
#   B 0,864 = log 8 · log 9 (0,90 · 0,96); C 0,96 = log 9; D 1,38 = log 24 (esqueceu o expoente 2 do 3).
# QUESTÃO 9 (texto do material): log 1,5 = log 3 − log 2 = b − a → A. Erradas (material): B a − b = log(2/3), negativo;
#   C a + b = log 6; D b/a = log₂ 3; E 1 + b − a = log 15 (confundiu 1,5 com 15).
# QUESTÃO 7 (texto do material): verdadeiras II e IV → B. I falsa (a = b = 10: 1,30 contra 2); III falsa (a = 100, b = 10:
#   1 contra 2). Erradas (material): A e D aceitam a I; C aceita a III; E aceita a III e deixa de fora a II.
# Atalhos (verde): vezes vira mais, dividir vira menos, expoente vai para a frente + "teste com 10 e 100" ·
#   a conferência dos inteiros (entre 1 e 10 → log entre 0 e 1; entre 10 e 100 → entre 1 e 2; entre 0 e 1 → negativo).
# Contas conferidas em trabalho/conferir_contas.py.
# Frases-chave (meio e fim, idênticas): 1. Produto vira soma, quociente vira diferença, expoente desce multiplicando.
#   2. Soma dentro do log não tem regra. 3. Número entre 0 e 1 tem log negativo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "As 3 propriedades do logaritmo e o kit log 2 e log 3 | Logaritmos Ep. 2"
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
        "{a}Log de *dez mais dez* [p=0.2] é log de dez *mais* log de dez? [p=0.5] {b}Teste: [p=0.2] log de vinte [p=0.2] "
        "dá mais ou menos *um vírgula trinta.* [p=0.4] {c}Mas log de dez mais log de dez [p=0.2] dá *dois.* [p=0.5] "
        "{d}A regra que *parece óbvia* [p=0.2] está *errada,* [p=0.3] {e}e a alternativa com ela [p=0.2] *sempre "
        "aparece.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai usar as *três propriedades* [p=0.3] {b}e calcular o log de muitos "
        "números [p=0.2] só com *log de dois* e *log de três.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Potenciação: [p=0.2] multiplicou potências de mesma base, "
        "[p=0.2] *soma* os expoentes; [p=0.2] dividiu, [p=0.2] *subtrai;* [p=0.2] potência de potência, [p=0.2] "
        "*multiplica.* [p=0.4] {b}Da série de Divisibilidade: [p=0.2] setenta e dois [p=0.2] é *dois ao cubo vezes "
        "três ao quadrado.* [p=0.4] {c}E do episódio passado: [p=0.2] log é um *expoente.*"),

    # ================= CONCRETO: A RÉGUA DE CÁLCULO =================
    dict(id="04", block="regua", text=
        "{t}Antes das calculadoras, [p=0.2] como se multiplicava? [p=0.4] {a}Com a *régua de cálculo:* [p=0.2] uma "
        "régua que *multiplica somando comprimentos.* [p=0.4] {b}Pegue o trecho de *um até dois.* [p=0.3] {c}Emende o "
        "trecho de *um até três.* [p=0.4] {d}Onde termina? [p=0.3] Exatamente no *seis:* [p=0.2] dois vezes três."),
    dict(id="05", block="regua", text=
        "{t}Por quê? [p=0.3] {a}Nessa régua, [p=0.2] cada número fica a uma distância proporcional ao *seu log.* "
        "[p=0.4] {b}Somar comprimentos [p=0.2] é *somar logs,* [p=0.3] {c}e o resultado cai no *produto.* [p=0.4] "
        "{d}Essa é a primeira propriedade."),

    # ================= BLOCO A: PRODUTO VIRA SOMA =================
    dict(id="06", block="produto", text=
        "{t}Escrita como regra. [p=0.4] {a}Uma *propriedade operatória* [p=0.2] é uma regra que transforma uma conta "
        "em outra. [p=0.4] {b}Log de *M vezes N* [p=0.2] é *log de M mais log de N.* [p=0.2] O *produto,* [p=0.2] o "
        "resultado de uma multiplicação, [p=0.2] vira *soma.* [p=0.4] {c}Teste: [p=0.2] log de dez vezes cem [p=0.2] "
        "é log de mil, [p=0.2] *três.* [p=0.3] {d}E log de dez mais log de cem: [p=0.2] um mais dois, [p=0.2] *três.*"),
    dict(id="07", block="produto", text=
        "{t}De onde vem? [p=0.4] {a}Das potências: [p=0.2] *b elevado a x vezes b elevado a y* [p=0.2] é *b elevado a "
        "x mais y.* [p=0.4] {b}Multiplicar *soma os expoentes.* [p=0.3] {c}E log *é* expoente. [p=0.4] {d}As "
        "propriedades do log são as regras de potência [p=0.2] *lidas de trás para frente.*"),

    # ================= BLOCO B: QUOCIENTE VIRA DIFERENÇA =================
    dict(id="08", block="quociente", text=
        "{t}E a divisão? [p=0.4] {a}O *quociente* [p=0.2] é o resultado de uma divisão. [p=0.3] {b}Log de *M dividido "
        "por N* [p=0.2] é *log de M menos log de N.* [p=0.2] Quociente vira *diferença.* [p=0.4] {c}Teste: [p=0.2] "
        "log de mil dividido por dez [p=0.2] é log de cem, [p=0.2] *dois.* [p=0.3] {d}E três menos um: [p=0.2] "
        "*dois.* [p=0.2] Bateu."),

    # ================= BLOCO C: EXPOENTE DESCE MULTIPLICANDO =================
    dict(id="09", block="potencia", text=
        "{t}E se o número estiver elevado a alguma coisa? [p=0.4] {a}Uma *potência* [p=0.2] é um número multiplicado "
        "por ele mesmo, [p=0.2] como dez ao cubo. [p=0.4] {b}Log de *M elevado a k* [p=0.2] é *k vezes log de M:* "
        "[p=0.2] o expoente *desce multiplicando.* [p=0.4] {c}Teste: [p=0.2] log de dez ao cubo, [p=0.2] *três;* "
        "[p=0.2] três vezes log de dez, [p=0.2] *três.*"),
    dict(id="10", block="potencia", text=
        "{t}E raiz? [p=0.4] {a}Raiz quadrada de dois [p=0.2] é *dois elevado a um meio.* [p=0.4] {b}Então o log "
        "[p=0.2] é *um meio vezes log de dois:* [p=0.3] {c}mais ou menos *zero vírgula quinze.*"),

    # ================= ATALHO: AS TRÊS NUMA LINHA =================
    dict(id="11", block="atalho", text=
        "{t}Atalho. [p=0.3] {a}Dentro do log, [p=0.2] *vezes* vira *mais;* [p=0.2] *dividir* vira *menos;* [p=0.2] o "
        "*expoente* vai para a *frente.* [p=0.4] {b}Na dúvida sobre uma regra, [p=0.2] *teste com dez e cem:* [p=0.2] "
        "os logs são um e dois."),

    # ================= BLOCO D: O QUE AS PROPRIEDADES NÃO DIZEM =================
    dict(id="12", block="naodizem", text=
        "{t}E o que as propriedades *não* dizem? [p=0.4] {a}Log de *M mais N* [p=0.2] *não tem regra.* [p=0.3] "
        "{b}Soma dentro do log [p=0.2] é *porta trancada.* [p=0.4] {c}O teste do começo: [p=0.2] *um vírgula "
        "trinta* contra *dois.*"),
    dict(id="13", block="naodizem", text=
        "{t}E dividir um log pelo outro? [p=0.4] {a}Log de M *sobre* log de N [p=0.2] *não* é log de M menos log de "
        "N. [p=0.4] {b}Teste com mil e dez: [p=0.2] três sobre um, [p=0.2] *três.* [p=0.3] {c}Três menos um, [p=0.2] "
        "*dois.* [p=0.2] Não bate."),

    # ================= BLOCO E: O KIT =================
    dict(id="14", block="kit", text=
        "{t}Agora, o *kit.* [p=0.3] {a}Três caixinhas: [p=0.2] log de dois, [p=0.2] *zero vírgula trezentos e um;* "
        "[p=0.3] log de três, [p=0.2] *zero vírgula quatrocentos e setenta e sete;* [p=0.3] log de dez, [p=0.2] *um.* "
        "[p=0.4] {b}Para usar, [p=0.2] faça a *decomposição em fatores primos:* [p=0.2] escreva o número como produto "
        "de primos. [p=0.4] {c}Todo número feito de *dois, três e cinco* [p=0.2] sai do kit. [p=0.2] E o cinco? "
        "[p=0.2] *Dez dividido por dois.*"),
    dict(id="15", block="kit", text=
        "{t}Montando as peças. [p=0.3] {a}Quatro, *dois ao quadrado:* [p=0.2] duas vezes zero vírgula trezentos e um, "
        "[p=0.2] *zero vírgula seiscentos e dois.* [p=0.4] {b}Seis, *dois vezes três:* [p=0.2] soma, [p=0.2] *zero "
        "vírgula setecentos e setenta e oito.* [p=0.4] {c}Nove, *três ao quadrado:* [p=0.2] *zero vírgula novecentos "
        "e cinquenta e quatro.* [p=0.4] {d}Doze, *dois ao quadrado vezes três:* [p=0.2] *um vírgula zero setenta e "
        "nove.*"),
    dict(id="16", block="kit", text=
        "{t}E com divisão? [p=0.4] {a}Cinco, *dez dividido por dois:* [p=0.2] um menos zero vírgula trezentos e um, "
        "[p=0.2] *zero vírgula seiscentos e noventa e nove.* [p=0.4] {b}Um vírgula cinco, *três dividido por dois:* "
        "[p=0.2] *zero vírgula cento e setenta e seis.*"),

    # ================= BLOCO F: MENOR QUE 1, LOG NEGATIVO =================
    dict(id="17", block="negativo", text=
        "{t}E um número *menor que um?* [p=0.4] {a}Zero vírgula nove [p=0.2] é *nove dividido por dez:* [p=0.2] zero "
        "vírgula novecentos e cinquenta e quatro *menos um,* [p=0.2] *menos* zero vírgula zero quarenta e seis. "
        "[p=0.4] {b}Zero vírgula dois, [p=0.2] *dois dividido por dez:* [p=0.2] *menos* zero vírgula seiscentos e "
        "noventa e nove. [p=0.4] {c}Para o dez dar menos que um, [p=0.2] o expoente tem que ser *negativo.* [p=0.4] "
        "{d}Log de zero vírgula nove positivo [p=0.2] é *erro de sinal:* [p=0.2] decisivo no próximo episódio."),

    # ================= ATALHO: CONFERÊNCIA DOS INTEIROS =================
    dict(id="18", block="atalho2", text=
        "{t}Atalho para conferir. [p=0.3] {a}Número entre *um e dez:* [p=0.2] log entre *zero e um.* [p=0.3] {b}Entre "
        "*dez e cem:* [p=0.2] entre *um e dois.* [p=0.3] {c}Entre *zero e um:* [p=0.2] *negativo.* [p=0.4] {d}Doze "
        "está entre dez e cem: [p=0.2] um vírgula zero setenta e nove. [p=0.2] *Bateu.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Com *log de dois igual a zero vírgula trinta* [p=0.2] e *log de três igual a zero "
        "vírgula quarenta e oito,* [p=0.2] calcule *log de dezoito.* [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Decomposição: [p=0.2] dezoito é *dois vezes três ao quadrado.* [p=0.4] "
        "{b}Produto vira soma, [p=0.2] expoente desce: [p=0.2] zero vírgula trinta [p=0.2] mais *duas vezes* zero "
        "vírgula quarenta e oito. [p=0.4] {c}Zero vírgula trinta mais zero vírgula noventa e seis: [p=0.2] *um "
        "vírgula vinte e seis.* [p=0.4] {d}Confere: [p=0.2] entre dez e cem, [p=0.2] log entre *um e dois.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] produto vira soma, [p=0.2] quociente vira diferença, "
        "[p=0.2] expoente desce multiplicando. [p=0.5] {b}Dois: [p=0.2] soma dentro do log não tem regra. [p=0.5] "
        "{c}Três: [p=0.2] número entre zero e um tem log negativo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] log de M mais N [p=0.2] igual a log de M mais log "
        "de N. [p=0.3] {b}Parece certo, [p=0.2] porque lembra a regra do produto. [p=0.3] {c}Mas a soma de fora "
        "[p=0.2] só aparece quando *dentro* tem *vezes.*"),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] log de M *dividido* por log de N [p=0.2] igual a log de M menos log de N. [p=0.3] "
        "{b}Parece certo, [p=0.2] porque tem divisão e diferença. [p=0.3] {c}Mas a diferença é o log do *quociente.* "
        "[p=0.2] Com mil e cem: [p=0.2] três sobre dois [p=0.2] é *um e meio,* [p=0.2] e não um."),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] log de setenta e dois [p=0.2] igual a log de oito *vezes* log de nove. [p=0.3] "
        "{b}Parece certo, [p=0.2] porque setenta e dois *é* oito vezes nove. [p=0.3] {c}Mas o vezes de dentro [p=0.2] "
        "vira *mais* do lado de fora."),
    dict(id="25", block="erros", text=
        "{a}Quarto: [p=0.2] log de zero vírgula nove *positivo.* [p=0.3] {b}Parece certo, [p=0.2] porque log de nove é "
        "positivo. [p=0.3] {c}Mas zero vírgula nove é nove sobre dez: [p=0.2] *menos um.* [p=0.2] Dá *menos* zero "
        "vírgula zero quarenta e seis."),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="26", block="q2", text=
        "{t}Agora, questões do nosso material. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um técnico precisa de *log de setenta e dois,* [p=0.2] mas só tem *log de dois igual a "
        "zero vírgula trinta* [p=0.2] e *log de três igual a zero vírgula quarenta e oito.* [p=0.4] {qa}A: [p=0.2] zero "
        "vírgula setenta e oito. [p=0.3] {qb}B: [p=0.2] zero vírgula oitocentos e sessenta e quatro. [p=0.3] {qc}C: "
        "[p=0.2] zero vírgula noventa e seis. [p=0.3] {qd}D: [p=0.2] um vírgula trinta e oito. [p=0.3] {qe}E: [p=0.2] "
        "um vírgula oitenta e seis."),
    dict(id="27", block="q2", text=
        "{t}Primeiro, a decomposição. [p=0.3] {a}Setenta e dois [p=0.2] é *oito vezes nove:* [p=0.2] *dois ao cubo "
        "vezes três ao quadrado.* [p=0.4] {b}Os expoentes descem: [p=0.2] *três vezes* zero vírgula trinta, [p=0.2] "
        "zero vírgula noventa, [p=0.3] {c}mais *duas vezes* zero vírgula quarenta e oito, [p=0.2] zero vírgula "
        "noventa e seis. [p=0.4] {d}Total: [p=0.2] *um vírgula oitenta e seis,* [p=0.2] entre um e dois. [p=0.3] "
        "{ok}*Letra E!*"),
    dict(id="28", block="q2", text=
        "{t}E as outras? [p=0.3] {xa}A A [p=0.2] é *log de seis.* [p=0.4] {xb}A B [p=0.2] *multiplica* log de oito "
        "por log de nove. [p=0.4] {xc}A C [p=0.2] é só *log de nove.* [p=0.4] {xd}E a D [p=0.2] é *log de vinte e "
        "quatro:* [p=0.2] esqueceu o expoente do três."),

    # ================= QUESTÃO 9 (NÓS FAZEMOS) =================
    dict(id="29", block="q9", text=
        "{t}Esta a gente faz junto. [p=0.3] {a}Numa tabela antiga, [p=0.2] *log de dois* é *a* [p=0.2] e *log de "
        "três* é *b.* [p=0.2] Quanto vale *log de um vírgula cinco?* [p=0.4] {qa}A: [p=0.2] b menos a. "
        "[p=0.3] {qb}B: [p=0.2] a menos b. [p=0.3] {qc}C: [p=0.2] a mais b. [p=0.3] {qd}D: [p=0.2] b sobre a. [p=0.3] "
        "{qe}E: [p=0.2] um mais b menos a. [p=0.4] {p}Pense comigo: [p=0.2] um vírgula cinco é feito de quê? [p=1.5]"),
    dict(id="30", block="q9", text=
        "{t}Um vírgula cinco [p=0.2] é *três dividido por dois.* [p=0.4] {a}Quociente vira diferença: [p=0.2] log de "
        "três *menos* log de dois. [p=0.3] {b}Em letras: [p=0.2] *b menos a.* [p=0.4] {c}Confere com o kit: [p=0.2] "
        "*zero vírgula cento e setenta e seis.* [p=0.2] Positivo e pequeno, [p=0.2] como deve ser. [p=0.3] "
        "{ok}*Letra A!*"),
    dict(id="31", block="q9", text=
        "{t}E as erradas? [p=0.3] {xb}A B [p=0.2] é log de *dois terços:* [p=0.2] *negativo.* [p=0.4] {xc}A C [p=0.2] "
        "é *log de seis.* [p=0.4] {xd}A D [p=0.2] divide os logs: [p=0.2] isso é *log de três na base dois.* [p=0.4] "
        "{xe}E a E [p=0.2] é *log de quinze:* [p=0.2] confundiu um vírgula cinco com quinze."),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="32", block="q7", text=
        "{t}E esta é *sua.* [p=0.3] {a}Um estudante escreveu quatro igualdades, [p=0.2] com *a* e *b* positivos. "
        "[p=0.4] {b}Um: [p=0.2] log de *a mais b* [p=0.2] igual a log de a mais log de b. [p=0.3] Dois: [p=0.2] log de "
        "*a ao cubo* [p=0.2] igual a três log de a. [p=0.3] Três: [p=0.2] log de *a sobre b* [p=0.2] igual a log de a "
        "*sobre* log de b. [p=0.3] Quatro: [p=0.2] log de *um* igual a zero. [p=0.4] {c}São verdadeiras para todos os "
        "valores [p=0.2] apenas: [p=0.3] {qa}A: [p=0.2] um e dois. [p=0.3] {qb}B: [p=0.2] dois e quatro. [p=0.3] "
        "{qc}C: [p=0.2] dois e três. [p=0.3] {qd}D: [p=0.2] um, dois e quatro. [p=0.3] {qe}E: [p=0.2] três e quatro. "
        "[p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="33", block="q7", text=
        "{t}Conferindo. [p=0.3] {a}A dois é a regra da potência: [p=0.2] *verdadeira.* [p=0.3] {b}A quatro vem de "
        "*dez elevado a zero* igual a um: [p=0.2] *verdadeira.* [p=0.4] {c}A um: [p=0.2] com a e b iguais a dez, "
        "[p=0.2] um vírgula trinta contra dois: [p=0.2] *falsa.* [p=0.4] {d}A três: [p=0.2] com a igual a cem e b "
        "igual a dez, [p=0.2] um contra dois: [p=0.2] *falsa.* [p=0.3] {ok}*Letra B!*"),
    dict(id="34", block="q7", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] {xd}e a D [p=0.2] aceitam a *um,* [p=0.2] que é falsa. [p=0.4] "
        "{xc}A C [p=0.2] aceita a *três.* [p=0.4] {xe}E a E [p=0.2] aceita a três [p=0.2] e deixa de fora a *dois,* "
        "[p=0.2] que é verdadeira."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="35", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] produto vira soma, [p=0.2] quociente vira "
        "diferença, [p=0.2] expoente desce multiplicando. [p=0.5] {b}Dois: [p=0.2] soma dentro do log não tem regra. "
        "[p=0.5] {c}Três: [p=0.2] número entre zero e um tem log negativo."),

    # ================= PONTE E CTA =================
    dict(id="36", block="ponte", text=
        "{a}*Um vírgula zero oito elevado a t* [p=0.2] igual a *dois:* [p=0.4] {b}o t está *preso no expoente,* "
        "[p=0.3] e dois não é potência de um vírgula zero oito. [p=0.5] {c}Como derrubar esse t? [p=0.5] {d}Próximo "
        "episódio."),
    dict(id="37", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído no log de dez mais dez? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
