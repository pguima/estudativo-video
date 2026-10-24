# Roteiro — Grandezas Proporcionais, Episódio 3 de 6: O gráfico de cada relação e a armadilha da parcela fixa
# Base: Estudos/Enem/estudos/01-matematica/07-grandezas-proporcionais.html — seções 05 e 10 (+ Questões 4 e 5 da seção 12).
# Função afim: só citada (série própria, semana 8).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A PERGUNTA DA ORIGEM: quando a primeira grandeza vale zero, a segunda também vale zero? (zero quilo de arroz custa zero;
#     zero quilômetro de táxi já custa R$ 6).
#   A reta direta NASCE na origem; a do táxi já nasce "devendo" a bandeirada.
#   A hipérbole nunca toca os eixos: por mais rápido que você dirija, o tempo de viagem nunca chega a zero.
# Decisão de desenho (do usuário): o gancho é o próprio táxi da Questão 5 e o bloco e) faz a conta. A Questão 5 entra como a
#   "prova oficial do gancho": leitura, pausa, resolução curta e foco nas alternativas erradas.
# Gráficos (exatos): arroz y = 5x (reta pela origem) · viagem x·y = 240 (hipérbole; pontos 40/6, 60/4, 80/3, 120/2, 240/1) ·
#   táxi y = 2,5x + 6 (reta que corta o eixo vertical em 6; 4 km → 16, 8 km → 26, 16 km → 46).
# Nós fazemos: 3 gráficos → reta pela origem = DIRETA · reta que corta o eixo vertical em 10 = NENHUMA · hipérbole = INVERSA.
# QUESTÃO 4 do material (texto idêntico na tela): C (arroz, k = 5). Explicações do material: A e B têm cobrança com
#   zero (afim); D é quadrática; E é inversa.
# QUESTÃO 5 do material: 6 + 2,5 · 16 = 46 → B. Explicação do material: D (R$ 52) = dobrou os 26 (bandeirada duas vezes).
#   Explicações NOSSAS (o material só explica a D): A (R$ 40) = 2,5 · 16, esqueceu a bandeirada; E (R$ 58) = 2 · 26 + 6,
#   dobrou tudo e ainda somou outra bandeirada; C (R$ 48) não sai de nenhuma conta com essa regra de cobrança.
# Frases-chave (meio e fim, idênticas, do usuário): 1. Direta: reta que nasce na origem. 2. Inversa: hipérbole que nunca
#   toca os eixos. 3. Zero de um dá zero do outro? Se não, há parcela fixa e não é proporção.
# Atalhos (verde): "o k é quanto a reta sobe a cada passo de 1" · "dedo no eixo em pé: cortou acima do zero? parcela fixa" ·
#   "separe o fixo do que varia: só a parte que varia acompanha" · "passar pela origem não basta: tem de ser reta".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "O gráfico de cada proporção e a armadilha do táxi (parcela fixa) · Matemática ENEM, grandezas proporcionais, ep. 3"

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
        "{a}Uma corrida de táxi de *oito quilômetros* [p=0.2] custa *vinte e seis reais.* [p=0.5] {b}Quanto custa uma de "
        "*dezesseis quilômetros?* [p=0.6] {c}Se você respondeu *cinquenta e dois reais,* [p=0.3] {d}caiu na armadilha *mais "
        "cobrada* deste assunto."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai identificar a relação *pelo desenho do gráfico,* [p=0.4] {b}e nunca mais vai cair "
        "na *parcela fixa.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do primeiro episódio: [p=0.2] na proporção *direta,* [p=0.2] a "
        "*divisão* de uma grandeza pela outra [p=0.2] dá sempre o mesmo número, [p=0.2] o *k.* [p=0.4] {b}Na *inversa,* "
        "[p=0.2] quem não muda é a *multiplicação.*"),
    dict(id="04", block="prereq", text=
        "{t}E como ler um gráfico. [p=0.3] {a}*Gráfico* é um desenho que mostra como uma grandeza muda com a outra. [p=0.4] "
        "{b}Ele tem duas réguas, [p=0.2] os *eixos:* [p=0.2] a deitada é o eixo *horizontal,* [p=0.2] {c}e a em pé é o eixo "
        "*vertical.* [p=0.4] {d}Cada ponto é um par: [p=0.2] ande na horizontal até um valor, [p=0.2] e suba até o outro. "
        "[p=0.4] {e}E o canto onde os eixos se cruzam, [p=0.2] no zero dos dois, [p=0.2] se chama *origem.*"),

    # ================= CONCRETO: ARROZ E TÁXI =================
    dict(id="05", block="compras", text=
        "{t}Agora, duas compras lado a lado. [p=0.3] {a}De um lado, *arroz a cinco reais o quilo.* [p=0.4] {b}Do outro, "
        "um *táxi:* [p=0.2] *seis reais de bandeirada,* [p=0.2] mais *dois e cinquenta por quilômetro.* [p=0.4] {c}A "
        "*bandeirada* é o valor que o taxímetro já marca quando você entra, [p=0.2] antes de andar um metro. [p=0.4] {d}Ela "
        "é uma *parcela fixa:* [p=0.2] um valor cobrado uma vez só, [p=0.2] qualquer que seja a distância."),
    dict(id="06", block="compras", text=
        "{t}Os dois parecem iguais: [p=0.2] {a}mais quilos, mais caro; [p=0.3] {b}mais quilômetros, mais caro. [p=0.4] "
        "{c}Mas só *um* deles é proporcional. [p=0.3] Qual? [p=0.4] {d}O gráfico conta."),

    # ================= BLOCO A: DIRETA = RETA PELA ORIGEM =================
    dict(id="07", block="arroz", text=
        "{t}Primeiro, o arroz. [p=0.2] Como é o desenho de uma proporção direta? [p=0.4] {a}Zero quilo custa *zero.* "
        "[p=0.3] {b}Um quilo, [p=0.2] cinco reais. [p=0.3] {c}Dois quilos, [p=0.2] dez. [p=0.3] {d}Três, [p=0.2] quinze. "
        "[p=0.4] {e}Ligue os pontos: [p=0.2] sai uma *reta,* [p=0.2] uma linha sem curva nenhuma. [p=0.4] {f}E ela *nasce "
        "na origem.*"),
    dict(id="08", block="arroz", text=
        "{t}E repare quanto a reta *sobe* a cada quilo a mais: [p=0.2] {a}sempre *cinco reais.* [p=0.4] {b}Essa subida tem "
        "nome: [p=0.2] *inclinação,* [p=0.2] o quanto a reta é íngreme. [p=0.4] {c}E a inclinação é o próprio *k,* [p=0.2] "
        "o preço por quilo. [p=0.4] {d}Um arroz de oito reais daria uma reta *mais em pé,* [p=0.2] mas nascendo no mesmo "
        "lugar: [p=0.2] a origem."),

    # ================= BLOCO B: INVERSA = HIPÉRBOLE =================
    dict(id="09", block="viagem", text=
        "{t}Agora, a viagem de *duzentos e quarenta quilômetros.* [p=0.3] Que desenho faz uma relação inversa? [p=0.4] "
        "{a}A quarenta por hora, [p=0.2] seis horas. [p=0.3] {b}A sessenta, [p=0.2] quatro horas. [p=0.3] {c}A oitenta, "
        "[p=0.2] três. [p=0.3] {d}A cento e vinte, [p=0.2] duas. [p=0.4] {e}Velocidade vezes tempo [p=0.2] dá sempre "
        "duzentos e quarenta. [p=0.4] {f}Ligue os pontos: [p=0.2] *não sai reta.* [p=0.3] Sai uma curva que desce rápido "
        "e depois vai deitando. [p=0.3] {g}Ela se chama *hipérbole.*"),
    dict(id="10", block="viagem", text=
        "{t}E repare nas pontas da curva. [p=0.3] {a}Quanto mais rápido, [p=0.2] menos tempo, [p=0.2] e a curva desce em "
        "direção ao eixo deitado. [p=0.3] {b}Mas *nunca encosta:* [p=0.2] por mais rápido que você dirija, [p=0.2] o tempo "
        "de viagem *nunca chega a zero.* [p=0.4] {c}Do outro lado, [p=0.2] quanto mais devagar, [p=0.2] mais horas, "
        "[p=0.2] e a curva sobe colada no eixo em pé, [p=0.2] sem tocar nele. [p=0.4] {d}Uma linha da qual a curva chega "
        "cada vez mais perto, [p=0.2] sem nunca tocar, [p=0.2] se chama *assíntota.* [p=0.3] {e}Na hipérbole, [p=0.2] os "
        "dois eixos são assíntotas."),

    # ================= BLOCO C: O TÁXI = RETA FORA DA ORIGEM =================
    dict(id="11", block="taxi", text=
        "{t}E o táxi? [p=0.3] {a}Zero quilômetro: [p=0.2] o taxímetro já marca *seis reais.* [p=0.4] {b}Quatro quilômetros: "
        "[p=0.2] seis mais dez, [p=0.2] dezesseis. [p=0.3] {c}Oito: [p=0.2] seis mais vinte, [p=0.2] vinte e seis. [p=0.4] "
        "{d}Ligue os pontos: [p=0.2] sai uma reta, sim. [p=0.3] {e}Mas ela *não nasce na origem.* [p=0.3] Nasce lá no "
        "*seis,* [p=0.2] no eixo em pé. [p=0.4] {f}É como se a corrida já começasse *devendo a bandeirada.*"),
    dict(id="12", block="taxi", text=
        "{t}Uma reta assim, [p=0.2] que corta o eixo em pé *acima do zero,* [p=0.2] {a}não é proporção nenhuma: [p=0.2] "
        "nem direta, [p=0.2] nem inversa. [p=0.4] {b}Ela até tem nome, [p=0.2] *função afim,* [p=0.2] mas é assunto de "
        "uma série própria. [p=0.4] {c}Aqui, guarde só isso: [p=0.2] reta que *não passa pela origem* [p=0.2] não é "
        "proporcional."),

    # ================= BLOCO D: O TESTE DE DOIS SEGUNDOS =================
    dict(id="13", block="teste", text=
        "{t}Então, como decidir em *dois segundos,* [p=0.2] olhando um gráfico? [p=0.4] {a}Olhe onde a reta corta o eixo "
        "em pé. [p=0.4] {b}Corta no zero, [p=0.2] na origem? [p=0.2] Pode ser direta. [p=0.4] {c}Corta *acima* do zero? "
        "[p=0.2] Existe uma parcela fixa, [p=0.2] e a relação *não é proporcional.* [p=0.4] {d}Atalho: [p=0.2] antes de "
        "qualquer conta, [p=0.2] *ponha o dedo no eixo em pé.*"),

    # ================= BLOCO E: O TÁXI EM NÚMEROS =================
    dict(id="14", block="contas", text=
        "{t}Agora, de volta à pergunta do começo. [p=0.4] {a}Oito quilômetros: [p=0.2] seis de bandeirada, [p=0.2] mais "
        "dois e cinquenta vezes oito, [p=0.2] vinte. [p=0.3] Total: [p=0.2] *vinte e seis.* [p=0.5] {b}Dezesseis "
        "quilômetros: [p=0.2] seis de bandeirada, [p=0.2] mais dois e cinquenta vezes dezesseis, [p=0.2] quarenta. [p=0.3] "
        "Total: [p=0.2] *quarenta e seis reais.* [p=0.4] {c}Não cinquenta e dois."),
    dict(id="15", block="contas", text=
        "{t}Por quê? [p=0.3] {a}A distância dobrou, [p=0.2] mas só a parte *por quilômetro* dobrou: [p=0.2] de vinte para "
        "quarenta. [p=0.4] {b}A bandeirada continuou *seis,* [p=0.2] porque é cobrada uma vez só. [p=0.4] {c}Quem dobrou "
        "os vinte e seis inteiros [p=0.2] pagou a bandeirada *duas vezes.* [p=0.4] {d}Atalho: [p=0.2] *separe o fixo do que "
        "varia.* [p=0.3] Só a parte que varia acompanha a distância."),

    # ================= BLOCO F: A MESMA ESTRUTURA NO DIA A DIA =================
    dict(id="16", block="diadia", text=
        "{t}E essa estrutura, [p=0.2] um fixo mais um que varia, [p=0.2] aparece em todo lugar. [p=0.4] {a}A conta de luz "
        "e de água com *taxa mínima:* [p=0.2] você paga um valor mesmo sem consumir nada. [p=0.4] {b}O plano de celular com "
        "*franquia:* [p=0.2] um valor fixo por mês, [p=0.2] mais o que passar dela. [p=0.4] {c}O *frete* com taxa de "
        "despacho, [p=0.2] mais o preço por quilo. [p=0.4] {d}E o *salário* com uma parte fixa, [p=0.2] mais a comissão "
        "sobre as vendas. [p=0.4] {e}Em todos, [p=0.2] dobrar o consumo *não dobra* a conta."),

    # ================= BLOCO G: A PERGUNTA DA ORIGEM =================
    dict(id="17", block="origem", text=
        "{t}Por isso, a pergunta que resolve tudo isso é uma só: [p=0.2] a *pergunta da origem.* [p=0.4] {a}Quando a "
        "primeira grandeza vale zero, [p=0.2] a segunda também vale zero? [p=0.5] {b}Zero quilo de arroz custa zero: "
        "[p=0.2] pode ser proporcional. [p=0.4] {c}Zero quilômetro de táxi já custa seis reais: [p=0.2] *não é.*"),
    dict(id="18", block="origem", text=
        "{t}Mas atenção: [p=0.2] passar pela origem é *necessário,* [p=0.2] mas não basta. [p=0.3] Também precisa ser uma "
        "*reta.* [p=0.4] {a}A área de um quadrado, [p=0.2] a partir do lado, [p=0.2] nasce no zero, [p=0.2] mas é uma "
        "*curva:* [p=0.2] dobrar o lado quadruplica a área. [p=0.4] {b}Os *juros compostos* [p=0.2] e as *tarifas por "
        "faixa* [p=0.2] também não são proporcionais. [p=0.3] {c}Esses casos você já viu na série de Razão."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.2] Três gráficos. [p=0.3] {a}O primeiro: [p=0.2] uma reta que sai da origem. [p=0.3] {b}O "
        "segundo: [p=0.2] uma reta que corta o eixo em pé *no dez.* [p=0.3] {c}O terceiro: [p=0.2] uma curva que desce e "
        "vai deitando, [p=0.2] sem tocar os eixos. [p=0.4] {d}Para cada um: [p=0.2] *direta, inversa ou nenhuma?* [p=0.3] "
        "*Pause o vídeo e responda.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}O primeiro é reta e nasce na origem: [p=0.2] *direta.* [p=0.4] {b}O segundo começa "
        "no dez: [p=0.2] tem parcela fixa, [p=0.2] então *nenhuma.* [p=0.2] Não é proporcional. [p=0.4] {c}E o terceiro "
        "é a hipérbole: [p=0.2] *inversa.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] direta: [p=0.2] reta que nasce na origem. [p=0.5] {b}Dois: "
        "[p=0.2] inversa: [p=0.2] hipérbole que nunca toca os eixos. [p=0.5] {c}Três: [p=0.2] zero de um dá zero do outro? "
        "[p=0.3] Se não, [p=0.2] há parcela fixa [p=0.2] e não é proporção."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que *toda reta* é proporção direta. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a direta também é uma reta. [p=0.4] {c}Mas a direta é a reta que *nasce na "
        "origem.* [p=0.3] Reta que corta o eixo em pé acima do zero [p=0.2] tem parcela fixa."),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] *dobrar o preço do táxi* junto com a distância. [p=0.4] {b}Parece certo, [p=0.2] porque a "
        "distância dobrou, [p=0.2] e a gente dobra tudo no automático. [p=0.4] {c}Mas a bandeirada *não dobra:* [p=0.2] só "
        "a parte por quilômetro."),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] achar que a hipérbole *toca os eixos.* [p=0.4] {b}Parece certo, [p=0.2] porque no desenho "
        "ela chega bem pertinho. [p=0.4] {c}Mas o tempo de uma viagem nunca chega a zero: [p=0.2] os eixos são "
        "*assíntotas.*"),
    dict(id="25", block="erros", text=
        "{a}Quarto: [p=0.2] achar que *estar relacionado* é o mesmo que *ser proporcional.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque uma grandeza muda quando a outra muda. [p=0.4] {c}Mas o táxi, [p=0.2] a conta de luz [p=0.2] e a "
        "área do quadrado [p=0.2] mudam junto, [p=0.2] e nenhum é proporcional. [p=0.3] Proporção exige o *k* constante."),

    # ================= QUESTÃO 4 DO MATERIAL =================
    dict(id="26", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Entre as situações "
        "abaixo, [p=0.2] aquela em que as duas grandezas envolvidas são *diretamente proporcionais* é: [p=0.4] {qa}A: "
        "[p=0.2] o valor de uma corrida de táxi com bandeirada fixa, [p=0.2] em função da distância. [p=0.3] {qb}B: [p=0.2] "
        "o valor da conta de luz com taxa de disponibilidade, [p=0.2] em função do consumo. [p=0.3] {qc}C: [p=0.2] o preço "
        "total de arroz vendido a cinco reais o quilo, [p=0.2] em função da quantidade comprada. [p=0.3] {qd}D: [p=0.2] a "
        "área de um terreno quadrado, [p=0.2] em função da medida do lado. [p=0.3] {qe}E: [p=0.2] o tempo de uma viagem de "
        "distância fixa, [p=0.2] em função da velocidade média. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="q4", text=
        "{t}Vamos fazer a pergunta da origem *em voz alta,* [p=0.2] uma por uma. [p=0.4] {xa}A: [p=0.2] zero quilômetro de "
        "táxi custa zero? [p=0.2] Não: [p=0.2] já tem a bandeirada. [p=0.4] {xb}B: [p=0.2] consumo zero, conta zero? "
        "[p=0.2] Não: [p=0.2] a taxa de disponibilidade é a taxa mínima, [p=0.2] cobrada mesmo sem consumo. [p=0.4] {c}C: "
        "[p=0.2] zero quilo de arroz custa zero? [p=0.2] *Sim.* [p=0.3] E dobrar os quilos dobra o preço: [p=0.2] direta, "
        "[p=0.2] com *k igual a cinco.* [p=0.3] {ok}*Letra C!*"),
    dict(id="28", block="q4", text=
        "{t}E as outras duas? [p=0.3] {xd}A D nasce no zero, [p=0.2] mas dobrar o lado *quadruplica* a área: [p=0.2] é "
        "quadrática, [p=0.2] não direta. [p=0.4] {xe}E a E: [p=0.2] mais velocidade, [p=0.2] menos tempo. [p=0.2] É "
        "*inversa.* [p=0.4] {a}Repare: [p=0.2] as cinco situações têm grandezas *relacionadas.* [p=0.3] Só uma é "
        "diretamente proporcional."),

    # ================= QUESTÃO 5 DO MATERIAL (a prova oficial do gancho) =================
    dict(id="29", block="q5", text=
        "{t}Mais uma do material, [p=0.2] e essa você já conhece. [p=0.4] {a}Uma corrida de táxi custa *seis reais* de "
        "bandeirada, [p=0.2] mais *dois reais e cinquenta centavos* por quilômetro rodado. [p=0.3] {b}Sabendo que uma "
        "corrida de oito quilômetros custa vinte e seis reais, [p=0.2] o valor de uma corrida de *dezesseis quilômetros* "
        "será de: [p=0.4] {qa}A: [p=0.2] quarenta reais. [p=0.3] {qb}B: [p=0.2] quarenta e seis reais. [p=0.3] {qc}C: "
        "[p=0.2] quarenta e oito reais. [p=0.3] {qd}D: [p=0.2] cinquenta e dois reais. [p=0.3] {qe}E: [p=0.2] cinquenta e "
        "oito reais. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{t}Pergunta da origem: [p=0.2] {a}zero quilômetro custa zero? [p=0.2] Não, [p=0.2] custa seis. [p=0.3] Então, "
        "*nada de dobrar.* [p=0.4] {b}Seis, [p=0.2] mais dois e cinquenta vezes dezesseis, [p=0.2] quarenta: [p=0.2] "
        "*quarenta e seis reais.* [p=0.3] {ok}*Letra B!*"),
    dict(id="31", block="q5", text=
        "{t}E as erradas? [p=0.3] {xd}A D é a armadilha da questão: [p=0.2] dobrou os vinte e seis [p=0.2] e pagou a "
        "bandeirada duas vezes. [p=0.4] {xa}A A esqueceu a bandeirada: [p=0.2] só os quarenta dos quilômetros. [p=0.4] "
        "{xe}A E fez pior: [p=0.2] dobrou tudo [p=0.2] e ainda somou mais uma bandeirada. [p=0.4] {xc}E a C não sai de "
        "nenhuma conta com essa regra de cobrança."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] direta: [p=0.2] reta que nasce na origem. [p=0.5] "
        "{b}Dois: [p=0.2] inversa: [p=0.2] hipérbole que nunca toca os eixos. [p=0.5] {c}Três: [p=0.2] zero de um dá zero "
        "do outro? [p=0.3] Se não, [p=0.2] há parcela fixa [p=0.2] e não é proporção."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}E quando uma grandeza depende de *duas* outras, [p=0.2] {b}uma de forma direta [p=0.2] e outra inversa? "
        "[p=0.4] {c}É assim que estão escritas *metade das fórmulas de Física.* [p=0.4] {d}Próximo episódio."),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na bandeirada do táxi? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
