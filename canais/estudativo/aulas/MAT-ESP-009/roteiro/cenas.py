# Estudativo · MAT-ESP-009 — Encher um recipiente: nível, vazão e tempo (Matemática · Geometria Espacial · Prismas e cilindros).
# Habilidade: descobrir quanto o nível sobe e em quanto tempo uma caixa enche, ligando volume, altura e vazão.
# Pré-requisitos: MAT-ESP-008 (cilindro, πr²·h), MAT-RAZ-018 (tempo = volume ÷ vazão). Usa MAT-ESP-007 (volume = área da base · altura), MAT-MED-005 (1 dm³ = 1 L; 1 m³ = 1.000 L), MAT-MED-006 (minutos em horas). Próxima: MAT-ESP-010.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Só recipientes de paredes retas (prisma e cilindro em pé).

TITULO = "Encher um recipiente: nível, vazão e tempo"

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
    dict(id="s01", block="gancho", text="{a}Um aquário com fundo de sessenta por trinta centímetros. [p=0.2] Você despeja {b}um balde de nove litros. [p=0.3] {c}Quanto o nível da água sobe? [p=0.3] A resposta é {d}cinco centímetros, [p=0.2] e sai de uma divisão só."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você descobre quanto o nível sobe [p=0.2] e em quanto tempo um recipiente enche, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}o volume do prisma e do cilindro é a área da base vezes a altura; [p=0.2] {c}um decímetro cúbico é um litro, e um metro cúbico guarda mil litros; [p=0.2] e {d}o tempo é o volume dividido pela vazão. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="camada", text="Quando a água entra, ela forma {a}uma camada no fundo, [p=0.2] com {b}a forma do fundo. [p=0.3] Essa camada é um prisma, ou um cilindro se o fundo for redondo: [p=0.2] {c}o volume dela é a área do fundo vezes a altura. [p=0.3] Só que agora {d}o volume é conhecido, [p=0.2] e {e}a altura é o que falta."),
    dict(id="s05", block="camada", text="Então, isolando a altura: [p=0.2] {a}o quanto o nível sobe é o volume dividido pela área do fundo. [p=0.3] Mas, antes de dividir, {b}tudo na mesma unidade."),
    # aquário
    dict(id="s06", block="aquario", text="No aquário, use o atalho do bloco: {a}tudo em decímetros, porque o litro é um decímetro cúbico. [p=0.2] {b}Sessenta centímetros são seis decímetros. [p=0.2] {c}Trinta centímetros são três. [p=0.2] {d}Seis vezes três dá dezoito decímetros quadrados de fundo."),
    dict(id="s07", block="aquario", text="{a}Nove litros são nove decímetros cúbicos. [p=0.2] {b}Nove dividido por dezoito dá zero vírgula cinco decímetro. [p=0.3] {c}Meio decímetro são cinco centímetros: [p=0.2] o nível sobe cinco centímetros."),
    # tempo para encher
    dict(id="s08", block="caixa", text="Agora o tempo. [p=0.2] Lembra da caixa-d'água com {a}fundo de dois metros por um metro e meio [p=0.2] e {b}um metro de altura? [p=0.2] Uma torneira solta {c}vinte e cinco litros por minuto. [p=0.3] {d}Em quanto tempo a caixa vazia enche?"),
    dict(id="s09", block="caixa", text="{a}Dois vezes um vírgula cinco dá três metros quadrados de fundo, [p=0.2] e {b}vezes um metro de altura dá três metros cúbicos: [p=0.2] {c}três mil litros. [p=0.3] Tempo é volume dividido pela vazão: [p=0.2] {d}três mil dividido por vinte e cinco dá cento e vinte minutos, [p=0.2] {e}duas horas."),
    # nível depois de um tempo
    dict(id="s10", block="nivel", text="E depois de {a}meia hora, onde está o nível? [p=0.2] {b}Trinta vezes vinte e cinco dá setecentos e cinquenta litros, [p=0.2] ou {c}zero vírgula setenta e cinco metro cúbico. [p=0.3] {d}Dividido pelos três metros quadrados do fundo, dá zero vírgula vinte e cinco metro: [p=0.2] {e}vinte e cinco centímetros."),
    # erro comum
    dict(id="s11", block="erro", text="O erro mais comum é {a}dividir litros por metros quadrados. [p=0.2] {b}Setecentos e cinquenta dividido por três dá duzentos e cinquenta. [p=0.2] O nível subiria {c}duzentos e cinquenta metros, [p=0.2] numa caixa de um metro de altura! [p=0.3] {d}Passe os litros para metros cúbicos antes: três casas para a esquerda."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho. [p=0.2] Com {a}paredes retas e a mesma vazão o tempo todo, [p=0.2] {b}o nível sobe o mesmo tanto a cada minuto. [p=0.3] Meia hora é {c}um quarto das duas horas, [p=0.2] então o nível está em {d}um quarto do metro: vinte e cinco centímetros. [p=0.2] Sem converter nada."),
    dict(id="s13", block="atalho", text="Funciona porque {a}cada centímetro de altura guarda o mesmo volume, [p=0.2] já que o fundo não muda de tamanho. [p=0.3] {b}Não compensa num recipiente que alarga ou afunila, como um funil ou uma garrafa: [p=0.2] ali, {c}o nível sobe mais rápido na parte estreita."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma caixa-d'água em forma de cilindro tem {a}um metro de raio e {b}um vírgula cinco metro de altura. [p=0.2] Uma torneira de {c}trinta litros por minuto enche a caixa vazia. [p=0.2] {d}Use pi igual a três. [p=0.3] {e}Quanto o nível sobe em uma hora? [p=0.2] {f}E em quanto tempo a caixa enche?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] O fundo é um círculo: {a}três vezes um ao quadrado dá três metros quadrados. [p=0.3] Em uma hora, {b}sessenta vezes trinta dá mil e oitocentos litros, [p=0.2] ou {c}um vírgula oito metro cúbico. [p=0.2] {d}Um vírgula oito dividido por três dá zero vírgula seis metro: [p=0.2] o nível sobe {e}sessenta centímetros."),
    dict(id="s17", block="resposta", text="Para encher: {a}três metros quadrados vezes um vírgula cinco dá quatro vírgula cinco metros cúbicos, [p=0.2] {b}quatro mil e quinhentos litros. [p=0.2] {c}Quatro mil e quinhentos dividido por trinta dá cento e cinquenta minutos: [p=0.2] {d}duas horas e meia."),
    dict(id="s18", block="resposta", text="Pelo atalho, confira: [p=0.2] o nível sobe {a}sessenta centímetros por hora, [p=0.2] e a caixa tem {b}cento e cinquenta centímetros. [p=0.2] {c}Cento e cinquenta dividido por sessenta dá dois vírgula cinco: [p=0.2] duas horas e meia. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o quanto o nível sobe é o volume dividido pela área do fundo, [p=0.2] {b}o tempo é o volume dividido pela vazão, [p=0.2] e {c}tudo na mesma unidade antes de dividir."),
    dict(id="s20", block="fim", text="Na próxima aula, você pratica tudo isso: [p=0.2] {a}lê moldes e vistas [p=0.2] e calcula {b}volume, capacidade e área em caixas, latas e reservatórios. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
