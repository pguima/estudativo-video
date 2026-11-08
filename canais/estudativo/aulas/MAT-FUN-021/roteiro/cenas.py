# Estudativo · MAT-FUN-021 — Achar a lei da parábola (Matemática · Funções · Função quadrática).
# Habilidade: escrever a parábola de raízes 1 e 5 que passa por (0, 10) como y = 2(x − 1)(x − 5), passar para a forma desenvolvida e ler o vértice na forma y = a(x − h)² + k.
# Pré-requisitos: MAT-FAT-011 (cada raiz vira um parêntese), MAT-FUN-017 (raízes no gráfico). Próxima: MAT-FUN-022.
# Questão inédita, criada para esta aula. Vértice (MAT-FUN-018) fora da ficha: explicado na hora como o ponto onde a parábola faz a curva,
#   e lido pela forma a(x − h)² + k com o argumento "o quadrado nunca é negativo". Quadrado da diferença: MAT-FAT-001.
# Contas: y = a(x − 1)(x − 5) · (0, 10): 10 = a(−1)(−5) = 5a → a = 2 · 2(x² − 6x + 5) = 2x² − 12x + 10 ·
#   2(x − 3)² − 8 = 2(x² − 6x + 9) − 8 = 2x² − 12x + 10 · vértice (3, −8); 3 é o meio de 1 e 5.
# Sem o á: (x − 1)(x − 5) corta o eixo y em 5. Erro: ler o vértice como x = −3: 2(−6)² − 8 = 64, longe de ser o mais baixo.
# Atalho: a = c ÷ (produto das raízes) = 10 ÷ 5 = 2 · não vale com ponto fora do eixo y, como (6, 10): a·5·1 = 10.
# Questão: raízes −2 e 4, ponto (0, −16) · produto −8 · a = 2 · y = 2(x + 2)(x − 4) = 2x² − 4x − 16 ·
#   vértice de 2(x − 1)² − 18 = (1, −18) (é a mesma parábola: 2x² − 4x + 2 − 18).
# Visual: E.plano com E.curva de 2x² − 12x + 10 (x de 0 a 6), E.ponto em (1, 0), (5, 0), (0, 10) e no vértice (3, −8);
#   curva de (x − 1)(x − 5) tracejada passando por (0, 5); as três formas da lei empilhadas (fatorada, desenvolvida, do vértice).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á"; h e k se falam "agá" e "ká".

