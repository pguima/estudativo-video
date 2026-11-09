# Estudativo · FIS-ELE-024 — Leis de Kirchhoff: nós e malhas (Física · Eletricidade · Leis de Kirchhoff · extensão).
# Habilidade: aplicar a soma das correntes num nó e a soma das tensões numa malha, com a regra de sinais.
# Pré-requisitos: FIS-ELE-022 (receptor, fem contra subtrai), e por ela 012 (nó, ramo), 009, 004 (potencial). Próxima: FIS-ELE-025.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Sistema de equações (MAT-EQU-018) NÃO está em "Já ensinado": a aula resolve só malha única (uma incógnita); duas malhas = próxima.
# Regra de sinais: andando a malha, gerador do − para o + soma ε (e do + para o − subtrai); resistor a favor da corrente subtrai R·i.
# Contas: nó 5 + 2 = 4 + i → i = 3 A. Malha: 20 − 2i − 8 − 4i = 0 → 12 = 6i → i = 2 A; chute ao contrário → −2 A.
#   Erro: +8 → 28/6 ≈ 4,67 A. Atalho (20 − 8)/(2 + 4) = 2.  Questão: (18 − 6)/(1 + 2 + 3) = 12/6 = 2 A.

TITULO = "Leis de Kirchhoff: nós e malhas"

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
    dict(id="s01", block="gancho", text="{a}Uma bateria virada contra a outra, na mesma volta do circuito: [p=0.2] {b}ela soma ou subtrai? [p=0.3] {c}E, num cruzamento de fios, quanto de corrente vai para cada lado? [p=0.3] {d}Duas regras respondem: [p=0.1] {e}as leis de Kirchhoff."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar a lei dos nós [p=0.1] e {b}a lei das malhas, [p=0.1] {c}com a regra de sinais que evita quase todo erro."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}nó é onde a corrente se divide ou se junta, e ramo é o caminho entre dois nós; [p=0.2] {c}a tensão num resistor é erre vezes i; [p=0.2] e {d}o que gerador e receptor fazem com a tensão. [p=0.3] Se faltar alguma, procure no canal."),
    # lei dos nós
    dict(id="s04", block="nos", text="{a}Primeira lei: a lei dos nós. [p=0.2] {b}A soma das correntes que chegam num nó [p=0.1] é igual à soma das que saem. [p=0.3] {c}Carga não some nem se acumula no fio: [p=0.1] {d}é como água num cano que se divide."),
    dict(id="s05", block="nos", text="Exemplo: {a}chegam cinco ampères e dois ampères. [p=0.2] {b}Saem quatro ampères e uma corrente desconhecida. [p=0.3] {c}Cinco mais dois, sete, igual a quatro mais i: [p=0.1] {d}i vale três ampères."),
    # lei das malhas
    dict(id="s06", block="malhas", text="{a}Segunda lei: a lei das malhas. [p=0.2] {b}Malha é qualquer caminho fechado do circuito. [p=0.3] {c}Dando uma volta inteira, [p=0.1] a soma das tensões que sobem e descem é zero."),
    dict(id="s07", block="malhas", text="Por quê? [p=0.2] {a}Cada ponto do circuito tem um potencial. [p=0.2] {b}Voltando ao ponto de partida, você volta ao mesmo potencial. [p=0.3] {c}É como andar num morro: [p=0.1] {d}quando você volta ao começo, tudo o que subiu, desceu."),
    # sinais
    dict(id="s08", block="sinais", text="Agora, a regra de sinais. [p=0.2] {a}Escolha um sentido para a corrente [p=0.1] e ande a malha nesse sentido. [p=0.3] {b}No gerador, se você entra pelo negativo e sai pelo positivo, [p=0.1] {c}some épsilon, porque o potencial sobe. [p=0.2] {d}Se entra pelo positivo, subtraia."),
    dict(id="s09", block="sinais", text="{a}No resistor, andando a favor da corrente, [p=0.1] {b}subtraia erre vezes i, porque o potencial cai. [p=0.2] {c}Andando contra a corrente, some."),
    # exemplo
    dict(id="s10", block="exemplo", text="Veja esta malha. [p=0.2] {a}Um gerador de vinte volts, [p=0.1] {b}um resistor de dois ohms, [p=0.1] {c}uma bateria de oito volts virada contra o gerador [p=0.1] e {d}um resistor de quatro ohms."),
    dict(id="s11", block="exemplo", text="Ande no sentido da corrente, saindo do negativo do gerador de vinte. [p=0.2] {a}Mais vinte. [p=0.1] {b}Menos dois i. [p=0.1] {c}Na bateria de oito, você entra pelo positivo: menos oito. [p=0.1] {d}Menos quatro i. [p=0.2] {e}Tudo igual a zero."),
    dict(id="s12", block="exemplo", text="{a}Vinte menos oito, doze, igual a seis i: [p=0.1] {b}i vale dois ampères. [p=0.3] {c}E a bateria de oito volts, com a corrente entrando pelo positivo, [p=0.1] {d}funciona como receptor: ela está sendo carregada."),
    dict(id="s13", block="exemplo", text="{a}E se você chutasse a corrente ao contrário? [p=0.2] {b}A conta daria menos dois ampères. [p=0.3] {c}O sinal de menos só avisa que o sentido real é o oposto. [p=0.2] {d}O valor, dois ampères, continua certo."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}dar o sinal do gerador pelo sentido da corrente. [p=0.3] {b}O sinal depende só do polo por onde você entra. [p=0.2] {c}Quem escreve mais oito na bateria virada [p=0.1] acha vinte e oito dividido por seis, [p=0.1] {d}quase quatro vírgula sete ampères, [p=0.1] e erra."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho para uma malha só: [p=0.2] {a}a corrente é a soma das forças eletromotrizes a favor, menos as contra, [p=0.1] {b}dividida pela soma de todas as resistências. [p=0.3] {c}Vinte menos oito, dividido por dois mais quatro: dois ampères. [p=0.3] Funciona porque {d}é a lei das malhas já arrumada, a mesma conta da aula de receptores. [p=0.2] {e}Não serve com mais de uma malha: [p=0.1] aí, é sistema de equações, na próxima aula."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Numa malha, dois geradores estão virados um contra o outro: [p=0.1] {b}dezoito volts e seis volts. [p=0.2] {c}Há três resistores: um, dois e três ohms. [p=0.3] {d}Qual é a corrente, [p=0.1] e {e}em qual gerador ela entra pelo positivo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O de dezoito vence: [p=0.1] a corrente sai pelo positivo dele. [p=0.3] {b}Lei das malhas: dezoito menos seis, menos um i, menos dois i, menos três i, igual a zero. [p=0.2] {c}Doze igual a seis i: [p=0.1] {d}dois ampères."),
    dict(id="s19", block="resposta", text="{a}A corrente entra pelo positivo do gerador de seis volts: [p=0.1] {b}ele funciona como receptor."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}no nó, o que chega é igual ao que sai; [p=0.2] {b}na malha, as tensões da volta somam zero; [p=0.2] e {c}o sinal do gerador depende do polo por onde você entra."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai juntar as duas leis [p=0.1] {a}num circuito com duas malhas e dois geradores, [p=0.2] {b}montando um sistema de equações. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
