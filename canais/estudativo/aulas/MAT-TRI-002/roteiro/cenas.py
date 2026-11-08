# Estudativo · MAT-TRI-002 — Achar um lado com seno, cosseno ou tangente (Matemática · Trigonometria).
# Habilidade: escolher a razão certa e achar o cateto oposto a 37° com hipotenusa 10, usando sen 37° = 0,6 (6).
# Pré-requisitos: MAT-TRI-001 (seno, cosseno e tangente), MAT-EQU-010 (equação com decimais). Próxima: MAT-TRI-003.
# Questão inédita, criada para esta aula. Valores de 37° como a prova costuma dar: sen ≈ 0,6, cos ≈ 0,8, tg ≈ 0,75 (reais: 0,6018; 0,7986; 0,7536).
# Contas: escada 10 m a 37° do chão · altura = 10 · 0,6 = 6 · pé = 10 · 0,8 = 8 · 36 + 64 = 100 (6-8-10 = 3-4-5 dobrado).
# Telhado: avança 8 m, 37° · subida = 0,75 · 8 = 6.
# Erro: "ângulo embaixo, cosseno" → 0,8 · 10 = 8 para a altura (é a distância no chão).
# Atalho: oposto = hipotenusa · seno; adjacente = hipotenusa · cosseno; não compensa quando falta a hipotenusa (divide).
# Questão: pipa a 12 m, linha a 37° do chão · 0,6 = 12/x · 0,6x = 12 · 6x = 120 · x = 20 m · erro: 0,6 · 12 = 7,2 < 12.
# Visual (E.triangulo, E.angulo):
#   s01, s05-s08: escada apoiada na parede (triângulo com o chão), ângulo de 37° no pé; rótulos hipotenusa 10, oposto x, adjacente.
#   s04: as três perguntas em cartões: ângulo? lado que conheço? lado que quero?
#   s09-s10: telhado (triângulo com base 8 e subida x), 37° na base.
#   s11-s12: 8 m desenhado na parede em vermelho; seta mostrando que 8 é a distância no chão.
#   s15-s18: pipa com linha esticada até o chão, altura 12, 37° no chão; 7,2 riscado em vermelho.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Achar um lado com seno, cosseno ou tangente"

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
    dict(id="s01", block="gancho", text="{a}Uma escada de dez metros está apoiada numa parede, [p=0.2] fazendo {b}trinta e sete graus com o chão. [p=0.3] {c}A que altura ela toca a parede? [p=0.3] Pitágoras não resolve: {d}você só conhece um lado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você escolhe a razão certa [p=0.2] e acha {b}o lado que falta, com um ângulo e um lado, [p=0.2] e ainda leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}seno, cosseno e tangente, as divisões entre os lados do triângulo retângulo; [p=0.2] e {c}resolver equação com decimal, como zero vírgula seis igual a xis dividido por dez. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s04", block="metodo", text="O segredo é {a}escolher a razão certa. [p=0.2] Para isso, faça três perguntas. [p=0.2] {b}Qual é o ângulo? [p=0.2] {c}Que lado eu conheço? [p=0.2] {d}Que lado eu quero?"),
    dict(id="s05", block="metodo", text="Na escada: {a}o ângulo é o de trinta e sete graus, no chão. [p=0.2] {b}A escada fica de frente para o ângulo reto: é a hipotenusa, e mede dez. [p=0.2] {c}A altura fica de frente para os trinta e sete graus: é o cateto oposto."),
    dict(id="s06", block="metodo", text="{a}Oposto e hipotenusa. [p=0.2] Que razão junta esses lados? [p=0.2] {b}O seno: oposto dividido pela hipotenusa. [p=0.3] Trinta e sete graus não tem um valor que você saiba de cabeça, [p=0.2] então {c}a prova dá o valor. [p=0.2] Aqui, {d}o seno de trinta e sete graus é cerca de zero vírgula seis."),
    dict(id="s07", block="metodo", text="Monte a igualdade: {a}zero vírgula seis igual a xis dividido por dez. [p=0.2] {b}Multiplique cada lado por dez. [p=0.2] {c}Xis igual a zero vírgula seis vezes dez, que dá seis. [p=0.3] A escada toca a parede a {d}seis metros de altura."),
    dict(id="s08", block="metodo", text="E a distância do pé da escada até a parede? [p=0.2] {a}Adjacente e hipotenusa: cosseno. [p=0.2] O cosseno de trinta e sete é cerca de {b}zero vírgula oito. [p=0.2] {c}Zero vírgula oito vezes dez dá oito metros. [p=0.3] Seis, [p=0.1] oito e dez: {d}o triângulo de lados três, [p=0.1] quatro e cinco, dobrado. [p=0.2] Esse triângulo tem um ângulo de quase trinta e sete graus. [p=0.2] Por isso a prova usa trinta e sete graus com esses valores redondos."),
    # tangente
    dict(id="s09", block="tangente", text="E quando a hipotenusa não entra? [p=0.2] Um telhado sobe com {a}trinta e sete graus [p=0.2] e avança {b}oito metros na horizontal. [p=0.2] {c}Quanto ele sobe? [p=0.3] {d}Oposto e adjacente: tangente."),
    dict(id="s10", block="tangente", text="A tangente de trinta e sete é cerca de {a}zero vírgula setenta e cinco. [p=0.2] {b}Zero vírgula setenta e cinco igual a xis dividido por oito. [p=0.2] {c}Xis igual a zero vírgula setenta e cinco vezes oito, que dá seis metros."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}escolher a razão pela posição no desenho. [p=0.2] Na escada, o ângulo está embaixo, no chão, [p=0.2] e a pessoa pensa: {b}embaixo, cosseno. [p=0.2] {c}Zero vírgula oito vezes dez dá oito, [p=0.2] e ela responde {d}oito metros de altura."),
    dict(id="s12", block="erro", text="Mas oito é {a}a distância no chão. [p=0.2] Quem decide a razão não é a posição: [p=0.2] é {b}qual lado fica de frente para o ângulo. [p=0.2] {c}A altura está de frente para os trinta e sete graus: oposto, então seno."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, quando você conhece a hipotenusa: [p=0.2] {a}o oposto é a hipotenusa vezes o seno. [p=0.2] {b}O adjacente é a hipotenusa vezes o cosseno. [p=0.2] Sem montar equação: {c}dez vezes zero vírgula seis dá seis."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o seno é o oposto dividido pela hipotenusa: [p=0.2] a hipotenusa passa para o outro lado multiplicando. [p=0.3] {b}Não compensa quando o lado que falta é a própria hipotenusa. [p=0.2] Aí, ela fica embaixo, e {c}você divide."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma pipa está a {a}doze metros de altura. [p=0.2] A linha, presa no chão e esticada, faz {b}trinta e sete graus com o chão. [p=0.2] Use o valor que a prova daria: {c}seno de trinta e sete graus, cerca de zero vírgula seis. [p=0.3] {d}Qual o comprimento da linha?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}A linha é a hipotenusa. [p=0.2] {b}A altura está de frente para o ângulo: é o oposto. [p=0.2] Oposto e hipotenusa: {c}seno. [p=0.3] {d}Zero vírgula seis igual a doze dividido por xis."),
    dict(id="s18", block="resposta", text="{a}Multiplique cada lado por xis: zero vírgula seis xis igual a doze. [p=0.2] {b}Multiplique por dez para tirar a vírgula: seis xis igual a cento e vinte. [p=0.2] {c}Dividindo por seis, xis igual a vinte. [p=0.3] {d}A linha mede vinte metros, [p=0.2] e faz sentido: {e}a hipotenusa é maior que a altura."),
    dict(id="s19", block="resposta", text="Quem multiplicou {a}doze por zero vírgula seis achou sete vírgula dois, [p=0.2] uma linha {b}mais curta que a altura da pipa. [p=0.2] Impossível: {c}com a hipotenusa procurada, divida."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}ângulo, lado conhecido e lado procurado. [p=0.2] {b}Os lados escolhem a razão. [p=0.2] {c}Monte a igualdade e resolva."),
    dict(id="s21", block="fim", text="Na próxima aula, você monta de cabeça {a}a tabela dos ângulos que mais caem em prova: [p=0.2] trinta graus, [p=0.2] quarenta e cinco graus [p=0.2] e sessenta graus. [p=0.3] E descobre {b}de onde ela vem: do quadrado e do triângulo equilátero. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
