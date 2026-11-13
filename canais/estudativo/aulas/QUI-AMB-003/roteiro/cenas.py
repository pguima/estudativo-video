# Estudativo · QUI-AMB-003 — Efeito estufa e camada de ozônio (Química · Química e Ambiente · Combustíveis, poluição e chuva ácida).
# Habilidade: diferenciar efeito estufa de buraco na camada de ozônio, citar CO₂, CH₄ e CFC e dizer onde o ozônio protege
# e onde polui.
# Pré-requisitos: QUI-AMB-001, QUI-ORG-010. Próxima: QUI-AMB-004 (tratamento de água).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fórmulas faladas: CO₂ "cê ó dois", CH₄ "cê agá quatro", O₃ "ó três", O₂ "ó dois", CFC "cê éfe cê".
# Fatos: sem efeito estufa, a média da Terra seria cerca de −18 °C (hoje, cerca de 15 °C); o CO₂ do ar subiu cerca de 50%
# desde antes das fábricas (de ~280 para ~420 partes por milhão; ppm não está em "Já ensinado", então só a porcentagem);
# o metano retém dezenas de vezes mais calor que a mesma massa de CO₂; a camada de ozônio fica na estratosfera, entre
# cerca de 15 e 35 km; o cloro do CFC age como catalisador e um átomo destrói milhares de moléculas de O₃; Protocolo de
# Montreal (1987) baniu os CFC e a camada se recupera devagar; o ozônio perto do chão forma-se de gases do escapamento
# com luz do Sol e irrita olhos e pulmões; os CFC também são gases estufa. AMB-002 não está em "Já ensinado".

