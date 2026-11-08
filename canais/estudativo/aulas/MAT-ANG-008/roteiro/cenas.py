# Estudativo · MAT-ANG-008 — Altura, mediana, bissetriz e mediatriz (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: traçar altura, mediana, bissetriz e mediatriz num triângulo, dizer o que cada uma divide ou corta e apontar a altura de um obtusângulo, que cai fora dele.
# Pré-requisitos: MAT-ANG-007 (congruência), MAT-ANG-005 (classificar triângulos), MAT-ANG-001 (ângulo reto). Próxima: MAT-ANG-020.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras dos vértices narradas como se falam: "á", "bê", "cê", "eme", "pê".
# Figuras: E.triangulo com cada linha traçada em cor da matéria; E.marcas_iguais nas metades; E.angulo (arcos iguais da bissetriz, quadradinho do reto).
# s08-s09: obtusângulo com B̂ obtuso; o lado CB é prolongado (tracejado) além de B e a altura de A cai fora, com o quadradinho no prolongamento.
# s11: ponto P qualquer na mediatriz de AB, ligado a A e a B (PA = PB por LAL).
# s14: isósceles com topo de 40° e base 10: uma linha só, com 20° e 20°, 5 e 5, e ângulo reto na base.
# Questão: B̂ = 120°, Â = 24° (Ĉ = 36°).

