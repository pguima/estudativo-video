# Estudativo · QUI-ORG-027 — Polímeros naturais, plásticos e reciclagem (Química · Química Orgânica · Polímeros).
# Habilidade: citar amido, celulose, proteína e borracha como polímeros naturais, diferenciar termoplástico de termofixo e
# dizer qual pode ser reciclado por fusão.
# Pré-requisitos: QUI-ORG-025, QUI-ORG-026. Próxima: QUI-ORG-028 (praticando polímeros).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.
# Fatos: amido e celulose = polímeros de glicose (condensação, sai água); o corpo humano digere amido e não digere celulose;
# proteína = cadeia de aminoácidos ligados por amidas (ligação peptídica); queratina do cabelo. Borracha natural = poli-isopreno,
# do látex da seringueira; vulcanização (Goodyear, 1839) = pontes de enxofre entre as cadeias. Termoplástico: PE, PP, PVC, PET,
# PS (amolecem e se remoldam). Termofixo: baquelite (cabo de panela, tomada), resinas; não amolecem, se decompõem.
# Códigos do triângulo de reciclagem (NBR 13230): 1 PET, 2 PEAD, 3 PVC, 4 PEBD, 5 PP, 6 PS, 7 outros.
# Questão inédita: garrafa PET × cabo de panela de baquelite.

TITULO = "Polímeros naturais, plásticos e reciclagem"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # gancho
    dict(id="s01", block="gancho", text="{a}O pão, a camiseta de algodão, o seu cabelo e o pneu do carro. [p=0.3] {b}Todos são feitos de polímeros, [p=0.2] e {c}nenhum saiu de uma fábrica de plástico: [p=0.2] {d}a natureza fabrica os dela."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}citar os polímeros naturais, [p=0.2] {c}separar termoplástico de termofixo [p=0.2] e {d}dizer qual plástico se recicla derretendo. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre das duas últimas aulas. [p=0.2] {a}No polímero de adição, a dupla do monômero abre e nada sai. [p=0.2] {b}No de condensação, cada ligação solta uma molécula pequena, como a água."),
    # naturais
    dict(id="s04", block="natural", text="{a}O amido, do pão, do arroz e da batata, [p=0.2] {b}é uma cadeia de glicose, um açúcar. [p=0.3] {c}A celulose, do algodão, do papel e da madeira, [p=0.2] {d}também é feita de glicose, mas ligada de outro jeito. [p=0.3] {e}Por isso, o corpo humano digere o amido e não digere a celulose."),
    dict(id="s05", block="natural", text="{a}Nos dois, cada glicose que entra na cadeia solta uma água: [p=0.2] {b}são polímeros de condensação."),
    dict(id="s06", block="natural", text="{a}A proteína, como a do cabelo e da carne, [p=0.2] {b}é uma cadeia de aminoácidos, moléculas com um grupo ácido e um grupo amina. [p=0.3] {c}Eles se ligam por amidas, soltando água: [p=0.2] {d}a proteína é uma poliamida natural."),
    dict(id="s07", block="natural", text="{a}E a borracha natural vem do látex da seringueira. [p=0.2] {b}É um polímero de adição de um monômero com duas duplas, o isopreno. [p=0.3] Como o isopreno tem duas duplas, uma delas sobra em cada unidade da cadeia. [p=0.2] {c}Crua, a borracha fica mole no calor. [p=0.2] {d}Aquecida com enxofre, ganha pontes de enxofre entre as cadeias: [p=0.2] {e}é a vulcanização, que faz o pneu."),
    # termoplástico e termofixo
    dict(id="s08", block="termo", text="Agora, os plásticos. [p=0.2] {a}No termoplástico, as cadeias são fios soltos, como espaguete, [p=0.2] presos uns aos outros só por atrações fracas. [p=0.3] {b}No calor, os fios escorregam, [p=0.2] {c}o plástico amolece {d}e pode ganhar outra forma. [p=0.3] {e}Polietileno, polipropileno, pê vê cê, PET e poliestireno são termoplásticos."),
    dict(id="s09", block="termo", text="{a}No termofixo, as cadeias estão amarradas umas às outras por ligações fortes, [p=0.2] {b}como uma rede de pesca. [p=0.3] {c}No calor, a rede não escorrega: [p=0.2] {d}o plástico não amolece, e, se esquentar demais, queima. [p=0.3] {e}É o caso da baquelite, dos cabos de panela e das tomadas."),
    # reciclagem
    dict(id="s10", block="recicla", text="Daí vem a reciclagem por fusão: [p=0.2] {a}o termoplástico é derretido e moldado de novo, [p=0.2] {b}e o termofixo não. [p=0.3] {c}Para ajudar na separação, as embalagens trazem um triângulo com um número: [p=0.2] {d}número um é o PET, [p=0.1] {e}número três é o pê vê cê, [p=0.1] {f}número seis é o poliestireno."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}achar que todo plástico se recicla derretendo. [p=0.3] {b}O termofixo não derrete: [p=0.2] {c}ele só pode ser moído e usado como enchimento de outros materiais, ou queimado para gerar energia."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.2] {a}pergunte se as cadeias estão soltas ou amarradas. [p=0.3] {b}Soltas, como espaguete: [p=0.1] amolece, é termoplástico, recicla por fusão. [p=0.3] {c}Amarradas, como rede: [p=0.1] não amolece, é termofixo, não recicla por fusão. [p=0.3] {d}A borracha vulcanizada também é amarrada, pelas pontes de enxofre: [p=0.2] por isso o pneu não derrete."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Numa cooperativa chegam uma garrafa PET [p=0.2] {b}e um cabo de panela de baquelite. [p=0.3] {c}Qual pode ser derretido e virar outro objeto? [p=0.2] {d}E por quê?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="{a}O PET tem cadeias soltas: [p=0.1] é termoplástico. [p=0.2] {b}No calor, amolece, e pode virar fibra, tecido ou outra garrafa. [p=0.3] {c}A baquelite tem cadeias amarradas em rede: [p=0.1] é termofixo. [p=0.2] {d}Não amolece, e não se recicla por fusão."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}amido, celulose, proteína e borracha são polímeros naturais. [p=0.2] {b}Termoplástico tem cadeias soltas e recicla por fusão. [p=0.2] {c}Termofixo tem cadeias amarradas e não recicla por fusão."),
    dict(id="s17", block="fim", text="Na próxima aula, você vai praticar {a}monômeros, tipos de polímero e o destino dos plásticos [p=0.2] em {b}questões de prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
