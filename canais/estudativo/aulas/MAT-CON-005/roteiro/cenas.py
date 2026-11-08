# Estudativo · MAT-CON-005 — Fração geratriz de uma dízima (Matemática · Conjuntos · Conjuntos numéricos).
# Habilidade: transformar 0,444… em 4/9, 0,1212… em 4/33 e 0,2333… em 7/30, pela equação com x e pelo macete dos noves.
# Pré-requisitos: MAT-CON-004 (racionais), MAT-EQU-010 (multiplicar tudo por 10 ou 100). Próxima: MAT-CON-006.
# Questão inédita, criada para esta aula.
# Contas: x = 0,444…; 10x = 4,444…; 9x = 4; x = 4/9 · x = 0,1212…; 100x = 12,1212…; 99x = 12; 12/99 = 4/33 ·
#   x = 0,2333…; 10x = 2,333…; 100x = 23,333…; 90x = 21; 21/90 = 7/30 · gancho: 4/10 = 0,4 e 44/100 = 0,44.
# Erro: 0,1212… vezes 10 = 1,2121…: as partes depois da vírgula (2121… e 1212…) não batem.
# Macete: período sobre noves; com algarismo antes: (23 − 2)/90. Não compensa: 23/99 = 0,2323… (outro número).
# Questão: 0,777… = 7/9 · 0,1666… = (16 − 1)/90 = 15/90 = 1/6; 1 ÷ 6 = 0,1666…
# Visual: as equações empilhadas, com as caudas "…" alinhadas e riscadas na subtração.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Fração geratriz: a fração de uma dízima"

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
    dict(id="s01", block="gancho", text="{a}Zero vírgula quatro quatro quatro, sem fim. [p=0.3] Que fração é essa? [p=0.2] Não é quatro décimos, [p=0.2] nem quarenta e quatro centésimos. [p=0.3] É {b}quatro nonos. [p=0.2] E dá para descobrir isso {c}em segundos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você transforma qualquer dízima em fração, [p=0.2] com uma equação e com um {b}macete de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}dízima é racional, porque nasce de uma fração, [p=0.2] e {c}multiplicar uma equação inteira por dez ou por cem, [p=0.2] fazendo a vírgula andar. [p=0.3] Se faltar alguma, procure no canal."),
    # equação: um algarismo
    dict(id="s04", block="equacao", text="A fração que gera uma dízima se chama {a}fração geratriz. [p=0.3] Para achar, dê um nome à dízima: [p=0.2] {b}xis igual a zero vírgula quatro quatro quatro, sem fim."),
    dict(id="s05", block="equacao", text="{a}Multiplique os dois lados por dez. [p=0.2] A vírgula anda uma casa: [p=0.2] {b}dez xis igual a quatro vírgula quatro quatro quatro. [p=0.3] Repare: {c}depois da vírgula, a cauda é idêntica à do xis."),
    dict(id="s06", block="equacao", text="Em seguida, {a}tire xis dos dois lados. [p=0.2] À esquerda, {b}dez xis menos xis dá nove xis. [p=0.3] À direita, tirar xis é tirar {c}zero vírgula quatro quatro quatro. [p=0.2] A cauda some, e {d}sobra quatro."),
    dict(id="s07", block="equacao", text="{a}Nove xis igual a quatro. [p=0.2] {b}Divida por nove: xis igual a quatro nonos. [p=0.3] Confira: {c}quatro dividido por nove dá zero vírgula quatro quatro quatro."),
    # dois algarismos
    dict(id="s08", block="dois", text="Veja {a}zero vírgula um dois um dois. [p=0.2] O período tem {b}dois algarismos, [p=0.2] então multiplique por {c}cem, para a vírgula andar duas casas: [p=0.2] {d}cem xis igual a doze vírgula um dois um dois."),
    dict(id="s09", block="dois", text="Tire xis dos dois lados: [p=0.2] {a}noventa e nove xis igual a doze. [p=0.2] {b}Xis igual a doze noventa e nove avos. [p=0.3] Doze e noventa e nove se dividem por três: {c}quatro trinta e três avos."),
    # algarismo antes do período
    dict(id="s10", block="antes", text="E quando tem algarismo {a}antes do período? [p=0.2] Veja {b}zero vírgula dois três três três. [p=0.3] O dois aparece uma vez só. [p=0.2] O período é {c}o três."),
    dict(id="s11", block="antes", text="Faça a vírgula andar até {a}logo antes do período: [p=0.2] {b}dez xis igual a dois vírgula três três três. [p=0.3] Depois, até {c}o fim do primeiro período: [p=0.2] {d}cem xis igual a vinte e três vírgula três três três. [p=0.3] {e}As caudas agora são iguais."),
    dict(id="s12", block="antes", text="Na equação do cem, {a}tire dez xis dos dois lados. [p=0.2] À esquerda, {b}noventa xis. [p=0.2] À direita, tire o valor de dez xis, que é dois vírgula três três três: [p=0.2] {c}sobra vinte e um. [p=0.3] {d}Xis igual a vinte e um noventa avos. [p=0.2] Divida por três: {e}sete trinta avos."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}multiplicar por dez quando o período tem dois algarismos. [p=0.3] Zero vírgula um dois um dois, vezes dez, [p=0.2] dá {b}um vírgula dois um dois um. [p=0.3] Compare as caudas: {c}dois um dois um contra um dois um dois. [p=0.2] {d}Não batem, e nada some. [p=0.3] {e}Ande com a vírgula um período inteiro."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o macete dos noves. [p=0.2] {a}Em cima, o período. [p=0.2] {b}Embaixo, um nove para cada algarismo do período. [p=0.3] {c}Quatro nonos. [p=0.2] {d}Doze noventa e nove avos. [p=0.2] O mesmo que a equação deu."),
    dict(id="s15", block="atalho", text="Funciona porque a equação {a}sempre deixa noves: [p=0.2] dez xis menos xis dá {b}nove xis. [p=0.2] Cem xis menos xis dá {c}noventa e nove xis."),
    dict(id="s16", block="atalho", text="Com algarismo antes do período, o macete muda. [p=0.2] {a}Em cima: tudo até o fim do primeiro período, menos o que não se repete. [p=0.2] {b}Vinte e três menos dois dá vinte e um. [p=0.3] {c}Embaixo: um nove para o período, e um zero para o algarismo antes dele. [p=0.2] {d}Noventa. [p=0.2] De novo, {e}sete trinta avos."),
    dict(id="s17", block="atalho", text="Não compensa usar o macete simples nesse caso. [p=0.2] Ele daria {a}vinte e três noventa e nove avos, [p=0.2] que é {b}zero vírgula dois três dois três: outro número. [p=0.3] Se não lembrar a versão com zero, {c}a equação nunca falha."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Ache a fração geratriz, na forma mais simples, [p=0.2] de {a}zero vírgula sete sete sete [p=0.2] e de {b}zero vírgula um seis seis seis."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Na primeira, o período é sete, de um algarismo: {a}sete nonos. [p=0.3] Na segunda, o um fica {b}antes do período, que é o seis. [p=0.2] {c}Em cima: dezesseis menos um dá quinze. [p=0.2] {d}Embaixo: noventa."),
    dict(id="s21", block="resposta", text="{a}Quinze noventa avos. [p=0.2] Divida em cima e embaixo por quinze: {b}um sexto. [p=0.3] Confira: {c}um dividido por seis dá zero vírgula um seis seis seis. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}ande com a vírgula até as caudas ficarem iguais [p=0.2] e {b}subtraia para a cauda sumir. [p=0.3] Com prática, {c}os noves dão a resposta direto."),
    dict(id="s23", block="fim", text="Toda dízima com período vira fração. [p=0.2] Na próxima aula, você conhece os decimais que {a}não acabam e não se repetem, [p=0.2] como {b}a raiz de sete e o pi. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
