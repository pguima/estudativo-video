# Estudativo · FIS-OPT-011 — Equação dos espelhos e aumento (Física · Óptica · Refração, lentes e olho humano).
# Habilidade: calcular com 1/f = 1/p + 1/p' e o aumento, usando o sinal de côncavo e convexo.
# Pré-requisitos: FIS-OPT-003 (raios notáveis), MAT-EQU-010 (equação com frações), MAT-FRA-008 (somar frações). Próxima: FIS-OPT-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Referencial de Gauss: objeto real p > 0; côncavo f > 0, convexo f < 0;
# p' > 0 imagem real (na frente), p' < 0 virtual (atrás); A = i/o = −p'/p. Atalho p' = f·p/(p − f), deduzido na aula.

TITULO = "Equação dos espelhos e aumento"

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
    dict(id="s01", block="gancho", text="Um espelho côncavo com {a}foco a vinte centímetros [p=0.2] e {b}um objeto a trinta. [p=0.3] Os raios dizem: {c}imagem real, invertida e maior. [p=0.3] Mas onde, exatamente? [p=0.2] E maior quanto? [p=0.3] A equação responde: {d}a sessenta centímetros do espelho, [p=0.2] {e}duas vezes maior."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}a posição da imagem [p=0.2] e {c}o aumento, [p=0.2] sem errar {d}o sinal do convexo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}os raios notáveis e o tipo de imagem em cada espelho; [p=0.2] e {c}somar frações com denominadores diferentes, pelo MMC. [p=0.3] Se faltar alguma, procure no canal."),
    # a equação
    dict(id="s04", block="equacao", text="Três distâncias, todas medidas a partir do espelho: [p=0.2] {a}efe, a distância focal; [p=0.2] {b}pê, a distância do objeto; [p=0.2] e {c}pê linha, a distância da imagem. [p=0.3] {d}Use a mesma unidade nas três."),
    dict(id="s05", block="equacao", text="A equação dos espelhos, também chamada de equação de Gauss, diz: [p=0.2] {a}um dividido por efe [p=0.1] é igual a {b}um dividido por pê [p=0.1] {c}mais um dividido por pê linha."),
    dict(id="s06", block="equacao", text="E os sinais contam a história. [p=0.2] {a}O objeto na frente do espelho tem pê positivo. [p=0.3] {b}Espelho côncavo: efe positivo. [p=0.2] {c}Convexo: efe negativo. [p=0.3] Se der {d}pê linha positivo, a imagem é real, na frente do espelho. [p=0.2] {e}Negativo, virtual, atrás dele."),
    # exemplo
    dict(id="s07", block="exemplo", text="Vamos ao gancho: {a}efe igual a vinte, pê igual a trinta. [p=0.3] Passe o um dividido por pê para o outro lado, subtraindo: [p=0.2] {b}um dividido por pê linha é igual a um vinte avos menos um trinta avos. [p=0.3] {c}O MMC de vinte e trinta é sessenta: [p=0.2] {d}três sessenta avos menos dois sessenta avos, [p=0.2] {e}um sessenta avos. [p=0.3] Então {f}pê linha é sessenta centímetros, positivo: imagem real."),
    # aumento
    dict(id="s08", block="aumento", text="O aumento, {a}A, diz quantas vezes a imagem é maior. [p=0.2] {b}É a altura da imagem dividida pela altura do objeto, [p=0.2] {c}ou menos pê linha dividido por pê."),
    dict(id="s09", block="aumento", text="{a}Menos sessenta dividido por trinta: [p=0.2] {b}menos dois. [p=0.3] {c}O sinal de menos diz que a imagem é invertida. [p=0.2] {d}O dois diz que ela é duas vezes maior. [p=0.3] {e}Aumento positivo seria imagem direita; [p=0.2] {f}e, sem olhar o sinal, se o número fica entre zero e um, a imagem é menor."),
    # convexo
    dict(id="s10", block="convexo", text="Agora um convexo: {a}um retrovisor com foco de vinte centímetros, [p=0.2] {b}então efe é menos vinte. [p=0.2] {c}O objeto está a trinta. [p=0.3] {d}Um dividido por pê linha é igual a menos um vinte avos menos um trinta avos: [p=0.2] {e}menos três sessenta avos menos dois sessenta avos, [p=0.2] {f}menos cinco sessenta avos, que é menos um doze avos."),
    dict(id="s11", block="convexo", text="{a}Pê linha é menos doze centímetros: [p=0.2] {b}imagem virtual, atrás do espelho. [p=0.3] {c}No aumento, o menos da fórmula com o menos do pê linha dá mais: [p=0.2] {d}doze dividido por trinta, mais dois quintos. [p=0.3] {e}Direita e menor: [p=0.2] do jeito que o convexo sempre faz."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}esquecer o sinal do convexo. [p=0.3] {b}Com efe igual a mais vinte, [p=0.2] a conta dá {c}pê linha igual a mais sessenta: [p=0.2] imagem real. [p=0.3] {d}Mas o convexo nunca dá imagem real. [p=0.2] {e}Antes de pôr o número, escreva o sinal do espelho."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}pê linha é efe vezes pê, [p=0.1] {b}dividido por pê menos efe. [p=0.3] No gancho: {c}vinte vezes trinta, seiscentos, [p=0.2] {d}dividido por trinta menos vinte, dez: [p=0.2] {e}sessenta. [p=0.3] Sem MMC."),
    dict(id="s14", block="atalho", text="Funciona porque {a}é a mesma equação, com as frações já subtraídas e viradas de cabeça para baixo. [p=0.3] {b}No convexo, cuidado com o sinal: [p=0.2] {c}menos vinte vezes trinta, menos seiscentos, [p=0.2] {d}dividido por trinta menos o menos vinte. [p=0.2] Menos com menos dá mais: trinta mais vinte, cinquenta: [p=0.2] {e}menos doze. [p=0.3] E {f}se a questão der o raio de curvatura, divida por dois para ter o foco."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um espelho de maquiagem é côncavo, com {a}foco de trinta centímetros. [p=0.3] {b}O rosto está a quinze centímetros dele. [p=0.3] {c}Onde está a imagem, [p=0.2] e {d}qual é o aumento?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Pelo atalho: {a}trinta vezes quinze, quatrocentos e cinquenta, [p=0.2] {b}dividido por quinze menos trinta, que é menos quinze. [p=0.3] {c}Pê linha é menos trinta centímetros: [p=0.2] {d}imagem virtual, atrás do espelho."),
    dict(id="s18", block="resposta", text="No aumento, {a}o menos da fórmula com o menos do pê linha dá mais: [p=0.2] {b}trinta dividido por quinze, mais dois. [p=0.3] {c}Imagem direita e duas vezes maior. [p=0.2] Bate com os raios: [p=0.2] {d}rosto entre o foco e o espelho."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}um dividido por efe é um dividido por pê mais um dividido por pê linha; [p=0.2] {b}côncavo tem efe positivo e convexo, negativo; [p=0.2] e {c}o aumento é menos pê linha dividido por pê, com o sinal dizendo se a imagem é invertida."),
    dict(id="s20", block="fim", text="Na próxima aula, a luz {a}muda de meio: [p=0.2] {b}o índice de refração e a lei de Snell, [p=0.2] que explicam {c}o lápis que parece quebrado dentro do copo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
