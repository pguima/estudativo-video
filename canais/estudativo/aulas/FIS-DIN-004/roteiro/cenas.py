# Estudativo · FIS-DIN-004 — Peso e força normal (Física · Dinâmica · Leis de Newton).
# Habilidade: calcular o peso com P = m·g, separar peso de massa e achar a normal no chão e no elevador.
# Pré-requisitos: FIS-DIN-002 (F = m·a), FIS-DIN-003 (ação e reação), FIS-CIN-013 (queda livre, g = 10 m/s²). Próxima: FIS-DIN-005.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# g = 10 m/s² (como em FIS-CIN-013). Gravidade da Lua ≈ 1,6 m/s² (valor de referência: 1,62 m/s²).
# A balança comum mede a força que faz em você (a normal) e mostra em "quilos" dividindo por 10: dito como simplificação.

TITULO = "Peso e força normal"

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
    dict(id="s01", block="gancho", text="{a}Suba numa balança dentro de um elevador. [p=0.2] Quando ele {b}arranca para cima, a balança marca {c}mais do que você pesa. [p=0.3] {d}Sua massa não mudou. [p=0.2] Então, o que a balança está medindo?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}calcular o peso, [p=0.2] {c}separar peso de massa [p=0.2] e achar a {d}força normal, no chão e no elevador."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}força resultante igual a massa vezes aceleração; [p=0.2] {c}ação e reação, em corpos diferentes; [p=0.2] e {d}a aceleração da queda livre, gê, igual a dez metros por segundo ao quadrado. [p=0.3] Se faltar alguma, procure no canal."),
    # peso
    dict(id="s04", block="peso", text="{a}Peso é a força com que a Terra puxa um corpo. [p=0.2] {b}Aponta sempre para baixo, na vertical. [p=0.3] Se você soltar o corpo, só o peso age, [p=0.2] e ele cai com {c}aceleração gê. [p=0.3] Então, pela segunda lei: {d}pê é igual a eme vezes gê."),
    dict(id="s05", block="peso", text="{a}Pê é o peso, em newtons. [p=0.1] {b}Eme é a massa, em quilogramas. [p=0.1] {c}Gê é dez metros por segundo ao quadrado. [p=0.3] {d}Uma pessoa de sessenta quilogramas: [p=0.2] {e}sessenta vezes dez, seiscentos newtons."),
    dict(id="s06", block="peso", text="{a}Massa e peso não são a mesma coisa. [p=0.2] {b}Massa é quanto de matéria o corpo tem: [p=0.1] em quilogramas, e é a mesma em qualquer lugar. [p=0.3] {c}Na Lua, gê é perto de um vírgula seis metro por segundo ao quadrado. [p=0.2] A mesma pessoa continua com sessenta quilogramas, [p=0.2] mas {d}pesa só noventa e seis newtons."),
    # normal
    dict(id="s07", block="normal", text="Agora, {a}um corpo parado no chão. [p=0.2] O peso puxa para baixo, [p=0.1] e {b}o chão empurra para cima. [p=0.3] Essa força do chão é a {c}força normal. [p=0.2] Normal quer dizer {d}perpendicular: ela sai da superfície, em ângulo reto."),
    dict(id="s08", block="normal", text="Corpo parado: {a}resultante zero. [p=0.2] No chão plano, sem mais nada, {b}a normal é igual ao peso. [p=0.3] Mas atenção: [p=0.1] {c}normal e peso não são ação e reação. [p=0.2] As duas estão {d}no mesmo corpo. [p=0.2] O par do peso é {e}o corpo puxando a Terra."),
    # elevador
    dict(id="s09", block="elevador", text="E a balança? [p=0.2] {a}Ela mede a força com que empurra você: a normal. [p=0.3] Depois, {b}divide por dez e mostra em quilos. [p=0.3] {c}Parado, a normal é seiscentos, e ela mostra sessenta."),
    dict(id="s10", block="elevador", text="{a}O elevador arranca para cima com aceleração de dois metros por segundo ao quadrado. [p=0.3] A resultante aponta para cima: [p=0.1] {b}normal menos peso é igual a eme vezes á. [p=0.3] {c}Normal menos seiscentos é igual a sessenta vezes dois. [p=0.2] {d}A normal vale setecentos e vinte newtons. [p=0.2] {e}A balança mostra setenta e dois."),
    dict(id="s11", block="elevador", text="{a}Se a aceleração aponta para baixo, também de dois, [p=0.2] {b}o peso vence: [p=0.1] {c}seiscentos menos a normal é igual a cento e vinte. [p=0.2] {d}A normal cai para quatrocentos e oitenta, [p=0.2] e {e}a balança mostra quarenta e oito."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] achar que {a}subindo, a balança sempre marca mais. [p=0.3] {b}Subindo com velocidade constante, a resultante é zero: [p=0.2] {c}a balança marca o de sempre, sessenta. [p=0.3] {d}O que manda é o sentido da aceleração, [p=0.1] não o sentido do movimento."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Aceleração para cima: [p=0.1] {b}normal igual a eme vezes, abre parênteses, gê mais á. [p=0.3] {c}Aceleração para baixo: [p=0.1] {d}eme vezes, abre parênteses, gê menos á. [p=0.3] {e}Sessenta vezes doze, setecentos e vinte, numa conta só."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a normal precisa segurar o peso e ainda dar a aceleração. [p=0.3] E dá um resultado famoso: [p=0.2] {b}se o elevador cai livre, á é igual a gê, [p=0.1] e {c}a normal é zero: você flutua. [p=0.3] {d}Não compensa quando você não sabe para onde aponta a aceleração: [p=0.2] aí, desenhe as forças."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma pessoa de cinquenta quilogramas está num elevador que desce e {b}vai freando, [p=0.2] com aceleração de {c}dois metros por segundo ao quadrado. [p=0.3] {d}Quanto marca a balança, em quilos?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Desce freando: a velocidade aponta para baixo e diminui, [p=0.2] então {b}a aceleração aponta para cima. [p=0.3] {c}Normal igual a cinquenta vezes, abre parênteses, dez mais dois: [p=0.2] {d}cinquenta vezes doze, seiscentos newtons. [p=0.3] {e}A balança mostra sessenta quilos. [p=0.2] Quem olhou só o descer usou dez menos dois, e achou quarenta quilos."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}peso é eme vezes gê, em newtons, [p=0.2] {b}massa é em quilogramas e não muda, [p=0.2] e {c}a normal sai da superfície e muda com a aceleração."),
    dict(id="s19", block="fim", text="Na próxima aula, entram {a}as forças dos fios e das molas: [p=0.2] {b}a tração, [p=0.1] {c}a força elástica [p=0.2] e {d}a balança de mola da feira. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
