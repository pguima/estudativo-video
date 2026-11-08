# Estudativo · MAT-CON-006 — Irracionais e números reais (Matemática · Conjuntos · Conjuntos numéricos).
# Habilidade: separar √16 de √7, reconhecer π = 3,14159… como decimal que não para nem repete (origem: aula de circunferência), colocar 1,4, √2 e 3/2 em ordem na reta e classificar qualquer número dentro de ℝ.
# Pré-requisitos: MAT-CON-005 (fração geratriz), MAT-POT-016 (raízes; √−4 não dá número da reta). Próxima: MAT-CON-007.
# Questão inédita, criada para esta aula. Sem prova de irracionalidade: só o fato, dito como já provado.
# Contas: √16 = 4 · 2² = 4 < 7 < 9 = 3² · √7 = 2,6457… · π = 3,14159… · 1,4² = 1,96 < 2 < 2,25 = 1,5² → 1,4 < √2 < 3/2.
# Atalho (elevar ao quadrado) não vale com negativos: −3 < −2, mas 9 > 4.
# Questão: √25 = 5 · √10 irracional (10 não é quadrado) · 0,1212… = 4/33 · −4 inteiro · 3² = 9 < 10 < 10,24 = 3,2² → 3 < √10 < 3,2.
# Visual: reta numérica de 1 a 2 com 1,4, √2 (≈1,414) e 1,5 marcados; círculos ℕ ⊂ ℤ ⊂ ℚ dentro do retângulo ℝ, com os irracionais na faixa de fora de ℚ.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Irracionais e números reais"

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
    dict(id="s01", block="gancho", text="{a}Raiz quadrada de dezesseis e raiz quadrada de sete. [p=0.3] Parecem da mesma família. [p=0.2] Mas {b}a primeira é um natural, [p=0.2] e a segunda {c}não vira fração de jeito nenhum."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você separa esses números, [p=0.2] põe raízes em ordem na reta [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}toda dízima com período vira fração, [p=0.2] e {c}raiz quadrada, o número positivo que vezes ele mesmo dá o de dentro. [p=0.3] Se faltar alguma, procure no canal."),
    # √16 e √7
    dict(id="s04", block="raizes", text="{a}Raiz de dezesseis é quatro, porque quatro vezes quatro dá dezesseis. [p=0.2] Natural, inteiro e racional. [p=0.3] {b}Raiz de sete não é exata. [p=0.2] Ela fica {c}entre dois e três, [p=0.2] porque dois ao quadrado dá quatro, e três ao quadrado dá nove."),
    dict(id="s05", block="raizes", text="Na calculadora, aparece {a}dois vírgula seis quatro cinco sete, e muito mais. [p=0.3] Esse decimal {b}não acaba e não tem período: [p=0.2] nenhum trecho se repete para sempre. [p=0.3] Como saber, se ninguém vê o fim? [p=0.2] Os matemáticos já provaram que {c}ele não pode ser escrito como fração. [p=0.2] E todo decimal que acaba ou que tem período vira fração. [p=0.3] A prova não cabe nesta aula: aqui, você usa o fato."),
    # irracional
    dict(id="s06", block="irracional", text="Número assim se chama {a}irracional: [p=0.2] {b}não acaba, não se repete e não vira fração. [p=0.3] E vale uma regra: a raiz quadrada de um natural que {c}não é o quadrado de nenhum natural, [p=0.2] como dois, três, cinco ou sete, [p=0.2] {d}é sempre irracional."),
    dict(id="s07", block="irracional", text="O irracional mais famoso é {a}o pi: [p=0.2] {b}três vírgula um quatro um cinco nove, sem fim e sem repetir. [p=0.3] De onde ele vem é {c}assunto da aula de circunferência. [p=0.3] Por enquanto, guarde: {d}três vírgula catorze é só um valor aproximado do pi."),
    # reais
    dict(id="s08", block="reais", text="Juntando racionais e irracionais, você tem {a}os números reais, [p=0.2] com a letra {b}erre. [p=0.3] São {c}todos os pontos da reta numérica. [p=0.3] {d}Quê está contido em erre, [p=0.2] e {e}os irracionais ficam em erre, do lado de fora de quê."),
    dict(id="s09", block="reais", text="E a {a}raiz quadrada de menos quatro? [p=0.2] Você já viu que ela {b}não dá número da reta. [p=0.3] Então {c}ela não pertence a erre."),
    # ordem na reta
    dict(id="s10", block="ordem", text="Ponha em ordem na reta: [p=0.2] {a}um vírgula quatro, [p=0.2] {b}raiz de dois [p=0.2] e {c}três dividido por dois."),
    dict(id="s11", block="ordem", text="{a}Três dividido por dois é um vírgula cinco. [p=0.3] {b}Um vírgula quatro ao quadrado dá um vírgula noventa e seis, [p=0.2] menos que dois. [p=0.2] {c}Um vírgula cinco ao quadrado dá dois vírgula vinte e cinco, [p=0.2] mais que dois. [p=0.3] Então a raiz de dois {d}fica no meio deles."),
    dict(id="s12", block="ordem", text="A ordem é {a}um vírgula quatro, [p=0.2] {b}raiz de dois, [p=0.2] {c}três dividido por dois. [p=0.3] Na reta, cada número tem {d}o seu ponto, racional ou não."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é achar que {a}todo decimal sem fim é irracional. [p=0.3] {b}Zero vírgula quatro quatro quatro não acaba, [p=0.2] mas tem período, [p=0.2] e {c}é quatro nonos: racional. [p=0.3] {d}Irracional é o que não acaba e também não se repete."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho para comparar raiz com decimal: {a}eleve tudo ao quadrado. [p=0.3] Foi o que você fez com a raiz de dois: [p=0.2] {b}a raiz desaparece, [p=0.2] e a comparação fica entre números comuns."),
    dict(id="s15", block="atalho", text="Funciona porque, entre números positivos, {a}o maior tem o quadrado maior. [p=0.3] {b}Não compensa com negativos. [p=0.2] {c}Menos três é menor que menos dois, [p=0.2] mas o quadrado de menos três é nove, [p=0.2] {d}maior que quatro, o quadrado de menos dois."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Entre {a}raiz de vinte e cinco, [p=0.2] {b}raiz de dez, [p=0.2] {c}zero vírgula um dois um dois, sem fim, [p=0.2] e {d}menos quatro, [p=0.2] {e}qual é irracional? [p=0.3] Depois, {f}ponha em ordem: três, raiz de dez e três vírgula dois."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Raiz de vinte e cinco é cinco: natural. [p=0.2] {b}A dízima tem período: é quatro trinta e três avos, racional. [p=0.2] {c}Menos quatro é inteiro. [p=0.3] {d}Dez fica entre nove e dezesseis: não é o quadrado de nenhum natural. [p=0.2] {e}Raiz de dez é a irracional."),
    dict(id="s19", block="resposta", text="Para a ordem, eleve ao quadrado. [p=0.2] {a}Três ao quadrado, nove. [p=0.2] {b}Raiz de dez ao quadrado, dez. [p=0.2] {c}Três vírgula dois ao quadrado, dez vírgula vinte e quatro. [p=0.3] Ordem: {d}três, raiz de dez, três vírgula dois."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}racional vira fração, [p=0.2] {b}irracional não acaba e não se repete [p=0.2] e {c}os reais são todos os pontos da reta."),
    dict(id="s21", block="fim", text="Na próxima aula, você escreve {a}pedaços inteiros da reta, [p=0.2] como todos os reais entre dois e cinco, [p=0.2] usando {b}colchetes. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
