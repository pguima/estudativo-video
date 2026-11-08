# Estudativo · MAT-RAZ-011 — Ler uma fórmula como proporcionalidade (Matemática · Razão e Proporção).
# Habilidade: dizer o que acontece com R em R = k · L/A quando L dobra e A cai pela metade.
# Pré-requisitos: MAT-EQU-011 (isolar uma letra), MAT-FRA-011 (dividir frações), MAT-RAZ-010 (proporcional ao quadrado). Próxima: MAT-RAZ-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras apresentadas uma vez e depois chamadas pelo nome (como em MAT-EQU-011). Física da resistência é só contexto: FIS-ELE-010.
# d = v · t: 2 h → 4 h dobra a distância. t = d/v: 120 km a 40 km/h = 3 h; a 80 km/h = 1,5 h.
# R = k · L/A: L × 2 → R × 2; A × 1/2 → R ÷ 1/2 = R × 2; total × 4. Erro: 2 · 1/2 = 1 ("não muda").
# Atalho: fatores no lugar das letras: 1 · 2 ÷ (1/2) = 4. Exemplo: y = k · x²/z, x × 2 e z × 2 → 4/2 = 2.
# Questão: y = k · x²/z, x × 3 e z × 3 → 9/3 = 3 (triplica).

TITULO = "Ler uma fórmula como proporcionalidade"

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
    dict(id="s01", block="gancho", text="{a}Um fio elétrico ganha o dobro do comprimento, [p=0.2] e o corte dele fica com a metade da área. [p=0.3] A dificuldade para a corrente passar {b}fica igual? [p=0.2] {c}Ela fica quatro vezes maior. [p=0.3] E dá para saber {d}sem nenhum número do fio."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê uma fórmula e diz o que acontece com o resultado quando as letras mudam, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}três coisas: [p=0.2] {b}distância igual a velocidade vezes tempo, [p=0.2] {c}dividir por um meio é o mesmo que multiplicar por dois, [p=0.2] e {d}dobrar o lado de um quadrado quadruplica a área. [p=0.3] Se faltar alguma, procure no canal."),
    # letra que multiplica
    dict(id="s04", block="cima", text="Comece pela fórmula que você conhece: {a}distância igual a velocidade vezes tempo. [p=0.3] Deixe a velocidade fixa e {b}dobre o tempo. [p=0.2] Duas horas viram quatro, [p=0.2] e {c}a distância dobra. [p=0.3] A letra que multiplica é {d}diretamente proporcional ao resultado."),
    # letra que divide
    dict(id="s05", block="baixo", text="Agora isole o tempo: {a}tempo igual a distância dividida pela velocidade. [p=0.3] {b}Cento e vinte quilômetros a quarenta quilômetros por hora: três horas. [p=0.2] {c}A oitenta quilômetros por hora: uma hora e meia. [p=0.3] Dobrou a velocidade, {d}o tempo caiu pela metade."),
    dict(id="s06", block="baixo", text="A letra que fica embaixo da fração é {a}inversamente proporcional ao resultado. [p=0.3] Daí sai a regra da aula: [p=0.2] {b}em cima, direto. [p=0.2] {c}Embaixo, inverso. [p=0.3] E se a letra estiver ao quadrado, {d}o fator dela vai ao quadrado, como o lado na área."),
    # a fórmula do fio
    dict(id="s07", block="fio", text="Vamos ao fio. [p=0.2] A fórmula é {a}erre igual a cá vezes éle dividido por a maiúsculo. [p=0.3] {b}Erre é a resistência: o quanto o fio dificulta a passagem da corrente. [p=0.2] {c}Éle é o comprimento do fio. [p=0.2] {d}A maiúsculo é a área do corte, a bolinha que aparece quando você corta o fio. [p=0.2] E {e}cá é um número fixo, que depende do material."),
    dict(id="s08", block="fio", text="Daqui em diante, eu chamo cada letra pelo nome. [p=0.2] A física disso fica para outra aula. [p=0.3] Aqui, só leia: [p=0.2] {a}o comprimento está em cima: direto. [p=0.2] {b}A área está embaixo: inverso."),
    dict(id="s09", block="fio", text="Agora, {a}uma mudança de cada vez. [p=0.3] {b}O comprimento dobrou: a resistência fica vezes dois. [p=0.3] {c}A área caiu pela metade: a resistência fica dividida por um meio. [p=0.2] E dividir por um meio é {d}multiplicar por dois."),
    dict(id="s10", block="fio", text="Juntando: {a}vezes dois, e vezes dois de novo. [p=0.2] {b}A resistência fica quatro vezes maior. [p=0.3] Faz sentido: {c}fio mais comprido e mais fino, mais difícil para a corrente passar."),
    # erro comum
    dict(id="s11", block="erro", text="O erro comum é {a}tratar a letra de baixo como se estivesse em cima. [p=0.3] A pessoa pensa: [p=0.2] {b}o comprimento dobrou, vezes dois. [p=0.2] {c}A área caiu pela metade, vezes um meio. [p=0.2] {d}Dois vezes um meio dá um, então a resistência não muda."),
    dict(id="s12", block="erro", text="Mas a área {a}divide. [p=0.2] Diminuir o que está embaixo {b}aumenta o resultado. [p=0.3] Antes de juntar os fatores, {c}veja de que lado da fração cada letra está."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: [p=0.2] {a}troque cada letra pelo fator da mudança. [p=0.3] Letra que não muda {b}vale um, e o cá também. [p=0.3] {c}Um, vezes dois, dividido por um meio. [p=0.2] {d}Dá quatro. [p=0.2] Uma linha, e pronto."),
    dict(id="s14", block="atalho", text="Funciona porque o cá não muda, então {a}só os fatores decidem quanto o resultado cresce. [p=0.3] Com quadrado também: [p=0.2] numa fórmula com {b}xis ao quadrado dividido por zê, [p=0.2] se xis e zê dobram, fica {c}dois ao quadrado dividido por dois. [p=0.2] {d}Quatro dividido por dois: o resultado dobra."),
    dict(id="s15", block="atalho", text="{a}Não vale quando a fórmula tem uma parte somada. [p=0.3] {b}No táxi com bandeirada, dobrar os quilômetros não dobra o preço, [p=0.2] porque a bandeirada não muda. [p=0.2] Aí, {c}faça a conta com números."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Numa fórmula, {a}ípsilon é igual a cá vezes xis ao quadrado, dividido por zê. [p=0.3] {b}Xis fica três vezes maior, [p=0.1] e {c}zê também fica três vezes maior. [p=0.3] {d}O que acontece com ípsilon?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Xis está em cima e {a}ao quadrado: o fator é três ao quadrado, nove. [p=0.2] Zê está embaixo: {b}divide por três. [p=0.3] {c}Nove dividido por três dá três. [p=0.2] {d}Ípsilon fica três vezes maior."),
    dict(id="s19", block="resposta", text="Repare: {a}xis e zê triplicaram, e mesmo assim ípsilon mudou. [p=0.3] Quem responde que nada muda {b}esqueceu o quadrado do xis."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}em cima, direto. [p=0.2] {b}Embaixo, inverso. [p=0.2] {c}Ao quadrado, o fator vai ao quadrado. [p=0.2] E {d}multiplique os efeitos."),
    dict(id="s21", block="fim", text="Na próxima aula, você {a}pratica a trilha toda: [p=0.2] {b}descobre o tipo de relação e resolve regra de três simples e composta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
