# Estudativo · FIS-EGF-007 — Empuxo: princípio de Arquimedes (Física · Equilíbrio, Gravitação e Fluidos · Hidrostática).
# Habilidade: calcular E = d·V·g, sabendo que d é a densidade do líquido e V o volume deslocado.
# Pré-requisitos: FIS-EGF-005 (Stevin), FIS-DIN-001 (resultante), MAT-MED-005 (litros e m³). Próxima: FIS-EGF-008.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# A letra do empuxo (E) é narrada como "empuxo", para não confundir com o verbo "é". g = 10 m/s²; água 1.000 kg/m³; ferro 7.800.
# Contas: 1.000·0,002·10 = 20 N; 800·0,002·10 = 16 N; 7.800·0,001·10 = 78 N; 800·0,003·10 = 24 N; metade = 12 N.

TITULO = "Empuxo: princípio de Arquimedes"

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
    dict(id="s01", block="gancho", text="{a}Uma bola de ferro e uma de isopor, do mesmo tamanho, [p=0.1] {b}presas totalmente debaixo d'água. [p=0.3] {c}Qual recebe mais força da água para cima? [p=0.3] {d}Nenhuma. [p=0.2] A força é a mesma nas duas."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender de onde vem essa força [p=0.2] e {b}calcular quanto ela vale."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}A lei de Stevin: quanto mais fundo, maior a pressão. [p=0.2] E {c}a densidade: massa sobre volume, [p=0.1] mil quilos por metro cúbico na água. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem
    dict(id="s04", block="origem", text="{a}Mergulhe uma caixa na água. [p=0.2] {b}Nas laterais, a água empurra dos dois lados, [p=0.1] e esses empurrões se anulam. [p=0.3] {c}Mas a face de baixo está mais funda que a de cima. [p=0.2] {d}Lá embaixo, a pressão é maior. [p=0.3] {e}A sobra é uma força para cima: o empuxo."),
    dict(id="s05", block="origem", text="{a}Arquimedes descobriu quanto ela vale: [p=0.2] {b}o empuxo é igual ao peso do líquido que o corpo tira do lugar. [p=0.3] {c}O corpo entra, e a água sai do caminho. [p=0.2] {d}O peso dessa água que saiu é o empuxo."),
    # fórmula
    dict(id="s06", block="formula", text="Em fórmula: [p=0.1] {a}empuxo igual a dê vezes vê vezes gê. [p=0.3] {b}Dê é a densidade do líquido, não a do corpo, em quilograma por metro cúbico. [p=0.2] {c}Vê é o volume deslocado: a parte do corpo que está dentro do líquido, em metros cúbicos. [p=0.2] {d}Gê é dez. [p=0.3] {e}Dê vezes vê é a massa do líquido deslocado. [p=0.1] Vezes gê, o peso dela."),
    dict(id="s07", block="formula", text="{a}Uma pedra de dois litros está toda debaixo d'água. [p=0.2] {b}Dois litros são dois milésimos de metro cúbico. [p=0.3] {c}Empuxo: mil vezes dois milésimos vezes dez, [p=0.1] {d}vinte newtons. [p=0.3] {e}Se a mesma pedra estiver no óleo, de densidade oitocentos, [p=0.1] {f}o empuxo cai para dezesseis newtons."),
    dict(id="s08", block="formula", text="{a}Volte ao ferro e ao isopor. [p=0.2] {b}Mesmo tamanho, totalmente submersos: [p=0.1] {c}o mesmo volume deslocado. [p=0.2] {d}Mesmo líquido, mesmo volume, mesmo empuxo. [p=0.3] {e}O que muda é o peso de cada um, [p=0.2] e a disputa entre peso e empuxo é {f}assunto da próxima aula."),
    dict(id="s09", block="formula", text="{a}E se só uma parte do corpo estiver dentro? [p=0.2] {b}Conta só essa parte. [p=0.3] {c}Um barco carregado afunda mais, desloca mais água [p=0.1] {d}e recebe mais empuxo."),
    dict(id="s10", block="formula", text="{a}E a profundidade, muda o empuxo? [p=0.2] {b}Depois que o corpo está todo dentro, não. [p=0.3] {c}Mais fundo, a pressão aumenta em cima e embaixo, na mesma medida. [p=0.2] {d}A diferença entre as faces continua igual, [p=0.1] e o empuxo também."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar a densidade do corpo na fórmula. [p=0.3] {b}Uma bola de ferro de um litro, com densidade de sete mil e oitocentos quilos por metro cúbico. [p=0.2] Quem usa a do ferro {c}acha setenta e oito newtons. [p=0.3] {d}Mas quem empurra é a água. [p=0.2] {e}Com mil, a da água: dez newtons. [p=0.2] {f}Setenta e oito newtons é o peso da bola, não o empuxo."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.2] {a}na água, cada litro deslocado dá dez newtons de empuxo. [p=0.3] Funciona porque {b}um litro de água tem um quilo, [p=0.1] {c}e um quilo pesa dez newtons. [p=0.3] {d}Três litros submersos, trinta newtons. [p=0.1] {e}Meio litro, cinco."),
    dict(id="s13", block="atalho", text="{a}Em outro líquido, ajuste: [p=0.2] {b}multiplique pela densidade em grama por centímetro cúbico. [p=0.3] {c}Oitocentos quilos por metro cúbico são zero vírgula oito grama por centímetro cúbico: [p=0.1] no óleo, cada litro dá oito newtons."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um objeto de três litros está totalmente mergulhado em óleo, [p=0.1] {b}de densidade oitocentos quilos por metro cúbico. [p=0.3] {c}Qual é o empuxo? [p=0.2] {d}E se só metade dele estivesse dentro do óleo?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Três litros são três milésimos de metro cúbico. [p=0.3] {b}Empuxo: oitocentos vezes três milésimos vezes dez, [p=0.1] {c}vinte e quatro newtons. [p=0.3] {d}Pelo atalho: três litros vezes oito newtons por litro, [p=0.1] vinte e quatro. [p=0.3] {e}Com metade dentro, só um litro e meio deslocado: [p=0.1] {f}doze newtons."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}o empuxo vem da pressão maior embaixo; [p=0.2] {b}ele vale o peso do líquido deslocado, dê vê gê; [p=0.2] e {c}dê é do líquido, e vê é só a parte que está dentro."),
    dict(id="s18", block="fim", text="Na próxima aula, {a}empuxo contra peso: [p=0.2] {b}quem afunda, quem boia, [p=0.1] e quanto de um iceberg fica escondido. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
