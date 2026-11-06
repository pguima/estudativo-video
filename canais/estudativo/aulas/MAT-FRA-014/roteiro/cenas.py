# Estudativo · MAT-FRA-014 — Ler, comparar e arredondar decimais (Matemática · Frações e Decimais).
# Habilidade: ler 3,25, explicar por que 0,8 é maior que 0,75 e arredondar 3,146 para 3,15.
# Pré-requisitos: MAT-FRA-001 (o que é uma fração), MAT-NUM-002 (ler e comparar números grandes). Próxima: MAT-FRA-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Ler, comparar e arredondar decimais"

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
    dict(id="s01", block="gancho", text="{a}Zero vírgula oito ou {b}zero vírgula setenta e cinco: [p=0.2] qual é maior? [p=0.4] Se você apostou no setenta e cinco, [p=0.2] {c}caiu no erro mais comum dos decimais."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai ler, comparar e arredondar números com vírgula, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}comparar números grandes [p=0.2] e {c}saber que fração é dividir um inteiro em partes iguais. [p=0.3] Se faltar alguma, procure no canal."),
    # a vírgula
    dict(id="s04", block="virgula", text="Comece pelo dinheiro. [p=0.2] {a}Três reais e vinte e cinco centavos [p=0.2] se escreve {b}três vírgula vinte e cinco. [p=0.3] A vírgula separa: {c}à esquerda, o inteiro. [p=0.2] {d}À direita, o pedaço que não chega a um inteiro."),
    # casas decimais
    dict(id="s05", block="casas", text="Divida {a}um real em dez partes iguais. [p=0.2] Cada parte é uma {b}moeda de dez centavos. [p=0.2] Uma parte em dez se chama {c}décimo, [p=0.2] e fica na {d}primeira casa depois da vírgula. [p=0.3] {e}Casa decimal é isso: cada lugar depois da vírgula."),
    dict(id="s06", block="casas", text="Divida o real em {a}cem partes. [p=0.2] Cada parte é {b}um centavo. [p=0.2] Uma parte em cem se chama {c}centésimo, [p=0.2] e fica na {d}segunda casa."),
    dict(id="s07", block="casas", text="Divida em {a}mil partes, e cada uma é um {b}milésimo, [p=0.2] na {c}terceira casa. [p=0.3] Essa moeda não existe, [p=0.2] mas o {d}preço do dólar no noticiário usa essa casa."),
    # leitura
    dict(id="s08", block="leitura", text="Para ler, você tem {a}duas formas. [p=0.2] A rápida: {b}três vírgula vinte e cinco. [p=0.3] A completa: {c}três inteiros e vinte e cinco centésimos. [p=0.3] Quem dá o nome é a {d}última casa: [p=0.2] aqui ela é a dos centésimos."),
    dict(id="s09", block="leitura", text="{a}Zero vírgula oito termina nos décimos. [p=0.2] Então também se lê {b}oito décimos."),
    # comparar
    dict(id="s10", block="comparar", text="Volte à pergunta do começo. [p=0.2] {a}Oito décimos são oito moedas de dez centavos: [p=0.2] {b}oitenta centavos. [p=0.3] E {c}zero vírgula setenta e cinco são {d}setenta e cinco centavos."),
    dict(id="s11", block="comparar", text="Oitenta é mais que setenta e cinco. [p=0.2] Então {a}zero vírgula oito é maior que zero vírgula setenta e cinco."),
    dict(id="s12", block="comparar", text="A regra: compare {a}casa por casa, da esquerda para a direita. [p=0.2] {b}Inteiros: zero e zero, empate. [p=0.2] {c}Décimos: oito contra sete. [p=0.2] O oito ganha, e {d}a comparação termina aqui. [p=0.2] O cinco nem entra."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é ler o que vem depois da vírgula {a}como número inteiro: [p=0.2] {b}setenta e cinco é maior que oito. [p=0.3] Só que esse oito está na casa dos décimos, [p=0.2] e {c}vale oitenta centavos. [p=0.2] {d}Mais algarismos não significa número maior."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}iguale as casas com zeros. [p=0.2] {b}Zero vírgula oito vira {c}zero vírgula oitenta. [p=0.3] Aí é só comparar {d}oitenta com setenta e cinco."),
    dict(id="s15", block="atalho", text="Funciona porque {a}zero no fim, depois da vírgula, não muda o valor: [p=0.2] oito moedas de dez centavos continuam sendo oitenta centavos. [p=0.3] {b}Não compensa quando um número tem muitas casas: [p=0.2] você escreveria zeros à toa, e a comparação casa por casa resolve antes."),
    # arredondar
    dict(id="s16", block="arredondar", text="Agora, arredondar. [p=0.2] {a}Três vírgula cento e quarenta e seis reais não cabe no caixa, [p=0.2] porque {b}não existe moeda menor que um centavo. [p=0.3] Arredondar é {c}trocar o número pelo vizinho mais próximo com menos casas."),
    dict(id="s17", block="arredondar", text="Com duas casas, os vizinhos são {a}três vírgula catorze e {b}três vírgula quinze. [p=0.3] Iguale as casas: [p=0.2] três vírgula cento e quarenta [p=0.2] contra três vírgula cento e cinquenta. [p=0.3] Cento e quarenta e seis está {c}mais perto de cento e cinquenta."),
    dict(id="s18", block="arredondar", text="A regra: {a}olhe o algarismo logo depois da última casa que vai ficar. [p=0.2] Se for {b}cinco ou mais, essa casa sobe um. [p=0.2] Se for {c}menos que cinco, ela fica como está."),
    dict(id="s19", block="arredondar", text="Aqui, a última casa que fica é a do {a}quatro. [p=0.2] Logo depois vem o {b}seis. [p=0.2] O quatro sobe para cinco: {c}três vírgula quinze."),
    dict(id="s20", block="arredondar", text="Se fosse {a}três vírgula cento e quarenta e dois, o dois é menos que cinco: {b}três vírgula catorze. [p=0.3] E se for {c}exatamente cinco? [p=0.2] Aí o número fica bem no meio dos vizinhos, e nenhum está mais perto. [p=0.2] Por combinação, {d}cinco manda subir: [p=0.2] {e}três vírgula cento e quarenta e cinco vira três vírgula quinze."),
    # questão
    dict(id="s21", block="questao", text="Hora de testar. [p=0.2] O banco A vende o dólar por {a}cinco vírgula sete reais. [p=0.2] O banco B, por {b}cinco vírgula seiscentos e oitenta e cinco. [p=0.3] {c}Qual é o mais barato? [p=0.2] E {d}quanto fica o preço do banco B, arredondado para centavos?"),
    dict(id="s22", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta", text="Vamos lá. [p=0.2] Iguale as casas: {a}cinco vírgula setecentos [p=0.2] contra {b}cinco vírgula seiscentos e oitenta e cinco. [p=0.3] Nos décimos, {c}seis é menor que sete. [p=0.2] O {d}banco B é o mais barato."),
    dict(id="s24", block="resposta", text="Para arredondar, a última casa que fica é a do {a}oito. [p=0.2] Logo depois vem {b}um cinco, que manda subir. [p=0.2] O oito vira nove: {c}cinco reais e sessenta e nove centavos."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: {a}a última casa dá o nome, [p=0.2] {b}compare casa por casa, [p=0.2] e {c}de cinco para cima, sobe."),
    dict(id="s26", block="fim", text="Na próxima aula, você {a}soma e subtrai decimais alinhando a vírgula, [p=0.2] até com {b}troco e dívida. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
