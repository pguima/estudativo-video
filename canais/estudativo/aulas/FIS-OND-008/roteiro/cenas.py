# Estudativo · FIS-OND-008 — Efeito Doppler (Física · Ondas e Som · Som e efeito Doppler).
# Habilidade: explicar a sirene que muda de tom e calcular a frequência percebida com o atalho de sinais da fórmula.
# Pré-requisitos: FIS-OND-006 (altura = frequência), MAT-EQU-010 (equação com frações). Próxima: FIS-OND-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. f' = f·(v ± vo)/(v ∓ vf), com o sinal escolhido pelo sentido (aproximar faz f' subir).
# 720·340/320 = 765; 720·340/360 = 680; 680/600 = 17/15 → 340 − vf = 300 → vf = 40 m/s = 144 km/h.

TITULO = "Efeito Doppler"

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
    dict(id="s01", block="gancho", text="{a}A ambulância vem chegando, [p=0.1] e a sirene soa {b}aguda. [p=0.2] {c}Ela passa por você, [p=0.1] e o som {d}fica grave. [p=0.3] {e}Mas a sirene não mudou nada."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar essa mudança [p=0.2] e calcular {b}a frequência que você ouve, [p=0.2] com {c}um atalho para os sinais da fórmula."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}frequência alta é som agudo, e baixa é som grave; [p=0.2] e {c}resolver uma equação com fração. [p=0.3] Se faltar alguma, procure no canal."),
    # por quê
    dict(id="s04", block="porque", text="A sirene solta {a}uma crista atrás da outra, [p=0.1] e cada uma se espalha como um círculo. [p=0.3] {b}Com a ambulância parada, as cristas ficam igualmente espaçadas, [p=0.1] e todo mundo ouve a mesma frequência."),
    dict(id="s05", block="porque", text="{a}Com a ambulância andando, cada crista sai de um ponto mais à frente. [p=0.3] {b}Na frente dela, as cristas se apertam: [p=0.1] lambda menor, {c}mais cristas chegam por segundo, som mais agudo. [p=0.3] {d}Atrás, elas se espalham: [p=0.1] lambda maior, {e}som mais grave. [p=0.3] Esse é o {f}efeito Doppler."),
    dict(id="s06", block="porque", text="Funciona também com {a}você se mexendo. [p=0.2] {b}Indo na direção da sirene, você encontra as cristas mais depressa: [p=0.1] ouve mais agudo. [p=0.2] {c}Fugindo dela, mais grave. [p=0.3] {d}O que importa é se a distância diminui ou aumenta."),
    # fórmula
    dict(id="s07", block="formula", text="A fórmula é esta: [p=0.2] {a}efe linha igual a efe vezes uma fração. [p=0.2] {b}Em cima, vê mais ou menos a velocidade de quem ouve, o observador. [p=0.2] {c}Embaixo, vê mais ou menos a velocidade de quem emite, a fonte. [p=0.3] {d}Efe é a frequência da sirene, [p=0.1] {e}efe linha, efe com um tracinho, a que você ouve, as duas em hertz; [p=0.1] e {f}vê, a velocidade do som, trezentos e quarenta metros por segundo."),
    dict(id="s08", block="formula", text="E os sinais? [p=0.2] Pense no som: [p=0.2] {a}quem anda em direção ao outro faz a frequência subir. [p=0.2] Então, escolha o sinal que {b}deixa a fração maior: [p=0.2] {c}mais em cima, se é você que vai em direção à fonte; [p=0.2] {d}menos embaixo, se é a fonte que vem em sua direção. [p=0.3] {e}Quem se afasta faz a frequência cair: menos em cima, mais embaixo. [p=0.3] {f}Quem está parado tem velocidade zero, e o termo some."),
    # exemplo
    dict(id="s09", block="exemplo", text="Uma ambulância com sirene de {a}setecentos e vinte hertz vem {b}a vinte metros por segundo na sua direção. [p=0.2] Você está parado: {c}em cima, só trezentos e quarenta. [p=0.2] A fonte se aproxima: {d}embaixo, trezentos e quarenta menos vinte, trezentos e vinte."),
    dict(id="s10", block="exemplo", text="{a}Setecentos e vinte dividido por trezentos e vinte simplifica para nove quartos. [p=0.2] {b}Nove quartos de trezentos e quarenta: [p=0.1] {c}setecentos e sessenta e cinco hertz. [p=0.3] {d}Depois que ela passa, ela se afasta: [p=0.1] mais embaixo, trezentos e sessenta. [p=0.2] Setecentos e vinte dividido por trezentos e sessenta dá dois, [p=0.1] {e}e duas vezes trezentos e quarenta, seiscentos e oitenta hertz. [p=0.3] Mais agudo na chegada, mais grave na saída."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: {a}trocar os sinais. [p=0.2] Com a ambulância chegando, a pessoa põe {b}trezentos e quarenta mais vinte embaixo [p=0.1] e acha {c}seiscentos e oitenta hertz, mais grave que a sirene. [p=0.3] {d}Absurdo: quem se aproxima soa mais agudo. [p=0.2] Se a conta deu o contrário, {e}o sinal está trocado."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}antes da conta, decida se a resposta é maior ou menor. [p=0.2] {b}Aproximou: maior que a frequência da fonte. [p=0.1] {c}Afastou: menor. [p=0.3] Só isso já {d}corta metade das alternativas, [p=0.1] e escolhe os sinais por você. [p=0.3] {e}Não basta quando um se aproxima e o outro se afasta, como numa perseguição: [p=0.1] aí, monte a fórmula com o sinal de cada um."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Uma sirene de seiscentos hertz se aproxima de você, que está parado. [p=0.2] {b}Você ouve seiscentos e oitenta hertz. [p=0.2] {c}O som anda a trezentos e quarenta metros por segundo. [p=0.3] {d}Qual é a velocidade da sirene?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=0.3] {b}Uma dica: compare as frequências antes de mexer na equação. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}A sirene se aproxima: menos embaixo. [p=0.2] {b}Seiscentos e oitenta é igual a seiscentos vezes trezentos e quarenta, dividido por trezentos e quarenta menos vê da fonte. [p=0.3] {c}Divida os dois lados por seiscentos: [p=0.1] {d}a fração vale seiscentos e oitenta dividido por seiscentos, [p=0.1] que simplifica para dezessete quinze avos."),
    dict(id="s16", block="resposta", text="{a}Então, trezentos e quarenta dividido pelo de baixo vale dezessete quinze avos. [p=0.2] Trezentos e quarenta é vinte vezes dezessete, [p=0.1] {b}então o de baixo é vinte vezes quinze: trezentos. [p=0.3] {c}Trezentos e quarenta menos vê é trezentos: [p=0.1] {d}a sirene vem a quarenta metros por segundo, [p=0.1] {e}cento e quarenta e quatro quilômetros por hora."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}aproximou, mais agudo; afastou, mais grave; [p=0.2] {b}a sirene não muda, muda o que chega ao seu ouvido; [p=0.2] e {c}escolha o sinal que leva a resposta para o lado certo."),
    dict(id="s18", block="fim", text="Na próxima aula, você {a}pratica tudo de som: [p=0.2] {b}decibéis, instrumentos, ressonância e Doppler. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
