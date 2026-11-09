# Estudativo · FIS-ENE-001 — Trabalho de uma força (Física · Energia e Colisões · Trabalho e energia).
# Habilidade: calcular τ = F·d·cos θ, dizer quando o trabalho é zero ou negativo e usar a área do gráfico F × d.
# Pré-requisitos: FIS-DIN-002 (F = m·a, newton), FIS-CIN-003 (componente F·cos θ), MAT-TRI-008 (cos 0°, 90°, 180°),
#   MAT-ARE-003 (área do triângulo). Próxima: FIS-ENE-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Primeira aula da trilha: o cabeçalho do visual.py guarda a linguagem visual de Energia e Colisões. Questão inédita.
# Peso (FIS-DIN-004), normal e atrito NÃO estão em "Já ensinado": as forças vêm com valor dado; a força do chão é
#   "a força que o chão faz, para cima". Energia só aparece na ponte para a próxima aula.
# Contas: 20 · 10 = 200 J; 50 · 10 · cos 60° = 500 · 0,5 = 250 J (erro sem cosseno: 500 J); freio −2.000 · 20 = −40.000 J;
#   área triângulo 5 · 40 / 2 = 100 J; questão 100 · 8 · 0,5 = 400 J e força do chão a 90°: zero.

TITULO = "Trabalho de uma força"

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
    dict(id="s01", block="gancho", text="{a}Você segura uma mochila pesada, parada, por dez minutos. [p=0.2] O braço {b}cansa. [p=0.3] Mas, para a Física, a força que você fez na mochila realizou {c}trabalho zero."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular o trabalho de uma força, [p=0.2] dizer quando ele é {b}zero ou negativo [p=0.2] e tirar o trabalho {c}da área de um gráfico."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}força se mede em newton, o N; [p=0.2] e {c}a parte de uma força inclinada que fica ao longo do chão é a força vezes o cosseno do ângulo. [p=0.3] Cosseno de zero grau é um, de noventa é zero, e de cento e oitenta, menos um. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é trabalho
    dict(id="s04", block="ideia", text="Na Física, {a}trabalho é o que uma força faz quando o corpo se desloca. [p=0.2] Sem deslocamento, {b}não há trabalho, [p=0.2] por mais que você se esforce. [p=0.3] Por isso a mochila parada dá zero: {c}o deslocamento é zero."),
    dict(id="s05", block="ideia", text="Quando a força tem {a}a mesma direção e o mesmo sentido do deslocamento, [p=0.2] o trabalho é {b}a força vezes a distância: [p=0.2] {c}tau igual a efe vezes dê. [p=0.3] Tau é essa letra grega, o símbolo do trabalho. [p=0.2] {d}Efe é a força, em newton, [p=0.1] e {e}dê é o deslocamento, em metro."),
    dict(id="s06", block="ideia", text="A unidade é {a}newton vezes metro, [p=0.2] que ganhou um nome: {b}joule, com a letra jota. [p=0.3] Empurre um carrinho de supermercado com {c}vinte newtons por dez metros: [p=0.2] {d}vinte vezes dez, duzentos joules."),
    # força inclinada
    dict(id="s07", block="inclinada", text="E se a força for inclinada? [p=0.2] Você puxa {a}uma mala de rodinhas pela alça, com cinquenta newtons, [p=0.2] e {b}a alça faz sessenta graus com o chão. [p=0.3] Só {c}a parte da força ao longo do chão ajuda a mala a andar. [p=0.2] {d}A parte para cima não leva a mala para a frente."),
    dict(id="s08", block="inclinada", text="Essa parte é {a}a força vezes o cosseno do ângulo. [p=0.2] Por isso, a fórmula completa é {b}tau igual a efe vezes dê vezes cosseno de teta, [p=0.2] e {c}teta é o ângulo entre a força e o deslocamento."),
    dict(id="s09", block="inclinada", text="Na mala, andando dez metros: [p=0.2] {a}cinquenta vezes dez vezes cosseno de sessenta. [p=0.2] {b}Cosseno de sessenta graus é meio. [p=0.2] {c}Cinquenta vezes dez, quinhentos; [p=0.1] {d}vezes meio, duzentos e cinquenta joules."),
    # zero e negativo
    dict(id="s10", block="sinais", text="Há dois casos especiais. [p=0.2] {a}Força em pé, a noventa graus do deslocamento: [p=0.2] {b}cosseno de noventa é zero, [p=0.2] e o trabalho {c}é zero. [p=0.3] Ande no plano, sem acelerar, com a mochila na mão: [p=0.2] {d}sua força aponta para cima, [p=0.1] o caminho é para a frente, [p=0.2] e {e}ela não faz trabalho."),
    dict(id="s11", block="sinais", text="{a}Força contra o movimento, a cento e oitenta graus: [p=0.2] {b}cosseno de cento e oitenta é menos um, [p=0.2] e o trabalho {c}fica negativo. [p=0.3] É o freio de um carro: [p=0.1] {d}dois mil newtons contra o movimento, por vinte metros, [p=0.2] {e}dão menos quarenta mil joules. [p=0.2] O sinal de menos diz que {f}essa força atrapalha o movimento."),
    dict(id="s12", block="sinais", text="Juntando os sinais: [p=0.2] {a}a força ajuda, trabalho positivo; [p=0.2] {b}a força atrapalha, negativo; [p=0.2] {c}a força é perpendicular ao caminho, zero."),
    # gráfico
    dict(id="s13", block="grafico", text="Veja o gráfico. [p=0.2] Ponha {a}a força no eixo vertical [p=0.1] e {b}o deslocamento no horizontal. [p=0.3] Com a força constante de vinte newtons, a linha é {c}reta e deitada. [p=0.2] Até dez metros, a região embaixo dela é {d}um retângulo de vinte por dez: [p=0.2] {e}duzentos, o mesmo trabalho do carrinho."),
    dict(id="s14", block="grafico", text="{a}No gráfico da força pelo deslocamento, a área é o trabalho. [p=0.3] E isso vale mesmo quando a força muda. [p=0.2] Se ela {b}cresce de zero a quarenta newtons em cinco metros, [p=0.2] a área é {c}um triângulo: [p=0.1] base vezes altura, dividido por dois. [p=0.2] {d}Cinco vezes quarenta, duzentos, dividido por dois: [p=0.1] {e}cem joules."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer o cosseno. [p=0.2] Na mala, a pessoa faz {b}cinquenta vezes dez [p=0.1] e responde {c}quinhentos joules."),
    dict(id="s16", block="erro", text="Mas {a}a parte da força para cima não ajuda a mala a andar. [p=0.2] Só {b}metade da força trabalha, [p=0.1] e o certo é {c}duzentos e cinquenta joules, [p=0.2] metade do que a pessoa respondeu. [p=0.3] {d}Sem o cosseno, a conta só vale para força deitada no mesmo sentido do caminho."),
    # atalho
    dict(id="s17", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}antes de qualquer conta, compare a força com o caminho. [p=0.3] {b}Força perpendicular ao caminho? Trabalho zero, sem conta nenhuma. [p=0.2] {c}Força contra o caminho? O sinal já é menos. [p=0.3] Muita questão pergunta só isso, [p=0.2] como {d}o trabalho da força que o chão faz, para cima, num carro andando no plano: [p=0.2] {e}zero."),
    dict(id="s18", block="atalho", text="Funciona porque {a}o cosseno de noventa é zero, e ele zera a conta inteira. [p=0.3] {b}Não compensa quando a força é inclinada e a questão pede o valor: [p=0.2] aí, faça a conta com o cosseno."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Uma pessoa puxa {a}um caixote com uma corda que faz sessenta graus com o chão. [p=0.2] A força na corda é de {b}cem newtons, [p=0.2] e o caixote anda {c}oito metros. [p=0.3] {d}Qual é o trabalho da força da corda? [p=0.2] {e}E o da força que o chão faz no caixote, para cima?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] {a}Tau igual a efe vezes dê vezes cosseno de teta: [p=0.2] {b}cem vezes oito vezes cosseno de sessenta. [p=0.2] {c}Cem vezes oito, oitocentos. [p=0.2] {d}Vezes meio: quatrocentos joules."),
    dict(id="s22", block="resposta", text="E a força do chão {a}aponta para cima, [p=0.1] {b}a noventa graus do caminho. [p=0.2] {c}Trabalho zero, sem conta nenhuma."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}trabalho é força vezes deslocamento vezes cosseno do ângulo, em joule; [p=0.2] {b}força perpendicular dá zero, e força contra dá negativo; [p=0.2] e {c}no gráfico, a área é o trabalho."),
    dict(id="s24", block="fim", text="Na próxima aula, você vai ver {a}a potência, [p=0.1] a rapidez com que o trabalho é feito, [p=0.2] e {b}o rendimento, a parte do que uma máquina recebe que vira trabalho útil. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
