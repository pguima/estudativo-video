# Estudativo · MAT-RAZ-016 — Converter km/h em m/s (Matemática · Razão e Proporção).
# Habilidade: transformar 72 km/h em 20 m/s e 15 m/s em 54 km/h, dividindo ou multiplicando por 3,6.
# Pré-requisitos: MAT-RAZ-015 (taxas e velocidade média). Próxima: MAT-RAZ-024.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Converter km/h em m/s"

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
    dict(id="s01", block="gancho", text="Um carro a {a}setenta e dois quilômetros por hora. [p=0.3] Quantos {b}metros ele anda em um segundo? [p=0.3] São {c}vinte. [p=0.2] E dá para achar isso com uma conta só."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você converte nos dois sentidos sem errar a direção, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}ler uma taxa, em que a palavra por quer dizer dividido, [p=0.2] e {c}a escada do metro: um quilômetro tem mil metros. [p=0.3] Se faltar alguma, procure no canal."),
    # as duas unidades
    dict(id="s04", block="unidades", text="{a}Metros por segundo diz quantos metros você anda {b}em cada segundo. [p=0.3] É a unidade que aparece nas questões de física. [p=0.2] {c}Quilômetros por hora é a do velocímetro do carro. [p=0.3] Na conversão, {d}as duas unidades mudam ao mesmo tempo: [p=0.2] o quilômetro vira metro, e a hora vira segundo."),
    # na raça
    dict(id="s05", block="deducao", text="Primeiro, sem atalho nenhum. [p=0.2] {a}Setenta e dois quilômetros são setenta e dois mil metros. [p=0.3] {b}Uma hora tem sessenta minutos, e cada minuto tem sessenta segundos: [p=0.2] {c}sessenta vezes sessenta dá três mil e seiscentos segundos."),
    dict(id="s06", block="deducao", text="São {a}setenta e dois mil metros em três mil e seiscentos segundos. [p=0.3] Por segundo: {b}setenta e dois mil dividido por três mil e seiscentos. [p=0.3] Corte dois zeros de cada número: [p=0.2] {c}setecentos e vinte dividido por trinta e seis. [p=0.2] {d}Vinte metros por segundo."),
    # o fator
    dict(id="s07", block="fator", text="Repare no que você fez: [p=0.2] {a}multiplicou por mil e dividiu por três mil e seiscentos. [p=0.3] O mil cabe {b}três vírgula seis vezes no três mil e seiscentos. [p=0.2] Por isso, essas contas juntas dão o mesmo que uma só: {c}dividir por três vírgula seis. [p=0.3] Confira com o carro: setenta e dois dividido por três vírgula seis dá os mesmos vinte."),
    dict(id="s08", block="fator", text="{a}De quilômetros por hora para metros por segundo: divida por três vírgula seis. [p=0.3] {b}De metros por segundo para quilômetros por hora: multiplique por três vírgula seis. [p=0.3] Teste: {c}cinquenta e quatro dividido por três vírgula seis. [p=0.2] Tire a vírgula do divisor: {d}quinhentos e quarenta dividido por trinta e seis dá quinze metros por segundo."),
    dict(id="s09", block="volta", text="No caminho de volta, parta dos {a}quinze metros por segundo. [p=0.3] {b}Quinze vezes três vírgula seis. [p=0.2] Quinze vezes três dá quarenta e cinco. [p=0.2] Quinze vezes zero vírgula seis dá nove. [p=0.3] {c}Cinquenta e quatro quilômetros por hora."),
    # erro
    dict(id="s10", block="erro", text="O erro comum é {a}errar a direção. [p=0.3] A pessoa multiplica setenta e dois por três vírgula seis [p=0.2] e acha {b}duzentos e cinquenta e nove vírgula dois metros por segundo. [p=0.3] Seriam {c}mais de duzentos e cinquenta metros a cada segundo. [p=0.2] Coisa de avião, não de carro."),
    dict(id="s11", block="erro", text="Para nunca errar: [p=0.2] um metro por segundo já é três vírgula seis quilômetros por hora. [p=0.3] Então {a}a mesma velocidade tem sempre o número maior em quilômetros por hora. [p=0.3] Indo para quilômetros por hora, {b}o número cresce: multiplica. [p=0.2] Indo para metros por segundo, {c}o número diminui: divide."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}guarde três pares. [p=0.3] {b}Trinta e seis quilômetros por hora são dez metros por segundo. [p=0.2] {c}Setenta e dois são vinte. [p=0.2] {d}Cento e oito são trinta."),
    dict(id="s13", block="atalho", text="Funciona porque {a}trinta e seis dividido por três vírgula seis dá dez, exato. [p=0.2] Os outros pares são o dobro e o triplo. [p=0.3] E noventa? [p=0.2] Noventa é setenta e dois mais dezoito, [p=0.2] e dezoito é a metade de trinta e seis. [p=0.2] {b}Vinte mais cinco: vinte e cinco metros por segundo."),
    dict(id="s14", block="atalho", text="{a}Não compensa com números que não saem desses pares, como cem. [p=0.2] Cem dividido por três vírgula seis dá vinte e sete vírgula sete, e os setes não acabam. [p=0.2] Aí, {b}divida por três vírgula seis direto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Numa rodovia, a placa marca {a}noventa quilômetros por hora. [p=0.3] Um radar mede um carro a {b}trinta metros por segundo. [p=0.3] {c}Esse carro está acima do limite?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Passe o carro para quilômetros por hora: {a}multiplique por três vírgula seis. [p=0.3] {b}Trinta vezes três vírgula seis dá cento e oito. [p=0.3] {c}Cento e oito é mais que noventa: está acima do limite."),
    dict(id="s18", block="resposta", text="Pelo atalho, nem precisava de conta: [p=0.2] {a}trinta metros por segundo é um dos pares, cento e oito quilômetros por hora. [p=0.3] Ou pelo outro lado: {b}o limite de noventa são vinte e cinco metros por segundo, [p=0.2] e o carro passou disso."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}para metros por segundo, divida por três vírgula seis. [p=0.2] {b}Para quilômetros por hora, multiplique. [p=0.2] E {c}quilômetros por hora tem sempre o número maior."),
    dict(id="s20", block="fim", text="Na próxima aula, uma pegadinha clássica: [p=0.2] {a}ida a quarenta quilômetros por hora, volta a sessenta. [p=0.3] A velocidade média {b}não é cinquenta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
