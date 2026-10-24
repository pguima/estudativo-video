# Roteiro — Sistemas de Equações Lineares, Episódio 4 de 5: três incógnitas, escalonar ou somar tudo.
# Base: Estudos/Enem/estudos/01-matematica/22-sistemas-equacoes-lineares.html — seção 08 + Questões 2 e 8 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A ESCADA: o sistema escalonado é uma escada; comece pelo degrau de baixo (uma incógnita só) e suba substituindo.
#   AS PESAGENS EM DUPLA: cada pessoa subiu na balança DUAS vezes; some tudo e divida por 2.
#   TOTAL MENOS A DUPLA: cada um é o total menos a dupla em que ele não está.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (todos conferidos em Python):
#   Escada (material): x + y + z = 6 · y + z = 5 · z = 3 → z = 3, y = 2, x = 1 (conferência 1 + 2 + 3 = 6).
#   Atalho da escada (nosso, verde): x = 6 − 5 = 1 direto, porque y + z já é 5.
#   Combos (material): A + B = 13 · B + C = 15 · A + C = 14 → 2(A + B + C) = 42 → 21 → C = 8, A = 6, B = 7.
#   Nós fazemos (prompt): 9, 11, 10 → soma 30 → total 15 → A = 4, B = 5, C = 6 (conferência 4 + 5 = 9).
# Erros clássicos com números nossos (para não resolver as questões antes da hora):
#   1. esquecer de dividir por 2: combos, total 42 → C = 42 − 13 = 29, mais que B + C = 15 (absurdo).
#   2. dividir uma dupla por 2: combos, A + B = 13 → 6,5 e 6,5; mas A = 6 e B = 7.
#   3. responder o intermediário: na escada, perguntam y e a pessoa responde 5 (o y + z do degrau do meio); y = 2.
# QUESTÃO 2 (eu faço, texto idêntico): 125 + 145 + 140 = 410 → 205 → B = 205 − 140 = 65 (C). Ana 60, Caio 80;
#   conferência 60 + 65 = 125. Erradas (do material): A = massa de Ana · E = massa de Caio · B 125 ÷ 2 · D 145 ÷ 2.
# QUESTÃO 8 (você faz, texto idêntico): f + m + d = 20 · f + 2m + 3d = 37 · m = d + 2 → (2ª − 1ª) m + 2d = 17 →
#   3d + 2 = 17 → d = 5, m = 7 (B), f = 8; conferência 20 questões e 37 pontos. Erradas (do material): A 5 = difíceis ·
#   C 8 = fáceis · D 15 = pontos das difíceis · E 17 = intermediário m + 2d.
# Acréscimos nossos (verde): o atalho da escada (subtrair o degrau de baixo do de cima) e o "contar quantas vezes cada
#   letra aparece" antes de somar. Escalonamento geral 3 × 3, classificação 3 × 3 e Sarrus: só citados (série de
#   Determinantes).
# Frases-chave (meio e fim, idênticas): 1. Sistema escalonado: resolva de baixo para cima. 2. Em duplas, cada um aparece
#   duas vezes: some e divida por 2. 3. Cada um é o total menos a dupla em que ele não está.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Sistema com 3 incógnitas: a escada e o atalho da soma · Matemática ENEM, Sistemas episódio 4"

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
        "{a}Ana e Beto, [p=0.2] *cento e vinte e cinco quilos.* [p=0.3] {b}Beto e Caio, [p=0.2] *cento e quarenta e "
        "cinco.* [p=0.3] {c}Ana e Caio, [p=0.2] *cento e quarenta.* [p=0.5] {d}Muita gente divide cento e vinte e cinco "
        "por dois [p=0.2] e diz que Beto pesa *sessenta e dois e meio.* [p=0.4] {e}Ele pesa *sessenta e cinco.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai resolver sistemas com *três incógnitas* [p=0.3] {b}pela *escada* [p=0.2] e pelo "
        "*atalho da soma.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio um, [p=0.2] a *substituição:* [p=0.2] se x mais y é dez "
        "[p=0.2] e y é três, [p=0.2] troque o y por três, [p=0.2] e *x é sete.* [p=0.4] {b}Do episódio dois, [p=0.2] "
        "*subtrair uma equação da outra:* [p=0.2] o que é igual nas duas [p=0.2] *some.*"),

    # ================= CONCRETO: A BALANÇA =================
    dict(id="04", block="balanca", text=
        "{t}Imagine três amigos numa *balança de farmácia.* [p=0.3] {a}Eles sobem *em duplas,* [p=0.2] e anotam três "
        "números. [p=0.4] {b}Ninguém subiu sozinho. [p=0.2] Então como descobrir *quanto pesa cada um?* [p=0.4] {c}São "
        "*três* valores escondidos. [p=0.2] Vamos precisar de *três* pistas."),

    # ================= BLOCO A: TRÊS EQUAÇÕES =================
    dict(id="05", block="tres", text=
        "{t}Quantas equações bastam? [p=0.4] {a}Um *sistema três por três* [p=0.2] tem três equações [p=0.2] e três "
        "incógnitas. [p=0.4] {b}E as equações precisam ser *independentes:* [p=0.2] cada uma traz uma informação *nova,* "
        "[p=0.2] e não é cópia nem mistura das outras. [p=0.4] {c}Com duas pistas para três números, [p=0.2] *sobra "
        "dúvida.*"),

    # ================= BLOCO B: A ESCADA =================
    dict(id="06", block="escada", text=
        "{t}Existe um sistema fácil de três incógnitas? [p=0.4] {a}Existe. [p=0.2] Olhe este: [p=0.2] x mais y mais z "
        "igual a seis; [p=0.2] y mais z igual a cinco; [p=0.2] z igual a três. [p=0.4] {b}Cada linha tem *uma letra a "
        "menos.* [p=0.3] É um *sistema escalonado:* [p=0.2] parece uma *escada.* [p=0.4] {c}E *escalonar* [p=0.2] é "
        "justamente arrumar um sistema nesse formato."),
    dict(id="07", block="escada", text=
        "{t}Por onde começar? [p=0.3] {a}Pelo *degrau de baixo,* [p=0.2] que tem uma letra só: [p=0.2] *z igual a três.* "
        "[p=0.4] {b}Suba um degrau [p=0.2] e substitua: [p=0.2] y mais três igual a cinco, [p=0.2] *y igual a dois.* "
        "[p=0.4] {c}Suba mais um: [p=0.2] x mais dois mais três igual a seis, [p=0.2] *x igual a um.* [p=0.4] {d}Isso é "
        "a *substituição de baixo para cima.* [p=0.2] Confira: [p=0.2] um mais dois mais três, [p=0.2] *seis.*"),
    dict(id="08", block="atalho_escada", text=
        "{t}Um atalho na escada. [p=0.3] {a}Repare: [p=0.2] o degrau de cima é x *mais* y mais z. [p=0.2] E o do meio "
        "[p=0.2] já diz que *y mais z* é cinco. [p=0.4] {b}Então subtraia: [p=0.2] seis menos cinco. [p=0.2] *x é um,* "
        "[p=0.2] sem nem achar o y."),

    # ================= BLOCO C: O ATALHO DA SOMA =================
    dict(id="09", block="soma", text=
        "{t}E quando o sistema *não* é uma escada? [p=0.4] {a}Numa lanchonete, [p=0.2] os combos de dois lanches custam: "
        "[p=0.2] A mais B, *treze reais;* [p=0.2] B mais C, *quinze;* [p=0.2] A mais C, *catorze.* [p=0.4] {b}Some as "
        "três [p=0.2] e *conte* quantas vezes cada letra aparece. [p=0.3] {c}A: [p=0.2] *duas vezes.* [p=0.2] B: [p=0.2] "
        "*duas vezes.* [p=0.2] C: [p=0.2] *duas vezes.* [p=0.4] {d}Então treze mais quinze mais catorze, [p=0.2] "
        "*quarenta e dois,* [p=0.2] é *duas vezes* A mais B mais C. [p=0.3] Dividindo por dois: [p=0.2] *vinte e um.*"),

    # ================= BLOCO D: TOTAL MENOS A DUPLA =================
    dict(id="10", block="regra", text=
        "{t}E agora, cada um? [p=0.4] {a}O C é o total [p=0.2] menos a dupla *em que ele não está.* [p=0.2] Vinte e um "
        "menos treze: [p=0.2] *C igual a oito.* [p=0.4] {b}O A: [p=0.2] vinte e um menos quinze, [p=0.2] *seis.* [p=0.4] "
        "{c}O B: [p=0.2] vinte e um menos catorze, [p=0.2] *sete.* [p=0.4] {d}Confira com uma dupla: [p=0.2] seis mais "
        "sete, [p=0.2] *treze.* [p=0.2] Bate."),
    dict(id="11", block="atalho_soma", text=
        "{t}O atalho inteiro [p=0.2] em três passos. [p=0.3] {a}Um: [p=0.2] *some* as três duplas. [p=0.3] {b}Dois: "
        "[p=0.2] *divida por dois,* [p=0.2] porque cada um apareceu duas vezes. [p=0.3] {c}Três: [p=0.2] tire do total "
        "[p=0.2] *a dupla que não tem* quem você procura."),

    # ================= BLOCO E: QUANDO USAR =================
    dict(id="12", block="quando", text=
        "{t}Quando esse atalho funciona? [p=0.4] {a}Quando *cada incógnita aparece o mesmo número de vezes.* [p=0.4] {b}É "
        "o caso das *pesagens em dupla,* [p=0.2] dos *combos* de lanchonete [p=0.2] e das *distâncias entre três "
        "cidades.* [p=0.4] {c}Para os outros sistemas três por três, [p=0.2] existe o escalonamento completo, [p=0.2] que "
        "fica para a série de *Determinantes.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="13", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}A mais B, *nove.* [p=0.2] B mais C, *onze.* [p=0.2] A mais C, *dez.* [p=0.4] {b}Quanto "
        "vale cada um? [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="14", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Some: [p=0.2] nove mais onze mais dez, [p=0.2] *trinta.* [p=0.2] Cada letra apareceu "
        "duas vezes: [p=0.2] divida por dois, [p=0.2] *total quinze.* [p=0.4] {b}A é quinze menos onze, [p=0.2] *quatro.* "
        "[p=0.2] B é quinze menos dez, [p=0.2] *cinco.* [p=0.2] C é quinze menos nove, [p=0.2] *seis.* [p=0.4] {c}Confira: "
        "[p=0.2] quatro mais cinco, [p=0.2] *nove.* [p=0.2] Bate."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="15", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] sistema escalonado: [p=0.2] resolva de baixo para cima. "
        "[p=0.5] {b}Dois: [p=0.2] em duplas, cada um aparece duas vezes: [p=0.2] some e divida por dois. [p=0.5] {c}Três: "
        "[p=0.2] cada um é o total menos a dupla em que ele não está."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="16", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] somar as três duplas [p=0.2] e *esquecer de "
        "dividir por dois.* [p=0.2] Nos combos, [p=0.2] o C daria quarenta e dois menos treze, [p=0.2] *vinte e nove.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a soma foi feita direitinho. [p=0.4] {c}Mas sozinho o C custaria mais "
        "[p=0.2] que o combo B mais C, de quinze. [p=0.2] Absurdo. [p=0.2] *Cada um apareceu duas vezes:* [p=0.2] divida "
        "por dois."),
    dict(id="17", block="erros", text=
        "{a}Segundo: [p=0.2] dividir *uma dupla* por dois. [p=0.2] A mais B é treze, [p=0.2] então cada um custaria *seis "
        "e cinquenta.* [p=0.4] {b}Parece certo, [p=0.2] porque são dois lanches [p=0.2] e treze reais. [p=0.4] {c}Mas "
        "isso supõe que os dois *custam o mesmo.* [p=0.2] Ninguém disse isso. [p=0.2] O A custa *seis* [p=0.2] e o B, "
        "*sete.*"),
    dict(id="18", block="erros", text=
        "{a}Terceiro: [p=0.2] responder um *resultado do meio do caminho.* [p=0.2] Na escada, [p=0.2] perguntam o y, "
        "[p=0.2] e a pessoa responde *cinco,* [p=0.2] o y mais z do degrau do meio. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o cinco é o número que está na tela. [p=0.4] {c}Mas cinco é y *mais* z. [p=0.2] O y é *dois.* [p=0.2] "
        "Antes de marcar, [p=0.2] *releia a pergunta.*"),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="19", block="q2", text=
        "{t}Questão do ENEM, [p=0.2] do nosso material: [p=0.2] a balança do começo. [p=0.2] Eu resolvo. [p=0.4] {a}Três "
        "amigos, [p=0.2] Ana, Beto e Caio, [p=0.2] subiram em duplas numa balança. [p=0.3] Ana e Beto juntos marcaram "
        "*cento e vinte e cinco quilos;* [p=0.2] Beto e Caio, *cento e quarenta e cinco;* [p=0.2] Ana e Caio, *cento e "
        "quarenta.* [p=0.3] A massa de Beto, em quilogramas, é: [p=0.4] {qa}A: sessenta. [p=0.2] {qb}B: sessenta e dois "
        "vírgula cinco. [p=0.2] {qc}C: sessenta e cinco. [p=0.2] {qd}D: setenta e dois vírgula cinco. [p=0.2] {qe}E: "
        "oitenta. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="20", block="q2", text=
        "{t}*Pesagens em dupla:* [p=0.2] atalho da soma. [p=0.4] {a}Cento e vinte e cinco mais cento e quarenta e cinco "
        "mais cento e quarenta: [p=0.2] *quatrocentos e dez.* [p=0.2] Cada um subiu duas vezes: [p=0.2] divida por dois, "
        "[p=0.2] *total duzentos e cinco.* [p=0.4] {b}Beto é o total menos a dupla em que ele *não* está: [p=0.2] Ana e "
        "Caio. [p=0.2] Duzentos e cinco menos cento e quarenta: [p=0.2] *sessenta e cinco.* [p=0.4] {c}Ana fica com "
        "sessenta, [p=0.2] Caio com oitenta. [p=0.2] Confira: [p=0.2] sessenta mais sessenta e cinco, [p=0.2] *cento e "
        "vinte e cinco.* [p=0.3] {ok}*Letra C!*"),
    dict(id="21", block="q2", text=
        "{t}E as erradas? [p=0.3] {xa}A A é a massa da *Ana,* [p=0.2] não a do Beto. [p=0.4] {xe}A E é a massa do *Caio.* "
        "[p=0.4] {xb}A B dividiu cento e vinte e cinco por dois, [p=0.2] {xd}e a D dividiu cento e quarenta e cinco por "
        "dois: [p=0.3] as duas supõem que os dois da dupla *pesam o mesmo.*"),

    # ================= QUESTÃO 8 (VOCÊ FAZ) =================
    dict(id="22", block="q8", text=
        "{t}Agora é com você. [p=0.4] {a}Uma prova tem *vinte questões:* [p=0.2] as fáceis valem um ponto, [p=0.2] as "
        "médias valem dois [p=0.2] e as difíceis valem três, [p=0.2] num total de *trinta e sete pontos.* [p=0.3] O "
        "número de questões médias é *dois a mais* que o de difíceis. [p=0.3] O número de questões *médias* é: [p=0.4] "
        "{qa}A: cinco. [p=0.2] {qb}B: sete. [p=0.2] {qc}C: oito. [p=0.2] {qd}D: quinze. [p=0.2] {qe}E: dezessete. "
        "[p=0.4] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="23", block="q8", text=
        "{t}Etiquetas: [p=0.2] f fáceis, [p=0.2] m médias, [p=0.2] d difíceis. [p=0.2] Uma equação por informação. "
        "[p=0.4] {a}*f mais m mais d* igual a vinte. [p=0.2] *f mais dois m mais três d* igual a trinta e sete. [p=0.2] E "
        "*m igual a d mais dois.* [p=0.4] {b}Subtraia a primeira da segunda [p=0.2] e conte: [p=0.2] o f *some,* [p=0.2] "
        "sobra *um* m [p=0.2] e *dois* d. [p=0.2] *m mais dois d igual a dezessete.* [p=0.4] {c}Troque o m por d mais "
        "dois: [p=0.2] três d mais dois igual a dezessete, [p=0.2] *d igual a cinco.* [p=0.2] Então *m é sete* [p=0.2] e "
        "f é oito. [p=0.4] {d}Confira: [p=0.2] oito mais sete mais cinco, *vinte;* [p=0.2] oito mais catorze mais quinze, "
        "*trinta e sete.* [p=0.3] {ok}*Letra B!*"),
    dict(id="24", block="q8", text=
        "{t}E as erradas? [p=0.3] {xa}A A é o número de *difíceis.* [p=0.3] {xc}A C, o de *fáceis.* [p=0.3] {xd}A D são "
        "os *pontos* das difíceis: [p=0.2] cinco vezes três. [p=0.3] {xe}E a E é o *meio do caminho:* [p=0.2] m mais "
        "dois d, [p=0.2] o terceiro erro clássico."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="25", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] sistema escalonado: [p=0.2] resolva de baixo para "
        "cima. [p=0.5] {b}Dois: [p=0.2] em duplas, cada um aparece duas vezes: [p=0.2] some e divida por dois. [p=0.5] "
        "{c}Três: [p=0.2] cada um é o total menos a dupla em que ele não está."),

    # ================= PONTE E CTA =================
    dict(id="26", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as pegadinhas [p=0.3] {c}e vemos "
        "sistemas *na Física,* [p=0.2] *na Química* [p=0.2] e *na Geometria.*"),
    dict(id="27", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha dividido uma pesagem em dupla por dois? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
