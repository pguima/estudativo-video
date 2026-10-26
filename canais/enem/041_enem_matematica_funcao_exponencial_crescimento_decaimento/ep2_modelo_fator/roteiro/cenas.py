# Roteiro — Função Exponencial: crescimento e decaimento, Episódio 2 de 6: o modelo Q₀ · aᵗ, da frase do enunciado ao fator
# Base: Estudos/Enem/estudos/01-matematica/26-funcao-exponencial-crescimento-decaimento.html — seção 04 (+ quadro
#   "O que rende mais aqui" da seção 01) + Questões 3 e 6 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A lei é uma RECEITA com dois ingredientes: de onde começa (Q₀) e por quanto multiplica a cada passo (a).
#   O fator é o que SOBRA: quem perde 15% fica com 85%.
#   Juros compostos são a exponencial de TERNO E GRAVATA: M = C · (1 + i)ᵗ é Q₀ · aᵗ com outro nome.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# DESVIO DO PROMPT (exemplo NOSSO): o bloco e pedia f(0) = 3 e f(2) = 12 → a = 2, que é exatamente a montagem da
#   Questão 6 ("você faz", com pausa): sobraria só calcular f(3). Usei f(0) = 5 e f(2) = 45 → a² = 9 → a = 3
#   (confere f(1) = 15). Os pontos (0, 3) e (2, 12) só aparecem na Questão 6.
# Nós fazemos (prompt): 50 000 · 1,02ᵗ; 1,02² = 1,0404 → 52 020 habitantes.
# Tabela de tradução (t = 0, 1, 2 testados na tela): carro 60 000 · 0,85ᵗ → 60 000, 51 000, 43 350;
#   bactérias 500 · 3ᵗ → 500, 1 500, 4 500; população 200 000 · 1,03ᵗ; juros 1 000 · 1,02ᵗ.
# QUESTÃO 3 (texto idêntico ao material): razões 40/50 = 32/40 = 25,6/32 = 0,8; Q₀ = 50 000 → E.
#   Erradas (material): A acerta t = 0 e t = 1, mas dá 30 000 em t = 2; B usa a taxa de perda (0,2) como fator;
#   C começa em 40 000; D (0,8t, produto) dá 0 em t = 0.
# QUESTÃO 6 (texto idêntico): k = 3; 3a² = 12 → a = 2; f(3) = 3 · 2³ = 24 → C.
#   Erradas (material): A 16,5 = reta (inclinação 4,5); B 18 = 3 · 2 · 3; D 36 = supõe a = 3 (12 · 3);
#   E 48 = multiplica 12 por a² = 4 (dois passos onde só há um).
# Atalhos (verde): taxa vira fator (ganhou: 1 + taxa · perdeu: 1 − taxa · dobrou: 2 · triplicou: 3) ·
#   o teste do t = 0 (a lei tem que devolver o valor inicial) · dois pontos: divida um pelo outro ·
#   1,02² = 1 + 0,04 + 0,0004 (o quadrado da série de Juros compostos).
# Contas conferidas em trabalho/conferir_contas.py.
# Frases-chave (meio e fim, idênticas): 1. Com o valor inicial e o fator, a lei sai sozinha.
#   2. O fator é o que sobra: perder 15% é multiplicar por 0,85. 3. Juros compostos são a mesma exponencial com outro nome.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Função exponencial: da frase do enunciado à lei Q₀ · aᵗ | Função Exponencial Ep. 2"
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
        "{a}Um carro de *sessenta mil reais* [p=0.2] perde *quinze por cento* do valor por ano. [p=0.4] {b}Quem "
        "multiplica por *zero vírgula quinze* [p=0.2] conclui que, depois de um ano, [p=0.2] ele vale *nove mil reais.* "
        "[p=0.4] {c}O certo é *cinquenta e um mil reais.* [p=0.4] {d}Um número errado na lei [p=0.2] e a questão inteira "
        "*vai embora.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai transformar qualquer frase de enunciado: [p=0.2] *dobra,* [p=0.2] "
        "*cresce três por cento,* [p=0.2] *perde quinze por cento,* [p=0.3] {b}numa *lei* pronta para usar."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Da série de Porcentagem: [p=0.2] aumentar *i* por cento [p=0.2] "
        "é multiplicar por *um mais i;* [p=0.2] descontar, [p=0.2] por *um menos i.* [p=0.4] {b}E, da série de Juros "
        "compostos: [p=0.2] *M igual a C vezes um mais i, elevado a t.* [p=0.3] Ela vai voltar *disfarçada.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Três histórias. [p=0.3] {a}Um *carro* que perde valor todo ano. [p=0.3] {b}Uma *cidade* que cresce todo "
        "ano. [p=0.3] {c}*Bactérias* que triplicam a cada hora. [p=0.4] {d}Em comum: [p=0.2] a cada passo do tempo, "
        "[p=0.2] o valor é *multiplicado pelo mesmo número.* [p=0.2] A escada do episódio passado."),

    # ================= BLOCO A: A LEI GERAL =================
    dict(id="05", block="lei", text=
        "{t}E como se escreve isso numa linha só? [p=0.4] {a}Com uma *lei:* [p=0.2] a fórmula que dá o valor em cada "
        "instante. [p=0.4] {b}Q de t [p=0.2] igual a *Q zero* [p=0.2] vezes *a elevado a t.* [p=0.4] {c}*Q zero* é o "
        "*valor inicial:* [p=0.2] quanto vale no instante zero. [p=0.4] {d}E o *a* é o *fator:* [p=0.2] o número que "
        "multiplica o valor a cada passo do tempo. [p=0.4] {e}Uma *receita* com dois ingredientes: [p=0.2] de onde "
        "começa, [p=0.2] e por quanto multiplica a cada passo."),
    dict(id="06", block="lei", text=
        "{t}E o fator já conta o fim da história? [p=0.3] {a}Fator *maior que um:* [p=0.2] cada passo aumenta: [p=0.2] "
        "*crescimento.* [p=0.4] {b}Fator *entre zero e um:* [p=0.2] cada passo diminui: [p=0.2] *decaimento.* [p=0.2] "
        "Se é um bem perdendo valor, [p=0.2] *depreciação.*"),

    # ================= BLOCO B: A TABELA DE TRADUÇÃO =================
    dict(id="07", block="traducao", text=
        "{t}E como sai o fator da frase? [p=0.4] {a}Uma população de *duzentos mil* [p=0.2] cresce *três por cento* ao "
        "ano. [p=0.4] {b}Esses três por cento são a *taxa:* [p=0.2] a porcentagem que muda a cada passo. [p=0.4] "
        "{c}Cresce: [p=0.2] um *mais* zero vírgula zero três. [p=0.2] Fator *um vírgula zero três.* [p=0.4] {d}A lei: "
        "[p=0.2] *P igual a duzentos mil vezes um vírgula zero três elevado a t.*"),
    dict(id="08", block="traducao", text=
        "{t}Agora o carro, [p=0.2] que perde quinze por cento ao ano. [p=0.4] {a}Da barra de cem por cento, [p=0.2] sai "
        "um pedaço de quinze. [p=0.4] {b}O que *sobra?* [p=0.3] *Oitenta e cinco por cento.* "
        "[p=0.2] Fator *zero vírgula oitenta e cinco.* [p=0.4] {c}A lei: [p=0.2] *V igual a sessenta mil vezes zero "
        "vírgula oitenta e cinco elevado a t.* [p=0.4] {d}Teste: [p=0.2] t igual a zero, [p=0.2] sessenta mil. [p=0.3] "
        "{e}t igual a um, [p=0.2] *cinquenta e um mil.* [p=0.3] {f}t igual a dois, [p=0.2] quarenta e três mil, "
        "trezentos e cinquenta."),
    dict(id="09", block="traducao", text=
        "{t}*Quinhentas* bactérias que *triplicam* a cada hora? [p=0.3] {a}Fator *três.* [p=0.3] {b}A lei: [p=0.2] "
        "*N igual a quinhentos vezes três elevado a t.* [p=0.3] {c}Quinhentas, [p=0.2] mil e quinhentas, [p=0.2] "
        "quatro mil e quinhentas."),

    # ================= BLOCO C: JUROS COMPOSTOS DISFARÇADOS =================
    dict(id="10", block="disfarce", text=
        "{t}E *mil reais* a juros compostos de *dois por cento* ao mês? [p=0.4] {a}Fator um vírgula zero dois. "
        "[p=0.2] Lei: [p=0.2] *M igual a mil vezes um vírgula zero dois elevado a t.* [p=0.4] {b}Já viu isso? [p=0.3] "
        "É a fórmula da série de Juros compostos. [p=0.4] {c}Tire a fantasia: [p=0.2] o *C* é o Q zero, [p=0.2] e o *um "
        "mais i* é o fator. [p=0.4] {d}Juros compostos são a exponencial de *terno e gravata.*"),

    # ================= ATALHO: TAXA VIRA FATOR =================
    dict(id="11", block="atalho", text=
        "{t}Atalho para traduzir sem pensar. [p=0.3] {a}*Ganhou,* [p=0.2] um mais a taxa. [p=0.2] *Perdeu,* [p=0.2] "
        "um menos a taxa. [p=0.2] *Dobrou,* [p=0.2] dois. [p=0.2] *Triplicou,* [p=0.2] três. [p=0.4] {b}E confira com "
        "*t igual a zero:* [p=0.2] elevado a zero dá um, [p=0.2] então a lei tem que devolver o *valor inicial.*"),

    # ================= BLOCO D: O FATOR É O QUE SOBRA =================
    dict(id="12", block="sobra", text=
        "{t}E se você copiar o número da frase? [p=0.4] {a}Zero vírgula quinze: [p=0.2] o carro ficaria com *quinze por "
        "cento* do preço. [p=0.3] {b}Fator três: [p=0.2] a cidade *triplicaria.* [p=0.3] {c}Zero vírgula zero três: "
        "[p=0.2] *encolheria.* [p=0.3] {d}O fator é o que *sobra.*"),

    # ================= BLOCO E: DOIS PONTOS =================
    dict(id="13", block="pontos", text=
        "{t}E se a questão der só dois valores da função? [p=0.4] {a}Exemplo: [p=0.2] f de zero igual a *cinco* "
        "[p=0.2] e f de dois igual a *quarenta e cinco.* [p=0.4] {b}f de zero é o começo: [p=0.2] *Q zero é cinco.* "
        "[p=0.4] {c}f de dois: [p=0.2] cinco vezes *a ao quadrado* [p=0.2] igual a quarenta e cinco. [p=0.3] {d}Divida "
        "por cinco: [p=0.2] a ao quadrado, *nove.* [p=0.3] {e}a igual a *três,* [p=0.2] porque a base é sempre "
        "positiva."),
    dict(id="14", block="pontos", text=
        "{t}O atalho: [p=0.2] {a}*divida um valor pelo outro.* [p=0.2] Quarenta e cinco por cinco, [p=0.2] nove. "
        "[p=0.3] {b}De zero até dois são *dois passos:* [p=0.2] a vezes a. [p=0.4] {c}Lei: [p=0.2] *cinco vezes três "
        "elevado a x.* [p=0.2] Quinze, [p=0.2] quarenta e cinco. [p=0.2] Bateu."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma cidade de *cinquenta mil* habitantes [p=0.2] cresce *dois por cento* ao ano. "
        "[p=0.3] Escreva a lei [p=0.2] e calcule a população daqui a dois anos. [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Começa em cinquenta mil; [p=0.2] cresce dois por cento: [p=0.2] fator *um vírgula "
        "zero dois.* [p=0.2] *P igual a cinquenta mil vezes um vírgula zero dois elevado a t.* [p=0.4] {b}Dois anos: "
        "[p=0.2] um vírgula zero dois ao quadrado. [p=0.2] Atalho da série de Juros: [p=0.2] um, [p=0.2] mais zero "
        "vírgula zero quatro, [p=0.2] mais zero vírgula zero zero zero quatro: [p=0.2] *um vírgula zero quatro zero "
        "quatro.* [p=0.4] {c}Vezes cinquenta mil: [p=0.2] *cinquenta e dois mil e vinte* habitantes."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] com o valor inicial e o fator, a lei sai sozinha. "
        "[p=0.5] {b}Dois: [p=0.2] o fator é o que sobra: [p=0.2] perder quinze por cento é multiplicar por zero "
        "vírgula oitenta e cinco. [p=0.5] {c}Três: [p=0.2] juros compostos são a mesma exponencial com outro nome."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] perde quinze por cento, [p=0.2] fator *zero vírgula "
        "quinze.* [p=0.3] {b}Parece certo, [p=0.2] porque o quinze está no enunciado. [p=0.3] {c}Mas o fator é o que "
        "sobra: [p=0.2] *zero vírgula oitenta e cinco.*"),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] cresce três por cento, [p=0.2] fator *três.* [p=0.3] {b}Parece certo, [p=0.2] porque é o "
        "número da frase. [p=0.3] {c}Mas fator três é *triplicar.* [p=0.2] A taxa vira fator *somando um:* [p=0.2] um "
        "vírgula zero três."),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] três vezes dois elevado a x [p=0.2] virar *seis* elevado a x. [p=0.3] {b}Parece certo, "
        "[p=0.2] porque três vezes dois é seis. [p=0.3] {c}Mas a potência vem *antes.* [p=0.2] Com x igual a dois: "
        "[p=0.2] três vezes quatro, [p=0.2] *doze;* [p=0.2] seis ao quadrado, [p=0.2] *trinta e seis.* [p=0.2] O "
        "número da frente *não entra na base.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="21", block="q3", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Esta, [p=0.2] eu resolvo "
        "com você. [p=0.4] {a}O valor de mercado de uma *máquina agrícola* [p=0.2] nos anos após a compra: [p=0.2] "
        "*cinquenta mil,* [p=0.2] *quarenta mil,* [p=0.2] *trinta e dois mil* [p=0.2] e *vinte e cinco mil e "
        "seiscentos* reais. [p=0.4] {b}Qual expressão serve para todos os dados? [p=0.4] {qa}A: [p=0.2] cinquenta "
        "mil menos dez mil t. [p=0.3] {qb}B: [p=0.2] cinquenta mil, [p=0.2] zero vírgula dois elevado a t. [p=0.3] "
        "{qc}C: [p=0.2] quarenta mil, [p=0.2] zero vírgula oito elevado a t. [p=0.3] {qd}D: [p=0.2] zero vírgula oito "
        "*vezes* t. [p=0.3] {qe}E: [p=0.2] cinquenta mil, [p=0.2] zero vírgula oito elevado a t."),
    dict(id="22", block="q3", text=
        "{t}Primeiro, o fator: [p=0.2] {a}divida cada valor pelo anterior. [p=0.2] Quarenta sobre cinquenta, [p=0.2] "
        "*zero vírgula oito.* [p=0.2] {b}Trinta e dois sobre quarenta, [p=0.2] zero vírgula oito. [p=0.2] {c}E o "
        "último, [p=0.2] também. [p=0.3] {d}Sempre o mesmo: [p=0.2] *exponencial,* [p=0.2] perdendo *vinte por cento* "
        "ao ano. [p=0.4] {e}Em t igual a zero, [p=0.2] cinquenta mil. [p=0.2] A lei: [p=0.2] cinquenta mil vezes zero "
        "vírgula oito elevado a t. [p=0.3] {ok}*Letra E!*"),
    dict(id="23", block="q3", text=
        "{t}E as outras? [p=0.3] {xa}A A [p=0.2] acerta os dois primeiros, [p=0.2] mas em t igual a dois dá *trinta "
        "mil:* [p=0.2] uma reta não serve. [p=0.4] {xb}A B [p=0.2] usa a *taxa de perda,* [p=0.2] zero vírgula dois, "
        "[p=0.2] como fator. [p=0.4] {xc}A C [p=0.2] começa em *quarenta mil:* [p=0.2] falha no teste do zero. "
        "[p=0.4] {xd}E a D [p=0.2] escreve zero vírgula oito *vezes* t: [p=0.2] em t igual a zero, [p=0.2] dá "
        "*zero.*"),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="24", block="q6", text=
        "{t}E esta é *sua.* [p=0.3] {a}O gráfico de *f de x igual a k vezes a elevado a x,* [p=0.2] com k e a "
        "positivos, [p=0.2] passa pelos pontos *zero, três* [p=0.2] e *dois, doze.* [p=0.2] O valor de *f de três* é: "
        "[p=0.4] {qa}A: [p=0.2] dezesseis vírgula cinco. [p=0.3] {qb}B: [p=0.2] dezoito. [p=0.3] {qc}C: [p=0.2] vinte "
        "e quatro. [p=0.3] {qd}D: [p=0.2] trinta e seis. [p=0.3] {qe}E: [p=0.2] quarenta e oito. [p=0.5] {p}*Pause o "
        "vídeo e resolva.* [p=2.0]"),
    dict(id="25", block="q6", text=
        "{t}Conferindo. [p=0.3] {a}f de zero é o valor inicial: [p=0.2] *k igual a três.* [p=0.4] {b}Três vezes a ao "
        "quadrado igual a doze: [p=0.2] a ao quadrado, quatro; [p=0.2] *a igual a dois.* [p=0.4] {c}f de três: "
        "[p=0.2] três vezes *dois ao cubo.* [p=0.2] Primeiro a potência, oito; [p=0.2] vezes três, [p=0.2] *vinte e "
        "quatro.* [p=0.3] {d}Confira: [p=0.2] de doze, um passo, vezes dois: [p=0.2] vinte e quatro. [p=0.3] "
        "{ok}*Letra C!*"),
    dict(id="26", block="q6", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] ligou os pontos por uma *reta.* [p=0.3] {xb}A B [p=0.2] trocou a "
        "potência por um produto: [p=0.2] três vezes dois vezes três. [p=0.3] {xd}A D [p=0.2] supôs *a igual a três.* "
        "[p=0.3] {xe}E a E [p=0.2] multiplicou doze por quatro, [p=0.2] como se de dois para três houvesse *dois "
        "passos.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] com o valor inicial e o fator, a lei sai "
        "sozinha. [p=0.5] {b}Dois: [p=0.2] o fator é o que sobra: [p=0.2] perder quinze por cento é multiplicar por "
        "zero vírgula oitenta e cinco. [p=0.5] {c}Três: [p=0.2] juros compostos são a mesma exponencial com outro "
        "nome."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}*Mil bactérias* [p=0.2] que dobram a cada *trinta minutos:* [p=0.3] {b}depois de três horas, [p=0.2] são "
        "*seis mil?* [p=0.5] {c}Nem perto. [p=0.4] {d}Próximo episódio: [p=0.2] duplicação e meia-vida."),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído no fator zero vírgula quinze? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
