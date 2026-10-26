# Roteiro — Porcentagem, Episódio 5 de 6: Ponto percentual × por cento, e porcentagem em gráficos
# Base: Estudos/Enem/estudos/01-matematica/09-porcentagem.html — seções 08 e 09 (+ Questões 7 e 8 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   PONTO PERCENTUAL = GRAU no termômetro: subiu 2 graus é a diferença; "por cento" diz quanto isso é perto do que era antes.
#   O gráfico de setores é uma PIZZA de 360°: a pizza inteira é 100%, então cada 1% é uma fatia de 3,6°.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Exemplos: o gancho (juros de 2% para 4%) é do usuário e fica. Os blocos a)–c) usam OUTRO par de taxas (inflação de 5% para
#   6%: 1 p.p. = 20%), para não entregar a Questão 7 (8% → 10%). No bloco e), as referências 90°, 180° e 36° ficam; os 54°
#   ficam só para a Questão 8. Exemplo nosso do caminho de volta: 72° ÷ 3,6 = 20%. Grupos (bloco f): 20 homens e 80 mulheres,
#   30% de cada → 6 + 24 = 30 de 100 = 30% do grupo (não 60%), e os grupos nem têm o mesmo número de praticantes.
# Só gráfico de setores (outros gráficos têm série própria).
# QUESTÃO 7 do material (texto idêntico na tela): 10 − 8 = 2 p.p.; (10 − 8)/8 = 25% → B.
#   Material: A ("aumentou 2%" seria 8% → 8,16%) e C (20% = usou o valor final como base). Explicações NOSSAS:
#   D (10 p.p.) = leu a taxa nova como se fosse a diferença; E (dobrou) = dobrar seria ir de 8% para 16%.
# QUESTÃO 8 do material: 54 ÷ 360 = 0,15 = 15%, ou 54 ÷ 3,6 = 15 → C. Conferência: 15 × 3,6 = 54.
#   Atalho: 54° = 36° + 18° → 10% + 5% = 15%. O material não explica as erradas. Explicações NOSSAS: E (54%) = leu o grau
#   como porcentagem; A (5,4%) = dividiu por 10, como se 1% fossem 10°; D (18%) = dividiu por 3 em vez de 3,6;
#   B (10%) = é a referência de 36°, não de 54°.
# Nós fazemos (prompt): aprovação de 40% para 30% → caiu 10 p.p.; 10 ÷ 40 = 25%.
# Atalhos (verde): "p.p.: só subtraia · %: subtraia e divida pelo de ANTES" · "90° = 25%, 180° = 50%, 36° = 10%" ·
#   "de graus para %: divida por 3,6" · "pergunte sempre: por cento DE QUEM?".
# Frases-chave (meio e fim, idênticas): 1. Ponto percentual: a diferença. Por cento: em relação ao que era.
#   2. Na pizza, 1% vale 3,6°. 3. Só se somam porcentagens do mesmo todo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Ponto percentual × por cento e gráfico de setores | Porcentagem Ep. 5"
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
        "{a}Os juros foram de *dois por cento* para *quatro por cento.* [p=0.4] {b}Subiram dois por cento? [p=0.4] "
        "{c}Subiram *dois pontos percentuais,* [p=0.3] {d}e o custo do dinheiro *dobrou.* [p=0.5] {e}Chamar isso de "
        "aumento de dois por cento [p=0.2] *esconde a notícia.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai distinguir *ponto percentual* de *por cento* [p=0.3] {b}e ler qualquer "
        "*gráfico de setores.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido do episódio um. [p=0.3] {a}Um preço vai de *quarenta* para *cinquenta.* [p=0.3] "
        "Subiu dez. [p=0.4] {b}Em porcentagem, [p=0.2] você divide pelo valor *de onde partiu:* [p=0.2] dez dividido por "
        "quarenta, [p=0.2] *vinte e cinco por cento.* [p=0.4] {c}O denominador é sempre *o que era antes.*"),

    # ================= BLOCO A: PONTO PERCENTUAL =================
    dict(id="04", block="manchete", text=
        "{t}Agora, uma manchete. [p=0.3] {a}A inflação do mês foi de *cinco por cento* [p=0.2] para *seis por cento.* "
        "[p=0.4] {b}Aqui, cinco e seis por cento são *taxas:* [p=0.2] uma taxa é uma porcentagem que mede alguma coisa, "
        "[p=0.2] quantos em cada cem. [p=0.4] {c}A pergunta é: [p=0.2] a inflação *subiu quanto?* [p=0.4] {d}Existem duas "
        "respostas certas. [p=0.3] E uma errada, [p=0.2] que aparece todo dia no jornal."),
    dict(id="05", block="pp", text=
        "{t}A primeira resposta: [p=0.2] *subtrair.* [p=0.3] {a}Seis menos cinco: [p=0.2] *um.* [p=0.4] {b}Esse um tem "
        "nome: [p=0.2] *ponto percentual,* [p=0.2] que se escreve p ponto p ponto. [p=0.4] {c}Ponto percentual é a "
        "*diferença* entre duas taxas. [p=0.3] Só isso: [p=0.2] uma subtração."),
    dict(id="06", block="pp", text=
        "{t}Pense num *termômetro.* [p=0.3] {a}A temperatura foi de vinte para vinte e dois graus. [p=0.4] {b}Ninguém diz "
        "que subiu dois por cento. [p=0.3] Diz que subiu *dois graus.* [p=0.4] {c}O ponto percentual [p=0.2] é o *grau* "
        "das taxas: [p=0.2] mede quanto a taxa andou, [p=0.2] na própria régua dela."),

    # ================= BLOCO B: POR CENTO =================
    dict(id="07", block="relativa", text=
        "{t}A segunda resposta: [p=0.2] *por cento.* [p=0.3] {a}Agora a pergunta é outra: [p=0.2] esse um ponto [p=0.2] "
        "é *muito ou pouco* perto do que era antes? [p=0.4] {b}Faça como no lembrete: [p=0.2] a diferença, [p=0.2] "
        "dividida pelo valor *de onde partiu.* [p=0.3] Um dividido por cinco: [p=0.2] *vinte por cento.* [p=0.4] {c}Isso "
        "é a *variação relativa:* [p=0.2] o tamanho da mudança *em relação* ao que era."),
    dict(id="08", block="relativa", text=
        "{t}Guarde o atalho. [p=0.3] {a}Ponto percentual: [p=0.2] *só subtraia.* [p=0.4] {b}Por cento: [p=0.2] "
        "*subtraia e divida pelo de antes.*"),

    # ================= BLOCO C: AS DUAS ESTÃO CERTAS =================
    dict(id="09", block="certas", text=
        "{t}Então, quem está certo? [p=0.3] {a}A inflação subiu *um ponto percentual.* [p=0.3] Certo. [p=0.4] {b}A "
        "inflação subiu *vinte por cento.* [p=0.3] Também certo. [p=0.4] {c}As duas frases descrevem *a mesma mudança.* "
        "[p=0.4] {d}O errado é dizer [p=0.2] que subiu *um por cento.* [p=0.3] Um por cento de cinco [p=0.2] é zero "
        "vírgula zero cinco. [p=0.3] {e}Essa frase levaria a inflação para cinco vírgula zero cinco, [p=0.2] *não para "
        "seis.*"),

    # ================= BLOCO D: OS JUROS QUE DOBRARAM =================
    dict(id="10", block="juros", text=
        "{t}Agora, o caso do começo da aula. [p=0.3] {a}Juros de *dois* para *quatro por cento.* [p=0.4] {b}Em pontos "
        "percentuais: [p=0.2] quatro menos dois, [p=0.2] *dois pontos.* [p=0.4] {c}Em por cento: [p=0.2] dois dividido "
        "por dois, [p=0.2] *cem por cento.* [p=0.3] A taxa *dobrou.* [p=0.4] {d}Quem fala só em dois por cento [p=0.2] "
        "faz parecer pequeno [p=0.2] o que, na verdade, *dobrou.*"),

    # ================= BLOCO E: A PIZZA DE 360° =================
    dict(id="11", block="pizza", text=
        "{t}Mudando de assunto: [p=0.2] um *gráfico de pizza.* [p=0.3] {a}O nome técnico é *gráfico de setores:* [p=0.2] "
        "um círculo cortado em fatias, [p=0.2] e cada fatia é um setor. [p=0.4] {b}Veja os gastos de uma família: [p=0.2] "
        "moradia, [p=0.2] comida, [p=0.2] transporte, [p=0.2] lazer. [p=0.4] {c}A pizza inteira é o gasto total: [p=0.2] "
        "*cem por cento.*"),
    dict(id="12", block="pizza", text=
        "{t}E quanto vale um por cento na pizza? [p=0.3] {a}Uma volta completa no círculo [p=0.2] tem *trezentos e "
        "sessenta graus.* [p=0.4] {b}Cem por cento é a volta toda. [p=0.3] Então, um por cento [p=0.2] é trezentos e "
        "sessenta dividido por cem: [p=0.2] *três vírgula seis graus.* [p=0.4] {c}O ângulo de cada fatia, [p=0.2] medido "
        "lá no centro da pizza, [p=0.2] se chama *ângulo central.* [p=0.4] {d}E a regra é: [p=0.2] *ângulo igual à "
        "porcentagem vezes três vírgula seis.*"),
    dict(id="13", block="pizza", text=
        "{t}Três fatias que vale ter na cabeça. [p=0.3] {a}*Noventa graus,* [p=0.2] um canto reto: [p=0.2] um quarto da "
        "pizza, [p=0.2] *vinte e cinco por cento.* [p=0.4] {b}*Cento e oitenta graus,* [p=0.2] meia pizza: [p=0.2] "
        "*cinquenta por cento.* [p=0.4] {c}E *trinta e seis graus:* [p=0.2] *dez por cento.*"),
    dict(id="14", block="pizza", text=
        "{t}E o caminho de volta? [p=0.3] {a}Uma fatia de *setenta e dois graus.* [p=0.3] Quanto por cento? [p=0.4] "
        "{b}Se multiplicar por três vírgula seis leva de porcentagem para grau, [p=0.2] *dividir* leva de volta. [p=0.3] "
        "Setenta e dois dividido por três vírgula seis: [p=0.2] *vinte por cento.* [p=0.4] {c}Ou pelo atalho: [p=0.2] "
        "setenta e dois é duas vezes trinta e seis. [p=0.2] Duas vezes dez por cento: [p=0.2] *vinte.*"),

    # ================= BLOCO F: BASES DIFERENTES =================
    dict(id="15", block="grupos", text=
        "{t}Última armadilha. [p=0.3] {a}Num grupo, [p=0.2] *trinta por cento* dos homens praticam esporte. [p=0.3] {b}E "
        "*trinta por cento* das mulheres também. [p=0.4] {c}Então sessenta por cento do grupo pratica esporte? [p=0.4] "
        "{d}Vamos contar. [p=0.2] São *vinte* homens e *oitenta* mulheres. [p=0.3] Trinta por cento de vinte: [p=0.2] "
        "*seis.* [p=0.3] Trinta por cento de oitenta: [p=0.2] *vinte e quatro.* [p=0.4] {e}Seis mais vinte e quatro: "
        "[p=0.2] trinta pessoas, [p=0.2] de cem. [p=0.3] *Trinta por cento,* [p=0.2] e não sessenta."),
    dict(id="16", block="grupos", text=
        "{t}O que aconteceu? [p=0.3] {a}Cada trinta por cento é de um *todo diferente:* [p=0.2] um é dos homens, [p=0.2] "
        "o outro, das mulheres. [p=0.4] {b}E repare: [p=0.2] os dois são trinta por cento, [p=0.2] mas um grupo tem *seis* "
        "praticantes [p=0.2] e o outro, *vinte e quatro.* [p=0.4] {c}Atalho: [p=0.2] diante de uma porcentagem, [p=0.2] "
        "pergunte sempre: [p=0.2] *por cento de quem?*"),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}A aprovação de um governo foi de *quarenta* para *trinta por cento.* [p=0.4] {b}Quantos "
        "*pontos percentuais* caiu? [p=0.3] E quantos *por cento?* [p=0.3] {c}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Pontos percentuais: [p=0.2] quarenta menos trinta, [p=0.2] *dez pontos.* [p=0.4] "
        "{b}Por cento: [p=0.2] dez dividido pelo valor de antes, [p=0.2] que é quarenta: [p=0.2] *vinte e cinco por "
        "cento.* [p=0.4] {c}A aprovação caiu dez pontos, [p=0.2] e isso é uma queda de *um quarto* do que ela era."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] ponto percentual: a diferença. [p=0.2] Por cento: em "
        "relação ao que era. [p=0.5] {b}Dois: [p=0.2] na pizza, um por cento vale três vírgula seis graus. [p=0.5] "
        "{c}Três: [p=0.2] só se somam porcentagens do mesmo todo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dizer *subiu dois por cento* [p=0.2] quando "
        "subiu *dois pontos percentuais.* [p=0.4] {b}Parece certo, [p=0.2] porque os dois números têm o sinal de por cento. "
        "[p=0.4] {c}Mas a diferença entre duas taxas [p=0.2] se mede em *pontos.* [p=0.3] Em por cento, [p=0.2] de dois "
        "para quatro é *cem por cento.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] usar o *valor final* como base. [p=0.2] De cinco para seis, [p=0.2] um dividido por seis. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o seis é o número mais recente. [p=0.4] {c}Mas a base é sempre *o que era "
        "antes:* [p=0.2] um dividido por cinco, [p=0.2] *vinte por cento.*"),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] *somar* porcentagens de grupos diferentes. [p=0.2] Trinta mais trinta, [p=0.2] sessenta. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque são porcentagens da mesma pesquisa. [p=0.4] {c}Mas cada uma é de um *todo "
        "diferente.* [p=0.3] Conte as pessoas: [p=0.2] deu *trinta por cento* do grupo."),

    # ================= QUESTÃO 7 DO MATERIAL =================
    dict(id="23", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Um levantamento apontou "
        "que a taxa de desemprego de uma região [p=0.2] passou de *oito por cento* para *dez por cento* em um ano. [p=0.4] "
        "{b}Sobre essa mudança, [p=0.2] é correto afirmar que a taxa: [p=0.4] {qa}A: [p=0.2] aumentou dois por cento. "
        "[p=0.3] {qb}B: [p=0.2] aumentou dois pontos percentuais, [p=0.2] o que corresponde a um aumento relativo de vinte e "
        "cinco por cento. [p=0.3] {qc}C: [p=0.2] aumentou vinte por cento. [p=0.3] {qd}D: [p=0.2] aumentou dez pontos "
        "percentuais. [p=0.3] {qe}E: [p=0.2] dobrou. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="24", block="q7", text=
        "{t}Vamos resolver. [p=0.3] {a}A diferença: [p=0.2] dez menos oito, [p=0.2] *dois pontos percentuais.* [p=0.4] "
        "{b}A variação relativa: [p=0.2] dois dividido pelo de antes, [p=0.2] que é oito: [p=0.2] *vinte e cinco por "
        "cento.* [p=0.3] {ok}*Letra B!* [p=0.2] Ela traz as duas leituras certas. [p=0.5] {xa}A A é o erro de linguagem "
        "do jornal: [p=0.2] subir dois por cento [p=0.2] levaria oito para oito vírgula dezesseis. [p=0.4] {xc}A C usou o "
        "*valor final* como base: [p=0.2] dois dividido por dez. [p=0.4] {xd}A D leu a taxa nova [p=0.2] como se fosse a "
        "diferença. [p=0.4] {xe}E a E: [p=0.2] dobrar seria ir de oito para *dezesseis.*"),

    # ================= QUESTÃO 8 DO MATERIAL =================
    dict(id="25", block="q8", text=
        "{t}E a segunda. [p=0.3] {a}Em um gráfico de setores [p=0.2] que representa a distribuição de gastos de uma família, "
        "[p=0.2] o setor correspondente aos gastos com transporte [p=0.2] tem ângulo central de *cinquenta e quatro graus.* "
        "[p=0.4] {b}Esse setor representa, [p=0.2] do total de gastos: [p=0.4] {qa}A: [p=0.2] cinco vírgula quatro por "
        "cento. [p=0.3] {qb}B: [p=0.2] dez. [p=0.3] {qc}C: [p=0.2] quinze. [p=0.3] {qd}D: [p=0.2] dezoito. [p=0.3] {qe}E: "
        "[p=0.2] cinquenta e quatro por cento. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q8", text=
        "{t}Vamos resolver. [p=0.3] {a}De graus para por cento: [p=0.2] divida por três vírgula seis. [p=0.3] Cinquenta e "
        "quatro dividido por três vírgula seis: [p=0.2] *quinze.* [p=0.4] {b}Pelo atalho: [p=0.2] cinquenta e quatro é "
        "trinta e seis mais dezoito. [p=0.2] Dez por cento, [p=0.2] mais a metade disso, [p=0.2] cinco: [p=0.2] *quinze por "
        "cento.* [p=0.3] {ok}*Letra C!* [p=0.4] {c}Conferindo: [p=0.2] quinze vezes três vírgula seis [p=0.2] dá cinquenta e "
        "quatro. [p=0.5] {xe}A E leu o *grau* como se fosse por cento. [p=0.4] {xa}A A dividiu por dez, [p=0.2] como se "
        "cada por cento valesse dez graus. [p=0.4] {xd}A D dividiu por três, [p=0.2] e não por três vírgula seis. [p=0.4] "
        "{xb}E a B é a fatia de *trinta e seis* graus, [p=0.2] não de cinquenta e quatro."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] ponto percentual: a diferença. [p=0.2] Por cento: "
        "em relação ao que era. [p=0.5] {b}Dois: [p=0.2] na pizza, um por cento vale três vírgula seis graus. [p=0.5] "
        "{c}Três: [p=0.2] só se somam porcentagens do mesmo todo."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] {b}juntamos tudo, [p=0.2] {c}caçamos as pegadinhas [p=0.2] {d}e "
        "treinamos com *questões novas.*"),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha visto uma manchete falar em por cento quando era ponto "
        "percentual? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
