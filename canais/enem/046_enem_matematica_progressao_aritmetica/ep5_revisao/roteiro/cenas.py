# Roteiro — Progressão Aritmética, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/31-progressao-aritmetica.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9). As 5 questões são INÉDITAS (números e erros do prompt do usuário).
#   Progressão geométrica: só a ponte (e o aviso do V/F 7).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o "n − 1" é falado "ene menos um"; o gancho só acrescenta, depois delas,
#   o que a aula vai ter). Na narração, "PA" vai escrito "pê-á" (o script de voz local não aplica a tabela de pronúncia).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 A ESCADA DE DEGRAUS IGUAIS · DO 1º AO 12º DEGRAU, 11 SALTOS · TESTE COM n = 1 (ícone: escada) ·
#   ep2 POSTES E INTERVALOS · O "+ 1" CONTA O PRIMEIRO · x − r, x, x + r (ícone: fila de postes) ·
#   ep3 O TRUQUE DE GAUSS · AS DUAS ESCADAS FORMAM UM RETÂNGULO · SOMA = TERMOS × MÉDIA (ícone: pares de Gauss) ·
#   ep4 O TERMO ZERO DOS JUROS SIMPLES · A SEMANA É UMA PA DE RAZÃO 7 (ícone: extrato bancário).
# Prática de recuperação: a cena 04 abre com uma pergunta e pausa antes do índice; cada V/F e cada questão têm pausa.
# O que a prova cobra (seção 01): padrões de figuras · termo distante · soma de muitos termos · contagem. O que mais
#   rende: o "n − 1" e a soma pela média.
# Onde aparece (seção 10): Financeira (montantes de juros simples, razão C · i) · Física (velocidades no MUV; distâncias
#   1, 3, 5, 7… em segundos sucessivos a partir do repouso) · Química (séries homólogas: +CH₂, +14 u) · Geografia (cerca
#   de 6,5 °C a menos a cada 1 000 m).
# Estratégia (seção 09): 3 hábitos — escrever os três primeiros termos · termo ou soma? · média na soma
#   ((8, 11, 14, 17, 20) = 5 · 14 = 70, exemplo do material).
# V/F (os 9 erros da seção 11, NA ORDEM do material). DESVIO NOSSO (marcado): para o jogo não ter resposta previsível,
#   três frases aparecem na versão CERTA (verdadeiras: 3, 5 e 8); as outras seis são o erro (falsas). Números NOSSOS
#   (fora das Q1–Q9 e das questões dos eps. 1 a 4; conferidos em trabalho/conferir_questoes.py):
#   1 F a₁ = 6, r = 4: a₁₀ = 6 + 10 · 4 = 46 (certo 6 + 9 · 4 = 42) · 2 F soma de (5, 9, …, 41), 10 termos = 10 · 46 = 460
#   (certo 230) · 3 V R$ 20 e +R$ 5 por mês: "no 6º mês" é o termo (45), "em 6 meses" é a soma · 4 F razão de
#   (50, 43, 36) = 7 (é −7) · 5 V múltiplos de 6 de 102 a 498: (498 − 102) ÷ 6 + 1 = 67 · 6 F 3 meios entre 2 e 18:
#   r = 16 ÷ 3 (5 termos, 4 saltos: r = 4) · 7 F (3, 6, 12, 24) é PA (é PG: as diferenças 3, 6, 12 mudam) · 8 V fila de
#   quadrados de palitos: 3n + 1 (4, 7, 10) · 9 F R$ 500 a 2% ao mês: mês 6 = 500 + 5 · 10 (certo 500 + 6 · 10 = 560).
# QUESTÕES INÉDITAS (números e erros do prompt; conferidas em trabalho/conferir_questoes.py: uma única correta; a ordem
#   das letras é nossa):
#   Q1 triângulos de palitos (3 palitos, +2): a_n = 2n + 1 → figura 40 = 81 → C. A 79 (39 triângulos: 2 · 39 + 1) ·
#      B 80 (esquece o palito inicial: 2 · 40) · D 83 (40 saltos: 3 + 40 · 2) · E 120 (três por triângulo).
#   Q2 poupança R$ 30 e +R$ 10 por mês, total em 10 meses: a₁₀ = 120; S = (30 + 120) · 10 ÷ 2 = R$ 750 → A.
#      B R$ 120 (só o 10º depósito) · C R$ 300 (30 · 10, sem os aumentos) · D R$ 800 (a₁₀ = 130, 10 saltos) ·
#      E R$ 1.500 (sem dividir por 2).
#   Q3 postes a cada 40 m em 1 km, com poste nas duas pontas: 25 intervalos + 1 = 26 postes → E. B 25 (contou os
#      intervalos). Explicações NOSSAS (o prompt só lista os valores): A 24 (tirou um, achando que uma ponta não conta) ·
#      C 27 (somou um poste a mais em cada ponta) · D 40 (respondeu o espaçamento, em metros).
#   Q4 4 meios entre 10 e 35: 6 termos, 5 saltos, r = 25 ÷ 5 = 5 → (10, 15, 20, 25, 30, 35) → B. C 6,25 (dividiu por 4,
#      os meios) · A ≈ 4,17 (dividiu por 6, os termos) · E 25 (esqueceu de dividir). Explicação NOSSA da D 7 (o prompt só
#      dá o valor): dividiu o 35 pelos 5 saltos, sem tirar o 10 do começo.
#   Q5 PA de 15 termos com o 8º (o do meio) = 12: soma = 15 · 12 = 180 → D. A 90 (dividiu por 2 sem necessidade) ·
#      B 168 (14 termos) · C 192 (16 termos) · E 360 (soma dos extremos 24, sem dividir por 2: 15 · 24).
# Gabaritos: C, A, E, B, D.
# Atalhos (verde): os 3 hábitos (cenas 08 e 09) · "conte os saltos com o dedo" na Q1 · "soma = termos × média" na Q2
#   e na Q5 · "intervalos + 1" na Q3 · "meios + 2 = termos; termos − 1 = saltos" na Q4.
# Checklist (seção 13) → episódio (como o prompt pede): razão, termo geral, figuras e PA como afim → ep1 · média dos
#   vizinhos, três termos, interpolação e contagem → ep2 · soma, equidistantes (e termo × soma) → ep3 · juros simples,
#   calendário e treinos → ep4.
# Meta (prompt e material): 30 questões, 21 acertos (70%), com pelo menos dez de contexto.
# Ponte (do usuário): Progressão geométrica e soma dos infinitos termos.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de progressão aritmética: palitos, poupança e postes | PA Ep. 5"
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
        "{a}O nome *\"progressão aritmética\"* pode nem aparecer na prova. [p=0.4] {b}O que aparece é *palito de "
        "fósforo,* [p=0.2] *fileira de teatro,* [p=0.2] *depósito que aumenta todo mês.* [p=0.4] {c}E quase todo "
        "distrator é feito de um único erro: [p=0.3] *o ene menos um.* [p=0.5] {d}Hoje: [p=0.2] nove frases de "
        "verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Padrões de figuras:* [p=0.2] palitos ou bolinhas que crescem; [p=0.2] "
        "pede-se a figura cinquenta. [p=0.3] {b}*Um termo distante:* [p=0.2] quanto no décimo segundo mês. [p=0.3] "
        "{c}*A soma de muitos termos:* [p=0.2] as cadeiras de um teatro. [p=0.3] {d}E *contagem:* [p=0.2] quantos "
        "postes, [p=0.2] quantos múltiplos de sete."),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.3] Duas habilidades. [p=0.4] {a}Primeiro, [p=0.2] *o ene menos um:* [p=0.2] do "
        "primeiro ao décimo segundo termo, [p=0.2] são *onze saltos,* não doze. [p=0.4] {b}Segundo, [p=0.2] *a soma "
        "pela média:* [p=0.2] número de termos [p=0.2] vezes primeiro mais último, [p=0.2] dividido por dois."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] tente lembrar: [p=0.2] do primeiro ao vigésimo termo, [p=0.2] *quantos saltos?* "
        "[p=1.2] {a}Um: [p=0.2] a pê-á é uma *escada de degraus iguais.* [p=0.2] Do primeiro ao vigésimo, *dezenove "
        "saltos.* [p=0.2] E toda fórmula se *testa com ene igual a um.* [p=0.4] {b}Dois: [p=0.2] *postes e "
        "intervalos.* [p=0.2] O *mais um* conta o primeiro, [p=0.2] e três termos viram *xis menos erre, xis e xis "
        "mais erre.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] o *truque de Gauss.* [p=0.2] Duas escadas encaixadas formam *um retângulo,* [p=0.2] por isso "
        "a soma divide por dois: [p=0.2] *termos vezes a média.* [p=0.4] {b}Quatro: [p=0.2] a pê-á *disfarçada.* "
        "[p=0.2] Nos juros simples, o capital é o *termo zero,* o chão. [p=0.2] E a *semana é uma pê-á de razão "
        "sete.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}Na *Matemática Financeira,* [p=0.2] os montantes de juros simples [p=0.2] "
        "sobem sempre *o mesmo juro.* [p=0.3] {b}Na *Física,* [p=0.2] no movimento acelerado, [p=0.2] as velocidades "
        "formam pê-á; [p=0.2] e, partindo do repouso, [p=0.2] as distâncias de cada segundo seguem *um, três, cinco, "
        "sete.*"),
    dict(id="07", block="onde", text=
        "{c}Na *Química,* [p=0.2] cada carbono a mais numa série [p=0.2] acrescenta *cê agá dois:* [p=0.2] catorze "
        "unidades de massa. [p=0.3] {d}E na *Geografia,* [p=0.2] a temperatura cai cerca de *seis vírgula cinco "
        "graus* [p=0.2] a cada mil metros de altitude: [p=0.2] uma pê-á *decrescente.*"),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Três hábitos. [p=0.4] {a}Um: [p=0.2] *escreva os três primeiros termos.* "
        "[p=0.2] Antes de qualquer fórmula. [p=0.2] {a2}Eles confirmam que é pê-á, [p=0.2] dão a razão [p=0.2] e servem "
        "para *testar* a fórmula que você montar."),
    dict(id="09", block="habitos", text=
        "{b}Dois: [p=0.2] *termo ou soma?* [p=0.2] \"No décimo segundo mês\" é termo; [p=0.2] \"em doze meses\" é soma. "
        "[p=0.2] Sublinhe a palavra que decide. [p=0.4] {c}Três: [p=0.2] *use a média na soma.* [p=0.2] Oito, onze, "
        "catorze, dezessete e vinte: [p=0.2] o do meio é catorze, [p=0.2] e a soma é *cinco vezes catorze, setenta.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] numa pê-á que começa em seis, com razão quatro, [p=0.2] o décimo termo é *seis mais dez vezes "
        "quatro,* [p=0.2] quarenta e seis. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o dez da "
        "posição parece ser o número de saltos. [p=0.3] {g}Mas do primeiro ao décimo degrau [p=0.2] são *nove "
        "saltos:* [p=0.2] seis mais trinta e seis, *quarenta e dois.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] a soma de cinco, nove, treze, até quarenta e um, [p=0.2] com dez termos, [p=0.2] é *dez vezes "
        "quarenta e seis,* [p=0.2] quatrocentos e sessenta. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque juntar o primeiro com o último parece a conta inteira. [p=0.3] {g}Mas as duas escadas formam um "
        "retângulo: [p=0.2] *divida por dois.* [p=0.2] Duzentos e trinta."),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] quem deposita vinte reais no primeiro mês [p=0.2] e cinco a mais por mês: [p=0.2] *no sexto "
        "mês* pede o termo; [p=0.2] *em seis meses* pede a soma. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] "
        "{e}Parece falso porque as duas frases quase não mudam. [p=0.3] {g}Mas \"no\" é *um depósito,* quarenta e "
        "cinco reais; [p=0.2] \"em\" é *o total.*"),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] a razão de *cinquenta, quarenta e três, trinta e seis* [p=0.2] é *sete.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a distância entre os números é mesmo sete. [p=0.3] {g}Mas razão é "
        "*segundo menos primeiro:* [p=0.2] quarenta e três menos cinquenta, [p=0.2] *menos sete.* [p=0.2] A escada "
        "desce."),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] de cento e dois a quatrocentos e noventa e oito, [p=0.2] os múltiplos de seis são *a "
        "diferença dividida por seis, mais um:* [p=0.2] sessenta e sete. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* "
        "[p=0.3] {e}Parece falso porque o *mais um* parece sobrar. [p=0.3] {g}Mas a divisão conta os *intervalos,* "
        "[p=0.2] e o mais um conta o *primeiro poste.*"),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] para pôr três meios aritméticos entre dois e dezoito, [p=0.2] a razão é *dezesseis dividido "
        "por três.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque são três números novos. [p=0.3] "
        "{g}Mas três meios mais os dois extremos dão *cinco termos* [p=0.2] e *quatro saltos:* [p=0.2] razão quatro. "
        "[p=0.2] Dois, seis, dez, catorze, dezoito."),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] *três, seis, doze, vinte e quatro* [p=0.2] é uma pê-á. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque a sequência cresce bem certinha. [p=0.3] {g}Mas as diferenças são três, "
        "seis, doze: [p=0.2] *não são iguais.* [p=0.2] Aqui cada termo *dobra:* [p=0.2] é uma pê-gê, [p=0.2] o assunto "
        "do próximo material."),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] numa fila de quadrados feitos de palitos, [p=0.2] a figura ene tem *três ene mais um* "
        "palitos. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque cada quadrado tem quatro "
        "lados. [p=0.3] {g}Mas quadrados vizinhos *dividem um lado.* [p=0.2] Teste com ene igual a um: [p=0.2] "
        "*quatro;* [p=0.2] depois sete, depois dez."),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] quinhentos reais a dois por cento ao mês, em juros simples: [p=0.2] o montante do sexto "
        "mês [p=0.2] é *quinhentos mais cinco vezes dez.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque o ene menos um virou costume. [p=0.3] {g}Mas o capital é o *termo zero,* o chão: [p=0.2] no sexto mês "
        "já subiram *seis degraus.* [p=0.2] Quinhentos e sessenta."),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *escreva os primeiros termos,* [p=0.2] decida *termo ou soma* "
        "[p=0.2] e só então faça a conta."),

    # ================= QUESTÃO 1: PALITOS =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma fila de triângulos é feita com palitos. [p=0.2] A figura um tem *três palitos,* "
        "[p=0.2] e cada triângulo novo acrescenta *dois.* [p=0.3] {b}Quantos palitos tem a *figura quarenta?* [p=0.4] "
        "{la}A, [p=0.2] setenta e nove. [p=0.2] {lb}B, [p=0.2] oitenta. [p=0.2] {lc}C, [p=0.2] oitenta e um. [p=0.2] "
        "{ld}D, [p=0.2] oitenta e três. [p=0.2] {le}E, [p=0.2] cento e vinte. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Os três primeiros: [p=0.2] *três, cinco, sete.* [p=0.2] Razão dois. [p=0.3] {a}Da figura um à quarenta, "
        "[p=0.2] *trinta e nove saltos:* [p=0.2] três mais setenta e oito, [p=0.2] *oitenta e um.* [p=0.2] {v}Ou "
        "dois ene mais um; [p=0.2] teste com ene igual a um: [p=0.2] três. [p=0.2] {ok}*Letra C!* [p=0.4] {xd}A D deu "
        "*quarenta saltos.* [p=0.2] {xa}A A contou trinta e nove triângulos. [p=0.2] {xb}A B esqueceu o *palito "
        "inicial,* [p=0.2] {xe}e a E deu três palitos a cada triângulo, [p=0.2] como se eles não dividissem lado."),

    # ================= QUESTÃO 2: TERMO OU SOMA =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma pessoa deposita *trinta reais* no primeiro mês [p=0.2] e, a cada mês, *dez "
        "reais a mais.* [p=0.3] {b}Quanto ela terá depositado *ao todo em dez meses?* [p=0.4] {la}A, [p=0.2] "
        "setecentos e cinquenta reais. [p=0.2] {lb}B, [p=0.2] cento e vinte. [p=0.2] {lc}C, [p=0.2] trezentos. "
        "[p=0.2] {ld}D, [p=0.2] oitocentos. [p=0.2] {le}E, [p=0.2] mil e quinhentos. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}*Ao todo:* é soma. [p=0.2] Trinta, quarenta, cinquenta... [p=0.3] {a}O décimo depósito: [p=0.2] trinta mais "
        "*nove* vezes dez, [p=0.2] *cento e vinte.* [p=0.2] A soma: [p=0.2] trinta mais cento e vinte, [p=0.2] vezes "
        "dez, [p=0.2] dividido por dois: [p=0.2] *setecentos e cinquenta.* [p=0.2] {ok}*Letra A!* [p=0.4] {xb}A B "
        "respondeu *só o décimo depósito.* [p=0.2] {xe}A E esqueceu de *dividir por dois.* [p=0.2] {xd}A D usou *dez "
        "saltos* [p=0.2] {xc}e a C esqueceu os aumentos."),

    # ================= QUESTÃO 3: POSTES =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Ao longo de *um quilômetro* de estrada, [p=0.2] serão instalados postes *a cada "
        "quarenta metros,* [p=0.2] com um poste em cada ponta. [p=0.3] {b}Quantos postes serão instalados? [p=0.4] "
        "{la}A, [p=0.2] vinte e quatro. [p=0.2] {lb}B, [p=0.2] vinte e cinco. [p=0.2] {lc}C, [p=0.2] vinte e sete. "
        "[p=0.2] {ld}D, [p=0.2] quarenta. [p=0.2] {le}E, [p=0.2] vinte e seis. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Um quilômetro é mil metros. [p=0.2] Mil dividido por quarenta: [p=0.2] *vinte e cinco intervalos.* "
        "[p=0.3] {a}Mas postes são *intervalos mais um:* [p=0.2] o mais um conta o *primeiro poste.* [p=0.2] *Vinte e "
        "seis.* [p=0.2] {ok}*Letra E!* [p=0.4] {xb}A B contou os *intervalos.* [p=0.2] {xa}A A tirou um, [p=0.2] como "
        "se uma ponta não contasse. [p=0.2] {xc}A C pôs um poste a mais em cada ponta, [p=0.2] {xd}e a D respondeu o "
        "*espaçamento,* em metros."),

    # ================= QUESTÃO 4: MEIOS ARITMÉTICOS =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Entre *dez* e *trinta e cinco* [p=0.2] serão colocados *quatro meios "
        "aritméticos.* [p=0.3] {b}Qual é a razão dessa pê-á? [p=0.4] {la}A, [p=0.2] cerca de quatro vírgula dezessete. "
        "[p=0.2] {lb}B, [p=0.2] cinco. [p=0.2] {lc}C, [p=0.2] seis vírgula vinte e cinco. [p=0.2] {ld}D, [p=0.2] sete. "
        "[p=0.2] {le}E, [p=0.2] vinte e cinco. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Quatro meios *mais os dois extremos:* [p=0.2] *seis termos.* [p=0.2] E seis termos têm *cinco saltos.* "
        "[p=0.3] {a}A distância é trinta e cinco menos dez, [p=0.2] vinte e cinco; [p=0.2] dividida por cinco, [p=0.2] "
        "*razão cinco.* [p=0.2] {v}Dez, quinze, vinte, vinte e cinco, trinta, trinta e cinco. [p=0.2] {ok}*Letra B!* "
        "[p=0.4] {xc}A C dividiu pelos *quatro meios.* [p=0.2] {xa}A A dividiu pelos *seis termos.* [p=0.2] {xe}A E "
        "esqueceu de dividir, [p=0.2] {xd}e a D dividiu o trinta e cinco [p=0.2] *sem tirar o dez* do começo."),

    # ================= QUESTÃO 5: SOMA PELO TERMO DO MEIO =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Uma pê-á tem *quinze termos,* [p=0.2] e o *oitavo,* o do meio, [p=0.2] vale "
        "*doze.* [p=0.3] {b}Qual é a soma dos quinze termos? [p=0.4] {la}A, [p=0.2] noventa. [p=0.2] {lb}B, [p=0.2] "
        "cento e sessenta e oito. [p=0.2] {lc}C, [p=0.2] cento e noventa e dois. [p=0.2] {ld}D, [p=0.2] cento e "
        "oitenta. [p=0.2] {le}E, [p=0.2] trezentos e sessenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Com quantidade ímpar de termos, [p=0.2] o do meio *já é a média.* [p=0.3] {a}Soma igual a termos vezes "
        "média: [p=0.2] quinze vezes doze, [p=0.2] *cento e oitenta.* [p=0.2] Nem precisa da razão. [p=0.2] "
        "{ok}*Letra D!* [p=0.4] {xa}A A dividiu por dois *sem necessidade:* [p=0.2] o doze já é a média. [p=0.2] "
        "{xb}A B e {xc}a C usaram catorze e dezesseis termos. [p=0.2] {xe}E a E somou os extremos, [p=0.2] vinte e "
        "quatro, [p=0.2] e *esqueceu de dividir por dois.*"),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}Razão, termo geral, figuras [p=0.2] e a pê-á como função afim: [p=0.2] "
        "episódio um. [p=0.3] {c}Média dos vizinhos, três termos, meios [p=0.2] e contagem: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}A soma de Gauss, os termos equidistantes [p=0.2] e *termo ou soma:* [p=0.2] episódio três. [p=0.3] "
        "{b}Juros simples, calendário e treinos: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] "
        "reveja o episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma.* [p=0.4] {c}E "
        "pelo menos *dez* delas de contexto: [p=0.2] padrões, [p=0.2] cotidiano [p=0.2] e contagem."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Progressão geométrica e soma dos infinitos termos:* [p=0.3] {b}o crescimento deixa de "
        "ser *por soma* [p=0.3] {c}e passa a ser *por multiplicação.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de progressão aritmética está "
        "completa. [p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