TITULO = "Efeito estufa e camada de ozônio"

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
    dict(id="s01", block="gancho", text="{a}O buraco na camada de ozônio esquenta o planeta? [p=0.3] {b}Não. [p=0.3] {c}Efeito estufa e camada de ozônio são dois problemas diferentes, [p=0.1] {d}com gases diferentes, em lugares diferentes do céu."),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai separar os dois de vez, [p=0.2] {b}saber quais gases causam cada um [p=0.2] e {c}descobrir onde o ozônio protege e onde ele polui."),
    # lembrete
    dict(id="s03", block="lembrete", text="Três lembretes. [p=0.2] {a}O ozônio, ó três, é um alótropo do oxigênio que você respira, o ó dois. [p=0.3] {b}A queima de combustível fóssil põe no ar cê ó dois novo. [p=0.3] {c}E o cê éfe cê, um haleto orgânico com cloro e flúor, solta cloro quando a luz forte do Sol o quebra."),
    # efeito estufa
    dict(id="s04", block="estufa", text="Comece pela estufa. [p=0.2] {a}A luz do Sol atravessa o ar e esquenta o chão. [p=0.3] {b}O chão quente devolve energia para o céu, como calor, numa luz invisível chamada infravermelho. [p=0.3] {c}Alguns gases do ar seguram parte desse calor [p=0.1] {d}e o mandam de volta para baixo."),
    dict(id="s05", block="estufa", text="{a}Isso é o efeito estufa, e ele é bom. [p=0.3] {b}Sem ele, a média da Terra seria de dezoito graus negativos. [p=0.2] {c}Com ele, fica perto de quinze graus positivos. [p=0.3] {d}O problema é a intensificação: gás demais, calor demais."),
    dict(id="s06", block="estufa", text="{a}O principal culpado é o cê ó dois, da queima de petróleo, carvão e gás, e das queimadas. [p=0.3] {b}Desde o começo das fábricas, há uns duzentos anos, o cê ó dois do ar já subiu cerca de cinquenta por cento. [p=0.3] {c}O segundo é o metano, cê agá quatro: [p=0.1] {d}sai do arroto do gado, dos lixões e das plantações de arroz alagadas. [p=0.3] {e}Cada quilo de metano segura dezenas de vezes mais calor que um quilo de cê ó dois."),
    # ozônio
    dict(id="s07", block="ozonio", text="Agora, o ozônio. [p=0.2] {a}Bem acima das nuvens, entre quinze e trinta e cinco quilômetros de altura, [p=0.1] {b}há uma camada com mais ó três. [p=0.3] {c}Ela barra a maior parte da luz ultravioleta do Sol, [p=0.1] {d}a que queima a pele, causa câncer de pele e danifica os olhos."),
    dict(id="s08", block="ozonio", text="{a}O cê éfe cê era usado em geladeiras e sprays. [p=0.2] {b}Ele não reage com nada aqui embaixo e sobe devagar até a camada. [p=0.3] {c}Lá em cima, a luz ultravioleta solta o cloro, [p=0.1] {d}e cada átomo de cloro destrói milhares de moléculas de ó três, [p=0.1] {e}porque age como catalisador: sai inteiro de cada reação."),
    dict(id="s09", block="ozonio", text="{a}Em mil novecentos e oitenta e sete, nasceu o Protocolo de Montreal. [p=0.2] {b}Com o tempo, todos os países aderiram, e o uso de cê éfe cê foi proibido. [p=0.3] {c}A camada está se recuperando, devagar."),
    # ozônio ruim
    dict(id="s10", block="chao", text="E aqui está a pegadinha. [p=0.2] {a}O ó três também se forma perto do chão, [p=0.1] {b}a partir dos gases do escapamento, com a luz do Sol. [p=0.3] {c}Aqui embaixo, ele irrita os olhos e o pulmão: é poluente. [p=0.3] {d}Lá no alto, o ozônio protege; [p=0.1] {e}aqui embaixo, polui."),
    # atalho
    dict(id="s11", block="atalho", text="O atalho de prova é {a}a direção da luz. [p=0.3] {b}O efeito estufa segura o calor que sai do chão: [p=0.1] {c}gases cê ó dois e metano; resultado, aquecimento. [p=0.3] {d}A camada de ozônio barra a luz que chega do Sol: [p=0.1] {e}o culpado é o cê éfe cê; resultado, mais ultravioleta na pele."),
    dict(id="s12", block="atalho", text="Funciona porque {a}são duas luzes diferentes: [p=0.1] infravermelho saindo, ultravioleta entrando. [p=0.3] {b}A principal ponte entre os dois é o cê éfe cê, [p=0.1] {c}que, além de destruir ozônio, também é um gás estufa forte. [p=0.2] Se a questão disser isso, não estranhe."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}dizer que o buraco na camada de ozônio aumenta o aquecimento global. [p=0.3] {b}O buraco deixa entrar mais ultravioleta, [p=0.1] e isso queima a pele, não esquenta o planeta. [p=0.3] {c}O aquecimento vem do calor preso pelos gases estufa."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Cada fato é de efeito estufa ou de camada de ozônio? [p=0.3] {a}Um: o gado solta metano. [p=0.2] {b}Dois: mais ultravioleta chega ao chão no sul do planeta. [p=0.2] {c}Três: a queima de carvão aumenta o cê ó dois. [p=0.2] {d}Quatro: um gás de geladeira antiga solta cloro lá no alto."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="{a}Um: metano segura calor, efeito estufa. [p=0.2] {b}Dois: ultravioleta é a luz que o ozônio barra, camada de ozônio. [p=0.2] {c}Três: cê ó dois, efeito estufa. [p=0.2] {d}Quatro: cloro do cê éfe cê, camada de ozônio."),
    dict(id="s17", block="resposta", text="{a}Ficou meio a meio: [p=0.1] um e três no efeito estufa, [p=0.1] dois e quatro na camada de ozônio. [p=0.2] {b}Quem pôs o ultravioleta no efeito estufa trocou as luzes: [p=0.1] {c}estufa é o calor que sai, ozônio é a luz que entra."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}efeito estufa segura o calor, com cê ó dois e metano; [p=0.2] {b}a camada de ozônio barra o ultravioleta e é atacada pelo cê éfe cê; [p=0.2] e {c}o ozônio protege no alto e polui perto do chão."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai seguir a água do rio até a sua torneira: [p=0.2] {a}as etapas do tratamento de água e a química de cada uma. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
