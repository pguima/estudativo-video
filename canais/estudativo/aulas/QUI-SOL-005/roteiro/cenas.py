# Estudativo · QUI-SOL-005 — Diluição e mistura de soluções (Química · Soluções · Concentração, diluição e titulação).
# Habilidade: usar C₁V₁ = C₂V₂ para diluir e calcular a concentração final ao juntar duas soluções do mesmo soluto.
# Pré-requisitos: QUI-SOL-004, MAT-EQU-011. Próxima: QUI-SOL-006 (titulação).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Contas: gancho 0,5 × 100 = 50 = C₂ × 500 → C₂ = 0,1 mol/L (volume × 5, concentração ÷ 5); água posta = 500 − 100 = 400 mL.
# Preparar: 2 × V₁ = 0,5 × 500 → V₁ = 125 mL de estoque + 375 mL de água.
# Mistura: 200 mL de 0,5 mol/L (0,1 mol) + 300 mL de 1,0 mol/L (0,3 mol) = 0,4 mol em 0,5 L → 0,8 mol/L; erro: 0,5 + 1,0 = 1,5.
# Questão: 250 mL de 0,8 mol/L até 1 L → ×4 → 0,2 mol/L; depois + 3 L de 0,6 mol/L: (0,2 + 1,8) ÷ 4 L = 0,5 mol/L (a média simples daria 0,4).
# Soluto do exemplo da mistura = açúcar (ácido e base ficam para a titulação, na próxima aula).

