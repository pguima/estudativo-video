# Estudativo · MAT-EQU-009 — Equação com parênteses (Matemática · Equações do 1º Grau).
# Habilidade: resolver 3(x − 2) = 2x + 4 e reconhecer o que acontece em 2x + 1 = 2x + 3.
# Pré-requisitos: MAT-EQU-004 (distributiva e sinal de menos), MAT-EQU-008 (letra dos dois lados). Próxima: MAT-EQU-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Equação com parênteses"

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
    dict(id="s01", block="gancho", text="{a}Dois xis mais um igual a dois xis mais três. [p=0.3] Você faz tudo certo, e {b}o xis some. [p=0.3] Errou alguma coisa? [p=0.2] {c}Não. [p=0.2] Essa equação está dando um recado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve equações com parênteses [p=0.2] e entende o que fazer quando o xis desaparece. [p=0.2] E leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}abrir parênteses, multiplicando o número de fora por cada termo de dentro, [p=0.2] e {c}resolver equação com xis dos dois lados. [p=0.3] Se faltar alguma, procure no canal."),
    # exemplo com parênteses
    dict(id="s04", block="parenteses", text="Veja {a}três, abre parênteses, xis menos dois, fecha parênteses, igual a dois xis mais quatro. [p=0.3] O xis está {b}preso dentro dos parênteses. [p=0.2] Antes de usar a balança, {c}solte ele."),
    dict(id="s05", block="parenteses", text="{a}Passo um: abra os parênteses. [p=0.2] O três na frente quer dizer {b}três vezes tudo o que está dentro, [p=0.2] como {c}três pacotes iguais, cada um com xis menos dois dentro. [p=0.3] Então o três multiplica {d}cada termo de dentro."),
    dict(id="s06", block="parenteses", text="{a}Três vezes xis dá três xis. [p=0.2] {b}Três vezes menos dois dá menos seis. [p=0.3] Fica {c}três xis menos seis igual a dois xis mais quatro."),
    dict(id="s07", block="parenteses", text="{a}Passo dois: agora é uma equação como as da aula passada. [p=0.2] {b}Tire dois xis de cada lado: [p=0.2] {c}xis menos seis igual a quatro. [p=0.3] {d}Some seis de cada lado: [p=0.2] {e}xis igual a dez."),
    dict(id="s08", block="parenteses", text="Conferindo na equação {a}do começo, com os parênteses. [p=0.2] {b}Dez menos dois dá oito. [p=0.1] Vezes três dá vinte e quatro. [p=0.3] {c}Dois vezes dez dá vinte. [p=0.1] Mais quatro dá vinte e quatro. [p=0.2] Bateu."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é {a}multiplicar só o xis. [p=0.2] A pessoa escreve {b}três xis menos dois, [p=0.2] esquecendo de multiplicar o dois. [p=0.3] E chega em {c}xis igual a seis."),
    dict(id="s10", block="erro", text="Confira: {a}seis menos dois dá quatro. [p=0.1] Vezes três dá doze. [p=0.2] {b}Dois vezes seis mais quatro dá dezesseis. [p=0.2] {c}Doze não é dezesseis. [p=0.3] O número de fora multiplica {d}todo mundo lá dentro."),
    # quando o xis some
    dict(id="s11", block="some", text="Agora, o caso do começo: {a}dois xis mais um igual a dois xis mais três. [p=0.3] {b}Tire dois xis de cada lado. [p=0.2] Sobra {c}um igual a três."),
    dict(id="s12", block="some", text="Um igual a três é {a}falso. [p=0.2] E não depende do xis, porque {b}ele sumiu. [p=0.3] Então {c}nenhum número resolve essa equação. [p=0.2] A resposta é: {d}não tem solução."),
    dict(id="s13", block="some", text="Na balança, dá para ver. [p=0.2] {a}Cada prato tem duas caixas iguais. [p=0.2] Mas {b}um prato tem um peso a mais, e o outro tem três. [p=0.3] Seja qual for o peso da caixa, {c}o lado direito pesa sempre dois quilos a mais. [p=0.2] Nunca equilibra."),
    dict(id="s14", block="some", text="E se sobrar uma conta verdadeira? [p=0.2] Veja {a}dois, abre parênteses, xis mais um, fecha parênteses, igual a dois xis mais dois. [p=0.3] Abrindo os parênteses, o lado esquerdo vira dois xis mais dois, {b}igualzinho ao direito. [p=0.2] Tirando dois xis de cada lado, sobra {c}dois igual a dois: verdadeiro, seja qual for o xis. [p=0.3] Os pratos são iguais, então {d}todo número serve. [p=0.2] Teste com dez: vinte e dois igual a vinte e dois."),
    # atalho
    dict(id="s15", block="atalho", text="O atalho: {a}depois de abrir os parênteses e juntar os termos semelhantes, olhe o número que multiplica o xis em cada lado. [p=0.3] {b}Se for o mesmo, o xis vai sumir. [p=0.2] Basta comparar os números sem letra: [p=0.2] {c}diferentes, nenhuma solução. [p=0.2] {d}Iguais, todo número serve."),
    dict(id="s16", block="atalho", text="Funciona porque {a}tirar o mesmo tanto de caixas de cada prato deixa só os pesos. [p=0.3] {b}Não vale olhar antes de abrir os parênteses: [p=0.2] no primeiro exemplo, {c}o três xis estava escondido lá dentro."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Resolva {a}quatro, abre parênteses, xis mais um, fecha parênteses, igual a xis mais dezenove. [p=0.3] {b}Quanto vale xis?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Abra os parênteses: quatro xis mais quatro. [p=0.2] O número que multiplica o xis é {b}quatro de um lado e um do outro: [p=0.2] são diferentes, então tem solução. [p=0.3] {c}Tire xis de cada lado: três xis mais quatro igual a dezenove. [p=0.2] {d}Subtraia quatro: três xis igual a quinze. [p=0.2] {e}Divida por três: xis igual a cinco."),
    dict(id="s20", block="resposta", text="Conferindo: {a}cinco mais um dá seis. [p=0.1] Vezes quatro dá vinte e quatro. [p=0.2] {b}Cinco mais dezenove dá vinte e quatro. [p=0.2] Bateu. [p=0.3] Quem multiplicou só o xis chegou em {c}seis, que não confere."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}abra os parênteses primeiro, [p=0.2] {b}resolva como antes [p=0.2] e, se o xis sumir, {c}leia o que sobrou."),
    dict(id="s22", block="fim", text="Na próxima aula, a equação vem com {a}frações e com vírgula, [p=0.2] e você aprende a {b}fazer as frações sumirem. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
