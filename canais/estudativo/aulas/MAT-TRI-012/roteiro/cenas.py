# Estudativo · MAT-TRI-012 — Fenômenos periódicos: marés e ondas (Matemática · Trigonometria · Ciclo e funções trigonométricas).
# Habilidade: ler em h(t) = 5 + 2 cos(πt/6) a altura máxima (7), a mínima (3) e o período (12 h).
# Pré-requisitos: MAT-TRI-014 (máx = a + b, mín = a − b, período: o de dentro chega a 2π). Usa também MAT-EQU-007 (mesmo nos dois lados),
#   MAT-FUN-003 (f(x)), MAT-TRI-008 (cos 0 = 1, cos π = −1). Próxima: MAT-TRI-013.
# Questão inédita, criada para esta aula. Porto e roda-gigante imaginados para a aula (não são dados reais).
# h(t): t em horas desde a meia-noite, h em metros · máx 5 + 2 = 7 · mín 5 − 2 = 3 · nível médio 5.
# Período: πt/6 = 2π → t/6 = 2 → t = 12 h · t = 0: cos 0 = 1 → 7 m (meia-noite) · t = 6: πt/6 = π, cos π = −1 → 3 m · t = 12: 7 m (meio-dia).
# Erro: período = 6 (o número da fórmula); em t = 6 o de dentro só chega a π (meia volta, da alta para a baixa).
# Atalho: dentro = πt/n → período 2n (πt/6 → 12) · não vale com número multiplicando o π: 2πt/5 = 2π → t = 5.
# Questão: roda-gigante h(t) = 12 + 10 cos(πt/3), t em minutos · máx 22 m · mín 2 m · período 6 min · confere: 22 − 2 = 20 m de diâmetro;
#   mínimo em t = 3 (πt/3 = π).
# Visual (E.plano, E.curva, E.ponto):
#   s01: porto com a água subindo e descendo; régua de maré.
#   s04: h(t) = 5 + 2 cos(πt/6) com etiquetas "t: horas desde a meia-noite" e "h: altura em metros".
#   s05: máx 7, mín 3, linha do meio 5.
#   s06: πt/6 = 2π → t/6 = 2 → t = 12, linha a linha.
#   s07-s08: plano com t de 0 a 24 e h de 0 a 8; onda entre 3 e 7, pontos (0, 7), (6, 3), (12, 7), (18, 3), (24, 7); período 12 destacado.
#   s09: "6 h" riscado em vermelho; meia volta marcada entre t = 0 e t = 6.
#   s10-s11: cartão do atalho "πt/n → período 2n"; 2πt/5 → 5 como exceção.
#   s12-s15: roda-gigante com a cadeira; gráfico de 12 + 10 cos(πt/3) entre 2 e 22, período 6.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; t narrado "tê", h narrado "agá".

