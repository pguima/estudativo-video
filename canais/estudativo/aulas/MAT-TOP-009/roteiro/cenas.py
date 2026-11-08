# Estudativo · MAT-TOP-009 — Posição entre duas circunferências (Matemática · Tópicos Avançados · Distância de ponto a reta e área por determinante).
# Habilidade: comparar a distância entre os centros com a soma e a diferença dos raios e dizer que centros a 5 e raios 3 e 2 dão tangentes externas.
# Pré-requisitos: MAT-ANA-010 (posições relativas de ponto e reta), MAT-FAV-002 (módulo). Próxima: MAT-TOP-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Equações lidas como na MAT-ANA-008 ("xis menos um, ao quadrado, mais ípsilon menos dois,
# ao quadrado, igual a dezesseis"). Sem letras R e r na fala: "o raio maior", "o raio menor".

TITULO = "Posição entre duas circunferências"

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
    dict(id="s01", block="gancho", text="Duas circunferências: {a}uma de raio três, {b}outra de raio dois, [p=0.2] com os centros a {c}cinco de distância. [p=0.3] Elas se cortam? [p=0.2] {d}Três mais dois dá cinco, [p=0.2] exatamente a distância: [p=0.2] {e}elas só se encostam, num ponto."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você descobre a posição entre duas circunferências comparando três números, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}ler o centro e o raio na equação reduzida; [p=0.2] {c}a distância entre dois pontos, pelo triângulo retângulo; [p=0.2] e {d}o módulo, que tira o sinal. [p=0.3] Se faltar alguma, procure no canal."),
    # os casos
    dict(id="s04", block="casos", text="Compare {a}a distância entre os centros com dois números: [p=0.2] {b}a soma dos raios [p=0.2] e {c}a diferença dos raios. [p=0.3] Imagine a circunferência menor andando em direção à maior."),
    dict(id="s05", block="casos", text="{a}Distância maior que a soma: [p=0.2] uma fica fora da outra, sem se tocar. [p=0.2] São {b}externas."),
    dict(id="s06", block="casos", text="{a}Distância igual à soma: [p=0.2] elas se encostam por fora, num ponto. [p=0.2] São {b}tangentes externas, como no gancho."),
    dict(id="s07", block="casos", text="{a}Distância maior que a diferença e menor que a soma: [p=0.2] elas se cortam em dois pontos. [p=0.2] São {b}secantes."),
    dict(id="s08", block="casos", text="{a}Distância igual à diferença: [p=0.2] a menor encosta por dentro, num ponto. [p=0.2] São {b}tangentes internas. [p=0.3] {c}Distância menor que a diferença: [p=0.2] uma fica dentro da outra, sem tocar. [p=0.3] E com distância {d}zero, os centros coincidem: [p=0.2] {e}são concêntricas."),
    dict(id="s09", block="casos", text="E por que módulo na diferença? [p=0.2] Porque {a}a diferença tem que dar positiva: [p=0.2] {b}módulo de dois menos três é um, [p=0.2] não importa a ordem dos raios."),
    dict(id="s10", block="casos", text="Conte os pontos em comum: [p=0.2] {a}secantes, dois. [p=0.2] {b}Tangentes, por fora ou por dentro, um só: [p=0.2] tangente quer dizer que encosta. [p=0.2] {c}Externas, uma dentro da outra ou concêntricas: nenhum."),
    # exemplo com equações
    dict(id="s11", block="exemplo", text="Agora, com as equações. [p=0.2] {a}Xis menos um, ao quadrado, mais ípsilon menos dois, ao quadrado, igual a dezesseis: [p=0.2] centro {b}xis um, ípsilon dois, e raio quatro. [p=0.3] {c}Xis menos quatro, ao quadrado, mais ípsilon menos seis, ao quadrado, igual a quatro: [p=0.2] centro {d}xis quatro, ípsilon seis, e raio dois."),
    dict(id="s12", block="exemplo", text="Distância entre os centros: {a}catetos três e quatro, hipotenusa cinco. [p=0.3] {b}Soma dos raios: seis. [p=0.2] {c}Diferença: dois. [p=0.3] {d}Cinco está entre dois e seis: [p=0.2] {e}as circunferências são secantes."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}comparar só com a soma. [p=0.2] Centros a {b}um de distância, raios {c}cinco e dois. [p=0.3] A pessoa vê que {d}um é menor que sete e responde: secantes. [p=0.3] Mas um também é {e}menor que a diferença, três: [p=0.2] {f}a menor está inteira dentro da maior."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}uma régua com duas marcas. [p=0.2] {b}Marque a diferença e a soma dos raios. [p=0.2] Coloque a distância na régua: [p=0.2] {c}antes da primeira marca, uma dentro da outra; [p=0.2] {d}em cima dela, tangentes internas; [p=0.2] {e}entre as marcas, secantes; [p=0.2] {f}em cima da segunda, tangentes externas; [p=0.2] {g}depois dela, externas."),
    dict(id="s15", block="atalho", text="Funciona porque, afastando os centros, {a}as marcas são os dois momentos em que elas se encostam. [p=0.3] {b}A régua diz quantos pontos de encontro existem, [p=0.2] mas não diz onde eles estão: [p=0.2] {c}para achar os pontos, a conta é outra."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Xis ao quadrado mais ípsilon ao quadrado igual a cem, [p=0.2] e {b}xis menos três, ao quadrado, mais ípsilon menos quatro, ao quadrado, igual a vinte e cinco. [p=0.3] {c}Qual é a posição entre elas?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] A primeira tem {a}centro na origem e raio dez. [p=0.2] A segunda, {b}centro xis três, ípsilon quatro, e raio cinco. [p=0.3] {c}Distância entre os centros: catetos três e quatro, cinco."),
    dict(id="s19", block="resposta", text="{a}Soma dos raios: quinze. [p=0.2] {b}Diferença: dez menos cinco, cinco. [p=0.3] {c}A distância é igual à diferença: [p=0.2] {d}tangentes internas. [p=0.2] A menor encosta por dentro, num ponto só."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}calcule a distância entre os centros, [p=0.2] {b}a soma e a diferença dos raios, [p=0.2] e {c}veja onde a distância cai na régua."),
    dict(id="s21", block="fim", text="Na próxima aula, começam as cônicas, uma família de curvas famosas. [p=0.2] A primeira é {a}a parábola, vista como os pontos que ficam à mesma distância de {b}um ponto e de uma reta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
