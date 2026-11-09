# Estudativo · FIS-MOD-007 — Praticando: física moderna (Física · Física Moderna · Quantização, dualidade e relatividade · prática).
# Habilidade: resolver questões de fóton, efeito fotoelétrico, espectros e relatividade.
# Pré-requisitos: FIS-MOD-001 a 006 e FIS-MOD-011. Próxima: FIS-MOD-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Prática: cinco questões inéditas, criadas para esta aula. Constantes: h = 6,6 × 10⁻³⁴ J·s, c = 3 × 10⁸ m/s, 1 eV = 1,6 × 10⁻¹⁹ J.
# Q1: 600 nm → f = 5 × 10¹⁴ Hz → E = 3,3 × 10⁻¹⁹ J. Q2: 4,8 × 10⁻¹⁹ J = 3 eV; sódio 2,3 eV → 0,7 eV. Q3: hidrogênio −13,6 / −3,4
# / −1,51 eV: 10,2 eV é absorvido, 11 eV não. Q4: 2 μs a 0,6c → γ = 1,25 → 2,5 μs e 450 m. Q5: mesma quantidade de movimento →
# mesmo λ (pegadinha). Nanômetro: prefixo nano (MAT-MED-003) = 10⁻⁹.

TITULO = "Praticando: física moderna"

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
    dict(id="s01", block="gancho", text="{a}Física Moderna assusta pelo nome, [p=0.2] {b}mas a prova cobra poucas fórmulas, sempre as mesmas. [p=0.3] {c}Até o fim desta aula, você vai resolver cinco questões [p=0.2] de fóton, efeito fotoelétrico, espectros, dualidade e relatividade."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as aulas deste módulo. [p=0.2] {a}Agá vale seis vírgula seis vezes dez elevado a menos trinta e quatro joule vezes segundo, [p=0.2] {b}cê vale três vezes dez elevado a oito metros por segundo, [p=0.2] e {c}um elétron-volt vale um vírgula seis vezes dez elevado a menos dezenove joule. [p=0.3] Se faltar alguma aula, procure no canal."),
    # método
    dict(id="s03", block="metodo", text="Primeiro, o método: [p=0.2] {a}a palavra da questão escolhe a fórmula. [p=0.3] {b}Frequência ou cor da luz: [p=0.1] energia igual a agá vezes efe. [p=0.2] {c}Arrancar elétron de metal: [p=0.1] energia cinética igual a agá vezes efe menos dáblio. [p=0.2] {d}Nível ou salto: [p=0.1] a diferença entre os níveis."),
    dict(id="s04", block="metodo", text="{a}Onda de uma partícula: [p=0.1] lambda igual a agá sobre quê. [p=0.2] {b}Velocidade perto da luz: [p=0.1] gama, que multiplica o tempo e divide o comprimento. [p=0.3] {c}E antes de qualquer conta, confira se as unidades combinam: [p=0.1] joule com joule, elétron-volt com elétron-volt."),
    # questão 1
    dict(id="s05", block="q1", text="Questão um. [p=0.2] {a}Uma luz laranja tem comprimento de onda de seiscentos nanômetros, [p=0.1] {b}seis vezes dez elevado a menos sete metros. [p=0.3] {c}Qual é a energia de cada fóton, em joule? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s06", block="q1", text="{a}Falta a frequência: cê igual a lambda vezes efe. [p=0.2] {b}Três vezes dez elevado a oito dividido por seis vezes dez elevado a menos sete: [p=0.2] {c}cinco vezes dez elevado a catorze hertz. [p=0.3] {d}Agá vezes efe: seis vírgula seis vezes cinco, trinta e três, [p=0.1] e dez elevado a menos vinte. [p=0.2] {e}Três vírgula três vezes dez elevado a menos dezenove joules."),
    # questão 2
    dict(id="s07", block="q2", text="Questão dois. [p=0.2] {a}Fótons de quatro vírgula oito vezes dez elevado a menos dezenove joules batem no sódio, [p=0.1] {b}de função trabalho dois vírgula três elétron-volts. [p=0.3] {c}Com que energia saem os elétrons? [p=0.2] {d}E se a intensidade triplicar? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s08", block="q2", text="{a}Unidades diferentes: passe o fóton para elétron-volt. [p=0.2] {b}Quatro vírgula oito dividido por um vírgula seis: três elétron-volts. [p=0.3] {c}Três menos dois vírgula três: [p=0.1] {d}zero vírgula sete elétron-volt. [p=0.3] {e}Com o triplo da intensidade, saem três vezes mais elétrons, [p=0.1] {f}cada um com os mesmos zero vírgula sete."),
    # questão 3
    dict(id="s09", block="q3", text="Questão três. [p=0.2] {a}Um átomo de hidrogênio está no primeiro nível, menos treze vírgula seis elétron-volts. [p=0.2] {b}O segundo vale menos três vírgula quatro, [p=0.1] e o terceiro, menos um vírgula cinquenta e um. [p=0.3] {c}Ele absorve um fóton de dez vírgula dois elétron-volts? [p=0.1] {d}E um de onze? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s10", block="q3", text="{a}Do primeiro para o segundo, o salto é treze vírgula seis menos três vírgula quatro: [p=0.1] dez vírgula dois. [p=0.2] {b}O fóton de dez vírgula dois paga o salto exato: [p=0.1] {c}é absorvido. [p=0.3] {d}Do primeiro para o terceiro, o salto é doze vírgula zero nove. [p=0.2] {e}Onze fica entre os saltos, não paga nenhum certinho: [p=0.1] {f}o fóton passa direto."),
    # questão 4
    dict(id="s11", block="q4", text="Questão quatro. [p=0.2] {a}Uma partícula instável vive dois microssegundos, parada. [p=0.2] {b}Num acelerador, ela anda a zero vírgula seis cê. [p=0.3] {c}Quanto tempo ela vive, medida no laboratório? [p=0.1] {d}E quantos metros anda? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s12", block="q4", text="{a}Zero vírgula seis cê: pelo três, quatro, cinco, gama é um vírgula vinte e cinco. [p=0.2] {b}O laboratório vê de fora: tempo maior. [p=0.2] {c}Dois vezes um vírgula vinte e cinco: dois vírgula cinco microssegundos. [p=0.3] {d}A velocidade é zero vírgula seis vezes três vezes dez elevado a oito: [p=0.1] um vírgula oito vezes dez elevado a oito metros por segundo. [p=0.2] {e}Vezes dois vírgula cinco vezes dez elevado a menos seis segundos: [p=0.1] {f}quatrocentos e cinquenta metros."),
    # questão 5
    dict(id="s13", block="q5", text="Questão cinco. [p=0.2] {a}Um elétron e um próton têm a mesma quantidade de movimento. [p=0.3] {b}Qual dos dois tem o maior comprimento de onda? [p=0.2] {c}Pause e tente. [p=3.0]"),
    dict(id="s14", block="q5", text="{a}A pegadinha está na massa. [p=0.2] {b}Lambda é agá dividido por quê, [p=0.1] e quê é o mesmo para os dois. [p=0.3] {c}Mesmo quê, mesmo lambda: [p=0.1] {d}os comprimentos de onda são iguais. [p=0.3] {e}A massa só importa quando a questão fixa a velocidade: [p=0.2] {f}mesma velocidade, o elétron, mais leve, tem quê menor [p=0.1] {g}e lambda maior."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: {a}a palavra da questão escolhe a fórmula, [p=0.2] {b}e as unidades se acertam antes da conta. [p=0.3] Na próxima aula, {c}a Física vai ao céu: [p=0.2] {d}a vida das estrelas e os buracos negros. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
