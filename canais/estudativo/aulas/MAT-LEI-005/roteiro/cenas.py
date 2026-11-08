# Estudativo · MAT-LEI-005 — Conta por faixas (Matemática · Leitura de Problemas).
# Habilidade: calcular a conta de 24 m³ de água com preços diferentes por faixa.
# Pré-requisitos: MAT-FRA-016 (multiplicar decimais), MAT-LEI-001 (pergunta e dados úteis). Próxima: MAT-LEI-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Tabela de preços inventada para a aula (não é tarifa real). Visual: tabela de três faixas e barra de 24 m³ cortada em 10 + 10 + 4.

TITULO = "Conta por faixas"

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
    dict(id="s01", block="gancho", text="Uma casa gastou {a}vinte e quatro metros cúbicos de água no mês. [p=0.3] Se você calculou {b}cento e noventa e seis reais e oitenta centavos, [p=0.2] cobrou {c}quase oitenta reais a mais do que o certo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula qualquer conta cobrada por faixas, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas: [p=0.2] {a}multiplicar números com vírgula [p=0.2] e {b}ler a pergunta antes do texto. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é metro cúbico e faixa
    dict(id="s04", block="faixas", text="Antes, a unidade. [p=0.2] Água se mede em {a}metro cúbico: [p=0.2] o que cabe numa caixa com {b}um metro de largura, de comprimento e de altura. [p=0.3] São {c}mil litros."),
    dict(id="s05", block="faixas", text="Muitas contas de água são cobradas {a}por faixas. [p=0.3] Quanto mais você gasta, mais caro fica cada metro cúbico, [p=0.2] mas só {b}a parte que passou de cada limite. [p=0.3] Veja uma tabela inventada para esta aula."),
    dict(id="s06", block="faixas", text="{a}Os primeiros dez metros cúbicos: três reais e cinquenta centavos cada. [p=0.3] {b}Os dez seguintes: cinco reais cada. [p=0.3] {c}O que passar de vinte: oito reais e vinte centavos cada."),
    # 24 m³
    dict(id="s07", block="conta", text="Agora os vinte e quatro metros cúbicos. [p=0.2] A pergunta quer {a}o valor da conta, em reais. [p=0.2] O segredo é {b}cortar o consumo nas faixas. [p=0.3] {c}Dez na primeira, [p=0.2] {d}dez na segunda, [p=0.2] e sobram {e}quatro na terceira. [p=0.3] Dez mais dez mais quatro: vinte e quatro. [p=0.2] Fecha."),
    dict(id="s08", block="conta", text="Primeira faixa: {a}dez vezes três e cinquenta dá trinta e cinco reais. [p=0.3] Segunda faixa: {b}dez vezes cinco dá cinquenta reais."),
    dict(id="s09", block="conta", text="Terceira faixa: {a}quatro vezes oito vírgula dois. [p=0.2] Sem a vírgula, {b}quatro vezes oitenta e dois dá trezentos e vinte e oito. [p=0.2] Com uma casa, {c}trinta e dois vírgula oito: [p=0.2] trinta e dois reais e oitenta centavos."),
    dict(id="s10", block="conta", text="Some as faixas: {a}trinta e cinco mais cinquenta mais trinta e dois e oitenta. [p=0.3] A conta é de {b}cento e dezessete reais e oitenta centavos."),
    dict(id="s11", block="conta", text="E quem gastou só {a}sete metros cúbicos? [p=0.2] Fica tudo na primeira faixa: [p=0.2] {b}sete vezes três e cinquenta dá vinte e quatro reais e cinquenta centavos. [p=0.3] Cobrar assim faz quem gasta pouco pagar menos por metro cúbico, [p=0.2] e {c}pesa no bolso de quem gasta muito."),
    # erro comum
    dict(id="s12", block="erro", text="E os cento e noventa e seis e oitenta do começo? [p=0.2] A pessoa olhou o consumo, viu que passou de vinte, [p=0.2] e cobrou {a}tudo pelo preço mais caro: [p=0.2] {b}vinte e quatro vezes oito e vinte."),
    dict(id="s13", block="erro", text="Só que o preço de oito e vinte vale {a}só para os quatro metros cúbicos depois do vinte. [p=0.3] Os primeiros vinte continuam com {b}o preço das faixas de baixo. [p=0.3] Passar de uma faixa {c}não muda o preço do que veio antes. [p=0.3] Quem vai de vinte para {d}vinte e um metros cúbicos paga só {e}mais oito reais e vinte centavos, [p=0.2] e não a conta inteira pelo preço mais caro."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: [p=0.2] {a}faixa cheia vira valor fixo. [p=0.3] Quem passa de vinte sempre paga {b}trinta e cinco mais cinquenta dá oitenta e cinco reais, pelos primeiros vinte. [p=0.3] Depois, só calcula {c}o que passou."),
    dict(id="s15", block="atalho", text="Funciona porque as faixas de baixo {a}são iguais para todo mundo que passa delas. [p=0.3] Você faz essa conta uma vez e reaproveita. [p=0.3] Não compensa quando o consumo {b}fica dentro da primeira faixa: [p=0.2] aí, é uma multiplicação só."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar, com a mesma tabela. [p=0.2] Uma casa gastou {a}trinta e um metros cúbicos no mês. [p=0.3] {b}Quanto vai pagar?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá, pelo atalho. [p=0.2] Os primeiros vinte: {a}oitenta e cinco reais. [p=0.3] Passou de vinte: {b}trinta e um menos vinte dá onze metros cúbicos."),
    dict(id="s19", block="resposta", text="{a}Onze vezes oito vírgula dois. [p=0.2] Sem a vírgula, {b}onze vezes oitenta e dois dá novecentos e dois. [p=0.2] Com uma casa, {c}noventa reais e vinte centavos. [p=0.3] Total: {d}oitenta e cinco mais noventa e vinte dá cento e setenta e cinco reais e vinte centavos."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo a aula: {a}corte o consumo nas faixas, [p=0.2] {b}cada pedaço com o seu próprio preço, [p=0.2] e {c}some os pedaços no fim da conta."),
    dict(id="s21", block="fim", text="Na próxima aula, você aprende a {a}escolher a melhor opção: [p=0.2] comparar {b}o preço por litro [p=0.2] e montar {c}a compra mais barata com embalagens de tamanhos diferentes. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
