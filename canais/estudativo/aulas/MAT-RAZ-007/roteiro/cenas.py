# Estudativo · MAT-RAZ-007 — Regra de três inversa (Matemática · Razão e Proporção).
# Habilidade: descobrir o tempo de 6 pintores sabendo que 4 pintores levam 9 dias.
# Pré-requisitos: MAT-RAZ-005 (teste do dobro), MAT-RAZ-006 (regra de três direta). Próxima: MAT-RAZ-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula.
# 4 · 9 = 36 = 6 · x → x = 6. Erro (direta): 4/9 = 6/x → 4x = 54 → x = 13,5. Tabela com a coluna sem o xis virada: 9/x = 6/4 → 6x = 36 → x = 6.
# Velocidade: 60 · 4 = 240 = 80 · x → x = 3. Questão: ração para 5 cachorros, 6 semanas; 3 cachorros: 5 · 6 = 30 = 3 · x → x = 10 (6/x = 3/5).

TITULO = "Regra de três inversa"

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
    dict(id="s01", block="gancho", text="{a}Quatro pintores pintam uma casa em nove dias. [p=0.3] {b}Com seis pintores, quantos dias? [p=0.3] Se você respondeu {c}treze dias e meio, [p=0.2] contratou mais gente e a obra ficou mais lenta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve a regra de três em que uma grandeza sobe e a outra desce, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}o teste do dobro, que diz se a relação é direta ou inversa, [p=0.2] e {c}a regra de três direta, com a tabela e o produto cruzado. [p=0.3] Se faltar alguma, procure no canal."),
    # por que o produto não muda
    dict(id="s04", block="ideia", text="Comece pelo teste do dobro. [p=0.2] {a}Dobrando os pintores, a casa fica pronta na metade do tempo. [p=0.3] Uma grandeza dobrou e a outra caiu pela metade: [p=0.2] a relação é {b}inversa."),
    dict(id="s05", block="ideia", text="Agora pense no trabalho todo. [p=0.2] {a}Quatro pintores durante nove dias são trinta e seis dias de trabalho de um pintor. [p=0.3] Ou seja: {b}um pintor sozinho levaria trinta e seis dias. [p=0.3] Esse total {c}não muda, seja qual for a equipe, [p=0.2] porque a casa é a mesma."),
    dict(id="s06", block="ideia", text="Com seis pintores, os trinta e seis dias de trabalho se repartem: [p=0.2] {a}trinta e seis dividido por seis dá {b}seis dias. [p=0.3] Mais pintores, menos dias. [p=0.2] {c}Faz sentido. [p=0.3] É a mesma ideia de passar pelo preço de um quilo: [p=0.2] primeiro, {d}quanto tempo leva um pintor só."),
    dict(id="s07", block="ideia", text="Essa é a marca da relação inversa: [p=0.2] {a}a multiplicação das duas grandezas dá sempre o mesmo número. [p=0.3] {b}Quatro vezes nove dá trinta e seis. [p=0.2] {c}Seis vezes seis dá trinta e seis."),
    # método das colunas
    dict(id="s08", block="metodo", text="Na prova, você pode montar {a}a tabela, como na regra de três direta, com cada grandeza na sua coluna. [p=0.3] {b}Pintores: quatro e seis. [p=0.2] {c}Dias: nove e xis."),
    dict(id="s09", block="metodo", text="O teste do dobro deu inversa, então antes da conta {a}vire de cabeça para baixo a coluna que não tem o xis. [p=0.3] Virando a dos pintores, {b}fica nove dividido por xis igual a seis quartos."),
    dict(id="s10", block="metodo", text="Daí, {a}produto cruzado. [p=0.2] {b}Seis vezes xis igual a quatro vezes nove, trinta e seis. [p=0.3] {c}Xis igual a trinta e seis dividido por seis: [p=0.2] {d}seis dias. [p=0.3] O mesmo resultado do trabalho total."),
    # erro comum
    dict(id="s11", block="erro", text="De onde saíram os treze dias e meio do começo? [p=0.2] A pessoa {a}não fez o teste do dobro e montou a regra de três direta. [p=0.3] {b}Quatro vezes xis igual a nove vezes seis, cinquenta e quatro. [p=0.2] {c}Xis igual a treze e meio."),
    dict(id="s12", block="erro", text="A conta está certa, [p=0.1] mas {a}a montagem está errada. [p=0.3] Antes de marcar, pergunte: [p=0.2] {b}mais gente trabalhando pode levar mais dias? [p=0.2] Não pode. [p=0.2] Essa pergunta leva {c}três segundos e pega o erro."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: [p=0.2] {a}na inversa, multiplique na linha. [p=0.3] Cada linha é uma situação. [p=0.2] {b}Quatro pintores vezes nove dias [p=0.2] {c}igual a seis pintores vezes xis dias. [p=0.3] {d}Trinta e seis igual a seis xis. [p=0.2] {e}Xis igual a seis."),
    dict(id="s14", block="atalho", text="Funciona porque, na relação inversa, {a}a multiplicação de cada linha é o trabalho total, e ele não muda. [p=0.3] Serve para velocidade e tempo também. [p=0.2] {b}A sessenta quilômetros por hora, uma viagem leva quatro horas. [p=0.2] {c}A oitenta por hora, a conta é sessenta vezes quatro igual a oitenta vezes xis. [p=0.2] {d}Xis igual a três horas."),
    dict(id="s15", block="atalho", text="{a}Só use depois do teste do dobro. [p=0.2] Se a relação for direta, multiplicar na linha {b}dá errado. [p=0.3] E com três grandezas, como pintores, horas e dias, {c}é outro tipo de regra de três, assunto de outra aula."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Um saco grande de ração alimenta cinco cachorros iguais durante seis semanas. [p=0.3] {b}Se forem só três desses cachorros, quantas semanas o mesmo saco dura?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Teste do dobro: {a}com o dobro de cachorros, a ração acaba na metade do tempo. [p=0.2] {b}Inversa. [p=0.3] Multiplique na linha: [p=0.2] {c}cinco vezes seis dá trinta, [p=0.2] {d}igual a três vezes xis."),
    dict(id="s19", block="resposta", text="{a}Xis igual a trinta dividido por três: [p=0.2] {b}dez semanas. [p=0.3] Menos cachorros, a ração dura mais. [p=0.2] {c}Faz sentido. [p=0.3] Pelas colunas, virando a dos cachorros, {d}seis dividido por xis igual a três quintos, [p=0.2] e o produto cruzado dá os mesmos dez."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}teste do dobro primeiro. [p=0.2] {b}Se for inversa, a multiplicação de cada linha é a mesma. [p=0.2] {c}E confira se o resultado faz sentido."),
    dict(id="s21", block="fim", text="Na próxima aula, entram {a}três grandezas de uma vez: [p=0.2] {b}máquinas, horas e peças, todas diretas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
