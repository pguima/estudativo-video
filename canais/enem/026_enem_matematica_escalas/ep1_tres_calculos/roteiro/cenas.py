# Roteiro — Escalas, Plantas e Mapas, Episódio 1 de 4: o que é escala, os três cálculos e a cadeia até o quilômetro
# Base: Estudos/Enem/estudos/01-matematica/11-escalas-plantas-mapas.html — seções 02 e 05 + Questões 1, 2 e 3 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O mapa é uma FOTO ENCOLHIDA do mundo: cada 1 cm do papel "guarda" n cm do mundo real.
#   Do mapa para o mundo, o número CRESCE: multiplique pelo denominador. Do mundo para o mapa, ENCOLHE: divida.
#   O ATALHO DOS 5 ZEROS: em 1 : n, cada centímetro vale n ÷ 100 000 km (a tesoura corta cinco zeros do denominador).
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos: o bloco d e a cadeia usam a Questão 1 (6 cm em 1 : 500 000), pedida pelo prompt e resolvida como "eu faço".
#   Exemplos NOSSOS nos blocos g e h (para não entregar a Q2 "nós fazemos" e a Q3 "você faz"):
#   cálculo 2: 20 km em 1 : 500 000 → 2 000 000 cm ÷ 500 000 = 4 cm (atalho: 20 ÷ 5 = 4 cm);
#   cálculo 3: 3 cm para 15 km → 1 500 000 cm → 3 / 1 500 000 = 1 / 500 000 (atalho: 15 ÷ 3 = 5 km por cm → 500 000).
#   O erro 3 usa "12 km e 4 cm sem converter" (dados da Q3), como pede o prompt: mostra só o erro (4/12 = 1 : 3), não a resposta.
# Nós fazemos (prompt): 1 : 200 000, 3 cm → 2 km por cm → 6 km.
# QUESTÃO 1 (texto idêntico na tela): 6 × 500 000 = 3 000 000 cm = 30 000 m = 30 km → B.
#   O material diz que "C, D e E são de quem parou em cada degrau"; só a E é isso. O vídeo diz:
#   E (30 000) = parou nos metros; D (3 000) = pulou o degrau cm → m (só ÷ 1 000); C (300) = cortou zeros demais (÷ 10 000);
#   A (3) = cortou seis zeros em vez de cinco. (Os 3 000 000 cm, parar no primeiro degrau, nem estão nas alternativas.)
# QUESTÃO 2 (texto idêntico): 45 km = 4 500 000 cm ÷ 1 500 000 = 3 cm → B. Material: E (300 cm) = três metros de mapa.
#   Explicações NOSSAS: A (0,3 cm) = um zero a menos na conversão; C (30 cm) = um zero a mais;
#   D (33 cm) = dividiu ao contrário, com os km parados em metros: 1 500 000 ÷ 45 000 ≈ 33.
# QUESTÃO 3 (texto idêntico): 12 km = 1 200 000 cm; 4 / 1 200 000 = 1 / 300 000 → C.
#   O material diz que a B é de quem usou 12 000; 4 / 12 000 = 1 : 3 000, que é a A (parou nos metros). O vídeo diz:
#   A = parou nos metros; B (1 : 30 000) = perdeu um zero; D (1 : 3 000 000) = zero a mais;
#   E (1 : 4 800 000) = multiplicou 4 × 1 200 000 em vez de dividir.
# Atalhos (verde): "corte cinco zeros do denominador" · cálculo 2 pelo atalho (real em km ÷ km por cm) ·
#   cálculo 3 pelo atalho (km ÷ cm = km por cm; devolva os cinco zeros) · conferência de plausibilidade.
# Frases-chave (meio e fim, idênticas): 1. Escala é desenho sobre real, na mesma unidade.
#   2. Do mapa para o mundo, multiplique; do mundo para o mapa, divida. 3. Em 1 : n, cada centímetro vale n ÷ 100 000 km.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Escala do zero: os três cálculos e o caminho até o quilômetro · Matemática ENEM, Escalas episódio 1"

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
        "{a}A conta da escala é fácil: [p=0.2] *uma multiplicação.* [p=0.4] {b}O que derruba é o caminho de *centímetros* "
        "até *quilômetros.* [p=0.4] {c}Quem pula um degrau [p=0.2] erra por *cem* [p=0.2] ou por *mil,* [p=0.3] {d}e a "
        "alternativa errada [p=0.2] *está lá.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai resolver os *três tipos* de questão de escala [p=0.3] {b}e chegar ao "
        "*quilômetro* sem pular degrau."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Da série de Razão: [p=0.2] *razão* é uma comparação feita por "
        "*divisão.* [p=0.2] Dois para cinco [p=0.2] é dois dividido por cinco. [p=0.4] {b}E, da série de Unidades, "
        "[p=0.2] a escada: [p=0.2] de centímetro para metro, [p=0.2] *divide por cem.* [p=0.2] De metro para "
        "quilômetro, [p=0.2] *divide por mil.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe três objetos. [p=0.3] {a}Um *mapa rodoviário:* [p=0.2] uma estrada de centenas de quilômetros [p=0.2] "
        "cabe num palmo de papel. [p=0.4] {b}A *planta* de um apartamento à venda: [p=0.2] a sala inteira [p=0.2] em "
        "poucos centímetros. [p=0.4] {c}E um carrinho em miniatura [p=0.2] com a etiqueta *escala um para quarenta e "
        "três:* [p=0.2] o carro de verdade é quarenta e três vezes maior. [p=0.4] {d}Os três são a mesma coisa: [p=0.2] "
        "uma *foto encolhida* do mundo."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}E o que, exatamente, diz o quanto a foto encolheu? [p=0.4] {a}A *escala.* [p=0.3] {b}Escala é a razão entre "
        "o *desenho* [p=0.2] e o *real.* [p=0.4] {c}*Desenho* é a medida no papel, [p=0.2] a que você mede com a régua. "
        "[p=0.2] *Medida real* é a do mundo, [p=0.2] a que existe de verdade. [p=0.4] {d}Escala é igual a desenho "
        "*dividido* por real."),
    dict(id="06", block="definicao", text=
        "{t}Só que tem uma condição. [p=0.3] {a}As duas medidas têm que estar na *mesma unidade:* [p=0.2] centímetro "
        "com centímetro. [p=0.4] {b}Aí as unidades se cancelam, [p=0.2] e sobra um *número puro:* [p=0.2] um número sem "
        "unidade nenhuma, [p=0.2] nem centímetro, [p=0.2] nem quilômetro. [p=0.4] {c}É por isso que a escala aparece "
        "assim: [p=0.2] *um, dois-pontos, duzentos e cinquenta mil.* [p=0.2] Sem unidade."),

    # ================= BLOCO B: LER A ESCALA =================
    dict(id="07", block="ler", text=
        "{t}E como se lê um para duzentos e cinquenta mil? [p=0.4] {a}O número de baixo da fração, [p=0.2] o que vem "
        "depois dos dois-pontos, [p=0.2] é o *denominador.* [p=0.4] {b}E a leitura é: [p=0.2] *um centímetro no papel "
        "vale duzentos e cinquenta mil centímetros no terreno.* [p=0.4] {c}Lembre da foto encolhida: [p=0.2] cada "
        "centímetro do papel *guarda* duzentos e cinquenta mil centímetros do mundo."),

    # ================= BLOCO C: AMPLIAÇÃO =================
    dict(id="08", block="ampliacao", text=
        "{t}E a escala sempre encolhe? [p=0.3] Quase sempre. [p=0.3] {a}Quando o desenho é menor que o real, [p=0.2] é "
        "uma *escala de redução:* [p=0.2] mapas e plantas. [p=0.4] {b}Mas existe a *escala de ampliação,* [p=0.2] em que "
        "o desenho é maior que o objeto. [p=0.2] *Dez para um:* [p=0.2] o desenho de uma peça pequenininha, [p=0.2] dez "
        "vezes maior. [p=0.4] {c}E *um para um* [p=0.2] é o tamanho natural. [p=0.4] {d}Só para você conhecer. [p=0.2] "
        "Hoje, a gente fica na redução."),

    # ================= BLOCO D: CÁLCULO 1 =================
    dict(id="09", block="calc1", text=
        "{t}Agora, o primeiro cálculo. [p=0.2] Num mapa de escala um para quinhentos mil, [p=0.2] duas cidades estão a "
        "*seis centímetros.* [p=0.2] Qual é a distância real? [p=0.4] {a}Vamos *desencolher* o mapa. [p=0.3] {b}Cada "
        "centímetro guarda quinhentos mil centímetros. [p=0.2] São seis centímetros: [p=0.2] seis *vezes* quinhentos "
        "mil. [p=0.4] {c}*Três milhões de centímetros.* [p=0.4] {d}Do mapa para o mundo, [p=0.2] o número *cresce:* "
        "[p=0.2] *multiplique pelo denominador.*"),

    # ================= BLOCO E: A CADEIA =================
    dict(id="10", block="cadeia", text=
        "{t}Mas quem mede estrada em centímetros? [p=0.4] {a}O resultado está certo, [p=0.2] só que na unidade errada. "
        "[p=0.2] Faltam *dois degraus.* [p=0.4] {b}Primeiro degrau: [p=0.2] centímetro para metro, [p=0.2] *dividido por "
        "cem.* [p=0.2] Três milhões viram *trinta mil metros.* [p=0.4] {c}Segundo degrau: [p=0.2] metro para "
        "quilômetro, [p=0.2] *dividido por mil.* [p=0.2] Trinta mil viram *trinta quilômetros.* [p=0.4] {d}Agora sim: "
        "[p=0.2] uma distância de estrada."),
    dict(id="11", block="cadeia", text=
        "{t}Dá para subir os dois degraus de uma vez? [p=0.3] Dá. [p=0.3] {a}Dividir por cem e depois por mil [p=0.2] é o "
        "mesmo que dividir por *cem mil.* [p=0.4] {b}Cem mil tem *cinco zeros.* [p=0.3] Então, de centímetro para "
        "quilômetro, [p=0.2] *a vírgula anda cinco casas para a esquerda.* [p=0.4] {c}Três milhões de centímetros, "
        "[p=0.2] cinco casas: [p=0.2] *trinta quilômetros.*"),

    # ================= BLOCO F: O ATALHO DOS 5 ZEROS =================
    dict(id="12", block="atalho", text=
        "{t}E se der para fazer tudo isso antes de começar? [p=0.4] {a}Atalho: [p=0.2] numa escala um para *n,* [p=0.2] "
        "cada centímetro vale *n dividido por cem mil* quilômetros. [p=0.4] {b}Na prática: [p=0.2] *corte cinco zeros* "
        "do denominador. [p=0.4] {c}Quinhentos mil, [p=0.2] tesoura nos cinco zeros: [p=0.2] sobra o *cinco.* [p=0.2] "
        "Cada centímetro vale *cinco quilômetros.* [p=0.4] {d}Seis centímetros, [p=0.2] seis vezes cinco: [p=0.2] "
        "*trinta quilômetros.* [p=0.2] De cabeça."),
    dict(id="13", block="atalho", text=
        "{t}Vamos treinar a tesoura. [p=0.3] {a}Um para *um milhão:* [p=0.2] corta cinco zeros, [p=0.2] sobra dez. "
        "[p=0.2] *Dez quilômetros* por centímetro. [p=0.4] {b}Um para *duzentos e cinquenta mil:* [p=0.2] tem só quatro "
        "zeros. [p=0.2] Então a vírgula anda as cinco casas: [p=0.2] *dois vírgula cinco quilômetros* por centímetro. "
        "[p=0.4] {c}Um para *cinquenta mil:* [p=0.2] do mesmo jeito, [p=0.2] *zero vírgula cinco quilômetro,* [p=0.2] "
        "meio quilômetro por centímetro."),

    # ================= BLOCO G: CÁLCULO 2 =================
    dict(id="14", block="calc2", text=
        "{t}E o caminho contrário? [p=0.2] Você conhece a distância real [p=0.2] e quer saber quanto ela ocupa no papel. "
        "[p=0.4] {a}Exemplo: [p=0.2] *vinte quilômetros* num mapa um para quinhentos mil. [p=0.4] {b}Primeiro, [p=0.2] "
        "passe o real para *centímetros,* [p=0.2] a unidade da régua: [p=0.2] vinte quilômetros são *dois milhões* de "
        "centímetros. [p=0.4] {c}Do mundo para o mapa, [p=0.2] o número *encolhe:* [p=0.2] *divida pelo denominador.* "
        "[p=0.2] Dois milhões dividido por quinhentos mil: [p=0.2] *quatro centímetros.* [p=0.4] {d}Atalho: [p=0.2] "
        "cada centímetro vale cinco quilômetros. [p=0.2] Vinte dividido por cinco: [p=0.2] quatro centímetros."),

    # ================= BLOCO H: CÁLCULO 3 =================
    dict(id="15", block="calc3", text=
        "{t}E quando a pergunta é a própria escala? [p=0.4] {a}Exemplo: [p=0.2] *três centímetros* no mapa [p=0.2] "
        "representam *quinze quilômetros.* [p=0.4] {b}Escala é desenho sobre real, [p=0.2] na *mesma unidade.* [p=0.2] "
        "Quinze quilômetros são *um milhão e quinhentos mil* centímetros. [p=0.4] {c}Três sobre um milhão e quinhentos "
        "mil. [p=0.2] Divida em cima e embaixo por três, [p=0.2] para o de cima virar um: [p=0.2] *um para quinhentos "
        "mil.*"),
    dict(id="16", block="calc3", text=
        "{t}E tem atalho aqui também? [p=0.3] Tem. [p=0.3] {a}Divida os quilômetros pelos centímetros: [p=0.2] quinze "
        "dividido por três, [p=0.2] *cinco quilômetros por centímetro.* [p=0.4] {b}Agora faça a tesoura ao contrário: "
        "[p=0.2] *devolva os cinco zeros.* [p=0.2] Cinco vira *quinhentos mil.* [p=0.4] {c}A escala é um para quinhentos "
        "mil. [p=0.2] Os dois caminhos batem."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Num mapa um para *duzentos mil,* [p=0.2] *três centímetros* valem quantos quilômetros? "
        "[p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}É do mapa para o mundo: [p=0.2] o número cresce. [p=0.4] {b}Tesoura: [p=0.2] "
        "duzentos mil, [p=0.2] cinco zeros fora, [p=0.2] *dois quilômetros* por centímetro. [p=0.4] {c}Três centímetros, "
        "[p=0.2] três vezes dois: [p=0.2] *seis quilômetros.* [p=0.4] {d}E pela cadeia, [p=0.2] para conferir: [p=0.2] "
        "três vezes duzentos mil, [p=0.2] seiscentos mil centímetros, [p=0.2] seis mil metros, [p=0.2] seis "
        "quilômetros. [p=0.2] Bateu."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] escala é desenho sobre real, na mesma unidade. [p=0.5] "
        "{b}Dois: [p=0.2] do mapa para o mundo, multiplique; [p=0.2] do mundo para o mapa, divida. [p=0.5] {c}Três: "
        "[p=0.2] em um para *n,* [p=0.2] cada centímetro vale *n* dividido por cem mil quilômetros."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *parar nos centímetros reais.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque a multiplicação está perfeita: [p=0.2] três milhões. [p=0.4] {c}Mas ainda "
        "faltam os degraus. [p=0.2] Divida por cem mil [p=0.2] e chegue ao quilômetro."),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] *multiplicar* quando devia *dividir,* [p=0.2] ou o contrário. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque os números são os mesmos, [p=0.2] só muda a operação. [p=0.4] {c}Pergunte para onde você vai. "
        "[p=0.2] Para o mundo, [p=0.2] o número cresce: [p=0.2] multiplica. [p=0.2] Para o mapa, [p=0.2] encolhe: "
        "[p=0.2] divide."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] montar a escala com *unidades diferentes.* [p=0.2] Quatro centímetros para doze "
        "quilômetros, [p=0.2] quatro sobre doze, [p=0.2] *um para três.* [p=0.4] {b}Parece certo, [p=0.2] porque a "
        "fração simplificou bonitinho. [p=0.4] {c}Mas um para três diria que o mapa tem um terço do tamanho da estrada. "
        "[p=0.2] Passe tudo para centímetros *antes* de dividir."),
    dict(id="23", block="erros", text=
        "{a}Quarto: [p=0.2] *inverter a razão:* [p=0.2] real sobre desenho, [p=0.2] *duzentos e cinquenta mil para "
        "um.* [p=0.4] {b}Parece certo, [p=0.2] porque os números são os de sempre. [p=0.4] {c}Mas isso seria um mapa "
        "duzentas e cinquenta mil vezes *maior* que o mundo. [p=0.2] Escala é *desenho sobre real:* [p=0.2] o um vem "
        "primeiro."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="24", block="q1", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Esta primeira, [p=0.2] eu "
        "resolvo com você. [p=0.4] {a}Em um mapa rodoviário de escala *um para quinhentos mil,* [p=0.2] a distância "
        "entre duas cidades é representada por um segmento de *seis centímetros.* [p=0.2] A distância real é de: "
        "[p=0.4] {qa}A: [p=0.2] três quilômetros. [p=0.3] {qb}B: [p=0.2] trinta. [p=0.3] {qc}C: [p=0.2] trezentos. "
        "[p=0.3] {qd}D: [p=0.2] três mil. [p=0.3] {qe}E: [p=0.2] trinta mil quilômetros."),
    dict(id="25", block="q1", text=
        "{t}Qual dos três cálculos é? [p=0.3] {a}Tenho o desenho [p=0.2] e quero o real: [p=0.2] do mapa para o mundo. "
        "[p=0.2] *Cálculo um:* [p=0.2] multiplica. [p=0.4] {b}Seis vezes quinhentos mil: [p=0.2] três milhões de "
        "centímetros. [p=0.4] {c}A cadeia: [p=0.2] dividido por cem, [p=0.2] trinta mil metros; [p=0.2] dividido por "
        "mil, [p=0.2] *trinta quilômetros.* [p=0.4] {d}Pelo atalho: [p=0.2] tesoura nos cinco zeros, [p=0.2] cinco "
        "quilômetros por centímetro, [p=0.2] seis vezes cinco, [p=0.2] trinta. [p=0.4] {e}Plausível? [p=0.2] Trinta "
        "quilômetros entre duas cidades: [p=0.2] faz sentido. [p=0.3] {ok}*Letra B!*"),
    dict(id="26", block="q1", text=
        "{t}E as outras? [p=0.2] Repare: [p=0.2] elas são *tropeços na cadeia.* [p=0.4] {xe}A E, [p=0.2] trinta mil, "
        "[p=0.2] *parou nos metros:* [p=0.2] subiu um degrau e esqueceu o outro. [p=0.4] {xd}A D, [p=0.2] três mil, "
        "[p=0.2] *pulou o degrau do metro:* [p=0.2] dividiu só por mil. [p=0.4] {xc}A C, [p=0.2] trezentos, [p=0.2] "
        "cortou só quatro zeros. [p=0.4] {xa}E a A, [p=0.2] três, [p=0.2] cortou *seis.* [p=0.4] {f}Cada degrau errado "
        "[p=0.2] tem a sua alternativa esperando."),

    # ================= QUESTÃO 2 (NÓS FAZEMOS) =================
    dict(id="27", block="q2", text=
        "{t}A próxima, a gente faz junto. [p=0.3] {a}Um cartógrafo precisa representar uma distância real de *quarenta "
        "e cinco quilômetros* [p=0.2] em um mapa de escala *um para um milhão e quinhentos mil.* [p=0.2] No mapa, essa "
        "distância ocupará: [p=0.4] {qa}A: [p=0.2] zero vírgula três centímetro. [p=0.3] {qb}B: [p=0.2] três. [p=0.3] "
        "{qc}C: [p=0.2] trinta. [p=0.3] {qd}D: [p=0.2] trinta e três. [p=0.3] {qe}E: [p=0.2] trezentos centímetros. "
        "[p=0.5] {p}Qual dos três cálculos é? [p=0.2] *Pause e tente.* [p=2.0]"),
    dict(id="28", block="q2", text=
        "{t}Tenho o real [p=0.2] e quero o desenho: [p=0.2] do mundo para o mapa. [p=0.2] *Cálculo dois:* [p=0.2] "
        "divide. [p=0.4] {a}Passe para centímetros: [p=0.2] quarenta e cinco quilômetros [p=0.2] são *quatro milhões e "
        "quinhentos mil* centímetros. [p=0.4] {b}Dividido por um milhão e quinhentos mil: [p=0.2] *três centímetros.* "
        "[p=0.4] {c}Pelo atalho: [p=0.2] tesoura, [p=0.2] quinze quilômetros por centímetro; [p=0.2] quarenta e cinco "
        "dividido por quinze, [p=0.2] três. [p=0.4] {d}Plausível? [p=0.2] Três centímetros cabem numa folha. [p=0.3] "
        "{ok}*Letra B!*"),
    dict(id="29", block="q2", text=
        "{t}E as erradas? [p=0.3] {xe}A E, [p=0.2] trezentos centímetros, [p=0.2] seriam *três metros* de mapa: [p=0.2] "
        "nenhuma folha aguenta. [p=0.4] {xa}A A [p=0.2] {xc}e a C [p=0.2] erraram um zero na conversão, [p=0.2] uma "
        "para menos, [p=0.2] outra para mais. [p=0.4] {xd}E a D, [p=0.2] trinta e três, [p=0.2] dividiu ao contrário, "
        "[p=0.2] com os quilômetros parados em metros."),

    # ================= QUESTÃO 3 (VOCÊ FAZ) =================
    dict(id="30", block="q3", text=
        "{t}E esta é *sua.* [p=0.3] {a}Em um mapa, [p=0.2] um trecho de estrada com *doze quilômetros* de extensão real "
        "[p=0.2] está representado por um segmento de *quatro centímetros.* [p=0.2] A escala desse mapa é: [p=0.4] "
        "{qa}A: [p=0.2] um para três mil. [p=0.3] {qb}B: [p=0.2] um para trinta mil. [p=0.3] {qc}C: [p=0.2] um para "
        "trezentos mil. [p=0.3] {qd}D: [p=0.2] um para três milhões. [p=0.3] {qe}E: [p=0.2] um para quatro milhões e "
        "oitocentos mil. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="31", block="q3", text=
        "{t}Conferindo. [p=0.2] A pergunta é a própria escala: [p=0.2] *cálculo três.* [p=0.4] {a}Mesma unidade: "
        "[p=0.2] doze quilômetros são *um milhão e duzentos mil* centímetros. [p=0.4] {b}Desenho sobre real: [p=0.2] "
        "quatro sobre um milhão e duzentos mil. [p=0.2] Divida por quatro: [p=0.2] *um para trezentos mil.* [p=0.4] "
        "{c}Pelo atalho: [p=0.2] doze dividido por quatro, [p=0.2] três quilômetros por centímetro; [p=0.2] devolva os "
        "cinco zeros: [p=0.2] trezentos mil. [p=0.3] {ok}*Letra C!*"),
    dict(id="32", block="q3", text=
        "{t}E as outras? [p=0.3] {xa}A A, [p=0.2] um para três mil, [p=0.2] *parou nos metros:* [p=0.2] usou doze mil. "
        "[p=0.4] {xb}A B perdeu um zero; [p=0.2] {xd}a D ganhou um a mais. [p=0.4] {xe}E a E [p=0.2] *multiplicou* "
        "quatro por um milhão e duzentos mil, [p=0.2] em vez de dividir."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] escala é desenho sobre real, na mesma unidade. "
        "[p=0.5] {b}Dois: [p=0.2] do mapa para o mundo, multiplique; [p=0.2] do mundo para o mapa, divida. [p=0.5] "
        "{c}Três: [p=0.2] em um para *n,* [p=0.2] cada centímetro vale *n* dividido por cem mil quilômetros."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Se você fotocopiar um mapa *ampliado,* [p=0.2] qual escala continua valendo: [p=0.2] o *número* [p=0.2] ou a "
        "*barrinha?* [p=0.5] {b}E um para dez mil [p=0.2] é escala *grande* [p=0.2] ou *pequena?* [p=0.5] {c}Próximo "
        "episódio."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já conhecia o atalho dos cinco zeros? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
