# Estudativo · QUI-TER-007 — Lei da velocidade e ordem de reação (Química · Termoquímica e Cinética · Cinética química).
# Habilidade: escrever v = k · [A]ᵃ · [B]ᵇ e achar as ordens em uma tabela de experimentos.
# Pré-requisitos: QUI-TER-005, MAT-POT-001, MAT-RAZ-010. Próxima: QUI-TER-008 (praticando a trilha).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Para a voz, os expoentes não são lidos como letras: "cada concentração elevada a um expoente, a ordem". Os reagentes genéricos
# da questão são X e Y, narrados "xis" e "ípsilon" (A e B soariam como artigo e "bê").
# Exemplo: 2 H₂ + 2 NO → N₂ + 2 H₂O, lei real v = k[H₂][NO]² (o erro dos coeficientes daria [H₂]²[NO]²).
# Tabela ilustrativa: (0,10; 0,10; 0,002), (0,20; 0,10; 0,004), (0,20; 0,20; 0,016) ⇒ ordem 1 em H₂, 2 em NO, global 3; k = 2.
# Questão: X triplica, v 2 → 18 (ordem 2); Y dobra, v igual (ordem 0) ⇒ v = k[X]². 2⁰ = 1 está em MAT-POT-005 (Já ensinado).

TITULO = "Lei da velocidade e ordem de reação"

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
    dict(id="s01", block="gancho", text="{a}Você dobra a concentração de um reagente, [p=0.1] e a reação fica {b}quatro vezes mais rápida. [p=0.3] {c}Dobra a de outro, [p=0.1] e {d}a velocidade nem se mexe. [p=0.3] {e}A regra que explica isso cabe numa tabela de experimentos."),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai {a}escrever a lei da velocidade [p=0.2] e {b}achar a ordem de cada reagente numa tabela."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}potência: dois ao quadrado é dois vezes dois, quatro. [p=0.2] {b}Proporcional ao quadrado: dobrou o lado, a área do quadrado quadruplica. [p=0.2] E {c}mais concentração dá mais colisões. [p=0.2] Se faltar alguma, procure no canal."),
    # a lei
    dict(id="s04", block="lei", text="{a}A velocidade depende das concentrações dos reagentes. [p=0.2] {b}A lei da velocidade escreve isso numa fórmula: [p=0.2] {c}vê igual a cá, [p=0.1] {d}vezes a concentração de cada reagente, entre colchetes, [p=0.1] {e}elevada a um expoente."),
    dict(id="s05", block="lei", text="{a}Vê é a velocidade. [p=0.2] {b}Cá é a constante de velocidade: [p=0.1] um número fixo para aquela reação, naquela temperatura. [p=0.2] {c}Mudou a temperatura, o cá muda. [p=0.3] {d}Cada expoente é a ordem daquele reagente: [p=0.1] {e}ele diz quanto aquele reagente pesa na rapidez."),
    dict(id="s06", block="lei", text="{a}E o mais importante: [p=0.1] {b}a ordem se descobre no experimento, [p=0.1] {c}não nos coeficientes da equação. [p=0.3] {d}Só a reação que acontece numa batida só, sem passos no meio, segue os coeficientes, [p=0.1] e a questão avisa quando é o caso."),
    # como achar a ordem
    dict(id="s07", block="ordem", text="Como descobrir a ordem? [p=0.2] {a}Escolha dois experimentos em que só um reagente muda. [p=0.1] Ele dobra, e você vê o que a velocidade faz. [p=0.3] {b}A velocidade não mudou: ordem zero. [p=0.1] {c}Dobrou: ordem um. [p=0.1] {d}Quadruplicou: ordem dois, [p=0.1] {e}como a área do quadrado."),
    dict(id="s08", block="ordem", text="{a}Por trás está a potência. [p=0.2] {b}Dois elevado à ordem dá o fator da velocidade. [p=0.2] {c}Dois elevado a zero dá um. [p=0.1] {d}Dois elevado a um, dois. [p=0.1] {e}Dois ao quadrado, quatro."),
    # exemplo resolvido
    dict(id="s09", block="exemplo", text="Veja a reação do agá dois com o monóxido de nitrogênio, ene ó, [p=0.1] {a}que forma ene dois e água. [p=0.3] {b}São três experimentos, cada um com concentrações diferentes, [p=0.1] {c}e a velocidade medida em cada um."),
    dict(id="s10", block="exemplo", text="{a}Do experimento um para o dois, o agá dois dobra [p=0.1] {b}e o ene ó fica igual. [p=0.2] {c}A velocidade vai de zero vírgula zero zero dois para zero vírgula zero zero quatro mol por litro por segundo: [p=0.1] {d}dobrou. [p=0.2] {e}Ordem um para o agá dois."),
    dict(id="s11", block="exemplo", text="{a}Do dois para o três, o ene ó dobra e o agá dois fica igual. [p=0.2] {b}A velocidade vai de zero vírgula zero zero quatro para zero vírgula zero um seis: [p=0.1] {c}quatro vezes. [p=0.2] {d}Ordem dois para o ene ó."),
    dict(id="s12", block="exemplo", text="{a}A lei fica: vê igual a cá, vezes a concentração de agá dois, vezes a de ene ó ao quadrado. [p=0.3] {b}Somando as ordens, um mais dois, [p=0.1] {c}a reação é de ordem três no total."),
    # erro comum
    dict(id="s13", block="erro", text="{a}O erro comum é copiar os coeficientes da equação. [p=0.2] {b}Ela tem dois agá dois e dois ene ó, [p=0.1] {c}então a pessoa eleva ambos ao quadrado. [p=0.3] {d}Mas a tabela mostra ordem um para o agá dois. [p=0.2] {e}Quem manda é o experimento."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho: [p=0.2] {a}o fator da velocidade é o fator da concentração elevado à ordem. [p=0.3] {b}Dobrou, e a velocidade foi a oito vezes? [p=0.1] Dois ao cubo: ordem três. [p=0.2] {c}Triplicou, e foi a nove vezes? [p=0.1] Três ao quadrado: ordem dois."),
    dict(id="s15", block="atalho", text="{a}E serve para prever. [p=0.2] Na lei do exemplo, {b}dobrar o agá dois e o ene ó juntos [p=0.1] {c}multiplica a velocidade por dois vezes quatro, [p=0.1] {d}oito vezes. [p=0.3] {e}Por isso a ordem vale tanto: ela diz o efeito antes de você medir."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Numa reação entre os reagentes xis e ípsilon, veja a tabela. [p=0.3] {b}Do experimento um para o dois, xis triplica e ípsilon fica igual, [p=0.1] e a velocidade vai de dois para dezoito. [p=0.3] {c}Do dois para o três, ípsilon dobra e xis fica igual, [p=0.1] e a velocidade fica em dezoito. [p=0.3] {d}Escreva a lei da velocidade."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="{a}Xis triplicou e a velocidade foi de dois para dezoito: [p=0.1] {b}nove vezes. [p=0.2] {c}Três ao quadrado dá nove: ordem dois. [p=0.3] {d}Ípsilon dobrou e a velocidade não mudou: [p=0.1] {e}ordem zero."),
    dict(id="s19", block="resposta", text="{a}A lei: vê igual a cá vezes a concentração de xis ao quadrado. [p=0.2] {b}O ípsilon some da lei, [p=0.1] porque qualquer número elevado a zero dá um."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}a lei da velocidade é cá vezes cada concentração elevada à sua ordem, [p=0.2] {b}e a ordem sai da tabela, nunca dos coeficientes."),
    dict(id="s21", block="fim", text="{a}Na próxima aula, você pratica a trilha inteira: [p=0.1] {b}delta agá, energia de ativação, velocidade e ordem, em questões de prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
