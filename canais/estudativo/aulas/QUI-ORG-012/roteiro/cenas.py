# Estudativo · QUI-ORG-012 — Ponto de ebulição dos orgânicos (Química · Química Orgânica · Propriedades físicas e isomeria).
# Habilidade: ordenar hidrocarboneto, álcool e ácido pelo ponto de ebulição e dizer por que a ramificação diminui esse valor.
# Pré-requisitos: QUI-ORG-009 (funções nitrogenadas), QUI-LIG-010 (primeiro a força, depois o tamanho). Próxima: QUI-ORG-013 (solubilidade, sabão).
# Marcas: {cue} animação · [p=0.2] pausa. Temperaturas por extenso, em graus Celsius, a 1 atm (valores arredondados).
# Primeira aula do módulo Propriedades físicas e isomeria: o visual.py acrescenta a linguagem das forças entre moléculas.
# Dados (material 36): butano ≈ 0 °C (−0,5), propan-1-ol 97, ácido etanoico 118, propanona 56 (massas 58 a 60 g/mol);
# metano −161, propano −42, pentano 36, hexano 69; pentano 36, metilbutano 28, dimetilpropano ≈ 10 (todos C5H12).
# Os nomes ramificados (QUI-ORG-004) não estão em "Já ensinado": a voz diz "com um galho / com dois galhos", a tela mostra o nome.
# Questão: pentano (72 g/mol) 36 °C < butan-1-ol (74) 118 °C < ácido propanoico (74) 141 °C. Parafina > 300 °C × metanol 65 °C.
# Questão inédita, criada para esta aula.

