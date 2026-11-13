# Estudativo · QUI-ORG-016 — Isomeria óptica: carbono quiral (Química · Química Orgânica · Propriedades físicas e isomeria).
# Habilidade: achar o carbono quiral, contar os isômeros ópticos com 2 elevado a n e explicar o caso da talidomida.
# Pré-requisitos: QUI-ORG-014, MAT-POT-001. Próxima: QUI-ORG-017 (praticando propriedades e isomeria, com remédios e alimentos).
# Marcas: {cue} animação · [p=0.2] pausa. Números e fórmulas por extenso; "2 elevado a n" = "dois elevado a ene".
# Fatos: talidomida, vendida a partir de 1957 contra enjoo na gravidez, retirada em 1961; cerca de 10 mil bebês com malformações.
# Uma das formas (enantiômeros) ligada às malformações; o corpo converte uma na outra, então separar não resolveria.
# Quiral vem do grego kheir, mão. Ácido lático: CH3–CH(OH)–COOH, um carbono quiral. Glicose de cadeia aberta: 4 quirais, 16 isômeros.
# 2^n falha em molécula simétrica (forma meso, como o ácido tartárico): fica para outra aula. Questão inédita: pentano-2,3-diol, 2 quirais, 4.

TITULO = "Isomeria óptica: carbono quiral"

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
    dict(id="s01", block="gancho", text="{a}Em mil novecentos e cinquenta e sete, chegou às farmácias um calmante, muito usado contra o enjoo na gravidez: [p=0.2] {b}a talidomida. [p=0.3] Em poucos anos, {c}cerca de dez mil bebês nasceram com malformações. [p=0.3] Parte da explicação está numa molécula que tem {d}uma gêmea no espelho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}achar o carbono quiral, [p=0.2] {c}contar os isômeros ópticos com uma potência [p=0.2] e {d}entender o caso da talidomida."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai precisar de duas coisas. [p=0.2] {a}Isômeros têm a mesma fórmula molecular e estruturas diferentes. [p=0.3] E {b}potência: dois elevado a três é dois vezes dois vezes dois, {c}que dá oito."),
    # mãos
    dict(id="s04", block="maos", text="Olhe para as suas mãos. [p=0.2] {a}Elas têm as mesmas partes, na mesma ordem. [p=0.2] {b}Uma é a imagem da outra no espelho. [p=0.3] Mas {c}tente encaixar uma sobre a outra, palma com costas: [p=0.2] {d}o polegar fica do lado errado."),
    dict(id="s05", block="maos", text="Por isso a luva da mão direita não serve na esquerda. [p=0.3] Objeto que não se encaixa na própria imagem do espelho se chama {a}quiral, [p=0.2] palavra que vem do grego e quer dizer {b}mão."),
    # carbono quiral
    dict(id="s06", block="quiral", text="Na molécula, quem faz esse papel é {a}o carbono quiral. [p=0.3] É {b}um carbono com quatro ligantes diferentes, [p=0.2] quatro grupos diferentes presos a ele, {c}todos por ligação simples. [p=0.3] Na fórmula, ele costuma ganhar {d}um asterisco."),
    dict(id="s07", block="quiral", text="Veja o ácido lático, do iogurte: [p=0.1] {a}cê agá três, cê agá com ó agá, cê ó ó agá. [p=0.3] O carbono do meio tem {b}um hidrogênio, [p=0.1] {c}um ó agá, [p=0.1] {d}um cê agá três [p=0.1] {e}e um cê ó ó agá. [p=0.3] {f}Quatro ligantes diferentes: carbono quiral."),
    dict(id="s08", block="quiral", text="Com ele, o ácido lático existe em {a}duas formas, [p=0.2] uma {b}imagem da outra no espelho, como as mãos. [p=0.3] {c}Ferver, derreter, dissolver: nisso as duas são iguais. [p=0.3] A diferença aparece {d}na luz polarizada, um tipo especial de luz: [p=0.2] {e}uma forma desvia essa luz para a direita, {f}a outra para a esquerda. [p=0.3] Daí o nome isomeria óptica."),
    # talidomida
    dict(id="s09", block="talidomida", text="E aparece {a}no corpo, porque muitas moléculas do corpo também são quirais. [p=0.3] {b}Na talidomida, uma forma acalmava. [p=0.2] {c}A outra foi ligada às malformações. [p=0.3] E pior: {d}o próprio corpo transforma uma forma na outra. [p=0.2] Por isso, nem separar as duas tornaria o remédio seguro na gravidez."),
    # contar
    dict(id="s10", block="contar", text="Agora, a conta. [p=0.2] {a}Cada carbono quiral pode ficar de dois jeitos. [p=0.2] {b}Com um carbono quiral, são dois isômeros. [p=0.2] {c}Com dois, dois vezes dois, quatro. [p=0.2] {d}Com três, oito."),
    dict(id="s11", block="contar", text="Então, com ene carbonos quirais diferentes, {a}o número de isômeros ópticos é dois elevado a ene. [p=0.3] A glicose, na forma de cadeia aberta, tem {b}quatro carbonos quirais: [p=0.2] dois elevado a quatro {c}dá dezesseis isômeros."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com um erro comum: [p=0.2] {a}achar que todo carbono com ó agá no meio da cadeia é quiral. [p=0.3] {b}Veja o propan dois ol: cê agá três, cê agá com ó agá, cê agá três."),
    dict(id="s13", block="erro", text="O carbono do meio tem {a}hidrogênio, ó agá {b}e dois grupos cê agá três. [p=0.3] {c}Dois ligantes iguais: não é quiral. [p=0.3] Agora, troque um cê agá três por um cê agá dois cê agá três: [p=0.2] {d}é o butan dois ol, [p=0.2] e {e}o carbono do meio passa a ser quiral."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.2] {a}antes de testar, risque os carbonos que nunca são quirais. [p=0.3] {b}Carbono de ligação dupla ou tripla: [p=0.1] ele não tem quatro ligantes. [p=0.3] {c}Carbono com dois ou três hidrogênios, como cê agá dois e cê agá três: [p=0.1] já tem dois ligantes iguais. [p=0.3] {d}Sobram poucos para olhar com calma."),
    dict(id="s15", block="atalho", text="{a}Só não confie no dois elevado a ene quando a molécula é simétrica, com as duas metades iguais. [p=0.2] {b}Aí o número real é menor, e isso fica para outra aula."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Na tela, uma cadeia de cinco carbonos, com um ó agá no carbono dois e outro no carbono três. [p=0.3] {b}Quantos carbonos quirais ela tem? [p=0.2] {c}E quantos isômeros ópticos?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Primeiro, o atalho. [p=0.2] {a}Os cê agá três das pontas e o cê agá dois saem. [p=0.3] Sobram os carbonos dois e três. [p=0.2] {b}O carbono dois tem hidrogênio, ó agá, cê agá três e o resto da cadeia: [p=0.1] quiral. [p=0.3] {c}O carbono três tem hidrogênio, ó agá, cê agá dois cê agá três e o outro lado da cadeia: [p=0.1] quiral."),
    dict(id="s19", block="resposta", text="São {a}dois carbonos quirais, e as metades da molécula são diferentes. [p=0.3] Então, {b}dois elevado a dois, [p=0.1] {c}quatro isômeros ópticos."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}carbono quiral tem quatro ligantes diferentes, [p=0.1] {b}cada um dá duas formas, uma imagem da outra no espelho, [p=0.1] e {c}ene carbonos quirais dão dois elevado a ene isômeros."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai praticar o módulo: [p=0.2] {a}ponto de ebulição, solubilidade e as isomerias, [p=0.2] em questões com {b}remédios e alimentos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
