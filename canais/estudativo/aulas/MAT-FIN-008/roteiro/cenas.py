# Estudativo · MAT-FIN-008 — Taxa equivalente e taxa efetiva (Matemática · Matemática Financeira).
# Habilidade: mostrar que 1% ao mês não é 12%, e sim 12,68% ao ano, e transformar 12% ao ano com capitalização mensal em taxa efetiva.
# Pré-requisitos: MAT-FIN-004 (juros compostos), MAT-POT-008 (expoente fracionário). Próxima: MAT-FIN-009.
# Questão inédita, criada para esta aula. Sem calculadora: 1,01¹² e 1,02¹² vêm de tabela dada no enunciado.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Taxa equivalente e taxa efetiva"

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
    dict(id="s01", block="gancho", text="{a}Um financiamento cobra um por cento de juros ao mês. [p=0.3] Em um ano, {b}doze por cento? [p=0.3] Não. [p=0.2] {c}Doze vírgula sessenta e oito por cento."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai trocar uma taxa ao mês por uma taxa ao ano sem cair nessa, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Juros compostos: a cada mês, o valor é multiplicado pelo fator, um mais a taxa. [p=0.2] E {b}expoente fracionário: elevar a um meio é tirar a raiz quadrada. [p=0.3] Se faltar alguma, procure no canal."),
    # exemplo de cabeça
    dict(id="s04", block="dois_meses", text="Comece com uma taxa que dá conta de cabeça: [p=0.2] {a}dez por cento ao mês, durante dois meses. [p=0.3] Cem reais viram {b}cento e dez no primeiro mês. [p=0.2] No segundo, os dez por cento valem sobre cento e dez: {c}cento e vinte e um."),
    dict(id="s05", block="dois_meses", text="Em dois meses, o dinheiro cresceu {a}vinte e um por cento, e não vinte. [p=0.3] O real a mais vem dos {b}juros sobre os juros: [p=0.2] dez por cento dos dez reais do primeiro mês."),
    # taxa equivalente
    dict(id="s06", block="equivalente", text="Por isso, {a}dez por cento ao mês equivale a vinte e um por cento a cada dois meses. [p=0.3] {b}Taxas equivalentes levam o mesmo capital ao mesmo montante, no mesmo tempo. [p=0.2] Montante é o valor final, já com os juros."),
    dict(id="s07", block="equivalente", text="Na conta, é só potência. [p=0.2] {a}O fator do período longo é o fator do período curto, elevado ao número de vezes que ele cabe. [p=0.3] {b}Um vírgula um ao quadrado, um vírgula vinte e um."),
    # o caso do gancho
    dict(id="s08", block="um_ano", text="Agora o caso do gancho: um por cento ao mês, durante um ano. [p=0.2] O fator mensal é {a}um vírgula zero um. [p=0.2] Um ano tem doze meses: {b}um vírgula zero um elevado a doze. [p=0.3] Essa conta ninguém faz de cabeça. [p=0.2] A prova dá {c}uma tabela de potências no enunciado."),
    dict(id="s09", block="um_ano", text="A tabela dá {a}cerca de um vírgula um dois seis oito. [p=0.2] Vezes cem, a vírgula anda duas casas: [p=0.2] cento e doze reais e sessenta e oito centavos. [p=0.3] Doze reais e sessenta e oito centavos em cada cem: [p=0.2] {b}doze vírgula sessenta e oito por cento ao ano. [p=0.2] O que passou de doze são, de novo, {c}juros sobre juros."),
    # caminho de volta
    dict(id="s10", block="volta", text="E o caminho de volta? [p=0.2] Uma aplicação rende {a}vinte e um por cento a cada dois meses. [p=0.2] Quanto é ao mês? [p=0.3] O fator mensal é {b}um vírgula vinte e um elevado a um meio, [p=0.2] ou seja, {c}a raiz quadrada de um vírgula vinte e um. [p=0.2] Dá {d}um vírgula um: dez por cento ao mês."),
    # nominal e efetiva
    dict(id="s11", block="nominal", text="Agora, a frase que aparece em contrato: [p=0.2] {a}doze por cento ao ano, com capitalização mensal. [p=0.3] Capitalização mensal quer dizer que {b}os juros entram na conta todo mês."),
    dict(id="s12", block="nominal", text="Esses doze por cento são só um rótulo: a {a}taxa nominal. [p=0.2] O banco divide por doze e cobra {b}um por cento ao mês, com juros compostos. [p=0.3] E isso você já viu: dá {c}doze vírgula sessenta e oito por cento ao ano. [p=0.2] Essa é a {d}taxa efetiva, a que você paga de verdade."),
    dict(id="s13", block="nominal", text="A receita tem dois passos. [p=0.2] {a}Passo um: divida a taxa nominal pelo número de períodos. [p=0.2] {b}Passo dois: eleve o fator a esse número de períodos. [p=0.2] Tire o um da frente, e o que sobra é a taxa efetiva."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é {a}multiplicar a taxa pelo tempo: [p=0.2] um por cento vezes doze dá doze por cento. [p=0.3] Essa é a conta dos {b}juros simples, em que os juros não rendem juros. [p=0.2] Nos juros compostos, {c}a taxa efetiva sai sempre maior."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho de prova, para dois períodos. [p=0.2] {a}Some a taxa com ela mesma, [p=0.2] e some também a taxa vezes a taxa, dividido por cem. [p=0.3] Dez mais dez dá vinte. [p=0.2] {b}Dez vezes dez dá cem, dividido por cem dá um. [p=0.2] {c}Vinte e um por cento."),
    dict(id="s16", block="atalho", text="Funciona porque são {a}dois aumentos seguidos, e o segundo vale também sobre o primeiro. [p=0.3] Não compensa com muitos períodos, como doze meses: [p=0.2] aí, {b}use a tabela do enunciado. [p=0.3] Mas guarde a pista: indo para um período mais longo, {c}alternativa igual ou menor que a taxa vezes o tempo está errada."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um banco anuncia {a}vinte e quatro por cento ao ano, com capitalização mensal. [p=0.2] O enunciado dá: {b}um vírgula zero dois elevado a doze é cerca de um vírgula vinte e sete. [p=0.3] {c}Qual é a taxa efetiva ao ano?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Passo um: {a}vinte e quatro dividido por doze dá dois por cento ao mês. [p=0.2] Fator mensal: {b}um vírgula zero dois. [p=0.3] Passo dois: em doze meses, {c}um vírgula zero dois elevado a doze, que a tabela dá como um vírgula vinte e sete. [p=0.2] Tire o inteiro: {d}cerca de vinte e sete por cento ao ano."),
    dict(id="s20", block="resposta", text="Bate com a pista: {a}vinte e sete é maior que vinte e quatro. [p=0.2] Quem respondeu vinte e quatro {b}leu só o rótulo."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}nos juros compostos, a taxa não se multiplica pelo tempo. [p=0.2] {b}Eleve o fator."),
    dict(id="s22", block="fim", text="Na próxima aula, a mesma ideia mede a {a}inflação: [p=0.2] cinco por cento num ano e quatro no outro {b}não dão nove, [p=0.2] e você descobre quanto o seu dinheiro {c}perde de poder de compra. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
