# Estudativo · MAT-CON-007 — Intervalos: colchetes e reta (Matemática · Conjuntos · Conjuntos numéricos).
# Habilidade: ler ]2, 5] como os reais maiores que 2 e até 5, desenhar na reta com bolinha aberta e fechada e escrever a solução de 2x − 1 ≤ 5 como ]−∞, 3].
# Pré-requisitos: MAT-CON-006 (números reais), MAT-EQU-015 (inequação e bolinhas na reta). Próxima: MAT-CON-008.
# Questão inédita, criada para esta aula. Bolinha fechada = entra, aberta = fica de fora, como na MAT-EQU-015.
# Contas: π ≈ 3,14 e √10 ≈ 3,16 estão entre 2 e 5 · 2x − 1 ≤ 5 → 2x ≤ 6 → x ≤ 3 → ]−∞, 3] · erro: 4,9 ∈ ]2, 5].
# Questão: [−1, 4[: −1 entra, 4 não · 3x + 2 > 11 → 3x > 9 → x > 3 → ]3, +∞[.
# Visual: reta numérica com intervalos (E.reta + E.intervalo): ]2, 5], ]−∞, 3], [−1, 4[ e ]3, +∞[; colchetes grandes na tela.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Intervalos: colchetes e reta"

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
    dict(id="s01", block="gancho", text="{a}Quantos números reais existem entre dois e cinco? [p=0.3] Se você pensou em {b}três e quatro, [p=0.2] esqueceu {c}dois vírgula cinco, a raiz de dez, o pi. [p=0.3] São {d}infinitos. [p=0.2] E para escrever todos eles, basta {e}um par de colchetes."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê e escreve intervalos, [p=0.2] desenha na reta [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}os números reais, que são todos os pontos da reta, [p=0.2] e {c}inequação, com bolinha fechada quando o número entra e aberta quando fica de fora. [p=0.3] Se faltar alguma, procure no canal."),
    # intervalo
    dict(id="s04", block="intervalo", text="Um pedaço da reta se chama {a}intervalo. [p=0.2] Ele se escreve com {b}as duas pontas entre colchetes, [p=0.2] separadas por vírgula. [p=0.3] Cada colchete diz {c}se a ponta entra."),
    dict(id="s05", block="intervalo", text="{a}Colchete virado para o número, como quem abraça: [p=0.2] a ponta entra. [p=0.2] Esse lado é {b}fechado. [p=0.3] {c}Colchete de costas para o número: [p=0.2] a ponta fica de fora. [p=0.2] Esse lado é {d}aberto."),
    dict(id="s06", block="intervalo", text="Veja {a}este intervalo, de dois a cinco. [p=0.2] No dois, o colchete está de costas: {b}aberto. [p=0.2] No cinco, está abraçando: {c}fechado. [p=0.3] São {d}os reais maiores que dois e até cinco, com o cinco junto."),
    dict(id="s07", block="intervalo", text="Na reta, é o desenho da inequação: [p=0.2] {a}bolinha aberta no dois, [p=0.2] {b}bolinha fechada no cinco, [p=0.2] e {c}pinta o caminho entre elas. [p=0.3] Em inequação, {d}xis maior que dois e, ao mesmo tempo, menor ou igual a cinco."),
    dict(id="s08", block="intervalo", text="Os colchetes também podem ser iguais. [p=0.2] {a}Fechado nas pontas, de um a três: [p=0.2] o um e o três entram. [p=0.3] {b}Aberto nas pontas: o um e o três ficam de fora, [p=0.2] mas {c}tudo o que está entre eles continua lá, [p=0.2] até o dois vírgula nove nove."),
    # infinito
    dict(id="s09", block="infinito", text="E quando o pedaço não tem fim? [p=0.2] Entra o símbolo {a}do infinito, um oito deitado. [p=0.3] {b}Mais infinito, para a direita. [p=0.2] {c}Menos infinito, para a esquerda. [p=0.3] Infinito não é um número que se alcança, [p=0.2] então do lado dele o colchete é {d}sempre aberto."),
    dict(id="s10", block="infinito", text="Resolva {a}dois xis menos um, menor ou igual a cinco. [p=0.3] {b}Some um de cada lado: dois xis menor ou igual a seis. [p=0.2] {c}Divida cada lado por dois, que é positivo: [p=0.2] {d}xis menor ou igual a três."),
    dict(id="s11", block="infinito", text="Na reta, {a}bolinha fechada no três, [p=0.2] e pinta tudo {b}para a esquerda, sem fim. [p=0.3] Como intervalo: {c}de menos infinito até três, [p=0.2] fechado no três [p=0.2] e aberto no menos infinito, como sempre."),
    # erro
    dict(id="s12", block="erro", text="Volte ao intervalo do começo, aberto no dois e fechado no cinco. [p=0.2] O erro mais comum é escrever {a}chaves com três, quatro e cinco. [p=0.3] Chaves {b}listam elementos soltos. [p=0.2] O intervalo pega {c}todos os reais do pedaço: [p=0.2] {d}quatro vírgula nove está lá, [p=0.2] e a raiz de dez também. [p=0.3] {e}Chaves para listar, colchetes para um pedaço da reta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho para passar da inequação para o intervalo: [p=0.2] {a}olhe o tracinho embaixo do sinal. [p=0.3] {b}Tem tracinho, o colchete fecha. [p=0.2] {c}Sem tracinho, abre."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o tracinho é um pedaço do sinal de igual: [p=0.2] ele avisa que a ponta também serve. [p=0.3] {b}Não vale do lado do infinito: [p=0.2] ali, o colchete é sempre aberto. [p=0.3] E alguns livros usam {c}parênteses no lugar do colchete aberto. [p=0.2] Parêntese também quer dizer {d}ponta de fora."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Olhe este intervalo, de menos um a quatro. [p=0.2] {b}O menos um entra? [p=0.2] {c}E o quatro? [p=0.3] Depois, resolva {d}três xis mais dois, maior que onze, [p=0.2] e {e}escreva a resposta como intervalo."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] O colchete do menos um está abraçando: {a}o menos um entra. [p=0.2] O do quatro está de costas: {b}o quatro fica de fora. [p=0.3] Na reta, {c}bolinha fechada no menos um e aberta no quatro. [p=0.2] O três vírgula nove nove ainda está lá dentro."),
    dict(id="s18", block="resposta", text="Na inequação, {a}tire dois de cada lado: três xis maior que nove. [p=0.2] {b}Divida por três: xis maior que três. [p=0.3] Sem tracinho, {c}aberto no três. [p=0.2] Vai para a direita sem fim: [p=0.2] {d}de três até mais infinito, aberto nas pontas."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}colchete abraçando, a ponta entra. [p=0.2] {b}De costas, fica de fora. [p=0.2] E {c}no infinito, sempre aberto."),
    dict(id="s20", block="fim", text="Na próxima aula, você {a}cruza e junta intervalos, [p=0.2] {b}empilhando uma reta sobre a outra. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
