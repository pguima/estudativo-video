# Estudativo · MAT-MED-006 — Converter tempo e hora decimal (Matemática · Medidas e Unidades).
# Habilidade: transformar 2 h 15 min em minutos e ler 2,2 h como 2 h 12 min, sem confundir décimo com minuto.
# Pré-requisitos: MAT-FRA-002 (fração de quantidade), MAT-FRA-004 (número misto), MAT-FRA-016 (multiplicar decimais), MAT-FRA-019 (decimal em fração). Próxima: MAT-MED-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Somar e subtrair horas com troca de sessenta minutos fica para MAT-MED-007.

TITULO = "Converter tempo e hora decimal"

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
    dict(id="s01", block="gancho", text="O aplicativo diz que a viagem dura {a}duas vírgula duas horas. [p=0.3] Se você leu {b}duas horas e vinte minutos, [p=0.2] vai chegar {c}oito minutos antes do que imagina."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai converter horas em minutos, [p=0.2] ler hora com vírgula sem errar [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}calcular a fração de uma quantidade, [p=0.2] {c}trocar decimal por fração [p=0.2] e {d}multiplicar decimais. [p=0.3] Se faltar alguma, procure no canal."),
    # o tempo é diferente
    dict(id="s04", block="sessenta", text="Metro, grama e litro andam {a}de dez em dez. [p=0.2] O tempo, não. [p=0.3] {b}Uma hora tem sessenta minutos. [p=0.2] {c}Um minuto tem sessenta segundos. [p=0.3] O tempo anda {d}de sessenta em sessenta."),
    dict(id="s05", block="sessenta", text="Por isso, aqui {a}não basta andar com a vírgula, [p=0.2] que só serve para dez, cem e mil. [p=0.2] De hora para minuto, {b}multiplique por sessenta. [p=0.2] De minuto para hora, {c}divida por sessenta."),
    # horas e minutos em minutos
    dict(id="s06", block="minutos", text="Um filme dura {a}duas horas e quinze minutos. [p=0.2] Quantos minutos são? [p=0.3] {b}Duas horas: duas vezes sessenta dá cento e vinte. [p=0.2] {c}Mais quinze: cento e trinta e cinco minutos."),
    dict(id="s07", block="minutos", text="Quinze minutos também é {a}um quarto de hora: [p=0.2] sessenta dividido por quatro dá quinze. [p=0.3] Então o filme dura {b}duas horas e um quarto, [p=0.2] um número misto: {c}dois inteiros e um quarto de hora."),
    dict(id="s08", block="horas", text="E o caminho de volta? [p=0.2] Uma aula de {a}cento e cinquenta minutos. [p=0.2] Quantas vezes o sessenta cabe aí? [p=0.2] {b}Duas, que dão cento e vinte. [p=0.2] Sobram {c}trinta minutos. [p=0.3] A aula dura {d}duas horas e trinta minutos."),
    dict(id="s09", block="horas", text="Trinta minutos é meia hora, [p=0.2] então também dá para escrever {a}dois vírgula cinco horas. [p=0.3] E com segundos é igual: [p=0.2] {b}uma hora tem sessenta vezes sessenta, [p=0.2] {c}três mil e seiscentos segundos."),
    dict(id="s10", block="horas", text="E quando sobra menos de uma hora? [p=0.2] {a}Quarenta e cinco minutos, em horas. [p=0.2] São quarenta e cinco de sessenta. [p=0.2] Dividindo em cima e embaixo por quinze, [p=0.3] fica {b}três quartos de hora. [p=0.3] Em decimal, {c}zero vírgula setenta e cinco hora."),
    # hora com vírgula
    dict(id="s11", block="decimal", text="E a hora com vírgula? [p=0.2] Em {a}duas vírgula duas horas, o que vem antes da vírgula são {b}duas horas inteiras. [p=0.3] O resto, {c}zero vírgula dois, é um pedaço de hora. [p=0.2] São {d}dois décimos de hora, [p=0.2] e não vinte minutos."),
    dict(id="s12", block="decimal", text="Dois décimos de sessenta minutos: [p=0.2] divide pelo de baixo, {a}sessenta dividido por dez dá seis. [p=0.2] Multiplica pelo de cima, {b}seis vezes dois dá doze. [p=0.3] A viagem dura {c}duas horas e doze minutos."),
    dict(id="s13", block="decimal", text="A mesma conta sai multiplicando o decimal: {a}zero vírgula dois vezes sessenta. [p=0.2] Sem a vírgula, dois vezes sessenta dá cento e vinte. [p=0.2] Uma casa: {b}doze minutos."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é o do começo: {a}ler os décimos como minutos. [p=0.2] Isso só daria certo se {b}a hora tivesse cem minutos. [p=0.3] Ela tem sessenta. [p=0.2] {c}Zero vírgula cinco hora é meia hora: trinta minutos, [p=0.2] e não cinquenta."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}cada décimo de hora são seis minutos. [p=0.3] {b}Zero vírgula um: seis. [p=0.2] {c}Zero vírgula dois: doze. [p=0.2] {d}Zero vírgula cinco: trinta. [p=0.2] {e}Zero vírgula oito: quarenta e oito. [p=0.3] Basta {f}multiplicar o algarismo dos décimos por seis."),
    dict(id="s16", block="atalho", text="Funciona porque {a}sessenta dividido por dez dá seis. [p=0.3] {b}Não compensa com duas casas, como zero vírgula vinte e cinco: [p=0.2] aí, troque por fração. [p=0.2] {c}Vinte e cinco centésimos é um quarto: quinze minutos."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma entrega leva {a}três vírgula quatro horas. [p=0.2] {b}Quanto é isso em horas e minutos? [p=0.3] E um treino dura {c}uma hora e cinquenta minutos. [p=0.2] {d}Quantos minutos são?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Antes da vírgula, {a}três horas inteiras. [p=0.2] Depois, {b}quatro décimos: quatro vezes seis dá vinte e quatro. [p=0.3] {c}Três horas e vinte e quatro minutos, [p=0.2] e não três horas e quarenta. [p=0.3] Confira: {d}quatro décimos é menos que meia hora, [p=0.2] e vinte e quatro minutos também."),
    dict(id="s20", block="resposta", text="No treino, {a}uma hora são sessenta minutos. [p=0.2] {b}Sessenta mais cinquenta: cento e dez minutos. [p=0.3] Um pouco menos que duas horas, {c}que seriam cento e vinte."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}o tempo anda de sessenta em sessenta, [p=0.2] e {b}cada décimo de hora são seis minutos."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai {a}somar e subtrair horas, [p=0.2] como {b}três horas e cinquenta minutos mais duas horas e vinte e cinco, [p=0.2] trocando {c}sessenta minutos por uma hora. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
