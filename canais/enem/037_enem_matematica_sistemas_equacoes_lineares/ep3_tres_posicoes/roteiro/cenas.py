# Roteiro — Sistemas de Equações Lineares, Episódio 3 de 5: concorrentes, paralelas ou coincidentes — classificar sem resolver.
# Base: Estudos/Enem/estudos/01-matematica/22-sistemas-equacoes-lineares.html — seções 06 e 07 + Questões 6 e 3 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Cada equação é uma ESTRADA DE SOLUÇÕES; a solução do sistema é o CRUZAMENTO.
#   0 = 2 é a conta dizendo "esses TRILHOS nunca se encontram"; 0 = 0 é a conta dizendo "é a MESMA ESTRADA desenhada duas vezes".
#   Múltipla só do lado esquerdo: paralelas; múltipla inteira: a mesma reta.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (todos conferidos em Python):
#   Bloco a (material, seção 06): x + y = 5 e x − y = −1 → somando, 2x = 4 → (2, 3), concorrentes, SPD ·
#     x + 2y = 4 e 2x + 4y = 10 → 2 × a primeira = 2x + 4y = 8; subtraindo, 0 = 2 → paralelas, SI ·
#     x + 2y = 4 e 2x + 4y = 8 → 0 = 0 → coincidentes, SPI; pontos (4, 0), (2, 1), (0, 2) servem nas duas.
#   Bloco b (série de Equações do 1º grau, Q6 do ep. 1): fretes 40 + 3x e 3x + 36 → 0x = −4: mesma tarifa, taxas diferentes.
#   Bloco c: razões do bloco a: 1/1 = 1 e 1/(−1) = −1 (diferentes → SPD) · 1/2 = 2/4 ≠ 4/10 (SI) · 1/2 = 2/4 = 4/8 (SPI).
#   Desvio do prompt (regra de exemplos): o bloco e pedia 2x + 3y = 5 e 4x + ky = 10 → k = 6, que é exatamente a Questão 3
#     ("você faz", com pausa). O bloco e usa 3x + 2y = 7 e 6x + ky = 14 → fator 2 → k = 4; qualquer outro k → uma solução.
#   Nós fazemos (prompt): x − 3y = 2 e −2x + 6y = −4 → razões 1/(−2) = (−3)/6 = 2/(−4) = −1/2 → SPI, coincidentes;
#     com 5 no lado direito: 2/5 ≠ −1/2 → SI, paralelas. Pela adição: 2 × a primeira + a segunda dá 0 = 0 (ou 0 = 9 com o 5).
#   Erro 3 usa o "nós fazemos" com o 5 (já resolvido): esquerda múltipla, direita não → não é "a mesma reta".
# QUESTÃO 6 (eu faço; texto idêntico ao material): esquerda de s = dobro da de r; direita 2 · 4 = 8 ≠ 10; razões
#   1/2 = 2/4 ≠ 4/10 → paralelas distintas, sem solução (E). Adição: s − 2r → 0 = 2. Erradas (material): B valeria com 8 no
#   lado direito; A e C ignoram a mesma inclinação; D falha no teste direto (0 + 0 ≠ 4). "Perpendiculares" definido na hora
#   (cruzam formando um canto reto, como um L) — definição nossa.
# QUESTÃO 3 (você faz; texto idêntico): fator 2 (4 = 2 · 2 e 10 = 2 · 5) → k = 2 · 3 = 6 (A). Erradas (material): E descreve
#   os casos de solução única; B troca o sinal; C copia o 3 sem multiplicar; D multiplica por 4. Com −6, 3 ou 12: concorrentes.
# Determinante: só citado em uma frase (série de Determinantes e sistemas lineares); sem cálculo e sem Cramer.
# Atalhos (verde): ACHE O FATOR (divida um número da segunda pelo correspondente da primeira e teste nos outros; o lado
#   direito por último) · no parâmetro, o fator vem do PAR COMPLETO (x e lado direito), depois multiplique.
# Frases-chave (meio e fim, idênticas): 1. Concorrentes: uma solução. Paralelas: nenhuma. Coincidentes: infinitas.
#   2. 0 = 2 é impossível; 0 = 0 é infinitas. 3. Múltipla só à esquerda, paralelas; múltipla inteira, a mesma reta.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Sistema sem solução? 0 = 2 não é erro de conta | Sistemas Lineares Ep. 3"
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
    "SPD": "ésse-pê-dê",
    "SPI": "ésse-pê-í",
    "SI": "ésse-í",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Você resolve um sistema, [p=0.2] as letras somem [p=0.2] e sobra *zero igual a dois.* [p=0.5] {b}A maioria "
        "*apaga tudo* [p=0.2] achando que errou a conta. [p=0.5] {c}Não errou: [p=0.3] a conta acabou de dizer [p=0.2] "
        "que *não existe resposta.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai dizer se um sistema tem *uma,* [p=0.2] *nenhuma* [p=0.2] ou *infinitas* soluções, "
        "[p=0.3] {b}muitas vezes *sem resolver nada.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] no *método da adição,* [p=0.2] você "
        "multiplica uma equação inteira [p=0.2] e soma ou subtrai, [p=0.2] para uma letra *sumir.* [p=0.4] {b}Da série de "
        "Equações do primeiro grau: [p=0.2] os fretes *quarenta mais três x* [p=0.2] e *três x mais trinta e seis* [p=0.2] "
        "nunca empatam. [p=0.3] A conta dava *zero x igual a menos quatro.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe três cenas da rua. [p=0.3] {a}Dois *trilhos de trem:* [p=0.2] correm lado a lado [p=0.2] e *nunca* se "
        "encontram. [p=0.4] {b}Um *cruzamento* de duas ruas: [p=0.2] elas têm *um único ponto* em comum. [p=0.4] {c}E uma "
        "rua desenhada *duas vezes* no mapa, [p=0.2] uma em cima da outra: [p=0.2] *todos* os pontos em comum."),
    dict(id="05", block="estrada", text=
        "{t}O que isso tem a ver com sistema? [p=0.4] {a}A equação *x mais y igual a cinco* [p=0.2] tem muitas soluções: "
        "[p=0.2] zero e cinco, [p=0.2] um e quatro, [p=0.2] dois e três. [p=0.4] {b}Marcando todas no plano, [p=0.2] elas "
        "formam uma *reta.* [p=0.3] Cada equação é uma *estrada de soluções.* [p=0.4] {c}E a solução do sistema [p=0.2] é o "
        "ponto que está nas *duas* estradas: [p=0.2] o *cruzamento.*"),

    # ================= BLOCO A: AS TRÊS POSIÇÕES =================
    dict(id="06", block="concorrentes", text=
        "{t}Primeira posição. [p=0.3] {a}*x mais y igual a cinco* [p=0.2] e *x menos y igual a menos um.* [p=0.4] {b}Somando "
        "as duas, [p=0.2] o y some: [p=0.2] dois x igual a quatro, [p=0.2] *x igual a dois* [p=0.2] e *y igual a três.* "
        "[p=0.4] {c}As retas se cruzam *uma vez,* [p=0.2] no ponto dois, três. [p=0.3] São retas *concorrentes:* [p=0.2] "
        "que se cruzam num único ponto. [p=0.4] {d}E o sistema se chama *possível e determinado,* [p=0.2] o SPD: [p=0.2] "
        "tem *uma única* solução."),
    dict(id="07", block="paralelas", text=
        "{t}Segunda posição. [p=0.3] {a}*x mais dois y igual a quatro* [p=0.2] e *dois x mais quatro y igual a dez.* "
        "[p=0.4] {b}Multiplique a primeira por dois: [p=0.2] dois x mais quatro y [p=0.2] igual a *oito.* [p=0.3] Agora "
        "subtraia da segunda: [p=0.2] o x some, [p=0.2] o y some, [p=0.2] e sobra *zero igual a dois.* [p=0.4] {c}É a conta "
        "dizendo: [p=0.2] *esses trilhos nunca se encontram.* [p=0.3] São retas *paralelas:* [p=0.2] lado a lado, sem "
        "ponto comum. [p=0.4] {d}O sistema é *impossível,* [p=0.2] o SI: [p=0.2] *nenhuma* solução."),
    dict(id="08", block="coincidentes", text=
        "{t}Terceira posição. [p=0.3] {a}*x mais dois y igual a quatro* [p=0.2] e *dois x mais quatro y igual a oito.* "
        "[p=0.4] {b}O mesmo passo: [p=0.2] dobro da primeira, [p=0.2] menos a segunda. [p=0.2] Sobra *zero igual a zero.* "
        "[p=0.4] {c}É a conta dizendo: [p=0.2] *é a mesma estrada desenhada duas vezes.* [p=0.3] Quatro e zero, [p=0.2] dois "
        "e um, [p=0.2] zero e dois: [p=0.2] tudo serve nas duas. [p=0.3] São retas *coincidentes.* [p=0.4] {d}O sistema é "
        "*possível e indeterminado,* [p=0.2] o SPI: [p=0.2] *infinitas* soluções."),
    dict(id="09", block="painel", text=
        "{t}Lado a lado. [p=0.3] {a}*Concorrentes:* [p=0.2] um cruzamento, [p=0.2] uma solução. [p=0.4] {b}*Paralelas:* "
        "[p=0.2] zero igual a dois, [p=0.2] nenhuma. [p=0.4] {c}*Coincidentes:* [p=0.2] zero igual a zero, [p=0.2] infinitas. "
        "[p=0.4] {d}Não existe quarta posição: [p=0.2] duas retas [p=0.2] *só* podem fazer isso."),

    # ================= BLOCO B: PREÇOS =================
    dict(id="10", block="precos", text=
        "{t}E onde isso aparece na prova? [p=0.4] {a}Nos *preços.* [p=0.2] Lembra dos fretes? [p=0.2] Os dois cobravam *três "
        "reais* por quilômetro, [p=0.2] com taxas diferentes. [p=0.4] {b}Mesmo preço por unidade: [p=0.2] as retas sobem "
        "*juntas,* [p=0.2] como trilhos. [p=0.3] Uma fica sempre quatro reais acima. [p=0.4] {c}Por isso a pergunta [p=0.2] "
        "*quando custam o mesmo?* [p=0.2] não tem resposta. [p=0.2] O zero x igual a menos quatro [p=0.2] era um *zero igual a "
        "dois* disfarçado."),

    # ================= BLOCO C: AS RAZÕES =================
    dict(id="11", block="razoes", text=
        "{t}Dá para saber a posição *sem resolver?* [p=0.4] {a}Dá. [p=0.2] Escreva cada equação no formato *a x mais b y "
        "igual a c.* [p=0.3] O a, o b e o c são os *coeficientes:* [p=0.2] os números de cada lugar. [p=0.4] {b}Agora divida "
        "cada número da primeira [p=0.2] pelo número do *mesmo lugar* na segunda. [p=0.2] É a *razão entre coeficientes.* "
        "[p=0.4] {c}Três razões, [p=0.2] em três caixinhas: [p=0.2] a com a, [p=0.2] b com b, [p=0.2] c com c."),
    dict(id="12", block="regra", text=
        "{t}E o que as caixinhas dizem? [p=0.4] {a}Se a razão do a é *diferente* da do b: [p=0.2] concorrentes, [p=0.2] *SPD.* "
        "[p=0.2] No primeiro exemplo, [p=0.2] um e menos um. [p=0.4] {b}Se a e b são *iguais,* [p=0.2] mas o c é diferente: "
        "[p=0.2] paralelas, [p=0.2] *SI.* [p=0.2] Um meio, dois quartos, [p=0.2] mas quatro décimos. [p=0.4] {c}Se as *três* "
        "são iguais: [p=0.2] a mesma reta, [p=0.2] *SPI.* [p=0.2] Um meio, dois quartos, quatro oitavos."),

    # ================= BLOCO D: EM PALAVRAS (ATALHO) =================
    dict(id="13", block="palavras", text=
        "{t}Sem frações, [p=0.2] em palavras. [p=0.4] {a}Se a segunda é *múltipla* da primeira [p=0.2] *só do lado "
        "esquerdo:* [p=0.2] paralelas. [p=0.4] {b}Se é múltipla *inteira,* [p=0.2] lado direito junto: [p=0.2] a *mesma "
        "reta.* [p=0.4] {c}O atalho: [p=0.2] *ache o fator.* [p=0.2] Divida um número da segunda pelo da primeira, "
        "[p=0.2] e teste esse fator nos outros. [p=0.3] {d}O lado direito, [p=0.2] *por último:* [p=0.2] é ele que separa "
        "paralelas de coincidentes."),

    # ================= BLOCO E: PARÂMETRO =================
    dict(id="14", block="parametro", text=
        "{t}E quando o sistema traz uma *letra a mais?* [p=0.4] {a}*Três x mais dois y igual a sete* [p=0.2] e *seis x mais "
        "k y igual a catorze.* [p=0.3] O k é um *parâmetro:* [p=0.2] um número que a questão deixou para você escolher. "
        "[p=0.4] {b}Para quanto k há *infinitas* soluções? [p=0.3] Ache o fator no par *completo:* [p=0.2] seis é o dobro de "
        "três, [p=0.2] catorze é o dobro de sete. [p=0.2] Fator *dois.* [p=0.4] {c}Então k é o dobro de dois: [p=0.2] *k igual "
        "a quatro.* [p=0.4] {d}Com *qualquer outro* k, [p=0.2] a razão do b muda: [p=0.2] *uma única* solução."),
    dict(id="15", block="determinante", text=
        "{a}Você pode ouvir falar de um tal de *determinante* [p=0.2] para fazer essa mesma classificação. [p=0.3] {b}Isso "
        "tem série própria: [p=0.2] *Determinantes e sistemas lineares.* [p=0.3] {c}Aqui, [p=0.2] as razões resolvem."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Classifique: [p=0.2] *x menos três y igual a dois* [p=0.2] e *menos dois x mais seis y igual "
        "a menos quatro.* [p=0.4] {b}E se o lado direito da segunda fosse *cinco?* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}As três razões: [p=0.2] um sobre menos dois, [p=0.2] menos três sobre seis, [p=0.2] dois "
        "sobre menos quatro. [p=0.2] Todas valem *menos um meio.* [p=0.4] {b}Três iguais: [p=0.2] a mesma reta, [p=0.2] *SPI,* "
        "coincidentes. [p=0.2] O fator é *menos dois,* [p=0.2] e vale até no lado direito. [p=0.4] {c}Com o cinco, [p=0.2] a "
        "última razão vira *dois quintos,* [p=0.2] diferente de menos um meio. [p=0.3] Múltipla só à esquerda: [p=0.2] "
        "*paralelas,* SI."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] concorrentes: uma solução. [p=0.2] Paralelas: nenhuma. "
        "[p=0.2] Coincidentes: infinitas. [p=0.5] {b}Dois: [p=0.2] zero igual a dois é impossível; [p=0.2] zero igual a zero "
        "é infinitas. [p=0.5] {c}Três: [p=0.2] múltipla só à esquerda, paralelas; [p=0.2] múltipla inteira, a mesma reta."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] sobra *zero igual a dois,* [p=0.2] e a pessoa pensa "
        "*errei a conta.* [p=0.4] {b}Parece certo, [p=0.2] porque zero nunca é igual a dois. [p=0.4] {c}Mas o absurdo é a "
        "*resposta:* [p=0.2] não existe par que sirva nas duas. [p=0.2] Sistema *impossível.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] sobra *zero igual a zero,* [p=0.2] e a pessoa marca *solução zero:* [p=0.2] x igual a zero, "
        "y igual a zero. [p=0.4] {b}Parece certo, [p=0.2] porque só aparece o zero na tela. [p=0.4] {c}Mas zero igual a zero "
        "é *sempre* verdade: [p=0.2] qualquer ponto da estrada serve. [p=0.2] São *infinitas* soluções."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] ver que a esquerda é múltipla [p=0.2] e já dizer *mesma reta.* [p=0.2] Como em x menos três y "
        "igual a dois [p=0.2] e menos dois x mais seis y igual a cinco. [p=0.4] {b}Parece certo, [p=0.2] porque os números "
        "das letras batem. [p=0.4] {c}Mas faltou o lado direito: [p=0.2] dois vezes menos dois daria menos quatro, [p=0.2] "
        "*não cinco.* [p=0.2] São *paralelas.*"),

    # ================= QUESTÃO 6 (EU FAÇO) =================
    dict(id="22", block="q6", text=
        "{t}Questão do ENEM, [p=0.2] do nosso material. [p=0.2] Eu resolvo. [p=0.4] {a}Um estudante representou no plano "
        "cartesiano [p=0.2] as retas *r: x mais dois y igual a quatro* [p=0.2] e *s: dois x mais quatro y igual a dez,* "
        "[p=0.2] para resolver graficamente o sistema formado por elas. [p=0.3] Ele deve concluir que as retas são: [p=0.4] "
        "{qa}A: concorrentes, [p=0.2] e o sistema tem uma única solução. [p=0.2] {qb}B: coincidentes, [p=0.2] e o sistema "
        "tem infinitas soluções. [p=0.2] {qc}C: perpendiculares, [p=0.2] e o sistema tem uma única solução. [p=0.2] {qd}D: "
        "concorrentes na origem, [p=0.2] e a solução é zero, zero. [p=0.2] {qe}E: paralelas distintas, [p=0.2] e o sistema "
        "não tem solução. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q6", text=
        "{t}É o par do começo, [p=0.2] agora com cara de prova. [p=0.4] {a}As razões: [p=0.2] um sobre dois, [p=0.2] dois "
        "sobre quatro, [p=0.2] quatro sobre dez. [p=0.2] As duas primeiras valem *um meio;* [p=0.2] a terceira, *dois "
        "quintos.* [p=0.4] {b}Em palavras: [p=0.2] a esquerda de s é o dobro da de r, [p=0.2] mas o dobro de quatro é oito, "
        "[p=0.2] *não dez.* [p=0.4] {c}Pela adição, [p=0.2] s menos duas vezes r [p=0.2] dá *zero igual a dois.* [p=0.3] "
        "Paralelas distintas, [p=0.2] sem solução. [p=0.3] {ok}*Letra E!*"),
    dict(id="24", block="q6", text=
        "{t}E as erradas? [p=0.3] {xb}A B valeria [p=0.2] se o lado direito de s fosse *oito.* [p=0.4] {xa}A A e a C "
        "ignoram que as duas retas têm a *mesma inclinação:* [p=0.2] sobem juntas, [p=0.2] e não se cruzam. [p=0.3] "
        "{xc}*Perpendicular* é cruzar formando um canto reto, [p=0.2] como um L. [p=0.4] {xd}E a D falha no teste direto: "
        "[p=0.2] zero mais zero [p=0.2] não dá quatro."),

    # ================= QUESTÃO 3 (VOCÊ FAZ) =================
    dict(id="25", block="q3", text=
        "{t}Agora é com você. [p=0.4] {a}Um aplicativo resolve sistemas lineares [p=0.2] e informa quando há infinitas "
        "soluções. [p=0.3] Um usuário digitou o sistema formado por [p=0.2] *dois x mais três y igual a cinco* [p=0.2] e "
        "*quatro x mais k y igual a dez* [p=0.2] e recebeu a mensagem: [p=0.2] *infinitas soluções.* [p=0.3] O valor de k "
        "digitado foi: [p=0.4] {qa}A: seis. [p=0.2] {qb}B: menos seis. [p=0.2] {qc}C: três. [p=0.2] {qd}D: doze. [p=0.2] "
        "{qe}E: qualquer valor diferente de seis. [p=0.4] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{t}*Infinitas soluções:* [p=0.2] múltipla *inteira.* [p=0.4] {a}O fator vem do par completo: [p=0.2] quatro é o "
        "dobro de dois, [p=0.2] dez é o dobro de cinco. [p=0.2] Fator *dois.* [p=0.4] {b}Então k é o dobro de três: [p=0.2] "
        "*k igual a seis.* [p=0.3] As razões ficam um meio, [p=0.2] um meio, [p=0.2] um meio. [p=0.3] {ok}*Letra A!*"),
    dict(id="27", block="q3", text=
        "{t}E as erradas? [p=0.3] {xe}A E descreve justamente os casos de *uma única* solução. [p=0.4] {xb}A B *troca o "
        "sinal.* [p=0.3] {xc}A C *copia* o três sem multiplicar. [p=0.3] {xd}E a D multiplica por *quatro.* [p=0.4] Com "
        "menos seis, três ou doze, [p=0.2] as retas são *concorrentes.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] concorrentes: uma solução. [p=0.2] Paralelas: nenhuma. "
        "[p=0.2] Coincidentes: infinitas. [p=0.5] {b}Dois: [p=0.2] zero igual a dois é impossível; [p=0.2] zero igual a zero "
        "é infinitas. [p=0.5] {c}Três: [p=0.2] múltipla só à esquerda, paralelas; [p=0.2] múltipla inteira, a mesma reta."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Ana e Beto pesam *cento e vinte e cinco quilos* juntos; [p=0.3] {b}Beto e Caio, *cento e quarenta e cinco;* "
        "[p=0.3] {c}Ana e Caio, *cento e quarenta.* [p=0.3] {d}Quanto pesa o Beto? [p=0.4] {e}Três incógnitas, [p=0.2] e um "
        "atalho que resolve em *duas linhas.* [p=0.3] Próximo episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já apagou uma conta que deu zero igual a dois? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
