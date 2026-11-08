# Estudativo · MAT-PRO-002 — Padrões em figuras (Matemática · Progressões).
# Habilidade: descobrir quantos palitos tem a figura 50 de uma fileira de quadradinhos, contando o que se repete e escrevendo a lei.
# Pré-requisitos: MAT-PRO-001 (lei de formação, posição e termo). Próxima: MAT-PRO-003.
# Questão inédita, criada para esta aula. Sem PA nem termo geral (MAT-PRO-004) e sem distributiva (MAT-EQU-004 fora da ficha): as duas leituras são conferidas só com números.
# Quadradinhos: figura n tem n quadradinhos · palitos 4, 7, 10, 13 · lei P = 3n + 1 (1 palito de partida + 3 por quadradinho) · figura 50: 150 + 1 = 151.
# Outra leitura: 4 do primeiro + 3 × 49 = 4 + 147 = 151.
# Erro: 4 × 50 = 200 conta duas vezes cada um dos 49 palitos de divisa → 200 − 49 = 151.
# Atalho: aumento constante 3 → 3n + ? · figura 1: 3 + ? = 4 → ? = 1 · não compensa: quadrados de quadradinhos 1, 4, 9 contando quadradinhos, não palitos (aumentos 3, 5: não é constante; n × n).
# Questão: fileira de hexágonos 6, 11, 16 → aumento 5 → 5n + 1 · figura 40: 200 + 1 = 201 · 91 palitos: 5n + 1 = 91 → 5n = 90 → n = 18.
# Visual: figuras 1, 2 e 3 de palitos (quadradinhos lado a lado) com os palitos novos acesos na cor da matéria; palito de partida destacado;
#   tabela figura | palitos com "+3" entre as linhas; palitos de divisa piscando em vermelho no erro; quadrados 1×1, 2×2 e 3×3 no "não compensa";
#   fileira de hexágonos 1, 2 e 3 na questão.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; P narrado "pê", n "ene".

