# Estudativo · MAT-POT-003 — Multiplicar e dividir potências de mesma base (Matemática · Potências e Raízes).
# Habilidade: reduzir 2³ · 2⁴ a 2⁷ e 5⁷ ÷ 5⁴ a 5³ e explicar por que 7⁰ = 1.
# Pré-requisitos: MAT-NUM-009 (dividir por um algarismo), MAT-POT-001 (o que é potência). Próxima: MAT-POT-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sem fração, negativo, ordem das operações ou a palavra "fator": fora da ficha desta aula.
# 2³ · 2⁴ = 8 × 16 = 128 = 2⁷ (2¹² = 4.096 é o erro) · 5 · 5³ = 5⁴ · 5⁷ ÷ 5⁴ = 78.125 ÷ 625 = 125 · 7³ ÷ 7³ = 343 ÷ 343 = 1.
# Base diferente: 2³ · 3² = 8 × 9 = 72 · Soma: 2³ + 2⁴ = 8 + 16 = 24, não 128.
# Atalho: 16 × 32 = 2⁴ · 2⁵ = 2⁹ = 512. Questão: 3⁵ · 3² = 3⁷; 3⁷ ÷ 3⁷ = 3⁰ = 1.

TITULO = "Multiplicar e dividir potências de mesma base"

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
    dict(id="s01", block="gancho", text="{a}Sete elevado a zero. [p=0.3] Se você respondeu {b}zero, [p=0.2] está em boa companhia, e errou. [p=0.3] A resposta é {c}um. [p=0.2] E isso não é decreto: dá para provar."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você multiplica e divide potências {b}sem calcular nenhuma delas, [p=0.2] entende esse resultado [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}o expoente diz quantas vezes a base aparece na multiplicação, [p=0.2] e {c}a divisão desfaz a multiplicação. [p=0.3] Se faltar alguma, procure no canal."),
    # multiplicar
    dict(id="s04", block="vezes", text="Pense nas visualizações de um vídeo que {a}dobram todo dia. [p=0.3] Em {b}três dias, elas ficam multiplicadas por dois ao cubo. [p=0.3] Em mais {c}quatro dias, multiplicadas por dois elevado a quatro. [p=0.3] No total, {d}dois ao cubo vezes dois elevado a quatro."),
    dict(id="s05", block="vezes", text="Quantos dias foram? [p=0.2] Sete. [p=0.2] Então a conta tem que dar {a}dois elevado a sete. [p=0.3] Abra as potências para ver: [p=0.2] {b}dois vezes dois vezes dois, [p=0.2] {c}vezes dois vezes dois vezes dois vezes dois. [p=0.3] {d}O dois aparece sete vezes."),
    dict(id="s06", block="vezes", text="A regra: {a}multiplicando potências de mesma base, [p=0.2] {b}repete a base e soma os expoentes. [p=0.3] Número sem expoente conta como {c}expoente um, porque aparece uma vez. [p=0.2] {d}Cinco vezes cinco ao cubo é cinco elevado a quatro."),
    # dividir
    dict(id="s07", block="dividir", text="Dividir é o caminho de volta. [p=0.2] {a}Cinco elevado a sete dividido por cinco elevado a quatro. [p=0.3] Dividir por cinco {b}desfaz uma multiplicação por cinco. [p=0.2] Então {c}dividir por cinco elevado a quatro desfaz quatro de uma vez."),
    dict(id="s08", block="dividir", text="O cinco aparecia {a}sete vezes. [p=0.2] {b}Saem quatro. [p=0.2] {c}Sobram três. [p=0.2] Dá {d}cinco ao cubo, que é cento e vinte e cinco."),
    dict(id="s09", block="dividir", text="A regra: {a}dividindo potências de mesma base, [p=0.2] {b}repete a base e subtrai os expoentes. [p=0.3] Aqui, o primeiro expoente é maior ou igual ao segundo. [p=0.2] O outro caso é assunto de outra aula."),
    # expoente zero
    dict(id="s10", block="zero", text="Vamos à prova do começo. [p=0.2] Todo número dividido por ele mesmo dá um. [p=0.2] Então {a}sete ao cubo dividido por sete ao cubo {b}dá um."),
    dict(id="s11", block="zero", text="Pela regra, {a}repete a base e subtrai: [p=0.2] {b}três menos três dá zero. [p=0.2] Fica {c}sete elevado a zero. [p=0.3] Saíram todos os setes, mas o resultado não é zero: [p=0.2] a divisão já deu um. [p=0.3] A mesma conta não pode ter duas respostas. [p=0.2] Logo, {d}sete elevado a zero é um."),
    dict(id="s12", block="zero", text="Isso vale para {a}qualquer base, menos a base zero: [p=0.2] a prova divide a base por ela mesma, e não existe divisão por zero. [p=0.3] E faz sentido no vídeo: [p=0.2] {b}zero dias dobrando, e as visualizações ficam como estavam. [p=0.2] É {c}o mesmo que multiplicar por um."),
    # só mesma base
    dict(id="s13", block="base", text="Cuidado: {a}essas regras só valem com a mesma base. [p=0.3] Veja {b}dois ao cubo vezes três ao quadrado. [p=0.2] O dois e o três se repetem cada um por si, e {c}nada se junta. [p=0.3] {d}Calcule cada potência: [p=0.2] {e}oito vezes nove dá setenta e dois."),
    dict(id="s14", block="base", text="E só valem para {a}vezes e dividido. [p=0.3] {b}Dois ao cubo mais dois elevado a quatro é oito mais dezesseis: [p=0.2] {c}vinte e quatro. [p=0.3] Dois elevado a sete daria {d}cento e vinte e oito."),
    # erro
    dict(id="s15", block="erro", text="O erro comum é {a}multiplicar os expoentes: [p=0.2] escrever dois ao cubo vezes dois elevado a quatro igual a {b}dois elevado a doze. [p=0.3] Abra e conte. [p=0.2] O dois aparece {c}três vezes e depois quatro vezes. [p=0.2] Isso dá {d}sete vezes, não doze."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}a escada do dois. [p=0.3] {b}Dois. [p=0.2] {c}Quatro. [p=0.2] {d}Oito. [p=0.2] {e}Dezesseis. [p=0.2] {f}Trinta e dois. [p=0.3] Cada degrau é {g}um expoente. [p=0.3] Para fazer {h}dezesseis vezes trinta e dois de cabeça, [p=0.2] veja os degraus: {i}dezesseis é o degrau quatro [p=0.2] e {j}trinta e dois é o degrau cinco."),
    dict(id="s17", block="atalho", text="{a}Quatro mais cinco dá nove. [p=0.2] Suba até {b}o degrau nove: [p=0.2] {c}sessenta e quatro. [p=0.2] {d}Cento e vinte e oito. [p=0.2] {e}Duzentos e cinquenta e seis. [p=0.2] {f}Quinhentos e doze."),
    dict(id="s18", block="atalho", text="Funciona porque é {a}a regra de somar expoentes, disfarçada. [p=0.3] {b}Só compensa com números da escada. [p=0.2] Em {c}dezoito vezes trinta e dois, o dezoito não é degrau: {d}arme a conta."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Escreva como uma potência só: {a}três elevado a cinco vezes três ao quadrado. [p=0.3] Depois, divida {b}esse resultado por três elevado a sete. [p=0.3] {c}Quanto dá no fim?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Multiplicando, soma: {a}cinco mais dois dá sete. [p=0.2] {b}Três elevado a sete. [p=0.3] Dividindo, subtrai: {c}sete menos sete dá zero. [p=0.2] {d}Três elevado a zero: [p=0.2] {e}um. [p=0.3] Faz sentido: você dividiu um número por ele mesmo."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}na mesma base, [p=0.2] {b}vezes soma os expoentes, [p=0.2] {c}dividido subtrai, [p=0.2] e {d}expoente zero dá um."),
    dict(id="s23", block="fim", text="Na próxima aula, aparece {a}potência de potência [p=0.2] e {b}potência de uma multiplicação, [p=0.2] e você escreve {c}números grandes como potências. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
