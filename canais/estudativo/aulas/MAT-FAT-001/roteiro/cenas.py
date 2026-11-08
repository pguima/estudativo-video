# Estudativo · MAT-FAT-001 — Quadrado da soma e da diferença: (a ± b)² (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: abrir (x + 3)² e (x − 3)² sem multiplicar tudo, evitar o erro (a + b)² = a² + b² e calcular 101² de cabeça.
# Pré-requisitos: MAT-EQU-005 (chuveirinho, piso). Próxima: MAT-FAT-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula. Piso e chuveirinho como em MAT-EQU-005.
# (x + 3)² = x² + 6x + 9 (x = 10: 169; erro x² + 9 = 109) · (x − 3)² = x² − 6x + 9 (x = 10: 49) · (2x + 1)² = 4x² + 4x + 1 (441).
# Erro com números: (3 + 4)² = 49; 9 + 16 = 25; faltam 2·3·4 = 24. Atalho: 101² = 10.201; 99² = 9.801.
# Questão: (x − 5)² = x² − 10x + 25; 95² = 10.000 − 1.000 + 25 = 9.025.

TITULO = "Quadrado da soma e da diferença"

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
    dict(id="s01", block="gancho", text="{a}Abre parênteses, xis mais três, fecha parênteses, ao quadrado. [p=0.3] Se você escreveu {b}xis ao quadrado mais nove, [p=0.2] perdeu um pedaço no caminho. [p=0.3] Com xis igual a dez, o certo dá {c}cento e sessenta e nove. [p=0.2] A sua resposta dá {d}cento e nove."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você abre esse quadrado sem multiplicar tudo, [p=0.2] e ainda calcula {b}cento e um ao quadrado de cabeça."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas. [p=0.2] {b}Ao quadrado é o número vezes ele mesmo. [p=0.2] E {c}o chuveirinho: cada termo de um parêntese multiplica cada termo do outro. [p=0.3] Se faltar alguma, procure no canal."),
    # abrir pelo chuveirinho
    dict(id="s04", block="abrir", text="Xis mais três, ao quadrado, é {a}xis mais três, vezes xis mais três. [p=0.3] Pelo chuveirinho: {b}xis vezes xis, xis ao quadrado. [p=0.2] {c}Xis vezes três dá três xis. [p=0.2] {d}Três vezes xis, mais três xis. [p=0.2] {e}Três vezes três dá nove."),
    dict(id="s05", block="abrir", text="Juntando: {a}xis ao quadrado mais seis xis mais nove. [p=0.3] O seis xis é o pedaço que sumiu no gancho. [p=0.2] E repare: ele veio {b}de dois termos iguais, três xis e mais três xis."),
    # piso
    dict(id="s06", block="piso", text="No piso, isso aparece na hora. [p=0.2] Um piso quadrado de lado {a}xis mais três [p=0.2] tem {b}um quadrado grande, xis ao quadrado, [p=0.2] {c}um quadradinho de três por três, nove, [p=0.2] e {d}duas faixas iguais, de três xis cada."),
    # regra
    dict(id="s07", block="regra", text="Essa conta aparece tanto que ganhou nome: {a}produto notável. [p=0.2] É o {b}quadrado da soma: [p=0.2] {c}o quadrado do primeiro termo, [p=0.2] {d}mais duas vezes o primeiro vezes o segundo, [p=0.2] {e}mais o quadrado do segundo. [p=0.3] Na tela, {f}a letra a é o primeiro termo, e a letra bê é o segundo."),
    # diferença
    dict(id="s08", block="diferenca", text="E com menos? [p=0.2] {a}Abre parênteses, xis menos três, fecha parênteses, ao quadrado. [p=0.3] {b}O quadrado do primeiro: xis ao quadrado. [p=0.2] {c}Duas vezes xis vezes menos três: menos seis xis. [p=0.2] {d}O quadrado de menos três: mais nove, porque sinais iguais dão mais. [p=0.3] Resultado: {e}xis ao quadrado menos seis xis mais nove."),
    dict(id="s09", block="diferenca", text="Esse é o {a}quadrado da diferença. [p=0.2] {b}Só o termo do meio fica com menos. [p=0.2] O último é sempre mais. [p=0.3] Teste com dez: [p=0.2] {c}dez menos três dá sete, e sete ao quadrado dá quarenta e nove. [p=0.2] {d}Cem menos sessenta mais nove também dá quarenta e nove."),
    # número na frente do xis
    dict(id="s10", block="frente", text="A regra vale até com número na frente do xis, [p=0.2] onde o atalho da aula do chuveirinho não serve. [p=0.2] {a}Abre parênteses, dois xis mais um, fecha parênteses, ao quadrado. [p=0.3] {b}Dois xis vezes dois xis: quatro xis ao quadrado. [p=0.2] {c}Duas vezes dois xis vezes um: quatro xis. [p=0.2] {d}Um ao quadrado: um. [p=0.3] Fica {e}quatro xis ao quadrado mais quatro xis mais um."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é o do gancho: [p=0.2] {a}elevar cada termo ao quadrado e somar. [p=0.3] Veja com números. [p=0.2] {b}Três mais quatro dá sete, e sete ao quadrado dá quarenta e nove. [p=0.2] Elevando cada um, daria {c}nove mais dezesseis: vinte e cinco. [p=0.3] {d}Faltaram as duas faixas do meio: duas vezes três vezes quatro, vinte e quatro."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}cento e um ao quadrado, de cabeça. [p=0.2] Cento e um é {b}cem mais um. [p=0.3] {c}Cem ao quadrado, dez mil. [p=0.2] {d}Duas vezes cem vezes um, duzentos. [p=0.2] {e}Um ao quadrado, um. [p=0.3] Total: {f}dez mil duzentos e um."),
    dict(id="s13", block="atalho", text="Com menos, também. [p=0.2] {a}Noventa e nove é cem menos um. [p=0.2] {b}Dez mil menos duzentos mais um: [p=0.2] {c}nove mil oitocentos e um."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o número redondo é fácil de elevar ao quadrado, [p=0.2] e o resto é conta pequena. [p=0.3] {b}Compensa quando o número está a poucos passos de um redondo, como noventa e cinco, a cinco passos do cem. [p=0.2] {c}Longe disso, a conta do meio pesa, e a conta armada é mais segura."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Escreva sem parênteses: {a}abre parênteses, xis menos cinco, fecha parênteses, ao quadrado. [p=0.3] Depois, use o resultado para calcular {b}noventa e cinco ao quadrado de cabeça."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}O quadrado do primeiro: xis ao quadrado. [p=0.2] {b}Duas vezes xis vezes menos cinco: menos dez xis. [p=0.2] {c}Menos cinco ao quadrado: mais vinte e cinco. [p=0.3] Resposta: {d}xis ao quadrado menos dez xis mais vinte e cinco."),
    dict(id="s18", block="resposta", text="Noventa e cinco é {a}cem menos cinco: o xis vale cem. [p=0.2] {b}Dez mil menos mil mais vinte e cinco: [p=0.2] {c}nove mil e vinte e cinco."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}quadrado do primeiro, [p=0.2] {b}duas vezes o primeiro vezes o segundo, [p=0.2] {c}quadrado do segundo. [p=0.3] {d}O termo do meio nunca some."),
    dict(id="s20", block="fim", text="Na próxima aula, você multiplica {a}a soma pela diferença, [p=0.2] como xis mais cinco, vezes xis menos cinco, [p=0.2] e abre {b}o cubo de uma soma. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
