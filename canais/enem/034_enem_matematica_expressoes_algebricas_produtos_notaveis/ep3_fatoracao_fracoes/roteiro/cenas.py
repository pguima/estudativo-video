# Roteiro — Expressões Algébricas e Produtos Notáveis, Episódio 3 de 5: fatoração, frações algébricas e o produto notável
#   usado ao contrário
# Base: Estudos/Enem/estudos/01-matematica/19-expressoes-algebricas-produtos-notaveis.html — seções 06 e 07 + Questões 4 e 5
#   (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   FATORAR É O CAMINHO DE VOLTA: o produto notável monta, a fatoração desmonta.
#   CORTA-SE FATOR, NUNCA TERMO: fator multiplica tudo em cima e tudo embaixo; termo é só uma parcela (um pedaço do bolo).
#   O L QUE VIRA RETÂNGULO: tire b × b de a × a, recorte o L e remonte: (a + b) por (a − b).
#   O QUE ERA PROIBIDO CONTINUA PROIBIDO: o valor que zerava o denominador antes de cortar continua fora da resposta.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos: os blocos a–g usam os exemplos do material/prompt. Bloco h com números NOSSOS (para não entregar a Q5, que é
#   "você faz"): a + b = 5 e ab = 6 → a² + b² = 25 − 12 = 13; conferência com 2 e 3 (4 + 9 = 13).
#   Erro 3 usa a fração do bloco g: com x = −3, a original dá 0/0 e a simplificada daria 2.
# Nós fazemos (prompt): (x² − 25)/(x² − 10x + 25) = (x + 5)(x − 5)/(x − 5)² = (x + 5)/(x − 5), x ≠ 5; x = 0: −1 e −1.
# QUESTÃO 4 (eu faço, texto idêntico): (x + 4)(x − 4)/(x + 4)² = (x − 4)/(x + 4) → B. Erradas do material e do prompt:
#   A = "cortou" x² com x² (sobra −16/(8x + 16) = −2/(x + 2)); C inverte; D esquece que o denominador é um quadrado;
#   E fatora x² − 16 como (x − 4)². Conferência x = 0: −16/16 = −1 e −4/4 = −1.
# QUESTÃO 5 (você faz, texto idêntico): a + b = 9, ab = 14 → a² + b² = 81 − 28 = 53 → A. Erradas do material:
#   C (81) = (a + b)² direto; B (67) = subtraiu só ab; D (95) e E (109) somaram (81 + 14 e 81 + 28). Lados 2 e 7: 4 + 49 = 53.
# Acréscimo NOSSO (marcado): conferência "desenvolva de volta" depois de cada fatoração e o atalho de reconhecimento
#   (raiz das pontas, confira o meio); a ordem de ataque (fator comum primeiro → produto notável → soma e produto).
# Frases-chave (meio e fim, idênticas): 1. Fatorar é o caminho de volta do produto notável. 2. Comece sempre pelo fator
#   comum. 3. Corta-se fator, nunca termo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Fatoração do zero: os 5 casos e a fração que você não pode cortar · Matemática ENEM, Álgebra episódio 3"

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
        "{a}Na fração *x mais três, sobre três,* [p=0.2] muita gente corta o três [p=0.2] e fica com *x.* [p=0.4] "
        "{b}Com x igual a seis: [p=0.2] seis mais três, nove, [p=0.2] dividido por três, [p=0.2] dá *três,* [p=0.2] "
        "e não seis. [p=0.4] {c}O corte parecia inocente [p=0.2] e *errou o dobro.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *fatorar* pelos cinco casos, [p=0.3] {b}simplificar frações "
        "algébricas sem cortar o que não pode [p=0.3] {c}e tirar *a ao quadrado mais b ao quadrado* [p=0.2] de *a mais b* "
        "e de *a vezes b.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio dois, os três produtos notáveis: [p=0.2] quadrado da "
        "soma, [p=0.2] quadrado da diferença [p=0.2] e soma vezes diferença. [p=0.4] {b}E da série de Frações: [p=0.2] "
        "doze dezoito avos vira dois terços [p=0.2] porque o *seis* multiplica em cima e embaixo. [p=0.2] Só se corta o "
        "que *multiplica.*"),

    # ================= CONCRETO E DEFINIÇÃO =================
    dict(id="04", block="concreto", text=
        "{t}Comece com um número. [p=0.3] {a}Doze é igual a três vezes quatro: [p=0.2] *o doze fatorado.* [p=0.4] "
        "{b}*Fatorar* é escrever uma coisa como *multiplicação,* [p=0.2] e cada pedaço que multiplica [p=0.2] é um "
        "*fator.* [p=0.4] {c}No episódio dois, o produto notável *montava* a conta. [p=0.4] {d}Fatorar é o *caminho de "
        "volta:* [p=0.2] o produto notável monta, [p=0.2] a fatoração *desmonta.*"),

    # ================= BLOCO A: FATOR COMUM =================
    dict(id="05", block="comum", text=
        "{t}E qual é o primeiro passo, sempre? [p=0.4] {a}Procurar o *fator comum:* [p=0.2] o que se repete em *todos* os "
        "termos. [p=0.4] {b}Em seis x ao quadrado mais nove x, [p=0.2] seis e nove têm o *três* em comum, [p=0.2] e os "
        "dois têm um *x.* [p=0.4] {c}O três x sai para fora, [p=0.2] e no parêntese fica o que sobrou: [p=0.2] *dois x "
        "mais três.* [p=0.4] {d}Resultado: [p=0.2] *três x vezes dois x mais três.*"),
    dict(id="06", block="comum", text=
        "{t}E como saber se acertou? [p=0.3] {a}Faça o caminho de ida: [p=0.2] três x vezes dois x, seis x ao quadrado; "
        "[p=0.2] três x vezes três, nove x. [p=0.3] Voltou. [p=0.4] {b}*Atalho:* [p=0.2] toda fatoração se confere "
        "*desenvolvendo de volta.* [p=0.2] Dez segundos que salvam a questão."),

    # ================= BLOCO B: AGRUPAMENTO =================
    dict(id="07", block="agrupa", text=
        "{t}E se nada se repetir nos quatro termos? [p=0.4] {a}Em *a x mais três a mais dois x mais seis,* [p=0.2] agrupe "
        "de dois em dois. [p=0.4] {b}Dos dois primeiros sai o *a:* [p=0.2] a vezes x mais três. [p=0.2] Dos dois últimos "
        "sai o *dois:* [p=0.2] dois vezes x mais três. [p=0.4] {c}Apareceu o *mesmo parêntese* nos dois grupos: [p=0.2] "
        "agora *ele* é o fator comum. [p=0.4] {d}Resultado: [p=0.2] *a mais dois, vezes x mais três.* [p=0.2] É o "
        "*agrupamento.*"),

    # ================= BLOCO C: DIFERENÇA DE QUADRADOS =================
    dict(id="08", block="difquad", text=
        "{t}E dois termos com um sinal de menos? [p=0.4] {a}Em *x ao quadrado menos vinte e cinco,* [p=0.2] os dois são "
        "quadrados: [p=0.2] de x e de cinco. [p=0.4] {b}É uma *diferença de quadrados:* [p=0.2] um quadrado *menos* "
        "outro. [p=0.4] {c}Ela vira a soma vezes a diferença: [p=0.2] *x mais cinco, vezes x menos cinco.* [p=0.4] "
        "{d}Conferindo: [p=0.2] o menos cinco x e o mais cinco x se anulam. [p=0.2] Voltou."),
    dict(id="09", block="lshape", text=
        "{t}Mas por que isso vale? [p=0.4] {a}Pegue um quadrado de lado *a* [p=0.2] e tire do canto um quadrado de lado "
        "*b.* [p=0.4] {b}Sobra um *L,* [p=0.2] de área *a ao quadrado menos b ao quadrado.* [p=0.4] {c}Recorte o L em "
        "dois retângulos [p=0.2] e remonte. [p=0.4] {d}Vira um retângulo de lados *a mais b* [p=0.2] e *a menos b.* "
        "[p=0.4] {e}Mesma área, [p=0.2] agora como *multiplicação.*"),

    # ================= BLOCO D: TRINÔMIO QUADRADO PERFEITO =================
    dict(id="10", block="tqp", text=
        "{t}E com três termos? [p=0.4] {a}Um *trinômio quadrado perfeito* [p=0.2] é uma expressão de três termos [p=0.2] "
        "que nasceu de um quadrado. [p=0.4] {b}Teste *x ao quadrado menos seis x mais nove.* [p=0.2] Raiz das *pontas:* "
        "[p=0.2] *x* e *três.* [p=0.4] {c}Confira o do meio: [p=0.2] *duas vezes* x vezes três, [p=0.2] *seis x.* [p=0.2] "
        "Confere! [p=0.4] {d}Com o sinal de menos: [p=0.2] *x menos três, ao quadrado.*"),
    dict(id="11", block="tqp", text=
        "{t}Esse é o *atalho* de reconhecimento: [p=0.3] {a}*raiz das pontas,* [p=0.2] e o dobro do produto delas tem que "
        "ser o termo do meio. [p=0.4] {b}Mais um: [p=0.2] *quatro x ao quadrado mais doze x mais nove.* [p=0.2] Pontas: "
        "[p=0.2] *dois x* e *três.* [p=0.2] Dobro do produto: [p=0.2] *doze x.* [p=0.2] Confere. [p=0.4] {c}É *dois x "
        "mais três, ao quadrado.*"),

    # ================= BLOCO E: SOMA E PRODUTO =================
    dict(id="12", block="somaprod", text=
        "{t}E se o termo do meio não conferir? [p=0.4] {a}Em *x ao quadrado mais cinco x mais seis,* [p=0.2] procure "
        "*dois números* [p=0.2] de *soma* cinco [p=0.2] e *produto* seis. [p=0.4] {b}Dois e três. [p=0.4] {c}Fica *x mais "
        "dois, vezes x mais três:* [p=0.2] o *trinômio soma e produto.* [p=0.4] {d}Aqui ele é só *fatoração.* [p=0.2] "
        "Resolver *equação* com ele [p=0.2] é assunto da série de Equação do segundo grau."),

    # ================= BLOCO F: COMBINADO =================
    dict(id="13", block="combo", text=
        "{t}E quando um caso só não basta? [p=0.4] {a}Em *x ao cubo menos quatro x,* [p=0.2] o fator comum primeiro: "
        "[p=0.2] sai um *x,* [p=0.2] e fica x ao quadrado menos quatro. [p=0.4] {b}E o que sobrou [p=0.2] é diferença de "
        "quadrados! [p=0.4] {c}Resultado: [p=0.2] *x vezes x mais dois, vezes x menos dois.* [p=0.4] {d}Essa é a *ordem "
        "de ataque:* [p=0.2] fator comum primeiro; [p=0.2] depois, produto notável ou soma e produto."),

    # ================= BLOCO G: FRAÇÕES ALGÉBRICAS =================
    dict(id="14", block="tesoura", text=
        "{t}E nas frações com letras, o que se pode cortar? [p=0.4] {a}Uma *fração algébrica* [p=0.2] é uma fração com "
        "letras. [p=0.4] {b}A regra é a das frações de número: [p=0.2] *corta-se fator, nunca termo.* [p=0.4] {c}*Termo* "
        "é só uma parcela, separada por mais ou menos. [p=0.2] Cortar termo [p=0.2] é cortar só *um pedaço do bolo.* "
        "[p=0.4] {d}*Fator* multiplica *tudo* em cima [p=0.2] e *tudo* embaixo. [p=0.2] Esse se corta."),
    dict(id="15", block="fracao", text=
        "{t}Então como se simplifica? [p=0.3] Fatorando primeiro. [p=0.4] {a}Pegue *x ao quadrado menos nove, sobre x ao "
        "quadrado mais três x.* [p=0.4] {b}Antes de tudo, a *condição de existência:* [p=0.2] os valores que zeram o "
        "denominador são proibidos. [p=0.2] Embaixo está *x vezes x mais três:* [p=0.2] proibidos o *zero* e o *menos "
        "três.* [p=0.4] {c}Em cima, [p=0.2] x mais três vezes x menos três. [p=0.4] {d}O *x mais três* multiplica tudo em "
        "cima e tudo embaixo: [p=0.2] é fator, *corta.* [p=0.4] {e}Sobra *x menos três, sobre x,* [p=0.2] com x diferente "
        "de zero e de menos três."),
    dict(id="16", block="fracao", text=
        "{t}Mas por que o menos três continua proibido, [p=0.2] se ele sumiu da fração? [p=0.4] {a}Porque a conta "
        "*original,* com menos três, [p=0.2] dá *zero sobre zero:* [p=0.2] não existe. [p=0.4] {b}Simplificar não pode "
        "*criar* um valor. [p=0.4] {c}*O que era proibido continua proibido.*"),

    # ================= BLOCO H: O PRODUTO NOTÁVEL AO CONTRÁRIO =================
    dict(id="17", block="contrario", text=
        "{t}E se a questão der a soma e o produto, [p=0.2] e pedir a soma dos *quadrados?* [p=0.4] {a}O quadrado da soma "
        "é a ao quadrado, mais dois a b, mais b ao quadrado. [p=0.4] {b}Passe o dois a b para o outro lado: [p=0.2] *a ao "
        "quadrado mais b ao quadrado [p=0.2] é a mais b, ao quadrado, menos dois a b.* [p=0.4] {c}Exemplo: [p=0.2] soma "
        "cinco, produto seis. [p=0.2] Vinte e cinco menos doze: [p=0.2] *treze.* [p=0.4] {d}Com os números dois e três: "
        "[p=0.2] quatro mais nove, treze. [p=0.2] Sem descobrir os números!"),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Agora você. [p=0.3] {a}Simplifique: [p=0.2] *x ao quadrado menos vinte e cinco, [p=0.2] sobre x ao quadrado "
        "menos dez x mais vinte e cinco.* [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Em cima, diferença de quadrados: [p=0.2] x mais cinco, vezes x menos cinco. [p=0.4] "
        "{b}Embaixo, pontas x e cinco, [p=0.2] meio dez x: [p=0.2] *x menos cinco, ao quadrado.* [p=0.2] Proibido: "
        "[p=0.2] x igual a cinco. [p=0.4] {c}Corte um x menos cinco: [p=0.2] sobra *x mais cinco, sobre x menos cinco.* "
        "[p=0.4] {d}Com x igual a zero: [p=0.2] a original dá menos vinte e cinco sobre vinte e cinco, *menos um;* "
        "[p=0.2] a simplificada, cinco sobre menos cinco, *menos um.* [p=0.2] Bateu!"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Hora de guardar três frases. [p=0.5] {a}Um: [p=0.2] fatorar é o caminho de volta do produto notável. "
        "[p=0.5] {b}Dois: [p=0.2] comece sempre pelo fator comum. [p=0.5] {c}Três: [p=0.2] corta-se fator, nunca "
        "termo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{a}Erro um: [p=0.2] cortar o três em *x mais três, sobre três.* [p=0.4] {b}Parece certo porque o três está em "
        "cima e embaixo, [p=0.2] como nas frações de número. [p=0.4] {c}Mas em cima o três é *termo.* [p=0.2] Fatore "
        "antes: [p=0.2] se não virou multiplicação, [p=0.2] *não corta.*"),
    dict(id="22", block="erros", text=
        "{a}Erro dois: [p=0.2] dizer que *x ao quadrado menos dezesseis* [p=0.2] é *x menos quatro, ao quadrado.* [p=0.4] "
        "{b}Parece certo: [p=0.2] tem quadrado, tem quatro, tem menos. [p=0.4] {c}Mas esse quadrado teria um termo do "
        "meio, [p=0.2] menos oito x. [p=0.2] O certo é *x mais quatro, vezes x menos quatro.*"),
    dict(id="23", block="erros", text=
        "{a}Erro três: [p=0.2] simplificar e *esquecer* a condição de existência. [p=0.4] {b}Parece certo porque x menos "
        "três sobre x [p=0.2] aceita o menos três sem reclamar. [p=0.4] {c}Mas a original, com menos três, dá zero sobre "
        "zero. [p=0.2] Escreva os proibidos *antes* de cortar."),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="24", block="q4", text=
        "{t}Questão de prova, [p=0.2] e esta eu faço com você. [p=0.3] {a}Para x diferente de menos quatro, [p=0.2] a "
        "expressão *x ao quadrado menos dezesseis, [p=0.2] sobre x ao quadrado mais oito x mais dezesseis,* [p=0.2] é "
        "igual a: [p=0.4] {qa}A: [p=0.2] menos dois, sobre x mais dois. [p=0.3] {qb}B: [p=0.2] x menos quatro, sobre x "
        "mais quatro. [p=0.3] {qc}C: [p=0.2] x mais quatro, sobre x menos quatro. [p=0.3] {qd}D: [p=0.2] x menos "
        "quatro. [p=0.3] {qe}E: [p=0.2] x menos quatro ao quadrado, sobre x mais quatro ao quadrado."),
    dict(id="25", block="q4", text=
        "{t}Primeiro, fatorar em cima e embaixo. [p=0.4] {a}Em cima, [p=0.2] diferença de quadrados: [p=0.2] x mais "
        "quatro, vezes x menos quatro. [p=0.4] {b}Embaixo, [p=0.2] raiz das pontas: [p=0.2] x e quatro; [p=0.2] dobro "
        "do produto, *oito x.* [p=0.2] Confere: [p=0.2] *x mais quatro, ao quadrado.* [p=0.4] {c}Corte um x mais quatro "
        "de cada lado. [p=0.2] Sobra *x menos quatro, sobre x mais quatro.* [p=0.4] {d}Confira com x igual a zero: "
        "[p=0.2] a original dá menos dezesseis sobre dezesseis, [p=0.2] menos um. [p=0.2] A resposta, menos quatro "
        "sobre quatro, [p=0.2] menos um. [p=0.3] {ok}*Letra B!*"),
    dict(id="26", block="q4", text=
        "{t}E as erradas? [p=0.3] {xa}A A *cortou* o x ao quadrado de cima com o de baixo: [p=0.2] cortou termos, [p=0.2] "
        "e sobrou menos dezesseis sobre oito x mais dezesseis. [p=0.4] {xc}A C *inverteu.* [p=0.3] {xd}A D esqueceu que "
        "embaixo há um *quadrado.* [p=0.3] {xe}E a E é o erro dois: [p=0.2] x menos quatro, ao quadrado, em cima."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="27", block="q5", text=
        "{t}E esta é *sua.* [p=0.3] Um dado: [p=0.2] num retângulo, o quadrado da diagonal é a soma dos quadrados dos "
        "lados, [p=0.2] o teorema de Pitágoras, que tem série própria. [p=0.4] {a}Um retângulo tem perímetro de *dezoito "
        "centímetros* [p=0.2] e área de *catorze centímetros quadrados.* [p=0.2] O quadrado da medida da diagonal desse "
        "retângulo, [p=0.2] em centímetros quadrados, é: [p=0.4] {qa}A: [p=0.2] cinquenta e três. [p=0.3] {qb}B: [p=0.2] "
        "sessenta e sete. [p=0.3] {qc}C: [p=0.2] oitenta e um. [p=0.3] {qd}D: [p=0.2] noventa e cinco. [p=0.3] {qe}E: "
        "[p=0.2] cento e nove. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="28", block="q5", text=
        "{t}Conferindo. [p=0.3] {a}Lados *a* e *b:* [p=0.2] o perímetro dá a mais b igual a *nove;* [p=0.2] a área, a "
        "vezes b igual a *catorze.* [p=0.4] {b}Pede-se a ao quadrado mais b ao quadrado: [p=0.2] nove ao quadrado, "
        "oitenta e um, [p=0.2] menos vinte e oito: [p=0.2] *cinquenta e três.* [p=0.4] {c}Os lados são dois e sete: "
        "[p=0.2] quatro mais quarenta e nove, cinquenta e três. [p=0.3] {ok}*Letra A!* [p=0.4] {xc}A C é o oitenta e um "
        "direto, [p=0.2] o sonho do calouro de trás para frente. [p=0.3] {xb}A B tirou só um catorze. [p=0.3] {xd}A D "
        "[p=0.2] {xe}e a E *somaram* em vez de subtrair."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] fatorar é o caminho de volta do produto "
        "notável. [p=0.5] {b}Dois: [p=0.2] comece sempre pelo fator comum. [p=0.5] {c}Três: [p=0.2] corta-se fator, "
        "nunca termo."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}Quanto é *mil e três vezes novecentos e noventa e sete,* [p=0.2] sem calculadora, [p=0.2] em *cinco "
        "segundos?* [p=0.5] {b}Próximo episódio: [p=0.2] produtos notáveis como *atalho de conta.*"),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha cortado um termo achando que era fator? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
