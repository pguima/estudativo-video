# Estudativo · MAT-CNT-004 — Fatorial (Matemática · Contagem e Probabilidade · Permutações, arranjos e combinações).
# Habilidade: calcular 5! = 120 e simplificar 8!/6! = 56 sem fazer a conta inteira.
# Pré-requisitos: MAT-CNT-001 (princípio multiplicativo, casinhas), MAT-FRA-003 (simplificar fração). Próxima: MAT-CNT-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; "!" narrado como "fatorial".
# Questão inédita, criada para esta aula. O nome "permutação" fica para MAT-CNT-005; zero fatorial = 1 sai da escada (1! = 1 × 0!), na s09.
# Prateleira: 5 × 4 = 20; × 3 = 60; × 2 = 120; × 1 = 120. 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 6 × 120 = 720.
# 8!/6! = 8 × 7 × 6!/6! = 56 (40.320 / 720 = 56). Erro: 8 − 6 = 2 → 2! = 2.
# Atalho: diferença = quantos números sobram · 10!/7! = 10 × 9 × 8 = 720 · 10!/2! sobram 8 números (10 a 3).
# Questão: 4! + 3! = 24 + 6 = 30 (erro 7! = 5.040) · 12!/10! = 12 × 11 = 132 (12! = 479.001.600, passa de quatrocentos milhões).

