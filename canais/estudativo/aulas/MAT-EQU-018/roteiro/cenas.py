# Estudativo · MAT-EQU-018 — Sistema de equações: método da substituição (Matemática · Equações do 1º Grau).
# Habilidade: testar se x = 2 e y = 3 resolvem um sistema e resolver c + m = 30 e 4c + 2m = 100 por substituição.
# Pré-requisitos: MAT-EQU-009 (equação com parênteses). Próxima: MAT-EQU-019.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Montar o sistema a partir do texto é da MAT-EQU-020: aqui o sistema dos veículos já vem pronto, só com o sentido de cada letra.

TITULO = "Sistema de equações: método da substituição"

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
    dict(id="s01", block="gancho", text="{a}Xis mais ípsilon igual a cinco. [p=0.3] São duas letras, cada uma no lugar de um número. [p=0.3] Quanto vale xis? [p=0.3] {b}Pode ser um, e aí ípsilon é quatro. [p=0.2] {c}Pode ser dois, e aí ípsilon é três. [p=0.3] Com uma equação só, {d}sobra resposta demais."),
    dict(id="s02", block="gancho", text="Mas, se chega {a}uma segunda informação, [p=0.2] a resposta vira uma só. [p=0.3] {b}Até o fim desta aula, você resolve duas equações juntas, [p=0.2] e ainda leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}resolver equação fazendo o mesmo de cada lado da balança, [p=0.2] e {c}abrir parênteses, multiplicando o número de fora por cada termo de dentro. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é sistema e solução
    dict(id="s04", block="sistema", text="Duas equações que precisam valer {a}ao mesmo tempo formam um {b}sistema. [p=0.3] Veja este: [p=0.2] {c}xis mais ípsilon igual a cinco, [p=0.2] e {d}dois xis mais ípsilon igual a sete."),
    dict(id="s05", block="sistema", text="Será que {a}xis igual a dois e ípsilon igual a três resolvem? [p=0.2] Troque as letras pelos números. [p=0.3] Na primeira, {b}dois mais três dá cinco. [p=0.2] {c}Confere. [p=0.3] Na segunda, {d}duas vezes dois dá quatro, mais três dá sete. [p=0.2] {e}Confere também."),
    dict(id="s06", block="sistema", text="Valeu nas duas equações, então {a}é a solução do sistema. [p=0.3] E {b}xis igual a um com ípsilon igual a quatro? [p=0.2] Na primeira, {c}um mais quatro dá cinco. [p=0.2] Na segunda, {d}duas vezes um mais quatro dá seis, e não sete. [p=0.3] {e}Falhou em uma, não serve."),
    # o problema
    dict(id="s07", block="problema", text="Testar é ótimo para conferir. [p=0.2] Mas como achar a solução do zero? [p=0.3] Num estacionamento há {a}trinta veículos, entre carros e motos, [p=0.2] e {b}cem rodas no total. [p=0.3] {c}Quantos são os carros e quantas são as motos?"),
    dict(id="s08", block="problema", text="{a}A letra xis é o número de carros. [p=0.2] {b}A letra ípsilon é o número de motos. [p=0.3] Carros mais motos dá trinta: [p=0.2] {c}xis mais ípsilon igual a trinta. [p=0.3] Cada carro tem quatro rodas, e cada moto tem duas: [p=0.2] {d}quatro xis mais dois ípsilon igual a cem."),
    # método
    dict(id="s09", block="metodo", text="A substituição tem {a}três passos. [p=0.3] {b}Passo um: deixar uma letra sozinha. [p=0.2] Na primeira equação, tire o xis de cada lado da balança: [p=0.2] {c}ípsilon igual a trinta menos xis. [p=0.2] As motos são trinta menos os carros."),
    dict(id="s10", block="metodo", text="{a}Passo dois: trocar essa letra na outra equação. [p=0.2] Onde estava ípsilon, entra {b}trinta menos xis, entre parênteses. [p=0.3] Fica {c}quatro xis mais duas vezes o parêntese, igual a cem."),
    dict(id="s11", block="metodo", text="Abrindo o parêntese: [p=0.2] {a}duas vezes trinta dá sessenta. [p=0.2] {b}Duas vezes menos xis dá menos dois xis. [p=0.3] Juntando as letras, {c}quatro xis menos dois xis dá dois xis. [p=0.2] Ficou {d}dois xis mais sessenta igual a cem."),
    dict(id="s12", block="metodo", text="Daqui em diante é a balança. [p=0.2] {a}Tire sessenta de cada lado: [p=0.2] {b}dois xis igual a quarenta. [p=0.2] {c}Divida cada lado por dois: [p=0.2] {d}xis igual a vinte. [p=0.3] São vinte carros."),
    dict(id="s13", block="metodo", text="{a}Passo três: voltar para achar a outra letra. [p=0.2] Ípsilon é trinta menos xis: [p=0.2] {b}trinta menos vinte dá dez. [p=0.3] Resposta: {c}vinte carros e dez motos."),
    dict(id="s14", block="conferir", text="Sempre confira {a}nas duas equações. [p=0.3] {b}Vinte mais dez dá trinta veículos. [p=0.2] {c}Vinte carros com quatro rodas dão oitenta. [p=0.2] {d}Dez motos com duas rodas dão vinte. [p=0.2] {e}Oitenta mais vinte dá cem. [p=0.2] {f}Bateu."),
    # erro
    dict(id="s15", block="erro", text="Agora, cuidado com o erro mais comum, que mora no parêntese. [p=0.2] A pessoa multiplica {a}só o trinta [p=0.2] e escreve {b}sessenta menos xis, [p=0.2] em vez de {c}sessenta menos dois xis."),
    dict(id="s16", block="erro", text="Aí a conta vira {a}três xis igual a quarenta, [p=0.2] e quarenta dividido por três {b}não dá número inteiro. [p=0.3] Ninguém estaciona um pedaço de carro. [p=0.3] O número de fora {c}multiplica tudo o que está dentro do parêntese."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho prometido: [p=0.2] {a}deixe sozinha a letra sem número escrito na frente, a que tem o um escondido. [p=0.3] Em xis mais ípsilon igual a trinta, nenhuma letra tem número escrito na frente. [p=0.2] Basta {b}tirar uma delas de cada lado."),
    dict(id="s18", block="atalho", text="Funciona porque, assim, {a}você não divide nada. [p=0.3] Se isolasse o xis na segunda equação, [p=0.2] teria que {b}dividir tudo por quatro, e apareceria fração. [p=0.3] {c}Quando todas as letras têm número escrito na frente, a substituição dá trabalho, [p=0.2] e outro método compensa mais."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Resolva por substituição: [p=0.2] {a}xis mais ípsilon igual a doze, [p=0.2] e {b}três xis mais ípsilon igual a vinte. [p=0.3] {c}Quanto valem xis e ípsilon?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Na primeira, tire xis de cada lado: [p=0.2] {a}ípsilon igual a doze menos xis. [p=0.3] Na segunda, troque o ípsilon: [p=0.2] {b}três xis mais doze menos xis, igual a vinte. [p=0.2] Com mais na frente, o parêntese só some. [p=0.3] Juntando as letras, {c}dois xis mais doze igual a vinte."),
    dict(id="s22", block="resposta", text="{a}Tire doze de cada lado: [p=0.2] {b}dois xis igual a oito. [p=0.2] Dividindo por dois, {c}xis igual a quatro. [p=0.3] E ípsilon é doze menos quatro: [p=0.2] {d}ípsilon igual a oito."),
    dict(id="s23", block="resposta", text="Conferindo: [p=0.2] {a}quatro mais oito dá doze. [p=0.2] {b}Três vezes quatro dá doze, mais oito dá vinte. [p=0.2] {c}Bateu nas duas."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}deixe uma letra sozinha, [p=0.2] {b}troque na outra equação [p=0.2] e {c}confira nas duas."),
    dict(id="s25", block="fim", text="E quando nenhuma letra está sozinha? [p=0.2] Na próxima aula, você resolve o sistema {a}somando as equações, [p=0.2] para uma letra sumir. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
