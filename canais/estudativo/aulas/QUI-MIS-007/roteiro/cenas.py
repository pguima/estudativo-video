# Estudativo · QUI-MIS-007 — Decantar, filtrar e centrifugar (Química · Matéria e Misturas · Separação de misturas).
# Habilidade: separar areia da água por decantação ou filtração, explicar a centrífuga e separar água e óleo no funil de
# decantação.
# Pré-requisitos: QUI-MIS-002, MAT-RAZ-017. Próxima: QUI-MIS-008 (destilação: simples e fracionada).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: água 1 g/cm³; óleo de cozinha cerca de 0,9 g/cm³; líquido de densidade 1,5 g/cm³ que não se mistura com a água
# (como o clorofórmio, sem citar o nome); na centrífuga do laboratório, o sangue separa o plasma (em cima) das células
# (embaixo). O filtro não segura o que está dissolvido. Estados físicos e destilação ainda não ensinados: citados como
# outra aula.

TITULO = "Decantar, filtrar e centrifugar"

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
    dict(id="s01", block="gancho", text="{a}Deixe um copo de água barrenta parado em cima da mesa. [p=0.3] {b}Em uma hora, o barro está no fundo e a água de cima clareou. [p=0.3] {c}Ninguém mexeu no copo. [p=0.2] {d}Quem fez a separação?"),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai separar sólido de líquido de três jeitos: [p=0.1] {b}decantar, filtrar e centrifugar. [p=0.3] {c}E ainda vai separar água e óleo, sem perder uma gota."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula de densidade: [p=0.1] {a}o mais denso afunda e o menos denso fica por cima. [p=0.3] {b}E da aula de misturas: [p=0.1] {c}na mistura heterogênea, dá para ver as fases."),
    # decantação
    dict(id="s04", block="decantar", text="A resposta do copo é {a}a gravidade. [p=0.2] {b}O barro é mais denso que a água, então desce devagar até o fundo. [p=0.3] {c}Esse jeito de separar, deixando em repouso, se chama decantação."),
    dict(id="s05", block="decantar", text="{a}Depois, você inclina o copo com cuidado e despeja a água de cima em outro copo, [p=0.1] {b}deixando o barro para trás. [p=0.3] {c}Só funciona em mistura heterogênea, com uma parte mais densa que a outra."),
    # filtração
    dict(id="s06", block="filtrar", text="Para ser mais rápido, {a}passe a mistura por um filtro. [p=0.2] {b}O filtro é cheio de furos minúsculos. [p=0.3] {c}A água passa pelos furos; [p=0.1] {d}os grãos de areia, maiores que os furos, ficam presos. [p=0.3] {e}Isso é a filtração."),
    dict(id="s07", block="filtrar", text="Você faz isso todo dia: {a}no coador de café. [p=0.2] {b}O pó fica no coador, [p=0.1] {c}e o café passa. [p=0.3] {d}Repare: a filtração separa por tamanho, não por densidade."),
    # centrífuga
    dict(id="s08", block="centrifugar", text="E quando as partículas são tão finas que demoram dias para descer? [p=0.2] {a}Gire a mistura bem rápido. [p=0.3] {b}A rotação empurra o mais denso para o fundo do tubo, com muito mais força que a gravidade. [p=0.3] {c}Isso é a centrifugação: [p=0.1] uma decantação acelerada."),
    dict(id="s09", block="centrifugar", text="{a}No laboratório, a centrífuga separa o sangue em minutos: [p=0.2] {b}as células, mais densas, vão para o fundo, [p=0.1] {c}e o plasma, a parte líquida, amarelada, fica em cima."),
    # funil
    dict(id="s10", block="funil", text="Agora, dois líquidos que não se misturam: {a}água e óleo. [p=0.3] {b}O óleo é menos denso, então fica por cima. [p=0.3] Para separar, use o {c}funil de decantação, também chamado de funil de separação: [p=0.1] {d}um vidro em forma de gota, com uma torneira embaixo."),
    dict(id="s11", block="funil", text="{a}Ponha a mistura e espere as duas camadas se formarem. [p=0.3] {b}Abra a torneira: sai primeiro o líquido de baixo, a água. [p=0.3] {c}Quando a divisa chegar na torneira, feche. [p=0.2] {d}O óleo fica no funil."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.1] {a}sólido no líquido? [p=0.1] {b}Tem tempo, decante. [p=0.1] {c}Quer rápido, filtre. [p=0.1] {d}Partícula fina demais, centrifugue. [p=0.3] {e}Dois líquidos que não se misturam? [p=0.1] {f}Funil, e sai primeiro o mais denso, que está embaixo."),
    dict(id="s13", block="atalho", text="Funciona porque {a}os quatro métodos usam a mesma coisa: [p=0.1] a mistura é heterogênea, com partes separadas, mesmo que às vezes só no microscópio, como no sangue. [p=0.3] {b}Por isso nenhum deles separa mistura homogênea. [p=0.2] {c}Para essas, é preciso destilar, que é assunto da próxima aula."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}achar que dá para tirar o sal da água do mar com um filtro. [p=0.3] {b}Não dá. [p=0.2] {c}O sal está dissolvido: espalhado em partículas muito menores que qualquer furo de filtro."),
    dict(id="s15", block="erro", text="{a}A água salgada passa inteira pelo filtro, [p=0.1] {b}tão salgada quanto entrou. [p=0.3] {c}O filtro só segura o que não está dissolvido."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}No funil, há água, de densidade um grama por centímetro cúbico, [p=0.1] {b}e um óleo, de densidade zero vírgula nove. [p=0.3] {c}Ao abrir a torneira, qual sai primeiro? [p=0.3] {d}E se, no lugar do óleo, fosse um líquido de densidade um vírgula cinco, que também não se mistura com a água?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="{a}A água tem densidade um, maior que zero vírgula nove. [p=0.1] Então a água é a mais densa e fica embaixo. [p=0.2] {b}Sai primeiro a água."),
    dict(id="s19", block="resposta", text="{a}No segundo caso, um vírgula cinco é maior que um. [p=0.2] {b}Agora o outro líquido fica embaixo, [p=0.1] {c}e é ele que sai primeiro. [p=0.3] {d}Quem decorou que sempre sai a água errou a segunda. [p=0.2] {e}Sai o mais denso, seja ele qual for."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}decantar é esperar o mais denso descer; [p=0.2] {b}filtrar é reter o grão maior que o furo; [p=0.2] {c}centrifugar é decantar com pressa; [p=0.2] e {d}no funil sai primeiro o mais denso."),
    dict(id="s21", block="fim", text="Na próxima aula, você separa o que o filtro não separa: [p=0.2] {a}a destilação, simples e fracionada, [p=0.1] e o caminho do petróleo até a gasolina. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
