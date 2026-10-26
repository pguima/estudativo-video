# Roteiro — Operações e Conjuntos Numéricos, Episódio 2: Os conjuntos numéricos — racional ou irracional? (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/01-operacoes-e-conjuntos-numericos.html — seções 02 e 03 + Questão 6 da seção 12
#   (fração geratriz, seção 04, NÃO é ensinada: só se diz que existe e que terá vídeo próprio)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: BONECAS RUSSAS. ℕ cabe dentro de ℤ, que cabe dentro de ℚ, que cabe dentro de ℝ.
#   Os irracionais são outra boneca, do lado de fora de ℚ, mas dentro de ℝ.
# Ritual de classificação (sempre o mesmo, visível na tela): escreva em decimal → olhe depois da vírgula →
#   acaba? repete? nem acaba nem repete?
# Frases-chave (meio e fim, idênticas):
#   1. Naturais dentro dos inteiros, dentro dos racionais, dentro dos reais; os irracionais ficam ao lado dos racionais.
#   2. Acaba ou repete: racional. Nem acaba nem repete: irracional.
#   3. Raiz de quadrado perfeito é racional.
# Na narração, os símbolos são falados pela letra ("a letra N"); na tela aparecem ℕ ℤ ℚ 𝕀 ℝ ⊂ ∪.

