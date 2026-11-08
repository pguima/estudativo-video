# Estudativo · MAT-PRO-005 — Atalhos da PA: termo do meio e contar termos (Matemática · Progressões · Sequências e PA).
# Habilidade: achar x em 2, x, 10, escrever três termos como x − r, x, x + r e contar quantos múltiplos de 7 têm três algarismos.
# Pré-requisitos: MAT-PRO-004 (razão e termo geral), MAT-DIV-001 (múltiplos). Próxima: MAT-PRO-006.
# Questão inédita, criada para esta aula. Termos como na MAT-PRO-004: razão "erre", saltos, termo geral; PA = "pê á".
# Divisão com resto narrada como na MAT-PRO-003 ("dá catorze, com resto dois"). "Média" explicada na hora: somar os vizinhos e dividir por dois.
# Meio: x − 2 = 10 − x → 2x = 12 → x = 6 · (2 + 10) / 2 = 6.
# Três termos: soma 18, maior = dobro do menor · 3x = 18 → x = 6 · 6 + r = 2(6 − r) → 6 + r = 12 − 2r → 3r = 6 → r = 2 → 4, 6, 8.
# Múltiplos de 7 com 3 algarismos: 100 ÷ 7 = 14 r 2 (98) → 105 · 999 ÷ 7 = 142 r 5 → 994 · 994 = 105 + (n − 1) · 7 → 889 = 7(n − 1) → n − 1 = 127 → n = 128.
# Erro: (994 − 105) / 7 = 127, sem o mais um · 7, 14, 21: (21 − 7) / 7 = 2, mas são 3 termos.
# Atalho: 999 ÷ 7 → 142 · 99 ÷ 7 = 14 r 1 → 142 − 14 = 128. Não compensa em 4, 9, 14 (não são múltiplos de 5).
# Questão: 8, x, 20 → 14 · idades soma 45, mais velho = dobro do mais novo → x = 15 · 15 + r = 30 − 2r → r = 5 → 10, 15, 20
#   · múltiplos de 6 entre 100 e 400: 400 = 6 · 66 + 4 · 99 = 6 · 16 + 3 → 66 − 16 = 50 (atalho como na s15).
# Visual: 2, x, 10 com dois arcos iguais "+4"; três caixas x − r | x | x + r com o −r e o +r riscados na soma (E.formula);
#   reta de números com 105 … 994 e saltos de 7 (postes e espaços: 3 termos, 2 saltos para 7, 14, 21).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Atalhos da PA: termo do meio e contar termos"

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
    dict(id="s01", block="gancho", text="{a}Quantos números de três algarismos são múltiplos de sete? [p=0.3] Listar todos dá trabalho. [p=0.2] Com uma pê á, é {b}uma conta só. [p=0.3] E a resposta, {c}cento e vinte e oito, tem uma armadilha que derruba muita gente."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o termo do meio sem fórmula, [p=0.2] escreve três termos com uma letra só [p=0.2] e conta os termos de qualquer pê á. [p=0.2] E ainda leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}o termo geral da pê á, que soma ao primeiro termo um salto de razão para cada passo, [p=0.2] e {b}múltiplos, os resultados da tabuada de um número. [p=0.3] Se faltar alguma, procure no canal."),
    # termo do meio
    dict(id="s04", block="meio", text="Primeiro, o termo do meio. [p=0.2] A lista {a}dois, [p=0.1] xis, [p=0.1] dez é uma pê á. [p=0.2] Quanto vale o xis? [p=0.3] Na pê á, {b}o salto de dois até xis é igual ao salto de xis até dez."),
    dict(id="s05", block="meio", text="Em equação: {a}xis menos dois igual a dez menos xis. [p=0.2] {b}Passe os xis para um lado e os números para o outro: dois xis igual a doze. [p=0.2] {c}Xis igual a seis. [p=0.3] Confira: {d}dois, [p=0.1] seis, [p=0.1] dez, de quatro em quatro."),
    dict(id="s06", block="meio", text="Repare: {a}dois mais dez dá doze, e dividido por dois dá seis. [p=0.3] {b}O termo do meio é a média dos vizinhos: [p=0.2] some os vizinhos e divida por dois. [p=0.2] Ele fica {c}à mesma distância de cada vizinho."),
    # três termos
    dict(id="s07", block="tres", text="Agora, uma questão clássica. [p=0.2] {a}Três números em pê á somam dezoito, [p=0.2] e {b}o maior é o dobro do menor. [p=0.2] Quais são?"),
    dict(id="s08", block="tres", text="O truque é {a}chamar o do meio de xis. [p=0.2] Os três ficam {b}xis menos erre, [p=0.1] xis [p=0.1] e xis mais erre. [p=0.3] Na soma, {c}o menos erre e o mais erre se cancelam: [p=0.2] {d}três xis igual a dezoito. [p=0.2] {e}Xis igual a seis, de cara."),
    dict(id="s09", block="tres", text="Agora a outra pista. [p=0.2] O maior é o dobro do menor: {a}seis mais erre igual a duas vezes, abre parênteses, seis menos erre. [p=0.3] {b}Seis mais erre igual a doze menos dois erre. [p=0.2] {c}Três erre igual a seis. [p=0.2] {d}Erre igual a dois. [p=0.3] Os números são {e}quatro, [p=0.1] seis [p=0.1] e oito. [p=0.2] E oito é mesmo o dobro de quatro."),
    # contar termos
    dict(id="s10", block="contar", text="Por fim, contar termos. [p=0.2] Qual é o {a}primeiro múltiplo de sete com três algarismos? [p=0.2] {b}Cem dividido por sete dá catorze, com resto dois. [p=0.2] Sete vezes catorze dá noventa e oito, que tem só dois algarismos. [p=0.2] O próximo é {c}cento e cinco."),
    dict(id="s11", block="contar", text="E o {a}último? [p=0.2] {b}Novecentos e noventa e nove dividido por sete dá cento e quarenta e dois, com resto cinco. [p=0.2] {c}Sete vezes cento e quarenta e dois dá novecentos e noventa e quatro. [p=0.3] A lista é uma pê á de razão sete: {d}de cento e cinco até novecentos e noventa e quatro."),
    dict(id="s12", block="contar", text="Use o termo geral com o ene desconhecido: [p=0.2] {a}novecentos e noventa e quatro igual a cento e cinco, mais, abre parênteses, ene menos um, fecha parênteses, vezes sete. [p=0.3] {b}Tire cento e cinco de cada lado: sobra oitocentos e oitenta e nove. [p=0.2] {c}Divida por sete: ene menos um dá cento e vinte e sete. [p=0.2] {d}Ene dá cento e vinte e oito."),
    dict(id="s13", block="contar", text="Resumido numa frase: {a}último menos primeiro, dividido pela razão, mais um. [p=0.3] A divisão conta {b}os saltos. [p=0.2] {c}O mais um conta o primeiro termo, que não precisou de salto."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é {a}esquecer o mais um, e responder {b}cento e vinte e sete. [p=0.3] Teste numa lista pequena: {c}sete, [p=0.1] catorze, [p=0.1] vinte e um. [p=0.2] Vinte e um menos sete, dividido por sete, {d}dá dois. [p=0.2] Mas a lista tem {e}três números. [p=0.2] São dois saltos e três termos."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho, para múltiplos: [p=0.2] {a}conte os que existem até o fim, e tire os que vêm antes do começo. [p=0.3] Até novecentos e noventa e nove, {b}a divisão já deu cento e quarenta e dois. [p=0.2] Até noventa e nove: {c}noventa e nove dividido por sete dá catorze, com resto um. [p=0.2] {d}Cento e quarenta e dois menos catorze dá cento e vinte e oito."),
    dict(id="s16", block="atalho", text="Funciona porque a divisão {a}conta os múltiplos desde o primeiro: sete vezes um, [p=0.1] depois sete vezes dois, [p=0.1] e assim até o quociente. [p=0.3] Não compensa quando a lista {b}não é de múltiplos, como quatro, [p=0.1] nove, [p=0.1] catorze. [p=0.2] Aí, {c}último menos primeiro, dividido pela razão, mais um."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Em oito, [p=0.1] xis, [p=0.1] vinte, que formam uma pê á, quanto vale o xis? [p=0.3] {b}Três irmãos têm idades em pê á que somam quarenta e cinco anos, [p=0.2] e o mais velho tem o dobro da idade do mais novo. [p=0.2] Quais são as idades? [p=0.3] E {c}quantos múltiplos de seis existem entre cem e quatrocentos?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Oito mais vinte dá vinte e oito. [p=0.2] {b}Dividido por dois dá catorze. [p=0.3] Nas idades, o do meio é xis: {c}três xis igual a quarenta e cinco. [p=0.2] Xis igual a quinze. [p=0.2] {d}Quinze mais erre igual a duas vezes, abre parênteses, quinze menos erre. [p=0.2] {e}Três erre igual a quinze, e erre igual a cinco. [p=0.2] {f}Dez, [p=0.1] quinze [p=0.1] e vinte anos."),
    dict(id="s20", block="resposta", text="Nos múltiplos de seis: {a}quatrocentos dividido por seis dá sessenta e seis, com resto quatro. [p=0.2] Os que vêm antes do começo: {b}noventa e nove dividido por seis dá dezesseis, com resto três. [p=0.2] {c}Sessenta e seis menos dezesseis dá cinquenta múltiplos."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}o termo do meio é a média dos vizinhos. [p=0.2] {b}Três termos viram xis menos erre, xis e xis mais erre. [p=0.2] E {c}o número de termos é o número de saltos mais um."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai {a}somar de um até cem em segundos, com a ideia de Gauss, [p=0.2] e calcular {b}o total juntado em trinta dias com uma fórmula. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
