# Estudativo · FIS-EGF-009 — Praticando: hidrostática (Física · Equilíbrio, Gravitação e Fluidos · Hidrostática · prática).
# Habilidade: resolver questões de pressão, prensa hidráulica e empuxo.
# Pré-requisitos: FIS-EGF-004, FIS-EGF-005, FIS-EGF-006, FIS-EGF-007, FIS-EGF-008. Próxima: FIS-EGF-010.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula.
# g = 10 m/s²; 1 atm ≈ 10⁵ Pa. Contas: 500 N/1 cm² = 5 × 10⁶ Pa = 50 atm; 250 cm² → 250 vezes menos; 0,8·h = 1·12 → h = 15 cm;
# diâmetros 2 e 10 → 5² = 25 → 5.000/25 = 200 N; 50 − 30 = 20 N → 2 L → 5 kg/2 L = 2,5 g/cm³; gelo 0,9: água 90%, óleo 0,8 afunda.

TITULO = "Praticando: hidrostática"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações com líquidos e pressão, [p=0.1] criadas para esta aula: [p=0.2] {b}do salto alto [p=0.1] {c}até um cubo de gelo que afunda. [p=0.3] Em cada uma, {d}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}pressão, força sobre área; [p=0.2] {b}Stevin, pê zero mais dê gê agá; [p=0.2] {c}Pascal, efe um sobre á um igual a efe dois sobre á dois; [p=0.2] e {d}empuxo, dê vê gê. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: salto alto
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] {b}Uma pessoa de cinquenta quilos, de salto fino, [p=0.1] {c}apoia o peso todo num salto de um centímetro quadrado. [p=0.3] {d}Qual é a pressão no chão, em pascal e em atmosferas? [p=0.2] {e}E com um tênis de duzentos e cinquenta centímetros quadrados?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}O peso: quinhentos newtons. [p=0.2] {b}Quinhentos sobre um: quinhentos newtons por centímetro quadrado. [p=0.2] {c}Vezes dez mil: [p=0.1] {d}cinco milhões de pascals. [p=0.3] {e}Divida por cem mil: cinquenta atmosferas. [p=0.2] É por isso que o salto fino marca o piso de madeira. [p=0.3] {f}No tênis, a área é duzentas e cinquenta vezes maior, [p=0.1] {g}e a pressão, duzentas e cinquenta vezes menor: [p=0.1] vinte mil pascals, dois décimos de atmosfera."),
    # situação 2: tubo em U
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] {b}Num tubo em U, há água e óleo. [p=0.2] {c}A água fica doze centímetros acima da linha da separação. [p=0.2] {d}O óleo tem densidade zero vírgula oito grama por centímetro cúbico. [p=0.3] {e}Qual é a altura da coluna de óleo?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] {a}Na linha da separação, a pressão é a mesma dos dois lados. [p=0.2] {b}Dê vezes agá do óleo igual a dê vezes agá da água. [p=0.3] {c}Zero vírgula oito vezes agá, igual a um vezes doze. [p=0.2] {d}Agá é doze dividido por zero vírgula oito: [p=0.1] {e}quinze centímetros. [p=0.2] {f}O óleo, menos denso, fica mais alto. [p=0.2] Confira: zero vírgula oito vezes quinze dá doze."),
    # situação 3: prensa com diâmetros
    dict(id="s09", block="questao3", text="{a}Situação três. [p=0.2] {b}Numa prensa hidráulica, o pistão pequeno tem dois centímetros de diâmetro, [p=0.1] {c}e o grande, dez. [p=0.3] {d}Que força no pistão pequeno levanta uma carga de cinco mil newtons?"),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="Vamos lá. [p=0.2] {a}Os diâmetros: dez sobre dois, cinco vezes. [p=0.2] {b}As áreas: cinco ao quadrado, vinte e cinco vezes. [p=0.3] {c}A força: cinco mil dividido por vinte e cinco, [p=0.1] {d}duzentos newtons. [p=0.3] {e}Quem dividisse por cinco acharia mil newtons: [p=0.1] cinco vezes mais força do que precisa."),
    # situação 4: peso aparente
    dict(id="s12", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Numa balança de gancho, um bloco marca cinquenta newtons no ar. [p=0.2] {c}Mergulhado todo na água, marca trinta. [p=0.3] {d}Qual é o volume do bloco? [p=0.2] {e}E a densidade dele?"),
    dict(id="s13", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta4", text="Vamos lá. [p=0.2] {a}O que sumiu da balança foi o empuxo: [p=0.1] {b}cinquenta menos trinta, vinte newtons. [p=0.3] {c}Na água, cada litro deslocado dá dez newtons: [p=0.1] {d}o volume é de dois litros. [p=0.3] {e}A massa: cinquenta newtons são cinco quilos. [p=0.2] {f}Densidade: cinco quilos em dois litros, [p=0.1] {g}dois vírgula cinco quilos por litro, [p=0.1] que é o mesmo que dois vírgula cinco gramas por centímetro cúbico."),
    # atalho
    dict(id="s15", block="atalho", text="Guarde o atalho dessa: [p=0.2] {a}na água, os newtons que somem da balança, divididos por dez, dão o volume em litros. [p=0.3] {b}Peso no ar dividido pelo que sumiu: [p=0.1] {c}cinquenta sobre vinte, dois vírgula cinco, a densidade em grama por centímetro cúbico. [p=0.3] Funciona porque {d}o peso tem a densidade do corpo, e o empuxo, a da água, que vale um. [p=0.2] {e}Em outro líquido, multiplique pela densidade dele."),
    # situação 5: gelo no óleo
    dict(id="s16", block="questao5", text="{a}Última situação. [p=0.2] {b}Um cubo de gelo, de densidade zero vírgula nove, [p=0.1] {c}cai num copo de água [p=0.1] {d}e outro cai num copo de óleo, de zero vírgula oito. [p=0.3] {e}O que acontece em cada copo?"),
    dict(id="s17", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta5", text="Vamos lá. [p=0.2] {a}Na água: zero vírgula nove é menor que um, [p=0.1] {b}o gelo boia, [p=0.1] {c}com nove décimos dentro. [p=0.3] {d}No óleo: zero vírgula nove é maior que zero vírgula oito. [p=0.2] {e}O gelo é mais denso que o óleo, [p=0.1] {f}e afunda. [p=0.3] No copo de óleo, o gelo vai para o fundo: [p=0.1] parece truque, mas é só densidade."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}área em metro quadrado para dar pascal, e na prensa, a mesma unidade dos dois lados; [p=0.2] {b}na mesma altura do mesmo líquido, a mesma pressão; [p=0.2] {c}razão dos diâmetros ao quadrado na prensa; [p=0.2] e {d}densidade decide quem boia."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}o líquido entra em movimento: [p=0.2] {b}vazão, e por que a água acelera quando o cano afina. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
