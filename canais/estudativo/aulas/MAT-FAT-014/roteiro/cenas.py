# Estudativo · MAT-FAT-014 — Praticando: equação do 2º grau (Matemática · Fatoração e Equação do 2º Grau · prática).
# Habilidade: resolver equações do 2º grau pelo caminho mais curto e montar a equação a partir de um problema.
# Pré-requisitos: MAT-FAT-007, MAT-FAT-008, MAT-FAT-009, MAT-FAT-010, MAT-FAT-011, MAT-FAT-012, MAT-FAT-013. Próxima: nenhuma na trilha (fecha a trilha; a seguinte no curso é MAT-FUN-001, plano cartesiano).
# Questões inéditas, criadas para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o coeficiente a se fala "á".

TITULO = "Praticando: equação do 2º grau"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões criadas para esta aula. [p=0.2] Todas saem pela fórmula de Bhaskara, [p=0.2] mas quase todas têm {b}um caminho mais curto. [p=0.3] Em cada uma, {c}pause o vídeo e procure esse caminho antes de ver a resposta."),
    # lembrete / mapa
    dict(id="s02", block="mapa", text="Antes de começar, {a}o mapa da escolha. [p=0.2] {b}Faltou um termo? É incompleta: isole o xis ao quadrado ou coloque em evidência. [p=0.2] {c}Á igual a um e números pequenos? Tente soma e produto. [p=0.2] {d}Nada disso? Bhaskara, com o delta primeiro. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] Resolva {b}abre parênteses, xis menos três, fecha parênteses, ao quadrado, igual a dezesseis."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Dá para abrir o quadrado e usar Bhaskara. [p=0.2] Mas olhe de novo: {a}algo ao quadrado dá dezesseis. [p=0.3] Esse algo vale {b}quatro ou menos quatro. [p=0.2] {c}Xis menos três igual a quatro dá sete. [p=0.2] {d}Xis menos três igual a menos quatro dá menos um."),
    dict(id="s06", block="resposta1", text="Conferindo o menos um: {a}menos um menos três, menos quatro, e menos quatro ao quadrado dá dezesseis. [p=0.2] Bateu. [p=0.3] Quem pegou só o quatro {b}perdeu a raiz negativa, como no xis ao quadrado igual a quarenta e nove."),
    # questão 2
    dict(id="s07", block="questao2", text="{a}Questão dois. [p=0.2] Resolva {b}xis ao quadrado menos nove xis mais vinte igual a zero."),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Á vale um, então {a}soma e produto. [p=0.2] {b}Soma nove, produto vinte. [p=0.2] Pares de vinte: {c}um e vinte, dois e dez, quatro e cinco. [p=0.3] {d}Quatro e cinco somam nove. [p=0.2] Raízes: {e}quatro e cinco. [p=0.3] Quem esqueceu de trocar o sinal procurou soma menos nove, [p=0.2] e achou {f}menos quatro e menos cinco, que não servem."),
    # questão 3
    dict(id="s10", block="questao3", text="{a}Questão três. [p=0.2] Resolva {b}dois xis ao quadrado mais quatro xis menos quatro igual a zero."),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Primeiro, {a}tudo é par: divida a equação inteira por dois. [p=0.2] {b}Xis ao quadrado mais dois xis menos dois igual a zero. [p=0.3] Os pares de menos dois não somam menos dois. [p=0.2] {c}Então, Bhaskara. [p=0.2] {d}Delta: quatro mais oito dá doze."),
    dict(id="s13", block="resposta3", text="{a}Doze é quatro vezes três: raiz de doze é dois raiz de três. [p=0.2] {b}Menos dois, mais ou menos dois raiz de três, dividido por dois. [p=0.2] Divida cada parte de cima por dois: [p=0.2] {c}menos um mais raiz de três, ou menos um menos raiz de três. [p=0.3] Quem dividiu {d}só o menos dois [p=0.2] ficou com {e}menos um, mais ou menos dois raiz de três, e errou."),
    # atalho
    dict(id="s14", block="atalho", text="Repare no primeiro passo da questão três: {a}dividir por um fator comum antes de tudo. [p=0.3] Funciona porque {b}zero dividido por dois continua zero, [p=0.2] e as raízes não mudam. [p=0.2] Com números menores, {c}o delta encolhe. [p=0.3] {d}Não compensa quando a divisão cria fração: [p=0.2] aí, use a equação como veio."),
    # questão 4
    dict(id="s15", block="questao4", text="{a}Questão quatro. [p=0.2] Para que valor de ká a equação {b}xis ao quadrado menos dez xis mais ká igual a zero tem raiz dupla? [p=0.3] E {c}qual é essa raiz?"),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Raiz dupla é {a}delta igual a zero. [p=0.2] {b}Cem menos quatro ká igual a zero. [p=0.2] {c}Ká igual a vinte e cinco. [p=0.3] A raiz é {d}menos bê dividido por dois á: dez dividido por dois dá cinco. [p=0.2] Faz sentido: {e}xis ao quadrado menos dez xis mais vinte e cinco é xis menos cinco, ao quadrado."),
    # questão 5
    dict(id="s18", block="questao5", text="{a}Última questão. [p=0.2] Um cercado retangular usa {b}vinte e seis metros de tela no contorno [p=0.2] e tem {c}quarenta metros quadrados de área. [p=0.3] {d}Quais são as medidas do cercado?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] O contorno passa por {a}dois comprimentos e duas larguras. [p=0.2] Então {b}um comprimento mais uma largura é a metade: treze metros. [p=0.3] {c}A largura é xis, e o comprimento, treze menos xis. [p=0.2] Área: {d}xis, vezes o parêntese treze menos xis, igual a quarenta."),
    dict(id="s21", block="resposta5", text="Arrumando e deixando o á positivo: [p=0.2] {a}xis ao quadrado menos treze xis mais quarenta igual a zero. [p=0.2] {b}Soma treze, produto quarenta: cinco e oito. [p=0.3] Aqui, {c}as duas raízes servem, e dão o mesmo cercado: [p=0.2] {d}cinco metros por oito metros. [p=0.2] Conferindo: {e}cinco vezes oito dá quarenta, e cinco mais oito mais cinco mais oito, vinte e seis."),
    dict(id="s22", block="resposta5", text="Repare: o problema já era {a}soma e produto disfarçado. [p=0.2] Dois lados que {b}somam treze e multiplicados dão quarenta."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}olhe a equação antes de calcular, [p=0.2] {b}escolha o caminho mais curto [p=0.2] e {c}passe cada raiz pelo filtro do problema."),
    dict(id="s24", block="fim", text="Com isso, você fecha {a}a trilha de fatoração e equação do segundo grau. [p=0.3] A próxima trilha é {b}funções, [p=0.2] e começa pelo {c}plano cartesiano: marcar e ler pontos num quadriculado, como num mapa. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
