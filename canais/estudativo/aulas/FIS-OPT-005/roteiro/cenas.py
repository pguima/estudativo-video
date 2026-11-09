# Estudativo · FIS-OPT-005 — Reflexão total, dispersão e cor (Física · Óptica · Refração, lentes e olho humano).
# Habilidade: achar o ângulo limite com sen L = n menor/n maior, explicar fibra óptica, miragem e arco-íris e dizer a cor de
# um objeto sob uma luz colorida.
# Pré-requisitos: FIS-OPT-004 (n = c/v, lei de Snell). Próxima: FIS-OPT-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. sen 90° = 1 não é ângulo notável de MAT-TRI-003: a aula justifica (o cateto oposto
# fica do tamanho da hipotenusa). Espelhos esféricos (FIS-OPT-003) não estão em "Já ensinado": a ponte para lentes não os cita.
# Arco-íris: a reflexão no fundo da gota não é total (dito sem "total"). Miragem: ar quente perto do chão tem índice menor.

TITULO = "Reflexão total, dispersão e cor"

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
    dict(id="s01", block="gancho", text="{a}A internet chega até você presa dentro de um fio de vidro, [p=0.2] fino como um cabelo. [p=0.3] {b}O fio pode fazer curva, [p=0.2] e {c}a luz não escapa pelos lados. [p=0.3] O segredo é {d}a reflexão total."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}o ângulo limite, [p=0.2] explicar {c}a fibra óptica, a miragem e o arco-íris, [p=0.2] e dizer {d}a cor de um objeto sob uma luz colorida."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a lei de Snell, ene um vezes seno de i igual a ene dois vezes seno de r; [p=0.2] e {c}saindo para um meio de índice menor, o raio se afasta da normal. [p=0.3] Se faltar alguma, procure no canal."),
    # ângulo limite
    dict(id="s04", block="limite", text="Pense na luz {a}saindo do vidro para o ar. [p=0.2] {b}Ela se afasta da normal. [p=0.3] {c}Aumente o ângulo de incidência: [p=0.2] {d}o raio que sai vai deitando, cada vez mais rente à superfície."),
    dict(id="s05", block="limite", text="{a}Num certo ângulo, o raio sai deitado, a noventa graus da normal. [p=0.2] Esse é {b}o ângulo limite, L. [p=0.3] {c}Acima dele, a luz não sai mais: [p=0.2] {d}ela toda volta para dentro do vidro. [p=0.2] Isso é {e}a reflexão total."),
    dict(id="s06", block="limite", text="Para calcular, use a lei de Snell com {a}o raio de saída a noventa graus. [p=0.3] {b}O seno de noventa graus vale um, [p=0.2] porque ali o cateto oposto fica do tamanho da hipotenusa. [p=0.3] Sobra {c}seno de L igual ao ene menor dividido pelo ene maior."),
    dict(id="s07", block="limite", text="{a}Um material de índice dois, com ar do lado de fora: [p=0.2] {b}seno de L é um dividido por dois, um meio. [p=0.2] {c}L é trinta graus. [p=0.3] {d}Raio chegando com mais de trinta graus da normal fica preso."),
    dict(id="s08", block="limite", text="São {a}duas condições: [p=0.2] {b}a luz vai do meio de índice maior para o de índice menor, [p=0.2] e {c}chega com ângulo maior que o limite. [p=0.3] {d}Do ar para o vidro, nunca há reflexão total."),
    # aplicações
    dict(id="s09", block="usos", text="{a}Na fibra óptica, a luz entra por uma ponta [p=0.2] e {b}bate na parede sempre acima do ângulo limite. [p=0.3] {c}Reflete por inteiro, vai e volta em zigue-zague, [p=0.2] e {d}chega do outro lado, mesmo com o fio fazendo curva."),
    dict(id="s10", block="usos", text="{a}A miragem no asfalto quente funciona parecido. [p=0.2] {b}O ar colado no chão fica mais quente e com índice um pouco menor. [p=0.3] {c}A luz do céu que desce rasante vai se afastando da normal, [p=0.2] {d}até virar para cima. [p=0.3] Seu olho vê {e}o céu no chão, e parece uma poça d'água."),
    # dispersão
    dict(id="s11", block="cores", text="{a}A luz branca é a mistura de todas as cores. [p=0.3] {b}No vidro, cada cor tem um índice um pouco diferente: [p=0.2] {c}o violeta tem o maior índice e desvia mais; [p=0.2] {d}o vermelho tem o menor e desvia menos. [p=0.3] Num prisma, um bloco de vidro em forma de triângulo, as cores se separam: [p=0.2] isso é {e}a dispersão."),
    dict(id="s12", block="cores", text="{a}No arco-íris, cada gota de chuva faz isso. [p=0.2] {b}A luz do Sol refrata ao entrar na gota, [p=0.1] {c}reflete no fundo dela [p=0.1] e {d}refrata de novo ao sair. [p=0.3] Cada cor sai num ângulo diferente. [p=0.2] Por isso {e}você vê o arco-íris com o Sol nas costas."),
    # cor dos objetos
    dict(id="s13", block="objeto", text="E a cor de um objeto? [p=0.2] {a}Ele não tem luz própria: [p=0.2] {b}reflete umas cores e absorve as outras. [p=0.3] {c}A camiseta vermelha reflete o vermelho e absorve o resto. [p=0.2] {d}A branca reflete todas. [p=0.2] {e}A preta absorve todas."),
    dict(id="s14", block="objeto", text="Agora acenda {a}uma luz só azul. [p=0.3] {b}A camiseta vermelha não tem vermelho para refletir: [p=0.2] {c}ela parece preta. [p=0.3] E {d}uma camiseta branca, sob luz vermelha, parece vermelha."),
    # erro
    dict(id="s15", block="erro", text="O erro mais comum é {a}virar a fração do ângulo limite: [p=0.2] {b}ene maior dividido pelo ene menor. [p=0.3] {c}Com índice dois, isso dá seno igual a dois. [p=0.3] {d}Mas o seno nunca passa de um. [p=0.2] {e}Deu mais que um, a fração está de cabeça para baixo."),
    # atalho
    dict(id="s16", block="atalho", text="Agora, os atalhos de prova. [p=0.2] {a}Seno do limite: sempre o menor dividido pelo maior. [p=0.3] {b}Cor sob luz colorida: [p=0.2] {c}se o objeto reflete a cor da luz, ele aparece com essa cor; [p=0.2] {d}se não reflete, aparece preto. [p=0.3] {e}E na dispersão, violeta desvia mais, vermelho desvia menos."),
    dict(id="s17", block="atalho", text="Funciona porque o objeto só devolve a luz que recebe: [p=0.2] {a}ele não cria cor nenhuma. [p=0.3] {b}Cuidado só com luz misturada, como a amarela de algumas lâmpadas, que pode ter várias cores: [p=0.2] aí, {c}leia o que a questão diz sobre a luz."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Um raio vai de {a}um cristal de índice raiz de dois para o ar. [p=0.3] {b}Qual é o ângulo limite? [p=0.2] E {c}se o raio chegar a sessenta graus da normal, [p=0.2] ele sai ou reflete por inteiro?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Seno de L é o menor dividido pelo maior: [p=0.2] {b}um dividido por raiz de dois. [p=0.2] {c}Racionalizando, com raiz de dois em cima e embaixo, [p=0.1] fica raiz de dois dividido por dois. [p=0.3] {d}O ângulo com esse seno é quarenta e cinco graus."),
    dict(id="s21", block="resposta", text="{a}Sessenta é mais que quarenta e cinco, [p=0.2] e a luz vai do índice maior para o menor. [p=0.3] {b}As duas condições valem: reflexão total. [p=0.2] O raio não sai."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}seno de L é o ene menor dividido pelo maior; [p=0.2] {b}reflexão total só do índice maior para o menor, acima do limite; [p=0.2] e {c}o objeto só aparece com uma cor se reflete essa cor."),
    dict(id="s23", block="fim", text="Na próxima aula, o vidro {a}ganha curva: [p=0.2] {b}as lentes, [p=0.2] que juntam ou espalham a luz e formam imagens. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
