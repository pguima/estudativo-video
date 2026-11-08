# Estudativo · MAT-RAZ-004 — Grandezas direta e inversamente proporcionais (Matemática · Razão e Proporção).
# Habilidade: reconhecer numa tabela que y/x é sempre o mesmo número, ou que velocidade vezes tempo não muda.
# Pré-requisitos: MAT-RAZ-001 (razão). Próxima: MAT-RAZ-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Proporção e produto cruzado (MAT-RAZ-002) não estão na cadeia: só divisão e multiplicação.
# O teste do dobro fica para MAT-RAZ-005. Na tela: tabelas de duas colunas.

TITULO = "Grandezas direta e inversamente proporcionais"

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
    dict(id="s01", block="gancho", text="Mais quilos de feijão, {a}mais você paga. [p=0.3] Mais velocidade na estrada, {b}menos tempo de viagem. [p=0.3] Uma dupla anda junto, a outra anda ao contrário. [p=0.2] E {c}uma conta simples na tabela mostra qual é qual."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reconhece numa tabela se duas grandezas são proporcionais, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}razão, que é comparar dois números pela divisão. [p=0.3] Se faltar essa aula, procure no canal."),
    # grandeza
    dict(id="s04", block="grandeza", text="Primeiro, uma palavra. [p=0.2] {a}Grandeza é tudo que dá para medir ou contar: [p=0.2] {b}preço, [p=0.1] {c}peso, [p=0.1] {d}tempo, [p=0.1] {e}velocidade."),
    # direta
    dict(id="s05", block="direta", text="Veja esta tabela. [p=0.2] {a}Um quilo de feijão, oito reais. [p=0.2] {b}Dois quilos, dezesseis. [p=0.2] {c}Três quilos, vinte e quatro. [p=0.2] {d}Cinco quilos, quarenta."),
    dict(id="s06", block="direta", text="Faça a razão de cada linha: {a}preço dividido por quilos. [p=0.3] {b}Dezesseis dividido por dois dá oito. [p=0.2] {c}Vinte e quatro dividido por três dá oito. [p=0.2] {d}Quarenta dividido por cinco dá oito. [p=0.3] Dá sempre {e}o mesmo número."),
    dict(id="s07", block="direta", text="Quando a divisão dá sempre o mesmo número, [p=0.2] as grandezas são {a}diretamente proporcionais. [p=0.3] E esse número tem significado: [p=0.2] {b}oito reais é o preço de um quilo. [p=0.2] Nos livros, esse número fixo se chama {c}constante de proporcionalidade. [p=0.3] Com ele, você completa a tabela: [p=0.2] {d}quatro quilos, quatro vezes oito dá trinta e dois reais."),
    # inversa
    dict(id="s08", block="inversa", text="Agora, uma viagem de cento e vinte quilômetros. [p=0.2] Velocidade em {a}quilômetros por hora: [p=0.2] quantos quilômetros o carro anda {b}em uma hora."),
    dict(id="s09", block="inversa", text="A {a}trinta por hora, a viagem leva quatro horas. [p=0.2] A {b}quarenta por hora, leva três horas. [p=0.2] A {c}sessenta por hora, leva duas horas. [p=0.3] Aqui, dividir não dá sempre o mesmo. [p=0.2] {d}Multiplique."),
    dict(id="s10", block="inversa", text="{a}Trinta vezes quatro dá cento e vinte. [p=0.2] {b}Quarenta vezes três dá cento e vinte. [p=0.2] {c}Sessenta vezes dois dá cento e vinte. [p=0.3] {d}Velocidade vezes tempo não muda."),
    dict(id="s11", block="inversa", text="Quando o produto é sempre o mesmo, [p=0.2] as grandezas são {a}inversamente proporcionais. [p=0.3] E o cento e vinte também tem significado: [p=0.2] se o carro anda sessenta quilômetros em cada hora, [p=0.2] em duas horas anda cento e vinte. [p=0.2] {b}Velocidade vezes tempo é a distância. [p=0.3] E dá para completar a tabela: [p=0.2] a {c}cento e vinte por hora, a viagem leva {d}uma hora, [p=0.2] porque cento e vinte vezes um dá cento e vinte."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é pensar: {a}subiu junto, então é diretamente proporcional. [p=0.3] Uma criança mede {b}noventa centímetros aos dois anos [p=0.2] e {c}cem centímetros aos quatro. [p=0.2] A idade subiu, a altura também."),
    dict(id="s13", block="erro", text="Mas faça a divisão: [p=0.2] {a}noventa dividido por dois dá quarenta e cinco. [p=0.2] {b}Cem dividido por quatro dá vinte e cinco. [p=0.3] {c}Números diferentes: não é proporcional. [p=0.2] Subir junto não basta. [p=0.2] {d}Quem decide é a conta. [p=0.3] O contrário também engana: [p=0.2] {e}um sobe, o outro desce, e mesmo assim pode não ser inversa. [p=0.2] De novo, faça a conta."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho prometido, para não trocar as contas: [p=0.2] {a}direta, divisão. [p=0.2] As duas palavras começam com {b}dê. [p=0.3] {c}Inversa, o contrário: multiplicação."),
    dict(id="s15", block="atalho", text="Funciona porque na direta {a}as duas grandezas crescem na mesma medida, [p=0.2] e a divisão fica parada. [p=0.3] Na inversa, {b}uma cresce na medida em que a outra encolhe, [p=0.2] e o produto fica parado. [p=0.3] O macete só diz {c}qual conta fazer. [p=0.2] Confira {d}todas as linhas. [p=0.2] Se nem a divisão nem o produto se repetem, [p=0.2] não é nenhuma das duas."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Torneiras iguais enchem uma caixa d'água. [p=0.2] {a}Uma torneira leva doze horas. [p=0.1] {b}Duas torneiras levam seis horas. [p=0.1] {c}Três levam quatro horas. [p=0.1] {d}Quatro levam três horas. [p=0.3] {e}As grandezas são direta ou inversamente proporcionais? [p=0.2] E {f}qual número não muda?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Mais torneiras, menos tempo: pista de inversa. [p=0.2] Pista, não prova: quem decide é a conta. [p=0.2] {a}Teste multiplicando. [p=0.2] {b}Um vezes doze dá doze. [p=0.1] {c}Dois vezes seis dá doze. [p=0.1] {d}Três vezes quatro dá doze. [p=0.1] {e}Quatro vezes três dá doze."),
    dict(id="s19", block="resposta", text="O produto não muda: {a}inversamente proporcionais. [p=0.3] E o doze é {b}o tempo que uma torneira sozinha levaria. [p=0.2] Repartido entre mais torneiras, ele encurta. [p=0.3] Com {c}seis torneiras: doze dividido por seis dá duas horas."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}divisão sempre igual, direta. [p=0.2] {b}Produto sempre igual, inversa."),
    dict(id="s21", block="fim", text="Na próxima aula, um teste rápido, sem tabela: {a}dobre uma grandeza e veja o que acontece com a outra. [p=0.3] E você descobre por que {b}a corrida de táxi não é proporcional. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
