# Estudativo · MAT-FUN-027 — Praticando: função racional simples (Matemática · Funções · Função racional simples · prática).
# Habilidade: reconhecer relações do tipo y = k/x em tabelas e gráficos e interpretar o que acontece quando x cresce.
# Pré-requisitos: MAT-FUN-025 (y = k/x, x · y = k, um ponto dá a lei), MAT-FUN-026 (custo médio, assíntota, atalho do alvo). Próxima: nenhuma na trilha; fecha Funções e aponta MAT-ANG-001 (próxima da playlist Matemática do Zero).
# Questões inéditas, criadas para esta aula. Teste do dobro (MAT-RAZ-005) fora da ficha: não usado.
# Q1: conta dividida 2→180, 3→120, 4→90, 5→72 · produtos 360 · y = 360/x · 6 pessoas → 60.
# Q2: tabela A 2→30, 3→20, 5→12, 6→10 (produto 60, é k/x) · tabela B 1→30, 2→15, 3→10, 4→6 (30, 30, 30, 24: não é; só a última linha denuncia). Narradas "tabela á" e "tabela bê".
# Q3: hipérbole por (2, 9), (3, 6) e (6, 3) · 18, 18 e 18 · y = 18/x · x = 9 → 2 · x = 180 → 0,1 · y nunca chega a zero.
# Q4: curso online C(x) = 4.000 + 10x · custo médio 10 + 4.000/x · 200 alunos → 20 + 10 = 30 · alvo 15 → 4.000 ÷ 5 = 800 · nunca chega a 10.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; pares narrados "xis dois, ípsilon nove"; k se fala "cá".
# Visual: tabelas de duas colunas com a coluna "x · y" aparecendo; tabela B com o 24 da última linha em vermelho; E.plano com E.curva de 18/x e E.ponto em (2, 9), (3, 6), (6, 3), (9, 2);
#   seta ao longo da curva para a direita, colando no eixo x; curva 10 + 4.000/x com assíntota tracejada em y = 10; cortina final para Geometria Plana.

