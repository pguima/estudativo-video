# Estudativo · MAT-POT-006 — Praticando: potências (Matemática · Potências e Raízes · prática).
# Habilidade: simplificar expressões usando todas as propriedades de potência.
# Pré-requisitos: MAT-POT-001, MAT-POT-002, MAT-POT-003, MAT-POT-004, MAT-POT-005. Próxima: MAT-POT-007.
# Questões inéditas, criadas para esta aula. Sem somar frações (MAT-FRA-007 fora da ficha).
# 1: 8² · 4³ ÷ 2⁹ = 2⁶ · 2⁶ ÷ 2⁹ = 2³ = 8 (64 × 64 ÷ 512).
# 2: −2⁴ + (−2)³ × 3 = −16 − 24 = −40; com −2⁴ = 16 errado, −8.
# 3: 0,5³ × 2³ + 9⁰ = 1³ + 1 = 2 (0,125 × 8 = 1).
# 4: 15² × 3⁻² = 225 ÷ 9 = 25 = 5².
# 5: 10⁴ × 10⁻¹ = 10³ = 1.000 mm (10.000 × 0,1). Folha comum: cerca de 0,1 mm.

TITULO = "Praticando: potências"

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
    dict(id="s01", block="gancho", text="{a}Cinco contas, [p=0.2] criadas para esta aula. [p=0.3] Cada uma junta o que você viu sobre potências. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada."),
    # lembrete
    dict(id="s02", block="lembrete", text="Suas ferramentas: [p=0.2] {a}mesma base, vezes soma os expoentes e dividido subtrai. [p=0.2] {b}Expoente dentro e fora do parêntese, multiplica. [p=0.2] {c}A potência vem antes do vezes. [p=0.2] {d}Expoente negativo vira fração. [p=0.3] Se alguma travar, procure a aula no canal."),
    # conta 1: mesma base
    dict(id="s03", block="questao1", text="{a}Conta um. [p=0.2] {b}Oito ao quadrado vezes quatro ao cubo, [p=0.2] {c}dividido por dois elevado a nove. [p=0.3] {d}Quanto dá?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Oito é dois ao cubo. [p=0.2] {b}Quatro é dois ao quadrado. [p=0.3] Expoente dentro e fora do parêntese, multiplica: {c}oito ao quadrado vira dois elevado a seis. [p=0.2] {d}Quatro ao cubo também vira dois elevado a seis."),
    dict(id="s06", block="resposta1", text="Multiplicando, soma: {a}seis mais seis dá doze. [p=0.2] Dividindo, subtrai: {b}doze menos nove dá três. [p=0.2] {c}Dois ao cubo é oito. [p=0.3] Pelo caminho longo, seriam {d}sessenta e quatro vezes sessenta e quatro, e ainda uma divisão por quinhentos e doze."),
    # atalho
    dict(id="s07", block="atalho", text="Esse é o atalho da prática: {a}ponha tudo na mesma base. [p=0.3] Funciona porque {b}somar e subtrair expoentes pede base igual. [p=0.3] {c}Não compensa quando os números não vêm da mesma base, [p=0.2] como {d}oito e nove: [p=0.2] aí, calcule cada um."),
    # conta 2: sinais e ordem
    dict(id="s08", block="questao2", text="{a}Conta dois. [p=0.2] {b}Menos dois elevado a quatro, sem parênteses, [p=0.2] {c}mais, abre parênteses, menos dois, fecha parênteses, ao cubo, [p=0.2] {d}vezes três."),
    dict(id="s09", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="resposta2", text="Vamos lá. [p=0.2] As potências vêm primeiro. [p=0.2] {a}Sem parênteses, o menos fica de fora: {b}dois elevado a quatro dá dezesseis, [p=0.2] e o menos entra depois: {c}menos dezesseis. [p=0.2] {d}Com parênteses e expoente ímpar: menos oito. [p=0.3] Depois o vezes: {e}menos oito vezes três dá menos vinte e quatro."),
    dict(id="s11", block="resposta2", text="Por último, {a}uma dívida de dezesseis e outra de vinte e quatro: {b}menos quarenta. [p=0.3] Quem achou mais dezesseis no começo terminou em {c}menos oito, por causa de um parêntese que não existia."),
    # conta 3: juntar bases e expoente zero
    dict(id="s12", block="questao3", text="{a}Conta três. [p=0.2] {b}Zero vírgula cinco ao cubo, [p=0.2] {c}vezes dois ao cubo, [p=0.2] {d}mais nove elevado a zero."),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] Expoentes iguais, junte as bases: {a}abre parênteses, zero vírgula cinco vezes dois, fecha parênteses, ao cubo. [p=0.3] {b}Zero vírgula cinco vezes dois dá um. [p=0.2] {c}Um ao cubo dá um. [p=0.3] {d}Nove elevado a zero também dá um, e não zero. [p=0.2] Um mais um: {e}dois. [p=0.3] Confira: {f}zero vírgula cinco ao cubo é zero vírgula cento e vinte e cinco, e isso vezes oito dá um."),
    # conta 4: expoente negativo em fração
    dict(id="s15", block="questao4", text="{a}Conta quatro. [p=0.2] {b}Quinze ao quadrado [p=0.2] {c}vezes três elevado a menos dois."),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Vamos lá. [p=0.2] A escada dos quadrados dá {a}duzentos e vinte e cinco. [p=0.2] Expoente negativo vira fração: {b}um nono. [p=0.3] Um nono de duzentos e vinte e cinco: {c}dividido por nove dá vinte e cinco. [p=0.3] Outro caminho: quinze é {d}três vezes cinco. [p=0.2] {e}Três ao quadrado vezes cinco ao quadrado, vezes um nono. [p=0.2] Três ao quadrado é nove, e nove vezes um nono dá um. [p=0.2] {f}Sobra cinco ao quadrado."),
    # conta 5: base dez
    dict(id="s18", block="questao5", text="{a}Última conta, com medida. [p=0.2] A espessura de uma folha de papel comum, em milímetros, é cerca de {b}dez elevado a menos um. [p=0.3] Uma gráfica empilha {c}dez elevado a quatro folhas. [p=0.3] {d}Qual é a altura da pilha, em milímetros?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] Folhas vezes espessura: {a}dez elevado a quatro vezes dez elevado a menos um. [p=0.3] Mesma base, soma os expoentes. [p=0.2] Somar menos um é tirar um: {b}quatro menos um dá três. [p=0.2] {c}Dez ao cubo: {d}mil milímetros. [p=0.3] Confira: {e}dez mil vezes zero vírgula um dá mil. [p=0.3] Repare: o expoente é negativo, mas a altura não. [p=0.2] O menos só diz que a folha mede {f}um décimo de milímetro."),
    # última dica
    dict(id="s21", block="dica", text="Uma última dica, para quando bater a dúvida se uma regra existe: {a}teste com números pequenos. [p=0.3] {b}Abre parênteses, um mais dois, fecha parênteses, ao quadrado, é um ao quadrado mais dois ao quadrado? [p=0.3] {c}De um lado, três ao quadrado dá nove. [p=0.2] {d}Do outro, um mais quatro dá cinco. [p=0.3] Não bateu: {e}a regra não existe."),
    dict(id="s22", block="dica", text="Funciona porque {a}um exemplo que falha já derruba a regra. [p=0.3] Só que {b}um exemplo que bate não prova nada: [p=0.2] em dois ao quadrado, base vezes expoente também dá quatro, por coincidência. [p=0.3] {c}Bateu? Teste outro número."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}procure a mesma base, [p=0.2] {b}veja o que está dentro do parêntese [p=0.2] e {c}resolva a potência antes do vezes."),
    dict(id="s24", block="fim", text="Na próxima aula, você faz {a}o caminho de volta da potência: [p=0.2] {b}a raiz quadrada. [p=0.3] Fatorando, vai descobrir {c}qual número ao quadrado dá mil setecentos e sessenta e quatro. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
