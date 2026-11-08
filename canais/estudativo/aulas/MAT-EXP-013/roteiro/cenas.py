# Estudativo · MAT-EXP-013 — Função logarítmica: gráfico e inequações (Matemática · Exponencial e Logaritmo).
# Habilidade: traçar y = log₂ x como espelho de y = 2ˣ, dar o domínio de log(x − 3) e resolver log₂ x > 3.
# Pré-requisitos: MAT-EXP-005 (inequação exponencial), MAT-EXP-008 (o que é logaritmo), MAT-FUN-004 (domínio). Próxima: MAT-EXP-014.
# Questão inédita, criada para esta aula. Propriedades e equações logarítmicas (MAT-EXP-009 a 012) fora da ficha: não usadas.
# Gancho: log₂ 8 = 3 · log₂ 1.024 = 10 · 1.024 ÷ 8 = 128 (mais de cem vezes) · 10 − 3 = 7.
# Tabela: log₂ 1/4 = −2, log₂ 1/2 = −1, log₂ 1 = 0, log₂ 2 = 1, log₂ 4 = 2, log₂ 8 = 3 · espelho de 2ˣ: (2, 4) ↔ (4, 2).
# Domínio: log(x − 3), base 10 → x − 3 > 0 → x > 3 → ]3, +∞[ · x = 3 daria log 0.
# Inequação: log₂ x > 3 = log₂ 8 → base 2 > 1, mantém → x > 8 → ]8, +∞[.
# Erro: log₂ x < 3 → "x < 8" esquece x > 0 (x = −1: 2^? = −1 não existe) → certo: ]0, 8[.
# Questão: log₂(x − 1) < 3 · domínio x > 1 · x − 1 < 2³ = 8 → x < 9 · resposta ]1, 9[ · teste x = 5: log₂ 4 = 2 < 3.
# Visual: tabelas de log₂ x e de 2ˣ lado a lado com as colunas trocadas; E.plano de −3 a 9 nos dois eixos; E.curva de 2ˣ e de log₂ x;
#   E.ponto em (2, 4) e (4, 2); reta y = x tracejada como espelho (dobra); eixo y como parede que a curva não toca;
#   E.reta numérica com ]3, +∞[, ]0, 8[ e ]1, 9[; linha deitada y = 3 cortando a curva em x = 8 (E.curva da constante).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; log narrado "logaritmo de oito na base dois".

