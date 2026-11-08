# Estudativo · MAT-RAZ-025 — Unidades como guia (Matemática · Razão e Proporção).
# Habilidade: descobrir quantos litros uma torneira pingando desperdiça em 30 dias só encaixando gotas, litros e dias até as unidades se cancelarem.
# Pré-requisitos: MAT-FRA-009 (multiplicar frações), MAT-RAZ-018 (vazão). Próxima: MAT-RAZ-019.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Dado usado: vinte gotas fazem um mililitro (valor de referência, dito como suposição do problema).

TITULO = "Unidades como guia"

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
    dict(id="s01", block="gancho", text="Uma torneira pingando parece não gastar nada. [p=0.2] {a}Uma gota aqui, outra ali. [p=0.3] Em um mês, ela pode jogar fora {b}mais de quarenta litros de água."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai fazer essa conta sem decorar nenhuma regra. [p=0.2] Quem monta a conta são {b}as próprias unidades."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}multiplicar frações, cortando em cruz, [p=0.2] e {c}ler uma vazão, como litros por minuto. [p=0.3] Se faltar alguma, procure no canal."),
    # unidade corta
    dict(id="s04", block="corta", text="Comece por algo conhecido. [p=0.2] Um carro a {a}oitenta quilômetros por hora, durante {b}três horas. [p=0.3] {c}Oitenta vezes três dá duzentos e quarenta quilômetros."),
    dict(id="s05", block="corta", text="Agora olhe as unidades. [p=0.2] Quilômetro por hora é {a}quilômetro em cima, hora embaixo. [p=0.2] Vezes {b}hora em cima. [p=0.3] Hora em cima e hora embaixo {c}se cortam, como números no cortar em cruz. [p=0.2] Sobra {d}quilômetro. [p=0.3] A unidade do resultado saiu sozinha. [p=0.2] Na aula de velocidade, ela já servia para conferir a conta. [p=0.2] Aqui, ela vai {e}montar a conta."),
    # fator que vale um
    dict(id="s06", block="fator", text="A segunda peça é o {a}fator de conversão. [p=0.2] Uma hora tem sessenta minutos. [p=0.2] Então {b}sessenta minutos sobre uma hora é a mesma quantidade em cima e embaixo."),
    dict(id="s07", block="fator", text="Uma fração com a mesma quantidade em cima e embaixo {a}vale um. [p=0.2] Multiplicar por um não muda o valor. [p=0.2] {b}Só troca a unidade. [p=0.3] E você escolhe o lado: a unidade que você quer sumir vai {c}do lado oposto, para cortar."),
    # torneira
    dict(id="s08", block="torneira", text="Vamos à torneira. [p=0.2] Ela pinga {a}vinte gotas por minuto. [p=0.2] Suponha que {b}vinte gotas fazem um mililitro. [p=0.3] {c}Quantos litros ela desperdiça em trinta dias?"),
    dict(id="s09", block="torneira", text="Comece pelo que tem: {a}vinte gotas por minuto. [p=0.2] Para sumir com gota, ponha gota embaixo: [p=0.2] {b}vezes um mililitro sobre vinte gotas. [p=0.3] {c}Gota corta com gota, e vinte corta com vinte. [p=0.2] Sobra {d}um mililitro por minuto."),
    dict(id="s10", block="torneira", text="Minuto está embaixo. [p=0.2] Ponha minuto em cima: {a}vezes sessenta minutos sobre uma hora. [p=0.2] Minuto corta, e fica {b}sessenta mililitros por hora."),
    dict(id="s11", block="torneira", text="Hora está embaixo. [p=0.2] {a}Vezes vinte e quatro horas sobre um dia. [p=0.2] {b}Sessenta vezes vinte e quatro dá mil quatrocentos e quarenta mililitros por dia."),
    dict(id="s12", block="torneira", text="Dia está embaixo, e o problema dá {a}trinta dias. [p=0.2] Vezes trinta dias, e o dia corta: [p=0.2] {b}quarenta e três mil e duzentos mililitros."),
    dict(id="s13", block="torneira", text="Falta chegar em litro. [p=0.2] {a}Vezes um litro sobre mil mililitros. [p=0.2] Dividir por mil é {b}andar com a vírgula três casas para a esquerda. [p=0.3] {c}Quarenta e três vírgula dois litros, [p=0.2] jogados fora gota a gota."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: {a}o fator de cabeça para baixo. [p=0.2] A pessoa quer passar de um mililitro por minuto para mililitro por hora, [p=0.2] e {b}divide por sessenta."),
    dict(id="s15", block="erro", text="Dá {a}um sessenta avos de mililitro por hora. [p=0.2] Mas em uma hora pinga muito mais que em um minuto! [p=0.3] As unidades denunciam: no fator {b}uma hora sobre sessenta minutos, [p=0.2] o minuto fica {c}embaixo duas vezes, e nada corta. [p=0.3] Se a unidade não cortou, {d}vire o fator."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho de prova: {a}monte a fila inteira antes de fazer qualquer conta. [p=0.3] Corte as unidades {b}e os números em cruz, [p=0.2] e só multiplique no fim."),
    dict(id="s17", block="atalho", text="Funciona porque, numa fila de multiplicações, tudo de cima se multiplica junto, e tudo de baixo também. [p=0.2] Na torneira, {a}o vinte de cima corta com o vinte de baixo, [p=0.2] e as contas ficam menores."),
    dict(id="s18", block="atalho", text="Não compensa numa conversão de {a}um passo só, como duas horas em minutos. [p=0.2] Aí, {b}multiplique direto."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Um chuveiro gasta {a}nove litros por minuto. [p=0.2] Uma pessoa toma {b}um banho de dez minutos por dia. [p=0.3] {c}Quantos metros cúbicos de água ela gasta em trinta dias?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] {a}Nove litros por minuto, vezes dez minutos por dia: [p=0.2] o minuto corta, {b}noventa litros por dia. [p=0.3] Vezes trinta dias: {c}dois mil e setecentos litros."),
    dict(id="s22", block="resposta", text="Um metro cúbico são mil litros. [p=0.2] Então, {a}vezes um metro cúbico sobre mil litros: [p=0.2] o litro corta, e a vírgula anda três casas para a esquerda. [p=0.3] {b}Dois vírgula sete metros cúbicos."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}escreva com as unidades, [p=0.2] {b}multiplique por fatores que valem um, [p=0.2] e {c}pare quando sobrar só a unidade que a pergunta pede."),
    dict(id="s24", block="fim", text="Na próxima aula, {a}você pratica tudo desta parte do curso: [p=0.2] {b}dividir em partes proporcionais, velocidade, densidade e vazão. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
