# Roteiro — Números Complexos, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/36-numeros-complexos.html — seções 01, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9). As 5 questões são INÉDITAS (dados, alternativas e motivos das erradas do PROMPT).
#   Último assunto do bloco de Álgebra e Funções.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (números e símbolos falados por extenso).
# As "três ideias" do gancho (na tela): Δ < 0 tem um par conjugado · i² = −1 em toda conta · todo complexo é um ponto.
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 o SUPERPODER do i (i² = −1) · o RELÓGIO DE QUATRO HORAS das potências · as GÊMEAS ESPELHADAS (ícone: relógio) ·
#   ep2 o PEDÁGIO do i² · o conjugado como ESPELHO · LIMPAR O i DO ANDAR DE BAIXO (ícone: cancela de pedágio) ·
#   ep3 o ENDEREÇO NO MAPA · o módulo como DIAGONAL DO RETÂNGULO · a MANIVELA de 90° (ícone: manivela) ·
#   ep4 o ENDEREÇO DO RADAR (distância e direção) · ESTICAR E GIRAR na multiplicação (ícone: radar).
# Prática de recuperação: a cena 04 abre com uma pergunta e pausa antes do índice; cada V/F e cada questão têm pausa.
# O que a prova cobra (seção 01): Δ < 0 (sem raízes reais, com par conjugado) · forma algébrica e potências de i ·
#   geometria no plano (módulo = distância, vezes i = giro de 90°) · forma trigonométrica para potências grandes.
# Onde aparece (seção 10): Polinômios · Trigonometria · Geometria Analítica · Física e engenharia (corrente alternada e
#   ondas: módulo = amplitude, argumento = fase).
# Estratégia (seção 10): 4 hábitos — potência de i → resto por 4 · divisão → conjugado e conferência · potência alta →
#   forma trigonométrica ou uma potência pequena simples · pergunta geométrica → desenhe o ponto.
# V/F (os 9 erros da seção 11, NA ORDEM do prompt). DESVIO NOSSO (marcado, como nas revisões anteriores): para o jogo não
#   ter resposta previsível, três frases aparecem na versão CERTA (verdadeiras: 2, 5 e 7); as outras seis são o erro
#   (falsas). No item 4 (dividir parte por parte) o exemplo é NOSSO: (4 + 2i) ÷ (1 + i) = 3 − i.
#   Conferido em trabalho/conferir_questoes.py.
# QUESTÕES INÉDITAS (dados exatos do prompt; conferidas em trabalho/conferir_questoes.py):
#   Q1 i^45 + i^62: 45 = 4 · 11 + 1 → i; 62 = 4 · 15 + 2 → −1 → −1 + i (B). A 1 + i usa i² = 1 · C −1 − i erra o
#      resto de 45 · D 0 acha que potências diferentes se anulam · E −i multiplica (i^107).
#   Q2 (7 + i) ÷ (1 + i) × (1 − i): (8 − 6i) ÷ 2 = 4 − 3i (C); conferência (4 − 3i)(1 + i) = 7 + i. A esquece o ÷ 2 ·
#      D troca as partes · E erra o sinal da imaginária. CORREÇÃO DO PROMPT (marcada): o prompt diz que a B (7 + i)
#      "divide parte por parte", mas parte por parte (7 ÷ 1 e i ÷ i) daria 8. A B mantém o numerador: dividiu cada parte
#      só pelo 1, como se o i de baixo não existisse. É assim que o vídeo explica.
#   Q3 x² − 2x + 10: Δ = −36, x = (2 ± 6i) ÷ 2 = 1 ± 3i (A); soma 2, produto 10. B usa b em vez de −b · C divide só a
#      parte real · D não divide por 2a · E vale só nos reais.
#   Q4 giro horário = × (−i): −i(5 + 2i) = 2 − 5i (D); (a, b) → (b, −a). A anti-horário · B conjugado · C 180° · E troca
#      as partes sem sinal.
#   Q5 (1 − i)² = −2i; (−2i)² = −4 (B); De Moivre: (√2)⁴ = 4 e 4 · 315° = 1 260° = 3 voltas + 180°. A esquece i² = −1 ·
#      C módulo 2 · D ângulo 270° · E −2i · 4.
# Gabaritos: B, C, A, D, B (letras e alternativas do prompt).
# Atalhos (verde): os 4 hábitos (cenas 08 e 09) · "dois últimos algarismos" na Q1 · "confira multiplicando de volta" na
#   Q2 · "soma e produto conferem" na Q3 · "(a, b) vira (b, −a)" na Q4 · "potência pequena que dá número simples" na Q5.
# Checklist (seção 13) → episódio (como o prompt pede): i, forma algébrica, Δ < 0 e potências → ep1 · operações,
#   conjugado, divisão e equações com z̄ → ep2 · plano, módulo, distância e giros → ep3 · forma trigonométrica e
#   De Moivre → ep4.
# Meta (prompt e material): 20 questões, 14 acertos, com pelo menos cinco de divisão ou potência e três no plano.
# Ponte (do usuário): Ângulos, retas paralelas e transversais (abre o bloco de Geometria Plana).
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão: potências de i, divisão, giros e as pegadinhas | Números Complexos Ep. 5"
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
        "{a}Sendo honesto, como o próprio material: [p=0.3] números complexos *quase não caem de forma direta* no ENEM. "
        "[p=0.5] {b}Mas *três ideias* daqui [p=0.2] se reaproveitam na prova e nos vestibulares. [p=0.5] {e}Hoje você "
        "garante as três."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que aparece, quando aparece? [p=0.4] {a}*Delta negativo:* [p=0.2] nenhuma raiz real, [p=0.2] mas um par "
        "de raízes conjugadas. [p=0.3] {b}*Contas na forma a mais b i,* [p=0.2] e as potências de i. [p=0.3] "
        "{c}*Geometria no plano:* [p=0.2] o módulo é uma distância, [p=0.2] e vezes i é um giro de noventa graus. "
        "[p=0.3] {d}E a *forma trigonométrica,* [p=0.2] para potências grandes."),
    dict(id="03", block="rende", text=
        "{t}E a dica que mais rende, [p=0.2] do próprio material: [p=0.3] {a}trate o i como uma *letra qualquer.* "
        "[p=0.4] {b}E, no fim, [p=0.2] *troque i ao quadrado por menos um.* [p=0.3] Quase todo erro do assunto [p=0.2] "
        "vem de esquecer essa troca, [p=0.2] ou de fazer com o sinal errado."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] tente lembrar: [p=0.2] *quanto vale i ao quadrado?* [p=1.2] {a}Um: [p=0.2] o "
        "*relógio.* [p=0.2] O i é uma letra com *superpoder:* [p=0.2] ao quadrado, vira menos um. [p=0.2] As potências "
        "giram num *relógio de quatro horas,* [p=0.2] e as raízes do delta negativo [p=0.2] são *gêmeas espelhadas.* "
        "[p=0.4] {b}Dois: [p=0.2] a *cancela.* [p=0.2] O i ao quadrado paga *pedágio* e vira menos um, [p=0.2] o "
        "conjugado é um *espelho,* [p=0.2] e na divisão você *limpa o i do andar de baixo.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] a *manivela.* [p=0.2] Todo complexo é um *endereço no mapa,* [p=0.2] o módulo é a *diagonal "
        "do retângulo,* [p=0.2] e vezes i *gira a manivela* noventa graus. [p=0.4] {b}Quatro: [p=0.2] o *radar.* "
        "[p=0.2] A forma trigonométrica é o *endereço do radar:* [p=0.2] distância e direção. [p=0.2] E multiplicar é "
        "*esticar e girar.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E nas outras áreas? [p=0.4] {a}Em *Polinômios,* [p=0.2] as raízes não reais [p=0.2] vêm em *pares "
        "conjugados.* [p=0.3] {b}Na *Trigonometria,* [p=0.2] a forma polar usa o ciclo, [p=0.2] e multiplicar *soma os "
        "ângulos.*"),
    dict(id="07", block="onde", text=
        "{c}Na *Geometria Analítica,* [p=0.2] a distância entre pontos [p=0.2] e a rotação de figuras. [p=0.3] {d}E na "
        "*Física e na engenharia,* [p=0.2] corrente alternada e ondas: [p=0.2] o módulo é a *amplitude,* [p=0.2] e o "
        "argumento é a *fase.*"),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 10) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Quatro hábitos. [p=0.4] {a}Um: [p=0.2] *potência de i? Resto por quatro.* "
        "[p=0.2] Só o resto importa. [p=0.4] {b}Dois: [p=0.2] *divisão?* [p=0.2] Multiplique em cima e embaixo pelo "
        "*conjugado do denominador,* [p=0.2] e confira multiplicando de volta."),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] *potência alta de algo simples?* [p=0.2] Forma trigonométrica, [p=0.2] ou uma potência "
        "pequena que dá um número simples, [p=0.2] como *um mais i, ao quadrado, igual a dois i.* [p=0.4] {d}Quatro: "
        "[p=0.2] *pergunta geométrica?* [p=0.2] *Desenhe o ponto.* [p=0.2] Um esboço elimina o quadrante errado."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] *i ao quadrado é um.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque um "
        "número vezes ele mesmo [p=0.2] costuma dar positivo. [p=0.3] {g}Mas esse é o *superpoder* do i: [p=0.2] i ao "
        "quadrado é *menos um.* [p=0.2] É a definição."),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] a parte imaginária de *três menos quatro i* [p=0.2] é *menos quatro.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a gente quer levar o i junto. [p=0.3] {g}Mas a parte "
        "imaginária é *só o número* que acompanha o i: [p=0.2] menos quatro, [p=0.2] sem o i."),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] *dois mais três i, vezes um menos i,* [p=0.2] dá *dois menos três i.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque multiplicar real com real [p=0.2] e imaginária com imaginária "
        "parece natural. [p=0.3] {g}Mas é a *distributiva completa,* [p=0.2] e o i ao quadrado *paga o pedágio:* "
        "[p=0.2] dá *cinco mais i.*"),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] para dividir *quatro mais dois i* [p=0.2] por *um mais i,* [p=0.2] divida *parte por "
        "parte.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque na soma é parte com parte. [p=0.3] "
        "{g}Mas na divisão, [p=0.2] *limpe o i do andar de baixo:* [p=0.2] multiplique pelo conjugado, [p=0.2] e dá "
        "*três menos i.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] *raiz de menos quatro, vezes raiz de menos nove,* [p=0.2] dá *menos seis.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque juntar as raízes daria raiz de trinta e seis, [p=0.2] "
        "seis. [p=0.3] {g}Mas escreva com i *antes* de multiplicar: [p=0.2] dois i vezes três i [p=0.2] é seis i ao "
        "quadrado: [p=0.2] *menos seis.*"),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] o módulo de *três mais quatro i* é *sete.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] "
        "{e}Engana porque somar as partes é o mais rápido. [p=0.3] {g}Mas o módulo é a *diagonal do retângulo:* "
        "[p=0.2] Pitágoras. [p=0.2] Raiz de nove mais dezesseis, [p=0.2] *cinco.*"),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] o conjugado de *três mais quatro i* [p=0.2] é *três menos quatro i.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a gente pensa em trocar os dois sinais. [p=0.3] {g}Mas "
        "o *espelho* troca *só a parte imaginária.* [p=0.2] Menos três menos quatro i [p=0.2] é o *oposto,* outra coisa."),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] o argumento de *menos um mais i* [p=0.2] é *quarenta e cinco graus.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque quarenta e cinco é o ângulo da tabela. [p=0.3] {g}Mas os "
        "*sinais escolhem o quadrante:* [p=0.2] real negativa, imaginária positiva, [p=0.2] segundo quadrante: [p=0.2] "
        "*cento e trinta e cinco graus.*"),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] com *delta negativo,* [p=0.2] a equação *não tem raízes.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque era isso que a gente dizia no segundo grau. [p=0.3] {g}Mas falta uma "
        "palavra: [p=0.2] não há raízes *reais.* [p=0.2] Há duas raízes complexas, [p=0.2] *gêmeas espelhadas.*"),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] escreva *i ao quadrado igual a menos um* quando aparecer, "
        "[p=0.2] resolva [p=0.2] e *confira.*"),

    # ================= QUESTÃO 1: POTÊNCIAS DE i =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}O valor de *i elevado a quarenta e cinco [p=0.2] mais i elevado a sessenta e dois* "
        "é: [p=0.4] {la}A, [p=0.2] um mais i. [p=0.2] {lb}B, [p=0.2] menos um mais i. [p=0.2] {lc}C, [p=0.2] menos um "
        "menos i. [p=0.2] {ld}D, [p=0.2] zero. [p=0.2] {le}E, [p=0.2] menos i. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Hábito um: [p=0.2] *resto por quatro.* [p=0.2] O relógio de quatro horas. [p=0.3] {a}Quarenta e cinco "
        "dividido por quatro [p=0.2] deixa resto *um:* [p=0.2] i. [p=0.3] {b}Sessenta e dois [p=0.2] deixa resto "
        "*dois:* [p=0.2] menos um. [p=0.2] Somando, [p=0.2] *menos um mais i.* [p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A "
        "fez i ao quadrado igual a um, [p=0.2] {xc}a C errou o resto do quarenta e cinco, [p=0.2] {xd}a D achou que "
        "potências diferentes se anulam, [p=0.2] {xe}e a E multiplicou em vez de somar."),

    # ================= QUESTÃO 2: DIVISÃO =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}A divisão de *sete mais i* [p=0.2] por *um mais i,* [p=0.2] na forma a mais b "
        "i, é: [p=0.4] {la}A, [p=0.2] oito menos seis i. [p=0.2] {lb}B, [p=0.2] sete mais i. [p=0.2] {lc}C, [p=0.2] "
        "quatro menos três i. [p=0.2] {ld}D, [p=0.2] menos três mais quatro i. [p=0.2] {le}E, [p=0.2] quatro mais três "
        "i. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Hábito dois: [p=0.2] *limpe o i do andar de baixo.* [p=0.2] O conjugado de um mais i [p=0.2] é *um menos "
        "i.* [p=0.3] {a}Em cima: [p=0.2] sete, menos sete i, mais i, menos i ao quadrado: [p=0.2] *oito menos seis i.* "
        "[p=0.2] Embaixo: [p=0.2] um mais um, *dois.* [p=0.2] Dividindo, [p=0.2] *quatro menos três i.* [p=0.3] "
        "{v}Conferindo: [p=0.2] quatro menos três i, [p=0.2] vezes um mais i, [p=0.2] volta a *sete mais i.* [p=0.2] "
        "{ok}*Letra C!* [p=0.4] {xa}A A esqueceu de dividir por dois, [p=0.2] {xb}a B dividiu só pelo um, [p=0.2] "
        "como se o i de baixo não existisse, [p=0.2] {xd}a D trocou as partes, [p=0.2] {xe}e a E errou o sinal."),

    # ================= QUESTÃO 3: DELTA NEGATIVO =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}As raízes de *x ao quadrado menos dois x mais dez, igual a zero,* [p=0.2] nos "
        "complexos, são: [p=0.4] {la}A, [p=0.2] um mais ou menos três i. [p=0.2] {lb}B, [p=0.2] menos um mais ou menos "
        "três i. [p=0.2] {lc}C, [p=0.2] um mais ou menos seis i. [p=0.2] {ld}D, [p=0.2] dois mais ou menos seis i. "
        "[p=0.2] {le}E, [p=0.2] inexistentes. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Delta negativo [p=0.2] não é fim de conversa. [p=0.3] {a}Delta: [p=0.2] quatro menos quarenta, [p=0.2] "
        "*menos trinta e seis.* [p=0.2] A raiz de menos trinta e seis é *seis i.* [p=0.3] {b}x é dois mais ou menos "
        "seis i, [p=0.2] dividido por dois: [p=0.2] *um mais ou menos três i.* [p=0.2] As gêmeas espelhadas. [p=0.3] "
        "{v}Conferindo: [p=0.2] a soma dá *dois,* [p=0.2] e o produto, [p=0.2] um mais nove, [p=0.2] dá *dez.* [p=0.2] "
        "{ok}*Letra A!* [p=0.4] {xb}A B usou b em vez de menos b, [p=0.2] {xc}a C dividiu só a parte real, [p=0.2] "
        "{xd}a D não dividiu por dois a, [p=0.2] {xe}e a E só vale nos reais."),

    # ================= QUESTÃO 4: GIRO NO PLANO =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Um programa gira o ponto *cinco mais dois i* [p=0.2] em noventa graus, [p=0.2] "
        "no sentido *horário,* [p=0.2] em torno da origem. [p=0.2] Ou seja, [p=0.2] multiplica por *menos i.* [p=0.3] "
        "{b}O novo ponto é: [p=0.4] {la}A, [p=0.2] menos dois mais cinco i. [p=0.2] {lb}B, [p=0.2] cinco menos dois "
        "i. [p=0.2] {lc}C, [p=0.2] menos cinco menos dois i. [p=0.2] {ld}D, [p=0.2] dois menos cinco i. [p=0.2] "
        "{le}E, [p=0.2] dois mais cinco i. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Hábito quatro: [p=0.2] *desenhe o ponto.* [p=0.2] Cinco para o lado, [p=0.2] dois para cima. [p=0.3] "
        "{a}Menos i vezes cinco mais dois i: [p=0.2] menos cinco i, [p=0.2] menos dois i ao quadrado, [p=0.2] que vira "
        "*mais dois.* [p=0.2] Fica *dois menos cinco i.* [p=0.3] {b}A manivela ao contrário: [p=0.2] *a, b vira b, "
        "menos a.* [p=0.2] Do primeiro para o quarto quadrante. [p=0.2] {ok}*Letra D!* [p=0.4] {xa}A A é o giro "
        "anti-horário, [p=0.2] {xb}a B é o conjugado, [p=0.2] {xc}a C é o giro de cento e oitenta graus, [p=0.2] {xe}e "
        "a E trocou as partes sem o sinal."),

    # ================= QUESTÃO 5: POTÊNCIA ALTA =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}*Um menos i, elevado à quarta,* [p=0.2] vale: [p=0.4] {la}A, [p=0.2] quatro. "
        "[p=0.2] {lb}B, [p=0.2] menos quatro. [p=0.2] {lc}C, [p=0.2] dezesseis. [p=0.2] {ld}D, [p=0.2] menos quatro i. "
        "[p=0.2] {le}E, [p=0.2] menos oito i. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Hábito três: [p=0.2] uma *potência pequena* que dá um número simples. [p=0.3] {a}Um menos i, ao quadrado: "
        "[p=0.2] um, menos dois i, mais i ao quadrado: [p=0.2] *menos dois i.* [p=0.2] Ao quadrado de novo: [p=0.2] "
        "quatro i ao quadrado, [p=0.2] *menos quatro.* [p=0.3] {v}Pelo radar: [p=0.2] módulo raiz de dois, à quarta, "
        "*quatro;* [p=0.2] e quatro vezes trezentos e quinze graus [p=0.2] dá três voltas e *cento e oitenta.* [p=0.2] "
        "{ok}*Letra B!* [p=0.4] {xa}A A esqueceu que i ao quadrado é menos um, [p=0.2] {xc}a C usou módulo dois, "
        "[p=0.2] {xd}a D errou o ângulo final, [p=0.2] {xe}e a E multiplicou por quatro em vez de elevar ao quadrado."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}O i, a forma a mais b i, [p=0.2] o delta negativo e as potências: [p=0.2] "
        "episódio um. [p=0.3] {c}Operações, conjugado, divisão [p=0.2] e equações com z barra: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Plano, módulo, distância e giros: [p=0.2] episódio três. [p=0.3] {b}Forma trigonométrica e De Moivre: "
        "[p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte questões* [p=0.2] {b}e acerte pelo menos *catorze.* [p=0.4] {c}Com pelo "
        "menos *cinco* de divisão ou potência, [p=0.2] e *três* de interpretação no plano."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Este foi o último assunto do bloco de *Álgebra e Funções.* [p=0.4] {b}O próximo é *Ângulos, retas paralelas "
        "e transversais,* [p=0.2] que abre o bloco de *Geometria Plana.* [p=0.4] {c}E os ângulos que você somou ao "
        "multiplicar complexos [p=0.2] são um bom aquecimento: [p=0.3] lá, somar e comparar ângulos [p=0.2] é o jogo "
        "inteiro."),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de números complexos está completa. "
        "[p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
