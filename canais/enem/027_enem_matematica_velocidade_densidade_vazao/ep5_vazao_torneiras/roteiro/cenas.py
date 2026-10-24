# Roteiro — Velocidade, Densidade e Vazão, Episódio 5 de 6: vazão, torneiras somando e ralos subtraindo
# Base: Estudos/Enem/estudos/01-matematica/12-velocidade-densidade-vazao.html — seção 06 + Questões 5, 9, 6 e 7 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na revisão):
#   VAZÃO É A VELOCIDADE DA ÁGUA: em vez de quilômetros por hora, litros por minuto.
#   PEDAÇOS DO TANQUE: quem enche em 6 horas enche 1/6 do tanque por hora (tanque fatiado em 6 fatias).
#   TORNEIRAS SÃO UM TIME (o tempo DIMINUI); O RALO É UM SABOTADOR (o tempo AUMENTA).
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Pré-requisitos: as três perguntas da taxa (ep. 1: taxa → divida; numerador → multiplique; denominador → divida ao
#   contrário), soma de frações com denominadores diferentes (série de Frações), 1 m³ = 1 000 L e 1 dia = 24 h (Unidades).
# Exemplos: o bloco b é a própria Q5 (1 500 L a 12,5 L/min), por desenho do usuário, e o bloco d/e são as Q6/Q7 (seção 06
#   do material usa os mesmos números). Q5 e Q6 são "eu faço" (repetir é ok); a Q7 é "você faz": nos blocos ela aparece como
#   EXEMPLO DO MÉTODO (o prompt pede o 1/4 − 1/6 no bloco e), e na questão a novidade é a leitura das alternativas.
# Nós fazemos (prompt): 2 h e 6 h → 1/2 + 1/6 = 3/6 + 1/6 = 4/6 = 2/3 do tanque por hora → 3/2 h = 1 h 30 min (< 2 h ✓).
# Contas conferidas em Python: 1 500 ÷ 12,5 = 120 min · 1/6 + 1/3 = 1/2 → 2 h · 1/4 − 1/6 = 1/12 → 12 h ·
#   250 000 · 180 = 45 000 000 L/dia = 45 000 m³/dia ÷ 24 = 1 875 m³/h · 45 000 · 24 = 1 080 000 · 1 875 ÷ 10 = 187,5 ·
#   1 875 · 10 = 18 750 · 1/4 + 1/6 = 5/12 → 2,4 h · média 6 e 3 = 4,5 h · média 4 e 6 = 5 h.
# QUESTÃO 5 (eu faço) → C (2 h). EXPLICAÇÃO NOSSA (o material não explica as erradas): nenhuma das outras sai da conta;
#   A (1 h) só encheria 750 L; E (3 h) encheria 2 250 L; B e D ficam meia hora para cada lado da certa.
# QUESTÃO 9 (nós fazemos) → B (1 875 m³/h). Material: D (45 000) sem a divisão por 24. CORREÇÃO DO MATERIAL (via prompt):
#   E (1 080 000) NÃO é "o total em litros por dia" (que é 45 000 000); é 45 000 · 24, multiplicou em vez de dividir.
#   Do prompt: A (187,5) e C (18 750) erram uma potência de 10.
# QUESTÃO 6 (eu faço) → B (2 h). Material: D e E maiores que 3 h, impossíveis. Do prompt: D soma, E multiplica, C (4 h 30)
#   média dos tempos, A (1 h 30) é o tempo de duas torneiras iguais à mais rápida (1/3 + 1/3 = 2/3 → 1,5 h).
# QUESTÃO 7 (você faz) → D (12 h). Material: A (2 h) impossível, menor que 4 h. Do prompt: C (10) soma, E (24) multiplica,
#   B (5) média; quem SOMA a vazão do ralo chega perto da A (1/4 + 1/6 = 5/12 → 2,4 h).
# Atalhos (verde): dividir por 12,5 = multiplicar por 8 e dividir por 100 · "produto sobre a soma" para duas torneiras
#   (6 · 3 ÷ 9 = 2) e "produto sobre a diferença" para torneira e ralo (4 · 6 ÷ 2 = 12) · fração do tanque por hora
#   virada de cabeça para baixo = tempo (1/2 → 2 h; 2/3 → 3/2 h).
# Frases-chave (meio e fim, idênticas): 1. Somam-se vazões, nunca tempos. 2. Torneira soma, ralo subtrai.
#   3. Com ajuda, o tempo diminui; com ralo, aumenta.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Duas torneiras juntas: 9 horas? NÃO! · Matemática ENEM, Velocidade, densidade e vazão, episódio 5"

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
        "{a}Uma torneira enche um tanque em *6 horas* [p=0.2] e outra em *3.* [p=0.3] Juntas, [p=0.2] quanto tempo? "
        "[p=0.5] {b}Quem soma diz *9 horas:* [p=0.3] mais tempo com *duas* torneiras do que com uma. [p=0.5] "
        "{c}A resposta é *2 horas,* [p=0.3] e você vai descobrir sem nem saber o tamanho do tanque."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular *tempo de enchimento,* [p=0.3] {b}*vazão* de uma cidade inteira "
        "[p=0.3] {c}e qualquer problema de *torneiras e ralos.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] pediu a taxa, [p=0.2] *divida;* [p=0.2] "
        "pediu o de cima, [p=0.2] *multiplique;* [p=0.2] pediu o de baixo, [p=0.2] *divida ao contrário.* [p=0.4] "
        "{b}Da série de Frações: [p=0.2] para somar, [p=0.2] mesmo denominador. [p=0.2] Um terço vale *dois sextos.* "
        "[p=0.4] {c}E de Unidades: [p=0.2] um metro cúbico tem *mil litros;* [p=0.2] um dia, [p=0.2] *vinte e quatro horas.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em três cenas de casa. [p=0.3] {a}Um *balde* embaixo da torneira. [p=0.4] {b}A *caixa-d'água* lá em "
        "cima, [p=0.2] enchendo pelo cano. [p=0.4] {c}E uma *banheira* enchendo [p=0.2] com o *ralo aberto.* [p=0.4] "
        "{d}A mesma pergunta nas três: [p=0.2] *em quanto tempo enche?*"),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="def", text=
        "{t}E o que decide esse tempo? [p=0.4] {a}A *vazão:* [p=0.2] a quantidade de água que passa [p=0.2] em cada "
        "unidade de tempo. [p=0.4] {b}Pense assim: [p=0.2] *vazão é a velocidade da água.* [p=0.3] Em vez de "
        "quilômetros por hora, [p=0.2] *litros por minuto.* [p=0.4] {c}A conta é volume dividido por tempo: [p=0.2] "
        "*Q igual a V sobre t.* [p=0.4] {d}E aparece em litros por segundo, [p=0.2] litros por minuto [p=0.2] ou metros "
        "cúbicos por hora."),
    dict(id="06", block="def", text=
        "{t}E se a pergunta for o *tempo?* [p=0.4] {a}O tempo está *embaixo* da fração: [p=0.2] *divida ao contrário.* "
        "[p=0.4] {b}Tempo igual a *volume dividido pela vazão.* [p=0.4] {c}Os litros que cabem no *reservatório,* "
        "[p=0.2] a sua *capacidade,* [p=0.2] divididos pelos litros que entram por minuto."),

    # ================= BLOCO B: A CAIXA =================
    dict(id="07", block="caixa", text=
        "{t}Vamos ver na prática? [p=0.3] {a}Uma caixa de *mil e quinhentos litros,* [p=0.2] com uma torneira de *doze e "
        "meio litros por minuto.* [p=0.4] {b}Tempo: [p=0.2] mil e quinhentos litros [p=0.2] dividido por doze e meio "
        "litros por minuto. [p=0.4] {c}Repare nas unidades: [p=0.2] *litro* em cima, [p=0.2] *litro* embaixo. [p=0.2] "
        "Os litros se cancelam [p=0.2] e sobra o *minuto.* [p=0.4] {d}Dá *cento e vinte minutos.* [p=0.3] Cada hora tem "
        "sessenta: [p=0.2] *duas horas.*"),
    dict(id="08", block="atalho_div", text=
        "{t}E como dividir por doze e meio sem calculadora? [p=0.4] {a}Atalho: [p=0.2] dividir por doze e meio [p=0.2] "
        "é o mesmo que *multiplicar por oito* [p=0.2] e *dividir por cem.* [p=0.2] Porque oito vezes doze e meio dá cem. "
        "[p=0.4] {b}Mil e quinhentos vezes oito: [p=0.2] doze mil. [p=0.2] Dividido por cem: [p=0.2] *cento e vinte.* "
        "[p=0.4] {c}Confira multiplicando de volta: [p=0.2] doze e meio vezes cento e vinte, [p=0.2] mil e quinhentos."),

    # ================= BLOCO C: FRAÇÕES DO TANQUE =================
    dict(id="09", block="fatias", text=
        "{t}Mas e quando o enunciado *não* diz o tamanho do tanque? [p=0.4] {a}Só diz: [p=0.2] esta torneira enche em "
        "*seis horas.* [p=0.4] {b}Truque: [p=0.2] *pense em pedaços do tanque.* [p=0.3] Corte o tanque em *seis fatias* "
        "iguais. [p=0.4] {c}Se enche tudo em seis horas, [p=0.2] enche *uma fatia por hora:* [p=0.2] *um sexto do tanque "
        "por hora.* [p=0.4] {d}Essa é a *fração do tanque:* [p=0.2] o pedaço que enche em uma hora. [p=0.2] E ela "
        "funciona como vazão, [p=0.2] sem saber quantos litros cabem."),

    # ================= BLOCO D: DUAS TORNEIRAS =================
    dict(id="10", block="duas", text=
        "{t}E com duas torneiras abertas juntas? [p=0.4] {a}A de seis horas: [p=0.2] *um sexto* do tanque por hora, "
        "[p=0.2] uma fatia. [p=0.4] {b}A de três horas: [p=0.2] *um terço,* [p=0.2] que é dois sextos: [p=0.2] *duas fatias.* [p=0.4] {c}Juntas, [p=0.2] um sexto mais dois sextos: [p=0.2] *três "
        "sextos,* [p=0.2] que é *metade* do tanque por hora. [p=0.4] {d}Metade por hora: [p=0.2] o tanque enche em "
        "*duas horas.*"),
    dict(id="11", block="duas", text=
        "{t}E por que diminuiu? [p=0.4] {a}Porque torneiras são *um time trabalhando junto:* [p=0.2] o tempo *diminui.* "
        "[p=0.4] {b}E o que se somou foram as *frações por hora,* [p=0.2] as vazões. [p=0.3] Nunca as horas. [p=0.4] {c}E o último passo: [p=0.2] se enche *um meio* por hora, [p=0.2] o "
        "tempo é *dois sobre um.* [p=0.2] A fração de cabeça para baixo."),
    dict(id="12", block="atalho_prod", text=
         "{t}Tem atalho? [p=0.3] Tem. [p=0.4] {a}Para *duas torneiras,* [p=0.2] o tempo junto é o "
        "*produto sobre a soma.* [p=0.4] {b}Seis vezes três, [p=0.2] dezoito. [p=0.2] Seis mais três, [p=0.2] nove. "
        "[p=0.2] Dezoito dividido por nove: [p=0.2] *duas horas.* [p=0.4] {c}Só cuidado: [p=0.2] ele vale para *duas* de "
        "cada vez. [p=0.2] Com três torneiras, [p=0.2] volte para as fatias."),

    # ================= BLOCO E: TORNEIRA E RALO =================
    dict(id="13", block="ralo", text=
        "{t}E se alguém *atrapalhar?* [p=0.4] {a}A água que entra é a *vazão de entrada.* "
        "[p=0.3] {b}A que sai pelo ralo, [p=0.2] a *vazão de saída.* [p=0.4] {c}O ralo é um *sabotador:* [p=0.2] a vazão dele "
        "*subtrai.* [p=0.4] {d}Torneira enche em *quatro* horas, [p=0.2] ralo esvazia em *seis.* [p=0.3] Um quarto "
        "menos um sexto."),
    dict(id="14", block="ralo", text=
        "{t}Como fazer essa conta? [p=0.3] {a}Mesmo denominador: [p=0.2] doze. [p=0.3] Um quarto é *três doze avos.* "
        "[p=0.2] Um sexto é *dois doze avos.* [p=0.4] {b}No tanque de doze fatias, [p=0.2] a cada hora a torneira pinta "
        "*três* [p=0.2] e o ralo apaga *duas.* [p=0.4] {c}Sobra *uma fatia por hora:* [p=0.2] um doze avos. [p=0.4] "
        "{d}De cabeça para baixo: [p=0.2] o tanque enche em *doze horas.*"),
    dict(id="15", block="ralo2", text=
        "{t}E se o ralo fosse *mais rápido* que a torneira? [p=0.4] {a}Sai mais do que entra: [p=0.2] *nunca* enche. [p=0.4] {b}Atalho para torneira e ralo: [p=0.2] *produto sobre a "
        "diferença.* [p=0.2] Quatro vezes seis, [p=0.2] vinte e quatro. [p=0.2] Seis menos quatro, [p=0.2] dois. [p=0.2] "
        "Vinte e quatro dividido por dois: [p=0.2] *doze.* [p=0.2] Bateu."),

    # ================= BLOCO F: A CONFERÊNCIA =================
    dict(id="16", block="confere", text=
        "{t}E como pegar um sinal trocado? [p=0.4] {a}Com *duas torneiras,* [p=0.2] o tempo fica *menor* que o da mais "
        "rápida sozinha: [p=0.2] duas horas, [p=0.2] menos que três. [p=0.4] {b}Com *ralo,* [p=0.2] fica *maior* que o "
        "da torneira sozinha: [p=0.2] doze horas, [p=0.2] mais que quatro. [p=0.4] {c}Se contrariar, [p=0.2] você trocou o sinal."),

    # ================= BLOCO G: Q = A · v =================
    dict(id="17", block="qav", text=
        "{t}E nos rios e canos? [p=0.4] {a}Aparece *Q igual a A vezes v:* [p=0.2] a *área* do corte do cano [p=0.2] "
        "vezes a *velocidade* da água. [p=0.4] {b}Isso é *Física.* [p=0.2] Por hoje, [p=0.2] só guarde que existe."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma torneira enche um tanque em *2 horas* [p=0.2] e outra em *6 horas.* [p=0.2] Juntas, "
        "[p=0.2] em quanto tempo? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}A primeira: [p=0.2] *um meio* do tanque por hora. [p=0.2] A segunda: [p=0.2] *um "
        "sexto.* [p=0.4] {b}Mesmo denominador: [p=0.2] um meio é *três sextos.* [p=0.2] Três sextos mais um sexto: "
        "[p=0.2] *quatro sextos,* [p=0.2] que simplifica para *dois terços* por hora. [p=0.4] {c}De cabeça para baixo: "
        "[p=0.2] *três meios* de hora, [p=0.2] *uma hora e meia.* [p=0.2] Uma hora e trinta minutos. [p=0.4] {d}Conferência: "
        "[p=0.2] menor que as duas horas da mais rápida. [p=0.2] Certo."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] somam-se vazões, [p=0.2] nunca tempos. [p=0.5] "
        "{b}Dois: [p=0.2] torneira soma, [p=0.2] ralo subtrai. [p=0.5] {c}Três: [p=0.2] com ajuda, [p=0.2] o tempo "
        "diminui; [p=0.2] com ralo, [p=0.2] aumenta."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar os tempos* de duas torneiras. [p=0.4] "
        "{b}Parece certo [p=0.2] porque são dois números de horas [p=0.2] e a palavra *juntas* lembra soma. [p=0.4] "
        "{c}Mas a soma dá *mais* tempo com mais ajuda. [p=0.2] Some as vazões."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] *somar* a vazão do ralo. [p=0.4] {b}Parece certo [p=0.2] porque você acabou de aprender "
        "a somar as frações. [p=0.4] {c}Mas o ralo tira água. [p=0.2] A vazão dele *subtrai.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] misturar *litros por minuto* com *horas.* [p=0.4] {b}Parece certo [p=0.2] porque a conta "
        "fecha [p=0.2] e não aparece nenhum aviso. [p=0.4] {c}Mas o resultado sai *sessenta vezes* errado. [p=0.2] "
        "Padronize a unidade de tempo antes."),
    dict(id="24", block="erros", text=
        "{a}Quarto: [p=0.2] esquecer de dividir por *vinte e quatro* [p=0.2] ao passar de *por dia* para *por hora.* "
        "[p=0.4] {b}Parece certo [p=0.2] porque já está em metros cúbicos [p=0.2] e parece o fim. "
        "[p=0.4] {c}Mas faltou o tempo. [p=0.2] Um dia tem vinte e quatro horas: [p=0.2] divida."),

    # ================= RODADA 1: QUESTÃO 5 (EU FAÇO) =================
    dict(id="25", block="q5", text=
        "{t}Questões, [p=0.2] em duas rodadas. [p=0.2] Rodada um: [p=0.2] vazão direta. [p=0.3] {a}Do nosso material, "
        "[p=0.2] e eu resolvo com você. [p=0.2] Uma caixa-d'água de *mil e quinhentos litros* "
        "[p=0.2] é abastecida com *doze e meio litros por minuto.* [p=0.2] Partindo vazia, [p=0.2] o tempo para encher "
        "é de: [p=0.4] {qa}A: [p=0.2] uma hora. [p=0.3] {qb}B: [p=0.2] uma hora e trinta minutos. [p=0.3] {qc}C: [p=0.2] "
        "duas horas. [p=0.3] {qd}D: [p=0.2] duas horas e trinta minutos. [p=0.3] {qe}E: [p=0.2] três horas. [p=0.4] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q5", text=
        "{t}Qual das três perguntas é esta? [p=0.2] Pede o *tempo,* [p=0.2] o de baixo: [p=0.2] divida ao contrário. "
        "[p=0.4] {a}Mil e quinhentos litros [p=0.2] dividido por doze e meio litros por minuto. [p=0.3] Litro corta "
        "litro, [p=0.2] sobra minuto: [p=0.2] *cento e vinte minutos.* [p=0.3] {b}Em horas: [p=0.2] *duas.* [p=0.2] "
        "{ok}*Letra C!* [p=0.4] {c}As outras não saem da conta. [p=0.2] {xa}Em uma hora, [p=0.2] só meia caixa. [p=0.2] {xe}Em três, "
        "[p=0.2] transborda. [p=0.2] {xb}A B [p=0.2] {xd}e a D [p=0.2] ficam meia hora para cada lado."),

    # ================= RODADA 1: QUESTÃO 9 (NÓS FAZEMOS) =================
    dict(id="27", block="q9", text=
        "{t}Agora uma cidade inteira, [p=0.2] juntos. [p=0.3] {a}Uma cidade com *duzentos e cinquenta "
        "mil* habitantes [p=0.2] consome, em média, [p=0.2] *cento e oitenta litros* por pessoa por dia. [p=0.3] A vazão "
        "média, [p=0.2] em metros cúbicos por hora, [p=0.2] é de: [p=0.4] {qa}A: [p=0.2] cento e oitenta e sete vírgula "
        "cinco. [p=0.3] {qb}B: [p=0.2] mil oitocentos e setenta e cinco. [p=0.3] {qc}C: [p=0.2] dezoito mil setecentos e "
        "cinquenta. [p=0.3] {qd}D: [p=0.2] quarenta e cinco mil. [p=0.3] {qe}E: [p=0.2] um milhão e oitenta mil. [p=0.4] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="28", block="q9", text=
        "{t}Um degrau de cada vez. [p=0.4] {a}A cidade toda num dia: [p=0.2] "
        "duzentos e cinquenta mil pessoas vezes cento e oitenta litros. [p=0.2] *Quarenta e cinco milhões* de litros por "
        "dia. [p=0.4] {b}Agora, metros cúbicos. [p=0.2] Cada metro cúbico tem mil litros: [p=0.2] divida por mil. [p=0.2] "
        "*Quarenta e cinco mil* metros cúbicos por dia. [p=0.4] {c}Por último, [p=0.2] por hora. [p=0.2] O dia tem vinte "
        "e quatro horas: [p=0.2] divida por vinte e quatro. [p=0.2] *Mil oitocentos e setenta e cinco* metros cúbicos "
        "por hora. [p=0.3] {ok}*Letra B!*"),
    dict(id="29", block="q9", text=
        "{t}E as erradas contam uma história. [p=0.3] {xd}A D, [p=0.2] quarenta e cinco mil, [p=0.2] parou no metro "
        "cúbico *por dia:* [p=0.2] esqueceu a divisão por vinte e quatro. [p=0.4] {xe}A E, [p=0.2] um milhão e oitenta "
        "mil, [p=0.2] é quarenta e cinco mil *vezes* vinte e quatro: [p=0.2] multiplicou pelas horas em vez de dividir. "
        "[p=0.4] {xa}A A [p=0.2] {xc}e a C [p=0.2] erram uma *potência de dez:* [p=0.2] um zero a menos, [p=0.2] um zero "
        "a mais."),

    # ================= RODADA 2: QUESTÃO 6 (EU FAÇO) =================
    dict(id="30", block="q6", text=
        "{t}Rodada dois: [p=0.2] frações do tanque. [p=0.3] {a}Uma torneira, [p=0.2] sozinha, [p=0.2] enche um tanque em "
        "*seis horas.* [p=0.2] Outra, [p=0.2] em *três.* [p=0.2] Abertas ao mesmo tempo, [p=0.2] encherão o tanque em: "
        "[p=0.4] {qa}A: [p=0.2] uma hora e trinta minutos. [p=0.3] {qb}B: [p=0.2] duas horas. [p=0.3] {qc}C: [p=0.2] "
        "quatro horas e trinta minutos. [p=0.3] {qd}D: [p=0.2] nove horas. [p=0.3] {qe}E: [p=0.2] dezoito horas. [p=0.4] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="31", block="q6", text=
        "{t}É a do começo, [p=0.2] e eu faço com você. [p=0.3] {a}Um sexto mais um terço, [p=0.2] que é dois sextos: "
        "[p=0.2] *três sextos,* [p=0.2] metade do tanque por hora. [p=0.3] {b}De cabeça para baixo: [p=0.2] *duas horas.* "
        "[p=0.2] {ok}*Letra B!* [p=0.3] {c}Conferência: [p=0.2] duas horas é menor que as três da mais rápida. [p=0.2] "
        "*Tempo menor:* [p=0.2] certo."),
    dict(id="32", block="q6", text=
        "{t}E as outras? [p=0.3] {xd}A D [p=0.2] *somou* os tempos. [p=0.2] {xe}A E [p=0.2] *multiplicou.* [p=0.2] As "
        "duas passam de três horas: [p=0.2] impossíveis. [p=0.4] {xc}A C [p=0.2] fez a *média* dos tempos, [p=0.2] seis "
        "mais três dividido por dois. [p=0.4] {xa}E a A, [p=0.2] uma hora e meia, [p=0.2] seria o tempo de *duas "
        "torneiras iguais à mais rápida,* [p=0.2] como se as duas enchessem em três horas."),

    # ================= RODADA 2: QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="33", block="q7", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma torneira enche um reservatório vazio em *quatro horas.* [p=0.2] Um ralo "
        "esvazia o reservatório cheio em *seis.* [p=0.2] Com os dois abertos, [p=0.2] a partir do reservatório vazio, "
        "[p=0.2] ele fica cheio em: [p=0.4] {qa}A: [p=0.2] duas horas. [p=0.3] {qb}B: [p=0.2] cinco. [p=0.3] {qc}C: "
        "[p=0.2] dez. [p=0.3] {qd}D: [p=0.2] doze. [p=0.3] {qe}E: [p=0.2] vinte e quatro horas. [p=0.4] {p}*Pause o vídeo "
        "e resolva sozinho.* [p=2.0]"),
    dict(id="34", block="q7", text=
        "{t}Conferindo. [p=0.3] {a}Torneira soma, [p=0.2] ralo subtrai: [p=0.2] um quarto menos um sexto. [p=0.2] Três "
        "doze avos menos dois doze avos: [p=0.2] *um doze avos* por hora. [p=0.4] {b}De cabeça para baixo: [p=0.2] *doze "
        "horas.* [p=0.2] {ok}*Letra D!* [p=0.3] {c}Conferência: [p=0.2] doze é maior que as quatro da torneira sozinha. "
        "[p=0.2] *Tempo maior:* [p=0.2] certo."),
    dict(id="35", block="q7", text=
        "{t}E as erradas? [p=0.3] {xc}A C, [p=0.2] dez, [p=0.2] somou os tempos. [p=0.2] {xe}A E, [p=0.2] vinte e "
        "quatro, [p=0.2] multiplicou. [p=0.2] {xb}A B, [p=0.2] cinco, [p=0.2] fez a média. [p=0.4] {xa}E a A, [p=0.2] "
        "duas horas, [p=0.2] é *impossível:* [p=0.2] com ralo, [p=0.2] não dá para encher mais rápido que a torneira "
        "sozinha. [p=0.3] É de quem *somou* a vazão do ralo."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="36", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] somam-se vazões, [p=0.2] nunca tempos. [p=0.5] "
        "{b}Dois: [p=0.2] torneira soma, [p=0.2] ralo subtrai. [p=0.5] {c}Três: [p=0.2] com ajuda, [p=0.2] o tempo "
        "diminui; [p=0.2] com ralo, [p=0.2] aumenta."),

    # ================= PONTE E CTA =================
    dict(id="37", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos *velocidade,* [p=0.2] *densidade* [p=0.2] e *vazão,* "
        "[p=0.3] {b}caçamos as pegadinhas [p=0.2] e treinamos para o ENEM, [p=0.3] {c}com questões de Matemática, "
        "[p=0.2] Física [p=0.2] e Geografia."),
    dict(id="38", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] no começo, você também pensou em nove horas? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
