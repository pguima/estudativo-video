# Estudativo · MAT-RAZ-015 — Taxas e velocidade média (Matemática · Razão e Proporção).
# Habilidade: ler km/L e R$/kg e calcular a velocidade de quem faz 180 km em 2 h 30 min e o tempo para fazer 240 km a 80 km/h.
# Pré-requisitos: MAT-EQU-011 (isolar letra), MAT-FRA-018 (dividir por decimal), MAT-MED-006 (hora decimal), MAT-RAZ-001 (razão). Próxima: MAT-RAZ-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Preços inventados, sem referência a preço real.

TITULO = "Taxas e velocidade média"

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
    dict(id="s01", block="gancho", text="Um ônibus faz {a}cento e oitenta quilômetros {b}em duas horas e trinta minutos. [p=0.3] Qual foi a velocidade? [p=0.3] Se você escreveu o tempo como {c}dois vírgula três horas, [p=0.2] errou {d}antes de fazer a conta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê qualquer taxa, [p=0.2] calcula a velocidade média e o tempo de uma viagem, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}quatro coisas: [p=0.2] {b}o que é razão, [p=0.2] {c}passar horas e minutos para hora decimal, [p=0.2] {d}dividir por número com vírgula [p=0.2] e {e}isolar uma letra numa fórmula. [p=0.3] Se faltar alguma, procure no canal."),
    # taxa
    dict(id="s04", block="taxa", text="Razão é a comparação de dois números por meio da divisão. [p=0.2] Quando os números são de {a}tipos diferentes, [p=0.2] como quilômetro e litro, [p=0.2] a razão ganha um nome: {b}taxa. [p=0.3] E a palavra {c}por, numa taxa, quer dizer {d}dividido por."),
    dict(id="s05", block="taxa", text="{a}Doze quilômetros por litro: [p=0.2] o carro anda doze quilômetros {b}com cada litro. [p=0.3] Com {c}quarenta litros, anda {d}doze vezes quarenta dá quatrocentos e oitenta quilômetros."),
    dict(id="s06", block="taxa", text="{a}Trinta reais por quilo: [p=0.2] {b}um quilo custa trinta reais. [p=0.2] Meio quilo, {c}quinze reais. [p=0.3] A taxa diz {d}quanto vale uma unidade. [p=0.2] Por isso ela serve para comparar."),
    dict(id="s07", block="taxa", text="Um pacote de {a}dois quilos custa cinquenta reais. [p=0.2] Outro, de {b}três quilos, custa setenta e dois. [p=0.3] Qual compensa? [p=0.2] Ache o preço do quilo. [p=0.2] {c}Cinquenta dividido por dois dá vinte e cinco reais por quilo. [p=0.2] {d}Setenta e dois dividido por três dá vinte e quatro reais por quilo. [p=0.3] {e}O pacote maior sai mais barato."),
    # velocidade média
    dict(id="s08", block="velocidade", text="Velocidade também é taxa: {a}quilômetros por hora, [p=0.2] quilômetros divididos por horas. [p=0.3] {b}Velocidade média é a distância total dividida pelo tempo total. [p=0.3] É média porque o ônibus acelera e freia, [p=0.2] mas a conta trata a viagem como se fosse {c}num ritmo só."),
    dict(id="s09", block="velocidade", text="Volte ao ônibus. [p=0.2] {a}Duas horas e trinta minutos. [p=0.2] Trinta minutos é {b}meia hora, zero vírgula cinco. [p=0.3] Então o tempo é {c}dois vírgula cinco horas."),
    dict(id="s10", block="velocidade", text="{a}Cento e oitenta dividido por dois vírgula cinco. [p=0.3] Tire a vírgula do divisor, multiplicando cada número por dez: [p=0.2] {b}mil e oitocentos dividido por vinte e cinco. [p=0.3] {c}Setenta e dois quilômetros por hora."),
    # tempo
    dict(id="s11", block="tempo", text="E quando a pergunta é o tempo? [p=0.2] Um carro vai fazer {a}duzentos e quarenta quilômetros [p=0.1] a {b}oitenta quilômetros por hora. [p=0.3] Isolando o tempo na fórmula: {c}tempo igual a distância dividida pela velocidade. [p=0.3] {d}Duzentos e quarenta dividido por oitenta dá três horas."),
    dict(id="s12", block="tempo", text="Confira pelo outro lado. [p=0.2] {a}Oitenta quilômetros em cada hora, durante três horas: [p=0.2] oitenta vezes três dá {b}duzentos e quarenta quilômetros. [p=0.3] Se a conta tivesse ido para o lado errado, essa conferência não bateria."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}ler duas horas e trinta minutos como dois vírgula três. [p=0.3] {b}Cento e oitenta dividido por dois vírgula três dá um número quebrado, [p=0.2] perto de {c}setenta e oito. [p=0.3] Só que zero vírgula três hora são {d}dezoito minutos, não trinta. [p=0.3] A hora tem sessenta minutos, não dez."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}tem meia hora no tempo? [p=0.2] Dobre tudo. [p=0.3] {b}Cento e oitenta quilômetros em duas horas e meia [p=0.2] é o mesmo ritmo de {c}trezentos e sessenta quilômetros em cinco horas. [p=0.3] {d}Trezentos e sessenta dividido por cinco dá setenta e dois."),
    dict(id="s15", block="atalho", text="Funciona porque {a}dobrar a distância e o tempo não muda a velocidade, [p=0.2] como numa fração equivalente. [p=0.3] {b}Não compensa quando os minutos não fazem meia hora, [p=0.2] como em {c}duas horas e vinte minutos. [p=0.2] Aí, converta e divida."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma ciclista pedalou {a}quarenta e cinco quilômetros [p=0.1] em {b}uma hora e trinta minutos. [p=0.3] {c}Qual foi a velocidade média? [p=0.3] E {d}quanto tempo ela levaria para fazer cento e cinquenta quilômetros nesse ritmo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Uma hora e trinta minutos é {a}um vírgula cinco hora. [p=0.3] Pelo atalho, dobre tudo: {b}noventa quilômetros em três horas. [p=0.3] {c}Noventa dividido por três dá trinta quilômetros por hora."),
    dict(id="s19", block="resposta", text="Falta o tempo: {a}distância dividida pela velocidade. [p=0.3] {b}Cento e cinquenta dividido por trinta dá cinco horas. [p=0.3] Conferindo: {c}trinta vezes cinco dá cento e cinquenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}por quer dizer dividido. [p=0.2] {b}Velocidade média é distância total dividida pelo tempo total, [p=0.2] e {c}minuto não é décimo de hora."),
    dict(id="s21", block="fim", text="Na próxima aula, você passa de {a}quilômetros por hora para {b}metros por segundo, [p=0.2] com um número só. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
