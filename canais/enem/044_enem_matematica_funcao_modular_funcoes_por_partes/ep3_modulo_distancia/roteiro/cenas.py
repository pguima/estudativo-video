# Roteiro — Função Modular e Funções por Partes, Episódio 3 de 5: módulo é distância (o gráfico em V e o rebatimento)
# Base: Estudos/Enem/estudos/01-matematica/29-funcao-modular-funcoes-por-partes.html — seções 02, 04 e 05 + Questões 3 e 6.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A DISTÂNCIA: módulo é distância até o zero; distância nunca é negativa (os dois bonequinhos em −3 e 3).
#   O VÉRTICE MORA ONDE O DE DENTRO ZERA: em |x − 3|, o V vai para o 3 (o sinal engana).
#   O ESPELHO NO CHÃO: |f(x)| — o que está acima do eixo fica; o que está abaixo é rebatido para cima.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Equações e inequações modulares: episódio 4. Aqui, os zeros do V e as soluções da Q6 saem pela DISTÂNCIA
#   ("a que distância de −1 está x?") e pelo "o de dentro vale 3 ou −3", sem o método de casos do ep. 4.
# Concreto (regra 1): a régua no chão com dois bonequinhos em −3 e 3 (3 passos cada) e a amplitude térmica entre
#   −4 °C e 9 °C (13 graus).
# Nós fazemos (prompt): y = |x + 1| − 3 → vértice (−1, −3); |x + 1| = 3 → x = 2 ou x = −4.
# Erros (prompt): |x − 3| para a esquerda · |a + b| = |a| + |b| sempre · √(x²) = x.
# QUESTÃO 3 ("eu faço"): gabarito A. Erradas = material (B lê o −2 como esquerda; C troca o sinal do −1 e põe o V acima
#   do eixo, sem zeros; D erra o vértice nos dois sinais, zeros certos; E erra a conta do segundo caso, x = −1).
# QUESTÃO 6 ("você faz", com pausa): gabarito E (quatro). Erradas = prompt, que CORRIGE o material na B: o material diz
#   que a B "conta uma raiz por caso, esquecendo o ±", mas isso daria DUAS; a B é de quem fica com a raiz positiva de
#   um único caso (x = √7), esquecendo o ± e o segundo caso. C só o caso x² − 4 = 3; D seria |x² − 4| = 4 (a reta
#   encosta no topo); A acha que o módulo impede a igualdade (só com número negativo do lado direito).
# Ressalva (desenho do usuário, mantido): o bloco h ensina a contagem geral de |x² − 4| = k antes da Q6; para não
#   entregar o caso k = 3, a régua do bloco h para em k = 1 (quatro cortes), k = 4 (três) e k = 5 (dois); o k = 3 só
#   aparece na Q6.
# Acréscimos NOSSOS (marcados): três cenas verdes de ATALHO — "conta de dentro primeiro, depois tire o sinal" (cena 09),
#   "vértice: zere o de dentro para achar o x; o número de fora é o y" (cena 15, com |x − 5| + 2 para não usar a Q3 nem
#   o nós fazemos) e "contar soluções: régua horizontal na altura k, conte os cortes" (cena 19); a conferência da Q3 e
#   do nós fazemos pela distância ("a 1 do 2: 1 e 3"; "a 3 do −1: 2 e −4"); √7 ≈ 2,65 na conferência da Q6.
# Frases-chave (meio e fim, idênticas): 1. Módulo é distância: nunca é negativo.
#   2. O vértice mora onde o de dentro zera.
#   3. |f(x)|: acima fica, abaixo rebate.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Módulo do zero: distância, o gráfico em V e o rebatimento · Matemática ENEM, Função Modular ep. 3"

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
        "{a}Módulo de menos três *mais* módulo de três [p=0.2] dá *seis.* [p=0.5] {b}Módulo de menos três mais três "
        "[p=0.2] dá *zero.* [p=0.5] {c}As mesmas barrinhas, [p=0.2] os mesmos números, [p=0.2] *resultados diferentes.* "
        "[p=0.5] {d}Hoje você entende por quê, [p=0.2] e ganha um gráfico em forma de *V* de presente."),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Função modular e funções por partes.* [p=0.4] {a}Ao final, [p=0.2] "
        "você vai *calcular módulos,* [p=0.3] {b}achar o *vértice* de qualquer V [p=0.3] {c}e *contar soluções* olhando "
        "um gráfico rebatido."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Da série de Operações: [p=0.2] os *negativos* ficam à esquerda do "
        "zero, [p=0.2] e *menos de menos sete é sete.* [p=0.4] {b}Da série de Função quadrática: [p=0.2] a parábola "
        "*x ao quadrado menos quatro* [p=0.2] corta o eixo x em *menos dois* e *dois,* [p=0.2] com o vértice, o "
        "ponto mais baixo, [p=0.2] em *zero, menos quatro.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine uma régua no chão, [p=0.2] com o zero no meio. [p=0.4] {a}Uma pessoa está no *menos três;* "
        "[p=0.2] outra, no *três.* [p=0.4] {b}As duas caminham até o zero. [p=0.2] Cada uma dá *três passos.* "
        "[p=0.4] {c}E entre *menos quatro graus* e *nove graus?* [p=0.3] O termômetro andou *treze graus.* [p=0.4] "
        "{d}Distância não tem sinal."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}Então, o que é o módulo? [p=0.4] {a}A *reta numérica* é essa régua: [p=0.2] os números em ordem. "
        "[p=0.3] O *módulo,* [p=0.2] ou *valor absoluto,* [p=0.2] é a *distância* do número até o zero. [p=0.4] "
        "{b}Escreve-se com duas barrinhas. [p=0.3] Módulo de menos três é três. [p=0.4] {c}*Módulo é distância até "
        "o zero:* [p=0.2] *distância nunca é negativa.*"),
    dict(id="06", block="definicao", text=
        "{t}E a regra escrita? [p=0.4] {a}Se x é zero ou positivo, [p=0.2] o módulo é *o próprio x.* [p=0.4] {b}Se "
        "x é negativo, [p=0.2] o módulo é *menos x.* [p=0.3] Teste com menos sete: [p=0.2] menos de menos sete "
        "[p=0.2] dá *sete.* [p=0.4] {c}O módulo só *apaga o sinal.*"),

    # ================= BLOCO B: DISTÂNCIA ENTRE DOIS PONTOS =================
    dict(id="07", block="dist", text=
        "{t}E a distância entre *dois* pontos? [p=0.4] {a}É o *módulo da diferença:* [p=0.2] módulo de a menos b. "
        "[p=0.4] {b}Entre menos dois e quatro: [p=0.2] quatro menos menos dois, [p=0.2] *seis.* [p=0.3] Na outra "
        "ordem, [p=0.2] menos seis, [p=0.2] e o módulo devolve *seis.* [p=0.4] {c}A ordem *não importa.*"),
    dict(id="08", block="tabela", text=
        "{t}Vamos treinar. [p=0.4] {a}Módulo de cinco menos nove: [p=0.2] primeiro a conta de dentro, [p=0.2] menos "
        "quatro. [p=0.2] Módulo: [p=0.2] *quatro.* [p=0.4] {b}Módulo de nove menos cinco: [p=0.2] *quatro* também. "
        "[p=0.4] {c}Módulo de menos três mais módulo de três: [p=0.2] *seis.* [p=0.4] {d}E módulo de menos três "
        "mais três: [p=0.2] dentro dá zero, [p=0.2] módulo *zero.* [p=0.3] Esse é o *gancho* resolvido."),
    dict(id="09", block="atalho_dentro", text=
        "{t}Atalho para nunca errar um módulo. [p=0.4] {a}*Primeiro,* [p=0.2] faça a conta *de dentro* das barrinhas. "
        "[p=0.4] {b}*Depois,* [p=0.2] tire o sinal do resultado. [p=0.4] {c}Nessa ordem, [p=0.2] *sempre.*"),

    # ================= BLOCO C: ARMADILHAS COM LETRA =================
    dict(id="10", block="letra", text=
        "{t}E quando aparece uma *letra?* [p=0.4] {a}Módulo de menos x é igual a x? [p=0.3] Teste com x igual a "
        "menos cinco: [p=0.2] o módulo dá *cinco,* [p=0.2] que é *menos x,* [p=0.2] não x. [p=0.4] {b}O certo: "
        "[p=0.2] módulo de menos x [p=0.2] é *módulo de x.* [p=0.4] {c}E, da série de Potenciação: [p=0.2] raiz de "
        "x ao quadrado [p=0.2] também é *módulo de x.* [p=0.3] Raiz de vinte e cinco, [p=0.2] *cinco.*"),

    # ================= BLOCO D: A FUNÇÃO |x| =================
    dict(id="11", block="funcao_v", text=
        "{t}E se o módulo virar uma *função?* [p=0.4] {a}f de x igual a módulo de x. [p=0.2] Marque os pontos: "
        "[p=0.2] menos dois vai em dois, [p=0.2] menos um em um, [p=0.2] zero em zero, [p=0.2] um em um, [p=0.2] "
        "dois em dois. [p=0.4] {b}Formou um *V.* [p=0.3] O bico se chama *vértice:* [p=0.2] onde o gráfico muda de "
        "direção. [p=0.4] {c}À direita, [p=0.2] vale *x;* [p=0.2] à esquerda, [p=0.2] *menos x.* [p=0.3] Como no "
        "episódio um: [p=0.2] *duas leis, um gráfico só.*"),

    # ================= BLOCO E: DESLOCAMENTOS =================
    dict(id="12", block="desloc", text=
        "{t}Para onde o V vai em *módulo de x menos três?* [p=0.4] {a}Um *deslocamento* é o gráfico mudando de "
        "lugar, [p=0.2] sem mudar de forma. [p=0.4] {b}O de dentro zera quando x é *três.* [p=0.3] O V anda *três "
        "para a direita.* [p=0.3] O sinal *engana.* [p=0.4] {c}Em módulo de x mais dois, [p=0.2] zera em *menos "
        "dois:* [p=0.2] o V vai *para a esquerda.*"),
    dict(id="13", block="desloc", text=
        "{t}E o número *de fora?* [p=0.4] {a}Módulo de x *mais um:* [p=0.2] o V *sobe* um. [p=0.4] {b}*Duas vezes* "
        "módulo de x: [p=0.2] o V *fecha.* [p=0.4] {c}E *menos* módulo de x: [p=0.2] o V fica *de cabeça para "
        "baixo.*"),

    # ================= BLOCO F: O VÉRTICE (a, b) =================
    dict(id="14", block="vertice", text=
        "{t}Onde fica o vértice de *módulo de x menos a, mais b?* [p=0.4] {a}No ponto *a, b.* [p=0.3] O a *zera o "
        "de dentro;* [p=0.2] o b é o número *de fora.* [p=0.4] {b}O vértice é o *ponto de mínimo,* [p=0.2] o mais "
        "baixo do gráfico: [p=0.2] o módulo nunca fica abaixo de zero, [p=0.2] então y nunca fica abaixo de *b.* "
        "[p=0.4] {c}Por isso, [p=0.2] a *imagem,* [p=0.2] o que sai, [p=0.2] vai de *b* até o infinito."),
    dict(id="15", block="atalho_vert", text=
        "{t}Atalho para o vértice. [p=0.4] {a}*Zere o de dentro:* [p=0.2] é o *x* do vértice. [p=0.4] {b}O *número "
        "de fora* [p=0.2] é o *y.* [p=0.4] {c}Módulo de x menos cinco, mais dois: [p=0.2] vértice em *cinco, dois.*"),

    # ================= BLOCO G: O REBATIMENTO =================
    dict(id="16", block="rebate", text=
        "{t}E se o módulo abraçar uma função *inteira?* [p=0.4] {a}Pense num *espelho no chão,* [p=0.2] o eixo x. "
        "[p=0.4] {b}O que está *acima* [p=0.2] *fica.* [p=0.4] {c}O que está *abaixo* [p=0.2] é *rebatido,* [p=0.2] "
        "espelhado para cima: [p=0.2] a altura menos três vira *três.*"),
    dict(id="17", block="rebate", text=
        "{t}Vamos rebater a parábola *x ao quadrado menos quatro.* [p=0.4] {a}Ela é *negativa* entre menos dois e "
        "dois. [p=0.3] Esse trecho *dobra para cima,* [p=0.2] como papel. [p=0.4] {b}O vértice zero, menos quatro "
        "[p=0.2] vira *zero, quatro:* [p=0.2] um *máximo local,* [p=0.2] o mais alto daquele pedaço. [p=0.4] {c}E "
        "as raízes *não saem do lugar:* [p=0.2] módulo de zero é zero."),

    # ================= BLOCO H: CONTAR SOLUÇÕES =================
    dict(id="18", block="contar", text=
        "{t}Quantas soluções tem módulo de x ao quadrado menos quatro *igual a k?* [p=0.4] {a}Passe uma *régua "
        "horizontal* na altura k. [p=0.3] Com k negativo, [p=0.2] *nenhum* corte. [p=0.2] Em zero, [p=0.2] *dois.* "
        "[p=0.4] {b}Em k igual a um, [p=0.2] *quatro:* [p=0.2] dois no arco do meio, [p=0.2] um em cada perna. "
        "[p=0.3] Vale para todo k entre zero e quatro. [p=0.4] {c}Em quatro, [p=0.2] a régua *encosta no topo:* "
        "[p=0.2] *três.* [p=0.3] {d}Acima de quatro, [p=0.2] *dois.*"),
    dict(id="19", block="atalho_conta", text=
        "{t}Atalho para contar soluções *sem conta nenhuma.* [p=0.4] {a}*Desenhe* o gráfico rebatido. [p=0.4] {b}Passe "
        "a *régua horizontal* na altura pedida. [p=0.4] {c}*Conte os cortes.* [p=0.2] Cada corte é uma solução."),

    # ================= NÓS FAZEMOS =================
    dict(id="20", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Onde fica o *vértice* de y igual a módulo de x mais um, [p=0.2] menos três? [p=0.4] {b}E "
        "em que valores de x [p=0.2] o gráfico *corta o eixo x?* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Zere o de dentro: [p=0.2] *x igual a menos um.* [p=0.2] O de fora é *menos "
        "três.* [p=0.3] Vértice: [p=0.2] *menos um, menos três.* [p=0.4] {b}Cortar o eixo x é ter y zero: [p=0.2] "
        "módulo de x mais um *igual a três.* [p=0.3] x está a *três passos* do menos um. [p=0.4] {c}Para a direita, "
        "[p=0.2] *dois;* [p=0.2] para a esquerda, [p=0.2] *menos quatro.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="22", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] módulo é distância: [p=0.2] nunca é negativo. [p=0.5] "
        "{b}Dois: [p=0.2] o vértice mora onde o de dentro zera. [p=0.5] {c}Três: [p=0.2] módulo de f de x: [p=0.2] acima "
        "fica, [p=0.2] abaixo rebate."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="23", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que módulo de x menos três [p=0.2] "
        "leva o V *para a esquerda.* [p=0.4] {b}Parece certo, [p=0.2] porque o *menos* lembra a esquerda. [p=0.4] "
        "{c}Mas o vértice mora onde o de dentro zera: [p=0.2] em três, [p=0.2] *à direita.*"),
    dict(id="24", block="erros", text=
        "{a}Segundo: [p=0.2] achar que módulo de a mais b [p=0.2] é *sempre* a soma dos módulos. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque com dois positivos funciona. [p=0.4] {c}Mas módulo de menos três mais três é *zero,* "
        "[p=0.2] e a soma dos módulos dá *seis.*"),
    dict(id="25", block="erros", text=
        "{a}Terceiro: [p=0.2] raiz de x ao quadrado [p=0.2] *igual a x.* [p=0.4] {b}Parece certo, [p=0.2] porque a "
        "raiz *desfaz* o quadrado. [p=0.4] {c}Mas com menos cinco, [p=0.2] a raiz de vinte e cinco dá *cinco.* "
        "[p=0.3] O certo é *módulo de x.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="26", block="q3", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] *eu faço* com você. [p=0.4] {a}O perfil de "
        "uma calha é f de x igual a módulo de x menos dois, [p=0.2] menos um, [p=0.2] em metros. [p=0.3] O ponto "
        "mais baixo do gráfico [p=0.2] e os valores de x em que f de x é zero [p=0.2] são: [p=0.3] {qa}A: [p=0.2] "
        "dois, menos um; [p=0.2] um e três. [p=0.2] {qb}B: [p=0.2] menos dois, menos um; [p=0.2] menos três e menos "
        "um. [p=0.2] {qc}C: [p=0.2] dois, um; [p=0.2] não há. [p=0.2] {qd}D: [p=0.2] menos dois, um; [p=0.2] um e "
        "três. [p=0.2] {qe}E: [p=0.2] dois, menos um; [p=0.2] menos um e três. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="27", block="q3", text=
        "{t}Vamos lá. [p=0.3] {a}O ponto mais baixo é o *vértice.* [p=0.2] Zere o de dentro: [p=0.2] *dois.* "
        "[p=0.2] O de fora: [p=0.2] *menos um.* [p=0.3] Vértice: [p=0.2] *dois, menos um.* [p=0.4] {b}Os zeros: "
        "[p=0.2] módulo de x menos dois *igual a um.* [p=0.3] x está a *um passo* do dois: [p=0.2] *um* ou *três.* "
        "[p=0.4] {c}Confira: [p=0.2] f de um e f de três [p=0.2] dão *zero.* [p=0.3] {ok}*Letra A!*"),
    dict(id="28", block="q3", text=
        "{t}E as armadilhas? [p=0.3] {xb}A B lê o *menos dois* como esquerda. [p=0.4] {xc}A C troca o sinal do "
        "menos um [p=0.2] e põe o V *acima* do eixo, [p=0.2] sem zeros. [p=0.4] {xd}A D erra o vértice *nos dois "
        "sinais,* [p=0.2] com os zeros certos. [p=0.4] {xe}E a E erra a conta: [p=0.2] x menos dois igual a menos "
        "um [p=0.2] dá *um,* [p=0.2] não menos um."),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="29", block="q6", text=
        "{t}Agora é com você. [p=0.4] {a}O gráfico de g de x igual a módulo de x ao quadrado menos quatro [p=0.2] "
        "sai da parábola x ao quadrado menos quatro, [p=0.2] refletindo para cima o trecho abaixo do eixo. [p=0.3] "
        "Quantos números reais x [p=0.2] fazem *g de x igual a três?* [p=0.3] {qa}A: [p=0.2] nenhum. [p=0.2] {qb}B: "
        "[p=0.2] um. [p=0.2] {qc}C: [p=0.2] dois. [p=0.2] {qd}D: [p=0.2] três. [p=0.2] {qe}E: [p=0.2] quatro. "
        "[p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="30", block="q6", text=
        "{t}Vamos conferir, [p=0.2] por *dois caminhos.* [p=0.4] {a}Pela conta: [p=0.2] o de dentro vale *três* ou "
        "*menos três.* [p=0.4] {b}x ao quadrado menos quatro igual a três: [p=0.2] x ao quadrado é sete, [p=0.2] "
        "*mais ou menos raiz de sete.* [p=0.4] {c}Igual a menos três: [p=0.2] x ao quadrado é um, [p=0.2] *mais ou "
        "menos um.* [p=0.3] *Quatro* soluções."),
    dict(id="31", block="q6", text=
        "{t}Agora pelo *gráfico.* [p=0.4] {a}O topo do arco rebatido está em *zero, quatro.* [p=0.3] A régua em "
        "três [p=0.2] passa *abaixo* do topo. [p=0.4] {b}Corta o arco do meio *duas vezes,* [p=0.2] em menos um e "
        "um, [p=0.2] e cada perna *uma vez,* [p=0.2] perto de dois vírgula seis cinco. [p=0.4] {c}Quatro cortes. "
        "[p=0.3] {ok}*Letra E!*"),
    dict(id="32", block="q6", text=
        "{t}E as armadilhas? [p=0.3] {xc}A C, dois, [p=0.2] resolve só o caso *igual a três.* [p=0.4] {xd}A D, "
        "três, [p=0.2] seria a resposta de g de x igual a *quatro,* [p=0.2] com a régua no topo. [p=0.4] {xb}A B, "
        "um, [p=0.2] fica só com *raiz de sete,* [p=0.2] esquecendo o mais ou menos e o outro caso. [p=0.4] {xa}E a "
        "A, nenhum, [p=0.2] acha que o módulo impede a igualdade, [p=0.2] o que só vale com número *negativo* do "
        "outro lado."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] módulo é distância: [p=0.2] nunca é negativo. "
        "[p=0.5] {b}Dois: [p=0.2] o vértice mora onde o de dentro zera. [p=0.5] {c}Três: [p=0.2] módulo de f de x: "
        "[p=0.2] acima fica, [p=0.2] abaixo rebate."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Um pacote de café de *quinhentos gramas* [p=0.2] pode variar no máximo *oito gramas.* [p=0.4] {b}Como se "
        "escreve isso com as *duas barrinhas?* [p=0.4] {c}E por que módulo de x igual a cinco tem *duas* respostas? "
        "[p=0.4] {d}Próximo episódio."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] em que outra situação do dia a dia o que importa é a distância, e não "
        "o sinal? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os "
        "*flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
