# Estudativo · MAT-EST-013 — Qual medida usar (Matemática · Estatística · Mediana, moda e dispersão).
# Habilidade: explicar por que um salário muito alto puxa a média e quase não muda a mediana e escolher a medida certa para cada caso.
# Pré-requisitos: MAT-EST-011 (moda e mediana). Usa MAT-EST-008 (média; total = média × quantidade) e MAT-EST-001 (variável qualitativa). Próxima: MAT-EST-014.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Empresa fictícia; salários só como exemplo, sem valor real atual.
# Dados (tela): 10 funcionários: 4 × R$ 2.000, 3 × R$ 2.500, 2 × R$ 3.000, 1 × R$ 21.000 (diretor).
#   Soma 8 000 + 7 500 + 6 000 + 21 000 = 42 500; média 4 250. Em ordem, 5º e 6º = 2 500 → mediana 2 500. Moda 2 000.
#   9 de 10 ganham até 3 000. Diretor vai a 41 000: soma 62 500; média 6 250 (subiu 2 000); mediana 2 500 (igual).
#   Erro: tirar o diretor → 21 500/9 ≈ 2 388,89 (conta não citada em voz; só "jogar fora um dado real").
#   Questão: calçados → moda; casas com mansão → mediana; guardar o mesmo valor por mês para pagar a luz do ano → média (total do ano ÷ 12).
# Visual:
#   s01: placa "salário médio R$ 4.250"; dez bonequinhos, nove com sacos pequenos e um com saco enorme.
#   s04-s06: E.colunas com os dez salários; linha da média puxada para cima; marcador da mediana parado no meio.
#   s07: coluna do diretor cresce para 41 000; média sobe para 6 250; mediana não se mexe.
#   s08-s10: três cartões: média (gangorra), mediana (meio da fila), moda (o mais comum).
#   s13-s14: placas de pista ("metade ganha até", "mais vendido", "total do ano") ligadas às medidas.

