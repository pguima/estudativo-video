# Estudativo · MAT-ESP-007 — Prisma: área e volume (Matemática · Geometria Espacial · Prismas e cilindros).
# Habilidade: usar volume = área da base · altura em prismas de base triangular e hexagonal e somar as faces para achar a área total.
# Pré-requisitos: MAT-ESP-006 (área da caixa), MAT-ESP-005 (volume do bloco), MAT-ARE-005 (ℓ²√3/4; hexágono = 6 triângulos; atalho da metade do lado), MAT-ARE-003 (b·h/2). Usa MAT-ANG-015 (Pitágoras) e MAT-ESP-002 (molde). Próxima: MAT-ESP-008.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Prismas retos só.

TITULO = "Prisma: área e volume"

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
    dict(id="s01", block="gancho", text="{a}Uma embalagem de papelão em forma de prisma, deitada. [p=0.2] A ponta é um triângulo de {b}base seis centímetros e altura quatro, [p=0.2] e a embalagem tem {c}dez de comprimento. [p=0.3] Muita gente multiplica tudo: {d}seis vezes quatro vezes dez dá duzentos e quarenta. [p=0.3] É {e}o dobro do certo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o volume e a área de um prisma, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}no bloco, o volume é a área da base vezes a altura; [p=0.2] {c}a área do triângulo é base vezes altura, dividido por dois; [p=0.2] e {d}o hexágono regular se corta em seis triângulos equiláteros. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é prisma
    dict(id="s04", block="prisma", text="{a}Prisma é o sólido com {b}duas bases iguais, uma de frente para a outra, [p=0.2] ligadas por {c}retângulos, as faces laterais. [p=0.3] {d}A altura do prisma é a distância entre as duas bases. [p=0.2] Aqui, as faces laterais ficam em pé, como paredes."),
    dict(id="s05", block="prisma", text="O nome vem da base. [p=0.2] {a}Base triangular, prisma triangular. [p=0.2] {b}Base hexagonal, prisma hexagonal. [p=0.3] E o bloco, a caixa de sapato, é {c}um prisma de base retangular."),
    # volume
    dict(id="s06", block="volume", text="Lembra do bloco? [p=0.2] {a}A área do fundo diz quantos cubinhos cabem {b}na primeira camada. [p=0.2] {c}A altura diz quantas camadas são. [p=0.3] Num prisma qualquer, é igual: [p=0.2] {d}cada camada tem a forma da base."),
    dict(id="s07", block="volume", text="Então a regra do bloco vale para todo prisma: [p=0.2] {a}volume é a área da base vezes a altura. [p=0.3] A diferença é só {b}a forma da base: [p=0.2] {c}triângulo, hexágono, o que for. [p=0.2] Calcule a área dela primeiro."),
    dict(id="s08", block="triangular", text="Na embalagem, {a}a base é o triângulo da ponta. [p=0.2] {b}Seis vezes quatro dá vinte e quatro, [p=0.2] e {c}dividido por dois dá doze centímetros quadrados. [p=0.3] Como ela está deitada, {d}a altura do prisma é a distância de uma ponta à outra: dez. [p=0.2] {e}Doze vezes dez dá cento e vinte centímetros cúbicos."),
    dict(id="s09", block="triangular", text="E os duzentos e quarenta do começo? [p=0.2] São {a}o bloco em volta da embalagem. [p=0.2] Faltou {b}dividir o triângulo por dois, [p=0.2] e o prisma ocupa {c}só metade desse bloco."),
    dict(id="s10", block="hexagonal", text="Agora um prisma hexagonal: [p=0.2] {a}base hexágono regular de lado quatro centímetros [p=0.2] e {b}altura dez. [p=0.3] A base são {c}seis triângulos equiláteros de lado quatro. [p=0.2] Pelo atalho da metade do lado, a área do equilátero é a metade do lado, ao quadrado, vezes raiz de três: [p=0.2] {d}a metade de quatro é dois, e dois ao quadrado dá quatro. [p=0.2] Cada triângulo tem {e}quatro raiz de três."),
    dict(id="s11", block="hexagonal", text="{a}Seis vezes quatro raiz de três dá vinte e quatro raiz de três: [p=0.2] é a área da base. [p=0.3] {b}Vezes dez dá duzentos e quarenta raiz de três centímetros cúbicos. [p=0.3] Com raiz de três perto de um vírgula sete, [p=0.2] {c}são uns quatrocentos e oito."),
    # área total
    dict(id="s12", block="area", text="E a área? [p=0.2] {a}Abra a embalagem, como um molde. [p=0.2] Aparecem {b}os dois triângulos das pontas [p=0.2] e {c}três retângulos, um para cada lado do triângulo. [p=0.3] {d}A área total é a soma de todas as faces."),
    dict(id="s13", block="area", text="O triângulo da ponta tem os lados inclinados iguais, [p=0.2] então a altura cai bem no meio da base. [p=0.3] Cada lado inclinado mede {a}cinco. [p=0.2] Pitágoras confirma, com a metade da base, três, e a altura, quatro: [p=0.2] {b}três ao quadrado mais quatro ao quadrado dá vinte e cinco, [p=0.2] e a raiz de vinte e cinco é cinco."),
    dict(id="s14", block="area", text="{a}Bases: duas vezes doze dá vinte e quatro. [p=0.2] Laterais: {b}cinco vezes dez, [p=0.1] {c}mais cinco vezes dez, [p=0.1] {d}mais seis vezes dez [p=0.2] dá cento e sessenta. [p=0.3] {e}Vinte e quatro mais cento e sessenta dá cento e oitenta e quatro centímetros quadrados de papelão."),
    # erro comum
    dict(id="s15", block="erro", text="O erro mais comum na área é {a}esquecer as bases. [p=0.2] A pessoa soma só os retângulos e para em {b}cento e sessenta. [p=0.3] Mas a embalagem tem {c}duas pontas para fechar. [p=0.2] Prisma tem sempre {d}duas bases: confira se as somou."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho, para a área lateral: [p=0.2] {a}perímetro da base vezes a altura. [p=0.3] {b}Cinco mais cinco mais seis dá dezesseis. [p=0.2] {c}Dezesseis vezes dez dá cento e sessenta. [p=0.2] Uma conta só."),
    dict(id="s17", block="atalho", text="Funciona porque {a}todos os retângulos têm a altura do prisma. [p=0.2] Lado a lado, viram {b}um retângulo só, tão comprido quanto o contorno da base. [p=0.3] {c}Ele não inclui as bases: some as duas no fim. [p=0.2] E {d}não serve direto quando falta uma face lateral, como numa calha aberta em cima: [p=0.2] aí o contorno inclui um lado sem papel. [p=0.2] Tire esse retângulo, ou some só os que existem."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Uma peça de madeira é {a}um prisma hexagonal regular, [p=0.2] com {b}dois centímetros de lado na base [p=0.1] e {c}cinco de altura. [p=0.3] {d}Qual é o volume? [p=0.2] {e}E a área total? [p=0.2] Pode deixar a raiz de três na resposta."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Lado dois: {a}a metade é um, e um ao quadrado dá um. [p=0.2] Cada triângulo tem {b}raiz de três, [p=0.2] e a base tem {c}seis raiz de três. [p=0.3] {d}Vezes cinco dá trinta raiz de três centímetros cúbicos."),
    dict(id="s21", block="resposta", text="Na área, {a}as duas bases dão doze raiz de três. [p=0.2] Pelo atalho, {b}o perímetro é seis vezes dois, que dá doze, [p=0.2] e {c}doze vezes cinco dá sessenta. [p=0.3] Área total: {d}sessenta mais doze raiz de três centímetros quadrados, [p=0.2] perto de {e}oitenta."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}volume, área da base vezes altura. [p=0.2] {b}Área total, as duas bases mais as faces laterais."),
    dict(id="s23", block="fim", text="Na próxima aula, a base fica redonda: [p=0.2] {a}o cilindro. [p=0.2] Você calcula quanto cabe numa lata de {b}raio cinco e altura dez [p=0.2] e quanto metal ela gasta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