TITULO = "Ponto de ebulição dos orgânicos"

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
    dict(id="s01", block="gancho", text="{a}Butano, propan um ol e ácido acético, o do vinagre, têm quase a mesma massa. [p=0.3] {b}Mas o butano ferve perto de zero grau, [p=0.1] {c}o propan um ol, perto de noventa e sete, [p=0.1] {d}e o ácido, a cento e dezoito. [p=0.3] {e}Quem explica essa diferença é a função."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}ordenar hidrocarboneto, álcool e ácido pelo ponto de ebulição [p=0.2] e {c}explicar por que os galhos, as ramificações da cadeia, baixam esse valor."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula de forças entre moléculas: [p=0.2] {a}ferver é afastar as moléculas umas das outras, não quebrar a molécula. [p=0.3] {b}A força mais forte é a ligação de hidrogênio, [p=0.1] {c}depois o dipolo permanente, [p=0.1] {d}e a mais fraca, o dipolo induzido. [p=0.3] {e}E a comparação segue a ordem: primeiro a força, depois o tamanho."),
    # hidrocarboneto
    dict(id="s04", block="hidrocarboneto", text="{a}Comece pelo hidrocarboneto. [p=0.2] {b}Carbono e hidrogênio têm eletronegatividades bem parecidas: [p=0.1] {c}a molécula é apolar [p=0.1] {d}e só faz dipolo induzido. [p=0.3] {e}Por isso, os pequenos são gases, como o metano e o butano do gás de cozinha."),
    dict(id="s05", block="hidrocarboneto", text="{a}Entre hidrocarbonetos do mesmo tipo, quanto maior a molécula, maior o ponto de ebulição. [p=0.2] {b}Metano, menos cento e sessenta e um graus. [p=0.1] {c}Propano, menos quarenta e dois. [p=0.1] {d}Pentano, trinta e seis. [p=0.1] {e}Hexano, sessenta e nove. [p=0.3] {f}Molécula maior tem mais superfície para o dipolo induzido agir."),
    # álcool e ácido
    dict(id="s06", block="oxigenio", text="{a}No álcool, o ó agá muda tudo. [p=0.2] {b}O agá preso ao oxigênio faz ligação de hidrogênio com o oxigênio da molécula vizinha. [p=0.3] {c}Por isso, o propan um ol ferve a noventa e sete graus, [p=0.1] {d}quase cem graus acima do butano, de massa parecida."),
    dict(id="s07", block="oxigenio", text="{a}O ácido carboxílico vai além. [p=0.2] {b}Duas moléculas se encaixam pelas carboxilas, com duas ligações de hidrogênio, [p=0.1] {c}e andam aos pares. [p=0.3] {d}Separar esses pares custa mais: [p=0.1] o ácido etanoico, o acético, ferve a cento e dezoito graus."),
    dict(id="s08", block="oxigenio", text="{a}E o aldeído, a cetona e o éter? [p=0.2] {b}Eles têm oxigênio, mas nenhum agá preso a ele. [p=0.2] {c}São polares e fazem dipolo permanente: [p=0.1] {d}ficam no meio. [p=0.2] {e}A propanona ferve a cinquenta e seis graus."),
    dict(id="s09", block="oxigenio", text="{a}Entre os compostos com oxigênio e massas parecidas, a ordem fica assim: [p=0.2] {b}embaixo, o hidrocarboneto; [p=0.1] {c}depois, aldeído, cetona e éter; [p=0.1] {d}depois, o álcool; [p=0.1] {e}e, no topo, o ácido carboxílico."),
    # galhos
    dict(id="s10", block="galhos", text="{a}E os galhos? [p=0.2] Veja três moléculas com a mesma fórmula, cê cinco agá doze. [p=0.3] {b}O pentano, em fila, ferve a trinta e seis graus. [p=0.2] {c}Com um galho, a vinte e oito. [p=0.2] {d}Com dois galhos no mesmo carbono, quase uma bolinha, a cerca de dez."),
    dict(id="s11", block="galhos", text="{a}A força é a mesma: só dipolo induzido. [p=0.2] {b}O que muda é a forma. [p=0.3] {c}A molécula comprida encosta na vizinha ao longo do corpo todo, como lápis num estojo. [p=0.3] {d}A ramificada fica mais redonda e encosta pouco, como bolas de gude. [p=0.3] {e}Menos contato, força menor, ponto de ebulição mais baixo."),
    # erro comum
    dict(id="s12", block="erro", text="{a}O erro mais comum é ordenar só pela massa. [p=0.2] {b}Pela massa, o butano e o ácido acético quase empatam. [p=0.2] {c}No ponto de ebulição, a diferença passa de cem graus. [p=0.3] {d}Com tamanhos parecidos, primeiro a força; [p=0.1] o tamanho desempata."),
    # atalho
    dict(id="s13", block="atalho", text="{a}O atalho: [p=0.1] {b}procure um agá preso a oxigênio. [p=0.2] {c}Tem a carboxila, cê ó ó agá? Fica no topo. [p=0.2] {d}Tem ó agá? Logo abaixo. [p=0.2] {e}Tem oxigênio sem agá? No meio. [p=0.2] {f}Só carbono e hidrogênio? Embaixo."),
    dict(id="s14", block="atalho", text="{a}Funciona porque a ligação de hidrogênio precisa do agá preso ao oxigênio. [p=0.3] {b}Só não vale quando os tamanhos são muito diferentes: [p=0.1] {c}a parafina da vela, só com carbono e hidrogênio, ferve muito acima do metanol, que é bem pequeno."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Pentano, butan um ol e ácido propanoico têm massas quase iguais. [p=0.3] {b}Coloque os três em ordem, do menor para o maior ponto de ebulição."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}O pentano só tem carbono e hidrogênio: [p=0.1] dipolo induzido, embaixo. [p=0.2] {b}O butan um ol tem ó agá: [p=0.1] ligação de hidrogênio, no meio. [p=0.2] {c}O ácido propanoico tem a carboxila: [p=0.1] ligações de hidrogênio aos pares, no topo. [p=0.3] {d}Os valores: trinta e seis graus, [p=0.1] cento e dezoito [p=0.1] e cento e quarenta e um."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}primeiro a força: ácido, álcool, os polares sem agá no oxigênio e, embaixo, o hidrocarboneto. [p=0.2] {b}Depois o tamanho. [p=0.2] {c}E, com a mesma fórmula, mais galhos dão menos contato e ponto de ebulição mais baixo."),
    dict(id="s19", block="fim", text="Na próxima aula, a mesma ideia explica {a}por que o etanol se mistura com a água e o hexano não, [p=0.1] {b}como medir o álcool da gasolina [p=0.1] e {c}como o sabão tira a gordura. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
