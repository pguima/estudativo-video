# Estudativo · MAT-FUN-009 — Função afim: lei e gráfico (Matemática · Funções · Função afim).
# Habilidade: escrever a lei de um táxi de R$ 5 mais R$ 2,50 por km e traçar a reta de f(x) = 2x − 1 com dois pontos.
# Pré-requisitos: MAT-FUN-006 (gráfico de uma função). Próxima: MAT-FUN-010.
# Questão inédita, criada para esta aula. Letras narradas: "á", "bê", "xis", "ípsilon". Domínio ainda não está na ficha: não usar o termo.
# Táxi: 0 km → 5 · 1 km → 7,50 · 2 km → 10 · 3 km → 12,50 · 6 km → 20 · lei P = 5 + 2,5d, ou f(x) = 2,5x + 5 (a = 2,5, b = 5).
# Erro: trocar os números, 5d + 2,5 → 6 km daria 32,50 em vez de 20.
# Reta de f(x) = 2x − 1: (0, −1) e (2, 3); conferência (1, 1).
# Questão: encanador, R$ 40 a visita mais R$ 30 por hora · f(x) = 30x + 40 · f(3) = 130 · pontos (0, 40) e (1, 70).
# Visual: tabela do táxi com "+2,50" entre as linhas; fórmula f(x) = ax + b com á e bê destacados; plano (E.plano) com os pontos
#   do táxi alinhados (E.ponto) e a reta (E.reta_pontos); plano com (0, −1), (2, 3) e a reta, depois (1, 1) acendendo em cima dela.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Função afim: lei e gráfico"

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
    dict(id="s01", block="gancho", text="{a}Para desenhar o gráfico de uma função, você monta uma tabela com vários pontos. [p=0.3] Mas existe um tipo de função em que {b}dois pontos bastam. [p=0.3] Ela aparece em {c}táxi, conta de luz, salário com comissão. [p=0.2] É a {d}função afim."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você escreve a lei de uma função afim, [p=0.2] {b}traça a reta dela com dois pontos [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}o gráfico de uma função. [p=0.2] Você escolhe o xis, calcula o ípsilon e marca o ponto. [p=0.3] Se faltar, procure no canal."),
    # táxi
    dict(id="s04", block="taxi", text="Volte ao táxi do começo da trilha. [p=0.2] Ele cobra {a}cinco reais só para começar a corrida: [p=0.2] a parte fixa, que se chama {b}bandeirada. [p=0.2] E mais {c}dois reais e cinquenta centavos por quilômetro rodado."),
    dict(id="s05", block="taxi", text="Monte a tabela. [p=0.2] {a}Zero quilômetro: cinco reais, só a bandeirada. [p=0.2] {b}Um quilômetro: sete e cinquenta. [p=0.2] {c}Dois quilômetros: dez reais. [p=0.2] {d}Três quilômetros: doze e cinquenta. [p=0.3] A cada quilômetro, o preço {e}sobe sempre o mesmo valor: dois e cinquenta."),
    dict(id="s06", block="taxi", text="A lei é a fórmula que junta tudo, e você já a conhece. [p=0.2] O preço é {a}a bandeirada de cinco reais, [p=0.2] {b}mais dois vírgula cinco vezes a distância. [p=0.3] {c}Pê igual a cinco mais dois vírgula cinco vezes dê, [p=0.2] em que {d}dê é a distância em quilômetros e pê é o preço em reais. [p=0.3] Para seis quilômetros: {e}dois vírgula cinco vezes seis dá quinze. [p=0.2] {f}Somando a bandeirada: vinte reais."),
    # função afim
    dict(id="s07", block="afim", text="Toda função com essa forma se chama {a}função afim: [p=0.2] {b}efe de xis igual a á xis mais bê. [p=0.3] {c}O á é o número que multiplica o xis. [p=0.2] {d}O bê é o número sozinho. [p=0.3] No táxi, o dê faz o papel do xis: [p=0.2] {e}á vale dois vírgula cinco e bê vale cinco. [p=0.2] O que cada um significa no gráfico é o assunto da próxima aula."),
    dict(id="s08", block="afim", text="Outro exemplo: {a}efe de xis igual a dois xis menos um. [p=0.2] Aqui, {b}á vale dois e bê vale menos um. [p=0.3] O bê leva junto {c}o sinal que está na frente dele."),
    # gráfico
    dict(id="s09", block="grafico", text="E o gráfico? [p=0.2] Marque os pontos do táxi no plano. [p=0.3] Como o preço sobe sempre o mesmo tanto a cada passo, [p=0.2] {a}os pontos ficam alinhados. [p=0.3] {b}O gráfico de uma função afim é sempre uma reta."),
    dict(id="s10", block="grafico", text="E para traçar uma reta, {a}dois pontos bastam: [p=0.2] por dois pontos passa {b}uma reta só. [p=0.3] É o que você faz com uma régua: [p=0.2] encosta nos dois pontos e risca."),
    dict(id="s11", block="grafico", text="Vamos traçar {a}efe de xis igual a dois xis menos um. [p=0.3] {b}Xis zero: dois vezes zero dá zero. [p=0.2] Tirando um, dá menos um. [p=0.2] Ponto {c}xis zero, ípsilon menos um. [p=0.3] {d}Xis dois: dois vezes dois dá quatro. [p=0.2] Tirando um, dá três. [p=0.2] Ponto {e}xis dois, ípsilon três. [p=0.3] {f}Ligue esses pontos e prolongue para os lados."),
    dict(id="s12", block="grafico", text="Quer conferir? [p=0.2] Calcule um terceiro ponto. [p=0.2] {a}Xis um: dois vezes um dá dois. [p=0.2] Tirando um, dá um. [p=0.3] {b}O ponto xis um, ípsilon um, cai em cima da reta. [p=0.2] Se tivesse caído fora, {c}alguma conta estaria errada."),
    # erro
    dict(id="s13", block="erro", text="Agora, cuidado com um erro muito comum: [p=0.2] {a}trocar os números de lugar. [p=0.2] A pessoa escreve {b}cinco vezes dê, mais dois vírgula cinco. [p=0.3] Para seis quilômetros, daria {c}trinta e dois e cinquenta, [p=0.2] e não vinte reais. [p=0.3] {d}Quem multiplica a distância é o que se paga por quilômetro. [p=0.2] {e}O valor fixo fica sozinho."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}o ponto do xis zero sai de graça. [p=0.3] Com xis zero, {b}o á vezes zero dá zero, e sobra só o bê. [p=0.2] Em dois xis menos um, {c}o ponto é xis zero, ípsilon menos um, sem conta nenhuma. [p=0.3] Para o segundo ponto, {d}escolha um xis que deixe a conta fácil."),
    dict(id="s15", block="atalho", text="{a}Não compensa quando o desenho só mostra xis longe do zero, [p=0.2] como de cinquenta a cem. [p=0.2] Aí o ponto do xis zero {b}nem cabe na tela. [p=0.2] Escolha {c}dois xis que apareçam no desenho."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um encanador cobra {a}quarenta reais pela visita, [p=0.1] mais {b}trinta reais por hora de trabalho. [p=0.3] {c}Escreva a lei do preço. [p=0.2] {d}Quanto custa um serviço de três horas? [p=0.2] E {e}que dois pontos você usaria para traçar a reta?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] O que multiplica as horas é {a}o valor por hora, trinta. [p=0.2] O valor fixo é {b}a visita, quarenta. [p=0.3] Lei: {c}efe de xis igual a trinta xis mais quarenta, [p=0.2] com {d}xis em horas e o preço em reais."),
    dict(id="s19", block="resposta", text="Três horas: {a}trinta vezes três dá noventa. [p=0.2] {b}Somando a visita: cento e trinta reais. [p=0.3] Para a reta, {c}o ponto de graça: xis zero, ípsilon quarenta. [p=0.2] E um fácil: {d}xis um, ípsilon setenta. [p=0.2] O ponto {e}xis três, ípsilon cento e trinta serve de conferência."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}função afim é á xis mais bê, [p=0.2] {b}o gráfico é uma reta [p=0.2] e {c}dois pontos bastam para traçá-la."),
    dict(id="s21", block="fim", text="Na próxima aula, você descobre {a}o que o á e o bê contam: [p=0.2] {b}de onde a reta parte [p=0.2] e {c}quanto ela sobe ou desce a cada passo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
