# Roteiro — Conceito de Função, Domínio e Imagem, Episódio 2 de 6: domínio, contradomínio, imagem e a notação f(x).
# Base: Estudos/Enem/estudos/01-matematica/23-conceito-funcao-dominio-imagem.html — seção 04 e 1ª parte da seção 05
#   (tabela de substituições e o quadro "f(a + b) não é f(a) + f(b)") + Questões 4 e 7 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Domínio é o que PODE entrar; contradomínio é o CARDÁPIO; imagem é o que REALMENTE sai da cozinha (parte do cardápio).
#   O x é uma CADEIRA VAZIA: o que vier entre parênteses senta no lugar dele, e senta COM os parênteses.
#   O f não é um número multiplicando o parêntese: é o NOME DA MÁQUINA (por isso f(3x) não é 3·f(x)).
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Contas (conferidas em Python), f(x) = x² − 1: f(3) = 8 · f(−2) = (−2)² − 1 = 3 (o erro −2² − 1 dá −5) · f(x + 1) =
#   (x + 1)² − 1 = x² + 2x · f(5) = 24 · f(2) + f(3) = 3 + 8 = 11. Seção 04: f(x) = x², A = {1, 2, 3}, B = {1, 4, 7, 9}
#   → Im = {1, 4, 9}; o 7 nunca sai.
# TROCA DE EXEMPLO (regra de exemplos): a tabela da seção 05 e a "cadeira vazia" do prompt usam f(2x) = 4x² − 1, que é
#   exatamente a resposta da Questão 7 ("você faz", com pausa). Nos blocos d e e e no erro 2, usamos f(3x) = (3x)² − 1 =
#   9x² − 1 e f(3x) ≠ 3·f(x) = 3x² − 3 (com x = 1: f(3) = 8, mas 3·f(1) = 0). O f(2x) só aparece na Q7.
# Nós fazemos (prompt): g(x) = 2x + 1, A = {0, 1, 2}, B = {0, 1, 2, 3, 4, 5} → g(0) = 1, g(1) = 3, g(2) = 5 → Im = {1, 3, 5}.
# QUESTÃO 4 (eu faço): g(x) = x², A = {−2, −1, 0, 1, 2} → imagens 4, 1, 0, 1, 4 → Im = {0, 1, 4} → B. Erradas (do material):
#   A é o contradomínio; C é o domínio; D esquece g(0) = 0; E calcula −2² em vez de (−2)² (e nem cabe em B).
# QUESTÃO 7 (você faz): f(2x) = (2x)² − 1 = 4x² − 1 → C. Erradas (do material): A esquece os parênteses (2x² eleva só o x);
#   B é 2·f(x); D é 4·f(x); E é (2x − 1)². Conferência com x = 1: f(2) = 3 e só a C dá 3 (A 1, B 0, D 0, E 1).
# Acréscimos nossos (verde): "calcule cada entrada e risque as repetidas" (imagem de conjunto finito) e "teste com x = 1"
#   (confere qualquer substituição de expressão: f(x + 1) com x = 1 vira f(2) = 3, e x² + 2x também dá 3).
# Frases-chave (meio e fim, idênticas): 1. Domínio é o que entra; imagem é o que realmente sai. 2. A imagem é parte do
#   contradomínio, não necessariamente ele todo. 3. Substitua o x pelo que estiver entre parênteses, com parênteses.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Domínio, imagem e f(x) do zero: a máquina e a cadeira vazia · Matemática ENEM, Funções episódio 2"

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
        "{a}Com *f de x igual a x ao quadrado menos um,* [p=0.3] quanto vale *f de dois mais três?* [p=0.5] {b}Muita "
        "gente faz [p=0.2] *f de dois mais f de três:* [p=0.2] três mais oito, [p=0.2] *onze.* [p=0.4] {c}A resposta é "
        "*vinte e quatro.* [p=0.4] {d}Hoje você descobre por que essas duas contas [p=0.2] dão resultados tão "
        "diferentes."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai separar *domínio, contradomínio e imagem* [p=0.2] sem confundir, [p=0.3] {b}e "
        "calcular *f de qualquer coisa:* [p=0.3] {c}de um número negativo, [p=0.2] de dois x, [p=0.2] de x mais um."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes de trinta segundos. [p=0.3] {a}Da série de Potenciação: [p=0.2] *menos dois, entre "
        "parênteses, ao quadrado* [p=0.2] é menos dois vezes menos dois: [p=0.2] *mais quatro.* [p=0.3] Sem parênteses, "
        "[p=0.2] o quadrado pega só o dois: [p=0.2] *menos quatro.* [p=0.4] {b}E da série de Expressões Algébricas: "
        "[p=0.2] *x mais um, ao quadrado,* [p=0.2] é *x ao quadrado, mais dois x, mais um.* [p=0.2] Nunca só x ao "
        "quadrado mais um."),

    # ================= CONCRETO: A MÁQUINA DE REFRIGERANTE =================
    dict(id="04", block="maquina", text=
        "{t}Imagine uma máquina de refrigerante. [p=0.3] {a}Ela aceita só moedas de *um,* [p=0.2] *dois* [p=0.2] e "
        "*cinco reais.* [p=0.2] Moeda de cinquenta centavos? [p=0.2] Não entra. [p=0.4] {b}No painel, [p=0.2] ela mostra "
        "*seis sabores.* [p=0.4] {c}Mas dois botões [p=0.2] estão *sempre esgotados.* [p=0.2] Ninguém nunca recebe "
        "esses dois. [p=0.4] {d}Guarde essa máquina: [p=0.2] ela tem *três listas diferentes.* [p=0.2] O que pode "
        "entrar, [p=0.2] o que aparece no painel [p=0.2] e o que realmente sai."),

    # ================= BLOCO A: OS TRÊS CONJUNTOS =================
    dict(id="05", block="conjuntos", text=
        "{t}Como a matemática chama essas três listas? [p=0.4] {a}Uma função *f, de A em B,* [p=0.2] leva cada elemento "
        "de A [p=0.2] a um elemento de B. [p=0.4] {b}O conjunto A [p=0.2] é o *domínio:* [p=0.2] tudo o que *pode "
        "entrar.* [p=0.4] {c}O conjunto B [p=0.2] é o *contradomínio:* [p=0.2] o *cardápio,* [p=0.2] onde as saídas são "
        "procuradas. [p=0.4] {d}E a *imagem* [p=0.2] é o que *realmente sai da cozinha.*"),
    dict(id="06", block="conjuntos", text=
        "{t}E qual é a relação entre o cardápio e o que sai? [p=0.4] {a}Tudo o que sai [p=0.2] *está no cardápio.* "
        "[p=0.2] A cozinha não inventa prato. [p=0.4] {b}Em matemática: [p=0.2] *a imagem está contida no "
        "contradomínio.* [p=0.4] {c}Esse símbolo, [p=0.2] que parece um U deitado, [p=0.2] se lê *está contido em.* "
        "[p=0.2] Quer dizer: [p=0.2] todo elemento daqui [p=0.2] também está ali."),

    # ================= BLOCO B: O EXEMPLO DA SEÇÃO 04 =================
    dict(id="07", block="exemplo", text=
        "{t}Vamos ver isso com números. [p=0.3] {a}*f de x igual a x ao quadrado.* [p=0.2] Domínio: [p=0.2] *um, dois e "
        "três.* [p=0.2] Contradomínio: [p=0.2] *um, quatro, sete e nove.* [p=0.4] {b}O um entra [p=0.2] e sai *um.* "
        "[p=0.3] {c}O dois entra [p=0.2] e sai *quatro.* [p=0.3] {d}O três entra [p=0.2] e sai *nove.* [p=0.4] {e}E o "
        "sete? [p=0.3] Está no cardápio, [p=0.2] mas *nunca sai.* [p=0.2] Nenhum número do domínio [p=0.2] chega "
        "nele."),
    dict(id="08", block="exemplo", text=
        "{t}Então, qual é a imagem? [p=0.4] {a}Só o que saiu: [p=0.2] *um, quatro e nove.* [p=0.4] {b}Ela é um pedaço "
        "recortado de dentro do cardápio. [p=0.2] *Menor* que o contradomínio. [p=0.4] {c}Atalho para achar a imagem "
        "[p=0.2] quando o domínio é uma lista: [p=0.2] *calcule cada entrada,* [p=0.2] anote as saídas [p=0.2] e *risque "
        "as repetidas.*"),

    # ================= BLOCO C: IMAGEM E PRÉ-IMAGEM =================
    dict(id="09", block="preimagem", text=
        "{t}E como se fala de uma flecha só? [p=0.4] {a}Na flecha que sai do três e chega no nove, [p=0.2] *nove é a "
        "imagem de três.* [p=0.4] {b}E pelo caminho contrário: [p=0.2] *três é a pré-imagem de nove.* [p=0.2] É o x "
        "que produziu aquele resultado. [p=0.4] {c}Imagem é a *chegada.* [p=0.2] Pré-imagem é a *partida.*"),

    # ================= BLOCO D: A NOTAÇÃO f(x) =================
    dict(id="10", block="notacao", text=
        "{t}E o que significa escrever *f de x?* [p=0.4] {a}O *f* [p=0.2] é o *nome da máquina.* [p=0.2] Não é um "
        "número multiplicando nada. [p=0.4] {b}O que vai entre parênteses [p=0.2] é *o que entra.* [p=0.4] {c}E *f de "
        "três* [p=0.2] é *o que sai* quando entra o três. [p=0.2] Esse resultado se chama *valor numérico.* [p=0.4] "
        "{d}Com *f de x igual a x ao quadrado menos um:* [p=0.2] três ao quadrado, nove, [p=0.2] menos um: [p=0.2] *f "
        "de três é oito.*"),
    dict(id="11", block="cadeira", text=
        "{t}E se entrar um número negativo? [p=0.4] {a}Pense no x como uma *cadeira vazia.* [p=0.2] Ele sai da fórmula, "
        "[p=0.2] e fica um parêntese esperando. [p=0.4] {b}O que vier [p=0.2] senta na cadeira, [p=0.2] *e senta com os "
        "parênteses.* [p=0.4] {c}*f de menos dois:* [p=0.2] abre parênteses, menos dois, fecha, [p=0.2] ao quadrado, "
        "menos um. [p=0.4] {d}Menos dois ao quadrado [p=0.2] dá *mais quatro.* [p=0.2] Menos um: [p=0.2] *três.*"),
    dict(id="12", block="cadeira", text=
        "{t}E se entrar uma expressão inteira? [p=0.4] {a}*f de três x:* [p=0.2] o três x senta na cadeira, com "
        "parênteses. [p=0.2] *Três x, entre parênteses, ao quadrado, menos um.* [p=0.4] {b}O quadrado pega o três *e* "
        "o x: [p=0.2] *nove x ao quadrado.* [p=0.2] Menos um. [p=0.4] {c}*f de três x* [p=0.2] é *nove x ao quadrado "
        "menos um.*"),
    dict(id="13", block="cadeira", text=
        "{t}Agora a mais pedida: [p=0.2] *f de x mais um.* [p=0.4] {a}O x mais um senta na cadeira: [p=0.2] *x mais um, "
        "entre parênteses, ao quadrado, menos um.* [p=0.4] {b}Pelo lembrete do começo: [p=0.2] x ao quadrado, mais dois "
        "x, mais um. [p=0.2] Menos um. [p=0.4] {c}O mais um e o menos um se cancelam: [p=0.2] *x ao quadrado mais dois "
        "x.*"),
    dict(id="14", block="cadeira", text=
        "{t}E como ter certeza de que a conta está certa? [p=0.4] {a}Atalho: [p=0.2] *teste com x igual a um.* [p=0.4] "
        "{b}Se x é um, [p=0.2] f de x mais um [p=0.2] vira *f de dois:* [p=0.2] quatro menos um, [p=0.2] *três.* [p=0.4] "
        "{c}E a resposta, x ao quadrado mais dois x? [p=0.2] Um mais dois: [p=0.2] *três.* [p=0.2] Bateu. [p=0.4] {d}Se "
        "não batesse, [p=0.2] você saberia na hora [p=0.2] que errou em algum lugar."),

    # ================= BLOCO E: f(a + b) NÃO É f(a) + f(b) =================
    dict(id="15", block="soma", text=
        "{t}Agora, o gancho do começo. [p=0.3] Por que *f de dois mais três* não é onze? [p=0.4] {a}Primeiro, [p=0.2] "
        "resolva o que está *dentro* do parêntese: [p=0.2] dois mais três, [p=0.2] *cinco.* [p=0.2] O cinco entra na "
        "máquina: [p=0.2] vinte e cinco menos um, [p=0.2] *vinte e quatro.* [p=0.4] {b}Já *f de dois mais f de três* "
        "[p=0.2] usa a máquina *duas vezes:* [p=0.2] três mais oito, [p=0.2] *onze.* [p=0.4] {c}São perguntas "
        "diferentes. [p=0.2] *A máquina não distribui.*"),
    dict(id="16", block="soma", text=
        "{t}E o *f de três x* [p=0.2] é três vezes f de x? [p=0.4] {a}Não. [p=0.2] Lembre: [p=0.2] o f é o *nome da "
        "máquina,* [p=0.2] não um número. [p=0.4] {b}*Três vezes f de x* [p=0.2] é três x ao quadrado menos três. [p=0.2] "
        "*f de três x* [p=0.2] é nove x ao quadrado menos um. [p=0.4] {c}Teste com x igual a um: [p=0.2] f de três dá "
        "*oito;* [p=0.2] três vezes f de um dá *zero.* [p=0.2] Nada a ver."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*g de x igual a dois x mais um,* [p=0.2] com domínio *zero, um e dois,* [p=0.2] e "
        "contradomínio *de zero a cinco.* [p=0.4] {b}Qual é a imagem? [p=0.3] *Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}*g de zero:* [p=0.2] dois vezes zero, mais um: [p=0.2] *um.* [p=0.3] {b}*g de um:* "
        "[p=0.2] dois mais um: [p=0.2] *três.* [p=0.3] {c}*g de dois:* [p=0.2] quatro mais um: [p=0.2] *cinco.* [p=0.4] "
        "{d}Imagem: [p=0.2] *um, três e cinco.* [p=0.4] {e}E o zero, o dois e o quatro? [p=0.2] Estão no cardápio, "
        "[p=0.2] mas nunca saem."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] domínio é o que entra; imagem é o que realmente sai. "
        "[p=0.5] {b}Dois: [p=0.2] a imagem é parte do contradomínio, não necessariamente ele todo. [p=0.5] {c}Três: "
        "[p=0.2] substitua o x pelo que estiver entre parênteses, com parênteses."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que *imagem e contradomínio* [p=0.2] "
        "são a mesma coisa. [p=0.4] {b}Parece certo, [p=0.2] porque os dois ficam do lado da saída. [p=0.4] {c}Mas o "
        "contradomínio é o cardápio inteiro; [p=0.2] a imagem é *só o que sai.* [p=0.2] Pode ser menor."),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] escrever *f de três x* [p=0.2] igual a *três vezes f de x.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o f parece um número multiplicando o parêntese. [p=0.4] {c}Mas o f é o nome da máquina. [p=0.2] "
        "O três x *entra* nela: [p=0.2] *nove x ao quadrado menos um.*"),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] *f de a mais b* [p=0.2] igual a *f de a mais f de b.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque lembra a propriedade distributiva. [p=0.4] {c}Mas a máquina não distribui. [p=0.2] Some primeiro, "
        "[p=0.2] depois aplique: [p=0.2] *f de cinco, vinte e quatro.*"),
    dict(id="23", block="erros", text=
        "{a}Quarto: [p=0.2] em *f de menos dois,* [p=0.2] escrever menos dois ao quadrado *sem parênteses.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque os números são os mesmos. [p=0.4] {c}Mas sem parênteses [p=0.2] dá menos quatro "
        "menos um, [p=0.2] *menos cinco.* [p=0.2] Com parênteses, [p=0.2] *três.* [p=0.2] Ponha o parêntese *antes* de "
        "calcular."),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="24", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] Eu resolvo, [p=0.2] e você "
        "confere. [p=0.4] {a}Considere a função *g, de A em B,* [p=0.2] com A igual a *menos dois, menos um, zero, um e "
        "dois,* [p=0.2] B igual a *zero, um, dois, três, quatro e cinco,* [p=0.2] e *g de x igual a x ao quadrado.* "
        "[p=0.2] A imagem de g é: [p=0.4] {qa}A: [p=0.2] zero, um, dois, três, quatro e cinco. [p=0.3] {qb}B: [p=0.2] "
        "zero, um e quatro. [p=0.3] {qc}C: [p=0.2] menos dois, menos um, zero, um e dois. [p=0.3] {qd}D: [p=0.2] um e "
        "quatro. [p=0.3] {qe}E: [p=0.2] menos quatro, menos um, zero, um e quatro. [p=0.4] {p}*Pause e tente* antes de "
        "mim. [p=2.0]"),
    dict(id="25", block="q4", text=
        "{t}O atalho: [p=0.2] calcule cada entrada. [p=0.3] {a}*g de menos dois:* [p=0.2] menos dois, entre parênteses, "
        "ao quadrado: [p=0.2] *quatro.* [p=0.3] {b}*g de menos um:* [p=0.2] *um.* [p=0.2] *g de zero:* [p=0.2] *zero.* "
        "[p=0.3] {c}*g de um:* [p=0.2] *um.* [p=0.2] *g de dois:* [p=0.2] *quatro.* [p=0.4] {d}Saíram quatro, um, zero, "
        "um, quatro. [p=0.2] Agora risque as repetidas: [p=0.2] num conjunto, [p=0.2] *ninguém se escreve duas vezes.* "
        "[p=0.4] {e}Imagem: [p=0.2] *zero, um e quatro.* [p=0.3] {ok}*Letra B!*"),
    dict(id="26", block="q4", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] é o *contradomínio:* [p=0.2] o cardápio inteiro, [p=0.2] não o que "
        "sai. [p=0.4] {xc}A C [p=0.2] é o *domínio:* [p=0.2] o que entra. [p=0.4] {xd}A D [p=0.2] esqueceu que *g de "
        "zero é zero.* [p=0.4] {xe}E a E [p=0.2] calculou menos dois ao quadrado *sem parênteses,* [p=0.2] e deu menos "
        "quatro. [p=0.2] Repare: [p=0.2] o menos quatro nem está no cardápio. [p=0.2] *A cozinha não inventa prato.*"),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="27", block="q7", text=
        "{t}Agora é com você. [p=0.3] {a}Dada a função *f de x igual a x ao quadrado menos um,* [p=0.2] a expressão de "
        "*f de dois x* é: [p=0.4] {qa}A: [p=0.2] dois x ao quadrado, menos um. [p=0.3] {qb}B: [p=0.2] dois x ao "
        "quadrado, menos dois. [p=0.3] {qc}C: [p=0.2] quatro x ao quadrado, menos um. [p=0.3] {qd}D: [p=0.2] quatro x ao "
        "quadrado, menos quatro. [p=0.3] {qe}E: [p=0.2] quatro x ao quadrado, menos quatro x, mais um. [p=0.4] {p}Use a "
        "cadeira vazia. [p=0.2] *Pause o vídeo e tente.* [p=2.5]"),
    dict(id="28", block="q7", text=
        "{t}Conferindo. [p=0.3] {a}O dois x senta na cadeira, *com parênteses:* [p=0.2] *dois x, entre parênteses, ao "
        "quadrado, menos um.* [p=0.4] {b}O quadrado pega o dois e o x: [p=0.2] *quatro x ao quadrado.* [p=0.2] Menos um. "
        "[p=0.4] {c}E o teste com x igual a um? [p=0.2] f de dois: [p=0.2] quatro menos um, *três.* [p=0.2] Das cinco "
        "alternativas, [p=0.2] *só a C dá três.* [p=0.3] {ok}*Letra C!*"),
    dict(id="29", block="q7", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] esqueceu os parênteses: [p=0.2] o quadrado pegou *só o x.* [p=0.4] "
        "{xb}A B [p=0.2] é *duas vezes f de x:* [p=0.2] tratou o f como número. [p=0.4] {xd}A D [p=0.2] é *quatro vezes f "
        "de x.* [p=0.4] {xe}E a E [p=0.2] elevou ao quadrado a expressão inteira: [p=0.2] *dois x menos um, ao "
        "quadrado.* [p=0.2] Não é isso que a cadeira pede."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] domínio é o que entra; imagem é o que realmente "
        "sai. [p=0.5] {b}Dois: [p=0.2] a imagem é parte do contradomínio, não necessariamente ele todo. [p=0.5] {c}Três: "
        "[p=0.2] substitua o x pelo que estiver entre parênteses, com parênteses."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Até aqui, [p=0.2] a questão dava a *entrada* [p=0.2] e pedia a saída. [p=0.4] {b}E quando ela dá a *saída,* "
        "[p=0.3] *paguei trinta reais no táxi,* [p=0.3] e pede quantos quilômetros eu andei? [p=0.5] {c}Próximo "
        "episódio: [p=0.2] *o caminho de volta.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual desses quatro erros você já cometeu? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
