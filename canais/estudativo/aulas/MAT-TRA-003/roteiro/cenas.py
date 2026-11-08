# Estudativo · MAT-TRA-003 — Qual lei usar: senos ou cossenos (Matemática · Trigonometria Avançada · Lei dos senos e dos cossenos).
# Habilidade: olhar os dados e escolher a lei certa, achar a distância entre dois pontos separados por um lago e dizer, só pelos
#   lados 4, 5 e 7, que o triângulo é obtusângulo.
# Pré-requisitos: MAT-TRA-001 (lei dos senos, par completo, número fixo), MAT-TRA-002 (lei dos cossenos, atalho 60° → −bc).
#   Usa MAT-ANG-004 (soma 180°), MAT-ANG-005 (acutângulo, retângulo, obtusângulo), MAT-ANG-015 (Pitágoras). Próxima: MAT-TRA-004.
# Questão inédita, criada para esta aula; o lago é uma situação imaginada. Seno e cosseno por extenso.
# Lago: CA = 80 m, CB = 50 m, ângulo C = 60° · AB² = 6.400 + 2.500 − 80 · 50 = 8.900 − 4.000 = 4.900 · AB = 70 m.
# 4, 5, 7: 49 = 16 + 25 − 40 cos → 41 − 40 cos = 49 → cos = −8/40 = −1/5 < 0 → obtuso. Atalho: 49 > 41.
# Erro: lei dos senos sem par (80 / sen ? = 50 / sen ?): duas incógnitas.
# Questão: 6, 8, 11 · 121 > 36 + 64 = 100 → obtusângulo · dois ângulos e o lado entre eles → terceiro ângulo pela soma 180° → senos.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Qual lei usar: senos ou cossenos"

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
    dict(id="s01", block="gancho", text="{a}Dois pontos separados por um lago. [p=0.2] Ninguém atravessa a água esticando uma trena. [p=0.3] Mas, de um terceiro ponto, dá para medir {b}a distância até cada um [p=0.2] e {c}o ângulo entre essas direções. [p=0.3] {d}Senos ou cossenos? [p=0.2] Escolher a lei é metade da questão."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você olha os dados e escolhe a lei certa, [p=0.2] e leva um {b}atalho para saber, só pelos lados, se o triângulo tem um ângulo obtuso."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a lei dos senos, em que cada lado dividido pelo seno do ângulo de frente dá o mesmo número; [p=0.2] e {c}a lei dos cossenos, o Pitágoras com um ajuste. [p=0.3] Se faltar alguma, procure no canal."),
    # a decisão
    dict(id="s04", block="decide", text="A pergunta que decide é uma só: {a}tem um par completo? [p=0.2] Ou seja, um lado e o ângulo de frente para ele. [p=0.3] {b}Tem par completo: lei dos senos. [p=0.2] Ela usa esse par para achar o que falta."),
    dict(id="s05", block="decide", text="{a}Não tem par completo: lei dos cossenos. [p=0.2] Isso acontece em dois casos: [p=0.2] {b}dois lados e o ângulo entre eles, [p=0.2] ou {c}os três lados, sem nenhum ângulo."),
    dict(id="s06", block="decide", text="E se vierem {a}dois ângulos e um lado que não fica de frente para nenhum deles? [p=0.2] {b}Ache o terceiro ângulo, porque a soma é cento e oitenta graus. [p=0.2] Pronto: {c}apareceu o par, e é lei dos senos."),
    # o lago
    dict(id="s07", block="lago", text="De volta ao lago. [p=0.2] Do terceiro ponto, {a}a distância até um dos pontos é oitenta metros, [p=0.2] {b}até o outro, cinquenta metros, [p=0.2] e {c}o ângulo entre as direções é de sessenta graus. [p=0.3] {d}Dois lados e o ângulo entre eles: [p=0.2] nenhum par completo. [p=0.2] Lei dos cossenos."),
    dict(id="s08", block="lago", text="Sessenta graus: {a}vale o atalho do menos o produto. [p=0.2] {b}Oitenta ao quadrado, seis mil e quatrocentos. [p=0.2] {c}Cinquenta ao quadrado, dois mil e quinhentos. [p=0.2] {d}Oitenta vezes cinquenta, quatro mil. [p=0.3] {e}Seis mil e quatrocentos, mais dois mil e quinhentos, menos quatro mil: [p=0.2] quatro mil e novecentos. [p=0.2] {f}A raiz dá setenta metros de um ponto ao outro."),
    # obtuso pelos lados
    dict(id="s09", block="lados", text="E com os três lados? [p=0.2] Veja o triângulo de lados {a}quatro, cinco e sete. [p=0.3] O maior ângulo fica {b}de frente para o maior lado, o sete. [p=0.3] Pela lei dos cossenos, {c}quarenta e nove é igual a dezesseis mais vinte e cinco, menos o ajuste."),
    dict(id="s10", block="lados", text="{a}Dezesseis mais vinte e cinco dá quarenta e um. [p=0.2] Para chegar a quarenta e nove, {b}o ajuste precisa somar oito. [p=0.3] Ajuste que soma vem de {c}cosseno negativo, [p=0.2] e cosseno negativo é {d}ângulo maior que noventa graus. [p=0.3] {e}O triângulo é obtusângulo."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}começar pela lei dos senos sem par completo. [p=0.2] No lago, seria {b}oitenta dividido pelo seno do ângulo de frente para ele. [p=0.2] Que ângulo? [p=0.2] {c}Ninguém sabe. [p=0.3] A igualdade fica com duas incógnitas, e a conta não sai. [p=0.2] {d}Sem par completo, cossenos."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}compare o quadrado do maior lado com a soma dos quadrados dos outros dois. [p=0.3] {b}Maior: obtusângulo. [p=0.2] {c}Igual: retângulo, porque é o próprio Pitágoras. [p=0.2] {d}Menor: acutângulo, com os três ângulos agudos."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a diferença é o ajuste da lei dos cossenos, [p=0.2] e o sinal dela diz o sinal do cosseno. [p=0.3] {b}Só vale com o maior lado. [p=0.2] Com um lado menor, o teste sempre dá agudo [p=0.2] e não diz nada sobre o triângulo."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um terreno triangular tem lados de {a}seis, oito e onze metros. [p=0.3] {b}Ele tem um ângulo obtuso? [p=0.3] E se, em vez dos lados, você soubesse {c}dois ângulos e o lado entre eles, {d}que lei usaria?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] O maior lado é onze: {a}onze ao quadrado, cento e vinte e um. [p=0.2] {b}Seis ao quadrado mais oito ao quadrado, trinta e seis mais sessenta e quatro, cem. [p=0.3] {c}Cento e vinte e um é maior que cem: [p=0.2] {d}tem um ângulo obtuso, de frente para o onze."),
    dict(id="s17", block="resposta", text="Na segunda parte: {a}dois ângulos dão o terceiro, pela soma de cento e oitenta. [p=0.2] Aí {b}o lado conhecido ganha o ângulo de frente: [p=0.2] par completo. [p=0.2] {c}Lei dos senos."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}tem par completo, senos. [p=0.2] {b}Dois lados e o ângulo entre eles, ou três lados, cossenos. [p=0.2] E {c}o quadrado do maior lado diz se tem ângulo obtuso."),
    dict(id="s19", block="fim", text="Na próxima aula, a trigonometria ganha {a}três parentes: secante, cossecante e cotangente. [p=0.2] Com eles, você {b}simplifica expressões, [p=0.2] como {c}um menos cosseno ao quadrado, dividido por seno, que vira só o seno. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
