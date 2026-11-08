# Estudativo · MAT-EQU-002 — Valor numérico de uma expressão (Matemática · Equações do 1º Grau).
# Habilidade: calcular 2x² − 3 para x = −2, sempre com parênteses ao substituir.
# Pré-requisitos: MAT-EQU-001 (a letra no lugar de um número), MAT-NUM-018 (expressões com inteiros), MAT-POT-002 (potência de negativo). Próxima: MAT-EQU-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula.
# Ordem como em MAT-POT-002: parênteses, potência, vezes e dividido, mais e menos.
# 3x + 4, x = 5 → 3 × (5) + 4 = 19 · 5 − x, x = −4 → 5 − (−4) = 9.
# 2x² − 3, x = −2 → 2 × (−2)² − 3 = 2 × 4 − 3 = 5. Sem parênteses: 2 × (−4) − 3 = −11. Vezes antes da potência: (−4)² − 3 = 13.
# Questão: x² − 4x, x = −3 → 9 − (−12) = 21; perdendo o sinal, 9 − 12 = −3.

TITULO = "Valor numérico de uma expressão"

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
    dict(id="s01", block="gancho", text="{a}Dois xis ao quadrado menos três, [p=0.2] com {b}xis igual a menos dois. [p=0.3] Se deu {c}menos onze, [p=0.2] faltou um par de parênteses. [p=0.3] A resposta é {d}cinco."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você troca a letra por qualquer número sem errar o sinal, [p=0.2] com um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Três lembretes. [p=0.2] {a}Dois xis é dois vezes xis. [p=0.2] {b}A ordem: parênteses, depois potência, depois vezes e dividido, por último mais e menos. [p=0.3] E {c}abre parênteses, menos três, fecha parênteses, ao quadrado, dá nove, [p=0.2] mas {d}menos três ao quadrado, sem parênteses, dá menos nove. [p=0.3] Se faltar alguma, procure no canal."),
    # trocar
    dict(id="s04", block="trocar", text="Trocar a letra por um número e fazer a conta [p=0.2] dá o {a}valor numérico da expressão. [p=0.3] Veja {b}três xis mais quatro, para xis igual a cinco. [p=0.3] {c}Apague o xis [p=0.2] e {d}ponha o cinco entre parênteses: [p=0.2] {e}três vezes cinco mais quatro."),
    dict(id="s05", block="trocar", text="Repare que {a}o vezes escondido volta a aparecer. [p=0.2] Na ordem de sempre: {b}três vezes cinco dá quinze. [p=0.2] {c}Quinze mais quatro dá dezenove."),
    dict(id="s06", block="trocar", text="Com número positivo, o parêntese parece enfeite. [p=0.2] Mas ele {a}guarda o número inteiro, com sinal e tudo. [p=0.3] Veja {b}cinco menos xis, para xis igual a menos quatro. [p=0.3] Com parênteses: {c}cinco menos, abre parênteses, menos quatro, fecha parênteses. [p=0.2] Tirar uma dívida é como ganhar: {d}cinco mais quatro dá nove. [p=0.3] Sem parênteses, {e}um sinal de menos encosta no outro, [p=0.2] e é aí que a conta se perde."),
    dict(id="s07", block="trocar", text="Por isso, a regra é: [p=0.2] {a}ao trocar a letra, ponha o número entre parênteses. [p=0.2] Positivo ou negativo, {b}sempre. [p=0.3] É um hábito que custa um segundo [p=0.2] e evita o erro mais caro desta aula."),
    # a conta do começo
    dict(id="s08", block="exemplo", text="Voltando ao começo: {a}dois xis ao quadrado menos três, com xis igual a menos dois. [p=0.3] Troque com parênteses: [p=0.2] {b}dois vezes, abre parênteses, menos dois, fecha parênteses, ao quadrado, menos três."),
    dict(id="s09", block="exemplo", text="Na ordem. [p=0.2] {a}Primeiro a potência: menos dois vezes menos dois. [p=0.2] Sinais iguais: mais quatro. [p=0.2] {b}Depois o vezes: dois vezes quatro dá oito. [p=0.2] {c}Por último, oito menos três dá {d}cinco."),
    dict(id="s10", block="exemplo", text="E o menos onze? [p=0.2] Sem parênteses, o expoente {a}só alcança o dois, e não o sinal. [p=0.2] A potência vira {b}menos quatro, [p=0.2] o vezes dá {c}menos oito, [p=0.2] e no fim sai {d}menos onze. [p=0.3] O xis valia menos dois inteiro, [p=0.2] mas {e}a conta usou só um pedaço dele."),
    # erro
    dict(id="s11", block="erro", text="Outro erro comum: [p=0.2] fazer {a}o vezes antes da potência. [p=0.2] A pessoa calcula {b}dois vezes menos dois, que dá menos quatro, [p=0.2] e eleva {c}isso ao quadrado: dezesseis. [p=0.2] Termina em {d}treze. [p=0.3] Mas, em dois xis ao quadrado, {e}o expoente está colado só no xis. [p=0.2] O número da frente fica de fora e {f}multiplica depois."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}com o menos dentro do parêntese, expoente par apaga o sinal. [p=0.3] {b}Abre parênteses, menos dois, fecha parênteses, ao quadrado, [p=0.2] dá o mesmo que {c}dois ao quadrado: quatro. [p=0.3] Sem parênteses, como no menos onze, o expoente nem alcança o sinal. [p=0.3] Então, ao trocar o xis com parênteses em xis ao quadrado, {d}faça a conta com o número sem o sinal."),
    dict(id="s13", block="atalho", text="Funciona porque {a}cada dupla de menos vira mais. [p=0.3] Mas {b}não vale no xis sem expoente: [p=0.2] em menos três xis, o sinal do número muda a resposta."),
    dict(id="s14", block="atalho", text="{a}Nem com expoente ímpar. [p=0.2] {b}Abre parênteses, menos dois, fecha parênteses, ao cubo, dá menos oito, [p=0.2] mas {c}dois ao cubo dá oito. [p=0.3] Com expoente ímpar, o sinal fica, [p=0.2] e a conta é feita inteira, com sinal e tudo."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Calcule {a}xis ao quadrado menos quatro xis, [p=0.2] para {b}xis igual a menos três."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá, com parênteses: [p=0.2] {a}abre parênteses, menos três, fecha parênteses, ao quadrado, [p=0.2] menos quatro vezes, abre parênteses, menos três, fecha parênteses. [p=0.3] Pelo atalho, {b}a potência dá nove."),
    dict(id="s18", block="resposta", text="{a}Quatro vezes menos três dá menos doze. [p=0.2] Fica {b}nove menos, abre parênteses, menos doze, fecha parênteses. [p=0.2] Tirar uma dívida é como ganhar: [p=0.2] {c}nove mais doze dá {d}vinte e um. [p=0.3] Quem perdeu o sinal fez nove menos doze [p=0.2] e chegou em {e}menos três: [p=0.2] esqueceu que tirar uma dívida é ganhar."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}troque a letra pelo número entre parênteses, com sinal e tudo, [p=0.2] e {b}siga a ordem das operações."),
    dict(id="s20", block="fim", text="Na próxima aula, você aprende a {a}juntar termos parecidos, [p=0.2] como {b}três xis mais cinco xis, [p=0.2] e deixa a expressão {c}mais curta. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
