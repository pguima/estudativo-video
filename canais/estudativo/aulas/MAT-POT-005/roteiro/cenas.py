# Estudativo · MAT-POT-005 — Expoente negativo e potências de 10 (Matemática · Potências e Raízes).
# Habilidade: escrever 2⁻³ como 1/8 e 10⁻³ como 0,001, contando zeros e casas decimais.
# Pré-requisitos: MAT-FRA-016 (andar com a vírgula), MAT-POT-002 (potência de negativo, fração ou decimal), MAT-POT-003 (mesma base). Próxima: MAT-POT-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sem potência de potência: MAT-POT-004 não está na ficha desta aula. Sem converter 1/8 em decimal (MAT-FRA-015 fora da ficha).
# 2³ ÷ 2⁶ = 8 ÷ 64 = 1/8 = 2⁻³ · escada 8, 4, 2, 1, 1/2, 1/4, 1/8 · 3⁻² = 1/9 · 10³ = 1.000 · 10⁶ = 1.000.000 · 10⁰ = 1 · 10⁻³ = 1/1.000 = 0,001 · 10⁻² = 0,01.
# Atalho: 10⁻⁶ = 0,000001 (6 zeros contando o de antes da vírgula; 6 casas).
# Questão: 5³ ÷ 5⁵ = 5⁻² = 1/25 (125 ÷ 3.125) · 10⁻⁵ = 0,00001.

TITULO = "Expoente negativo e potências de 10"

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
    dict(id="s01", block="gancho", text="{a}Dois elevado a menos três. [p=0.3] Se você pensou {b}menos oito, [p=0.2] caiu na armadilha. [p=0.3] O resultado nem é negativo. [p=0.2] É {c}um oitavo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você transforma expoente negativo em fração, [p=0.2] escreve {b}potências de dez contando zeros e casas [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}três coisas: [p=0.2] {b}dividindo potências de mesma base, subtrai os expoentes, [p=0.2] {c}o traço da fração é uma divisão [p=0.2] e {d}andar com a vírgula. [p=0.3] Se faltar alguma, procure no canal."),
    # sai da divisão
    dict(id="s04", block="divisao", text="De onde vem um expoente negativo? [p=0.2] Da {a}divisão. [p=0.3] Até aqui, o primeiro expoente nunca era menor que o segundo. [p=0.2] Falta esse caso: {b}dois ao cubo dividido por dois elevado a seis."),
    dict(id="s05", block="divisao", text="Pela regra, {a}repete a base e subtrai: [p=0.2] três menos seis dá {b}menos três. [p=0.2] Fica {c}dois elevado a menos três. [p=0.3] Mas o que isso quer dizer?"),
    dict(id="s06", block="divisao", text="Faça a mesma conta de outro jeito. [p=0.2] O traço é divisão, então escreva {a}dois ao cubo em cima e dois elevado a seis embaixo. [p=0.3] Abra: {b}em cima, o dois aparece três vezes. [p=0.2] {c}Embaixo, seis vezes. [p=0.3] {d}Divida em cima e embaixo por dois ao cubo."),
    dict(id="s07", block="divisao", text="Em cima fica {a}um. [p=0.2] Embaixo, o dois {b}ainda aparece três vezes: dois ao cubo, que é oito. [p=0.3] A conta é a mesma, então {c}dois elevado a menos três é um oitavo. [p=0.3] A regra: {d}expoente negativo vira fração, com um em cima e a potência de expoente positivo embaixo."),
    dict(id="s08", block="divisao", text="Veja outra: {a}três elevado a menos dois. [p=0.2] Um em cima, {b}três ao quadrado embaixo: [p=0.2] {c}um nono."),
    # escada
    dict(id="s09", block="escada", text="Essa fração também aparece em uma escada. [p=0.2] {a}Oito é dois ao cubo. [p=0.2] {b}Quatro é dois ao quadrado. [p=0.2] {c}Dois é dois elevado a um. [p=0.2] {d}Um é dois elevado a zero. [p=0.3] Cada degrau {e}divide por dois."),
    dict(id="s10", block="escada", text="Continue descendo. [p=0.2] {a}Expoente menos um: um meio. [p=0.2] {b}Expoente menos dois: um quarto. [p=0.2] {c}Expoente menos três: um oitavo. [p=0.3] O mesmo resultado, sem nenhuma regra nova."),
    # base dez
    dict(id="s11", block="dez", text="Com base dez, tudo vira contagem. [p=0.2] Expoente positivo conta {a}zeros. [p=0.2] {b}Dez ao cubo é mil: três zeros. [p=0.2] {c}Dez elevado a seis é um milhão: seis zeros. [p=0.2] {d}Dez elevado a zero é um: nenhum zero."),
    dict(id="s12", block="dez", text="Expoente negativo conta {a}casas depois da vírgula. [p=0.3] {b}Dez elevado a menos três é um dividido por dez ao cubo: [p=0.2] {c}um milésimo. [p=0.3] Mil tem três zeros, então {d}a vírgula anda três casas para a esquerda: [p=0.2] {e}zero vírgula zero zero um."),
    dict(id="s13", block="dez", text="São {a}três casas, com o um na última. [p=0.3] Repare: depois da vírgula, são dois zeros e o um. [p=0.2] Quem conta só os zeros depois da vírgula erra. [p=0.2] {b}Dez elevado a menos dois tem duas casas: [p=0.2] {c}zero vírgula zero um."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é o do começo: {a}achar que expoente negativo deixa o número negativo. [p=0.3] Mas a conta veio de {b}um número positivo dividido por outro positivo. [p=0.2] Isso {c}nunca dá negativo. [p=0.3] O menos do expoente não é o sinal do resultado: [p=0.2] ele manda {d}virar fração."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho, para base dez com expoente negativo: [p=0.2] {a}escreva tantos zeros quanto o expoente, [p=0.2] {b}ponha a vírgula depois do primeiro zero [p=0.2] e {c}termine com um."),
    dict(id="s16", block="atalho", text="{a}Dez elevado a menos seis. [p=0.2] {b}Seis zeros. [p=0.2] {c}Vírgula depois do primeiro. [p=0.2] {d}Um no fim. [p=0.3] {e}Zero vírgula zero zero zero zero zero um."),
    dict(id="s17", block="atalho", text="Funciona porque são {a}seis casas, e a última é do um. [p=0.2] Sobram cinco zeros depois da vírgula, {b}mais o zero antes dela. [p=0.3] {c}Só vale para base dez. [p=0.2] Em {d}dois elevado a menos três, não há zeros para contar: [p=0.2] vire fração."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] São duas partes. [p=0.2] {a}Resolva cinco ao cubo dividido por cinco elevado a cinco, [p=0.2] e escreva como fração. [p=0.3] Depois, {b}escreva dez elevado a menos cinco como número decimal."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Repete a base e subtrai: {a}três menos cinco dá menos dois. [p=0.2] {b}Cinco elevado a menos dois. [p=0.3] Vira fração: {c}um em cima, cinco ao quadrado embaixo. [p=0.2] {d}Um vinte e cinco avos."),
    dict(id="s21", block="resposta", text="Na base dez, são {a}cinco casas, com o um na última. [p=0.3] {b}Zero vírgula zero zero zero zero um."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}expoente negativo é fração, não número negativo. [p=0.2] Na base dez, {b}positivo conta zeros [p=0.2] e {c}negativo conta casas."),
    dict(id="s23", block="fim", text="Na próxima aula, você {a}pratica: [p=0.2] {b}simplifica expressões usando todas as propriedades de potência. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
