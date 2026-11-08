# Estudativo · MAT-FUN-015 — Praticando: função afim (Matemática · Funções · Função afim · prática).
# Habilidade: montar a lei de uma situação, ler os coeficientes e comparar duas retas no gráfico.
# Pré-requisitos: MAT-FUN-009, MAT-FUN-010, MAT-FUN-011, MAT-FUN-012, MAT-FUN-013, MAT-FUN-014. Próxima: MAT-FUN-016.
# Questões inéditas, criadas para esta aula. Valores da caixa d'água, das locadoras e da pipoca inventados.
# Taxa de variação narrada "delta ípsilon dividido por delta xis" e bê trocando o ponto na fórmula, como na MAT-FUN-010 e 012.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á".
# Visual: situação 1, reta descendo de (0, 500) a (25, 0); situação 2, reta por (2, 7) e (5, 16); situação 3, retas A e B cruzando em (80, 140).

TITULO = "Praticando: função afim"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações com tudo da função afim, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar: {a}a lei, efe de xis igual a á xis mais bê, [p=0.2] {b}o valor inicial e a taxa de variação, delta ípsilon dividido por delta xis, [p=0.2] {c}o zero da função, [p=0.2] {d}a lei a partir de dois pontos, [p=0.2] {e}a reta que passa pela origem [p=0.2] e {f}o ponto de equilíbrio. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: lei, coeficientes, zero e sinal
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma caixa d'água tem {b}quinhentos litros. [p=0.2] Com a torneira aberta, ela perde {c}vinte litros por hora. [p=0.3] {d}Escreva a lei do volume. [p=0.2] A reta sobe ou desce? [p=0.2] E em quantas horas a caixa esvazia?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] O valor inicial é o que tem no começo: {a}quinhentos. [p=0.2] A cada hora, o volume cai vinte: {b}a taxa é menos vinte. [p=0.3] Lei: {c}efe de xis igual a quinhentos menos vinte xis, com xis em horas. [p=0.2] Taxa negativa: {d}a reta desce."),
    dict(id="s06", block="resposta1", text="Caixa vazia é volume zero: {a}o zero da função. [p=0.2] Quinhentos menos vinte xis igual a zero. [p=0.2] {b}Vinte xis igual a quinhentos. [p=0.2] {c}Xis igual a vinte e cinco horas. [p=0.3] Antes das vinte e cinco horas, {d}a função é positiva: ainda tem água."),
    # situação 2: lei por dois pontos e proporcionalidade
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma reta passa por {b}xis dois, ípsilon sete, [p=0.2] e por {c}xis cinco, ípsilon dezesseis. [p=0.3] {d}Qual é a lei? [p=0.2] Quanto vale efe de dez? [p=0.2] E as grandezas são proporcionais?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] A taxa é delta ípsilon dividido por delta xis. [p=0.2] {a}Delta ípsilon: dezesseis menos sete dá nove. [p=0.2] {b}Delta xis: cinco menos dois dá três. [p=0.2] {c}Nove dividido por três: á vale três."),
    dict(id="s10", block="resposta2", text="Para o bê, troque um dos pontos na fórmula. [p=0.2] Com xis dois e ípsilon sete: {a}três vezes dois, mais bê, igual a sete. [p=0.2] Seis mais bê igual a sete: {b}bê vale um. [p=0.3] Lei: {c}efe de xis igual a três xis mais um. [p=0.2] Efe de dez: {d}trinta mais um dá trinta e um."),
    dict(id="s11", block="resposta2", text="E não é proporcional: {a}o bê vale um, [p=0.2] então a reta {b}não passa pela origem."),
    # atalho
    dict(id="s12", block="atalho", text="Aqui cabe um atalho para o bê: {a}ande para trás até o xis zero. [p=0.2] Do xis dois até o zero são {b}dois passos, [p=0.2] e cada passo para trás {c}tira três. [p=0.2] Sete menos seis: {d}bê igual a um."),
    dict(id="s13", block="atalho", text="Funciona porque o bê é o valor da função {a}no xis zero, [p=0.2] e a taxa diz quanto a função muda a cada passo. [p=0.3] Não compensa quando {b}os pontos estão longe do zero, como em xis cinquenta. [p=0.2] Aí, {c}troque o ponto na fórmula, como na resposta."),
    # situação 3: comparar duas retas
    dict(id="s14", block="questao3", text="{a}Situação três. [p=0.2] No gráfico, os preços de duas locadoras de carro. [p=0.2] {b}Na locadora A, são cem reais, mais cinquenta centavos por quilômetro. [p=0.2] {c}Na locadora B, sessenta reais, mais um real por quilômetro. [p=0.3] {d}Para uma viagem de cento e vinte quilômetros, qual compensa?"),
    dict(id="s15", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta3", text="Vamos lá. [p=0.2] Primeiro, o cruzamento: {a}cem mais zero vírgula cinco xis, igual a sessenta mais xis. [p=0.2] Tire zero vírgula cinco xis e sessenta dos dois lados: {b}quarenta igual a zero vírgula cinco xis. [p=0.2] Dobrando, {c}xis igual a oitenta. [p=0.3] As retas se cruzam em {d}xis oitenta, ípsilon cento e quarenta."),
    dict(id="s17", block="resposta3", text="Antes de oitenta quilômetros, a reta de baixo é a de B. [p=0.2] Depois, {a}é a de A. [p=0.2] Cento e vinte vem depois: {b}compensa a A. [p=0.3] Conferindo: {c}na locadora A, cem mais sessenta dá cento e sessenta reais. [p=0.2] {d}Na B, sessenta mais cento e vinte dá cento e oitenta. [p=0.3] Quem olhou só a parte fixa, menor em B, {e}pagou vinte reais a mais."),
    # situação 4: custo, receita, lucro
    dict(id="s18", block="questao4", text="{a}Última situação. [p=0.2] Um carrinho de pipoca tem {b}custo fixo de seiscentos reais por mês. [p=0.2] Cada saquinho custa {c}dois reais para fazer, e é vendido por {d}cinco. [p=0.3] {e}Qual é o ponto de equilíbrio? [p=0.2] E com cento e cinquenta saquinhos vendidos, o mês dá lucro ou prejuízo?"),
    dict(id="s19", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta4", text="Vamos lá. [p=0.2] Cada saquinho deixa {a}cinco menos dois dá três reais. [p=0.2] Pelo atalho do equilíbrio, {b}seiscentos dividido por três dá duzentos saquinhos. [p=0.3] O lucro é {c}éle de xis igual a três xis menos seiscentos."),
    dict(id="s21", block="resposta4", text="Com cento e cinquenta: {a}três vezes cento e cinquenta dá quatrocentos e cinquenta. [p=0.2] Menos seiscentos, {b}menos cento e cinquenta reais. [p=0.3] {c}Prejuízo. [p=0.2] Faz sentido: cento e cinquenta {d}ainda não chegou no equilíbrio de duzentos."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}o bê é onde a reta começa, [p=0.2] {b}o á é quanto ela sobe ou desce a cada passo, [p=0.2] e {c}no gráfico, a reta de cima vale mais."),
    dict(id="s23", block="fim", text="Na próxima aula, o xis aparece {a}ao quadrado, e o gráfico deixa de ser reta: [p=0.2] vira {b}a parábola. [p=0.3] Você vai ver como dois números da lei dizem {c}para onde ela abre e onde corta o eixo ípsilon. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
