# Estudativo · MAT-RAZ-014 — Dividir em partes inversamente proporcionais (Matemática · Razão e Proporção).
# Habilidade: repartir um prêmio de forma inversa às faltas de cada um.
# Pré-requisitos: MAT-RAZ-013 (divisão direta), MAT-RAZ-004 (grandezas inversas), MAT-FRA-008 (MMC nas frações). Próxima: MAT-RAZ-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Listas de números separadas por pausa, sem vírgula.

TITULO = "Dividir em partes inversamente proporcionais"

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
    dict(id="s01", block="gancho", text="Uma empresa vai dividir {a}um prêmio de dois mil trezentos e quarenta reais [p=0.2] entre três funcionários, [p=0.2] em partes inversamente proporcionais às faltas: [p=0.2] quem {b}faltou menos leva mais. [p=0.3] {c}O Edu teve duas faltas. [p=0.2] {d}A Fabi teve três. [p=0.2] {e}O Gil teve quatro."),
    dict(id="s02", block="gancho", text="Muita gente {a}troca a ordem dos números e erra. [p=0.3] {b}Até o fim desta aula, você reparte esse prêmio do jeito certo, [p=0.2] e ainda leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}dividir em partes diretamente proporcionais, com o cá, [p=0.2] {c}saber que, em grandezas inversas, o produto não muda, [p=0.2] e {d}somar frações com o MMC. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia
    dict(id="s04", block="ideia", text="Dividir em partes {a}inversamente proporcionais quer dizer: [p=0.2] quanto maior o número, {b}menor a parte. [p=0.3] Quem tem o dobro de faltas leva {c}a metade do que o outro leva. [p=0.2] Quem tem o triplo, {d}a terça parte."),
    dict(id="s05", block="ideia", text="Por isso, os pesos não são as faltas. [p=0.2] São {a}os inversos delas: um meio, um terço e um quarto. [p=0.3] O inverso de um número é {b}um dividido por ele. [p=0.2] O inverso de dois é {c}um dividido por dois: um meio."),
    dict(id="s06", block="ideia", text="Por que o inverso? [p=0.2] Em grandezas inversas, {a}parte vezes faltas dá sempre o mesmo número. [p=0.3] Então cada parte é {b}esse número dividido pelas faltas. [p=0.2] E dividir por dois é o mesmo que {c}multiplicar por um meio."),
    # tirar as frações
    dict(id="s07", block="pesos", text="Mas peso em fração dá trabalho. [p=0.2] Tire as frações com o {a}MMC dos denominadores. [p=0.3] MMC de dois [p=0.1] três [p=0.1] e quatro: {b}doze. [p=0.3] Multiplique cada fração por doze. [p=0.2] {c}Um meio de doze, seis. [p=0.2] {d}Um terço de doze, quatro. [p=0.2] {e}Um quarto de doze, três."),
    dict(id="s08", block="pesos", text="Multiplicar todos os pesos pelo mesmo número {a}não muda a divisão. [p=0.3] Virou uma divisão direta comum, [p=0.2] com pesos {b}seis [p=0.2] quatro [p=0.2] e três."),
    # a conta
    dict(id="s09", block="conta", text="{a}Some os pesos: treze. [p=0.3] {b}Dois mil trezentos e quarenta dividido por treze dá cento e oitenta. [p=0.2] Esse é o cá."),
    dict(id="s10", block="conta", text="{a}Edu: seis vezes cento e oitenta dá mil e oitenta reais. [p=0.3] {b}Fabi: quatro vezes cento e oitenta dá setecentos e vinte reais. [p=0.3] {c}Gil: três vezes cento e oitenta dá quinhentos e quarenta reais."),
    dict(id="s11", block="confere", text="Duas conferências. [p=0.2] {a}A soma dá dois mil trezentos e quarenta. [p=0.3] E {b}parte vezes faltas dá sempre o mesmo. [p=0.2] {c}Mil e oitenta vezes dois dá dois mil cento e sessenta. [p=0.2] {d}Setecentos e vinte vezes três dá dois mil cento e sessenta. [p=0.2] {e}Quinhentos e quarenta vezes quatro dá dois mil cento e sessenta. [p=0.3] É inversa de verdade."),
    # erro
    dict(id="s12", block="erro", text="Lembra do erro do começo? [p=0.2] É {a}trocar a ordem, usando pesos quatro [p=0.2] três [p=0.2] e dois. [p=0.3] {b}A soma dá nove, e o cá dá duzentos e sessenta. [p=0.3] O Edu levaria {c}mil e quarenta reais, [p=0.2] a Fabi, setecentos e oitenta, [p=0.2] e o Gil, quinhentos e vinte."),
    dict(id="s13", block="erro", text="Parece certo: quem faltou menos levou mais. [p=0.3] Mas teste o produto. [p=0.2] {a}Mil e quarenta vezes dois dá dois mil e oitenta. [p=0.2] {b}Setecentos e oitenta vezes três dá dois mil trezentos e quarenta. [p=0.3] {c}Não deu o mesmo, então não é inversa. [p=0.3] Inverso é {d}um dividido pelo número, não trocar a ordem."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}o MMC dividido por cada número já é o peso. [p=0.3] {b}Doze dividido por dois dá seis. [p=0.2] {c}Doze dividido por três dá quatro. [p=0.2] {d}Doze dividido por quatro dá três. [p=0.3] Sem escrever fração nenhuma."),
    dict(id="s15", block="atalho", text="Funciona porque {a}um meio de doze é doze dividido por dois. [p=0.2] É a mesma conta, pulando a fração. [p=0.3] {b}Com duas pessoas, é ainda mais fácil: [p=0.2] inversa a dois e três é {c}direta a três e dois. [p=0.3] Mas trocar a ordem {d}só funciona com duas pessoas. [p=0.2] Com três ou mais, é justamente o erro que você viu."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma avó vai dividir {a}mil e oitocentos reais entre três netos, [p=0.2] de forma {b}inversa à idade. [p=0.3] As idades são {c}três anos [p=0.2] quatro anos [p=0.2] e seis anos. [p=0.3] {d}Quanto recebe cada neto?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] MMC de três [p=0.1] quatro [p=0.1] e seis: {a}doze. [p=0.3] Os pesos são doze dividido por cada idade: [p=0.2] {b}quatro [p=0.2] três [p=0.2] e dois. [p=0.3] {c}A soma é nove. [p=0.2] {d}Mil e oitocentos dividido por nove dá duzentos."),
    dict(id="s19", block="resposta", text="{a}Neto de três anos: quatro vezes duzentos dá oitocentos reais. [p=0.3] {b}Neto de quatro anos: seiscentos reais. [p=0.2] {c}Neto de seis anos: quatrocentos reais. [p=0.3] Conferindo: {d}a soma dá mil e oitocentos, [p=0.2] e {e}parte vezes idade dá sempre dois mil e quatrocentos. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}inversa aos números é direta aos inversos. [p=0.3] {b}O MMC dividido por cada número dá os pesos, [p=0.2] e {c}o resto é o cá de sempre."),
    dict(id="s21", block="fim", text="Na próxima aula, a razão ganha o nome de {a}taxa: [p=0.2] quilômetros por litro, reais por quilo [p=0.2] e {b}a velocidade média de uma viagem. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