TITULO = "Achar a lei da parábola"

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
    dict(id="s01", block="gancho", text="{a}Uma parábola corta o eixo xis no um e no cinco, [p=0.2] e {b}corta o eixo ípsilon no dez. [p=0.3] {c}Qual é a lei dela? [p=0.2] Com esses três números, dá para escrever a função inteira."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você escreve a lei de uma parábola pelas raízes, [p=0.2] passa para a forma com á, bê e cê, [p=0.2] {b}lê o ponto de virada direto na lei [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}Raiz é onde a parábola corta o eixo xis. [p=0.2] E {c}cada raiz vira um parêntese, xis menos a raiz: [p=0.2] {d}xis ao quadrado mais cinco xis mais seis é xis mais dois, vezes xis mais três. [p=0.3] Se faltar alguma, procure no canal."),
    # forma fatorada
    dict(id="s04", block="fatorada", text="Raízes um e cinco. [p=0.2] O primeiro palpite é {a}ípsilon igual a xis menos um, vezes xis menos cinco. [p=0.2] Em xis igual a um, {b}o primeiro parêntese zera. [p=0.2] Em xis igual a cinco, {c}zera o segundo. [p=0.3] As raízes batem."),
    dict(id="s05", block="fatorada", text="Mas confira o corte no eixo ípsilon, onde {a}xis vale zero. [p=0.2] {b}Menos um vezes menos cinco: cinco. [p=0.2] O desenho pede {c}dez. [p=0.3] O palpite tem as raízes certas, mas {d}não passa pelo ponto do desenho."),
    dict(id="s06", block="fatorada", text="É que existem {a}infinitas parábolas com raízes um e cinco. [p=0.2] Todas cabem em {b}ípsilon igual a á, vezes xis menos um, vezes xis menos cinco. [p=0.3] O á pode virar a boca para baixo e deixar a parábola mais fechada ou mais aberta, {c}mas não mexe nas raízes: [p=0.2] á vezes zero continua zero."),
    dict(id="s07", block="fatorada", text="Essa é a {a}forma fatorada: [p=0.2] {b}o á, vezes um parêntese para cada raiz. [p=0.3] Quem escolhe o á é {c}o ponto que sobrou. [p=0.2] Troque {d}xis zero, ípsilon dez: [p=0.2] {e}dez igual a á, vezes menos um, vezes menos cinco. [p=0.2] {f}Dez igual a cinco á, então á vale dois."),
    dict(id="s08", block="fatorada", text="A lei é {a}ípsilon igual a dois, vezes xis menos um, vezes xis menos cinco."),
    # desenvolvida
    dict(id="s09", block="desenvolvida", text="Para a forma com á, bê e cê, {a}abra os parênteses. [p=0.2] {b}Xis menos um, vezes xis menos cinco, dá xis ao quadrado menos seis xis mais cinco. [p=0.2] {c}Vezes dois: dois xis ao quadrado menos doze xis mais dez. [p=0.3] {d}O cê é dez: o corte no eixo ípsilon bateu."),
    # forma do vértice
    dict(id="s10", block="vertice", text="Existe uma terceira forma, que mostra {a}o vértice: [p=0.2] o ponto onde a parábola faz a curva e muda de sentido. [p=0.3] A mesma função se escreve {b}ípsilon igual a dois, vezes o parêntese xis menos três, ao quadrado, menos oito."),
    dict(id="s11", block="vertice", text="Confira abrindo: [p=0.2] {a}xis menos três, ao quadrado, dá xis ao quadrado menos seis xis mais nove. [p=0.2] {b}Vezes dois: dois xis ao quadrado menos doze xis mais dezoito. [p=0.2] {c}Tirando oito, fica mais dez. [p=0.2] A mesma lei."),
    dict(id="s12", block="vertice", text="Olhe o parêntese ao quadrado: {a}ele nunca é negativo. [p=0.2] O menor valor dele é {b}zero, quando xis vale três. [p=0.2] Aí sobra {c}ípsilon igual a menos oito. [p=0.2] Em qualquer outro xis, o parêntese ao quadrado é positivo, [p=0.2] e o ípsilon fica acima de menos oito. [p=0.3] O ponto mais baixo é {d}xis três, ípsilon menos oito. [p=0.2] E o três fica {e}bem no meio do um e do cinco."),
    dict(id="s13", block="vertice", text="Essa é a {a}forma do vértice: [p=0.2] {b}ípsilon igual a á, vezes o parêntese xis menos agá, ao quadrado, mais ká. [p=0.3] O vértice é {c}xis agá, ípsilon ká. [p=0.2] No exemplo, agá é três e ká é menos oito. [p=0.2] Com á negativo, o vértice vira o ponto mais alto."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}copiar o sinal de dentro do parêntese. [p=0.2] A pessoa vê xis menos três e diz que o vértice está em {b}xis menos três. [p=0.3] Teste: {c}menos três menos três dá menos seis, que ao quadrado dá trinta e seis. [p=0.2] {d}Vezes dois, menos oito: sessenta e quatro. [p=0.2] Bem longe do ponto mais baixo. [p=0.3] {e}O xis do vértice é o número que zera o parêntese."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho para achar o á sem montar equação: [p=0.2] {a}á é o cê dividido pelo produto das raízes. [p=0.3] {b}Produto das raízes: um vezes cinco dá cinco. [p=0.2] {c}Dez dividido por cinco: dois."),
    dict(id="s16", block="atalho", text="Funciona porque, em xis zero, {a}cada parêntese vira a raiz com o sinal trocado. [p=0.2] Trocar o sinal de ambos os fatores não muda o produto, [p=0.2] então o resultado é {b}á vezes o produto das raízes, que é o cê. [p=0.3] {c}Não vale quando o ponto dado não está no eixo ípsilon, [p=0.2] como xis seis, ípsilon dez. [p=0.2] {d}Aí, troque o ponto na forma fatorada."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma parábola tem {a}raízes menos dois e quatro [p=0.2] e passa por {b}xis zero, ípsilon menos dezesseis. [p=0.3] {c}Escreva a lei na forma fatorada e na forma com á, bê e cê. [p=0.3] Depois, {d}diga o vértice de ípsilon igual a dois, vezes o parêntese xis menos um, ao quadrado, menos dezoito."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Ípsilon igual a á, vezes xis mais dois, vezes xis menos quatro. [p=0.2] Pelo atalho, o produto das raízes é {b}menos oito, [p=0.2] e {c}menos dezesseis dividido por menos oito dá dois. [p=0.3] Lei: {d}dois, vezes xis mais dois, vezes xis menos quatro."),
    dict(id="s20", block="resposta", text="Abrindo: {a}xis mais dois, vezes xis menos quatro, dá xis ao quadrado menos dois xis menos oito. [p=0.2] {b}Vezes dois: dois xis ao quadrado menos quatro xis menos dezesseis. [p=0.3] Na forma do vértice, {c}o um zera o parêntese: [p=0.2] vértice em {d}xis um, ípsilon menos dezoito. [p=0.2] E o um fica {e}no meio do menos dois e do quatro: bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}cada raiz vira um parêntese, [p=0.2] {b}o ponto que sobra decide o á [p=0.2] e {c}a forma do vértice mostra o vértice sem conta."),
    dict(id="s22", block="fim", text="Na próxima aula, a parábola responde a uma desigualdade: [p=0.2] {a}para quais xis o xis ao quadrado menos cinco xis mais seis fica negativo? [p=0.2] A resposta está {b}onde a curva passa abaixo do eixo xis. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
