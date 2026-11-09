# Estudativo · FIS-ENE-006 — Praticando: trabalho e energia (Física · Energia e Colisões · Trabalho e energia · prática).
# Habilidade: seguir as transformações de energia e calcular trabalho, potência e rendimento em questões de prova.
# Pré-requisitos: FIS-ENE-001, FIS-ENE-002, FIS-ENE-003, FIS-ENE-004, FIS-ENE-005. Próxima: FIS-ENE-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula.
# Contas: área 4·30 + 2·30/2 = 120 + 30 = 150 J; guindaste 500·10·12 = 60.000 J, 60.000/20 = 3.000 W, 3.000/4.000 = 75 %
#   (perda 1.000 W, um quarto); freada 108/72 = 1,5, 1,5² = 2,25, 40·2,25 = 90 m (72 km/h = 20 m/s, 108 km/h = 30 m/s: (30/20)² = 2,25);
#   mola 800·0,1²/2 = 4 J; 0,5·v²/2 = 4 → v² = 16 → v = 4 m/s; usina 2.000·10·50 = 1.000.000 J/s = 1 MW, 90 % = 900.000 W = 900 kW.

TITULO = "Praticando: trabalho e energia"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, criadas para esta aula: [p=0.2] {b}um gráfico, um guindaste, uma freada, uma mola e uma usina. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.3] E repare {d}para onde a energia vai."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar o que viu nesta trilha: [p=0.2] {a}trabalho, força vezes deslocamento vezes cosseno, ou a área do gráfico; [p=0.2] {b}potência, trabalho dividido pelo tempo, e rendimento, útil dividido por total; [p=0.2] {c}energia cinética e energia potencial; [p=0.2] e {d}a conservação da energia. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: gráfico
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma força empurra uma caixa pelo chão, sempre na direção do movimento. [p=0.2] O gráfico mostra a força: {b}trinta newtons constantes nos primeiros quatro metros, [p=0.2] {c}e depois ela cai até zero nos dois metros seguintes. [p=0.3] {d}Qual é o trabalho total da força?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Trabalho é a área do gráfico, [p=0.2] e ela tem duas partes. [p=0.2] {b}O retângulo: quatro vezes trinta, cento e vinte joules. [p=0.2] {c}O triângulo: dois vezes trinta, sessenta, dividido por dois, trinta joules. [p=0.3] {d}Total: cento e cinquenta joules."),
    # situação 2: guindaste
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Um guindaste elétrico levanta {b}uma carga de quinhentos quilogramas a doze metros de altura, [p=0.2] devagar, em {c}vinte segundos. [p=0.2] Ele recebe {d}quatro quilowatts da rede elétrica. [p=0.3] {e}Qual é o rendimento do guindaste?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] O útil é a energia que a carga ganhou em altura: [p=0.2] {a}quinhentos vezes dez vezes doze, sessenta mil joules. [p=0.3] {b}Potência útil: sessenta mil dividido por vinte, três mil watts. [p=0.2] {c}Quatro quilowatts são quatro mil watts. [p=0.2] {d}Três mil dividido por quatro mil: setenta e cinco por cento."),
    dict(id="s09", block="resposta2", text="Siga a energia: [p=0.2] {a}ela chega como energia elétrica, [p=0.1] {b}três quartos viram energia potencial da carga, [p=0.2] e {c}um quarto vira calor no motor."),
    # situação 3: freada
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Um carro a {b}setenta e dois quilômetros por hora freia e para em {c}quarenta metros. [p=0.3] {d}Com a mesma força de freio, a cento e oito quilômetros por hora, em quantos metros ele para?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] O freio tira toda a energia cinética, e {a}ela vai com o quadrado da velocidade. [p=0.3] {b}Cento e oito dividido por setenta e dois dá um vírgula cinco. [p=0.2] {c}Um vírgula cinco ao quadrado, dois vírgula vinte e cinco. [p=0.2] {d}Quarenta vezes dois vírgula vinte e cinco: noventa metros. [p=0.3] {e}A energia do movimento vira calor nos freios."),
    # atalho
    dict(id="s13", block="atalho", text="Aqui cabe um atalho: {a}numa comparação, não precisa converter para metro por segundo, [p=0.2] porque a unidade corta na divisão. [p=0.3] {b}Convertendo, setenta e dois quilômetros por hora são vinte metros por segundo, e cento e oito são trinta: [p=0.2] {c}trinta dividido por vinte dá o mesmo um vírgula cinco. [p=0.3] {d}Não compensa quando a questão pede a energia ou a força: [p=0.2] aí, a velocidade precisa estar em metro por segundo."),
    # situação 4: mola
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] Uma mola de {b}oitocentos newtons por metro está comprimida {c}dez centímetros, [p=0.2] empurrando {d}um carrinho de meio quilograma, parado. [p=0.3] Sem atrito, {e}com que velocidade o carrinho sai quando a mola é solta?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}Energia da mola: oitocentos vezes zero vírgula um ao quadrado, dividido por dois. [p=0.2] {b}Zero vírgula um ao quadrado, zero vírgula zero um; [p=0.2] {c}oitocentos vezes zero vírgula zero um, oito, dividido por dois, quatro joules. [p=0.3] {d}Sem atrito, toda essa energia vira cinética."),
    dict(id="s17", block="resposta4", text="{a}Zero vírgula cinco vezes vê ao quadrado, dividido por dois, igual a quatro. [p=0.2] {b}Zero vírgula cinco dividido por dois dá zero vírgula vinte e cinco. [p=0.2] {c}Vê ao quadrado igual a quatro dividido por zero vírgula vinte e cinco: dezesseis. [p=0.2] {d}Vê igual a quatro metros por segundo."),
    # situação 5: usina
    dict(id="s18", block="questao5", text="{a}Última situação. [p=0.2] Numa usina hidrelétrica, {b}a cada segundo, dois mil quilogramas de água descem cinquenta metros até a turbina. [p=0.3] {c}A usina transforma noventa por cento dessa energia em energia elétrica. [p=0.3] {d}Que potência elétrica sai da usina?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] {a}Energia potencial da água, a cada segundo: dois mil vezes dez vezes cinquenta, [p=0.2] {b}um milhão de joules. [p=0.2] {c}Um milhão de joules por segundo é um milhão de watts: um megawatt. [p=0.3] {d}Noventa por cento disso: novecentos mil watts, novecentos quilowatts."),
    dict(id="s21", block="resposta5", text="Siga a energia: [p=0.2] {a}a potencial da água vira cinética na descida, [p=0.2] {b}a cinética gira a turbina e vira elétrica no gerador, [p=0.2] e {c}dez por cento se perdem como calor."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}força que muda pede a área do gráfico; [p=0.2] {b}rendimento compara o útil com o total; [p=0.2] {c}velocidade maior pesa ao quadrado na energia e na frenagem; [p=0.2] e {d}sem atrito, a energia só muda de forma."),
    dict(id="s23", block="fim", text="Na próxima aula, começa um assunto novo: [p=0.2] {a}a quantidade de movimento e o impulso, [p=0.2] e {b}por que o airbag protege numa batida. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
