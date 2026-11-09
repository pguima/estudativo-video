# Estudativo · FIS-OPT-010 — Praticando: espelhos, lentes e olho (Física · Óptica · Refração, lentes e olho humano). Prática.
# Habilidade: resolver questões de reflexão, refração, lentes e correção da visão.
# Pré-requisitos: FIS-OPT-001 a 009 e FIS-OPT-011. Próxima: nenhuma (última da trilha).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Cinco questões inéditas, criadas para esta aula: espelho plano (002), convexo com Gauss (003/011), ângulo limite (004/005),
# lupa com a equação das lentes (006/007), óculos (007/008). Números diferentes dos exemplos das aulas. Cada uma lembra um atalho.

TITULO = "Praticando óptica: espelhos, lentes e olho"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões, [p=0.2] {b}do espelho aos óculos. [p=0.3] Em cada uma, {c}pause o vídeo, tente, [p=0.2] e depois confira {d}o caminho e o atalho. [p=0.3] Pegue papel e lápis."),
    dict(id="s02", block="gancho", text="Antes, {a}três lembretes que valem para todas. [p=0.2] {b}Com um espelho ou uma lente só, imagem real é invertida, e virtual é direita. [p=0.3] {c}Côncavo e convergente têm efe positivo; [p=0.2] {d}convexo e divergente, efe negativo. [p=0.3] E {e}ângulos sempre medidos a partir da normal."),
    # questão 1: espelho plano
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] Uma loja quer um espelho em que {b}clientes de até cento e noventa centímetros se vejam inteiros. [p=0.3] {c}Qual a altura mínima do espelho? [p=0.2] E {d}se o cliente se afastar, ele vai precisar de um espelho maior? [p=0.3] {e}Para quem tem os olhos a cento e oitenta centímetros do chão, onde fica a borda de baixo?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="{a}A altura mínima é metade da altura da pessoa: [p=0.2] {b}cento e noventa dividido por dois, noventa e cinco centímetros. [p=0.3] {c}E não precisa de espelho maior: [p=0.2] {d}a imagem se afasta junto, o espelho continua no meio do caminho, [p=0.2] e {e}a metade não muda. [p=0.3] {f}A borda de baixo fica na metade da altura dos olhos: [p=0.2] {g}noventa centímetros do chão."),
    # questão 2: retrovisor convexo
    dict(id="s06", block="q2", text="{a}Questão dois. [p=0.2] Um retrovisor convexo tem {b}foco de dois metros. [p=0.3] {c}Um carro está oito metros atrás dele. [p=0.3] {d}Onde se forma a imagem do carro, [p=0.2] e {e}quantas vezes ela é menor?"),
    dict(id="s07", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="r2", text="{a}Convexo: efe é menos dois. [p=0.3] Pelo atalho, {b}pê linha é efe vezes pê, dividido por pê menos efe: [p=0.2] {c}menos dois vezes oito, menos dezesseis, [p=0.2] {d}dividido por oito menos o menos dois, que dá dez. [p=0.2] {e}Pê linha é menos um vírgula seis metro: [p=0.2] imagem virtual, atrás do espelho."),
    dict(id="s09", block="r2", text="{a}No aumento, o menos da fórmula com o menos do pê linha dá mais: [p=0.2] {b}um vírgula seis dividido por oito, zero vírgula dois. [p=0.3] {c}Direita e cinco vezes menor. [p=0.3] {d}Por isso alguns retrovisores avisam que os objetos estão mais perto do que parecem: [p=0.2] a imagem é pequena, e o cérebro acha que o carro está mais longe."),
    # questão 3: ângulo limite
    dict(id="s10", block="q3", text="{a}Questão três. [p=0.2] Um raio vai de {b}um material de índice dois para o ar, [p=0.2] {c}chegando a quarenta graus da normal. [p=0.3] {d}Ele sai para o ar ou reflete por inteiro?"),
    dict(id="s11", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="r3", text="{a}Seno do limite é o menor dividido pelo maior: [p=0.2] {b}um dividido por dois, um meio. [p=0.2] {c}O ângulo limite é trinta graus. [p=0.3] {d}Quarenta é mais que trinta, [p=0.2] e a luz vai do índice maior para o menor. [p=0.3] {e}Reflexão total: o raio não sai, [p=0.2] como na fibra óptica. [p=0.3] {f}Se chegasse a vinte graus, menos que o limite, ele sairia, se afastando da normal."),
    # questão 4: lupa
    dict(id="s13", block="q4", text="{a}Questão quatro. [p=0.2] Uma lupa é uma lente convergente com {b}foco de doze centímetros. [p=0.3] {c}Ela está a oito centímetros de um selo. [p=0.3] {d}Onde fica a imagem, [p=0.2] e {e}quantas vezes ela é maior?"),
    dict(id="s14", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="r4", text="{a}Convergente: efe é mais doze. [p=0.3] {b}Doze vezes oito, noventa e seis, [p=0.2] {c}dividido por oito menos doze, menos quatro: [p=0.2] {d}pê linha é menos vinte e quatro centímetros. [p=0.3] {e}Imagem virtual, do mesmo lado do selo."),
    dict(id="s16", block="r4", text="{a}No aumento, de novo, menos com menos dá mais: [p=0.2] {b}vinte e quatro dividido por oito, três. [p=0.3] {c}Direita e três vezes maior. [p=0.2] {d}Bate com a regra: objeto dentro do foco, imagem de lupa."),
    # questão 5: óculos
    dict(id="s17", block="q5", text="{a}Questão cinco. [p=0.2] Uma receita de óculos pede {b}menos cinco graus. [p=0.3] {c}Que lente é essa, [p=0.2] {d}qual é o foco [p=0.2] e {e}que defeito ela corrige?"),
    dict(id="s18", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="r5", text="{a}Grau negativo: lente divergente. [p=0.3] Pelo atalho, {b}o foco em centímetros é cem dividido pelo grau: [p=0.2] {c}cem dividido por cinco, vinte centímetros, [p=0.2] {d}com sinal de menos. [p=0.3] {e}Míope, menos: ela corrige a miopia, [p=0.2] de quem só vê nítido até vinte centímetros."),
    # fechamento
    dict(id="s20", block="fim", text="Repare que {a}todas saíram com um atalho: [p=0.2] {b}a metade do espelho plano, [p=0.1] {c}efe vezes pê dividido por pê menos efe, nos espelhos e nas lentes, [p=0.1] {d}o menor dividido pelo maior [p=0.1] e {e}cem dividido pelo grau."),
    dict(id="s21", block="fim", text="{a}Errou alguma? [p=0.2] Procure no canal a aula daquele assunto e refaça a questão. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
