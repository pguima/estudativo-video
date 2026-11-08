# Estudativo · MAT-POR-009 — Praticando: porcentagem, aumentos e lucro (Matemática · Porcentagem · prática).
# Habilidade: calcular porcentagens, preços, descontos e margens em problemas de compra e venda.
# Pré-requisitos: MAT-POR-001, MAT-POR-002, MAT-POR-003, MAT-POR-004, MAT-POR-005, MAT-POR-014, MAT-POR-006, MAT-POR-007, MAT-POR-008. Próxima: MAT-POR-010.
# Questões inéditas, criadas para esta aula. Variações sucessivas ainda não foram ensinadas (MAT-POR-010).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: porcentagem, aumentos e lucro"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações de compra e venda, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}os fatores de aumento e de desconto, [p=0.2] {b}a parte dividida pelo total, [p=0.2] {c}o preço de antes, dividindo pelo fator, [p=0.2] e {d}o lucro sobre o custo ou sobre a venda. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: desconto
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma geladeira custa {b}dois mil e quatrocentos reais. [p=0.2] À vista, tem {c}quinze por cento de desconto. [p=0.3] {d}Quanto você paga à vista?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Tirar quinze por cento é ficar com oitenta e cinco: {a}fator zero vírgula oitenta e cinco. [p=0.2] {b}Dois mil e quatrocentos vezes zero vírgula oitenta e cinco: [p=0.1] {c}dois mil e quarenta reais."),
    # atalho
    dict(id="s06", block="atalho", text="Dá para fazer de cabeça, com o atalho do {a}dez mais cinco. [p=0.2] {b}Dez por cento de dois mil e quatrocentos: duzentos e quarenta. [p=0.2] {c}Cinco por cento é a metade: cento e vinte. [p=0.2] Desconto de {d}trezentos e sessenta. [p=0.2] {e}Dois mil e quatrocentos menos trezentos e sessenta dá dois mil e quarenta."),
    dict(id="s07", block="atalho", text="Funciona porque {a}dez por cento é só andar a vírgula uma casa, [p=0.2] e cinco é a metade disso. [p=0.3] Não compensa com {b}porcentagens quebradas, como trinta e sete por cento: [p=0.2] aí, {c}use o fator."),
    # situação 2: variação
    dict(id="s08", block="questao2", text="{a}Situação dois. [p=0.2] O aluguel passou de {b}mil duzentos e cinquenta reais [p=0.2] para {c}mil e quatrocentos. [p=0.3] {d}De quantos por cento foi o aumento?"),
    dict(id="s09", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="resposta2", text="Vamos lá. [p=0.2] O aumento foi de {a}cento e cinquenta reais. [p=0.2] Ele vai em cima, e {b}o valor de antes, mil duzentos e cinquenta, vai embaixo. [p=0.3] Simplifique por cinquenta: {c}três vinte e cinco avos. [p=0.2] Multiplique em cima e embaixo por quatro: {d}doze centésimos. [p=0.2] {e}Doze por cento."),
    dict(id="s11", block="resposta2", text="Se você dividiu por mil e quatrocentos, {a}usou o valor novo. [p=0.2] O valor de antes é sempre o cem por cento. [p=0.2] No erro relativo, a conta é a mesma: [p=0.2] {b}o erro dividido pela medida."),
    # situação 3: preço de antes
    dict(id="s12", block="questao3", text="{a}Situação três. [p=0.2] Na liquidação, com {b}trinta e cinco por cento de desconto, [p=0.2] uma jaqueta saiu por {c}cento e dezessete reais. [p=0.3] {d}Qual era o preço sem desconto?"),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] Com trinta e cinco por cento de desconto, o fator é {a}zero vírgula sessenta e cinco. [p=0.2] Preço de antes: {b}cento e dezessete dividido por zero vírgula sessenta e cinco. [p=0.2] Duas casas: {c}onze mil e setecentos dividido por sessenta e cinco."),
    dict(id="s15", block="resposta3", text="{a}Cento e dezessete dividido por sessenta e cinco dá um, e sobram cinquenta e dois. [p=0.2] {b}Quinhentos e vinte dividido por sessenta e cinco dá oito, e não sobra nada. [p=0.2] Com o último zero, {c}cento e oitenta reais. [p=0.3] Quem somou trinta e cinco por cento a cento e dezessete achou {d}cento e cinquenta e sete reais e noventa e cinco centavos, e errou."),
    # situação 4: lucro
    dict(id="s16", block="questao4", text="{a}Situação quatro. [p=0.2] Uma doceira gasta {b}dois reais e cinquenta centavos em cada bolo de pote [p=0.2] e vende por {c}quatro reais. [p=0.3] {d}Qual é a margem de lucro sobre o custo? [p=0.2] {e}E sobre a venda?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] Lucro: {a}quatro reais menos dois reais e cinquenta centavos dá um real e cinquenta centavos. [p=0.3] Sobre o custo: {b}um vírgula cinco dividido por dois vírgula cinco. [p=0.2] Sem as vírgulas, {c}quinze vinte e cinco avos, que simplifica para três quintos: {d}sessenta por cento."),
    dict(id="s19", block="resposta4", text="Sobre a venda: {a}um vírgula cinco dividido por quatro dá [p=0.1] {b}zero vírgula trezentos e setenta e cinco. [p=0.2] São {c}trinta e sete vírgula cinco por cento. [p=0.3] Mesmo lucro, {d}totais diferentes."),
    # situação 5: promoção
    dict(id="s20", block="questao5", text="{a}Última situação. [p=0.2] Você precisa de cinco latas de tinta. [p=0.2] Uma loja faz {b}leve cinco, pague três. [p=0.2] Outra dá {c}quarenta e cinco por cento de desconto. [p=0.3] {d}Qual compensa mais?"),
    dict(id="s21", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta5", text="Vamos lá. [p=0.2] Leve cinco, pague três: {a}saem duas latas de graça em cinco. [p=0.2] {b}Dois quintos, quarenta por cento de desconto. [p=0.3] {c}Quarenta é menos que quarenta e cinco: [p=0.2] {d}o desconto de quarenta e cinco por cento compensa mais. [p=0.3] Quem dividiu pelas três latas pagas achou {e}cerca de sessenta e sete por cento, e errou."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}ache o total certo antes de dividir, [p=0.2] {b}use o fator para ir e voltar [p=0.2] e {c}confira se a resposta faz sentido."),
    dict(id="s24", block="fim", text="Na próxima aula, você vê o que acontece com {a}dois aumentos seguidos. [p=0.2] {b}Dez por cento e depois vinte por cento não dão trinta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
