# Estudativo · FIS-CAL-008 — Praticando: temperatura, dilatação e calorimetria (Física · Calor e Termodinâmica · prática).
# Habilidade: resolver questões de escalas, dilatação e trocas de calor com e sem mudança de estado.
# Pré-requisitos: FIS-CAL-001 a FIS-CAL-007. Próxima: FIS-CAL-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Valores de tabela: c água = 1, c gelo = 0,5 cal/(g·°C), L fusão = 80 cal/g.
# La Paz (cerca de 3.600 m): a água ferve perto de 88 °C.

TITULO = "Praticando: temperatura, dilatação e calorimetria"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, [p=0.2] criadas para esta aula, [p=0.2] com tudo o que você viu sobre temperatura e calor. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}a proporção entre escalas, [p=0.2] {b}delta éle igual a éle zero alfa delta tê, [p=0.2] {c}quê igual a eme cê delta tê, [p=0.2] {d}quê igual a eme éle [p=0.2] e {e}a soma dos calores igual a zero. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: escala inventada
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um cientista cria a escala xis. [p=0.2] Nela, {b}o gelo derrete a vinte graus xis [p=0.1] e {c}a água ferve a duzentos e vinte. [p=0.3] {d}Quanto marca essa escala quando a Celsius marca cinquenta?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] O caminho do gelo à fervura: {a}cem graus na Celsius [p=0.1] e {b}duzentos na xis. [p=0.3] {c}Cinquenta graus Celsius é metade do caminho. [p=0.2] Na xis, {d}metade de duzentos é cem, [p=0.2] contados a partir do gelo, {e}que é vinte. [p=0.3] {f}Cento e vinte graus xis."),
    dict(id="s06", block="resposta1", text="Pela proporção, dá o mesmo: [p=0.2] {a}xis menos vinte, dividido por duzentos, igual a cinquenta dividido por cem. [p=0.3] Quem esquece de somar o vinte {b}responde cem, [p=0.1] {c}e erra."),
    # situação 2: dilatação volumétrica
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Um bloco de metal tem {b}quinhentos centímetros cúbicos. [p=0.2] O alfa do metal é {c}dois vezes dez elevado a menos cinco por grau Celsius. [p=0.3] {d}Quanto o volume aumenta se o bloco esquentar cem graus?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] É volume, então {a}gama, três alfa: [p=0.2] {b}seis vezes dez elevado a menos cinco. [p=0.3] {c}Delta vê é quinhentos, vezes cem, vezes o gama. [p=0.3] {d}Quinhentos vezes cem dá cinquenta mil, que é cinco vezes dez elevado a quatro. [p=0.2] {e}Cinco vezes seis dá trinta, [p=0.1] e {f}dez elevado a quatro vezes dez elevado a menos cinco dá dez elevado a menos um."),
    dict(id="s10", block="resposta2", text="{a}Trinta vezes zero vírgula um: três centímetros cúbicos. [p=0.3] Quem usa o alfa em vez do gama acha {b}um, [p=0.2] {c}três vezes menos."),
    # situação 3: metal na água
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Uma peça de {b}duzentos gramas de metal a trezentos graus, [p=0.1] com calor específico {c}zero vírgula um, [p=0.2] cai num calorímetro com {d}trezentos e oitenta gramas de água a vinte graus. [p=0.3] {e}Qual é a temperatura final?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Substâncias diferentes: {a}nada de média ponderada só com as massas. [p=0.2] Soma dos calores igual a zero. [p=0.3] {b}Metal: duzentos, vezes zero vírgula um, vezes a variação, tê menos trezentos. [p=0.2] {c}Água: trezentos e oitenta, vezes um, vezes a variação, tê menos vinte."),
    dict(id="s14", block="resposta3", text="Fica {a}vinte tê menos seis mil, [p=0.1] mais trezentos e oitenta tê menos sete mil e seiscentos, [p=0.1] igual a zero. [p=0.3] {b}Quatrocentos tê igual a treze mil e seiscentos. [p=0.2] {c}Tê igual a trinta e quatro graus Celsius."),
    # situação 4: gelo abaixo de zero
    dict(id="s15", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Cem gramas de gelo a menos dez graus [p=0.1] caem em {c}duzentos gramas de água a cinquenta graus. [p=0.3] O calor específico do gelo é {d}zero vírgula cinco. [p=0.2] {e}Derrete tudo? Qual é a temperatura final?"),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Vamos lá. [p=0.2] Primeiro, compare. [p=0.2] {a}Disponível: duzentos vezes cinquenta dá dez mil calorias. [p=0.3] Necessário, em duas etapas: [p=0.2] {b}levar o gelo até zero, cem vezes zero vírgula cinco vezes dez, que dá quinhentas; [p=0.2] {c}e derreter, cem vezes oitenta, que dá oito mil. [p=0.2] {d}No total, oito mil e quinhentas."),
    dict(id="s18", block="resposta4", text="{a}Dez mil é mais que oito mil e quinhentos: derrete tudo. [p=0.3] {b}Sobram mil e quinhentas calorias [p=0.1] para {c}trezentos gramas de água a partir de zero. [p=0.2] {d}Mil e quinhentos dividido por trezentos: cinco graus Celsius."),
    # situação 5: diagrama de fases
    dict(id="s19", block="questao5", text="{a}Última situação. [p=0.2] Em {b}La Paz, na Bolívia, a mais de três mil e quinhentos metros de altitude, [p=0.2] {c}a água ferve perto de oitenta e oito graus. [p=0.3] {d}Use o diagrama de fases para explicar por quê."),
    dict(id="s20", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta5", text="Vamos lá. [p=0.2] Lá no alto, há menos ar em cima de você, [p=0.2] então {a}a pressão é menor que uma atmosfera. [p=0.3] {b}A linha da pressão desce [p=0.2] e {c}cruza a curva de vaporização mais à esquerda, [p=0.1] {d}antes dos cem graus. [p=0.3] Pressão menor, {e}ebulição mais fria."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}escala nova é proporção a partir do gelo; [p=0.2] {b}volume pede gama, três alfa; [p=0.2] {c}substâncias diferentes pedem a soma igual a zero; [p=0.2] e {d}com gelo, compare antes de calcular."),
    dict(id="s23", block="fim", text="Na próxima aula, você vai ver {a}como o calor viaja dentro de um material, [p=0.2] e por que {b}o metal parece mais frio que a madeira, mesmo estando na mesma temperatura. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
