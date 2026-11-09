# Estudativo · FIS-ENE-005 — Conservação da energia e energia dissipada (Física · Energia e Colisões · Trabalho e energia).
# Habilidade: igualar a energia inicial e a final na montanha-russa e no pêndulo, com o atalho v = √(2·g·h), e calcular a
#   energia perdida no atrito.
# Pré-requisitos: FIS-ENE-003 (Ec), FIS-ENE-004 (Ep), MAT-POT-007 (raiz quadrada). Próxima: FIS-ENE-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Atrito (FIS-DIN-007) não está em "Já ensinado": é citado como a força do esfregar, assunto de outra aula, sem fórmula.
#   A normal (FIS-DIN-004) é perpendicular ao trilho: trabalho zero (FIS-ENE-001). Porcentagem não está em "Já ensinado".
# Contas: m·10·20 = m·v²/2 → v² = 400 → v = 20 m/s; pêndulo √(2·10·0,45) = √9 = 3 m/s; volta: 20²/(2·10) = 20 m;
#   escorregador 30·10·5 = 1.500 J, 30·36/2 = 540 J, dissipada 960 J; questão √(2·10·3,2) = √64 = 8 m/s;
#   50·10·3,2 = 1.600 J, 50·36/2 = 900 J, dissipada 700 J.

TITULO = "Conservação da energia e energia dissipada"

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
    dict(id="s01", block="gancho", text="{a}Um carrinho de montanha-russa parte do repouso e desce de vinte metros de altura. [p=0.2] {b}A que velocidade ele chega lá embaixo? [p=0.3] Sem atrito, a resposta {c}não depende da massa [p=0.1] {d}nem do formato do trilho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai igualar a energia do começo e a do fim, [p=0.2] usar {b}um atalho para a velocidade [p=0.2] e calcular {c}a energia perdida no atrito."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}a energia cinética, eme vezes vê ao quadrado, dividido por dois; [p=0.2] {c}a energia potencial, eme vezes gê vezes agá; [p=0.2] e {d}raiz quadrada. [p=0.3] Se faltar alguma, procure no canal."),
    # conservação
    dict(id="s04", block="conserva", text="{a}A soma da energia cinética com a potencial se chama energia mecânica. [p=0.3] Quando {b}não há atrito nem resistência do ar, [p=0.2] {c}a energia mecânica se conserva: [p=0.2] ela muda de forma, mas {d}o total não muda."),
    dict(id="s05", block="conserva", text="Veja nas barras. [p=0.2] {a}No alto, parado, é tudo potencial. [p=0.2] {b}Na descida, a potencial diminui e a cinética cresce. [p=0.2] {c}Embaixo, é tudo cinética. [p=0.3] {d}A altura total das barras fica igual o tempo todo."),
    # montanha-russa
    dict(id="s06", block="conta", text="Faça a conta do carrinho. [p=0.2] {a}Energia no alto: eme vezes dez vezes vinte. [p=0.2] {b}Energia embaixo: eme vezes vê ao quadrado, dividido por dois. [p=0.3] {c}Iguale as duas."),
    dict(id="s07", block="conta", text="{a}A massa aparece dos dois lados e corta. [p=0.2] Sobra {b}vê ao quadrado, dividido por dois, igual a duzentos. [p=0.2] {c}Vê ao quadrado igual a quatrocentos. [p=0.2] {d}Vê igual a vinte metros por segundo. [p=0.3] Por isso a massa não importa."),
    dict(id="s08", block="conta", text="E o formato do trilho? [p=0.2] {a}A normal, a força do trilho no carrinho, é sempre perpendicular ao caminho, [p=0.2] então {b}não faz trabalho. [p=0.3] Só conta {c}a diferença de altura. [p=0.3] {d}No pêndulo, a força do fio também é perpendicular ao caminho, e também não faz trabalho."),
    # atalho
    dict(id="s09", block="atalho", text="Agora, o atalho de prova. [p=0.2] Saindo do repouso, sem atrito, a conta sempre dá {a}vê igual à raiz de dois vezes gê vezes agá. [p=0.3] No pêndulo, {b}solte a esfera quarenta e cinco centímetros acima do ponto mais baixo: [p=0.2] {c}raiz de dois vezes dez vezes zero vírgula quarenta e cinco, [p=0.2] {d}raiz de nove, três metros por segundo."),
    dict(id="s10", block="atalho", text="Funciona porque {a}a massa sempre corta. [p=0.2] E vale ao contrário: [p=0.2] {b}subindo sem atrito, com vinte metros por segundo, o carrinho chega a vinte metros de altura. [p=0.3] {c}Não compensa se o corpo já começa andando, ou se há atrito: [p=0.2] aí, iguale as energias com todos os termos."),
    # dissipada
    dict(id="s11", block="dissipada", text="E com atrito? [p=0.2] {a}O atrito é a força que aparece quando uma superfície esfrega na outra, assunto de outra aula. [p=0.2] Ele {b}transforma parte da energia em calor. [p=0.3] Essa parte se chama {c}energia dissipada: [p=0.2] {d}a energia do começo menos a do fim."),
    dict(id="s12", block="dissipada", text="Uma criança de {a}trinta quilogramas desce um escorregador de cinco metros de altura [p=0.2] e chega embaixo a {b}seis metros por segundo. [p=0.3] {c}No alto: trinta vezes dez vezes cinco, mil e quinhentos joules. [p=0.2] {d}Embaixo: trinta vezes trinta e seis, dividido por dois, quinhentos e quarenta joules."),
    dict(id="s13", block="dissipada", text="{a}Mil e quinhentos menos quinhentos e quarenta: [p=0.1] {b}novecentos e sessenta joules viraram calor. [p=0.3] {c}A energia não sumiu: [p=0.1] o escorregador e a roupa da criança esquentaram um pouco."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o corpo mais pesado chega mais rápido. [p=0.2] Com um carrinho {b}de cem quilogramas e outro de quinhentos, saindo dos mesmos vinte metros de altura, sem atrito, [p=0.2] a pessoa espera {c}o de quinhentos bem mais veloz."),
    dict(id="s15", block="erro", text="Mas {a}a massa cortou na conta. [p=0.2] {b}Cada um chega a vinte metros por segundo. [p=0.3] {c}O mais pesado tem mais energia, mas também precisa de mais energia para a mesma velocidade."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um skatista de {a}cinquenta quilogramas parte do repouso no alto de uma rampa de {b}três vírgula dois metros de altura. [p=0.3] {c}Sem atrito, com que velocidade ele chegaria embaixo? [p=0.2] {d}E, se ele chega a seis metros por segundo, quanta energia foi dissipada?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Pelo atalho: raiz de dois vezes dez vezes três vírgula dois. [p=0.2] {b}Dois vezes dez, vinte; vinte vezes três vírgula dois, sessenta e quatro. [p=0.2] {c}Raiz de sessenta e quatro, oito metros por segundo."),
    dict(id="s19", block="resposta", text="{a}No alto: cinquenta vezes dez vezes três vírgula dois, mil e seiscentos joules. [p=0.2] {b}Embaixo: cinquenta vezes trinta e seis, dividido por dois, novecentos joules. [p=0.2] {c}Dissipada: mil e seiscentos menos novecentos, setecentos joules."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}sem atrito, a energia do começo é igual à do fim; [p=0.2] {b}saindo do repouso, vê é a raiz de dois vezes gê vezes agá; [p=0.2] e {c}com atrito, a energia dissipada é a do começo menos a do fim."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai {a}praticar tudo isso: [p=0.2] trabalho, potência, rendimento e energia, em questões de prova. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
