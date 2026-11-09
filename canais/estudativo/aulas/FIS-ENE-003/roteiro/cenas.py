# Estudativo · FIS-ENE-003 — Energia cinética e teorema do trabalho (Física · Energia e Colisões · Trabalho e energia).
# Habilidade: calcular Ec = m·v²/2 e usar τ = ΔEc, lembrando que dobrar a velocidade quadruplica a energia.
# Pré-requisitos: FIS-ENE-001 (trabalho), MAT-RAZ-010 (proporcional ao quadrado). Próxima: FIS-ENE-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Torricelli (FIS-CIN-009) e peso não estão em "Já ensinado": a fórmula de Ec é apresentada, sem dedução; o freio vem como
#   força resultante horizontal (sem atrito com o ar).
# Contas: 2 · 3² / 2 = 9 J; 1.000 · 10² / 2 = 50.000 J; 1.000 · 20² / 2 = 200.000 J (×4); freio 0 − 200.000 = −200.000 J,
#   F · 40 = 200.000 → F = 5.000 N; erro (20 − 10)²: 2 · 100 / 2 = 100 J; certo 400 − 100 = 300 J; atalho 40 · 4 = 160 m;
#   questão 4 · 9 / 2 = 18 J, 4 · 25 / 2 = 50 J, τ = 32 J; 8 · d = 32 → d = 4 m.

