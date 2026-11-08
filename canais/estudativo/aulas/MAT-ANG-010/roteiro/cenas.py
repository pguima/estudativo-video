# Estudativo · MAT-ANG-010 — Teorema de Tales: feixe de paralelas (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: achar x quando retas paralelas cortam duas transversais, com segmentos 3 e 6 numa e 4 e x na outra (x = 8).
# Pré-requisitos: MAT-ANG-003 (paralelas e transversal), MAT-RAZ-002 (proporção, cruz, procurar o fator). Próxima: MAT-ANG-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. "Cruz", "está para" e "procure o fator" como em MAT-RAZ-002.
# Figuras (E.paralelas só faz duas paralelas e uma transversal: montar com E.segmento):
#   feixe com três paralelas quase horizontais e duas transversais inclinadas; pedaços 3 e 6 na da esquerda, 4 e x na da direita.
#   s05-s06: linhas de caderno igualmente espaçadas e duas réguas inclinadas, com os trechos iguais marcados (E.marcas_iguais).
#   s10: trecho inteiro, da primeira à última paralela (9 e 12), com chave.
#   Questão: três ruas paralelas e duas avenidas; 60 m e 90 m numa avenida, 200 m no total na outra (80 m e 120 m).

TITULO = "Teorema de Tales: feixe de paralelas"

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
    dict(id="s01", block="gancho", text="{a}Num mapa, três ruas paralelas cortam duas avenidas. [p=0.3] Numa avenida, os quarteirões medem {b}três e seis centímetros. [p=0.2] Na outra, o primeiro mede {c}quatro. [p=0.3] E o segundo? [p=0.2] Sem régua, dá para saber: {d}oito centímetros."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha esse número em qualquer feixe de paralelas, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o que são retas paralelas e o que é uma transversal, [p=0.2] e {c}achar o número que falta numa proporção, com a cruz. [p=0.3] Se faltar alguma, procure no canal."),
    # feixe
    dict(id="s04", block="feixe", text="Várias retas paralelas juntas formam {a}um feixe de paralelas. [p=0.2] Uma reta que corta todas elas é {b}uma transversal. [p=0.3] Cada transversal fica {c}dividida em pedaços, um entre cada paralela e a seguinte."),
    # caderno
    dict(id="s05", block="caderno", text="Por que os pedaços combinam? [p=0.2] Pense {a}nas linhas do caderno: paralelas, sempre à mesma distância. [p=0.3] Passe {b}uma régua inclinada por cima delas. [p=0.2] Entre uma linha e a seguinte, {c}a régua marca sempre o mesmo tamanho."),
    dict(id="s06", block="caderno", text="Com {a}outra régua, mais inclinada, [p=0.2] o pedaço muda de tamanho, [p=0.2] mas {b}continua igual entre linhas vizinhas. [p=0.3] Então, se um trecho pega {c}o dobro de linhas numa régua, [p=0.2] ele também é o dobro {d}na outra régua."),
    # regra
    dict(id="s07", block="regra", text="Isso vale mesmo com as paralelas em distâncias diferentes. [p=0.2] É o {a}Teorema de Tales: [p=0.2] {b}retas paralelas cortam as transversais em pedaços proporcionais. [p=0.3] Proporcional quer dizer {c}na mesma razão: [p=0.2] o que um pedaço é do outro numa transversal, ele é na outra também."),
    dict(id="s08", block="regra", text="Na figura do começo: [p=0.2] {a}pedaço de cima sobre pedaço de baixo, numa transversal, [p=0.2] igual a {b}pedaço de cima sobre pedaço de baixo, na outra. [p=0.3] Fica {c}três está para seis, assim como quatro está para xis."),
    dict(id="s09", block="regra", text="Agora é a cruz. [p=0.2] {a}Três vezes xis, de um lado. [p=0.2] {b}Seis vezes quatro dá vinte e quatro, do outro. [p=0.3] {c}Três xis igual a vinte e quatro. [p=0.2] {d}Divida por três: xis igual a oito."),
    # outras montagens
    dict(id="s10", block="montagens", text="Também dá para montar {a}de uma transversal para a outra: [p=0.2] {b}três está para quatro, assim como seis está para xis. [p=0.2] A cruz dá {c}o mesmo três xis igual a vinte e quatro. [p=0.3] E vale com {d}o trecho inteiro, da primeira à última paralela: [p=0.2] {e}três está para nove, assim como quatro está para doze. [p=0.2] Isso ajuda quando a questão dá {f}o total."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}trocar a ordem de um lado só. [p=0.2] A pessoa monta {b}três está para seis, assim como xis está para quatro. [p=0.3] A cruz dá {c}seis xis igual a doze, [p=0.2] e xis vira {d}dois."),
    dict(id="s12", block="erro", text="Mas o xis fica {a}entre as mesmas paralelas que o seis, [p=0.2] e o seis é o maior pedaço da sua transversal. [p=0.2] Então {b}o xis tem que ser maior que quatro. [p=0.3] Regra de ouro: {c}nas duas frações, os pedaços na mesma ordem."),
    # atalho
    dict(id="s13", block="atalho", text="E o atalho prometido: {a}procure o fator dentro da mesma transversal. [p=0.3] {b}Seis é o dobro de três. [p=0.2] Então, na outra, {c}xis é o dobro de quatro: oito. [p=0.2] Sem montar conta."),
    dict(id="s14", block="atalho", text="Funciona porque {a}proporção é fração equivalente: [p=0.2] o que multiplica numa transversal, multiplica na outra. [p=0.3] Não compensa quando {b}o fator não é inteiro. [p=0.2] Pedaços de {c}quatro e seis numa transversal, dez e xis na outra: [p=0.2] aí, vá de cruz. [p=0.2] {d}Quatro xis igual a sessenta, e xis igual a quinze."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Três ruas paralelas cortam duas avenidas. [p=0.2] Na primeira avenida, os quarteirões medem {b}sessenta e noventa metros. [p=0.3] Na segunda, {c}o trecho da primeira à última rua mede duzentos metros. [p=0.3] {d}Quanto mede cada quarteirão na segunda avenida?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Na primeira avenida, o trecho inteiro é {a}sessenta mais noventa, que dá cento e cinquenta metros. [p=0.3] Compare o primeiro quarteirão com o trecho inteiro, em cada avenida: [p=0.2] {b}sessenta está para cento e cinquenta, assim como xis está para duzentos."),
    dict(id="s18", block="resposta", text="Cruz: {a}cento e cinquenta xis igual a sessenta vezes duzentos, que dá doze mil. [p=0.2] {b}Divida por cento e cinquenta: xis igual a oitenta metros. [p=0.3] O outro quarteirão: {c}duzentos menos oitenta dá cento e vinte metros."),
    dict(id="s19", block="resposta", text="Conferindo: {a}oitenta sobre cento e vinte, dividindo em cima e embaixo por quarenta, dá dois terços. [p=0.2] {b}Sessenta sobre noventa, dividindo por trinta, também dá dois terços. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}paralelas cortam as transversais em pedaços proporcionais, [p=0.2] e {b}as frações seguem sempre a mesma ordem."),
    dict(id="s21", block="fim", text="Na próxima aula, Tales entra {a}dentro do triângulo: [p=0.2] uma paralela a um lado corta os outros lados na mesma razão. [p=0.3] E você descobre {b}onde a bissetriz corta o lado da frente. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
