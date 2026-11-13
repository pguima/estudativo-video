# Estudativo · QUI-EQL-002 — Princípio de Le Chatelier (Química · Equilíbrio Químico · Equilíbrio e Le Chatelier).
# Habilidade: prever para que lado o equilíbrio desloca ao mudar concentração, pressão ou temperatura e dizer por que o
# catalisador não desloca, como na síntese da amônia.
# Pré-requisitos: QUI-EQL-001, QUI-CAL-011, QUI-TER-006. Próxima: QUI-EQL-003 (produto iônico da água, pH e pOH).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: N₂ + 3 H₂ ⇌ 2 NH₃, ΔH = −92 kJ; processo Haber-Bosch perto de 200 atm e 400–450 °C, com catalisador de ferro;
# 2 SO₂ + O₂ ⇌ 2 SO₃, ΔH < 0 (etapa do ácido sulfúrico). Só a temperatura muda o valor de K.

TITULO = "Princípio de Le Chatelier"

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
    dict(id="s01", block="gancho", text="{a}A amônia dos fertilizantes vem de um equilíbrio: [p=0.1] ene dois mais três agá dois formando dois ene agá três. [p=0.3] {b}Nas condições erradas, quase nada de amônia se forma. [p=0.2] {c}A indústria mexe na pressão e na temperatura e empurra o equilíbrio para o lado que interessa. [p=0.3] {d}Como saber o lado?"),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai {a}prever para que lado o equilíbrio se desloca [p=0.2] ao mudar {b}concentração, pressão ou temperatura, [p=0.2] e {c}dizer por que o catalisador não desloca."),
    # lembrete
    dict(id="s03", block="lembrete", text="{a}Você já sabe que, no equilíbrio, ida e volta têm a mesma velocidade. [p=0.2] {b}Que a reação com delta agá negativo libera calor. [p=0.2] {c}E que o catalisador baixa a energia de ativação. [p=0.2] Se faltar alguma, procure no canal."),
    # o princípio
    dict(id="s04", block="principio", text="{a}O princípio de Le Chatelier diz: [p=0.1] {b}quando você perturba um equilíbrio, ele se desloca para diminuir a perturbação. [p=0.3] {c}O equilíbrio foge da mudança. [p=0.3] {d}Deslocar para a direita é formar mais produto; [p=0.1] {e}para a esquerda, mais reagente."),
    # concentração
    dict(id="s05", block="concentracao", text="{a}Primeira perturbação: a concentração. [p=0.2] {b}Ponha mais ene dois. [p=0.1] {c}O equilíbrio consome o que chegou: [p=0.1] {d}desloca para a direita e forma mais amônia. [p=0.3] {e}Tire amônia do sistema: [p=0.1] {f}ele repõe o que saiu, e também vai para a direita."),
    dict(id="s06", block="concentracao", text="{a}A regra: [p=0.1] adicionou um gás ou uma substância dissolvida, o equilíbrio vai para o lado oposto ao dela. [p=0.2] {b}Retirou, vai para o lado dela. [p=0.2] Sólido e líquido puro não contam, porque estão fora do cá cê."),
    # pressão
    dict(id="s07", block="pressao", text="{a}Segunda: a pressão, que só importa para gases. [p=0.2] {b}Conte as moléculas de gás de cada lado pelos coeficientes. [p=0.2] {c}Na amônia, um mais três dá quatro, à esquerda; [p=0.1] {d}e duas, à direita."),
    dict(id="s08", block="pressao", text="{a}Aumentar a pressão é apertar o gás num volume menor. [p=0.2] {b}O equilíbrio alivia indo para o lado com menos moléculas de gás: [p=0.1] {c}a direita, mais amônia. [p=0.3] {d}Diminuir a pressão faz o contrário. [p=0.2] {e}E se os dois lados tiverem o mesmo número de moléculas de gás, a pressão não desloca nada."),
    # temperatura
    dict(id="s09", block="temperatura", text="{a}Terceira: a temperatura. [p=0.2] {b}A síntese da amônia tem delta agá negativo: [p=0.1] {c}a ida libera calor, [p=0.1] {d}então a volta absorve. [p=0.3] {e}Esquentar favorece o sentido que absorve calor, o endotérmico: [p=0.1] {f}aqui, a volta, e sobra menos amônia. [p=0.3] {g}Esfriar favorece o exotérmico: mais amônia."),
    dict(id="s10", block="temperatura", text="{a}A temperatura é a única perturbação que muda o valor da constante cá cê. [p=0.2] {b}As outras só fazem o equilíbrio andar até voltar ao mesmo cá cê."),
    # catalisador
    dict(id="s11", block="catalisador", text="{a}E o catalisador? [p=0.2] {b}Ele baixa a energia de ativação da ida e da volta. [p=0.2] {c}As duas aceleram juntas, [p=0.1] {d}e o equilíbrio chega mais cedo, [p=0.1] {e}mas no mesmo lugar. [p=0.2] O catalisador não desloca."),
    # a indústria
    dict(id="s12", block="haber", text="{a}Agora, a fábrica. [p=0.2] {b}Pressão alta, perto de duzentas atmosferas, empurra para a amônia. [p=0.2] {c}Temperatura baixa também empurraria, mas deixaria a reação lenta demais. [p=0.3] {d}Por isso se usa cerca de quatrocentos e cinquenta graus Celsius, um meio-termo, [p=0.1] {e}com um catalisador de ferro para compensar a lentidão."),
    # erro comum
    dict(id="s13", block="erro", text="{a}O erro comum é dizer que o catalisador aumenta a quantidade de produto. [p=0.2] {b}Não aumenta: ele só faz o equilíbrio chegar mais rápido. [p=0.2] {c}O equilíbrio não fica com mais amônia: [p=0.1] ela só sai mais rápido."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho: [p=0.2] {a}trate o calor como se fosse uma substância. [p=0.2] {b}Na amônia, que libera calor, escreva o calor do lado dos produtos. [p=0.2] {c}Esquentar é adicionar calor: [p=0.1] {d}o equilíbrio foge dele, para a esquerda. [p=0.3] {e}Assim, a temperatura segue a mesma regra da concentração. [p=0.2] {f}Só funciona se você souber o sinal do delta agá, então procure no enunciado."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Na produção do ácido sulfúrico, há este equilíbrio, tudo gás: [p=0.1] dois esse ó dois mais gás oxigênio formando dois esse ó três, [p=0.1] com delta agá negativo. [p=0.3] O que acontece com o esse ó três [p=0.1] {b}se você adicionar gás oxigênio? [p=0.2] {c}Se aumentar a pressão? [p=0.2] {d}Se esquentar? [p=0.2] {e}E se puser um catalisador?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}Adicionou oxigênio: o equilíbrio o consome e vai para a direita, [p=0.1] mais esse ó três. [p=0.3] {b}Pressão: há três moléculas de gás à esquerda e duas à direita. [p=0.1] Pressão alta vai para o lado de menos gás: [p=0.1] direita, mais esse ó três."),
    dict(id="s18", block="resposta", text="{a}Temperatura: delta agá negativo, então o calor está nos produtos. [p=0.1] Esquentar empurra para a esquerda: [p=0.1] {b}menos esse ó três. [p=0.3] {c}Catalisador: não desloca. [p=0.1] {d}A quantidade fica igual, só chega mais rápido."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}o equilíbrio foge da perturbação. [p=0.2] {b}Concentração e pressão o fazem andar; [p=0.1] {c}a temperatura também desloca e ainda muda o cá cê; [p=0.1] {d}e o catalisador não desloca nada."),
    dict(id="s20", block="fim", text="Na próxima aula, o equilíbrio da própria água: [p=0.1] {a}o produto iônico, [p=0.1] {b}o pê agá e o pê ó agá. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
