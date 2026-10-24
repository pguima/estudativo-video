# Roteiro — Números Complexos, Episódio 3 de 5: o plano de Argand-Gauss — módulo, distância e o giro de 90°
# Base: Estudos/Enem/estudos/01-matematica/36-numeros-complexos.html — seção 06 + quadro "Giros prontos" da seção 08
#   + Questões 4 e 5 (seção 12). Forma trigonométrica e "multiplicar soma os ângulos" ficam para o episódio 4.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O ENDEREÇO NO MAPA: a parte real anda para o lado, a parte imaginária anda para cima.
#   A DIAGONAL DO RETÂNGULO: o módulo é a distância em linha reta até a origem, por Pitágoras.
#   A MANIVELA: multiplicar por i gira 90° no sentido anti-horário; (a, b) vira (−b, a) e a distância não muda.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: par ordenado; Pitágoras em uma frase ("terá série própria"); i² = −1 e z · z̄ = a² + b² (eps. 1 e 2).
# Exemplos dos blocos = os NOVOS do prompt: 3 + 4i (afixo e módulo), de 2 + i até 8 + 9i (distância 10), i(4 + i) =
#   −1 + 4i (giro, módulo √17). O exemplo i(3 + 2i) da seção 08 é a Q5 ("você faz") e NÃO aparece antes da pausa.
#   A Q4 é o próprio gancho e é "eu faço" (repetir é ok).
# Erro 2 com exemplo NOSSO: 3 + 4i → conjugado 3 − 4i (espelho no eixo real) × oposto −3 − 4i (giro de 180°).
# Acréscimos NOSSOS (marcados): cena verde de ATALHO "distância em dois passos: subtraia, depois Pitágoras; procure o
#   3, 4, 5 e seus múltiplos" e cena verde "giro por i sem conta: troque as partes de lugar e mude o sinal da que foi
#   para a frente".
# Nós fazemos (prompt): |−5 + 12i| = √(25 + 144) = 13; i(2 + 5i) = 2i + 5i² = −5 + 2i.
# QUESTÃO 4 (eu faço): |(4 + 6i) − (1 + 2i)| = |3 + 4i| = 5 (B). Erradas = material: A √5 = |1 + 2i| (o ponto de
#   partida); D √52 = |4 + 6i| (como se saísse do canto); C 7 soma as partes; E 25 esquece a raiz. CUIDADO: A e D são
#   raízes (√5 e √52), não "5" e "52".
# QUESTÃO 5 (você faz): i(3 + 2i) = 3i + 2i² = −2 + 3i (D), do 1º para o 2º quadrante, módulo √13. Erradas = material:
#   A 2 − 3i = giro horário (× −i); B −3 − 2i = giro de 180° (× −1); C 3 − 2i = conjugado; E 2 + 3i troca as partes
#   sem o sinal (reflexão na reta y = x, não é giro).
# Frases-chave (meio e fim, idênticas): 1. Todo complexo é um ponto: real para o lado, imaginária para cima.
#   2. Módulo é Pitágoras; distância é o módulo da diferença. 3. Vezes i gira 90° anti-horário: (a, b) vira (−b, a).
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "O plano dos números complexos: módulo, distância e o giro de 90° · Matemática ENEM, Complexos episódio 3"

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
        "{a}Um robô sai de *um mais dois i* [p=0.2] e vai em linha reta [p=0.2] até *quatro mais seis i.* [p=0.4] "
        "{b}Andou *sete* metros? [p=0.4] {c}Não: [p=0.2] *cinco.* [p=0.4] {d}É o velho triângulo *três, quatro, cinco* "
        "[p=0.2] escondido dentro de dois números complexos."),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Números complexos.* [p=0.4] {a}Ao final, [p=0.2] você vai pôr "
        "*qualquer complexo no plano,* [p=0.3] {b}*medir distâncias* [p=0.3] {c}e *girar pontos noventa graus* [p=0.2] "
        "com uma multiplicação."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes. [p=0.3] {a}*Par ordenado:* [p=0.2] primeiro o *x,* [p=0.2] depois o *y.* [p=0.4] "
        "{b}*Pitágoras,* [p=0.2] no triângulo retângulo: [p=0.2] hipotenusa ao quadrado [p=0.2] é a soma dos quadrados "
        "dos catetos. [p=0.2] Terá série própria. [p=0.4] "
        "{c}E dos episódios um e dois: [p=0.2] *i ao quadrado é menos um,* [p=0.2] e z vezes o conjugado [p=0.2] dá *a "
        "ao quadrado mais b ao quadrado.*"),

    # ================= CONCRETO =================
    dict(id="04", block="galpao", text=
        "{t}Imagine a planta de um galpão, [p=0.2] toda *quadriculada.* [p=0.4] {a}Um robô anda *três metros para a "
        "direita* [p=0.2] e *quatro para cima.* [p=0.4] {b}E num programa de desenho [p=0.2] que *gira* figuras. "
        "[p=0.4] {c}Os dois fazem contas [p=0.2] *com números complexos.*"),

    # ================= BLOCO A: O AFIXO =================
    dict(id="05", block="afixo", text=
        "{t}Onde fica um número complexo? [p=0.4] {a}No *plano de Argand-Gauss:* [p=0.2] um plano cartesiano em que "
        "cada complexo [p=0.2] vira um *ponto.* [p=0.4] {b}*Eixo real:* [p=0.2] o horizontal. [p=0.2] *Eixo "
        "imaginário:* [p=0.2] o vertical. [p=0.4] {c}*Afixo:* [p=0.2] o ponto que representa o complexo. [p=0.2] A "
        "mais b i [p=0.2] é o ponto *a, b.* [p=0.4] {d}Três mais quatro i: [p=0.2] *três para o lado, quatro para "
        "cima.* [p=0.3] É um *endereço no mapa.*"),

    # ================= BLOCO B: O MÓDULO =================
    dict(id="06", block="modulo", text=
        "{t}A que distância esse ponto está da origem? [p=0.4] {a}*Módulo:* [p=0.2] a distância em linha reta [p=0.2] "
        "até a origem. [p=0.4] {b}É a *diagonal do retângulo.* [p=0.2] Catetos três e quatro. [p=0.4] {c}Pitágoras: "
        "[p=0.2] nove mais dezesseis, [p=0.2] vinte e cinco; [p=0.2] raiz de vinte e cinco, [p=0.2] *cinco.* [p=0.4] "
        "{d}E repare: [p=0.2] z vezes o conjugado [p=0.2] dá vinte e cinco: [p=0.2] *o módulo ao quadrado.*"),

    # ================= BLOCO C: O QUE CADA OPERAÇÃO FAZ =================
    dict(id="07", block="operacoes", text=
        "{t}E as contas, [p=0.2] o que fazem no desenho? [p=0.4] {a}O *conjugado* [p=0.2] é uma *reflexão* no eixo "
        "real: [p=0.2] a imagem no espelho. [p=0.4] {b}O *oposto,* [p=0.2] menos z, [p=0.2] é um *giro de cento e "
        "oitenta graus.* [p=0.4] {c}E a *soma* [p=0.2] é uma "
        "*translação:* [p=0.2] arrastar o ponto [p=0.2] sem girar."),
    dict(id="08", block="distancia", text=
        "{t}E a distância entre *dois* pontos? [p=0.4] {a}É o *módulo da diferença.* [p=0.4] {b}De dois mais i [p=0.2] "
        "até oito mais nove i: [p=0.2] a diferença é *seis mais oito i.* [p=0.4] {c}Trinta e seis mais sessenta e "
        "quatro, [p=0.2] cem; [p=0.2] raiz de cem: [p=0.2] *dez.*"),
    dict(id="09", block="atalho_dist", text=
        "{t}Atalho. [p=0.4] {a}Distância em *dois passos:* [p=0.2] *subtraia,* [p=0.2] depois *Pitágoras.* [p=0.4] "
        "{b}E fique de olho no *três, quatro, cinco* [p=0.2] e nos seus múltiplos: [p=0.2] seis, oito, dez."),

    # ================= BLOCO D: O GIRO DE 90° =================
    dict(id="10", block="giro", text=
        "{t}E multiplicar por i, [p=0.2] o que faz? [p=0.4] {a}*Rotação:* [p=0.2] girar em volta da origem. [p=0.2] "
        "*Anti-horário:* [p=0.2] contra os ponteiros do relógio. [p=0.4] {b}Pegue quatro mais i. [p=0.2] "
        "Vezes i: [p=0.2] quatro i, [p=0.2] mais i ao quadrado. [p=0.4] {c}I ao quadrado é menos um: [p=0.2] *menos "
        "um mais quatro i.* [p=0.4] {d}O ponto quatro, um [p=0.2] foi para *menos um, quatro.* [p=0.3] É uma "
        "*manivela* girando noventa graus. [p=0.4] {e}Distância até a origem: [p=0.2] *raiz de dezessete,* [p=0.2] "
        "antes e depois."),

    # ================= BLOCO E: OS GIROS PRONTOS =================
    dict(id="11", block="giros", text=
        "{t}Guarde os giros prontos. [p=0.4] {a}Vezes i: [p=0.2] noventa graus anti-horário; [p=0.2] *a, b vira menos "
        "b, a.* [p=0.4] {b}Vezes menos um: [p=0.2] *cento e oitenta graus.* [p=0.4] {c}Vezes menos i: [p=0.2] noventa "
        "graus *horário,* [p=0.2] o sentido dos ponteiros; [p=0.2] a, b vira *b, menos a.* [p=0.4] {d}Nenhum muda o "
        "módulo, [p=0.2] porque o módulo de i [p=0.2] é *um.*"),
    dict(id="12", block="atalho_giro", text=
        "{t}Atalho. [p=0.4] {a}Giro por i *sem conta:* [p=0.2] *troque as partes de lugar* [p=0.4] {b}e *mude o sinal* "
        "da que foi para a frente. [p=0.4] {c}Quatro, um: [p=0.2] troca, [p=0.2] um, quatro; [p=0.2] muda o sinal da "
        "frente: [p=0.2] *menos um, quatro.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="13", block="exercicio", text=
        "{t}Sua vez, [p=0.2] duas perguntas. [p=0.3] {a}Qual é o módulo de *menos cinco mais doze i?* [p=0.4] {b}E onde "
        "vai parar *dois mais cinco i* [p=0.2] depois de um giro de noventa graus anti-horário? [p=0.4] {c}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="14", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Vinte e cinco mais cento e quarenta e quatro: [p=0.2] cento e sessenta e nove. "
        "[p=0.2] Raiz: [p=0.2] *treze.* [p=0.4] {b}Agora, [p=0.2] i vezes dois mais cinco i: [p=0.2] dois i, [p=0.2] "
        "mais cinco i ao quadrado: [p=0.3] {c}*menos cinco mais dois i.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="15", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] todo complexo é um ponto: [p=0.2] real para o lado, "
        "[p=0.2] imaginária para cima. [p=0.5] {b}Dois: [p=0.2] módulo é Pitágoras; [p=0.2] distância é o módulo da "
        "diferença. [p=0.5] {c}Três: [p=0.2] vezes i gira noventa graus anti-horário: [p=0.2] a, b vira menos b, a."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="16", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.4] {a}Dizer que o módulo de três mais quatro i [p=0.2] é *sete,* [p=0.2] "
        "somando as partes. [p=0.4] {b}Parece certo, [p=0.2] porque o robô *anda* três e *anda* quatro. [p=0.4] {c}Mas "
        "o módulo é a *linha reta:* [p=0.2] a diagonal. [p=0.2] Pitágoras dá *cinco.*"),
    dict(id="17", block="erros", text=
        "{t}Segundo erro. [p=0.3] {a}Confundir *conjugado* com *oposto.* [p=0.4] {b}Parece certo, [p=0.2] porque os "
        "dois *trocam sinais.* [p=0.4] {c}Mas o conjugado de três mais quatro i, [p=0.2] *três menos quatro i,* "
        "[p=0.2] é o espelho no eixo real. [p=0.3] O oposto, [p=0.2] *menos três menos quatro i,* [p=0.2] é o giro "
        "de cento e oitenta."),

    # ================= QUESTÃO 4: EU FAÇO =================
    dict(id="18", block="q4", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {a}Num galpão, [p=0.2] as posições de um robô são "
        "números complexos, [p=0.2] em metros. [p=0.3] Ele sai de *um mais dois i* "
        "[p=0.2] e vai em linha reta até *quatro mais seis i.* [p=0.4] {b}A distância percorrida é: [p=0.3] {qa}A: "
        "raiz de cinco. [p=0.2] {qb}B: cinco. [p=0.2] {qc}C: sete. [p=0.2] {qd}D: raiz de cinquenta e dois. [p=0.2] "
        "{qe}E: vinte e cinco."),
    dict(id="19", block="q4", text=
        "{t}Essa, [p=0.2] *eu faço.* [p=0.4] {a}Desenho os dois pontos. "
        "[p=0.4] {b}Distância é o módulo da diferença: [p=0.2] quatro menos um, [p=0.2] *três;* [p=0.2] seis menos "
        "dois, [p=0.2] *quatro.* [p=0.4] {c}Três mais quatro i: [p=0.2] o triângulo três, quatro, cinco. [p=0.3] "
        "*Cinco metros.* [p=0.3] {ok}*Letra B!*"),
    dict(id="20", block="q4", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A é o módulo do ponto de *partida.* [p=0.4] {xd}A D é o módulo do ponto de "
        "*chegada,* [p=0.2] como se o robô saísse do canto. [p=0.4] {xc}A C *soma* as partes, [p=0.2] três mais "
        "quatro. [p=0.4] {xe}E a E *esquece a raiz.*"),

    # ================= QUESTÃO 5: VOCÊ FAZ =================
    dict(id="21", block="q5", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}Um programa de desenho gira um ponto noventa graus [p=0.2] no "
        "sentido anti-horário, [p=0.2] *multiplicando por i.* [p=0.3] O ponto *três mais dois i,* [p=0.2] depois do "
        "giro, [p=0.2] vira: [p=0.3] {qa}A: dois menos três i. [p=0.2] {qb}B: menos três menos dois i. [p=0.2] "
        "{qc}C: três menos dois i. [p=0.2] {qd}D: menos dois mais três i. [p=0.2] {qe}E: dois mais três i. [p=0.4] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q5", text=
        "{t}Vamos conferir. [p=0.3] {a}I vezes três mais dois i: [p=0.2] três i, [p=0.2] mais dois i ao quadrado: "
        "[p=0.2] *menos dois mais três i.* [p=0.3] {b}Do primeiro para o *segundo quadrante,* [p=0.2] módulo raiz de "
        "treze. [p=0.3] {ok}*Letra D!* [p=0.4] {xa}A A gira no sentido *horário.* [p=0.3] {xb}A B gira *cento e "
        "oitenta.* [p=0.3] {xc}A C é o *conjugado.* [p=0.3] {xe}E a E troca as partes *sem o sinal:* [p=0.2] é um "
        "espelho, [p=0.2] não um giro."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="23", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] todo complexo é um ponto: [p=0.2] real para o "
        "lado, [p=0.2] imaginária para cima. [p=0.5] {b}Dois: [p=0.2] módulo é Pitágoras; [p=0.2] distância é o módulo "
        "da diferença. [p=0.5] {c}Três: [p=0.2] vezes i gira noventa graus anti-horário: [p=0.2] a, b vira menos b, a."),

    # ================= PONTE E CTA =================
    dict(id="24", block="ponte", text=
        "{a}E se, em vez de dizer [p=0.2] *ande um para o lado e um para cima,* [p=0.4] {b}você disser [p=0.2] *ande "
        "raiz de dois na direção de quarenta e cinco graus?* [p=0.4] {c}Com esse endereço, [p=0.2] *um mais i elevado "
        "a oito* [p=0.2] sai de cabeça. [p=0.3] {d}Próximo episódio."),
    dict(id="25", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você teria respondido sete metros no gancho? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
