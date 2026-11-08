# Estudativo · MAT-EQU-008 — Equação com letra dos dois lados (Matemática · Equações do 1º Grau).
# Habilidade: resolver 2x + 3 = 11 e 5x − 2 = 3x + 8.
# Pré-requisitos: MAT-EQU-003 (juntar termos semelhantes), MAT-EQU-007 (a balança). Próxima: MAT-EQU-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Equação com letra dos dois lados"

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
    dict(id="s01", block="gancho", text="{a}Cinco xis menos dois igual a três xis mais oito. [p=0.3] Tem {b}xis dos dois lados do igual. [p=0.3] Parece mais difícil, [p=0.2] mas a regra é {c}a mesma da balança."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve equações de vários passos, [p=0.2] com xis de um lado ou dos dois, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}fazer o mesmo nos dois lados da balança [p=0.2] e {c}juntar termos semelhantes, como juntar cinco xis menos três xis em dois xis. [p=0.3] Se faltar alguma, procure no canal."),
    # dois passos
    dict(id="s04", block="ordem", text="Comece por {a}dois xis mais três igual a onze. [p=0.3] Aqui o xis passou por uma conta e depois outra: [p=0.2] ele foi {b}multiplicado por dois [p=0.2] e depois {c}somado com três."),
    dict(id="s05", block="ordem", text="Para desfazer, vá {a}na ordem contrária, [p=0.2] como quem se veste. [p=0.2] Você {b}põe a meia e depois o sapato, [p=0.2] mas {c}tira primeiro o sapato. [p=0.3] O último a entrar foi o mais três, [p=0.2] então {d}ele sai primeiro."),
    dict(id="s06", block="ordem", text="{a}Passo um: subtraia três de cada lado. [p=0.2] {b}Onze menos três dá oito. [p=0.2] Fica {c}dois xis igual a oito."),
    dict(id="s07", block="ordem", text="{a}Passo dois: divida cada lado por dois. [p=0.2] {b}Oito dividido por dois dá quatro. [p=0.3] {c}Xis igual a quatro. [p=0.3] Conferindo: {d}dois vezes quatro dá oito. [p=0.2] Mais três dá onze. [p=0.2] Bateu."),
    # xis dos dois lados
    dict(id="s08", block="lados", text="Voltando a {a}cinco xis menos dois igual a três xis mais oito. [p=0.3] Na balança, há {b}caixas nos dois pratos: [p=0.2] cinco de um lado e três do outro. [p=0.3] O primeiro passo é {c}deixar as caixas num prato só."),
    dict(id="s09", block="lados", text="{a}Tire três xis de cada lado. [p=0.2] Sobram {b}duas caixas à esquerda e nenhuma à direita. [p=0.3] Juntando termos semelhantes, {c}cinco xis menos três xis dá dois xis. [p=0.2] Fica {d}dois xis menos dois igual a oito."),
    dict(id="s10", block="lados", text="Por que tirar três xis, e não cinco xis? [p=0.2] Tirar cinco xis também daria certo, [p=0.1] mas à direita sobraria três xis menos cinco xis: menos dois xis, [p=0.2] uma quantidade negativa de caixas, que a balança nem mostra. [p=0.3] Tirando três xis, a letra fica {a}no lado que tinha mais xis, [p=0.2] e {b}o número que multiplica a letra fica positivo. [p=0.2] Você foge do sinal de menos."),
    dict(id="s11", block="lados", text="Daqui em diante, é o caso de antes. [p=0.2] {a}O dois está subtraindo: some dois de cada lado. [p=0.2] {b}Dois xis igual a dez. [p=0.2] {c}Divida cada lado por dois: [p=0.2] {d}xis igual a cinco."),
    dict(id="s12", block="lados", text="Conferindo no lado esquerdo: [p=0.2] {a}cinco vezes cinco dá vinte e cinco. [p=0.1] Menos dois dá vinte e três. [p=0.3] No lado direito: [p=0.2] {b}três vezes cinco dá quinze. [p=0.1] Mais oito dá vinte e três. [p=0.3] {c}Vinte e três igual a vinte e três. Bateu."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum aparece no primeiro exemplo. [p=0.2] A pessoa {a}divide primeiro, mas só o dois xis e o onze: [p=0.2] {b}xis mais três igual a onze dividido por dois, que é cinco e meio. [p=0.3] Daí em diante, {c}toda conta sai errada."),
    dict(id="s14", block="erro", text="Teste com o quatro, que você já conferiu: [p=0.2] {a}quatro mais três dá sete, [p=0.2] {b}e não cinco e meio. [p=0.3] Dividir até vale, mas {c}teria que dividir o três também. [p=0.2] Por isso, {d}tire primeiro o número sem letra."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho que você talvez já tenha ouvido: [p=0.2] {a}passa para o outro lado trocando o sinal. [p=0.3] Ele não é uma regra nova. [p=0.2] É {b}a balança, escrita mais rápido."),
    dict(id="s16", block="atalho", text="Em dois xis mais três igual a onze, você subtraiu três de cada lado. [p=0.2] À esquerda, {a}o mais três sumiu. [p=0.2] À direita, {b}apareceu um menos três. [p=0.3] Parece que o três {c}pulou o igual e trocou de sinal."),
    dict(id="s17", block="atalho", text="Cuidado: isso vale só para {a}o que está somando ou subtraindo, com letra ou sem. [p=0.3] O número que multiplica a letra {b}passa dividindo, e não vira menos. [p=0.2] Veja dois xis igual a dez. [p=0.2] {c}Xis igual a dez dividido por dois, que dá cinco. [p=0.3] {d}Na dúvida, não use o atalho: [p=0.1] faça a conta nos dois lados."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Resolva {a}sete xis menos quatro igual a três xis mais vinte. [p=0.3] {b}Quanto vale xis?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Deixe a letra do lado com mais xis: {a}tire três xis de cada lado. [p=0.2] {b}Quatro xis menos quatro igual a vinte. [p=0.3] {c}Some quatro de cada lado: quatro xis igual a vinte e quatro. [p=0.2] {d}Divida cada lado por quatro: xis igual a seis."),
    dict(id="s21", block="resposta", text="Conferindo: [p=0.2] {a}sete vezes seis dá quarenta e dois. [p=0.1] Menos quatro dá trinta e oito. [p=0.3] {b}Três vezes seis dá dezoito. [p=0.1] Mais vinte dá trinta e oito. [p=0.2] {c}Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}junte o xis no lado que tem mais, [p=0.2] {b}tire o número sem letra [p=0.2] e {c}divida pelo número que multiplica a letra."),
    dict(id="s23", block="fim", text="Na próxima aula, a equação vem com {a}parênteses, [p=0.2] e você conhece {b}uma equação que nenhum número resolve. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
