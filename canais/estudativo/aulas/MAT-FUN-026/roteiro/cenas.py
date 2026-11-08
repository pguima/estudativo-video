# Estudativo · MAT-FUN-026 — Custo médio e outras funções racionais (Matemática · Funções · Função racional simples).
# Habilidade: calcular o custo médio C(x)/x = 30 + 2.000/x, dizer que ele se aproxima de 30 sem nunca chegar e dar o domínio de (x + 1)/(x − 2).
# Pré-requisitos: MAT-FUN-005 (domínio pela fórmula: os vilões), MAT-FUN-014 (C(x) = 2.000 + 30x), MAT-FUN-025 (y = k/x nunca toca o eixo). Próxima: MAT-FUN-027.
# Questão inédita, criada para esta aula. A fábrica é a da MAT-FUN-014; a gráfica da questão tem valores inventados.
# Separar a soma: (10 + 6)/2 = 5 + 3 = 8 · (2.000 + 30x)/x = 2.000/x + 30 · x = 1 → 2.030; 100 → 50; 1.000 → 32; 10.000 → 30,2.
# Erro: "cortar o x" só no 30x e manter 2.000 → 2.030 para qualquer x; com 100 peças o certo é 5.000/100 = 50.
# Atalho: custo médio alvo → fixo ÷ (alvo − custo por peça): 2.000 ÷ (40 − 30) = 200; confere 2.000/200 + 30 = 40. Alvo ≤ 30: impossível.
# Domínio: (x + 1)/(x − 2) → x ≠ 2 → ]−∞, 2[ ou ]2, +∞[ (o "ou" da MAT-FUN-005); x = −1 entra: 0/(−3) = 0.
# Questão: C(x) = 600 + 2x · 300 convites → 600/300 + 2 = 4 · alvo 3 → 600 ÷ 1 = 600 convites · (x − 5)/(x + 3) → x ≠ −3.
# Termo novo explicado na hora: assíntota (a reta y = 30 que a curva persegue sem alcançar).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; C se fala "cê"; pares narrados "xis cem, ípsilon cinquenta".
# Visual: lei C(x) = 2.000 + 30x; divisão parcela por parcela; tabela x | custo médio; E.plano (x de 0 a 1.000, y de 0 a 100, escala a confirmar);
#   E.curva de 30 + 2.000/x, reta tracejada y = 30 com o rótulo "assíntota"; pontos (100, 50) e (1.000, 32); reta numérica com furo no 2; resposta da questão em cartões.

