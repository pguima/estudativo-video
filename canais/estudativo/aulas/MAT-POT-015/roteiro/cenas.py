# Estudativo · MAT-POT-015 — Praticando: notação científica (Matemática · Potências e Raízes · prática).
# Habilidade: fazer contas e comparar medidas muito grandes ou muito pequenas, como a distância até o Sol.
# Pré-requisitos: MAT-POT-012, MAT-POT-013, MAT-POT-014. Próxima: nenhuma; é a última da trilha Potências e Raízes (15ª de 15).
# Questões inéditas, criadas para esta aula. As duas cidades são invenção; o ano de 365 dias é conta (365 × 24 × 3.600 = 31.536.000 s).
# Fatos: Terra-Sol cerca de 150 milhões de km (NASA, Sun Facts; NSSDC Earth Fact Sheet: 149,598 × 10⁶ km).
# Fatos: luz cerca de 300 mil km/s (NIST CODATA 2022: 299.792.458 m/s, valor exato). Conta real: cerca de 499 s; na aula, 500 s.
# Fatos: folha de papel cerca de 100.000 nm = 1 × 10⁻⁴ m; fio de cabelo 80.000 a 100.000 nm, usado 8 × 10⁻⁵ m (NNCO, Just How Small Is "Nano"?).
# Fatos: bactéria E. coli cerca de 2 μm de comprimento = 2 × 10⁻⁶ m (BioNumbers BNID 100001: 1,94 a 2,72 μm).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: notação científica"

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
    dict(id="s01", block="gancho", text="{a}Quantos minutos a luz do Sol leva para chegar até você? [p=0.3] Dá para calcular com o que você já sabe. [p=0.3] São {b}quatro situações, criadas para esta aula. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}escrever em notação científica, [p=0.2] {b}multiplicar e dividir, [p=0.2] {c}somar com expoente igual [p=0.2] e {d}achar a ordem de grandeza. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: escrever e dividir
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] O Sol está a {b}cerca de cento e cinquenta milhões de quilômetros da Terra. [p=0.3] A luz percorre {c}cerca de trezentos mil quilômetros por segundo. [p=0.3] {d}Em quantos segundos a luz do Sol chega aqui?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] A pergunta é quantas vezes trezentos mil cabe na distância: {a}é uma divisão. [p=0.3] Escreva os números: {b}um vírgula cinco vezes dez elevado a oito, [p=0.2] dividido por {c}três vezes dez elevado a cinco."),
    dict(id="s06", block="resposta1", text="{a}Um vírgula cinco dividido por três dá zero vírgula cinco. [p=0.2] {b}Oito menos cinco dá três: dez elevado a três. [p=0.3] Deu {c}zero vírgula cinco vezes dez elevado a três. [p=0.3] Mas {d}zero vírgula cinco fica abaixo de um: a forma ainda não está certa."),
    dict(id="s07", block="resposta1", text="A vírgula anda uma casa para a direita: {a}cinco. [p=0.2] A frente ficou dez vezes maior, então {b}o expoente desce de três para dois. [p=0.3] {c}Cinco vezes dez elevado a dois: quinhentos segundos. [p=0.3] Um minuto tem sessenta segundos, e oito vezes sessenta dá quatrocentos e oitenta. [p=0.2] São {d}cerca de oito minutos e vinte segundos."),
    # situação 2: comparar e dividir medidas pequenas
    dict(id="s08", block="questao2", text="{a}Situação dois, com duas perguntas. [p=0.2] Uma folha de papel tem {b}cerca de um vezes dez elevado a menos quatro metro de espessura. [p=0.3] Um fio de cabelo tem {c}cerca de oito vezes dez elevado a menos cinco metro de largura. [p=0.3] Primeira pergunta: {d}qual é o mais fino?"),
    dict(id="s09", block="questao2", text="Segunda pergunta. [p=0.2] Uma bactéria comum mede {a}cerca de dois vezes dez elevado a menos seis metro. [p=0.3] {b}Quantas bactérias em fila cobrem a largura do fio?"),
    dict(id="s10", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta2", text="Vamos lá. [p=0.2] Oito parece maior que um, mas, na forma correta, {a}quem decide primeiro é o expoente. [p=0.3] Na reta numérica, {b}menos quatro está à direita de menos cinco, [p=0.2] então a folha é mais grossa. [p=0.3] {c}O mais fino é o fio de cabelo. [p=0.3] Só compare a frente {d}quando os expoentes forem iguais."),
    dict(id="s12", block="resposta2", text="Agora a divisão. [p=0.2] {a}Oito dividido por dois dá quatro. [p=0.3] Nos expoentes: {b}menos cinco menos, abre parênteses, menos seis, fecha parênteses. [p=0.2] Tirar um negativo é somar: {c}menos cinco mais seis dá um. [p=0.3] {d}Quatro vezes dez elevado a um: {e}cerca de quarenta bactérias."),
    # situação 3: somar
    dict(id="s13", block="questao3", text="{a}Situação três. [p=0.2] Uma cidade tem {b}dois vírgula quatro vezes dez elevado a seis habitantes. [p=0.3] A vizinha tem {c}seis vezes dez elevado a cinco. [p=0.3] {d}Quantos habitantes têm juntas, em notação científica?"),
    dict(id="s14", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta3", text="Vamos lá. [p=0.2] Soma pede o mesmo expoente. [p=0.2] Passe para o maior: {a}seis vezes dez elevado a cinco vira zero vírgula seis vezes dez elevado a seis. [p=0.3] {b}Dois vírgula quatro mais zero vírgula seis dá três. [p=0.3] Resposta: {c}três vezes dez elevado a seis, ou três milhões de habitantes. [p=0.3] Quem soma direto acha {d}oito vírgula quatro vezes dez elevado a seis: [p=0.2] mais de oito milhões, quando nenhuma das cidades chega a dois milhões e meio."),
    # atalho
    dict(id="s16", block="atalho", text="O atalho vale para a divisão da luz do Sol: [p=0.2] {a}ande a vírgula antes de dividir. [p=0.3] Um vírgula cinco vezes dez elevado a oito é {b}quinze vezes dez elevado a sete. [p=0.2] Quinze dividido por três dá cinco. [p=0.2] Nos expoentes, sete menos cinco dá dois. [p=0.2] Resultado: cinco vezes dez elevado a dois, sem ajuste no fim. [p=0.3] Funciona porque a frente ficou dez vezes maior, e a potência, dez vezes menor. [p=0.2] {c}Não compensa quando o primeiro número da frente já é maior que o segundo: [p=0.2] aí, divida direto."),
    # situação 4: ordem de grandeza
    dict(id="s17", block="questao4", text="{a}Última situação. [p=0.2] Um ano de {b}trezentos e sessenta e cinco dias tem {c}trinta e um milhões e quinhentos e trinta e seis mil segundos. [p=0.3] {d}Qual é a ordem de grandeza desse número?"),
    dict(id="s18", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta4", text="Vamos lá. [p=0.2] Em notação científica, são {a}cerca de três vírgula quinze vezes dez elevado a sete. [p=0.3] Começa com três vírgula um, então {b}compare com calma: [p=0.2] {c}três vírgula quinze não passa de três vírgula dezesseis. [p=0.3] O expoente fica: {d}dez elevado a sete. [p=0.3] Foi por pouco!"),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}nas contas, cuide dos expoentes, [p=0.2] {b}na soma, iguale antes [p=0.2] e {c}no fim, confira se a frente ficou de um até menos de dez."),
    dict(id="s21", block="fim", text="{a}Com esta prática, você fecha a trilha de potências e raízes. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
