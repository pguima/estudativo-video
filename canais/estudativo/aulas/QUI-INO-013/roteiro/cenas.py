# Estudativo · QUI-INO-013 — Brønsted-Lowry e Lewis (Química · Funções e Reações Inorgânicas · Ácidos, bases, sais e óxidos).
# Habilidade: apontar pares conjugados e dizer o que é um ácido de Lewis.
# Pré-requisitos: QUI-INO-001, QUI-INO-002, QUI-LIG-002. Próxima: QUI-INO-006 (praticando o módulo).
# Narração: "Brônsted" (grafia para a voz; na tela, Brønsted). NH₃ = "ene agá três", NH₄⁺ = "ene agá quatro mais",
# H₃O⁺ = "agá três ó mais", BF₃ = "bê éfe três", HNO₃ = "agá ene ó três", NO₃⁻ = "ene ó três menos".
# Fatos: Johannes Brønsted (dinamarquês) e Thomas Lowry (inglês), 1923; Gilbert Lewis (americano), também 1923.
# NH₃ + H₂O → NH₄⁺ + OH⁻ (a amônia deixa a água básica). HCl + H₂O → H₃O⁺ + Cl⁻. BF₃: o boro tem 6 elétrons em volta e
# aceita o par livre do N da amônia (NH₃BF₃). Água = anfótera (doa ou recebe H⁺). Equilíbrio (⇌) é de outra aula: as
# reações aparecem com seta simples. Questão inédita: HNO₃ + H₂O → H₃O⁺ + NO₃⁻; H⁺ + H₂O → H₃O⁺ (H⁺ = ácido de Lewis).

