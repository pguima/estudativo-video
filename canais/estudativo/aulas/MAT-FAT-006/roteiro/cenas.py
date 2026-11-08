# Estudativo · MAT-FAT-006 — Praticando: produtos notáveis e fatoração (Matemática · Fatoração e Equação do 2º Grau · prática).
# Habilidade: abrir produtos notáveis, fatorar expressões, simplificar frações algébricas antes de fazer a conta e racionalizar denominadores.
# Pré-requisitos: MAT-FAT-001, MAT-FAT-015, MAT-FAT-002, MAT-FAT-003, MAT-FAT-004, MAT-FAT-005. Próxima: MAT-FAT-007.
# Questões inéditas, criadas para esta aula. Equação do 2º grau ainda não foi ensinada (MAT-FAT-007).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".

TITULO = "Praticando: produtos notáveis e fatoração"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões criadas para esta aula, [p=0.2] uma para cada ferramenta desta parte do curso. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}os produtos notáveis, [p=0.2] {b}colocar em evidência, [p=0.2] {c}simplificar frações com letra [p=0.2] e {d}racionalizar. [p=0.3] Para conferir, {e}o teste com dez: troque o xis por dez antes e depois. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: abrir
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] Escreva sem parênteses: {b}abre parênteses, dois xis menos três, fecha parênteses, ao quadrado, [p=0.2] sem multiplicar tudo."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}O quadrado do primeiro: dois xis vezes dois xis dá quatro xis ao quadrado. [p=0.2] {b}Duas vezes o primeiro vezes o segundo: duas vezes dois xis vezes menos três, menos doze xis. [p=0.2] {c}O quadrado do segundo: mais nove. [p=0.3] Resposta: {d}quatro xis ao quadrado menos doze xis mais nove."),
    dict(id="s06", block="resposta1", text="Teste com dez: [p=0.2] {a}vinte menos três dá dezessete, e dezessete ao quadrado dá duzentos e oitenta e nove. [p=0.2] {b}Quatrocentos menos cento e vinte mais nove também. [p=0.2] Bateu. [p=0.3] Quem escreveu {c}dois xis ao quadrado no começo esqueceu de elevar o dois: [p=0.2] {d}o quadrado vale para o termo inteiro, número e letra."),
    # questão 2: fatorar
    dict(id="s07", block="questao2", text="{a}Questão dois. [p=0.2] Fatore até o fim: {b}xis ao cubo menos quatro xis."),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Antes de tudo, {a}o fator comum: o xis está nos dois termos. [p=0.2] Fica {b}xis, abre parênteses, xis ao quadrado menos quatro, fecha parênteses. [p=0.3] Dentro, uma {c}diferença de dois quadrados: quatro é o quadrado de dois. [p=0.2] Resposta: {d}xis, vezes o parêntese xis mais dois, vezes o parêntese xis menos dois."),
    dict(id="s10", block="resposta2", text="Teste com dez: [p=0.2] {a}mil menos quarenta dá novecentos e sessenta. [p=0.2] {b}Dez vezes doze vezes oito também. [p=0.3] Quem parou com o xis em evidência {c}não errou, mas não terminou: [p=0.2] a questão pedia até o fim."),
    # questão 3: simplificar antes da conta
    dict(id="s11", block="questao3", text="{a}Questão três. [p=0.2] Calcule {b}xis ao quadrado mais dez xis mais vinte e cinco, dividido por xis mais cinco, [p=0.2] para {c}xis igual a noventa e cinco."),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Trocar o xis direto obriga a calcular {a}noventa e cinco ao quadrado logo de cara. [p=0.3] Simplifique antes. [p=0.2] Em cima, {b}o primeiro é o quadrado de xis, o último é o quadrado de cinco, [p=0.2] e {c}duas vezes xis vezes cinco dá dez xis: o meio bate. [p=0.2] É {d}xis mais cinco, ao quadrado."),
    dict(id="s14", block="resposta3", text="{a}Corte um xis mais cinco em cima e embaixo. [p=0.2] Sobra {b}xis mais cinco, para xis diferente de menos cinco. [p=0.3] Com noventa e cinco: {c}cem. [p=0.2] Sem calculadora e sem conta armada."),
    # atalho
    dict(id="s15", block="atalho", text="Esse é o atalho desta prática: {a}simplifique antes de trocar o xis. [p=0.3] Funciona porque {b}a fração simplificada vale o mesmo em todo valor permitido do xis, [p=0.2] e a conta encolhe. [p=0.3] {c}Não compensa quando nada se corta: [p=0.2] aí, troque o xis direto."),
    # questão 4: racionalizar
    dict(id="s16", block="questao4", text="{a}Questão quatro. [p=0.2] Racionalize {b}seis dividido por, abre parênteses, raiz de cinco menos raiz de dois, fecha parênteses."),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] Tem subtração embaixo, então entra {a}o conjugado: raiz de cinco mais raiz de dois. [p=0.3] Embaixo, pelo atalho da racionalização: {b}cinco menos dois dá três. [p=0.2] Em cima: {c}seis, abre parênteses, raiz de cinco mais raiz de dois, fecha parênteses."),
    dict(id="s19", block="resposta4", text="{a}Divida em cima e embaixo por três. [p=0.2] Resposta: {b}dois, abre parênteses, raiz de cinco mais raiz de dois, fecha parênteses, [p=0.2] ou {c}dois raiz de cinco mais dois raiz de dois. [p=0.3] Quem multiplicou {d}só embaixo mudou o valor da fração: [p=0.2] o de cima tem que acompanhar."),
    # questão 5: cálculo de cabeça
    dict(id="s20", block="questao5", text="{a}Última questão. [p=0.2] Calcule de cabeça {b}mil e dois vezes novecentos e noventa e oito."),
    dict(id="s21", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta5", text="Os números estão {a}à mesma distância de mil: [p=0.2] {b}mil mais dois, vezes mil menos dois. [p=0.3] É soma vezes diferença: {c}mil ao quadrado menos dois ao quadrado. [p=0.2] {d}Um milhão menos quatro: [p=0.2] {e}novecentos e noventa e nove mil novecentos e noventa e seis."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}abra com o produto notável certo, [p=0.2] {b}procure fator comum antes de tudo [p=0.2] e {c}simplifique antes de fazer a conta."),
    dict(id="s24", block="fim", text="Na próxima aula, a fatoração vira ferramenta para resolver {a}equações do segundo grau, [p=0.2] como {b}xis ao quadrado menos quarenta e nove igual a zero [p=0.2] e {c}xis ao quadrado menos cinco xis igual a zero. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
