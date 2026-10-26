# Roteiro — Equação do 2º Grau e Fórmula de Bhaskara, Episódio 2 de 6: a fórmula de Bhaskara e o que o Δ revela.
# Base: Estudos/Enem/estudos/01-matematica/21-equacao-2o-grau-bhaskara.html — seções 04 e 05 (com o quadro "De onde vem a
#   fórmula") + Questão 2.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Bhaskara é uma CHAVE MESTRA: abre qualquer equação do 2º grau, mas só se a equação estiver arrumada (= 0).
#   O Δ é o PORTEIRO: positivo deixa passar duas raízes, zero deixa passar uma, negativo não deixa passar nenhuma
#     (não existe raiz quadrada real de número negativo).
#   A fórmula é o QUADRADO DA SOMA usado ao contrário: arrume a equação para virar (2ax + b)².
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (todos conferidos em Python):
#   2x² − 7x + 3 = 0: a = 2, b = −7, c = 3 → Δ = 49 − 24 = 25 → x = (7 ± 5)/4 → 3 e 1/2; conferência 2·9 − 21 + 3 = 0.
#   Tabela do Δ: x² − 5x + 4 (Δ = 9, raízes 1 e 4) · x² + 2x + 5 (Δ = −16).
#   DESVIO DO PROMPT: o exemplo de Δ = 0 (x² − 6x + 9) e o bloco g (x² − 6x + k → k = 9) são exatamente a resposta da
#   Questão 2, que tem pausa ("eu começo, você termina"). Para não entregá-la, o Δ = 0 usa x² − 4x + 4 (raiz 2) e o
#   parâmetro usa x² − 8x + k = 0 → 64 − 4k = 0 → k = 16 → (x − 4)².
#   Tropeços: −7² = −49 daria Δ = −49 − 24 = −73 ("sem raiz", falso) · 7 + 5 ÷ 4 = 8,25 (só a raiz dividida) ·
#   sem igualar a zero: x² − 5x = −6 usado com c = −6 dá 6 e −1 (36 − 30 = 6, não −6); arrumado, x² − 5x + 6 = 0 → 2 e 3.
# Nós fazemos (prompt): 3x² − 5x − 2 = 0 → Δ = 25 + 24 = 49 → x = (5 ± 7)/6 → 2 e −1/3; conferência 12 − 10 − 2 = 0.
# QUESTÃO 2 (eu começo, você termina; texto idêntico): Δ = 0 → 36 − 4k = 0 → k = 9 → C; (x − 3)².
#   Erradas (material): A 3 = a própria raiz dupla, não o k; B 6 copia o b sem sinal; D 36 esquece o 4 de 4ac;
#   E −9 erra o sinal ao isolar k: Δ = 36 + 36 = 72, dois pontos de contato.
# Parábola (bloco f): só ilustração, sem vértice nem concavidade (série de Função Quadrática).
# Atalhos (verde): conferência de 10 segundos (substitua uma raiz) · a e c com sinais opostos → Δ sempre positivo
#   (o −4ac vira soma) → duas raízes garantidas · "uma única raiz" = Δ = 0.
# Frases-chave (meio e fim, idênticas): 1. Primeiro a, b e c com sinal; depois o Δ. 2. Δ positivo, duas raízes; zero, uma;
#   negativo, nenhuma real. 3. O 2a divide o numerador inteiro.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Fórmula de Bhaskara do zero: o sinal do b e o que o delta revela | Bhaskara Ep. 2"
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
    "Bhaskara": "Báskara",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Na fórmula de Bhaskara, [p=0.2] quase todo erro começa *antes* da fórmula: [p=0.3] {b}no *sinal do b.* "
        "[p=0.5] {c}Com b igual a menos sete, [p=0.2] o b ao quadrado é *mais quarenta e nove* [p=0.3] {d}e o menos b é "
        "*mais sete.* [p=0.5] {e}Erre um dos dois [p=0.2] e as raízes saem *trocadas.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai aplicar Bhaskara *sem errar sinal* [p=0.3] {b}e saber, só olhando o *delta,* "
        "[p=0.2] quantas raízes a equação tem."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] a tabelinha *a, b, c,* [p=0.2] com o sinal "
        "grudado em cada número. [p=0.4] {b}Da série de Operações: [p=0.2] *menos sete, entre parênteses, ao quadrado* "
        "[p=0.2] é mais quarenta e nove; [p=0.2] sem parênteses, *menos* quarenta e nove. [p=0.4] {c}E de Expressões "
        "Algébricas: [p=0.2] o *quadrado da soma,* [p=0.2] a mais b, ao quadrado."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe esta equação: [p=0.2] *dois x ao quadrado, menos sete x, mais três, igual a zero.* [p=0.4] {a}Dá para "
        "colocar x em evidência, como no episódio um? [p=0.3] *Não:* [p=0.2] o três não tem x. [p=0.4] {b}Dá para isolar "
        "o x ao quadrado? [p=0.3] *Também não:* [p=0.2] o menos sete x atrapalha. [p=0.4] {c}Os truques das incompletas "
        "*travaram.* [p=0.3] {d}Precisamos de uma ferramenta que abra *qualquer* equação: [p=0.2] uma *chave mestra.*"),

    # ================= BLOCO A: A FÓRMULA =================
    dict(id="05", block="formula", text=
        "{t}Que chave é essa? [p=0.4] {a}A *fórmula de Bhaskara* [p=0.2] é a receita que dá as raízes de qualquer "
        "equação do segundo grau. [p=0.4] {b}Ela tem duas etapas. [p=0.2] A primeira é o *discriminante,* [p=0.2] "
        "chamado de *delta,* [p=0.2] esse triângulo grego. [p=0.4] {c}Delta é igual a *b ao quadrado, menos quatro a "
        "c.* [p=0.5] {d}Mas atenção: [p=0.2] a chave mestra só abre a equação *arrumada,* [p=0.2] com zero de um lado."),
    dict(id="06", block="formula", text=
        "{t}E a segunda etapa? [p=0.4] {a}x é igual a *menos b, mais ou menos raiz de delta,* [p=0.2] tudo dividido por "
        "*dois a.* [p=0.5] {b}Esse *mais ou menos* quer dizer duas contas: [p=0.2] uma com mais, [p=0.2] outra com menos. "
        "[p=0.4] {c}Por isso costumam sair *duas* raízes."),

    # ================= BLOCO B: EXEMPLO COMPLETO =================
    dict(id="07", block="exemplo", text=
        "{t}Vamos abrir aquela equação. [p=0.4] {a}Primeiro, a tabelinha: [p=0.2] a igual a *dois,* [p=0.2] b igual a "
        "*menos sete,* [p=0.2] c igual a *três.* [p=0.4] {b}Agora o delta: [p=0.2] *menos sete, entre parênteses,* ao "
        "quadrado, [p=0.2] menos quatro, vezes dois, vezes três. [p=0.4] {c}Menos sete ao quadrado: [p=0.2] *quarenta e "
        "nove.* [p=0.2] Quatro vezes dois vezes três: [p=0.2] *vinte e quatro.* [p=0.4] {d}Quarenta e nove menos vinte e "
        "quatro: [p=0.2] *delta igual a vinte e cinco.*"),
    dict(id="08", block="exemplo", text=
        "{t}Segunda etapa. [p=0.3] {a}Menos b: [p=0.2] o b é menos sete, [p=0.2] então menos b é *mais sete.* [p=0.4] "
        "{b}Raiz de vinte e cinco: [p=0.2] *cinco.* [p=0.2] Dois a: [p=0.2] *quatro.* [p=0.4] {c}x igual a sete, mais ou "
        "menos cinco, [p=0.2] sobre quatro. [p=0.4] {d}Com mais: [p=0.2] doze sobre quatro, [p=0.2] *três.* [p=0.3] "
        "{e}Com menos: [p=0.2] dois sobre quatro, [p=0.2] *um meio.*"),
    dict(id="09", block="exemplo", text=
        "{t}Atalho: [p=0.2] a *conferência de dez segundos.* [p=0.4] {a}Coloque uma raiz de volta na equação. [p=0.3] "
        "{b}Com x igual a três: [p=0.2] dois vezes nove, *dezoito,* [p=0.2] menos vinte e um, [p=0.2] mais três: "
        "[p=0.2] *zero.* [p=0.3] {ok}*Bateu!* [p=0.4] {c}Se não desse zero, [p=0.2] o erro estaria quase sempre num "
        "*sinal.*"),

    # ================= BLOCO C: OS TRÊS TROPEÇOS =================
    dict(id="10", block="tropecos", text=
        "{t}Onde a maioria tropeça? [p=0.4] {a}Tropeço um: [p=0.2] o b ao quadrado. [p=0.2] Com b igual a menos sete, "
        "[p=0.2] é *mais* quarenta e nove. [p=0.2] Um número ao quadrado nunca fica negativo. [p=0.4] {b}Tropeço dois: "
        "[p=0.2] o menos b. [p=0.2] O oposto de menos sete é *mais sete.* [p=0.4] {c}Tropeço três: [p=0.2] o dois a "
        "divide o numerador *inteiro.* [p=0.2] É sete mais cinco, [p=0.2] *tudo* dividido por quatro, [p=0.2] e não sete "
        "mais cinco quartos."),

    # ================= BLOCO D: DE ONDE VEM =================
    dict(id="11", block="origem", text=
        "{t}E de onde saiu essa fórmula? [p=0.3] Em um minuto. [p=0.4] {a}Ela é o *quadrado da soma usado ao contrário.* "
        "[p=0.4] {b}Pegue a x ao quadrado, mais b x, mais c, igual a zero, [p=0.2] e multiplique tudo por *quatro a.* "
        "[p=0.4] {c}Depois some *b ao quadrado* dos dois lados. [p=0.4] {d}O lado esquerdo vira um quadrado perfeito: "
        "[p=0.2] *dois a x, mais b, ao quadrado.* [p=0.3] {e}E o direito vira *b ao quadrado menos quatro a c:* [p=0.2] "
        "o próprio delta."),
    dict(id="12", block="origem", text=
        "{t}E o mais ou menos? [p=0.4] {a}Se um número ao quadrado dá delta, [p=0.2] esse número pode ser *mais* raiz de "
        "delta [p=0.2] ou *menos* raiz de delta. [p=0.4] {b}Cinco ao quadrado dá vinte e cinco; [p=0.2] menos cinco ao "
        "quadrado *também.* [p=0.4] {c}Isolando o x, [p=0.2] sai a fórmula inteira."),

    # ================= BLOCO E: O PORTEIRO =================
    dict(id="13", block="porteiro", text=
        "{t}E por que o delta tem esse nome, *discriminante?* [p=0.4] {a}Porque ele é o *porteiro:* [p=0.2] decide quantas "
        "raízes passam. [p=0.4] {b}Uma *raiz real* é uma solução que existe entre os números que usamos no dia a dia. "
        "[p=0.4] {c}Primeira porta: [p=0.2] *delta positivo.* [p=0.2] x ao quadrado, menos cinco x, mais quatro: [p=0.2] "
        "delta igual a *nove.* [p=0.3] {d}Passam *duas* raízes: [p=0.2] *um* e *quatro.*"),
    dict(id="14", block="porteiro", text=
        "{t}Segunda porta: [p=0.2] *delta igual a zero.* [p=0.4] {a}x ao quadrado, menos quatro x, mais quatro: [p=0.2] "
        "dezesseis menos dezesseis, [p=0.2] *zero.* [p=0.4] {b}Mais zero e menos zero dão a mesma coisa. [p=0.2] Passa "
        "*uma* raiz só: [p=0.2] *dois.* [p=0.4] {c}Ela se chama *raiz dupla:* [p=0.2] as duas contas caem no mesmo "
        "número."),
    dict(id="15", block="porteiro", text=
        "{t}Terceira porta: [p=0.2] *delta negativo.* [p=0.4] {a}x ao quadrado, mais dois x, mais cinco: [p=0.2] quatro "
        "menos vinte, [p=0.2] *menos dezesseis.* [p=0.4] {b}Raiz de menos dezesseis? [p=0.2] Nenhum número real ao "
        "quadrado dá negativo. [p=0.4] {c}Porta *trancada:* [p=0.2] *nenhuma* raiz real. [p=0.2] Pode parar a conta "
        "aqui."),
    dict(id="16", block="porteiro", text=
        "{t}Atalho para o porteiro. [p=0.4] {a}Se o a e o c têm *sinais opostos,* [p=0.2] o menos quatro a c vira uma "
        "*soma.* [p=0.4] {b}Aí o delta é b ao quadrado *mais* um número positivo: [p=0.2] sempre positivo. [p=0.4] "
        "{c}Duas raízes garantidas, [p=0.2] *sem fazer conta.*"),

    # ================= BLOCO F: A PARÁBOLA (SÓ CITADA) =================
    dict(id="17", block="parabola", text=
        "{t}E onde isso aparece num gráfico? [p=0.4] {a}O desenho de y igual a a x ao quadrado, mais b x, mais c [p=0.2] "
        "é uma curva chamada *parábola.* [p=0.4] {b}As raízes são os pontos em que ela *corta o eixo x:* [p=0.2] duas "
        "vezes, [p=0.2] uma vez [p=0.2] ou nenhuma. [p=0.4] {c}É o mesmo porteiro, desenhado. [p=0.2] O gráfico tem "
        "série própria: [p=0.2] *Função Quadrática.*"),

    # ================= BLOCO G: PARÂMETRO =================
    dict(id="18", block="parametro", text=
        "{t}E quando a equação tem uma *letra* no lugar de um número? [p=0.4] {a}Essa letra é um *parâmetro:* [p=0.2] um "
        "valor que você escolhe e que muda a equação. [p=0.4] {b}x ao quadrado, menos oito x, mais k, igual a zero. "
        "[p=0.2] Para qual k existe *uma única raiz?* [p=0.4] {c}Uma única raiz é a segunda porta: [p=0.2] *delta igual a "
        "zero.* [p=0.4] {d}Sessenta e quatro, menos quatro k, igual a zero: [p=0.2] *k igual a dezesseis.* [p=0.4] "
        "{e}Confere: [p=0.2] x ao quadrado, menos oito x, mais dezesseis [p=0.2] é *x menos quatro, ao quadrado.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva *três x ao quadrado, menos cinco x, menos dois, igual a zero,* [p=0.2] por "
        "Bhaskara. [p=0.3] {p}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}a igual a três, [p=0.2] b igual a menos cinco, [p=0.2] c igual a menos dois. "
        "[p=0.4] {b}Delta: [p=0.2] vinte e cinco, menos quatro vezes três vezes menos dois. [p=0.2] Menos com menos: "
        "[p=0.2] vinte e cinco *mais* vinte e quatro, [p=0.2] *quarenta e nove.* [p=0.4] {c}x igual a cinco, mais ou menos "
        "sete, [p=0.2] sobre seis: [p=0.2] *dois* [p=0.2] ou *menos um terço.* [p=0.4] {d}Conferência com x igual a dois: "
        "[p=0.2] doze, menos dez, menos dois: [p=0.2] *zero.* [p=0.3] {ok}*Bateu!*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Três frases para guardar. [p=0.5] {a}Um: [p=0.2] primeiro a, b e c com sinal; [p=0.2] depois o delta. "
        "[p=0.5] {b}Dois: [p=0.2] delta positivo, duas raízes; [p=0.2] zero, uma; [p=0.2] negativo, nenhuma real. "
        "[p=0.5] {c}Três: [p=0.2] o dois a divide o numerador inteiro."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{a}Erro número um: [p=0.2] calcular o delta com *menos sete ao quadrado igual a menos quarenta e nove.* [p=0.4] "
        "{b}Parece certo porque, na calculadora, [p=0.2] menos sete ao quadrado sem parênteses dá mesmo menos quarenta e "
        "nove. [p=0.4] {c}Correção: [p=0.2] escreva o b *sempre entre parênteses.* [p=0.2] Senão o delta vira menos "
        "setenta e três, [p=0.2] e você jura que não tem raiz."),
    dict(id="23", block="erros", text=
        "{a}Erro número dois: [p=0.2] dividir *só a raiz* por dois a. [p=0.4] {b}Parece certo porque a raiz de delta "
        "fica bem em cima do dois a. [p=0.2] Sete mais cinco quartos dá *oito vírgula vinte e cinco.* [p=0.4] {c}Correção: "
        "[p=0.2] o traço da fração cobre o numerador *inteiro.* [p=0.2] Some primeiro, [p=0.2] divida depois: [p=0.2] "
        "*três.*"),
    dict(id="24", block="erros", text=
        "{a}Erro número três: [p=0.2] aplicar a fórmula *sem igualar a zero.* [p=0.4] {a2}Em x ao quadrado, menos cinco "
        "x, igual a menos seis, [p=0.2] a pessoa usa c igual a menos seis [p=0.2] e acha seis e menos um. [p=0.4] {b}Parece "
        "certo porque os três números estão ali, prontos. [p=0.4] {c}Correção: [p=0.2] a chave mestra só abre a equação "
        "arrumada. [p=0.2] Passe o menos seis para o outro lado: [p=0.2] *mais seis.* [p=0.2] As raízes são *dois* e "
        "*três.*"),

    # ================= QUESTÃO 2 (EU COMEÇO, VOCÊ TERMINA) =================
    dict(id="25", block="q2", text=
        "{t}Hora de questão. [p=0.3] {a}Um programa de desenho traça a curva *y igual a x ao quadrado, menos seis x, mais "
        "k,* [p=0.2] em que k é escolhido pelo usuário. [p=0.2] Para uma vinheta, o designer quer que a curva toque o "
        "eixo horizontal em *exatamente um ponto.* [p=0.2] O valor de k deve ser: [p=0.4] {qa}A: [p=0.2] três. [p=0.3] "
        "{qb}B: [p=0.2] seis. [p=0.3] {qc}C: [p=0.2] nove. [p=0.3] {qd}D: [p=0.2] trinta e seis. [p=0.3] {qe}E: [p=0.2] "
        "menos nove."),
    dict(id="26", block="q2", text=
        "{t}Eu começo. [p=0.3] {a}Tocar o eixo em um único ponto [p=0.2] é ter *uma única raiz.* [p=0.2] Segunda porta: "
        "[p=0.2] *delta igual a zero.* [p=0.4] {b}Tabelinha: [p=0.2] a igual a um, [p=0.2] b igual a menos seis, [p=0.2] "
        "c igual a k. [p=0.4] {c}Agora você termina. [p=0.2] {p}*Pause o vídeo.* [p=2.0] {d}Menos seis, ao quadrado, "
        "[p=0.2] trinta e seis, [p=0.2] menos quatro k, [p=0.2] igual a zero. [p=0.2] *k igual a nove.* [p=0.4] {e}Confere: "
        "[p=0.2] x ao quadrado, menos seis x, mais nove [p=0.2] é *x menos três, ao quadrado,* [p=0.2] que só zera em "
        "três. [p=0.3] {ok}*Letra C!*"),
    dict(id="27", block="q2", text=
        "{t}E as erradas? [p=0.3] {xa}A A, [p=0.2] três, [p=0.2] é a própria *raiz dupla,* [p=0.2] não o k. [p=0.4] {xb}A "
        "B *copiou o b* sem o sinal. [p=0.4] {xd}A D esqueceu o *quatro* de quatro a c. [p=0.4] {xe}E a E, [p=0.2] menos "
        "nove, [p=0.2] errou o sinal ao isolar o k: [p=0.2] com ela, o delta seria *setenta e dois,* [p=0.2] e a curva "
        "tocaria o eixo em *dois* pontos."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] primeiro a, b e c com sinal; [p=0.2] depois o "
        "delta. [p=0.5] {b}Dois: [p=0.2] delta positivo, duas raízes; [p=0.2] zero, uma; [p=0.2] negativo, nenhuma real. "
        "[p=0.5] {c}Três: [p=0.2] o dois a divide o numerador inteiro."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Em *x ao quadrado, menos sete x, mais dez, igual a zero,* [p=0.2] dá para achar as raízes sem fórmula "
        "nenhuma, [p=0.2] em *três segundos:* [p=0.4] {b}dois números que *somam sete* e *multiplicam dez.* [p=0.5] "
        "{c}Próximo episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual dos três tropeços já te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* "
        "deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, "
        "[p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui "
        "no Estudativo. [p=1.5]"),
]
