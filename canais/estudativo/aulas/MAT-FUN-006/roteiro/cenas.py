# Estudativo · MAT-FUN-006 — Gráfico de uma função (Matemática · Funções · O que é função).
# Habilidade: montar a tabela de f(x) = x² − 1, marcar os pontos e usar o teste da reta vertical para dizer se uma curva é função.
# Pré-requisitos: MAT-FUN-001 (plano cartesiano), MAT-FUN-003 (f(x)). Próxima: MAT-FUN-007.
# Questão inédita, criada para esta aula. Domínio e imagem (MAT-FUN-004) fora da ficha: não usados. Parábola citada como assunto de outra aula.
# Tabela: f(−2) = 3, f(−1) = 0, f(0) = −1, f(1) = 0, f(2) = 3 · entre os pontos: f(0,5) = 0,25 − 1 = −0,75.
# Erro: reta horizontal y = 3 toca a parábola em x = −2 e x = 2 (duas entradas, mesma saída: pode).
# Atalho: entradas opostas dão a mesma saída em x² − 1; não vale em x² + x: f(2) = 6, f(−2) = 2.
# Questão: f(x) = 3 − x² · f(0) = 3, f(±1) = 2, f(±2) = −1 (U de cabeça para baixo) · reta inclinada e onda deitada: função; U deitado: não.
# Visual: E.plano de −3 a 3 (x) e −2 a 4 (y); tabela x | f(x); E.ponto nos 5 pontos com guias; E.curva de x² − 1 de −2,2 a 2,2;
#   ponto (0,5; −0,75) caindo na curva; reta vertical tracejada deslizando; círculo (duas curvas ±√(4 − x²)) e U deitado (±√x) com a vertical tocando duas vezes; onda deitada (ex.: sen x) na questão;
#   reta horizontal y = 3 tocando em −2 e 2 (erro); curva de 3 − x² e reta inclinada na resposta.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; pares narrados como "xis menos dois, ípsilon três", como na MAT-FUN-001.

