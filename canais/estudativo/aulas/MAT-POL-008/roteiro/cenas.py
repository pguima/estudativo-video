# Estudativo · MAT-POL-008 — Cordas que se cruzam e secantes (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: usar que o produto dos pedaços de uma corda é igual ao da outra (3 · 8 = 4 · x dá x = 6) e aplicar a mesma ideia a duas secantes.
# Pré-requisitos: MAT-ANG-012 (semelhança por dois ângulos), MAT-POL-006 (ângulo inscrito, metade do central). Usa também MAT-ANG-002 (opostos pelo vértice). Próxima: MAT-POL-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "pê", "xis".
# Secante e tangente são explicadas na hora (MAT-POL-007 não está na cadeia de pré-requisitos desta aula).
# Visual: E.circulo com cordas (E.segmento); pedaços rotulados; E.angulo para marcar ângulos iguais.
#   s01-s05: cordas AB e CD cruzando em P; PA = 3, PB = 8, PC = 4, PD = x (x = 6).
#   s06-s07: triângulos PAC e PDB destacados; ângulos opostos pelo vértice em P; inscritos em A e em D abrindo o mesmo arco CB.
#   s08-s13: ponto P fora; secante 1 passa pelo centro: fora 2, dentro 16 (inteira 18, raio 8, P a 10 do centro);
#            secante 2: fora 4, dentro x (inteira 9, x = 5). Erro: 2 · 16 = 4 · x dá x = 8.
#   s14-s16: tangente de P: tangente² = 2 · 18 = 36, tangente 6 (triângulo 6-8-10 com o raio).
#   Questão: secante 1 fora 4, dentro 21 (inteira 25, produto 100); secante 2 fora 5, inteira 20, dentro 15; tangente 10.

