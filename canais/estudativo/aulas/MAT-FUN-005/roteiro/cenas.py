# Estudativo · MAT-FUN-005 — Domínio pela fórmula (Matemática · Funções · O que é função).
# Habilidade: dizer que 1/(x − 2) exige x ≠ 2 e que √(x − 3) exige x ≥ 3, escrevendo a resposta em intervalo.
# Pré-requisitos: MAT-FUN-004 (domínio), MAT-EQU-015 (inequação), MAT-POT-016 (raiz de negativo). Próxima: MAT-FUN-006.
# Questão inédita, criada para esta aula. União de intervalos (MAT-CON-008) fora da ficha: citada como assunto de outra aula.
# Divisão por zero: 6 ÷ 2 = 3 porque 3 × 2 = 6; 6 ÷ 0 pediria um número que vezes zero dá 6: não existe.
# 1/(x − 2): x − 2 ≠ 0 → x ≠ 2 → ]−∞, 2[ ou ]2, +∞[ (na tela, "ou": "e" seria interseção, MAT-CON-008) · √(x − 3): x − 3 ≥ 0 → x ≥ 3 → [3, +∞[ · teste: x = 7 → √4 = 2; x = 2 → √−1 fora; √0 = 0.
# Erro: tratar a raiz como divisão, x − 3 ≠ 0 → x ≠ 3, deixaria entrar o 2 (√−1).
# Atalho: raiz cúbica não barra: ∛−8 = −2; raiz quarta (índice par) barra como a quadrada.
# Questão: g(x) = 5/(x + 4) → x ≠ −4 → ]−∞, −4[ ou ]−4, +∞[ · h(x) = √(6 − 2x) → 6 − 2x ≥ 0 → −2x ≥ −6 → x ≤ 3 → ]−∞, 3]; teste x = 0: √6 existe.
# Visual: fórmulas com o denominador e o radicando realçados; reta numérica com furo (bolinha aberta) no 2 e pintada dos lados;
#   reta com bolinha fechada no 3 pintada para a direita; os "vilões" (divisão e raiz par) em cartões; respostas em intervalo.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras: efe, gê, agá.

