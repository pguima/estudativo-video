# Roteiro — Conceito de Função, Domínio e Imagem, Episódio 4 de 6: o gráfico (teste da reta vertical e leitura de
#   domínio, imagem e comportamento).
# Base: Estudos/Enem/estudos/01-matematica/23-conceito-funcao-dominio-imagem.html — seções 06 e 07 + Questão 8 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   As SOMBRAS: o domínio é a sombra da curva no CHÃO (eixo x, lanterna em cima); a imagem é a sombra na PAREDE (eixo y,
#     lanterna do lado).
#   A RÉGUA EM PÉ: passe uma régua vertical pelo gráfico; se em algum lugar ela tocar a curva duas vezes, aquele x teria
#     duas saídas, e não é função (é o "duas flechas saindo" do ep. 1; horizontal cortando duas vezes = "duas flechas
#     chegando", que pode).
#   QUANDO × QUANTO: pergunta de "quando" se responde no chão (x); pergunta de "quanto" se responde na parede (y).
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Plano cartesiano: só o mínimo (eixo x, eixo y, par ordenado) em ~30 s, com a promessa da série própria.
# Gráfico da seção 07 (desenho nosso que respeita TODOS os dados do material): sobe de (−1, 1) até (2, 4) e desce até
#   x = 6, passando por (4, 3); a ponta direita fica em y ≈ 1,7 (o material não dá esse valor e o vídeo não o cita).
#   Leituras: domínio [−1, 6] · imagem [1, 4] · máximo 4 em x = 2 · mínimo 1 em x = −1 · cresce em [−1, 2] · decresce em
#   [2, 6] · sem zeros · f(4) = 3.
# Exemplo concreto NOSSO: previsão do tempo com máxima de 28 °C às 14 h (curva suave de 18 °C a 28 °C).
# Nós fazemos (prompt): segmentos (0, 2)–(3, 5) e (3, 5)–(6, −1), pontas incluídas → domínio [0, 6]; imagem [−1, 5]
#   (o mais baixo é −1, na ponta direita; o mais alto é 5, no meio).
# QUESTÃO 8 ("você faz", com pausa): segmentos (−2, 1)–(1, 4) e (1, 4)–(5, 0) → imagem [0, 4] → E. Erradas (prompt e
#   material): A [−2, 5] é o domínio; B [1, 4] só o primeiro segmento; C [0, 5] e D [−2, 4] misturam x e y. Detalhe NOSSO
#   (marcado): C junta o y mais baixo (0) com o x mais à direita (5); D junta o x mais à esquerda (−2) com o y mais alto (4).
# Acréscimos NOSSOS (verde): "a régua em pé, nunca deitada" (cena 10) e "quando ou quanto? diga o eixo antes do número"
#   (cena 17). Erro 2 usa o gráfico do "nós fazemos" (ponta a ponta daria [−1, 2]).
# Frases-chave (meio e fim, idênticas): 1. Régua em pé tocando duas vezes: não é função. 2. Domínio é a sombra no chão;
#   imagem é a sombra na parede. 3. Cresce e decresce se responde em x.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Gráfico de função do zero: domínio e imagem são SOMBRAS | Funções Ep. 4"
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
        "{a}Uma questão pergunta em que intervalo a função *cresce.* [p=0.4] {b}A curva sobe da altura *um* até a altura "
        "*quatro,* [p=0.3] e muita gente marca *entre um e quatro.* [p=0.5] {c}Errado: [p=0.2] a resposta certa fala do "
        "*x,* [p=0.2] e não da altura. [p=0.4] {d}Hoje você aprende a não cair nessa troca."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai olhar um gráfico e dizer se ele é de uma *função,* [p=0.3] {b}qual é o *domínio,* "
        "[p=0.2] qual é a *imagem,* [p=0.3] {c}onde está o *máximo* [p=0.2] e onde a curva *sobe* ou *desce.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Um *par ordenado,* [p=0.2] como *três vírgula dois,* [p=0.2] é um "
        "endereço: [p=0.2] primeiro anda *três* na horizontal, [p=0.2] depois sobe *dois* na vertical. [p=0.4] {b}E, da "
        "série de Equações e inequações: [p=0.2] o intervalo *de menos um a seis,* [p=0.2] com *colchete fechado,* "
        "[p=0.2] quer dizer que as pontas *entram.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Abra a *previsão do tempo* no celular. [p=0.3] {a}Embaixo, as *horas* do dia. [p=0.2] Na lateral, a "
        "*temperatura.* [p=0.4] {b}Qual foi a *máxima* do dia, [p=0.2] e a que horas ela aconteceu? [p=0.5] {c}Para a "
        "máxima, [p=0.2] você olha a *lateral:* [p=0.2] *vinte e oito graus.* [p=0.3] {d}Para a hora, [p=0.2] você desce "
        "até *embaixo:* [p=0.2] *quatorze horas.* [p=0.3] Sem perceber, [p=0.2] você leu um gráfico."),

    # ================= PLANO CARTESIANO =================
    dict(id="05", block="plano", text=
        "{t}Esse desenho tem nome. [p=0.3] {a}O *plano cartesiano* são duas retas numeradas que se cruzam. [p=0.3] A "
        "deitada é o *eixo horizontal,* [p=0.2] o *eixo x:* [p=0.2] pense nele como o *chão.* [p=0.4] {b}A de pé é o *eixo "
        "vertical,* [p=0.2] o *eixo y:* [p=0.2] a *parede.* [p=0.4] {c}Cada ponto tem um par ordenado, [p=0.2] *x vírgula "
        "y.* [p=0.3] {d}O plano ainda vai ganhar uma série só dele. [p=0.2] Hoje, isso basta."),

    # ================= BLOCO A: O GRÁFICO =================
    dict(id="06", block="grafico", text=
        "{t}E o que é o *gráfico* de uma função? [p=0.4] {a}Pegue cada entrada *x* [p=0.2] e a sua saída, *f de x.* "
        "[p=0.3] Junte as duas num ponto: [p=0.2] *x vírgula f de x.* [p=0.4] {b}Com f de x igual a x mais um: [p=0.2] "
        "*zero vírgula um,* [p=0.2] *um vírgula dois,* [p=0.2] *dois vírgula três.* [p=0.4] {c}O *gráfico* é o desenho de "
        "*todos* esses pontos juntos. [p=0.3] {d}A altura de cada ponto [p=0.2] é a saída daquele x."),

    # ================= BLOCO B: A RÉGUA EM PÉ =================
    dict(id="07", block="regua", text=
        "{t}Como saber, só de olhar, [p=0.2] se um desenho é gráfico de função? [p=0.4] {a}Pegue uma *régua em pé* [p=0.2] "
        "e passe pelo desenho, [p=0.2] da esquerda para a direita. [p=0.4] {b}Nesta curva, [p=0.2] a régua toca *uma vez* "
        "em cada lugar. [p=0.3] *É função.* [p=0.5] {c}Agora, na *circunferência.* [p=0.3] {d}Aqui a régua toca *duas "
        "vezes* [p=0.2] no mesmo lugar."),
    dict(id="08", block="regua2", text=
        "{t}E por que isso estraga tudo? [p=0.4] {a}Os dois pontos estão no *mesmo x.* [p=0.3] Um em cima, [p=0.2] outro "
        "embaixo. [p=0.4] {b}Então aquele x teria *duas saídas.* [p=0.3] É o *duas flechas saindo* do episódio um. [p=0.4] "
        "{c}A circunferência *não é* gráfico de função. [p=0.3] Esse é o *teste da reta vertical.*"),

    # ================= BLOCO C: HORIZONTAL PODE =================
    dict(id="09", block="horizontal", text=
        "{t}E se a régua estiver *deitada?* [p=0.4] {a}Olhe esta curva em forma de *U.* [p=0.2] Uma reta horizontal "
        "[p=0.2] corta a curva em *dois* pontos. [p=0.4] {b}Isso só diz que *dois x diferentes* [p=0.2] têm a *mesma* "
        "altura. [p=0.3] {c}É o *duas flechas chegando:* [p=0.2] pode. [p=0.4] {d}A curva em U continua sendo "
        "*função.*"),
    dict(id="10", block="atalho1", text=
        "{t}Guarde o atalho. [p=0.3] {a}*Régua em pé, [p=0.2] nunca deitada.* [p=0.4] {b}Deslize a régua de pé pelo "
        "gráfico inteiro. [p=0.3] Tocou *duas vezes* em algum lugar? [p=0.2] Não é função. [p=0.4] {c}A régua deitada "
        "[p=0.2] não decide nada."),

    # ================= BLOCO D: AS SOMBRAS =================
    dict(id="11", block="sombras", text=
        "{t}Agora, um gráfico de verdade. [p=0.3] Qual é o *domínio* dele? [p=0.4] {a}Acenda uma *lanterna em cima* da "
        "curva. [p=0.3] A sombra cai no *chão,* [p=0.2] no eixo x. [p=0.4] {b}Essa sombra é a *projeção* da curva no "
        "eixo x. [p=0.3] Ela vai de *menos um* até *seis.* [p=0.4] {c}O domínio é o intervalo *de menos um a seis,* "
        "[p=0.2] com as pontas. [p=0.3] {d}*O domínio é a sombra no chão.*"),
    dict(id="12", block="sombras", text=
        "{t}E a *imagem?* [p=0.3] {a}Agora a lanterna fica *do lado* direito. [p=0.3] A sombra cai na *parede,* [p=0.2] no "
        "eixo y. [p=0.4] {b}Ela vai de *um* até *quatro.* [p=0.3] A imagem é o intervalo *de um a quatro.* [p=0.4] {c}E "
        "repare: [p=0.2] o ponto mais alto, o *quatro,* [p=0.2] está no *meio* da curva, [p=0.2] e não numa ponta. [p=0.4] "
        "{d}A imagem vai do ponto *mais baixo* ao *mais alto,* [p=0.2] estejam onde estiverem."),

    # ================= BLOCO E: A TABELA DE LEITURA =================
    dict(id="13", block="leitura", text=
        "{t}O que mais o ENEM pergunta sobre um gráfico? [p=0.4] {a}O *máximo* é a maior altura. [p=0.3] O *mínimo,* "
        "[p=0.2] a menor. [p=0.4] {b}Na parede: [p=0.2] máximo *quatro.* [p=0.2] No chão: [p=0.2] ele acontece em *x igual "
        "a dois.* [p=0.4] {c}Na parede: [p=0.2] mínimo *um.* [p=0.2] No chão: [p=0.2] em *x igual a menos um.*"),
    dict(id="14", block="leitura", text=
        "{t}E onde a curva sobe? [p=0.4] {a}Leia sempre da esquerda para a direita, [p=0.2] como quem anda. [p=0.3] A "
        "função é *crescente* [p=0.2] onde a curva *sobe:* [p=0.3] {b}de x igual a *menos um* até x igual a *dois.* [p=0.4] "
        "{c}E é *decrescente* onde ela *desce:* [p=0.3] {d}de x igual a *dois* até x igual a *seis.*"),
    dict(id="15", block="leitura", text=
        "{t}E os *zeros?* [p=0.3] {a}Um *zero,* [p=0.2] ou *raiz,* [p=0.2] é onde a curva *toca o chão,* [p=0.2] o eixo x. "
        "[p=0.3] {b}Aqui, [p=0.2] *não há:* [p=0.2] a curva fica toda acima. [p=0.5] {c}E quanto vale *f de quatro?* "
        "[p=0.3] {d}Fique em *x igual a quatro,* [p=0.2] suba até a curva [p=0.2] e leia a altura na parede: [p=0.3] "
        "*três.*"),

    # ================= BLOCO F: CRESCIMENTO SE DÁ EM x =================
    dict(id="16", block="emx", text=
        "{t}Lembra do gancho? [p=0.3] {a}*A função cresce entre um e quatro.* [p=0.3] Um e quatro são *alturas:* [p=0.2] "
        "estão na parede. [p=0.4] {b}A resposta certa fala do *chão:* [p=0.3] cresce para x entre *menos um* e *dois.* "
        "[p=0.4] {c}Alternativas que trocam um pelo outro [p=0.2] são distratores *frequentes.*"),
    dict(id="17", block="atalho2", text=
        "{t}E como nunca mais trocar? [p=0.3] {a}Atalho: [p=0.2] antes de responder, [p=0.2] pergunte: [p=0.2] *é "
        "pergunta de quando, [p=0.2] ou de quanto?* [p=0.4] {b}*Quando* [p=0.2] se responde no *chão,* [p=0.2] no x. "
        "[p=0.2] Onde cresce, [p=0.2] em que x acontece. [p=0.4] {c}*Quanto* [p=0.2] se responde na *parede,* [p=0.2] no y. "
        "[p=0.2] Qual é o máximo, [p=0.2] quanto vale. [p=0.3] {d}E diga o eixo em voz alta [p=0.2] *antes* do número."),

    # ================= EU FAÇO =================
    dict(id="18", block="eufaco", text=
        "{t}Agora eu leio o gráfico inteiro, [p=0.2] em voz alta, [p=0.2] como numa prova. [p=0.4] {a}Domínio: [p=0.2] "
        "sombra no chão, [p=0.2] *de menos um a seis.* [p=0.3] {b}Imagem: [p=0.2] sombra na parede, [p=0.2] *de um a "
        "quatro.* [p=0.3] {c}Máximo: [p=0.2] parede *quatro,* [p=0.2] chão *dois.* [p=0.2] Mínimo: [p=0.2] parede *um,* "
        "[p=0.2] chão *menos um.* [p=0.3] {d}Cresce: [p=0.2] chão, [p=0.2] *de menos um a dois.* [p=0.2] Decresce: "
        "[p=0.2] *de dois a seis.* [p=0.3] Cinco leituras, [p=0.2] cinco vezes o eixo antes do número."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}O gráfico de uma função é formado por *dois segmentos.* [p=0.3] O primeiro vai de *zero "
        "vírgula dois* [p=0.2] até *três vírgula cinco.* [p=0.3] O segundo vai de *três vírgula cinco* [p=0.2] até *seis "
        "vírgula menos um.* [p=0.3] As pontas estão incluídas. [p=0.4] {b}Qual é o domínio, [p=0.2] e qual é a imagem? "
        "[p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Sombra no chão: [p=0.2] o x vai de *zero* até *seis.* [p=0.2] Domínio: [p=0.2] *de "
        "zero a seis.* [p=0.4] {b}Sombra na parede: [p=0.2] o ponto mais alto é o *cinco,* [p=0.2] no meio. [p=0.3] O "
        "mais baixo é o *menos um,* [p=0.2] na ponta direita. [p=0.4] {c}Imagem: [p=0.2] *de menos um a cinco.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] régua em pé tocando duas vezes: [p=0.2] não é função. "
        "[p=0.5] {b}Dois: [p=0.2] domínio é a sombra no chão; [p=0.2] imagem é a sombra na parede. [p=0.5] {c}Três: "
        "[p=0.2] cresce e decresce se responde em x."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] ler a *imagem* no eixo *x.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque o eixo x é o primeiro que a gente olha. [p=0.4] {c}Mas a imagem são as *saídas,* [p=0.2] "
        "as alturas. [p=0.2] Ela mora na *parede.*"),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] achar que a imagem vai *de uma ponta à outra* do gráfico. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque as pontas são os pontos que mais chamam a atenção. [p=0.4] {c}No exercício que a gente fez, [p=0.2] isso "
        "daria *de menos um a dois.* [p=0.3] Mas o *cinco* está no meio. [p=0.2] O máximo pode estar *no meio.*"),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] responder o intervalo de crescimento com valores de *y.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o que *sobe* é a altura. [p=0.4] {c}Mas a pergunta é *onde* sobe. [p=0.2] É de *quando:* [p=0.2] "
        "responde-se no *x.*"),
    dict(id="25", block="erros", text=
        "{a}Quarto: [p=0.2] achar que uma reta *horizontal* cortando duas vezes [p=0.2] desqualifica a função. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque *dois cortes* lembra o teste da régua. [p=0.4] {c}Mas o teste vale só para a "
        "régua *em pé.* [p=0.2] Deitada, [p=0.2] são flechas chegando: [p=0.2] *pode.*"),

    # ================= QUESTÃO 8 (VOCÊ FAZ) =================
    dict(id="26", block="q8", text=
        "{t}E esta é *sua.* [p=0.3] {a}O gráfico de uma função f é formado por dois segmentos de reta. [p=0.3] O primeiro "
        "liga *menos dois vírgula um* [p=0.2] a *um vírgula quatro.* [p=0.3] O segundo liga *um vírgula quatro* [p=0.2] a "
        "*cinco vírgula zero.* [p=0.3] As extremidades pertencem ao gráfico. [p=0.4] {b}A imagem de f é o intervalo: "
        "[p=0.3] {qa}A: [p=0.2] de menos dois a cinco. [p=0.2] {qb}B: [p=0.2] de um a quatro. [p=0.2] {qc}C: [p=0.2] de "
        "zero a cinco. [p=0.2] {qd}D: [p=0.2] de menos dois a quatro. [p=0.2] {qe}E: [p=0.2] de zero a quatro. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="q8", text=
        "{t}Conferindo. [p=0.3] {a}Imagem é pergunta de *quanto:* [p=0.2] *parede.* [p=0.4] {b}O ponto mais alto tem y "
        "igual a *quatro.* [p=0.3] {c}E o mais baixo? [p=0.2] Cuidado: [p=0.2] não é o *um* da ponta esquerda. [p=0.3] É o "
        "*zero,* [p=0.2] no ponto *cinco vírgula zero.* [p=0.4] {d}Os segmentos não têm buracos, [p=0.2] então todas as "
        "alturas entre eles aparecem. [p=0.3] {ok}*De zero a quatro: [p=0.2] letra E!*"),
    dict(id="28", block="q8", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A é o *domínio:* [p=0.2] a sombra no chão. [p=0.4] {xb}A B olha só o *primeiro "
        "segmento.* [p=0.4] {xc}A C [p=0.2] {xd}e a D *misturam* x e y. [p=0.3] {a}A C junta o y mais baixo, [p=0.2] "
        "*zero,* [p=0.2] com o x mais à direita, [p=0.2] *cinco.* [p=0.3] A D junta o x mais à esquerda, [p=0.2] *menos "
        "dois,* [p=0.2] com o y mais alto, [p=0.2] *quatro.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] régua em pé tocando duas vezes: [p=0.2] não é "
        "função. [p=0.5] {b}Dois: [p=0.2] domínio é a sombra no chão; [p=0.2] imagem é a sombra na parede. [p=0.5] {c}Três: "
        "[p=0.2] cresce e decresce se responde em x."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}E quando não há gráfico, [p=0.2] só a fórmula? [p=0.4] {b}Em *f de x igual a um sobre x menos três,* [p=0.3] "
        "por que o *três* não pode entrar? [p=0.5] {c}E numa *caixa de papelão,* [p=0.2] por que o x não pode passar de "
        "*dez centímetros?* [p=0.5] {d}Próximo episódio: [p=0.2] domínio pela fórmula [p=0.2] e pelo contexto."),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual gráfico do seu dia a dia você mais olha? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
