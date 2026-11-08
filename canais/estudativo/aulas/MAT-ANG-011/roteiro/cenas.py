# Estudativo · MAT-ANG-011 — Tales no triângulo e teorema da bissetriz interna (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: usar uma paralela a um lado para achar um segmento e dividir o lado oposto na razão dos outros dois: lados 6 e 9 e oposto 10 dão pedaços 4 e 6.
# Pré-requisitos: MAT-ANG-010 (Tales, cruz, mesma ordem), MAT-ANG-008 (bissetriz). Próxima: MAT-ANG-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "á", "bê", "cê", "dê", "eme", "ene", "pê".
# Figuras: E.triangulo, E.segmento, E.angulo (metades iguais da bissetriz).
#   s04-s07: ABC com A em cima; MN paralelo a BC (M em AB, N em AC); terceira paralela tracejada passando por A. AM = 2, MB = 3, AN = 4, NC = x (6).
#   s09-s12: bissetriz de A até D em BC; AB = 6, AC = 9, BC = 10; BD = x (4), DC = 10 − x (6).
#   s13: isósceles com a bissetriz do topo caindo no meio da base (metades com tracinhos iguais), como no atalho de MAT-ANG-008; depois um lado vizinho cresce e o pedaço junto dele cresce.
#   Questão: AB = 8, AC = 12, BC = 15 (BD = 6, DC = 9).

