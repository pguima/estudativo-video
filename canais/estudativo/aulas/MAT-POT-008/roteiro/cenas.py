# Estudativo · MAT-POT-008 — Expoente fracionário (Matemática · Potências e Raízes · Radiciação).
# Habilidade: ler 9^(1/2) como √9 e 8^(1/3) como ∛8 e calcular 8^(2/3) = 4.
# Pré-requisitos: MAT-POT-004, MAT-POT-016. Próxima: MAT-POT-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Origem pela potência de potência: (9^(1/2))² = 9^(1/2 · 2) = 9¹ = 9 · (8^(1/3))³ = 8¹ = 8. Sem expoente negativo (MAT-POT-005 fora da ficha).
# 8^(2/3) = (8^(1/3))² = 2² = 4. Erro: √(8³) = √512 ≈ 22,6. Atalho: 8 = 2³ → 2^(3 · 2/3) = 2² = 4.
# Questão: 25^(3/2) = (√25)³ = 5³ = 125; atalho (5²)^(3/2) = 5³. Inédita.

TITULO = "Expoente fracionário"

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
    dict(id="s01", block="gancho", text="{a}Nove elevado a um meio. [p=0.3] Se você pensou {b}quatro vírgula cinco, fez a metade de nove. [p=0.3] A resposta é {c}três."),
    dict(id="s02", block="gancho", text="Esse expoente em forma de fração não é invenção. [p=0.2] Ele sai {a}de uma regra que você já conhece."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}potência de potência [p=0.2] e {c}raiz quadrada e raiz cúbica. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem
    dict(id="s04", block="origem", text="Olhe a regra: {a}dois ao cubo, tudo elevado a quatro. [p=0.2] Vira {b}dois elevado a doze. [p=0.2] Os expoentes {c}se multiplicam: três vezes quatro."),
    dict(id="s05", block="origem", text="E se o expoente for {a}um meio? [p=0.2] O nove não pode aparecer meia vez em uma multiplicação, então contar não serve mais. [p=0.2] O valor dessa potência é escolhido para a regra continuar valendo. [p=0.3] Pegue {b}nove elevado a um meio e eleve tudo ao quadrado. [p=0.2] Multiplique os expoentes: {c}um meio vezes dois dá um. [p=0.2] Sobra {d}nove elevado a um, que é nove."),
    dict(id="s06", block="origem", text="Ou seja: nove elevado a um meio é {a}um número que, ao quadrado, dá nove. [p=0.3] Isso é a {b}raiz quadrada de nove. [p=0.2] E, como no símbolo da raiz, vale o positivo: {c}três. [p=0.3] Quatro vírgula cinco não serve: {d}ao quadrado, dá vinte vírgula vinte e cinco."),
    dict(id="s07", block="origem", text="Outra regra confirma. [p=0.2] Na multiplicação de mesma base, os expoentes se somam. [p=0.2] {a}Nove elevado a um meio vezes nove elevado a um meio. [p=0.2] Cada expoente é uma metade, e {b}duas metades fazem um inteiro. [p=0.2] O resultado é {c}nove elevado a um, que é nove. [p=0.2] De novo, o número vezes ele mesmo dá nove."),
    dict(id="s08", block="origem", text="Com um terço, a mesma ideia. [p=0.2] {a}Oito elevado a um terço, tudo ao cubo. [p=0.2] {b}Um terço vezes três dá um. [p=0.2] Sobra {c}oito. [p=0.3] Então oito elevado a um terço é o número que, ao cubo, dá oito: [p=0.2] {d}raiz cúbica de oito, que dá {e}dois."),
    dict(id="s09", block="origem", text="Viu o padrão? [p=0.2] {a}O de baixo da fração é o índice da raiz. [p=0.2] {b}Um meio é raiz quadrada. [p=0.2] {c}Um terço é raiz cúbica. [p=0.2] {d}Um quarto é raiz quarta."),
    # dois terços
    dict(id="s10", block="dois_tercos", text="E quando o de cima não é um? [p=0.2] {a}Oito elevado a dois terços. [p=0.3] {b}Dois terços é um terço vezes dois. [p=0.2] Pela mesma regra, você faz {c}oito elevado a um terço e depois {d}eleva ao quadrado."),
    dict(id="s11", block="dois_tercos", text="{a}Raiz cúbica de oito dá dois. [p=0.2] {b}Dois ao quadrado dá quatro. [p=0.3] Oito elevado a dois terços é {c}quatro. [p=0.3] {d}O de baixo é a raiz. [p=0.2] {e}O de cima é a potência."),
    dict(id="s12", block="dois_tercos", text="A ordem não muda o resultado. [p=0.2] Fazendo a potência primeiro: {a}oito ao quadrado dá sessenta e quatro, [p=0.2] e {b}raiz cúbica de sessenta e quatro dá quatro. [p=0.2] Só que a {c}raiz primeiro deixa números menores."),
    dict(id="s13", block="dois_tercos", text="Mais um: {a}vinte e sete elevado a dois terços. [p=0.2] {b}Raiz cúbica de vinte e sete dá três. [p=0.2] {c}Três ao quadrado dá nove."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}trocar os papéis: [p=0.2] usar o de cima como raiz e o de baixo como potência. [p=0.2] Aí daria {b}raiz quadrada de oito ao cubo. [p=0.2] Isso é raiz de quinhentos e doze, que {c}passa de vinte e dois. [p=0.3] Bem longe de quatro."),
    dict(id="s15", block="erro", text="Para não trocar, pense em uma planta: {a}a raiz fica embaixo da terra. [p=0.2] {b}O de baixo é a raiz."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}escreva a base como potência. [p=0.3] {b}Oito é dois ao cubo. [p=0.2] Fica {c}dois ao cubo, tudo elevado a dois terços. [p=0.2] {d}Três vezes dois terços dá dois. [p=0.2] Sobra {e}dois ao quadrado, que dá quatro."),
    dict(id="s17", block="atalho", text="Funciona porque é {a}potência de potência: [p=0.2] o expoente três cancela o três de baixo da fração. [p=0.3] Não compensa quando {b}esse cancelamento não acontece, [p=0.2] como em {c}dez elevado a um meio: dez não é o quadrado de nenhum número inteiro. [p=0.2] Raiz de dez não é exata: {d}deixe como raiz ou estime."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}Quanto dá vinte e cinco elevado a três meios?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] O de baixo é {a}dois: raiz quadrada. [p=0.2] {b}Raiz de vinte e cinco dá cinco. [p=0.2] O de cima é {c}três: ao cubo. [p=0.2] {d}Cinco ao cubo dá cento e vinte e cinco."),
    dict(id="s21", block="resposta", text="Pelo atalho: {a}vinte e cinco é cinco ao quadrado. [p=0.2] {b}Dois vezes três meios dá três. [p=0.2] {c}Cinco ao cubo dá de novo cento e vinte e cinco."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}expoente em fração é raiz disfarçada. [p=0.2] {b}O de baixo é a raiz [p=0.2] e {c}o de cima é a potência."),
    dict(id="s23", block="fim", text="Na próxima aula, você vai {a}multiplicar raízes, [p=0.2] {b}simplificar raiz de setenta e dois [p=0.2] e descobrir {c}quando dá para somar raízes. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
