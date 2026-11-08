# Estudativo · MAT-ANA-008 — Equação reduzida da circunferência (Matemática · Geometria Analítica).
# Habilidade: ler em (x − 2)² + (y + 1)² = 9 o centro (2, −1) e o raio 3 e escrever a equação a partir do centro e do raio.
# Pré-requisitos: MAT-ANA-001 (distância entre dois pontos), MAT-POL-004 (circunferência e raio). Próxima: MAT-ANA-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Visual: plano cartesiano com circunferência (centro na origem e raio 5; centro (2, −1) e raio 3), triângulo retângulo do centro ao ponto.

TITULO = "Equação reduzida da circunferência: centro e raio"

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
    dict(id="s01", block="gancho", text="{a}Xis menos dois, ao quadrado, mais ípsilon mais um, ao quadrado, igual a nove. [p=0.3] Parece só uma conta. [p=0.2] Mas é {b}um desenho: uma circunferência. [p=0.3] E dá para ler {c}o centro e o raio dela em cinco segundos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê o centro e o raio numa equação assim, [p=0.2] {b}escreve a equação a partir deles [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}na circunferência, todos os pontos ficam à mesma distância do centro, e essa distância é o raio; [p=0.2] e {c}a distância entre dois pontos sai de um triângulo retângulo, com Pitágoras. [p=0.3] Se faltar alguma, procure no canal."),
    # centro na origem
    dict(id="s04", block="origem", text="Comece pelo caso mais simples: {a}centro na origem, raio cinco. [p=0.2] Pegue {b}o ponto xis três, ípsilon quatro. [p=0.3] Do centro até ele, os catetos são {c}três e quatro. [p=0.2] {d}Três ao quadrado mais quatro ao quadrado dá vinte e cinco, [p=0.2] que é {e}cinco ao quadrado. [p=0.2] O ponto está a cinco do centro: fica na circunferência."),
    dict(id="s05", block="origem", text="Vale para qualquer ponto xis, ípsilon da circunferência: [p=0.2] os catetos são {a}o próprio xis e o próprio ípsilon, [p=0.2] e a hipotenusa é {b}o raio. [p=0.3] Coordenada negativa também serve: {c}o quadrado apaga o sinal. [p=0.3] Então, {d}xis ao quadrado mais ípsilon ao quadrado igual a vinte e cinco. [p=0.2] Essa é {e}a equação da circunferência: a regra que todos os pontos dela cumprem."),
    # centro fora da origem
    dict(id="s06", block="centro", text="E se o centro sai da origem? [p=0.2] {a}Centro xis dois, ípsilon menos um, raio três. [p=0.3] Para um ponto xis, ípsilon, o cateto deitado é {b}a diferença dos xis: xis menos dois. [p=0.2] O cateto em pé é {c}a diferença dos ípsilons: ípsilon menos, abre parênteses, menos um, fecha parênteses, [p=0.2] que vira {d}ípsilon mais um."),
    dict(id="s07", block="centro", text="Pitágoras de novo: {a}xis menos dois, ao quadrado, mais ípsilon mais um, ao quadrado, igual a três ao quadrado, [p=0.2] que dá {b}nove. [p=0.3] É a equação do começo da aula."),
    dict(id="s08", block="centro", text="Confira com {a}o ponto xis cinco, ípsilon menos um, três passos à direita do centro. [p=0.2] {b}Cinco menos dois dá três, e três ao quadrado dá nove. [p=0.2] {c}Menos um mais um dá zero. [p=0.2] {d}Nove mais zero dá nove. [p=0.2] Bateu: o ponto está na circunferência."),
    # regra
    dict(id="s09", block="regra", text="A regra geral: [p=0.2] {a}xis menos á, ao quadrado, mais ípsilon menos bê, ao quadrado, igual a érre ao quadrado. [p=0.3] {b}Á e bê são as coordenadas do centro. [p=0.2] {c}Érre é o raio. [p=0.2] Essa forma se chama {d}equação reduzida."),
    dict(id="s10", block="ler", text="Para ler, olhe {a}o sinal dentro de cada parêntese. [p=0.2] {b}Xis menos dois: o xis do centro é dois. [p=0.2] {c}Ípsilon mais um é o mesmo que ípsilon menos, abre parênteses, menos um, fecha parênteses: o ípsilon do centro é menos um. [p=0.3] {d}O centro tem o sinal contrário ao que aparece. [p=0.2] E o raio: {e}a raiz de nove dá três."),
    dict(id="s11", block="escrever", text="Agora o caminho de volta: {a}centro xis menos três, ípsilon quatro, raio cinco. [p=0.2] {b}Xis menos, abre parênteses, menos três, fecha parênteses, vira xis mais três. [p=0.2] {c}Ípsilon menos quatro fica como está. [p=0.2] E {d}cinco ao quadrado dá vinte e cinco. [p=0.3] {e}Xis mais três, ao quadrado, mais ípsilon menos quatro, ao quadrado, igual a vinte e cinco."),
    dict(id="s12", block="escrever", text="E se o número da direita não for um quadrado perfeito? [p=0.2] Em {a}xis menos um, ao quadrado, mais ípsilon ao quadrado, igual a sete, [p=0.2] o raio é {b}a raiz de sete. [p=0.3] E o ípsilon sem parêntese é {c}ípsilon menos zero: [p=0.2] o centro é {d}xis um, ípsilon zero."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}dizer que o raio do começo é nove. [p=0.2] Nove é {b}o raio ao quadrado. [p=0.3] Com raio nove, a circunferência passaria por {c}xis onze, ípsilon menos um. [p=0.2] Teste esse ponto: {d}onze menos dois dá nove, e nove ao quadrado dá oitenta e um. [p=0.2] Oitenta e um {e}não é nove: o ponto não cumpre a equação. [p=0.2] {f}O raio é a raiz: três."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho para o centro: [p=0.2] {a}pergunte que número zera cada parêntese. [p=0.3] {b}Xis menos dois zera com dois. [p=0.2] {c}Ípsilon mais um zera com menos um. [p=0.2] Centro: {d}xis dois, ípsilon menos um. [p=0.2] Sem se preocupar com sinal trocado."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o centro está a distância zero dele mesmo: [p=0.2] ali, os dois catetos somem. [p=0.3] {b}Não compensa quando a equação vem com os parênteses já abertos, [p=0.2] sem parêntese para zerar. [p=0.2] {c}Esse caso fica para a próxima aula."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Xis mais um, ao quadrado, mais ípsilon menos cinco, ao quadrado, igual a dezesseis. [p=0.2] {b}Qual é o centro, e qual é o raio? [p=0.3] Depois, {c}escreva a equação da circunferência de centro xis quatro, ípsilon zero, e raio seis."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Xis mais um zera com menos um. [p=0.2] {b}Ípsilon menos cinco zera com cinco. [p=0.2] Centro: {c}xis menos um, ípsilon cinco. [p=0.2] Raio: {d}a raiz de dezesseis dá quatro."),
    dict(id="s19", block="resposta", text="Na segunda parte, o xis do centro é quatro: {a}xis menos quatro, ao quadrado. [p=0.2] O ípsilon do centro é zero: {b}ípsilon menos zero é só ípsilon, ao quadrado. [p=0.2] {c}Seis ao quadrado dá trinta e seis. [p=0.3] Fica {d}xis menos quatro, ao quadrado, mais ípsilon ao quadrado, igual a trinta e seis."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}o centro é o que zera os parênteses, [p=0.2] e {b}o raio é a raiz do número da direita."),
    dict(id="s21", block="fim", text="Na próxima aula, a equação vem {a}com os parênteses abertos, [p=0.2] como {b}xis ao quadrado mais ípsilon ao quadrado menos quatro xis mais dois ípsilon menos quatro igual a zero, [p=0.2] e você {c}completa quadrados para achar o centro e o raio. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
