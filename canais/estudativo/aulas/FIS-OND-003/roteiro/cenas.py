# Estudativo · FIS-OND-003 — Reflexão, refração e difração de ondas (Física · Ondas e Som · Ondas e seus fenômenos).
# Habilidade: dizer o que muda quando a onda troca de meio, com a frequência sempre igual, e quando ela contorna um obstáculo.
# Pré-requisitos: FIS-OND-002 (v = λ·f), FIS-OPT-004 (lei de Snell, normal). Próxima: FIS-OND-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Som no ar ≈ 340 m/s; na água ≈ 1.500 m/s (1.480 m/s a 20 °C: "cerca de").
# Tanque: onda em água rasa é mais lenta que em água funda. Voz: λ de ~10 cm a ~3 m; luz visível: 0,0004 a 0,0007 mm.

TITULO = "Reflexão, refração e difração de ondas"

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
    dict(id="s01", block="gancho", text="{a}Você ouve uma pessoa falando do outro lado do muro, [p=0.2] {b}mas não consegue ver essa pessoa. [p=0.3] {c}O som contorna o muro. [p=0.2] {d}A luz, quase nada. [p=0.2] Por quê?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber o que acontece quando uma onda {b}bate num obstáculo, [p=0.2] {c}troca de meio [p=0.1] ou {d}passa por uma fresta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a equação vê igual a lambda vezes efe; [p=0.2] e {c}a lei de Snell da luz, com o raio que se aproxima ou se afasta da normal, a reta a noventa graus da fronteira. [p=0.3] Se faltar alguma, procure no canal."),
    # reflexão
    dict(id="s04", block="reflexao", text="Primeiro, {a}a reflexão: a onda bate e volta para o mesmo meio. [p=0.2] {b}O eco é o som refletido numa parede. [p=0.3] Como ela continua no mesmo meio, {c}nada muda: [p=0.1] nem a velocidade, nem a frequência, nem o lambda. [p=0.2] E vale a regra do espelho: {d}o ângulo de chegada é igual ao de saída."),
    dict(id="s05", block="reflexao", text="No ar, o som anda a cerca de {a}trezentos e quarenta metros por segundo. [p=0.2] Grite de frente para um paredão a {b}cento e setenta metros: [p=0.2] o som vai e volta, {c}trezentos e quarenta metros, [p=0.2] e o eco chega {d}um segundo depois."),
    # refração
    dict(id="s06", block="refracao", text="Agora, {a}a refração: a onda passa para outro meio, [p=0.2] e {b}a velocidade muda. [p=0.3] Com a luz, você já viu isso. [p=0.2] Com a onda na água, também acontece: [p=0.1] {c}na parte rasa de um tanque, ela anda mais devagar que na parte funda."),
    dict(id="s07", block="refracao", text="E aqui está a regra de ouro: {a}na refração, a frequência não muda. [p=0.3] Quem decide a frequência é {b}a fonte. [p=0.2] Cada crista que chega na fronteira {c}passa para o outro lado: [p=0.2] nenhuma some, e nenhuma é criada. [p=0.3] {d}Então, o que muda junto com a velocidade é o lambda."),
    dict(id="s08", block="refracao", text="Uma onda de {a}dois hertz anda a {b}zero vírgula quatro metro por segundo na parte funda. [p=0.2] {c}Lambda é zero vírgula quatro dividido por dois: zero vírgula dois metro. [p=0.3] Na parte rasa, {d}a velocidade cai para zero vírgula dois. [p=0.2] A frequência continua dois, [p=0.1] e {e}o lambda cai para zero vírgula um metro. [p=0.2] {f}Metade da velocidade, metade do lambda."),
    dict(id="s09", block="refracao", text="Se a onda chega inclinada, {a}ela também muda de direção, como a luz. [p=0.2] {b}Entrando no meio mais lento, ela se aproxima da normal; [p=0.2] {c}entrando no mais rápido, se afasta. [p=0.3] {d}Se chega em cima da normal, muda a velocidade, mas segue reto."),
    # difração
    dict(id="s10", block="difracao", text="Por último, {a}a difração: a onda contorna obstáculos e se espalha depois de uma fresta. [p=0.3] Ela é forte quando {b}a fresta ou o obstáculo tem tamanho parecido com o lambda, ou menor."),
    dict(id="s11", block="difracao", text="O lambda do som da voz vai de {a}dezenas de centímetros a alguns metros, [p=0.2] o tamanho de portas e muros: [p=0.1] {b}o som contorna. [p=0.3] O lambda da luz é {c}menor que um milésimo de milímetro. [p=0.2] Diante de um muro, {d}a luz quase não contorna, e forma sombra."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: {a}achar que a frequência muda na refração. [p=0.2] A onda passa para um meio mais rápido, [p=0.1] e o aluno {b}acha que a frequência aumentou. [p=0.3] {c}Errado: o que aumentou foi o lambda. [p=0.2] {d}A frequência é da fonte, e a fonte não mudou."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}em nenhum desses três fenômenos a frequência muda: [p=0.1] nem na reflexão, nem na refração, nem na difração. [p=0.3] Então, {b}velocidade e lambda andam juntos, na mesma proporção: [p=0.2] {c}velocidade três vezes maior, lambda três vezes maior. [p=0.3] {d}Não compensa quando a questão já dá a frequência e a nova velocidade: [p=0.1] aí, use vê igual a lambda vezes efe direto."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um som de quinhentos hertz passa do ar, onde anda a trezentos e quarenta metros por segundo, [p=0.2] {b}para a água, onde anda a cerca de mil e quinhentos. [p=0.3] {c}Na água, qual é a frequência, e qual é o lambda?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}A frequência não muda: [p=0.1] {b}quinhentos hertz. [p=0.3] {c}Lambda é vê dividido por efe: [p=0.1] {d}mil e quinhentos dividido por quinhentos, [p=0.1] {e}três metros. [p=0.3] No ar, eram {f}zero vírgula sessenta e oito metro: [p=0.2] o som ficou mais rápido, e o lambda, mais comprido."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}na reflexão, a onda volta; [p=0.1] {b}na refração, mudam a velocidade e o lambda; [p=0.1] {c}na difração, ela contorna; [p=0.2] e, {d}nos três, a frequência não muda."),
    dict(id="s18", block="fim", text="Na próxima aula, {a}duas ondas se encontram: [p=0.2] elas podem {b}se reforçar [p=0.1] ou {c}se apagar, como no fone que cancela ruído. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
