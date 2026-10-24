# Roteiro — Escalas, Plantas e Mapas, Episódio 3 de 4: Plantas e maquetes — a área usa n² e o volume usa n³
# Base: Estudos/Enem/estudos/01-matematica/11-escalas-plantas-mapas.html — seções 06, 07 e 08
#   + Questões 9 (aquecimento), 5 (eu faço), 6 (nós fazemos) e 7 (você faz).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   Na planta 1 : 200, o QUADRADINHO de 1 cm² tem lado 1 cm; no mundo real o lado vira 2 m, e o quadradinho vira um quadrado
#   de 2 m × 2 m = 4 m² (quatro quadrados de 1 m²).
#   A MAQUETE encolhe em TRÊS direções ao mesmo tempo: comprimento, largura e altura. 20 × 20 × 20 = 8 000.
#   1 : 100 é a escala mais amigável: 1 cm do papel é exatamente 1 metro.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte. "n" é falado "ene" (o número de baixo
#   da escala, apresentado na cena 09).
# Exemplos: o prompt desenhou os blocos com os números das próprias questões (bloco c = Q6, bloco d = Q5, bloco e = Q7, e o
#   gancho já revela os 40 000 L da Q7). Mantidos como o usuário desenhou: a Q7 "você faz" vira a prova de que o aluno refaz
#   o caminho SOZINHO, e o valor novo dela está nas alternativas erradas. O "nós fazemos" (1 : 50, 6 × 8 cm) é inédito.
# Q9 (material): 7 · 50 = 350 cm = 3,5 m → B. Plausibilidade (material): D = 35 m, um prédio; A = 35 cm, menos que um passo.
#   Explicações NOSSAS do mecanismo: A (0,35 m) = multiplicou por 5 em vez de 50 · C (7 m) = leu como se fosse 1 : 100 ·
#   D (35 m) = dividiu os 350 cm por 10 em vez de 100 · E (350 m) = chamou os 350 centímetros de metros.
# Q5 (material): 5 m × 4 m = 20 m² → C; pelo fator de área 20 cm² · 100² = 200 000 cm² = 20 m².
#   Explicações NOSSAS: A (0,2 m²) = fator linear na área (20 · 100 = 2 000 cm²) · B (2 m²) = 200 000 cm² ÷ 100 000 (cortou
#   cinco zeros, o atalho do quilômetro fora do lugar) · D (200 m²) = ÷ 1 000 · E (2 000 m²) = ÷ 100, como se fosse comprimento.
# Q6 (material): 1 · 200² = 40 000 cm² = 4 m² → C. IMPRECISÃO do material: "a alternativa B (2 m²) é de quem aplicou o fator
#   200 uma vez só". Quem aplica o fator uma vez só chega a 200 cm² = 0,02 m², que é a A. No vídeo: A = fator linear;
#   B = 200 cm² convertidos dividindo por 100, como comprimento. Explicações NOSSAS: D (20 m²) = grande demais (o quadrado real
#   tem só 2 m de lado; 20 m² é uma sala inteira) · E (40 m²) = 40 000 ÷ 1 000 em vez de ÷ 10 000.
# Q7 (material): 5 · 20³ = 40 000 L = 40 m³ → D; A = fator linear, C = esqueceu os 5 L (material).
#   Explicações NOSSAS: B (2 000 L) = fator de ÁREA, 5 · 400 · E (400 000 L) = um zero a mais.
# Atalhos (verde): "em 1 : 100, troque cm por m" · "em 1 : 50, metade do número em cm dá metros" ·
#   "ache o LADO real de 1 cm e eleve ao quadrado" · "converta os lados primeiro" · "capacidade real = maquete × n³".
# Fórmulas explicadas na hora: área do retângulo = base × altura (quantos quadradinhos de 1 m² cabem) ·
#   1 m² = 10 000 cm² (100 × 100) · 1 m³ = 1 000 L.
# Frases-chave (meio e fim, idênticas): 1. Comprimento usa n; área usa n²; volume usa n³.
#   2. Em planta, converta os lados antes de calcular a área. 3. Em 1 : 100, 1 centímetro é 1 metro.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Planta e maquete no ENEM: por que a área usa n² e o volume usa n³ · Escalas, episódio 3"

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
        "{a}Numa maquete *um para vinte,* [p=0.2] a caixa-d'água comporta *cinco litros.* [p=0.4] {b}A caixa real comporta "
        "*cem litros?* [p=0.5] {c}Não: [p=0.2] comporta *quarenta mil.* [p=0.4] {d}Esse é o erro mais caro deste assunto."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai calcular *áreas* a partir de plantas [p=0.2] {b}e *volumes* a partir de maquetes "
        "[p=0.3] {c}sem esquecer o *quadrado* e o *cubo.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] para achar a medida *real,* [p=0.2] "
        "multiplique a do desenho pelo número de baixo da escala. [p=0.3] Do papel para o mundo, [p=0.2] o número *cresce.* "
        "[p=0.4] {b}A área de um retângulo é *base vezes altura:* [p=0.2] quantos quadradinhos cabem lá dentro. [p=0.4] "
        "{c}Um metro quadrado tem *dez mil* centímetros quadrados, [p=0.2] porque são cem por cem. [p=0.3] {d}E um metro "
        "cúbico são *mil litros.*"),

    # ================= CONCRETO =================
    dict(id="04", block="cotidiano", text=
        "{t}Agora imagine um apartamento à venda. [p=0.3] {a}O anúncio traz um desenho dele, [p=0.2] visto de cima. "
        "[p=0.3] {b}No papel, [p=0.2] a sala tem *cinco centímetros* por *quatro.* [p=0.4] {c}E na entrada do prédio "
        "[p=0.2] tem uma miniatura dele, [p=0.2] com caixa-d'água e tudo. [p=0.4] {d}Quanto mede a sala de verdade? "
        "[p=0.2] Quanta água cabe na caixa de verdade?"),
    dict(id="05", block="defs", text=
        "{t}Esse desenho tem nome. [p=0.3] {a}A *planta baixa* é o desenho da casa vista de cima, [p=0.2] como se alguém "
        "tirasse o teto. [p=0.4] {b}O projeto ainda traz o *corte,* [p=0.2] o prédio fatiado de cima a baixo, [p=0.2] "
        "{c}e a *fachada,* [p=0.2] a vista de fora. [p=0.2] Todos na mesma escala. [p=0.4] {d}E a miniatura é a "
        "*maquete:* [p=0.2] um modelo em três dimensões, [p=0.2] encolhido."),

    # ================= BLOCO A: PLANTAS E PROJETOS =================
    dict(id="06", block="plantas", text=
        "{t}E quanto vale um centímetro numa planta? [p=0.3] Depende da escala. [p=0.4] {a}Em *um para vinte,* [p=0.2] "
        "usada para móveis e detalhes, [p=0.2] um centímetro vale *vinte centímetros.* [p=0.3] {b}Em *um para cinquenta,* "
        "[p=0.2] a planta de uma casa: [p=0.2] *cinquenta centímetros.* [p=0.3] {c}Em *um para cem,* [p=0.2] a planta de "
        "um prédio: [p=0.2] *um metro.* [p=0.3] {d}Em um para quinhentos, [p=0.2] um loteamento: [p=0.2] cinco metros. "
        "[p=0.3] {e}E em um para mil, [p=0.2] o plano de uma cidade: [p=0.2] dez metros."),
    dict(id="07", block="cem", text=
        "{t}Repare na de *um para cem.* [p=0.3] {a}Um centímetro vezes cem [p=0.2] são cem centímetros: [p=0.2] *um "
        "metro.* [p=0.4] {b}Uma parede de sete centímetros no papel [p=0.2] mede *sete metros.* [p=0.3] {c}É a escala mais "
        "amigável de todas. [p=0.4] {d}Atalho: [p=0.2] em um para cem, [p=0.2] *é só trocar centímetro por metro.* "
        "[p=0.3] {e}E em um para cinquenta, [p=0.2] cada centímetro é meio metro: [p=0.2] *a metade do número* dá os metros."),

    # ================= BLOCO B: AS TRÊS ESCALAS =================
    dict(id="08", block="tres", text=
        "{t}Mas e a *área?* [p=0.3] Ela usa a mesma escala? [p=0.4] {a}Chame o número de baixo da escala de *ene.* "
        "[p=0.3] {b}A escala que você já conhece, [p=0.2] um para ene, [p=0.2] é a *escala linear:* [p=0.2] vale para "
        "*comprimentos.* [p=0.4] {c}A área tem *duas* medidas, [p=0.2] comprimento e largura. [p=0.2] Cada uma cresce ene "
        "vezes. [p=0.2] Então a *escala de área* é um para *ene ao quadrado.* [p=0.4] {d}E o volume tem *três* medidas. "
        "[p=0.2] A *escala de volume* é um para *ene ao cubo.*"),

    # ================= BLOCO C: O QUADRADINHO QUE VIRA 4 m² =================
    dict(id="09", block="quadradinho", text=
        "{t}Teste. [p=0.2] Numa planta *um para duzentos,* [p=0.2] um centímetro quadrado vale quanto? [p=0.4] {a}Pela "
        "escala de área: [p=0.2] duzentos ao quadrado [p=0.2] é duzentos vezes duzentos, [p=0.2] *quarenta mil.* [p=0.3] "
        "{b}Um centímetro quadrado vira *quarenta mil* centímetros quadrados. [p=0.4] {c}Para passar a metro quadrado, "
        "[p=0.2] divida por dez mil: [p=0.2] *quatro metros quadrados.*"),
    dict(id="10", block="quadradinho", text=
        "{t}Parece mágica? [p=0.3] Então veja. [p=0.3] {a}Um centímetro quadrado [p=0.2] é um quadradinho de *um "
        "centímetro* de lado. [p=0.4] {b}No mundo real, [p=0.2] esse lado vira duzentos centímetros: [p=0.2] *dois "
        "metros.* [p=0.4] {c}E o quadradinho vira um quadrado de *dois metros por dois metros.* [p=0.3] {d}Dentro dele "
        "cabem *quatro* quadrados de um metro quadrado. [p=0.4] {e}Atalho: [p=0.2] ache quanto vale o *lado* em metros "
        "[p=0.2] e eleve ao quadrado."),

    # ================= BLOCO D: CONVERTA OS LADOS PRIMEIRO =================
    dict(id="11", block="lados", text=
        "{t}E a sala do anúncio, [p=0.2] cinco por quatro centímetros, [p=0.2] numa planta *um para cem?* [p=0.4] "
        "{a}Existe um caminho mais seguro do que usar o quadrado. [p=0.3] {b}Converta os *lados* primeiro. [p=0.2] Cinco "
        "centímetros viram *cinco metros.* [p=0.2] Quatro centímetros viram *quatro metros.* [p=0.4] {c}Agora a área, "
        "[p=0.2] com as medidas reais: [p=0.2] cinco vezes quatro, [p=0.2] *vinte metros quadrados.* [p=0.4] {d}Assim "
        "você nunca esquece o quadrado, [p=0.2] porque ele acontece sozinho [p=0.2] quando você multiplica lado por lado."),

    # ================= BLOCO E: A MAQUETE E O CUBO =================
    dict(id="12", block="maquete", text=
        "{t}E a caixa-d'água da maquete? [p=0.3] {a}A maquete encolhe em *três* direções ao mesmo tempo. [p=0.4] {b}No "
        "comprimento, [p=0.2] a caixa real é *vinte* vezes maior. [p=0.3] {c}Na largura também: [p=0.2] vinte vezes "
        "vinte, [p=0.2] *quatrocentas* caixinhas no fundo. [p=0.3] {d}E na altura: [p=0.2] vinte camadas. [p=0.4] "
        "{e}Vinte vezes vinte vezes vinte: [p=0.2] *oito mil* caixinhas da maquete [p=0.2] cabem na caixa real."),
    dict(id="13", block="maquete", text=
        "{t}E agora o passo que muita gente esquece. [p=0.3] {a}Cada caixinha guarda *cinco litros.* [p=0.4] {b}Cinco "
        "vezes oito mil: [p=0.2] *quarenta mil litros.* [p=0.4] {c}E como um metro cúbico são mil litros, [p=0.2] isso é "
        "*quarenta metros cúbicos.* [p=0.4] {d}Atalho: [p=0.2] capacidade real [p=0.2] é a da maquete [p=0.2] *vezes ene "
        "ao cubo.*"),
    dict(id="14", block="maquete_fachada", text=
        "{t}E na mesma maquete, [p=0.2] o que mais muda? [p=0.3] {a}As *alturas* [p=0.2] são medidas de comprimento: "
        "[p=0.2] ficam divididas por *vinte.* [p=0.4] {b}As áreas, [p=0.2] como a fachada, [p=0.2] ficam divididas por "
        "vinte ao quadrado: [p=0.2] *quatrocentos.* [p=0.4] {c}E o volume, [p=0.2] por *oito mil.* [p=0.3] Uma escala, "
        "[p=0.2] três fatores."),

    # ================= BLOCO F: REFERÊNCIAS RÁPIDAS =================
    dict(id="15", block="tabela", text=
        "{t}Dá para montar uma tabela inteira com uma regra só. [p=0.4] {a}Numa escala um para ene, [p=0.2] um centímetro "
        "vale ene centímetros, [p=0.2] e um centímetro quadrado vale *ene ao quadrado* centímetros quadrados. [p=0.4] "
        "{b}Em um para cinquenta: [p=0.2] meio metro de lado, [p=0.2] *zero vírgula vinte e cinco* metro quadrado. [p=0.3] "
        "{c}Em um para cem: [p=0.2] um metro, [p=0.2] *um* metro quadrado. [p=0.3] {d}Em um para mil: [p=0.2] dez metros, "
        "[p=0.2] *cem* metros quadrados. [p=0.3] {e}E num mapa um para cinquenta mil: [p=0.2] meio quilômetro de lado, "
        "[p=0.2] *vinte e cinco hectares.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Numa planta *um para cinquenta,* [p=0.2] um quarto mede *seis* por *oito* centímetros. "
        "[p=0.3] {b}Qual é a área real? [p=0.4] {c}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos conferir, [p=0.2] convertendo os lados primeiro. [p=0.3] {a}Em um para cinquenta, [p=0.2] cada "
        "centímetro é meio metro. [p=0.2] Seis centímetros: [p=0.2] *três metros.* [p=0.2] Oito centímetros: [p=0.2] "
        "*quatro metros.* [p=0.4] {b}Três vezes quatro: [p=0.2] *doze metros quadrados.* [p=0.4] {c}Um quarto de três por "
        "quatro. [p=0.2] Faz sentido!"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] comprimento usa ene; [p=0.2] área usa ene ao quadrado; "
        "[p=0.2] volume usa ene ao cubo. [p=0.5] {b}Dois: [p=0.2] em planta, converta os lados antes de calcular a área. "
        "[p=0.5] {c}Três: [p=0.2] em um para cem, [p=0.2] um centímetro é um metro."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] numa planta um para duzentos, [p=0.2] um "
        "centímetro quadrado [p=0.2] valeria *duzentos* centímetros quadrados. [p=0.4] {b}Parece certo, [p=0.2] porque a "
        "escala diz duzentos. [p=0.4] {c}Mas o duzentos é para *comprimento.* [p=0.2] A área cresce duzentos vezes "
        "duzentos: [p=0.2] quarenta mil centímetros quadrados, [p=0.2] *quatro metros quadrados.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] numa maquete um para vinte, [p=0.2] o volume real seria *vinte* vezes maior. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque é o número da escala. [p=0.4] {c}Mas a maquete encolhe em três direções: "
        "[p=0.2] vinte vezes vinte vezes vinte, [p=0.2] *oito mil.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] achar os *oito mil* [p=0.2] e responder oito mil litros. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o cubo da escala era justamente o difícil. [p=0.4] {c}Mas oito mil é quantas maquetes cabem. [p=0.2] "
        "Falta multiplicar pela *capacidade* da maquete."),
    dict(id="22", block="erros", text=
        "{a}Quarto: [p=0.2] não conferir o resultado. [p=0.2] Uma parede de *trinta e cinco metros* numa sala. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque a conta foi feita. [p=0.4] {c}Mas trinta e cinco metros é o comprimento de um "
        "prédio. [p=0.2] Em planta, [p=0.2] você *sabe* o tamanho de um cômodo: [p=0.2] use isso."),

    # ================= QUESTÃO 9 (AQUECIMENTO) =================
    dict(id="23", block="q9", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.3] Um aquecimento rápido. [p=0.4] "
        "{a}Na planta baixa de uma residência, [p=0.2] na escala *um para cinquenta,* [p=0.2] uma parede da sala tem *sete "
        "centímetros.* [p=0.3] {b}O comprimento real dessa parede é de: [p=0.4] {qa}A: [p=0.2] zero vírgula trinta e cinco "
        "metro. [p=0.3] {qb}B: [p=0.2] três vírgula cinco. [p=0.3] {qc}C: [p=0.2] sete. [p=0.3] {qd}D: [p=0.2] trinta e "
        "cinco. [p=0.3] {qe}E: [p=0.2] trezentos e cinquenta metros."),
    dict(id="24", block="q9", text=
        "{t}Sete vezes cinquenta: [p=0.2] *trezentos e cinquenta centímetros.* [p=0.3] {a}Dividindo por cem: [p=0.2] *três "
        "vírgula cinco metros.* [p=0.2] {ok}*Letra B!* [p=0.4] {b}Confira: [p=0.2] uma parede de sala com três metros e "
        "meio. [p=0.2] Faz sentido. [p=0.4] {xa}A A multiplicou por cinco, [p=0.2] e não por cinquenta: [p=0.2] trinta e "
        "cinco centímetros, [p=0.2] menos que um passo. [p=0.3] {xc}A C leu como se fosse um para cem. [p=0.3] {xd}A D "
        "dividiu por dez em vez de cem: [p=0.2] uma parede do tamanho de um prédio. [p=0.3] {xe}E a E chamou os "
        "centímetros de metros."),

    # ================= QUESTÃO 5 (EU FAÇO) =================
    dict(id="25", block="q5", text=
        "{t}A próxima, [p=0.2] eu faço com você. [p=0.3] {a}Numa planta baixa na escala *um para cem,* [p=0.2] uma sala "
        "aparece como um retângulo de *cinco* por *quatro* centímetros. [p=0.3] {b}A área real dessa sala é de: [p=0.4] "
        "{qa}A: [p=0.2] zero vírgula dois metro quadrado. [p=0.3] {qb}B: [p=0.2] dois. [p=0.3] {qc}C: [p=0.2] vinte. "
        "[p=0.3] {qd}D: [p=0.2] duzentos. [p=0.3] {qe}E: [p=0.2] dois mil metros quadrados."),
    dict(id="26", block="q5", text=
        "{t}Caminho um, [p=0.2] o seguro: [p=0.2] converta os lados. [p=0.3] {a}Em um para cem, [p=0.2] centímetro vira "
        "metro: [p=0.2] *cinco metros* por *quatro metros.* [p=0.3] {b}Cinco vezes quatro: [p=0.2] *vinte metros "
        "quadrados.* [p=0.2] {ok}*Letra C!* [p=0.4] {c}Caminho dois, [p=0.2] para comparar: [p=0.2] a área no papel é "
        "vinte centímetros quadrados. [p=0.2] Vezes cem ao quadrado, [p=0.2] dez mil: [p=0.2] duzentos mil centímetros "
        "quadrados. [p=0.3] {d}Dividindo por dez mil: [p=0.2] *vinte metros quadrados.* [p=0.2] Os dois batem, [p=0.2] "
        "mas o primeiro não deixa você esquecer o quadrado."),
    dict(id="27", block="q5", text=
        "{t}E as outras? [p=0.3] {xa}A A usou o fator de comprimento na área: [p=0.2] vinte vezes cem, [p=0.2] dois mil "
        "centímetros quadrados, [p=0.2] zero vírgula dois metro quadrado. [p=0.4] {xb}A B, [p=0.2] {xd}a D [p=0.2] {xe}e a "
        "E [p=0.2] acharam os duzentos mil centímetros quadrados, [p=0.2] mas dividiram pelo número errado: [p=0.2] por "
        "cem mil, [p=0.2] por mil [p=0.2] e por cem. [p=0.4] {c}De centímetro quadrado para metro quadrado, [p=0.2] é "
        "sempre *dez mil.*"),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="28", block="q6", text=
        "{t}Esta, [p=0.2] a gente faz junto. [p=0.3] {a}Em um projeto na escala *um para duzentos,* [p=0.2] cada "
        "centímetro quadrado do papel representa, [p=0.2] na realidade: [p=0.4] {qa}A: [p=0.2] zero vírgula zero dois "
        "metro quadrado. [p=0.3] {qb}B: [p=0.2] dois. [p=0.3] {qc}C: [p=0.2] quatro. [p=0.3] {qd}D: [p=0.2] vinte. "
        "[p=0.3] {qe}E: [p=0.2] quarenta metros quadrados. [p=0.4] {p}Pause e pense: [p=0.2] quanto mede o *lado* real do "
        "quadradinho? [p=1.5]"),
    dict(id="29", block="q6", text=
        "{t}O lado: [p=0.2] um centímetro vezes duzentos, [p=0.2] duzentos centímetros, [p=0.2] *dois metros.* [p=0.4] "
        "{a}Dois por dois: [p=0.2] *quatro metros quadrados.* [p=0.2] {ok}*Letra C!* [p=0.4] {b}Pelo fator: [p=0.2] "
        "duzentos ao quadrado, [p=0.2] quarenta mil centímetros quadrados, [p=0.2] quatro metros quadrados. [p=0.2] Bate. "
        "[p=0.4] {xa}A A é a armadilha: [p=0.2] o fator duzentos uma vez só, [p=0.2] duzentos centímetros quadrados. "
        "[p=0.3] {xb}A B converteu esses duzentos como se fosse comprimento, [p=0.2] dividindo por cem. [p=0.3] {xd}A D é "
        "grande demais: [p=0.2] vinte metros quadrados é uma sala inteira. [p=0.3] {xe}E a E dividiu por mil, [p=0.2] e "
        "não por dez mil."),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="30", block="q7", text=
        "{t}E a última, [p=0.2] *você faz,* [p=0.2] sem olhar para trás. [p=0.3] {a}Uma maquete na escala *um para "
        "vinte* [p=0.2] reproduz um reservatório de água. [p=0.2] A maquete comporta *cinco litros.* [p=0.3] {b}O "
        "reservatório real comporta: [p=0.4] {qa}A: [p=0.2] cem litros. [p=0.3] {qb}B: [p=0.2] dois mil. [p=0.3] "
        "{qc}C: [p=0.2] oito mil. [p=0.3] {qd}D: [p=0.2] quarenta mil. [p=0.3] {qe}E: [p=0.2] quatrocentos mil litros. "
        "[p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="31", block="q7", text=
        "{t}Capacidade é volume, [p=0.2] e volume tem três dimensões. [p=0.3] {a}Vinte ao cubo: [p=0.2] vinte vezes vinte "
        "vezes vinte, [p=0.2] *oito mil.* [p=0.3] {b}Vezes os cinco litros da maquete: [p=0.2] *quarenta mil litros.* "
        "[p=0.2] {ok}*Letra D!* [p=0.4] {c}Confira: [p=0.2] quarenta metros cúbicos, [p=0.2] uma caixa de uns quatro "
        "metros por quatro, [p=0.2] com dois e meio de altura. [p=0.2] Para um reservatório, [p=0.2] faz sentido."),
    dict(id="32", block="q7", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A usou o fator de comprimento: [p=0.2] cinco vezes vinte. [p=0.4] {xb}A B usou "
        "o fator de *área:* [p=0.2] cinco vezes quatrocentos. [p=0.4] {xc}A C achou os oito mil [p=0.2] e esqueceu os "
        "cinco litros. [p=0.4] {xe}E a E pôs um zero a mais."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] comprimento usa ene; [p=0.2] área usa ene ao "
        "quadrado; [p=0.2] volume usa ene ao cubo. [p=0.5] {b}Dois: [p=0.2] em planta, converta os lados antes de calcular "
        "a área. [p=0.5] {c}Três: [p=0.2] em um para cem, [p=0.2] um centímetro é um metro."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] {b}juntamos tudo, [p=0.2] {c}caçamos as pegadinhas [p=0.2] {d}e "
        "treinamos com questões de *Matemática* e *Geografia.*"),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantos metros quadrados tem o seu quarto? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
