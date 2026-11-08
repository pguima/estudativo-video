# Estudativo · MAT-FAT-012 — Problemas de equação do 2º grau (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: achar dois números consecutivos com produto 156 e o instante em que h = 20t − 5t² volta a zero, descartando a resposta que não faz sentido.
# Pré-requisitos: MAT-EQU-013 (montar a equação, quatro passos), MAT-FAT-010 (Bhaskara). Próxima: MAT-FAT-013.
# Soma e produto (FAT-011) e discriminante (FAT-009) não estão nos pré-requisitos: a aula resolve só por Bhaskara e por evidência.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o coeficiente a se fala "á".

TITULO = "Problemas de equação do 2º grau"

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
    dict(id="s01", block="gancho", text="{a}Um livro aberto mostra duas páginas seguidas. [p=0.2] {b}Multiplicando os números delas, dá cento e cinquenta e seis. [p=0.3] {c}Que páginas são? [p=0.3] A equação vai dar duas respostas, [p=0.2] e {d}uma delas não serve."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você monta equações do segundo grau a partir de problemas [p=0.2] e sabe {b}qual raiz jogar fora."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}os quatro passos para montar uma equação: [p=0.2] o que você não sabe vira xis, cada informação vira conta, [p=0.2] ache o que é igual a quê, resolva e responda. [p=0.3] E {b}a fórmula de Bhaskara. [p=0.3] Se faltar alguma, procure no canal."),
    # páginas
    dict(id="s04", block="paginas", text="{a}Passo um: a primeira página é xis. [p=0.2] {b}Passo dois: a seguinte é xis mais um. [p=0.2] {c}Passo três: o produto das duas é cento e cinquenta e seis. [p=0.3] {d}Xis, vezes o parêntese xis mais um, igual a cento e cinquenta e seis."),
    dict(id="s05", block="paginas", text="Aplique a distributiva e arrume: [p=0.2] {a}xis ao quadrado mais xis menos cento e cinquenta e seis igual a zero. [p=0.3] Apareceu xis ao quadrado: {b}é do segundo grau. [p=0.2] {c}Á vale um, bê vale um, cê vale menos cento e cinquenta e seis."),
    dict(id="s06", block="paginas", text="{a}Delta: um mais seiscentos e vinte e quatro dá seiscentos e vinte e cinco. [p=0.2] {b}A raiz de seiscentos e vinte e cinco é vinte e cinco. [p=0.3] {c}Com mais: menos um mais vinte e cinco dá vinte e quatro, dividido por dois dá doze. [p=0.2] {d}Com menos: menos um menos vinte e cinco dá menos vinte e seis, dividido por dois, menos treze."),
    dict(id="s07", block="paginas", text="{a}Passo quatro: responder o que foi pedido. [p=0.2] {b}Página menos treze não existe. [p=0.2] Fica {c}xis igual a doze: páginas doze e treze. [p=0.3] Conferindo: {d}doze vezes treze dá cento e cinquenta e seis. [p=0.2] Bateu."),
    dict(id="s08", block="paginas", text="Repare: {a}menos treze e menos doze também multiplicados dão cento e cinquenta e seis. [p=0.2] Para a conta, a raiz serve. [p=0.2] {b}Quem descarta é o problema, não a conta."),
    # bola
    dict(id="s09", block="bola", text="Segundo problema. [p=0.2] Uma bola é chutada para cima. [p=0.2] A altura dela, em metros, é {a}agá igual a vinte tê menos cinco tê ao quadrado, [p=0.2] em que {b}tê é o tempo em segundos, contado a partir do chute. [p=0.3] {c}Depois de quanto tempo ela volta ao chão?"),
    dict(id="s10", block="bola", text="No chão, a altura é {a}zero. [p=0.2] {b}Vinte tê menos cinco tê ao quadrado igual a zero. [p=0.3] Não tem número sozinho: {c}é incompleta. [p=0.2] Coloque {d}cinco tê em evidência: [p=0.2] {e}cinco tê, vezes o parêntese quatro menos tê, igual a zero."),
    dict(id="s11", block="bola", text="Algum fator vale zero: {a}tê igual a zero ou tê igual a quatro. [p=0.3] Mas {b}no instante zero, a bola está saindo do pé. [p=0.2] Ela ainda nem subiu. [p=0.2] Resposta: {c}quatro segundos. [p=0.3] Conferindo: {d}vinte vezes quatro dá oitenta. [p=0.2] {e}Cinco vezes dezesseis dá oitenta. [p=0.2] Oitenta menos oitenta dá zero."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}responder com a primeira raiz que apareceu, sem voltar ao texto. [p=0.2] Na bola, quem responde {b}zero segundo diz que ela nem saiu do chão. [p=0.2] Nas páginas, {c}menos treze nem existe. [p=0.3] {d}Toda raiz passa pelo filtro do problema: [p=0.2] página, medida e quantidade não são negativas, [p=0.2] e o instante zero é a partida."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho para números seguidos: {a}procure perto da raiz do produto. [p=0.2] {b}Doze vezes doze dá cento e quarenta e quatro, [p=0.2] e {c}treze vezes treze dá cento e sessenta e nove. [p=0.2] Cento e cinquenta e seis fica entre esses resultados. [p=0.2] Teste {d}doze vezes treze: cento e cinquenta e seis."),
    dict(id="s14", block="atalho", text="Funciona porque {a}números seguidos são quase iguais, [p=0.2] e o produto deles fica entre os quadrados de cada um. [p=0.3] {b}Não compensa quando a resposta não é inteira [p=0.2] ou {c}quando os números não são vizinhos: [p=0.2] aí, monte a equação."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um terreno retangular tem {a}o comprimento cinco metros maior que a largura. [p=0.2] A área é {b}cento e cinquenta metros quadrados. [p=0.3] Área de um retângulo é {c}comprimento vezes largura. [p=0.2] {d}Quais são as medidas do terreno?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}A largura é xis, e o comprimento, xis mais cinco. [p=0.2] {b}Xis, vezes o parêntese xis mais cinco, igual a cento e cinquenta. [p=0.2] Arrumando: {c}xis ao quadrado mais cinco xis menos cento e cinquenta igual a zero."),
    dict(id="s18", block="resposta", text="{a}Delta: vinte e cinco mais seiscentos dá seiscentos e vinte e cinco. [p=0.2] Raiz: vinte e cinco. [p=0.3] {b}Menos cinco mais vinte e cinco dá vinte, dividido por dois dá dez. [p=0.2] {c}Menos cinco menos vinte e cinco dá menos trinta, dividido por dois, menos quinze."),
    dict(id="s19", block="resposta", text="{a}Largura negativa não existe. [p=0.2] Resposta: {b}dez metros de largura e quinze de comprimento. [p=0.3] Conferindo: {c}dez vezes quinze dá cento e cinquenta. [p=0.2] Quem respondeu só dez {d}esqueceu o comprimento: [p=0.2] a pergunta pedia as medidas."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}monte com os quatro passos, [p=0.2] {b}resolva [p=0.2] e {c}passe cada raiz pelo filtro do problema."),
    dict(id="s21", block="fim", text="Na próxima aula, aparecem equações {a}que não parecem do segundo grau, [p=0.2] como {b}xis elevado a quatro, menos treze xis ao quadrado, mais trinta e seis, igual a zero. [p=0.3] E {c}uma troca de letra resolve tudo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
