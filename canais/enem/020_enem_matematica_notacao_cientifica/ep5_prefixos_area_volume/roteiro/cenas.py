# Roteiro — Notação Científica e Ordem de Grandeza, Episódio 5 de 6: Prefixos (de tera a pico) e a armadilha da
# conversão de área e volume (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/05-notacao-cientifica-ordem-grandeza.html — seção 07 (+ Questão 6 da seção 12).
# Fora do recorte (série de Unidades e Conversões): escala de conversão, unidades compostas, análise dimensional.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   PREFIXO = uma potência de 10 com APELIDO: quilo = 10³, mega = 10⁶, nano = 10⁻⁹.
#   ÁREA = GRADE de quadradinhos: 1 m² tem 100 quadradinhos de 1 cm numa fileira… mas são 100 FILEIRAS: 100 × 100 = 10 000.
#   VOLUME = CUBO DE CUBINHOS: 100 × 100 × 100 = 1 000 000.
# Prefixos (tabela da seção 07): tera T 10¹² · giga G 10⁹ · mega M 10⁶ · quilo k 10³ · deci d 10⁻¹ · centi c 10⁻² ·
#   mili m 10⁻³ · micro μ 10⁻⁶ · nano n 10⁻⁹ · pico p 10⁻¹².
# Fatores: 1 m = 10² cm → 1 m² = 10⁴ cm² → 1 m³ = 10⁶ cm³ · 1 km = 10³ m → 1 km² = 10⁶ m² → 1 km³ = 10⁹ m³.
# Equivalências: 1 L = 1 dm³ · 1 mL = 1 cm³ · 1 m³ = 1 000 L · 1 hectare = 10⁴ m² (quadrado de 100 m de lado) · 1 km² = 100 hectares.
# Nós fazemos: 3 m² = 3 · 10⁴ cm² · 2 m³ = 2 000 L.
# QUESTÃO 6 do material (texto idêntico na tela): 2,5 · 10³ m² em cm² → 2,5 · 10³ · 10⁴ = 2,5 · 10⁷ → C.
#   A (2,5 · 10⁵): usou 10² em vez de 10⁴ (explicação do material).
#   Explicações NOSSAS (o material só explica a A): B (2,5 · 10⁶) usou o fator 10³, como se o centímetro fosse o
#   milímetro (confundiu centi com mili); D (2,5 · 10⁹) elevou o fator ao CUBO, como se fosse volume;
#   E (2,5 · 10¹) dividiu por 10² em vez de multiplicar (andou para o lado errado: centímetro quadrado é menor, então
#   o número tem que CRESCER).
# Os exemplos dos blocos NÃO usam os números da Questão 6 (piso de 1 m², 3 m², 1 km²).
# Frases-chave (meio e fim, idênticas):
#   1. Prefixo é potência de 10 com apelido.
#   2. Área: o fator vai ao quadrado. Volume: ao cubo.
#   3. 1 m³ são 1 000 litros.
# Atalhos (verde): "os grandes andam de 3 em 3: quilo 3, mega 6, giga 9, tera 12" · "os pequenos, a partir do mili, também:
#   mili −3, micro −6, nano −9, pico −12" · "área: dobre o expoente do fator; volume: triplique" ·
#   "unidade menor → número maior" · "1 litro = um cubo de 10 cm; 1 mL = um cubinho de 1 cm".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "1 m² NÃO são 100 cm²: prefixos e a armadilha de área e volume | Notação Científica Ep. 5"
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
        "{a}Um metro quadrado [p=0.2] tem quantos *centímetros quadrados?* [p=0.6] {b}Se você disse *cem,* [p=0.3] "
        "{c}você errou [p=0.2] por um fator de *cem.* [p=0.5] {d}Este é um dos erros *mais caros* [p=0.2] da prova inteira."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber os prefixos, [p=0.2] *de tera a pico,* [p=0.3] {b}e converter "
        "*área* e *volume* [p=0.2] sem cair na armadilha. [p=0.4] {c}E sem decorar tabela: [p=0.2] contando quadradinhos."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Potência de potência: [p=0.2] dez ao quadrado, [p=0.2] tudo ao "
        "quadrado, [p=0.2] é dez ao quadrado vezes dez ao quadrado. [p=0.3] {b}Os expoentes se *multiplicam:* [p=0.2] "
        "dois vezes dois, [p=0.2] *dez elevado a quatro.* [p=0.4] {c}E multiplicar em notação científica: [p=0.2] "
        "número com número, [p=0.2] e os expoentes do dez *somam.* [p=0.3] {d}Três vezes dez ao quadrado, [p=0.2] vezes "
        "dez ao cubo, [p=0.2] dá *três vezes dez elevado a cinco.*"),

    # ================= BLOCO A: PREFIXOS GRANDES =================
    dict(id="04", block="grandes", text=
        "{t}O que têm em comum [p=0.2] o *gigabyte* do seu celular, [p=0.2] o *quilômetro* da estrada [p=0.2] e o "
        "*miligrama* do remédio? [p=0.5] {a}Todos começam com um *prefixo:* [p=0.2] um pedacinho colado na frente da "
        "unidade. [p=0.4] {b}E cada prefixo é uma *potência de dez com apelido.*"),
    dict(id="05", block="grandes", text=
        "{t}Os grandes. [p=0.3] {a}*Quilo* é dez ao cubo, [p=0.2] mil: [p=0.2] um quilômetro são mil metros. [p=0.4] "
        "{b}*Mega* é dez elevado a seis, [p=0.2] um milhão: [p=0.2] o megawatt de uma usina. [p=0.4] {c}*Giga* é dez "
        "elevado a nove, [p=0.2] um bilhão: [p=0.2] o gigabyte do celular. [p=0.4] {d}E *tera* é dez elevado a doze: "
        "[p=0.2] o terabyte de um HD."),
    dict(id="06", block="grandes", text=
        "{t}Repare no atalho: [p=0.3] {a}os grandes andam de *três em três.* [p=0.3] {b}Quilo, três. [p=0.2] Mega, seis. "
        "[p=0.2] Giga, nove. [p=0.2] Tera, doze. [p=0.4] {c}Cada degrau da escada [p=0.2] multiplica por *mil.*"),

    # ================= BLOCO B: PREFIXOS PEQUENOS =================
    dict(id="07", block="pequenos", text=
        "{t}E os pequenos? [p=0.3] Eles têm expoente *negativo:* [p=0.2] dividem em vez de multiplicar. [p=0.4] {a}*Deci* "
        "é dez elevado a menos um: [p=0.2] um décimo. [p=0.3] {b}*Centi* é dez elevado a menos dois: [p=0.2] um centésimo. "
        "[p=0.2] Cabem cem centímetros num metro. [p=0.4] {c}E *mili* é dez elevado a menos três: [p=0.2] o miligrama do "
        "remédio, [p=0.2] o mililitro da seringa."),
    dict(id="08", block="pequenos", text=
        "{t}Descendo mais. [p=0.3] {a}*Micro* é dez elevado a menos seis, [p=0.2] e o símbolo é essa letra grega, [p=0.2] "
        "o *mi:* [p=0.2] o micrograma de poluente no ar. [p=0.4] {b}*Nano* é dez elevado a menos nove: [p=0.2] o "
        "nanômetro, [p=0.2] a escala de um vírus. [p=0.4] {c}E *pico* é dez elevado a menos doze: [p=0.2] o picossegundo."),
    dict(id="09", block="pequenos", text=
        "{t}O atalho aqui é o espelho do outro. [p=0.3] {a}A partir do mili, [p=0.2] também de *três em três:* [p=0.3] "
        "{b}mili, menos três. [p=0.2] Micro, menos seis. [p=0.2] Nano, menos nove. [p=0.2] Pico, menos doze. [p=0.4] "
        "{c}Só o deci e o centi, [p=0.2] os vizinhos do metro, [p=0.2] fogem da regra: [p=0.2] menos um e menos dois."),

    # ================= BLOCO C: A ARMADILHA DA ÁREA =================
    dict(id="10", block="area", text=
        "{t}Agora, a armadilha. [p=0.3] Imagine um piso coberto de azulejos. [p=0.4] {a}*Área* é o quanto de chão uma "
        "figura cobre, [p=0.2] medido em *quadradinhos.* [p=0.4] {b}Um *metro quadrado* [p=0.2] é a área de um quadrado "
        "com um metro de lado. [p=0.4] {c}E um *centímetro quadrado* [p=0.2] é um quadradinho de um centímetro de lado, "
        "[p=0.2] do tamanho de uma unha."),
    dict(id="11", block="area", text=
        "{t}Quantos quadradinhos de um centímetro [p=0.2] cabem no quadrado de um metro? [p=0.4] {a}Um metro tem *cem* "
        "centímetros. [p=0.2] Então a primeira fileira tem *cem* quadradinhos. [p=0.4] {b}E é aqui que quase todo mundo "
        "para. [p=0.4] {c}Mas o quadrado não tem uma fileira só: [p=0.2] tem *cem fileiras!* [p=0.4] {d}Cem vezes cem: "
        "[p=0.2] *dez mil* quadradinhos."),
    dict(id="12", block="area", text=
        "{t}Por isso, [p=0.2] *um metro quadrado [p=0.2] é dez elevado a quatro centímetros quadrados.* [p=0.4] {a}O metro "
        "vira dez ao quadrado centímetros, [p=0.2] e na área esse fator vai *ao quadrado:* [p=0.3] {b}dez ao quadrado, "
        "[p=0.2] ao quadrado, [p=0.2] dez elevado a quatro. [p=0.4] {c}Atalho: [p=0.2] em área, [p=0.2] *dobre* o "
        "expoente do fator."),

    # ================= BLOCO D: A ARMADILHA DO VOLUME =================
    dict(id="13", block="volume", text=
        "{t}E o volume? [p=0.3] Pense numa caixa d'água. [p=0.4] {a}*Volume* é o espaço que uma coisa ocupa, [p=0.2] "
        "medido em *cubinhos.* [p=0.4] {b}Um *metro cúbico* é um cubo de um metro de lado. [p=0.3] {c}Um *centímetro "
        "cúbico* [p=0.2] é um cubinho de um centímetro, [p=0.2] do tamanho de um dado pequeno."),
    dict(id="14", block="volume", text=
        "{t}Vamos encher o cubo grande de cubinhos. [p=0.4] {a}Uma fileira: [p=0.2] *cem.* [p=0.3] {b}Cem fileiras "
        "formam uma camada: [p=0.2] *dez mil.* [p=0.4] {c}E o cubo tem *cem camadas,* [p=0.2] uma em cima da outra. "
        "[p=0.4] {d}Cem vezes cem vezes cem: [p=0.2] *um milhão* de cubinhos. [p=0.4] {e}Um metro cúbico [p=0.2] é *dez "
        "elevado a seis* centímetros cúbicos."),
    dict(id="15", block="volume", text=
        "{t}É a mesma ideia, [p=0.2] com um degrau a mais. [p=0.4] {a}No volume, [p=0.2] o fator vai *ao cubo:* [p=0.2] "
        "dez ao quadrado, [p=0.2] ao cubo, [p=0.2] dez elevado a seis. [p=0.4] {b}Atalho: [p=0.2] comprimento, [p=0.2] "
        "expoente normal. [p=0.2] Área, [p=0.2] *dobra.* [p=0.2] Volume, [p=0.2] *triplica.* [p=0.4] {c}E confira o "
        "sentido: [p=0.2] a unidade ficou *menor,* [p=0.2] então o número tem que ficar *maior.*"),

    # ================= BLOCO E: O MESMO COM QUILÔMETRO =================
    dict(id="16", block="km", text=
        "{t}E funciona com qualquer prefixo. [p=0.3] {a}Um quilômetro são *dez ao cubo* metros. [p=0.4] {b}Então um "
        "quilômetro quadrado [p=0.2] é dez ao cubo, ao quadrado: [p=0.2] *dez elevado a seis* metros quadrados. [p=0.4] "
        "{c}E um quilômetro cúbico [p=0.2] é dez ao cubo, ao cubo: [p=0.2] *dez elevado a nove* metros cúbicos."),

    # ================= BLOCO F: AS EQUIVALÊNCIAS QUE CAEM SEMPRE =================
    dict(id="17", block="equiv", text=
        "{t}Agora, as equivalências que caem sempre. [p=0.4] {a}*Capacidade* é o quanto cabe dentro de um recipiente, "
        "[p=0.2] e a unidade dela é o *litro.* [p=0.4] {b}Um litro [p=0.2] é exatamente um *decímetro cúbico:* [p=0.2] "
        "um cubo de dez centímetros de lado. [p=0.4] {c}E um mililitro [p=0.2] é um *centímetro cúbico:* [p=0.2] aquele "
        "dado pequeno."),
    dict(id="18", block="equiv", text=
        "{t}E a mais importante: [p=0.3] {a}*um metro cúbico são mil litros.* [p=0.4] {b}Por quê? [p=0.2] Um metro tem dez "
        "decímetros, [p=0.2] e no volume o fator vai ao cubo: [p=0.2] dez vezes dez vezes dez, [p=0.2] *mil* decímetros "
        "cúbicos. [p=0.3] {c}Mil litros. [p=0.4] {d}É a caixa d'água de mil litros, [p=0.2] que você vê no telhado das casas."),
    dict(id="19", block="equiv", text=
        "{t}E no campo, [p=0.2] a área se mede em *hectare.* [p=0.4] {a}Um hectare [p=0.2] é a área de um quadrado de *cem "
        "metros* de lado: [p=0.2] cem vezes cem, [p=0.2] *dez elevado a quatro* metros quadrados. [p=0.4] {b}E um "
        "quilômetro quadrado, [p=0.2] que é dez elevado a seis metros quadrados, [p=0.2] tem *cem hectares.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="20", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Duas conversões. [p=0.3] {a}Três metros quadrados, [p=0.2] em centímetros quadrados. [p=0.3] "
        "{b}E dois metros cúbicos, [p=0.2] em litros. [p=0.4] {c}*Pause o vídeo e converta.* [p=2.0]"),
    dict(id="21", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Cada metro quadrado tem dez elevado a quatro centímetros quadrados. [p=0.2] Três "
        "deles: [p=0.2] *três vezes dez elevado a quatro.* [p=0.2] Trinta mil. [p=0.4] {b}E cada metro cúbico tem mil "
        "litros. [p=0.2] Dois deles: [p=0.2] *dois mil litros.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="22", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] prefixo é potência de dez com apelido. [p=0.5] {b}Dois: "
        "[p=0.2] área: [p=0.2] o fator vai ao quadrado. [p=0.2] Volume: [p=0.2] ao cubo. [p=0.5] {c}Três: [p=0.2] um metro "
        "cúbico são mil litros."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="23", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] um metro quadrado igual a *cem* centímetros "
        "quadrados. [p=0.4] {b}Parece certo, [p=0.2] porque um metro tem cem centímetros. [p=0.4] {c}Mas isso é uma fileira "
        "só. [p=0.2] São cem fileiras: [p=0.2] *dez mil.*"),
    dict(id="24", block="erros", text=
        "{a}Segundo: [p=0.2] um metro cúbico igual a *cem,* [p=0.2] ou *dez mil* centímetros cúbicos. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque são os números que a gente já viu. [p=0.4] {c}Mas o cubo tem *três* direções: [p=0.2] cem "
        "vezes cem vezes cem, [p=0.2] *um milhão.*"),
    dict(id="25", block="erros", text=
        "{a}Terceiro: [p=0.2] confundir *mili* com *micro.* [p=0.4] {b}Parece certo, [p=0.2] porque os dois começam com "
        "*m* [p=0.2] e os dois são pequenos. [p=0.4] {c}Mas mili é dez elevado a menos três, [p=0.2] e micro, [p=0.2] dez "
        "elevado a menos seis: [p=0.2] *mil vezes* menor."),

    # ================= QUESTÃO 6 DO MATERIAL =================
    dict(id="26", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Um terreno retangular "
        "tem área de [p=0.2] dois vírgula cinco vezes dez ao cubo [p=0.2] metros quadrados. [p=0.3] Essa área, [p=0.2] "
        "expressa em centímetros quadrados, [p=0.2] corresponde a: [p=0.4] {qa}A: [p=0.2] dois vírgula cinco vezes dez "
        "elevado a cinco. [p=0.3] {qb}B: [p=0.2] dois vírgula cinco vezes dez elevado a seis. [p=0.3] {qc}C: [p=0.2] dois "
        "vírgula cinco vezes dez elevado a sete. [p=0.3] {qd}D: [p=0.2] dois vírgula cinco vezes dez elevado a nove. "
        "[p=0.3] {qe}E: [p=0.2] dois vírgula cinco vezes dez elevado a um. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="questao", text=
        "{t}Vamos resolver. [p=0.3] {a}É área, [p=0.2] então o fator vai ao quadrado: [p=0.2] um metro são dez ao quadrado "
        "centímetros, [p=0.2] e um metro quadrado são *dez elevado a quatro* centímetros quadrados. [p=0.4] {b}Agora, "
        "multiplicar: [p=0.2] dois vírgula cinco vezes dez ao cubo, [p=0.2] vezes dez elevado a quatro. [p=0.3] {c}Os "
        "expoentes somam: [p=0.2] três mais quatro, [p=0.2] *sete.* [p=0.3] {d}Dois vírgula cinco vezes dez elevado a "
        "sete. [p=0.3] {ok}*Letra C!*"),
    dict(id="28", block="questao", text=
        "{t}E as outras? [p=0.3] {xa}A A é a armadilha da aula: [p=0.2] usou dez ao quadrado [p=0.2] em vez de dez "
        "elevado a quatro. [p=0.2] Errou por um fator de cem. [p=0.4] {xb}A B usou dez ao cubo, [p=0.2] como se fosse "
        "milímetro: [p=0.2] confundiu centi com mili. [p=0.4] {xd}A D elevou o fator ao *cubo,* [p=0.2] como se fosse "
        "volume. [p=0.4] {xe}E a E dividiu em vez de multiplicar: [p=0.2] mas a unidade ficou menor, [p=0.2] então o "
        "número tinha que *crescer.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] prefixo é potência de dez com apelido. [p=0.5] "
        "{b}Dois: [p=0.2] área: [p=0.2] o fator vai ao quadrado. [p=0.2] Volume: [p=0.2] ao cubo. [p=0.5] {c}Três: "
        "[p=0.2] um metro cúbico são mil litros."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] a gente junta tudo, [p=0.3] {b}caça as pegadinhas [p=0.3] {c}e "
        "treina com questões de *Matemática,* [p=0.2] *Física,* [p=0.2] *Química* [p=0.2] e *Biologia.*"),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também achava que um metro quadrado tinha cem centímetros quadrados? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
