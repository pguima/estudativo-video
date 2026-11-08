# Estudativo · MAT-FIN-007 — Praticando: juros simples e compostos (Matemática · Matemática Financeira · prática).
# Habilidade: calcular juros, montantes e prazos em empréstimos e aplicações.
# Pré-requisitos: MAT-FIN-001, MAT-FIN-002, MAT-FIN-003, MAT-FIN-004, MAT-FIN-005, MAT-FIN-006. Próxima: MAT-FIN-008.
# Questões inéditas, criadas para esta aula. Situação 3: multa de 2% e juros de 1% ao mês, como no condomínio.
# A situação 4 prepara a ponte: 1% ao mês rende 12,68% em um ano (MAT-FIN-008, taxa equivalente).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: juros simples e compostos"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações de dinheiro, [p=0.2] criadas para esta aula. [p=0.3] Empréstimo, aplicação, conta atrasada. [p=0.2] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}três ferramentas: [p=0.2] {b}a fórmula dos juros simples, jota igual a cê vezes i vezes tê, [p=0.2] {c}a dos compostos, capital vezes o fator elevado ao tempo, [p=0.2] e {d}taxa e tempo sempre na mesma unidade. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: juros simples com conversão
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um empréstimo de {b}dois mil e quinhentos reais, [p=0.1] a juros simples de {c}dezoito por cento ao ano, [p=0.1] foi pago em {d}oito meses. [p=0.3] {e}Quanto foi pago no total?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Taxa ao ano, tempo em meses: {a}converta. [p=0.2] {b}Dezoito dividido por doze dá um vírgula cinco por cento ao mês. [p=0.2] {c}Vezes oito meses, doze por cento."),
    dict(id="s06", block="resposta1", text="{a}Doze por cento de dois mil e quinhentos. [p=0.2] Dez por cento são duzentos e cinquenta, [p=0.1] e dois por cento são cinquenta. [p=0.2] Juros de {b}trezentos reais. [p=0.3] A pergunta é o total: {c}dois mil e oitocentos reais."),
    # situação 2: achar a taxa
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Um empréstimo em juros simples [p=0.1] de {b}oitocentos reais foi quitado com {c}mil e quarenta, [p=0.1] {d}seis meses depois. [p=0.3] {e}Qual foi a taxa ao mês?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Cuidado: mil e quarenta é {a}o montante. [p=0.2] Juros: {b}mil e quarenta menos oitocentos dá duzentos e quarenta. [p=0.3] Juro de um mês: {c}duzentos e quarenta dividido por seis dá quarenta. [p=0.2] {d}Quarenta dividido por oitocentos dá zero vírgula zero cinco: [p=0.1] {e}cinco por cento ao mês."),
    # situação 3: conta atrasada
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Um condomínio de {b}mil e duzentos reais foi pago com {c}quinze dias de atraso. [p=0.3] Multa de {d}dois por cento [p=0.1] e juros de mora de {e}um por cento ao mês, cobrados por dia. [p=0.3] {f}Quanto foi pago?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] {a}Multa, uma vez só: dois por cento de mil e duzentos dá vinte e quatro reais. [p=0.3] Mora: quinze dias são {b}meio mês. [p=0.2] Metade de um por cento dá {c}zero vírgula cinco por cento. [p=0.2] {d}Zero vírgula cinco por cento de mil e duzentos dá seis reais."),
    dict(id="s13", block="resposta3", text="Pelo atalho, {a}dois por cento mais meio por cento dá dois e meio por cento de uma vez: [p=0.1] trinta reais. [p=0.3] Total: {b}mil duzentos e trinta reais."),
    # situação 4: compostos contra simples
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Cinco mil reais ficam aplicados por {c}doze meses, a {d}um por cento ao mês. [p=0.3] {e}Quanto rende a mais em juros compostos do que em simples? [p=0.3] A tabela dá: {f}um vírgula zero um elevado a doze, cerca de um vírgula um dois seis oito."),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] Doze meses passam de {a}um período da taxa, então os compostos ganham. [p=0.3] Simples: {b}um por cento vezes doze dá doze por cento. [p=0.2] Doze por cento de cinco mil dá {c}seiscentos reais de juros."),
    dict(id="s17", block="resposta4", text="Compostos: {a}cinco mil vezes um vírgula um dois seis oito. [p=0.2] Cerca de {b}cinco mil seiscentos e trinta e quatro reais. [p=0.2] Juros de seiscentos e trinta e quatro. [p=0.3] Diferença: {c}trinta e quatro reais a mais nos compostos."),
    # situação 5: valor presente
    dict(id="s18", block="questao5", text="{a}Última situação. [p=0.2] Uma pessoa quer ter {b}oito mil quatrocentos e cinquenta reais daqui a {c}dois anos. [p=0.2] A aplicação rende {d}trinta por cento ao ano, em juros compostos, [p=0.1] uma taxa alta, só de exemplo. [p=0.3] {e}Quanto ela precisa aplicar hoje?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] Fator: {a}um vírgula três. [p=0.2] Dois anos: {b}um vírgula três ao quadrado dá um vírgula seis nove. [p=0.3] Capital: {c}oito mil quatrocentos e cinquenta dividido por um vírgula seis nove. [p=0.2] Ande duas casas: {d}oitocentos e quarenta e cinco mil dividido por cento e sessenta e nove. [p=0.2] {e}Cinco mil reais."),
    dict(id="s21", block="resposta5", text="Conferindo pela ida: {a}cinco mil vira seis mil e quinhentos, [p=0.1] que vira oito mil quatrocentos e cinquenta. [p=0.2] Bateu. [p=0.3] Quem tirou trinta por cento duas vezes do total {b}errou: [p=0.1] os juros nasceram do capital, e não do montante."),
    # atalho
    dict(id="s22", block="atalho", text="Para fechar, um atalho para {a}dobrar, nos simples e nos compostos. [p=0.3] {b}Nos simples, cem dividido pela taxa. [p=0.2] {c}Nos compostos, setenta e dois dividido pela taxa. [p=0.3] A oito por cento ao mês: {d}nos simples, doze meses e meio. [p=0.2] {e}Nos compostos, cerca de nove meses."),
    dict(id="s23", block="atalho", text="Os compostos dobram antes porque {a}rendem juro sobre juro. [p=0.3] Os cuidados são os mesmos das aulas: [p=0.2] o setenta e dois é {b}uma estimativa, [p=0.1] e erra mais com taxas muito altas."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}taxa e tempo na mesma unidade, [p=0.2] {b}separe juros de montante [p=0.2] e {c}confira se a resposta faz sentido."),
    dict(id="s25", block="fim", text="Repare na situação quatro: [p=0.2] um por cento ao mês rendeu {a}doze vírgula sessenta e oito por cento em um ano, e não doze. [p=0.3] Na próxima aula, você entende essa diferença: [p=0.1] {b}taxa equivalente e taxa efetiva. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
