# Estudativo · MAT-POR-003 — Descobrir quantos por cento e achar o total (Matemática · Porcentagem).
# Habilidade: dizer que 30 é 25% de 120 e descobrir o total sabendo que 60 são 30% dele.
# Pré-requisitos: MAT-POR-002 (porcentagem de um valor), MAT-RAZ-006 (regra de três direta). Próxima: MAT-POR-004.
# Questão inédita, criada para esta aula. MAT-FRA-018 ainda não foi ensinada: nada de dividir por decimal.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Descobrir quantos por cento e achar o total"

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
    dict(id="s01", block="gancho", text="Você ganhou {a}trinta reais de desconto numa compra de {b}cento e vinte. [p=0.3] Quantos por cento foi o desconto? [p=0.2] Muita gente chuta {c}trinta por cento, [p=0.2] só porque o número é trinta. [p=0.3] Mas foi {d}vinte e cinco."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai descobrir quantos por cento uma parte é do total, [p=0.2] achar o total quando só conhece a parte, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}calcular a porcentagem de um valor [p=0.2] e {c}montar uma regra de três. [p=0.3] Se faltar alguma, procure no canal."),
    # quantos por cento
    dict(id="s04", block="quantos", text="Quantos por cento trinta é de cento e vinte? [p=0.2] Comece pela fração: {a}a parte em cima, o total embaixo. [p=0.3] {b}Trinta cento e vinte avos."),
    dict(id="s05", block="quantos", text="Agora, divida: {a}trinta dividido por cento e vinte dá zero vírgula vinte e cinco. [p=0.3] Zero vírgula vinte e cinco é {b}vinte e cinco centésimos. [p=0.2] Ou seja, {c}vinte e cinco por cento."),
    dict(id="s06", block="quantos", text="A regra: {a}divida a parte pelo total. [p=0.2] Depois, {b}ande a vírgula duas casas para a direita. [p=0.3] Isso é multiplicar por cem, [p=0.2] porque {c}por cento conta em cada cem. [p=0.3] {d}Zero vírgula quatro, por exemplo, vira quarenta por cento."),
    dict(id="s07", block="quantos", text="A regra de três chega no mesmo lugar. [p=0.2] Monte a tabela: {a}reais de um lado, por cento do outro. [p=0.2] Na primeira linha, cento e vinte reais e cem por cento. [p=0.2] Na segunda, trinta reais e xis. [p=0.3] {b}Cento e vinte está para trinta, assim como cem está para xis. [p=0.3] {c}Pelo produto cruzado, cento e vinte vezes xis é igual a três mil. [p=0.2] {d}Xis é igual a vinte e cinco."),
    # achar o total
    dict(id="s08", block="total", text="Agora, o caminho de volta. [p=0.2] {a}Sessenta reais são trinta por cento de um valor. [p=0.2] Qual é o valor inteiro? [p=0.3] Aqui, sessenta é {b}a parte. [p=0.2] O total é {c}o cem por cento."),
    dict(id="s09", block="total", text="Passe por um pedaço pequeno: {a}o dez por cento. [p=0.2] Trinta por cento são três vezes dez por cento. [p=0.2] Então {b}dez por cento é sessenta dividido por três: vinte reais. [p=0.3] O total são dez vezes isso: {c}vinte vezes dez dá duzentos reais."),
    dict(id="s10", block="total", text="É a mesma ideia de achar o preço de um quilo antes de achar o de sete. [p=0.3] Pela regra de três, também sai. [p=0.2] Na tabela, {a}trinta por cento com sessenta reais, [p=0.2] e cem por cento com xis. [p=0.2] Trinta está para cem, assim como sessenta está para xis. [p=0.2] {b}Trinta vezes xis é igual a seis mil, e xis é igual a duzentos."),
    dict(id="s11", block="total", text="E dá para conferir: {a}dez por cento de duzentos é vinte. [p=0.2] {b}Vezes três, sessenta. [p=0.2] Bateu."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}calcular a porcentagem da parte. [p=0.2] A pessoa faz {b}trinta por cento de sessenta [p=0.2] e responde {c}dezoito. [p=0.3] Mas sessenta já é um pedaço do total. [p=0.2] O total {d}não pode ser menor que a parte."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para achar quantos por cento: {a}faça o total virar cem. [p=0.3] {b}Dezessete de cinquenta. [p=0.2] Dobre em cima e embaixo: {c}trinta e quatro em cada cem. [p=0.2] {d}Trinta e quatro por cento, sem dividir nada."),
    dict(id="s14", block="atalho", text="Funciona porque a fração equivalente {a}não muda o valor, [p=0.2] e com cem embaixo, o de cima já é a porcentagem. [p=0.3] Total vinte e cinco? {b}Multiplique por quatro. [p=0.2] Total duzentos? {c}Divida por dois. [p=0.3] Não compensa com {d}cento e vinte: [p=0.2] aí, divida a parte pelo total."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma turma tem {a}quarenta alunos. [p=0.2] Desses, {b}catorze passaram de primeira. [p=0.2] {c}Quantos por cento passaram? [p=0.3] Na mesma escola, {d}quarenta e cinco alunos são quinze por cento do total. [p=0.2] {e}Quantos alunos tem a escola?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Na turma, a fração é {a}catorze quarenta avos. [p=0.2] {b}Divida em cima e embaixo por dois: sete vinte avos. [p=0.3] Vinte vezes cinco dá cem, então {c}multiplique em cima e embaixo por cinco: [p=0.2] {d}trinta e cinco centésimos. [p=0.2] {e}Trinta e cinco por cento passaram."),
    dict(id="s18", block="resposta", text="Na escola, quarenta e cinco é {a}a parte. [p=0.2] Quinze por cento são três vezes cinco por cento, [p=0.2] então {b}cinco por cento é quarenta e cinco dividido por três: quinze alunos. [p=0.3] Cem por cento são vinte vezes cinco por cento: [p=0.2] {c}quinze vezes vinte dá trezentos alunos."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}quantos por cento é a parte dividida pelo total. [p=0.2] Para {b}achar o total, passe por um pedaço pequeno e chegue ao cem por cento."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai aumentar e descontar com {a}uma conta só: [p=0.2] por exemplo, {b}somar quinze por cento a um preço multiplicando por um vírgula quinze. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
