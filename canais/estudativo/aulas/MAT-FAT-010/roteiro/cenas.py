# Estudativo · MAT-FAT-010 — Bhaskara com raiz não exata (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: arrumar x(x − 2) = 1 e chegar a x = 1 ± √2, simplificando √8 e dividindo por 2.
# Pré-requisitos: MAT-FAT-008 (Bhaskara), MAT-POT-009 (simplificar radicais). Próxima: MAT-FAT-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o coeficiente a se fala "á".

TITULO = "Bhaskara com raiz não exata"

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
    dict(id="s01", block="gancho", text="{a}Xis, vezes o parêntese xis menos dois, igual a um. [p=0.3] Nenhum número inteiro resolve. [p=0.2] A resposta é {b}um mais raiz de dois, ou um menos raiz de dois. [p=0.3] E não tem nada de errado com ela."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você leva a fórmula de Bhaskara até o fim quando o delta não tem raiz exata, [p=0.2] e ainda ganha {b}um atalho para não errar a divisão final."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}a fórmula de Bhaskara, com o delta primeiro, [p=0.2] e {b}simplificar radicais, tirando as duplas de primos. [p=0.3] Se faltar alguma, procure no canal."),
    # arrumar
    dict(id="s04", block="arrumar", text="Primeiro, {a}arrume a equação. [p=0.2] A fórmula só funciona com {b}tudo de um lado e zero do outro. [p=0.3] {c}Aplique a distributiva: xis ao quadrado menos dois xis igual a um. [p=0.2] {d}Tire um de cada lado: xis ao quadrado menos dois xis menos um igual a zero."),
    dict(id="s05", block="arrumar", text="Agora sim: {a}á vale um, bê vale menos dois, cê vale menos um."),
    # delta
    dict(id="s06", block="delta", text="Delta: {a}abre parênteses, menos dois, fecha parênteses, ao quadrado, quatro. [p=0.2] {b}Quatro vezes um vezes menos um, menos quatro. [p=0.2] {c}Quatro menos, abre parênteses, menos quatro, fecha parênteses: delta igual a oito."),
    dict(id="s07", block="delta", text="Oito não é quadrado de nenhum inteiro: [p=0.2] {a}a raiz de oito não é exata. [p=0.2] Isso não é erro: {b}a conta continua com a raiz. [p=0.2] Siga em frente. [p=0.3] {c}Oito é dois vezes dois vezes dois. [p=0.2] Uma dupla sai, e fica {d}dois raiz de dois."),
    # fórmula
    dict(id="s08", block="formula", text="Na fórmula: {a}xis igual a dois, mais ou menos dois raiz de dois, tudo dividido por dois. [p=0.3] Os termos de cima têm o dois: {b}coloque em evidência. [p=0.2] {c}Dois, vezes o parêntese um mais ou menos raiz de dois, dividido por dois. [p=0.2] {d}Corte o dois de cima com o de baixo."),
    dict(id="s09", block="formula", text="Resposta: {a}xis igual a um mais raiz de dois, [p=0.2] ou {b}xis igual a um menos raiz de dois. [p=0.3] É assim que a resposta aparece nas alternativas: {c}com a raiz, sem vírgula."),
    dict(id="s10", block="sentido", text="Faz sentido? [p=0.2] Raiz de dois vale perto de {a}um vírgula quatro. [p=0.2] As raízes ficam perto de {b}dois vírgula quatro e de menos zero vírgula quatro. [p=0.3] Teste a primeira na equação original: [p=0.2] xis vale dois vírgula quatro, e xis menos dois vale zero vírgula quatro. [p=0.2] {c}Dois vírgula quatro vezes zero vírgula quatro dá zero vírgula noventa e seis. [p=0.2] {d}Quase um. [p=0.2] Com o valor aproximado, quase um é o esperado."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}dividir só um termo por dois. [p=0.2] A pessoa corta o dois do primeiro termo e esquece o outro: [p=0.2] {b}um mais ou menos dois raiz de dois. [p=0.3] Teste com um vírgula quatro: {c}um mais dois vezes um vírgula quatro dá três vírgula oito. [p=0.2] Aí, xis menos dois vale um vírgula oito, [p=0.2] e {d}três vírgula oito vezes um vírgula oito dá quase sete. [p=0.2] Longe de um. [p=0.3] {e}O dividido por dois vale para tudo o que está em cima."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}separe a fração em duas antes de dividir. [p=0.2] {b}Menos bê dividido por dois á: dois dividido por dois dá um. [p=0.2] {c}Raiz de delta dividido por dois á: dois raiz de dois dividido por dois, raiz de dois. [p=0.3] Junte com o mais ou menos: {d}um mais ou menos raiz de dois."),
    dict(id="s13", block="atalho", text="Funciona porque {a}dividir uma soma é dividir cada parte. [p=0.2] Dez reais mais seis reais, divididos entre duas pessoas: [p=0.2] {b}cinco mais três para cada uma, oito. [p=0.3] Separando, {c}nenhum termo fica sem a sua divisão, [p=0.2] e o erro comum não tem como acontecer."),
    dict(id="s14", block="atalho", text="{a}Não compensa quando as partes não dividem certinho, [p=0.2] como em {b}três, mais ou menos raiz de cinco, dividido por dois. [p=0.2] Aí, {c}deixe a fração inteira, do jeito que saiu da fórmula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Resolva {a}xis ao quadrado igual a quatro xis mais um. [p=0.2] Deixe a resposta {b}na forma mais simples."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Tudo para um lado: xis ao quadrado menos quatro xis menos um igual a zero. [p=0.2] {b}Á vale um, bê vale menos quatro, cê vale menos um. [p=0.3] {c}Delta: dezesseis mais quatro dá vinte. [p=0.2] {d}Vinte é quatro vezes cinco: raiz de vinte é dois raiz de cinco."),
    dict(id="s18", block="resposta", text="{a}Quatro, mais ou menos dois raiz de cinco, dividido por dois. [p=0.2] {b}Dois em evidência em cima, e corte com o dois de baixo: [p=0.2] {c}dois mais raiz de cinco, ou dois menos raiz de cinco. [p=0.3] Pelo atalho, separando: {d}quatro dividido por dois dá dois. [p=0.2] {e}Dois raiz de cinco dividido por dois, raiz de cinco. [p=0.2] {f}Dois, mais ou menos raiz de cinco. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}arrume tudo igual a zero, [p=0.2] {b}simplifique a raiz do delta [p=0.2] e {c}divida todos os termos de cima."),
    dict(id="s20", block="fim", text="Na próxima aula, você acha raízes {a}de cabeça, sem fórmula, [p=0.2] como as de {b}xis ao quadrado menos sete xis mais doze, [p=0.2] usando {c}a soma e o produto. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
