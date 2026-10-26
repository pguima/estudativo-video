# Roteiro — Expressões Algébricas e Produtos Notáveis, Episódio 2 de 5: produtos notáveis e o sonho do calouro
# Base: Estudos/Enem/estudos/01-matematica/19-expressoes-algebricas-produtos-notaveis.html — seções 04 e 05 + Questões 2, 7 e 9.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O QUADRADO de lado a + b se divide em quatro pedaços: a², b² e DOIS retângulos a · b. O sonho do calouro esquece os dois.
#   O expoente passa pela PORTA da multiplicação, (a · b)² = a² · b², mas fica BARRADO na porta da soma.
#   O TESTE DE 10 SEGUNDOS: na dúvida, troque as letras por números pequenos (2 e 3) e compare.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos: os blocos usam os exemplos do prompt (tabela da seção 04, piso 3 + 4 = 7, raiz de 9 + 16, teste com 1 e 2).
#   NOSSOS: o erro 3 ("termo do meio pela metade") usa (x + 5)² = x² + 5x + 25, conferido com x = 1 (36 contra 31);
#   a conferência do "nós fazemos" usa x = 2: (6 − 2)² = 16 e 36 − 24 + 4 = 16.
# Nós fazemos (prompt): (3x − 2)² = 9x² − 12x + 4 (termo do meio 2 · 3x · 2 = 12x).
# QUESTÃO 2 (texto idêntico na tela): (x + 3)² − x² = 6x + 9 → D. Erradas (material): A 9 = sonho do calouro;
#   B 6x = esqueceu o quadradinho de canto; C 3x + 9 = contou um retângulo só; E = área nova inteira, não o aumento.
# QUESTÃO 7 (texto idêntico): (4x² − 12x + 9) − (4x² + 12x + 9) = −24x → B. Teste x = 1: 1 − 25 = −24.
#   Erradas (material): A 0 = sonho do calouro; C −12x = termo do meio 6x (esqueceu o 2 de 2ab); D 24x = sinal ao tirar
#   o parêntese; E 8x² + 18 = somou os quadrados em vez de subtrair.
# QUESTÃO 9 (texto idêntico): (x + 1)³ − x³ = 3x² + 3x + 1 → D. Teste x = 2: 8 → 27, acréscimo 19 = 12 + 6 + 1.
#   Erradas (material): A 1 = sonho do calouro cúbico; B e C esquecem um termo do meio; E = volume novo inteiro.
# Atalhos (verde): a frase do quadrado ("quadrado do primeiro, duas vezes o primeiro pelo segundo, quadrado do segundo") ·
#   soma pela diferença = quadrado do primeiro menos quadrado do segundo · cubo: coeficientes 1, 3, 3, 1 (na diferença,
#   sinais alternados) · teste de 10 segundos.
# Frases-chave (meio e fim, idênticas): 1. O quadrado da soma tem sempre o termo do meio, 2ab.
#   2. Na multiplicação o expoente entra; na soma, fica barrado. 3. Na dúvida, teste com números.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Produtos notáveis e o sonho do calouro: o termo do meio que o ENEM esconde | Produtos Notáveis Ep. 2"
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
        "{a}*A mais b, ao quadrado,* [p=0.2] igual a *a ao quadrado mais b ao quadrado.* [p=0.5] {b}Essa conta está "
        "*errada,* [p=0.3] {c}é feita por *milhões* de estudantes todo ano [p=0.3] {d}e o ENEM sabe disso: [p=0.3] a "
        "resposta errada está sempre lá, [p=0.2] *esperando por você.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai desenvolver os *produtos notáveis* de cabeça [p=0.3] {b}e enxergar "
        "o *termo do meio* [p=0.2] que a pegadinha esconde."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio um, [p=0.2] a distributiva do *aperto de mão:* "
        "[p=0.2] cada termo de um parêntese cumprimenta cada termo do outro. [p=0.4] {b}E da série de Potenciação: "
        "[p=0.2] na *soma,* [p=0.2] não existe propriedade de potência."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine um piso *quadrado.* [p=0.3] {a}O lado tem três lajotas, [p=0.2] mais quatro lajotas: [p=0.2] "
        "*sete* de lado. [p=0.4] {b}Quantas lajotas no total? [p=0.2] Sete vezes sete: [p=0.2] *quarenta e nove.* "
        "[p=0.4] {c}Agora faça do jeito apressado: [p=0.2] três ao quadrado, nove, [p=0.2] mais quatro ao quadrado, "
        "dezesseis: [p=0.2] *vinte e cinco.* [p=0.4] {d}Ficaram *vinte e quatro* lajotas de fora. [p=0.3] Onde elas "
        "estão?"),

    # ================= BLOCO A: QUADRADO DA SOMA =================
    dict(id="05", block="soma", text=
        "{t}Elas estão em dois retângulos esquecidos. [p=0.4] {a}Um *produto notável* é uma multiplicação que aparece "
        "tanto [p=0.2] que vale a pena guardar o resultado pronto. [p=0.4] {b}O primeiro é o *quadrado da soma:* "
        "[p=0.2] a mais b, ao quadrado. [p=0.4] {c}Desenhe um quadrado de lado *a mais b.* [p=0.2] Ele se divide em "
        "quatro pedaços: [p=0.2] {d}o quadrado *a ao quadrado,* [p=0.2] o quadrado *b ao quadrado* [p=0.2] {e}e "
        "*dois* retângulos *a vezes b.* [p=0.4] {f}Somando: [p=0.2] a ao quadrado, [p=0.2] mais *dois a b,* [p=0.2] "
        "mais b ao quadrado."),
    dict(id="06", block="soma", text=
        "{t}E o *dois a b* do meio tem nome: [p=0.2] *termo do meio.* [p=0.4] {a}Confira pela distributiva: [p=0.2] a "
        "mais b, vezes a mais b. [p=0.4] {b}a vezes a, [p=0.2] a ao quadrado. [p=0.2] a vezes b, [p=0.2] *a b.* "
        "[p=0.2] b vezes a, [p=0.2] *outro a b.* [p=0.2] b vezes b, [p=0.2] b ao quadrado. [p=0.4] {c}Os dois *a b* "
        "se juntam: [p=0.2] *dois a b.*"),
    dict(id="07", block="soma", text=
        "{t}Atalho: [p=0.2] uma frase. [p=0.4] {a}*O quadrado do primeiro, [p=0.2] duas vezes o primeiro pelo "
        "segundo, [p=0.2] o quadrado do segundo.* [p=0.5] {b}Teste com x mais cinco, ao quadrado. [p=0.3] {c}Quadrado "
        "do primeiro: [p=0.2] *x ao quadrado.* [p=0.3] {d}Duas vezes o primeiro pelo segundo: [p=0.2] dois vezes x "
        "vezes cinco, [p=0.2] *dez x.* [p=0.3] {e}Quadrado do segundo: [p=0.2] *vinte e cinco.*"),

    # ================= BLOCO B: QUADRADO DA DIFERENÇA =================
    dict(id="08", block="diferenca", text=
        "{t}E se for *menos?* [p=0.2] O que muda? [p=0.4] {a}O *quadrado da diferença* é a menos b, ao quadrado. "
        "[p=0.4] {b}Resultado: [p=0.2] a ao quadrado, [p=0.2] *menos* dois a b, [p=0.2] mais b ao quadrado. [p=0.4] "
        "{c}Só o termo do meio troca de sinal. [p=0.3] {d}E o b ao quadrado continua *positivo:* [p=0.2] menos b "
        "vezes menos b [p=0.2] dá mais."),

    # ================= BLOCO C: SOMA PELA DIFERENÇA =================
    dict(id="09", block="somadif", text=
        "{t}E se você multiplicar a *soma* pela *diferença?* [p=0.4] {a}O *produto da soma pela diferença* é a mais "
        "b, vezes a menos b. [p=0.4] {b}Aperto de mão: [p=0.2] a ao quadrado, [p=0.2] *menos a b,* [p=0.2] *mais a "
        "b,* [p=0.2] menos b ao quadrado. [p=0.4] {c}O menos a b e o mais a b [p=0.2] *se cancelam.* [p=0.3] {d}Sobra "
        "a ao quadrado menos b ao quadrado. [p=0.4] {e}Atalho: [p=0.2] *quadrado do primeiro menos quadrado do "
        "segundo.* [p=0.2] x mais sete, vezes x menos sete: [p=0.2] *x ao quadrado menos quarenta e nove.*"),

    # ================= BLOCO D: A TABELA =================
    dict(id="10", block="tabela", text=
        "{t}E quando o primeiro termo tem um número na frente? [p=0.4] {a}Dois x menos três, ao quadrado. [p=0.4] "
        "{b}Quadrado do primeiro: [p=0.2] dois x ao quadrado [p=0.2] é *quatro x ao quadrado,* [p=0.2] porque o dois "
        "também é elevado. [p=0.4] {c}Duas vezes o primeiro pelo segundo: [p=0.2] dois vezes dois x vezes três, "
        "[p=0.2] *doze x,* [p=0.2] com o sinal de menos. [p=0.4] {d}Quadrado do segundo: [p=0.2] *mais nove,* [p=0.2] "
        "positivo. [p=0.4] {e}O mesmo molde aparece nos *juros compostos:* [p=0.2] um mais i, ao quadrado."),

    # ================= BLOCO E: O CUBO =================
    dict(id="11", block="cubo", text=
        "{t}E se o expoente for *três?* [p=0.4] {a}O *cubo da soma:* [p=0.2] a mais b, ao cubo, [p=0.2] é a ao cubo, "
        "[p=0.2] mais *três* a ao quadrado b, [p=0.2] mais *três* a b ao quadrado, [p=0.2] mais b ao cubo. [p=0.4] "
        "{b}No *cubo da diferença,* [p=0.2] os sinais se alternam: [p=0.2] *mais, menos, mais, menos.* [p=0.5] "
        "{c}Atalho: [p=0.2] os números da frente são *um, três, três, um.* [p=0.3] {d}O expoente do a desce; [p=0.2] "
        "o do b sobe."),

    # ================= BLOCO F: O SONHO DO CALOURO =================
    dict(id="12", block="calouro", text=
        "{t}E aquele erro do começo? [p=0.4] {a}Esse erro tem apelido: [p=0.2] *sonho do calouro.* [p=0.4] {b}Ele "
        "parece certo porque, na *multiplicação,* funciona: [p=0.2] a vezes b, ao quadrado, [p=0.2] é a ao quadrado "
        "vezes b ao quadrado. [p=0.4] {c}O expoente *passa pela porta* da multiplicação. [p=0.3] {d}Mas fica "
        "*barrado* na porta da soma."),
    dict(id="13", block="calouro", text=
        "{t}Veja com números. [p=0.3] {a}Três mais quatro, sete; [p=0.2] sete ao quadrado, *quarenta e nove.* [p=0.2] "
        "Três ao quadrado mais quatro ao quadrado, *vinte e cinco.* [p=0.4] {b}A diferença, vinte e quatro, [p=0.2] é "
        "o *dois a b.* [p=0.5] {c}E a raiz cai na mesma armadilha: [p=0.2] raiz de nove mais dezesseis [p=0.2] é raiz "
        "de vinte e cinco, *cinco.* [p=0.3] {d}Mas raiz de nove mais raiz de dezesseis [p=0.2] é três mais quatro, "
        "*sete.*"),

    # ================= BLOCO G: TESTE DE 10 SEGUNDOS =================
    dict(id="14", block="teste", text=
        "{t}E como não cair nunca mais? [p=0.4] {a}O *teste de dez segundos.* [p=0.3] *Expressões equivalentes* são "
        "as que dão o *mesmo* resultado para qualquer número. [p=0.4] {b}Na dúvida, [p=0.2] troque as letras por "
        "números pequenos. [p=0.3] {c}Com a igual a um e b igual a dois: [p=0.2] um mais dois, ao quadrado, [p=0.2] "
        "*nove.* [p=0.2] Um ao quadrado mais dois ao quadrado, [p=0.2] *cinco.* [p=0.3] Deu diferente: [p=0.2] *não* "
        "são iguais. [p=0.4] {d}Só evite *zero* e *um* sozinhos: [p=0.2] eles escondem diferenças."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Desenvolva *três x menos dois, ao quadrado.* [p=0.3] Use a frase. [p=0.3] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Quadrado do primeiro: [p=0.2] três x ao quadrado, [p=0.2] *nove x ao quadrado.* "
        "[p=0.4] {b}Duas vezes o primeiro pelo segundo: [p=0.2] dois vezes três x vezes dois, [p=0.2] *doze x,* "
        "[p=0.2] com sinal de menos. [p=0.4] {c}Quadrado do segundo: [p=0.2] *mais quatro.* [p=0.4] {d}Teste com x "
        "igual a dois: [p=0.2] seis menos dois, ao quadrado, dezesseis. [p=0.2] Trinta e seis, menos vinte e quatro, "
        "mais quatro: [p=0.2] *dezesseis.* [p=0.3] {ok}*Bateu!*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Três frases para guardar. [p=0.5] {a}Um: [p=0.2] o quadrado da soma tem sempre o termo do meio, [p=0.2] "
        "dois a b. [p=0.5] {b}Dois: [p=0.2] na multiplicação o expoente entra; [p=0.2] na soma, fica barrado. [p=0.5] "
        "{c}Três: [p=0.2] na dúvida, teste com números."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{a}Erro número um: [p=0.2] a mais b, ao quadrado, [p=0.2] igual a a ao quadrado mais b ao quadrado. [p=0.4] "
        "{b}Parece certo porque o expoente *entra* na multiplicação, [p=0.2] e a gente acha que entra em tudo. "
        "[p=0.4] {c}Correção: [p=0.2] faltam os *dois retângulos.* [p=0.2] Escreva sempre o *dois a b.*"),
    dict(id="19", block="erros", text=
        "{a}Erro número dois: [p=0.2] a menos b, ao quadrado, [p=0.2] igual a a ao quadrado *menos* b ao quadrado. "
        "[p=0.4] {b}Parece certo porque é tão curtinho [p=0.2] e existe mesmo um produto com esse resultado. [p=0.4] "
        "{c}Correção: [p=0.2] esse é o resultado da *soma pela diferença.* [p=0.2] O quadrado da diferença tem o "
        "*menos dois a b.*"),
    dict(id="20", block="erros", text=
        "{a}Erro número três: [p=0.2] o *termo do meio pela metade.* [p=0.4] {a2}x mais cinco, ao quadrado, [p=0.2] "
        "virando x ao quadrado, mais *cinco x,* mais vinte e cinco. [p=0.4] {b}Parece certo porque *tem* termo do "
        "meio; [p=0.2] só esqueceram o *dois.* [p=0.4] {c}Correção: [p=0.2] são *dois* retângulos: [p=0.2] *dez x.* "
        "[p=0.3] Teste com x igual a um: [p=0.2] trinta e seis contra trinta e um."),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="21", block="q2", text=
        "{t}Hora de questão. [p=0.3] {a}Um terreno *quadrado* tem lado de *x metros.* [p=0.2] O proprietário vai "
        "aumentar cada lado em *três metros,* [p=0.2] mantendo a forma quadrada. [p=0.2] O *aumento* da área do "
        "terreno, em metros quadrados, é dado por: [p=0.4] {qa}A: [p=0.2] nove. [p=0.3] {qb}B: [p=0.2] seis x. "
        "[p=0.3] {qc}C: [p=0.2] três x mais nove. [p=0.3] {qd}D: [p=0.2] seis x mais nove. [p=0.3] {qe}E: [p=0.2] x "
        "ao quadrado, mais seis x, mais nove. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q2", text=
        "{t}Eu faço com você. [p=0.3] {a}Pelo desenho: [p=0.2] o terreno cresce três metros para a direita [p=0.2] e "
        "três para baixo. [p=0.4] {b}A área nova tem *duas faixas* de três por x, [p=0.2] *três x* cada, [p=0.2] {c}e "
        "um *quadradinho de canto,* [p=0.2] três por três, *nove.* [p=0.4] {d}Aumento: [p=0.2] *seis x mais nove.* "
        "[p=0.4] {e}Pela conta: [p=0.2] x mais três, ao quadrado, [p=0.2] menos o x ao quadrado antigo: [p=0.2] o "
        "mesmo seis x mais nove. [p=0.3] {ok}*Letra D!*"),
    dict(id="23", block="q2", text=
        "{t}E as erradas? [p=0.3] {xa}A A, [p=0.2] nove, [p=0.2] é o *sonho do calouro:* [p=0.2] sem os retângulos, "
        "sobra só o quadradinho. [p=0.4] {xb}A B [p=0.2] esqueceu o *quadradinho de canto.* [p=0.4] {xc}A C [p=0.2] "
        "contou *um retângulo só.* [p=0.4] {xe}E a E [p=0.2] é a área nova *inteira,* [p=0.2] não o aumento."),

    # ================= QUESTÃO 7 (NÓS FAZEMOS) =================
    dict(id="24", block="q7", text=
        "{t}Agora fazemos juntos. [p=0.3] {a}A expressão *dois x menos três, ao quadrado,* [p=0.2] *menos dois x mais "
        "três, ao quadrado,* [p=0.2] é equivalente a: [p=0.4] {qa}A: [p=0.2] zero. [p=0.3] {qb}B: [p=0.2] menos vinte "
        "e quatro x. [p=0.3] {qc}C: [p=0.2] menos doze x. [p=0.3] {qd}D: [p=0.2] vinte e quatro x. [p=0.3] {qe}E: "
        "[p=0.2] oito x ao quadrado, mais dezoito. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q7", text=
        "{t}Os dois quadrados, pela frase. [p=0.3] {a}O primeiro já é nosso conhecido: [p=0.2] *quatro x ao quadrado, "
        "menos doze x, mais nove.* [p=0.4] {b}O segundo: [p=0.2] *quatro x ao quadrado, mais doze x, mais nove.* "
        "[p=0.4] {c}Subtraia: [p=0.2] o menos entra no parêntese inteiro. [p=0.2] Os quatro x ao quadrado e os noves "
        "se cancelam, [p=0.2] e sobra menos doze x, menos doze x: [p=0.2] *menos vinte e quatro x.* [p=0.4] {d}Teste "
        "com x igual a um: [p=0.2] um, menos vinte e cinco, [p=0.2] *menos vinte e quatro.* [p=0.3] {ok}*Letra B!*"),
    dict(id="26", block="q7", text=
        "{t}E as erradas? [p=0.3] {xa}A A, [p=0.2] zero, [p=0.2] é o sonho do calouro: [p=0.2] sem os termos do meio, "
        "tudo se cancela. [p=0.4] {xc}A C usou *seis x* como termo do meio: [p=0.2] esqueceu o dois de dois a b. "
        "[p=0.4] {xd}A D errou o *sinal* ao tirar o parêntese. [p=0.4] {xe}E a E *somou* os quadrados em vez de "
        "subtrair."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="27", block="q9", text=
        "{t}E esta é *sua.* [p=0.3] {a}Um reservatório tem a forma de um *cubo* de aresta *x metros.* [p=0.2] Num "
        "projeto de ampliação, a aresta será aumentada em *um metro.* [p=0.2] O *acréscimo* de volume, em metros "
        "cúbicos, será: [p=0.4] {qa}A: [p=0.2] um. [p=0.3] {qb}B: [p=0.2] três x mais um. [p=0.3] {qc}C: [p=0.2] três "
        "x ao quadrado, mais um. [p=0.3] {qd}D: [p=0.2] três x ao quadrado, mais três x, mais um. [p=0.3] {qe}E: "
        "[p=0.2] x ao cubo, mais três x ao quadrado, mais três x, mais um. [p=0.5] {p}*Pause o vídeo e resolva.* "
        "[p=2.0]"),
    dict(id="28", block="q9", text=
        "{t}Conferindo. [p=0.3] {a}Volume novo menos volume antigo: [p=0.2] x mais um, ao cubo, [p=0.2] menos x ao "
        "cubo. [p=0.4] {b}Pelo cubo da soma, com um, três, três, um: [p=0.2] x ao cubo, mais três x ao quadrado, mais "
        "três x, mais um. [p=0.4] {c}Tire o x ao cubo: [p=0.2] *três x ao quadrado, mais três x, mais um.* [p=0.4] "
        "{d}Teste com x igual a dois: [p=0.2] o volume vai de oito para vinte e sete, [p=0.2] acréscimo de "
        "*dezenove.* [p=0.2] E doze, mais seis, mais um, [p=0.2] *dezenove.* [p=0.3] {ok}*Letra D!*"),
    dict(id="29", block="q9", text=
        "{t}E as outras? [p=0.3] {xa}A A, [p=0.2] um, [p=0.2] é o sonho do calouro em versão *cúbica.* [p=0.4] {xb}A "
        "B [p=0.2] {xc}e a C [p=0.2] esqueceram *um* dos termos do meio. [p=0.4] {xe}E a E [p=0.2] é o volume novo "
        "*inteiro,* [p=0.2] não o acréscimo."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] o quadrado da soma tem sempre o termo do meio, "
        "[p=0.2] dois a b. [p=0.5] {b}Dois: [p=0.2] na multiplicação o expoente entra; [p=0.2] na soma, fica barrado. "
        "[p=0.5] {c}Três: [p=0.2] na dúvida, teste com números."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}E se o caminho for o *contrário:* [p=0.2] alguém te dá *x ao quadrado menos vinte e cinco* [p=0.2] e pede "
        "para escrever como *multiplicação?* [p=0.5] {b}Próximo episódio: [p=0.2] *fatoração.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] você já tinha caído no sonho do calouro? [p=0.5] {anki}E tem mais: [p=0.2] na "
        "*descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o "
        "aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, "
        "e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
