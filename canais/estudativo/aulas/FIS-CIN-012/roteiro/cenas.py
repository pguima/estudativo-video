# Estudativo · FIS-CIN-012 — Gráfico velocidade por tempo: inclinação e área (Física · Cinemática · Gráficos do movimento).
# Habilidade: tirar a aceleração da inclinação e o deslocamento da área do gráfico v × t, e a variação de velocidade da área do gráfico a × t.
# Pré-requisitos: FIS-CIN-011 (gráfico s × t), FIS-CIN-007 (aceleração), MAT-ARE-003 (triângulo), MAT-ARE-004 (trapézio). Próxima: FIS-CIN-013.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Contas: 20/10 = 2 m/s²; 10·20/2 = 100 m; 10·5 = 50 m; (30+10)·4/2 = 80 m (= 10·4 + 5·4²/2); 2·5 = 10 m/s;
# questão: 12/6 = 2 m/s²; 6·12/2 + 10·12 = 36 + 120 = 156 m = (16+10)·12/2.

TITULO = "Gráfico velocidade por tempo: inclinação e área"

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
    dict(id="s01", block="gancho", text="{a}Um carro parte do repouso [p=0.2] e, ganhando velocidade sempre no mesmo ritmo, chega a {b}vinte metros por segundo em dez segundos. [p=0.3] {c}Quantos metros ele andou? [p=0.3] Dá para responder {d}sem fórmula nenhuma, [p=0.2] só com a área de {e}um triângulo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai tirar de um gráfico de velocidade {b}a aceleração [p=0.2] e {c}o deslocamento, [p=0.2] e de um gráfico de aceleração, {d}quanto a velocidade mudou."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a aceleração, que é quanto a velocidade muda dividido pelo tempo que levou; [p=0.2] e {c}a área do triângulo, base vezes altura dividido por dois. [p=0.3] Se faltar alguma, procure no canal."),
    # ler o gráfico
    dict(id="s04", block="ler", text="No gráfico de velocidade por tempo, {a}o eixo deitado é o tempo, em segundos, [p=0.2] e {b}o de pé é a velocidade, em metros por segundo. [p=0.3] Cada ponto diz {c}a velocidade naquele instante, [p=0.2] como uma foto do velocímetro."),
    dict(id="s05", block="ler", text="{a}Linha deitada: a velocidade não muda, é o movimento uniforme. [p=0.3] {b}Linha subindo: o carro acelera. [p=0.2] {c}Linha descendo: o carro freia."),
    # inclinação
    dict(id="s06", block="inclinacao", text="No gráfico de posição, a inclinação da reta era a velocidade. [p=0.3] Aqui, a inclinação é {a}a aceleração. [p=0.3] Inclinação é {b}quanto a linha sobe [p=0.1] dividido por {c}quanto ela anda para o lado."),
    dict(id="s07", block="inclinacao", text="No carro do começo, a linha sobe {a}vinte metros por segundo [p=0.1] enquanto anda {b}dez segundos. [p=0.3] {c}Vinte dividido por dez: [p=0.1] {d}dois metros por segundo ao quadrado. [p=0.3] A cada segundo, o carro ganha dois metros por segundo."),
    # área
    dict(id="s08", block="area", text="E a área? [p=0.2] Comece pelo mais simples: {a}velocidade constante de dez metros por segundo, durante cinco segundos. [p=0.3] Você já sabe que a distância é {b}velocidade vezes tempo: [p=0.2] {c}cinquenta metros. [p=0.3] Mas dez vezes cinco é {d}a área deste retângulo."),
    dict(id="s09", block="area", text="A regra vale para qualquer linha: [p=0.2] {a}a área entre a linha e o eixo do tempo é o deslocamento. [p=0.3] No carro do começo, {b}um triângulo de base dez e altura vinte: [p=0.2] {c}dez vezes vinte, dividido por dois, [p=0.1] {d}cem metros."),
    dict(id="s10", block="area", text="Se o carro já estava andando, a figura vira {a}um trapézio. [p=0.2] Saiu de {b}dez e chegou a trinta metros por segundo em {c}quatro segundos. [p=0.3] {d}Área do trapézio: [p=0.1] base maior mais base menor, vezes a altura, dividido por dois. [p=0.3] Aqui, as bases são as velocidades, e a altura é o tempo. [p=0.3] {e}Trinta mais dez, quarenta, [p=0.1] vezes quatro, cento e sessenta, [p=0.1] dividido por dois: {f}oitenta metros."),
    dict(id="s11", block="area", text="E se a linha passar {a}para baixo do eixo, [p=0.2] a velocidade ficou negativa: [p=0.2] {b}o carro está voltando. [p=0.2] {c}Essa área conta com sinal de menos."),
    # gráfico a × t
    dict(id="s12", block="aceleracao", text="Por fim, {a}o gráfico de aceleração por tempo. [p=0.3] {b}Aceleração constante de dois metros por segundo ao quadrado, durante cinco segundos. [p=0.3] {c}A área, dois vezes cinco, [p=0.1] dá {d}dez metros por segundo. [p=0.3] Essa área não é distância: [p=0.2] é {e}quanto a velocidade mudou."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}ler o gráfico de velocidade como se fosse de posição. [p=0.3] {b}Em dez segundos, a linha está em vinte, [p=0.2] e a pessoa responde: {c}o carro está a vinte metros. [p=0.3] {d}Não. [p=0.2] Vinte é a velocidade, em metros por segundo. [p=0.3] {e}O caminho percorrido é a área: cem metros. [p=0.2] Antes de tudo, leia {f}o nome do eixo de pé."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] pense numa escada de três degraus: [p=0.1] {a}no topo, a posição, [p=0.1] {b}velocidade [p=0.1] e {c}aceleração. [p=0.3] {d}A inclinação desce um degrau: [p=0.2] posição dá velocidade, e velocidade dá aceleração. [p=0.3] {e}A área sobe um degrau: [p=0.2] aceleração dá a mudança de velocidade, e velocidade dá o deslocamento."),
    dict(id="s15", block="atalho", text="Funciona por causa das unidades. [p=0.2] {a}A inclinação divide pelo tempo: [p=0.2] metro por segundo, dividido por segundo, é metro por segundo ao quadrado. [p=0.3] {b}A área multiplica pelo tempo: [p=0.2] metro por segundo, vezes segundo, é metro. [p=0.3] {c}Não compensa quando a linha passa para baixo do eixo: [p=0.2] aí, separe as áreas, porque a de baixo conta com sinal de menos."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Um ônibus parte do repouso [p=0.1] e, sempre no mesmo ritmo, chega a {b}doze metros por segundo em seis segundos. [p=0.2] Depois, {c}mantém essa velocidade por mais dez segundos. [p=0.3] {d}Qual é a aceleração no começo? [p=0.2] {e}E quantos metros ele anda ao todo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Inclinação do primeiro trecho: [p=0.1] {b}doze dividido por seis, [p=0.1] {c}dois metros por segundo ao quadrado."),
    dict(id="s19", block="resposta", text="Agora, a área. [p=0.2] {a}O triângulo: seis vezes doze, dividido por dois, [p=0.1] trinta e seis metros. [p=0.3] {b}O retângulo: dez vezes doze, [p=0.1] cento e vinte metros. [p=0.3] {c}Ao todo, cento e cinquenta e seis metros. [p=0.3] A figura toda é um trapézio deitado: [p=0.1] as bases são os tempos, dezesseis e dez, e a altura é a velocidade, doze. [p=0.2] {d}Dezesseis mais dez, vezes doze, dividido por dois. [p=0.2] O mesmo resultado."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: no gráfico de velocidade, {a}a inclinação é a aceleração, [p=0.2] e {b}a área é o deslocamento. [p=0.3] No de aceleração, {c}a área é quanto a velocidade mudou."),
    dict(id="s21", block="fim", text="Na próxima aula, a aceleração vem da gravidade: [p=0.2] {a}a queda livre, [p=0.2] em que, sem o ar atrapalhar, tudo cai {b}ganhando dez metros por segundo a cada segundo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
