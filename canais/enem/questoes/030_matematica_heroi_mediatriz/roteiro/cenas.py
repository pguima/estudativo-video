# Estudativo · Questão 030 — ENEM 2025, 2º dia, caderno amarelo, questão 147: num jogo, o herói é atacado pelo vilão mais
# próximo; para não ser atacado, anda equidistante dos dois. No quadrado STUV, os vilões estão em V(8; 6) e T, e o herói
# começa em S(6; 2). T não é dado: de S a V o lado anda (2, 4); girado 90°, (−4, 2) → T = (2, 4) (e U = (4, 8)).
# A trajetória é a mediatriz de TV: ponto médio (5; 5); coeficiente de TV = 2/6 = 1/3; perpendicular: −3;
# y − 5 = −3(x − 5) → y = −3x + 20 → alternativa A. Conferência: passa por S (−18 + 20 = 2) e por U (−12 + 20 = 8): é a
# outra diagonal do quadrado. Pegadinhas: D e E (+3) não trocam o sinal; B e C (−3) não passam pelo ponto médio (5; 5).
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: mediatriz (equidistante de dois pontos) → 2: coeficiente angular (Δy ÷ Δx; perpendiculares:
# produto −1) → 3: equação da reta por um ponto → passo 1: achar T (girar o lado 90°) → passo 2: ponto médio → passo 3:
# o coeficiente da mediatriz → passo 4: a equação → conferência (S e U) → A → pegadinhas → desafio → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: o herói e os dois vilões (mediatriz e equação da reta)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nas contas, fale devagar e com clareza, número por número. Faça as perguntas com "
            "curiosidade genuína, mostre surpresa na resposta e comemore o resultado. Respeite as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão cento e quarenta e sete do ENEM dois mil e vinte e cinco. [p=0.2] Num jogo, [p=0.1] o herói é atacado "
        "pelo vilão que estiver *mais perto.* [p=0.3] {b}Os vilões estão em dois cantos de um quadrado: [p=0.1] em *V,* "
        "[p=0.1] no ponto oito e seis, [p=0.1] e em *T.* [p=0.2] O herói começa em *S,* [p=0.1] no ponto seis e dois. "
        "[p=0.3] {c}Para não ser atacado, [p=0.1] ele precisa ficar *à mesma distância* dos dois vilões. [p=0.3] {d}Qual "
        "é a equação desse caminho? [p=0.3] {e}Nessa aula, [p=0.1] você vai usar a *mediatriz,* [p=0.1] o *coeficiente "
        "angular* [p=0.1] e a *equação da reta.*"),
    dict(id="02", block="mediatriz", text=
        "{a}Ferramenta um: [p=0.1] a *mediatriz.* [p=0.3] {b}Pense em dois pontos. [p=0.2] Todos os pontos que ficam *à "
        "mesma distância* dos dois [p=0.1] formam uma reta. [p=0.3] {c}Essa reta é a mediatriz do segmento entre eles. "
        "[p=0.3] {d}Ela passa pelo *ponto médio* do segmento [p=0.1] e corta o segmento em *ângulo reto.*"),
    dict(id="03", block="coeficiente", text=
        "{a}Ferramenta dois: [p=0.1] o *coeficiente angular.* [p=0.3] {b}Ele mede a inclinação da reta: [p=0.1] é quanto o "
        "ípsilon sobe [p=0.1] para cada passo do xis. [p=0.3] {c}Entre dois pontos, [p=0.1] é a *variação do ípsilon* "
        "[p=0.1] dividida pela *variação do xis.* [p=0.3] {d}E retas *perpendiculares* [p=0.1] têm coeficientes que, "
        "multiplicados, [p=0.1] dão *menos um.* [p=0.2] Por exemplo: [p=0.1] um terço [p=0.1] e menos três."),
    dict(id="04", block="equacao", text=
        "{a}Ferramenta três: [p=0.1] a *equação da reta.* [p=0.3] {b}Se você sabe *um ponto* da reta [p=0.1] e o "
        "*coeficiente angular,* [p=0.1] já tem tudo. [p=0.3] {c}Ípsilon menos ípsilon zero [p=0.1] é igual a eme, [p=0.1] "
        "vezes xis menos xis zero."),
    dict(id="05", block="ponto_t", text=
        "{a}Passo um: [p=0.1] onde está o vilão *T?* [p=0.3] {b}O enunciado não dá. [p=0.1] Mas *STUV é um quadrado.* "
        "[p=0.3] {c}De S até V, [p=0.1] o xis anda *dois* [p=0.1] e o ípsilon sobe *quatro.* [p=0.3] {d}O lado de S até T "
        "[p=0.1] é igual, [p=0.1] só que girado noventa graus: [p=0.1] os números trocam de lugar [p=0.1] e um sinal muda. "
        "[p=0.2] O xis volta *quatro* [p=0.1] e o ípsilon sobe *dois.* [p=0.3] {e}Então T fica no ponto *dois e quatro.*"),
    dict(id="06", block="ponto_medio", text=
        "{a}Passo dois: [p=0.1] o ponto médio entre T e V. [p=0.3] {b}A média dos xis: [p=0.1] dois mais oito, [p=0.1] "
        "dividido por dois, [p=0.1] dá *cinco.* [p=0.3] {c}A média dos ípsilons: [p=0.1] quatro mais seis, [p=0.1] "
        "dividido por dois, [p=0.1] dá *cinco.* [p=0.3] {d}O ponto médio é *cinco e cinco.*"),
    dict(id="07", block="inclinacao", text=
        "{a}Passo três: [p=0.1] a inclinação. [p=0.3] {b}De T até V, [p=0.1] o ípsilon sobe *dois* [p=0.1] e o xis anda "
        "*seis.* [p=0.2] O coeficiente é dois sobre seis: [p=0.1] *um terço.* [p=0.3] {c}A mediatriz é perpendicular a "
        "esse segmento. [p=0.2] Então o coeficiente dela é *menos três,* [p=0.1] porque um terço vezes menos três [p=0.1] "
        "dá menos um."),
    dict(id="08", block="equacao_final", text=
        "{a}Passo quatro: [p=0.1] a equação. [p=0.3] {b}Pelo ponto cinco e cinco, [p=0.1] com coeficiente menos três: "
        "[p=0.2] ípsilon menos cinco [p=0.1] é igual a menos três, [p=0.1] vezes xis menos cinco. [p=0.3] {c}Fazendo a "
        "distributiva: [p=0.1] ípsilon menos cinco [p=0.1] é igual a menos três xis mais quinze. [p=0.3] {d}Passando o "
        "cinco para o outro lado: [p=0.1] *ípsilon igual a menos três xis mais vinte.*"),
    dict(id="09", block="resposta", text=
        "{a}Conferindo: [p=0.1] o herói começa em S, [p=0.1] no ponto seis e dois. [p=0.2] Menos três vezes seis, [p=0.1] "
        "mais vinte, [p=0.1] dá *dois.* [p=0.2] Ele já começa no caminho certo! [p=0.3] {b}E o caminho passa também por U: "
        "[p=0.1] a mediatriz é a *outra diagonal* do quadrado. [p=0.3] {c}Alternativa *A.*"),
    dict(id="10", block="pegadinhas", text=
        "{a}E as outras? [p=0.3] {b}A *D* e a *E* têm coeficiente *mais três:* [p=0.1] esqueceram de trocar o sinal. "
        "[p=0.3] {c}A *B* e a *C* têm o coeficiente certo, [p=0.1] mas não passam pelo ponto médio. [p=0.2] {d}Com xis "
        "igual a cinco, [p=0.1] elas dariam ípsilon igual a um [p=0.1] e a menos trinta e cinco, [p=0.1] e não cinco."),
    dict(id="11", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}Qual é a equação da reta [p=0.1] que passa pelos dois vilões, [p=0.1] *T e V?* "
        "[p=0.3] {c}Deixe sua resposta nos comentários."),
    dict(id="12", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}À mesma distância de dois pontos: [p=0.1] a mediatriz. [p=0.2] {c}Ela passa pelo "
        "ponto médio. [p=0.2] {d}E o coeficiente dela é o perpendicular: [p=0.1] o inverso, [p=0.1] com o sinal trocado."),
    dict(id="13", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*equação da reta,* [p=0.2] {c}*ponto médio e distância* [p=0.2] {d}e *retas perpendiculares.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
