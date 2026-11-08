# Estudativo · MAT-POT-013 — Contas em notação científica (Matemática · Potências e Raízes).
# Habilidade: calcular (3 × 10⁵) · (4 × 10²) = 1,2 × 10⁸, somar 3 × 10⁵ + 8 × 10⁴ e dizer quantas vezes a massa da Terra é maior que a da Lua.
# Pré-requisitos: MAT-FRA-015 (somar decimais), MAT-FRA-016 (andar com a vírgula), MAT-FRA-018 (dividir por decimal), MAT-POT-003 (mesma base), MAT-POT-012 (notação científica). Próxima: MAT-POT-014.
# Questão inédita, criada para esta aula. A gráfica e a fábrica de garrafas são invenção.
# Fatos: Terra 5,97 × 10²⁴ kg e Lua 7,35 × 10²² kg (NASA NSSDC, Earth e Moon Fact Sheets: 5,9722 e 0,07346 × 10²⁴ kg; razão real 81,3).
# Arredondados na aula para 6 × 10²⁴ e 7,4 × 10²², que dão cerca de 81.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Contas em notação científica"

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
    dict(id="s01", block="gancho", text="{a}Três vezes dez elevado a cinco {b}mais oito vezes dez elevado a quatro. [p=0.3] Se você somou três com oito e escreveu {c}onze vezes dez elevado a cinco, [p=0.2] sua resposta saiu quase o triplo do valor certo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai multiplicar, dividir e somar em notação científica, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}escrever em notação científica, [p=0.2] {c}multiplicar e dividir potências de mesma base [p=0.2] e {d}fazer contas com decimais. [p=0.3] Se faltar alguma, procure no canal."),
    # multiplicar
    dict(id="s04", block="multiplicar", text="Uma gráfica enviou {a}trezentas mil caixas, [p=0.2] cada uma com {b}quatrocentas folhas. [p=0.3] Em notação científica: {c}três vezes dez elevado a cinco, [p=0.2] vezes {d}quatro vezes dez elevado a dois."),
    dict(id="s05", block="multiplicar", text="Na multiplicação, a ordem não muda o resultado. [p=0.2] Então {a}junte os números da frente [p=0.2] e {b}junte as potências. [p=0.3] {c}Três vezes quatro dá doze. [p=0.2] Nas potências, mesma base, soma os expoentes: {d}dez elevado a sete."),
    dict(id="s06", block="multiplicar", text="Deu {a}doze vezes dez elevado a sete. [p=0.3] O valor está certo, mas {b}a forma não: doze passa de dez. [p=0.3] Ande a vírgula uma casa para a esquerda: {c}um vírgula dois. [p=0.2] A frente ficou dez vezes menor, então {d}a potência fica dez vezes maior: [p=0.2] o expoente sobe de sete para oito."),
    dict(id="s07", block="multiplicar", text="Resposta: {a}um vírgula dois vezes dez elevado a oito. [p=0.3] São {b}cento e vinte milhões de folhas."),
    # dividir
    dict(id="s08", block="terra", text="Dividir é parecido: {a}divida os números da frente [p=0.2] e {b}subtraia os expoentes. [p=0.3] Massa é a quantidade de matéria, o que a balança mede. [p=0.2] A da Terra é {c}cerca de seis vezes dez elevado a vinte e quatro quilos. [p=0.2] A da Lua, {d}cerca de sete vírgula quatro vezes dez elevado a vinte e dois quilos."),
    dict(id="s09", block="terra", text="{a}Quantas vezes a massa da Terra é maior? [p=0.3] Divida {b}seis por sete vírgula quatro. [p=0.2] Tirando a vírgula do divisor, é {c}sessenta dividido por setenta e quatro, [p=0.2] que dá {d}cerca de zero vírgula oitenta e um."),
    dict(id="s10", block="terra", text="Nas potências, {a}vinte e quatro menos vinte e dois: dez elevado a dois, que é cem. [p=0.3] {b}Zero vírgula oitenta e um vezes cem. [p=0.2] A vírgula anda duas casas para a direita: {c}cerca de oitenta e uma vezes. [p=0.3] A frente ficou abaixo de um, mas a pergunta pede um número comum, então aqui não precisa da forma."),
    # somar
    dict(id="s11", block="soma", text="Somar é diferente. [p=0.2] Volte para {a}três vezes dez elevado a cinco {b}mais oito vezes dez elevado a quatro. [p=0.3] Imagine notas: [p=0.2] {c}três notas de cem mil [p=0.2] e {d}oito notas de dez mil."),
    dict(id="s12", block="soma", text="As notas têm {a}valores diferentes, [p=0.2] então não dá para juntar três com oito. [p=0.3] Por isso, a soma {b}só funciona com o mesmo expoente. [p=0.3] Por extenso: {c}trezentos mil mais oitenta mil dá {d}trezentos e oitenta mil."),
    dict(id="s13", block="soma", text="O método é {a}igualar os expoentes, passando para o maior. [p=0.3] {b}Oito vezes dez elevado a quatro vira {c}zero vírgula oito vezes dez elevado a cinco. [p=0.3] A frente ficou dez vezes menor, e a potência, dez vezes maior. [p=0.2] O valor é o mesmo."),
    dict(id="s14", block="soma", text="Com o mesmo expoente, some os da frente: [p=0.2] {a}três mais zero vírgula oito dá três vírgula oito. [p=0.3] Resposta: {b}três vírgula oito vezes dez elevado a cinco, [p=0.2] os mesmos {c}trezentos e oitenta mil."),
    # erro
    dict(id="s15", block="erro", text="O erro comum é o do começo: {a}somar os da frente sem igualar os expoentes. [p=0.3] Onze vezes dez elevado a cinco é {b}um milhão e cem mil. [p=0.3] Mas trezentos mil mais oitenta mil {c}não chega nem a meio milhão. [p=0.3] {d}Multiplicar e dividir não pedem expoente igual. {e}Somar e subtrair pedem."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho da multiplicação: {a}ache o expoente antes da conta. [p=0.3] {b}Some os expoentes. [p=0.2] Se os números da frente derem {c}dez ou mais, {d}some mais um. [p=0.3] Três vezes quatro passou de dez: {e}sete mais um dá oito."),
    dict(id="s17", block="atalho", text="Funciona porque cada número da frente é menor que dez, [p=0.2] então o produto {a}fica abaixo de cem, [p=0.2] e basta {b}um ajuste. [p=0.3] Serve para {c}eliminar alternativas. [p=0.3] {d}Não compensa na soma: aí, iguale os expoentes."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Uma fábrica produz {a}seis vezes dez elevado a quatro garrafas por dia. [p=0.3] Ela funcionou por {b}cinco vezes dez elevado a dois dias. [p=0.3] {c}Quantas garrafas produziu, em notação científica?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Seis vezes cinco dá trinta. [p=0.2] {b}Quatro mais dois dá seis: dez elevado a seis. [p=0.3] Ficou {c}trinta vezes dez elevado a seis."),
    dict(id="s21", block="resposta", text="Trinta passa de dez. [p=0.2] Ande a vírgula uma casa para a esquerda: {a}três. [p=0.2] {b}O expoente sobe de seis para sete. [p=0.3] Resposta: {c}três vezes dez elevado a sete garrafas, [p=0.2] ou {d}trinta milhões."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}multiplicar soma expoentes, [p=0.2] {b}dividir subtrai, [p=0.2] e {c}conta de mais ou de menos pede expoente igual. [p=0.3] E, em notação científica, {d}a frente fica de um até menos de dez."),
    dict(id="s23", block="fim", text="Na próxima aula, você vai conhecer a {a}ordem de grandeza: [p=0.2] a potência de dez mais próxima de um número, [p=0.2] e por que a referência é {b}três vírgula dezesseis. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
