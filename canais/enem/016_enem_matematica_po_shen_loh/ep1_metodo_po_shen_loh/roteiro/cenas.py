# Roteiro — Equação do 2º grau, Episódio 1 de 1: o método de Po-Shen Loh (média ± u) (aula para iniciantes)
# Base: pedido do usuário (22/10/2026) — sem material HTML; conteúdo conferido em analise/conferir_contas.py.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: a GANGORRA EQUILIBRADA — as duas raízes são duas crianças sentadas à MESMA DISTÂNCIA (u) do meio da
#   gangorra (a média). Retomada: u = 0 → as duas sentam juntas no meio (raiz dupla); u² negativo → não há onde sentar
#   (sem raiz real); esquecer o ± → uma criança sozinha, a gangorra tomba.
# Ideia central: (x − r)(x − s) = x² − (r + s)x + rs → soma = −b, produto = c (com o x² sozinho, a = 1).
#   Média m = −b/2; raízes m − u e m + u; produto (m − u)(m + u) = m² − u² = c → u² = m² − c.
# Crédito (só estes fatos): Po-Shen Loh, professor da Carnegie Mellon, foi técnico da seleção dos EUA na Olimpíada
#   Internacional de Matemática, divulgou o método em 2019; ideia com raízes na Babilônia.
# Contas conferidas por script (analise/conferir_contas.py: método × Bhaskara × substituição na equação):
#   x² − 8x + 12 = 0 → m = 4, u² = 16 − 12 = 4, u = 2 → 2 e 6 (Bhaskara: Δ = 64 − 48 = 16, (8 ± 4)/2 = 6 e 2; 2² − 16 + 12 = 0).
#   x² − 5x + 6 = 0 → m = 2,5, m² = 6,25, u² = 0,25, u = 0,5 → 2 e 3 (soma 5, produto 6).
#   2x² + 4x − 6 = 0 → ÷2 → x² + 2x − 3 = 0 → m = −1, u² = 1 + 3 = 4, u = 2 → −3 e 1 (2·9 − 12 − 6 = 0; 2 + 4 − 6 = 0).
#   x² − 6x + 7 = 0 → m = 3, u² = 9 − 7 = 2, u = √2 → 3 − √2 ≈ 1,59 e 3 + √2 ≈ 4,41 (Bhaskara: (6 ± √8)/2).
#   x² − 10x + 25 = 0 → m = 5, u² = 0 → raiz dupla 5.   x² − 2x + 5 = 0 → m = 1, u² = 1 − 5 = −4 → sem raiz real (Δ = −16).
#   Bhaskara com a = 1: Δ = b² − 4c = 4(m² − c) = 4u² → √Δ/2 = u, −b/2 = m: é a mesma conta.
# Questão (inédita, estilo ENEM): terreno retangular, perímetro 40 m, área 96 m² → lados somam 20, produto 96 →
#   x² − 20x + 96 = 0 → m = 10, u² = 100 − 96 = 4, u = 2 → 8 e 12. Gabarito D.
#   Erradas: A 4 e 24 (área 96, perímetro 56) · B 6 e 14 (usou u = 4, esqueceu a raiz quadrada; área 84) ·
#   C 6 e 16 (área 96, perímetro 44) · E 10 e 10 (parou na média, esqueceu o u; área 100).
# Treino na tela (cena 30, conferido): x² − 6x + 8 = 0 → 2 e 4 · x² + 4x − 5 = 0 → −5 e 1 · 3x² − 12x + 9 = 0 → 1 e 3.
# Voz: gerada em 2 partes (corte na cena 16); conferida pela transcrição (analise/extenso.py): nada pulado, repetido ou
#   inventado — as diferenças são só a grafia do Whisper (x², 2x, "u" ouvido como "um", ordinais como "2.").
# Frases-chave (meio e fim, idênticas):
#   1. A média é menos b sobre dois.
#   2. O u ao quadrado é a média ao quadrado, menos c.
#   3. As raízes são a média menos u e a média mais u.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Equação do 2º grau sem Bhaskara: o método de Po-Shen Loh — Matemática ENEM"

# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar (igual à série 015)
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase "
            "forte às palavras-chave. Nas contas, fale devagar e com clareza, como quem raciocina junto com o aluno. "
            "Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, "
            "exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Dois números somam *oito* [p=0.2] e, multiplicados, dão *doze.* [p=0.4] Quais são? [p=0.8] {b}Dois e seis. "
        "[p=0.3] Fácil, né? [p=0.4] {c}Pois essa pergunta *é* uma equação do segundo grau. [p=0.4] {d}E hoje você vai "
        "resolver qualquer uma delas com essa mesma ideia, [p=0.2] *sem decorar a fórmula de Bhaskara.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai achar as raízes de uma equação do segundo grau [p=0.2] em *três passos* "
        "curtos, [p=0.4] {b}e vai entender *de onde* vem cada passo."),
    dict(id="03", block="prereq", text=
        "{t}Antes, duas lembranças rápidas. [p=0.3] {a}Equação do segundo grau é a que tem *x ao quadrado,* [p=0.2] e "
        "nenhuma potência maior. [p=0.3] {b}Por exemplo: [p=0.2] x ao quadrado, menos oito x, mais doze, igual a zero. "
        "[p=0.4] {c}*Raiz* é o número que, no lugar do x, [p=0.2] *zera* a conta. [p=0.4] {d}Teste o dois: [p=0.2] dois "
        "ao quadrado é quatro; [p=0.2] oito vezes dois, dezesseis. [p=0.3] {e}Quatro menos dezesseis mais doze: [p=0.2] "
        "*zero.* [p=0.3] {f}O dois é raiz!"),
    dict(id="04", block="prereq", text=
        "{t}Segunda lembrança. [p=0.3] {a}Esse tipo de equação aparece assim: [p=0.2] x ao quadrado, mais b x, mais c, "
        "igual a zero. [p=0.4] {b}O *b* é o número que acompanha o x, [p=0.2] *com o sinal.* [p=0.3] {c}O *c* é o número "
        "sozinho. [p=0.4] {d}No nosso exemplo, [p=0.2] b é menos oito [p=0.2] e c é doze. [p=0.4] {e}E cuidado: [p=0.2] "
        "*raiz quadrada* é outra coisa. [p=0.2] É o número que, ao quadrado, dá o valor. [p=0.3] {f}Raiz quadrada de "
        "quatro é dois, [p=0.2] porque dois ao quadrado é quatro."),

    # ================= BLOCO A: DE ONDE VÊM A SOMA E O PRODUTO =================
    dict(id="05", block="fatores", text=
        "{t}Agora, uma pergunta curiosa: [p=0.2] por que dois números que somam oito e multiplicam doze [p=0.2] resolvem "
        "essa equação? [p=0.4] {a}Olhe para esta conta: [p=0.2] x menos dois, [p=0.2] vezes x menos seis, [p=0.2] igual a "
        "zero. [p=0.4] {b}Se x for dois, [p=0.2] o primeiro parêntese vira zero. [p=0.3] {c}Se x for seis, [p=0.2] o "
        "segundo vira zero. [p=0.4] {d}E zero vezes qualquer coisa [p=0.2] é *zero.* [p=0.3] {e}Então dois e seis são as "
        "raízes."),
    dict(id="06", block="fatores", text=
        "{t}Agora, multiplique tudo. [p=0.3] {a}x vezes x: [p=0.2] x ao quadrado. [p=0.3] {b}Os dois do meio: [p=0.2] "
        "menos seis x [p=0.2] e menos dois x, [p=0.2] que juntos dão menos oito x. [p=0.4] {c}E menos dois vezes menos "
        "seis: [p=0.2] mais doze. [p=0.4] {d}Voltou a nossa equação! [p=0.4] {e}Repare: [p=0.2] o oito é a *soma* das "
        "raízes, [p=0.2] {f}e o doze é o *produto.*"),
    dict(id="07", block="fatores", text=
        "{t}E isso vale sempre. [p=0.3] {a}Na equação x ao quadrado, mais b x, mais c, [p=0.4] {b}a soma das raízes é "
        "*menos b,* [p=0.2] o b com o sinal trocado. [p=0.4] {c}E o produto das raízes é o *c.* [p=0.4] {d}No exemplo: "
        "[p=0.2] b é menos oito, [p=0.2] então a soma é oito. [p=0.2] E o produto é doze."),

    # ================= BLOCO B: A GANGORRA =================
    dict(id="08", block="gangorra", text=
        "{t}Agora, a ideia genial. [p=0.3] {a}Pense numa *gangorra.* [p=0.3] Para ela ficar equilibrada, [p=0.2] as duas "
        "crianças sentam à *mesma distância* do meio. [p=0.4] {b}Com as raízes é igual. [p=0.3] Dois números que somam "
        "oito: [p=0.2] {c}três e cinco, [p=0.2] {d}dois e seis, [p=0.2] {e}um e sete. [p=0.4] {f}Todos ficam equilibrados "
        "em volta do *quatro,* [p=0.2] o meio da gangorra."),
    dict(id="09", block="gangorra", text=
        "{t}Esse meio tem nome: [p=0.2] é a *média.* [p=0.3] {a}A média é a soma dividida por dois. [p=0.2] Oito "
        "dividido por dois: [p=0.2] quatro. [p=0.4] {b}Como a soma é menos b, [p=0.2] a média é *menos b sobre dois.* "
        "[p=0.4] {c}E a distância de cada raiz até o meio, [p=0.2] a gente chama de *u.* [p=0.4] {d}Então as raízes são "
        "[p=0.2] *a média menos u* [p=0.2] {e}e *a média mais u.*"),
    dict(id="10", block="gangorra", text=
        "{t}Falta descobrir o u. [p=0.3] E quem conta é o *produto.* [p=0.4] {a}As raízes são quatro menos u [p=0.2] e "
        "quatro mais u. [p=0.2] Multiplicadas, dão doze. [p=0.4] {b}Fazendo a multiplicação, [p=0.2] os termos do meio, "
        "[p=0.2] mais quatro u e menos quatro u, [p=0.2] se cancelam. [p=0.3] {c}Sobra dezesseis, menos o u ao quadrado, "
        "[p=0.2] igual a doze. [p=0.4] {d}Então o u ao quadrado é *quatro,* [p=0.2] {e}e o u é *dois.* [p=0.4] {f}Raízes: "
        "[p=0.2] quatro menos dois, [p=0.2] *dois;* [p=0.2] {g}quatro mais dois, [p=0.2] *seis.*"),

    # ================= CRÉDITO =================
    dict(id="11", block="credito", text=
        "{t}Esse caminho ficou famoso com *Po-Shen Loh,* [p=0.2] professor de matemática da universidade Carnegie Mellon, "
        "[p=0.2] nos Estados Unidos. [p=0.4] {a}Ele foi técnico da seleção americana na Olimpíada Internacional de "
        "Matemática, [p=0.3] {b}e divulgou o método em dois mil e dezenove. [p=0.4] {c}Mas a ideia tem raízes antigas: "
        "[p=0.2] os *babilônios* já usavam algo parecido, [p=0.2] há milhares de anos."),

    # ================= A RECEITA =================
    dict(id="12", block="receita", text=
        "{t}Então, a receita em três passos. [p=0.4] {z}Antes de tudo: [p=0.2] o x ao quadrado precisa estar sozinho, "
        "[p=0.2] sem número na frente. [p=0.4] {a}Passo um: [p=0.2] a média. [p=0.2] *Menos b sobre dois.* [p=0.4] "
        "{b}Passo dois: [p=0.2] o *u ao quadrado é a média ao quadrado, menos c.* [p=0.2] Depois, tire a raiz quadrada. "
        "[p=0.4] {c}Passo três: [p=0.2] as raízes são *a média menos u* [p=0.2] e *a média mais u.*"),

    # ================= EXEMPLO: B ÍMPAR =================
    dict(id="13", block="ex_impar", text=
        "{t}Vamos testar com uma média quebrada. [p=0.3] {a}x ao quadrado, menos cinco x, mais seis, igual a zero. "
        "[p=0.4] {b}Aqui, b é menos cinco [p=0.2] e c é seis. [p=0.4] {c}Passo um: [p=0.2] menos b sobre dois [p=0.2] é "
        "cinco sobre dois, [p=0.2] *dois vírgula cinco.* [p=0.4] {d}Passo dois: [p=0.2] dois vírgula cinco ao quadrado "
        "[p=0.2] é seis vírgula vinte e cinco. [p=0.3] {e}Menos seis: [p=0.2] zero vírgula vinte e cinco. [p=0.3] {f}A "
        "raiz quadrada disso é zero vírgula cinco, [p=0.2] porque meio vezes meio é um quarto. [p=0.4] {g}Passo três: "
        "[p=0.2] dois vírgula cinco menos zero vírgula cinco, [p=0.2] *dois.* [p=0.2] {h}Mais zero vírgula cinco, "
        "[p=0.2] *três.*"),

    # ================= EXEMPLO: A DIFERENTE DE 1 =================
    dict(id="14", block="ex_a", text=
        "{t}E se tiver número na frente do x ao quadrado? [p=0.4] {a}Dois x ao quadrado, mais quatro x, menos seis, "
        "igual a zero. [p=0.4] {b}Passo zero: [p=0.2] *divida tudo por dois.* [p=0.3] {c}Fica x ao quadrado, mais dois x, "
        "menos três, igual a zero. [p=0.4] {d}Agora, b é *mais dois.* [p=0.2] Menos b sobre dois: [p=0.2] *menos um.* "
        "[p=0.3] Atenção ao sinal! [p=0.4] {e}O u ao quadrado: [p=0.2] menos um ao quadrado é um. [p=0.2] Um, menos o "
        "menos três, [p=0.2] é um mais três: [p=0.2] quatro. [p=0.2] O u é dois. [p=0.4] {f}Raízes: [p=0.2] menos um "
        "menos dois, [p=0.2] *menos três;* [p=0.2] {g}menos um mais dois, [p=0.2] *um.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="15", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a média é menos b sobre dois. [p=0.5] {b}Dois: [p=0.2] "
        "o u ao quadrado é a média ao quadrado, menos c. [p=0.5] {c}Três: [p=0.2] as raízes são a média menos u e a média "
        "mais u."),

    # ================= CASOS ESPECIAIS =================
    dict(id="16", block="ex_irracional", text=
        "{t}E quando o u ao quadrado não é um quadrado perfeito? [p=0.4] {a}x ao quadrado, menos seis x, mais sete, igual "
        "a zero. [p=0.4] {b}Média: [p=0.2] menos b sobre dois, [p=0.2] *três.* [p=0.3] {c}O u ao quadrado: [p=0.2] três "
        "ao quadrado é nove; [p=0.2] nove menos sete, [p=0.2] *dois.* [p=0.4] {d}Nenhum número inteiro ao quadrado dá "
        "dois. [p=0.2] Sem problema: [p=0.2] o u é a *raiz quadrada de dois.* [p=0.4] {e}Raízes: [p=0.2] três menos raiz "
        "de dois [p=0.2] e três mais raiz de dois."),
    dict(id="17", block="ex_dupla", text=
        "{t}E se o u der *zero?* [p=0.4] {a}x ao quadrado, menos dez x, mais vinte e cinco, igual a zero. [p=0.4] "
        "{b}Média: [p=0.2] *cinco.* [p=0.3] {c}O u ao quadrado: [p=0.2] vinte e cinco menos vinte e cinco, [p=0.2] "
        "*zero.* [p=0.4] {d}Na gangorra, [p=0.2] as duas crianças sentam *bem no meio,* [p=0.2] juntas. [p=0.4] {e}As "
        "duas raízes são iguais a cinco. [p=0.2] É a *raiz dupla.*"),
    dict(id="18", block="ex_negativo", text=
        "{t}E se o u ao quadrado der *negativo?* [p=0.4] {a}x ao quadrado, menos dois x, mais cinco, igual a zero. "
        "[p=0.4] {b}Média: [p=0.2] *um.* [p=0.3] {c}O u ao quadrado: [p=0.2] um menos cinco, [p=0.2] *menos quatro.* "
        "[p=0.4] {d}Mas qualquer número ao quadrado dá zero ou positivo. [p=0.2] Dois ao quadrado é quatro; [p=0.2] menos "
        "dois ao quadrado *também* é quatro. [p=0.4] {e}Então não existe esse u. [p=0.2] Na gangorra, [p=0.2] não tem "
        "onde as crianças sentarem. [p=0.4] {f}A resposta é: [p=0.2] a equação *não tem raiz real.* [p=0.2] Não é erro "
        "de conta."),

    # ================= BHASKARA E ATALHO DE PROVA =================
    dict(id="19", block="bhaskara", text=
        "{t}E a fórmula de Bhaskara? [p=0.3] Ela dá a *mesma* resposta. [p=0.4] {a}Na primeira equação, [p=0.2] o delta "
        "é b ao quadrado menos quatro vezes c: [p=0.2] sessenta e quatro menos quarenta e oito, [p=0.2] *dezesseis.* "
        "[p=0.4] {b}x é oito, mais ou menos quatro, [p=0.2] tudo sobre dois: [p=0.2] seis ou dois. [p=0.4] {c}Agora "
        "repare: [p=0.2] oito sobre dois é quatro, [p=0.2] a *média.* [p=0.2] {d}Quatro sobre dois é dois, [p=0.2] o *u.* "
        "[p=0.4] {e}Bhaskara é a média mais ou menos u, [p=0.2] *disfarçada.* [p=0.3] É a mesma conta, [p=0.2] só que "
        "sem precisar decorar."),
    dict(id="20", block="atalho", text=
        "{t}Na prova, o atalho fica assim. [p=0.4] {a}Um: [p=0.2] tem número na frente do x ao quadrado? [p=0.2] Divida "
        "tudo por ele primeiro. [p=0.4] {b}Dois: [p=0.2] a média é a metade do b, [p=0.2] *com o sinal trocado.* [p=0.4] "
        "{c}Três: [p=0.2] no fim, confira: [p=0.2] as raízes somam menos b [p=0.2] e multiplicam c."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] esquecer de dividir pelo número da frente. [p=0.3] Em "
        "dois x ao quadrado, mais quatro x, menos seis, [p=0.2] a pessoa usa b igual a quatro [p=0.2] e acha média menos "
        "dois. [p=0.4] {b}Parece certo, [p=0.2] porque o quatro está ali, à vista. [p=0.4] {c}Mas a soma é menos b só "
        "quando o x ao quadrado está sozinho. [p=0.2] *Divida primeiro.*"),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] errar o sinal da média. [p=0.3] Em x ao quadrado, menos oito x, mais doze, [p=0.2] a pessoa "
        "escreve média menos quatro. [p=0.4] {b}Parece certo, [p=0.2] porque tem um menos na frente do oito. [p=0.4] {c}Mas "
        "a média é *menos b* sobre dois: [p=0.2] o menos da regra troca o sinal do b. [p=0.2] Menos com menos: [p=0.2] "
        "*mais quatro.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] esquecer o mais ou menos [p=0.2] e responder uma raiz só. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque a primeira conta já deu um número que funciona. [p=0.4] {c}Mas a gangorra tem *duas* crianças: [p=0.2] "
        "média menos u *e* média mais u. [p=0.2] Com uma só, [p=0.2] a gangorra tomba."),
    dict(id="24", block="erros", text=
        "{a}Quarto: [p=0.2] achar que u ao quadrado negativo é erro de conta [p=0.2] e ficar refazendo. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque a gente se acostuma a sempre achar uma resposta. [p=0.4] {c}Mas u ao quadrado negativo *é* "
        "a resposta: [p=0.2] a equação não tem raiz real. [p=0.2] Confira uma vez e siga em frente."),

    # ================= QUESTÃO ESTILO ENEM =================
    dict(id="25", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {a}Um terreno retangular tem perímetro de quarenta metros "
        "[p=0.2] e área de noventa e seis metros quadrados. [p=0.4] {b}Quais são as medidas dos lados do terreno, em "
        "metros? [p=0.4] {c}A: [p=0.2] quatro e vinte e quatro. [p=0.3] {d}B: [p=0.2] seis e catorze. [p=0.3] {e}C: "
        "[p=0.2] seis e dezesseis. [p=0.3] {f}D: [p=0.2] oito e doze. [p=0.3] {g}E: [p=0.2] dez e dez. [p=0.4] "
        "{p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="26", block="questao", text=
        "{t}Vamos lá. [p=0.3] {a}Perímetro é a volta inteira no terreno: [p=0.2] os quatro lados somados. [p=0.3] Se a "
        "volta é quarenta, [p=0.2] um comprimento mais uma largura dá *vinte.* [p=0.4] {b}Área do retângulo: [p=0.2] "
        "comprimento vezes largura, [p=0.2] *noventa e seis.* [p=0.4] {c}Dois números que somam vinte [p=0.2] e "
        "multiplicam noventa e seis. [p=0.3] É a equação x ao quadrado, menos vinte x, mais noventa e seis, igual a zero. "
        "[p=0.4] {d}E o atalho: [p=0.2] a soma e o produto já estão no enunciado. [p=0.2] Dá para ir direto ao método!"),
    dict(id="27", block="questao", text=
        "{a}Média: [p=0.2] vinte dividido por dois, [p=0.2] *dez.* [p=0.3] {b}O u ao quadrado: [p=0.2] dez ao quadrado é "
        "cem; [p=0.2] cem menos noventa e seis, [p=0.2] *quatro.* [p=0.3] {c}O u é *dois.* [p=0.4] {d}Lados: [p=0.2] dez "
        "menos dois, [p=0.2] *oito;* [p=0.2] dez mais dois, [p=0.2] *doze.* [p=0.4] {e}Conferindo: [p=0.2] oito mais doze "
        "é vinte, [p=0.2] oito vezes doze, noventa e seis. [p=0.3] {ok}*Letra D!*"),
    dict(id="28", block="questao", text=
        "{t}E as outras? [p=0.3] {xe}Dez e dez [p=0.2] é de quem parou na média [p=0.2] e esqueceu o u: [p=0.2] a área "
        "daria cem. [p=0.4] {xb}Seis e catorze [p=0.2] é de quem usou u igual a quatro, [p=0.2] esquecendo a raiz "
        "quadrada: [p=0.2] área oitenta e quatro. [p=0.4] {xa}E quatro e vinte e quatro, [p=0.2] {xc}seis e dezesseis, "
        "[p=0.2] têm a área certa, [p=0.2] mas a volta passa de quarenta. [p=0.2] Olharam só o produto."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a média é menos b sobre dois. [p=0.5] {b}Dois: "
        "[p=0.2] o u ao quadrado é a média ao quadrado, menos c. [p=0.5] {c}Três: [p=0.2] as raízes são a média menos u e "
        "a média mais u."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}Agora é com você: [p=0.2] pegue três equações do seu caderno [p=0.2] e resolva pela média e pelo u. [p=0.4] "
        "{b}Depois, confira com Bhaskara: [p=0.2] {c}vai dar a *mesma resposta.*"),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já conhecia esse jeito de resolver sem Bhaskara? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
