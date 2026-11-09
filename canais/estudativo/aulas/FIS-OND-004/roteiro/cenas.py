# Estudativo · FIS-OND-004 — Interferência e polarização (Física · Ondas e Som · Ondas e seus fenômenos).
# Habilidade: prever reforço ou cancelamento de ondas, explicar o fone com cancelamento de ruído e dizer quais ondas polarizam.
# Pré-requisitos: FIS-OND-003 (fenômenos ondulatórios). Usa também FIS-OND-002 (crista, vale, λ, transversal e longitudinal). Próxima: FIS-OND-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. A regra da diferença de caminho vale para fontes em fase ("juntas, no mesmo tempo").

TITULO = "Interferência e polarização"

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
    dict(id="s01", block="gancho", text="{a}Um fone de ouvido apaga o barulho do avião [p=0.2] {b}jogando mais som no seu ouvido. [p=0.3] {c}Som mais som dando silêncio. [p=0.2] Parece mágica, mas é Física."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai prever quando duas ondas {b}se reforçam [p=0.1] ou {c}se cancelam, [p=0.2] e dizer {d}quais ondas podem ser polarizadas."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}crista, vale, amplitude e lambda no desenho da onda; [p=0.2] e {c}a diferença entre onda transversal e longitudinal. [p=0.3] Se faltar alguma, procure no canal."),
    # interferência
    dict(id="s04", block="soma", text="Quando duas ondas se encontram no mesmo ponto, {a}elas se somam. [p=0.2] Esse encontro se chama {b}interferência. [p=0.3] E depois do encontro, {c}cada uma segue o seu caminho, como se nada tivesse acontecido."),
    dict(id="s05", block="soma", text="{a}Crista com crista: [p=0.1] as alturas se somam, e a onda fica maior. [p=0.2] É a {b}interferência construtiva. [p=0.3] {c}Duas cristas de dois centímetros fazem uma de quatro."),
    dict(id="s06", block="soma", text="{a}Crista com vale: [p=0.1] uma sobe, a outra desce, e elas se descontam. [p=0.2] É a {b}interferência destrutiva. [p=0.3] {c}Se as amplitudes são iguais, a soma dá zero: [p=0.1] naquele ponto, o meio fica parado."),
    # fone
    dict(id="s07", block="fone", text="É isso que o fone faz. [p=0.2] {a}Um microfone capta o ruído de fora. [p=0.2] {b}O fone toca uma onda igual, mas invertida: [p=0.1] crista onde o ruído tem vale. [p=0.3] {c}No seu ouvido, as duas se cancelam."),
    # prever
    dict(id="s08", block="prever", text="Agora, como prever. [p=0.2] Duas caixas de som {a}tocam a mesma onda, juntas. [p=0.2] Você está num ponto. [p=0.2] O que decide é {b}a diferença entre as distâncias até cada caixa."),
    dict(id="s09", block="prever", text="{a}Se a diferença for um número inteiro de lambdas, [p=0.1] zero, um, dois, [p=0.2] crista chega com crista: {b}reforço. [p=0.3] {c}Se for meio lambda, um lambda e meio, dois lambdas e meio, [p=0.2] crista chega com vale: {d}cancelamento."),
    dict(id="s10", block="prever", text="Com {a}lambda de dois metros: [p=0.2] num ponto a {b}cinco metros de uma caixa e sete da outra, [p=0.1] {c}a diferença é dois metros, um lambda: reforço. [p=0.3] Num ponto a {d}cinco e seis metros, [p=0.1] {e}a diferença é um metro, meio lambda: cancelamento."),
    # polarização
    dict(id="s11", block="polariza", text="Agora, a {a}polarização. [p=0.2] Passe uma corda por {b}uma grade de ripas em pé. [p=0.3] {c}A onda que sobe e desce passa pela fresta. [p=0.2] {d}A que vai para os lados bate nas ripas e para. [p=0.3] Do outro lado, só sobra {e}uma direção de vibração: a onda foi polarizada."),
    dict(id="s12", block="polariza", text="Só {a}onda transversal pode ser polarizada. [p=0.2] {b}Na longitudinal, a vibração já é na direção do caminho: não há o que filtrar. [p=0.3] Por isso, {c}o som não polariza. [p=0.2] {d}E a luz polariza: [p=0.1] é a prova de que a luz é transversal. [p=0.3] {e}Os óculos de sol polarizados usam isso: [p=0.1] cortam o brilho refletido na água e no asfalto."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: {a}olhar as distâncias, e não a diferença. [p=0.2] Um ponto está {b}a três metros de uma caixa e a três metros e meio da outra, [p=0.1] com lambda de um metro. [p=0.3] {c}As distâncias são quase iguais, e parece reforço. [p=0.2] {d}Mas a diferença é meio metro, meio lambda: [p=0.1] {e}ali, o som se cancela."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}divida a diferença por meio lambda. [p=0.3] {b}Deu par: reforço. [p=0.1] {c}Deu ímpar: cancelamento. [p=0.2] Zero conta como par. [p=0.3] Funciona porque cada meio lambda a mais troca crista por vale. [p=0.2] Se não der número inteiro, fica no meio do caminho: nem reforço nem cancelamento total. [p=0.3] {d}Só vale com fontes que soltam a crista no mesmo instante, como nas questões. [p=0.2] Se uma estiver invertida, como no fone, a regra se inverte."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Duas caixas de som tocam juntas uma onda de {a}cento e setenta hertz. [p=0.2] O som anda a {b}trezentos e quarenta metros por segundo. [p=0.3] {c}Num ponto a cinco metros de uma caixa e a oito da outra, o som se reforça ou se cancela? [p=0.2] {d}E o som pode ser polarizado?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Lambda é trezentos e quarenta dividido por cento e setenta: dois metros. [p=0.2] {b}Meio lambda, um metro. [p=0.3] {c}A diferença é oito menos cinco, três metros. [p=0.2] {d}Três dividido por um, três: ímpar. [p=0.2] {e}Cancelamento. [p=0.3] E {f}o som não pode ser polarizado: é onda longitudinal."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}crista com crista reforça, crista com vale cancela; [p=0.2] {b}diferença dividida por meio lambda: par reforça, ímpar cancela; [p=0.2] e {c}só onda transversal polariza."),
    dict(id="s19", block="fim", text="Na próxima aula, {a}você pratica tudo do módulo: [p=0.2] {b}pêndulo, mola, a equação da onda e cada fenômeno numa situação. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
