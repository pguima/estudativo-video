# Estudativo · MAT-FAV-007 — Função par e função ímpar (Matemática · Funções Avançadas · Função composta e inversa).
# Habilidade: testar f(−x) e dizer que x² é par, com gráfico simétrico no eixo y, e que x³ é ímpar, com gráfico simétrico na origem.
# Pré-requisitos: MAT-FUN-007 (ler um gráfico), MAT-POL-010 (eixos de simetria). Próxima: MAT-FAV-008.
# Questão inédita, criada para esta aula. Parábola, módulo e exponencial fora da ficha: os gráficos aparecem por pontos, sem nome.
# (−2)² = 4 = 2² · (−2)³ = −8 = −(2³) · (−x)² = x² → par · (−x)³ = −x³ → ímpar · x + 1: f(−x) = −x + 1, −f(x) = −x − 1 → nenhuma.
# Erro: x³ + 1 · f(2) = 9 · f(−2) = −7 · −f(2) = −9 → não é ímpar.
# Atalho (soma de potências de x): só expoentes pares (número sozinho conta como par) → par; só ímpares, sem número sozinho → ímpar.
# Questão: f(x) = x³ − 4x → f(−x) = −x³ + 4x = −f(x) → ímpar · g(x) = x² − 5 → par · h(x) = x² + x → nenhuma (h(1) = 2, h(−1) = 0).
# Visual: plano −3..3 com x² (E.curva), pontos (±2, 4) e a dobra no eixo y (metade da esquerda girando sobre a direita);
#   plano com x³/2 para caber (marcas reais: (2, 8) e (−2, −8) com escala própria) e o giro de meia volta na origem; palco no atalho.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; "éfe de menos xis".

TITULO = "Função par e função ímpar"

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
    dict(id="s01", block="gancho", text="{a}Menos dois ao quadrado dá quatro, [p=0.2] o mesmo que {b}dois ao quadrado. [p=0.3] Já {c}menos dois ao cubo dá menos oito: [p=0.2] {d}o oposto de dois ao cubo. [p=0.3] Essa diferença separa as funções em {e}pares e ímpares, [p=0.2] e dá para ver no gráfico."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você testa se uma função é par, ímpar ou nenhuma das duas, [p=0.2] {b}reconhece pela simetria do gráfico [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}potência de número negativo: expoente par dá positivo, e expoente ímpar mantém o sinal; [p=0.2] e {b}eixo de simetria: a linha onde você dobra a figura e as metades coincidem. [p=0.3] Se faltar alguma, procure no canal."),
    # o teste
    dict(id="s04", block="teste", text="O teste é um só: {a}troque o xis por menos xis [p=0.2] e compare {b}éfe de menos xis com éfe de xis."),
    # par
    dict(id="s05", block="par", text="Em {a}éfe de xis igual a xis ao quadrado, [p=0.2] {b}menos xis, ao quadrado, dá xis ao quadrado. [p=0.2] {c}Voltou igual. [p=0.3] Quando éfe de menos xis é igual a éfe de xis, a função é {d}par."),
    dict(id="s06", block="par", text="No gráfico: {a}xis dois e xis menos dois têm a mesma altura, quatro. [p=0.2] {b}Isso vale para todo número e o seu oposto. [p=0.2] Então, {c}o eixo ípsilon é um eixo de simetria: [p=0.2] {d}dobre o papel nele, e as metades se cobrem."),
    # ímpar
    dict(id="s07", block="impar", text="Agora, {a}éfe de xis igual a xis ao cubo. [p=0.2] {b}Menos xis, ao cubo, dá menos xis ao cubo. [p=0.2] {c}Voltou o oposto. [p=0.3] Quando éfe de menos xis é o oposto de éfe de xis, a função é {d}ímpar."),
    dict(id="s08", block="impar", text="No gráfico: {a}xis dois dá oito, [p=0.2] e {b}xis menos dois dá menos oito. [p=0.2] Um ponto fica à direita e em cima; o outro, à esquerda e embaixo. [p=0.3] Aqui, a dobra não funciona. [p=0.2] O que funciona é {c}girar o desenho meia volta em torno da origem: [p=0.2] {d}ele cai em cima de si mesmo. [p=0.2] É a {e}simetria em relação à origem."),
    # nenhuma
    dict(id="s09", block="nenhuma", text="E existe {a}a função que não é nenhuma das duas. [p=0.2] Em {b}xis mais um, [p=0.2] éfe de menos xis dá {c}menos xis mais um. [p=0.2] {d}Não é igual a xis mais um, [p=0.2] {e}nem é o oposto, que seria menos xis menos um. [p=0.3] {f}Nem par, nem ímpar."),
    # erro
    dict(id="s10", block="erro", text="O erro comum é {a}olhar só o expoente. [p=0.2] A pessoa vê {b}xis ao cubo mais um e diz: expoente três, ímpar."),
    dict(id="s11", block="erro", text="Teste: {a}éfe de dois dá nove. [p=0.2] {b}Éfe de menos dois dá menos oito mais um: menos sete. [p=0.2] O oposto de nove seria menos nove. [p=0.2] {c}Não bateu: não é ímpar. [p=0.3] {d}O mais um estragou a simetria."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, para leis que são somas de potências de xis. [p=0.2] {a}Só expoentes pares: par. [p=0.2] O número sozinho conta como par, [p=0.2] porque ele não muda quando o xis vira menos xis. [p=0.3] {b}Só expoentes ímpares, sem número sozinho: ímpar. [p=0.2] {c}Misturou: nem par, nem ímpar."),
    dict(id="s13", block="atalho", text="Funciona porque {a}menos xis num expoente par perde o sinal, [p=0.2] e {b}num expoente ímpar mantém o sinal. [p=0.3] {c}O atalho só vale para soma de potências de xis. [p=0.2] {d}Em outras leis, faça o teste do menos xis."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Classifique em par, ímpar ou nenhuma das duas: [p=0.2] {a}éfe de xis igual a xis ao cubo menos quatro xis; [p=0.2] {b}gê de xis igual a xis ao quadrado menos cinco; [p=0.2] e {c}agá de xis igual a xis ao quadrado mais xis."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Em éfe, xis ao cubo tem expoente três, e quatro xis tem expoente um: só ímpares, sem número sozinho. [p=0.2] {b}Ímpar. [p=0.2] No teste, {c}éfe de menos xis dá menos xis ao cubo mais quatro xis, o oposto de éfe."),
    dict(id="s17", block="resposta", text="{a}Em gê, o expoente dois e o menos cinco sozinho: tudo par. [p=0.2] {b}Par. [p=0.3] {c}Em agá, expoente dois com expoente um: misturou. [p=0.2] {d}Nem par, nem ímpar. [p=0.2] Confira com o um: {e}agá de um dá dois, e agá de menos um dá zero."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}troque xis por menos xis. [p=0.2] {b}Voltou igual: par, espelho no eixo ípsilon. [p=0.2] {c}Voltou o oposto: ímpar, meia volta na origem."),
    dict(id="s19", block="fim", text="Na próxima aula, {a}você pratica tudo da trilha: [p=0.2] {b}função por partes, módulo, composta, inversa e paridade, em situações de prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
