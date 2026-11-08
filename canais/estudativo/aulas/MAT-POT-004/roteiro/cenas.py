# Estudativo · MAT-POT-004 — Potência de potência e de um produto (Matemática · Potências e Raízes).
# Habilidade: reduzir (2³)⁴ a 2¹², calcular (2 · 5)³ e escrever 64 como 2⁶ e 360 como 2³ · 3² · 5.
# Pré-requisitos: MAT-DIV-003 (fatoração), MAT-POT-002 (potência de negativo, fração ou decimal), MAT-POT-003 (mesma base). Próxima: MAT-POT-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Fatoração pelas divisões sucessivas, como em MAT-DIV-003.
# (2³)⁴ = 8⁴ = 4.096 = 2¹²; o erro dá 2⁷ = 128 · (2 · 5)³ = 10³ = 1.000 = 8 × 125 · 64 → 32 → 16 → 8 → 4 → 2 → 1 = 2⁶ · 360 = 2³ · 3² · 5 (8 × 9 = 72; 72 × 5 = 360).
# Erro: (2 + 3)² = 25; 2² + 3² = 13. Atalho: 2⁴ · 5³ = 2 · 10³ = 2.000 = 16 × 125.
# Questão: 216 → 108 → 54 → 27 → 9 → 3 → 1 = 2³ · 3³ = (2 · 3)³ = 6³.

