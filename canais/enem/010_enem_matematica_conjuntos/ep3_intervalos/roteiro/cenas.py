# Roteiro — Operações e Conjuntos Numéricos, Episódio 3: Intervalos reais — a bolinha cheia e a bolinha vazia (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/01-operacoes-e-conjuntos-numericos.html — seção 09
#   (o material não tem questão deste tema: a questão das cenas 26–30 é INÉDITA, criada para o vídeo)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: o COLCHETE É UM BRAÇO. Virado para o número, ABRAÇA: o número entra.
#   Virado para fora, EMPURRA: o número fica de fora. Na reta: bolinha cheia = entra; bolinha vazia = não entra.
# Regra visual: todo intervalo aparece nas TRÊS formas ao mesmo tempo (português · colchetes · reta).
# Frases-chave (meio e fim, idênticas):
#   1. Colchete virado para o número: entra. Virado para fora: não entra.
#   2. Bolinha cheia entra; bolinha vazia não.
#   3. Infinito é sempre aberto.
# Questão inédita (gabarito C): reta com bolinha VAZIA no 20 e seta para a direita (tarifa máxima de água).
#   A [20, +∞[ "a partir de 20"   → leu a bolinha vazia como incluída (erro 2)
#   B ]20, +∞] "acima de 20"      → fechou o lado do infinito (erro 1)
#   C ]20, +∞[ "acima de 20"      → CORRETA
#   D ]20, +∞[ "a partir de 20"   → confundiu "acima de" com "a partir de" (erro 3)
#   E [20, +∞] "a partir de 20"   → erros 1 e 2 juntos