TITULO = "Qual medida usar: média, mediana ou moda"

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
    dict(id="s01", block="gancho", text="{a}Numa empresa, o salário médio é de quatro mil duzentos e cinquenta reais. [p=0.3] Parece bom. [p=0.2] Mas {b}nove dos dez funcionários ganham até três mil. [p=0.3] A conta está certa. [p=0.2] Só que {c}a média não era a medida certa para essa pergunta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você sabe quando usar média, mediana ou moda [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três medidas: [p=0.2] {b}a média aritmética, que é a soma dividida pela quantidade; [p=0.2] {c}a mediana, o valor do meio com os dados em ordem; [p=0.2] e {d}a moda, o valor que mais aparece. [p=0.3] Se faltar alguma, procure no canal."),
    # o exemplo
    dict(id="s04", block="salarios", text="Os salários estão na tela. [p=0.2] {a}Quatro pessoas ganham dois mil reais. [p=0.2] {b}Três ganham dois mil e quinhentos. [p=0.2] {c}Duas ganham três mil. [p=0.2] E o diretor ganha {d}vinte e um mil."),
    dict(id="s05", block="salarios", text="{a}A soma dá quarenta e dois mil e quinhentos. [p=0.2] {b}Dividida por dez pessoas, dá quatro mil duzentos e cinquenta. [p=0.3] Agora a mediana. [p=0.2] Com dez salários em ordem, olhe {c}o quinto e o sexto: dois mil e quinhentos. [p=0.3] E a moda: {d}dois mil, o salário mais comum."),
    dict(id="s06", block="salarios", text="Por que a média ficou tão alta? [p=0.2] Porque ela {a}soma todos os valores. [p=0.2] O salário do diretor entra inteiro na soma [p=0.2] e {b}puxa a média para cima. [p=0.3] Já a mediana só olha {c}a posição. [p=0.2] O diretor é só mais um na ponta da fila."),
    dict(id="s07", block="salarios", text="Veja o teste. [p=0.2] O diretor ganha um aumento e vai para {a}quarenta e um mil. [p=0.3] {b}A média sobe para seis mil duzentos e cinquenta. [p=0.3] {c}A mediana continua dois mil e quinhentos. [p=0.2] O quinto e o sexto da fila não mudaram."),
    # quando usar cada uma
    dict(id="s08", block="quando", text="Então, quando usar cada uma? [p=0.2] {a}A média, quando importa o total, [p=0.2] porque {b}média vezes quantidade dá o total. [p=0.2] E quando os dados não têm valores muito fora do padrão."),
    dict(id="s09", block="quando", text="{a}A mediana, quando há valores extremos, [p=0.2] como salários, preços de imóveis e tempo de espera. [p=0.3] Ela responde {b}quanto ganha quem está no meio da fila."),
    dict(id="s10", block="quando", text="{a}A moda, quando a pergunta é o mais comum: [p=0.2] o tamanho de roupa que mais sai, o sabor mais pedido. [p=0.3] E ela é {b}a única das três que funciona com dado que não é número, como cor ou sabor."),
    # erro
    dict(id="s11", block="erro", text="Um erro comum: [p=0.2] {a}jogar fora o salário do diretor [p=0.2] para a média ficar mais justa. [p=0.3] Não pode. [p=0.2] {b}Ele é um dado real da empresa. [p=0.2] A saída não é apagar o dado: [p=0.2] é {c}escolher a medida que não se deixa puxar, a mediana."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: [p=0.2] {a}compare a média com a mediana. [p=0.3] Se a média ficou {b}bem acima da mediana, [p=0.2] tem valor muito alto puxando para cima. [p=0.2] Se ficou {c}bem abaixo, tem valor muito baixo puxando para baixo. [p=0.3] Funciona porque só a média sente os valores das pontas. [p=0.2] Diferença pequena não prova nada: [p=0.2] aí, olhe os dados."),
    dict(id="s13", block="atalho", text="E o enunciado costuma dar pistas. [p=0.2] {a}Metade ganha até, ou valor central, pede mediana. [p=0.2] {b}Mais comum ou mais vendido pede moda. [p=0.2] {c}Dividir o total igualmente pede média."),
    dict(id="s14", block="atalho", text="Mas a palavra é só pista. [p=0.2] {a}Quem decide é a situação. [p=0.3] Na dúvida, pergunte: [p=0.2] {b}eu preciso do total, do meio ou do mais comum?"),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Diga a medida certa para cada caso. [p=0.3] {a}Caso um: uma loja de calçados vai repor o estoque e quer saber o número que mais sai. [p=0.3] {b}Caso dois: um site quer mostrar o preço típico das casas de um bairro, que tem uma mansão. [p=0.3] {c}Caso três: uma família quer guardar o mesmo valor todo mês [p=0.2] para que, no fim do ano, o dinheiro guardado pague todas as contas de luz."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Caso um: moda. [p=0.2] A loja quer o número mais comum, e não um tamanho quebrado no meio do caminho. [p=0.3] {b}Caso dois: mediana. [p=0.2] A mansão puxaria a média para cima, e o preço pareceria mais alto do que é para a maioria."),
    dict(id="s18", block="resposta", text="{a}Caso três: média. [p=0.2] O valor guardado por mês, vezes doze meses, precisa dar o total das contas do ano: [p=0.2] {b}é o total dividido igualmente pelos doze meses. [p=0.3] Aqui, o mês mais caro precisa entrar na conta."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.2] {a}a média sente cada valor, [p=0.2] {b}a mediana só sente a posição [p=0.2] e {c}a moda mostra o mais comum."),
    dict(id="s20", block="fim", text="Na próxima aula, você corta os dados {a}em quatro partes, em vez de duas. [p=0.2] São {b}os quartis, [p=0.2] e você vai entender o que quer dizer {c}ficar no percentil noventa de uma prova. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
