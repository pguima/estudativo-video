# Estudativo · QUI-CAL-013 — Volume molar e estequiometria com gases (Química · Cálculos Químicos · Estudo dos gases).
# Habilidade: usar 22,4 L por mol nas CNTP e calcular que 46 g de etanol queimados liberam 44,8 L de CO₂.
# Pré-requisitos: QUI-CAL-005, QUI-CAL-012. Próxima: QUI-CAL-014 (misturas gasosas e pressão parcial).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; CNTP lido "cê ene tê pê". Questão inédita.
# Contas: 0,082 · 273 / 1 = 22,386 ≈ 22,4 L; 1 mol de H₂ (2 g), O₂ (32 g) e CO₂ (44 g); C₂H₆O + 3 O₂ → 2 CO₂ + 3 H₂O;
# 46 g → 2 · 22,4 = 44,8 L; água: 3 mol = 54 g ≈ 54 mL de líquido (não 67,2 L). Questão: 92 g = 2 mol → 6 mol O₂ → 134,4 L.
# Fato: algumas provas usam CNTP a 1 bar (22,7 L) ou 25 °C (24,5 L); o roteiro manda usar o que a prova der.

TITULO = "Volume molar e estequiometria com gases"

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
    dict(id="s01", block="gancho", text="{a}Um balão com dois gramas de hidrogênio, [p=0.1] {b}outro com trinta e dois gramas de oxigênio [p=0.1] {c}e outro com quarenta e quatro gramas de gás carbônico. [p=0.3] {d}Na mesma temperatura e pressão, os três têm exatamente o mesmo tamanho. [p=0.2] {e}Por quê?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}usar o volume molar nas cê ene tê pê, vinte e dois vírgula quatro litros, [p=0.2] e {c}calcular volumes de gás numa reação, [p=0.2] com um {d}atalho que só vale para gases."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a conta de massa para massa numa equação, [p=0.2] e {c}a equação pê vê igual a ene erre tê. [p=0.3] Se faltar alguma, procure no canal."),
    # volume molar
    dict(id="s04", block="molar", text="{a}Cada balão tem um mol de gás. [p=0.3] {b}Em pê vê igual a ene erre tê, [p=0.1] o volume é ene erre tê dividido por pê. [p=0.2] {c}Nenhuma letra diz qual é o gás. [p=0.3] {d}Mesmos mols, mesma temperatura e mesma pressão: [p=0.1] {e}mesmo volume, para qualquer gás."),
    dict(id="s05", block="molar", text="{a}O volume de um mol de gás se chama volume molar. [p=0.3] {b}A prova costuma usar as cê ene tê pê: [p=0.1] {c}condições normais de temperatura e pressão, [p=0.1] {d}zero grau Celsius e uma atmosfera."),
    dict(id="s06", block="molar", text="{a}Nessas condições, o volume de um mol é [p=0.1] {b}um vezes zero vírgula zero oito dois vezes duzentos e setenta e três, [p=0.1] dividido por um. [p=0.3] {c}Dá cerca de vinte e dois vírgula quatro litros. [p=0.3] {d}Fora dessas condições, o valor muda: [p=0.1] a prova avisa, ou você usa pê vê igual a ene erre tê."),
    # etanol
    dict(id="s07", block="etanol", text="{a}Volte à queima do etanol: [p=0.1] cê dois agá seis ó mais três ó dois forma dois cê ó dois mais três agá dois ó. [p=0.3] {b}Quarenta e seis gramas de etanol, um mol, [p=0.1] {c}formam dois mols de cê ó dois. [p=0.3] {d}Nas cê ene tê pê, cada mol de gás ocupa vinte e dois vírgula quatro litros: [p=0.1] {e}dois vezes vinte e dois vírgula quatro dá quarenta e quatro vírgula oito litros."),
    dict(id="s08", block="etanol", text="{a}Embaixo da equação, o gás pode vir em litros e o resto em gramas. [p=0.2] {b}Quarenta e seis gramas de etanol para quarenta e quatro vírgula oito litros de gás carbônico. [p=0.3] {c}A regra de três funciona do mesmo jeito."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é {a}usar os vinte e dois vírgula quatro litros para o que não é gás. [p=0.3] {b}A água dessa reação, nas cê ene tê pê, não é gás. [p=0.2] {c}Três mols de água não ocupam sessenta e sete vírgula dois litros: [p=0.1] {d}cabem em pouco mais de cinquenta mililitros. [p=0.3] {e}O volume molar vale só para gases."),
    # atalho
    dict(id="s10", block="atalho", text="O atalho: [p=0.1] {a}entre gases, na mesma temperatura e pressão, [p=0.1] {b}a proporção dos volumes é a dos coeficientes. [p=0.3] {c}Na equação, três ó dois geram dois cê ó dois: [p=0.1] {d}três litros de oxigênio dão dois litros de gás carbônico. [p=0.2] {e}Nem precisa do vinte e dois vírgula quatro."),
    dict(id="s11", block="atalho", text="{a}Funciona porque o volume de um gás é proporcional aos mols. [p=0.3] {b}Não compensa quando uma das substâncias é sólida ou líquida, [p=0.1] {c}como o etanol e a água: [p=0.1] aí, passe pelo mol."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] {a}Quantos litros de oxigênio, nas cê ene tê pê, [p=0.1] {b}são gastos para queimar noventa e dois gramas de etanol?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Vamos lá. [p=0.2] {a}Noventa e dois gramas são dois mols de etanol. [p=0.3] {b}Cada mol de etanol gasta três de ó dois: [p=0.1] {c}são seis mols de oxigênio. [p=0.3] {d}Seis vezes vinte e dois vírgula quatro [p=0.1] {e}dá cento e trinta e quatro vírgula quatro litros."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: [p=0.1] {a}nas cê ene tê pê, um mol de qualquer gás ocupa vinte e dois vírgula quatro litros; [p=0.2] {b}e, entre gases, os volumes seguem os coeficientes."),
    dict(id="s16", block="fim", text="Na próxima aula, os gases se misturam, [p=0.1] e você descobre {a}quanto da pressão do ar vem do oxigênio. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
