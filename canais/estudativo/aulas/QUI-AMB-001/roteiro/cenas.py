# Estudativo · QUI-AMB-001 — Combustíveis fósseis e biocombustíveis (Química · Química e Ambiente · Combustíveis, poluição e chuva ácida).
# Habilidade: comparar gasolina, etanol e biodiesel em energia por grama e CO₂ liberado, explicar a octanagem e dizer que a
# planta retira CO₂ do ar ao crescer e por isso o biocombustível fecha parte do ciclo do carbono (fotossíntese vem depois).
# Pré-requisitos: QUI-MIS-008, QUI-CAL-005, QUI-TER-001, QUI-ORG-004, QUI-ORG-023. Próxima: QUI-AMB-002.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos (entalpias de combustão de referência, água líquida): octano C₈H₁₈ −5 471 kJ/mol, 114 g/mol → 48,0 kJ/g;
# etanol C₂H₆O −1 368 kJ/mol, 46 g/mol → 29,7 kJ/g (arredondado para 30); biodiesel (ésteres metílicos de soja) cerca de
# 40 kJ/g. CO₂: 46 g de etanol → 88 g (1,9 g por grama); 114 g de octano → 352 g (3,1 g por grama); por energia, os dois
# dão cerca de 64 g de CO₂ por MJ. Octanagem: heptano = 0, isoctano (2,2,4-trimetilpentano) = 100; mede resistência à
# detonação, não energia. Gasolina brasileira com cerca de 30% de etanol anidro desde 2025 (lei; muda com o tempo).
# Fração de oxigênio na massa: etanol 16/46 ≈ 35%; oleato de metila (biodiesel) 32/296 ≈ 11%; octano 0.
# Regra prática dos 70% (etanol compensa até cerca de 70% do preço da gasolina).