TITULO = "Domínio pela fórmula"

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
    dict(id="s01", block="gancho", text="Na função {a}efe de xis igual a um dividido por xis menos dois, [p=0.2] com o xis menos dois todo embaixo, [p=0.2] coloque {b}xis igual a dois. [p=0.3] Fica {c}um dividido por zero, [p=0.2] e a calculadora mostra {d}erro. [p=0.3] O dois {e}não pode entrar nessa função."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o domínio só pela fórmula, [p=0.2] escreve a resposta em intervalo [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}domínio, o conjunto do que pode entrar na função; [p=0.2] {c}resolver inequação, virando o sinal ao dividir por negativo; [p=0.2] e {d}saber que raiz quadrada de negativo não dá número da reta. [p=0.3] Se faltar alguma, procure no canal."),
    # regra
    dict(id="s04", block="regra", text="Quando a função vem só pela fórmula, sem história, [p=0.2] o domínio é {a}todo número real que deixa a conta funcionar. [p=0.3] Na maioria das contas, {b}qualquer número entra. [p=0.2] Só {c}duas coisas barram a entrada: [p=0.2] {d}divisão por zero [p=0.2] e {e}raiz quadrada de negativo."),
    dict(id="s05", block="zero", text="Por que não se divide por zero? [p=0.2] {a}Seis dividido por dois dá três, porque três vezes dois dá seis. [p=0.3] {b}Seis dividido por zero seria um número que, vezes zero, desse seis. [p=0.2] Mas {c}todo número vezes zero dá zero. [p=0.2] Esse número {d}não existe."),
    # divisão
    dict(id="s06", block="divisao", text="Então, em {a}um sobre xis menos dois, [p=0.2] o de baixo {b}não pode ser zero. [p=0.3] {c}Xis menos dois diferente de zero. [p=0.2] Resolva como equação: {d}xis diferente de dois. [p=0.3] {e}Qualquer real entra, menos o dois."),
    dict(id="s07", block="divisao", text="Na reta, é {a}a reta toda com um furo no dois: [p=0.2] {b}bolinha aberta ali. [p=0.3] Em intervalo, são {c}duas partes, [p=0.2] e o xis pode estar em uma ou na outra. [p=0.2] {d}De menos infinito até dois, [p=0.2] ou {e}de dois até mais infinito, [p=0.2] {f}sempre aberto no dois. [p=0.3] O símbolo que junta as partes, a {g}união, é assunto de outra aula."),
    # raiz
    dict(id="s08", block="raiz", text="E a raiz? [p=0.2] Veja {a}efe de xis igual a raiz quadrada de xis menos três, [p=0.2] com o xis menos três {b}todo dentro da raiz. [p=0.3] O de dentro {c}não pode ser negativo. [p=0.2] Mas pode ser zero, porque {d}raiz de zero é zero. [p=0.3] Então, {e}xis menos três maior ou igual a zero."),
    dict(id="s09", block="raiz", text="{a}Some três de cada lado: xis maior ou igual a três. [p=0.3] Em intervalo: {b}de três até mais infinito, [p=0.2] {c}fechado no três, porque ele entra. [p=0.3] Teste: {d}xis igual a sete dá raiz de quatro, que é dois. [p=0.2] {e}Xis igual a dois dá raiz de menos um: não dá número da reta. [p=0.2] Bateu."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}tratar a raiz como a divisão. [p=0.2] A pessoa escreve xis menos três {b}diferente de zero [p=0.2] e responde {c}xis diferente de três. [p=0.3] Aí o dois entraria, [p=0.2] e {d}raiz de menos um não dá número da reta. [p=0.3] {e}Embaixo da divisão, diferente de zero. [p=0.2] {f}Dentro da raiz quadrada, maior ou igual a zero."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: {a}procure os vilões antes de fazer conta. [p=0.3] {b}Tem divisão com xis embaixo? [p=0.2] O de baixo, diferente de zero. [p=0.2] {c}Tem raiz quadrada com xis dentro? [p=0.2] O de dentro, maior ou igual a zero. [p=0.3] {d}Não tem nenhum vilão? [p=0.2] O domínio é {e}todos os reais."),
    dict(id="s12", block="atalho", text="Funciona porque {a}só esses lugares quebram a conta. [p=0.2] Repare que {b}a raiz cúbica não barra ninguém: [p=0.2] raiz cúbica de menos oito é menos dois. [p=0.2] Já a raiz quarta tem índice par e barra o negativo, como a quadrada. [p=0.3] {c}Não compensa parar na fórmula quando há uma história, [p=0.2] como {d}tempo ou número de pessoas. [p=0.2] Aí, {e}a situação também corta o domínio."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Ache o domínio de cada função, em intervalo. [p=0.3] {a}Gê de xis igual a cinco sobre xis mais quatro, [p=0.2] com o xis mais quatro todo embaixo. [p=0.3] {b}Agá de xis igual a raiz quadrada de seis menos dois xis, [p=0.2] com tudo dentro da raiz."),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] Em gê, o de baixo não pode ser zero: [p=0.2] {a}xis mais quatro diferente de zero. [p=0.2] {b}Tire quatro: xis diferente de menos quatro. [p=0.3] Em intervalo: {c}de menos infinito até menos quatro, [p=0.2] ou {d}de menos quatro até mais infinito, [p=0.2] sempre aberto no menos quatro."),
    dict(id="s16", block="resposta", text="Em agá, o de dentro não pode ser negativo: [p=0.2] {a}seis menos dois xis maior ou igual a zero. [p=0.2] {b}Tire seis: menos dois xis maior ou igual a menos seis. [p=0.2] {c}Divida por menos dois e vire o sinal: [p=0.2] {d}xis menor ou igual a três. [p=0.3] Em intervalo: {e}de menos infinito até três, fechado no três. [p=0.3] Teste o zero: {f}raiz de seis existe, e o zero está na resposta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}embaixo da divisão, diferente de zero. [p=0.2] {b}Dentro da raiz quadrada, maior ou igual a zero. [p=0.2] {c}Sem vilão, todos os reais."),
    dict(id="s18", block="fim", text="Na próxima aula, a função ganha {a}um desenho. [p=0.2] Você monta a tabela, {b}marca os pontos no plano cartesiano [p=0.2] e usa {c}o teste da reta vertical para saber se uma curva é função. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
