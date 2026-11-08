# Estudativo · MAT-ANA-010 — Posições relativas: ponto, reta e circunferência (Matemática · Geometria Analítica).
# Habilidade: dizer se um ponto é interno, externo ou está na circunferência e se uma reta é secante, tangente ou externa, substituindo a reta na equação e olhando o discriminante.
# Pré-requisitos: MAT-ANA-006 (encontro de retas por sistema), MAT-ANA-009 (centro e raio), MAT-FAT-009 (discriminante), MAT-POL-007 (tangente e secante). Próxima: MAT-ANA-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Visual: plano com a circunferência de centro (2, −1) e raio 3 e três pontos; depois x² + y² = 25 com as retas y = x + 1, y = 5 e y = x + 10.

TITULO = "Ponto e reta diante da circunferência: dentro, fora, secante ou tangente"

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
    dict(id="s01", block="gancho", text="{a}Uma reta e uma circunferência. [p=0.2] Elas se cortam, {b}só se encostam [p=0.2] ou {c}nem se tocam? [p=0.3] Sem desenho nenhum, {d}uma conta responde: [p=0.2] o mesmo delta da equação do segundo grau."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você diz onde um ponto fica [p=0.2] e {b}o que uma reta faz com a circunferência, [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}ler o centro e o raio na equação da circunferência; [p=0.2] {c}o encontro de duas linhas é a solução do sistema, pela substituição; [p=0.2] e {d}o delta, bê ao quadrado menos quatro vezes á vezes cê, que conta as raízes. [p=0.3] Se faltar alguma, procure no canal."),
    # ponto
    dict(id="s04", block="ponto", text="Comece pelo ponto. [p=0.2] Use a circunferência {a}xis menos dois, ao quadrado, mais ípsilon mais um, ao quadrado, igual a nove: [p=0.2] {b}centro xis dois, ípsilon menos um, e raio três. [p=0.3] O lado esquerdo é {c}a distância até o centro, ao quadrado. [p=0.2] Então basta {d}trocar o ponto na equação e comparar com nove."),
    dict(id="s05", block="ponto", text="{a}Xis cinco, ípsilon menos um: [p=0.2] {b}três ao quadrado mais zero ao quadrado dá nove. [p=0.2] Igual a nove: {c}o ponto está na circunferência. [p=0.3] {d}Xis seis, ípsilon dois: [p=0.2] {e}quatro ao quadrado mais três ao quadrado dá vinte e cinco. [p=0.2] Mais que nove: {f}ponto externo, do lado de fora."),
    dict(id="s06", block="ponto", text="{a}Xis quatro, ípsilon um: [p=0.2] {b}dois ao quadrado mais dois ao quadrado dá oito. [p=0.2] Menos que nove: {c}ponto interno, do lado de dentro. [p=0.3] A regra: {d}menor que érre ao quadrado, dentro. [p=0.2] {e}Igual, em cima. [p=0.2] {f}Maior, fora."),
    # reta: secante
    dict(id="s07", block="reta", text="Agora, a reta. [p=0.2] Pegue uma circunferência mais simples: {a}xis ao quadrado mais ípsilon ao quadrado igual a vinte e cinco, [p=0.2] com centro na origem e raio cinco. [p=0.3] E a reta {b}ípsilon igual a xis mais um. [p=0.2] Um ponto de encontro cumpre {c}as duas equações ao mesmo tempo: é um sistema."),
    dict(id="s08", block="reta", text="Pela substituição, {a}troque o ípsilon por xis mais um: [p=0.2] {b}xis ao quadrado mais xis mais um, ao quadrado, igual a vinte e cinco. [p=0.3] Xis mais um, ao quadrado, dá xis ao quadrado mais dois xis mais um. [p=0.2] Juntando os termos: [p=0.2] {c}dois xis ao quadrado mais dois xis mais um igual a vinte e cinco. [p=0.2] Tirando vinte e cinco dos dois lados e dividindo tudo por dois: [p=0.2] {d}xis ao quadrado mais xis menos doze igual a zero."),
    dict(id="s09", block="reta", text="Cada raiz dessa equação é {a}um ponto de encontro. [p=0.2] Então {b}o delta conta os pontos. [p=0.3] Atenção: aqui, á, bê e cê são os números da equação do segundo grau, e não o centro. [p=0.2] {c}Á vale um, bê vale um e cê vale menos doze. [p=0.3] {d}Bê ao quadrado: um ao quadrado dá um. [p=0.2] {e}Quatro vezes um vezes menos doze dá menos quarenta e oito. [p=0.2] Tirar menos quarenta e oito é somar: [p=0.2] {f}um mais quarenta e oito dá quarenta e nove. [p=0.2] Delta positivo."),
    dict(id="s10", block="reta", text="Delta positivo, {a}duas raízes: dois pontos de encontro. [p=0.2] A reta entra e sai: {b}é secante. [p=0.3] As raízes são {c}três e menos quatro, [p=0.2] e os pontos são {d}xis três, ípsilon quatro, [p=0.2] e {e}xis menos quatro, ípsilon menos três."),
    # tangente e externa
    dict(id="s11", block="outras", text="Troque de reta: {a}ípsilon igual a cinco. [p=0.2] Fica {b}xis ao quadrado mais vinte e cinco igual a vinte e cinco: [p=0.2] {c}xis ao quadrado igual a zero. [p=0.2] Aqui, bê e cê valem zero, e {d}o delta dá zero: um ponto só. [p=0.2] A reta só encosta: {e}é tangente, no ponto xis zero, ípsilon cinco."),
    dict(id="s12", block="outras", text="E {a}a reta ípsilon igual a xis mais dez. [p=0.2] Substituindo, abrindo o quadrado e tirando vinte e cinco dos dois lados, fica {b}dois xis ao quadrado mais vinte xis mais setenta e cinco igual a zero. [p=0.2] Á vale dois, bê vale vinte e cê vale setenta e cinco. [p=0.2] {c}Bê ao quadrado dá quatrocentos. [p=0.2] {d}Quatro vezes dois vezes setenta e cinco dá seiscentos. [p=0.2] {e}Quatrocentos menos seiscentos dá menos duzentos. [p=0.2] {f}Delta negativo: nenhum ponto de encontro. [p=0.2] A reta passa longe: {g}é externa."),
    dict(id="s13", block="outras", text="A regra da reta: [p=0.2] {a}delta positivo, secante. [p=0.2] {b}Delta zero, tangente. [p=0.2] {c}Delta negativo, externa."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}comparar com o raio, e não com o raio ao quadrado. [p=0.2] No ponto xis quatro, ípsilon um, a conta deu {b}oito. [p=0.2] Quem compara com o raio, três, vê {c}oito maior que três, e diz que o ponto está fora. [p=0.3] Mas oito é {d}a distância ao quadrado. [p=0.2] Compare {e}quadrado com quadrado: oito é menor que nove, e o ponto está dentro."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho, para {a}reta deitada ou em pé. [p=0.2] Nelas, a distância do centro até a reta {b}se lê direto no plano. [p=0.3] Da origem até {c}ípsilon igual a cinco são cinco passos para cima. [p=0.2] {d}Cinco é o raio: tangente, sem conta nenhuma."),
    dict(id="s16", block="atalho", text="Funciona porque {a}a distância até uma reta deitada é a diferença dos ípsilons, [p=0.2] e até uma reta em pé, a diferença dos xis. [p=0.2] E, na aula de tangente e corda, você viu que {b}distância igual ao raio é tangente, menor é secante e maior é externa. [p=0.3] {c}Não compensa com reta inclinada, como ípsilon igual a xis mais um: [p=0.2] aí, {d}substituição e delta são o caminho seguro."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] A circunferência é {a}xis ao quadrado mais ípsilon ao quadrado igual a dez. [p=0.3] {b}O ponto xis três, ípsilon dois, está dentro, fora ou em cima dela? [p=0.2] E {c}a reta ípsilon igual a dez menos três xis é secante, tangente ou externa?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O ponto: {a}nove mais quatro dá treze. [p=0.2] {b}Treze é maior que dez: o ponto está fora. [p=0.3] A reta: troque o ípsilon, e fica {c}xis ao quadrado mais dez menos três xis, ao quadrado, igual a dez."),
    dict(id="s20", block="resposta", text="Abrindo o quadrado: {a}cem menos sessenta xis mais nove xis ao quadrado. [p=0.2] Juntando e tirando dez dos dois lados: {b}dez xis ao quadrado menos sessenta xis mais noventa igual a zero. [p=0.2] Dividindo tudo por dez: {c}xis ao quadrado menos seis xis mais nove igual a zero."),
    dict(id="s21", block="resposta", text="{a}Trinta e seis menos trinta e seis dá zero. [p=0.2] {b}Delta zero: a reta é tangente. [p=0.2] Ela encosta em {c}xis três, ípsilon um. [p=0.2] Conferindo: {d}nove mais um dá dez. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}para o ponto, compare com érre ao quadrado. [p=0.2] {b}Para a reta, substitua e olhe o sinal do delta."),
    dict(id="s23", block="fim", text="Na próxima aula, {a}é hora de praticar: [p=0.2] {b}centro e raio de equações diferentes [p=0.2] e {c}a posição de pontos e retas, em situações novas. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
