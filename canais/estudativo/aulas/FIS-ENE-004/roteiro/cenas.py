# Estudativo · FIS-ENE-004 — Energia potencial: gravitacional e elástica (Física · Energia e Colisões · Trabalho e energia).
# Habilidade: calcular Ep = m·g·h e Ep = k·x²/2 e dizer de onde cada fórmula tira a energia guardada.
# Pré-requisitos: FIS-ENE-001 (trabalho e área do gráfico), FIS-DIN-004 (P = m·g), FIS-DIN-005 (F = k·x). Próxima: FIS-ENE-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# g = 10 m/s² (FIS-CIN-013). As duas fórmulas saem do trabalho que ficou guardado: P·h e a área do triângulo F × x.
# Contas: 2 · 10 · 5 = 100 J; mola 500 · 0,2² / 2 = 500 · 0,04 / 2 = 10 J (erro em cm: 500 · 20² / 2 = 100.000 J, 10.000 vezes mais);
#   atalho F·x/2 = 100 · 0,2 / 2 = 10 J (F = 500 · 0,2 = 100 N); questão 0,5 · 10 · 2 = 10 J e 1.000 · 0,1² / 2 = 5 J.

TITULO = "Energia potencial: gravitacional e elástica"

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
    dict(id="s01", block="gancho", text="{a}Um vaso parado na janela do quinto andar não se move. [p=0.2] Mas, {b}se cair, chega ao chão em alta velocidade. [p=0.3] {c}A energia já estava lá, guardada. [p=0.2] Ela se chama {d}energia potencial."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a energia guardada {b}na altura [p=0.1] e {c}numa mola, [p=0.2] e saber de onde vem cada fórmula."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}o trabalho, força vezes deslocamento; [p=0.2] {c}o peso, massa vezes gê, com gê igual a dez metros por segundo ao quadrado; [p=0.2] e {d}a lei de Hooke: a força da mola é cá vezes xis. [p=0.3] Se faltar alguma, procure no canal."),
    # gravitacional
    dict(id="s04", block="gravitacional", text="{a}Energia potencial é energia guardada pela posição ou pela deformação de um corpo. [p=0.2] Ela {b}não aparece como movimento agora, [p=0.2] mas {c}pode virar movimento depois."),
    dict(id="s05", block="gravitacional", text="Comece pela altura. [p=0.2] Para subir {a}um corpo de massa eme, devagar e sem acelerar, até uma altura agá, [p=0.2] você faz uma força {b}igual ao peso, eme vezes gê, [p=0.2] ao longo de {c}agá metros. [p=0.3] {d}O seu trabalho é eme vezes gê vezes agá."),
    dict(id="s06", block="gravitacional", text="Esse trabalho {a}fica guardado no corpo. [p=0.2] Por isso, {b}a energia potencial gravitacional, o é pê, vale eme vezes gê vezes agá. [p=0.3] {c}Eme em quilograma, [p=0.1] gê em metro por segundo ao quadrado, [p=0.1] e agá, a altura, em metro. [p=0.2] Sai em {d}joule."),
    dict(id="s07", block="gravitacional", text="Um vaso de {a}dois quilogramas, a cinco metros do chão: [p=0.2] {b}dois vezes dez vezes cinco, cem joules."),
    dict(id="s08", block="gravitacional", text="Uma pergunta importante: {a}altura medida a partir de onde? [p=0.2] {b}Você escolhe o nível zero, quase sempre o chão. [p=0.3] {c}Com o zero na altura do vaso, a energia dele seria zero. [p=0.2] O que nunca muda é {d}a diferença de energia entre dois pontos."),
    # elástica
    dict(id="s09", block="elastica", text="Passe para a mola. [p=0.2] Para esticar uma mola, a força {a}não é constante: [p=0.2] começa em {b}zero e cresce até cá vezes xis. [p=0.3] {c}Xis é a deformação, quanto a mola esticou ou encolheu, em metro, [p=0.2] e {d}cá é a constante da mola, em newton por metro."),
    dict(id="s10", block="elastica", text="Força que muda pede {a}o gráfico. [p=0.2] Força por deformação dá {b}uma reta que sai do zero. [p=0.2] O trabalho é {c}a área do triângulo: [p=0.1] base xis, [p=0.1] altura cá vezes xis, [p=0.2] {d}dividido por dois."),
    dict(id="s11", block="elastica", text="Esse trabalho também fica guardado: [p=0.2] {a}a energia potencial elástica é cá vezes xis ao quadrado, dividido por dois. [p=0.3] Uma mola de {b}quinhentos newtons por metro, esticada {c}vinte centímetros: [p=0.2] {d}em metro, zero vírgula dois. [p=0.2] {e}Zero vírgula dois ao quadrado, zero vírgula zero quatro. [p=0.2] {f}Quinhentos vezes zero vírgula zero quatro, vinte, dividido por dois: dez joules."),
    dict(id="s12", block="elastica", text="E de novo aparece o quadrado: [p=0.2] {a}deformação dobrada, energia quatro vezes maior."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar a deformação em centímetro. [p=0.2] A pessoa faz {b}quinhentos vezes vinte ao quadrado, dividido por dois, [p=0.2] e acha {c}cem mil joules."),
    dict(id="s14", block="erro", text="{a}O cá está em newton por metro, então o xis precisa estar em metro. [p=0.2] Com centímetro, {b}o resultado sai dez mil vezes maior: [p=0.2] {c}cem mil, em vez de dez."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova. [p=0.2] Às vezes a questão não dá o cá, [p=0.2] e dá {a}a força final da mola. [p=0.3] Aí, use direto a área do triângulo: [p=0.2] {b}força vezes deformação, dividido por dois. [p=0.3] {c}Uma força de cem newtons estica a mola vinte centímetros: [p=0.2] {d}cem vezes zero vírgula dois, vinte, dividido por dois: dez joules."),
    dict(id="s16", block="atalho", text="Funciona porque {a}a força final já é cá vezes xis. [p=0.2] É {b}a mesma mola de antes, com a mesma energia. [p=0.3] {c}Não compensa se a questão dá o cá e o xis: [p=0.2] aí, a fórmula é mais direta."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Um livro de meio quilograma está numa estante, a dois metros do chão. [p=0.2] {b}Qual é a energia potencial dele, em relação ao chão? [p=0.3] E {c}uma mola de mil newtons por metro, comprimida dez centímetros: [p=0.2] {d}quanta energia ela guarda?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}O livro: zero vírgula cinco vezes dez vezes dois, [p=0.2] {b}dez joules."),
    dict(id="s20", block="resposta", text="{a}A mola: dez centímetros, em metro, são zero vírgula um. [p=0.2] {b}Zero vírgula um ao quadrado, zero vírgula zero um. [p=0.2] {c}Mil vezes zero vírgula zero um, dez, dividido por dois: [p=0.1] {d}cinco joules. [p=0.3] Comprimida ou esticada, a conta é a mesma."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}na altura, a energia potencial vale eme vezes gê vezes agá; [p=0.2] {b}na mola, cá vezes xis ao quadrado, dividido por dois; [p=0.2] e {c}as duas são o trabalho que ficou guardado."),
    dict(id="s22", block="fim", text="Na próxima aula, a energia guardada {a}vira movimento: [p=0.2] você vai igualar {b}a energia do começo e a do fim na montanha-russa e no pêndulo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
