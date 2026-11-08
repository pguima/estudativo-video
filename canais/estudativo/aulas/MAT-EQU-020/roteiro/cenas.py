# Estudativo · MAT-EQU-020 — Montar sistema a partir do problema (Matemática · Equações do 1º Grau).
# Habilidade: escrever o sistema de um caso com inteiras e meias-entradas e resolver 30 veículos e 100 rodas supondo que todos são motos.
# Pré-requisitos: MAT-EQU-013 (montar equação), MAT-EQU-018 (substituição). Próxima: MAT-EQU-021.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Preços do teatro inventados para a aula. A ficha não lista a MAT-EQU-019 como já ensinada: aqui só substituição e o atalho.

TITULO = "Montar sistema a partir do problema"

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
    dict(id="s01", block="gancho", text="{a}Trinta veículos, entre carros e motos, [p=0.2] e {b}cem rodas. [p=0.3] Quantos são os carros? [p=0.3] Dá para descobrir {c}sem escrever letra nenhuma."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você transforma um problema de texto em sistema, [p=0.2] e ainda leva esse {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}montar uma equação, com o que você não sabe virando letra, [p=0.2] e {c}resolver um sistema por substituição. [p=0.3] Se faltar alguma, procure no canal."),
    # o problema do teatro
    dict(id="s04", block="teatro", text="Veja este caso, com preços inventados para a aula. [p=0.2] Um teatro vendeu {a}cento e cinquenta ingressos, entre inteiras e meias-entradas. [p=0.3] {b}A inteira custa quarenta reais. [p=0.2] {c}A meia custa vinte reais. [p=0.3] Ao todo, entraram {d}quatro mil e quatrocentos reais. [p=0.3] {e}Quantas inteiras e quantas meias foram vendidas?"),
    # montar
    dict(id="s05", block="montar", text="{a}Primeiro passo: diga o que cada letra conta. [p=0.2] {b}A letra xis é o número de inteiras. [p=0.2] {c}A letra ípsilon é o número de meias. [p=0.3] As letras contam ingressos, {d}não reais."),
    dict(id="s06", block="montar", text="{a}Segundo passo: uma equação para as quantidades. [p=0.2] Ingressos somam com ingressos: [p=0.2] {b}xis mais ípsilon igual a cento e cinquenta."),
    dict(id="s07", block="montar", text="{a}Terceiro passo: uma equação para o dinheiro. [p=0.2] Cada inteira traz quarenta reais, [p=0.2] então as inteiras trazem {b}quarenta xis. [p=0.2] Cada meia traz vinte reais, [p=0.2] então as meias trazem {c}vinte ípsilon. [p=0.3] Somando, {d}quarenta xis mais vinte ípsilon igual a quatro mil e quatrocentos."),
    dict(id="s08", block="montar", text="Pronto, {a}esse é o sistema. [p=0.3] Repare no molde: [p=0.2] {b}uma equação conta as coisas, [p=0.2] {c}a outra soma os valores. [p=0.3] Sempre que o problema dá o total de coisas e o total em dinheiro, ele cabe nesse molde."),
    # resolver
    dict(id="s09", block="resolver", text="Resolvendo por substituição: [p=0.2] {a}ípsilon igual a cento e cinquenta menos xis. [p=0.3] Na outra equação, o vinte multiplica cada termo do parêntese: [p=0.2] {b}quarenta xis mais três mil menos vinte xis, igual a quatro mil e quatrocentos. [p=0.3] Juntando as letras e tirando três mil de cada lado: [p=0.2] {c}vinte xis igual a mil e quatrocentos, [p=0.2] e {d}xis igual a setenta. [p=0.3] As meias são cento e cinquenta menos setenta: [p=0.2] {e}oitenta."),
    dict(id="s10", block="resolver", text="Conferindo: [p=0.2] {a}setenta mais oitenta dá cento e cinquenta ingressos. [p=0.2] {b}Setenta inteiras dão dois mil e oitocentos reais. [p=0.2] {c}Oitenta meias dão mil e seiscentos. [p=0.2] {d}Somando, quatro mil e quatrocentos. [p=0.2] Bateu nas duas."),
    # erro
    dict(id="s11", block="erro", text="Agora, cuidado com o erro mais comum na montagem: [p=0.2] {a}misturar coisas diferentes na mesma equação. [p=0.2] A pessoa escreve {b}xis mais ípsilon igual a quatro mil e quatrocentos."),
    dict(id="s12", block="erro", text="Mas xis mais ípsilon conta {a}ingressos, [p=0.2] e quatro mil e quatrocentos são {b}reais. [p=0.3] Seriam quatro mil e quatrocentos ingressos, [p=0.2] num teatro que vendeu cento e cinquenta. [p=0.3] {c}Cada equação fala de uma coisa só."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho prometido, de volta aos veículos: [p=0.2] {a}suponha que todos são motos. [p=0.3] Trinta motos teriam {b}sessenta rodas. [p=0.2] Mas são cem, então {c}faltam quarenta rodas."),
    dict(id="s14", block="atalho", text="Trocar uma moto por um carro {a}mantém os trinta veículos [p=0.2] e {b}acrescenta duas rodas, [p=0.2] porque o carro tem quatro e a moto tem duas. [p=0.3] Para ganhar quarenta rodas, {c}quarenta dividido por dois dá vinte trocas. [p=0.3] São {d}vinte carros, [p=0.2] e as motos são trinta menos vinte: {e}dez."),
    dict(id="s15", block="atalho", text="Conferindo: [p=0.2] {a}vinte carros dão oitenta rodas. [p=0.2] {b}Dez motos dão vinte rodas. [p=0.2] {c}Oitenta mais vinte dá cem. [p=0.2] É a resposta que o sistema daria, {d}feita de cabeça."),
    dict(id="s16", block="atalho", text="Funciona porque {a}o total de veículos não muda, [p=0.2] e {b}cada troca acrescenta sempre as mesmas duas rodas. [p=0.3] Não compensa quando o problema {c}não dá o total de coisas, [p=0.2] ou quando há {d}mais de dois tipos. [p=0.2] Aí, monte o sistema."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma pessoa tem {a}vinte e cinco cédulas, umas de dez reais e outras de vinte reais. [p=0.3] Ao todo, são {b}trezentos e oitenta reais. [p=0.3] {c}Monte o sistema e descubra quantas cédulas de vinte reais ela tem."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}A letra xis conta as cédulas de dez. [p=0.2] {b}A letra ípsilon conta as cédulas de vinte. [p=0.3] Quantidades: {c}xis mais ípsilon igual a vinte e cinco. [p=0.3] Dinheiro: {d}dez xis mais vinte ípsilon igual a trezentos e oitenta."),
    dict(id="s20", block="resposta", text="Pelo atalho, suponha {a}todas de dez reais: [p=0.2] seriam {b}duzentos e cinquenta reais. [p=0.2] {c}Faltam cento e trinta. [p=0.3] Trocar uma cédula de dez por uma de vinte {d}acrescenta dez reais. [p=0.2] {e}Cento e trinta dividido por dez dá treze. [p=0.3] Ela tem {f}treze cédulas de vinte reais."),
    dict(id="s21", block="resposta", text="As de dez são vinte e cinco menos treze: [p=0.2] {a}doze cédulas. [p=0.3] Conferindo: [p=0.2] {b}treze mais doze dá vinte e cinco. [p=0.2] {c}Treze cédulas de vinte dão duzentos e sessenta reais. [p=0.2] {d}Doze cédulas de dez dão cento e vinte. [p=0.2] {e}Somando, trezentos e oitenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}diga o que cada letra conta, [p=0.2] {b}uma equação para as quantidades [p=0.2] e {c}outra para os valores."),
    dict(id="s23", block="fim", text="Na próxima aula, você {a}pratica com problemas de preços e quantidades, [p=0.2] montando e resolvendo cada sistema pelo caminho mais curto. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
