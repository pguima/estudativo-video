# Estudativo · FIS-CIN-001 — Grandezas físicas e Sistema Internacional (Física · Cinemática · Grandezas e vetores).
# Habilidade: dar a unidade do SI de cada grandeza, separar grandeza escalar de vetorial e conferir uma fórmula pelas unidades.
# Pré-requisitos: MAT-MED-003 (prefixos), MAT-POT-012 (notação científica), MAT-RAZ-025 (unidades como guia). Próxima: FIS-CIN-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Primeira aula de Física: guarda a linguagem visual da matéria (veja o visual.py). Questão inédita, criada para esta aula.
# Fato do gancho: a sonda Mars Climate Orbiter (NASA) se perdeu em Marte em 1999 porque uma equipe usou unidades inglesas e a
# outra esperava o sistema métrico. SI narrado "esse i". km/h → m/s feito com fatores (MAT-RAZ-025): o atalho do 3,6 é MAT-RAZ-016,
# que não está em "Já ensinado".

TITULO = "Grandezas físicas e Sistema Internacional"

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
    dict(id="s01", block="gancho", text="{a}Em mil novecentos e noventa e nove, uma sonda da NASA chegou a Marte [p=0.2] e {b}se perdeu. [p=0.3] O culpado foi uma {c}unidade. [p=0.2] Uma equipe fez as contas em {d}unidades inglesas, [p=0.2] e a outra esperava {e}o sistema métrico."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dar a unidade certa de cada grandeza, [p=0.2] separar as grandezas que precisam de {b}direção e sentido [p=0.2] e conferir uma fórmula {c}só pelas unidades."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}os prefixos, como o quilo, que vale mil; [p=0.2] e {c}cortar unidades como números numa fração, multiplicando por fatores que valem um. [p=0.3] Se faltar alguma, procure no canal."),
    # grandeza
    dict(id="s04", block="grandeza", text="Grandeza física é {a}tudo o que dá para medir: [p=0.2] comprimento, massa, tempo, velocidade. [p=0.3] E medir é {b}comparar com um padrão. [p=0.2] Medir uma mesa de dois metros é ver que {c}o metro cabe nela duas vezes."),
    dict(id="s05", block="grandeza", text="Por isso, toda medida tem duas partes: [p=0.2] {a}o número [p=0.1] e {b}a unidade. [p=0.3] {c}Só o número não diz nada. [p=0.2] Velocidade vinte? [p=0.2] {d}Vinte quilômetros por hora é uma bicicleta. [p=0.2] {e}Vinte metros por segundo é um carro na estrada."),
    # SI
    dict(id="s06", block="si", text="Para o mundo inteiro usar os mesmos padrões, existe o {a}Sistema Internacional de Unidades, o esse i. [p=0.3] Ele tem sete unidades de base, mas para estudar o movimento, três bastam: [p=0.2] comprimento em {b}metro, [p=0.2] massa em {c}quilograma [p=0.2] e tempo em {d}segundo."),
    dict(id="s07", block="si", text="As outras do movimento se montam com essas três. [p=0.2] {a}Área é metro vezes metro: metro quadrado. [p=0.3] {b}Velocidade é distância dividida por tempo: metro por segundo."),
    dict(id="s08", block="si", text="Repare em duas pegadinhas. [p=0.2] {a}A massa do esse i é o quilograma, não o grama: [p=0.2] das três, é a única que já vem com prefixo. [p=0.3] E {b}a hora e o quilômetro por hora são muito usados, [p=0.2] mas {c}não são do esse i."),
    # conversão
    dict(id="s09", block="converter", text="Por isso, numa questão, {a}passe tudo para metro, quilograma e segundo antes de calcular. [p=0.2] Vamos converter {b}setenta e dois quilômetros por hora em metros por segundo."),
    dict(id="s10", block="converter", text="Para sumir com o quilômetro, {a}vezes mil metros sobre um quilômetro. [p=0.2] Para sumir com a hora, {b}vezes uma hora sobre três mil e seiscentos segundos, [p=0.2] porque uma hora tem sessenta vezes sessenta, três mil e seiscentos segundos."),
    dict(id="s11", block="converter", text="{a}Quilômetro corta com quilômetro, [p=0.1] {b}hora corta com hora. [p=0.2] Sobram {c}setenta e dois mil metros divididos por três mil e seiscentos segundos. [p=0.2] Corte dois zeros de cada lado: [p=0.1] {d}setecentos e vinte dividido por trinta e seis. [p=0.2] {e}Vinte metros por segundo."),
    # escalar e vetorial
    dict(id="s12", block="vetorial", text="Agora, uma diferença importante. [p=0.2] {a}Uma pessoa tem massa de sessenta quilogramas. [p=0.2] O número e a unidade {b}dizem tudo. [p=0.3] Uma grandeza assim se chama {c}escalar. [p=0.2] {d}Tempo e temperatura também são escalares."),
    dict(id="s13", block="vetorial", text="Mas, se eu digo {a}ande três metros, [p=0.2] fica a pergunta: para onde? [p=0.3] Você pode terminar em {b}qualquer ponto desta roda. [p=0.3] Falta dizer {c}a direção [p=0.1] e {d}o sentido."),
    dict(id="s14", block="vetorial", text="{a}Direção é a linha do movimento: horizontal, vertical ou inclinada. [p=0.2] {b}Sentido é para que lado dessa linha: [p=0.2] para a direita ou para a esquerda, para cima ou para baixo. [p=0.3] Uma grandeza que precisa disso se chama {c}vetorial."),
    dict(id="s15", block="vetorial", text="Ela é desenhada como uma seta, {a}o vetor. [p=0.2] {b}O tamanho da seta mostra o valor, que se chama módulo. [p=0.2] {c}A linha da seta é a direção, [p=0.1] e {d}a ponta é o sentido. [p=0.3] {e}Deslocamento, que é a mudança de lugar, [p=0.1] velocidade e força são vetoriais. [p=0.3] O velocímetro do carro mostra {f}só o módulo, [p=0.2] mas a velocidade também tem direção e sentido."),
    # conferir a fórmula
    dict(id="s16", block="formula", text="Agora, mais um uso das unidades: [p=0.2] {a}conferir uma fórmula. [p=0.3] A distância percorrida é {b}a velocidade vezes o tempo: [p=0.2] {c}dê igual a vê vezes tê. [p=0.3] Troque cada letra pela unidade do esse i: [p=0.2] {d}metro por segundo vezes segundo."),
    dict(id="s17", block="formula", text="{a}O segundo de cima corta com o de baixo, [p=0.2] e sobra {b}metro. [p=0.2] Distância em metro: {c}a fórmula está coerente. [p=0.3] A regra é esta: [p=0.1] {d}os dois lados do igual precisam ter a mesma unidade. [p=0.3] {e}Unidade errada prova que a fórmula está errada. [p=0.2] {f}Unidade certa ainda não prova que ela está certa."),
    dict(id="s18", block="formula", text="Agora, se alguém lembrar errado: [p=0.2] {a}velocidade dividida pelo tempo. [p=0.3] Fica {b}metro por segundo, dividido por segundo: [p=0.2] o segundo aparece duas vezes embaixo, [p=0.1] {c}metro por segundo ao quadrado. [p=0.3] {d}Essa unidade existe: é a da aceleração, assunto de outra aula. [p=0.2] Mas {e}não é metro. [p=0.2] Para distância, a fórmula está errada."),
    # erro
    dict(id="s19", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}misturar unidades na mesma conta. [p=0.3] Um carro a setenta e dois quilômetros por hora anda durante {b}dez segundos. [p=0.2] A pessoa faz {c}setenta e dois vezes dez, [p=0.1] setecentos e vinte, [p=0.2] e responde {d}setecentos e vinte metros."),
    dict(id="s20", block="erro", text="Mas {a}a hora está embaixo e o segundo está em cima: [p=0.2] {b}nada corta. [p=0.3] Com a velocidade em metro por segundo, [p=0.2] {c}vinte metros por segundo vezes dez segundos, [p=0.2] o carro anda {d}duzentos metros. [p=0.2] Bem menos que setecentos e vinte."),
    # atalho
    dict(id="s21", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}decore só metro, quilograma e segundo, e tire as outras da fórmula. [p=0.3] Troque cada grandeza pela unidade dela e faça a conta só com as unidades. [p=0.3] {b}Vazão é volume dividido por tempo: [p=0.2] {c}metro cúbico por segundo. [p=0.3] {d}Algumas unidades montadas ganham nome próprio, como o newton da força, [p=0.2] mas isso fica para a aula de cada uma."),
    dict(id="s22", block="atalho", text="Funciona porque {a}a unidade passa pelas mesmas contas que o número. [p=0.3] E isso elimina alternativas: [p=0.2] {b}se a questão pede uma distância, a alternativa velocidade dividida pelo tempo cai sem conta nenhuma, [p=0.2] porque dá metro por segundo ao quadrado. [p=0.3] {c}Não compensa quando todas as alternativas têm a mesma unidade: [p=0.2] aí, faça a conta."),
    # questão
    dict(id="s23", block="questao", text="Hora de testar. [p=0.2] Um ciclista pedala a {a}dezoito quilômetros por hora. [p=0.3] {b}Quantos metros ele anda em um minuto? [p=0.3] E mais: {c}a velocidade dele é uma grandeza escalar ou vetorial?"),
    dict(id="s24", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s25", block="resposta", text="Vamos lá. [p=0.2] {a}Dezoito quilômetros por hora, [p=0.1] {b}vezes mil metros sobre um quilômetro, [p=0.1] {c}vezes uma hora sobre três mil e seiscentos segundos. [p=0.3] {d}Dezoito mil dividido por três mil e seiscentos. [p=0.2] Corte dois zeros: cento e oitenta dividido por trinta e seis, [p=0.2] {e}cinco metros por segundo."),
    dict(id="s26", block="resposta", text="{a}Um minuto são sessenta segundos. [p=0.2] {b}Cinco metros por segundo vezes sessenta segundos: [p=0.2] o segundo corta, e sobram {c}trezentos metros. [p=0.3] E a velocidade é {d}vetorial. [p=0.2] O dezoito é só o módulo: [p=0.2] para saber aonde ele chega, é preciso saber para onde ele pedala."),
    # fechamento
    dict(id="s27", block="fim", text="Resumindo: {a}toda medida é número com unidade, [p=0.2] {b}passe tudo para metro, quilograma e segundo antes da conta, [p=0.2] {c}grandeza vetorial precisa de direção e sentido, [p=0.2] e {d}os dois lados de uma fórmula têm a mesma unidade."),
    dict(id="s28", block="fim", text="Na próxima aula, você vai {a}somar e subtrair vetores, [p=0.2] como {b}no barco que atravessa um rio com a correnteza empurrando. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
