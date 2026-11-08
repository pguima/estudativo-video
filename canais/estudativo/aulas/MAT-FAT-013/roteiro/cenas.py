# Estudativo · MAT-FAT-013 — Equações que viram do 2º grau (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: resolver x⁴ − 13x² + 36 = 0 trocando x² por y e 6/x = x − 1 multiplicando por x.
# Pré-requisitos: MAT-FAT-004 (valor proibido), MAT-FAT-011 (soma e produto), MAT-POT-004 (potência de potência). Próxima: MAT-FAT-014.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis", y se escreve "ípsilon".

TITULO = "Equações que viram do 2º grau"

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
    dict(id="s01", block="gancho", text="{a}Xis elevado a quatro, menos treze xis ao quadrado, mais trinta e seis, igual a zero. [p=0.3] Expoente quatro. [p=0.2] Parece outro assunto. [p=0.3] Mas, com {b}uma troca de letra, [p=0.2] vira uma equação do segundo grau que você resolve {c}de cabeça."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você desmonta esse disfarce [p=0.2] e também o de {b}equações com xis embaixo da fração."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}soma e produto, para achar raízes de cabeça, [p=0.2] {c}potência de potência: xis ao quadrado, ao quadrado, é xis elevado a quatro, [p=0.2] e {d}o valor proibido de uma fração com letra. [p=0.3] Se faltar alguma, procure no canal."),
    # biquadrada: troca
    dict(id="s04", block="troca", text="Repare: {a}xis elevado a quatro é xis ao quadrado, ao quadrado. [p=0.2] Então dê um nome novo para {b}xis ao quadrado: ípsilon. [p=0.3] Xis elevado a quatro vira {c}ípsilon ao quadrado. [p=0.2] E a equação vira {d}ípsilon ao quadrado menos treze ípsilon mais trinta e seis igual a zero."),
    dict(id="s05", block="troca", text="Essa você conhece. [p=0.2] {a}Soma treze, produto trinta e seis. [p=0.2] Pelos pares do produto: {b}quatro e nove. [p=0.3] {c}Ípsilon igual a quatro ou ípsilon igual a nove."),
    # biquadrada: volta
    dict(id="s06", block="volta", text="Mas a pergunta é {a}o xis, não o ípsilon. [p=0.2] Volte para a troca. [p=0.3] {b}Xis ao quadrado igual a quatro: xis igual a dois ou menos dois. [p=0.2] {c}Xis ao quadrado igual a nove: xis igual a três ou menos três."),
    dict(id="s07", block="volta", text="São {a}quatro raízes: menos três, menos dois, dois e três. [p=0.3] Conferindo o dois: {b}dezesseis menos cinquenta e dois mais trinta e seis, zero. [p=0.2] Bateu. [p=0.3] Equação assim, com xis elevado a quatro, xis ao quadrado e número, se chama {c}biquadrada."),
    dict(id="s08", block="volta", text="Um cuidado: se o ípsilon der {a}negativo, ele não gera xis nenhum. [p=0.2] Ípsilon é xis ao quadrado, [p=0.2] e {b}número vezes ele mesmo nunca dá negativo."),
    # fração
    dict(id="s09", block="fracao", text="Outro disfarce: {a}seis dividido por xis igual a xis menos um. [p=0.2] Tem xis embaixo da fração. [p=0.3] Antes de tudo, o valor proibido: [p=0.2] {b}xis não pode ser zero."),
    dict(id="s10", block="fracao", text="{a}Multiplique os dois lados por xis. [p=0.2] À esquerda, {b}o xis de baixo some, e fica seis. [p=0.2] À direita, {c}xis vezes o parêntese xis menos um: xis ao quadrado menos xis. [p=0.3] Tudo para um lado: {d}xis ao quadrado menos xis menos seis igual a zero."),
    dict(id="s11", block="fracao", text="{a}Soma um, produto menos seis. [p=0.2] Produto negativo: {b}sinais contrários. [p=0.2] {c}Três e menos dois. [p=0.3] Nenhuma é o zero proibido, então {d}as duas valem."),
    dict(id="s12", block="fracao", text="Conferindo o três: {a}seis dividido por três dá dois, e três menos um também. [p=0.2] O menos dois: {b}seis dividido por menos dois dá menos três, [p=0.2] e menos dois menos um também. [p=0.2] Bateu."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}parar no ípsilon. [p=0.2] Na biquadrada, a pessoa responde {b}quatro e nove. [p=0.3] Teste o quatro no lugar do xis: [p=0.2] {c}duzentos e cinquenta e seis menos duzentos e oito mais trinta e seis dá oitenta e quatro. [p=0.2] Não deu zero. [p=0.3] {d}O ípsilon é só um apoio: sempre volte para o xis."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho da biquadrada: {a}ache só as raízes positivas e espelhe. [p=0.2] Se dois serve, {b}menos dois também. [p=0.3] Funciona porque {c}o xis só aparece com expoente par, [p=0.2] e expoente par apaga o sinal."),
    dict(id="s15", block="atalho", text="{a}Não vale se a equação tiver xis com expoente ímpar, [p=0.2] como {b}xis ao cubo ou xis sozinho. [p=0.2] Na equação da fração, por exemplo, {c}três serve, mas menos três não: [p=0.2] seis dividido por menos três dá menos dois, e menos três menos um dá menos quatro."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Resolva as duas: [p=0.2] {a}xis elevado a quatro, menos dez xis ao quadrado, mais nove, igual a zero. [p=0.3] E {b}xis, mais quatro dividido por xis, igual a cinco. [p=0.2] Nessa, só o quatro fica em cima do xis."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Na primeira, xis ao quadrado vira ípsilon: [p=0.2] {a}ípsilon ao quadrado menos dez ípsilon mais nove igual a zero. [p=0.2] {b}Soma dez, produto nove: um e nove. [p=0.3] Volte para o xis: {c}xis ao quadrado igual a um dá um ou menos um. [p=0.2] {d}Xis ao quadrado igual a nove dá três ou menos três."),
    dict(id="s19", block="resposta", text="Na segunda, {a}xis não pode ser zero. [p=0.2] {b}Multiplique tudo por xis: xis ao quadrado mais quatro igual a cinco xis. [p=0.2] {c}Xis ao quadrado menos cinco xis mais quatro igual a zero. [p=0.3] {d}Soma cinco, produto quatro: um e quatro. [p=0.2] Conferindo o quatro: {e}quatro mais um dá cinco."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}troque xis ao quadrado por ípsilon e volte no fim. [p=0.2] {b}Com xis embaixo, anote o proibido e multiplique por xis."),
    dict(id="s21", block="fim", text="Na próxima aula, você {a}pratica tudo de equação do segundo grau: [p=0.2] escolhe {b}o caminho mais curto para cada uma [p=0.2] e {c}monta a equação a partir de um problema. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
