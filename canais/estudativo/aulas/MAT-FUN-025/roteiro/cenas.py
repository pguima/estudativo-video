# Estudativo · MAT-FUN-025 — Função y = k/x: a hipérbole (Matemática · Funções · Função racional simples).
# Habilidade: traçar y = 12/x para x > 0, mostrar que x · y = 12 é constante e reconhecer no gráfico duas grandezas inversamente proporcionais.
# Pré-requisitos: MAT-FUN-006 (gráfico pela tabela), MAT-RAZ-004 (inversa: o produto não muda). Próxima: MAT-FUN-026.
# Questão inédita, criada para esta aula. O exemplo das torneiras (12 h ÷ número de torneiras) é a questão da MAT-RAZ-004.
# Domínio (MAT-FUN-004/005) fora da ficha: o x = 0 é barrado com uma frase (nenhum número vezes zero dá doze).
# Teste do dobro (MAT-RAZ-005) fora da ficha: não usado. Ramo negativo citado em uma frase: 12/(−2) = −6.
# Tabela: 1→12, 2→6, 3→4, 4→3, 6→2, 12→1 · 0,5→24 · 24→0,5 · erro: y = 12 − x → (2, 10), (6, 6), (10, 2): produtos 20, 36, 20; toca o eixo x em 12.
# Atalho: um ponto dá a lei, k = x · y · questão: (4, 5) → k = 20 → y = 20/x; x = 10 → 2; (2, 10) também está nela.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; pares narrados "xis três, ípsilon quatro"; k se fala "cá".
# Visual: tabela torneiras | horas; E.plano de 0 a 13 (x) e 0 a 13 (y, escala a confirmar no visual, com o 24 fora da tela); E.ponto nos 6 pontos;
#   E.curva de 12/x de 0,9 a 13 (setas mostrando que sobe perto do eixo y e desce perto do eixo x sem tocar); retângulos x por y nos pontos (opcional, só para "o produto é doze");
#   ramo negativo pequeno no canto de baixo à esquerda; reta descendente 12 − x cortando o eixo x em 12 (erro); hipérbole por (4, 5) e (2, 10) na questão.

