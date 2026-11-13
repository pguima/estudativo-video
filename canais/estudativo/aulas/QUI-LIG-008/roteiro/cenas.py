# Estudativo · QUI-LIG-008 — Semelhante dissolve semelhante (Química · Ligações Químicas · Polaridade e forças intermoleculares).
# Habilidade: prever se sal, etanol, óleo e iodo se dissolvem em água ou em gasolina.
# Pré-requisitos: QUI-LIG-004, QUI-LIG-007. Próxima: QUI-LIG-009 (três forças intermoleculares).
# Atenção: LIG-009 (forças) NÃO está em "Já ensinado": a atração entre moléculas de água é dita pelos polos (δ+ com δ−),
# sem o nome "ligação de hidrogênio"; densidade (MAT-RAZ-017) também não: nada de "afunda/boia por ser mais denso".
# Marcas: {cue} animação · [p=0.2] pausa. Questão inédita, criada para esta aula (teste da proveta da ANP, com números redondos).
# Fatos: gasolina = mistura de hidrocarbonetos (apolar); óleo de cozinha quase só C e H (apolar); I₂ pouco solúvel em água
# (≈ 0,3 g/L), solúvel em solventes apolares; etanol miscível em água e em gasolina; a gasolina brasileira leva etanol
# (30 % desde ago/2025): 50 mL de gasolina → 15 mL de etanol → água de 50 para 65 mL. Mel (açúcares, polares) dissolve em água.

TITULO = "Semelhante dissolve semelhante"

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
    dict(id="s01", block="gancho", text="{a}Óleo e água não se misturam: [p=0.1] {b}pode chacoalhar, e as camadas voltam a se separar. [p=0.3] {c}Mas o óleo some na gasolina, [p=0.1] e {d}o sal some na água. [p=0.3] {e}Uma regra de três palavras explica tudo isso."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai prever se {b}sal, álcool, óleo e iodo se dissolvem {c}na água ou na gasolina. [p=0.2] E leva um {d}atalho para decidir olhando a fórmula."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}a polaridade: [p=0.1] {b}a água é polar, com o lado do oxigênio negativo e o dos hidrogênios positivo. [p=0.3] E {c}o sal de cozinha é iônico: [p=0.1] ene á mais e cê éle menos, presos num cristal bem arrumado. [p=0.2] Se alguma travar, procure no canal."),
    # dissolver
    dict(id="s04", block="dissolver", text="{a}Dissolver é espalhar as partículas de uma substância no meio das partículas de outra, [p=0.1] até não dar mais para ver. [p=0.3] {b}Quem se dissolve é o soluto. [p=0.1] {c}Quem dissolve, em maior quantidade, é o solvente."),
    dict(id="s05", block="dissolver", text="{a}A gasolina, sem o álcool, é uma mistura de moléculas feitas só de carbono e hidrogênio. [p=0.2] {b}Esses átomos têm eletronegatividades parecidas, [p=0.1] e as moléculas ficam {c}apolares. [p=0.3] {d}O óleo de cozinha também é quase todo carbono e hidrogênio: apolar."),
    # a regra
    dict(id="s06", block="regra", text="A regra é: {a}semelhante dissolve semelhante. [p=0.3] {b}Polar dissolve polar, e também muitos compostos iônicos, como o sal. [p=0.2] {c}Apolar dissolve apolar. [p=0.3] {d}A água dissolve o sal. [p=0.1] {e}A gasolina dissolve o óleo."),
    dict(id="s07", block="regra", text="Por quê? [p=0.2] {a}As moléculas de água se atraem pelas pontas: [p=0.1] o lado positivo de uma puxa o lado negativo da outra. [p=0.3] {b}Para entrar no meio delas, a partícula precisa oferecer atração também. [p=0.3] {c}O sal oferece. [p=0.1] {d}O lado negativo da água cerca o ene á mais, [p=0.1] {e}o lado positivo cerca o cê éle menos, [p=0.1] e os íons se soltam do cristal."),
    dict(id="s08", block="regra", text="{a}O óleo não oferece nada: não tem polos. [p=0.2] {b}As moléculas de água continuam presas umas às outras, [p=0.1] e {c}deixam o óleo de fora. [p=0.2] Por isso, {d}duas camadas. [p=0.3] {e}E o sal na gasolina? [p=0.1] Fica inteiro: a gasolina não tem polos para soltar os íons."),
    # iodo e etanol
    dict(id="s09", block="exemplos", text="{a}O iodo, i dois, é feito de átomos iguais: apolar. [p=0.2] {b}Na água, ele quase não se dissolve. [p=0.2] {c}Na gasolina, dissolve bem."),
    dict(id="s10", block="exemplos", text="E o álcool comum, o etanol, {a}se mistura com os dois. [p=0.2] {b}A molécula tem um pedaço polar, o ó agá, [p=0.1] e {c}um pedaço apolar, de carbono e hidrogênio. [p=0.3] {d}O ó agá se dá bem com a água, [p=0.1] {e}o pedaço de carbono, com a gasolina. [p=0.3] Por isso, dá para misturar os dois combustíveis: [p=0.1] {f}a gasolina do Brasil já chega ao posto com etanol."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com um erro comum: [p=0.2] {a}achar que o óleo não se mistura porque é grosso. [p=0.3] {b}O mel é bem mais grosso, e se dissolve na água. [p=0.2] {c}A gasolina é fininha, e não se dissolve na água. [p=0.3] {d}Quem decide não é a grossura: é a polaridade."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho para decidir pela fórmula: [p=0.2] {a}só carbono e hidrogênio, ou átomos todos iguais, como i dois? Apolar: vai com a gasolina. [p=0.3] {b}É iônico, de metal com ametal, ou tem ó agá? Em geral, vai com a água. [p=0.3] Funciona porque {c}as ligações entre carbono e hidrogênio quase não têm polo, [p=0.1] e {d}o ó agá é bem polar."),
    dict(id="s13", block="atalho", text="{a}Não compensa com moléculas grandes, de muitos carbonos e um ó agá só: [p=0.1] {b}a parte apolar vence, e elas quase não se dissolvem na água."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um fiscal usa uma proveta, um tubo de vidro com marcas de volume. [p=0.2] {b}Ele mistura cinquenta mililitros de gasolina com cinquenta mililitros de água, [p=0.1] e agita. [p=0.3] {c}No fim, a camada de água tem sessenta e cinco mililitros. [p=0.3] {d}Por que a água aumentou? [p=0.2] E {e}quantos mililitros de etanol havia na gasolina?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Água e gasolina não se misturam: polar e apolar. [p=0.2] {b}Mas o etanol da gasolina se dá bem com a água, [p=0.1] e {c}passa para a camada de água. [p=0.3] {d}A água ganhou o etanol: [p=0.1] sessenta e cinco menos cinquenta dá {e}quinze mililitros de etanol. [p=0.2] E a camada de gasolina encolheu para trinta e cinco."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}semelhante dissolve semelhante. [p=0.1] {b}Polar e iônico vão com a água, [p=0.1] {c}apolar vai com a gasolina, [p=0.1] e {d}o etanol, com um pedaço de cada, vai com os dois."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai conhecer {a}as três forças que seguram uma molécula na outra: [p=0.1] {b}dipolo induzido, dipolo permanente e ligação de hidrogênio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
