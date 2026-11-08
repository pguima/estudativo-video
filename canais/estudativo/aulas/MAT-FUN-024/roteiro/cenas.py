# Estudativo · MAT-FUN-024 — Praticando: função quadrática (Matemática · Funções · Função quadrática · prática).
# Habilidade: achar raízes e vértice, montar a função de um problema e decidir entre máximo, mínimo e sinal.
# Pré-requisitos: MAT-FUN-016 a MAT-FUN-023 e MAT-FUN-028. Próxima: MAT-FUN-025.
# Questões inéditas, criadas para esta aula. Métodos e termos das aulas da trilha: boca (sinal do á), média das raízes,
#   −b/2a, "o xis diz quando, o ípsilon diz quanto" (MAT-FUN-019), anotar o que é o xis e atalho dos parênteses (MAT-FUN-020),
#   fora das raízes o sinal do á, entre elas o contrário (MAT-FUN-022). Lei da parábola (021) e quadro de sinais (023) não entram.
# Q1: f(x) = x² − 8x + 12 · Δ = 64 − 48 = 16 · x = (8 ± 4)/2 → 6 e 2 · xv = 4 · f(4) = 16 − 32 + 12 = −4 · mínimo · imagem [−4, +∞[.
# Q2: h(t) = −5t² + 30t · raízes 0 e −b/a = 6 · topo em 3 s · h(3) = −45 + 90 = 45 m · no ar 6 s.
# Q3: marmita a R$ 20, 200 por dia, cada R$ 1 de aumento perde 5 · x = reais de aumento · R(x) = (20 + x)(200 − 5x) ·
#   zeros −20 e 40 · média 10 · preço 30 · 150 marmitas · R = 4.500 (antes: 4.000) · erro: responder 10 (o aumento).
# Q4: L(x) = −x² + 12x − 20 (mil reais; x em toneladas) · Δ = 144 − 80 = 64 · x = (−12 ± 8)/(−2) → 2 e 10 · á negativo:
#   entre as raízes, positivo → ]2, 10[ · xv = 6 · L(6) = −36 + 72 − 20 = 16 mil reais.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á"; h, R e L se falam "agá", "erre" e "ele".
# Visual: E.plano com E.curva de x² − 8x + 12 (x de 1 a 7), E.ponto em (2, 0), (6, 0), (4, −4), sombra da imagem no eixo y;
#   E.curva de −5t² + 30t (t de 0 a 6), E.ponto em (3, 45) com setas "quando?" e "quanto?"; quadro preço × quantidade com x anotado;
#   E.curva de −x² + 12x − 20 com E.area verde entre 2 e 10 acima do eixo e E.ponto no vértice (6, 16).

