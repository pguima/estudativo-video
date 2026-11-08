# Estudativo · MAT-ARE-007 — Praticando: perímetros e áreas (Matemática · Áreas e Perímetros · prática).
# Habilidade: escolher a fórmula certa, converter unidades e calcular custo de piso, cerca e pintura.
# Pré-requisitos: MAT-ARE-001, MAT-ARE-002, MAT-ARE-003, MAT-ARE-004, MAT-ARE-005, MAT-ARE-006. Próxima: MAT-ARE-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Preços hipotéticos. √3 ≈ 1,7, como em MAT-ANG-017. Termos de ARE-004/005/006: base maior, base menor, base do meio,
#   metade do lado, á de xis, meia volta.
# Contas: 2.500 cm = 25 m; 2 · (40 + 25) = 130; 130 · 15 = 1.300 + 650 = 1.950. Paralelogramo 12 · 4 = 48 → R$ 480 (erro 12 · 5 · 10 = 600);
#   borda 2 · (12 + 5) = 34. Trapézio (6 + 4) · 3 / 2 = 15 → R$ 750; base do meio 5 · 3 = 15. Hexágono lado 4 (atalho da metade do lado: 2² = 4): 6 · 16√3/4 = 24√3 ≈ 40,8;
#   40,8 / 20 = 2,04 → 3 galões. Cercado: 60 m → x(30 − x), raízes 0 e 30, vértice 15 → 225 m² (20 × 10 = 200).
# Visual:
#   s03-s06: E.retangulo 40 m × 2.500 cm → 25 m (escada de dois degraus); a volta traçada; etiqueta R$ 15/m.
#   s07-s08: 130 × 15 = 130 × 10 + metade (1.300 + 650 = 1.950).
#   s09-s12: E.paralelogramo base 12, lado inclinado 5, altura 4 tracejada; área com a altura (verde), borda com o lado (contorno traçado); 12 · 5 riscado em vermelho.
#   s13-s15: E.trapezio base maior 6, base menor 4, altura 3; no fim, a base do meio 5 e o retângulo 5 × 3.
#   s16-s19: E.regular hexágono de lado 4 dividido em 6 E.triangulo equiláteros; três galões, o terceiro quase cheio (só 0,04 usado).
#   s20-s23: cercados com 60 m de tela: 20 × 10 (200) e 15 × 15 (225); parábola A(x) = x(30 − x) com raízes 0 e 30 e o vértice em 15.

