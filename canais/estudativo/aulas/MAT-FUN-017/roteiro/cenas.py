# Estudativo · MAT-FUN-017 — Raízes: onde a parábola corta o eixo x (Matemática · Funções · Função quadrática).
# Habilidade: achar x = 1 e x = 3 em f(x) = x² − 4x + 3 e desenhar a parábola nos três casos do discriminante.
# Pré-requisitos: MAT-FAT-009 (discriminante), MAT-FUN-016 (a parábola: concavidade e corte no eixo y). Próxima: MAT-FUN-018.
# Questão inédita, criada para esta aula. Soma e produto (MAT-FAT-011) fora da ficha: raízes só por Bhaskara.
# O atalho retoma o dos sinais contrários de a e c (MAT-FAT-009), agora com o motivo visto no gráfico.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á".
# Visual: parábola de x² − 4x + 3 com os pontos (0, 3), (1, 0) e (3, 0); três planos lado a lado: x² − 4x + 3 (corta), x² − 4x + 4 (encosta em (2, 0)), x² − 4x + 5 (não toca); depois x² + 2x − 8.

TITULO = "Raízes: onde a parábola corta o eixo x"

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
    dict(id="s01", block="gancho", text="{a}Três parábolas. [p=0.2] Uma corta o eixo xis em dois pontos. [p=0.2] Outra só encosta nele. [p=0.2] E a terceira {b}nem chega perto. [p=0.3] Uma conta que você já conhece diz qual é qual, {c}antes de desenhar."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha onde a parábola corta o eixo xis, desenha os três casos [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}a fórmula de Bhaskara, com o delta, bê ao quadrado menos quatro á cê, [p=0.2] e {b}a parábola: o sinal do á diz para onde ela abre, e o cê diz onde ela corta o eixo ípsilon. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="Todo ponto do eixo xis tem {a}ípsilon igual a zero. [p=0.2] Então, para achar onde a parábola corta esse eixo, faça {b}efe de xis igual a zero. [p=0.3] A função vira {c}uma equação do segundo grau. [p=0.2] As soluções dela são as {d}raízes da função, também chamadas de zeros."),
    # exemplo
    dict(id="s05", block="exemplo", text="Em {a}xis ao quadrado menos quatro xis mais três igual a zero, [p=0.2] á vale um, bê vale menos quatro e cê vale três. [p=0.2] O delta é bê ao quadrado, dezesseis, menos quatro vezes um vezes três, doze: {b}dezesseis menos doze dá quatro. [p=0.2] A raiz de quatro é dois. [p=0.2] Menos bê é quatro, e dois á é dois. [p=0.2] Xis é igual a {c}quatro, mais ou menos dois, dividido por dois."),
    dict(id="s06", block="exemplo", text="{a}Com mais: seis dividido por dois dá três. [p=0.2] {b}Com menos: dois dividido por dois dá um. [p=0.3] A parábola corta o eixo xis em {c}xis um, ípsilon zero, [p=0.2] e em {d}xis três, ípsilon zero."),
    dict(id="s07", block="exemplo", text="Agora dá para desenhar sem tabela comprida. [p=0.2] {a}Á positivo: abre para cima. [p=0.2] {b}Corta o eixo ípsilon no três. [p=0.2] {c}Corta o eixo xis no um e no três. [p=0.3] Três pontos e a boca: {d}a parábola está pronta."),
    # os três casos
    dict(id="s08", block="casos", text="E o delta conta mais. [p=0.2] {a}Delta positivo: duas raízes diferentes, [p=0.2] e a parábola {b}corta o eixo xis em dois pontos. [p=0.2] É o caso que você acabou de ver."),
    dict(id="s09", block="casos", text="{a}Delta zero: uma raiz só, a dupla. [p=0.2] A parábola {b}encosta no eixo em um ponto e volta. [p=0.3] Em {c}xis ao quadrado menos quatro xis mais quatro, o delta é dezesseis menos dezesseis: zero. [p=0.2] A raiz é {d}quatro dividido por dois dá dois. [p=0.2] A parábola encosta em xis dois, ípsilon zero."),
    dict(id="s10", block="casos", text="{a}Delta negativo: nenhuma raiz real. [p=0.2] A parábola {b}não toca o eixo xis. [p=0.3] Em {c}xis ao quadrado menos quatro xis mais cinco, o delta é dezesseis menos vinte: menos quatro. [p=0.2] Como o á é positivo, {d}ela fica inteira acima do eixo, sorrindo no ar."),
    dict(id="s11", block="casos", text="Com á negativo, os três casos se repetem {a}de cabeça para baixo. [p=0.2] Com delta negativo, a parábola fica {b}inteira abaixo do eixo."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é pensar que, com {a}delta negativo, a parábola não existe. [p=0.2] Ela existe, sim. [p=0.2] Em xis ao quadrado menos quatro xis mais cinco, {b}efe de zero dá cinco, [p=0.2] e {c}efe de dois dá um. [p=0.3] Os pontos estão lá. [p=0.2] O que não existe é {d}o lugar em que ela toca o eixo xis."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, e desta vez dá para ver o motivo. [p=0.2] {a}Se á e cê têm sinais contrários, a parábola corta o eixo xis em dois pontos, sem conta. [p=0.3] Em {b}xis ao quadrado mais dois xis menos oito, o á é positivo e o cê é negativo."),
    dict(id="s14", block="atalho", text="Olhe o desenho. [p=0.2] {a}Á positivo: ela abre para cima. [p=0.2] {b}Cê negativo: ela cruza o eixo ípsilon abaixo do eixo xis. [p=0.2] Um sorriso que passa por baixo do eixo {c}precisa cruzar o eixo duas vezes para subir dos dois lados. [p=0.3] Não compensa com sinais iguais: {d}aí, calcule o delta."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Onde a parábola de {a}efe de xis igual a xis ao quadrado menos seis xis mais oito corta o eixo xis? [p=0.3] E a parábola de {b}gê de xis igual a menos xis ao quadrado mais dois xis menos um: [p=0.2] {c}corta, encosta ou não toca o eixo xis?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Em efe, o delta é {a}trinta e seis menos trinta e dois dá quatro. [p=0.2] Xis é igual a seis, mais ou menos dois, dividido por dois: {b}quatro ou dois. [p=0.2] A parábola corta o eixo xis {c}no dois e no quatro."),
    dict(id="s18", block="resposta", text="Em gê, á vale menos um e cê vale menos um. [p=0.2] Sinais iguais: o atalho não decide. [p=0.2] Delta: {a}dois ao quadrado, quatro, [p=0.2] menos quatro vezes, abre parênteses, menos um, fecha parênteses, vezes, abre parênteses, menos um, fecha parênteses. [p=0.2] Quatro menos quatro: {b}zero. [p=0.3] A raiz é menos dois dividido por menos dois: {c}um. [p=0.2] A parábola abre para baixo e {d}encosta no eixo em xis um, ípsilon zero."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}raiz é onde a parábola toca o eixo xis, [p=0.2] e {b}o sinal do delta diz se ela corta, encosta ou não toca."),
    dict(id="s20", block="fim", text="Na próxima aula, o ponto mais importante da parábola: {a}o vértice, onde ela faz a curva. [p=0.2] Nesta parábola, ele fica {b}bem no meio do um e do três. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