TITULO = "Praticando: função quadrática"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, criadas para esta aula, com o principal da parábola. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}as raízes, com delta e Bhaskara; [p=0.2] {b}o vértice, pela média das raízes ou por menos bê dividido por dois á; [p=0.2] {c}o sinal do á, que diz a boca; [p=0.2] e {d}o estudo do sinal. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: raízes, vértice e imagem
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Para {b}efe de xis igual a xis ao quadrado menos oito xis mais doze: [p=0.3] {c}ache as raízes e o vértice. [p=0.2] O vértice é máximo ou mínimo? [p=0.2] E qual é a imagem?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Delta: {a}bê ao quadrado dá sessenta e quatro, [p=0.2] e quatro vezes á vezes cê dá quarenta e oito. [p=0.2] Sessenta e quatro menos quarenta e oito dá dezesseis. [p=0.2] A raiz de dezesseis é quatro. [p=0.2] Xis é igual a oito, mais ou menos quatro, dividido por dois, dá {b}seis ou dois."),
    dict(id="s06", block="resposta1", text="O xis do vértice é {a}a média das raízes: dois mais seis dá oito, [p=0.2] e oito dividido por dois dá quatro. [p=0.2] O ípsilon: {b}dezesseis menos trinta e dois mais doze dá menos quatro. [p=0.3] Vértice em {c}xis quatro, ípsilon menos quatro. [p=0.2] Á positivo, a boca abre para cima: {d}é o mínimo. [p=0.3] A imagem vai {e}de menos quatro até mais infinito, fechado no menos quatro."),
    # situação 2: altura máxima
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma bola é lançada do chão para cima. [p=0.2] {b}A altura dela, em metros, é agá de tê igual a menos cinco tê ao quadrado mais trinta tê, [p=0.2] com tê em segundos. [p=0.3] {c}Qual é a altura máxima? [p=0.2] E {d}quanto tempo a bola fica no ar?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá, pelo atalho da bola. [p=0.2] Sem cê, {a}uma raiz é zero, [p=0.2] e a outra é {b}menos bê dividido por á: menos trinta dividido por menos cinco dá seis. [p=0.3] A bola sai do chão no zero e volta {c}aos seis segundos. [p=0.2] Esse é o tempo no ar."),
    dict(id="s10", block="resposta2", text="O topo fica no meio: {a}três segundos. [p=0.2] Mas a pergunta é a altura, então calcule {b}agá de três. [p=0.2] Três ao quadrado é nove, vezes menos cinco dá {c}menos quarenta e cinco. [p=0.2] Mais noventa dá {d}quarenta e cinco metros. [p=0.3] Quem respondeu três {e}parou no xis do vértice: respondeu quando, não quanto."),
    # situação 3: montar a função
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Um restaurante vende {b}duzentas marmitas por dia, a vinte reais cada. [p=0.2] Ele descobre que {c}cada real de aumento faz perder cinco marmitas. [p=0.3] {d}Qual preço dá a maior receita? [p=0.2] E de quanto é essa receita?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] {a}Xis é quantos reais de aumento. [p=0.2] Anote isso ao lado do xis. [p=0.3] {b}O preço fica vinte mais xis. [p=0.2] {c}As marmitas ficam duzentas menos cinco xis. [p=0.2] Receita é preço vezes quantidade: {d}erre de xis igual ao parêntese vinte mais xis, vezes o parêntese duzentos menos cinco xis."),
    dict(id="s14", block="resposta3", text="Atalho: não abra os parênteses. [p=0.2] {a}Vinte mais xis zera em menos vinte. [p=0.2] {b}Duzentos menos cinco xis zera em quarenta. [p=0.2] O meio: {c}menos vinte mais quarenta dá vinte, [p=0.2] e vinte dividido por dois dá dez. [p=0.3] O melhor aumento é de dez reais."),
    dict(id="s15", block="resposta3", text="Mas a pergunta é {a}o preço. [p=0.2] Vinte mais dez dá {b}trinta reais. [p=0.2] Vende {c}cento e cinquenta marmitas, [p=0.2] e a receita é {d}trinta vezes cento e cinquenta, que dá quatro mil e quinhentos reais. [p=0.3] Antes, eram quatro mil. [p=0.2] Quem respondeu dez reais {e}deu o aumento, não o preço."),
    # situação 4: sinal e máximo
    dict(id="s16", block="questao4", text="{a}Última situação, e ela junta máximo e sinal. [p=0.2] Uma fábrica produz xis toneladas por mês. [p=0.2] {b}O lucro, em mil reais, é ele de xis igual a menos xis ao quadrado mais doze xis menos vinte. [p=0.3] {c}Para quais produções há lucro? [p=0.2] E {d}qual produção dá o maior lucro?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] Ter lucro é {a}ele de xis maior que zero: é estudo do sinal. [p=0.2] Delta: bê ao quadrado dá cento e quarenta e quatro. [p=0.2] E quatro vezes á vezes cê é quatro vezes menos um vezes menos vinte, que dá {b}oitenta positivo, porque menos com menos dá mais. [p=0.2] Cento e quarenta e quatro menos oitenta dá sessenta e quatro. [p=0.2] A raiz é oito. [p=0.2] Xis é igual a menos doze, mais ou menos oito, dividido por menos dois, dá {c}dois ou dez."),
    dict(id="s19", block="resposta4", text="Á negativo, a boca abre para baixo. [p=0.2] {a}Entre as raízes, o sinal é o contrário do á: positivo. [p=0.2] Há lucro {b}entre duas e dez toneladas, sem as pontas, [p=0.2] porque nelas o lucro é zero: {c}o intervalo aberto de dois a dez."),
    dict(id="s20", block="resposta4", text="E o maior lucro fica {a}no meio das raízes: seis toneladas. [p=0.2] {b}Ele de seis: menos trinta e seis mais setenta e dois menos vinte. [p=0.2] Dá {c}dezesseis, ou seja, dezesseis mil reais. [p=0.3] A pergunta pedia a produção: {d}seis toneladas."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}o sinal do á decide a boca, [p=0.2] {b}o vértice responde máximo e mínimo [p=0.2] e {c}as raízes separam os sinais. [p=0.3] E sempre {d}releia o que a pergunta pede."),
    dict(id="s22", block="fim", text="Na próxima aula, uma curva nova: {a}a hipérbole, de ípsilon igual a doze dividido por xis. [p=0.2] Nela, {b}xis vezes ípsilon dá sempre doze, [p=0.2] e o gráfico mostra {c}grandezas inversamente proporcionais. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
