# Estudativo · MAT-POT-002 — Potência de negativo, fração ou decimal (Matemática · Potências e Raízes).
# Habilidade: calcular (−2)³, (2/3)³ e 0,3², ver a diferença entre (−3)² e −3² e resolver 2 + 3 × 2².
# Pré-requisitos: MAT-FRA-009 (multiplicar frações), MAT-FRA-016 (decimais), MAT-NUM-018 (expressões com inteiros), MAT-POT-001 (o que é potência). Próxima: MAT-POT-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sem propriedades de mesma base: MAT-POT-003 vem depois.
# (−2)³ = 4 × (−2) = −8 · (−3)² = 9 · −3² = −(3 × 3) = −9 · (2/3)³ = 8/27 · 0,3² = 0,09 (9 com 1 + 1 casas).
# 2 + 3 × 2² = 2 + 12 = 14; erros: (2 + 3) × 4 = 20; 2 + (3 × 2)² = 38. (−1)²⁵ = −1.
# MAT-NUM-018 chama de "sinal colado" o menos do começo da conta: s08 avisa que a potência é resolvida antes dele.
# Questão: 10 − 2 × (−3)² = 10 − 18 = −8; saindo da ordem, 8 × 9 = 72.

TITULO = "Potência de negativo, fração ou decimal"

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
    dict(id="s01", block="gancho", text="{a}Abre parênteses, menos três, fecha parênteses, ao quadrado. [p=0.3] Dá {b}nove. [p=0.3] {c}Sem parênteses, menos três ao quadrado. [p=0.3] Dá {d}menos nove. [p=0.3] Um par de parênteses troca o sinal da resposta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula potência de negativo, de fração e de decimal, [p=0.2] põe a potência {b}na ordem das operações [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}quatro coisas: [p=0.2] {b}o que é potência, [p=0.2] {c}a regra de sinais, [p=0.2] {d}multiplicar frações [p=0.2] e {e}multiplicar decimais. [p=0.3] Se faltar alguma, procure no canal."),
    # base negativa
    dict(id="s04", block="negativo", text="O expoente continua dizendo {a}quantas vezes a base aparece. [p=0.3] Só que agora a base é negativa, e o parêntese mostra isso: {b}abre parênteses, menos dois, fecha parênteses, ao cubo. [p=0.3] O menos dois aparece três vezes: {c}menos dois vezes menos dois vezes menos dois."),
    dict(id="s05", block="negativo", text="Uma conta por vez. [p=0.2] {a}Menos dois vezes menos dois: sinais iguais, mais quatro. [p=0.3] {b}Mais quatro vezes menos dois: sinais diferentes, {c}menos oito."),
    # com e sem parênteses
    dict(id="s06", block="parenteses", text="Volte ao começo da aula. [p=0.2] {a}Abre parênteses, menos três, fecha parênteses, ao quadrado. [p=0.3] A base é o menos três inteiro: {b}menos três vezes menos três. [p=0.2] Sinais iguais: {c}mais nove."),
    dict(id="s07", block="parenteses", text="{a}Sem parênteses, o expoente só alcança o que está colado nele: {b}o três. [p=0.2] O menos fica de fora. [p=0.3] Primeiro, {c}três vezes três dá nove. [p=0.2] Depois, entra o menos: {d}menos nove."),
    dict(id="s08", block="parenteses", text="Você aprendeu que o menos do começo da conta é um sinal colado no número. [p=0.2] Continua sendo, mas {a}a potência é resolvida antes dele. [p=0.3] Para o menos entrar na potência, {b}só com parênteses."),
    # fração
    dict(id="s09", block="fracao", text="E com fração? [p=0.2] A cada lavagem, uma camiseta fica com {a}dois terços da cor que tinha antes. [p=0.3] Depois de {b}três lavagens, restam dois terços de dois terços de dois terços. [p=0.3] A palavra de significa vezes, então a conta é {c}abre parênteses, dois terços, fecha parênteses, ao cubo."),
    dict(id="s10", block="fracao", text="O parêntese faz {a}a fração inteira se repetir. [p=0.3] Multiplica os de cima: {b}dois vezes dois vezes dois dá oito. [p=0.2] Multiplica os de baixo: {c}três vezes três vezes três dá vinte e sete. [p=0.3] {d}Oito vinte e sete avos. [p=0.3] O expoente vale {e}para o de cima e para o de baixo."),
    # decimal
    dict(id="s11", block="decimal", text="E com decimal? [p=0.2] {a}Zero vírgula três ao quadrado é {b}zero vírgula três vezes zero vírgula três. [p=0.3] Ignore as vírgulas: {c}três vezes três dá nove. [p=0.2] Conte as casas: {d}uma mais uma dá duas. [p=0.2] Nove com duas casas: {e}zero vírgula zero nove."),
    # ordem
    dict(id="s12", block="ordem", text="E onde a potência entra na ordem das operações? [p=0.3] Você viu que o vezes é {a}uma soma empacotada. [p=0.2] A potência é {b}um vezes empacotado. [p=0.3] Primeiro se resolvem os pacotes. [p=0.2] Então ela ganha um degrau só dela."),
    dict(id="s13", block="ordem", text="A ordem fica assim: [p=0.2] {a}parênteses, [p=0.2] {b}depois potência, [p=0.2] {c}depois vezes e dividido, [p=0.2] {d}por último mais e menos. [p=0.3] A potência entra {e}antes do vezes."),
    dict(id="s14", block="ordem", text="{a}Dois mais três vezes dois ao quadrado. [p=0.3] {b}Primeiro a potência: dois ao quadrado dá quatro. [p=0.2] {c}Depois o vezes: três vezes quatro dá doze. [p=0.2] {d}Por último, dois mais doze dá {e}catorze."),
    dict(id="s15", block="ordem", text="Quem soma primeiro chega em {a}vinte. [p=0.3] Quem faz {b}três vezes dois antes do expoente chega em {c}trinta e oito. [p=0.2] Saiu da ordem, saiu da resposta."),
    # erro
    dict(id="s16", block="erro", text="O erro comum aqui é escrever {a}zero vírgula três ao quadrado igual a zero vírgula nove. [p=0.3] A pessoa faz três vezes três e {b}conta uma casa só. [p=0.3] Mas multiplicar por zero vírgula três é pegar só um pedaço, [p=0.2] então o resultado tem que ficar {c}menor que zero vírgula três. [p=0.3] {d}Zero vírgula zero nove fica. [p=0.2] Elevar nem sempre faz crescer: {e}com base entre zero e um, o número diminui."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho: {a}olhe o expoente antes de fazer conta. [p=0.3] Base negativa com {b}expoente par dá positivo. [p=0.2] Com {c}expoente ímpar dá negativo."),
    dict(id="s18", block="atalho", text="{a}Abre parênteses, menos um, fecha parênteses, elevado a vinte e cinco. [p=0.3] {b}Vinte e cinco é ímpar. [p=0.2] Resposta: {c}menos um. [p=0.3] Nenhuma conta."),
    dict(id="s19", block="atalho", text="Funciona porque {a}cada dupla de menos vira mais. [p=0.2] Com expoente ímpar, {b}sobra um menos sem dupla. [p=0.3] {c}Só vale com o menos dentro do parêntese. [p=0.2] E com base positiva não compensa: [p=0.2] não há sinal para decidir."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Resolva: {a}dez menos dois vezes, [p=0.2] {b}abre parênteses, menos três, fecha parênteses, ao quadrado."),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] A potência vem primeiro, e o menos está dentro do parêntese: {a}mais nove. [p=0.2] Depois o vezes: {b}dois vezes nove dá dezoito. [p=0.2] Por último: {c}dez menos dezoito dá {d}menos oito. [p=0.3] Quem começou por dez menos dois chegou em setenta e dois: saiu da ordem."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}o parêntese decide quem é a base, [p=0.2] e {b}a potência vem antes do vezes."),
    dict(id="s24", block="fim", text="Na próxima aula, você vai {a}multiplicar e dividir potências de mesma base sem calcular cada uma [p=0.2] e descobrir {b}por que um número elevado a zero dá um. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
