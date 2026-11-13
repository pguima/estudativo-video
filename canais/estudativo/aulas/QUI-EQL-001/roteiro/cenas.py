# Estudativo · QUI-EQL-001 — Equilíbrio químico e constante Kc (Química · Equilíbrio Químico · Equilíbrio e Le Chatelier).
# Habilidade: dizer por que o equilíbrio é dinâmico e escrever Kc e Kp deixando sólidos e líquidos de fora.
# Pré-requisitos: QUI-SOL-004, QUI-TER-004, QUI-CAL-014, MAT-POT-001. Próxima: QUI-EQL-009 (calcular Kc).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Primeira aula da trilha de Equilíbrio: o cabeçalho do visual.py guarda a linguagem visual da trilha (seta dupla, Kc em fração).
# Leitura para a voz: Kc = "cá cê", Kp = "cá pê"; ⇌ = "em equilíbrio com". Fatos: N₂O₄ é incolor e NO₂ é marrom (o equilíbrio
# muda de cor); garrafa fechada de refrigerante: o CO₂ sai e volta à bebida na mesma taxa (equilíbrio físico);
# CaCO₃(s) ⇌ CaO(s) + CO₂(g): Kc = [CO₂], Kp = pCO₂; C(s) + H₂O(g) ⇌ CO(g) + H₂(g) (gás de água): Kc = [CO][H₂]/[H₂O].

