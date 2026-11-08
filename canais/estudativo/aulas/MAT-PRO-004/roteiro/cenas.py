# Estudativo · MAT-PRO-004 — Progressão aritmética: razão e termo geral (Matemática · Progressões · Sequências e PA).
# Habilidade: achar a razão de 5, 9, 13, …, calcular o 20º termo com aₙ = a₁ + (n − 1)r = 81 e ver a PA como uma função afim.
# Pré-requisitos: MAT-PRO-001 (posição e termo, aₙ), MAT-FUN-009 (função afim: f(x) = ax + b, reta), MAT-EQU-009 (equação com parênteses). Próxima: MAT-PRO-005.
# Questão inédita, criada para esta aula. Letras narradas: "á um", "á ene", "erre", "xis", "bê"; PA = "pê á". Termos como na MAT-PRO-001: posição, termo, lei de formação.
# Coeficientes e taxa de variação (MAT-FUN-010) fora da ficha: o "á" da função afim é dito só como "o número que multiplica".
# Contas: razão 9 − 5 = 4 · a₂₀ = 5 + 19 · 4 = 5 + 76 = 81 · a₃ = 5 + 2 · 4 = 13 · lei 5 + 4(n − 1) = 4n + 1.
# Razão negativa: 20, 17, 14 (r = −3). Erro: 5 + 20 · 4 = 85; no 1º termo daria 5 + 1 · 4 = 9 ≠ 5.
# Atalho: de a₃ = 13 ao a₂₀: 17 saltos · 17 · 4 = 68 · 13 + 68 = 81.
# Questão: 7, 12, 17 · r = 5 · a₃₀ = 7 + 29 · 5 = 152 · lei 5n + 2 (5 · 30 + 2 = 152).
# Visual: lista 5, 9, 13, 17 com "+4" em arco entre os termos; fórmula aₙ = a₁ + (n − 1) · r (E.formula) com cada letra
#   apontada; plano (E.plano) com pontos (1, 5), (2, 9), (3, 13), (4, 17) (E.ponto) e a reta y = 4x + 1 tracejada por baixo
#   (E.curva, tracejada=True), para mostrar "pontos soltos em cima de uma reta".
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Progressão aritmética: razão e termo geral"

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
    dict(id="s01", block="gancho", text="{a}Cinco, [p=0.1] nove, [p=0.1] treze, [p=0.1] dezessete. [p=0.3] Qual é o {b}vigésimo termo? [p=0.3] Dá para escrever a lista inteira até lá. [p=0.2] Ou fazer {c}uma conta só, e chegar em {d}oitenta e um."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a razão e calcula qualquer termo com uma fórmula. [p=0.2] Vai descobrir que essa lista é {b}uma velha conhecida. [p=0.2] E ainda leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}posição e termo, como em á índice ene, [p=0.2] {b}a função afim, que vira uma reta, [p=0.2] e {c}equação com parênteses. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é PA
    dict(id="s04", block="pa", text="Repare na lista: {a}de um termo para o próximo, sempre soma quatro. [p=0.3] Sequência que anda {b}somando sempre o mesmo número se chama {c}progressão aritmética, ou pê á."),
    dict(id="s05", block="pa", text="O número que se soma é {a}a razão, e a letra dela é {b}erre. [p=0.3] Para achar, {c}faça um termo menos o anterior: [p=0.2] nove menos cinco dá quatro. [p=0.2] {d}Confira com outro par: treze menos nove também dá quatro. [p=0.3] {e}A razão é quatro."),
    dict(id="s06", block="pa", text="A razão também pode ser negativa. [p=0.2] Em {a}vinte, [p=0.1] dezessete, [p=0.1] catorze, [p=0.2] a lista desce: {b}a razão é menos três. [p=0.3] E com razão zero, {c}o número só se repete."),
    # termo geral
    dict(id="s07", block="saltos", text="Agora, o vigésimo termo. [p=0.2] Saindo do primeiro, quantas vezes você soma quatro? [p=0.3] {a}Para chegar no segundo, uma vez. [p=0.2] {b}No terceiro, duas. [p=0.2] No vigésimo, {c}dezenove vezes. [p=0.3] {d}Os saltos são sempre um a menos que a posição."),
    dict(id="s08", block="formula", text="Isso vira {a}a fórmula do termo geral: [p=0.2] {b}á índice ene igual a á índice um, mais, abre parênteses, ene menos um, fecha parênteses, vezes erre. [p=0.3] {c}Á índice um é o primeiro termo. [p=0.1] {d}Ene é a posição que você quer. [p=0.1] {e}Ene menos um é o número de saltos. [p=0.1] {f}Erre é a razão."),
    dict(id="s09", block="formula", text="Para o vigésimo: {a}á índice vinte igual a cinco mais dezenove vezes quatro. [p=0.2] {b}Dezenove vezes quatro dá setenta e seis. [p=0.2] {c}Mais cinco dá oitenta e um. [p=0.3] Teste a fórmula num termo que você enxerga: [p=0.2] {d}á índice três é cinco mais duas vezes quatro, que dá treze. [p=0.2] Bateu."),
    # PA como função afim
    dict(id="s10", block="afim", text="Agora, a velha conhecida. [p=0.2] Faça a distributiva na fórmula: [p=0.2] {a}cinco, mais quatro ene, menos quatro. [p=0.2] Junte os números soltos: {b}á índice ene igual a quatro ene mais um. [p=0.3] É uma {c}função afim, com o ene no papel do xis. [p=0.2] {d}O número que multiplica o ene é a razão, quatro. [p=0.2] {e}O número sozinho é o termo que viria antes do cinco: cinco menos quatro dá um."),
    dict(id="s11", block="afim", text="No plano, marque {a}posição um, termo cinco. [p=0.2] {b}Posição dois, termo nove. [p=0.2] {c}Posição três, termo treze. [p=0.3] Os pontos ficam {d}alinhados, como na função afim. [p=0.3] Só que não existe posição um e meio. [p=0.2] O gráfico de uma pê á são {e}pontos separados, todos em cima de uma reta."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}usar o ene no lugar de ene menos um. [p=0.2] A pessoa faz {b}cinco mais vinte vezes quatro, [p=0.2] e responde {c}oitenta e cinco."),
    dict(id="s13", block="erro", text="Teste essa conta no primeiro termo: [p=0.2] {a}cinco mais uma vez quatro dá nove. [p=0.2] Mas o primeiro termo é cinco! [p=0.3] {b}O primeiro termo não tem salto nenhum. [p=0.2] Por isso, {c}ene menos um."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}pule de qualquer termo que você conhece. [p=0.3] Se você já sabe que {b}á índice três é treze, [p=0.2] do terceiro ao vigésimo são {c}dezessete saltos. [p=0.2] {d}Dezessete vezes quatro dá sessenta e oito. [p=0.2] {e}Treze mais sessenta e oito dá oitenta e um."),
    dict(id="s15", block="atalho", text="Funciona porque {a}cada salto vale uma razão, não importa de onde você parte. [p=0.2] Os saltos são {b}a posição de chegada menos a de partida. [p=0.3] Brilha quando a questão dá {c}um termo solto, como o décimo. [p=0.2] Não compensa quando ela já dá o primeiro: [p=0.2] {d}aí, a fórmula é a mesma conta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma pessoa guarda {a}sete reais na primeira semana, [p=0.1] {b}doze na segunda, [p=0.1] {c}dezessete na terceira, e assim por diante. [p=0.3] {d}Qual é a razão? [p=0.2] {e}Quanto ela guarda na trigésima semana? [p=0.2] E {f}como fica a lei, na forma de função afim?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Doze menos sete dá cinco: a razão é cinco. [p=0.3] Trigésima semana: {b}vinte e nove saltos. [p=0.2] {c}Vinte e nove vezes cinco dá cento e quarenta e cinco. [p=0.2] {d}Mais sete dá cento e cinquenta e dois reais."),
    dict(id="s19", block="resposta", text="A lei: {a}sete, mais cinco ene, menos cinco. [p=0.2] {b}Á índice ene igual a cinco ene mais dois. [p=0.3] Confira: {c}cinco vezes trinta dá cento e cinquenta, e mais dois dá cento e cinquenta e dois. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}na pê á, a razão é um termo menos o anterior. [p=0.2] {b}Até a posição ene, são ene menos um saltos. [p=0.2] E {c}a pê á é uma função afim, vista só nas posições."),
    dict(id="s21", block="fim", text="Na próxima aula, os atalhos da pê á: [p=0.2] {a}o termo do meio de dois, xis, dez, sem fórmula, [p=0.2] {b}três termos escritos com uma letra só [p=0.2] e {c}quantos números de três algarismos são múltiplos de sete. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
