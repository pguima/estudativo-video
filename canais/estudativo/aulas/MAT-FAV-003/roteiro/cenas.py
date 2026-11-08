# Estudativo · MAT-FAV-003 — Equações e inequações modulares (Matemática · Funções Avançadas · Função modular e definida por partes).
# Habilidade: resolver |x − 3| = 5 (x = 8 ou x = −2) e |x − 3| < 5 (−2 < x < 8) pensando em distância até o 3.
# Pré-requisitos: MAT-EQU-016 (inequação dupla), MAT-FAV-002 (módulo e gráfico em V). Próxima: MAT-FAV-004.
# Questão inédita, criada para esta aula.
# Distância: |8 − 3| = 5 · |−2 − 3| = |−5| = 5 · |x − 3| = 5 → x = 3 + 5 = 8 ou x = 3 − 5 = −2 (x − 3 = ±5).
# Casos: |x − 3| = 0 → x = 3 · |x − 3| = −1 → nenhum.
# Inequação: |x − 3| < 5 → −5 < x − 3 < 5 → −2 < x < 8 → ]−2, 8[ · |x − 3| > 5 → x < −2 ou x > 8.
# Erro: |x − 3| < 5 → "x < 8" · teste x = −10: |−10 − 3| = 13, e 13 não é < 5.
# Atalho: centro = número que zera o de dentro, raio = número do outro lado; pontas = centro ± raio; menor → entre, maior → fora.
# Questão: |x + 2| ≤ 4 · centro −2, raio 4 · pontas −6 e 2 · [−6, 2] · conta: −4 ≤ x + 2 ≤ 4 → −6 ≤ x ≤ 2.
# Visual: reta numérica de −3 a 9 com o 3 no centro e os saltos de 5 para cada lado (E.salto); conta em duas linhas;
#   E.intervalo para ]−2, 8[ e para as duas semirretas de fora; −10 com o salto de 13 em vermelho; palco escuro no atalho.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; "módulo de xis menos três".

TITULO = "Equações e inequações modulares"

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
    dict(id="s01", block="gancho", text="{a}Módulo de xis menos três igual a cinco. [p=0.2] Muita gente resolve rápido: {b}xis igual a oito. [p=0.3] Está certo, mas {c}está incompleto. [p=0.2] Existe {d}outro número que também funciona, e ele é negativo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve equações e inequações com módulo [p=0.2] {b}pensando em distância, quase sem conta, [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}o módulo como distância até o zero, [p=0.2] e {b}a inequação dupla, aquela com três partes, em que você faz a mesma conta em todas. [p=0.3] Se faltar alguma, procure no canal."),
    # distância
    dict(id="s04", block="distancia", text="A ideia que resolve tudo: [p=0.2] {a}módulo de xis menos três é a distância entre xis e três. [p=0.3] Teste: {b}de oito até três são cinco passos, [p=0.2] e oito menos três dá cinco. [p=0.2] {c}De menos dois até três também são cinco passos, [p=0.2] e menos dois menos três dá menos cinco, que tem módulo cinco."),
    # equação
    dict(id="s05", block="equacao", text="Então, {a}módulo de xis menos três igual a cinco pergunta: [p=0.2] quais números estão {b}a cinco passos do três? [p=0.3] Ande cinco para a direita: {c}oito. [p=0.2] Ande cinco para a esquerda: {d}menos dois. [p=0.2] Duas respostas."),
    dict(id="s06", block="equacao", text="Na conta, é o mesmo: [p=0.2] o de dentro vale {a}cinco ou menos cinco. [p=0.2] {b}Xis menos três igual a cinco dá oito. [p=0.2] {c}Xis menos três igual a menos cinco dá menos dois."),
    dict(id="s07", block="equacao", text="Dois casos especiais. [p=0.2] {a}Módulo igual a zero: só um número, o próprio três. [p=0.2] {b}Módulo igual a menos um: nenhum número, [p=0.2] porque distância nunca é negativa."),
    # inequação
    dict(id="s08", block="inequacao", text="E {a}módulo de xis menos três menor que cinco? [p=0.2] Agora são os números {b}a menos de cinco passos do três. [p=0.3] Eles ficam {c}entre menos dois e oito. [p=0.2] Na reta, {d}bolinha vazia nas pontas, [p=0.2] porque a distância cinco não é menor que cinco."),
    dict(id="s09", block="inequacao", text="Na conta, vira {a}uma inequação dupla: [p=0.2] menos cinco, menor que xis menos três, menor que cinco. [p=0.2] {b}Some três nas três partes: [p=0.2] {c}menos dois, menor que xis, menor que oito."),
    dict(id="s10", block="inequacao", text="Com o maior, é o contrário: [p=0.2] {a}módulo de xis menos três maior que cinco [p=0.2] são os números {b}a mais de cinco passos do três. [p=0.2] Eles ficam {c}do lado de fora: xis menor que menos dois, ou xis maior que oito."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}tirar as barras e seguir a conta. [p=0.2] Em módulo de xis menos três menor que cinco, a pessoa escreve {b}xis menos três menor que cinco, [p=0.2] e responde {c}xis menor que oito."),
    dict(id="s12", block="erro", text="Mas teste {a}xis igual a menos dez. [p=0.2] Menos dez é menor que oito. [p=0.2] Só que de menos dez até três são {b}treze passos, [p=0.2] e treze não é menor que cinco. [p=0.3] Faltou {c}a outra ponta: xis maior que menos dois."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}centro e raio. [p=0.2] {b}O centro é o número que zera o de dentro. [p=0.2] {c}O raio é o número do outro lado. [p=0.3] As pontas são {d}centro menos raio e centro mais raio."),
    dict(id="s14", block="atalho", text="Depois, uma regra curta: [p=0.2] {a}menor, fica entre as pontas. [p=0.2] {b}Maior, fica fora delas. [p=0.3] Funciona porque módulo é distância: [p=0.2] perto do centro é entre, longe é fora. [p=0.3] {c}Se tiver número multiplicando o xis, como dois xis, [p=0.2] use a inequação dupla: é mais seguro."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Resolva {a}módulo de xis mais dois, menor ou igual a quatro. [p=0.2] {b}Dê a resposta como intervalo."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Xis mais dois zera com menos dois: esse é o centro. [p=0.2] {b}O raio é quatro. [p=0.3] Pontas: {c}menos dois menos quatro, menos seis; [p=0.2] e {d}menos dois mais quatro, dois."),
    dict(id="s18", block="resposta", text="É menor ou igual: {a}fica entre as pontas, e as pontas entram. [p=0.2] {b}Menos seis, menor ou igual a xis, menor ou igual a dois. [p=0.2] Intervalo {c}fechado no menos seis e fechado no dois. [p=0.3] Pela conta: {d}menos quatro, menor ou igual a xis mais dois, menor ou igual a quatro. [p=0.2] Tirando dois das três partes, {e}dá o mesmo."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}módulo é distância, [p=0.2] {b}o igual dá duas respostas, [p=0.2] e {c}o menor fica entre, o maior fica fora."),
    dict(id="s20", block="fim", text="Na próxima aula, uma função entra dentro da outra: [p=0.2] {a}a função composta, [p=0.2] em que {b}a saída de uma vira a entrada da seguinte. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