TITULO = "Altura, mediana, bissetriz e mediatriz"

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
    dict(id="s01", block="gancho", text="{a}Quatro linhas, [p=0.2] quatro nomes parecidos: [p=0.2] {b}altura, mediana, bissetriz e mediatriz. [p=0.3] Na prova, quem troca uma pela outra {c}perde a questão inteira."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai traçar cada uma, [p=0.2] saber o que ela divide ou corta, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}o ângulo reto, de noventa graus, [p=0.2] {c}o triângulo isósceles, com dois lados iguais, [p=0.2] e {d}os casos de congruência. [p=0.3] Se faltar alguma, procure no canal."),
    # mediana
    dict(id="s04", block="mediana", text="{a}Comece pela mediana. [p=0.2] Ela sai de um vértice, [p=0.2] que é um dos cantos do triângulo, [p=0.2] e vai até {b}o ponto médio do lado da frente. [p=0.3] Ponto médio é {c}o ponto que divide o lado em duas metades iguais."),
    dict(id="s05", block="mediana", text="Se o lado {a}bê cê mede dez, [p=0.2] a mediana que sai do á chega no ponto eme, [p=0.2] e fica {b}cinco para cada lado. [p=0.3] Guarde assim: {c}mediana corta o lado ao meio."),
    # bissetriz
    dict(id="s06", block="bissetriz", text="{a}A bissetriz também sai de um vértice, [p=0.2] mas ela divide {b}o ângulo ao meio. [p=0.3] Se o ângulo em á mede {c}oitenta graus, [p=0.2] a bissetriz deixa {d}quarenta graus de cada lado. [p=0.3] Bis quer dizer {e}dois: ela corta o ângulo em duas partes iguais."),
    # altura
    dict(id="s07", block="altura", text="{a}A altura sai de um vértice e vai até o lado da frente [p=0.2] formando {b}um ângulo reto. [p=0.3] É como medir uma pessoa: [p=0.2] {c}a fita desce reta, em pé, até o chão. [p=0.2] A altura é {d}a distância do vértice até a reta desse lado."),
    dict(id="s08", block="obtuso", text="E se o triângulo for obtusângulo, com um ângulo maior que noventa graus? [p=0.3] Veja {a}o ângulo em bê, bem aberto. [p=0.2] Saindo do á, a linha em ângulo reto {b}não chega no lado bê cê. [p=0.3] Você precisa {c}prolongar esse lado para além do bê, [p=0.2] e a altura {d}cai fora do triângulo."),
    dict(id="s09", block="obtuso", text="No obtusângulo, isso acontece com {a}as alturas que saem dos ângulos agudos. [p=0.2] Só {b}a altura que sai do ângulo obtuso fica dentro. [p=0.3] E no triângulo retângulo, {c}os lados do ângulo reto já são alturas."),
    # mediatriz
    dict(id="s10", block="mediatriz", text="{a}A mediatriz é diferente das outras: [p=0.2] ela {b}não precisa sair de vértice nenhum. [p=0.3] É a reta que passa {c}pelo ponto médio de um lado [p=0.2] e {d}faz ângulo reto com ele. [p=0.2] Ela corta o lado ao meio, em pé."),
    dict(id="s11", block="mediatriz", text="E tem uma propriedade que vai ser útil: [p=0.2] {a}qualquer ponto da mediatriz fica à mesma distância das pontas do lado. [p=0.3] Pegue um ponto {b}pê nela e ligue às pontas. [p=0.2] Os triângulos que se formam têm {c}metades iguais do lado, o ângulo reto e um lado em comum: [p=0.2] {d}lado, ângulo, lado. [p=0.2] São congruentes, e {e}as ligações têm o mesmo tamanho."),
    # erro comum
    dict(id="s12", block="erro", text="O erro mais comum é achar que {a}a bissetriz também cai no meio do lado. [p=0.3] Em geral, {b}não cai. [p=0.2] Num triângulo com um lado bem mais comprido que o outro, [p=0.2] ela chega {c}longe do ponto médio. [p=0.3] Dividir o ângulo ao meio {d}não divide o lado ao meio."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho prometido: {a}no isósceles, a linha do topo faz tudo. [p=0.3] Saindo do vértice entre os lados iguais, [p=0.2] {b}a mesma linha é altura, mediana e bissetriz, [p=0.2] e {c}ela ainda cai em cima da mediatriz da base."),
    dict(id="s14", block="atalho", text="Exemplo: {a}topo de quarenta graus e base de dez. [p=0.2] Uma linha só divide o topo em {b}vinte graus e vinte graus, [p=0.2] divide a base em {c}cinco e cinco [p=0.2] e encontra a base em {d}ângulo reto."),
    dict(id="s15", block="atalho", text="Funciona por congruência. [p=0.2] As metades têm {a}os lados iguais do isósceles, [p=0.2] as metades da base [p=0.1] e {b}o lado do meio em comum. [p=0.2] Lado, lado, lado: {c}as metades são iguais. [p=0.3] Não compensa {d}nos vértices da base, [p=0.2] nem no escaleno: lá, {e}cada linha vai para um lugar diferente. [p=0.2] Só no equilátero o atalho vale para os três vértices."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] No triângulo á bê cê, {a}o ângulo em bê mede cento e vinte graus [p=0.2] e {b}o ângulo em á mede vinte e quatro graus. [p=0.3] {c}A bissetriz do á divide esse ângulo em duas partes: quanto mede cada uma? [p=0.2] {d}E a altura que sai do á cai dentro ou fora do triângulo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] A bissetriz divide o ângulo ao meio: [p=0.2] {a}vinte e quatro dividido por dois dá doze. [p=0.2] {b}Doze graus de cada lado."),
    dict(id="s19", block="resposta", text="O ângulo em bê passa de noventa graus, então o triângulo é {a}obtusângulo. [p=0.2] O á não é o vértice do ângulo obtuso, [p=0.2] então {b}a altura do á cai fora. [p=0.3] Prolongue o lado cê bê para além do bê [p=0.2] e desça a linha até ele, {c}em ângulo reto."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}mediana corta o lado ao meio, [p=0.2] {b}bissetriz corta o ângulo ao meio, [p=0.2] {c}altura chega em ângulo reto, [p=0.2] e {d}mediatriz corta o lado ao meio em ângulo reto."),
    dict(id="s21", block="fim", text="Na próxima aula, cada uma dessas linhas aparece {a}três vezes no triângulo, [p=0.2] e as três se cruzam {b}num ponto só. [p=0.3] Um desses pontos, o {c}baricentro, divide a mediana em dois pedaços, um com o dobro do outro. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
