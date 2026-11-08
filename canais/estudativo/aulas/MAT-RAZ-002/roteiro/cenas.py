# Estudativo · MAT-RAZ-002 — Proporção: achar o termo desconhecido (Matemática · Razão e Proporção).
# Habilidade: conferir que 2/3 = 6/9 pelo produto cruzado e descobrir x em x/6 = 4/3.
# Pré-requisitos: MAT-RAZ-001 (razão), MAT-FRA-005 (produto cruzado), MAT-EQU-008 (equação). Próxima: MAT-RAZ-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. "Teste da cruz" e "produto cruzado" como em MAT-FRA-003 e MAT-FRA-005.

TITULO = "Proporção: achar o termo desconhecido"

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
    dict(id="s01", block="gancho", text="{a}Xis sobre seis igual a quatro terços. [p=0.3] Quanto vale xis? [p=0.3] Parece coisa de equação difícil, [p=0.2] mas sai em {b}uma multiplicação e uma divisão."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você descobre o número que falta em qualquer proporção, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}o que é razão, [p=0.2] {c}o teste da cruz das frações [p=0.2] e {d}resolver equação fazendo o mesmo nos dois lados. [p=0.3] Se faltar alguma, procure no canal."),
    # proporção
    dict(id="s04", block="proporcao", text="Uma receita usa {a}dois copos de açúcar para três de farinha. [p=0.2] Outra usa {b}seis de açúcar para nove de farinha. [p=0.3] A segunda é só {c}a primeira multiplicada por três. [p=0.2] O sabor é o mesmo."),
    dict(id="s05", block="proporcao", text="As razões são iguais: {a}dois terços igual a seis nonos. [p=0.3] Uma igualdade entre duas razões se chama {b}proporção. [p=0.2] Lê-se assim: {c}dois está para três, assim como seis está para nove."),
    dict(id="s06", block="proporcao", text="Para conferir, use {a}o produto cruzado, o mesmo teste da cruz das frações. [p=0.3] {b}Dois vezes nove dá dezoito. [p=0.2] {c}Três vezes seis dá dezoito. [p=0.2] {d}Deu igual: é proporção. [p=0.3] Nos livros, isso aparece como {e}produto dos meios igual ao produto dos extremos. [p=0.2] Os extremos são o dois e o nove, as pontas da frase. [p=0.2] Os meios, o três e o seis. [p=0.2] É a mesma cruz."),
    # achar x
    dict(id="s07", block="achar", text="E quando falta um número? [p=0.2] Volte para {a}xis sobre seis igual a quatro terços. [p=0.3] Se é proporção, {b}a cruz tem que dar igual. [p=0.2] Então monte a cruz com o xis dentro."),
    dict(id="s08", block="achar", text="{a}Três vezes xis, de um lado. [p=0.2] {b}Seis vezes quatro, do outro. [p=0.3] Fica a equação {c}três xis igual a vinte e quatro. [p=0.2] {d}Divida cada lado por três: [p=0.2] {e}xis igual a oito."),
    dict(id="s09", block="achar", text="Conferindo: {a}oito sextos, dividindo em cima e embaixo por dois, [p=0.2] vira {b}quatro terços. [p=0.2] Bateu."),
    dict(id="s10", block="achar", text="Por que a cruz vale? [p=0.2] Porque é {a}a balança: [p=0.2] multiplique os dois lados por seis e por três. [p=0.3] Do lado do xis, {b}o seis de baixo some e fica três xis. [p=0.2] Do outro, o três de baixo some e fica seis vezes quatro. [p=0.3] Sobra {c}exatamente a cruz."),
    dict(id="s11", block="achar", text="O xis pode estar embaixo também. [p=0.2] {a}Cinco sobre xis igual a dez catorze avos. [p=0.3] Cruz: {b}dez xis igual a cinco vezes catorze dá setenta. [p=0.2] {c}Divida por dez: xis igual a sete."),
    dict(id="s12", block="receita", text="Agora, de volta à receita. [p=0.2] Se você usar {a}oito copos de açúcar, [p=0.2] quantos copos de farinha mantêm o sabor? [p=0.3] {b}Dois está para três, assim como oito está para xis. [p=0.3] Cruz: {c}dois xis igual a três vezes oito dá vinte e quatro. [p=0.2] {d}Xis igual a doze copos de farinha."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}multiplicar reto, em vez de cruzado. [p=0.3] Em xis sobre seis igual a quatro terços, a pessoa faz {b}xis vezes quatro igual a seis vezes três. [p=0.2] Dá {c}quatro xis igual a dezoito, [p=0.2] e xis vira {d}quatro e meio."),
    dict(id="s14", block="erro", text="Dá para ver que está errado sem conta. [p=0.2] Com xis menor que seis, {a}xis sobre seis fica menor que um. [p=0.2] Mas {b}quatro terços é maior que um. [p=0.3] Lembre: {c}a cruz liga o de cima de uma com o de baixo da outra."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho prometido: {a}procure o fator. [p=0.3] Em xis sobre seis igual a quatro terços, {b}de três para seis, multiplicou por dois. [p=0.2] Então em cima também: {c}quatro vezes dois dá oito. [p=0.2] Sem equação."),
    dict(id="s16", block="atalho", text="Funciona porque {a}proporção é fração equivalente: [p=0.2] o que multiplica embaixo, multiplica em cima. [p=0.3] Não compensa quando {b}o fator não é inteiro, [p=0.2] como de quatro para seis. [p=0.2] Aí, {c}vá de cruz."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Ache xis em {a}xis sobre quatro igual a quinze sextos."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] De quatro para seis o fator não é inteiro, então {a}cruz. [p=0.2] {b}Seis xis igual a quatro vezes quinze dá sessenta. [p=0.3] {c}Divida por seis: xis igual a dez."),
    dict(id="s20", block="resposta", text="Conferindo: {a}dez quartos, dividindo em cima e embaixo por dois, [p=0.2] dá cinco dividido por dois. [p=0.3] {b}Quinze sextos, dividindo por três, dá o mesmo. [p=0.3] Quem simplificou quinze sextos antes {c}achou o fator: de dois para quatro, vezes dois. [p=0.2] Cinco vezes dois, {d}o mesmo dez."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}proporção é razão igual a razão, [p=0.2] e {b}com a cruz, ela vira uma equação simples."),
    dict(id="s22", block="fim", text="Na próxima aula, o {a}truque do cá: [p=0.2] você vai achar {b}dois números na razão três para cinco que somam sessenta e quatro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
