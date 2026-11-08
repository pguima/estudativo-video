# Estudativo · MAT-POL-003 — Polígonos regulares: ângulo interno, externo e ladrilhos (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: calcular o ângulo interno do octógono regular (135°) e explicar por que hexágonos regulares cobrem um piso sem buracos e pentágonos não.
# Pré-requisitos: MAT-POL-002 (soma dos ângulos internos), MAT-ANG-004 (ângulo externo). Próxima: MAT-POL-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Polígonos regulares: ângulo interno, externo e ladrilhos"

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
    dict(id="s01", block="gancho", text="{a}Olhe um favo de mel. [p=0.2] As abelhas usam {b}hexágonos, encaixados sem nenhum buraco. [p=0.3] Por que não {c}pentágonos? [p=0.3] A resposta está {d}num único ângulo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o ângulo de qualquer polígono regular, [p=0.2] {b}descobre quais deles formam um piso sem buracos [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a soma dos ângulos internos de um polígono é ene menos dois, vezes cento e oitenta, [p=0.2] e {c}o ângulo externo nasce quando você prolonga um lado. [p=0.3] Se faltar alguma, procure no canal."),
    # regular
    dict(id="s04", block="regular", text="{a}Polígono regular tem todos os lados iguais e todos os ângulos iguais. [p=0.3] As duas exigências juntas. [p=0.2] {b}Um losango achatado tem lados iguais, mas ângulos diferentes: não é regular. [p=0.2] {c}Um retângulo comprido tem ângulos iguais, mas lados diferentes: também não. [p=0.3] {d}O quadrado, que é losango e retângulo ao mesmo tempo, é o quadrilátero regular."),
    dict(id="s05", block="regular", text="Como os ângulos são iguais, {a}cada ângulo interno é a soma dividida pelo número de lados. [p=0.3] No octógono, a soma é {b}seis vezes cento e oitenta, que dá mil e oitenta. [p=0.2] {c}Mil e oitenta dividido por oito dá cento e trinta e cinco graus."),
    dict(id="s06", block="regular", text="No hexágono, a soma é {a}setecentos e vinte. [p=0.2] {b}Setecentos e vinte dividido por seis dá cento e vinte graus. [p=0.3] No pentágono, a soma é {c}quinhentos e quarenta. [p=0.2] {d}Quinhentos e quarenta dividido por cinco dá cento e oito graus."),
    # externo
    dict(id="s07", block="externo", text="Agora o ângulo externo. [p=0.2] {a}Prolongue um lado do octógono. [p=0.2] Entre o prolongamento e o lado vizinho, nasce {b}o externo. [p=0.3] Ele e o interno estão {c}sobre uma linha reta: [p=0.2] {d}cento e oitenta menos cento e trinta e cinco dá quarenta e cinco graus."),
    dict(id="s08", block="externo", text="E aqui tem uma regra bonita. [p=0.2] Imagine que você {a}caminha pela borda do octógono. [p=0.2] Em cada vértice, você {b}vira o ângulo externo. [p=0.3] Quando chega de volta ao começo, deu {c}uma volta completa. [p=0.2] {d}A soma dos externos é trezentos e sessenta graus, em qualquer polígono convexo."),
    # erro
    dict(id="s09", block="erro", text="Cuidado com o erro mais comum: {a}trocar o externo pelo interno. [p=0.3] A pessoa faz {b}trezentos e sessenta dividido por oito, acha quarenta e cinco [p=0.2] e diz que esse é o ângulo do octógono. [p=0.3] Mas {c}quarenta e cinco é agudo, [p=0.2] e {d}os cantos do octógono são bem abertos: obtusos. [p=0.2] Quarenta e cinco é o externo."),
    # atalho
    dict(id="s10", block="atalho", text="E o atalho prometido: {a}comece pelo externo. [p=0.3] {b}Trezentos e sessenta dividido pelo número de lados. [p=0.2] Depois, {c}o interno é cento e oitenta menos ele. [p=0.3] Octógono: {d}trezentos e sessenta dividido por oito dá quarenta e cinco; [p=0.2] {e}cento e oitenta menos quarenta e cinco dá cento e trinta e cinco."),
    dict(id="s11", block="atalho", text="Funciona porque {a}a volta completa não depende do número de lados, [p=0.2] e a conta fica bem menor que a da soma. [p=0.3] {b}Só vale para polígono regular. [p=0.2] Se os ângulos forem diferentes, {c}os externos também são, [p=0.2] e só a soma de trezentos e sessenta continua valendo."),
    # piso
    dict(id="s12", block="piso", text="Agora o piso. [p=0.2] Para cobrir um chão sem buracos e sem peça em cima de peça, [p=0.2] os cantos que se encontram num ponto {a}precisam fechar uma volta: trezentos e sessenta graus."),
    dict(id="s13", block="piso", text="{a}Hexágono regular: cento e vinte graus. [p=0.2] {b}Três hexágonos num ponto: três vezes cento e vinte dá trezentos e sessenta. [p=0.2] {c}Fecha certinho. [p=0.2] É o favo de mel."),
    dict(id="s14", block="piso", text="{a}Pentágono regular: cento e oito graus. [p=0.2] {b}Três pentágonos num ponto: três vezes cento e oito dá trezentos e vinte e quatro. [p=0.1] {c}Sobra um buraco de trinta e seis graus. [p=0.2] {d}Com quatro pentágonos, quatro vezes cento e oito dá quatrocentos e trinta e dois. [p=0.1] Passa da volta, e uma peça fica em cima da outra. [p=0.3] {e}Pentágonos regulares não cobrem o piso sozinhos."),
    dict(id="s15", block="piso", text="A regra: {a}um polígono regular cobre o piso sozinho quando o ângulo interno cabe um número exato de vezes em trezentos e sessenta. [p=0.3] Só três passam no teste: [p=0.2] {b}o triângulo equilátero, de sessenta graus, [p=0.2] {c}o quadrado, de noventa, [p=0.2] e {d}o hexágono, de cento e vinte."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um polígono regular tem {a}doze lados. [p=0.3] {b}Quanto mede cada ângulo interno? [p=0.2] {c}E, num piso com dois desses polígonos em cada ponto, que polígono regular completa o encaixe?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá, pelo atalho. [p=0.2] {a}Externo: trezentos e sessenta dividido por doze dá trinta. [p=0.2] {b}Interno: cento e oitenta menos trinta dá cento e cinquenta graus."),
    dict(id="s19", block="resposta", text="No ponto, {a}cento e cinquenta mais cento e cinquenta dá trezentos. [p=0.2] {b}Para fechar a volta, faltam sessenta graus. [p=0.2] Sessenta é o ângulo do {c}triângulo equilátero. [p=0.3] Conferindo pela soma: {d}dez vezes cento e oitenta dá mil e oitocentos, [p=0.2] e mil e oitocentos dividido por doze dá cento e cinquenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}regular tem lados e ângulos iguais. [p=0.2] {b}O externo é trezentos e sessenta dividido pelo número de lados, [p=0.2] {c}o interno é cento e oitenta menos o externo. [p=0.2] E, {d}no piso, os cantos fecham trezentos e sessenta."),
    dict(id="s21", block="fim", text="Na próxima aula, uma figura sem lado nenhum: {a}a circunferência. [p=0.2] Você conhece {b}raio e diâmetro [p=0.2] e calcula {c}quanto uma roda anda em cada volta. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
