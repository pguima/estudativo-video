# Estudativo · MAT-CNT-018 — Árvore de probabilidades (Matemática · Contagem e Probabilidade · União, interseção e condicional).
# Habilidade: multiplicar ao longo de cada caminho e somar os caminhos para achar a chance total de um evento, como a de um filho ter certa característica genética.
# Pré-requisitos: MAT-CNT-017 (sorteios sucessivos), MAT-FRA-008 (somar frações com denominadores diferentes). Próxima: MAT-CNT-019.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras narradas como se falam (á, bê); genética narrada como versão dominante e recessiva, com A e a na tela.
# Questão inédita, criada para esta aula. Evento complementar (MAT-CNT-013) não está em "Já ensinado": "o que falta para o inteiro" (como em MAT-FRA-008).
# Chuva (E.arvore com ramos em fração): chove 1/3 → atrasa 1/2, não atrasa 1/2 · não chove 2/3 → atrasa 1/4, não atrasa 3/4.
# Caminhos: 1/3 × 1/2 = 1/6 · 2/3 × 1/4 = 2/12 = 1/6 · soma 2/6 = 1/3. Pontas: 1/6 + 1/6 + 1/6 + 1/2 = 1.
# Genética (na tela: A e a; pai Aa, mãe Aa): pai passa A ou a (1/2), mãe A ou a (1/2): 4 pontas de 1/4.
# aa = 1/2 × 1/2 = 1/4 = 25% · exatamente um a (Aa ou aA) = 1/4 + 1/4 = 1/2. Erro: 1/4 (vê um caminho só).
# Atalho: corte os galhos que não chegam ao evento; não compensa com várias perguntas na mesma árvore (aí confira: pontas somam 1).
# Questão: máquina A 3/5 das peças, defeito 1/10 · B 2/5, defeito 1/20 → 3/50 + 2/100 = 3/50 + 1/50 = 4/50 = 8%.

