# Roteiro — Juros Compostos, Episódio 3 de 5: potências sem calculadora e descobrir o tempo
# Base: Estudos/Enem/estudos/01-matematica/14-juros-compostos-montante.html — seções 05 e 06 + Questões 6, 7 e 2 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   Multiplicar por 1,1 é SOMAR A DÉCIMA PARTE: 1,331 + 0,1331 = 1,4641.
#   DOBRAR O TEMPO é ELEVAR O FATOR AO QUADRADO, não dobrar o fator.
#   A regra do 72 é o RADAR: em segundos, diz se a resposta está perto de 7 anos ou de 25.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Logaritmos: só como valores DADOS + "por que o log derruba o expoente fica para a série de Logaritmos".
# Exemplos:
#   Blocos a–g: os do material (1,1² … 1,1⁵; 1,03¹⁰ ≈ 1,34 → 1,34² ≈ 1,80; 1,1⁷ ≈ 1,61 · 1,21 ≈ 1,95; 1,34² ≈ 1,80;
#   régua 1,1¹ … 1,1⁵ até passar de 1,6; 0,301 ÷ 0,041 ≈ 7,3; regra do 72: 10% → 7,2 · 6% → 12 · 8% → 9).
#   A régua do bloco e é a mesma da Q7 (pedido do prompt); a Q7 é "nós fazemos", em reais, e o novo nela são as erradas.
#   Bloco h (NOSSO): triplicar a 10% com log 3 ≈ 0,477 → 0,477 ÷ 0,041 ≈ 11,6 anos; quadruplicar = 7,3 + 7,3 ≈ 14,6.
#   Nós fazemos (prompt): 1,22² = 1,4884 ≈ 1,49 (NOSSO: "não é 2,44") · 72 ÷ 9 = 8 anos.
#   Erro 3 (NOSSO): 0,301 ÷ 0,1 ≈ 3 anos, desmentido pelo radar (≈ 7).
# QUESTÃO 6 (eu faço): 1,34² = 1,7956 → 2.000 · 1,7956 ≈ 3.591 → D. Erradas (material): A só 6 meses (2.680); B simples,
#   60% (3.200); C soma os semestres, 68% (3.360); E fator × 2 (5.360). Conferência pelo radar (NOSSA): 72 ÷ 5 ≈ 14 meses
#   para dobrar → em 12 meses, quase o dobro.
# QUESTÃO 7 (nós fazemos): 1,1⁴ ≈ 1,46 (R$ 1.460) não basta; 1,1⁵ ≈ 1,61 (R$ 1.610) basta → B. Erradas (material):
#   C simples (1.000 + 100 · 6); A para em 1,46; D um mês a mais; E 1.600 ÷ 100.
# QUESTÃO 2 (você faz): 0,48 ÷ 0,08 = 6 anos → B; 1,2⁶ ≈ 2,99. Erradas (material): A dobrar (0,30 ÷ 0,08 = 3,75);
#   C dobro do tempo de dobrar (quadruplicar, 7,5); D triplicar em simples (0,2t = 2 → 10); E J = 3C (0,2t = 3 → 15).
#   Radar (NOSSO): 72 ÷ 20 = 3,6 para dobrar, ≈ 7,2 para quadruplicar → triplicar fica no meio.
# Atalhos (verde): "×1,1 = some a décima parte" · "as 3 técnicas: ache as potências dadas, escreva o prazo como soma,
#   reais só no fim" · "o tempo pelo log em 3 passos" · "regra do 72 (radar)".
# Frases-chave (meio e fim, idênticas): 1. Dobrar o tempo é elevar o fator ao quadrado. 2. O tempo está no expoente:
#   tentativa, logaritmo ou regra do 72. 3. Divida pelo log do fator, nunca pela taxa.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Juros compostos sem calculadora: potências, tempo e a regra do 72 · Matemática ENEM, Juros compostos episódio 3"

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
        "{a}O enunciado diz: [p=0.2] *um vírgula zero cinco elevado a seis* [p=0.2] é aproximadamente *um vírgula "
        "trinta e quatro.* [p=0.4] {b}A pergunta é sobre *doze meses.* [p=0.4] {c}Quem faz *duas vezes* um vírgula "
        "trinta e quatro [p=0.2] *erra.* [p=0.3] {d}Quem faz um vírgula trinta e quatro *ao quadrado* [p=0.2] *acerta.* "
        "[p=0.4] {e}Essa é a diferença entre pensar em *juros simples* [p=0.2] e pensar em *juros compostos.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai usar as *potências que o enunciado der,* [p=0.3] {b}descobrir o *tempo* por "
        "*tentativa* ou por *logaritmo* [p=0.3] {c}e estimar com a *regra do setenta e dois.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] *M igual a C vezes um mais i, elevado a t.* "
        "[p=0.2] O *um mais i* é o *fator* de cada período. [p=0.4] {b}*Potência* é multiplicação repetida; [p=0.2] o "
        "*expoente,* o numerinho de cima, [p=0.2] conta as vezes. [p=0.4] {c}E da Potenciação: [p=0.2] somar "
        "expoentes é *multiplicar potências;* [p=0.2] e elevar ao quadrado [p=0.2] *dobra o expoente.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Duas perguntas da vida real. [p=0.3] {a}Uma dívida de *dois mil reais* no cartão, [p=0.2] a *cinco por "
        "cento ao mês.* [p=0.2] Quanto vira em *um ano,* [p=0.2] se ninguém pagar? [p=0.4] {b}E em quanto tempo o meu "
        "dinheiro *dobra?* [p=0.4] {c}Nas duas: [p=0.2] uma *potência grande* [p=0.2] e *nenhuma calculadora.*"),

    # ================= BLOCO A: PASSO A PASSO =================
    dict(id="05", block="passo", text=
        "{t}Técnica um: [p=0.2] multiplicar *passo a passo.* [p=0.4] {a}A dez por cento, [p=0.2] o fator é *um "
        "vírgula um.* [p=0.4] {b}Ao quadrado: [p=0.2] *um vírgula vinte e um.* [p=0.2] Ao cubo: [p=0.2] *um vírgula "
        "três, três, um.* [p=0.4] {c}À quarta: [p=0.2] *um vírgula quatro, seis, quatro, um.* [p=0.2] À quinta: "
        "[p=0.2] cerca de *um vírgula sessenta e um.* [p=0.4] {d}Serve para expoentes *pequenos.*"),
    dict(id="06", block="passo", text=
        "{t}E de cabeça? [p=0.4] {a}Multiplicar por um vírgula um [p=0.2] é *somar a décima parte.* [p=0.4] {b}Um "
        "vírgula três, três, um, [p=0.2] mais zero vírgula um, três, três, um: [p=0.2] *um vírgula quatro, seis, "
        "quatro, um.* [p=0.4] {c}Ande com a vírgula *uma casa* [p=0.2] e some."),

    # ================= BLOCO B: QUEBRAR O EXPOENTE =================
    dict(id="07", block="quebrar", text=
        "{t}E se o expoente for *grande?* [p=0.4] {a}Técnica dois: [p=0.2] *quebrar o expoente,* [p=0.2] escrever o "
        "prazo como *soma de prazos iguais.* [p=0.4] {b}Vinte meses são *dez mais dez:* [p=0.2] o fator de vinte "
        "meses [p=0.2] é o de dez meses *ao quadrado.* [p=0.4] {c}Com *um vírgula zero três elevado a dez* [p=0.2] "
        "cerca de *um vírgula trinta e quatro,* [p=0.4] {d}vinte meses dão *um vírgula trinta e quatro ao quadrado:* "
        "[p=0.2] cerca de *um vírgula oitenta.*"),

    # ================= BLOCO C: COMBINAR POTÊNCIAS =================
    dict(id="08", block="combinar", text=
        "{t}E se o prazo não for o dobro de nada? [p=0.4] {a}Técnica três: [p=0.2] *combinar potências,* [p=0.2] "
        "multiplicar fatores de prazos que *somam* o pedido. [p=0.4] {b}Sete anos a dez por cento: [p=0.2] sete é "
        "*cinco mais dois.* [p=0.4] {c}*Um vírgula sessenta e um* [p=0.2] vezes *um vírgula vinte e um:* [p=0.4] "
        "{d}cerca de *um vírgula noventa e cinco.*"),
    dict(id="09", block="combinar", text=
        "{t}O atalho das três técnicas. [p=0.3] {a}Ache as *potências dadas.* [p=0.4] {b}Escreva o prazo como *soma* "
        "dos expoentes dados. [p=0.4] {c}Multiplique os fatores, [p=0.2] e *reais* só na *última linha.*"),

    # ================= BLOCO D: DOBRAR O TEMPO =================
    dict(id="10", block="dobrar", text=
        "{t}Agora, a pegadinha do gancho. [p=0.4] {a}Seis meses dão fator *um vírgula trinta e quatro.* [p=0.2] E "
        "doze? [p=0.4] {b}O segundo semestre começa com o saldo *já aumentado:* [p=0.2] o fator *multiplica ele "
        "mesmo.* [p=0.2] *Um vírgula trinta e quatro ao quadrado,* [p=0.2] cerca de *um vírgula oitenta.* [p=0.4] "
        "{c}Não é *dois vírgula sessenta e oito,* [p=0.2] {d}nem um vírgula sessenta e oito. [p=0.4] {e}Dobrar o "
        "tempo é *elevar o fator ao quadrado,* [p=0.2] *não dobrar o fator.*"),

    # ================= BLOCO E: TENTATIVA =================
    dict(id="11", block="tentativa", text=
        "{t}E quando a pergunta é o *tempo?* [p=0.4] {a}Ele está *no expoente,* [p=0.2] lá em cima. [p=0.4] {b}A "
        "primeira saída é a *tentativa:* [p=0.2] testar os expoentes até passar da meta. [p=0.4] {c}A dez por cento "
        "ao mês, [p=0.2] quando o saldo passa de *um vírgula seis vezes* o capital? [p=0.4] {d}Um vírgula um, [p=0.2] "
        "um vírgula vinte e um, [p=0.2] um vírgula trinta e três, [p=0.2] um vírgula quarenta e seis: [p=0.2] ainda "
        "não. [p=0.4] {e}Um vírgula sessenta e um: [p=0.2] passou! [p=0.2] *Cinco meses.*"),

    # ================= BLOCO F: LOGARITMO DADO =================
    dict(id="12", block="log", text=
        "{t}E se o prazo for longo demais para testar? [p=0.4] {a}Aí entra o *logaritmo.* [p=0.2] Hoje, [p=0.2] ele é "
        "só um *número que o enunciado entrega.* [p=0.4] {b}A fórmula: [p=0.2] *t igual a log de M sobre C,* [p=0.2] "
        "dividido por *log de um mais i.* [p=0.4] {c}Dobrar a dez por cento ao ano: [p=0.2] log de dois, *zero "
        "vírgula três, zero, um,* [p=0.2] sobre log de um vírgula um, *zero vírgula zero, quatro, um.* [p=0.4] "
        "{d}Cerca de *sete vírgula três anos.* [p=0.4] {e}Por que o log *derruba* o expoente [p=0.2] fica para a "
        "série de *Logaritmos.* [p=0.2] Na prova, [p=0.2] os logs *sempre vêm dados.*"),
    dict(id="13", block="log", text=
        "{t}O atalho do logaritmo. [p=0.3] {a}Um: [p=0.2] *M sobre C:* [p=0.2] dobrar é dois, [p=0.2] triplicar é "
        "três. [p=0.4] {b}Dois: [p=0.2] o *log desse número.* [p=0.4] {c}Três: [p=0.2] divida pelo *log do fator,* "
        "[p=0.2] *nunca pela taxa.*"),

    # ================= BLOCO G: REGRA DO 72 =================
    dict(id="14", block="regra72", text=
        "{t}E dá para *estimar* em segundos? [p=0.4] {a}Estimar é achar um valor *aproximado,* [p=0.2] bom para "
        "eliminar alternativas. [p=0.4] {b}A *regra do setenta e dois:* [p=0.2] o tempo para *dobrar* [p=0.2] é cerca "
        "de *setenta e dois dividido pela taxa* em por cento. [p=0.4] {c}A dez por cento, [p=0.2] *sete vírgula "
        "dois.* [p=0.2] A seis, [p=0.2] *doze.* [p=0.2] A oito, [p=0.2] *nove.* [p=0.4] {d}É o seu *radar:* [p=0.2] "
        "diz se a resposta está perto de *sete anos* [p=0.2] ou de *vinte e cinco.* [p=0.4] {e}Vale bem entre *dois e "
        "vinte por cento.*"),

    # ================= BLOCO H: TRIPLICAR =================
    dict(id="15", block="triplicar", text=
        "{t}E para *triplicar?* [p=0.4] {a}O tempo de dobrar *não serve:* [p=0.2] troque o log de dois [p=0.2] pelo "
        "*log de três.* [p=0.4] {b}A dez por cento: [p=0.2] zero vírgula quatro, sete, sete [p=0.2] sobre zero "
        "vírgula zero, quatro, um: [p=0.2] cerca de *onze vírgula seis anos.* [p=0.4] {c}E *dobrar duas vezes* "
        "[p=0.2] é *quadruplicar:* [p=0.2] cerca de *catorze vírgula seis.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Considere *um vírgula zero dois elevado a dez,* [p=0.2] aproximadamente *um vírgula "
        "vinte e dois.* [p=0.2] Qual é o *fator de vinte meses* [p=0.2] a dois por cento ao mês? [p=0.4] {b}E, pela "
        "regra do setenta e dois, [p=0.2] em quanto tempo um capital *dobra* a *nove por cento ao ano?* [p=0.3] *Pause "
        "e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Vinte meses são *dez mais dez:* [p=0.2] *um vírgula vinte e dois ao quadrado.* "
        "[p=0.4] {b}Dá *um vírgula quatro, oito, oito, quatro,* [p=0.2] cerca de *um vírgula quarenta e nove.* "
        "[p=0.2] Não dois vírgula quarenta e quatro! [p=0.4] {c}E o radar: [p=0.2] setenta e dois sobre nove, [p=0.2] "
        "*oito anos.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] dobrar o tempo é elevar o fator ao quadrado. [p=0.5] "
        "{b}Dois: [p=0.2] o tempo está no expoente: [p=0.2] tentativa, logaritmo ou regra do setenta e dois. [p=0.5] "
        "{c}Três: [p=0.2] divida pelo log do fator, [p=0.2] nunca pela taxa."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] o tempo dobrou, [p=0.2] e você *dobra o "
        "fator:* [p=0.2] *dois vírgula sessenta e oito.* [p=0.4] {b}Parece certo, [p=0.2] porque em juros simples "
        "[p=0.2] o dobro do tempo dava o dobro dos juros. [p=0.4] {c}Mas em compostos, [p=0.2] o fator vai *ao "
        "quadrado.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] *somar as taxas:* [p=0.2] trinta e quatro mais trinta e quatro, [p=0.2] *sessenta e oito "
        "por cento.* [p=0.4] {b}Parece certo, [p=0.2] porque cada semestre rende mesmo trinta e quatro. [p=0.4] "
        "{c}Mas o segundo rende sobre um saldo *maior.* [p=0.2] Somar taxas é pensar em *simples.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] dividir o log de dois *pela taxa:* [p=0.2] zero vírgula três sobre zero vírgula um, "
        "[p=0.2] *três anos.* [p=0.4] {b}Parece certo, [p=0.2] porque a taxa é o número que mais aparece. [p=0.4] "
        "{c}Mas o denominador é o *log de um mais i.* [p=0.2] E o radar avisava: [p=0.2] *perto de sete,* não de "
        "três."),
    dict(id="22", block="erros", text=
        "{a}Quarto: [p=0.2] usar o tempo de *dobrar* para *triplicar:* [p=0.2] uma vez e meia, [p=0.2] ou o dobro "
        "dele. [p=0.4] {b}Parece certo, [p=0.2] porque três está entre dois e quatro. [p=0.4] {c}Mas triplicar usa o "
        "*log de três.* [p=0.2] E o dobro do tempo de dobrar [p=0.2] é *quadruplicar.*"),

    # ================= QUESTÃO 6 (EU FAÇO) =================
    dict(id="23", block="q6", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Eu resolvo com você. "
        "[p=0.4] {a}Uma dívida de *dois mil reais* no cartão de crédito [p=0.2] cresce a juros compostos de *cinco por "
        "cento ao mês.* [p=0.2] Considere *um vírgula zero cinco elevado a seis,* [p=0.2] aproximadamente *um vírgula "
        "trinta e quatro.* [p=0.2] Se nada for pago, [p=0.2] após *doze meses* a dívida será de, aproximadamente: "
        "[p=0.4] {qa}A: [p=0.2] dois mil, seiscentos e oitenta reais. [p=0.3] {qb}B: [p=0.2] três mil e duzentos reais. "
        "[p=0.3] {qc}C: [p=0.2] três mil, trezentos e sessenta reais. [p=0.3] {qd}D: [p=0.2] três mil, quinhentos e "
        "noventa reais. [p=0.3] {qe}E: [p=0.2] cinco mil, trezentos e sessenta reais."),
    dict(id="24", block="q6", text=
        "{t}O enunciado deu o fator de *seis* meses [p=0.2] e pediu *doze.* [p=0.4] {a}Doze são *seis mais seis:* "
        "[p=0.2] *um vírgula trinta e quatro ao quadrado,* [p=0.2] *um vírgula sete, nove, cinco, seis.* [p=0.4] "
        "{b}Só agora, os reais: [p=0.2] dois mil vezes isso, [p=0.2] cerca de *três mil, quinhentos e noventa e um.* "
        "[p=0.4] {c}Plausível? [p=0.2] O radar diz que a cinco por cento a dívida dobra em uns *catorze meses.* "
        "[p=0.2] Em doze, [p=0.2] *quase o dobro.* [p=0.3] {ok}*Letra D!*"),
    dict(id="25", block="q6", text=
        "{t}E as erradas? [p=0.4] {xa}A A usa só o fator de *seis meses.* [p=0.3] {xb}A B é juros *simples,* [p=0.2] "
        "sessenta por cento. [p=0.3] {xc}A C *soma as taxas* dos semestres. [p=0.3] {xe}E a E *multiplica o fator por "
        "dois.*"),

    # ================= QUESTÃO 7 (NÓS FAZEMOS) =================
    dict(id="26", block="q7", text=
        "{t}Agora, *nós fazemos* juntos. [p=0.4] {a}*Mil reais* a juros compostos de *dez por cento ao mês.* [p=0.2] "
        "Considere um vírgula um à quarta, [p=0.2] cerca de *um vírgula quarenta e seis,* [p=0.2] e à quinta, [p=0.2] "
        "cerca de *um vírgula sessenta e um.* [p=0.2] O número *mínimo* de meses completos [p=0.2] para o saldo "
        "atingir *pelo menos mil e seiscentos reais* é: [p=0.4] {qa}A: [p=0.2] quatro. [p=0.2] {qb}B: [p=0.2] cinco. "
        "[p=0.2] {qc}C: [p=0.2] seis. [p=0.2] {qd}D: [p=0.2] sete. [p=0.2] {qe}E: [p=0.2] dezesseis."),
    dict(id="27", block="q7", text=
        "{t}A meta é *um vírgula seis vezes* o capital. [p=0.4] {a}Quatro meses, [p=0.2] *mil, quatrocentos e "
        "sessenta:* [p=0.2] não basta. [p=0.2] {b}Cinco, [p=0.2] *mil, seiscentos e dez:* [p=0.2] passou. [p=0.3] "
        "{ok}*Letra B!* [p=0.4] {xc}A C é juros *simples:* [p=0.2] mil mais cem vezes seis. [p=0.3] {xa}A A para "
        "*abaixo da meta.* [p=0.3] {xd}A D conta *um mês a mais.* [p=0.3] {xe}E a E divide mil e seiscentos por cem, "
        "[p=0.2] misturando *montante* com *juros do mês.*"),

    # ================= QUESTÃO 2 (VOCÊ FAZ) =================
    dict(id="28", block="q2", text=
        "{t}E agora, [p=0.2] é *você* quem faz. [p=0.3] {a}Um fundo rende juros compostos de *vinte por cento ao ano.* "
        "[p=0.2] Para estimar em quanto tempo um capital aplicado nesse fundo *triplica,* [p=0.2] um analista usou: "
        "[p=0.2] *log de dois, zero vírgula trinta;* [p=0.2] *log de três, zero vírgula quarenta e oito;* [p=0.2] e *log "
        "de um vírgula dois, zero vírgula zero oito.* [p=0.2] O tempo obtido foi de: [p=0.3] {qa}A: [p=0.2] três vírgula "
        "setenta e cinco anos. [p=0.2] {qb}B: [p=0.2] seis anos. [p=0.2] {qc}C: [p=0.2] sete vírgula cinco anos. [p=0.2] "
        "{qd}D: [p=0.2] dez anos. [p=0.2] {qe}E: [p=0.2] quinze anos. [p=0.4] {b}*Pause o vídeo* [p=0.2] e tente. "
        "[p=2.0]"),
    dict(id="29", block="q2", text=
        "{t}Conferindo. [p=0.3] {a}Triplicar: [p=0.2] *log de três,* [p=0.2] zero vírgula quarenta e oito. [p=0.4] "
        "{b}Dividido pelo log do *fator,* [p=0.2] zero vírgula zero oito: [p=0.2] *seis anos.* [p=0.4] "
        "{c}Conferência: [p=0.2] um vírgula dois à sexta [p=0.2] dá *dois vírgula noventa e nove.* [p=0.4] {d}E o "
        "radar: [p=0.2] dobra em uns *três vírgula seis* anos, [p=0.2] quadruplica em uns *sete.* [p=0.2] Triplicar "
        "fica *no meio.* [p=0.3] {ok}*Letra B!*"),
    dict(id="30", block="q2", text=
        "{t}E as erradas? [p=0.4] {xa}A A é o tempo para *dobrar:* [p=0.2] o log de dois estava lá *de isca.* [p=0.4] "
        "{xc}A C é o dobro do tempo de dobrar: [p=0.2] *quadruplicar.* [p=0.4] {xd}A D é triplicar em juros "
        "*simples:* [p=0.2] vinte por cento ao ano, [p=0.2] dez anos. [p=0.4] {xe}E a E faz *juros igual a três vezes "
        "o capital,* [p=0.2] também em simples."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] dobrar o tempo é elevar o fator ao quadrado. "
        "[p=0.5] {b}Dois: [p=0.2] o tempo está no expoente: [p=0.2] tentativa, logaritmo ou regra do setenta e dois. "
        "[p=0.5] {c}Três: [p=0.2] divida pelo log do fator, [p=0.2] nunca pela taxa."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}E o caminho de volta? [p=0.3] Você quer ter *doze mil e cem reais* [p=0.2] daqui a *dois anos.* [p=0.4] "
        "{b}Quanto precisa aplicar *hoje?* [p=0.4] {c}Tirar dez por cento duas vezes *não funciona.* [p=0.4] "
        "{d}Próximo episódio."),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já conhecia a regra do setenta e dois? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