TITULO = "Equilíbrio químico e constante Kc"

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
    dict(id="s01", block="gancho", text="{a}Numa garrafa fechada de refrigerante, o gás carbônico sai da bebida o tempo todo. [p=0.2] {b}E volta para ela o tempo todo. [p=0.3] {c}Mesmo assim, a quantidade de gás lá dentro não muda. [p=0.3] {d}Nada parou, e nada muda. [p=0.2] Como?"),
    dict(id="s02", block="gancho", text="Isso é equilíbrio. [p=0.2] Até o fim da aula, você vai entender {a}por que ele é dinâmico [p=0.2] e escrever {b}as constantes cá cê e cá pê, [p=0.2] {c}sabendo quem fica de fora."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar: [p=0.1] {a}concentração em mol por litro, escrita entre colchetes; [p=0.2] {b}a velocidade média de uma reação; [p=0.2] {c}a pressão parcial de um gás numa mistura; [p=0.2] e {d}potência. [p=0.2] Se faltar alguma, procure no canal."),
    # reação reversível e equilíbrio dinâmico
    dict(id="s04", block="reversivel", text="{a}Muitas reações andam nos dois sentidos. [p=0.2] {b}Os reagentes formam produtos, [p=0.1] {c}e os produtos se desfazem em reagentes de novo. [p=0.3] {d}Elas se escrevem com uma seta dupla. [p=0.2] {e}Da esquerda para a direita é a ida; [p=0.1] da direita para a esquerda, a volta."),
    dict(id="s05", block="reversivel", text="Veja o ene dois ó quatro, um gás sem cor. [p=0.1] Cada molécula dele forma duas de ene ó dois, um gás marrom. [p=0.3] {a}No início, só há ene dois ó quatro, e a ida é rápida. [p=0.2] {b}O ene ó dois aparece, [p=0.1] {c}e a volta começa, devagar."),
    dict(id="s06", block="reversivel", text="{a}Com o tempo, sobra menos reagente, e menos moléculas se transformam a cada segundo: [p=0.1] a ida perde velocidade. [p=0.2] {b}Com mais produto, a volta ganha velocidade. [p=0.3] {c}Até que as duas velocidades ficam iguais. [p=0.2] {d}Isso é o equilíbrio: [p=0.1] {e}a cor para de mudar, e as concentrações ficam constantes."),
    dict(id="s07", block="reversivel", text="{a}Mas as reações não pararam. [p=0.2] {b}A cada segundo, o que se forma de um lado se desfaz do outro, na mesma quantidade. [p=0.3] {c}Por isso o equilíbrio é dinâmico. [p=0.2] {d}É como subir uma escada rolante que desce: [p=0.1] {e}se você sobe na mesma velocidade dela, fica no mesmo lugar."),
    # a constante Kc
    dict(id="s08", block="kc", text="{a}No equilíbrio, existe uma conta que sempre dá o mesmo número, naquela temperatura: [p=0.2] {b}a constante de equilíbrio, cá cê. [p=0.3] {c}Em cima, os produtos; [p=0.1] {d}embaixo, os reagentes; [p=0.2] {e}cada concentração elevada ao seu coeficiente."),
    dict(id="s09", block="kc", text="{a}No exemplo, [p=0.1] {b}cá cê é a concentração de ene ó dois ao quadrado, [p=0.1] {c}dividida pela de ene dois ó quatro. [p=0.2] {d}O dois do expoente é o coeficiente do ene ó dois."),
    dict(id="s10", block="kc", text="{a}Na síntese da amônia, ene dois mais três agá dois [p=0.1] formam dois ene agá três. [p=0.3] {b}Cá cê é a amônia ao quadrado, [p=0.1] {c}dividida pelo ene dois, [p=0.1] vezes o agá dois ao cubo. [p=0.3] {d}Cá cê grande quer dizer muito produto no equilíbrio; [p=0.1] {e}pequeno, pouco produto."),
    # quem fica de fora
    dict(id="s11", block="fora", text="{a}E quem fica de fora? [p=0.2] {b}Sólidos e líquidos puros. [p=0.2] {c}A concentração deles não muda: um pedaço de carvão é carvão puro do começo ao fim. [p=0.3] {d}Por isso, só entram gases e substâncias dissolvidas em água."),
    dict(id="s12", block="fora", text="{a}Veja o calcário aquecido. [p=0.1] O carbonato de cálcio, sólido, forma óxido de cálcio, sólido, e gás carbônico. [p=0.3] {b}Os sólidos saem, [p=0.1] {c}e o cá cê fica sendo só a concentração do gás carbônico."),
    # Kp
    dict(id="s13", block="kp", text="{a}Quando há gases, existe outra constante: cá pê. [p=0.2] {b}No lugar das concentrações, entram as pressões parciais, [p=0.1] {c}a parte da pressão total que cabe a cada gás. [p=0.3] {d}A forma é a mesma: produtos em cima, reagentes embaixo, coeficientes no expoente. [p=0.2] {e}No calcário, cá pê é só a pressão do gás carbônico."),
    # erro comum
    dict(id="s14", block="erro", text="{a}O erro comum é achar que, no equilíbrio, reagentes e produtos têm a mesma concentração. [p=0.3] {b}Não: o que fica igual são as velocidades da ida e da volta. [p=0.2] {c}As concentrações só param de mudar, [p=0.1] {d}e podem ser bem diferentes umas das outras."),
    # atalho
    dict(id="s15", block="atalho", text="O atalho para escrever qualquer constante: [p=0.2] {a}produtos sobre reagentes, [p=0.1] {b}coeficiente vira expoente, [p=0.1] {c}e só entra o que é gás ou está dissolvido. [p=0.3] {d}Colchete é cá cê; pressão é cá pê, e cá pê só aceita gás."),
    dict(id="s16", block="atalho", text="Funciona para qualquer equação balanceada. [p=0.2] {a}Só cuidado com a água: [p=0.1] {b}líquida, fica de fora; [p=0.1] {c}vapor, entra."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Carvão em brasa e vapor de água formam monóxido de carbono e gás hidrogênio. [p=0.3] {b}Cê sólido mais agá dois ó gás, em equilíbrio com cê ó gás mais agá dois gás. [p=0.3] {c}Escreva cá cê e cá pê."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="{a}O carvão é sólido: fica de fora. [p=0.2] {b}A água, aqui, é vapor, um gás: entra. [p=0.3] {c}Cá cê é a concentração do monóxido de carbono vezes a do gás hidrogênio, [p=0.1] dividida pela do vapor de água. [p=0.3] {d}Cá pê tem a mesma forma, com as pressões parciais. [p=0.2] {e}Todos os coeficientes são um, então não aparece expoente."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}no equilíbrio, ida e volta têm a mesma velocidade, e as concentrações param de mudar. [p=0.2] {b}A constante é produtos sobre reagentes, com os coeficientes no expoente, [p=0.1] sem sólidos nem líquidos puros."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai {a}calcular o cá cê com números, [p=0.2] {b}montando o quadro início, reage, equilíbrio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