TITULO = "Árvore de probabilidades"

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
    dict(id="s01", block="gancho", text="O pai e a mãe {a}não têm certa característica. [p=0.2] Mas cada um carrega, escondida, a versão do gene que a provoca. [p=0.3] Mesmo assim, {b}o filho pode nascer com ela? [p=0.2] Pode. [p=0.3] Com que chance? [p=0.3] Uma árvore desenhada em poucos segundos responde: [p=0.2] {c}um quarto."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você monta uma árvore de probabilidades, [p=0.2] sabe {b}quando multiplicar e quando somar [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}multiplicar as chances de etapas em sequência, como nos sorteios, [p=0.2] e {c}somar frações com denominadores diferentes. [p=0.3] Se faltar alguma, procure no canal."),
    # chuva
    dict(id="s04", block="chuva", text="Comece com o dia a dia. [p=0.2] A chance de {a}chover amanhã é um terço. [p=0.2] Se chover, a chance de você {b}chegar atrasado é um meio. [p=0.2] Se não chover, é {c}um quarto. [p=0.3] {d}Qual a chance de você se atrasar?"),
    dict(id="s05", block="chuva", text="Desenhe a árvore. [p=0.2] Do ponto de partida saem {a}dois galhos: chove, com um terço, [p=0.2] e não chove, com {b}dois terços, o que falta para o inteiro. [p=0.3] De cada um saem {c}mais dois galhos: atrasa ou não atrasa. [p=0.2] Em cada galho, {d}a chance escrita em cima."),
    dict(id="s06", block="chuva", text="Cada caminho do começo até a ponta é {a}uma história completa. [p=0.3] {b}Chove e atrasa: [p=0.2] um terço vezes um meio dá {c}um sexto. [p=0.3] {d}Não chove e atrasa: [p=0.2] dois terços vezes um quarto dá {e}dois doze avos, que simplifica para um sexto."),
    dict(id="s07", block="chuva", text="Você se atrasa {a}por um caminho ou pelo outro, [p=0.2] e eles não acontecem juntos: [p=0.2] ou choveu, ou não choveu. [p=0.2] Então {b}some. [p=0.2] {c}Um sexto mais um sexto dá dois sextos, [p=0.2] que é {d}um terço."),
    # regra
    dict(id="s08", block="regra", text="Essa é a regra da árvore: [p=0.2] {a}ao longo do caminho, multiplique. [p=0.2] {b}Entre caminhos, some. [p=0.3] Ao longo, as etapas acontecem {c}uma depois da outra: é a palavra e. [p=0.2] Entre caminhos, são histórias diferentes: {d}é a palavra ou."),
    # genética
    dict(id="s09", block="genetica", text="Agora a genética. [p=0.2] Cada pessoa tem {a}duas versões de um gene, [p=0.2] e passa {b}uma delas ao filho, ao acaso: [p=0.2] meio a meio. [p=0.3] Pense numa característica que só aparece quando o filho recebe {c}a versão recessiva do pai e também da mãe. [p=0.2] Na tela, a recessiva é o á minúsculo. [p=0.3] Recessiva quer dizer que ela fica escondida quando a outra versão, a dominante, está junto."),
    dict(id="s10", block="genetica", text="O pai tem {a}uma versão dominante e uma recessiva. [p=0.2] Na tela, a dominante é o á maiúsculo. [p=0.2] A mãe também tem uma de cada. [p=0.2] Por causa da dominante, {b}nem o pai nem a mãe mostram a característica."),
    dict(id="s11", block="genetica", text="Na árvore, {a}o pai passa a dominante ou a recessiva, com um meio cada. [p=0.2] Depois, {b}a mãe faz o mesmo. [p=0.2] São {c}quatro pontas."),
    dict(id="s12", block="genetica", text="O filho só tem a característica no caminho {a}recessiva do pai e recessiva da mãe. [p=0.2] {b}Um meio vezes um meio dá um quarto: [p=0.2] {c}vinte e cinco por cento."),
    dict(id="s13", block="genetica", text="E a chance de o filho {a}receber uma recessiva só, sem ter a característica? [p=0.2] Há {b}dois caminhos: [p=0.2] a recessiva vem do pai, [p=0.2] ou vem da mãe. [p=0.2] Cada caminho tem {c}um quarto. [p=0.2] {d}Um quarto mais um quarto dá um meio."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é {a}ver só um desses caminhos. [p=0.2] A pessoa trata receber uma recessiva como um caminho único, [p=0.2] e responde {b}um quarto. [p=0.3] Mas vir do pai e vir da mãe são {c}histórias diferentes na árvore. [p=0.2] Cada ponta conta. [p=0.2] Por isso, {d}um meio."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}corte os galhos que não interessam. [p=0.2] Desenhe só os caminhos que {b}chegam ao que a questão pede. [p=0.3] No atraso, você não precisa dos galhos {c}não atrasa: [p=0.2] eles não entram na soma."),
    dict(id="s16", block="atalho", text="Funciona porque {a}cada galho cortado daria uma ponta que você não somaria. [p=0.3] {b}Não compensa quando a questão faz várias perguntas sobre a mesma árvore. [p=0.2] Aí, desenhe a árvore inteira, [p=0.2] e confira: {c}todas as pontas somam um inteiro."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma fábrica tem {a}duas máquinas. [p=0.2] {b}A máquina á faz três quintos das peças, [p=0.2] e um décimo delas sai com defeito. [p=0.3] {c}A máquina bê faz o resto, [p=0.2] e um vinte avos das peças dela sai com defeito. [p=0.3] {d}Pegando uma peça ao acaso, qual a chance de ela ter defeito?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] A máquina bê faz {a}dois quintos, o que falta para o inteiro. [p=0.3] {b}Caminho á e defeito: [p=0.2] três quintos vezes um décimo dá {c}três cinquenta avos. [p=0.3] {d}Caminho bê e defeito: [p=0.2] dois quintos vezes um vinte avos dá {e}dois centésimos, que simplifica para um cinquenta avos."),
    dict(id="s20", block="resposta", text="Some os caminhos: {a}três cinquenta avos mais um cinquenta avos dá quatro cinquenta avos. [p=0.3] Em por cento, dá {b}oito por cento: [p=0.2] {c}oito em cada cem peças saem com defeito."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}ao longo do caminho, multiplique. [p=0.2] {b}Entre caminhos, some."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica {a}tudo de probabilidade: [p=0.2] contar, usar o complementar, somar ou multiplicar, [p=0.2] em questões de {b}sorteio e de genética. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
