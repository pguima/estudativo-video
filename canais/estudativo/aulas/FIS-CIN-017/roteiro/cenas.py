# Estudativo · FIS-CIN-017 — Praticando: gráficos, queda e lançamentos (Física · Cinemática · prática).
# Habilidade: ler gráficos do movimento e resolver questões de queda e lançamentos.
# Pré-requisitos: FIS-CIN-011, 012, 013, 014, 015, 016, 003. Próxima: FIS-CIN-018.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula.
# Contas: Q1 a = (0 − 20)/4 = −5 m/s²; área 4·20/2 = 40 m (Torricelli: 400/10 = 40). Q2 125 = 5t² → t = 5 s; v = 50 m/s.
# Q3 voo 8 s → subida 4 s; v0 = 40 m/s; H = 5·16 = 80 m (= 1600/20). Q4 5 = 5t² → t = 1 s; A = 3 m; a 6 m/s → 6 m.
# Q5 30° e 60° complementares → mesmo alcance; 45° = maior.

TITULO = "Praticando: gráficos, queda e lançamentos"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, [p=0.2] criadas para esta aula, [p=0.2] com gráficos, quedas e lançamentos. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar: [p=0.2] {a}no gráfico de velocidade, inclinação é aceleração e área é deslocamento; [p=0.2] {b}na queda, altura igual a cinco tê ao quadrado e velocidade igual a dez tê; [p=0.2] {c}na subida, o mesmo tempo da descida; [p=0.2] {d}e, nos lançamentos, cada direção cuidando da sua vida. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: gráfico
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um carro a {b}vinte metros por segundo freia [p=0.1] e para em {c}quatro segundos. [p=0.2] No gráfico de velocidade por tempo, {d}é uma reta descendo até zero. [p=0.3] {e}Qual é a aceleração? [p=0.1] {f}E quantos metros o carro anda até parar?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Inclinação: a velocidade cai vinte em quatro segundos. [p=0.2] {b}Menos vinte dividido por quatro: [p=0.1] {c}menos cinco metros por segundo ao quadrado. [p=0.2] O sinal de menos diz que ele está freando. [p=0.3] {d}Distância: a área do triângulo, quatro vezes vinte, dividido por dois, [p=0.1] {e}quarenta metros. [p=0.3] {f}Confira com Torricelli: [p=0.1] a velocidade final é zero, [p=0.1] e, usando a freada sem o sinal, quatrocentos é igual a duas vezes cinco vezes a distância, [p=0.1] e a distância é quarenta. [p=0.2] Bateu."),
    # situação 2: queda livre
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Uma pedra cai do alto de {b}um penhasco de cento e vinte e cinco metros. [p=0.2] Despreze o ar. [p=0.3] {c}Quanto tempo ela leva [p=0.1] {d}e com que velocidade chega ao chão?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] {a}Cento e vinte e cinco igual a cinco tê ao quadrado. [p=0.2] {b}Tê ao quadrado é vinte e cinco, [p=0.1] {c}tê é cinco segundos. [p=0.3] {d}Velocidade: dez vezes cinco, cinquenta metros por segundo. [p=0.3] Cento e oitenta quilômetros por hora."),
    # atalho
    dict(id="s09", block="atalho", text="Aqui cabe o atalho: [p=0.2] {a}a tabela da queda. [p=0.2] {b}Cinco, vinte, quarenta e cinco, oitenta, cento e vinte e cinco metros, [p=0.2] {c}para um, dois, três, quatro e cinco segundos. [p=0.3] Viu cento e vinte e cinco, {d}são cinco segundos, sem conta. [p=0.2] {e}Fora da tabela, divida por cinco e tire a raiz."),
    # situação 3: lançamento vertical
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Uma bola é jogada para cima [p=0.1] e {b}volta à mão oito segundos depois. [p=0.3] {c}Com que velocidade ela foi lançada? [p=0.2] {d}E até que altura subiu?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] {a}Subida e descida levam o mesmo tempo: [p=0.2] {b}quatro segundos para subir. [p=0.3] Ela perde dez metros por segundo a cada segundo, até zero, [p=0.2] então {c}saiu com dez vezes quatro, quarenta metros por segundo. [p=0.3] {d}Altura: a descida é uma queda de quatro segundos, [p=0.1] {e}oitenta metros. [p=0.3] {f}Confira com Torricelli: mil e seiscentos dividido por vinte, oitenta."),
    # situação 4: lançamento horizontal
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] Uma bola sai rolando de {b}um telhado de cinco metros de altura, [p=0.2] na horizontal, a {c}três metros por segundo. [p=0.3] {d}A que distância da parede ela toca o chão? [p=0.2] {e}E se saísse com o dobro da velocidade?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] {a}O tempo vem da altura: cinco metros, um segundo de queda. [p=0.3] {b}Alcance: três vezes um, três metros. [p=0.3] Com o dobro da velocidade, {c}o tempo continua um segundo, [p=0.2] porque a altura manda no tempo. [p=0.2] {d}O alcance dobra: seis metros."),
    # situação 5: ângulos
    dict(id="s16", block="questao5", text="{a}Última situação, e ela não tem conta. [p=0.2] Dois jogadores chutam a bola do chão com a mesma velocidade, [p=0.2] {b}um a trinta graus e {c}outro a sessenta. [p=0.3] {d}Qual chega mais longe? [p=0.2] {e}E que ângulo daria o maior alcance?"),
    dict(id="s17", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta5", text="Vamos lá. [p=0.2] Trinta mais sessenta dá noventa: {a}são ângulos complementares. [p=0.2] {b}O seno de um é o cosseno do outro, [p=0.2] então {c}as duas bolas caem no mesmo ponto. [p=0.3] A de sessenta {d}sobe mais e demora mais. [p=0.3] {e}O maior alcance sai a quarenta e cinco graus, [p=0.2] porque a bola sai e chega na mesma altura e o ar foi desprezado."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}no gráfico, leia o eixo antes de tudo; [p=0.2] {b}na queda, a tabela do cinco; [p=0.2] {c}no lançamento, a altura manda no tempo."),
    dict(id="s20", block="fim", text="Na próxima aula, o movimento passa a {a}girar: [p=0.2] você vai entender {b}período, frequência e rotações por minuto, [p=0.2] como no {c}ventilador e na máquina de lavar. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
