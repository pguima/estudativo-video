# Estudativo · QUI-SOL-003 — Concentração em g/L, porcentagem e ppm (Química · Soluções · Concentração, diluição e titulação).
# Habilidade: calcular a concentração em g/L, ler 0,9% no soro como 9 g/L e 2 ppm como 2 mg/L.
# Pré-requisitos: QUI-SOL-001, MAT-RAZ-001, MAT-POR-001, MAT-MED-002. Próxima: QUI-SOL-004 (concentração em mol/L).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Fatos: soro fisiológico = NaCl a 0,9% (m/v), 9 g por litro. 1 L de solução aquosa diluída pesa cerca de 1 kg = 1 000 000 mg,
# por isso 1 ppm = 1 mg/L. Contas: 20 ÷ 0,5 = 40; 20 ÷ 500 = 0,04 (erro); 0,9 × 10 = 9; questão 9 × 0,25 = 2,25; 6 ÷ 2 = 3.
# "Porcentagem em massa por volume" (m/v) é a do soro; a em massa (m/m) e a em volume (v/v) só são citadas no atalho.

TITULO = "Concentração em g/L, porcentagem e ppm"

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
    dict(id="s01", block="gancho", text="{a}No frasco de soro fisiológico está escrito: [p=0.1] {b}zero vírgula nove por cento de cloreto de sódio, o sal de cozinha. [p=0.3] {c}Quantos gramas de sal há num litro desse soro? [p=0.3] {d}Nove gramas. [p=0.2] E dá para ver isso em dois segundos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a concentração {b}em gramas por litro, [p=0.2] ler {c}a porcentagem do rótulo [p=0.2] e {d}as partes por milhão de um laudo de água."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}o soluto se dissolve no solvente, e os dois juntos formam a solução. [p=0.3] {b}Um litro tem mil mililitros, [p=0.1] {c}um grama tem mil miligramas, [p=0.2] e {d}cinco por cento são cinco em cada cem."),
    # concentração comum
    dict(id="s04", block="gl", text="Concentração diz {a}quanto soluto há em cada pedaço da solução. [p=0.3] {b}A mais usada é a concentração comum, em gramas por litro: [p=0.2] {c}quantos gramas de soluto há em cada litro de solução."),
    dict(id="s05", block="gl", text="A fórmula é {a}cê igual a eme dividido por vê. [p=0.3] {b}Cê é a concentração. [p=0.2] {c}Eme é a massa do soluto, em gramas. [p=0.2] {d}Vê é o volume da solução, em litros. [p=0.3] Vinte gramas de sal num litro de solução: [p=0.1] {e}vinte gramas por litro."),
    dict(id="s06", block="gl", text="{a}E vinte gramas em quinhentos mililitros? [p=0.3] {b}Primeiro, passe o volume para litros: [p=0.1] quinhentos mililitros são meio litro. [p=0.3] {c}Se meio litro tem vinte gramas, um litro tem o dobro: [p=0.1] {d}quarenta gramas por litro."),
    dict(id="s07", block="gl", text="{a}Repare: o volume é o da solução, não o da água. [p=0.2] {b}No laboratório, você dissolve o sal e completa com água até a marca do frasco."),
    # porcentagem
    dict(id="s08", block="por", text="{a}A porcentagem do soro funciona assim: [p=0.2] {b}zero vírgula nove por cento são zero vírgula nove grama de sal em cada cem mililitros de soro. [p=0.3] {c}Um litro tem dez vezes cem mililitros. [p=0.2] {d}Então são dez vezes zero vírgula nove: [p=0.1] {e}nove gramas por litro."),
    # ppm
    dict(id="s09", block="ppm", text="Quando o soluto é muito pouco, como um poluente na água, [p=0.2] usa-se {a}partes por milhão, que se escreve pê pê eme. [p=0.3] {b}É uma parte de soluto para cada milhão de partes de solução."),
    dict(id="s10", block="ppm", text="{a}Um litro de água pesa cerca de um quilo, que são um milhão de miligramas. [p=0.3] {b}Então um miligrama em cada litro é uma parte em um milhão. [p=0.3] {c}Na água, um pê pê eme é um miligrama por litro. [p=0.2] {d}Dois pê pê eme são dois miligramas por litro."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum: [p=0.2] {a}dividir pelo volume em mililitros. [p=0.3] Vinte gramas em quinhentos mililitros, [p=0.1] e a pessoa faz {b}vinte dividido por quinhentos: [p=0.1] {c}zero vírgula zero quatro grama por litro."),
    dict(id="s12", block="erro", text="{a}Confira com o bom senso: [p=0.2] meio litro tem vinte gramas, [p=0.1] {b}e um litro teria só quatro centésimos de grama? [p=0.3] {c}Não pode. [p=0.2] Gramas por litro pedem o volume em litros: [p=0.1] {d}a resposta certa é quarenta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho do rótulo: [p=0.2] {a}porcentagem vezes dez dá gramas por litro. [p=0.3] {b}Zero vírgula nove por cento, nove gramas por litro. [p=0.2] {c}Cinco por cento, cinquenta gramas por litro. [p=0.3] {d}E na água, o pê pê eme já é o número de miligramas por litro."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a porcentagem conta gramas em cem mililitros, [p=0.1] e um litro é dez vezes isso. [p=0.3] {b}Não compensa quando a porcentagem é em massa, como numa liga de metal, [p=0.2] ou em volume, como o álcool de uma bebida. [p=0.2] Aí ela não conta gramas em cada cem mililitros."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Um frasco tem duzentos e cinquenta mililitros de soro a zero vírgula nove por cento. [p=0.2] {b}Qual é a concentração em gramas por litro? [p=0.2] {c}E quantos gramas de sal há no frasco? [p=0.3] {d}Outra: um laudo diz que dois litros de água de poço têm seis miligramas de nitrato. [p=0.2] {e}Quantos pê pê eme são?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}Pelo atalho, zero vírgula nove por cento são nove gramas por litro. [p=0.3] {b}O frasco tem duzentos e cinquenta mililitros, que são zero vírgula vinte e cinco litro. [p=0.2] {c}Nove vezes zero vírgula vinte e cinco dá dois vírgula vinte e cinco gramas de sal."),
    dict(id="s18", block="resposta", text="No laudo, {a}seis miligramas em dois litros: [p=0.1] {b}seis dividido por dois dá três miligramas por litro. [p=0.3] {c}Na água, são três pê pê eme."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}concentração comum é a massa do soluto dividida pelo volume da solução em litros, [p=0.2] {b}porcentagem vezes dez dá gramas por litro, [p=0.1] e {c}na água, pê pê eme é miligrama por litro."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai trocar os gramas por {a}mols, [p=0.2] e calcular {b}a concentração em mol por litro, a que o laboratório mais usa. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
