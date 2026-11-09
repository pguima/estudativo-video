# Estudativo · FIS-CAL-011 — Trabalho de um gás (Física · Calor e Termodinâmica · Termodinâmica e máquinas térmicas).
# Habilidade: calcular τ = p·ΔV e usar a área do gráfico p × V, inclusive a área de dentro de um ciclo.
# Pré-requisitos: FIS-ENE-001 (trabalho de uma força), QUI-CAL-011 (transformações gasosas), MAT-ARE-004 (área do trapézio).
# Próxima: FIS-CAL-012. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fora de "Já ensinado": FIS-CAL-001 e FIS-CAL-003 (temperatura em Celsius e calor). A aula não usa temperatura nem calor.
# Pressão em pascal (FIS-EGF-004); litro ↔ metro cúbico (MAT-MED-005); prefixo quilo (MAT-MED-003).

TITULO = "Trabalho de um gás"

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
    dict(id="s01", block="gancho", text="{a}Dentro do motor de um carro, [p=0.2] quem empurra o pistão não é uma mão nem uma mola. [p=0.3] {b}É um gás. [p=0.3] E um gás que empurra {c}faz trabalho, como qualquer força."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}o trabalho de um gás [p=0.2] e {c}tirar esse trabalho direto de um gráfico."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o trabalho de uma força que empurra no sentido do movimento, tau igual a éfe vezes dê, em joule; [p=0.2] e {c}a pressão, que é força dividida por área, em pascal. [p=0.3] Se faltar alguma, procure no canal."),
    # a fórmula
    dict(id="s04", block="formula", text="Pense num {a}gás preso num cilindro, [p=0.2] com {b}uma tampa que desliza, o êmbolo, que no motor se chama pistão. [p=0.3] {c}O gás empurra o êmbolo com uma pressão pê. [p=0.2] Como a pressão é força por área, {d}a força é pê vezes a área do êmbolo."),
    dict(id="s05", block="formula", text="{a}O êmbolo anda uma distância dê. [p=0.2] Trabalho é força vezes distância: [p=0.2] {b}pê vezes área vezes dê. [p=0.3] Mas {c}área vezes distância é o volume que o gás ganhou: [p=0.2] {d}a variação de volume, delta vê. [p=0.3] Delta é o símbolo de variação: {e}o volume final menos o inicial."),
    dict(id="s06", block="formula", text="Fica assim: [p=0.2] {a}tau, o trabalho, é igual a pê vezes delta vê. [p=0.3] {b}Tau é a letra grega que as provas usam para trabalho, em joule. [p=0.2] {c}Pê é a pressão, em pascal. [p=0.2] {d}Delta vê, em metro cúbico. [p=0.3] Vale quando {e}a pressão fica constante, a transformação isobárica."),
    # exemplo
    dict(id="s07", block="exemplo", text="Exemplo. [p=0.2] Um gás a {a}cem mil pascals [p=0.2] se expande {b}de dois para cinco litros. [p=0.3] {c}Delta vê é cinco menos dois: três litros. [p=0.3] Em metro cúbico: {d}um metro cúbico tem mil litros, [p=0.2] então {e}três litros são três milésimos de metro cúbico."),
    dict(id="s08", block="exemplo", text="{a}Cem mil vezes três milésimos: [p=0.2] {b}trezentos joules. [p=0.3] E o sinal conta uma história. [p=0.2] {c}Na expansão, delta vê é positivo: o gás empurra e faz trabalho. [p=0.3] {d}Na compressão, delta vê é negativo: alguém empurra o gás, e ele recebe trabalho. [p=0.3] {e}Com o volume parado, o trabalho é zero."),
    # gráfico
    dict(id="s09", block="grafico", text="Vamos ao gráfico. [p=0.2] Ponha {a}a pressão no eixo de pé [p=0.1] e {b}o volume no deitado. [p=0.3] {c}Pressão constante é uma linha reta deitada. [p=0.3] {d}A área embaixo dela é um retângulo: [p=0.2] {e}altura pê, base delta vê. [p=0.3] {f}Área igual a pê vezes delta vê: [p=0.2] é o trabalho."),
    dict(id="s10", block="grafico", text="E isso vale sempre: [p=0.2] {a}no gráfico pê vê, o trabalho é a área embaixo da linha, [p=0.2] como no gráfico de força por distância. [p=0.3] Se a pressão muda em linha reta, {b}a figura vira um trapézio. [p=0.3] Pressão de {c}cem para trezentos quilopascals, [p=0.2] volume de {d}um para três metros cúbicos."),
    dict(id="s11", block="grafico", text="Área do trapézio: {a}base maior mais base menor, vezes a altura, dividido por dois. [p=0.3] Aqui, o trapézio está deitado: [p=0.2] {b}as bases são as pressões, [p=0.1] trezentos e cem, [p=0.2] e {c}a altura é a variação de volume, dois. [p=0.3] {d}Quatrocentos vezes dois, dividido por dois: [p=0.2] {e}quatrocentos quilojoules."),
    # ciclo
    dict(id="s12", block="ciclo", text="E se o gás {a}vai e volta ao ponto de partida? [p=0.2] Isso é {b}um ciclo, como num motor. [p=0.3] {c}Na ida, por cima, a pressão é alta: [p=0.2] o gás faz {d}o trabalho da área embaixo do caminho de cima. [p=0.3] {e}Na volta, por baixo, ele é comprimido com pressão baixa: [p=0.2] recebe {f}o trabalho da área embaixo do caminho de baixo."),
    dict(id="s13", block="ciclo", text="{a}A diferença é só a área de dentro do ciclo. [p=0.3] Pressão de {b}cem a duzentos quilopascals, [p=0.2] volume de {c}um a quatro metros cúbicos: [p=0.2] {d}altura cem, base três: trezentos quilojoules por volta. [p=0.3] {e}Ciclo no sentido horário, o trabalho é positivo: [p=0.2] é o motor. [p=0.2] {f}No anti-horário, a ida é por baixo, e o saldo fica negativo."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}multiplicar pascal por litro. [p=0.3] No exemplo, a pessoa faz {b}cem mil vezes três [p=0.2] e responde {c}trezentos mil joules. [p=0.3] {d}Mil vezes mais que o certo, [p=0.2] porque {e}o litro é mil vezes menor que o metro cúbico."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}quilopascal vezes litro dá joule direto. [p=0.3] Cem mil pascals são {b}cem quilopascals. [p=0.2] {c}Cem vezes três litros: trezentos joules, [p=0.2] sem converter nada."),
    dict(id="s16", block="atalho", text="Funciona porque {a}o quilo multiplica por mil, [p=0.2] e {b}o litro divide por mil: [p=0.2] {c}um cancela o outro. [p=0.3] {d}Não compensa se a pressão vier em atmosfera, [p=0.2] ou o volume em centímetro cúbico: [p=0.2] aí, converta para pascal e metro cúbico."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um gás, a pressão constante de {a}duzentos quilopascals, [p=0.2] {b}passa de quatro para um litro. [p=0.3] {c}Qual é o trabalho? [p=0.2] E {d}o gás fez ou recebeu esse trabalho?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Delta vê é o final menos o inicial: [p=0.2] {b}um menos quatro, menos três litros. [p=0.3] Com o atalho: {c}duzentos quilopascals vezes menos três litros, [p=0.2] {d}menos seiscentos joules."),
    dict(id="s20", block="resposta", text="{a}O sinal de menos diz que o volume diminuiu: [p=0.2] foi uma compressão. [p=0.2] {b}O gás recebeu seiscentos joules de trabalho."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}tau é pê vezes delta vê; [p=0.2] {b}no gráfico pê vê, o trabalho é a área; [p=0.2] e {c}no ciclo, é a área de dentro."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai ver {a}para onde vai o calor que um gás recebe: [p=0.2] {b}uma parte vira trabalho, e outra fica guardada nele. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
