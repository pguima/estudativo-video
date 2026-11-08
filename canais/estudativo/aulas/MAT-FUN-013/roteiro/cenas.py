# Estudativo · MAT-FUN-013 — Função linear e grandezas proporcionais (Matemática · Funções · Função afim).
# Habilidade: reconhecer y = kx no gráfico como reta que passa pela origem, achar k e explicar por que o táxi com bandeirada não é proporcional.
# Pré-requisitos: MAT-FUN-009 (função afim: lei e gráfico), MAT-RAZ-005 (teste do dobro). Próxima: MAT-FUN-014.
# Questão inédita, criada para esta aula. Feijão a R$ 8 o quilo (MAT-RAZ-004) e táxi P = 5 + 2,5d (MAT-FUN-009).
# FUN-010 a 012 fora da ficha: sem "taxa de variação" nem lei por dois pontos. Pares narrados "xis três, ípsilon vinte e quatro".
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á".
# Visual: plano com a reta do feijão pela origem e a do táxi cortando o eixo y no 5; na questão, retas A (origem, (5, 60)) e B ((0, 20), (5, 60), (10, 100)).

TITULO = "Função linear e grandezas proporcionais"

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
    dict(id="s01", block="gancho", text="{a}Dois gráficos, {b}duas retas subindo. [p=0.3] Uma é o preço do feijão. [p=0.2] A outra, o preço de uma corrida de táxi. [p=0.3] Só uma delas mostra grandezas proporcionais, [p=0.2] e {c}um único ponto entrega qual é."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reconhece a proporção num gráfico, acha o número que liga as grandezas [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}a função afim, efe de xis igual a á xis mais bê, que tem uma reta como gráfico, [p=0.2] e {b}o teste do dobro: se uma grandeza dobra e a outra dobra junto, é direta. [p=0.3] Se faltar alguma, procure no canal."),
    # feijão
    dict(id="s04", block="feijao", text="Comece pelo feijão. [p=0.2] {a}Um quilo custa oito reais. [p=0.2] {b}Dois quilos, dezesseis. [p=0.2] {c}Três quilos, vinte e quatro. [p=0.3] E {d}zero quilo? [p=0.2] Zero real: quem não leva nada não paga nada."),
    dict(id="s05", block="feijao", text="A lei é {a}ípsilon igual a oito xis: o preço é oito vezes os quilos. [p=0.3] É uma função afim em que {b}o bê vale zero. [p=0.2] Não tem parte fixa nenhuma."),
    # função linear
    dict(id="s06", block="linear", text="Função afim com bê igual a zero tem nome próprio: {a}função linear. [p=0.2] Ela se escreve {b}ípsilon igual a ká xis, [p=0.2] em que ká é um número fixo. [p=0.3] No feijão, {c}ká vale oito: o preço de um quilo."),
    dict(id="s07", block="linear", text="E toda função linear é {a}diretamente proporcional. [p=0.2] Dobre o xis, e ká vezes o dobro {b}dá o dobro do resultado. [p=0.3] Divida o ípsilon pelo xis em qualquer linha: [p=0.2] {c}dezesseis dividido por dois dá oito. [p=0.2] {d}Vinte e quatro dividido por três dá oito. [p=0.3] Por isso o ká é a {e}constante de proporcionalidade: o número que essa divisão sempre dá."),
    # gráfico
    dict(id="s08", block="grafico", text="Vamos ao gráfico. [p=0.2] Marque {a}xis um, ípsilon oito, [p=0.2] {b}xis dois, ípsilon dezesseis, [p=0.2] e {c}xis três, ípsilon vinte e quatro. [p=0.3] A reta, prolongada para trás, {d}passa pela origem: o ponto xis zero, ípsilon zero."),
    dict(id="s09", block="grafico", text="Não é por acaso. [p=0.2] Com xis igual a zero, {a}ká vezes zero dá zero. [p=0.3] Toda função linear tem {b}uma reta que passa pela origem."),
    # táxi
    dict(id="s10", block="taxi", text="Compare com o táxi: {a}pê igual a cinco mais dois vírgula cinco dê. [p=0.3] Aqui o bê vale cinco, a bandeirada. [p=0.2] Com zero quilômetro, você já paga {b}cinco reais. [p=0.3] A reta {c}corta o eixo ípsilon no cinco, acima da origem."),
    dict(id="s11", block="taxi", text="Faça o teste do dobro. [p=0.2] {a}Dois quilômetros, dez reais. [p=0.2] {b}Quatro quilômetros, quinze reais. [p=0.2] Se fosse proporcional, seriam vinte. [p=0.3] A parte dos quilômetros dobrou, mas {c}a bandeirada continuou cinco. [p=0.3] Por isso a corrida não é proporcional à distância."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é achar que {a}toda reta que sobe é proporcional. [p=0.2] A do táxi sobe, e não é. [p=0.3] Veja a divisão: {b}dez dividido por dois dá cinco. [p=0.2] {c}Quinze dividido por quatro dá três vírgula setenta e cinco. [p=0.3] Mudou. [p=0.2] Subir não basta: {d}a reta precisa passar pela origem."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}se a reta passa pela origem, um ponto só dá o ká. [p=0.2] Pegue qualquer ponto da reta, fora a própria origem, e faça {b}ípsilon dividido por xis. [p=0.3] No feijão, {c}xis três, ípsilon vinte e quatro: [p=0.2] vinte e quatro dividido por três dá oito."),
    dict(id="s14", block="atalho", text="Funciona porque, se {a}o ípsilon é ká vezes o xis, dividir o ípsilon pelo xis devolve o ká. [p=0.3] Não compensa quando {b}o desenho não mostra a origem, com os eixos começando longe do zero. [p=0.2] Aí, {c}faça a divisão em dois pontos. [p=0.2] Deu o mesmo número? É proporcional."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] No gráfico, {a}duas retas. [p=0.2] A reta A sai da origem e passa por {b}xis cinco, ípsilon sessenta. [p=0.2] A reta B corta o eixo ípsilon {c}no vinte, e também passa por xis cinco, ípsilon sessenta. [p=0.3] {d}Qual delas é proporcional? [p=0.2] Qual é o ká dela, e qual é a lei?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] A reta A passa pela origem: {a}é proporcional. [p=0.2] Pelo atalho, {b}sessenta dividido por cinco dá doze. [p=0.2] Ká vale doze, e a lei é {c}ípsilon igual a doze xis."),
    dict(id="s18", block="resposta", text="A reta B não passa pela origem: {a}não é proporcional. [p=0.3] Repare na armadilha: {b}no ponto xis cinco, ípsilon sessenta, a divisão também dá doze. [p=0.2] Mas a reta B passa ainda por {c}xis dez, ípsilon cem, [p=0.2] e cem dividido por dez dá dez. [p=0.3] Mudou: {d}com a reta fora da origem, um ponto só engana."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}reta pela origem, grandezas proporcionais, [p=0.2] e {b}o ká é o ípsilon dividido pelo xis."),
    dict(id="s20", block="fim", text="Na próxima aula, duas retas dividem o mesmo gráfico: {a}o custo e a receita de uma pequena fábrica. [p=0.2] Você vai achar {b}quantas peças ela precisa vender para parar de ter prejuízo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
