# Estudativo · MAT-ANG-007 — Congruência de triângulos: LLL, LAL, ALA e LAAo (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: apontar qual caso garante que dois triângulos são iguais e descobrir por congruência um lado ou um ângulo que falta.
# Pré-requisitos: MAT-ANG-005 (classificar triângulos), MAT-ANG-004 (soma dos ângulos), MAT-ANG-002 (opostos pelo vértice). Próxima: MAT-ANG-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras dos vértices narradas como se falam: "á", "bê", "cê", "dê", "eme", "pê", "quê", "érre".
# Figuras: E.triangulo (pares de triângulos), E.marcas_iguais (lados iguais), E.angulo, E.segmento.
# s11-s13: "gravata" com os segmentos AC e BD se cruzando no ponto M (AM = MC = 4, BM = MD = 3, AB = 6).
# s15: erro do LLA — ângulo de 30° em A, AB = 6, e um arco de raio 4 centrado em B corta a outra reta em dois pontos (C1 e C2).
# Questão: ABC com AB = 9, Â = 50°, B̂ = 30°, BC = 7 (Ĉ = 100°); PQR com PQ = 9, P̂ = 50°, Q̂ = 30°.

TITULO = "Congruência de triângulos: LLL, LAL, ALA e LAAo"

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
    dict(id="s01", block="gancho", text="{a}Dois triângulos têm os mesmos ângulos: [p=0.2] cinquenta graus, sessenta graus e setenta graus. [p=0.3] Eles são iguais? [p=0.3] Quem disse sim {b}caiu na armadilha. [p=0.3] Um pode ser {c}a ampliação do outro: [p=0.2] mesmo formato, tamanho diferente."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber quais medidas bastam para garantir que dois triângulos são iguais, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}os ângulos de um triângulo somam cento e oitenta graus, [p=0.2] e {c}lados com o mesmo número de tracinhos são iguais. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é congruente
    dict(id="s04", block="congruente", text="Na geometria, triângulos iguais têm um nome: {a}congruentes. [p=0.2] Quer dizer {b}mesmo formato e mesmo tamanho. [p=0.3] Recorte um e coloque sobre o outro: [p=0.2] {c}ele cobre certinho, [p=0.2] mesmo que você precise girar ou virar o papel."),
    dict(id="s05", block="congruente", text="Cada triângulo tem {a}três lados e três ângulos. [p=0.2] São seis medidas. [p=0.3] A boa notícia: {b}você não precisa conferir todas. [p=0.2] Três medidas, no lugar certo, já bastam. [p=0.2] E são {c}quatro casos."),
    # os quatro casos
    dict(id="s06", block="lll", text="{a}Primeiro caso: lado, lado, lado. [p=0.2] Pegue três varetas: [p=0.1] {b}três centímetros, quatro centímetros e cinco centímetros. [p=0.3] Monte o triângulo do jeito que quiser: [p=0.2] {c}sempre sai o mesmo."),
    dict(id="s07", block="lll", text="É por isso que telhado e portão usam triângulos: [p=0.2] {a}com os lados fixos, ele não entorta. [p=0.3] Se os três lados de um são iguais aos três lados do outro, [p=0.2] {b}os triângulos são congruentes."),
    dict(id="s08", block="lal", text="{a}Segundo caso: lado, ângulo, lado. [p=0.2] Pense num compasso de desenho. [p=0.2] {b}As pernas têm tamanho fixo, [p=0.2] e {c}a abertura entre elas está travada. [p=0.3] Então a distância entre as pontas {d}também fica fixa. [p=0.3] O detalhe: {e}o ângulo precisa estar entre os lados, [p=0.2] como no meio do nome."),
    dict(id="s09", block="ala", text="{a}Terceiro caso: ângulo, lado, ângulo. [p=0.2] Um lado conhecido, [p=0.2] e {b}os ângulos das pontas desse lado. [p=0.3] As retas saem das pontas já inclinadas [p=0.2] e {c}só podem se encontrar num ponto. [p=0.2] O triângulo fica decidido."),
    dict(id="s10", block="laao", text="{a}Quarto caso: lado, ângulo e ângulo oposto. [p=0.2] Um lado, [p=0.1] {b}um ângulo numa ponta dele, [p=0.2] e {c}o ângulo lá da frente, oposto a esse lado. [p=0.3] Ele funciona por causa do cento e oitenta: [p=0.2] {d}com dois ângulos, você descobre o terceiro. [p=0.2] E {e}vira ângulo, lado, ângulo."),
    dict(id="s11", block="laao", text="Nos livros, cada caso aparece {a}pelas iniciais, como está na tela. [p=0.3] E três ângulos sozinhos? [p=0.2] {b}Não é caso, como você viu no começo. [p=0.2] Mesmo formato com tamanho diferente é {c}semelhança, assunto de outra aula."),
    # exemplo: descobrir a medida que falta
    dict(id="s12", block="gravata", text="Para que serve isso? [p=0.2] Para {a}descobrir uma medida sem medir. [p=0.3] Os segmentos {b}á cê e bê dê se cruzam no ponto eme. [p=0.2] Eme fica no meio de cada segmento: [p=0.2] {c}á eme e eme cê medem quatro. [p=0.2] {d}Bê eme e eme dê medem três."),
    dict(id="s13", block="gravata", text="O lado {a}á bê mede seis. [p=0.2] Quanto mede {b}cê dê? [p=0.3] Compare os triângulos {c}á eme bê e cê eme dê. [p=0.2] {d}Lado: quatro e quatro. [p=0.2] {e}Ângulo: no eme, eles são opostos pelo vértice, então são iguais. [p=0.2] {f}Lado: três e três."),
    dict(id="s14", block="gravata", text="O ângulo está entre os lados: [p=0.2] {a}lado, ângulo, lado. [p=0.2] Os triângulos são congruentes. [p=0.3] {b}Cê dê fica de frente para o ângulo do eme, assim como á bê. [p=0.2] Então {c}cê dê também mede seis."),
    # erro comum
    dict(id="s15", block="erro", text="O erro mais comum é {a}usar o ângulo fora do lugar: [p=0.2] dois lados e um ângulo que {b}não está entre eles."),
    dict(id="s16", block="erro", text="Veja: {a}ângulo de trinta graus no á, [p=0.2] {b}lado á bê com seis, [p=0.2] e {c}lado bê cê com quatro. [p=0.3] Preso no bê, o lado de quatro {d}encosta na outra reta em dois pontos. [p=0.2] Saem {e}dois triângulos diferentes com as mesmas medidas. [p=0.3] Por isso, {f}lado, lado e ângulo de fora não garantem que os triângulos são iguais."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho prometido: {a}dois ângulos valem por três. [p=0.3] Se a questão deu dois ângulos, {b}calcule o terceiro com o cento e oitenta. [p=0.2] Aí qualquer lado serve, [p=0.1] desde que esteja entre os mesmos ângulos nos dois triângulos: [p=0.2] {c}você sempre cai em ângulo, lado, ângulo."),
    dict(id="s18", block="atalho", text="Exemplo: {a}um lado de oito, [p=0.2] {b}cinquenta graus numa ponta [p=0.2] e {c}sessenta graus lá na frente. [p=0.3] Cinquenta mais sessenta dá cento e dez. [p=0.2] {d}Cento e oitenta menos cento e dez dá setenta. [p=0.3] Assim, o lado de oito {e}tem ângulo conhecido nas duas pontas."),
    dict(id="s19", block="atalho", text="Funciona porque {a}a soma dos ângulos é sempre cento e oitenta graus. [p=0.3] Não compensa quando a questão já deu {b}três lados, [p=0.2] ou {c}lado, ângulo e lado com o ângulo no meio: [p=0.2] aí o caso já está pronto."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] No triângulo {a}á bê cê, o lado á bê mede nove centímetros, [p=0.2] o ângulo em á mede cinquenta graus [p=0.1] e o ângulo em bê, trinta graus. [p=0.3] O lado {b}bê cê mede sete centímetros."),
    dict(id="s21", block="questao", text="No triângulo {a}pê quê érre, o lado pê quê também mede nove centímetros, [p=0.2] o ângulo em pê mede cinquenta graus [p=0.1] e o ângulo no vértice quê, trinta graus. [p=0.3] {b}Qual caso garante que eles são congruentes? [p=0.2] {c}Quanto medem o lado quê érre e o ângulo em érre?"),
    dict(id="s22", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta", text="Vamos lá. [p=0.2] Nos dois triângulos, o lado de nove está {a}entre o ângulo de cinquenta graus e o de trinta graus. [p=0.2] Caso {b}ângulo, lado, ângulo."),
    dict(id="s24", block="resposta", text="O vértice quê corresponde ao bê: {a}ambos têm trinta graus. [p=0.2] Então o lado quê érre corresponde a bê cê: {b}sete centímetros. [p=0.3] E o ângulo em érre: cinquenta mais trinta dá oitenta. [p=0.2] {c}Cento e oitenta menos oitenta dá cem graus."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: {a}três medidas no lugar certo garantem triângulos congruentes, [p=0.2] e {b}aí toda medida que falta é copiada do outro."),
    dict(id="s26", block="fim", text="Na próxima aula, você conhece {a}quatro linhas especiais do triângulo: [p=0.2] {b}altura, mediana, bissetriz e mediatriz, [p=0.2] e o que cada uma divide ou corta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
