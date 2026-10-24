# Roteiro — Equação do 2º Grau e Fórmula de Bhaskara, Episódio 4 de 6: do texto à equação (áreas, campeonatos, Pitágoras
# e lucro) e o descarte de raízes.
# Base: Estudos/Enem/estudos/01-matematica/21-equacao-2o-grau-bhaskara.html — seção 07 + Questões 1, 6, 9 e 7 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O x² NASCE quando duas medidas desconhecidas se multiplicam: largura × comprimento, times × adversários, preço × quantidade.
#   DESCARTAR NÃO É TROCAR O SINAL: a raiz −10 vai para a LIXEIRA inteira; ela não vira 10.
#   A CALÇADA ABRAÇA o jardim: aparece dos DOIS lados de cada medida, por isso cada medida cresce 2x.
#   CADA JOGO FOI CONTADO DUAS VEZES (A × B e B × A): por isso se divide por 2.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (todos conferidos em trabalho/conferir_contas.py):
#   Calçada (seção 07 = Questão 1, "eu faço": repetir é permitido): (10 + 2x)(6 + 2x) = 140 → 4x² + 32x − 80 = 0 →
#   ÷ 4 → x² + 8x − 20 = 0 → soma −8, produto −20 → 2 e −10 → 2 m · conferência 14 · 10 = 140.
#   Campeonato (seção 07): 4 times = 6 jogos (tabela) · 45 jogos → n² − n − 90 = 0, Δ = 361, n = (1 + 19)/2 = 10 (−9 fora) ·
#   turno e returno com 10 times = 90 jogos. Releia a pergunta: área só da calçada = 140 − 60 = 80 m²; lado externo maior 14 m.
#   Nós fazemos (prompt): x(x + 3) = 40 → x² + 3x − 40 = 0 → 5 e −8 → 5 m · 5 · 8 = 40.
# Exemplo nosso (regra de exemplos): o erro 3 ((x + 2)² = x² + 4 dentro de Pitágoras) usaria os números da Questão 9, que é
#   a "você faz". Ele usa x² + (x + 1)² = 25: errado dá x² = 12 (x ≈ 3,5); certo dá x² + x − 12 = 0 → 3 e −4 (9 + 16 = 25).
# QUESTÃO 1 (eu faço, texto idêntico): A, 2 m. Erradas (material e prompt): E troca o sinal da raiz descartada · C calçada
#   num lado só, (10 + x)(6 + x) = 140 → 4 · B esquece o 4x²: 60 + 32x = 140 → 2,5 · D esquece os termos do meio:
#   60 + 4x² = 140 → √20 ≈ 4,5.
# QUESTÃO 6 (nós fazemos, texto idêntico): n² − n − 132 = 0, Δ = 529 = 23², n = (1 + 23)/2 = 12 → C; −11 descartada;
#   12 · 11 ÷ 2 = 66. Erradas: D para no √Δ (23) · B é n − 1 ou o −11 com o sinal trocado · A trata como n² = 66 (≈ 8,1) ·
#   E divide 66 por 2.
# QUESTÃO 9 (você faz, texto idêntico): x² + (x + 2)² = 100 → x² + 2x − 48 = 0 → 6 e −8 → lado maior 8 (D); 36 + 64 = 100.
#   Erradas: B é o lado menor · E vem de (x + 2)² = x² + 4 (x² = 48, x ≈ 6,9, maior ≈ 8,9) · C supõe tela quadrada
#   (10 ÷ √2 ≈ 7,1) · A é metade da diagonal.
# QUESTÃO 7 (desafio, texto idêntico): L = x(50 − x) − (10x + 300) = −x² + 40x − 300; lucro zero: x² − 40x + 300 = 0,
#   Δ = 400, raízes 10 e 30. Sinal por TESTE de valores (sem a regra do sinal): L(5) = −125, L(20) = 100, L(35) = −125.
#   Resposta A (10). Erradas: C a outra raiz (o lucro volta a zero) · B 20, lucro máximo, só CITADO (série de Função
#   quadrática; nada de vértice calculado) · D soma das raízes · E produto.
# Acréscimos nossos (verde): "iguale a zero e divida pelo fator comum"; "dois números SEGUIDOS cujo produto é o dobro dos
#   jogos" (10 · 9 = 90, 12 · 11 = 132); "confira na frase do texto, não na equação".
# Frases-chave (meio e fim, idênticas): 1. Duas medidas desconhecidas multiplicadas: equação do 2º grau. 2. Iguale a zero e
#   simplifique antes da fórmula. 3. Raiz sem sentido se descarta, não se troca o sinal.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Do texto à equação do 2º grau: a raiz que vai para o lixo · Matemática ENEM, 2º grau episódio 4"

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
        "{a}A equação deu *menos dez* e *dois.* [p=0.4] {b}A largura de uma calçada não pode ser negativa, [p=0.2] então "
        "muita gente marca *dez metros.* [p=0.4] {c}A resposta é *dois.* [p=0.4] {d}O menos dez não muda de sinal: "
        "[p=0.2] *ele vai para o lixo.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai transformar *áreas, campeonatos e lucros* em equação do segundo grau [p=0.3] "
        "{b}e escolher *a raiz que faz sentido.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do primeiro grau: [p=0.2] a *etiqueta do x,* [p=0.2] e *a raiz nem sempre "
        "é a resposta.* [p=0.4] {b}Das expressões algébricas: [p=0.2] x mais dois, ao quadrado, [p=0.2] é *x ao quadrado, "
        "mais quatro x, mais quatro.* [p=0.4] {c}E do episódio três: [p=0.2] *soma e produto* acham as raízes de cabeça."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Duas situações do dia a dia. [p=0.3] {a}A planta de um jardim de *dez por seis metros,* [p=0.2] com uma "
        "*calçada* em volta. [p=0.4] {b}E a tabela de um campeonato de bairro, [p=0.2] em que *todo time enfrenta todo "
        "time.* [p=0.4] {c}Transformar uma situação dessas em equação [p=0.2] tem nome: *modelar.*"),

    # ================= BLOCO A: DE ONDE NASCE O x² =================
    dict(id="05", block="nasce", text=
        "{t}Mas por que aparece um *x ao quadrado?* [p=0.4] {a}Porque *duas medidas desconhecidas se multiplicam.* "
        "[p=0.4] {b}Largura *vezes* comprimento. [p=0.3] {c}Times *vezes* adversários. [p=0.3] {d}Preço *vezes* "
        "quantidade. [p=0.4] {e}x vezes x [p=0.2] dá *x ao quadrado.*"),

    # ================= BLOCO B: A CALÇADA =================
    dict(id="06", block="calcada", text=
        "{t}Quanto mede a calçada, [p=0.2] se o conjunto tem *cento e quarenta metros quadrados?* [p=0.4] {a}Etiqueta: "
        "[p=0.2] *x é a largura da calçada, em metros.* [p=0.4] {b}A calçada *abraça* o jardim: [p=0.2] aparece dos *dois "
        "lados* de cada medida. [p=0.4] {c}O dez vira *dez mais dois x,* [p=0.2] e o seis vira *seis mais dois x.* [p=0.4] "
        "{d}Área é comprimento vezes largura: [p=0.2] *o produto dos dois, igual a cento e quarenta.*"),
    dict(id="07", block="calcada", text=
        "{a}Fazendo a distributiva: [p=0.2] *quatro x ao quadrado, mais trinta e dois x, mais sessenta,* [p=0.2] igual a "
        "cento e quarenta. [p=0.4] {b}Passe o cento e quarenta para o lado de lá: [p=0.2] *igual a zero.* [p=0.4] {c}Tudo "
        "é múltiplo de quatro: [p=0.2] *divida por quatro.* [p=0.2] Fica *x ao quadrado, mais oito x, menos vinte, igual a "
        "zero.* [p=0.4] {d}Soma menos oito, [p=0.2] produto menos vinte: [p=0.2] *dois* e *menos dez.*"),
    dict(id="08", block="calcada", text=
        "{t}Qual raiz serve? [p=0.4] {a}Volte ao texto: [p=0.2] x é uma *largura,* [p=0.2] e largura negativa não existe. "
        "[p=0.4] {b}O menos dez *vai embora.* [p=0.4] {c}A calçada mede *dois metros.* [p=0.4] {d}Confira: [p=0.2] "
        "catorze vezes dez, [p=0.2] *cento e quarenta.*"),
    dict(id="09", block="atalho1", text=
        "{t}O atalho: [p=0.3] {a}antes da fórmula, [p=0.2] *iguale a zero.* [p=0.4] {b}Depois divida tudo por um *fator "
        "comum.* [p=0.4] {c}As raízes *não mudam,* [p=0.2] e os números ficam pequenos para soma e produto."),

    # ================= BLOCO C: O CAMPEONATO =================
    dict(id="10", block="campeonato", text=
        "{t}E o campeonato? [p=0.4] {a}Em *turno único,* [p=0.2] cada time enfrenta cada um dos outros *uma vez só.* "
        "[p=0.4] {b}Com quatro times, [p=0.2] cada um enfrenta *três* adversários: [p=0.2] quatro vezes três, [p=0.2] "
        "*doze.* [p=0.4] {c}Mas olhe a tabela: [p=0.2] *A contra B* e *B contra A* [p=0.2] são o *mesmo jogo.* [p=0.4] "
        "{d}Cada jogo foi contado *duas vezes.* [p=0.2] Divida por dois: [p=0.2] *seis jogos.*"),
    dict(id="11", block="campeonato", text=
        "{t}Com n times, [p=0.2] jogos é *n vezes n menos um, dividido por dois.* [p=0.4] {a}Com *quarenta e cinco jogos:* "
        "[p=0.2] *n ao quadrado, menos n, menos noventa, igual a zero.* [p=0.4] {b}Delta: [p=0.2] *trezentos e sessenta e "
        "um,* [p=0.2] dezenove ao quadrado. [p=0.4] {c}n é um mais dezenove, sobre dois: [p=0.2] *dez times.* [p=0.2] O "
        "menos nove vai para o lixo. [p=0.4] {d}Em *turno e returno,* [p=0.2] cada par joga *duas vezes:* [p=0.2] *não* se "
        "divide por dois."),
    dict(id="12", block="atalho2", text=
        "{t}Atalho: [p=0.3] {a}n vezes n menos um [p=0.2] são *dois números seguidos.* [p=0.4] {b}Dobre os jogos: [p=0.2] "
        "noventa [p=0.2] é *dez vezes nove.* [p=0.4] {c}O maior [p=0.2] é o *número de times.*"),

    # ================= BLOCO D: DESCARTAR =================
    dict(id="13", block="descartar", text=
        "{t}O que é *descartar* uma raiz? [p=0.4] {a}É jogar fora a raiz que *não faz sentido:* [p=0.2] medida, tempo ou "
        "número de times *negativo.* [p=0.4] {b}Ela vai para a lixeira *inteira.* [p=0.4] {c}*Descartar não é trocar o "
        "sinal:* [p=0.2] o menos dez *não vira dez.*"),

    # ================= BLOCO E: RELEIA A PERGUNTA =================
    dict(id="14", block="releia", text=
        "{t}Achou a raiz. [p=0.2] Acabou? [p=0.4] {a}Não: [p=0.2] *releia a pergunta.* [p=0.4] {b}No jardim, [p=0.2] a "
        "largura da calçada é *dois;* [p=0.2] o lado maior do conjunto, *catorze.* [p=0.4] {c}E a área *só da calçada:* "
        "[p=0.2] cento e quarenta menos sessenta, [p=0.2] *oitenta metros quadrados.* [p=0.4] {d}Mesma equação, [p=0.2] "
        "três respostas."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um terreno retangular tem um lado *três metros maior* que o outro [p=0.2] e área de "
        "*quarenta metros quadrados.* [p=0.4] {b}Quanto mede o *lado menor?* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Etiqueta: [p=0.2] x é o lado menor, em metros. [p=0.2] O maior é *x mais três.* "
        "[p=0.4] {b}x vezes x mais três, [p=0.2] igual a quarenta. [p=0.2] *x ao quadrado, mais três x, menos quarenta, "
        "igual a zero.* [p=0.4] {c}Soma menos três, [p=0.2] produto menos quarenta: [p=0.2] *cinco* e *menos oito.* "
        "[p=0.4] {d}Menos oito vai para o lixo. [p=0.2] Lado menor: *cinco metros.* [p=0.2] Confira: [p=0.2] cinco vezes "
        "oito, *quarenta.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] duas medidas desconhecidas multiplicadas: [p=0.2] equação "
        "do segundo grau. [p=0.5] {b}Dois: [p=0.2] iguale a zero e simplifique antes da fórmula. [p=0.5] {c}Três: "
        "[p=0.2] raiz sem sentido se descarta, [p=0.2] não se troca o sinal."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] a conta dá dois e menos dez, [p=0.2] e a pessoa "
        "marca *dez metros.* [p=0.4] {b}Parece certo, [p=0.2] porque o dez apareceu na conta. [p=0.4] {c}Mas o menos dez "
        "*vai para o lixo inteiro.* [p=0.2] A resposta é a *outra* raiz: [p=0.2] *dois.*"),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] aplicar a fórmula direto [p=0.2] no produto *igual a cento e quarenta.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque os números estão todos ali. [p=0.4] {c}Mas a fórmula só vale [p=0.2] com *zero do outro "
        "lado.* [p=0.2] Passe o cento e quarenta: [p=0.2] o c é *menos oitenta,* [p=0.2] não sessenta."),
    dict(id="20", block="erros", text=
        "{t}Terceiro, [p=0.2] no *teorema de Pitágoras:* [p=0.2] num triângulo retângulo, [p=0.2] o lado maior ao quadrado "
        "[p=0.2] é a soma dos quadrados dos outros dois. [p=0.4] {a}Lados x e x mais um, [p=0.2] lado maior cinco: [p=0.2] "
        "a pessoa escreve x mais um ao quadrado [p=0.2] como *x ao quadrado mais um.* [p=0.4] {b}Parece certo: [p=0.2] é só "
        "elevar cada pedaço. [p=0.4] {c}Mas falta o *termo do meio,* [p=0.2] dois x. [p=0.2] Certo: [p=0.2] *x ao quadrado, "
        "mais x, menos doze, igual a zero:* [p=0.2] lados *três* e *quatro.*"),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="21", block="q1", text=
        "{t}Questão do ENEM, [p=0.2] do nosso material. [p=0.2] Eu resolvo. [p=0.4] {a}Um jardim retangular de *dez metros "
        "por seis metros* [p=0.2] será contornado por uma calçada de largura constante, [p=0.2] em todos os lados. [p=0.3] "
        "Com a calçada, [p=0.2] o conjunto formará um retângulo de *cento e quarenta metros quadrados* de área. [p=0.3] A "
        "largura da calçada será de: [p=0.4] {qa}A: dois metros. [p=0.2] {qb}B: dois vírgula cinco metros. [p=0.2] {qc}C: "
        "quatro metros. [p=0.2] {qd}D: cerca de quatro vírgula cinco metros. [p=0.2] {qe}E: dez metros. [p=0.4] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{a}Dez mais dois x, [p=0.2] vezes seis mais dois x, [p=0.2] igual a cento e quarenta. [p=0.4] {b}Iguale a zero e "
        "divida por quatro: [p=0.2] *x ao quadrado, mais oito x, menos vinte.* [p=0.4] {c}Raízes *dois* e *menos dez;* "
        "[p=0.2] o menos dez vai para o lixo. [p=0.4] {d}Confira: [p=0.2] catorze vezes dez, [p=0.2] *cento e quarenta.* "
        "[p=0.3] {ok}*Letra A!*"),
    dict(id="23", block="q1", text=
        "{t}E as erradas? [p=0.3] {xe}A E *trocou o sinal* da raiz descartada. [p=0.4] {xc}A C pôs calçada *de um lado "
        "só,* [p=0.2] e dá quatro. [p=0.4] {xb}A B esqueceu o *quatro x ao quadrado:* [p=0.2] dá dois e meio. [p=0.4] {xd}E "
        "a D esqueceu os *termos do meio:* [p=0.2] raiz de vinte, [p=0.2] *quatro e meio.*"),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="24", block="q6", text=
        "{t}Agora, juntos. [p=0.4] {a}Em um campeonato de futebol de bairro [p=0.2] disputado em *turno único,* [p=0.2] "
        "cada time enfrenta cada um dos outros *exatamente uma vez.* [p=0.3] A tabela completa tem *sessenta e seis jogos.* "
        "[p=0.3] O número de times participantes é: [p=0.4] {qa}A: oito. [p=0.2] {qb}B: onze. [p=0.2] {qc}C: doze. "
        "[p=0.2] {qd}D: vinte e três. [p=0.2] {qe}E: trinta e três. [p=0.4] {p}*Pause e monte a equação.* [p=2.0]"),
    dict(id="25", block="q6", text=
        "{t}Turno único: [p=0.2] divide por dois. [p=0.4] {a}*n ao quadrado, menos n, menos cento e trinta e dois, igual a "
        "zero.* [p=0.4] {b}Delta: [p=0.2] *quinhentos e vinte e nove,* [p=0.2] vinte e três ao quadrado. [p=0.4] {c}n é "
        "um mais vinte e três, sobre dois: [p=0.2] *doze.* [p=0.2] O menos onze vai para o lixo. [p=0.4] {d}Confira: "
        "[p=0.2] doze vezes onze, [p=0.2] metade, [p=0.2] *sessenta e seis.* [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="q6", text=
        "{t}E as erradas? [p=0.3] {xd}A D *parou na raiz do delta.* [p=0.4] {xb}A B é o número de *adversários* de cada "
        "time, [p=0.2] ou o menos onze *com o sinal trocado.* [p=0.4] {xa}A A tratou como *n ao quadrado igual a sessenta "
        "e seis.* [p=0.4] {xe}E a E só dividiu sessenta e seis por dois."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="27", block="q9", text=
        "{t}Agora é com você. [p=0.4] {a}A diagonal de uma tela retangular mede *dez polegadas,* [p=0.2] e um dos lados da "
        "tela mede *duas polegadas a mais* que o outro. [p=0.3] A medida do *lado maior,* em polegadas, é: [p=0.4] {qa}A: "
        "cinco. [p=0.2] {qb}B: seis. [p=0.2] {qc}C: cerca de sete vírgula um. [p=0.2] {qd}D: oito. [p=0.2] {qe}E: cerca de "
        "oito vírgula nove. [p=0.4] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="28", block="q9", text=
        "{t}A diagonal faz um triângulo retângulo. [p=0.4] {a}Lados x e x mais dois: [p=0.2] *x ao quadrado, mais x mais "
        "dois ao quadrado, igual a cem.* [p=0.4] {b}Com o termo do meio, [p=0.2] igualando a zero e dividindo por dois: "
        "[p=0.2] *x ao quadrado, mais dois x, menos quarenta e oito.* [p=0.4] {c}Raízes *seis* e *menos oito:* [p=0.2] "
        "lado maior, *oito.* [p=0.4] {d}Confira: [p=0.2] trinta e seis mais sessenta e quatro, [p=0.2] *cem.* [p=0.3] "
        "{ok}*Letra D!*"),
    dict(id="29", block="q9", text=
        "{t}E as erradas? [p=0.3] {xb}A B é o *lado menor:* [p=0.2] releia a pergunta. [p=0.4] {xe}A E esqueceu o termo do "
        "meio. [p=0.4] {xc}A C supôs uma tela *quadrada.* [p=0.4] {xa}E a A é só *metade da diagonal.*"),

    # ================= QUESTÃO 7 (DESAFIO FINAL) =================
    dict(id="30", block="q7", text=
        "{t}Desafio final. [p=0.4] {a}Uma pequena fábrica vende *x unidades* de um produto por semana [p=0.2] ao preço "
        "unitário de *cinquenta menos x* reais. [p=0.3] O custo semanal de produção é *dez x mais trezentos* reais. [p=0.3] "
        "A *menor* quantidade semanal vendida [p=0.2] a partir da qual a fábrica *deixa de ter prejuízo* é: [p=0.4] {qa}A: "
        "dez. [p=0.2] {qb}B: vinte. [p=0.2] {qc}C: trinta. [p=0.2] {qd}D: quarenta. [p=0.2] {qe}E: trezentos. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="31", block="q7", text=
        "{t}Três palavras primeiro. [p=0.3] {a}*Receita* é o dinheiro que entra: [p=0.2] preço vezes quantidade. [p=0.2] "
        "*Custo* é o que sai. [p=0.2] *Lucro* é receita menos custo; [p=0.2] negativo, [p=0.2] é *prejuízo.* [p=0.4] "
        "{b}Lucro: [p=0.2] *menos x ao quadrado, mais quarenta x, menos trezentos.* [p=0.4] {c}Lucro zero, [p=0.2] vezes "
        "menos um: [p=0.2] delta *quatrocentos,* [p=0.2] raízes *dez* e *trinta.*"),
    dict(id="32", block="q7", text=
        "{t}Qual das duas? [p=0.2] *Teste valores.* [p=0.4] {a}Com *cinco* unidades, [p=0.2] o lucro dá *menos cento e "
        "vinte e cinco:* [p=0.2] prejuízo. [p=0.4] {b}Com *vinte,* [p=0.2] dá *mais cem:* [p=0.2] lucro. [p=0.4] {c}O "
        "prejuízo acaba em *dez unidades.* [p=0.3] {ok}*Letra A!* [p=0.4] {xc}A C é a outra raiz: [p=0.2] depois de "
        "trinta, *o prejuízo volta.* [p=0.4] {xb}A B é onde o lucro é *máximo,* [p=0.2] assunto da série de *Função "
        "quadrática.* [p=0.4] {xd}A D é a *soma* das raízes, [p=0.2] {xe}e a E, *o produto.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] duas medidas desconhecidas multiplicadas: [p=0.2] "
        "equação do segundo grau. [p=0.5] {b}Dois: [p=0.2] iguale a zero e simplifique antes da fórmula. [p=0.5] {c}Três: "
        "[p=0.2] raiz sem sentido se descarta, [p=0.2] não se troca o sinal."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}x à quarta, menos treze x ao quadrado, mais trinta e seis, igual a zero [p=0.2] tem *expoente quatro.* [p=0.4] "
        "{b}Parece outro assunto, [p=0.2] mas é uma equação do segundo grau *disfarçada.* [p=0.4] {c}*Próximo episódio.*"),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já marcou uma raiz com o sinal trocado? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