TITULO = "Cordas que se cruzam e secantes"

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
    dict(id="s01", block="gancho", text="{a}Duas cordas se cruzam dentro de uma circunferência. [p=0.2] Uma fica cortada em pedaços de {b}três e de oito centímetros. [p=0.2] A outra, em {c}quatro e num pedaço que ninguém mediu. [p=0.3] Sem régua, dá para saber que ele mede {d}seis centímetros."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o pedaço que falta em cordas e em secantes, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}triângulos com dois ângulos iguais são semelhantes, e os lados ficam proporcionais; [p=0.2] e {c}o ângulo inscrito vale a metade do central do mesmo arco. [p=0.3] Se faltar alguma, procure no canal."),
    # cordas
    dict(id="s04", block="cordas", text="Corda é {a}o segmento que liga dois pontos da circunferência. [p=0.2] Quando duas cordas se cruzam num ponto {b}pê, [p=0.2] cada uma fica dividida em {c}dois pedaços. [p=0.3] A regra: {d}o produto dos pedaços de uma é igual ao produto dos pedaços da outra."),
    dict(id="s05", block="cordas", text="No exemplo: {a}três vezes oito é igual a quatro vezes xis. [p=0.2] {b}Três vezes oito dá vinte e quatro. [p=0.2] {c}Quatro xis igual a vinte e quatro. [p=0.2] {d}Xis igual a seis centímetros."),
    dict(id="s06", block="porque", text="De onde vem isso? [p=0.2] Ligue as pontas das cordas e aparecem {a}dois triângulos. [p=0.3] Os ângulos em pê são {b}opostos pelo vértice: iguais. [p=0.2] E {c}os ângulos inscritos que abrem o mesmo arco [p=0.2] valem a metade do mesmo central: {d}também são iguais."),
    dict(id="s07", block="porque", text="Dois ângulos iguais: {a}triângulos semelhantes. [p=0.2] Os lados ficam proporcionais, [p=0.2] e a cruz da proporção vira {b}pedaço vezes pedaço igual a pedaço vezes pedaço. [p=0.3] Na prova, você {c}só usa a regra."),
    # secantes
    dict(id="s08", block="secantes", text="A mesma ideia vale {a}fora da circunferência. [p=0.2] {b}Secante é a reta que corta a circunferência em dois pontos. [p=0.3] De um ponto pê do lado de fora, saem {c}duas secantes. [p=0.2] Em cada uma, há {d}o pedaço de fora, de pê até a circunferência, [p=0.2] e {e}a secante inteira, de pê até o outro lado."),
    dict(id="s09", block="secantes", text="A regra: {a}o de fora vezes a inteira dá o mesmo nas duas secantes. [p=0.3] Repare que os pedaços {b}sempre começam no pê, [p=0.2] como nas cordas. [p=0.2] E o motivo é o mesmo: {c}dois triângulos semelhantes, com o ângulo do pê em comum."),
    dict(id="s10", block="secantes", text="Exemplo. [p=0.2] Uma secante tem {a}dois centímetros fora [p=0.2] e {b}dezesseis dentro. [p=0.3] A outra tem {c}quatro fora, [p=0.2] e o pedaço de dentro é {d}o xis."),
    dict(id="s11", block="secantes", text="A inteira da primeira: {a}dois mais dezesseis dá dezoito. [p=0.2] {b}Dois vezes dezoito dá trinta e seis. [p=0.3] Na outra, {c}quatro vezes a inteira dá trinta e seis, [p=0.2] então {d}a inteira mede nove. [p=0.2] Tirando o pedaço de fora: {e}nove menos quatro dá cinco centímetros."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}usar o pedaço de dentro no lugar da inteira, [p=0.2] como se fosse corda. [p=0.3] A pessoa faz {b}dois vezes dezesseis, que dá trinta e dois, [p=0.2] e {c}quatro vezes xis igual a trinta e dois. [p=0.2] Acha {d}xis igual a oito: errado."),
    dict(id="s13", block="erro", text="Na corda, os pedaços saem do pê {a}para lados opostos. [p=0.2] Na secante, {b}saem do pê para o mesmo lado: [p=0.2] um até o primeiro ponto, o outro até o segundo. [p=0.2] Por isso entra {c}a secante inteira."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho prometido: {a}a tangente. [p=0.2] Tangente é a reta que {b}só encosta na circunferência, num ponto. [p=0.3] Se do pê também sai uma tangente, [p=0.2] {c}a tangente ao quadrado é igual ao de fora vezes a inteira de qualquer secante."),
    dict(id="s15", block="atalho", text="No exemplo, o de fora vezes a inteira deu {a}trinta e seis. [p=0.2] Então {b}a tangente ao quadrado é trinta e seis, [p=0.2] e {c}a tangente mede seis centímetros. [p=0.3] Sem desenhar mais nada."),
    dict(id="s16", block="atalho", text="Funciona porque a tangente é {a}uma secante em que os pontos de corte se juntaram num só. [p=0.2] Imagine a secante {b}girando em volta do pê até só encostar. [p=0.2] O de fora e a inteira {c}ficam iguais, e o produto vira um quadrado. [p=0.3] Não compensa quando {d}a reta corta em dois pontos: [p=0.2] aí não tem quadrado, {e}é o de fora vezes a inteira."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] De um ponto pê, fora de uma circunferência, saem duas secantes. [p=0.3] Na primeira, {a}quatro centímetros ficam fora e vinte e um dentro. [p=0.2] Na segunda, {b}cinco ficam fora. [p=0.3] {c}Quanto mede o pedaço de dentro da segunda? [p=0.2] {d}E a tangente que sai do pê?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] A inteira da primeira: {a}quatro mais vinte e um dá vinte e cinco. [p=0.2] {b}Quatro vezes vinte e cinco dá cem. [p=0.3] Na segunda, {c}cinco vezes a inteira dá cem, [p=0.2] então {d}a inteira mede vinte. [p=0.2] {e}Vinte menos cinco dá quinze centímetros dentro."),
    dict(id="s20", block="resposta", text="E a tangente: {a}ao quadrado, ela dá cem. [p=0.2] {b}A tangente mede dez centímetros. [p=0.3] Quem usasse o pedaço de dentro, {c}quatro vezes vinte e um, [p=0.2] chegaria em oitenta e quatro, e a conta nem sairia exata."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}nas cordas, pedaço vezes pedaço. [p=0.2] {b}Nas secantes, o de fora vezes a inteira. [p=0.2] {c}Tudo medido a partir do pê."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica {a}polígonos e circunferência: [p=0.2] {b}quadriláteros, polígonos regulares, voltas de roda e ângulos na circunferência. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
