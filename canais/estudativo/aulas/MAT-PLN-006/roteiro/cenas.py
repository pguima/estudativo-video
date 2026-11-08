# Estudativo · MAT-PLN-006 — Relações de Girard (Matemática · Polinômios · Raízes e relações de Girard).
# Habilidade: dizer sem resolver que as raízes de x³ − 6x² + 11x − 6 = 0 somam 6 e têm produto 6.
# Pré-requisitos: MAT-FAT-011 (soma e produto no grau dois), MAT-PLN-004 (forma fatorada). Próxima: MAT-PLN-007.
# Soma de frações (MAT-FRA-008) não está na ficha: a única conta com fração é 1 + 1/2 = 3/2 (número misto, MAT-FRA-004)
# e −6 · 1/2 = −3 (MAT-FRA-009). Nome falado "Jirár" (na tela, Girard). Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; a, b, c, d se falam "á, bê, cê, dê".

TITULO = "Relações de Girard"

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
    dict(id="s01", block="gancho", text="{a}Xis ao cubo menos seis xis ao quadrado mais onze xis menos seis igual a zero. [p=0.3] {b}Quanto dá a soma das raízes? [p=0.2] E o produto? [p=0.3] {c}Seis e seis. [p=0.2] E nem precisa achar as raízes."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê a soma e o produto das raízes direto dos coeficientes, [p=0.2] com as {b}relações de Jirár."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}soma e produto: em xis ao quadrado mais bê xis mais cê igual a zero, a soma das raízes é menos bê, e o produto é cê; [p=0.2] e {c}a forma fatorada, com um parêntese por raiz. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem
    dict(id="s04", block="origem", text="De onde vem isso? [p=0.2] Pegue um polinômio com raízes {a}um, dois e três. [p=0.2] Na forma fatorada: {b}xis menos um, vezes xis menos dois, vezes xis menos três. [p=0.3] Abrindo tudo, dá {c}xis ao cubo menos seis xis ao quadrado mais onze xis menos seis: [p=0.2] o polinômio do começo."),
    dict(id="s05", block="origem", text="Agora olhe os números. [p=0.2] {a}O seis do xis ao quadrado é um mais dois mais três: a soma das raízes. [p=0.3] {b}O seis do fim é um vezes dois vezes três: o produto. [p=0.3] {c}E o onze é a soma dos produtos de duas em duas: [p=0.2] {d}um vezes dois, mais um vezes três, mais dois vezes três."),
    # a regra
    dict(id="s06", block="regra", text="No grau três, a equação é {a}á xis ao cubo, mais bê xis ao quadrado, mais cê xis, mais dê, igual a zero. [p=0.3] {b}a soma das raízes é menos bê dividido por á. [p=0.2] {c}A soma dos produtos de duas em duas é cê dividido por á. [p=0.2] {d}O produto é menos dê dividido por á."),
    dict(id="s07", block="regra", text="Repare nos sinais: {a}troca, mantém, troca. [p=0.2] Eles vêm dos sinais de menos dentro dos parênteses. [p=0.3] Quando {b}á vale um, é só ler os números: [p=0.2] {c}soma seis, duas em duas onze, produto seis."),
    # com á diferente de um
    dict(id="s08", block="coef_a", text="Com á diferente de um, {a}divida pelo á. [p=0.2] Em {b}dois xis ao cubo menos três xis ao quadrado menos onze xis mais seis igual a zero: [p=0.3] {c}soma: o bê com o sinal trocado, três, dividido por dois: três meios. [p=0.2] {d}Produto: menos seis dividido por dois, menos três."),
    dict(id="s09", block="coef_a", text="As raízes dessa equação são {a}três, menos dois e um meio. [p=0.2] {b}Três menos dois dá um, e um mais um meio é um e meio, que é três meios. [p=0.2] {c}Três vezes menos dois, menos seis, e vezes um meio, menos três. [p=0.2] Bateu."),
    # erro
    dict(id="s10", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer de trocar o sinal do produto. [p=0.2] No grau dois, o produto é o cê, sem trocar. [p=0.2] No grau três, {b}troca. [p=0.3] No polinômio do começo, quem não troca responde {c}menos seis. [p=0.2] Mas {d}um vezes dois vezes três dá seis, positivo."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: {a}uma raiz conhecida, mais Jirár, dá as outras duas de cabeça. [p=0.3] Se {b}um é raiz de xis ao cubo menos seis xis ao quadrado mais onze xis menos seis, [p=0.2] {c}as outras duas somam seis menos um, cinco, [p=0.2] e, como o produto das três é seis, {d}as outras duas multiplicadas dão seis dividido por um, seis. [p=0.3] {e}Soma cinco, produto seis: dois e três."),
    dict(id="s12", block="atalho", text="Funciona porque {a}a soma e o produto valem para as três raízes juntas: [p=0.2] tirando a conhecida, sobra o que falta. [p=0.3] {b}Não compensa se as raízes não forem inteiras: [p=0.2] aí, baixe o grau com Briô-Rufíni e use Bhaskara."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Sem resolver, {a}quanto dão a soma e o produto das raízes [p=0.2] de {b}xis ao cubo menos quatro xis ao quadrado mais xis mais seis igual a zero?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}Á vale um, bê vale menos quatro, cê vale um, dê vale seis. [p=0.3] {b}Soma: o bê com o sinal trocado, quatro. [p=0.2] {c}Produto: o dê com o sinal trocado, menos seis."),
    dict(id="s16", block="resposta", text="Conferindo: as raízes são {a}menos um, dois e três. [p=0.2] {b}Menos um mais dois mais três dá quatro. [p=0.2] {c}Menos um vezes dois vezes três dá menos seis. [p=0.2] Bateu."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo, no grau três: {a}a soma é menos bê dividido por á, [p=0.2] {b}de duas em duas, cê dividido por á, [p=0.2] e {c}o produto, menos dê dividido por á."),
    dict(id="s18", block="fim", text="Na próxima aula, você {a}pratica tudo de polinômios: [p=0.2] {b}divisão, raízes, gráfico e Jirár, [p=0.2] em questões no estilo das provas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
