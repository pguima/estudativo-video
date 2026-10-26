# Roteiro — Função Quadrática, Episódio 2 de 5: o vértice, o eixo de simetria, o máximo ou mínimo e as trajetórias.
# Base: Estudos/Enem/estudos/01-matematica/25-funcao-quadratica-vertice-raizes.html — seções 04 e 08 + Questões 1, 8 e 9.
#   Na seção 08, os instantes de 15 m (1 s e 3 s) já foram resolvidos na série de Equação do 2º grau: aqui só CITADOS
#   ("você já resolveu isso") para mostrar a simetria. Otimização com texto = ep. 3; formas fatorada e canônica = ep. 4.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O VÉRTICE MORA NO MEIO DAS RAÍZES: a parábola é um ESPELHO dobrado no eixo de simetria (a folha dobrada ao meio).
#   O x DO VÉRTICE responde ONDE ou QUANDO; o y DO VÉRTICE responde QUANTO.
#   O GRÁFICO NÃO É O CAMINHO: a bola sobe e desce em linha reta; a parábola está no desenho altura × tempo.
#   Do ep. 1: a parábola que SORRI (a > 0, tem fundo = mínimo) ou fica TRISTE (a < 0, tem topo = máximo).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Exemplos do prompt nos blocos (todos conferidos em trabalho/conferir_contas.py):
#   2x² − 8x + 6: xᵥ = 8/4 = 2; yᵥ = f(2) = 8 − 16 + 6 = −2; pela fórmula, −Δ/4a = −16/8 = −2; raízes 1 e 3, média 2.
#   h(t) = −5t² + 20t: tᵥ = 2 s; h(2) = 20 m; volta ao solo em 4 s (−5t(t − 4) = 0; o 0 é o lançamento); 15 m em 1 s e 3 s.
# Exemplo NOSSO (marcado) para "dois pontos de mesma altura": g(x) = x² − 6x + 5, g(0) = g(6) = 5 → eixo x = 3.
# Erros clássicos com os exemplos dos blocos: b/2a = −2 (espelhado) · −b/a = 4 (soma das raízes 1 + 3) · h(t) do bloco f
#   (responder 2 em vez de 20) · 2x² − 8x + 6 tem MÍNIMO · o gráfico h × t não é o caminho.
# Nós fazemos (prompt): x² − 4x + 3 → xᵥ = 2, f(2) = −1, a > 0 → mínimo, Im = [−1, +∞[; confere: raízes 1 e 3, média 2.
# QUESTÃO 1 (eu faço; texto idêntico ao material): B (45 m). Erradas (material): A instante; C só 30·3; D 45 + 90;
#   E instante de volta ao solo (6 s) sem o termo quadrático (30·6).
# QUESTÃO 8 (nós fazemos): A (30 peças e R$ 3 200,00). C(30) = 2·900 − 3 600 + 5 000 (dobrar ANTES de elevar daria o
#   distrator E, cuidado do roteiros.md). Erradas (material): B −b/a = 60; C soma 120·30 (10 400); D divide por 4a
#   (15 peças, R$ 3 650); E toma o termo independente (custo de zero peças).
# QUESTÃO 9 (você faz, com pausa): C (4 m). y = 0 → (x − 4)² = 4 → x = 2 ou 6. Erradas (material): A = yᵥ (2);
#   B ignora o 0,5: (x − 4)² = 2 → 4 ± √2, distância 2√2; D = abscissa da reentrada (6), medida do marco; E dobra a
#   abscissa do vértice (8). O "por que essa forma entrega o vértice" fica para o episódio 4 (só citado).
# Acréscimos NOSSOS (marcados): atalho verde "ache o x primeiro e SUBSTITUA" (cena 08); atalho verde "a média de dois
#   pontos de mesma altura" (cena 10); atalho verde "sublinhe a pergunta: quando/onde → x; quanto → y" (cena 16);
#   conferência da Q8 pelo sinal de a; na Q1, a conferência "a outra raiz (6 s) está a 3 s do vértice, como o 0".
# Frases-chave (meio e fim, idênticas): 1. xᵥ = −b sobre 2a; o yᵥ é f(xᵥ). 2. O vértice fica no meio das raízes.
#   3. x do vértice: onde ou quando. y do vértice: quanto.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "O vértice da parábola do zero: máximo, mínimo e altura máxima | Função Quadrática Ep. 2"
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
        "{a}Um artefato de fogos explode no *ponto mais alto.* [p=0.4] {b}A conta dá *três segundos,* [p=0.2] e o três "
        "está nas alternativas. [p=0.4] {c}Mas a pergunta era a *altura:* [p=0.2] *quarenta e cinco metros.* [p=0.5] "
        "{d}Metade dos erros deste assunto [p=0.2] é responder o *x do vértice* [p=0.2] quando pediam o *y.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai achar o *vértice* de qualquer parábola, [p=0.3] {b}dizer se ele é *máximo ou "
        "mínimo* [p=0.3] {c}e responder *altura máxima, instante e volta ao solo* de um lançamento."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] a positivo, a parábola *sorri;* [p=0.2] "
        "negativo, fica *triste;* [p=0.2] as *raízes* são onde ela toca o eixo x. [p=0.4] {b}Da série de Equação do "
        "2º grau: [p=0.2] a soma das raízes é *menos b sobre a.* [p=0.4] {c}E de Conceito de função: [p=0.2] a "
        "*imagem* é a *sombra* na parede."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Três imagens. [p=0.4] {a}A bola jogada para cima *para* um instante lá no alto. [p=0.4] {b}A rampa de "
        "skate em U tem um *ponto mais baixo.* [p=0.4] {c}A parábola *dobrada ao meio* tem as metades *coincidindo.* "
        "[p=0.4] {d}Os três falam do mesmo ponto: [p=0.2] o *vértice.*"),

    # ================= BLOCO A: VÉRTICE E EIXO =================
    dict(id="05", block="vertice", text=
        "{t}Mas o que é o vértice? [p=0.4] {a}O *vértice* é o ponto em que a curva *para de descer e começa a subir,* "
        "[p=0.2] ou o contrário. [p=0.4] {b}O *eixo de simetria* é a reta vertical que passa por ele [p=0.2] e divide "
        "a parábola em duas metades iguais. [p=0.4] {c}Um *espelho.*"),

    # ================= BLOCO B: AS COORDENADAS =================
    dict(id="06", block="coord", text=
        "{t}E como achar esse ponto sem desenhar? [p=0.4] {a}O *x do vértice* [p=0.2] é *menos b, sobre dois a.* "
        "[p=0.4] {b}O *y do vértice* [p=0.2] é *menos delta, sobre quatro a,* [p=0.3] {c}que é o mesmo que *f de x do "
        "vértice:* [p=0.2] a altura da curva naquele x."),
    dict(id="07", block="coord", text=
        "{t}Teste em *dois x ao quadrado, menos oito x, mais seis.* [p=0.4] {a}Menos b é *mais oito;* [p=0.2] dois a "
        "é *quatro.* [p=0.2] Oito sobre quatro: [p=0.2] x do vértice igual a *dois.* [p=0.4] {b}Agora f de dois: "
        "[p=0.2] oito, menos dezesseis, mais seis: [p=0.2] *menos dois.* [p=0.4] {c}Pela fórmula: [p=0.2] delta é "
        "dezesseis, [p=0.2] e menos dezesseis sobre oito [p=0.2] também dá *menos dois.* [p=0.3] {ok}*As duas "
        "concordam.*"),

    # ================= BLOCO C: SUBSTITUA =================
    dict(id="08", block="substitua", text=
        "{t}Atalho para o y. [p=0.4] {a}Ache *primeiro o x,* [p=0.2] depois *substitua* na função. [p=0.4] {b}Assim "
        "você não precisa do delta [p=0.2] nem do sinal de menos. [p=0.4] {c}A fórmula com delta fica para quando o x "
        "der uma *fração feia.*"),

    # ================= BLOCO D: NO MEIO DAS RAÍZES =================
    dict(id="09", block="meio", text=
        "{t}E por que essa fórmula funciona? [p=0.4] {a}As raízes de dois x ao quadrado, menos oito x, mais seis "
        "[p=0.2] são *um* e *três.* [p=0.4] {b}Dobre no eixo: [p=0.2] o um e o três se *encontram.* [p=0.4] {c}O "
        "vértice mora no *meio das raízes:* [p=0.2] um mais três, sobre dois: [p=0.2] *dois.* [p=0.4] {d}Menos b "
        "sobre a é a *soma;* [p=0.2] sobre dois a, a *média.*"),
    dict(id="10", block="meio", text=
        "{t}Atalho: [p=0.2] e sem as raízes? [p=0.4] {a}Serve *qualquer par de pontos de mesma altura.* [p=0.4] {b}Em "
        "x ao quadrado, menos seis x, mais cinco, [p=0.2] f de zero e f de seis valem *cinco.* [p=0.4] {c}O eixo "
        "passa no meio: [p=0.2] *x igual a três.*"),

    # ================= BLOCO E: MÁXIMO OU MÍNIMO =================
    dict(id="11", block="maxmin", text=
        "{t}O vértice é o mais alto ou o mais baixo? [p=0.4] {a}Com *a positivo,* a parábola sorri: [p=0.2] *ponto de "
        "mínimo,* o fundo. [p=0.4] {b}Com *a negativo,* fica triste: [p=0.2] *ponto de máximo,* o topo. [p=0.4] {c}O "
        "y do vértice é o *valor mínimo* ou *máximo:* [p=0.2] o menor ou o maior resultado."),
    dict(id="12", block="maxmin", text=
        "{t}E a imagem? [p=0.4] {a}Em dois x ao quadrado, menos oito x, mais seis, [p=0.2] o vértice é *mínimo.* "
        "[p=0.4] {b}A sombra na parede começa em *menos dois* e sobe sem fim. [p=0.4] {c}A curva *desce* até dois, "
        "[p=0.2] depois *sobe.* [p=0.4] {d}Com a negativo, tudo se inverte."),

    # ================= BLOCO F: TRAJETÓRIAS =================
    dict(id="13", block="trajeto", text=
        "{t}Agora a bola. [p=0.4] {a}A altura é *h de t igual a menos cinco t ao quadrado, mais vinte t,* [p=0.2] em "
        "metros e segundos. [p=0.4] {b}a negativo: [p=0.2] o vértice é *máximo.* [p=0.4] {c}Quando? [p=0.2] Menos "
        "vinte sobre menos dez: [p=0.2] *dois segundos.* [p=0.4] {d}A que altura? [p=0.2] h de dois, [p=0.2] menos "
        "vinte mais quarenta: [p=0.2] *vinte metros.*"),
    dict(id="14", block="trajeto", text=
        "{t}E a volta ao chão? [p=0.4] {a}Altura zero: [p=0.2] menos cinco t, vezes t menos quatro, igual a zero. "
        "[p=0.4] {b}O zero é o *lançamento;* [p=0.2] a volta é em *quatro segundos.* [p=0.4] {c}E os quinze metros, "
        "em um e em três segundos? [p=0.2] *Você já resolveu isso.* [p=0.2] Os dois ficam a *um segundo* do vértice."),

    # ================= BLOCO G: GRÁFICO × CAMINHO =================
    dict(id="15", block="caminho", text=
        "{t}A bola faz curva no ar? [p=0.4] {a}*Não.* [p=0.2] Ela sobe e desce em *linha reta.* [p=0.4] {b}A parábola "
        "está no *desenho altura por tempo.* [p=0.4] {c}A *trajetória,* o caminho no espaço, [p=0.2] é a reta. "
        "[p=0.4] {d}No lançamento *oblíquo,* o chute de lado, [p=0.2] o caminho é parábola: [p=0.2] *Física.*"),
    dict(id="16", block="pergunta", text=
        "{t}Atalho: [p=0.2] *sublinhe a pergunta.* [p=0.4] {a}*Quando* ou *onde* é o *x do vértice.* [p=0.4] "
        "{b}*Quanto* é o *y do vértice.* [p=0.4] {c}Na bola: [p=0.2] *quando,* dois segundos; [p=0.2] *quanto,* vinte "
        "metros."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}f de x igual a *x ao quadrado, menos quatro x, mais três.* [p=0.2] Qual é o vértice? "
        "[p=0.2] Ele é máximo ou mínimo? [p=0.2] Qual é a imagem? [p=0.3] {p}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Menos b sobre dois a: [p=0.2] *quatro sobre dois,* [p=0.2] *dois.* [p=0.4] "
        "{b}Substitua: [p=0.2] quatro, menos oito, mais três: [p=0.2] *menos um.* [p=0.4] {c}a positivo: [p=0.2] "
        "*mínimo.* [p=0.2] Imagem: [p=0.2] de *menos um até mais infinito.* [p=0.4] {d}Confira: [p=0.2] as raízes são "
        "um e três, [p=0.2] média *dois.* [p=0.3] {ok}*Bateu!*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Três frases para guardar. [p=0.5] {a}Um: [p=0.2] x do vértice é menos b sobre dois a; [p=0.2] o y do "
        "vértice é f de x do vértice. [p=0.5] {b}Dois: [p=0.2] o vértice fica no meio das raízes. [p=0.5] {c}Três: "
        "[p=0.2] x do vértice: onde ou quando. [p=0.2] y do vértice: quanto."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{a}Erro número um: [p=0.2] x do vértice igual a *b sobre dois a.* [p=0.4] {b}Parece certo porque o menos é "
        "pequeno e some na pressa. [p=0.4] {c}Correção: [p=0.2] escreva o menos *antes* do número. [p=0.2] Sem ele, o "
        "vértice vai para *menos dois:* [p=0.2] *espelhado.*"),
    dict(id="21", block="erros", text=
        "{a}Erro número dois: [p=0.2] usar *menos b sobre a.* [p=0.4] {b}Parece certo porque é a fórmula da série "
        "passada. [p=0.4] {c}Correção: [p=0.2] isso dá *quatro,* a *soma* das raízes. [p=0.2] O vértice é a *média:* "
        "[p=0.2] metade."),
    dict(id="22", block="erros", text=
        "{a}Erro número três: [p=0.2] responder o x quando pedem o *máximo.* [p=0.4] {b}Parece certo porque o dois "
        "sai primeiro. [p=0.4] {c}Correção: [p=0.2] *instante não é altura.* [p=0.2] Topo em dois segundos, [p=0.2] "
        "altura de *vinte metros.*"),
    dict(id="23", block="erros", text=
        "{a}Erro número quatro: [p=0.2] achar que *a positivo tem máximo.* [p=0.4] {b}Parece certo porque *positivo* "
        "soa como *topo.* [p=0.4] {c}Correção: [p=0.2] a positivo *sorri,* [p=0.2] e sorriso tem *fundo:* [p=0.2] é "
        "*mínimo.*"),
    dict(id="24", block="erros", text=
        "{a}Erro número cinco: [p=0.2] achar que o gráfico altura por tempo é o *caminho* do objeto. [p=0.4] "
        "{b}Parece certo porque o desenho lembra um arremesso. [p=0.4] {c}Correção: [p=0.2] o eixo horizontal é o "
        "*tempo.* [p=0.2] No lançamento vertical, o caminho é *reto.*"),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="25", block="q1", text=
        "{t}Hora de questão. [p=0.3] {a}Em uma demonstração de fogos, [p=0.2] um artefato é lançado verticalmente a "
        "partir do solo, [p=0.2] e sua altura, em metros, é dada por *h de t igual a menos cinco t ao quadrado, mais "
        "trinta t,* [p=0.2] em que t é o tempo em segundos após o lançamento. [p=0.2] O artefato explode no ponto mais "
        "alto da trajetória. [p=0.2] A altura da explosão, em metros, é: [p=0.4] {qa}A: [p=0.2] três. [p=0.3] {qb}B: "
        "[p=0.2] quarenta e cinco. [p=0.3] {qc}C: [p=0.2] noventa. [p=0.3] {qd}D: [p=0.2] cento e trinta e cinco. "
        "[p=0.3] {qe}E: [p=0.2] cento e oitenta."),
    dict(id="26", block="q1", text=
        "{t}Eu faço. [p=0.3] {a}Pedem a *altura:* [p=0.2] o *y* do vértice. [p=0.4] {b}O x primeiro: [p=0.2] menos "
        "trinta sobre menos dez, [p=0.2] *três segundos.* [p=0.4] {c}Substitua: [p=0.2] menos cinco vezes nove, "
        "*menos quarenta e cinco;* [p=0.2] mais trinta vezes três, *noventa:* [p=0.2] *quarenta e cinco metros.* "
        "[p=0.3] {ok}*Letra B!* [p=0.4] {d}Confira: [p=0.2] a volta é em seis segundos, [p=0.2] e o três é o *meio.*"),
    dict(id="27", block="q1", text=
        "{t}E as erradas? [p=0.3] {xa}A A, três, [p=0.2] é o *instante.* [p=0.4] {xc}A C faz só *trinta vezes três,* "
        "[p=0.2] sem o menos cinco t ao quadrado. [p=0.4] {xd}A D *troca o sinal* desse termo: [p=0.2] quarenta e "
        "cinco mais noventa. [p=0.4] {xe}E a E usa a *volta ao solo,* seis segundos, [p=0.2] e ainda ignora o "
        "quadrado."),

    # ================= QUESTÃO 8 (NÓS FAZEMOS) =================
    dict(id="28", block="q8", text=
        "{t}Agora juntos. [p=0.3] {a}O custo diário de produção de uma oficina, em reais, [p=0.2] é *C de x igual a "
        "dois x ao quadrado, menos cento e vinte x, mais cinco mil,* [p=0.2] em que x é o número de peças produzidas "
        "no dia. [p=0.2] A quantidade de peças que torna o custo mínimo e o valor desse custo são, respectivamente: "
        "[p=0.4] {qa}A: [p=0.2] trinta peças e três mil e duzentos reais. [p=0.3] {qb}B: [p=0.2] sessenta peças e cinco "
        "mil reais. [p=0.3] {qc}C: [p=0.2] trinta peças e dez mil e quatrocentos reais. [p=0.3] {qd}D: [p=0.2] quinze "
        "peças e três mil seiscentos e cinquenta reais. [p=0.3] {qe}E: [p=0.2] trinta peças e cinco mil reais. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="29", block="q8", text=
        "{t}Vamos juntos. [p=0.3] {a}Pedem *o x e o y.* [p=0.2] a positivo: [p=0.2] existe um *mínimo.* [p=0.4] "
        "{b}Cento e vinte sobre quatro: [p=0.2] *trinta peças.* [p=0.4] {c}Substitua com calma: [p=0.2] trinta ao "
        "quadrado, novecentos; [p=0.2] vezes dois, *mil e oitocentos.* [p=0.2] Menos três mil e seiscentos, mais "
        "cinco mil: [p=0.2] *três mil e duzentos.* [p=0.3] {ok}*Letra A!* [p=0.4] {xb}A B usou *menos b sobre a.* "
        "[p=0.3] {xc}A C *somou* o cento e vinte vezes trinta. [p=0.3] {xd}A D dividiu por *quatro a.* [p=0.3] {xe}A "
        "E é o custo de *zero* peças."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="30", block="q9", text=
        "{t}Agora é com você. [p=0.3] {a}Num parque aquático, [p=0.2] a trajetória do salto de um golfinho, fora da "
        "água, [p=0.2] é descrita por *y igual a menos zero vírgula cinco, vezes x menos quatro ao quadrado, mais "
        "dois,* [p=0.2] em que x é a distância horizontal, em metros, a partir de um marco na borda do tanque, [p=0.2] e "
        "y é a altura acima da superfície da água, em metros. [p=0.2] A distância horizontal entre o ponto em que o "
        "golfinho sai da água e o ponto em que volta a ela é: [p=0.4] {qa}A: [p=0.2] dois metros. [p=0.3] {qb}B: "
        "[p=0.2] dois raiz de dois metros. [p=0.3] {qc}C: [p=0.2] quatro metros. [p=0.3] {qd}D: [p=0.2] seis metros. "
        "[p=0.3] {qe}E: [p=0.2] oito metros. [p=0.4] {p}*Pause o vídeo.* [p=2.0]"),
    dict(id="31", block="q9", text=
        "{t}Confira. [p=0.3] {a}Na água, a altura é *zero.* [p=0.4] {b}Zero vírgula cinco, vezes x menos quatro ao "
        "quadrado, igual a dois: [p=0.2] o quadrado vale *quatro.* [p=0.4] {c}x menos quatro é *dois* ou *menos "
        "dois:* [p=0.2] x é *dois* ou *seis.* [p=0.4] {d}Seis menos dois: [p=0.2] *quatro metros.* [p=0.3] {ok}*Letra "
        "C!* [p=0.4] {e}E o vértice, em quatro, está no *meio.*"),
    dict(id="32", block="q9", text=
        "{t}E as erradas? [p=0.3] {xa}A A é a *altura máxima.* [p=0.4] {xb}A B ignorou o *zero vírgula cinco.* "
        "[p=0.4] {xd}A D é o ponto de volta, medido do *marco.* [p=0.4] {xe}A E dobrou o quatro. [p=0.4] {f}Por que "
        "essa forma *entrega* o vértice? [p=0.2] *Episódio quatro.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] x do vértice é menos b sobre dois a; [p=0.2] o "
        "y do vértice é f de x do vértice. [p=0.5] {b}Dois: [p=0.2] o vértice fica no meio das raízes. [p=0.5] "
        "{c}Três: [p=0.2] x do vértice: onde ou quando. [p=0.2] y do vértice: quanto."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Com *sessenta metros de tela* e um muro, [p=0.2] qual retângulo dá a *maior horta?* [p=0.4] {b}Quase todo "
        "mundo chuta um *quadrado,* [p=0.2] e o quadrado *perde.* [p=0.5] {c}Próximo episódio: [p=0.2] "
        "*otimização.*"),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] você já respondeu o x quando pediam o y? [p=0.5] {anki}E tem mais: [p=0.2] na "
        "*descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo "
        "de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, e *até a "
        "próxima aula* aqui no Estudativo. [p=1.5]"),
]