TITULO = "Praticando: perímetros e áreas"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações de obra e reforma, [p=0.2] criadas para esta aula: [p=0.2] {b}cerca, grama, piso, tinta e tela. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.3] O mais difícil nem é a conta: [p=0.2] é {d}escolher a fórmula certa."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar o que viu nesta trilha: [p=0.2] {a}perímetro, a volta inteira; [p=0.2] {b}área de retângulo, de paralelogramo e de triângulo; [p=0.2] {c}de trapézio e de hexágono regular; [p=0.2] e {d}o retângulo de maior área. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: cerca
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um terreno retangular mede {b}quarenta metros por dois mil e quinhentos centímetros. [p=0.3] A cerca custa {c}quinze reais o metro. [p=0.3] {d}Quanto custa cercar o terreno inteiro?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Cerca vai na borda: {a}é perímetro. [p=0.2] Antes, {b}tudo na mesma unidade. [p=0.2] Do centímetro ao metro, dois degraus para cima, duas casas para a esquerda: [p=0.2] {c}dois mil e quinhentos centímetros são vinte e cinco metros."),
    dict(id="s06", block="resposta1", text="Pelo atalho do retângulo, {a}some e dobre. [p=0.2] Quarenta mais vinte e cinco dá sessenta e cinco, [p=0.2] e {b}o dobro dá cento e trinta metros. [p=0.3] {c}Cento e trinta vezes quinze dá mil novecentos e cinquenta reais."),
    # atalho
    dict(id="s07", block="atalho", text="Aqui cabe um atalho para o preço: {a}vezes quinze é vezes dez, mais a metade. [p=0.3] {b}Cento e trinta vezes dez dá mil e trezentos. [p=0.2] {c}A metade de mil e trezentos dá seiscentos e cinquenta. [p=0.2] {d}Mil e trezentos mais seiscentos e cinquenta dá mil novecentos e cinquenta."),
    dict(id="s08", block="atalho", text="Funciona porque {a}quinze é dez mais cinco, e cinco é a metade de dez. [p=0.2] O mesmo vale para {b}vezes cinco: vezes dez e a metade. [p=0.3] {c}Não compensa com preço quebrado, como catorze reais e noventa centavos: [p=0.2] aí, {d}faça a conta armada."),
    # situação 2: grama e borda no paralelogramo
    dict(id="s09", block="questao2", text="{a}Situação dois. [p=0.2] Um canteiro tem forma de {b}paralelogramo, com base de doze metros, [p=0.2] {c}lado inclinado de cinco metros [p=0.2] e {d}altura de quatro metros. [p=0.3] A grama custa {e}dez reais o metro quadrado. [p=0.2] {f}Quanto custa gramar o canteiro? [p=0.2] {g}E quantos metros de borda ele tem?"),
    dict(id="s10", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta2", text="Vamos lá. [p=0.2] Grama cobre a superfície: {a}é área. [p=0.2] No paralelogramo, {b}base vezes altura. [p=0.2] {c}Doze vezes quatro dá quarenta e oito metros quadrados. [p=0.2] {d}Quarenta e oito vezes dez reais dá quatrocentos e oitenta reais."),
    dict(id="s12", block="resposta2", text="A borda é {a}o contorno, e o contorno passa pelo lado inclinado. [p=0.2] Lados opostos são iguais: {b}doze mais cinco dá dezessete, [p=0.2] e {c}o dobro dá trinta e quatro metros. [p=0.3] Repare: {d}na área entra a altura; [p=0.2] {e}no perímetro entra o lado. [p=0.3] Quem faz doze vezes cinco paga {f}seiscentos reais de grama, [p=0.2] cento e vinte a mais."),
    # situação 3: piso no trapézio
    dict(id="s13", block="questao3", text="{a}Situação três. [p=0.2] Uma varanda tem forma de {b}trapézio, [p=0.2] com {c}base maior de seis metros, base menor de quatro metros [p=0.2] e {d}altura de três metros. [p=0.3] O piso custa {e}cinquenta reais o metro quadrado. [p=0.2] {f}Quanto custa o piso da varanda?"),
    dict(id="s14", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta3", text="Vamos lá. [p=0.2] Área do trapézio: {a}base maior mais base menor, vezes a altura, dividido por dois. [p=0.3] {b}Seis mais quatro dá dez. [p=0.2] {c}Dez vezes três dá trinta. [p=0.2] {d}Dividido por dois dá quinze metros quadrados. [p=0.3] {e}Quinze vezes cinquenta dá setecentos e cinquenta reais. [p=0.3] Pela base do meio, {f}seis mais quatro dá dez, e a metade dá cinco, [p=0.2] e cinco vezes três dá os mesmos quinze."),
    # atalho
    # situação 4: tinta no hexágono
    dict(id="s16", block="questao4", text="{a}Situação quatro. [p=0.2] O piso de um quiosque é um {b}hexágono regular de quatro metros de lado. [p=0.3] Cada galão de tinta pinta {c}vinte metros quadrados. [p=0.2] {d}Quantos galões são necessários para pintar o piso? [p=0.2] Use {e}raiz de três perto de um vírgula sete."),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] O hexágono regular se divide em {a}seis triângulos equiláteros de lado quatro. [p=0.3] Área de um equilátero: {b}éle ao quadrado, vezes raiz de três, dividido por quatro. [p=0.2] Pelo atalho da metade do lado, {c}a metade de quatro é dois, e dois ao quadrado dá quatro. [p=0.2] São {d}quatro raiz de três em cada triângulo."),
    dict(id="s19", block="resposta4", text="{a}Seis triângulos dão vinte e quatro raiz de três. [p=0.2] {b}Vinte e quatro vezes um vírgula sete dá quarenta vírgula oito metros quadrados. [p=0.3] {c}Quarenta vírgula oito dividido por vinte dá dois vírgula zero quatro galões. [p=0.3] Com dois galões, {d}falta um pedacinho do piso. [p=0.2] {e}Compre três galões."),
    # situação 5: maior área com a tela
    dict(id="s20", block="questao5", text="{a}Última situação. [p=0.2] Com {b}sessenta metros de tela, uma pessoa quer cercar um galinheiro retangular. [p=0.3] {c}Que medidas dão a maior área possível, e que área é essa?"),
    dict(id="s21", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta5", text="Vamos lá. [p=0.2] A tela é o perímetro, então {a}comprimento mais largura é a meia volta: sessenta dividido por dois dá trinta. [p=0.2] Se um lado é {b}xis, o outro é {c}trinta menos xis. [p=0.3] A área fica {d}á de xis igual a xis vezes trinta menos xis, com o trinta menos xis entre parênteses. [p=0.2] As raízes são {e}zero e trinta: com um lado zero, a área some."),
    dict(id="s23", block="resposta5", text="O vértice fica {a}na média das raízes: [p=0.2] zero mais trinta, dividido por dois, dá quinze. [p=0.2] Quinze metros por quinze metros: {b}um quadrado. [p=0.2] {c}Quinze vezes quinze dá duzentos e vinte e cinco metros quadrados. [p=0.2] É o atalho da aula do retângulo de maior área: {d}sessenta dividido por quatro dá quinze. [p=0.3] Compare com {e}vinte por dez, que gasta a mesma tela [p=0.2] e dá só {f}duzentos."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}borda pede perímetro, [p=0.2] {b}cobertura pede área, [p=0.2] {c}medidas na mesma unidade, [p=0.2] e {d}no fim, veja se a resposta faz sentido na hora de comprar."),
    dict(id="s25", block="fim", text="Na próxima aula, a figura fica redonda: [p=0.2] você vai calcular {a}a área do círculo, [p=0.2] {b}a da coroa, o anel entre dois círculos, [p=0.2] e {c}a do setor, uma fatia do círculo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