TITULO = "Função y = k/x: a hipérbole"

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
    dict(id="s01", block="gancho", text="Mais torneiras, {a}menos tempo para encher a caixa. [p=0.3] Quando você desenha isso no plano, {b}não sai uma reta. [p=0.2] Sai uma curva que desce cada vez mais devagar [p=0.2] e {c}nunca encosta no eixo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você desenha essa curva, descobre o número que nunca muda nela [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}grandezas inversamente proporcionais, em que o produto é sempre o mesmo, [p=0.2] e {b}o gráfico pela tabela: escolhe o xis, calcula o ípsilon e marca o ponto. [p=0.3] Se faltar alguma, procure no canal."),
    # a lei
    dict(id="s04", block="lei", text="Lembra das torneiras iguais? [p=0.2] {a}Uma torneira enche a caixa em doze horas. [p=0.2] {b}Duas, em seis. [p=0.2] {c}Três, em quatro. [p=0.3] O tempo é sempre {d}doze dividido pelo número de torneiras."),
    dict(id="s05", block="lei", text="Chamando o número de torneiras de xis e o tempo de ípsilon: [p=0.2] {a}ípsilon igual a doze dividido por xis. [p=0.3] E repare: {b}xis vezes ípsilon dá sempre doze. [p=0.2] É o produto que não muda, a marca da {c}grandeza inversamente proporcional."),
    # tabela
    dict(id="s06", block="tabela", text="Vamos à tabela, só com xis positivo. [p=0.2] {a}Xis um, ípsilon doze. [p=0.2] {b}Xis dois, ípsilon seis. [p=0.2] {c}Xis três, ípsilon quatro. [p=0.2] {d}Xis quatro, ípsilon três. [p=0.2] {e}Xis seis, ípsilon dois. [p=0.2] {f}Xis doze, ípsilon um."),
    dict(id="s07", block="tabela", text="Como função, o xis também pode ser quebrado. [p=0.2] {a}Xis zero vírgula cinco: doze dividido por zero vírgula cinco dá vinte e quatro. [p=0.3] {b}Xis vinte e quatro: doze dividido por vinte e quatro dá zero vírgula cinco."),
    # curva
    dict(id="s08", block="curva", text="Marque os pontos e ligue com uma curva suave. [p=0.2] {a}Perto do eixo ípsilon, ela dispara para cima. [p=0.2] {b}Longe dele, ela desce cada vez mais devagar, quase deitada. [p=0.3] Essa curva se chama {c}hipérbole."),
    dict(id="s09", block="curva", text="Por que ela nunca toca os eixos? [p=0.2] Use o produto. [p=0.2] Se o ípsilon fosse zero, {a}xis vezes zero daria zero, nunca doze. [p=0.2] Se o xis fosse zero, mesma coisa. [p=0.3] E ainda: {b}doze dividido por zero não existe, [p=0.2] porque nenhum número vezes zero dá doze. [p=0.3] {c}A curva chega perto dos eixos, mas não encosta."),
    dict(id="s10", block="curva", text="Com xis negativo, a hipérbole tem {a}uma segunda parte, no canto de baixo à esquerda: [p=0.2] doze dividido por menos dois dá menos seis. [p=0.3] Em problemas com torneiras, tempo ou dinheiro, {b}só a parte positiva interessa."),
    # reconhecer
    dict(id="s11", block="reconhecer", text="Para reconhecer a hipérbole num gráfico, {a}escolha alguns pontos e multiplique as coordenadas. [p=0.3] Em {b}xis dois, ípsilon seis, dá doze. [p=0.2] Em {c}xis três, ípsilon quatro, também dá doze. [p=0.3] {d}Produto sempre igual: as grandezas são inversamente proporcionais. [p=0.2] Esse número fixo costuma ser chamado de {e}cá, e a lei geral é {f}ípsilon igual a cá dividido por xis."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é achar que {a}todo gráfico que desce é inversamente proporcional. [p=0.3] Veja a reta {b}ípsilon igual a doze menos xis. [p=0.2] Ela desce: passa por {c}xis dois, ípsilon dez, [p=0.2] e por {d}xis seis, ípsilon seis."),
    dict(id="s13", block="erro", text="Multiplique: {a}dois vezes dez dá vinte. [p=0.2] {b}Seis vezes seis dá trinta e seis. [p=0.3] {c}Produtos diferentes: não é inversa. [p=0.2] E tem mais uma pista: {d}ela corta o eixo xis no doze. [p=0.2] A hipérbole nunca faz isso."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}um ponto basta para achar a lei. [p=0.2] Se a hipérbole passa por {b}xis três, ípsilon quatro, [p=0.2] o cá é {c}três vezes quatro, que dá doze. [p=0.2] A lei é {d}ípsilon igual a doze dividido por xis. [p=0.3] Com ela, qualquer outro ponto sai na hora."),
    dict(id="s15", block="atalho", text="Funciona porque, nessa curva, {a}xis vezes ípsilon é sempre o cá. [p=0.3] Não compensa quando {b}você ainda não sabe se a curva é uma hipérbole. [p=0.2] Aí, {c}multiplique as coordenadas de vários pontos antes. [p=0.2] Se algum produto der diferente, a lei é outra."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma hipérbole do tipo {a}ípsilon igual a cá dividido por xis passa pelo ponto {b}xis quatro, ípsilon cinco. [p=0.3] {c}Qual é a lei? [p=0.2] Quanto vale o ípsilon {d}em xis dez? [p=0.2] E o ponto {e}xis dois, ípsilon dez, está na curva?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] O cá é {a}quatro vezes cinco, que dá vinte. [p=0.2] A lei é {b}ípsilon igual a vinte dividido por xis. [p=0.3] Em xis dez: {c}vinte dividido por dez dá dois. [p=0.3] E o ponto xis dois, ípsilon dez: {d}dois vezes dez dá vinte. [p=0.2] O produto bate: {e}está na curva."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}em ípsilon igual a cá dividido por xis, xis vezes ípsilon é sempre cá, [p=0.2] e {b}o gráfico é uma hipérbole que nunca toca os eixos."),
    dict(id="s20", block="fim", text="Na próxima aula, a hipérbole entra na fábrica: [p=0.2] {a}o custo médio de cada peça. [p=0.2] Quanto mais peças, mais barata fica cada uma, [p=0.2] mas {b}existe um valor que ela nunca alcança. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