TITULO = "Bolinha Cheia ou Vazia? Intervalos Reais do Zero | Matemática Básica Ep. 3"
PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Num gráfico do ENEM, [p=0.2] uma bolinha *vazia* em vez de cheia [p=0.3] {b}muda a alternativa correta. "
        "[p=0.5] {c}Em seis minutos, [p=0.2] você nunca mais erra isso."),
    dict(id="02", block="promessa", text=
        "{a}Até o fim desta aula, [p=0.2] você vai ler e escrever qualquer intervalo [p=0.3] "
        "{b}de três jeitos: [p=0.2] em português, [p=0.2] {c}com colchetes [p=0.2] {d}e desenhado na reta."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, duas lembranças rápidas. [p=0.3] {a}Do episódio dois: [p=0.2] a *reta real* não tem buracos. "
        "[p=0.3] {b}Entre o dois e o três, [p=0.2] tem o dois e meio, [p=0.2] tem a raiz de cinco, [p=0.2] tem infinitos números."),
    dict(id="04", block="prereq", text=
        "{t}E dois sinais. [p=0.3] {a}Este quer dizer *menor que:* [p=0.2] a ponta fica do lado do menor. "
        "[p=0.3] Dois é menor que cinco. [p=0.4] {b}Com um tracinho embaixo, [p=0.2] vira *menor ou igual:* "
        "[p=0.2] pode ser menor, [p=0.2] ou exatamente igual. [p=0.4] {c}Virados ao contrário, [p=0.2] viram *maior que* "
        "[p=0.2] e *maior ou igual.*"),

    # ================= BLOCO A: FECHADO =================
    dict(id="05", block="fechado", text=
        "{t}Uma promoção vale *de dois a cinco* de março. [p=0.4] {a}O dia dois tem promoção? [p=0.3] Tem. [p=0.3] "
        "{b}E o dia cinco? [p=0.2] Também. [p=0.4] {c}As duas pontas *entram.*"),
    dict(id="06", block="fechado", text=
        "{t}Um pedaço da reta entre dois números [p=0.2] se chama *intervalo.* [p=0.4] {a}As pontas se chamam *extremos.* "
        "[p=0.4] {b}Quando os dois extremos entram, [p=0.2] o intervalo é *fechado.* [p=0.4] {c}Na reta, [p=0.2] "
        "cada ponta que entra [p=0.2] ganha uma *bolinha cheia.*"),
    dict(id="07", block="fechado", text=
        "{t}Com *colchetes,* [p=0.2] aqueles parênteses quadrados, [p=0.2] fica assim. [p=0.4] {a}Pense que o colchete é um *braço.* [p=0.3] {b}Virado para o número, "
        "[p=0.2] ele *abraça* o número: [p=0.2] o número entra. [p=0.4] {c}Aqui, os dois braços abraçam: [p=0.2] "
        "o dois e o cinco entram."),
    dict(id="08", block="fechado", text=
        "{t}E tem um terceiro jeito de escrever. [p=0.3] {a}A letra *x* representa qualquer número do intervalo. "
        "[p=0.4] {b}Dois é menor ou igual a x, [p=0.2] que é menor ou igual a cinco. [p=0.4] {c}Uma frase assim, "
        "[p=0.2] com sinal de menor no lugar do igual, [p=0.2] se chama *inequação.*"),

    # ================= BLOCO B: ABERTO =================
    dict(id="09", block="aberto", text=
        "{t}E se as pontas *não* entram? [p=0.4] {a}Uma planta só sobrevive *acima* de dois graus [p=0.2] "
        "e *abaixo* de cinco. [p=0.4] {b}Com dois graus, [p=0.2] ela não aguenta. [p=0.3] Com cinco, [p=0.2] também não."),
    dict(id="10", block="aberto", text=
        "{t}Nenhuma ponta entra: [p=0.2] o intervalo é *aberto.* [p=0.4] {a}Na reta, [p=0.2] as bolinhas ficam *vazias.* "
        "[p=0.4] {b}E os braços viram para fora: [p=0.2] eles *empurram* o número. [p=0.4] {c}Na inequação, "
        "[p=0.2] o sinal perde o tracinho: [p=0.2] dois é menor que x, [p=0.2] que é menor que cinco."),
    dict(id="11", block="aberto", text=
        "{t}Atenção: [p=0.2] alguns livros escrevem o aberto com *parênteses.* [p=0.4] {a}É a mesma coisa. "
        "[p=0.3] {b}Os parênteses também são braços virados para fora."),

    # ================= BLOCO C: SEMIABERTO =================
    dict(id="12", block="semiaberto", text=
        "{t}E quando só *uma* ponta entra? [p=0.4] {a}Pense na conta de luz, [p=0.2] que é cobrada por faixas de consumo. "
        "[p=0.4] {b}A segunda faixa vai de cem *até antes* de duzentos. [p=0.3] {c}O cem entra. [p=0.3] {d}O duzentos já é da "
        "faixa seguinte."),
    dict(id="13", block="semiaberto", text=
        "{t}Isso é um intervalo *semiaberto:* [p=0.2] meio aberto. [p=0.4] {a}No cem, [p=0.2] braço abraçando [p=0.2] "
        "e bolinha cheia. [p=0.4] {b}No duzentos, [p=0.2] braço empurrando [p=0.2] e bolinha vazia."),

    # ================= BLOCO D/E: INFINITO =================
    dict(id="14", block="infinito", text=
        "{t}E quando não tem ponta do outro lado? [p=0.4] {a}*Proibido para menores de dezoito.* [p=0.3] "
        "Quem pode entrar? [p=0.4] {b}Quem tem dezoito, [p=0.2] ou mais. [p=0.3] "
        "{c}Não tem limite."),
    dict(id="15", block="infinito", text=
        "{t}Esse \"não tem fim\" se chama *infinito,* [p=0.2] {a}e o símbolo é um oito deitado. [p=0.4] "
        "{b}O dezoito entra: [p=0.2] bolinha cheia e braço abraçando. [p=0.4] {c}E do outro lado, [p=0.2] "
        "a reta segue com uma *seta,* [p=0.2] até mais infinito. [p=0.4] {d}Na inequação: [p=0.2] x maior ou igual a dezoito."),
    dict(id="16", block="infinito_regra", text=
        "{t}E repare no colchete do infinito: [p=0.2] ele está *sempre* virado para fora. [p=0.4] {a}Por quê? [p=0.3] "
        "{b}Porque infinito *não é um número.* [p=0.4] {c}E não dá para abraçar "
        "uma coisa que nunca acaba. [p=0.4] {d}A regra, sem exceção: [p=0.2] o lado do infinito é *sempre aberto.*"),

    # ================= BLOCO F: GRÁFICOS =================
    dict(id="17", block="graficos", text=
        "{t}E onde isso aparece no ENEM? [p=0.4] {a}Muito em *gráficos.* [p=0.3] {b}Uma linha que termina numa bolinha "
        "*cheia:* [p=0.2] aquele ponto faz parte. [p=0.4] {c}Numa bolinha *vazia:* [p=0.2] o ponto ficou de fora."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos juntar tudo em três frases. [p=0.5] {a}Um: [p=0.2] colchete virado para o número: entra. "
        "[p=0.2] Virado para fora: não entra. [p=0.5] {b}Dois: [p=0.2] bolinha cheia entra; [p=0.2] bolinha vazia não. "
        "[p=0.5] {c}Três: [p=0.2] infinito é sempre aberto."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erro1", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] fechar o colchete do infinito. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o outro lado está fechado. "
        "[p=0.4] {c}Mas infinito não se abraça. [p=0.3] Lado do infinito: [p=0.2] *aberto.*"),
    dict(id="20", block="erro2", text=
        "{a}Segundo: [p=0.2] ler a bolinha vazia como ponto incluído. [p=0.4] {b}Parece certo, [p=0.2] porque a linha "
        "*chega* até a bolinha. [p=0.4] {c}Mas chegar perto não é entrar. [p=0.3] Vazia: [p=0.2] *ficou de fora.*"),
    dict(id="21", block="erro3", text=
        "{a}Terceiro: [p=0.2] confundir *acima de* com *a partir de.* [p=0.4] {b}Parece certo, [p=0.2] porque no dia a dia "
        "a gente fala os dois como se fossem iguais. [p=0.4] {c}Mas frete grátis *acima* de cem reais: [p=0.2] "
        "uma compra de cem *não* ganha. [p=0.3] Bolinha vazia. [p=0.4] {d}*A partir de* dezoito: [p=0.2] o dezoito entra. "
        "[p=0.2] Bolinha cheia."),

    # ================= EXERCÍCIO =================
    dict(id="22", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Traduza para colchetes [p=0.2] e desenhe na reta. [p=0.4] {a}Um: [p=0.2] meia-entrada "
        "*a partir de* sessenta anos. [p=0.4] {b}Dois: [p=0.2] grupos *de dez a vinte* pessoas, [p=0.2] contando os dois. "
        "[p=0.4] {c}Três: [p=0.2] temperatura *abaixo de zero.* [p=0.4] {p}*Pause o vídeo e traduza.* [p=1.5]"),
    dict(id="23", block="exercicio", text=
        "{t}Conferindo. [p=0.3] {a}A partir de sessenta: [p=0.2] o sessenta entra, [p=0.2] fechado no sessenta, "
        "[p=0.2] até mais infinito, [p=0.2] aberto."),
    dict(id="24", block="exercicio", text=
        "{b}De dez a vinte, contando os dois: [p=0.2] fechado nas duas pontas. [p=0.4] {c}Abaixo de zero: [p=0.2] "
        "de *menos infinito,* [p=0.2] o infinito do lado esquerdo, [p=0.2] aberto, [p=0.2] até o zero, [p=0.2] também aberto, [p=0.2] porque zero grau "
        "não está abaixo de zero."),

    # ================= QUESTÃO INÉDITA =================
    dict(id="25", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {e1}Uma companhia de água cobra a tarifa mais cara "
        "conforme o consumo do mês. [p=0.4] {e2}A faixa da tarifa mais cara aparece na reta: "
        "[p=0.2] uma bolinha *vazia* no vinte [p=0.2] e a linha pintada para a direita, [p=0.2] sem fim. "
        "[p=0.4] {e3}Qual alternativa descreve essa faixa?"),
    dict(id="26", block="questao", text=
        "{t}As alternativas. [p=0.3] {a}A: [p=0.2] fechado no vinte, [p=0.2] infinito aberto: [p=0.2] consumo a partir de vinte. "
        "[p=0.4] {b}B: [p=0.2] aberto no vinte, [p=0.2] infinito *fechado:* [p=0.2] consumo acima de vinte. [p=0.4] "
        "{c}C: [p=0.2] aberto no vinte, [p=0.2] infinito aberto: [p=0.2] consumo acima de vinte."),
    dict(id="27", block="questao", text=
        "{d}D: [p=0.2] aberto no vinte, [p=0.2] infinito aberto: [p=0.2] consumo *a partir de* vinte. [p=0.4] "
        "{e}E: [p=0.2] fechado no vinte, [p=0.2] infinito fechado: [p=0.2] consumo a partir de vinte. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="28", block="questao", text=
        "{t}Vamos ler a reta. [p=0.3] {r1}Bolinha vazia no vinte: [p=0.2] o vinte *não* entra. [p=0.2] Braço empurrando. "
        "[p=0.4] {r2}Seta para a direita: [p=0.2] até mais infinito, [p=0.2] que é sempre aberto. [p=0.4] "
        "{r3}Em português: [p=0.2] *acima* de vinte. [p=0.4] {r}*Letra C.*"),
    dict(id="29", block="questao", text=
        "{t}E as erradas? [p=0.3] {a}A leu a bolinha vazia como se o vinte entrasse. [p=0.4] {b}B fechou o lado do infinito. "
        "[p=0.4] {d}D escreveu certo com colchetes, [p=0.2] mas traduziu errado: [p=0.2] confundiu acima de com a partir de. "
        "[p=0.4] {e}E cometeu dois erros juntos: [p=0.2] fechou o vinte [p=0.2] e fechou o infinito."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] colchete virado para o número: entra. "
        "[p=0.2] Virado para fora: não entra. [p=0.5] {b}Dois: [p=0.2] bolinha cheia entra; [p=0.2] bolinha vazia não. "
        "[p=0.5] {c}Três: [p=0.2] infinito é sempre aberto."),

    # ================= PONTE =================
    dict(id="31", block="ponte", text=
        "{t}Você viu conjuntos de *números.* [p=0.4] {a}Agora, vamos usar conjuntos de *pessoas,* [p=0.3] "
        "{b}na questão que cai quase todo ano no ENEM: [p=0.3] {c}*o diagrama de Venn.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] frete grátis acima de cem reais: [p=0.2] a compra de cem ganha? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
