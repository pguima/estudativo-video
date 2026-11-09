# Estudativo · FIS-EGF-006 — Princípio de Pascal: prensa hidráulica (Física · Equilíbrio, Gravitação e Fluidos · Hidrostática).
# Habilidade: usar F1/A1 = F2/A2 no elevador de carro e dizer por que a força ganha cobra em distância.
# Pré-requisitos: FIS-EGF-005 (Stevin), FIS-EGF-004 (pressão), MAT-RAZ-002 (proporção), MAT-RAZ-010 (área ∝ quadrado).
# Próxima: FIS-EGF-007. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# "Trabalho" (FIS-ENE-001) não está em "Já ensinado": o preço do ganho é explicado pelo volume de óleo, A1·x1 = A2·x2.
# Contas: F1/10 = 10.000/1.000 → 100 N; 10·x1 = 1.000·1 → 100 cm; 1.000/20 = 50; 12.000/50 = 240 N; 4·50 = 200 cm.

TITULO = "Princípio de Pascal: prensa hidráulica"

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
    dict(id="s01", block="gancho", text="{a}No elevador hidráulico de uma oficina, um carro de uma tonelada sobe. [p=0.3] {b}E a força que empurra o pistão pequeno do elevador pode ser {c}cem vezes menor que o peso do carro. [p=0.3] O segredo é {d}um líquido preso num tubo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a força numa prensa hidráulica [p=0.2] e {b}dizer qual é o preço desse ganho de força."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}A pressão: força sobre área. [p=0.2] E {c}a lei de Stevin: num líquido parado, pontos na mesma altura têm a mesma pressão. [p=0.3] Se faltar alguma, procure no canal."),
    # princípio
    dict(id="s04", block="principio", text="{a}Aperte uma garrafa de água fechada. [p=0.2] {b}O aumento de pressão que a sua mão causa não fica só ali: [p=0.2] {c}ele chega igual a todos os pontos do líquido. [p=0.3] {d}Esse é o princípio de Pascal: [p=0.1] {e}o aumento de pressão num líquido preso se transmite inteiro para todo o líquido."),
    # prensa
    dict(id="s05", block="prensa", text="{a}A prensa hidráulica usa isso. [p=0.2] {b}São dois cilindros ligados, cheios de óleo, [p=0.1] {c}cada um com um pistão: uma tampa que desliza. [p=0.3] {d}Um é fino, de área á um. [p=0.1] {e}O outro é largo, de área á dois."),
    dict(id="s06", block="prensa", text="{a}Você empurra o pistão fino com a força efe um. [p=0.2] {b}A pressão que isso cria é efe um sobre á um. [p=0.2] {c}Ela chega inteira ao pistão largo, [p=0.1] que recebe {d}efe dois sobre á dois. [p=0.3] {e}As pressões são iguais: [p=0.1] efe um sobre á um igual a efe dois sobre á dois."),
    dict(id="s07", block="prensa", text="{a}Efe um e efe dois são as forças, em newtons. [p=0.2] {b}Á um e á dois são as áreas dos pistões. [p=0.3] {c}Como é uma igualdade de razões, [p=0.1] {d}não precisa converter a área para metro quadrado: [p=0.1] basta usar a mesma unidade nos dois lados."),
    dict(id="s08", block="prensa", text="{a}O carro pesa dez mil newtons [p=0.1] e está no pistão de mil centímetros quadrados. [p=0.2] {b}O pistão fino tem dez centímetros quadrados. [p=0.3] {c}Efe um sobre dez igual a dez mil sobre mil. [p=0.2] {d}Efe um sobre dez igual a dez, [p=0.1] {e}e efe um igual a cem newtons. [p=0.3] {f}Área cem vezes maior, força cem vezes maior."),
    # preço
    dict(id="s09", block="preco", text="{a}Mas ninguém ganha força de graça. [p=0.2] {b}O óleo que sai do cilindro fino entra no largo: [p=0.1] {c}o volume é o mesmo. [p=0.3] {d}E o volume é a área vezes o quanto o pistão anda. [p=0.2] {e}Área cem vezes maior, deslocamento cem vezes menor."),
    dict(id="s10", block="preco", text="{a}Para o carro subir um centímetro, [p=0.1] {b}o pistão fino tem que descer cem centímetros. [p=0.3] {c}A força ganha cobra em distância: [p=0.1] {d}força cem vezes menor, caminho cem vezes maior. [p=0.2] {e}Por isso o macaco hidráulico pede tantas bombadas."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a pressão é maior no pistão largo, porque a força lá é maior. [p=0.3] {b}A pressão é a mesma nos dois. [p=0.2] {c}A força é maior porque a mesma pressão age numa área maior. [p=0.3] {d}Quem multiplica a força é a área, não a pressão."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.2] {a}a razão das áreas é o ganho. [p=0.2] {b}Divida a área grande pela pequena: [p=0.1] esse número multiplica a força e divide o deslocamento. [p=0.3] {c}Se a questão der os diâmetros, [p=0.1] eleve a razão ao quadrado: [p=0.2] {d}diâmetro dez vezes maior, área cem vezes maior."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a área de um círculo cresce com o quadrado do diâmetro, [p=0.1] como a de qualquer figura ampliada. [p=0.3] {b}O erro clássico é usar a razão dos diâmetros direto: [p=0.1] dez, em vez de cem."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Num elevador hidráulico, o pistão pequeno tem vinte centímetros quadrados [p=0.1] {b}e o grande, mil. [p=0.3] {c}Que força no pistão pequeno sustenta um carro de doze mil newtons? [p=0.2] {d}E quanto o pistão pequeno desce para o carro subir quatro centímetros?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}O ganho: mil dividido por vinte, [p=0.1] {b}cinquenta vezes. [p=0.3] {c}A força: doze mil dividido por cinquenta, [p=0.1] {d}duzentos e quarenta newtons. [p=0.3] {e}O deslocamento: quatro centímetros vezes cinquenta, [p=0.1] {f}duzentos centímetros, [p=0.1] dois metros."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}o líquido preso transmite o aumento de pressão inteiro; [p=0.2] {b}efe um sobre á um é igual a efe dois sobre á dois; [p=0.2] e {c}o que se ganha em força se paga em distância."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai conhecer {a}a força que a água faz para cima em tudo o que entra nela: [p=0.2] {b}o empuxo, de Arquimedes. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
