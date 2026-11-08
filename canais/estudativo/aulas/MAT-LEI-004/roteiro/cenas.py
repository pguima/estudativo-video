# Estudativo · MAT-LEI-004 — Estimar contas e quantidades (Matemática · Leitura de Problemas).
# Habilidade: achar 48 × 21 ≈ 1.000 e estimar os batimentos do coração em 70 anos, usando ordem de grandeza.
# Pré-requisitos: MAT-FRA-014 (arredondar), MAT-LEI-001 (pergunta e dados úteis), MAT-NUM-007 (vezes dez e cem), MAT-POT-013 (contas em notação científica), MAT-POT-014 (ordem de grandeza). Próxima: MAT-LEI-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Setenta batimentos por minuto é um valor típico de repouso, usado só como estimativa.

TITULO = "Estimar contas e quantidades"

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
    dict(id="s01", block="gancho", text="Quantas vezes o coração bate {a}em setenta anos de vida? [p=0.3] Milhões? [p=0.2] Bilhões? [p=0.3] Dá para responder {b}sem calculadora e sem conta comprida."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai estimar contas e quantidades enormes, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de três coisas: [p=0.2] {a}arredondar um número, [p=0.2] {b}multiplicar por dez e por cem acrescentando zeros, [p=0.2] e {c}a ordem de grandeza, a potência de dez mais próxima de um número. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é estimar
    dict(id="s04", block="estimar", text="Estimar é fazer {a}uma conta parecida, só que fácil. [p=0.3] Você troca cada número por {b}um vizinho redondo, [p=0.2] e aceita um resultado aproximado. [p=0.3] O sinal de {c}aproximadamente é um igual ondulado."),
    dict(id="s05", block="estimar", text="Veja {a}quarenta e oito vezes vinte e um. [p=0.3] Quarenta e oito está perto de {b}cinquenta. [p=0.2] Vinte e um está perto de {c}vinte. [p=0.3] {d}Cinco vezes dois dá dez, [p=0.2] e os dois zeros no fim: {e}mil."),
    dict(id="s06", block="estimar", text="A conta exata dá {a}mil e oito. [p=0.3] A estimativa errou por oito, [p=0.2] e custou dois segundos."),
    dict(id="s07", block="estimar", text="Quando isso basta? [p=0.2] Leia a pergunta. [p=0.2] Se ela diz {a}aproximadamente, ou se as alternativas são {b}cem, mil e dez mil, [p=0.2] a estimativa já escolhe a certa. [p=0.3] Se as alternativas forem {c}mil e oito e mil e dez, [p=0.2] aí só a conta exata resolve."),
    # coração
    dict(id="s08", block="coracao", text="Agora o coração. [p=0.2] Em repouso, ele bate uns {a}setenta vezes por minuto. [p=0.3] Uma hora tem {b}sessenta minutos: [p=0.2] {c}setenta vezes sessenta dá quatro mil e duzentos por hora. [p=0.3] Arredonde para {d}quatro mil."),
    dict(id="s09", block="coracao", text="Um dia tem {a}vinte e quatro horas. [p=0.2] Arredonde para {b}vinte e cinco. [p=0.3] {c}Quatro mil vezes vinte e cinco dá cem mil batidas por dia. [p=0.3] Em notação científica, {d}dez elevado a cinco."),
    dict(id="s10", block="coracao", text="E quantos dias há em setenta anos? [p=0.2] {a}Setenta vezes trezentos e sessenta e cinco. [p=0.3] Troque trezentos e sessenta e cinco por {b}trezentos e sessenta: [p=0.2] {c}sete vezes trinta e seis dá duzentos e cinquenta e dois, [p=0.2] e dois zeros: {d}vinte e cinco mil e duzentos. [p=0.3] Uns {e}dois vírgula cinco vezes dez elevado a quatro dias."),
    dict(id="s11", block="coracao", text="Multiplique: {a}dez elevado a cinco vezes dois vírgula cinco vezes dez elevado a quatro. [p=0.3] Na frente, dois vírgula cinco. [p=0.2] Nas potências, {b}cinco mais quatro dá nove. [p=0.3] {c}Dois vírgula cinco vezes dez elevado a nove: [p=0.2] uns {d}dois bilhões e meio de batidas."),
    dict(id="s12", block="coracao", text="A ordem de grandeza: {a}dois vírgula cinco não passa de três vírgula dezesseis, [p=0.2] então o expoente fica: {b}dez elevado a nove. [p=0.3] A conta exata dá cerca de {c}dois bilhões, quinhentos e setenta e cinco milhões. [p=0.2] Mesma ordem de grandeza."),
    # erro comum
    dict(id="s13", block="erro", text="O erro comum na estimativa é {a}perder um zero. [p=0.3] Cinquenta vezes vinte vira {b}cinco vezes dois dá dez, [p=0.2] e a pessoa põe só um zero: {c}cem. [p=0.3] Mas cinquenta tem um zero, e vinte tem outro. [p=0.2] São {d}dois zeros: mil. [p=0.3] Errar um zero é errar {e}dez vezes."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: [p=0.2] {a}na multiplicação, arredonde um número para cima e o outro para baixo. [p=0.3] Quarenta e oito subiu para cinquenta. [p=0.2] Vinte e um desceu para vinte. [p=0.3] Os erros {b}se compensam, e a estimativa fica perto."),
    dict(id="s15", block="atalho", text="No coração foi igual: [p=0.2] {a}quatro mil e duzentos desceu, [p=0.2] {b}vinte e quatro subiu. [p=0.3] Funciona porque um número que cresce {c}equilibra o outro que diminui. [p=0.3] Não compensa quando descer fica longe demais: [p=0.2] {d}em quarenta e oito vezes vinte e nove, o vinte e nove vai para trinta. [p=0.2] Forçar para vinte erraria por quase quatrocentos."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Em repouso, uma pessoa respira cerca de {a}quinze vezes por minuto. [p=0.3] {b}Estime quantas vezes ela respira em um dia [p=0.2] e {c}dê a ordem de grandeza."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Por hora: {a}quinze vezes sessenta, novecentas. [p=0.2] Arredonde para {b}mil. [p=0.3] Por dia: {c}mil vezes vinte e quatro dá vinte e quatro mil. [p=0.2] Aqui, o vinte e quatro fica como está: o novecentos já subiu."),
    dict(id="s19", block="resposta", text="{a}Vinte e quatro mil é dois vírgula quatro vezes dez elevado a quatro. [p=0.3] Dois vírgula quatro não passa de três vírgula dezesseis: [p=0.2] ordem de grandeza {b}dez elevado a quatro. [p=0.3] A conta exata dá {c}vinte e um mil e seiscentas respirações. [p=0.2] A mesma ordem."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}troque por vizinhos redondos, [p=0.2] {b}conte os zeros com cuidado, [p=0.2] e {c}deixe a pergunta dizer se a estimativa basta."),
    dict(id="s21", block="fim", text="Na próxima aula, você calcula uma conta de água em que {a}cada faixa de consumo tem um preço diferente. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
