# Estudativo · MAT-CON-002 — União, interseção, diferença e complementar (Matemática · Conjuntos).
# Habilidade: calcular A ∪ B, A ∩ B, A − B e o complementar de A para A = {1, 2, 3, 4} e B = {3, 4, 5}, sem confundir 'e' com 'ou'.
# Pré-requisitos: MAT-CON-001 (pertence, contido, vazio). Próxima: MAT-CON-003.
# Questão inédita, criada para esta aula. Universo do exemplo: U = {1, 2, 3, 4, 5, 6}.
# Contas: A ∩ B = {3, 4} · A ∪ B = {1, 2, 3, 4, 5} · A − B = {1, 2} · B − A = {5} · complementar de A = {5, 6}.
# Erro: "ou" lido como um ou outro, só → {1, 2, 5}. Questão: U = {2, 4, 6, 8, 10, 12}, A = {2, 4, 6, 8}, B = {4, 8, 12}:
#   A ∩ B = {4, 8} · B − A = {12} · A ∪ B = {2, 4, 6, 8, 12} · complementar de B = {2, 6, 10}.
# Visual: diagrama de Venn de 2 conjuntos (E.venn) com os números nas regiões; cada operação pinta sua região.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "União, interseção, diferença e complementar"

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
    dict(id="s01", block="gancho", text="Uma pesquisa pergunta: [p=0.2] {a}quem toma café ou chá? [p=0.3] Quem toma {b}café e também chá entra na conta? [p=0.3] Na matemática, {c}entra. [p=0.2] E essa palavrinha ou derruba muita gente na prova."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você faz as quatro operações com conjuntos [p=0.2] sem trocar a palavra e pela palavra ou, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}escrever um conjunto entre chaves, [p=0.2] {c}o símbolo de pertence [p=0.2] e {d}o conjunto vazio. [p=0.3] Se faltar alguma, procure no canal."),
    # diagrama
    dict(id="s04", block="venn", text="Vamos usar dois conjuntos. [p=0.2] {a}O conjunto á tem um, dois, três e quatro. [p=0.2] {b}O conjunto bê tem três, quatro e cinco. [p=0.3] No desenho, cada conjunto é {c}um círculo, [p=0.2] e {d}o três e o quatro ficam na parte em comum. [p=0.3] Esse desenho se chama {e}diagrama de Venn."),
    # interseção
    dict(id="s05", block="intersecao", text="A {a}interseção de á e bê é o que está {b}em á e em bê, ao mesmo tempo. [p=0.3] É a parte em comum: {c}três e quatro. [p=0.3] O símbolo é {d}um U de cabeça para baixo."),
    # união
    dict(id="s06", block="uniao", text="A {a}união é o que está {b}em á ou em bê. [p=0.3] Na matemática, esse ou {c}inclui quem está em ambos. [p=0.3] Junte tudo, sem repetir: {d}um, dois, três, quatro e cinco. [p=0.3] O símbolo é {e}um U aberto para cima, como um copo que junta tudo."),
    # diferença
    dict(id="s07", block="diferenca", text="A {a}diferença, á menos bê, é o que está {b}em á e não está em bê. [p=0.3] Comece pelo conjunto á e {c}risque o que também está em bê. [p=0.2] Sobram {d}um e dois. [p=0.3] A ordem importa: {e}bê menos á deixa só o cinco."),
    # complementar
    dict(id="s08", block="complementar", text="Falta o complementar. [p=0.2] Ele precisa de um {a}universo: o conjunto de tudo que está em jogo na questão. [p=0.3] Aqui, o universo tem {b}os números de um até seis."),
    dict(id="s09", block="complementar", text="O {a}complementar de á é o que está no universo e {b}fora de á. [p=0.3] Tire do universo o um, o dois, o três e o quatro. [p=0.2] Sobram {c}cinco e seis. [p=0.3] Na prova, ele aparece como {d}a letra com um traço em cima, [p=0.2] ou com {e}um cê pequeno no alto."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}tirar da união quem está em ambos. [p=0.2] A pessoa lê a palavra ou como um ou outro, só um, [p=0.2] e escreve {b}um, dois e cinco. [p=0.3] Mas o três está em á, [p=0.2] então {c}ele está em á ou em bê. [p=0.2] O quatro também. [p=0.2] Ambos entram."),
    dict(id="s11", block="erro", text="Guarde assim: [p=0.2] {a}a palavra e exige ambos ao mesmo tempo. [p=0.2] {b}A palavra ou aceita pelo menos um."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}comece pela interseção. [p=0.3] Com {b}o três e o quatro na mão, o resto sai sozinho. [p=0.2] {c}Á menos bê é o conjunto á, tirando a interseção: um e dois. [p=0.2] {d}Bê menos á, pelo mesmo caminho: cinco. [p=0.2] E {e}a união junta os pedaços: um, dois, três, quatro e cinco."),
    dict(id="s13", block="atalho", text="Funciona porque o diagrama tem {a}pedaços que não se misturam: [p=0.2] só á, a parte em comum, e só bê. [p=0.3] {b}Não compensa quando um conjunto está inteiro dentro do outro: [p=0.2] aí a interseção é {c}o conjunto de dentro, [p=0.2] e a união é {d}o conjunto de fora, direto."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] O universo tem {a}dois, quatro, seis, oito, dez e doze. [p=0.2] {b}O conjunto á tem dois, quatro, seis e oito. [p=0.2] {c}O conjunto bê tem quatro, oito e doze. [p=0.3] Calcule {d}a união, a interseção, bê menos á [p=0.2] e {e}o complementar de bê."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá, começando pela interseção: {a}quatro e oito. [p=0.3] {b}Bê menos á: tirando a interseção, sobra só o doze. [p=0.3] {c}União: dois, quatro, seis, oito e doze, sem repetir nada."),
    dict(id="s17", block="resposta", text="Complementar de bê: o que está no universo e fora de bê. [p=0.2] {a}Dois, seis e dez. [p=0.3] Repare no dez: {b}ele não está em nenhum dos conjuntos, [p=0.2] mas está no universo, e entra."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}a palavra e pede interseção, a parte em comum. [p=0.2] {b}A palavra ou pede união, tudo junto. [p=0.2] {c}Menos é tirar o que está no outro. [p=0.2] E {d}complementar é o que falta para o universo."),
    dict(id="s19", block="fim", text="Na próxima aula, o diagrama de Venn resolve problemas, [p=0.2] como descobrir {a}quantos alunos não praticam nenhum esporte, [p=0.2] com dois e até {b}três conjuntos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
