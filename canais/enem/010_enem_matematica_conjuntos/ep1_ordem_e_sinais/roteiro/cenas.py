# Roteiro — Operações e Conjuntos Numéricos, Episódio 1: Ordem das operações e regra de sinais (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/01-operacoes-e-conjuntos-numericos.html — seção 05 + Questão 3 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   ORDEM: a conta tem fila de prioridade, como o PRONTO-SOCORRO (parênteses → potências → vezes e dividir → mais e menos).
#   SINAIS: positivo é DINHEIRO QUE ENTRA, negativo é DÍVIDA (reta numérica + extrato bancário na tela).
# Frases-chave (meio e fim, idênticas):
#   1. Parênteses, potência, vezes e dividir, mais e menos.
#   2. Sinais iguais na multiplicação: positivo. Diferentes: negativo.
#   3. Sem parênteses, o expoente não pega o sinal de menos.
# Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = dica · vermelho = erro.
# Visual das contas: a expressão inteira fica sempre na tela; a parte resolvida ganha cor e "encolhe" para o resultado.

TITULO = "2 + 3 × 4 dá 14 ou 20? Ordem das operações e regra de sinais do zero — Matemática ENEM, episódio 1"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Quanto dá *dois mais três vezes quatro?* [p=0.6] {b}Metade das pessoas responde *vinte.* [p=0.3] "
        "{c}A outra metade responde *catorze.* [p=0.5] {d}Só uma está certa. [p=0.4] {e}E essa diferença derruba questões do ENEM "
        "[p=0.2] de física, [p=0.2] de função [p=0.2] e de estatística."),
    dict(id="02", block="promessa", text=
        "{a}Até o fim desta aula, [p=0.2] você vai resolver *qualquer* expressão, [p=0.2] que é uma conta com várias operações juntas, [p=0.2] sem errar sinal. [p=0.4] "
        "{b}Sem decoreba: [p=0.2] entendendo o porquê de cada passo."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, duas lembranças rápidas. [p=0.3] {a}Número *negativo* [p=0.2] é o que fica abaixo do zero. "
        "[p=0.3] Como o termômetro num dia de frio: [p=0.2] *menos cinco graus.* [p=0.4] {b}Na *reta numérica,* [p=0.2] uma linha com todos os números em ordem, [p=0.2] "
        "os negativos ficam à esquerda do zero, [p=0.2] e os *positivos,* os acima do zero, [p=0.2] à direita."),
    dict(id="04", block="prereq", text=
        "{t}E *potência* [p=0.2] é uma multiplicação repetida. [p=0.4] {a}Dois elevado a três [p=0.2] é o dois multiplicado por ele mesmo, "
        "[p=0.2] *três vezes:* [p=0.2] dois vezes dois vezes dois, [p=0.2] que dá *oito.* [p=0.4] {b}O número de baixo, o dois, [p=0.2] "
        "se chama *base.* [p=0.3] {c}O numerozinho de cima, o três, [p=0.2] se chama *expoente:* [p=0.2] ele diz quantas vezes a base aparece. "
        "[p=0.4] {d}Elevado a dois tem um apelido: [p=0.2] *ao quadrado.* [p=0.2] Elevado a três: [p=0.2] *ao cubo.* [p=0.4] {e}E atenção: [p=0.2] dois ao cubo *não* é dois vezes três."),

    # ================= BLOCO A: A ORDEM =================
    dict(id="05", block="ordem_por_que", text=
        "{t}Então, por que a conta não é feita da esquerda para a direita, [p=0.2] como a gente lê um texto? [p=0.5] "
        "{a}Pense em se vestir. [p=0.3] Meia primeiro, [p=0.2] depois o sapato. [p=0.4] {b}Se inverter a ordem, [p=0.2] "
        "o resultado é outro. [p=0.4] {c}Numa conta é igual: [p=0.2] a ordem muda o resultado."),
    dict(id="06", block="ordem_pronto_socorro", text=
        "{t}Por isso, toda conta tem uma *fila de prioridade,* [p=0.2] como num pronto-socorro. [p=0.4] Lá, quem está mais grave "
        "é atendido primeiro, [p=0.2] não quem chegou antes. [p=0.5] {a}Primeiro, os *parênteses.* [p=0.4] {b}Depois, as *potências.* [p=0.4] {c}Depois, *vezes e dividir.* [p=0.4] {d}Por último, *mais e menos.*"),
    dict(id="07", block="ordem_gancho", text=
        "{t}Voltando à conta do começo. [p=0.3] {a}Dois mais três vezes quatro. [p=0.4] {b}Quem é atendido primeiro? [p=0.3] "
        "O *vezes.* [p=0.3] {c}Três vezes quatro, [p=0.2] doze. [p=0.4] {d}Sobra dois mais doze: [p=0.3] {e}*catorze.* [p=0.5] "
        "{f}O vinte aparece em quem soma primeiro, [p=0.2] fura a fila."),
    dict(id="08", block="ordem_exemplo", text=
        "{t}Agora uma conta com todas as etapas da fila. [p=0.3] {a}Cinquenta menos dois vezes, [p=0.2] entre parênteses, "
        "[p=0.2] um mais dois, [p=0.2] elevado ao quadrado. [p=0.5] {b}Primeiro, os parênteses: [p=0.2] um mais dois, [p=0.2] três. "
        "[p=0.4] {c}Depois, a potência: [p=0.2] três ao quadrado, [p=0.2] três vezes três, [p=0.2] nove. [p=0.4] "
        "{d}Depois, o vezes: [p=0.2] dois vezes nove, [p=0.2] dezoito. [p=0.4] {e}Por último, o menos: [p=0.2] cinquenta menos dezoito, "
        "[p=0.2] *trinta e dois.*"),
    dict(id="09", block="ordem_colchetes", text=
        "{t}E os *colchetes,* [p=0.2] aqueles parênteses quadrados? [p=0.4] {a}Pense numa caixa dentro de outra caixa: "
        "[p=0.2] você abre *de dentro para fora.* [p=0.4] {b}Dois vezes, [p=0.2] colchete, [p=0.2] dez menos, [p=0.2] "
        "entre parênteses, [p=0.2] três mais um. [p=0.4] {c}Dentro: [p=0.2] quatro. [p=0.3] {d}Fora: [p=0.2] dez menos quatro, seis. "
        "[p=0.3] {e}Dois vezes seis: [p=0.2] *doze.* [p=0.4] {f}As *chaves* seguem a mesma ideia: [p=0.2] são a caixa mais de fora."),
    dict(id="10", block="ordem_empate", text=
        "{t}E se dois pacientes têm a mesma gravidade? [p=0.4] {a}Vezes e dividir têm a *mesma prioridade.* [p=0.3] Mais e menos também. "
        "[p=0.4] {b}No empate, [p=0.2] vale a ordem de chegada: [p=0.2] *da esquerda para a direita.* [p=0.5] {c}Doze dividido por dois, "
        "[p=0.2] vezes três. [p=0.3] {d}Primeiro o dividir, que veio antes: [p=0.2] seis. [p=0.3] {e}Depois, seis vezes três: [p=0.2] *dezoito.*"),

    # ================= BLOCO B: SINAIS IGUAIS NA SOMA =================
    dict(id="11", block="sinal_def", text=
        "{t}Agora, os sinais. [p=0.3] {a}O *sinal* é o mais ou o menos na frente do número. [p=0.4] {b}E a ideia que guia tudo: "
        "[p=0.3] {c}positivo é *dinheiro que entra.* [p=0.4] {d}Negativo é *dívida.*"),
    dict(id="12", block="sinais_iguais", text=
        "{t}Você já deve sete reais a um amigo. [p=0.3] {a}E aí faz mais uma dívida, [p=0.2] de três reais. [p=0.4] Quanto você deve agora? "
        "[p=0.5] {b}Dez reais. [p=0.4] {c}Na matemática, [p=0.2] isso se escreve menos sete menos três, [p=0.2] *igual a menos dez.* "
        "[p=0.4] {d}Na reta, [p=0.2] você anda sete para a esquerda, [p=0.2] e mais três para a esquerda."),
    dict(id="13", block="sinais_iguais", text=
        "{t}Dívida com dívida: [p=0.2] a dívida cresce. [p=0.4] {a}Dinheiro com dinheiro: [p=0.2] o saldo cresce. "
        "[p=0.3] Cinco mais três, oito. [p=0.5] {b}A regra: [p=0.2] com *sinais iguais,* [p=0.2] você *soma* os números [p=0.2] "
        "e *mantém o sinal.*"),

    # ================= BLOCO C: SINAIS DIFERENTES NA SOMA =================
    dict(id="14", block="sinais_diferentes", text=
        "{t}E quando os sinais são diferentes? [p=0.4] {a}Você está devendo sete reais. [p=0.3] {b}Aí entram três reais na sua conta. "
        "[p=0.4] {c}O dinheiro paga parte da dívida, [p=0.2] mas não toda. [p=0.4] {d}Você ainda deve *quatro.* [p=0.4] "
        "{e}Menos sete mais três, [p=0.2] *menos quatro.*"),
    dict(id="15", block="sinais_diferentes", text=
        "{t}Agora o contrário. [p=0.3] {a}Você deve três, [p=0.2] e entram sete. [p=0.4] {b}Paga a dívida e ainda sobram *quatro.* "
        "[p=0.3] Menos três mais sete, [p=0.2] *mais quatro.* [p=0.5] {c}A regra: [p=0.2] com *sinais diferentes,* [p=0.2] você *subtrai,* "
        "[p=0.3] {d}e fica com o sinal do número que pesa mais, [p=0.2] sem olhar o sinal."),

    # ================= BLOCO D: MULTIPLICAR E DIVIDIR =================
    dict(id="16", block="mult_sinais", text=
        "{t}E na multiplicação, o que acontece com os sinais? [p=0.4] {a}Três dívidas de quatro reais. [p=0.3] Três vezes menos quatro: "
        "[p=0.2] você deve *doze.* [p=0.2] Menos doze. [p=0.5] {b}Agora, alguém *cancela* três dívidas suas de quatro reais. "
        "[p=0.4] {c}Tirar uma dívida é bom para você: [p=0.2] é como ganhar dinheiro. [p=0.3] {d}Menos três vezes menos quatro: "
        "[p=0.2] *mais doze.*"),
    dict(id="17", block="mult_regra", text=
        "{t}A regra da multiplicação: [p=0.3] {a}*sinais iguais,* [p=0.2] resultado *positivo.* [p=0.3] Menos com menos, mais. "
        "[p=0.4] {b}*Sinais diferentes,* [p=0.2] resultado *negativo.* [p=0.5] {c}E a divisão segue a mesma regra. [p=0.3] "
        "{d}Menos doze dividido por quatro, [p=0.2] menos três. [p=0.3] {e}Menos doze dividido por menos quatro, [p=0.2] mais três."),
    dict(id="18", block="mult_armadilha", text=
        "{t}Mas cuidado com uma armadilha. [p=0.3] {a}Essa história de menos com menos dá mais [p=0.2] vale para *vezes e dividir.* "
        "[p=0.4] {b}Na soma, não. [p=0.3] Menos sete menos três [p=0.2] é dívida com dívida: [p=0.2] *menos dez,* [p=0.2] e não mais dez."),

    # ================= BLOCO E: MENOS ANTES DE PARÊNTESES =================
    dict(id="19", block="menos_parenteses", text=
        "{t}E um sinal de menos na frente de parênteses, [p=0.2] o que ele faz? [p=0.4] {a}Pense no menos como *o contrário de.* "
        "[p=0.3] {b}O contrário de dever doze reais [p=0.2] é *ter* doze reais. [p=0.4] {c}Por isso, [p=0.2] menos, [p=0.2] "
        "entre parênteses, [p=0.2] menos doze, [p=0.2] vira *mais doze.*"),
    dict(id="20", block="menos_parenteses", text=
        "{t}E com mais números dentro? [p=0.3] {a}Menos, [p=0.2] entre parênteses, [p=0.2] cinco menos oito. [p=0.4] "
        "{b}O menos de fora *inverte todos os sinais* de dentro. [p=0.3] {c}O cinco vira menos cinco. [p=0.2] O menos oito vira mais oito. "
        "[p=0.4] {d}Menos cinco mais oito: [p=0.2] *três.* [p=0.5] {e}Conferindo por dentro: [p=0.2] "
        "cinco menos oito, [p=0.2] menos três. [p=0.3] {f}O contrário de menos três: [p=0.2] *três.*"),

    # ================= BLOCO F: BASE NEGATIVA, EXPOENTE PAR OU ÍMPAR =================
    dict(id="21", block="base_negativa", text=
        "{t}E quando a base da potência é negativa? [p=0.4] {a}Menos dois, entre parênteses, [p=0.2] elevado a quatro. "
        "[p=0.3] É o menos dois multiplicado por ele mesmo, [p=0.2] quatro vezes. [p=0.5] {b}Menos dois vezes menos dois: [p=0.2] sinais iguais, [p=0.2] "
        "*mais quatro.* [p=0.4] {c}Vezes menos dois: [p=0.2] sinais diferentes, [p=0.2] *menos oito.* [p=0.4] "
        "{d}Vezes menos dois: [p=0.2] sinais iguais, [p=0.2] *mais dezesseis.*"),
    dict(id="22", block="base_negativa", text=
        "{t}Repare no que aconteceu: [p=0.2] os sinais de menos se cancelam *em pares.* [p=0.4] {a}Com quatro sinais, [p=0.2] "
        "formam dois pares, [p=0.2] e não sobra nenhum. [p=0.2] Resultado positivo. [p=0.4] {b}Com três, [p=0.2] "
        "menos dois elevado a três, [p=0.2] sobra um menos *sozinho.* [p=0.2] Menos oito. [p=0.5] "
        "{c}A regra: [p=0.2] base negativa com expoente *par,* [p=0.2] positivo. [p=0.3] {d}Com expoente *ímpar,* [p=0.2] negativo."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="23", block="recap", text=
        "{t}Vamos juntar tudo em três frases. [p=0.5] {a}Um: [p=0.2] parênteses, potência, vezes e dividir, mais e menos. [p=0.5] "
        "{b}Dois: [p=0.2] sinais iguais na multiplicação: positivo. [p=0.2] Diferentes: negativo. [p=0.5] {c}Três: [p=0.2] "
        "sem parênteses, o expoente não pega o sinal de menos. [p=0.4] {d}Essa terceira é o erro mais caro da prova. [p=0.2] Eu explico agora."),

    # ================= BLOCO G: −3² x (−3)² =================
    dict(id="24", block="menos_quadrado", text=
        "{t}Menos três ao quadrado e menos três, entre parênteses, ao quadrado. [p=0.3] {a}Parecem iguais. [p=0.3] "
        "{b}Não são. [p=0.5] {c}Volte ao pronto-socorro: [p=0.2] a potência é atendida *antes* do menos. [p=0.4] "
        "{d}Sem parênteses, [p=0.2] o expoente só pega o número colado nele: [p=0.2] o três. [p=0.4] "
        "{e}Três vezes três, nove. [p=0.2] {f}E o menos entra depois: [p=0.2] *menos nove.*"),
    dict(id="25", block="menos_quadrado", text=
        "{t}Os parênteses funcionam como um *embrulho.* [p=0.4] {a}Tudo o que está dentro, [p=0.2] o menos e o três, [p=0.2] "
        "é elevado junto. [p=0.4] {b}Menos três vezes menos três: [p=0.2] sinais iguais, [p=0.2] *mais nove.* [p=0.5] "
        "{c}Sem parênteses, menos nove. [p=0.3] Com parênteses, mais nove."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="26", block="erro1", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] dois mais três vezes quatro igual a vinte. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a gente lê da esquerda para a direita, [p=0.2] como um texto. [p=0.4] "
        "{c}Mas a conta tem fila: [p=0.2] o vezes vem antes. [p=0.3] {d}*Catorze.*"),
    dict(id="27", block="erro2", text=
        "{a}Segundo: [p=0.2] menos três ao quadrado igual a nove. [p=0.4] {b}Parece certo, [p=0.2] porque o menos está colado no três, "
        "[p=0.2] e menos com menos dá mais. [p=0.4] {c}Mas, sem parênteses, [p=0.2] o expoente não pega o sinal. [p=0.3] {d}*Menos nove.*"),
    dict(id="28", block="erro3", text=
        "{a}Terceiro: [p=0.2] doze menos, entre parênteses, menos doze, [p=0.2] igual a zero. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque você vê o doze e o menos, [p=0.2] e já pensa em doze menos doze. [p=0.4] {c}Mas são *dois* sinais de menos. "
        "[p=0.3] {d}Tirar uma dívida é ganhar: [p=0.2] doze mais doze, [p=0.2] *vinte e quatro.*"),

    # ================= EXERCÍCIO RÁPIDO =================
    dict(id="29", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Menos dois, entre parênteses, elevado a três. [p=0.4] {b}E menos dois ao quadrado, [p=0.2] sem parênteses. "
        "[p=0.4] {p}*Pause o vídeo e calcule.* [p=1.5]"),
    dict(id="30", block="exercicio", text=
        "{t}Conferindo. [p=0.3] {a}Menos dois, entre parênteses, ao cubo: [p=0.2] base negativa, expoente ímpar. [p=0.2] "
        "*Menos oito.* [p=0.4] {b}Menos dois ao quadrado, sem parênteses: [p=0.2] o expoente só pega o dois. [p=0.2] "
        "Dois vezes dois, quatro, [p=0.2] e o menos depois: [p=0.2] *menos quatro.*"),

    # ================= QUESTÃO 3 =================
    dict(id="31", block="questao", text=
        "{t}Hora de treinar, no estilo do ENEM. [p=0.4] {e1}O saldo de uma conta é atualizado por esta expressão, em reais: [p=0.4] "
        "{e2}doze, [p=0.2] menos quatro vezes, entre parênteses, menos três, [p=0.3] mais, entre parênteses, menos dois, elevado a três, [p=0.2] dividido por quatro. "
        "[p=0.4] {e3}Qual é o saldo?"),
    dict(id="32", block="questao", text=
        "{t}As alternativas. [p=0.3] {a}A: [p=0.2] dois reais. [p=0.3] {b}B: [p=0.2] dez reais. [p=0.3] {c}C: [p=0.2] dezoito reais. "
        "[p=0.3] {d}D: [p=0.2] vinte e dois reais. [p=0.3] {e}E: [p=0.2] vinte e seis reais. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="33", block="questao", text=
        "{t}Vamos pela fila. [p=0.3] {a}Não tem conta dentro de parênteses para fazer, [p=0.2] então a primeira é a *potência.* "
        "[p=0.4] {b}Menos dois ao cubo: [p=0.2] base negativa, expoente ímpar. [p=0.2] *Menos oito.* [p=0.5] "
        "{c}Depois, vezes e dividir. [p=0.3] {d}Quatro vezes menos três: [p=0.2] sinais diferentes, [p=0.2] *menos doze.* "
        "[p=0.4] {e}Menos oito dividido por quatro: [p=0.2] sinais diferentes, [p=0.2] *menos dois.*"),
    dict(id="34", block="questao", text=
        "{t}Sobrou: [p=0.2] doze, [p=0.2] menos, menos doze, [p=0.2] mais, menos dois. [p=0.4] {a}Menos com menos doze: [p=0.2] "
        "cancelar dívida é ganhar. [p=0.2] *Mais doze.* [p=0.4] {b}Mais com menos dois: [p=0.2] *menos dois.* [p=0.4] "
        "{c}Doze mais doze menos dois: [p=0.3] *vinte e dois reais.* [p=0.3] {d}*Letra D.*"),
    dict(id="35", block="questao", text=
        "{t}E as erradas? [p=0.4] {e}Vinte e seis: [p=0.2] quem fez menos dois ao cubo igual a *mais* oito. "
        "[p=0.2] Esqueceu que expoente ímpar mantém o menos. [p=0.4] {a}Dois: [p=0.2] quem errou essa potência [p=0.2] *e* ainda transformou "
        "menos, menos doze [p=0.2] em menos doze. [p=0.2] Dois erros na mesma conta."),
    dict(id="36", block="questao", text=
        "{c}Dezoito: [p=0.2] quem fez menos dois ao cubo igual a menos dois vezes três, [p=0.2] menos seis, [p=0.2] e ainda esqueceu de dividir por quatro. "
        "[p=0.4] {b}E dez [p=0.2] não sai de nenhum erro de regra. [p=0.2] É a alternativa do chute. [p=0.4] "
        "{x}Se a sua conta deu outro valor, [p=0.2] *refaça pela fila.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="37", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] parênteses, potência, vezes e dividir, mais e menos. [p=0.5] "
        "{b}Dois: [p=0.2] sinais iguais na multiplicação: positivo. [p=0.2] Diferentes: negativo. [p=0.5] {c}Três: [p=0.2] "
        "sem parênteses, o expoente não pega o sinal de menos."),

    # ================= PONTE =================
    dict(id="38", block="ponte", text=
        "{t}Você operou com positivos e negativos. [p=0.4] {a}Mas de onde vieram esses números? [p=0.4] "
        "{b}E existe número que não é fração? [p=0.5] {c}No próximo episódio: [p=0.2] *os conjuntos numéricos.*"),
    dict(id="39", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] antes desta aula, você respondia catorze ou vinte? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
