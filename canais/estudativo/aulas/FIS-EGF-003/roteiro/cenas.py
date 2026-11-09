# Estudativo · FIS-EGF-003 — Gravitação universal (Física · Equilíbrio, Gravitação e Fluidos · Equilíbrio, torque e gravitação).
# Habilidade: usar F = G·M·m/d² por proporção e achar a gravidade de um planeta.
# Pré-requisitos: FIS-EGF-002 (Kepler), FIS-DIN-004 (peso P = m·g), MAT-RAZ-010/011 (proporção ao quadrado). Próxima: FIS-EGF-013.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: G ≈ 6,67 × 10⁻¹¹ N·m²/kg² (narrado "cerca de seis vírgula sete"); raio da Terra ≈ 6.400 km; Marte: massa ≈ 0,107 da
# Terra, raio ≈ 0,53, g ≈ 3,7 m/s² (a aproximação 1/10 e 1/2 dá 4). Os números da questão são aproximados e ditos assim.

TITULO = "Gravitação universal"

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
    dict(id="s01", block="gancho", text="{a}A força que derruba uma maçã da árvore [p=0.2] é {b}a mesma que segura a Lua em volta da Terra. [p=0.3] Essa foi a grande ideia de {c}Isaac Newton. [p=0.2] E ela cabe {d}numa fórmula só."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar essa fórmula por proporção, [p=0.2] {b}sem decorar número nenhum, [p=0.2] e {c}achar a gravidade de outro planeta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}O peso: pê igual a eme vezes gê, a força com que a Terra puxa um corpo. [p=0.2] E {c}as leis de Kepler: os planetas giram em órbitas em volta do Sol. [p=0.3] Se faltar alguma, procure no canal."),
    # a lei
    dict(id="s04", block="lei", text="{a}Newton disse que todo corpo com massa atrai todo outro corpo com massa. [p=0.2] {b}Você atrai a Terra, e a Terra atrai você. [p=0.3] {c}Pela terceira lei, as duas forças têm o mesmo valor, [p=0.1] em sentidos opostos."),
    dict(id="s05", block="lei", text="{a}A força é efe igual a gê maiúsculo vezes eme maiúsculo vezes eme minúsculo, sobre dê ao quadrado. [p=0.3] {b}Eme maiúsculo e eme minúsculo são as massas dos corpos, em quilogramas. [p=0.2] {c}Dê é a distância entre os centros deles, em metros. [p=0.2] {d}E gê maiúsculo é a constante da gravitação, igual no universo todo."),
    dict(id="s06", block="lei", text="{a}Gê maiúsculo vale cerca de seis vírgula sete vezes dez elevado a menos onze, [p=0.1] no Sistema Internacional. [p=0.2] {b}Um número minúsculo. [p=0.3] Por isso {c}você não sente a atração de uma pessoa do seu lado: [p=0.2] {d}só uma massa enorme, como a de um planeta, dá uma força que se sente."),
    # proporção
    dict(id="s07", block="proporcao", text="Leia a fórmula como proporção. [p=0.2] {a}As massas estão em cima: [p=0.1] {b}dobrou uma massa, dobrou a força. [p=0.3] {c}A distância está embaixo, e ao quadrado: [p=0.2] {d}dobrou a distância, a força fica dividida por dois ao quadrado, [p=0.1] {e}quatro vezes menor."),
    dict(id="s08", block="proporcao", text="{a}Triplicou a distância? [p=0.1] {b}Força dividida por nove. [p=0.3] {c}Distância pela metade? [p=0.2] {d}Força quatro vezes maior. [p=0.3] {e}A gravidade enfraquece rápido com a distância, [p=0.1] mas {f}nunca chega a zero."),
    # gravidade de um planeta
    dict(id="s09", block="gravidade", text="E de onde vêm os dez metros por segundo ao quadrado do peso? [p=0.3] {a}O peso é a força da gravitação da Terra sobre você. [p=0.2] {b}Na superfície, a distância entre os centros é o raio da Terra, érre. [p=0.3] {c}Iguale eme vezes gê com a fórmula de Newton, [p=0.2] {d}e a sua massa corta dos dois lados."),
    dict(id="s10", block="gravidade", text="{a}Sobra a gravidade, gê minúsculo: [p=0.1] a constante vezes a massa do planeta, sobre o raio ao quadrado. [p=0.3] {b}A gravidade na superfície depende só da massa do planeta e do raio dele. [p=0.2] {c}Não depende da sua massa: [p=0.1] por isso, sem o ar, tudo cai junto."),
    dict(id="s11", block="gravidade", text="{a}Um planeta tem o dobro da massa da Terra [p=0.1] e o dobro do raio. [p=0.3] {b}A massa dobra: gravidade vezes dois. [p=0.2] {c}O raio dobra: gravidade dividida por quatro. [p=0.3] {d}Dois quartos, a metade. [p=0.2] {e}Lá, gê vale cinco metros por segundo ao quadrado."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que distância dobrada dá força pela metade. [p=0.3] {b}A distância está ao quadrado: [p=0.1] dobrou, divide por quatro. [p=0.3] E {c}a distância é medida de centro a centro. [p=0.2] {d}Um satélite a seis mil e quatrocentos quilômetros de altura [p=0.1] está a {e}doze mil e oitocentos do centro da Terra: [p=0.1] o dobro do raio. [p=0.2] {f}Lá, o peso dele é a quarta parte."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.2] {a}não substitua números. [p=0.2] Monte {b}o fator de cada grandeza: [p=0.2] {c}o fator da massa em cima, [p=0.1] {d}o fator da distância, ao quadrado, embaixo. [p=0.3] {e}Massa vezes três e distância vezes dois: [p=0.1] {f}três quartos da força."),
    dict(id="s14", block="atalho", text="Funciona porque {a}gê maiúsculo e o que não mudou cortam na comparação. [p=0.3] {b}Só precisa de gê maiúsculo quando a questão não dá nenhum caso conhecido para comparar: [p=0.2] aí, a conta com notação científica é obrigatória."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Marte tem cerca de um décimo da massa da Terra [p=0.2] {b}e metade do raio. [p=0.3] {c}Quanto vale a gravidade em Marte, aproximadamente? [p=0.2] {d}E quanto pesa lá uma pessoa de setenta quilos?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}A massa é um décimo: a gravidade fica dividida por dez. [p=0.2] {b}O raio é metade: um meio ao quadrado, um quarto, [p=0.1] embaixo. [p=0.2] Dividir por um quarto é {c}multiplicar por quatro. [p=0.3] {d}Dez, dividido por dez, vezes quatro: [p=0.1] {e}quatro metros por segundo ao quadrado. [p=0.3] O valor medido é três vírgula sete: [p=0.1] a estimativa foi boa."),
    dict(id="s18", block="resposta", text="{a}O peso lá: setenta vezes quatro, [p=0.1] {b}duzentos e oitenta newtons. [p=0.2] Na Terra, setecentos. [p=0.3] {c}A massa continua setenta quilos. [p=0.2] {d}O que muda de planeta para planeta é o peso."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}efe é gê maiúsculo vezes as massas, sobre a distância ao quadrado; [p=0.2] {b}distância dobrada, força quatro vezes menor; [p=0.2] e {c}a gravidade de um planeta depende da massa dele e do raio ao quadrado."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai usar essa força para {a}achar a velocidade de um satélite [p=0.2] e {b}entender por que o mar sobe e desce todo dia. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
