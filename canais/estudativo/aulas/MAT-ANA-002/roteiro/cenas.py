# Estudativo · MAT-ANA-002 — Ponto médio e baricentro (Matemática · Geometria Analítica · Pontos no plano).
# Habilidade: achar o ponto médio de (2, 4) e (6, 10), que é (4, 7), e o baricentro de um triângulo pela média das coordenadas.
# Pré-requisitos: MAT-FUN-001 (plano cartesiano), MAT-ANG-020 (baricentro, encontro das medianas). Próxima: MAT-ANA-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Pares narrados "xis dois, ípsilon quatro", como na MAT-FUN-001. Vértices "á", "bê", "cê".
# Média aritmética não está na ficha: explicada na hora (soma dividida pela quantidade). Todas as contas dão inteiro.

TITULO = "Ponto médio e baricentro"

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
    dict(id="s01", block="gancho", text="Duas amigas moram em {a}xis dois, ípsilon quatro, [p=0.2] e em {b}xis seis, ípsilon dez. [p=0.3] Elas querem se encontrar {c}exatamente no meio do caminho. [p=0.2] Onde? [p=0.3] Em {d}xis quatro, ípsilon sete, [p=0.2] e dá para achar de cabeça."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o ponto médio de qualquer segmento [p=0.2] e {b}o baricentro de um triângulo, [p=0.2] com um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}ler e marcar pontos no plano, primeiro o xis, depois o ípsilon; [p=0.2] e {c}o baricentro, o ponto de equilíbrio do triângulo, onde as três medianas se encontram. [p=0.3] Se faltar alguma, procure no canal."),
    # o meio de dois números
    dict(id="s04", block="media", text="Comece com {a}uma coordenada só. [p=0.2] Na reta numérica, qual é o meio entre {b}dois e seis? [p=0.3] {c}É quatro: dois passos de cada lado."),
    dict(id="s05", block="media", text="A conta que acha o meio é {a}somar e dividir por dois. [p=0.2] {b}Dois mais seis dá oito. [p=0.2] {c}Oito dividido por dois dá quatro. [p=0.3] Esse número do meio se chama {d}média: [p=0.2] a soma dividida pela quantidade de números."),
    # ponto médio
    dict(id="s06", block="medio", text="No plano, {a}faça isso com o xis e com o ípsilon, separados. [p=0.3] {b}Xis: dois mais seis dá oito, [p=0.2] dividido por dois dá quatro. [p=0.2] {c}Ípsilon: quatro mais dez dá catorze, [p=0.2] dividido por dois dá sete. [p=0.3] O ponto médio é {d}xis quatro, ípsilon sete."),
    dict(id="s07", block="medio", text="Por que funciona? [p=0.2] Do primeiro ponto até o ponto médio, {a}o corredor anda dois e o elevador sobe três. [p=0.3] Do ponto médio até o segundo, {b}anda dois e sobe três de novo. [p=0.3] {c}Passos iguais: ele está bem no meio do segmento."),
    dict(id="s08", block="medio", text="Com negativos, a conta é a mesma. [p=0.2] Ponto médio de {a}xis menos três, ípsilon dois, [p=0.2] e {b}xis cinco, ípsilon menos seis. [p=0.3] {c}Xis: menos três mais cinco dá dois, [p=0.2] dividido por dois dá um. [p=0.2] {d}Ípsilon: dois menos seis dá menos quatro, [p=0.2] dividido por dois dá menos dois. [p=0.3] Ponto médio: {e}xis um, ípsilon menos dois."),
    # baricentro
    dict(id="s09", block="baricentro", text="E o baricentro? [p=0.2] É a mesma ideia, com {a}três pontos. [p=0.3] {b}Some os três xis e divida por três. [p=0.2] {c}Some os três ípsilons e divida por três. [p=0.3] O baricentro é {d}a média das coordenadas dos vértices."),
    dict(id="s10", block="baricentro", text="Triângulo de vértices {a}xis um, ípsilon dois; [p=0.2] {b}xis cinco, ípsilon quatro; [p=0.2] e {c}xis três, ípsilon nove. [p=0.3] {d}Xis: um mais cinco mais três dá nove, [p=0.2] dividido por três dá três. [p=0.2] {e}Ípsilon: dois mais quatro mais nove dá quinze, [p=0.2] dividido por três dá cinco. [p=0.3] Baricentro: {f}xis três, ípsilon cinco."),
    # erro
    dict(id="s11", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}subtrair em vez de somar. [p=0.3] Com os pontos do começo, a pessoa faz {b}seis menos dois dá quatro, dividido por dois dá dois. [p=0.2] E {c}dez menos quatro dá seis, dividido por dois dá três. [p=0.2] Responde {d}xis dois, ípsilon três."),
    dict(id="s12", block="erro", text="Mas o meio tem de ficar {a}entre os pontos. [p=0.2] O ípsilon três {b}nem chega no quatro, que é onde o segmento começa. [p=0.3] A subtração dá {c}metade do caminho, e não o lugar do meio. [p=0.2] {d}Para o ponto médio, some."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, que cai muito: [p=0.2] {a}achar a outra ponta, conhecendo o ponto médio. [p=0.3] {b}Dobre o ponto médio e tire a ponta que você tem. [p=0.3] Ponto médio {c}xis quatro, ípsilon sete; [p=0.2] uma ponta em {d}xis dois, ípsilon quatro. [p=0.2] {e}Oito menos dois dá seis. [p=0.2] {f}Catorze menos quatro dá dez. [p=0.2] A outra ponta é {g}xis seis, ípsilon dez."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o ponto médio é a soma dividida por dois. [p=0.2] Então {b}o dobro dele é a soma das pontas: [p=0.2] tirando uma, sobra a outra. [p=0.3] {c}Não compensa quando você já tem as pontas: [p=0.2] aí, some e divida por dois."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um triângulo tem vértices {a}á, em xis menos dois, ípsilon cinco; [p=0.2] {b}bê, em xis quatro, ípsilon um; [p=0.2] e {c}cê, em xis sete, ípsilon três. [p=0.3] {d}Qual é o ponto médio do lado á bê? [p=0.2] E {e}qual é o baricentro?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Ponto médio de á bê. [p=0.2] {a}Xis: menos dois mais quatro dá dois, dividido por dois dá um. [p=0.2] {b}Ípsilon: cinco mais um dá seis, dividido por dois dá três. [p=0.3] {c}Xis um, ípsilon três."),
    dict(id="s18", block="resposta", text="Baricentro. [p=0.2] {a}Xis: menos dois mais quatro mais sete dá nove, dividido por três dá três. [p=0.2] {b}Ípsilon: cinco mais um mais três dá nove, dividido por três dá três. [p=0.3] {c}Xis três, ípsilon três. [p=0.3] Quem dividiu por dois {d}esqueceu que são três vértices."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o ponto médio é a média de dois pontos, [p=0.2] {b}o baricentro é a média de três, [p=0.2] e {c}cada coordenada se calcula separada."),
    dict(id="s20", block="fim", text="Na próxima aula, você mede {a}quanto uma reta é inclinada [p=0.2] e descobre {b}se três pontos estão na mesma reta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
