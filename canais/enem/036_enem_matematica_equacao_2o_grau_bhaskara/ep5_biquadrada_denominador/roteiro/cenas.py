# Roteiro — Equação do 2º Grau e Fórmula de Bhaskara, Episódio 5 de 6: equações que viram do 2º grau (biquadradas e x no
#   denominador).
# Base: Estudos/Enem/estudos/01-matematica/21-equacao-2o-grau-bhaskara.html — seção 08 + Questão 8 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A TROCA DE VARIÁVEL É UMA FANTASIA: o x² se veste de y, a equação vira do 2º grau, e no final a fantasia TEM de sair.
#   Y NEGATIVO É BILHETE SEM VALOR: nenhum x ao quadrado dá negativo (o bilhete rasgado com "sem raiz real").
#   O VALOR PROIBIDO CONTINUA PROIBIDO: multiplicar pelo x do denominador só vale com x ≠ 0.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (todos conferidos em Python):
#   Concreto: 3⁴ = 81 = 9². Bloco a/b: x⁴ − 13x² + 36 = 0 → y² − 13y + 36 = 0 → y = 4 ou 9 (soma 13, produto 36) → ±2 e ±3
#   (2⁴ − 13·4 + 36 = 16 − 52 + 36 = 0). Bloco d: 6/x = x − 1 → (x ≠ 0) x² − x − 6 = 0 → 3 e −2 (6/3 = 2 = 3 − 1;
#   6/(−2) = −3 = −2 − 1).
#   Erro 3 (exemplo nosso): x²/x = 5 → x² = 5x → x² − 5x = 0 → 0 ou 5; o zero é o valor proibido → só 5.
# Nós fazemos (prompt): x⁴ − 10x² + 9 = 0 → y = 1 ou 9 → ±1 e ±3 (quatro raízes).
# QUESTÃO 8 (você faz, texto idêntico): y² − 5y − 36 = 0, Δ = 25 + 144 = 169, y = (5 ± 13)/2 → 9 ou −4 → ±3; x² = −4 sem raiz
#   real → duas soluções → C. Erradas (material/prompt): E aceita x² = −4 como ±2 (quatro); B fica só com o 3 (uma);
#   A acha que o y negativo invalida tudo (nenhuma). D (três): o material diz só "mistura as duas coisas"; a explicação é
#   NOSSA: fica com o 3 e o −3 e ainda conta o y = −4 como se fosse mais uma resposta.
#   (O material escreve "y = (5 ± 13/2)"; o vídeo usa a forma certa (5 ± 13)/2.)
# Acréscimos nossos (verde): soma e produto no y; "anote o proibido antes de multiplicar"; o atalho do produto dos y
#   (c/a negativo → um y de cada sinal → exatamente duas raízes reais), usado como conferência DEPOIS da Questão 8.
# Frases-chave (meio e fim, idênticas): 1. Na biquadrada, x² vira y. 2. Não pare no y: volte para x. 3. y negativo não gera
#   raiz real.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Equação biquadrada e x no denominador: não pare no y · Matemática ENEM, 2º grau episódio 5"

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
        "{a}*x elevado à quarta, menos treze x ao quadrado, mais trinta e seis, igual a zero,* [p=0.3] tem *quatro "
        "respostas.* [p=0.5] {b}*x elevado à quarta, menos cinco x ao quadrado, menos trinta e seis, igual a zero,* "
        "[p=0.3] que parece igual, [p=0.2] tem *só duas.* [p=0.5] {c}O que muda é um *detalhe* [p=0.2] que muita gente "
        "ignora."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai resolver *biquadradas* [p=0.3] {b}e equações com *x no denominador* [p=0.3] "
        "{c}usando o que você *já sabe.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio três: [p=0.2] *soma e produto.* [p=0.2] Soma sete e produto dez: "
        "[p=0.2] *dois e cinco.* [p=0.4] {b}Do "
        "episódio um: [p=0.2] *x ao quadrado igual a vinte e cinco* [p=0.2] dá *cinco ou menos cinco.* [p=0.4] {c}E da "
        "Potenciação: [p=0.2] *x ao quadrado, elevado ao quadrado,* [p=0.2] é *x elevado à quarta.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Quanto é *três elevado à quarta?* [p=0.5] {a}Três vezes três vezes três vezes três: [p=0.2] *oitenta e um.* "
        "[p=0.4] {b}Junte de dois em dois: [p=0.2] *nove vezes nove,* [p=0.2] *oitenta e um* de novo. [p=0.4] {c}Então *x elevado à quarta* [p=0.2] é só *x ao quadrado, ao quadrado:* [p=0.2] "
        "um *quadrado de um quadrado.*"),

    # ================= BLOCO A: A TROCA DE VARIÁVEL =================
    dict(id="05", block="biquadrada", text=
        "{t}E que equação é essa do começo? [p=0.4] {a}Uma *equação biquadrada:* [p=0.2] a que só tem *x elevado à quarta, "
        "x ao quadrado e número.* [p=0.2] Nenhum x sozinho. [p=0.4] {b}O truque é a *troca de variável:* [p=0.2] dar um "
        "nome novo a um pedaço. [p=0.4] {c}O x ao quadrado *veste uma fantasia* [p=0.2] e passa a se chamar *y.*"),
    dict(id="06", block="biquadrada", text=
        "{t}E o que acontece com a equação? [p=0.4] {a}Se x ao quadrado é y, [p=0.2] x elevado à quarta é *y ao "
        "quadrado.* [p=0.4] {b}Fica: [p=0.2] *y ao quadrado, menos treze y, mais trinta e seis, igual a zero.* [p=0.4] {c}Soma treze, produto trinta e seis: [p=0.2] "
        "*quatro e nove.* [p=0.4] {d}Atalho: [p=0.2] no y, use *soma e produto* antes de pensar em fórmula."),

    # ================= BLOCO B: A VOLTA =================
    dict(id="07", block="volta", text=
        "{t}Acabou? [p=0.4] {a}*Não.* [p=0.2] Quatro e nove são valores de *y.* [p=0.2] A pergunta era o *x.* [p=0.4] "
        "{b}A fantasia *tem de sair.* [p=0.4] {c}Se y é quatro, [p=0.2] *x ao quadrado igual a quatro:* [p=0.2] *dois ou "
        "menos dois.* [p=0.4] {d}Se y é nove, [p=0.2] *x ao quadrado igual a nove:* [p=0.2] *três ou menos três.* [p=0.4] "
        "{e}*Quatro raízes.* [p=0.2] Confira o dois: [p=0.2] dezesseis, menos cinquenta e dois, mais trinta e seis: "
        "[p=0.2] *zero.*"),

    # ================= BLOCO C: A REGRA DA VOLTA =================
    dict(id="08", block="regra", text=
        "{t}E todo y vira duas raízes? [p=0.4] {a}Cada y *positivo* [p=0.2] dá *duas:* [p=0.2] o mais e o menos. [p=0.4] "
        "{b}y igual a *zero* [p=0.2] dá *uma só:* [p=0.2] o próprio zero. [p=0.4] {c}E y *negativo* [p=0.2] não dá "
        "*nenhuma.* [p=0.4] {d}Nenhum número ao quadrado dá negativo. [p=0.2] y negativo é *bilhete sem valor:* [p=0.2] "
        "rasgue."),

    # ================= BLOCO D: x NO DENOMINADOR =================
    dict(id="09", block="denominador", text=
        "{t}E quando o x aparece *embaixo* de uma fração? [p=0.4] {a}*Seis sobre x, igual a x menos um.* [p=0.4] {b}Antes "
        "de tudo, a *condição de existência:* [p=0.2] o valor que o x *não pode* ter. [p=0.2] Não existe divisão por zero, "
        "[p=0.2] então *x diferente de zero.* [p=0.4] {c}Agora multiplique os dois lados por x: "
        "[p=0.2] *seis igual a x ao quadrado, menos x.*"),
    dict(id="10", block="denominador", text=
        "{t}E agora? [p=0.4] {a}Arrume: [p=0.2] *x ao quadrado, menos x, menos seis, igual a zero.* [p=0.4] {b}Soma um, "
        "produto menos seis: [p=0.2] *três e menos dois.* [p=0.4] {c}Alguma delas é o zero proibido? [p=0.2] *Não.* "
        "[p=0.2] Então as duas servem. [p=0.4] {d}Confira: [p=0.2] seis sobre três é dois, [p=0.2] e três menos um, *dois.* "
        "[p=0.2] Seis sobre menos dois é menos três, [p=0.2] e menos dois menos um, *menos três.*"),
    dict(id="11", block="denominador", text=
        "{t}Atalho para o x no denominador. [p=0.3] {a}*Anote o proibido* antes de multiplicar. [p=0.4] {b}No fim, [p=0.2] "
        "*risque* quem cair nele. [p=0.3] O valor proibido *continua proibido.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="12", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quantas raízes reais tem *x elevado à quarta, menos dez x ao quadrado, mais nove, igual a "
        "zero?* [p=0.2] E quais são? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="13", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}x ao quadrado vira y: [p=0.2] *y ao quadrado, menos dez y, mais nove.* [p=0.4] "
        "{b}Soma dez, produto nove: [p=0.2] *um e nove.* [p=0.4] {c}Volte para x: [p=0.2] x ao quadrado igual a um, "
        "[p=0.2] *um ou menos um.* [p=0.2] x ao quadrado igual a nove, [p=0.2] *três ou menos três.* [p=0.4] {d}*Quatro "
        "raízes.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="14", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] na biquadrada, x ao quadrado vira y. [p=0.5] {b}Dois: [p=0.2] não "
        "pare no y: volte para x. [p=0.5] {c}Três: [p=0.2] y negativo não gera raiz real."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="15", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] resolver a do começo [p=0.2] e responder *quatro e "
        "nove.* [p=0.4] {b}Parece certo, [p=0.2] porque quatro e nove *resolvem* a equação em y. [p=0.4] {c}Mas a "
        "pergunta é o x: [p=0.2] volte, [p=0.2] e as respostas são *dois, menos dois, três e menos três.*"),
    dict(id="16", block="erros", text=
        "{a}Segundo: [p=0.2] ler *x ao quadrado igual a menos quatro* [p=0.2] como *mais ou menos dois.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque o quatro tem raiz, [p=0.2] e é *dois.* [p=0.4] {c}Mas dois ao quadrado é *quatro positivo,* "
        "[p=0.2] e menos dois também. [p=0.2] Ninguém ao quadrado dá *menos quatro:* [p=0.2] *sem raiz real.*"),
    dict(id="17", block="erros", text=
        "{a}Terceiro: [p=0.2] em *x ao quadrado sobre x, igual a cinco,* [p=0.2] multiplicar por x [p=0.2] e aceitar "
        "*zero e cinco.* [p=0.4] {b}Parece certo, [p=0.2] porque as contas estão certas. [p=0.4]"
        " {c}Mas o zero *zera o denominador.* [p=0.2] Ele era proibido desde o começo: [p=0.2] *só o cinco.*"),

    # ================= QUESTÃO 8 (VOCÊ FAZ) =================
    dict(id="18", block="q8", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] *Você faz.* [p=0.4] {a}Considere a "
        "equação *x elevado à quarta, menos cinco x ao quadrado, menos trinta e seis, igual a zero.* [p=0.2] O número de "
        "soluções reais dessa equação é: [p=0.4] {qa}A: [p=0.2] nenhuma. [p=0.3] {qb}B: [p=0.2] uma. [p=0.3] {qc}C: "
        "[p=0.2] duas. [p=0.3] {qd}D: [p=0.2] três. [p=0.3] {qe}E: [p=0.2] quatro. [p=0.4] {p}*Pause e resolva.* [p=2.0]"),
    dict(id="19", block="q8", text=
        "{t}Vamos conferir. [p=0.3] {a}x ao quadrado vira y: [p=0.2] *y ao quadrado, menos cinco y, menos trinta e seis.* "
        "[p=0.4] {b}Por Bhaskara: [p=0.2] delta é vinte e cinco, mais cento e quarenta e quatro: [p=0.2] *cento e "
        "sessenta e nove.* [p=0.2] A raiz é treze. [p=0.4] {c}y é *cinco mais ou menos treze, sobre dois:* [p=0.2] "
        "*nove* ou *menos quatro.* [p=0.4] {d}Volte para x. [p=0.2] x ao quadrado igual a nove: [p=0.2] *três e menos "
        "três.* [p=0.4] {e}x ao quadrado igual a menos quatro: [p=0.2] *bilhete sem valor.* [p=0.4] {ok}*Duas soluções.* "
        "[p=0.2] *Letra C!*"),
    dict(id="20", block="q8", text=
        "{t}Atalho para conferir. [p=0.3] {a}O produto dos dois y é o número sozinho: [p=0.2] *menos trinta e seis.* "
        "[p=0.4] {b}Produto negativo: [p=0.2] *um y positivo e um negativo.* [p=0.4] {c}O positivo dá duas raízes, "
        "[p=0.2] o negativo, nenhuma: [p=0.2] *exatamente duas.*"),
    dict(id="21", block="q8", text=
        "{t}E as erradas? [p=0.3] {xe}A E aceita x ao quadrado igual a menos quatro [p=0.2] como *mais ou menos dois.* "
        "[p=0.4] {xb}A B fica só com a raiz *positiva,* o três. [p=0.4] {xd}A D *mistura:* [p=0.2] fica com o três e o "
        "menos três [p=0.2] e ainda conta o y negativo como resposta. [p=0.4] {xa}E a A acha que o y negativo *invalida "
        "a equação inteira.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="22", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] na biquadrada, x ao quadrado vira y. [p=0.5] {b}Dois: "
        "[p=0.2] não pare no y: volte para x. [p=0.5] {c}Três: [p=0.2] y negativo não gera raiz real."),

    # ================= PONTE E CTA =================
    dict(id="23", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] {c}e "
        "vemos a equação do segundo grau na *Física* e na *Economia.*"),
    dict(id="24", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha parado no y alguma vez? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
