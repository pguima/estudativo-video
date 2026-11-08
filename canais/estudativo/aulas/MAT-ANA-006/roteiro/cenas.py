# Estudativo · MAT-ANA-006 — Ponto de encontro de duas retas (Matemática · Geometria Analítica · Equação da reta).
# Habilidade: achar onde y = 2x + 1 e y = −x + 4 se cruzam, em (1, 3), resolvendo um sistema.
# Pré-requisitos: MAT-ANA-004 (equação reduzida e geral), MAT-EQU-018 (sistema por substituição). Próxima: MAT-ANA-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas: "eme" (m), "ene" (n), "xis", "ípsilon".
# MAT-ANA-005 (paralelas) não está em "Já ensinado" desta ficha: o caso das paralelas é explicado na hora, pela inclinação.

TITULO = "Ponto de encontro de duas retas"

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
    dict(id="s01", block="gancho", text="Duas retas no plano: [p=0.2] {a}ípsilon igual a dois xis mais um [p=0.2] e {b}ípsilon igual a menos xis mais quatro. [p=0.3] {c}Em que ponto exato elas se cruzam? [p=0.3] O desenho dá {d}um palpite. [p=0.2] A conta dá {e}a certeza."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o ponto de encontro de duas retas [p=0.2] e sabe, antes da conta, {b}se esse ponto existe."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a equação reduzida da reta, ípsilon igual a eme xis mais ene; [p=0.2] e {c}o sistema por substituição: deixar uma letra sozinha e trocar na outra equação. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="O ponto de encontro está {a}nas duas retas ao mesmo tempo. [p=0.2] Então, as coordenadas dele {b}valem nas duas equações. [p=0.3] Duas equações que precisam valer juntas [p=0.2] formam {c}um sistema."),
    # resolver
    dict(id="s05", block="resolver", text="Aqui, {a}o ípsilon já está sozinho nas duas. [p=0.2] Troque o ípsilon da segunda pelo que ele vale na primeira: [p=0.2] {b}dois xis mais um igual a menos xis mais quatro. [p=0.3] É a substituição, e na prática {c}você só iguala as duas expressões."),
    dict(id="s06", block="resolver", text="Daqui em diante é a balança. [p=0.2] {a}Some xis de cada lado: três xis mais um igual a quatro. [p=0.2] {b}Tire um de cada lado: três xis igual a três. [p=0.2] {c}Divida por três: xis igual a um."),
    dict(id="s07", block="resolver", text="Falta o ípsilon. [p=0.2] Use {a}qualquer uma das retas: [p=0.2] {b}dois vezes um mais um dá três. [p=0.3] E confira na outra: {c}menos um mais quatro dá três. [p=0.2] {d}Bateu. [p=0.3] As retas se cruzam em {e}xis um, ípsilon três."),
    # forma geral
    dict(id="s08", block="geral", text="E se as retas vierem {a}na forma geral? [p=0.2] {b}Xis mais ípsilon menos sete igual a zero, [p=0.2] e {c}dois xis menos ípsilon menos dois igual a zero. [p=0.3] Isole o ípsilon na primeira: {d}ípsilon igual a sete menos xis."),
    dict(id="s09", block="geral", text="Troque na segunda: [p=0.2] {a}dois xis menos, abre parênteses, sete menos xis, fecha parênteses, menos dois, igual a zero. [p=0.3] O menos antes do parêntese troca os sinais de dentro: [p=0.2] {b}dois xis menos sete mais xis menos dois igual a zero."),
    dict(id="s10", block="geral", text="{a}Três xis menos nove igual a zero, [p=0.2] e {b}xis igual a três. [p=0.2] Então, {c}ípsilon é sete menos três, que dá quatro. [p=0.3] As retas se cruzam em {d}xis três, ípsilon quatro."),
    # nem sempre existe
    dict(id="s11", block="casos", text="Toda dupla de retas se cruza? [p=0.2] Não. [p=0.3] Pegue {a}ípsilon igual a dois xis mais um [p=0.2] e {b}ípsilon igual a dois xis mais cinco. [p=0.3] Igualando, {c}o dois xis some de cada lado, [p=0.2] e sobra {d}um igual a cinco: impossível."),
    dict(id="s12", block="casos", text="Faz sentido: {a}as retas sobem dois a cada passo, com a mesma inclinação. [p=0.2] São {b}retas paralelas: [p=0.2] uma corre ao lado da outra e {c}nunca se encontram. [p=0.3] O sistema {d}não tem solução."),
    dict(id="s13", block="casos", text="Então, são {a}três casos. [p=0.2] {b}Eme diferente: as retas se cruzam num ponto só. [p=0.2] {c}Eme igual e ene diferente: paralelas, nenhum ponto. [p=0.2] {d}Eme igual e ene igual: é a mesma reta, e todos os pontos são comuns."),
    # erro
    dict(id="s14", block="erro", text="Agora, cuidado com o erro mais comum, na hora de juntar os xis. [p=0.2] Em {a}dois xis mais um igual a menos xis mais quatro, [p=0.2] a pessoa leva o menos xis para a esquerda {b}com o mesmo sinal. [p=0.3] Escreve {c}dois xis menos xis igual a três, [p=0.2] e acha {d}xis igual a três."),
    dict(id="s15", block="erro", text="A conferência denuncia. [p=0.2] Com xis três, {a}a primeira reta dá ípsilon sete. [p=0.2] {b}A segunda dá ípsilon um. [p=0.3] {c}Ípsilons diferentes: não é ponto de encontro. [p=0.3] {d}Para sumir com o menos xis, some xis de cada lado."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}compare os emes antes de fazer conta. [p=0.3] {b}Eme diferente: tem ponto de encontro, e vale resolver. [p=0.2] {c}Eme igual: olhe o ene. [p=0.2] Com ene diferente, {d}não existe ponto nenhum, e a resposta sai sem conta."),
    dict(id="s17", block="atalho", text="Funciona porque {a}o eme é a inclinação: [p=0.2] retas com inclinações diferentes {b}acabam se cruzando em algum lugar. [p=0.3] {c}Não compensa quando a questão pede o ponto: [p=0.2] o atalho diz se ele existe, mas {d}não diz onde. [p=0.2] Aí, resolva o sistema."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Uma locadora cobra {a}ípsilon igual a três xis mais vinte, [p=0.2] e outra cobra {b}ípsilon igual a cinco xis mais oito, [p=0.2] com xis em dias e ípsilon em reais. [p=0.3] {c}Em que ponto as retas se cruzam? [p=0.2] E {d}o que esse ponto quer dizer?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Os emes são três e cinco, diferentes: {a}existe o ponto. [p=0.2] Igualando: {b}três xis mais vinte igual a cinco xis mais oito. [p=0.3] {c}Tire três xis de cada lado: vinte igual a dois xis mais oito. [p=0.2] {d}Tire oito de cada lado: doze igual a dois xis. [p=0.2] {e}Xis igual a seis."),
    dict(id="s21", block="resposta", text="O ípsilon: {a}três vezes seis dá dezoito, mais vinte dá trinta e oito. [p=0.2] Na outra: {b}cinco vezes seis dá trinta, mais oito dá trinta e oito. [p=0.2] Bateu. [p=0.3] O ponto é {c}xis seis, ípsilon trinta e oito: [p=0.2] {d}com seis dias de aluguel, as locadoras cobram o mesmo, trinta e oito reais."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}o ponto de encontro resolve as duas equações, [p=0.2] {b}iguale e confira, [p=0.2] e {c}eme igual com ene diferente quer dizer paralelas, sem encontro."),
    dict(id="s23", block="fim", text="Na próxima aula, você pratica {a}tudo de pontos e retas: [p=0.2] {b}distância, equação da reta [p=0.2] e {c}como duas retas se cruzam, em questões. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
