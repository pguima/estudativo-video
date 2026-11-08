# Estudativo · MAT-PRO-001 — Sequências e lei de formação (Matemática · Progressões).
# Habilidade: achar o 10º termo de aₙ = 3n + 1, continuar aₙ₊₁ = 2aₙ − 1 a partir do primeiro termo e não confundir posição com valor.
# Pré-requisitos: MAT-FUN-003 (f(x) e caminho de volta). Próxima: MAT-PRO-002.
# Questão inédita, criada para esta aula. Plano cartesiano e função afim (MAT-FUN-001, MAT-FUN-009) fora da ficha: não usados. PA citada só como assunto de outra aula.
# Lei aₙ = 3n + 1: a₁ = 4, a₂ = 7, a₃ = 10, a₁₀ = 31, a₁₀₀ = 301 · volta: 3n + 1 = 100 → n = 33 (está) · 3n + 1 = 50 → 3n = 49 → n = 16,33… (não está).
# Recorrência aₙ₊₁ = 2aₙ − 1, a₁ = 3: 3, 5, 9, 17, 33 · sem a₁ não começa.
# Erro: a₁₀ lido como "termo que vale 10": 3n + 1 = 10 → n = 3 (a₃ = 10, não a₁₀).
# Questão: aₙ = 5n − 2 → a₂₀ = 98 · 5n − 2 = 73 → n = 15 · aₙ₊₁ = 2aₙ + 3, a₁ = 1: 1, 5, 13, 29 → a₄ = 29.
# Visual: fila de caixas numeradas com posição embaixo (1º, 2º, 3º…) e valor dentro; aₙ = 3n + 1 com legendas "posição" e "termo";
#   máquina entrada n → saída aₙ (como a máquina da MAT-FUN-003); setas "×2 −1" de uma caixa para a seguinte na recorrência; 49 ÷ 3 riscado.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; aₖ narrado "á índice k" (índice apresentado no s05); aₙ₊₁ "á índice ene mais um" (aₙ + 1 seria "á índice ene, mais um").

