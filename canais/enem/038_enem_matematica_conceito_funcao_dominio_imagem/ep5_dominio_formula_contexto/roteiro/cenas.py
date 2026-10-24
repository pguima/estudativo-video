# Roteiro — Conceito de Função, Domínio e Imagem, Episódio 5 de 6: domínio pela fórmula e pelo contexto.
# Base: Estudos/Enem/estudos/01-matematica/23-conceito-funcao-dominio-imagem.html — seção 08 + Questões 3 e 5 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   As DUAS PROIBIÇÕES DA CALCULADORA: dividir por zero e tirar raiz quadrada de número negativo.
#   O domínio é o PORTEIRO: só deixa entrar o x com o qual a conta existe E que faz sentido no problema.
#   A CORRENTE arrebenta no elo mais fraco: com várias condições, vale a mais restritiva.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Contas (conferidas em Python): f(x) = 1/(x − 3) → x ≠ 3 (f(4) = 1) · g(x) = √(x − 2) → x ≥ 2 (g(2) = √0 = 0; g(1) = √(−1)
#   proibido) · h(x) = 5/√x → x > 0 · p(x) = 3x² − x + 7 → ℝ · bola h(t) = 20t − 5t² no ar de 0 a 4 s (h(4) = 0).
#   Pré-requisito (exemplo nosso): −3x ≥ 12 → x ≤ −4 (dividiu por −3, o sinal virou).
#   Nós fazemos (prompt): √(10 − 2x) → 10 − 2x ≥ 0 → −2x ≥ −10 → x ≤ 5 (x = 5 dá √0 = 0; x = 6 dá √(−2)).
#   Gancho: V(12) = 12 · 6 · (−4) = −288: a fórmula calcula, mas a largura 20 − 24 = −4 cm não existe.
# TROCA DE EXEMPLO (regra de exemplos): o bloco f do prompt usa a folha de 30 cm × 20 cm, que é exatamente a Questão 5
#   ("você faz", com pausa: resposta 0 < x < 10). No bloco f usamos uma folha NOSSA de 36 cm × 16 cm: 36 − 2x > 0 → x < 18;
#   16 − 2x > 0 → x < 8 → 0 < x < 8. A animação principal da folha 30 × 20 (o lado de 20 some em x = 10, selo "a caixa
#   não existe") fica na RESOLUÇÃO da Q5, depois da pausa. O erro 1 também usa a folha 36 × 16 (V(9) = 9 · 18 · (−2) = −324).
# QUESTÃO 3 (eu faço): f(x) = √(x − 2)/(x − 5) → x ≥ 2 e x ≠ 5 → D. f(2) = 0/(−3) = 0 (o 2 entra); f(5) = √3/0 (erro).
#   Erradas (do material): C exclui o 2 à toa; A esquece o denominador; B esquece a raiz; E exclui o trecho entre 2 e 5
#   (x = 3 dá √1/(−2) = −0,5, sem erro).
# QUESTÃO 5 (você faz): caixa 30 × 20 → x > 0, x < 15, x < 10 → 0 < x < 10 → B. Erradas (do material): A usa só o lado de
#   30 cm; D esquece que se recorta x dos dois lados (20 − x > 0 → x < 20); C ignora o tamanho da folha; E é o trecho em que
#   20 − 2x é negativo (volume negativo, como o −288 do gancho).
# Acréscimos NOSSOS: atalho verde "raiz: bolinha fechada · denominador: furo" (cena 08); atalho verde "teste os extremos
#   na fórmula" (cena 15, junto do nós fazemos).
# Frases-chave (meio e fim, idênticas): 1. Denominador não pode ser zero; raiz quadrada não aceita negativo.
#   2. O contexto corta ainda mais: medida positiva, contagem inteira. 3. Com várias condições, vale a mais restritiva.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Domínio pela fórmula e pelo contexto: as duas proibições e a caixa de papelão · Matemática ENEM, Funções episódio 5"

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
        "{a}De uma folha de *30 cm por 20 cm,* [p=0.2] você recorta quadradinhos nos cantos [p=0.2] para montar uma "
        "caixa. [p=0.4] {b}A fórmula do volume aceita *x igual a 12 cm.* [p=0.4] {c}A folha, *não:* [p=0.2] com 12 cm, "
        "[p=0.2] um dos lados some antes. [p=0.5] {d}Hoje você aprende a ouvir as duas, [p=0.2] *a fórmula e o problema.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai achar o domínio de fórmulas com *fração* e *raiz* [p=0.3] {b}e cortar o domínio "
        "pelo *contexto:* [p=0.2] medidas positivas, [p=0.2] contagens inteiras, [p=0.2] tempo não negativo."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] o *domínio* é o conjunto das entradas "
        "permitidas. [p=0.4] {b}E, da série de Equações e inequações: [p=0.2] "
        "se *dividir por negativo,* [p=0.2] *o sinal vira.* [p=0.3] "
        "Menos três x maior ou igual a doze [p=0.2] vira *x menor ou igual a menos quatro.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Já viu uma conta dar erro? [p=0.4] {a}Numa *planilha,* [p=0.2] divida por zero: [p=0.2] aparece "
        "*#DIV/0!* [p=0.4] {b}Na *calculadora,* [p=0.2] tire a raiz de menos quatro: [p=0.2] *erro.* [p=0.4] {c}São as "
        "*duas proibições da calculadora:* [p=0.2] dividir por zero [p=0.2] e tirar raiz quadrada de número negativo."),

    # ================= BLOCO A: DOMÍNIO PELA FÓRMULA =================
    dict(id="05", block="porteiro", text=
        "{t}Quando a função vem só com a fórmula, [p=0.2] quem entra? [p=0.4] {a}O *domínio da fórmula* é o "
        "maior conjunto de números reais [p=0.2] com o qual a conta *existe.* [p=0.4] {b}Os *números reais* "
        "[p=0.2] são todos os números da reta: [p=0.2] negativos, [p=0.2] decimais, [p=0.2] frações. "
        "[p=0.4] {c}Pense num *porteiro:* [p=0.2] só entra o x com o qual a conta não dá erro. [p=0.3] Cada proibição é uma *restrição.*"),

    # ================= BLOCO B: DENOMINADOR =================
    dict(id="06", block="denominador", text=
        "{t}Primeira proibição: [p=0.2] onde mora a divisão? [p=0.4] {a}No *denominador,* [p=0.2] o "
        "número de baixo da fração. [p=0.4] {b}Em *f de x igual a um sobre x menos três,* [p=0.2] o x três dá "
        "um sobre *zero.* [p=0.2] Proibido. [p=0.4] {c}Com x igual a quatro: [p=0.2] um "
        "sobre um, [p=0.2] *um.* [p=0.2] Pode. [p=0.4] {d}Domínio: [p=0.2] *x diferente de três.*"),

    # ================= BLOCO C: RADICANDO =================
    dict(id="07", block="radicando", text=
        "{t}Segunda proibição: [p=0.2] a raiz. [p=0.4] {a}A *raiz quadrada* de um número [p=0.2] é o número que, "
        "vezes ele mesmo, [p=0.2] dá o original: [p=0.2] raiz de nove é três. [p=0.3] O que fica dentro dela "
        "[p=0.2] se chama *radicando.* [p=0.4] {b}Em *g de x igual à raiz de x menos dois,* [p=0.2] o radicando não pode "
        "ser negativo: [p=0.2] x menos dois *maior ou igual a zero,* [p=0.2] *x maior ou igual a dois.* [p=0.4] {c}Teste "
        "o extremo: [p=0.2] x igual a dois [p=0.2] dá raiz de zero, [p=0.2] *zero.* [p=0.2] *Pode.* [p=0.3] {d}x igual a "
        "um [p=0.2] dá raiz de menos um: [p=0.2] proibido."),
    dict(id="08", block="atalho", text=
        "{t}Como desenhar rápido? [p=0.3] {a}Atalho: [p=0.2] ache a *fronteira* igualando a zero o que está em "
        "perigo. [p=0.4] {b}Na *raiz,* [p=0.2] o zero *entra:* [p=0.2] *bolinha fechada.* [p=0.4] {c}No *denominador,* "
        "[p=0.2] o zero *não entra:* [p=0.2] *bolinha aberta,* [p=0.2] um furo na reta."),

    # ================= BLOCO D: AS DUAS JUNTAS =================
    dict(id="09", block="juntas", text=
        "{t}E as duas juntas? [p=0.4] {a}Em *h de x igual a cinco sobre raiz de x:* [p=0.2] a "
        "raiz pede *x maior ou igual a zero.* [p=0.4] {b}Mas a raiz está no *denominador:* [p=0.2] raiz de zero é zero, "
        "[p=0.2] e cinco sobre zero é proibido. [p=0.4] {c}O zero passa no primeiro porteiro [p=0.2] e é barrado "
        "no segundo. [p=0.3] Domínio: [p=0.2] *x maior que zero.*"),
    dict(id="10", block="juntas", text=
        "{t}E sem proibição nenhuma? [p=0.4] {a}Em *p de x igual a três x ao quadrado, menos x, mais sete,* "
        "[p=0.2] não tem divisão por x [p=0.2] nem raiz. [p=0.4] {b}Domínio: [p=0.2] *todos os reais,* "
        "[p=0.2] a reta inteira."),

    # ================= BLOCO E: DOMÍNIO PELO CONTEXTO =================
    dict(id="11", block="contexto", text=
        "{t}Mas a conta existir basta? [p=0.4] {a}Num problema, [p=0.2] o porteiro faz uma *segunda pergunta:* "
        "[p=0.2] *isso faz sentido aqui?* [p=0.3] A situação real [p=0.2] é o *contexto.* [p=0.4] {b}*Contagens,* "
        "[p=0.2] como pessoas e ingressos, [p=0.2] só aceitam *números naturais:* [p=0.2] zero, um, dois, três... "
        "[p=0.3] Não existe meio ingresso. [p=0.4] {c}Por isso o gráfico é feito de *pontos isolados,* [p=0.2] sem linha "
        "ligando."),
    dict(id="12", block="contexto", text=
        "{a}*Tempo e distância:* [p=0.2] não negativos, [p=0.2] e às vezes *limitados.* [p=0.3] A bola jogada para cima "
        "[p=0.2] só está no ar de zero a quatro segundos, [p=0.2] quando toca o chão. [p=0.4] {b}*Medidas de figuras:* "
        "[p=0.2] lado, altura, largura [p=0.2] precisam ser *positivas.*"),

    # ================= BLOCO F: A CAIXA (EXEMPLO NOSSO) =================
    dict(id="13", block="caixa", text=
        "{t}E com várias condições ao mesmo tempo? [p=0.4] {a}Pegue uma folha de *36 cm por 16 cm* [p=0.2] e "
        "recorte quadradinhos de lado x nos cantos. [p=0.4] {b}A altura da caixa é *x:* [p=0.2] x maior que zero. "
        "[p=0.3] {c}O comprimento perde x dos *dois* lados: [p=0.2] 36 menos dois x maior que zero, [p=0.2] *x menor que "
        "dezoito.* [p=0.4] {d}A largura: [p=0.2] 16 menos dois x maior que zero, [p=0.2] *x menor que oito.*"),
    dict(id="14", block="caixa", text=
        "{t}Qual condição manda? [p=0.4] {a}Com x igual a oito, [p=0.2] a largura *some,* [p=0.2] enquanto o comprimento "
        "ainda tem vinte centímetros. [p=0.4] {b}Uma *corrente arrebenta no elo mais fraco:* [p=0.2] vale a condição *mais "
        "restritiva.* [p=0.4] {c}Domínio: [p=0.2] *x entre zero e oito,* [p=0.2] sem os extremos."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Qual é o domínio de *g de x igual à raiz de dez menos dois x?* [p=0.4] {b}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Radicando maior ou igual a zero: [p=0.2] dez menos dois x maior ou igual a zero. "
        "[p=0.4] {b}Passo o dez: [p=0.2] *menos dois x maior ou igual a menos dez.* [p=0.4] {c}Divido por menos dois: "
        "[p=0.2] *o sinal vira.* [p=0.2] *x menor ou igual a cinco.* [p=0.4] {d}Teste os extremos: [p=0.2] x igual a "
        "cinco dá raiz de zero, [p=0.2] *pode.* [p=0.3] x igual a seis dá raiz de menos dois, [p=0.2] *proibido.* "
        "[p=0.3] {e}Atalho: [p=0.2] *teste a fronteira e um vizinho.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] denominador não pode ser zero; [p=0.2] raiz quadrada "
        "não aceita negativo. [p=0.5] {b}Dois: [p=0.2] o contexto corta ainda mais: [p=0.2] medida positiva, [p=0.2] "
        "contagem inteira. [p=0.5] {c}Três: [p=0.2] com várias condições, [p=0.2] vale a mais restritiva."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *esquecer o contexto.* [p=0.2] Na folha de 36 "
        "por 16, [p=0.2] a fórmula aceita x igual a nove. [p=0.4] {b}Parece certo, [p=0.2] porque a conta sai: [p=0.2] "
        "menos 324. [p=0.4] {c}Mas a largura ficou com menos dois centímetros."),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] *excluir à toa* um extremo que funciona, [p=0.2] e tirar o dois da raiz de x menos dois. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o zero assusta, [p=0.2] como no denominador. [p=0.4] {c}Mas raiz de "
        "zero é zero. [p=0.2] *Teste* antes de expulsar."),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] *usar só uma condição* quando há duas. [p=0.2] Em cinco sobre raiz de x, [p=0.2] "
        "responder x maior ou igual a zero. [p=0.4] {b}Parece certo, [p=0.2] porque você viu a raiz [p=0.2] e parou. "
        "[p=0.4] {c}Mas ela está no denominador: [p=0.2] o zero cai."),
    dict(id="21", block="erros", text=
        "{a}Quarto: [p=0.2] desenhar *linha contínua* num problema de *contagem.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque a fórmula aceita dois e meio. [p=0.4] {c}Mas meio ingresso não se vende: [p=0.2] *pontos "
        "isolados.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="22", block="q3", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Uma planilha "
        "calcula um índice pela fórmula [p=0.2] *f de x igual à raiz de x menos dois, sobre x menos cinco,* [p=0.3] e "
        "mostra *erro* quando a conta não pode ser feita. [p=0.3] Sem erro, quando: [p=0.4] "
        "{qa}A: [p=0.2] x maior ou igual a dois. [p=0.3] {qb}B: [p=0.2] x diferente de cinco. [p=0.3] {qc}C: [p=0.2] x "
        "maior que dois e x diferente de cinco. [p=0.3] {qd}D: [p=0.2] x maior ou igual a dois e x diferente de cinco. "
        "[p=0.3] {qe}E: [p=0.2] x maior que cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q3", text=
        "{t}Duas proibições. [p=0.4] {a}Raiz: [p=0.2] x menos dois maior ou igual a zero, [p=0.2] *x maior "
        "ou igual a dois.* [p=0.4] {b}Denominador: [p=0.2] x menos cinco diferente de zero, [p=0.2] *x diferente de "
        "cinco.* [p=0.4] {c}Teste os extremos. [p=0.2] x igual a dois: [p=0.2] zero sobre menos três, [p=0.2] *zero.* "
        "[p=0.2] Sem erro: [p=0.2] o dois *entra.* [p=0.3] {d}x igual a cinco: [p=0.2] divisão por zero. [p=0.2] O cinco "
        "*fica de fora.* [p=0.3] {ok}*Letra D!*"),
    dict(id="24", block="q3", text=
        "{t}E as outras? [p=0.3] {xc}A C exclui o dois à toa. [p=0.4] {xa}A A esquece o denominador. [p=0.3] {xb}A B "
        "esquece a raiz. [p=0.4] {xe}E a E exclui o trecho entre dois e cinco, [p=0.2] onde a conta funciona: [p=0.2] x "
        "igual a três dá *menos meio.*"),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="25", block="q5", text=
        "{t}E esta é *sua.* [p=0.3] {a}De uma folha de *30 cm por 20 cm* [p=0.2] recortam-se nos cantos "
        "[p=0.2] quadrados de lado x [p=0.2] para uma caixa sem tampa. [p=0.3] O volume é *x vezes trinta "
        "menos dois x, vezes vinte menos dois x.* [p=0.3] O domínio deve ser: [p=0.4] "
        "{qa}A: [p=0.2] x entre zero e quinze. [p=0.3] {qb}B: [p=0.2] x entre zero e dez. [p=0.3] {qc}C: [p=0.2] x maior "
        "que zero. [p=0.3] {qd}D: [p=0.2] x entre zero e vinte. [p=0.3] {qe}E: [p=0.2] x entre dez e quinze. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q5", text=
        "{t}Conferindo. [p=0.3] {a}Três medidas positivas: [p=0.2] x maior que zero, [p=0.2] trinta menos dois x "
        "positivo, [p=0.2] *x menor que quinze,* [p=0.2] e vinte menos dois x positivo, [p=0.2] *x menor que dez.* "
        "[p=0.4] {b}Em x igual a dez, [p=0.2] o lado de *20 cm desaparece:* [p=0.2] a caixa não existe, [p=0.2] e o de "
        "trinta ainda sobra. [p=0.4] {c}O elo mais fraco é o lado de vinte. [p=0.3] {ok}Entre zero e dez: [p=0.2] "
        "*letra B!*"),
    dict(id="27", block="q5", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A usa só o lado de trinta. [p=0.3] {xd}A D tira só *um* x "
        "do lado de vinte. [p=0.3] {xc}A C ignora o tamanho da folha. [p=0.4] {xe}E a E é o trecho em que vinte menos dois x é "
        "negativo: [p=0.2] volume negativo, [p=0.2] como o *x igual a 12* do começo."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] denominador não pode ser zero; [p=0.2] raiz "
        "quadrada não aceita negativo. [p=0.5] {b}Dois: [p=0.2] o contexto corta ainda mais: [p=0.2] medida positiva, "
        "[p=0.2] contagem inteira. [p=0.5] {c}Três: [p=0.2] com várias condições, [p=0.2] vale a mais restritiva."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}vemos como funções aparecem em "
        "*Física, Química, Biologia e Geografia* [p=0.3] {c}e caçamos as pegadinhas."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual das duas proibições da calculadora você já viu dar erro? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
