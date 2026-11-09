# Estudativo · FIS-OND-002 — Ondas: tipos e a equação v = λ·f (Física · Ondas e Som · Ondas e seus fenômenos).
# Habilidade: classificar ondas, medir amplitude e comprimento no gráfico e usar v = λ·f, inclusive nas ondas sísmicas.
# Pré-requisitos: FIS-OND-001 (oscilação, amplitude, período), MAT-TRI-011 (gráfico do seno). Próxima: FIS-OND-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Energia (FIS-ENE) não está em "Já ensinado": usada no sentido do dia a dia.
# Ondas sísmicas: P (primárias, longitudinais, mais rápidas, passam por sólidos e líquidos); S (secundárias, transversais,
# mais lentas, não atravessam líquidos). 4 km/s é valor típico de onda S na crosta.

TITULO = "Ondas: tipos e a equação v = λ·f"

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
    dict(id="s01", block="gancho", text="{a}No estádio, a torcida faz a ola. [p=0.2] {b}A onda dá a volta inteira na arquibancada, [p=0.2] mas {c}ninguém sai do lugar. [p=0.3] {d}Cada pessoa só levanta e senta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai classificar as ondas, [p=0.2] {b}ler a amplitude e o comprimento no desenho [p=0.2] e usar {c}a equação vê igual a lambda vezes efe."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a oscilação, com amplitude, período e frequência; [p=0.2] e {c}o gráfico do seno, a curva que sobe e desce sem parar. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é onda
    dict(id="s04", block="onda", text="Onda é isso: {a}uma perturbação, uma sacudida, que viaja pelo meio. [p=0.2] {b}Ela leva energia de um lugar para outro: [p=0.1] é ela que faz um barco parado balançar. [p=0.2] Mas {c}não leva a matéria junto: [p=0.1] o barco sobe, desce e fica no lugar. [p=0.3] Numa corda, {d}cada ponto só sobe e desce, [p=0.2] e {e}o formato da onda é que anda."),
    # tipos
    dict(id="s05", block="tipos", text="As ondas se dividem de dois jeitos. [p=0.2] O primeiro é {a}a natureza. [p=0.2] {b}A onda mecânica precisa de um meio para andar: [p=0.1] corda, água, ar. [p=0.2] O som é mecânico: {c}no vácuo, não há som. [p=0.3] {d}A onda eletromagnética anda até no vácuo: [p=0.1] é o caso da luz do Sol e das ondas de rádio. [p=0.2] Do que ela é feita é assunto de outra aula."),
    dict(id="s06", block="tipos", text="O segundo jeito é {a}a direção da vibração. [p=0.2] {b}Na onda transversal, o meio vibra em ângulo reto com o caminho da onda: [p=0.2] a corda sobe e desce, e a onda vai para o lado. [p=0.3] {c}Na onda longitudinal, o meio vibra na mesma direção do caminho, [p=0.2] {d}como uma mola comprida que se aperta e se estica. [p=0.2] {e}O som é assim: o ar é empurrado para a frente e para trás."),
    # desenho
    dict(id="s07", block="desenho", text="Agora, o desenho da onda. [p=0.2] {a}Os pontos mais altos são as cristas, [p=0.1] {b}e os mais baixos, os vales. [p=0.3] {c}A amplitude, letra á, vai do meio até a crista. [p=0.2] {d}O comprimento de onda vai de uma crista até a próxima, [p=0.1] e a letra é grega: {e}lambda. [p=0.2] Os dois são distâncias, em metros."),
    dict(id="s08", block="desenho", text="{a}A frequência é quantas oscilações cada ponto faz por segundo, em hertz. [p=0.2] Quem decide é {b}a fonte: [p=0.1] a mão que balança a corda. [p=0.3] {c}E o período é o tempo de uma oscilação."),
    # equação
    dict(id="s09", block="equacao", text="Enquanto um ponto faz uma oscilação completa, [p=0.2] {a}a onda anda exatamente um comprimento de onda. [p=0.3] Velocidade é distância dividida pelo tempo: [p=0.2] {b}lambda dividido por tê. [p=0.2] E dividir por tê é o mesmo que multiplicar por efe. [p=0.2] Daí, {c}vê igual a lambda vezes efe. [p=0.3] {d}Lambda em metros, efe em hertz, vê em metros por segundo."),
    dict(id="s10", block="equacao", text="Uma corda com {a}lambda de meio metro, [p=0.1] e a mão faz {b}quatro oscilações por segundo. [p=0.2] {c}Zero vírgula cinco vezes quatro: [p=0.1] {d}dois metros por segundo."),
    # sísmicas
    dict(id="s11", block="sismo", text="A mesma equação vale {a}nos terremotos. [p=0.2] Eles mandam dois tipos de onda pelo chão. [p=0.2] {b}A onda pê, primária, é longitudinal e a mais rápida: chega primeiro. [p=0.3] {c}A onda esse, secundária, é transversal, mais lenta, [p=0.1] e não atravessa líquidos."),
    dict(id="s12", block="sismo", text="Uma onda esse a {a}quatro mil metros por segundo, com {b}frequência de dois hertz. [p=0.2] Lambda é vê dividido por efe: [p=0.1] {c}quatro mil dividido por dois, [p=0.1] {d}dois mil metros. [p=0.2] Cada onda tem dois quilômetros de comprimento."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: {a}medir a amplitude de crista a vale. [p=0.2] {b}De crista a vale dá o dobro da amplitude. [p=0.3] O mesmo vale para o lambda: [p=0.2] {c}de crista a vale é só meio comprimento de onda. [p=0.2] {d}O lambda vai de crista a crista, ou de vale a vale."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a frequência é da fonte, [p=0.1] {b}e a velocidade é do meio. [p=0.3] No mesmo meio, a velocidade fica fixa. [p=0.2] Então, {c}se a frequência dobra, o lambda cai pela metade. [p=0.2] {d}Mão mais rápida faz ondas mais curtas, não mais velozes. [p=0.3] {e}Não vale quando a onda troca de meio: [p=0.1] aí, a velocidade muda, assunto da próxima aula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Numa corda, da primeira à terceira crista há sessenta centímetros. [p=0.2] {b}Da crista ao vale, na vertical, há dez centímetros. [p=0.2] {c}A fonte faz cinco oscilações por segundo. [p=0.3] {d}Quais são a amplitude, o comprimento de onda e a velocidade?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Da crista ao vale é o dobro da amplitude: [p=0.1] {b}á vale cinco centímetros. [p=0.3] {c}Da primeira à terceira crista, são dois comprimentos de onda: [p=0.1] {d}lambda é trinta centímetros, zero vírgula três metro."),
    dict(id="s18", block="resposta", text="{a}Vê é zero vírgula três vezes cinco: [p=0.1] {b}um vírgula cinco metro por segundo."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}onda leva energia sem levar matéria; [p=0.2] {b}a mecânica precisa de meio, e a eletromagnética não; [p=0.2] {c}o lambda vai de crista a crista; [p=0.2] e {d}vê é igual a lambda vezes efe."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}a onda encontra obstáculos: [p=0.2] ela {b}bate e volta, [p=0.1] {c}muda de meio [p=0.1] e {d}contorna cantos. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
