# Estudativo · MAT-RAZ-009 — Regra de três composta com grandeza inversa (Matemática · Razão e Proporção).
# Habilidade: descobrir quantos dias 18 operários, trabalhando 10 h por dia, levam num muro feito por 12 operários em 15 dias de 8 h, com o atalho 12 · 8 · 15 = 18 · 10 · x.
# Pré-requisitos: MAT-RAZ-007 (regra de três inversa), MAT-RAZ-008 (composta com grandezas diretas). Próxima: MAT-RAZ-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Mesmos termos de MAT-RAZ-007 (trabalho total, multiplicar na linha) e MAT-RAZ-008 (uma de cada vez, colunas).
# Uma de cada vez: 12 · 15 = 180; 180 ÷ 18 = 10 dias; 10 · 8 = 80 h; 80 ÷ 10 = 8 dias.
# Colunas: 15/x = 18/12 · 10/8 = 180/96 = 15/8 → x = 8. Erro (tudo direto): 15/x = 12/18 · 8/10 = 96/180 = 8/15 → x = 225/8 = 28,125.
# Atalho: 12 · 8 · 15 = 1.440 = 18 · 10 · x = 180x → x = 8.
# Questão: 4 jardineiros, 6 h/dia, 15 dias → 5 jardineiros, 8 h/dia: 4 · 6 · 15 = 360 = 40x → x = 9; colunas 15/x = 5/4 · 8/6 = 40/24 = 5/3 → x = 9.

TITULO = "Regra de três composta com grandeza inversa"

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
    dict(id="s01", block="gancho", text="{a}Doze operários, trabalhando oito horas por dia, levantam um muro em quinze dias. [p=0.3] {b}Dezoito operários, trabalhando dez horas por dia, levam quantos dias? [p=0.3] Mais gente, mais horas, [p=0.2] e tem quem responda {c}mais de vinte e oito dias."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve a regra de três composta com grandeza inversa, [p=0.2] e ainda leva um {b}atalho de uma linha só."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}na regra de três inversa, a multiplicação de cada linha não muda, [p=0.2] e {c}na composta, você muda uma grandeza de cada vez. [p=0.3] Se faltar alguma, procure no canal."),
    # uma de cada vez
    dict(id="s04", block="ideia", text="Primeiro, só os operários mudam. [p=0.2] As horas ficam paradas em oito por dia. [p=0.3] {a}Doze operários em quinze dias: um operário sozinho levaria {b}doze vezes quinze dá cento e oitenta dias. [p=0.2] Com dezoito, {c}cento e oitenta dividido por dezoito dá dez dias."),
    dict(id="s05", block="ideia", text="Agora mudam as horas. [p=0.2] {a}Dez dias de oito horas são oitenta horas com a equipe inteira trabalhando. [p=0.3] Trabalhando dez horas por dia, {b}oitenta dividido por dez dá oito dias. [p=0.3] Resposta: {c}oito dias. [p=0.2] Mais gente e mais horas: {d}menos dias."),
    # colunas
    dict(id="s06", block="metodo", text="Pelas colunas, o caminho é o da aula anterior, {a}com um passo a mais. [p=0.3] {b}Operários: doze e dezoito. [p=0.2] {c}Horas por dia: oito e dez. [p=0.2] {d}Dias: quinze e xis."),
    dict(id="s07", block="metodo", text="Compare {a}cada coluna com a do xis, uma de cada vez. [p=0.3] {b}Dobrando os operários, os dias caem pela metade: inversa. [p=0.2] {c}Dobrando as horas por dia, os dias também caem pela metade: inversa."),
    dict(id="s08", block="metodo", text="O passo a mais: {a}vire as colunas inversas antes de montar. [p=0.3] Operários vira {b}dezoito doze avos. [p=0.2] Horas vira {c}dez oitavos. [p=0.3] A coluna do xis {d}nunca vira."),
    dict(id="s09", block="metodo", text="Agora, como antes: {a}quinze dividido por xis igual à multiplicação das outras frações. [p=0.3] {b}Dezoito vezes dez dá cento e oitenta. [p=0.2] {c}Doze vezes oito dá noventa e seis. [p=0.3] Simplificando por doze, {d}quinze oitavos. [p=0.2] Quinze dividido por xis igual a quinze oitavos: {e}xis igual a oito."),
    # erro comum
    dict(id="s10", block="erro", text="E os mais de vinte e oito dias do começo? [p=0.2] Saem de {a}tratar tudo como direto, sem virar nada. [p=0.3] {b}Quinze dividido por xis igual a doze dezoito avos vezes oito décimos. [p=0.2] O produto cruzado dá {c}vinte e oito dias e mais um pedaço."),
    dict(id="s11", block="erro", text="O bom senso pega esse erro: [p=0.2] {a}mais operários e mais horas não podem dar mais dias. [p=0.3] E lembre: {b}compare cada coluna só com a do xis, [p=0.2] {c}nunca uma com a outra."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: [p=0.2] {a}multiplique tudo em cada linha e iguale. [p=0.3] {b}Doze operários vezes oito horas vezes quinze dias: mil quatrocentos e quarenta horas de trabalho. [p=0.3] Nas apostilas, isso se chama {c}homem-hora."),
    dict(id="s13", block="atalho", text="Na outra linha, {a}dezoito vezes dez vezes xis. [p=0.2] Dezoito vezes dez dá {b}cento e oitenta xis, [p=0.2] {c}igual a mil quatrocentos e quarenta. [p=0.3] {d}Mil quatrocentos e quarenta dividido por cento e oitenta: oito dias. [p=0.3] Sem virar nenhuma coluna."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o muro é o mesmo, então o total de horas trabalhadas também é. [p=0.3] {b}Não vale se a obra mudar de tamanho. [p=0.2] Com um muro {c}duas vezes maior, o total de horas dobra. [p=0.2] Aí, {d}volte para as colunas e crie uma coluna para o tamanho do muro."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Quatro jardineiros, trabalhando seis horas por dia, cuidam de um parque em quinze dias. [p=0.3] {b}Cinco jardineiros, trabalhando oito horas por dia, cuidam do mesmo parque em quantos dias?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá, pelo atalho. [p=0.2] {a}Quatro vezes seis vezes quinze: trezentas e sessenta horas de trabalho. [p=0.3] {b}Cinco vezes oito vezes xis: quarenta xis. [p=0.2] {c}Trezentos e sessenta dividido por quarenta: nove dias."),
    dict(id="s18", block="resposta", text="Mais gente e mais horas, menos dias: {a}faz sentido. [p=0.3] Pelas colunas, jardineiros e horas por dia são inversas e viram: [p=0.2] {b}cinco quartos vezes oito sextos dá cinco terços. [p=0.2] {c}Quinze dividido por xis igual a cinco terços, [p=0.2] e o produto cruzado dá os mesmos {d}nove dias."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}compare cada coluna com a do xis, [p=0.2] {b}vire as inversas [p=0.2] e, quando a obra é a mesma, {c}multiplique tudo em cada linha."),
    dict(id="s20", block="fim", text="Na próxima aula, uma relação que não é direta nem inversa: [p=0.2] {a}dobre o lado de um quadrado [p=0.2] e {b}a área fica quatro vezes maior. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