TITULO = "Diluição e mistura de soluções"

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
    dict(id="s01", block="gancho", text="{a}Cem mililitros de uma solução de sal com zero vírgula cinco mol por litro. [p=0.3] {b}Você completa com água até quinhentos mililitros. [p=0.3] {c}Nenhum grão de sal entrou ou saiu. [p=0.2] {d}A concentração cai para quanto? [p=0.3] {e}Para zero vírgula um mol por litro. E a conta cabe numa linha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}diluir uma solução com uma fórmula só [p=0.2] e {c}calcular a concentração de duas soluções misturadas."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}concentração em mol por litro é o número de mols dividido pelo volume. [p=0.3] {b}Então o número de mols é a concentração vezes o volume. [p=0.3] E {c}numa fórmula, você isola uma letra fazendo a mesma conta dos dois lados."),
    # diluição
    dict(id="s04", block="diluir", text="{a}Diluir é acrescentar solvente. [p=0.2] {b}O volume cresce, [p=0.1] {c}mas o soluto continua o mesmo: [p=0.1] {d}só se espalha num espaço maior. [p=0.3] {e}Por isso a concentração cai."),
    dict(id="s05", block="diluir", text="{a}Antes, a quantidade de soluto é a concentração inicial vezes o volume inicial. [p=0.3] {b}Depois, é a concentração final vezes o volume final. [p=0.3] {c}Como o soluto não mudou, as duas contas são iguais: [p=0.2] {d}cê um vê um igual a cê dois vê dois."),
    dict(id="s06", block="diluir", text="No começo da aula: [p=0.1] {a}zero vírgula cinco vezes cem dá cinquenta. [p=0.2] {b}Do outro lado, cê dois vezes quinhentos. [p=0.3] {c}Divida os dois lados por quinhentos: [p=0.1] {d}cinquenta dividido por quinhentos dá zero vírgula um mol por litro."),
    dict(id="s07", block="diluir", text="{a}Os volumes podem ficar em mililitros, desde que os dois estejam na mesma unidade. [p=0.3] {b}E a concentração pode ser em mol por litro ou em gramas por litro: [p=0.2] só não misture as duas."),
    # preparar
    dict(id="s08", block="preparar", text="{a}A fórmula também ensina a preparar. [p=0.2] {b}Você tem um estoque com dois mol por litro [p=0.2] e {c}quer quinhentos mililitros com zero vírgula cinco mol por litro. [p=0.3] {d}Dois vezes vê um igual a zero vírgula cinco vezes quinhentos, que dá duzentos e cinquenta. [p=0.2] {e}Vê um dá cento e vinte e cinco mililitros."),
    dict(id="s09", block="preparar", text="{a}Pegue cento e vinte e cinco mililitros do estoque [p=0.1] e {b}complete com água até quinhentos. [p=0.3] {c}Você pôs trezentos e setenta e cinco mililitros de água."),
    # mistura
    dict(id="s10", block="mistura", text="E quando você junta duas soluções do mesmo soluto? [p=0.2] {a}Duzentos mililitros de uma solução de açúcar com zero vírgula cinco mol por litro, [p=0.2] {b}mais trezentos mililitros com um mol por litro. [p=0.3] {c}Não há reação, então os mols se somam, e os volumes também."),
    dict(id="s11", block="mistura", text="{a}Na primeira, zero vírgula cinco vezes zero vírgula dois litro dá zero vírgula um mol. [p=0.3] {b}Na segunda, um vezes zero vírgula três dá zero vírgula três mol. [p=0.3] {c}Juntos, zero vírgula quatro mol, [p=0.1] {d}em meio litro. [p=0.3] {e}Zero vírgula quatro dividido por zero vírgula cinco dá zero vírgula oito mol por litro."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum: [p=0.2] {a}somar as concentrações. [p=0.3] {b}Zero vírgula cinco mais um dá um vírgula cinco, [p=0.1] e a pessoa marca isso. [p=0.3] {c}Mas a mistura ficaria mais concentrada que as duas soluções que você juntou. [p=0.2] {d}Impossível. [p=0.2] {e}Some os mols, não as concentrações."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, dois atalhos de prova. [p=0.2] {a}Na diluição, veja quantas vezes o volume cresceu, [p=0.1] e {b}divida a concentração pelo mesmo número. [p=0.3] {c}De cem para quinhentos, cresceu cinco vezes: [p=0.1] {d}zero vírgula cinco dividido por cinco dá zero vírgula um. [p=0.3] Funciona porque o mesmo soluto se espalha num volume cinco vezes maior. [p=0.2] {e}Não compensa quando a conta não é inteira, como de trezentos para setecentos mililitros: [p=0.1] aí use a fórmula."),
    dict(id="s14", block="atalho", text="{a}Na mistura, o resultado fica sempre entre as duas concentrações, [p=0.2] {b}mais perto da que tem mais volume. [p=0.3] {c}Zero vírgula oito está entre zero vírgula cinco e um inteiro, mais perto do um inteiro. [p=0.3] {d}Não compensa quando os solutos reagem, como um ácido com uma base: [p=0.2] aí parte deles some, e isso é assunto da próxima aula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Duzentos e cinquenta mililitros de uma solução de sal com zero vírgula oito mol por litro [p=0.1] {b}são diluídos até um litro. [p=0.3] {c}Qual é a nova concentração? [p=0.3] {d}Depois, você junta essa solução a três litros de outra, do mesmo sal, com zero vírgula seis mol por litro. [p=0.2] {e}Qual é a concentração final?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}De duzentos e cinquenta mililitros para um litro, o volume cresceu quatro vezes. [p=0.2] {b}Zero vírgula oito dividido por quatro dá zero vírgula dois mol por litro."),
    dict(id="s18", block="resposta", text="Na mistura, {a}um litro com zero vírgula dois tem zero vírgula dois mol. [p=0.2] {b}Três litros com zero vírgula seis têm um vírgula oito mol. [p=0.3] {c}Juntos, dois mols em quatro litros: [p=0.1] {d}dá zero vírgula cinco mol por litro. [p=0.3] {e}Ficou entre as duas, mais perto da que tinha mais volume."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}na diluição, cê um vê um igual a cê dois vê dois, porque o soluto não muda. [p=0.2] {b}Na mistura, some os mols e divida pelo volume total."),
    dict(id="s20", block="fim", text="Na próxima aula, as soluções {a}reagem: [p=0.1] você vai usar {b}uma base de concentração conhecida para descobrir a concentração de um ácido. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
