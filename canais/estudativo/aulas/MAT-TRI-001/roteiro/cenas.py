# Estudativo · MAT-TRI-001 — Seno, cosseno e tangente no triângulo retângulo (Matemática · Trigonometria).
# Habilidade: apontar cateto oposto, cateto adjacente e hipotenusa e calcular sen = 0,6, cos = 0,8 e tg = 0,75 para o ângulo oposto ao lado 3 no triângulo 3-4-5.
# Pré-requisitos: MAT-ANG-015 (catetos e hipotenusa, Pitágoras), MAT-ANG-012 (semelhança: mesmos ângulos, lados proporcionais), MAT-FRA-019 (fração em decimal). Próxima: MAT-TRI-002.
# Questão inédita, criada para esta aula. Seno, cosseno e tangente narrados por extenso; na tela, sen, cos e tg. Ângulo narrado "alfa" (α).
# Dividir por decimal (MAT-FRA-018) fora da ficha: no atalho, 3/5 ÷ 4/5 explicado pelos quintos que se cancelam.
# Contas: 3-4-5, α oposto ao 3 · sen α = 3/5 = 0,6 · cos α = 4/5 = 0,8 · tg α = 3/4 = 0,75 · 6-8-10: 6/10 = 0,6.
# Erro: ângulo oposto ao 4 com "oposto = 3" decorado → 0,6; certo: sen = 4/5 = 0,8.
# Atalho: tg = sen/cos = (3/5)/(4/5) = 3/4 = 0,75 · sen e cos de ângulo agudo < 1 (hipotenusa é o maior lado).
# Questão: catetos 5 e 12 · 25 + 144 = 169 · hipotenusa 13 · ângulo oposto ao 12: sen = 12/13, cos = 5/13, tg = 12/5 = 2,4.
# Visual (E.triangulo, E.angulo):
#   s01: triângulo 3-4-5 e, ao lado, o 6-8-10 (mesma forma, dobrado); 3/5 = 0,6 e 6/10 = 0,6.
#   s04-s05: 3-4-5 com o quadradinho do reto e α marcado com arco; rótulos "oposto", "adjacente", "hipotenusa" aparecendo em cada lado.
#   s06-s08: as três definições como frações de lados (sen α = CO/H, cos α = CA/H, tg α = CO/CA), cada uma com o par de lados aceso no triângulo.
#   s10-s11: o mesmo triângulo com o outro ângulo agudo marcado; rótulos oposto e adjacente trocando de lugar; 0,6 riscado em vermelho.
#   s15-s18: triângulo de catetos 5 e 12, ângulo de frente para o 12 marcado, hipotenusa "?" virando 13.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Seno, cosseno e tangente no triângulo retângulo"

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
    dict(id="s01", block="gancho", text="{a}Um triângulo retângulo de catetos três e quatro, e hipotenusa cinco. [p=0.2] {b}Outro com o dobro do tamanho: catetos seis e oito, e hipotenusa dez. [p=0.3] Divida o menor lado pelo maior, em cada um. [p=0.2] {c}No pequeno e no grande, dá zero vírgula seis. [p=0.3] Não é coincidência: é a base da trigonometria."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você dá nome a cada lado do triângulo retângulo [p=0.2] e calcula {b}seno, cosseno e tangente, [p=0.2] com um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}catetos e hipotenusa, do teorema de Pitágoras; [p=0.2] {c}triângulos com os mesmos ângulos têm lados proporcionais; [p=0.2] e {d}passar fração para decimal, como três quintos, que dá zero vírgula seis. [p=0.3] Se faltar alguma, procure no canal."),
    # nomes
    dict(id="s04", block="nomes", text="Escolha {a}um dos ângulos agudos, os que são menores que noventa graus. [p=0.2] Vamos chamá-lo de {b}alfa. [p=0.3] {c}A hipotenusa continua sendo o lado de frente para o ângulo reto."),
    dict(id="s05", block="nomes", text="Os catetos ganham nomes novos. [p=0.2] {a}Cateto oposto é o que fica de frente para alfa. [p=0.2] {b}Cateto adjacente é o cateto que encosta em alfa: adjacente quer dizer vizinho. [p=0.3] No nosso triângulo, com alfa de frente para o três: [p=0.2] {c}o oposto é o três, [p=0.2] {d}o adjacente é o quatro [p=0.2] e {e}a hipotenusa é o cinco."),
    # razões
    dict(id="s06", block="razoes", text="Agora, três divisões. [p=0.2] {a}Seno de alfa é o cateto oposto dividido pela hipotenusa: [p=0.2] {b}três quintos, que dá zero vírgula seis. [p=0.3] Na tela e na prova, o nome vem {c}abreviado."),
    dict(id="s07", block="razoes", text="{a}Cosseno de alfa é o cateto adjacente dividido pela hipotenusa: [p=0.2] {b}quatro quintos, que dá zero vírgula oito."),
    dict(id="s08", block="razoes", text="{a}Tangente de alfa é o cateto oposto dividido pelo adjacente: [p=0.2] {b}três quartos, que dá zero vírgula setenta e cinco."),
    dict(id="s09", block="razoes", text="E por que o triângulo maior deu {a}o mesmo zero vírgula seis? [p=0.2] Com todos os lados dobrados, {b}o pequeno e o grande são semelhantes, com os mesmos ângulos. [p=0.2] {c}Seis dividido por dez dá zero vírgula seis de novo. [p=0.3] Seno, cosseno e tangente {d}dependem só do ângulo, não do tamanho do triângulo."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}decorar o lado, e não a posição. [p=0.2] Troque de ângulo: pegue {b}o ângulo de frente para o quatro. [p=0.2] Quem decorou que o oposto é o três {c}diz que o seno dá zero vírgula seis."),
    dict(id="s11", block="erro", text="Mas agora {a}o oposto é o quatro, [p=0.2] e {b}o adjacente é o três. [p=0.2] O seno desse ângulo é {c}quatro quintos, que dá zero vírgula oito. [p=0.3] {d}Oposto e adjacente mudam com o ângulo. [p=0.2] {e}Só a hipotenusa fica sempre no mesmo lugar."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}a tangente é o seno dividido pelo cosseno. [p=0.3] {b}Três quintos dividido por quatro quintos: [p=0.2] os pedaços são do mesmo tamanho, então é só {c}três dividido por quatro. [p=0.2] {d}A mesma tangente, zero vírgula setenta e cinco."),
    dict(id="s13", block="atalho", text="Funciona porque {a}seno e cosseno têm a mesma hipotenusa embaixo, [p=0.2] e {b}ela se cancela na divisão. [p=0.2] Sobra {c}oposto dividido por adjacente. [p=0.3] Serve quando a questão dá o seno e o cosseno, e não os lados. [p=0.2] Não compensa quando você já tem {d}os lados: [p=0.2] aí, divida direto."),
    dict(id="s14", block="atalho", text="E uma conferência rápida: [p=0.2] {a}seno e cosseno de ângulo agudo são sempre menores que um, [p=0.2] porque {b}a hipotenusa, embaixo, é o maior lado. [p=0.3] Deu mais que um? [p=0.2] {c}Algum lado foi trocado: refaça os nomes."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um triângulo retângulo tem catetos {a}cinco e doze. [p=0.3] Para o ângulo {b}de frente para o doze, [p=0.2] {c}calcule o seno, o cosseno e a tangente."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Primeiro, a hipotenusa, por Pitágoras: [p=0.2] {a}vinte e cinco mais cento e quarenta e quatro dá cento e sessenta e nove. [p=0.2] {b}A raiz dá treze. [p=0.3] Para esse ângulo, {c}o oposto é o doze [p=0.2] e {d}o adjacente é o cinco."),
    dict(id="s18", block="resposta", text="{a}O seno dá doze treze avos. [p=0.2] {b}O cosseno dá cinco treze avos. [p=0.2] {c}A tangente é doze dividido por cinco, que dá dois vírgula quatro. [p=0.3] A tangente {d}pode passar de um, porque não tem a hipotenusa embaixo."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}seno é oposto dividido pela hipotenusa, [p=0.2] {b}cosseno é adjacente dividido pela hipotenusa [p=0.2] e {c}tangente é oposto dividido pelo adjacente."),
    dict(id="s20", block="fim", text="Na próxima aula, o caminho de volta: [p=0.2] você sabe {a}o ângulo e um lado, [p=0.2] e acha {b}o lado que falta, [p=0.2] como {c}o cateto de frente para trinta e sete graus numa hipotenusa de dez. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
