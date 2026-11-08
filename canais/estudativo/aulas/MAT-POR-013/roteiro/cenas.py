# Estudativo · MAT-POR-013 — Praticando: variações sucessivas (Matemática · Porcentagem · prática).
# Habilidade: acumular aumentos e descontos e interpretar variações divulgadas em notícias.
# Pré-requisitos: MAT-POR-010, MAT-POR-011, MAT-POR-012. Próxima: fim da trilha Porcentagem; segue MAT-FIN-001 (Juros simples).
# Questões e notícias inéditas, criadas para esta aula; nenhuma é manchete real.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: variações sucessivas"

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
    dict(id="s01", block="gancho", text="Lojas e notícias {a}adoram porcentagem, [p=0.2] e muitas vezes ela engana. [p=0.3] Aqui vão {b}cinco situações, criadas para esta aula. [p=0.2] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}multiplicar os fatores em variações seguidas, [p=0.2] {b}dividir um pelo fator para voltar ao valor original, [p=0.2] {c}separar ponto percentual de variação percentual [p=0.2] e {d}multiplicar porcentagem de porcentagem. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: dois aumentos
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] A conta de água subiu {b}cinco por cento em um ano [p=0.2] e {c}dez por cento no ano seguinte. [p=0.3] {d}Qual foi o aumento total?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Fatores: {a}um vírgula zero cinco e um vírgula um. [p=0.2] Sem as vírgulas, {b}cento e cinco vezes onze dá mil cento e cinquenta e cinco. [p=0.2] Três casas: {c}um vírgula cento e cinquenta e cinco. [p=0.3] Aumento de {d}quinze vírgula cinco por cento, [p=0.1] e não de quinze."),
    # atalho
    dict(id="s06", block="atalho", text="Com o atalho, sai de cabeça. [p=0.2] {a}Cinco mais dez dá quinze. [p=0.2] {b}Cinco vezes dez dá cinquenta, dividido por cem dá zero vírgula cinco. [p=0.2] {c}Quinze vírgula cinco por cento. [p=0.3] Funciona porque {d}o segundo aumento também vale sobre o primeiro. [p=0.2] Com três variações ou mais, {e}não compensa: multiplique os fatores."),
    # situação 2: dois descontos
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma liquidação anuncia {b}trinta por cento de desconto [p=0.2] e {c}mais vinte por cento no caixa, sobre o preço já com desconto. [p=0.3] {d}Qual é o desconto total?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Fatores: {a}zero vírgula sete e zero vírgula oito. [p=0.2] {b}Sete vezes oito dá cinquenta e seis: [p=0.1] {c}zero vírgula cinquenta e seis. [p=0.3] Você paga cinquenta e seis por cento do preço: {d}desconto total de quarenta e quatro por cento. [p=0.3] Com {e}cem reais: [p=0.1] cai para setenta, [p=0.2] e vinte por cento de setenta são catorze: {f}cinquenta e seis. [p=0.3] Quem somou achou {g}cinquenta por cento de desconto, e errou."),
    # situação 3: notícia de sobe e desce
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Uma notícia diz: [p=0.2] {b}as vendas de uma fábrica caíram sessenta por cento em um ano, [p=0.2] subiram sessenta por cento no ano seguinte {c}e voltaram ao nível de antes. [p=0.3] {d}A notícia está certa? [p=0.2] {e}E quanto as vendas precisariam subir para voltar?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] Fatores: {a}zero vírgula quatro e um vírgula seis. [p=0.2] {b}Quatro vezes dezesseis dá sessenta e quatro: zero vírgula sessenta e quatro. [p=0.2] As vendas estão {c}trinta e seis por cento abaixo do que eram. [p=0.2] {d}A notícia errou. [p=0.3] Com {e}cem: [p=0.1] cai para quarenta, [p=0.2] sobe sessenta por cento de quarenta dá vinte e quatro, [p=0.2] e para em {f}sessenta e quatro."),
    dict(id="s13", block="resposta3", text="Para voltar: {a}um dividido por zero vírgula quatro. [p=0.2] Ande uma casa: dez dividido por quatro dá dois vírgula cinco. [p=0.2] Fator dois vírgula cinco é o valor inteiro mais uma vez e meia ele: [p=0.1] {b}precisariam subir cento e cinquenta por cento. [p=0.3] Pelas frações: {c}perdeu três quintos, e ficaram dois. [p=0.2] Precisa ganhar três partes em cima de duas: {d}uma vez e meia o que ficou."),
    # situação 4: ponto percentual
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] A taxa de juros de um financiamento caiu de {b}doze por cento para {c}nove por cento ao ano. [p=0.2] A manchete diz: {d}juros caem três por cento. [p=0.3] {e}Como corrigir a manchete?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}Doze menos nove dá três pontos percentuais. [p=0.2] A variação percentual divide pelo valor de antes: [p=0.2] {b}três dividido por doze dá zero vírgula vinte e cinco. [p=0.3] Então {c}os juros caíram três pontos percentuais, [p=0.2] ou {d}vinte e cinco por cento. [p=0.2] Três por cento está errado."),
    # situação 5: porcentagem de porcentagem
    dict(id="s17", block="questao5", text="{a}Última situação. [p=0.2] Em um bairro, {b}setenta por cento das casas têm internet. [p=0.2] Dessas, {c}quarenta por cento têm internet por fibra. [p=0.3] {d}Que porcentagem de todas as casas do bairro tem fibra?"),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="Vamos lá. [p=0.2] Os quarenta por cento são {a}das casas com internet, não de todas. [p=0.2] Porcentagem de porcentagem, multiplique: [p=0.2] {b}setenta vezes quarenta dá dois mil e oitocentos. [p=0.2] {c}Dividido por cem dá vinte e oito por cento das casas. [p=0.3] Confira com {d}cem casas: [p=0.2] setenta com internet, [p=0.2] e {e}quarenta por cento de setenta dá vinte e oito."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}variações seguidas se multiplicam, [p=0.2] {b}a volta divide um pelo fator [p=0.2] e {c}diferença entre porcentagens é ponto percentual. [p=0.3] Com isso, {d}você fechou a trilha de porcentagem."),
    dict(id="s21", block="fim", text="A próxima trilha é {a}matemática financeira, [p=0.2] e começa pelos {b}juros simples: [p=0.2] o que são {c}capital, taxa, tempo e montante, [p=0.2] e quanto rendem {d}mil e duzentos reais a dois por cento ao mês, em seis meses. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
