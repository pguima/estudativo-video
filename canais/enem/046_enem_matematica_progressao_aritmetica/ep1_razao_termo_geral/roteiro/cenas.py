# Roteiro — Progressão Aritmética, Episódio 1 de 5: o que é PA, a razão e o "n − 1"
# Base: Estudos/Enem/estudos/01-matematica/31-progressao-aritmetica.html — seções 02, 03 e 04 + Questões 2 e 1 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A PA é uma ESCADA DE DEGRAUS IGUAIS: a razão é a altura do degrau.
#   Do 1º ao 12º degrau você sobe 11 vezes: n − 1 SALTOS.
#   TESTE A FÓRMULA COM n = 1: ela tem de devolver o primeiro termo.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt). Na narração, "PA" vai escrito "pê-á" (o script de voz
#   local não aplica a tabela de pronúncia); na tela fica "PA".
# Exemplos: o gancho, a escada e o bloco c usam a Questão 2 (Ana, 50 + 11 · 15 = 215), que é o "eu faço".
#   DESVIO do prompt (para não entregar a Questão 1, "você faz", com pausa): o bloco e (padrão de figuras) e o erro 3 usam
#   TRIÂNGULOS de palitos (3 palitos, +2 por triângulo → a_n = 2n + 1; figura 20 = 41; erro: 3n), em vez dos quadrados
#   (4, +3 → 3n + 1 → figura 50 = 151, que é a resposta da Q1). Os quadrados só aparecem no concreto (4, 7, 10, sem fórmula)
#   e na própria Q1.
# Bloco d (do prompt): a_4 = 17 e a_10 = 41 → 6r = 24, r = 4, a_1 = 5. Do 5º ao 20º: 15 saltos (material).
# Bloco f (do prompt): a_n = r · n + (a_1 − r); (5, 8, 11, 14, 17, 20) sobre y = 3n + 2.
# Nós fazemos (prompt): (7, 11, 15, …) → r = 4; a_30 = 7 + 29 · 4 = 123; teste n = 1 → 7.
# QUESTÃO 2 (texto idêntico na tela, "eu faço"): a_12 = 50 + 11 · 15 = 215 → C. Erradas (material e prompt):
#   A (165) = só o acréscimo, 11 · 15 · B (180) = 12 · 15 sem os 50 · D (230) = 12 saltos · E (1 590) = soma dos 12.
# QUESTÃO 1 (texto idêntico na tela, "você faz"): a_50 = 4 + 49 · 3 = 151 → D. Erradas (CORREÇÃO do roteiros.md):
#   o material diz que "A usa razão 2", mas razão 2 daria 4 + 49 · 2 = 102. O vídeo diz: A (101) = quem acha que cada
#   quadrado novo acrescenta 2 palitos e faz 2 · 50 + 1 · B (148) = 3 · 49 + 1 · C (150) = 3 · 50 · E (200) = 4 · 50.
# Atalhos (verde): "teste com n = 1" · "razão = diferença dos termos ÷ diferença das posições" · "conte os saltos com o dedo".
# Frases-chave (meio e fim, idênticas): 1. Razão é segundo menos primeiro.
#   2. Do 1º ao n-ésimo termo há n − 1 saltos. 3. PA é uma reta vista só nos números inteiros.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Progressão aritmética do zero: a razão e o n − 1 | PA Ep. 1"
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
        "{a}Ana deposita *cinquenta reais* em janeiro [p=0.2] e, a cada mês, [p=0.2] *quinze reais a mais.* [p=0.4] "
        "{b}Quanto em dezembro? [p=0.5] {c}Quem faz cinquenta mais *doze* vezes quinze [p=0.2] responde duzentos e "
        "trinta reais [p=0.2] *e erra.* [p=0.4] {d}A resposta é *duzentos e quinze reais,* [p=0.3] {e}e o motivo "
        "[p=0.2] cabe numa *escada.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai achar o termo *cinquenta,* [p=0.2] *cem* [p=0.2] ou *mil* [p=0.2] de "
        "qualquer pê-á [p=0.3] {b}sem listar os anteriores."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Da série de Equações: [p=0.2] seis *erre* igual a vinte e quatro? "
        "[p=0.2] Divida os dois lados por seis: [p=0.2] *erre vale quatro.* [p=0.4] {b}E, da série de Função Afim: "
        "[p=0.2] o número que diz *quanto muda a cada unidade* [p=0.2] é o coeficiente *a* da reta. [p=0.3] Guarde essa "
        "ideia: [p=0.2] ela volta daqui a pouco."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe três coisas do dia a dia. [p=0.3] {a}Uma *escada:* [p=0.2] todos os degraus têm a mesma altura. [p=0.4] "
        "{b}Um *cofrinho* que recebe [p=0.2] quinze reais a mais a cada mês. [p=0.4] {c}E quadradinhos de *palitos de "
        "fósforo:* [p=0.2] quatro, [p=0.2] sete, [p=0.2] dez palitos. [p=0.4] {d}Nos três, [p=0.2] o próximo é o "
        "anterior [p=0.2] *mais um valor fixo.*"),

    # ================= BLOCO A: O QUE É PA =================
    dict(id="05", block="definicao", text=
        "{t}Antes do nome difícil, [p=0.2] três palavras simples. [p=0.3] {a}*Sequência* é uma lista de números em "
        "ordem: [p=0.2] tem primeiro, [p=0.2] segundo, [p=0.2] terceiro. [p=0.4] {b}Cada número da lista [p=0.2] é um "
        "*termo.* [p=0.4] {c}E o lugar dele na fila é a *posição,* [p=0.2] também chamada de *índice.* [p=0.4] {d}O "
        "primeiro termo se escreve *a um;* [p=0.2] o termo da posição *ene* [p=0.2] se escreve *a ene.*"),
    dict(id="06", block="pa", text=
        "{t}E o que faz uma sequência ser uma pê-á? [p=0.4] {a}*Progressão aritmética,* [p=0.2] a pê-á, [p=0.2] é a "
        "sequência em que cada termo [p=0.2] é o anterior *mais um número fixo.* [p=0.4] {b}Esse número fixo é a "
        "*razão,* [p=0.2] a letra *erre.* [p=0.4] {c}Cinco, oito, onze, catorze: [p=0.2] sempre mais três. [p=0.2] "
        "*Razão três,* positiva: [p=0.2] os termos sobem, [p=0.2] pê-á *crescente.* [p=0.4] {d}A pê-á é uma escada de "
        "degraus iguais: [p=0.2] a razão é *a altura do degrau.*"),
    dict(id="07", block="pa", text=
        "{t}E se o degrau descer? [p=0.4] {a}Quarenta, trinta e quatro, vinte e oito: [p=0.2] razão *menos seis.* "
        "[p=0.2] Os termos diminuem: [p=0.2] pê-á *decrescente.* [p=0.4] {b}Sete, sete, sete: [p=0.2] razão *zero,* "
        "[p=0.2] pê-á *constante.* [p=0.4] {c}Um e meio, dois, dois e meio: [p=0.2] razão *zero vírgula cinco.* [p=0.2] "
        "A razão não precisa ser inteira. [p=0.4] {d}E dois, quatro, oito, dezesseis? [p=0.3] As diferenças são dois, "
        "quatro, oito: [p=0.2] *não* são iguais. [p=0.2] Isso *não é pê-á;* [p=0.2] é assunto da próxima série."),

    # ================= BLOCO B: RAZÃO =================
    dict(id="08", block="razao", text=
        "{t}Como achar a razão sem errar o sinal? [p=0.4] {a}*Segundo menos primeiro.* [p=0.3] Sempre nessa ordem. "
        "[p=0.4] {b}Em quarenta, trinta e quatro, vinte e oito: [p=0.2] trinta e quatro *menos* quarenta [p=0.2] dá "
        "*menos seis.* [p=0.4] {c}Quem faz o maior menos o menor [p=0.2] fica com *mais seis,* [p=0.3] {d}e a sequência "
        "passa a *subir* [p=0.2] quando deveria *descer.*"),

    # ================= BLOCO C: TERMO GERAL =================
    dict(id="09", block="saltos", text=
        "{t}Agora, o coração da aula. [p=0.2] Quanto Ana deposita em dezembro? [p=0.4] {a}Escreva os primeiros: [p=0.2] "
        "*a um* é cinquenta, [p=0.2] *a dois* é sessenta e cinco, [p=0.2] *a três* é oitenta. [p=0.4] {b}Agora suba a "
        "escada com o dedo. [p=0.2] Do primeiro ao segundo degrau: [p=0.2] *um* salto. [p=0.2] Do primeiro ao terceiro: "
        "[p=0.2] *dois* saltos. [p=0.4] {c}E do primeiro ao *décimo segundo?* [p=0.5] {d}*Onze* saltos. [p=0.3] Do "
        "primeiro ao décimo segundo degrau, [p=0.2] você sobe *onze* vezes."),
    dict(id="10", block="formula", text=
        "{t}Isso vira uma fórmula. [p=0.3] {a}Para chegar à posição *ene,* [p=0.2] você dá *ene menos um* saltos. "
        "[p=0.4] {b}Então *a ene* é igual a *a um* [p=0.2] mais *ene menos um* vezes *erre.* [p=0.3] É o *termo geral:* "
        "[p=0.2] a fórmula que entrega qualquer termo direto. [p=0.4] {c}Dezembro: [p=0.2] cinquenta mais *onze* vezes "
        "quinze. [p=0.2] Cinquenta mais cento e sessenta e cinco: [p=0.2] *duzentos e quinze reais.*"),
    dict(id="11", block="teste", text=
        "{t}E como saber se a fórmula está certa? [p=0.4] {a}Teste com *ene igual a um.* [p=0.3] Ela tem de devolver o "
        "primeiro termo. [p=0.4] {b}Um menos um é zero; [p=0.2] zero vezes quinze é zero; [p=0.2] sobra *cinquenta.* "
        "[p=0.2] *Passou.* [p=0.4] {c}Agora a versão errada, [p=0.2] com *ene* saltos: [p=0.2] cinquenta mais um vezes "
        "quinze [p=0.2] dá *sessenta e cinco.* [p=0.3] {d}Janeiro com sessenta e cinco? [p=0.2] *Reprovada.*"),

    # ================= BLOCO D: A PARTIR DE QUALQUER TERMO =================
    dict(id="12", block="qualquer", text=
        "{t}E se você não conhece o primeiro termo? [p=0.4] {a}Comece de *qualquer* termo conhecido. [p=0.3] *A ene* é "
        "igual a *a ká* [p=0.2] mais *ene menos ká* vezes *erre.* [p=0.4] {b}O *ká* é só a posição de onde você parte. "
        "[p=0.4] {c}Do quinto ao vigésimo termo, [p=0.2] por exemplo, [p=0.2] são vinte menos cinco: [p=0.2] *quinze* "
        "saltos."),
    dict(id="13", block="dois", text=
        "{t}E dá para achar a razão com dois termos soltos? [p=0.4] {a}Dá. [p=0.2] *A quatro* é dezessete [p=0.2] e *a "
        "dez* é quarenta e um. [p=0.4] {b}Do quarto ao décimo: [p=0.2] *seis* saltos. [p=0.2] E o termo subiu quarenta "
        "e um menos dezessete: [p=0.2] *vinte e quatro.* [p=0.4] {c}Seis *erre* igual a vinte e quatro: [p=0.2] *erre "
        "igual a quatro.* [p=0.4] {d}E o primeiro? [p=0.2] Desça três saltos a partir do quarto: [p=0.2] dezessete menos "
        "doze, [p=0.2] *cinco.*"),
    dict(id="14", block="dois", text=
        "{a}O atalho: [p=0.2] *razão é a diferença dos termos [p=0.2] dividida pela diferença das posições.* [p=0.4] "
        "{b}Quarenta e um menos dezessete, [p=0.2] vinte e quatro; [p=0.2] dez menos quatro, [p=0.2] seis. [p=0.2] Vinte "
        "e quatro dividido por seis: [p=0.2] *quatro.* [p=0.3] {c}Sem montar equação nenhuma."),

    # ================= BLOCO E: PADRÃO DE FIGURAS =================
    dict(id="15", block="figuras", text=
        "{t}E os palitos? [p=0.2] Vamos treinar com *triângulos,* [p=0.2] que funcionam do mesmo jeito. [p=0.4] {a}O "
        "primeiro triângulo usa *três* palitos. [p=0.4] {b}O segundo encosta no primeiro [p=0.2] e *aproveita um lado:* "
        "[p=0.2] só precisa de *dois* palitos novos. [p=0.4] {c}Três, cinco, sete: [p=0.2] pê-á de razão *dois.* [p=0.4] "
        "{d}Figura *ene:* [p=0.2] três mais *ene menos um* vezes dois, [p=0.2] que dá *dois ene mais um.* [p=0.3] A "
        "figura vinte usa *quarenta e um* palitos, [p=0.2] sem desenhar nenhuma das anteriores."),

    # ================= BLOCO F: PA E FUNÇÃO AFIM =================
    dict(id="16", block="afim", text=
        "{t}E por que a pê-á lembra uma reta? [p=0.4] {a}Abra o termo geral: [p=0.2] *a ene* é igual a *erre* vezes "
        "*ene,* [p=0.2] mais *a um menos erre.* [p=0.4] {b}É a cara de uma *função afim:* [p=0.2] *y* igual a *a x* "
        "mais *b.* [p=0.4] {c}A razão faz o papel do coeficiente *a:* [p=0.2] *quanto muda a cada passo.*"),
    dict(id="17", block="afim", text=
        "{a}Marque a pê-á cinco, oito, onze, catorze, dezessete, vinte [p=0.2] no plano. [p=0.4] {b}Os pontos ficam "
        "*alinhados* [p=0.2] sobre a reta *y* igual a *três ene mais dois.* [p=0.4] {c}Mas são *pontos soltos:* [p=0.2] "
        "não existe a posição dois e meio. [p=0.4] {d}A cada passo de um na posição, [p=0.2] o termo sobe *três:* "
        "[p=0.2] a razão é a *inclinação.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Qual é o *trigésimo* termo da pê-á [p=0.2] sete, onze, quinze? [p=0.5] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Razão: [p=0.2] segundo menos primeiro, [p=0.2] onze menos sete, [p=0.2] *quatro.* "
        "[p=0.4] {b}Do primeiro ao trigésimo: [p=0.2] *vinte e nove* saltos. [p=0.4] {c}Sete mais vinte e nove vezes "
        "quatro: [p=0.2] sete mais cento e dezesseis, [p=0.2] *cento e vinte e três.* [p=0.4] {d}Teste com *ene igual a "
        "um:* [p=0.2] sete mais zero vezes quatro, [p=0.2] *sete.* [p=0.2] Passou."),

    # ================= MINI-RECAP =================
    dict(id="20", block="recap", text=
        "{t}Três frases para guardar. [p=0.5] {a}Um: [p=0.2] razão é segundo menos primeiro. [p=0.5] {b}Dois: [p=0.2] do "
        "primeiro ao *ene*-ésimo termo [p=0.2] há *ene menos um* saltos. [p=0.5] {c}Três: [p=0.2] pê-á é uma reta "
        "[p=0.2] vista só nos números inteiros."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{a}Erro um: [p=0.2] *a doze* igual a *a um* [p=0.2] mais *doze* vezes *erre.* [p=0.4] {b}Parece certo porque é "
        "o *décimo segundo* termo, [p=0.2] e o doze está ali, [p=0.2] pedindo para entrar. [p=0.4] {c}Mas o primeiro "
        "degrau já é o ponto de partida: [p=0.2] são *onze* saltos. [p=0.2] Um salto a mais [p=0.2] é exatamente a "
        "alternativa errada."),
    dict(id="22", block="erros", text=
        "{a}Erro dois: [p=0.2] razão de quarenta, trinta e quatro, vinte e oito [p=0.2] igual a *seis.* [p=0.4] "
        "{b}Parece certo porque a distância entre os números é mesmo seis, [p=0.2] e o sinal some sem barulho. [p=0.4] "
        "{c}Faça segundo menos primeiro: [p=0.2] *menos seis.* [p=0.2] Sequência que desce [p=0.2] tem razão negativa."),
    dict(id="23", block="erros", text=
        "{a}Erro três: [p=0.2] contar *três* palitos por triângulo [p=0.2] e dizer que a figura *ene* usa *três ene* "
        "palitos. [p=0.4] {b}Parece certo porque cada triângulo, sozinho, [p=0.2] tem mesmo três lados. [p=0.4] {c}Mas "
        "os vizinhos *dividem um lado.* [p=0.2] Só o primeiro usa três; [p=0.2] cada novo usa dois: [p=0.2] *dois ene "
        "mais um.*"),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="24", block="q2", text=
        "{t}Questão do material, [p=0.2] e esta eu faço com você. [p=0.3] {a}Para juntar dinheiro, [p=0.2] Ana depositou "
        "*cinquenta reais* em janeiro [p=0.2] e decidiu que, a cada mês, [p=0.2] depositaria *quinze reais a mais* do "
        "que no mês anterior. [p=0.2] O valor que ela vai depositar em *dezembro,* [p=0.2] o décimo segundo mês, é: "
        "[p=0.4] {qa}A: [p=0.2] cento e sessenta e cinco reais. [p=0.3] {qb}B: [p=0.2] cento e oitenta. [p=0.3] {qc}C: "
        "[p=0.2] duzentos e quinze. [p=0.3] {qd}D: [p=0.2] duzentos e trinta. [p=0.3] {qe}E: [p=0.2] mil quinhentos e "
        "noventa reais."),
    dict(id="25", block="q2", text=
        "{t}Primeiro, os três primeiros termos: [p=0.2] cinquenta, sessenta e cinco, oitenta. [p=0.2] Razão *quinze.* "
        "[p=0.4] {a}Dezembro é a posição doze: [p=0.2] *onze* saltos. [p=0.4] {b}Cinquenta mais onze vezes quinze: "
        "[p=0.2] *duzentos e quinze.* [p=0.4] {c}Faz sentido? [p=0.2] Partindo de cinquenta [p=0.2] e subindo quinze por "
        "mês, [p=0.2] chegar perto de duzentos [p=0.2] é razoável. [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="q2", text=
        "{t}E as outras? [p=0.3] {xa}A A, cento e sessenta e cinco, [p=0.2] é *só o acréscimo:* [p=0.2] onze vezes "
        "quinze, [p=0.2] sem os cinquenta. [p=0.4] {xb}A B usa doze vezes quinze [p=0.2] e esquece o depósito inicial. "
        "[p=0.4] {xd}A D, duzentos e trinta, [p=0.2] usou *doze* saltos. [p=0.4] {xe}E a E é a *soma* dos doze "
        "depósitos, [p=0.2] que ninguém pediu."),

    # ================= QUESTÃO 1 (VOCÊ FAZ) =================
    dict(id="27", block="q1", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma criança monta, com palitos de fósforo, [p=0.2] uma sequência de figuras. "
        "[p=0.2] A figura um é um quadrado, [p=0.2] com *quatro* palitos; [p=0.2] a figura dois tem dois quadrados lado a "
        "lado, [p=0.2] que compartilham um palito, [p=0.2] com *sete* palitos; [p=0.2] a figura três tem três quadrados "
        "em fila, [p=0.2] com *dez* palitos, [p=0.2] e assim por diante. [p=0.2] O número de palitos para montar a "
        "figura *cinquenta* é: [p=0.4] {qa}A: [p=0.2] cento e um. [p=0.3] {qb}B: [p=0.2] cento e quarenta e oito. "
        "[p=0.3] {qc}C: [p=0.2] cento e cinquenta. [p=0.3] {qd}D: [p=0.2] cento e cinquenta e um. [p=0.3] {qe}E: "
        "[p=0.2] duzentos. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="28", block="q1", text=
        "{t}Conferindo. [p=0.2] Quatro, sete, dez: [p=0.2] razão *três.* [p=0.4] {a}Da figura um até a cinquenta: "
        "[p=0.2] *quarenta e nove* saltos. [p=0.4] {b}Quatro mais quarenta e nove vezes três: [p=0.2] quatro mais cento "
        "e quarenta e sete, [p=0.2] *cento e cinquenta e um.* [p=0.4] {c}Pela forma de reta: [p=0.2] três vezes "
        "cinquenta, mais um. [p=0.2] Mesmo resultado. [p=0.3] {ok}*Letra D!*"),
    dict(id="29", block="q1", text=
        "{t}E as erradas? [p=0.3] {xa}A A, cento e um, [p=0.2] é de quem acha que cada quadrado novo acrescenta *dois* "
        "palitos: [p=0.2] dois vezes cinquenta, mais um. [p=0.4] {xb}A B usou *quarenta e nove* quadrados. [p=0.4] "
        "{xc}A C esqueceu o palito inicial: [p=0.2] três vezes cinquenta. [p=0.4] {xe}E a E contou *quatro* palitos por "
        "quadrado, [p=0.2] ignorando os lados compartilhados."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] razão é segundo menos primeiro. [p=0.5] {b}Dois: "
        "[p=0.2] do primeiro ao *ene*-ésimo termo [p=0.2] há *ene menos um* saltos. [p=0.5] {c}Três: [p=0.2] pê-á é uma "
        "reta [p=0.2] vista só nos números inteiros."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Entre os postes do quilômetro *três* [p=0.2] e do quilômetro *vinte e sete* [p=0.2] vão entrar mais *cinco* "
        "postes, [p=0.2] todos igualmente espaçados. [p=0.4] {b}A distância entre eles [p=0.2] é vinte e quatro dividido "
        "por cinco? [p=0.4] {c}*Não.* [p=0.4] {d}Próximo episódio: [p=0.2] contar termos e saltos *sem errar.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído no salto a mais? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
