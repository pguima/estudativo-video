# Estudativo · FIS-MOD-001 — Fóton: a energia em pacotes (Física · Física Moderna · Quantização, dualidade e relatividade).
# Habilidade: calcular E = h·f, converter joule em elétron-volt e explicar a ideia de Planck.
# Pré-requisitos: FIS-OND-010 (espectro, c = λ·f), FIS-ELE-004 (τ = q·U). Próxima: FIS-MOD-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Primeira aula da trilha Física Moderna: guarda a linguagem visual da trilha (veja o visual.py). Questão inédita.
# Constantes: h = 6,6 × 10⁻³⁴ J·s (valor exato 6,626 × 10⁻³⁴), carga do elétron 1,6 × 10⁻¹⁹ C (1,602 × 10⁻¹⁹), 1 eV = 1,6 × 10⁻¹⁹ J.
# História: Planck (1900) e a luz dos corpos quentes; Einstein (1905): a luz é feita de pacotes. Frequências: 8 × 10¹⁴ Hz
# (375 nm, ultravioleta próximo); 4 × 10¹⁴ Hz (750 nm, vermelho do fim do visível); 1,6 × 10¹⁵ Hz (187 nm, ultravioleta distante).
# Energia cinética (FIS-ENE-002) não está em "Já ensinado": não é usada.

