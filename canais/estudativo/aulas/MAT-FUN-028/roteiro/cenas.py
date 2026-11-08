# Estudativo · MAT-FUN-028 — Sistema de inequações (Matemática · Funções · Função quadrática).
# Habilidade: achar os x que valem ao mesmo tempo em x − 1 > 0 e x² − 5x + 6 < 0, resolvendo cada uma e empilhando as retas até chegar a ]2, 3[.
# Pré-requisitos: MAT-CON-008 (interseção empilhando retas; maior dos começos e menor dos fins), MAT-FUN-022 (inequação do 2º grau). Próxima: MAT-FUN-024.
# Questão inédita, criada para esta aula. Inequação do 1º grau: MAT-EQU-015 (vira o sinal ao multiplicar ou dividir por negativo).
# Contas: x − 1 > 0 → ]1, +∞[ · x² − 5x + 6 < 0 → ]2, 3[ · interseção ]2, 3[.
#   Exemplo 2: x² − 6x + 5 ≤ 0: Δ = 36 − 20 = 16, raízes 1 e 5 → [1, 5] · 2x − 6 > 0 → x > 3 · interseção ]3, 5].
# Erro: união ]1, +∞[ · x = 10: 10 − 1 = 9 > 0, mas 100 − 50 + 6 = 56, não é < 0.
# Atalho (da MAT-CON-008): maior dos começos, menor dos fins · não compensa com resposta de dois pedaços (x² − 9 > 0: x < −3 ou x > 3).
# Questão: x² − x − 6 ≤ 0: Δ = 1 + 24 = 25, raízes 3 e −2 → [−2, 3] · 3 − x < 4 → −x < 1 → x > −1 · interseção ]−1, 3] ·
#   inteiros 0, 1, 2, 3 → quatro (o −1 fica de fora).
# Visual: chave do sistema; retas empilhadas com E.reta + E.intervalo (]1, +∞[ sobre ]2, 3[), faixa vertical na parte comum e reta-resposta;
#   E.plano com a parábola de x² − 5x + 6 ao lado, se couber; segundo sistema [1, 5] sobre ]3, +∞[ → ]3, 5]; na resposta, os inteiros 0 a 3 marcados.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á".

