# Estudativo · MAT-FRA-018 — Dividir por um número decimal (Matemática · Frações e Decimais).
# Habilidade: calcular 1,5 ÷ 0,25 tirando a vírgula do divisor.
# Pré-requisitos: MAT-FRA-016 (andar com a vírgula), MAT-FRA-017 (resultado decimal), MAT-NUM-010 (dois algarismos). Próxima: MAT-FRA-019.
# Questão inédita, criada para esta aula. Sem MDC nem simplificação: esta cadeia não tem MAT-FRA-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Dividir por um número decimal"

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
    dict(id="s01", block="gancho", text="{a}Um vírgula cinco {b}dividido por zero vírgula vinte e cinco. [p=0.3] O resultado é maior ou menor que um vírgula cinco? [p=0.4] Quase todo mundo diz menor, porque dividir parece sempre diminuir. [p=0.3] A resposta é {c}seis."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dividir por qualquer número com vírgula, [p=0.2] sem medo dela, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}andar com a vírgula ao multiplicar por dez ou por cem, [p=0.2] {c}dividir por dois algarismos [p=0.2] e {d}continuar a conta depois da vírgula. [p=0.3] Se faltar alguma, procure no canal."),
    # moedas: por que cresce
    dict(id="s04", block="moedas", text="Por que o resultado cresceu? [p=0.3] Dividir também é perguntar {a}quantas vezes um número cabe no outro. [p=0.3] Imagine que você tem {b}um real e cinquenta centavos [p=0.2] e quer trocar tudo por {c}moedas de vinte e cinco centavos."),
    dict(id="s05", block="moedas", text="{a}Quatro moedas fazem um real. [p=0.2] {b}Mais duas fazem os cinquenta centavos. [p=0.3] São {c}seis moedas. [p=0.3] A moeda é pequena, então {d}cabe muitas vezes. [p=0.2] Por isso o resultado cresceu."),
    # por que andar a vírgula não muda
    dict(id="s06", block="porque", text="Repare em uma coisa. [p=0.2] Em reais, a conta é {a}um vírgula cinco dividido por zero vírgula vinte e cinco. [p=0.3] Em centavos, a mesma conta é {b}cento e cinquenta dividido por vinte e cinco. [p=0.3] O dinheiro é o mesmo, a moeda é a mesma, então {c}o resultado é o mesmo: seis."),
    dict(id="s07", block="porque", text="E passar de reais para centavos é {a}multiplicar por cem, [p=0.2] tanto o dinheiro quanto a moeda. [p=0.3] Multiplicar por cem é {b}andar a vírgula duas casas para a direita. [p=0.3] Esse é o segredo: [p=0.2] andar a vírgula {c}o mesmo tanto no primeiro número e no segundo não muda a divisão. [p=0.2] Só troca reais por centavos."),
    # regra
    dict(id="s08", block="regra", text="Isso vira uma regra de {a}três passos. [p=0.2] {b}Passo um: olhe o divisor, o número que vem depois do sinal de dividir, [p=0.2] e conte as casas depois da vírgula. [p=0.3] Em zero vírgula vinte e cinco, são {c}duas casas."),
    dict(id="s09", block="regra", text="{a}Passo dois: ande a vírgula essas casas para a direita, no divisor e no outro número. [p=0.3] {b}Zero vírgula vinte e cinco vira vinte e cinco. [p=0.2] {c}Um vírgula cinco só tem uma casa, então complete com um zero: [p=0.1] {d}cento e cinquenta."),
    dict(id="s10", block="regra", text="{a}Passo três: divida normalmente. [p=0.2] {b}Vinte e cinco vezes seis, cento e cinquenta. [p=0.2] {c}Deu seis. [p=0.3] Para conferir, {d}multiplique de volta: [p=0.1] seis vezes zero vírgula vinte e cinco dá um vírgula cinco."),
    # exemplo em que o outro número fica com vírgula
    dict(id="s11", block="exemplo", text="Só o divisor precisa perder a vírgula. [p=0.2] O outro número pode ficar com ela. [p=0.3] {a}Um quilo e meio de banana custou {b}três reais e setenta e cinco centavos. [p=0.2] {c}Quanto custa o quilo?"),
    dict(id="s12", block="exemplo", text="A conta é {a}três vírgula setenta e cinco dividido por um vírgula cinco. [p=0.3] O divisor tem {b}uma casa, então ande uma casa em cada número: [p=0.2] {c}trinta e sete vírgula cinco dividido por quinze."),
    dict(id="s13", block="exemplo", text="{a}Trinta e sete dividido por quinze dá dois, e sobram sete. [p=0.2] {b}Ponha a vírgula no resultado [p=0.2] e {c}desça o cinco: setenta e cinco. [p=0.2] {d}Setenta e cinco dividido por quinze dá cinco. [p=0.3] O quilo custa {e}dois reais e cinquenta centavos."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: {a}andar a vírgula só no divisor. [p=0.2] A pessoa faz {b}um vírgula cinco dividido por vinte e cinco [p=0.2] e acha {c}zero vírgula zero seis."),
    dict(id="s15", block="erro", text="É como trocar a moeda de vinte e cinco centavos por {a}vinte e cinco reais, [p=0.2] sem mudar o dinheiro que você tem. [p=0.3] Mudou um número, {b}muda o outro também, [p=0.2] o mesmo tanto de casas."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho. [p=0.2] {a}Dividir por zero vírgula cinco é dobrar. [p=0.2] {b}Dividir por zero vírgula vinte e cinco é multiplicar por quatro. [p=0.3] {c}Um vírgula cinco vezes quatro: seis, sem armar nada."),
    dict(id="s17", block="atalho", text="Funciona porque {a}zero vírgula cinco cabe duas vezes em cada inteiro, [p=0.2] e {b}zero vírgula vinte e cinco cabe quatro vezes, [p=0.2] como as moedas no real. [p=0.3] Não compensa com divisores como {c}zero vírgula sete: [p=0.2] aí, tire a vírgula."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Um rolo tem {a}cinco vírgula quatro metros de fita. [p=0.2] Cada laço usa {b}zero vírgula quarenta e cinco metro. [p=0.3] {c}Quantos laços dá para fazer, usando a fita toda?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] A conta é {a}cinco vírgula quatro dividido por zero vírgula quarenta e cinco. [p=0.2] O divisor tem {b}duas casas. [p=0.2] Ande duas casas em cada número: {c}quinhentos e quarenta dividido por quarenta e cinco."),
    dict(id="s21", block="resposta", text="{a}Cinquenta e quatro dividido por quarenta e cinco dá um, e sobram nove. [p=0.2] {b}Desça o zero: noventa. [p=0.2] {c}Noventa dividido por quarenta e cinco dá dois. [p=0.3] Resposta: {d}doze laços."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}conte as casas do divisor, [p=0.2] {b}ande a vírgula igual no primeiro e no segundo número [p=0.2] e {c}divida normalmente."),
    dict(id="s23", block="fim", text="Na próxima aula, você aprende a {a}trocar fração por decimal [p=0.2] e {b}decimal por fração. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
