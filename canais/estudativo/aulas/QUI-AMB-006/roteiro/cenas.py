# Estudativo · QUI-AMB-006 — Química verde e economia atômica (Química · Química e Ambiente · Tratamento de água e química verde).
# Habilidade: aplicar os princípios da química verde e calcular a economia atômica de um processo.
# Pré-requisitos: QUI-CAL-008, MAT-POR-003. Próxima: QUI-AMB-007 (praticando: química e ambiente).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: os 12 princípios da química verde (Anastas e Warner, 1998); economia atômica = massa molar do produto desejado ÷
# soma das massas molares dos reagentes (com os coeficientes) × 100. Massas: H 1, C 12, N 14, O 16, Ca 40, Fe 56.
# N₂ + 3 H₂ → 2 NH₃: 28 + 6 = 34 → 34: 100%. CaCO₃ → CaO + CO₂: 56 ÷ 100 = 56%.
# Fe₂O₃ + 3 CO → 2 Fe + 3 CO₂: 160 + 84 = 244; 2 × 56 = 112; 112 ÷ 244 ≈ 0,459 → cerca de 46%.
# Só QUI-MIS-001, ATO, INO-007/008 e CAL estão em "Já ensinado" de Química: sem orgânica e sem ambiente.

TITULO = "Química verde e economia atômica"

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
    dict(id="s01", block="gancho", text="{a}Uma reação pode ter rendimento de cem por cento [p=0.1] {b}e, mesmo assim, jogar fora quase metade da massa que você comprou. [p=0.3] {c}Por isso a química verde criou outra conta: [p=0.1] {d}a economia atômica."),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai conhecer {b}os princípios da química verde [p=0.2] e {c}calcular a economia atômica de um processo, [p=0.1] {d}para dizer qual caminho desperdiça menos."),
    # lembrete
    dict(id="s03", block="lembrete", text="Três lembretes. [p=0.2] {a}A massa molar é a soma das massas dos átomos da fórmula. [p=0.3] {b}Pela conservação das massas, os reagentes somam a mesma massa que os produtos. [p=0.3] {c}E porcentagem é a parte dividida pelo total, vezes cem."),
    # química verde
    dict(id="s04", block="verde", text="{a}Química verde é planejar a reação para não sujar desde o começo. [p=0.3] {b}A ideia principal é simples: [p=0.1] {c}é melhor não gerar o resíduo do que tratá-lo depois."),
    dict(id="s05", block="verde", text="São doze princípios, e a prova cobra estes. [p=0.2] {a}Prevenir o resíduo. [p=0.2] {b}Usar substâncias menos tóxicas. [p=0.2] {c}Trocar os líquidos perigosos usados para dissolver, os solventes, por água, quando der. [p=0.2] {d}Gastar menos energia, trabalhando perto da temperatura ambiente. [p=0.2] {e}Usar matéria-prima renovável. [p=0.2] {f}E preferir catalisadores: substâncias que aceleram a reação e saem inteiras dela."),
    dict(id="s06", block="verde", text="{a}E há um princípio que dá para medir: [p=0.1] {b}aproveitar o máximo dos átomos dos reagentes no produto que você quer. [p=0.3] Essa é a economia atômica."),
    # a conta
    dict(id="s07", block="conta", text="A conta: {a}massa molar do produto desejado, [p=0.1] {b}dividida pela soma das massas molares dos reagentes, [p=0.1] {c}vezes cem. [p=0.3] {d}Use a equação balanceada, com os coeficientes."),
    dict(id="s08", block="conta", text="{a}Primeiro exemplo: a amônia. [p=0.2] {b}Uma molécula de nitrogênio, ene dois, mais três de hidrogênio, agá dois, dá duas de amônia, ene agá três. [p=0.3] {c}Reagentes: vinte e oito mais seis dá trinta e quatro gramas. [p=0.2] {d}Produto: duas vezes dezessete dá trinta e quatro. [p=0.3] {e}Trinta e quatro de trinta e quatro: [p=0.1] {f}cem por cento. Nenhum átomo sobra."),
    dict(id="s09", block="conta", text="{a}Segundo exemplo: a cal virgem, cê á ó, que se tira do calcário, cê á cê ó três. [p=0.3] {b}Aquecido, o calcário se quebra em cal e cê ó dois. [p=0.3] {c}Reagente: cem gramas. [p=0.2] {d}Produto desejado, a cal: cinquenta e seis. [p=0.3] {e}Cinquenta e seis dividido por cem dá cinquenta e seis por cento."),
    dict(id="s10", block="conta", text="{a}Os outros quarenta e quatro por cento saem como cê ó dois, que você não queria. [p=0.3] {b}E isso acontece mesmo com rendimento de cem por cento."),
    # rendimento × economia
    dict(id="s11", block="compara", text="Qual é a diferença para o rendimento? [p=0.2] {a}O rendimento compara o que você obteve com o que a equação promete. [p=0.3] {b}A economia atômica olha a própria equação: [p=0.1] {c}quanto da massa dos reagentes pode terminar no produto que você quer. [p=0.3] {d}Um diz se a reação foi bem feita; [p=0.1] {e}o outro, se o caminho escolhido é bom."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}achar que rendimento de cem por cento quer dizer processo verde. [p=0.3] {b}A cal acabou de mostrar que não: [p=0.1] {c}cem por cento de rendimento, e quarenta e quatro por cento da massa vira cê ó dois."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.1] {a}se a equação tem um produto só, a economia atômica é cem por cento, sem conta. [p=0.3] {b}Funciona porque todos os átomos dos reagentes vão para ele. [p=0.3] {c}É o caso da amônia: tudo vira um produto só."),
    dict(id="s14", block="atalho", text="{a}O atalho não vale quando há subproduto: [p=0.1] aí, é preciso fazer a conta. [p=0.3] {b}E economia alta não basta: [p=0.1] {c}um caminho com cem por cento, mas com reagente tóxico ou muito gasto de energia, ainda fere outros princípios."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Na siderurgia, o ferro sai do minério assim: [p=0.1] {b}óxido de ferro, éfe é dois ó três, mais três cê ó dá dois éfe é mais três cê ó dois. [p=0.3] {c}As massas molares são: minério, cento e sessenta; cê ó, vinte e oito; ferro, cinquenta e seis. [p=0.3] {d}Qual é a economia atômica, se o produto desejado é o ferro?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}Reagentes: cento e sessenta mais três vezes vinte e oito. [p=0.2] {b}Três vezes vinte e oito dá oitenta e quatro, [p=0.1] {c}e o total dá duzentos e quarenta e quatro. [p=0.3] {d}Produto: dois ferros, duas vezes cinquenta e seis, que dá cento e doze."),
    dict(id="s18", block="resposta", text="{a}Cento e doze dividido por duzentos e quarenta e quatro. [p=0.2] {b}Atalho de cabeça: a metade de duzentos e quarenta e quatro é cento e vinte e dois, [p=0.1] e cento e doze é um pouco menos. [p=0.3] {c}A conta dá cerca de quarenta e seis por cento. [p=0.3] {d}Quem esqueceu o três do cê ó achou cento e doze de cento e oitenta e oito, e errou."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}química verde é não gerar o resíduo; [p=0.2] {b}economia atômica é produto desejado sobre reagentes, vezes cem; [p=0.2] e {c}um produto só dá cem por cento."),
    dict(id="s20", block="fim", text="Na próxima aula, você pratica tudo da química ambiental [p=0.1] {a}em textos de prova sobre energia, poluição e água. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
