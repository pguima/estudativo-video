# Estudativo · FIS-OPT-004 — Índice de refração e lei de Snell (Física · Óptica · Refração, lentes e olho humano).
# Habilidade: calcular n = c/v e usar n1·sen i = n2·sen r, dizendo se o raio se aproxima ou se afasta da normal.
# Pré-requisitos: FIS-OPT-002 (normal, ângulo medido da normal), MAT-TRI-003 (30°, 45°, 60°), MAT-EQU-011 (isolar letra). Próxima: FIS-OPT-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Notação científica (MAT-POT-012) não está em "Já ensinado": c = 300.000 km/s.
# Água n ≈ 1,33 só citada (dividir por fração não está em "Já ensinado"). Vidro comum n ≈ 1,5 (v ≈ 200.000 km/s).

TITULO = "Índice de refração e lei de Snell"

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
    dict(id="s01", block="gancho", text="{a}Um lápis dentro de um copo d'água parece quebrado. [p=0.3] {b}Ele não quebrou. [p=0.2] Quem mudou de caminho foi {c}a luz."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}o índice de refração [p=0.2] e usar {c}a lei de Snell [p=0.2] para dizer {d}para onde o raio entorta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a normal, a reta a noventa graus da superfície, de onde se medem os ângulos; [p=0.2] e {c}o seno de trinta, quarenta e cinco e sessenta graus. [p=0.3] Se faltar alguma, procure no canal."),
    # refração
    dict(id="s04", block="refracao", text="Quando a luz passa de um meio para outro, como {a}do ar para a água, [p=0.2] {b}a velocidade dela muda. [p=0.2] Isso é {c}a refração. [p=0.3] {d}Se a luz chega inclinada, ela também muda de direção. [p=0.2] {e}Se chega em cima da normal, muda a velocidade, mas segue reto."),
    dict(id="s05", block="refracao", text="Pense num carrinho de supermercado {a}saindo do piso liso para a grama, meio de lado. [p=0.3] {b}A roda que entra primeiro freia antes, [p=0.2] e {c}o carrinho vira. [p=0.3] Com a luz é parecido: {d}a parte do feixe que entra primeiro no meio mais lento fica para trás, e o feixe entorta."),
    # índice
    dict(id="s06", block="indice", text="{a}No vácuo, a luz anda a cerca de trezentos mil quilômetros por segundo. [p=0.2] Esse valor se chama {b}cê. [p=0.3] {c}O índice de refração, ene, diz quantas vezes a luz é mais lenta num meio: [p=0.2] {d}ene é igual a cê dividido por vê, [p=0.2] onde vê é a velocidade da luz naquele meio."),
    dict(id="s07", block="indice", text="{a}No vidro comum, a luz anda a uns duzentos mil quilômetros por segundo. [p=0.3] {b}Trezentos mil dividido por duzentos mil: [p=0.2] {c}ene igual a um vírgula cinco. [p=0.3] {d}Quilômetro por segundo corta com quilômetro por segundo: [p=0.2] o índice não tem unidade."),
    dict(id="s08", block="indice", text="{a}No vácuo, ene é um, [p=0.2] e no ar, quase um. [p=0.2] {b}Na água, perto de um vírgula três. [p=0.3] {c}O índice nunca é menor que um, [p=0.2] porque nada é mais rápido que a luz no vácuo. [p=0.3] {d}Quanto maior o ene, mais lenta a luz: [p=0.2] dizemos que o meio é {e}mais refringente."),
    # Snell
    dict(id="s09", block="snell", text="E para onde o raio entorta? [p=0.2] {a}O ângulo i, de incidência, fica no meio um, [p=0.2] {b}e o ângulo r, de refração, fica no meio dois. [p=0.2] {c}Os dois medidos a partir da normal."),
    dict(id="s10", block="snell", text="A lei de Snell diz: [p=0.2] {a}ene um vezes seno de i [p=0.1] é igual a {b}ene dois vezes seno de r. [p=0.3] {c}O produto do índice pelo seno é o mesmo dos dois lados."),
    dict(id="s11", block="snell", text="Exemplo: {a}do ar, com ene igual a um, [p=0.2] {b}para um vidro de índice raiz de três, [p=0.2] {c}chegando a sessenta graus da normal. [p=0.3] {d}Um vezes seno de sessenta, raiz de três dividido por dois, [p=0.2] é igual a raiz de três vezes seno de r."),
    dict(id="s12", block="snell", text="{a}Divida os dois lados por raiz de três: [p=0.2] {b}seno de r é um meio. [p=0.2] {c}O ângulo cujo seno é um meio é trinta graus. [p=0.3] {d}O raio foi de sessenta para trinta: [p=0.2] {e}se aproximou da normal."),
    dict(id="s13", block="snell", text="A regra geral: [p=0.2] {a}entrando num meio mais refringente, o raio se aproxima da normal. [p=0.3] {b}Saindo para um meio menos refringente, ele se afasta. [p=0.3] {c}É por isso que o lápis parece quebrado: [p=0.2] a luz que vem dele se afasta da normal ao sair da água."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}virar a fração do índice: [p=0.2] {b}vê dividido por cê. [p=0.3] No vidro, isso dá {c}dois terços, menos que um. [p=0.3] {d}E índice menor que um diria que a luz é mais rápida que no vácuo. [p=0.2] {e}Deu menos que um? A fração está de cabeça para baixo."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Maior índice, menor ângulo. [p=0.3] {b}Como ene vezes seno é o mesmo dos dois lados, [p=0.2] {c}onde o ene é grande, o seno tem que ser pequeno, e o ângulo também. [p=0.3] {d}Sem conta, você já corta as alternativas com o raio entortando para o lado errado."),
    dict(id="s16", block="atalho", text="E mais um: {a}índice e velocidade andam ao contrário. [p=0.2] {b}Índice dobrou, a velocidade caiu pela metade. [p=0.3] {c}Num meio de índice dois, a luz anda a cento e cinquenta mil quilômetros por segundo. [p=0.3] {d}Para achar o ângulo exato, porém, só fazendo a conta da lei de Snell."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um raio passa {a}do ar para um líquido de índice raiz de dois, [p=0.2] {b}chegando a quarenta e cinco graus da normal. [p=0.3] {c}Qual é o ângulo de refração? [p=0.2] E {d}o raio se aproxima ou se afasta da normal?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Um vezes seno de quarenta e cinco, raiz de dois dividido por dois, [p=0.2] {b}é igual a raiz de dois vezes seno de r. [p=0.3] {c}Dividindo por raiz de dois, seno de r é um meio: [p=0.2] {d}r é trinta graus."),
    dict(id="s20", block="resposta", text="{a}De quarenta e cinco para trinta: o raio se aproximou da normal, [p=0.2] {b}como manda o atalho, [p=0.2] porque o líquido é mais refringente que o ar."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}ene é cê dividido por vê, e nunca é menor que um; [p=0.2] {b}ene um vezes seno de i é igual a ene dois vezes seno de r; [p=0.2] e {c}maior índice, menor ângulo com a normal."),
    dict(id="s22", block="fim", text="Na próxima aula, a luz {a}tenta sair e não consegue: [p=0.2] {b}a reflexão total, que prende a luz na fibra óptica, [p=0.2] e {c}as cores do arco-íris. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
