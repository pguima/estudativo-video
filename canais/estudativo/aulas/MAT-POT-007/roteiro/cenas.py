# Estudativo · MAT-POT-007 — Raiz quadrada: exata e aproximada (Matemática · Potências e Raízes · Radiciação).
# Habilidade: descobrir que √1.764 = 42 fatorando, conferir com 42² e dizer que √20 está entre 4 e 5, perto de 4,5.
# Pré-requisitos: MAT-FRA-014, MAT-POT-004. Próxima: MAT-POT-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# 1.764 → 882 → 441 → 147 → 49 → 7 → 1 = 2·2·3·3·7·7; 2·3·7 = 42; 42 × 40 = 1.680; 42 × 2 = 84; soma 1.764.
# √20: 16 < 20 < 25; meio de 16 e 25 = 20,5; 4,5² = 20,25; 4,4² = 19,36. Valor real ≈ 4,47.
# Erro: √16 ≠ 8 (8² = 64). Atalho: 40² = 1.600, 50² = 2.500, final 4 → 2 ou 8 → 42.
# Questão: 784 → 392 → 196 → 98 → 49 → 7 → 1 = 2·2·2·2·7·7; 2·2·7 = 28; 28² = 784. Inédita.

TITULO = "Raiz quadrada: exata e aproximada"

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
    dict(id="s01", block="gancho", text="{a}Raiz quadrada de mil setecentos e sessenta e quatro. [p=0.3] Parece conta de calculadora. [p=0.3] Mas só com divisões simples, você chega em {b}quarenta e dois."),
    dict(id="s02", block="gancho", text="E quando a raiz não é exata, como a {a}raiz quadrada de vinte, [p=0.2] você descobre {b}um valor bem próximo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você só precisa de {a}três coisas: [p=0.2] {b}elevar ao quadrado, [p=0.2] {c}fatorar em primos [p=0.2] e {d}multiplicar decimais. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="ideia", text="Imagine um {a}piso quadrado com vinte e cinco lajotas. [p=0.2] Quantas lajotas tem cada lado? [p=0.3] {b}Cinco lajotas, porque cinco vezes cinco dá vinte e cinco."),
    dict(id="s05", block="ideia", text="Essa pergunta é a {a}raiz quadrada: [p=0.2] {b}que número, vezes ele mesmo, dá este aqui? [p=0.3] É o caminho de volta de elevar ao quadrado. [p=0.2] {c}A raiz quadrada de vinte e cinco é cinco."),
    dict(id="s06", block="sinal", text="Um detalhe. [p=0.2] {a}Três ao quadrado dá nove. [p=0.2] {b}Menos três entre parênteses, ao quadrado, também dá nove. [p=0.3] Mas o {c}símbolo da raiz escolhe sempre o positivo: [p=0.2] {d}raiz de nove é três, e pronto."),
    # fatorar
    dict(id="s07", block="fatorar", text="E com número grande? [p=0.2] Fatore. [p=0.2] {a}Mil setecentos e sessenta e quatro é par: [p=0.2] {b}por dois dá oitocentos e oitenta e dois. [p=0.2] {c}Por dois de novo dá quatrocentos e quarenta e um."),
    dict(id="s08", block="fatorar", text="Esse é ímpar, e a soma dos algarismos dá nove. [p=0.2] {a}Por três dá cento e quarenta e sete. [p=0.2] {b}Por três de novo dá quarenta e nove. [p=0.2] {c}Por sete dá sete. [p=0.2] {d}Por sete dá um."),
    dict(id="s09", block="duplas", text="Olhe {a}a coluna dos divisores. [p=0.2] Cada primo veio {b}em dupla: [p=0.2] {c}uma dupla de dois [p=0.2] {d}uma de três [p=0.2] e {e}uma de sete."),
    dict(id="s10", block="duplas", text="Raiz quadrada pede {a}dois grupos iguais, porque é um número vezes ele mesmo. [p=0.2] Então cada grupo leva {b}um primo de cada dupla. [p=0.3] {c}Dois vezes três vezes sete dá {d}quarenta e dois."),
    dict(id="s11", block="duplas", text="Sempre confira: {a}quarenta e dois ao quadrado. [p=0.2] {b}Quarenta e dois vezes quarenta dá mil seiscentos e oitenta. [p=0.2] {c}Quarenta e dois vezes dois dá oitenta e quatro. [p=0.2] {d}Somando dá mil setecentos e sessenta e quatro. [p=0.2] Bateu."),
    # estimar
    dict(id="s12", block="estimar", text="E a {a}raiz quadrada de vinte? [p=0.2] Fatorando dá {b}dois vezes dois vezes cinco. [p=0.2] O {c}cinco ficou sem dupla, então a raiz não é exata. [p=0.3] Vamos cercar."),
    dict(id="s13", block="estimar", text="{a}Quatro ao quadrado dá dezesseis. [p=0.2] {b}Cinco ao quadrado dá vinte e cinco. [p=0.2] Vinte fica entre esses resultados, então a {c}raiz de vinte fica entre quatro e cinco."),
    dict(id="s14", block="estimar", text="De dezesseis até vinte são quatro. [p=0.2] De vinte até vinte e cinco são cinco. [p=0.2] Então {a}vinte fica quase no meio. [p=0.2] Teste o meio entre quatro e cinco: {b}quatro vírgula cinco. [p=0.3] {c}Quatro vírgula cinco vezes ele mesmo dá vinte vírgula vinte e cinco. [p=0.2] Passou um pouquinho."),
    dict(id="s15", block="estimar", text="Teste o vizinho: {a}quatro vírgula quatro ao quadrado dá dezenove vírgula trinta e seis, [p=0.2] que fica mais longe de vinte. [p=0.3] Com uma casa decimal, o melhor valor é {b}quatro vírgula cinco, [p=0.2] e ele é aproximado."),
    # erro
    dict(id="s16", block="erro", text="O erro mais comum é {a}dividir por dois. [p=0.2] A pessoa vê {b}raiz de dezesseis e escreve oito. [p=0.3] Mas {c}oito vezes oito dá sessenta e quatro. [p=0.2] O certo é {d}quatro. [p=0.3] Raiz quadrada não é metade. [p=0.2] Só com raiz de quatro a metade acerta, por coincidência."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho para raiz exata de número grande. [p=0.2] Primeiro, {a}cerque com dezenas: [p=0.2] {b}quarenta ao quadrado dá mil e seiscentos [p=0.2] e {c}cinquenta ao quadrado dá dois mil e quinhentos. [p=0.3] A raiz está entre quarenta e cinquenta."),
    dict(id="s18", block="atalho", text="Depois, {a}olhe o final. [p=0.2] Termina em quatro, e só número {b}terminado em dois ou em oito tem quadrado terminado em quatro. [p=0.3] Está bem mais perto de mil e seiscentos, então é {c}quarenta e dois."),
    dict(id="s19", block="atalho", text="Funciona porque {a}o último algarismo do produto depende só dos últimos algarismos. [p=0.3] Mas só serve {b}se a raiz for exata. [p=0.2] Sem essa certeza, {c}fatore."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] {a}Quanto dá a raiz quadrada de setecentos e oitenta e quatro? [p=0.2] Fatore e {b}confira no fim."),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] {a}Por dois dá trezentos e noventa e dois. [p=0.2] {b}Por dois dá cento e noventa e seis. [p=0.2] {c}Por dois dá noventa e oito. [p=0.2] {d}Por dois dá quarenta e nove. [p=0.2] {e}Por sete dá sete. [p=0.2] {f}Por sete dá um."),
    dict(id="s23", block="resposta", text="O número dois apareceu quatro vezes, então são {a}duas duplas. [p=0.2] O sete forma {b}mais uma. [p=0.2] Um primo de cada dupla: {c}dois vezes dois vezes sete dá {d}vinte e oito. [p=0.3] Conferindo: {e}vinte e oito ao quadrado dá setecentos e oitenta e quatro."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}raiz exata sai das duplas de primos, [p=0.2] e {b}raiz não exata você cerca e confere."),
    dict(id="s25", block="fim", text="Na próxima aula, a raiz entra em {a}fração e decimal, [p=0.2] aparece a {b}raiz cúbica [p=0.2] e você descobre o que acontece com {c}número negativo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
