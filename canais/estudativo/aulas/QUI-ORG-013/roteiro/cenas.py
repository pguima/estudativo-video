# Estudativo · QUI-ORG-013 — Solubilidade, sabões e detergentes (Química · Química Orgânica · Propriedades físicas e isomeria).
# Habilidade: dizer por que etanol mistura com água e hexano não, medir o álcool da gasolina e explicar como o sabão remove a gordura.
# Pré-requisitos: QUI-ORG-012, QUI-LIG-008 (semelhante dissolve semelhante), QUI-INO-003 (sais), MAT-POR-003 (quantos por cento).
# Próxima: QUI-ORG-014 (isomeria plana). Marcas: {cue} animação · [p=0.2] pausa. COO⁻ = "cê ó ó menos"; SO₃⁻ = "esse ó três menos".
# Fatos: etanol miscível com água; hexano imiscível e menos denso (0,66 g/mL); butan-1-ol pouco solúvel (≈ 70 g/L), hexan-1-ol
# quase nada (≈ 6 g/L). Gasolina comum: 30% de etanol desde ago/2025 (CONFERIR com o usuário). Teste da proveta (ANP): 50 mL de
# gasolina + 50 mL de solução de NaCl; aumento da fase aquosa = etanol; 65 mL → 15 mL → 15/50 = 0,30 = 30%. Sabão = sal de sódio de
# ácido graxo (a saponificação fica para outra aula); micela; detergente = sulfonato, funciona em água dura (Ca²⁺ forma nata com sabão);
# cadeia linear = biodegradável. Questão: 63 mL → 13 mL → 26%. Questão inédita, criada para esta aula.

