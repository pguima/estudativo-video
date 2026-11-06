# Estudativo · MAT-NUM-005 — Tabuada com macetes: 2, 5, 9 e 10 (Matemática · Números e Contas).
# Habilidade: ler 4 × 3 como 3 + 3 + 3 + 3 e responder 7 × 5, 6 × 2 e 9 × 7 de cabeça, sem contar nos dedos.
# Pré-requisitos: MAT-NUM-004. Próxima: MAT-NUM-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Contas: 4 × 3 = 3 + 3 + 3 + 3 = 12 = 3 × 4 · 7 × 10 = 70 · 6 × 2 = 6 + 6 = 12 · 7 × 5 = 70 ÷ 2 = 35 · 9 × 7 = 70 − 7 = 63.
# 2, 5, 9 e 10 cobrem 30 das 45 contas da tabuada do 2 ao 10, contando cada par uma vez: mais da metade.
# Questão: 9 × 8 = 72 · 5 × 6 = 30 · 72 + 30 = 102.

TITULO = "Tabuada com macetes: 2, 5, 9 e 10"

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
    dict(id="s01", block="gancho", text="{a}Nove vezes sete. [p=0.3] Se você travou, {b}não é falta de capacidade: [p=0.2] mandaram decorar, e ninguém mostrou o caminho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você responde de cabeça as tabuadas do dois, do cinco, do nove e do dez. [p=0.3] Isso já resolve {b}mais da metade da tabuada, [p=0.2] e ainda tem um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}somar [p=0.2] e {c}subtrair de cabeça. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é vezes
    dict(id="s04", block="vezes", text="O que quer dizer {a}vezes? [p=0.3] Imagine uma compra em {b}quatro parcelas de três reais. [p=0.2] O total é {c}três mais três mais três mais três: [p=0.2] {d}doze. [p=0.3] Quatro vezes três é isso: [p=0.2] {e}o três repetido quatro vezes. [p=0.3] Na conta, a palavra vezes vira {f}este sinal em forma de xis."),
    dict(id="s05", block="vezes", text="Veja {a}quatro fileiras com três cadeiras. [p=0.2] Olhe a sala de lado: [p=0.2] {b}são três fileiras com quatro cadeiras. [p=0.3] As cadeiras são as mesmas: {c}doze. [p=0.3] Então, na multiplicação, {d}a ordem não muda o resultado."),
    dict(id="s06", block="vezes", text="{a}Tabuada é a tabela dessas contas, do um até o dez. [p=0.3] E ela não precisa entrar na marra."),
    # dez
    dict(id="s07", block="dez", text="Comece pela mais fácil, {a}a do dez. [p=0.2] {b}Sete vezes dez são sete notas de dez: [p=0.2] {c}setenta. [p=0.3] Na tabuada, vezes dez é {d}pôr um zero no fim. [p=0.3] Por quê? [p=0.2] Sete notas de dez são {e}sete dezenas: [p=0.2] o sete vai para a casa das dezenas, [p=0.2] e {f}a casa das unidades fica vazia."),
    # dois
    dict(id="s08", block="dois", text="A do dois é {a}o dobro, [p=0.2] que é o número somado com ele mesmo. [p=0.3] {b}Seis vezes dois é o mesmo que dois vezes seis: [p=0.2] {c}seis mais seis dá {d}doze. [p=0.3] {e}Oito vezes dois: [p=0.2] oito mais oito. [p=0.2] Completando o dez, dá {f}dezesseis."),
    # cinco
    dict(id="s09", block="cinco", text="A do cinco usa a do dez. [p=0.2] Uma nota de cinco vale {a}metade de uma nota de dez, [p=0.2] e metade é dividir em duas partes iguais. [p=0.3] Então {b}sete notas de cinco valem metade de sete notas de dez. [p=0.3] A regra: {c}faça vezes dez e corte ao meio."),
    dict(id="s10", block="cinco", text="{a}Sete vezes cinco. [p=0.2] Vezes dez dá {b}setenta. [p=0.3] Metade de setenta: [p=0.2] {c}metade de sessenta é trinta, [p=0.2] {d}metade de dez é cinco. [p=0.2] Juntando, {e}trinta e cinco. [p=0.3] Mais uma: {f}oito vezes cinco. [p=0.2] Vezes dez dá oitenta. [p=0.2] A metade é {g}quarenta."),
    # nove
    dict(id="s11", block="nove", text="A do nove também usa a do dez. [p=0.2] Nove vezes é {a}dez vezes menos uma vez. [p=0.3] Pense em {b}nove parcelas de sete reais: [p=0.2] são dez parcelas, tirando uma. [p=0.3] {c}Dez vezes sete dá setenta. [p=0.2] {d}Tire um sete: [p=0.2] {e}sessenta e três. [p=0.3] Confira: sessenta e três mais sete dá setenta."),
    dict(id="s12", block="nove", text="{a}Nove vezes quatro: [p=0.2] dez vezes quatro dá quarenta. [p=0.2] Tirando um quatro, fica {b}trinta e seis."),
    # o que já está resolvido
    dict(id="s13", block="mapa", text="Olhe {a}a tabuada inteira. [p=0.3] {b}Toda conta com dois, com cinco, com nove ou com dez já está resolvida. [p=0.3] {c}E vezes um é o próprio número: [p=0.2] sete vezes um dá sete. [p=0.3] O que sobrou é {d}bem menos do que parecia."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}somar no lugar de multiplicar. [p=0.2] A pessoa vê seis vezes dois e responde {b}oito. [p=0.3] Mas oito é {c}seis mais dois. [p=0.2] Seis vezes dois é o dois repetido seis vezes: [p=0.2] {d}doze."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho do nove. [p=0.2] {a}Nove vezes sete. [p=0.3] Tire um do sete: [p=0.2] {b}o seis é o primeiro algarismo. [p=0.3] Quanto falta do seis até o nove? [p=0.2] {c}Três: esse é o segundo algarismo. [p=0.3] {d}Sessenta e três."),
    dict(id="s16", block="atalho", text="Funciona porque é a conta de antes: {a}setenta menos sete. [p=0.3] Tirar sete de setenta {b}derruba a dezena de sete para seis. [p=0.2] Na unidade fica o que falta do sete até o dez: {c}três. [p=0.3] E o que falta do seis até o nove é {d}esse mesmo três. [p=0.3] {e}Não compensa fora da tabuada: [p=0.2] em {f}nove vezes doze, tirar um dá onze, e onze já passa de nove. [p=0.2] Aí, volte para {g}dez vezes menos uma vez."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Você comprou {a}nove caixas com oito garrafas cada [p=0.2] e {b}cinco caixas com seis garrafas cada. [p=0.3] {c}Quantas garrafas são ao todo?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Nove vezes oito: [p=0.2] dez vezes oito dá oitenta. [p=0.2] Tirando um oito, fica {b}setenta e dois. [p=0.3] {c}Cinco vezes seis: [p=0.2] dez vezes seis dá sessenta, [p=0.2] e a metade é {d}trinta. [p=0.3] Juntando: {e}setenta e dois mais trinta dá {f}cento e duas garrafas."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}vezes é soma repetida. [p=0.2] {b}Vezes cinco é metade de vezes dez. [p=0.2] {c}Vezes nove é dez vezes menos uma vez."),
    dict(id="s21", block="fim", text="Na próxima aula, você fecha {a}as tabuadas que faltam, [p=0.2] {b}dobrando resultados que já sabe. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
