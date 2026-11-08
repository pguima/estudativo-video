# Estudativo · MAT-POL-005 — Comprimento de um arco (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: calcular com regra de três o arco de 60° numa circunferência de raio 6 (2π).
# Pré-requisitos: MAT-ANG-001 (volta de 360°), MAT-POL-004 (C = 2πr), MAT-RAZ-006 (regra de três direta). Próxima: MAT-POL-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Comprimento de um arco"

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
    dict(id="s01", block="gancho", text="{a}Uma minipizza de seis centímetros de raio, [p=0.2] cortada em {b}seis fatias iguais. [p=0.3] Quanto mede {c}a borda de uma fatia? [p=0.3] Não precisa de fita métrica: [p=0.2] {d}uma regra de três resolve."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você mede qualquer pedaço de circunferência [p=0.2] e leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}uma volta inteira tem trezentos e sessenta graus, [p=0.2] {c}a volta da circunferência mede dois pi érre, [p=0.2] e {d}a regra de três direta, com a tabela e a cruz. [p=0.3] Se faltar alguma, procure no canal."),
    # arco
    dict(id="s04", block="arco", text="{a}Arco é um pedaço da circunferência, entre dois pontos dela. [p=0.2] Na pizza, {b}é a borda de uma fatia."),
    dict(id="s05", block="arco", text="Ligue cada ponta do arco ao centro. [p=0.2] {a}Os raios formam um ângulo com o vértice no centro: o ângulo central. [p=0.3] Ele diz {b}que pedaço da volta o arco ocupa. [p=0.2] Seis fatias iguais dividem a volta: [p=0.2] {c}trezentos e sessenta dividido por seis dá sessenta graus cada."),
    dict(id="s06", block="arco", text="Agora repare. [p=0.2] {a}Dobrou o ângulo, o arco dobra: [p=0.2] {b}duas fatias têm o dobro de borda de uma. [p=0.2] Três fatias, o triplo. [p=0.2] A pizza inteira, as seis fatias, dá a volta toda. [p=0.3] Ângulo e arco são {c}diretamente proporcionais. [p=0.2] E aí entra a regra de três."),
    # exemplo
    dict(id="s07", block="exemplo", text="{a}Passo um: a volta inteira. [p=0.2] Raio seis: {b}duas vezes pi vezes seis dá doze pi centímetros. [p=0.3] {c}Passo dois: a tabela. [p=0.2] Na primeira linha, {d}trezentos e sessenta graus para doze pi. [p=0.2] Na segunda, {e}sessenta graus para xis."),
    dict(id="s08", block="exemplo", text="{a}Passo três: a cruz. [p=0.2] {b}Trezentos e sessenta xis igual a sessenta vezes doze pi, que dá setecentos e vinte pi. [p=0.2] {c}Divida por trezentos e sessenta: xis igual a dois pi. [p=0.3] Com pi igual a três, {d}duas vezes três dá seis centímetros de borda."),
    dict(id="s09", block="exemplo", text="Confira o sentido: {a}sessenta graus é um pedaço pequeno da volta, [p=0.2] e {b}dois pi é bem menor que doze pi. [p=0.3] Se a prova pedir pi igual a três vírgula catorze, [p=0.2] {c}duas vezes três vírgula catorze dá seis vírgula vinte e oito centímetros. [p=0.3] Por isso muita resposta vem {d}com o pi escrito: [p=0.2] dois pi serve para qualquer valor que a prova escolher."),
    # erro
    dict(id="s10", block="erro", text="Cuidado com o erro mais comum: {a}pôr o raio na tabela, no lugar da volta. [p=0.3] {b}Trezentos e sessenta graus para seis, [p=0.2] sessenta graus para xis. [p=0.2] Dá {c}xis igual a um. [p=0.3] Mas o raio não é a borda. [p=0.2] Ao lado dos trezentos e sessenta graus vai {d}o que a volta inteira mede: doze pi."),
    # atalho
    dict(id="s11", block="atalho", text="E o atalho prometido: {a}transforme o ângulo em fração da volta. [p=0.3] {b}Sessenta graus de trezentos e sessenta [p=0.2] é {c}um sexto da volta. [p=0.2] O arco é {d}um sexto de doze pi, que dá dois pi. [p=0.2] Sem cruz."),
    dict(id="s12", block="atalho", text="Guarde as frações que mais caem: [p=0.2] {a}noventa graus é um quarto da volta; [p=0.2] {b}cento e oitenta é metade; [p=0.2] {c}cento e vinte é um terço; [p=0.2] {d}quarenta e cinco é um oitavo."),
    dict(id="s13", block="atalho", text="Funciona porque ângulo e arco são proporcionais: [p=0.2] {a}o arco é a mesma fração da volta que o ângulo. [p=0.3] {b}Não compensa com ângulo quebrado, como cinquenta graus: [p=0.2] a fração vira {c}cinco trinta e seis avos. [p=0.2] Aí, {d}monte a tabela."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] O ponteiro dos minutos de um relógio mede {a}dez centímetros. [p=0.3] {b}Em vinte minutos, quantos centímetros a ponta dele percorre? [p=0.2] {c}Use pi igual a três."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] O ponteiro é o raio: [p=0.1] {a}a volta é duas vezes três vezes dez, que dá sessenta centímetros. [p=0.3] O ponteiro grande dá uma volta em {b}sessenta minutos. [p=0.2] Vinte minutos é {c}um terço da volta, [p=0.2] e trezentos e sessenta dividido por três dá cento e vinte graus."),
    dict(id="s17", block="resposta", text="{a}Um terço de sessenta centímetros dá vinte centímetros. [p=0.3] Pela tabela, sai o mesmo: [p=0.2] {b}trezentos e sessenta graus para sessenta centímetros; [p=0.2] {c}cento e vinte graus para xis. [p=0.2] {d}Trezentos e sessenta xis igual a cento e vinte vezes sessenta, que dá sete mil e duzentos. [p=0.2] Sete mil e duzentos dividido por trezentos e sessenta dá vinte. [p=0.2] Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}o arco é a mesma fração da volta que o ângulo central. [p=0.2] {b}Calcule a volta inteira [p=0.2] e {c}pegue a fração, ou monte a regra de três."),
    dict(id="s19", block="fim", text="Na próxima aula, o ângulo central ganha {a}um parceiro, com o vértice na própria circunferência: o ângulo inscrito. [p=0.2] E ele {b}vale a metade. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