TITULO = "Gráfico de uma função"

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
    dict(id="s01", block="gancho", text="{a}Este desenho é o gráfico de uma função? [p=0.2] {b}E este outro? [p=0.3] Existe um teste que responde em segundos, [p=0.2] {c}só com uma régua em pé."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você desenha o gráfico de uma função a partir de uma tabela, [p=0.2] usa {b}o teste da reta vertical [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}marcar pontos no plano, primeiro o corredor, depois o elevador, [p=0.2] e {c}calcular efe de xis, trocando o xis pelo número entre parênteses. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="O gráfico junta essas ideias. [p=0.2] {a}A entrada vai no eixo xis. [p=0.2] {b}A saída vai no eixo ípsilon. [p=0.3] Cada entrada com a sua saída vira {c}um ponto do plano. [p=0.2] O gráfico é {d}o desenho de todos esses pontos."),
    # tabela
    dict(id="s05", block="tabela", text="Vamos desenhar {a}efe de xis igual a xis ao quadrado menos um. [p=0.3] Primeiro, {b}a tabela. [p=0.2] Escolha entradas fáceis, {c}de menos dois até dois. [p=0.3] {d}Efe de menos dois: abre parênteses, menos dois, fecha parênteses, ao quadrado, dá quatro. [p=0.2] {e}Quatro menos um dá três."),
    dict(id="s06", block="tabela", text="Do mesmo jeito. [p=0.2] {a}Efe de menos um: um menos um. Dá zero. [p=0.2] {b}Efe de zero: zero menos um. Dá menos um. [p=0.2] {c}Efe de um dá zero. [p=0.2] {d}Efe de dois dá três."),
    # pontos
    dict(id="s07", block="pontos", text="Cada linha da tabela vira um ponto. [p=0.2] {a}Xis menos dois, ípsilon três: [p=0.1] dois para a esquerda, três para cima. [p=0.2] {b}Xis menos um, ípsilon zero: em cima do eixo xis. [p=0.2] {c}Xis zero, ípsilon menos um: um para baixo, no eixo ípsilon. [p=0.2] {d}Depois, xis um, ípsilon zero, [p=0.1] e {e}xis dois, ípsilon três."),
    dict(id="s08", block="pontos", text="Em seguida, {a}ligue os pontos com uma curva suave, [p=0.2] e não com tracinhos retos. [p=0.3] Entre os pontos também há entradas. [p=0.2] {b}Efe de zero vírgula cinco dá zero vírgula vinte e cinco menos um, [p=0.2] ou seja, {c}menos zero vírgula setenta e cinco. [p=0.2] E esse ponto {d}cai em cima da curva. [p=0.3] O desenho parece {e}um U. [p=0.2] Ele se chama parábola, e é assunto de outra aula."),
    # teste
    dict(id="s09", block="teste", text="E o teste da régua? [p=0.2] Lembre: função é {a}cada entrada com uma saída só. [p=0.3] Cada entrada é um lugar do eixo xis. [p=0.2] {b}Uma reta em pé, passando por ali, [p=0.2] toca o gráfico {c}em todas as saídas dessa entrada."),
    dict(id="s10", block="teste", text="Então, deslize {a}uma reta vertical pelo desenho. [p=0.3] {b}Se ela nunca toca a curva mais de uma vez, é função. [p=0.2] {c}Se em algum lugar ela toca duas vezes, não é: [p=0.2] {d}aquela entrada teria duas saídas. [p=0.3] E onde a reta não toca nada, [p=0.2] aquele xis só não é entrada dessa função."),
    dict(id="s11", block="teste", text="Na nossa curva, {a}toda reta em pé toca uma vez só: é função. [p=0.3] Já {b}o círculo falha: [p=0.2] {c}a reta em pé no meio dele toca em cima e embaixo. [p=0.2] {d}Não é gráfico de função."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}passar a régua deitada. [p=0.2] {b}Uma reta deitada na altura três toca a curva duas vezes, [p=0.2] em xis menos dois e em xis dois. [p=0.3] Isso são {c}duas entradas com a mesma saída, [p=0.2] e {d}isso pode. [p=0.2] O que não pode é {e}uma entrada com duas saídas. [p=0.2] {f}Por isso, a régua fica em pé."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho para montar a tabela: [p=0.2] em xis ao quadrado menos um, {a}entradas opostas dão a mesma saída. [p=0.3] {b}Efe de dois e efe de menos dois dão três. [p=0.2] Calcule {c}só os positivos e o zero, [p=0.2] e {d}copie os resultados para os negativos."),
    dict(id="s14", block="atalho", text="Funciona porque {a}expoente par apaga o sinal: [p=0.2] menos dois entre parênteses, ao quadrado, dá o mesmo que dois ao quadrado. [p=0.3] {b}Não compensa quando o xis também aparece sem expoente, [p=0.2] como em {c}xis ao quadrado mais xis. [p=0.2] Ali, {d}efe de dois dá seis, [p=0.2] mas {e}efe de menos dois dá dois."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Monte a tabela de efe de xis igual a três menos xis ao quadrado, [p=0.2] {b}de menos dois até dois. [p=0.3] Depois, olhe {c}estes três desenhos: [p=0.2] {d}uma reta inclinada, [p=0.2] {e}uma onda deitada, que sobe e desce da esquerda para a direita, [p=0.2] e {f}um U deitado. [p=0.3] {g}Quais são gráficos de função?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Efe de zero dá três. [p=0.2] {b}Efe de um: três menos um dá dois. [p=0.2] {c}Efe de dois: três menos quatro dá menos um. [p=0.3] Pelo atalho, {d}os negativos copiam os positivos. [p=0.2] Efe de menos um também dá dois, [p=0.2] e efe de menos dois também dá menos um. [p=0.3] {e}Ligando os pontos, sai um U de cabeça para baixo."),
    dict(id="s18", block="resposta", text="Nos desenhos, passe a régua em pé. [p=0.2] {a}A reta inclinada é tocada uma vez só: função. [p=0.2] {b}A onda também é tocada uma vez só, em qualquer lugar: função. [p=0.2] {c}O U deitado é tocado duas vezes, em cima e embaixo. [p=0.2] {d}Não é função."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}tabela, pontos e curva suave. [p=0.2] E {b}se a régua em pé toca duas vezes, não é função."),
    dict(id="s20", block="fim", text="Na próxima aula, você {a}lê um gráfico pronto: [p=0.2] {b}a temperatura ao longo de um dia. [p=0.2] Vai achar {c}a máxima, quando marcou zero, [p=0.2] quando subiu e quando desceu. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
