# Roteiro — Progressão Geométrica, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/32-progressao-geometrica-soma-infinita.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9; as Q1 e Q2 também não, porque repetem a série de Função Exponencial). As 5 questões são
#   INÉDITAS. Matrizes: só a ponte.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois delas, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 A MÁQUINA ×q · O EXPOENTE É QUANTAS VEZES A MÁQUINA AGE · NA PA DIVIDE, NA PG TIRA A RAIZ (ícone: máquina ×q) ·
#   ep2 A PG É A PA COM A SOMA TROCADA POR MULTIPLICAÇÃO · x/q, x, x·q · AS PARCELAS QUE DESLIZAM E SE CANCELAM
#       (ícone: árvore da corrente) ·
#   ep3 METADE DO QUE SOBROU · A FÓRMULA COM FREIO (|q| < 1) · A BOLA CAI UMA VEZ E DEPOIS FAZ TUDO DUAS VEZES
#       (ícone: bola quicando) ·
#   ep4 O FATOR É O QUE SOBRA · CONTE OS PERÍODOS ANTES DA CONTA (ícone: carro com a etiqueta de preço caindo; o ep. 4 foi
#       feito em paralelo: as analogias vêm do prompt do vídeo 4).
# Prática de recuperação: a cena 04 abre com uma pergunta e pausa antes do índice; cada V/F e cada questão têm pausa.
# O que a prova cobra (seção 01): crescimento por fator · decaimento · soma finita · soma infinita. O que mais rende:
#   contar os períodos e reconhecer a soma infinita.
# Onde aparece (seção 10): Química (meia-vida: ÷ 2) · Biologia (mitose, 2ⁿ; pirâmide de energia, razão ≈ 0,1) ·
#   Financeira (montantes, razão 1 + i) · Física (+10 dB multiplica a intensidade por 10: níveis em PA, intensidades em PG).
# Estratégia (seção 09): 3 hábitos — contar os períodos (exemplo do material: meia-vida de 8 h em 2 dias → 6) · termo,
#   soma finita ou soma infinita? · usar as potências que o enunciado dá (2¹⁰ = 1 024).
# V/F (os 9 erros da seção 11, NA ORDEM do material). DESVIO NOSSO (marcado): para o jogo não ter resposta previsível,
#   três frases aparecem na versão CERTA (verdadeiras: 3, 6 e 8); as outras seis são o erro (falsas). Números NOSSOS
#   (fora das Q1–Q9 e das questões dos eps. 1 a 4; conferidos em trabalho/conferir_questoes.py):
#   1 F a₁ = 3, q = 2: a₆ = 3 · 2⁶ = 192 (certo 3 · 2⁵ = 96) · 2 F razão de (90, 30, 10) = −60 (é 1/3) ·
#   3 V triplica 4 vezes: 100 · 3⁴ = 8 100 (não 100 · 3 · 4) · 4 F 8% ao ano: q = 0,08 (é 1,08) ·
#   5 F S∞ de 30 + 10 + 10/3 + … = 30 ÷ (1/3) = 90 (certo 30 ÷ (2/3) = 45) · 6 V 1 + 3 + 9 + … não tem soma infinita ·
#   7 F bola de 5 m que sobe metade: total = 5 ÷ (1/2) = 10 m (certo 5 + 2 · 5 = 15 m) ·
#   8 V corrente 4, 16, 64: total em 3 dias = 84, não 4³ · 9 F 0,4545… = 45/100 (certo 45/99 = 5/11).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; a ordem das letras é nossa):
#   Q1 medicamento 320 mg, meia-vida 6 h, após 1 dia: 24 ÷ 6 = 4 meias-vidas → 320 · (1/2)⁴ = 20 mg → B.
#      A 10 (uma a mais) · C 40 (uma a menos) · D 80 (320 ÷ 4) · E 160 (uma meia-vida só). (números do prompt)
#   Q2 grupo: 2 na 1ª semana, cada um convida 2 na semana seguinte; total ao fim da 5ª semana:
#      2 + 4 + 8 + 16 + 32 = 62 → D. A 32 (só a 5ª semana) · B 10 (linear) · C 64 (2⁶) · E 126 (seis semanas). (prompt)
#   Q3 DESVIO DO PROMPT (marcado): o prompt pede a bola de 9 m que sobe 2/3 (45 m), mas o ep. 3 desta série JÁ usou
#      exatamente essa bola no bloco f e no erro 3 (27 em vez de 45). Para a questão ser inédita de verdade, usamos uma
#      bola NOSSA, com os mesmos erros clássicos: solta de 10 m, sobe 3/5 da altura anterior. Descidas 10 ÷ (2/5) = 25;
#      subidas 6 ÷ (2/5) = 15; total 10 + 2 · 15 = 40 m → A. B 25 (só descidas) · C 15 (só subidas) · D 30 (dobra as
#      subidas e esquece a queda inicial) · E 50 (dobra as descidas, contando a queda inicial duas vezes).
#      A queda inicial é contada UMA vez (o "verifique" do prompt, agora com 40 m).
#   Q4 tabela 600, 540, 486, 437,4 nos anos 0 a 3: quociente 0,9 → V = 600 · 0,9ⁿ → E. A 600 − 60n (dá 480 no ano 2) ·
#      B 600 · 0,1ⁿ (taxa no lugar do fator) · C 600 · 0,9n (dá 0 no ano 0) · D 540 · 0,9ⁿ (começa no valor errado).
#   Q5 0,3636… = 0,36 + 0,0036 + …: a₁ = 0,36, q = 0,01 → 0,36 ÷ 0,99 = 36/99 = 4/11 → C. A 36/100 (truncou) ·
#      B 36/90 = 2/5 · D 36/999 = 4/111 (três noves para dois algarismos) · E 1/3 (uma aproximação). (prompt)
# Gabaritos: B, D, A, E, C.
# Atalhos (verde): os 3 hábitos (cenas 08 e 09) · "períodos = tempo ÷ meia-vida" na Q1 · "próximo termo menos o
#   primeiro, ÷ (q − 1)" na Q2 (do ep. 2) · "total = h · (1 + q) ÷ (1 − q)" na Q3 (do ep. 3) · "o fator é o que sobra:
#   540 ÷ 600" na Q4 · "noves = 1 − q" na Q5 (do ep. 3).
# Checklist (seção 13) → episódio (como o prompt pede): razão, fator 1 ± i, termo geral e tabela PA × PG → ep1 ·
#   b² = ac, três termos e soma finita → ep2 · soma infinita, dízimas e bola → ep3 · meia-vida, juros, depreciação → ep4.
# Meta (prompt e material): 30 questões, 21 acertos (70%), com pelo menos oito de soma infinita ou de decaimento.
# Ponte (do usuário): Matrizes e operações.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de progressão geométrica: remédio, corrente e bola quicando · Matemática ENEM, PG ep. 5"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, passo a passo. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}Bactérias, [p=0.2] remédios, [p=0.2] dinheiro, [p=0.2] uma bola quicando: [p=0.3] {b}o ENEM usa a PG para "
        "tudo que *cresce ou diminui por um fator fixo.* [p=0.4] {c}Hoje você treina para reconhecer qual das três "
        "perguntas ele está fazendo: [p=0.3] *termo,* [p=0.2] *soma* [p=0.2] ou *soma infinita.* [p=0.5] {d}São nove "
        "frases de verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Crescimento por fator:* [p=0.2] bactérias que dobram, [p=0.2] mensagens "
        "repassadas. [p=0.3] {b}*Decaimento:* [p=0.2] meia-vida, [p=0.2] depreciação, [p=0.2] a bola que perde altura. "
        "[p=0.3] {c}*Soma finita:* [p=0.2] o total de uma corrente. [p=0.3] {d}E *soma infinita:* [p=0.2] a distância "
        "da bola até parar, [p=0.2] e as dízimas."),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.3] Duas habilidades. [p=0.4] {a}Primeiro, [p=0.2] *contar os períodos:* [p=0.2] "
        "dobra a cada vinte minutos, durante duas horas, [p=0.2] são *seis multiplicações* por dois. [p=0.4] "
        "{b}Segundo, [p=0.2] *reconhecer a soma infinita:* [p=0.2] com a razão entre menos um e um, [p=0.2] as parcelas "
        "encolhem, [p=0.2] e a soma vira *a um sobre um menos q.*"),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] tente lembrar: [p=0.2] do primeiro ao sexto termo, [p=0.2] *quantas vezes a "
        "máquina age?* [p=1.2] {a}Um: [p=0.2] a PG é uma *máquina de multiplicar por q.* [p=0.2] Do primeiro ao sexto, "
        "*cinco vezes.* [p=0.2] E, para achar a razão, [p=0.2] na PA se divide; [p=0.2] *na PG se tira a raiz.* [p=0.4] "
        "{b}Dois: [p=0.2] a PG é a PA *com a soma trocada por multiplicação.* [p=0.2] Três termos viram *xis sobre q, xis "
        "e xis vezes q,* [p=0.2] e na soma *as parcelas deslizam e se cancelam.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] *metade do que sobrou.* [p=0.2] Infinitas parcelas, um número finito, [p=0.2] mas só "
        "*com freio.* [p=0.2] E a bola *cai uma vez* [p=0.2] e depois faz tudo *duas "
        "vezes.* [p=0.4] {b}Quatro: [p=0.2] a PG *disfarçada.* [p=0.2] O fator é *o que sobra:* [p=0.2] quem perde vinte "
        "por cento fica com oitenta. [p=0.2] E *conte os períodos* antes de qualquer conta."),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}Na *Química,* [p=0.2] a cada meia-vida, [p=0.2] a massa do isótopo *se divide "
        "por dois.* [p=0.3] {b}Na *Biologia,* [p=0.2] cada célula origina duas: [p=0.2] *dois elevado a ene* depois de "
        "ene ciclos. [p=0.2] E na pirâmide de energia, [p=0.2] só uns dez por cento passam: [p=0.2] razão *zero vírgula "
        "um.*"),
    dict(id="07", block="onde", text=
        "{c}Na *Matemática Financeira,* [p=0.2] os montantes de juros compostos [p=0.2] formam uma PG de razão *um mais "
        "i.* [p=0.3] {d}E na *Física,* [p=0.2] cada mais dez decibéis *multiplica a intensidade por dez:* [p=0.2] os "
        "níveis andam em PA, [p=0.2] as intensidades, *em PG.*"),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Três hábitos. [p=0.4] {a}Um: [p=0.2] *conte os períodos com calma.* [p=0.2] "
        "Meia-vida de oito horas, em dois dias: [p=0.2] {a2}converta para horas, [p=0.2] quarenta e oito, [p=0.2] e "
        "divida por oito: [p=0.2] *seis meias-vidas.* [p=0.2] O expoente é quantas vezes o fator age."),
    dict(id="09", block="habitos", text=
        "{b}Dois: [p=0.2] *termo, soma ou soma infinita?* [p=0.2] \"No fim\" é termo; [p=0.2] \"ao todo\" é soma; "
        "[p=0.2] \"até parar\" é soma infinita. [p=0.4] {c}Três: [p=0.2] *use as potências que o enunciado dá.* [p=0.2] "
        "Se ele deu dois elevado a dez igual a mil e vinte e quatro, [p=0.2] monte a conta para esse número aparecer."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] numa PG que começa em três, com razão dois, [p=0.2] o sexto termo é *três vezes dois elevado a "
        "seis,* [p=0.2] cento e noventa e dois. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o seis da "
        "posição parece ser o expoente. [p=0.3] {g}Mas do primeiro ao sexto termo, [p=0.2] a máquina age *cinco vezes:* "
        "[p=0.2] três vezes trinta e dois, *noventa e seis.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] a razão de *noventa, trinta e dez* [p=0.2] é *menos sessenta.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque, na PA, a razão é mesmo a diferença. [p=0.3] {g}Mas na PG a razão é *o "
        "quociente:* [p=0.2] trinta dividido por noventa, [p=0.2] *um terço.*"),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] cem bactérias que *triplicam quatro vezes* [p=0.2] viram *cem vezes três elevado a quatro,* "
        "[p=0.2] oito mil e cem. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade de "
        "fazer cem vezes três vezes quatro. [p=0.3] {g}Mas fator repetido *é potência,* [p=0.2] não produto pelo número "
        "de vezes."),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] uma cidade que cresce *oito por cento ao ano* [p=0.2] tem razão *zero vírgula zero oito.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o oito por cento está escrito ali. [p=0.3] "
        "{g}Mas a razão é *o fator:* [p=0.2] tudo o que havia, mais oito por cento. [p=0.2] *Um vírgula zero oito.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] a soma infinita de *trinta, mais dez, mais dez terços...* [p=0.2] é trinta dividido por um "
        "terço, [p=0.2] *noventa.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece que é só dividir pela razão. [p=0.3] {g}Mas o denominador é *um menos q:* [p=0.2] trinta dividido por "
        "dois terços, [p=0.2] *quarenta e cinco.*"),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] *um, mais três, mais nove, mais vinte e sete...* [p=0.2] não tem soma infinita. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque existe uma fórmula pronta para a soma "
        "infinita. [p=0.3] {g}Mas a fórmula só funciona *com freio.* [p=0.2] Com razão três, [p=0.2] a soma "
        "*nunca para de crescer.*"),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] uma bola solta de *cinco metros* sobe sempre *metade* da altura anterior. [p=0.2] A distância "
        "total é *cinco dividido por meio:* [p=0.2] dez metros. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque a fórmula parece resolver tudo. [p=0.3] {g}Mas isso são *só as descidas.* [p=0.2] "
        "Depois da primeira queda, [p=0.2] cada altura é percorrida *duas vezes:* [p=0.2] *quinze metros.*"),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] numa corrente com *quatro, dezesseis e sessenta e quatro* pessoas por dia, [p=0.2] o total em "
        "três dias *não é* quatro elevado a três. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso "
        "porque o quatro elevado a três está bem ali. [p=0.3] {g}Mas ele é *só o último dia.* [p=0.2] O total é a soma: "
        "[p=0.2] *oitenta e quatro.*"),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] *zero vírgula quarenta e cinco, quarenta e cinco...* [p=0.2] é igual a *quarenta e cinco "
        "centésimos.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque começa mesmo com "
        "quarenta e cinco. [p=0.3] {g}Mas a dízima é *uma soma infinita,* [p=0.2] não um corte: [p=0.2] quarenta e "
        "cinco sobre *noventa e nove,* [p=0.2] *cinco onze avos.*"),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *escreva o fator,* [p=0.2] *conte os períodos* [p=0.2] e decida "
        "*termo, soma ou soma infinita.*"),

    # ================= QUESTÃO 1: MEIA-VIDA =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Um paciente tem *trezentos e vinte miligramas* de um remédio no sangue. [p=0.2] A "
        "meia-vida do remédio é de *seis horas.* [p=0.3] {b}Quanto resta *depois de um dia?* [p=0.4] {la}A, [p=0.2] dez "
        "miligramas. [p=0.2] {lb}B, [p=0.2] vinte. [p=0.2] {lc}C, [p=0.2] quarenta. [p=0.2] {ld}D, [p=0.2] oitenta. "
        "[p=0.2] {le}E, [p=0.2] cento e sessenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}O fator é *meio.* [p=0.2] E os períodos: [p=0.2] um dia tem vinte e quatro horas; [p=0.2] dividido por seis, "
        "[p=0.2] *quatro meias-vidas.* [p=0.3] {a}Trezentos e vinte, [p=0.2] cento e sessenta, [p=0.2] oitenta, [p=0.2] "
        "quarenta, [p=0.2] *vinte.* [p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A contou *uma meia-vida a mais,* [p=0.2] {xc}e "
        "a C, *uma a menos.* [p=0.2] {xd}A D dividiu por quatro. [p=0.2] {xe}E a E "
        "parou na *primeira* meia-vida."),

    # ================= QUESTÃO 2: SOMA FINITA =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Na primeira semana, *duas pessoas* entram num grupo. [p=0.2] Cada pessoa que entra "
        "convida *duas novas* na semana seguinte. [p=0.3] {b}Quantas pessoas entraram *ao todo* até o fim da *quinta "
        "semana?* [p=0.4] {la}A, [p=0.2] trinta e duas. [p=0.2] {lb}B, [p=0.2] dez. [p=0.2] {lc}C, [p=0.2] sessenta e "
        "quatro. [p=0.2] {ld}D, [p=0.2] sessenta e duas. [p=0.2] {le}E, [p=0.2] cento e vinte e seis. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}*Ao todo:* é soma finita. [p=0.2] Fator dois, [p=0.2] cinco semanas. [p=0.3] {a}Dois, quatro, oito, "
        "dezesseis, trinta e dois: [p=0.2] somando, *sessenta e dois.* [p=0.2] {v}Pelo atalho do episódio dois: "
        "[p=0.2] o próximo termo, sessenta e quatro, [p=0.2] menos o primeiro, dois. [p=0.2] {ok}*Letra D!* [p=0.4] "
        "{xa}A A respondeu *só a quinta semana.* [p=0.2] {xb}A B pensou "
        "*linear.* [p=0.2] {xc}A C fez dois elevado a seis, [p=0.2] {xe}e a E somou *seis semanas.*"),

    # ================= QUESTÃO 3: A BOLA =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Uma bola é solta de *dez metros* de altura. [p=0.2] A cada quique, sobe *três "
        "quintos* da altura anterior. [p=0.3] {b}Qual é a distância total percorrida *até parar?* [p=0.4] {la}A, "
        "[p=0.2] quarenta metros. [p=0.2] {lb}B, [p=0.2] vinte e cinco. [p=0.2] {lc}C, [p=0.2] quinze. [p=0.2] {ld}D, "
        "[p=0.2] trinta. [p=0.2] {le}E, [p=0.2] cinquenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}*Até parar:* soma infinita. [p=0.2] Razão três quintos: [p=0.2] tem freio. [p=0.3] {a}As descidas: [p=0.2] "
        "dez dividido por dois quintos, [p=0.2] *vinte e cinco.* [p=0.2] As subidas começam em seis: [p=0.2] seis "
        "dividido por dois quintos, [p=0.2] *quinze.* [p=0.2] Total, *quarenta metros.* [p=0.2] {ok}*Letra A!* [p=0.4] "
        "{xb}A B ficou *só nas descidas,* [p=0.2] {xc}e a C, só nas subidas. [p=0.2] {xd}A D dobrou as subidas [p=0.2] e "
        "*esqueceu a primeira queda.* [p=0.2] {xe}E a E dobrou as descidas, [p=0.2] contando a queda inicial *duas "
        "vezes.*"),

    # ================= QUESTÃO 4: A TABELA =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Uma tabela mostra o valor de um equipamento: [p=0.2] *seiscentos, quinhentos e "
        "quarenta, quatrocentos e oitenta e seis* [p=0.2] e *quatrocentos e trinta e sete vírgula quatro,* [p=0.2] nos "
        "anos zero a três. [p=0.3] {b}Qual é o modelo? [p=0.4] {la}A, [p=0.2] seiscentos menos sessenta ene. [p=0.2] "
        "{lb}B, [p=0.2] seiscentos vezes zero vírgula um elevado a ene. [p=0.2] {lc}C, [p=0.2] seiscentos vezes zero "
        "vírgula nove ene. [p=0.2] {ld}D, [p=0.2] quinhentos e quarenta vezes zero vírgula nove elevado a ene. [p=0.2] "
        "{le}E, [p=0.2] seiscentos vezes zero vírgula nove elevado a ene. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Divida um valor pelo anterior: [p=0.2] quinhentos e quarenta sobre seiscentos, [p=0.2] *zero vírgula "
        "nove.* [p=0.2] O quociente é sempre o mesmo: [p=0.2] é PG. [p=0.3] {a}O fator é o que sobra: [p=0.2] perde dez "
        "por cento, [p=0.2] fica com noventa. [p=0.2] E no ano zero vale *seiscentos.* [p=0.2] {ok}*Letra E!* [p=0.4] "
        "{xa}A A é uma PA: [p=0.2] no ano dois daria *quatrocentos e oitenta.* [p=0.2] {xb}A B usou *a taxa no lugar do "
        "fator.* [p=0.2] {xc}A C dá *zero* no ano zero, [p=0.2] {xd}e a D começa no valor errado."),

    # ================= QUESTÃO 5: A DÍZIMA =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}A dízima *zero vírgula trinta e seis, trinta e seis...* [p=0.2] pode ser "
        "vista como uma soma infinita. [p=0.3] {b}Qual fração ela representa? [p=0.4] {la}A, [p=0.2] trinta e seis "
        "centésimos. [p=0.2] {lb}B, [p=0.2] dois quintos. [p=0.2] {lc}C, [p=0.2] quatro onze avos. [p=0.2] {ld}D, "
        "[p=0.2] quatro sobre cento e onze. [p=0.2] {le}E, [p=0.2] um terço. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Zero vírgula trinta e seis, [p=0.2] mais zero vírgula zero zero trinta e seis, [p=0.2] e assim por diante. "
        "[p=0.2] Primeiro termo, *zero vírgula trinta e seis;* [p=0.2] razão, *um centésimo.* [p=0.3] {a}Um menos q "
        "[p=0.2] é zero vírgula noventa e nove: [p=0.2] *trinta e seis sobre noventa e nove,* [p=0.2] *quatro onze "
        "avos.* [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A *cortou a dízima.* [p=0.2] {xb}A B dividiu por noventa, [p=0.2] "
        "{xd}a D usou *três noves* para dois algarismos, [p=0.2] {xe}e a E é só *um valor parecido.*"),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}Razão, fator um mais ou menos i, termo geral [p=0.2] e a tabela PA contra PG: "
        "[p=0.2] episódio um. [p=0.3] {c}Bê ao quadrado igual a a vezes c, [p=0.2] três termos e soma finita: [p=0.2] "
        "episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Soma infinita, dízimas e a bola: [p=0.2] episódio três. [p=0.3] {b}Meia-vida, juros e depreciação: "
        "[p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma.* [p=0.4] {c}E "
        "pelo menos *oito* delas de soma infinita [p=0.2] ou de decaimento: [p=0.2] meia-vida, [p=0.2] quiques."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Matrizes e operações,* [p=0.2] que abre a parte de álgebra linear: [p=0.3] {b}tabelas "
        "de números *com endereço,* [p=0.3] {c}e uma multiplicação feita *linha por coluna.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de progressão geométrica está "
        "completa. [p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