TITULO = "Fenômenos periódicos: marés e ondas"

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
    dict(id="s01", block="gancho", text="{a}A maré sobe e desce todos os dias, sempre no mesmo ritmo. [p=0.3] Quem trabalha num porto precisa saber {b}quando a água fica alta [p=0.2] e {c}quando fica baixa. [p=0.3] Uma fórmula com cosseno responde as duas perguntas."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê numa situação do dia a dia o máximo, o mínimo e o período, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa da aula anterior: [p=0.2] {a}máximo é á mais bê, [p=0.2] {b}mínimo é á menos bê, [p=0.2] e {c}a onda fecha uma volta quando o que está dentro do parêntese chega a dois pi. [p=0.3] Se faltar, procure no canal."),
    # a fórmula
    dict(id="s04", block="formula", text="Num porto imaginado para esta aula, a altura da água segue {a}agá de tê igual a cinco, mais duas vezes o cosseno de pi tê dividido por seis. [p=0.3] {b}Tê é o tempo, em horas, contado a partir da meia-noite. [p=0.2] {c}Agá de tê é a altura da água, em metros, nessa hora."),
    # máximo e mínimo
    dict(id="s05", block="altura", text="O cosseno vai de menos um a um. [p=0.2] {a}Maré alta: cinco mais dois dá sete metros. [p=0.2] {b}Maré baixa: cinco menos dois dá três metros. [p=0.3] {c}O cinco é o nível médio da água, o meio da onda."),
    # período
    dict(id="s06", block="periodo", text="E de quantas em quantas horas a maré se repete? [p=0.2] Quando {a}o de dentro do parêntese chega a dois pi. [p=0.3] {b}Pi tê dividido por seis igual a dois pi. [p=0.2] {c}Divida cada lado por pi: tê dividido por seis igual a dois. [p=0.2] {d}Multiplique por seis: tê igual a doze. [p=0.3] {e}O período é de doze horas."),
    # quando
    dict(id="s07", block="quando", text="E a que horas a maré é alta? [p=0.2] Quando {a}o cosseno vale um, o que acontece com o ângulo zero. [p=0.2] {b}Em tê igual a zero, à meia-noite: sete metros."),
    dict(id="s08", block="quando", text="Seis horas depois, {a}o de dentro vale pi, [p=0.2] e {b}o cosseno de pi é menos um. [p=0.2] {c}Maré baixa de três metros às seis da manhã. [p=0.3] {d}Ao meio-dia, maré alta de novo. [p=0.2] No gráfico, {e}a onda oscila entre três e sete, com um pico a cada doze horas."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é {a}dizer que o período é seis, o número que aparece na fórmula. [p=0.3] Mas em seis horas, {b}o de dentro só chegou a pi: meia volta. [p=0.2] {c}A maré só foi da alta para a baixa. [p=0.2] Para voltar à alta, {d}faltam mais seis horas. [p=0.2] {e}Período de doze."),
    # atalho
    dict(id="s10", block="atalho", text="Agora o atalho. [p=0.2] Quando o de dentro é {a}pi tê dividido por um número, [p=0.2] {b}o período é o dobro desse número. [p=0.3] {c}Pi tê dividido por seis: período doze. [p=0.2] {d}Pi tê dividido por doze: período vinte e quatro."),
    dict(id="s11", block="atalho", text="Funciona porque o pi se corta de cada lado, [p=0.2] e sobra {a}tê dividido pelo número igual a dois. [p=0.3] {b}Não serve quando vem um número multiplicando o pi em cima, [p=0.2] como em {c}dois pi tê dividido por cinco. [p=0.2] Aí, {d}iguale a dois pi e resolva: [p=0.2] ali, o período {e}dá cinco."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] Numa roda-gigante, a altura de uma cadeira, em metros, é {a}agá de tê igual a doze, mais dez vezes o cosseno de pi tê dividido por três, [p=0.2] com {b}tê em minutos. [p=0.3] {c}Qual é a altura máxima? [p=0.2] {d}E a mínima? [p=0.2] {e}Quanto tempo a roda leva para dar uma volta?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Vamos lá. [p=0.2] {a}Máxima: doze mais dez dá vinte e dois metros. [p=0.2] {b}Mínima: doze menos dez dá dois metros. [p=0.3] Pelo atalho, pi tê dividido por três: [p=0.2] {c}o período é o dobro de três: dá seis minutos. [p=0.2] {d}Uma volta a cada seis minutos."),
    dict(id="s15", block="resposta", text="Confira o sentido: [p=0.2] {a}vinte e dois menos dois dá vinte metros, a altura da roda de ponta a ponta. [p=0.3] E {b}em tê igual a três, o de dentro vale pi: [p=0.2] {c}é a cadeira no ponto mais baixo, na metade da volta."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: {a}o número somado é o nível médio, [p=0.2] {b}máximo e mínimo saem de á mais bê e á menos bê, [p=0.2] e {c}o período é quando o de dentro chega a dois pi."),
    dict(id="s17", block="fim", text="Na próxima aula, você {a}pratica a parte do ciclo inteira: [p=0.2] {b}radianos, sinais, a relação fundamental e as ondas, [p=0.2] em questões no estilo da prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
