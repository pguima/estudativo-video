# Estudativo · QUI-CAL-010 — Pressão, volume e temperatura: a escala Kelvin (Química · Cálculos Químicos · Estudo dos gases).
# Habilidade: explicar a pressão pelo choque das partículas, converter 27 °C em 300 K e 760 mmHg em 1 atm.
# Pré-requisitos: QUI-MIS-003, MAT-MED-005, MAT-NUM-016, FIS-EGF-004. Próxima: QUI-CAL-011 (transformações gasosas).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Primeira aula do módulo Estudo dos gases: guarda a linguagem visual da trilha (veja o visual.py).
# ATENÇÃO: mol, massa molar e regra de três NÃO estão em "Já ensinado" desta aula (só a Física da pressão e a QUI-MIS-003).
# Fatos: zero absoluto −273,15 °C (a prova usa 273); Torricelli: 76 cm = 760 mmHg ao nível do mar; 1 atm ≈ 10⁵ Pa (FIS-EGF-004);
# a ~5.500 m a pressão é ~380 mmHg (0,5 atm) e a temperatura do ar fica perto de −20 °C. 20 °C = 293 K; 40 °C = 313 K.

TITULO = "Pressão, volume e temperatura: a escala Kelvin"

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
    dict(id="s01", block="gancho", text="{a}Encha um balão e ponha no congelador. [p=0.3] {b}Uma hora depois, ele está menor, meio murcho. [p=0.2] {c}Nenhum ar saiu. [p=0.3] {d}O que mudou foi a temperatura, [p=0.1] e, com ela, o volume."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}explicar a pressão de um gás pelas partículas, [p=0.2] {c}converter graus Celsius em kelvin [p=0.2] e {d}milímetros de mercúrio em atmosfera."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}no gás, as partículas voam soltas, e mais rápido quando ele esquenta; [p=0.2] {c}pressão é força dividida por área; [p=0.2] e {d}um litro é um decímetro cúbico. [p=0.3] Se faltar alguma, procure no canal."),
    # pressão
    dict(id="s04", block="pressao", text="{a}Dentro do balão, bilhões de trilhões de partículas voam em linha reta, [p=0.1] {b}batem na parede e voltam. [p=0.3] {c}Cada batida é um empurrão minúsculo. [p=0.2] {d}Somados, os empurrões viram uma força na parede inteira."),
    dict(id="s05", block="pressao", text="{a}Essa força dividida pela área é a pressão do gás. [p=0.3] {b}Mais batidas, ou batidas mais fortes: [p=0.1] {c}mais pressão. [p=0.3] {d}Por isso, encher o pneu aumenta a pressão: [p=0.1] {e}mais partículas batendo no mesmo espaço."),
    # volume
    dict(id="s06", block="volume", text="{a}O volume do gás é o espaço que ele ocupa. [p=0.2] {b}O gás não tem volume próprio: [p=0.1] {c}ele ocupa o recipiente inteiro, seja qual for. [p=0.3] {d}Nas contas, o volume vem em litros: [p=0.1] {e}um metro cúbico tem mil litros."),
    # temperatura
    dict(id="s07", block="temperatura", text="{a}A temperatura mede a agitação das partículas. [p=0.2] {b}Gás quente: partículas rápidas. [p=0.1] {c}Gás frio: partículas lentas. [p=0.3] {d}No congelador, as partículas do balão ficam lentas [p=0.1] e batem com menos força, [p=0.1] {e}e o ar de fora aperta o balão até ele encolher."),
    dict(id="s08", block="temperatura", text="{a}Esfrie cada vez mais, e a agitação cai. [p=0.2] {b}A duzentos e setenta e três graus Celsius negativos, ela chegaria ao mínimo. [p=0.2] {c}Não dá para ficar mais frio que isso: [p=0.1] {d}é o zero absoluto."),
    # kelvin
    dict(id="s09", block="kelvin", text="{a}A escala Kelvin começa ali. [p=0.2] {b}Zero kelvin é o zero absoluto. [p=0.3] {c}O tamanho do grau é o mesmo do Celsius: [p=0.1] {d}por isso, para converter, basta somar duzentos e setenta e três."),
    dict(id="s10", block="kelvin", text="{a}Vinte e sete graus Celsius: vinte e sete mais duzentos e setenta e três dá trezentos kelvin. [p=0.3] {b}Zero grau Celsius vira duzentos e setenta e três kelvin. [p=0.3] {c}Nas contas de gás, a temperatura vai sempre em kelvin."),
    # unidades de pressão
    dict(id="s11", block="unidades", text="{a}A pressão aparece em três unidades. [p=0.2] {b}A atmosfera, que é a pressão do ar ao nível do mar. [p=0.2] {c}O pascal, que é newton por metro quadrado: [p=0.1] {d}uma atmosfera tem cerca de cem mil pascals. [p=0.3] {e}E o milímetro de mercúrio."),
    dict(id="s12", block="unidades", text="{a}Torricelli encheu um tubo de vidro com mercúrio e virou de boca para baixo numa bacia. [p=0.2] O mercúrio desceu e parou a setenta e seis centímetros: [p=0.1] {b}setecentos e sessenta milímetros. [p=0.2] Quem segura a coluna é o ar, empurrando a bacia. [p=0.3] {c}Por isso, uma atmosfera é igual a setecentos e sessenta milímetros de mercúrio. [p=0.3] {d}Para passar para atmosfera, divida por setecentos e sessenta."),
    # erro
    dict(id="s13", block="erro", text="A agitação acompanha a temperatura em kelvin: [p=0.1] dobrar o kelvin dobra a agitação. [p=0.2] O erro mais comum é {a}achar que dobrar a temperatura em Celsius dobra a agitação. [p=0.3] {b}De vinte para quarenta graus Celsius parece o dobro. [p=0.2] {c}Em kelvin, vai de duzentos e noventa e três para trezentos e treze: [p=0.1] {d}bem menos que o dobro. [p=0.3] {e}Para comparar temperaturas de gás, só vale o kelvin."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho: [p=0.1] {a}uma variação de temperatura é a mesma em Celsius e em kelvin. [p=0.3] {b}Esquentou vinte graus Celsius? [p=0.1] {c}Esquentou vinte kelvin. [p=0.3] {d}Funciona porque o grau tem o mesmo tamanho nas duas escalas, [p=0.1] {e}e o duzentos e setenta e três some na subtração. [p=0.3] {f}Não compensa quando a conta pede a temperatura em si: [p=0.1] aí, você soma duzentos e setenta e três."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}No alto de uma montanha de uns cinco mil e quinhentos metros, [p=0.1] {b}a pressão do ar é de cerca de trezentos e oitenta milímetros de mercúrio, [p=0.2] {c}e a temperatura pode ser de vinte e três graus Celsius negativos. [p=0.3] {d}Quanto é essa pressão em atmosfera? [p=0.2] {e}E a temperatura em kelvin?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Trezentos e oitenta é a metade de setecentos e sessenta: [p=0.1] {b}meia atmosfera. [p=0.3] {c}Menos vinte e três mais duzentos e setenta e três [p=0.1] {d}dá duzentos e cinquenta kelvin."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}a pressão do gás vem das batidas das partículas; [p=0.2] {b}kelvin é Celsius mais duzentos e setenta e três; [p=0.2] {c}e uma atmosfera são setecentos e sessenta milímetros de mercúrio."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai mexer nessas três variáveis: [p=0.2] {a}apertar, aquecer ou travar o volume do gás, [p=0.1] e {b}prever o novo volume com uma equação só. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
