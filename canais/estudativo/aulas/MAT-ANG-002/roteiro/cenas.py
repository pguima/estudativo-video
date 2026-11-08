# Estudativo · MAT-ANG-002 — Ângulos complementares, suplementares e opostos pelo vértice (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: achar o complemento de 35° (55°) e o suplemento de 110° (70°) e resolver 3x − 10 = x + 30 em ângulos opostos pelo vértice.
# Pré-requisitos: MAT-ANG-001 (graus, reto, raso), MAT-EQU-009 (equação com parênteses, letra dos dois lados). Próxima: MAT-ANG-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Visual: canto de folha dividido por um risco (E.angulo), linha reta com semirreta, duas retas cruzadas com os quatro ângulos.

TITULO = "Ângulos complementares, suplementares e opostos pelo vértice"

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
    dict(id="s01", block="gancho", text="{a}Qual é o complemento de trinta e cinco graus? [p=0.3] Se você respondeu {b}cento e quarenta e cinco, [p=0.2] trocou duas palavras que caem muito em prova: [p=0.2] {c}complemento e suplemento."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você não confunde mais essas palavras, [p=0.2] {b}acha ângulos escondidos onde duas retas se cruzam [p=0.2] e ainda leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}saber que o ângulo reto mede noventa graus e o raso, a linha reta, mede cento e oitenta, [p=0.2] e {c}resolver equação com xis dos dois lados. [p=0.3] Se faltar alguma, procure no canal."),
    # complementares
    dict(id="s04", block="complemento", text="Pegue {a}o canto de uma folha: noventa graus. [p=0.2] {b}Risque uma linha saindo do canto. [p=0.3] O canto virou {c}dois ângulos, [p=0.2] e juntos eles ainda fazem noventa."),
    dict(id="s05", block="complemento", text="Ângulos que somam noventa graus são {a}complementares. [p=0.2] Um é {b}o complemento do outro: [p=0.2] o que falta para completar o reto."),
    dict(id="s06", block="complemento", text="Complemento de trinta e cinco: [p=0.2] {a}noventa menos trinta e cinco dá {b}cinquenta e cinco graus. [p=0.3] Conferindo: {c}trinta e cinco mais cinquenta e cinco dá noventa."),
    # suplementares
    dict(id="s07", block="suplemento", text="Agora pegue {a}uma linha reta: cento e oitenta graus, o ângulo raso. [p=0.2] {b}Risque uma linha saindo de um ponto dela. [p=0.3] Os ângulos que ficam lado a lado {c}somam cento e oitenta."),
    dict(id="s08", block="suplemento", text="Ângulos que somam cento e oitenta graus são {a}suplementares. [p=0.2] Suplemento de cento e dez: [p=0.2] {b}cento e oitenta menos cento e dez dá {c}setenta graus."),
    # opostos pelo vértice
    dict(id="s09", block="opostos", text="Veja {a}duas retas que se cruzam, como uma tesoura aberta. [p=0.2] Elas formam {b}quatro ângulos em volta do vértice, o ponto do cruzamento."),
    dict(id="s10", block="opostos", text="Os ângulos que ficam {a}de frente um para o outro se chamam opostos pelo vértice. [p=0.3] E eles {b}têm sempre a mesma medida."),
    dict(id="s11", block="opostos", text="Por quê? [p=0.2] Digamos que um deles mede {a}cinquenta graus. [p=0.2] O vizinho forma com ele uma linha reta: [p=0.2] {b}cento e oitenta menos cinquenta dá cento e trinta. [p=0.3] E o oposto forma uma linha reta com esse vizinho: [p=0.2] {c}cento e oitenta menos cento e trinta dá cinquenta de novo. [p=0.3] Com qualquer medida é assim: [p=0.2] os ângulos de frente completam a linha reta com o mesmo vizinho."),
    dict(id="s12", block="opostos", text="A regra da tesoura: [p=0.2] {a}de frente, iguais. [p=0.2] {b}Lado a lado, somam cento e oitenta."),
    # com equação
    dict(id="s13", block="equacao", text="Com letra, a ideia é a mesma. [p=0.2] Dois ângulos opostos pelo vértice medem {a}três xis menos dez [p=0.2] e {b}xis mais trinta. [p=0.3] Opostos são iguais, então: [p=0.2] {c}três xis menos dez igual a xis mais trinta."),
    dict(id="s14", block="equacao", text="{a}Tire xis de cada lado: [p=0.2] {b}dois xis menos dez igual a trinta. [p=0.2] {c}Some dez de cada lado: [p=0.2] {d}dois xis igual a quarenta. [p=0.2] {e}Divida por dois: xis igual a vinte."),
    dict(id="s15", block="equacao", text="Mas xis não é o ângulo. [p=0.2] {a}Três vezes vinte dá sessenta, menos dez dá cinquenta graus. [p=0.2] {b}Vinte mais trinta dá cinquenta. [p=0.3] {c}Cada ângulo mede cinquenta graus. [p=0.2] Bateu."),
    # erro
    dict(id="s16", block="erro", text="Voltando ao erro do começo. [p=0.2] Quem troca as palavras faz {a}cento e oitenta menos trinta e cinco [p=0.2] e responde {b}cento e quarenta e cinco. [p=0.3] Mas o complemento completa {c}o reto, de noventa."),
    dict(id="s17", block="erro", text="Para não trocar: {a}cê vem antes de ésse no alfabeto, [p=0.2] e {b}noventa vem antes de cento e oitenta. [p=0.3] {c}Complemento, noventa. [p=0.2] {d}Suplemento, cento e oitenta."),
    # atalho
    dict(id="s18", block="atalho", text="E o atalho prometido: [p=0.2] {a}para ângulo agudo, o suplemento é o complemento mais noventa. [p=0.3] Complemento de trinta e cinco: cinquenta e cinco. [p=0.2] {b}Suplemento: cinquenta e cinco mais noventa dá {c}cento e quarenta e cinco."),
    dict(id="s19", block="atalho", text="Funciona porque {a}cento e oitenta é noventa mais noventa. [p=0.3] {b}Não serve para ângulo de noventa graus ou mais, [p=0.2] porque ele não tem complemento. [p=0.2] Aí, faça {c}cento e oitenta menos o ângulo, direto."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Duas retas se cruzam. [p=0.2] Dois ângulos {a}lado a lado medem xis mais quarenta [p=0.2] e {b}dois xis mais vinte. [p=0.3] {c}Quanto mede cada um?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] Lado a lado, {a}somam cento e oitenta: [p=0.2] {b}xis mais quarenta mais dois xis mais vinte igual a cento e oitenta. [p=0.3] {c}Juntando: três xis mais sessenta igual a cento e oitenta. [p=0.2] {d}Tire sessenta: três xis igual a cento e vinte. [p=0.2] {e}Divida por três: xis igual a quarenta."),
    dict(id="s23", block="resposta", text="Os ângulos: {a}quarenta mais quarenta dá oitenta graus. [p=0.2] {b}Duas vezes quarenta mais vinte dá cem graus. [p=0.3] Conferindo: {c}oitenta mais cem dá cento e oitenta. [p=0.2] Bateu. [p=0.3] Quem iguala as expressões, como se fossem opostos, chega em {d}ângulos de sessenta graus, [p=0.2] que não fecham a linha reta."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}complementares somam noventa, [p=0.2] {b}suplementares somam cento e oitenta, [p=0.2] e {c}opostos pelo vértice são iguais."),
    dict(id="s25", block="fim", text="Na próxima aula, aparecem {a}retas que nunca se cruzam, as paralelas, [p=0.2] cortadas por uma terceira reta. [p=0.2] E você descobre {b}quais dos oito ângulos que surgem são iguais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
