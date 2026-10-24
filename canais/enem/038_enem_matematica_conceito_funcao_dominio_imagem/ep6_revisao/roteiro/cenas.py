# Roteiro — Conceito de Função, Domínio e Imagem, Episódio 6 de 6: Revisão geral, estratégia de prova, pegadinhas e treino
#   (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/23-conceito-funcao-dominio-imagem.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 a MÁQUINA (mesma entrada, mesma saída) · a DATA DE NASCIMENTO (duas flechas chegando pode, duas saindo não)
#       (ícone: a máquina) ·
#   ep2 o CARDÁPIO × o que SAI DA COZINHA (contradomínio × imagem) · a CADEIRA VAZIA do x (ícone: o cardápio) ·
#   ep3 o caminho de IDA e o de VOLTA · as GAVETAS da função por partes (ícone: a máquina ao contrário) ·
#   ep4 a RÉGUA EM PÉ · a SOMBRA no CHÃO (domínio) e na PAREDE (imagem) (ícone: a régua em pé) ·
#   ep5 o PORTEIRO do domínio (só entra o x com o qual a conta existe E que faz sentido) (ícone: o porteiro).
#   O ep. 5 ainda não estava pronto quando esta revisão foi escrita: a analogia dele vem do prompt do vídeo 5.
# O que a prova cobra (seção 01): calcular valores · caminho de volta · ler gráficos · decidir o domínio · reconhecer
#   funções. O que mais rende: entrada (x, eixo horizontal, domínio) × saída (y, eixo vertical, imagem).
# Onde aparece (seção 10): Física (v × t não mostra onde o móvel está) · Química (curva de solubilidade: cada temperatura,
#   uma solubilidade) · Biologia (o máximo é o "ótimo") · Geografia (climogramas e séries históricas: o domínio é o
#   período mostrado; não extrapole).
# Estratégia (seção 09): eixos e unidades antes de tudo · dão o x ou o y? · por partes: localize a faixa · domínio: teste
#   os extremos das alternativas.
# V/F (os 9 erros da seção 11, com números nossos, sem as Q1–Q9; 6 falsas e 3 verdadeiras — as verdadeiras são as versões
#   CERTAS dos erros 3, 7 e 9): 1 F aniversário igual → "aluno → data" não é função · 2 F elemento sem flecha pode ser
#   função · 3 V f(x) = x + 1, A = {1, 2, 3}, B = {0, …, 5}: Im = {2, 3, 4} ⊂ B · 4 F f(x) = x² + 3 → f(3x) = 3x² + 9 (é
#   9x² + 3; com x = 2: 39 × 21 — com x = 1 as duas dão 12, por isso o teste usa 2) · 5 F f(x) = x²: f(2 + 3) = f(2) + f(3)
#   (25 × 13) · 6 F C(n) = 10 + 4n, pagou R$ 50 → calcular C(50) (é 10 + 4n = 50 → n = 10) · 7 V a imagem se lê no eixo
#   vertical · 8 F começa em y = 2 e termina em y = 5 → imagem [2, 5] · 9 V a fórmula aceita −2, mas um comprimento não.
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico; as
#   explicações das erradas são NOSSAS):
#   Q1 (tabela) dia → nº de clientes: seg 40, ter 52, qua 52, qui 61, sex 40 → é função, Im = {40, 52, 61} → B.
#      A "não é: o 52 aparece em dois dias" (duas flechas CHEGANDO) · C Im = {seg, …, sex} (o domínio) · D "não é: sobe e
#      desce" (comportamento não decide) · E "todo o intervalo de 40 a 61" (o 45 nunca sai).
#   Q2 (gráfico, termômetro) temperatura × hora: (0, 16) → (6, 12) → (14, 30) → (24, 18), eixo y desenhado de 0 a 40 °C.
#      Máxima e imagem: 30 °C e [12, 30] → E. A 18 °C e [16, 18] (as pontas) · B 30 °C e [0, 24] (o domínio) · C 14 °C e
#      [12, 30] (respondeu QUANDO, no chão, em vez de QUANTO) · D 30 °C e [0, 40] (a escala do eixo: o cardápio).
#   Q3 (patinete) P(m) = 3 + 0,5m, pagou R$ 12 → 0,5m = 9 → m = 18 min → C. A 4 (12 ÷ 3, dividiu pela tarifa fixa) ·
#      B 9 (calculou P(12): f(k) no lugar de x) · D 24 (12 ÷ 0,5, esqueceu o fixo) · E 30 (somou o fixo: 15 ÷ 0,5).
#   Q4 (bicicleta) R$ 5 pela 1ª meia hora + R$ 2 por meia hora adicional OU FRAÇÃO; uso de 1 h 40 min = 100 min: depois da
#      1ª meia hora sobram 70 min = 2 meias horas + 10 min de fração → 3 adicionais → 5 + 6 = R$ 11 → D. A R$ 8 (todas as 4
#      meias horas a R$ 2, sem a gaveta da primeira) · B R$ 9 (ignorou a fração) · C R$ 9,67 (cobrou proporcional: 5 + 2 ·
#      70/30) · E R$ 13 (contou a 1ª meia hora também como adicional: 5 + 4 · 2).
#   Q5 (cercado) 60 m de tela e um muro como um dos lados: lados x, x e 60 − 2x; A(x) = x(60 − 2x) → 0 < x < 30 → A.
#      B x > 0 (esqueceu o outro lado) · C 0 < x < 60 (descontou o x uma vez só; com x = 45, área negativa) · D 0 ≤ x ≤ 30
#      (aceitou lado zero: cercado sem área) · E x < 30 (esqueceu que medida é positiva).
# Gabaritos: B, E, C, D, A.
# Checklist (seção 13) → episódio (como o prompt pede): definição e flechas → ep1 · domínio, imagem e f(x) → ep2 ·
#   f(x) = k e por partes → ep3 · gráfico → ep4 · domínio por fórmula e contexto → ep5.
# Meta (prompt e material): 30 questões, pelo menos 21 acertos (70%), com pelo menos dez de leitura de gráficos de outras
#   áreas (Física, Química, Geografia).
# Ponte (do usuário): Função afim: gráfico, coeficientes e aplicações; o táxi P(d) = 5 + 2,5d.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de função: 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, Funções episódio 6"

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
        "{a}Função é a habilidade de Matemática que mais aparece *fora da Matemática:* [p=0.3] {b}todo gráfico de "
        "Física, Química, Biologia e Geografia [p=0.2] *é uma função.* [p=0.4] {c}Quem domina este assunto [p=0.2] "
        "*ganha pontos em quatro provas.* [p=0.4] {d}Hoje: [p=0.2] nove frases de verdadeiro ou falso [p=0.2] e cinco "
        "questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Calcular valores:* [p=0.2] o preço da corrida. "
        "[p=0.3] {b}*O caminho de volta:* [p=0.2] que distância custou trinta reais. [p=0.3] {c}*Ler gráficos:* [p=0.2] máximo, sobe e desce. [p=0.3] {d}*Decidir o domínio:* [p=0.2] que valores fazem "
        "sentido. [p=0.3] {e}E *reconhecer funções* [p=0.2] em tabelas e curvas."),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.4] {a}Separar *entrada* e *saída.* [p=0.3] {b}A entrada é o *xis,* [p=0.2] no "
        "eixo *horizontal:* [p=0.2] forma o *domínio.* [p=0.3] {c}A saída é o *ípsilon,* [p=0.2] no eixo *vertical:* "
        "[p=0.2] forma a *imagem.* [p=0.4] {d}Metade dos erros [p=0.2] é *trocar uma pela outra.*"),

    # ================= ÍNDICE DA REVISÃO: OS 5 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] a *máquina.* [p=0.2] A mesma "
        "entrada dá *sempre a mesma saída.* [p=0.2] E a *data de nascimento:* [p=0.2] duas flechas *chegando* pode; "
        "[p=0.2] duas *saindo,* não. [p=0.4] {b}Dois: [p=0.2] o contradomínio é o *cardápio;* [p=0.2] a imagem é o que "
        "*sai da cozinha.* [p=0.2] E o xis é uma *cadeira vazia.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] o caminho de *ida* e o de *volta,* [p=0.2] e as *gavetas* das partes. [p=0.4] "
        "{b}Quatro: [p=0.2] a *régua em pé,* [p=0.2] e as *sombras:* [p=0.2] domínio no *chão,* [p=0.2] imagem na *parede.* [p=0.4] {c}Cinco: [p=0.2] o *porteiro do domínio:* [p=0.2] só entra o xis com o qual a conta existe "
        "*e* que faz sentido no problema."),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}Na *Física,* [p=0.2] leia o eixo vertical: [p=0.2] um gráfico de "
        "*velocidade* por tempo [p=0.2] não mostra *onde* o carro está. [p=0.3] {b}Na *Química,* [p=0.2] a curva de "
        "solubilidade: [p=0.2] cada temperatura tem *uma única* solubilidade. [p=0.2] É função."),
    dict(id="07", block="onde", text=
        "{c}Na *Biologia,* [p=0.2] o ponto mais alto [p=0.2] é o *ótimo.* [p=0.3] {d}E na *Geografia,* [p=0.2] climogramas e séries históricas: [p=0.2] o domínio é o "
        "*período mostrado.* [p=0.2] *Não extrapole* para fora dele."),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Quatro hábitos. [p=0.4] {a}Um: [p=0.2] *leia os eixos antes de tudo,* [p=0.2] "
        "com as unidades. [p=0.3] {b}Dois: [p=0.2] pergunte: [p=0.2] *dão o xis ou o ípsilon?* [p=0.2] Deram a saída? [p=0.2] Caminho de volta."),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] na função por partes, [p=0.2] *descubra a gaveta* antes de fazer a conta. [p=0.3] {d}Quatro: "
        "[p=0.2] no domínio, [p=0.2] *teste os extremos* das alternativas. [p=0.2] O porteiro barra o que não serve."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] dois alunos fazem aniversário no mesmo dia. [p=0.2] Então \"aluno, data de nascimento\" [p=0.2] "
        "*não é função.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque duas flechas chegam na mesma "
        "data. [p=0.3] {g}Mas *chegar junto pode.* [p=0.2] Proibido é *um* aluno com *duas* datas."),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] no diagrama, [p=0.2] um elemento do conjunto de partida *ficou sem flecha.* [p=0.2] Ainda "
        "assim, pode ser função. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque os outros estão certinhos. [p=0.3] {g}Mas na máquina, *toda entrada tem saída.* [p=0.2] Sobrou um sem flecha? [p=0.2] Não é "
        "função."),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] com éfe de xis igual a xis mais um, [p=0.2] domínio um, dois e três, [p=0.2] e contradomínio "
        "de zero a cinco, [p=0.2] a imagem é *dois, três e quatro.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] "
        "{e}Parece falso porque a tentação é responder o zero a cinco. [p=0.3] {g}Mas o contradomínio é o "
        "*cardápio.* [p=0.2] A imagem é *o que sai da cozinha.*"),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] se éfe de xis é xis ao quadrado mais três, [p=0.2] então éfe de três xis [p=0.2] é *três "
        "xis ao quadrado mais nove.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o três parece multiplicar tudo. [p=0.3] {g}Mas o três xis *senta na cadeira vazia,* [p=0.2] com parênteses: [p=0.2] *nove xis "
        "ao quadrado mais três.* "),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] se éfe de xis é xis ao quadrado, [p=0.2] então éfe de dois mais três [p=0.2] é *éfe de dois "
        "mais éfe de três.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o éfe parece um número. [p=0.3] {g}Mas éfe é o *nome da máquina.* [p=0.2] Cinco ao quadrado, [p=0.2] "
        "*vinte e cinco,* [p=0.2] e não quatro mais nove."),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] o preço é cê de ene igual a dez mais quatro ene. [p=0.2] Alguém *pagou cinquenta reais.* "
        "[p=0.2] Então eu calculo *cê de cinquenta.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o cinquenta salta aos olhos. [p=0.3] {g}Mas deram a *saída:* [p=0.2] é o *caminho de volta.* "
        "[p=0.2] Dez mais quatro ene igual a cinquenta: [p=0.2] *ene igual a dez.*"),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] num gráfico, [p=0.2] a imagem se lê no *eixo vertical.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a gente lê da esquerda para a direita. [p=0.3] {g}Mas a "
        "imagem é a *sombra na parede.* [p=0.2] O chão é do domínio."),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] o gráfico *começa* em ípsilon igual a dois [p=0.2] e *termina* em ípsilon igual a cinco. "
        "[p=0.2] Então a imagem é *de dois a cinco.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o olho vê as pontas primeiro. [p=0.3] {g}Mas o *máximo pode estar no meio.* [p=0.2] A imagem vai do "
        "ponto *mais baixo* ao *mais alto.*"),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] a fórmula aceita xis igual a menos dois, [p=0.2] mas se o xis é *um comprimento,* [p=0.2] "
        "menos dois *não entra.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a conta dá "
        "certo. [p=0.3] {g}Mas o *porteiro* escuta a fórmula *e* o problema: [p=0.2] medida é positiva, [p=0.2] "
        "contagem é inteira."),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas, [p=0.2] escreva na margem: [p=0.2] *dão o xis ou o ípsilon?*"),

    # ================= QUESTÃO 1: RECONHECER FUNÇÃO NUMA TABELA =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma lanchonete anotou os clientes de cada dia: [p=0.2] "
        "segunda, *quarenta;* [p=0.2] terça, *cinquenta e dois;* [p=0.2] quarta, *cinquenta e dois;* [p=0.2] quinta, "
        "*sessenta e um;* [p=0.2] sexta, *quarenta.* [p=0.3] {b}Sobre a relação *dia, número de clientes,* [p=0.2] é "
        "correto afirmar: [p=0.4] {la}A, [p=0.2] não é função, porque o cinquenta e dois aparece em dois dias. [p=0.2] "
        "{lb}B, [p=0.2] é função; imagem: quarenta, cinquenta e dois, sessenta e um. [p=0.2] {lc}C, [p=0.2] é função; imagem: de segunda a sexta. [p=0.2] {ld}D, [p=0.2] não é função, porque o número sobe e depois "
        "desce. [p=0.2] {le}E, [p=0.2] é função; imagem: todos os números de quarenta a sessenta e um. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Sabendo o *dia,* [p=0.2] eu sei o *número* sem dúvida? [p=0.2] Sei: [p=0.2] cada dia, *uma* saída. [p=0.3] {a}É função. [p=0.2] E a imagem é o que *realmente sai.* [p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A confundiu flechas *chegando* com flechas "
        "saindo. [p=0.2] {xd}A D julgou pelo sobe e desce, [p=0.2] que não decide nada. [p=0.2] {xc}A C deu o "
        "*domínio.* [p=0.2] {xe}E a E pôs na imagem números que *nunca saíram,* [p=0.2] como quarenta e cinco."),

    # ================= QUESTÃO 2: MÁXIMO E IMAGEM NUM GRÁFICO DE OUTRA ÁREA =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}O gráfico mostra a temperatura de uma cidade ao longo de um dia. [p=0.2] O eixo vertical vai de zero a quarenta graus. [p=0.3] {b}A temperatura "
        "*máxima* [p=0.2] e o conjunto de *todas* as temperaturas registradas são: [p=0.4] {la}A, [p=0.2] dezoito "
        "graus; [p=0.2] de dezesseis a dezoito. [p=0.2] {lb}B, [p=0.2] trinta graus; [p=0.2] de zero a vinte e quatro. "
        "[p=0.2] {lc}C, [p=0.2] catorze graus; [p=0.2] de doze a trinta. [p=0.2] {ld}D, [p=0.2] trinta graus; [p=0.2] "
        "de zero a quarenta. [p=0.2] {le}E, [p=0.2] trinta graus; [p=0.2] de doze a trinta. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Eixos primeiro: [p=0.2] hora no chão, [p=0.2] temperatura na parede. [p=0.3] {a}O ponto mais alto está *no meio,* [p=0.2] às catorze horas: [p=0.2] "
        "*trinta graus.* [p=0.2] O mais baixo, às seis: [p=0.2] *doze.* [p=0.3] {b}A sombra na parede vai de doze a "
        "trinta. [p=0.2] {ok}*Letra E!* [p=0.4] {xa}A A ficou nas *pontas.* [p=0.2] {xb}A B deu o *domínio.* [p=0.2] "
        "{xc}A C respondeu *quando,* [p=0.2] no chão. [p=0.2] {xd}E a D leu a escala do eixo: [p=0.2] o *cardápio,* "
        "[p=0.2] não o que saiu."),

    # ================= QUESTÃO 3: O CAMINHO DE VOLTA (PATINETE) =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Um patinete cobra *três reais* para desbloquear [p=0.2] e *cinquenta "
        "centavos por minuto:* [p=0.2] pê de eme igual a três mais zero vírgula cinco eme. [p=0.3] {b}Uma pessoa "
        "*pagou doze reais.* [p=0.2] Quantos minutos ela andou? [p=0.4] {la}A, [p=0.2] quatro. [p=0.2] {lb}B, [p=0.2] "
        "nove. [p=0.2] {lc}C, [p=0.2] dezoito. [p=0.2] {ld}D, [p=0.2] vinte e quatro. [p=0.2] {le}E, [p=0.2] trinta. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Dão o xis ou o ípsilon? [p=0.2] Doze reais é o *preço:* [p=0.2] é a saída. [p=0.2] *Caminho de volta.* "
        "[p=0.3] {a}Três mais zero vírgula cinco eme igual a doze. [p=0.2] Tire os três: [p=0.2] zero vírgula cinco eme "
        "igual a nove. [p=0.3] {b}Divida por meio: [p=0.2] *dezoito minutos.* [p=0.2] {ok}*Letra C!* [p=0.2] {v}Confira: [p=0.2] três mais nove, doze. [p=0.4] {xb}A B calculou *pê de doze:* [p=0.2] fez a ida, "
        "[p=0.2] não a volta. [p=0.2] {xd}A D esqueceu os três reais. [p=0.2] {xe}A E *somou* os três. [p=0.2] {xa}E "
        "a A dividiu pela tarifa fixa."),

    # ================= QUESTÃO 4: FUNÇÃO POR PARTES ("OU FRAÇÃO") =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Uma bicicleta compartilhada cobra *cinco reais* pela primeira meia hora [p=0.2] "
        "e *dois reais* por meia hora adicional *ou fração.* [p=0.3] {b}Uma pessoa usou a bicicleta por *uma hora e "
        "quarenta minutos.* [p=0.2] Quanto pagou? [p=0.4] {la}A, [p=0.2] oito reais. [p=0.2] {lb}B, [p=0.2] nove. "
        "[p=0.2] {lc}C, [p=0.2] nove e sessenta e sete. [p=0.2] {ld}D, [p=0.2] onze. [p=0.2] {le}E, [p=0.2] treze. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Descubra a gaveta. [p=0.2] Uma hora e quarenta são *cem minutos.* [p=0.3] {a}A primeira meia hora: [p=0.2] "
        "*cinco reais.* [p=0.2] Sobram setenta minutos: [p=0.2] duas meias horas *e dez minutos.* [p=0.3] {b}Começou a "
        "meia hora, [p=0.2] pagou a meia hora inteira: [p=0.2] *três adicionais.* [p=0.2] Cinco mais seis, [p=0.2] "
        "*onze reais.* [p=0.2] {ok}*Letra D!* [p=0.4] {xb}A B ignorou a fração. [p=0.2] {xc}A C cobrou proporcional, "
        "[p=0.2] o que o \"ou fração\" proíbe. [p=0.2] {xe}A E cobrou a primeira também como adicional, [p=0.2] {xa}e a "
        "A esqueceu a gaveta da primeira meia hora."),

    # ================= QUESTÃO 5: DOMÍNIO PELO CONTEXTO (CERCADO) =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Com *sessenta metros* de tela [p=0.2] e um *muro* como um dos lados, [p=0.2] alguém vai cercar uma horta retangular. [p=0.2] Os dois lados que saem do muro medem *xis;* "
        "[p=0.2] o lado da frente mede *sessenta menos dois xis.* [p=0.3] {b}Para que o cercado exista, [p=0.2] o "
        "domínio de xis é: [p=0.4] {la}A, [p=0.2] xis entre zero e trinta. [p=0.2] {lb}B, [p=0.2] xis maior que zero. "
        "[p=0.2] {lc}C, [p=0.2] xis entre zero e sessenta. [p=0.2] {ld}D, [p=0.2] de zero a trinta, com os extremos. "
        "[p=0.2] {le}E, [p=0.2] xis menor que trinta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Chame o porteiro. [p=0.2] *Todo lado precisa ser positivo.* [p=0.3] {a}Xis maior que zero. [p=0.2] E "
        "sessenta menos dois xis maior que zero: [p=0.2] xis *menor que trinta.* [p=0.3] {b}As duas ao mesmo tempo: "
        "[p=0.2] *entre zero e trinta, sem os extremos.* [p=0.2] {ok}*Letra A!* [p=0.4] {xb}A B esqueceu o lado da "
        "frente. [p=0.2] {xe}A E esqueceu o zero. [p=0.2] {xc}A C descontou o xis *uma vez só:* [p=0.2] com quarenta e "
        "cinco, a área dá negativa. [p=0.2] {xd}E a D deixou entrar lado zero: [p=0.2] um cercado *sem área.*"),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra "
        "pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Definição, variáveis e flechas: [p=0.2] episódio um. [p=0.3] "
        "{c}Domínio, contradomínio, imagem e éfe de xis: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Caminho de volta e funções por partes: [p=0.2] episódio três. [p=0.3] {b}Régua em pé e leitura de "
        "gráficos: [p=0.2] episódio quatro. [p=0.3] {c}Domínio pela fórmula e pelo contexto: [p=0.2] episódio cinco. "
        "[p=0.4] {d}O que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta "
        "por cento. [p=0.4] {c}E pelo menos *dez* de leitura de gráficos de outras áreas: [p=0.2] Física, Química e "
        "Geografia."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Função afim: gráfico, coeficientes e aplicações,* [p=0.3] {b}a primeira família de "
        "funções do bloco. [p=0.4] {c}Aquele táxi, [p=0.2] pê de dê igual a cinco mais dois vírgula cinco dê, [p=0.3] "
        "{d}vai ganhar *nome e sobrenome.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de conceito de função está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
