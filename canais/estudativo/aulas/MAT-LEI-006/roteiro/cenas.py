# Estudativo · MAT-LEI-006 — Escolher a melhor opção (Matemática · Leitura de Problemas).
# Habilidade: comparar o preço por litro e montar a compra mais barata de embalagens de 4 e de 6 unidades.
# Pré-requisitos: MAT-LEI-003 (barras e tabelas), MAT-RAZ-015 (taxas). Próxima: MAT-LEI-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Preços inventados para a aula. Visual: duas etiquetas lado a lado e tabela de casos (pacotes de seis, latas que faltam, pacotes de quatro, total).

TITULO = "Escolher a melhor opção"

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
    dict(id="s01", block="gancho", text="Uma garrafa de suco de {a}um litro e meio custa cinco reais e quarenta. [p=0.2] Uma de {b}dois litros custa sete reais. [p=0.3] A etiqueta menor engana: [p=0.2] {c}a garrafa de dois litros sai mais em conta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você compara preços do jeito certo e monta a compra mais barata, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de duas coisas: [p=0.2] {a}numa taxa, a palavra por quer dizer dividido por, [p=0.2] e {b}opções se organizam numa tabela. [p=0.3] Se faltar alguma, procure no canal."),
    # preço por litro
    dict(id="s04", block="litro", text="Garrafas de tamanhos diferentes não se comparam pela etiqueta. [p=0.2] Compare {a}o preço por litro: [p=0.2] quanto custa {b}um litro em cada garrafa."),
    dict(id="s05", block="litro", text="Dois litros por sete reais: {a}sete dividido por dois dá três reais e cinquenta por litro."),
    dict(id="s06", block="litro", text="Um litro e meio por cinco e quarenta: {a}cinco vírgula quatro dividido por um vírgula cinco. [p=0.3] Tire a vírgula do divisor, multiplicando cada número por dez: [p=0.2] {b}cinquenta e quatro dividido por quinze dá [p=0.2] {c}três reais e sessenta por litro."),
    dict(id="s07", block="litro", text="{a}Três e cinquenta contra três e sessenta. [p=0.3] A garrafa de dois litros custa mais na etiqueta, [p=0.2] mas {b}cada litro sai dez centavos mais barato. [p=0.3] A etiqueta diz o preço da garrafa. [p=0.2] O preço por litro diz {c}o preço do suco. [p=0.3] E isso só compensa {d}se você for usar todo o suco."),
    # embalagens de 4 e 6
    dict(id="s08", block="latas", text="Às vezes, a pergunta pede uma quantidade certa. [p=0.2] Você precisa de {a}dezesseis latas de refrigerante. [p=0.3] {b}O pacote de quatro custa dez reais. [p=0.2] {c}O de seis custa treze reais e oitenta. [p=0.3] Qual é a compra mais barata?"),
    dict(id="s09", block="latas", text="Primeiro, o preço por lata. [p=0.2] {a}Dez dividido por quatro dá dois e cinquenta. [p=0.2] {b}Treze e oitenta dividido por seis dá dois e trinta. [p=0.3] {c}O pacote de seis é o mais barato por lata."),
    dict(id="s10", block="latas", text="Mas dezesseis latas não fecham só com pacotes de seis. [p=0.2] Monte a tabela: {a}pacotes de seis, latas que faltam, pacotes de quatro e total."),
    dict(id="s11", block="latas", text="{a}Zero pacotes de seis: [p=0.2] faltam dezesseis, {b}quatro pacotes de quatro, quarenta reais. [p=0.3] {c}Um pacote de seis: [p=0.2] faltam dez, e dez latas {d}não fecham com pacotes de quatro. [p=0.2] Linha descartada."),
    dict(id="s12", block="latas", text="{a}Dois pacotes de seis: [p=0.2] faltam quatro, {b}um pacote de quatro. [p=0.3] {c}Duas vezes treze e oitenta dá vinte e sete e sessenta. [p=0.2] Mais dez: trinta e sete reais e sessenta centavos. [p=0.3] Três pacotes de seis já passam de dezesseis. [p=0.2] A melhor compra: {d}dois de seis e um de quatro."),
    # erro comum
    dict(id="s13", block="erro", text="O erro comum é parar no preço por lata. [p=0.2] A pessoa vê que o de seis é mais barato e leva {a}só pacotes de seis: três pacotes. [p=0.3] {b}Três vezes treze e oitenta dá quarenta e um reais e quarenta centavos, [p=0.2] e {c}duas latas sobrando. [p=0.3] Gastou mais e levou o que não precisava."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: [p=0.2] {a}comece pelo maior número possível da embalagem mais barata por unidade. [p=0.3] Se a conta fechar, {b}é a resposta. [p=0.2] Se não fechar, {c}tire um pacote e teste de novo."),
    dict(id="s15", block="atalho", text="Funciona porque cada lata no pacote de seis {a}custa menos. [p=0.3] Quanto mais latas vêm nele, menor a conta. [p=0.3] Não compensa quando o enunciado aceita sobra ou tem promoção: [p=0.2] aí, {b}faça a tabela inteira."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Você precisa de exatamente {a}vinte e duas garrafas de água. [p=0.3] {b}O pacote de quatro custa seis reais. [p=0.2] {c}O de seis custa oito reais e quarenta. [p=0.3] {d}Qual é a compra mais barata, e quanto custa?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Por garrafa: {a}seis dividido por quatro dá um e cinquenta. [p=0.2] {b}Oito e quarenta dividido por seis dá um e quarenta. [p=0.3] O pacote de seis ganha. [p=0.2] Pelo atalho, o máximo de pacotes de seis: {c}três, dezoito garrafas."),
    dict(id="s19", block="resposta", text="Faltam {a}quatro: um pacote de quatro. [p=0.2] Fechou. [p=0.3] {b}Três vezes oito e quarenta dá vinte e cinco e vinte. [p=0.2] {c}Mais seis: trinta e um reais e vinte centavos. [p=0.3] Confira outra linha: {d}um de seis e quatro de quatro dá trinta e dois e quarenta. [p=0.2] Mais caro."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}compare o preço por unidade, [p=0.2] {b}monte as opções que fecham a quantidade [p=0.2] e {c}escolha o menor total."),
    dict(id="s21", block="fim", text="Na próxima aula, você pratica tudo da trilha: [p=0.2] {a}ler enunciados longos, [p=0.2] {b}estimar o resultado [p=0.2] e {c}escolher a melhor opção. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