TITULO = "Combustíveis fósseis e biocombustíveis"

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
    dict(id="s01", block="gancho", text="{a}Com um litro de etanol, o carro anda menos do que com um litro de gasolina. [p=0.3] {b}E o etanol também solta gás carbônico quando queima. [p=0.3] {c}Mesmo assim, ele é chamado de combustível renovável. [p=0.3] {d}As três frases são verdade."),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai comparar {b}gasolina, etanol e biodiesel [p=0.1] em energia e em gás carbônico, [p=0.2] {c}entender o que é octanagem [p=0.2] e {d}descobrir de onde vem o renovável."),
    # lembrete
    dict(id="s03", block="lembrete", text="Três lembretes. [p=0.2] {a}A gasolina sai do petróleo, na destilação fracionada. [p=0.3] {b}A queima é exotérmica: libera energia, e o delta agá é negativo. [p=0.3] {c}E, pela estequiometria, quarenta e seis gramas de etanol queimados liberam oitenta e oito gramas de cê ó dois."),
    # fóssil × bio
    dict(id="s04", block="origem", text="{a}Combustível fóssil vem de restos de seres vivos que ficaram enterrados por milhões de anos: [p=0.1] {b}petróleo, gás natural e carvão. [p=0.3] {c}Biocombustível vem de plantas e gorduras de hoje: [p=0.1] {d}o etanol da cana [p=0.1] {e}e o biodiesel, feito de óleo de soja ou de sebo."),
    # energia
    dict(id="s05", block="energia", text="Quanta energia sai de cada grama? [p=0.3] {a}O octano, da gasolina, libera cerca de quarenta e oito quilojoules por grama. [p=0.2] {b}O biodiesel, cerca de quarenta. [p=0.2] {c}O etanol, perto de trinta."),
    dict(id="s06", block="energia", text="Por que o etanol perde? [p=0.2] {a}Compare as fórmulas. [p=0.2] {b}O octano, da gasolina, é só carbono e hidrogênio. [p=0.3] {c}O etanol já tem um oxigênio na molécula: [p=0.1] {d}ele chega ao motor meio queimado. [p=0.3] {e}O biodiesel também tem oxigênio, mas pouco, numa molécula bem comprida."),
    dict(id="s07", block="energia", text="É por isso que {a}o carro roda menos quilômetros com um litro de etanol: [p=0.1] por litro, o etanol também perde. [p=0.3] {b}E vem daí a regra do posto: [p=0.1] {c}o etanol só compensa se custar até uns setenta por cento do preço da gasolina."),
    # CO2
    dict(id="s08", block="co2", text="E o gás carbônico? [p=0.2] {a}Quarenta e seis gramas de etanol liberam oitenta e oito gramas de cê ó dois: [p=0.1] {b}quase dois gramas de gás para cada grama queimado. [p=0.3] {c}Um mol de octano, cento e catorze gramas, libera oito mols de cê ó dois: [p=0.1] {d}trezentos e cinquenta e dois gramas. [p=0.2] Passa de três gramas por grama."),
    dict(id="s09", block="co2", text="{a}Por grama, a gasolina solta mais gás carbônico, [p=0.1] {b}mas também dá mais energia. [p=0.3] {c}Para a mesma energia, os dois soltam quase o mesmo cê ó dois. [p=0.3] {d}A diferença não está no escapamento. [p=0.2] {e}Está na origem do carbono."),
    # ciclo do carbono
    dict(id="s10", block="ciclo", text="{a}Enquanto a cana cresce, ela retira cê ó dois do ar para formar o próprio corpo. [p=0.3] Como a planta faz isso é a fotossíntese, {b}assunto de outra aula, na Biologia. [p=0.3] {c}Quando o etanol queima, esse carbono volta para o ar. [p=0.2] {d}E a próxima safra o retira de novo."),
    dict(id="s11", block="ciclo", text="{a}O carbono do petróleo estava fora do ar havia milhões de anos, debaixo da terra. [p=0.3] {b}Queimado, ele é cê ó dois novo, que se soma ao que já estava no ar. [p=0.3] É isso que quer dizer renovável: {c}o biocombustível fecha o ciclo do carbono."),
    dict(id="s12", block="ciclo", text="{a}Mas só fecha em parte. [p=0.2] {b}Plantar, adubar, colher, transportar e destilar gastam energia, [p=0.1] e quase sempre essa energia vem de combustível fóssil. [p=0.3] {c}Renovável não quer dizer emissão zero."),
    # octanagem
    dict(id="s13", block="octanagem", text="Falta a octanagem. [p=0.2] {a}No motor, a mistura de combustível e ar é espremida pelo pistão antes da faísca. [p=0.3] {b}Se ela explodir sozinha, antes da hora, o motor bate e perde força. [p=0.3] {c}A octanagem mede quanto o combustível aguenta ser espremido sem explodir antes da hora."),
    dict(id="s14", block="octanagem", text="A escala tem dois padrões. [p=0.2] {a}O heptano, de cadeia reta, explode fácil: vale zero. [p=0.3] {b}O isoctano, dois, dois, quatro trimetilpentano, todo ramificado, aguenta muito: vale cem. [p=0.3] {c}Ramificação resiste; cadeia reta detona."),
    dict(id="s15", block="octanagem", text="{a}O etanol tem octanagem alta. [p=0.2] {b}Esse é um dos motivos para a gasolina vendida no Brasil levar etanol misturado, [p=0.1] {c}perto de trinta por cento desde dois mil e vinte e cinco."),
    # erro
    dict(id="s16", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que octanagem mede a energia do combustível. [p=0.3] {b}Não mede. [p=0.2] {c}O etanol tem octanagem maior que a da gasolina e, mesmo assim, libera bem menos energia por grama. [p=0.3] {d}Octanagem é resistência a ser espremido, não força."),
    # atalho
    dict(id="s17", block="atalho", text="O atalho de prova para comparar energia: [p=0.1] {a}olhe quanto da massa é oxigênio. [p=0.3] {b}Quanto maior essa parte, menos energia por grama. [p=0.2] {c}No etanol, mais de um terço da massa é oxigênio; no biodiesel, só um décimo; no octano, nada. [p=0.3] Funciona porque {d}o oxigênio já está ligado: [p=0.1] aquela parte da molécula já foi queimada."),
    dict(id="s18", block="atalho", text="{a}Não compensa quando a questão compara por mol ou por litro. [p=0.2] {b}Aí, a ordem pode mudar, e você usa os números da própria questão."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] {a}Use quarenta e oito quilojoules por grama para a gasolina e trinta para o etanol. [p=0.3] {b}Quantos gramas de cada um liberam mil e duzentos quilojoules? [p=0.3] {c}E o que explica a diferença?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s21", block="resposta", text="{a}Gasolina: mil e duzentos dividido por quarenta e oito [p=0.1] {b}dá vinte e cinco gramas. [p=0.3] {c}Etanol: mil e duzentos dividido por trinta [p=0.1] {d}dá quarenta gramas."),
    dict(id="s22", block="resposta", text="{a}Para a mesma energia, você queima bem mais etanol: quinze gramas a mais. [p=0.3] {b}O motivo é o oxigênio que ele já traz na molécula. [p=0.3] {c}Quem multiplicou, em vez de dividir, chegou a números enormes, sem sentido."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: [p=0.1] {a}a gasolina dá mais energia por grama; [p=0.2] {b}todos soltam gás carbônico; [p=0.2] {c}o biocombustível é renovável porque a planta retira esse carbono do ar; [p=0.2] e {d}octanagem é resistência, não energia."),
    dict(id="s24", block="fim", text="Na próxima aula, você vai atrás do que mais sai do escapamento e das chaminés: [p=0.2] {a}os poluentes do ar e a chuva ácida. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
