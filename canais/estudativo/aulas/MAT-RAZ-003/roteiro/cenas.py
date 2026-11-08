# Estudativo · MAT-RAZ-003 — O truque do k (Matemática · Razão e Proporção).
# Habilidade: achar dois números na razão 3 para 5 que somam 64, escrevendo 3k + 5k = 64.
# Pré-requisitos: MAT-RAZ-002 (proporção), MAT-EQU-013 (montar equação do problema). Próxima: MAT-RAZ-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. "Cá" é como a voz lê a letra k.

TITULO = "O truque do k"

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
    dict(id="s01", block="gancho", text="Dois números estão {a}na razão três para cinco [p=0.2] e {b}somam sessenta e quatro. [p=0.3] Quais são eles? [p=0.3] {c}Três e cinco? [p=0.2] Somam oito, não sessenta e quatro. [p=0.2] Com uma letra só, isso sai em uma linha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você divide qualquer total numa razão dada, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o que é razão e proporção, [p=0.2] e {c}transformar um problema em equação. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="Razão três para cinco quer dizer: {a}a cada três de um, cinco do outro. [p=0.3] Pense em {b}pacotinhos iguais. [p=0.2] O primeiro número é {c}três pacotinhos. [p=0.2] O segundo, {d}cinco pacotinhos do mesmo tamanho."),
    dict(id="s05", block="ideia", text="Por que não montar uma proporção e usar a cruz? [p=0.2] Porque aqui {a}nenhum dos números é conhecido, [p=0.2] e a cruz só acha um número que falta. [p=0.3] Não sabemos o tamanho do pacotinho. [p=0.2] Então ele vira uma letra: {b}cá. [p=0.3] O primeiro número é {c}três cá. [p=0.2] O segundo, {d}cinco cá. [p=0.3] E a razão continua certa: {e}três cá para cinco cá é três para cinco."),
    # resolver
    dict(id="s06", block="resolver", text="Agora o problema vira equação. [p=0.2] Juntos, eles somam sessenta e quatro: [p=0.2] {a}três cá mais cinco cá igual a sessenta e quatro. [p=0.3] Juntando, {b}oito cá igual a sessenta e quatro. [p=0.2] {c}Divida por oito: cá igual a oito."),
    dict(id="s07", block="resolver", text="Cada pacotinho vale oito. [p=0.2] Mas a pergunta pede os números. [p=0.3] {a}Três vezes oito dá vinte e quatro. [p=0.2] {b}Cinco vezes oito dá quarenta."),
    dict(id="s08", block="resolver", text="Conferindo: {a}vinte e quatro mais quarenta dá sessenta e quatro. [p=0.2] E {b}vinte e quatro quarenta avos, dividindo por oito, [p=0.2] dá {c}três quintos. [p=0.2] Bateu."),
    dict(id="s09", block="resolver", text="O truque também serve quando o problema dá {a}a diferença. [p=0.2] Se o maior tem dezesseis a mais que o menor: [p=0.3] {b}cinco cá menos três cá igual a dezesseis. [p=0.2] {c}Dois cá igual a dezesseis, cá igual a oito. [p=0.2] Os mesmos {d}vinte e quatro e quarenta. [p=0.3] A diferença entre cinco cá e três cá são {e}dois pacotinhos."),
    dict(id="s10", block="tres", text="E com {a}três números? [p=0.2] Igual. [p=0.2] Na razão {b}dois para três para cinco, com soma cinquenta: [p=0.2] {c}dois cá mais três cá mais cinco cá, dez cá. [p=0.2] {d}Cá igual a cinco. [p=0.3] Os números são {e}dez [p=0.2] quinze [p=0.2] e vinte e cinco."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}confundir três para cinco com três quintos do total. [p=0.3] A pessoa faz {b}três quintos de sessenta e quatro: [p=0.2] {c}trinta e oito vírgula quatro. [p=0.2] Sobram {d}vinte e cinco vírgula seis para o outro."),
    dict(id="s12", block="erro", text="Mas o primeiro devia ser {a}o menor, e saiu maior. [p=0.3] Três para cinco não é três de cinco partes do total. [p=0.2] O total tem {b}três mais cinco dá oito partes. [p=0.2] O primeiro é {c}três oitavos do total."),
    # atalho
    dict(id="s13", block="atalho", text="Daí sai o atalho: {a}divida o total pelo número de partes. [p=0.3] {b}Três mais cinco dá oito partes. [p=0.2] {c}Sessenta e quatro dividido por oito dá oito por parte. [p=0.2] {d}Três partes, vinte e quatro. [p=0.2] {e}Cinco partes, quarenta. [p=0.2] Sem escrever equação. [p=0.3] É o mesmo que tomar {f}três oitavos de sessenta e quatro: [p=0.2] divide por oito, multiplica por três."),
    dict(id="s14", block="atalho", text="Funciona porque {a}somar as partes é o mesmo que juntar os cá: [p=0.2] oito cá, oito partes. [p=0.3] Não compensa quando o problema {b}mistura outras contas, [p=0.2] como o dobro do primeiro mais o segundo. [p=0.2] Aí, {c}escreva com cá e monte a equação."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma massa leva {a}farinha e açúcar na razão cinco para dois. [p=0.2] Juntos, são {b}mil e quatrocentos gramas. [p=0.3] {c}Quantos gramas de açúcar vão na massa?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Farinha é {a}cinco cá. [p=0.2] Açúcar é {b}dois cá. [p=0.2] {c}Sete cá igual a mil e quatrocentos. [p=0.2] {d}Divida por sete: cá igual a duzentos."),
    dict(id="s18", block="resposta", text="Açúcar: {a}dois vezes duzentos dá quatrocentos gramas. [p=0.3] A farinha fica com {b}cinco vezes duzentos dá mil gramas. [p=0.2] Conferindo: {c}mil mais quatrocentos dá mil e quatrocentos. [p=0.2] Bateu. [p=0.3] Pelo atalho: {d}cinco mais dois dá sete partes. [p=0.2] Mil e quatrocentos dividido por sete dá duzentos por parte. [p=0.2] Duas partes de açúcar, {e}quatrocentos gramas."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}na razão três para cinco, os números são três cá e cinco cá. [p=0.2] {b}Ache o cá e multiplique."),
    dict(id="s20", block="fim", text="Na próxima aula, você vê {a}grandezas que andam juntas e grandezas que andam ao contrário, [p=0.2] como {b}quilos e preço, [p=0.2] ou {c}velocidade e tempo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
