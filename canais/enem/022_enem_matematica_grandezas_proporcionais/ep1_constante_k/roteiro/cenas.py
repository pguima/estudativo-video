# Roteiro — Grandezas Proporcionais, Episódio 1 de 6: A constante k, o número que não muda e revela a relação inteira
# Base: Estudos/Enem/estudos/01-matematica/07-grandezas-proporcionais.html — seções 02, 03 e 04 (+ Questões 2 e 3 da seção 12).
# O teste do dobro e a regra de três já foram ensinados na série de Razão: aqui, só revisão relâmpago (sem reensinar a regra de três).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O k é o número que NÃO muda enquanto tudo varia, e sempre significa alguma coisa (preço por quilo, velocidade, densidade).
#   DIRETA = a etiqueta de preço por quilo: preço ÷ quilos dá sempre o mesmo número.
#   INVERSA = a viagem de 240 km é um "bolo" fixo: velocidade × tempo dá sempre 240.
# Exemplos âncora do usuário MANTIDOS (decisão da série): combustível 180 km → 15 L (k = 1/12) e a viagem de 240 km.
#   As Questões 2 (300 km) e 3 (80 → 100 km/h, k = 240) entram como APLICAÇÃO: o mesmo k, outro valor pedido.
#   Para não entregar as respostas antes, os blocos NÃO calculam 300 km nem 100 km/h: usam 120 km (10 L) e 120 km/h (2 h).
#   O exemplo de hora decimal do bloco g) é 240 km a 150 km/h = 1,6 h = 1 h 36 min (o 2,4 h da Questão 3 fica para ela).
# Nós fazemos: R$ 36 por 4 kg → k = 9 R$/kg → 7 kg = R$ 63.
# QUESTÃO 2 do material (texto idêntico na tela): k = 15/180 = 1/12 → 300/12 = 25 L → C. Plausibilidade do material
#   (distância ×1,7, consumo ×1,7). Explicações NOSSAS (o material não explica as erradas): B (20) = 300 ÷ 15, dividiu a
#   distância pelos litros; D (30) = dobrou os 15 L, como se a distância tivesse dobrado (300 não é o dobro de 180);
#   A (18) e E (36) caem pela plausibilidade (18 cresce pouco demais; 36 mais que dobra).
# QUESTÃO 3 do material: 80 · 3 = 240 = k → 240/100 = 2,4 h → 0,4 · 60 = 24 min → 2 h 24 min → A. B (2 h 40) = leu 2,4 como
#   2 h 40 (material). Explicações NOSSAS: D (3 h 45) = tratou como direta, 3 · 100/80 = 3,75 h, e o tempo aumentou (absurdo);
#   E (3 h 75) = o mesmo erro da D e ainda escreveu 75 minutos; C (2 h 50) não sai da conta (e 2,5 h seria 2 h 30).
# Frases-chave (meio e fim, idênticas): 1. Direta: o quociente não muda. Inversa: o produto não muda.
#   2. Um par de valores basta para achar o k. 3. Décimo de hora não é minuto: multiplique por 60.
# Atalhos (verde): "direta divide, inversa multiplica" · "um par basta: ache o k, escreva a fórmula" ·
#   "multiplicar por 1/12 é dividir por 12" · "o k da inversa é o que fica fixo" · "cada décimo de hora = 6 minutos".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "A constante k: o número que não muda (direta e inversa do zero) | Grandezas Proporcionais Ep. 1"
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
        "{a}Na regra de três [p=0.2] você resolvia a proporção. [p=0.5] {b}Agora vai descobrir o *número escondido* por trás "
        "dela, [p=0.3] {c}o *k,* [p=0.3] {d}que transforma qualquer problema [p=0.2] numa *única multiplicação.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai achar o k [p=0.2] a partir de *um único par de valores,* [p=0.4] {b}montar a "
        "*fórmula* [p=0.4] {c}e *prever* qualquer outro valor."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}O *teste do dobro,* [p=0.2] da série de Razão: [p=0.2] dobre uma "
        "grandeza e veja a outra. [p=0.3] Dobrou também? [p=0.2] *Direta.* [p=0.3] Virou metade? [p=0.2] *Inversa.* [p=0.5] "
        "{b}E dividir por uma fração [p=0.2] é multiplicar pela fração *virada.* [p=0.3] Dividir por um meio [p=0.2] é "
        "multiplicar por dois."),

    # ================= CONCRETO: A ETIQUETA =================
    dict(id="04", block="etiqueta", text=
        "{t}Comece pelo mercado. [p=0.3] {a}A carne custa *vinte reais o quilo.* [p=0.4] {b}Dois quilos: [p=0.2] quarenta "
        "reais. [p=0.3] {c}Três quilos: [p=0.2] sessenta. [p=0.4] {d}Agora divida o preço pelos quilos, [p=0.2] em cada "
        "compra. [p=0.3] Quarenta dividido por dois: [p=0.2] vinte. [p=0.3] Sessenta dividido por três: [p=0.2] vinte. "
        "[p=0.4] {e}O preço muda, [p=0.2] os quilos mudam, [p=0.3] mas *esse número não muda.* [p=0.3] É ele que está "
        "escrito na etiqueta."),

    # ================= BLOCO A: AS DUAS CONSTANTES =================
    dict(id="05", block="constante", text=
        "{t}Preço e quilos são *grandezas:* [p=0.2] coisas que dá para medir ou contar. [p=0.4] {a}E quando duas grandezas "
        "são diretamente proporcionais, [p=0.3] o *quociente* entre elas, [p=0.2] que é o resultado da divisão, [p=0.3] "
        "{b}fica *constante:* [p=0.2] não muda nunca. [p=0.4] {c}Esse número tem nome: [p=0.2] *constante de "
        "proporcionalidade.* [p=0.3] A gente chama de *k.*"),
    dict(id="06", block="constante", text=
        "{t}Em fórmula: [p=0.2] {a}*y dividido por x é igual a k.* [p=0.4] {b}Ou, passando o x para o outro lado, [p=0.2] *y "
        "é igual a k vezes x.* [p=0.4] {c}Na etiqueta: [p=0.2] o preço é igual a vinte vezes os quilos. [p=0.4] {d}Essa "
        "fórmula serve para *qualquer* compra."),
    dict(id="07", block="constante", text=
        "{t}E na inversa? [p=0.3] {a}Pense numa viagem de *duzentos e quarenta quilômetros.* [p=0.3] Mais rápido, [p=0.2] "
        "menos tempo. [p=0.4] {b}Aqui o que não muda é o *produto,* [p=0.2] o resultado da multiplicação: [p=0.3] {c}*x vezes "
        "y é igual a k.* [p=0.4] {d}Ou: [p=0.2] *y é igual a k dividido por x.* [p=0.5] {e}Atalho: [p=0.2] *direta, divida. "
        "Inversa, multiplique.* [p=0.3] O que der sempre igual [p=0.2] é o k."),

    # ================= BLOCO B: O K SIGNIFICA ALGO =================
    dict(id="08", block="significa", text=
        "{t}E aqui está o segredo: [p=0.2] o k *nunca é um número solto.* [p=0.4] Ele sempre significa alguma coisa. [p=0.4] "
        "{a}Preço e quantidade: [p=0.2] o k é o *preço por unidade.* [p=0.3] {b}Distância e tempo: [p=0.2] o k é a "
        "*velocidade.* [p=0.3] {c}Massa e volume: [p=0.2] o k é a *densidade,* [p=0.2] quanto de massa cabe em cada pedaço "
        "de espaço."),
    dict(id="09", block="significa", text=
        "{t}Nas inversas também. [p=0.3] {a}Velocidade e tempo: [p=0.2] o k é a *distância* da viagem. [p=0.4] {b}Operários "
        "e prazo de uma obra: [p=0.2] o k é o *total de trabalho.* [p=0.4] {c}Por isso, [p=0.2] quando achar o k, [p=0.2] "
        "pergunte: [p=0.2] *o que esse número significa?* [p=0.3] Muitas vezes, [p=0.2] ele já é a resposta da questão."),

    # ================= BLOCO C: ACHAR O K COM UM PAR =================
    dict(id="10", block="par", text=
        "{t}Como achar o k? [p=0.3] Basta *um par de valores.* [p=0.4] {a}Se y vale *quinze* quando x vale *cinco,* [p=0.2] "
        "e a relação é direta, [p=0.3] {b}divida: [p=0.2] quinze dividido por cinco, [p=0.2] *k igual a três.* [p=0.4] {c}A "
        "fórmula completa é *y igual a três x.* [p=0.4] {d}E agora qualquer valor sai numa multiplicação: [p=0.2] x igual a "
        "oito? [p=0.2] Três vezes oito, [p=0.2] *vinte e quatro.*"),
    dict(id="11", block="par", text=
        "{t}Na inversa, [p=0.2] o mesmo caminho, [p=0.2] multiplicando. [p=0.3] {a}Se y vale *seis* quando x vale *quatro,* "
        "[p=0.3] {b}k é seis vezes quatro, [p=0.2] *vinte e quatro.* [p=0.3] {c}Fórmula: [p=0.2] y igual a vinte e quatro "
        "dividido por x. [p=0.3] {d}x igual a oito? [p=0.2] Vinte e quatro dividido por oito, [p=0.2] *três.* [p=0.4] "
        "{e}Atalho: [p=0.2] *um par basta.* [p=0.2] Ache o k, [p=0.2] escreva a fórmula, [p=0.2] e acabou."),

    # ================= BLOCO D: DIRETA NA PRÁTICA =================
    dict(id="12", block="combustivel", text=
        "{t}Agora, na vida real. [p=0.3] {a}Um carro gasta *quinze litros* em *cento e oitenta quilômetros.* [p=0.3] {b}Em "
        "trezentos e sessenta, [p=0.2] *trinta litros.* [p=0.3] {c}Em quinhentos e quarenta, [p=0.2] *quarenta e cinco.* "
        "[p=0.4] {d}Teste do dobro: [p=0.2] o dobro da distância, [p=0.2] o dobro de litros. [p=0.2] *Direta.* [p=0.4] {e}Então "
        "divida: [p=0.2] litros por quilômetros."),
    dict(id="13", block="combustivel", text=
        "{a}Quinze sobre cento e oitenta. [p=0.3] Simplificando por quinze: [p=0.2] *um doze avos.* [p=0.4] {b}Trinta sobre "
        "trezentos e sessenta: [p=0.2] *um doze avos.* [p=0.3] {c}Quarenta e cinco sobre quinhentos e quarenta: [p=0.2] *um "
        "doze avos.* [p=0.4] {d}Esse é o k: [p=0.2] *um doze avos de litro por quilômetro.* [p=0.3] {e}Cada quilômetro gasta "
        "um doze avos de litro."),
    dict(id="14", block="combustivel", text=
        "{t}E como se usa? [p=0.3] {a}Litros igual a um doze avos vezes a distância. [p=0.4] {b}Atalho: [p=0.2] multiplicar "
        "por um doze avos [p=0.2] é o mesmo que *dividir por doze.* [p=0.4] {c}Cento e vinte quilômetros? [p=0.2] Cento e vinte "
        "dividido por doze, [p=0.2] *dez litros.* [p=0.4] {d}E repare: [p=0.2] o doze é o famoso *quilômetro por litro* do "
        "painel. [p=0.3] É o mesmo k, [p=0.2] visto de cabeça para baixo."),
    dict(id="15", block="sequencia", text=
        "{t}E isso vale para listas inteiras. [p=0.3] {a}Uma *sequência* é uma lista de números em ordem. [p=0.4] {b}Dois, "
        "três e cinco. [p=0.2] {c}Seis, nove e quinze. [p=0.4] {d}Divida um pelo outro, [p=0.2] termo a termo: [p=0.2] seis "
        "sobre dois, [p=0.2] nove sobre três, [p=0.2] quinze sobre cinco. [p=0.3] Sempre *três.* [p=0.4] {e}São *sequências "
        "diretamente proporcionais,* [p=0.2] com k igual a três."),

    # ================= BLOCO E: INVERSA NA PRÁTICA =================
    dict(id="16", block="bolo", text=
        "{t}Agora a viagem de duzentos e quarenta quilômetros. [p=0.3] Pense nela como um *bolo:* [p=0.2] o tamanho total não "
        "muda. [p=0.4] {a}A *quarenta* quilômetros por hora, [p=0.2] você corta o bolo em fatias de quarenta: [p=0.2] *seis "
        "horas.* [p=0.4] {b}A *sessenta,* [p=0.2] fatias maiores: [p=0.2] *quatro horas.* [p=0.4] {c}A *oitenta:* [p=0.2] "
        "*três horas.*"),
    dict(id="17", block="bolo", text=
        "{t}Multiplique cada par. [p=0.3] {a}Quarenta vezes seis: [p=0.2] duzentos e quarenta. [p=0.3] {b}Sessenta vezes "
        "quatro: [p=0.2] duzentos e quarenta. [p=0.3] {c}Oitenta vezes três: [p=0.2] duzentos e quarenta. [p=0.4] {d}O k é "
        "*duzentos e quarenta,* [p=0.2] e ele significa a própria *distância.* [p=0.4] {e}Atalho: [p=0.2] na inversa, [p=0.2] "
        "*o k é o que o problema mantém fixo.*"),
    dict(id="18", block="bolo", text=
        "{t}E a fórmula prevê qualquer velocidade. [p=0.3] {a}Tempo igual a duzentos e quarenta dividido pela velocidade. "
        "[p=0.4] {b}Cento e vinte quilômetros por hora? [p=0.2] Duzentos e quarenta dividido por cento e vinte: [p=0.2] *duas "
        "horas.* [p=0.4] {c}O dobro da velocidade de sessenta, [p=0.2] a metade do tempo de quatro horas. [p=0.3] O teste do "
        "dobro confirma."),

    # ================= BLOCO F: A PONTE 1/x =================
    dict(id="19", block="ponte1x", text=
        "{t}Uma curiosidade que liga as duas ideias. [p=0.3] {a}O *inverso* de um número [p=0.2] é um dividido por ele: "
        "[p=0.2] o inverso de quatro é *um quarto.* [p=0.4] {b}Tempo igual a duzentos e quarenta dividido pela velocidade "
        "[p=0.2] é o mesmo que duzentos e quarenta *vezes* o inverso da velocidade. [p=0.4] {c}Então: [p=0.2] se y é inversa "
        "de x, [p=0.3] *y é direta de um sobre x.* [p=0.3] É a mesma relação, [p=0.2] vista por outro ângulo."),

    # ================= BLOCO G: O RELÓGIO =================
    dict(id="20", block="relogio", text=
        "{t}Cuidado agora, [p=0.2] porque o relógio *não é decimal.* [p=0.4] {a}Duzentos e quarenta quilômetros a *cento e "
        "cinquenta* por hora: [p=0.2] duzentos e quarenta dividido por cento e cinquenta, [p=0.2] *um vírgula seis hora.* "
        "[p=0.4] {b}Uma hora e sessenta minutos? [p=0.3] *Não!* [p=0.3] {c}Uma hora tem sessenta minutos, [p=0.2] não cem. "
        "[p=0.3] {d}Zero vírgula seis hora [p=0.2] é zero vírgula seis vezes sessenta: [p=0.2] *trinta e seis minutos.* "
        "[p=0.3] Uma hora e trinta e seis."),
    dict(id="21", block="relogio", text=
        "{t}Mais um, [p=0.2] o mais famoso. [p=0.3] {a}*Zero vírgula quatro hora* não é quarenta minutos. [p=0.4] {b}Zero "
        "vírgula quatro vezes sessenta: [p=0.2] *vinte e quatro minutos.* [p=0.4] {c}Atalho: [p=0.2] *cada décimo de hora "
        "vale seis minutos.* [p=0.3] Zero vírgula quatro: [p=0.2] quatro vezes seis, [p=0.2] vinte e quatro."),

    # ================= NÓS FAZEMOS =================
    dict(id="22", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um produto custa *trinta e seis reais* por *quatro quilos.* [p=0.4] {b}Qual é o k? [p=0.3] "
        "{c}E quanto custam *sete quilos?* [p=0.4] {d}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="23", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Preço e quilos: [p=0.2] direta. [p=0.2] Então divida: [p=0.2] trinta e seis dividido "
        "por quatro, [p=0.2] *k igual a nove.* [p=0.3] Nove reais por quilo. [p=0.4] {b}Fórmula: [p=0.2] preço igual a nove "
        "vezes os quilos. [p=0.3] {c}Sete quilos: [p=0.2] nove vezes sete, [p=0.2] *sessenta e três reais.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="24", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] direta, [p=0.2] o quociente não muda. [p=0.2] Inversa, [p=0.2] "
        "o produto não muda. [p=0.5] {b}Dois: [p=0.2] um par de valores basta para achar o k. [p=0.5] {c}Três: [p=0.2] décimo "
        "de hora não é minuto: [p=0.2] multiplique por sessenta."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="25", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] usar o *quociente* numa relação inversa, [p=0.2] ou "
        "o produto numa direta. [p=0.4] {b}Parece certo, [p=0.2] porque as duas contas dão algum número. [p=0.4] {c}Mas só "
        "uma dá *sempre o mesmo* número. [p=0.3] Faça o teste do dobro antes."),
    dict(id="26", block="erros", text=
        "{a}Segundo: [p=0.2] ler *dois vírgula quatro horas* como duas horas e quarenta minutos. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o quatro está ali, [p=0.2] logo depois da vírgula. [p=0.4] {c}Mas a hora tem sessenta minutos: "
        "[p=0.2] zero vírgula quatro vezes sessenta, [p=0.2] vinte e quatro. [p=0.3] Duas horas e vinte e quatro."),
    dict(id="27", block="erros", text=
        "{a}Terceiro: [p=0.2] tratar o k como um *símbolo sem significado.* [p=0.4] {b}Parece certo, [p=0.2] porque é só uma "
        "letra na fórmula. [p=0.4] {c}Mas o k é o preço por quilo, [p=0.2] a velocidade, [p=0.2] a distância. [p=0.3] Muitas "
        "vezes, [p=0.2] *ele é a própria resposta* que a questão pede."),

    # ================= QUESTÃO 2 DO MATERIAL =================
    dict(id="28", block="q2", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}O consumo de combustível de "
        "um automóvel é diretamente proporcional à distância percorrida. [p=0.3] {b}Em um trajeto de *cento e oitenta "
        "quilômetros,* [p=0.2] o veículo consumiu *quinze litros.* [p=0.3] {c}Mantidas as condições, [p=0.2] o consumo em um "
        "trajeto de *trezentos quilômetros* será de: [p=0.4] {qa}A: [p=0.2] dezoito litros. [p=0.3] {qb}B: [p=0.2] vinte "
        "litros. [p=0.3] {qc}C: [p=0.2] vinte e cinco litros. [p=0.3] {qd}D: [p=0.2] trinta litros. [p=0.3] {qe}E: [p=0.2] "
        "trinta e seis litros. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="29", block="q2", text=
        "{t}Vamos resolver. [p=0.3] {a}O próprio enunciado diz: [p=0.2] *direta.* [p=0.2] Então o quociente é o k. [p=0.4] "
        "{b}Quinze sobre cento e oitenta: [p=0.2] *um doze avos* de litro por quilômetro. [p=0.4] {c}Trezentos vezes um doze "
        "avos: [p=0.2] trezentos dividido por doze, [p=0.2] *vinte e cinco litros.* [p=0.3] {ok}*Letra C!* [p=0.4] {d}Confira: "
        "[p=0.2] a distância cresceu umas *um vírgula sete* vezes, [p=0.2] e quinze vezes um vírgula sete dá uns vinte e cinco. "
        "[p=0.3] Coerente."),
    dict(id="30", block="q2", text=
        "{t}E as outras? [p=0.3] {xb}A B dividiu trezentos por quinze: [p=0.2] misturou os números. [p=0.4] {xd}A D *dobrou* "
        "os quinze litros, [p=0.2] mas trezentos não é o dobro de cento e oitenta. [p=0.4] {xa}A A cresce pouco demais, [p=0.3] "
        "{xe}e a E mais que dobra. [p=0.3] O bom senso elimina as duas."),

    # ================= QUESTÃO 3 DO MATERIAL =================
    dict(id="31", block="q3", text=
        "{t}Mais uma do material. [p=0.3] {a}Um motorista percorre determinado trajeto em *três horas,* [p=0.2] mantendo "
        "velocidade média de *oitenta quilômetros por hora.* [p=0.4] {b}Se aumentar a velocidade média para *cem* quilômetros "
        "por hora, [p=0.2] o mesmo trajeto será percorrido em: [p=0.4] {qa}A: [p=0.2] duas horas e vinte e quatro minutos. "
        "[p=0.3] {qb}B: [p=0.2] duas horas e quarenta minutos. [p=0.3] {qc}C: [p=0.2] duas horas e cinquenta minutos. [p=0.3] "
        "{qd}D: [p=0.2] três horas e quarenta e cinco minutos. [p=0.3] {qe}E: [p=0.2] três horas e setenta e cinco minutos. "
        "[p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="32", block="q3", text=
        "{t}Vamos resolver. [p=0.3] {a}Mesmo trajeto: [p=0.2] mais rápido, [p=0.2] menos tempo. [p=0.2] *Inversa.* [p=0.2] "
        "Então o produto é o k. [p=0.4] {b}Oitenta vezes três: [p=0.2] *duzentos e quarenta.* [p=0.2] É a distância! [p=0.4] "
        "{c}Cem vezes o tempo dá duzentos e quarenta: [p=0.2] o tempo é *dois vírgula quatro horas.* [p=0.4] {d}E agora o "
        "relógio: [p=0.2] zero vírgula quatro vezes sessenta, [p=0.2] *vinte e quatro minutos.* [p=0.3] {ok}*Letra A!* [p=0.3] "
        "Duas horas e vinte e quatro. [p=0.3] Menos de três horas: [p=0.2] coerente."),
    dict(id="33", block="q3", text=
        "{t}E as outras? [p=0.3] {xb}A B é a armadilha do relógio: [p=0.2] leu dois vírgula quatro como duas horas e "
        "quarenta. [p=0.4] {xd}A D tratou como *direta,* [p=0.2] e o tempo aumentou indo mais rápido: [p=0.2] absurdo. [p=0.4] "
        "{xe}A E fez o mesmo [p=0.2] e ainda escreveu setenta e cinco minutos. [p=0.4] {xc}E a C não sai da conta."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="34", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] direta, [p=0.2] o quociente não muda. [p=0.2] Inversa, "
        "[p=0.2] o produto não muda. [p=0.5] {b}Dois: [p=0.2] um par de valores basta para achar o k. [p=0.5] {c}Três: [p=0.2] "
        "décimo de hora não é minuto: [p=0.2] multiplique por sessenta."),

    # ================= PONTE E CTA =================
    dict(id="35", block="ponte", text=
        "{a}E quando o ENEM te dá uma *tabela* [p=0.2] e pergunta que relação é essa? [p=0.4] {b}Duas contas resolvem qualquer "
        "questão desse tipo. [p=0.4] {c}Próximo episódio."),
    dict(id="36", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha lido duas vírgula quatro horas como duas e quarenta? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
