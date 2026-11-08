# Estudativo · MAT-PLN-008 — Delta negativo: o número i (Matemática · Polinômios · Raízes complexas).
# Habilidade: usar i² = −1 para resolver x² − 4x + 13 = 0 (x = 2 ± 3i) e multiplicar (2 + 3i)(2 − 3i) = 13.
# Pré-requisitos: MAT-CON-006 (números reais), MAT-FAT-009 (delta negativo, sem raiz real), MAT-FAT-010 (Bhaskara até o fim). Próxima: MAT-PLN-009.
# As aulas de polinômio (MAT-PLN-001 a 007) não estão na ficha desta: a aula fica só na equação do 2º grau.
# Soma e produto (MAT-FAT-011) também não: o 13 = 4 + 9 sai da soma vezes diferença (MAT-FAT-015). Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o número i se escreve "í".

TITULO = "Delta negativo: o número i"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado menos quatro xis mais treze igual a zero. [p=0.3] O delta dá {b}menos trinta e seis, [p=0.2] e nenhum número da reta resolve. [p=0.3] Mesmo assim, a resposta de prova é {c}dois mais ou menos três í."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve equações com delta negativo usando um número novo, [p=0.2] {b}o í, [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}a fórmula de Bhaskara, com o delta primeiro; [p=0.2] {c}delta negativo, nenhuma raiz real, porque nenhum número real ao quadrado dá negativo; [p=0.2] e {d}a raiz de uma multiplicação: raiz de quatro vezes dois é raiz de quatro vezes raiz de dois. [p=0.3] Se faltar alguma, procure no canal."),
    # o número i
    dict(id="s04", block="numero_i", text="Os matemáticos fizeram uma pergunta ousada: [p=0.2] e se existisse {a}um número que, ao quadrado, desse menos um? [p=0.3] Ele não está na reta. [p=0.2] Ganhou o nome de {b}í, a unidade imaginária. [p=0.3] A regra que você precisa é uma só: {c}í ao quadrado é igual a menos um."),
    dict(id="s05", block="numero_i", text="Com ele, {a}a raiz de menos um passa a ser í. [p=0.2] E qualquer raiz de negativo se resolve: [p=0.2] {b}menos trinta e seis é trinta e seis vezes menos um. [p=0.2] A raiz de trinta e seis é seis, e a de menos um é í: [p=0.2] {c}seis í."),
    dict(id="s06", block="numero_i", text="Números como {a}dois mais três í se chamam {b}números complexos: [p=0.2] {c}uma parte real, o dois, [p=0.2] mais {d}uma parte imaginária, o três í. [p=0.3] Os reais estão dentro deles: {e}é só a parte imaginária valer zero."),
    # resolver
    dict(id="s07", block="resolver", text="Volte para {a}xis ao quadrado menos quatro xis mais treze igual a zero. [p=0.2] {b}Á vale um, bê vale menos quatro, cê vale treze. [p=0.2] Delta: {c}dezesseis menos cinquenta e dois, menos trinta e seis. [p=0.3] {d}Raiz de delta: seis í."),
    dict(id="s08", block="resolver", text="Na fórmula: {a}quatro, mais ou menos seis í, dividido por dois. [p=0.2] {b}Divida cada parte por dois: [p=0.2] {c}quatro dividido por dois dá dois, [p=0.2] e {d}seis í dividido por dois dá três í. [p=0.3] {e}Xis igual a dois mais três í, ou dois menos três í."),
    dict(id="s09", block="resolver", text="Confira o dois mais três í. [p=0.2] {a}Ao quadrado, pelo quadrado da soma: quatro mais doze í mais nove í ao quadrado. [p=0.2] Como í ao quadrado é menos um, {b}fica menos cinco mais doze í. [p=0.3] {c}Menos quatro vezes dois mais três í: menos oito menos doze í. [p=0.2] {d}Somando tudo com o treze: zero. [p=0.2] Bateu."),
    # multiplicar
    dict(id="s10", block="multiplicar", text="Multiplicar complexos é {a}o chuveirinho de sempre, trocando í ao quadrado por menos um. [p=0.2] Veja {b}dois mais três í, vezes dois menos três í. [p=0.3] É {c}soma vezes diferença: [p=0.2] {d}dois ao quadrado menos, abre parênteses, três í, fecha parênteses, ao quadrado."),
    dict(id="s11", block="multiplicar", text="{a}Três í, ao quadrado, é nove vezes í ao quadrado: menos nove. [p=0.2] {b}Quatro menos, abre parênteses, menos nove, fecha parênteses: treze. [p=0.3] O í sumiu: {c}o resultado é real. [p=0.2] Dois menos três í é o {d}conjugado de dois mais três í: só o sinal do í muda."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}dizer que a raiz de menos trinta e seis é menos seis. [p=0.2] Mas {b}menos seis, ao quadrado, dá trinta e seis, positivo. [p=0.3] {c}Seis í, ao quadrado, dá trinta e seis vezes menos um: menos trinta e seis. [p=0.2] {d}O menos de dentro da raiz vira í, e não sinal de menos."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}um complexo vezes o conjugado dele [p=0.2] é {b}a parte real ao quadrado, mais o quadrado do número que acompanha o í. [p=0.3] {c}Dois mais três í, vezes dois menos três í: quatro mais nove, treze. [p=0.2] {d}Sem chuveirinho."),
    dict(id="s14", block="atalho", text="Funciona porque {a}é soma vezes diferença, [p=0.2] e {b}o í ao quadrado transforma o menos em mais. [p=0.3] {c}Não vale para dois complexos quaisquer, como dois mais três í, vezes um menos í: [p=0.2] aí, faça o chuveirinho."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Resolva {a}xis ao quadrado mais dois xis mais cinco igual a zero."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Á vale um, bê vale dois, cê vale cinco. [p=0.2] Delta: {b}quatro menos vinte, menos dezesseis. [p=0.2] {c}Raiz de menos dezesseis: quatro í."),
    dict(id="s18", block="resposta", text="Na fórmula: {a}menos dois, mais ou menos quatro í, dividido por dois. [p=0.2] {b}Menos dois dividido por dois, menos um. [p=0.2] {c}Quatro í dividido por dois, dois í. [p=0.3] Resposta: {d}xis igual a menos um mais dois í, ou menos um menos dois í."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}í ao quadrado é menos um, [p=0.2] {b}raiz de negativo vira í, [p=0.2] e {c}a fórmula de Bhaskara continua funcionando."),
    dict(id="s20", block="fim", text="Na próxima aula, você descobre que {a}raízes complexas vêm em pares: [p=0.2] se {b}um mais dois í é raiz, um menos dois í também é. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
