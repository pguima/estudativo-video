# Estudativo · FIS-ELE-007 — Praticando: eletrostática (Física · Eletricidade · Eletrostática · prática).
# Habilidade: resolver questões de eletrização, força, campo, potencial e capacitores.
# Pré-requisitos: FIS-ELE-001 a FIS-ELE-006. Próxima: FIS-ELE-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Prática: cinco questões inéditas, criadas para esta aula, uma por assunto do módulo.
# Contas: (4,8 − 1,6)/2 = 1,6 µC; B vai de −1,6 a +1,6: 3,2 µC = 2 × 10¹³ elétrons. 80·(1/2)·4 = 160 N.
# 1,6e-19·5e4 = 8e-15 N. 5e4·0,02 = 1000 V; 1,6e-19·1000 = 1,6e-16 J. 10e-6·200 = 2e-3 C; 2e-3·200/2 = 0,2 J; 0,2/4 = 0,05 J.

TITULO = "Praticando: eletrostática"

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
    dict(id="s01", block="gancho", text="Eletrostática tem {a}muitas fórmulas parecidas, [p=0.2] e a prova adora misturar. [p=0.3] {b}Até o fim desta aula, você vai resolver cinco questões que cobrem o módulo, [p=0.2] e {c}saber qual fórmula usar só de olhar o que a questão pede."),
    # lembrete / método
    dict(id="s02", block="metodo", text="Você vai usar as aulas deste módulo. [p=0.2] Se faltar alguma, procure no canal. [p=0.3] O método é um só: [p=0.1] {a}veja a grandeza que a questão pede [p=0.1] e {b}procure a fórmula que tem essa grandeza e os dados."),
    dict(id="s03", block="metodo", text="{a}Carga contando elétrons: quê igual a ene vezes ê. [p=0.2] {b}Força entre duas cargas: Coulomb. [p=0.2] {c}Campo: efe dividido por quê. [p=0.2] {d}Tensão no campo uniforme: o campo vezes a distância. [p=0.2] {e}Trabalho: quê vezes U. [p=0.2] {f}E capacitor: cê igual a quê dividido por U."),
    # questão 1
    dict(id="s04", block="q1", text="Questão um. [p=0.2] Duas esferas de metal iguais: [p=0.1] {a}a esfera um tem mais quatro vírgula oito microcoulombs, [p=0.1] {b}e a esfera dois, menos um vírgula seis microcoulomb. [p=0.3] Elas se encostam e se separam. [p=0.2] {c}Com que carga cada uma fica? [p=0.2] {d}E quantos elétrons passaram de uma para a outra? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s05", block="q1", text="{a}Some com o sinal: quatro vírgula oito menos um vírgula seis, três vírgula dois. [p=0.2] {b}Divida por dois: mais um vírgula seis microcoulomb em cada. [p=0.3] {c}A esfera dois foi de menos um vírgula seis para mais um vírgula seis: [p=0.1] mudou três vírgula dois microcoulombs. [p=0.3] {d}Ene é a carga dividida por ê: [p=0.1] três vírgula dois dividido por um vírgula seis, dois; [p=0.1] nos expoentes, menos seis mais dezenove, treze. [p=0.2] {e}Dois vezes dez elevado a treze elétrons, [p=0.1] {f}que saíram da esfera dois e foram para a um."),
    # questão 2
    dict(id="s06", block="q2", text="Questão dois. [p=0.2] Duas cargas se atraem com {a}oitenta newtons. [p=0.3] {b}Uma das cargas cai pela metade, [p=0.2] e {c}a distância entre elas também cai pela metade. [p=0.3] {d}Qual é a nova força? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s07", block="q2", text="Use a proporção. [p=0.2] {a}A carga caiu pela metade: a força vai dividida por dois. [p=0.3] {b}A distância caiu pela metade: [p=0.1] a força fica quatro vezes maior. [p=0.3] {c}Oitenta dividido por dois, quarenta; [p=0.1] {d}vezes quatro, cento e sessenta newtons. [p=0.3] {e}A força dobrou."),
    # questão 3
    dict(id="s08", block="q3", text="Questão três. [p=0.2] Entre duas placas paralelas, o campo é uniforme, de {a}cinco vezes dez elevado a quatro newtons por coulomb. [p=0.3] {b}Um elétron é posto entre elas. [p=0.2] {c}Qual é a força sobre ele, [p=0.1] {d}em valor e sentido? [p=0.3] E se esse elétron estivesse {f}dentro de uma esfera de metal carregada e em equilíbrio? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s09", block="q3", text="{a}A força é a carga vezes o campo, [p=0.1] e a carga do elétron é a carga elementar. [p=0.3] {b}Um vírgula seis vezes cinco, oito; [p=0.1] {c}menos dezenove mais quatro, menos quinze. [p=0.2] {d}Oito vezes dez elevado a menos quinze newton. [p=0.3] {e}O elétron é negativo: [p=0.1] {f}a força é contrária ao campo, apontando para a placa positiva. [p=0.3] {g}Dentro da esfera de metal em equilíbrio, o campo é zero: [p=0.1] força zero."),
    # questão 4
    dict(id="s10", block="q4", text="Questão quatro. [p=0.2] Nas mesmas placas, {a}a distância entre elas é de dois centímetros. [p=0.3] {b}Qual é a tensão entre as placas? [p=0.2] {c}E qual é o trabalho da força elétrica sobre um próton [p=0.1] que vai da placa positiva até a negativa? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s11", block="q4", text="{a}Dois centímetros são zero vírgula zero dois metro. [p=0.2] {b}U é o campo vezes a distância: [p=0.1] cinco vezes dez elevado a quatro, vezes zero vírgula zero dois, [p=0.2] {c}mil volts. [p=0.3] {d}Tau é quê vezes U: [p=0.1] um vírgula seis vezes dez elevado a menos dezenove, vezes mil, [p=0.2] {e}um vírgula seis vezes dez elevado a menos dezesseis joule. [p=0.3] {f}Positivo: o próton foi do potencial maior para o menor."),
    # questão 5
    dict(id="s12", block="q5", text="Questão cinco. [p=0.2] Um capacitor de {a}dez microfarads está ligado a {b}duzentos volts. [p=0.3] {c}Qual é a energia guardada? [p=0.2] {d}E qual seria a energia com a tensão pela metade? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s13", block="q5", text="{a}Primeiro, a carga: quê é cê vezes U. [p=0.1] Dez vezes dez elevado a menos seis, vezes duzentos: [p=0.1] {b}dois vezes dez elevado a menos três coulomb. [p=0.3] {c}Energia, quê vezes U dividido por dois: [p=0.1] {d}zero vírgula dois joule. [p=0.3] {e}Com a tensão pela metade, a energia, que tem U ao quadrado, cai quatro vezes: [p=0.2] {f}zero vírgula zero cinco joule."),
    # fechamento
    dict(id="s14", block="fim", text="Resumindo: {a}olhe o que a questão pede, [p=0.1] {b}ache a fórmula que liga isso aos dados [p=0.2] e {c}use a proporção sempre que der. [p=0.3] Na próxima aula, as cargas começam a andar: [p=0.2] {d}a corrente elétrica. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