TITULO = "Fóton: a energia em pacotes"

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
    dict(id="s01", block="gancho", text="{a}Uma lâmpada vermelha fortíssima, ligada o dia inteiro, [p=0.2] não te dá queimadura de sol. [p=0.3] {b}Poucos minutos de sol forte dão. [p=0.3] A culpada é {c}a luz ultravioleta que vem do sol. [p=0.2] E o segredo é que a luz chega {d}em pacotes."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a energia de um pacote de luz, [p=0.2] {b}passar de joule para elétron-volt [p=0.2] e {c}explicar a ideia de Planck."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a luz é uma onda, e a velocidade dela é o comprimento de onda vezes a frequência; [p=0.2] e {c}o trabalho da força elétrica é a carga vezes a diferença de potencial. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia de Planck
    dict(id="s04", block="pacote", text="Em mil e novecentos, {a}a Física não explicava a luz de um corpo quente, [p=0.2] como {b}o ferro em brasa, que passa do vermelho ao amarelo e ao branco quando esquenta. [p=0.3] {c}O alemão Max Planck achou a saída: [p=0.2] a energia da luz {d}não sai em qualquer quantidade. [p=0.2] {e}Sai em pacotes."),
    dict(id="s05", block="pacote", text="Pense numa {a}rampa e numa escada. [p=0.2] Na rampa, você para em qualquer altura. [p=0.2] {b}Na escada, só nos degraus. [p=0.3] Para Planck, a energia é como a escada. [p=0.2] Essa ideia se chama {c}quantização. [p=0.3] Em mil novecentos e cinco, {d}Einstein foi além: a própria luz é feita desses pacotes. [p=0.2] Hoje, o pacote de luz se chama {e}fóton."),
    # a fórmula
    dict(id="s06", block="formula", text="{a}A energia de um fóton é a constante de Planck vezes a frequência da luz: [p=0.2] {b}energia igual a agá vezes efe. [p=0.3] {c}A frequência vai em hertz, [p=0.1] {d}a energia sai em joule, [p=0.2] e {e}a constante agá vale seis vírgula seis vezes dez elevado a menos trinta e quatro joule vezes segundo."),
    dict(id="s07", block="formula", text="Confira pela unidade: [p=0.2] {a}o hertz é um por segundo, [p=0.2] então {b}o segundo corta, e sobra joule. [p=0.3] E veja como agá é pequena: [p=0.2] {c}são trinta e três zeros depois da vírgula antes do seis. [p=0.2] Por isso {d}um fóton sozinho tem pouquíssima energia, [p=0.2] e {e}uma lâmpada solta bilhões de bilhões de fótons por segundo."),
    # exemplo
    dict(id="s08", block="exemplo", text="Vamos calcular. [p=0.2] Uma luz ultravioleta tem frequência de {a}oito vezes dez elevado a catorze hertz. [p=0.3] {b}Seis vírgula seis vezes oito: cinquenta e dois vírgula oito. [p=0.2] {c}Nas potências de dez, some os expoentes: menos trinta e quatro mais catorze, menos vinte. [p=0.3] {d}Ande a vírgula uma casa para a esquerda, e o expoente sobe um: [p=0.2] {e}cinco vírgula vinte e oito vezes dez elevado a menos dezenove joules."),
    # elétron-volt
    dict(id="s09", block="ev", text="{a}Número em joule, para um fóton, é sempre assim: minúsculo e chato de ler. [p=0.2] Por isso, no mundo do átomo, se usa uma unidade bem menor: [p=0.2] {b}o elétron-volt. [p=0.3] {c}É o trabalho para levar a carga de um elétron por uma diferença de potencial de um volt. [p=0.3] {d}Carga vezes diferença de potencial: [p=0.1] {e}um vírgula seis vezes dez elevado a menos dezenove coulomb, vezes um volt. [p=0.2] {f}Um elétron-volt é um vírgula seis vezes dez elevado a menos dezenove joule."),
    dict(id="s10", block="ev", text="Para passar de joule para elétron-volt, {a}divida por um vírgula seis vezes dez elevado a menos dezenove. [p=0.3] {b}As potências de dez são iguais e se cancelam. [p=0.2] {c}Sobra cinco vírgula vinte e oito dividido por um vírgula seis: [p=0.1] {d}três vírgula três. [p=0.2] O fóton ultravioleta tem {e}três vírgula três elétron-volts."),
    # brilho não é energia do fóton
    dict(id="s11", block="brilho", text="E a lâmpada vermelha fortíssima? [p=0.2] {a}Luz mais forte é mais fótons, [p=0.2] {b}não fótons mais fortes. [p=0.3] {c}A energia de cada fóton depende só da frequência. [p=0.3] {d}E cada fóton age sozinho: [p=0.2] para estragar uma molécula da pele, um fóton precisa ter energia suficiente. [p=0.2] {e}Muitos fótons fracos não somam forças."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}multiplicar na conversão. [p=0.3] {b}Cinco vírgula vinte e oito vezes dez elevado a menos dezenove, vezes um vírgula seis vezes dez elevado a menos dezenove, [p=0.2] dá {c}oito vírgula quatro vezes dez elevado a menos trinta e oito. [p=0.3] {d}Pense no tamanho: o elétron-volt é uma unidade minúscula, [p=0.2] e {e}o número numa unidade menor fica maior, [p=0.1] como um metro vale cem centímetros."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}energia e frequência são diretamente proporcionais. [p=0.2] {b}Dobrou a frequência, dobrou a energia. [p=0.3] {c}Uma luz vermelha de quatro vezes dez elevado a catorze hertz tem metade da frequência do nosso ultravioleta. [p=0.2] Então, {d}metade da energia: um vírgula sessenta e cinco elétron-volt, sem conta nenhuma."),
    dict(id="s14", block="atalho", text="E como a velocidade da luz é fixa, [p=0.2] {a}comprimento de onda maior quer dizer frequência menor, e fóton mais fraco. [p=0.3] {b}Do vermelho para o violeta, o fóton fica mais forte. [p=0.3] {c}Não compensa quando os números não têm relação simples: [p=0.2] aí, faça agá vezes efe."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma lâmpada ultravioleta emite luz de {a}um vírgula seis vezes dez elevado a quinze hertz. [p=0.3] {b}Qual é a energia de cada fóton, em joule e em elétron-volt? [p=0.3] E {c}quantas vezes ela é maior que a do fóton vermelho de quatro vezes dez elevado a catorze hertz?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Seis vírgula seis vezes um vírgula seis: dez vírgula cinquenta e seis. [p=0.2] {b}Menos trinta e quatro mais quinze: dez elevado a menos dezenove. [p=0.2] {c}Dez vírgula cinquenta e seis vezes dez elevado a menos dezenove joules. [p=0.2] Deixe assim, que facilita a conversão. [p=0.3] {d}Para elétron-volt, divida por um vírgula seis vezes dez elevado a menos dezenove: [p=0.2] {e}seis vírgula seis elétron-volts."),
    dict(id="s18", block="resposta", text="{a}E a comparação, pelo atalho: [p=0.2] {b}um vírgula seis vezes dez elevado a quinze é dezesseis vezes dez elevado a catorze. [p=0.2] {c}Dezesseis dividido por quatro: quatro. [p=0.3] {d}Quatro vezes a frequência, quatro vezes a energia. [p=0.2] Confira: {e}quatro vezes um vírgula sessenta e cinco dá seis vírgula seis."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a luz vem em pacotes, os fótons; [p=0.2] {b}a energia de cada um é agá vezes efe; [p=0.2] e {c}para passar para elétron-volt, divida por um vírgula seis vezes dez elevado a menos dezenove."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}a luz arranca elétrons de um metal, [p=0.2] e você vai ver por que {b}a cor da luz importa mais que o brilho. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
