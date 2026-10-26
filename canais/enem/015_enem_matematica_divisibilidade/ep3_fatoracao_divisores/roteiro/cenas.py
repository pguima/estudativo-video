# Roteiro — Matemática ENEM, Divisibilidade, Primos, MMC e MDC, Episódio 3 de 7: Fatoração em primos e a fórmula de
#   quantos divisores um número tem (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/02-divisibilidade-primos-mmc-mdc.html — seções 05 e 06 + Questão 4 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   RECEITA: a fatoração é a receita do número — quais tijolos primos e quantos de cada. Todo número tem uma receita única.
#   LANCHE: montar um divisor é como montar um lanche — cada primo entra de 0 até o seu expoente; multiplicam-se as escolhas.
# Contas na narração por extenso; na tela, notação normal (2³ · 3² · 5).
# Questão 4: enunciado e alternativas como no material. A resolução do material diz que a alternativa A (12) é "a armadilha de
#   quem multiplica os expoentes sem somar 1: 3·2·1 = 6, ou de quem soma errado" — mas 3·2·1 dá 6, não 12. O 12 sai de quem
#   esquece o expoente 1 do 5: (3+1)(2+1) = 12. A narração usa a explicação que bate com a conta e cita que o 6 nem está nas opções.
#   B (18) sai de errar a fatoração (2² em vez de 2³): 3·3·2 = 18. C (20) e E (36) não saem de erro clássico da fórmula.
# Frases-chave (meio e fim, idênticas):
#   1. Fatorar é achar a receita de primos do número.
#   2. Divida sempre pelo menor primo possível.
#   3. Divisores: some 1 em cada expoente e multiplique.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "O 360 Tem 24 Divisores: Descubra em 15 Segundos | Divisibilidade Ep. 3"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, soe como quem está raciocinando de verdade, passo a passo. Ritmo didático e "
            "tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está "
            "escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}O *trezentos e sessenta* tem *vinte e quatro* divisores. [p=0.5] {b}Dá para descobrir isso em *quinze segundos,* "
        "[p=0.3] {c}sem listar nenhum deles."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *fatorar* qualquer número em primos [p=0.4] {b}e contar os seus divisores "
        "[p=0.2] com uma *fórmula.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, duas lembranças rápidas. [p=0.3] {a}*Primo* é o número que tem exatamente dois divisores: [p=0.2] o um e "
        "ele mesmo. [p=0.3] {b}Dois, [p=0.2] três, [p=0.2] cinco, [p=0.2] sete, [p=0.2] onze... [p=0.3] {c}São os *tijolos* "
        "do episódio dois."),
    dict(id="04", block="prereq", text=
        "{t}E *potência* é multiplicação repetida. [p=0.3] {a}Dois elevado a três [p=0.2] é dois vezes dois vezes dois: "
        "[p=0.2] *oito.* [p=0.4] {b}O numerozinho de cima se chama *expoente:* [p=0.2] diz quantas vezes o número aparece. "
        "[p=0.4] {c}E um detalhe que vai ser importante hoje: [p=0.2] qualquer número elevado a *zero* [p=0.2] dá *um.*"),

    # ================= BLOCO A: A RECEITA =================
    dict(id="05", block="receita", text=
        "{t}O que uma receita de bolo te diz? [p=0.4] {a}Quais ingredientes entram: [p=0.2] farinha, [p=0.2] ovo, [p=0.2] "
        "açúcar. [p=0.3] {b}E *quanto* de cada um: [p=0.2] três ovos, [p=0.2] duas xícaras. [p=0.4] {c}Com a receita, "
        "[p=0.2] você sabe exatamente do que o bolo é feito."),
    dict(id="06", block="receita", text=
        "{t}E se um número tivesse receita? [p=0.4] {a}*Fatorar* [p=0.2] é escrever um número como uma multiplicação. "
        "[p=0.3] {b}Doze é dois vezes seis. [p=0.3] {c}Cada número dessa multiplicação [p=0.2] se chama *fator.*"),
    dict(id="07", block="receita", text=
        "{t}Mas o seis ainda dá para quebrar: [p=0.2] seis é dois vezes três. [p=0.4] {a}Quando todos os fatores são primos, "
        "[p=0.2] a gente chama de *fatoração em primos.* [p=0.4] {b}Doze é dois vezes dois vezes três. [p=0.3] {c}Essa é a "
        "*receita* do doze: [p=0.2] dois tijolos dois [p=0.2] e um tijolo três."),
    dict(id="08", block="teorema", text=
        "{t}E será que o mesmo número pode ter duas receitas diferentes? [p=0.5] {a}Não. [p=0.3] Isso tem até um nome "
        "pomposo: [p=0.2] *teorema fundamental da aritmética.* [p=0.4] {b}Ele diz que todo número maior que um [p=0.2] é uma "
        "multiplicação de primos [p=0.2] de *uma única maneira.* [p=0.4] {c}Só a ordem dos fatores pode mudar. [p=0.3] "
        "{d}A receita é *única.*"),

    # ================= BLOCO B: COMO FATORAR (EU FAÇO) =================
    dict(id="09", block="varal", text=
        "{t}E como achar a receita do trezentos e sessenta? [p=0.4] {a}A regra é uma só: [p=0.2] divida sempre pelo *menor "
        "primo possível,* [p=0.2] até chegar a *um.* [p=0.4] {b}Eu escrevo o número à esquerda [p=0.2] e o primo à direita. "
        "[p=0.3] Esse esquema se chama *varal.*"),
    dict(id="10", block="varal", text=
        "{a}Trezentos e sessenta é par, [p=0.2] então divide por dois: [p=0.2] *cento e oitenta.* [p=0.4] {b}Cento e oitenta "
        "ainda é par: [p=0.2] dois de novo, [p=0.2] *noventa.* [p=0.4] {c}Noventa é par: [p=0.2] dois, [p=0.2] "
        "*quarenta e cinco.* [p=0.4] {d}Quarenta e cinco é ímpar. [p=0.2] O dois não divide mais. [p=0.3] Próximo primo: "
        "[p=0.2] o *três.*"),
    dict(id="11", block="varal", text=
        "{a}Quatro mais cinco dá nove, [p=0.2] então o três divide: [p=0.2] *quinze.* [p=0.4] {b}Três de novo: [p=0.2] "
        "*cinco.* [p=0.4] {c}O cinco não divide por três. [p=0.2] Próximo primo: [p=0.2] o *cinco.* [p=0.2] Cinco dividido "
        "por cinco, [p=0.2] *um.* [p=0.4] {d}Chegou a um: [p=0.2] *acabou.*"),
    dict(id="12", block="varal", text=
        "{t}Agora eu leio a coluna da direita. [p=0.3] {a}Três vezes o dois: [p=0.2] *dois ao cubo.* [p=0.3] {b}Duas vezes o "
        "três: [p=0.2] *três ao quadrado.* [p=0.3] {c}E um cinco. [p=0.4] {d}Trezentos e sessenta [p=0.2] é dois ao cubo, "
        "[p=0.2] vezes três ao quadrado, [p=0.2] vezes cinco. [p=0.4] {e}Conferindo: [p=0.2] oito vezes nove, [p=0.2] "
        "setenta e dois; [p=0.2] vezes cinco, [p=0.2] *trezentos e sessenta.* [p=0.2] Fechou!"),

    # ================= NÓS FAZEMOS =================
    dict(id="13", block="nos", text=
        "{t}Sua vez. [p=0.3] {a}Pegue papel e fatore *setenta e dois* [p=0.2] {b}e *cento e vinte.* [p=0.3] {c}Lembre: "
        "[p=0.2] sempre o menor primo, [p=0.2] até chegar a um. [p=0.4] {p}*Pause o vídeo.* [p=2.0]"),
    dict(id="14", block="nos", text=
        "{t}Conferindo. [p=0.3] {a}Setenta e dois: [p=0.2] trinta e seis, [p=0.2] dezoito, [p=0.2] nove, [p=0.2] com três "
        "dois; [p=0.3] depois três, [p=0.2] um, [p=0.2] com dois três. [p=0.3] {b}Setenta e dois é dois ao cubo vezes três "
        "ao quadrado. [p=0.5] {c}Cento e vinte: [p=0.2] sessenta, [p=0.2] trinta, [p=0.2] quinze, [p=0.2] com três dois; "
        "[p=0.3] depois cinco, [p=0.2] um. [p=0.3] {d}Cento e vinte é dois ao cubo vezes três vezes cinco."),

    # ================= BLOCO D: POR QUE IMPORTA =================
    dict(id="15", block="importa", text=
        "{t}Tá, [p=0.2] mas para que serve essa receita? [p=0.4] {a}Para quase tudo deste assunto. [p=0.3] {b}O MMC, "
        "[p=0.2] {c}o MDC [p=0.2] {d}e a contagem de divisores [p=0.2] saem *todos* da fatoração. [p=0.4] {e}E a contagem "
        "a gente faz agora."),

    # ================= BLOCO E/F: A FÓRMULA DOS DIVISORES =================
    dict(id="16", block="lanche", text=
        "{t}Imagine uma lanchonete. [p=0.3] {a}Dois tipos de pão. [p=0.3] {b}Três tipos de recheio. [p=0.4] {c}Quantos "
        "lanches diferentes dá para montar? [p=0.4] {d}Para cada pão, [p=0.2] três recheios: [p=0.2] dois vezes três, "
        "[p=0.2] *seis lanches.* [p=0.4] {e}Quando as escolhas são independentes, [p=0.2] *multiplica.*"),
    dict(id="17", block="lanche", text=
        "{t}E o que isso tem a ver com divisores? [p=0.4] {a}Doze é dois ao quadrado vezes três. [p=0.3] {b}Todo divisor do "
        "doze [p=0.2] é feito só com esses tijolos. [p=0.4] {c}O dois pode entrar *zero,* [p=0.2] *uma* ou *duas* vezes: "
        "[p=0.2] três escolhas. [p=0.4] {d}O três pode entrar *zero* ou *uma* vez: [p=0.2] duas escolhas. [p=0.4] {e}Três "
        "vezes duas: [p=0.2] *seis divisores.*"),
    dict(id="18", block="lanche", text=
        "{t}Vamos montar os seis. [p=0.3] {a}Nenhum dois e nenhum três: [p=0.2] *um.* [p=0.3] {b}Um dois: [p=0.2] *dois.* "
        "[p=0.3] {c}Dois dois: [p=0.2] *quatro.* [p=0.3] {d}Só o três: [p=0.2] *três.* [p=0.3] {e}Dois vezes três: "
        "[p=0.2] *seis.* [p=0.3] {f}Quatro vezes três: [p=0.2] *doze.* [p=0.4] {g}Um, dois, três, quatro, seis e doze: "
        "[p=0.2] a mesma lista do episódio um!"),
    dict(id="19", block="mais1", text=
        "{t}Repare no *zero.* [p=0.3] {a}O divisor um [p=0.2] é o lanche sem nenhum tijolo. [p=0.3] {b}É o dois elevado a "
        "zero, [p=0.2] que vale um. [p=0.4] {c}Por isso, [p=0.2] cada primo tem uma escolha *a mais* [p=0.2] do que o seu "
        "expoente. [p=0.4] {d}Expoente dois? [p=0.2] Três escolhas: [p=0.2] zero, um ou dois."),
    dict(id="20", block="formula", text=
        "{t}E está pronta a fórmula. [p=0.3] {a}Fatore o número. [p=0.3] {b}Some *um* a cada expoente. [p=0.3] {c}E "
        "*multiplique* os resultados."),
    dict(id="21", block="formula", text=
        "{t}Agora, o trezentos e sessenta. [p=0.3] {a}Dois ao cubo: [p=0.2] o dois entra zero, um, dois ou três vezes. "
        "[p=0.2] Quatro escolhas. [p=0.4] {b}Três ao quadrado: [p=0.2] zero, um ou dois. [p=0.2] Três escolhas. [p=0.4] "
        "{c}E o cinco, [p=0.2] que está elevado a um: [p=0.2] zero ou um. [p=0.2] Duas escolhas. [p=0.4] {d}Quatro vezes "
        "três vezes dois: [p=0.2] *vinte e quatro divisores.* [p=0.3] {e}Quinze segundos, [p=0.2] sem listar nenhum."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="22", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] fatorar é achar a receita de primos do número. [p=0.5] "
        "{b}Dois: [p=0.2] divida sempre pelo menor primo possível. [p=0.5] {c}Três: [p=0.2] divisores: [p=0.2] some um em "
        "cada expoente e multiplique."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="23", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] multiplicar os expoentes *sem somar um.* [p=0.2] "
        "Três vezes dois vezes um: [p=0.2] seis. [p=0.4] {b}Parece certo, [p=0.2] porque os expoentes dizem quantas vezes "
        "cada primo aparece. [p=0.4] {c}Mas esquece a escolha do *zero:* [p=0.2] o certo é quatro vezes três vezes dois."),
    dict(id="24", block="erros", text=
        "{a}Segundo: [p=0.2] esquecer o expoente *um* [p=0.2] de quem aparece sozinho, [p=0.2] como o cinco. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque esse expoente nem vem escrito. [p=0.4] {c}Mas cinco é cinco elevado a um: [p=0.2] "
        "ele também ganha o seu mais um."),
    dict(id="25", block="erros", text=
        "{a}Terceiro: [p=0.2] *parar a fatoração* antes de chegar a um. [p=0.2] Por exemplo, [p=0.2] parar no quarenta e "
        "cinco. [p=0.4] {b}Parece certo, [p=0.2] porque o número já ficou pequeno. [p=0.4] {c}Mas quarenta e cinco não é "
        "primo: [p=0.2] é três ao quadrado vezes cinco. [p=0.2] Só pare no *um.*"),

    # ================= QUESTÃO 4 =================
    dict(id="26", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {a}Quantos divisores positivos tem o número trezentos e sessenta? "
        "[p=0.4] {b}A: [p=0.2] doze. [p=0.3] {c}B: [p=0.2] dezoito. [p=0.3] {d}C: [p=0.2] vinte. [p=0.3] {e}D: [p=0.2] "
        "vinte e quatro. [p=0.3] {f}E: [p=0.2] trinta e seis. [p=0.4] {p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="27", block="q4", text=
        "{t}Vamos lá. [p=0.3] {a}Fatorando: [p=0.2] dois ao cubo, [p=0.2] vezes três ao quadrado, [p=0.2] vezes cinco "
        "elevado a um. [p=0.4] {b}Soma um a cada expoente: [p=0.2] quatro, três e dois. [p=0.3] {c}Multiplica: [p=0.2] "
        "*vinte e quatro.* [p=0.3] {ok}*Letra D!*"),
    dict(id="28", block="q4", text=
        "{t}E as armadilhas? [p=0.3] {xa}A letra A, doze, [p=0.2] é de quem esquece o mais um do cinco: [p=0.2] quatro vezes "
        "três. [p=0.4] {xb}A B, dezoito, [p=0.2] é de quem erra a fatoração [p=0.2] e acha dois ao quadrado no lugar de dois "
        "ao cubo. [p=0.4] {x6}E quem multiplica os expoentes sem somar um [p=0.2] chega a seis, [p=0.2] que nem está nas "
        "opções. [p=0.3] Se o seu resultado não aparece, [p=0.2] desconfie da conta."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] fatorar é achar a receita de primos do número. "
        "[p=0.5] {b}Dois: [p=0.2] divida sempre pelo menor primo possível. [p=0.5] {c}Três: [p=0.2] divisores: [p=0.2] some "
        "um em cada expoente e multiplique."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}Com a receita de primos na mão, [p=0.2] você está pronto para a questão que cai quase todo ano: [p=0.3] "
        "{b}ônibus, [p=0.2] lâmpadas [p=0.2] e remédios [p=0.2] que voltam a coincidir. [p=0.4] {c}Próximo episódio: "
        "[p=0.2] *MMC.*"),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantos divisores tem o setenta e dois? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