TITULO = "Energia cinética e teorema do trabalho"

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
    dict(id="s01", block="gancho", text="{a}Um carro a oitenta quilômetros por hora tem quanta energia, comparado com o mesmo carro a quarenta? [p=0.3] {b}O dobro? [p=0.3] Não: {c}quatro vezes. [p=0.2] E é por isso que {d}a velocidade pesa tanto numa batida."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a energia cinética, a do movimento, [p=0.2] e usar {b}o teorema do trabalho para achar trabalhos, forças de freio e distâncias."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o trabalho, força vezes deslocamento vezes cosseno, em joule; [p=0.2] e {c}a ideia de proporcional ao quadrado: se um número dobra, o quadrado dele fica quatro vezes maior. [p=0.3] Se faltar alguma, procure no canal."),
    # energia cinética
    dict(id="s04", block="cinetica", text="{a}Energia é a capacidade de realizar trabalho. [p=0.2] {b}Um corpo em movimento tem energia: [p=0.2] a bola rolando derruba os pinos do boliche. [p=0.3] Essa energia do movimento se chama {c}energia cinética."),
    dict(id="s05", block="cinetica", text="Ela é {a}a massa vezes a velocidade ao quadrado, dividido por dois: [p=0.2] {b}é cê igual a eme vezes vê ao quadrado, dividido por dois. [p=0.3] {c}Eme é a massa, em quilograma. [p=0.1] {d}Vê é a velocidade, em metro por segundo. [p=0.2] E a energia sai em {e}joule, a mesma unidade do trabalho."),
    dict(id="s06", block="cinetica", text="Uma bola de {a}dois quilogramas a três metros por segundo: [p=0.2] {b}três ao quadrado, nove; [p=0.1] {c}dois vezes nove, dezoito; [p=0.1] {d}dividido por dois, nove joules."),
    # o quadrado
    dict(id="s07", block="quadrado", text="Veja o quadrado. [p=0.2] Um carro de mil quilogramas {a}a dez metros por segundo tem [p=0.2] mil vezes cem, dividido por dois: {b}cinquenta mil joules. [p=0.3] {c}A vinte metros por segundo, o dobro da velocidade: [p=0.2] mil vezes quatrocentos, dividido por dois: {d}duzentos mil joules. [p=0.3] {e}Quatro vezes a energia."),
    dict(id="s08", block="quadrado", text="{a}Velocidade dobrada, energia vezes quatro. [p=0.2] {b}Velocidade triplicada, energia vezes nove. [p=0.3] Já {c}a massa entra sem quadrado: [p=0.2] massa dobrada, energia dobrada."),
    # teorema
    dict(id="s09", block="teorema", text="Como um corpo ganha ou perde essa energia? [p=0.2] {a}Recebendo trabalho. [p=0.3] {b}O trabalho da força resultante, a soma de todas as forças, é igual à variação da energia cinética: [p=0.2] {c}tau igual a delta é cê, [p=0.2] {d}a energia do fim menos a do começo. [p=0.3] Esse é o {e}teorema do trabalho e da energia cinética."),
    dict(id="s10", block="teorema", text="{a}Trabalho positivo, a energia aumenta: o corpo acelera. [p=0.2] {b}Trabalho negativo, a energia diminui: o corpo freia."),
    dict(id="s11", block="freio", text="Veja uma freada. [p=0.2] {a}O carro de mil quilogramas, a vinte metros por segundo, freia até parar. [p=0.2] {b}No fim, a energia cinética é zero. [p=0.2] {c}Zero menos duzentos mil: [p=0.1] o freio fez {d}menos duzentos mil joules de trabalho."),
    dict(id="s12", block="freio", text="Se o carro parou em {a}quarenta metros, [p=0.2] o trabalho do freio é {b}menos a força vezes quarenta, [p=0.2] porque o freio é contra o movimento. [p=0.3] {c}Força vezes quarenta igual a duzentos mil: [p=0.2] {d}a força do freio é de cinco mil newtons."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}subtrair as velocidades antes de elevar ao quadrado. [p=0.2] Um corpo de dois quilogramas vai de {b}dez para vinte metros por segundo. [p=0.2] A pessoa faz {c}vinte menos dez, dez, [p=0.1] {d}e calcula dois vezes cem, dividido por dois: cem joules."),
    dict(id="s14", block="erro", text="Mas a variação é {a}a energia do fim menos a do começo. [p=0.2] {b}No fim: dois vezes quatrocentos, dividido por dois, quatrocentos joules. [p=0.2] {c}No começo: dois vezes cem, dividido por dois, cem joules. [p=0.2] {d}Quatrocentos menos cem: trezentos joules, [p=0.1] o triplo do que a pessoa achou."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}com a mesma força de freio, a distância para parar também vai com o quadrado da velocidade. [p=0.3] {b}Velocidade dobrada, distância de frenagem quatro vezes maior. [p=0.2] O carro que, a vinte metros por segundo, parava em quarenta metros, [p=0.2] {c}a quarenta metros por segundo precisa de cento e sessenta metros."),
    dict(id="s16", block="atalho", text="Funciona porque {a}força vezes distância é a energia que o freio tira, [p=0.2] e {b}a energia vai com o quadrado. [p=0.3] {c}Não compensa se a força do freio muda, ou se o carro não para: [p=0.2] aí, faça a conta da energia."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um carrinho de {a}quatro quilogramas está a três metros por segundo. [p=0.2] Uma força resultante o leva a {b}cinco metros por segundo. [p=0.3] {c}Qual foi o trabalho dessa força? [p=0.2] {d}E, se ela vale oito newtons, em quantos metros isso aconteceu?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}No começo: quatro vezes nove, dividido por dois, dezoito joules. [p=0.2] {b}No fim: quatro vezes vinte e cinco, dividido por dois, cinquenta joules. [p=0.2] {c}Cinquenta menos dezoito: trinta e dois joules."),
    dict(id="s20", block="resposta", text="{a}A força ajuda o movimento, então o trabalho é a força vezes a distância. [p=0.2] {b}Oito vezes dê igual a trinta e dois: [p=0.1] {c}dê igual a quatro metros."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}energia cinética é massa vezes velocidade ao quadrado, dividido por dois; [p=0.2] {b}dobrou a velocidade, a energia fica quatro vezes maior; [p=0.2] e {c}o trabalho da resultante é a energia do fim menos a do começo."),
    dict(id="s22", block="fim", text="Na próxima aula, a energia fica guardada: [p=0.2] {a}a energia potencial de um corpo no alto [p=0.1] {b}e de uma mola esticada. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
