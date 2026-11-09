# Estudativo · FIS-DIN-003 — Terceira lei: ação e reação (Física · Dinâmica · Leis de Newton).
# Habilidade: achar o par de ação e reação de uma força e dizer por que as duas não se anulam.
# Pré-requisitos: FIS-DIN-001 (força resultante, inércia). Próxima: FIS-DIN-004.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# F = m·a (FIS-DIN-002), aceleração (FIS-CIN-007), peso e normal (FIS-DIN-004) não estão em "Já ensinado": o livro na mesa é
# contado sem os nomes (a Terra puxa, a mesa empurra) e os nomes ficam como ponte para a próxima aula; na batida, o "estrago
# maior no carro" é só citado como assunto da segunda lei.

TITULO = "Terceira lei: ação e reação"

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
    dict(id="s01", block="gancho", text="{a}Um cavalo puxa uma carroça. [p=0.2] Pela terceira lei de Newton, {b}a carroça puxa o cavalo de volta, com a mesma força. [p=0.3] {c}Então, como os dois saem do lugar?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}achar o par de ação e reação de qualquer força [p=0.2] e entender {c}por que as duas não se anulam."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}força é um vetor, com módulo, direção e sentido; [p=0.2] e {c}o que decide o movimento de um corpo é a resultante das forças nele. [p=0.3] Se faltar alguma, procure no canal."),
    # a lei
    dict(id="s04", block="lei", text="Força é sempre {a}uma troca entre dois corpos. [p=0.3] {b}Se a sua mão empurra a mesa, [p=0.2] {c}a mesa empurra a sua mão. [p=0.3] As duas têm {d}o mesmo módulo, {e}a mesma direção [p=0.1] e {f}sentidos opostos."),
    dict(id="s05", block="lei", text="{a}De patins, empurre uma parede. [p=0.2] Você faz força na parede, [p=0.1] e {b}a parede faz força em você: [p=0.2] {c}é ela que joga você para trás."),
    dict(id="s06", block="lei", text="{a}Para andar, seu pé empurra o chão para trás, [p=0.2] e {b}o chão empurra você para a frente. [p=0.3] {c}No foguete, ele empurra os gases para baixo, [p=0.2] e {d}os gases empurram o foguete para cima."),
    dict(id="s07", block="lei", text="E não precisa encostar. [p=0.2] {a}Um ímã atrai um prego. [p=0.2] {b}O prego atrai o ímã, com a mesma força. [p=0.3] {c}Segure o prego e solte o ímã: [p=0.2] {d}é o ímã que anda até o prego."),
    # o par
    dict(id="s08", block="par", text="Como achar o par de uma força? [p=0.2] {a}Troque os nomes de lugar. [p=0.3] {b}Pé empurra chão [p=0.1] vira {c}chão empurra pé. [p=0.3] As duas forças {d}nascem juntas e somem juntas, [p=0.2] e {e}cada uma age num corpo diferente."),
    # não se anulam
    dict(id="s09", block="anula", text="E é por isso que {a}ação e reação nunca se anulam. [p=0.3] Só se somam {b}forças no mesmo corpo. [p=0.2] {c}A força do cavalo está na carroça; [p=0.2] {d}a força da carroça está no cavalo."),
    dict(id="s10", block="anula", text="Para saber se o cavalo anda, {a}olhe só as forças nele. [p=0.3] {b}A carroça puxa para trás. [p=0.2] Mas os cascos empurram o chão para trás, [p=0.2] e {c}o chão empurra o cavalo para a frente. [p=0.3] {d}Se o chão empurra mais do que a carroça puxa, [p=0.1] o cavalo sai do lugar."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum. [p=0.2] {a}Um livro parado na mesa. [p=0.2] {b}A Terra puxa o livro para baixo; [p=0.2] {c}a mesa empurra o livro para cima. [p=0.3] Mesmo módulo, sentidos opostos. [p=0.2] {d}É um par de ação e reação?"),
    dict(id="s12", block="erro", text="{a}Não. [p=0.2] As duas estão {b}no mesmo corpo, o livro. [p=0.3] Troque os nomes: [p=0.2] o par de {c}Terra puxa livro é {d}livro puxa Terra. [p=0.3] E o par de {e}mesa empurra livro é {f}livro empurra mesa. [p=0.3] Elas se igualam por outro motivo: {g}o livro está parado, com resultante zero."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}escreva cada força como uma frase, quem faz em quem. [p=0.3] {b}O par é a mesma frase, de trás para a frente. [p=0.3] {c}Se as duas forças estão no mesmo corpo, não são par."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a terceira lei fala de dois corpos trocando força. [p=0.3] Mas ela {b}não diz se alguém se move: [p=0.2] para isso, {c}esqueça o par e some só as forças no corpo que interessa."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Um caminhão e um carro batem de frente. [p=0.3] {b}A força do caminhão no carro é maior, menor ou igual à força do carro no caminhão?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Troque os nomes: {a}caminhão empurra carro, [p=0.1] {b}carro empurra caminhão. [p=0.3] É um par de ação e reação, então {c}as forças são iguais. [p=0.3] {d}O carro sofre mais estrago, sim, [p=0.2] mas o motivo está na massa, [p=0.1] {e}assunto da segunda lei, não desta."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}toda força tem um par, [p=0.2] {b}com o mesmo módulo e a mesma direção, em sentido oposto, [p=0.2] {c}e em outro corpo. [p=0.2] Por isso, {d}ação e reação nunca se anulam."),
    dict(id="s19", block="fim", text="Na próxima aula, as forças sobre o livro ganham nome: [p=0.2] {a}o peso e a força normal. [p=0.2] E você vai ver por que {b}a balança mente dentro do elevador. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
