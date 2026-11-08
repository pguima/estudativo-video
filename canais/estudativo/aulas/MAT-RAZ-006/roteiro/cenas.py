# Estudativo · MAT-RAZ-006 — Regra de três direta (Matemática · Razão e Proporção).
# Habilidade: descobrir o preço de 7 kg sabendo que 3 kg custam R$ 18, pela regra de três ou passando pelo preço de 1 kg.
# Pré-requisitos: MAT-RAZ-002 (proporção e produto cruzado), MAT-RAZ-004 (grandezas diretamente proporcionais). Próxima: MAT-RAZ-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. O teste do dobro (MAT-RAZ-005) não está na cadeia: a direta é reconhecida pelo preço por quilo fixo.
# Na tela: tabela de duas colunas (quilos | reais) com o xis na segunda linha.

TITULO = "Regra de três direta"

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
    dict(id="s01", block="gancho", text="{a}Três quilos de carne custam dezoito reais. [p=0.3] {b}Quanto custam sete quilos? [p=0.3] Essa pergunta, com outros números, {c}aparece muito em prova. [p=0.2] E tem dois caminhos para responder."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve qualquer regra de três direta, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}achar o xis numa proporção pelo produto cruzado, [p=0.2] e {c}reconhecer grandezas diretamente proporcionais, em que a divisão não muda. [p=0.3] Se faltar alguma, procure no canal."),
    # montar
    dict(id="s04", block="montar", text="{a}Regra de três é o nome da conta que acha um número a partir de outros três. [p=0.3] Aqui, os três conhecidos são {b}três, dezoito e sete. [p=0.2] O que falta é {c}o xis."),
    dict(id="s05", block="montar", text="{a}Passo um: confira o tipo. [p=0.2] Quilos e preço são {b}diretamente proporcionais: [p=0.2] o preço de um quilo não muda, compre um quilo ou dez. [p=0.2] Mais quilos, mais reais, na mesma medida."),
    dict(id="s06", block="montar", text="{a}Passo dois: monte a tabela, com cada grandeza na sua coluna. [p=0.3] {b}Quilos de um lado, reais do outro. [p=0.2] Na primeira linha, {c}três e dezoito. [p=0.2] Na segunda, {d}sete e xis. [p=0.3] O xis fica {e}na coluna do que você quer descobrir: [p=0.2] aqui, os reais."),
    dict(id="s07", block="montar", text="{a}Passo três: como é direta, as colunas formam uma proporção. [p=0.3] {b}Três está para sete, assim como dezoito está para xis. [p=0.3] Cruz: {c}três xis igual a sete vezes dezoito dá cento e vinte e seis. [p=0.2] {d}Divida por três: xis igual a quarenta e dois reais."),
    # caminho da unidade
    dict(id="s08", block="unidade", text="O segundo caminho passa {a}pelo preço de um quilo. [p=0.3] {b}Dezoito dividido por três dá seis reais o quilo. [p=0.2] {c}Sete quilos, sete vezes seis dá quarenta e dois reais. [p=0.3] O mesmo resultado. [p=0.3] E ele faz sentido: {d}sete quilos é mais que três, [p=0.2] então tem que custar mais que dezoito."),
    dict(id="s09", block="unidade", text="Esse seis é {a}o número que não muda na tabela direta: [p=0.2] {b}preço dividido por quilos. [p=0.2] Na aula das grandezas, ele era o preço do quilo de feijão. [p=0.3] Quando a divisão é exata, esse caminho costuma ser {c}o mais rápido de cabeça."),
    dict(id="s10", block="unidade", text="Mas nem sempre o valor de um sai inteiro. [p=0.2] {a}Quatro metros de mangueira custam trinta reais. [p=0.2] {b}Quanto custam seis metros? [p=0.3] Trinta dividido por quatro não é exato. [p=0.2] Pela cruz: {c}quatro xis igual a seis vezes trinta dá cento e oitenta. [p=0.2] {d}Xis igual a quarenta e cinco reais. [p=0.3] Confira o sentido: {e}mais metros, mais reais."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}deixar unidades diferentes na mesma coluna. [p=0.3] {b}Três metros de tecido custam dezoito reais. [p=0.2] {c}Quanto custam cinquenta centímetros?"),
    dict(id="s12", block="erro", text="Quem monta com {a}três e cinquenta na mesma coluna [p=0.2] chega em {b}trezentos reais. [p=0.2] Mais caro que os três metros inteiros! [p=0.3] Na escada do metro, {c}três metros são trezentos centímetros. [p=0.2] Com {d}trezentos centímetros e cinquenta centímetros na mesma coluna, [p=0.2] dá {e}três reais."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho prometido: {a}divida antes de multiplicar. [p=0.3] Na cruz, você chegou em {b}três xis igual a sete vezes dezoito. [p=0.2] Não faça o cento e vinte e seis. [p=0.2] {c}Divida o dezoito por três primeiro: seis. [p=0.2] {d}Sete vezes seis dá quarenta e dois."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a ordem de multiplicar e dividir não muda o resultado, [p=0.2] e dividir primeiro {b}deixa os números pequenos. [p=0.3] Não compensa quando {c}nenhuma divisão é exata, [p=0.2] como sete vezes vinte dividido por três. [p=0.2] Aí, {d}multiplique primeiro e divida no fim."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma impressora imprime {a}quarenta e cinco páginas em três minutos. [p=0.3] {b}Quantas páginas ela imprime em oito minutos, no mesmo ritmo?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Mais minutos, mais páginas, no mesmo ritmo: {a}direta. [p=0.3] Tabela: {b}três minutos, quarenta e cinco páginas. [p=0.2] {c}Oito minutos, xis páginas. [p=0.3] Cruz: {d}três xis igual a oito vezes quarenta e cinco dá trezentos e sessenta. [p=0.2] {e}Dividido por três dá cento e vinte."),
    dict(id="s18", block="resposta", text="Com o atalho: {a}quarenta e cinco dividido por três dá quinze. [p=0.2] {b}Oito vezes quinze dá cento e vinte páginas. [p=0.3] Esse quinze é {c}quantas páginas saem por minuto: [p=0.2] o caminho da unidade dá o mesmo."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}confira se é direta, [p=0.2] {b}monte a tabela com unidades iguais [p=0.2] e {c}resolva pela cruz ou pelo valor de um."),
    dict(id="s20", block="fim", text="Na próxima aula, a {a}regra de três inversa: [p=0.2] se {b}quatro pintores levam nove dias, quanto tempo levam seis? [p=0.3] Lá, a montagem muda. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
