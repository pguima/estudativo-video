# Estudativo · MAT-FRA-008 — Somar e subtrair com denominadores diferentes (Matemática · Frações e Decimais).
# Habilidade: calcular 1/2 + 1/3 e 3/4 − 1/6 e descobrir que sobra 5/12 de quem gastou 1/4 e 1/3 do salário.
# Pré-requisitos: MAT-FRA-007 (mesmo denominador), MAT-FRA-003 (equivalentes), MAT-DIV-005 (MMC). Próxima: MAT-FRA-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Somar e subtrair frações com denominadores diferentes"

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
    dict(id="s01", block="gancho", text="{a}Um meio {b}mais um terço. [p=0.3] Se a sua resposta foi {c}dois quintos, [p=0.2] você caiu no erro mais comum das frações."),
    dict(id="s02", block="gancho", text="E dá para perceber sem fazer conta nenhuma: {a}dois quintos é menos que um meio. [p=0.3] Você somou, e o resultado {b}diminuiu. [p=0.3] Não pode estar certo."),
    dict(id="s03", block="gancho", text="{a}Até o fim desta aula, você vai somar e subtrair quaisquer frações, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s04", block="lembrete", text="Para acompanhar, você só precisa de {a}três coisas: [p=0.2] {b}somar frações com o mesmo denominador, [p=0.2] {c}trocar uma fração por outra equivalente, [p=0.2] e {d}achar o MMC. [p=0.3] Se faltar alguma, as aulas estão na descrição."),
    # por que não dá
    dict(id="s05", block="barras", text="Por que não dá para somar direto? [p=0.3] Imagine {a}duas barras de chocolate iguais. [p=0.2] Uma foi cortada em {b}duas partes. [p=0.2] A outra, em {c}três."),
    dict(id="s06", block="barras", text="{a}Um meio é um pedaço grande. [p=0.2] {b}Um terço é um pedaço menor. [p=0.3] São tamanhos diferentes, [p=0.2] então somar um pedaço com um pedaço {c}não diz quanto chocolate você tem."),
    dict(id="s07", block="barras", text="A saída é cortar as duas barras no {a}mesmo tamanho de pedaço. [p=0.3] Se cada barra tiver {b}seis partes, [p=0.2] um meio vira {c}três sextos, [p=0.2] e um terço vira {d}dois sextos."),
    dict(id="s08", block="barras", text="Agora os pedaços são iguais, e a conta é a que você já conhece: [p=0.2] {a}três sextos mais dois sextos [p=0.2] dá {b}cinco sextos. [p=0.3] O tamanho do pedaço não muda. [p=0.2] Só contamos quantos são."),
    # método
    dict(id="s09", block="metodo", text="Esse é o método inteiro, e ele tem {a}três passos."),
    dict(id="s10", block="metodo", text="{a}Passo um: achar um denominador comum. [p=0.2] O melhor é o {b}MMC dos denominadores. [p=0.2] MMC de dois e três é {c}seis."),
    dict(id="s11", block="metodo", text="{a}Passo dois: reescrever cada fração com esse denominador. [p=0.2] E aqui entra a frase que resolve tudo: [p=0.2] {b}divide pelo de baixo, [p=0.2] {c}multiplica pelo de cima. [p=0.4] {d}Seis dividido por dois dá três. {e}Três vezes um, três. [p=0.3] {f}Seis dividido por três dá dois. {g}Dois vezes um, dois."),
    dict(id="s12", block="metodo", text="{a}Passo três: soma os de cima e repete o de baixo. [p=0.2] {b}Cinco sextos."),
    # subtração
    dict(id="s13", block="subtrair", text="Com subtração é igual. [p=0.2] Vamos fazer {a}três quartos menos um sexto."),
    dict(id="s14", block="subtrair", text="MMC de quatro e seis: {a}doze. [p=0.3] {b}Doze dividido por quatro dá três; {c}três vezes três, nove. [p=0.3] {d}Doze dividido por seis dá dois; {e}dois vezes um, dois."),
    dict(id="s15", block="subtrair", text="Ficou {a}nove doze avos menos dois doze avos. [p=0.2] Nove menos dois, {b}sete doze avos. [p=0.3] Sete e doze não têm divisor comum além do um, então está pronto."),
    # simplificar no fim
    dict(id="s16", block="simplificar", text="Às vezes ainda dá para {a}simplificar. [p=0.2] Veja {b}um sexto mais três décimos. [p=0.3] MMC de seis e dez: {c}trinta. [p=0.2] Um sexto vira {d}cinco trinta avos. [p=0.2] Três décimos vira {e}nove trinta avos."),
    dict(id="s17", block="simplificar", text="Somando, {a}catorze trinta avos. [p=0.3] Os dois números são pares, então {b}divida em cima e embaixo por dois. [p=0.2] Resposta final: {c}sete quinze avos."),
    # erro
    dict(id="s18", block="erro", text="Agora, cuidado com um erro muito comum. [p=0.2] A pessoa troca o denominador e {a}esquece do numerador. [p=0.2] Escreve um meio como {b}um sexto."),
    dict(id="s19", block="erro", text="Mas um sexto é {a}bem menor que um meio. [p=0.3] Se o de baixo mudou, {b}o de cima tem que acompanhar. [p=0.2] Só assim a fração continua valendo o mesmo."),
    # atalho
    dict(id="s20", block="atalho", text="Agora o atalho prometido: {a}a borboleta. [p=0.3] Ela serve quando são duas frações."),
    dict(id="s21", block="atalho", text="Multiplique em cruz: [p=0.2] {a}um vezes três, três. [p=0.2] {b}Dois vezes um, dois. [p=0.2] Some, e esse é o número de cima: {c}cinco. [p=0.2] Embaixo, multiplique os denominadores: {d}dois vezes três, seis. [p=0.2] {e}Cinco sextos de novo."),
    dict(id="s22", block="atalho", text="Funciona porque ela usa o {a}produto dos denominadores como denominador comum. [p=0.3] É rápida, mas o número pode vir maior: [p=0.2] em três quartos menos um sexto, dá {b}catorze vinte e quatro avos, [p=0.2] e aí você precisa {c}simplificar até sete doze avos."),
    dict(id="s23", block="atalho", text="{a}Denominadores pequenos, borboleta. [p=0.2] {b}Denominadores grandes, MMC."),
    # questão
    dict(id="s24", block="questao", text="Hora de testar. [p=0.2] Uma pessoa gastou {a}um quarto do salário com aluguel [p=0.1] e {b}um terço com mercado. [p=0.3] {c}Que fração do salário sobrou?"),
    dict(id="s25", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s26", block="resposta", text="Vamos lá. [p=0.2] Primeiro, o total gasto: {a}um quarto mais um terço. [p=0.2] O MMC de quatro e três é doze, então fica {b}três doze avos mais quatro doze avos, [p=0.2] que dá {c}sete doze avos."),
    dict(id="s27", block="resposta", text="Mas a pergunta é o que {a}sobrou. [p=0.2] O salário inteiro é {b}doze doze avos. [p=0.2] Doze menos sete: {c}sobraram cinco doze avos do salário."),
    # fechamento
    dict(id="s28", block="fim", text="Resumindo: {a}mesmo denominador, [p=0.2] {b}troca as frações, [p=0.2] {c}soma os de cima. [p=0.3] Com isso, você nunca mais cai nos dois quintos."),
    dict(id="s29", block="fim", text="A próxima aula é {a}multiplicar frações, [p=0.2] e lá você nem precisa de denominador comum. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
