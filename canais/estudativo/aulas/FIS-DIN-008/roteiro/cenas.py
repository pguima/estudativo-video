# Estudativo · FIS-DIN-008 — Plano inclinado (Física · Dinâmica · Atrito, plano inclinado e sistemas).
# Habilidade: decompor o peso em P·sen θ e P·cos θ e achar a aceleração com e sem atrito, com o atalho a = g·sen θ.
# Pré-requisitos: FIS-DIN-007 (atrito), FIS-CIN-003 (decompor vetor com seno e cosseno). Próxima: FIS-DIN-009.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# g = 10 m/s². sen 30° = 0,5 (MAT-TRI-003). Rampa "sen θ = 0,6 e cos θ = 0,8" é dado da questão (ângulo de cerca de 37°).
# Tração (FIS-DIN-005) não está em "Já ensinado": nenhuma rampa tem fio.

TITULO = "Plano inclinado"

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
    dict(id="s01", block="gancho", text="{a}Uma caixa pesada e uma leve descem juntas uma rampa lisa, sem atrito. [p=0.3] {b}Qual chega primeiro lá embaixo? [p=0.3] {c}Nenhuma: elas chegam juntas. [p=0.2] E você vai ver o porquê numa fórmula curta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}dividir o peso em duas partes na rampa [p=0.2] e achar {c}a aceleração, com e sem atrito."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}decompor um vetor em duas componentes com seno e cosseno; [p=0.2] e {c}o atrito cinético, mi vezes ene. [p=0.3] Se faltar alguma, procure no canal."),
    # decompor
    dict(id="s04", block="decompor", text="{a}Um bloco numa rampa de ângulo teta. [p=0.2] {b}O peso aponta para baixo, na vertical. [p=0.3] Mas o bloco só pode andar {c}ao longo da rampa. [p=0.2] Por isso, {d}gire os eixos: [p=0.1] um ao longo da rampa, [p=0.1] outro perpendicular a ela."),
    dict(id="s05", block="decompor", text="O peso vira {a}duas componentes. [p=0.2] {b}Ao longo da rampa, puxando para baixo: pê vezes seno de teta. [p=0.3] {c}Perpendicular, apertando o bloco contra a rampa: pê vezes cosseno de teta. [p=0.3] {d}O ângulo entre o peso e a perpendicular é o próprio teta, [p=0.2] por isso o seno e o cosseno saem desse ângulo."),
    dict(id="s06", block="decompor", text="Um jeito de não trocar: [p=0.2] {a}rampa deitada, teta igual a zero, o bloco não desce. [p=0.3] {b}Seno de zero é zero. [p=0.2] Então, {c}é o seno que puxa rampa abaixo."),
    # normal
    dict(id="s07", block="normal", text="{a}Na perpendicular, o bloco não sai da rampa: [p=0.2] {b}resultante zero nessa direção. [p=0.3] Então, {c}a normal é pê vezes cosseno de teta. [p=0.3] {d}Na rampa, a normal é menor que o peso."),
    # sem atrito
    dict(id="s08", block="sematrito", text="{a}Sem atrito, só uma força fica ao longo da rampa: pê vezes seno de teta. [p=0.3] Pela segunda lei, {b}eme vezes gê vezes seno de teta é igual a eme vezes á. [p=0.3] {c}A massa corta dos dois lados. [p=0.2] {d}Á é igual a gê vezes seno de teta."),
    dict(id="s09", block="sematrito", text="{a}Numa rampa de trinta graus, seno de trinta é zero vírgula cinco: [p=0.2] {b}á é cinco metros por segundo ao quadrado. [p=0.3] {c}Para a caixa pesada e para a leve. [p=0.2] É por isso que elas chegam juntas."),
    # com atrito
    dict(id="s10", block="comatrito", text="{a}Com atrito, ele aponta contra o deslizamento, rampa acima. [p=0.2] Exemplo: {b}bloco de dez quilogramas, [p=0.1] {c}seno de teta zero vírgula seis, cosseno zero vírgula oito, [p=0.1] {d}mi cinético zero vírgula vinte e cinco."),
    dict(id="s11", block="comatrito", text="{a}Peso de cem newtons. [p=0.2] {b}Ao longo da rampa, cem vezes zero vírgula seis: sessenta. [p=0.2] {c}Normal: cem vezes zero vírgula oito, oitenta. [p=0.2] {d}Atrito: zero vírgula vinte e cinco vezes oitenta, vinte. [p=0.3] {e}Resultante: sessenta menos vinte, quarenta. [p=0.2] {f}Á é quarenta dividido por dez: quatro metros por segundo ao quadrado."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar a normal igual ao peso na rampa. [p=0.3] {b}Com ene igual a cem, o atrito daria vinte e cinco, [p=0.2] e {c}á, três vírgula cinco. [p=0.2] {d}Errado. [p=0.2] Na rampa, {e}a normal é só a parte do peso que aperta: pê vezes cosseno de teta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Sem atrito: á é gê vezes seno de teta. [p=0.3] {b}Com atrito, descendo: á é gê vezes, abre parênteses, seno de teta menos mi vezes cosseno de teta, fecha parênteses. [p=0.3] {c}Dez vezes, abre parênteses, zero vírgula seis menos zero vírgula dois: quatro. [p=0.2] O mesmo resultado, sem calcular força nenhuma."),
    dict(id="s14", block="atalho", text="Funciona porque {a}todas as forças da rampa têm a massa como fator, [p=0.2] e a massa corta. [p=0.3] {b}Não compensa quando alguém empurra ou puxa o bloco: [p=0.2] aí, essa força não tem a massa, e {c}o jeito é somar as forças."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Um bloco de dois quilogramas desce uma rampa [p=0.2] com {b}seno de teta zero vírgula seis e cosseno zero vírgula oito. [p=0.2] O {c}mi cinético é zero vírgula cinco. [p=0.3] {d}Qual é a aceleração? [p=0.2] E {e}qual é a normal?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá, pelo atalho. [p=0.2] {a}Á é dez vezes, abre parênteses, zero vírgula seis menos zero vírgula cinco vezes zero vírgula oito, fecha parênteses. [p=0.3] {b}Zero vírgula cinco vezes zero vírgula oito: zero vírgula quatro. [p=0.2] {c}Zero vírgula seis menos zero vírgula quatro: zero vírgula dois. [p=0.2] {d}Vezes dez: dois metros por segundo ao quadrado."),
    dict(id="s18", block="resposta", text="{a}A normal é pê vezes cosseno de teta: [p=0.1] {b}vinte vezes zero vírgula oito, [p=0.1] {c}dezesseis newtons. [p=0.3] Confira pelas forças: {d}doze para baixo, menos o atrito de oito: [p=0.1] {e}resultante de quatro, e quatro dividido por dois dá dois. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}na rampa, o seno puxa para baixo e o cosseno aperta; [p=0.2] {b}a normal é pê vezes cosseno de teta; [p=0.2] e {c}sem atrito, á é gê vezes seno de teta."),
    dict(id="s20", block="fim", text="Na próxima aula, os blocos {a}andam amarrados: [p=0.2] você vai achar {b}a aceleração de blocos ligados por fios e polias [p=0.2] tratando tudo como {c}um corpo só. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
