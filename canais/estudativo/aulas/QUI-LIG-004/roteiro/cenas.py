# Estudativo · QUI-LIG-004 — Qual é a ligação e o que ela explica (Química · Ligações Químicas · Ligações iônica, covalente e metálica).
# Habilidade: dizer se NaCl, H₂O e Fe têm ligação iônica, covalente ou metálica e prever quem conduz eletricidade, em que
# condição, e quem tem ponto de fusão alto.
# Pré-requisitos: QUI-LIG-001, QUI-LIG-002, QUI-LIG-003. Próxima: QUI-LIG-005 (praticando: tipos de ligação).
# Marcas: {cue} animação · [p=0.2] pausa. Questão inédita, criada para esta aula. Fe = "éfe é".
# Fatos: PF NaCl 801 °C; Fe 1538 °C; gelo 0 °C; Hg líquido (PF −39 °C); água pura quase não conduz, a da torneira conduz pelos
# sais dissolvidos; grafite (carbono) conduz. Questão: X = alumínio (PF 660 °C, conduz sólido); Y = KCl (PF 770 °C, conduz
# só fundido); Z = etanol (PF −114 °C, não conduz). "Ponto de fusão" explicado na hora (QUI-MIS-003 não está em "Já ensinado").
# Forças entre moléculas = outra aula (QUI-LIG-009).

