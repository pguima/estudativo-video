# Estudativo · QUI-MIS-006 — Separar sólidos: da peneira ao ímã (Química · Matéria e Misturas · Separação de misturas).
# Habilidade: escolher entre catação, peneiração, ventilação, levigação, flotação, separação magnética e dissolução
# fracionada olhando a diferença entre os sólidos.
# Pré-requisitos: QUI-MIS-002, MAT-RAZ-017. Próxima: QUI-MIS-007 (decantar, filtrar e centrifugar).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: densidade da água 1 g/cm³; ouro cerca de 19 g/cm³; areia cerca de 2,6 g/cm³; isopor e serragem boiam (menos de
# 1 g/cm³). Levigação = corrente de água leva o menos denso (bateia); ventilação = corrente de ar; flotação = líquido
# parado em que um boia e o outro afunda (também na reciclagem de plásticos). Filtração é a próxima aula; evaporação e
# estados físicos não estão em "Já ensinado": citados como assunto de outra aula.

TITULO = "Separar sólidos: da peneira ao ímã"

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
    dict(id="s01", block="gancho", text="{a}O garimpeiro separa o ouro da areia com uma bacia e um pouco de água. [p=0.3] {b}Sem máquina e sem produto nenhum. [p=0.3] {c}Como isso funciona?"),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai conhecer {b}sete jeitos de separar sólidos misturados [p=0.2] e {c}a pergunta que escolhe o jeito certo em qualquer questão."),
    # lembrete
    dict(id="s03", block="lembrete", text="Dois lembretes. [p=0.2] {a}Mistura heterogênea é aquela em que dá para ver as partes. [p=0.3] {b}E densidade é massa dividida por volume: [p=0.1] {c}o que tem densidade menor que a da água boia; [p=0.1] {d}o que tem maior afunda."),
    # princípio
    dict(id="s04", block="ideia", text="Toda separação usa {a}uma diferença entre os componentes. [p=0.3] Se fossem iguais em tudo, não daria para separar. [p=0.3] Então a pergunta é sempre a mesma: {b}em que esses sólidos são diferentes?"),
    dict(id="s05", block="ideia", text="Para sólidos, as respostas mais comuns são quatro: {a}tamanho, [p=0.1] {b}densidade, [p=0.1] {c}ímã [p=0.1] {d}e dissolver na água. [p=0.3] Cada uma leva a um método."),
    # tamanho
    dict(id="s06", block="tamanho", text="{a}Diferença de tamanho ou de aparência. [p=0.3] {b}Se as partes são grandes e poucas, você separa com a mão ou com uma pinça: [p=0.1] {c}é a catação, como catar as pedrinhas do feijão."),
    dict(id="s07", block="tamanho", text="{a}Se são muitos grãos de tamanhos diferentes, use uma peneira: [p=0.1] {b}é a peneiração, também chamada de tamisação. [p=0.3] {c}Os grãos pequenos passam pelos furos, [p=0.1] {d}os grandes ficam. [p=0.2] É o pedreiro peneirando areia."),
    # densidade
    dict(id="s08", block="densidade", text="{a}Diferença de densidade. [p=0.3] Aqui há três métodos, e o que muda entre eles é o que empurra os grãos. [p=0.3] {b}Com uma corrente de ar, é a ventilação: [p=0.2] {c}o vento leva a casca do arroz ou do café, pouco densa, [p=0.1] {d}e o grão, mais denso, cai."),
    dict(id="s09", block="densidade", text="{a}Com uma corrente de água, é a levigação. [p=0.3] É o garimpeiro: [p=0.1] {b}ele gira a bacia com água, [p=0.1] {c}a água arrasta a areia, menos densa, [p=0.2] {d}e o ouro, quase vinte vezes mais denso que a água, fica no fundo."),
    dict(id="s10", block="densidade", text="{a}Num líquido parado, é a flotação. [p=0.3] Escolhe-se um líquido em que {b}um sólido boia {c}e o outro afunda. [p=0.3] {d}Serragem e areia na água: a serragem boia, a areia vai para o fundo. [p=0.3] {e}A reciclagem separa tipos de plástico assim."),
    # ímã e dissolução
    dict(id="s11", block="outros", text="{a}Um dos sólidos é atraído por ímã? [p=0.2] {b}Separação magnética. [p=0.3] {c}O ímã puxa a limalha de ferro, que é ferro em pó, e a areia fica. [p=0.3] {d}Nas usinas de lixo, ímãs gigantes tiram as latas de aço."),
    dict(id="s12", block="outros", text="{a}Um dos sólidos dissolve na água e o outro não? [p=0.2] {b}Dissolução fracionada. [p=0.3] {c}Ponha sal com areia na água e mexa: [p=0.1] {d}o sal dissolve, a areia não. [p=0.3] {e}Depois, é tirar a areia da água e tirar a água do sal, [p=0.1] e isso é assunto das próximas aulas."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova é {a}a pergunta da diferença. [p=0.3] {b}Tamanho: catação ou peneira. [p=0.2] {c}Densidade: ar, água correndo ou líquido parado. [p=0.2] {d}Ímã: separação magnética. [p=0.2] {e}Dissolve: dissolução fracionada."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a prova quase nunca pede o nome solto: [p=0.1] ela descreve a situação. [p=0.3] {b}Achada a diferença, sobram uma ou duas opções. [p=0.3] {c}Não basta quando a mistura tem três componentes: [p=0.1] aí, cada diferença vira um passo, e a ordem importa. [p=0.2] Isso fica para outra aula."),
    # erro
    dict(id="s15", block="erro", text="O erro mais comum é {a}achar que, na levigação, o que fica é o mais leve. [p=0.3] É o contrário. [p=0.2] {b}A água leva o que é menos denso. [p=0.2] {c}Na bacia do garimpeiro, quem fica é o ouro, [p=0.1] {d}o mais denso de todos."),
    dict(id="s16", block="erro", text="{a}E não troque ventilação por levigação. [p=0.2] {b}As duas usam densidade; [p=0.1] {c}muda só o que corre: ar ou água."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Que método separa cada mistura? [p=0.3] {a}Um: grãos de café secos, misturados com as cascas soltas. [p=0.2] {b}Dois: bolinhas de isopor misturadas com areia, e você só tem um balde de água. [p=0.2] {c}Três: açúcar misturado com areia."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="{a}Café: a diferença é a densidade, e a casca é pouco densa. [p=0.2] {b}Uma corrente de ar resolve: ventilação."),
    dict(id="s20", block="resposta", text="{a}Isopor e areia, com um balde de água: também densidade. [p=0.2] {b}Na água, o isopor boia e a areia afunda: flotação. [p=0.3] {c}Açúcar e areia: o açúcar dissolve na água e a areia não. [p=0.2] {d}Dissolução fracionada. [p=0.3] {e}Quem pensou em peneira para o açúcar errou: os grãos têm quase o mesmo tamanho."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.1] {a}separar é usar uma diferença. [p=0.2] {b}Ache a diferença, [p=0.1] {c}e o método aparece."),
    dict(id="s22", block="fim", text="Na próxima aula, você separa sólido de líquido: [p=0.2] {a}decantar, filtrar e centrifugar, [p=0.1] e ainda separar água e óleo. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
