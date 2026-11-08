# Estudativo · MAT-POR-001 — O que é porcentagem: fração e decimal (Matemática · Porcentagem).
# Habilidade: ler 25% como 25 em cada 100 e escrever 12,5% como 1/8 e como 0,125.
# Pré-requisitos: MAT-FRA-003 (equivalentes e simplificação), MAT-FRA-019 (fração em decimal). Próxima: MAT-POR-002.
# Questão inédita, criada para esta aula. MAT-FRA-016 ainda não foi ensinada: nada de andar com a vírgula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "O que é porcentagem: fração e decimal"

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
    dict(id="s01", block="gancho", text="{a}Doze vírgula cinco por cento. [p=0.3] Parece um número quebrado, difícil de imaginar. [p=0.3] Mas é só {b}uma pizza cortada em oito pedaços, [p=0.2] e você pega {c}um pedaço."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai trocar porcentagem por fração e por decimal, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}simplificar uma fração [p=0.2] e {c}trocar fração por decimal. [p=0.3] Se faltar alguma, procure no canal."),
    # em cada cem
    dict(id="s04", block="grade", text="O que quer dizer {a}vinte e cinco por cento? [p=0.2] A própria expressão conta. [p=0.2] {b}Por cento quer dizer {c}em cada cem. [p=0.3] Vinte e cinco por cento é {d}vinte e cinco em cada cem."),
    dict(id="s05", block="grade", text="Imagine {a}uma grade com cem quadradinhos. [p=0.2] Pinte {b}vinte e cinco deles. [p=0.3] Você pintou vinte e cinco por cento da grade."),
    # fração e decimal
    dict(id="s06", block="fracao", text="Virar fração é direto: {a}o número vai em cima, e o cem vai embaixo. [p=0.2] {b}Vinte e cinco centésimos. [p=0.3] Vinte e cinco e cem são divisíveis por vinte e cinco. [p=0.2] {c}Dividindo em cima e embaixo, fica um quarto. [p=0.3] Na grade dá para ver: {d}quatro blocos iguais, e você pintou um."),
    dict(id="s07", block="fracao", text="E o decimal? [p=0.2] Centésimos se escrevem com {a}duas casas depois da vírgula. [p=0.2] Vinte e cinco centésimos é {b}zero vírgula vinte e cinco. [p=0.3] Então vinte e cinco por cento, um quarto e zero vírgula vinte e cinco são {c}o mesmo número, escrito de três jeitos."),
    dict(id="s08", block="fracao", text="A regra: {a}o símbolo de por cento é uma fração com cem embaixo. [p=0.2] {b}Sete por cento é sete centésimos, [p=0.1] que dá zero vírgula zero sete. [p=0.2] {c}Sessenta por cento é sessenta centésimos, [p=0.1] que simplifica para três quintos."),
    # doze e meio
    dict(id="s09", block="meio", text="Voltando ao gancho. [p=0.2] Doze vírgula cinco por cento são {a}doze e meio em cada cem. [p=0.3] Fração com meio em cima é estranha, então {b}dobre em cima e embaixo: [p=0.2] {c}vinte e cinco em cada duzentos. [p=0.3] Como nas frações equivalentes, dobrar em cima e embaixo não muda o valor."),
    dict(id="s10", block="meio", text="Agora simplifique. [p=0.2] Vinte e cinco e duzentos são divisíveis por vinte e cinco. [p=0.2] {a}Vinte e cinco dividido por vinte e cinco dá um. [p=0.2] {b}Duzentos dividido por vinte e cinco dá oito. [p=0.3] {c}Um oitavo. [p=0.2] A fatia de pizza do começo."),
    dict(id="s11", block="meio", text="Para o decimal, {a}divida um por oito. [p=0.2] Um é menor que oito: escreva zero e vírgula. [p=0.2] {b}Dez dividido por oito dá um, e sobram dois. [p=0.2] {c}Vinte dividido por oito dá dois, e sobram quatro. [p=0.2] {d}Quarenta dividido por oito dá cinco, e não sobra nada. [p=0.3] {e}Zero vírgula cento e vinte e cinco."),
    # erro
    dict(id="s12", block="erro", text="Agora, cuidado com um erro muito comum: escrever {a}cinco por cento como {b}zero vírgula cinco. [p=0.3] Só que zero vírgula cinco é cinco décimos, [p=0.2] o mesmo que cinquenta centésimos: [p=0.2] {c}cinquenta por cento, a metade."),
    dict(id="s13", block="erro", text="Cinco por cento são cinco {a}centésimos. [p=0.2] Centésimo pede duas casas, [p=0.2] então fica {b}zero vírgula zero cinco. [p=0.3] Dez vezes menor do que a pessoa escreveu."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}o caminho das metades. [p=0.3] {b}Cem por cento é o inteiro. [p=0.2] {c}Metade disso, cinquenta por cento, vale um meio. [p=0.2] {d}Metade de novo, vinte e cinco por cento, vale um quarto. [p=0.2] {e}Mais uma metade, doze vírgula cinco por cento, vale um oitavo."),
    dict(id="s15", block="atalho", text="Funciona porque {a}cada metade dobra o número de baixo da fração. [p=0.3] Guarde também que {b}dez por cento vale um décimo, [p=0.2] e {c}vinte por cento vale um quinto. [p=0.3] Não compensa em porcentagens como {d}trinta e sete por cento: [p=0.2] aí, use direto {e}trinta e sete centésimos."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] A bateria do celular está em {a}trinta e sete vírgula cinco por cento. [p=0.3] {b}Que fração da carga é essa, na forma mais simples? [p=0.2] {c}E qual é o decimal?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] São trinta e sete e meio em cada cem. [p=0.2] {a}Dobre em cima e embaixo: setenta e cinco em cada duzentos. [p=0.3] {b}Divida em cima e embaixo por vinte e cinco. [p=0.2] Fica {c}três oitavos."),
    dict(id="s19", block="resposta", text="Pelo atalho, sai mais rápido. [p=0.2] Trinta e sete e meio é {a}três vezes doze e meio. [p=0.2] Então são {b}três fatias de um oitavo. [p=0.2] Três oitavos. [p=0.3] E três oitavos você já transformou em decimal: {c}zero vírgula trezentos e setenta e cinco."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}por cento é em cada cem. [p=0.2] {b}Ponha o cem embaixo e simplifique. [p=0.2] Para o decimal, {c}divida o de cima pelo de baixo."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai {a}calcular a porcentagem de um valor: [p=0.2] {b}quinze por cento de oitenta, de cabeça, [p=0.2] e {c}contas maiores, com o decimal. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
