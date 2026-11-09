# Estudativo · FIS-ELE-006 — Capacitores (Física · Eletricidade · Eletrostática).
# Habilidade: usar C = Q/U, calcular a energia guardada e explicar o flash da câmera.
# Pré-requisitos: FIS-ELE-004 (tensão U, volt = J/C). Próxima: FIS-ELE-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Corrente (FIS-ELE-008) não está em "Já ensinado": carregar = "ligar a uma pilha".
# A energia como área do triângulo no gráfico U × Q usa a ideia de FIS-ENE-001 (área = trabalho). Flash de câmera
# fotográfica com lâmpada de xenônio: capacitor carregado em segundos, descarga em menos de 1 ms.
# Contas: 100e-6·300 = 3e-2 C; 3e-2·300/2 = 4,5 J; 20e-6·100 = 2e-3 C; 2e-3·100/2 = 0,1 J.

TITULO = "Capacitores"

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
    dict(id="s01", block="gancho", text="{a}O flash de uma câmera fotográfica acende por menos de um milésimo de segundo. [p=0.3] {b}As pilhas sozinhas não dariam conta de soltar a energia tão rápido. [p=0.3] {c}Quem faz isso é o capacitor."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar {b}cê igual a quê dividido por U, [p=0.2] {c}calcular a energia guardada [p=0.1] e {d}explicar o flash."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a tensão U, a diferença de potencial, se mede em volt, que é joule por coulomb; [p=0.3] e {c}no gráfico da força pelo deslocamento, a área é o trabalho. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="capacitor", text="Um capacitor é {a}duas placas de metal, uma de frente para a outra, [p=0.1] {b}separadas por um isolante. [p=0.3] Ligue as placas a uma pilha: [p=0.2] {c}uma fica com carga mais Q, [p=0.1] {d}a outra, com menos Q. [p=0.3] {e}Entre elas, surge um campo uniforme, e uma tensão U."),
    dict(id="s05", block="capacitor", text="Quanto mais tensão, mais carga: [p=0.2] {a}dobrou a tensão, a carga dobra. [p=0.3] A razão entre elas é {b}a capacitância: [p=0.1] {c}cê igual a quê dividido por U. [p=0.3] {d}Cê é a capacitância, em farad; [p=0.2] {e}quê é a carga de uma placa, em coulomb; [p=0.2] {f}U é a tensão, em volt."),
    dict(id="s06", block="capacitor", text="{a}Um farad é muito. [p=0.2] Os capacitores comuns têm {b}microfarads, milionésimos de farad. [p=0.3] {c}Cuidado com as letras. [p=0.1] Aqui, cê é a capacitância: a carga continua em coulomb. [p=0.2] E o éfe maiúsculo do farad não é o éfe da força."),
    dict(id="s07", block="capacitor", text="Um capacitor de {a}cem microfarads ligado a {b}trezentos volts. [p=0.3] {c}Quê é cê vezes U: [p=0.2] {d}cem vezes dez elevado a menos seis, vezes trezentos, [p=0.2] {e}três vezes dez elevado a menos dois coulomb."),
    # energia
    dict(id="s08", block="energia", text="Carregar o capacitor exige trabalho, [p=0.2] e esse trabalho fica guardado como {a}energia. [p=0.3] {b}No gráfico da tensão pela carga, a linha é reta [p=0.1] e sai do zero. [p=0.3] Tensão é joule por coulomb, [p=0.1] então tensão vezes carga dá joule: [p=0.2] {c}a área embaixo da linha é a energia, um triângulo. [p=0.2] {d}Base vezes altura, dividido por dois: [p=0.2] {e}energia igual a quê vezes U, dividido por dois."),
    dict(id="s09", block="energia", text="No capacitor de antes: [p=0.2] {a}três vezes dez elevado a menos dois, vezes trezentos, [p=0.2] {b}dá nove. [p=0.2] {c}Dividido por dois: [p=0.1] {d}quatro vírgula cinco joules."),
    dict(id="s10", block="energia", text="E o flash? [p=0.2] {a}As pilhas carregam o capacitor devagar, em alguns segundos. [p=0.3] {b}No clique, ele solta tudo em menos de um milésimo de segundo. [p=0.3] {c}Pouca energia, entregue muito rápido: [p=0.1] {d}a luz forte do flash."),
    dict(id="s11", block="energia", text="Como quê é cê vezes U, a energia também é {a}cê vezes U ao quadrado, dividido por dois. [p=0.3] {b}Dobrou a tensão? [p=0.1] {c}A energia fica quatro vezes maior."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer o dividido por dois. [p=0.3] {b}Quê vezes U dá nove joules, [p=0.1] o dobro da resposta certa. [p=0.3] {c}A energia é a área do triângulo, não a do retângulo: [p=0.2] {d}a tensão começou em zero e foi subindo."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a energia tem três formas, e todas dão o mesmo. [p=0.3] {b}Quê vezes U, dividido por dois. [p=0.2] {c}Cê vezes U ao quadrado, dividido por dois. [p=0.2] {d}Quê ao quadrado, dividido por duas vezes cê. [p=0.3] {e}Escolha a que usa os dados da questão, e você pula uma etapa."),
    dict(id="s14", block="atalho", text="Funciona porque {a}as três vêm de quê igual a cê vezes U. [p=0.3] {b}Não compensa decorar se você confunde as três: [p=0.2] calcule quê primeiro e use quê vezes U, dividido por dois."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um capacitor de {a}vinte microfarads é ligado a {b}cem volts. [p=0.3] {c}Qual é a carga em cada placa? [p=0.2] {d}E qual é a energia guardada?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Quê é cê vezes U: [p=0.1] {b}vinte vezes dez elevado a menos seis, vezes cem, [p=0.2] {c}dá dois mil vezes dez elevado a menos seis, [p=0.1] {d}ou dois vezes dez elevado a menos três coulomb."),
    dict(id="s18", block="resposta", text="{a}A energia é quê vezes U, dividido por dois. [p=0.2] {b}Dois vezes dez elevado a menos três, vezes cem: [p=0.1] zero vírgula dois. [p=0.2] {c}Dividido por dois: [p=0.1] {d}zero vírgula um joule."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}cê é quê dividido por U, em farad; [p=0.2] {b}a energia é quê vezes U, dividido por dois, a área do triângulo; [p=0.2] e {c}o capacitor carrega devagar e solta de uma vez."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai {a}praticar a eletrostática toda: [p=0.2] {b}eletrização, força, campo, potencial e capacitores, [p=0.1] em questões de prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
