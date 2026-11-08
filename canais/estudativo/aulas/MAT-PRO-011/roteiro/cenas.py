# Estudativo · MAT-PRO-011 — Soma infinita de uma PG (Matemática · Progressões · Progressão geométrica).
# Habilidade: mostrar que 1 + 1/2 + 1/4 + … = 2, calcular a distância total de uma bola que quica e reencontrar 0,444… = 4/9.
# Pré-requisitos: MAT-PRO-010 (soma da PG finita e atalho "termo seguinte ao último"), MAT-CON-005 (fração geratriz, 0,444… = 4/9). Próxima: MAT-PRO-012.
# Questão inédita, criada para esta aula. Termos narrados como "o primeiro termo" (sem "á um"); q narrado "quê".
# Contas: parede a 2 m, passos 1, 1/2, 1/4… · falta 1, 1/2, 1/4… · (1/2)¹⁰ = 1/1.024 ≈ 0,001.
# Fórmula: Sₙ = a₁(qⁿ − 1)/(q − 1); qⁿ → 0 quando −1 < q < 1 → S = −a₁/(q − 1) = a₁/(1 − q).
# Parede: 1/(1 − 1/2) = 1/(1/2) = 2.
# Bola de 10 m, sobe 1/2: subidas 5 + 2,5 + 1,25 + … = 5/(1/2) = 10; descidas depois da 1ª = 10 · total 10 + 10 + 10 = 30.
# Erro: 10/(1 − 1/2) = 20 (cada altura contada uma vez só).
# Dízima: 0,444… = 4/10 + 4/100 + … · (4/10)/(1 − 1/10) = (4/10)/(9/10) = 4/9.
# Atalho da bola: H · (1 + r)/(1 − r) = 10 · (3/2)/(1/2) = 30. Motivo: descidas H/(1 − r), subidas H·r/(1 − r).
# Questão: 12 m, sobe 1/3 · subidas 4/(2/3) = 6 · 12 + 6 + 6 = 24 · atalho 12 · 4/3 = 16; 16 ÷ 2/3 = 24.
# Visual:
#   s01-s04: pessoa andando até uma parede a 2 m; segmentos de 1, 1/2, 1/4… preenchendo a barra; o que falta encolhendo.
#   s05-s07: E.colunas encolhendo (razão 1/2) ao lado de colunas crescendo (razão 2) riscadas; S = a₁/(1 − q) com legendas; faixa −1 < q < 1.
#   s09-s12: bola quicando (E.curva): queda de 10, subidas e descidas de 5, 2,5, 1,25…; subidas e descidas com cores diferentes; 20 em vermelho.
#   s13-s14: 0,444… decomposto em 0,4 + 0,04 + 0,004…; (4/10)/(9/10) = 4/9.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Soma infinita de uma PG"

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
    dict(id="s01", block="gancho", text="{a}Você está a dois metros de uma parede. [p=0.2] {b}Anda um metro. [p=0.2] {c}Depois, meio metro. [p=0.2] {d}Depois, um quarto de metro, sempre a metade do passo anterior. [p=0.3] São {e}infinitos passos, [p=0.2] e o total nunca passa de {f}dois metros."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você soma uma pê gê infinita numa conta só, [p=0.2] calcula {b}quanto anda uma bola que quica [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a soma da pê gê, ésse índice ene igual a á índice um, vezes, abre parênteses, quê elevado a ene, menos um, fecha parênteses, dividido por, abre parênteses, quê menos um, fecha parênteses; [p=0.2] e {c}a fração de uma dízima, como zero vírgula quatro quatro quatro, sem fim, que é quatro nonos. [p=0.3] Se faltar alguma, procure no canal."),
    # por que não estoura
    dict(id="s04", block="parede", text="Por que a soma não estoura? [p=0.2] Olhe {a}quanto falta até a parede. [p=0.2] Depois do primeiro passo, {b}falta um metro. [p=0.2] Depois do segundo, {c}falta meio metro. [p=0.2] {d}Cada passo cobre a metade do que falta. [p=0.3] O que falta {e}encolhe até quase zero, mas o total nunca passa dos dois metros."),
    dict(id="s05", block="parede", text="Isso acontece quando {a}a razão fica entre menos um e um. [p=0.2] Aqui, a razão é {b}um meio, e os termos encolhem. [p=0.3] Com razão {c}dois, os termos crescem, e a soma infinita não tem fim."),
    # fórmula
    dict(id="s06", block="formula", text="Olhe a fórmula da soma por dentro. [p=0.2] Ela tem {a}quê elevado a ene. [p=0.2] Com razão um meio, {b}um meio elevado a dez já é um dividido por mil e vinte e quatro. [p=0.2] Quase {c}zero. [p=0.3] Com infinitos termos, essa potência {d}some."),
    dict(id="s07", block="formula", text="Sem a potência, sobra {a}menos á índice um, dividido por, abre parênteses, quê menos um, fecha parênteses. [p=0.2] Troque o sinal em cima e embaixo: a divisão não muda, como menos seis dividido por menos dois dá o mesmo que seis dividido por dois. [p=0.3] {b}A soma infinita é á índice um dividido por, abre parênteses, um menos quê, fecha parênteses. [p=0.3] {c}Quê é a razão, [p=0.2] e {d}ela precisa estar entre menos um e um."),
    dict(id="s08", block="formula", text="Na parede: {a}primeiro termo um, razão um meio. [p=0.2] {b}Um menos um meio dá um meio. [p=0.2] {c}Um dividido por um meio dá dois. [p=0.3] {d}Os dois metros da parede."),
    # bola
    dict(id="s09", block="bola", text="Agora, a bola. [p=0.2] Ela cai de {a}dez metros. [p=0.2] Em cada quique, {b}sobe a metade da altura de que caiu. [p=0.3] {c}Que distância ela percorre até parar?"),
    dict(id="s10", block="bola", text="{a}Primeiro, a queda de dez metros. [p=0.2] Depois, ela {b}sobe cinco e desce cinco. [p=0.2] {c}Sobe dois e meio e desce dois e meio. [p=0.3] Cada altura depois do começo {d}conta duas vezes: na subida e na descida."),
    dict(id="s11", block="bola", text="As subidas são {a}cinco, mais dois e meio, mais um e um quarto, e assim por diante. [p=0.2] Soma infinita: {b}cinco dividido por um meio dá dez. [p=0.2] As descidas depois da primeira também somam {c}dez. [p=0.3] Total: {d}dez da queda, mais dez, mais dez, dá trinta metros."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}jogar tudo na fórmula de uma vez: [p=0.2] {b}dez dividido por um meio dá vinte. [p=0.3] Essa conta soma {c}cada altura uma vez só, [p=0.2] e esquece que a bola {d}sobe e desce. [p=0.2] Só a primeira queda {e}não tem subida antes."),
    # dízima
    dict(id="s13", block="dizima", text="A mesma fórmula explica as dízimas. [p=0.2] {a}Zero vírgula quatro quatro quatro, sem fim, [p=0.2] é {b}quatro décimos, mais quatro centésimos, mais quatro milésimos, e assim por diante. [p=0.3] Uma pê gê de {c}primeiro termo quatro décimos e razão um décimo."),
    dict(id="s14", block="dizima", text="{a}Um menos um décimo dá nove décimos. [p=0.2] {b}Quatro décimos dividido por nove décimos dá quatro nonos. [p=0.3] {c}O mesmo quatro nonos da fração da dízima. [p=0.2] E agora você vê de onde vem {d}o nove de baixo: do um menos um décimo."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho da bola: [p=0.2] {a}a altura, vezes, abre parênteses, um mais a fração, fecha parênteses, dividido por, abre parênteses, um menos a fração, fecha parênteses. [p=0.3] {b}Dez vezes um e meio dá quinze. [p=0.2] {c}Quinze dividido por um meio dá trinta. [p=0.2] Numa conta só."),
    dict(id="s16", block="atalho", text="Funciona porque {a}as descidas somam a altura dividida por, abre parênteses, um menos a fração, fecha parênteses, [p=0.2] e {b}as subidas são as descidas vezes a fração. [p=0.3] Não compensa se a bola {c}for lançada para cima no começo, [p=0.2] ou se a questão pedir {d}só as subidas. [p=0.2] Aí, monte as somas uma a uma."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma bola cai de {a}doze metros [p=0.2] e, em cada quique, sobe {b}um terço da altura de que caiu. [p=0.3] {c}Que distância ela percorre até parar?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] As subidas começam em {a}quatro metros, com razão um terço. [p=0.2] {b}Um menos um terço dá dois terços. [p=0.2] {c}Quatro dividido por dois terços dá seis. [p=0.3] {d}Doze da queda, mais seis subindo, mais seis descendo, dá vinte e quatro metros."),
    dict(id="s20", block="resposta", text="Pelo atalho: {a}doze vezes quatro terços dá dezesseis. [p=0.2] {b}Dezesseis dividido por dois terços dá vinte e quatro. [p=0.2] Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}com a razão entre menos um e um, [p=0.2] {b}a soma infinita é o primeiro termo dividido por, abre parênteses, um menos a razão, fecha parênteses."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica {a}tudo de pê gê [p=0.2] em problemas de {b}juros, de remédio no sangue e de bola quicando. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