TITULO = "Sequências e lei de formação"

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
    dict(id="s01", block="gancho", text="{a}Quatro. [p=0.2] Sete. [p=0.2] Dez. [p=0.2] Treze. [p=0.3] Qual é o próximo? [p=0.2] Fácil: {b}dezesseis. [p=0.3] Agora, qual é {c}o centésimo? [p=0.2] Ninguém quer escrever cem números para descobrir."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha qualquer termo de uma lista como essa sem escrever todos, [p=0.2] separa {b}a posição do valor [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de uma coisa: [p=0.2] {a}efe de xis. [p=0.2] Número nos parênteses, você calcula. [p=0.2] Número depois do igual, você resolve a equação. [p=0.3] Se faltar, procure no canal."),
    # o que é sequência
    dict(id="s04", block="sequencia", text="Uma lista de números {a}em ordem se chama sequência. [p=0.2] Cada número da lista é {b}um termo. [p=0.3] E cada termo tem {c}um lugar na fila: primeiro, segundo, terceiro."),
    dict(id="s05", block="sequencia", text="Para não misturar as duas coisas, a matemática usa {a}uma letra com um número pequeno embaixo, chamado índice. [p=0.2] {b}Á índice um é o primeiro termo, que vale quatro. [p=0.2] {c}Á índice dois é o segundo, que vale sete. [p=0.3] O índice é {d}a posição. [p=0.2] O que a letra vale é {e}o termo."),
    # lei de formação
    dict(id="s06", block="lei", text="Essa sequência tem uma regra: {a}á índice ene igual a três ene mais um. [p=0.2] {b}Ene é a posição. [p=0.2] {c}Á índice ene é o termo que mora nela. [p=0.3] Essa regra se chama {d}lei de formação."),
    dict(id="s07", block="lei", text="É a mesma ideia de efe de xis: [p=0.2] {a}a posição entra, o termo sai. [p=0.3] Ene igual a um: {b}três vezes um dá três, e mais um dá quatro. [p=0.2] Ene igual a dois: {c}três vezes dois dá seis, e mais um dá sete. [p=0.2] Bate com a lista."),
    dict(id="s08", block="lei", text="E o décimo termo? [p=0.2] Troque o ene por dez: {a}três vezes dez dá trinta, [p=0.2] {b}mais um dá trinta e um. [p=0.3] {c}Á índice dez vale trinta e um, [p=0.2] sem escrever os nove termos de antes. [p=0.3] E o centésimo do começo da aula? [p=0.2] {d}Três vezes cem dá trezentos, e mais um dá trezentos e um."),
    # recorrência
    dict(id="s09", block="recorrencia", text="Há outro tipo de regra: a que diz {a}como passar de um termo para o seguinte. [p=0.3] Veja {b}á índice ene mais um, com o ene mais um todo no índice, [p=0.1] igual a dois vezes á índice ene, menos um. [p=0.2] Em palavras: {c}o próximo é o dobro do anterior, menos um."),
    dict(id="s10", block="recorrencia", text="Só que essa regra precisa de um ponto de partida. [p=0.2] Sem {a}o primeiro termo, ela não começa. [p=0.3] Digamos {b}á índice um igual a três. [p=0.2] {c}O dobro de três, menos um, dá cinco. [p=0.2] {d}O dobro de cinco, menos um, dá nove. [p=0.2] {e}O dobro de nove, menos um, dá dezessete. [p=0.2] {f}O próximo dá trinta e três."),
    dict(id="s11", block="recorrencia", text="Aqui, cada termo {a}depende do anterior. [p=0.2] Para chegar no décimo, {b}você passa por todos antes dele."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}trocar posição por valor. [p=0.2] A questão pede {b}á índice dez, em á índice ene igual a três ene mais um. [p=0.2] A pessoa faz {c}três ene mais um igual a dez, [p=0.2] acha {d}ene igual a três, e responde três."),
    dict(id="s13", block="erro", text="Mas ela descobriu outra coisa: {a}a posição do termo que vale dez. [p=0.2] Dez é {b}o terceiro termo, não o décimo. [p=0.3] {c}Número embaixo da letra é posição: troque o ene por ele e calcule. [p=0.2] {d}Valor do termo, depois do igual: resolva a equação."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}o caminho de volta diz se um número está na sequência. [p=0.3] O cem aparece em três ene mais um? [p=0.2] {b}Três ene mais um igual a cem. [p=0.2] {c}Três ene igual a noventa e nove. [p=0.2] {d}Ene igual a trinta e três. [p=0.2] Está, no trigésimo terceiro lugar."),
    dict(id="s15", block="atalho", text="E o cinquenta? [p=0.2] {a}Três ene igual a quarenta e nove. [p=0.2] Quarenta e nove dividido por três {b}não dá exato. [p=0.3] Não existe posição dezesseis e pouco: [p=0.2] {c}o cinquenta não está na sequência."),
    dict(id="s16", block="atalho", text="Funciona porque posição {a}só pode ser um número inteiro, a partir do um. [p=0.3] Não compensa na regra que {b}passa de um termo para o seguinte: [p=0.2] ali não dá para voltar direto, [p=0.2] e o jeito é {c}escrever os termos até passar do número."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Na sequência {a}á índice ene igual a cinco ene menos dois, [p=0.2] {b}quanto vale o vigésimo termo? [p=0.2] E {c}em que posição aparece o setenta e três? [p=0.3] Depois, com {d}á índice um igual a um, [p=0.1] e á índice ene mais um igual a dois vezes á índice ene, mais três, [p=0.2] {e}quanto vale á índice quatro?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Vigésimo termo: posição vinte. [p=0.2] {a}Cinco vezes vinte dá cem, [p=0.2] {b}menos dois dá noventa e oito. [p=0.3] Agora setenta e três é valor: equação. [p=0.2] {c}Cinco ene menos dois igual a setenta e três. [p=0.2] {d}Cinco ene igual a setenta e cinco. [p=0.2] {e}Ene igual a quinze: décimo quinto lugar."),
    dict(id="s20", block="resposta", text="Na segunda, comece pelo um. [p=0.2] {a}O dobro de um, mais três, dá cinco. [p=0.2] {b}O dobro de cinco, mais três, dá treze. [p=0.2] {c}O dobro de treze, mais três, dá vinte e nove. [p=0.3] {d}Á índice quatro vale vinte e nove."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}o número embaixo é a posição, o termo é o valor. [p=0.2] {b}Com a lei em ene, troque e calcule. [p=0.2] {c}Com a regra do anterior, comece do primeiro e vá passo a passo."),
    dict(id="s22", block="fim", text="Na próxima aula, as sequências viram desenho: [p=0.2] {a}uma fileira de quadradinhos feita de palitos. [p=0.3] Você vai descobrir {b}quantos palitos tem a figura cinquenta, sem desenhar nenhuma. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