TITULO = "Padrões em figuras"

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
    dict(id="s01", block="gancho", text="{a}Um quadradinho de palitos usa quatro palitos. [p=0.2] Quantos palitos tem {b}uma fileira de cinquenta quadradinhos? [p=0.3] Quem responde {c}duzentos erra. [p=0.2] São {d}cento e cinquenta e um."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você descobre de onde vem esse número, [p=0.2] escreve a lei de qualquer fileira de figuras [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de uma coisa: [p=0.2] {a}lei de formação. [p=0.2] Ene é a posição, [p=0.2] e o termo é o que sai quando você troca o ene por um número. [p=0.3] Se faltar, procure no canal."),
    # contar
    dict(id="s04", block="contar", text="Desenhe as primeiras figuras. [p=0.2] {a}Figura um: um quadradinho, quatro palitos. [p=0.2] {b}Figura dois: dois quadradinhos lado a lado. [p=0.2] Conte: {c}sete palitos, não oito. [p=0.3] O palito do meio {d}é dividido: serve ao quadradinho da esquerda e ao da direita."),
    dict(id="s05", block="contar", text="{a}Figura três: dez palitos. [p=0.2] Monte a tabela: {b}quatro, depois sete, depois dez. [p=0.3] De uma figura para a próxima, entram sempre {c}três palitos novos: [p=0.2] {d}um em cima, um embaixo e um fechando à direita. [p=0.2] O da esquerda {e}já estava lá."),
    # lei
    dict(id="s06", block="lei", text="Agora olhe a fileira assim: [p=0.2] {a}um palito de partida, em pé, na ponta esquerda. [p=0.2] E cada quadradinho {b}traz três palitos. [p=0.3] Na figura ene, são ene quadradinhos. [p=0.2] Então {c}pê igual a três ene mais um. [p=0.2] Pê é o número de palitos."),
    dict(id="s07", block="lei", text="Teste antes de confiar: [p=0.2] {a}na figura um, três mais um dá quatro. [p=0.2] {b}Na figura dois, seis mais um dá sete. [p=0.2] Bateu. [p=0.3] E repare: é {c}a mesma lei da aula passada, três ene mais um, [p=0.2] agora com cara de desenho."),
    dict(id="s08", block="lei", text="Figura cinquenta: {a}três vezes cinquenta dá cento e cinquenta, [p=0.2] {b}mais um dá cento e cinquenta e um palitos."),
    dict(id="s09", block="lei", text="Dá para ver de outro jeito. [p=0.2] {a}O primeiro quadradinho usa quatro. [p=0.2] {b}Os outros quarenta e nove trazem três cada um, [p=0.2] e quarenta e nove vezes três dá cento e quarenta e sete. [p=0.2] {c}Quatro mais cento e quarenta e sete dá cento e cinquenta e um. [p=0.3] Olhar diferente, {d}mesma contagem."),
    # erro
    dict(id="s10", block="erro", text="O erro comum é {a}multiplicar quatro por cinquenta. [p=0.2] Dá {b}duzentos, [p=0.2] como se cada quadradinho tivesse os seus quatro palitos só para ele."),
    dict(id="s11", block="erro", text="Mas entre dois quadradinhos vizinhos há {a}um palito de divisa, contado duas vezes. [p=0.2] Numa fileira de cinquenta, são {b}quarenta e nove divisas. [p=0.2] {c}Duzentos menos quarenta e nove dá cento e cinquenta e um. [p=0.2] Bate com a lei."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}o aumento vira o número do ene. [p=0.3] A tabela sobe {b}de três em três? [p=0.2] Então a lei começa com {c}três ene. [p=0.2] Falta só o número solto. [p=0.2] Na figura um, {d}três ene dá três, mas a figura tem quatro. [p=0.2] Falta um: {e}três ene mais um."),
    dict(id="s13", block="atalho", text="Funciona porque, a cada figura, {a}o ene sobe um e o três ene sobe três, [p=0.2] igual aos palitos. [p=0.2] O número solto só {b}acerta o ponto de partida. [p=0.3] Não compensa quando o aumento {c}muda de figura para figura. [p=0.2] Conte os quadradinhos de quadrados de um por um, dois por dois e três por três: [p=0.2] {d}um, depois quatro, depois nove. [p=0.2] Sobe três, depois cinco. [p=0.2] Aí a lei é outra: {e}ene vezes ene."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Agora é {a}uma fileira de hexágonos, figuras de seis lados, feitas de palitos. [p=0.2] Hexágonos vizinhos {b}dividem um palito. [p=0.2] As figuras têm {c}seis palitos, depois onze, depois dezesseis. [p=0.3] {d}Escreva a lei, [p=0.2] diga {e}quantos palitos tem a figura quarenta [p=0.2] e {f}qual figura usa noventa e um palitos."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=0.3] Pista: comece pelo que entra de uma figura para a seguinte. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] De seis para onze, e de onze para dezesseis: {a}sobe cinco. [p=0.2] A lei começa com {b}cinco ene. [p=0.2] Na figura um, cinco ene dá cinco, mas são seis: {c}pê igual a cinco ene mais um."),
    dict(id="s17", block="resposta", text="Figura quarenta: {a}cinco vezes quarenta dá duzentos, e mais um dá duzentos e um palitos. [p=0.3] Noventa e um palitos é valor: {b}cinco ene mais um igual a noventa e um. [p=0.2] {c}Cinco ene igual a noventa. [p=0.2] {d}Ene igual a dezoito: figura dezoito."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}conte o que entra de uma figura para a próxima. [p=0.2] {b}Esse aumento multiplica o ene, [p=0.2] e {c}a figura um acerta o resto da lei."),
    dict(id="s19", block="fim", text="Na próxima aula, o padrão {a}dá voltas: [p=0.2] letras que se repetem, dias da semana. [p=0.3] Você vai descobrir {b}a letra da posição dois mil e vinte e seis [p=0.2] e {c}o dia da semana daqui a cem dias, só com o resto de uma divisão. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
