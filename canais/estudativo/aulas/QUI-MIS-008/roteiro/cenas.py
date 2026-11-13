# Estudativo · QUI-MIS-008 — Destilação: simples e fracionada (Química · Matéria e Misturas · Separação de misturas).
# Habilidade: escolher entre evaporação, destilação simples e destilação fracionada, explicar como o petróleo é separado e
# dizer por que o álcool 96% não se purifica só por destilação.
# Pré-requisitos: QUI-MIS-004, QUI-MIS-007. Próxima: QUI-MIS-009 (praticando: escolher o método de separação).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: etanol ferve a cerca de 78 °C, água a 100 °C, acetona a cerca de 56 °C (miscível com água); no condensador a água
# fria entra por baixo e sai por cima; na torre do petróleo saem, de cima para baixo: gás de cozinha, gasolina, querosene,
# diesel, óleos lubrificantes e, no fundo, o asfalto; o petróleo é mistura de substâncias de carbono e hidrogênio; o
# álcool 96% é azeotrópico (vapor com a mesma composição do líquido), o álcool quase puro sai por outro processo.

TITULO = "Destilação: simples e fracionada"

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
    dict(id="s01", block="gancho", text="{a}Na salina, o sol tira a água do mar e o sal fica no chão. [p=0.3] {b}Mas e se você quisesse a água, e não o sal? [p=0.3] {c}Muitos navios, no meio do oceano, fazem isso todo dia."),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai escolher entre {b}evaporação, destilação simples e destilação fracionada, [p=0.2] {c}ver como o petróleo vira gasolina [p=0.2] e {d}descobrir por que o álcool para nos noventa e seis por cento."),
    # lembrete
    dict(id="s03", block="lembrete", text="Três lembretes. [p=0.2] {a}Filtro não separa mistura homogênea, como água com sal. [p=0.3] {b}Vaporização é de líquido para gás; condensação, de gás para líquido. [p=0.3] {c}E cada substância tem o seu ponto de ebulição: a temperatura em que ferve."),
    # evaporação
    dict(id="s04", block="evaporar", text="{a}O jeito mais simples é a evaporação. [p=0.2] {b}Deixe a água salgada ao sol ou no fogo: [p=0.1] {c}a água vai embora para o ar, e o sal fica. [p=0.3] {d}É a salina. [p=0.2] {e}Mas a água se perde: só serve quando você quer o sólido."),
    # destilação simples
    dict(id="s05", block="simples", text="Para guardar a água, use a {a}destilação simples. [p=0.3] {b}A água salgada vai num balão de vidro e é aquecida. [p=0.2] {c}A água ferve, [p=0.1] {d}e o vapor sobe e entra num tubo comprido, o condensador."),
    dict(id="s06", block="simples", text="{a}Em volta do condensador corre água fria, que entra por baixo e sai por cima. [p=0.3] {b}O vapor esfria, condensa {c}e pinga no frasco do outro lado: [p=0.1] {d}é a água destilada. [p=0.3] {e}O sal, que não ferve nessa temperatura, fica no balão."),
    dict(id="s07", block="simples", text="{a}A destilação simples serve para separar um sólido dissolvido de um líquido, [p=0.1] {b}ficando com os dois. [p=0.3] É um dos jeitos de um navio tirar água doce da água do mar."),
    # fracionada
    dict(id="s08", block="fracionada", text="E se forem dois líquidos misturados, {a}como álcool e água? [p=0.3] {b}Ambos fervem: o álcool a setenta e oito graus, a água a cem. [p=0.3] Na destilação simples, os vapores sairiam juntos."),
    dict(id="s09", block="fracionada", text="{a}A destilação fracionada põe uma coluna cheia de obstáculos de vidro entre o balão e o condensador. [p=0.3] {b}Na subida, o vapor do líquido que ferve mais fácil segue subindo, [p=0.1] {c}e o do outro condensa e volta para o balão."),
    dict(id="s10", block="fracionada", text="{a}Sai primeiro o líquido de menor ponto de ebulição: o álcool, ainda com um pouco de água, e já vamos ver por quê. [p=0.3] {b}O termômetro no alto da coluna marca setenta e oito graus enquanto ele sai. [p=0.3] {c}Quando a temperatura pula para perto de cem, é a água que começou a passar: [p=0.1] {d}hora de trocar o frasco."),
    # petróleo
    dict(id="s11", block="petroleo", text="{a}O petróleo é uma mistura de milhares de substâncias feitas de carbono e hidrogênio. [p=0.3] {b}Ele é separado numa destilação fracionada gigante: a torre da refinaria."),
    dict(id="s12", block="petroleo", text="{a}O petróleo entra aquecido embaixo, [p=0.1] {b}e a torre é mais quente no pé e mais fria no topo. [p=0.3] {c}Cada parte condensa na altura em que a torre está mais fria que o ponto de ebulição dela."),
    dict(id="s13", block="petroleo", text="{a}No topo, saem os gases, como o gás de cozinha. [p=0.2] {b}Descendo, a gasolina, [p=0.1] {c}o querosene dos aviões, [p=0.1] {d}o óleo diesel [p=0.1] {e}e os óleos lubrificantes. [p=0.2] {f}No fundo, fica o asfalto. [p=0.3] {g}Quanto mais alto na torre, menor o ponto de ebulição."),
    # álcool 96
    dict(id="s14", block="alcool", text="Agora, o mistério do álcool. [p=0.2] {a}Destilando álcool com água, você chega a noventa e seis por cento de álcool, [p=0.1] {b}e não passa disso. [p=0.3] {c}Lembra da mistura azeotrópica? [p=0.2] {d}É ela: ferve numa temperatura fixa, como se fosse pura."),
    dict(id="s15", block="alcool", text="{a}Nesse ponto, o vapor tem a mesma composição do líquido: [p=0.1] {b}noventa e seis por cento no balão, noventa e seis no vapor. [p=0.3] {c}Destilar de novo não muda nada. [p=0.3] {d}Para tirar o resto da água, é preciso outro processo, com outra substância."),
    # atalho
    dict(id="s16", block="atalho", text="O atalho de prova: {a}pergunte o que você quer guardar. [p=0.3] {b}Só o sólido dissolvido: evaporação. [p=0.2] {c}O líquido, ou os dois: destilação simples. [p=0.2] {d}Dois ou mais líquidos que se misturam: fracionada, [p=0.1] {e}e sai primeiro o de menor ponto de ebulição."),
    dict(id="s17", block="atalho", text="Funciona porque {a}os três usam a mesma diferença: [p=0.1] {b}um componente ferve e o outro não, ou ferve depois. [p=0.3] {c}Não funciona na mistura azeotrópica: [p=0.1] ali, os dois fervem juntos."),
    # erro
    dict(id="s18", block="erro", text="O erro mais comum é {a}achar que, na fracionada, sai primeiro o mais pesado. [p=0.3] {b}Quem manda é o ponto de ebulição: [p=0.1] {c}sai primeiro quem ferve mais fácil. [p=0.3] {d}Na torre do petróleo, as moléculas maiores também fervem mais tarde, [p=0.1] e por isso parece que é o peso. [p=0.2] {e}Mas quem decide é sempre o ponto de ebulição."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] {a}Acetona e água se misturam completamente. [p=0.2] {b}A acetona ferve a cinquenta e seis graus; a água, a cem. [p=0.3] {c}Que método separa as duas? [p=0.2] {d}Qual sai primeiro? [p=0.2] {e}E o que o termômetro marca enquanto ela sai?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s21", block="resposta", text="{a}Dois líquidos misturados: [p=0.1] {b}destilação fracionada. [p=0.3] {c}Sai primeiro a acetona, que ferve mais fácil, [p=0.2] {d}com o termômetro marcando cinquenta e seis graus. [p=0.3] {e}Quem escolheu a simples veria os dois vapores saírem misturados."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: [p=0.1] {a}evaporação guarda o sólido; [p=0.2] {b}destilação simples guarda o líquido; [p=0.2] {c}fracionada separa líquidos que se misturam, do menor ponto de ebulição para o maior; [p=0.2] e {d}a azeotrópica não se separa só destilando."),
    dict(id="s23", block="fim", text="Na próxima aula, você junta tudo: [p=0.2] {a}a ordem certa dos métodos para separar uma mistura de três componentes. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
