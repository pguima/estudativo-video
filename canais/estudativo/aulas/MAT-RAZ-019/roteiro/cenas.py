# Estudativo · MAT-RAZ-019 — Praticando: divisão proporcional, velocidade, densidade e vazão (Matemática · Razão e Proporção · prática).
# Habilidade: repartir lucros em partes proporcionais e resolver problemas de viagem, densidade e torneiras.
# Pré-requisitos: MAT-RAZ-013, MAT-RAZ-014, MAT-RAZ-015, MAT-RAZ-016, MAT-RAZ-017, MAT-RAZ-018, MAT-RAZ-024, MAT-RAZ-025. Próxima: MAT-RAZ-020.
# Questões inéditas, criadas para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: divisão proporcional, velocidade, densidade e vazão"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, [p=0.2] criadas para esta aula: [p=0.2] {b}sócios, prêmio, viagem, um objeto na água e uma caixa-d'água. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}o cá, que é o valor de uma parte, [p=0.2] {b}a palavra por, que quer dizer dividido, [p=0.2] {c}velocidade média, que é distância total sobre tempo total, [p=0.2] e {d}as unidades, que conferem a conta. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: direta com tempo
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] A Lia pôs {b}seis mil reais num negócio, por quatro meses. [p=0.2] O Rui pôs {c}quatro mil reais, por nove meses. [p=0.3] O lucro foi de {d}cinco mil reais. [p=0.2] {e}Quanto cada um recebe?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Tem tempo na história, então o peso é {a}capital vezes tempo. [p=0.2] Lia: {b}seis mil vezes quatro dá vinte e quatro mil. [p=0.2] Rui: {c}quatro mil vezes nove dá trinta e seis mil. [p=0.3] Dividindo por doze mil, os pesos ficam {d}dois e três."),
    dict(id="s06", block="resposta1", text="{a}Dois cá mais três cá igual a cinco mil. [p=0.2] Cinco cá igual a cinco mil, e o cá é {b}mil. [p=0.3] {c}Lia, dois mil reais. [p=0.2] {d}Rui, três mil reais. [p=0.3] Quem olha só o capital dá mais para a Lia, [p=0.2] mas o Rui ficou mais que o dobro do tempo."),
    # situação 2: inversa
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Um prêmio de {b}mil e duzentos reais vai ser dividido entre três pessoas, [p=0.2] {c}de forma inversa às faltas. [p=0.3] Elas tiveram {d}duas, três e seis faltas. [p=0.2] {e}Quanto recebe cada uma?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Inversa às faltas é direta aos inversos. [p=0.2] Pelo atalho, {a}o MMC dividido por cada número. [p=0.2] MMC de dois, três e seis: {b}seis. [p=0.2] Os pesos são {c}três, dois e um."),
    dict(id="s10", block="resposta2", text="A soma dos pesos é seis. [p=0.2] {a}Mil e duzentos dividido por seis dá duzentos. [p=0.3] {b}Seiscentos, quatrocentos e duzentos reais. [p=0.3] Confira com o produto: [p=0.2] {c}seiscentos vezes duas faltas, mil e duzentos. [p=0.2] Quatrocentos vezes três, também. [p=0.2] Duzentos vezes seis, também. [p=0.2] {d}É inversa de verdade."),
    # situação 3: viagem
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Um caminhão carregado sobe uma serra de {b}noventa quilômetros a trinta quilômetros por hora. [p=0.2] Volta vazio, pela mesma estrada, {c}a quarenta e cinco quilômetros por hora. [p=0.3] {d}Sem contar paradas, qual foi a velocidade média na ida e volta? [p=0.2] E {e}quanto é isso em metros por segundo?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] A média das velocidades daria {a}trinta e sete e meio, e é a armadilha. [p=0.3] Use distância total sobre tempo total. [p=0.2] Subida: {b}noventa dividido por trinta dá três horas. [p=0.2] Descida: {c}noventa dividido por quarenta e cinco dá duas horas."),
    dict(id="s14", block="resposta3", text="Distância total: {a}cento e oitenta quilômetros. [p=0.2] Tempo total: {b}cinco horas. [p=0.2] {c}Trinta e seis quilômetros por hora. [p=0.3] Pelo atalho da ida e volta dá o mesmo: [p=0.2] {d}duas vezes trinta vezes quarenta e cinco, dois mil e setecentos, dividido por setenta e cinco dá trinta e seis. [p=0.3] E trinta e seis é um dos pares do atalho: {e}dez metros por segundo."),
    # situação 4: densidade
    dict(id="s15", block="questao4", text="{a}Situação quatro. [p=0.2] Um bloco de madeira tem {b}seiscentos gramas [p=0.1] e {c}oitocentos centímetros cúbicos de volume. [p=0.3] {d}Qual é a densidade dele? [p=0.2] {e}Ele boia na água?"),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Vamos lá. [p=0.2] Densidade é {a}massa dividida pelo volume. [p=0.2] {b}Seiscentos dividido por oitocentos: [p=0.2] simplifique por duzentos, {c}três quartos, [p=0.2] ou {d}zero vírgula setenta e cinco grama por centímetro cúbico."),
    dict(id="s18", block="resposta4", text="A água tem densidade de {a}um grama por centímetro cúbico. [p=0.2] O bloco tem menos que a água, então {b}boia. [p=0.2] Pelo atalho, {c}seiscentos é menor que oitocentos: boia de novo. [p=0.3] Cuidado com a ordem da divisão: [p=0.2] quem faz oitocentos dividido por seiscentos acha um número {d}maior que um, [p=0.2] e afunda um bloco que boia."),
    # situação 5: torneiras
    dict(id="s19", block="questao5", text="{a}Última situação. [p=0.2] Uma caixa-d'água enche em {b}duas horas com uma torneira [p=0.1] e em {c}três horas com outra. [p=0.3] {d}Com as duas ligadas, em quantas horas e minutos ela enche?"),
    dict(id="s20", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta5", text="Vamos lá. [p=0.2] Produto sobre soma: {a}dois vezes três dá seis. [p=0.2] {b}Dois mais três dá cinco. [p=0.2] {c}Seis dividido por cinco dá um vírgula dois hora. [p=0.3] Pelas frações dá o mesmo: [p=0.2] {d}um meio mais um terço, cinco sextos da caixa por hora. [p=0.2] A caixa inteira são seis sextos, e seis dividido por cinco dá um vírgula dois de novo. [p=0.3] E repare: {e}aqui não tem o dobro do atalho da viagem. [p=0.2] Na ida e volta, a viagem tem dois trechos, e daí vem o dobro. [p=0.2] Aqui, a caixa é uma só."),
    dict(id="s22", block="resposta5", text="Agora, cuidado: um vírgula dois hora {a}não é uma hora e vinte minutos. [p=0.2] Use as unidades: [p=0.2] {b}zero vírgula dois hora vezes sessenta minutos por hora. [p=0.2] A hora corta, e sobram {c}doze minutos. [p=0.2] Confere com o atalho: cada décimo de hora são seis minutos. [p=0.3] {d}Uma hora e doze minutos. [p=0.2] Menos que as duas horas da torneira mais rápida: faz sentido."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}ache o peso certo antes de dividir, [p=0.2] {b}some tempos e distâncias, não velocidades, [p=0.2] e {c}deixe as unidades conferirem a conta."),
    dict(id="s24", block="fim", text="Na próxima aula, a razão vai parar no mapa: {a}a escala. [p=0.2] Você vai ler {b}um para cem [p=0.1] e descobrir quantos quilômetros valem três centímetros de mapa. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
