# Estudativo · FIS-MAG-001 — Ímãs e campo magnético (Física · Magnetismo · Magnetismo e indução).
# Habilidade: desenhar as linhas de campo de um ímã, explicar a bússola e dizer por que o ímã partido gera dois ímãs.
# Pré-requisitos: FIS-ELE-003 (campo elétrico e linhas de força). Próxima: FIS-MAG-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Primeira aula do Magnetismo: guarda a linguagem visual da trilha (veja o visual.py). Questão inédita, criada para esta aula.
# Corrente elétrica (FIS-ELE-008) não está em "Já ensinado": a origem do magnetismo no movimento das cargas fica como
# assunto de outra aula. "B" é narrado "bê"; tesla é a unidade, sem conta nesta aula.

TITULO = "Ímãs e campo magnético"

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
    dict(id="s01", block="gancho", text="{a}Pegue um ímã e {b}quebre ao meio. [p=0.3] Um pedaço fica só com o norte, [p=0.1] e o outro só com o sul? [p=0.4] {c}Não. [p=0.2] Você ganha {d}dois ímãs inteiros, [p=0.2] cada um com norte e sul."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai desenhar as linhas de campo de um ímã, [p=0.2] {b}explicar como a bússola funciona [p=0.2] e {c}entender por que o ímã partido vira dois."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas do campo elétrico. [p=0.2] {b}As linhas de força saem da carga positiva e entram na negativa. [p=0.3] E {c}onde as linhas ficam mais juntas, o campo é mais forte. [p=0.3] Se faltar alguma, procure no canal."),
    # polos
    dict(id="s04", block="polos", text="Todo ímã tem {a}duas pontas, chamadas polos: [p=0.2] o {b}polo norte [p=0.1] e o {c}polo sul. [p=0.3] Aproxime dois ímãs. [p=0.2] {d}Norte com norte, eles se empurram. [p=0.2] {e}Norte com sul, eles se puxam."),
    dict(id="s05", block="polos", text="É a mesma regra das cargas: [p=0.2] {a}iguais se repelem, [p=0.1] {b}diferentes se atraem. [p=0.3] E o ímã empurra ou puxa {c}sem encostar, [p=0.2] como a carga elétrica. [p=0.3] Então, em volta dele, também existe um campo."),
    # campo
    dict(id="s06", block="campo", text="É o {a}campo magnético: [p=0.2] a região em volta do ímã onde {b}outro ímã sente força. [p=0.3] Ele é representado pela letra {c}bê, [p=0.2] e a unidade dele no Sistema Internacional é o {d}tesla. [p=0.3] O campo bê é um vetor: [p=0.2] em cada ponto, {e}tem direção e sentido."),
    # linhas
    dict(id="s07", block="linhas", text="Para enxergar o campo, a gente desenha {a}linhas de campo, [p=0.2] como as linhas de força. [p=0.3] Do lado de fora do ímã, {b}elas saem do polo norte, [p=0.2] {c}dão a volta [p=0.1] e {d}entram no polo sul."),
    dict(id="s08", block="linhas", text="Três regras para desenhar. [p=0.2] {a}Primeira: em cada ponto, o vetor bê é tangente à linha, [p=0.2] quer dizer, encosta nela e segue o sentido da seta. [p=0.3] {b}Segunda: perto dos polos, as linhas se apertam, [p=0.2] e o campo é mais forte. [p=0.3] {c}Terceira: duas linhas nunca se cruzam."),
    dict(id="s09", block="linhas", text="Uma diferença das linhas de força: [p=0.2] {a}as linhas de campo não terminam no polo. [p=0.2] {b}Por dentro do ímã, elas voltam do sul para o norte [p=0.2] e {c}se fecham, como um laço."),
    # bússola
    dict(id="s10", block="bussola", text="Agora, a {a}bússola. [p=0.2] A agulha dela é {b}um ímã pequeno e leve, que gira à vontade. [p=0.3] Ela {c}se alinha com a linha de campo, [p=0.2] e {d}o polo norte da agulha aponta no sentido do campo bê."),
    dict(id="s11", block="bussola", text="Por isso, a bússola é um medidor de campo. [p=0.2] {a}Espalhe várias em volta de um ímã: [p=0.2] {b}cada agulha desenha um pedacinho da linha de campo."),
    dict(id="s12", block="bussola", text="E longe de qualquer ímã, ela aponta para o norte. [p=0.3] Por quê? [p=0.2] {a}Porque a Terra também é um ímã gigante. [p=0.3] {b}O norte da agulha é atraído por um polo sul. [p=0.2] Então, {c}perto do polo norte geográfico, fica o polo sul magnético da Terra."),
    # partido
    dict(id="s13", block="partido", text="Voltando ao ímã partido. [p=0.2] Pense no ímã como {a}uma fila de ímãs minúsculos, [p=0.2] todos virados para o mesmo lado. [p=0.3] {b}Corte a fila no meio. [p=0.2] {c}Cada metade ainda começa num sul e termina num norte."),
    dict(id="s14", block="partido", text="Corte de novo, e de novo: [p=0.2] {a}sempre aparecem os dois polos. [p=0.3] {b}Não existe polo magnético sozinho. [p=0.3] É aqui que o ímã {c}é diferente da carga: [p=0.2] uma carga positiva pode ficar sozinha. [p=0.2] {d}Um polo norte, não. [p=0.3] {e}De onde vêm esses ímãs minúsculos é assunto de outra aula."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o norte da bússola aponta para um polo norte magnético. [p=0.3] {b}Se fosse assim, norte com norte se empurrariam, [p=0.2] e a agulha fugiria. [p=0.3] {c}O norte geográfico da Terra é um sul magnético."),
    # atalho
    dict(id="s16", block="atalho", text="Agora, o atalho de prova. [p=0.2] Guarde: [p=0.1] por fora do ímã, {a}a linha sai do norte [p=0.2] e {b}entra no sul. [p=0.3] É uma rua de mão única: do norte para o sul, por fora. [p=0.3] {c}E a bússola é uma seta do campo: [p=0.2] o norte da agulha aponta para onde a linha vai."),
    dict(id="s17", block="atalho", text="Funciona com qualquer ímã: [p=0.2] {a}ímã em barra, [p=0.1] {b}ímã de ferradura, [p=0.1] e até a Terra. [p=0.3] Na prova, para achar o sentido da agulha, [p=0.2] {c}desenhe a linha que passa no ponto [p=0.1] e siga a seta. [p=0.3] {d}Bem perto de um polo, nem precisa desenhar: [p=0.2] perto do norte, a agulha aponta para longe dele; [p=0.1] perto do sul, aponta para ele."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}Um ímã em barra está deitado, com o norte à direita. [p=0.3] {b}Uma bússola fica logo à direita do polo norte. [p=0.3] {c}Para onde aponta o norte da agulha? [p=0.3] E mais: {d}se o ímã for partido ao meio, que polo aparece na ponta quebrada do pedaço que tem o norte?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Do lado de fora, a linha sai do norte. [p=0.2] Logo à direita dele, {b}ela sai reta para a direita. [p=0.3] {c}O norte da agulha aponta para a direita, [p=0.1] para longe do ímã."),
    dict(id="s21", block="resposta", text="{a}Agora, o ímã partido. [p=0.2] O pedaço da direita tem o norte na ponta direita. [p=0.2] {b}Na ponta quebrada, que é a esquerda dele, [p=0.1] {c}aparece um polo sul. [p=0.3] Cada pedaço {d}é um ímã inteiro."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}polos iguais se repelem, [p=0.2] {b}por fora, a linha sai do norte e entra no sul, [p=0.2] {c}a bússola aponta no sentido do campo, [p=0.2] e {d}todo ímã tem dois polos."),
    dict(id="s23", block="fim", text="Na próxima aula, você vai ver {a}uma corrente elétrica mexer numa bússola, [p=0.2] e {b}achar o campo de um fio com a regra da mão direita. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