TITULO = "Custo médio e outras funções racionais"

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
    dict(id="s01", block="gancho", text="Se a fábrica faz {a}uma peça só, essa peça custa dois mil e trinta reais. [p=0.3] Fazendo {b}mil peças, cada uma sai por trinta e dois. [p=0.3] Quanto mais peças, mais barata cada uma. [p=0.2] Mas existe um preço que ela {c}nunca alcança, nem com um milhão de peças."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o custo médio, descobre esse limite, acha o domínio de outras funções com divisão [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}o custo da fábrica, cê de xis igual a dois mil mais trinta xis; [p=0.2] {b}a hipérbole, cá dividido por xis, que nunca toca o eixo; [p=0.2] e {c}o domínio pela fórmula: embaixo da divisão, diferente de zero. [p=0.3] Se faltar alguma, procure no canal."),
    # custo médio
    dict(id="s04", block="medio", text="O custo de dois mil mais trinta xis é {a}o custo total do mês. [p=0.2] Dois mil de aluguel e máquinas, e trinta reais por peça. [p=0.3] O {b}custo médio é quanto sai cada peça: [p=0.2] {c}o custo total dividido pelo número de peças."),
    dict(id="s05", block="medio", text="Com cem peças, o custo total é {a}dois mil mais três mil, que dá cinco mil reais. [p=0.2] Cinco mil dividido por cem dá {b}cinquenta reais por peça. [p=0.3] Repare que é mais do que os trinta de material. [p=0.2] Cada peça {c}carrega um pedaço do aluguel."),
    # separar
    dict(id="s06", block="separar", text="Agora, a lei do custo médio: {a}dois mil mais trinta xis, tudo dividido por xis. [p=0.3] Para dividir uma soma, {b}divida cada parcela. [p=0.2] Teste com números: {c}dez mais seis, dividido por dois, dá oito. [p=0.2] E {d}dez dividido por dois, mais seis dividido por dois, também dá oito."),
    dict(id="s07", block="separar", text="Então fica {a}dois mil dividido por xis, [p=0.2] mais {b}trinta xis dividido por xis. [p=0.2] Trinta xis dividido por xis é {c}trinta. [p=0.3] O custo médio é {d}trinta, [p=0.2] mais dois mil dividido por xis."),
    # tabela
    dict(id="s08", block="tabela", text="Com essa forma, as contas saem de cabeça. [p=0.2] {a}Uma peça: dois mil mais trinta dá dois mil e trinta reais. [p=0.2] {b}Cem peças: vinte mais trinta dá cinquenta. [p=0.2] {c}Mil peças: dois mais trinta dá trinta e dois. [p=0.2] {d}Dez mil peças: zero vírgula dois mais trinta dá trinta reais e vinte centavos."),
    # limite
    dict(id="s09", block="limite", text="O custo médio chega a trinta? [p=0.2] Para isso, {a}dois mil dividido por xis teria que dar zero. [p=0.2] E essa é a hipérbole da aula passada: [p=0.2] {b}ela chega perto do zero, mas nunca encosta. [p=0.3] Então o custo médio {c}se aproxima de trinta reais, sem nunca chegar."),
    dict(id="s10", block="limite", text="No gráfico, é {a}a mesma hipérbole, levantada trinta unidades. [p=0.2] Ela desce e vai deitando sobre {b}uma reta tracejada na altura trinta. [p=0.3] Essa reta que a curva persegue sem alcançar se chama {c}assíntota. [p=0.3] Na prática, os trinta são o material: [p=0.2] {d}o aluguel se espalha por tantas peças que quase some."),
    # domínio
    dict(id="s11", block="dominio", text="Funções com xis embaixo da divisão se chamam {a}funções racionais. [p=0.2] E o domínio sai pelo vilão que você já conhece. [p=0.3] Veja {b}xis mais um, dividido por xis menos dois, [p=0.2] com cada parte entre parênteses."),
    dict(id="s12", block="dominio", text="O de baixo não pode ser zero: {a}xis menos dois diferente de zero, [p=0.2] {b}xis diferente de dois. [p=0.3] Em intervalo: {c}de menos infinito até dois, [p=0.2] ou {d}de dois até mais infinito, [p=0.2] sempre aberto no dois."),
    dict(id="s13", block="dominio", text="E o de cima pode ser zero, sim. [p=0.2] Em {a}xis igual a menos um, fica zero dividido por menos três: {b}dá zero, um número normal. [p=0.3] Na fábrica, a história também corta: [p=0.2] {c}xis é número de peças, então um, dois, três, e assim por diante."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}cortar o xis só de um lado. [p=0.2] A pessoa risca o xis do trinta xis com o xis de baixo [p=0.2] e escreve {b}dois mil mais trinta, que dá dois mil e trinta, para qualquer quantidade. [p=0.3] Mas com cem peças, você viu: {c}cinco mil dividido por cem dá cinquenta. [p=0.2] A divisão vale {d}para as duas parcelas."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho do alvo, muito cobrado: {a}quantas peças para o custo médio cair a quarenta reais? [p=0.3] Tire o custo por peça: {b}quarenta menos trinta dá dez. [p=0.2] Divida o fixo por esse resto: {c}dois mil dividido por dez dá duzentas peças."),
    dict(id="s16", block="atalho", text="Funciona porque o pedaço do aluguel, {a}dois mil dividido por xis, precisa valer dez. [p=0.2] Conferindo: {b}dois mil dividido por duzentos dá dez. [p=0.2] Mais trinta dá quarenta. [p=0.3] Não compensa quando {c}o alvo é trinta ou menos: [p=0.2] aí não existe resposta, porque o custo médio nunca chega lá."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar, com valores inventados. [p=0.2] Uma gráfica tem {a}custo de seiscentos mais dois xis para fazer xis convites. [p=0.3] {b}Qual é o custo médio de trezentos convites? [p=0.2] {c}Quantos convites para o custo médio cair a três reais? [p=0.2] E, longe da gráfica: {d}qual é o domínio de xis menos cinco, dividido por xis mais três?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O custo médio é {a}dois, [p=0.2] mais seiscentos dividido por xis. [p=0.2] Com trezentos convites: {b}seiscentos dividido por trezentos dá dois. [p=0.2] Mais dois dá quatro reais. [p=0.3] Para três reais, pelo atalho: {c}três menos dois dá um. [p=0.2] Seiscentos dividido por um dá {d}seiscentos convites."),
    dict(id="s20", block="resposta", text="No domínio, só o de baixo importa: {a}xis mais três diferente de zero. [p=0.2] {b}Xis diferente de menos três. [p=0.3] Em intervalo: {c}de menos infinito até menos três, [p=0.2] ou {d}de menos três até mais infinito, [p=0.2] sempre aberto no menos três. [p=0.3] O cinco, que zera o de cima, {e}entra normalmente."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}o custo médio é o custo por peça, [p=0.2] mais o fixo dividido por xis, [p=0.2] e {b}ele se aproxima do custo por peça sem nunca chegar."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica tudo isso: [p=0.2] {a}reconhecer o cá dividido por xis em tabelas e gráficos [p=0.2] e {b}dizer o que acontece quando o xis cresce. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
