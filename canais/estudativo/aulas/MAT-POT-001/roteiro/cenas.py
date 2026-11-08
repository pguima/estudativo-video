# Estudativo · MAT-POT-001 — O que é potência (Matemática · Potências e Raízes).
# Habilidade: calcular 2⁵ = 32 sem confundir com 2 × 5, dizer os quadrados de 1 a 15 e usar o macete de 35².
# Pré-requisitos: MAT-NUM-008 (multiplicar por dois algarismos). Próxima: MAT-POT-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sem divisão, decimal, fração, negativo ou "fator": fora da ficha desta aula.
# Escada: 1, +3 = 4, +5 = 9, +7 = 16, +9 = 25 ... 100, +21 = 121, +23 = 144, +25 = 169, +27 = 196, +29 = 225. Pulo = lado antigo + lado novo.
# 35²: faixa de 5 × 35 cortada e colada: 30 × 40 = 1.200, sobra canto 5 × 5 = 25; total 1.225. 36²: 30 × 42 + 6 × 6 = 1.296.
# Questão: 5⁴ = 25, 125, 625 (5 × 4 = 20 é o erro) · 45²: 4 × 5 = 20 → 2.025.

TITULO = "O que é potência"

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
    dict(id="s01", block="gancho", text="{a}Dois elevado a cinco. [p=0.3] Se você respondeu {b}dez, [p=0.2] caiu no erro mais comum. [p=0.3] A resposta é {c}trinta e dois."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula qualquer potência, [p=0.2] monta os {b}quadrados de um a quinze sem decorar lista [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}a tabuada [p=0.2] e {c}multiplicar por dois algarismos. [p=0.3] Se faltar alguma, procure no canal."),
    # dobrar o papel
    dict(id="s04", block="papel", text="Pegue {a}uma folha de papel e dobre ao meio. [p=0.2] Ficam {b}duas camadas. [p=0.3] Dobre de novo: {c}quatro. [p=0.2] De novo: {d}oito. [p=0.3] Cada dobra multiplica as camadas por dois."),
    dict(id="s05", block="papel", text="Depois de {a}cinco dobras, a conta é {b}dois vezes dois vezes dois vezes dois vezes dois. [p=0.2] Dá {c}trinta e duas camadas. [p=0.3] Existe uma forma curta: {d}um dois grande com um cinco pequeno no alto. [p=0.2] Você lê assim: dois elevado a cinco."),
    # nomes
    dict(id="s06", block="nomes", text="Essa forma curta se chama {a}potência. [p=0.3] O número escrito grande é {b}a base: [p=0.2] é ele que se repete. [p=0.3] O número escrito pequeno é {c}o expoente: [p=0.2] ele diz {d}quantas vezes a base aparece na multiplicação."),
    dict(id="s07", block="nomes", text="Veja mais uma: {a}três elevado a quatro. [p=0.3] O três aparece quatro vezes: {b}três vezes três vezes três vezes três. [p=0.3] Uma conta por vez: {c}nove. [p=0.2] {d}Vinte e sete. [p=0.2] {e}Oitenta e um."),
    dict(id="s08", block="nomes", text="Alguns expoentes têm nome próprio. [p=0.2] Elevado a dois se diz {a}ao quadrado. [p=0.2] Elevado a três se diz {b}ao cubo. [p=0.3] {c}Três ao quadrado são as lajotas de um piso quadrado: três fileiras de três dão nove. [p=0.3] {d}Dois ao cubo são caixinhas empilhadas em um cubo: [p=0.2] duas de largura, duas de fundo e duas de altura. [p=0.2] São {e}oito caixinhas."),
    # quadrados
    dict(id="s09", block="quadrados", text="Vale ter {a}os quadrados de um a quinze na ponta da língua. [p=0.3] Mas não decore lista. [p=0.2] {b}Veja o piso crescer."),
    dict(id="s10", block="quadrados", text="Um piso de {a}três por três tem nove lajotas. [p=0.3] Para virar {b}quatro por quatro, encoste {c}três lajotas de um lado, [p=0.2] {d}três do outro [p=0.2] e {e}uma no canto. [p=0.3] São {f}sete lajotas novas. [p=0.2] Nove mais sete: {g}dezesseis."),
    dict(id="s11", block="quadrados", text="A cada piso, o lado cresce um, [p=0.2] então a faixa nova ganha sempre {a}duas lajotas a mais. [p=0.3] Daí sai uma escada. [p=0.2] Comece no {b}um. [p=0.2] {c}Mais três dá quatro. [p=0.2] {d}Mais cinco dá nove. [p=0.2] {e}Mais sete dá dezesseis. [p=0.2] {f}Mais nove dá vinte e cinco."),
    dict(id="s12", block="quadrados", text="{a}Mais onze dá trinta e seis. [p=0.2] {b}Mais treze dá quarenta e nove. [p=0.2] {c}Mais quinze dá sessenta e quatro. [p=0.2] {d}Mais dezessete dá oitenta e um. [p=0.2] {e}Mais dezenove dá cem. [p=0.3] Até aqui, a tabuada confere cada degrau. [p=0.2] Depois do cem, a escada continua. [p=0.2] {f}Mais vinte e um dá cento e vinte e um. [p=0.2] {g}Mais vinte e três dá cento e quarenta e quatro. [p=0.2] {h}Mais vinte e cinco dá cento e sessenta e nove. [p=0.2] {i}Mais vinte e sete dá cento e noventa e seis. [p=0.2] {j}Mais vinte e nove dá duzentos e vinte e cinco."),
    dict(id="s13", block="quadrados", text="O pulo é sempre {a}o lado antigo mais o lado novo. [p=0.3] Do piso treze para o piso catorze, o pulo é {b}treze mais catorze: vinte e sete. [p=0.3] Você não guarda quinze resultados: {c}guarda uma regra e sobe a escada."),
    # erro
    dict(id="s14", block="erro", text="O erro do começo: [p=0.2] {a}dois vezes cinco é dois mais dois mais dois mais dois mais dois: dez. [p=0.3] {b}Dois elevado a cinco troca cada mais por vezes: trinta e dois. [p=0.3] Um caso engana: {c}em dois ao quadrado, base vezes expoente também dá quatro. [p=0.2] É coincidência. [p=0.2] Troque a base: {d}três ao quadrado dá nove, e três vezes dois dá seis."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}quadrado de número terminado em cinco. [p=0.3] {b}Trinta e cinco ao quadrado. [p=0.2] {c}Tire o cinco do final: sobra o três. [p=0.2] {d}Multiplique pelo número seguinte: três vezes quatro dá doze. [p=0.2] {e}Escreva vinte e cinco depois do doze: [p=0.2] {f}mil duzentos e vinte e cinco."),
    dict(id="s16", block="atalho", text="Por que funciona? [p=0.2] Pense em {a}um piso de trinta e cinco por trinta e cinco. [p=0.3] {b}Corte uma faixa de cinco na lateral [p=0.2] e {c}cole em cima. [p=0.3] O piso vira {d}trinta por quarenta: [p=0.2] é o três vezes quatro, com dois zeros. [p=0.2] {e}Dá mil e duzentos. [p=0.3] A ponta da faixa fica de fora: {f}um cantinho de cinco por cinco, com vinte e cinco lajotas. [p=0.3] {g}Juntando, mil duzentos e vinte e cinco."),
    dict(id="s17", block="atalho", text="Com final cinco, o corte deixa {a}dois números redondos: trinta e quarenta. [p=0.3] Com outro final, não. [p=0.2] {b}Trinta e seis ao quadrado viraria trinta por quarenta e dois, mais outro canto. [p=0.2] {c}Aí não compensa: arme a conta."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}Quanto é cinco elevado a quatro? [p=0.3] E uma praça tem {b}quarenta e cinco fileiras de quarenta e cinco lajotas. [p=0.3] {c}Quantas lajotas tem a praça?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] O cinco aparece quatro vezes: {a}vinte e cinco. [p=0.2] {b}Cento e vinte e cinco. [p=0.2] {c}Seiscentos e vinte e cinco. [p=0.3] Vinte seria o erro de sempre."),
    dict(id="s21", block="resposta", text="Na praça, a conta é {a}quarenta e cinco ao quadrado. [p=0.2] {b}Quatro vezes cinco dá vinte. [p=0.2] {c}Vinte e cinco depois do vinte: [p=0.2] {d}dois mil e vinte e cinco lajotas."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}o expoente diz quantas vezes a base aparece na multiplicação, [p=0.2] e {b}a escada monta os quadrados para você."),
    dict(id="s23", block="fim", text="Na próxima aula, a base muda: [p=0.2] {a}negativo, fração e decimal. [p=0.3] E a potência {b}entra na ordem das operações. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
