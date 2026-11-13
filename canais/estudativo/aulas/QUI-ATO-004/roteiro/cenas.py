# Estudativo · QUI-ATO-004 — Prótons, nêutrons e elétrons: Z, A, íons e isótopos (Química · Átomo e Tabela Periódica).
# Habilidade: achar quantos prótons, nêutrons e elétrons tem o ²³Na⁺ e o ³⁵Cl⁻ usando Z e A e dizer se dois átomos são isótopos.
# Pré-requisitos: QUI-ATO-002, MAT-NUM-016. Próxima: QUI-ATO-005 (distribuição eletrônica pelo diagrama de Pauling).
# Questão inédita, criada para esta aula. Letras narradas: Z = "zê", A = "á".
# Fatos: Na Z = 11, A = 23 (12 nêutrons); Cl Z = 17, A = 35 (18 nêutrons); C-12, C-13, C-14 (6, 7, 8 nêutrons);
# Al Z = 13, A = 27 (14 nêutrons), Al³⁺ com 10 elétrons; Z = 14, A = 27 é o silício-27 (isóbaro, não isótopo);
# o elétron tem cerca de 1/1836 da massa do próton ("quase duas mil vezes mais leve").

TITULO = "Prótons, nêutrons e elétrons: Z, A, íons e isótopos"

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
    dict(id="s01", block="gancho", text="{a}Sódio vinte e três, com carga um mais. [p=0.3] {b}Quantos prótons, nêutrons e elétrons tem esse átomo? [p=0.3] {c}A resposta sai de duas contas de menos."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}contar as partículas de qualquer átomo ou íon [p=0.2] e {b}dizer se dois átomos são isótopos."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula do ouro: [p=0.1] {a}o átomo tem um núcleo positivo e, em volta, a eletrosfera. [p=0.3] E da Matemática: [p=0.1] {b}subtrair um número negativo é somar. [p=0.2] {c}Três menos, abre parênteses, menos cinco, fecha parênteses, dá oito."),
    # as partículas
    dict(id="s04", block="particulas", text="Dentro do núcleo há dois tipos de partícula. [p=0.2] {a}O próton tem carga positiva. [p=0.2] {b}O nêutron não tem carga: é neutro. [p=0.3] {c}Próton e nêutron têm quase a mesma massa, [p=0.1] e quase toda a massa do átomo fica neles."),
    dict(id="s05", block="particulas", text="{a}Na eletrosfera ficam os elétrons, com carga negativa. [p=0.2] {b}O elétron é quase duas mil vezes mais leve que o próton. [p=0.3] {c}Num átomo neutro, há tantos elétrons quanto prótons: [p=0.1] {d}as cargas se cancelam."),
    # Z e A
    dict(id="s06", block="za", text="{a}O número de prótons se chama número atômico, com a letra zê. [p=0.2] {b}Ele é a identidade do elemento. [p=0.3] {c}Todo átomo com onze prótons é sódio. [p=0.1] {d}Com dezessete, é cloro. [p=0.3] {e}Mudou o número de prótons, mudou o elemento."),
    dict(id="s07", block="za", text="{a}Prótons mais nêutrons dá o número de massa, com a letra á. [p=0.3] {b}Para achar os nêutrons, faça a conta ao contrário: [p=0.1] {c}nêutrons é igual ao número de massa menos o número atômico. [p=0.3] {d}Na escrita do átomo, o número de massa fica no alto, à esquerda do símbolo, [p=0.1] e o número atômico, embaixo, também à esquerda."),
    dict(id="s08", block="za", text="No sódio vinte e três, {a}o número atômico é onze, e o de massa, vinte e três. [p=0.2] {b}Onze prótons. [p=0.2] {c}Vinte e três menos onze dá doze nêutrons. [p=0.2] {d}E, se o átomo é neutro, onze elétrons."),
    # íons
    dict(id="s09", block="ions", text="Só que {a}o átomo pode ganhar ou perder elétrons. [p=0.2] {b}O núcleo não muda, [p=0.1] só a eletrosfera. [p=0.3] Com elétrons a mais ou a menos, {c}as cargas não se cancelam, [p=0.1] e o átomo vira {d}um íon."),
    dict(id="s10", block="ions", text="{a}Perdeu elétrons? [p=0.1] Sobra positivo: {b}é um cátion. [p=0.2] {c}Ganhou elétrons? [p=0.1] Sobra negativo: {d}é um ânion. [p=0.3] {e}A carga, escrita no alto à direita, diz quantos elétrons mudaram."),
    dict(id="s11", block="ions", text="{a}Sódio com carga um mais: [p=0.1] perdeu um elétron. [p=0.2] {b}Onze prótons, [p=0.1] {c}doze nêutrons [p=0.1] e {d}onze menos um, que dá dez elétrons."),
    dict(id="s12", block="ions", text="{a}Cloro trinta e cinco, com carga um menos. [p=0.1] O zê do cloro é dezessete. [p=0.2] {b}Dezessete prótons. [p=0.2] {c}Trinta e cinco menos dezessete dá dezoito nêutrons. [p=0.2] {d}Ganhou um elétron: [p=0.1] dezessete mais um dá dezoito elétrons."),
    # isótopos
    dict(id="s13", block="isotopos", text="{a}Átomos do mesmo elemento podem ter números de nêutrons diferentes. [p=0.2] Eles se chamam {b}isótopos: [p=0.1] {c}mesmo zê, número de massa diferente. [p=0.3] {d}Carbono doze, carbono treze e carbono catorze. [p=0.2] {e}Todos têm seis prótons. [p=0.2] Os nêutrons são {f}seis, sete e oito."),
    dict(id="s14", block="isotopos", text="Isótopos são {a}o mesmo elemento: [p=0.1] {b}muda só o número de nêutrons, e com ele a massa."),
    # erro
    dict(id="s15", block="erro", text="O erro comum: [p=0.1] {a}achar que o cátion ganhou elétrons, [p=0.1] por causa do sinal de mais. [p=0.3] {b}É o contrário. [p=0.1] {c}O elétron é negativo, [p=0.1] {d}então perder elétron deixa o saldo positivo."),
    # atalho
    dict(id="s16", block="atalho", text="O atalho para os elétrons: [p=0.1] {a}elétrons é igual a zê menos a carga. [p=0.3] {b}Sódio um mais: onze menos um dá dez. [p=0.3] {c}Cloro um menos: dezessete menos, abre parênteses, menos um, fecha parênteses, [p=0.1] dá dezoito."),
    dict(id="s17", block="atalho", text="Funciona porque {a}cada carga positiva é um elétron que falta, [p=0.2] e {b}cada carga negativa é um elétron que sobra. [p=0.3] {c}Não compensa se você se perde no sinal. [p=0.2] Aí, pense em {d}perdeu ou ganhou, e faça a conta direto."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] O alumínio vinte e sete, de zê treze, forma {a}o íon com carga três mais. [p=0.3] {b}Quantos prótons, nêutrons e elétrons tem esse íon? [p=0.3] E {c}um átomo de zê catorze e número de massa vinte e sete é isótopo do alumínio?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Treze prótons, o próprio zê. [p=0.2] {b}Vinte e sete menos treze dá catorze nêutrons. [p=0.2] {c}Carga três mais: perdeu três elétrons. [p=0.1] Treze menos três dá {d}dez elétrons. [p=0.3] {e}Se você achou dezesseis, somou a carga: [p=0.1] é o erro do sinal de mais."),
    dict(id="s21", block="resposta", text="{a}E o átomo de zê catorze? [p=0.2] {b}Tem o mesmo número de massa, mas outro zê. [p=0.2] Outro número de prótons é {c}outro elemento. [p=0.2] {d}Não é isótopo do alumínio."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: [p=0.1] {a}zê conta os prótons. [p=0.1] {b}Número de massa menos zê dá os nêutrons. [p=0.1] {c}Elétrons é zê menos a carga. [p=0.1] {d}E isótopos têm o mesmo zê."),
    dict(id="s23", block="fim", text="Na próxima aula, você distribui {a}os vinte e seis elétrons do ferro [p=0.1] pelo {b}diagrama de Pauling, seguindo as diagonais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
