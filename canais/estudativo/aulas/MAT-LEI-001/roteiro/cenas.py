# Estudativo · MAT-LEI-001 — Achar a pergunta e os dados úteis (Matemática · Leitura de Problemas).
# Habilidade: ler a pergunta antes do texto, marcar só os números que entram na conta e corrigir 7,3 ônibus para 8.
# Pré-requisitos: MAT-NUM-011 (qual conta o problema pede), MAT-FRA-017 (dividir com resultado decimal). Próxima: MAT-LEI-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.

TITULO = "Achar a pergunta e os dados úteis"

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
    dict(id="s01", block="gancho", text="Uma escola vai levar {a}duzentas e noventa e duas pessoas para um passeio. [p=0.2] Cada ônibus leva {b}quarenta. [p=0.3] A conta dá {c}sete vírgula três. [p=0.3] Só que ninguém contrata {d}três décimos de ônibus."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar a pergunta, separar os números que importam e dar uma resposta que faz sentido, [p=0.2] com um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de duas coisas: [p=0.2] {a}escolher a conta pela história, [p=0.2] e {b}continuar a divisão depois da vírgula. [p=0.3] Se faltar alguma, procure no canal."),
    # passo 1: a pergunta primeiro
    dict(id="s04", block="pergunta", text="Problema de prova costuma ser longo. [p=0.2] E quem lê do começo ao fim, guardando tudo, chega na pergunta {a}cansado e confuso. [p=0.3] Por isso, inverta a ordem: {b}leia a pergunta primeiro."),
    dict(id="s05", block="pergunta", text="Veja o problema inteiro. [p=0.2] {a}Uma escola tem oito turmas. [p=0.2] {b}Para o passeio, se inscreveram duzentas e noventa e duas pessoas. [p=0.2] {c}O passeio dura seis horas, [p=0.2] {d}a entrada custa quinze reais, [p=0.2] e {e}cada ônibus leva quarenta passageiros."),
    dict(id="s06", block="pergunta", text="A pergunta fica quase sempre {a}no fim: [p=0.2] {b}quantos ônibus a escola precisa contratar? [p=0.3] Agora você sabe o que procura: {c}um número de ônibus. [p=0.2] Com isso na cabeça, o resto do texto fica mais fácil."),
    # passo 2: marcar os dados úteis
    dict(id="s07", block="dados", text="Segundo passo: {a}marque só os números que a pergunta usa. [p=0.3] Para saber de ônibus, importa {b}quantas pessoas vão [p=0.2] e {c}quantas cabem em cada ônibus."),
    dict(id="s08", block="dados", text="E o resto? [p=0.2] {a}Oito turmas, {b}seis horas, {c}quinze reais. [p=0.3] Nenhum muda a quantidade de ônibus. [p=0.2] {d}Risque. [p=0.3] Prova coloca número a mais de propósito, para ver quem usa tudo sem pensar."),
    # passo 3: conta e sentido
    dict(id="s09", block="conta", text="Terceiro passo: a conta. [p=0.2] Repartir as pessoas em grupos de quarenta é {a}divisão. [p=0.3] Quantos quarentas cabem em duzentos e noventa e dois? [p=0.2] {b}Sete vezes quarenta: sete vezes quatro dá vinte e oito, mais um zero: duzentos e oitenta. [p=0.2] Sobram doze. [p=0.3] Continuando depois da vírgula, o doze vira cento e vinte, [p=0.2] que tem {c}três quarentas. [p=0.2] Resultado: sete vírgula três."),
    dict(id="s10", block="conta", text="Mas a pergunta pede {a}ônibus, e ônibus vem inteiro. [p=0.3] {b}Sete ônibus levam só {c}duzentas e oitenta pessoas. [p=0.3] Ficam {d}doze pessoas na calçada."),
    dict(id="s11", block="conta", text="Essas doze precisam de mais um ônibus, mesmo que ele saia quase vazio. [p=0.3] Resposta: {a}oito ônibus. [p=0.3] Confira: {b}oito vezes quarenta dá trezentos e vinte lugares. [p=0.2] Cabe todo mundo."),
    # erro comum
    dict(id="s12", block="erro", text="O erro comum é usar a regra de arredondar decimais: [p=0.2] {a}depois do sete vem um três, menos que cinco, então fica sete. [p=0.3] Só que, com sete ônibus, {b}doze pessoas ficam para trás. [p=0.3] A regra do cinco serve para achar o valor mais próximo, como num preço ou numa medida. [p=0.2] Quando a resposta conta coisas que só existem inteiras, quem decide é {c}a pergunta."),
    dict(id="s13", block="erro", text="E às vezes a pergunta manda descer. [p=0.2] {a}Com cinquenta reais, quantos pacotes de três reais você compra? [p=0.3] {b}Cinquenta dividido por três dá dezesseis vírgula seis seis seis, sem fim, [p=0.2] e a regra do cinco mandaria subir. [p=0.3] Só que dezessete pacotes custam cinquenta e um reais: {c}você não consegue pagar. [p=0.3] Resposta: {d}dezesseis pacotes. [p=0.3] {e}Precisa caber todo mundo? Sobe. [p=0.2] {f}O dinheiro não chega? Desce."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: [p=0.2] {a}quando a resposta tem que ser inteira, troque a divisão pela tabuada. [p=0.3] Procure o múltiplo de quarenta logo abaixo e logo acima de duzentos e noventa e dois: [p=0.2] {b}duzentos e oitenta, com sete, [p=0.2] e {c}trezentos e vinte, com oito."),
    dict(id="s15", block="atalho", text="Funciona porque dividir é perguntar {a}quantos grupos cabem. [p=0.3] Os vizinhos já mostram as duas respostas possíveis, [p=0.2] e a pergunta escolhe entre elas. [p=0.3] Não compensa quando o divisor {b}é difícil de multiplicar de cabeça: [p=0.2] aí, faça a divisão."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Para pintar três cômodos, uma pessoa precisa de quarenta e cinco litros de tinta. [p=0.2] {b}A tinta vem em latas de quatro litros, [p=0.1] {c}que custam cento e vinte reais cada. [p=0.2] {d}A pintura vai levar dois dias. [p=0.3] {e}Quantas latas ela precisa comprar?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] A pergunta pede {a}latas. [p=0.2] Os números úteis são {b}quarenta e cinco litros e quatro litros por lata. [p=0.2] {c}Três cômodos, cento e vinte reais e dois dias: risque."),
    dict(id="s19", block="resposta", text="{a}Quarenta e cinco dividido por quatro dá onze vírgula vinte e cinco, [p=0.2] e a regra do cinco mandaria descer. [p=0.3] Pela tabuada: {b}onze latas dão quarenta e quatro litros, e falta um litro. [p=0.2] {c}Doze latas dão quarenta e oito. [p=0.3] A tinta precisa dar para tudo, então sobe: {d}doze latas."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}pergunta primeiro, [p=0.2] {b}risque o que não serve, [p=0.2] e {c}confira se a resposta faz sentido no mundo real."),
    dict(id="s21", block="fim", text="Na próxima aula, você conhece as palavras que mudam a conta, [p=0.2] como {a}a mais que, {b}do restante e {c}no mínimo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
