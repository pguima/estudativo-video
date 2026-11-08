# Estudativo · MAT-POT-011 — Praticando: raízes (Matemática · Potências e Raízes · Radiciação · prática).
# Habilidade: calcular, estimar e simplificar raízes em problemas de medida.
# Pré-requisitos: MAT-POT-007, MAT-POT-016, MAT-POT-008, MAT-POT-009. Próxima: MAT-POT-012.
# Questões inéditas, criadas para esta aula. Área e volume explicados na hora: geometria não está na ficha.
# P1: 1.225 → 245 → 49 → 7 → 1 = 5·5·7·7 → 35 → √12,25 = 3,5; 4 × 3,5 = 14 m.
# P2: 25 < 30 < 36; 5,5² = 30,25 > 30: não cabe (√30 ≈ 5,48). Atalho: comparar quadrados.
# P3: √32 = 4√2; √50 = 5√2; soma 9√2 ≈ 12,6 com 1,4 (real 12,73); erro √82 ≈ 9,06.
# P4: 729 = 3·3·3·3·3·3 → ∛729 = 9; fundo 9² = 81 m² = 729^(2/3); 9³ = 729.

TITULO = "Praticando: raízes"

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
    dict(id="s01", block="gancho", text="{a}Quatro problemas de medida, [p=0.2] criados para esta aula. [p=0.3] Em cada um, {b}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Uma ideia volta sempre. [p=0.2] A {a}área é o tamanho de uma superfície. [p=0.2] No quadrado, {b}área é lado vezes lado, [p=0.2] medida em {c}metros quadrados. [p=0.3] Então {d}o lado é a raiz quadrada da área. [p=0.3] Se alguma conta travar, procure a aula no canal."),
    # problema 1: exata com decimal
    dict(id="s03", block="questao1", text="{a}Problema um. [p=0.2] Uma sala quadrada tem {b}doze vírgula vinte e cinco metros quadrados de piso. [p=0.3] Você vai colocar rodapé {c}nas quatro paredes inteiras, sem descontar porta. [p=0.3] {d}Quantos metros de rodapé são necessários?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] O lado é a {a}raiz de doze vírgula vinte e cinco. [p=0.2] Esqueça a vírgula e fatore {b}mil duzentos e vinte e cinco. [p=0.2] {c}Por cinco dá duzentos e quarenta e cinco. [p=0.2] {d}Por cinco dá quarenta e nove. [p=0.2] {e}Por sete dá sete. [p=0.2] {f}Por sete dá um."),
    dict(id="s06", block="resposta1", text="Uma dupla de cinco e uma dupla de sete: {a}cinco vezes sete dá trinta e cinco. [p=0.2] O número tinha duas casas, então a raiz tem uma: {b}três vírgula cinco metros de lado. [p=0.3] Mas a pergunta é o rodapé: {c}quatro vezes três vírgula cinco dá {d}catorze metros."),
    # problema 2: estimar
    dict(id="s07", block="questao2", text="{a}Problema dois. [p=0.2] Um jardim quadrado tem {b}trinta metros quadrados. [p=0.3] Você quer encostar {c}uma tábua de cinco metros e meio ao longo de um lado do jardim. [p=0.3] {d}A tábua cabe nesse lado, sem sobrar para fora?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] O lado é a {a}raiz de trinta. [p=0.2] {b}Cinco ao quadrado dá vinte e cinco [p=0.2] e {c}seis ao quadrado dá trinta e seis. [p=0.2] Então o lado fica {d}entre cinco e seis metros. [p=0.3] Mas será que chega a cinco e meio?"),
    # atalho
    dict(id="s10", block="atalho", text="Aqui entra o atalho: {a}não calcule a raiz, eleve a medida da tábua ao quadrado. [p=0.3] {b}Cinco vírgula cinco vezes ele mesmo dá trinta vírgula vinte e cinco. [p=0.2] Passou de trinta, então {c}a tábua é maior que o lado. [p=0.2] {d}Não cabe, por pouco."),
    dict(id="s11", block="atalho", text="Funciona porque {a}quanto maior a medida, maior o quadrado dela. [p=0.3] Não compensa quando a pergunta pede {b}o valor do lado: [p=0.2] aí, cerque e confira."),
    # problema 3: simplificar e somar
    dict(id="s12", block="questao3", text="{a}Problema três. [p=0.2] Dois canteiros quadrados têm {b}trinta e dois e {c}cinquenta metros quadrados. [p=0.3] Eles ficam {d}um ao lado do outro, cada um com um lado inteiro na calçada. [p=0.3] {e}Quantos metros de calçada ocupam juntos? [p=0.2] Dê a forma simplificada e um valor aproximado."),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] A medida é {a}raiz de trinta e dois mais raiz de cinquenta. [p=0.3] {b}Trinta e dois é dezesseis vezes dois: {c}quatro raiz de dois. [p=0.2] {d}Cinquenta é vinte e cinco vezes dois: {e}cinco raiz de dois."),
    dict(id="s15", block="resposta3", text="Mesmo número dentro, então some: {a}nove raiz de dois metros. [p=0.3] Use {b}raiz de dois perto de um vírgula quatro. [p=0.2] {c}Nove vezes um vírgula quatro dá doze vírgula seis. [p=0.2] Um pouco mais de {d}doze metros e meio. [p=0.3] Quem soma direto escreve {e}raiz de oitenta e dois, que dá só cerca de nove."),
    # problema 4: cubo e expoente fracionário
    dict(id="s16", block="questao4", text="{a}Último problema, e ele junta tudo. [p=0.2] Um reservatório tem forma de {b}cubo: [p=0.2] comprimento, largura e altura iguais. [p=0.2] Nele cabem {c}setecentos e vinte e nove metros cúbicos: esse é o volume, que é comprimento vezes largura vezes altura. [p=0.3] Você vai forrar {d}só o fundo, [p=0.2] que é {e}um quadrado, com lona. [p=0.3] {f}Quantos metros quadrados de lona são necessários?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] No cubo, o volume é {a}lado vezes lado vezes lado, [p=0.2] então o lado é a raiz cúbica do volume. [p=0.2] Fatorando, {b}o número três aparece seis vezes. [p=0.3] Raiz quadrada pede dois grupos iguais. [p=0.2] {c}Raiz cúbica pede três grupos iguais, então procure trios. [p=0.2] Seis vezes formam dois trios, e cada grupo leva um primo de cada trio: {d}três vezes três dá nove metros de lado."),
    dict(id="s19", block="resposta4", text="O fundo é um quadrado: {a}lado vezes lado. [p=0.2] {b}Nove vezes nove dá oitenta e um metros quadrados de lona. [p=0.3] Repare: você fez a raiz cúbica e depois elevou ao quadrado. [p=0.2] Isso é {c}setecentos e vinte e nove elevado a dois terços: o de baixo é a raiz, o de cima é a potência. [p=0.3] Conferindo o volume: {d}nove vezes nove vezes nove dá setecentos e vinte e nove."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}área de quadrado chama raiz quadrada, [p=0.2] {b}volume de cubo chama raiz cúbica, [p=0.2] e {c}raiz não exata só se soma com o mesmo número dentro."),
    dict(id="s21", block="fim", text="Na próxima aula, o assunto muda: {a}notação científica, [p=0.2] o jeito de escrever número enorme ou muito pequeno usando {b}potência de dez. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
