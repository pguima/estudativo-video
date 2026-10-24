# Roteiro — Determinantes e Sistemas Lineares, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino
#   (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/34-determinantes-sistemas-lineares.html — seções 01, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9). As 5 questões são INÉDITAS (dados, alternativas e motivos das erradas do PROMPT).
#   Área de triângulo por determinante: só citada (série própria na Geometria Analítica).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois delas, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 o TESTE DA CHAVE (det ≠ 0: a inversa existe) · o produto da secundária DE CASACO · o TIME VERDE contra o TIME
#       VERMELHO de Sarrus (ícone: chave) ·
#   ep2 as LINHAS PARENTES zeram o det · os BOTÕES DE VOLUME (k^n) (ícone: botões de volume) ·
#   ep3 a TROCA DE FIGURINHA do D_x · o D principal é o CHÃO DA FRAÇÃO (ícone: figurinha trocada) ·
#   ep4 o SEMÁFORO (verde = uma solução; amarelo = olhe as equações) · equações GÊMEAS e BRIGADAS · a PORTA (0, 0) do
#       homogêneo (ícone: semáforo).
#   Os eps. 3 e 4 estavam em produção em paralelo: as analogias deles vêm do prompt deste vídeo.
# Prática de recuperação: a cena 04 abre com uma pergunta e pausa antes do índice; cada V/F e cada questão têm pausa.
# O que a prova cobra (seção 01): determinante · regra de Cramer · classificação. O que mais rende: D ≠ 0 garante
#   solução única; D = 0 exige olhar as equações (incompatíveis → nenhuma; repetidas → infinitas).
# Onde aparece (seção 10): Geometria Analítica (área e alinhamento de três pontos; só citada) · Química (balanceamento
#   como sistema homogêneo) · Física (malhas de circuitos, leis de Kirchhoff) · Economia (misturas, cestas e combos).
# Estratégia (seção 10): 3 hábitos — procurar a propriedade antes de Sarrus · calcular só o necessário · conferir nas
#   equações originais.
# V/F (os 9 erros da seção 11, NA ORDEM do material). DESVIO NOSSO (marcado, como nas revisões anteriores): para o jogo
#   não ter resposta previsível, três frases aparecem na versão CERTA (verdadeiras: 3, 6 e 8); as outras seis são o
#   erro (falsas). Conferidas em trabalho/conferir_questoes.py:
#   1 F |3 −2; 4 5| = 15 − 8 = 7 (certo 15 − (−8) = 23) · 2 F em Sarrus, subtrai-se só o 1º produto vermelho ·
#   3 V numa 3 × 3 com det A = 2, det(2A) = 16 (2³ · 2) · 4 F D = 0 → impossível (x + y = 2 e 2x + 2y = 4: infinitas) ·
#   5 F achou (1, 1) → solução única (no mesmo sistema, (0, 2) e (3, −1) também servem) · 6 V D_x troca a COLUNA de x
#   pela coluna dos termos independentes · 7 F x = D ÷ D_x (certo D_x ÷ D: em x + y = 5, x − y = 1, D = −2, D_x = −6,
#   x = 3; ao contrário daria 1/3) · 8 V um homogêneo nunca é impossível · 9 F k² = 4 → só k = 2 (k = ±2).
# QUESTÕES INÉDITAS (dados exatos do prompt; conferidas em trabalho/conferir_questoes.py):
#   Q1 det (4 −3 / 2 5) = 20 − (−6) = 26 → C. A 14 (20 − 6) · D −26 (secundária menos principal) · B −14 (os dois erros) ·
#      E 9 (soma a diagonal principal).
#   Q2 ordem 2, det A = 4: det(3A) = 3² · 4 = 36 → C. B 12 (só × 3) · E 108 (3³, como se fosse 3 × 3) · D 64 (4³) ·
#      A 7 (3 + 4).
#   Q3 3c + 2p = 34, 2c + 5p = 30: D = 15 − 4 = 11; D_p = 3·30 − 2·34 = 22; p = 2 → B (R$ 2,00); caderno R$ 10,00;
#      confere 20 + 10 = 30. C 10 (a outra incógnita) · E 22 (D_p sem dividir) · D 11 (o próprio D) · A 0,50 (D ÷ D_p).
#   Q4 2x + y = 4, 6x + ky = 12: D = 2k − 6 = 0 só em k = 3; aí a 2ª é o triplo INTEIRO da 1ª (3 · 4 = 12): gêmeas →
#      infinitas → B. Nenhum k dá impossível (D ≠ 0: solução única; D = 0: gêmeas). A confunde D = 0 com impossível ·
#      C ignora o caso D = 0 · D erra o sinal (k = −3 dá D = −12) · E troca o caso de solução única pelo impossível.
#   Q5 homogêneo x + y = 0, 3x + ky = 0: D = k − 3 = 0 → k = 3 → A (aí (t, −t) resolve). B erra o sinal · C k = 0 dá
#      D = −3 ≠ 0 (só a trivial) · D é justamente o caso de solução única · E esquece que D = 0 libera outras soluções.
# Gabaritos: C, C, B, B, A (letras e alternativas do prompt).
# Atalhos (verde): os 3 hábitos (cenas 08 e 09) · "produto com sinal, entre parênteses" na Q1 · "conte as linhas: k^n"
#   na Q2 · "Cramer só na incógnita pedida" na Q3 · "D = 0? compare as equações" na Q4 · "o homogêneo só pergunta se há
#   outras" na Q5.
# Checklist (seção 13) → episódio (como o prompt pede): 2 × 2, Sarrus, Laplace e inversa → ep1 · propriedades → ep2 ·
#   A · X = B e Cramer → ep3 · classificação, parâmetro e homogêneo → ep4.
# Meta (prompt e material): 25 questões, 18 acertos, com pelo menos seis de classificação ou discussão de sistemas.
# Ponte (do usuário): Polinômios e equações polinomiais.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de determinantes e sistemas: Cramer, D = 0 e as pegadinhas · Matemática ENEM, Determinantes ep. 5"

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
        "{a}No ENEM, [p=0.2] o sistema vem numa história de *ingressos* [p=0.2] ou de *lanchonete.* [p=0.4] {b}O "
        "determinante é o *atalho* para duas perguntas: [p=0.3] {c}*qual é o valor pedido* [p=0.3] {d}e *se existe uma "
        "resposta só.* [p=0.5] {e}Hoje: [p=0.2] nove frases de verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] Três ferramentas. [p=0.3] {a}O *determinante:* [p=0.2] o número que diz se a "
        "matriz tem inversa. [p=0.3] {b}A *regra de Cramer:* [p=0.2] cada incógnita como uma divisão de determinantes. "
        "[p=0.3] {c}E a *classificação:* [p=0.2] uma solução, [p=0.2] infinitas [p=0.2] ou nenhuma."),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.3] {a}*D diferente de zero* [p=0.2] garante *uma solução só.* [p=0.4] {b}*D igual a "
        "zero* [p=0.2] não decide sozinho: [p=0.2] *olhe as equações.* [p=0.3] {c}Se elas brigam, [p=0.2] nenhuma "
        "solução. [p=0.2] {d}Se são repetidas, [p=0.2] infinitas."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] tente lembrar: [p=0.2] no dois por dois, [p=0.2] *o que acontece com o produto da "
        "secundária?* [p=1.2] {a}Um: [p=0.2] o *teste da chave.* [p=0.2] Determinante diferente de zero, [p=0.2] a chave "
        "abre: [p=0.2] existe inversa. [p=0.2] O produto da secundária entra *de casaco,* [p=0.2] com o sinal dele, "
        "[p=0.2] e em Sarrus é o *time verde contra o time vermelho.* [p=0.4] {b}Dois: [p=0.2] as *linhas parentes* "
        "zeram o determinante, [p=0.2] e os *botões de volume:* [p=0.2] a matriz inteira vezes k [p=0.2] gira todos os "
        "botões."),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] a *troca de figurinha.* [p=0.2] No D x, [p=0.2] sai a coluna do x [p=0.2] e entram os termos "
        "independentes. [p=0.2] E o D principal é o *chão da fração.* [p=0.4] {b}Quatro: [p=0.2] o *semáforo.* "
        "[p=0.2] Verde, uma solução; [p=0.2] amarelo, olhe as equações: [p=0.2] *gêmeas* dão infinitas, [p=0.2] "
        "*brigadas* dão nenhuma. [p=0.2] E o homogêneo tem a *porta zero, zero* sempre aberta."),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E nas outras áreas? [p=0.4] {a}Na *Geometria Analítica,* [p=0.2] o determinante dá a área de um triângulo "
        "[p=0.2] e diz se três pontos estão alinhados. [p=0.2] Isso tem série própria. [p=0.3] {b}Na *Química,* "
        "[p=0.2] balancear uma equação [p=0.2] é resolver um *sistema homogêneo.*"),
    dict(id="07", block="onde", text=
        "{c}Na *Física,* [p=0.2] os circuitos com várias malhas [p=0.2] viram sistemas nas correntes. [p=0.3] {d}E na "
        "*Economia,* [p=0.2] misturas, cestas e combos: [p=0.2] cada restrição é uma equação, [p=0.2] e o determinante "
        "diz se os dados bastam."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 10) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Três hábitos. [p=0.4] {a}Um: [p=0.2] *procure a propriedade antes de fazer "
        "Sarrus.* [p=0.2] Linha de zeros, [p=0.2] linhas parentes: [p=0.2] determinante zero na hora. [p=0.4] {b}Dois: "
        "[p=0.2] *calcule só o necessário.* [p=0.2] Pediram o preço de um item? [p=0.2] Cramer só nessa incógnita. "
        "[p=0.2] Pediram quantas soluções? [p=0.2] Nem resolva: [p=0.2] classifique."),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] *confira nas equações originais.* [p=0.2] Substituir leva segundos [p=0.2] e pega quase todo "
        "erro de sinal."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] o determinante de *três, menos dois; quatro, cinco* [p=0.2] é *quinze menos oito,* [p=0.2] "
        "sete. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o oito aparece mesmo na conta. [p=0.3] "
        "{g}Mas o produto entra *de casaco:* [p=0.2] menos dois vezes quatro é *menos oito.* [p=0.2] Quinze menos menos "
        "oito, [p=0.2] *vinte e três.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] em Sarrus, [p=0.2] o sinal de menos vale *só para o primeiro produto* vermelho. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque escrevemos os produtos um atrás do outro. [p=0.3] {g}Mas "
        "é time contra time: [p=0.2] some o placar vermelho inteiro [p=0.2] e subtraia *o bloco todo.*"),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] numa matriz *três por três* com determinante dois, [p=0.2] o determinante de *duas vezes A* "
        "[p=0.2] é *dezesseis.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade "
        "de responder quatro. [p=0.3] {g}Mas são *três botões de volume:* [p=0.2] dois ao cubo, oito, [p=0.2] vezes "
        "dois, [p=0.2] dezesseis."),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] *D igual a zero* [p=0.2] quer dizer *sistema impossível.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o zero parece dizer não tem jeito. [p=0.3] {g}Mas é o amarelo do "
        "semáforo: [p=0.2] em *x mais y igual a dois* [p=0.2] e *dois x mais dois y igual a quatro,* [p=0.2] D é zero "
        "[p=0.2] e as equações são *gêmeas:* [p=0.2] infinitas soluções."),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] nesse mesmo sistema, [p=0.2] você achou *x igual a um e y igual a um.* [p=0.2] Então a "
        "solução é única. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a conta deu certo. [p=0.3] "
        "{g}Mas com D zero, [p=0.2] ela é só *uma entre muitas:* [p=0.2] zero e dois [p=0.2] e três e menos um também "
        "servem."),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] para montar o *D x,* [p=0.2] tire a *coluna do x* [p=0.2] e ponha no lugar a coluna dos "
        "termos independentes. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente "
        "troca a *linha.* [p=0.3] {g}Mas a figurinha trocada é a *coluna:* [p=0.2] a coluna do x sai, [p=0.2] os "
        "resultados entram."),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] pela regra de Cramer, [p=0.2] *x é D dividido por D x.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque os dois determinantes estão ali. [p=0.3] {g}Mas o D principal é o "
        "*chão da fração:* [p=0.2] x é *D x sobre D.* [p=0.2] Em *x mais y igual a cinco* e *x menos y igual a um,* "
        "[p=0.2] dá três. [p=0.2] Ao contrário, daria um terço."),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] um sistema *homogêneo* [p=0.2] nunca é impossível. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque ele pode ter D zero. [p=0.3] {g}Mas a *porta zero, zero* "
        "está sempre aberta: [p=0.2] tudo igual a zero resolve. [p=0.2] A pergunta é só se há *outras* soluções."),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] se *k ao quadrado é quatro,* [p=0.2] então *k é dois.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o dois é a resposta que vem primeiro. [p=0.3] {g}Mas é uma equação do "
        "segundo grau: [p=0.2] *k é dois ou menos dois.*"),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *calcule o D primeiro,* [p=0.2] resolva [p=0.2] e *confira nas "
        "equações.*"),

    # ================= QUESTÃO 1: DETERMINANTE 2 × 2 =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}O determinante da matriz *quatro, menos três; dois, cinco* [p=0.2] é: [p=0.4] "
        "{la}A, [p=0.2] catorze. [p=0.2] {lb}B, [p=0.2] menos catorze. [p=0.2] {lc}C, [p=0.2] vinte e seis. [p=0.2] "
        "{ld}D, [p=0.2] menos vinte e seis. [p=0.2] {le}E, [p=0.2] nove. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Principal menos secundária, [p=0.2] com o produto de casaco. [p=0.3] {a}Quatro vezes cinco, *vinte.* "
        "[p=0.2] Menos três vezes dois, *menos seis.* [p=0.2] Vinte menos menos seis: [p=0.2] *vinte e seis.* [p=0.2] "
        "{ok}*Letra C!* [p=0.4] {xa}A A fez vinte menos seis. [p=0.2] {xd}A D fez a secundária menos a principal, "
        "[p=0.2] {xb}a B juntou os dois erros, [p=0.2] {xe}e a E só somou a diagonal."),

    # ================= QUESTÃO 2: det(kA) =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma matriz A de *ordem dois* [p=0.2] tem determinante *quatro.* [p=0.3] {b}O "
        "determinante de *três A* é: [p=0.4] {la}A, [p=0.2] sete. [p=0.2] {lb}B, [p=0.2] doze. [p=0.2] {lc}C, [p=0.2] "
        "trinta e seis. [p=0.2] {ld}D, [p=0.2] sessenta e quatro. [p=0.2] {le}E, [p=0.2] cento e oito. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Os botões de volume. [p=0.2] *Conte as linhas:* [p=0.2] ordem dois, dois botões. [p=0.3] {a}Três ao "
        "quadrado, *nove,* [p=0.2] vezes quatro: [p=0.2] *trinta e seis.* [p=0.2] {ok}*Letra C!* [p=0.4] {xb}A B girou "
        "*um botão só.* [p=0.2] {xe}A E usou três ao cubo, [p=0.2] como se a matriz fosse três por três. [p=0.2] {xd}A D "
        "elevou o quatro ao cubo, [p=0.2] {xa}e a A somou três mais quatro."),

    # ================= QUESTÃO 3: CRAMER EM CONTEXTO =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}*Três cadernos e duas canetas* custam trinta e quatro reais. [p=0.2] *Dois cadernos "
        "e cinco canetas* custam trinta reais. [p=0.3] {b}O preço de *uma caneta* é: [p=0.4] {la}A, [p=0.2] cinquenta "
        "centavos. [p=0.2] {lb}B, [p=0.2] dois reais. [p=0.2] {lc}C, [p=0.2] dez reais. [p=0.2] {ld}D, [p=0.2] onze "
        "reais. [p=0.2] {le}E, [p=0.2] vinte e dois reais. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Pediram *só a caneta:* [p=0.2] Cramer só nessa incógnita. [p=0.3] {a}D: [p=0.2] três vezes cinco, menos dois "
        "vezes dois, [p=0.2] *onze.* [p=0.2] D p, [p=0.2] trocando a figurinha da coluna da caneta: [p=0.2] três vezes "
        "trinta, menos dois vezes trinta e quatro, [p=0.2] *vinte e dois.* [p=0.2] Vinte e dois sobre onze, [p=0.2] "
        "*dois reais.* [p=0.3] {v}O caderno sai *dez reais,* [p=0.2] e vinte mais dez dá trinta. [p=0.2] {ok}*Letra "
        "B!* [p=0.4] {xc}A C é o caderno. [p=0.2] {xe}A E esqueceu de dividir, [p=0.2] {xd}a D é o próprio D, [p=0.2] "
        "{xa}e a A inverteu a fração."),

    # ================= QUESTÃO 4: DISCUSSÃO COM PARÂMETRO =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Sobre o sistema *dois x mais y igual a quatro* [p=0.2] e *seis x mais k y igual a "
        "doze,* [p=0.2] é correto afirmar que ele: [p=0.4] {la}A, [p=0.2] é impossível para k igual a três. [p=0.2] "
        "{lb}B, [p=0.2] tem infinitas soluções para k igual a três. [p=0.2] {lc}C, [p=0.2] tem solução única para "
        "qualquer k. [p=0.2] {ld}D, [p=0.2] tem infinitas soluções para k igual a menos três. [p=0.2] {le}E, [p=0.2] é "
        "impossível para todo k diferente de três. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}D primeiro: [p=0.2] *dois k menos seis.* [p=0.2] Zera *só* em k igual a três. [p=0.3] {a}E aí, o amarelo: "
        "[p=0.2] olhe as equações. [p=0.2] A segunda é *o triplo inteiro* da primeira, [p=0.2] até o doze, que é três "
        "vezes quatro. [p=0.2] *Gêmeas:* [p=0.2] infinitas soluções. [p=0.2] {ok}*Letra B!* [p=0.3] {v}Repare: "
        "[p=0.2] *nenhum k* deixa esse sistema impossível. [p=0.4] {xa}A A confundiu D zero com impossível. [p=0.2] "
        "{xc}A C ignorou o caso D zero, [p=0.2] {xd}a D errou o sinal, [p=0.2] {xe}e a E trocou o verde pelo vermelho."),

    # ================= QUESTÃO 5: HOMOGÊNEO =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}O sistema homogêneo *x mais y igual a zero* [p=0.2] e *três x mais k y igual "
        "a zero* [p=0.2] tem soluções *além de zero, zero* quando: [p=0.4] {la}A, [p=0.2] k igual a três. [p=0.2] "
        "{lb}B, [p=0.2] k igual a menos três. [p=0.2] {lc}C, [p=0.2] k igual a zero. [p=0.2] {ld}D, [p=0.2] k "
        "diferente de três. [p=0.2] {le}E, [p=0.2] nunca, [p=0.2] pois um homogêneo só tem a solução zero, zero. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}A porta zero, zero está sempre aberta. [p=0.2] A pergunta é se há *outras.* [p=0.3] {a}Para isso, [p=0.2] "
        "*D tem de ser zero:* [p=0.2] k menos três igual a zero, [p=0.2] *k igual a três.* [p=0.2] {v}Conferindo: "
        "[p=0.2] com k três, [p=0.2] um e menos um resolve as duas. [p=0.2] {ok}*Letra A!* [p=0.4] {xb}A B errou o "
        "sinal. [p=0.2] {xc}Com k zero, D dá menos três: [p=0.2] só a trivial. [p=0.2] {xd}A D é justamente o caso de "
        "solução única, [p=0.2] {xe}e a E esqueceu que D zero abre outras portas."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}Dois por dois, Sarrus, Laplace [p=0.2] e a inversa: [p=0.2] episódio um. "
        "[p=0.3] {c}As propriedades: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}A vezes X igual a B [p=0.2] e a regra de Cramer: [p=0.2] episódio três. [p=0.3] {b}Classificação, "
        "parâmetro e homogêneo: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o "
        "episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte e cinco questões* [p=0.2] {b}e acerte pelo menos *dezoito.* [p=0.4] "
        "{c}Com pelo menos *seis* de classificação [p=0.2] ou discussão de sistemas."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Polinômios e equações polinomiais:* [p=0.3] {b}a busca por soluções sai de *várias "
        "incógnitas do primeiro grau* [p=0.3] {c}e vai para *uma incógnita só, de grau alto.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de determinantes está completa. [p=0.2] "
        "Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