TITULO = "Potência de potência e de um produto"

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
    dict(id="s01", block="gancho", text="{a}Abre parênteses, dois ao cubo, fecha parênteses, elevado a quatro. [p=0.3] Se você {b}somou os expoentes e chegou em dois elevado a sete, [p=0.2] {c}errou. [p=0.2] A resposta é {d}dois elevado a doze."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você sabe quando somar e quando multiplicar expoentes, [p=0.2] escreve {b}números grandes como potências de primos [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}multiplicando potências de mesma base, soma os expoentes, [p=0.2] e {c}fatorar é escrever um número como multiplicação só de primos. [p=0.3] Se faltar alguma, procure no canal."),
    # potência de potência
    dict(id="s04", block="potpot", text="Em um laboratório, uma colônia de bactérias {a}dobra a cada hora. [p=0.3] Um turno dura {b}três horas, [p=0.2] então cada turno multiplica a colônia por dois ao cubo. [p=0.3] Depois de {c}quatro turnos, a conta é {d}abre parênteses, dois ao cubo, fecha parênteses, elevado a quatro."),
    dict(id="s05", block="potpot", text="Quantas horas foram? [p=0.2] {a}Quatro vezes três dá doze. [p=0.3] Abra para ver: {b}o dois ao cubo aparece quatro vezes, [p=0.2] e {c}em cada um o dois aparece três vezes. [p=0.3] São {d}quatro blocos de três: [p=0.2] {e}dois elevado a doze."),
    dict(id="s06", block="potpot", text="A regra: {a}potência de potência, [p=0.2] {b}repete a base e multiplica os expoentes. [p=0.3] Compare com a soma. [p=0.2] {c}Dois ao cubo vezes dois elevado a quatro tem um vezes entre as potências: soma, e dá sete. [p=0.2] {d}Com o parêntese, um expoente fica dentro e o outro fora: multiplica, e dá doze."),
    # potência de um produto
    dict(id="s07", block="produto", text="E quando a base é uma multiplicação? [p=0.2] {a}Abre parênteses, dois vezes cinco, fecha parênteses, ao cubo. [p=0.3] Pela ordem, primeiro o parêntese: {b}dois vezes cinco dá dez. [p=0.2] {c}Dez ao cubo dá mil."),
    dict(id="s08", block="produto", text="Abra a potência. [p=0.2] O parêntese aparece três vezes: {a}dois vezes cinco, repetido três vezes. [p=0.3] Multiplicação aceita trocar a ordem, então {b}junte quem é igual. [p=0.2] Fica {c}dois ao cubo vezes cinco ao cubo. [p=0.2] {d}Oito vezes cento e vinte e cinco dá mil de novo."),
    dict(id="s09", block="produto", text="A regra: {a}o expoente de fora vai para cada número da multiplicação. [p=0.3] Ela vale também ao contrário: [p=0.2] {b}numa multiplicação com expoentes iguais, junte as bases. [p=0.3] Base diferente continua sem somar expoente. [p=0.2] Aqui é outra regra: {c}o expoente fica como está."),
    # fatoração com potências
    dict(id="s10", block="fatorar", text="Potência também {a}encurta a fatoração. [p=0.3] {b}Sessenta e quatro. [p=0.2] Divisões sucessivas pelo menor primo: {c}trinta e dois. [p=0.2] {d}Dezesseis. [p=0.2] {e}Oito. [p=0.2] {f}Quatro. [p=0.2] {g}Dois. [p=0.2] {h}Um. [p=0.3] Foram {i}seis divisões por dois: [p=0.2] {j}sessenta e quatro é dois elevado a seis."),
    dict(id="s11", block="fatorar", text="Com primos diferentes, junte os iguais. [p=0.2] Você já fatorou {a}trezentos e sessenta: {b}dois vezes dois vezes dois vezes três vezes três vezes cinco. [p=0.3] {c}O dois aparece três vezes: dois ao cubo. [p=0.2] {d}O três aparece duas vezes: três ao quadrado. [p=0.2] {e}O cinco aparece uma vez, e o expoente um não se escreve. [p=0.3] {f}Fica dois ao cubo vezes três ao quadrado vezes cinco."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é levar o expoente {a}para dentro de qualquer parêntese. [p=0.3] {b}Abre parênteses, dois mais três, fecha parênteses, ao quadrado. [p=0.2] A pessoa escreve {c}dois ao quadrado mais três ao quadrado: quatro mais nove dá treze."),
    dict(id="s13", block="erro", text="Mas o parêntese vem primeiro: {a}dois mais três dá cinco. [p=0.2] {b}Cinco ao quadrado dá vinte e cinco. [p=0.3] A regra vale para {c}multiplicação, nunca para soma."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}procure pares de dois e cinco. [p=0.3] Cada par {b}vira um dez, e vezes dez é só acrescentar zero. [p=0.3] {c}Dois elevado a quatro vezes cinco ao cubo: [p=0.2] dá para formar {d}três pares, e {e}sobra um número dois."),
    dict(id="s15", block="atalho", text="Três pares são {a}dez ao cubo, que é mil. [p=0.2] {b}Vezes o dois que sobrou dá dois mil. [p=0.3] Sem o atalho, você faria dezesseis vezes cento e vinte e cinco para chegar no mesmo lugar."),
    dict(id="s16", block="atalho", text="Funciona porque {a}a ordem da multiplicação não muda o resultado. [p=0.3] {b}Não compensa quando falta o dois ou o cinco, [p=0.2] como em {c}três ao quadrado vezes sete ao quadrado: [p=0.2] ali não se forma nenhum dez."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Fatore duzentos e dezesseis, usando potências. [p=0.3] Depois, {b}escreva o resultado como uma potência só."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Por dois: {a}cento e oito. [p=0.2] {b}Cinquenta e quatro. [p=0.2] {c}Vinte e sete. [p=0.2] Foram três divisões: {d}dois ao cubo. [p=0.3] Por três: {e}nove. [p=0.2] {f}Três. [p=0.2] {g}Um. [p=0.2] Mais três divisões: {h}três ao cubo."),
    dict(id="s20", block="resposta", text="Expoentes iguais, junte as bases: {a}abre parênteses, dois vezes três, fecha parênteses, ao cubo. [p=0.3] Resposta: {b}seis ao cubo. [p=0.2] Confira: {c}seis vezes seis vezes seis dá duzentos e dezesseis."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}mesma base, com vezes entre as potências, soma. [p=0.2] {b}Expoente dentro e expoente fora do parêntese, multiplica. [p=0.2] {c}Expoente de fora vai para cada número da multiplicação."),
    dict(id="s22", block="fim", text="Na próxima aula, o expoente {a}fica negativo, [p=0.2] e você escreve {b}dez elevado a menos três como número decimal, contando as casas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
