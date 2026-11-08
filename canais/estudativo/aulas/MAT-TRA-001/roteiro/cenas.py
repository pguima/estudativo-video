# Estudativo · MAT-TRA-001 — Lei dos senos (Matemática · Trigonometria Avançada · Lei dos senos e dos cossenos).
# Habilidade: achar o lado b = 10√2 num triângulo com ângulos de 30° e 45°, sabendo que o lado oposto a 30° mede 10.
# Pré-requisitos: MAT-TRI-002 (cateto oposto = hipotenusa × seno), MAT-TRI-009 (sen 120° = sen 60°). Usa MAT-TRI-003 (sen 30° = 1/2,
#   sen 45° = √2/2, sen 60° = √3/2), MAT-FRA-011 (dividir por 1/2 é multiplicar por 2), MAT-ANG-004 (soma 180°). Próxima: MAT-TRA-002.
# Questão inédita, criada para esta aula. Seno narrado por extenso; na tela, sen. Lados nomeados pelo ângulo de frente ("o lado de
#   frente para os trinta graus"); a letra minúscula do livro só aparece na regra. "Raiz de dois dividido por dois", como na MAT-TRI-003.
# Aproximações das aulas anteriores: √2 ≈ 1,4 e √3 ≈ 1,7.
# Contas: A = 30°, B = 45°, C = 105° · altura h = x · sen 30° = 10 · sen 45° · 10 / (1/2) = 20 · x = 20 · √2/2 = 10√2 ≈ 14 (> 10, 45° > 30°).
# Erro: 10 com 45° → 10 / (√2/2) = 10√2 · x = 10√2 · 1/2 = 5√2 ≈ 7 (menor que 10, de frente para o ângulo maior: impossível).
# Questão: 30° e 120°, lado oposto a 30° = 5 · 5 / (1/2) = 10 · sen 120° = sen 60° = √3/2 · 10 · √3/2 = 5√3 ≈ 8,5.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Lei dos senos"

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
    dict(id="s01", block="gancho", text="{a}Um triângulo com ângulos de trinta e de quarenta e cinco graus. [p=0.2] {b}O lado de frente para os trinta mede dez. [p=0.3] {c}Quanto mede o lado de frente para os quarenta e cinco? [p=0.3] {d}Não tem ângulo reto, [p=0.2] então seno, cosseno e tangente do triângulo retângulo não resolvem direto."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve isso numa linha, com a lei dos senos, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}no triângulo retângulo, o cateto oposto é a hipotenusa vezes o seno do ângulo; [p=0.2] e {c}o seno de um ângulo maior que noventa graus, como seno de cento e cinquenta, que é igual a seno de trinta. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem
    dict(id="s04", block="altura", text="De onde vem a lei? [p=0.2] Trace {a}a altura que desce do vértice de cima. [p=0.2] Ela parte o triângulo em {b}dois triângulos retângulos, [p=0.2] e {c}a altura é cateto nos dois."),
    dict(id="s05", block="altura", text="{a}No da esquerda, a hipotenusa é o lado que você quer, o xis, [p=0.2] e o ângulo é trinta graus. [p=0.2] Então {b}a altura é xis vezes seno de trinta. [p=0.3] {c}No da direita, a hipotenusa é o dez, [p=0.2] e o ângulo é quarenta e cinco. [p=0.2] {d}A altura é dez vezes seno de quarenta e cinco."),
    dict(id="s06", block="altura", text="A altura é uma só, então {a}xis vezes seno de trinta é igual a dez vezes seno de quarenta e cinco. [p=0.3] Divida cada lado da igualdade pelos dois senos, [p=0.2] e aparece {b}a lei dos senos: [p=0.2] {c}cada lado, dividido pelo seno do ângulo de frente para ele, dá o mesmo número."),
    # a regra
    dict(id="s07", block="regra", text="Nos livros, ela vem com letras: [p=0.2] {a}á dividido por seno de á, igual a bê dividido por seno de bê, igual a cê dividido por seno de cê. [p=0.3] {b}A letra minúscula é o lado. [p=0.2] {c}A maiúscula é o ângulo de frente para ele. [p=0.3] Lado e ângulo de frente formam {d}um par."),
    # a conta
    dict(id="s08", block="conta", text="Agora, a conta. [p=0.2] {a}Dez dividido por seno de trinta, igual a xis dividido por seno de quarenta e cinco. [p=0.3] {b}Seno de trinta é um meio, [p=0.2] e dividir por um meio é multiplicar por dois: [p=0.2] {c}dez vezes dois, vinte."),
    dict(id="s09", block="conta", text="Então {a}xis dividido por seno de quarenta e cinco também dá vinte. [p=0.2] Para achar xis, {b}multiplique vinte pelo seno de quarenta e cinco: [p=0.2] {c}vinte vezes raiz de dois dividido por dois, [p=0.2] {d}dez raiz de dois. [p=0.3] Com raiz de dois perto de um vírgula quatro, {e}dá cerca de catorze."),
    dict(id="s10", block="conta", text="Confira: {a}o maior ângulo fica de frente para o maior lado. [p=0.2] {b}Quarenta e cinco é maior que trinta, [p=0.2] e {c}catorze é maior que dez. [p=0.2] Faz sentido."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}formar o par errado. [p=0.2] A pessoa junta {b}o dez com os quarenta e cinco graus, [p=0.2] que encostam nele, mas não ficam de frente. [p=0.3] A conta dá {c}cerca de sete."),
    dict(id="s12", block="erro", text="Sete de frente para quarenta e cinco, e dez de frente para trinta? [p=0.2] {a}O lado maior ficaria de frente para o ângulo menor. [p=0.2] {b}Não pode. [p=0.3] {c}Cada lado só conversa com o ângulo de frente para ele."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}ache primeiro o número fixo. [p=0.2] É {b}o lado do par completo dividido pelo seno do seu ângulo. [p=0.2] Aqui, {c}vinte. [p=0.3] Daí, {d}qualquer lado é vinte vezes o seno do ângulo de frente para ele. [p=0.2] {e}Quarenta e cinco graus: vinte vezes raiz de dois dividido por dois, dez raiz de dois."),
    dict(id="s14", block="atalho", text="Funciona porque a lei garante que {a}a divisão dá o mesmo número para os três lados. [p=0.3] {b}Só não começa sem um par completo: [p=0.2] um lado e o ângulo de frente para ele. [p=0.2] {c}Sem esse par, o caso é da lei dos cossenos, a da próxima aula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Num triângulo, dois ângulos medem {a}trinta e cento e vinte graus. [p=0.2] {b}O lado de frente para os trinta mede cinco metros. [p=0.3] {c}Quanto mede o lado de frente para os cento e vinte?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] O número fixo: {a}cinco dividido por um meio dá dez. [p=0.3] {b}Seno de cento e vinte é igual a seno de sessenta, [p=0.2] pela redução ao primeiro quadrante: {c}raiz de três dividido por dois."),
    dict(id="s18", block="resposta", text="{a}Dez vezes raiz de três dividido por dois dá cinco raiz de três. [p=0.2] Com raiz de três perto de um vírgula sete, {b}cerca de oito vírgula cinco metros. [p=0.3] {c}O maior ângulo tem o maior lado: faz sentido."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}cada lado dividido pelo seno do ângulo de frente dá o mesmo número. [p=0.2] {b}Ache esse número com o par completo [p=0.2] e {c}multiplique pelo seno do ângulo que você quer."),
    dict(id="s20", block="fim", text="Na próxima aula, a lei dos cossenos: [p=0.2] você acha {a}o terceiro lado quando sabe dois lados e o ângulo entre eles, [p=0.2] como {b}lados três e cinco, com cento e vinte graus no meio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
