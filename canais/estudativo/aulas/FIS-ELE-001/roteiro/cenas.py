# Estudativo · FIS-ELE-001 — Carga elétrica e eletrização (Física · Eletricidade · Eletrostática).
# Habilidade: calcular Q = n·e e dizer como fica a carga de cada corpo na eletrização por atrito, contato e indução.
# Pré-requisitos: QUI-ATO-004 (prótons e elétrons), MAT-POT-013 (contas em notação científica). Próxima: FIS-ELE-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Primeira aula de Eletricidade: guarda a linguagem visual da trilha (veja o visual.py). Questão inédita, criada para esta aula.
# Limites da ficha: FIS-CIN-001 (SI) não está em "Já ensinado": o coulomb é apresentado aqui; nada de força em newton.
# "micro" (µ) é explicado na hora como "vezes dez elevado a menos seis" (prefixos não estão em "Já ensinado").
# A letra e da carga elementar é narrada "ê". Pente de plástico no cabelo seco: o pente fica negativo e o cabelo positivo.

TITULO = "Carga elétrica e eletrização"

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
    dict(id="s01", block="gancho", text="{a}Passe um pente de plástico no cabelo seco [p=0.2] e {b}aproxime de pedacinhos de papel. [p=0.3] {c}O papel pula e gruda no pente. [p=0.3] Sem cola e sem ímã: [p=0.2] só {d}elétrons que mudaram de lugar."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a carga de um corpo [p=0.2] {b}contando elétrons, [p=0.2] e dizer como fica cada corpo {c}no atrito, no contato e na indução."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o átomo tem prótons no núcleo e elétrons em volta; [p=0.3] e {c}as potências de dez: [p=0.1] para multiplicar, some os expoentes, [p=0.1] e para dividir, subtraia. [p=0.3] Se faltar alguma, procure no canal."),
    # carga
    dict(id="s04", block="carga", text="Prótons e elétrons têm {a}carga elétrica. [p=0.2] A do próton é {b}positiva, [p=0.1] a do elétron é {c}negativa, [p=0.2] e elas têm {d}o mesmo tamanho. [p=0.3] Num corpo comum, há {e}tantos prótons quanto elétrons: [p=0.2] as cargas se cancelam, e o corpo é {f}neutro."),
    dict(id="s05", block="carga", text="Para eletrizar um corpo, [p=0.1] quem se mexe são {a}os elétrons. [p=0.2] Os prótons ficam presos no núcleo. [p=0.3] {b}Perdeu elétrons? Sobram prótons, e o corpo fica {c}positivo. [p=0.3] {d}Ganhou elétrons? Fica {e}negativo."),
    dict(id="s06", block="carga", text="E corpos carregados se empurram ou se puxam. [p=0.2] {a}Cargas de mesmo sinal se repelem, [p=0.1] quer dizer, se afastam. [p=0.3] {b}Cargas de sinais opostos se atraem."),
    # Q = n·e
    dict(id="s07", block="quantidade", text="A carga se mede em {a}coulomb, com a letra cê maiúscula. [p=0.3] A carga de um único elétron vale {b}um vírgula seis vezes dez elevado a menos dezenove coulomb. [p=0.3] É a {c}carga elementar, a letra ê: [p=0.2] a menor carga que se encontra solta na natureza."),
    dict(id="s08", block="quantidade", text="Por isso, a carga de um corpo é {a}quê igual a ene vezes ê. [p=0.3] {b}Quê é a carga, em coulomb; [p=0.2] {c}ene é quantos elétrons o corpo ganhou ou perdeu; [p=0.2] e {d}ê é a carga elementar."),
    dict(id="s09", block="quantidade", text="Um corpo {a}perdeu cinco vezes dez elevado a doze elétrons. [p=0.3] {b}Cinco vezes um vírgula seis dá oito. [p=0.2] {c}Nos expoentes, doze menos dezenove, menos sete. [p=0.3] A carga é {d}oito vezes dez elevado a menos sete coulomb, [p=0.2] {e}positiva, porque ele perdeu elétrons."),
    # atrito
    dict(id="s10", block="atrito", text="Agora, os três jeitos de eletrizar. [p=0.2] O primeiro é o {a}atrito: esfregar um corpo no outro. [p=0.3] No pente e no cabelo, {b}elétrons passam do cabelo para o pente. [p=0.3] {c}O pente fica negativo, [p=0.1] {d}o cabelo fica positivo. [p=0.3] {e}Sinais opostos, e cargas de mesmo tamanho: [p=0.2] o que um perdeu, o outro ganhou."),
    # condutor e isolante
    dict(id="s11", block="contato", text="Para os outros dois jeitos, uma ideia. [p=0.2] Nos {a}metais, os elétrons andam com facilidade: [p=0.1] eles são {b}condutores. [p=0.3] No {c}plástico, no vidro e na borracha, os elétrons quase não andam: [p=0.1] são {d}isolantes."),
    # contato
    dict(id="s12", block="contato", text="O segundo jeito é o {a}contato. [p=0.2] Encoste uma esfera de metal carregada {b}em outra, neutra. [p=0.3] {c}Elétrons passam de uma esfera para a outra, [p=0.2] e as duas ficam com {d}carga de mesmo sinal. [p=0.3] Se as esferas forem {e}iguais, cada uma fica com {f}a metade do total."),
    dict(id="s13", block="contato", text="A esfera um tem {a}mais oito microcoulombs. [p=0.2] Micro quer dizer {b}vezes dez elevado a menos seis. [p=0.3] A esfera dois, igual, tem {c}menos dois microcoulombs. [p=0.3] Encoste uma na outra. [p=0.2] {d}Some com o sinal: oito menos dois, seis. [p=0.2] {e}Divida por dois: [p=0.1] {f}cada uma fica com mais três microcoulombs. [p=0.3] {g}A soma não mudou: seis antes, seis depois. [p=0.2] A carga se conserva."),
    # indução
    dict(id="s14", block="inducao", text="O terceiro jeito é a {a}indução, sem encostar. [p=0.2] Aproxime {b}um bastão negativo de uma esfera de metal neutra. [p=0.3] {c}Os elétrons da esfera fogem para o lado de longe, [p=0.2] e {d}o lado de perto fica positivo. [p=0.3] A esfera continua neutra: [p=0.1] só {e}separou as cargas."),
    dict(id="s15", block="inducao", text="Para ela ficar carregada, {a}ligue a esfera à terra com um fio. [p=0.2] A terra funciona como um depósito enorme de elétrons, [p=0.2] e {b}os elétrons empurrados pelo bastão descem pelo fio. [p=0.3] {c}Corte o fio, [p=0.1] {d}afaste o bastão, [p=0.2] e a esfera fica {e}positiva: [p=0.2] {f}sinal oposto ao do bastão, que nem encostou nela."),
    dict(id="s16", block="inducao", text="É parecido com o papel do começo. [p=0.2] {a}O pente negativo empurra os elétrons do papel. [p=0.2] Como o papel é isolante, eles só se deslocam um pouquinho, [p=0.2] mas {b}o lado de perto fica positivo, [p=0.2] e {c}o papel é puxado."),
    # erro
    dict(id="s17", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o corpo positivo ganhou prótons. [p=0.3] {b}Prótons não saem do núcleo numa eletrização. [p=0.3] {c}Positivo é falta de elétrons; [p=0.2] {d}negativo é excesso de elétrons. [p=0.3] Na indução, a esfera ficou positiva porque {e}perdeu elétrons para a terra."),
    # atalho
    dict(id="s18", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}grave o sinal de cada jeito. [p=0.3] {b}Atrito: sinais opostos. [p=0.2] {c}Contato: mesmo sinal. [p=0.2] {d}Indução com fio terra: sinal oposto ao do corpo que induziu. [p=0.3] E no contato entre esferas iguais, {e}some as cargas com o sinal e divida por dois."),
    dict(id="s19", block="atalho", text="Funciona porque {a}a carga total não muda: [p=0.2] o que um corpo perde, o outro ganha. [p=0.3] {b}Não vale dividir meio a meio quando as esferas têm tamanhos diferentes: [p=0.2] a maior fica com mais carga."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Uma esfera de metal tem carga de {a}menos três vírgula dois vezes dez elevado a menos seis coulomb. [p=0.3] {b}Ela ganhou ou perdeu elétrons? E quantos? [p=0.3] {c}Depois, ela encosta em outra esfera igual, neutra. [p=0.2] {d}Com que carga cada uma fica?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] A carga é negativa, então {a}ela ganhou elétrons. [p=0.3] Para achar quantos, {b}divida a carga pela carga elementar. [p=0.2] {c}Três vírgula dois dividido por um vírgula seis, dois. [p=0.2] {d}Dividir por dez elevado a menos dezenove é multiplicar por dez elevado a dezenove: [p=0.1] menos seis mais dezenove, treze. [p=0.3] {e}Dois vezes dez elevado a treze elétrons."),
    dict(id="s23", block="resposta", text="No contato com a esfera neutra: [p=0.2] {a}menos três vírgula dois mais zero, [p=0.1] {b}dividido por dois. [p=0.3] {c}Cada uma fica com menos um vírgula seis vezes dez elevado a menos seis coulomb. [p=0.2] {d}Mesmo sinal, como sempre no contato."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}quem se mexe são os elétrons; [p=0.2] {b}a carga é ene vezes ê; [p=0.2] e {c}atrito dá sinais opostos, contato dá o mesmo sinal, [p=0.1] e indução com terra, o sinal oposto ao do corpo que induziu."),
    dict(id="s25", block="fim", text="Na próxima aula, você vai calcular {a}a força entre duas cargas, a lei de Coulomb, [p=0.2] e ver por que {b}dobrar a distância divide a força por quatro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
