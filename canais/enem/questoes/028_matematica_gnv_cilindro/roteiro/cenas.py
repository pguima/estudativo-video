# Estudativo · Questão 028 — ENEM 2025, 2º dia, caderno amarelo, questão 146: cilindros de GNV de 10, 14, 17, 21 e 25 m³,
# preço proporcional à capacidade; o carro roda 30 km por dia, 7 dias por semana, e gasta 1 m³ a cada 13 km. O cilindro
# mais barato que garante um só abastecimento semanal: 30 × 7 = 210 km; 210 ÷ 13 = 16,15... m³ (13 × 16 = 208, sobram 2 km)
# → precisa de mais de 16 m³ → o menor que serve é 17 → alternativa C. Conferência: 17 × 13 = 221 km ≥ 210.
# Pegadinhas: B (14) leva só 182 km (o gás acaba no 7º dia); A (10) leva 130 km (acaba no 5º dia); D e E servem, mas
# são mais caras.
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: leitura do enunciado (m³, "1 m³ a cada 13 km", preço proporcional) → A FERRAMENTA 1: proporção (1 → 13, 2 → 26,
# 3 → 39; gás = distância ÷ 13) → A FERRAMENTA 2: arredondar para cima (50 alunos em vans de 12 → 5 vans) → passo 1:
# 30 × 7 = 210 km → passo 2: 210 ÷ 13 ≈ 16,2 (mais de 16) → passo 3: o menor cilindro acima → 17 → conferência → C →
# por que as outras estão erradas → desafio → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: qual cilindro de GNV escolher? (proporção e arredondar para cima)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nas contas, fale devagar e com clareza, número por número. Faça as perguntas com "
            "curiosidade genuína, mostre surpresa na resposta e comemore o resultado. Respeite as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão cento e quarenta e seis do ENEM dois mil e vinte e cinco. [p=0.2] Uma pessoa vai instalar *gás "
        "natural* no carro. [p=0.3] {b}A loja tem cilindros de dez, catorze, dezessete, vinte e um [p=0.1] e vinte e "
        "cinco metros cúbicos, [p=0.1] e o preço é *proporcional* à capacidade. [p=0.3] {c}O carro roda *trinta "
        "quilômetros* por dia, [p=0.1] sete dias por semana, [p=0.1] e gasta *um metro cúbico* a cada *treze "
        "quilômetros.* [p=0.3] {d}Qual é o cilindro mais barato [p=0.1] que aguenta a semana inteira com um "
        "abastecimento só? [p=0.3] {e}Nessa aula, [p=0.1] você vai usar a *proporção* [p=0.1] e uma regra que pega "
        "muita gente: [p=0.1] quando *arredondar para cima.*"),
    dict(id="02", block="leitura", text=
        "{a}Antes das contas, [p=0.1] vamos traduzir o enunciado. [p=0.3] {b}*Metro cúbico* é uma medida de volume: "
        "[p=0.1] é quanto gás cabe no cilindro. [p=0.3] {c}*Um metro cúbico a cada treze quilômetros* [p=0.1] quer "
        "dizer que cada metro cúbico de gás [p=0.1] leva o carro por treze quilômetros. [p=0.3] {d}E *preço "
        "proporcional à capacidade* [p=0.1] quer dizer: [p=0.1] quanto maior o cilindro, [p=0.1] mais caro. [p=0.2] "
        "{e}Então o mais barato [p=0.1] é o *menor que dá conta.*"),
    dict(id="03", block="proporcao", text=
        "{a}Ferramenta um: [p=0.1] a *proporção.* [p=0.3] {b}Se um metro cúbico leva o carro por treze quilômetros, "
        "[p=0.1] dois metros cúbicos levam por *vinte e seis,* [p=0.2] {c}e três, [p=0.1] por *trinta e nove.* [p=0.3] "
        "{d}O gás e a distância crescem juntos, [p=0.1] na mesma razão. [p=0.3] {e}Então, para saber quanto gás uma "
        "distância precisa, [p=0.1] é só *dividir a distância por treze.*"),
    dict(id="04", block="arredondar", text=
        "{a}Ferramenta dois: [p=0.1] quando *arredondar para cima.* [p=0.3] {b}Cinquenta alunos vão viajar [p=0.1] em "
        "vans de *doze* lugares. [p=0.2] Cinquenta dividido por doze [p=0.1] dá quatro, [p=0.1] e sobram dois alunos. "
        "[p=0.3] {c}Quatro vans não bastam: [p=0.1] dois alunos ficariam para trás. [p=0.2] São *cinco* vans. [p=0.3] "
        "{d}Quando a conta decide se *cabe ou não cabe,* [p=0.1] qualquer sobra [p=0.1] obriga a subir para o próximo."),
    dict(id="05", block="semana", text=
        "{a}Passo um: [p=0.1] quantos quilômetros por semana? [p=0.3] {b}Trinta quilômetros por dia, [p=0.1] durante "
        "sete dias: [p=0.1] trinta vezes sete, [p=0.1] {c}*duzentos e dez quilômetros.*"),
    dict(id="06", block="gas", text=
        "{a}Passo dois: [p=0.1] quanto gás para duzentos e dez quilômetros? [p=0.3] {b}Pela proporção, [p=0.1] "
        "duzentos e dez dividido por treze. [p=0.3] {c}Treze vezes dezesseis [p=0.1] dá duzentos e oito. [p=0.2] "
        "Sobram *dois quilômetros.* [p=0.3] {d}Dá *dezesseis vírgula dois,* [p=0.1] mais ou menos. [p=0.2] E, como nas "
        "vans, [p=0.1] essa sobra conta: [p=0.1] precisa de *mais de dezesseis* metros cúbicos."),
    dict(id="07", block="escolha", text=
        "{a}Passo três: [p=0.1] qual cilindro escolher? [p=0.3] {b}O de dez e o de catorze [p=0.1] são *menores* que "
        "dezesseis vírgula dois: [p=0.1] o gás acaba antes do fim da semana. [p=0.3] {c}O de dezessete, [p=0.1] o de "
        "vinte e um [p=0.1] e o de vinte e cinco [p=0.1] *aguentam.* [p=0.3] {d}Como o preço cresce com a capacidade, "
        "[p=0.1] o mais barato entre eles [p=0.1] é o de *dezessete.*"),
    dict(id="08", block="resposta", text=
        "{a}Conferindo: [p=0.1] dezessete metros cúbicos [p=0.1] levam o carro por dezessete vezes treze, [p=0.1] "
        "*duzentos e vinte e um quilômetros.* [p=0.3] {b}A semana pede duzentos e dez. [p=0.2] Sobram onze "
        "quilômetros de folga. [p=0.3] {c}Alternativa *C.*"),
    dict(id="09", block="pegadinhas", text=
        "{a}E as outras? [p=0.3] {b}Catorze, [p=0.1] a *B,* [p=0.1] parece perto, [p=0.1] mas só leva o carro por "
        "cento e oitenta e dois quilômetros: [p=0.1] o gás acaba no *sétimo dia.* [p=0.3] {c}Dez, [p=0.1] a *A,* "
        "[p=0.1] leva só por cento e trinta: [p=0.1] acaba no *quinto dia.* [p=0.3] {d}Vinte e um e vinte e cinco "
        "[p=0.1] funcionam, [p=0.1] mas são *mais caros* [p=0.1] do que precisa."),
    dict(id="10", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}E se o carro rodasse *quarenta quilômetros* por dia? [p=0.2] Qual cilindro a "
        "pessoa escolheria? [p=0.3] {c}Deixe sua resposta nos comentários."),
    dict(id="11", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}A distância da semana: [p=0.1] a do dia vezes sete. [p=0.2] {c}O gás: "
        "[p=0.1] a distância dividida por treze. [p=0.2] {d}E o cilindro: [p=0.1] o *menor* que fica *acima* do "
        "resultado."),
    dict(id="12", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*razão e proporção,* [p=0.2] {c}*regra de três* [p=0.2] {d}e *divisão com resto.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