TITULO = "Tales no triângulo e teorema da bissetriz interna"

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
    dict(id="s01", block="gancho", text="{a}Num triângulo, dois lados medem seis e nove, [p=0.2] e o lado da frente mede dez. [p=0.3] {b}A bissetriz do ângulo entre eles corta esse lado em dois pedaços. [p=0.2] Muita gente chuta {c}cinco e cinco. [p=0.3] {d}Errado: são quatro e seis."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você usa Tales dentro do triângulo, [p=0.2] acha esses pedaços sem medir [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o Teorema de Tales, com paralelas cortando transversais em pedaços proporcionais, [p=0.2] e {c}a bissetriz, que divide um ângulo ao meio. [p=0.3] Se faltar alguma, procure no canal."),
    # Tales no triângulo
    dict(id="s04", block="tales", text="Pegue {a}um triângulo á bê cê, com o á em cima. [p=0.2] Trace {b}uma reta paralela ao lado bê cê, [p=0.2] cortando o lado á bê no ponto eme [p=0.1] e o lado á cê no ponto ene."),
    dict(id="s05", block="tales", text="Onde está o feixe de paralelas? [p=0.2] Imagine {a}mais uma paralela, passando pelo á. [p=0.3] São {b}três paralelas: a do á, a eme ene e a bê cê. [p=0.2] E os lados á bê e á cê são {c}as transversais, que se encontram lá em cima."),
    dict(id="s06", block="tales", text="Então vale Tales: [p=0.2] {a}á eme está para eme bê, assim como á ene está para ene cê. [p=0.3] Pedaço de cima sobre pedaço de baixo, {b}nos lados cortados pela paralela."),
    dict(id="s07", block="tales", text="Exemplo: {a}á eme mede dois e eme bê mede três. [p=0.2] {b}Á ene mede quatro. [p=0.2] Quanto mede ene cê? [p=0.3] {c}Dois está para três, assim como quatro está para xis. [p=0.2] Cruz: {d}dois xis igual a três vezes quatro, que dá doze. [p=0.2] {e}Xis igual a seis."),
    # bissetriz
    dict(id="s08", block="bissetriz", text="E a bissetriz? [p=0.2] Na aula dela, você viu que, em geral, {a}ela não corta o lado da frente ao meio. [p=0.3] Então onde ela corta? [p=0.2] Quem responde é o {b}teorema da bissetriz interna."),
    dict(id="s09", block="bissetriz", text="A bissetriz do á corta o lado bê cê {a}no ponto dê. [p=0.2] Os pedaços ficam {b}na mesma razão dos lados vizinhos: [p=0.2] {c}bê dê está para dê cê, assim como á bê está para á cê. [p=0.3] Cada pedaço {d}acompanha o lado que encosta nele."),
    dict(id="s10", block="bissetriz", text="No gancho, {a}á bê mede seis, á cê mede nove e bê cê mede dez. [p=0.2] Chame {b}bê dê de xis. [p=0.2] O resto do lado, {c}dê cê, é dez menos xis."),
    dict(id="s11", block="bissetriz", text="{a}Xis está para dez menos xis, assim como seis está para nove. [p=0.3] Cruz: {b}nove xis igual a seis vezes, abre parênteses, dez menos xis. [p=0.2] Distribuindo: {c}nove xis igual a sessenta menos seis xis."),
    dict(id="s12", block="bissetriz", text="{a}Some seis xis em cada lado: quinze xis igual a sessenta. [p=0.2] {b}Xis igual a quatro. [p=0.3] Então {c}bê dê mede quatro, [p=0.2] e dê cê mede dez menos quatro, que dá seis."),
    # por que vale
    dict(id="s13", block="porque", text="Por que a regra faz sentido? [p=0.2] Uma imagem ajuda a lembrar, sem ser prova. [p=0.3] {a}No isósceles, você viu que a bissetriz do topo cai bem no meio da base. [p=0.2] {b}Lados vizinhos iguais, pedaços iguais: a regra concorda. [p=0.3] E quando um lado vizinho cresce, {c}o pedaço junto dele também cresce."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}ligar cada pedaço ao lado errado. [p=0.2] A pessoa monta {b}bê dê está para dê cê, assim como nove está para seis, [p=0.2] e acha {c}bê dê igual a seis e dê cê igual a quatro: [p=0.2] {d}trocados."),
    dict(id="s15", block="erro", text="Confira na figura: {a}o pedaço maior fica junto do lado maior. [p=0.2] Á cê, com nove, encosta em dê cê, [p=0.2] então {b}dê cê é o pedaço maior: seis."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho prometido: {a}divida em partes. [p=0.2] Primeiro, simplifique a razão dos lados, como numa fração: [p=0.2] seis para nove, dividindo por três, {b}fica dois para três. [p=0.3] Então pense no lado bê cê dividido em partes iguais: [p=0.2] {c}duas partes em bê dê e três partes em dê cê, cinco ao todo. [p=0.2] {d}Dez dividido por cinco dá dois por parte. [p=0.2] {e}Duas partes dão quatro. [p=0.2] Três partes dão seis."),
    dict(id="s17", block="atalho", text="Funciona porque {a}razão dois para três quer dizer isto: [p=0.2] a cada duas partes em bê dê, três partes em dê cê. [p=0.3] Não compensa quando a questão {b}já dá um dos pedaços: [p=0.2] aí, {c}a proporção direta é mais curta."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] No triângulo á bê cê, {a}á bê mede oito centímetros e á cê mede doze. [p=0.2] O lado {b}bê cê mede quinze. [p=0.3] A bissetriz do á corta bê cê no ponto dê. [p=0.2] {c}Quanto mede cada pedaço?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Oito e doze, divididos por quatro, ficam {a}dois e três. [p=0.2] O lado de quinze tem {b}cinco partes: [p=0.2] {c}quinze dividido por cinco dá três. [p=0.3] {d}Bê dê, junto do lado de oito, tem duas partes, que dão seis centímetros. [p=0.2] {e}Dê cê, junto do lado de doze, tem três partes, que dão nove centímetros."),
    dict(id="s21", block="resposta", text="Conferindo pela cruz: {a}seis está para nove, assim como oito está para doze. [p=0.2] {b}Seis vezes doze dá setenta e dois. [p=0.2] Nove vezes oito também dá setenta e dois. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}uma paralela a um lado corta os outros lados na mesma razão, [p=0.2] e {b}a bissetriz divide o lado da frente na razão dos lados vizinhos."),
    dict(id="s23", block="fim", text="Repare que a paralela de hoje separou {a}um triângulo menor, com o mesmo formato do grande. [p=0.3] Na próxima aula, você reconhece {b}triângulos semelhantes por dois ângulos iguais [p=0.2] e acha {c}o lado que falta. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
