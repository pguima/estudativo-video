# Estudativo · MAT-NUM-011 — Qual conta o problema pede (Matemática · Números e Contas).
# Habilidade: decidir se um problema pede soma, subtração, multiplicação ou divisão pelas palavras do texto.
# Pré-requisitos: MAT-NUM-009 (dividir por um algarismo). Próxima: MAT-NUM-012.
# Questão inédita, criada para esta aula. Contas só por um algarismo: MAT-NUM-008 e MAT-NUM-010 não estão na ficha desta aula.
# Palavra é pista, nunca regra: a decisão vem da pergunta "o que está acontecendo com a quantidade?".
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Qual conta o problema pede"

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
    dict(id="s01", block="gancho", text="{a}Ana tem trinta reais. [p=0.2] {b}Isso é cinco reais a mais do que Bia tem. [p=0.3] {c}Quanto Bia tem? [p=0.4] Viu a palavra {d}mais e somou? [p=0.2] Então caiu: {e}trinta e cinco está errado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai escolher a conta pelo sentido do texto, [p=0.2] não por uma palavra solta, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa saber {a}somar, [p=0.2] {b}subtrair, [p=0.2] {c}multiplicar [p=0.2] e {d}dividir por um algarismo. [p=0.3] Se faltar alguma, procure no canal."),
    # a pergunta
    dict(id="s04", block="pergunta", text="Todo problema se resolve com uma pergunta: [p=0.2] {a}saindo do que eu sei para chegar ao que o problema pede, o que acontece com a quantidade? [p=0.3] Há {b}quatro respostas, [p=0.2] e cada uma é uma conta."),
    dict(id="s05", block="quatro", text="{a}Está juntando ou aumentando? É soma. [p=0.2] Você tinha {b}trezentos reais [p=0.2] e recebeu {c}cento e vinte. [p=0.2] O dinheiro aumentou: {d}quatrocentos e vinte. [p=0.3] Palavras que costumam indicar isso: {e}recebeu, ganhou, juntou."),
    dict(id="s06", block="quatro", text="{a}Está tirando ou diminuindo? É subtração. [p=0.2] Você tinha {b}trezentos reais [p=0.2] e gastou {c}cento e vinte. [p=0.2] O dinheiro diminuiu: {d}cento e oitenta. [p=0.3] Pistas: {e}gastou, perdeu, sobrou, falta."),
    dict(id="s07", block="quatro", text="{a}Está repetindo grupos iguais? É multiplicação. [p=0.2] {b}Seis caixas, [p=0.2] {c}doze ovos em cada caixa. [p=0.2] O doze se repete seis vezes: {d}setenta e dois ovos. [p=0.2] Daria para somar doze seis vezes: multiplicar é o jeito curto. [p=0.3] Pistas: {e}cada, por dia, o dobro."),
    dict(id="s08", block="quatro", text="{a}Está repartindo em partes iguais? É divisão. [p=0.2] {b}Oitenta e quatro reais [p=0.2] {c}entre seis pessoas: [p=0.2] {d}catorze reais para cada uma. [p=0.3] Pistas: {e}entre, igualmente, a metade."),
    # pista não é regra
    dict(id="s09", block="pista", text="Só que são {a}pistas, não regras. [p=0.2] Nenhuma palavra decide sozinha. [p=0.3] Veja o {b}cada. [p=0.2] {c}Setenta e dois ovos, [p=0.2] {d}seis em cada caixa. [p=0.2] {e}Quantas caixas? [p=0.3] Os ovos já estão contados, e você vai separar em grupos. [p=0.2] Tem a palavra cada, e a conta é {f}divisão: doze caixas."),
    dict(id="s10", block="pista", text="O mesmo vale para {a}sobrou. [p=0.2] Você {b}gastou oitenta reais [p=0.2] e {c}sobraram cento e vinte. [p=0.2] {d}Quanto tinha antes? [p=0.3] Saindo do que sobrou para chegar ao que você tinha, a quantidade aumenta: [p=0.2] {e}oitenta mais cento e vinte dá duzentos. [p=0.2] Apareceu sobrou, e a conta é soma."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}obedecer à palavra sem ler a frase. [p=0.2] Volte à Ana. [p=0.2] {b}Ninguém ganhou dinheiro nenhum: [p=0.2] a frase só compara. [p=0.3] Então pergunte: {c}quem tem mais? [p=0.2] É a Ana."),
    dict(id="s12", block="erro", text="Saindo dos trinta reais dela para chegar ao valor de Bia, {a}a quantidade diminui. [p=0.2] {b}Trinta menos cinco dá vinte e cinco. [p=0.3] {c}Confira na história: vinte e cinco mais cinco dá trinta. [p=0.2] Fecha."),
    dict(id="s13", block="erro", text="O contrário também engana. [p=0.2] A conta de água deu {a}quarenta reais. [p=0.2] {b}Isso é oito reais a menos do que a conta de luz. [p=0.2] {c}Quanto deu a de luz? [p=0.3] Apareceu menos, mas {d}quem custou mais foi a luz. [p=0.2] Saindo dos quarenta reais, a quantidade aumenta: [p=0.2] {e}quarenta mais oito dá quarenta e oito."),
    # mais de uma conta
    dict(id="s14", block="passos", text="Há problemas com {a}mais de uma conta. [p=0.2] {b}Três camisas de quarenta reais, [p=0.2] {c}pagas com duzentos. [p=0.2] {d}Qual é o troco? [p=0.3] Faça a pergunta a cada passo. [p=0.2] Repete grupos iguais: {e}três vezes quarenta dá cento e vinte. [p=0.2] Depois, tira: {f}duzentos menos cento e vinte dá oitenta."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}troque por números pequenos. [p=0.3] {b}Novecentos e doze folhetos [p=0.2] em {c}pacotes de seis. [p=0.2] {d}Quantos pacotes? [p=0.3] Pense em {e}dez folhetos em pacotes de dois. [p=0.2] {f}Dá cinco pacotes, e você dividiu. [p=0.3] Então a conta é {g}novecentos e doze dividido por seis, [p=0.2] que dá {h}cento e cinquenta e dois pacotes."),
    dict(id="s16", block="atalho", text="Funciona porque {a}a conta depende da história, não do tamanho dos números. [p=0.3] {b}Não compensa quando a história já está clara: [p=0.2] aí, vá direto à conta."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Caio tem {a}quarenta e cinco anos. [p=0.2] Isso é {b}três vezes a idade da filha. [p=0.3] {c}Que conta resolve, e quantos anos tem a filha?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Apareceu a palavra {a}vezes, mas o total já está dado: são os anos do Caio. [p=0.2] A frase compara, e {b}quem tem mais anos é ele. [p=0.3] Os anos dele são {c}três partes iguais, [p=0.2] e cada parte é a idade dela. [p=0.2] Repartir é {d}divisão."),
    dict(id="s20", block="resposta", text="{a}Quarenta e cinco dividido por três dá quinze. [p=0.2] {b}A filha tem quinze anos. [p=0.3] {c}Confira: três vezes quinze dá quarenta e cinco."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}a palavra é pista, [p=0.2] {b}a história decide. [p=0.2] Pergunte sempre: {c}do que eu sei até o que o problema pede, o que acontece com a quantidade?"),
    dict(id="s22", block="fim", text="A próxima aula é {a}só prática: [p=0.2] {b}problemas do dia a dia com as quatro contas, [p=0.2] {c}números grandes e atalhos. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