TITULO = "Solubilidade, sabões e detergentes"

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
    dict(id="s01", block="gancho", text="{a}Etanol e água se misturam em qualquer proporção. [p=0.2] {b}Hexano e água, quase nada. [p=0.3] {c}E o sabão consegue juntar a água com a gordura. [p=0.2] {d}As três coisas têm a mesma explicação."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar {b}por que o etanol se mistura com a água e o hexano não, [p=0.2] {c}medir o álcool da gasolina [p=0.2] e {d}entender como o sabão tira a gordura."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula de solubilidade: [p=0.2] {a}semelhante dissolve semelhante. [p=0.2] {b}O polar se mistura com o polar, [p=0.1] {c}e o apolar, com o apolar. [p=0.3] {d}E da aula passada: [p=0.1] o ó agá faz ligação de hidrogênio."),
    # etanol × hexano
    dict(id="s04", block="mistura", text="{a}O etanol tem duas partes. [p=0.2] {b}O ó agá, polar, faz ligação de hidrogênio com a água. [p=0.2] {c}A cadeia de dois carbonos, apolar, é curta. [p=0.3] {d}A parte polar vence, e o etanol se mistura com a água."),
    dict(id="s05", block="mistura", text="{a}O hexano só tem carbono e hidrogênio: [p=0.1] é todo apolar. [p=0.2] {b}As moléculas de água preferem ficar juntas, presas pelas ligações de hidrogênio, [p=0.1] {c}e deixam o hexano de fora. [p=0.3] {d}Ele forma uma camada separada, por cima, porque é mais leve que o mesmo volume de água, como o óleo."),
    dict(id="s06", block="mistura", text="{a}Quanto maior a cadeia, menos o álcool se mistura com a água. [p=0.2] {b}O butan um ol já se mistura só um pouco. [p=0.2] {c}O hexan um ol, quase nada: [p=0.1] {d}o mesmo ó agá, mas com uma parte apolar comprida demais."),
    # gasolina
    dict(id="s07", block="gasolina", text="{a}Essa disputa entre as partes serve para medir o álcool da gasolina. [p=0.2] {b}A gasolina comum leva etanol, [p=0.1] e o governo define quanto: [p=0.1] {c}hoje, trinta por cento."),
    dict(id="s08", block="gasolina", text="{a}O teste é feito numa proveta, um tubo de vidro com marcas de volume. [p=0.2] {b}Ponha cinquenta mililitros de gasolina [p=0.1] {c}e cinquenta de água com um pouco de sal, que ajuda as camadas a se separarem bem. [p=0.2] {d}Agite e espere separar."),
    dict(id="s09", block="gasolina", text="{a}O etanol prefere a água, porque faz ligação de hidrogênio com ela. [p=0.2] {b}Ele sai da gasolina e vai para a camada de baixo. [p=0.3] {c}Se a água subiu de cinquenta para sessenta e cinco mililitros, [p=0.1] {d}entraram quinze mililitros de etanol."),
    dict(id="s10", block="gasolina", text="{a}Quanto é quinze de cinquenta, em porcentagem? [p=0.2] {b}Quinze dividido por cinquenta dá zero vírgula três: [p=0.1] {c}trinta por cento."),
    # sabão
    dict(id="s11", block="sabao", text="{a}E o sabão? [p=0.2] {b}Ele é o sal de sódio de um ácido graxo, [p=0.1] um ácido carboxílico de cadeia bem longa. [p=0.2] {c}Ele vem da reação da gordura com a soda cáustica, assunto de outra aula."),
    dict(id="s12", block="sabao", text="{a}A molécula do sabão tem cauda e cabeça. [p=0.2] {b}A cauda é uma cadeia comprida de carbonos: [p=0.1] apolar, ela se mistura com a gordura. [p=0.2] {c}A cabeça é o cê ó ó menos, com o sódio: [p=0.1] com carga, ela gosta da água."),
    dict(id="s13", block="sabao", text="{a}Na louça, as caudas entram na gordura, [p=0.1] {b}e as cabeças ficam para fora, viradas para a água. [p=0.2] {c}Elas formam uma bolinha com a gordura presa dentro: a micela. [p=0.3] {d}A água leva a micela embora, e a gordura vai junto."),
    dict(id="s14", block="sabao", text="{a}O detergente faz o mesmo, com outra cabeça: [p=0.1] {b}o grupo sulfonato, esse ó três menos. [p=0.2] {c}A vantagem é que ele funciona até na água dura, cheia de cálcio, [p=0.1] onde o sabão forma uma nata e perde a força. [p=0.3] {d}E o detergente de cadeia sem galhos é biodegradável: [p=0.1] as bactérias conseguem desmontá-lo."),
    # erro comum
    dict(id="s15", block="erro", text="{a}O erro mais comum é dizer que o sabão dissolve a gordura na água. [p=0.3] {b}A gordura não se dissolve: [p=0.1] {c}ela continua inteira, presa dentro das micelas. [p=0.2] {d}O sabão é a ponte entre a água e a gordura."),
    # atalho
    dict(id="s16", block="atalho", text="{a}O atalho do teste da gasolina: [p=0.2] {b}com cinquenta mililitros de gasolina, [p=0.1] a porcentagem de etanol é o dobro do que a água subiu. [p=0.3] {c}Subiu quinze? [p=0.1] Trinta por cento. [p=0.2] {d}Subiu doze? [p=0.1] Vinte e quatro."),
    dict(id="s17", block="atalho", text="{a}Funciona porque cinquenta é a metade de cem: [p=0.1] dobrar transforma a parte em porcentagem. [p=0.3] {b}Não vale com outro volume de gasolina. [p=0.2] {c}Com cem mililitros, o aumento já é a porcentagem. [p=0.2] {d}Nos outros casos, divida o aumento pelo volume de gasolina."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}No teste, cinquenta mililitros de gasolina foram agitados com cinquenta de água com sal. [p=0.2] {b}No fim, a camada de água marcou sessenta e três mililitros. [p=0.3] {c}Qual é a porcentagem de etanol nessa gasolina?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="{a}A água subiu de cinquenta para sessenta e três: [p=0.1] {b}entraram treze mililitros de etanol. [p=0.3] {c}Pelo atalho, o dobro de treze dá vinte e seis. [p=0.2] {d}A gasolina tem vinte e seis por cento de etanol. [p=0.3] {e}Na conta completa: treze dividido por cinquenta dá zero vírgula vinte e seis."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.1] {a}com cadeia curta, vence o ó agá, e o álcool vai para a água; [p=0.2] {b}com cadeia longa, vence a parte apolar. [p=0.2] {c}O hexano fica de fora, [p=0.1] e {d}o sabão segura os dois lados ao mesmo tempo."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai ver moléculas com a mesma fórmula e desenhos diferentes: [p=0.2] {a}a isomeria plana. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
