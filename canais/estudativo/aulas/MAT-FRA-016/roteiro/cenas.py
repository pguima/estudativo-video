# Estudativo · MAT-FRA-016 — Multiplicar decimais e andar com a vírgula (Matemática · Frações e Decimais).
# Habilidade: calcular 3,7 × 100 e 45 ÷ 1.000 só andando com a vírgula e 1,2 × 0,3 = 0,36, inclusive com sinal negativo.
# Pré-requisitos: MAT-FRA-014 (casas decimais), MAT-NUM-008 (multiplicar por dois algarismos), MAT-NUM-017 (regra de sinais). Próxima: MAT-FRA-017.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Multiplicar decimais e andar com a vírgula"

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
    dict(id="s01", block="gancho", text="Um metro de fita custa {a}trinta centavos. [p=0.2] Você leva {b}um metro e vinte. [p=0.3] A conta é {c}um vírgula dois vezes zero vírgula três. [p=0.3] Se deu {d}três vírgula seis, [p=0.2] você pagou três reais e sessenta centavos em pouco mais de um metro de fita barata."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai multiplicar decimais, até com sinal negativo, [p=0.2] andar com a vírgula sem armar conta [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}três coisas: [p=0.2] {b}saber o que é casa decimal, [p=0.2] {c}multiplicar por dois algarismos [p=0.2] e {d}a regra de sinais. [p=0.3] Se faltar alguma, procure no canal."),
    # andar com a vírgula
    dict(id="s04", block="andar", text="Comece pelo mais fácil. [p=0.2] {a}Cem pessoas pagam três reais e setenta centavos cada. [p=0.3] A conta é {b}três vírgula sete vezes cem."),
    dict(id="s05", block="andar", text="{a}Cem tem dois zeros, [p=0.2] então {b}a vírgula anda duas casas para a direita. [p=0.3] {c}Uma casa: trinta e sete. [p=0.2] {d}Duas casas: trezentos e setenta, completando com zero. [p=0.3] São {e}trezentos e setenta reais."),
    dict(id="s06", block="andar", text="Por que funciona? [p=0.2] {a}Sete moedas de dez centavos, multiplicadas por dez, viram {b}sete reais. [p=0.3] Cada algarismo sobe uma casa. [p=0.2] Na tela, parece que {c}foi a vírgula que andou."),
    dict(id="s07", block="andar", text="Dividir é o caminho de volta. [p=0.2] {a}Quarenta e cinco dividido por mil. [p=0.3] Todo número inteiro tem {b}uma vírgula escondida no fim: [p=0.2] quarenta e cinco é o mesmo que quarenta e cinco vírgula zero. [p=0.3] {c}Mil tem três zeros, então ela anda três casas para a esquerda."),
    dict(id="s08", block="andar", text="{a}Uma: quatro vírgula cinco. [p=0.2] {b}Duas: zero vírgula quarenta e cinco. [p=0.2] {c}Três: zero vírgula zero quarenta e cinco, [p=0.2] com um zero para ocupar a casa. [p=0.3] São {d}quarenta e cinco milésimos."),
    dict(id="s09", block="andar", text="A regra, só para dez, cem e mil: [p=0.2] {a}multiplicar anda para a direita, e o número cresce. [p=0.2] {b}Dividir anda para a esquerda, e o número diminui. [p=0.2] {c}Quantos zeros, tantas casas."),
    # multiplicar
    dict(id="s10", block="multiplicar", text="Voltando à fita. [p=0.2] {a}Um vírgula dois vezes zero vírgula três. [p=0.3] {b}Passo um: ignore as vírgulas. [p=0.2] {c}Doze vezes três, trinta e seis."),
    dict(id="s11", block="multiplicar", text="{a}Passo dois: conte as casas depois da vírgula. [p=0.2] {b}Uma no um vírgula dois, [p=0.2] {c}uma no zero vírgula três. [p=0.2] Ao todo, {d}duas casas."),
    dict(id="s12", block="multiplicar", text="{a}Passo três: o resultado fica com essas casas. [p=0.2] Trinta e seis, com duas casas: {b}zero vírgula trinta e seis. [p=0.3] {c}Trinta e seis centavos."),
    dict(id="s13", block="multiplicar", text="Por que funciona? [p=0.2] Sem a vírgula, {a}o um vírgula dois ficou dez vezes maior. [p=0.2] {b}O zero vírgula três também. [p=0.3] Então o resultado ficou {c}dez vezes dez, cem vezes maior, [p=0.2] e você {d}desfaz isso andando duas casas para a esquerda."),
    dict(id="s14", block="multiplicar", text="Confira na fita: [p=0.2] {a}um metro, trinta centavos. [p=0.2] {b}Vinte centímetros, a quinta parte do metro, seis centavos. [p=0.3] Total: {c}trinta e seis centavos."),
    # sinal
    dict(id="s15", block="sinal", text="E com sinal? [p=0.2] Primeiro {a}decida o sinal, depois faça a conta sem ele. [p=0.3] Se você leva a fita fiado, cada metro é uma dívida: {b}menos zero vírgula três. [p=0.2] {c}Menos zero vírgula três vezes um vírgula dois. [p=0.2] Sinais diferentes, negativo. [p=0.2] A conta sem sinal já deu zero vírgula trinta e seis: {d}menos zero vírgula trinta e seis."),
    dict(id="s16", block="sinal", text="Se a loja cancela essa dívida, você tira um vírgula dois metros do fiado: [p=0.2] {a}menos zero vírgula três vezes menos um vírgula dois. [p=0.2] Menos vezes menos dá mais: [p=0.2] {b}mais zero vírgula trinta e seis. [p=0.3] Tirar uma dívida é como ganhar esse dinheiro."),
    # erro
    dict(id="s17", block="erro", text="O erro comum é o do começo: {a}contar as casas de um número só. [p=0.3] A pessoa vê uma casa e escreve {b}três vírgula seis. [p=0.3] Mas multiplicar por {c}zero vírgula três é pegar só um pedaço, [p=0.2] então o resultado tem que ficar {d}menor que um vírgula dois."),
    # atalho
    dict(id="s18", block="atalho", text="Agora o atalho: {a}vezes cinco. [p=0.3] {b}Multiplique por dez, andando a vírgula, [p=0.2] e {c}tire a metade. [p=0.3] {d}Dois vírgula quatro vezes cinco: [p=0.2] {e}vinte e quatro, [p=0.2] metade, {f}doze."),
    dict(id="s19", block="atalho", text="Funciona porque {a}cinco é a metade de dez. [p=0.3] {b}Não compensa quando a metade não sai de cabeça: [p=0.2] aí, arme a conta."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Você levou fiado {a}um metro e cinquenta de tecido, [p=0.2] e {b}cada metro é uma dívida de três reais e vinte centavos. [p=0.3] Seu saldo estava em zero. [p=0.2] {c}Qual é o saldo agora?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] A conta é {a}menos três vírgula dois vezes um vírgula cinco. [p=0.3] Sem vírgulas: {b}trinta e dois vezes quinze, [p=0.2] {c}quatrocentos e oitenta."),
    dict(id="s23", block="resposta", text="Uma casa mais uma casa: {a}duas casas. [p=0.2] Fica {b}quatro vírgula oitenta. [p=0.3] Sinais diferentes, negativo: {c}saldo de menos quatro vírgula oito reais."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}quantos zeros, tantas casas. [p=0.2] {b}Na multiplicação, some as casas. [p=0.2] E {c}o sinal se decide primeiro."),
    dict(id="s25", block="fim", text="Na próxima aula, você vai {a}dividir quando sobra resto: [p=0.2] a conta {b}continua depois da vírgula. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
