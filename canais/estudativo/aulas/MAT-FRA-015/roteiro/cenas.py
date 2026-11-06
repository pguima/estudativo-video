# Estudativo · MAT-FRA-015 — Somar e subtrair decimais (Matemática · Frações e Decimais).
# Habilidade: calcular 10 − 3,25 alinhando a vírgula e −2,5 + 1,2.
# Pré-requisitos: MAT-FRA-014 (ler e comparar decimais), MAT-NUM-004 (subtrair com a conta armada), MAT-NUM-016 (somar e subtrair inteiros). Próxima: MAT-FRA-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Somar e subtrair decimais"

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
    dict(id="s01", block="gancho", text="{a}Dois vírgula trinta e cinco {b}mais um vírgula quatro. [p=0.3] Se deu {c}dois vírgula quarenta e nove, [p=0.2] a vírgula te enganou."),
    dict(id="s02", block="gancho", text="Dá para perceber sem armar nada: {a}dois inteiros mais um inteiro já dão três. [p=0.3] {b}O resultado não pode ser menor que isso."),
    dict(id="s03", block="gancho", text="{a}Até o fim desta aula, você vai somar e subtrair decimais sem tropeçar, [p=0.2] até com número negativo, [p=0.2] e ainda leva o {b}atalho do troco."),
    # o que precisa saber
    dict(id="s04", block="lembrete", text="Para acompanhar, você só precisa de {a}três coisas: [p=0.2] {b}ler décimos e centésimos, [p=0.2] {c}subtrair pedindo emprestado [p=0.2] e {d}somar inteiros pensando em dívida e pagamento. [p=0.3] Se faltar alguma, procure no canal."),
    # alinhar
    dict(id="s05", block="alinhar", text="A conta armada pede uma coisa só: [p=0.2] {a}vírgula embaixo de vírgula. [p=0.3] Assim, {b}inteiro fica com inteiro, [p=0.2] {c}décimo com décimo [p=0.2] e {d}centésimo com centésimo."),
    dict(id="s06", block="alinhar", text="Um vírgula quatro tem uma casa só. [p=0.2] Complete com zero: {a}um vírgula quarenta. [p=0.3] O valor não muda, e a conta fica sem buraco."),
    dict(id="s07", block="alinhar", text="Some como sempre, da direita para a esquerda: [p=0.2] {a}cinco mais zero, cinco. [p=0.2] {b}Três mais quatro, sete. [p=0.2] A {c}vírgula desce reta. [p=0.2] {d}Dois mais um, três. [p=0.3] Resultado: {e}três vírgula setenta e cinco."),
    # subtrair
    dict(id="s08", block="subtrair", text="Na subtração, a regra é a mesma. [p=0.2] Você paga {a}três reais e vinte e cinco centavos [p=0.2] com {b}uma nota de dez. [p=0.3] {c}Qual é o troco?"),
    dict(id="s09", block="subtrair", text="Todo número inteiro tem {a}uma vírgula escondida no fim. [p=0.2] Dez é o mesmo que {b}dez vírgula zero zero. [p=0.3] Arme assim, {c}vírgula embaixo de vírgula."),
    dict(id="s10", block="subtrair", text="Zero menos cinco não dá, e o vizinho também é zero. [p=0.2] Então {a}o empréstimo vem lá do dez. [p=0.3] Ele vira {b}nove reais, [p=0.2] {c}nove moedas de dez centavos [p=0.2] e {d}dez moedas de um centavo."),
    dict(id="s11", block="subtrair", text="{a}Dez menos cinco, cinco. [p=0.2] {b}Nove menos dois, sete. [p=0.2] {c}Nove menos três, seis. [p=0.3] O troco é {d}seis reais e setenta e cinco centavos."),
    dict(id="s12", block="subtrair", text="Confira com uma soma: {a}seis vírgula setenta e cinco mais três vírgula vinte e cinco [p=0.2] tem que dar {b}dez. [p=0.2] E dá."),
    # negativo
    dict(id="s13", block="negativo", text="E com número negativo? [p=0.2] Veja {a}menos dois vírgula cinco mais um vírgula dois. [p=0.3] O {b}menos dois vírgula cinco é uma dívida de dois reais e cinquenta centavos. [p=0.2] O {c}mais um vírgula dois é um pagamento de um real e vinte centavos."),
    dict(id="s14", block="negativo", text="Na reta, você {a}sai do menos dois vírgula cinco [p=0.2] e {b}anda um vírgula dois para a direita. [p=0.3] A dívida é maior que o pagamento, então {c}você ainda deve."),
    dict(id="s15", block="negativo", text="Quanto? A diferença: {a}dois vírgula cinco menos um vírgula dois [p=0.2] dá {b}um vírgula três. [p=0.3] Como ainda é dívida, o resultado é {c}menos um vírgula três."),
    # erro
    dict(id="s16", block="erro", text="De onde veio aquele dois vírgula quarenta e nove? [p=0.2] A pessoa {a}alinhou pela direita, como nos números inteiros. [p=0.3] Aí o {b}quatro caiu embaixo do cinco: [p=0.2] {c}décimo somado com centésimo. [p=0.3] {d}É como somar moeda de dez centavos com moeda de um centavo, como se valessem o mesmo."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho: {a}o troco do caixa. [p=0.2] Em vez de tirar, {b}suba do preço até a nota. [p=0.3] De três e vinte e cinco até {c}três e cinquenta: vinte e cinco centavos. [p=0.2] Até {d}quatro: mais cinquenta centavos. [p=0.2] Até {e}dez: mais seis reais. [p=0.3] Junte tudo: {f}seis reais e setenta e cinco centavos."),
    dict(id="s18", block="atalho", text="Funciona porque subtrair é {a}medir a distância entre os números, [p=0.2] e essa distância é igual na ida e na volta. [p=0.3] {b}Não compensa com muitas casas decimais: [p=0.2] aí, arme a conta."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Seu saldo está em {a}menos sete vírgula quatro reais. [p=0.2] Você {b}deposita cinco reais. [p=0.3] {c}Qual é o novo saldo?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] A conta é {a}menos sete vírgula quatro mais cinco. [p=0.3] A dívida é maior que o depósito, então {b}você ainda deve. [p=0.3] Use a vírgula escondida do cinco: {c}sete vírgula quatro menos cinco vírgula zero."),
    dict(id="s22", block="resposta", text="{a}Quatro menos zero, quatro. [p=0.2] {b}Sete menos cinco, dois. [p=0.3] Deu {c}dois vírgula quatro, e ainda é dívida: [p=0.2] o novo saldo é {d}menos dois vírgula quatro reais."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}vírgula embaixo de vírgula, [p=0.2] {b}zero para completar as casas [p=0.2] e {c}o sinal de quem for maior, dívida ou pagamento."),
    dict(id="s24", block="fim", text="Na próxima aula, a vírgula {a}sai andando: [p=0.2] você {b}multiplica por cem e divide por mil sem armar conta, [p=0.2] e multiplica {c}decimal por decimal. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
