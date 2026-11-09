# Estudativo · FIS-DIN-007 — Força de atrito: estático e cinético (Física · Dinâmica · Atrito, plano inclinado e sistemas).
# Habilidade: calcular o atrito com μ·N, dizer se o bloco se move e explicar por que o freio ABS encurta a frenagem.
# Pré-requisitos: FIS-DIN-004 (peso e normal). Próxima: FIS-DIN-008.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# g = 10 m/s². Tração (FIS-DIN-005) não está em "Já ensinado": as forças são "empurrar". Torricelli (FIS-CIN-009) está.
# Coeficientes do ABS (0,8 e 0,5) são ilustrativos, para asfalto seco; o texto não os apresenta como medidos.

TITULO = "Força de atrito: estático e cinético"

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
    dict(id="s01", block="gancho", text="{a}Empurrar um armário parado é difícil. [p=0.2] {b}Depois que ele começa a deslizar, fica mais fácil. [p=0.3] E é pelo mesmo motivo que {c}o freio ABS para o carro em menos metros."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}calcular o atrito, [p=0.2] {c}dizer se um bloco se move [p=0.2] e {d}explicar o freio ABS."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a normal, que no chão plano é igual ao peso, eme vezes gê; [p=0.2] e {c}força resultante igual a massa vezes aceleração. [p=0.3] Se faltar alguma, procure no canal."),
    # atrito
    dict(id="s04", block="atrito", text="{a}Atrito é a força que o chão faz contra o deslizamento. [p=0.2] Ela é {b}paralela ao chão [p=0.1] e {c}aponta contra o deslizamento, ou contra a tentativa de deslizar. [p=0.3] Ela vem das {d}pequenas asperezas das duas superfícies, que se prendem."),
    dict(id="s05", block="atrito", text="O atrito depende de {a}duas coisas: [p=0.2] {b}de quanto as superfícies se apertam, que é a normal, de letra ene, [p=0.2] e {c}do tipo de material, que é o coeficiente de atrito, a letra grega mi. [p=0.3] {d}Mi não tem unidade: é só um número, como zero vírgula quatro."),
    # estático
    dict(id="s06", block="estatico", text="{a}Com o corpo parado, o atrito é estático. [p=0.3] E ele {b}se ajusta: [p=0.2] {c}empurre com cem newtons, e o atrito faz cem para trás; [p=0.2] {d}empurre com duzentos, ele faz duzentos. [p=0.3] Até um limite: [p=0.1] {e}o atrito estático máximo, mi estático vezes ene."),
    dict(id="s07", block="estatico", text="{a}Um armário de quarenta quilogramas: [p=0.2] {b}normal de quatrocentos newtons. [p=0.2] {c}Mi estático de zero vírgula seis: [p=0.2] {d}o máximo é duzentos e quarenta newtons. [p=0.3] {e}Empurrou com duzentos? [p=0.1] {f}Não se move, e o atrito vale duzentos. [p=0.2] {g}Para sair do lugar, mais de duzentos e quarenta."),
    # cinético
    dict(id="s08", block="cinetico", text="{a}Depois que desliza, o atrito é cinético: [p=0.2] {b}mi cinético vezes ene, sempre o mesmo valor. [p=0.3] E {c}mi cinético costuma ser menor que o estático. [p=0.3] É por isso que o armário fica mais fácil de empurrar depois que começa a andar."),
    dict(id="s09", block="cinetico", text="No armário, {a}mi cinético é zero vírgula quatro: [p=0.2] {b}atrito de cento e sessenta newtons. [p=0.3] {c}Empurrando com trezentos, ele desliza, [p=0.2] e {d}a resultante é trezentos menos cento e sessenta, cento e quarenta. [p=0.3] {e}Cento e quarenta dividido por quarenta: três vírgula cinco metros por segundo ao quadrado."),
    # ABS
    dict(id="s10", block="abs", text="Agora, o freio ABS. [p=0.2] {a}Sem ABS, numa freada forte, a roda trava e o pneu desliza no asfalto: [p=0.2] {b}atrito cinético, o menor. [p=0.3] {c}O ABS solta e aperta o freio muitas vezes por segundo, [p=0.2] e a roda {d}continua girando sem deslizar: [p=0.2] {e}atrito estático, o maior."),
    dict(id="s11", block="abs", text="Com o atrito freando sozinho, {a}a desaceleração é mi vezes gê, como você vai ver no atalho. [p=0.3] {b}A vinte metros por segundo, com mi de zero vírgula oito, [p=0.2] á é oito, e Torricelli diz que o carro {c}para em vinte e cinco metros. [p=0.3] {d}Travado, com mi de zero vírgula cinco, [p=0.2] á é cinco, e o carro {e}para em quarenta metros. [p=0.3] {f}Quinze metros de diferença."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar mi estático vezes ene como atrito, sempre. [p=0.3] {b}No armário empurrado com duzentos, [p=0.2] o atrito {c}não é duzentos e quarenta. [p=0.2] Se fosse, {d}sobraria força para trás, e o armário andaria sozinho para trás. [p=0.3] {e}Mi vezes ene é só o limite."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}No chão plano, com só o atrito freando, [p=0.2] {b}á é igual a mi vezes gê: [p=0.1] {c}a massa nem entra na conta. [p=0.3] {d}Mi de zero vírgula cinco? [p=0.1] {e}Cinco metros por segundo ao quadrado, para qualquer carro."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o atrito é mi vezes eme vezes gê, [p=0.2] e a segunda lei {b}divide pela mesma massa. [p=0.3] {c}Não compensa quando outra força empurra junto, [p=0.2] ou quando {d}a normal não é igual ao peso."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma caixa de cinquenta quilogramas está parada no chão. [p=0.2] {b}Mi estático vale zero vírgula cinco, [p=0.1] e {c}mi cinético, zero vírgula três. [p=0.3] {d}Você empurra com duzentos newtons. [p=0.2] {e}Ela se move? [p=0.2] {f}Quanto vale o atrito?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Normal igual ao peso, quinhentos newtons. [p=0.2] {b}Limite do estático: zero vírgula cinco vezes quinhentos, duzentos e cinquenta. [p=0.3] {c}Duzentos é menos que duzentos e cinquenta: [p=0.1] {d}a caixa não se move. [p=0.3] {e}O atrito é estático e vale duzentos newtons, [p=0.1] igual ao empurrão. [p=0.3] {f}O mi cinético estava ali só para confundir."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}parado, o atrito se ajusta até mi estático vezes ene; [p=0.2] {b}deslizando, vale mi cinético vezes ene; [p=0.2] e {c}o ABS freia com o estático, que é maior."),
    dict(id="s19", block="fim", text="Na próxima aula, o chão {a}fica inclinado: [p=0.2] você vai {b}dividir o peso em duas partes [p=0.2] e achar {c}a aceleração de um bloco na rampa. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