TITULO = "Praticando: função racional simples"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, criadas para esta aula, para fechar a trilha de funções. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar três ferramentas: [p=0.2] {a}em ípsilon igual a cá dividido por xis, xis vezes ípsilon é sempre cá; [p=0.2] {b}um ponto basta para achar o cá; [p=0.2] e {c}o custo médio, que se aproxima do custo por peça sem nunca chegar. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: tabela de conta dividida
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um grupo divide igualmente a conta de um churrasco. [p=0.2] Com {b}duas pessoas, cada uma paga cento e oitenta reais. [p=0.2] Com {c}três, cento e vinte. [p=0.2] Com {d}quatro, noventa. [p=0.2] Com {e}cinco, setenta e dois. [p=0.3] {f}Qual é a lei? [p=0.2] E quanto cada um paga se forem seis?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Multiplique cada linha. [p=0.2] {a}Dois vezes cento e oitenta dá trezentos e sessenta. [p=0.2] {b}Três vezes cento e vinte, também. [p=0.2] {c}Quatro vezes noventa, também. [p=0.2] {d}Cinco vezes setenta e dois, também. [p=0.3] O cá é trezentos e sessenta, e ele tem significado: {e}é o valor da conta inteira."),
    dict(id="s06", block="resposta1", text="A lei é {a}ípsilon igual a trezentos e sessenta dividido por xis. [p=0.2] Com seis pessoas: {b}trezentos e sessenta dividido por seis dá sessenta reais."),
    # situação 2: qual tabela é k/x
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Duas tabelas, e nas duas o ípsilon desce. [p=0.3] Na {b}tabela á: xis dois, ípsilon trinta; [p=0.1] xis três, ípsilon vinte; [p=0.1] xis cinco, ípsilon doze; [p=0.1] xis seis, ípsilon dez. [p=0.3] Na {c}tabela bê: xis um, ípsilon trinta; [p=0.1] xis dois, ípsilon quinze; [p=0.1] xis três, ípsilon dez; [p=0.1] xis quatro, ípsilon seis. [p=0.3] {d}Qual delas é do tipo cá dividido por xis?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Na tabela á, multiplique: {a}dois vezes trinta dá sessenta. [p=0.1] Três vezes vinte, também. [p=0.1] Cinco vezes doze, também. [p=0.1] Seis vezes dez, também. [p=0.2] {b}É do tipo cá dividido por xis, com cá igual a sessenta."),
    dict(id="s10", block="resposta2", text="Na tabela bê, cuidado. [p=0.2] As primeiras linhas enganam: {a}um vezes trinta dá trinta, [p=0.2] dois vezes quinze também, [p=0.2] e três vezes dez também. [p=0.3] Mas a última é {b}quatro vezes seis, que dá {c}vinte e quatro. [p=0.3] {d}Produtos diferentes: não é. [p=0.2] Esse é o erro mais comum: {e}conferir duas ou três linhas e parar. [p=0.2] Confira todas."),
    # situação 3: gráfico
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Um gráfico em forma de hipérbole passa pelos pontos {b}xis dois, ípsilon nove; [p=0.1] {c}xis três, ípsilon seis; [p=0.1] e {d}xis seis, ípsilon três. [p=0.3] {e}É do tipo cá dividido por xis? [p=0.2] Quanto vale o ípsilon {f}em xis nove? [p=0.2] E o que acontece com o ípsilon {g}quando o xis cresce sem parar?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] {a}Dois vezes nove dá dezoito. [p=0.2] {b}Três vezes seis, também dezoito. [p=0.2] {c}Seis vezes três, também. [p=0.3] Todos os produtos batem: é do tipo cá dividido por xis, {d}ípsilon igual a dezoito dividido por xis. [p=0.2] Em xis nove: {e}dezoito dividido por nove dá dois."),
    dict(id="s14", block="resposta3", text="Quando o xis cresce, o ípsilon {a}fica cada vez menor. [p=0.2] Em xis cento e oitenta, por exemplo, {b}dá zero vírgula um. [p=0.3] A curva {c}vai colando no eixo xis, [p=0.2] mas {d}nunca chega a zero: [p=0.2] o produto precisa continuar valendo dezoito."),
    # atalho
    dict(id="s15", block="atalho", text="Aqui cabe um atalho para eliminar alternativas: {a}a hipérbole nunca toca os eixos. [p=0.2] Gráfico que corta o eixo xis ou o eixo ípsilon {b}não é do tipo cá dividido por xis, sem conta. [p=0.3] Funciona porque, num eixo, uma das coordenadas é zero, e o produto daria zero. [p=0.2] Não compensa quando a curva {c}não toca os eixos: [p=0.2] aí, {d}multiplique as coordenadas para conferir."),
    # situação 4: custo médio
    dict(id="s16", block="questao4", text="{a}Última situação. [p=0.2] Um curso online gasta {b}quatro mil reais por mês com a plataforma, [p=0.1] mais {c}dez reais por aluno. [p=0.3] {d}Qual é o custo médio por aluno com duzentos alunos? [p=0.2] Com quantos alunos ele cai a quinze reais? [p=0.2] E ele pode chegar a dez?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] O custo médio é {a}dez, [p=0.2] mais quatro mil dividido por xis. [p=0.2] Com duzentos alunos: {b}quatro mil dividido por duzentos dá vinte. [p=0.2] Mais dez dá {c}trinta reais por aluno."),
    dict(id="s19", block="resposta4", text="Para quinze reais, pelo atalho do alvo: {a}quinze menos dez dá cinco. [p=0.2] {b}Quatro mil dividido por cinco dá oitocentos alunos. [p=0.3] E dez reais, {c}nunca. [p=0.2] Quatro mil dividido por xis {d}nunca vira zero. [p=0.2] O custo médio só {e}se aproxima de dez, conforme os alunos aumentam."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}multiplique as coordenadas, todas, [p=0.2] e lembre que, {b}quando o xis cresce, cá dividido por xis encolhe sem chegar a zero."),
    dict(id="s21", block="fim", text="Com esta aula, {a}a trilha de funções termina. [p=0.2] Na próxima, começa a geometria plana, pelos {b}ângulos: [p=0.2] por que os ponteiros do relógio, às três horas, formam {c}um quarto de volta, ou noventa graus, [p=0.2] e como classificar um ângulo em {d}agudo, reto, obtuso ou raso. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
