# Estudativo · FIS-OND-009 — Praticando: som e efeito Doppler (Física · Ondas e Som · Som e efeito Doppler · prática).
# Habilidade: resolver questões de decibéis, instrumentos, ressonância e Doppler.
# Pré-requisitos: FIS-OND-006, 007, 008. Próxima: FIS-OND-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Prática: cinco questões inéditas, criadas para esta aula. 340/680 = 0,5 m; v = 2·0,6·300 = 360 m/s; tubo aberto de 0,5 m: 340, 680, 1.020 Hz;
# Doppler com observador: 500·(340 + 34)/340 = 550 Hz.

TITULO = "Praticando: som e efeito Doppler"

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
    dict(id="s01", block="gancho", text="Na prova, o som aparece de {a}quatro jeitos: [p=0.2] {b}decibéis, [p=0.1] {c}instrumentos, [p=0.1] {d}ressonância [p=0.1] e {e}Doppler. [p=0.3] {f}Até o fim desta aula, você vai resolver cinco questões que cobrem os quatro."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as aulas deste módulo: [p=0.2] {a}altura, intensidade e timbre; [p=0.1] {b}cordas e tubos; [p=0.1] {c}e o efeito Doppler. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s03", block="metodo", text="Primeiro, o método: [p=0.1] {a}veja o que a questão compara. [p=0.2] {b}Grave ou agudo é frequência. [p=0.1] {c}Forte ou fraco é intensidade, em decibéis. [p=0.1] {d}Instrumentos diferentes na mesma nota é timbre. [p=0.1] {e}Corpo que vibra forte com um som é ressonância. [p=0.1] {f}E fonte ou ouvinte andando é Doppler."),
    # questão 1
    dict(id="s04", block="q1", text="Questão um. [p=0.2] {a}Um fone no volume máximo chega a cem decibéis. [p=0.2] {b}A recomendação é não passar de oitenta. [p=0.3] {c}Quantas vezes o som máximo é mais intenso que o recomendado? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s05", block="q1", text="{a}Cem menos oitenta: vinte decibéis. [p=0.2] {b}Duas dezenas: um seguido de dois zeros. [p=0.2] {c}Cem vezes mais intenso. [p=0.3] {d}Quem dividiu cem por oitenta e achou um vírgula vinte e cinco esqueceu que a escala é de logaritmo."),
    # questão 2
    dict(id="s06", block="q2", text="Questão dois. [p=0.2] {a}Uma flauta e um violino tocam a mesma nota, de seiscentos e oitenta hertz, com a mesma intensidade. [p=0.3] {b}O que é igual nos dois sons, e o que é diferente? [p=0.2] {c}E qual é o lambda desse som no ar? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s07", block="q2", text="{a}Mesma frequência: mesma altura. [p=0.1] {b}Mesma intensidade: mesma força. [p=0.2] {c}O que muda é o timbre, o formato da onda, [p=0.1] porque cada instrumento mistura harmônicos de um jeito. [p=0.3] {d}Lambda: trezentos e quarenta dividido por seiscentos e oitenta, meio metro, [p=0.1] igual para os dois."),
    # questão 3
    dict(id="s08", block="q3", text="Questão três. [p=0.2] {a}Uma corda de violão de sessenta centímetros vibra no fundamental a trezentos hertz. [p=0.3] {b}Qual é a velocidade da onda na corda? [p=0.2] {c}E a frequência do terceiro harmônico? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s09", block="q3", text="{a}No fundamental, a corda é meio lambda: [p=0.1] lambda é o dobro, um vírgula dois metro. [p=0.2] {b}Vê é um vírgula dois vezes trezentos: [p=0.1] trezentos e sessenta metros por segundo. [p=0.3] {c}Terceiro harmônico: três vezes o fundamental, [p=0.1] {d}novecentos hertz."),
    # questão 4
    dict(id="s10", block="q4", text="Questão quatro. [p=0.2] {a}Um tubo aberto nas duas pontas, de meio metro, está perto de um alto-falante. [p=0.2] {b}O som anda a trezentos e quarenta metros por segundo. [p=0.3] {c}Em qual destas frequências o tubo ressoa: [p=0.1] duzentos, trezentos e quarenta, ou quinhentos e dez hertz? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s11", block="q4", text="{a}Tubo aberto: dois ele, um metro. [p=0.2] {b}Fundamental: trezentos e quarenta dividido por um, trezentos e quarenta hertz. [p=0.2] {c}Os próximos harmônicos são seiscentos e oitenta, mil e vinte, e assim por diante. [p=0.3] {d}Só trezentos e quarenta está na lista: [p=0.1] ressonância. [p=0.2] {e}Quinhentos e dez é um vírgula cinco vezes o fundamental: não serve."),
    # questão 5
    dict(id="s12", block="q5", text="Questão cinco. [p=0.2] {a}Você está num carro a trinta e quatro metros por segundo, [p=0.1] indo na direção de uma sirene parada de quinhentos hertz. [p=0.3] {b}Que frequência você ouve? [p=0.2] {c}Pause e tente. [p=3.0]"),
    dict(id="s13", block="q5", text="{a}Aproximou: a resposta é maior que quinhentos. [p=0.2] {b}Quem se move é o observador: mais em cima. [p=0.1] {c}A fonte está parada: embaixo, só trezentos e quarenta. [p=0.3] {d}Trezentos e quarenta mais trinta e quatro, trezentos e setenta e quatro, [p=0.1] dividido por trezentos e quarenta: um vírgula um. [p=0.2] {e}Quinhentos vezes um vírgula um: quinhentos e cinquenta hertz."),
    # fechamento
    dict(id="s14", block="fim", text="Resumindo: {a}decibéis, conte as dezenas; [p=0.1] {b}instrumentos, o timbre; [p=0.1] {c}cordas e tubos, múltiplos do fundamental; [p=0.1] {d}Doppler, aproximou, subiu. [p=0.3] Na próxima aula, você conhece {e}o espectro eletromagnético, do rádio ao raio gama. [p=0.3] {f}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {g}Bons estudos!"),
]
