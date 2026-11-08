# Estudativo · MAT-CON-009 — Praticando: conjuntos e números reais (Matemática · Conjuntos · prática).
# Habilidade: resolver problemas com diagrama de Venn, classificar números, achar frações geratrizes e escrever respostas em intervalos.
# Pré-requisitos: MAT-CON-001 a MAT-CON-008. Próxima: fim da trilha; na playlist Matemática do Zero, segue MAT-FAT-001 (produtos notáveis).
# Questões inéditas, criadas para esta aula.
# 1) 80 pessoas; filmes 45, música 38, ambos 12 → só filmes 33, só música 26, união 71 (= 45 + 38 − 12), nenhum 9.
# 2) √36 = 6 ∈ ℕ · −5 ∈ ℤ, ∉ ℕ · 7/4 = 1,75 ∈ ℚ, ∉ ℤ · √3 irracional · todos em ℝ.
# 3) 0,2777… = (27 − 2)/90 = 25/90 = 5/18; equação: 100x = 27,777…, 10x = 2,777…, 90x = 25; 5 ÷ 18 = 0,2777…
# 4) 5 − 2x ≥ −3 → −2x ≥ −8 → x ≤ 4 → ]−∞, 4]; teste do zero: 5 ≥ −3 e 0 ≤ 4.
# 5) ]−∞, 4] ∩ ]1, 6[ = ]1, 4] (1 ∉ ]1, 6[; 4 ∈ ambos) · ]−∞, 4] ∪ ]1, 6[ = ]−∞, 6[ (6 em nenhum).
# Visual: Venn de 2 conjuntos (E.venn); quadro de classificação ℕ, ℤ, ℚ, irracional; retas empilhadas com intervalos (E.reta + E.intervalo).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: conjuntos e números reais"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, criadas para esta aula, [p=0.2] com tudo da trilha de conjuntos e números reais. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}o diagrama de Venn, de dentro para fora, [p=0.2] {b}a escada dos conjuntos de números, [p=0.2] {c}a fração geratriz [p=0.2] e {d}os intervalos na reta. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: Venn
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Numa pesquisa com {b}oitenta pessoas, [p=0.2] {c}quarenta e cinco assinam um serviço de filmes, [p=0.2] {d}trinta e oito assinam um de música [p=0.2] e {e}doze assinam ambos. [p=0.3] {f}Quantas não assinam nenhum? [p=0.2] E {g}quantas assinam só o de filmes?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá, de dentro para fora. [p=0.2] {a}Doze no meio. [p=0.2] {b}Só filmes: quarenta e cinco menos doze dá trinta e três. [p=0.2] {c}Só música: trinta e oito menos doze dá vinte e seis. [p=0.3] {d}Doze mais trinta e três mais vinte e seis dá setenta e um. [p=0.2] {e}Oitenta menos setenta e um: nove pessoas não assinam nenhum."),
    dict(id="s06", block="resposta1", text="Pela fórmula, o mesmo: [p=0.2] {a}quarenta e cinco mais trinta e oito dá oitenta e três, [p=0.2] {b}menos os doze contados duas vezes, setenta e um. [p=0.3] E a segunda pergunta já saiu no caminho: [p=0.2] {c}trinta e três assinam só o de filmes."),
    # situação 2: classificar
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Olhe estes números: [p=0.2] {b}raiz de trinta e seis, [p=0.2] {c}menos cinco, [p=0.2] {d}sete quartos [p=0.2] e {e}raiz de três. [p=0.3] {f}Qual é natural? [p=0.2] Qual é inteiro, mas não natural? [p=0.2] Qual é racional, mas não inteiro? [p=0.2] E qual é irracional?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá, subindo a escada. [p=0.2] {a}Raiz de trinta e seis é seis: natural. [p=0.3] {b}Menos cinco não conta objetos, mas é inteiro. [p=0.3] {c}Sete quartos é um vírgula setenta e cinco: [p=0.2] não é inteiro, mas é fração, então é racional."),
    dict(id="s10", block="resposta2", text="{a}Três fica entre um e quatro: não é o quadrado de nenhum natural, [p=0.2] então {b}raiz de três é irracional. [p=0.3] E repare: {c}os quatro números são reais. [p=0.2] Todos têm o seu ponto na reta."),
    # situação 3: geratriz
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Qual é a fração geratriz de {b}zero vírgula dois sete sete sete, sem fim, [p=0.2] {c}na forma mais simples?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Primeiro, olhe {a}o que fica fora do período. [p=0.2] O dois aparece uma vez só, e {b}o período é o sete. [p=0.3] {c}Em cima: vinte e sete menos dois dá vinte e cinco. [p=0.2] {d}Embaixo: um nove pelo período e um zero pelo dois, noventa."),
    dict(id="s14", block="resposta3", text="{a}Vinte e cinco noventa avos. [p=0.2] Divida em cima e embaixo por cinco: {b}cinco dezoito avos. [p=0.3] Pela equação, dá o mesmo: [p=0.2] {c}cem xis menos dez xis dá noventa xis, [p=0.2] igual a vinte e sete vírgula sete sete sete menos dois vírgula sete sete sete dá [p=0.2] {d}vinte e cinco."),
    dict(id="s15", block="resposta3", text="Quem usa o macete simples escreve {a}vinte e sete noventa e nove avos, [p=0.2] que é {b}zero vírgula dois sete dois sete. [p=0.2] Outro número. [p=0.3] Na dízima, {c}olhe primeiro o que fica fora do período."),
    # situação 4: inequação e intervalo
    dict(id="s16", block="questao4", text="{a}Situação quatro. [p=0.2] Resolva {b}cinco menos dois xis, maior ou igual a menos três, [p=0.2] e {c}escreva a resposta como intervalo."),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] {a}Tire cinco de cada lado: menos dois xis maior ou igual a menos oito. [p=0.3] {b}Divida por menos dois. [p=0.2] É negativo, então {c}vira o sinal: [p=0.2] {d}xis menor ou igual a quatro."),
    dict(id="s19", block="resposta4", text="Tem tracinho: {a}fechado no quatro. [p=0.2] Vai para a esquerda, sem fim: [p=0.2] {b}de menos infinito até quatro, aberto no infinito. [p=0.3] Teste o zero: {c}cinco menos zero dá cinco, que é maior que menos três. [p=0.2] E o zero {d}está mesmo na resposta. [p=0.2] Bateu."),
    # situação 5: interseção e união
    dict(id="s20", block="questao5", text="{a}Última situação, e ela junta tudo. [p=0.2] Pegue {b}a resposta da situação quatro [p=0.2] e {c}o intervalo aberto de um a seis. [p=0.3] {d}Ache a interseção e a união."),
    dict(id="s21", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta5", text="Vamos lá, empilhando as retas. [p=0.2] Interseção: {a}o maior dos começos é o um. [p=0.2] {b}O menor dos fins é o quatro. [p=0.3] Falta conferir as pontas. [p=0.2] {c}O um está na reta de cima, mas na de baixo a bolinha é aberta: fica de fora. [p=0.2] {d}O quatro está em ambas: entra."),
    dict(id="s23", block="resposta5", text="Interseção: {a}aberto no um e fechado no quatro. [p=0.3] Na união, o pintado vai {b}de menos infinito até o seis. [p=0.2] {c}O seis não está em nenhuma: aberto. [p=0.3] União: {d}de menos infinito até seis, aberto nas pontas."),
    # atalho
    dict(id="s24", block="atalho", text="Daqui sai um atalho de prova: {a}teste um número em cada resposta. [p=0.3] O dois, por exemplo, está em ambas as retas. [p=0.2] Então {b}ele tem que estar na interseção, e está. [p=0.3] Funciona porque a resposta é {c}o grupo de números que servem. [p=0.2] Não compensa para decidir as pontas: [p=0.2] ali, {d}confira na pilha, uma por uma."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: {a}no diagrama, de dentro para fora. [p=0.2] {b}Para classificar, suba a escada. [p=0.2] {c}Na dízima, olhe o que fica fora do período. [p=0.2] E {d}nas pontas dos intervalos, confira uma por uma."),
    dict(id="s26", block="fim", text="Com isso, você fecha a trilha de conjuntos e números reais. [p=0.3] A próxima trilha do curso abre os {a}produtos notáveis: [p=0.2] {b}abrir xis mais três, ao quadrado, sem multiplicar tudo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
