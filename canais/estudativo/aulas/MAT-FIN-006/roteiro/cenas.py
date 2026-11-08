# Estudativo · MAT-FIN-006 — Juros compostos: achar o capital ou o tempo (Matemática · Matemática Financeira).
# Habilidade: descobrir quanto aplicar hoje para ter R$ 1.210 em 2 anos a 10% e em quantos meses o capital dobra pela regra do 72, com o aviso de que logaritmo vem depois.
# Pré-requisitos: MAT-FIN-004 (fórmula dos compostos), MAT-FRA-018 (dividir por decimal). Próxima: MAT-FIN-007.
# Questão inédita, criada para esta aula. Sem equações (fora da ficha): voltar é desfazer a multiplicação pelo fator com uma divisão.
# Logaritmo citado só como assunto de outra aula. MAT-FIN-005 fora da ficha: não citada.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Juros compostos: achar o capital ou o tempo"

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
    dict(id="s01", block="gancho", text="Você quer ter {a}mil duzentos e dez reais daqui a {b}dois anos. [p=0.2] A aplicação rende {c}dez por cento ao ano, em juros compostos. [p=0.3] Quanto aplicar hoje? [p=0.3] A resposta é {d}mil reais, [p=0.2] e sai com uma divisão só."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar o capital nos juros compostos [p=0.2] e estimar em quanto tempo um dinheiro dobra, [p=0.2] com um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a fórmula dos compostos, montante igual a capital vezes o fator elevado ao tempo, [p=0.2] e {c}dividir por um número com vírgula. [p=0.3] Se faltar alguma, procure no canal."),
    # capital
    dict(id="s04", block="capital", text="Pense no caminho de ida. [p=0.2] {a}O capital, multiplicado pelo fator um vírgula um a cada ano, vira o montante. [p=0.3] Dois anos: {b}um vírgula um ao quadrado dá um vírgula vinte e um."),
    dict(id="s05", block="capital", text="Para voltar, {a}desfaça a multiplicação com uma divisão. [p=0.3] Capital: {b}o montante dividido pelo fator elevado ao tempo. [p=0.3] {c}Mil duzentos e dez dividido por um vírgula vinte e um."),
    dict(id="s06", block="capital", text="O divisor tem {a}duas casas depois da vírgula. [p=0.2] Ande duas casas no primeiro e no segundo número. [p=0.2] {b}Cento e vinte e um mil dividido por cento e vinte e um. [p=0.2] {c}Mil reais."),
    dict(id="s07", block="capital", text="Conferindo pelo caminho de ida: {a}mil vira mil e cem. [p=0.2] {b}Mil e cem vira mil duzentos e dez. [p=0.2] Bateu. [p=0.3] Esse capital tem um nome: {c}valor presente. [p=0.2] É quanto um dinheiro do futuro vale hoje."),
    # erro
    dict(id="s08", block="erro", text="O erro comum é {a}tirar os juros do montante. [p=0.2] A pessoa calcula {b}vinte e um por cento de mil duzentos e dez [p=0.1] e tira do total. [p=0.2] Fica com {c}novecentos e cinquenta e cinco reais e noventa centavos."),
    dict(id="s09", block="erro", text="Confira na ida: {a}os vinte e um por cento agora valem sobre novecentos e cinquenta e cinco, um valor menor que mil duzentos e dez. [p=0.2] Rendem menos que os duzentos e cinquenta e quatro que foram tirados, [p=0.2] e o total {b}não volta a mil duzentos e dez. [p=0.3] Os vinte e um por cento foram calculados {c}sobre o capital, e não sobre o montante."),
    # tempo
    dict(id="s10", block="tempo", text="Agora o tempo. [p=0.2] {a}A dez por cento ao ano, em quantos anos o dinheiro dobra? [p=0.3] Dobrar é ter {b}fator dois: o montante vale duas vezes o capital. [p=0.2] A pergunta vira: {c}um vírgula um elevado a quanto dá dois?"),
    dict(id="s11", block="tempo", text="A prova costuma dar {a}uma tabela. [p=0.2] {b}Um vírgula um elevado a sete, cerca de um vírgula nove cinco. [p=0.2] {c}Elevado a oito, cerca de dois vírgula um quatro. [p=0.3] {d}O dinheiro dobra entre o sétimo e o oitavo ano."),
    dict(id="s12", block="tempo", text="A conta exata usa {a}logaritmo, assunto de outra aula, mais adiante. [p=0.3] Para estimar sem tabela, existe um atalho."),
    # atalho
    dict(id="s13", block="atalho", text="{a}A regra do setenta e dois. [p=0.3] {b}Divida setenta e dois pela taxa. [p=0.2] O resultado é {c}o tempo aproximado para dobrar, na unidade da taxa. [p=0.3] {d}Setenta e dois dividido por dez dá sete vírgula dois anos. [p=0.2] Entre sete e oito, como na tabela."),
    dict(id="s14", block="atalho", text="Com taxa ao mês, a resposta sai em meses. [p=0.2] {a}Seis por cento ao mês: [p=0.1] {b}setenta e dois dividido por seis dá doze meses. [p=0.3] Na conta exata, {c}um vírgula zero seis elevado a doze dá cerca de dois vírgula zero um. [p=0.2] Quase exato."),
    dict(id="s15", block="atalho", text="Funciona porque {a}setenta e dois foi escolhido para acertar o dobro com pouco erro nas taxas mais comuns, [p=0.1] como você conferiu na tabela. [p=0.2] A conta que explica esse número usa logaritmo. [p=0.2] E setenta e dois se divide por muitos números. [p=0.3] Não compensa com {b}taxas muito altas, como cinquenta por cento: [p=0.1] o erro cresce. [p=0.2] Nem quando a prova pede o valor exato: {c}aí, use a tabela."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Quanto aplicar hoje, a vinte por cento ao ano em juros compostos, [p=0.1] uma taxa alta, só de exemplo, [p=0.1] para ter {b}sete mil e duzentos reais em dois anos? [p=0.3] E, a {c}quatro por cento ao mês, [p=0.1] {d}em quantos meses, mais ou menos, um dinheiro dobra?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Fator: {a}um vírgula dois. [p=0.2] Dois anos: {b}um vírgula dois ao quadrado dá um vírgula quatro quatro. [p=0.3] {c}Sete mil e duzentos dividido por um vírgula quatro quatro. [p=0.2] Ande duas casas: {d}setecentos e vinte mil dividido por cento e quarenta e quatro. [p=0.2] {e}Cinco mil reais."),
    dict(id="s19", block="resposta", text="Conferindo: {a}cinco mil vira seis mil, [p=0.1] que vira sete mil e duzentos. [p=0.2] Bateu. [p=0.3] E o dobro: {b}setenta e dois dividido por quatro, cerca de dezoito meses."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}para achar o capital, divida o montante pelo fator elevado ao tempo. [p=0.2] {b}Para estimar o tempo de dobrar, setenta e dois dividido pela taxa."),
    dict(id="s21", block="fim", text="Na próxima aula, você {a}pratica tudo de juros simples e compostos: [p=0.2] {b}empréstimos, aplicações, contas atrasadas e prazos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
