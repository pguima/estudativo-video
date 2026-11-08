# Estudativo · MAT-TRI-009 — Redução ao primeiro quadrante (Matemática · Trigonometria).
# Habilidade: calcular sen 150° = 1/2 e cos 240° = −1/2 trocando pelo ângulo do 1º quadrante e ajustando o sinal.
# Pré-requisitos: MAT-TRI-008 (seno no eixo vertical, cosseno no horizontal, sinais por quadrante, macete "to, se, ta, co"). Usa MAT-TRI-003 (tabela de 30°, 45° e 60°) e MAT-TRI-007 (ciclo, voltas). Próxima: MAT-TRI-010.
# Questão inédita, criada para esta aula. Seno, cosseno e tangente narrados por extenso; graus por extenso.

TITULO = "Redução ao primeiro quadrante"

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
    dict(id="s01", block="gancho", text="{a}Seno de cento e cinquenta graus. [p=0.2] Ele não está na tabela. [p=0.3] Mas a resposta é {b}um meio, o mesmo que seno de trinta. [p=0.3] {c}Todo arco do ciclo tem um parceiro no primeiro quadrante."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula seno e cosseno fora do primeiro quadrante [p=0.2] {b}com a tabela que já conhece, [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a tabela de trinta, quarenta e cinco e sessenta graus; [p=0.2] {c}o seno é a altura no ciclo, e o cosseno, a horizontal; [p=0.2] e {d}os sinais em cada quadrante: to, se, ta, co. [p=0.3] Se faltar alguma, procure no canal."),
    # segundo quadrante
    dict(id="s04", block="segundo", text="Marque {a}cento e cinquenta graus: segundo quadrante. [p=0.2] {b}Faltam trinta graus para chegar em cento e oitenta. [p=0.3] Agora, marque {c}trinta graus no primeiro quadrante. [p=0.2] {d}Os pontos ficam frente a frente, como num espelho, com o eixo vertical no meio."),
    dict(id="s05", block="segundo", text="{a}A mesma altura: seno de cento e cinquenta é igual a seno de trinta, um meio. [p=0.3] {b}Na horizontal, a mesma distância, só que à esquerda. [p=0.2] {c}Cosseno de cento e cinquenta é menos raiz de três dividido por dois."),
    dict(id="s06", block="segundo", text="Regra do segundo quadrante: {a}o parceiro é cento e oitenta menos o ângulo."),
    # terceiro quadrante
    dict(id="s07", block="terceiro", text="Agora, {a}cosseno de duzentos e quarenta graus. [p=0.2] {b}Passou de cento e oitenta: terceiro quadrante. [p=0.2] Passou quanto? [p=0.2] {c}Duzentos e quarenta menos cento e oitenta dá sessenta. [p=0.3] {d}O parceiro é sessenta graus, do lado oposto do ciclo, passando pelo centro."),
    dict(id="s08", block="terceiro", text="{a}Cosseno de sessenta é um meio. [p=0.2] {b}No terceiro quadrante, o cosseno é negativo. [p=0.2] {c}Cosseno de duzentos e quarenta dá menos um meio."),
    # quarto quadrante
    dict(id="s09", block="quarto", text="{a}No terceiro quadrante, o parceiro é o ângulo menos cento e oitenta. [p=0.2] {b}No quarto, é trezentos e sessenta menos o ângulo. [p=0.3] Por exemplo, {c}trezentos e trinta graus: trezentos e sessenta menos trezentos e trinta dá trinta. [p=0.2] {d}No quarto, o seno é negativo: seno de trezentos e trinta dá menos um meio."),
    # método
    dict(id="s10", block="metodo", text="O método tem {a}dois passos. [p=0.2] {b}Passo um, o número: pegue o valor do parceiro na tabela. [p=0.2] {c}Passo dois, o sinal: veja o quadrante do ângulo original."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}copiar o sinal do parceiro. [p=0.2] Cosseno de sessenta é positivo, [p=0.2] e a pessoa escreve {b}cosseno de duzentos e quarenta igual a um meio. [p=0.3] Mas duzentos e quarenta fica {c}à esquerda do eixo vertical: cosseno negativo. [p=0.3] {d}O parceiro dá o número. [p=0.2] {e}O quadrante original dá o sinal."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}o parceiro é a distância até o eixo horizontal. [p=0.2] Olhe para {b}cento e oitenta ou trezentos e sessenta, o que estiver mais perto. [p=0.3] {c}Cento e cinquenta está a trinta de cento e oitenta. [p=0.2] {d}Duzentos e quarenta está a sessenta de cento e oitenta. [p=0.2] {e}Trezentos e quinze está a quarenta e cinco de trezentos e sessenta."),
    dict(id="s13", block="atalho", text="Funciona porque {a}o ciclo é simétrico: [p=0.2] arcos à mesma distância do eixo horizontal têm {b}a mesma altura e a mesma horizontal. [p=0.2] Só muda o sinal. [p=0.3] {c}Não serve para arcos em cima dos eixos, como noventa ou duzentos e setenta graus: [p=0.2] leia direto no ciclo. [p=0.2] E ângulo maior que uma volta? [p=0.2] {d}Tire trezentos e sessenta primeiro."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Calcule {a}seno de duzentos e vinte e cinco graus [p=0.2] e {b}cosseno de trezentos graus."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Duzentos e vinte e cinco: terceiro quadrante. [p=0.2] {b}Duzentos e vinte e cinco menos cento e oitenta dá quarenta e cinco. [p=0.2] {c}Seno de quarenta e cinco é raiz de dois dividido por dois. [p=0.2] {d}No terceiro, seno negativo: menos raiz de dois dividido por dois."),
    dict(id="s17", block="resposta", text="{a}Trezentos: quarto quadrante. [p=0.2] {b}Trezentos e sessenta menos trezentos dá sessenta. [p=0.2] {c}Cosseno de sessenta é um meio. [p=0.2] {d}No quarto, o cosseno é positivo: cosseno de trezentos dá um meio."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}ache o parceiro no primeiro quadrante, [p=0.2] {b}pegue o valor na tabela [p=0.2] e {c}dê o sinal pelo quadrante original."),
    dict(id="s19", block="fim", text="Na próxima aula, você junta seno e cosseno numa conta só: [p=0.2] {a}seno ao quadrado mais cosseno ao quadrado dá um. [p=0.2] Com ela, se {b}o seno é três quintos no primeiro quadrante, [p=0.2] você acha {c}o cosseno: quatro quintos. [p=0.2] E a tangente volta como {d}o seno dividido pelo cosseno. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