TITULO = "Brønsted-Lowry e Lewis"

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
    dict(id="s01", block="gancho", text="{a}A amônia, ene agá três, deixa a água básica. [p=0.3] {b}Mas ela não tem ó agá nenhum na fórmula. [p=0.3] {c}Pela regra de Arrhenius, ela nem seria base. [p=0.2] {d}Então a regra precisa crescer."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}usar a definição de Brônsted e Lowry, [p=0.1] {b}apontar os pares conjugados [p=0.2] e {c}dizer o que é um ácido de Lewis."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}o agá mais é um hidrogênio sem o elétron, ou seja, só um próton. [p=0.3] {b}Na estrutura de Lewis, os elétrons aparecem aos pares. [p=0.2] {c}E o nitrogênio da amônia tem um par livre, que não está em ligação nenhuma."),
    # Brønsted-Lowry
    dict(id="s04", block="bronsted", text="Em mil novecentos e vinte e três, o dinamarquês Brônsted e o inglês Lowry olharam para o agá mais. [p=0.3] {a}Ácido é quem doa agá mais. [p=0.2] {b}Base é quem recebe agá mais."),
    dict(id="s05", block="bronsted", text="Veja a amônia na água. [p=0.2] {a}Ene agá três, mais agá dois ó, [p=0.1] {b}produz o íon amônio, ene agá quatro mais, [p=0.1] {c}e o ó agá menos. [p=0.3] {d}A água doou um agá mais: ela foi o ácido. [p=0.2] {e}A amônia recebeu: foi a base. [p=0.2] {f}E o ó agá menos que sobrou deixa a água básica."),
    dict(id="s06", block="bronsted", text="Com o ácido clorídrico, é o contrário. [p=0.2] {a}Agá cê éle, mais agá dois ó, [p=0.1] {b}produz agá três ó mais e cê éle menos. [p=0.3] {c}O agá cê éle doou: é o ácido. [p=0.2] {d}A água recebeu: é a base. [p=0.3] {e}A água muda de papel conforme o parceiro. [p=0.1] Por isso se diz que ela é anfótera: pode ser ácido ou base."),
    # pares conjugados
    dict(id="s07", block="pares", text="Agora, os pares. [p=0.2] {a}Quando o agá cê éle doa o agá mais, sobra o cê éle menos. [p=0.3] {b}Os dois formam um par conjugado: [p=0.1] {c}fórmulas que diferem por um agá mais, e só."),
    dict(id="s08", block="pares", text="{a}O cê éle menos é a base conjugada do agá cê éle. [p=0.3] {b}Do outro lado, a água recebeu um agá mais e virou agá três ó mais: [p=0.2] {c}o hidrônio é o ácido conjugado da água."),
    dict(id="s09", block="pares", text="{a}Em toda reação desse tipo, há dois pares: [p=0.2] {b}um ácido com a sua base conjugada, [p=0.1] {c}e uma base com o seu ácido conjugado."),
    # Lewis
    dict(id="s10", block="lewis", text="No mesmo ano, o americano Lewis olhou para os elétrons. [p=0.2] {a}Base de Lewis é quem doa um par de elétrons. [p=0.2] {b}Ácido de Lewis é quem recebe esse par."),
    dict(id="s11", block="lewis", text="{a}Quando a amônia recebe um agá mais, [p=0.1] {b}é o par livre do nitrogênio que se liga a ele. [p=0.3] {c}A amônia doou o par: é a base de Lewis. [p=0.2] {d}O agá mais, sem elétron nenhum, recebeu o par: é o ácido de Lewis."),
    dict(id="s12", block="lewis", text="{a}E o ácido de Lewis nem precisa ter hidrogênio. [p=0.2] {b}No bê éfe três, o boro tem só seis elétrons em volta: [p=0.1] {c}falta um par para completar o octeto. [p=0.3] {d}Ele recebe o par da amônia, e por isso é um ácido de Lewis."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}cruzar os pares: [p=0.1] {b}juntar o agá cê éle com o agá três ó mais, porque ambos são ácidos. [p=0.3] {c}Par conjugado não é ácido com ácido. [p=0.2] {d}É um ácido com a base que sobra dele, quando ele perde um agá mais."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova para achar o par: [p=0.2] {a}tire um agá da fórmula e tire um da carga: [p=0.1] é a base conjugada. [p=0.3] {b}Ponha um agá e some um na carga: [p=0.1] é o ácido conjugado."),
    dict(id="s15", block="atalho", text="{a}Agá dois ó, tirando um agá: [p=0.1] {b}ó agá menos. [p=0.2] {c}Agá dois ó, pondo um agá: [p=0.1] {d}agá três ó mais. [p=0.3] Funciona porque {e}o agá mais leva uma carga positiva com ele. [p=0.2] {f}Mas no ácido de Lewis não há agá para contar: [p=0.1] {g}lá, procure quem recebe o par de elétrons."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Na reação {a}agá ene ó três, mais agá dois ó, [p=0.1] {b}produz agá três ó mais e ene ó três menos: [p=0.3] {c}quem é o ácido e quem é a base de Brônsted? [p=0.2] {d}Quais são os dois pares conjugados? [p=0.3] E {e}quando o cê éle menos se liga ao á éle cê éle três, em que o alumínio tem só seis elétrons em volta, quem é o ácido de Lewis?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O agá ene ó três doou o agá mais: é o ácido. [p=0.2] {b}A água recebeu: é a base. [p=0.3] {c}Primeiro par: agá ene ó três e ene ó três menos. [p=0.2] {d}Segundo par: agá três ó mais e agá dois ó."),
    dict(id="s19", block="resposta", text="{a}Na ligação do cloreto com o á éle cê éle três, [p=0.1] {b}o cê éle menos doa um par de elétrons: [p=0.1] é a base de Lewis. [p=0.3] {c}O alumínio, com falta de um par, recebe: [p=0.1] {d}o á éle cê éle três é o ácido de Lewis."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}para Brônsted e Lowry, ácido doa agá mais e base recebe; [p=0.2] {b}o par conjugado difere por um agá mais; [p=0.2] e {c}ácido de Lewis é quem recebe um par de elétrons."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai {a}praticar tudo o que viu sobre ácidos, bases, sais e óxidos, [p=0.2] {b}com questões de produtos do dia a dia. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
