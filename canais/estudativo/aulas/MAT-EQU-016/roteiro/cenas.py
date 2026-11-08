# Estudativo · MAT-EQU-016 — Inequação dupla e inequação em problemas (Matemática · Equações do 1º Grau).
# Habilidade: resolver −1 < 2x + 3 ≤ 9 e descobrir a partir de quantos minutos um plano fica mais barato.
# Pré-requisitos: MAT-EQU-014 (comparar dois planos), MAT-EQU-015 (inequação e reta). Próxima: MAT-EQU-017.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Planos novos (não os da MAT-EQU-014), com valores inventados. Cobrança por minuto inteiro: resposta em minutos inteiros (71).
# Questão inédita, criada para esta aula.

TITULO = "Inequação dupla e inequação em problemas"

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
    dict(id="s01", block="gancho", text="Dois planos empatam com {a}setenta minutos, [p=0.2] e a conta só vem com minuto inteiro. [p=0.3] A partir de quantos minutos o plano de minuto mais barato passa a ganhar? [p=0.3] Quem responde {b}setenta erra. [p=0.2] No setenta, eles {c}ainda custam o mesmo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve inequação com duas condições ao mesmo tempo, [p=0.2] responde {b}a partir de quantos [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}achar com quantos minutos dois planos custam o mesmo, [p=0.2] e {c}resolver inequação, virando o sinal quando multiplica ou divide por negativo. [p=0.3] Se faltar alguma, procure no canal."),
    # dupla
    dict(id="s04", block="dupla", text="Primeiro, a inequação dupla. [p=0.2] Leia com calma: [p=0.2] {a}menos um menor que dois xis mais três, [p=0.2] menor ou igual a nove."),
    dict(id="s05", block="dupla", text="Ela faz {a}duas exigências de uma vez. [p=0.2] {b}Dois xis mais três tem que ser maior que menos um. [p=0.2] E, ao mesmo tempo, {c}tem que ser menor ou igual a nove. [p=0.3] Ou seja, {d}a conta do meio fica presa entre menos um e nove."),
    dict(id="s06", block="dupla", text="A balança continua valendo, [p=0.2] só que agora com {a}três partes. [p=0.2] O que você faz numa, {b}faz nas três. [p=0.3] {c}Tire três de cada parte: [p=0.2] {d}menos quatro menor que dois xis, menor ou igual a seis."),
    dict(id="s07", block="dupla", text="{a}Divida as três partes por dois. [p=0.2] Dois é positivo, então {b}nada vira: [p=0.2] {c}menos dois menor que xis, menor ou igual a três."),
    dict(id="s08", block="dupla", text="Na reta, {a}o menos dois fica de fora: bolinha aberta. [p=0.2] {b}O três entra, por causa do igual: bolinha fechada. [p=0.3] E você pinta {c}só o pedaço entre as bolinhas."),
    dict(id="s09", block="dupla", text="Conferindo a ponta fechada: [p=0.2] {a}dois vezes três mais três dá nove, [p=0.2] e nove é menor ou igual a nove. [p=0.2] {b}Serve."),
    # problema
    dict(id="s10", block="planos", text="Agora o problema, com valores inventados para a aula. [p=0.2] {a}O plano A cobra trinta e cinco reais por mês, [p=0.2] mais trinta centavos por minuto. [p=0.3] {b}O plano B não tem mensalidade: [p=0.2] cobra oitenta centavos por minuto. [p=0.3] {c}Em A e em B, a conta do mês sempre vem com um número inteiro de minutos. [p=0.2] {d}A partir de quantos minutos na conta o plano A fica mais barato?"),
    dict(id="s11", block="planos", text="{a}Os minutos viram xis. [p=0.2] {b}Mais barato quer dizer menor. [p=0.2] Então {c}a conta de A tem que ser menor que a conta de B: [p=0.3] {d}trinta e cinco mais zero vírgula três xis, menor que zero vírgula oito xis."),
    dict(id="s12", block="planos", text="{a}Tire zero vírgula três xis de cada lado: [p=0.2] {b}trinta e cinco menor que zero vírgula cinco xis. [p=0.3] {c}Divida por zero vírgula cinco, que é positivo. [p=0.2] Dividir por meio é dobrar: [p=0.2] {d}setenta menor que xis. [p=0.2] Ou seja, {e}xis maior que setenta."),
    dict(id="s13", block="planos", text="O minuto é inteiro, [p=0.2] e o primeiro número inteiro maior que setenta é {a}setenta e um. [p=0.3] A resposta: {b}a partir de setenta e um minutos."),
    dict(id="s14", block="planos", text="Conferindo, {a}com setenta minutos, A e B dão cinquenta e seis reais. [p=0.3] {b}Com setenta e um, A dá cinquenta e seis reais e trinta centavos. [p=0.2] {c}B dá cinquenta e seis reais e oitenta centavos. [p=0.2] {d}A ficou mais barato."),
    # erro
    dict(id="s15", block="erro", text="Por isso, cuidado com o erro do começo: [p=0.2] {a}responder o empate. [p=0.3] Setenta é onde os preços {b}são iguais. [p=0.2] Mais barato {c}começa no minuto seguinte. [p=0.3] Releia a pergunta: [p=0.2] {d}igual, menor ou menor ou igual?"),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho prometido: [p=0.2] {a}ache o empate e depois escolha o lado. [p=0.3] {b}A diferença das mensalidades é trinta e cinco reais. [p=0.2] A do minuto é cinquenta centavos. [p=0.2] {c}Trinta e cinco dividido por zero vírgula cinco dá setenta. [p=0.3] Depois do empate, ganha sempre {d}o plano de minuto mais barato."),
    dict(id="s17", block="atalho", text="Funciona porque {a}os preços só trocam de posição no empate. [p=0.3] {b}Não compensa quando o minuto custa o mesmo nos planos: [p=0.2] aí não existe empate, [p=0.2] e quem tem a mensalidade menor ganha sempre. [p=0.2] Na dúvida, {c}monte a inequação."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar, com valores inventados. [p=0.2] Um estacionamento cobra {a}oito reais de entrada [p=0.2] mais {b}três reais por hora, [p=0.2] e {c}hora começada é cobrada como hora inteira. [p=0.3] Você tem {d}trinta reais. [p=0.2] {e}Por quantas horas, no máximo, pode deixar o carro?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}As horas viram xis. [p=0.2] O gasto tem que caber nos trinta: [p=0.2] {b}oito mais três xis, menor ou igual a trinta. [p=0.3] {c}Tire oito de cada lado: [p=0.2] {d}três xis menor ou igual a vinte e dois. [p=0.2] {e}Divida por três: [p=0.2] {f}xis menor ou igual a vinte e dois terços. [p=0.2] Como três vezes sete dá vinte e um, [p=0.1] isso é um pouco mais que sete."),
    dict(id="s21", block="resposta", text="Aqui o arredondamento é {a}para baixo. [p=0.2] Com oito horas, a conta é {b}oito mais vinte e quatro dá trinta e dois: [p=0.2] passa dos trinta. [p=0.3] Resposta: {c}sete horas. [p=0.2] Conferindo: {d}oito mais vinte e um dá vinte e nove reais. [p=0.2] {e}Cabe."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}na inequação dupla, faça o mesmo nas três partes. [p=0.2] {b}No problema, a pergunta decide o sinal [p=0.2] e {c}a unidade decide o arredondamento."),
    dict(id="s23", block="fim", text="Na próxima aula, é {a}hora de praticar: [p=0.2] {b}problemas de equação e de inequação, [p=0.2] do texto até a resposta com a unidade certa. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
