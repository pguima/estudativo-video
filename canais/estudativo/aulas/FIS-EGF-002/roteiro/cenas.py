# Estudativo · FIS-EGF-002 — Leis de Kepler (Física · Equilíbrio, Gravitação e Fluidos · Equilíbrio, torque e gravitação).
# Habilidade: descrever órbita elíptica e lei das áreas e usar a razão T²/R³ constante para comparar dois planetas.
# Pré-requisitos: FIS-CIN-018 (período), MAT-RAZ-011 (fórmula como proporção), MAT-POT-016 (raízes). Próxima: FIS-EGF-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# "Já ensinado" não tem força nem gravitação: o porquê das órbitas fica para a próxima aula. Fatos: periélio no começo de
# janeiro, afélio no começo de julho (a Terra anda cerca de 30,3 km/s e 29,3 km/s); distância Terra-Sol varia cerca de 3%
# (147 a 152 milhões de km). Kepler publicou as leis entre 1609 e 1619. Estações: inclinação do eixo (outra aula).

TITULO = "Leis de Kepler"

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
    dict(id="s01", block="gancho", text="{a}A Terra não anda em volta do Sol num círculo perfeito, [p=0.2] e {b}nem sempre na mesma velocidade. [p=0.3] {c}No começo de janeiro, ela corre mais. [p=0.2] {d}No começo de julho, mais devagar. [p=0.3] Quem descobriu isso, há mais de quatrocentos anos, foi {e}Johannes Kepler."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai descrever a órbita de um planeta, [p=0.2] {b}dizer onde ele anda mais rápido [p=0.2] e {c}comparar o ano de dois planetas com uma conta só."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}O período: o tempo de uma volta completa, a letra tê. [p=0.2] O da Terra em volta do Sol é um ano. [p=0.2] E {c}potência e raiz, para a conta. [p=0.3] Se faltar alguma, procure no canal."),
    # primeira lei
    dict(id="s04", block="elipse", text="{a}Órbita é o caminho do planeta em volta do Sol. [p=0.3] {b}A primeira lei de Kepler diz que esse caminho é uma elipse, [p=0.2] {c}um círculo achatado. [p=0.3] E o Sol {d}não fica no centro. [p=0.2] Fica num ponto deslocado para um lado, {e}chamado foco."),
    dict(id="s05", block="elipse", text="Por isso a distância ao Sol muda. [p=0.2] {a}O ponto mais perto do Sol se chama periélio. [p=0.2] {b}O mais longe, afélio. [p=0.3] {c}No desenho, a elipse está bem achatada, para dar para ver. [p=0.2] {d}A órbita da Terra é quase um círculo: [p=0.2] a distância ao Sol vai só de cento e quarenta e sete a cento e cinquenta e dois milhões de quilômetros."),
    # segunda lei
    dict(id="s06", block="areas", text="{a}A segunda lei fala da velocidade. [p=0.2] Imagine {b}uma linha ligando o Sol ao planeta. [p=0.2] Enquanto o planeta anda, {c}essa linha varre uma área, [p=0.1] como o ponteiro de um relógio. [p=0.3] {d}Em tempos iguais, a linha varre áreas iguais."),
    dict(id="s07", block="areas", text="{a}Perto do Sol, a linha é curta. [p=0.2] Para varrer a mesma área, {b}o planeta precisa percorrer um arco maior: [p=0.2] {c}ele vai mais rápido. [p=0.3] {d}Longe do Sol, a linha é comprida, [p=0.1] e {e}um arco curto já basta: ele vai devagar. [p=0.3] {f}Mais rápido no periélio, mais devagar no afélio."),
    # terceira lei
    dict(id="s08", block="terceira", text="{a}A terceira lei liga o período ao tamanho da órbita. [p=0.2] Use {b}érre, o raio médio da órbita: a distância média até o Sol. [p=0.3] {c}Para todos os planetas do Sol, [p=0.1] tê ao quadrado dividido por érre ao cubo dá {d}o mesmo número."),
    dict(id="s09", block="terceira", text="{a}Tê ao quadrado é tê vezes tê. [p=0.1] {b}Érre ao cubo é érre vezes érre vezes érre. [p=0.3] {c}Quanto mais longe do Sol, maior o ano do planeta, [p=0.2] e o ano cresce {d}mais depressa que a distância."),
    dict(id="s10", block="terceira", text="Um exemplo. [p=0.2] {a}Um planeta está quatro vezes mais longe do Sol que a Terra. [p=0.2] {b}Qual é o ano dele? [p=0.3] Use como unidade de distância {c}a distância Terra-Sol, [p=0.1] a unidade astronômica, [p=0.2] e como unidade de tempo {d}o ano da Terra. [p=0.2] Para a Terra, {e}tê é um e érre é um: [p=0.1] a razão vale um. [p=0.3] {f}Então, nessas unidades, para todo planeta do Sol, tê ao quadrado é igual a érre ao cubo."),
    dict(id="s11", block="terceira", text="{a}Érre é quatro: quatro ao cubo, sessenta e quatro. [p=0.2] {b}Tê ao quadrado é sessenta e quatro, [p=0.2] e {c}tê é a raiz de sessenta e quatro: [p=0.1] {d}oito anos. [p=0.3] Quatro vezes mais longe, {e}oito vezes mais tempo por volta."),
    dict(id="s12", block="terceira", text="Só tem um cuidado: [p=0.2] a razão é a mesma {a}para quem gira em volta do mesmo astro. [p=0.3] {b}As luas de Júpiter têm a razão delas, [p=0.2] {c}diferente da razão dos planetas em volta do Sol."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o verão acontece quando a Terra está mais perto do Sol. [p=0.3] {b}No começo de janeiro, a Terra passa pelo ponto mais perto do Sol, [p=0.2] e {c}é verão no Brasil, mas inverno na Europa. [p=0.3] {d}A distância muda pouco e não explica as estações. [p=0.2] Elas vêm {e}da inclinação do eixo da Terra, assunto de outra aula."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.2] {a}se o raio multiplica por um número, [p=0.1] {b}o período multiplica por esse número vezes a raiz dele. [p=0.3] {c}Raio quatro vezes maior: [p=0.1] quatro vezes a raiz de quatro, [p=0.1] {d}oito vezes. [p=0.2] {e}Raio nove vezes maior: [p=0.1] nove vezes três, {f}vinte e sete vezes."),
    dict(id="s15", block="atalho", text="Funciona porque {a}tê ao quadrado acompanha érre ao cubo. [p=0.2] {b}Confira com quatro: quatro ao cubo, sessenta e quatro, [p=0.1] cuja raiz é oito, [p=0.1] que é quatro vezes dois. [p=0.3] {c}Compensa quando o número tem raiz exata, como quatro, nove ou dezesseis. [p=0.2] {d}Se não tiver, faça a conta inteira."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Dois planetas giram em volta da mesma estrela. [p=0.2] {b}O raio da órbita de um é dezesseis vezes o raio da órbita do outro. [p=0.3] {c}Quantas vezes o ano do planeta mais distante é maior? [p=0.2] {d}E em que ponto da órbita ele anda mais rápido?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Mesma estrela, então a razão é a mesma. [p=0.2] {b}Raio dezesseis vezes maior: [p=0.1] {c}dezesseis vezes a raiz de dezesseis, [p=0.1] que é quatro. [p=0.2] {d}Sessenta e quatro vezes. [p=0.3] Confira: {e}sessenta e quatro ao quadrado é quatro mil e noventa e seis, [p=0.1] {f}e dezesseis ao cubo também."),
    dict(id="s19", block="resposta", text="E ele anda {a}mais rápido no ponto da órbita mais perto da estrela, [p=0.2] porque ali {b}precisa de um arco maior para varrer a mesma área."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a órbita é uma elipse, com o Sol num foco; [p=0.2] {b}áreas iguais em tempos iguais, então mais rápido perto do Sol; [p=0.2] e {c}tê ao quadrado sobre érre ao cubo é o mesmo para quem gira em volta do mesmo astro."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai ver {a}a força que segura os planetas nessas órbitas: [p=0.2] {b}a gravitação universal de Newton. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
