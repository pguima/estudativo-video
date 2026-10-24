# Roteiro — Unidades de Medida e Conversões, Episódio 2 de 5: Área e volume — por que os degraus valem 100 e 1 000,
#   e a ponte entre litro e metro cúbico
# Base: Estudos/Enem/estudos/01-matematica/10-unidades-conversoes.html — seções 04 e 05 + "1 cm³ de água pesa 1 g" (seção 06)
#   + Questões 1 (eu faço), 2 (nós fazemos) e 9 (você faz).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   Na área, cada degrau é uma GRADE de 10 × 10 = 100 quadradinhos; no volume, um CUBO de 10 × 10 × 10 = 1 000 cubinhos.
#   A CAIXA DE LEITE de 1 litro: o leite dela enche exatamente um cubo de 10 cm (1 dm) de aresta → 1 L = 1 dm³.
#   1 litro de água pesa 1 quilo (a garrafa na balança).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Caixa de leite (desvio consciente): o prompt diz que a caixa "é quase um cubo de 10 cm de lado". A caixa real de 1 L mede
#   uns 6 × 9 × 17 cm (alta e fina). Para não ensinar algo falso, o vídeo diz que ela NÃO tem forma de cubo, mas o leite dela
#   enche certinho um cubo de 10 cm de aresta. A caixa continua EXPLICANDO o litro (mesmo volume, outra forma).
# Exemplos: nenhum bloco usa a piscina 8 × 5 × 1,5 (Q9 "você faz"). A Q1 (2,5 ha) é "eu faço" e a Q2 (1,2 m³) é "nós fazemos".
# Q1 (material, sem explicação das erradas): 2,5 · 10 000 = 25 000 → C. Conferência pelo campo (≈ 0,7 ha): 2,5 ha ≈ 3,5 campos.
#   Explicações NOSSAS: A (250) = × 100, como se fosse o are · B (2 500) = hectare de 1 000 m² (erro clássico) ·
#   D (250 000) = um zero a mais · E (2 500 000) = tratou hectare como km² (100 vezes maior).
# Q2 (material): 1,2 · 1 000 = 1 200 L → D; conferência: caixas residenciais de 500 a 2 000 L (material).
#   Explicações NOSSAS: A (1,2) = m³ = litro · B (12) = degrau de 10 · C (120) = degrau de 100 · E (12 000) = fator de área.
#   Imprecisão do material: "A, B e C dariam volumes menores que um balde" — 120 L não é menos que um balde. No vídeo:
#   A e B dariam menos que um balde; a C mal enche uma banheira.
# Q9 (material): V = 8 · 5 · 1,5 = 60 m³ → 60 000 L → D; a tentação é responder 60 (A, explicação do material).
#   Explicações NOSSAS: B (600) e C (6 000) = fatores 10 e 100 · E (600 000) = fator de área (10 000).
#   Conferência: 60 caixas-d'água de 1 000 L; 60 toneladas de água.
# Atalhos (verde): "área: dois zeros por degrau" · "na dúvida, converta o LADO e multiplique lado por lado" ·
#   "hectare → m²: × 10 000 (quatro zeros)" · "volume: três zeros por degrau" · "para água: litros e quilos são o mesmo número".
# Fórmula explicada na hora: volume do bloco retangular = comprimento × largura × altura (quantos cubinhos de 1 m cabem).
# Frases-chave (meio e fim, idênticas): 1. Área: cada degrau vale 100. Volume: cada degrau vale 1 000.
#   2. 1 litro é 1 decímetro cúbico; 1 metro cúbico são 1 000 litros. 3. 1 litro de água pesa 1 quilo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Área e volume sem errar: metro quadrado, metro cúbico e litro · Unidades de medida, episódio 2"

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
        "{a}Um metro quadrado tem *cem* centímetros quadrados? [p=0.4] {b}Um metro cúbico tem *um* litro? [p=0.5] "
        "{c}As duas respostas estão *erradas,* [p=0.2] e são os dois erros mais caros deste assunto."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai converter área e volume *sem errar* [p=0.3] {b}e passar de metro cúbico para "
        "*litro* [p=0.2] e para *quilo de água.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido do episódio um. [p=0.3] {a}A escada das medidas de comprimento tem *sete degraus:* "
        "[p=0.2] quilômetro, hectômetro, decâmetro, *metro,* decímetro, centímetro e milímetro. [p=0.4] {b}Lembra da frase? "
        "[p=0.2] *Kátia Hoje Dançou Muito, Dançou Com Marcos.* [p=0.4] {c}Descer um degrau multiplica por *dez;* [p=0.2] "
        "subir divide por dez. [p=0.3] {d}Um metro são dez decímetros, [p=0.2] ou cem centímetros."),

    # ================= CONCRETO =================
    dict(id="04", block="cotidiano", text=
        "{t}Agora olhe ao redor. [p=0.3] {a}O piso da cozinha, [p=0.2] coberto de azulejos. [p=0.3] {b}Uma caixa de leite "
        "de um litro. [p=0.3] {c}A caixa-d'água no telhado. [p=0.3] {d}Uma piscina, [p=0.2] um campo de futebol. [p=0.4] "
        "{e}Nenhum deles se mede com uma régua só. [p=0.2] O piso tem *largura e comprimento.* [p=0.2] A caixa tem "
        "largura, comprimento *e altura.*"),
    dict(id="05", block="defs", text=
        "{t}O piso pede uma medida de *área:* [p=0.2] o tamanho de uma superfície, [p=0.2] quanto chão ela cobre. [p=0.4] "
        "{a}A área se mede em quadradinhos. [p=0.3] O *metro quadrado,* [p=0.2] que se escreve *m* com um dois pequenininho "
        "no alto, [p=0.2] é um quadrado de *um metro* de cada lado. [p=0.4] {b}O centímetro quadrado é um quadradinho de "
        "um centímetro: [p=0.2] mais ou menos do tamanho de uma unha."),
    dict(id="06", block="defs", text=
        "{t}Já a caixa pede uma medida de *volume:* [p=0.2] o espaço que uma coisa ocupa. [p=0.4] {a}O volume se mede em "
        "cubinhos. [p=0.3] O *metro cúbico,* [p=0.2] *m* com um três pequenininho, [p=0.2] é um cubo de um metro de "
        "*aresta.* [p=0.3] Aresta é cada beirada do cubo. [p=0.4] {b}E *capacidade* é quanto cabe lá dentro: [p=0.2] é ela "
        "que a gente mede em *litros.*"),

    # ================= BLOCO A: ÁREA, A GRADE =================
    dict(id="07", block="grade", text=
        "{t}E aqui vem a pergunta do gancho. [p=0.3] Um decímetro quadrado tem quantos centímetros quadrados? [p=0.4] "
        "{a}Desenhe o quadrado: [p=0.2] um decímetro de lado, [p=0.2] ou seja, *dez centímetros.* [p=0.4] {b}Na primeira "
        "fileira cabem *dez* quadradinhos de um centímetro. [p=0.3] {c}Mas são *dez fileiras.* [p=0.3] {d}Dez vezes dez: "
        "[p=0.2] *cem* quadradinhos. [p=0.4] {e}Na área, [p=0.2] cada degrau da escada é uma *grade de dez por dez:* "
        "[p=0.2] vale *cem.*"),
    dict(id="08", block="escada_area", text=
        "{t}Então a escada é a mesma, [p=0.2] mas cada degrau agora vale *cem.* [p=0.4] {a}Um metro quadrado [p=0.2] são "
        "*cem* decímetros quadrados. [p=0.3] {b}Um degrau a mais: [p=0.2] *dez mil* centímetros quadrados. [p=0.3] {c}Mais "
        "um: [p=0.2] *um milhão* de milímetros quadrados. [p=0.4] {d}E do quilômetro quadrado ao metro quadrado [p=0.2] são "
        "três degraus: [p=0.2] cem, vezes cem, vezes cem. [p=0.2] *Um milhão* de metros quadrados. [p=0.4] {e}Atalho: "
        "[p=0.2] em área, [p=0.2] *dois zeros por degrau.*"),

    # ================= BLOCO B: CONFIRMAÇÃO SEM DECORAR =================
    dict(id="09", block="confirma", text=
        "{t}E se você esquecer? [p=0.3] Confira sem decorar. [p=0.3] {a}Um metro quadrado é um quadrado de *cem "
        "centímetros* de lado. [p=0.4] {b}Cem quadradinhos na primeira fileira, [p=0.2] e *cem fileiras.* [p=0.3] {c}Cem "
        "vezes cem: [p=0.2] *dez mil* centímetros quadrados. [p=0.4] {d}Atalho: [p=0.2] na dúvida, [p=0.2] converta o "
        "*lado* [p=0.2] e multiplique lado por lado."),

    # ================= BLOCO C: UNIDADES AGRÁRIAS =================
    dict(id="10", block="hectare", text=
        "{t}No campo, [p=0.2] ninguém mede terra em metro quadrado. [p=0.3] Mede em *hectare.* [p=0.4] {a}Um hectare é um "
        "quadrado de *cem metros* de lado. [p=0.3] Cem vezes cem: [p=0.2] *dez mil metros quadrados.* [p=0.4] {b}Cem metros "
        "é um *hectômetro.* [p=0.2] Então o hectare é o hectômetro quadrado [p=0.2] da nossa escada. [p=0.4] {c}O *are* é "
        "menor: [p=0.2] um quadrado de dez metros de lado, [p=0.2] cem metros quadrados. [p=0.4] {d}E um quilômetro "
        "quadrado [p=0.2] tem *cem hectares.*"),
    dict(id="11", block="hectare", text=
        "{t}Para ter uma referência na cabeça: [p=0.3] {a}um campo de futebol oficial mede uns cento e cinco por sessenta e "
        "oito metros, [p=0.2] perto de *sete mil* metros quadrados. [p=0.3] {b}É mais ou menos *zero vírgula sete* "
        "hectare. [p=0.4] {c}Atalho: [p=0.2] de hectare para metro quadrado, [p=0.2] *vezes dez mil.* [p=0.2] Quatro zeros."),

    # ================= BLOCO D: VOLUME, O CUBO =================
    dict(id="12", block="cubo", text=
        "{t}E no volume? [p=0.3] Um decímetro cúbico tem quantos centímetros cúbicos? [p=0.4] {a}Pegue um cubo de *dez "
        "centímetros* de aresta. [p=0.3] {b}A camada do fundo [p=0.2] é uma grade de dez por dez: [p=0.2] *cem* cubinhos. "
        "[p=0.4] {c}E são *dez camadas.* [p=0.3] {d}Cem vezes dez: [p=0.2] *mil* cubinhos. [p=0.4] {e}No volume, [p=0.2] "
        "cada degrau é um *cubo de dez por dez por dez:* [p=0.2] vale *mil.*"),
    dict(id="13", block="escada_vol", text=
        "{t}Então: [p=0.3] {a}um metro cúbico [p=0.2] são *mil* decímetros cúbicos. [p=0.3] {b}Mais um degrau: [p=0.2] "
        "*um milhão* de centímetros cúbicos. [p=0.4] {c}Atalho: [p=0.2] em volume, [p=0.2] *três zeros por degrau.*"),

    # ================= BLOCO E: A CAIXA DE LEITE =================
    dict(id="14", block="leite", text=
        "{t}E o litro, [p=0.2] onde ele entra nessa escada? [p=0.3] Pegue uma caixa de leite de *um litro.* [p=0.4] {a}Ela "
        "não tem forma de cubo: [p=0.2] é alta e fininha. [p=0.3] {b}Mas despeje esse leite numa caixinha em forma de "
        "cubo, [p=0.2] com *dez centímetros* de aresta. [p=0.4] {c}Enche certinho, [p=0.2] até a boca. [p=0.4] {d}Dez "
        "centímetros é um decímetro. [p=0.3] Então *um litro é um decímetro cúbico.* [p=0.3] É o decímetro cúbico que "
        "você já segurou na mão."),
    dict(id="15", block="ponte_litro", text=
        "{t}E dessa caixa saem as outras. [p=0.3] {a}O decímetro cúbico tem mil centímetros cúbicos, [p=0.2] e o litro tem "
        "mil mililitros. [p=0.3] {b}Então *um mililitro é um centímetro cúbico:* [p=0.2] um cubinho de um centímetro. "
        "[p=0.2] É por isso que a seringa de remédio marca mililitro [p=0.2] ou centímetro cúbico. [p=0.4] {c}E o metro "
        "cúbico tem mil decímetros cúbicos. [p=0.3] {d}Então *um metro cúbico são mil litros:* [p=0.2] uma caixa-d'água "
        "de mil litros."),

    # ================= BLOCO F: O ENGANO DO METRO CÚBICO =================
    dict(id="16", block="mil_caixas", text=
        "{t}Aqui mora o segundo erro do gancho. [p=0.3] {a}Um metro cúbico *não* é um litro. [p=0.3] {b}Imagine o cubo de "
        "um metro sendo enchido com caixinhas de um litro. [p=0.3] {c}Dez numa fileira, [p=0.2] dez fileiras numa camada, "
        "[p=0.2] dez camadas. [p=0.4] {d}Dez vezes dez vezes dez: [p=0.2] *mil litros.*"),

    # ================= BLOCO G: A MASSA DA ÁGUA =================
    dict(id="17", block="agua", text=
        "{t}E quanto *pesa* isso? [p=0.3] {a}Um centímetro cúbico de água pura [p=0.2] pesa *um grama.* [p=0.4] {b}Então um "
        "litro, [p=0.2] que tem mil centímetros cúbicos, [p=0.2] pesa mil gramas: [p=0.2] *um quilo.* [p=0.2] Ponha uma "
        "garrafa de um litro de água na balança: [p=0.2] um quilo. [p=0.4] {c}E um metro cúbico, [p=0.2] mil litros, "
        "[p=0.2] pesa mil quilos: [p=0.2] *uma tonelada.* [p=0.4] {d}Atalho: [p=0.2] para água, [p=0.2] *litros e quilos "
        "são o mesmo número.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Três conversões. [p=0.3] {a}Três metros quadrados em centímetros quadrados. [p=0.3] {b}Zero "
        "vírgula cinco metro cúbico em litros. [p=0.3] {c}Duzentos e cinquenta mililitros em centímetros cúbicos. [p=0.4] "
        "{d}*Pause o vídeo e converta.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}De metro quadrado para centímetro quadrado: [p=0.2] dois degraus de área, [p=0.2] "
        "vezes dez mil. [p=0.2] Três vezes dez mil: [p=0.2] *trinta mil.* [p=0.4] {b}De metro cúbico para litro: [p=0.2] "
        "vezes mil. [p=0.2] Meio metro cúbico: [p=0.2] *quinhentos litros.* [p=0.4] {c}E mililitro é centímetro cúbico: "
        "[p=0.2] *duzentos e cinquenta.* [p=0.2] Nem precisa de conta."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] área: cada degrau vale cem. [p=0.2] Volume: cada degrau "
        "vale mil. [p=0.5] {b}Dois: [p=0.2] um litro é um decímetro cúbico; [p=0.2] um metro cúbico são mil litros. "
        "[p=0.5] {c}Três: [p=0.2] um litro de água pesa um quilo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] um metro quadrado [p=0.2] igual a *cem* "
        "centímetros quadrados. [p=0.4] {b}Parece certo, [p=0.2] porque um metro tem cem centímetros. [p=0.4] {c}Mas isso "
        "é o *lado.* [p=0.2] A área é lado vezes lado: [p=0.2] *dez mil.*"),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] um metro cúbico [p=0.2] igual a *mil* centímetros cúbicos. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque volume vale mil por degrau. [p=0.4] {c}Mas do metro ao centímetro são *dois* degraus: [p=0.2] mil vezes "
        "mil, [p=0.2] *um milhão.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] um metro cúbico [p=0.2] igual a *um* litro. [p=0.4] {b}Parece certo, [p=0.2] porque os dois "
        "parecem a unidade principal de volume. [p=0.4] {c}Mas o litro é o *decímetro* cúbico, [p=0.2] a caixa de leite. "
        "[p=0.2] O metro cúbico são *mil* litros."),
    dict(id="24", block="erros", text=
        "{a}Quarto: [p=0.2] um hectare [p=0.2] igual a *mil* metros quadrados. [p=0.4] {b}Parece certo, [p=0.2] porque mil "
        "é o número das conversões de sempre. [p=0.4] {c}Mas o hectare é um quadrado de cem metros de lado: [p=0.2] cem "
        "vezes cem, [p=0.2] *dez mil.*"),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="25", block="q1", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.3] Esta primeira, [p=0.2] eu faço "
        "com você. [p=0.4] {a}Um produtor rural pretende cercar uma área de plantio de *dois vírgula cinco hectares.* "
        "[p=0.4] {b}Essa área, [p=0.2] expressa em metros quadrados, [p=0.2] corresponde a: [p=0.4] {qa}A: [p=0.2] duzentos e "
        "cinquenta. [p=0.3] {qb}B: [p=0.2] dois mil e quinhentos. [p=0.3] {qc}C: [p=0.2] vinte e cinco mil. [p=0.3] "
        "{qd}D: [p=0.2] duzentos e cinquenta mil. [p=0.3] {qe}E: [p=0.2] dois milhões e quinhentos mil."),
    dict(id="26", block="q1", text=
        "{t}Vamos lá. [p=0.3] {a}Um hectare é um quadrado de cem metros de lado: [p=0.2] *dez mil* metros quadrados. "
        "[p=0.4] {b}Dois vírgula cinco vezes dez mil: [p=0.2] a vírgula anda quatro casas, [p=0.2] *vinte e cinco mil.* "
        "[p=0.3] {ok}*Letra C!* [p=0.4] {c}Confira com o campo de futebol, [p=0.2] de zero vírgula sete hectare. [p=0.3] "
        "Dois vírgula cinco hectares [p=0.2] dão uns *três campos e meio.* [p=0.2] Três e meio vezes sete mil: [p=0.2] perto "
        "de vinte e cinco mil. [p=0.2] Fecha!"),
    dict(id="27", block="q1", text=
        "{t}E as outras? [p=0.3] {xb}A B usou o hectare de *mil* metros quadrados, [p=0.2] o quarto erro clássico. [p=0.4] "
        "{xa}A A multiplicou só por cem, [p=0.2] como se fosse o *are.* [p=0.4] {xd}A D pôs um zero a mais. [p=0.4] {xe}E a "
        "E tratou o hectare como *quilômetro quadrado,* [p=0.2] que é cem vezes maior."),

    # ================= QUESTÃO 2 (NÓS FAZEMOS) =================
    dict(id="28", block="q2", text=
        "{t}A próxima, [p=0.2] a gente faz junto. [p=0.3] {a}Uma caixa-d'água tem capacidade de *um vírgula dois metro "
        "cúbico.* [p=0.3] {b}O volume de água que ela comporta, [p=0.2] em litros, [p=0.2] é de: [p=0.4] {qa}A: [p=0.2] um "
        "vírgula dois litro. [p=0.3] {qb}B: [p=0.2] doze. [p=0.3] {qc}C: [p=0.2] cento e vinte. [p=0.3] {qd}D: [p=0.2] mil "
        "e duzentos. [p=0.3] {qe}E: [p=0.2] doze mil litros. [p=0.4] {p}Pause e me diga: [p=0.2] qual é a ponte entre "
        "metro cúbico e litro? [p=1.5]"),
    dict(id="29", block="q2", text=
        "{t}A ponte: [p=0.2] *um metro cúbico são mil litros.* [p=0.4] {a}Então um vírgula dois vezes mil: [p=0.2] *mil e "
        "duzentos litros.* [p=0.3] {ok}*Letra D!* [p=0.4] {b}Confira: [p=0.2] caixas-d'água de casa têm entre quinhentos e "
        "dois mil litros. [p=0.2] Fecha. [p=0.4] {xa}A A trocou metro cúbico por litro. [p=0.3] {xb}A B usou o degrau de "
        "dez, [p=0.2] {xc}e a C, o de cem: [p=0.2] a B dá menos que um balde, [p=0.2] e a C mal enche uma banheira. [p=0.3] "
        "{xe}E a E usou o fator de *área,* [p=0.2] dez mil."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="30", block="q9", text=
        "{t}E a última, [p=0.2] *você faz.* [p=0.3] {a}Uma piscina retangular tem *oito* metros de comprimento, [p=0.2] "
        "*cinco* metros de largura [p=0.2] e *um vírgula cinco* metro de profundidade uniforme. [p=0.4] {b}Cheia até a "
        "borda, [p=0.2] ela comporta: [p=0.4] {qa}A: [p=0.2] sessenta litros. [p=0.3] {qb}B: [p=0.2] seiscentos. [p=0.3] "
        "{qc}C: [p=0.2] seis mil. [p=0.3] {qd}D: [p=0.2] sessenta mil. [p=0.3] {qe}E: [p=0.2] seiscentos mil litros. "
        "[p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="31", block="q9", text=
        "{t}Vamos resolver. [p=0.3] {a}Primeiro, o volume. [p=0.2] Numa caixa retangular, [p=0.2] o volume é *comprimento "
        "vezes largura vezes altura:* [p=0.2] quantos cubinhos de um metro cabem lá dentro. [p=0.4] {b}Oito vezes cinco, "
        "[p=0.2] quarenta, [p=0.2] vezes um vírgula cinco: [p=0.2] *sessenta metros cúbicos.* [p=0.4] {c}E agora, [p=0.2] o "
        "passo que a questão quer ver: [p=0.2] vezes mil. [p=0.2] *Sessenta mil litros.* [p=0.3] {ok}*Letra D!*"),
    dict(id="32", block="q9", text=
        "{t}E a tentação? [p=0.3] {xa}A A é exatamente o *sessenta,* [p=0.2] o volume em metros cúbicos, [p=0.2] sem "
        "converter. [p=0.4] {xb}A B [p=0.2] {xc}e a C usaram os fatores de dez e de cem. [p=0.3] {xe}A E, [p=0.2] o fator "
        "de área. [p=0.4] {c}E confira: [p=0.2] sessenta mil litros [p=0.2] são sessenta caixas-d'água de mil litros, "
        "[p=0.2] e *sessenta toneladas* de água. [p=0.2] Para uma piscina dessas, [p=0.2] faz sentido."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] área: cada degrau vale cem. [p=0.2] Volume: cada "
        "degrau vale mil. [p=0.5] {b}Dois: [p=0.2] um litro é um decímetro cúbico; [p=0.2] um metro cúbico são mil litros. "
        "[p=0.5] {c}Três: [p=0.2] um litro de água pesa um quilo."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Todas as unidades andam de dez em dez. [p=0.3] {b}Menos uma: [p=0.2] *o tempo.* [p=0.4] {c}E é por isso que "
        "ele derruba tanta gente. [p=0.4] {d}Próximo episódio."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantos litros cabem na caixa-d'água da sua casa? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
