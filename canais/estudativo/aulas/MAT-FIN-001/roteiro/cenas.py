# Estudativo · MAT-FIN-001 — Juros simples (Matemática · Matemática Financeira).
# Habilidade: apontar capital, taxa, tempo e montante e achar os juros de R$ 1.200 a 2% ao mês por 6 meses, com taxa e tempo na mesma unidade.
# Pré-requisitos: MAT-POR-002 (porcentagem de um valor). Próxima: MAT-FIN-002.
# Questão inédita, criada para esta aula. Sem fatores (MAT-POR-004 fora da ficha): montante = capital + juros, por soma.
# Sem equações: a fórmula é lida como uma receita de multiplicação, com cada letra explicada.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Juros simples"

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
    dict(id="s01", block="gancho", text="Você pegou {a}mil reais emprestados, a {b}trinta e seis por cento ao ano, [p=0.2] e pagou tudo em {c}cinco meses. [p=0.3] Se a sua conta de juros deu {d}mil e oitocentos reais, [p=0.2] você pagaria quase o dobro do empréstimo só de juros. [p=0.3] A resposta certa é {e}cento e cinquenta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular juros simples sem cair nessa, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa só: [p=0.2] {b}calcular a porcentagem de um valor, [p=0.2] de cabeça ou multiplicando pelo decimal. [p=0.3] Se faltar, procure no canal."),
    # os quatro personagens
    dict(id="s04", block="nomes", text="Quem empresta dinheiro {a}cobra pelo tempo que ele fica com você. [p=0.2] Esse aluguel do dinheiro se chama {b}juros. [p=0.3] E toda conta de juros tem {c}quatro personagens."),
    dict(id="s05", block="nomes", text="{a}Capital é o valor emprestado ou aplicado: [p=0.1] mil e duzentos reais. [p=0.2] {b}Taxa é a porcentagem cobrada em cada período: [p=0.1] dois por cento ao mês. [p=0.2] {c}Tempo é quantos períodos se passam: [p=0.1] seis meses."),
    dict(id="s06", block="nomes", text="E {a}montante é o total no fim: [p=0.2] {b}o capital mais os juros. [p=0.3] É o valor que você devolve, [p=0.1] ou que você resgata, se for uma aplicação."),
    # mês a mês
    dict(id="s07", block="mes", text="Nos {a}juros simples, os juros de cada mês são calculados sempre {b}sobre o capital do começo. [p=0.3] {c}Dois por cento de mil e duzentos: [p=0.1] um por cento é doze, então dois por cento são {d}vinte e quatro reais."),
    dict(id="s08", block="mes", text="Todo mês, os mesmos vinte e quatro. [p=0.2] Em seis meses, {a}vinte e quatro vezes seis: {b}cento e quarenta e quatro reais de juros. [p=0.3] Montante: {c}mil e duzentos mais cento e quarenta e quatro. [p=0.2] {d}Mil trezentos e quarenta e quatro reais."),
    # fórmula
    dict(id="s09", block="formula", text="Isso vira uma fórmula curta: {a}jota igual a cê vezes i vezes tê. [p=0.3] Cada letra guarda um personagem. [p=0.2] {b}Jota, os juros. [p=0.1] {c}Cê, o capital. [p=0.1] {d}A letra i, a taxa. [p=0.1] {e}Tê, o tempo. [p=0.3] Capital vezes taxa dá o juro de um período: [p=0.1] um mês, se a taxa for ao mês. [p=0.2] Vezes o tempo, o juro total."),
    dict(id="s10", block="formula", text="A taxa entra {a}como decimal: dois por cento são zero vírgula zero dois. [p=0.3] {b}Mil e duzentos vezes zero vírgula zero dois dá vinte e quatro. [p=0.2] {c}Vezes seis dá cento e quarenta e quatro. [p=0.2] A mesma conta de antes."),
    # mesma unidade
    dict(id="s11", block="unidade", text="Agora, a regra que mais derruba gente: [p=0.2] {a}taxa e tempo precisam estar na mesma unidade. [p=0.3] {b}Taxa ao mês pede tempo em meses. [p=0.2] {c}Taxa ao ano pede tempo em anos."),
    dict(id="s12", block="unidade", text="Volte ao gancho: {a}trinta e seis por cento ao ano, por cinco meses. [p=0.3] Nos juros simples, a taxa do ano se divide igualmente pelos meses. [p=0.2] Um ano tem doze meses, então {b}trinta e seis dividido por doze dá três por cento ao mês."),
    dict(id="s13", block="unidade", text="{a}Três por cento vezes cinco meses, quinze por cento. [p=0.2] {b}Quinze por cento de mil dá cento e cinquenta reais. [p=0.3] Quem multiplicou trinta e seis por cinco [p=0.1] misturou {c}taxa ao ano com tempo em meses."),
    # erro
    dict(id="s14", block="erro", text="Outro erro comum: {a}usar a taxa sem passar para decimal. [p=0.2] A pessoa faz {b}mil e duzentos vezes dois vezes seis, [p=0.1] e acha {c}catorze mil e quatrocentos reais de juros. [p=0.3] Doze vezes o valor emprestado, em seis meses. [p=0.2] Dois por cento é {d}zero vírgula zero dois, e não dois."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}junte taxa e tempo numa porcentagem só. [p=0.3] {b}Dois por cento ao mês, por seis meses: doze por cento. [p=0.2] {c}Doze por cento de mil e duzentos: [p=0.1] dez por cento é cento e vinte, e dois por cento são vinte e quatro. [p=0.2] {d}Cento e quarenta e quatro, de cabeça."),
    dict(id="s16", block="atalho", text="Funciona porque, nos juros simples, {a}todo mês rende a mesma porcentagem do mesmo capital. [p=0.3] Não compensa quando a porcentagem total fica quebrada, [p=0.1] como {b}um vírgula sete por cento por nove meses. [p=0.2] Aí, {c}vá de decimal, na fórmula."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma loja financia {a}dois mil reais a juros simples [p=0.1] de {b}dezoito por cento ao ano. [p=0.2] A dívida é paga em {c}quatro meses. [p=0.3] {d}Quanto são os juros, e qual é o montante?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Taxa ao ano e tempo em meses: {a}converta. [p=0.2] {b}Dezoito dividido por doze dá um vírgula cinco por cento ao mês. [p=0.2] {c}Vezes quatro meses, seis por cento."),
    dict(id="s20", block="resposta", text="{a}Seis por cento de dois mil: [p=0.1] um por cento é vinte, então seis por cento são {b}cento e vinte reais de juros. [p=0.3] Montante: {c}dois mil cento e vinte reais."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}taxa e tempo na mesma unidade, [p=0.2] {b}juros iguais todo mês, sobre o capital, [p=0.2] e {c}montante é capital mais juros."),
    dict(id="s22", block="fim", text="Na próxima aula, a pergunta muda de lado: [p=0.2] você descobre {a}em quantos meses um dinheiro dobra, a cinco por cento ao mês. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
