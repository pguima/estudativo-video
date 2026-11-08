# Estudativo · MAT-RAZ-021 — Descobrir a escala e usar escala gráfica (Matemática · Razão e Proporção).
# Habilidade: achar a escala de um mapa em que 4 cm representam 10 km e medir com a régua numa escala gráfica.
# Pré-requisitos: MAT-RAZ-020 (o que é escala). Usa também MAT-FRA-003 (simplificar) e MAT-MED-001 (escada do metro). Próxima: MAT-RAZ-022.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Descobrir a escala e usar escala gráfica"

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
    dict(id="s01", block="gancho", text="Você tira uma cópia de um mapa, {a}reduzida pela metade. [p=0.3] No canto, a escala escrita continua dizendo {b}um para cinquenta mil. [p=0.2] Só que agora {c}ela está errada. [p=0.3] O mapa encolheu pela metade, e a escala de verdade passou a ser {d}um para cem mil."),
    dict(id="s02", block="gancho", text="Mas existe um jeito de escala que {a}continua certo em qualquer cópia. [p=0.3] {b}Até o fim desta aula, você vai usar esse jeito [p=0.2] e descobrir a escala de um mapa que não tem nenhuma escrita."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}saber que escala é desenho sobre real, na mesma unidade, [p=0.2] e {c}subir e descer a escada do metro. [p=0.3] Se faltar alguma, procure no canal."),
    # achar a escala
    dict(id="s04", block="achar", text="Comece pelo mapa sem escala. [p=0.2] Você sabe só que {a}quatro centímetros no papel representam {b}dez quilômetros de verdade. [p=0.3] Qual é a escala?"),
    dict(id="s05", block="achar", text="Escala é desenho sobre real, {a}na mesma unidade. [p=0.2] Então passe dez quilômetros para centímetros. [p=0.2] {b}Vezes mil dá dez mil metros. [p=0.2] {c}Vezes cem dá um milhão de centímetros."),
    dict(id="s06", block="achar", text="A razão fica {a}quatro sobre um milhão. [p=0.3] Escala se escreve com {b}um em cima. [p=0.2] Então simplifique: divida em cima e embaixo por quatro. [p=0.2] {c}Um sobre duzentos e cinquenta mil. [p=0.3] A escala é {d}um para duzentos e cinquenta mil. [p=0.3] Conferindo: {e}duzentos e cinquenta mil vezes quatro dá um milhão. [p=0.2] Bateu."),
    # escala gráfica
    dict(id="s07", block="grafica", text="Agora o jeito que resiste à cópia: a {a}escala gráfica. [p=0.2] É uma {b}barrinha no canto do mapa, dividida em trechos, [p=0.2] com a distância real escrita embaixo: {c}zero, cinco quilômetros, dez quilômetros."),
    dict(id="s08", block="grafica", text="Para usar, {a}meça um trecho da barra com a régua. [p=0.2] Digamos que de zero a cinco quilômetros dê {b}dois centímetros. [p=0.3] Então, nesse mapa, {c}cada dois centímetros valem cinco quilômetros."),
    dict(id="s09", block="grafica", text="Duas cidades estão a {a}seis centímetros. [p=0.2] Seis centímetros são {b}três trechos de dois. [p=0.2] {c}Três vezes cinco dá quinze quilômetros."),
    dict(id="s10", block="grafica", text="E se a distância não for um número certo de trechos? [p=0.2] {a}Marque as duas cidades na borda de uma tira de papel. [p=0.2] Depois, {b}encoste a tira na barra [p=0.1] e leia a distância direto nos números dela."),
    dict(id="s11", block="grafica", text="E se você precisar da escala numérica? [p=0.2] {a}Dois centímetros para cinco quilômetros. [p=0.2] Cinco quilômetros são {b}quinhentos mil centímetros. [p=0.2] Dividindo por dois: {c}um para duzentos e cinquenta mil, de novo."),
    dict(id="s12", block="grafica", text="Por que ela resiste à cópia? [p=0.2] Quando o mapa encolhe, {a}a barra encolhe junto. [p=0.3] A distância entre as cidades e o trecho da barra diminuem na mesma proporção, [p=0.2] e a conta continua dando {b}quinze quilômetros."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: {a}montar a razão com unidades diferentes. [p=0.2] Quatro centímetros para dez quilômetros vira {b}quatro sobre dez, [p=0.2] e a escala sai {c}um para dois vírgula cinco."),
    dict(id="s14", block="erro", text="Isso diria que {a}o mapa tem quase metade do tamanho da região de verdade! [p=0.3] Uma escala de mapa tem {b}um número enorme embaixo. [p=0.2] Se saiu pequeno, faltou {c}passar tudo para centímetro."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}divida o real pelo desenho, já em centímetros. [p=0.3] {b}Um milhão dividido por quatro dá duzentos e cinquenta mil. [p=0.2] Esse é o número de baixo da escala, {c}direto."),
    dict(id="s16", block="atalho", text="Funciona porque é exatamente {a}a simplificação que deixa o um em cima. [p=0.2] Dividir o de baixo pelo de cima é o que faz o de cima virar um. [p=0.3] Não compensa quando a pergunta é {b}só uma distância e o mapa tem a barra: [p=0.2] aí, {c}conte os trechos, sem achar escala nenhuma."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Na escala gráfica de um mapa, {a}três centímetros representam seis quilômetros. [p=0.3] {b}Qual é a escala numérica? [p=0.2] E {c}qual a distância real entre dois pontos a nove centímetros no mapa?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Seis quilômetros são {a}seiscentos mil centímetros. [p=0.2] {b}Seiscentos mil dividido por três dá duzentos mil. [p=0.2] Escala: {c}um para duzentos mil."),
    dict(id="s20", block="resposta", text="Nove centímetros são {a}três trechos de três. [p=0.2] {b}Três vezes seis dá dezoito quilômetros. [p=0.3] Pela escala dá o mesmo: [p=0.2] {c}nove vezes duzentos mil dá um milhão e oitocentos mil centímetros, [p=0.2] {d}dezoito quilômetros."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}para achar a escala, passe para centímetro e divida o real pelo desenho. [p=0.2] {b}Na escala gráfica, meça a barra e conte os trechos."),
    dict(id="s22", block="fim", text="Na próxima aula, uma armadilha: {a}área e volume numa planta ou maquete. [p=0.2] Ali, {b}aplicar a escala direto dá errado. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