TITULO = "Sistema de inequações"

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
    dict(id="s01", block="gancho", text="Um número precisa obedecer {a}duas condições ao mesmo tempo: [p=0.2] {b}xis menos um maior que zero, [p=0.2] e {c}xis ao quadrado menos cinco xis mais seis menor que zero. [p=0.3] Quem resolve cada uma e {d}junta tudo erra. [p=0.2] Aqui, quem manda é a palavra {e}e."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve um sistema de inequações empilhando as respostas, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas. [p=0.2] {b}Inequação do primeiro grau: faça o mesmo nos dois lados, e vire o sinal ao dividir por negativo. [p=0.2] {c}Inequação do segundo grau: raízes, boca e o pedaço certo. [p=0.2] E {d}interseção de intervalos: empilhar as retas e ficar com o que está pintado em todas. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="sistema", text="Um {a}sistema de inequações é uma lista de inequações que precisam valer {b}ao mesmo tempo. [p=0.2] Elas vêm unidas por uma chave. [p=0.3] Ao mesmo tempo é a palavra {c}e. [p=0.2] E a palavra e, em intervalos, é {d}interseção."),
    # método
    dict(id="s05", block="metodo", text="O método tem {a}três passos. [p=0.2] {b}Passo um: resolva cada inequação sozinha. [p=0.3] Primeira: {c}xis menos um maior que zero. [p=0.2] {d}Some um de cada lado: xis maior que um. [p=0.2] Em intervalo: {e}de um até mais infinito, aberto nas pontas."),
    dict(id="s06", block="metodo", text="Segunda: {a}xis ao quadrado menos cinco xis mais seis, menor que zero. [p=0.2] Você resolveu essa na aula de inequação do segundo grau: [p=0.2] {b}raízes dois e três, boca para cima, [p=0.2] e o pedaço de baixo: {c}o intervalo aberto de dois a três."),
    dict(id="s07", block="metodo", text="{a}Passo dois: empilhe as respostas, com os números alinhados. [p=0.2] {b}Em cima, tudo depois do um. [p=0.2] {c}Embaixo, o pedaço entre dois e três. [p=0.3] {d}Passo três: fique só com o que está pintado em ambas as retas."),
    dict(id="s08", block="metodo", text="Entre dois e três, {a}ambas estão pintadas. [p=0.2] Nas pontas, {b}o dois e o três têm bolinha aberta na reta de baixo: ficam de fora. [p=0.3] Resposta: {c}o intervalo aberto de dois a três."),
    dict(id="s09", block="metodo", text="Repare: {a}a primeira condição não tirou nada daqui. [p=0.2] Todo número entre dois e três {b}já é maior que um. [p=0.3] Mas nem sempre é assim. [p=0.2] Veja outro sistema."),
    # segundo sistema
    dict(id="s10", block="outro", text="{a}Xis ao quadrado menos seis xis mais cinco, menor ou igual a zero, [p=0.2] e {b}dois xis menos seis, maior que zero. [p=0.3] Na primeira, o delta dá {c}trinta e seis menos vinte: dezesseis. [p=0.2] As raízes são um e cinco. [p=0.2] Boca para cima, pedaço de baixo, com o tracinho: {d}fechado de um a cinco."),
    dict(id="s11", block="outro", text="Na segunda, {a}some seis: dois xis maior que seis. [p=0.2] {b}Divida por dois: xis maior que três. [p=0.3] Empilhando, o pintado em ambas vai {c}do três ao cinco. [p=0.2] {d}O três fica de fora, porque a segunda não pega. [p=0.2] {e}O cinco entra, porque está em ambas. [p=0.3] Resposta: {f}aberto no três, fechado no cinco."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}juntar as respostas em vez de cruzar. [p=0.2] No primeiro sistema, juntar dá {b}tudo depois do um. [p=0.3] Teste o {c}dez. [p=0.2] Dez menos um dá nove, positivo: tudo bem. [p=0.2] Mas {d}cem menos cinquenta mais seis dá cinquenta e seis, que não é menor que zero. [p=0.2] {e}O dez falha na segunda. [p=0.2] {f}Sistema é e: interseção, nunca união."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}quando cada inequação dá um pedaço só, [p=0.2] a resposta vai {b}do maior dos começos ao menor dos fins. [p=0.3] No segundo sistema, os começos são um e três: {c}o maior é três. [p=0.2] Os fins são cinco e mais infinito: {d}o menor é cinco. [p=0.2] Do três ao cinco, e as pontas você confere."),
    dict(id="s14", block="atalho", text="Funciona porque, para valer em ambas, o número precisa {a}ter passado de cada começo [p=0.2] e {b}não ter chegado a nenhum fim. [p=0.3] {c}Não compensa quando uma das respostas tem dois pedaços, [p=0.2] como {d}xis ao quadrado menos nove, maior que zero: [p=0.2] menor que menos três, ou maior que três. [p=0.2] Aí, {e}empilhe as retas."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Quantos números inteiros satisfazem, ao mesmo tempo, [p=0.2] {b}xis ao quadrado menos xis menos seis, menor ou igual a zero, [p=0.2] e {c}três menos xis, menor que quatro?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Na primeira, á vale um, bê vale menos um e cê vale menos seis. [p=0.2] {a}Delta: um mais vinte e quatro dá vinte e cinco. [p=0.2] Menos bê é um. [p=0.2] {b}Com mais: um mais cinco, dividido por dois, dá três. [p=0.2] {c}Com menos: um menos cinco, dividido por dois, dá menos dois. [p=0.3] Boca para cima, pedaço de baixo, com tracinho: {d}fechado de menos dois a três."),
    dict(id="s18", block="resposta", text="Na segunda, {a}tire três de cada lado: menos xis menor que um. [p=0.2] {b}Multiplique por menos um e vire o sinal: xis maior que menos um. [p=0.3] Pelo atalho, o maior dos começos é {c}menos um, [p=0.2] e o menor dos fins é {d}três. [p=0.2] Aberto no menos um, fechado no três."),
    dict(id="s19", block="resposta", text="Os inteiros desse pedaço são {a}o zero, [p=0.2] o um, [p=0.2] o dois [p=0.2] e o três. [p=0.2] {b}Quatro números inteiros. [p=0.3] Quem contou o menos um {c}esqueceu que a ponta é aberta."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}resolva cada inequação, [p=0.2] {b}empilhe as retas [p=0.2] e {c}fique com o que está pintado em todas."),
    dict(id="s21", block="fim", text="Na próxima aula, é hora de praticar {a}a função quadrática inteira: [p=0.2] {b}raízes e vértice, [p=0.2] {c}máximo e mínimo em problemas [p=0.2] e {d}o sinal da parábola. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
