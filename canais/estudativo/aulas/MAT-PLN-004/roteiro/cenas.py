# Estudativo · MAT-PLN-004 — Raízes e forma fatorada (Matemática · Polinômios · Raízes e relações de Girard).
# Habilidade: usar uma raiz dada para baixar o grau e escrever x³ − 2x² − 5x + 6 = (x − 1)(x − 3)(x + 2), sabendo que grau n dá n raízes.
# Pré-requisitos: MAT-FAT-008 (Bhaskara, delta primeiro), MAT-PLN-003 (Briot-Ruffini). Próxima: MAT-PLN-005.
# Soma e produto (MAT-FAT-011) e discriminante (MAT-FAT-009) não estão na ficha: o quociente se resolve só por Bhaskara.
# Raízes que não estão na reta (complexas, MAT-PLN-008) só são citadas como assunto de outra aula. Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; n se fala "ene".

TITULO = "Raízes e forma fatorada de um polinômio"

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
    dict(id="s01", block="gancho", text="{a}Xis ao cubo menos dois xis ao quadrado menos cinco xis mais seis igual a zero. [p=0.3] A fórmula de Bhaskara {b}não serve para grau três. [p=0.3] Mas, se alguém te contar que {c}um é raiz, [p=0.2] o problema vira uma equação do segundo grau, [p=0.2] e você acha {d}todas as raízes."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você usa uma raiz para baixar o grau [p=0.2] e escreve o polinômio {b}como uma multiplicação de parênteses."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}o Briô-Rufíni, que divide por xis menos um número, [p=0.2] e {c}a fórmula de Bhaskara, com o delta primeiro. [p=0.3] Se faltar alguma, procure no canal."),
    # raiz e divisão exata
    dict(id="s04", block="raiz", text="{a}Raiz de um polinômio é o número que faz ele dar zero. [p=0.2] O um é raiz porque {b}P de um é um menos dois menos cinco mais seis: zero. [p=0.3] E P de um é {c}o resto da divisão por xis menos um. [p=0.2] Resto zero quer dizer {d}divisão exata."),
    dict(id="s05", block="raiz", text="Sem resto, {a}o polinômio é xis menos um, vezes o quociente. [p=0.2] Pelo Briô-Rufíni da aula passada, {b}o quociente é xis ao quadrado menos xis menos seis. [p=0.3] {c}O grau caiu de três para dois. [p=0.2] É isso que se chama {d}baixar o grau."),
    # as outras raízes
    dict(id="s06", block="baixar", text="Uma multiplicação dá zero quando {a}algum fator vale zero. [p=0.2] {b}O xis menos um dá a raiz um. [p=0.2] As outras saem de {c}xis ao quadrado menos xis menos seis igual a zero."),
    dict(id="s07", block="baixar", text="{a}Á vale um, bê vale menos um, cê vale menos seis. [p=0.2] Delta, bê ao quadrado menos quatro á cê: {b}um mais vinte e quatro, vinte e cinco. [p=0.2] {c}A raiz de vinte e cinco é cinco, e menos bê é um. [p=0.3] {d}Com mais: um mais cinco, seis, dividido por dois, três. [p=0.2] {e}Com menos: um menos cinco, menos quatro, dividido por dois, menos dois."),
    # forma fatorada
    dict(id="s08", block="fatorada", text="As raízes são {a}um, três e menos dois. [p=0.2] Cada raiz vira {b}um parêntese: xis menos a raiz. [p=0.2] Com a raiz menos dois, {c}xis menos menos dois vira xis mais dois. [p=0.3] {d}Xis menos um, vezes xis menos três, vezes xis mais dois. [p=0.2] Essa é a {e}forma fatorada."),
    dict(id="s09", block="fatorada", text="Teste com dez: [p=0.2] {a}mil menos duzentos menos cinquenta mais seis, setecentos e cinquenta e seis. [p=0.2] {b}Nove vezes sete vezes doze, também setecentos e cinquenta e seis. [p=0.2] Bateu."),
    dict(id="s10", block="fatorada", text="Se o número da frente não for um, {a}ele fica na frente da forma fatorada. [p=0.2] {b}Dois xis ao quadrado menos dois tem raízes um e menos um, [p=0.2] e é igual a {c}dois, vezes xis menos um, vezes xis mais um."),
    # teorema fundamental
    dict(id="s11", block="teorema", text="Quantas raízes um polinômio pode ter? [p=0.2] O {a}teorema fundamental da álgebra responde: [p=0.2] {b}o número de raízes é igual ao grau. [p=0.2] Grau três, três raízes; grau quatro, quatro. [p=0.3] Isso contando {c}as repetidas [p=0.2] e {d}raízes que nem estão na reta, assunto de outra aula. [p=0.3] Então, na reta, são {e}no máximo tantas quanto o grau. [p=0.2] Grau três: {f}achou três raízes, acabou."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer a raiz que foi dada. [p=0.2] A pessoa resolve o quociente, acha {b}três e menos dois, e para. [p=0.3] Mas {c}o um também é raiz. [p=0.2] {d}Grau três pede três raízes: confira se estão todas."),
    # atalho
    dict(id="s13", block="atalho", text="E se ninguém der a raiz? [p=0.2] Atalho: {a}com o primeiro coeficiente igual a um e todos inteiros, [p=0.2] as raízes inteiras estão {b}entre os divisores do termo independente. [p=0.3] Aqui, {c}divisores de seis: um, dois, três, seis, e os negativos."),
    dict(id="s14", block="atalho", text="Comece pelo um, que é o mais rápido: [p=0.2] {a}P de um é só somar os coeficientes. [p=0.2] {b}Deu zero, o um é raiz. [p=0.3] Funciona porque {c}o termo independente é a multiplicação dos números dos parênteses: [p=0.2] {d}menos um vezes menos três vezes dois dá seis. [p=0.2] Cada raiz é um desses números com o sinal trocado, então divide o seis. [p=0.3] {e}Se as raízes não forem inteiras, o atalho não acha nada: [p=0.2] aí, a questão precisa dar uma raiz."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Dois é raiz de xis ao cubo menos sete xis mais seis. [p=0.2] {b}Escreva a forma fatorada."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Briô-Rufíni com o dois, sem esquecer o zero do xis ao quadrado: [p=0.2] {b}um, zero, menos sete, seis. [p=0.3] {c}Baixe o um. [p=0.2] {d}Dois mais zero, dois. [p=0.2] {e}Quatro menos sete, menos três. [p=0.2] {f}Menos seis mais seis, zero."),
    dict(id="s18", block="resposta", text="Quociente: {a}xis ao quadrado mais dois xis menos três. [p=0.2] {b}Delta: quatro mais doze, dezesseis. Raiz, quatro. [p=0.3] {c}Menos dois mais quatro, dividido por dois, um. [p=0.2] {d}Menos dois menos quatro, dividido por dois, menos três."),
    dict(id="s19", block="resposta", text="Resposta: {a}xis menos dois, vezes xis menos um, vezes xis mais três. [p=0.3] {b}Três raízes para grau três: dois, um e menos três."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}uma raiz dá uma divisão exata, [p=0.2] {b}a divisão baixa o grau, [p=0.2] e {c}cada raiz vira um parêntese."),
    dict(id="s21", block="fim", text="Na próxima aula, você vê {a}o que uma raiz repetida faz no gráfico [p=0.2] e descobre o sinal de um polinômio {b}sem abrir nada. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
