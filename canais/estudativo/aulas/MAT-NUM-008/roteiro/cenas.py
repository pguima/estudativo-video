# Estudativo · MAT-NUM-008 — Multiplicar por dois algarismos (Matemática · Números e Contas).
# Habilidade: calcular 34 × 26 com a conta armada.
# Pré-requisitos: MAT-NUM-007 (multiplicar por 10, por 100 e por um algarismo). Próxima: MAT-NUM-009.
# Questão inédita, criada para esta aula. Sem divisão: ela só chega em MAT-NUM-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Multiplicar por dois algarismos"

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
    dict(id="s01", block="gancho", text="Um auditório tem {a}trinta e quatro fileiras [p=0.2] com {b}vinte e seis cadeiras cada. [p=0.3] Se a sua conta deu {c}duzentas e setenta e duas cadeiras, [p=0.2] sumiram mais de seiscentas, [p=0.2] tudo por causa de {d}um zero."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai multiplicar por dois algarismos [p=0.2] sem perder esse zero [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}multiplicar por um algarismo, com vai-um, [p=0.2] e {c}acrescentar o zero quando multiplica por dez. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia: dois blocos
    dict(id="s04", block="blocos", text="Antes da conta, pense nas cadeiras. [p=0.2] Passe um corredor por todas as fileiras. [p=0.2] Cada fileira fica com {a}vinte cadeiras de um lado [p=0.2] e {b}seis do outro."),
    dict(id="s05", block="blocos", text="O bloco pequeno tem {a}trinta e quatro vezes seis. [p=0.2] O bloco grande tem {b}trinta e quatro vezes vinte. [p=0.3] {c}Some os blocos, e estão contadas todas as cadeiras. [p=0.2] A conta armada é só isso, escrito em duas linhas."),
    # conta armada
    dict(id="s06", block="conta", text="{a}Arme a conta: trinta e quatro em cima, [p=0.2] {b}vinte e seis embaixo, [p=0.2] unidade embaixo de unidade."),
    dict(id="s07", block="conta", text="{a}Primeira linha: tudo vezes seis. [p=0.2] {b}Seis vezes quatro dá vinte e quatro: [p=0.2] {c}escreva o quatro, e o dois sobe. [p=0.2] {d}Seis vezes três dá dezoito. [p=0.2] {e}Com o dois que subiu, vinte. [p=0.3] {f}Duzentos e quatro: esse é o bloco pequeno."),
    dict(id="s08", block="conta", text="{a}Segunda linha: agora o dois do vinte e seis. [p=0.3] Esse dois não vale dois. [p=0.2] Ele está na casa das dezenas, então {b}vale vinte. [p=0.3] E vezes vinte é vezes dois e vezes dez. [p=0.2] Por isso, {c}a linha começa com um zero."),
    dict(id="s09", block="conta", text="Antes de seguir, {a}risque o dois que subiu: ele já foi usado. [p=0.3] {b}Dois vezes quatro dá oito. [p=0.2] {c}Dois vezes três dá seis. [p=0.3] {d}Seiscentos e oitenta: esse é o bloco grande."),
    dict(id="s10", block="conta", text="{a}Some as linhas, como numa soma comum: [p=0.2] {b}duzentos e quatro mais seiscentos e oitenta. [p=0.3] São {c}oitocentas e oitenta e quatro cadeiras."),
    # conferir trocando a ordem
    dict(id="s11", block="conferir", text="Para conferir, {a}troque a ordem: [p=0.2] {b}vinte e seis vezes trinta e quatro. [p=0.3] Primeira linha, vezes quatro: {c}cento e quatro. [p=0.2] Segunda linha, vezes trinta: {d}o zero primeiro. [p=0.2] {e}Três vezes seis dá dezoito: escreva o oito, e o um sobe. [p=0.2] {f}Três vezes dois dá seis. [p=0.2] Com o um que subiu, {g}sete. [p=0.2] {h}Setecentos e oitenta. [p=0.3] Somando as linhas, {i}oitocentos e oitenta e quatro de novo."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}esquecer o zero. [p=0.2] A pessoa escreve {b}sessenta e oito embaixo do duzentos e quatro [p=0.2] e soma: {c}duzentos e setenta e dois. [p=0.3] Ela multiplicou por dois, e o número valia vinte. [p=0.2] {d}Quase todo o bloco grande sumiu. [p=0.2] O zero guarda a casa das unidades e empurra o resto para as dezenas."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}confira pelo tamanho. [p=0.3] Troque cada número pelo redondo mais perto: [p=0.2] {b}trinta e quatro vira trinta. [p=0.2] {c}Vinte e seis também vira trinta. [p=0.3] {d}Três vezes três dá nove, [p=0.2] com um zero de cada trinta: {e}novecentos."),
    dict(id="s14", block="atalho", text="{a}Oitocentos e oitenta e quatro está perto de novecentos. [p=0.2] {b}Duzentos e setenta e dois, nem de longe. [p=0.3] Funciona porque {c}arredondar muda pouco cada número, [p=0.2] então muda pouco o resultado. [p=0.3] {d}Não compensa quando as opções de resposta da prova são muito próximas: [p=0.2] aí, arme a conta."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um mercado recebeu {a}vinte e sete caixas, [p=0.2] cada uma com {b}trinta e oito latas. [p=0.3] {c}Quantas latas chegaram no total?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Trinta e oito em cima, vinte e sete embaixo. [p=0.3] Primeira linha, vezes sete: [p=0.2] {b}sete vezes oito dá cinquenta e seis. [p=0.2] {c}Escreva o seis, e o cinco sobe. [p=0.2] {d}Sete vezes três dá vinte e um. [p=0.2] Com o cinco que subiu, {e}vinte e seis. [p=0.2] {f}Duzentos e sessenta e seis."),
    dict(id="s18", block="resposta", text="Segunda linha, vezes vinte: {a}o zero primeiro. [p=0.2] {b}Dois vezes oito dá dezesseis. [p=0.2] {c}Escreva o seis, e o um sobe. [p=0.2] {d}Dois vezes três dá seis. [p=0.2] Com o um que subiu, {e}sete. [p=0.2] {f}Setecentos e sessenta. [p=0.3] Some as linhas: [p=0.2] {g}seis mais zero, seis. [p=0.2] {h}Seis mais seis, doze: fica o dois e vai um. [p=0.2] {i}Dois mais sete, nove, com o um que veio, dez. [p=0.2] É a última casa: escreva o dez. [p=0.3] {j}Mil e vinte e seis latas."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}uma linha para as unidades, [p=0.2] {b}outra para as dezenas, começando com zero, [p=0.2] e {c}some as linhas."),
    dict(id="s20", block="fim", text="Na próxima aula, a conta anda ao contrário: [p=0.2] você vai {a}dividir por um algarismo, [p=0.2] entender {b}o resto [p=0.2] e {c}tirar a prova real. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
