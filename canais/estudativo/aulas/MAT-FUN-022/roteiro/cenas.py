# Estudativo · MAT-FUN-022 — Estudo do sinal e inequação do 2º grau (Matemática · Funções · Função quadrática).
# Habilidade: resolver x² − 5x + 6 < 0 desenhando a parábola e responder ]2, 3[.
# Pré-requisitos: MAT-FUN-017 (raízes e os três casos do delta no gráfico), MAT-CON-007 (intervalos e colchetes). Próxima: MAT-FUN-023.
# Questão inédita, criada para esta aula. Raízes por Bhaskara, reaproveitando os exemplos da MAT-FAT-008 (x² − 5x + 6 e −x² + 2x + 3)
#   e da MAT-FAT-009 (x² + 2x + 5, delta −16). União (∪) fora da ficha: respostas de dois pedaços ditas com "ou".
# Contas: x² − 5x + 6: Δ = 1, raízes 2 e 3 · f(2,5) = 6,25 − 12,5 + 6 = −0,25 · < 0 → ]2, 3[ · ≤ 0 → [2, 3] · > 0 → x < 2 ou x > 3.
#   −x² + 2x + 3 ≥ 0: raízes −1 e 3, boca para baixo → [−1, 3] · x² + 2x + 5: > 0 para todo x real, < 0 para nenhum.
# Erro: "x < 2 ou x < 3" (copiar o sinal) inclui o 0, mas f(0) = 6 > 0.
# Atalho: fora das raízes, sinal do a; entre elas, o contrário · não vale com Δ ≤ 0.
# Questão: −x² + 6x − 8 > 0: Δ = 36 − 32 = 4, raízes 2 e 4, a < 0 → ]2, 4[ · x² − 9 ≥ 0: raízes −3 e 3 → x ≤ −3 ou x ≥ 3.
# Visual: E.plano com E.curva de x² − 5x + 6 (x de 0,5 a 4,5); trecho entre 2 e 3 em vermelho abaixo do eixo (E.area) e trechos
#   de fora em verde; reta numérica com "+ 2 − 3 +" e o intervalo ]2, 3[ (E.intervalo); depois −x² + 2x + 3 com [−1, 3] e
#   x² + 2x + 5 inteira acima do eixo.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á".