TITULO = "Qual é a ligação e o que ela explica"

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
    dict(id="s01", block="gancho", text="{a}Três materiais da cozinha: o sal, o gelo e a panela de ferro. [p=0.3] {b}Qual deles conduz eletricidade sólido? [p=0.2] {c}Qual só conduz derretido? [p=0.2] {d}E qual derrete mais fácil? [p=0.3] {e}A resposta está no tipo de ligação de cada um."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer {b}a ligação de uma substância pelos elementos, [p=0.2] e {c}prever quem conduz, em que condição, e quem só derrete em temperatura alta. [p=0.2] E ainda leva {d}o atalho que a prova mais cobra."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você já viu as três ligações. [p=0.2] {a}Na iônica, o metal entrega elétrons ao ametal, e os íons se atraem. [p=0.2] {b}Na covalente, ametais dividem pares e formam moléculas. [p=0.2] {c}Na metálica, íons positivos ficam num mar de elétrons. [p=0.2] Se alguma travar, procure no canal."),
    # qual é a ligação
    dict(id="s04", block="regra", text="Para saber qual é, olhe {a}os elementos. [p=0.2] {b}Metal com ametal: iônica. [p=0.2] {c}Ametal com ametal: covalente. [p=0.2] {d}Metal sozinho, ou metal com metal: metálica. [p=0.3] {e}O hidrogênio entra como ametal."),
    dict(id="s05", block="regra", text="{a}Ene á cê éle: sódio é metal, cloro é ametal. [p=0.1] Iônica. [p=0.3] {b}Agá dois ó: hidrogênio e oxigênio. [p=0.1] Covalente. [p=0.3] {c}E o ferro, sozinho: [p=0.1] metálica."),
    # condução
    dict(id="s06", block="conduz", text="Para conduzir eletricidade, {a}é preciso carga que possa andar. [p=0.3] {b}No ferro, os elétrons soltos andam sempre: [p=0.1] {c}conduz sólido e derretido."),
    dict(id="s07", block="conduz", text="{a}No sal, há cargas: os íons. [p=0.2] {b}Mas, no sólido, cada íon está preso no seu lugar do retículo. [p=0.1] {c}Sólido, não conduz. [p=0.3] {d}Derreta o sal, ou dissolva na água, [p=0.1] e {e}os íons ficam livres para andar: [p=0.1] {f}aí conduz."),
    dict(id="s08", block="conduz", text="{a}Na água pura, só há moléculas inteiras, sem carga sobrando. [p=0.2] {b}Ela quase não conduz. [p=0.3] {c}A água da torneira conduz porque leva sais dissolvidos, [p=0.1] e os íons desses sais é que andam."),
    # ponto de fusão
    dict(id="s09", block="fusao", text="E o ponto de fusão, {a}a temperatura em que o sólido derrete? [p=0.3] {b}Derreter o sal é desmontar o retículo, [p=0.1] com íons opostos se atraindo forte: [p=0.1] {c}oitocentos e um graus. [p=0.3] {d}Os metais também costumam derreter só em temperatura alta: [p=0.1] o ferro, {e}a mil quinhentos e trinta e oito graus. [p=0.3] A exceção famosa é {f}o mercúrio, líquido na temperatura ambiente."),
    dict(id="s10", block="fusao", text="{a}Já o gelo derrete a zero grau. [p=0.2] Por quê, se a ligação entre hidrogênio e oxigênio é forte? [p=0.3] {b}Porque derreter o gelo não quebra essa ligação. [p=0.2] {c}Só afasta uma molécula da outra. [p=0.3] {d}As forças entre moléculas são bem mais fracas, [p=0.1] e são assunto de outra aula."),
    dict(id="s11", block="fusao", text="{a}Juntando tudo: [p=0.2] {b}iônico: ponto de fusão alto; conduz derretido ou na água, não sólido. [p=0.3] {c}Covalente feito de moléculas, que se chama molecular: [p=0.1] ponto de fusão baixo; não conduz puro. [p=0.3] {d}Metálico: conduz sólido e derretido; quase sempre, ponto de fusão alto."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que, como o sal tem íons, ele conduz sempre. [p=0.3] {b}Ligue um cristal de sal numa pilha com uma lâmpada: [p=0.1] {c}ela não acende. [p=0.2] {d}Íon preso não leva corrente. [p=0.3] {e}Ponha o sal na água, e a lâmpada acende."),
    # atalho
    dict(id="s13", block="atalho", text="A prova costuma fazer o caminho inverso: [p=0.1] {a}descreve o comportamento e pergunta a ligação. [p=0.3] O atalho é olhar a condução. [p=0.2] {b}Conduz sólido? Metálica. [p=0.3] {c}Não conduz sólido, mas conduz derretido? Iônica. [p=0.3] {d}Não conduz e derrete fácil? Molecular."),
    dict(id="s14", block="atalho", text="Funciona porque {a}elétron solto quase só existe no metal, [p=0.1] e {b}íon preso só se solta quando o sólido se desfaz. [p=0.3] {c}Conduzir na água não serve de prova: [p=0.1] alguns moleculares, como certos ácidos, também conduzem, e isso é assunto de outra aula. [p=0.3] {d}E o grafite, da ponta do lápis, é carbono, um ametal, e conduz: [p=0.1] um caso especial."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}O material xis derrete a seiscentos e sessenta graus e conduz sólido. [p=0.3] {b}O ípsilon derrete a setecentos e setenta graus, não conduz sólido, mas conduz derretido. [p=0.3] {c}O zê derrete a cento e catorze graus negativos e não conduz. [p=0.3] {d}Qual é a ligação de cada um?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá, pela condução. [p=0.2] {a}Xis conduz sólido: metálico. [p=0.1] É o alumínio. [p=0.3] {b}Ípsilon só conduz derretido: iônico, com os íons presos no sólido. [p=0.1] É o cloreto de potássio, um sal. [p=0.3] {c}Zê não conduz e derrete muito abaixo de zero: covalente, feito de moléculas. [p=0.1] É o álcool comum."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}metal com ametal é iônica, [p=0.1] ametal com ametal, covalente, [p=0.1] metal com metal, metálica. [p=0.2] {b}E a ligação diz o comportamento: [p=0.1] {c}quem conduz, quando conduz, e quem aguenta calor."),
    dict(id="s19", block="fim", text="Na próxima aula, {a}você pratica tudo isso: [p=0.1] {b}monta fórmulas e prevê propriedades em questões de prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
