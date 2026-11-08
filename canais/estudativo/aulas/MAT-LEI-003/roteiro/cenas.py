# Estudativo · MAT-LEI-003 — Desenhar o problema: barras e tabelas (Matemática · Leitura de Problemas).
# Habilidade: resolver um problema de frações com barras e organizar opções numa tabela em vez de montar equação.
# Pré-requisitos: MAT-EQU-002 (valor numérico), MAT-FRA-010 (fração do restante), MAT-LEI-001 (pergunta e dados úteis). Próxima: MAT-LEI-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Visual: barra dividida em partes iguais (cinco partes; depois uma barra de um bloco e outra de três) e tabela de casos.

TITULO = "Desenhar o problema: barras e tabelas"

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
    dict(id="s01", block="gancho", text="Uma pessoa gastou {a}dois quintos do salário [p=0.2] e ainda ficou com {b}seiscentos reais. [p=0.3] Qual é o salário? [p=0.3] Muita gente acha que precisa de equação. [p=0.2] Basta {c}um desenho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve problemas desenhando barras e montando tabelas, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de três coisas: [p=0.2] {a}leia a pergunta primeiro, [p=0.2] {b}antes de cada fração, pergunte fração de quê, [p=0.2] e {c}troque a letra pelo número para calcular. [p=0.3] Se faltar alguma, procure no canal."),
    # barras: parte para o total
    dict(id="s04", block="barra1", text="Desenhe o salário como {a}uma barra. [p=0.2] Quintos? Então corte em {b}cinco partes iguais. [p=0.3] {c}Pinte duas: é o que ela gastou. [p=0.2] Sobram {d}três partes."),
    dict(id="s05", block="barra1", text="E o texto diz quanto sobrou: {a}seiscentos reais. [p=0.3] Então três partes valem seiscentos. [p=0.2] {b}Seiscentos dividido por três dá duzentos: [p=0.2] cada parte vale duzentos reais."),
    dict(id="s06", block="barra1", text="O salário são cinco partes: {a}cinco vezes duzentos dá mil reais. [p=0.3] Confira: {b}dois quintos de mil, quatrocentos. [p=0.2] {c}Mil menos quatrocentos dá seiscentos. [p=0.2] Bateu."),
    # barras: comparação
    dict(id="s07", block="barra2", text="A barra também serve para comparar. [p=0.2] Pedro tem {a}o triplo da idade do filho. [p=0.2] Somadas, as idades dão {b}quarenta e oito anos. [p=0.3] Qual é a idade de cada um?"),
    dict(id="s08", block="barra2", text="O filho é {a}um bloco. [p=0.2] O Pedro, triplo, são {b}três blocos iguais a esse. [p=0.3] Ao todo, {c}quatro blocos valem quarenta e oito. [p=0.2] {d}Quarenta e oito dividido por quatro dá doze. [p=0.3] O filho tem {e}doze anos, e o Pedro, {f}trinta e seis."),
    dict(id="s09", block="barra2", text="Repare: ninguém montou equação. [p=0.2] Equação é assunto de outra aula. [p=0.3] O desenho mostra {a}quantas partes iguais existem, [p=0.2] e a conta vira uma divisão. [p=0.3] No salário, se o texto desse a parte gasta, o caminho seria o mesmo: [p=0.2] {b}duas partes valem quatrocentos, [p=0.2] cada parte vale duzentos, [p=0.2] e o salário continua {c}mil reais."),
    # tabela de casos
    dict(id="s10", block="tabela", text="Quando há poucas opções, outra ferramenta resolve: {a}a tabela. [p=0.3] Num estacionamento há {b}dez veículos, entre carros e motos. [p=0.2] Ao todo, são {c}trinta e duas rodas. [p=0.3] Quantos carros há?"),
    dict(id="s11", block="tabela", text="Monte colunas: {a}carros, motos e rodas. [p=0.3] Cada linha é um palpite. [p=0.2] As rodas são {b}quatro vezes os carros mais duas vezes as motos. [p=0.3] Zero carros e dez motos: {c}vinte rodas. [p=0.2] Um carro e nove motos: {d}vinte e duas."),
    dict(id="s12", block="tabela", text="Repare no padrão: {a}cada carro no lugar de uma moto soma duas rodas. [p=0.3] De vinte até trinta e duas, faltam {b}doze rodas. [p=0.2] Doze dividido por dois: {c}seis carros. [p=0.3] Você pulou quatro linhas da tabela [p=0.2] e não montou equação nenhuma."),
    dict(id="s13", block="tabela", text="Confira na linha: {a}seis carros e quatro motos. [p=0.2] {b}Seis vezes quatro dá vinte e quatro. [p=0.2] {c}Quatro vezes dois dá oito. [p=0.2] {d}Trinta e duas rodas. [p=0.2] Bateu."),
    # erro comum
    dict(id="s14", block="erro", text="Agora, o erro comum. [p=0.2] Voltando ao salário: a pessoa calcula {a}dois quintos de seiscentos, duzentos e quarenta, [p=0.2] e soma: {b}oitocentos e quarenta reais."),
    dict(id="s15", block="erro", text="Mas seiscentos não é o salário. [p=0.2] É {a}a parte que sobrou. [p=0.3] Os dois quintos são do salário inteiro, que ainda era desconhecido. [p=0.2] A barra mostra isso na hora: {b}seiscentos ocupa três partes, não cinco."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho da tabela: {a}não preencha linha por linha. [p=0.3] Monte {b}a primeira linha, [p=0.2] veja {c}quanto cada troca muda, [p=0.2] e {d}pule direto para a resposta."),
    dict(id="s17", block="atalho", text="Funciona porque cada troca muda {a}sempre o mesmo tanto. [p=0.3] Não compensa quando a mudança não é igual a cada linha, [p=0.2] como num preço que fica mais barato a partir de certa quantidade. [p=0.2] Aí, {b}preencha a tabela com calma."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Um caixa tem {a}doze notas, [p=0.1] umas de cinco reais e outras de dez. [p=0.2] O total é {b}oitenta e cinco reais. [p=0.3] {c}Quantas notas de dez há no caixa?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá, pela tabela. [p=0.2] Primeira linha: {a}doze notas de cinco, sessenta reais. [p=0.3] Cada nota de cinco trocada por uma de dez {b}soma cinco reais. [p=0.2] De sessenta até oitenta e cinco, faltam {c}vinte e cinco."),
    dict(id="s21", block="resposta", text="{a}Vinte e cinco dividido por cinco dá cinco trocas. [p=0.2] São {b}cinco notas de dez [p=0.1] e {c}sete de cinco. [p=0.3] Confira: {d}cinquenta mais trinta e cinco dá oitenta e cinco. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}fração vira barra de partes iguais, [p=0.2] {b}opções viram tabela, [p=0.2] e {c}a última linha sempre é conferida."),
    dict(id="s23", block="fim", text="Na próxima aula, você aprende a {a}estimar contas e quantidades, [p=0.2] como saber, sem calcular tudo, {b}quantas vezes seu coração já bateu. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
