# Estudativo · FIS-CAL-007 — Diagrama de fases (Física · Calor e Termodinâmica · Calorimetria e mudanças de estado).
# Habilidade: ler ponto triplo e curvas de um diagrama de fases e explicar a panela de pressão.
# Pré-requisitos: FIS-CAL-004 (patamar, calor latente), FIS-EGF-004 (pressão, atm), QUI-MIS-003 (mudanças de estado). Próxima: FIS-CAL-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Fatos: a panela de pressão doméstica trabalha perto de 2 atm, e a água ferve perto de 120 °C; no topo do Everest, perto de 70 °C.
# Ponto triplo do CO2 ≈ 5,1 atm e −57 °C (o gelo-seco sublima a 1 atm). A curva de fusão da água inclina para a esquerda.
# Ponto crítico fica de fora (não está na habilidade).

TITULO = "Diagrama de fases"

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
    dict(id="s01", block="gancho", text="{a}No topo do Everest, a água ferve a uns setenta graus. [p=0.3] {b}Na panela de pressão, a uns cento e vinte. [p=0.3] É a mesma água. [p=0.2] O que mudou foi {c}a pressão."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai ler {b}um diagrama de fases [p=0.2] e explicar {c}por que a panela de pressão cozinha mais rápido."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}pressão, que ao nível do mar vale uma atmosfera; [p=0.2] e {c}as mudanças de estado, como a sublimação, em que o sólido vira gás direto. [p=0.3] Se faltar alguma, procure no canal."),
    # o diagrama
    dict(id="s04", block="diagrama", text="O diagrama de fases é um gráfico com {a}a temperatura no eixo de baixo [p=0.1] e {b}a pressão no eixo da esquerda. [p=0.3] Cada ponto dele é uma situação: [p=0.2] {c}tal temperatura, com tal pressão. [p=0.3] E ele diz {d}em que estado a substância está ali."),
    dict(id="s05", block="diagrama", text="Ele tem {a}três regiões. [p=0.2] {b}Sólido, à esquerda, nas temperaturas baixas. [p=0.2] {c}Líquido, em cima, à direita. [p=0.2] {d}Vapor, embaixo, nas pressões baixas."),
    dict(id="s06", block="diagrama", text="As regiões são separadas por {a}três curvas. [p=0.2] {b}A de fusão, entre sólido e líquido. [p=0.2] {c}A de vaporização, entre líquido e vapor. [p=0.2] {d}A de sublimação, entre sólido e vapor. [p=0.3] {e}Em cima de uma curva, os dois estados convivem: [p=0.2] é o patamar da curva de aquecimento."),
    dict(id="s07", block="diagrama", text="As três curvas se encontram num ponto: [p=0.2] {a}o ponto triplo. [p=0.3] Ali, {b}sólido, líquido e vapor convivem ao mesmo tempo. [p=0.3] Na água, ele fica {c}numa pressão bem baixa, [p=0.2] muito menor que uma atmosfera."),
    # leitura a 1 atm
    dict(id="s08", block="leitura", text="Agora, leia o diagrama da água. [p=0.2] {a}Trace uma linha em uma atmosfera. [p=0.3] Andar por essa linha para a direita é {b}esquentar com a pressão fixa. [p=0.3] A linha cruza {c}a fusão em zero grau [p=0.2] e {d}a vaporização em cem graus. [p=0.3] São os pontos fixos da escala Celsius."),
    # panela de pressão
    dict(id="s09", block="panela", text="Na panela de pressão, a tampa prende o vapor, [p=0.2] e a pressão chega {a}perto de duas atmosferas. [p=0.3] {b}A linha sobe, [p=0.2] e {c}encontra a curva de vaporização mais à direita: [p=0.2] {d}perto de cento e vinte graus."),
    dict(id="s10", block="panela", text="{a}A água fica líquida mais quente, [p=0.2] e {b}a comida cozinha mais rápido. [p=0.3] {c}Na montanha, é o contrário: [p=0.2] pressão menor, {d}a água ferve abaixo de cem, [p=0.2] e o macarrão demora mais."),
    # a água é diferente
    dict(id="s11", block="fusao", text="Repare na curva de fusão da água: [p=0.2] {a}ela tomba para a esquerda. [p=0.3] Então, {b}quanto mais pressão, menor a temperatura de fusão do gelo. [p=0.3] Na maioria das substâncias, como o gás carbônico, {c}ela tomba para a direita."),
    # gelo seco
    dict(id="s12", block="fusao", text="E o gás carbônico tem outra surpresa: [p=0.2] seu ponto triplo fica {a}acima de cinco atmosferas. [p=0.3] {b}Em uma atmosfera, a linha passa por baixo dele, [p=0.2] e só cruza {c}a curva de sublimação. [p=0.3] O gás carbônico sólido, o {d}gelo-seco, [p=0.2] vira gás direto, sem passar por líquido."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}dizer que, na panela de pressão, a água ferve mais rápido. [p=0.3] {b}É o contrário: [p=0.2] ela demora mais para ferver, [p=0.2] porque {c}precisa chegar a cento e vinte graus. [p=0.3] O que fica mais rápido {d}é o cozimento."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho: [p=0.2] {a}trace a linha da pressão da questão e ande para a direita. [p=0.3] {b}Cada curva que você cruza é uma mudança de estado. [p=0.3] E guarde a regra: [p=0.2] {c}pressão sobe, a temperatura de ebulição sobe. [p=0.3] {d}Com a pressão abaixo da do ponto triplo, o sólido vira gás direto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] O ponto triplo de uma substância fica em {a}meia atmosfera e vinte graus. [p=0.3] Você aquece o sólido {b}em uma atmosfera. [p=0.2] {c}O que acontece? [p=0.3] E {d}em zero vírgula dois atmosfera?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Uma atmosfera é mais que meia: [p=0.2] a linha passa {b}acima do ponto triplo. [p=0.1] Ela cruza {c}a fusão e depois a vaporização: [p=0.2] o sólido derrete e, depois, o líquido ferve."),
    dict(id="s18", block="resposta", text="{a}Zero vírgula dois atmosfera é menos que meia: [p=0.2] a linha passa {b}abaixo do ponto triplo [p=0.1] e só cruza {c}a sublimação. [p=0.2] {d}O sólido vira gás direto, [p=0.1] {e}sem passar por líquido."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}cada região é um estado, cada curva é uma mudança; [p=0.2] {b}no ponto triplo, os três convivem; [p=0.2] e {c}mais pressão, ebulição mais quente."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai {a}praticar tudo deste módulo: [p=0.2] {b}escalas, dilatação, trocas de calor, com e sem gelo, e o diagrama de fases. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
