# Estudativo · MAT-FRA-001 — O que é uma fração (Matemática · Frações e Decimais).
# Habilidade: pintar 3/4 de uma figura, dizer o que são numerador e denominador e ler 12/4 como 12 ÷ 4.
# Pré-requisitos: MAT-NUM-009. Próxima: MAT-FRA-002.
# Equivalência e simplificação ainda não foram ensinadas (MAT-FRA-003): todas as frações já estão na forma final.
# Ensina a leitura das frações (meio a décimo, "avos" a partir do onze), usada sem explicação nas aulas seguintes.

TITULO = "O que é uma fração"

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
    dict(id="s01", block="gancho", text="{a}Três quartos. [p=0.3] {b}Cinco doze avos. [p=0.3] {c}Doze quartos. [p=0.3] Se essas palavras te travam, [p=0.2] calma: ninguém nasce sabendo esse código, e ele é bem mais simples do que parece."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}pintar uma fração, [p=0.2] {b}ler qualquer fração em voz alta, [p=0.2] descobrir que {c}doze quartos é só o número três, [p=0.2] e ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] {b}saber dividir. [p=0.3] Se faltar isso, procure a aula no canal."),
    # a barra
    dict(id="s04", block="barra", text="Imagine {a}uma barra de chocolate. [p=0.2] Você vai dividir essa barra com três amigos, de forma justa. [p=0.3] Então corta em {b}quatro pedaços iguais."),
    dict(id="s05", block="barra", text="{a}Cada pedaço é um quarto da barra. [p=0.3] Fração é isso: {b}um jeito de dizer que parte de um inteiro você tem. [p=0.2] Inteiro, aqui, é a barra completa."),
    dict(id="s06", block="barra", text="{a}Pinte um pedaço: um quarto. [p=0.3] Pinte mais {b}dois. [p=0.2] Três dos quatro pedaços estão pintados. [p=0.3] Pronto: você acabou de pintar {c}três quartos da barra."),
    dict(id="s07", block="barra", text="Só tem uma exigência: os pedaços precisam ser {a}iguais. [p=0.3] Se um for enorme e outro minúsculo, {b}aquilo não é um quarto da barra."),
    # numerador e denominador
    dict(id="s08", block="nomes", text="Na escrita, a fração tem {a}um traço, [p=0.2] {b}um número em cima [p=0.2] e {c}outro embaixo."),
    dict(id="s09", block="nomes", text="O de baixo se chama {a}denominador. [p=0.2] Ele diz {b}em quantas partes iguais o inteiro foi dividido. [p=0.3] Denominar é dar nome, [p=0.2] e é ele que {c}dá o nome ao pedaço: quarto."),
    dict(id="s10", block="nomes", text="O de cima se chama {a}numerador. [p=0.2] Ele {b}conta quantas partes você pegou. [p=0.3] Mudou o de cima, {c}muda a quantidade de pedaços. [p=0.2] Mudou o de baixo, {d}muda o tamanho do pedaço."),
    dict(id="s11", block="nomes", text="Com esses nomes, pintar fica automático. [p=0.2] Para pintar {a}dois quintos, [p=0.2] o de baixo manda {b}cortar em cinco partes iguais, [p=0.2] e o de cima manda {c}pintar duas."),
    # ler
    dict(id="s12", block="leitura", text="Como se lê uma fração? [p=0.2] {a}Primeiro o de cima, como um número normal. [p=0.2] {b}Depois o nome do pedaço, que vem do de baixo."),
    dict(id="s13", block="leitura", text="São nove nomes. [p=0.2] Barra cortada em duas partes: {a}meio. [p=0.2] Em três: {b}terço. [p=0.2] Em quatro: {c}quarto. [p=0.2] Em cinco: {d}quinto. [p=0.2] Em seis: {e}sexto."),
    dict(id="s14", block="leitura", text="Em sete: {a}sétimo. [p=0.2] Em oito: {b}oitavo. [p=0.2] Em nove: {c}nono. [p=0.2] Em dez: {d}décimo."),
    dict(id="s15", block="leitura", text="Com mais de um pedaço, é só usar o plural: [p=0.2] {a}um quinto, [p=0.2] {b}dois quintos, [p=0.2] {c}sete oitavos."),
    dict(id="s16", block="leitura", text="De onze em diante, a lista acaba, e a regra fica ainda mais fácil. [p=0.2] Fale o número de baixo e acrescente a palavra {a}avos. [p=0.3] {b}Um onze avos. [p=0.2] {c}Cinco doze avos. [p=0.2] {d}Três vinte avos. [p=0.3] Cem e mil têm nome próprio, centésimo e milésimo, mas isso é assunto de outra aula."),
    # o traço
    dict(id="s17", block="traco", text="E aquele traço também tem significado: {a}o traço da fração é uma divisão. [p=0.3] Doze quartos quer dizer {b}doze dividido por quatro."),
    dict(id="s18", block="traco", text="Imagine {a}doze barras inteiras para {b}quatro pessoas. [p=0.2] Cada uma leva {c}três barras. [p=0.3] Então {d}doze quartos é igual a três. [p=0.3] É um número comum, escrito em forma de fração."),
    dict(id="s19", block="traco", text="Fração com o de cima maior que o de baixo é assunto de outra aula. [p=0.2] Por enquanto, guarde: {a}traço é divisão."),
    # erro
    dict(id="s20", block="erro", text="Cuidado com o erro mais comum. [p=0.2] Olhe a barra: {a}três pedaços pintados, [p=0.2] {b}um sem pintar. [p=0.3] Muita gente põe {c}o três em cima e o um embaixo."),
    dict(id="s21", block="erro", text="Mas o traço é divisão, e {a}três dividido por um dá três. [p=0.3] Seriam {b}três barras inteiras, [p=0.2] e você tem menos de uma. [p=0.3] O de baixo conta {c}todos os pedaços, pintados ou não."),
    # atalho
    dict(id="s22", block="atalho", text="E o atalho prometido: {a}a tabuada ao contrário. [p=0.3] Viu {b}vinte e quatro sextos? [p=0.2] Não arme a conta. [p=0.2] Pergunte: {c}seis vezes quanto dá vinte e quatro? [p=0.3] {d}Quatro."),
    dict(id="s23", block="atalho", text="Funciona porque {a}dividir é o caminho de volta de multiplicar. [p=0.3] Quando não compensa? [p=0.2] Fora da tabuada, como em {b}seiscentos e doze terços. [p=0.2] Aí, {c}arme a conta de dividir."),
    # questão
    dict(id="s24", block="questao", text="Hora de testar. [p=0.2] Uma barra tem {a}doze pedaços iguais. [p=0.2] Você comeu {b}cinco. [p=0.3] {c}Que fração da barra você comeu, e como ela se lê?"),
    dict(id="s25", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s26", block="resposta", text="Vamos lá. [p=0.2] O de baixo é o total de pedaços: {a}doze. [p=0.2] O de cima é o que você pegou: {b}cinco. [p=0.3] De onze em diante, usamos avos: {c}cinco doze avos."),
    # fechamento
    dict(id="s27", block="fim", text="Resumindo: {a}o de baixo diz em quantas partes o inteiro foi dividido, [p=0.2] {b}o de cima diz quantas você pegou, [p=0.2] e {c}o traço é uma divisão."),
    dict(id="s28", block="fim", text="Na próxima aula, você vai {a}calcular três quartos de vinte [p=0.2] e {b}descobrir um salário inteiro sabendo só uma parte dele. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
