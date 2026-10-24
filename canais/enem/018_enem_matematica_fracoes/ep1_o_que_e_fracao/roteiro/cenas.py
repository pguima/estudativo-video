# Roteiro — Frações, Decimais e Dízimas, Episódio 1 de 8: O que é uma fração (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/03-fracoes-decimais-dizimas.html — seções 02 e 03 (+ questão INÉDITA).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   PIZZA: o denominador diz em quantas fatias a pizza foi cortada; o numerador diz quantas você pegou.
#   EQUIVALENTES: a mesma quantidade de pizza cortada de jeitos diferentes (metade em 2, 4 ou 6 fatias).
#   "DE" = um sinal de VEZES disfarçado.
# Pré-requisitos (série 015): MDC = "a maior régua que mede tudo certinho"; atalho do varal (decomposição simultânea):
#   MDC = produto dos primos que dividiram TODOS ao mesmo tempo (84, 120 → 2, 2, 3 → MDC = 12).
# Números do material: 3/4 de 200 = 150 · 3 ÷ 4 = 0,75 · 2/5 de 300 = 120 · 1/2 = 2/4 = 3/6 = 50/100 = 0,5 ·
#   6/9 e 10/15 (6·15 = 90 = 9·10) · 84/120 → MDC 12 → 7/10. Exemplo próprio da dica: 15/25 de 40 = 3/5 de 40 = 24.
# QUESTÃO INÉDITA (situação hipotética, marcada na tela): 120 funcionários, 2/5 à noite (= 48), 18 fazem hora extra →
#   18/48 → MDC 6 → 3/8 (C). Erradas: A 3/20 (ignorou o "de": 18/120) · B 1/4 (subtraiu: 120 − 48 = 72 → 18/72) ·
#   D 18/48 (não simplificou) · E 3/48 (dividiu só o numerador por 6). Conferido: única correta.
# Frases-chave (meio e fim, idênticas):
#   1. Denominador: em quantas fatias. Numerador: quantas você pegou.
#   2. "De" significa vezes.
#   3. Simplificar é dividir em cima e embaixo pelo mesmo número; pelo MDC, de uma vez.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "O que é uma fração de verdade: os 4 significados e como simplificar · Matemática ENEM, episódio 1"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem trauma de fração: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
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
        "{a}Quase nunca cai uma questão *de frações* no ENEM. [p=0.5] {b}E mesmo assim, [p=0.2] a fração está em *dezenas* "
        "de questões: [p=0.3] {c}probabilidade, [p=0.2] porcentagem, [p=0.2] estatística, [p=0.2] Física. [p=0.5] {d}Ela é o "
        "passo que separa quem chega ao gabarito [p=0.2] *de quem para no meio.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai entender *o que uma fração significa* em cada enunciado, [p=0.4] "
        "{b}e simplificar qualquer fração *de uma vez só.* [p=0.4] {c}E se fração te dá arrepio, [p=0.2] calma: [p=0.2] a gente "
        "começa do zero, [p=0.2] com pizza."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Dividir é repartir em partes iguais: [p=0.2] doze dividido por quatro "
        "dá três. [p=0.4] {b}E o *MDC,* [p=0.2] da série anterior, [p=0.2] é a maior régua que mede tudo certinho: [p=0.2] "
        "o maior número que divide dois números ao mesmo tempo. [p=0.3] {c}O MDC de doze e dezoito é seis."),

    # ================= BLOCO A: A FRAÇÃO COMO PIZZA =================
    dict(id="04", block="pizza", text=
        "{t}Primeira pergunta: [p=0.2] você pede uma pizza cortada em *quatro* fatias [p=0.2] e come *três.* [p=0.4] "
        "Quanto da pizza você comeu? [p=0.5] {a}Três de quatro fatias. [p=0.3] {b}Em matemática, [p=0.2] isso se escreve "
        "assim: [p=0.2] *três quartos.* [p=0.4] {c}Isso é uma *fração:* [p=0.2] um jeito de escrever pedaços de um inteiro."),
    dict(id="05", block="pizza", text=
        "{t}O número de baixo tem nome: [p=0.2] *denominador.* [p=0.4] {a}Ele diz em *quantas fatias* a pizza foi cortada. "
        "[p=0.3] Aqui, [p=0.2] quatro."),
    dict(id="06", block="pizza", text=
        "{t}E o número de cima é o *numerador.* [p=0.4] {a}Ele diz *quantas fatias você pegou.* [p=0.3] Aqui, [p=0.2] três. "
        "[p=0.5] {b}Guarde assim: [p=0.2] denominador, [p=0.2] em quantas fatias; [p=0.2] numerador, [p=0.2] quantas você pegou."),

    # ================= BLOCO B: OS QUATRO SIGNIFICADOS =================
    dict(id="07", block="significados", text=
        "{t}Agora, uma surpresa: [p=0.2] três quartos *nem sempre* é pizza. [p=0.4] {a}A mesma fração tem *quatro "
        "significados,* [p=0.2] conforme o enunciado. [p=0.4] {b}E reconhecer qual está em jogo [p=0.2] evita montar a conta errada."),
    dict(id="08", block="significados", text=
        "{t}O primeiro você já conhece: [p=0.2] *parte-todo.* [p=0.4] {a}O todo foi dividido em quatro, [p=0.2] e você pegou "
        "três. [p=0.3] {b}Comeu três quartos da pizza."),
    dict(id="09", block="significados", text=
        "{t}O segundo é o *quociente,* [p=0.2] que é o resultado de uma divisão. [p=0.4] {a}Você tem *três barras* de chocolate "
        "para dividir entre *quatro pessoas.* [p=0.4] {b}Quanto cada uma ganha? [p=0.3] {c}Três dividido por quatro: [p=0.2] "
        "*zero vírgula setenta e cinco* barra por pessoa. [p=0.3] {d}Três quartos de barra para cada um."),
    dict(id="10", block="significados", text=
        "{t}O terceiro é a *razão:* [p=0.2] uma comparação entre duas quantidades. [p=0.4] {a}Numa turma, [p=0.2] há três "
        "meninos *para cada* quatro meninas. [p=0.4] {b}Atenção: [p=0.2] aqui o quatro *não é o total.* [p=0.3] {c}É só a "
        "quantidade de meninas, [p=0.2] comparada com a de meninos."),
    dict(id="11", block="significados", text=
        "{t}E o quarto é o *operador:* [p=0.2] a fração que age sobre uma quantidade. [p=0.4] {a}Três quartos de duzentos reais. "
        "[p=0.4] {b}Primeiro, [p=0.2] um quarto de duzentos: [p=0.2] duzentos dividido por quatro, [p=0.2] cinquenta. [p=0.4] "
        "{c}Você quer três quartos: [p=0.2] três vezes cinquenta, [p=0.2] *cento e cinquenta reais.*"),

    # ================= BLOCO C: "DE" = VEZES =================
    dict(id="12", block="de", text=
        "{t}E aqui está a palavra que resolve metade dos problemas: [p=0.3] *de.* [p=0.4] {a}Sempre que aparecer *de* entre uma "
        "fração e uma quantidade, [p=0.3] {b}ele é um sinal de *vezes* disfarçado. [p=0.4] {c}Três quartos de duzentos [p=0.2] "
        "é três quartos *vezes* duzentos."),
    dict(id="13", block="de", text=
        "{t}Mais um: [p=0.2] *dois quintos de trezentos alunos.* [p=0.4] {a}O atalho é este: [p=0.2] *divida pelo de baixo,* "
        "[p=0.2] {b}e *multiplique pelo de cima.* [p=0.4] {c}Trezentos dividido por cinco, [p=0.2] sessenta. [p=0.3] {d}Sessenta "
        "vezes dois, [p=0.2] *cento e vinte alunos.*"),

    # ================= BLOCO D: FRAÇÕES EQUIVALENTES =================
    dict(id="14", block="equivalentes", text=
        "{t}Agora, uma pergunta de pizzaria: [p=0.3] metade da pizza em *duas* fatias grandes, [p=0.2] ou em *quatro* fatias "
        "menores. [p=0.3] Em qual você come mais? [p=0.5] {a}Em nenhuma! [p=0.3] {b}Metade é metade. [p=0.4] {c}Frações assim "
        "têm nome: [p=0.2] *frações equivalentes,* [p=0.2] que representam a mesma quantidade, [p=0.2] escrita de outro jeito."),
    dict(id="15", block="equivalentes", text=
        "{t}Veja a mesma metade, [p=0.2] recortada. [p=0.4] {a}Um meio. [p=0.3] {b}Dois quartos. [p=0.3] {c}Três sextos. [p=0.3] "
        "{d}Cinquenta centésimos. [p=0.3] {e}E em decimal, [p=0.2] zero vírgula cinco. [p=0.5] {f}O pedaço não mudou de tamanho. "
        "[p=0.2] Só o *corte.*"),
    dict(id="16", block="equivalentes", text=
        "{t}E isso vira uma regra. [p=0.4] {a}Se você *multiplica* ou *divide* o de cima e o de baixo pelo *mesmo número,* [p=0.3] "
        "{b}o valor da fração não muda. [p=0.5] {c}Por quê? [p=0.2] Cortar cada fatia em duas [p=0.2] dobra as fatias que você pegou, "
        "[p=0.2] e dobra as fatias da pizza. [p=0.3] {d}A quantidade continua igual."),

    # ================= BLOCO E: PRODUTO CRUZADO =================
    dict(id="17", block="cruzado", text=
        "{t}E como saber se duas frações são equivalentes, [p=0.2] sem desenhar pizza? [p=0.4] {a}Por exemplo: [p=0.2] seis "
        "nonos e dez quinze avos. [p=0.4] {b}Use o *produto cruzado:* [p=0.2] multiplicar em xis. [p=0.4] {c}Seis vezes quinze, "
        "[p=0.2] noventa. [p=0.3] {d}Nove vezes dez, [p=0.2] noventa. [p=0.4] {e}Deu o mesmo? [p=0.2] *São equivalentes.*"),

    # ================= BLOCO F: SIMPLIFICAR =================
    dict(id="18", block="simplificar", text=
        "{t}Agora, imagine a fração *oitenta e quatro cento e vinte avos.* [p=0.3] Assusta, não assusta? [p=0.4] {a}*Simplificar* "
        "é dividir em cima e embaixo pelo mesmo número, [p=0.2] para escrever com números menores. [p=0.4] {b}Divide por dois: "
        "[p=0.2] quarenta e dois sessenta avos. [p=0.3] {c}Por dois de novo: [p=0.2] vinte e um trinta avos. [p=0.3] {d}Por três: "
        "[p=0.2] *sete décimos.*"),
    dict(id="19", block="simplificar", text=
        "{t}E sete décimos não simplifica mais: [p=0.3] {a}o único número que divide o sete e o dez ao mesmo tempo [p=0.2] é o *um.* "
        "[p=0.4] {b}Essa é a *fração irredutível:* [p=0.2] a que já está simplificada ao máximo."),
    dict(id="20", block="simplificar", text=
        "{t}Mas foram três passos. [p=0.3] Dá para fazer em *um?* [p=0.4] {a}Dá! [p=0.2] Divida pelo *MDC.* [p=0.4] {b}E o MDC sai "
        "rapidinho no varal da série anterior: [p=0.3] {c}oitenta e quatro e cento e vinte, [p=0.2] divididos juntos por dois, "
        "[p=0.2] por dois [p=0.2] e por três. [p=0.4] {d}Dois vezes dois vezes três: [p=0.2] MDC igual a *doze.* [p=0.4] "
        "{e}Oitenta e quatro dividido por doze, [p=0.2] sete. [p=0.3] Cento e vinte dividido por doze, [p=0.2] dez. [p=0.3] "
        "{f}*Sete décimos,* [p=0.2] de uma vez só."),

    # ================= BLOCO G: DICA DE PROVA =================
    dict(id="21", block="dica", text=
        "{t}E uma dica de prova que economiza muito tempo: [p=0.3] *simplifique ANTES de fazer as contas,* [p=0.2] nunca no fim. "
        "[p=0.5] {a}Quinze vinte e cinco avos de quarenta. [p=0.4] {b}Simplificando primeiro, [p=0.2] quinze vinte e cinco avos "
        "vira *três quintos.* [p=0.4] {c}E três quintos de quarenta é fácil: [p=0.2] quarenta dividido por cinco, [p=0.2] oito, "
        "[p=0.2] vezes três, [p=0.2] *vinte e quatro.* [p=0.4] {d}Números pequenos, [p=0.2] menos chance de errar."),

    # ================= NÓS FAZEMOS =================
    dict(id="22", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Duas contas. [p=0.4] {a}Primeira: [p=0.2] *três quartos de sessenta.* [p=0.4] {b}Segunda: "
        "[p=0.2] simplifique *dezoito vinte e quatro avos.* [p=0.4] {c}Pause o vídeo e calcule. [p=2.0]"),
    dict(id="23", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Três quartos de sessenta: [p=0.2] divide pelo de baixo, [p=0.2] sessenta dividido por "
        "quatro, [p=0.2] quinze. [p=0.3] Multiplica pelo de cima, [p=0.2] quinze vezes três, [p=0.2] *quarenta e cinco.* [p=0.5] "
        "{b}Dezoito vinte e quatro avos: [p=0.2] o MDC de dezoito e vinte e quatro é seis. [p=0.3] {c}Dezoito dividido por seis, "
        "[p=0.2] três. [p=0.2] Vinte e quatro dividido por seis, [p=0.2] quatro. [p=0.3] *Três quartos.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="24", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] denominador, [p=0.2] em quantas fatias. [p=0.2] Numerador, "
        "[p=0.2] quantas você pegou. [p=0.5] {b}Dois: [p=0.2] *de* significa vezes. [p=0.5] {c}Três: [p=0.2] simplificar é dividir "
        "em cima e embaixo pelo mesmo número; [p=0.2] pelo MDC, [p=0.2] de uma vez."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="25", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar ou subtrair* quando o enunciado diz três quartos "
        "*de* alguma coisa. [p=0.4] {b}Parece certo, [p=0.2] porque a palavra *de* não tem cara de conta. [p=0.4] {c}Mas *de* é "
        "vezes: [p=0.2] divide pelo de baixo [p=0.2] e multiplica pelo de cima."),
    dict(id="26", block="erros", text=
        "{a}Segundo: [p=0.2] simplificar *só o numerador,* [p=0.2] ou dividir os dois por números *diferentes.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque os números ficam menores. [p=0.4] {c}Mas aí a pizza muda de tamanho. [p=0.2] Em cima e "
        "embaixo, [p=0.2] *sempre pelo mesmo número.*"),
    dict(id="27", block="erros", text=
        "{a}Terceiro: [p=0.2] deixar a resposta *sem simplificar* [p=0.2] quando a questão pede a irredutível. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque a fração tem o mesmo valor. [p=0.4] {c}Mas o ENEM coloca a fração não simplificada [p=0.2] como "
        "alternativa errada. [p=0.2] Confira se ainda dá para dividir."),

    # ================= QUESTÃO INÉDITA =================
    dict(id="28", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {a}Uma empresa tem *cento e vinte* funcionários. [p=0.3] {b}Desses, "
        "[p=0.2] *dois quintos* trabalham no turno da noite. [p=0.4] {c}Entre os funcionários da noite, [p=0.2] *dezoito* fazem "
        "hora extra. [p=0.4] {d}Que fração dos funcionários do turno da noite faz hora extra, [p=0.2] na forma irredutível?"),
    dict(id="29", block="questao", text=
        "{a}A: [p=0.2] três vinte avos. [p=0.4] {b}B: [p=0.2] um quarto. [p=0.4] {c}C: [p=0.2] três oitavos. [p=0.4] {d}D: "
        "[p=0.2] dezoito quarenta e oito avos. [p=0.4] {e}E: [p=0.2] três quarenta e oito avos. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="30", block="questao", text=
        "{t}Vamos resolver. [p=0.3] {a}Primeiro, [p=0.2] quantos trabalham à noite? [p=0.2] Dois quintos *de* cento e vinte. "
        "[p=0.3] O *de* é vezes. [p=0.4] {b}Cento e vinte dividido por cinco, [p=0.2] vinte e quatro. [p=0.2] Vezes dois, [p=0.2] "
        "*quarenta e oito.* [p=0.4] {c}Dezoito de quarenta e oito: [p=0.2] dezoito quarenta e oito avos. [p=0.4] {d}O MDC de "
        "dezoito e quarenta e oito é seis. [p=0.3] Dividindo os dois por seis: [p=0.2] *três oitavos.* [p=0.3] {ok}*Letra C!*"),
    dict(id="31", block="questao", text=
        "{t}E as outras? [p=0.3] {xd}A D é a mesma fração, [p=0.2] *sem simplificar.* [p=0.4] {xe}A E dividiu *só o numerador* "
        "por seis. [p=0.4] {xb}A B subtraiu: [p=0.2] fez cento e vinte menos quarenta e oito, [p=0.2] e usou os funcionários do "
        "dia. [p=0.4] {xa}E a A esqueceu o *de:* [p=0.2] comparou os dezoito com os cento e vinte da empresa toda."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] denominador, [p=0.2] em quantas fatias. [p=0.2] Numerador, "
        "[p=0.2] quantas você pegou. [p=0.5] {b}Dois: [p=0.2] *de* significa vezes. [p=0.5] {c}Três: [p=0.2] simplificar é dividir "
        "em cima e embaixo pelo mesmo número; [p=0.2] pelo MDC, [p=0.2] de uma vez."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}E quando a fração passa de uma pizza inteira, [p=0.2] tipo *duas pizzas e três quartos?* [p=0.4] {b}E como saber qual "
        "fração é *maior?* [p=0.5] {c}Próximo episódio."),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quanto deu três quartos de sessenta para você? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
