# Roteiro — Função Composta e Função Inversa, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino
#   (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/30-funcao-composta-inversa.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9). As 5 questões são INÉDITAS (números e erros do prompt do usuário).
#   Progressão aritmética: só a ponte.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (números por extenso; "f ∘ g" lido "efe bola gê"; o gancho só acrescenta,
#   depois delas, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 MÁQUINAS EM FILA · DE DENTRO PARA FORA · MEIA E SAPATO (ícone: duas máquinas em fila) ·
#   ep2 A GRANDEZA-PONTE QUE SOME · "A DE DENTRO RECEBE O QUE VOCÊ TEM" (ícone: ponte que some) ·
#   ep3 O CAMINHO DE VOLTA · DESFAZER NA ORDEM CONTRÁRIA · f⁻¹ DESFAZ, 1/f VIRA DE CABEÇA PARA BAIXO (ícone: esteira
#       rodando ao contrário) ·
#   ep4 CADA SAÍDA COM UM DONO · O ESPELHO EM y = x · EM TABELA, PROCURE NAS SAÍDAS (ícone: espelho na diagonal).
#   O ep. 4 foi feito em paralelo: as analogias dele vêm do prompt do vídeo 4 (roteiros.md).
# Prática de recuperação: a cena 04 abre com uma pergunta e pausa antes do índice; cada V/F e cada questão têm pausa.
# O que a prova cobra (seção 01): encadear modelos · inverter fórmulas · tabelas encadeadas ou códigos · gráfico da
#   inversa. O que mais rende: a ordem (a de dentro age primeiro) e inverter é trocar entrada e saída.
# Onde aparece (seção 10): Física (F = 1,8C + 32 e C = (F − 32)/1,8; posição → velocidade → energia) · Química
#   (pH = −log[H⁺] e [H⁺] = 10^(−pH)) · Matemática Financeira (câmbio e impostos) · Linguagens e TIC (codificar e
#   decodificar).
# Estratégia (seção 09): 3 hábitos — grandeza intermediária · teste com um ponto · tabelas de dentro para fora.
# V/F (os 9 erros da seção 11, NA ORDEM do material). DESVIO NOSSO (marcado): para o jogo não ter resposta previsível,
#   três frases aparecem na versão CERTA (verdadeiras: 2, 6 e 9); as outras seis são o erro (falsas). Números NOSSOS
#   (fora das Q1–Q9 e das questões dos eps. 1 a 4), com f(x) = x + 1 e g(x) = 3x:
#   1 F em f(g(x)), f age primeiro (g primeiro: f(g(2)) = f(6) = 7) · 2 V f(g(x)) e g(f(x)) podem dar resultados
#   diferentes (7 e 9) · 3 F f(g(x)) = f(x) · g(x) (3 · 6 = 18, não 7) · 4 F f(x) = x² + 1 ⇒ f(x + 2) = x² + 3
#   ((x + 2)² + 1 = x² + 4x + 5; teste x = 1: 10 e 4) · 5 F f⁻¹(x) = 1/f(x) (f(x) = 2x: f⁻¹(8) = 4, 1/f(8) = 1/16) ·
#   6 V a inversa de 3x + 2 é (x − 2)/3 (f(1) = 5 e (5 − 2)/3 = 1) · 7 F x² tem inversa √x em todos os reais
#   ((−3)² = 3² = 9; só com x ≥ 0) · 8 F o gráfico da inversa é o reflexo no eixo y (na reta y = x; (2, 5) vira (5, 2))
#   · 9 V em tabela, para f⁻¹(b), procure b nas SAÍDAS.
# QUESTÕES INÉDITAS (do prompt; conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro
#   clássico; a ordem das letras é nossa, exceto a Q5, que o prompt já fixa):
#   Q1 US$ 50,00, dólar a R$ 5,00, imposto de 60% sobre o valor em reais: F(r(d)) = 1,6 · 5d = 8d → R$ 400,00 → E.
#      A R$ 80,00 (1,6 · 50, sem converter) · B R$ 250,00 (sem imposto) · C R$ 280,00 (60% de 50 dólares = 30 somado
#      aos 250 reais) · D R$ 330,00 (somou 5 + 1,6 em vez de multiplicar: 6,6 · 50). Teste com um ponto: US$ 1 →
#      R$ 5 → R$ 8.
#   Q2 f(x) = x + 5, g(x) = x²: f(g(3)) = f(9) = 14 → B. A 9 (parou em g(3)) · C 17 (f(3) + g(3)) · D 64 (g(f(3)),
#      ordem trocada) · E 72 (f(3) · g(3)).
#   Q3 F = 1,8C + 32, 104 °F: (104 − 32) ÷ 1,8 = 40 °C → D. A 219,2 (aplicou a fórmula, em vez de desfazer) ·
#      B ≈ 75,6 (somou o 32) · C 72 (esqueceu de dividir) · E ≈ 25,8 (dividiu antes de subtrair). Conferência:
#      1,8 · 40 + 32 = 104.
#   Q4 f invertível passa por (−2, 5) → f⁻¹ passa por (5, −2) → C. A (−2, 5) (o próprio ponto de f) · B (2, −5)
#      (trocou os sinais) · D (−5, 2) (trocou e mudou os sinais: espelho errado) · E (5, −1/2) (usou 1/f).
#   Q5 tabela x = 1, 2, 3, 4; f = 2, 4, 1, 3; g = 3, 1, 4, 2: g(4) = 2; o 2 está nas saídas de f na coluna x = 1 → 1 → A.
#      B 2 (parou em g(4)) · C 3 (ignorou g: f(4)) · D 4 (usou f no lugar de f⁻¹: f(g(4)) = f(2)) · E "f não tem
#      inversa" (falso: cada saída de f aparece uma única vez).
# Gabaritos: E, B, D, C, A.
# Atalhos (verde): os 3 hábitos (cenas 08 e 09) · "teste com um ponto" na Q1 e na Q3 · "(a, b) vira (b, a)" na Q4.
# Checklist (seção 13) → episódio (como o prompt pede): ordem e lei da composta → ep1 · contexto e função escondida → ep2 ·
#   calcular inversas → ep3 · bijetora, gráfico e tabelas → ep4.
# Meta (prompt e material): 25 questões, 18 acertos, com pelo menos oito de contexto.
# Ponte (do usuário): Progressão aritmética.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de função composta e inversa: câmbio, termômetro e tabela · Matemática ENEM, Composta e Inversa ep. 5"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, passo a passo. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}O ENEM quase nunca escreve *efe bola gê.* [p=0.4] {b}Ele escreve *\"o custo depende das peças, que dependem "
        "do tempo\"* [p=0.3] ou *\"quanto ele andou, se pagou trinta e sete reais\".* [p=0.4] {c}Hoje você treina para "
        "reconhecer *composta e inversa sem o símbolo.* [p=0.4] {d}Nove frases de verdadeiro ou falso [p=0.2] e cinco "
        "questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Encadear modelos:* [p=0.2] o custo depende das peças, que dependem do "
        "tempo. [p=0.3] {b}*Inverter uma fórmula:* [p=0.2] dada a temperatura em Fahrenheit, achar em Celsius. [p=0.3] "
        "{c}Ler *tabelas encadeadas* [p=0.2] ou um código para decifrar. [p=0.3] {d}E reconhecer o *gráfico da "
        "inversa.*"),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.3] Duas habilidades. [p=0.4] {a}Primeiro, [p=0.2] *a ordem:* [p=0.2] em efe de gê "
        "de xis, [p=0.2] quem age primeiro é o *gê, a de dentro.* [p=0.4] {b}Segundo: [p=0.2] *inverter é trocar "
        "entrada e saída.* [p=0.3] Quase todo distrator troca a ordem [p=0.2] ou confunde a inversa com *um sobre.*"),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] tente lembrar: [p=0.2] em efe de gê de xis, [p=0.2] quem trabalha *primeiro?* "
        "[p=1.2] {a}Um: [p=0.2] as *máquinas em fila.* [p=0.2] O que sai de uma entra na outra, [p=0.2] e se lê *de "
        "dentro para fora.* [p=0.2] A ordem importa, como *meia e sapato.* [p=0.4] {b}Dois: [p=0.2] a grandeza que "
        "aparece nas duas fórmulas é a *ponte:* [p=0.2] você atravessa e ela *some.* [p=0.2] E a de dentro *recebe o "
        "que você tem.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] a inversa é o *caminho de volta.* [p=0.2] Desfaça *na ordem contrária:* [p=0.2] primeiro o "
        "sapato, depois a meia. [p=0.2] E efe inversa *desfaz;* [p=0.2] um sobre efe só vira de cabeça para baixo. "
        "[p=0.4] {b}Quatro: [p=0.2] para voltar, *cada saída precisa de um dono.* [p=0.2] O gráfico da inversa é o "
        "*espelho na reta y igual a xis,* [p=0.2] e em tabela, *procure nas saídas.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}Na *Física,* [p=0.2] Celsius para Fahrenheit e Fahrenheit para Celsius "
        "[p=0.2] são *inversas.* [p=0.2] E a energia em função do tempo, passando pela velocidade, [p=0.2] é uma "
        "*composta.* [p=0.3] {b}Na *Química,* [p=0.2] o pê agá é menos o log da concentração, [p=0.2] e a concentração "
        "é dez elevado a menos pê agá: [p=0.2] *um desfaz o outro.*"),
    dict(id="07", block="onde", text=
        "{c}Na *Matemática Financeira,* [p=0.2] converter o dólar e depois cobrar o imposto [p=0.2] é *compor;* [p=0.2] "
        "voltar do preço final ao inicial é *inverter.* [p=0.3] {d}E em *Linguagens e tecnologia,* [p=0.2] codificar "
        "uma mensagem é aplicar uma função; [p=0.2] *decodificar é aplicar a inversa.*"),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Três hábitos. [p=0.4] {a}Um: [p=0.2] *ache a grandeza intermediária.* [p=0.2] "
        "Num texto com duas fórmulas, [p=0.2] sublinhe a grandeza que aparece *nas duas:* [p=0.2] peças, altitude, "
        "valor em reais. [p=0.2] {a2}Ela é a ponte: [p=0.2] substitua [p=0.2] e ela *some da resposta.*"),
    dict(id="09", block="habitos", text=
        "{b}Dois: [p=0.2] *teste as alternativas com um ponto.* [p=0.2] Se efe de um é três, [p=0.2] a inversa certa "
        "leva o três *de volta ao um.* [p=0.4] {c}Três: [p=0.2] em tabelas, *de dentro para fora.* [p=0.2] Para a "
        "composta, o resultado da primeira tabela vira entrada da segunda. [p=0.2] Para a inversa, [p=0.2] *procure o "
        "número nas saídas.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] em efe de gê de xis, [p=0.2] quem age primeiro é o *efe.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque a gente lê da esquerda para a direita, [p=0.2] e o efe vem antes. "
        "[p=0.3] {g}Mas é *de dentro para fora:* [p=0.2] primeiro o gê, [p=0.2] depois o efe."),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] com efe de xis igual a xis mais um [p=0.2] e gê de xis igual a três xis, [p=0.2] efe de gê "
        "de dois e gê de efe de dois [p=0.2] dão resultados *diferentes.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* "
        "[p=0.3] {e}Parece falso porque soma e multiplicação aceitam qualquer ordem. [p=0.3] {g}Mas é *meia e "
        "sapato:* [p=0.2] efe de seis dá *sete;* [p=0.2] gê de três dá *nove.*"),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] efe de gê de xis [p=0.2] é efe de xis *vezes* gê de xis. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque os parênteses lembram multiplicação. [p=0.3] {g}Mas compor é *pôr uma "
        "dentro da outra.* [p=0.2] Com as mesmas funções, [p=0.2] a composta em dois dá *sete,* [p=0.2] e o produto "
        "dá *dezoito.*"),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] se efe de xis é xis ao quadrado mais um, [p=0.2] então efe de xis mais dois [p=0.2] é "
        "*xis ao quadrado mais três.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque dá vontade de "
        "elevar só o xis [p=0.2] e somar o dois depois. [p=0.3] {g}Mas a expressão entra *inteira, entre parênteses:* "
        "[p=0.2] xis mais dois, ao quadrado, mais um. [p=0.2] Teste com xis igual a um: [p=0.2] dez, e não quatro."),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] efe inversa de xis [p=0.2] é *um sobre efe de xis.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o menos um parece expoente. [p=0.3] {g}Mas efe inversa *desfaz.* "
        "[p=0.2] Com efe de xis igual a dois xis, [p=0.2] a inversa leva o oito ao *quatro;* [p=0.2] um sobre efe dá "
        "*um dezesseis avos.*"),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] a inversa de *três xis mais dois* [p=0.2] é *xis menos dois, sobre três.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade de dividir primeiro. [p=0.3] {g}Mas é "
        "*sapato antes da meia:* [p=0.2] o último passo foi somar dois, [p=0.2] então ele sai primeiro. [p=0.2] Teste: "
        "[p=0.2] efe de um é cinco, [p=0.2] e cinco menos dois, sobre três, *volta ao um.*"),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] xis ao quadrado tem inversa *raiz de xis* [p=0.2] em todos os números reais. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a raiz parece desfazer o quadrado. [p=0.3] {g}Mas três "
        "e menos três dão *o mesmo nove:* [p=0.2] a saída tem *dois donos.* [p=0.2] Só com xis maior ou igual a zero."),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] o gráfico da inversa é o reflexo do gráfico de efe [p=0.2] no *eixo y.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o eixo y é o espelho mais famoso. [p=0.3] {g}Mas o espelho é a "
        "*diagonal y igual a xis:* [p=0.2] o ponto dois, cinco [p=0.2] vira *cinco, dois.*"),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] numa tabela, [p=0.2] para achar efe inversa de bê, [p=0.2] você procura o bê na linha das "
        "*saídas* de efe. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o costume é "
        "procurar na linha de cima. [p=0.3] {g}Mas a inversa *lê a tabela de baixo para cima:* [p=0.2] ache o bê nas "
        "saídas [p=0.2] e leia a entrada."),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *ache a ordem* ou *o caminho de volta* antes de qualquer conta, "
        "[p=0.2] e *teste com um ponto* no fim."),

    # ================= QUESTÃO 1: CÂMBIO E IMPOSTO =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Um produto custa *cinquenta dólares.* [p=0.2] O dólar está a *cinco reais,* [p=0.2] "
        "e sobre o valor em reais incide um imposto de *sessenta por cento.* [p=0.3] {b}Quanto a pessoa paga, em "
        "reais? [p=0.4] {la}A, [p=0.2] oitenta reais. [p=0.2] {lb}B, [p=0.2] duzentos e cinquenta. [p=0.2] {lc}C, "
        "[p=0.2] duzentos e oitenta. [p=0.2] {ld}D, [p=0.2] trezentos e trinta. [p=0.2] {le}E, [p=0.2] quatrocentos. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Duas máquinas em fila. [p=0.2] A primeira converte: [p=0.2] *cinco vezes os dólares.* [p=0.2] A segunda "
        "cobra o imposto: [p=0.2] *um vírgula seis vezes os reais.* [p=0.3] {a}Em fila: [p=0.2] um vírgula seis vezes "
        "cinco, [p=0.2] *oito vezes os dólares.* [p=0.2] Oito vezes cinquenta: [p=0.2] *quatrocentos reais.* [p=0.2] "
        "{v}Teste com um dólar: [p=0.2] vira cinco reais, [p=0.2] e com imposto, oito. [p=0.2] {ok}*Letra E!* [p=0.4] "
        "{xb}A B esqueceu o imposto. [p=0.2] {xa}A A cobrou o imposto *sem converter.* [p=0.2] {xc}A C calculou o "
        "imposto *em dólar* [p=0.2] e somou aos reais. [p=0.2] {xd}E a D *somou* cinco com um vírgula seis, [p=0.2] em "
        "vez de multiplicar."),

    # ================= QUESTÃO 2: A ORDEM =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Sejam efe de xis igual a *xis mais cinco* [p=0.2] e gê de xis igual a *xis ao "
        "quadrado.* [p=0.3] {b}Quanto vale *efe de gê de três?* [p=0.4] {la}A, [p=0.2] nove. [p=0.2] {lb}B, [p=0.2] "
        "catorze. [p=0.2] {lc}C, [p=0.2] dezessete. [p=0.2] {ld}D, [p=0.2] sessenta e quatro. [p=0.2] {le}E, [p=0.2] "
        "setenta e dois. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}De dentro para fora. [p=0.2] Primeiro o gê: [p=0.2] três ao quadrado, *nove.* [p=0.3] {a}O nove entra no "
        "efe: [p=0.2] nove mais cinco, *catorze.* [p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A parou no meio do caminho. "
        "[p=0.2] {xd}A D trocou a ordem: [p=0.2] calculou gê de efe, [p=0.2] oito ao quadrado. [p=0.2] {xc}A C "
        "*somou* as duas, [p=0.2] {xe}e a E *multiplicou.*"),

    # ================= QUESTÃO 3: DESFAZER A CONVERSÃO =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}A temperatura em Fahrenheit é *um vírgula oito vezes Celsius, mais trinta e "
        "dois.* [p=0.2] Um termômetro marca *cento e quatro graus Fahrenheit.* [p=0.3] {b}Quanto é, em Celsius? "
        "[p=0.4] {la}A, [p=0.2] duzentos e dezenove vírgula dois. [p=0.2] {lb}B, [p=0.2] cerca de setenta e cinco "
        "vírgula seis. [p=0.2] {lc}C, [p=0.2] setenta e dois. [p=0.2] {ld}D, [p=0.2] quarenta. [p=0.2] {le}E, [p=0.2] "
        "cerca de vinte e cinco vírgula oito. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}O caminho de volta. [p=0.2] Na ida: [p=0.2] *vezes um vírgula oito,* [p=0.2] depois *mais trinta e dois.* "
        "[p=0.3] {a}Na volta, na ordem contrária: [p=0.2] primeiro *menos trinta e dois,* [p=0.2] setenta e dois; "
        "[p=0.2] depois *dividido por um vírgula oito,* [p=0.2] *quarenta graus.* [p=0.2] {v}Teste: [p=0.2] um vírgula "
        "oito vezes quarenta, mais trinta e dois, *cento e quatro.* [p=0.2] {ok}*Letra D!* [p=0.4] {xe}A E dividiu "
        "*antes* de subtrair. [p=0.2] {xc}A C esqueceu de dividir. [p=0.2] {xb}A B somou o trinta e dois, [p=0.2] {xa}e "
        "a A aplicou a fórmula de ida."),

    # ================= QUESTÃO 4: PONTO DA INVERSA =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}O gráfico de uma função invertível efe [p=0.2] passa pelo ponto *menos dois, "
        "cinco.* [p=0.3] {b}Por qual ponto passa o gráfico da *inversa?* [p=0.4] {la}A, [p=0.2] menos dois, cinco. "
        "[p=0.2] {lb}B, [p=0.2] dois, menos cinco. [p=0.2] {lc}C, [p=0.2] cinco, menos dois. [p=0.2] {ld}D, [p=0.2] "
        "menos cinco, dois. [p=0.2] {le}E, [p=0.2] cinco, menos um meio. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Efe leva o menos dois ao cinco. [p=0.2] A inversa faz o *caminho de volta:* [p=0.2] leva o cinco ao *menos "
        "dois.* [p=0.3] {a}No espelho da diagonal, [p=0.2] *a, bê vira bê, a:* [p=0.2] o ponto *cinco, menos dois.* "
        "[p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A é o ponto do próprio efe. [p=0.2] {xb}A B e {xd}a D mexeram nos "
        "*sinais:* [p=0.2] espelho errado. [p=0.2] {xe}E a E usou *um sobre,* [p=0.2] e o menos um não é expoente."),

    # ================= QUESTÃO 5: TABELA =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}A tabela mostra efe e gê para xis igual a um, dois, três e quatro. [p=0.3] "
        "{b}Calcule *efe inversa de gê de quatro.* [p=0.4] {la}A, [p=0.2] um. [p=0.2] {lb}B, [p=0.2] dois. [p=0.2] "
        "{lc}C, [p=0.2] três. [p=0.2] {ld}D, [p=0.2] quatro. [p=0.2] {le}E, [p=0.2] não é possível calcular, [p=0.2] "
        "porque efe não tem inversa. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}De dentro para fora. [p=0.2] Na linha do gê, coluna quatro: [p=0.2] *gê de quatro é dois.* [p=0.3] {a}Agora "
        "a inversa: [p=0.2] procure o dois *nas saídas de efe.* [p=0.2] Ele está na coluna *xis igual a um.* [p=0.2] "
        "Resposta: *um.* [p=0.2] {ok}*Letra A!* [p=0.4] {xb}A B parou no gê. [p=0.2] {xc}A C ignorou o gê [p=0.2] e "
        "calculou efe de quatro. [p=0.2] {xd}A D usou efe no lugar da inversa. [p=0.2] {xe}E a E está errada: [p=0.2] "
        "cada saída de efe aparece *uma vez só,* [p=0.2] então efe tem inversa."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}A ordem e a lei da composta: [p=0.2] episódio um. [p=0.3] {c}Encadear "
        "fórmulas de um texto e achar a função escondida: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Calcular inversas [p=0.2] e não confundir com um sobre efe: [p=0.2] episódio três. [p=0.3] {b}Bijetora, "
        "o gráfico no espelho e as tabelas: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] "
        "reveja o episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte e cinco questões* [p=0.2] {b}e acerte pelo menos *dezoito.* [p=0.4] {c}E "
        "pelo menos *oito* delas de contexto: [p=0.2] fórmulas encadeadas [p=0.2] ou conversões para inverter."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Progressão aritmética:* [p=0.3] {b}uma função afim vista só nos números naturais, "
        "[p=0.3] {c}em que cada termo soma *sempre o mesmo tanto.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de função composta e função inversa "
        "está completa. [p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
