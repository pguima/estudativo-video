# Roteiro — Função Composta e Função Inversa, Episódio 1 de 5: composição (máquinas em fila e a ordem que importa)
# Base: Estudos/Enem/estudos/01-matematica/30-funcao-composta-inversa.html — seções 02 e 03 + Questões 2 e 6 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   MÁQUINAS EM FILA: o que sai da primeira entra na segunda.
#   f(g(x)) se lê DE DENTRO PARA FORA: quem age primeiro é a de dentro.
#   MEIA E SAPATO: a ordem muda o resultado.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material (seções 02 e 03): g(x) = 2x + 1 e f(x) = x² − 1 → f(g(2)) = 24, g(f(2)) = 7, f(2) · g(2) = 15;
#   leis f(g(x)) = 4x² + 4x e g(f(x)) = 2x² − 1; "número antes de lei" com f(g(3)) = f(7) = 48.
# Concreto: o caixa da loja aparece SEM dizer qual ordem dá 117 e qual dá 115 (a Questão 6 é "você faz"). O gancho do
#   usuário já cita os dois preços; a Questão 6 cobra QUAL ordem é qual, a lei geral e as erradas. Mantido como desenhado.
# Nós fazemos (prompt): f(x) = 3x, g(x) = x + 4 → f(g(1)) = f(5) = 15 e g(f(1)) = g(3) = 7.
# QUESTÃO 2 ("eu faço", texto idêntico na tela): g(2) = 7, f(7) = 48 → E. Erradas como no material: A 9 = g(f(2)), ordem
#   trocada; B 10 = f(2) + g(2); C 21 = f(2) · g(2); D 24 = (2x + 3)² lido como 4x² + 9 (sem o termo do meio).
# QUESTÃO 6 ("você faz", com pausa): c(p) = p − 20, d(p) = 0,9p; d(c(150)) = 117, c(d(150)) = 115 → D (porcentagem antes,
#   R$ 2,00 mais barato). Lei geral 0,9p − 18 × 0,9p − 20. Erradas como no material (A comutativa; B conclusão invertida;
#   C confunde os R$ 18,00 efetivos do cupom com a diferença; E toma o cupom inteiro como diferença). Ponte com Descontos:
#   percentual com percentual comuta (0,8 · 0,9 = 0,9 · 0,8); reais com percentual, não.
# Atalhos (verde): "número antes de lei" · "confira a lei com um número" (4 · 2² + 4 · 2 = 24 = f(g(2))) · no caixa,
#   "porcentagem primeiro, cupom depois" (acréscimo nosso, conferido em Python).
# Frases-chave (meio e fim, idênticas): 1. O que sai de uma máquina entra na outra.
#   2. Leia de dentro para fora: a de dentro age primeiro. 3. Trocou a ordem, trocou o resultado.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Função composta do zero: a ordem das máquinas muda tudo | Composta e Inversa Ep. 1"
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
        "{a}Produto de *cento e cinquenta reais,* [p=0.2] um cupom de *vinte reais* [p=0.2] e *dez por cento* de "
        "desconto. [p=0.4] {b}Tanto faz a ordem? [p=0.4] {c}Não: [p=0.2] numa ordem você paga *cento e dezessete reais,* "
        "[p=0.2] na outra, *cento e quinze.* [p=0.4] {d}Hoje você descobre por quê, [p=0.2] e qual ordem pedir no caixa."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular *f de g de x* em um número [p=0.3] {b}e montar a *lei da "
        "composta,* [p=0.2] {c}sem trocar a ordem das máquinas."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Da série de Conceito de Função: [p=0.2] calcular *f de cinco* é "
        "trocar o x por cinco. [p=0.4] {b}E dá para trocar o x por uma *expressão inteira,* [p=0.2] sempre *entre "
        "parênteses.* [p=0.4] {c}Da série de Expressões algébricas: [p=0.2] dois x mais um, ao quadrado, [p=0.2] é "
        "*quatro x ao quadrado, mais quatro x, mais um.* [p=0.2] Com o termo do meio."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine uma fábrica. [p=0.3] {a}A primeira máquina *corta* a peça. [p=0.2] A segunda *pinta.* [p=0.4] "
        "{b}A peça que sai da primeira [p=0.2] entra direto na segunda. [p=0.4] {c}Agora o caixa de uma loja: [p=0.2] "
        "a etiqueta passa por *dois carimbos,* [p=0.2] o do cupom e o dos dez por cento. [p=0.4] {d}Nos dois casos, "
        "[p=0.2] uma etapa *alimenta* a outra."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}E como a matemática escreve essa fila? [p=0.4] {a}Assim: [p=0.2] *f de g de x.* [p=0.3] Isso se chama "
        "*função composta:* [p=0.2] uma função aplicada ao resultado de outra. [p=0.4] {b}Também se escreve *f bola g,* "
        "[p=0.2] com uma bolinha no meio. [p=0.4] {c}A *g* é a *função de dentro:* [p=0.2] ela age primeiro. [p=0.2] A "
        "*f* é a *função de fora:* [p=0.2] age depois."),
    dict(id="06", block="definicao", text=
        "{t}Repare numa coisa estranha. [p=0.3] {a}Você *escreve* o f primeiro, [p=0.2] mas quem *age* primeiro é o g. "
        "[p=0.4] {b}*f de g de x* se lê de dentro para fora. [p=0.4] {c}E um cuidado: [p=0.2] o que sai de g [p=0.2] "
        "precisa ser um número que *f aceita.* [p=0.2] Se f não aceita, [p=0.2] a fila trava."),

    # ================= BLOCO B: OS VALORES PASSANDO =================
    dict(id="07", block="maquinas", text=
        "{t}Vamos ligar as máquinas. [p=0.3] {a}A *g* faz *dois x mais um.* [p=0.2] A *f* faz *x ao quadrado, menos um.* "
        "[p=0.4] {b}Entra o número *dois* na g: [p=0.2] dois vezes dois, mais um: [p=0.2] sai *cinco.* [p=0.4] {c}O "
        "cinco desce pela esteira [p=0.2] e entra na f: [p=0.2] cinco ao quadrado, menos um: [p=0.2] sai *vinte e "
        "quatro.* [p=0.4] {d}Então *f de g de dois* é *vinte e quatro.*"),
    dict(id="08", block="maquinas", text=
        "{t}E se as máquinas trocarem de lugar? [p=0.4] {a}Agora o dois entra *primeiro na f:* [p=0.2] dois ao "
        "quadrado, menos um: [p=0.2] sai *três.* [p=0.4] {b}O três entra na g: [p=0.2] dois vezes três, mais um: "
        "[p=0.2] sai *sete.* [p=0.4] {c}Mesmo número na entrada, [p=0.2] mesmas máquinas, [p=0.2] e o resultado mudou: "
        "[p=0.2] *vinte e quatro* virou *sete.*"),

    # ================= BLOCO C: NÚMERO ANTES DE LEI =================
    dict(id="09", block="numero", text=
        "{t}E se a prova perguntar só *f de g de três?* [p=0.4] {a}Atalho: [p=0.2] *número antes de lei.* [p=0.2] Não "
        "monte fórmula nenhuma. [p=0.4] {b}Calcule *g de três:* [p=0.2] dois vezes três, mais um: [p=0.2] *sete.* "
        "[p=0.4] {c}Jogue o sete na f: [p=0.2] sete ao quadrado, menos um: [p=0.2] *quarenta e oito.* [p=0.4] {d}Dois "
        "passos curtos, [p=0.2] e quase nenhuma chance de errar a álgebra."),

    # ================= BLOCO D: A LEI DA COMPOSTA =================
    dict(id="10", block="lei", text=
        "{t}E quando a pergunta pede a *fórmula?* [p=0.4] {a}Aí você monta a *lei da composta:* [p=0.2] a regra que "
        "liga direto a entrada à saída. [p=0.4] {b}Na f, [p=0.2] troque cada x pela g inteira, [p=0.2] *entre "
        "parênteses:* [p=0.2] dois x mais um, ao quadrado, [p=0.2] menos um. [p=0.4] {c}Desenvolva com o termo do "
        "meio: [p=0.2] quatro x ao quadrado, mais quatro x, mais um, menos um. [p=0.4] {d}O mais um e o menos um se "
        "anulam: [p=0.2] *quatro x ao quadrado, mais quatro x.*"),
    dict(id="11", block="lei", text=
        "{t}E a outra ordem, *g de f de x?* [p=0.4] {a}Agora a de dentro é a f. [p=0.2] Na g, [p=0.2] troque o x por "
        "*x ao quadrado menos um,* entre parênteses: [p=0.2] dois vezes isso, mais um. [p=0.4] {b}Dois x ao quadrado, "
        "menos dois, mais um: [p=0.2] *dois x ao quadrado, menos um.* [p=0.4] {c}Duas leis *diferentes.* [p=0.3] Com x "
        "igual a dois: [p=0.2] uma dá vinte e quatro, [p=0.2] a outra dá sete."),
    dict(id="12", block="comuta", text=
        "{t}Isso tem nome. [p=0.3] {a}Uma operação é *comutativa* [p=0.2] quando a ordem não muda o resultado, [p=0.2] "
        "como na soma: [p=0.2] dois mais três é três mais dois. [p=0.4] {b}A composição, em geral, [p=0.2] *não é "
        "comutativa.* [p=0.3] f bola g é diferente de g bola f. [p=0.4] {c}Pense em *meia e sapato:* [p=0.2] meia e "
        "depois sapato, tudo certo. [p=0.2] Sapato e depois meia, [p=0.2] *não dá.* [p=0.3] A ordem muda o resultado."),
    dict(id="13", block="atalho", text=
        "{t}E como saber se a lei que você montou está certa? [p=0.4] {a}Atalho: [p=0.2] *confira com um número.* "
        "[p=0.4] {b}Ponha x igual a dois na lei: [p=0.2] quatro vezes quatro, mais quatro vezes dois: [p=0.2] *vinte e "
        "quatro.* [p=0.4] {c}É o mesmo vinte e quatro que as máquinas deram. [p=0.2] Bateu: [p=0.2] a lei está certa."),

    # ================= BLOCO E: NÃO É PRODUTO =================
    dict(id="14", block="produto", text=
        "{t}E se eu multiplicar f de dois por g de dois? [p=0.4] {a}f de dois é *três.* [p=0.2] g de dois é *cinco.* "
        "[p=0.2] Três vezes cinco: [p=0.2] *quinze.* [p=0.4] {b}Nada a ver com vinte e quatro. [p=0.4] {c}Compor *não "
        "é multiplicar.* [p=0.2] Na composição, [p=0.2] o resultado de uma máquina *entra* na outra. [p=0.2] Não se "
        "juntam dois resultados separados."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Com *f de x igual a três x* [p=0.2] e *g de x igual a x mais quatro,* [p=0.4] {b}calcule "
        "*f de g de um* [p=0.2] e *g de f de um.* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}*f de g de um:* [p=0.2] a de dentro é a g. [p=0.2] g de um, [p=0.2] um mais quatro, "
        "[p=0.2] *cinco.* [p=0.2] Depois f de cinco, [p=0.2] três vezes cinco, [p=0.2] *quinze.* [p=0.4] {b}*g de f de "
        "um:* [p=0.2] agora a de dentro é a f. [p=0.2] f de um, [p=0.2] *três.* [p=0.2] Depois g de três, [p=0.2] três "
        "mais quatro, [p=0.2] *sete.* [p=0.4] {c}Ordens diferentes, [p=0.2] resultados diferentes."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] o que sai de uma máquina entra na outra. [p=0.5] "
        "{b}Dois: [p=0.2] leia de dentro para fora: [p=0.2] a de dentro age primeiro. [p=0.5] {c}Três: [p=0.2] trocou a "
        "ordem, trocou o resultado."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] em *f de g de x,* [p=0.2] aplicar a *f "
        "primeiro.* [p=0.4] {b}Parece certo, [p=0.2] porque a gente lê da esquerda para a direita, [p=0.2] e o f vem "
        "antes. [p=0.4] {c}Mas a de dentro age primeiro: [p=0.2] *comece pela g.*"),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] achar que *f bola g é igual a g bola f.* [p=0.4] {b}Parece certo, [p=0.2] porque na soma "
        "e na multiplicação a ordem não importa. [p=0.4] {c}Mas a composição *não é comutativa.* [p=0.2] Com x igual "
        "a dois, [p=0.2] vinte e quatro contra sete."),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] *multiplicar* f de x por g de x [p=0.2] em vez de substituir. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque f de g lembra f vezes g, [p=0.2] como dois de três lembra dois vezes três. [p=0.4] {c}Mas "
        "compor é *colocar uma dentro da outra.* [p=0.2] O produto deu quinze; [p=0.2] a composta, vinte e quatro."),
    dict(id="21", block="erros", text=
        "{a}Quarto: [p=0.2] em *f de dois x mais um,* [p=0.2] elevar *só o x* ao quadrado: [p=0.2] dois x ao quadrado, "
        "mais um, menos um. [p=0.4] {b}Parece certo, [p=0.2] porque na f o quadrado está grudado no x. [p=0.4] {c}Mas "
        "o x foi trocado pela expressão *inteira.* [p=0.2] Ponha os parênteses: [p=0.2] *dois x mais um, ao quadrado,* "
        "menos um."),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="22", block="q2", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] Esta, [p=0.2] eu resolvo com você. "
        "[p=0.4] {a}Considere as funções *f de x igual a x ao quadrado, menos um,* [p=0.2] e *g de x igual a dois x mais "
        "três,* [p=0.2] definidas para todo x real. [p=0.2] O valor de *f de g de dois* é: [p=0.4] {qa}A: [p=0.2] nove. "
        "[p=0.3] {qb}B: [p=0.2] dez. [p=0.3] {qc}C: [p=0.2] vinte e um. [p=0.3] {qd}D: [p=0.2] vinte e quatro. [p=0.3] "
        "{qe}E: [p=0.2] quarenta e oito. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q2", text=
        "{t}A pergunta é um *número só.* [p=0.2] Então: [p=0.2] número antes de lei. [p=0.4] {a}De dentro para fora: "
        "[p=0.2] primeiro a g. [p=0.2] g de dois, [p=0.2] dois vezes dois, mais três: [p=0.2] *sete.* [p=0.4] {b}Agora o "
        "sete entra na f: [p=0.2] sete ao quadrado, menos um: [p=0.2] quarenta e nove menos um, [p=0.2] *quarenta e "
        "oito.* [p=0.4] {ok}*Letra E!*"),
    dict(id="24", block="q2", text=
        "{t}E repare: [p=0.2] cada alternativa errada é um erro clássico. [p=0.4] {xa}A A, nove, [p=0.2] *trocou a "
        "ordem:* [p=0.2] fez g de f de dois. [p=0.4] {xb}A B, dez, [p=0.2] *somou* f de dois com g de dois: [p=0.2] três "
        "mais sete. [p=0.4] {xc}A C, vinte e um, [p=0.2] *multiplicou:* [p=0.2] três vezes sete. [p=0.4] {xd}E a D, "
        "vinte e quatro, [p=0.2] desenvolveu dois x mais três, ao quadrado, [p=0.2] *sem o termo do meio:* [p=0.2] "
        "dezesseis mais nove, menos um."),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="25", block="q6", text=
        "{t}E a última é *sua:* [p=0.2] a do gancho. [p=0.4] {a}Uma loja oferece, para um produto de *cento e cinquenta "
        "reais,* [p=0.2] um cupom que abate *vinte reais* do preço [p=0.2] e uma promoção de *dez por cento* de "
        "desconto. [p=0.2] O sistema permite aplicar os dois, [p=0.2] em qualquer ordem, [p=0.2] sempre sobre o valor da "
        "etapa anterior. [p=0.2] Comparando as duas ordens, conclui-se que: [p=0.4] {qa}A: [p=0.2] o preço final é o "
        "mesmo nas duas ordens. [p=0.3] {qb}B: [p=0.2] aplicar o cupom antes é dois reais mais barato. [p=0.3] {qc}C: "
        "[p=0.2] aplicar o cupom antes é dezoito reais mais barato. [p=0.3] {qd}D: [p=0.2] aplicar a porcentagem antes "
        "é dois reais mais barato. [p=0.3] {qe}E: [p=0.2] aplicar a porcentagem antes é vinte reais mais barato. "
        "[p=0.5] {p}*Pause e resolva.* [p=2.0]"),
    dict(id="26", block="q6", text=
        "{t}Conferindo. [p=0.2] São *duas máquinas:* [p=0.2] o cupom, *c de p igual a p menos vinte,* [p=0.2] e o "
        "desconto, *d de p igual a zero vírgula nove p.* [p=0.4] {a}Cupom antes: [p=0.2] cento e cinquenta menos vinte, "
        "[p=0.2] cento e trinta. [p=0.2] Noventa por cento disso: [p=0.2] *cento e dezessete.* [p=0.4] {b}Porcentagem "
        "antes: [p=0.2] noventa por cento de cento e cinquenta, [p=0.2] cento e trinta e cinco. [p=0.2] Menos vinte: "
        "[p=0.2] *cento e quinze.* [p=0.4] {c}A porcentagem antes sai *dois reais mais barato.* [p=0.3] {ok}*Letra D!*"),
    dict(id="27", block="q6", text=
        "{t}E por que dois reais? [p=0.4] {a}Monte as duas leis. [p=0.2] Cupom antes: [p=0.2] *zero vírgula nove p, "
        "menos dezoito.* [p=0.2] Porcentagem antes: [p=0.2] *zero vírgula nove p, menos vinte.* [p=0.4] {b}Com o cupom "
        "antes, [p=0.2] os dez por cento caem também sobre os vinte reais do cupom, [p=0.2] e ele passa a valer só "
        "*dezoito.* [p=0.4] {c}Atalho de caixa: [p=0.2] peça a *porcentagem primeiro,* [p=0.2] e o cupom depois."),
    dict(id="28", block="q6", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] supõe que a composição é comutativa. [p=0.3] {xb}A B [p=0.2] *inverte* "
        "a conclusão. [p=0.3] {xc}A C [p=0.2] confunde os dezoito reais do cupom [p=0.2] com a diferença entre as ordens. "
        "[p=0.3] {xe}A E [p=0.2] toma o cupom inteiro como diferença. [p=0.4] {a}E na série de Descontos [p=0.2] você "
        "viu que dois descontos em porcentagem [p=0.2] podem vir em qualquer ordem. [p=0.2] Isso continua certo: "
        "[p=0.2] *multiplicar comuta.* [p=0.4] {b}O que não comuta [p=0.2] é misturar um desconto em *reais* com um em "
        "*porcentagem.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] o que sai de uma máquina entra na outra. "
        "[p=0.5] {b}Dois: [p=0.2] leia de dentro para fora: [p=0.2] a de dentro age primeiro. [p=0.5] {c}Três: [p=0.2] "
        "trocou a ordem, trocou o resultado."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}Uma fábrica faz *quarenta peças por hora,* [p=0.2] e cada peça custa *três reais* [p=0.2] mais um custo "
        "fixo. [p=0.4] {b}Qual é o custo em função das *horas,* [p=0.2] sem passar pelas peças? [p=0.5] {c}Próximo "
        "episódio."),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] no seu dia a dia, [p=0.2] onde a ordem das etapas muda o resultado? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
