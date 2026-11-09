# Estudativo · FIS-EGF-011 — Princípio de Bernoulli (Física · Equilíbrio, Gravitação e Fluidos · Hidrodinâmica).
# Habilidade: relacionar velocidade e pressão em asas de avião e tubos e usar v = √(2·g·h) na saída de um tanque.
# Pré-requisitos: FIS-EGF-010 (continuidade), FIS-EGF-005 (Stevin), FIS-ENE-005 (conservação da energia, v = √(2gh)).
# Próxima: FIS-EGF-012. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita. Aula de extensão (Fuvest).
# Fluido ideal: sem atrito, incompressível, escoamento constante. Teorema de Torricelli (mesmo Evangelista Torricelli da
# equação de frenagem, FIS-CIN-009). Contas: 1.000·(3² − 1²)/2 = 4.000 Pa; √(2·10·5) = 10 m/s; √(20·0,8) = 4; √(20·1,8) = 6.

TITULO = "Princípio de Bernoulli"

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
    dict(id="s01", block="gancho", text="{a}Num vendaval, telhados são arrancados para cima. [p=0.3] {b}O vento sopra de lado, por cima do telhado. [p=0.2] {c}Então, quem empurra o telhado para cima? [p=0.3] {d}O ar parado de dentro da casa."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai relacionar a velocidade de um fluido com a pressão, [p=0.2] {b}explicar a asa do avião [p=0.2] e {c}calcular a velocidade da água que sai por um furo num tanque."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas. [p=0.2] {b}A continuidade: onde o cano afina, a água acelera. [p=0.2] {c}A lei de Stevin: a pressão aumenta com a profundidade. [p=0.2] E {d}a conservação da energia: sem atrito, cinética mais potencial fica constante. [p=0.3] Se faltar alguma, procure no canal."),
    # velocidade e pressão
    dict(id="s04", block="ideia", text="{a}Quando a água passa de um cano largo para um fino, ela acelera. [p=0.2] {b}Para acelerar, alguma coisa tem que empurrá-la para a frente. [p=0.3] {c}Quem empurra é a pressão: [p=0.1] {d}maior no trecho largo, menor no fino. [p=0.3] {e}Onde o fluido é mais rápido, a pressão é menor."),
    dict(id="s05", block="ideia", text="{a}Daniel Bernoulli escreveu isso como conservação da energia. [p=0.2] {b}Num fluido sem atrito, [p=0.1] a soma de três termos não muda ao longo do tubo: [p=0.3] {c}pê, mais densidade vezes vê ao quadrado sobre dois, mais densidade vezes gê vezes agá."),
    dict(id="s06", block="ideia", text="{a}Pê é a pressão, em pascal. [p=0.2] {b}Densidade vezes vê ao quadrado sobre dois é a energia cinética de cada metro cúbico: [p=0.1] eme vê ao quadrado sobre dois, com a densidade no lugar da massa. [p=0.3] {c}Densidade vezes gê vezes agá é a energia potencial de cada metro cúbico. [p=0.2] {d}Vê é a velocidade, e agá, a altura."),
    dict(id="s07", block="ideia", text="{a}Num cano deitado, a altura não muda, [p=0.1] e o último termo é igual dos dois lados. [p=0.2] {b}A água passa de um para três metros por segundo. [p=0.3] {c}A pressão cai o quanto sobe o termo do meio. [p=0.2] Três ao quadrado, nove; um ao quadrado, um. [p=0.2] {d}Mil, vezes nove menos um, sobre dois. [p=0.2] {e}Quatro mil pascals a menos no trecho rápido."),
    # aplicações
    dict(id="s08", block="asa", text="{a}A asa do avião tem formato curvo e vai um pouco inclinada. [p=0.2] {b}O ar passa mais rápido por cima do que por baixo. [p=0.3] {c}Ar rápido, pressão menor em cima. [p=0.2] {d}A pressão maior embaixo empurra a asa para cima: [p=0.1] {e}é a força de sustentação."),
    dict(id="s09", block="asa", text="{a}O telhado é a mesma coisa. [p=0.2] {b}Vento forte por cima: pressão menor do lado de fora. [p=0.2] {c}Dentro, o ar está parado, com a pressão de sempre. [p=0.3] {d}A diferença empurra o telhado para cima."),
    # tanque
    dict(id="s10", block="tanque", text="{a}Um tanque aberto tem um furo embaixo. [p=0.2] {b}O furo está agá metros abaixo da superfície da água. [p=0.3] {c}Em cima e no furo, a pressão é a do ar, a mesma: ela corta. [p=0.2] {d}Em cima, a água está quase parada, porque o furo é pequeno. [p=0.2] {e}Sobra a energia potencial virando cinética."),
    dict(id="s11", block="tanque", text="{a}O resultado é vê igual à raiz de dois gê agá: [p=0.1] o teorema de Torricelli, [p=0.1] do mesmo Torricelli da equação de frenagem. [p=0.3] {b}É a velocidade de uma pedra que cai do repouso dessa altura agá. [p=0.3] {c}Furo cinco metros abaixo da superfície: [p=0.1] {d}raiz de dois vezes dez vezes cinco, raiz de cem, [p=0.1] {e}dez metros por segundo."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o ar rápido empurra mais. [p=0.3] {b}Sopre entre duas folhas de papel penduradas lado a lado. [p=0.2] {c}Muita gente espera que elas se afastem. [p=0.2] {d}Elas se juntam: [p=0.1] {e}o ar rápido do meio tem pressão menor, [p=0.1] e o ar parado de fora empurra as folhas para dentro."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.2] {a}em questão de tanque furado, não monte a equação de Bernoulli. [p=0.2] {b}Use direto vê igual à raiz de dois gê agá, [p=0.1] {c}com agá medido da superfície até o furo, não do chão. [p=0.3] {d}Com gê igual a dez, vê ao quadrado é vinte vezes agá: [p=0.1] {e}zero vírgula oito metro dá raiz de dezesseis, quatro metros por segundo."),
    dict(id="s14", block="atalho", text="{a}Só não vale com o tanque fechado e o ar de dentro apertado: [p=0.2] {b}aí, a pressão em cima é diferente da pressão no furo, e não corta."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma caixa d'água aberta tem um furo [p=0.1] {b}um vírgula oito metro abaixo do nível da água. [p=0.3] {c}Com que velocidade a água sai? [p=0.2] {d}E, num cano deitado que afina, a pressão no trecho fino é maior ou menor que no largo?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Vê ao quadrado é vinte vezes um vírgula oito: [p=0.1] {b}trinta e seis. [p=0.2] {c}Vê é a raiz de trinta e seis: [p=0.1] {d}seis metros por segundo. [p=0.3] {e}No cano, o trecho fino tem a água mais rápida, [p=0.1] {f}então a pressão ali é menor."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}onde o fluido é mais rápido, a pressão é menor; [p=0.2] {b}a soma de pressão, energia cinética e energia potencial por volume não muda ao longo do tubo; [p=0.2] e {c}no furo do tanque, vê é a raiz de dois gê agá."),
    dict(id="s19", block="fim", text="Na próxima aula, {a}você pratica vazão e Bernoulli [p=0.2] {b}em questões inéditas, para fechar a trilha. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
