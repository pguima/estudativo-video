# Estudativo · FIS-CIN-010 — Praticando: vetores e movimentos (Física · Cinemática · Movimento uniforme e variado · prática).
# Habilidade: escolher a equação certa para cada problema de vetores, movimento uniforme e movimento variado.
# Pré-requisitos: FIS-CIN-001, 002, 004, 005, 006, 007, 008, 009. Próxima: FIS-CIN-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Prática: cinco questões inéditas, criadas para esta aula. FIS-CIN-003 (decomposição) não está em "Já ensinado".

TITULO = "Praticando: vetores e movimentos"

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
    dict(id="s01", block="gancho", text="Numa prova de Física, {a}a dificuldade quase nunca é a conta. [p=0.2] É {b}escolher a fórmula. [p=0.3] {c}Até o fim desta aula, você vai resolver cinco questões de vetores e movimentos, [p=0.2] e escolher a equação certa {d}em segundos."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as aulas deste módulo: [p=0.2] {a}soma de vetores, [p=0.1] {b}movimento uniforme e encontro, [p=0.1] {c}e as equações do movimento com aceleração. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s03", block="metodo", text="Primeiro, o método. [p=0.2] {a}A velocidade é constante? [p=0.1] É movimento uniforme: {b}esse igual a esse zero mais vê tê. [p=0.3] {c}A velocidade muda? [p=0.1] Aí são quatro ferramentas, [p=0.1] e cada uma {d}deixa uma grandeza de fora."),
    dict(id="s04", block="metodo", text="{a}Vê igual a vê zero mais á tê não tem o deslocamento. [p=0.2] {b}O sorvetão não tem a velocidade final. [p=0.2] {c}Torricelli não tem o tempo. [p=0.2] {d}E a média das velocidades não tem a aceleração. [p=0.3] {e}São cinco grandezas: vê zero, vê, á, tê e delta esse. [p=0.2] Liste o que a questão dá e o que ela pede. [p=0.2] {f}A grandeza que não aparece em nenhum dos dois diz qual ferramenta usar."),
    # questão 1
    dict(id="s05", block="q1", text="Questão um. [p=0.2] {a}Um avião pequeno voa para o norte a quarenta metros por segundo, [p=0.2] e {b}o vento o empurra para o leste a trinta. [p=0.3] {c}Qual é a velocidade do avião para quem está no chão? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s06", block="q1", text="{a}Norte e leste fazem ângulo reto: [p=0.2] Pitágoras. [p=0.2] {b}Trinta, quarenta e cinquenta formam o terno três, quatro, cinco, vezes dez. [p=0.2] {c}Cinquenta metros por segundo. [p=0.3] {d}Setenta seria somar os módulos, [p=0.1] e isso só vale com as setas em fila."),
    # questão 2
    dict(id="s07", block="q2", text="Questão dois. [p=0.2] Numa avenida reta, dois carros vêm {a}um em direção ao outro. [p=0.2] {b}Um está na posição zero, a vinte metros por segundo. [p=0.2] {c}O outro está na posição seiscentos metros, a dez metros por segundo. [p=0.3] {d}Quando e onde eles se cruzam? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s08", block="q2", text="Velocidade constante e {a}sentidos opostos: o atalho. [p=0.2] {b}Vinte mais dez, trinta metros por segundo. [p=0.2] {c}Seiscentos dividido por trinta: vinte segundos. [p=0.3] {d}Onde? O primeiro anda vinte vezes vinte: posição quatrocentos metros."),
    # questão 3
    dict(id="s09", block="q3", text="Questão três. [p=0.2] {a}Uma bicicleta parte do repouso e chega a seis metros por segundo em quatro segundos, [p=0.1] com aceleração constante. [p=0.3] {b}Quanto ela andou? [p=0.2] {c}Pause e tente. [p=3.0]"),
    dict(id="s10", block="q3", text="Liste: {a}vê zero, zero; [p=0.1] vê, seis; [p=0.1] tê, quatro. [p=0.2] Pede {b}o deslocamento. [p=0.2] {c}Ninguém falou de aceleração: [p=0.2] use a média das velocidades. [p=0.3] {d}Zero mais seis, dividido por dois, três. [p=0.2] {e}Três vezes quatro: doze metros."),
    # questão 4
    dict(id="s11", block="q4", text="Questão quatro. [p=0.2] {a}Um avião precisa chegar a sessenta metros por segundo para decolar. [p=0.2] {b}Ele parte do repouso com aceleração de três metros por segundo ao quadrado. [p=0.3] {c}Qual é o comprimento mínimo da pista? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s12", block="q4", text="Dá {a}vê zero, vê e á. [p=0.2] Pede {b}o deslocamento. [p=0.2] {c}O tempo não aparece: Torricelli. [p=0.3] {d}Sessenta ao quadrado, três mil e seiscentos, igual a zero mais duas vezes três vezes delta esse. [p=0.2] {e}Três mil e seiscentos dividido por seis: seiscentos metros."),
    # questão 5
    dict(id="s13", block="q5", text="Questão cinco. [p=0.2] {a}Um carro anda de ré, a menos dez metros por segundo, [p=0.1] com aceleração de menos dois metros por segundo ao quadrado. [p=0.3] {b}Qual é a velocidade três segundos depois? [p=0.2] {c}E o movimento é acelerado ou retardado? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s14", block="q5", text="Pede {a}a velocidade, e o deslocamento não aparece: [p=0.2] {b}vê igual a vê zero mais á tê. [p=0.3] {c}Menos dez, somado com menos dois vezes três, que dá menos seis: [p=0.2] {d}menos dezesseis metros por segundo. [p=0.3] {e}Velocidade e aceleração negativas: sinais iguais, acelerado. [p=0.2] Aceleração negativa não quer dizer freada."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: {a}velocidade constante, sorvete; [p=0.2] {b}velocidade mudando, escolha pela grandeza que falta. [p=0.3] Na próxima aula, o movimento vira desenho: [p=0.2] {c}o gráfico da posição pelo tempo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
