# Estudativo · MAT-NUM-007 — Multiplicar por 10, por 100 e por um algarismo (Matemática · Números e Contas).
# Habilidade: calcular 37 × 100 de cabeça, 6 × 23 como 6 × 20 + 6 × 3 e 47 × 6 com a conta armada.
# Pré-requisitos: MAT-NUM-001 (valor posicional), MAT-NUM-003 (somar com vai-um), MAT-NUM-006 (tabuada). Próxima: MAT-NUM-008.
# Questão inédita, criada para esta aula. Sem vírgula: ela só chega em MAT-FRA-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Multiplicar por 10, por 100 e por um algarismo"

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
    dict(id="s01", block="gancho", text="{a}Seis parcelas de {b}quarenta e sete reais. [p=0.3] Se a sua conta deu {c}duzentos e quarenta e dois, [p=0.2] faltaram {d}quarenta reais, [p=0.2] e eles sumiram num número pequeno que muita gente esquece."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai multiplicar por dez e por cem de cabeça, [p=0.2] armar a conta por um algarismo [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}três coisas: [p=0.2] {b}saber o valor de cada algarismo, [p=0.2] {c}somar com vai-um [p=0.2] e {d}a tabuada. [p=0.3] Se faltar alguma, procure no canal."),
    # vezes dez e vezes cem
    dict(id="s04", block="zeros", text="Comece pelo mais fácil. [p=0.2] Quanto é {a}trinta e sete vezes dez? [p=0.3] {b}Sete unidades, repetidas dez vezes, viram {c}sete dezenas. [p=0.2] {d}Três dezenas, repetidas dez vezes, viram {e}três centenas."),
    dict(id="s05", block="zeros", text="Cada algarismo {a}subiu uma casa, [p=0.2] e a casa das unidades ficou vazia. [p=0.2] Quem ocupa casa vazia é o {b}zero: [p=0.2] {c}trezentos e setenta."),
    dict(id="s06", block="zeros", text="Vezes cem, cada algarismo sobe {a}duas casas, [p=0.2] e entram {b}dois zeros. [p=0.3] {c}Trinta e sete vezes cem dá {d}três mil e setecentos."),
    dict(id="s07", block="zeros", text="A regra, para números inteiros como esses: [p=0.2] {a}vezes dez, acrescente um zero no fim. [p=0.2] {b}Vezes cem, acrescente dois zeros. [p=0.3] Vale também para quem já termina em zero: {c}quarenta vezes dez dá quatrocentos. [p=0.3] Preço com centavos fica para outra aula."),
    # quebrar o número
    dict(id="s08", block="quebrar", text="E quando o número não é redondo? [p=0.2] {a}Seis vezes vinte e três. [p=0.3] Imagine {b}seis envelopes. [p=0.2] Em cada envelope, {c}uma nota de vinte reais [p=0.2] e {d}três moedas de um real."),
    dict(id="s09", block="quebrar", text="Junte as notas: {a}seis vezes vinte. [p=0.2] Vinte é dois vezes dez, então faça {b}seis vezes dois, que dá doze, [p=0.2] e {c}acrescente o zero: cento e vinte."),
    dict(id="s10", block="quebrar", text="Junte as moedas: {a}seis vezes três dá dezoito. [p=0.3] {b}Cento e vinte mais dezoito dá {c}cento e trinta e oito. [p=0.3] Você quebrou o vinte e três em {d}vinte mais três [p=0.2] e multiplicou cada pedaço. [p=0.2] O dinheiro é o mesmo, só foi contado por partes."),
    # conta armada
    dict(id="s11", block="conta", text="A conta armada faz exatamente isso, [p=0.2] começando pelas unidades. [p=0.2] Vamos às parcelas do começo: {a}quarenta e sete vezes seis. [p=0.3] {b}O seis fica embaixo do sete. [p=0.2] A ordem não muda o resultado, como na tabuada: [p=0.2] três vezes quatro é igual a quatro vezes três."),
    dict(id="s12", block="conta", text="{a}Seis vezes sete dá quarenta e dois. [p=0.3] Na casa das unidades só cabe um algarismo: [p=0.2] {b}escreva o dois [p=0.2] e {c}o quatro sobe, igual ao vai-um da soma. [p=0.3] O nome é vai-um mesmo quando vão quatro."),
    dict(id="s13", block="conta", text="{a}Seis vezes quatro dá vinte e quatro. [p=0.2] {b}Com o quatro que subiu, vinte e oito. [p=0.3] Não há mais nada para multiplicar, [p=0.2] então ninguém precisa subir: {c}escreva o vinte e oito inteiro. [p=0.2] Resultado: {d}duzentos e oitenta e dois."),
    dict(id="s14", block="conta", text="Confira quebrando: [p=0.2] {a}seis vezes quarenta dá duzentos e quarenta. [p=0.2] {b}Seis vezes sete dá quarenta e dois. [p=0.2] {c}Somando, duzentos e oitenta e dois. [p=0.2] Fecha."),
    # erro
    dict(id="s15", block="erro", text="O erro comum é {a}esquecer de somar o que subiu. [p=0.2] Seis vezes quatro dá {b}vinte e quatro, [p=0.2] a pessoa ignora o vai-um e escreve {c}duzentos e quarenta e dois. [p=0.3] Mas aquele quatro são {d}quatro dezenas: quarenta reais. [p=0.2] O que subiu {e}sempre entra na conta. [p=0.3] E dava para desconfiar: quarenta e sete é quase cinquenta, [p=0.2] e {f}seis vezes cinquenta dá trezentos. [p=0.2] Duzentos e quarenta e dois ficou longe demais."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}vezes noventa e nove. [p=0.3] {b}Noventa e nove parcelas de seis reais. [p=0.2] Faça {c}cem vezes seis: seiscentos. [p=0.2] {d}Tire um seis: [p=0.2] {e}quinhentos e noventa e quatro."),
    dict(id="s17", block="atalho", text="Funciona porque {a}noventa e nove é cem menos um. [p=0.3] Você contou uma parcela a mais, e devolve essa parcela. [p=0.3] {b}Serve para número colado em um redondo. [p=0.2] {c}Longe disso, como em trinta e cinco, não compensa: [p=0.2] aí, arme a conta."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Uma compra foi parcelada em {a}oito vezes [p=0.2] de {b}cinquenta e sete reais. [p=0.3] {c}Qual é o total pago?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] A conta é {a}cinquenta e sete vezes oito. [p=0.3] {b}Oito vezes sete dá cinquenta e seis: [p=0.2] {c}escreva o seis, e o cinco sobe. [p=0.3] {d}Oito vezes cinco dá quarenta. [p=0.2] {e}Com o cinco que subiu, quarenta e cinco. [p=0.2] Total: {f}quatrocentos e cinquenta e seis reais."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}vezes dez e vezes cem, acrescente zeros. [p=0.2] {b}Número difícil, quebre em pedaços. [p=0.2] {c}Na conta armada, some sempre o que subiu."),
    dict(id="s22", block="fim", text="Na próxima aula, {a}o número de baixo também tem dois algarismos, [p=0.2] e a conta ganha {b}uma segunda linha. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
