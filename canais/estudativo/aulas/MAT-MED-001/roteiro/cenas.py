# Estudativo · MAT-MED-001 — Converter comprimento: a escada do metro (Matemática · Medidas e Unidades).
# Habilidade: escolher a unidade certa para cada medida e converter 2,5 km em metros e 340 cm em metros.
# Pré-requisitos: MAT-FRA-016 (andar com a vírgula). Próxima: MAT-MED-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Área, volume e prefixos como giga ficam para MAT-MED-003 a 005.

TITULO = "Converter comprimento: a escada do metro"

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
    dict(id="s01", block="gancho", text="Uma corrida de {a}dois vírgula cinco quilômetros. [p=0.3] Quantos metros? [p=0.3] Se você respondeu {b}duzentos e cinquenta, [p=0.2] encolheu a corrida {c}dez vezes."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai escolher a unidade certa para cada medida, [p=0.2] converter comprimentos sem decorar tabela [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] {b}andar com a vírgula. [p=0.2] Vezes dez, ela vai uma casa para a direita. [p=0.2] Dividido por dez dá uma casa para a esquerda. [p=0.3] Se faltar, procure no canal."),
    # escolher a unidade
    dict(id="s04", block="unidade", text="Toda medida de comprimento tem {a}um número e uma unidade. [p=0.2] A unidade principal é o {b}metro: [p=0.2] mais ou menos um passo bem largo de um adulto."),
    dict(id="s05", block="unidade", text="Para distâncias grandes, existe o {a}quilômetro, que vale mil metros: [p=0.2] serve para a distância entre duas cidades. [p=0.3] Para coisas pequenas, o {b}centímetro, a centésima parte do metro: [p=0.2] serve para medir um lápis. [p=0.3] E o {c}milímetro, a milésima parte: [p=0.2] os risquinhos menores da régua."),
    dict(id="s06", block="unidade", text="Escolher a unidade é escolher {a}a que deixa o número fácil de ler. [p=0.2] A altura de uma pessoa: {b}um vírgula setenta metro, [p=0.2] ou {c}cento e setenta centímetros. [p=0.3] Ninguém diz {d}zero vírgula zero zero um sete quilômetro."),
    # a escada
    dict(id="s07", block="escada", text="Para converter, pense numa {a}escada de sete degraus. [p=0.2] No meio, o {b}metro. [p=0.2] Acima dele, {c}decâmetro, hectômetro e quilômetro. [p=0.2] Abaixo, {d}decímetro, centímetro e milímetro."),
    dict(id="s08", block="escada", text="Cada degrau vale {a}dez vezes o de baixo. [p=0.3] Então a regra é uma só: [p=0.2] {b}cada degrau, uma casa da vírgula. [p=0.2] {c}Descendo, para uma unidade menor, o número cresce: a vírgula vai para a direita. [p=0.2] {d}Subindo, o número diminui: a vírgula vai para a esquerda."),
    dict(id="s09", block="escada", text="Faz sentido: [p=0.2] em um metro cabem {a}cem centímetros. [p=0.2] Unidade menor, {b}mais pedaços para cobrir a mesma distância."),
    # quilômetro para metro
    dict(id="s10", block="km", text="Voltando à corrida: {a}dois vírgula cinco quilômetros em metros. [p=0.2] Do quilômetro ao metro, são {b}três degraus para baixo. [p=0.3] {c}Um degrau: vinte e cinco. [p=0.2] {d}Dois: duzentos e cinquenta. [p=0.2] {e}Três: dois mil e quinhentos, completando com zero."),
    dict(id="s11", block="km", text="{a}Dois mil e quinhentos metros. [p=0.2] É a mesma conta que {b}vezes mil: [p=0.2] mil tem três zeros, três casas."),
    # centímetro para metro
    dict(id="s12", block="cm", text="E o caminho de volta: {a}trezentos e quarenta centímetros em metros. [p=0.2] Do centímetro ao metro, {b}dois degraus para cima. [p=0.3] Lembre que todo número inteiro tem {c}uma vírgula escondida no fim."),
    dict(id="s13", block="cm", text="{a}Um degrau: trinta e quatro. [p=0.2] {b}Dois: três vírgula quarenta. [p=0.3] O zero no fim não muda nada: {c}três vírgula quatro metros. [p=0.2] É o mesmo que {d}dividir por cem."),
    dict(id="s14", block="cm", text="Mais um, bem curto: {a}quarenta e cinco milímetros em centímetros. [p=0.2] Um degrau para cima, uma casa para a esquerda: [p=0.2] {b}quatro vírgula cinco centímetros."),
    # erro
    dict(id="s15", block="erro", text="O erro comum é {a}andar para o lado errado. [p=0.2] A pessoa multiplica e escreve {b}trinta e quatro mil metros. [p=0.3] São trinta e quatro quilômetros, [p=0.2] para uma medida que cabe {c}dentro de uma sala!"),
    dict(id="s16", block="erro", text="Antes de andar a vírgula, pergunte: {a}a unidade ficou maior ou menor? [p=0.2] {b}Unidade maior, número menor. [p=0.2] O metro é maior que o centímetro, então {c}o número tem que diminuir."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho: {a}o nome já diz a conta. [p=0.3] {b}Quilo quer dizer mil: [p=0.2] um quilômetro, mil metros, três casas. [p=0.2] {c}Centi quer dizer centésimo: [p=0.2] cem centímetros fazem um metro, duas casas. [p=0.2] {d}Mili quer dizer milésimo: [p=0.2] mil milímetros, três casas."),
    dict(id="s18", block="atalho", text="Funciona porque {a}o começo do nome é o próprio degrau. [p=0.3] {b}Não compensa entre duas unidades longe do metro, como quilômetro e centímetro: [p=0.2] aí, conte os degraus na escada. [p=0.3] {c}Um vírgula dois quilômetro em centímetros: cinco degraus, cinco casas, [p=0.2] {d}cento e vinte mil centímetros."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Uma pessoa caminhou {a}um vírgula oito quilômetro de manhã [p=0.2] e {b}novecentos e cinquenta metros à tarde. [p=0.3] {c}Quantos metros ela andou no dia?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Antes de somar, {a}tudo na mesma unidade. [p=0.2] Do quilômetro ao metro, {b}três casas para a direita. [p=0.2] {c}Um vírgula oito vira mil e oitocentos."),
    dict(id="s22", block="resposta", text="{a}Mil e oitocentos mais novecentos e cinquenta: [p=0.2] {b}dois mil setecentos e cinquenta metros. [p=0.3] Quem soma direto {c}um vírgula oito com novecentos e cinquenta [p=0.2] mistura quilômetro com metro e erra."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}cada degrau, uma casa. [p=0.2] {b}Unidade menor, número maior."),
    dict(id="s24", block="fim", text="Na próxima aula, a mesma escada serve para {a}massa e capacidade: [p=0.2] {b}tonelada em quilos e mililitros em litros. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
