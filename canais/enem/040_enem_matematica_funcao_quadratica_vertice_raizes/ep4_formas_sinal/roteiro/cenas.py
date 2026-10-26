# Roteiro — Função Quadrática, Episódio 4 de 5: três formas da mesma função (geral, fatorada, canônica) e estudo do sinal
# Base: Estudos/Enem/estudos/01-matematica/25-funcao-quadratica-vertice-raizes.html — seções 06 e 07 + Questões 4, 6 e 5
#   (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   AS TRÊS FOTOS DA MESMA PESSOA: a geral mostra o c, a fatorada mostra as raízes, a canônica mostra o vértice.
#   PARÁBOLA TRISTE É POSITIVA NO MEIO; PARÁBOLA SORRINDO É NEGATIVA NO MEIO: entre as raízes, o sinal contrário ao de a;
#     fora delas, o mesmo sinal de a (a sorrindo/triste vem do episódio 1).
#   NUNCA DIVIDA POR x: você não sabe se ele é positivo ou negativo, e o sinal da desigualdade pode virar.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Forma fatorada, soma e produto e "nunca divida por x" = REVISÃO (série de Equação do 2º grau); (x − 2)² = x² − 4x + 4
#   (série de Expressões algébricas); sinal da afim (série de Função afim).
# Exemplos do prompt nos blocos: 2x² − 8x + 6 = 2(x − 1)(x − 3) = 2(x − 2)² − 2; arco da ponte (raízes 0 e 40, topo 10 no
#   meio → a = −1/40); x² − 5x + 6 ≤ 0 → 2 ≤ x ≤ 3; x² > 4x → x < 0 ou x > 4. O bloco c repete os dados da Q6, que é
#   "nós fazemos" (o prompt pede para continuar o bloco c na Q6).
# Nós fazemos (prompt): x² − 9 < 0 → raízes −3 e 3, a > 0, negativa entre as raízes: −3 < x < 3; quem "tira a raiz" e
#   escreve x < 3 aceita −5, e (−5)² − 9 = 16 > 0.
# Exemplos NOSSOS nos erros (marcados), para não entregar a Q5 ("você faz") nem a Q4:
#   erro 2: x² − 5x + 6 (do bloco e), teste em 2,5 → −0,25 (negativa entre as raízes);
#   erro 3: L(x) = −x² + 10x − 16 (raízes 2 e 8, topo em 5): cresce até 5, mas L(1) = −7 (prejuízo);
#   erro 4: raízes 2 e 4 cortando o eixo y em 8 → a · (−2)(−4) = 8 → a = 1 (x² − 6x + 8); quem usa a = 8 escreve
#     8x² − 48x + 64, que corta o eixo y em 64.
# Acréscimos NOSSOS (marcados): atalho verde "a pergunta escolhe a foto" (cena 07); atalho verde "ache o a com um ponto que
#   não seja raiz" (cena 09); atalho verde "desenhe a carinha: o sinal de a no lado de fora" (cena 11); atalho verde
#   "confira com um número de cada região" (cena 13).
# QUESTÃO 4 ("eu faço", com pausa): gabarito B (x² − 6x + 5). Erradas = material e prompt (A: raízes −1 e −5;
#   C: raízes certas, corta em −5; D: troca soma e produto, raízes 2 e 3; E: a = 5, corta em 25).
# QUESTÃO 6 ("nós fazemos", com pausa): gabarito B (4,375 m). f(5) = −1/40 · 5 · (−35) = 175/40 = 4,375. Erradas = prompt
#   (A: reta do pé ao topo, 10 · 5/20 = 2,5; D: proporção linear com os 15 m até o centro, 10 · 15/20 = 7,5; E: 5 m do
#   centro, f(15) = 9,375; C: (15/20)² · 10 = 5,625 é o quanto DESCEU do topo; 10 − 5,625 = 4,375).
# QUESTÃO 5 ("você faz", com pausa): gabarito D (entre 400 e 1 000 unidades). Raízes 4 e 10 (soma 14, produto 40);
#   a = −1 < 0, positiva entre as raízes. Erradas = material (C: sinal de a > 0; A e B: só um pedaço da região errada;
#   E: "lucro crescendo", x < 7, com L(2) = −16).
# Frases-chave (meio e fim, idênticas): 1. Geral mostra o c; fatorada, as raízes; canônica, o vértice.
#   2. Entre as raízes, o sinal contrário ao de a. 3. Inequação do 2º grau: passe tudo para um lado e nunca divida por x.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Três formas da função quadrática e estudo do sinal | Função Quadrática Ep. 4"
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
        "{a}Para resolver *x ao quadrado maior que quatro x,* [p=0.3] muita gente divide os dois lados por x [p=0.2] "
        "e responde *x maior que quatro.* [p=0.5] {b}Teste *x igual a menos um:* [p=0.3] um, [p=0.2] maior que menos "
        "quatro. [p=0.3] *Verdade!* [p=0.5] {c}A divisão jogou fora *metade da resposta.* [p=0.4] {d}Hoje você aprende "
        "o jeito que *não perde nada.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o quarto episódio da série de *Função quadrática.* [p=0.4] {a}Ao final, [p=0.2] você vai *escrever a "
        "lei de uma parábola* a partir do gráfico [p=0.3] {b}e dizer para quais x ela é *positiva ou negativa,* "
        "[p=0.3] {c}*sem errar o sentido.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Com raízes x um e x dois, [p=0.2] a função vira *a, [p=0.1] vezes x "
        "menos x um, [p=0.1] vezes x menos x dois,* [p=0.2] e as raízes saem por *soma e produto.* [p=0.4] {b}*x menos "
        "dois, ao quadrado,* [p=0.2] é x ao quadrado, menos quatro x, mais quatro. [p=0.4] {c}E *estudar o sinal* é "
        "achar onde dá *mais* e onde dá *menos.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe o arco de uma *ponte* sobre um rio: [p=0.2] {a}os pés *na água,* [p=0.2] o topo *bem no meio.* "
        "[p=0.4] {b}E pense numa *fábrica* que só lucra numa *faixa* de produção: [p=0.2] pouco ou demais, [p=0.2] "
        "prejuízo. [p=0.4] {c}As duas são *parábolas.* "),

    # ================= BLOCO A: AS TRÊS FORMAS =================
    dict(id="05", block="formas", text=
        "{t}Uma parábola pode ter *três leis?* [p=0.4] {a}Pode. [p=0.2] A *forma geral:* [p=0.2] *a x ao quadrado, "
        "mais b x, mais c.* [p=0.4] {b}A *forma fatorada:* [p=0.2] a lei escrita com as *raízes.* [p=0.4] {c}A *forma "
        "canônica:* [p=0.2] a, vezes x menos x do vértice, ao quadrado, [p=0.1] mais y do vértice. [p=0.2] A lei "
        "escrita com o *vértice.* [p=0.4] {d}São *três fotos da mesma pessoa:* [p=0.2] a geral mostra o *c,* [p=0.2] a "
        "fatorada mostra as *raízes,* [p=0.2] a canônica mostra o *vértice.*"),
    dict(id="06", block="mesma", text=
        "{t}Quer ver? [p=0.3] {a}*Dois x ao quadrado, menos oito x, mais seis:* [p=0.2] corta o eixo y em *seis.* "
        "[p=0.4] {b}A mesma função é *dois, vezes x menos um, vezes x menos três:* [p=0.2] raízes *um e três.* [p=0.4] "
        "{c}E é *dois, vezes x menos dois ao quadrado, menos dois:* [p=0.2] vértice *dois, menos dois.* [p=0.4] "
        "{d}Confira: [p=0.2] desenvolva a canônica com o produto notável [p=0.2] e a geral volta, [p=0.2] com o *mais "
        "seis.*"),
    dict(id="07", block="foto", text=
        "{t}E qual foto usar? [p=0.4] {a}Atalho: [p=0.2] *a pergunta escolhe a foto.* [p=0.4] {b}Pediram onde *corta o "
        "eixo y?* [p=0.2] Geral. [p=0.3] Pediram as *raízes?* [p=0.2] Fatorada. [p=0.3] Pediram o *topo ou o fundo?* "
        "[p=0.2] Canônica. [p=0.4] {c}A conta vira *leitura.*"),

    # ================= BLOCO C: A LEI PELO GRÁFICO =================
    dict(id="08", block="ponte_lei", text=
        "{t}E se você só tem o *desenho?* [p=0.4] {a}O arco da ponte: [p=0.2] pés a *quarenta metros* um do outro, "
        "[p=0.2] topo *dez metros* acima da água. [p=0.4] {b}Com a origem num pé, [p=0.2] as raízes são *zero e "
        "quarenta:* [p=0.2] comece pela *fatorada.* [p=0.2] *f de x igual a a, vezes x, vezes x menos quarenta.* "
        "[p=0.4] {c}O topo, *vinte, dez,* acha o a: [p=0.2] a vezes vinte, vezes menos vinte, igual a dez. [p=0.2] *a "
        "igual a menos um quarenta avos.* [p=0.4] {d}Negativo: [p=0.2] parábola *triste.*"),
    dict(id="09", block="ponte_lei", text=
        "{t}E se o desenho mostrar o *topo?* [p=0.3] {a}Comece pela *canônica:* [p=0.2] o vértice entra direto, "
        "[p=0.2] falta só o a. [p=0.4] {b}Atalho: [p=0.2] *ache o a com um ponto que não seja raiz.* [p=0.2] Na raiz, "
        "o a some da conta."),

    # ================= BLOCO D: ESTUDO DO SINAL =================
    dict(id="10", block="sinal", text=
        "{t}Onde a parábola é *positiva?* [p=0.4] {a}*Estudar o sinal* é dizer para quais x ela dá *positivo,* [p=0.2] "
        "*negativo* [p=0.2] ou *zero.* [p=0.4] {b}Desenhe a parábola sobre a reta dos números: [p=0.2] acima do eixo, "
        "*verde;* [p=0.2] abaixo, *vermelho.* [p=0.4] {c}Com duas raízes: [p=0.2] *entre as raízes, o sinal contrário "
        "ao de a; [p=0.2] fora delas, o mesmo sinal de a.*"),
    dict(id="11", block="carinha", text=
        "{t}Por quê? [p=0.4] {a}*Parábola triste é positiva no meio:* [p=0.2] a barriga sobe acima do eixo. [p=0.4] "
        "{b}*Parábola sorrindo é negativa no meio:* [p=0.2] o fundo desce abaixo do eixo. [p=0.4] {c}Atalho: [p=0.2] "
        "*desenhe a carinha.* [p=0.2] Do lado de fora das raízes, [p=0.2] o sinal é sempre o do a."),
    dict(id="12", block="delta", text=
        "{t}E sem duas raízes? [p=0.3] {a}Com a positivo e *delta zero,* [p=0.2] ela só encosta: [p=0.2] *positiva* em "
        "todo x, [p=0.2] menos na raiz. [p=0.4] {b}Com *delta negativo,* [p=0.2] nem encosta: [p=0.2] *positiva para "
        "todo x.*"),

    # ================= BLOCO E: INEQUAÇÃO =================
    dict(id="13", block="ineq", text=
        "{t}E a *inequação?* [p=0.4] {a}Uma *inequação do segundo grau* pergunta onde a função é maior ou menor que "
        "zero.  [p=0.4] {b}*x ao quadrado, menos cinco x, mais seis, menor ou igual a zero.* [p=0.2] Soma cinco, "
        "produto seis: [p=0.2] raízes *dois e três.* [p=0.4] {c}a positivo: [p=0.2] sorrindo, [p=0.2] negativa no "
        "meio. [p=0.2] *x entre dois e três,* [p=0.2] com os dois incluídos. [p=0.2] Esse é o *conjunto solução:* [p=0.2] todos os x que servem. [p=0.4] {d}Atalho: [p=0.2] *confira com "
        "um número de cada região.* [p=0.2] Zero dá seis: [p=0.2] fora. [p=0.2] Dois e meio dá negativo: [p=0.2] "
        "dentro."),
    dict(id="14", block="naodivida", text=
        "{t}E o gancho? [p=0.3] {a}Não divida: [p=0.2] *passe tudo para um lado.* [p=0.2] x ao quadrado, menos quatro "
        "x, maior que zero. [p=0.4] {b}x vezes x menos quatro: [p=0.2] raízes *zero e quatro.* [p=0.2] Sorrindo: "
        "[p=0.2] *positiva fora.* [p=0.2] *x menor que zero ou x maior que quatro.* [p=0.4] {c}A divisão apagou a "
        "parte *negativa,* [p=0.2] porque *nunca se divide por x:* [p=0.2] você não sabe se ele é positivo ou "
        "negativo, [p=0.2] e o sinal da desigualdade pode virar."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Para quais x vale *x ao quadrado, menos nove, menor que zero?* [p=0.4] {b}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}x ao quadrado igual a nove: [p=0.2] raízes *menos três e três.* [p=0.4] {b}a "
        "positivo: [p=0.2] sorrindo, [p=0.2] negativa no meio. [p=0.2] *x entre menos três e três.* [p=0.4] {c}Quem "
        "tira a raiz e escreve só *x menor que três* [p=0.2] aceita o *menos cinco.* [p=0.2] Mas vinte e cinco menos "
        "nove dá *dezesseis:* [p=0.2] positivo. [p=0.2] Não serve."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] geral mostra o c; [p=0.2] fatorada, as raízes; "
        "[p=0.2] canônica, o vértice. [p=0.5] {b}Dois: [p=0.2] entre as raízes, o sinal contrário ao de a. [p=0.5] "
        "{c}Três: [p=0.2] inequação do segundo grau: [p=0.2] passe tudo para um lado [p=0.2] e nunca divida por x."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] x ao quadrado maior que quatro x, [p=0.2] "
        "então *x maior que quatro.* [p=0.4] {b}Parece certo, [p=0.2] porque dividir funciona nas equações. [p=0.4] "
        "{c}Mas x pode ser *negativo:* [p=0.2] x menor que zero [p=0.2] *ou* x maior que quatro."),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] dizer que x ao quadrado, menos cinco x, mais seis [p=0.2] é *positiva entre dois e três.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o a é positivo. [p=0.4] {c}Mas dois e meio dá *menos zero vírgula "
        "vinte e cinco.* [p=0.2] Com a positivo, [p=0.2] o meio é *negativo.*"),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] confundir lucro *crescendo* com lucro *positivo.* [p=0.2] Menos x ao quadrado, mais dez "
        "x, menos dezesseis [p=0.2] cresce até *x igual a cinco.* [p=0.4] {b}Parece certo, [p=0.2] porque crescer soa "
        "bom. [p=0.4] {c}Mas em x igual a um vale *menos sete:* [p=0.2] prejuízo, subindo. [p=0.2] Lucro positivo é "
        "*entre as raízes,* [p=0.2] dois e oito."),
    dict(id="21", block="erros", text=
        "{a}Quarto: [p=0.2] tomar o corte no eixo y pelo *a.* [p=0.2] Raízes dois e quatro, [p=0.2] corte em *oito:* "
        "[p=0.2] escrever *oito, vezes x menos dois, vezes x menos quatro.* [p=0.4] {b}Parece certo, [p=0.2] porque o "
        "oito é o número que sobrou. [p=0.4] {c}Mas essa lei corta em *sessenta e quatro.* [p=0.2] Em x igual a zero: "
        "[p=0.2] a vezes oito igual a oito. [p=0.2] *a igual a um.*"),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="22", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}O gráfico de "
        "uma função quadrática corta o eixo x em *um e cinco* [p=0.2] e o eixo y no ponto *zero, cinco.* [p=0.3] A lei "
        "dessa função é: [p=0.3] {qa}A: [p=0.2] x ao quadrado, mais seis x, mais cinco. [p=0.2] {qb}B: [p=0.2] x ao "
        "quadrado, menos seis x, mais cinco. [p=0.2] {qc}C: [p=0.2] menos x ao quadrado, mais seis x, menos cinco. "
        "[p=0.2] {qd}D: [p=0.2] x ao quadrado, menos cinco x, mais seis. [p=0.2] {qe}E: [p=0.2] cinco x ao quadrado, "
        "menos trinta x, mais vinte e cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q4", text=
        "{t}O gráfico mostra as *raízes:* [p=0.2] foto fatorada. [p=0.4] {a}*f de x igual a a, vezes x menos um, vezes "
        "x menos cinco.* [p=0.4] {b}O ponto zero, cinco: [p=0.2] a, vezes menos um, vezes menos cinco, igual a cinco. "
        "[p=0.2] *a igual a um.* [p=0.4] {c}Desenvolvendo: [p=0.2] *x ao quadrado, menos seis x, mais cinco.* [p=0.2] "
        "Em x igual a um: [p=0.2] *zero.* [p=0.3] {ok}*Letra B!*"),
    dict(id="24", block="q4", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A tem raízes *menos um e menos cinco.* [p=0.4] {xc}A C tem as raízes "
        "certas, [p=0.2] mas corta em *menos cinco.* [p=0.4] {xd}A D troca soma e produto: [p=0.2] raízes *dois e "
        "três.* [p=0.4] {xe}E a E usa a igual a cinco [p=0.2] e corta em *vinte e cinco.*"),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="25", block="q6", text=
        "{t}Esta a gente faz junto. [p=0.4] {a}Os pés do arco estão a *quarenta metros* um do outro, [p=0.2] e o topo "
        "fica *dez metros* acima da água, no meio. [p=0.3] A altura do arco [p=0.2] num ponto a *cinco metros de um "
        "dos pés* é: [p=0.3] {qa}A: [p=0.2] dois vírgula cinco metros. [p=0.2] {qb}B: [p=0.2] quatro vírgula três sete "
        "cinco. [p=0.2] {qc}C: [p=0.2] cinco vírgula seis dois cinco. [p=0.2] {qd}D: [p=0.2] sete vírgula cinco. "
        "[p=0.2] {qe}E: [p=0.2] nove vírgula três sete cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q6", text=
        "{t}A lei já está pronta: [p=0.2] *menos um quarenta avos, vezes x, vezes x menos quarenta.* [p=0.4] {a}Cinco "
        "metros do pé: [p=0.2] *x igual a cinco.* [p=0.2] Menos um quarenta avos, vezes cinco, vezes menos trinta e "
        "cinco. [p=0.4] {b}Dá *cento e setenta e cinco quarenta avos:* [p=0.2] *quatro vírgula três sete cinco "
        "metros.* [p=0.4] {c}Plausível: [p=0.2] perto do pé, [p=0.2] menos da metade do topo. [p=0.3] {ok}*Letra B!*"),
    dict(id="27", block="q6", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A sobe em *linha reta* do pé ao topo. [p=0.4] {xd}A D faz a reta com os "
        "*quinze metros* até o centro. [p=0.4] {xe}A E mede os cinco metros *a partir do centro.* [p=0.4] {xc}E a C: "
        "[p=0.2] quinze vinte avos, ao quadrado, vezes dez, [p=0.2] é o quanto o arco *desceu* do topo. [p=0.2] Dez "
        "menos isso: [p=0.2] quatro vírgula três sete cinco."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="28", block="q5", text=
        "{t}E esta é *sua.* [p=0.3] {a}O lucro mensal de uma pequena fábrica, em milhares de reais, [p=0.2] é *L de x "
        "igual a menos x ao quadrado, mais catorze x, menos quarenta,* [p=0.2] com x em *centenas* de unidades. [p=0.3] "
        "A fábrica tem lucro positivo quando produz: [p=0.3] {qa}A: [p=0.2] menos de quatrocentas unidades. [p=0.2] "
        "{qb}B: [p=0.2] mais de mil. [p=0.2] {qc}C: [p=0.2] menos de quatrocentas ou mais de mil. [p=0.2] {qd}D: "
        "[p=0.2] mais de quatrocentas e menos de mil. [p=0.2] {qe}E: [p=0.2] menos de setecentas. [p=0.5] {p}*Pause o "
        "vídeo e tente.* [p=2.0]"),
    dict(id="29", block="q5", text=
        "{t}Conferindo. [p=0.3] {a}Soma catorze, produto quarenta: [p=0.2] raízes *quatro e dez.* [p=0.4] {b}a igual a "
        "*menos um:* [p=0.2] parábola triste, [p=0.2] *positiva no meio.* [p=0.2] *Entre quatrocentas e mil unidades.* "
        "[p=0.4] {c}Testando: [p=0.2] L de sete vale *nove,* lucro. [p=0.2] L de dois, *menos dezesseis,* prejuízo. "
        "[p=0.3] {ok}*Letra D!*"),
    dict(id="30", block="q5", text=
        "{t}E as armadilhas? [p=0.3] {xc}A C é o sinal de uma parábola *sorrindo.* [p=0.4] {xa}A A [p=0.2] {xb}e a B "
        "[p=0.2] ficam com *um pedaço só* dessa região errada. [p=0.4] {xe}E a E confunde lucro *crescendo,* [p=0.2] "
        "antes do topo em sete, [p=0.2] com lucro *positivo.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] geral mostra o c; [p=0.2] fatorada, as raízes; "
        "[p=0.2] canônica, o vértice. [p=0.5] {b}Dois: [p=0.2] entre as raízes, o sinal contrário ao de a. [p=0.5] "
        "{c}Três: [p=0.2] inequação do segundo grau: [p=0.2] passe tudo para um lado [p=0.2] e nunca divida por x."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}vemos a parábola na *Física,* [p=0.2] "
        "na *Economia* [p=0.2] e na *Geometria* [p=0.3] {c}e caçamos as *pegadinhas.*"),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual das três fotos da parábola [p=0.2] você mais vai usar na "
        "prova? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os "
        "*flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
