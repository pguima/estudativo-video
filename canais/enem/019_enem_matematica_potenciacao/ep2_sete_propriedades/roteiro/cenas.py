# Roteiro — Potenciação e Radiciação, Episódio 2 de 7: As sete propriedades da potenciação (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/04-potenciacao-radiciacao.html — seção 03 (+ Questão 1 da seção 12
#       e a questão extra (2³ · 4²) / 8 enviada pelo usuário).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   FILA DE FATORES: potência é uma fila de fatores iguais; multiplicar JUNTA as filas (soma), dividir CANCELA
#   fatores em pares (subtrai), potência de potência COPIA a fila (multiplica).
#   MESMA FRUTA: só dá para juntar filas da mesma fruta → primeiro transforme tudo na mesma base (2, 4, 8, 16, 32 → base 2).
#   TESTE COM 2 E 3: na dúvida, troque por números pequenos e confira (cinco segundos).
# Propriedades abertas antes da regra: 2³·2⁴ = 2⁷ · 2⁷÷2³ = 2⁴ · (2³)² = 2⁶ · (2·5)³ = 2³·5³ (= 1000) ·
#   (2/3)³ = 8/27 · a³÷a³ = a⁰ = 1 · a²÷a⁵ = 1/a³ = a⁻³ (3⁻² = 1/9).
# Falsas propriedades (selo de teste): 2² + 2³ = 12 ≠ 2⁵ = 32 · (2+3)² = 25 ≠ 4 + 9 = 13 · (2³)² = 64 ≠ 2^(3²) = 2⁹ = 512.
# QUESTÃO EXTRA (eu faço): (2³ · 4²) / 8 → 4² = (2²)² = 2⁴, 8 = 2³ → 2⁷ / 2³ = 2⁴ = 16 → D.
#   Explicações NOSSAS: B (4) = escreveu o 4 como 2² e esqueceu o ² de fora (2³·2²/2³ = 2²); C (8) = fez 4² = 4 · 2 = 8
#   (o erro de partida); A (2) e E (32) não saem de nenhum caminho certo (o teste 8 · 16 = 128, ÷ 8 = 16 elimina).
# QUESTÃO 1 do material (você faz; texto idêntico na tela): (2⁵ · 4³) / 8² → 2⁵ · 2⁶ / 2⁶ = 2⁵ = 32 → C.
#   Explicações NOSSAS (o material não comenta as erradas): B (16) = somou na potência de potência do 4³ (2⁵);
#   D (64) = somou na do 8² (2⁵); E (128) = fez 8² = 8 · 2 = 16 = 2⁴; A (8) não sai de nenhum caminho certo.
#   Conferência com números: 4³ = 64 e 8² = 64 → o quociente é 1 → sobra 2⁵ = 32.
# Frases-chave (meio e fim, idênticas):
#   1. Multiplicou mesma base: soma. Dividiu: subtrai. Potência de potência: multiplica.
#   2. Primeiro tudo na mesma base.
#   3. Na soma não existe propriedade. Na dúvida, teste com 2 e 3.
# Atalhos (verde): "mesma base multiplicando? copie a base e some" · "dividindo: de cima menos de baixo" ·
#   "potência de potência: multiplique" · "o expoente de fora entra em cada fator" · "dobrando: 2, 4, 8, 16, 32 =
#   2¹ a 2⁵" · "teste com 2 e 3".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "As 7 propriedades da potência (sem decorar nenhuma) | Potenciação Ep. 2"
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
        "{a}Sete regras. [p=0.3] *Só sete.* [p=0.5] {b}Com elas, [p=0.2] você simplifica qualquer expressão de potência "
        "da prova. [p=0.5] {c}E não precisa decorar nenhuma, [p=0.3] porque vai ver *de onde cada uma vem.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai aplicar as sete propriedades *sem pensar,* [p=0.4] {b}e vai saber "
        "*quando elas não valem.* [p=0.4] {c}Que é exatamente onde a prova tenta te pegar."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes do episódio um. [p=0.3] {a}Potência é uma *fila de fatores iguais:* [p=0.2] dois "
        "elevado a três é dois vezes dois vezes dois. [p=0.4] {b}Qualquer número, [p=0.2] menos o zero, [p=0.2] "
        "elevado a zero dá *um.* [p=0.4] {c}E expoente negativo *inverte:* [p=0.2] dois elevado a menos três é um oitavo."),
    dict(id="04", block="prereq", text=
        "{t}E uma palavra nova: [p=0.2] *propriedade.* [p=0.3] {a}Propriedade é uma regra que vale *sempre,* [p=0.2] "
        "para qualquer número. [p=0.4] {b}Ela não é uma lei inventada: [p=0.2] é um *atalho* para uma conta que você já "
        "sabe fazer. [p=0.4] {c}Por isso, [p=0.2] a gente vai *abrir* cada potência antes de ver a regra."),

    # ================= PROPRIEDADE 1: PRODUTO DE MESMA BASE =================
    dict(id="05", block="p1", text=
        "{t}Quanto é dois ao cubo [p=0.2] vezes dois elevado a quatro? [p=0.4] {a}Vamos abrir. [p=0.2] Dois ao cubo é "
        "uma fila de *três* dois. [p=0.3] {b}Dois elevado a quatro, [p=0.2] uma fila de *quatro* dois. [p=0.4] {c}Multiplicar "
        "é *juntar as filas.* [p=0.3] {d}Conte: [p=0.2] *sete* dois. [p=0.3] {e}Dois elevado a sete."),
    dict(id="06", block="p1", text=
        "{t}Repare: [p=0.2] três mais quatro, [p=0.2] sete. [p=0.4] {a}Os expoentes *se somaram.* [p=0.4] {b}Essa é a "
        "propriedade um: [p=0.2] *a elevado a m, [p=0.2] vezes a elevado a n, [p=0.2] é a elevado a m mais n.* [p=0.4] "
        "{c}O *a* é a base, [p=0.2] e o *m* e o *n* são os expoentes. [p=0.4] {d}*Mesma base* quer dizer o mesmo número "
        "embaixo, [p=0.2] nas duas potências. [p=0.4] {e}Atalho: [p=0.2] mesma base multiplicando? [p=0.2] Copie a base "
        "*e some os expoentes.*"),

    # ================= PROPRIEDADE 2: QUOCIENTE DE MESMA BASE =================
    dict(id="07", block="p2", text=
        "{t}E dividir? [p=0.2] Dois elevado a sete, [p=0.2] dividido por dois ao cubo. [p=0.4] {a}Escreva como fração: "
        "[p=0.2] sete dois em cima, [p=0.2] três dois embaixo. [p=0.4] {b}Agora *cancele em pares:* [p=0.2] um dois de cima "
        "com um dois de baixo, [p=0.2] porque dois dividido por dois dá um. [p=0.4] {c}Três pares somem. [p=0.3] "
        "{d}Sobram *quatro* dois em cima: [p=0.2] dois elevado a quatro."),
    dict(id="08", block="p2", text=
        "{t}Sete menos três, [p=0.2] quatro. [p=0.4] {a}Na divisão, [p=0.2] os expoentes *se subtraem.* [p=0.4] {b}Propriedade "
        "dois: [p=0.2] *a elevado a m, [p=0.2] dividido por a elevado a n, [p=0.2] é a elevado a m menos n.* [p=0.4] {c}O "
        "resultado de uma divisão tem um nome: [p=0.2] *quociente.* [p=0.4] {d}Atalho: [p=0.2] dividiu mesma base? [p=0.2] "
        "Expoente de cima *menos* o de baixo."),

    # ================= PROPRIEDADE 3: POTÊNCIA DE POTÊNCIA =================
    dict(id="09", block="p3", text=
        "{t}E quando uma potência inteira é elevada de novo? [p=0.3] Dois ao cubo, [p=0.2] tudo ao quadrado. [p=0.4] "
        "{a}Isso se chama *potência de potência.* [p=0.4] {b}Ao quadrado quer dizer: [p=0.2] a fila aparece *duas vezes.* "
        "[p=0.4] {c}A fila de três dois é *copiada:* [p=0.2] três, [p=0.2] mais três. [p=0.4] {d}*Seis* dois. [p=0.3] Dois "
        "elevado a seis."),
    dict(id="10", block="p3", text=
        "{t}Três copiado duas vezes: [p=0.2] três vezes dois, [p=0.2] seis. [p=0.4] {a}Aqui os expoentes se *multiplicam.* "
        "[p=0.4] {b}Propriedade três: [p=0.2] *a elevado a m, [p=0.2] tudo elevado a n, [p=0.2] é a elevado a m vezes n.* "
        "[p=0.4] {c}Atalho: [p=0.2] viu um expoente do lado de fora do parêntese, [p=0.2] em cima de outro? [p=0.2] "
        "*Multiplique os dois.*"),

    # ================= PROPRIEDADE 4: POTÊNCIA DE UM PRODUTO =================
    dict(id="11", block="p4", text=
        "{t}E se dentro do parêntese tiver uma multiplicação? [p=0.3] Dois vezes cinco, [p=0.2] tudo ao cubo. [p=0.4] "
        "{a}Abra: [p=0.2] dois vezes cinco, [p=0.2] três vezes seguidas. [p=0.4] {b}Na multiplicação, [p=0.2] a ordem não "
        "importa. [p=0.2] Então junte os dois de um lado [p=0.2] {c}e os cinco do outro. [p=0.4] {d}Dois ao cubo, [p=0.2] "
        "vezes cinco ao cubo."),
    dict(id="12", block="p4", text=
        "{t}O expoente de fora *se distribuiu:* [p=0.2] distribuir é entregar para cada um que está dentro. [p=0.4] "
        "{a}Propriedade quatro: [p=0.2] *a vezes b, [p=0.2] tudo elevado a n, [p=0.2] é a elevado a n, [p=0.2] vezes b "
        "elevado a n.* [p=0.4] {b}Confira com números: [p=0.2] dez ao cubo é mil. [p=0.3] {c}Oito vezes cento e vinte e "
        "cinco, [p=0.2] também *mil.* [p=0.4] {d}Atalho: [p=0.2] o expoente de fora *entra em cada fator* de dentro."),

    # ================= PROPRIEDADE 5: POTÊNCIA DE UM QUOCIENTE =================
    dict(id="13", block="p5", text=
        "{t}E com uma fração dentro do parêntese? [p=0.3] Dois terços ao cubo. [p=0.4] {a}Abra: [p=0.2] dois terços, "
        "[p=0.2] três vezes. [p=0.4] {b}Fração vezes fração: [p=0.2] em cima com em cima, [p=0.2] embaixo com embaixo. "
        "[p=0.4] {c}Em cima, [p=0.2] dois ao cubo, [p=0.2] *oito.* [p=0.3] Embaixo, [p=0.2] três ao cubo, [p=0.2] *vinte e "
        "sete.* [p=0.4] {d}Propriedade cinco: [p=0.2] *a sobre b, [p=0.2] elevado a n, [p=0.2] é a elevado a n [p=0.2] sobre "
        "b elevado a n.* [p=0.3] O expoente vai para os dois andares."),

    # ================= PROPRIEDADES 6 E 7 =================
    dict(id="14", block="p6", text=
        "{t}E as duas últimas, [p=0.2] você já conhece. [p=0.3] {a}Olhe: [p=0.2] a ao cubo, [p=0.2] dividido por a ao "
        "cubo. [p=0.4] {b}Pela propriedade dois, [p=0.2] três menos três, [p=0.2] *a elevado a zero.* [p=0.4] {c}Mas todo "
        "número dividido por ele mesmo dá *um.* [p=0.4] {d}Então a elevado a zero é um: [p=0.2] *propriedade seis.* "
        "[p=0.3] {e}É o mesmo degrau da escada do episódio um."),
    dict(id="15", block="p7", text=
        "{t}E se embaixo tiver *mais* fatores que em cima? [p=0.3] {a}A ao quadrado, [p=0.2] dividido por a elevado a "
        "cinco. [p=0.4] {b}Cancelando os pares, [p=0.2] sobram *três* a embaixo: [p=0.2] um sobre a ao cubo. [p=0.4] "
        "{c}E pela propriedade dois, [p=0.2] dois menos cinco, [p=0.2] *menos três.* [p=0.4] {d}Então a elevado a menos "
        "três é um sobre a ao cubo: [p=0.2] *propriedade sete.* [p=0.3] {e}Três elevado a menos dois? [p=0.2] Um nono."),
    dict(id="16", block="tabela", text=
        "{t}Pronto: [p=0.2] as sete, [p=0.2] lado a lado. [p=0.4] {a}Produto, [p=0.2] soma. [p=0.2] {b}Quociente, "
        "[p=0.2] subtrai. [p=0.2] {c}Potência de potência, [p=0.2] multiplica. [p=0.3] {d}Expoente de fora, [p=0.2] entra "
        "em cada fator e em cada andar. [p=0.3] {e}Zero dá um, [p=0.2] e negativo inverte. [p=0.4] {f}Nenhuma decorada: "
        "[p=0.2] todas *abertas.*"),

    # ================= A CONDIÇÃO QUE NINGUÉM LÊ =================
    dict(id="17", block="condicao", text=
        "{t}Agora, a condição que ninguém lê. [p=0.4] {a}As propriedades um e dois só valem com a *mesma base.* [p=0.4] "
        "{b}É como juntar filas de fruta: [p=0.2] três maçãs com quatro maçãs dá uma fila de sete maçãs. [p=0.3] {c}Mas "
        "dois ao cubo vezes três elevado a quatro? [p=0.2] Maçã com laranja: [p=0.2] *não vira uma fila só.* [p=0.4] "
        "{d}Já as propriedades quatro e cinco [p=0.2] exigem o *mesmo expoente.*"),

    # ================= O PRIMEIRO MOVIMENTO: MESMA BASE =================
    dict(id="18", block="mesma_base", text=
        "{t}Então, qual é o primeiro movimento em toda expressão? [p=0.4] {a}Transformar tudo *na mesma fruta.* [p=0.4] "
        "{b}Se aparecem dois, [p=0.2] quatro, [p=0.2] oito, [p=0.2] dezesseis e trinta e dois, [p=0.3] {c}todos viram "
        "potência de dois. [p=0.4] {d}Quatro é dois ao quadrado. [p=0.2] Oito, [p=0.2] dois ao cubo. [p=0.2] Dezesseis, "
        "[p=0.2] dois elevado a quatro. [p=0.2] Trinta e dois, [p=0.2] dois elevado a cinco."),
    dict(id="19", block="mesma_base", text=
        "{t}E um atalho para não errar. [p=0.3] {a}Comece no dois [p=0.2] e vá *dobrando:* [p=0.2] dois, [p=0.2] quatro, "
        "[p=0.2] oito, [p=0.2] dezesseis, [p=0.2] trinta e dois. [p=0.4] {b}A posição na fila [p=0.2] é o expoente. "
        "[p=0.3] {c}O oito é o terceiro? [p=0.2] Dois ao cubo."),

    # ================= TRÊS COISAS QUE NÃO EXISTEM =================
    dict(id="20", block="falsas", text=
        "{t}Agora, três regras que *parecem* existir. [p=0.3] Mas não existem. [p=0.4] {a}Primeira: [p=0.2] a elevado a "
        "m, [p=0.2] *mais* a elevado a n, [p=0.2] daria a elevado a m mais n? [p=0.4] {b}Teste com números pequenos. "
        "[p=0.2] Dois ao quadrado mais dois ao cubo: [p=0.2] quatro mais oito, [p=0.2] *doze.* [p=0.4] {c}Dois elevado a "
        "cinco: [p=0.2] *trinta e dois.* [p=0.3] {d}Não bate. [p=0.2] Na *soma,* [p=0.2] não existe propriedade nenhuma."),
    dict(id="21", block="falsas", text=
        "{t}Segunda: [p=0.2] a mais b, [p=0.2] ao quadrado, [p=0.2] daria a ao quadrado mais b ao quadrado? [p=0.4] "
        "{a}Teste: [p=0.2] dois mais três é cinco, [p=0.2] e cinco ao quadrado é *vinte e cinco.* [p=0.4] {b}Quatro mais "
        "nove, [p=0.2] *treze.* [p=0.3] {c}Não bate. [p=0.2] O expoente entra em cada fator de uma *multiplicação,* "
        "[p=0.2] não de uma soma."),
    dict(id="22", block="falsas", text=
        "{t}Terceira: [p=0.2] dois ao cubo, [p=0.2] tudo ao quadrado, [p=0.2] é igual a dois elevado a três ao quadrado? "
        "[p=0.4] {a}O primeiro é potência de potência: [p=0.2] dois elevado a seis, [p=0.2] *sessenta e quatro.* [p=0.4] "
        "{b}O segundo é uma *torre:* [p=0.2] o expoente tem o próprio expoente. [p=0.3] {c}E a torre se resolve *de cima "
        "para baixo:* [p=0.2] três ao quadrado é nove, [p=0.2] e dois elevado a nove [p=0.2] é *quinhentos e doze.*"),
    dict(id="23", block="teste", text=
        "{t}Viu o que salvou a gente nas três? [p=0.4] {a}O *teste com números pequenos.* [p=0.4] {b}Não lembra se uma "
        "regra existe? [p=0.2] Troque as letras por dois e três, [p=0.2] e faça a conta dos dois lados. [p=0.4] {c}Leva "
        "*cinco segundos,* [p=0.2] e é muito melhor do que apostar."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="24", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] multiplicou mesma base, [p=0.2] soma. [p=0.2] Dividiu, "
        "[p=0.2] subtrai. [p=0.2] Potência de potência, [p=0.2] multiplica. [p=0.5] {b}Dois: [p=0.2] primeiro, [p=0.2] tudo "
        "na mesma base. [p=0.5] {c}Três: [p=0.2] na soma não existe propriedade. [p=0.2] Na dúvida, [p=0.2] teste com dois "
        "e três."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="25", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] somar os expoentes numa *soma* de potências. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a regra de somar expoentes existe. [p=0.4] {c}Mas ela é do *produto:* "
        "[p=0.2] dois ao quadrado mais dois ao cubo é doze, [p=0.2] não trinta e dois."),
    dict(id="26", block="erros", text=
        "{a}Segundo: [p=0.2] dois ao cubo, [p=0.2] ao quadrado, [p=0.2] virar dois elevado a *cinco.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque somar expoentes é a regra mais famosa. [p=0.4] {c}Mas a fila foi *copiada:* [p=0.2] três vezes "
        "dois, [p=0.2] dois elevado a *seis.*"),
    dict(id="27", block="erros", text=
        "{a}Terceiro: [p=0.2] a mais b ao quadrado, [p=0.2] igual a a ao quadrado mais b ao quadrado. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque com multiplicação funciona. [p=0.4] {c}Mas com soma, [p=0.2] não: [p=0.2] o teste deu "
        "vinte e cinco contra treze."),
    dict(id="28", block="erros", text=
        "{a}Quarto: [p=0.2] usar as propriedades com *bases diferentes.* [p=0.4] {b}Parece certo, [p=0.2] porque são "
        "todas potências. [p=0.4] {c}Mas maçã com laranja não junta: [p=0.2] transforme *primeiro* tudo na mesma base."),

    # ================= QUESTÃO EXTRA (EU FAÇO) =================
    dict(id="29", block="extra", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] e eu resolvo com você. [p=0.4] {a}Simplificando a expressão "
        "[p=0.2] dois ao cubo vezes quatro ao quadrado, [p=0.2] dividido por oito, [p=0.2] obtém-se: [p=0.4] {qa}A: "
        "[p=0.2] dois. [p=0.3] {qb}B: [p=0.2] quatro. [p=0.3] {qc}C: [p=0.2] oito. [p=0.3] {qd}D: [p=0.2] dezesseis. "
        "[p=0.3] {qe}E: [p=0.2] trinta e dois."),
    dict(id="30", block="extra", text=
        "{t}Primeiro movimento: [p=0.2] *tudo na mesma base.* [p=0.4] {a}Quatro é dois ao quadrado. [p=0.2] Então quatro ao "
        "quadrado é dois ao quadrado, [p=0.2] ao quadrado: [p=0.2] potência de potência, [p=0.2] *dois elevado a quatro.* "
        "[p=0.4] {b}E oito é dois ao cubo. [p=0.4] {c}Em cima, [p=0.2] dois ao cubo vezes dois elevado a quatro: [p=0.2] soma, "
        "[p=0.2] *dois elevado a sete.* [p=0.4] {d}Dividido por dois ao cubo: [p=0.2] subtrai, [p=0.2] *dois elevado a "
        "quatro.* [p=0.3] {e}Dezesseis. [p=0.2] {ok}*Letra D!*"),
    dict(id="31", block="extra", text=
        "{t}E as outras? [p=0.3] {xb}A B é de quem escreveu o quatro como dois ao quadrado [p=0.2] e *esqueceu* o ao "
        "quadrado de fora. [p=0.4] {xc}A C é de quem fez quatro ao quadrado como quatro vezes dois: [p=0.2] o erro de "
        "partida. [p=0.4] {xa}A A e a E não saem de nenhum caminho certo. [p=0.3] {xe}E o teste confirma: [p=0.2] oito "
        "vezes dezesseis, [p=0.2] cento e vinte e oito, [p=0.2] dividido por oito, [p=0.2] *dezesseis.*"),

    # ================= QUESTÃO 1 DO MATERIAL (VOCÊ FAZ) =================
    dict(id="32", block="questao", text=
        "{t}Agora é a sua vez, [p=0.2] com uma questão do nosso material de estudo. [p=0.4] {a}Simplificando a expressão "
        "[p=0.2] dois elevado a cinco, [p=0.2] vezes quatro ao cubo, [p=0.2] dividido por oito ao quadrado, [p=0.2] "
        "obtém-se: [p=0.4] {qa}A: [p=0.2] oito. [p=0.3] {qb}B: [p=0.2] dezesseis. [p=0.3] {qc}C: [p=0.2] trinta e dois. "
        "[p=0.3] {qd}D: [p=0.2] sessenta e quatro. [p=0.3] {qe}E: [p=0.2] cento e vinte e oito. [p=0.5] {p}Comece pela "
        "mesma base. [p=0.2] *Pause o vídeo e tente.* [p=2.0]"),
    dict(id="33", block="questao", text=
        "{t}Vamos conferir. [p=0.3] {a}Quatro ao cubo [p=0.2] é dois ao quadrado, [p=0.2] ao cubo: [p=0.2] dois vezes três, "
        "[p=0.2] *dois elevado a seis.* [p=0.4] {b}Oito ao quadrado [p=0.2] é dois ao cubo, [p=0.2] ao quadrado: [p=0.2] "
        "também *dois elevado a seis.* [p=0.4] {c}Em cima, [p=0.2] cinco mais seis, [p=0.2] dois elevado a onze. [p=0.4] "
        "{d}Dividido por dois elevado a seis: [p=0.2] onze menos seis, [p=0.2] dois elevado a cinco. [p=0.3] {e}*Trinta e "
        "dois.* [p=0.2] {ok}*Letra C!*"),
    dict(id="34", block="questao", text=
        "{t}E as armadilhas? [p=0.3] {xb}A B é de quem *somou* na potência de potência do quatro ao cubo. [p=0.4] {xd}A D "
        "somou na do oito ao quadrado. [p=0.4] {xe}A E fez oito ao quadrado [p=0.2] como oito vezes dois. [p=0.4] {xa}A A "
        "não sai de nenhum caminho certo. [p=0.4] {chk}E repare: [p=0.2] quatro ao cubo e oito ao quadrado [p=0.2] dão "
        "sessenta e quatro *os dois.* [p=0.2] Se cancelam, [p=0.2] e sobra dois elevado a cinco."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="35", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] multiplicou mesma base, [p=0.2] soma. [p=0.2] "
        "Dividiu, [p=0.2] subtrai. [p=0.2] Potência de potência, [p=0.2] multiplica. [p=0.5] {b}Dois: [p=0.2] primeiro, "
        "[p=0.2] tudo na mesma base. [p=0.5] {c}Três: [p=0.2] na soma não existe propriedade. [p=0.2] Na dúvida, [p=0.2] "
        "teste com dois e três."),

    # ================= PONTE E CTA =================
    dict(id="36", block="ponte", text=
        "{a}Existe uma base que aparece mais que todas no ENEM: [p=0.3] {b}a *base dez.* [p=0.4] {c}População, [p=0.2] "
        "distâncias, [p=0.2] energia... [p=0.4] {d}Próximo episódio: [p=0.2] *potências de dez.*"),
    dict(id="37", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual das sete propriedades você não conhecia? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
