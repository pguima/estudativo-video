# Estudativo · FIS-EGF-010 — Vazão e equação da continuidade (Física · Equilíbrio, Gravitação e Fluidos · Hidrodinâmica).
# Habilidade: usar Q = A·v e A1·v1 = A2·v2 para explicar por que a água acelera no cano mais fino.
# Pré-requisitos: FIS-EGF-004 (pressão), FIS-CIN-005 (s = v·t), MAT-RAZ-018 (vazão), MAT-ARE-008 (área do círculo). Próxima: FIS-EGF-011.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula. Aula de extensão (Fuvest).
# Líquido tratado como incompressível, em regime constante. Contas: 20 cm² · 50 cm/s = 1.000 cm³/s = 1 L/s; 20·0,5 = 5·v2 → 2 m/s;
# diâmetro 2 → 1: área ÷ 4, v = 2·4 = 8 m/s; vazão com π = 3: 3 cm² · 200 cm/s = 600 cm³/s = 0,6 L/s; 12 L ÷ 0,6 = 20 s.

TITULO = "Vazão e equação da continuidade"

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
    dict(id="s01", block="gancho", text="{a}Tampe com o dedo parte da ponta da mangueira, [p=0.2] e {b}a água sai bem mais rápida e vai mais longe. [p=0.3] {c}A torneira não abriu mais: [p=0.1] passa praticamente a mesma água por segundo. [p=0.2] {d}O que mudou foi o tamanho da saída."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a vazão de um cano [p=0.2] e {b}achar a velocidade da água quando o cano afina."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas. [p=0.2] {b}A vazão: o volume dividido pelo tempo, como litros por segundo. [p=0.2] {c}A velocidade constante: a distância é vê vezes tê. [p=0.2] E {d}a área do círculo: pi vezes érre ao quadrado. [p=0.3] Se faltar alguma, procure no canal."),
    # vazão
    dict(id="s04", block="vazao", text="{a}Vazão é o volume que passa por um ponto do cano a cada segundo. [p=0.2] {b}Quê igual ao volume sobre o tempo. [p=0.3] {c}No Sistema Internacional, metro cúbico por segundo. [p=0.1] {d}No dia a dia, litro por segundo. [p=0.2] {e}Um metro cúbico tem mil litros."),
    dict(id="s05", block="vazao", text="{a}Olhe a água andando dentro do cano, com velocidade vê. [p=0.2] {b}Num tempo tê, ela anda vê vezes tê. [p=0.3] {c}O volume que passou é um cilindro de água: [p=0.1] {d}a área do cano vezes esse comprimento. [p=0.3] {e}Divida pelo tempo, e o tê some: [p=0.1] {f}quê igual a á vezes vê."),
    dict(id="s06", block="vazao", text="{a}Á é a área da seção do cano, o círculo que aparece quando você corta o cano, em metros quadrados. [p=0.2] {b}Vê é a velocidade da água, em metros por segundo. [p=0.2] {c}A vazão sai em metros cúbicos por segundo."),
    dict(id="s07", block="vazao", text="{a}Um cano tem área de vinte centímetros quadrados, [p=0.1] {b}e a água anda nele a cinquenta centímetros por segundo, [p=0.1] meio metro por segundo. [p=0.3] {c}Com tudo em centímetro: [p=0.1] {d}vinte vezes cinquenta, [p=0.1] {e}mil centímetros cúbicos por segundo. [p=0.2] Mil centímetros cúbicos são um litro: [p=0.1] {f}a vazão é de um litro por segundo."),
    # continuidade
    dict(id="s08", block="continuidade", text="{a}O cano afina. [p=0.2] {b}A água não se comprime, não some e não se acumula no caminho. [p=0.3] {c}Todo litro que entra num trecho sai do outro, no mesmo tempo. [p=0.2] {d}A vazão é a mesma em todo o cano."),
    dict(id="s09", block="continuidade", text="{a}Então, á um vezes vê um é igual a á dois vezes vê dois. [p=0.3] {b}Essa é a equação da continuidade. [p=0.2] {c}Área menor, velocidade maior, [p=0.1] na mesma proporção: [p=0.1] {d}área e velocidade são inversamente proporcionais."),
    dict(id="s10", block="continuidade", text="{a}Aquele cano de vinte centímetros quadrados afina para cinco. [p=0.2] {b}Vinte vezes meio, igual a cinco vezes vê dois. [p=0.2] {c}Dez igual a cinco vê dois: [p=0.1] {d}vê dois igual a dois metros por segundo. [p=0.3] {e}Área quatro vezes menor, velocidade quatro vezes maior. [p=0.2] {f}É o seu dedo na mangueira."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}a questão dá o diâmetro, e a pessoa usa o diâmetro como se fosse a área. [p=0.3] {b}Um cano de quatro centímetros de diâmetro afina para dois: [p=0.1] {c}a pessoa diz que a velocidade dobra. [p=0.3] {d}Mas a área depende do raio ao quadrado. [p=0.2] {e}Diâmetro pela metade, área quatro vezes menor, [p=0.1] {f}velocidade quatro vezes maior."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.2] {a}com diâmetros, nem calcule a área. [p=0.2] {b}Divida o diâmetro largo pelo fino e eleve ao quadrado: [p=0.1] {c}é quantas vezes a velocidade aumenta no trecho fino. [p=0.3] {d}Diâmetro três vezes menor: velocidade nove vezes maior. [p=0.3] Funciona porque {e}o pi aparece dos dois lados e corta, [p=0.1] e o raio é sempre metade do diâmetro."),
    dict(id="s13", block="atalho", text="{a}O atalho não dá a vazão: [p=0.2] {b}para ela, a área precisa ser calculada."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Uma mangueira de dois centímetros de diâmetro [p=0.1] {b}termina num bico de um centímetro. [p=0.2] {c}A água anda na mangueira a dois metros por segundo. [p=0.3] {d}Com que velocidade ela sai do bico? [p=0.2] {e}E em quanto tempo ela enche um balde de doze litros? [p=0.2] Use pi igual a três."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}O diâmetro cai pela metade. [p=0.2] {b}A área fica quatro vezes menor. [p=0.2] {c}A velocidade fica quatro vezes maior: [p=0.1] {d}oito metros por segundo. [p=0.3] {e}A vazão: raio de um centímetro, área de três vezes um ao quadrado, três centímetros quadrados. [p=0.2] {f}Dois metros por segundo são duzentos centímetros por segundo: [p=0.1] três vezes duzentos, [p=0.1] seiscentos centímetros cúbicos por segundo, [p=0.1] zero vírgula seis litro por segundo. [p=0.3] {g}Doze litros divididos por zero vírgula seis: [p=0.1] {h}vinte segundos."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}vazão é volume sobre tempo, e também área vezes velocidade; [p=0.2] {b}num cano, a vazão é a mesma em todo trecho; [p=0.2] e {c}onde o cano afina, a água acelera."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai ver {a}o que acontece com a pressão quando a água acelera, [p=0.2] e {b}por que isso ajuda um avião a voar: o princípio de Bernoulli. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
