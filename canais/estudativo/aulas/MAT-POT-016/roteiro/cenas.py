# Estudativo · MAT-POT-016 — Raiz de fração e decimal, raiz cúbica e raiz de negativo (Matemática · Potências e Raízes · Radiciação).
# Habilidade: calcular √(9/16), √0,25, ∛27 e ⁴√16, dizer que ∛−8 = −2 e saber que √−4 não dá número da reta.
# Pré-requisitos: MAT-POT-002, MAT-POT-007. Próxima: MAT-POT-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# √(9/16) = 3/4; (3/4)² = 9/16 · √0,25 = √(25/100) = 5/10 = 0,5; 0,5² = 0,25 · ∛27 = 3 · ⁴√16 = 2.
# ∛−8 = −2: (−2)(−2) = 4; 4(−2) = −8 · √−4: 2² = 4, (−2)² = 4, 0² = 0: sem número da reta. Sem números complexos.
# Atalho: √1,44 = 1,2 (√144 = 12; duas casas → uma) · √0,4 ≠ 0,2 (0,2² = 0,04).
# Questão: √(25/49) = 5/7 · √0,09 = 0,3 · ∛−64 = −4 · √−25 não dá número da reta. Inédita.

TITULO = "Raiz de fração e decimal, raiz cúbica e raiz de negativo"

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
    dict(id="s01", block="gancho", text="{a}Raiz quadrada de zero vírgula vinte e cinco. [p=0.3] A resposta é {b}zero vírgula cinco, [p=0.2] que é {c}maior que o número de dentro. [p=0.3] Raiz nem sempre diminui."),
    dict(id="s02", block="gancho", text="E tem raiz de número negativo que {a}existe, [p=0.2] e outra que {b}não dá número nenhum da reta. [p=0.3] Uma pergunta só resolve tudo isso."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}raiz quadrada, o número que vezes ele mesmo dá o de dentro, [p=0.2] e {c}potência de negativo, de fração e de decimal. [p=0.3] Se faltar alguma, procure no canal."),
    # fração
    dict(id="s04", block="fracao", text="Comece por {a}raiz de nove dezesseis avos. [p=0.2] Multiplicar fração é de cima com de cima, de baixo com de baixo. [p=0.2] Então a raiz faz o caminho de volta: {b}raiz de nove em cima dá três, [p=0.2] {c}raiz de dezesseis embaixo dá quatro. [p=0.2] Resposta: {d}três quartos."),
    dict(id="s05", block="fracao", text="Conferindo: {a}três quartos vezes três quartos dá nove dezesseis avos."),
    # decimal
    dict(id="s06", block="decimal", text="No decimal, a ideia é a mesma. [p=0.2] {a}Zero vírgula vinte e cinco é vinte e cinco centésimos. [p=0.3] {b}Raiz de vinte e cinco dá cinco. [p=0.2] {c}Raiz de cem dá dez. [p=0.2] Fica {d}cinco décimos, que é zero vírgula cinco."),
    dict(id="s07", block="decimal", text="Conferindo: {a}zero vírgula cinco vezes ele mesmo dá zero vírgula vinte e cinco. [p=0.3] Sempre que o número está {b}entre zero e um, a raiz fica maior que ele."),
    # cúbica
    dict(id="s08", block="cubica", text="E se o número se repetir três vezes? [p=0.2] Imagine {a}um cubo montado com vinte e sete cubinhos. [p=0.2] Quantos cubinhos tem cada lado? [p=0.3] {b}Três cubinhos, porque três vezes três vezes três dá vinte e sete. [p=0.2] Essa é a {c}raiz cúbica: raiz cúbica de vinte e sete é três."),
    dict(id="s09", block="indice", text="O número pequeno na abertura do símbolo se chama {a}índice. [p=0.2] Ele diz quantas vezes o número se repete. [p=0.3] {b}Índice três é raiz cúbica. [p=0.2] {c}Índice quatro é raiz quarta: [p=0.2] {d}raiz quarta de dezesseis é dois. [p=0.2] Confira: dois vezes dois vezes dois vezes dois dá dezesseis. [p=0.2] Com índice par, vale o combinado da raiz quadrada: fica o positivo."),
    dict(id="s10", block="indice", text="Na raiz quadrada, o {a}índice é dois, e nem se escreve."),
    # negativo
    dict(id="s11", block="negativo", text="E com negativo? [p=0.2] {a}Raiz cúbica de menos oito. [p=0.2] Que número, repetido três vezes, dá menos oito? [p=0.3] {b}Menos dois vezes menos dois dá quatro. [p=0.2] {c}Quatro vezes menos dois dá menos oito. [p=0.3] A resposta é {d}menos dois."),
    dict(id="s12", block="negativo", text="E a {a}raiz quadrada de menos quatro? [p=0.2] {b}Dois vezes dois dá quatro positivo. [p=0.2] {c}Menos dois vezes menos dois também. [p=0.2] Zero vezes zero dá zero. [p=0.3] Número vezes ele mesmo {d}nunca dá negativo. [p=0.2] Então {e}não existe número da reta para essa raiz."),
    dict(id="s13", block="negativo", text="A regra: {a}índice ímpar aceita negativo. [p=0.2] {b}Índice par não aceita. [p=0.3] É o que você viu na potência: cada dupla de menos vira mais. [p=0.2] Com índice par, todos os menos formam dupla, e o resultado nunca é negativo. [p=0.2] Com índice ímpar, sobra um menos sem dupla."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}escrever que raiz quadrada de menos quatro é menos dois. [p=0.3] Confira: {b}menos dois vezes menos dois dá quatro positivo, não menos quatro. [p=0.2] Na raiz quadrada, {c}o sinal de menos não sai de dentro."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho para decimal: {a}metade das casas. [p=0.3] {b}Um vírgula quarenta e quatro tem duas casas. [p=0.2] Esqueça a vírgula: {c}raiz de cento e quarenta e quatro dá doze. [p=0.2] A raiz leva a metade das casas, uma só: {d}um vírgula dois."),
    dict(id="s16", block="atalho", text="Funciona porque, ao multiplicar decimais, {a}as casas se somam: [p=0.2] uma mais uma dá duas. [p=0.3] Não compensa com {b}número ímpar de casas. [p=0.2] Raiz de zero vírgula quatro {c}não é zero vírgula dois, [p=0.2] porque esse vezes ele mesmo dá {d}zero vírgula zero quatro. [p=0.2] Aí, cerque o valor."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Quatro raízes: {a}raiz de vinte e cinco quarenta e nove avos, [p=0.2] {b}raiz de zero vírgula zero nove, [p=0.2] {c}raiz cúbica de menos sessenta e quatro [p=0.2] e {d}raiz quadrada de menos vinte e cinco. [p=0.3] {e}Uma não dá número da reta: qual? [p=0.2] {f}Calcule as outras."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Raiz de vinte e cinco dá cinco, raiz de quarenta e nove dá sete: {a}cinco sétimos. [p=0.3] Zero vírgula zero nove tem duas casas: raiz de nove dá três. [p=0.2] Com uma casa fica {b}zero vírgula três."),
    dict(id="s20", block="resposta", text="Na raiz cúbica, {a}quatro vezes quatro vezes quatro dá sessenta e quatro. [p=0.2] Com índice ímpar, o sinal fica: {b}menos quatro. [p=0.3] A última tem índice par e número negativo: {c}não dá número da reta."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}o índice diz quantas vezes o número se repete, [p=0.2] e {b}índice par com negativo não dá número da reta."),
    dict(id="s22", block="fim", text="Na próxima aula, uma surpresa: {a}expoente em forma de fração. [p=0.2] Você vai ver que {b}nove elevado a um meio é a raiz de nove. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