TITULO = "Função logarítmica: gráfico e inequações"

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
    dict(id="s01", block="gancho", text="{a}Logaritmo de oito na base dois dá três. [p=0.2] {b}Logaritmo de mil e vinte e quatro na base dois dá dez. [p=0.3] O número {c}ficou mais de cem vezes maior, [p=0.2] e o logaritmo andou {d}só sete. [p=0.3] Esse crescimento preguiçoso tem um desenho, [p=0.2] e ele é o espelho de uma curva que você já conhece."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você desenha esse gráfico, [p=0.2] diz quais números podem entrar no logaritmo, [p=0.2] resolve inequações com ele [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}ler o logaritmo como expoente, [p=0.2] {b}o gráfico de dois elevado a xis [p=0.2] e {c}a inequação exponencial, com o sinal que vira quando a base fica entre zero e um. [p=0.3] Se faltar alguma, procure no canal."),
    # tabela
    dict(id="s04", block="tabela", text="Monte a tabela de {a}ípsilon igual a logaritmo de xis na base dois. [p=0.2] Para cada xis, pergunte: dois elevado a quanto dá esse número? [p=0.3] {b}Xis igual a um: dois elevado a zero dá um, então ípsilon é zero. [p=0.2] {c}Xis igual a dois: ípsilon é um. [p=0.2] {d}Xis igual a quatro: ípsilon é dois. [p=0.2] {e}Xis igual a oito: ípsilon é três."),
    dict(id="s05", block="tabela", text="E abaixo de um? [p=0.2] {a}Um meio é dois elevado a menos um: ípsilon é menos um. [p=0.2] {b}Um quarto é dois elevado a menos dois: ípsilon é menos dois."),
    # espelho
    dict(id="s06", block="espelho", text="Coloque do lado a tabela de {a}dois elevado a xis. [p=0.2] Lá, {b}xis dois dá ípsilon quatro. [p=0.2] No logaritmo, {c}xis quatro dá ípsilon dois. [p=0.3] São os mesmos números, {d}com as colunas trocadas. [p=0.2] A potência pega o expoente e entrega o resultado. [p=0.2] O logaritmo {e}faz o caminho de volta."),
    dict(id="s07", block="espelho", text="No plano, trocar xis com ípsilon é refletir numa reta: {a}a diagonal, onde xis e ípsilon são iguais. [p=0.2] Não é o espelho no eixo ípsilon da aula de função exponencial: [p=0.2] agora o espelho é a diagonal. [p=0.3] Dobre o papel nela, [p=0.2] e {b}a curva de dois elevado a xis cai em cima da curva do logaritmo."),
    dict(id="s08", block="espelho", text="Olhe a curva do logaritmo. [p=0.2] Ela passa por {a}xis um, ípsilon zero, porque o logaritmo de um é sempre zero. [p=0.2] {b}Sobe, porque a base dois é maior que um, [p=0.2] mas sobe {c}cada vez mais devagar. [p=0.3] E {d}nunca encosta no eixo ípsilon: chega perto, sem tocar."),
    dict(id="s09", block="espelho", text="Com base entre zero e um, como um meio, {a}a curva desce. [p=0.2] É a mesma regra da exponencial: {b}base maior que um sobe, base entre zero e um desce."),
    # domínio
    dict(id="s10", block="dominio", text="Repare que a curva {a}só existe à direita do eixo ípsilon. [p=0.2] Dois elevado a qualquer expoente {b}é sempre positivo. [p=0.2] Então o que fica dentro do logaritmo, o logaritmando, {c}precisa ser maior que zero. [p=0.3] Os números que podem entrar formam {d}o domínio: [p=0.2] de zero até mais infinito, aberto no zero."),
    dict(id="s11", block="dominio", text="Veja {a}logaritmo de xis menos três. [p=0.2] {b}A base dez está escondida. [p=0.2] O logaritmando agora é {c}xis menos três, e ele precisa ser positivo. [p=0.2] {d}Xis menos três maior que zero. [p=0.2] {e}Xis maior que três. [p=0.3] Domínio: {f}de três até mais infinito, aberto no três. [p=0.2] O próprio três fica de fora, porque daria logaritmo de zero, que não existe."),
    # inequação
    dict(id="s12", block="inequacao", text="Agora a inequação: {a}logaritmo de xis na base dois maior que três. [p=0.2] Escreva o três como logaritmo na base dois: [p=0.2] {b}três é o logaritmo de oito na base dois. [p=0.3] Fica {c}logaritmo de xis maior que logaritmo de oito, os logaritmos na base dois."),
    dict(id="s13", block="inequacao", text="Base dois, maior que um: a curva sobe. [p=0.2] Logaritmo maior vem de {a}logaritmando maior. [p=0.2] O sinal se mantém: {b}xis maior que oito. [p=0.3] No gráfico, trace {c}a linha deitada na altura três: [p=0.2] a curva passa acima dela {d}depois do xis oito."),
    dict(id="s14", block="inequacao", text="Com base entre zero e um, {a}o sinal vira, como na exponencial. [p=0.2] E nos dois casos, {b}confira o domínio: o logaritmando tem que ser positivo."),
    # erro
    dict(id="s15", block="erro", text="O erro comum é {a}esquecer o domínio. [p=0.2] Em {b}logaritmo de xis na base dois menor que três, [p=0.2] a pessoa resolve {c}xis menor que oito e para aí."),
    dict(id="s16", block="erro", text="Mas xis menor que oito inclui {a}o zero e o menos um. [p=0.2] Dois elevado a quanto dá menos um? [p=0.2] {b}Nenhum expoente. [p=0.2] Esse logaritmo nem existe. [p=0.3] A resposta certa junta as condições: {c}xis maior que zero e menor que oito. [p=0.2] Intervalo {d}aberto no zero e aberto no oito."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho: {a}a base sobe e vira potência. [p=0.2] Logaritmo de xis na base dois maior que três? [p=0.2] Leve a base para o outro lado, com o três de expoente: [p=0.2] {b}xis maior que dois ao cubo. [p=0.2] {c}Xis maior que oito, numa linha só."),
    dict(id="s18", block="atalho", text="Funciona porque o logaritmo {a}é um expoente: [p=0.2] logaritmo maior que três quer dizer que o dois precisa de mais que três no expoente para chegar no xis. [p=0.3] Com base maior que um, isso é {b}xis maior que dois ao cubo. [p=0.3] Mas o atalho não faz tudo: [p=0.2] {c}com base entre zero e um, vire o sinal; [p=0.2] e {d}junte sempre o domínio no fim: no menor que oito, foi ele que tirou o zero e os negativos."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Resolva {a}logaritmo de xis menos um na base dois menor que três, com o xis menos um todo dentro do logaritmo. [p=0.3] {b}Dê a resposta como intervalo."),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Primeiro, o domínio: {a}xis menos um maior que zero, então xis maior que um. [p=0.3] Agora a base sobe: {b}xis menos um menor que dois ao cubo, que dá oito. [p=0.2] Base dois, o sinal fica: {c}xis menor que nove."),
    dict(id="s22", block="resposta", text="Junte as condições: {a}xis maior que um e menor que nove. [p=0.2] Intervalo {b}aberto no um e aberto no nove. [p=0.3] Teste o cinco: {c}cinco menos um dá quatro, [p=0.2] e o logaritmo de quatro na base dois dá dois, menor que três. [p=0.2] Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}o logaritmo é o espelho da exponencial na diagonal. [p=0.2] {b}O logaritmando tem que ser positivo. [p=0.2] E {c}na inequação, base maior que um mantém o sinal, e base entre zero e um vira."),
    dict(id="s24", block="fim", text="Na próxima aula, o logaritmo sai do papel: [p=0.2] {a}a acidez de um líquido, a força de um terremoto e o barulho em decibéis. [p=0.3] Você vai ver por que pê agá três é {b}cem vezes mais ácido que pê agá cinco. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
