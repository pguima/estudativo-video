# Roteiro — Potenciação e Radiciação, Episódio 4 de 7: Raiz, a operação que desfaz a potência (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/04-potenciacao-radiciacao.html — seções 05 e 06 (+ Questão 8 da seção 12).
# Simplificar radicais (√50 = 5√2) é o ep5: aqui só as propriedades.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   IDA E VOLTA: potência é o caminho de ida (9 → 81); raiz é o caminho de volta (81 → 9). √81 pergunta: quem, ao quadrado, deu 81?
#   GEOMETRIA: raiz quadrada = lado do quadrado (piso de 81 m² → lado 9 m); raiz cúbica = aresta do cubo (caixa de 8 L → 2 dm).
#   DOIS PONTOS DE PARTIDA, UM DESTINO: −5 e +5 ao quadrado dão 25, mas a volta da raiz quadrada vai só para o +5.
# Termos definidos na hora: raiz, radical (o sinal √), índice, radicando, raiz quadrada, raiz cúbica, números reais, módulo.
# Teste com números pequenos (ep2): √(4·9) = 6 = 2·3 · √(100/4) = 5 = 10/2 · √(9+16) = 5 ≠ 3 + 4 = 7 · ⁴√16 = 2 = √4.
# QUESTÃO 8 do material (texto idêntico na tela): x = −7 → √(x²) + ∛(x³) = 7 + (−7) = 0 → C.
#   A (−14): aplicou √(x²) = x, esqueceu o módulo (explicação do material).
#   Explicações NOSSAS (o material só explica a A): E (14) = tirou o sinal das DUAS raízes (pôs módulo também na cúbica);
#   D (7) = fez só a raiz quadrada e esqueceu a segunda parcela; B (−7) = fez só a raiz cúbica.
# Frases-chave (meio e fim, idênticas):
#   1. Raiz desfaz a potência.
#   2. Raiz de índice par devolve sempre o positivo.
#   3. A raiz se distribui no produto e na divisão, nunca na soma.
# Atalhos (verde): "confira elevando de volta" · "índice par com negativo dentro: não existe; ímpar: copie o sinal" ·
#   "índice par tira o sinal; ímpar mantém" · "raiz de raiz: multiplique os índices" · "divida índice e expoente pelo mesmo
#   número" · "na dúvida, teste com números de raiz exata (9 e 16)".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "√(9 + 16) NÃO é √9 + √16: raiz do zero, sem decorar · Matemática ENEM, episódio 4"

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
        "{a}Raiz de nove mais dezesseis [p=0.2] é igual a raiz de nove [p=0.2] mais raiz de dezesseis? [p=0.5] {b}Faça a conta. "
        "[p=0.3] {c}De um lado, [p=0.2] nove mais dezesseis é vinte e cinco, [p=0.2] e a raiz dá *cinco.* [p=0.4] {d}Do outro, "
        "[p=0.2] três mais quatro, [p=0.2] *sete.* [p=0.5] {e}Essa regra que parece óbvia *não existe.* [p=0.3] {f}E o ENEM "
        "sabe disso."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber *quando uma raiz existe,* [p=0.3] {b}como ela se comporta com números "
        "*negativos,* [p=0.3] {c}e quais regras valem *de verdade.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes do episódio um. [p=0.3] {a}Potência é multiplicar a base por ela mesma: [p=0.2] cinco ao "
        "quadrado é cinco vezes cinco, [p=0.2] *vinte e cinco.* [p=0.2] Dois ao cubo, [p=0.2] dois vezes dois vezes dois, "
        "[p=0.2] *oito.* [p=0.4] {b}E com base negativa: [p=0.2] expoente *par* dá positivo, [p=0.2] menos cinco ao quadrado "
        "dá *vinte e cinco.* [p=0.3] {c}Expoente *ímpar* dá negativo: [p=0.2] menos dois ao cubo dá *menos oito.*"),

    # ================= BLOCO A/B: IDA E VOLTA, PELA GEOMETRIA =================
    dict(id="04", block="piso", text=
        "{t}Imagine um piso quadrado [p=0.2] com *oitenta e um metros quadrados* de área. [p=0.3] Quanto mede o lado? [p=0.5] "
        "{a}A área do quadrado é o lado vezes o lado, [p=0.2] o lado *ao quadrado.* [p=0.4] {b}Então a pergunta é: [p=0.2] "
        "que número, vezes ele mesmo, [p=0.2] dá oitenta e um? [p=0.4] {c}Nove! [p=0.2] Porque nove vezes nove é oitenta e "
        "um. [p=0.3] {d}O lado mede *nove metros.*"),
    dict(id="05", block="idavolta", text=
        "{t}Repare no que aconteceu. [p=0.3] {a}Elevar ao quadrado é o *caminho de ida:* [p=0.2] do nove, [p=0.2] você chega "
        "no oitenta e um. [p=0.4] {b}E a pergunta do piso fez o *caminho de volta:* [p=0.2] do oitenta e um, [p=0.2] de volta "
        "para o nove. [p=0.4] {c}Esse caminho de volta tem nome: [p=0.2] *raiz.* [p=0.3] {d}A raiz é a operação que *desfaz* "
        "a potência."),
    dict(id="06", block="nomes", text=
        "{t}E como se escreve? [p=0.3] {a}Com este sinal, [p=0.2] que se chama *radical.* [p=0.4] {b}O número que fica "
        "dentro, [p=0.2] o oitenta e um, [p=0.2] é o *radicando.* [p=0.4] {c}E o numerozinho no canto [p=0.2] é o *índice:* "
        "[p=0.2] ele diz qual potência você está desfazendo. [p=0.4] {d}Índice dois é a *raiz quadrada,* [p=0.2] e o dois "
        "nem se escreve. [p=0.3] {e}Raiz de oitenta e um é *nove.*"),
    dict(id="07", block="nomes", text=
        "{t}No geral, [p=0.2] a matemática escreve assim: [p=0.3] {a}raiz de índice *n* de *a* [p=0.2] é igual a *b* [p=0.3] "
        "{b}quando *b* elevado a *n* [p=0.2] dá *a.* [p=0.4] {c}Essa setinha dupla quer dizer: [p=0.2] uma coisa vale "
        "*exatamente quando* a outra vale. [p=0.4] {d}É a ida e a volta, [p=0.2] escritas lado a lado."),
    dict(id="08", block="cubo", text=
        "{t}E se o índice for *três?* [p=0.3] {a}Pense numa caixa em forma de cubo, [p=0.2] com *oito litros.* [p=0.3] Quanto "
        "mede a aresta, [p=0.2] que é cada lado do cubo? [p=0.4] {b}O volume do cubo é aresta vezes aresta vezes aresta: "
        "[p=0.2] a aresta *ao cubo.* [p=0.4] {c}Que número, ao cubo, dá oito? [p=0.3] *Dois.* [p=0.4] {d}Essa é a *raiz "
        "cúbica:* [p=0.2] raiz de índice três de oito [p=0.2] é *dois.* [p=0.3] {e}Raiz quadrada é o lado do quadrado; "
        "[p=0.2] raiz cúbica é a aresta do cubo."),
    dict(id="09", block="confere", text=
        "{t}E um atalho para nunca errar uma raiz: [p=0.3] {a}*confira elevando de volta.* [p=0.4] {b}Achou que raiz de "
        "oitenta e um é nove? [p=0.2] Nove ao quadrado dá oitenta e um? [p=0.2] Dá. [p=0.2] Certo. [p=0.4] {c}Raiz cúbica de "
        "oito é dois? [p=0.2] Dois ao cubo dá oito? [p=0.2] Dá. [p=0.3] {d}A volta sempre se confere com a ida."),

    # ================= BLOCO C: QUANDO A RAIZ EXISTE =================
    dict(id="10", block="existe", text=
        "{t}E agora, uma pergunta curiosa: [p=0.2] quanto é raiz de *menos quatro?* [p=0.5] {a}Que número, ao quadrado, "
        "dá menos quatro? [p=0.3] {b}Dois? [p=0.2] Dois ao quadrado dá *quatro,* positivo. [p=0.3] {c}Menos dois? [p=0.2] "
        "Menos com menos dá mais: [p=0.2] também *quatro.* [p=0.4] {d}Nenhum número ao quadrado dá negativo. [p=0.3] {e}Então "
        "raiz de menos quatro *não existe* [p=0.2] nos números reais."),
    dict(id="11", block="existe", text=
        "{t}E o que são os *números reais?* [p=0.3] {a}São todos os números que cabem numa reta: [p=0.2] inteiros, "
        "[p=0.2] frações, [p=0.2] decimais, [p=0.2] positivos e negativos. [p=0.4] {b}São os números que você usa no dia a "
        "dia, [p=0.2] e os únicos que o ENEM usa nestas questões. [p=0.4] {c}Nessa reta, [p=0.2] *nenhum* número é a raiz "
        "quadrada de menos quatro."),
    dict(id="12", block="existe", text=
        "{t}Mas e a raiz *cúbica* de menos oito? [p=0.4] {a}Que número, ao cubo, dá menos oito? [p=0.3] {b}Menos dois! "
        "[p=0.3] Menos dois, vezes menos dois, vezes menos dois: [p=0.2] *menos oito.* [p=0.4] {c}Expoente ímpar *conserva* o "
        "sinal. [p=0.3] {d}Então a raiz cúbica de menos oito *existe,* [p=0.2] e é *negativa:* [p=0.2] menos dois."),
    dict(id="13", block="tabela", text=
        "{t}Juntando tudo numa tabela. [p=0.3] {a}Índice par, [p=0.2] radicando positivo: [p=0.2] existe. [p=0.2] Raiz de "
        "dezesseis é quatro. [p=0.4] {b}Índice par, [p=0.2] radicando negativo: [p=0.2] *não existe.* [p=0.4] {c}Índice "
        "ímpar, [p=0.2] radicando positivo: [p=0.2] existe. [p=0.2] Raiz cúbica de oito é dois. [p=0.4] {d}Índice ímpar, "
        "[p=0.2] radicando negativo: [p=0.2] existe, [p=0.2] e é *negativa.* [p=0.4] {e}Atalho: [p=0.2] índice par com "
        "negativo dentro, [p=0.2] não existe. [p=0.2] Índice ímpar, [p=0.2] *copie o sinal.*"),

    # ================= BLOCO D: A SUTILEZA DO MÓDULO =================
    dict(id="14", block="modulo", text=
        "{t}Agora, a sutileza que mais aparece em questão. [p=0.3] {a}Quanto é a raiz de *menos cinco ao quadrado?* [p=0.4] "
        "{b}Parece que a raiz desfaz o quadrado [p=0.2] e sobra o menos cinco. [p=0.4] {c}Mas faça com calma: [p=0.2] "
        "primeiro o quadrado, [p=0.2] menos cinco ao quadrado é *vinte e cinco.* [p=0.3] {d}Raiz de vinte e cinco: [p=0.2] "
        "*cinco.* [p=0.2] Positivo!"),
    dict(id="15", block="modulo", text=
        "{t}Por quê? [p=0.3] {a}No caminho de ida, [p=0.2] existem *dois* pontos de partida: [p=0.2] menos cinco ao quadrado "
        "dá vinte e cinco, [p=0.2] e mais cinco ao quadrado também. [p=0.4] {b}Mas a volta da raiz quadrada [p=0.2] tem um "
        "destino só: [p=0.2] o *positivo.* [p=0.4] {c}A raiz quadrada foi combinada assim, [p=0.2] para dar sempre uma "
        "resposta só, [p=0.2] sem sinal de menos."),
    dict(id="16", block="modulo", text=
        "{t}Esse valor sem sinal tem nome: [p=0.2] *módulo.* [p=0.3] {a}O módulo de um número é a distância dele até o zero: "
        "[p=0.2] o módulo de menos cinco é cinco, [p=0.2] e o de cinco também é cinco. [p=0.4] {b}Ele se escreve entre duas "
        "barrinhas em pé. [p=0.4] {c}Então a regra certa é: [p=0.2] raiz de *a ao quadrado* [p=0.2] é o *módulo de a,* "
        "[p=0.2] e não simplesmente *a.*"),
    dict(id="17", block="impar_sinal", text=
        "{t}E no índice ímpar? [p=0.3] {a}Raiz cúbica de menos dois ao cubo: [p=0.2] menos dois ao cubo é menos oito, "
        "[p=0.2] e a raiz cúbica de menos oito [p=0.2] é *menos dois.* [p=0.4] {b}Voltou com o sinal. [p=0.2] No índice "
        "ímpar, [p=0.2] *não tem módulo.* [p=0.4] {c}Atalho: [p=0.2] índice par *tira* o sinal; [p=0.2] índice ímpar "
        "*mantém.*"),

    # ================= BLOCO E: PROPRIEDADES QUE VALEM =================
    dict(id="18", block="produto", text=
        "{t}E quais regras valem com raiz? [p=0.3] A primeira: [p=0.2] *raiz de um produto.* [p=0.3] {a}Produto é o resultado "
        "de uma multiplicação. [p=0.4] {b}Raiz de quatro vezes nove [p=0.2] é raiz de trinta e seis, [p=0.2] *seis.* [p=0.4] "
        "{c}E raiz de quatro, [p=0.2] vezes raiz de nove, [p=0.2] é dois vezes três: [p=0.2] *seis* também! [p=0.4] {d}A raiz "
        "do produto [p=0.2] é o produto das raízes."),
    dict(id="19", block="produto", text=
        "{t}Com a divisão, [p=0.2] a mesma coisa. [p=0.3] {a}Raiz de cem dividido por quatro [p=0.2] é raiz de vinte e cinco, "
        "[p=0.2] *cinco.* [p=0.4] {b}E raiz de cem [p=0.2] dividido por raiz de quatro [p=0.2] é dez dividido por dois: "
        "[p=0.2] *cinco.* [p=0.4] {c}A raiz do quociente, [p=0.2] que é o resultado de uma divisão, [p=0.2] é o quociente "
        "das raízes."),
    dict(id="20", block="ida_volta2", text=
        "{t}E se você faz a raiz [p=0.2] e depois eleva ao quadrado? [p=0.4] {a}Raiz de sete, [p=0.2] ao quadrado. [p=0.4] "
        "{b}A raiz foi a volta, [p=0.2] o quadrado é a ida: [p=0.2] uma desfaz a outra. [p=0.4] {c}Sobra o *sete.* [p=0.3] "
        "{d}Raiz de *a*, [p=0.2] ao quadrado, [p=0.2] é igual a *a.*"),
    dict(id="21", block="raiz_raiz", text=
        "{t}E uma raiz *dentro* de outra raiz? [p=0.3] {a}Raiz quadrada da raiz cúbica de sessenta e quatro. [p=0.4] {b}Por "
        "dentro: [p=0.2] raiz cúbica de sessenta e quatro é *quatro,* [p=0.2] porque quatro ao cubo dá sessenta e quatro. "
        "[p=0.3] {c}Raiz de quatro: [p=0.2] *dois.* [p=0.4] {d}Agora o atalho: [p=0.2] *multiplique os índices.* [p=0.2] Dois "
        "vezes três, [p=0.2] seis. [p=0.3] {e}Raiz sexta de sessenta e quatro é *dois,* [p=0.2] porque dois elevado a seis "
        "dá sessenta e quatro. [p=0.3] Mesma resposta, [p=0.2] num passo só."),

    # ================= BLOCO F: SIMPLIFICAR ÍNDICE E EXPOENTE =================
    dict(id="22", block="dividir_indice", text=
        "{t}Mais um truque: [p=0.2] dá para *encolher* o índice? [p=0.4] {a}Raiz quarta de quatro. [p=0.3] {b}O quatro de "
        "dentro é dois ao quadrado. [p=0.4] {c}Divida o índice *e* o expoente pelo mesmo número, [p=0.2] o dois: [p=0.2] "
        "{d}o índice quatro vira dois, [p=0.2] o expoente dois vira um. [p=0.4] {e}Sobra a raiz quadrada de dois. [p=0.4] "
        "{f}Confira com um caso de conta exata: [p=0.2] raiz quarta de dezesseis é dois, [p=0.2] e raiz de quatro também é "
        "*dois.* [p=0.3] O valor não muda."),

    # ================= BLOCO G: A PROPRIEDADE QUE NÃO EXISTE =================
    dict(id="23", block="soma", text=
        "{t}E a soma? [p=0.2] Lembra do começo da aula? [p=0.4] {a}Raiz de nove mais dezesseis [p=0.2] é raiz de vinte e "
        "cinco: [p=0.2] *cinco.* [p=0.4] {b}Raiz de nove mais raiz de dezesseis [p=0.2] é três mais quatro: [p=0.2] *sete.* "
        "[p=0.4] {c}Cinco não é sete. [p=0.3] {d}A raiz se distribui no produto e na divisão, [p=0.2] *nunca na soma.* "
        "[p=0.2] Nem na subtração. [p=0.4] {e}Atalho: [p=0.2] ficou em dúvida se uma regra existe? [p=0.2] Teste com números "
        "que têm raiz exata, [p=0.2] como nove e dezesseis. [p=0.2] Leva cinco segundos."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="24", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] raiz desfaz a potência. [p=0.5] {b}Dois: [p=0.2] raiz de "
        "índice par devolve sempre o positivo. [p=0.5] {c}Três: [p=0.2] a raiz se distribui no produto e na divisão, "
        "[p=0.2] nunca na soma."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="25", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] raiz de *a mais b* [p=0.2] igual a raiz de *a* mais "
        "raiz de *b.* [p=0.4] {b}Parece certo, [p=0.2] porque com a multiplicação funciona. [p=0.4] {c}Mas o teste desmente: "
        "[p=0.2] raiz de nove mais dezesseis dá *cinco,* [p=0.2] e não sete."),
    dict(id="26", block="erros", text=
        "{a}Segundo: [p=0.2] raiz de *a ao quadrado* [p=0.2] igual a *a,* [p=0.2] esquecendo o módulo. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque a raiz desfaz o quadrado. [p=0.4] {c}Mas com menos cinco: [p=0.2] raiz de vinte e cinco é "
        "*cinco,* [p=0.2] positivo."),
    dict(id="27", block="erros", text=
        "{a}Terceiro: [p=0.2] dizer que raiz de menos quatro [p=0.2] é *menos dois.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque a raiz cúbica de menos oito é menos dois. [p=0.4] {c}Mas menos dois *ao quadrado* dá mais quatro. [p=0.2] "
        "Raiz quadrada de negativo [p=0.2] *não existe* nos reais."),

    # ================= QUESTÃO 8 DO MATERIAL =================
    dict(id="28", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Para *xis* igual a menos "
        "sete, [p=0.2] o valor de raiz de *xis ao quadrado,* [p=0.2] mais raiz cúbica de *xis ao cubo,* [p=0.2] é: [p=0.4] "
        "{qa}A: [p=0.2] menos catorze. [p=0.3] {qb}B: [p=0.2] menos sete. [p=0.3] {qc}C: [p=0.2] zero. [p=0.3] {qd}D: "
        "[p=0.2] sete. [p=0.3] {qe}E: [p=0.2] catorze. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="29", block="questao", text=
        "{t}Vamos resolver, [p=0.2] separando as duas raízes. [p=0.3] {x}O *xis* é só um número escondido: [p=0.2] aqui, "
        "ele vale menos sete. [p=0.4] {a}Primeira parte, [p=0.2] índice *par:* [p=0.2] menos sete ao quadrado é quarenta e "
        "nove, [p=0.2] e a raiz de quarenta e nove é *sete,* [p=0.2] positivo. [p=0.4] {b}Segunda parte, [p=0.2] índice "
        "*ímpar:* [p=0.2] menos sete ao cubo é menos trezentos e quarenta e três, [p=0.2] e a raiz cúbica volta com o sinal: "
        "[p=0.2] *menos sete.* [p=0.4] {c}Sete mais menos sete: [p=0.2] *zero.* [p=0.3] {ok}*Letra C!*"),
    dict(id="30", block="questao", text=
        "{t}E as outras? [p=0.3] {xa}A A, menos catorze, [p=0.2] é de quem achou que raiz de *xis ao quadrado* é *xis,* "
        "[p=0.2] e esqueceu o módulo. [p=0.4] {xe}A E, catorze, [p=0.2] tirou o sinal das *duas* raízes, [p=0.2] até da "
        "cúbica, [p=0.2] que conserva o sinal. [p=0.4] {xd}A D fez só a primeira parte, [p=0.3] {xb}e a B, [p=0.2] só a "
        "segunda."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] raiz desfaz a potência. [p=0.5] {b}Dois: [p=0.2] raiz "
        "de índice par devolve sempre o positivo. [p=0.5] {c}Três: [p=0.2] a raiz se distribui no produto e na divisão, "
        "[p=0.2] nunca na soma."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}Raiz de cinquenta, [p=0.2] cinco raiz de dois, [p=0.2] raiz de vinte e cinco vezes dois: [p=0.3] {b}três jeitos "
        "de escrever o *mesmo número.* [p=0.4] {c}E a prova sempre quer o mais simples. [p=0.4] {d}Próximo episódio: "
        "[p=0.2] *simplificar radicais.*"),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também achava que raiz de nove mais dezesseis dava sete? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
