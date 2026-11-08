# Estudativo · MAT-EQU-019 — Sistema de equações: método da adição (Matemática · Equações do 1º Grau).
# Habilidade: resolver 3x + 2y = 16 e 5x − 2y = 16 somando as equações e 2x + 3y = 12 e 3x + 2y = 13 multiplicando antes.
# Pré-requisitos: MAT-EQU-004 (sinal de menos antes do parêntese), MAT-EQU-018 (substituição). Próxima: MAT-EQU-020.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Sistema de equações: método da adição"

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
    dict(id="s01", block="gancho", text="{a}Três xis mais dois ípsilon igual a dezesseis. [p=0.2] {b}Cinco xis menos dois ípsilon igual a dezesseis. [p=0.3] Nenhuma letra está sozinha, [p=0.2] mas dá para matar esse sistema {c}somando uma equação com a outra."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender por que essa soma é permitida, [p=0.2] o que fazer quando ela {b}não basta, [p=0.2] e ainda leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas: [p=0.2] {b}a solução de um sistema vale nas duas equações ao mesmo tempo, [p=0.2] e {c}o sinal de menos antes do parêntese troca o sinal de tudo o que está dentro. [p=0.3] Se faltar alguma, procure no canal."),
    # por que pode somar
    dict(id="s04", block="balanca", text="A primeira equação é uma {a}balança equilibrada. [p=0.2] Num prato, {b}três xis mais dois ípsilon. [p=0.2] No outro, {c}dezesseis. [p=0.3] Você já sabe: colocando {d}o mesmo peso em cada prato, ela continua equilibrada."),
    dict(id="s05", block="balanca", text="A segunda equação diz que {a}cinco xis menos dois ípsilon vale dezesseis. [p=0.2] Então junte {b}cinco xis menos dois ípsilon ao prato de três xis mais dois ípsilon, [p=0.2] e {c}mais dezesseis ao outro prato. [p=0.3] Como essas duas coisas valem o mesmo, [p=0.2] você pôs o mesmo peso em cada prato, [p=0.2] e a balança {d}continua equilibrada."),
    dict(id="s06", block="somar", text="Veja o que acontece. [p=0.2] {a}Três xis mais cinco xis dá oito xis. [p=0.2] {b}Mais dois ípsilon com menos dois ípsilon dá zero: [p=0.2] {c}o ípsilon sumiu. [p=0.3] Do outro lado, {d}dezesseis mais dezesseis dá trinta e dois. [p=0.2] Ficou {e}oito xis igual a trinta e dois."),
    dict(id="s07", block="somar", text="{a}Divida cada lado por oito: [p=0.2] {b}xis igual a quatro. [p=0.3] Na primeira equação, três xis vira doze: [p=0.2] {c}doze mais dois ípsilon igual a dezesseis. [p=0.3] {d}Tire doze de cada lado: [p=0.2] {e}dois ípsilon igual a quatro, [p=0.2] e {f}ípsilon igual a dois."),
    dict(id="s08", block="somar", text="Conferindo na segunda: [p=0.2] {a}cinco vezes quatro dá vinte. [p=0.2] {b}Duas vezes dois dá quatro. [p=0.2] {c}Vinte menos quatro dá dezesseis. [p=0.2] {d}Bateu."),
    # multiplicar antes
    dict(id="s09", block="multiplicar", text="Deu certo porque havia {a}mais dois ípsilon numa equação e menos dois ípsilon na outra. [p=0.2] Números opostos se anulam. [p=0.3] E neste sistema? [p=0.2] {b}Dois xis mais três ípsilon igual a doze, [p=0.2] e {c}três xis mais dois ípsilon igual a treze."),
    dict(id="s10", block="multiplicar", text="Somando direto, {a}nenhuma letra some. [p=0.3] Então, antes, {b}multiplique cada equação até uma letra ter o mesmo número na frente. [p=0.2] Na balança, isso é permitido: [p=0.2] {c}o triplo de um prato pesa o mesmo que o triplo do outro."),
    dict(id="s11", block="multiplicar", text="{a}A primeira, vezes três: [p=0.2] {b}seis xis mais nove ípsilon igual a trinta e seis. [p=0.3] {c}A segunda, vezes dois: [p=0.2] {d}seis xis mais quatro ípsilon igual a vinte e seis. [p=0.3] O xis ficou com {e}seis na frente nas duas."),
    dict(id="s12", block="multiplicar", text="Com números iguais, {a}subtraia a segunda da primeira. [p=0.2] É tirar {b}o mesmo peso de cada prato. [p=0.3] Como no menos antes do parêntese, o menos vale para cada termo da segunda. [p=0.3] {c}Seis xis menos seis xis dá zero. [p=0.2] {d}Nove ípsilon menos quatro ípsilon dá cinco ípsilon. [p=0.2] {e}Trinta e seis menos vinte e seis dá dez."),
    dict(id="s13", block="multiplicar", text="Ficou {a}cinco ípsilon igual a dez, [p=0.2] então {b}ípsilon igual a dois. [p=0.3] Na primeira equação original: [p=0.2] {c}dois xis mais seis igual a doze. [p=0.2] {d}Dois xis igual a seis, [p=0.2] e {e}xis igual a três."),
    dict(id="s14", block="multiplicar", text="Conferindo na segunda: [p=0.2] {a}três vezes três dá nove, mais quatro dá treze. [p=0.2] {b}Bateu. [p=0.3] A regra: {c}números opostos na frente da letra, some. [p=0.2] {d}Números iguais, subtraia. [p=0.2] {e}Nem um nem outro? Multiplique antes."),
    # erro
    dict(id="s15", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}multiplicar só um lado. [p=0.2] A pessoa escreve {b}seis xis mais nove ípsilon igual a doze, [p=0.2] e o doze fica sem multiplicar."),
    dict(id="s16", block="erro", text="Na balança, é como {a}triplicar um prato e deixar o outro igual: [p=0.2] desequilibra. [p=0.3] A conta segue e dá {b}um ípsilon negativo e quebrado, [p=0.2] e o par {c}não confere nas duas equações. [p=0.3] Multiplicou? [p=0.2] {d}Multiplique a equação inteira."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho prometido: [p=0.2] {a}antes de resolver, olhe o que a pergunta pede. [p=0.3] Volte ao segundo sistema. [p=0.2] Se a pergunta quer {b}xis mais ípsilon, some as equações do jeito que estão. [p=0.2] {c}Cinco xis mais cinco ípsilon igual a vinte e cinco. [p=0.2] Divida cada lado por cinco: [p=0.2] {d}xis mais ípsilon igual a cinco."),
    dict(id="s18", block="atalho", text="Funciona porque, somando, {a}cada letra ficou com cinco na frente. [p=0.3] Não compensa quando a soma deixa {b}números diferentes na frente das letras, [p=0.2] ou quando a pergunta quer {c}cada valor separado. [p=0.2] Aí, resolva o sistema inteiro."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Resolva pela adição: [p=0.2] {a}xis mais dois ípsilon igual a onze, [p=0.2] e {b}três xis menos quatro ípsilon igual a três. [p=0.3] {c}Quanto valem xis e ípsilon?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] O ípsilon tem {a}mais dois numa e menos quatro na outra. [p=0.2] Então {b}multiplique a primeira por dois: [p=0.2] {c}dois xis mais quatro ípsilon igual a vinte e dois. [p=0.3] Com mais quatro e menos quatro, {d}some: [p=0.2] {e}cinco xis igual a vinte e cinco, [p=0.2] e {f}xis igual a cinco."),
    dict(id="s22", block="resposta", text="Na primeira equação: [p=0.2] {a}cinco mais dois ípsilon igual a onze. [p=0.2] {b}Dois ípsilon igual a seis, [p=0.2] e {c}ípsilon igual a três. [p=0.3] Conferindo na segunda: [p=0.2] {d}três vezes cinco dá quinze. [p=0.2] {e}Quatro vezes três dá doze. [p=0.2] {f}Quinze menos doze dá três. [p=0.2] Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}deixe uma letra com números opostos ou iguais, [p=0.2] {b}some ou subtraia para ela sumir [p=0.2] e {c}confira nas duas equações."),
    dict(id="s24", block="fim", text="Na próxima aula, você aprende a {a}transformar um problema escrito em sistema, [p=0.2] e ainda resolve um deles {b}supondo que tudo é de um tipo só. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
