# Roteiro — Determinantes e Sistemas Lineares, Episódio 4 de 5: uma, infinitas ou nenhuma (classificar e discutir
#   pelo determinante)
# Base: Estudos/Enem/estudos/01-matematica/34-determinantes-sistemas-lineares.html — seções 08 e 09 + Questões 4, 7 e 9
#   (seção 12). A Questão 5 do material NÃO é usada (quase igual a uma questão da série de Sistemas).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na revisão):
#   o SEMÁFORO: D ≠ 0 é sinal verde (uma solução só, e pronto); D = 0 é sinal amarelo (pare e olhe as equações).
#   com D = 0, as equações são GÊMEAS (uma é múltipla inteira da outra: infinitas) ou BRIGADAS (múltiplas só no lado
#   esquerdo: nenhuma).
#   o homogêneo tem a PORTA (0, 0) sempre aberta: nunca é impossível.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Revisão das retas (série 22) em ~25 s, na cena 03.
# Exemplos NOSSOS (o recorte não traz conta para eles; nenhum repete as Q4, Q7 e Q9):
#   bloco b: gêmeas x + 2y = 3 / 2x + 4y = 6 e brigadas 2x + 4y = 7 (são os da seção 08, como o prompt pede);
#     D_x das brigadas = 3·4 − 2·7 = −2 ≠ 0 → SI; nas gêmeas D_x = 3·4 − 2·6 = 0 e D_y = 1·6 − 3·2 = 0.
#   bloco c (exemplo NOVO do prompt): x + 3y = 2 e 3x + ky = m → D = k − 9; k = 9 → triplo; m = 6 SPI, m ≠ 6 SI.
#   bloco d (3 × 3 com parâmetro, nosso): x + y + z = 3; x + 2y + z = 4; 2x + 3y + kz = 7 → D = k − 2;
#     k = 2: L2 − L1 → y = 1; L3 − 2L1 → y = 1; subtraindo → 0 = 0 (redundante, SPI).
#     Se o 7 fosse 9: L3 − 2L1 → y = 3; com y = 1 → 0 = 2 (SI).
#   bloco e (homogêneo, nosso): x + 2y = 0 e 3x + 5y = 0 → D = −1 ≠ 0 → só (0, 0);
#     2x − y = 0 e 6x − 3y = 0 → D = 0 → infinitas, por exemplo (1, 2).
#   erro 2: nas gêmeas, (1, 1) é solução e (3, 0) também → achar uma não prova que é única.
#   erro 4 (k² = 4 ⟹ só k = 2): mantido como o prompt pede; é a mesma conta da Q7, que é "nós fazemos" e vem depois.
# Nós fazemos (prompt): 2x − y = 1 e 4x − 2y = 5 → D = 2·(−2) − (−1)·4 = 0; o dobro da 1ª daria 2, não 5: SI;
#   D_x = 1·(−2) − (−1)·5 = 3 ≠ 0.
# QUESTÃO 4 (eu faço): x + 2y = 3 e 2x + ky = m → D = k − 4; k = 4 → dobro; compatível só com m = 6 → A (k = 4 e m ≠ 6).
#   Erradas como o material: B é o caso SPI; C é o caso SPD; D soma no determinante (k + 4 = 0 → k = −4);
#   E copia os números da 1ª equação (k = 2, m = 3), como se a 2ª tivesse de ser idêntica — esquece que basta a proporção.
# QUESTÃO 7 (nós fazemos): x + ky = 0 e kx + 4y = 0 → D = 4 − k² = 0 → k = 2 ou k = −2 → E; com k = 2, (2, −1).
#   Erradas como o material: A esquece o quadrado (4 − k = 0); B esquece a raiz negativa; C dá D = 4 (só trivial);
#   D resolve k² = 16.
# QUESTÃO 9 (você faz, com pausa): 1ª + 2ª = 3ª (redundante); D = 1(−3 − 0) − 1(3 − 4) + 1(0 + 2) = 0 por Laplace;
#   há solução e não é única → B (SPI); outra solução (−0,5; 2,5; 4). O GANCHO do usuário já diz "infinitas soluções";
#   mantido igual. Na Q9, o que é novo é a justificativa (equação redundante, D = 0) e as alternativas erradas.
#   Erradas como o material: A conclui unicidade; C confunde D = 0 com impossível; D não satisfaz a 1ª (0 ≠ 6);
#   E diz que repetição gera impossibilidade.
# Frases-chave (meio e fim, idênticas): 1. D diferente de zero: uma solução só. 2. D igual a zero: gêmeas dão
#   infinitas, brigadas dão nenhuma. 3. Homogêneo nunca é impossível.
# Contas conferidas em Python: trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Uma, infinitas ou nenhuma: classificar sistemas pelo determinante | Determinantes Ep. 4"
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
        "{a}Um estudante achou o terno [p=0.2] *um, dois, três* [p=0.2] num sistema três por três [p=0.2] e cravou: "
        "[p=0.2] *solução única.* [p=0.5] {b}Errou: [p=0.2] o sistema tem *infinitas soluções.* [p=0.5] {c}E o "
        "determinante *avisava.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai *classificar qualquer sistema pelo determinante,* [p=0.2] sem resolver, [p=0.3] "
        "{b}e *discutir um sistema* [p=0.2] com letras no lugar dos números."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes. [p=0.3] {a}Da série de Sistemas: [p=0.2] retas que se *cruzam,* [p=0.2] uma solução; "
        "[p=0.2] *paralelas,* [p=0.2] nenhuma; [p=0.2] *coincidentes,* [p=0.2] infinitas. [p=0.4] {b}Do episódio um: "
        "[p=0.2] dois por dois é *a d menos b c.* [p=0.4] {c}E do segundo grau: [p=0.2] *k ao quadrado igual a quatro* "
        "[p=0.2] tem *duas* raízes, [p=0.2] dois e menos dois."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine um técnico [p=0.2] numa máquina de misturas [p=0.2] com *dois botões,* [p=0.2] *k* e *m.* [p=0.4] "
        "{a}Cada posição muda as equações da mistura. [p=0.4] {b}Em que posições [p=0.2] o problema tem *uma "
        "resposta,* [p=0.2] *várias,* [p=0.2] ou *nenhuma?* [p=0.4] {c}Ele não precisa resolver nada. [p=0.2] Basta "
        "*um número:* [p=0.2] o determinante."),

    # ================= BLOCO A: A TABELA =================
    dict(id="05", block="tabela", text=
        "{t}Quantas respostas um sistema pode ter? [p=0.4] {a}*Uma só:* [p=0.2] *possível e determinado,* [p=0.2] o "
        "*esse pê dê.* [p=0.4] {b}*Infinitas:* [p=0.2] *possível e indeterminado,* [p=0.2] o *esse pê i.* [p=0.4] "
        "{c}*Nenhuma:* [p=0.2] *impossível,* [p=0.2] o *esse i.* [p=0.4] {d}E quem decide primeiro [p=0.2] é o *dê,* "
        "[p=0.2] o determinante."),
    dict(id="06", block="tabela", text=
        "{t}Como o dê decide? [p=0.4] {a}Pense num *semáforo.* [p=0.2] Dê *diferente de zero* [p=0.2] é *sinal verde:* "
        "[p=0.2] uma solução só, [p=0.2] e pronto. [p=0.4] {b}Dê *igual a zero* [p=0.2] é *sinal amarelo:* [p=0.2] "
        "*pare e olhe as equações.* [p=0.4] {c}Paralelas e coincidentes [p=0.2] têm a *mesma inclinação,* [p=0.2] e é "
        "isso que zera o dê."),

    # ================= BLOCO B: D = 0 NÃO É IMPOSSÍVEL =================
    dict(id="07", block="gemeas", text=
        "{t}Então dê zero quer dizer impossível? [p=0.4] {a}Olhe: [p=0.2] *x mais dois y igual a três,* [p=0.2] e "
        "*dois x mais quatro y igual a seis.* [p=0.2] A segunda é o *dobro* da primeira, [p=0.2] inteirinha. [p=0.4] "
        "{b}São *gêmeas:* [p=0.2] a mesma reta, [p=0.2] equações *compatíveis.* [p=0.2] Infinitas soluções. [p=0.4] "
        "{c}Troque o seis por *sete.* [p=0.2] O dobro daria seis, [p=0.2] não sete. [p=0.4] {d}São *brigadas:* [p=0.2] "
        "paralelas, [p=0.2] equações *contraditórias.* [p=0.2] Nenhuma solução."),
    dict(id="08", block="gemeas", text=
        "{t}E com conta? [p=0.4] {a}Use o *dê x* do episódio três: [p=0.2] a coluna do x [p=0.2] trocada pelos termos "
        "independentes. [p=0.4] {b}Nas brigadas: [p=0.2] três vezes quatro, [p=0.2] menos dois vezes sete: [p=0.2] "
        "*menos dois.* [p=0.4] {c}Em dois por dois: [p=0.2] *dê zero* e *dê x ou dê y diferente de zero:* [p=0.2] "
        "*impossível.* [p=0.4] {d}Nas gêmeas, [p=0.2] os dois dão zero: [p=0.2] compare as equações [p=0.2] antes de "
        "concluir."),
    dict(id="09", block="gemeas", text=
        "{t}Um atalho sem essas contas. [p=0.4] {a}Ache o *fator* do lado esquerdo: [p=0.2] aqui, [p=0.2] *vezes "
        "dois.* [p=0.4] {b}Aplique no lado direito: [p=0.2] três vezes dois, [p=0.2] *seis.* [p=0.4] {c}Bateu: [p=0.2] "
        "*gêmeas.* [p=0.2] Não bateu: [p=0.2] *brigadas.*"),

    # ================= BLOCO C: DISCUSSÃO COM PARÂMETRO =================
    dict(id="10", block="parametro", text=
        "{t}E quando aparece uma *letra* no lugar de um número? [p=0.4] {a}Ela é um *parâmetro:* [p=0.2] um número "
        "ajustável, [p=0.2] como os botões da máquina. [p=0.4] {b}*Discutir o sistema* [p=0.2] é dizer, [p=0.2] para "
        "cada valor, [p=0.2] se ele é esse pê dê, [p=0.2] esse pê i [p=0.2] ou esse i. [p=0.4] {c}Exemplo: [p=0.2] *x "
        "mais três y igual a dois,* [p=0.2] e *três x mais k y igual a m.*"),
    dict(id="11", block="parametro", text=
        "{t}Passo um: [p=0.2] o dê. [p=0.4] {a}Um vezes k, [p=0.2] menos três vezes três: [p=0.2] *k menos nove.* "
        "[p=0.4] {b}Se *k é diferente de nove,* [p=0.2] sinal verde: [p=0.2] *esse pê dê,* [p=0.2] seja qual for o "
        "*m.* [p=0.4] {c}O *m* só importa [p=0.2] no sinal amarelo."),
    dict(id="12", block="parametro", text=
        "{t}Passo dois: [p=0.2] *k igual a nove.* [p=0.4] {a}A segunda vira [p=0.2] *três x mais nove y igual a m:* "
        "[p=0.2] o lado esquerdo é o *triplo* da primeira. [p=0.4] {b}O triplo do dois é *seis.* [p=0.2] Com *m igual "
        "a seis,* [p=0.2] gêmeas: [p=0.2] *esse pê i.* [p=0.4] {c}Com *m diferente de seis,* [p=0.2] brigadas: [p=0.2] "
        "*esse i.* [p=0.4] {d}E o resumo vai numa tabela: [p=0.2] condição, [p=0.2] classificação."),
    dict(id="13", block="parametro", text=
        "{t}Atalho de toda discussão. [p=0.4] {a}*Primeiro,* [p=0.2] ache o valor que *zera* o dê: [p=0.2] o resto é "
        "esse pê dê. [p=0.4] {b}*Só depois,* [p=0.2] nesse valor, [p=0.2] compare o lado direito. [p=0.4] {c}Duas "
        "perguntas, [p=0.2] nessa ordem."),

    # ================= BLOCO D: 3 × 3 E ESCALONAMENTO =================
    dict(id="14", block="escalona", text=
        "{t}E em três por três? [p=0.4] {a}*x mais y mais z igual a três;* [p=0.2] *x mais dois y mais z igual a "
        "quatro;* [p=0.2] *dois x mais três y mais k z igual a sete.* [p=0.4] {b}Por Laplace, [p=0.2] o dê dá *k menos "
        "dois.* [p=0.2] Com k diferente de dois: [p=0.2] esse pê dê. [p=0.4] {c}Com *k igual a dois,* [p=0.2] sinal "
        "amarelo: [p=0.2] hora de *escalonar.*"),
    dict(id="15", block="escalona", text=
        "{t}Escalonar é *zerar* a primeira incógnita [p=0.2] nas equações de baixo, [p=0.2] formando uma *escada.* "
        "[p=0.4] {a}Segunda menos primeira: [p=0.2] *y igual a um.* [p=0.4] {b}Terceira menos duas vezes a primeira: "
        "[p=0.2] *y igual a um* de novo. [p=0.4] {c}Subtraindo as duas: [p=0.2] *zero igual a zero.* [p=0.4] {d}Uma "
        "*equação redundante:* [p=0.2] não traz informação nova. [p=0.2] Sem contradição: [p=0.2] *esse pê i.*"),
    dict(id="16", block="escalona", text=
        "{t}E se o sete fosse *nove?* [p=0.4] {a}A terceira menos duas vezes a primeira [p=0.2] dá *y igual a três.* "
        "[p=0.4] {b}Com o *y igual a um* de cima: [p=0.2] *zero igual a dois.* [p=0.4] {c}*Contradição:* [p=0.2] *esse "
        "i.*"),

    # ================= BLOCO E: HOMOGÊNEO =================
    dict(id="17", block="homogeneo", text=
        "{t}E se todo o lado direito for *zero?* [p=0.4] {a}É o *sistema homogêneo.* [p=0.4] {b}Nele, [p=0.2] x e y "
        "iguais a zero [p=0.2] *sempre* funcionam: [p=0.2] a *solução trivial.* [p=0.2] A *porta zero, zero* [p=0.2] "
        "está sempre aberta. [p=0.4] {c}Por isso, [p=0.2] ele *nunca é impossível.* [p=0.4] {d}E tem *outras* soluções "
        "[p=0.2] exatamente quando *dê é zero.*"),
    dict(id="18", block="homogeneo", text=
        "{t}Dois exemplos. [p=0.4] {a}*X mais dois y igual a zero* [p=0.2] e *três x mais cinco y igual a zero:* "
        "[p=0.2] dê é cinco menos seis, [p=0.2] *menos um.* [p=0.2] Só a porta zero, zero. [p=0.4] {b}*Dois x menos y "
        "igual a zero* [p=0.2] e *seis x menos três y igual a zero:* [p=0.2] dê *zero.* [p=0.4] {c}Há outras soluções, "
        "[p=0.2] como *um, dois.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Classifique o sistema: [p=0.2] *dois x menos y igual a um,* [p=0.2] e *quatro x menos "
        "dois y igual a cinco.* [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Dê: [p=0.2] menos quatro, [p=0.2] menos o menos quatro: [p=0.2] *zero.* [p=0.2] "
        "Sinal amarelo. [p=0.4] {b}O fator é *dois.* [p=0.2] O dobro do um daria *dois,* [p=0.2] não cinco. [p=0.2] "
        "*Brigadas:* [p=0.2] *esse i.* [p=0.4] {c}Confirmando: [p=0.2] dê x [p=0.2] é menos dois mais cinco, [p=0.2] "
        "*três.* [p=0.2] Diferente de zero: [p=0.2] impossível mesmo."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] Dê diferente de zero: [p=0.2] uma solução só. [p=0.5] "
        "{b}Dois: [p=0.2] Dê igual a zero: [p=0.2] gêmeas dão infinitas, [p=0.2] brigadas dão nenhuma. [p=0.5] {c}Três: "
        "[p=0.2] homogêneo nunca é impossível."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *dê zero, [p=0.2] logo impossível.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque zero lembra *nada.* [p=0.4] {c}Mas zero é só o *sinal amarelo:* [p=0.2] as "
        "gêmeas têm dê zero [p=0.2] e *infinitas* soluções."),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] *achei uma solução, [p=0.2] então é esse pê dê.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "a conta fechou. [p=0.4] {c}Mas nas gêmeas, [p=0.2] *um, um* [p=0.2] é solução, [p=0.2] e *três, zero* [p=0.2] "
        "também. [p=0.2] Achar uma [p=0.2] não prova que é *a única.* [p=0.2] Quem decide é o dê."),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] *homogêneo pode ser impossível.* [p=0.4] {b}Parece certo, [p=0.2] porque todo sistema "
        "parece poder brigar. [p=0.4] {c}Mas o *zero, zero* [p=0.2] sempre serve. [p=0.2] A porta está *sempre aberta.*"),
    dict(id="25", block="erros", text=
        "{a}Quarto: [p=0.2] *k ao quadrado igual a quatro, [p=0.2] então k igual a dois,* [p=0.2] e só. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque o dois vem primeiro na cabeça. [p=0.4] {c}Mas menos dois ao quadrado [p=0.2] "
        "também dá quatro: [p=0.2] *dois e menos dois.*"),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="26", block="q4", text=
        "{t}Agora, questões do material de estudo. [p=0.2] Esta, [p=0.2] *eu faço.* "
        "[p=0.4] {a}Um técnico descreve uma mistura pelo sistema [p=0.2] *x mais dois y igual a três,* [p=0.2] e *dois "
        "x mais k y igual a m,* [p=0.2] em que k e m são constantes reais ajustáveis. [p=0.2] O sistema *não tem "
        "solução* exatamente quando: [p=0.4] {qa}A: [p=0.2] k igual a quatro e m diferente de seis. [p=0.3] {qb}B: "
        "[p=0.2] k igual a quatro e m igual a seis. [p=0.3] {qc}C: [p=0.2] k diferente de quatro, [p=0.2] para qualquer "
        "m. [p=0.3] {qd}D: [p=0.2] k igual a menos quatro e m diferente de seis. [p=0.3] {qe}E: [p=0.2] k igual a dois "
        "e m diferente de três."),
    dict(id="27", block="q4", text=
        "{t}Passo um: [p=0.2] o dê. [p=0.4] {a}Um vezes k, [p=0.2] menos dois vezes dois: [p=0.2] *k menos quatro.* "
        "[p=0.2] Com k diferente de quatro, [p=0.2] sinal verde: [p=0.2] tem solução. [p=0.4] {b}Passo dois: [p=0.2] "
        "*k igual a quatro.* [p=0.2] A segunda vira *dois x mais quatro y igual a m:* [p=0.2] o lado esquerdo é o "
        "*dobro* da primeira. [p=0.4] {c}O dobro do três é *seis.* [p=0.2] Para brigarem, [p=0.2] *m diferente de "
        "seis.* [p=0.3] {ok}*Letra A!*"),
    dict(id="28", block="q4", text=
        "{t}E as outras? [p=0.3] {xb}A B [p=0.2] é o caso das *gêmeas:* [p=0.2] infinitas soluções. [p=0.4] {xc}A C "
        "[p=0.2] é o *sinal verde:* [p=0.2] solução única. [p=0.4] {xd}A D [p=0.2] *somou* no determinante: [p=0.2] k "
        "mais quatro igual a zero. [p=0.4] {xe}E a E [p=0.2] copiou os números da primeira equação, [p=0.2] como se a "
        "segunda tivesse de ser *idêntica,* [p=0.2] e esqueceu que basta a *proporção.*"),

    # ================= QUESTÃO 7 (NÓS FAZEMOS) =================
    dict(id="29", block="q7", text=
        "{t}A próxima, [p=0.2] *nós fazemos.* [p=0.4] {a}O sistema [p=0.2] *x mais k y igual a zero* [p=0.2] e *k x "
        "mais quatro y igual a zero,* [p=0.2] com k real, [p=0.2] sempre admite a solução x igual a y igual a zero. "
        "[p=0.2] Ele admite também soluções *diferentes* dessa quando: [p=0.4] {qa}A: [p=0.2] k igual a quatro. [p=0.3] "
        "{qb}B: [p=0.2] k igual a dois, [p=0.2] apenas. [p=0.3] {qc}C: [p=0.2] k igual a zero. [p=0.3] {qd}D: [p=0.2] k "
        "igual a quatro ou k igual a menos quatro. [p=0.3] {qe}E: [p=0.2] k igual a dois ou k igual a menos dois. "
        "[p=0.5] {p}Pense comigo: [p=0.2] que tipo de sistema é esse? [p=1.5]"),
    dict(id="30", block="q7", text=
        "{t}É *homogêneo:* [p=0.2] a porta zero, zero [p=0.2] já está aberta. [p=0.4] {a}Outras soluções [p=0.2] "
        "aparecem quando *dê é zero.* [p=0.2] Um vezes quatro, [p=0.2] menos k vezes k: [p=0.2] *quatro menos k ao "
        "quadrado.* [p=0.4] {b}Igual a zero: [p=0.2] k ao quadrado igual a quatro. [p=0.2] *Duas* raízes: [p=0.2] "
        "*dois e menos dois.* [p=0.4] {c}Com k igual a dois, [p=0.2] *dois, menos um* [p=0.2] serve: [p=0.2] dois mais "
        "dois vezes menos um, [p=0.2] zero. [p=0.3] {ok}*Letra E!*"),
    dict(id="31", block="q7", text=
        "{t}E as outras? [p=0.3] {xa}A A [p=0.2] esqueceu o *quadrado:* [p=0.2] quatro menos k igual a zero. [p=0.4] "
        "{xb}A B [p=0.2] esqueceu a raiz *negativa.* [p=0.4] {xc}A C [p=0.2] dá dê igual a quatro, [p=0.2] diferente de "
        "zero: [p=0.2] só a porta zero, zero. [p=0.4] {xd}E a D [p=0.2] resolveu *k ao quadrado igual a dezesseis.*"),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="32", block="q9", text=
        "{t}E a última [p=0.2] é *sua.* [p=0.2] É a do gancho. [p=0.4] {a}Ao resolver o sistema [p=0.2] *x mais y mais z "
        "igual a seis;* [p=0.2] *x menos y mais dois z igual a cinco;* [p=0.2] *dois x mais três z igual a onze,* "
        "[p=0.2] um estudante verificou que o terno um, dois, três [p=0.2] satisfaz as três equações. [p=0.2] Sobre esse "
        "sistema, [p=0.2] é correto afirmar que ele é: [p=0.4] {qa}A: [p=0.2] possível e determinado, [p=0.2] e um, "
        "dois, três é sua única solução. [p=0.3] {qb}B: [p=0.2] possível e indeterminado. [p=0.3] {qc}C: [p=0.2] "
        "impossível, [p=0.2] porque o determinante dos coeficientes é zero. [p=0.3] {qd}D: [p=0.2] possível e "
        "determinado, [p=0.2] com solução zero, zero, zero. [p=0.3] {qe}E: [p=0.2] impossível, [p=0.2] porque a "
        "terceira equação repete as outras. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="33", block="q9", text=
        "{t}Conferindo. [p=0.3] {a}Some a primeira com a segunda: [p=0.2] *dois x mais três z igual a onze.* [p=0.2] É "
        "a terceira! [p=0.4] {b}Ela é *redundante.* [p=0.2] E o dê, [p=0.2] por Laplace na primeira linha: [p=0.2] "
        "menos três, [p=0.2] mais um, [p=0.2] mais dois: [p=0.2] *zero.* [p=0.4] {c}Tem solução [p=0.2] e não é única: "
        "[p=0.2] *esse pê i.* [p=0.2] Outra: [p=0.2] *menos zero vírgula cinco, [p=0.2] dois vírgula cinco, [p=0.2] "
        "quatro.* [p=0.3] {ok}*Letra B!*"),
    dict(id="34", block="q9", text=
        "{t}E as outras? [p=0.3] {xa}A A [p=0.2] concluiu que é única [p=0.2] só porque *achou uma.* [p=0.4] {xc}A C "
        "[p=0.2] confundiu dê zero com *impossível,* [p=0.2] mas o um, dois, três [p=0.2] prova que há solução. [p=0.4] "
        "{xd}A D [p=0.2] nem satisfaz a primeira: [p=0.2] zero não é seis. [p=0.4] {xe}E a E: [p=0.2] equação repetida "
        "[p=0.2] gera *infinitas* soluções, [p=0.2] não impossibilidade."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="35", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] Dê diferente de zero: [p=0.2] uma solução só. "
        "[p=0.5] {b}Dois: [p=0.2] Dê igual a zero: [p=0.2] gêmeas dão infinitas, [p=0.2] brigadas dão nenhuma. [p=0.5] "
        "{c}Três: [p=0.2] homogêneo nunca é impossível."),

    # ================= PONTE E CTA =================
    dict(id="36", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] *juntamos tudo,* [p=0.2] *caçamos as pegadinhas* [p=0.2] e "
        "treinamos com *questões inéditas.*"),
    dict(id="37", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também achava que dê zero era impossível? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
