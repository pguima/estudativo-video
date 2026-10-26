# Roteiro — Expressões Algébricas e Produtos Notáveis, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e
#   treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/19-expressoes-algebricas-produtos-notaveis.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 a letra como CAIXINHA (com parênteses) · termos semelhantes como FRUTAS IGUAIS · a distributiva como APERTO DE MÃO ·
#     o MENOS como ESPELHO ·
#   ep2 o QUADRADO com DOIS RETÂNGULOS ab · o expoente BARRADO NA PORTA DA SOMA · o TESTE DE 10 SEGUNDOS ·
#   ep3 CORTA-SE FATOR, NUNCA TERMO · o L QUE VIRA RETÂNGULO ·
#   ep4 os GÊMEOS ao redor do NÚMERO REDONDO.
#   (O ep4 foi escrito em paralelo: a analogia dele vem do prompt do vídeo 5 e do plano da série.)
# O que a prova cobra (seção 01): modelar · comparar expressões (distrator (a + b)² = a² + b²) · calcular sem calculadora ·
#   simplificar antes de calcular. As duas habilidades que mais rendem: traduzir com cuidado e lembrar do termo do meio.
# Onde aparece (seção 10): Financeira (1,1² = 1,21: 21%, não 20%; o 1% a mais é o i² — série de Juros compostos) ·
#   Física ((2v)² = 4v²: energia cinética × 4) · Geometria (lado + k → área + 2kx + k²) · Equação do 2º grau (Bhaskara
#   nasce do quadrado da soma: próxima série do bloco). Só pontes, sem aprofundar.
# Estratégia (seção 09): teste com um número (x = 2; se duas baterem, outro valor) · uma frase de cada vez · procure o
#   termo do meio nos distratores.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras — as verdadeiras são as versões CERTAS dos erros 3, 4 e 9):
#   1 F (a + b)² = a² + b² · 2 F (a − b)² = a² − b² · 3 V −2² sem parênteses vale −4 · 4 V 5 − (x − 3) = 8 − x ·
#   5 F 2x + 3x² = 5x³ · 6 F (3x)² = 3x² · 7 F cortar o 3 em (x + 3)/3 · 8 F "o dobro da soma de x com 3" = 2x + 3 ·
#   9 V x² − 16 = (x + 4)(x − 4).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta, confirmada pelo teste do número;
#   cada errada = um erro clássico):
#   Q1 (corrida de aplicativo) bandeirada R$ 5,00 por corrida + R$ 2,00 por km; corrida 1: x km; corrida 2: 3 km a mais.
#      Total: (5 + 2x) + (5 + 2(x + 3)) = 4x + 16 → D. A 4x + 13 (2x + 3: "o dobro da soma") · B 4x + 11 (bandeirada uma
#      vez só) · C 4x + 10 (esqueceu os 3 km a mais) · E 20x (juntou termos não semelhantes). Teste x = 4: 13 + 19 = 32.
#   Q2 (terreno) quadrado de lado x perde 6 m em cada lado (calçada): (x − 6)² = x² − 12x + 36 → B. A x² − 36 (sonho do
#      calouro) · C x² − 6x + 36 (termo do meio pela metade) · D x² − 12x − 36 (b² negativo) · E x² + 12x + 36 (sinal
#      trocado: é o quadrado da soma). Teste x = 10: 4² = 16; só a B dá 16.
#   Q3 (praça) quadrado de lado x, + 4 m em cada lado; AUMENTO da área: (x + 4)² − x² = 8x + 16 → E. A 16 (sonho do
#      calouro) · B 8x (esqueceu o quadradinho de canto) · C 4x + 16 (um retângulo só: termo do meio pela metade) ·
#      D x² + 8x + 16 (área nova inteira, não o aumento). Teste x = 10: 196 − 100 = 96.
#   Q4 (fração) (3x² − 12)/(x² − 4x + 4) = 3(x + 2)(x − 2)/(x − 2)² = 3(x + 2)/(x − 2), x ≠ 2 → A. B 3 (fatorou x² − 4
#      como (x − 2)²) · C 9/(4x − 4) ("cortou" o x²: termo) · D (x + 2)/(x − 2) (perdeu o fator comum 3) · E 3(x − 2)/(x + 2)
#      (inverteu). Teste x = 3: 15/1 = 15; só a A dá 15 (x = 0 não serve: a E também daria −3).
#   Q5 (gramado) 302 m por 298 m: (300 + 2)(300 − 2) = 90 000 − 4 = 89 996 m² → C. A 90 004 (somou o quadrado do passo) ·
#      B 90 000 (aproximou e ignorou o quadrado do passo) · D 89 998 (tirou 2, não 2²) · E 88 804 (fez 298²).
# Gabaritos: D, B, E, A, C.
# Checklist (seção 13, 13 itens) → episódio: tradução, valor numérico, operações e sinais: ep1 · quadrados, soma pela
#   diferença, desenho do quadrado e cubo: ep2 · fatoração, frações e a² + b²: ep3 · contas de cabeça: ep4 · teste de
#   alternativas: este episódio.
# Meta (material): 30 questões, pelo menos 21 acertos (70%), com pelo menos dez de modelagem.
# Ponte (do usuário): Equações e inequações do 1º grau.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de expressões algébricas: 9 pegadinhas e 5 questões estilo ENEM | Produtos Notáveis Ep. 5"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, termo por termo. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}Este assunto quase nunca aparece com a palavra *fatore* na prova. [p=0.4] {b}Ele aparece disfarçado de "
        "*corrida de aplicativo,* [p=0.2] de *terreno ampliado* [p=0.2] e de *conta sem calculadora.* [p=0.4] {c}Hoje "
        "você aprende a *tirar o disfarce.* [p=0.4] {d}Nove frases de verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova cobra? [p=0.4] {a}*Modelar:* [p=0.2] escrever a expressão de um custo. "
        "[p=0.3] {b}*Comparar expressões:* [p=0.2] qual alternativa é equivalente, [p=0.2] com distratores feitos de erros. [p=0.3] {c}*Calcular sem calculadora.* [p=0.3] {d}E *simplificar antes de calcular.*"),
    dict(id="03", block="duas", text=
        "{t}E duas habilidades rendem mais que todas. [p=0.4] {a}Primeira: [p=0.2] *traduzir com cuidado.* [p=0.4] {b}Segunda: [p=0.2] *lembrar do "
        "termo do meio.* [p=0.2] A mais b ao quadrado [p=0.2] tem *dois a b,* [p=0.2] sempre."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] a letra é uma *caixinha:* "
        "[p=0.2] o número entra *com parênteses.* [p=0.3] Só se somam *frutas iguais.* [p=0.2] A distributiva é um *aperto "
        "de mão,* [p=0.2] e o menos antes do parêntese [p=0.2] é um *espelho.* [p=0.4] {b}Dois: [p=0.2] o quadrado da soma "
        "tem *dois retângulos* a b. [p=0.3] O expoente fica *barrado na porta da soma.* [p=0.2] E na dúvida, [p=0.2] o "
        "*teste de dez segundos.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] *corta-se fator, nunca termo.* [p=0.3] E a diferença de quadrados [p=0.2] é o *L que vira "
        "retângulo.* [p=0.4] {b}Quatro: [p=0.2] contas de cabeça com os *gêmeos* [p=0.2] ao redor do *número redondo.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E onde mais isso aparece? [p=0.4] {a}Na *Matemática Financeira:* [p=0.2] dez por cento ao mês, por dois meses, "
        "[p=0.2] é um vírgula um ao quadrado, [p=0.2] um vírgula vinte e um. [p=0.2] *Vinte e um* por cento, não vinte. "
        "[p=0.2] O um por cento a mais [p=0.2] é o *i ao quadrado,* [p=0.2] o juro sobre juro. "
        "[p=0.3] {b}Na *Física,* [p=0.2] dobrar a velocidade [p=0.2] multiplica a energia de movimento por *quatro.*"),
    dict(id="07", block="onde", text=
        "{c}Na *Geometria,* [p=0.2] aumentar o lado de um quadrado em *k* [p=0.2] acrescenta *dois k xis mais k ao "
        "quadrado* à área. [p=0.3] {d}E na *equação do segundo grau:* [p=0.2] a fórmula de Bhaskara [p=0.2] nasce do "
        "*quadrado da soma.* [p=0.2] Próxima série do bloco."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}Na prova, [p=0.2] três hábitos. [p=0.4] {a}Um: [p=0.2] *teste as alternativas com um número.* [p=0.2] Troque "
        "xis por dois. [p=0.2] Se duas baterem, [p=0.2] teste outro valor. "
        "[p=0.3] {b}Dois: [p=0.2] *traduza uma frase de cada vez,* [p=0.2] e só depois junte tudo. [p=0.3] {c}Três: "
        "[p=0.2] *procure o termo do meio* nos distratores. [p=0.2] Sem ele, [p=0.2] ou pela metade, "
        "[p=0.2] é o sonho do calouro."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="09", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="10", block="vf", text=
        "{t}Um: [p=0.2] a mais b, ao quadrado, [p=0.2] é igual a *a ao quadrado mais b ao quadrado.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece que o expoente entra nas duas parcelas. [p=0.3] {g}Mas falta "
        "o *termo do meio:* [p=0.2] os *dois retângulos* do desenho. [p=0.2] A ao quadrado, [p=0.2] *mais dois a b,* "
        "[p=0.2] mais b ao quadrado."),
    dict(id="11", block="vf", text=
        "{t}Dois: [p=0.2] a menos b, ao quadrado, [p=0.2] é igual a *a ao quadrado menos b ao quadrado.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece que o menos só se copia. [p=0.3] {g}O certo é a ao quadrado, "
        "[p=0.2] *menos dois a b,* [p=0.2] mais b ao quadrado. [p=0.2] O b ao quadrado continua *positivo.*"),
    dict(id="12", block="vf", text=
        "{t}Três: [p=0.2] menos dois ao quadrado, [p=0.2] escrito *sem parênteses,* [p=0.2] vale *menos quatro.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dois ao quadrado é quatro, [p=0.2] e o sinal "
        "parece ir junto. [p=0.3] {g}Mas sem parênteses, [p=0.2] o expoente pega *só o dois.* [p=0.2] Por isso, [p=0.2] ao "
        "trocar a caixinha por um negativo, [p=0.2] *use parênteses.*"),
    dict(id="13", block="vf", text=
        "{t}Quatro: [p=0.2] cinco, [p=0.2] menos o parêntese xis menos três, [p=0.2] é igual a *oito menos xis.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente escreve cinco menos xis *menos* três. "
        "[p=0.3] {g}Mas o menos é um *espelho:* [p=0.2] troca *todos* os sinais de dentro. [p=0.2] Cinco menos xis, [p=0.2] "
        "*mais três.*"),
    dict(id="14", block="vf", text=
        "{t}Cinco: [p=0.2] dois xis mais três xis ao quadrado [p=0.2] dá *cinco xis ao cubo.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque dois mais três dá cinco. [p=0.3] {g}Mas são *frutas diferentes.* [p=0.2] Só "
        "termos *semelhantes* se somam. "),
    dict(id="15", block="vf", text=
        "{t}Seis: [p=0.2] três xis, ao quadrado, [p=0.2] é igual a *três xis ao quadrado.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o quadrado parece ser só do xis. [p=0.3] {g}Mas na *multiplicação* o expoente "
        "*entra:* [p=0.2] atinge o três também. [p=0.2] *Nove* xis ao quadrado."),
    dict(id="16", block="vf", text=
        "{t}Sete: [p=0.2] em xis mais três, [p=0.2] tudo dividido por três, [p=0.2] posso *cortar o três.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque tem três em cima e embaixo. [p=0.3] {g}Mas o três de cima "
        "é *termo,* [p=0.2] não fator. [p=0.2] *Corta-se fator, nunca termo.* "),
    dict(id="17", block="vf", text=
        "{t}Oito: [p=0.2] *o dobro da soma* de xis com três [p=0.2] é *dois xis mais três.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque a palavra *dobro* vem primeiro, [p=0.2] colada no xis. [p=0.3] {g}Mas é o dobro "
        "*da soma:* [p=0.2] primeiro a soma, [p=0.2] depois o dobro. [p=0.2] *Dois, abre parênteses, xis mais três.*"),
    dict(id="18", block="vf", text=
        "{t}E nove: [p=0.2] xis ao quadrado menos dezesseis [p=0.2] é igual a *xis mais quatro, vezes xis menos quatro.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque xis menos quatro, *ao quadrado,* "
        "[p=0.2] parece a mesma coisa. [p=0.3] {g}Mas diferença de quadrados [p=0.2] é *soma pela diferença:* [p=0.2] o L "
        "que vira retângulo. "),
    dict(id="19", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas, [p=0.2] confira a resposta *trocando xis por um número.*"),

    # ================= QUESTÃO 1: MODELAGEM (CORRIDAS) =================
    dict(id="20", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Um aplicativo cobra *cinco reais* de bandeirada [p=0.2] em *cada* corrida, [p=0.2] mais "
        "*dois reais* por quilômetro. [p=0.2] Uma pessoa fez duas corridas: [p=0.2] a primeira com *xis* quilômetros, "
        "[p=0.2] e a segunda com *três quilômetros a mais* que a primeira. [p=0.3] {b}O valor total das duas corridas é "
        "[p=0.4] {la}A, [p=0.2] quatro xis mais treze. [p=0.2] {lb}B, [p=0.2] quatro xis mais onze. [p=0.2] {lc}C, [p=0.2] "
        "quatro xis mais dez. [p=0.2] {ld}D, [p=0.2] quatro xis mais dezesseis. [p=0.2] {le}E, [p=0.2] vinte xis. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q1", text=
        "{d}Uma frase de cada vez. [p=0.3] {a}Corrida um: [p=0.2] *cinco mais dois xis.* [p=0.3] {b}Corrida dois: [p=0.2] "
        "cinco, [p=0.2] mais dois vezes *xis mais três.* [p=0.2] O aperto de mão dá dois xis mais seis. [p=0.3] {c}Juntando "
        "as frutas iguais: [p=0.2] *quatro xis mais dezesseis.* [p=0.2] {ok}*Letra D!* [p=0.3] {v}Com quatro quilômetros: [p=0.2] *trinta e dois* reais. [p=0.4] {xa}A A fez o dobro da soma *sem parênteses.* "
        "[p=0.2] {xb}A B cobrou a bandeirada uma vez só, [p=0.2] {xc}a C esqueceu os três quilômetros a mais, [p=0.2] {xe}e a "
        "E juntou frutas diferentes."),

    # ================= QUESTÃO 2: EQUIVALÊNCIA (TERRENO) =================
    dict(id="22", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Um terreno quadrado tem lado de *xis metros.* [p=0.2] Para a calçada, [p=0.2] perdeu "
        "*seis metros* em cada lado, [p=0.2] e continuou quadrado. [p=0.3] {b}A área que sobrou, em metros quadrados, é "
        "[p=0.4] {la}A, [p=0.2] xis ao quadrado menos trinta e seis. [p=0.2] {lb}B, [p=0.2] xis ao quadrado menos doze xis "
        "mais trinta e seis. [p=0.2] {lc}C, [p=0.2] xis ao quadrado menos seis xis mais trinta e seis. [p=0.2] {ld}D, "
        "[p=0.2] xis ao quadrado menos doze xis menos trinta e seis. [p=0.2] {le}E, [p=0.2] xis ao quadrado mais doze xis "
        "mais trinta e seis. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q2", text=
        "{d}O lado novo é *xis menos seis.* [p=0.2] A área é esse lado ao quadrado. [p=0.3] {a}Agora, [p=0.2] o *teste do "
        "número:* [p=0.2] xis igual a dez. [p=0.2] Sobra um quadrado de lado quatro: [p=0.2] área *dezesseis.* [p=0.3] {b}Só "
        "uma alternativa dá dezesseis: [p=0.2] {ok}*a letra B.* [p=0.3] {v}E o desenvolvimento confirma: [p=0.2] o termo do "
        "meio é duas vezes xis vezes seis, [p=0.2] *doze xis.* [p=0.4] {xa}A A é o sonho do calouro. [p=0.2] {xc}A C pôs o "
        "termo do meio pela metade. [p=0.2] {xd}A D deixou o trinta e seis negativo, [p=0.2] {xe}e a E trocou o sinal."),

    # ================= QUESTÃO 3: ÁREA (PRAÇA AMPLIADA) =================
    dict(id="24", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Uma praça quadrada tem lado de *xis metros.* [p=0.2] A prefeitura vai aumentar *cada "
        "lado* em *quatro metros.* [p=0.3] {b}O *aumento* da área da praça, em metros quadrados, é [p=0.4] {la}A, [p=0.2] "
        "dezesseis. [p=0.2] {lb}B, [p=0.2] oito xis. [p=0.2] {lc}C, [p=0.2] quatro xis mais dezesseis. [p=0.2] {ld}D, "
        "[p=0.2] xis ao quadrado mais oito xis mais dezesseis. [p=0.2] {le}E, [p=0.2] oito xis mais dezesseis. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q3", text=
        "{d}Desenhe o quadrado novo. [p=0.3] {a}Em volta do antigo, [p=0.2] aparecem *dois retângulos* de xis por "
        "quatro, [p=0.2] e um *quadradinho* de quatro por quatro no canto. [p=0.3] {b}Aumento: [p=0.2] oito xis [p=0.2] mais "
        "dezesseis. [p=0.2] {ok}*Letra E!* [p=0.3] {v}Confira com xis igual a dez: [p=0.2] cento e noventa e seis menos cem, "
        "[p=0.2] *noventa e seis.* [p=0.4] {xa}A A é o sonho do calouro. [p=0.2] {xb}A B esqueceu o quadradinho do canto. "
        "[p=0.2] {xc}A C contou um retângulo só, [p=0.2] {xd}e a D deu a área nova inteira, [p=0.2] não o aumento."),

    # ================= QUESTÃO 4: FRAÇÃO ALGÉBRICA =================
    dict(id="26", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Para xis diferente de dois, [p=0.2] a fração *três xis ao quadrado menos doze,* "
        "[p=0.2] sobre *xis ao quadrado menos quatro xis mais quatro,* [p=0.3] {b}é igual a [p=0.4] {la}A, [p=0.2] três "
        "vezes xis mais dois, sobre xis menos dois. [p=0.2] {lb}B, [p=0.2] três. [p=0.2] {lc}C, [p=0.2] nove sobre quatro "
        "xis menos quatro. [p=0.2] {ld}D, [p=0.2] xis mais dois, sobre xis menos dois. [p=0.2] {le}E, [p=0.2] três vezes xis "
        "menos dois, sobre xis mais dois. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q4", text=
        "{d}Fatore em cima e embaixo, [p=0.2] *começando pelo fator comum.* [p=0.3] {a}Em cima: [p=0.2] três, vezes xis ao "
        "quadrado menos quatro, [p=0.2] que é o L que vira retângulo: [p=0.2] *três, xis mais dois, xis menos dois.* [p=0.3] "
        "{b}Embaixo: [p=0.2] *xis menos dois, ao quadrado.* [p=0.3] {c}Corte o fator xis menos dois: [p=0.2] três vezes xis "
        "mais dois, [p=0.2] sobre xis menos dois. [p=0.2] {ok}*Letra A!* [p=0.3] {v}Confira com xis igual a três: [p=0.2] "
        "quinze sobre um, [p=0.2] *quinze.*  [p=0.4] {xb}A B fatorou como quadrado. [p=0.2] {xc}A C "
        "cortou termo. [p=0.2] {xd}A D perdeu o três, [p=0.2] {xe}e a E inverteu."),

    # ================= QUESTÃO 5: CONTA SEM CALCULADORA =================
    dict(id="28", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Um condomínio vai cobrir com grama [p=0.2] um terreno retangular de *trezentos e "
        "dois* metros [p=0.2] por *duzentos e noventa e oito* metros. [p=0.3] {b}Sem calculadora, [p=0.2] a área do terreno, "
        "em metros quadrados, é [p=0.4] {la}A, [p=0.2] noventa mil e quatro. [p=0.2] {lb}B, [p=0.2] noventa mil. [p=0.2] "
        "{lc}C, [p=0.2] oitenta e nove mil novecentos e noventa e seis. [p=0.2] {ld}D, [p=0.2] oitenta e nove mil novecentos "
        "e noventa e oito. [p=0.2] {le}E, [p=0.2] oitenta e oito mil oitocentos e quatro. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="29", block="q5", text=
        "{d}Os dois números são *gêmeos* [p=0.2] ao redor do trezentos. [p=0.3] {a}Trezentos mais dois, [p=0.2] vezes "
        "trezentos menos dois: [p=0.2] *soma pela diferença.* [p=0.3] {b}Trezentos ao quadrado, [p=0.2] noventa mil, "
        "[p=0.2] menos dois ao quadrado, [p=0.2] quatro. [p=0.2] *Oitenta e nove mil novecentos e noventa e seis.* [p=0.2] "
        "{ok}*Letra C!* [p=0.3] {v}Um pouco *menos* que noventa mil: [p=0.2] faz sentido. [p=0.4] {xb}A B aproximou [p=0.2] e ignorou o quadrado do passo. [p=0.2] {xa}A A somou esse quadrado. "
        "[p=0.2] {xd}A D tirou dois, e não dois ao quadrado, [p=0.2] {xe}e a E fez duzentos e noventa e oito ao quadrado."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="30", block="checklist", text=
        "{t}O checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Tradução, [p=0.2] valor numérico [p=0.2] e operações: "
        "[p=0.2] episódio um. [p=0.3] {c}Produtos notáveis, [p=0.2] o desenho do quadrado [p=0.2] e o cubo: [p=0.2] "
        "episódio dois."),
    dict(id="31", block="checklist", text=
        "{a}Fatoração, [p=0.2] frações [p=0.2] e a ao quadrado mais b ao quadrado: [p=0.2] episódio três. [p=0.3] {b}Contas "
        "de cabeça: [p=0.2] episódio quatro. [p=0.3] {c}E o teste de alternativas: [p=0.2] *este* episódio. [p=0.4] {d}O que "
        "você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="32", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta "
        "por cento. [p=0.4] {c}E pelo menos *dez* delas de *modelagem:* [p=0.2] escrever a expressão a partir de um texto."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}O próximo assunto é *Equações e inequações do primeiro grau,* [p=0.3] {b}onde estas ferramentas passam a "
        "*encontrar valores desconhecidos.*"),
    dict(id="34", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de expressões algébricas está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
