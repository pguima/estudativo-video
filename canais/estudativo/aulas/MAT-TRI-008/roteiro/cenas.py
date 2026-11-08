# Estudativo · MAT-TRI-008 — Seno, cosseno e tangente no ciclo (Matemática · Trigonometria).
# Habilidade: ler o seno no eixo vertical e o cosseno no horizontal, dizer que sen 90° = 1 e cos 180° = −1 e dar o sinal de cada um em cada quadrante.
# Pré-requisitos: MAT-TRI-007 (ciclo de raio 1, origem à direita, sentido anti-horário, quadrantes). Usa MAT-TRI-001 (razões; tangente = seno ÷ cosseno), MAT-TRI-003 (sen 30° = 1/2) e MAT-NUM-017 (regra de sinais). Próxima: MAT-TRI-009.
# Questão inédita, criada para esta aula. Seno, cosseno e tangente narrados por extenso; graus por extenso. Ponto do ciclo narrado "pê".

TITULO = "Seno, cosseno e tangente no ciclo"

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
    dict(id="s01", block="gancho", text="{a}Cosseno de cento e oitenta graus. [p=0.2] Nenhum triângulo retângulo tem um ângulo de cento e oitenta. [p=0.3] Mesmo assim, {b}a resposta existe: [p=0.2] {c}menos um. [p=0.3] O segredo é ler {d}o ciclo trigonométrico."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê seno e cosseno de qualquer arco direto no ciclo [p=0.2] e sabe {b}o sinal de cada um, com um macete."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}seno é o oposto dividido pela hipotenusa, e cosseno, o adjacente dividido pela hipotenusa; [p=0.2] e {c}o ciclo trigonométrico: raio um, partida à direita, giro no anti-horário. [p=0.3] Se faltar alguma, procure no canal."),
    # leitura
    dict(id="s04", block="leitura", text="Marque {a}um arco no primeiro quadrante, com a ponta no ponto pê. [p=0.2] {b}Desça uma linha de pê até o eixo xis. [p=0.2] Nasce {c}um triângulo retângulo, [p=0.2] e {d}a hipotenusa é o raio: um."),
    dict(id="s05", block="leitura", text="{a}O seno é o oposto dividido por um: [p=0.2] {b}é a própria altura de pê. [p=0.3] {c}O cosseno é o adjacente dividido por um: [p=0.2] {d}é a distância de pê na horizontal."),
    dict(id="s06", block="leitura", text="Então: {a}o seno se lê no eixo vertical, o ípsilon. [p=0.2] {b}O cosseno se lê no eixo horizontal, o xis. [p=0.3] Em trinta graus, pê fica {c}na altura um meio: [p=0.2] {d}seno de trinta, um meio, como na tabela."),
    # pontos nos eixos
    dict(id="s07", block="eixos", text="A vantagem: {a}essa leitura vale para qualquer arco, mesmo sem triângulo. [p=0.3] {b}Em noventa graus, pê está no topo: altura um, horizontal zero. [p=0.2] {c}Seno de noventa dá um. [p=0.2] {d}Cosseno de noventa dá zero."),
    dict(id="s08", block="eixos", text="{a}Em cento e oitenta graus, pê está à esquerda, no menos um do eixo xis. [p=0.2] {b}Cosseno de cento e oitenta dá menos um. [p=0.2] {c}Seno de cento e oitenta dá zero: não há altura nenhuma. [p=0.3] Como o raio é um, {d}seno e cosseno ficam sempre entre menos um e um."),
    # sinais
    dict(id="s09", block="sinais", text="Agora, os sinais. [p=0.2] {a}Acima do eixo xis, a altura é positiva. [p=0.2] {b}Seno positivo no primeiro e no segundo quadrantes, [p=0.2] {c}negativo no terceiro e no quarto."),
    dict(id="s10", block="sinais", text="{a}À direita do eixo ípsilon, a horizontal é positiva. [p=0.2] {b}Cosseno positivo no primeiro e no quarto quadrantes, [p=0.2] {c}negativo no segundo e no terceiro."),
    dict(id="s11", block="sinais", text="E a tangente? [p=0.2] {a}Tangente é o seno dividido pelo cosseno. [p=0.2] Pela regra de sinais: [p=0.2] {b}sinais iguais, positiva, no primeiro e no terceiro quadrantes. [p=0.2] {c}Sinais diferentes, negativa, no segundo e no quarto. [p=0.3] {d}Em noventa graus, o cosseno é zero, e não se divide por zero: a tangente de noventa não existe."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}trocar os eixos. [p=0.2] Seno de cento e oitenta: a pessoa olha a horizontal e responde {b}menos um. [p=0.3] Mas seno é altura, [p=0.2] e em cento e oitenta pê está {c}em cima do eixo xis: o seno dá zero. [p=0.3] Para não trocar: {d}seno sobe e desce, cosseno vai e vem."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o macete dos sinais: {a}to, se, ta, co. [p=0.3] {b}Primeiro quadrante: todos positivos. [p=0.2] {c}Segundo: só o seno. [p=0.2] {d}Terceiro: só a tangente. [p=0.2] {e}Quarto: só o cosseno. [p=0.2] Sempre na ordem do anti-horário."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o seno é positivo em cima, [p=0.2] {b}o cosseno, à direita, [p=0.2] e {c}a tangente segue a regra de sinais. [p=0.3] {d}Não serve para arcos em cima dos eixos, como noventa ou cento e oitenta graus: [p=0.2] aí, um deles é zero, e zero não tem sinal. [p=0.2] {e}Leia direto no ciclo."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Para o arco de {a}duzentos graus, [p=0.2] diga {b}o sinal do seno, do cosseno e da tangente. [p=0.3] {c}E quanto dá o seno de duzentos e setenta graus?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Duzentos graus passa de cento e oitenta e não chega a duzentos e setenta: terceiro quadrante. [p=0.2] {b}Embaixo: seno negativo. [p=0.2] {c}À esquerda: cosseno negativo. [p=0.2] {d}Negativo dividido por negativo: tangente positiva. [p=0.2] Bate com o macete: {e}no terceiro, só a tangente."),
    dict(id="s18", block="resposta", text="{a}Duzentos e setenta graus é o ponto mais baixo do ciclo. [p=0.2] {b}A altura ali é menos um. [p=0.2] {c}O seno de duzentos e setenta dá menos um."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}seno é a altura, no eixo vertical. [p=0.2] {b}Cosseno é a horizontal, no eixo xis. [p=0.2] {c}To, se, ta, co dá os sinais."),
    dict(id="s20", block="fim", text="Na próxima aula, você calcula {a}seno de cento e cinquenta graus e cosseno de duzentos e quarenta graus [p=0.2] {b}trocando cada um por um ângulo do primeiro quadrante [p=0.2] e {c}ajustando o sinal. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
