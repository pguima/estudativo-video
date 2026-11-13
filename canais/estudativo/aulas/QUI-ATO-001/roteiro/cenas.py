# Estudativo · QUI-ATO-001 — Modelos de Dalton e Thomson (Química · Átomo e Tabela Periódica · Modelos atômicos e distribuição eletrônica).
# Habilidade: dizer o que mudou da esfera maciça de Dalton para o modelo com elétrons de Thomson e qual fato obrigou a trocar de modelo.
# Pré-requisitos: QUI-MIS-001. Próxima: QUI-ATO-002 (Rutherford: a lâmina de ouro e o núcleo).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: Dalton (inglês), modelo de 1803 a 1808 ("por volta de mil e oitocentos"); J. J. Thomson (inglês), elétron em 1897,
# com raios catódicos que se desviam para a placa positiva e aparecem com qualquer metal no eletrodo; modelo "pudim de passas".
# Núcleo e Rutherford ficam para a QUI-ATO-002; reação química (conservação da massa) só citada, é assunto de outra aula.

TITULO = "Modelos de Dalton e Thomson"

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
    dict(id="s01", block="gancho", text="{a}Passe um pente de plástico no cabelo seco [p=0.1] e chegue perto de {b}papel picado. [p=0.3] {c}O papel pula e gruda no pente. [p=0.3] {d}O primeiro modelo de átomo não conseguia explicar isso."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai conhecer {a}o átomo de Dalton, [p=0.2] {b}o de Thomson [p=0.2] e {c}o fato que obrigou a trocar um pelo outro."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula de átomos e moléculas: [p=0.1] {a}tudo é feito de átomos, [p=0.2] e {b}cada tipo de átomo é um elemento químico. [p=0.3] Só que ninguém enxerga um átomo. [p=0.2] Por isso, a ciência {c}cria modelos."),
    # modelo
    dict(id="s04", block="modelo", text="{a}Modelo é uma imagem simplificada que explica o que se observa. [p=0.3] É como {b}um mapa: [p=0.1] não é a cidade, mas ajuda a andar nela. [p=0.3] {c}Quando aparece um fato que o modelo não explica, [p=0.2] ele {d}é trocado por um melhor."),
    # Dalton
    dict(id="s05", block="dalton", text="Por volta de mil e oitocentos, o inglês {a}John Dalton imaginou o átomo como {b}uma esfera maciça, [p=0.2] parecida com {c}uma bola de bilhar: [p=0.2] {d}inteira por dentro, [p=0.1] sem partes menores [p=0.1] e {e}impossível de dividir."),
    dict(id="s06", block="dalton", text="Para Dalton, {a}átomos do mesmo elemento são iguais entre si, [p=0.2] e {b}átomos de elementos diferentes são diferentes. [p=0.3] Quando uma substância se transforma em outra, [p=0.1] {c}os átomos só trocam de lugar: [p=0.2] {d}nenhum some e nenhum aparece. [p=0.3] Essas transformações são {e}assunto de outra aula."),
    # o fato novo: a eletricidade
    dict(id="s07", block="eletrico", text="Mas havia algo que a bola de bilhar não explicava: [p=0.2] {a}a eletricidade. [p=0.3] Existem dois tipos de carga elétrica, [p=0.1] {b}a positiva [p=0.1] e {c}a negativa. [p=0.3] {d}Cargas opostas se atraem. [p=0.2] {e}Cargas iguais se repelem, ou seja, se empurram."),
    dict(id="s08", block="eletrico", text="Atritar o pente no cabelo {a}faz carga passar de um para o outro, [p=0.2] e o pente fica carregado. [p=0.3] Mas {b}uma esfera maciça e sem partes não tem nada para passar. [p=0.3] {c}A resposta só veio com uma descoberta: [p=0.1] o elétron."),
    # Thomson
    dict(id="s09", block="thomson", text="Em mil oitocentos e noventa e sete, o inglês {a}Joseph John Thomson trabalhou com {b}um tubo de vidro quase sem ar. [p=0.2] Ligado à eletricidade, [p=0.1] o tubo solta {c}um feixe, chamado raio catódico, [p=0.1] porque sai do cátodo, a placa de metal ligada ao polo negativo."),
    dict(id="s10", block="thomson", text="Entre {a}uma placa positiva e outra negativa, [p=0.2] {b}o feixe se curva para o lado positivo. [p=0.3] Se é atraído pelo positivo, [p=0.1] {c}o feixe é feito de partículas negativas. [p=0.3] E elas apareciam {d}com qualquer metal dentro do tubo: [p=0.2] estavam em todos os átomos. [p=0.3] Thomson tinha descoberto {e}o elétron."),
    dict(id="s11", block="thomson", text="{a}Se o elétron é um pedaço do átomo, [p=0.2] {b}o átomo pode ser dividido. [p=0.3] Era exatamente {c}o que Dalton dizia ser impossível."),
    dict(id="s12", block="pudim", text="O modelo de Thomson: [p=0.1] {a}uma esfera de carga positiva, [p=0.2] com {b}elétrons negativos espalhados nela, [p=0.2] como {c}as passas de um pudim, ou de um panetone. [p=0.3] {d}O positivo e o negativo se equilibram, [p=0.2] e o átomo inteiro fica {e}neutro, sem carga."),
    dict(id="s13", block="pudim", text="E o pente? [p=0.2] {a}No atrito, elétrons passam de um material para o outro. [p=0.2] {b}Quem ganha elétrons fica negativo. [p=0.1] {c}Quem perde fica positivo. [p=0.3] E o pente carregado {d}atrai o papel."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com um erro comum: [p=0.2] {a}achar que Thomson descobriu o núcleo do átomo. [p=0.3] {b}No pudim de passas não existe núcleo: [p=0.2] {c}o positivo está espalhado pela esfera toda. [p=0.3] Thomson descobriu {d}o elétron. [p=0.2] O núcleo veio depois, {e}e é assunto da próxima aula."),
    # atalho
    dict(id="s15", block="atalho", text="O atalho de prova: [p=0.2] procure {a}a palavra-chave do enunciado. [p=0.3] {b}Indivisível, sem partes, bola de bilhar: [p=0.2] {c}é Dalton. [p=0.3] {d}Elétrons espalhados numa esfera positiva, pudim de passas: [p=0.2] {e}é Thomson."),
    dict(id="s16", block="atalho", text="Funciona porque {a}cada modelo nasceu de uma ideia central, [p=0.2] e a prova descreve essa ideia. [p=0.3] {b}Não compensa quando a questão pede o motivo da troca: [p=0.2] aí, lembre {c}do fato. [p=0.2] O elétron mostrou que o átomo se divide."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um texto descreve o átomo assim: [p=0.2] {a}uma esfera de carga positiva, com partículas negativas presas nela. [p=0.3] {b}Que modelo é esse? [p=0.2] E {c}que descoberta derrubou o modelo anterior?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Esfera positiva com partículas negativas: [p=0.2] {b}é o pudim de passas, o modelo de Thomson. [p=0.3] O anterior era {c}o de Dalton, a esfera maciça. [p=0.2] Ele caiu com {d}a descoberta do elétron, [p=0.2] {e}que mostrou que o átomo tem partes e pode ser dividido."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}Dalton, esfera maciça e indivisível. [p=0.2] {b}Thomson, esfera positiva com elétrons, [p=0.2] {c}porque o elétron mostrou que o átomo se divide."),
    dict(id="s21", block="fim", text="Na próxima aula, {a}uma folha finíssima de ouro [p=0.1] {b}derruba o pudim de passas [p=0.2] e revela {c}o núcleo do átomo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
