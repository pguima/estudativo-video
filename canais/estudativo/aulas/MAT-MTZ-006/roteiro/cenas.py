# Estudativo · MAT-MTZ-006 — Sistema 3x3 por escalonamento (Matemática · Matrizes e Sistemas).
# Habilidade: resolver x + y + z = 6, x + 2y + z = 8, x + y + 2z = 9 eliminando uma letra por vez, até achar (1, 2, 3).
# Pré-requisitos: MAT-EQU-019 (método da adição). Próxima: MAT-MTZ-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Matrizes (MAT-MTZ-001 a 005) não estão na ficha: tudo com equações, sem matriz.
# Letras narradas "xis", "ípsilon" e "zê", como em MAT-EQU-019.

TITULO = "Sistema 3x3 por escalonamento"

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
    dict(id="s01", block="gancho", text="{a}Três equações e três letras: xis, ípsilon e zê. [p=0.3] Parece muita coisa, [p=0.2] mas o segredo é {b}não atacar tudo de uma vez. [p=0.3] Elimine {c}uma letra por vez, [p=0.2] e o sistema vira {d}uma escada."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve um sistema de três equações e três letras, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre {a}duas coisas: [p=0.2] {b}a solução de um sistema vale em todas as equações ao mesmo tempo, [p=0.2] e {c}no método da adição, você soma ou subtrai equações inteiras para uma letra sumir. [p=0.3] Se faltar alguma, procure no canal."),
    # o sistema
    dict(id="s04", block="sistema", text="Veja este sistema. [p=0.2] {a}Xis mais ípsilon mais zê igual a seis. [p=0.2] {b}Xis mais dois ípsilon mais zê igual a oito. [p=0.2] {c}Xis mais ípsilon mais dois zê igual a nove. [p=0.3] A resposta é um trio: [p=0.2] {d}um valor para xis, um para ípsilon e um para zê."),
    dict(id="s05", block="sistema", text="O objetivo é chegar numa {a}escada: [p=0.2] {b}uma equação com as três letras, [p=0.2] {c}outra com duas, [p=0.2] {d}e a última com uma letra só. [p=0.3] Esse jeito de arrumar se chama {e}escalonamento, [p=0.2] e a escada se resolve {f}de baixo para cima."),
    # eliminar
    dict(id="s06", block="elimina", text="Para chegar lá, {a}use a primeira equação para tirar o xis das outras duas. [p=0.3] {b}Segunda menos primeira: [p=0.2] xis menos xis, zero; [p=0.2] dois ípsilon menos ípsilon, ípsilon; [p=0.2] zê menos zê, zero; [p=0.2] oito menos seis, dois. [p=0.3] Sobrou {c}ípsilon igual a dois."),
    dict(id="s07", block="elimina", text="{a}Terceira menos primeira: [p=0.2] o xis some, o ípsilon some, [p=0.2] e {b}dois zê menos zê dá zê. [p=0.2] Nove menos seis: {c}zê igual a três."),
    dict(id="s08", block="elimina", text="E se a segunda começasse com {a}dois xis? [p=0.2] Aí, {b}multiplique a primeira por dois antes de subtrair, [p=0.2] como no método da adição. [p=0.3] {c}A ideia é sempre a mesma: o xis precisa sumir."),
    # subir
    dict(id="s09", block="subir", text="Agora, {a}suba a escada. [p=0.2] Na primeira equação, troque ípsilon por dois e zê por três: [p=0.2] {b}xis mais dois mais três igual a seis. [p=0.2] {c}Xis mais cinco igual a seis, [p=0.2] e {d}xis igual a um."),
    dict(id="s10", block="subir", text="A solução é o trio {a}um, dois, três. [p=0.3] Confira na terceira: [p=0.2] {b}um mais dois, mais duas vezes três: [p=0.2] um mais dois mais seis, nove. [p=0.2] {c}Bateu."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}subtrair só o lado das letras. [p=0.3] Na segunda menos primeira, a pessoa esquece de fazer oito menos seis [p=0.2] e escreve {b}ípsilon igual a oito. [p=0.3] Daí em diante, {c}nada confere. [p=0.3] A equação é uma balança: {d}o que sai de um lado sai do outro."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho de prova: [p=0.2] {a}em questão com alternativas, teste os trios. [p=0.3] {b}Troque as letras pelos números de cada alternativa. [p=0.2] {c}O trio que valer nas três equações é a resposta."),
    dict(id="s13", block="atalho", text="Funciona porque a solução {a}precisa valer em todas as equações. [p=0.3] Comece pela {b}equação de números mais diferentes: [p=0.2] ela derruba mais alternativas. [p=0.3] {c}Não compensa sem alternativas: aí, escalone."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Resolva: [p=0.2] {a}xis mais ípsilon mais zê igual a seis; [p=0.2] {b}dois xis mais três ípsilon mais zê igual a catorze; [p=0.2] {c}xis mais dois ípsilon mais três zê igual a onze."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] A segunda começa com dois xis, então {a}multiplique a primeira por dois: [p=0.2] {b}dois xis mais dois ípsilon mais dois zê igual a doze. [p=0.3] {c}Segunda menos essa: [p=0.2] ípsilon menos zê igual a dois."),
    dict(id="s17", block="resposta", text="{a}Terceira menos primeira: [p=0.2] ípsilon mais dois zê igual a cinco. [p=0.3] Sobraram duas equações com ípsilon e zê. [p=0.2] {b}Subtraia uma da outra, e o ípsilon some. [p=0.2] Dois zê menos, abre parênteses, menos zê, fecha parênteses: {c}três zê. [p=0.2] Cinco menos dois, três. [p=0.2] {d}Três zê igual a três, e zê igual a um."),
    dict(id="s18", block="resposta", text="Subindo a escada: [p=0.2] {a}ípsilon menos um igual a dois, [p=0.2] então ípsilon é três. [p=0.3] {b}Xis mais três mais um igual a seis, [p=0.2] então xis é dois. [p=0.3] A solução é {c}dois, três, um."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}use a primeira equação para tirar o xis das outras, [p=0.2] {b}repita até virar escada [p=0.2] e {c}suba a escada, conferindo no fim."),
    dict(id="s20", block="fim", text="Na próxima aula, você descobre que nem todo sistema tem uma resposta só: [p=0.2] {a}alguns têm infinitas, [p=0.2] e {b}outros não têm nenhuma. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
