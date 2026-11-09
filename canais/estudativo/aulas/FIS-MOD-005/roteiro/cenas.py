# Estudativo · FIS-MOD-005 — Relatividade restrita (Física · Física Moderna · Quantização, dualidade e relatividade).
# Habilidade: calcular dilatação do tempo e contração do comprimento.
# Pré-requisitos: FIS-OND-010 (luz, c = 3 × 10⁸ m/s). Próxima: FIS-MOD-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# "Já ensinado" desta aula não tem FIS-MOD-001 a 004: não são citadas. Tem raiz (MAT-POT-007/016) e ternos pitagóricos
# (MAT-ANG-016), base do atalho: 0,6² + 0,8² = 1 → v = 0,6c dá γ = 1/0,8 = 1,25; v = 0,8c dá γ = 1/0,6 = 5/3.
# Fatos: Einstein, 1905. Múon: vida média de 2,2 μs em repouso, nasce a ~15 km de altura. GPS corrige os relógios pela relatividade.
# Δt = γ·Δt₀ (tempo próprio Δt₀ = o do relógio que viaja junto); L = L₀/γ (comprimento próprio L₀ = medido parado em relação ao corpo).

TITULO = "Relatividade restrita"

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
    dict(id="s01", block="gancho", text="{a}Uma astronauta viaja numa nave muito rápida e volta {b}oito anos mais velha. [p=0.3] {c}O irmão gêmeo dela, que ficou na Terra, [p=0.2] {d}envelheceu dez. [p=0.3] Não é ficção: [p=0.1] {e}é uma conta da relatividade."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular quanto o tempo dilata [p=0.2] e {b}quanto o comprimento contrai [p=0.1] para quem anda perto da velocidade da luz."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a luz anda a três vezes dez elevado a oito metros por segundo, a velocidade cê; [p=0.2] e {c}a raiz quadrada. [p=0.3] Se faltar alguma, procure no canal."),
    # os postulados
    dict(id="s04", block="postulados", text="Em mil novecentos e cinco, {a}Einstein partiu de duas ideias. [p=0.3] {b}Primeira: as leis da Física são as mesmas para quem está parado e para quem anda em linha reta, com velocidade constante. [p=0.2] {c}Dentro de um avião em voo tranquilo, um copo cai igual ao de casa."),
    dict(id="s05", block="postulados", text="{a}Segunda: a luz no vácuo tem a mesma velocidade para todo mundo. [p=0.3] {b}Uma nave a metade da velocidade da luz acende o farol. [p=0.2] {c}Quem está na nave mede cê. [p=0.2] {d}Quem está parado lá fora também mede cê, [p=0.1] {e}e não uma vez e meia cê. [p=0.3] Para isso dar certo, {f}quem tem que mudar é o tempo."),
    # dilatação
    dict(id="s06", block="tempo", text="Imagine um relógio de luz na nave: [p=0.2] {a}um pulso de luz que sobe e desce entre dois espelhos. [p=0.3] {b}Para a astronauta, a luz faz um caminho reto. [p=0.2] {c}Para quem vê de fora, a nave anda, e a luz faz um caminho inclinado, mais comprido. [p=0.3] {d}Mesma velocidade, caminho maior: [p=0.1] {e}de fora, cada tique demora mais."),
    dict(id="s07", block="tempo", text="Essa é a {a}dilatação do tempo. [p=0.2] {b}O tempo de fora é gama vezes o tempo da nave. [p=0.3] {c}O tempo da nave, medido pelo relógio que viaja junto, se chama tempo próprio. [p=0.2] E {d}gama é o fator de Lorentz: [p=0.1] {e}um dividido pela raiz de um menos vê ao quadrado sobre cê ao quadrado, [p=0.1] onde vê é a velocidade da nave."),
    dict(id="s08", block="tempo", text="Vamos ao gêmeo. [p=0.2] A nave anda a {a}zero vírgula seis cê. [p=0.2] {b}Vê sobre cê é zero vírgula seis; ao quadrado, zero vírgula trinta e seis. [p=0.2] {c}Um menos zero vírgula trinta e seis: zero vírgula sessenta e quatro. [p=0.2] {d}A raiz é zero vírgula oito, [p=0.1] e {e}gama é um dividido por zero vírgula oito: um vírgula vinte e cinco."),
    dict(id="s09", block="tempo", text="{a}Oito anos na nave vezes um vírgula vinte e cinco: [p=0.2] {b}dez anos na Terra. [p=0.3] E existe prova: [p=0.2] {c}o múon, uma partícula que nasce no alto da atmosfera e vive pouquíssimo. [p=0.2] {d}Ele só chega ao chão porque, para nós, o tempo dele passa mais devagar."),
    # contração
    dict(id="s10", block="comprimento", text="{a}O comprimento também muda. [p=0.2] {b}Quem vê a nave passar a mede mais curta, na direção do movimento. [p=0.3] {c}O comprimento de fora é o comprimento próprio dividido por gama. [p=0.2] {d}Comprimento próprio é o medido por quem está parado junto da nave. [p=0.3] {e}Uma nave de cem metros, a zero vírgula seis cê: [p=0.1] {f}cem dividido por um vírgula vinte e cinco, oitenta metros."),
    dict(id="s11", block="comprimento", text="{a}Gama é sempre maior que um, e cresce sem limite perto de cê. [p=0.2] {b}Por isso, nada com massa chega à velocidade da luz. [p=0.3] {c}Na velocidade de um avião, gama é praticamente um, [p=0.1] e {d}o efeito não aparece no dia a dia."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}dividir o tempo, em vez de multiplicar. [p=0.3] {b}Oito dividido por um vírgula vinte e cinco dá seis vírgula quatro anos na Terra. [p=0.2] {c}Mas o tempo de quem vê de fora tem que ser o maior. [p=0.3] {d}A regra para não errar: [p=0.1] {e}de fora, o tempo é maior e o comprimento é menor. [p=0.2] {f}Gama sempre multiplica o tempo e divide o comprimento."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}as velocidades das questões quase sempre são zero vírgula seis cê ou zero vírgula oito cê. [p=0.3] {b}Pense no triângulo três, quatro, cinco: [p=0.2] {c}zero vírgula seis ao quadrado mais zero vírgula oito ao quadrado dá um. [p=0.3] {d}Então a raiz da fórmula é sempre o outro número."),
    dict(id="s14", block="atalho", text="{a}Zero vírgula seis cê: a raiz é zero vírgula oito, [p=0.1] e gama é cinco quartos, um vírgula vinte e cinco. [p=0.2] {b}Zero vírgula oito cê: a raiz é zero vírgula seis, [p=0.1] e gama é cinco terços. [p=0.3] {c}Não compensa com outras velocidades: [p=0.1] aí, faça a conta da raiz."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma nave de cinquenta metros viaja a zero vírgula oito cê. [p=0.2] {b}Na Terra, a viagem dura trinta anos. [p=0.3] {c}Quanto tempo passa para quem está na nave? [p=0.2] E {d}qual é o comprimento da nave para quem a vê passar?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Zero vírgula oito cê: gama é cinco terços. [p=0.3] {b}O tempo da Terra é gama vezes o tempo da nave. [p=0.2] {c}Trinta igual a cinco terços vezes o tempo da nave. [p=0.2] {d}Trinta vezes três quintos: [p=0.1] {e}dezoito anos na nave."),
    dict(id="s18", block="resposta", text="{a}E o comprimento: [p=0.1] cinquenta dividido por cinco terços. [p=0.2] {b}Cinquenta vezes três quintos: [p=0.1] {c}trinta metros. [p=0.3] {d}Confira a regra: [p=0.1] tempo de fora maior, trinta anos contra dezoito; [p=0.1] comprimento de fora menor, trinta metros contra cinquenta."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a luz tem a mesma velocidade para todos; [p=0.2] {b}de fora, o tempo é gama vezes maior [p=0.1] {c}e o comprimento, gama vezes menor; [p=0.2] e {d}com zero vírgula seis e zero vírgula oito, use o três, quatro, cinco."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}a relatividade junta massa e energia [p=0.2] na fórmula mais famosa da Física: {b}energia igual a massa vezes cê ao quadrado. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
