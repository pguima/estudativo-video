# Roteiro — Função Quadrática, Episódio 1 de 5: a parábola, concavidade, corte no eixo y e o que o Δ desenha
# Base: Estudos/Enem/estudos/01-matematica/25-funcao-quadratica-vertice-raizes.html — seções 02 e 03.
#   A Questão 7 do material NÃO entra (quase igual à Q2 da série de Equação do 2º grau): no lugar dela, a QUESTÃO NOVA
#   do prompt (f(x) = −x² + 10x − k inteiramente abaixo do eixo x), que não está no material.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A PARÁBOLA QUE SORRI OU FICA TRISTE: a > 0 sorri (boca para cima, tem um fundo = mínimo); a < 0 fica triste
#     (boca para baixo, tem um topo = máximo).
#   O Δ CONTA OS TOQUES NO CHÃO: o eixo x é o chão; Δ > 0 duas vezes, Δ = 0 uma vez, Δ < 0 nenhuma.
#   O a ANDA COM O x²: identifique pela potência, não pela posição (h = 20t − 5t² tem a = −5).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Bhaskara, Δ e soma e produto = REVISÃO (série de Equação do 2º grau). O vértice fica para o episódio 2: aqui só é citado.
# Exemplos do prompt nos blocos: 2x² − 8x + 6 (corta em (0, 6); Δ = (−8)² − 4·2·6 = 16; raízes 1 e 3) e x² − 7x + 10
#   (soma 7, produto 10: 2 e 5). Exemplos NOSSOS das três parábolas (cena 14–15): x² − 4x + 3 (Δ = 4, raízes 1 e 3),
#   x² − 4x + 4 (Δ = 0, raiz dupla 2), x² − 2x + 3 (Δ = −8) e a virada −x² + 2x − 3 (Δ = −8, toda abaixo).
# Nós fazemos (prompt): −x² + 4x + 5 → a = −1 (boca para baixo), corta em (0, 5), x² − 4x − 5 = 0 → soma 4, produto −5 →
#   raízes 5 e −1 (confere: Δ = 16 + 20 = 36).
# QUESTÃO NOVA ("você faz", com pausa): gabarito C (k > 25). Δ = 10² − 4·(−1)·(−k) = 100 − 4k < 0 → k > 25. Conferência
#   pelo ponto mais alto, em x = 5: f(5) = 25 − k < 0. Erradas = prompt (A: Δ > 0, dois cortes; B: Δ = 0, tangencia;
#   D: esquece o 4 de 4ac, 100 − k < 0; E: sinal trocado, 100 + 4k < 0, que na verdade dá dois cortes).
# Acréscimos NOSSOS (marcados): atalho verde "ponha x = 0: sobra o c" (cena 10); atalho verde "a, b e c pela potência,
#   com sinal" (cena 12); atalho verde "leitura em 3 olhadas: a → boca, c → corte no y, Δ → toques no x" (cena 17);
#   na Questão nova, o "x = 5 é o meio" é só citado (o porquê é o episódio 2).
# Erro 3 usa x² − 2x + 3 (Δ = −8 e f(0) = 3, positiva para todo x).
# Frases-chave (meio e fim, idênticas): 1. a positivo sorri e tem mínimo; a negativo fica triste e tem máximo.
#   2. c é onde a parábola corta o eixo vertical. 3. Δ conta quantas vezes a parábola encosta no eixo x.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Função quadrática do zero: a parábola e o que o Δ desenha · Matemática ENEM, Função quadrática episódio 1"

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
        "{a}Uma bola é lançada para cima: [p=0.3] depois de zero, um, dois, três e quatro segundos, [p=0.2] ela está a "
        "*zero, quinze, vinte, quinze e zero metros.* [p=0.5] {b}Sobe quinze, [p=0.2] sobe cinco, [p=0.2] desce cinco, "
        "[p=0.2] desce quinze. [p=0.5] {c}Na função afim os degraus eram sempre iguais. [p=0.3] Aqui *não são,* [p=0.3] "
        "{d}e o desenho deixa de ser reta: [p=0.3] *vira parábola.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o primeiro episódio da série de *Função quadrática.* [p=0.4] {a}Ao final, você vai olhar para uma lei "
        "do segundo grau e dizer, [p=0.2] sem desenhar, [p=0.3] *para que lado a parábola abre,* [p=0.3] {b}*onde corta o "
        "eixo vertical* [p=0.3] {c}e *quantas vezes toca o eixo horizontal.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Equação do segundo grau: [p=0.2] a *fórmula de Bhaskara,* "
        "[p=0.2] o *delta,* *b ao quadrado menos quatro a c,* [p=0.2] e a *soma e produto.* [p=0.4] {b}Da Função "
        "afim: [p=0.2] a reta sobe *no mesmo ritmo.* [p=0.4] {c}E do Conceito de função: [p=0.2] o gráfico é feito "
        "dos pontos *x, f de x.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}O que estas três coisas têm em comum? [p=0.4] {a}A *bola chutada para cima:* [p=0.2] sobe, [p=0.2] para, "
        "[p=0.2] desce. [p=0.4] {b}O *jato de água* do bebedouro. [p=0.4] {c}E o perfil da *antena parabólica.* "
        "[p=0.4] {d}As três desenham a *mesma curva.* [p=0.3] E ela tem uma lei."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}Que lei é essa? [p=0.4] {a}Uma *função quadrática,* [p=0.2] ou *do segundo grau,* [p=0.2] tem a forma *f "
        "de x igual a a x ao quadrado, [p=0.2] mais b x, [p=0.2] mais c.* [p=0.4] {b}O *a,* o *b* e o *c* são os "
        "*coeficientes:* [p=0.2] os números fixos da lei. [p=0.4] {c}E o desenho dela é a *parábola:* [p=0.2] a "
        "curva em arco, [p=0.2] igual à da bola."),
    dict(id="06", block="definicao", text=
        "{t}E o *a* pode ser zero? [p=0.4] {a}Não. [p=0.2] Com a igual a zero, [p=0.2] o x ao quadrado *some.* "
        "[p=0.4] {b}Sobra *b x mais c:* [p=0.2] uma *função afim,* [p=0.2] e o gráfico volta a ser *reta.*"),

    # ================= BLOCO B: CONCAVIDADE =================
    dict(id="07", block="concavidade", text=
        "{t}Para que lado a parábola abre? [p=0.4] {a}Isso é a *concavidade:* [p=0.2] o lado para onde a boca "
        "aponta. [p=0.2] Quem decide é *só o a.* [p=0.4] {b}a *positivo:* [p=0.2] a parábola *sorri,* [p=0.2] boca "
        "para cima. [p=0.2] Tem um *fundo,* [p=0.2] um *mínimo,* [p=0.2] e nenhum máximo. [p=0.4] {c}a *negativo:* "
        "[p=0.2] ela fica *triste,* [p=0.2] boca para baixo. [p=0.2] Tem um *topo,* [p=0.2] um *máximo,* [p=0.2] e "
        "nenhum mínimo. [p=0.4] {d}A bola sobe e desce: [p=0.2] tem topo. [p=0.2] O a dela é *negativo.*"),
    dict(id="08", block="abertura", text=
        "{t}E o *tamanho* do a? [p=0.4] {a}Muda a *abertura.* [p=0.3] Compare *meio x ao quadrado,* [p=0.2] *x ao "
        "quadrado* [p=0.2] e *três x ao quadrado.* [p=0.4] {b}Quanto maior o a, [p=0.2] sem olhar o sinal, [p=0.2] "
        "mais *fechada* a parábola."),

    # ================= BLOCO C: O c =================
    dict(id="09", block="corte_y", text=
        "{t}E onde a parábola corta o eixo vertical? [p=0.4] {a}No eixo vertical, [p=0.2] o x vale *zero.* [p=0.4] "
        "{b}Ponha zero no x: [p=0.2] o a x ao quadrado some, [p=0.2] o b x some, [p=0.2] sobra *só o c.* [p=0.4] "
        "{c}Em *dois x ao quadrado, menos oito x, mais seis,* [p=0.2] o corte é no ponto *zero, seis.* [p=0.4] {d}E "
        "o *b?* [p=0.2] Junto com o a, [p=0.2] ele decide de que lado fica a ponta da parábola. [p=0.2] Episódio "
        "dois."),
    dict(id="10", block="atalho_c", text=
        "{t}Atalho. [p=0.3] {a}*Ponha x igual a zero: [p=0.2] sobra o c.* [p=0.4] {b}O c é a *altura* do corte no "
        "eixo vertical. [p=0.3] {c}Na bola, [p=0.2] o c é zero: [p=0.2] ela sai *do chão.*"),

    # ================= BLOCO D: O a ANDA COM O x² =================
    dict(id="11", block="potencia", text=
        "{t}E se a lei vier fora de ordem? [p=0.4] {a}A altura da bola é *h de t igual a vinte t, [p=0.2] menos "
        "cinco t ao quadrado.* [p=0.4] {b}O a é o vinte, [p=0.2] que vem primeiro? [p=0.4] {c}Não. [p=0.2] O *a anda "
        "com o x ao quadrado,* [p=0.2] esteja onde estiver. [p=0.3] Aqui, [p=0.2] o *a é menos cinco,* [p=0.2] o b é "
        "vinte [p=0.2] e o c é zero."),
    dict(id="12", block="atalho_abc", text=
        "{t}Atalho. [p=0.3] {a}*Identifique pela potência, [p=0.2] não pela posição.* [p=0.4] {b}Com o x ao "
        "quadrado: [p=0.2] o a. [p=0.2] Com o x sozinho: [p=0.2] o b. [p=0.2] Sem x: [p=0.2] o c. [p=0.4] {c}E "
        "escreva os três *com o sinal.*"),

    # ================= BLOCO E: RAÍZES =================
    dict(id="13", block="raizes", text=
        "{t}E onde a parábola corta o eixo horizontal? [p=0.4] {a}Nas *raízes,* [p=0.2] ou *zeros:* [p=0.2] os "
        "valores de x em que f de x vale zero. [p=0.4] {b}É resolver *a x ao quadrado mais b x mais c igual a zero.* "
        "[p=0.2] Você já sabe. [p=0.4] {c}Em *dois x ao quadrado, menos oito x, mais seis:* [p=0.2] delta igual a "
        "*menos oito, entre parênteses, ao quadrado,* [p=0.2] menos quatro vezes dois vezes seis. [p=0.2] "
        "*Dezesseis.* [p=0.2] Raízes *um e três.* [p=0.4] {d}Em *x ao quadrado, menos sete x, mais dez:* [p=0.2] "
        "soma sete, [p=0.2] produto dez. [p=0.2] *Dois e cinco.*"),

    # ================= BLOCO F: O Δ DESENHA =================
    dict(id="14", block="delta", text=
        "{t}E o delta, [p=0.2] o que tem a ver com o desenho? [p=0.4] {a}O delta, [p=0.2] o *discriminante,* [p=0.2] "
        "*conta quantas vezes a parábola encosta no chão,* [p=0.2] o eixo x. [p=0.4] {b}Delta *positivo:* [p=0.2] "
        "*dois* cortes. [p=0.4] {c}Delta *zero:* [p=0.2] *um* toque. [p=0.2] É a *raiz dupla:* [p=0.2] a parábola "
        "*tangencia* o eixo, [p=0.2] encosta sem atravessar, [p=0.2] com a ponta *em cima do eixo.* [p=0.4] {d}Delta "
        "*negativo:* [p=0.2] *nenhum* corte. [p=0.2] Ela flutua."),
    dict(id="15", block="delta_lado", text=
        "{t}E com delta negativo, [p=0.2] de que lado ela fica? [p=0.4] {a}*Inteira de um lado só,* [p=0.2] e quem "
        "escolhe é o *a.* [p=0.4] {b}a *positivo:* [p=0.2] ela sorri [p=0.2] e fica *toda acima* do eixo. [p=0.4] "
        "{c}Vire a boca para baixo, [p=0.2] a *negativo:* [p=0.2] *toda abaixo.*"),
    dict(id="16", block="atalho_olhadas", text=
        "{t}Junte tudo. [p=0.3] {a}Atalho: [p=0.2] *leitura em três olhadas.* [p=0.4] {b}O *sinal do a:* [p=0.2] a "
        "boca. [p=0.3] {c}O *c:* [p=0.2] o corte no eixo vertical. [p=0.3] {d}O *delta:* [p=0.2] quantos toques no "
        "eixo horizontal. [p=0.4] {e}Sem desenhar nada."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*f de x igual a menos x ao quadrado, [p=0.2] mais quatro x, [p=0.2] mais cinco.* "
        "[p=0.4] {b}Para que lado abre? [p=0.3] Onde corta o eixo vertical? [p=0.3] Quais são as raízes? [p=0.4] "
        "{c}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O x ao quadrado está com *menos um:* [p=0.2] *boca para baixo.* [p=0.4] {b}O c "
        "é cinco: [p=0.2] corta em *zero, cinco.* [p=0.4] {c}Para as raízes, [p=0.2] multiplique tudo por menos um: "
        "[p=0.2] *x ao quadrado, menos quatro x, menos cinco, igual a zero.* [p=0.2] Soma quatro, [p=0.2] produto "
        "menos cinco. [p=0.4] {d}*Cinco e menos um.* [p=0.3] Cinco mais menos um, quatro; [p=0.2] cinco vezes menos "
        "um, menos cinco. [p=0.2] *Bate.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a positivo sorri e tem mínimo; [p=0.2] a negativo fica "
        "triste e tem máximo. [p=0.5] {b}Dois: [p=0.2] c é onde a parábola corta o eixo vertical. [p=0.5] {c}Três: "
        "[p=0.2] delta conta quantas vezes a parábola encosta no eixo x."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] ler *a igual a vinte* [p=0.2] em *vinte t "
        "menos cinco t ao quadrado.* [p=0.4] {b}Parece certo, [p=0.2] porque na definição o a vem *primeiro.* "
        "[p=0.4] {c}Mas o a anda com o quadrado: [p=0.2] *menos cinco.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] achar que *a positivo tem máximo.* [p=0.4] {b}Parece certo, [p=0.2] porque positivo "
        "lembra *subir,* [p=0.2] e subir lembra *topo.* [p=0.4] {c}Mas o a positivo sorri: [p=0.2] tem *fundo,* "
        "[p=0.2] tem *mínimo.*"),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] achar que *delta negativo* [p=0.2] é *função negativa.* [p=0.4] {b}Parece certo: "
        "[p=0.2] os dois são *negativos.* [p=0.4] {c}Mas delta negativo só diz que *não há raiz.* [p=0.2] *x ao "
        "quadrado, menos dois x, mais três* [p=0.2] tem delta menos oito, [p=0.2] e é *positiva* para todo x. "
        "[p=0.3] Sem raízes, [p=0.2] ela tem o *sinal do a.*"),

    # ================= QUESTÃO NOVA (VOCÊ FAZ) =================
    dict(id="23", block="qnova", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta é *sua.* [p=0.4] {a}Em um programa de computador, "
        "[p=0.2] o gráfico de *f de x igual a menos x ao quadrado, [p=0.2] mais dez x, [p=0.2] menos k* [p=0.2] "
        "aparece *inteiramente abaixo* do eixo das abscissas, [p=0.2] sem tocá-lo. [p=0.3] Esses valores de k "
        "satisfazem: [p=0.3] {qa}A: [p=0.2] k menor que vinte e cinco. [p=0.2] {qb}B: [p=0.2] k igual a vinte e "
        "cinco. [p=0.2] {qc}C: [p=0.2] k maior que vinte e cinco. [p=0.2] {qd}D: [p=0.2] k maior que cem. [p=0.2] "
        "{qe}E: [p=0.2] k menor que menos vinte e cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="24", block="qnova", text=
        "{t}Conferindo. [p=0.3] {a}a igual a *menos um:* [p=0.2] boca para baixo. [p=0.2] Inteira abaixo do eixo, "
        "[p=0.2] sem tocar o chão: [p=0.2] *delta negativo.* [p=0.4] {b}Com sinal: [p=0.2] a, menos um; [p=0.2] b, "
        "dez; [p=0.2] c, *menos k.* [p=0.4] {c}Delta: [p=0.2] dez ao quadrado, [p=0.2] menos quatro, [p=0.2] vezes "
        "*menos um,* [p=0.2] vezes *menos k:* [p=0.2] *cem menos quatro k.* [p=0.4] {d}Cem menos quatro k menor que "
        "zero: [p=0.2] *k maior que vinte e cinco.* [p=0.3] {ok}*Letra C!*"),
    dict(id="25", block="qnova", text=
        "{t}Outro jeito de conferir. [p=0.3] {a}O topo dessa parábola fica em *x igual a cinco.* [p=0.2] O porquê é "
        "o próximo episódio. [p=0.4] {b}f de cinco: [p=0.2] menos vinte e cinco, mais cinquenta, menos k: [p=0.2] "
        "*vinte e cinco menos k.* [p=0.4] {c}Se até o topo fica abaixo do chão, [p=0.2] a parábola inteira fica: "
        "[p=0.2] *k maior que vinte e cinco.* [p=0.2] Bate."),
    dict(id="26", block="qnova", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A é delta *positivo:* [p=0.2] dois cortes. [p=0.4] {xb}A B é delta "
        "*zero:* [p=0.2] ela encosta. [p=0.4] {xd}A D *esquece o quatro:* [p=0.2] cem menos k. [p=0.4] {xe}E a E "
        "*troca o sinal:* [p=0.2] cem mais quatro k. [p=0.2] Com k menor que menos vinte e cinco, [p=0.2] a parábola "
        "corta o eixo *duas vezes.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a positivo sorri e tem mínimo; [p=0.2] a negativo "
        "fica triste e tem máximo. [p=0.5] {b}Dois: [p=0.2] c é onde a parábola corta o eixo vertical. [p=0.5] {c}Três: "
        "[p=0.2] delta conta quantas vezes a parábola encosta no eixo x."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}Um artefato de fogos é lançado com *h de t igual a menos cinco t ao quadrado, [p=0.2] mais trinta t,* "
        "[p=0.2] e explode no *ponto mais alto.* [p=0.4] {b}Em que instante [p=0.2] e a que altura? [p=0.4] {c}A "
        "resposta mora num *ponto só* da parábola. [p=0.4] {d}Próximo episódio: [p=0.2] *o vértice.*"),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] onde você já viu uma parábola hoje? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