TITULO = "O Número Que Nunca Termina: Racional ou Irracional? | Matemática Básica Ep. 2"
PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Existe um número que *nunca termina* [p=0.3] {b}e *nunca se repete.* [p=0.5] {c}Os gregos descobriram isso "
        "medindo a diagonal de um quadrado. [p=0.4] {d}E, segundo a lenda, [p=0.2] isso causou um *escândalo.* [p=0.5] "
        "{e}Hoje, ele cai no ENEM."),
    dict(id="02", block="promessa", text=
        "{a}Até o fim desta aula, [p=0.2] você vai olhar para *qualquer* número [p=0.3] {b}e dizer, em segundos, [p=0.2] "
        "se ele é *racional* ou *irracional.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, duas lembranças rápidas. [p=0.3] {a}*Fração* é uma divisão escrita de outro jeito. [p=0.3] "
        "{b}Três quartos é três dividido por quatro, [p=0.2] *zero vírgula setenta e cinco:* [p=0.2] a forma *decimal,* com vírgula. [p=0.4] "
        "{c}O número de cima se chama *numerador.* [p=0.3] {d}O de baixo, *denominador:* [p=0.2] em quantas partes você dividiu."),
    dict(id="04", block="prereq", text=
        "{t}E a *raiz quadrada* é o caminho de volta do quadrado. [p=0.4] {a}Três ao quadrado, [p=0.2] três vezes três, "
        "[p=0.2] dá nove. [p=0.4] {b}Então a raiz quadrada de nove [p=0.2] é *três:* [p=0.2] o número que, "
        "vezes ele mesmo, [p=0.2] dá nove."),

    # ================= CONJUNTO =================
    dict(id="05", block="conjunto", text=
        "{t}Agora, a palavra principal da aula: [p=0.2] *conjunto.* [p=0.4] {a}Conjunto é um grupo de coisas [p=0.2] "
        "que têm algo em comum. [p=0.3] Como o conjunto dos dias da semana. [p=0.4] {b}Na matemática, [p=0.2] "
        "a gente lista os itens do conjunto entre *chaves.*"),
    dict(id="06", block="historia", text=
        "{t}E os números não nasceram todos de uma vez. [p=0.4] {a}Cada tipo de número foi inventado [p=0.2] "
        "quando apareceu um *problema* [p=0.2] que os números antigos não resolviam."),

    # ================= BLOCO A: NATURAIS =================
    dict(id="07", block="naturais", text=
        "{t}Qual foi o primeiro problema? [p=0.4] {a}*Contar.* [p=0.3] Um pastor quer saber [p=0.2] quantas ovelhas tem. "
        "[p=0.4] {b}Um, dois, três... [p=0.4] {c}Esses números de contar [p=0.2] se chamam *naturais.* [p=0.4] "
        "{d}O símbolo é um *N* maiúsculo, [p=0.2] com um traço duplo."),
    dict(id="08", block="naturais", text=
        "{t}E o zero? [p=0.3] {a}No Brasil, [p=0.2] o zero *é* natural: [p=0.2] zero ovelhas no pasto. [p=0.4] "
        "{b}Então os naturais são: [p=0.2] zero, um, dois, três, [p=0.2] e os três pontinhos, [p=0.2] "
        "que querem dizer *continua para sempre.*"),

    # ================= BLOCO B: INTEIROS =================
    dict(id="09", block="inteiros", text=
        "{t}Mas e se você tem três reais [p=0.2] e gasta cinco? [p=0.4] {a}Ou se o termômetro marca *menos dois graus?* "
        "[p=0.4] {b}Os naturais não dão conta: [p=0.2] eles não têm nada abaixo do zero."),
    dict(id="10", block="inteiros", text=
        "{t}Entram os *negativos.* [p=0.4] {a}Juntando os negativos com os naturais, [p=0.2] você tem os *inteiros.* "
        "[p=0.4] {b}O símbolo é um *Z,* [p=0.2] de *Zahlen,* [p=0.2] que é números em alemão. [p=0.4] "
        "{c}Menos dois, menos um, zero, um, dois... [p=0.2] para os dois lados."),
    dict(id="11", block="inteiros", text=
        "{t}E repare: [p=0.2] todo natural *também* é inteiro. [p=0.4] {a}É como as *bonecas russas,* [p=0.2] "
        "aquelas bonecas de madeira [p=0.2] que se encaixam uma dentro da outra. [p=0.4] "
        "{b}A boneca dos naturais [p=0.2] cabe *dentro* da boneca dos inteiros."),

    # ================= BLOCO C: RACIONAIS =================
    dict(id="12", block="racionais", text=
        "{t}Próximo problema: [p=0.2] uma pizza cortada em quatro pedaços. [p=0.4] {a}Você come três. [p=0.3] "
        "Quanto da pizza você comeu? [p=0.4] {b}*Três quartos.* [p=0.3] {c}E três quartos não é inteiro: [p=0.2] "
        "fica entre o zero e o um."),
    dict(id="13", block="racionais", text=
        "{t}Os números que podem ser escritos como *fração de inteiros* [p=0.2] se chamam *racionais.* [p=0.4] "
        "{a}O símbolo é um *Q,* [p=0.2] de quociente, [p=0.2] o resultado de uma divisão. [p=0.4] "
        "{b}Com uma regra: [p=0.2] o denominador *não pode ser zero.* [p=0.3] {c}Não existe cortar uma pizza em zero pedaços."),
    dict(id="14", block="racionais", text=
        "{t}Exemplos: [p=0.2] {a}um meio. [p=0.3] {b}Zero vírgula setenta e cinco, [p=0.2] que é três quartos. [p=0.3] "
        "{c}E até o menos cinco, [p=0.2] que é menos cinco sobre um. [p=0.4] {d}Todo inteiro vira fração. [p=0.3] "
        "{e}Então a boneca dos inteiros [p=0.2] cabe *dentro* da boneca dos racionais."),

    # ================= BLOCO D: IRRACIONAIS =================
    dict(id="15", block="irracionais", text=
        "{t}Será que fração resolve tudo? [p=0.4] Os gregos achavam que sim. [p=0.4] {a}Até que mediram a *diagonal* "
        "de um quadrado de lado um. [p=0.4] {b}A diagonal é a linha que corta o quadrado de um canto ao outro."),
    dict(id="16", block="irracionais", text=
        "{t}Quanto mede essa diagonal? [p=0.4] {a}Se você desenha um quadrado em cima dela, [p=0.2] "
        "ele tem área *dois:* [p=0.2] o dobro do quadrado pequeno, [p=0.2] que tem área um. [p=0.4] {b}Então a diagonal é o número que, "
        "vezes ele mesmo, dá dois. [p=0.4] {c}É a *raiz de dois.*"),
    dict(id="17", block="irracionais", text=
        "{t}E a raiz de dois em decimal? [p=0.3] {a}Um vírgula quatro, um, quatro, dois, um, três, cinco... [p=0.4] "
        "{b}*Nunca termina.* [p=0.3] {c}E *nunca se repete.* [p=0.4] {d}Nenhuma fração de inteiros chega nela. "
        "[p=0.3] Foi esse o escândalo."),
    dict(id="18", block="irracionais", text=
        "{t}Esses números se chamam *irracionais:* [p=0.3] {a}decimais *infinitos,* [p=0.2] que *não se repetem.* [p=0.4] "
        "{b}O símbolo é um *I.* [p=0.4] {c}E na história das bonecas, [p=0.2] eles são *outra* boneca, [p=0.2] "
        "{d}que fica *do lado de fora* dos racionais."),

    # ================= BLOCO E: REAIS =================
    dict(id="19", block="reais", text=
        "{t}E onde fica a raiz de dois? [p=0.4] {a}Na reta numérica, [p=0.2] entre o um e o dois. [p=0.4] "
        "{b}Se só existissem os racionais, [p=0.2] a reta teria *buracos.* [p=0.4] {c}Os irracionais tapam esses buracos."),
    dict(id="20", block="reais", text=
        "{t}Juntando racionais e irracionais, [p=0.2] você tem os *reais,* [p=0.2] {a}com o símbolo *R.* [p=0.4] "
        "{b}É a reta inteira, [p=0.2] *sem nenhum buraco.* [p=0.4] {c}Esse juntar tem nome: [p=0.2] *união,* "
        "[p=0.2] e o símbolo parece um *U.* [p=0.4] {d}Reais é igual a racionais união irracionais."),

    # ================= BLOCO F: A CADEIA =================
    dict(id="21", block="cadeia", text=
        "{t}Agora, as bonecas inteiras. [p=0.4] {a}Existe um símbolo que quer dizer *está contido em:* [p=0.2] "
        "cabe dentro de. [p=0.4] {b}Naturais está contido em inteiros, [p=0.2] {c}que está contido em racionais, "
        "[p=0.2] {d}que está contido em reais."),
    dict(id="22", block="cadeia", text=
        "{t}Mas o caminho de volta *não vale.* [p=0.4] {a}Menos cinco é inteiro, [p=0.2] mas *não* é natural. [p=0.4] "
        "{b}Um meio é racional, [p=0.2] mas *não* é inteiro."),
    dict(id="23", block="cadeia", text=
        "{t}E os irracionais? [p=0.3] {a}Eles ficam *fora* dessa fila. [p=0.3] São reais, [p=0.2] mas não são racionais. "
        "[p=0.4] {b}Os reais são uma caixa com *duas metades* [p=0.2] que não se tocam: [p=0.3] {c}de um lado, os racionais. "
        "[p=0.3] {d}Do outro, os irracionais."),

    # ================= BLOCO G: NOTAÇÕES =================
    dict(id="24", block="notacoes", text=
        "{t}Nos enunciados, esses símbolos às vezes vêm com enfeites. [p=0.4] "
        "{a}O *asterisco* tira o zero. [p=0.3] {b}Naturais com asterisco: [p=0.2] um, dois, três... [p=0.4] "
        "{c}Reais com asterisco: [p=0.2] todos os reais, menos o zero."),
    dict(id="25", block="notacoes", text=
        "{t}E um sinalzinho embaixo do Z [p=0.2] escolhe um lado. [p=0.4] {a}Com o *mais,* [p=0.2] fica o zero "
        "e os positivos. [p=0.4] {b}Com o *menos,* [p=0.2] fica o zero e os negativos. [p=0.4] "
        "{c}E com o asterisco e o mais juntos, [p=0.2] só os positivos, [p=0.2] sem o zero."),

    # ================= BLOCO H: O CRITÉRIO =================
    dict(id="26", block="criterio", text=
        "{t}E agora, a pergunta que o ENEM faz de verdade: [p=0.3] {a}esse número é racional ou irracional? [p=0.4] "
        "{b}O teste é sempre o mesmo. [p=0.3] {c}Escreva em decimal. [p=0.3] {d}Olhe depois da vírgula. [p=0.3] "
        "{e}E pergunte: [p=0.2] acaba? [p=0.2] repete? [p=0.2] ou nem acaba nem repete?"),
    dict(id="27", block="criterio", text=
        "{t}Três quartos: [p=0.2] zero vírgula setenta e cinco. [p=0.3] {a}*Acaba.* [p=0.3] {b}Isso se chama "
        "*decimal exato.* [p=0.3] {c}É racional."),
    dict(id="28", block="criterio", text=
        "{t}Um terço: [p=0.2] zero vírgula três, três, três, três... [p=0.4] {a}Não acaba, [p=0.2] mas *repete.* "
        "[p=0.4] {b}Isso se chama *dízima periódica.* [p=0.3] {c}E o pedaço que repete, o três, [p=0.2] "
        "se chama *período.* [p=0.4] {d}Também é racional: [p=0.2] toda dízima periódica tem uma fração que a gera. "
        "[p=0.3] {e}Como achar essa fração, [p=0.2] fica para um vídeo próprio."),
    dict(id="29", block="criterio", text=
        "{t}E a raiz de dois: [p=0.2] um vírgula quatro, um, quatro, dois, um, três, cinco... [p=0.4] "
        "{a}*Nem acaba, nem repete.* [p=0.3] {b}Irracional. [p=0.5] {c}A regra: [p=0.2] acaba ou repete, [p=0.2] "
        "racional. [p=0.3] Nem acaba nem repete, [p=0.2] irracional."),

    # ================= BLOCO I: OS IRRACIONAIS DA PROVA =================
    dict(id="30", block="famosos", text=
        "{t}E quais irracionais caem na prova? [p=0.4] {a}Primeiro, as *raízes que não são exatas:* [p=0.2] "
        "raiz de dois, [p=0.2] de três, [p=0.2] de cinco, [p=0.2] de dez."),
    dict(id="31", block="famosos", text=
        "{t}Depois, três números famosos. [p=0.3] {a}O *pi:* [p=0.2] três vírgula um, quatro, um, cinco, nove... "
        "[p=0.2] é o contorno de qualquer círculo [p=0.2] dividido pela largura dele. [p=0.4] {b}O número *e,* "
        "[p=0.2] dois vírgula setenta e um, [p=0.2] que aparece em contas de crescimento. [p=0.4] "
        "{c}E o *número de ouro,* [p=0.2] um vírgula seiscentos e dezoito, [p=0.2] das questões de arte, arquitetura e natureza."),

    # ================= BLOCO J: A PEGADINHA DA RAIZ =================
    dict(id="32", block="raiz_exata", text=
        "{t}Então todo número com raiz é irracional? [p=0.4] {a}*Não.* [p=0.3] {b}Raiz de nove é *três.* [p=0.3] "
        "Três é inteiro, [p=0.2] logo racional. [p=0.4] {c}Raiz de zero vírgula vinte e cinco [p=0.2] é *zero vírgula cinco,* "
        "[p=0.2] porque zero vírgula cinco vezes zero vírgula cinco dá zero vírgula vinte e cinco. [p=0.4] "
        "{d}Raiz de dezesseis vinte e cinco avos [p=0.2] é *quatro quintos.*"),
    dict(id="33", block="raiz_exata", text=
        "{t}O segredo é o *quadrado perfeito:* [p=0.2] um número que é um inteiro vezes ele mesmo. [p=0.4] "
        "{a}Um, quatro, nove, dezesseis, vinte e cinco... [p=0.2] até quatrocentos, que é vinte vezes vinte. [p=0.4] "
        "{b}Essa é a sua lista de *raízes exatas.* [p=0.4] {c}Raiz de quadrado perfeito [p=0.2] dá número certinho: "
        "[p=0.2] é racional."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="34", block="recap", text=
        "{t}Vamos juntar tudo em três frases. [p=0.5] {a}Um: [p=0.2] naturais dentro dos inteiros, dentro dos racionais, "
        "dentro dos reais; [p=0.2] os irracionais ficam ao lado dos racionais. [p=0.5] {b}Dois: [p=0.2] acaba ou repete, "
        "racional. [p=0.2] Nem acaba nem repete, irracional. [p=0.5] {c}Três: [p=0.2] raiz de quadrado perfeito é racional."),

    # ================= BLOCO K: TRUQUE PARA ORDENAR =================
    dict(id="35", block="ordenar", text=
        "{t}E quando a questão mistura raiz, fração e decimal, [p=0.2] e pede a ordem? [p=0.4] {a}O truque: "
        "[p=0.2] passe *tudo* para decimal. [p=0.4] {b}Guarde quatro valores: [p=0.2] raiz de dois, um vírgula quarenta e um. "
        "[p=0.3] Raiz de três, um vírgula setenta e três. [p=0.3] Raiz de cinco, dois vírgula vinte e quatro. "
        "[p=0.3] E pi, três vírgula catorze."),
    dict(id="36", block="ordenar", text=
        "{t}Exemplo: [p=0.2] raiz de três, [p=0.2] um vírgula sete [p=0.2] e sete quartos. [p=0.4] "
        "{a}Raiz de três, um vírgula setenta e três. [p=0.3] {b}Sete quartos, sete dividido por quatro, [p=0.2] "
        "um vírgula setenta e cinco. [p=0.4] {c}Do menor para o maior: [p=0.2] um vírgula sete, [p=0.2] raiz de três, "
        "[p=0.2] sete quartos."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="37", block="erro1", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] achar que dízima periódica é irracional. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque ela também nunca termina. [p=0.4] {c}Mas ela *repete.* [p=0.3] "
        "Repetiu, tem fração. [p=0.2] *Racional.*"),
    dict(id="38", block="erro2", text=
        "{a}Segundo: [p=0.2] achar que todo número com raiz é irracional. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque os irracionais famosos são raízes. [p=0.4] {c}Mas raiz de quadrado perfeito é exata. [p=0.3] "
        "Raiz de nove é três: [p=0.2] *racional.*"),
    dict(id="39", block="erro3", text=
        "{a}Terceiro: [p=0.2] achar que vinte e dois sétimos é irracional, [p=0.2] porque é o pi. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque muita gente usa vinte e dois sétimos no lugar do pi. [p=0.4] "
        "{c}Mas é só uma *aproximação.* [p=0.3] Vinte e dois sétimos é fração de inteiros: [p=0.2] *racional.*"),

    # ================= EXERCÍCIO RÁPIDO =================
    dict(id="40", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Classifique: [p=0.2] {a}zero vírgula setenta e cinco, [p=0.3] {b}raiz de dezesseis, "
        "[p=0.3] {c}raiz de sete, [p=0.3] {d}e zero vírgula quatro, quatro, quatro, quatro... [p=0.4] "
        "{p}*Pause o vídeo e classifique.* [p=1.5]"),
    dict(id="41", block="exercicio", text=
        "{t}Conferindo. [p=0.3] {a}Zero vírgula setenta e cinco acaba: [p=0.2] racional. [p=0.3] {b}Raiz de dezesseis "
        "é quatro: [p=0.2] racional. [p=0.3] {c}Sete não é quadrado perfeito; [p=0.2] raiz de sete nem acaba nem repete: "
        "[p=0.2] *irracional.* [p=0.3] {d}Zero vírgula quatro, quatro, quatro repete: [p=0.2] racional."),

    # ================= QUESTÃO 6 =================
    dict(id="42", block="questao", text=
        "{t}Hora de treinar, no estilo do ENEM. [p=0.4] {e1}Considere os números: [p=0.3] raiz de nove, [p=0.2] "
        "raiz de dez, [p=0.2] um vírgula dois, três, dois, três, repetindo, [p=0.3] pi, [p=0.2] vinte e dois sétimos "
        "[p=0.2] e raiz de dezesseis vinte e cinco avos. [p=0.4] {e2}Quantos deles são irracionais?"),
    dict(id="43", block="questao", text=
        "{t}As alternativas: [p=0.2] {a}A, um. [p=0.2] {b}B, dois. [p=0.2] {c}C, três. [p=0.2] {d}D, quatro. "
        "[p=0.2] {e}E, cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="44", block="questao", text=
        "{t}Vamos fazer o teste, um por um. [p=0.4] {n1}Raiz de nove: [p=0.2] nove é quadrado perfeito, [p=0.2] "
        "dá três. [p=0.2] Racional. [p=0.4] {n2}Raiz de dez: [p=0.2] dez não é quadrado perfeito. [p=0.2] "
        "Nem acaba nem repete. [p=0.2] *Irracional.*"),
    dict(id="45", block="questao", text=
        "{n3}Um vírgula dois, três, dois, três: [p=0.2] repete. [p=0.2] Dízima periódica, [p=0.2] racional. [p=0.4] "
        "{n4}Pi: [p=0.2] *irracional.* [p=0.4] {n5}Vinte e dois sétimos: [p=0.2] parece o pi, [p=0.2] mas é fração. "
        "[p=0.2] Racional. [p=0.4] {n6}Raiz de dezesseis vinte e cinco avos: [p=0.2] quatro quintos. [p=0.2] Racional."),
    dict(id="46", block="questao", text=
        "{t}Sobraram *dois* irracionais: [p=0.2] raiz de dez e pi. [p=0.3] {r}*Letra B.* [p=0.5] "
        "{a}A, um, [p=0.2] é de quem achou que só o pi é irracional. [p=0.4] {c}C, três, [p=0.2] caiu na pegadinha "
        "do vinte e dois sétimos."),
    dict(id="47", block="questao", text=
        "{d}D, quatro, [p=0.2] contou também a dízima, [p=0.2] que repete e é racional. [p=0.4] {e}A letra E, cinco, "
        "[p=0.2] é de quem acha que toda raiz é irracional, [p=0.2] e ainda contou a dízima."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="48", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] naturais dentro dos inteiros, dentro dos racionais, "
        "dentro dos reais; [p=0.2] os irracionais ficam ao lado dos racionais. [p=0.5] {b}Dois: [p=0.2] acaba ou repete, "
        "racional. [p=0.2] Nem acaba nem repete, irracional. [p=0.5] {c}Três: [p=0.2] raiz de quadrado perfeito é racional."),

    # ================= PONTE =================
    dict(id="49", block="ponte", text=
        "{t}A reta real não tem buracos. [p=0.4] {a}Mas e quando a questão quer só um *pedaço* dela, [p=0.2] "
        "tipo de dois até cinco? [p=0.5] {b}No próximo episódio: [p=0.2] *intervalos reais.*"),
    dict(id="50", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na pegadinha do vinte e dois sétimos? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
