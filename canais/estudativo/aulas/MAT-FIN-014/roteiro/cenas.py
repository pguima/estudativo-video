# Estudativo · MAT-FIN-014 — Praticando: taxas, inflação e propostas (Matemática · Matemática Financeira · prática).
# Habilidade: comparar propostas de compra, financiamento e aplicação e escolher a melhor.
# Pré-requisitos: MAT-FIN-008, MAT-FIN-009, MAT-FIN-010, MAT-FIN-011, MAT-FIN-012, MAT-FIN-013. Próxima: fim da trilha (segue MAT-LEI-001 na Matemática do Zero).
# Questões inéditas, criadas para esta aula. Sem calculadora: todas as contas saem de cabeça.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: taxas, inflação e propostas"

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
    dict(id="s01", block="gancho", text="{a}Cinco propostas do dia a dia, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}taxa efetiva, [p=0.2] {b}inflação e taxa real, [p=0.2] {c}juros embutidos, [p=0.2] {d}SAC e Price [p=0.2] e {e}rendimento líquido. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: taxa efetiva
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um empréstimo anuncia {b}vinte e quatro por cento ao ano, com capitalização semestral: [p=0.2] os juros entram na conta a cada seis meses. [p=0.3] {c}Qual é a taxa efetiva ao ano?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Semestre é meio ano: {a}metade de vinte e quatro, doze por cento ao semestre. [p=0.2] Em um ano, o fator se repete duas vezes: {b}um vírgula doze ao quadrado. [p=0.2] Pelo atalho de dois períodos: doze mais doze dá vinte e quatro. [p=0.2] Doze vezes doze dá cento e quarenta e quatro, dividido por cem dá um vírgula quarenta e quatro. [p=0.3] Juntos, taxa efetiva de {c}vinte e cinco vírgula quarenta e quatro por cento ao ano. [p=0.2] Maior que os vinte e quatro do rótulo, {d}como a pista da taxa efetiva avisava."),
    # situação 2: inflação acumulada e taxa real
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Num país em época de inflação alta, a inflação foi de {b}dez por cento em um ano e de vinte por cento no seguinte. [p=0.2] No mesmo período, um salário subiu {c}sessenta e cinco por cento. [p=0.3] {d}Qual foi o ganho real do salário?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] Primeiro, a inflação acumulada: {a}um vírgula um vezes um vírgula dois dá um vírgula trinta e dois. [p=0.3] Para o ganho real, {b}divida os fatores. [p=0.2] Ande duas casas: {c}cento e sessenta e cinco dividido por cento e trinta e dois."),
    dict(id="s09", block="resposta2", text="Cento e trinta e dois cabe uma vez e sobram {a}trinta e três. [p=0.2] Trinta e três é {b}um quarto de cento e trinta e dois. [p=0.2] Fator um vírgula vinte e cinco: {c}ganho real de vinte e cinco por cento. [p=0.3] Quem somou a inflação e subtraiu achou {d}trinta e cinco. [p=0.2] Com taxas altas, a subtração erra feio."),
    # situação 3: taxa embutida
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Um celular custa {b}mil e duzentos reais à vista, [p=0.2] ou {c}seiscentos de entrada e seiscentos e três em trinta dias. [p=0.2] O seu dinheiro rende {d}um por cento ao mês. [p=0.3] {e}Qual é a taxa embutida, e qual forma vale mais a pena?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] Tire a entrada: o saldo é {a}mil e duzentos menos seiscentos dá seiscentos. [p=0.2] Por esses seiscentos, você paga {b}seiscentos e três um mês depois. [p=0.2] Um por cento de seiscentos é seis, então três é {c}meio por cento ao mês. [p=0.3] Na mesma data: aplicados, os seiscentos viram seiscentos e seis. [p=0.2] Você paga seiscentos e três e ainda sobram três reais. [p=0.2] A loja cobra meio, o seu dinheiro rende um: {d}pague a prazo."),
    # situação 4: SAC e Price
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] Um financiamento de {b}vinte e quatro mil reais, em vinte e quatro meses, a {c}um por cento ao mês. [p=0.3] {d}Qual é a primeira prestação pela SAC? [p=0.2] E {e}qual sistema cobra mais juros no total, SAC ou Price?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] Amortização: {a}vinte e quatro mil dividido por vinte e quatro dá mil. [p=0.2] Juros: um por cento do saldo, {b}duzentos e quarenta. [p=0.2] Primeira prestação: {c}mil duzentos e quarenta reais. [p=0.3] Cobra mais juros {d}a Price: [p=0.2] ela amortiza menos no começo, e {e}os juros correm sobre um saldo maior."),
    # situação 5: rendimento líquido
    dict(id="s16", block="questao5", text="{a}Última situação. [p=0.2] Você vai aplicar {b}dez mil reais por um ano. [p=0.2] O banco A paga {c}onze por cento ao ano, com quinze por cento de imposto sobre o rendimento. [p=0.2] O banco B paga {d}nove e meio por cento ao ano, sem imposto. [p=0.3] {e}Qual escolher?"),
    dict(id="s17", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta5", text="Vamos lá. [p=0.2] Em A, o rendimento bruto é {a}mil e cem reais. [p=0.2] Imposto: dez por cento, cento e dez; [p=0.2] cinco por cento, cinquenta e cinco. [p=0.2] Juntos, {b}cento e sessenta e cinco. [p=0.2] Líquido: {c}novecentos e trinta e cinco."),
    dict(id="s19", block="resposta5", text="Em B, nove e meio por cento de dez mil: {a}novecentos e cinquenta, inteiros. [p=0.3] Escolha {b}o banco B, por quinze reais. [p=0.2] Os onze por cento de A {c}eram brutos."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: antes de escolher, compare {a}na mesma data, [p=0.2] {b}no mesmo prazo [p=0.2] e {c}pelo valor de verdade: efetivo, real ou líquido."),
    dict(id="s21", block="fim", text="Com isso, você fecha {a}a Matemática Financeira. [p=0.2] Na próxima aula, começa uma trilha nova, sobre {b}ler problemas de matemática: [p=0.2] achar a pergunta antes do texto e separar {c}só os números que entram na conta. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
