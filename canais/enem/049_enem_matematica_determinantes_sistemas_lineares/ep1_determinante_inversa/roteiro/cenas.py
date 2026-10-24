# Roteiro — Determinantes e Sistemas Lineares, Episódio 1 de 5: o que é o determinante (2 × 2, Sarrus, Laplace e o
#   teste da inversa)
# Base: Estudos/Enem/estudos/01-matematica/34-determinantes-sistemas-lineares.html — seções 02, 03 e 05 + Questão 2
#   (seção 12). Propriedades ficam para o episódio 2.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   o determinante é o TESTE DA CHAVE: diferente de zero, a chave abre (tem inversa); zero, não abre.
#   o produto da secundária entra DE CASACO: entre parênteses, com o sinal dele, e só depois é subtraído.
#   Sarrus é o TIME VERDE contra o TIME VERMELHO: cada time soma o seu placar; no fim, verde menos vermelho, em bloco.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Exemplos NOSSOS (para não entregar a Q2, que é "você faz"):
#   pré-requisito de soma e produto: x² − 5x + 6 = 0 → 2 e 3 (o prompt pedia x² + x − 6 = 0, que é a equação da Q2 e
#   daria a resposta −3 e 2 antes da pausa);
#   bloco c: (x 4 / 1 x − 3) → x² − 3x − 4 = 0 → 4 e −1 (é o exemplo novo do próprio prompt).
#   Atalho de Laplace pela linha 2 (a que tem zero): −0 + 4·(2 − 15) − 1·(4 − 5) = −52 + 1 = −51 (conferido).
# Nós fazemos (prompt): (−2 3 / 4 −5) → 10 − 12 = −2; (1 2 0 / 0 1 3 / 2 0 1) → verdes 13, vermelhas 0 → 13.
# QUESTÃO 2 (texto idêntico na tela): matriz (x 3 / 2 x + 1); x(x + 1) − 6 = 0 → x² + x − 6 = 0 → −3 e 2 → D.
#   Erradas como o material: A esquece a secundária (x(x + 1) = 0 → 0 e −1); B troca os sinais das raízes; C soma o 6
#   (x² + x + 6 = 0 não tem raiz real); E acha uma raiz por tentativa e para.
# Ponte: (1 0 −1 / 3 2 1 / 5 4 3) tem det 0 (L3 = 2·L2 − L1), conferido; só citada.
# Frases-chave (meio e fim, idênticas): 1. Ordem 2: principal menos secundária, com o sinal dentro do produto.
#   2. Sarrus: some cada time e subtraia o bloco vermelho inteiro. 3. Determinante zero: a matriz não tem inversa.
# Contas conferidas em Python (numpy): 23, −51 (Sarrus e Laplace pelas linhas 1 e 2), −2, 13, 0; raízes 4/−1, 2/3, −3/2.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Determinante do zero: 2 × 2, Sarrus e o teste da inversa · Matemática ENEM, Determinantes episódio 1"

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
        "{a}Determinante de *três, menos dois, quatro e cinco.* [p=0.4] {b}Metade da turma escreve [p=0.2] *quinze menos "
        "oito, sete.* [p=0.4] {c}A resposta é *vinte e três.* [p=0.4] {d}E é esse número [p=0.2] que diz se uma matriz "
        "*tem inversa.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai calcular determinantes *dois por dois* e *três por três* [p=0.2] *sem errar "
        "sinal* [p=0.3] {b}e vai saber, [p=0.2] só por ele, [p=0.2] se uma matriz *tem inversa.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Sinais: [p=0.2] *menos vezes menos dá mais;* [p=0.2] menos vezes "
        "mais [p=0.2] dá menos. [p=0.4] {b}Da série de Matrizes: [p=0.2] a fórmula da inversa dois por dois [p=0.2] "
        "*divide* por *a d menos b c.* [p=0.4] {c}E da série de Equação do segundo grau: [p=0.2] em *x ao quadrado menos "
        "cinco x mais seis,* [p=0.2] dois números que somam cinco e multiplicam seis: [p=0.2] *dois e três.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Lembra da criptografia da série de Matrizes? [p=0.4] {a}A mensagem vira números, [p=0.2] e a *chave,* "
        "[p=0.2] uma matriz, [p=0.2] embaralha tudo. [p=0.4] {b}Para ler de volta, [p=0.2] usa-se a *inversa* da "
        "chave. [p=0.4] {c}Só que, às vezes, [p=0.2] a chave *não abre:* [p=0.2] ela não tem inversa. [p=0.4] {d}E existe "
        "*um único número* [p=0.2] que avisa isso antes. [p=0.2] Ele se chama *determinante.*"),

    # ================= BLOCO A: SÓ QUADRADAS =================
    dict(id="05", block="definicao", text=
        "{t}E qual matriz tem determinante? [p=0.4] {a}*Determinante* é um número [p=0.2] calculado a partir de uma "
        "matriz quadrada. [p=0.4] {b}Só as *quadradas* têm, [p=0.2] com o mesmo número de linhas e de colunas. [p=0.2] "
        "Uma dois por três [p=0.2] *não tem.* [p=0.4] {c}A *ordem* é esse tamanho: [p=0.2] ordem dois é dois por dois. "
        "[p=0.4] {d}E na ordem um, [p=0.2] o determinante é o próprio número: [p=0.2] o de *menos sete* [p=0.2] é *menos "
        "sete.*"),

    # ================= BLOCO B: ORDEM 2 =================
    dict(id="06", block="ordem2", text=
        "{t}E numa dois por dois? [p=0.4] {a}A *diagonal principal* [p=0.2] desce da esquerda para a direita: [p=0.2] "
        "*a* e *d.* [p=0.4] {b}A *diagonal secundária* [p=0.2] é a outra: [p=0.2] *b* e *c.* [p=0.4] {c}A regra: "
        "[p=0.2] *produto da principal menos produto da secundária.* [p=0.2] *A d menos b c.*"),
    dict(id="07", block="ordem2", text=
        "{t}Vamos ao gancho. [p=0.4] {a}Principal: [p=0.2] três vezes cinco, [p=0.2] *quinze.* [p=0.4] {b}Secundária: "
        "[p=0.2] menos dois vezes quatro, [p=0.2] *menos oito.* [p=0.4] {c}Agora o truque: [p=0.2] esse menos oito "
        "entra *de casaco,* [p=0.2] entre parênteses, [p=0.2] com o sinal dele. [p=0.4] {d}Quinze menos *menos oito:* "
        "[p=0.2] menos com menos dá mais. [p=0.2] Quinze mais oito, [p=0.2] *vinte e três.*"),
    dict(id="08", block="ordem2", text=
        "{t}Um atalho para nunca mais errar esse sinal. [p=0.4] {a}Calcule os *dois produtos completos* [p=0.2] e "
        "escreva cada um, [p=0.2] com sinal, [p=0.2] *antes* de subtrair. [p=0.4] {b}Quinze. [p=0.2] Menos oito, [p=0.2] "
        "de casaco. [p=0.4] {c}Só depois, [p=0.2] a conta: [p=0.2] quinze menos o casaco inteiro."),

    # ================= BLOCO C: DETERMINANTE NUMA EQUAÇÃO =================
    dict(id="09", block="equacao", text=
        "{t}E quando a matriz tem um *x* dentro? [p=0.4] {a}Matriz *x, quatro, um, x menos três.* [p=0.2] Para quais "
        "valores de x o determinante dá zero? [p=0.4] {b}Principal: [p=0.2] *x vezes x menos três.* [p=0.2] "
        "Secundária: [p=0.2] quatro vezes um, [p=0.2] *quatro.* [p=0.4] {c}Igualando a zero: [p=0.2] *x ao quadrado "
        "menos três x menos quatro, igual a zero.* [p=0.4] {d}Soma três, produto menos quatro: [p=0.2] *quatro e menos "
        "um.* [p=0.2] Conferindo o quatro: [p=0.2] quatro vezes um, [p=0.2] menos quatro: [p=0.2] *zero.* [p=0.4] {e}E por que "
        "procurar o zero? [p=0.2] Daqui a pouco você vai ver: [p=0.2] determinante zero [p=0.2] é a chave que *não abre.*"),

    # ================= BLOCO D: SARRUS =================
    dict(id="10", block="sarrus", text=
        "{t}E numa três por três? [p=0.4] {a}Aí entra a *regra de Sarrus:* [p=0.2] um jeito de calcular o determinante "
        "de ordem três [p=0.2] pelas diagonais. [p=0.4] {b}Primeiro passo: [p=0.2] *repita as duas primeiras colunas* "
        "à direita. [p=0.4] {c}Agora são dois times. [p=0.2] O *verde:* [p=0.2] três diagonais que descem para a "
        "*direita.* [p=0.2] O *vermelho:* [p=0.2] três que descem para a *esquerda.*"),
    dict(id="11", block="sarrus", text=
        "{t}O placar do time verde. [p=0.4] {a}Dois vezes quatro vezes um: [p=0.2] *oito.* [p=0.3] {b}Um vezes um vezes "
        "cinco: [p=0.2] *cinco.* [p=0.3] {c}Três vezes zero vezes dois: [p=0.2] *zero.* [p=0.4] {d}Verde: [p=0.2] "
        "*treze.*"),
    dict(id="12", block="sarrus", text=
        "{t}E o time vermelho. [p=0.4] {a}Três vezes quatro vezes cinco: [p=0.2] *sessenta.* [p=0.3] {b}Dois vezes um "
        "vezes dois: [p=0.2] *quatro.* [p=0.3] Um vezes zero vezes um: [p=0.2] *zero.* [p=0.2] Vermelho: [p=0.2] "
        "*sessenta e quatro.* [p=0.4] {c}Verde menos vermelho, [p=0.2] *em bloco:* [p=0.2] treze menos sessenta e "
        "quatro, [p=0.2] *menos cinquenta e um.* [p=0.4] {d}E atenção: [p=0.2] Sarrus *só vale* para três por três."),

    dict(id="13", block="sarrus", text=
        "{t}Um atalho para não se perder no meio das setas. [p=0.4] {a}Escreva o placar em *duas colunas:* [p=0.2] "
        "verde de um lado, [p=0.2] vermelho do outro. [p=0.4] {b}E olhe os *zeros:* [p=0.2] diagonal que passa por um "
        "zero [p=0.2] dá produto zero, [p=0.2] *sem conta.* [p=0.4] {c}Aqui, [p=0.2] o três, zero, dois [p=0.2] e o um, "
        "zero, um [p=0.2] já vão direto para o placar."),

    # ================= BLOCO E: LAPLACE =================
    dict(id="14", block="laplace", text=
        "{t}Tem outro caminho? [p=0.3] Tem. [p=0.4] {a}O *desenvolvimento de Laplace:* [p=0.2] escolha uma linha, "
        "[p=0.2] e trabalhe *um elemento de cada vez.* [p=0.4] {b}Para cada elemento, [p=0.2] risque a linha e a "
        "coluna dele. [p=0.2] Sobra uma dois por dois: [p=0.2] o *determinante que sobra.* [p=0.2] O nome técnico "
        "é *cofator.* [p=0.4] {c}E os sinais seguem o padrão [p=0.2] *mais, menos, mais,* [p=0.2] alternando como um *tabuleiro de "
        "xadrez* [p=0.2] que começa com mais no canto."),
    dict(id="15", block="laplace", text=
        "{t}Na mesma matriz, [p=0.2] pela primeira linha. [p=0.4] {a}O dois: [p=0.2] sobra *quatro menos dois,* "
        "[p=0.2] dois. [p=0.2] Dois vezes dois, [p=0.2] *quatro.* [p=0.4] {b}O um, [p=0.2] com sinal de menos: [p=0.2] "
        "sobra *zero menos cinco.* [p=0.2] Menos um vezes menos cinco, [p=0.2] *mais cinco.* [p=0.4] {c}O três: [p=0.2] "
        "sobra *zero menos vinte.* [p=0.2] Três vezes menos vinte, [p=0.2] *menos sessenta.* [p=0.4] {d}Quatro mais "
        "cinco menos sessenta: [p=0.2] *menos cinquenta e um.* [p=0.2] O mesmo resultado."),
    dict(id="16", block="laplace", text=
        "{t}E quando Laplace compensa? [p=0.4] {a}Atalho: [p=0.2] escolha a linha com *mais zeros.* [p=0.2] Zero vezes "
        "qualquer coisa [p=0.2] é zero, [p=0.2] e aquela parte *some.* [p=0.4] {b}A segunda linha começa com zero. "
        "[p=0.2] Os sinais dela: [p=0.2] *menos, mais, menos.* [p=0.4] {c}Quatro vezes menos treze, [p=0.2] menos "
        "cinquenta e dois. [p=0.2] Menos um vezes menos um, [p=0.2] mais um. [p=0.4] {d}*Menos cinquenta e um* de novo, "
        "[p=0.2] com uma conta a menos."),

    # ================= BLOCO F: O TESTE DA INVERSA =================
    dict(id="17", block="inversa", text=
        "{t}E a chave do começo? [p=0.4] {a}Uma matriz é *inversível* [p=0.2] quando tem inversa. [p=0.2] E ela tem "
        "inversa [p=0.2] *se, e somente se,* [p=0.2] o determinante for *diferente de zero.* [p=0.4] {b}Determinante "
        "zero: [p=0.2] a matriz é *singular.* [p=0.2] A chave *não abre.* [p=0.2] Exemplo: [p=0.2] *dois, quatro, um, dois:* [p=0.2] dois vezes dois "
        "menos quatro vezes um, [p=0.2] *zero.* [p=0.2] Essa não serve de chave. [p=0.4] {c}Por isso a fórmula da inversa "
        "[p=0.2] divide por a d menos b c: [p=0.2] se ele é zero, [p=0.2] a divisão é *impossível.*"),
    dict(id="18", block="inversa", text=
        "{t}E dá para saber mais alguma coisa? [p=0.4] {a}O determinante da inversa [p=0.2] é *um dividido pelo "
        "determinante.* [p=0.2] Se o da matriz é quatro, [p=0.2] o da inversa é *zero vírgula vinte e cinco,* [p=0.2] porque a matriz vezes a inversa "
        "dá a identidade, [p=0.2] e o determinante da identidade [p=0.2] é *um.* [p=0.4] "
        "{b}E para achar os valores de x [p=0.2] que *estragam* a chave: [p=0.2] resolva *determinante igual a zero.* "
        "[p=0.4] {c}Foi exatamente o que fizemos com o *quatro* e o *menos um.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Calcule o determinante de [p=0.2] *menos dois, três, quatro, menos cinco.* [p=0.4] "
        "{b}E o da três por três [p=0.2] *um, dois, zero; [p=0.2] zero, um, três; [p=0.2] dois, zero, um.* [p=0.4] "
        "{c}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Principal: [p=0.2] menos dois vezes menos cinco, [p=0.2] *dez.* [p=0.2] Secundária: "
        "[p=0.2] três vezes quatro, [p=0.2] doze. [p=0.2] Dez menos doze, [p=0.2] *menos dois.* [p=0.4] {b}Na três por "
        "três, [p=0.2] time verde: [p=0.2] um, [p=0.2] doze [p=0.2] e zero, [p=0.2] *treze.* [p=0.4] {c}Time vermelho: "
        "[p=0.2] as três diagonais passam por um zero: [p=0.2] *zero.* [p=0.2] Treze menos zero, [p=0.2] *treze.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] ordem dois: [p=0.2] principal menos secundária, "
        "[p=0.2] com o sinal dentro do produto. [p=0.5] {b}Dois: [p=0.2] Sarrus: [p=0.2] some cada time [p=0.2] e "
        "subtraia o bloco vermelho inteiro. [p=0.5] {c}Três: [p=0.2] determinante zero: [p=0.2] a matriz não tem "
        "inversa."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] escrever *quinze menos oito* [p=0.2] em vez de "
        "*quinze menos menos oito.* [p=0.4] {b}Parece certo, [p=0.2] porque a regra diz *menos,* [p=0.2] e o oito "
        "parece só um número. [p=0.4] {c}Mas o produto era *menos oito.* [p=0.2] Ele entra de casaco: [p=0.2] *vinte e "
        "três,* [p=0.2] não sete."),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] em Sarrus, [p=0.2] subtrair *só o primeiro* produto vermelho, [p=0.2] e somar os "
        "outros. [p=0.4] {b}Parece certo, [p=0.2] porque o sinal de menos [p=0.2] aparece uma vez só, [p=0.2] na "
        "frente do sessenta. [p=0.4] {c}Mas o menos vale para o *time inteiro:* [p=0.2] some o vermelho primeiro, "
        "[p=0.2] sessenta e quatro, [p=0.2] e subtraia *em bloco.*"),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] usar Sarrus [p=0.2] numa *quatro por quatro.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "a ideia das diagonais [p=0.2] parece que cresce junto com a matriz. [p=0.4] {c}Mas não cresce: [p=0.2] Sarrus "
        "*só vale* para três por três. [p=0.2] Numa quatro por quatro, [p=0.2] use *Laplace.*"),

    # ================= QUESTÃO 2 (VOCÊ FAZ) =================
    dict(id="25", block="q2", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] E esta é *sua.* [p=0.4] "
        "{a}Um sistema de criptografia [p=0.2] só pode usar como chave uma matriz que tenha inversa. [p=0.2] Para a "
        "matriz [p=0.2] *x, três, dois, x mais um,* [p=0.2] os valores reais de x [p=0.2] que a tornam inadequada como "
        "chave são: [p=0.4] {qa}A: [p=0.2] zero e menos um. [p=0.3] {qb}B: [p=0.2] menos dois e três. [p=0.3] {qc}C: "
        "[p=0.2] nenhum: ela sempre tem inversa. [p=0.3] {qd}D: [p=0.2] menos três e dois. [p=0.3] {qe}E: [p=0.2] apenas "
        "dois. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="26", block="q2", text=
        "{t}Conferindo. [p=0.3] {a}*Inadequada* quer dizer: [p=0.2] *sem inversa.* [p=0.2] Ou seja, [p=0.2] determinante "
        "*zero.* [p=0.4] {b}Principal: [p=0.2] x vezes x mais um. [p=0.2] Secundária: [p=0.2] três vezes dois, [p=0.2] "
        "*seis.* [p=0.2] Fica: [p=0.2] *x ao quadrado mais x menos seis, igual a zero.* [p=0.4] {c}Soma menos um, "
        "produto menos seis: [p=0.2] *menos três e dois.* [p=0.4] {d}Conferindo o dois: [p=0.2] dois vezes três, "
        "[p=0.2] menos seis: [p=0.2] zero. [p=0.2] E o menos três: [p=0.2] menos três vezes menos dois, [p=0.2] seis, "
        "[p=0.2] menos seis: [p=0.2] zero. [p=0.3] {ok}*Letra D!*"),
    dict(id="27", block="q2", text=
        "{t}E as outras? [p=0.3] {xa}A A [p=0.2] esqueceu a *secundária:* [p=0.2] resolveu só x vezes x mais um, igual a "
        "zero. [p=0.4] {xb}A B [p=0.2] achou os números certos [p=0.2] com os *sinais trocados.* [p=0.4] {xc}A C "
        "[p=0.2] *somou* o seis em vez de subtrair, [p=0.2] e essa equação não tem raiz real. [p=0.4] {xe}E a E "
        "[p=0.2] achou o dois por tentativa [p=0.2] e *parou:* [p=0.2] esqueceu que equação do segundo grau [p=0.2] "
        "pode ter *duas* raízes."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] ordem dois: [p=0.2] principal menos secundária, "
        "[p=0.2] com o sinal dentro do produto. [p=0.5] {b}Dois: [p=0.2] Sarrus: [p=0.2] some cada time [p=0.2] e "
        "subtraia o bloco vermelho inteiro. [p=0.5] {c}Três: [p=0.2] determinante zero: [p=0.2] a matriz não tem "
        "inversa."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Precisa mesmo fazer Sarrus em [p=0.2] *um, zero, menos um; [p=0.2] três, dois, um; [p=0.2] cinco, quatro, "
        "três?* [p=0.5] {b}Dá para ver que o resultado é *zero* [p=0.2] sem conta nenhuma. [p=0.4] {c}Próximo "
        "episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha escrito quinze menos oito? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
