# Estudativo · MAT-TOP-011 — Elipse: equação reduzida (Matemática · Tópicos Avançados · Noções de cônicas).
# Habilidade: ler em x²/25 + y²/9 = 1 os semieixos 5 e 3 e achar os focos (±4, 0) com a² = b² + c².
# Pré-requisitos: MAT-ANA-008 (circunferência x² + y² = 25), MAT-TOP-010 (parábola: foco e diretriz). Próxima: MAT-TOP-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas "á", "bê", "cê", "xis", "ípsilon". Frações lidas com "dividido por".
# Contas: (5, 0) até (−4, 0) = 9 e até (4, 0) = 1; 9 + 1 = 10. (0, 3) até (±4, 0): r{9 + 16} = 5; 5 + 5 = 10.
#   25 = 9 + c² → c = 4. Erro: 25 + 9 = 34, r{34} ≈ 5,8 > 5. 9x² + 25y² = 225 ÷ 225 → x²/25 + y²/9 = 1.
#   Questão: x²/16 + y²/25 = 1 → a = 5 (vertical), b = 4, c² = 25 − 16 = 9, c = 3, focos (0, ±3).

TITULO = "Elipse: equação reduzida, semieixos e focos"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado dividido por vinte e cinco, [p=0.2] mais ípsilon ao quadrado dividido por nove, [p=0.2] igual a um. [p=0.3] Essa equação desenha {b}uma elipse: um círculo achatado. [p=0.3] E dá para ler nela {c}a largura, a altura {d}e dois pontos especiais, os focos, [p=0.2] em poucos segundos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê os semieixos e os focos de uma elipse [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a circunferência de centro na origem e raio cinco tem a equação xis ao quadrado mais ípsilon ao quadrado igual a vinte e cinco; [p=0.2] e {c}na parábola, cada ponto fica à mesma distância do foco e da diretriz. [p=0.3] Se faltar alguma, procure no canal."),
    # o barbante
    dict(id="s04", block="barbante", text="Pegue {a}dois pregos e um barbante com as pontas presas neles. [p=0.2] Estique o barbante com um lápis {b}e dê a volta. [p=0.3] O desenho é {c}uma elipse."),
    dict(id="s05", block="barbante", text="Os pregos são {a}os focos. [p=0.2] O barbante não muda de tamanho. [p=0.2] Então {b}a distância até um foco, mais a distância até o outro, {c}dá sempre o mesmo. [p=0.3] Na parábola, as duas distâncias eram iguais. [p=0.2] Na elipse, {d}a soma é que fica fixa."),
    dict(id="s06", block="barbante", text="Com os focos em {a}xis menos quatro e xis quatro, e um barbante de dez, [p=0.2] confira no ponto {b}xis cinco, ípsilon zero: [p=0.2] até um foco, nove; até o outro, um. [p=0.2] {c}Nove mais um, dez. [p=0.3] No ponto {d}xis zero, ípsilon três, [p=0.2] cada distância é a hipotenusa de catetos três e quatro: {e}cinco. [p=0.2] Cinco mais cinco, dez de novo."),
    # a equação
    dict(id="s07", block="equacao", text="A elipse com centro na origem tem uma equação reduzida: [p=0.2] {a}xis ao quadrado dividido por á ao quadrado, mais ípsilon ao quadrado dividido por bê ao quadrado, igual a um. [p=0.3] {b}Á e bê são os semieixos: [p=0.2] a distância do centro até a borda, {c}na horizontal {d}e na vertical."),
    dict(id="s08", block="equacao", text="Na nossa equação, {a}á ao quadrado é vinte e cinco: á é cinco. [p=0.2] {b}Bê ao quadrado é nove: bê é três. [p=0.3] A elipse vai de {c}menos cinco a cinco no eixo xis, [p=0.2] e de {d}menos três a três no eixo ípsilon. [p=0.3] Largura dez, {e}o tamanho do barbante. [p=0.2] Altura seis."),
    dict(id="s09", block="equacao", text="Por que cinco? [p=0.2] No eixo xis, {a}o ípsilon vale zero. [p=0.2] Sobra xis ao quadrado dividido por vinte e cinco igual a um. [p=0.2] Então {b}xis ao quadrado dá vinte e cinco: [p=0.2] xis é cinco ou menos cinco."),
    # os focos
    dict(id="s10", block="focos", text="E os focos? [p=0.2] Volte ao ponto {a}xis zero, ípsilon três, no alto da elipse. [p=0.2] Ele fica {b}bem no meio entre os focos. [p=0.2] Então cada distância é {c}metade do barbante: [p=0.2] metade de dez, cinco, que é o á."),
    dict(id="s11", block="focos", text="Aparece {a}um triângulo retângulo. [p=0.2] {b}Um cateto é o bê, a altura, três. [p=0.2] {c}O outro é o cê, do centro até o foco. [p=0.2] E {d}a hipotenusa é o á, cinco."),
    dict(id="s12", block="focos", text="Pitágoras: {a}á ao quadrado igual a bê ao quadrado mais cê ao quadrado. [p=0.3] {b}Vinte e cinco igual a nove mais cê ao quadrado. [p=0.2] {c}Cê ao quadrado dá dezesseis, e cê dá quatro. [p=0.3] Focos em {d}xis menos quatro e xis quatro, com ípsilon zero."),
    # em pé
    dict(id="s13", block="empe", text="E se o número maior estiver embaixo do ípsilon? [p=0.2] Em {a}xis ao quadrado dividido por nove, mais ípsilon ao quadrado dividido por vinte e cinco, igual a um, [p=0.2] a elipse {b}fica em pé. [p=0.3] {c}O semieixo maior, cinco, agora fica na vertical, [p=0.2] e continua se chamando á: o á é sempre o maior. [p=0.2] E os focos sobem para o eixo ípsilon: {d}ípsilon menos quatro e ípsilon quatro."),
    # erro
    dict(id="s14", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}tratar o á como cateto. [p=0.2] A pessoa faz {b}cê ao quadrado igual a vinte e cinco mais nove, que dá trinta e quatro. [p=0.3] Só que a raiz de trinta e quatro {c}passa de cinco: [p=0.2] o foco ficaria fora da elipse."),
    dict(id="s15", block="erro", text="Mas os pregos ficam {a}dentro do desenho. [p=0.2] O foco está sempre {b}mais perto do centro que a borda: [p=0.2] {c}cê é menor que á. [p=0.3] Na elipse, {d}a hipotenusa é o á."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}o maior número manda. [p=0.3] {b}O denominador maior é o á ao quadrado, [p=0.2] e ele diz {c}para onde a elipse se estica. [p=0.3] E o cê ao quadrado é {d}o maior menos o menor: [p=0.2] vinte e cinco menos nove dá dezesseis. [p=0.2] Cê é quatro, sem desenhar triângulo."),
    dict(id="s17", block="atalho", text="Funciona porque {a}á ao quadrado igual a bê ao quadrado mais cê ao quadrado [p=0.2] é o mesmo que {b}cê ao quadrado igual a á ao quadrado menos bê ao quadrado. [p=0.3] {c}Não compensa quando o lado direito não é um, [p=0.2] como em {d}nove xis ao quadrado mais vinte e cinco ípsilon ao quadrado igual a duzentos e vinte e cinco. [p=0.2] Aí, {e}divida tudo por duzentos e vinte e cinco primeiro."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] A elipse é {a}xis ao quadrado dividido por dezesseis, mais ípsilon ao quadrado dividido por vinte e cinco, igual a um. [p=0.3] {b}Quais são os semieixos, [p=0.2] e {c}onde ficam os focos?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}O maior denominador é vinte e cinco, embaixo do ípsilon: [p=0.2] a elipse fica em pé. [p=0.3] {b}Á é a raiz de vinte e cinco, cinco, na vertical. [p=0.2] {c}Bê é a raiz de dezesseis, quatro, na horizontal."),
    dict(id="s21", block="resposta", text="{a}Cê ao quadrado: vinte e cinco menos dezesseis dá nove, [p=0.2] e cê dá três. [p=0.3] Os focos ficam no eixo ípsilon: {b}ípsilon menos três e ípsilon três. [p=0.3] {c}Três é menor que cinco: [p=0.2] os focos estão dentro, como deve ser."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}os denominadores são os semieixos ao quadrado, [p=0.2] {b}o maior diz para onde a elipse se estica, [p=0.2] e {c}cê ao quadrado é o maior menos o menor."),
    dict(id="s23", block="fim", text="Na próxima aula, {a}o mais vira menos, [p=0.2] e a figura se abre em {b}dois pedaços: a hipérbole. [p=0.2] E você aprende a dizer, só pela equação, qual figura ela desenha. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
