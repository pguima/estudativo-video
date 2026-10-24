# Roteiro — Função Afim, Episódio 3 de 5: o gráfico (crescente, decrescente, constante) e a lei a partir de dois pontos
# Base: Estudos/Enem/estudos/01-matematica/24-funcao-afim-grafico-coeficientes.html — seções 05 e 06 + Questões 6 e 5 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A ESCADA: cada degrau anda 1 para a direita e sobe a (ou desce, se a for negativo).
#   ONDE NASCE / PARA ONDE APONTA: o b é onde a reta nasce no eixo vertical; o a é para onde ela aponta.
#   OS DOIS PREGOS: dois pontos bastam, como dois pregos seguram uma régua.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Tangente do ângulo, declividade e paralelas/perpendiculares: só citados (cena 15), têm série própria em Geometria Analítica.
# Gancho (nosso desenho): esquerda y de 0 a 10 em x de 0 a 5 (a = 2, desenhada íngreme); direita y de 0 a 50 com eixo
#   até 100 (a = 10, desenhada mais deitada). O bloco c faz as duas contas.
# Bloco d e e = exemplo do material (2, 11) e (5, 20) → f(x) = 3x + 5 (o prompt pede; não é questão).
# DESVIO DO PROMPT: o bloco f pedia a escala E do material, (0, 10) e (100, 60) → E = 0,5C + 10, que é exatamente a lei
#   da Questão 5 ("você faz"). Para não entregar a Q5, o bloco f deduz a fórmula que o aluno já conhece:
#   (0, 32) e (100, 212) → F = 1,8C + 32 ("é o mesmo raciocínio que gera F = 1,8C + 32", como diz o material).
# Nós fazemos (prompt): (1, 4) e (3, 10) → a = 3, b = 1, f(x) = 3x + 1; conferência 3 · 3 + 1 = 10.
# Erros com exemplos NOSSOS: erro 1 = reta que nasce em 5 e sobe 2 por degrau, escrita 5x + 2 (o certo é 2x + 5);
#   erro 2 = os dois gráficos do gancho; erro 3 = (0, 2) e (2, 8): Δx/Δy = 2/6 = 1/3 em vez de 3; a conferência pega
#   (f(2) daria 2,67, não 8).
# QUESTÃO 6 ("eu faço", com pausa): gabarito A (2x − 3). Erradas = material (B troca a e b; C inverte a fração;
#   D erra o sinal de b; E erra o sinal de a).
# QUESTÃO 5 ("você faz", com pausa): gabarito B (28,5 °E). Erradas = material (A esquece o b: 0,5 · 37 = 18,5;
#   C soma 10 sem a taxa: 47; D inverte a taxa e esquece o b: 2 · 37 = 74; E inverte a taxa e soma o b: 84).
# Acréscimos NOSSOS (marcados): atalho verde "leia o gráfico em duas olhadas" (cena 08: onde corta = b; um degrau = a);
#   atalho verde "o quarto passo é o seguro" (cena 12: o ponto que não usou confere a lei).
# Frases-chave (meio e fim, idênticas): 1. a positivo sobe; a negativo desce; a zero fica deitado.
#   2. b é onde a reta corta o eixo vertical. 3. Dois pontos dão a lei; o terceiro dado confere.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Gráfico da função afim e a lei por dois pontos · Matemática ENEM, Função afim episódio 3"

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
        "{a}Dois gráficos de reta, [p=0.2] lado a lado: [p=0.3] o da esquerda parece *muito mais íngreme.* [p=0.5] "
        "{b}Mas, quando você lê os eixos, [p=0.2] o da direita *sobe mais rápido.* [p=0.5] {c}Olho engana; [p=0.3] "
        "*conta não.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Função afim.* [p=0.4] {a}Ao final, [p=0.2] você vai ler no gráfico "
        "o *sinal de a* [p=0.2] e o *valor de b* [p=0.3] {b}e escrever a *lei de qualquer reta* a partir de *dois "
        "pontos,* [p=0.3] {c}conferindo no fim."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Da série de Conceito de Função: [p=0.2] o eixo *x* é o *deitado,* "
        "[p=0.2] o *y* é o *em pé,* [p=0.2] e um ponto é um *par ordenado:* [p=0.2] primeiro o x, [p=0.2] depois o y. "
        "[p=0.4] {b}E do episódio dois: [p=0.2] *a é delta y sobre delta x.*"),

    # ================= CONCRETO =================
    dict(id="04", block="escada", text=
        "{t}Pense numa *rampa* e numa *escada,* [p=0.2] lidas da *esquerda para a direita.* [p=0.4] {a}A reta da "
        "função afim é uma *escada.* [p=0.3] {b}Cada degrau anda *um* para a direita [p=0.2] e sobe *a.* [p=0.4] "
        "{c}Se o a for negativo, [p=0.2] o degrau *desce.* [p=0.4] {d}O quanto a rampa sobe [p=0.2] se chama "
        "*inclinação.*"),

    # ================= BLOCO A: O SINAL DE a =================
    dict(id="05", block="sinal", text=
        "{t}O que decide se a reta sobe ou desce? [p=0.4] {a}O *sinal do a.* [p=0.4] {b}Com *a positivo,* [p=0.2] a "
        "reta sobe. [p=0.2] É uma *função crescente:* [p=0.2] o x aumenta, [p=0.2] o y aumenta. [p=0.4] {c}Com *a "
        "zero,* [p=0.2] ela fica *deitada.* [p=0.2] *Função constante:* [p=0.2] o y não muda. [p=0.4] {d}Com *a "
        "negativo,* [p=0.2] ela desce. [p=0.2] *Função decrescente:* [p=0.2] o x aumenta, [p=0.2] o y diminui."),

    # ================= BLOCO B: |a| E O b =================
    dict(id="06", block="tamanho", text=
        "{t}E o *tamanho* do a? [p=0.4] {a}Ele decide o quanto a reta é *íngreme.* [p=0.3] Sem o sinal, [p=0.2] ele "
        "se chama *módulo de a:* [p=0.2] módulo de menos quatro é *quatro.* [p=0.4] {b}Módulo maior, [p=0.2] reta "
        "mais em pé. [p=0.4] {c}E o *b* só *desloca* a reta para cima ou para baixo. [p=0.4] {d}O *b* é onde a reta "
        "*nasce* no eixo vertical; [p=0.2] o *a* é para onde ela *aponta.*"),
    dict(id="07", block="contexto", text=
        "{t}E numa questão? [p=0.4] {a}*a positivo:* [p=0.2] a conta que cresce com o consumo. [p=0.4] {b}*a "
        "negativo:* [p=0.2] a vela, [p=0.2] o reservatório, [p=0.2] o carro que desvaloriza. [p=0.4] {c}*Módulo "
        "maior:* [p=0.2] a tarifa mais cara. [p=0.4] {d}*b maior:* [p=0.2] parte fixa maior."),
    dict(id="08", block="olhadas", text=
        "{t}E como ler o a e o b no desenho? [p=0.4] {a}Atalho: [p=0.2] *duas olhadas.* [p=0.4] {b}Primeira: [p=0.2] "
        "onde a reta *corta o eixo vertical?* [p=0.2] Esse é o *b.* [p=0.4] {c}Segunda: [p=0.2] ande *um* para a "
        "direita. [p=0.2] Quanto subiu é o *a.* [p=0.4] {d}Aqui: [p=0.2] nasce no *cinco,* [p=0.2] sobe *dois:* "
        "[p=0.2] *dois x mais cinco.*"),

    # ================= BLOCO C: A ESCALA =================
    dict(id="09", block="escala", text=
        "{t}E os gráficos do começo? [p=0.4] {a}A *escala dos eixos* [p=0.2] é quanto vale cada pedacinho do eixo. "
        "[p=0.3] Ela muda o desenho, [p=0.2] não a conta. [p=0.4] {b}Na esquerda, [p=0.2] o y sobe *dez* enquanto o x "
        "anda cinco: [p=0.2] *a igual a dois.* [p=0.4] {c}Na direita, [p=0.2] sobe *cinquenta:* [p=0.2] *a igual a "
        "dez.* [p=0.4] {d}A olho, [p=0.2] só *no mesmo par de eixos.* [p=0.2] Fora disso, [p=0.2] conta."),

    # ================= BLOCO D: A LEI POR DOIS PONTOS =================
    dict(id="10", block="pregos", text=
        "{t}Quantos pontos desenham uma reta? [p=0.4] {a}*Dois,* [p=0.2] como *dois pregos* seguram uma régua. "
        "[p=0.4] {b}Então dois pontos dão a lei. [p=0.3] A reta passa por *dois, onze* [p=0.2] e *cinco, vinte.* "
        "[p=0.4] {c}Passo um: [p=0.2] o *a.* [p=0.3] O x andou *três;* [p=0.2] o y subiu *nove.* [p=0.4] {d}Nove "
        "sobre três: [p=0.2] *a igual a três.* [p=0.2] Três degraus, [p=0.2] cada um subindo três."),
    dict(id="11", block="pregos", text=
        "{t}Falta o b. [p=0.3] {a}Passo dois: [p=0.2] substitua *um dos pontos.* [p=0.3] Onze igual a três vezes dois "
        "mais b. [p=0.2] Onze igual a seis mais b: [p=0.2] *b igual a cinco.* [p=0.4] {b}Passo três: [p=0.2] a lei. "
        "[p=0.2] *f de x igual a três x mais cinco.* [p=0.4] {c}Passo quatro: [p=0.2] *confira com o outro ponto.* "
        "[p=0.3] Três vezes cinco, [p=0.2] mais cinco: [p=0.2] *vinte.* [p=0.2] Bate."),
    dict(id="12", block="quarto", text=
        "{t}Por que conferir, [p=0.2] se a conta já deu? [p=0.4] {a}Atalho: [p=0.2] *o quarto passo é o seguro.* "
        "[p=0.4] {b}O ponto que você *não usou* [p=0.2] é a sua *prova real.* [p=0.4] {c}Se a lei não passa por ele, "
        "[p=0.2] tem erro de sinal ou de fração."),

    # ================= BLOCO E: ATALHOS DO b =================
    dict(id="13", block="atalhob", text=
        "{t}E se um ponto tem *x igual a zero?* [p=0.4] {a}Aí o b *já está dado:* [p=0.2] é o y desse ponto, [p=0.2] "
        "onde a reta nasce. [p=0.4] {b}Outro caminho é o *sistema:* [p=0.2] dois a mais b igual a onze, [p=0.2] cinco "
        "a mais b igual a vinte. [p=0.4] {c}Subtraindo, [p=0.2] três a igual a nove. [p=0.2] Como na série de "
        "*Sistemas.*"),

    # ================= BLOCO F: OS TERMÔMETROS =================
    dict(id="14", block="termometro", text=
        "{t}E onde a prova esconde isso? [p=0.4] {a}Em *dois termômetros.* [p=0.3] Uma *escala termométrica* [p=0.2] "
        "é um jeito de numerar a temperatura. [p=0.4] {b}No gelo derretendo: [p=0.2] *zero* Celsius, [p=0.2] *trinta "
        "e dois* Fahrenheit. [p=0.3] Na água fervendo: [p=0.2] *cem* e *duzentos e doze.* [p=0.4] {c}O b é trinta e "
        "dois. [p=0.3] O a é cento e oitenta sobre cem: [p=0.2] *um vírgula oito.* [p=0.4] {d}*F igual a um vírgula "
        "oito C mais trinta e dois.* [p=0.3] A fórmula decorada [p=0.2] é uma reta por dois pontos."),
    dict(id="15", block="tangente", text=
        "{t}Um recado. [p=0.3] {a}O a também é a *tangente* do ângulo da reta, [p=0.2] e diz se duas retas são "
        "*paralelas.* [p=0.4] {b}Isso tem *série própria* em Geometria Analítica."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}A reta passa por *um, quatro* [p=0.2] e por *três, dez.* [p=0.3] Qual é a lei? "
        "[p=0.4] {b}Siga os quatro passos. [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O a: [p=0.2] o y subiu *seis,* [p=0.2] o x andou *dois.* [p=0.2] Seis sobre "
        "dois: [p=0.2] *a igual a três.* [p=0.4] {b}O b: [p=0.2] quatro igual a três vezes um mais b. [p=0.2] *b "
        "igual a um.* [p=0.4] {c}A lei: [p=0.2] *f de x igual a três x mais um.* [p=0.4] {d}Conferindo: [p=0.2] três "
        "vezes três, [p=0.2] mais um, [p=0.2] *dez.* [p=0.2] Bate."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a positivo sobe; [p=0.2] a negativo desce; [p=0.2] "
        "a zero fica deitado. [p=0.5] {b}Dois: [p=0.2] b é onde a reta corta o eixo vertical. [p=0.5] {c}Três: "
        "[p=0.2] dois pontos dão a lei; [p=0.2] o terceiro dado confere."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *trocar a e b.* [p=0.2] A reta nasce no "
        "cinco e sobe dois, [p=0.2] e a pessoa escreve *cinco x mais dois.* [p=0.4] {b}Parece certo, [p=0.2] porque o "
        "cinco aparece primeiro. [p=0.4] {c}Mas o b é onde nasce, [p=0.2] e o a é o degrau: [p=0.2] *dois x mais "
        "cinco.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] comparar inclinações *a olho* [p=0.2] em gráficos com escalas diferentes. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque a reta mais em pé *parece* subir mais rápido. [p=0.4] {c}Mas a escala "
        "engana. [p=0.2] Calcule delta y sobre delta x [p=0.2] em cada um."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] *inverter a fração.* [p=0.2] Pontos zero, dois [p=0.2] e dois, oito: [p=0.2] a "
        "pessoa faz *dois sobre seis,* [p=0.2] um terço. [p=0.4] {b}Parece certo, [p=0.2] porque os dois números "
        "estão certos; [p=0.2] só trocaram de andar. [p=0.4] {c}Mas é *y sobre x:* [p=0.2] seis sobre dois, [p=0.2] "
        "*três.* [p=0.2] E a conferência pega o erro na hora."),

    # ================= QUESTÃO 6 (EU FAÇO) =================
    dict(id="22", block="q6", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}O gráfico de "
        "uma função afim é uma reta [p=0.2] que corta o eixo vertical no ponto *zero, menos três* [p=0.2] e passa "
        "pelo ponto *dois, um.* [p=0.3] A lei dessa função é: [p=0.3] {qa}A: [p=0.2] dois x menos três. [p=0.2] "
        "{qb}B: [p=0.2] menos três x mais dois. [p=0.2] {qc}C: [p=0.2] zero vírgula cinco x menos três. [p=0.2] "
        "{qd}D: [p=0.2] dois x mais três. [p=0.2] {qe}E: [p=0.2] menos dois x menos três. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="23", block="q6", text=
        "{t}Os quatro passos. [p=0.3] {a}O ponto tem *x igual a zero:* [p=0.2] o b já está dado. [p=0.2] *b igual a "
        "menos três.* [p=0.4] {b}O a: [p=0.2] o y foi de menos três para um, [p=0.2] subiu *quatro.* [p=0.2] O x "
        "andou *dois.* [p=0.2] Quatro sobre dois: [p=0.2] *a igual a dois.* [p=0.4] {c}A lei: [p=0.2] *dois x menos "
        "três.* [p=0.4] {d}Conferindo: [p=0.2] dois vezes dois, [p=0.2] menos três, [p=0.2] *um.* [p=0.2] Bate. "
        "[p=0.3] {ok}*Letra A!*"),
    dict(id="24", block="q6", text=
        "{t}E as armadilhas? [p=0.3] {xb}A B *troca os papéis* de a e b. [p=0.4] {xc}A C *inverte a fração:* [p=0.2] "
        "dois sobre quatro. [p=0.4] {xd}A D erra o *sinal do b.* [p=0.4] {xe}E a E erra o *sinal do a:* [p=0.2] a "
        "reta sobe de menos três para um, [p=0.2] então é crescente."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="25", block="q5", text=
        "{t}E esta é *sua.* [p=0.3] {a}Um estudante criou uma escala termométrica *E* [p=0.2] que marca *dez graus "
        "E* no gelo derretendo, [p=0.2] zero grau Celsius, [p=0.2] e *sessenta graus E* na água fervendo, [p=0.2] "
        "cem graus Celsius. [p=0.3] A relação é afim. [p=0.3] Uma pessoa com *trinta e sete graus Celsius* teria: "
        "[p=0.3] {qa}A: [p=0.2] dezoito vírgula cinco. [p=0.2] {qb}B: [p=0.2] vinte e oito vírgula cinco. [p=0.2] "
        "{qc}C: [p=0.2] quarenta e sete. [p=0.2] {qd}D: [p=0.2] setenta e quatro. [p=0.2] {qe}E: [p=0.2] oitenta e "
        "quatro. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q5", text=
        "{t}Conferindo. [p=0.3] {a}Zero, dez: [p=0.2] x igual a zero, [p=0.2] então *b igual a dez.* [p=0.4] {b}O a: "
        "[p=0.2] cinquenta sobre cem, [p=0.2] *zero vírgula cinco.* [p=0.4] {c}Com trinta e sete: [p=0.2] dezoito "
        "vírgula cinco, [p=0.2] mais dez: [p=0.2] *vinte e oito vírgula cinco.* [p=0.4] {d}Conferindo com a fervura: "
        "[p=0.2] cinquenta mais dez, [p=0.2] sessenta. [p=0.2] Bate. [p=0.2] {ok}*Letra B!*"),
    dict(id="27", block="q5", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A *esquece o b,* [p=0.2] como se fosse proporcional. [p=0.4] {xc}A C "
        "soma dez [p=0.2] sem aplicar a taxa. [p=0.4] {xd}A D *inverte a taxa,* [p=0.2] usa dois, [p=0.2] e esquece "
        "o b. [p=0.4] {xe}E a E inverte a taxa [p=0.2] e soma o b."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a positivo sobe; [p=0.2] a negativo desce; "
        "[p=0.2] a zero fica deitado. [p=0.5] {b}Dois: [p=0.2] b é onde a reta corta o eixo vertical. [p=0.5] "
        "{c}Três: [p=0.2] dois pontos dão a lei; [p=0.2] o terceiro dado confere."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Uma confecção tem *doze mil reais* de custo fixo [p=0.2] e lucra *vinte reais* por camiseta. [p=0.4] "
        "{b}Com *seiscentas* camisetas, [p=0.2] ela tem lucro? [p=0.4] {c}Cuidado: [p=0.2] a resposta *não é sim.* "
        "[p=0.4] {d}Próximo episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual fórmula que você decorou [p=0.2] é, na verdade, uma reta? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
