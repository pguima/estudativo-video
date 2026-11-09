# Estudativo · FIS-MOD-002 — Efeito fotoelétrico (Física · Física Moderna · Quantização, dualidade e relatividade).
# Habilidade: usar Ec = h·f − W e explicar por que a frequência, e não a intensidade, arranca o elétron.
# Pré-requisitos: FIS-MOD-001 (E = h·f, elétron-volt). Próxima: FIS-MOD-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Energia cinética (FIS-ENE-002) não está em "Já ensinado": entra só como nome da energia de movimento, sem fórmula.
# Funções trabalho (valores de tabela, arredondados): sódio 2,3 eV (2,28), zinco 4,3 eV. Einstein explicou o efeito em 1905
# e ganhou o Nobel de 1921 por isso. Gráfico Ec × f é função afim (MAT-FUN-009): inclinação h, corta o eixo f em f₀.

TITULO = "Efeito fotoelétrico"

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
    dict(id="s01", block="gancho", text="{a}Jogue uma luz vermelha fortíssima numa placa de zinco: [p=0.2] {b}nada acontece. [p=0.3] {c}Troque por uma luz ultravioleta de frequência bem alta, mas fraquinha: [p=0.2] {d}elétrons saltam da placa na hora. [p=0.3] Luz fraca vence luz forte. [p=0.2] Por quê?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a energia do elétron que sai do metal [p=0.2] e {b}explicar por que quem manda é a frequência, [p=0.1] {c}e não a intensidade da luz."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a energia de um fóton é agá vezes efe; [p=0.2] e {c}um elétron-volt vale um vírgula seis vezes dez elevado a menos dezenove joule. [p=0.3] Se faltar alguma, procure no canal."),
    # o efeito
    dict(id="s04", block="efeito", text="Quando a luz certa bate num metal, [p=0.2] {a}ela arranca elétrons da superfície. [p=0.2] Isso é o {b}efeito fotoelétrico, [p=0.1] e os elétrons que saem se chamam {c}fotoelétrons. [p=0.3] {d}Quem explicou foi Einstein, em mil novecentos e cinco. [p=0.2] {e}Foi por isso, e não pela relatividade, que ele ganhou o prêmio Nobel."),
    dict(id="s05", block="efeito", text="A explicação tem uma regra só: [p=0.2] {a}cada fóton entrega toda a sua energia a um único elétron. [p=0.3] {b}Não existe meio fóton, [p=0.1] {c}e um elétron não junta a energia de vários fótons."),
    # função trabalho
    dict(id="s06", block="trabalho", text="Mas o elétron está preso ao metal. [p=0.2] Pense numa {a}bola no fundo de um buraco: [p=0.2] para tirar a bola dali, {b}você gasta uma energia mínima. [p=0.3] No metal, essa energia mínima se chama {c}função trabalho, [p=0.1] a letra é {d}dáblio, [p=0.2] e {e}cada metal tem a sua. [p=0.2] {f}Sódio, dois vírgula três elétron-volts. [p=0.1] {g}Zinco, quatro vírgula três."),
    dict(id="s07", block="trabalho", text="{a}Se o fóton tem menos energia que a função trabalho, [p=0.2] o elétron não sai. [p=0.3] {b}Se tem mais, o elétron sai, [p=0.2] e {c}o que sobra vira energia de movimento, [p=0.1] que se chama {d}energia cinética. [p=0.2] A fórmula dela é assunto de outra aula."),
    # a equação
    dict(id="s08", block="conta", text="{a}A equação é uma conta de sobra: [p=0.2] {b}energia cinética igual a agá vezes efe menos dáblio. [p=0.3] {c}Agá vezes efe é a energia que chega com o fóton. [p=0.2] {d}Dáblio é o preço para sair. [p=0.2] {e}E a energia cinética é o troco: [p=0.1] o máximo que o elétron leva."),
    dict(id="s09", block="conta", text="Vamos usar. [p=0.2] O fóton ultravioleta da aula passada tem {a}três vírgula três elétron-volts. [p=0.2] Ele bate no {b}sódio. [p=0.3] {c}Três vírgula três menos dois vírgula três: [p=0.2] {d}o elétron sai com um elétron-volt de energia cinética."),
    dict(id="s10", block="conta", text="{a}Já o fóton vermelho, de um vírgula sessenta e cinco elétron-volt, [p=0.2] {b}não paga os dois vírgula três do sódio. [p=0.3] {c}Nenhum elétron sai. [p=0.2] {d}A frequência em que o fóton paga exatamente o preço se chama {e}frequência de corte. [p=0.2] Abaixo dela, nada acontece."),
    # intensidade
    dict(id="s11", block="brilho", text="E a luz mais forte? [p=0.2] {a}Luz mais intensa é mais fótons por segundo. [p=0.3] {b}Acima do corte, mais fótons arrancam mais elétrons, [p=0.2] {c}mas cada um sai com a mesma energia. [p=0.3] {d}Abaixo do corte, mais fótons fracos continuam não arrancando nada. [p=0.2] {e}A frequência decide se sai, [p=0.1] {f}a intensidade decide quantos saem."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com {a}misturar unidades. [p=0.3] A questão dá o fóton em joule e a função trabalho em elétron-volt. [p=0.2] A pessoa faz {b}cinco vírgula vinte e oito vezes dez elevado a menos dezenove, menos dois vírgula três, [p=0.2] e a conta dá {c}praticamente menos dois vírgula três: energia negativa, impossível. [p=0.3] {d}Antes de subtrair, passe tudo para a mesma unidade: [p=0.2] {e}os cinco vírgula vinte e oito vezes dez elevado a menos dezenove joules são os três vírgula três elétron-volts."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}faça o gráfico da energia cinética pela frequência. [p=0.3] {b}A partir da frequência de corte, ele é uma reta, como numa função afim. [p=0.2] {c}A reta corta o eixo da frequência na frequência de corte. [p=0.2] {d}E, com a energia em joule, a inclinação dela é a constante agá."),
    dict(id="s14", block="atalho", text="Por isso, {a}num gráfico com metais diferentes, as retas são paralelas: [p=0.2] {b}a inclinação é agá, igual para todos. [p=0.3] {c}Muda só onde cada uma corta o eixo. [p=0.2] {d}O metal que corta mais à direita tem a maior função trabalho. [p=0.3] {e}Não compensa quando a questão não dá gráfico: [p=0.1] aí, use a equação."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Fótons de seis vírgula seis elétron-volts batem numa placa de zinco, [p=0.1] de função trabalho quatro vírgula três elétron-volts. [p=0.3] {b}Com que energia cinética sai cada elétron? [p=0.3] E {c}se a intensidade da luz dobrar, o que muda?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Seis vírgula seis é mais que quatro vírgula três: [p=0.1] o elétron sai. [p=0.3] {b}Energia cinética igual a seis vírgula seis menos quatro vírgula três: [p=0.2] {c}dois vírgula três elétron-volts."),
    dict(id="s18", block="resposta", text="{a}Com o dobro da intensidade, chegam o dobro de fótons. [p=0.2] {b}Saem o dobro de elétrons, [p=0.2] {c}mas cada um continua com dois vírgula três elétron-volts. [p=0.3] {d}A energia de cada elétron só muda se a frequência mudar."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}cada fóton entrega tudo a um elétron; [p=0.2] {b}a energia cinética é agá vezes efe menos dáblio; [p=0.2] e {c}a frequência decide se sai, a intensidade decide quantos."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}o elétron salta entre degraus dentro do átomo, [p=0.2] e você vai ver {b}como cada salto pinta a luz com uma cor. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
