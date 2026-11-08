# Estudativo · MAT-FAT-004 — Simplificar frações algébricas (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: reduzir (x² − 9)/(x − 3) a x + 3, para x ≠ 3, cortando só fatores e nunca parcelas.
# Pré-requisitos: MAT-FAT-003 (fatorar com produtos notáveis), MAT-FRA-003 (simplificação), MAT-FAT-002 (evidência). Próxima: MAT-FAT-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula. Divisão por zero explicada na hora. Sem decimais (FRA-014 fora de "Já ensinado").
# 18/24 = (6·3)/(6·4) = 3/4 · (x² − 9)/(x − 3) = x + 3 (x = 10: 91/7 = 13) · (5x + 15)/(x² − 9) = 5/(x − 3), x ≠ ±3 (x = 10: 65/91 = 5/7).
# Erro: (x + 3)/3 = x? x = 6: 9/3 = 3 contra 6.
# Questão: (x² − 25)/(2x + 10) = (x − 5)/2, x ≠ −5 (x = 10: 75/30 = 5/2).

TITULO = "Simplificar frações algébricas"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado menos nove, dividido por xis menos três. [p=0.3] Parece complicado. [p=0.2] Mas é só {b}xis mais três, disfarçado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você simplifica frações com letra [p=0.2] sem cair no {b}corte proibido, [p=0.2] e leva um {c}atalho para questões com alternativas."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas. [p=0.2] {b}Simplificar uma fração é dividir em cima e embaixo pelo mesmo número. [p=0.2] E {c}fatorar: colocar em evidência e usar a diferença de dois quadrados. [p=0.3] Se faltar alguma, procure no canal."),
    # com números
    dict(id="s04", block="numeros", text="Comece com números: {a}dezoito vinte e quatro avos. [p=0.2] Escreva {b}dezoito como seis vezes três [p=0.2] e {c}vinte e quatro como seis vezes quatro. [p=0.3] O seis multiplica em cima e embaixo. [p=0.2] Dividir em cima e embaixo por seis é {d}cortar o seis: [p=0.2] {e}três quartos."),
    dict(id="s05", block="numeros", text="Esse corte só vale para {a}fator: o que multiplica a parte de cima inteira e a de baixo inteira. [p=0.3] {b}Parcela, que é um pedaço de uma soma, não se corta."),
    # fração algébrica
    dict(id="s06", block="algebrica", text="Fração com letra se chama {a}fração algébrica, e segue a mesma regra. [p=0.2] Na do gancho, {b}fatore em cima: xis ao quadrado menos nove é xis mais três, vezes xis menos três. [p=0.3] Embaixo já está {c}xis menos três. [p=0.2] Ele é fator em cima e embaixo: {d}corte. [p=0.2] Sobra {e}xis mais três."),
    dict(id="s07", block="algebrica", text="Teste com dez: [p=0.2] {a}cem menos nove dá noventa e um, [p=0.2] e {b}dez menos três dá sete. [p=0.2] {c}Noventa e um dividido por sete dá treze. [p=0.2] E {d}dez mais três também dá treze."),
    # valor proibido
    dict(id="s08", block="proibido", text="Mas tem um detalhe. [p=0.2] {a}Com xis igual a três, o de baixo vira zero, [p=0.2] e {b}divisão por zero não existe. [p=0.3] A fração original não tem valor ali, [p=0.2] então a resposta completa é {c}xis mais três, para xis diferente de três."),
    # outro exemplo
    dict(id="s09", block="exemplo", text="Mais um: {a}cinco xis mais quinze, dividido por xis ao quadrado menos nove. [p=0.3] {b}Em cima, o cinco em evidência: cinco, abre parênteses, xis mais três, fecha parênteses. [p=0.2] {c}Embaixo, xis mais três, vezes xis menos três. [p=0.3] {d}Corte o xis mais três. [p=0.2] Sobra {e}cinco dividido por xis menos três."),
    dict(id="s10", block="exemplo", text="Agora são {a}dois valores proibidos: [p=0.2] {b}três e menos três, que zeram o de baixo da fração original: [p=0.2] xis menos três zera com três, e xis mais três zera com menos três. [p=0.3] Com dez, a original fica {c}sessenta e cinco dividido por noventa e um. [p=0.2] Dividindo em cima e embaixo por treze, {d}cinco sétimos. [p=0.2] E {e}cinco dividido por dez menos três também é cinco sétimos."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}cortar parcela. [p=0.2] Em {b}xis mais três, dividido por três, [p=0.2] a pessoa corta os três e escreve {c}xis. [p=0.3] Com seis no lugar do xis: [p=0.2] {d}seis mais três dá nove, e nove dividido por três dá três. [p=0.2] O corte daria {e}seis. [p=0.3] O três de cima {f}está somando, não multiplicando: não pode cortar."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, para questão com alternativas: {a}troque o xis por um número fácil. [p=0.2] Calcule a fração original e cada alternativa. [p=0.2] {b}A que der o mesmo valor é a candidata certa."),
    dict(id="s13", block="atalho", text="Funciona porque {a}expressões iguais dão o mesmo resultado para todo valor permitido do xis. [p=0.3] Cuidado: {b}nunca use um valor proibido. [p=0.2] {c}Evite zero e um, que fazem muita alternativa empatar. [p=0.2] E {d}se duas empatarem, teste outro número."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Simplifique {a}xis ao quadrado menos vinte e cinco, dividido por dois xis mais dez. [p=0.2] E diga {b}o valor proibido."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Em cima, diferença de quadrados: xis mais cinco, vezes xis menos cinco. [p=0.2] {b}Embaixo, o dois em evidência: dois, abre parênteses, xis mais cinco, fecha parênteses. [p=0.3] {c}Corte o xis mais cinco. [p=0.2] Resposta: {d}xis menos cinco, dividido por dois."),
    dict(id="s17", block="resposta", text="O proibido é o que zera o de baixo original: [p=0.2] {a}dois, abre parênteses, xis mais cinco, fecha parênteses, vale zero quando xis é menos cinco, [p=0.2] porque menos cinco mais cinco dá zero. [p=0.3] Confira com dez: {b}setenta e cinco dividido por trinta. [p=0.2] Dividindo em cima e embaixo por quinze, {c}cinco dividido por dois. [p=0.2] E {d}dez menos cinco, dividido por dois, também. [p=0.2] Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}fatore em cima e embaixo, [p=0.2] {b}corte só fatores, nunca parcelas, [p=0.2] e {c}anote o valor proibido."),
    dict(id="s19", block="fim", text="Na próxima aula, quem sai de baixo da fração é a raiz: [p=0.2] você vai {a}racionalizar, [p=0.2] e transformar um dividido por raiz de dois em {b}raiz de dois dividido por dois. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