TITULO = "Fatorial"

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
    dict(id="s01", block="gancho", text="{a}Oito fatorial dividido por seis fatorial. [p=0.3] Parece conta de calculadora. [p=0.3] Mas dá para resolver {b}de cabeça, em uma linha, [p=0.2] e o resultado é {c}cinquenta e seis."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula fatoriais, [p=0.2] {b}corta contas enormes antes de fazer [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}o princípio multiplicativo, com as casinhas, [p=0.2] e {c}simplificar fração: dividir em cima e embaixo pelo mesmo número. [p=0.3] Se faltar alguma, procure no canal."),
    # prateleira
    dict(id="s04", block="prateleira", text="Você tem {a}cinco livros diferentes para pôr em uma prateleira. [p=0.2] De quantas formas pode arrumar? [p=0.3] Faça {b}cinco casinhas, uma para cada lugar."),
    dict(id="s05", block="prateleira", text="No primeiro lugar, cabe {a}qualquer um dos cinco. [p=0.2] No segundo, {b}sobram quatro, [p=0.2] porque o livro que já foi para a prateleira não volta. [p=0.2] Depois, {c}três, [p=0.2] {d}dois [p=0.2] e {e}um."),
    dict(id="s06", block="prateleira", text="{a}Cinco vezes quatro dá vinte. [p=0.2] {b}Vezes três dá sessenta. [p=0.2] {c}Vezes dois dá cento e vinte. [p=0.2] {d}Vezes um dá cento e vinte formas."),
    # definição
    dict(id="s07", block="definicao", text="Essa multiplicação aparece tanto que tem nome: {a}fatorial. [p=0.3] Na escrita, é {b}o número seguido de um ponto de exclamação. [p=0.2] Aqui, ele não é espanto: é conta. [p=0.3] A regra: [p=0.2] {c}multiplique o número por todos os de baixo, [p=0.2] descendo de um em um {d}até chegar no um."),
    dict(id="s08", block="definicao", text="Os primeiros fatoriais crescem rápido. [p=0.2] {a}Um fatorial dá um. [p=0.2] {b}Dois fatorial dá dois. [p=0.2] {c}Três fatorial dá seis. [p=0.2] {d}Quatro fatorial dá vinte e quatro. [p=0.2] {e}Cinco fatorial dá cento e vinte. [p=0.2] {f}Seis fatorial dá setecentos e vinte."),
    dict(id="s09", block="definicao", text="Repare: {a}cada fatorial é o anterior vezes o número novo. [p=0.3] {b}Seis fatorial é seis vezes cinco fatorial: [p=0.2] seis vezes cento e vinte dá setecentos e vinte. [p=0.2] Sete fatorial é sete vezes seis fatorial: [p=0.2] dá cinco mil e quarenta. [p=0.3] Essa ideia é {c}a chave para cortar contas. [p=0.3] E a escada também desce: [p=0.2] {d}um fatorial é um vezes zero fatorial. [p=0.2] Para essa conta dar um, {e}zero fatorial tem que valer um. [p=0.2] Guarde isso: ele aparece nas próximas aulas."),
    # simplificar
    dict(id="s10", block="cortar", text="Voltando ao começo: {a}oito fatorial dividido por seis fatorial. [p=0.3] Abra o de cima {b}só até chegar no seis fatorial: [p=0.2] {c}oito vezes sete vezes seis fatorial."),
    dict(id="s11", block="cortar", text="Embaixo também tem seis fatorial. [p=0.2] É como simplificar fração: [p=0.2] {a}divida em cima e embaixo por seis fatorial. [p=0.2] {b}Ele some de cima e de baixo. [p=0.3] Sobra {c}oito vezes sete, que dá cinquenta e seis. [p=0.3] Pelo caminho longo, oito fatorial dá quarenta mil trezentos e vinte, [p=0.2] e ainda teria a divisão por setecentos e vinte."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}fazer a conta só com os números que aparecem. [p=0.2] A pessoa faz {b}oito menos seis dá dois, [p=0.2] e responde {c}dois fatorial, que dá dois. [p=0.3] Bem longe de cinquenta e seis. [p=0.3] O seis fatorial some inteiro, mas o oito e o sete ficam: [p=0.2] {d}abra o maior e corte só o que for igual."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}a diferença diz quantos números sobram. [p=0.3] De seis para oito, a diferença é dois: [p=0.2] sobram {b}dois números, descendo do oito: [p=0.2] oito e sete. [p=0.3] {c}Dez fatorial dividido por sete fatorial? [p=0.2] Diferença três: [p=0.2] {d}dez vezes nove vezes oito dá setecentos e vinte. [p=0.3] {e}Treze fatorial dividido por onze fatorial? [p=0.2] Diferença dois: [p=0.2] {f}treze vezes doze dá cento e cinquenta e seis."),
    dict(id="s14", block="atalho", text="Funciona porque {a}tudo do menor fatorial para baixo se corta. [p=0.3] Não compensa quando {b}os números estão longe, [p=0.2] como dez fatorial dividido por dois fatorial: [p=0.2] sobram oito números para multiplicar. [p=0.3] E {c}na soma, nada se corta: [p=0.2] oito fatorial mais seis fatorial não vira conta curta: [p=0.2] calcule cada fatorial separado."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Quanto é quatro fatorial mais três fatorial? [p=0.3] E {b}quanto é doze fatorial dividido por dez fatorial?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Na soma, nada se corta: [p=0.2] calcule cada fatorial separado. [p=0.2] {a}Quatro fatorial dá vinte e quatro. [p=0.2] {b}Três fatorial dá seis. [p=0.2] {c}Vinte e quatro mais seis dá trinta. [p=0.3] Quem juntou tudo em sete fatorial chegou em cinco mil e quarenta, bem longe."),
    dict(id="s18", block="resposta", text="Na divisão, a diferença é dois: [p=0.2] sobram {a}o doze e o onze. [p=0.2] {b}Doze vezes onze dá cento e trinta e dois. [p=0.3] Sem o corte, você teria que calcular {c}doze fatorial, que passa de quatrocentos milhões."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}fatorial multiplica o número por todos os de baixo, até o um. [p=0.3] Na divisão, {b}abra o maior até encontrar o menor, e corte."),
    dict(id="s20", block="fim", text="Na próxima aula, o fatorial vira ferramenta: [p=0.2] você conta {a}filas e anagramas, como as trocas de letras da palavra amor, [p=0.2] e {b}filas com duas pessoas sempre juntas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
