# Roteiro — Divisibilidade, Primos, MMC e MDC, Episódio 2 de 7: Números primos — os tijolos de todos os números (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/02-divisibilidade-primos-mmc-mdc.html — seção 04 + Questão 7 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=0.4] pausa
# Analogia âncora: primos são TIJOLOS (não se quebram em pedaços menores); compostos são CONSTRUÇÕES feitas com tijolos;
#   o 1 não é tijolo nem construção (categoria à parte). Visual: primo = quadradinhos que só formam UMA fila.
# Lidos EXATAMENTE como no material: definições de primo e composto (cenas 05–06), o 1 e o 2 (07–08), os 25 primos e a dica
#   das terminações (10–11), o método da raiz e o 181 (12–13), primos entre si (14), Questão 7 (enunciado e alternativas).
# Contas conferidas por script: 25 primos até 100 (crivo por 2, 3, 5, 7); √181 ≈ 13,45 (13² = 169, 14² = 196) e nenhum de
#   2, 3, 5, 7, 11, 13 divide 181; 21 = 3·7, 27 = 3·9, 33 = 3·11, 39 = 3·13; 51 = 3·17; 53 primo (√53 ≈ 7,3);
#   primos entre 20 e 40: 23, 29, 31, 37 → 4 (alternativa C).
# Frases-chave (meio e fim, idênticas):
#   1. Primo tem exatamente dois divisores.
#   2. O 1 não é primo; o 2 é o único primo par.
#   3. Para testar, divida pelos primos até a raiz.
# Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "O 1 é Primo? E o 2? Números Primos do Zero | Divisibilidade Ep. 2"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado por matemática, conversando de perto com um aluno "
            "que tem base fraca e medo de conta: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase "
            "forte às palavras-chave. Nas contas, fale devagar e com clareza, passo a passo. Ritmo didático e tranquilo, "
            "sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}O *um* é primo? [p=0.4] {b}O *dois* é primo? [p=0.5] {c}Metade das pessoas erra as duas, [p=0.2] e as duas caem "
        "em prova. [p=0.4] {d}Em sete minutos, [p=0.2] você nunca mais erra."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai reconhecer os *primos até cem* [p=0.4] {b}e testar se qualquer número é primo [p=0.2] "
        "com *poucas divisões.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Lembrando, rapidinho. [p=0.3] {a}Divisor é quem divide certinho, [p=0.2] sem sobrar. [p=0.3] {b}E para achar os "
        "divisores, [p=0.2] a gente procura *pares:* [p=0.2] trinta e seis é um vezes trinta e seis, [p=0.2] dois vezes dezoito, "
        "[p=0.2] três vezes doze, [p=0.2] quatro vezes nove, [p=0.2] seis vezes seis. [p=0.4] {c}E *raiz quadrada* [p=0.2] é o "
        "número que, vezes ele mesmo, [p=0.2] dá o número. [p=0.3] {d}Raiz de trinta e seis é seis, [p=0.2] porque seis vezes "
        "seis dá trinta e seis."),

    # ================= OS RETÂNGULOS =================
    dict(id="04", block="fila", text=
        "{t}Agora, um desafio com quadradinhos. [p=0.3] {a}Com *seis,* [p=0.2] dá para fazer uma fila [p=0.2] {b}ou um retângulo "
        "de dois por três. [p=0.4] {c}E com *sete?* [p=0.3] {d}Tenta duas fileiras: [p=0.2] sobra um. [p=0.3] {e}Três fileiras: "
        "[p=0.2] sobra um. [p=0.4] {f}O sete *só* forma uma fila. [p=0.3] E isso tem nome."),

    # ================= BLOCO A: PRIMO =================
    dict(id="05", block="primo", text=
        "{t}O sete é um número *primo.* [p=0.4] {a}Primo tem exatamente dois divisores: [p=0.2] o um [p=0.2] e ele mesmo. "
        "[p=0.4] {b}Pense num *tijolo:* [p=0.2] não dá para quebrá-lo em pedaços menores. [p=0.4] {c}Dois, três, cinco, sete: "
        "[p=0.2] só formam uma fila."),

    # ================= BLOCO B: COMPOSTO =================
    dict(id="06", block="composto", text=
        "{t}E o seis? [p=0.3] {a}Ele é *composto:* [p=0.2] tem mais de dois divisores. [p=0.3] {b}Um, dois, três e seis. "
        "[p=0.4] {c}Composto é uma *construção* [p=0.2] feita com tijolos: [p=0.2] seis é dois vezes três. [p=0.4] "
        "{d}Forma mais de um retângulo."),

    # ================= BLOCO C: O 1 =================
    dict(id="07", block="um", text=
        "{t}E o um? [p=0.3] É primo? [p=0.5] {a}*Não.* [p=0.3] {b}O um tem um único divisor: [p=0.2] ele mesmo. [p=0.3] "
        "{c}E a definição exige *dois.* [p=0.4] {d}Também não é composto. [p=0.3] {e}O um não é tijolo nem construção: "
        "[p=0.2] é uma *categoria à parte.*"),

    # ================= BLOCO D: O 2 =================
    dict(id="08", block="dois", text=
        "{t}E o dois, [p=0.2] que é par? [p=0.4] {a}O dois *é primo:* [p=0.2] seus divisores são um e dois, [p=0.2] exatamente "
        "dois. [p=0.4] {b}E é o *único primo par.* [p=0.3] {c}Qualquer outro par, [p=0.2] como o quatro, [p=0.2] tem o dois como "
        "divisor extra. [p=0.3] {d}Então é composto."),

    # ================= BLOCO E: O CRIVO =================
    dict(id="09", block="crivo", text=
        "{t}Então, quais são os primos até cem? [p=0.4] {a}Existe uma peneira antiga para isso: [p=0.2] o *crivo.* [p=0.4] "
        "{b}Risque o um. [p=0.3] {c}Agora, risque todos os múltiplos de dois, [p=0.2] menos o próprio dois. [p=0.4] {d}Depois, os "
        "múltiplos de três. [p=0.4] {e}Os de cinco. [p=0.4] {f}E os de sete. [p=0.5] {g}Quem sobrou aceso [p=0.2] é primo."),
    dict(id="10", block="crivo", text=
        "{t}Sobraram *vinte e cinco.* [p=0.3] {a}Dois, três, cinco, sete, [p=0.2] onze, treze, dezessete, dezenove, [p=0.2] "
        "vinte e três, vinte e nove, [p=0.2] trinta e um, trinta e sete, [p=0.2] quarenta e um, quarenta e três, quarenta e "
        "sete, [p=0.3] {b}cinquenta e três, cinquenta e nove, [p=0.2] sessenta e um, sessenta e sete, [p=0.2] setenta e um, "
        "setenta e três, setenta e nove, [p=0.2] oitenta e três, oitenta e nove [p=0.2] e noventa e sete. [p=0.4] "
        "{c}Vale decorar."),
    dict(id="11", block="crivo", text=
        "{t}E uma dica para não decorar errado. [p=0.3] {a}Nenhum termina em zero, dois, quatro, cinco, seis ou oito, [p=0.3] "
        "{b}com a única exceção do próprio dois [p=0.2] e do cinco."),

    # ================= BLOCO F: O TESTE DA RAIZ =================
    dict(id="12", block="raiz", text=
        "{t}E um número maior, [p=0.2] como cento e oitenta e um? [p=0.3] Vai dividir por tudo? [p=0.5] {a}Não precisa. "
        "[p=0.3] {b}Teste a divisão pelos primos *até a raiz quadrada* do número. [p=0.3] Se nenhum dividir, [p=0.2] ele é primo. "
        "[p=0.4] {c}Por quê? [p=0.3] Lembra dos pares do trinta e seis? [p=0.3] {d}Eles se encontram no seis vezes seis, [p=0.2] "
        "a raiz. [p=0.3] {e}Passou da raiz, [p=0.2] os pares já teriam aparecido."),
    dict(id="13", block="raiz", text=
        "{t}Vamos testar. [p=0.3] {a}Treze vezes treze dá cento e sessenta e nove; [p=0.2] catorze vezes catorze, [p=0.2] cento e "
        "noventa e seis. [p=0.3] {b}Então a raiz de cento e oitenta e um [p=0.2] é mais ou menos *treze vírgula quatro:* "
        "[p=0.2] é a linha de chegada. [p=0.4] {c}Por dois? [p=0.2] Não, é ímpar. [p=0.3] {d}Por três? [p=0.2] A soma dos "
        "algarismos dá dez: [p=0.2] não. [p=0.3] {e}Por cinco? [p=0.2] Termina em um: [p=0.2] não. [p=0.3] {f}Por sete? "
        "[p=0.2] Sobra seis. [p=0.3] {g}Por onze? [p=0.2] Sobra cinco. [p=0.3] {h}Por treze? [p=0.2] Sobra doze. [p=0.4] "
        "{i}Nenhum divide: [p=0.2] cento e oitenta e um *é primo.*"),

    # ================= BLOCO G: PRIMOS ENTRE SI =================
    dict(id="14", block="entresi", text=
        "{t}Agora, um nome que confunde. [p=0.3] {a}*Primos entre si:* [p=0.2] dois números cujo único divisor em comum é o um. "
        "[p=0.4] {b}Oito tem divisores um, dois, quatro e oito. [p=0.3] {c}Nove tem um, três e nove. [p=0.3] {d}Em comum, "
        "[p=0.2] só o um. [p=0.4] {e}Eles não precisam ser primos: [p=0.2] oito e nove são compostos, [p=0.2] mas são primos "
        "entre si."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="15", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] primo tem exatamente dois divisores. [p=0.5] {b}Dois: [p=0.2] "
        "o um não é primo; [p=0.2] o dois é o único primo par. [p=0.5] {c}Três: [p=0.2] para testar, [p=0.2] divida pelos "
        "primos até a raiz."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="16", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que o *um* é primo. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque ele só é divisível por um e por ele mesmo. [p=0.4] {c}Mas um e ele mesmo são o *mesmo* número: [p=0.2] "
        "é um divisor só."),
    dict(id="17", block="erros", text=
        "{a}Segundo: [p=0.2] achar que o dois não é primo [p=0.2] *porque é par.* [p=0.4] {b}Parece certo, [p=0.2] porque todos "
        "os outros pares são compostos. [p=0.4] {c}Mas os divisores do dois são um e dois: [p=0.2] exatamente dois."),
    dict(id="18", block="erros", text=
        "{a}Terceiro: [p=0.2] achar que todo ímpar é primo. [p=0.4] {b}Parece certo, [p=0.2] porque muitos primos são ímpares. "
        "[p=0.4] {c}Mas vinte e um é três vezes sete; [p=0.2] vinte e sete, três vezes nove; [p=0.2] trinta e três, três vezes "
        "onze; [p=0.2] trinta e nove, três vezes treze."),
    dict(id="19", block="erros", text=
        "{a}Quarto: [p=0.2] continuar testando *depois da raiz.* [p=0.4] {b}Parece mais seguro. [p=0.4] {c}Mas é só perda de "
        "tempo: [p=0.2] depois da linha de chegada, [p=0.2] não aparece divisor novo."),

    # ================= EXERCÍCIO =================
    dict(id="20", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Pause e diga: [p=0.2] cinquenta e um é primo? [p=0.3] {b}E cinquenta e três? [p=2.0] "),
    dict(id="21", block="exercicio", text=
        "{t}Cinquenta e um parece primo, [p=0.2] mas não é: [p=0.3] {a}cinco mais um dá seis, [p=0.2] então divide por três. "
        "[p=0.3] {b}Cinquenta e um é três vezes dezessete. [p=0.4] {c}E cinquenta e três? [p=0.2] A raiz fica perto de sete. "
        "[p=0.3] {d}Não é par, [p=0.2] a soma dá oito, [p=0.2] não termina em zero nem cinco, [p=0.2] e por sete sobra quatro. "
        "[p=0.4] {e}Cinquenta e três *é primo.*"),

    # ================= QUESTÃO 7 =================
    dict(id="22", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {a}Quantos números primos existem entre vinte e quarenta? [p=0.4] "
        "{b}A: [p=0.2] dois. [p=0.3] {c}B: [p=0.2] três. [p=0.3] {d}C: [p=0.2] quatro. [p=0.3] {e}D: [p=0.2] cinco. [p=0.3] "
        "{f}E: [p=0.2] seis. [p=0.5] {p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="23", block="q7", text=
        "{t}Vamos juntos. [p=0.3] {a}Elimine de saída todos os pares [p=0.2] e todos os terminados em cinco. [p=0.4] {b}Sobram "
        "poucos candidatos: [p=0.2] vinte e um, vinte e três, vinte e sete, vinte e nove, [p=0.2] trinta e um, trinta e três, "
        "trinta e sete [p=0.2] e trinta e nove."),
    dict(id="24", block="q7", text=
        "{t}Um a um. [p=0.3] {a}Vinte e um, [p=0.2] três vezes sete: [p=0.2] composto. [p=0.3] {b}Vinte e três: [p=0.2] primo. "
        "[p=0.3] {c}Vinte e sete, [p=0.2] três vezes nove: [p=0.2] composto. [p=0.3] {d}Vinte e nove: [p=0.2] primo. [p=0.3] "
        "{e}Trinta e um: [p=0.2] primo. [p=0.3] {f}Trinta e três, [p=0.2] três vezes onze: [p=0.2] composto. [p=0.3] {g}Trinta "
        "e sete: [p=0.2] primo. [p=0.3] {h}Trinta e nove, [p=0.2] três vezes treze: [p=0.2] composto. [p=0.5] {i}São quatro: "
        "[p=0.2] vinte e três, vinte e nove, trinta e um e trinta e sete. [p=0.3] {ok}*Letra C!* [p=0.4] {x}Marcou cinco ou "
        "seis? [p=0.2] Algum ímpar composto passou como primo."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="25", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] primo tem exatamente dois divisores. [p=0.5] {b}Dois: "
        "[p=0.2] o um não é primo; [p=0.2] o dois é o único primo par. [p=0.5] {c}Três: [p=0.2] para testar, [p=0.2] divida "
        "pelos primos até a raiz."),

    # ================= PONTE E CTA =================
    dict(id="26", block="ponte", text=
        "{a}Se os primos são tijolos, [p=0.2] todo número é uma construção feita com eles. [p=0.4] {b}Como descobrir quais "
        "tijolos formam o *trezentos e sessenta?* [p=0.4] {c}Próximo episódio: [p=0.2] *fatoração.*"),
    dict(id="27", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] antes desta aula, você achava que o um era primo? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
