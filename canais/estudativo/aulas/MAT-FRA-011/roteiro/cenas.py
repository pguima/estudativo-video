# Estudativo · MAT-FRA-011 — Dividir frações (Matemática · Frações e Decimais).
# Habilidade: calcular 2/3 ÷ 5/7 e descobrir quantos copos de 1/4 L cabem em 3 L.
# Pré-requisitos: MAT-FRA-009 (multiplicar). Próxima: MAT-FRA-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Soma de frações e número misto não estão na ficha: fração com o de cima maior aparece só como passo da conta.

TITULO = "Dividir frações"

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
    dict(id="s01", block="gancho", text="{a}Três litros de suco. [p=0.2] {b}Copos de um quarto de litro. [p=0.3] {c}Quantos copos você enche?"),
    dict(id="s02", block="gancho", text="A conta é {a}três dividido por um quarto, [p=0.2] e o resultado é {b}doze. [p=0.3] Você dividiu, e o número {c}cresceu. [p=0.3] Parece errado, mas está certo."),
    dict(id="s03", block="gancho", text="{a}Até o fim desta aula, você vai entender por quê, [p=0.2] dividir quaisquer frações [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s04", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] {b}multiplicar frações. [p=0.2] Numerador, o número de cima, vezes numerador. [p=0.1] Denominador, o de baixo, vezes denominador. [p=0.2] E {c}cortar em cruz quando der. [p=0.3] Se faltar, procure a aula no canal."),
    # quantas vezes cabe
    dict(id="s05", block="cabe", text="O que dividir quer dizer? [p=0.2] {a}Doze dividido por três pergunta: [p=0.2] {b}quantas vezes o três cabe no doze? [p=0.3] {c}Quatro. [p=0.3] Com fração, a pergunta é a mesma."),
    dict(id="s06", block="cabe", text="Três dividido por um quarto pergunta: {a}quantas vezes um quarto de litro cabe em três litros? [p=0.3] Comece por {b}um litro. [p=0.2] Cortado em quartos, ele rende {c}quatro copos."),
    dict(id="s07", block="cabe", text="Em três litros: {a}três vezes quatro, {b}doze copos. [p=0.3] Repare: {c}dividir por um quarto deu o mesmo que multiplicar por quatro. [p=0.2] O copo é menor que um litro, então cabe muitas vezes. [p=0.2] Por isso o número cresceu."),
    # de cima diferente de um
    dict(id="s08", block="garrafas", text="E se o de cima da fração não for um? [p=0.2] {a}Seis litros, em garrafas de {b}dois terços de litro. [p=0.3] Quantas garrafas? [p=0.2] Se a garrafa fosse de um terço, cada litro encheria três: {c}seis vezes três, dezoito garrafas."),
    dict(id="s09", block="garrafas", text="Mas dois terços é {a}o dobro de um terço. [p=0.2] Cabe metade: {b}dezoito dividido por dois, nove garrafas. [p=0.3] Olhe o que você fez: {c}multiplicou pelo três, que era o de baixo, [p=0.2] e {d}dividiu pelo dois, que era o de cima. [p=0.3] Faz sentido: o de baixo diz quantos pedaços cabem em um inteiro, [p=0.2] e o de cima diz quantos pedaços formam uma garrafa."),
    # regra
    dict(id="s10", block="regra", text="Multiplicar por três e dividir por dois é o mesmo que {a}multiplicar por três meios, [p=0.2] a fração {b}virada de cabeça para baixo. [p=0.3] Confira: {c}três meios de seis. [p=0.2] Seis dividido por dois, três. [p=0.2] Vezes três, {d}nove. [p=0.3] Não se assuste com o de cima maior que o de baixo: aqui, essa fração é só um passo da conta. [p=0.3] Repare que só a garrafa decidiu a conta. [p=0.2] Por isso, o caminho é o mesmo se antes do sinal de dividir vier um inteiro ou uma fração. [p=0.3] Daí sai a regra: [p=0.2] {e}conserva a primeira, {f}vira a segunda, {g}multiplica."),
    dict(id="s11", block="regra", text="Vamos usar: {a}dois terços dividido por cinco sétimos. [p=0.3] Conserva {b}dois terços. [p=0.2] Vira a segunda: {c}sete quintos. [p=0.2] Troca o dividido por {d}vezes."),
    dict(id="s12", block="regra", text="{a}Dois vezes sete, catorze. [p=0.2] {b}Três vezes cinco, quinze. [p=0.2] {c}Catorze quinze avos. [p=0.3] Deu menos que um: cinco sétimos não chega a caber uma vez inteira em dois terços. [p=0.3] Dá para conferir, porque multiplicar desfaz a divisão: {d}catorze quinze avos vezes cinco sétimos volta a {e}dois terços."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}virar a fração errada. [p=0.2] Em três dividido por um quarto, a pessoa vira o três, [p=0.2] que é {b}três dividido por um, [p=0.2] e escreve {c}um terço vezes um quarto: {d}um doze avos."),
    dict(id="s14", block="erro", text="Seria {a}menos de um copo em três litros. [p=0.2] Não faz sentido. [p=0.2] A que vira é sempre {b}a segunda, a que vem depois do sinal de dividir."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho prometido: {a}fração com um em cima. [p=0.3] Dividir por {b}um meio é dobrar. [p=0.2] Por {c}um terço, é multiplicar por três. [p=0.2] Por {d}um quarto, por quatro."),
    dict(id="s16", block="atalho", text="Funciona porque um inteiro tem {a}quatro quartos: cada unidade rende quatro. [p=0.3] Não compensa quando o de cima não é um, como em {b}cinco sétimos: [p=0.2] aí, {c}conserva, vira e multiplica."),
    dict(id="s17", block="atalho", text="Veja em ação: {a}três quartos de litro, em doses de {b}um oitavo de litro. [p=0.3] Dividir por um oitavo é {c}multiplicar por oito. [p=0.2] {d}Divida o oito e o quatro por quatro: ficam dois e um. [p=0.2] Três vezes dois, {e}seis doses."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Uma fita tem {a}quatro quintos de metro. [p=0.2] Cada laço usa {b}dois quinze avos de metro. [p=0.3] {c}Quantos laços dá para fazer?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Quantas vezes o laço cabe na fita? [p=0.2] Isso é {a}dividir. [p=0.3] {b}Conserva quatro quintos, [p=0.1] vira a segunda: {c}quinze meios, [p=0.1] e multiplica."),
    dict(id="s21", block="resposta", text="Só depois de virar, corte em cruz. [p=0.2] {a}Quatro e dois: divida por dois, ficam dois e um. [p=0.3] {b}Quinze e cinco: divida por cinco, ficam três e um. [p=0.3] {c}Dois vezes três: {d}seis laços. [p=0.3] Confira: {e}seis vezes dois quinze avos, doze quinze avos, [p=0.2] que simplifica para {f}quatro quintos. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}dividir é perguntar quantas vezes cabe. [p=0.2] Na conta, {b}conserva a primeira, vira a segunda e multiplica."),
    dict(id="s23", block="fim", text="Na próxima aula, você {a}junta as operações em uma conta só, [p=0.2] como {b}um meio mais dois terços vezes três quartos, [p=0.2] e encara {c}frações negativas e número misto. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
