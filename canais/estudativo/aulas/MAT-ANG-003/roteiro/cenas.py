# Estudativo · MAT-ANG-003 — Retas paralelas cortadas por uma transversal (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: diferenciar retas paralelas, concorrentes e perpendiculares e achar x quando ângulos correspondentes ou alternos medem 2x + 10 e 70°.
# Pré-requisitos: MAT-ANG-002 (opostos pelo vértice, suplementares). Próxima: MAT-ANG-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Visual: três pares de retas (concorrentes, perpendiculares, paralelas) e E.paralelas com os oito ângulos, destacando correspondentes e o "Z" dos alternos internos.

TITULO = "Retas paralelas cortadas por uma transversal"

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
    dict(id="s01", block="gancho", text="{a}Duas retas paralelas, cortadas por uma terceira reta, [p=0.2] formam {b}oito ângulos. [p=0.3] Parece muita coisa para decorar. [p=0.3] Mas, no fundo, {c}só existem duas medidas ali."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reconhece retas paralelas, concorrentes e perpendiculares, [p=0.2] {b}acha qualquer um dos oito ângulos [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}ângulos opostos pelo vértice são iguais, [p=0.2] e {c}ângulos lado a lado, sobre uma linha reta, somam cento e oitenta graus. [p=0.3] Se faltar alguma, procure no canal."),
    # tipos de retas
    dict(id="s04", block="retas", text="Primeiro, as posições de duas retas no papel. [p=0.2] {a}Se elas se cruzam em um ponto, são concorrentes, [p=0.2] como {b}as ruas de uma esquina."),
    dict(id="s05", block="retas", text="{a}Se se cruzam formando quatro ângulos retos, são perpendiculares. [p=0.2] É um tipo especial de concorrente: [p=0.2] {b}o cruzamento em cruz, com o quadradinho no canto."),
    dict(id="s06", block="retas", text="{a}Se nunca se cruzam, por mais que você estique, são paralelas. [p=0.2] Como {b}os trilhos de um trem [p=0.2] ou {c}as linhas do caderno: [p=0.2] sempre à mesma distância."),
    # transversal
    dict(id="s07", block="transversal", text="Agora, {a}uma terceira reta corta as paralelas. [p=0.2] Ela se chama {b}transversal. [p=0.3] Em cada cruzamento, você já conhece a regra da tesoura: [p=0.2] {c}de frente, iguais; [p=0.2] lado a lado, somam cento e oitenta."),
    dict(id="s08", block="transversal", text="E aqui está o segredo. [p=0.2] As paralelas apontam na mesma direção, [p=0.2] então a transversal corta cada uma {a}com a mesma inclinação. [p=0.3] {b}O cruzamento de baixo é uma cópia do cruzamento de cima."),
    # correspondentes
    dict(id="s09", block="nomes", text="Ângulos na {a}mesma posição em cada cruzamento se chamam correspondentes. [p=0.2] Por exemplo, {b}o de cima à direita no cruzamento de cima, [p=0.2] e {c}o de cima à direita no cruzamento de baixo. [p=0.3] Como um cruzamento é cópia do outro, {d}correspondentes são iguais."),
    # alternos
    dict(id="s10", block="nomes", text="Olhe só para {a}a faixa entre as paralelas. [p=0.2] Pegue um ângulo de dentro, de um lado da transversal, [p=0.2] e {b}o de dentro do outro lado, no outro cruzamento. [p=0.3] São {c}alternos internos. [p=0.2] Eles desenham {d}um zê, e também são iguais."),
    # exemplo
    dict(id="s11", block="exemplo", text="Vamos usar. [p=0.2] Dois ângulos correspondentes medem {a}dois xis mais dez [p=0.2] e {b}setenta graus. [p=0.3] Correspondentes são iguais: [p=0.2] {c}dois xis mais dez igual a setenta."),
    dict(id="s12", block="exemplo", text="{a}Tire dez de cada lado: dois xis igual a sessenta. [p=0.2] {b}Divida por dois: xis igual a trinta. [p=0.3] Conferindo: {c}duas vezes trinta mais dez dá setenta. [p=0.2] Bateu. [p=0.3] Se fossem alternos internos, {d}a conta seria a mesma."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: {a}igualar um ângulo agudo com um obtuso. [p=0.3] Imagine que o ângulo de dois xis mais dez é agudo, [p=0.2] e que {b}o ângulo de cento e dez graus, no outro cruzamento, é obtuso."),
    dict(id="s14", block="erro", text="Quem iguala faz {a}dois xis mais dez igual a cento e dez [p=0.2] e chega em {b}xis igual a cinquenta. [p=0.3] Aí o ângulo de dois xis mais dez daria {c}cento e dez: [p=0.2] obtuso, quando a figura mostra um agudo."),
    dict(id="s15", block="erro", text="{a}Agudo com obtuso não se iguala: soma cento e oitenta. [p=0.2] {b}Dois xis mais dez mais cento e dez igual a cento e oitenta. [p=0.2] Daí, {c}xis igual a trinta, e o agudo mede setenta."),
    # atalho
    dict(id="s16", block="atalho", text="E o atalho prometido: [p=0.2] {a}esqueça os nomes. [p=0.2] Com paralelas, só existem {b}ângulos agudos, todos iguais, [p=0.2] e {c}ângulos obtusos, todos iguais. [p=0.3] {d}Agudo com agudo, iguala. [p=0.2] {e}Agudo com obtuso, soma cento e oitenta."),
    dict(id="s17", block="atalho", text="Funciona porque {a}cada cruzamento só tem duas medidas, [p=0.2] e o de baixo copia o de cima. [p=0.3] {b}Não vale se as retas não forem paralelas. [p=0.2] E, {c}se a transversal for perpendicular, todos os ângulos são retos."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Retas paralelas cortadas por uma transversal. [p=0.2] Dois ângulos alternos internos medem {a}três xis menos vinte [p=0.2] e {b}xis mais quarenta. [p=0.3] {c}Quanto vale xis, e quanto mede cada um desses ângulos?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Alternos internos são iguais: [p=0.2] {a}três xis menos vinte igual a xis mais quarenta. [p=0.2] {b}Tire xis de cada lado: dois xis menos vinte igual a quarenta. [p=0.2] {c}Some vinte: dois xis igual a sessenta. [p=0.2] {d}Xis igual a trinta."),
    dict(id="s21", block="resposta", text="Cada ângulo: {a}três vezes trinta dá noventa, menos vinte dá setenta graus. [p=0.2] {b}Trinta mais quarenta dá setenta. [p=0.2] Bateu. [p=0.3] E, pelo atalho, {c}os ângulos obtusos da figura medem cento e oitenta menos setenta, que dá cento e dez graus."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}paralelas nunca se cruzam, [p=0.2] {b}a transversal faz o mesmo cruzamento duas vezes, [p=0.2] e {c}agudo com agudo é igual; agudo com obtuso soma cento e oitenta."),
    dict(id="s23", block="fim", text="Na próxima aula, esses ângulos alternos {a}provam que os ângulos de qualquer triângulo somam cento e oitenta graus. [p=0.2] E você conhece {b}o ângulo externo do triângulo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
