# Estudativo · MAT-PLN-007 — Praticando: polinômios e raízes (Matemática · Polinômios · Raízes e relações de Girard · prática).
# Habilidade: dividir polinômios, baixar o grau com uma raiz dada e usar Girard sem resolver a equação.
# Pré-requisitos: MAT-PLN-001, MAT-PLN-002, MAT-PLN-003, MAT-PLN-004, MAT-PLN-005, MAT-PLN-006. Próxima: MAT-PLN-008.
# Questões inéditas, criadas para esta aula, uma por aula do módulo. Raízes complexas (MAT-PLN-008) ainda não foram ensinadas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; k se fala "ká".

TITULO = "Praticando: polinômios e raízes"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões criadas para esta aula, [p=0.2] uma para cada ferramenta de polinômios. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}a identidade de polinômios, [p=0.2] {b}o teorema do resto, [p=0.2] {c}o Briô-Rufíni, [p=0.2] {d}o sinal pela multiplicidade [p=0.2] e {e}as relações de Jirár. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: identidade
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] Ache á e bê para que {b}á vezes, abre parênteses, xis menos um, fecha parênteses, ao quadrado, mais bê, [p=0.2] seja idêntico a {c}dois xis ao quadrado menos quatro xis mais cinco."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Abra o quadrado: á vezes, abre parênteses, xis ao quadrado menos dois xis mais um, fecha parênteses, mais bê. [p=0.2] {b}Distribua o á: á xis ao quadrado, menos dois á xis, mais á, mais bê."),
    dict(id="s06", block="resposta1", text="Compare termo a termo. [p=0.2] {a}No xis ao quadrado: á igual a dois. [p=0.2] {b}No xis: menos dois á dá menos quatro, e bate. [p=0.2] {c}No número sozinho: á mais bê é cinco. [p=0.2] {d}Dois mais bê dá cinco, então bê vale três."),
    # questão 2: teorema do resto
    dict(id="s07", block="questao2", text="{a}Questão dois. [p=0.2] Ache o valor de ká para que {b}xis ao cubo mais ká xis menos quatro [p=0.2] seja divisível por {c}xis menos dois."),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Divisível é {a}resto zero. [p=0.2] Pelo teorema do resto, {b}P de dois tem que dar zero. [p=0.3] {c}Oito mais dois ká menos quatro igual a zero. [p=0.2] {d}Quatro mais dois ká igual a zero: dois ká igual a menos quatro, [p=0.2] e {e}ká igual a menos dois. [p=0.3] {f}Sem armar nenhuma chave."),
    # questão 3: raiz dada
    dict(id="s10", block="questao3", text="{a}Questão três. [p=0.2] Sabendo que {b}menos um é raiz de xis ao cubo mais dois xis ao quadrado menos cinco xis menos seis, [p=0.2] {c}ache as outras raízes."),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] {a}Briô-Rufíni com o menos um: um, dois, menos cinco, menos seis. [p=0.3] {b}Baixe o um. [p=0.2] {c}Menos um mais dois, um. [p=0.2] {d}Menos um menos cinco, menos seis. [p=0.2] {e}Seis menos seis, zero."),
    dict(id="s13", block="resposta3", text="Sobra {a}xis ao quadrado mais xis menos seis igual a zero. [p=0.2] {b}Delta: um mais vinte e quatro, vinte e cinco. Raiz, cinco. [p=0.3] {c}Menos um mais cinco, dividido por dois, dois. [p=0.2] {d}Menos um menos cinco, dividido por dois, menos três. [p=0.3] Raízes: {e}menos um, dois e menos três."),
    # questão 4: sinal
    dict(id="s14", block="questao4", text="{a}Questão quatro. [p=0.2] Resolva {b}xis mais dois, ao quadrado, vezes xis menos um, menor que zero."),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] Raízes: {a}menos dois, dupla, [p=0.2] e {b}um, simples. [p=0.3] {c}Depois do um, mais. [p=0.2] {d}O um é raiz simples, troca: menos entre menos dois e um. [p=0.2] {e}O menos dois é raiz dupla, mantém: menos também antes dele."),
    dict(id="s17", block="resposta4", text="Menor que zero pede {a}os pedaços com menos, sem os zeros. [p=0.2] Resposta: {b}xis menor que um e xis diferente de menos dois. [p=0.3] Quem respondeu {c}só entre menos dois e um [p=0.2] trocou o sinal na raiz dupla."),
    # questão 5: Girard
    dict(id="s18", block="questao5", text="{a}Última questão. [p=0.2] Duas raízes de {b}xis ao cubo menos sete xis ao quadrado mais catorze xis menos oito igual a zero [p=0.2] {c}somam três. [p=0.2] {d}Qual é a terceira?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Pela soma de Jirár, {a}as três raízes somam sete: menos bê dividido por á. [p=0.2] {b}Duas somam três, então a terceira é sete menos três: quatro. [p=0.3] Conferindo: {c}sessenta e quatro menos cento e doze mais cinquenta e seis menos oito: zero. [p=0.2] Bateu."),
    # atalho
    dict(id="s21", block="atalho", text="O atalho desta prática: {a}antes de qualquer conta, teste o um, [p=0.2] porque P de um é só somar os coeficientes. [p=0.3] Na última questão, {b}um menos sete mais catorze menos oito dá zero: [p=0.2] {c}o um é raiz. [p=0.3] Então a raiz que falta é {d}sete menos um menos quatro: dois. [p=0.3] {e}Se a soma não der zero, o um não é raiz: siga o enunciado."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}divisível é resto zero, [p=0.2] {b}uma raiz conhecida baixa o grau, [p=0.2] e {c}Jirár dá soma e produto sem resolver."),
    dict(id="s23", block="fim", text="Na próxima aula, você resolve a equação que parecia não ter solução: [p=0.2] {a}a de delta negativo, [p=0.2] com o {b}número í, que ao quadrado dá menos um. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
