# Roteiro — Divisibilidade, Primos, MMC e MDC, Episódio 1 de 7: Múltiplos, divisores e os atalhos da divisibilidade (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/02-divisibilidade-primos-mmc-mdc.html — seções 02 e 03 + Questão 3 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   BALAS e ESCADA: divisor é quem divide certinho, sem sobrar bala; múltiplo é a tabuada, os degraus de quem sobe de 3 em 3.
#   RETÂNGULOS: os divisores de um número são os retângulos que dá para montar com aquela quantidade de quadradinhos
#     (36 → 1×36, 2×18, 3×12, 4×9, 6×6).
#   TESTE RÁPIDO: critério de divisibilidade diz se a divisão é exata sem você precisar fazer a conta.
# Exemplos do material (seção 03): 374 (2) · 522 (3) · 1 316 (4) · 895 (5) · 534 (6) · 1 729 (7, só citado) · 5 120 (8)
#   · 6 813 (9) · 2 470 (10) · 2 079 (11, só citado). 522, 1 316 e 534 ficam para o exercício "pause e responda";
#   na explicação dos critérios de 3, 4 e 6 usamos 471, 2 524 e 726 (conferidos por script).
# Questão 3 da seção 12 lida exatamente como no material (código 4 3 7 x 0) · gabarito: C (3 valores: x = 1, 4, 7).
# Frases-chave (meio e fim, idênticas):
#   1. Divisor divide sem sobrar; múltiplo é a tabuada.
#   2. Divisores acabam; múltiplos não.
#   3. Três e nove: some os algarismos.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Dá para saber se 6 813 é divisível por 9 em 2 segundos — Múltiplos, divisores e critérios · Matemática ENEM, episódio 1"

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
        "{a}Dá para saber se *seis mil oitocentos e treze* é divisível por nove [p=0.2] *em dois segundos,* [p=0.3] "
        "{b}sem fazer a divisão. [p=0.5] {c}E isso cai no ENEM [p=0.2] em questões de *código e senha.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber o que é *múltiplo* e o que é *divisor,* [p=0.4] {b}listar todos os "
        "divisores de um número [p=0.2] sem esquecer nenhum, [p=0.4] {c}e usar os *atalhos* da divisibilidade."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, uma lembrança rápida. [p=0.3] {a}Catorze balas para três crianças. [p=0.3] {b}Cada uma ganha quatro: "
        "[p=0.2] quatro vezes três, doze. [p=0.3] {c}E sobram *duas* balas. [p=0.4] {d}Isso que sobra [p=0.2] tem nome: "
        "[p=0.2] *resto.* [p=0.3] {e}Catorze dividido por três [p=0.2] dá quatro, [p=0.2] e sobra dois."),

    # ================= BLOCO A: DIVISOR E MÚLTIPLO =================
    dict(id="04", block="exata", text=
        "{t}E se fossem *doze* balas? [p=0.4] {a}Cada criança ganha quatro, [p=0.2] {b}e não sobra nenhuma. [p=0.3] Resto "
        "zero. [p=0.4] {c}Quando não sobra nada, [p=0.2] a divisão é *exata.* [p=0.3] {d}E a gente diz que doze é "
        "*divisível* por três: [p=0.2] a divisão por três é exata."),
    dict(id="05", block="divisor", text=
        "{t}Então, quem é o *divisor* nessa história? [p=0.4] {a}O três dividiu o doze *certinho,* [p=0.2] sem sobrar bala. "
        "[p=0.4] {b}Por isso, [p=0.2] três é *divisor* de doze. [p=0.3] {c}Divisor é quem divide certinho, [p=0.2] *sem "
        "sobrar bala.*"),
    dict(id="06", block="multiplo", text=
        "{t}E o outro lado da mesma história? [p=0.4] {a}Imagine subir uma escada de três em três degraus: [p=0.3] {b}três, "
        "[p=0.2] seis, [p=0.2] nove, [p=0.2] doze. [p=0.4] {c}Você pisa no doze. [p=0.3] Então doze é *múltiplo* de três. "
        "[p=0.4] {d}Múltiplo é a *tabuada:* [p=0.2] os degraus de quem sobe de três em três."),
    dict(id="07", block="mesma", text=
        "{t}Repare numa coisa curiosa. [p=0.3] {a}Doze dividido por três [p=0.2] dá quatro, [p=0.2] sem resto. [p=0.4] "
        "{b}Então três é divisor de doze, [p=0.3] {c}e doze é múltiplo de três. [p=0.4] {d}É a *mesma frase,* [p=0.2] dita de "
        "dois jeitos."),

    # ================= BLOCO B: ACABAM × NÃO ACABAM =================
    dict(id="08", block="finito", text=
        "{t}Quantos divisores o doze tem? [p=0.4] {a}Um, [p=0.2] dois, [p=0.2] três, [p=0.2] quatro, [p=0.2] seis [p=0.2] e "
        "doze. [p=0.4] {b}Seis divisores, [p=0.2] e *acabou.* [p=0.3] {c}Nenhum divisor passa do próprio número. [p=0.4] "
        "{d}Uma lista que acaba [p=0.2] se chama *finita.*"),
    dict(id="09", block="infinito", text=
        "{t}E os múltiplos de três? [p=0.4] {a}Zero, [p=0.2] três, [p=0.2] seis, [p=0.2] nove, [p=0.2] doze, [p=0.2] quinze... "
        "[p=0.4] {b}A escada *nunca termina.* [p=0.3] {c}Uma lista que não acaba [p=0.2] se chama *infinita.* [p=0.4] "
        "{d}Divisores acabam; [p=0.2] múltiplos não."),

    # ================= BLOCO C: REGRAS QUE SEMPRE VALEM =================
    dict(id="10", block="regras", text=
        "{t}Agora, algumas regras que *sempre* valem. [p=0.4] {a}Primeira: [p=0.2] o *um* divide qualquer número. [p=0.3] "
        "Sete balas para uma criança? [p=0.2] Ela leva tudo, [p=0.2] sem sobrar. [p=0.4] {b}Segunda: [p=0.2] todo número divide "
        "*a si mesmo.* [p=0.3] Sete balas para sete crianças: [p=0.2] uma para cada."),
    dict(id="11", block="zero", text=
        "{t}E o *zero?* [p=0.4] {a}Zero é múltiplo de todo número: [p=0.2] três vezes zero, [p=0.2] zero. [p=0.2] É o degrau "
        "onde a escada começa. [p=0.4] {b}Mas zero *não* é divisor de nenhum número. [p=0.3] {c}Repartir doze balas entre "
        "*zero* crianças? [p=0.3] Não faz sentido. [p=0.3] {d}Divisão por zero *não existe.*"),
    dict(id="12", block="soma", text=
        "{t}E uma última regra, que ajuda muito. [p=0.4] {a}O três divide o doze [p=0.2] e divide o nove. [p=0.4] {b}Então ele "
        "divide a soma: [p=0.2] vinte e um. [p=0.3] {c}E a diferença: [p=0.2] três. [p=0.4] {d}Grupinhos de três mais "
        "grupinhos de três [p=0.2] continuam em grupinhos de três."),

    # ================= BLOCO D: LISTAR SEM ESQUECER =================
    dict(id="13", block="retangulos", text=
        "{t}Agora, um desafio. [p=0.3] Como listar *todos* os divisores de trinta e seis, [p=0.2] sem esquecer nenhum? "
        "[p=0.4] {a}Pegue trinta e seis quadradinhos [p=0.2] e tente montar retângulos. [p=0.4] {b}Uma fila só: [p=0.2] um por "
        "trinta e seis. [p=0.3] {c}Duas filas de dezoito. [p=0.3] {d}Três de doze. [p=0.3] {e}Quatro de nove. [p=0.3] {f}E "
        "seis de seis, [p=0.2] um quadrado."),
    dict(id="14", block="retangulos", text=
        "{t}E com cinco filas? [p=0.3] {a}Não fecha: [p=0.2] sobra um quadradinho. [p=0.3] Cinco não é divisor. [p=0.4] "
        "{b}Os divisores são os *lados* dos retângulos que dá para montar. [p=0.4] {c}E repare: [p=0.2] no seis por seis, "
        "[p=0.2] os dois lados *se encontraram.* [p=0.3] Daqui para frente, [p=0.2] os retângulos só se repetiriam, deitados."),
    dict(id="15", block="pares", text=
        "{t}Então o método é este. [p=0.3] {a}Vá de um para cima, [p=0.2] procurando *pares* que multiplicados dão o número. "
        "[p=0.4] {b}Um vezes trinta e seis, [p=0.2] dois vezes dezoito, [p=0.2] três vezes doze, [p=0.2] quatro vezes nove, "
        "[p=0.2] seis vezes seis. [p=0.4] {c}Os lados se encontraram? [p=0.2] *Pare.* [p=0.4] {d}Juntando tudo: [p=0.2] um, "
        "dois, três, quatro, seis, nove, doze, dezoito e trinta e seis. [p=0.3] {e}*Nove* divisores."),

    # ================= BLOCO E: CRITÉRIOS QUE SE USAM DE VERDADE =================
    dict(id="16", block="criterio", text=
        "{t}E se o número for grande, [p=0.2] tipo seis mil oitocentos e treze? [p=0.4] {a}Aí entra o *critério de "
        "divisibilidade:* [p=0.2] um *teste rápido,* [p=0.2] que diz se a divisão é exata [p=0.2] sem você fazer a conta. "
        "[p=0.4] {b}E os testes olham para os *algarismos:* [p=0.2] os símbolos de zero a nove [p=0.2] que formam o número."),
    dict(id="17", block="c2", text=
        "{t}O mais fácil: [p=0.2] o do *dois.* [p=0.3] {a}O número é divisível por dois [p=0.2] quando termina em algarismo "
        "*par:* [p=0.2] zero, dois, quatro, seis ou oito. [p=0.4] {b}Trezentos e setenta e quatro [p=0.2] termina em quatro. "
        "[p=0.3] *Divisível* por dois."),
    dict(id="18", block="c5", text=
        "{t}O do *cinco:* [p=0.3] {a}termina em *zero* ou em *cinco.* [p=0.4] {b}Oitocentos e noventa e cinco [p=0.2] termina em "
        "cinco. [p=0.3] *Divisível.* [p=0.4] {c}E o do *dez:* [p=0.2] termina em zero. [p=0.3] {d}Dois mil quatrocentos e "
        "setenta. [p=0.2] *Divisível* por dez."),
    dict(id="19", block="c3", text=
        "{t}Agora, o mais útil de todos: [p=0.2] o do *três.* [p=0.4] {a}Some os algarismos. [p=0.3] Se a soma for divisível "
        "por três, [p=0.2] o número também é. [p=0.4] {b}Quatrocentos e setenta e um: [p=0.2] quatro mais sete mais um, [p=0.2] "
        "*doze.* [p=0.3] {c}Doze é divisível por três? [p=0.2] É. [p=0.3] {d}Então quatrocentos e setenta e um também é."),
    dict(id="20", block="c9", text=
        "{t}E o do *nove* [p=0.2] é igualzinho: [p=0.2] soma dos algarismos divisível por nove. [p=0.4] {a}Voltando ao começo: "
        "[p=0.2] seis mil oitocentos e treze. [p=0.3] {b}Seis mais oito, [p=0.2] catorze. [p=0.2] Mais um, quinze. [p=0.2] "
        "Mais três, *dezoito.* [p=0.4] {c}Dezoito é divisível por nove. [p=0.3] {d}Então seis mil oitocentos e treze *também é.* "
        "[p=0.3] Dois segundos!"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] divisor divide sem sobrar; [p=0.2] múltiplo é a tabuada. "
        "[p=0.5] {b}Dois: [p=0.2] divisores acabam; [p=0.2] múltiplos não. [p=0.5] {c}Três: [p=0.2] três e nove: [p=0.2] some "
        "os algarismos."),

    # ================= BLOCO F: 4, 6 E 8; 7 E 11 SÓ CITADOS =================
    dict(id="22", block="c4", text=
        "{t}E o do *quatro?* [p=0.4] {a}Olhe só os *dois últimos* algarismos. [p=0.3] Se eles formarem um número divisível por "
        "quatro, [p=0.2] o número inteiro é. [p=0.4] {b}Dois mil quinhentos e vinte e quatro: [p=0.2] os dois últimos formam "
        "*vinte e quatro.* [p=0.3] {c}Vinte e quatro é divisível por quatro. [p=0.2] Então o número também é."),
    dict(id="23", block="c6", text=
        "{t}O do *seis* [p=0.2] é a soma de dois testes: [p=0.3] {a}tem que passar no do dois [p=0.2] *e* no do três, [p=0.2] "
        "ao mesmo tempo. [p=0.4] {b}Setecentos e vinte e seis: [p=0.2] termina em seis, [p=0.2] é par. [p=0.3] {c}Sete mais "
        "dois mais seis, [p=0.2] quinze, [p=0.2] divisível por três. [p=0.3] {d}Passou nos dois: [p=0.2] *divisível por seis.*"),
    dict(id="24", block="c8", text=
        "{t}O do *oito* [p=0.2] olha os *três* últimos algarismos. [p=0.4] {a}Cinco mil cento e vinte: [p=0.2] os três últimos "
        "formam *cento e vinte,* [p=0.2] que é oito vezes quinze. [p=0.3] Divisível. [p=0.5] {b}Existem também os do *sete* e do "
        "*onze.* [p=0.3] {c}O do sete é trabalhoso: [p=0.2] muitas vezes, [p=0.2] é mais rápido *dividir* mesmo."),

    # ================= BLOCO G: COMBINAR CRITÉRIOS =================
    dict(id="25", block="combinar", text=
        "{t}E se a pergunta for divisível por *doze?* [p=0.2] Não tem teste do doze. [p=0.4] {a}Tem um truque: [p=0.2] junte "
        "dois testes. [p=0.3] {b}Para doze, [p=0.2] teste o *três* e o *quatro.* [p=0.3] {c}Para quinze, [p=0.2] o três e o cinco. "
        "[p=0.3] {d}Para quarenta e cinco, [p=0.2] o cinco e o nove. [p=0.4] {e}A regra é usar dois números *primos entre si:* "
        "[p=0.2] números cujo único divisor em comum é o um."),
    dict(id="26", block="combinar", text=
        "{t}E por que, para doze, [p=0.2] não adianta testar dois e seis? [p=0.4] {a}Porque o dois e o seis [p=0.2] têm o *dois* "
        "em comum: [p=0.2] não são primos entre si. [p=0.4] {b}Veja o trinta. [p=0.2] É par. [p=0.2] E é divisível por seis. "
        "[p=0.4] {c}Mas trinta dividido por doze [p=0.2] dá dois, [p=0.2] e *sobra seis.* [p=0.3] {d}Com três e quatro, [p=0.2] "
        "o trinta reprova no teste do quatro, [p=0.2] como deve ser."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="27", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que o *zero* é divisor de todo número. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque o zero aparece em toda tabuada. [p=0.4] {c}Mas isso faz dele *múltiplo* de todos. "
        "[p=0.2] Divisor, nunca: [p=0.2] divisão por zero não existe."),
    dict(id="28", block="erros", text=
        "{a}Segundo: [p=0.2] listar divisores no chute, [p=0.2] e esquecer algum. [p=0.4] {b}Parece certo, [p=0.2] porque os "
        "pequenos vêm fácil: [p=0.2] um, dois, três, quatro, seis... [p=0.4] {c}Mas os grandes, [p=0.2] como o dezoito, [p=0.2] "
        "ficam de fora. [p=0.3] Use os *pares,* [p=0.2] e cada pequeno traz o seu par grande."),
    dict(id="29", block="erros", text=
        "{a}Terceiro: [p=0.2] testar divisível por doze [p=0.2] com o dois e o seis. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "dois vezes seis é doze. [p=0.4] {c}Mas eles têm um divisor em comum, [p=0.2] e o trinta passa nos dois sem ser "
        "divisível por doze. [p=0.3] Use *três e quatro.*"),

    # ================= EXERCÍCIO RÁPIDO =================
    dict(id="30", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quinhentos e vinte e dois é divisível por três? [p=0.4] {b}Mil trezentos e dezesseis é divisível "
        "por quatro? [p=0.4] {c}E quinhentos e trinta e quatro, [p=0.2] por seis? [p=0.4] {p}*Pause o vídeo e responda.* "
        "[p=2.0]"),
    dict(id="31", block="exercicio", text=
        "{t}Conferindo. [p=0.3] {a}Cinco mais dois mais dois, [p=0.2] nove. [p=0.2] Divisível por três: [p=0.2] *sim.* [p=0.4] "
        "{b}Mil trezentos e dezesseis: [p=0.2] os dois últimos formam dezesseis, [p=0.2] que é quatro vezes quatro. [p=0.2] "
        "*Sim.* [p=0.4] {c}Quinhentos e trinta e quatro: [p=0.2] é par, [p=0.2] e cinco mais três mais quatro dá doze. "
        "[p=0.2] Passou nos dois: [p=0.2] *sim.*"),

    # ================= QUESTÃO 3 =================
    dict(id="32", block="questao", text=
        "{t}Agora, no estilo do ENEM. [p=0.4] {a}Um código de validação tem cinco algarismos na forma [p=0.2] quatro, três, sete, "
        "xis, zero, [p=0.3] em que xis é um algarismo desconhecido. [p=0.4] {b}O código só é válido se o número for divisível "
        "por seis. [p=0.4] {c}Quantos valores de xis tornam o código válido? [p=0.5] {d}A: [p=0.2] um. [p=0.2] B: [p=0.2] dois. "
        "[p=0.2] C: [p=0.2] três. [p=0.2] D: [p=0.2] quatro. [p=0.2] E: [p=0.2] cinco. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="33", block="questao", text=
        "{t}Vamos juntos. [p=0.3] {a}Divisível por seis [p=0.2] é passar no teste do dois [p=0.2] *e* no do três. [p=0.4] "
        "{b}O do dois: [p=0.2] o número termina em zero, [p=0.2] que é par. [p=0.3] Já passou, [p=0.2] seja qual for o xis. "
        "[p=0.4] {c}O do três: [p=0.2] a soma dos algarismos precisa ser divisível por três. [p=0.3] {d}Quatro mais três mais "
        "sete mais zero [p=0.2] dá catorze. [p=0.3] {e}A soma é *catorze mais xis.*"),
    dict(id="34", block="questao", text=
        "{t}Agora, testando o xis de zero a nove. [p=0.4] {a}Zero dá catorze: [p=0.2] não. [p=0.2] {b}Um dá *quinze:* [p=0.2] "
        "sim! [p=0.3] {c}Dois e três: [p=0.2] não. [p=0.2] {d}Quatro dá *dezoito:* [p=0.2] sim! [p=0.3] {e}Cinco e seis: [p=0.2] "
        "não. [p=0.2] {f}Sete dá *vinte e um:* [p=0.2] sim! [p=0.3] {g}Oito e nove: [p=0.2] não. [p=0.5] {h}Três valores: "
        "[p=0.2] um, quatro e sete. [p=0.3] {i}*Letra C.*"),
    dict(id="35", block="questao", text=
        "{t}E repare no padrão. [p=0.3] {a}Um, [p=0.2] quatro, [p=0.2] sete: [p=0.2] as soluções vão de *três em três.* [p=0.4] "
        "{b}Faz sentido: [p=0.2] para continuar na tabuada do três, [p=0.2] a soma precisa subir de três em três. [p=0.4] "
        "{c}Quem marca dois [p=0.2] costuma parar de testar antes do sete."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="36", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] divisor divide sem sobrar; [p=0.2] múltiplo é a tabuada. "
        "[p=0.5] {b}Dois: [p=0.2] divisores acabam; [p=0.2] múltiplos não. [p=0.5] {c}Três: [p=0.2] três e nove: [p=0.2] some "
        "os algarismos."),

    # ================= PONTE E CTA =================
    dict(id="37", block="ponte", text=
        "{a}Alguns números só formam *um* retângulo: [p=0.2] uma fila. [p=0.4] {b}O sete, [p=0.2] o treze, [p=0.2] o vinte e "
        "nove... [p=0.4] {c}São os *números primos,* [p=0.3] {d}e eles são os *tijolos* de todos os outros. [p=0.4] "
        "{e}Próximo episódio."),
    dict(id="38", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já conhecia o truque de somar os algarismos? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
