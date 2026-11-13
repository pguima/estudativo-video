# Estudativo · QUI-CAL-011 — Transformações gasosas e equação geral (Química · Cálculos Químicos · Estudo dos gases).
# Habilidade: reconhecer transformações isotérmica, isobárica e isocórica e achar o novo volume de um gás com
# P₁V₁/T₁ = P₂V₂/T₂, dizendo o que cada termo significa.
# Pré-requisitos: QUI-CAL-010, MAT-RAZ-002, MAT-RAZ-004, MAT-EQU-011. Próxima: QUI-CAL-012 (Clapeyron).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Contas: 10 L, 1 atm, 300 K → 2 atm, 360 K: V₂ = 1·10·360/(300·2) = 3.600/600 = 6 L; fatores 10 · ½ · 1,2 = 6.
# Erro em °C: 10·87/(27·2) ≈ 16,1 L. Questão: isobárica, 6 · 400/300 = 8 L. Mol e regra de três NÃO estão em "Já ensinado".
# "Iso" = igual; "baro" = pressão (barômetro); "córica" = de volume (isovolumétrica).

TITULO = "Transformações gasosas e equação geral"

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
    dict(id="s01", block="gancho", text="{a}Tampe a ponta de uma seringa e empurre o êmbolo, a peça que desliza lá dentro. [p=0.3] {b}Quanto mais você aperta, mais difícil fica. [p=0.2] {c}Com metade do espaço, o ar empurra de volta com o dobro da pressão. [p=0.3] {d}Essa troca tem regra, [p=0.1] e uma equação só resolve todos os casos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}reconhecer as três transformações de um gás [p=0.2] e {c}achar o novo volume com a equação geral, [p=0.2] com um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a temperatura de gás em kelvin; [p=0.2] {c}grandezas direta e inversamente proporcionais; [p=0.2] e {d}isolar uma letra numa fórmula. [p=0.3] Se faltar alguma, procure no canal."),
    # isotérmica
    dict(id="s04", block="isotermica", text="{a}Um gás preso tem três variáveis: [p=0.1] {b}pressão, volume e temperatura. [p=0.3] {c}Numa transformação, uma delas fica parada, e as outras mudam."),
    dict(id="s05", block="isotermica", text="{a}Temperatura parada: transformação isotérmica. [p=0.2] {b}Iso quer dizer igual; térmica, de temperatura. [p=0.3] {c}É a seringa: metade do volume, o dobro da pressão. [p=0.3] {d}Pressão e volume são inversamente proporcionais: [p=0.1] {e}pê vezes vê não muda."),
    # isobárica
    dict(id="s06", block="isobarica", text="{a}Pressão parada: isobárica. [p=0.1] Baro lembra pressão, como no barômetro, o aparelho que mede a pressão do ar. [p=0.3] {b}Esquente um balão, e ele cresce. [p=0.2] {c}Volume e temperatura em kelvin são diretamente proporcionais: [p=0.1] {d}de trezentos para seiscentos kelvin, o volume dobra. [p=0.2] {e}O volume dividido pela temperatura não muda."),
    # isocórica
    dict(id="s07", block="isocorica", text="{a}Volume parado: isocórica, ou isovolumétrica. [p=0.1] Córica vem de espaço: o volume. [p=0.3] {b}É a lata de spray no fogo: [p=0.1] o volume não muda, [p=0.1] {c}a temperatura sobe, [p=0.1] {d}e a pressão sobe junto, até a lata estourar. [p=0.3] {e}Pressão dividida por temperatura não muda."),
    # equação geral
    dict(id="s08", block="geral", text="{a}As três regras cabem numa equação só, a equação geral dos gases: [p=0.3] {b}pê um vezes vê um, sobre tê um, [p=0.1] {c}igual a pê dois vezes vê dois, sobre tê dois."),
    dict(id="s09", block="geral", text="{a}O número um marca o gás antes; [p=0.1] {b}o dois, depois. [p=0.3] {c}Pê é a pressão, vê o volume, tê a temperatura em kelvin. [p=0.3] {d}Se uma variável não muda, ela aparece igual dos dois lados e se cancela: [p=0.2] {e}se a temperatura não muda, ela se cancela, [p=0.1] e sobra pê um vê um igual a pê dois vê dois: a isotérmica."),
    # exemplo
    dict(id="s10", block="exemplo", text="{a}Um gás ocupa dez litros a uma atmosfera e vinte e sete graus Celsius. [p=0.2] {b}Ele é comprimido a duas atmosferas e aquecido a oitenta e sete graus. [p=0.2] {c}Qual é o novo volume? [p=0.3] {d}Primeiro, kelvin: vinte e sete graus viram trezentos kelvin, [p=0.1] {e}e oitenta e sete viram trezentos e sessenta."),
    dict(id="s11", block="exemplo", text="{a}Na equação: um vezes dez sobre trezentos [p=0.1] igual a dois vezes vê dois sobre trezentos e sessenta. [p=0.3] {b}Isole o vê dois: [p=0.1] {c}um vezes dez vezes trezentos e sessenta, [p=0.1] dividido por seiscentos, que é trezentos vezes dois. [p=0.3] {d}Três mil e seiscentos dividido por seiscentos dá seis litros."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}deixar a temperatura em Celsius. [p=0.3] {b}Usando vinte e sete graus e oitenta e sete graus, a conta dá cerca de dezesseis litros: [p=0.2] {c}a pressão dobrou e a temperatura subiu só um pouco: [p=0.1] o volume tinha que diminuir, não crescer. [p=0.3] {d}Sem kelvin, a proporção quebra."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho: [p=0.1] {a}trate cada mudança como um fator. [p=0.3] {b}A pressão dobrou: o volume cai à metade, vezes um meio. [p=0.2] {c}A temperatura foi de trezentos para trezentos e sessenta kelvin: [p=0.1] o volume cresce na mesma razão, vezes um vírgula dois. [p=0.3] {d}Dez vezes um meio vezes um vírgula dois dá seis litros."),
    dict(id="s14", block="atalho", text="{a}Funciona porque pressão é inversa e temperatura é direta. [p=0.2] {b}O fator da pressão vai de cabeça para baixo; [p=0.1] {c}o da temperatura vai na ordem. [p=0.3] {d}Não compensa com números que não se simplificam: [p=0.1] aí, use a equação."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Um cilindro com êmbolo solto, livre para subir e descer, tem seis litros de gás a vinte e sete graus Celsius. [p=0.2] {b}Ele é aquecido a cento e vinte e sete graus, [p=0.1] sem mudar a pressão. [p=0.3] {c}Qual é a transformação? [p=0.2] {d}E o novo volume?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Pressão parada: isobárica. [p=0.3] {b}Em kelvin, de trezentos para quatrocentos. [p=0.2] {c}O volume cresce na mesma razão: [p=0.1] {d}seis vezes quatrocentos, dividido por trezentos, [p=0.1] {e}dá oito litros."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}isotérmica, isobárica e isocórica dizem o que fica parado; [p=0.2] {b}a equação geral resolve as três, [p=0.1] {c}sempre com a temperatura em kelvin."),
    dict(id="s19", block="fim", text="Na próxima aula, entra a quantidade de gás: [p=0.2] {a}a equação pê vê igual a ene erre tê, [p=0.1] para {b}descobrir a massa de gás dentro de um cilindro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
