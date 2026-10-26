# Roteiro — Sistemas de Equações Lineares, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino
#   (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/22-sistemas-equacoes-lineares.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 DUAS INCÓGNITAS, DUAS PISTAS · uma equação CONTA e a outra SOMA VALORES · TROCAR A PEÇA, com parênteses ·
#       TUDO DE UM TIPO (ícone: o cercado de galinhas e coelhos) ·
#   ep2 JUNTAR AS NOTAS FISCAIS · MULTIPLICAR O PEDIDO INTEIRO (ícone: duas notas fiscais) ·
#   ep3 a ESTRADA de soluções e o CRUZAMENTO · 0 = 2 são TRILHOS que nunca se encontram (ícone: trilhos paralelos) ·
#   ep4 a ESCADA do sistema escalonado · cada um SOBE DUAS VEZES NA BALANÇA (ícone: balança com duplas).
# O que a prova cobra (seção 01): quantidade e valor · cabeças e patas · misturas · combinações de compras · interpretação
#   gráfica. O hábito que mais rende: nomear as incógnitas com unidade e olhar se a pergunta é uma combinação como x + y.
# Onde aparece (seção 10): Física s_A = 20 + 80t e s_B = 200 − 100t → 180t = 180 → t = 1 h, no km 100 · Química: massa de
#   soluto antes = depois · Geometria analítica: o ponto comum de duas retas · Função afim: ponto de equilíbrio (próximas
#   séries). Determinante e Cramer: só citados (série de Determinantes e sistemas lineares).
# Estratégia (seção 09): uma equação por informação · escolher o método pelo formato · conferir na equação que não foi usada
#   por último · responder a pergunta, não a incógnita.
# V/F (os 9 erros da seção 11, com números nossos, sem as Q1–Q9; 6 falsas e 3 verdadeiras — as verdadeiras são as versões
#   CERTAS dos erros 3, 5 e 9): 1 F "Rita tem o dobro de Léo" → 2R = L (é R = 2L; teste Léo 5, Rita 10) · 2 F m = 20 − c em
#   3c + 2m = 50 dá 3c + 40 − c (é 40 − 2c) · 3 V (x + 2y = 7) × 3 = 3x + 6y = 21 · 4 F achou c = 12 carros, a pergunta era
#   motos, marca 12 · 5 V "se Ana der 4 balas a Bia, ficam iguais" → A − 4 = B + 4 · 6 F pediram x + y: é obrigatório achar
#   x e y separados · 7 F deu 0 = 5: errei a conta (é sistema impossível) · 8 F deu 0 = 0: a solução é x = 0 e y = 0 (são
#   infinitas) · 9 V as duplas A + B, B + C e A + C somam 60 → A + B + C = 30.
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta, conferida nas equações originais;
#   cada errada = um erro clássico; as explicações das erradas são NOSSAS):
#   Q1 (cédulas) 30 cédulas de R$ 10 e R$ 50, R$ 700; quantas de R$ 10? d + c = 30 e 10d + 50c = 700 → d = 20, c = 10 → B.
#      A 10 (a outra incógnita) · C 30 (o total de cédulas) · D 40 (tudo de um tipo, mas dividiu os R$ 400 que faltam por
#      10, e não pela diferença 40) · E 70 (700 ÷ 10: como se todas fossem de R$ 10). Atalho: 30 de R$ 10 = 300; faltam 400;
#      cada troca por uma de 50 soma 40 → 10 de R$ 50.
#   Q2 (figurinhas) Ana tem o TRIPLO de Bruno; se Ana der 10 a Bruno, ficam iguais; quantas Ana tem? A = 3B e
#      A − 10 = B + 10 → 2B = 20 → B = 10, A = 30 → D. A 10 (Bruno) · B 15 (A − 10 = B: esqueceu que quem recebe também muda)
#      · C 20 (depois da troca) · E 40 (o total).
#   Q3 (combo do cinema) 3 pipocas + 1 refrigerante = R$ 50; 1 pipoca + 3 refrigerantes = R$ 38; quanto custam juntos 1 + 1?
#      Somando: 4p + 4r = 88 → p + r = 22 → C (pipoca 14, refrigerante 8). A 8 (o refrigerante) · B 14 (a pipoca) ·
#      D 44 (88 ÷ 2: cada item aparece QUATRO vezes na soma) · E 88 (a soma das duas compras).
#   Q4 (retas) r: 3x − y = 4 e s: 6x − 2y = 5 → razões 3/6 = −1/−2 = 1/2 ≠ 4/5; 2r − s: 0 = 3 → paralelas, sem solução → E.
#      A concorrentes, (1, −1) (testou só em r: em s dá 8) · B coincidentes (olhou só o lado esquerdo) · C "0 = 3: erro de
#      conta" · D concorrentes, (0, 0) (0 = algo lido como "solução zero"; nem está em r).
#   Q5 (idades dos irmãos) Ana + Bia = 31, Bia + Caio = 37, Ana + Caio = 28; idade de Ana? soma 96 ÷ 2 = 48 → Ana = 48 − 37
#      = 11 → A (Bia 20, Caio 17). B 14 (dividiu a dupla Ana + Caio por 2) · C 17 (Caio) · D 20 (Bia) · E 59 (96 − 37, sem
#      dividir por 2).
# Gabaritos: B, D, C, E, A.
# Checklist (seção 13) → episódio (como o prompt pede): solução, montagem, tradução, substituição, tudo de um tipo,
#   encontro → ep1 · adição e x + y → ep2 · SPD/SI/SPI, razões, 0 = 2 e 0 = 0 → ep3 · 3 × 3 escalonado e simétrico → ep4.
# Meta (prompt e material): 30 questões, pelo menos 21 acertos (70%), com pelo menos quinze de montagem a partir de texto.
# Ponte (do usuário): Conceito de função: domínio, contradomínio e imagem.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de sistemas lineares: 9 pegadinhas e 5 questões estilo ENEM | Sistemas Lineares Ep. 5"
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
        "{a}Ingressos inteiros e meias, [p=0.2] carros e motos, [p=0.2] café caro e café barato: [p=0.3] {b}o ENEM adora "
        "*duas condições valendo ao mesmo tempo.* [p=0.4] {c}A conta é curta; [p=0.2] o que decide a questão é a "
        "*tradução.* [p=0.4] {d}Hoje: [p=0.2] nove frases de verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E como o sistema aparece na prova? [p=0.4] {a}*Quantidade e valor:* [p=0.2] ingressos de dois preços. "
        "[p=0.3] {b}*Cabeças e patas:* [p=0.2] animais, veículos e rodas. [p=0.3] {c}*Misturas:* [p=0.2] dois cafés, "
        "duas soluções. [p=0.3] {d}*Combinações de compras:* [p=0.2] dois sanduíches e um suco. [p=0.3] {e}E "
        "*interpretação gráfica:* [p=0.2] o ponto onde duas retas se encontram."),
    dict(id="03", block="rende", text=
        "{t}E o hábito que mais rende? [p=0.4] {a}*Nomeie as incógnitas, com unidade.* [p=0.2] Í é o número de ingressos "
        "inteiros. [p=0.3] {b}Escreva *uma equação para cada informação.* [p=0.3] {c}E antes de resolver, [p=0.2] olhe "
        "a pergunta: [p=0.2] às vezes ela já é *xis mais ípsilon.*"),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] *duas incógnitas pedem duas "
        "pistas.* [p=0.2] Uma equação *conta,* [p=0.2] a outra *soma valores.* [p=0.2] Substituir é *trocar a peça,* "
        "com parênteses. [p=0.2] E o atalho: [p=0.2] *tudo de um tipo.* [p=0.4] {b}Dois: [p=0.2] somar equações é "
        "*juntar as notas fiscais.* [p=0.2] E multiplicar é *comprar o mesmo pedido* três vezes."),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] cada equação é uma *estrada de soluções,* [p=0.2] e a resposta é o *cruzamento.* [p=0.2] Zero "
        "igual a dois? [p=0.2] *Trilhos que nunca se encontram.* [p=0.4] {b}Quatro: [p=0.2] o sistema escalonado é uma "
        "*escada.* [p=0.2] E nas duplas, [p=0.2] *cada um sobe duas vezes na balança.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E isso aparece fora da Matemática? [p=0.4] {a}Na *Física,* [p=0.2] no encontro de dois carros. [p=0.2] Um "
        "sai do quilômetro vinte, a oitenta por hora. [p=0.2] O outro sai do duzentos, voltando a cem. [p=0.3] Iguale "
        "as posições: [p=0.2] cento e oitenta tê igual a cento e oitenta. [p=0.2] *Uma hora, no quilômetro cem.*"),
    dict(id="07", block="onde", text=
        "{b}Na *Química,* [p=0.2] nas misturas: [p=0.2] a massa de soluto *antes* [p=0.2] é igual à massa *depois.* "
        "[p=0.2] É a equação dos valores. [p=0.3] {c}Na *Geometria analítica,* [p=0.2] o ponto comum de duas retas. "
        "[p=0.3] {d}E na *Função afim,* [p=0.2] o ponto de equilíbrio entre dois planos. [p=0.2] Essa vem nas próximas "
        "séries. [p=0.2] Já determinante e Cramer [p=0.2] ficam para a série de *Determinantes.*"),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Quatro hábitos. [p=0.4] {a}Um: [p=0.2] *uma equação por informação.* [p=0.2] Só "
        "achou uma? [p=0.2] Releia: [p=0.2] a outra está escondida num \"ao todo\" ou num \"o dobro\". [p=0.3] "
        "{b}Dois: [p=0.2] *escolha o método pelo formato.* [p=0.2] Coeficiente um, [p=0.2] substituição. [p=0.2] "
        "Coeficientes opostos, [p=0.2] adição. [p=0.2] Pediram o total? [p=0.2] Some tudo."),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] *confira na equação que você não usou por último.* [p=0.2] Fechou nas duas? [p=0.2] Está "
        "certo. [p=0.3] {d}Quatro: [p=0.2] *responda a pergunta, não a incógnita.* [p=0.2] A outra incógnita [p=0.2] "
        "está sempre lá, [p=0.2] esperando você."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] \"Rita tem o dobro de Léo\" [p=0.2] vira *dois erre igual a éle.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o dois aparece perto da Rita. [p=0.3] {g}Teste com números: [p=0.2] Léo "
        "tem cinco, [p=0.2] Rita tem dez. [p=0.2] *Erre igual a dois éle.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] trocando eme por vinte menos cê [p=0.2] em três cê mais dois eme, [p=0.2] fica *três cê mais "
        "quarenta menos cê.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o quarenta saiu certo. "
        "[p=0.3] {g}Mas ao *trocar a peça,* [p=0.2] ela entra com parênteses: [p=0.2] o dois multiplica *tudo.* "
        "[p=0.2] *Quarenta menos dois cê.*"),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] multiplicar xis mais dois ípsilon igual a sete por três [p=0.2] dá *três xis mais seis "
        "ípsilon igual a vinte e um.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita "
        "gente esquece o sete. [p=0.3] {g}Mas é *comprar o mesmo pedido três vezes:* [p=0.2] o valor pago também triplica."),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] achei *doze carros.* [p=0.2] A pergunta era o número de motos. [p=0.2] *Marco doze.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque achar a incógnita dá sensação de missão "
        "cumprida. [p=0.3] {g}Mas *responda a pergunta, não a incógnita.* [p=0.2] Falta um passo."),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] \"se Ana der quatro balas a Bia, as duas ficam iguais\" [p=0.2] vira *a menos quatro igual a "
        "bê mais quatro.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente só "
        "tira de quem dá. [p=0.3] {g}Mas *quem recebe também muda:* [p=0.2] menos quatro de um lado, [p=0.2] mais "
        "quatro do outro."),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] pediram *xis mais ípsilon.* [p=0.2] Então é obrigatório achar o xis e o ípsilon separados. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece que a gente sempre resolve tudo. "
        "[p=0.3] {g}Mas às vezes é só *juntar as notas fiscais:* [p=0.2] some as equações, [p=0.2] e a pergunta "
        "aparece pronta."),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] no fim da conta deu *zero igual a cinco.* [p=0.2] Então *eu errei a conta.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque zero igual a cinco parece um absurdo. [p=0.3] {g}E é: [p=0.2] o "
        "absurdo é a resposta. [p=0.2] *Trilhos que nunca se encontram:* [p=0.2] sistema impossível."),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] deu *zero igual a zero.* [p=0.2] Então a solução é *xis igual a zero e ípsilon igual a "
        "zero.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o zero parece a resposta. [p=0.3] "
        "{g}Mas zero igual a zero é *a mesma estrada desenhada duas vezes:* [p=0.2] *infinitas soluções.*"),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] as duplas a mais bê, bê mais cê e a mais cê [p=0.2] somam sessenta. [p=0.2] Então os três "
        "juntos somam *trinta.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a "
        "tentação é dizer sessenta. [p=0.3] {g}Mas *cada um sobe duas vezes na balança:* [p=0.2] divida por dois."),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas, [p=0.2] *cole as etiquetas* das incógnitas [p=0.2] e confira nas duas "
        "equações."),

    # ================= QUESTÃO 1: QUANTIDADE E VALOR (CÉDULAS) =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Um caixa tem *trinta cédulas,* [p=0.2] umas de *dez* e outras de *cinquenta reais,* "
        "[p=0.2] somando *setecentos reais.* [p=0.3] {b}Quantas são as cédulas de *dez reais?* [p=0.4] {la}A, [p=0.2] "
        "dez. [p=0.2] {lb}B, [p=0.2] vinte. [p=0.2] {lc}C, [p=0.2] trinta. [p=0.2] {ld}D, [p=0.2] quarenta. [p=0.2] "
        "{le}E, [p=0.2] setenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Etiquetas: [p=0.2] *dê são as cédulas de dez; cê, as de cinquenta.* [p=0.3] {a}Uma equação conta: [p=0.2] dê "
        "mais cê igual a trinta. [p=0.2] A outra soma valores: [p=0.2] dez dê mais cinquenta cê igual a setecentos. "
        "[p=0.3] {b}Tudo de um tipo: [p=0.2] trinta cédulas de dez [p=0.2] dão trezentos. [p=0.2] Faltam quatrocentos, "
        "[p=0.2] e cada troca por uma de cinquenta soma quarenta. [p=0.2] *Dez de cinquenta.* [p=0.3] {c}Então, *vinte "
        "de dez.* [p=0.2] {ok}*Letra B!* [p=0.3] {v}Confira: [p=0.2] duzentos mais quinhentos, [p=0.2] setecentos. "
        "[p=0.4] {xa}A A é a outra incógnita. [p=0.2] {xc}A C é o total. [p=0.2] {xd}A D dividiu os quatrocentos por "
        "*dez,* [p=0.2] e não por quarenta. [p=0.2] {xe}E a E fez como se todas fossem de dez."),

    # ================= QUESTÃO 2: O TRIPLO E "DER K" (FIGURINHAS) =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Ana tem o *triplo* das figurinhas de Bruno. [p=0.2] Se Ana *der dez* figurinhas a "
        "Bruno, [p=0.2] os dois ficam com a *mesma quantidade.* [p=0.3] {b}Quantas figurinhas Ana tem? [p=0.4] {la}A, "
        "[p=0.2] dez. [p=0.2] {lb}B, [p=0.2] quinze. [p=0.2] {lc}C, [p=0.2] vinte. [p=0.2] {ld}D, [p=0.2] trinta. "
        "[p=0.2] {le}E, [p=0.2] quarenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Etiquetas: [p=0.2] *a é Ana; bê é Bruno.* [p=0.3] {a}O triplo: [p=0.2] *a igual a três bê.* [p=0.2] Teste: "
        "[p=0.2] Bruno dois, Ana seis. [p=0.2] Fecha. [p=0.3] {b}A troca: [p=0.2] Ana perde dez, [p=0.2] Bruno ganha "
        "dez. [p=0.2] *A menos dez igual a bê mais dez.* [p=0.3] {c}Troque a peça: [p=0.2] três bê menos dez igual a bê "
        "mais dez. [p=0.2] Dois bê igual a vinte: [p=0.2] Bruno tem dez, [p=0.2] *Ana tem trinta.* [p=0.2] {ok}*Letra "
        "D!* [p=0.3] {v}Depois da troca: [p=0.2] vinte e vinte. [p=0.4] {xa}A A é Bruno. [p=0.2] {xb}A B esqueceu que "
        "quem recebe também muda. [p=0.2] {xc}A C é depois da troca, [p=0.2] {xe}e a E, o total."),

    # ================= QUESTÃO 3: A PERGUNTA JÁ É A SOMA (CINEMA) =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}No cinema, [p=0.2] *três pipocas e um refrigerante* custam *cinquenta reais.* "
        "[p=0.2] *Uma pipoca e três refrigerantes* custam *trinta e oito.* [p=0.3] {b}Quanto custam, *juntos,* [p=0.2] "
        "uma pipoca e um refrigerante? [p=0.4] {la}A, [p=0.2] oito reais. [p=0.2] {lb}B, [p=0.2] catorze. [p=0.2] "
        "{lc}C, [p=0.2] vinte e dois. [p=0.2] {ld}D, [p=0.2] quarenta e quatro. [p=0.2] {le}E, [p=0.2] oitenta e oito. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Etiquetas: [p=0.2] *pê é a pipoca; erre, o refrigerante,* em reais. [p=0.3] {a}A pergunta é *pê mais "
        "erre.* [p=0.2] Junte as notas fiscais: [p=0.2] quatro pipocas e quatro refrigerantes, [p=0.2] *oitenta e "
        "oito reais.* [p=0.3] {b}Divida por quatro: [p=0.2] *vinte e dois.* [p=0.2] {ok}*Letra C!* [p=0.3] {v}Se "
        "quiser conferir: [p=0.2] pipoca catorze, [p=0.2] refrigerante oito. [p=0.2] Fecha nas duas. [p=0.4] {xa}A A "
        "e {xb}a B são os preços separados. [p=0.2] {xe}A E é a soma das duas compras, [p=0.2] {xd}e a D dividiu por "
        "dois, [p=0.2] mas cada item aparece *quatro* vezes."),

    # ================= QUESTÃO 4: CLASSIFICAÇÃO (RETAS) =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Num aplicativo de geometria, [p=0.2] alguém desenhou as retas *três xis menos "
        "ípsilon igual a quatro* [p=0.2] e *seis xis menos dois ípsilon igual a cinco.* [p=0.3] {b}Sobre as duas retas "
        "e o sistema, [p=0.2] é correto dizer: [p=0.4] {la}A, [p=0.2] concorrentes, no ponto um, menos um. [p=0.2] "
        "{lb}B, [p=0.2] coincidentes, com infinitas soluções. [p=0.2] {lc}C, [p=0.2] a conta dá zero igual a três: "
        "houve erro de cálculo. [p=0.2] {ld}D, [p=0.2] concorrentes, no ponto zero, zero. [p=0.2] {le}E, [p=0.2] "
        "paralelas, sem solução. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Compare os números. [p=0.3] {a}Do lado esquerdo, [p=0.2] a segunda reta é *o dobro* da primeira: [p=0.2] "
        "seis e menos dois. [p=0.3] {b}Mas do lado direito, [p=0.2] o dobro de quatro seria *oito,* [p=0.2] e está "
        "*cinco.* [p=0.3] {c}Dobre a primeira e subtraia: [p=0.2] *zero igual a três.* [p=0.2] Trilhos que nunca se "
        "encontram. [p=0.2] {ok}*Letra E!* [p=0.4] {xa}A A testou o ponto só na primeira reta. [p=0.2] {xb}A B olhou "
        "só o lado esquerdo. [p=0.2] {xc}A C achou que o absurdo era erro, [p=0.2] {xd}e a D leu o zero como "
        "resposta."),

    # ================= QUESTÃO 5: TRÊS INCÓGNITAS SIMÉTRICAS (IDADES) =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Três irmãos: [p=0.2] Ana, Bia e Caio. [p=0.2] Ana e Bia somam *trinta e um "
        "anos.* [p=0.2] Bia e Caio, *trinta e sete.* [p=0.2] Ana e Caio, *vinte e oito.* [p=0.3] {b}Qual é a idade de "
        "*Ana?* [p=0.4] {la}A, [p=0.2] onze anos. [p=0.2] {lb}B, [p=0.2] catorze. [p=0.2] {lc}C, [p=0.2] dezessete. "
        "[p=0.2] {ld}D, [p=0.2] vinte. [p=0.2] {le}E, [p=0.2] cinquenta e nove. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Cada irmão aparece em *duas* duplas. [p=0.3] {a}Some tudo: [p=0.2] noventa e seis. [p=0.2] *Divida por "
        "dois:* [p=0.2] os três juntos têm quarenta e oito. [p=0.3] {b}Ana é o total menos a dupla em que ela não "
        "está: [p=0.2] quarenta e oito menos trinta e sete. [p=0.2] *Onze anos.* [p=0.2] {ok}*Letra A!* [p=0.3] "
        "{v}Bia tem vinte, [p=0.2] Caio dezessete: [p=0.2] onze mais vinte, trinta e um. [p=0.4] {xb}A B dividiu uma "
        "dupla por dois. [p=0.2] {xc}A C é Caio, [p=0.2] {xd}a D é Bia, [p=0.2] {xe}e a E *não dividiu por dois.*"),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra "
        "pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Solução, montagem, tradução, [p=0.2] substituição, tudo de um "
        "tipo [p=0.2] e encontro de móveis: [p=0.2] episódio um. [p=0.3] {c}Adição e xis mais ípsilon: [p=0.2] "
        "episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}As três posições das retas, [p=0.2] as razões, [p=0.2] o zero igual a dois e o zero igual a zero: [p=0.2] "
        "episódio três. [p=0.3] {b}Escada e duplas: [p=0.2] episódio quatro. [p=0.4] {d}O que você *não* marcou, "
        "[p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta "
        "por cento. [p=0.4] {c}E pelo menos *quinze* de montagem a partir de texto: [p=0.2] ingressos, misturas e "
        "combos."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Conceito de função: domínio, contradomínio e imagem,* [p=0.3] {b}que abre o bloco de "
        "Funções [p=0.2] e transforma as retas deste assunto em funções: [p=0.3] {c}*uma coisa que determina a "
        "outra.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de sistemas lineares está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
