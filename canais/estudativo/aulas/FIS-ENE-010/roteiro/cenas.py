# Estudativo · FIS-ENE-010 — Praticando: impulso e colisões (Física · Energia e Colisões · Impulso e colisões · prática).
# Habilidade: resolver questões de impulso, recuo e colisões unindo momento e energia.
# Pré-requisitos: FIS-ENE-007, FIS-ENE-008, FIS-ENE-009. Próxima: nenhuma na trilha (em Física do Zero: FIS-EGF-001, torque).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula.
# Energia potencial e conservação da energia (FIS-ENE-004/005) NÃO estão em "Já ensinado": energia aqui é só a cinética.
# Contas: chute 0,45·30 = 13,5; 13,5/0,015 = 13.500/15 = 900 N; patinadora 2·15 = 30, 60·v = −30 → v = −0,5 m/s (60/2 = 30, 15/30 = 0,5);
#   bala 0,02·300 = 6 = 2·v → v = 3 m/s; Ec 0,02·90.000/2 = 900 J → 2·9/2 = 9 J, perdeu 891 J;
#   classificar 1·8 = 8 = vA + 3·3 → vA = −1; e = (3 + 1)/8 = 0,5; Ec 1·64/2 = 32 → 1·1/2 + 3·9/2 = 0,5 + 13,5 = 14;
#   elástica 6 = vA + 2vB, vB − vA = 6 → vA = −2, vB = 4; Ec 1·36/2 = 18 → 1·4/2 + 2·16/2 = 2 + 16 = 18.

TITULO = "Praticando: impulso e colisões"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, criadas para esta aula: [p=0.2] {b}um chute, um arremesso no gelo, uma bala num bloco e duas batidas de carrinhos. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar o que viu neste módulo: [p=0.2] {a}impulso é a variação da quantidade de movimento; [p=0.2] {b}sem nada de fora empurrando, a quantidade de movimento total se conserva, com sinal; [p=0.2] e {c}o coeficiente de restituição é o afastamento dividido pela aproximação. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: chute
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um jogador chuta {b}uma bola de zero vírgula quarenta e cinco quilograma, parada. [p=0.2] Ela sai a {c}trinta metros por segundo, [p=0.2] e o pé fica em contato com a bola por {d}quinze milésimos de segundo. [p=0.3] {e}Qual é a força média do chute?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}O impulso é a variação da quantidade de movimento: [p=0.2] {b}zero vírgula quarenta e cinco vezes trinta, treze vírgula cinco. [p=0.2] {c}Quinze milésimos de segundo são zero vírgula zero quinze. [p=0.3] {d}A força média é o impulso dividido pelo tempo: treze vírgula cinco dividido por zero vírgula zero quinze."),
    dict(id="s06", block="resposta1", text="Para dividir sem vírgula, {a}multiplique o de cima e o de baixo por mil: [p=0.2] {b}treze mil e quinhentos dividido por quinze. [p=0.2] {c}Novecentos newtons."),
    # situação 2: patinadora
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma patinadora de {b}sessenta quilogramas, parada no gelo, [p=0.2] arremessa {c}uma bola de dois quilogramas a quinze metros por segundo, para a frente. [p=0.3] {d}Com que velocidade ela recua?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Tudo começa parado, então {a}vale o atalho da razão inversa das massas. [p=0.2] {b}Sessenta é trinta vezes dois. [p=0.2] {c}Quinze dividido por trinta: [p=0.1] {d}zero vírgula cinco metro por segundo, para trás. [p=0.3] Na equação, {e}dois vezes quinze, mais sessenta vezes vê, igual a zero: [p=0.2] vê dá menos zero vírgula cinco."),
    # situação 3: bala no bloco
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Uma bala de {b}vinte gramas, a trezentos metros por segundo, [p=0.2] crava num bloco de madeira de {c}um vírgula noventa e oito quilograma, parado sobre uma superfície lisa, que não freia o bloco. [p=0.3] {d}Qual é a velocidade do conjunto, e quanta energia cinética se perdeu?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] {a}Vinte gramas são zero vírgula zero dois quilograma. [p=0.2] {b}Antes: zero vírgula zero dois vezes trezentos, seis. [p=0.2] {c}Depois, juntos: dois quilogramas vezes vê. [p=0.2] {d}Vê igual a três metros por segundo. [p=0.3] {e}Grudaram: colisão inelástica."),
    dict(id="s13", block="resposta3", text="{a}Energia antes: zero vírgula zero dois vezes noventa mil, dividido por dois, novecentos joules. [p=0.2] {b}Depois: dois vezes nove, dividido por dois, nove joules. [p=0.3] {c}Perdeu oitocentos e noventa e um joules: [p=0.2] quase tudo virou calor e madeira rasgada."),
    # situação 4: classificar
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] Um carrinho á, de {b}um quilograma, a oito metros por segundo, [p=0.2] bate num carrinho bê, de {c}três quilogramas, parado. [p=0.2] Depois da batida, {d}o bê sai a três metros por segundo. [p=0.3] {e}Qual é a velocidade do á, e que tipo de colisão é essa?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}Antes: um vezes oito, oito. [p=0.2] {b}Depois: vê á, mais três vezes três, nove. [p=0.2] {c}Vê á mais nove igual a oito: vê á igual a menos um. [p=0.3] {d}O á volta, a um metro por segundo."),
    dict(id="s17", block="resposta4", text="{a}Depois, o bê vai para a frente a três, e o á volta a um: [p=0.2] sentidos opostos, então {b}o afastamento é três mais um, quatro. [p=0.2] {c}A aproximação era oito. [p=0.2] {d}O coeficiente vale quatro dividido por oito: zero vírgula cinco. [p=0.3] {e}Parcialmente elástica: a energia caiu de trinta e dois para catorze joules."),
    # situação 5: elástica
    dict(id="s18", block="questao5", text="{a}Última situação. [p=0.2] Um carrinho á, de {b}um quilograma, a seis metros por segundo, [p=0.2] bate num carrinho bê, de {c}dois quilogramas, parado. [p=0.2] A colisão é {d}elástica. [p=0.3] {e}Quais são as velocidades depois da batida?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] {a}Quantidade de movimento: seis igual a vê á mais dois vê bê. [p=0.2] {b}Elástica, coeficiente igual a um: vê bê menos vê á igual a seis. [p=0.3] {c}Da segunda, vê bê é vê á mais seis. [p=0.2] {d}Na primeira: seis igual a vê á, mais dois vê á, mais doze. [p=0.2] {e}Três vê á igual a menos seis: vê á igual a menos dois."),
    dict(id="s21", block="resposta5", text="{a}E vê bê é menos dois mais seis: quatro metros por segundo. [p=0.3] {b}O á volta a dois metros por segundo: [p=0.2] bateu num corpo de massa maior e foi rebatido. [p=0.3] {c}Confira a energia: antes, dezoito joules; [p=0.2] depois, dois mais dezesseis, dezoito. [p=0.2] {d}Conservou, como deve ser na elástica."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}força média é o impulso dividido pelo tempo; [p=0.2] {b}começando parado, velocidades na razão inversa das massas; [p=0.2] {c}grudou, é inelástica e perde energia; [p=0.2] e {d}na elástica, use as duas equações e confira a energia."),
    dict(id="s23", block="fim", text="Com isso, você fecha a trilha de trabalho, energia e colisões. [p=0.2] Na Física, a próxima trilha começa {a}com torque e alavancas: [p=0.2] por que {b}uma chave de roda comprida solta o parafuso com menos força. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
