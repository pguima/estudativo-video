# Estudativo · MAT-POL-006 — Ângulo central e ângulo inscrito (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: usar que o inscrito vale metade do central do mesmo arco (central de 100°, inscrito de 50°) e que todo ângulo inscrito numa semicircunferência é reto.
# Pré-requisitos: MAT-ANG-005 (isósceles), MAT-ANG-004 (ângulo externo), MAT-POL-005 (arco e ângulo central). Próxima: MAT-POL-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Ângulo central e ângulo inscrito"

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
    dict(id="s01", block="gancho", text="{a}Meia pizza, cortada bem no meio. [p=0.2] Escolha {b}qualquer ponto da borda curva [p=0.2] e ligue às pontas do corte reto. [p=0.3] O ângulo nesse ponto {c}é sempre reto. [p=0.2] Ponto aqui, ponto ali: {d}noventa graus."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você entende por que isso acontece, [p=0.2] {b}calcula ângulos dentro da circunferência [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}o ângulo externo de um triângulo vale a soma dos internos de longe, [p=0.2] {c}no isósceles, os ângulos da base são iguais, [p=0.2] e {d}o ângulo central tem o vértice no centro e abre um arco. [p=0.3] Se faltar alguma, procure no canal."),
    # central
    dict(id="s04", block="central", text="{a}No ângulo central, os lados são raios. [p=0.2] Ele abre {b}um arco da circunferência. [p=0.3] E o arco também pode ser medido {c}em graus: [p=0.2] {d}ele mede o mesmo que o seu ângulo central."),
    # inscrito
    dict(id="s05", block="inscrito", text="Agora, o ângulo inscrito. [p=0.2] O vértice fica {a}em cima da circunferência. [p=0.2] E os lados são {b}cordas: [p=0.1] segmentos que ligam dois pontos da circunferência. [p=0.3] Ele também abre {c}um arco: o pedaço que fica entre os lados, do outro lado do círculo."),
    dict(id="s06", block="inscrito", text="Quando um central e um inscrito abrem {a}o mesmo arco, vale a regra: [p=0.2] {b}o inscrito vale a metade do central. [p=0.3] Central de {c}cem graus, [p=0.2] inscrito de {d}cinquenta graus."),
    # por que a metade
    dict(id="s07", block="prova", text="Por que a metade? [p=0.2] Pegue o caso em que {a}um lado do inscrito passa pelo centro, que vamos chamar de ponto ó. [p=0.2] O vértice do inscrito é {b}pê, e o arco vai de á até bê. [p=0.3] Ligue {c}o centro ao bê. [p=0.2] Nasce o triângulo {d}ó pê bê. [p=0.2] Os lados ó pê e ó bê são raios, então ele é {e}isósceles."),
    dict(id="s08", block="prova", text="No isósceles, {a}os ângulos da base são iguais: [p=0.2] o ângulo em pê, que é o inscrito, {b}é igual ao ângulo em bê. [p=0.2] Chame cada um de {c}xis."),
    dict(id="s09", block="prova", text="O ângulo central fica {a}do lado de fora desse triângulo, [p=0.2] porque o lado pê ó continua até o á. [p=0.2] Ele é {b}um ângulo externo. [p=0.3] E o externo vale {c}a soma dos internos de longe: [p=0.2] {d}xis mais xis dá dois xis. [p=0.3] {e}O central é o dobro do inscrito. [p=0.2] Com o centro em outras posições, a regra continua valendo."),
    # semicircunferência
    dict(id="s10", block="semi", text="Voltando à pizza do começo. [p=0.2] O corte reto é {a}um diâmetro, [p=0.1] e o arco do outro lado é {b}uma semicircunferência: meia volta. [p=0.3] O central desse arco é {c}a linha reta: cento e oitenta graus."),
    dict(id="s11", block="semi", text="O inscrito vale a metade: [p=0.2] {a}cento e oitenta dividido por dois dá noventa. [p=0.3] {b}Todo ângulo inscrito numa semicircunferência é reto. [p=0.2] Não importa onde fica o vértice na borda."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: {a}dividir quando devia multiplicar. [p=0.3] Um inscrito mede {b}trinta e cinco graus. [p=0.2] Quanto mede o central do mesmo arco? [p=0.2] Quem divide por dois acha {c}dezessete vírgula cinco. [p=0.3] Mas {d}o central é sempre o maior. [p=0.2] É o dobro: {e}duas vezes trinta e cinco dá setenta graus."),
    # atalho
    dict(id="s13", block="atalho", text="E o atalho prometido: [p=0.2] {a}viu um triângulo com um lado no diâmetro e o outro vértice na circunferência? [p=0.2] {b}O ângulo nesse vértice é reto, sem conta. [p=0.3] E {c}os outros ângulos do triângulo são complementares: [p=0.2] somam noventa."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o diâmetro abre meia volta, e a metade de cento e oitenta é noventa. [p=0.3] {b}Não vale se o lado não passa pelo centro: [p=0.2] uma corda qualquer não é diâmetro. [p=0.2] Aí, {c}volte para a metade do central."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Numa circunferência de centro no ponto ó, {a}o segmento á bê é um diâmetro, [p=0.2] e {b}cê é um ponto da circunferência. [p=0.2] No triângulo á bê cê, o ângulo em á mede {c}vinte e cinco graus. [p=0.3] {d}Quanto medem os ângulos em cê e em bê? [p=0.2] {e}E o ângulo central bê ó cê?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Lado á bê no diâmetro, vértice cê na circunferência: [p=0.2] {a}o ângulo em cê é reto, noventa graus. [p=0.2] {b}Em bê, noventa menos vinte e cinco dá sessenta e cinco graus."),
    dict(id="s18", block="resposta", text="O ângulo em á é inscrito e abre {a}o arco de bê até cê. [p=0.2] O central bê ó cê abre {b}o mesmo arco. [p=0.2] Então ele é o dobro: {c}duas vezes vinte e cinco dá cinquenta graus."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o inscrito vale a metade do central do mesmo arco, [p=0.2] e {b}numa semicircunferência, o inscrito é sempre reto."),
    dict(id="s20", block="fim", text="Na próxima aula, uma reta encontra a circunferência. [p=0.2] Ela pode {a}passar longe, só encostar ou cortar. [p=0.2] E a reta que só encosta {b}faz ângulo reto com o raio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