TITULO = "Estudo do sinal e inequação do 2º grau"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado menos cinco xis mais seis, menor que zero. [p=0.3] Muita gente resolve como equação, {b}acha dois e três e para. [p=0.3] Mas a resposta não são números soltos: [p=0.2] é {c}um pedaço inteiro da reta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve inequações do segundo grau só olhando a parábola, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}achar as raízes, com delta e Bhaskara; [p=0.2] {c}o sinal do á, que diz para onde a parábola abre; [p=0.2] e {d}intervalo, com o colchete abraçando quando a ponta entra. [p=0.3] Se faltar alguma, procure no canal."),
    # sinal
    dict(id="s04", block="sinal", text="Estudar o sinal é perguntar {a}onde a função é positiva, zero ou negativa. [p=0.2] No gráfico, é fácil. [p=0.2] {b}Acima do eixo xis, positiva. [p=0.2] {c}Em cima do eixo, zero. [p=0.2] {d}Abaixo do eixo, negativa."),
    # método
    dict(id="s05", block="metodo", text="O método tem {a}três passos. [p=0.2] {b}Passo um: as raízes. [p=0.2] Em xis ao quadrado menos cinco xis mais seis, você já fez a conta na aula de Bhaskara: [p=0.2] {c}delta um, raízes dois e três."),
    dict(id="s06", block="metodo", text="{a}Passo dois: a boca. [p=0.2] Á vale um, positivo: {b}abre para cima. [p=0.3] {c}Passo três: um desenho rápido. [p=0.2] {d}Um sorriso cortando o eixo no dois e no três. [p=0.2] A altura exata não importa: {e}só importa de que lado do eixo a curva está."),
    dict(id="s07", block="metodo", text="Hora de ler o desenho. [p=0.2] {a}Entre dois e três, a curva está abaixo do eixo: negativa. [p=0.2] {b}Antes do dois e depois do três, está acima: positiva. [p=0.3] Confira com {c}dois vírgula cinco. [p=0.2] Ao quadrado, dá seis vírgula vinte e cinco. [p=0.2] Tire cinco vezes dois vírgula cinco, que é doze vírgula cinco. [p=0.2] Some seis. [p=0.2] Dá {d}menos zero vírgula vinte e cinco. [p=0.2] Negativo: bateu."),
    dict(id="s08", block="metodo", text="A pergunta pedia {a}menor que zero: o pedaço de baixo. [p=0.2] Sem tracinho, {b}as pontas ficam de fora, porque nelas a função vale zero. [p=0.3] Resposta: {c}o intervalo aberto de dois a três."),
    dict(id="s09", block="metodo", text="Se fosse {a}menor ou igual a zero, as pontas entram: [p=0.2] {b}fechado de dois a três. [p=0.3] E se fosse {c}maior que zero, a resposta seria o lado de cima: [p=0.2] {d}xis menor que dois, ou xis maior que três."),
    # outros casos
    dict(id="s10", block="casos", text="Com á negativo, a boca vira. [p=0.2] Veja {a}menos xis ao quadrado mais dois xis mais três, maior ou igual a zero. [p=0.2] Na aula de Bhaskara, as raízes deram {b}menos um e três. [p=0.3] Abre para baixo: {c}entre as raízes, a curva fica acima do eixo. [p=0.2] Com o tracinho, {d}fechado de menos um a três."),
    dict(id="s11", block="casos", text="E sem raízes? [p=0.2] {a}Xis ao quadrado mais dois xis mais cinco tem delta menos dezesseis. [p=0.2] Abre para cima e {b}nunca toca o eixo: fica inteira acima dele. [p=0.3] Maior que zero vale {c}para todo xis real. [p=0.2] Menor que zero, {d}para nenhum."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}copiar o sinal da inequação para as raízes. [p=0.2] Em xis ao quadrado menos cinco xis mais seis, menor que zero, [p=0.2] a pessoa escreve {b}xis menor que dois, ou xis menor que três. [p=0.3] Teste o zero, que estaria nessa resposta: [p=0.2] {c}zero menos zero mais seis dá seis. [p=0.2] {d}Positivo. [p=0.2] {e}Quem decide o lado é o desenho, não o sinal escrito."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, sem desenho: [p=0.2] {a}fora das raízes, a função tem o mesmo sinal do á. [p=0.2] {b}Entre as raízes, o sinal contrário. [p=0.3] Em xis ao quadrado menos cinco xis mais seis, {c}o á é positivo: [p=0.2] entre dois e três, {d}negativo."),
    dict(id="s14", block="atalho", text="Funciona porque {a}as pontas da parábola seguem o á: [p=0.2] no sorriso, as pontas sobem e o miolo afunda abaixo do eixo. [p=0.3] {b}Não vale quando o delta é zero ou negativo: [p=0.2] aí não existe pedaço entre as raízes, [p=0.2] e {c}a parábola fica de um lado só do eixo, com o sinal do á."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Resolva {a}menos xis ao quadrado mais seis xis menos oito, maior que zero. [p=0.3] E também {b}xis ao quadrado menos nove, maior ou igual a zero."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Na primeira, {a}delta: trinta e seis menos trinta e dois dá quatro. [p=0.2] {b}Raízes dois e quatro. [p=0.2] Á negativo: {c}entre as raízes vem o sinal contrário, positivo. [p=0.2] Resposta: {d}o intervalo aberto de dois a quatro."),
    dict(id="s18", block="resposta", text="Na segunda, {a}xis ao quadrado igual a nove dá menos três e três. [p=0.2] Á positivo: {b}fora das raízes, positivo. [p=0.2] Com o tracinho, as pontas entram: [p=0.2] {c}xis menor ou igual a menos três, ou xis maior ou igual a três."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}ache as raízes, [p=0.2] {b}veja a boca [p=0.2] e {c}pegue o pedaço que a pergunta pede."),
    dict(id="s20", block="fim", text="Na próxima aula, a desigualdade vem em pedaços: [p=0.2] {a}xis menos um, vezes xis mais dois, dividido por xis menos três, maior ou igual a zero. [p=0.3] Você resolve com {b}o quadro de sinais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
