# Estudativo · MAT-RAZ-001 — O que é razão (Matemática · Razão e Proporção).
# Habilidade: escrever 3 meninos para 5 meninas como 3/5 e calcular a razão entre 50 cm e 2 m, na mesma unidade.
# Pré-requisitos: MAT-FRA-003 (equivalentes e simplificação), MAT-MED-001 (escada do metro). Próxima: MAT-RAZ-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sem divisão com resultado decimal (MAT-FRA-017 não está na cadeia).

TITULO = "O que é razão"

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
    dict(id="s01", block="gancho", text="Compare {a}uma fita de cinquenta centímetros [p=0.2] com {b}uma fita de dois metros. [p=0.3] Tem gente que divide cinquenta por dois e conclui: {c}vinte e cinco. [p=0.3] Vinte e cinco vezes o quê? [p=0.2] {d}A fita de cinquenta é a menor!"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você compara duas quantidades do jeito certo, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}simplificar fração, dividindo em cima e embaixo pelo mesmo número, [p=0.2] e {c}converter comprimento na escada do metro. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é razão
    dict(id="s04", block="razao", text="Numa turma, há {a}três meninos para cada cinco meninas. [p=0.3] Essa frase compara duas quantidades. [p=0.2] Em matemática, essa comparação se chama {b}razão."),
    dict(id="s05", block="razao", text="{a}Razão é a comparação de dois números por meio da divisão. [p=0.3] Você escreve como uma fração: {b}três quintos. [p=0.2] E lê de um jeito próprio: {c}três para cinco. [p=0.3] Em alguns livros, ela aparece com {d}dois-pontos entre os números. [p=0.2] Lê-se do mesmo jeito: três para cinco."),
    dict(id="s06", block="razao", text="O sentido é este: {a}a cada três meninos, aparecem cinco meninas. [p=0.3] Se a turma tiver {b}nove meninos e quinze meninas, [p=0.2] a razão é {c}nove quinze avos. [p=0.2] Divida em cima e embaixo por três: {d}três quintos de novo. [p=0.3] Razão se simplifica igual à fração. [p=0.2] Repare: a razão {e}não diz quantos alunos há. [p=0.2] Diz só como eles se repartem."),
    # ordem
    dict(id="s07", block="ordem", text="Na razão, {a}a ordem importa. [p=0.3] Meninos para meninas é {b}três quintos. [p=0.2] Meninas para meninos é {c}cinco terços, maior que um, [p=0.2] porque há mais meninas. [p=0.3] {d}O que vem primeiro na frase vai em cima."),
    dict(id="s08", block="ordem", text="E dá para comparar a parte com o todo. [p=0.2] A cada três meninos e cinco meninas, {a}são oito alunos. [p=0.2] Meninos para o total da turma: {b}três oitavos. [p=0.3] São {c}razões diferentes. [p=0.2] Leia com atenção o que o problema compara."),
    # mesma unidade
    dict(id="s09", block="unidade", text="Voltando às fitas. [p=0.2] Antes de dividir, {a}as duas medidas precisam estar na mesma unidade. [p=0.3] Na escada do metro, de metro para centímetro {b}são dois degraus: vezes cem. [p=0.2] {c}Dois metros são duzentos centímetros."),
    dict(id="s10", block="unidade", text="A razão é {a}cinquenta duzentos avos. [p=0.3] O MDC de cinquenta e duzentos é cinquenta. [p=0.2] {b}Cinquenta dividido por cinquenta dá um. [p=0.2] {c}Duzentos dividido por cinquenta dá quatro. [p=0.3] {d}Um quarto: a fita menor é a quarta parte da maior. [p=0.3] Confira: {e}quatro fitas de cinquenta centímetros, uma atrás da outra, [p=0.2] dão duzentos centímetros, exatamente dois metros."),
    dict(id="s11", block="unidade", text="Repare que o resultado {a}não tem unidade. [p=0.2] Centímetro dividido por centímetro some. [p=0.3] Um quarto vale {b}em qualquer unidade: [p=0.2] é só uma comparação."),
    # erro
    dict(id="s12", block="erro", text="Por isso, o erro mais comum é {a}dividir medidas em unidades diferentes. [p=0.3] {b}Cinquenta dividido por dois deu vinte e cinco [p=0.2] porque misturou centímetro com metro. [p=0.3] Um teste rápido: {c}a menor dividida pela maior precisa dar menos que um."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho prometido: {a}corte os zeros do final, em cima e embaixo, na mesma quantidade. [p=0.3] {b}Cinquenta duzentos avos vira cinco vinte avos. [p=0.2] Cinco vinte avos, dividindo por cinco, {c}um quarto."),
    dict(id="s14", block="atalho", text="Funciona porque {a}cortar um zero é dividir por dez, [p=0.2] e você fez isso {b}em cima e embaixo. [p=0.3] Só vale quando {c}o de cima e o de baixo terminam em zero. [p=0.2] Em {d}quarenta e cinco centésimos, só o de baixo termina em zero: [p=0.2] não corte nada."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma tábua mede {a}um vírgula dois metro. [p=0.2] Outra mede {b}oitenta centímetros. [p=0.3] {c}Qual é a razão entre a menor e a maior?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Primeiro, a mesma unidade. [p=0.2] {a}Um vírgula dois metro, vezes cem: cento e vinte centímetros. [p=0.3] A menor vai em cima: {b}oitenta cento e vinte avos. [p=0.3] {c}Corte um zero de cada: oito doze avos. [p=0.2] {d}Divida por quatro: dois terços."),
    dict(id="s18", block="resposta", text="A razão é {a}dois para três. [p=0.2] E ela é {b}menor que um, como devia: [p=0.2] a primeira tábua é a menor. [p=0.3] Quer dizer: {c}a cada dois pedaços de tamanho igual na tábua menor, [p=0.2] a maior tem três."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}razão é uma divisão escrita como fração, [p=0.2] {b}na ordem da frase [p=0.2] e {c}com as medidas na mesma unidade."),
    dict(id="s20", block="fim", text="Na próxima aula, você vê o que acontece quando {a}duas razões são iguais, [p=0.2] como {b}dois terços e seis nonos. [p=0.3] Isso é uma {c}proporção, e você vai descobrir o número que falta nela. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
