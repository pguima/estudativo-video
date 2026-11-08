# Estudativo · MAT-FUN-020 — Montar a função para otimizar (Matemática · Funções · Função quadrática).
# Habilidade: achar o preço que dá a maior receita quando cada R$ 1 de desconto vende 10 ingressos a mais.
# Pré-requisitos: MAT-FUN-019 (máximo e mínimo; xis responde quando/quanto usar, ípsilon responde o valor). Próxima: MAT-FUN-021.
# Questão inédita, criada para esta aula. Valores do show inventados. Receita e área do retângulo explicadas na hora.
# Show: preço 40, público 300, x = reais de desconto · preço 40 − x · vendidos 300 + 10x · R(x) = (40 − x)(300 + 10x)
#   = 12000 + 400x − 300x − 10x² = −10x² + 100x + 12000 · xv = −100/(−20) = 5 · preço 35 · 350 ingressos · R = 12250 (sem desconto: 12000).
# Erro: responder 5 reais (o desconto) quando a pergunta é o preço.
# Atalho: zeros dos fatores (x = 40 e x = −30), média (40 − 30)/2 = 5, sem abrir os parênteses · não compensa fora da forma de produto (L(x) da MAT-FUN-019).
# Questão: 40 m de tela, canteiro encostado no muro · A(x) = x(40 − 2x) · zeros 0 e 20 · xv = 10 · frente 20 m · A = 200 m².
# Visual: quadro "preço × quantidade" com as duas colunas ganhando xis; E.plano com E.curva de −10x² + 100x + 12000 (de −30 a 40, escala
#   em milhares) e E.ponto nos zeros −30 e 40 e no vértice (5, 12250); desenho do canteiro com muro, lados x, x e 40 − 2x;
#   parábola de x(40 − 2x) com zeros 0 e 20 e vértice (10, 200).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á"; R se fala "erre".

TITULO = "Montar a função para otimizar"

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
    dict(id="s01", block="gancho", text="Um show cobra {a}quarenta reais o ingresso e vende trezentos ingressos. [p=0.2] O dono descobre que {b}cada real de desconto vende dez ingressos a mais. [p=0.3] {c}Baixar o preço pode encher o caixa? [p=0.2] Pode, mas {d}só até certo ponto."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você transforma uma história numa função quadrática, [p=0.2] acha {b}o melhor valor [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}O vértice dá o máximo ou o mínimo: [p=0.2] o xis responde quanto usar, e o ípsilon responde o valor. [p=0.3] E {c}o chuveirinho, para abrir parênteses: cada termo de um multiplica cada termo do outro. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s04", block="metodo", text="O método tem {a}quatro passos. [p=0.2] {b}Passo um: escolha o que varia e chame de xis. [p=0.2] Aqui, xis é {c}quantos reais de desconto."),
    dict(id="s05", block="metodo", text="{a}Passo dois: escreva cada parte com xis. [p=0.2] {b}O preço fica quarenta menos xis. [p=0.2] {c}Os ingressos vendidos ficam trezentos mais dez xis: [p=0.2] dez a mais para cada real de desconto."),
    dict(id="s06", block="metodo", text="{a}Passo três: monte a função. [p=0.2] O dinheiro que entra se chama {b}receita, [p=0.2] e é o preço vezes a quantidade vendida. [p=0.3] {c}Erre de xis igual ao parêntese quarenta menos xis, vezes o parêntese trezentos mais dez xis."),
    dict(id="s07", block="metodo", text="Pelo chuveirinho: {a}quarenta vezes trezentos dá doze mil. [p=0.2] {b}Quarenta vezes dez xis dá quatrocentos xis. [p=0.2] {c}Menos xis vezes trezentos dá menos trezentos xis. [p=0.2] {d}Menos xis vezes dez xis dá menos dez xis ao quadrado. [p=0.3] Juntando: {e}menos dez xis ao quadrado, mais cem xis, mais doze mil."),
    dict(id="s08", block="metodo", text="{a}Passo quatro: o vértice. [p=0.2] Á vale menos dez, negativo: {b}tem máximo. [p=0.2] {c}Xis do vértice: menos cem dividido por menos vinte dá cinco. [p=0.3] O melhor desconto é de {d}cinco reais."),
    # resposta do show
    dict(id="s09", block="show", text="Falta responder o que foi pedido: {a}o preço. [p=0.2] {b}Quarenta menos cinco dá trinta e cinco reais. [p=0.2] Vendem {c}trezentos e cinquenta ingressos, [p=0.2] e a receita é {d}trinta e cinco vezes trezentos e cinquenta: doze mil duzentos e cinquenta reais. [p=0.3] Sem desconto, era {e}doze mil. [p=0.2] O desconto rendeu mais duzentos e cinquenta reais."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}responder cinco reais. [p=0.2] Cinco é {b}o desconto, porque foi isso que você chamou de xis. [p=0.2] A pergunta é {c}o preço: trinta e cinco reais. [p=0.3] {d}Anote ao lado do xis o que ele significa, [p=0.2] e volte nessa anotação antes de responder."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: {a}não abra os parênteses. [p=0.2] A receita é zero quando {b}algum parêntese vale zero. [p=0.2] {c}Quarenta menos xis zera em xis igual a quarenta: ingresso de graça. [p=0.2] {d}Trezentos mais dez xis zera em xis igual a menos trinta."),
    dict(id="s12", block="atalho", text="O vértice fica {a}no meio dessas raízes. [p=0.2] {b}Some as raízes: quarenta menos trinta dá dez. [p=0.2] {c}Divida por dois: cinco. [p=0.2] O mesmo desconto, sem chuveirinho."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a parábola é simétrica, e o vértice fica no meio das raízes. [p=0.2] O menos trinta não precisa fazer sentido na história: {b}é só um número da conta. [p=0.3] {c}Não compensa quando a função não vem como produto de dois parênteses, [p=0.2] como o lucro da aula passada. [p=0.2] Aí, vá de {d}menos bê dividido por dois á."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Você tem {a}quarenta metros de tela para cercar um canteiro retangular encostado num muro. [p=0.2] {b}O muro faz um dos lados, e a tela faz os outros três. [p=0.3] A área do retângulo é {c}comprimento vezes largura. [p=0.2] {d}Quais medidas dão a maior área? [p=0.2] {e}E qual é essa área?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Xis é cada lado que sai do muro. [p=0.2] São dois lados assim, então sobra {b}quarenta menos dois xis para o lado da frente. [p=0.3] Área: {c}xis, vezes o parêntese quarenta menos dois xis."),
    dict(id="s17", block="resposta", text="Pelo atalho: {a}o fator xis zera em xis igual a zero, [p=0.2] e {b}quarenta menos dois xis zera em vinte. [p=0.2] O meio é {c}dez. [p=0.3] Os lados que saem do muro medem {d}dez metros, a frente mede {e}vinte metros, [p=0.2] e a área é {f}duzentos metros quadrados."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}chame de xis o que varia, [p=0.2] {b}monte a função com a história, [p=0.2] {c}ache o vértice [p=0.2] e {d}responda o que foi perguntado."),
    dict(id="s19", block="fim", text="Na próxima aula, o caminho de volta: [p=0.2] você recebe {a}uma parábola com as raízes e mais um ponto [p=0.2] e {b}descobre a lei dela. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
