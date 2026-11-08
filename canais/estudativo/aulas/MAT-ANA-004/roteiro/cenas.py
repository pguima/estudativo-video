# Estudativo · MAT-ANA-004 — Equação da reta: reduzida, geral e segmentária (Matemática · Geometria Analítica · Equação da reta).
# Habilidade: escrever a reta de inclinação 2 que passa por (1, 3) como y = 2x + 1 e como 2x − y + 1 = 0 e ler os cortes nos eixos em x/3 + y/2 = 1.
# Pré-requisitos: MAT-ANA-003 (coeficiente angular m), MAT-FUN-012 (lei por um ponto na fórmula), MAT-EQU-011 (isolar uma letra). Próxima: MAT-ANA-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas: "eme" (m), "ene" (n), "xis", "ípsilon". Reduzida y = mx + n; o n faz o papel do b da função afim.
# Na tela: x/3 + y/2 = 1 e y − y₀ = m(x − x₀). Na voz, a segmentária é lida com "dividido por".

TITULO = "Equação da reta: reduzida, geral e segmentária"

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
    dict(id="s01", block="gancho", text="{a}Ípsilon igual a dois xis mais um. [p=0.3] {b}Dois xis menos ípsilon mais um igual a zero. [p=0.3] Parecem retas diferentes, [p=0.2] mas {c}são a mesma reta, escrita de dois jeitos. [p=0.3] E a prova pode usar {d}qualquer um deles."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você escreve a equação de uma reta, [p=0.2] passa de um jeito para o outro [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}o coeficiente angular, eme, que é delta ípsilon dividido por delta xis; [p=0.2] {c}achar a lei de uma reta trocando um ponto na fórmula; [p=0.2] e {d}isolar uma letra, fazendo o mesmo de cada lado. [p=0.3] Se faltar alguma, procure no canal."),
    # reduzida
    dict(id="s04", block="reduzida", text="O primeiro jeito é a {a}equação reduzida: [p=0.2] {b}ípsilon igual a eme xis mais ene. [p=0.3] {c}O eme é o coeficiente angular, a inclinação. [p=0.2] {d}O ene é onde a reta corta o eixo ípsilon: [p=0.2] o mesmo papel do bê na função afim, o valor inicial."),
    dict(id="s05", block="reduzida", text="Vamos achar a reta de {a}inclinação dois que passa por {b}xis um, ípsilon três. [p=0.3] Já dá para escrever {c}ípsilon igual a dois xis mais ene. [p=0.2] Troque o ponto na fórmula: [p=0.2] {d}três igual a dois vezes um, mais ene."),
    dict(id="s06", block="reduzida", text="{a}Três igual a dois mais ene. [p=0.2] {b}Tire dois de cada lado: [p=0.2] ene igual a um. [p=0.3] A reduzida é {c}ípsilon igual a dois xis mais um. [p=0.2] Ela mostra {d}a inclinação e o corte no eixo ípsilon, de olho."),
    # geral
    dict(id="s07", block="geral", text="O segundo jeito é a {a}equação geral: [p=0.2] {b}tudo de um lado, zero do outro. [p=0.3] Parta da reduzida e {c}tire ípsilon de cada lado: [p=0.2] {d}zero igual a dois xis menos ípsilon mais um. [p=0.2] Virando a igualdade, {e}dois xis menos ípsilon mais um igual a zero."),
    dict(id="s08", block="geral", text="Para que outro jeito? [p=0.2] Porque a geral escreve {a}qualquer reta, até a reta em pé. [p=0.3] {b}Xis menos três igual a zero é a reta vertical que passa no xis três. [p=0.2] Nela, o delta xis é zero, {c}não dá para dividir por zero [p=0.2] e {d}não existe eme nem reduzida."),
    # segmentária
    dict(id="s09", block="segmentaria", text="O terceiro jeito é a {a}equação segmentária: [p=0.2] {b}xis dividido por três, mais ípsilon dividido por dois, igual a um. [p=0.3] Ela entrega {c}os pontos onde a reta corta os eixos, sem conta."),
    dict(id="s10", block="segmentaria", text="{a}O número embaixo do xis é o corte no eixo xis: [p=0.2] {b}xis três, ípsilon zero. [p=0.2] {c}O número embaixo do ípsilon é o corte no eixo ípsilon: [p=0.2] {d}xis zero, ípsilon dois. [p=0.3] O motivo: no eixo xis, o ípsilon vale zero. [p=0.2] {e}Sobra xis dividido por três igual a um, [p=0.2] e o xis vale três."),
    # erro
    dict(id="s11", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}ler o eme direto na equação geral. [p=0.3] Pegue a reta da segmentária e multiplique tudo por seis, para sumir com as frações. [p=0.2] Na geral, ela fica {b}dois xis mais três ípsilon menos seis igual a zero. [p=0.2] Quem lê o número do xis diz que {c}o eme é dois, e que a reta sobe."),
    dict(id="s12", block="erro", text="Mas a reta vai de {a}xis zero, ípsilon dois, até xis três, ípsilon zero: [p=0.2] {b}ela desce. [p=0.3] Isole o ípsilon: {c}três ípsilon igual a menos dois xis mais seis. [p=0.2] Divida tudo por três: [p=0.2] {d}ípsilon igual a menos dois terços xis mais dois. [p=0.3] {e}Na geral, o eme só aparece depois de isolar o ípsilon."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, direto do ponto e da inclinação: [p=0.2] {a}ípsilon menos o ípsilon do ponto [p=0.2] igual a eme vezes, abre parênteses, xis menos o xis do ponto. [p=0.3] Com inclinação dois e o ponto xis um, ípsilon três: [p=0.2] {b}ípsilon menos três igual a dois vezes, abre parênteses, xis menos um."),
    dict(id="s14", block="atalho", text="{a}Abrindo o parêntese: ípsilon menos três igual a dois xis menos dois. [p=0.2] {b}Somando três de cada lado: ípsilon igual a dois xis mais um. [p=0.3] {c}A mesma reta, numa linha só."),
    dict(id="s15", block="atalho", text="Funciona porque, {a}entre o ponto dado e qualquer outro ponto da reta, [p=0.2] o delta ípsilon dividido pelo delta xis {b}tem de dar eme. [p=0.2] Multiplique cada lado pelo delta xis, e sai a fórmula do atalho. [p=0.3] {c}Não compensa quando o ponto já está no eixo ípsilon, como xis zero, ípsilon cinco: [p=0.2] aí, o ene é cinco, de olho."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar, em duas partes. [p=0.2] {a}Primeira: escreva a reduzida e a geral da reta de inclinação três [p=0.2] que passa por {b}xis um, ípsilon cinco. [p=0.3] {c}Segunda: onde a reta xis dividido por quatro, mais ípsilon dividido por cinco, igual a um, corta os eixos?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Ípsilon igual a três xis mais ene. [p=0.2] Troque o ponto: {b}cinco igual a três mais ene, [p=0.2] e o ene dá dois. [p=0.3] Reduzida: {c}ípsilon igual a três xis mais dois. [p=0.2] Tirando ípsilon de cada lado, a geral: {d}três xis menos ípsilon mais dois igual a zero."),
    dict(id="s19", block="resposta", text="Na segmentária, {a}o quatro embaixo do xis dá o corte em xis quatro, ípsilon zero. [p=0.2] {b}O cinco embaixo do ípsilon dá o corte em xis zero, ípsilon cinco."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a reduzida mostra a inclinação e o corte no eixo ípsilon, [p=0.2] {b}a geral serve para qualquer reta [p=0.2] e {c}a segmentária mostra os cortes nos eixos."),
    dict(id="s21", block="fim", text="Na próxima aula, você descobre {a}quando duas retas são paralelas [p=0.2] e {b}quando se cruzam em ângulo reto, [p=0.2] só olhando o eme. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
