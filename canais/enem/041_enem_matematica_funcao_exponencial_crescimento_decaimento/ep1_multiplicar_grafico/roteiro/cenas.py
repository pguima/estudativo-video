# Roteiro — Função Exponencial, Episódio 1 de 6: multiplicar em vez de somar, a função exponencial e seu gráfico
# Base: Estudos/Enem/estudos/01-matematica/26-funcao-exponencial-crescimento-decaimento.html — seções 02 e 03 + Questão 9.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   AS DUAS ESCADAS: a afim é uma escada de degraus iguais (soma sempre o mesmo); a exponencial é uma escada em que cada
#     degrau é o anterior multiplicado pelo mesmo fator.
#   VIRE DE CABEÇA PARA BAIXO: expoente negativo inverte, não põe sinal de menos no resultado (2⁻² = 1/4, positivo).
#   A PAREDE INVISÍVEL: a assíntota; a curva chega cada vez mais perto e nunca encosta.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Modelo Q₀ · aᵗ, meia-vida e equações: ficam para os próximos episódios (não aparecem aqui).
# DESVIO DO PROMPT: o bloco g pedia o exemplo y = 25 + 65 · 0,8ᵗ, que é exatamente a função da Questão 9 (com "pause o
#   vídeo e tente") e entregaria a resposta 25. O bloco g usa um exemplo NOSSO com o mesmo raciocínio: a sopa numa
#   cozinha a 22 °C, T = 22 + 70 · 0,5ᵗ → assíntota 22. O coeficiente usa 5 · 2ˣ → corta em (0, 5) (não 3 · 2ˣ, que é
#   o tema da Q6 do episódio 2).
# Concretos (regra 1): mesada que dobra (1, 2, 4, 8), boato em que cada um conta para 3 (1, 3, 9, 27), café esfriando
#   (só a intuição "rápido no começo, devagar depois"; a temperatura final fica para a Q9).
# Nós fazemos (prompt): tabela de 3ˣ para x = −2..2 → 1/9, 1/3, 1, 3, 9.
# Erros (prompt): 2⁻³ = −8 (certo 1/8) · achar que a curva encosta no eixo x.
# QUESTÃO 9 ("nós fazemos", com pausa): gabarito A (25 °C). Erradas = material (B 40 subtrai os dois números; C 65 é a
#   diferença inicial; D 77 é T(1) = 25 + 52; E 90 é T(0)).
# Acréscimos NOSSOS (marcados): três cenas verdes de ATALHO — "comece pelo 1 no x = 0; direita × base, esquerda ÷ base"
#   (cena 10), "três pontos bastam: x = −1, 0, 1" (cena 14) e "tempo grande com base entre 0 e 1: apague a potência; o
#   número somado sozinho é a assíntota" (cena 17).
# Frases-chave (meio e fim, idênticas): 1. Na exponencial, cada passo multiplica pelo mesmo fator.
#   2. Base maior que 1 sobe; base entre 0 e 1 desce; todas passam por (0, 1).
#   3. A exponencial nunca chega a zero: ela só se aproxima da assíntota.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Função exponencial do zero: multiplicar em vez de somar e o gráfico | Função Exponencial Ep. 1"
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
        "{a}Uma *mesada de um real* [p=0.2] que *dobra* toda semana. [p=0.5] {b}Em dez semanas, [p=0.2] *mil e vinte e "
        "quatro reais.* [p=0.5] {c}Em vinte semanas, [p=0.2] *mais de um milhão:* [p=0.2] dois elevado a vinte [p=0.2] é "
        "um milhão, quarenta e oito mil, quinhentos e setenta e seis. [p=0.5] {d}Somar nunca faria isso. [p=0.3] "
        "*Multiplicar faz.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o primeiro episódio da série de *Função exponencial.* [p=0.4] {a}Ao final, [p=0.2] você vai "
        "*reconhecer uma função exponencial,* [p=0.3] {b}saber por que a base tem *restrições* [p=0.3] {c}e *desenhar o "
        "gráfico* dela sem decorar nada."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos, da série de Potenciação. [p=0.3] {a}Qualquer base diferente de zero, [p=0.2] elevada "
        "a *zero,* [p=0.2] dá *um.* [p=0.4] {b}E expoente *negativo* [p=0.2] *inverte* a base: [p=0.2] dois elevado a "
        "menos dois [p=0.2] é um sobre dois ao quadrado, [p=0.2] *um quarto.* [p=0.4] {c}E, da série de Conceito de "
        "Função: [p=0.2] função é uma máquina. [p=0.2] *Entra x, sai y.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Repare em três coisas do dia a dia. [p=0.4] {a}A *mesada* que dobra: [p=0.2] um, dois, quatro, oito. "
        "[p=0.4] {b}Um *boato* no grupo de mensagens, [p=0.2] em que cada pessoa conta para *três:* [p=0.2] um, três, "
        "nove, vinte e sete. [p=0.4] {c}E um *café* esfriando na mesa: [p=0.2] rápido no começo, [p=0.2] cada vez mais "
        "devagar. [p=0.4] {d}Nas três, [p=0.2] cada passo *multiplica* pelo mesmo número."),

    # ================= BLOCO A: SOMAR × MULTIPLICAR =================
    dict(id="05", block="escadas", text=
        "{t}Qual é a diferença entre *somar* e *multiplicar* a cada passo? [p=0.4] {a}A função afim é uma escada de "
        "*degraus iguais:* [p=0.2] soma dois, soma dois, soma dois. [p=0.4] {b}Na exponencial, [p=0.2] cada degrau é o "
        "anterior *multiplicado* pelo mesmo número. [p=0.4] {c}Esse número se chama *fator.* [p=0.4] {d}Com fator dois, "
        "[p=0.2] em poucos passos [p=0.2] a segunda escada *sai da tela.*"),

    # ================= BLOCO B: DEFINIÇÃO =================
    dict(id="06", block="definicao", text=
        "{t}Então, o que é uma função exponencial? [p=0.4] {a}É toda função *f de x igual a a elevado a x.* [p=0.4] "
        "{b}O *a* é a *base:* [p=0.2] o número que se multiplica. [p=0.3] O *x* é o *expoente:* [p=0.2] quantas vezes. "
        "[p=0.4] {c}O detalhe que muda tudo: [p=0.2] a variável está *no expoente.* [p=0.4] {d}Em x ao quadrado, "
        "[p=0.2] ela está na base. [p=0.2] *Isso não é exponencial.*"),

    # ================= BLOCO C: AS RESTRIÇÕES =================
    dict(id="07", block="restricoes", text=
        "{t}E por que a base tem *regras?* [p=0.4] {a}Ela precisa ser *positiva* [p=0.2] e *diferente de um.* [p=0.4] "
        "{b}Com base *um,* [p=0.2] um elevado a qualquer coisa dá *um.* [p=0.2] A função ficaria parada, [p=0.2] "
        "*constante.* [p=0.4] {c}Com base *negativa,* [p=0.2] apareceriam contas como menos quatro elevado a um meio: "
        "[p=0.2] a *raiz de menos quatro,* [p=0.2] que não é um número real. [p=0.4] {d}A função ficaria *cheia de "
        "buracos.*"),

    # ================= BLOCO D: AS TABELAS =================
    dict(id="08", block="tabela", text=
        "{t}Vamos montar uma tabela. [p=0.3] {a}Dois elevado a x, [p=0.2] de menos dois até três. [p=0.4] {b}No zero, "
        "[p=0.2] *um.* [p=0.3] {c}Para a direita, [p=0.2] *vezes dois:* [p=0.2] dois, quatro, oito. [p=0.4] {d}Para a "
        "esquerda, [p=0.2] *dividido por dois:* [p=0.2] um meio, [p=0.2] um quarto."),
    dict(id="09", block="tabela", text=
        "{t}E com base *um meio?* [p=0.4] {a}No zero, [p=0.2] de novo *um.* [p=0.3] {b}Para a direita, [p=0.2] *vezes um "
        "meio:* [p=0.2] um meio, um quarto, um oitavo. [p=0.4] {c}Para a esquerda, [p=0.2] o contrário: [p=0.2] dois, "
        "quatro. [p=0.4] {d}Repare: [p=0.2] é a mesma lista, [p=0.2] *de trás para a frente.*"),
    dict(id="10", block="atalho_tab", text=
        "{t}Atalho para montar qualquer tabela. [p=0.4] {a}Comece pelo *um,* [p=0.2] no x igual a zero. [p=0.4] "
        "{b}Andou uma coluna para a direita? [p=0.2] *Multiplique pela base.* [p=0.4] {c}Voltou uma coluna? [p=0.2] "
        "*Divida pela base.* [p=0.4] {d}Sem calcular nenhuma potência."),

    # ================= BLOCO E: SEMPRE POSITIVO =================
    dict(id="11", block="positivo", text=
        "{t}Apareceu algum número *negativo* nas tabelas? [p=0.4] {a}*Nenhum.* [p=0.2] Nem o zero. [p=0.4] {b}Multiplicar "
        "ou dividir um número positivo [p=0.2] por outro positivo [p=0.2] *nunca* dá negativo. [p=0.4] {c}A *imagem* é o "
        "conjunto dos valores que *saem* da função. [p=0.3] Aqui, [p=0.2] *todos os números maiores que zero.*"),

    # ================= BLOCO F: O GRÁFICO =================
    dict(id="12", block="grafico", text=
        "{t}E como fica o desenho? [p=0.4] {a}Marque os pontos da tabela de dois elevado a x. [p=0.4] {b}A curva sobe "
        "[p=0.2] cada vez mais rápido. [p=0.3] É *crescente:* [p=0.2] x aumenta, [p=0.2] y aumenta. [p=0.4] {c}Para a "
        "esquerda, [p=0.2] ela vai *grudando* no eixo x, [p=0.2] sem tocar."),
    dict(id="13", block="grafico", text=
        "{t}E a base um meio? [p=0.4] {a}Os mesmos números, [p=0.2] ao contrário: [p=0.2] a curva *desce.* [p=0.3] É "
        "*decrescente.* [p=0.4] {b}As duas passam pelo ponto *zero, um,* [p=0.2] porque qualquer base elevada a zero "
        "[p=0.2] dá um. [p=0.4] {c}E uma é o *espelho* da outra: [p=0.2] um meio elevado a x [p=0.2] é dois elevado a "
        "menos x."),
    dict(id="14", block="atalho_graf", text=
        "{t}Atalho para desenhar sem tabela grande. [p=0.4] {a}Marque *três pontos:* [p=0.2] x igual a menos um, [p=0.2] "
        "zero [p=0.2] e um. [p=0.4] {b}Base maior que um: [p=0.2] o da direita fica mais alto, [p=0.2] a curva *sobe.* "
        "[p=0.3] Base entre zero e um: [p=0.2] fica mais baixo, [p=0.2] a curva *desce.* [p=0.4] {c}Depois, [p=0.2] ligue "
        "com uma curva suave."),

    # ================= BLOCO G: A ASSÍNTOTA =================
    dict(id="15", block="assintota", text=
        "{t}A curva *encosta* no eixo x? [p=0.4] {a}*Nunca.* [p=0.3] O eixo x é uma *assíntota horizontal:* [p=0.2] uma "
        "reta da qual a curva chega cada vez mais perto, [p=0.2] *sem nunca tocar.* [p=0.4] {b}Pense numa *parede "
        "invisível.* [p=0.3] Um meio, um quarto, um oitavo, um dezesseis avos: [p=0.2] encolhe sempre, [p=0.2] e *nunca "
        "vira zero.*"),
    dict(id="16", block="coef", text=
        "{t}E quando vêm outros números junto? [p=0.4] {a}O número que *multiplica* a potência [p=0.2] se chama "
        "*coeficiente.* [p=0.3] Em cinco vezes dois elevado a x, [p=0.2] a curva corta o eixo vertical no *cinco,* "
        "[p=0.2] e não no um. [p=0.4] {b}E um número *somado* [p=0.2] *levanta a parede.* [p=0.3] Uma sopa numa cozinha a "
        "vinte e dois graus: [p=0.2] T igual a vinte e dois [p=0.2] mais setenta vezes zero vírgula cinco elevado a t. "
        "[p=0.4] {c}A potência vai sumindo, [p=0.2] e a sopa se aproxima de *vinte e dois graus,* [p=0.2] a temperatura da "
        "cozinha. [p=0.3] A assíntota *subiu* para vinte e dois."),
    dict(id="17", block="atalho_ass", text=
        "{t}Atalho para achar essa parede. [p=0.4] {a}Base entre zero e um, [p=0.2] e o tempo crescendo? [p=0.4] "
        "{b}*Apague a potência.* [p=0.3] Ela vira quase zero. [p=0.4] {c}O número *somado sozinho* [p=0.2] é a assíntota."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Complete a tabela de *três elevado a x,* [p=0.2] para x de menos dois até dois. [p=0.4] "
        "{b}Use o atalho: [p=0.2] comece pelo um. [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}No zero, [p=0.2] *um.* [p=0.3] {b}Para a direita, [p=0.2] vezes três: [p=0.2] *três* "
        "[p=0.2] e *nove.* [p=0.4] {c}Para a esquerda, [p=0.2] dividido por três: [p=0.2] *um terço* [p=0.2] e *um nono.* "
        "[p=0.4] {d}Nenhum negativo. [p=0.2] E o gráfico *sobe,* [p=0.2] porque a base é maior que um."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] na exponencial, [p=0.2] cada passo multiplica pelo mesmo "
        "fator. [p=0.5] {b}Dois: [p=0.2] base maior que um sobe; [p=0.2] base entre zero e um desce; [p=0.2] todas passam "
        "por zero, um. [p=0.5] {c}Três: [p=0.2] a exponencial nunca chega a zero: [p=0.2] ela só se aproxima da "
        "assíntota."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dizer que dois elevado a menos três [p=0.2] é "
        "*menos oito.* [p=0.4] {b}Parece certo, [p=0.2] porque o sinal de menos *está ali,* [p=0.2] e a gente leva ele "
        "para o resultado. [p=0.4] {c}Mas expoente negativo é um *vire de cabeça para baixo,* [p=0.2] não um sinal de "
        "menos: [p=0.2] *um oitavo,* [p=0.2] positivo."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] achar que a curva *encosta* no eixo x [p=0.2] em algum momento. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque no desenho ela fica tão colada [p=0.2] que *parece* tocar. [p=0.4] {c}Mas a metade de um número "
        "positivo [p=0.2] ainda é positiva. [p=0.2] A parede é *invisível,* [p=0.2] e *nunca* é tocada."),

    # ================= QUESTÃO 9 (NÓS FAZEMOS) =================
    dict(id="23", block="q9", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] a gente resolve *junto.* [p=0.4] {a}Uma xícara "
        "de café é deixada sobre a mesa [p=0.2] de uma sala climatizada. [p=0.3] A temperatura dela, [p=0.2] em graus "
        "Celsius, [p=0.2] t minutos depois, [p=0.2] é T de t igual a vinte e cinco, [p=0.2] mais sessenta e cinco vezes "
        "zero vírgula oito elevado a t. [p=0.3] Com o tempo, [p=0.2] a temperatura do café se aproxima de: [p=0.3] "
        "{qa}A: [p=0.2] vinte e cinco graus. [p=0.2] {qb}B: [p=0.2] quarenta. [p=0.2] {qc}C: [p=0.2] sessenta e cinco. "
        "[p=0.2] {qd}D: [p=0.2] setenta e sete. [p=0.2] {qe}E: [p=0.2] noventa. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="24", block="q9", text=
        "{t}Vamos juntos. [p=0.3] {a}A base é *zero vírgula oito,* [p=0.2] entre zero e um. [p=0.2] Então a potência "
        "*encolhe:* [p=0.2] zero vírgula oito, [p=0.2] zero vírgula sessenta e quatro, [p=0.2] zero vírgula quinhentos e "
        "doze. [p=0.4] {b}A parcela sessenta e cinco vezes a potência [p=0.2] *desaparece aos poucos.* [p=0.4] {c}Sobra "
        "*vinte e cinco,* [p=0.2] a temperatura da sala. [p=0.2] É a *assíntota.* [p=0.3] {ok}*Letra A!*"),
    dict(id="25", block="q9", text=
        "{t}E as armadilhas? [p=0.3] {xb}A B *subtrai* os dois números do modelo. [p=0.4] {xc}A C é o sessenta e cinco, "
        "[p=0.2] a *diferença inicial* entre o café e a sala. [p=0.4] {xd}A D é a temperatura depois de *um minuto:* "
        "[p=0.2] vinte e cinco mais cinquenta e dois. [p=0.4] {xe}E a E é a temperatura *inicial:* [p=0.2] vinte e cinco "
        "mais sessenta e cinco."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] na exponencial, [p=0.2] cada passo multiplica pelo "
        "mesmo fator. [p=0.5] {b}Dois: [p=0.2] base maior que um sobe; [p=0.2] base entre zero e um desce; [p=0.2] todas "
        "passam por zero, um. [p=0.5] {c}Três: [p=0.2] a exponencial nunca chega a zero: [p=0.2] ela só se aproxima da "
        "assíntota."),

    # ================= PONTE E CTA =================
    dict(id="27", block="ponte", text=
        "{a}Um carro de *sessenta mil reais* [p=0.2] perde *quinze por cento* do valor por ano. [p=0.4] {b}Para achar o "
        "preço do ano seguinte, [p=0.2] você multiplica por *zero vírgula quinze* [p=0.2] ou por *zero vírgula oitenta e "
        "cinco?* [p=0.4] {c}Próximo episódio."),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] onde mais você já viu alguma coisa crescer *multiplicando?* "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
